import sqlite3
import tkinter as tk
from tkinter import messagebox


# --- LANGKAH 1: Inisialisasi Database SQLite ---
def init_db():
    conn = sqlite3.connect("nilai_siswa.db")
    cursor = conn.cursor()
    # Membuat tabel sesuai instruksi
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT NOT NULL,
            biologi INTEGER,
            fisika INTEGER,
            inggris INTEGER,
            prediksi_fakultas TEXT
        )
    """
    )
    conn.commit()
    conn.close()


# --- LANGKAH 2: Logika Prediksi dan Simpan Data ---
def submit_data():
    nama = entry_nama.get().strip()
    val_bio = entry_bio.get().strip()
    val_fis = entry_fis.get().strip()
    val_ing = entry_ing.get().strip()

    # Validasi input tidak boleh kosong
    if not nama or not val_bio or not val_fis or not val_ing:
        messagebox.showerror("Error", "Semua kolom harus diisi!")
        return

    # Validasi input harus berupa angka
    try:
        bio = int(val_bio)
        fis = int(val_fis)
        ing = int(val_ing)
    except ValueError:
        messagebox.showerror("Error", "Nilai mata pelajaran harus berupa angka!")
        return

    # Logika Kondisi Prediksi Fakultas
    if bio > fis and bio > ing:
        prediksi = "Kedokteran"
    elif fis > bio and fis > ing:
        prediksi = "Teknik"
    elif ing > bio and ing > fis:
        prediksi = "Bahasa"
    else:
        # Penanganan jika ada nilai tertinggi yang sama berimbang
        prediksi = "Belum Dapat Diprediksi (Nilai Seimbang)"

    # Menyimpan data ke SQLite
    try:
        conn = sqlite3.connect("nilai_siswa.db")
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
            VALUES (?, ?, ?, ?, ?)
        """,
            (nama, bio, fis, ing, prediksi),
        )
        conn.commit()
        conn.close()

        # Tampilkan hasil ke user dan reset form
        messagebox.showinfo(
            "Sukses", f"Data berhasil disimpan!\nHasil Prediksi: {prediksi}"
        )
        clear_fields()
    except Exception as e:
        messagebox.showerror("Database Error", f"Gagal menyimpan data: {e}")


def clear_fields():
    entry_nama.delete(0, tk.END)
    entry_bio.delete(0, tk.END)
    entry_fis.delete(0, tk.END)
    entry_ing.delete(0, tk.END)


# --- LANGKAH 3: Pembuatan UI dengan Tkinter ---
# Jalankan inisialisasi database di awal
init_db()

root = tk.Tk()
root.title("Input Nilai & Prediksi Fakultas")
root.geometry("400x300")
root.resizable(False, False)

# Label Judul
label_title = tk.Label(
    root, text="Sistem Prediksi Fakultas Siswa", font=("Arial", 14, "bold")
)
label_title.pack(pady=10)

# Frame Kontainer Form
frame_form = tk.Frame(root)
frame_form.pack(pady=10)

# Entry untuk Nama Siswa
tk.Label(frame_form, text="Nama Siswa:", font=("Arial", 10)).grid(
    row=0, column=0, sticky="w", pady=5, padx=5
)
entry_nama = tk.Entry(frame_form, width=25)
entry_nama.grid(row=0, column=1, pady=5, padx=5)

# Entry untuk Nilai Biologi
tk.Label(frame_form, text="Nilai Biologi:", font=("Arial", 10)).grid(
    row=1, column=0, sticky="w", pady=5, padx=5
)
entry_bio = tk.Entry(frame_form, width=25)
entry_bio.grid(row=1, column=1, pady=5, padx=5)

# Entry untuk Nilai Fisika
tk.Label(frame_form, text="Nilai Fisika:", font=("Arial", 10)).grid(
    row=2, column=0, sticky="w", pady=5, padx=5
)
entry_fis = tk.Entry(frame_form, width=25)
entry_fis.grid(row=2, column=1, pady=5, padx=5)

# Entry untuk Nilai Inggris
tk.Label(frame_form, text="Nilai Inggris:", font=("Arial", 10)).grid(
    row=3, column=0, sticky="w", pady=5, padx=5
)
entry_ing = tk.Entry(frame_form, width=25)
entry_ing.grid(row=3, column=1, pady=5, padx=5)

# Button Tkinter untuk Submit Nilai
btn_submit = tk.Button(
    root,
    text="Submit & Prediksi",
    command=submit_data,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5,
)
btn_submit.pack(pady=15)

# Menjalankan Aplikasi
root.mainloop()
