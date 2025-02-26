import requests
import time
from datetime import datetime

class SubdomainFinder:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.securitytrails.com/v1"
        self.headers = {'apikey': self.api_key}
    
    def find_subdomains(self, domain, children_only=False):
        """Mencari subdomain dengan pagination lengkap"""
        try:
            all_subdomains = []
            page = 1
            total_pages = 1
            
            while page <= total_pages:
                params = {
                    'children_only': str(children_only).lower(),
                    'page': page,
                    'limit': 100
                }
                
                response = requests.get(
                    f"{self.base_url}/domain/{domain}/subdomains",
                    headers=self.headers,
                    params=params
                )
                response.raise_for_status()
                
                data = response.json()
                current_subs = data.get('subdomains', [])
                all_subdomains.extend([f"{sub}.{domain}" for sub in current_subs])
                
                meta = data.get('meta', {})
                total_pages = meta.get('max_page', 1)
                
                print(f"🔍 Memproses halaman {page}/{total_pages}...")
                page += 1
                time.sleep(0.3)
            
            return all_subdomains
            
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return []

def save_to_file(domain, subdomains):
    """Menyimpan hasil ke file"""
    filename = f"results_{domain}.txt"
    with open(filename, 'w') as f:
        f.write("\n".join(subdomains))
    return filename

def print_banner():
    """Menampilkan banner"""
    print("""
                                                       
» Subdomain Finder
» Author: ./KeyzNet
» Contact: t.me/keyznet
    """)

def main():
    API_KEY = "YOUR_API_KEY"
    
    print_banner()
    
    # Validasi API Key
    if len(API_KEY) != 32 or not API_KEY.startswith('ADL'):
        print("\n⚠️  ERROR: Format API key tidak valid!")
        return
    
    finder = SubdomainFinder(API_KEY)
    
    # Input target
    domain = input("\n⌨  Masukkan domain target: ").strip().lower()
    if not domain:
        print("\n⚠️  ERROR: Domain tidak boleh kosong!")
        return
    
    children_only = input("🔘 Cari subdomain langsung saja? (y/n): ").lower() == 'y'
    
    # Proses pencarian
    print("\n🔄 Memulai scanning...")
    try:
        subdomains = finder.find_subdomains(domain, children_only)
        
        if subdomains:
            filename = save_to_file(domain, subdomains)
            print(f"\n✅ Berhasil menemukan {len(subdomains)} subdomain")
            print(f"💾 Hasil tersimpan di: {filename}")
        else:
            print("\n❌ Tidak ditemukan subdomain")
            
    except KeyboardInterrupt:
        print("\n🛑 Operasi dibatalkan oleh pengguna")

if __name__ == "__main__":
    main()