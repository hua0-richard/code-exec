FROM python:3.11

WORKDIR /fastapi

COPY ./requirements.txt /fastapi/requirements.txt

RUN apt-get update && apt-get install -y docker.io

RUN pip install --no-cache-dir --upgrade -r /fastapi/requirements.txt

RUN pip install pandas scipy mysql-connector-python

COPY ./main.py /fastapi/

USER nobody

CMD ["fastapi", "run", "main.py", "--port", "80"]