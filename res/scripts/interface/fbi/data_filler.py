import os
import tkinter as tk
from tkinter import ttk


class FBIDataFiller(tk.Frame):
	def __init__(self, master):
		super(FBIDataFiller, self).__init__(master)
		self.schemaLabel = ttk.Label(self, text="Schema: ")
		self.schemaVar = tk.StringVar()
		schemas = get_schemas()
		self.schemaCombobox = ttk.Combobox(
			self,
			textvariable=self.schemaVar,
			values=schemas,
			width=len(max(schemas, key=len))
		)
		self.__place()

	def __place(self):
		x, y = 10, 10
		self.schemaLabel.place(x=x, y=y)
		self.schemaLabel.update()
		x += self.schemaLabel.winfo_width()
		self.schemaCombobox.place(x=x + 5, y=y)


def get_schemas() -> list[str]:
	res = []
	folder = "res/schemas"
	nb_subfolders = 0
	for root, subdirs, files in os.walk(folder):
		if len(files) == 0:
			continue
		arr = [os.path.join(root[len(folder):], file[:-7]).replace('\\', '/') for file in files]
		res.extend(arr)
		nb_subfolders += 1
	# put direct files after folders
	if nb_subfolders > 1:
		while '/' not in res[0]:
			res.append(res.pop(0))
	return res
