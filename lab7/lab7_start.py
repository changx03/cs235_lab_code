"""Startup code for Lab 7 SQLAlchemy

Author: Luke Chang (xcha011@aucklanduni.ac.nz)
Date: 19/09/2022

"""
import os
import sqlite3

print('ROOT:', os.getcwd())

connection = sqlite3.connect('covid-19.db')
cursor = connection.cursor()

response = cursor.execute('SELECT title FROM articles LIMIT 5;').fetchall()
print(*response, sep='\n')

################################################################################
# Task 4: Add your code here:


# Insert a comment to Article id=10 by 'fmercury'
# Insert a comment to Article id=20 by 'fmercury'

# Delete Article id=50

# Print all comments by 'fmercury'

################################################################################

connection.close()
