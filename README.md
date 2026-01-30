### Pytest seleniums
#### Установка и запуск через Docker (headless):
```
docker compose up --build
```

#### Локальная установка:
>Требования:
    ( **python 3.10+**, **pip**, **GoogleChrome** )

linux:
```
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
```
Windows(PowerShell): (not tested)
```
    python -m venv .venv
    PS C:\> .venv\Scripts\Activate.ps1
    pip install -r requirements.txt
```

Запуск:
```
pytest --alluredir=allure-results
```

***
### (Опционально) Allure
#### Локальная установка:

>Требования:
    ( **node**, **java** )
    
Установка:
```
npm install
```

Запуск:
```
npx allure serve allure-results
```
