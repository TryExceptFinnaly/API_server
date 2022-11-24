import os

from flask import Flask, send_from_directory, render_template
from study_requests import StudyAPI, api_app

app = Flask(__name__)
api = api_app(app)

api.add_resource(StudyAPI, "/api-external/add-visit-image-to-mediafile", "/api-external/add-visit-image-to-mediafile/",
                 "/api-external/add-visit-image-to-mediafile/<dicom_uid>")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/api-external/add-visit-image-to-mediafile/<dicom_uid>/image')
def image(dicom_uid):
    return send_from_directory(os.path.join(app.root_path, 'images'), f'{dicom_uid}.jpg')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    # ssl_context=('certificate/cert.pem', 'certificate/key.pem'))
