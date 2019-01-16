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
               'filename': 'thespian.log',
               'formatter': 'normal',
               'level': logging.DEBUG},
    },
    'loggers': {
        '': {'handlers': ['h1',], 'level': logging.DEBUG}
    },
}


if __name__ == "__main__":
    base='multiprocTCPBase'
    if len(sys.argv) > 1:
        base=sys.argv[1]
    ActorSystem(
        systemBase=base,
        logDefs=logcfg
    )
