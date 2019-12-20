def pdf_to_imge(path):
    from PIL import Image
    from pdf2image import convert_from_path
    import os
    path = path + ".pdf"
        
    try:
        images_from_path = convert_from_path(os.path.abspath(path))
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
    path = r"D:\Zohaib\Fivrr\pdf_to_image\PDF_to_Image-\file-example_PDF_1MB.pdf"
    pdf_to_imge(path)

    