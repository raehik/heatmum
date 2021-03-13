#!/usr/bin/env python
from lib import *
import sys

socket = int(sys.argv[1])
state  = sys.argv[2].lower() == "on"
energenie_main(lambda : set_socket(socket, state))
