# Mod5: Fashion Recommendations

A standalone HTTP web server that can recommend similar fashion outfits, based on the the [Rent the Runway](https://www.renttherunway.com/) inventory.

Uses multiple neural networks (based on ResNet-50) behind the scenes to classify inputs by {category, texture, fabric, parts, shape}. The resulting embeddings are then used to query a pre-built nearest meighbors index for similar outputs.

A live demo is available at [http://fashionrecs.samantha.codes:5560/home](http://fashionrecs.samantha.codes:5560/home)

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

* [fast.ai](https://www.fast.ai/) - Deep learning library used for NN training
* [Flask](http://flask.pocoo.org/) - Python HTTP server
* [DeepFashion](http://mmlab.ie.cuhk.edu.hk/projects/DeepFashion.html) - Large-scale Fashion dataset used to train the classifiers
* [Annoy](https://github.com/spotify/annoy) - Efficient Approximate Nearest Neighbors library

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
