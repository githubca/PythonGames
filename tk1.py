import tkinter as tk
from datetime import datetime

window = tk.Tk()

greeting =  tk.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=20,
    height=3
)

greeting.pack()

now = datetime.now()

time = tk.Label(text=now.strftime("%H:%M:%S"))
time.pack()

entry = tk.Entry(fg="red", bg="white", width=50)
entry.pack()



frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(master=frame_a, text="I'm in Frame A")
label_a.pack()


label_b = tk.Label(master=frame_b, text="I'm in Frame B")
label_b.pack()

frame_a.pack()
frame_b.pack()

'''frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=window, width=100, bg="yellow")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=window, width=50, bg="blue")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)'''

frame = tk.Frame(master=window, width=150, height=150)
frame.pack()

label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
label1.place(x=0, y=0)

label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")
label2.place(x=75, y=75)

button = tk.Button(
    text="Click me!",
    width=15,
    height=3,
    bg="grey",
    fg="yellow",
)
button.pack()

window.mainloop()