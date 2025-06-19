# fastapi-backend

## Clone the repo
```bash
cd ~/path_to_dir/

git clone https://github.com/user/fastapi-backend
``` 
## Install dependencies, 
```bash
poetry install
```

## Set up the .env.* files
```
.env.dev
    PGDATABASE = bubble_plot
    PGHOST=localhost

.env.test
    PGDATABASE = bubble_plot_test
    PGHOST=localhost
```

## Seed local dev database


```bash
poetry run seed-db
```

[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)


## run tests
```bash
poetry run pytest -s tests
```

-s flag shows print output

## run server
```bash
poetry run fastapi dev main.py
```