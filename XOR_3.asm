name "xor"

org 100h

jmp start

m1:
s db 'abcd'
s_size = $ - m1
  db 0Dh,0Ah,'$'

k db '1234' 

filename db "myfile.txt", 0

start:

;pointers
lea di, s
lea si, k

;storing size in cx for loop
mov cx, s_size

;loop!
next_char:
    mov al, [di]
    mov bl, [si]
    xor al, bl
    mov [di], al
    inc di
    inc si
loop next_char
       
;let's print it:       
mov ah, 9
mov dx, offset s
int 21h 

;storing in file:
mov cx, 0
mov dx, offset filename 
mov ah, 3ch 
int 21h
         
mov bx, offset filename
mov cx, s_size
mov dx, offset s
mov ah, 40h
int 21h         



; wait for any key press:
mov ah, 0
int 16h

ret