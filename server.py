import socket
import threading

HOST = "127.0.0.1"
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()

clients = []
usernames = {}

def broadcast(message, sender_client=None):
    """Send message to all connected clients"""
    for client in clients:
        if client != sender_client:  # agar chaho to sabko bhej do
            try:
                client.send(message.encode("utf-8"))
            except:
                clients.remove(client)

def handle_client(client, addr):
    try:
        username = client.recv(1024).decode("utf-8")
        usernames[client] = username
        clients.append(client)

        join_msg = f"📢 {username} joined the chat!"
        print(join_msg)
        broadcast(join_msg, client)

        while True:
            message = client.recv(1024).decode("utf-8")
            if not message:
                break

            full_message = f"{username}: {message}"
            print(full_message)
            broadcast(full_message, client)

            # Auto reply from server on "hey"
            if message.lower() == "hey":
                reply = "Server: How are you?"
                print(reply)
                broadcast(reply)

    except Exception as e:
        print(f"⚠️ Error: {e}")
    finally:
        if client in clients:
            clients.remove(client)
        left_msg = f"❌ {usernames[client]} left the chat!"
        print(left_msg)
        broadcast(left_msg)
        client.close()

def start_server():
    print(f"🚀 Chat server running on {HOST}:{PORT}")
    while True:
        client, addr = server.accept()
        print(f"✅ Connected with {addr}")
        thread = threading.Thread(target=handle_client, args=(client, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
