import io
import requests
from tkinter import *
from PIL import ImageTk,Image
import webbrowser
from urllib.request import urlopen

class NewsApp:

    def __init__(self):
        self.data=requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=55a7e9bb81cc4fb5b3661e5d2ec8b374').json()
        self.load_gui()
        self.get_news_items(0)

    def load_gui(self):
        self.root=Tk()
        self.root.geometry('350x600')
        self.root.resizable(0,0)
        self.root.title('NewsApp')
        self.root.config(background='black')

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()


    def get_news_items(self,index):
        self.clear()
        try:
            img_url=self.data['articles'][index]['urlToImage']
            raw_data=urlopen(img_url).read()
            im=Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo=ImageTk.PhotoImage(im)
        except:
            img_url = 'https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg'
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)

        label=Label(self.root,image=photo)
        label.pack()



        Heading=Label(self.root,text=self.data['articles'][index]['title'],bg='black',fg='white',
                      wraplength=350,justify='center')
        Heading.pack(pady=(10,20))
        Heading.config(font=('verdana',15))

        Description = Label(self.root, text=self.data['articles'][index]['description'], bg='black', fg='white',
                        wraplength=350, justify='center')
        Description.pack(pady=(2, 20))
        Description.config(font=('verdana', 12))

        frame=Frame(self.root,bg='black')
        frame.pack(expand=True,fill=BOTH)

        if index != 0:
            prev=Button(frame,text='Previous',width=16,height=3,command=lambda :self.get_news_items(index-1))
            prev.pack(side=LEFT)

        rm = Button(frame, text='Read More', width=16, height=3,command=lambda :self.open_link(self.data['articles'][index]['url']))
        rm.pack(side=LEFT)

        if index !=len(self.data['articles'])-1:
            next = Button(frame, text='Next', width=16, height=3,command=lambda : self.get_news_items(index+1))
            next.pack(side=LEFT)

        self.root.mainloop()
    def open_link(self,url):
        webbrowser.open(url)













obj=NewsApp()