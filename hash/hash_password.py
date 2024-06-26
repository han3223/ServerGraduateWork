import hashlib


class HashPassword:
    @staticmethod
    def hash_password(password: str) -> str:
        try:
            # Используем SHA-256 для хэширования пароля
            hashed_bytes = hashlib.sha256(password.encode()).digest()

            # Преобразуем массив байтов в формат шестнадцатеричной строки
            hashed_password = ''.join(format(byte, '02x') for byte in hashed_bytes)

            return hashed_password
        except Exception as e:
            print(f"Error while hashing password: {e}")
            return ""
