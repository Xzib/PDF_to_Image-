def delete_files():
    import os
    import shutil
    os.chdir(r"..\pdf_to_jpg")        
    list_name = [name for name in os.listdir(".")]
    for i in list_name:
        os.remove(i)
    os.chdir(r"..\pdf_files")


if __name__ == "__main__":
    delete_files()        