import tkinter as tk
from tkinter import ttk

from __main__ import SAOMDT

from .fbi.data_filler import FBIDataFiller


class FBI(tk.Frame):
	def __init__(self, master: SAOMDT):
		super(FBI, self).__init__(master)
		self.tabbedmenu = ttk.Notebook(self)
		self.datafiller = FBIDataFiller(self)

		self.tabbedmenu.add(self.datafiller, text="Fill Data")

		self.tabbedmenu.place(x=10, y=10, relwidth=1, relheight=1, width=-20, height=-20)
