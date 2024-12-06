# Flask Course

## Description

Just doing a Flask refresher project since a lot has changed since I last used it.

## Rebuild after adding new dependencies

```shell
docker build . -t rest-apis-flask-python
```

## Run temporary development server

```shell
docker run --rm -p 5000:5000 -w /app -v "$(pwd):/app" rest-apis-flask-python
```

## Force rebuild

```shell
docker compose up --build --force-recreate --no-deps web
```

## Add a package

```shell
uv add <package-name>
uv pip freeze > requirements.txt
```
