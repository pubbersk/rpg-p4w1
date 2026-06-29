"""3.1"""
import combat
import world


"""3.2"""
def main():
    print("============================================")
    print("ДОБРО ПОЖАЛОВАТЬ В ИГРУ")
    print("ПОДЗЕМЕЛЬЕ PYTHON")
    print("============================================")

    player_name = input("Введите имя вашего героя: ").strip()

    if not player_name:
        player_name = "Безымянный Герой"
    
    print(f"\nПриветствуем тебя, рыцарь {player_name}! Твой путь начинается.")
    player = combat.create_player()


    """3.3"""
    is_running = True
    room_counter = 1
    player_level = 1


    """3.4"""
    while is_running:
        world.print_status(player, room_counter)

        print(f"Вы входите в новую локацию: {world.get_room_description()}")

        """3.6"""
        if room_counter > 1 and room_counter % 5 == 0:
            player = world.level_up()
            player_level += 1
            input("Нажмите Enter, чтобы продолжить...")


        """3.7"""
        if room_counter == 20:
            print("\n🔥 ВНИМАНИЕ! Пол подземелья содрогается... Перед вами ФИНАЛЬНЫЙ БОСС! 🔥")
            boss = {
                'name': "Древний Дракон Питон",
                'hp': 200,
                'attack': 25,
                'gold': 500
            }
            combat.start_battle(player, boss)
            
            # Проверка финала игры
            if combat.check_battle_result(player, boss):
                print("\n🏆🏆🏆 ПОЗДРАВЛЯЕМ! Вы победили Древнего Дракона и прошли игру! 🏆🏆🏆")
            else:
                print("\n💀 Дракон испепелил вас у самого финала...")
                print(f"Итоговая статистика: собрано золота: {player['gold']}, пройдено комнат: {room_counter}.")
            is_running = False
            break

        """3.5"""
        event = world.get_random_event()
        
        if event == 1:
            # Событие: Монстр
            monster = combat.make_monster(player_level)
            combat.start_battle(player, monster)
            
            # Задача 3.8: Обработка Game Over в случае поражения
            if not combat.check_battle_result(player, monster):
                print(f"\nИтоговая статистика: собрано золота: {player['gold']}, пройдено комнат: {room_counter}.")
                is_running = False
                break
                
        elif event == 2:
            # Событие: Торговец
            print("\n🧙 Вы встретили бродячего торговца!")
            shop_items = world.get_shop_items()
            
            print("Доступные товары:")
            for item, price in shop_items.items():
                print(f"- {item}: {price} золота")
                
            buy_choice = input("Что хотите купить? (Зелье / Заточка / Ничего): ").strip().lower()
            if buy_choice in ["зелье", "potion"]:
                world.buy_item(player, "Зелье", shop_items["Зелье"])
            elif buy_choice in ["заточка", "заточка оружия"]:
                world.buy_item(player, "Заточка оружия", shop_items["Заточка оружия"])
            else:
                print("Вы решили ничего не покупать.")
                
        elif event == 3:
            # Событие: Сундук
            player = world.open_chest(player)
            
        elif event == 4:
            # Событие: Пустая комната / Ловушка
            player = world.trigger_trap(player)
            # Если игрок погиб на ловушке
            if player['hp'] <= 0:
                print("\n💀 Вы погибли от ран, полученных в ловушке...")
                print(f"Итоговая статистика: собрано золота: {player['gold']}, пройдено комнат: {room_counter}.")
                is_running = False
                break

        # Переход к следующей комнате
        room_counter += 1
        if is_running:
            input("\nНажмите Enter, чтобы сделать следующий шаг...")

    print("\nСпасибо за игру!")


if __name__ == "__main__":
    main()


