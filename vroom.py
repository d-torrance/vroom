import tkinter as tk
import os
import pydub
import pydub.playback

class VroomVroom(tk.Frame):
    sounds = {
        "Start"    : "start",
        "Start 2"  : "start2",
        "Rev"      : "rev",
        "No start" : "no-start",
        "Move"     : "move",
        "Dukes"    : "dukes",
        "Brake"    : "brake",
        "Screech"  : "screech",
        "Skid"     : "skid",
        "Crash"    : "crash"
        }

    def __init__(self, root):
        super().__init__(root)
        self.winfo_toplevel().title("Vroom Vroom")
        for sound in VroomVroom.sounds:
            button = VroomButton(self, sound)
            button.pack(side=tk.LEFT)


class VroomButton(tk.Button):
    def __init__(self, root, sound):
        super().__init__(root,
                         text=sound,
                         command=self.make_sound)
        self.sound = sound
        
    def make_sound(self):
        pydub.playback.play(pydub.AudioSegment.from_file(
            f"{os.path.curdir}/audio/{VroomVroom.sounds[self.sound]}.mp3"))


root = tk.Tk()
vroom = VroomVroom(root)
vroom.pack()
root.mainloop()

