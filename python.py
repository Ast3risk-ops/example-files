from guizero import App, Text, PushButton
from sys import exit
from os import system
print("Hello world!")
def e():
    print("Goodbye...")
    app.destroy()
    system('clear')
    exit(["ERR_SUCCESS"])

app = App(title="This is a test app")
texta = Text(app, text="This file works!")
textb = Text(app, text="How about you try the video file?", font="Comic Sans MS")
textc = Text(app, text="Or look in the folder?", font="Impact")
button_boi = PushButton(app, command=e, text="Push Me!")
app.display()
