'''This file contains much of the logic behind collecting training data and controlling the 
agent that actually plays the game. This is the file that you will run to do everything you want with the game'''

import isaac_agent as agent
import window_controls as wc
import isaac_estimator as inn
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
    conn = server.run_server()
    while True:
        player.unpause()
        data = server.receive(conn)
        to_write = data.decode("utf-8")
        to_write = to_write.replace(" ", ",")
        if(to_write[:7] != '0,0,0,0' and to_write[8:] != '0,0'): # If there are no enemies, don't record any data
            f.write(to_write+"\n")
    f.close()

# The main loop
if __name__ == "__main__":
    player = agent.IsaacAgent()
    while True:
        user_in = input("Program running...\nControls:\n\tCollect Data (c)\n\tTrain (t)\n\tRun (r)\n")
        if(user_in == "c"):
            train(player)
        if(user_in == "t"):
            inn.train()
        if(user_in == "r"):
            inn.test()
        
        
