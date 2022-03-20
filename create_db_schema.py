#!/usr/bin/env python3
#!-*- coding:utf-8 -*-

import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(host=host_name,user=user_name,passwd=user_password)
        print("Connection to MySQL Server successful for user {} ".format(user_name))
    except Error as e:
        print(f"The error '{e}' occurred")
        exit(1)
    return connection

def create_database(cursor, db_name):
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(db_name))
        print("Database {} created.".format(db_name))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

def create_table(cursor, db_name, table_name):
    try:
        cursor.execute("USE {}".format(db_name))
        cursor.execute(table_name)
        print("Table {} created.".format(table_name))
    except mysql.connector.Error as err:
        print("Failed creating table: {}".format(err))
        exit(1)

def main():
    db_name = "people_lieux"

    table_people = """CREATE TABLE IF NOT EXISTS `people` (
        `people_id` int(6) NOT NULL AUTO_INCREMENT,
        `prenom` varchar(50) DEFAULT NULL,
        `nom` varchar(50) DEFAULT NULL,
        `date_naissance` date DEFAULT NULL,
        `commune` varchar(50) DEFAULT NULL,
        PRIMARY KEY (`people_id`)
        ) ENGINE=InnoDB;"""

    table_lieux = """CREATE TABLE IF NOT EXISTS `lieux` (
        `lieux_id` int(6) NOT NULL AUTO_INCREMENT,
        `commune` varchar(50) DEFAULT NULL,
        `departement` varchar(50) DEFAULT NULL,
        `region` varchar(50) DEFAULT NULL,
        PRIMARY KEY (`lieux_id`)
        ) ENGINE=InnoDB;"""

    connection = create_connection("localhost", "davidf", "")
    cursor = connection.cursor()
    cr_db = create_database(cursor, db_name)
    cr_table_p = create_table(cursor, db_name, table_people)
    cr_table_l = create_table(cursor, db_name, table_lieux)

    cursor.close()

if __name__ == "__main__":
    main()
