#!/bin/bash

# Lista de directorios
directories=(
    "/home/fede-caballero/UM/ingenieria/cuartoAnio/ingSoftware/Racing_systems_microservices/Docker/traefik/"
    "/home/fede-caballero/UM/ingenieria/cuartoAnio/ingSoftware/Racing_systems_microservices/Docker/redis/"
    "/home/fede-caballero/UM/ingenieria/cuartoAnio/ingSoftware/Racing_systems_microservices/Docker/postgres/"
)

# Iterar sobre cada directorio y ejecutar docker-compose up
for dir in "${directories[@]}"; do
    echo "Iniciando docker-compose en $dir"
    cd "$dir" || { echo "No se pudo cambiar al directorio $dir"; exit 1; }
    docker-compose up -d || { echo "Falló docker-compose en $dir"; exit 1; }
    echo "docker-compose iniciado en $dir"
done

echo "Todos los contenedores se han iniciado correctamente."