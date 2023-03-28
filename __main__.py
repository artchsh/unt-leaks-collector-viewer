import json
from datetime import datetime
from tkinter import *
import customtkinter


def formatDate(date: str) -> str:
    year_month = date.split('-')
    day = year_month[2].split('T')[0]
    year = year_month[0]
    month = year_month[1]
    return f'{day}/{month}/{year}'


data = json.load(open('channel_messages.json'))
messageContents = []
for OneMessage in data:
    try:
        if (OneMessage["message"] != ''):
            messageContents.append(formatDate(
                OneMessage["edit_date"]) + '\n' + OneMessage["message"])
    except:
        continue


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        if isinstance(o, bytes):
            return list(o)

        return json.JSONEncoder.default(self, o)


def stringsIncludes(txt, value1, value2):
    x1 = txt.find(value1)
    x2 = txt.find(value2)
    if (x1 == -1 and x2 == -1):
        return False
    else:
        return True


mathematics = ['#математика', '#матем', 'math']
computer_science = ['#информатика', 'Информатика', 'comp']

message_types = [mathematics, computer_science]
paths = [mathematics[2], computer_science[2]]

mathematics_messages = []
computer_science_messages = []

for message in messageContents:
    for message_type in message_types:
        if stringsIncludes(message, message_type[0], message_type[1]):
            splitedMessage = message.split('#')
            if (message_type[2] == paths[0]):
                mathematics_messages.append(message)
            elif (message_type[2] == paths[1]):
                computer_science_messages.append(message)
print(len(mathematics_messages), len(computer_science_messages))

for path in paths:
    with open(f'{path}.json', 'w') as outfile:
        if (path == paths[0]):
            json.dump(mathematics_messages, outfile, cls=DateTimeEncoder)
        elif (path == paths[1]):
            json.dump(computer_science_messages, outfile, cls=DateTimeEncoder)


class App(customtkinter.CTk):
    def __init__(self) -> None:
        super().__init__()
        # Global variables
        self.path = ''
        self.pages = []

        # Window
        self.title("UNT Leaks v1.0.0")
        window_width = 420
        window_height = 760
        self.minsize(window_width, window_height)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.resizable(False, True)

        # Text frame
        self.text_frame = customtkinter.CTkFrame(master=self)
        self.text_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Text
        self.textbox = customtkinter.CTkTextbox(master=self.text_frame, wrap='word', width=400, height=700)
        self.textbox.grid(row=0, column=0, columnspan=2)

        # Listboxes
        self.pages_combobox = customtkinter.CTkOptionMenu(
            master=self, command=self.page_callback)
        self.pages_combobox.grid(row=1, column=1)
        self.pages_combobox.set('-')
        self.paths_combobox = customtkinter.CTkOptionMenu(
            master=self, values=paths, command=self.path_callback)
        self.paths_combobox.grid(row=1, column=0)

    def page_callback(self, choice) -> None:
        selectedIndex = int(choice.split('.')[0]) - 1
        self.textbox.delete(index1="0.0", index2="100.100")
        material = ''
        if self.path == paths[0]:
            material = mathematics_messages[int(selectedIndex)]
        elif self.path == paths[1]:
            material = computer_science_messages[int(selectedIndex)]
        self.textbox.insert("0.0", material)

    def path_callback(self, choice) -> None:
        self.path = self.paths_combobox.get()
        self.pages = []
        if self.path == paths[0]:
            self.pages = []
            for i in range(len(mathematics_messages)):
                material = mathematics_messages[i]
                self.pages.append(material.split('\n')[0])
        elif self.path == paths[1]:
            self.pages = []
            for i in range(len(computer_science_messages)):
                material = computer_science_messages[i]
                self.pages.append(material.split('\n')[0])
        for page in self.pages:
            self.pages[self.pages.index(page)] = f'{self.pages.index(page) + 1}. {page}'
        self.pages_combobox.configure(values=self.pages)


if __name__ == "__main__":
    app = App()
    app.mainloop()
