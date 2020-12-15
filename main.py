# import file
from scripts import lyrics_extraction

if __name__ == '__main__':
    # run function from lyrics_extraction file
    data = lyrics_extraction.get_lyrics("Rihanna", "Diamonds")
