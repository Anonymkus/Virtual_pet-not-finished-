import random


class Pet:
	def __init__(
		self,
		name="неизвестно",
		satiety=0,
		health=0,
		mood=0,
		cleanness=0,
		energy=0,
		play=0,
		wash=0,
		alive=1,
		day=1,
		night=0
	):
		self.portrait = "tiger_emoji-main/happy.png"
		self.name = name
		self.satiety = satiety
		self.health = health
		self.mood = mood
		self.cleanness = cleanness
		self.energy = energy
		self.play = play
		self.wash = wash
		self.alive = alive
		self.day = day
		self.night = night
		self.satiety_change = 1
		self.health_change = 10
		self.mood_change = 20
		self.cleanness_change = 1
		self.energy_change = 1

	def feed_pet(self, num):
		if self.satiety < (100 - num):
			self.satiety += num
			self.energy += 5
			self.cleanness -= 5
			if self.mood < 95 and self.health < 99:
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
			print(f"{self.name} ещё не устал, не нужно его заставлять спать!")


	def change_portrait(self):
		pass


	def change_health_and_mood(self):
		pass


	def change_stats(self):
		if self.alive == 1:
			if self.day == 1:
				self.satiety -= 0.5
				self.energy -= 0.5
				self.cleanness -= 0.5
			if self.night == 1:
				self.satiety -= 0.03
				self.energy += 2
				self.cleanness -= 0.03
				self.mood += 0.05
				self.health += 0.04
