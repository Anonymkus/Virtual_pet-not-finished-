"""
	Рисунок питомца
	способности питомца
	показатели питомца
	время
"""

import tkinter as tk
from pet import Pet


class App(tk.Tk):
	def __init__(self):
		super().__init__()
		self.canvas = tk.Canvas(self, height=512, width=512)
		self.img = tk.PhotoImage(file = 'tiger_emoji-main/happy.png') 
		self.canvas.create_image(20, 20, anchor='nw',image=self.img)
		self.canvas.grid(row=2,column=1)


if __name__ == '__main__':
	window = App()
	window.title("Virtual Pet")
	window.geometry("1080x1080")
	tk.Label(window, text="Введите имя питомца: ")
	pet_name = tk.Entry(window)
	pet = Pet(
		name=pet_name,
		health=100,
		satiety=100,
		mood=100,
		cleanness=100,
		energy=100,
	)

	window.mainloop()
