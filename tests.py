import pytest
import allure
import requests
from superhero_finder import find_tallest_hero

# URL для мокирования API
API_URL = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"

# --- Мок-данные для тестов ---
mock_heroes_data = [
    {
        "id": 1823,
        "name": "Emily Lambert",
        "appearance": {
            "gender": "Female",
            "race": "Alien",
            "height": [
                "549'448",
                "595 cm"
            ],
            "weight": [
                "16 lb",
                "145 kg"
            ],
            "eye_color": "dCUWbtiNmiAikJjwCLUI",
            "hair_color": "FxRmHvLnrNDiEvYpgkVN"
        },
        "work": {
            "occupation": "Detective",
            "base": "Trinidad and Tobago"
        }
    },
    {
        "id": 3705,
        "name": "Jeremiah Moore",
        "appearance": {
            "gender": "Female",
            "race": "Unknown",
            "height": [
                "431'787",
                "84 cm"
            ],
            "weight": [
                "586 lb",
                "49 kg"
            ],
            "eye_color": "RVDEsRbIBNKNGoMiKgyO",
            "hair_color": "DsXrSJzXUUWdlGURsZNH"
        },
        "work": {
            "occupation": "Detective",
            "base": "Sierra Leone"
        }
    },
    {
        "id": 891,
        "name": "Donald Moore",
        "appearance": {
            "gender": "Other",
            "race": "God",
            "height": [
                "346'354",
                "92 cm"
            ],
            "weight": [
                "111 lb",
                "124 kg"
            ],
            "eye_color": "rUnsWVPRYCmJQKTzKJSh",
            "hair_color": "EcBRiaixyzNVgiutECBZ"
        },
        "work": {
            "occupation": "Detective",
            "base": "Barbados"
        }
    },
    {
        "id": 3708,
        "name": "Kristine Kelley",
        "appearance": {
            "gender": "Female",
            "race": "Mutant",
            "height": [
                "858'723",
                "773 cm"
            ],
            "weight": [
                "458 lb",
                "115 kg"
            ],
            "eye_color": "HOHHEJSyHprkzuktVmOm",
            "hair_color": "oCVFCjzUNPktzfQWNVYq"
        },
        "work": {
            "occupation": "Agent",
            "base": "Algeria"
        }
    },
    {
        "id": 3403,
        "name": "Christopher Salas",
        "appearance": {
            "gender": "Female",
            "race": "Demon",
            "height": [
                "151'91",
                "157 cm"
            ],
            "weight": [
                "414 lb",
                "189 kg"
            ],
            "eye_color": "HGPoFJMFrbMiKeWWZetm",
            "hair_color": "cabkSErnxlxsToSnEOMj"
        },
        "work": {
            "occupation": "-",  # Безработная
            "base": "Sierra Leone"
        }
    },
    {
        "id": 6047,
        "name": "Yvette Brown",
        "appearance": {
            "gender": "Male",
            "race": "God",
            "height": [
                "526'723",
                "382 cm"
            ],
            "weight": [
                "90 lb",
                "285 kg"
            ],
            "eye_color": "DMETMoyNfrkjLknZgYcG",
            "hair_color": "nVPxoKasZxAnxBKBzurL"
        },
        "work": {
            "occupation": "-",  # Безработный
            "base": "Pakistan"
        }
    },
    {
        "id": 2383,
        "name": "Nicholas Hubbard",
        "appearance": {
            "gender": "Male",
            "race": "Human",
            "height": [
                "662'625",
                "500 cm"
            ],
            "weight": [
                "293 lb",
                "116 kg"
            ],
            "eye_color": "gqcvOTQPQQTexCnuAofj",
            "hair_color": "ZuXTITkqxDUPenJUDZGh"
        },
        "work": {
            "occupation": "Detective",
            "base": "Bangladesh"
        }
    },
    {
        "id": 4748,
        "name": "Jennifer Robinson",
        "appearance": {
            "gender": "Male",
            "race": "Alien",
            "height": [
                "461'593",
                "44 cm"
            ],
            "weight": [
                "254 lb",
                "181 kg"
            ],
            "eye_color": "YiYjIwCAaetWLFkSmAWq",
            "hair_color": "TxcpTBUCDqCKnoTRKWLB"
        },
        "work": {
            "occupation": "Detective",
            "base": "Yemen"
        }
    },
    {
        "id": 5674,
        "name": "David Martin",
        "appearance": {
            "gender": "Male",
            "race": "Unknown",
            "height": [
                "-",
                "0 cm"  # Некорректный рост
            ],
            "weight": [
                "137 lb",
                "266 kg"
            ],
            "eye_color": "PrWVbqUjFivSHelcmwCV",
            "hair_color": "FxnmGUeRHpMljRidOUIE"
        },
        "work": {
            "occupation": "Vigilante",
            "base": "Isle of Man"
        }
    },
    {
        "id": 7001,
        "name": "William Freeman",
        "appearance": {
            "gender": "Male",
            "race": "God",
            "height": [
                "-",
                "-"  # Полностью некорректный рост
            ],
            "weight": [
                "587 lb",
                "272 kg"
            ],
            "eye_color": "hketzlNSFCFhvhIdbLyt",
            "hair_color": "pHIjTSKwrDrHQJDentPm"
        },
        "work": {
            "occupation": "Detective",
            "base": "Taiwan"
        }
    }
]


