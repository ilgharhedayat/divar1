FROM hub.hamdocker.ir/library/python:3.8
WORKDIR /divar/
COPY requirements.txt /requirements/base.txt
RUN pip install -r /requirements/base.txt
ADD ./ ./
ENTRYPOINT ["/bin/sh", "-c" , "python manage.py migrate && gunicorn --bind 0.0.0.0:8000 divar.wsgi"]
