import tkinter as tk
from tkinter import filedialog
import pygame
import os

# =====================================================
# AUDIO SETUP
# =====================================================

pygame.mixer.init()

deck1_channel = pygame.mixer.Channel(0)
deck2_channel = pygame.mixer.Channel(1)

sound1 = None
sound2 = None

playing1 = False
playing2 = False

volume1 = 1.0
volume2 = 1.0

crossfader_value = 0.5


# =====================================================
# MAIN WINDOW
# =====================================================

root = tk.Tk()
root.title("Python DJ Console V2")
root.geometry("1200x720")
root.configure(bg="#111111")
root.resizable(False, False)


# =====================================================
# CROSSFADE AUDIO
# =====================================================

def update_audio():

    left_factor = 1.0 - crossfader_value
    right_factor = crossfader_value

    deck1_channel.set_volume(volume1 * left_factor)
    deck2_channel.set_volume(volume2 * right_factor)


# =====================================================
# LOAD SONG
# =====================================================

def load_song(deck):

    global sound1, sound2

    file = filedialog.askopenfilename(
        title="Select Audio File",
        filetypes=[
            ("Audio Files", "*.mp3 *.wav *.ogg"),
            ("MP3", "*.mp3"),
            ("WAV", "*.wav"),
            ("OGG", "*.ogg")
        ]
    )

    if not file:
        return

    try:

        sound = pygame.mixer.Sound(file)

        if deck == 1:

            deck1_channel.stop()

            sound1 = sound

            song1_label.config(
                text=os.path.basename(file)
            )

            status1.config(
                text="LOADED"
            )

        else:

            deck2_channel.stop()

            sound2 = sound

            song2_label.config(
                text=os.path.basename(file)
            )

            status2.config(
                text="LOADED"
            )

    except Exception as e:

        print("Error:", e)


# =====================================================
# PLAY / PAUSE DECK 1
# =====================================================

def play_pause_1():

    global playing1

    if sound1 is None:
        return

    if playing1:

        deck1_channel.pause()

        playing1 = False

        play1_button.config(
            text="▶"
        )

        status1.config(
            text="PAUSED"
        )

    else:

        deck1_channel.unpause()

        if not deck1_channel.get_busy():

            deck1_channel.play(sound1)

        playing1 = True

        play1_button.config(
            text="Ⅱ"
        )

        status1.config(
            text="PLAYING"
        )


# =====================================================
# PLAY / PAUSE DECK 2
# =====================================================

def play_pause_2():

    global playing2

    if sound2 is None:
        return

    if playing2:

        deck2_channel.pause()

        playing2 = False

        play2_button.config(
            text="▶"
        )

        status2.config(
            text="PAUSED"
        )

    else:

        deck2_channel.unpause()

        if not deck2_channel.get_busy():

            deck2_channel.play(sound2)

        playing2 = True

        play2_button.config(
            text="Ⅱ"
        )

        status2.config(
            text="PLAYING"
        )


# =====================================================
# STOP
# =====================================================

def stop_1():

    global playing1

    deck1_channel.stop()

    playing1 = False

    play1_button.config(text="▶")

    status1.config(text="STOPPED")


def stop_2():

    global playing2

    deck2_channel.stop()

    playing2 = False

    play2_button.config(text="▶")

    status2.config(text="STOPPED")


# =====================================================
# CUE
# =====================================================

def cue_1():

    global playing1

    if sound1 is None:
        return

    deck1_channel.stop()
    deck1_channel.play(sound1)

    playing1 = True

    play1_button.config(text="Ⅱ")

    status1.config(text="CUE PLAY")


def cue_2():

    global playing2

    if sound2 is None:
        return

    deck2_channel.stop()
    deck2_channel.play(sound2)

    playing2 = True

    play2_button.config(text="Ⅱ")

    status2.config(text="CUE PLAY")


# =====================================================
# VOLUME
# =====================================================

def change_volume_1(value):

    global volume1

    volume1 = float(value)

    update_audio()


def change_volume_2(value):

    global volume2

    volume2 = float(value)

    update_audio()


# =====================================================
# CROSSFADER
# =====================================================

def change_crossfader(value):

    global crossfader_value

    crossfader_value = float(value)

    update_audio()


# =====================================================
# JOG WHEEL
# =====================================================

def jog_left(event=None):

    jog1_label.config(
        text="↶"
    )


