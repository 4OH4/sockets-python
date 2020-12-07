FROM python:3.7-alpine
ADD ./udpClient.py /
WORKDIR /
# Python unbuffered
CMD ["python", "-u", "udpClient.py"]