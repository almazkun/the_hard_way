class Song():
    def __init__(self, lyrics):
        self.lyrics = lyrics


    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
    

happy_bday = Song(["Happy bithday to you",
                    "Happy birthday to you!",
                    "Dear you happy birthday!"
                    ])


bulls_on_parade = Song(["Bulls are comming!",
                        "They are all are almost here!",
                        "Beware!"
                        ])


happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


generic_song = ["Bla bla blaaa", "Blaaa bla blaa", "bla blaaa Blaa"]
bla = Song(generic_song)

bla.sing_me_a_song()