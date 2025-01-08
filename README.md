# Sepolia ETH Balance Checker 🔍

Script untuk mengecek balance ETH di jaringan Sepolia testnet untuk multiple address sekaligus.

## ⭐ Fitur

- ✅ Mendukung pengecekan multiple address dari private key
- 📝 Menyimpan address dengan balance < 0.1 ETH ke file terpisah
- 🔄 Sistem retry otomatis jika terjadi gangguan RPC
- ⏳ Delay antar pengecekan untuk menghindari rate limiting
- 📊 Menampilkan statistik hasil pengecekan

## 🚀 Cara Penggunaan

### Persiapan

1. Clone repository ini
```bash
git clone https://github.com/Aethereal-Collective/sepolia-balance-checker.git
cd sepolia-balance-checker
```

2. Buat dan aktifkan virtual environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/MacOS
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Buat file `privatekey.txt` dan masukkan private key yang ingin dicek (satu private key per baris)
```
private_key_1
private_key_2
private_key_3
...
```

### Menjalankan Script

```bash
python balance_checker.py
```

## 📋 Output

Script akan menghasilkan:
1. Status koneksi ke Sepolia network
2. Balance untuk setiap address yang dicek
3. Ringkasan total address yang berhasil/gagal dicek
4. File `insufficient_address.txt` berisi daftar address dengan balance < 0.1 ETH

## 📝 License

MIT License - silakan gunakan dan modifikasi sesuai kebutuhan 
