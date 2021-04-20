# ZeroMQ-Push-Pull example

Example implementation of a task ventilator (server) and some workers (clients)
using ZeroMQ. Sends the messages in a round robin fashion to an arbitrary
number of clients. See the
[Divide and Conquer example in the documentation](https://zguide.zeromq.org/docs/chapter1/#Divide-and-Conquer)

## Requirements

* libzmq - ZeroMQ library
* pyzmq - Bindings for the ZeroMQ library
* virtualenv (recommended)

## Setup

```shell
virtualenv -p <path_to_python_executable> venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

Begin by starting an arbitrary number of clients

```shell
# On another shell you can launch multiple clients
# python zmqclient.py <client_id>

python zmqclient.py 1

Pulling messages from server tcp://localhost:5556
Client 1 ready ...
Client 1 got 0
Client 1 got 1
Client 1 got 4
Client 1 got 7
Client 1 got 10
Client 1 got 13
...
```

Then start the server to send messages to the socket. Each message will only be
received by one client.

```shell
python zmqserver.py

Sending 0
Sending 1
Sending 2
Sending 3
Sending 4
....
```

## ZMQ-Version

This is the ZMQ version at the time of writing

```shell
python version.py

zeromq-py/version.py
Current libzmq version is 4.3.4
Current  pyzmq version is 22.0.3
```
