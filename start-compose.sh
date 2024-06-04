#!/bin/bash

# Asegúrate de que no haya espacios alrededor del signo igual en la declaración de la variable
ROOT_DIR="/media/d3xtro/60CC3B634C20DFD06/4to/INGENIERIA-DE-SOFT/proyecto/"
# Directorios donde están tus archivos docker-compose.yml
MAIN_DIRS=("$ROOT_DIR/dockers/traefik" "$ROOT_DIR/dockers/redis" "$ROOT_DIR/dockers/postgres" "$ROOT_DIR/ms")

echo "Seleccione una opción:"
echo "1) Iniciar servicios"
echo "2) Detener servicios"
echo "3) Salir"
echo "Script iniciado"

select opcion in "Iniciar servicios" "Detener servicios" "Salir"; do
    case $opcion in
        "Iniciar servicios")
            echo "Iniciando servicios..."
            for main_dir in "${MAIN_DIRS[@]}"; do
                if cd "$main_dir"; then
                    if [ -f "docker-compose.yml" ]; then
                        docker compose up -d
                    else
                        echo "No se encontró docker-compose.yml en $main_dir"
                    fi
                else
                    echo "Error al cambiar al directorio $main_dir"
                fi
            done
            ;;
        "Detener servicios")
            echo "Deteniendo servicios..."
            for main_dir in "${MAIN_DIRS[@]}"; do
                if cd "$main_dir"; then
                    if [ -f "docker-compose.yml" ]; then
                        docker compose down
                    else
                        echo "No se encontró docker-compose.yml en $main_dir"
                    fi
                else
                    echo "Error al cambiar al directorio $main_dir"
                fi
            done
            ;;
        "Salir")
            echo "Saliendo del script."
            break
            ;;
        *)
            echo "Opción no válida. Intente nuevamente."
            ;;
    esac
done
