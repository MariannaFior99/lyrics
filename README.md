# SARDE IN SAOR-Project

### Get the lyrics of desired song! :notes:

In this repository you can find a file named ```main.py``` that triggers the lyrics.ovh Lyrics API, retrieving the lyrics of a song you want giving the artist and title name!

When you run the program for the first time executing the main file with: ```$ python3 main.py "Rihanna" "Diamonds"```, it will create a file ```data_song.csv``` located in ```data``` folder, containing the outputs requested.

> **Note:** the project requires the following modules to run: *json, csv, pandas, unittest, argparse, os.

It will give you results similar to the following table:
 
|      artist     |       song       |                   lyric                   | 
|-----------------|------------------|-------------------------------------------|
|     Rihanna     |     Diamonds     |  Shine bright like a diamond              |
|	              |                  |  Shine bright like a diamond              |
|	              |                  |  Find light in the beautiful sea          |
|	              |                  |  I choose to be happy                     |
|		          |		             |	You and I, you and I                     |
|                 |                  |  We're like diamonds in the sky           |
|		          |		             |	...                                      | 
|                 |                  |  Shine bright like a diamond              |


> **Note:** additional lyrics will be added to the same file.