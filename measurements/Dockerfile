FROM python:3.8.10-alpine3.13

WORKDIR /app

# Copy the django app to the working directory
COPY . /app

# Set the environment variables
ENV MEASUREMENTS_DB_HOST 10.128.0.3
ENV VARIABLES_HOST 10.128.0.4
ENV PLACES_HOST 10.128.0.8
ENV URL_VARIABLES http://10.128.0.4:8080/variables
ENV URL_PLACES http://10.128.0.8:8080/places

# Install Python dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["sh", "init.sh"]