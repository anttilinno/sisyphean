# Backend

## Set up the development environment

- [ ] Install pyenv  `https://github.com/pyenv/pyenv`
- [ ] Install latest python `pyenv install 3.11.2`
- [ ] Install pdm `https://github.com/pdm-project/pdm`
- [ ] Install dependencies from pyproject.toml `pdm install`
- [ ] *Optional* - Upgrade packages `pdm update`
- [ ] Start database easily `docker compose up`
- [ ] Initialize alembic `pdm run alembic upgrade base`
- [ ] Run migrations `pdm run alembic upgrade head`
- [ ] Run tests `pdm test` 

* Run daemon
```
pdm run uvicorn app.main:app --reload --workers 1
```

* Run tests
```
pdm run pytest -s
```
