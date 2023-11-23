FROM python:3.9

WORKDIR /project

COPY ./requirements.txt /project/requirements.txt

#RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /project/requirements.txt

COPY ./src /project/src

CMD ["uvicorn", "src.Api.app:app", "--host", "0.0.0.0", "--port", "80"]
