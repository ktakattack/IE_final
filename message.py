
class Message:
    def __init__(self, Mtype, sender, receiver,credential,source,resource): #Set the values in the constructor
        self.Mtype= Mtype #"offer"/"request"
        self.sender= sender
        self.receiver= receiver 
        self.credential= credential # array, i.e. ["C1","C2"]
        self.source= source # array, matches to credentials, i.e. credentials[0]="C2", source[0]="AS1"
        self.resource= resource
        #self.policy = policy #Second value from json