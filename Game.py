from tkinter import*
from tkinter import font
from random import*

koloda=[2,3,4,5,6,7,8,9,10,11]*4
shuffle(koloda)
count=0

def more():
    global count,koloda
    karta=koloda.pop()
    count+=karta
    if count>21:
        tx1['text']='you lose, you have '+str(count)+' point, more than 21'
        bt1.destroy()
        bt2.destroy()
    elif count==21:
        tx1['text']='YOU WIN, YOU HAVE 21 POINT'
    else:
        tx1['text'] = 'you have ' + str(count) + ' point'
def enough():
    global count
    if count<21:
        tx1['text'] = 'you lose, you dont have 21 point'



win=Tk()
win.title('21 point')
win.geometry("800x400")
win['bg']='#0f300c'

font1=font.Font(family='Starliner BTN', size=15)
font2=font.Font(family='Times New Roman', size=10)


tx1=Label(win, text='0 POINT', font=font1, foreground='#622C7D', background='#0f300c')
tx1.place(x=50, y=50)
tx2=Label(win, text='result')

bt1=Button(win, text='MORE', font=font2, command=more)
bt1.place(x=50, y=100)
bt2=Button(win, text='ENOUGH', font=font2, bg='#E3D922', activebackground='#7F7A13', command=enough)
bt2.place(x=100, y=100)

win.mainloop()