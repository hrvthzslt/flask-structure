FROM python:3.10-slim

COPY --from=ghcr.io/astral-sh/uv:0.6 /uv /uvx /bin/

COPY . /app

RUN uv pip install --system -r /app/requirements.txt

WORKDIR /app

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
