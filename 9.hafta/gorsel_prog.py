from tkinter import *

window = Tk()


window.title("selam")

lbl=Label(window,text="User Login",font=30)
lbl.grid(column=40,row=3)

lbl=Label(window,text="username")
lbl.grid(column=8,row=50)

lbl2=Label(window,text="password")
lbl2.grid(column=8,row=60)

txt=Entry(window,width=15)
txt.grid(column=10,row=50)

txt2=Entry(window,width=15,show='*')
txt2.grid(column=10,row=60)

def tkla():
    inp = txt.get()
    print(inp)

    if(txt.get()=="emir" and txt2.get()=="12"):
        correct=Tk()
        window.title("dogru")
        asd="Hoşgeldin",txt.get()
        lbl3=Label(correct,text=asd)
        lbl3.grid(column=0,row=0)
        correct.mainloop()
    else:
        yanlis=Tk()
        window.title("yanlis")
        
        lbl4=Label(yanlis,text="Başka kapıya")
        lbl4.grid(column=0,row=0)
        yanlis.mainloop()
        


btn=Button(window,text="Giriş Yap",width=6,height=1,command=lambda:tkla())
btn.grid(column=10,row=70)




window.geometry('500x400')
window.mainloop()