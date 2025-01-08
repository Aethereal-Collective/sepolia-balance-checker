# Sepolia ETH Balance Checker 🔍

Script Python sederhana untuk mengecek balance ETH di jaringan Sepolia testnet untuk multiple address sekaligus.

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
git clone <repository-url>
cd <repository-name>
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Buat file `privatekey.txt` dan masukkan private key yang ingin dicek (satu private key per baris)
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

## ⚙️ Konfigurasi

Beberapa parameter yang bisa disesuaikan di `balance_checker.py`:
- `MAX_RETRIES`: Jumlah maksimal percobaan jika terjadi error (default: 3)
- `RETRY_DELAY`: Jeda waktu antar percobaan dalam detik (default: 5)
- RPC URL: Bisa diganti dengan RPC node Sepolia lainnya

## 🔒 Keamanan

- Jangan pernah membagikan private key Anda
- Pastikan file `privatekey.txt` ditambahkan ke `.gitignore`
- Gunakan script ini hanya untuk address testnet

## 🌐 Network

Script ini menggunakan jaringan Sepolia testnet dengan detail:
- Chain ID: 11155111
- Currency: ETH
- Explorer: [sepolia.etherscan.io](https://sepolia.etherscan.io)

## 📝 License

MIT License - silakan gunakan dan modifikasi sesuai kebutuhan 