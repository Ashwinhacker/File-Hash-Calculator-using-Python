import hashlib

def calculate_hashes(file_path):
    hashes = {
        'MD5': hashlib.md5(),
        'SHA1': hashlib.sha1(),
        'SHA256': hashlib.sha256(),
        'SHA512': hashlib.sha512()
    }

    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                for h in hashes.values():
                    h.update(chunk)

        print("\n Hash Values for:", file_path)
        for name, h in hashes.items():
            print(f"{name}: {h.hexdigest()}")

    except FileNotFoundError:
        print("❌ File not found. Please check the file path and try again.")

# Ask user for image file path
file_path = input("Enter the image file path: ")
calculate_hashes(file_path)
