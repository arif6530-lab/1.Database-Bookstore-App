#here we will do all backened work and connect this file to our frontEnd.py

import sqlite3 #inbuilt lib of python

def make_table():
    conn=sqlite3.connect("BookStore.db") #making coonection
    cur=conn.cursor()
    query=cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Year INTEGER, ISBN INTEGER)")
    #note- id is auto incerement here bcoz its primary key
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("BookStore.db")
    cur=conn.cursor()
    query=cur.execute("SELECT * FROM book")
    result=cur.fetchall()
    conn.close()
    return result

def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("BookStore.db")
    cur=conn.cursor()
    query=cur.execute("SELECT * FROM book WHERE Title=? OR Author=? OR Year=? OR ISBN=?",(title,author,year,isbn)) # we can also use string formatting %s 
    result=cur.fetchall()
    return result
    conn.close()


def insert(title,author,year,isbn):
    conn=sqlite3.connect("BookStore.db")
    cur=conn.cursor()
    query=cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn): #we will fetch id of the selected details
    conn=sqlite3.connect("BookStore.db")
    cur=conn.cursor()
    query=cur.execute("UPDATE book SET Title=?, Author=?, Year=?, ISBN=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()
  
def delete(id): #we will fecth id of selected details
    conn=sqlite3.connect("BookStore.db")
    cur=conn.cursor()
    query=cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()


make_table()
#insert("half gf","chetan bhagat",2005,7423)
#delete(1)
#print(view())

#print(search("alchemist","p.s"))
#update(1,"cdef","Q.W",1988,3872)

