DO
$do$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'usuario') THEN
      CREATE ROLE usuario WITH LOGIN PASSWORD 'contraseña';
   END IF;
END
$do$;

DO
$do$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'nombre-base-de-datos') THEN
      CREATE DATABASE nombre-base-de-datos;
      GRANT ALL PRIVILEGES ON DATABASE nombre-base-de-datos TO usuario;
   END IF;
END
$do$;
