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
        # TODO: add progress bar to Tkinter GUI
        percent = int(100*(file_size - bytes_remaining)/file_size)
        print(f'{percent}% downloaded')


    def download(self, stream, output='output', filename=None):
        """
        Download stream to local folder.
        """
        global file_size
        file_size = 0
        file_size = stream.filesize
        stream.download(
            output_path=output,
            filename=filename
        )

