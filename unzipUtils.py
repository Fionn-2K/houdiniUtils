import os
import zipfile
import threading

DIRPATH = "C:\\Users\\fionn.sherrard\\Downloads\\assets\\zip_test"

class UnzipUtils:
    def __init__(self, ditpath):
        self.dirpath = ditpath

    def unzipAll(self):
        zipfiles = [file for file in os.listdir(self.dirpath) if file.endswith(".zip")]
        if len(zipfiles) > 0:
            for zipf in zipfiles:
                with zipfile.ZipFile(self.dirpath + "/" + zipf, "r") as zip_ref:
                    zip_ref.extractall(self.dirpath)
                print(f"Done Extracting {zipf}")
            print("All files unzipped")
        else:
            print(f"No zip files found in {self.dirpath}")

    def deleteZipFiles(self):
        zipfiles = [file for file in os.listdir(self.dirpath) if file.endswith(".zip")]
        if len(zipfiles) > 0:
            for zipf in zipfiles:
                print (f"{zipf} deleted!")
                os.remove(self.dirpath + "/" + zipf)
        else:
            print(f"No zip files found in {self.dirpath}")

if __name__ == "__main__":
    folder1 = UnzipUtils(DIRPATH)

    threading1 = threading.Thread(target=folder1.unzipAll())
    threading2 = threading.Thread(target=folder1.deleteZipFiles())

    ## 1 = unzip files, 2 = delete zip files
    threading1.start()
    threading1.join()
    threading2.start()