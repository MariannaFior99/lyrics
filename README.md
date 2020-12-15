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
|-----------------|------------------|-------------------------------------------|

> **Note:** additional lyrics will be added to the same file.


### Command line parameters
In order to execute the ```main.py``` file, a few command line parameters must be passed.
#### Positional arguments
- **artist**: The name of artist 
- **song**: The title song you want the lyrics of

#### Optional Argument
- **-h, --help**: show required inputs;
- **-q, --quiet**: disable reporting on warnings;
- **-v, --verbose**: print detailed operations about the link operation.

#### Retrieve last user research
To display the last lyrics run:  ```$ python3 csv_reader.py```

### Testing
Tests on ```csv_reader.py``` are provided in ```test_csv_reader.py```.
To run the tests do:
```$ cd lyrics```
```$ python3 -m unittest -v -b test_csv_reader.py```

```
test_empty_datafile (test_csv_reader.TestCSVReader) ... ok
test_file_is_not_csv (test_csv_reader.TestCSVReader) ... ok
test_no_datafile (test_csv_reader.TestCSVReader) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.007s

OK
```

### References
The API we use works on [lyrics.ovh](https://lyrics.ovh).

### Authors
- **Cabrele Sofia-872213**
- **Corbetti Elena-873379**
- **Fior Marianna-872571**

### License 
[GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)
