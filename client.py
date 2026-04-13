import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 12345))

print("✅ Connected to server")

while True:
    message = input("You: ")
    client.send(message.encode())

    if message.lower() == "bye":
        print("❌ You left the chat")
        break

    reply = client.recv(1024).decode()
    print("Server:", reply)

    if reply.lower() == "bye":
        print("❌ Server ended chat")
        break

client.close()