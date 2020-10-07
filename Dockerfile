FROM python:3.6-slim
RUN pip install poetry
WORKDIR /tmp/myapp
COPY pyproject.toml poetry.lock ./
RUN cd /tmp/myapp && poetry install --no-dev --no-root
# Copy in everything else:
COPY . .
CMD poetry run python -u deefbot/DeefBot.py