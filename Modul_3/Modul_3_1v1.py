shopping_dict = {
    "piekarnia": ["chleb", "pączek", "bułki"],
    "warzywniak": ["marchew", "seler",  "rukola"]
}

total = 0

for shop, items in shopping_dict.items():
    shop_items = len(items)  # liczba produktów w sklepie
    total += shop_items
    # brak capitalized() dla listy w princie 
    items_capitalized = [item.capitalize() for item in items]
    print(f"Idę do {shop.capitalize()} i kupuję tutaj następujące rzeczy: {items_capitalized}")
    
print(f"W sumie kupuję {total} produktów")