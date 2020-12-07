# sockets-python
Client/server sockets in Python for demo and debugging

## UDP
    cd udp/client
    python udpClient.py

    cd udp/server
    python threadedUDPserver.py

or

    docker build -t udpserver .
    docker run -p 10000:10000/udp udpserver
