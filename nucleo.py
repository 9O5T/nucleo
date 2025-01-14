import tkinter as tk
import customtkinter as ctk
import matplotlib
import matplotlib.pyplot as plt
import sqlite3 as sq
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk
import subprocess as sup
import os

program_extention = []



## Definitions:
main_font = ("Halvetica",14)
text_font = ("Halvetica",12)
mini_font = ("Halvetica",10)

def clear_all(wid):
    for item in wid.winfo_children():
        item.destroy()

def topbar_frame (sensei,backsite,txt):
    topbar_frame_wid = tk.Frame(master=sensei, width=app_w,background="white")
    topbar_frame_wid.pack(side="top",fill="x")

    topbar_frame_wid_back_btn = tk.Button(master=topbar_frame_wid, text="\u2190",font=("Calibri",20,"bold"),border=0,relief="flat",highlightthickness=0, activebackground='white',activeforeground="orange",highlightcolor="blue",foreground="orange",background="white",command=backsite)
    topbar_frame_wid_back_btn.pack(side="left",padx=10,pady=5)

    topbar_frame_wid_back_lbl = tk.Label(master=topbar_frame_wid,text=txt,background="white",font=main_font,foreground="orange")
    topbar_frame_wid_back_lbl.pack(side="left",pady=5)

def library_section_builder(sensei, img, file_name):
    program_name = file_name
    library_section_frame = tk.Frame(master=sensei,highlightthickness=1,highlightbackground="red",highlightcolor="blue",height=250,background="white")
    library_section_frame.pack(fill="x",pady=20,padx=30)
    library_section_frame.pack_propagate(False)
    library_section_image = tk.Frame(master=library_section_frame,highlightthickness=1,highlightbackground="white",highlightcolor="blue",height=250,width=250)
    library_section_image.pack(side="left")
    library_section_image.pack_propagate(False)

    library_section_lesson_img = tk.Label(master=library_section_image,image=img,background="white")
    library_section_lesson_img.pack(fill="both")

    file_path_id = f"programs/{file_name}/{file_name}_id.txt"
    

    with open(file_path_id,"r") as file:
        id_data = (file.read())
        id_data = id_data.split('\n')
    file.close()

    file_path_info = f"programs/{file_name}/{id_data[0]}"
    with open(file_path_info,"r",encoding='utf-8') as file:
        info_data = file.read()
        info_data = info_data.split("\n")
    file.close()

    library_section_lesson_id_frame = tk.Frame(master=library_section_frame,background="white",highlightthickness=1,highlightbackground="blue",highlightcolor="blue",height=250,width=250)
    library_section_lesson_id_frame.pack(side="left")
    library_section_lesson_id_frame.pack_propagate(False)

    library_section_lesson_header = tk.Label(master=library_section_frame,text=info_data[0],font=text_font,background="white",foreground="blue",anchor="center")
    library_section_lesson_header.pack(side="top",fill="x")

    library_section_lesson_writer = tk.Label(master=library_section_lesson_id_frame,text=info_data[1],font=text_font,background="white",foreground="blue",anchor="center")
    library_section_lesson_writer.pack(fill="both",expand=True)

    library_section_lesson_coder = tk.Label(master=library_section_lesson_id_frame,text=info_data[2],font=text_font,background="white",foreground="blue",anchor="center")
    library_section_lesson_coder.pack(fill="x")

    library_section_lesson_date = tk.Label(master=library_section_lesson_id_frame,text=info_data[3],font=text_font,background="white",foreground="blue",anchor="center")
    library_section_lesson_date.pack(fill="x")

    library_section_lesson_language = tk.Label(master=library_section_lesson_id_frame,text=info_data[4],font=text_font,background="white",foreground="purple",anchor="center")
    library_section_lesson_language.pack(fill="both",expand=True)



    file_path_bridge = f"programs/{file_name}/{id_data[1]}"
    file_path_program = f"programs/{file_name}/{id_data[2]}"
    file_path_abstract = f"programs/{file_name}/{id_data[3]}"
    

    with open(file_path_abstract,"r",encoding="utf-8") as file:
        abstract_data = file.read()

    library_section_frame_play_button = tk.Button(master=library_section_frame,border=0,highlightthickness=0,background="green2",text="Go to LAB",font=text_font,foreground="white",command=lambda:lab_frame_builder(id_data,info_data,program_name))
    library_section_frame_play_button.pack(fill="x",side="top",expand=True,padx=30)
    AV = tk.Text(master=library_section_frame,wrap="word",font=text_font,relief="flat",border=0,highlightthickness=0)
    AV.insert("end",abstract_data)
    AV.pack(fill="both",side="top",padx=30)
    AV.config(state="disabled")

    file.close()


