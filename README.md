# Mod5: Fashion Recommendations

A standalone HTTP web server that can recommend similar fashion outfits, based on the the [Rent the Runway](https://www.renttherunway.com/) inventory.

Uses multiple neural networks (with a ResNet50 backbone) behind the scenes to classify inputs by {category, texture, fabric, parts, shape}. The resulting embeddings are then used to query a pre-built nearest neighbors index for similar outputs.

To try the recommendation system without cloning the repo, see this [live demo](https://fashionrecs.samantha.codes/home)

## Installation

Use [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip install -r requirements.txt
```

## Usage

To run the web server, simply execute flask with the main recommender app:

```sh
FLASK_APP=recommender_app flask run
```

The main predictor can also be used independently of Flask, by calling `get_recs`:

```python
from predict import Predict

fashion = Predict()
recs = fashion.get_recs(img_path)
```

## Built With

* [fast.ai](https://www.fast.ai/) - Deep learning library used for CNN training
* [Flask](http://flask.pocoo.org/) - Python HTTP server
* [DeepFashion](http://mmlab.ie.cuhk.edu.hk/projects/DeepFashion/AttributePrediction.html) - Large-scale Fashion dataset used to train the classifiers
* [Annoy](https://github.com/spotify/annoy) - Efficient Approximate Nearest Neighbors library

## Files
* [Notebooks_CNNs](https://github.com/MsJacksonIYN/Mod5_FashionRecommendations/tree/master/Notebooks_CNNs) - Source code (.ipynb) for training CNNs
* [Notebooks_Recommender](https://github.com/MsJacksonIYN/Mod5_FashionRecommendations/tree/master/Notebooks_Recommender) - Source code (.ipynb) for building Annoy index and recommendations
* [Outfits](https://github.com/MsJacksonIYN/Mod5_FashionRecommendations/tree/master/Outfits) - Example images that can be used to test the recommendation system 
* [recommender_app.py](https://github.com/MsJacksonIYN/Mod5_FashionRecommendations/blob/master/recommender_app.py) - Spins up a Flask App to serve recommendations 
* [predict.py](https://github.com/MsJacksonIYN/Mod5_FashionRecommendations/blob/master/predict.py) - Recommendation System

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
