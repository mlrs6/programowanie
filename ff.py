from tkinter import Tk, Button
def click_action():
    print("wow!")
    click = Button(root, text="wow", width=11)
root = Tk()
root.geometry("400x200")
click=Button(root, text="nacisnij", width=11)
click.pack()
click.config(command=click_action)
root.mainloop()