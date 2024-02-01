# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 19:27:04 2024

@author: Erna Leticia
"""

import pandas

file = pandas.read_csv("country_data.csv")

print(file)

print(file.info())

print(file.describe())

# diab_data.csv
file_01 = pandas.read_csv("diab_data.csv")

print(file_01.info())

print(file_01.describe())

#housing_data.csv
file_02 = pandas.read_csv("housing_data.csv")

print(file_02.info())

print(file_02.describe())

#insurance_data.csv
file_03 = pandas.read_csv("insurance_data.csv")

print(file_03.info())

print(file_03.describe())

#iris_data.csv
file_04 = pandas.read_csv("iris.csv")

print(file_04.info())

print(file_04.describe())