def lab_frame_builder(id_data,info_data,program_name):
    clear_all(main_frame)
    lab_frame = tk.Frame(master=main_frame,background="white")
    lab_frame.pack(fill="both",expand=True)
    topbar_frame(lab_frame,nuclear_library_builder,"Library")
    tk.Label(master=lab_frame,text=info_data[0],font=("Calibri",20,"bold"),background="white",foreground="orange").pack(fill="x")



    lab_frame_left = tk.Frame(master=lab_frame,background="white")
    lab_frame_left.pack(side="left",expand=True,fill="both")
    lab_frame_left.pack_propagate(False)

    lab_frame_right = tk.Frame(master=lab_frame,background="black")
    lab_frame_right.pack(side="left",expand=True,fill="both",padx=10,pady=10)
    lab_frame_right.pack_propagate(False)

    lab_frame_subright = tk.Frame(master=lab_frame_right, background="white")
    lab_frame_subright.pack(side="top",fill="both")

    lab_frame_left_text = tk.Text(master=lab_frame_left, background="white",relief="flat", highlightthickness=1,border=0,font=text_font,wrap="word")
    lab_frame_left_text.pack(fill="both",expand=True,padx=10,pady=10)


    main_file_path_id = f"programs/{program_name}/{program_name}_main.txt"
    var_file_path_id = f"programs/{program_name}/{program_name}_variables_id.txt"
    var_file_path_var = f"programs/{program_name}/{program_name}_variables_var.txt"
    
    main_text = ""
    with open(main_file_path_id,"r",encoding='utf-8') as f:
        s = f.read()
        main_text = main_text + s

    #main_text = (main_text.replace("\n"," ").replace('\r\n', ' '))
    lab_frame_left_text.insert(tk.END,main_text)
    f.close()
    lab_frame_left_text.config(state=tk.DISABLED)
    with open(var_file_path_id,"r", encoding='utf-8') as file:
        s = file.read()
    file.close()
    s = (s.replace("\n","").split(":"))
    for i in range(len(s)-1):
        tk.Label(master=lab_frame_subright, text=s[i],anchor="e",font=text_font,background="white").grid(row=i,column=0,sticky="news")
    lab_entry = []
    lab_entry_vars = []
    for i in range(len(s)-1):
        lab_entry_vars.append(tk.StringVar(lab_frame_right))
        lab_entry.append(tk.Entry(master=lab_frame_subright, relief="flat",border=0, font=text_font,highlightthickness=1,background="white",foreground="blue",textvariable=lab_entry_vars[i]).grid(row=i,column=1,sticky="news"))
    
    

    def run_code():
        if s[-1] == "tab":
            sep_par = "    "
        elif s[-1] == "com":
            sep_par = ","
        elif s[-1] == "dub":
            sep_par = ";"

        variables_text = ""
        for var in lab_entry_vars:
            variables_text = variables_text + var.get() + sep_par
        with open(var_file_path_var,"w") as var_file:
            var_file.write(variables_text)
        var_file.close()

        tk.Label(master=lab_frame_right,background="black",font=text_font,foreground="green2",anchor="e",text="System : Program is started by nucleo.").pack(side="top",fill="x")
        crpath = os.getcwd()
        os.chdir(f"{crpath}/programs/{program_name}")
        #os.system(f"wsl gfortran {program_name}.f90; ./a.out ;exit")
        os.system(f"wsl ./{program_name}.sh")
        ans_file = open(f"{program_name}_variables_ans.txt","r")
        lines = ans_file.readlines()
        for line in lines:
            tk.Label(master=lab_frame_right,background="black",font=text_font,foreground="green2",anchor="w",text=line).pack(side="top",fill="x")
        ans_file.close()
        os.chdir(f"{crpath}")

    def open_pdf():
        crpath = os.getcwd()
        os.chdir(f"{crpath}/programs/{program_name}")
        os.system(f"{program_name}.pdf")
        os.chdir(f"{crpath}")

    lab_frame_button = tk.Button(master=lab_frame_subright,background="green2",border=0,font=text_font,text="Run",command=run_code)
    lab_frame_button.grid(column=0,row=len(s)-1,columnspan=2,sticky="news")

    lab_frame_see_pdf_button = tk.Button(master=lab_frame_left,background="magenta3",border=0,font=text_font,foreground="white",text="See PDF",command=open_pdf)
    lab_frame_see_pdf_button.pack(fill="x", padx=10,pady=10)
    lab_frame_subright.rowconfigure(len(s)-1,weight=1)
    lab_frame_subright.columnconfigure(1,weight=1)


