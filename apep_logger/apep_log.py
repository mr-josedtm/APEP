from apep_core.apep_input import ApepInput
from apep_core.apep_output import ApepOutput

from pymongo import MongoClient


def save_to_mongo(apep_output: ApepOutput):
    client = MongoClient("mongodb://root:example@localhost:27017/")

    db = client["test_database"]

    collection = db["apep_log"]

    doc_to_save = apep_output.metadata.get_metadata_doc()

    i_id = collection.insert_one(doc_to_save).inserted_id

    client.close()