def jog_right(event=None):

    jog1_label.config(
        text="↷"
    )


def jog2_left(event=None):

    jog2_label.config(
        text="↶"
    )


def jog2_right(event=None):

    jog2_label.config(
        text="↷"
    )


# =====================================================
# DECK CREATION
# =====================================================

def create_deck(parent, number):

    frame = tk.Frame(
        parent,
        bg="#1c1c1c",
        width=360,
        height=620,
        highlightbackground="#333333",
        highlightthickness=2
    )

    frame.pack(
        side="left",
        padx=8,
        pady=5
    )

    frame.pack_propagate(False)

    # -------------------------
    # DECK TITLE
    # -------------------------

    tk.Label(
        frame,
        text=f"DECK {number}",
        bg="#1c1c1c",
        fg="white",
        font=("Arial", 18, "bold")
    ).pack(pady=8)

    # -------------------------
    # JOG WHEEL
    # -------------------------

    canvas = tk.Canvas(
        frame,
        width=260,
        height=260,
        bg="#1c1c1c",
        highlightthickness=0
    )

    canvas.pack()

    # Outer wheel

    canvas.create_oval(
        8, 8,
        252, 252,
        fill="#090909",
        outline="#444444",
        width=8
    )

    # Ring

    canvas.create_oval(
        30, 30,
        230, 230,
        fill="#151515",
        outline="#555555",
        width=3
    )

    # Inner ring

    canvas.create_oval(
        70, 70,
        190, 190,
        fill="#222222",
        outline="#666666",
        width=3
    )

    # Center

    canvas.create_oval(
        105, 105,
        155, 155,
        fill="#111111",
        outline="#777777",
        width=2
    )

    # Wheel markings

    for i in range(0, 360, 15):

        import math

        angle = math.radians(i)

        x1 = 130 + 94 * math.cos(angle)
        y1 = 130 + 94 * math.sin(angle)

        x2 = 130 + 102 * math.cos(angle)
        y2 = 130 + 102 * math.sin(angle)

        canvas.create_line(
            x1, y1,
            x2, y2,
            fill="#777777"
        )

    # -------------------------
    # JOG STATUS
    # -------------------------

    global jog1_label, jog2_label

    if number == 1:

        jog1_label = tk.Label(
            frame,
            text="JOG",
            bg="#1c1c1c",
            fg="#aaaaaa",
            font=("Arial", 10)
        )

        jog1_label.pack()

    else:

        jog2_label = tk.Label(
            frame,
            text="JOG",
            bg="#1c1c1c",
            fg="#aaaaaa",
            font=("Arial", 10)
        )

        jog2_label.pack()

    # -------------------------
    # SONG NAME
    # -------------------------

    global song1_label, song2_label

    if number == 1:

        song1_label = tk.Label(
            frame,
            text="No Song Loaded",
            bg="#1c1c1c",
            fg="#bbbbbb",
            font=("Arial", 9),
            width=35
        )

        song1_label.pack(pady=3)

    else:

        song2_label = tk.Label(
            frame,
            text="No Song Loaded",
            bg="#1c1c1c",
            fg="#bbbbbb",
            font=("Arial", 9),
            width=35
        )

        song2_label.pack(pady=3)

    # -------------------------
    # LOAD BUTTON
    # -------------------------

    tk.Button(
        frame,
        text="LOAD SONG",
        command=lambda: load_song(number),
        bg="#292929",
        fg="white",
        activebackground="#444444",
        activeforeground="white",
        font=("Arial", 10, "bold"),
        width=15
    ).pack(pady=5)

    # -------------------------
    # CUE / PLAY / STOP
    # -------------------------

    controls = tk.Frame(
        frame,
        bg="#1c1c1c"
    )

    controls.pack(pady=5)

    tk.Button(
        controls,
        text="CUE",
        command=cue_1 if number == 1 else cue_2,
        bg="#252525",
        fg="white",
        font=("Arial", 9, "bold"),
        width=7,
        height=2
    ).pack(side="left", padx=4)

    global play1_button, play2_button

    if number == 1:

        play1_button = tk.Button(
            controls,
            text="▶",
            command=play_pause_1,
            bg="#164d24",
            fg="white",
            font=("Arial", 15, "bold"),
            width=7,
            height=2
        )

        play1_button.pack(
            side="left",
            padx=4
        )

    else:

        play2_button = tk.Button(
            controls,
            text="▶",
            command=play_pause_2,
            bg="#164d24",
            fg="white",
            font=("Arial", 15, "bold"),
            width=7,
            height=2
        )

        play2_button.pack(
            side="left",
            padx=4
        )

    tk.Button(
        controls,
        text="■",
        command=stop_1 if number == 1 else stop_2,
        bg="#252525",
        fg="white",
        font=("Arial", 10, "bold"),
        width=7,
        height=2
    ).pack(side="left", padx=4)

    # -------------------------
    # STATUS
    # -------------------------

    global status1, status2

    if number == 1:

        status1 = tk.Label(
            frame,
            text="READY",
            bg="#1c1c1c",
            fg="#999999",
            font=("Arial", 8)
        )

        status1.pack()

    else:

        status2 = tk.Label(
            frame,
            text="READY",
            bg="#1c1c1c",
            fg="#999999",
            font=("Arial", 8)
        )

        status2.pack()

    # -------------------------
    # TEMPO
    # -------------------------

    tk.Scale(
        frame,
        from_=20,
        to=-20,
        orient="horizontal",
        label="TEMPO",
        length=180,
        bg="#1c1c1c",
        fg="white",
        highlightthickness=0,
        troughcolor="#333333"
    ).pack(pady=3)


