class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
"I don't want to get sued",
"So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
"With pockets full of shells"])

jingle_bells = ["Jingle bells", "Jingle bells", "Jingle all the way"]

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

Song(jingle_bells).sing_me_a_song()

print("-" * 10)

back_in_black = ["Back in black"]

Song(back_in_black).sing_me_a_song()


Song(back_in_black.append("/n I hit the sack")).sing_me_a_song()
