# import file and package
from scripts import lyrics_extraction
import argparse


def parse_arguments():

    '''Insert artist and song inputs.'''

    parser = argparse.ArgumentParser(description='Show Lyrics')
    # Selection of the artsit
    parser.add_argument('artist', type=str, help='Insert an artist',
                        default=None)
    # Selection of the song
    parser.add_argument('song', type=str, help='Insert a song', default=None)

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-q', '--quiet', action='store_true',
                       help='print quiet')
    # Selection of the level of verbosity
    group.add_argument('-v', '--verbose', action='store_true',
                       help='print verbose')
    args = parser.parse_args()

    return args


if __name__ == '__main__':
    # run parse argument
    args = parse_arguments()
    # run function from lyrics_extraction file
    data = lyrics_extraction.get_lyrics(args.artist, args.song)
