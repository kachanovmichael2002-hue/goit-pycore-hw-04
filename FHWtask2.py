def get_cats_info(path):
    cats_list = []  # створюємо список для словників

    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()

                if not line:
                    continue

                parts = line.split(',')
                if len(parts) != 3:
                    print(f"Невірний рядок: {line}")
                    continue 
                
                cat_id, name, age = parts  # краще назвати cat_id, щоб не перезаписувати вбудоване id
                cat_dict = {"id": cat_id, "name": name, "age": age}
                cats_list.append(cat_dict)
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

    return cats_list