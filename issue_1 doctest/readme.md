## issue-01
Дана функция, кодирующая строку в соответсвии с таблицей азбуки Морзе

```python
# полный код в файле main.py
def encode(message: str) -> str:
    """
    Кодирует строку в соответсвии с таблицей азбуки Морзе
    """
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]
    return ' '.join(encoded_signs)
```

Напишите на неё тесты с использование `doctest`

**DoD (Definition of Done) - критерии, позволяющие понять, что задача сделана, как ожидается**:
* используется директива
* используется флаг
* тест с message = 'SOS'
* тест с исклечением (Exception)
* файл README.md с описанием шагов для запуска
* файл result с командами и результатами запуска
* файл *.py с функцией и доктестами
* нет замечаний от `flake8`

для создания тестов использовался переводчик:
https://morsecode.world/international/translator.html

**ЗАПУСК ТЕСТА**
``` 
python main.py 
```

