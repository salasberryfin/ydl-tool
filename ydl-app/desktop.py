from tkinter import *
from tkinter import ttk

from ydl import YouTubeVideo


WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
PADDING = 3

class DesktopApp():

    def __init__(self):
        """
            Initialize the GUI application
        """

        self.root = Tk()
        self.root.eval("tk::PlaceWindow . center")
        self.root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
        self.root.title('YouTube downloader')
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.mainframe = ttk.Frame(self.root, padding=f"{PADDING} {PADDING} 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        video_url = self.url(
            coords={"column": 2, "row": 1}
        )

        # Download button
        self.button(
            name="Download audio",
            coords={
                "column": 2,
                "row": 2
            },
            action=self.run,
            value=video_url,
        )

        self.root.mainloop()

    def button(self, name, coords, action, value):
        """
            Create a button and execute the given action
        """
        ttk.Button(
            self.mainframe,
            text=name,
            command=lambda: action(value.get())
        ).grid(
            column=coords.get("column"),
            row=coords.get("row"),
            sticky=W
        )

    def url(self, coords):
        video_url = StringVar()
        video_url_form = ttk.Entry(
            self.mainframe,
            width=int(WINDOW_WIDTH/10),
            textvariable=video_url
        )
        video_url_form.grid(
            column=coords.get("column"),
            row=coords.get("row"),
            sticky=(W, E)
        )
        video_url_form.insert(0, "Video URL...")
        
        return video_url

    def output(self):
        """
            Select output folder from text box
        """
        output_folder = StringVar()
        output_folder_form = ttk.Entry(
            self.mainframe,
            width=7,
            textvariable=output_folder,
        )
        output_folder_form.grid(
            column=10,
            row=2,
            sticky=(W, E)
        )
        output_folder_form.insert(0, "Output folder...")

    def run(self, url):
        """
            Invoke the YouTube utility.
        """
        yt = YouTubeVideo(url)
        audio = yt.audio
        yt.download(audio, self.root)

DesktopApp()
