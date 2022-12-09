#!/bin/bash

rm db.sqlite3
rm -rf ./girlsclothesapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations girlsclothesapi
python3 manage.py migrate girlsclothesapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata kids
python3 manage.py loaddata clothing_types
python3 manage.py loaddata clothing_uses
python3 manage.py loaddata clothing_items
python3 manage.py loaddata item_uses
python3 manage.py loaddata outfits
python3 manage.py loaddata outfit_items