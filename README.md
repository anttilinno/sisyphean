# Backend

## Set up the development environment

- [X] Install pyenv  `https://github.com/pyenv/pyenv`
- [X] Install latest python `pyenv install 3.11.2`
- [X] Install pdm `https://github.com/pdm-project/pdm`
- [X] Install dependencies from pyproject.toml `pdm install`
- [X] *Optional* - Upgrade packages `pdm update`
- [X] Start database easily `docker compose up`
- [X] Initialize alembic `pdm run alembic upgrade base`
- [X] Run migrations `pdm run alembic upgrade head`
- [ ] Run tests `pdm test` 

* Run daemon
```
pdm run uvicorn app.main:app --reload --workers 1
```

* Run tests
```
pdm run pytest -s
```

# !!! As fetch todos uses pagination, tests break, when there are enough items in database. Fix it.

Downgrade migration
```
pdm run alembic downgrade -1
```