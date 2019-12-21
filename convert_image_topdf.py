def image_to_pdf():
    import os
    import shutil
    from PIL import Image

    def sort_list(list_name):
        temp = ""
        for i in range(len(list_name)):
            for j in range(i+1,len(list_name)):
                if int(list_name[i].split("_")[0])>int(list_name[j].split("_")[0]):
                    temp= list_name[j]
                    list_name[j]=list_name[i]
                    list_name[i] = temp
        return list_name 





    counter = 0
    im_list = []
    name_list = [name for name in os.listdir(".")]
    #sorted_names = list(map(sort_list,name_list))
    sorted_list = sort_list(name_list)
    print(sorted_list)
 
    for name in sorted_list:
        #print(counter) 
        im = Image.open(name)
        im_list.append(im)
        counter += 1
    print(im_list)
       
    os.chdir("..")
    os.chdir(".\\image_to_pdf")
    pdf1_filename = "highlightedfile.pdf"
    im_list[0].save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True, append_images=im_list[1:])
    os.chdir("..")


if __name__ == "__main__":
    import os
    os.chdir('.\\pdf_to_jpg')
    image_to_pdf()    