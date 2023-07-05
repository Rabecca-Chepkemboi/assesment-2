class Artist:
    def __init__(self, name, country, music_type, instruments):
        self.name = name
        self.country = country
        self.music_type = music_type
        self.instruments = instruments
    def artist_detail(self):
        print(f"name: {self.name}, country: {self.country}, musicType: {self.music_type}, instruments: {', '.join(self.instruments)}")
class Performance(Artist):
    def __init__(self, name, country, music_type, instruments, stage_time):
        super().__init__(name, country, music_type, instruments)
        self.stage_time = stage_time
    def scheduling(self):
        print(f"name: {self.name}, musicType: {self.music_type}, time: {self.stage_time}")
    def play_instrument(self, instrument):
        if instrument in self.instruments:
            print(f"{self.name} is playing {instrument}")
        else:
            print(f"{self.name} is not playing {instrument}")
class Stage(Artist):
    def __init__(self, name, country, music_type, instruments, capacity, location):
        super().__init__(name, country, music_type, instruments)
        self.capacity = capacity
        self.location = location
    def performance(self):
        print(f"name: {self.name}, country: {self.country}, musicType: {self.music_type}, capacity: {self.capacity}, place: {self.location}")
artist = Artist("jayz", "Canada", "hiphop", ["guitar", "piano"])
artist.artist_detail()
perform = Performance("sautisol", "Kenya", "bongo", ["guitar", "piano"], "2 hours")
perform.scheduling()
stage = Stage("Bridget blue", "Kenya", "gospel", ["piano", "harp", "violin"], 100, "Nakuru")
stage.performance()





















