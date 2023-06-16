e_d = input("Press 'e' for encoding or 'd' for decoding:")
if(e_d != 'e' and e_d != 'd'):
   print("Invalid option")
   exit
k = input("Want random shift key 'y'/'n':")

if(k == 'y'):
    from random import random
    shift=int((random())*100)%26



text=input("Enter string to be encoded/decoded:")
if k == 'n':
    shift=int(input("Enter shift key:"))
shift%=26
if e_d == 'e':

    forw=""
    back=""

    for i in text:
        if i.isalpha():
            decoded_ord_forw=ord(i)+shift
            decoded_ord_back=ord(i)-shift
            if i.isupper():
                if decoded_ord_forw > ord('Z'):
                 decoded_ord_forw-=26
                if decoded_ord_back < ord('A'):
                 decoded_ord_back+=26
            elif i.islower():
                if decoded_ord_forw > ord('z'):
                    decoded_ord_forw-=26
                if decoded_ord_back < ord('a'):
                 decoded_ord_back+=26
            forw+=chr(decoded_ord_forw)
            back+=chr(decoded_ord_back)
        else:
            forw+=i
            back+=i
    print("Encoded strig:")

elif e_d == 'd':
    shift = -shift
    forw=""
    back=""

    for i in text:
        if i.isalpha():
            decoded_ord_forw=ord(i)-shift
            decoded_ord_back=ord(i)+shift
            if i.isupper():
                if decoded_ord_forw > ord('Z'):
                 decoded_ord_forw-=26
                if decoded_ord_back < ord('A'):
                 decoded_ord_back+=26
            elif i.islower():
                if decoded_ord_forw > ord('z'):
                    decoded_ord_forw-=26
                if decoded_ord_back < ord('a'):
                 decoded_ord_back+=26
            forw+=chr(decoded_ord_forw)
            back+=chr(decoded_ord_back)
        else:
            forw+=i
            back+=i
    print("Decoded string:")
    
print(abs(shift),"-> ",forw)
print(abs(shift),"<- ",back)

