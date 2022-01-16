FROM python:3.7-slim

RUN apt-get update && apt-get install libgomp1

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY run.py run.py
COPY log.py log.py
COPY upkeep upkeep

ENTRYPOINT [ "python3" ]
CMD [ "run.py", "upkeep" ]
