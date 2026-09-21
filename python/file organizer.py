import os
import shutil

categories = {
    "Images": {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff', '.tif', '.svg', '.ico', '.heic', '.heif'},

    "Documents": {'.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.csv', '.ppt', '.pptx', '.odp'},

    "Videos": {'.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm', '.m4v', '.mpeg', '.mpg', '.3gp'},

    "Music": {'.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a', '.wma', '.opus'},

    "Archives": {'.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.tar.gz', '.tar.xz'},

    "Programs": {'.exe', '.msi', '.bat', '.cmd', '.com'},

    "Code": {'.py', '.pyw', '.js', '.ts', '.html', '.htm', '.css', '.json', '.xml', '.yaml', '.yml', '.c', '.h', '.cpp', '.hpp', '.java', '.cs', '.php', '.sql', '.sh', '.ps1'}
}
download_path = os.listdir(r"C:\Users\EXO\Downloads")

def create_folder(base_path, category):
    folder_path = os.path.join(base_path, category)
    os.makedirs(folder_path, exist_ok=True)
    return folder_path

def get_category(extension):
    for category, extensions in categories.items():
        if extension in extensions:
            return category

    return 'Other'

for file in download_path:
    file_path = os.path.join(r"C:\Users\EXO\Downloads", file)

    if os.path.isfile(file_path):

        filename = os.path.basename(file_path)
        name, extension= os.path.splitext(filename)
        extension = extension.lower()

        category_found = get_category(extension)

        category_path = create_folder(r"C:\Users\EXO\Downloads", category_found)

        destination_path = os.path.join(category_path, file)

        if os.path.exists(destination_path):
            counter = 1
            new_filename = f"{name}_{counter}{extension}"
            new_destination = os.path.join(category_path, new_filename)
            while os.path.exists(new_destination):
                counter += 1
                new_filename = f"{name}_{counter}{extension}"
                new_destination = os.path.join(category_path, new_filename)
            shutil.move(file_path, new_destination)

        else:
            shutil.move(file_path, category_path)