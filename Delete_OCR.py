def delete_files():
    import os
    import shutil
    os.chdir(".\\pdf_to_jpg")
    shutil.rmtree(".")

if __name__ == "__main__":
    delete_files()        