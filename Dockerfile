FROM python:3.7
RUN pip install poetry
WORKDIR /tmp/myapp
COPY pyproject.toml poetry.lock ./
RUN cd /tmp/myapp && poetry install --no-root
# Copy in everything else:
COPY . .
RUN poetry install
CMD poetry run python deefbot/DeefBot.py