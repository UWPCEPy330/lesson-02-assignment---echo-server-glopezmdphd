import socket
import sys
import traceback


def server(log_buffer=sys.stderr):
    address = ('127.0.0.1', 10000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(1)

    print("making a server on {0}:{1}".format(*address), file=log_buffer)

    try:
        while True:
            print('waiting for a connection', file=log_buffer)
            conn, addr = sock.accept()
            try:
                print('connection - {0}:{1}'.format(*addr), file=log_buffer)
                while True:
                    data = conn.recv(16)
                    if not data:
                        break
                    print('received "{0}"'.format(data.decode('utf8')))
                    conn.sendall(data)
                    print('sent "{0}"'.format(data.decode('utf8')))
            except Exception as e:
                traceback.print_exc()
            finally:
                conn.close()
                print('echo complete, client connection closed', file=log_buffer)
    except KeyboardInterrupt:
        print('quitting echo server', file=log_buffer)
        sock.close()


if __name__ == '__main__':
    server()
    sys.exit(0)

