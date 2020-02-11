class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)



kgatlw = ["Nonagon infinity opens the door", "Nonagon infinity opens the door", "Wait for the answer to open the door"]

# the_song = Song(kgatlw)
#
# the_song.sing_me_a_song()

Song.sing_me_a_song(Song(kgatlw))
