import tkinter as tk
from tkinter import filedialog
import pygame


# ---------------- PYGAME AUDIO ----------------
pygame.mixer.init()

channel_1 = pygame.mixer.Channel(0)
channel_2 = pygame.mixer.Channel(1)

sound_1 = None
sound_2 = None

playing_1 = False
playing_2 = False


# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Python DJ Console")
root.geometry("1100x650")
root.configure(bg="#181818")
root.resizable(False, False)


# ---------------- FUNCTIONS ----------------

def load_song(deck):
    global sound_1, sound_2

    file = filedialog.askopenfilename(
        title="Select Song",
        filetypes=[
            ("Audio Files", "*.mp3 *.wav *.ogg"),
            ("MP3 Files", "*.mp3"),
            ("WAV Files", "*.wav")
        ]
    )

    if not file:
        return

    if deck == 1:
        sound_1 = pygame.mixer.Sound(file)
        song_name_1.config(text=file.split("/")[-1])

    else:
        sound_2 = pygame.mixer.Sound(file)
        song_name_2.config(text=file.split("/")[-1])


def play_pause(deck):
    global playing_1, playing_2

    if deck == 1:

        if sound_1 is None:
            return

        if playing_1:
            channel_1.pause()
            playing_1 = False
            play1_btn.config(text="▶")

        else:
            channel_1.play(sound_1, loops=-1)
            playing_1 = True
            play1_btn.config(text="Ⅱ")


    else:

        if sound_2 is None:
            return

        if playing_2:
            channel_2.pause()
            playing_2 = False
            play2_btn.config(text="▶")

        else:
            channel_2.play(sound_2, loops=-1)
            playing_2 = True
            play2_btn.config(text="Ⅱ")


def stop_song(deck):
    global playing_1, playing_2

    if deck == 1:
        channel_1.stop()
        playing_1 = False
        play1_btn.config(text="▶")

    else:
        channel_2.stop()
        playing_2 = False
        play2_btn.config(text="▶")


def cue_song(deck):

    if deck == 1 and sound_1:
        channel_1.stop()
        channel_1.play(sound_1)

    elif deck == 2 and sound_2:
        channel_2.stop()
        channel_2.play(sound_2)


def update_volume(value):

    volume = float(value)

    channel_1.set_volume(volume)
    channel_2.set_volume(volume)


def update_crossfader(value):

    value = float(value)

    # Left = Deck 1
    # Right = Deck 2

    left_volume = 1 - value
    right_volume = value

    channel_1.set_volume(left_volume)
    channel_2.set_volume(right_volume)


def update_deck1_volume(value):
    channel_1.set_volume(float(value))


def update_deck2_volume(value):
    channel_2.set_volume(float(value))


def close_app():
    pygame.mixer.quit()
    root.destroy()


# ==========================================================
#                       TITLE
# ==========================================================

title = tk.Label(
    root,
    text="PYTHON DJ CONSOLE",
    font=("Arial", 22, "bold"),
    bg="#181818",
    fg="white"
)

title.pack(pady=10)


# ==========================================================
#                       MAIN FRAME
# ==========================================================

main_frame = tk.Frame(
    root,
    bg="#222222"
)

main_frame.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=10
)


# ==========================================================
#                       DECK 1
# ==========================================================

deck1 = tk.Frame(
    main_frame,
    bg="#202020",
    width=360,
    height=540
)

deck1.pack(
    side="left",
    padx=10,
    pady=10
)

deck1.pack_propagate(False)


tk.Label(
    deck1,
    text="DECK 1",
    font=("Arial", 18, "bold"),
    bg="#202020",
    fg="white"
).pack(pady=8)


# ---------------- JOG WHEEL ----------------

canvas1 = tk.Canvas(
    deck1,
    width=260,
    height=260,
    bg="#202020",
    highlightthickness=0
)

canvas1.pack()

canvas1.create_oval(
    15, 15, 245, 245,
    fill="#111111",
    outline="#444444",
    width=8
)

