import base64
from MongoDB.MongoDatabase import MongoDatabase


class Record:
    def __init__(self) -> None:
        pass

    # get all records from mongoDB
    def get_record(self):
        mDb = MongoDatabase()
        deployments = mDb.getDeployment()
        deployment_records = deployments.find()
        for r in deployment_records:
            record = base64.b64decode(r["record"])
            file_name = "deployment/" + r["file_name"]
            with open(file_name, 'wb') as fp:
                fp.write(record)

    # storage a new record on mongoDB
    def new_record(self, file_name):
        mDb = MongoDatabase()
        deployments = mDb.getDeployment()

        with open(file_name, 'rb') as fp:
            record = base64.b64encode(fp.read())

        # mql for creating new document in Deployment collection
        new_deployment = {
            "file_name": file_name,
            "record": record
        }

        # run the mql on Deployment collections
        deployments.insert_one(new_deployment)
