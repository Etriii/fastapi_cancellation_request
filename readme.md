Install this following:
```
pip install fastapi uvicorn gunicorn sqlmodel psycopg2-binary httpx

or 

pip install -r requirements.txt
```

To run migrations:

``` generate migration
```
In Windows:
alembic revision --autogenerate -m "Migration Message"

``` run migration
alembic upgrade head
```
In Windows:
python -m alembic upgrade head

To run seeders:

windows: python -m app.migrate_fresh_and_seed  
note: it will reset your database data

-------------------///OTHERS///-------------------
python -c "import secrets; print(secrets.token_urlsafe(32))" #to generate secret keys


-------------------//////-------------------

To run the app:
```
uvicorn app.main:app --reload
```
In Windows:
python -m uvicorn app.main:app --reload



