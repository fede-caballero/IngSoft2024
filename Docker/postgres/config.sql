DO
$do$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'postgres') THEN
      CREATE ROLE postgres WITH LOGIN PASSWORD '1234456';
   END IF;
END
$do$;

DO
$do$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'postgres') THEN
      CREATE DATABASE postgres;
      GRANT ALL PRIVILEGES ON DATABASE postgres TO postgres;
   END IF;
END
$do$;
