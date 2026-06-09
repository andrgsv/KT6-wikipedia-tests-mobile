# Матрица соответствия требований и тестов

| Требование | Описание | Тест-кейсы | Автотесты |
|---|---|---|---|
| REQ-001 | Пользователь может запустить приложение | TC-001 | test_first_launch_can_skip_onboarding |
| REQ-002 | Пользователь может пропустить онбординг | TC-001 | test_first_launch_can_skip_onboarding |
| REQ-003 | Пользователь может выполнить поиск статьи | TC-002 | test_search_article_returns_relevant_results |
| REQ-004 | Пользователь может открыть статью | TC-003 | test_open_article_from_search_results |
| REQ-005 | Приложение не падает при пустом поиске | TC-004 | test_empty_search_field_does_not_crash_app |
| REQ-006 | Пользователь может сохранить статью | TC-005 | test_article_can_be_saved_without_login |
| REQ-007 | Пользователь может открыть настройки | TC-006 | test_open_settings_from_more_menu |