def search(word):
    con = sq.connect("element_data.db")
    con.commit()
    cursor =  con.execute(f"select * from elements where '{word}' IN (id,name,symbol,mass,noutron,proton,electron,shell,valance);")
    data = cursor.fetchall()
    con.close()
    return data

def periodic_table_builder():
    clear_all(main_frame)
    periodic_table_frame = tk.Frame(master=main_frame, background="white",width=app_w,height=app_h)
    periodic_table_frame.pack(fill="both",expand=True)
    topbar_frame(periodic_table_frame,menu_frame_builder,"home")
    periodic_table_img_label = tk.Label(master=periodic_table_frame,image=img_periodic_table,background="white")
    periodic_table_img_label.pack(pady=20)


def atomic_info_builder():
    def search_element():
        atomic_info_search_lb.delete(0,"end")
        sql_response = search(str(atomic_info_search_entry.get()))
        for i in sql_response:
            atomic_info_search_lb.insert("end",i[1])

    def load_selected_element():
        a = (atomic_info_search_lb.get(atomic_info_search_lb.curselection()))
        sql_response = search(a)
        response = sql_response[0]
        element_number.config(text = response[0]) 
        element_name.config(text = response[1])
        element_symbol.config(text = response[2])
        element_atomic_mass.config(text = response[3])
        element_number_noutron.config(text = response[4])
        element_number_proton.config(text = response[5])
        element_number_electron.config(text = response[6])
        element_number_shell.config(text = response[7])
        element_number_valance.config(text = response[8])

    def load_ev(event):
        load_selected_element()
    def search_ev(event):
        search_element()
            

    clear_all(main_frame)

    atomic_info = tk.Frame(master=main_frame, background="white",width=app_w,height=app_h)
    atomic_info.pack(fill="both",expand=True)
    topbar_frame(atomic_info,menu_frame_builder,"home")

    atomic_info_search_frame = tk.Frame(master=atomic_info,background="white",highlightthickness=0,highlightcolor="blue",highlightbackground="blue")
    atomic_info_search_frame.pack(side="left",anchor="n",padx=5)
    atomic_info_search_frame.columnconfigure(index=1,weight=1)
    
    atomic_info_search_entry = tk.Entry(master=atomic_info_search_frame,width=30, font=text_font, background="white",highlightthickness=1,highlightcolor="lightgreen")
    atomic_info_search_entry.grid(row=0,column=0,sticky="news")
    

    atomic_info_search_btn = tk.Button(master=atomic_info_search_frame,relief="flat",text="  \u2315  ",font=main_font,foreground="white",border=0,background="green2",command=search_element)
    atomic_info_search_btn.grid(row=0,column=1)

    atomic_info_search_lb = tk.Listbox(master=atomic_info_search_frame)
    atomic_info_search_lb.grid(row=1,column=0,columnspan=2,sticky="news")
    

    atomic_info_load_btn = tk.Button(master=atomic_info_search_frame,relief="flat",text="Load Element Data",font=mini_font,foreground="white",border=0,background="purple",command=load_selected_element)
    atomic_info_load_btn.grid(row=2,column=0,columnspan=2,sticky="news")

    line_frame = tk.Frame(master=atomic_info,highlightthickness=2,highlightbackground="orange",width=2)
    line_frame.pack(side="left",fill="y")

    atomic_info_load_frame = tk.Frame(master=atomic_info,highlightthickness=2,highlightbackground="white",background="white")
    atomic_info_load_frame.pack(side="left",fill="both",padx=5,anchor="center",expand=True)
    tk.Label(master=atomic_info_load_frame, text="Element ID",font=main_font,foreground="orange",background="white").pack(side="top",fill="x")

    atomic_info_symbol_frame = tk.Frame(master=atomic_info_load_frame,highlightthickness=1,width=270,height=270,highlightbackground="purple",background="white")
    atomic_info_symbol_frame.grid_propagate(False)
    atomic_info_symbol_frame.pack(side="top",pady=30)
    atomic_info_info_frame = tk.Frame(master=atomic_info_load_frame,background="white")
    atomic_info_info_frame.pack(side="top",pady=30)

    # Variables:
    tk.Label(master=atomic_info_info_frame,background="white", text="Name",font=text_font).grid(row=0,column=0,sticky="w")
    tk.Label(master=atomic_info_info_frame,background="white", text="Atomic Mass",font=text_font).grid(row=1,column=0,sticky="w")
    tk.Label(master=atomic_info_info_frame,background="white", text="Number of noutrons",font=text_font).grid(row=2,column=0,sticky="w")
    tk.Label(master=atomic_info_info_frame,background="white", text="Number of protons",font=text_font).grid(row=3,column=0,sticky="w")
    tk.Label(master=atomic_info_info_frame,background="white", text="Number of electrons",font=text_font).grid(row=4,column=0,sticky="w")
    tk.Label(master=atomic_info_info_frame,background="white", text="Number of shell",font=text_font).grid(row=5,column=0,sticky="w")
    tk.Label(master=atomic_info_info_frame,background="white", text="Number of valance",font=text_font).grid(row=6,column=0,sticky="w")
    for k in range(7):
        tk.Label(master=atomic_info_info_frame,background="white", text=":",font=text_font).grid(row=k,column=1,sticky="news")
        
    element_number = tk.Label(master=atomic_info_symbol_frame,background="white", text="1",font=("Calibri",20))
    element_number.grid(row=0,column=0,sticky="se")
    element_symbol= tk.Label(master=atomic_info_symbol_frame,background="white", text="H",font=("Calibri",120))
    element_symbol.grid(row=1,column=1,sticky="e")
    element_name = tk.Label(master=atomic_info_info_frame,background="white", text="Hydrogen",font=text_font)
    element_name.grid(row=0,column=2,sticky="w")
    element_atomic_mass = tk.Label(master=atomic_info_info_frame,background="white", text="1.007",font=text_font)
    element_atomic_mass.grid(row=1,column=2,sticky="w")
    element_number_noutron = tk.Label(master=atomic_info_info_frame,background="white", text="0",font=text_font)
    element_number_noutron.grid(row=2,column=2,sticky="w")
    element_number_proton = tk.Label(master=atomic_info_info_frame,background="white", text="1",font=text_font)
    element_number_proton.grid(row=3,column=2,sticky="w")
    element_number_electron = tk.Label(master=atomic_info_info_frame,background="white", text="1",font=text_font)
    element_number_electron.grid(row=4,column=2,sticky="w")
    element_number_shell = tk.Label(master=atomic_info_info_frame,background="white", text="1",font=text_font)
    element_number_shell.grid(row=5,column=2,sticky="w")
    element_number_valance= tk.Label(master=atomic_info_info_frame,background="white", text="1",font=text_font)
    element_number_valance.grid(row=6,column=2,sticky="w")




    atomic_info_search_entry.bind("<Return>",search_ev)
    atomic_info_search_lb.bind("<Return>",load_ev)


    #word = input("Aranacak kelime:")
    #data = search(word)
    #print(data)

