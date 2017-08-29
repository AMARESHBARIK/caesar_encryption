alphabet='abcdefghijklmnopqrstuvwxyz'
newmsg=''
msg=input('enter the message:')
key=int(input('enter the key u want:'))
for i in msg:
    if i in alphabet:
         pos=alphabet.find(i)
         newpos=(pos+key)%26
         newmsg+=alphabet[newpos]
    else:
        newmsg=newmsg+msg[i]

print('your coded msg is',newmsg)
         
