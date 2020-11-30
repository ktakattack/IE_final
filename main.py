import peer
import message
import resolution

AS1=Peer()
AS2=Peer()
Client=Peer()
Resource=Peer()

def main():
    print("main is running")

#Client (Request C1) -> 

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
