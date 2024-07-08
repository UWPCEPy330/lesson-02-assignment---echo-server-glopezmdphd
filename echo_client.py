import socket
import sys
import traceback


def client(msg, log_buffer=sys.stderr):
    server_address = ('localhost', 10000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('connecting to {0} port {1}'.format(*server_address), file=log_buffer)
    sock.connect(server_address)

    received_message = ''

    try:
        print('sending "{0}"'.format(msg), file=log_buffer)
        sock.sendall(msg.encode('utf-8'))

        while True:
            chunk = sock.recv(16)
            if len(chunk) < 16:
                received_message += chunk.decode('utf-8')
                print('received "{0}"'.format(chunk.decode('utf8')), file=log_buffer)
                break
            received_message += chunk.decode('utf-8')
            print('received "{0}"'.format(chunk.decode('utf8')), file=log_buffer)

    except Exception as e:
        traceback.print_exc()
    finally:
        print('closing socket', file=log_buffer)
        sock.close()

    return received_message


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage = '\nusage: python echo_client.py "this is my message"\n'
        print(usage, file=sys.stderr)
        sys.exit(1)

    msg = sys.argv[1]
    print("Server says: {}".format(client(msg)))


