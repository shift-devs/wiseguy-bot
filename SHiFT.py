import socket
import time
import random

SERVER = "irc.twitch.tv"
PORT = 6667

BOT_NICK = "TheMawgu"
OAUTH_TOKEN = "" 

CHANNEL = "shift"

funny_lines = [
    "Yall are fools.",
    "Fools",
]

irc = socket.socket()
irc.connect((SERVER, PORT))
irc.send(("PASS " + OAUTH_TOKEN + "\n" +
          "NICK " + BOT_NICK + "\n" +
          "JOIN #" + CHANNEL + "\n").encode())

print(f"Joining {CHANNEL}")

irc.send(f"PRIVMSG #{CHANNEL} :Fools\r\n".encode("utf-8"))

while True:
    response = irc.recv(2048).decode("utf-8")
    print(response)

    if "PING" in response:
        irc.send("PONG\n".encode("utf-8"))

    if "PRIVMSG" in response:
        username = response.split("!")[0][1:]
        message = response.split("PRIVMSG")[1].split(":")[1].strip()
        tags = response.split("PRIVMSG")[0]

        # Print message received
        print(f"Message posted: {message}")

    if random.random() < 1.0: 
        funny_line = random.choice(funny_lines)
        irc.send(f"PRIVMSG #{CHANNEL} :{funny_line}\r\n".encode("utf-8"))

    time_until_next_message = random.randint(60, 360)
    print(f"Time until next message: {time_until_next_message} seconds")

    time.sleep(time_until_next_message)

time.sleep(1)
