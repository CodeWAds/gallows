def get_categories_and_count(file_path):
    categories = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        current_category = None
        for line in lines:
            if line.strip():  # Проверяем, не является ли строка пустой
                if not current_category:  # Если текущая категория не установлена, значит это начало новой категории
                    current_category = line.strip()
                    categories[current_category] = []
                else:
                    # Если текущая категория уже установлена, значит это слова внутри текущей категории
                    splt = line.strip().split("-")
                    categories[current_category].append((splt[0], splt[1]))
            else:  # Если строка пустая, значит это разделитель между категориями
                current_category = None  # Сбрасываем текущую категорию
    return categories, len(categories)


# Замените 'categories.txt' на путь к вашему текстовому файлу
file_path = './src/config/dictionary.txt'
categories, count = get_categories_and_count(file_path)
print("Названия категорий:", categories)
print("Количество категорий:", count)

