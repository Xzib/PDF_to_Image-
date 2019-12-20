def pdf_to_imge(file_name):
    from PIL import Image
    from pdf2image import convert_from_path
    import os
    file_name = file_name + ".pdf"
        
    try:
        print(os.path.relpath(file_name))
        images_from_path = convert_from_path(os.path.relpath(file_name))
        print(images_from_path)
        counter = 1
        os.chdir(r".\pdf_to_jpg")
        for image in images_from_path:
            
            image.save('page_'+str(counter)+".jpg")
            counter += 1

    except:
        return "OOPS! Something went wrong.. Are you sure the file is present in the directory"
    else:
        return "Operation Finished successfully"


    

if __name__ == "__main__":
    file_name = "lease_example"
    pdf_to_imge(file_name)

    