# =====================================================
# MIXER
# =====================================================

def create_mixer(parent):

    mixer = tk.Frame(
        parent,
        bg="#242424",
        width=300,
        height=620,
        highlightbackground="#444444",
        highlightthickness=2
    )

    mixer.pack(
        side="left",
        padx=8,
        pady=5
    )

    mixer.pack_propagate(False)

    tk.Label(
        mixer,
        text="MIXER",
        bg="#242424",
        fg="white",
        font=("Arial", 20, "bold")
    ).pack(pady=12)

    # -------------------------
    # MASTER
    # -------------------------

    tk.Label(
        mixer,
        text="MASTER",
        bg="#242424",
        fg="#aaaaaa",
        font=("Arial", 10, "bold")
    ).pack()

    master = tk.Scale(
        mixer,
        from_=1,
        to=0,
        resolution=0.01,
        orient="vertical",
        length=130,
        bg="#242424",
        fg="white",
        highlightthickness=0
    )

    master.set(1)
    master.pack()

    # -------------------------
    # EQ
    # -------------------------

    tk.Label(
        mixer,
        text="EQUALIZER",
        bg="#242424",
        fg="white",
        font=("Arial", 11, "bold")
    ).pack(pady=8)

    for name in ["HIGH", "MID", "LOW"]:

        tk.Scale(
            mixer,
            from_=10,
            to=-10,
            orient="horizontal",
            length=180,
            label=name,
            bg="#242424",
            fg="white",
            highlightthickness=0
        ).pack()

    # -------------------------
    # CROSSFADER
    # -------------------------

    tk.Label(
        mixer,
        text="CROSSFADER",
        bg="#242424",
        fg="white",
        font=("Arial", 10, "bold")
    ).pack(pady=10)

    tk.Label(
        mixer,
        text="DECK 1        DECK 2",
        bg="#242424",
        fg="#999999"
    ).pack()

    crossfader = tk.Scale(
        mixer,
        from_=0,
        to=1,
        resolution=0.01,
        orient="horizontal",
        length=230,
        bg="#242424",
        fg="white",
        highlightthickness=0,
        troughcolor="#111111",
        command=change_crossfader
    )

    crossfader.set(0.5)

    crossfader.pack()


# =====================================================
# TOP TITLE
# =====================================================

tk.Label(
    root,
    text="PYTHON DJ CONSOLE",
    bg="#111111",
    fg="white",
    font=("Arial", 22, "bold")
).pack(pady=10)


# =====================================================
# MAIN AREA
# =====================================================

main = tk.Frame(
    root,
    bg="#111111"
)

main.pack()


# Create decks

create_deck(main, 1)

create_mixer(main)

create_deck(main, 2)


# =====================================================
# CLOSE
# =====================================================

def close_app():

    pygame.mixer.quit()
    root.destroy()


root.protocol(
    "WM_DELETE_WINDOW",
    close_app
)


# =====================================================
# START
# =====================================================

