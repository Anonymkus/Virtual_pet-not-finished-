"""
	переменные:
		pet_alive
		pet_sleep
		pet_wash
		pet_play
 	день:
 		1 день 1 млн тиков

 	ночь:
 		1 ночь 750 тыс тиков

	satiety - сытость:
		от 0 до 100
		при кормлении += 10
		при сне -= 0.5
		когда бодрствует -= 2
		при игре -= 5
		кормление зависит от здоровья и возможно от настроения
		ВОЗМОЖНО! пищевое отравление
	cleanness - чистота:
		от 0 до 100
		при сне -?
		при бодровстве -= 5
		при кормлении -= 10
		при мытье += 10
		при игре -= 10
		частое мытье понижает здоровье
	energy - энергия:
		от 0 до 100
		при сне += 10
		когда бодрствует -= 5
		когда ест += 2.5
		при игре -= -10
	health - здоровье:
		от 0 до 100
		при сне += 2
		при отсутствии мытья -= 4.5
		при энергозатротности -= 0.5
		при голодании -= 5
		здоровье зависит от сытости, чистоты, энергии
	mood - настроение:
		от 0 до 100
		при сне += 2
		после еды += 2.5
		после мытья += 2.5
		зависит от здоровья
		если здоровье > 50, то 
			mood -= 5
		если здоровье < 50, то
			mood -= 15
	portrait - портрет:
		mood = 100 до 75, то =)
		mood = 75 до 60, то =|
		mood = 45 до 30, то =/
		mood = 30 до 15, то =(
		mood = 15 до 0, то X(
		изменение портрета когда ест
		изменение портрета когда моется
		изменение портрета когда спит
"""

import tkinter as tk
import time
from pet import Pet


class App(tk.Tk):
	def __init__(self):
		super().__init__()
		self.pet = Pet(
			name=input("What is pet name? ").capitalize(),
			satiety=100,
			health=100,
			mood=100,  
			cleanness=100,
			energy=100
			)
		self.geometry("512x512")
		self.name_lbl = tk.Label(self, text=self.pet.name)
		self.name_lbl.pack()
		self.satiety_lbl = tk.Label(self)
		self.satiety_lbl.pack()
		self.health_lbl = tk.Label(self)
		self.health_lbl.pack()
		self.mood_lbl = tk.Label(self)
		self.mood_lbl.pack()
		self.cleanness_lbl = tk.Label(self)
		self.cleanness_lbl.pack()
		self.energy_lbl = tk.Label(self)
		self.energy_lbl.pack()

		self.canvas = tk.Canvas(self, width=256, height=256)
		self.canvas.pack()
		self.img = tk.PhotoImage(file=self.pet.portrait)
		self.img = self.img.subsample(2)
		self.canvas.create_image(128, 128, image=self.img, anchor=tk.CENTER)

		self.feed_btn = tk.Button(self, text="Feed your pet", command = lambda: self.pet.feed_pet(10)) #self.pet.satiety_change
		self.feed_btn.pack()
		self.play_btn = tk.Button(self, text="Play with your pet", command = lambda: self.pet.play_game(20)) #self.pet.energy_change
		self.play_btn.pack()
		self.wash_btn = tk.Button(self, text="Wash your pet", command = lambda: self.pet.take_a_bath(10)) #self.pet.cleanness_change
		self.wash_btn.pack()
		self.rest_btn = tk.Button(self, text="Let rest your pet", command = lambda: self.pet.have_a_rest(50)) #self.pet.cleanness_change
		self.rest_btn.pack()


	def update_tick(self):
		self.pet.change_stats()
		self.after(1000, self.update_tick)


	def change_day_and_night(self):
		self.pet.day = 1
		self.pet.night = 0
		print(f"{self.pet.day} день")
		self.after(1000000)
		self.pet.night = 1
		self.pet.day = 0
		print(f"{self.pet.night} ночь")
		self.after(750000, self.change_day_and_night)


	def update_stats(self):
		self.satiety_lbl.config(text=f"Satiety: {self.pet.satiety}")
		self.cleanness_lbl.config(text=f"Cleanness: {self.pet.cleanness}")
		self.energy_lbl.config(text=f"Energy: {self.pet.energy}")
		self.health_lbl.config(text=f"Health: {self.pet.health}")
		self.mood_lbl.config(text=f"Mood: {self.pet.mood}")
		self.after(100, self.update_stats)



# while self.pet.alive:
if __name__ == '__main__':
	window = App()
	window.update_tick()
	# window.change_day_and_night()
	window.update_stats()
	window.mainloop()
	


# print("Game over")
