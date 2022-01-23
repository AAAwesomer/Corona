FROM node:12-slim AS node-stage
WORKDIR /app/app/static

COPY app/static/package.json /app/app/static/package.json
COPY app/static/package-lock.json /app/app/static/package-lock.json
RUN npm install

COPY app/static /app/app/static
RUN npm run build

FROM python:3.7-slim AS python-stage
RUN apt-get update && apt-get install libgomp1

WORKDIR /app
RUN pip3 install gunicorn

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY --from=node-stage /app /app
COPY app app
COPY setup.py setup.py
COPY setup.cfg setup.cfg

RUN python3 setup.py install

CMD [ "python3",  "app/wsgi.py" ]
