# fablab-incbations

### setup
`. venv/bin/activate`

`export FLASK_APP=app`

`export FLASK_ENV=development`

`pipenv install`

`flask db init`

`flask db upgrade`

### dev
`flask run`

### deploy in heroku (or others)
`git push heroku master`
`gunicorn app:ap`
