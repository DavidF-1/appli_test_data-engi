# appli_test_data-engi
# About The Project 
- This project is about reading data from csv file,
- inserting those data into a relational dabase,
- reading data from multiple tables,an
- The results will show numbers of people
- listed by region and departement.

# Built With
- Ubuntu 20.04.4 LTS
- MySQL Server Community Edition 8.0.28-0ubuntu0.20.04.3
- Python 3.8.10 (default, Nov 26 2021, 20:14:08)

# Prerequisites
- sudo apt-get install mysql-server
- pip3 install mysql-connector-python

# Architecture Tree
- ./appli_test_data-engi/ : 
	3 scripts to execute with python3 :
	- create_db_schema.py
	- data_ingest.py
	- get_results.py
- ./appli_test_data-engi/data :
	a directory containing 3 files:
	- exemple_resultat.json, shows expecting format results
	- lieux.csv, data source about "lieux"
	- people.csv, data source about people
- /appli_test_data-engi/results : 
	a directory where json files containing results will be stored stamped with time in miliseconds# appli_test_data-engi
