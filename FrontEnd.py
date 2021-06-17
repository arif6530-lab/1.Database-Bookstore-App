#here we will make layout i.e front End of our Database App

from tkinter import * #lib for GUI
import BackEnd  #importing BackEnd.py file

def view_command():
    e5.delete(0,END)
    list1.delete(0,END) #delete from line 0 to End
    for rows in BackEnd.view():  #its a list of tuples ,therefore using loop to print one by one
        list1.insert(END,rows)

def search_command():
    e5.delete(0,END)
    list1.delete(0,END)
    for rows in BackEnd.search(title_text.get(),author_text.get(),year_text.get(),Isbn_text.get()):
        list1.insert(END,rows)
    

def insert_command():
    e5.delete(0,END)
    BackEnd.insert(title_text.get(),author_text.get(),year_text.get(),Isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),Isbn_text.get()))#just printing in list what we inserted
    e5.insert(END,"Insertion Successfull! Please refresh")

def get_selected_row(event): #select operation is event here
    try:
        global selected_row
        index=list1.curselection()[0]        #this index=list1.curselection()   will select index of our selected row (index of row starts from 0) 
        #it will give aa tuple containing the index of our row ex-(3,)     but we need to fetch the first element of that tuple
        #therefore we will use index=list1.curselection()[0]   now this will give index=3 
        #print(index)

        selected_row=list1.get(index)  #this will fetch complete row at present at index as a tuple
        #we will fetch the first thing of selected_row i.e 'id' of selected row

        e1.delete(0,END)
        e1.insert(END,selected_row[1])
        e2.delete(0,END)
        e2.insert(END,selected_row[2])
        e3.delete(0,END)
        e3.insert(END,selected_row[3])
        e4.delete(0,END)
        e4.insert(END,selected_row[4])
    except IndexError:
        pass        #expalaination of 'try' and 'except'  -----on running program pur listbox show empty,but on clicking on listbox it gives indent error bcoz of this line index=list1.curselection()[0] (it has no meaning if listbox is empty),therepas we use try except to get rid of this error,pass means 'do nothing'

        
def delete_command():
    e5.delete(0,END)
    BackEnd.delete(selected_row[0]) # selected_row[0]  is the id of the selected row
    e5.insert(END,"Deletion Successfull!,Please refresh")


def update_command():
    e5.delete(0,END)
    BackEnd.update(selected_row[0],title_text.get(),author_text.get(),year_text.get(),Isbn_text.get())
    e5.insert(END,"Updation Successfull! Please refresh")

    


window=Tk()#making an empty window by creating object of Tkinter

l0=Label(window,text="                        NEW BOOK-STORE                ",background="pink")
l0.grid(row=0,column=0,columnspan=4)

l1=Label(window,text="Title",foreground='blue')
l1.grid(row=1,column=0)

l2=Label(window,text="Author",foreground="blue")
l2.grid(row=1,column=2)

l3=Label(window,text="Year",foreground="blue")
l3.grid(row=2,column=0)

l4=Label(window,text="ISBN",foreground="blue")
l4.grid(row=2,column=2)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=1,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=1,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=2,column=1)


Isbn_text=StringVar()
e4=Entry(window,textvariable=Isbn_text)
e4.grid(row=2,column=3)

e5_value=StringVar()
e5=Entry(window,textvariable=e5_value,width=30,foreground="green")
e5.grid(row=8,column=0,columnspan=2)


list1=Listbox(window, height=6,width=35)
list1.grid(row=3,column=0,rowspan=8,columnspan=2)

list1.bind('<<ListboxSelect>>',get_selected_row) #when we will select a row ,this event will get recognized by listbox

sb1=Scrollbar(window,background="blue")
sb1.grid(row=2,column=2,rowspan=7)

list1.configure(yscrollcommand=sb1.set) #connecting list with scrollbar
sb1.configure(command=list1.yview) #connecting scrollbar with list

b1=Button(window,text="View all",width=8,command=view_command,background="orange")
b1.grid(row=3,column=3)

b2=Button(window,text="Search entry",width=8,command=search_command,background="orange")
b2.grid(row=4,column=3)

b3=Button(window,text="Add entry",width=8,command=insert_command,background="orange")
b3.grid(row=5,column=3)

b4=Button(window,text="Update",width=8,command=update_command,background="orange")
b4.grid(row=6,column=3)

b5=Button(window,text="Delete",width=8,command=delete_command,background="orange")
b5.grid(row=7,column=3)

b6=Button(window,text="close",width=8,command=window.destroy,background="orange")
b6.grid(row=8,column=3)



window.mainloop()#this emsure our window is opened while working