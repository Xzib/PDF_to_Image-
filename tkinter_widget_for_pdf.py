from convert_pdf_to_image import pdf_to_imge
from tesseract_ocr_test import highlight_text
from convert_image_topdf import image_to_pdf
from Delete_OCR import delete_files
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Highlight Pdf Documents")
window.configure(background="black")
'''
grid manager variables
'''
#rows
r = 0




'''
Function for all the buttons
'''

def click():
    file_path = file_name.get()
    value = pdf_to_imge(file_path)
    messagebox.showinfo('Result',value)
    entered_text = text_entry.get()
    messagebox.showinfo('Result',"looking for \'"+entered_text+"\'")
    text_count = highlight_text(entered_text)
    image_to_pdf()
    messagebox.showinfo('Result',"found "+"\'"+str(text_count)+"\'"+" occurances \n"+"View your file in \'imge_to_pdf\' directory")
    delete_files()



    #use this text for getting data from data base or inserting data into database

'''
Widget for Entering the path of the file to highlight text on current page
'''
Label(window,text="File Name",bg="black",fg="white").grid(row=r,column=0,stick=W)
file_name = Entry(window,width=20,bg='white')
file_name.grid(row=r,column=1,stick=W,padx=5,pady=5)
r+=1 #increment row count

'''
Widget for selecting the keyword to highlight text on current page
'''
#Adding entry box label to highlight the text from pages
Label(window,text="Type Text",bg="black",fg="white").grid(row=r,column=0, sticky=W)
#text entry box
text_entry = Entry(window,width=20,bg="white")
text_entry.grid(row=r,column=1,sticky=W,padx=5,pady=5)
r+=1 #increment row count



#Submit Button
Button(window,text="submit",width = 10, command=click).grid(row=r,column=1,stick=W,padx=5,pady=5)


# '''
# Widget for selecting the column of the table
# ''' 
# #adding label for box
# Label(window, text='Select Column',bg="black",fg="white").grid(row=0,column=3,sticky=W)
# #addig selectionbox
# sel_tab = Listbox(window,bg="black",fg='white')
# for i in range(5):
#     sel_tab.insert(i,chr(ord('a')+i))
# sel_tab.grid(row=1,column=3,stick=W)






window.mainloop()