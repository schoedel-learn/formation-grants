# scripts/_connect_mathesar.py — one-time: register the `grants` PG database in Mathesar.
# Runs INSIDE the mathesar_service container:
#   docker cp /tmp/grants_db_pw mathesar_service:/tmp/grants_db_pw
#   docker cp scripts/_connect_mathesar.py mathesar_service:/tmp/connect.py
#   docker exec -w /code -e PYTHONPATH=/code mathesar_service python /tmp/connect.py
#   docker exec mathesar_service rm /tmp/grants_db_pw /tmp/connect.py
import os, sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')
sys.path.insert(0, '/code')
import django
django.setup()
pw = open('/tmp/grants_db_pw').read().strip()
from django.contrib.auth import get_user_model
user = get_user_model().objects.filter(is_superuser=True).first()
from mathesar.utils.permissions import set_up_preexisting_database_for_user
db = set_up_preexisting_database_for_user(
    'postgresql-db-db-1', 5432, 'grants', 'grants', 'grants_app', pw, user,
    sample_data=[], sslmode='prefer')
print('registered database id:', db.id)
from mathesar.rpc import utils as rpc
from db import schemas
print('schemas:', schemas.list_schemas(rpc.connect(db.id, user)))