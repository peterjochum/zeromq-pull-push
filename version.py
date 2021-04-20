"""
Report currently used ZeroMQ version.

Taken from the ZeroMQ-docs at zguide.zeromq.org/docs/chapter1/
Author: Lev Givon <lev(at)columbia(dot)edu>
"""

import zmq

print(f"Current libzmq version is {zmq.zmq_version()}")
print(f"Current  pyzmq version is {zmq.__version__}")
