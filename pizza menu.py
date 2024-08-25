import json
import os
import time

BASE_PRICE = 200


def create_pizza(name, ingredients):
    return {
        "name": name,
        "ingredients": ingredients,
        "extra_ingredients": [],
        "price": BASE_PRICE
    }


def add_extra_ingredient(pizza, ingredient):
    pizza["extra_ingredients"].append(ingredient)
    pizza["price"] += 20


def create_order():
    return []


def add_pizza_to_order(order, pizza):
    order.append(pizza)


def calculate_total_price(order):
    total = 0
    for pizza in order:
        total += pizza["price"]
    return total


def create_sales():
    return {}


def add_sale(sales, pizza_name, price):
    if pizza_name in sales:
        sales[pizza_name]['count'] += 1
        sales[pizza_name]['revenue'] += price
    else:
        sales[pizza_name] = {'count': 1, 'revenue': price}


def display_welcome_message():
    print("*******************************")
    print("       PB SOFT uvádí...        ")
    print("*******************************")
    time.sleep(3)
    clear_console()
    print("*******************************")
    print("       Pizza aplikaci          ")
    print("*******************************")
    time.sleep(3)
    clear_console()


def clear_console():
    # Pro Windows
    if os.name == 'nt':
        os.system('cls')
    # Pro Linux a Mac
    else:
        os.system('clear')


def display_menu():
    print("*******************************")
    print("        HLAVNÍ MENU            ")
    print("*******************************")
    print("1 -> Vytvořit objednávku")
    print("2 -> Zaplatit")
    print("3 -> Admin menu")
    print("4 -> Exit")


def display_pizza_menu(pizzas):
    print("*******************************")
    print("        VÝBĚR PIZZY            ")
    print("*******************************")
    print("Vyberte pizzu z menu:")
    for i, pizza in enumerate(pizzas):
        print(f"{i + 1}. {pizza['name']}")
        print(f"   Ingredience: {', '.join(pizza['ingredients'])}")
        print(f"   Cena: {pizza['price']} Kč")
        print("-------------------------------")


def display_extra_ingredients_menu(pizza):
    print(f"Aktuální cena pizzy: {pizza['price']} Kč")
    print("*******************************")
    print("    PŘIDÁNÍ EXTRA PŘÍSAD       ")
    print("*******************************")
    print("1 -> Sýr")
    print("2 -> Vejce")
    print("3 -> Slanina")
    print("4 -> Zelenina")
    print("5 -> Papričky")
    print("6 -> Šunka")
    print("7 -> Salám")
    print("8 -> Ananas")
    print("9 -> Vrátit se do menu")


def display_order_summary(order):
    print("*******************************")
    print("       SOUHRN OBJEDNÁVKY       ")
    print("*******************************")
    for pizza in order:
        extras = f" + {', '.join(pizza['extra_ingredients'])}" if pizza['extra_ingredients'] else ""
        print(f"{pizza['name']} - {', '.join(pizza['ingredients'])}{extras} | Cena: {pizza['price']} Kč")
    print(f"Celková cena: {calculate_total_price(order)} Kč")


def display_payment_methods():
    print("*******************************")
    print("    ZVOLTE PLATEBNÍ METODU     ")
    print("*******************************")
    print("1 -> Kreditní karta")
    print("2 -> Hotovost")


def display_sales(sales):
    print("*******************************")
    print("      STATISTIKA PRODEJE       ")
    print("*******************************")
    print(json.dumps(sales, indent=4))


def prompt_user_input(message):
    return input(message)


def prompt_authorization():
    return input("Zadejte admin heslo: ")


def run():
    display_welcome_message()

    pizzas = [
        create_pizza("ŠUNKA SE ŽAMPIONY", ["sugo", "mozzarella", "šunka", "žampiony"]),
        create_pizza("PARMA", ["sugo", "mozzarella", "prosciutto", "rukola"]),
        create_pizza("SLANINOVÁ", ["sugo", "mozzarella", "slanina", "kukuřice"]),
        create_pizza("COCAIN", ["sugo", "mozzarella", "chorizo", "parmezán", "jalapeňos"]),
        create_pizza("ŽAMPIONOVÁ", ["sugo", "mozzarella", "žampiony"]),
        create_pizza("VEGETARIÁNSKÁ", ["sugo", "mozzarella", "rajčata", "žampiony", "špenát", "kukuřice"]),
        create_pizza("CAPRICCIOSA", ["sugo", "mozzarella", "šunka", "olivy", "artyčoky"]),
        create_pizza("MARGHERITA", ["sugo", "mozzarella", "bazalka"]),
        create_pizza("BALKAN", ["smetana", "mozzarella", "balkánský sýr", "špenát", "kukuřice"]),
        create_pizza("CARTEL", ["sugo", "mozzarella", "šunka", "olivy", "sušená rajčata", "rukola"]),
        create_pizza("SÝROVÁ", ["sugo", "mozzarella", "niva", "olivy"]),
    ]
    order = create_order()
    sales = create_sales()

    while True:
        display_menu()
        choice = prompt_user_input("Vyberte možnost: ")

        if choice == "1":
            create_order_menu(pizzas, order, sales)
        elif choice == "2":
            pay_order(order)
        elif choice == "3":
            admin_menu(sales)
        elif choice == "4":
            print("Děkujeme za použití Pizza App!")
            break
        else:
            print("Neplatná volba, zkuste to znovu.")


def create_order_menu(pizzas, order, sales):
    display_pizza_menu(pizzas)
    pizza_choice = int(prompt_user_input("Zadejte číslo pizzy, kterou chcete vybrat: ")) - 1

    if 0 <= pizza_choice < len(pizzas):
        chosen_pizza = pizzas[pizza_choice]
        while True:
            display_extra_ingredients_menu(chosen_pizza)
            extra_choice = prompt_user_input("Vyberte přísadu (číslo): ")
            if extra_choice == "1":
                add_extra_ingredient(chosen_pizza, "Sýr")
            elif extra_choice == "2":
                add_extra_ingredient(chosen_pizza, "Vejce")
            elif extra_choice == "3":
                add_extra_ingredient(chosen_pizza, "Slanina")
            elif extra_choice == "4":
                add_extra_ingredient(chosen_pizza, "Zelenina")
            elif extra_choice == "5":
                add_extra_ingredient(chosen_pizza, "Papričky")
            elif extra_choice == "6":
                add_extra_ingredient(chosen_pizza, "Šunka")
            elif extra_choice == "7":
                add_extra_ingredient(chosen_pizza, "Salám")
            elif extra_choice == "8":
                add_extra_ingredient(chosen_pizza, "Ananas")
            elif extra_choice == "9":
                break
            else:
                print("Opakujte znova a správně.")
            print(f"Aktuální cena pizzy: {chosen_pizza['price']} Kč")
        add_pizza_to_order(order, chosen_pizza)
        add_sale(sales, chosen_pizza["name"], chosen_pizza["price"])
        print(f"{chosen_pizza['name']} přidána do objednávky.")
    else:
        print("Neplatná volba.")


def pay_order(order):
    display_order_summary(order)
    display_payment_methods()
    payment_method = prompt_user_input("Zvolte platební metodu (číslo): ")

    if payment_method in ["1", "2"]:
        print("Platba úspěšná! Děkujeme za objednávku.")
        order.clear()
    else:
        print("Platba neakceptována. Zkuste znova.")


def admin_menu(sales):
    password = prompt_authorization()
    if password == "admin":
        display_sales(sales)
    else:
        print("Neplatné heslo!")


if __name__ == "__main__":
    run()
