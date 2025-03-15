import sys
import threading
import socket
import tkinter as tk
from tkinter import simpledialog, scrolledtext, messagebox


# Ask the user for their username
def ask_username():
    root = tk.Tk()
    root.withdraw()
    username = simpledialog.askstring("Username", "Enter your username:")
    if not username:
        messagebox.showerror("Error", "Username cannot be empty!")
        sys.exit(1)
    return username


# Ask the user for the recipient's username
def ask_recipient():
    root = tk.Tk()
    root.withdraw()
    recipient = simpledialog.askstring("Recipient", "Enter the recipient's username:")
    if not recipient:
        messagebox.showerror("Error", "Recipient cannot be empty!")
        sys.exit(1)
    return recipient


# Chat client class
class Client:

    def __init__(self, root, username, recipient, server_ip, port):
        self.username = username
        self.recipient = recipient
        self.server_ip = server_ip
        self.port = port
        self.clientSend = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.clientRecv = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.setup_gui(root)
        self.register_and_start_threads()

    def setup_gui(self, root):
        self.root = root
        self.root.title(f"Chat with {self.recipient}")

        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD)
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.chat_area.config(state=tk.DISABLED)

        self.message_entry = tk.Entry(root)
        self.message_entry.pack(padx=10, pady=(0, 10), fill=tk.X, expand=True)
        self.message_entry.bind("<Return>", self.send_message)

    def register_and_start_threads(self):
        self.clientSend.connect((self.server_ip, self.port))
        send_thread = threading.Thread(target=self.do_send_registration)
        send_thread.start()

        self.clientRecv.connect((self.server_ip, self.port))
        recv_thread = threading.Thread(target=self.do_recv_registration)
        recv_thread.start()

    def do_send_registration(self):
        regReq1 = f"REGISTER TOSEND {self.username}\n\n"
        self.clientSend.send(regReq1.encode("utf-8"))
        ack1 = self.clientSend.recv(1024).decode("utf-8")
        arr1 = ack1.split(" ")
        if arr1[0] == "REGISTERED" and arr1[1] == "TOSEND" and arr1[2] == f"{self.username}\n\n":
            print(f"{self.username} Successfully Registered to Send")
        else:
            messagebox.showerror("Error", "Failed to register to send messages.")
            sys.exit(1)

    def do_recv_registration(self):
        regReq2 = f"REGISTER TORECV {self.username}\n\n"
        self.clientRecv.send(regReq2.encode("utf-8"))
        ack2 = self.clientRecv.recv(1024).decode("utf-8")
        arr2 = ack2.split(" ")
        if arr2[0] == "REGISTERED" and arr2[1] == "TORECV" and arr2[2] == f"{self.username}\n\n":
            print(f"{self.username} Successfully Registered to Receive")
            recv_thread = threading.Thread(target=self.recv_msg)
            recv_thread.start()
        else:
            messagebox.showerror("Error", "Failed to register to receive messages.")
            sys.exit(1)

    def send_message(self, event=None):
        msg = self.message_entry.get()
        if not msg:
            return
        recipient, content, form = self.check_send_format(msg)
        if form:
            message = f"SEND {recipient}\nContent-length: {len(content)}\n\n{content}"
            self.clientSend.send(message.encode("utf-8"))
            self.chat_area.config(state=tk.NORMAL)
            self.chat_area.insert(tk.END, f"You: {content}\n")
            self.chat_area.config(state=tk.DISABLED)
            self.chat_area.yview(tk.END)
            self.message_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Message format incorrect.")

    def check_send_format(self, msg):
        recipient = self.recipient
        content = msg.strip()
        form = bool(recipient and content)
        return recipient, content, form

    def recv_msg(self):
        while True:
            try:
                msg = self.clientRecv.recv(1024).decode("utf-8")
                sender, content, form = self.check_recv_format(msg)
                if form:
                    self.chat_area.config(state=tk.NORMAL)
                    self.chat_area.insert(tk.END, f"{sender}: {content}\n")
                    self.chat_area.config(state=tk.DISABLED)
                    self.chat_area.yview(tk.END)
                    ack = f"RECEIVED {sender}\n\n"
                else:
                    ack = "ERROR 103 Header Incomplete\n\n"
                self.clientRecv.send(ack.encode("utf-8"))
            except Exception as e:
                print("Exception:", e)
                break

    def check_recv_format(self, msg):
        sender = ""
        content = ""
        form = True
        arr = msg.split("\n")
        a = arr[0].split(" ")
        b = arr[1].split(" ")
        if a[0] != "FORWARD" or b[0] != "Content-length:":
            form = False
        sender = a[1]
        content = arr[3]
        length = b[1]
        if not sender or not content or len(content) != int(length):
            form = False
        return sender, content, form


# Main execution
if __name__ == "__main__":
    username = ask_username()
    recipient = ask_recipient()
    SERVER_IP = "127.0.0.1"  # Change this to your server IP
    PORT = 5001

    root = tk.Tk()
    client = Client(root, username, recipient, SERVER_IP, PORT)
    root.mainloop()