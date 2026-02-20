total_profit = 0
total_margin = 0
count = 0

while True:
    buy_price = float(input("Введите цену покупки: "))
    sell_price = float(input("Введите цену продажи: "))
    if sell_price == 0:
        print("Ошибкаб цена продажи не может быть 0")
        continue
    profit = sell_price - buy_price
    margin = (profit/sell_price)*100
    print(f"Прибыль: {profit:.2f} zl")
    print(f"Маржа: {margin:.2f} %")

    if profit < 0:
        print("Внимание: Убыток!!!")

    total_margin += margin
    total_profit += profit
    count += 1

    again = input("Хотите рассчитать еще одну сделку? y/n: ").lower()
    if again == "n":
        break

if count > 0:
    print("\n======== Общая статистика ========")
    print(f"Общее количество сделок : {count}")
    print(f"Общая прибыль: {total_profit:.2f} zl")
    print(f"Средняя маржа: {(total_margin/count):.2f} %")
else:
    print("Сделок не было")
