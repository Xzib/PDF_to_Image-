def pdf_to_imge(path):
    from tesseract_ocr_test import highlight_text
    from PIL import Image
    from pdf2image import convert_from_path
    from Delete_OCR import delete_files
    import pandas as pd
    import os
    os.chdir(os.path.relpath(".\\pdf_files"))
    key_word = input("Enter keyword: ")
    data = {
            'File_Name':[],
            'Key_Word':[],
            'Page_Num':[],
            'Number_Of_Occurances':[],
            'Full_File_Path': [],
            }
    columns = [keys for keys in data.keys()]
    df = pd.DataFrame(columns=columns)
    print(df)
    
    print(df)
    # File_Name= []
    # Key_Word= []
    # Page_Num= []
    # Number_of_Occurences= []
    # Full_File_Path = []
    # x = os.getcwd()
    # print(x)
    # print(os.chdir(os.path.relpath(".\\pdf_files")))
    for path, directories, files in os.walk("."):
        for pdffile in files:
            print(f"inside {pdffile}")
            # print(os.path.abspath(path)) 
            # page_num_list = []
            # print(data['File_Name'][0])
            # print(data['Full_File_Path'][0])
            # file_name = file_name + ".pdf             
            # try:
            # print("inside try")
            images_from_path = convert_from_path(pdffile,dpi=200)
            # print(images_from_path)
            counter = 1
            os.chdir(r"..\pdf_to_jpg")
            # print(os.getcwd())
            for image in images_from_path:
                print(f"######### Converting image = {counter} #######")
                image.save(str(counter)+'_page'+".jpg")
                counter += 1
            new_data=highlight_text(key_word,data,path,pdffile)
            df = df.append(new_data ,ignore_index = True)
            print(new_data)
            os.chdir(r'..\pdf_files')
            delete_files()
            # except:
            #     print("OOPS! Something went wrong.. Are you sure the file is present in the directory") 
            # else:
            #     print ("Operation Finished successfully")
    df.to_csv('..\\key_words.csv', mode = 'a', header=False)

    

if __name__ == "__main__":
    
    path = r"."
    pdf_to_imge(path)

    