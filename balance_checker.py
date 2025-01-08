from web3 import Web3
import os
import time
from web3.exceptions import TransactionNotFound, BlockNotFound, InvalidAddress, ContractLogicError

# Inisialisasi koneksi ke Sepolia
rpc_url = "https://1rpc.io/sepolia"
w3 = Web3(Web3.HTTPProvider(rpc_url))

# Konfigurasi retry
MAX_RETRIES = 3
RETRY_DELAY = 5

def check_connection():
    for attempt in range(MAX_RETRIES):
        try:
            if w3.is_connected():
                print("✅ Terhubung ke Sepolia Network")
                return True
            else:
                raise Exception("Tidak dapat terhubung ke network")
        except Exception as e:
            if attempt < MAX_RETRIES - 1:
                print(f"❌ Percobaan {attempt + 1} gagal: {str(e)}")
                print(f"⏳ Mencoba kembali dalam {RETRY_DELAY} detik...")
                time.sleep(RETRY_DELAY)
            else:
                print("❌ Gagal terhubung ke network setelah beberapa percobaan")
                return False

def read_private_keys():
    try:
        with open('privatekey.txt', 'r') as file:
            # Membaca setiap baris dan menghapus whitespace
            private_keys = [line.strip() for line in file if line.strip()]
        return private_keys
    except FileNotFoundError:
        print("❌ File privatekey.txt tidak ditemukan")
        return []
    except Exception as e:
        print(f"❌ Error saat membaca file: {str(e)}")
        return []

def get_balance(private_key):
    for attempt in range(MAX_RETRIES):
        try:
            account = w3.eth.account.from_key(private_key)
            balance_wei = w3.eth.get_balance(account.address)
            balance_eth = w3.from_wei(balance_wei, 'ether')
            return account.address, float(balance_eth)
        except (TransactionNotFound, BlockNotFound, InvalidAddress, ContractLogicError) as e:
            print(f"❌ Error Web3: {str(e)}")
            return None, None
        except Exception as e:
            if attempt < MAX_RETRIES - 1:
                print(f"❌ Percobaan {attempt + 1} gagal: {str(e)}")
                print(f"⏳ Mencoba kembali dalam {RETRY_DELAY} detik...")
                time.sleep(RETRY_DELAY)
            else:
                print(f"❌ Gagal setelah {MAX_RETRIES} percobaan: {str(e)}")
                return None, None

def main():
    if not check_connection():
        return

    private_keys = read_private_keys()
    if not private_keys:
        return

    insufficient_addresses = []
    total_checked = 0
    failed_checks = 0
    print("\n🔍 Mengecek balance...\n")

    for i, pk in enumerate(private_keys, 1):
        address, balance = get_balance(pk)
        if address and balance is not None:
            total_checked += 1
            print(f"Address: {address}")
            print(f"Balance: {balance:.6f} ETH")
            print("-" * 50)
            
            if balance < 0.1:
                insufficient_addresses.append(address)
        else:
            failed_checks += 1
        
        # Tambahkan delay 3 detik jika bukan address terakhir
        if i < len(private_keys):
            print("⏳ Menunggu 3 detik...\n")
            time.sleep(3)

    # Tampilkan ringkasan
    print("\n📊 Ringkasan:")
    print(f"Total address dicek: {total_checked}")
    print(f"Gagal dicek: {failed_checks}")

    # Menyimpan address dengan balance kurang dari 0.1 ETH
    if insufficient_addresses:
        with open('insufficient_address.txt', 'w') as file:
            for address in insufficient_addresses:
                file.write(f"{address}\n")
        print(f"\n✅ {len(insufficient_addresses)} address dengan balance < 0.1 ETH telah disimpan ke insufficient_address.txt")
    else:
        print("\n✅ Semua address yang berhasil dicek memiliki balance >= 0.1 ETH")

if __name__ == "__main__":
    main() 