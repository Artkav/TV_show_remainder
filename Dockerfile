FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /TV_show_remainder
COPY requirements.txt /TV_show_remainder/
RUN pip install -r requirements.txt
COPY . /TV_show_remainder/