filename = input("Masukkan nama file: ")

try:
    with open(filename, 'r') as file:
        domain_count = dict()
        for line in file:
            if line.startswith("From "):
                parts = line.split()
                if len(parts) > 1:
                    email = parts[1]
                    domain = email.split('@')[-1]
                    domain_count[domain] = domain_count.get(domain, 0) + 1
        print(domain_count)
except FileNotFoundError:
    print("File tidak ditemukan.")
