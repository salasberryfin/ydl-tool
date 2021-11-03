from tkinter import *
from tkinter import ttk

from ydl import YouTubeVideo


class DesktopApp():

    def __init__(self, root):
        """
        Initialize the GUI application
        """

        root.title('Test app')

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.video_url = StringVar()
        video_url_entry = ttk.Entry(
            mainframe,
            width=7,
            textvariable=self.video_url
        )
        video_url_entry.grid(
            column=2,
            row=1,
            sticky=(W, E)
        )

        ttk.Button(
            mainframe,
            text='Download Audio',
            command=lambda: self.run()
        ).grid(
            column=2,
            row=2,
            sticky=W
        )

    def run(self):
        """
        Invoke the YouTube utility.
        """
        yt = YouTubeVideo(self.video_url.get())
        audio = yt.audio
        yt.download(audio, filename='output.mp4')


root = Tk()
DesktopApp(root)
root.mainloop()
