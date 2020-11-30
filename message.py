
class Message:

    def __init__(self, Mtype, sender, receiver,resource,policy): #Set the values in the constructor
        self.Mtype= Mtype #offer or request
        self.sender= sender #from
        self.receiver= receiver #to
        self.resource= resource #First value from json
        self.policy = policy #Second value from json

    def displayMessage(self): #Printing the values
        print ("Type:", self.Mtype, "Sender:", self.sender, "Receiver:", self.receiver, "Resource:",self.resource, "Policy:", self.policy)

    def checkMtype(self):
        if self.Mtype == "request":
            print("This exchanges requests this resource:",self.resource, "from:", self.receiver)
        else:
            print("This exchanges offers this resource:", self.resource, "from:", self.sender)

def main():
    print ("Welcome to testing a message creation\n") #Asking for user input just to test
    Mtype = input("Enter in the message type [request/offer]:\n")
    sender = input("Enter in the message sender:\n")
    receiver = input("Enter in the message receiver:\n")
    resource = input("Enter in the message resource:\n")
    policy = input("Enter in the message policy:\n")

    mess1 = Message(Mtype, sender, receiver,resource,policy) #Instance of message
    mess1.displayMessage() #DisplayMessage
    mess1.checkMtype()


if __name__ == "__main__":
    main()