root.mainloop()
import tkinter as tk
from tkinter import filedialog
import pygame
import os

# =====================================================
# AUDIO SETUP
# =====================================================

pygame.mixer.init()

deck1_channel = pygame.mixer.Channel(0)
deck2_channel = pygame.mixer.Channel(1)

sound1 = None
sound2 = None

playing1 = False
playing2 = False

volume1 = 1.0
volume2 = 1.0

crossfader_value = 0.5


# =====================================================
# MAIN WINDOW
# =====================================================

root = tk.Tk()
root.title("Python DJ Console V2")
root.geometry("1200x720")
root.configure(bg="#111111")
root.resizable(False, False)


# =====================================================
# CROSSFADE AUDIO
# =====================================================

def update_audio():

    left_factor = 1.0 - crossfader_value
    right_factor = crossfader_value

    deck1_channel.set_volume(volume1 * left_factor)
    deck2_channel.set_volume(volume2 * right_factor)


# =====================================================
# LOAD SONG
# =====================================================

def load_song(deck):

    global sound1, sound2

    file = filedialog.askopenfilename(
        title="Select Audio File",
        filetypes=[
            ("Audio Files", "*.mp3 *.wav *.ogg"),
            ("MP3", "*.mp3"),
            ("WAV", "*.wav"),
            ("OGG", "*.ogg")
        ]
    )

    if not file:
        return

    try:

        sound = pygame.mixer.Sound(file)

        if deck == 1:

            deck1_channel.stop()

            sound1 = sound

            song1_label.config(
                text=os.path.basename(file)
            )

            status1.config(
                text="LOADED"
            )

        else:

            deck2_channel.stop()

            sound2 = sound

            song2_label.config(
                text=os.path.basename(file)
            )

            status2.config(
                text="LOADED"
            )

    except Exception as e:

        print("Error:", e)


# =====================================================
# PLAY / PAUSE DECK 1
# =====================================================

def play_pause_1():

    global playing1

    if sound1 is None:
        return

    if playing1:

        deck1_channel.pause()

        playing1 = False

        play1_button.config(
            text="▶"
        )

        status1.config(
            text="PAUSED"
        )

    else:

        deck1_channel.unpause()

        if not deck1_channel.get_busy():

            deck1_channel.play(sound1)

        playing1 = True

        play1_button.config(
            text="Ⅱ"
        )

        status1.config(
            text="PLAYING"
        )


# =====================================================
# PLAY / PAUSE DECK 2
# =====================================================

def play_pause_2():

    global playing2

    if sound2 is None:
        return

    if playing2:

        deck2_channel.pause()

        playing2 = False

        play2_button.config(
            text="▶"
        )

        status2.config(
            text="PAUSED"
        )

    else:

        deck2_channel.unpause()

        if not deck2_channel.get_busy():

            deck2_channel.play(sound2)

        playing2 = True

        play2_button.config(
            text="Ⅱ"
        )

        status2.config(
            text="PLAYING"
        )


# =====================================================
# STOP
# =====================================================

def stop_1():

    global playing1

    deck1_channel.stop()

    playing1 = False

    play1_button.config(text="▶")

    status1.config(text="STOPPED")


def stop_2():

    global playing2

    deck2_channel.stop()

    playing2 = False

    play2_button.config(text="▶")

    status2.config(text="STOPPED")


# =====================================================
# CUE
# =====================================================

def cue_1():

    global playing1

    if sound1 is None:
        return

    deck1_channel.stop()
    deck1_channel.play(sound1)

    playing1 = True

    play1_button.config(text="Ⅱ")

    status1.config(text="CUE PLAY")


def cue_2():

    global playing2

    if sound2 is None:
        return

    deck2_channel.stop()
    deck2_channel.play(sound2)

    playing2 = True

    play2_button.config(text="Ⅱ")

    status2.config(text="CUE PLAY")


# =====================================================
# VOLUME
# =====================================================

def change_volume_1(value):

    global volume1

    volume1 = float(value)

    update_audio()


def change_volume_2(value):

    global volume2

    volume2 = float(value)

    update_audio()


# =====================================================
# CROSSFADER
# =====================================================

def change_crossfader(value):

    global crossfader_value

    crossfader_value = float(value)

    update_audio()


# =====================================================
# JOG WHEEL
# =====================================================

def jog_left(event=None):

    jog1_label.config(
        text="↶"
    )


