@echo off
REM pipenv run flask db init
pipenv run flask db migrate
pipenv run flask db upgrade
pipenv run python Run.py