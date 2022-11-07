import base64
from MongoDB.MongoDatabase import MongoDatabase
import os


class Record:
    def __init__(self) -> None:
        pass

    # get all records from mongoDB(y)
    def get_record(self):
        mDb = MongoDatabase()
        deployments = mDb.getDeployment()
        deployment_records = deployments.find()
        for r in deployment_records:
            record = base64.b64decode(r["record"])
            file_name = "build/deployments/5/" + r["file_name"]
            with open(file_name, 'wb') as fp:
                fp.write(record)

    # get all local records'name(y)
    def get_local_record_list(self):
        arr = next(os.walk('./build/deployments/5'))[2]
        local_records = set()
        for file in arr:
            local_records.add(file)
        return local_records

    # get all records'name from mongoDB(y)
    def get_db_record_list(self):
        mDb = MongoDatabase()
        deployments = mDb.getDeployment()
        deployment_records = deployments.find()
        records_list = set()
        for records in deployment_records:
            records_list.add(records["file_name"])
        return records_list

    # storage a new record on mongoDB(y)
    def new_record(self, file_name):
        mDb = MongoDatabase()
        deployments = mDb.getDeployment()

        with open(file_name, 'rb') as fp:
            record = base64.b64encode(fp.read())

        # mql for creating new document in Deployment collection
        new_deployment = {
            "file_name": file_name.split("/")[-1],
            "record": record
        }

        # run the mql on Deployment collections
        deployments.insert_one(new_deployment)

    # update records in mongoDB(y)
    def update_records(self) -> None:
        try:

            local_records = self.get_local_record_list()
            db_records = self.get_db_record_list()

            # creating the difference of the two sets
            diff_records = local_records - db_records

            # insert the different records into database
            for record in diff_records:
                filename = "build/deployments/5/" + record
                self.new_record(filename)
        except Exception:
            print("There is somthing wrong on updating records")
