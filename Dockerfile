# Dockerfile

# python version
FROM python:3.8

# copy application code to WORKDIR
WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# test
RUN python -m unittest test_find_matching_pair.py

ENTRYPOINT ["python", "find_matching_pair.py"]
