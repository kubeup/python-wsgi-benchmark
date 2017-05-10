import bjoern

from .base import parse_args, import_app


def main():
    args = parse_args()
    app = import_app(args)

    address, port = args.bind.split(':')

    bjoern.run(app, address, port)

if __name__ == '__main__':
    main()
