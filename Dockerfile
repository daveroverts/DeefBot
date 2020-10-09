FROM python:3.6-slim
WORKDIR /tmp
COPY requirements.txt /tmp
RUN pip install -r requirements.txt
COPY . /tmp
CMD ["python", "-u", "deefbot/DeefBot.py"]