# КТ №6. Тестирование функционала мобильного приложения Wikipedia

Учебный проект по теме **«Тестирование функционала мобильного приложения и составление тестовой документации»**.

В качестве объекта тестирования выбрано обычное реальное Android-приложение **Wikipedia** от Wikimedia Foundation.

## Почему выбрано это приложение

Wikipedia подходит для учебного мобильного тестирования, потому что:

- приложение доступно на Android;
- не требуется регистрация нового аккаунта;
- нет реальных платежей и транзакций;
- есть понятная функциональность: запуск приложения, поиск, открытие статьи, сохранение статьи, навигация, настройки;
- приложение можно запускать на эмуляторе или реальном Android-устройстве через Appium.

## Структура проекта

```text
wikipedia_appium_tests_KT6/
├── docs/
│   ├── appium_setup_windows_linux.md
│   ├── checklist.md
│   ├── defect_reports.md
│   ├── jira_cards.md
│   ├── mobile_platform_specifics.md
│   ├── test_cases.md
│   ├── test_plan.md
│   ├── test_report.md
│   ├── traceability_matrix.md
│   ├── KT6_report_Wikipedia.docx
│   └── KT6_report_Wikipedia.pdf
├── pages/
│   ├── article_page.py
│   ├── base_page.py
│   ├── main_page.py
│   ├── navigation_page.py
│   ├── onboarding_page.py
│   └── search_page.py
├── tests/
│   ├── test_article.py
│   ├── test_navigation.py
│   ├── test_onboarding.py
│   └── test_search.py
├── capabilities.example.json
├── conftest.py
├── pytest.ini
├── README.md
└── requirements.txt
```

## Что проверяется

1. Запуск приложения и пропуск онбординга.
2. Поиск статьи.
3. Открытие статьи из результатов поиска.
4. Проверка поведения при пустом поиске.
5. Сохранение статьи без регистрации.
6. Переход в настройки через нижнюю навигацию.

## Что не тестируется

В проекте специально не проверяются:

- регистрация нового аккаунта;
- вход в личный аккаунт;
- ввод персональных данных;
- платежи и покупки.

## Подготовка окружения

### 1. Установить Python-зависимости

```bash
pip install -r requirements.txt
```

### 2. Установить Appium

```bash
npm install -g appium
appium driver install uiautomator2
```

### 3. Подготовить Android

- Установить Android Studio и Android SDK.
- Настроить переменную `ANDROID_HOME`.
- Добавить в `PATH`:
  - `%ANDROID_HOME%\platform-tools` для Windows;
  - `$ANDROID_HOME/platform-tools` для Linux.
- Запустить Android-эмулятор или подключить реальный телефон.
- Проверить устройство командой:

```bash
adb devices
```

### 4. Установить приложение Wikipedia

Установить приложение **Wikipedia** из Google Play на эмулятор или реальное Android-устройство.

Пакет приложения в capabilities:

```json
"appium:appPackage": "org.wikipedia"
```

## Запуск Appium Server

```bash
appium
```

По умолчанию тесты используют адрес:

```text
http://127.0.0.1:4723
```

## Запуск тестов

```bash
pytest
```

Запуск только smoke-тестов:

```bash
pytest -m smoke
```

Запуск функциональных тестов:

```bash
pytest -m functional
```

## Настройка capabilities

Пример находится в файле `capabilities.example.json`.

При необходимости можно создать свой JSON-файл и передать путь через переменную окружения:

### Windows PowerShell

```powershell
$env:APPIUM_CAPS_FILE="C:\path\to\capabilities.json"
pytest
```

### Linux/macOS

```bash
APPIUM_CAPS_FILE=/path/to/capabilities.json pytest
```

## Примечание

Локаторы мобильного приложения могут изменяться после обновления Wikipedia. Если приложение обновилось и тесты перестали находить элементы, нужно проверить актуальные `resource-id` через Appium Inspector.
