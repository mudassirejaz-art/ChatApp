# ChatApp 💬

A simple **Python socket-based chat application** built with client-server architecture. Multiple clients can connect to the server and exchange real-time messages.

---

## 🚀 Features

* Client-Server architecture using Python `socket`
* Multiple clients can join the chat
* Broadcast messages to all connected clients
* Username-based identification
* Server keeps track of connected users
* Lightweight and easy to run

---

## 📂 Project Structure

```
ChatApp/
├── server.py        # Chat server script
├── client.py        # Chat client script
├── requirements.txt # Project dependencies
└── README.md        # Documentation
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/mudassirejaz-art/ChatApp.git
cd ChatApp
```

2. Create a virtual environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Start the Server

```bash
python3 server.py
```

### Start a Client

```bash
python3 client.py
```

When prompted, enter your username. Start chatting with others connected to the server!

---

## 🛠 Requirements

* Python 3.8+
* Standard Python libraries (`socket`, `threading`)

---

## 📌 Notes

* Default host: `127.0.0.1`
* Default port: `5555`
* Make sure to start the server **before** starting clients.

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

👨‍💻 Developed by **Mudassir Ejaz**