@allure.feature("Поиск супергероев")
class TestFindTallestHero:
    """
    Набор тестов для функции find_tallest_hero.
    """

    @pytest.fixture
    def mock_api(self, requests_mock):
        requests_mock.get(API_URL, json=mock_heroes_data)

    @allure.story("Поиск по критериям")
    @allure.title("Найти самого высокого мужчину с работой")
    def test_find_tallest_male_with_job(self, mock_api):
        """
        Тест проверяет поиск самого высокого супергероя мужского пола, у которого есть работа.
        Ожидаемый результат: Nicholas Hubbard (500 cm).
        """
        tallest = find_tallest_hero(gender="Male", has_job=True, api_url=API_URL)
        assert tallest == "Nicholas Hubbard"

    @allure.story("Поиск по критериям")
    @allure.title("Найти самого высокого мужчину без работы")
    def test_find_tallest_male_without_job(self, mock_api):
        """
        Тест проверяет поиск самого высокого безработного супергероя мужского пола.
        Ожидаемый результат: Yvette Brown (382 cm).
        """
        tallest = find_tallest_hero(gender="Male", has_job=False, api_url=API_URL)
        assert tallest == "Yvette Brown"

    @allure.story("Поиск по критериям")
    @allure.title("Найти самую высокую женщину с работой")
    def test_find_tallest_female_with_job(self, mock_api):
        """
        Тест проверяет поиск самой высокой супергероини, у которой есть работа.
        Ожидаемый результат: Kristine Kelley (773 cm).
        """
        tallest = find_tallest_hero(gender="Female", has_job=True, api_url=API_URL)
        assert tallest == "Kristine Kelley"

    @allure.story("Поиск по критериям")
    @allure.title("Найти самую высокую женщину без работы")
    def test_find_tallest_female_without_job(self, mock_api):
        """
        Тест проверяет поиск самой высокой безработной супергероини.
        Ожидаемый результат: Christopher Salas (157 cm).
        """
        tallest = find_tallest_hero(gender="Female", has_job=False, api_url=API_URL)
        assert tallest == "Christopher Salas"

    @allure.story("Граничные случаи")
    @allure.title("Герой не найден, если пол не соответствует")
    def test_no_hero_found_for_gender(self, mock_api):
        """
        Тест проверяет, что функция возвращает None, если нет героев указанного пола.
        """
        # В мок-данных нет героев с гендером 'Unknown'
        tallest = find_tallest_hero(gender="Unknown", has_job=True, api_url=API_URL)
        assert tallest is None

    @allure.story("Граничные случаи")
    @allure.title("Герой не найден, если статус работы не соответствует")
    def test_no_hero_found_for_job_status(self, mock_api):
        """
        Тест проверяет, что функция возвращает None, если нет героев с указанным статусом работы.
        В данном случае, ищем безработных героев с гендером '-', которых нет в данных.
        """
        tallest = find_tallest_hero(gender="-", has_job=False, api_url=API_URL)
        assert tallest is None

    @allure.story("Обработка ошибок API")
    @allure.title("Обработка ошибки сервера API (статус 500)")
    def test_api_server_error(self, requests_mock):
        """
        Тест проверяет, что функция возвращает None при ошибке сервера (статус 500).
        """
        requests_mock.get(API_URL, status_code=500)
        tallest = find_tallest_hero(gender="Male", has_job=True, api_url=API_URL)
        assert tallest is None

    @allure.story("Обработка ошибок API")
    @allure.title("Обработка ошибки сети (timeout)")
    def test_api_network_error(self, requests_mock):
        """
        Тест проверяет, что функция возвращает None при сетевой ошибке (например, таймаут).
        """
        requests_mock.get(API_URL, exc=requests.exceptions.Timeout)
        tallest = find_tallest_hero(gender="Male", has_job=True, api_url=API_URL)
        assert tallest is None

    @allure.story("Граничные случаи")
    @allure.title("Обработка пустого ответа от API")
    def test_empty_api_response(self, requests_mock):
        """
        Тест проверяет, что функция возвращает None, если API возвращает пустой список.
        """
        requests_mock.get(API_URL, json=[])
        tallest = find_tallest_hero(gender="Male", has_job=True, api_url=API_URL)
        assert tallest is None

    @allure.story("Обработка некорректных данных")
    @allure.title("Игнорирование героев с некорректными данными о росте")
    def test_hero_with_invalid_height_data(self, mock_api):
        """
        Тест проверяет, что герои с некорректными или отсутствующими данными о росте
        (например, '0 cm' или '-') корректно игнорируются.
        Самый высокий работающий мужчина после исключения некорректных - Nicholas Hubbard.
        """
        tallest = find_tallest_hero(gender="Male", has_job=True, api_url=API_URL)
        assert tallest == "Nicholas Hubbard"  # Blue Beetle (0 cm) и Invalid Height Hero (-) игнорируются

    @allure.story("Поиск по критериям")
    @allure.title("Проверка независимости от регистра для параметра 'gender'")
    def test_case_insensitivity_for_gender(self, mock_api):
        """
        Тест проверяет, что поиск по полу нечувствителен к регистру.
        'male' должен дать тот же результат, что и 'Male'.
        """
        tallest_lower = find_tallest_hero(gender="male", has_job=True, api_url=API_URL)
        tallest_upper = find_tallest_hero(gender="MALE", has_job=True, api_url=API_URL)
        assert tallest_lower == "Nicholas Hubbard"
        assert tallest_upper == "Nicholas Hubbard"
        assert tallest_lower == tallest_upper

    @allure.story("Обработка некорректных данных")
    @allure.title("Игнорирование героя без информации о росте")
    def test_hero_with_no_height_is_ignored(self, requests_mock):
        """
        Тест проверяет, что герой, у которого полностью отсутствует ключ 'height', игнорируется.
        """
        hero_without_height = {
            "id": 0,
            "name": "Heightless Man",
            "appearance": {"gender": "Male"},  # Нет ключа 'height'
            "work": {"occupation": "Worker"}
        }
        data = mock_heroes_data + [hero_without_height]
        requests_mock.get(API_URL, json=data)
        tallest = find_tallest_hero(gender="Male", has_job=True, api_url=API_URL)
        # Результат не должен измениться, Heightless Man игнорируется
        assert tallest == "Nicholas Hubbard"
