import os
import shutil
from rich.console import Console
from rich.prompt import Prompt
# https://docs.python.org/3/library/os.html



console = Console()

# Automate the creation of a folder.
# Write a Python script to create a new folder with a specified name.
def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
        print(f"Folder '{folder_name}' created successfully.")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists.")

# Handle a deleted user.
# user2 is a deleted user and need to move their documents from their user folder to a temporary folder. Your script will create the temporary folder. This will effectively delete the user from the system while still maintaining a record of their documents.
def move_user_documents(username):
    user_folder = f"{username}"
    temp_folder = Prompt.ask("Enter your folder name", default="user")
  

    if not os.path.exists(temp_folder):
        os.mkdir(temp_folder)
        print(f"Temporary folder '{temp_folder}' created successfully.")

    user_documents = os.path.join(user_folder, "Documents")
    temp_documents = os.path.join(temp_folder, username)

    if os.path.exists(user_documents):
        shutil.move(user_documents, temp_documents)
        print(f"User's documents moved to '{temp_documents}' successfully.")
    else:
        print(f"User's documents folder not found.")

# Sort documents into appropriate folders.
# Go through a given folder and sort the documents into additional folders based on their file type.
# Move log files into a logs folder. If a logs folder doesn’t exist, your script should create one.
# Move email files into a mail folder. If a mail folder doesn’t exist, your script should create one.
def sort_documents(source_folder):
    logs_folder = os.path.join(source_folder, "logs")
    mail_folder = os.path.join(source_folder, "mail")

    if not os.path.exists(logs_folder):
        os.mkdir(logs_folder)
        print(f"Logs folder '{logs_folder}' created successfully.")

    if not os.path.exists(mail_folder):
        os.mkdir(mail_folder)
        print(f"Mail folder '{mail_folder}' created successfully.")

    files = os.listdir(source_folder)
    for file in files:
        file_path = os.path.join(source_folder, file)
        if os.path.isfile(file_path):
            if file.endswith(".log"):
                shutil.move(file_path, os.path.join(logs_folder, file))
            elif file.endswith(".eml"):
                shutil.move(file_path, os.path.join(mail_folder, file))

#Parse a log file for errors and warnings.
# From the previous task, you’ve moved a log file into the logs folder. Now, parse the log file for errors and warnings and create two separate log files in a target directory:
# errors.log: Contains all error messages.
# warnings.log: Contains all warning messages.
def parse_log_file(log_file, target_directory):
    errors_log = os.path.join(target_directory, "errors.log")
    warnings_log = os.path.join(target_directory, "warnings.log")

    with open(log_file, "r") as file:
        log_data = file.readlines()

    errors = [line for line in log_data if "error" in line.lower()]
    warnings = [line for line in log_data if "warning" in line.lower()]

    with open(errors_log, "w") as file:
        file.writelines(errors)

    with open(warnings_log, "w") as file:
        file.writelines(warnings)

def count_file_types(directory):
    file_types = {}

    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            file_extension = os.path.splitext(file)[1]
            file_types[file_extension] = file_types.get(file_extension, 0) + 1

    print("File Type Counts:")
    for file_extension, count in file_types.items():
        print(f"{file_extension}: {count}")

def rename_files(source_directory, pattern, replacement):
    files = os.listdir(source_directory)
    for file in files:
        file_path = os.path.join(source_directory, file)
        if os.path.isfile(file_path):
            new_file_name = file.replace(pattern, replacement)
            if new_file_name != file:
                new_file_path = os.path.join(source_directory, new_file_name)
                os.rename(file_path, new_file_path)
                print(f"Renamed '{file}' to '{new_file_name}'.")

def backup_folders(source_directory, destination_directory):
    if not os.path.exists(destination_directory):
        os.mkdir(destination_directory)
        print(f"Backup folder '{destination_directory}' created successfully.")

    folders_to_backup = ["folder1", "folder2", "folder3"]  

    for folder in folders_to_backup:
        source_folder = os.path.join(source_directory, folder)
        destination_folder = os.path.join(destination_directory, folder)

        if os.path.exists(source_folder):
            shutil.copytree(source_folder, destination_folder)
            print(f"Folder '{folder}' backed up successfully.")
        else:
            print(f"Folder '{folder}' not found.")

#menu-driven application
while True:
    print("Automation Tasks:")
    print("1. Create a folder")
    print("2. Move user's documents")
    print("3. Sort documents into appropriate folders")
    print("4. Parse a log file for errors and warnings")
    print("5. Count file types in a directory")
    print("6. Rename files based on a pattern")
    print("7. Backup specific folders")
    print("Q. Exit")

    user_input = input("Enter your choice: ")
    

    if user_input == "1":
        folder_name = input("Enter folder name: ")
        create_folder(folder_name)
    elif user_input == "2":
        username = "user2" 
        move_user_documents(username)
    elif user_input == "3":
        source_folder = input("Enter source folder path: ")
        sort_documents(source_folder)
    elif user_input == "4":
        log_file = input("Enter log file path: ")
        target_directory = input("Enter target directory: ")
        parse_log_file(log_file, target_directory)
    elif user_input == "5":
        directory = input("Enter directory path: ")
        count_file_types(directory)
    elif user_input == "6":
        source_directory = input("Enter source directory: ")
        pattern = input("Enter pattern to replace: ")
        replacement = input("Enter replacement pattern: ")
        rename_files(source_directory, pattern, replacement)
    elif user_input == "7":
        source_directory = input("Enter source directory: ")
        destination_directory = input("Enter destination directory: ")
        backup_folders(source_directory, destination_directory)
    elif user_input == "Q":
        break
    else:
        print("Invalid choice. Please try again.")