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
    
    def __init__(self):
        with open("<PeerName>.json",'r') as Mypolicy:  # substitute Peer Name with current peer name ( AS_2,Client,..)
            self.PolicyVault= json.load(Mypolicy)
        print (self.PolicyVault, '<PeerName>_Policy_Vault')

        with open("<PeerName>.json",'r') as MyCredentials:  # substitute Peer Name with current peer name ( AS_2,Client,..)
            self.ResourceVault= json.load(MyCredentials)
        print (self.ResourceVault, 'EX.Email')
        
    def Send_Message(self, m, receiver):
        print ("Sending message (type: " + m.Mtype + ", resource: " + m.resource + ") to: " + receiver)
        
    def Receive_Message(self, m, sender):
        print("Received message (type: " + m.Mtype + ", resource: " + m.resource + ") from: " + sender)
    
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
            
			