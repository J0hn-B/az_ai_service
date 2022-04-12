import logging
import os
from tabulate import tabulate


log = logging.getLogger(__name__)


# Call API
def describe_image_in_stream(computervision_client, image_stream, path, image_list):
    for image_s in image_stream:
        description_results = computervision_client.describe_image_in_stream(
            image_s)
        for caption in description_results.captions:
            log.info(caption)
            if (len(description_results.captions) == 0):
                print("No description detected.")
            else:
                for file in image_list:
                    with open(path, "r") as record_file:
                        if(file in record_file.read()):
                            continue
                        else:
                            with open(path, "a+") as record_file:
                                log.info("Recorded: " + file +
                                         ": " + caption.text)
                                record_file.write(tabulate([['File:', file], ['Confidence:', "{:.2f}%".format(
                                    caption.confidence * 100)], ['Description:', caption.text]], numalign="right", tablefmt='simple', showindex=False))
                                record_file.close()
                                break
