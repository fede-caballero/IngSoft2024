@echo off
setlocal enabledelayedexpansion

rem Define variables
set ROOT_DIR=D:\4to\INGENIERIA-DE-SOFT\proyecto
set MAIN_DIRS=%ROOT_DIR%\dockers\traefik %ROOT_DIR%\dockers\redis %ROOT_DIR%\dockers\postgres %ROOT_DIR%\ms

echo Seleccione una opción:
echo 1) Iniciar servicios
echo 2) Detener servicios
echo 3) Salir
echo Script iniciado

set /p opcion=Ingrese su opción (1-3):

if %opcion%==1 (
    echo Iniciando servicios...
    for %%d in (%MAIN_DIRS%) do (
        pushd %%d
        if exist docker-compose.yml (
            docker compose up -d
        ) else (
            echo No se encontró docker-compose.yml en %%d
        )
        popd
    )
) else if %opcion%==2 (
    echo Deteniendo servicios...
    for %%d in (%MAIN_DIRS%) do (
        pushd %%d
        if exist docker-compose.yml (
            docker compose down
        ) else (
            echo No se encontró docker-compose.yml en %%d
        )
        popd
    )
) else if %opcion%==3 (
    echo Saliendo del script.
    exit /b
) else (
    echo Opción no válida. Intente nuevamente.
)

endlocal
