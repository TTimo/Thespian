from thespian.actors import ActorSystem
import sys
import logging

logcfg = {
    'version': 1,
    'formatters': {
        'normal': {'format': '%(levelname)-8s %(message)s'},
    },
    'handlers': {
        'h1': {'class': 'logging.FileHandler',
               'filename': 'start.log',
               'formatter': 'normal',
               'level': logging.DEBUG},
    },
    'loggers': {
        '': {'handlers': ['h1',], 'level': logging.DEBUG}
    },
}


if __name__ == "__main__":
    ActorSystem((sys.argv + ['multiprocTCPBase'])[1], logDefs=logcfg)
