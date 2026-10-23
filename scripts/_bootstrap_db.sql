-- one-time bootstrap for the grants database on chroma-server
-- applied as PG superuser role `myadmin` inside container postgresql-db-db-1
CREATE ROLE grants_app WITH LOGIN PASSWORD '__PASSWORD__';
CREATE DATABASE grants OWNER grants_app;
