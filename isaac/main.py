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
        # In the true program, the random here will be supplied by Tensorflow
        player.unpause()
        server.receive()
        # data = server.receive()
        # interpret_data(data)

        r = random.randint(0,4)
        player.move(r)

def test(player):
    while True:
        player.unpause()
        server.receive()

def interpret_data(data):
    print(data)

# The main loop
if __name__ == "__main__":
    print("Started")

    player = agent.IsaacAgent()
    # Randomly test the deliberate movement mechanics
    # random_test(player)
    test(player)
