import tkinter
from tkinter import *
import tkinter.messagebox as msg

window = Tk()
window.title("ToDo List")
frame_task = Frame(window)
frame_task.pack()

listbox_task=Listbox(frame_task, bg="black,fg=white", height=15, width=50,font="Helvetica")
listbox_task.pack(side=tkinter.LEFT)

scrollbar_task=Scrollbar(frame_task)
listbox_task.pack(side=tkinter.RIGHT, fill=tkinter.Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

#Button widget
entry_button=Button(window,text="Add task",width= 50,command=entertask)
entry_button.pack(pady=3)

