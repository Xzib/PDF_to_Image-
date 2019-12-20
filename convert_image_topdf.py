def image_to_pdf():
    import os
    import shutil
    from PIL import Image
    counter = 0
    im_list = []
 
    for name in os.listdir("."):
        print(counter)
        im = Image.open(name)
        im_list.append(im)
       
        counter += 1
       
    os.chdir("..")
    os.chdir(".\\image_to_pdf")
    pdf1_filename = "highlightedfile.pdf"
    im_list[0].save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True, append_images=im_list[1:])
    os.chdir("..")


if __name__ == "__main__":
    import os
    os.chdir('.\\pdf_to_jpg')
    image_to_pdf()    