class Music:
    # constructor
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        
    #method to show song info
    def show_info(self):
        print(f'{self.title} by {self.artist}')
        
        #method to play the song
    def play_song(self):
        print(f'Playing {self.title}')
        
    #create my Playlist of favorite songs
    #i wanna be yours by artic monkeys
    # nights like this by the kid laroi
playlist = [Music("I wanna be yours", "Artic monkeys"), Music("Nights like this", "The kid Laroi")]