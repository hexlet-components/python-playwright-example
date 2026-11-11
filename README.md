# python-playwright-example

[![CI](https://github.com/hexlet-components/python-playwright-example/actions/workflows/main.yml/badge.svg)](https://github.com/hexlet-components/python-playwright-example/actions/workflows/main.yml)
[![Check](https://github.com/hexlet-components/python-playwright-example/actions/workflows/check.yml/badge.svg)](https://github.com/hexlet-components/python-playwright-example/actions/workflows/check.yml)

Настроенный проект на [Playwright для Python](https://playwright.dev/python/) для курса [Playwright на Python](https://ru.hexlet.io/programs/python-playwright). Тесты проверяют учебное приложение Departures на стенде `https://http.hexlet.app/python-playwright`, тот же, на котором построены уроки. Студент сверяет с этим репозиторием свой проект в самостоятельных работах.

Проект собирает решения из разных уроков курса в одном месте.

- Тесты браузера лежат в `tests/e2e`, тесты API в `tests/api`. Вторые браузер не поднимают и ходят в API бронирований с токеном.
- Page Object для входа и раздела поездок лежит в `tests/pages`.
- Хуки в `tests/conftest.py` прикладывают к отчёту Allure скриншот, видео и трейс упавшего теста.
- `pytest.ini` включает трейсы и видео для упавших тестов и задаёт шаблон ссылок `@allure.issue` на Issues репозитория.
- CI в `.github/workflows/main.yml` прогоняет тесты и сохраняет сырые данные Allure и трейсы артефактами.

## Запуск

```sh
mise run setup
mise run test
mise run report-allure
```

`make <задача>` вызывает ту же задачу mise. Отчёт Allure собирает утилита `allure`, она ставится отдельно, см. [документацию Allure](https://allurereport.org/docs/v2/install/).

## Проверки

`mise run check` гоняет тот же набор, что CI: разметку, опечатки, ссылки, workflows, ruff, ty и уязвимости зависимостей.

---

[![Hexlet Ltd. logo](https://raw.githubusercontent.com/Hexlet/assets/master/images/hexlet_logo128.png)](https://hexlet.io/?utm_source=github&utm_medium=link&utm_campaign=python-playwright-example)

This repository is created and maintained by the team and the community of Hexlet, an educational project. [Read more about Hexlet](https://hexlet.io/pages/about?utm_source=github&utm_medium=link&utm_campaign=python-playwright-example).
