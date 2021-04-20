"""Generates some messages and pushes them to a channel."""

from time import sleep

import zmq

# Open the context which manages the underlying sockets
context = zmq.Context()

# Configure the socket to be a push socket
socket = context.socket(zmq.PUSH)
socket.bind("tcp://*:5556")

# Send a number of messages containing an integer
for n in range(20):
    print(f"Sending {n}")
    socket.send_string(str(n))
    sleep(1)
