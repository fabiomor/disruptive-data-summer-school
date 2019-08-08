# Disruptive Data Summer School - Test

#### This repository contains assignment projects for Disruptive Data Summer School 2019 - Data Science & Machine Learning in Viterbo

- **main.py** entry point of the whole project, use this class to launch single projects 
- **io_data.py** handles data access from both local csv and google spreadsheet (credentials API must be provided)
- **project1.py** tbd
- **project2.py** completed
- **project3.py** tbd
- **project4.py** completed
- **uris.csv** csv version of google sheets provided
- **words.csv** csv version of google sheets provided

##### Assignments

##### Project 1:

Starting from the site Curlie.org develops a script that extracts the categories listed on Curlie keeping the hierarchy between categories and save the results on a csv file or on a database of your choice.

##### Project 2:

This file (https://docs.google.com/spreadsheets/d/1y5HvjZgY3Fw2Qju9Y3KxpCsERJQcgTPFreHTXjWZSig/edit#gid=0) consists of two lists: the text1 list and the text2 list. Both lists are URIs from two different versions of the same website. Develop a script to associate each URI of the text1 variable with a URL of the text2 variable, according to a principle of textual similarity you chose.

If the script doesn't find any association for a certain URI of the first list in the second list should write ND.

##### Project 3:

Given this word list (https://docs.google.com/spreadsheets/d/1Clf6VpAwHRvTxeFft2TRCbSxLvMHO14zJiyA7fH1l5Y/edit#gid=0), write a script to estimate the search volume of each term on Google in the US in the last year.

##### Project 4:

Given this word list (https://docs.google.com/spreadsheets/d/1Clf6VpAwHRvTxeFft2TRCbSxLvMHO14zJiyA7fH1l5Y/edit#gid=0), write a script to:

- order the list from A to Z and generate a new ordered CSV file;

- count the number of words;

- evaluate the average word length for the list.