# Here is the basic genetic information

class Frame:
    # A shapshot of the run
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

    def populate(self, player_location, enemy_locations, times_taken_damage, times_dealt_damage):
        # Populate the gene with gathered data
        self.player_location = player_location
        self.enemy_locations = enemy_locations
        self.times_taken_damage = times_taken_damage
        self.times_dealt_damage = times_dealt_damage


class Gene:
    # All the frames for a given run
    # Will need to calculate the fitness for a gene as well.

    def __init__(self):
        # A list of frames
        self.frames = []
    
    def add_frame(frame):
        # Append a new frame to the gene
        self.frames.append(gene)


class Genome:
    # A set of genes.
    pass
    