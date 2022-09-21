import tkinter as tk
from tkinter import filedialog, Text
import os
import customtkinter as ctk


root = tk.Tk() # [Main Window]
root.title("Multi App loader")
apps = []
btnWidth = 200
frameCol= "#111"
bgCol = "#444"

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def addApp():
    
    for widget in frame.winfo_children():
        widget.destroy()
    
    filename = filedialog.askopenfilename(initialdir='/', title="Select a file",
                                          filetypes=(("executables", "*.exe"), ("all files", "*./")))
    print(filename)
    apps.append(filename)
    for app in apps:
        label = tk.Label(frame, text=app)
        label.pack()
    return filename


def loadApps():
    for app in apps:
        os.startfile(app)  

root.config(bg=bgCol, height=720)
canvas = tk.Canvas(root, height=710, width=700, bg=bgCol)
canvas.pack()
frame = ctk.CTkFrame(root, bg_color=bgCol, fg_color=frameCol, corner_radius=50)
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)
btnSection = ctk.CTkFrame(root, height=60, width=500, fg_color=bgCol)
btnSection.pack()
# [Buttons]
uploadFile = ctk.CTkButton(master=btnSection, text="Upload a File", corner_radius=10, fg_color="#608",
                           hover_color="#20f", width=btnWidth, height=60, command=addApp, text_font=("sans-serif", 12))
uploadFile.grid(column=0, row=0)
gap = tk.Label(btnSection, text="", width=5, bg=bgCol).grid(column=5, row=0)
openFile = ctk.CTkButton(master=btnSection, text="Load Files", corner_radius=10, fg_color="#608",
                         hover_color="#20f", width=btnWidth, height=60, command=loadApps, text_font=("sans-serif", 12))
openFile.grid(column=10, row=0)
for app in apps:
    label = ctk.CTkLabel(frame, text=app, fg_color="#fff", text_color=frameCol, pady=20, corner_radius=20)
    label.pack()

root.mainloop()

with open("save.txt", "w") as f:
    for app in apps:
        f.write(app + ',')