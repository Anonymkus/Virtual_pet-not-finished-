"""
	Рисунок питомца
	способности питомца
	показатели питомца
	время
"""

import tkinter as tk
import time
from pet import Pet


class App(tk.Tk):
	def __init__(self):
		super().__init__()
		self.pet = Pet(
			name="",
			satiety=100,
			health=100,
			mood=100,  
			cleanness=100,
			energy=100
		)
		self.geometry("512x512")
		self.name_lbl = tk.Label(self, text=f"Name: {self.pet.name}")
		self.name_lbl.pack()
		self.satiety_lbl = tk.Label(self)
		self.satiety_lbl.pack()
		self.health_lbl = tk.Label(self, text=f"Health: {self.pet.health}")
		self.health_lbl.pack()
		self.mood_lbl = tk.Label(self, text=f"Mood: {self.pet.mood}")
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

		self.feed_btn = tk.Button(self, text="Feed your pet")
		self.feed_btn.pack()

	def update_tick(self):
		self.pet.decrease_stats()
		self.satiety_lbl.config(text=f"Satiety: {self.pet.satiety}")
		self.cleanness_lbl.config(text=f"Cleanness: {self.pet.cleanness}")
		self.energy_lbl.config(text=f"Energy: {self.pet.energy}")
		self.after(10000, self.update_tick)

if __name__ == '__main__':
	window = App()
	window.update_tick()
	window.mainloop()
