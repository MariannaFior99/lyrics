# import required package
import csv


def create_csv(path):

    '''Create csv if it does not already exist.'''
    # open with csv-write-mode as data
    with open(path, 'w', newline='') as data:
        # create columns
        columns = ['artist', 'song', 'lyric']
        writer = csv.writer(data)
        writer.writerow(columns)
    return data


def write_data(path, artist, song, lyric):

    '''Function characterized by a try and except statements'''
    try:
        open(path)
    # if a csv file in path does not exist create a new csv file in path
    except:
        create_csv(path)

    r = [artist, song, lyric]
    # open with csv-read-mode as data
    with open(path, 'r', newline='') as data:
        # insert the latest research in csv.reader
        rows = [line for line in csv.reader(data, delimiter=',')]
        # if research is not already present
        if r not in rows:
            with open(path, 'a', newline='') as data:
                # add the research
                writer = csv.writer(data)
                writer.writerow(r)
