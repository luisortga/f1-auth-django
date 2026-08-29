#!/usr/bin/env bash
set -o errexit

# Instalar uv automáticamente si no está presente
if ! command -v uv &> /dev/null; then
    echo "Instalando uv..."
    curl -LsSf https://astral.sh | sh
    source $HOME/.local/bin/env
fi

# Sincronizar el entorno usando el archivo uv.lock (descarta paquetes de desarrollo si los hay)
uv sync --frozen --no-dev

# Ejecutar los comandos de Django en el entorno gestionado por uv
uv run python manage.py collectstatic --no-input
uv run python manage.py migrate
