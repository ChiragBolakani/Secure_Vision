import tkinter as tk

def generate_log():
    master = tk.Tk()
    master.geometry('300x300')
    master.title('CCTV Log')

    text_widget = tk.Text(master, height=300, width=300)
    scroll = tk.Scrollbar(master)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)
    scroll.config(command=text_widget.yview)

    text_widget.config(yscrollcommand=scroll.set)
    text_widget.pack()

    file1 = open('time_stamp.txt', 'r+') 
    Lines = file1.readlines() 
    for i in range(0, len(Lines)):
        text_widget.insert(tk.END, Lines[i])

    # Start the mainloop
    file1.close()
    tk.mainloop()

