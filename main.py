import sqlite3;
import tkinter as tk
from tkinter import BOTH, LEFT, VERTICAL,  ttk
from tkinter import messagebox
from tkinter.messagebox import  showinfo

from PIL import ImageTk, Image

root= tk.Tk();
root.title('Company Info');
root.geometry("780x500");
root.configure(bg='#F2F2F2')

main_frame =tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=1)


my_canvas= tk.Canvas(main_frame)
my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)


my_scrollbar= tk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)



my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion =my_canvas.bbox("all")))


second_frame =tk.Frame(my_canvas)

my_canvas.create_window((0,0), window=second_frame, anchor='nw')


input_frame= tk.LabelFrame(second_frame,bg='#F2F2F2', font=("Helvetica", 10) );
input_frame.grid(row=1, column=0, rowspan=5, columnspan=4, padx=10, pady=10)


input_frame_select= tk.LabelFrame(second_frame,text='Select Record',bg='#F2F2F2', font=("Helvetica", 10));
input_frame_select.grid(row=0, column=0,  padx=10, pady=10)



def update():
  conn= sqlite3.connect('company_info.db');
  c = conn.cursor();

  record_id = select_box.get()

  c.execute("""UPDATE company SET 
    company_name = :c_name,
    contact_name = :p_contact,
    country  = :country,
    email = :email,
    phone_number= :phone,
    web_page = :web

    WHERE oid = :oid""",
    {
    'c_name':c_name_editor.get(),
    'p_contact':p_name_editor.get(),
    'country':country_editor.get(),
    'email':email_editor.get(),
    'phone':phone_editor.get(),
    'web':web_editor.get(),
    'oid': record_id
    })

  conn.commit()

  conn.close(); 

  showinfo(
        title='Information',
        message='Data Edited to the Database')
  
  editor.destroy()
  
def edit():

  global editor;
  editor= tk.Tk();
  editor.title('Edit Company Info');
  editor.geometry("400x300");
  editor.configure(bg='#F2F2F2', padx=20, pady=20)

  conn= sqlite3.connect('company_info.db');
  c = conn.cursor();

  record_id= select_box.get()
  c.execute("SELECT * FROM company WHERE  oid ="+ record_id)
  records =c.fetchall()

  global c_name_editor
  global p_name_editor
  global country_editor
  global email_editor
  global phone_editor
  global web_editor

  c_name_editor = tk.Entry(editor,width=30)
  c_name_editor.grid(row=0, column=1, padx=20, columnspan=2)

  p_name_editor = tk.Entry(editor,width=30)
  p_name_editor.grid(row=1, column=1, padx=20, columnspan=2)

  country_editor = tk.Entry(editor,width=30)
  country_editor.grid(row=2, column=1, padx=20, columnspan=2)

  email_editor= tk.Entry(editor,width=30)
  email_editor.grid(row=3, column=1, padx=20, columnspan=2)

  phone_editor = tk.Entry(editor,width=30)
  phone_editor.grid(row=4, column=1, padx=20, columnspan=2)

  web_editor = tk.Entry(editor,width=30)
  web_editor.grid(row=5, column=1, padx=20, columnspan=2)
  

  c_name_label_editor=tk.Label(editor, text="Company Name", height=1, width=15, pady=8, padx=8, anchor='w')
  c_name_label_editor.grid(row=0,column=0)

  p_name_label_editor=tk.Label(editor, text="Contact Name", height=1, width=15, pady=8, padx=8, anchor='w')
  p_name_label_editor.grid(row=1,column=0)

  country_label_editor=tk.Label(editor, text="Country",height=1, width=15, pady=8, padx=8, anchor='w' )
  country_label_editor.grid(row=2,column=0)

  email_label_editor=tk.Label(editor, text="Email",  height=1, width=15, pady=8, padx=8, anchor='w')
  email_label_editor.grid(row=3,column=0)

  phone_label_editor=tk.Label(editor, text="Phone Number",  height=1, width=15, pady=8, padx=8, anchor='w')
  phone_label_editor.grid(row=4,column=0)

  web_label_editor=tk.Label(editor, text="Web Site",  height=1, width=15, pady=8, padx=8, anchor='w')
  web_label_editor.grid(row=5,column=0)
  
  save_btn_editor= tk.Button(editor, text="Save", command=update,  bg='#04C4D9', font=("Helvetica", 10))
  save_btn_editor.grid(row=6, column=1, pady=10, padx=10, ipadx=80 )

  for record in records:
    c_name_editor.insert(0,record[0])
    p_name_editor.insert(0,record[1])
    country_editor.insert(0,record[2])
    email_editor.insert(0,record[3])
    phone_editor.insert(0,record[4])
    web_editor.insert(0,record[5])
 
  conn.commit()

  conn.close(); 



def delete():
  conn= sqlite3.connect('company_info.db');

  c = conn.cursor();


  c.execute('DELETE from company where oid = ' + select_box.get())
  
  showinfo(
        title='Information',
        message='Data Deleted to the Database')

  conn.commit()

  conn.close();


def add():
  conn= sqlite3.connect('company_info.db');
  c = conn.cursor();

  c.execute("INSERT INTO company VALUES(:c_name, :p_name, :country, :email, :phone, :web)",
      {
        'c_name':c_name.get(),
        'p_name':p_name.get(),
        'country':country.get(),
        'email': email.get(),
        'phone':phone.get(),
        'web':web.get()
      }
    )
  conn.commit()

  conn.close(); 

  showinfo(
        title='Information',
        message='Data Added to the Database')
  
  new_data.destroy()


