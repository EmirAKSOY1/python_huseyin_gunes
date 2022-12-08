#VzEzV7jD1blXMvqg3SeWbrOoMLzqc7miQEQs9WjDKsbVhAOvkwpgumgAodEJ
from tkinter import *
from tkinter import messagebox
import http.client
import json
window =Tk()
window.title("selam")

pla=Label(window,text="Parite Gir",font=30)
pla.grid(column=0,row=1)

parite=Entry(window,width=15)
parite.grid(column=10,row=1)


bas=Label(window,text="Başlangıç",font=30)
bas.grid(column=0,row=3)

basparite=Entry(window,width=15)
basparite.grid(column=10,row=3)

bit=Label(window,text="Bitiş",font=30)
bit.grid(column=0,row=6)

bitparite=Entry(window,width=15)
bitparite.grid(column=10,row=6)

def cek():
  print(parite.get(),basparite.get(),bitparite.get())
  conn = http.client.HTTPSConnection("www.nosyapi.com")
  payload = ''
  headers = {
    'Authorization': 'VzEzV7jD1blXMvqg3SeWbrOoMLzqc7miQEQs9WjDKsbVhAOvkwpgumgAodEJ'
  }
  conn.request("GET", f"/apiv2/economy/getCoinDetails?code={parite.get()}", payload, headers)
  res = conn.getresponse()
  data = res.read()
  
  data=data.decode("utf-8")
  res = json.loads(data)
  res=res['data']
  
  print(res[0]['buying'])

btn=Button(window,text="Giriş Yap",width=6,height=1,command=lambda:cek())
btn.grid(column=10,row=70)
window.geometry('500x400')
window.mainloop()