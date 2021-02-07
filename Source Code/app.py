#[1]

import tkinter as tk
from tkinter import filedialog, Text
import os

#[2]

root = tk.Tk()
root.title("GUI-App")
apps = []

#[3]

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApp = f.read()
        tempApp = tempApp.split(',')
        apps = [x for x in tempApp if x.strip()]
        print(apps)

        
#[4]

def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(
        initialdir="/", title="Select file", filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(apps)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

#[5]

def runApps():
    for app in apps:
        os.startfile(app)

#[6]

canvas = tk.Canvas(root, height=500, width=500, bg="#263D42")
canvas.pack()

#[7]

frame = tk.Frame(root, bg="white")
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

#[8]

openFile = tk.Button(root, text="Open File", padx=25,
                     pady=10, fg='white', bg="#263D42", command=addApp)
openFile.pack()


#[9]

runApps = tk.Button(root, text="Run Apps", padx=25,
                    pady=10, fg='white', bg="#263D42", command=runApps)
runApps.pack()

#[10]

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()


root.mainloop()

#[11]

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
