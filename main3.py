import threading
from socket import *

from customtkinter import *


class MainWindow(CTk):
    def __init__(self):
        super().__init__()
        self.geometry('400x400')
        self.title('Чат')


        self.menu_frame = CTkFrame(self, width=0, height=400)
        self.menu_frame.place(x=0, y=0)
        self.menu_is_open = False

        self.open_menu_btn = CTkButton(self, width=30, text="|>", command=self.toggle_menu)
        self.open_menu_btn.place(x=0, y=0)

        self.scroll_messages = CTkScrollableFrame(self, width=360, height=370)
        self.scroll_messages.place(x=30, y=0)
        self.scroll_messages.grid_columnconfigure(0, weight=1)

        self.input_msg = CTkEntry(self, placeholder_text="Введіть повідомлення", width=360, height=30)
        self.input_msg.place(x=0, y=370)

        self.send_msg_btn = CTkButton(self, text=">", width=40, height=30, command=self.send_message)
        self.send_msg_btn.place(x=360, y=370)

        self.name_input = CTkEntry(self.menu_frame, width=130, placeholder_text="Введіть імя")

        self.change_theme = CTkButton(self.menu_frame,
                                      width=130,
                                      text="Чорна тема",
                                      command=self.toggle_theme)
        self.change_theme.place(x=10, y=130)
        self.current_theme = "Light"
        set_appearance_mode(self.current_theme)
        self.sock = None
        self.username = "Володя"

        try:
            self.sock = socket(AF_INET, SOCK_STREAM)
            self.sock.connect(('0.tcp.eu.ngrok.io',13572))
            threading.Thread(target=self.receive_messages, daemon=True).start()
            self.send_system_message(f"{self.username} приєднався(лась) до чату")
        except Exception as e :
            self.add_message(f"[SYSTEM] Не вдалось підключитися: {e}")


    def toggle_theme(self):
        if self.current_theme == "Light":
            self.current_theme = "Dark"
            set_appearance_mode(self.current_theme)
            self.change_theme.configure(text="Cвітла тема")
        else:
            self.current_theme = "Light"
            set_appearance_mode(self.current_theme)
            self.change_theme.configure(text="Чорна тема")
    def toggle_menu(self):
        if self.menu_is_open:
            self.open_menu_btn.configure(text="|>")
            self.menu_frame.configure(width=0)
            self.scroll_messages.place(x=30)
            self.input_msg.place(x=0)
            self.name_input.place_forget()
        else:
            self.open_menu_btn.configure(text="<|")
            self.menu_frame.configure(width=150)
            self.scroll_messages.place(x=150)
            self.input_msg.place(x=150)
            self.name_input.place(x=10, y=30)
            self.name = CTkButton()
        self.menu_is_open = not self.menu_is_open

    def add_message(self, msg):
        label = CTkLabel(self.scroll_messages, text=msg, anchor='w', justify='left', wraplength=300)
        label.grid(sticky='w', padx=5, pady=2)

    def send_message(self):
        msg = self.input_msg.get().strip()
        if msg:
            try:
                self.sock.send(f"TEXT@{self.username}@{msg}\n".encode('utf-8'))
                self.input_msg.delete(0, END)
            except:
                self.add_message("[SYSTEM] Повідомлення не надіслано")

    def send_system_message(self, msg):
        if self.sock:
            try:
                self.sock.send(f"TEXT@{self.username}@[SYSTEM] {msg}\n".encode('utf-8'))
            except:
                pass

    def process_message(self, msg):
        if not msg:
            return
        parts = msg.split("@", 2)
        if len(parts) == 3:
            _, author, text = parts
            self.add_message(f"{author}: {text}")

    def receive_messages(self):
        buffer = ""
        while True:
            try:
                data = self.sock.recv(1024)
                if not data:
                    break
                buffer += data.decode('utf-8')
                while "\n" in buffer:
                    line, buffer = buffer.split("\n", 1)
                    self.process_message(line.strip())
            except:
                break



win = MainWindow()
win.mainloop()