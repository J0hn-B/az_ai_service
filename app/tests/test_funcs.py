from app.local_files.helpers import *
import pytest
import os


#### Tests for the archive file ####

# Check that the archive folder and file exists
def test_archive_dir_and_file_exists():
    assert os.path.exists(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))) + "/analysis-archive/record.txt")


# Check the archive folder and file have the correct permissions set
def test_archive_file_write_permissions():
    assert os.access(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))) + "/analysis-archive/record.txt",
        os.W_OK)  # Check for write access

#### Tests for the archive file ####


#### Tests for the list functions ####

# Check that the photos folder exists
def test_images_folder_exists():
    image = os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))) + "/photos"
    assert os.path.exists(image)


# Check the photos folder and have the correct permissions set
def test_images_folder_write_permissions():
    image = os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))) + "/photos"
    assert os.access(image, os.W_OK)  # Check for write access
