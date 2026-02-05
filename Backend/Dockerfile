
FROM python:3.11-slim


COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /backend
COPY . .
RUN uv run python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab')"

EXPOSE 8000
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]