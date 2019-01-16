from thespian.actors import ActorSystem
import sys

if __name__ == "__main__":
    base='multiprocTCPBase'
    cap={'Admin Port': 12345}
    if len(sys.argv) > 1:
        base=sys.argv[1]
    ActorSystem(
        systemBase=base,
        capabilities=cap,
    ).shutdown()
