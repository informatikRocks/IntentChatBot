FROM --platform=$BUILDPLATFORM ghcr.io/astral-sh/uv:latest AS uv-stage

FROM python:3.13-slim

# uv Installation aus dem richtigen Stage
COPY --from=uv-stage /uv /uvx /bin/

# Arbeitsverzeichnis
WORKDIR /backend

# 1. Nur die Lock-Files kopieren
COPY pyproject.toml uv.lock ./

# 2. Dependencies installieren (ohne das Projekt selbst, da der Code noch fehlt)
RUN uv sync --frozen --no-install-project --no-dev

# 3. Den gesamten Ordnerinhalt kopieren (app, ml_engine, etc.)
COPY . .

# 4. NLTK Downloads
RUN uv run python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab')"

# 5. Umgebungsvariable setzen, damit Python deine Module findet
ENV PYTHONPATH=/backend

EXPOSE 8000

# Startbefehl
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]