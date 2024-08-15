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

delete_button=Button(window,text="Delete task",width=50,command=deletetask)
delete_button.pack(pady=3)

mark_button=Button(window,text="Mark as completed",width=50,command=markcompleted)
mark_button.pack(pady=3)

window.mainloop()
def entertask():
    input_text=""
    def add():
        input_text=entry_task.get(1.0,"end_1c")
        if input_text=="":
            tkinter.messagebox(title="Warning!",message="Please enter some text")
        else:
            listbox_task.insert(END,input_text)
            root1.destroy
    root1=Tk()
    root1.title("Add task")
    entry_task=Text(root1,width=40,height=4)
    entry_task.pack()
    button_temp=Button(root1,text="Add task")
