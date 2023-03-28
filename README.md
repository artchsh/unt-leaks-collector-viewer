# UNT Leaks Collector&Viewer
`__collect.py__` for collecting UNT (united national testing) Leaks from specified in `config.ini` channel and then put in json file. Then `__main__.py` opens json file, parses it, diving it into 2 different json with messages containing leaks about two subjects (math & comp science), and then showing it using GUI custom tkinter. 
I agree that this maybe is not an efficient way to do this but it works for me, so why not. 

## Start
1. You need to create an application at [My Telegram](https://my.telegram.org/) for an `Api Hash` and `Api ID`
2. Create a copy of `config.example.ini` in the same directory and rename it to `config.ini`
3. Put `Api Hash` and `Api ID` in `config.ini`
4. Put your phone number that is used for your account and username of your account into `phone` and `username` fields
5. Run start.bat

## Requirements
> Project was tested using Python 3.11.0
```
customtkinter==5.1.2
Telethon==1.27.0
```

## Contribution
If you wanna do an optimization for my code, feel free to do it, there is no special code style that you need to follow. Just do what you want.

## Additional Content
Feel free to give advice about my code. Im looking forward to it :D
