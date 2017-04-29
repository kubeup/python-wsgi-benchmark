import argparse
import importlib


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("app", help="dotted name of WSGI app callable [module:callable]")
    parser.add_argument("-b", "--bind",
                        help="The socket to bind",
                        default="127.0.0.1:8000")

    args = parser.parse_args()
    return args


def import_app(args):
    module_name, app_name = args.app.split(':')
    module = importlib.import_module(module_name)
    app = getattr(module, app_name)
    return app
