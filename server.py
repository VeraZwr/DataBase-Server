'''
Created on Mar 15, 2018

@author: Weiran Zhao
'''
import socketserver

#def hasNumber(inputString):
#    return any(char.isdigit() for char in inputString)

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """


    def handle(self):
        DB={}
        strout=""
        avalue=[]
        strname=""
        strmid=""
        name_list=[]
        strfin=""
        #open data.txt and put into server 
        with open("data.txt") as inputFile:
            #read line by line
            for line in inputFile:
                #split each line into words in list named element
                element=line.split('|')
                i = 0 
                while i < len(element):
                    if element[i]=="":
                        element[i]=None
                    i+=1
                if element[0]==None:
                    continue
                elif element[0][0].isdigit():
                    continue
                else:
                    #set first string as key of the dectionary, which is name
                    DB[element[0]]=element[1:4]
                    name_list.append(element[0])
        print(DB)        
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        # chast recevied data into string
        inputInfo=str(self.data,"utf-8").split(',')
        print(inputInfo)
        while inputInfo[0] != "8":
            if inputInfo[0]=="1":
                #search name
                for name in name_list:
                    #if find the name
                    if inputInfo[1]==name:
                        #use a string to store all the info of that name
                        print(DB.get(name))
                        #create a final output by the specific for
                        strout="|".join(str(x)for x in DB.get(name))
                        print(strout)
                        strfin=name+"|"+strout+"\n"
                        print(strfin)
                        break
                    else:
                        strfin=inputInfo[1]+" not found in data base"
            elif inputInfo[0]=="2":
                for name in name_list:
                    #print(name)
                    print(inputInfo[1]+"1")
                    if inputInfo[1] == name:
                        strfin="Customer is already exist"
                    else:
                        strname=inputInfo[1]
                        DB[inputInfo[1]]=inputInfo[2:]
                        name_list.append(inputInfo[1])
                        print(name_list)
                        avalue=DB.get(inputInfo[1])
                        strout="|".join(str(x)for x in avalue)
                        print(strout)
                        strmid=strname+"|"+strout
                        print("strmid")
                        strfin="Add: "+strmid+"\n\n"
                        print("strfin")
                        break
            elif inputInfo[0]=="3":
                for name in name_list:
                    if inputInfo[1] == name:
                        strname=inputInfo[1]
                        avalue=DB.get(inputInfo[1])
                        strout="|".join(str(x)for x in avalue)
                        strmid=strname+"|"+strout
                        strfin="Delete: "+strmid+"\n\n"
                        del DB[inputInfo[1]]
                        j=0
                        while j<len(name_list):
                            if name_list[j]==strname:
                                del name_list[j]
                                break
                            else:
                                j=j+1
                        break
                    else:
                        strfin="The customer you want to delete does not exist"
            elif inputInfo[0]=="4":
                for name in name_list:
                    if inputInfo[1]==name:
                        strname=inputInfo[1]
                        DB[inputInfo[1]][0]=inputInfo[2]
                        avalue=DB.get(inputInfo[1])
                        strout="|".join(str(x)for x in avalue)
                        strmid=strname+"|"+strout
                        strfin="After age update "+strmid+"\n\n"
                        break
                    else:
                        strfin="The customer you want to update age does not exist"
            elif inputInfo[0]=="5":
                for name in name_list:
                    if inputInfo[1]==name:
                        strname=inputInfo[1]
                        DB[inputInfo[1]][1]=inputInfo[3]
                        avalue=DB.get(inputInfo[1])
                        strout="|".join(str(x)for x in avalue)
                        strmid=strname+"|"+strout
                        strfin="After address update: "+strmid+"\n\n"
                        break
                    else:
                        strfin="The customer you want to uppdate address does not exist"
            elif inputInfo[0]=="6":
                for name in name_list:
                    if inputInfo[1]==name:
                        strname=inputInfo[1]
                        DB[inputInfo[1]][2]=inputInfo[4]
                        avalue=DB.get(inputInfo[1])
                        strout="|".join(str(x)for x in avalue)
                        strmid=strname+"|"+strout
                        strfin="After phone number update: "+strmid+"\n\n"
                        break
                    else:
                        strfin="The customer you want to update phone does not exist"
            elif inputInfo[0]=="7":
                name_list.sort()
                #print(name_list)
                for name in name_list:
                    strname = name
                    avalue=DB.get(strname)
                    strout="|".join(str(x)for x in avalue)
                    strmid=strname+"|"+strout+"\n"
                    print(strmid)
                    strfin=strfin+strmid
                    print(strfin)
                strfin="\n** Python DB contents **\n"+strfin+"\n"
                
            self.request.sendall(strfin.encode())
            strfin=""
            self.data = self.request.recv(1024).strip()
            inputInfo=str(self.data,"utf-8").split(',')
        #print("sented")
        #self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()


    
       
        
