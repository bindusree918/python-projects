import socket

# Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to localhost and port
server.bind(("127.0.0.1", 12345))

# Listen for connections
server.listen(1)

print("🟢 Server is waiting for connection...")

conn, addr = server.accept()
print("✅ Connected to:", addr)

while True:
    message = conn.recv(1024).decode()
    print("Client:", message)

    reply = input("You: ")
    conn.send(reply.encode())