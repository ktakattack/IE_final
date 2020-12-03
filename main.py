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
    print("create initial message, type: " + M1.Mtype + " sender: " + M1.sender + " receiver: " + M1.receiver + " credential: " + M1.credentials + " sources: " + M1.sources + " resources: " + M1.resource)

    print("Initializing communication protocol and enqueueing first message")
    communication_protocol(M1)

def communication_protocol(msg):
    messageQueue.put(msg) #insert first message

    while(not messageQueue.empty()): #will run as long as messageQueue still has pending messages
        currentMsg = messageQueue.get() #dequeue next message in line
        
        for peer in PeerList:
            if peer.PeerName == currentMsg.receiver: #search list of peers for PeerName matching msg.receiver name
                resultMsgs = peer.Receive_Message(currentMsg) #calls the receiver Peer's ResolutionResolver, it should return a new message/list of messages if more requests/offers need to be sent, it will be an empty list if not
                for msg in resultMsgs:#enqueue new messages
                    messageQueue.put(resultMsgs.get())
            else:
                print("Message recipient not found.")



if __name__ == '__main__':
    main()
