def generate_header():
    return 'Raport \n' + "="*15 + "\n"

def generate_user_report(users):
    user_report = "Uzytkownicy:\n"
    for user in users:
        user_report += f"- {user.username} ({user.role})\n"
    return user_report

def generte_product_report(shop):
    product_report = "\n Produkty:\n"
    for product in shop.products:
            product_report += f"- {product['name']} (${product['price']})\n"
    return product_report

def generate_shop_balance(shop):
     return f"\nStan finansow: ${shop.balance}\n"


def generate_report(users, shop):
    with open("report.txt", "w") as file:
        file.write(generate_header())
        file.write(generate_user_report(users))
        file.write( generte_product_report(shop))
        file.write(generate_shop_balance(shop))
