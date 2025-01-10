from tkinter import Tk,Label,Button,Entry,Text,Checkbutton,Radiobutton

okno=Tk()
b=0
for r in range(15):
    for c in range(15):
        b=b+1
        Button(text=(b)).grid(row=r,column=b)



okno.mainloop()
