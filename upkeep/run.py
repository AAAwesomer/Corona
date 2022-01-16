import os
from argparse import ArgumentParser
from google.cloud import storage
from dotenv import load_dotenv
load_dotenv()

from upkeep.pipeline import pipeline
import upkeep.model as model
from log import init_logging

LOGGER = init_logging(__name__)
BUCKET = "thecovidmodel"
FUNCTIONS = None


def upload_model(bst, bucket_name, destination_blob_name):
    """Uploads the model to google cloud storage.
    """
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    temp_file = "temp.txt"
    bst.save_model(temp_file)
    blob.upload_from_filename(temp_file)
    LOGGER.info("Model uploaded to {}.".format(destination_blob_name))
    os.remove(temp_file)


def upkeep():
    try:
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
    except KeyError:
        raise KeyError("Env GOOGLE_APPLICATION_CREDENTIALS must be set.")
    LOGGER.info("Running pipeline")
    _, covid_full = pipeline()
    LOGGER.info("Training model")
    bst = model.train(covid_full)
    LOGGER.info("Storing model in cloud storage")
    upload_model(bst, BUCKET, "model.txt")


def parse_args():
    parser = ArgumentParser(description="Run upkeep function")
    parser.add_argument("function", choices=list(FUNCTIONS.keys()),
                        help="Function to run")
    return parser.parse_args()


def main():
    args = parse_args()
    func = FUNCTIONS[args.function]
    func()


if __name__ == "__main__":
    FUNCTIONS = {
        "pipeline": pipeline,
        "upkeep": upkeep,
    }
    main()
    LOGGER.info("Finished.")
    # upload_covid_full()