def submit():
  global new_data
  new_data= tk.Tk();
  new_data.title('Company Info');
  new_data.geometry("400x300");
  new_data.configure(bg='#F2F2F2')

  global c_name
  global p_name
  global country
  global email
  global phone
  global web

  c_name = tk.Entry(new_data,width=30)
  c_name.grid(row=0, column=1, padx=20, columnspan=2)

  p_name = tk.Entry(new_data,width=30)
  p_name.grid(row=1, column=1, padx=20, columnspan=2)

  country = tk.Entry(new_data,width=30)
  country.grid(row=2, column=1, padx=20, columnspan=2)

  email= tk.Entry(new_data,width=30)
  email.grid(row=3, column=1, padx=20, columnspan=2)

  phone = tk.Entry(new_data,width=30)
  phone.grid(row=4, column=1, padx=20, columnspan=2)

  web = tk.Entry(new_data,width=30)
  web.grid(row=5, column=1, padx=20, columnspan=2)
  

  c_name_label=tk.Label(new_data, text="Company Name", height=1, width=15, pady=8, padx=8, anchor='w')
  c_name_label.grid(row=0,column=0)

  p_name_label=tk.Label(new_data, text="Contact Name", height=1, width=15, pady=8, padx=8, anchor='w')
  p_name_label.grid(row=1,column=0)

  country_label=tk.Label(new_data, text="Country",height=1, width=15, pady=8, padx=8, anchor='w' )
  country_label.grid(row=2,column=0)

  email_label=tk.Label(new_data, text="Email",  height=1, width=15, pady=8, padx=8, anchor='w')
  email_label.grid(row=3,column=0)

  phone_label=tk.Label(new_data, text="Phone Number",  height=1, width=15, pady=8, padx=8, anchor='w')
  phone_label.grid(row=4,column=0)

  web_label=tk.Label(new_data, text="Web Site",  height=1, width=15, pady=8, padx=8, anchor='w')
  web_label.grid(row=5,column=0)

  save_btn_editor= tk.Button(new_data, text="Save", command=add,  bg='#04C4D9', font=("Helvetica", 10))
  save_btn_editor.grid(row=6, column=1, pady=10, padx=10, ipadx=80 )


  # conn= sqlite3.connect('company_info.db');

  # c = conn.cursor();

#   c.execute("""CREATE TABLE company(
#    company_name text,
#    contact_name text,
#    country text,
#    email text,
#    phone_number,
#    web_page text
# )
# """);  

 
  # )

  # conn.commit()

  # conn.close();

 


def show():
  # top= tk.Toplevel()
  conn= sqlite3.connect('company_info.db');
  c = conn.cursor();

  style = ttk.Style(root)
  style.theme_use("clam")
  style.configure("Treeview.Heading", background="#04C4D9",bordercolor="#04C4D9")
  trv = ttk.Treeview(second_frame, selectmode ='browse')
  
  trv.grid(row=10,column=0,padx=20, pady=20)

# number of columns
  trv["columns"] = ("1", "2", "3","4","5","6","7")
  
# Defining heading
  trv['show'] = 'headings'
  
# width of columns and alignment 
  trv.column("1", width = 50, anchor ='c')
  trv.column("2", width = 100, anchor ='c')
  trv.column("3", width = 120, anchor ='c')
  trv.column("4", width = 80, anchor ='c')
  trv.column("5", width = 120, anchor ='c')
  trv.column("6", width = 100, anchor ='c')
  trv.column("7", width = 150, anchor ='c')
 
  
# Headings  
# respective columns
  trv.heading("1", text ="ID")
  trv.heading("2", text ="Company")
  trv.heading("3", text ="Contact Name")
  trv.heading("4", text ="Country")
  trv.heading("5", text ="Email")  
  trv.heading("6", text ="Phone Numer")
  trv.heading("7", text ="Web Page")
  


  c.execute("SELECT oid, * FROM company")
  records =c.fetchall()

  for row in records:
    trv.insert("", tk.END, values=row) 
    print(row)    
  conn.commit()

  conn.close(); 

select_box = tk.Entry(input_frame_select,width=30)
select_box.grid(row=1, column=1, padx=20, columnspan=2)

select_box_label=tk.Label(input_frame_select, text="ID number",  height=1, width=15, pady=8, padx=8, anchor='w')
select_box_label.grid(row=1,column=0)

submit_btn =tk.Button(input_frame, text="Register",command=submit, bg='#04C4D9' )
submit_btn.grid(row=0, column =1,  pady=10, padx=10, ipadx=20)

show_btn= tk.Button(input_frame, text="View", command=show,bg='#04C4D9', font=("Helvetica", 10),)
show_btn.grid(row=0, column=2, pady=10, padx=10, ipadx=20 )


delete_btn= tk.Button(input_frame_select, text="Delete", command=delete, bg='#04C4D9', font=("Helvetica", 10))
delete_btn.grid(row=2, column=2, pady=10, padx=10, ipadx=20 )

update_btn= tk.Button(input_frame_select, text="Edit", command=edit,  bg='#04C4D9', font=("Helvetica", 10),)
update_btn.grid(row=2, column=1, pady=10, padx=10, ipadx=20 )

show();


root.mainloop()