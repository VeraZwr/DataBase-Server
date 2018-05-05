'''
Created on Mar 15, 2018

@author: Vera Zhao
'''
import socket
import sysconfig

import socket
import sys

HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])
name=""
age=""
address=""
phone=""
select=""
# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST,PORT))
    print("Python DB Menu:\n\n 1. Find customer\n 2. Add cutomet\n 3. Delete customer\n 4. Update customer age\n 5. Update customer address\n 6. Update customer address\n 7. Print report\n 8. Exit\n\n")
    
    while select != '8':
        select = input("Select:").strip(' ')
        if select =='8':
            print ("Good bye")
            break
        else:
            #find customer
            if select == '1':
                name = input("Enter customer name: ").strip(' ')
                userStr="1"+","+name+","+","+","
            #add customer
            elif select == '2':
                name=input("Enter customer name: ").strip(' ')
                age=input("Enter age: ").strip(' ')
                address=input("Enter address: ").strip(' ')
                phone=input("Enter phone: ").strip(' ')
                userStr="2"+","+name+","+age+","+address+","+phone
            #delete customer
            elif select == '3':
                name=input("Enter customer name: ").strip(' ')
                userStr="3"+","+name+","+","+","
            
            elif select == '4':
                name = input("Enter customer name: ").strip(' ')
                age = input ("Enter age: ").strip(' ')
                userStr="4"+","+name+","+age+","+","
            elif select == '5':
                name = input("Enter customer name: ").strip(' ')
                address = input ("Enter address: ").strip(' ')
                userStr="5"+","+name+","+","+address+","
            elif select == '6':
                name = input("Enter customer name: ").strip(' ')
                phone = input("Enter phone number: ").strip(' ')
                userStr="6"+","+name+","+","+","+phone
            else:
                userStr='7'
                
        sock.sendall(bytes(userStr, "utf-8"))
        userStr=""
        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
        print("Server response: "+received)

    


    
        
          
    