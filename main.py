from tkinter import *

black = "#0F172A"
white = "#FFFFFF"
gray = "#64748B"

root = Tk()
root.title('Form')
# root.iconbitmap('./images/icon2.ico')
width = 599
height = 433
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(False, True)
root.configure(bg=white)

bg = PhotoImage(file='bg.png')

btn =   PhotoImage(file='btn.png')
card =   PhotoImage(file='card.png')
delt =   PhotoImage(file='delete.png')
edit =   PhotoImage(file='edit.png')





cnx = mysql.connector.connect(user='root', password='',
                              host='localhost')
cursor = cnx.cursor()

cursor.execute("create DATABASE IF NOT EXISTS boxtot_db;")
cursor.execute("USE boxtot_db")
cursor.execute("CREATE TABLE IF NOT EXISTS Users  ( id INT, name VARCHAR(255));")



def Create(id,name):
    cursor.execute(f"INSERT INTO Users (id, name) VALUES ({id}, '{name}');")
    print("added data")
    cnx.commit()



def Delete(id):
    cursor.execute(f"DELETE FROM Users WHERE id = {id};")
    cnx.commit()
    print("ITEM ", id, " is deleted")
    for widget in container.winfo_children():
        widget.destroy()
    Read()


def Logout(id,name):
    root.withdraw()
    data = {
        'id': id,
        'name': name,
    }
    with open('data.json', 'w') as f:
        json.dump(data, f)
    os.system('py create.py')




bgf = Label(root,image=bg ,bg=white)
bgf.place(x=0,y=0)

btnf = Button(root,image=btn,bd=0,bg=white,command=Logout)
btnf.place(x=420,y=0)

container = Frame(root, height=400, width=500,bg=white)





def Read():
    cursor.execute("SELECT * FROM Users;")  

    i=0
    for data in cursor:
    
    
        cardf = Label(container,image=card,bd=0,bg=white)
        deltf = Button(cardf,image=delt,bd=0,bg=white,cursor="hand2",command=lambda id=data[0]: Delete(id))
        editf= Button(cardf,image=edit,bd=0,bg=white,cursor="hand2",command=lambda id=data[0] , name=data[1]: Logout(id,name))
        editf.place(x=20,y=10)
        deltf.place(x=120,y=10)
        name = Label(cardf,text=data[1],font=("Arial ", 18),fg=black,bg=white)
        name.place(x=40,y=30)
        cardf.grid(row=i//3, column=i%3)
        i=i+1
Read()

container.place(x=50,y=120)

root.mainloop()