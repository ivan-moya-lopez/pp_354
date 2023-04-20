How To Create Small Random Sample From Large CSV File.

subsample is a command line tool built with Python. As long as you have pip installed, you can use the following:

pip install subsample

The workflow is simple:

    Identify the original CSV file to sample
    Decide how many rows you want
    Pipe that to a new file

Implemented in code:

subsample -n 1000 data.csv > data_sample.csv


Ref. https://www.nagraj.net/notes/how-to-create-small-random-sample-from-large-csv-file/
