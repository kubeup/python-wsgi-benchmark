from meinheld import patch
patch.patch_all()

from meinheld import server

from .base import parse_args, import_app


def main():
    args = parse_args()
    app = import_app(args)

    address, port = args.bind.split(':')

    if args.disable_logging:
        server.set_access_logger(None)

    server.listen((address, int(port)))
    server.set_keepalive(10)
    server.run(app)

if __name__ == '__main__':
    main()
