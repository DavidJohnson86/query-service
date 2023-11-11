# syntax=docker/dockerfile:1
FROM python:3.11-slim

WORKDIR /application

ENV PYTHONDONTWRITEBYTECODE 1

COPY ["pyproject.toml", "poetry.lock", "README.md","./"]
COPY query_service ./query_service


RUN set -eux \
    && apt-get update \
    && apt-get install -y openssl libssl-dev ca-certificates \
    libffi-dev gcc libc6-dev make musl-dev python3-dev python3-freetype \
    && apt-get clean \
    && pip install --upgrade pip setuptools wheel poetry==1.3.2 \
    && poetry config virtualenvs.create false \
    && poetry install \
    && rm -rf /root/.cache/pip

ENTRYPOINT ["hypercorn", "query_service.endpoints:app", "--reload", "--workers", "1", "--bind", "0.0.0.0:8000"]