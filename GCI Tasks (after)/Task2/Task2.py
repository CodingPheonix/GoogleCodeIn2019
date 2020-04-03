import tkinter as tk


def thing1():
    print("This will open/do thing 1")
def thing2():
    print("This will open/do thing 2")
def thing3():
    print("This will open/do thing 3")



root = tk.Tk()

frame = tk.Frame(root, height=500, width=500)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)

thing1button = tk.Button(frame,
                   text="Thing1",
                   command=thing1)
thing2button = tk.Button(frame,
                   text="Thing2",
                   command=thing2)
thing3button = tk.Button(frame,
                   text="Thing3",
                   command=thing3)


thing1button.pack(side=tk.LEFT)
thing2button.pack(side=tk.LEFT)
thing3button.pack(side=tk.LEFT)

root.mainloop()
