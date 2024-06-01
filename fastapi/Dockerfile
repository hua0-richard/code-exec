FROM python:3.11

WORKDIR /fastapi

COPY ./requirements.txt /fastapi/requirements.txt

RUN apt-get update && apt-get install -y docker.io

RUN pip install --no-cache-dir --upgrade -r /fastapi/requirements.txt

COPY ./main.py /fastapi/

CMD ["fastapi", "run", "main.py", "--port", "80"]