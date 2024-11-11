import tkinter as tk
from tkinter import ttk

from .settings import Settings
from res.scripts.utils import Singleton


class SAOMDT(tk.Tk, metaclass=Singleton):
	def __init__(self):
		super(SAOMDT, self).__init__()
		self.title("SAO:MD Tools")
		self.minsize(600, 400)
		self.settings = Settings(self)
		self.current_scene: tk.Widget | None = None
		self.settings_button = ttk.Button(self, text='⚙️', command=self.open_settings, width=3)
		self.settings_button.place(relx=1, y=5, x=-10, anchor='ne')

		from .flatbuffers_interface import FBI
		self.change_scene(FBI)

	def change_scene(self, scene, *args, **kws):
		loaded_scene = scene(self, *args, **kws)
		if self.current_scene is not None:
			self.current_scene.forget()
		self.current_scene = loaded_scene
		self.current_scene.place(x=0, y=0, relwidth=1, relheight=1)
		self.settings_button.lift()

	def open_settings(self):
		self.settings.open()
