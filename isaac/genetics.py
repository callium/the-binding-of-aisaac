# Here is the basic genetic information

class Gene:
    # A shapshot of the run
    def __init__(self):
        # A tuple
        self.player_location = (0, 0)

        # A list of tuples
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


class Genome:
    # All the genes for a given run
    def __init__(self):
        # A list of genes
        self.genes = []
    
    def add_gene(gene):
        # Append a new gene to the genome
        self.genes.append(gene)
    