def jog_right(event=None):

    jog1_label.config(
        text="↷"
    )


def jog2_left(event=None):

    jog2_label.config(
        text="↶"
    )


def jog2_right(event=None):

    jog2_label.config(
        text="↷"
    )


# =====================================================
# DECK CREATION
# =====================================================

def create_deck(parent, number):

    frame = tk.Frame(
        parent,
        bg="#1c1c1c",
        width=360,
        height=620,
        highlightbackground="#333333",
        highlightthickness=2
    )

    frame.pack(
        side="left",
        padx=8,
        pady=5
    )

    frame.pack_propagate(False)

    # -------------------------
    # DECK TITLE
    # -------------------------

    tk.Label(
        frame,
        text=f"DECK {number}",
        bg="#1c1c1c",
        fg="white",
        font=("Arial", 18, "bold")
    ).pack(pady=8)

    # -------------------------
    # JOG WHEEL
    # -------------------------

    canvas = tk.Canvas(
        frame,
        width=260,
        height=260,
        bg="#1c1c1c",
        highlightthickness=0
    )

    canvas.pack()

    # Outer wheel

    canvas.create_oval(
        8, 8,
        252, 252,
        fill="#090909",
        outline="#444444",
        width=8
    )

    # Ring

    canvas.create_oval(
        30, 30,
        230, 230,
        fill="#151515",
        outline="#555555",
        width=3
    )

    # Inner ring

    canvas.create_oval(
        70, 70,
        190, 190,
        fill="#222222",
        outline="#666666",
        width=3
    )

    # Center

    canvas.create_oval(
        105, 105,
        155, 155,
        fill="#111111",
        outline="#777777",
        width=2
    )

    # Wheel markings

    for i in range(0, 360, 15):

        import math

        angle = math.radians(i)

        x1 = 130 + 94 * math.cos(angle)
        y1 = 130 + 94 * math.sin(angle)

        x2 = 130 + 102 * math.cos(angle)
        y2 = 130 + 102 * math.sin(angle)

        canvas.create_line(
            x1, y1,
            x2, y2,
            fill="#777777"
        )

    # -------------------------
    # JOG STATUS
    # -------------------------

    global jog1_label, jog2_label

    if number == 1:

        jog1_label = tk.Label(
            frame,
            text="JOG",
            bg="#1c1c1c",
            fg="#aaaaaa",
            font=("Arial", 10)
        )

        jog1_label.pack()

    else:

        jog2_label = tk.Label(
            frame,
            text="JOG",
            bg="#1c1c1c",
            fg="#aaaaaa",
            font=("Arial", 10)
        )

        jog2_label.pack()

    # -------------------------
    # SONG NAME
    # -------------------------

    global song1_label, song2_label

    if number == 1:

        song1_label = tk.Label(
            frame,
            text="No Song Loaded",
            bg="#1c1c1c",
            fg="#bbbbbb",
            font=("Arial", 9),
            width=35
        )

        song1_label.pack(pady=3)

    else:

        song2_label = tk.Label(
            frame,
            text="No Song Loaded",
            bg="#1c1c1c",
            fg="#bbbbbb",
            font=("Arial", 9),
            width=35
        )

        song2_label.pack(pady=3)

    # -------------------------
    # LOAD BUTTON
    # -------------------------

    tk.Button(
        frame,
        text="LOAD SONG",
        command=lambda: load_song(number),
        bg="#292929",
        fg="white",
        activebackground="#444444",
        activeforeground="white",
        font=("Arial", 10, "bold"),
        width=15
    ).pack(pady=5)

    # -------------------------
    # CUE / PLAY / STOP
    # -------------------------

    controls = tk.Frame(
        frame,
        bg="#1c1c1c"
    )

    controls.pack(pady=5)

    tk.Button(
        controls,
        text="CUE",
        command=cue_1 if number == 1 else cue_2,
        bg="#252525",
        fg="white",
        font=("Arial", 9, "bold"),
        width=7,
        height=2
    ).pack(side="left", padx=4)

    global play1_button, play2_button

    if number == 1:

        play1_button = tk.Button(
            controls,
            text="▶",
            command=play_pause_1,
            bg="#164d24",
            fg="white",
            font=("Arial", 15, "bold"),
            width=7,
            height=2
        )

        play1_button.pack(
            side="left",
            padx=4
        )

    else:

        play2_button = tk.Button(
            controls,
            text="▶",
            command=play_pause_2,
            bg="#164d24",
            fg="white",
            font=("Arial", 15, "bold"),
            width=7,
            height=2
        )

        play2_button.pack(
            side="left",
            padx=4
        )

    tk.Button(
        controls,
        text="■",
        command=stop_1 if number == 1 else stop_2,
        bg="#252525",
        fg="white",
        font=("Arial", 10, "bold"),
        width=7,
        height=2
    ).pack(side="left", padx=4)

    # -------------------------
    # STATUS
    # -------------------------

    global status1, status2

    if number == 1:

        status1 = tk.Label(
            frame,
            text="READY",
            bg="#1c1c1c",
            fg="#999999",
            font=("Arial", 8)
        )

        status1.pack()

    else:

        status2 = tk.Label(
            frame,
            text="READY",
            bg="#1c1c1c",
            fg="#999999",
            font=("Arial", 8)
        )

        status2.pack()

    # -------------------------
    # TEMPO
    # -------------------------

    tk.Scale(
        frame,
        from_=20,
        to=-20,
        orient="horizontal",
        label="TEMPO",
        length=180,
        bg="#1c1c1c",
        fg="white",
        highlightthickness=0,
        troughcolor="#333333"
    ).pack(pady=3)


