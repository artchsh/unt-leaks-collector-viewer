from ChannelMessages import start as Telegram_Messages
import json
from datetime import datetime
import tkinter as tk

Telegram_Messages()
data = json.load(open('channel_messages.json'))
messageContents = []
for OneMessage in data:
    try:
        if(OneMessage["message"] != ''):
            messageContents.append(OneMessage["message"])
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
computer_science = ['#информатика','Информатика', 'comp']

message_types = [mathematics, computer_science]
paths = [mathematics[2], computer_science[2]]

mathematics_messages = []
computer_science_messages = []

for message in messageContents:
    for message_type in message_types:
        if stringsIncludes(message, message_type[0], message_type[1]):
            splitedMessage = message.split('#')
            if (message_type[2] == paths[0]):
                mathematics_messages.append(splitedMessage[0])
            elif (message_type[2] == paths[1]):
                computer_science_messages.append(splitedMessage[0])

for path in paths:
    with open(f'{path}.json', 'w') as outfile:
        if(path == paths[0]):
            json.dump(mathematics_messages, outfile, cls=DateTimeEncoder)
        elif(path == paths[1]):
            json.dump(computer_science_messages, outfile, cls=DateTimeEncoder)

root = tk.Tk()
root.title('UNT sniffer')
window_width = 900
window_height = 900


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)


root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, True)

topFrame = tk.Frame(master=root)
pathsFrame = tk.Frame(master=topFrame)
pagesFrame = tk.Frame(master=topFrame)

path_listbox = tk.Listbox(pathsFrame, selectmode='SINGLE')
pages_listbox = tk.Listbox(pagesFrame, selectmode='SINGLE')

globPath = ''

def goToPageBtnFunction():
    selectedIndex = pages_listbox.curselection()[0]
    if globPath == paths[0]:
        textContent.set(mathematics_messages[selectedIndex])
    elif globPath == paths[1]:
        textContent.set(computer_science_messages[selectedIndex])

def goToPathBtnFunction():
    global globPath
    selectedIndex = path_listbox.curselection()[0]
    path = paths[selectedIndex]
    globPath = path
    if path == paths[0]:
        pages_listbox.delete(0,100)
        for i in range(len(mathematics_messages) ):
            pages_listbox.insert(i, f'{i}')
    elif path == paths[1]:
        pages_listbox.delete(0,100)
        for i in range(len(computer_science_messages) ):
            pages_listbox.insert(i, f'{i}')

for path in paths:
    path_listbox.insert(paths.index(path), f'{path}')

goToPageBtn = tk.Button(pagesFrame, text = "Go to page", command=goToPageBtnFunction)
goToPathBtn = tk.Button(pathsFrame, text = "Go to path", command=goToPathBtnFunction)

textContent = tk.StringVar()
textContent.set(mathematics_messages[0])

text = tk.Label(root, textvariable=textContent, wraplength=window_width, justify='left')

pathsFrame.pack(side=tk.LEFT) 
pagesFrame.pack(side=tk.LEFT)
topFrame.pack(side=tk.TOP)

path_listbox.pack(side=tk.TOP)
pages_listbox.pack(side=tk.TOP)

goToPathBtn.pack(side=tk.BOTTOM)
goToPageBtn.pack(side=tk.BOTTOM)

text.pack(side=tk.TOP)

root.mainloop()