canvas1.create_oval(
    45, 45, 215, 215,
    fill="#181818",
    outline="#555555",
    width=3
)

canvas1.create_oval(
    90, 90, 170, 170,
    fill="#222222",
    outline="#777777",
    width=3
)

canvas1.create_text(
    130,
    130,
    text="JOG",
    fill="white",
    font=("Arial", 14, "bold")
)


# ---------------- SONG NAME ----------------

song_name_1 = tk.Label(
    deck1,
    text="No song loaded",
    bg="#202020",
    fg="#cccccc",
    font=("Arial", 10)
)

song_name_1.pack(pady=3)


# ---------------- LOAD ----------------

tk.Button(
    deck1,
    text="LOAD SONG",
    command=lambda: load_song(1),
    bg="#333333",
    fg="white",
    width=15,
    font=("Arial", 10, "bold")
).pack(pady=5)


# ---------------- CUE + PLAY ----------------

control1 = tk.Frame(
    deck1,
    bg="#202020"
)

control1.pack(pady=8)

tk.Button(
    control1,
    text="CUE",
    command=lambda: cue_song(1),
    bg="#333333",
    fg="white",
    width=8,
    height=2,
    font=("Arial", 10, "bold")
).pack(side="left", padx=5)

play1_btn = tk.Button(
    control1,
    text="▶",
    command=lambda: play_pause(1),
    bg="#174d25",
    fg="white",
    width=8,
    height=2,
    font=("Arial", 14, "bold")
)

play1_btn.pack(side="left", padx=5)

tk.Button(
    control1,
    text="■",
    command=lambda: stop_song(1),
    bg="#333333",
    fg="white",
    width=8,
    height=2,
    font=("Arial", 10, "bold")
).pack(side="left", padx=5)


# ---------------- VOLUME ----------------

tk.Label(
    deck1,
    text="VOLUME",
    bg="#202020",
    fg="white"
).pack()

volume1 = tk.Scale(
    deck1,
    from_=1,
    to=0,
    resolution=0.01,
    orient="vertical",
    length=100,
    bg="#202020",
    fg="white",
    highlightthickness=0,
    command=update_deck1_volume
)

volume1.set(1)
volume1.pack()


# ==========================================================
#                       MIXER
# ==========================================================

mixer = tk.Frame(
    main_frame,
    bg="#292929",
    width=220,
    height=540
)

mixer.pack(
    side="left",
    padx=5,
    pady=10
)

mixer.pack_propagate(False)


tk.Label(
    mixer,
    text="MIXER",
    font=("Arial", 18, "bold"),
    bg="#292929",
    fg="white"
).pack(pady=10)


# ---------------- CHANNEL VOLUME ----------------

tk.Label(
    mixer,
    text="CHANNEL 1",
    bg="#292929",
    fg="#bbbbbb"
).pack()

mix1 = tk.Scale(
    mixer,
    from_=1,
    to=0,
    resolution=0.01,
    orient="vertical",
    length=120,
    bg="#292929",
    fg="white",
    highlightthickness=0,
    command=update_deck1_volume
)

mix1.set(1)
mix1.pack(side="left", padx=12)


tk.Label(
    mixer,
    text="CHANNEL 2",
    bg="#292929",
    fg="#bbbbbb"
).pack()

mix2 = tk.Scale(
    mixer,
    from_=1,
    to=0,
    resolution=0.01,
    orient="vertical",
    length=120,
    bg="#292929",
    fg="white",
    highlightthickness=0,
    command=update_deck2_volume
)

mix2.set(1)
mix2.pack(side="right", padx=12)


# ---------------- EQ ----------------

eq_frame = tk.Frame(
    mixer,
    bg="#292929"
)

eq_frame.pack(
    pady=15
)

tk.Label(
    eq_frame,
    text="EQ",
    bg="#292929",
    fg="white",
    font=("Arial", 12, "bold")
).pack()

