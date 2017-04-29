from gevent import monkey
monkey.patch_all()

from gevent.pywsgi import WSGIServer

from .base import parse_args, import_app


def main():
    args = parse_args()
    app = import_app(args)

    bind = args.bind

    server = WSGIServer(bind, app)
    server.serve_forever()

if __name__ == '__main__':
    main()
