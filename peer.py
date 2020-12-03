from message import Message
from queue import Queue

import json

class Peer:
    PeerName = ""  # RS,AS_2,AS_3,Client
    Qsent={} # set of credentials pthis requested from others
    Qrecievd={} # set of credentials others requested from pthis
    Qnew={} # return list of credentials required (requests)
    Dsent={} # set of credentials pthis sent to others
    Dreceived ={} #set of credentials pthis received from others
    Dunlock={} # set of all credentials unlocked by d and other disclusure in Dreceived
    Dnew={} # return list of credentials already available (offers)
    PolicyVault = dict #i.e. {"C4": "True"}
    ResourceVault = dict #i.e. {"C4": "alice@kent.edu"}
    
    #TODO: Add code to initialize peer with list of unlocked credentials(Dunlock?), i.e. Client has C4 from Client_Resource.json, RS has C1 from RS_Resource.json, etc
    def __init__(self, data):
        self.PeerName = data

        with open(self.PeerName + "_Policy.json",'r') as Mypolicy: #set PolicyVault from json
            self.PolicyVault= json.load(Mypolicy)

        with open(self.PeerName + "_Resource.json",'r') as MyCredentials:  # set ResourceVault from json
            self.ResourceVault= json.load(MyCredentials)
    
    def send_Message(self):
        print ("unused function")

    def Receive_Message(self, m):
        return self.ResolutionResolver(m)
    
    def ResolutionResolver(self, m):
        OfferList = []
        RequestList = []
        resultMsgQueue = Queue()

        if m.Mtype == "offer":
            # calculate new disclosure Dnew that Pthis will send to other parties
            self.ResourceVault[m.credential] = m.resource
            self.PolicyVault[m.credential] = "True" #automatically set received resources to free share
            print(self.PeerName + " received offer of [Credential: " + m.credential + ", resource: " + str(m.resource).strip('[]') + "] from " + m.sender + ". Added credential/resource to " + self.PeerName + ".ResourceVault.")
            print(self.PeerName + ".ResourceVault contains:")
            print(self.ResourceVault.items())
            
            #Dnew = (intersection(Dunlock,Qrecievd)-Dsent)  # intersect and - need code
            
        elif m.Mtype=="request":
            print(self.PeerName + " received request for credential: " + m.credential + ".")

            OfferedCredentials = m.resource

            if m.credential in self.ResourceVault:
                if(self.PolicyVault[m.credential] == "True"):
                    print("Policy is True, offer resource.")
                    OfferList.append(m.credential)
                else:
                    RequiredCredentialsArray = self.PolicyVault[m.credential][1:-1].split(',') #converts policy to array of required credentials i.e. "[C2, C3]" -> ["C2","C3"]
                    for cred in RequiredCredentialsArray:
                        if cred in OfferedCredentials: #if required credential is already offered in message, skip
                            continue
                        else: #if required credential not in message, add to request list
                            RequestList.append(cred)
                    if not RequestList: #if required credentials list is empty, go ahead and offer the resource
                        OfferList.append(m.credential)
            
            else:
                print(self.PeerName + " does not have this resource.")
                # # calculate new Qnew that pthis will request from others, based on the policy
                # Drelevent= peer.policy.credential # the policy for the credential requested
                # Qnew= Drelevent - Drecived-Qsent
        
        for offer in OfferList:
            resultMsgQueue.put(Message("offer", self.PeerName, m.sender, offer, [], [self.ResourceVault[offer]]))

        return resultMsgQueue #list of messages M composed of offered credentials in Dnew and requests for credentials in Qnew - offer and request, enqueue them in Mreceived
            
# How to get credentials/sources from dictionary:
# RSPolicyValue = RS.PolicyVault["C1"][1:-1], 
# RSPolicyValue = RSPolicyValue.split(',')
# 
# printing those values:
# for obj in RSPolicyValue:
#     print(obj)

# Message flow:
# Client (Request C1) -> 
# RS (Request C2, C3) -> 
# Client (Request C2) -> 
# AS1 (Offer C2 Resource) -> 
# Client (Request C3) -> 
# AS2 (Request C4) -> 
# Client (Offer C4 Resource) -> 
# AS2 (Offer C3 Resource) -> 
# Client (Offer C2/C3 Resources) ->
# RS (Offer C1 Resource) -> 
# Client (Received Requested C1 Resource, done)