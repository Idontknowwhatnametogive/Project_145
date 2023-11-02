from tkinter import *
root=Tk()
root.title("Driving license")
root.geometry("400x300")

root.configure(bg="white")
canvas=Canvas(root,width=400,height=300)
canvas.create_image(0,0,anchor=NW)
canvas.create_rectangle(0, 0, 400, 55, fill = "red")
canvas.create_rectangle(0, 345, 300, 400, fill = "red")

label_heading = canvas.create_text(150,30, font=('Times', '24', 'bold italic'), text="Driving License")
label_name_tag = canvas.create_text(70,100, font=('Times', '10', 'bold'), text="Name: Winnie the Pooh ")
label__DOB_tag= canvas.create_text(80,130, font=('Times', '10', 'bold'), text="DOB: 21 August 1921 ")
label_Pno_tag = canvas.create_text(50,160, font=('Times', '10', 'bold'), text="Pno:451478 ")
label_Address_tag= canvas.create_text(110,190, font=('Times', '10', 'bold'), text="Address: Disney Land, Hong Kong")
abel_Authorisation_tag= canvas.create_text(150,220, font=('Times', '10', 'bold'), text="Authorisation to drive the follwing vechiles: Two four")

label_name = Label(root)
label_DOB = Label(root)
label_Pno = Label(root)

def myCardDetails():
    name= "Winnie the Pooh"
    print(type(name))
    DOB = "21 August 1921"
    Pno =["451478"]
    
    label_name['text'] = name
    label_DOB['text']=DOB
    label_Pno['text']=Pno
    
button1 =Button(root, text = "Show my ID Card", command=myCardDetails)
button1.configure(width = 20 , activebackground = "#9EC6EE", relief= FLAT) 
button1_window = canvas.create_window(150, 330, anchor=CENTER, window=button1) 
label_name_window = canvas.create_window(120, 165, anchor=CENTER, window=label_name) 
label_DOB_window = canvas.create_window(90, 205, anchor=CENTER, window=label_DOB)
label_Pno_window = canvas.create_window(155, 252, anchor=CENTER, window=label_Pno) 
canvas.pack()
    


root.mainloop()


