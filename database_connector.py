import sqlite3

def main():
    conn = sqlite3.connect('chinook.db')
    return conn