import argparse
import pytube as pt

TEST_URL = 'https://youtu.be/QHtSaA2o2Cs'


def download(stream, output='output', filename=None):
    """
    Download stream to local folder.
    """
    stream.download(
        output_path=output,
        filename=filename,
    )


def extract_audio(streams):
    """
    Extract audio only from YouTube object streams.
    return  :Stream
    """
    audio_only = streams.get_audio_only()   # Defaults to mp4

    return audio_only

def main():
    parser = argparse.ArgumentParser(
        description='Read input for download details'
    )
    parser.add_argument(
        '-u', '--url',
        help='YouTube video URL',
        required=True
    )
    args = parser.parse_args()
    video_url = args.url

    video = pt.YouTube(
        url=video_url,
    )
    streams = video.streams

    download(extract_audio(streams))

if __name__ == '__main__':
    main()

