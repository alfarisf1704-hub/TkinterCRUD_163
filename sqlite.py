import sqlite3
import tkinter as tk
from tkinter import messagebox as msg

def create_db():
    conn = sqlite3.connect("nilai_siswa.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT NOT NULL,
            biologi INTEGER NOT NULL,
            fisika INTEGER NOT NULL,
            inggris INTEGER NOT NULL,
            prediksi_fakultas TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

DB_Name = "nilai_siswa.db"
def run_query(sql, params=()):
    conn = sqlite3.connect(DB_Name)
    try:
        with conn:
            return conn.execute(sql, params).fetchall()
    finally:
        conn.close()

def add_nilai_siswa(biologi, fisika, inggris):
    run_query(
        "INSERT INTO nilai_siswa (biologi, fisika, inggris) VALUES (?, ?, ?)",
        (biologi, fisika, inggris),
    )


root = tk.Tk()
L1= tk.Label(root,text="Sistem Prediksi Prodi Dari Nilai")
L1.grid(row=0, column=0,columnspan=2)
L2= tk.Label(root,text="Biologi :")
L2.grid(row=1,column=0)
entry = tk.Entry(root, bd=5)
entry.grid(row=1,column=1)
submit = tk.Button(root,text="SUBMIT")
submit.grid(row=3,column=0,columnspan=2)
root.mainloop()