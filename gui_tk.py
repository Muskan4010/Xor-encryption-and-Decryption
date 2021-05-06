import tkinter as tk
import subprocess
import time
from tkinter import filedialog

HEIGHT = 500
WIDTH= 600

# Open up desired program
def open_emulator(str1, key):

    write_asm_code_in_file(str1,key)

    #* set your emulator and asm files path
    emulator_path = 'C:\emu8086\emu8086.exe'
    # asm_path = 'D:\Work\JIIT\COA_Project\Xor-encryption-and-Decryption\myfile_edit.asm'

    #* Or just pick the program and file using file explorer
    #emulator_path = filedialog.askopenfilename()
    asm_path = filedialog.askopenfilename()

    subprocess.call(
        [emulator_path, asm_path])

    # intentional delay
    time.sleep(8)

    encrypt_fxn(str1,key)

def write_asm_code_in_file(str1,key):
    
    while(len(str1)>len(key)):
        key=key+key
    key = key[0:len(str1)]
    
    fin = open("XOR_3.asm", "rt")
    data = fin.read()
    data = data.replace('abcd', str1)
    data = data.replace('1234', key)
    fin.close()
    fout = open("myfile_edit.asm", "wt")
    fout.write(data)
    fout.close()


def encrypt_fxn(str1,key):

    fin=open("C:\emu8086\MyBuild\myfile.txt", "rt")
    e=fin.read()
    fin.close
    e.decode("utf-8")
    print(str1,"string encrypted to",e)
    L3['text']= "ENCRYPTED STRING IS "+str(e)
    

#def decrypt_fxn(str1,key):
#    d="decrypted string"
#    print(str1,"string decrypted to",d)
#    L3['text']="DECRYPTED STRING IS "+str(d)

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


button = tk.Button(frame, text="Encrypt", bg='#56cc91',
                   command=lambda: open_emulator(entry1.get(), entry2.get()))
button.place(relx=0.3, rely=0.4 , relwidth=0.4, relheight=0.1)
# button = tk.Button(frame, text="Decrypt", bg='#db6063' , command= lambda:decrypt_fxn(entry1.get(),entry2.get()))
# button.place(relx=0.6, rely=0.4, relwidth=0.2, relheight=0.1)

L3=tk.Label(frame, font='20')
L3.place(relx= 0.1 , rely= 0.65 , relwidth= 0.8 , relheight= 0.3)

root.mainloop()
