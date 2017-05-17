import sys

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        f = open(filename)
        c = f.read()
        f.close()
        if not c.endswith(']}]}\n'):
            r = open(filename, 'w')
            r.write(c + ']}]}\n')
            r.close()

if __name__ == '__main__':
    main()
