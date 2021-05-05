import tkinter as tk
HEIGHT = 500
WIDTH= 600

def encrypt_fxn(str1,key):
    file = open('input1_str.asm','w')
    file.write(str1)
    file.close()
    file = open('input2_key.asm','w')
    file.write(key)
    file.close()
    e="encrypted string"
    print(str1,"string encrypted to",e)
    L3['text']= "ENCRYPTED STRING IS "+str(e)
    

def decrypt_fxn(str1,key):
    file = open('input1_str.asm','w')
    file.write(str1)
    file.close()
    file = open('input2_key.asm','w')
    file.write(key)
    file.close()
    d="decrypted string"
    print(str1,"string decrypted to",d)
    L3['text']="DECRYPTED STRING IS "+str(d)

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT ,width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#7bc5e3')
frame.place(relx=0.05, rely=0.05 , relwidth=0.9, relheight=0.9)

label= tk.Label(frame, text="Xor Encryption and Decryption",font='40', bg='#a5e4f2')
label.pack()

L1=tk.Label(frame, text="Enter String" ,font='20')
L1.place(relx=0.1, rely=0.15 , relwidth=0.35, relheight=0.06)
entry1= tk.Entry(frame,text="Enter string 1", bg='#fff5de')
entry1.place(relx=0.5, rely=0.15 , relwidth=0.45, relheight=0.06)

L2=tk.Label(frame, text="Enter KEY",font='20')
L2.place(relx=0.1, rely=0.25 , relwidth=0.35, relheight=0.06)
entry2= tk.Entry(frame, bg='#fff5de')
entry2.place(relx=0.5, rely=0.25 , relwidth=0.45, relheight=0.06)

button = tk.Button(frame, text="Encrypt", bg='#56cc91' , command=lambda:encrypt_fxn(entry1.get(),entry2.get()))
button.place(relx=0.2, rely=0.4 , relwidth=0.2, relheight=0.1)
button = tk.Button(frame, text="Decrypt", bg='#db6063' , command= lambda:decrypt_fxn(entry1.get(),entry2.get()))
button.place(relx=0.6, rely=0.4, relwidth=0.2, relheight=0.1)

L3=tk.Label(frame, font='20')
L3.place(relx= 0.1 , rely= 0.65 , relwidth= 0.8 , relheight= 0.3)


 

root.mainloop()
