from message import Message

import json

class Peer:
    PeerName = ""  # RS,AS_2,AS_3,Client
    # Qsent={} # set of credentials pthis requested from others
    # Qrecievd={} # set of credentials others requested from pthis
    # Qnew={}
    # Dsent={} # set of credentials pthis sent to others
    # Dreceived ={} #set of credentials pthis received from others
    # Dunlock={} # set of all credentials unlocked by d and other disclusure in Dreceived
    # Dnew={}
    PolicyVault = dict #i.e. {"C4": "True"}
    ResourceVault = dict #i.e. {"C4": "alice@kent.edu"}
    
    #TODO: Add code to initialize peer with list of unlocked credentials(Dunlock?), i.e. Client has C4 from Client_Resource.json, RS has C1 from RS_Resource.json, etc
    def __init__(self, data):
        self.PeerName = data
        # print("Initializing " + self.PeerName)

        with open(self.PeerName + "_Policy.json",'r') as Mypolicy:  # substitute Peer Name with current peer name ( AS_2,Client,..)
            self.PolicyVault= json.load(Mypolicy)
        # print (self.PolicyVault, self.PeerName + '_Policy_Vault')

        with open(self.PeerName + "_Resource.json",'r') as MyCredentials:  # substitute Peer Name with current peer name ( AS_2,Client,..)
            self.ResourceVault= json.load(MyCredentials)
        # print (self.ResourceVault, self.PeerName + '_Resource_Vault')
        
    def Send_Message(self, m):
        print ("Sending message (type: " + m.Mtype + ", resource: " + m.credential + ") to: ")
        
    def Receive_Message(self, m):
        # self.ResolutionResolver(m)
        print("Received message (type: " + m.Mtype + ", resource: " + m.credential + ") from: ")
    
    #m = {"request", Client, RS, "C1",[]} or m ={"offer", RS, Client, "20 % Discont",[]}
    def ResolutionResolver(m):
        if m.Mtype == "offer":
            #calculate new disclousre Dnew that Pthis will send to other parties
            Dunlock.put(m.credential)
            Dnew = (intersection(Dunlock,Qrecievd)-Dsent)  # intersect and - need code
            
        elif m.Mtype=="request":
            if m.credential in Dunlock: #need code to add credentials to list of unlocked credentials, i.e. RS has C1 from RS_Resource.json
                Dnew={m.credential} #if credential is in list of unlocked credentials then:
                if self.PolicyVault[m.credential] == "True" #it will check PolicyVault if true or an array of required credentials
                    

            elif m.sources: #if sources array is not empty
                #create new messages using sources i.e. m={"request",RS,Client,[C2,C3],[AS1,AS2]}
                print("new message")
            elif not m.sources:
                print("Invalid request, credential does not exist")
            else:
                #calculate new Qnew that pthis will request from others, based on th epolicy
                Drelevent= peer.policy.credential # the policy for the credential requested
                Qnew= Drelevent - Drecived-Qsent
        return (#list of messages M composed of offered credentials in Dnew and requests for credentials in Qnew - offer and request # enqueue then in Mreceived )

client.RequestSet = {"[C1,]"}, client.CredentialList{"[C4]"}
asdhjasdkjhakjhf
client.RequestSet = {"[C1,],[C2,],[C3,]"}
asdfkljhasfdkjh
client.ReceiveSet from AS1 {"[C2,ID810234567X]"}and AS2 {"[C3, Score780]"}, Client.ReceiveSet["[C2,ID810234567X],[C3, Score780]"], added to Client.CredentialList{"[C2,C3,C4]"} 
it also checks client.RequestSet = {"[C1,],[C2,],[C3,]"}/Client.ReceiveSet["[C2,ID810234567X],[C3, Score780]"] KEY INTERSECTION = {C2,C3}, 
so remove from RequestSet, result = Client.RequestSet{"[C1]"}
asdfasdfasdfhjk
client.ReceivesOffer = {"[C1, "20%"]"}, adds to ReceivedSet
client compares RequestSet to ReceivedSet and finds C1 in both, done