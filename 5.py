class CallDetail:
    def __init__(self):
        self.dailer = None
        self.receiver = None
        self.duration = None
        self.calltype = None
    def set_details(self,y):
        self.dailer = y[0]
        self.receiver = y[1]
        self.duration = y[2]
        self.calltype = y[3]
        self.getdetails()
    def getdetails(self):
        print(self.dailer.ljust(20),end=" ")
        print(self.receiver.ljust(20),end=" ")
        print(self.duration.ljust(20),end=" ")
        print(self.calltype.ljust(20))
        
class util:
    def __init__(self):
        self.list_of_call_Objects= []

    def parse_customer(self,list_of_call_string):
        for x in range(len(list_of_call_string)):
            y=list_of_call_string[x].split(",")
            self.list_of_call_Objects.append(CallDetail())
            self.list_of_call_Objects[x].set_details(y)
            


call = '9108109861,8050757308,60,ISD'
call1 = '9108109861,9741691292,50,Local'
call2 = '9108109861,8150055436,40,STD'
list_of_call_string=[call,call1,call2]

print("Dailer".ljust(20),end=" ")
print("Receiver".ljust(20),end=" ")
print("Duration".ljust(20),end=" ")
print("Type".ljust(20))
util().parse_customer(list_of_call_string)
