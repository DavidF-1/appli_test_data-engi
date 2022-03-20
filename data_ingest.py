#!/usr/bin/env python3
#!-*- coding:utf-8 -*-

import mysql.connector
import csv
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(host=host_name,user=user_name,passwd=user_password, database=db_name)
        print("Connection to MySQL Server successful for user {} ".format(user_name))
    except Error as e:
        print(f"The error '{e}' occurred")
        exit(1)
    return connection

def insert_table(connection, cursor, table_name, data_to):
    if table_name == "people":
        sql = "INSERT INTO people (prenom, nom, date_naissance, commune) VALUES(%s, %s, %s , %s)"
        values = (data_to['prenom'], data_to['nom'], data_to['date_naissance'], data_to['commune'])
        try:
            cursor.execute(sql, values)
            connection.commit()
        except mysql.connector.Error as err:
            print("An error occured: {}".format(err))
            exit(1)               
    else:
        sql = "INSERT INTO lieux (commune, departement, region) VALUES(%s, %s, %s)"
        values = (data_to['commune'], data_to['departement'], data_to['region'])
        try:
            cursor.execute(sql, values)
            connection.commit()
        except mysql.connector.Error as err:
            print("An error occured: {}".format(err))
            exit(1)

def read_and_write(connection, cursor, file_source, table_name):
    with open(file_source, newline='') as csvfile:
        freader = csv.reader(csvfile, quotechar='|')
        next(freader)
        if table_name == "people":
            for row in freader:
                data_to = {"prenom": row[0], "nom": row[1], "date_naissance": row[2], "commune": row[3]}
                insert_table(connection, cursor, table_name, data_to)
        else:
            for row in freader:
                data_to = {"commune": row[0], "departement": row[1], "region": row[2]}
                insert_table(connection, cursor, table_name, data_to)

def main():
    db_name = "people_lieux"
    table_lieux = "lieux"
    table_people = "people"
    file_source_l = "./data/lieux.csv"
    file_source_p = "./data/people.csv"

    connection = create_connection("localhost", "davidf", "", db_name)
    cursor = connection.cursor()

    read_and_write(connection, cursor, file_source_l, table_lieux)
    read_and_write(connection, cursor, file_source_p, table_people)
    
    cursor.close()

if __name__ == "__main__":
    main()
