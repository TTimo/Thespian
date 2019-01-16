from thespian.actors import ActorSystem
import sys

if __name__ == "__main__":
    base='multiprocTCPBase'
    if len(sys.argv) > 1:
        base=sys.argv[1]
    ActorSystem(
        systemBase=base,
    ).shutdown()
