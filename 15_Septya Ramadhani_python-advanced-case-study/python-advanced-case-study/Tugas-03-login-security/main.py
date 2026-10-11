import re
from datetime import datetime

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self): return self.__username

    @username.setter
    def username(self, value):
        if not isinstance(value, str) or not re.fullmatch(r"[A-Za-z0-9]{5,}", value):
            raise ValueError("username harus minimal 5 karakter dan hanya berisi huruf/angka")
        self.__username = value

    @property
    def password(self): return self.__password

    @password.setter
    def password(self, value):
        if not isinstance(value, str) or len(value) < 8:
            raise ValueError("password harus minimal 8 karakter")
        if not re.search(r"\d", value):
            raise ValueError("password harus mengandung minimal satu angka")
        self.__password = value

def audit_log(func):
    def wrapper(username, password):
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            status, alasan = func(username, password)
        except Exception as error:
            status, alasan = "DITOLAK", str(error)
        print(f"[{waktu}] Pengguna: {username!r} | Status: {status}")
        if alasan: print(f"  Alasan: {alasan}")
        return status, alasan
    return wrapper

@audit_log
def login(username, password):
    try: User(username, password)
    except ValueError as error: return "DITOLAK", str(error)
    return "BERHASIL", "format username dan password memenuhi aturan"

if __name__ == "__main__":
    print("=== SIMULASI LOGIN DAN AUDIT LOG ===")
    print("\n1. Username tidak sesuai aturan")
    login("ab!", "rahasia123")
    print("\n2. Password terlalu pendek")
    login("septya01", "abc12")
    print("\n3. Password tidak mengandung angka")
    login("septya02", "rahasiaaa")
    print("\n4. Login berhasil")
    login("septya03", "aman12345")
