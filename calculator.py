#import everything from tkinter module
from tkinter import*


#create a tkinter window
window=Tk()
#background color
window.configure(bg='#1C1C1C')
#creating calculator display
display=Label(window,width=60,height=5,text="",font=("arial=30"))
display.pack()

window.geometry("570x600+100+200")

window.resizable(0, 0)
window.title('calculator')

#starting with functions  
equation=""

def clear():
     global equation
     equation=""
     display.config(text=equation)

def show(value):
     global equation
     equation+=value
     display.config(text=equation)
     
def calculate():
     global equation
     result=""
     if equation !="" :
        try :
             result=eval(equation)
        except:
             result="error"
             equation=""
     display.config  (text=result)      
                  

         



#create  buttons
Button(window,text='C',width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:clear()).place(x=10,y=100)
Button(window,text='/',width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#4A4A4A",command=lambda:show("/")).place(x=150,y=100)
Button(window,text='%',width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#4A4A4A",command=lambda:show("%")).place(x=290,y=100)
Button(window,text='*',width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#4A4A4A",command=lambda:show("x"),).place(x=430,y=100)

Button(window,text='7',width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#4A4A4A",command=lambda:show("7")).place(x=10,y=200)
Button(window,text='8',width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#4A4A4A",command=lambda:show("8"),).place(x=150,y=200)
Button(window,text='9',width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#4A4A4A",command=lambda:show("9")).place(x=290,y=200)
Button(window,text='-',width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#4A4A4A",command=lambda:show("-")).place(x=430,y=200)

Button(window,text='4',width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#4A4A4A",command=lambda:show("4")).place(x=10,y=300)
Button(window,text='5',width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#4A4A4A",command=lambda:show("5")).place(x=150,y=300)
Button(window,text='6',width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#4A4A4A",command=lambda:show("6")).place(x=290,y=300)
Button(window,text='+',width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#4A4A4A",command=lambda:show("+")).place(x=430,y=300)

Button(window,text='1',width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#4A4A4A",command=lambda:show("1")).place(x=10,y=400)
Button(window,text='2',width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#4A4A4A",command=lambda:show("2")).place(x=150,y=400)
Button(window,text='3',width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#4A4A4A",command=lambda:show("3")).place(x=290,y=400)
Button(window,text='=',width=4,height=3,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#EE6C4D",command=lambda:calculate()).place(x=430,y=400)

Button(window,text='0',width=11,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#4A4A4A",command=lambda:show("0")).place(x=10,y=500)
Button(window,text='.',width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#4A4A4A",command=lambda:show(".")).place(x=290,y=500)




#atach  botton to window 



window.mainloop()