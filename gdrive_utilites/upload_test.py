from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class GDriveUpload:
    def __init__(self):
        pass

    ## Authenticate Google API
    def authenticate(self):
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        return GoogleDrive(gauth)

    ## Check if folder exists return it ID
    def get_folder_id(self, drive, folder_name):
        ## Get all folders in Google Drive, exclude those in trash
        file_list = drive.ListFile({'q': f"title='{folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
        if len(file_list) > 0:
            print(f"{folder_name} folder found.")
            return file_list[0]['id']
        else:
            ## If no folder found with folder_name, create a new folder with said name
            print(f"No folder with the name {folder_name} found! New folder created.")
            new_folder = self.create_folder(drive, folder_name)
            return new_folder['id']

    ## Create folder if it does not exist, then return
    def create_folder(self, drive, folder_name):
        folder_metadata = {
            'title': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        folder = drive.CreateFile(folder_metadata)
        folder.Upload()
        return folder

    # Upload sample file
    def upload_file(self, drive, upload_file, folder_id):
        file = drive.CreateFile(
            {
                'parents': [{'id': folder_id}]
            }
        )
        file.SetContentFile(upload_file)
        file.Upload()
        print("File uploaded")

## TEST CODE
if __name__ == "__main__":
    gu = GDriveUpload()
    gdrive = gu.authenticate()

    if gdrive is not None:
        dest_folder_id = gu.get_folder_id(gdrive, "Rebelway")
        gu.upload_file(gdrive, 'cat_image.jpg', dest_folder_id)
    else:
        print("Google drive not authenticated! Failed to upload file")
