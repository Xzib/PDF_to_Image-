from tkinter import *
window = Tk()
window.title("Highlight Pdf Documents")
window.configure(background="black")

'''
Function for all the buttons
'''

def click():
    entered_text = text_entry.get()
    #use this text for getting data from data base or inserting data into database

'''
Widget for Entering the path of the file to highlight text on current page
'''
  


'''
Widget for selecting the keyword to highlight text on current page
'''
#Adding entry box label to highlight the text from pages
Label(window,text="Type Text",bg="black",fg="white").grid(row=0,column=0, sticky=W)
#text entry box
text_entry = Entry(window,width=20,bg="white")
text_entry.grid(row=1,column=0,sticky=W)
#Submit Button
Button(window,text="Hightlight",width = 10, command=click).grid(row=2,column=0,stick=W)

'''
Widget for selecting the column of the table
''' 
#adding label for box
Label(window, text='Select Column',bg="black",fg="white").grid(row=0,column=3,sticky=W)
#addig selectionbox
sel_tab = Listbox(window,bg="black",fg='white')
for i in range(5):
    sel_tab.insert(i,chr(ord('a')+i))
sel_tab.grid(row=1,column=3,stick=W)






window.mainloop()