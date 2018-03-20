# Here is the basic genetic information

class Song:

    # Contains all of the data beats from a

    # A shapshot of the run
    player_location = None
    enemy_locations = None

    # 0 = UP, 1 = RIGHT, 2 = DOWN, 3 = LEFT, -1 = None
    shot_direction = None
    movement_direction = None

    def __init__(self):
        # A tuple
        self.player_location = (0, 0)

        # A list of tuples containing enemy locations, one for each enemy
        # May change this later depending on if I set a static number of enemies
        self.enemy_locations = [(0, 0)]

        self.shot_direction = -1
        self.movement_direction = -1

    # Populate the gene with gathered data
    def populate(self, player_location, enemy_locations, shot_direction, movement_direction):
        self.player_location = player_location
        self.enemy_locations = enemy_locations
        self.shot_direction = shot_direction
        self.movement_direction = movement_direction

    # Get the correct notes from the song
    def get_notes(self):
        pass

    # For debug purposes
    def print_song(self):
        print("Player Location: {}\nEnemy Locations: {}\nShot Direction: {}\nMovement Direction: {}".format(self.player_location, self.enemy_locations, self.shot_direction, self.movement_direction))


class Album:
    # This class contains all the data for a given run,
    # A new one will be created each time the game starts a new run
    # These will be bred together to get better runs, hopefully

    # All the songs for a given run
    # Will need to calculate the fitness for a song as well.
    songs = None
    fitness_score = 0

    # A list of frames
    def __init__(self):
        self.songs = []
        self.fitness_score = 0
    
    # Append a new frame to the gene
    def add_song(self, song):
        self.songs.append(song)

    # Returr songs
    def get_songs(self):
        return self.songs

    # Add the given amount to the fitness of the albumt
    def add_to_fitness(self):
        to_add = 50 # base increase score.
        for song in self.songs:
            song.get_notes()
            
    # Print a gene for debugging purposes
    def print_album(self):
        for x in range(len(self.songs)):
            print("Song: {}".format(self.songs[x]))