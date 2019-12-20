def pdf_to_imge(path):
    from PIL import Image
    from pdf2image import convert_from_path
    import os
        
        
    images_from_path = convert_from_path(path)
    counter = 1
    os.chdir(r".\pdf_to_jpg")
    for image in images_from_path:
        
        image.save('page_'+str(counter)+".jpg")
        counter += 1



    # Do something here