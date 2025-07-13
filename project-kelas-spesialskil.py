# TUGAS 02 Variabel, Input & Output Percabangan (if, elif, else), Perulangan (for/while), Struktur Data
# Implementasi Pada Studi Kasus Pemesanan Coffe Shop berbasis GUI

import tkinter as tk
from tkinter import messagebox

# Harga Menu Kopi
menu_kopi = {
    "Espresso": 15000,
    "Cappuccino": 20000,
    "Americano": 18000,
    "Mocha": 18000
}

pesanan = []

# Fungsi pesanan
def tambah_pesanan():
    jenis = var_kopi.get()
    try:
        jumlah = int(entry_jumlah.get())
        if jumlah <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Input Salah", "Jumlah harus angka lebih dari 0")
        return
    harga_satuan = menu_kopi[jenis]
    total = harga_satuan * jumlah
    hasil = f"{jenis} x {jumlah} = Rp{total:,}"
    pesanan.append(total)
    listbox.insert(tk.END, hasil)
    entry_jumlah.delete(0, tk.END)
    update_total()

# Fungsi update total
def update_total():
    total_semua = sum(pesanan)
    label_total.config(text=f"Total: Rp{total_semua:,}")

# Fungsi hapus semua
def hapus_semua():
    pesanan.clear()
    listbox.delete(0, tk.END)
    update_total()

# Tampilan GUI
root = tk.Tk()
root.title("Aplikasi Coffee Shop")
root.geometry("400x450")

tk.Label(root, text="Aplikasi Pemesanan Kopi", font=("Helvetica", 16, "bold")).pack(pady=10)

# FITUR TAMPILAN
# Pilih kopi
tk.Label(root, text="Pilih Jenis Kopi:").pack()
var_kopi = tk.StringVar(root)
var_kopi.set("Espresso")
menu_dropdown = tk.OptionMenu(root, var_kopi, *menu_kopi.keys())
menu_dropdown.pack()

# Input jumlah
tk.Label(root, text="Jumlah Cangkir:").pack()
entry_jumlah = tk.Entry(root)
entry_jumlah.pack()

# Tombol tambah pesanan
tk.Button(root, text="Tambah Pesanan", command=tambah_pesanan).pack(pady=10)

# List hasil pesanan
tk.Label(root, text="Daftar Pesanan:").pack()
listbox = tk.Listbox(root, width=40)
listbox.pack(pady=5)

# Label total
label_total = tk.Label(root, text="Total: Rp0", font=("Arial", 12, "bold"))
label_total.pack(pady=10)

# Tombol hapus semua
tk.Button(root, text="Hapus Semua", command=hapus_semua, bg="red", fg="white").pack()

# Jalankan GUI
root.mainloop()