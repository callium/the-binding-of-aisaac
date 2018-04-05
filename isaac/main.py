import genetics_data_structures as gen
import isaac_agent as agent
import tensorflow as tf
import window_controls as wc
import random
import server
import time

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
    f = open("training_data.txt", "a+")
    f.write("------------------------------\n")
    while True:
        player.unpause()
        data = server.receive()
        to_write = data.decode("utf-8")
        if(to_write[:7] != '0 0 0 0'): # If there are no enemies, don't record any data
            f.write(to_write+"\n")
    f.close()

def interpret_data(data):
    print(data)

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
        
        
