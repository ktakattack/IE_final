
class Message:
    def __init__(self, Mtype, sender, receiver,credentials,sources,resource): #Set the values in the constructor
        self.Mtype= Mtype #"offer"/"request"
        self.sender= sender
        self.receiver= receiver 
        self.credentials= credentials # array, i.e. ["C1","C2"]
        self.sources= sources # array, matches to credentials, i.e. credentials[0]="C2", source[0]="AS1"
        self.resource= resource
        #self.policy = policy #Second value from json