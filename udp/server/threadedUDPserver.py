import logging
import socketserver
import os
import sys


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Handler for each incomming request
    
    Responds with a string message back to the source
    """

    # Override the handle() method
    def handle(self):

        # Receive and print the datagram received from client
        logging.info("Recieved one request from {}".format(self.client_address[0]))
        datagram = self.rfile.readline().strip()

        logging.info(f"Datagram recieved : {datagram.decode()}")

        # Send a message to the client
        logging.info("Responding...")
        self.wfile.write(f"Response from Server".encode())


class EchoServer(socketserver.ThreadingUDPServer):
    """
    Server to process incomming requests
    
    Just logs the client address - anything else is handled by the EchoHandler
    """
    
    allow_reuse_address = True

    def process_request(self, request, client_address):
        logging.info("Connection from client %r", client_address)
        super().process_request(request, client_address)


if __name__ == "__main__":

    DEFAULT_HOST = "0.0.0.0"

    # Configure host and port from environment variables
    host = os.getenv("HOST", DEFAULT_HOST)
    if host == "localhost":
        host = DEFAULT_HOST
    port = int(os.getenv("PORT", 10000))

    logging.basicConfig(level=logging.INFO)
    logging.info(f"Listening on {host}:{port}")

    # Create server and start listening/echoing
    try:
        with EchoServer((host, port), EchoHandler) as server:
            server.serve_forever()
    except (KeyboardInterrupt, SystemExit):
        server.shutdown()
        server.server_close()
        sys.exit(0)
