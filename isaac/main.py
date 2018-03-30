import genetics_data_structures as gen
import isaac_agent as agent
import tensorflow as tf

class IsaacNN:
    def __init__(self, filename="isaac.tflearn"):
        self.filename = filename


# The main loop
if __name__ == "__main__":
    print("Started")
    while True:
        # album = gen.Album()
        player = agent.IsaacAgent()
        # agent.random_sequence()

