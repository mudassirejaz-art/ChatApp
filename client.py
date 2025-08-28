import socket
import threading

HOST = "127.0.0.1"
PORT = 5555

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode("utf-8")
            if message:
                print(message)
        except:
            print("⚠️ Disconnected from server")
            sock.close()
            break

def start_client():
    username = input("Enter your username: ")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    client.send(username.encode("utf-8"))
    print(f"📢 {username} joined the chat!")

    # Thread to listen for messages
    threading.Thread(target=receive_messages, args=(client,)).start()

    while True:
        msg = input()
        if msg.lower() == "exit":
            client.close()
            break
        client.send(msg.encode("utf-8"))

if __name__ == "__main__":
    start_client()
