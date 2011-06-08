"""
Place packages in here to include auto activated protocol interfaces to the core server.
Basic protocols are provided already.
"""

#import any added packages here:
from client import client
from events import events
from federationRemote import federationRemote
from federationHost import federationHost
import http

# Change this code to change the protocol configuration
from twisted.internet import reactor

reactor.listenTCP(8080, http.factory)
