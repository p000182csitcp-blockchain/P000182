import base64
import json
from MongoDB.MongoDatabase import MongoDatabase
import os


class Record:
    def __init__(self) -> None:
        self._deployments = MongoDatabase().getDeployment()

    # get all records from mongoDB()
    def get_record(self):
        deployment_records = self._deployments.find()
        for r in deployment_records:

            # loads(): translate str into dict
            db_read = json.loads(r["record"])

            if (r["file_name"] == "RSACertification.json"):
                file_name = "build/contracts/RSACertification.json"
                # dump(): write the data(not str) into file
                with open(file_name, 'w') as fp:
                    json.dump(db_read, fp, indent=4,
                              sort_keys=True, ensure_ascii=False)
            elif (r["file_name"] == "map.json"):
                file_name = "build/deployments/map.json"
                # dump(): write the data(not str) into file
                with open(file_name, 'w') as fp:
                    json.dump(db_read, fp, indent=4,
                              sort_keys=True, ensure_ascii=False)
            else:
                file_name = "build/deployments/5/" + r["file_name"]
                # dump(): write the data(not str) into file
                with open(file_name, 'w') as fp:
                    json.dump(db_read, fp)

    # get all local records'name(y)

    def get_local_record_list(self):
        arr = next(os.walk('./build/deployments/5'))[2]
        local_records = set()
        for file in arr:
            local_records.add(file)
        return local_records

    # storage a new record on mongoDB(y)
    def new_record_file(self, file_name):

        # load(): open the json file and translate the str into datatype
        with open(file_name, 'r') as fp:
            file_read = json.load(fp)

        # dumps(): translate the dict into str
        record = json.dumps(file_read)

        # mql for creating new document in Deployment collection
        new_deployment = {
            "file_name": file_name.split("/")[-1],
            "record": record
        }

        # run the mql on Deployment collections
        self._deployments.insert_one(new_deployment)

    # update records into mongoDB(y)
    def update_records(self) -> None:
        try:
            self.clean_records()
            RSACertification_path = "build/contracts/RSACertification.json"
            map_path = "build/deployments/map.json"
            local_records = self.get_local_record_list()
            # db_records = self.get_db_record_list()

            # insert all records' file into database
            for record in local_records:
                record_filename = "build/deployments/5/" + record
                self.new_record_file(record_filename)

            self.new_record_file(RSACertification_path)
            self.new_record_file(map_path)

        except Exception:
            print("There is somthing wrong on updating records")

    # clean the Deployment collection(y)
    def clean_records(self) -> None:
        self._deployments.delete_many({})
