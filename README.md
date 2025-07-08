```
pip install -r .\requirements.txt
```

Запустить тесты
```
pytest .\tests.py --alluredir=allure-results
```
Сгенерировать и открыть отчет Allure
```
allure serve allure-results
```
Сама функция в superhero_finder.py
