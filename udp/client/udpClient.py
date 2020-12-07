import socket
import sys
import time
import logging

server_address = ("localhost", 10000)


def create_and_send(message):

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1)

    # Connect the socket to the port where the server is listening
    logging.info("Connecting to %s port %s" % server_address)
    sock.connect(server_address)

    # Send messages to socket
    logging.info('%s: sending "%s"' % (sock.getsockname(), message))
    sock.send(message.encode())

    # Read response packet
    try:
        data = sock.recv(1024)
        logging.info('%s: received "%s"' % (sock.getsockname(), data.decode()))
    except socket.timeout:
        data = None
        logging.info("No response - timeout")
    except ConnectionRefusedError as e:
        logging.info("Unable to receive a response: %s" % e)

    sock.close()


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    message_counter = 0

    while True:

        try:
            message_counter += 1
            message = f"Message {str(message_counter)} from client"

            create_and_send(message)

        except ConnectionResetError as e:
            print("Error: ", e)

        except KeyboardInterrupt:
            break

        time.sleep(1)