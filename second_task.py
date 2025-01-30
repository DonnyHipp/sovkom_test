import argparse


def calculate_income(
        N: int,
        M: int,
        S: int,
        lots: list[tuple[int, str, float, int]]
) -> tuple[int, list[tuple[int, str, float, int]]]:
    """
    Рассчитывает максимальный доход и список лотов для покупки.
    :param N: Количество дней.
    :param M: Максимальное количество лотов в день.
    :param S: Начальный капитал.
    :param lots: Список лотов (день, название, цена, количество).
    :return: (доход, список купленных лотов).
    """
    lots.sort(key=lambda x: x[0])

    total_income = 0
    purchased_lots = []
    remaining_money = S

    for day in range(1, N + 1):
        daily_lots = [lot for lot in lots if lot[0] == day]

        count = 0
        for lot in daily_lots:
            if count >= M:
                break

            _, name, price, quantity = lot
            total_cost = price * 10 * quantity # сократил / 100 * 1000

            if total_cost <= remaining_money:
                remaining_money -= total_cost
                purchased_lots.append(lot)

                coupons = 30 * quantity
                nominal = 1000 * quantity
                income = coupons + nominal - total_cost
                total_income += income

                count += 1

    return int(total_income), purchased_lots


def test():
    N, M, S = 2, 2, 8000
    lots = [
        (1, "alfa-05", 100.2, 2),
        (2, "alfa-05", 101.5, 5),
        (2, "gazprom-07", 100.0, 2),
    ]
    expected_income = 131 # вот здесь не знаю почему 131, а не 135
    expected_lots = [
        (2, "alfa-05", 101.5, 5),
        (2, "gazprom-07", 100.0, 2),
    ]
    income, purchased_lots = calculate_income(N, M, S, lots)
    assert income == expected_income, f"Ошибка в тесте 1: {income} != {expected_income}"
    assert purchased_lots == expected_lots, f"Ошибка в тесте 1: {purchased_lots} != {expected_lots}"

    print("Все тесты прошли!")


def main():
    N, M, S = map(int, input().split())

    lots = []
    while True:
        line = input().strip()
        if not line:
            break
        day, name, price, quantity = line.split()
        lots.append((int(day), name, float(price), int(quantity)))

    income, purchased_lots = calculate_income(N, M, S, lots)

    print(income)
    for lot in purchased_lots:
        print(f"{lot[0]} {lot[1]} {lot[2]} {lot[3]}")
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--test", action="store_true", help="Тесты")
    args = parser.parse_args()

    if args.test:
        test()
    else:
        main()
