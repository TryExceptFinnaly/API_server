import os, random

from flask import Flask, send_from_directory, render_template
from flask_restful import Api, Resource, request, reqparse
from encode_image import ImageBase64

EXTERNAL_TOKEN = 'Token LookInside'

dicom_studies = [
    {
        'id': 1,
        'study_uid': 'study_uid1',
        'image_uid': 'image_uid1',
        'image': 'images/1.jpg'
    }
]

app = Flask(__name__)
app.logger.setLevel('INFO')
api = Api(app)


class StudyAPI(Resource):
    def get(self, id=0):
        if id == 0:
            return random.choice(dicom_studies), 200
        for study in dicom_studies:
            if study["id"] == int(id):
                return study, 200
        return "study not found", 404

    def post(self):
        app.logger.info(f'Request Headers:\n{request.headers}')
        if request.headers.get('Authorization') != EXTERNAL_TOKEN:
            return f'Uncorrected EXTERNAL_TOKEN!', 400
        parser = reqparse.RequestParser()
        parser.add_argument("study_uid")
        parser.add_argument("image_uid")
        parser.add_argument("image")
        params = parser.parse_args()
        id = dicom_studies[-1]['id'] + 1
        try:
            image_path = ImageBase64.decode(params['image'], f'{os.path.join(app.root_path, f"images/{id}.jpg")}')
        except Exception as exc:
            return f'Params <image> error: {exc}', 400
        study = {
            "id": id,
            "study_uid": params["study_uid"],
            "image_uid": params["image_uid"],
            "image": image_path
        }
        dicom_studies.append(study)
        return study, 201

    def delete(self, id):
        try:
            del dicom_studies[id]
            return f"study with id {id} is deleted.", 200
        except KeyError:
            return f"study with id {id} not found.", 400


api.add_resource(StudyAPI, "/api-external/add-visit-image-to-mediafile", "/api-external/add-visit-image-to-mediafile/",
                 "/api-external/add-visit-image-to-mediafile/<id>")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/api-external/add-visit-image-to-mediafile/<id>/image')
def image(id):
    return send_from_directory(os.path.join(app.root_path, 'images'), f'{id}.jpg')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    # ssl_context=('certificate/cert.pem', 'certificate/key.pem'))
