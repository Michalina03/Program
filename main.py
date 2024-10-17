import json
from admin import Admin
from employee import Employee
from importer import Importer
from shop import Shop
from report import generate_report

def load_data():
    try:
        with open("./data.json", "r") as file:
            return json.load(file)
    except:
        print("nieładuje pliku")

def save_json(data):
    with open("./data.json", "w") as file:
        json.dump(data, file, indent=4)

def find_user(users, username, password):
    for user in users:
        if user.username == username and user.password == password:
            return user
    return

def get_valid_choice(options):
    while True:
        try:
            choice = int(input("Wybierz opcję: "))
            if choice in options:
                return choice
            else:
                print(f"Proszę wybrać jedną z dostępnych opcji: {options}")
        except ValueError:
            print("Niepoprawny wybór, proszę podać liczbę.")

def create_user(user_data):
    if user_data['role'] == 'Admin':
        return Admin(user_data['username'], user_data['password'], user_data['role'])
    elif user_data['role'] == 'Employee':
        return Employee(user_data['username'], user_data['password'], user_data['role'])
    elif user_data['role'] == 'Importer':
        return Importer(user_data['username'], user_data['password'], user_data['role'])


def create_shop(shop_data):
    return Shop(shop_data)

data = load_data()
users = [create_user(user) for user in data['users']]
shop = create_shop(data['shop'])

print("Logowanie do systemu:")
username = input("Podaj nazwę użytkownika: ")
password = input("Podaj hasło: ")

user = find_user(users, username, password)

if not user:
    print("Błędny login lub hasło.")
else:
    print(f"Witaj, {user.username}!")
    
    while True:
        if isinstance(user, Admin):
            print("1. Zarządzaj użytkownikami")
            print("2. Zarządzaj sklepem")
            print("3. Wyjdź")
            choice = get_valid_choice([1, 2, 3])
            if choice == 1:
                user.admin_function(users, data)
            elif choice == 2:
                shop.admin_shop()
            elif choice == 3:
                break

        elif isinstance(user, Employee):
            print("Sprzedaj produkt")
            shop.employee_shop(user)
            print("1. Kontynuuj sprzedaż")
            print("2. Wyjdź")
            choice = get_valid_choice([1, 2])
            if choice == 2:
                break

        elif isinstance(user, Importer):
            print("Sprowadz produkt")
            shop.importer_shop(user)
            print("1. Kontynuuj import")
            print("2. Wyjdź")
            choice = get_valid_choice([1, 2])
            if choice == 2:
                break

    save_json({"users": [u.to_dictionary() for u in users], "shop": shop.to_dictionary()})
    generate_report(users, shop)
