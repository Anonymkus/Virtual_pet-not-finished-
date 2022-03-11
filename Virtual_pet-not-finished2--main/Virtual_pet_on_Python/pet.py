class Pet:
	def __init__(
		self,
		name="неизвестно",
		satiety=0,
		health=0,
		mood=0,
		cleanness=0,
		energy=0,
		dream=0,
		play=0,
		wash=0,
		alive=0
	):
		self.portrait = "tiger_emoji-main/happy.png"
		self.name = name
		self.satiety = satiety
		self.health = health
		self.mood = mood
		self.cleanness = cleanness
		self.energy = energy
		self.dream = dream
		self.play = play
		self.wash = wash
		self.alive = alive
		self.satiety_change = 1
		self.health_change = 10
		self.mood_change = 20
		self.cleanness_change = 1
		self.energy_change = 1

	def feed_pet(self, num):
		if self.satiety < 100:
			self.satiety += num
			self.energy += 5
			self.cleanness -= 5
			self.mood += 2.5
			self.health += 0.5
			print(f"{self.name} съел {num} и теперь у него {self.satiety} сытости")
		else:
			print(f"{self.name} ещё не проголодался, не нужно его кормить!")


	def play_game(self, num):
		if self.energy > 25:
			self.energy -= num
			self.satiety -= 10
			self.cleanness -= 5
			self.mood += 5
			self.health += 2.5
			print(f"{self.name} поиграл и теперь у него {self.energy} энергии")
		else:
			print(f"{self.name} устал, не нужно его тревожить!")


	def take_a_bath(self, num):
		if self.cleanness < 75:
			self.cleanness += num
			self.mood += 5
			self.health += 2.5
			print(f"{self.name} принял ванну и теперь у него {self.cleanness} чистоты")
		else:
			print(f"{self.name} ещё не испачкался, не нужно его кормить!")


	def have_a_rest(self, num):
		if self.energy < 25:
			self.energy += num
			input(f"{self.name} отдыхает")
			print(f"{self.name} отдохнул и теперь у него {self.energy} энергии")
		else:
			print(f"{self.name} ещё не испачкался, не нужно его кормить!")


	def change_portrait(self):
		pass

	def decrease_stats(self):
		if self.health > 0:
			self.satiety -= 0.5
			self.energy -= 1.5
			self.cleanness -= 0.5
			if self.dream == 1:
				self.satiety -= 0.03
				self.energy += 2
				self.cleanness -= 0.03
				self.mood += 0.05
				self.health += 0.04
			if self.satiety in range(80,91):

		else:
			result = 0
			return result
			