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
    
    def __init__(self, data):
        self.PeerName = data
        print("Initializing " + self.PeerName)

        with open(self.PeerName + "_Policy.json",'r') as Mypolicy:  # substitute Peer Name with current peer name ( AS_2,Client,..)
            self.PolicyVault= json.load(Mypolicy)
        print (self.PolicyVault, self.PeerName + '_Policy_Vault')

        with open(self.PeerName + "_Resource.json",'r') as MyCredentials:  # substitute Peer Name with current peer name ( AS_2,Client,..)
            self.ResourceVault= json.load(MyCredentials)
        print (self.ResourceVault, self.PeerName + '_Resource_Vault')
        
    def Send_Message(self, m, receiver):
        print ("Sending message (type: " + m.Mtype + ", resource: " + m.resource + ") to: " + receiver.PeerName)
        
    def Receive_Message(self, m, sender):
        print("Received message (type: " + m.Mtype + ", resource: " + m.resource + ") from: " + sender.PeerName)
    
    # def ResolutionResolver(m):
        # if m.type == "offer":
            # calculate new disclousre Dnew that Pthis will send to other parties
            # Dunlock.put(m.credential)
            # Dnew = (intersection(Dunlock,Qrecievd)-Dsent)  # intersect and - need code
            
        # elif m.type=="request":
            # if m.credential in Dunlock:
                # Dnew={m.credential}
            # else:
                # calculate new Qnew that pthis will request from others, based on th epolicy
                # Drelevent= peer.policy.credential # the policy for the credential requested
                # Qnew= Drelevent - Drecived-Qsent
        # return (#list of messages M composed of offered credentials in Dnew and requests for credentials in Qnew - offer and request # enqueue then in Mreceived )
            
			