def calculate_percentages(shares: list[float]) -> list[float]:
    """Вычисляет процентное выражение долей"""
    if any(share < 0 for share in shares):
        raise ValueError("Все доли должны быть неотрицательными.")
    total = sum(shares)
    return [(share / total) * 100 for share in shares]


def main():
    N = int(input())
    shares = [float(input()) for _ in range(N)]
    percentages = calculate_percentages(shares)
    for p in percentages:
        print(f"{p:.3f}")


def test():
    # Тест 1: Обычный случай
    shares = [1.5, 3, 6, 1.5]
    expected = [12.5, 25.0, 50.0, 12.5]
    result = calculate_percentages(shares)
    assert result == expected


    # Тест 2: Все доли равны
    shares = [1, 1, 1]
    expected = [33.333, 33.333, 33.333]
    result = calculate_percentages(shares)
    assert all(abs(a - b) < 0.001 for a, b in zip(result, expected))


    # Тест 3: Одна доля
    shares = [10]
    expected = [100.0]
    result = calculate_percentages(shares)
    assert result == expected


    # Тест 4: Доли с нулевыми значениями
    shares = [0, 5, 0, 5]
    expected = [0.0, 50.0, 0.0, 50.0]
    result = calculate_percentages(shares)
    assert result == expected


    # Тест 5: Отрицательные доли (некорректный ввод, но функция должна обработать)
    shares = [-1, -2, 4]
    try:
        result = calculate_percentages(shares)
    except ValueError as e:
        assert e.args[0] == "Все доли должны быть неотрицательными."


    # Тест 6: Пустой список (некорректный ввод, но функция должна обработать)
    shares = []
    expected = []
    result = calculate_percentages(shares)
    assert result == expected

    print("Все тесты прошли!")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Вычисление процентного выражения долей.")
    parser.add_argument("--test", action="store_true", help="Тесты")
    args = parser.parse_args()

    if args.test:
        test()
    else:
        main()
