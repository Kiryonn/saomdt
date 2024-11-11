import json
import os
import tkinter as tk
from tkinter import ttk

from res.scripts.utils import Singleton, Signal


class Settings(metaclass=Singleton):
	SETTINGS_PATH = "res/settings/setttings.json"
	def __init__(self, master):
		self.master = master
		# signals
		self.on_theme_changed = Signal[str]()

		# variables
		self.__themeVar = tk.StringVar()
		self.__toplevel: tk.Toplevel = None

		# add events
		self.__themeVar.trace_add("write", self.__on_theme_changed)

		# load data from saves
		self.load()

	def load(self):
		with open(self.SETTINGS_PATH, 'r', encoding='utf-8') as file:
			settings = json.load(file)
		self.__themeVar.set(settings['theme'])

	def save(self):
		data = {
			"theme": self.__themeVar.get()
		}
		if not os.path.exists(self.SETTINGS_PATH):
			os.makedirs(self.SETTINGS_PATH, exist_ok=True)
		with open(self.SETTINGS_PATH, 'w', encoding='utf-8') as file:
			json.dump(data, file)

	def __on_theme_changed(self, *_):
		style = ttk.Style()
		new_theme = self.__themeVar.get()
		if new_theme == style.theme_use():
			return
		style.theme_use(new_theme)
		self.save()
		self.on_theme_changed.emit(new_theme)

	def open(self):
		if self.__toplevel != None:
			return
		styles = ttk.Style()
		self.__toplevel = tk.Toplevel(self.master)
		self.__toplevel.title("Settings")
		self.__toplevel.minsize(250, 50)
		self.__toplevel.geometry("250x50")
		self.__toplevel.themeLabel = ttk.Label(self.__toplevel, text="Theme")
		self.__toplevel.themeChoser = ttk.Combobox(
			self.__toplevel,
			textvariable=self.__themeVar,
			values=styles.theme_names(),
			width=len(max(styles.theme_names(), key=len))
		)
		x, y = 10, 10
		self.__toplevel.themeLabel.place(x=x, y=y)
		self.__toplevel.themeLabel.update()
		x += self.__toplevel.themeLabel.winfo_width()
		self.__toplevel.themeChoser.place(x=x + 5, y=y)

	def close(self):
		self.__toplevel.destroy()
		self.__toplevel = None
