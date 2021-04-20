import datetime
filename=input("Enter filename: ")
file = open(filename,"rb")
image= file.read()
file.close()

image= bytearray(image)
key=48


for i,j in enumerate(image):
    image[i]= j^key
   
file= open("encrypted_image.jpg","wb")
file.write(image)
file.close()
date=datetime.datetime.now()
print("encrypted and save as encrypted_image.jpg on %s",date)
