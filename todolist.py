import tkinter as c
import tkinter.messagebox
import pickle
win=c.Tk()
win.geometry("300x400")
win.config(bg="#00EEEE")
#heading
c.Label(win,text="TASK LIST",font="bruney 19 bold",bg="black",fg="gold").pack()


frame1= c.Frame(win,bd=2,bg="maroon")
frame1.place(x=0,y=340,width=300,height=60)

frame2= c.Frame(win,bd=2,bg="lightblue")
frame2.place(x=0,y=305,width=300,height=35)

lf1=c.Label(win,text="write task:-",font="ariel 8 bold",bd=0)
lf1.place(x=3,y=318,width=60,height=10)

entry_task=c.Entry(win,bd=2)
entry_task.place(x=64,y=312,width=232)


def add_task():
    task=entry_task.get()
    if task != "":
         listbox_tasks.insert(c.END,task)
         entry_task.delete(0,c.END)
    else:
        c.messagebox.showwarning(title="warning", message="You must enter a task")
        

def load_data():
    try:
        tasks=pickle.load(open("tasks.dat","rb"))
        listbox_tasks.delete(0,c.END)
        for task in tasks:
            listbox_tasks.insert(c.END,task)
    except:
         c.messagebox.showwarning(title="warning", message="You must have tasks")



def del_task():
    try: 
        task_index=listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        c.messagebox.showwarning(title="warning", message="You must select a task")

def save_task():
      tasks=listbox_tasks.get(0,listbox_tasks.size())
      if len(tasks)!=0:
          pickle.dump(tasks,open("tasks.dat","wb"))
      else:
          c.messagebox.showwarning(title="warning", message="You must add a task")


#add button
ad_bu=c.Button(win,text="ADD",font="ariel 10 bold",bg="dark orange",fg="black",bd=3,cursor="hand2",command=add_task)
ad_bu.place(x=3,y=345,width=75,height=50)

#Load butoon
lo_bu=c.Button(win,text="Load task",font="ariel 10 bold",bg="#FF1493",fg="black",bd=3,cursor="hand2",command=load_data)
lo_bu.place(x=225,y=345,width=74,height=50)

#save button
sa_bu=c.Button(win,text="Save",font="ariel 10 bold",bg="#00CD00",fg="black",bd=3,cursor="hand2",command=save_task)
sa_bu.place(x=150,y=345,width=75,height=50)

#delete button
de_bu=c.Button(win,text="Delete",font="ariel 10 bold",bg="#9932CC",fg="black",bd=3,cursor="hand2",command=del_task)
de_bu.place(x=75,y=345,width=75,height=50)


listbox_tasks=c.Listbox(win,height=17,width=80)
listbox_tasks.pack()


c.mainloop()

