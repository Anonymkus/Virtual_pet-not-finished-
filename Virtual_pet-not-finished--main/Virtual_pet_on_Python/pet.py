class Pet:
    def __init__(
        self,
        name="неизвестно",
        satiety=0,
        health=0,
        mood=0,
        cleanness=0,
        energy=0
    ):
        self.portrait = "tiger_emoji-main/happy.png"
        self.name = name
        self.satiety = satiety
        self.health = health
        self.mood = mood
        self.cleanness = cleanness
        self.energy = energy
        self.satiety_change = -1
        self.health_change = -1
        self.mood_change = -1
        self.cleanness_change = -1
        self.energy_change = -1

    def feed(self, num):
        self.satiety += num
        print(f"{self.name} съел {num} и теперь у него {self.satiety} сытости")

    def change_portrait(self):
        pass

    def decrease_stats(self):
        self.satiety += self.satiety_change
        self.health += self.health_change
        self.mood += self.mood_change
        self.cleanness += self.cleanness_change
        self.energy += self.energy_change