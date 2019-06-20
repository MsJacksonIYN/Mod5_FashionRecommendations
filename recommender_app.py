from flask import Flask, request, render_template, url_for, flash, redirect
from predict import Predict
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

p = Predict()

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/home', methods=['GET'])
def render_home():
    return render_template('home.html')


@app.route('/data', methods=['GET'])
def render_data():
    return render_template('project_details.html')


@app.route('/data/model', methods=['GET'])
def render_datamodel():
    return render_template('data_model.html', img=url_for('static', filename='Attributes1000_head_arch.jpg'))


@app.route('/data/eda', methods=['GET'])
def render_dataeda():
    return render_template('data_eda.html')


@app.route('/data/rec-method', methods=['GET'])
def render_datarecmethod():
    return render_template('data_rec_method.html')


@app.route('/resources', methods=['GET'])
def render_resources():
    return render_template('resources.html')


@app.route('/recs', methods=['GET'])
def render_html():
    return render_template('get_inputs.html')


@app.route('/recs', methods=['POST'])
def make_recs():

    if 'img' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['img']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        img_path = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, img_path))

    recs = p.get_recs('static/'+img_path)
    return render_template('show_rec_imgs.html', img_path=url_for('static', filename=img_path), images=recs[0], urls=recs[2])
