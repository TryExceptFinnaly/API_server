from flask import Flask
from study_requests import StudyAPI, api_app

app = Flask(__name__)
api = api_app(app)

api.add_resource(StudyAPI, "/api-external/add-visit-image-to-mediafile", "/api-external/add-visit-image-to-mediafile/",
                 "/api-external/add-visit-image-to-mediafile/<int:dicom_uid>")
if __name__ == '__main__':
    app.run(debug=True)
