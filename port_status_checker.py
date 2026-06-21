import socket

host = input("Enter host (Example: google.com or localhost): ").strip()

if not host:
    host = "127.0.0.1"

port = int(input("Enter port number: "))

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)

    result = sock.connect_ex((host, port))

    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")

    sock.close()

except Exception as e:
    print("Error:", e)