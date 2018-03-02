# Here is the basic genetic information

class Frame:
    # A shapshot of the run
    player_location = None
    enemy_locations = None
    times_taken_damage = None
    times_dealt_damage = None

    def __init__(self):
        # A tuple
        self.player_location = (0, 0)

        # A list of tuples containing enemy locations, one for each enemy
        # May change this later depending on if I set a static number of enemies
        self.enemy_locations = [(0, 0)]

        # Integer
        self.times_taken_damage = 0

        # Integer
        self.times_dealt_damage = 0

    # Populate the gene with gathered data
    def populate(self, player_location, enemy_locations, times_taken_damage, times_dealt_damage):
        self.player_location = player_location
        self.enemy_locations = enemy_locations
        self.times_taken_damage = times_taken_damage
        self.times_dealt_damage = times_dealt_damage

    # For debug purposes
    def print_frame(self):
        print("Player Location: {}\nEnemy Locations: {}\nTimes Taken Damage: {}\nTimes Dealt Damage: {}".format(self.player_location, self.enemy_locations, self.times_taken_damage, self.times_dealt_damage))


class Gene:
    # All the frames for a given run
    # Will need to calculate the fitness for a gene as well.
    frames = None

    # A list of frames
    def __init__(self):
        self.frames = []
    
    # Append a new frame to the gene
    def add_frame(self, frame):
        self.frames.append(frame)

    # Print a gene for debugging purposes
    def print_gene(self):
        for x in range(len(self.frames)):
            print("Frame: {}".format(self.frames[x]))


class Genome:
    # A set of genes.
    pass
    