def nuclear_library_builder():
    clear_all(main_frame)
    nuclear_library_frame = tk.Frame(master=main_frame, background="white",width=app_w,height=app_h)
    nuclear_library_frame.pack(fill="both",expand=True)
    topbar_frame(nuclear_library_frame,menu_frame_builder,"home")

    nuclear_library_frame_scroll = ctk.CTkScrollableFrame(master=nuclear_library_frame,fg_color="white")
    nuclear_library_frame_scroll.pack(fill="both",expand=True)

    library_section_builder(nuclear_library_frame_scroll,image_3, "test")
    library_section_builder(nuclear_library_frame_scroll,image_6, "binding_energy")
    library_section_builder(nuclear_library_frame_scroll,image_7, "alfa_scattering")
    library_section_builder(nuclear_library_frame_scroll,image_4, "beta_scattering")
    library_section_builder(nuclear_library_frame_scroll,image_5, "rutherford")

def menu_frame_builder():
    clear_all(main_frame)
    menu_width = int((app_w/100)*25)
    manu_height = int((app_h/100)*80)
    menu_frame = tk.Frame(master=main_frame,background="white",width=menu_width, height=manu_height)
    menu_frame.pack(fill="y",expand=True)
    menu_frame.pack_propagate(False)
    menu_frame_lbl_header = tk.Label(master=menu_frame,text="Welcome to nucleo!", font=main_font, background="white",anchor="center")
    menu_frame_img_label = tk.Label(master=menu_frame,image=main_image,background="white")
    menu_frame_img_label.pack(pady=20)
    menu_frame_lbl_header.pack(side="top", fill="x",pady=20)

    main_btn_1 = tk.Button(master=menu_frame,text="Periodic Table",anchor="center",font=main_font,border=0,highlightcolor="red",highlightthickness=0,activebackground="gray",command=periodic_table_builder)
    main_btn_1.pack(side="top",fill="x",pady=3,padx=5)

    main_btn_2 = tk.Button(master=menu_frame,text="Atomic Info",anchor="center",font=main_font,border=0,highlightcolor="red",highlightthickness=0,activebackground="gray",command=atomic_info_builder)
    main_btn_2.pack(side="top",fill="x",pady=3,padx=5)

    main_btn_3 = tk.Button(master=menu_frame,text="Library",anchor="center",font=main_font,border=0,highlightcolor="red",highlightthickness=0,activebackground="gray",command=nuclear_library_builder)
    main_btn_3.pack(side="top",fill="x",pady=3,padx=5)

    main_btn_4 = tk.Button(master=menu_frame,text="Credits",anchor="center",font=main_font,border=0,highlightcolor="red",highlightthickness=0,activebackground="gray")
    main_btn_4.pack(side="top",fill="x",pady=3,padx=5)

    main_btn_5 = tk.Button(master=menu_frame,text="Privacy & Terms",anchor="center",font=main_font,border=0,highlightcolor="red",highlightthickness=0,activebackground="gray")
    main_btn_5.pack(side="top",fill="x",pady=3,padx=5)

    main_btn_5 = tk.Button(master=menu_frame,text="Help",anchor="center",font=main_font,border=0,highlightcolor="red",highlightthickness=0,activebackground="gray",background="orange",foreground="white")
    main_btn_5.pack(side="top",fill="x",pady=3,padx=5)
    

    menu_frame_lbl_endmenu = tk.Label(master=menu_frame,text="Created by Enes Yıldırım", font=mini_font, background="white",anchor="center")
    menu_frame_lbl_endmenu.pack(side="bottom", fill="x",pady=20)



