
FROM python:alpine3.6

WORKDIR /usr/src/app

RUN mkdir files
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
ENV PORT=8000

# For heroku, port env variable is injected
CMD python app.py $PORT