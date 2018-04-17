import isaac_agent as agent
import window_controls as wc
import random
import server

class IsaacNN:
    def __init__(self):
        pass

def random_test(player):
    while True:
        player.unpause()
        server.receive()

        r = random.randint(0,4)
        player.move(r)

def test(player):
    while True:
        player.unpause()
        server.receive()

# Get user data and save to a text file
def train(player):
    print("Training, quit program to finish training")
    f = open("training_data.csv", "a+")
    while True:
        player.unpause()
        data = server.receive()
        to_write = data.decode("utf-8")
        to_write = to_write.replace(" ", ",")
        if(to_write[:7] != '0,0,0,0' and to_write[8:] != '0,0'): # If there are no enemies, don't record any data
            f.write(to_write+"\n")
    f.close()

# The main loop
if __name__ == "__main__":
    player = agent.IsaacAgent()
    while True:
        user_in = input("Program running...\nControls:\n\tTrain (t)\n\tExecute (e)\n\tQuit(q)\n")
        if(user_in == "t"):
            train(player)
        if(user_in == "e"):
            test(player)
        if(user_in == "q"):
            break
        
        
