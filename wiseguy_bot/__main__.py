import socket
import time
import random
from . import APP_NAME, APP_DESCRIPTION
from argparse import ArgumentParser

SERVER = "irc.twitch.tv"
PORT = 6667

BOT_NICK = "WiseguyBot"

funny_lines = [
    "Yall are fools.",
    "Fools",
]


def main():
	parser = ArgumentParser(prog=APP_NAME, description=APP_DESCRIPTION)
	parser.add_argument('twitch_channel',
						type=str,
						help='Twitch Channel to connect to.')
	parser.add_argument('oauth_token',
						type=str,
						help='OAuth token for refresh auth.')
	args = parser.parse_args()

	irc = socket.socket()
	irc.connect((SERVER, PORT))
	irc.send(("PASS " + args.oauth_token + "\n" +
			  "NICK " + BOT_NICK + "\n" +
			  "JOIN #" + args.twitch_channel + "\n").encode())

	print(f"Joining https://twitch.tv/{args.twitch_channel}")

	irc.send(f"PRIVMSG #{args.twitch_channel} :Fools\r\n".encode("utf-8"))

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
			irc.send(f"PRIVMSG #{args.twitch_channel} :{funny_line}\r\n".encode("utf-8"))

		time_until_next_message = random.randint(60, 360)
		print(f"Time until next message: {time_until_next_message} seconds")

		time.sleep(time_until_next_message)

	time.sleep(1)

if __name__ == "__main__":
	main()
