FROM python:3.7-slim
RUN pip install requests
WORKDIR /test
COPY . .
CMD ["python", "-m", "unittest", "test_server"]



