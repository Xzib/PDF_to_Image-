def pdf_to_imge(path):
    from PIL import Image
    from pdf2image import convert_from_path
    import os
    os.chdir(os.path.relpath(".\\pdf_files"))
    # x = os.getcwd()
    # print(x)
    # print(os.chdir(os.path.relpath(".\\pdf_files")))
    for path, directories, files in os.walk("."):
        for file in files:
            print(file)
            # file_name = file_name + ".pdf"
                
            # try:
            #     images_from_path = convert_from_path(os.path.abspath(file),dpi=500)
            #     counter = 1
            #     os.chdir(r".\pdf_to_jpg")
            #     for image in images_from_path:
            #         image.save(str(counter)+'_page'+".jpg")
            #         counter += 1
            # except:
            #     return "OOPS! Something went wrong.. Are you sure the file is present in the directory"
            # else:
            #     return "Operation Finished successfully"


    

if __name__ == "__main__":
    
    path = r"."
    pdf_to_imge(path)

    