main_win = tk.Tk()

image_1 =  Image.open("images/nuclearphysics.png")
image_1 = image_1.resize((300,300))
main_image = ImageTk.PhotoImage(image_1)

image_2 =  Image.open("images/periodictable.png")
image_2 = image_2.resize((int(image_2.width/3),int(image_2.height/3)))
img_periodic_table =ImageTk.PhotoImage(image_2)

image_3 = Image.open("images/atomic_bomb.png")
image_3 = image_3.resize((250,250))
image_3 = ImageTk.PhotoImage(image_3)

image_4 = Image.open("images/beta_scattering.jpeg")
image_4 = image_4.resize((int(image_4.width/0.95),int(image_4.height/0.95)))
image_4 = ImageTk.PhotoImage(image_4)

image_5 = Image.open("images/rutherford_theta.jpg")
image_5 = image_5.resize((250,250))
image_5 = ImageTk.PhotoImage(image_5)

image_6 = Image.open("images/binding.png")
image_6 = image_6.resize((250,250))
image_6 = ImageTk.PhotoImage(image_6)

image_7 = Image.open("images/alfa_scatterx.png")
image_7 = image_7.resize((int(image_7.width/5),int(image_7.height/5)))
image_7 = ImageTk.PhotoImage(image_7)

icon = ImageTk.PhotoImage(file="images/lion.png")
main_win.iconphoto(False,icon)

main_win.title("nucleo")

screen_h = main_win.winfo_screenheight()
screen_w = main_win.winfo_screenwidth()

app_w = int(screen_w/1.25)
app_h = int(screen_h/1.25)

main_win.geometry(f"{app_w}x{app_h}+{int(screen_w*(0.5))-int(app_w*(0.5))}+{int(screen_h*(0.5))-int(app_h*(0.5))}")
main_win.minsize(width=app_w, height=app_h)

main_frame = tk.Frame(master=main_win,background="white")
main_frame.pack(fill="both",expand=True)
main_frame.pack_propagate(False)
## define menu
menu_frame_builder()

main_win.mainloop()