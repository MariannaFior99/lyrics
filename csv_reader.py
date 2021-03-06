# import required package
import pandas as pd


def read_data(path):

    '''Read the latest research.'''
    # if wrong input, print the type of error
    try:
        user_data = pd.read_csv(path, sep=',', header=0)
    except FileNotFoundError:
        print('The file does not exist')
        return

    except ValueError:
        print('File has a wrong encoding')
        return

    except UnicodeDecodeError:
        print('File has a wrong encoding')
        return

    print(user_data['lyric'].iloc[-1])


# otherwise add lyrics to data
if __name__ == '__main__':
    path = 'data/data_song.csv'
    read_data(path)
