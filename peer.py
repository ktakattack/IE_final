from message import Message

import json

class Peer:
    PeerName = ""  # RS,AS_2,AS_3,Client
    PolicyVault = dict #i.e. {"C4": "True"}
    ResourceVault = dict #i.e. {"C4": "alice@kent.edu"}

    #TODO: Add code to initialize peer with list of unlocked credentials(Dunlock?), i.e. Client has C4 from Client_Resource.json, RS has C1 from RS_Resource.json, etc
    def __init__(self, data):
        self.PeerName = data

        with open(self.PeerName + "_Policy.json",'r') as Mypolicy: #set PolicyVault from json
            self.PolicyVault= json.load(Mypolicy)

        with open(self.PeerName + "_Resource.json",'r') as MyCredentials:  # set ResourceVault from json
            self.ResourceVault= json.load(MyCredentials)

    def send_Message():
        print ("unused function")

    def Receive_Message(self, m):
        return self.ResolutionResolver(m)

    def ResolutionResolver(m):
        if m.type == "offer":
            # calculate new disclousre Dnew that Pthis will send to other parties
            Dunlock.put(m.credential)
            Dnew = (intersection(Dunlock,Qrecievd)-Dsent)  # intersect and - need code

        elif m.type=="request":
            if m.credential in Dunlock:
                Dnew={m.credential}
            else:
                # calculate new Qnew that pthis will request from others, based on th epolicy
                Drelevent= peer.policy.credential # the policy for the credential requested
                Qnew= Drelevent - Drecived-Qsent
        return (#list of messages M composed of offered credentials in Dnew and requests for credentials in Qnew - offer and request # enqueue then in Mreceived )


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