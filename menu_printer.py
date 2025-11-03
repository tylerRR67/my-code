#!/usr/bin/env python3
"""
menu_printer.py
Prints a formatted restaurant menu to the terminal.
"""

def print_menu():
    name = "The Rusty Spoon"
    address = "123 Main St. — Open 11:00 - 22:00"

    items = {
        "Starters": [
            ("Bruschetta", "Tomato, basil, garlic on toasted bread", 6.50),
            ("Soup of the Day", "Chef's choice with fresh herbs", 5.00),
            ("Calamari", "Lightly fried, served with aioli", 8.25),
        ],
        "Main Courses": [
            ("Grilled Salmon", "Lemon butter, seasonal veg", 18.00),
            ("Ribeye Steak", "10oz, garlic butter, fries", 22.50),
            ("Pasta Primavera", "Fresh vegetables, parmesan", 14.00),
        ],
        "Desserts": [
            ("Cheesecake", "Classic NY style", 6.00),
            ("Chocolate Lava Cake", "With vanilla ice cream", 6.75),
            ("Fruit Sorbet", "Seasonal selection", 5.50),
        ],
        "Drinks": [
            ("Soda", "Coke / Sprite / Fanta", 2.50),
            ("House Wine", "Red or White, glass", 7.00),
            ("Coffee", "Espresso or Americano", 3.00),
        ],
    }

    # Print header
    print("+" + "="*46 + "+")
    print(f"| {name:^44} |")
    print(f"| {address:^44} |")
    print("+" + "="*46 + "+")
    print()

    # Print sections
    for section, entries in items.items():
        print(f"{section}")
        print('-' * len(section))
        # Name (max 20), description (max 28), price (right-aligned)
        for name_item, desc, price in entries:
            name_fmt = name_item.ljust(20)[:20]
            desc_fmt = desc.ljust(28)[:28]
            price_fmt = f"${price:5.2f}"
            print(f" {name_fmt}  {desc_fmt}  {price_fmt}")
        print()

    print("We accept cash and cards. Thank you for dining with us!")


if __name__ == '__main__':
    print_menu()
