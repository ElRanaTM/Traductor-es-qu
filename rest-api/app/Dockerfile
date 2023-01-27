FROM alpine:3.10

RUN apk add --no-cache --update \
    python3 python3-dev gcc \
    gfortran musl-dev \
    libffi-dev openssl-dev
    
RUN pip3 install --upgrade pip

COPY /src/. /

RUN  pip3 install --no-cache-dir -r src/requirements.txt

CMD uvicorn main:app --host=0.0.0.0 --port=$PORT