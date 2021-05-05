name "xor"

org 100h

jmp start

m1:
s db 'iammusakna'
s_size = $ - m1
  db 0Dh,0Ah,'$'

k db 'gharis' 

filename db "myfile.txt", 0
handle dw ?

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
;mov ah, 9
;mov dx, offset s
;int 21h 

;creating a file:
mov ah, 3ch
mov cx, 0
mov dx, offset filename
int 21h
mov handle, ax

;storing in file:
mov ah, 40h         
mov bx, handle
mov dx, offset s
mov cx, s_size
int 21h

;closing the file
mov ah, 3eh
mov bx, handle
int 21h         

; wait for any key press:
mov ah, 0
int 16h

ret
