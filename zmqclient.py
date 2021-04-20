"""Message client prints messages it pulls from the server."""

import sys
from time import sleep

import zmq


def get_messages(client_id):
    """
    Set up the socket and listen for messages.

    :param client_id: Client ID of this client
    """
    #  Socket to talk to server
    context = zmq.Context()
    socket = context.socket(zmq.PULL)

    # Connect to the local server
    server_url = "tcp://localhost:5556"
    print(f"Pulling messages from server {server_url}")
    socket.connect(server_url)
    print(f"Client {client_id} ready ...")

    while True:
        string = socket.recv_string()
        print(f"Client {client_id} got {string}")
        sleep(0.1)


def usage():
    """Print usage information if invalid parameters are supplied."""
    print(f"Usage: {sys.argv[0]} <clientId>")


def main():
    """
    Check arguments and listens for messages.

    :return 1 on error
    """
    if len(sys.argv) != 2:
        usage()
        exit(1)
    client_id = sys.argv[1]
    get_messages(client_id)


if __name__ == "__main__":
    main()
