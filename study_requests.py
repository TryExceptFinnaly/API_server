import random
from flask_restful import Api, Resource, reqparse


def api_app(app):
    return Api(app)


dicom_studies = [
    {
        'dicom_uid': '0',
        'image': 'image0',
        'image_uid': 'image_uid0'
    },
    {
        'dicom_uid': '1',
        'image': 'image1',
        'image_uid': 'image_uid1'
    },
    {
        'dicom_uid': '2',
        'image': 'image2',
        'image_uid': 'image_uid2'
    },
    {
        'dicom_uid': '3',
        'image': 'image3',
        'image_uid': 'image_uid3'
    }
]


class StudyAPI(Resource):
    def get(self, dicom_uid=0):
        if dicom_uid == 0:
            return random.choice(dicom_studies), 200
        for study in dicom_studies:
            if study["dicom_uid"] == str(dicom_uid):
                return study, 200
        return "study not found", 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("dicom_uid")
        parser.add_argument("image")
        parser.add_argument("image_uid")
        params = parser.parse_args()
        for study in dicom_studies:
            if params['dicom_uid'] == study["dicom_uid"]:
                return f"study with dicom_uid {id} already exists", 400
        study = {
            "dicom_uid": params["dicom_uid"],
            "image": params["image"],
            "image_uid": params["image_uid"]
        }
        dicom_studies.append(study)
        return study, 201

    def put(self, dicom_uid):
        parser = reqparse.RequestParser()
        parser.add_argument("image")
        parser.add_argument("image_uid")
        params = parser.parse_args()
        for study in dicom_studies:
            if dicom_uid == study["dicom_uid"]:
                study["image"] = params["image"]
                study["image_uid"] = params["image_uid"]
                return study, 200

        study = {
            "dicom_uid": dicom_uid,
            "image": params["image"],
            "image_uid": params["image_uid"]
        }

        dicom_studies.append(study)
        return study, 201

    def delete(self, dicom_uid):
        global dicom_studies
        dicom_studies = [study for study in dicom_studies if study["dicom_uid"] != dicom_uid]
        return f"study with dicom_uid {dicom_uid} is deleted.", 200
