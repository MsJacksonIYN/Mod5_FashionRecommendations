# Mod5: Fashion Recommendations

A standalone HTTP web server that can recommend similar fashion outfits, based on the the [Rent the Runway](https://www.renttherunway.com/) inventory.

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

## Built With

* [fast.ai](https://www.fast.ai/) - Deep learning library used for NN training
* [Flask](http://flask.pocoo.org/) - Python HTTP server
* [DeepFashion](http://mmlab.ie.cuhk.edu.hk/projects/DeepFashion.html) - Large-scale Fashion dataset used to train the classifiers

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
