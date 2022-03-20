#!/usr/bin/env python3
#!-*- coding:utf-8 -*-

import json, time
import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(host=host_name,user=user_name,passwd=user_password, database=db_name)
    except Error as e:
        print(f"The error '{e}' occurred")
        exit(1)
    return connection

def main():
    db_name = "people_lieux"

    connection = create_connection("localhost", "davidf", "", db_name)
    cursor = connection.cursor()
    
    sql_reg = "SELECT COUNT(people_id) AS nbre_pers, region FROM people LEFT JOIN lieux ON lieux.commune = people.commune GROUP BY lieux.region"
    cursor.execute(sql_reg)
    rows = cursor.fetchall()
    result_reg = {}
    for row in rows:
        result_reg[row[1]] = row[0]

    sql_dep = "SELECT COUNT(people_id) AS nbre_pers, departement FROM people LEFT JOIN lieux ON lieux.commune = people.commune GROUP BY lieux.departement"
    cursor.execute(sql_dep)
    rows = cursor.fetchall()
    result_dep = {}
    for row in rows:
        result_dep[row[1]] = row[0]
    
    cursor.close()

    file_reg_dest = "./results/results_region_" + str(int(time.time() * 1000)) + ".json"
    with open(file_reg_dest, 'w', encoding='utf8') as json_file:
        data_reg = json.dumps(result_reg, sort_keys=True, ensure_ascii=False)
        print(json.dumps(result_reg, sort_keys=True, indent = 2, ensure_ascii=False))
        json_file.write(data_reg)

    file_dep_dest = "./results/results_departement_" + str(int(time.time() * 1000)) + ".json"
    with open(file_dep_dest, 'w', encoding='utf8') as json_file:
        data_dep = json.dumps(result_dep, sort_keys=True, ensure_ascii=False)
        print(json.dumps(result_dep, sort_keys=True, indent = 2, ensure_ascii=False))
        json_file.write(data_dep)

if __name__ == "__main__":
    main()
