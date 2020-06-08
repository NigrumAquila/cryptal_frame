from tkinter import filedialog, Tk

root = Tk()
root.attributes("-topmost", True)
root.withdraw()

pickFile = lambda title='Открытие': filedialog.askopenfilename(title=title)