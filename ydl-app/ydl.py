from tkinter import *
from tkinter import ttk

import pytube as pt


class YouTubeVideo():

    @property
    def streams(self):
        """
        Getter for video stream.
        """
        return self.video.streams

    @property
    def audio(self):
        """
        Getter for audio only.
        """
        return self.streams.get_audio_only()


    def __init__(self, video_url):
        self.video = pt.YouTube(
            url=video_url,
            on_progress_callback=self.show_progress_bar
        )

    def show_progress_bar(self, chunk, file_handler, bytes_remaining):
        """
        Display progress bar.
        """
        # Messy way of displaying Pytube progress bar in Tkinter
        percent = int(100*(file_size - bytes_remaining)/file_size)
        ttk.Label(tkinter_frame, text=f"{percent}% completed").grid(
            column=10,
            row=2,
            sticky=(W, E)
        )
        # # Check the usage of a progress bar
        # bar = ttk.Progressbar(
        #     tkinter_frame,
        #     orient=HORIZONTAL,
        #     length=100,
        #     mode="determinate"
        # ).grid(
        #     column=10,
        #     row=2,
        #     sticky=(W, E)
        # )
        # print(bar["value"])
        # bar["value"] += percent

        tkinter_frame.update_idletasks()
        print(f'{percent}% downloaded')

    def download(self, stream, gui, output='output', filename=None):
        """
        Download stream to local folder.
        """
        global file_size
        global tkinter_frame
        tkinter_frame = 0
        tkinter_frame = gui
        file_size = 0
        file_size = stream.filesize
        stream.download(
            output_path=output,
            filename=filename
        )