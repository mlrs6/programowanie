from tkinter import Tk, Button
click=0
def click_action(zzz):
    zzz.config( text=click)
root = Tk()
root.geometry("400x200")
click_zzz=Button(root, text="nacisnij", width=11)
click_zzz.pack()
click_zzz.config(command=lambda: click_action(click_zzz))
root.mainloop()
