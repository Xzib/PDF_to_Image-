def highlight_text(highlight_val):
    from PIL import Image
    import pytesseract
    from pytesseract import Output
    import os
    import cv2

    dir_path= r'.\pdf_to_jpg'
    #os.chdir(dir_path)
    #vocab = ['land','  lease','acres']
    tessdata_dir_config = "--tessdata-dir 'C:\\Program Files\\Tesseract-OCR\\tessdata'"
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    count = 0
    for page in os.listdir('.'):
        img = cv2.imread(page)
        d = pytesseract.image_to_data(img,output_type=Output.DICT,lang='eng', config=tessdata_dir_config)
        n_boxes = len(d['level'])
        overlay = img.copy()
        #user_input = input("What are you looking for: ")
        for i in range(n_boxes):
            text = d['text'][i].lower()
            #print(text)
            if text==highlight_val:
                count+=1
                #highlight the text
                #print('inside if')
                
                '''
                Take the co-ordinates of the text
                '''
                (x,y,w,h) = (d['left'][i],d['top'][i],d['width'][i],d['height'][i])

                '''
                In order to highlight the coressponding text we will increment the counter by 1
                '''
                (x1,y1,w1,h1) = (d['left'][i],d['top'][i],d['width'][i],d['height'][i])
                
                cv2.rectangle(overlay, (x,y),(x1+w1,y1+h1),(255,0,0),-1)
                alpha  = 0.4 
                img_new = cv2.addWeighted(overlay,alpha, img, 1-alpha,0)
                r=1000.0/img_new.shape[1]
                dim=(1000,int(img_new.shape[0]*r))
                resized = cv2.resize(img_new,dim,interpolation=cv2.INTER_AREA)
                cv2.imshow('img',resized)
                cv2.waitKey(500)
                cv2.destroyAllWindows()
                cv2.imwrite(page,img_new)
    return count



