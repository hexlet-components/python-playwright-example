# AGENTS.md

Репозиторий создан из шаблона `hexlet-components/component-template`. Шаблон ставит общий слой проверок из [dev-quality-gates](https://github.com/mokevnin/dev-quality-gates): mise, hk, commitlint, rumdl, typos, lychee, jactionlint и betterleaks. Стек здесь Python с uv, ruff и ty.

## Тесты повторяют уроки курса

Компонент служит образцом проекта для курса «Playwright на Python» (`courses/ru/python_playwright_course` в hexlet-exercise-kit). Page Object, хуки Allure в `tests/conftest.py`, моки табло и API бронирований взяты из уроков почти дословно. Правка кода здесь расходится с уроком, поэтому меняется в паре с курсом.

Тесты ходят на стенд `https://http.hexlet.app/python-playwright` из репозитория `hexlet-components/http-example`. Стенд свой, набор данных на нём не меняется, поэтому тесты гоняются и в CI. Падение теста здесь означает, что разошлись стенд и урок.

## Ссылки Allure

Репозиторий помечен как шаблон GitHub, студент создаёт из него свой через **Use this template**, как в `incident-lab`. README написан для студента. Шапка с вордмарком Хекслета взята из заготовки `component-template`, разделы про копию шаблона и запуск устроены по README `incident-lab`. `pytest.ini` задаёт шаблон `--allure-link-pattern` на Issues этого репозитория, в своей копии студент меняет в нём логин. В самих тестах `@allure.issue` нет: студент в самостоятельной работе заводит баг в своём репозитории и ставит его номер сам.
