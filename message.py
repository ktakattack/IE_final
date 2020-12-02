
class Message:
    #Kristi- uncertain how to initialize these
    def __init__(self, Mtype, sender, receiver,credential,sources): #Set the values in the constructor
        self.Mtype= Mtype #offer or request
        self.sender= sender #from
        self.receiver= receiver #to
        self.credential= credential #First value from json
        self.sources= sources
        #self.policy = policy #Second value from json


# def main():
#     print ("Welcome to testing a message creation\n") #Asking for user input just to test
#     Mtype = input("Enter in the message type [request/offer]:\n")
#     sender = input("Enter in the message sender:\n")
#     receiver = input("Enter in the message receiver:\n")
#     resource = input("Enter in the message resource:\n")
#     policy = input("Enter in the message policy:\n")

#     mess1 = Message(Mtype, sender, receiver,resource,policy) #Instance of message
#     mess1.displayMessage() #DisplayMessage
#     mess1.checkMtype()


# if __name__ == "__main__":
#     main()