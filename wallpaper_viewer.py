from tkinter import *
from PIL import ImageTk,Image
import os

def rotate_img():
    global counter
    img_lable.config(image=img_array[counter%len(img_array)])
    counter=counter+1
counter=1
root=Tk()



root.title("Wallpaper Viewer")
root.configure(bg='black')
root.geometry('300x400')




#heading_functionality
text_lable=Label(root,text="Wallpeper Viewer",bg='black',fg='white')
text_lable.configure(font=('verdana',20))
text_lable.pack(pady=10)



#image_functionality
img_list=os.listdir('E:\Python ZERO to HERO\wallpapers')
img_array=[]
for file in img_list:
    img=Image.open(os.path.join('E:\Python ZERO to HERO\wallpapers',file))
    resized_img=img.resize((250,250))
    img_array.append(ImageTk.PhotoImage(resized_img))
img_lable=Label(root,image=img_array[0])
img_lable.pack(pady=(10,10))



#button_functionality
next_btn=Button(text='Next',bg='white',fg='black',width=18,height=2,command=rotate_img)
next_btn.configure(font=('verdana',10))
next_btn.pack()
root.mainloop()

