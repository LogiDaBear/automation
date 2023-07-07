import os
import shutil
from automation import create_folder

def test_create_folder():
    folder_name = "TestFolder"
    create_folder(folder_name)
    assert os.path.exists(folder_name)
    assert os.path.isdir(folder_name)

def test_create_folder_already_exists():
    folder_name = "ExistingFolder"
    os.mkdir(folder_name)
    create_folder(folder_name)
    assert os.path.exists(folder_name)
    assert os.path.isdir(folder_name)

def test_move_user_documents():
    username = "user2"
    temp_folder = "temp_folder"
    user_documents_folder = os.path.join("path/to/users", username, "Documents")
    temp_documents_folder = os.path.join(temp_folder, username)

    os.mkdir(temp_folder)
    os.mkdir(user_documents_folder)


    assert os.path.exists(temp_documents_folder)
    assert os.path.isdir(temp_documents_folder)

    os.rmdir(temp_documents_folder)
    os.rmdir(temp_folder)
    os.rmdir(user_documents_folder)

# Run the tests
test_create_folder()
test_create_folder_already_exists()
test_move_user_documents()