for name in ["HIGH", "MID", "LOW"]:

    tk.Scale(
        eq_frame,
        from_=10,
        to=-10,
        orient="horizontal",
        length=130,
        label=name,
        bg="#292929",
        fg="white",
        highlightthickness=0
    ).pack()


# ---------------- CROSSFADER ----------------

tk.Label(
    mixer,
    text="CROSSFADER",
    bg="#292929",
    fg="white",
    font=("Arial", 10, "bold")
).pack(pady=5)

crossfader = tk.Scale(
    mixer,
    from_=0,
    to=1,
    resolution=0.01,
    orient="horizontal",
    length=170,
    bg="#292929",
    fg="white",
    highlightthickness=0,
    command=update_crossfader
)

crossfader.set(0.5)
crossfader.pack()


# ==========================================================
#                       DECK 2
# ==========================================================

deck2 = tk.Frame(
    main_frame,
    bg="#202020",
    width=360,
    height=540
)

deck2.pack(
    side="left",
    padx=10,
    pady=10
)

deck2.pack_propagate(False)


tk.Label(
    deck2,
    text="DECK 2",
    font=("Arial", 18, "bold"),
    bg="#202020",
    fg="white"
).pack(pady=8)


# ---------------- JOG WHEEL ----------------

canvas2 = tk.Canvas(
    deck2,
    width=260,
    height=260,
    bg="#202020",
    highlightthickness=0
)

canvas2.pack()

canvas2.create_oval(
    15, 15, 245, 245,
    fill="#111111",
    outline="#444444",
    width=8
)

canvas2.create_oval(
    45, 45, 215, 215,
    fill="#181818",
    outline="#555555",
    width=3
)

canvas2.create_oval(
    90, 90, 170, 170,
    fill="#222222",
    outline="#777777",
    width=3
)

canvas2.create_text(
    130,
    130,
    text="JOG",
    fill="white",
    font=("Arial", 14, "bold")
)


# ---------------- SONG NAME ----------------

song_name_2 = tk.Label(
    deck2,
    text="No song loaded",
    bg="#202020",
    fg="#cccccc",
    font=("Arial", 10)
)

song_name_2.pack(pady=3)


# ---------------- LOAD ----------------

tk.Button(
    deck2,
    text="LOAD SONG",
    command=lambda: load_song(2),
    bg="#333333",
    fg="white",
    width=15,
    font=("Arial", 10, "bold")
).pack(pady=5)


# ---------------- CUE + PLAY ----------------

control2 = tk.Frame(
    deck2,
    bg="#202020"
)

control2.pack(pady=8)

tk.Button(
    control2,
    text="CUE",
    command=lambda: cue_song(2),
    bg="#333333",
    fg="white",
    width=8,
    height=2,
    font=("Arial", 10, "bold")
).pack(side="left", padx=5)

play2_btn = tk.Button(
    control2,
    text="▶",
    command=lambda: play_pause(2),
    bg="#174d25",
    fg="white",
    width=8,
    height=2,
    font=("Arial", 14, "bold")
)

play2_btn.pack(side="left", padx=5)

tk.Button(
    control2,
    text="■",
    command=lambda: stop_song(2),
    bg="#333333",
    fg="white",
    width=8,
    height=2,
    font=("Arial", 10, "bold")
).pack(side="left", padx=5)


# ---------------- VOLUME ----------------

tk.Label(
    deck2,
    text="VOLUME",
    bg="#202020",
    fg="white"
).pack()

volume2 = tk.Scale(
    deck2,
    from_=1,
    to=0,
    resolution=0.01,
    orient="vertical",
    length=100,
    bg="#202020",
    fg="white",
    highlightthickness=0,
    command=update_deck2_volume
)

volume2.set(1)
volume2.pack()


# ==========================================================
#                       CLOSE
# ==========================================================

root.protocol("WM_DELETE_WINDOW", close_app)

root.mainloop()