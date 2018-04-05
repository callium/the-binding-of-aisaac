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
def train(player, f):
    while True:
        player.unpause()
        data = server.receive()
        # data = decode(data, "utf-8")
        # Decode data and write to file
        # f.write(data+"\n")

def interpret_data(data):
    print(data)

# The main loop
if __name__ == "__main__":
    player = agent.IsaacAgent()
    while True:
        user_in = input("Program running...\nControls:\n\tTrain (t)\n\tExecute (e)\n\tQuit(q)\n")
        if(user_in == "t"):
            # Randomly test the deliberate movement mechanics
            # random_test(player)
            f = open("training_data.txt", "a+")
            f.write("-----\nNew Session\n-----\n")
            train(player, f)
            f.close()
        if(user_in == "e"):
            test(player)
        if(user_in == "q"):
            break
        
        