# =====================================================
# MIXER
# =====================================================

def create_mixer(parent):

    mixer = tk.Frame(
        parent,
        bg="#242424",
        width=300,
        height=620,
        highlightbackground="#444444",
        highlightthickness=2
    )

    mixer.pack(
        side="left",
        padx=8,
        pady=5
    )

    mixer.pack_propagate(False)

    tk.Label(
        mixer,
        text="MIXER",
        bg="#242424",
        fg="white",
        font=("Arial", 20, "bold")
    ).pack(pady=12)

    # -------------------------
    # MASTER
    # -------------------------

    tk.Label(
        mixer,
        text="MASTER",
        bg="#242424",
        fg="#aaaaaa",
        font=("Arial", 10, "bold")
    ).pack()

    master = tk.Scale(
        mixer,
        from_=1,
        to=0,
        resolution=0.01,
        orient="vertical",
        length=130,
        bg="#242424",
        fg="white",
        highlightthickness=0
    )

    master.set(1)
    master.pack()

    # -------------------------
    # EQ
    # -------------------------

    tk.Label(
        mixer,
        text="EQUALIZER",
        bg="#242424",
        fg="white",
        font=("Arial", 11, "bold")
    ).pack(pady=8)

    for name in ["HIGH", "MID", "LOW"]:

        tk.Scale(
            mixer,
            from_=10,
            to=-10,
            orient="horizontal",
            length=180,
            label=name,
            bg="#242424",
            fg="white",
            highlightthickness=0
        ).pack()

    # -------------------------
    # CROSSFADER
    # -------------------------

    tk.Label(
        mixer,
        text="CROSSFADER",
        bg="#242424",
        fg="white",
        font=("Arial", 10, "bold")
    ).pack(pady=10)

    tk.Label(
        mixer,
        text="DECK 1        DECK 2",
        bg="#242424",
        fg="#999999"
    ).pack()

    crossfader = tk.Scale(
        mixer,
        from_=0,
        to=1,
        resolution=0.01,
        orient="horizontal",
        length=230,
        bg="#242424",
        fg="white",
        highlightthickness=0,
        troughcolor="#111111",
        command=change_crossfader
    )

    crossfader.set(0.5)

    crossfader.pack()


# =====================================================
# TOP TITLE
# =====================================================

tk.Label(
    root,
    text="PYTHON DJ CONSOLE",
    bg="#111111",
    fg="white",
    font=("Arial", 22, "bold")
).pack(pady=10)


# =====================================================
# MAIN AREA
# =====================================================

main = tk.Frame(
    root,
    bg="#111111"
)

main.pack()


# Create decks

create_deck(main, 1)

create_mixer(main)

create_deck(main, 2)


# =====================================================
# CLOSE
# =====================================================

def close_app():

    pygame.mixer.quit()
    root.destroy()


root.protocol(
    "WM_DELETE_WINDOW",
    close_app
)


# =====================================================
# START
# =====================================================

root.mainloop()