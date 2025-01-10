from tkinter import Tk, Button
clicks=0
def click_action():
    global clicks
    clicks+=1
    click.config( text=clicks)
root = Tk()
root.geometry("400x200")
click=Button(root, text="nacisnij", width=11)
click.pack()
click.config(command=click_action)
root.mainloop()
