import sys
from argparse import ArgumentParser, Namespace
from pydub import AudioSegment

def get_args() -> Namespace:
    parser = ArgumentParser()

    parser.add_argument(
        '-b',
        dest='bitrate',
        help='Bitrate for output mp3 file, in kbps.  Default value is 320.',
        default=320
    )
    parser.add_argument(
        '-i',
        dest='input_filepath',
        help='File path to a file listing URLs.',
        required=True
    )

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    return parser.parse_args()

def print_and_exit(msg: str) -> None:
    print(msg)
    sys.exit(0)

def convert_to_mp3(infile: str, bitrate: int, last_dot_index: int) -> None:
    filename = infile[ : last_dot_index]
    file_ext = infile[last_dot_index : ]
    source = {
        '.ogg': AudioSegment.from_ogg,
        '.wav': AudioSegment.from_wav
    }
    song = source[file_ext](infile)
    song.export(f"{filename}.mp3", format="mp3", bitrate=f"{bitrate}k")

def main() -> None:
    opts = get_args()
    infile = opts.input_filepath
    last_dot = infile.rfind('.')
    infile_ext = infile[last_dot:]
    VALID_FILE_TYPES = ('.ogg', '.wav')

    if not infile_ext in VALID_FILE_TYPES:
        msg = f"Error: Invalid input file type.  Valid file types are {VALID_FILE_TYPES}"
        print_and_exit(msg)

    convert_to_mp3(infile, opts.bitrate, last_dot)

if __name__ == "__main__":
    main()