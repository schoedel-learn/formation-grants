-- scripts/_schema.sql — one-time DDL for the grants database (chroma-server, PG `grants`).
-- Applied as role grants_app. Tables live in `public` (Mathesar connects as grants_app,
-- which owns its objects there; delete+reload means no staging table is needed).
CREATE TABLE IF NOT EXISTS grantor (
  id            bigserial PRIMARY KEY,
  name          text NOT NULL UNIQUE,
  kind          text,
  website       text NOT NULL,
  contact_name  text,
  contact_email text
);
-- NOTE: `grant` is a reserved word in PostgreSQL; the plural `grants` is the table name.
CREATE TABLE IF NOT EXISTS grants (
  id             bigserial PRIMARY KEY,
  grantor_id     bigint NOT NULL REFERENCES grantor(id) ON DELETE CASCADE,
  name           text NOT NULL,
  focus_areas    text,               -- space-separated tags; NULL allowed while researching (no confirmed areas yet): family marriage adult_faith_formation faith_formation ocia
  amount_min     numeric,
  amount_max     numeric,
  award_type     text NOT NULL DEFAULT 'cash',
  grantee_entity text NOT NULL,
  eligibility    text NOT NULL,
  deadline_type  text NOT NULL DEFAULT 'annual_cycle',
  next_deadline  date,
  application_url text,
  status         text NOT NULL DEFAULT 'researching',
  submitted_on   date,
  decision       text,
  award_amount   numeric,
  source_url     text NOT NULL,
  last_checked   date NOT NULL,
  wiki_page      text NOT NULL,
  UNIQUE (grantor_id, name)
);