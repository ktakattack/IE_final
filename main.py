from peer import Peer
from message import Message



def main():
    AS1=Peer("AS1")
    AS2=Peer("AS2")
    Client=Peer("Client")
    RS=Peer("RS")

    print(RS.PolicyVault["C1"])

    RSPolicyValue = RS.PolicyVault["C1"][1:-1]
    RSPolicyValue = RSPolicyValue.split(',')

    for obj in RSPolicyValue:
        print(obj)
    
    print("main is running")

#Client (Request C1) -> 
    M1 = Message("request", "Client", "RS", "C1", [])

    Client.Send_Message(M1)
    RS.Receive_Message(M1)

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

if __name__ == '__main__':
    main()
