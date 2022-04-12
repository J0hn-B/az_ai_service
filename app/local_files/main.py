#!/usr/bin/env bash

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

import os
import time
import logging
from tabulate import tabulate
import helpers
import image_process


# Loging setup
log = logging.getLogger(__name__)
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"), format='%(asctime)s : %(levelname)s : %(funcName)s : %(message)s',
                    datefmt='%H:%M:%S')


# Parameters
subscription_key = os.getenv('SUBSCRIPTION_KEY')
endpoint = os.getenv('ENDPOINT')

images_folder = os.path.dirname(os.path.abspath(__file__)) + "/../photos"
archive_folder = os.path.dirname(
    os.path.abspath(__file__)) + "/../analysis-archive"
archive_file_name = "record.txt"


def main():

    # Authenticate with the Azure API
    computervision_client = helpers.authenticate_api(
        endpoint, subscription_key)

    # Create the local archive folder if it doesn't exist
    archive_dir = helpers.create_directory(archive_folder)

    # Create the local archive file if it doesn't exist
    archive_record_file = helpers.create_file(archive_dir, archive_file_name)

    # Get the list of images to process from the photos folder
    image_list = helpers.get_files_list(images_folder)

    # Get the image data stream
    image_stream = helpers.get_image_stream(images_folder, image_list)

    # Call the API and record the results in the archive file
    image_process.describe_image_in_stream(
        computervision_client, image_stream, archive_record_file, image_list)


if __name__ == "__main__":
    main()
