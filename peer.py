from message import Message
from queue import Queue

import json

class Peer:
    PeerName = ""  # RS,AS_2,AS_3,Client
    PolicyVault = dict #i.e. {"C4": "True"}
    ResourceVault = dict #i.e. {"C4": "alice@kent.edu"}
    PendingRequests = []
    PendingOffers = {}
    CredentialList = []

    def __init__(self, data):
        self.PeerName = data

        with open(self.PeerName + "_Policy.json",'r') as Mypolicy: #set PolicyVault from json
            self.PolicyVault= json.load(Mypolicy)

        with open(self.PeerName + "_Resource.json",'r') as MyCredentials:  # set ResourceVault from json
            self.ResourceVault= json.load(MyCredentials)

        if self.PeerName == 'Client':
            self.PendingRequests.append("C1")

    #def send_Message(self):
    #    print ("unused function")

   # def Receive_Message(self):
    #    print ("Discount is valid")

    def ResolutionResolver(self, m):
        OfferList = []
        RequestList = []
        SourceList = []
        RequestDict = {} #Key = RequestCred, Value = Source
        resultMsgQueue = Queue()

        if m.Mtype == "offer":

            if(m.resource =="C3"):
                self.ResourceVault[m.credential] = m.resource
                self.PolicyVault[m.credential] = m.credential #"True" #automatically set received resources to free share
                print(self.PeerName + " received offer of [Credential: " + m.credential + ", resource: " + str(m.resource).strip('[]') + "] from " + m.sender + ". Added credential/resource to " + self.PeerName + ".ResourceVault.")
                print(self.PeerName + ".ResourceVault contains:")
                #print(self.ResourceVault.items())
                print( " PolicyVault ")
                print(self.PolicyVault.items())
                #print( " PendingOffers: ")
                #print(self.PendingOffers.items())

            else:
                self.ResourceVault[m.credential] = m.resource
                self.PolicyVault[m.credential] = "True" #automatically set received resources to free share
                print(self.PeerName + " received offer of [Credential: " + m.credential + ", resource: " + str(m.resource).strip('[]') + "] from " + m.sender + ". Added credential/resource to " + self.PeerName + ".ResourceVault.")
               # print(self.PeerName + ".ResourceVault contains:")
                print( "PolicyVault ")
                print(self.PolicyVault.items())
               # print( " Resource ")
                #print(self.ResourceVault.items())

            for PendingRequest in self.PendingRequests:
                if PendingRequest in self.ResourceVault:
                    self.PendingRequests.remove(PendingRequest)


            # if(m.credential in self.PendingOffers.keys()):
            #     print(m.credential + " received from: " + m.sender + ". Releasing " + self.PendingOffers[m.credential] + " to " + m.sender)
            #     OfferList.append(self.PendingOffers[m.credential])

        elif m.Mtype=="request":
            print(self.PeerName + " received request for credential: " + m.credential + ".")

            OfferedCredentials = m.resource

            if m.credential in self.ResourceVault:
                if(self.PolicyVault[m.credential] == "True"):
                    print("Policy is True, offer resource.")
                    OfferList.append(m.credential)
                else:
                    PolicyArray = self.PolicyVault[m.credential][1:-1].split(',') #converts policy to array of required credentials i.e. "[C2,AS1,C3,AS2]" -> ["C2","AS1","C3","AS2"]
                    i = 0
                    for obj in PolicyArray: #splitting policy vault into requested credential (even number), sources (odd number)
                        if(i%2 == 0):
                            RequestList.append(obj)
                        else:
                            SourceList.append(obj)
                        i += 1

                    print(m.credential + " requires the following resources: ")
                    j = 0
                    for cred in RequestList:
                        print(cred)
                    for cred in RequestList:
                        if cred in OfferedCredentials: #if required credential is already offered in message, skip
                            print(cred + " is in OfferedCredentials, skipping.")
                            continue
                        else: #if required credential not in message, add to request list
                            print(cred + " not found. Adding to RequestDict.")
                            self.PendingOffers[cred] = m.credential
                            RequestDict[cred]=m.sender
                        j += 1
                    if not RequestList: #if required credentials list is empty, go ahead and offer the resource
                        print("All credentials received, offering " + m.credential + ".")
                        OfferList.append(m.credential)

            else:
                print(self.PeerName + " does not have this resource.")
                if(m.source):
                    print("Source list provided. Adding to RequestList: ")
                    if(m.credential == "C2"): #hardcoded, having issues
                        RequestDict[m.credential] = "AS1"
                    elif(m.credential == "C3"):
                        RequestDict[m.credential] = "AS2"
                    print("Request " + m.credential + " from " + RequestDict[m.credential])
                else:
                    print("No sources, please request with proper credential name.")

        # if self.PendingRequests:
        #     print(self.PeerName + " still has the following open requests: ")
        #     print(self.PendingRequests)
        #     print("Adding to RequestDict")

        #     for Resource in self.ResourceVault:
        #         self.CredentialList.append(Resource)

        #     for PendingRequest in self.PendingRequests: #hardcoded, not sure how to get actual source
        #         if(PendingRequest == "C1"):
        #             RequestDict[PendingRequest] = "RS"
        #         elif(PendingRequest == "C3"):
        #             RequestDict[PendingRequest] = "AS2"

        for offer in OfferList:
            print("Adding offer for " + offer + " from " + self.PeerName + " to " + m.sender + " to queue.")
            resultMsgQueue.put(Message("offer", self.PeerName, m.sender, offer, [], [self.ResourceVault[offer]]))

        for request in RequestDict:
            self.PendingRequests.append(request)
            print("Adding request from " + self.PeerName + " to get " + request + " from " + RequestDict[request] + " to queue.")
            if(SourceList):
                resultMsgQueue.put(Message("request", self.PeerName, RequestDict[request], request, SourceList, []))
            else:
                resultMsgQueue.put(Message("request", self.PeerName, RequestDict[request], request, [], []))

        return resultMsgQueue

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