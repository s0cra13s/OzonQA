import requests


def parse_height_cm(height_list):
    """
    Извлекает рост в сантиметрах из списка строк.
    Пример ввода: ["5'10", "178 cm"]
    Возвращает: 178
    """
    for item in height_list:
        if 'cm' in item:
            try:
                # Убираем "cm" и преобразуем в число
                return int(item.replace(' cm', '').strip())
            except (ValueError, TypeError):
                # Если значение не может быть преобразовано, пропускаем его
                return 0
    return 0


def has_meaningful_occupation(occupation):
    """
    Проверяет, является ли род занятий осмысленным.
    "-" считается отсутствием работы.
    """
    if not occupation or occupation.strip() in '-':
        return False
    return True


def find_tallest_hero(gender, has_job, api_url):
    """
    Находит самого высокого супергероя по заданным критериям.

    Args:
        gender (str): Пол для фильтрации ('Male', 'Female'). Регистр не учитывается.
        has_job (bool): True, если герой должен иметь работу, False в противном случае.
        api_url (str): Ссылка на superhero API '/all.json'.

    Returns:
        str: Имя самого высокого героя, соответствующего критериям.
        None: Если герои не найдены или произошла ошибка.
    """
    try:
        response = requests.get(api_url, timeout=10)
        # Проверяем, что запрос успешен
        response.raise_for_status()
        all_heroes = response.json()
    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"Error getting data from API: {e}")
        return None

    tallest_hero_so_far = None
    max_height_so_far = 0

    for hero in all_heroes:
        # --- Проверка критериев ---
        # 1. Проверка пола (без учета регистра)
        hero_gender = hero.get('appearance', {}).get('gender', 'N/A')
        if not hero_gender or hero_gender.lower() != gender.lower():
            continue

        # 2. Проверка наличия работы
        occupation = hero.get('work', {}).get('occupation', '-')
        hero_has_job = has_meaningful_occupation(occupation)
        if hero_has_job != has_job:
            continue

        # --- Поиск самого высокого ---
        height_cm = parse_height_cm(hero.get('appearance', {}).get('height', []))

        if height_cm > max_height_so_far:
            max_height_so_far = height_cm
            tallest_hero_so_far = hero.get('name')

    return tallest_hero_so_far


print(find_tallest_hero("Female", False, "https://cdn.jsdelvr.net/gh/akabab/superhero-api@0.3.0/api/all.json"))
