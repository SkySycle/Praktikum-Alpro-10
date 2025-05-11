filename = input("Masukkan nama file : ")

try:
    with open(filename, 'r') as file:
        email_count = dict()
        for line in file:
            if line.startswith("From "):
                parts = line.split()
                if len(parts) > 1:
                    email = parts[1]
                    email_count[email] = email_count.get(email, 0) + 1
        print(email_count)
except FileNotFoundError:
    print("File tidak ditemukan.")
