# Fantasy Item Shop - Week 1
print("Welcome to the Fantasy Item Shop!")

player_name = input("What is your name? ")
player_gold = 100
inventory = []

# De winkelvoorraad: namen en prijzen staan in twee lists.
item_names = ["Sword", "Shield", "Potion", "Bow"]
item_prices = [50, 40, 20, 60]

print(f"\nHello {player_name}! You have {player_gold} gold.")

while True:
    print("\n=== Fantasy Item Shop ===")
    print()

    # Laat alle items uit de winkel zien met een for-loop.
    for index, item_name in enumerate(item_names):
        print(f"{index + 1}. Buy {item_name} ({item_prices[index]} gold)")

    print("5. View Inventory")
    print("6. Exit Shop")

    choice = input("\nWhat would you like to do? ").strip()

    match choice:
        case "1" | "2" | "3" | "4":
            item_index = int(choice) - 1
            item_name = item_names[item_index]
            item_price = item_prices[item_index]

            if player_gold >= item_price:
                player_gold -= item_price
                inventory.append(item_name)
                print(f"\nYou bought a {item_name}!")
                print(f"Remaining gold: {player_gold}")
            else:
                print("\nYou don't have enough gold!")
        case "5":
            if len(inventory) == 0:
                print("\nYour inventory is empty!")
            else:
                print("\nYour inventory:")
                for item in inventory:
                    print(f"- {item}")
        case "6":
            print(f"\nThanks for visiting, {player_name}!")
            print(f"You have {player_gold} gold left.")
            break
        case _:
            print("\nInvalid option! Please choose a number from 1 to 6.")
