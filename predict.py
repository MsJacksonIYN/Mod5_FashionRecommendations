import pandas as pd
import os

from fastai import *
from fastai.vision import *
from fastai.callbacks import *

from annoy import AnnoyIndex


class Predict():
    def __init__(self):
        print("About to download")
        data_path = untar_data(
            'https://womens-fashion-recommender.s3.us-east-2.amazonaws.com/models', data=False)
        print("Finished downloading")
        data_path = os.path.abspath(os.path.join(data_path, os.pardir))
        cat_learner = load_learner(
            path=data_path, file='cat-rn50-size150-fr4-unfr2-fr4-unfr4.pkl')
        texture_learner = load_learner(
            path=data_path, file='texture-resnet50-size150-fr12-unfr4.pkl')
        fabric_learner = load_learner(
            path=data_path, file='fabric-resnet50-size150-fr5-unfr4.pkl')
        parts_learner = load_learner(
            path=data_path, file='parts-resnet50-size150-fr5-unfr4.pkl')
        shape_learner = load_learner(
            path=data_path, file='shape-resnet50-size150-fr5-unfr4.pkl')
        self.all_cnns = [cat_learner, texture_learner,
                         fabric_learner, parts_learner, shape_learner]

        self.rtr_inventory = AnnoyIndex(512*len(self.all_cnns))
        self.rtr_inventory.load(os.path.join(
            data_path, 'rtr_inventory_5cnn.ann'))
        with open(os.path.join(data_path, 'rtr_images.pkl'), 'rb') as f:
            self.rtr_images = pickle.load(f)
        self.rtr_df = pd.read_csv(os.path.join(
            data_path, 'rtr_df.csv'), index_col='img_name')

    # returns the embeddings for a single image,
    # from a single given CNN's last FC layer
    def get_embeddings_for_image(self, cnn, img_path):
        hook = hook_output(cnn.model[-1][-3])
        cnn.predict(open_image(img_path))
        hook.remove()
        return hook.stored.cpu()[0]

    # returns the concatenated embeddings for a single image,
    # from the given list of CNNs' last FC layer
    def get_combined_embeddings_for_image(self, img_path):
        embeddings = []
        for cnn in self.all_cnns:
            embeddings.append(self.get_embeddings_for_image(cnn, img_path))
        return np.concatenate(embeddings)

    # queries the given vector against the given ANN index
    def query_ann_index(self, embeddings, n=5):
        nns = self.rtr_inventory.get_nns_by_vector(
            embeddings, n=n, include_distances=True)
        img_paths = [self.rtr_images[i] for i in nns[0]]
        return img_paths, nns[1]

    # Get and display recs
    def get_recs(self, img_path, n=5):
        embedding = self.get_combined_embeddings_for_image(img_path)
        img_paths, sim_scores = self.query_ann_index(embedding, n)
        urls = [self.rtr_df.loc[img]['url'] for img in img_paths]
        return img_paths, sim_scores, urls
