from peer import Peer
from message import Message
from queue import Queue

#Notes:---------------------------------------------
# How to get credentials/sources from dictionary:
# RSPolicyValue = RS.PolicyVault["C1"][1:-1], 
# RSPolicyValue = RSPolicyValue.split(',')
# 
# printing those values:
# for obj in RSPolicyValue:
#     print(obj)
#
# Overall Message flow:
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
#----------------------------------------------------

#Global variables
AS1=Peer("AS1")
AS2=Peer("AS2")
Client=Peer("Client")
RS=Peer("RS")
PeerList = [AS1, AS2, Client, RS]
messageQueue = Queue()

def main():
    M1 = Message("request", "Client", "RS", "C1", [], [])
    #M1 = Message("request", "Client", "AS1", "C2", [], [])
    print("create initial message, type: " + M1.Mtype + " sender: " + M1.sender + " receiver: " + M1.receiver + " credential: " + M1.credential + " sources: " + str(M1.source).strip('[]') + " resources: " + str(M1.resource).strip('[]'))

    M2 = Message("offer", "AS2", "Client", "C3", [], [])
    #print("create initial message, type: " + M1.Mtype + " sender: " + M1.sender + " receiver: " + M1.receiver + " credential: " + M1.credential + " sources: " + str(M1.source).strip('[]') + " resources: " + str(M1.resource).strip('[]'))

    M3 = Message("offer", "Client", "RS", "C2", [], [])
    M4 = Message("offer", "Client", "RS", "C3", [], [])
    M5 = Message("offer", "RS", "Client", "C1", [], [])


    print("Initializing communication protocol and enqueueing first message")
    communication_protocol(M1)
    #print("M1")

    communication_protocol(M2)
    #print("M2")

    communication_protocol(M3)
    #print("M3")

    communication_protocol(M4)
    #print("M4")

    communication_protocol(M5)
    #print("M5")
    print("Receive discount")

def communication_protocol(msg):
    recipientFound = False
    messageQueue.put(msg) #insert first message

    while(not messageQueue.empty()): #will run as long as messageQueue still has pending messages
        currentMsg = messageQueue.get() #dequeue next message in line

        for peer in PeerList:
            if peer.PeerName == currentMsg.receiver: #search list of peers for PeerName matching msg.receiver name
                recipientFound = True
                resultMsgs = peer.ResolutionResolver(currentMsg) #calls the receiver Peer's ResolutionResolver, it should return a new message/list of messages if more requests/offers need to be sent, it will be an empty list if not
                while (not resultMsgs.empty()): #enqueue new messages if resultMsgs not empty
                    messageQueue.put(resultMsgs.get())


    if(not recipientFound):
        print("Message recipient not found.")


if __name__ == '__main__':
    main()
