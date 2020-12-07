FROM python:3.7-alpine
ADD ./threadedUDPserver.py /
WORKDIR /
# Python unbuffered
CMD ["python", "-u", "threadedUDPserver.py"]