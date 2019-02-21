FROM python

VOLUME /code

WORKDIR /code

COPY ./src /code

# We're installing the project into the container so later we can mount straight into Python's dist packages and develop live

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    python setup.py install --single-version-externally-managed --root=/