def total_salary(file):
    total = 0
    count = 0

    try:
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()

                if not line:
                    continue

                parts = line.split(',')

                if len(parts) != 2:
                    print(f"Невірний рядок: {line}")
                    continue

                salary = int(parts[1])

                total += salary
                count += 1

        if count == 0:
            return (0, 0)

        average = total / count
        return (total, average)

    except FileNotFoundError:
        print("Файл не знайдено")
        return (0, 0)
    except ValueError:
        print("Помилка в даних файлу")
        return (0, 0)