import random

"""2.1"""
def get_room_description():
    rooms = ["Сырой подвал",
             "Тронный зал",
             "Цветущий сад",
             "Тёмные коридоры"]
    get_room = random.choice(rooms)
    return get_room


"""2.2"""
def get_random_event():
    events = [1, 2, 3, 4]
    get_event = random.choice(events)
    return get_event

"""2.3"""
def open_chest(player):
    results = [1, 2]
    get_result = random.choice(results)
    if get_result == 1:
        player['gold'] += random.randint(10, 30)
        return player['gold']
    else:
        player['attack'] *= 2
        print("Вы нашли новый мечь!")
        return player['attack']

"""2.4"""
def trigger_trap(player):
    print("Перед вами рычаг. Нажать? (1 - Да, 2 - Нет)")
    choice = input()
    if choice == 1:
        results = [1, 2]
        get_result = random.choice(results)
        if get_result == 1:
            player['hp'] -= 10
            return player['hp']
        else:
            player['gold'] += 20
            return player['gold']
        
"""2.5"""
def print_status(player, current_level):
    print("============================================")
    print(f"Здоровье: {player['max_hp']}/{player['hp']}")
    print(f"Атака: {player['attack']}")
    print(f"Золото: {player['gold']}")
    print(f"Комната: {current_level}")
    print("============================================")

"""2.6"""
def get_shop_items():
    shop_items = {"Зелье": 15, "Заточка оружия": 30} #Можно добавить новые позиции магазина.
    return shop_items

"""2.7"""
def buy_item(player, item_name, price):
    if player['gold'] >= price:
        player['gold'] -= price
        if item_name == "Зелье":
            player['hp'] += 25 #Значение можно изменить, или использовать player['hp'] = player['max_hp']. На усмотрение.
            print("Здоровье востановленно!")
        elif item_name == "Заточка оружия":
            player['attack'] += 10 #Значение можно изменить, или использовать player['attack'] *= 2. На усмотрение.
            print("Атака увеличина!")
    else:
        print("Недостаточно золота!")

"""2.8"""
def level_up(player):
    player['max_hp'] += 15
    player['hp'] = player['max_hp']
    player['attack'] += 3
    print("Вы повысили свой уровень!")