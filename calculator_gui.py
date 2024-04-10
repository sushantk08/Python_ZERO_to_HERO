from tkinter import *

first_number=second_number=operator=None
def get_digit(digit):
    current=text_lable['text']
    new=current+str(digit)
    text_lable.config(text=new)

def clr():
    text_lable.config(text='')

def get_operator(op):
    global first_number,operator
    first_number=int(text_lable['text'])
    operator=op
    text_lable.config(text='')

def get_result():
    global first_number,second_number,operator
    second_number=int(text_lable['text'])
    if operator=='+':
        text_lable.config(text=str(first_number+second_number))
    elif operator=='-':
        text_lable.config(text=str(first_number-second_number))
    elif operator=='*':
        text_lable.config(text=str(first_number*second_number))
    else:
        if second_number==0:
            text_lable.config(text='Error')
        else:
            text_lable.config(text=str(round(first_number/second_number,2)))


root=Tk()
root.geometry('280x380')
root.resizable(0,0)
root.configure(background='black')
root.title('Calculator')

text_lable=Label(root,text='',background='black',fg='white')
text_lable.grid(row=0,column=0,pady=(50,25),columnspan=5,sticky='w')
text_lable.configure(font=('verdana',30,'bold'))

btn_7=Button(root,text='7',width=5,height=2,command=lambda : get_digit(7))
btn_7.grid(row=1,column=0)
btn_7.configure(font=('verdana',14))

btn_8=Button(root,text='8',width=5,height=2,command=lambda : get_digit(8))
btn_8.grid(row=1,column=1)
btn_8.configure(font=('verdana',14))

btn_9=Button(root,text='9',width=5,height=2,command=lambda : get_digit(9))
btn_9.grid(row=1,column=2)
btn_9.configure(font=('verdana',14))

btn_add=Button(root,text='+',width=5,height=2,command=lambda :get_operator('+'))
btn_add.grid(row=1,column=3)
btn_add.configure(font=('verdana',14))

btn_6=Button(root,text='6',width=5,height=2,command=lambda : get_digit(6))
btn_6.grid(row=2,column=0)
btn_6.configure(font=('verdana',14))

btn_5=Button(root,text='5',width=5,height=2,command=lambda : get_digit(5))
btn_5.grid(row=2,column=1)
btn_5.configure(font=('verdana',14))

btn_4=Button(root,text='4',width=5,height=2,command=lambda : get_digit(4))
btn_4.grid(row=2,column=2)
btn_4.configure(font=('verdana',14))

btn_sub=Button(root,text='-',width=5,height=2,command=lambda :get_operator('-'))
btn_sub.grid(row=2,column=3)
btn_sub.configure(font=('verdana',14))

btn_3=Button(root,text='3',width=5,height=2,command=lambda : get_digit(3))
btn_3.grid(row=3,column=0)
btn_3.configure(font=('verdana',14))

btn_2=Button(root,text='2',width=5,height=2,command=lambda : get_digit(2))
btn_2.grid(row=3,column=1)
btn_2.configure(font=('verdana',14))

btn_1=Button(root,text='1',width=5,height=2,command=lambda : get_digit(1))
btn_1.grid(row=3,column=2)
btn_1.configure(font=('verdana',14))

btn_mul=Button(root,text='*',width=5,height=2,command=lambda :get_operator('*'))
btn_mul.grid(row=3,column=3)
btn_mul.configure(font=('verdana',14))

btn_clr=Button(root,text='C',width=5,height=2,command=lambda :clr())
btn_clr.grid(row=4,column=0)
btn_clr.configure(font=('verdana',14))

btn_0=Button(root,text='0',width=5,height=2,command=lambda : get_digit(0))
btn_0.grid(row=4,column=1)
btn_0.configure(font=('verdana',14))

btn_result=Button(root,text='=',width=5,height=2,command=get_result)
btn_result.grid(row=4,column=2)
btn_result.configure(font=('verdana',14))

btn_devide=Button(root,text='/',width=5,height=2,command=lambda :get_operator('/'))
btn_devide.grid(row=4,column=3)
btn_devide.configure(font=('verdana',14))



root.mainloop()