Настроенный проект с тестами на Playwright для Python к курсу [Playwright на Python](https://ru.hexlet.io/programs/python-playwright). Тесты проверяют учебное приложение Departures на стенде `https://http.hexlet.app/python-playwright`, на котором построены уроки курса. Проект собирает в одном месте решения из разных уроков, поэтому с ним удобно сверять свой проект в самостоятельных работах.

## Свой репозиторий из шаблона

Нажмите **Use this template → Create a new repository**. Выберите свой аккаунт GitHub и назовите репозиторий `python-playwright-example`. Создайте репозиторий и клонируйте его. В Settings → General → Features проверьте, что Issues включены. В Actions разрешите запуск workflows.

Баги, найденные тестами, заводите в Issues своего репозитория. Чтобы отчёт Allure вёл туда, замените в _pytest.ini_ `hexlet-components` своим логином в шаблоне `--allure-link-pattern`. После этого номер в `@allure.issue("1")` превращается в ссылку на первый issue вашего репозитория.

## Запуск

Потребуются [mise](https://mise.jdx.dev/) и `make`. Python, uv и браузер mise ставит сам.

```sh
mise install
make setup
make test
```

Тесты ходят на стенд в интернете, своё приложение поднимать не нужно. Упавший тест оставляет в каталоге _test-results/_ трейс и видео. Трейс открывается командой `uv run playwright show-trace <путь к trace.zip>`.

Отчёт Allure собирается из каталога _allure-results/_. Утилита `allure` ставится отдельно по [инструкции Allure](https://allurereport.org/docs/v2/install/).

```sh
make report-allure
```

## Что где лежит

| Путь | Содержимое |
| --- | --- |
| tests/e2e | Тесты через браузер: вход, ошибки входа, табло и подмена его API |
| tests/api | Тесты API бронирований с токеном, браузер не поднимается |
| tests/pages | Page Object страницы входа и раздела поездок |
| tests/conftest.py | Хуки, которые прикладывают к отчёту Allure скриншот, видео и трейс упавшего теста |
| pytest.ini | Трейсы и видео упавших тестов, каталог данных Allure, шаблон ссылок на Issues |
| .github/workflows/main.yml | Прогон тестов в CI, данные Allure и трейсы сохраняются артефактами |

## Проверки и разработка

`make check` гоняет тот же набор, что CI: ruff, ty, разметку, опечатки, ссылки, workflows и уязвимости зависимостей. `make fix` применяет автоисправления.

## Лицензия

MIT.
