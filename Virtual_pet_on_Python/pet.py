class Pet:
	def __init__(
		self, 
		name="", 
		health=0, 
		satiety=0, 
		mood=0, 
		cleanness=0, 
		energy=0,
		
	):
		self.name = name
		self.health = health
		self.satiety = satiety
		self.mood = mood
		self.cleanness = cleanness
		self.energy = energy
		self.health_change = -1
		self.satiety_change = -1
		self.mood_change = -1
		self.cleanness_change = -1
		self.energy_change = -1


	def feed_pet(self, num):
		self.satiety += num
		print(f"{self.name} съел {num}, здоровье стало равно {self.satiety}")

