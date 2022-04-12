from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
import os
import logging

log = logging.getLogger(__name__)


# Function to authenticate with the API
def authenticate_api(endpoint: str, subscription_key: str):
    # Access the Computer Vision client.
    computervision_client = ComputerVisionClient(
        endpoint, CognitiveServicesCredentials(subscription_key))
    log.info(endpoint)
    return computervision_client


# Function to create directory
def create_directory(directory: str):
    if not os.path.exists(directory):
        os.makedirs(directory)
        log.info(directory)
    return directory


# Function to create file if it doesn't exist
def create_file(directory: str, file_name: str):
    if not os.path.exists(os.path.join(directory, file_name)):
        file = open(os.path.join(directory, file_name), "a+")
        file.close()
        log.info(os.path.join(directory, file_name))
    return os.path.join(directory, file_name)


# Function to return a list of files to process
def get_files_list(directory: str):
    files_list = []
    for file in os.listdir(directory):
        files_list.append(file)
        log.info(file)
    return files_list


# Function to return image data stream
def get_image_stream(directory: str, files_list: str):
    image_data = []
    for image in files_list:
        image_path = os.path.join(directory, image)
        image_ob = open(image_path, "rb")
        image_data.append(image_ob)
        log.info(image_path)
    return image_data
