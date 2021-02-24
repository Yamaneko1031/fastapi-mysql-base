FROM python:3.8

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY ./app/pyproject.toml ./app/poetry.lock* /app/
WORKDIR /app/
RUN poetry install --no-root

EXPOSE 8080

COPY ./app /app
COPY startup.sh /startup.sh

RUN chmod 744 hoge.sh
CMD ["startup.sh"]

# CMD sh -c "uvicorn main:app --host 0.0.0.0 --port 8080 && alembic upgrade head"