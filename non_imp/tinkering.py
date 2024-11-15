import random
# import tkinter as tk
# import pygame
import matplotlib.pyplot as plt
import numpy
import sqlite3
import streamlit

xplot = [0.0]
yplot = [0.0]

for _ in range(100):
    xplot.append(xplot[-1] + 1)
    plus_minus = random.randrange(0, 2)
    if plus_minus == 0:
        yplot.append(yplot[-1] + float(numpy.random.random()))
    else:
        yplot.append(yplot[-1] - float(numpy.random.random()))

xplot1 = [0.0]
yplot1 = [0.0]

for _ in range(100):
    xplot1.append(xplot1[-1] + 1)
    plus_minus = random.randrange(0, 2)
    if plus_minus == 0:
        yplot1.append(yplot1[-1] + float(numpy.random.random()))
    else:
        yplot1.append(yplot1[-1] - float(numpy.random.random()))

plt.plot(xplot, yplot, color='green')
plt.plot(xplot1, yplot1, color='red')
streamlit.pyplot(plt.gcf())
# plt.show()

"""
file = sqlite3.connect('database.db')
cursor = file.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS user_data (id INTEGER PRIMARY KEY, username TEXT NOT NULL, password TEXT NOT NULL, balance REAL NOT NULL);
               ''')
"""
