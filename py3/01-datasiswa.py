#!/usr/bin/python3
# data siswa kelas 9A
# soal latihan CRUD python3 dengan sqlite3

import sqlite3



# cek table
conn = sqlite3.connect('datasiswa.db')
cursor = conn.cursor()
query = """CREATE TABLE IF NOT EXISTS siswa (
              siswa_id INTEGER PRIMARY KEY NOT NULL UNIQUE,
              siswa_nama TEXT UNIQUE,
              siswa_alamat TEXT,
              siswa_notelp TEXT,
              siswa_stamp TEXT
      )"""
cursor.execute(query)
conn.commit()


# custom func
def mclear():
  print("\n" * 100)

def lihatdata():
  mclear()
  print("DATA SISWA KELAS 9A")
  cursor = conn.execute("SELECT * FROM siswa ORDER BY siswa.siswa_nama ASC")
  index = 0
  rows = cursor.fetchall()
  if not rows:
    print("...Data kosong...")
  for row in rows:
    index += 1
    print(f"{index}. {row[1]}. [{row[0]}]")
  print("\nKetik [no ID] untuk detail")
  print("Ketik [K] untuk kembali")
  pil = input("Detail > ")
  try:
    pil = int(pil)
  except ValueError:
    pil = pil
  if isinstance(pil, int):
    lihatdetail(pil)
  elif pil in ["k", "K"]:
    menu()
  else:
    input("Pilihan tidak valid, tekan enter")
    lihatdata()


def lihatdetail(id):
  mclear()
  id = str(id)
  print(f"DATA SISWA ID: {id}")
  cursor = conn.execute("SELECT * FROM siswa WHERE siswa.siswa_id = %s" % (id))
  for data in cursor.fetchall():
    print(f"Nama: {data[1]}\nAlamat: {data[2]}\nNo. Telp: {data[3]}\n")
  print("\nKetik [E] untuk mengedit data")
  print("Ketik [H] untuk hapus data")
  print("Ketik [K] untuk kembali")
  pil = input("Edit > ")
  if pil in ["e", "E"]:
    namasis = input("Nama: ")
    if not namasis:
      input("Nama wajib diisi, kembali ke detail")
      lihatdetail(id)
    alamatsis = input("Alamat: ")
    notelpsis = input("No. telp: ")
    cursor.execute("UPDATE siswa SET siswa_nama = '%s' , siswa_alamat = '%s', siswa_notelp = '%s' WHERE siswa_id = '%s'" % (namasis, alamatsis, notelpsis, id))
    hasil = cursor.rowcount
    conn.commit()
    if hasil > 0:
      input("Berhasil mengedit data, tekan enter")
      lihatdetail(id)
    else:
      input("Gagal mengedit data, tekan enter")
      lihatdetail(id)
  elif pil in ["h", "h"]:
    cursor.execute("DELETE FROM siswa WHERE siswa_id = '%s'" % (id))
    hasil = cursor.rowcount
    conn.commit()
    if hasil > 0:
      input("Berhasil hapus data, tekan enter")
      lihatdata()
    else:
      input("Gagal hapus data, tekan enter")
      lihatdata()
  elif pil in ["k", "K"]:
    lihatdata()
  else:
    input("Pilihan tidak valid, tekan enter")
    lihatdetail(id)

def insertdata():
  mclear()
  print("INSERT DATA SISWA")
  namasis = input("Nama: ")
  if not namasis:
    insertdata()
  alamatsis = input("Alamat: ")
  notelpsis = input("No. telp: ")
  yakin = input("\nYakin data sudah benar?\ny = ya / t = tidak / k = kembali\nYakin? > ")
  if yakin in ["t", "T"]:
    insertdata()
  elif yakin in ("y", "Y"):
    query = ("INSERT INTO siswa (siswa_id, siswa_nama, siswa_alamat, siswa_notelp) VALUES (:ID, :Nama, :Alamat, :Notelp)")
    params = {
      'ID': None,
      'Nama': namasis,
      'Alamat': alamatsis,
      'Notelp': notelpsis
    }
    cursor.execute(query, params)
    hasil = cursor.rowcount
    conn.commit()
    print(f"Berhasil menginput {hasil} data")
  elif yakin in ("k", "K"):
    menu()
  else:
    input("Pilihan tidak valid, kembali ke insert data")
    insertdata()

def menu():
  mclear()
  print("Aplikasi Data Siswa kelas 9A")
  print("[L] Lihat data")
  print("[I] Insert data")
  print("\nKetik [X] untuk keluar")
  pil = input("> ")
  if pil in ["l", "L"]:
    lihatdata()
    input("\n\nKembali ke menu, tekan enter")
    mclear()
    menu()
  elif pil in ["i", "I"]:
    insertdata()
    input("\n\nKembali ke menu, tekan enter")
    mclear()
    menu()
  elif pil in ["x", "X"]:
    print("Terima kasih")
    exit()
  else:
    input("Pilihan tidak valid, tekan enter")
    menu()



# draw menu
menu()
