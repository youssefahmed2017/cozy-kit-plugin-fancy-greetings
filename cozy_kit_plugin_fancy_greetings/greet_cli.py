"""fancy-greet — standalone CLI for the fancy-greetings plugin."""

import argparse
import random
import sys


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="fancy-greet",
        description="Send a fancy greeting from the command line.",
    )
    parser.add_argument("name", nargs="?", default="friend", help="Name to greet.")
    parser.add_argument(
        "--style",
        choices=["wave", "celebrate", "cheer", "random"],
        default="random",
        help="Greeting style (default: random).",
    )
    args = parser.parse_args()

    greetings = {
        "wave": _wave,
        "celebrate": _celebrate,
        "cheer": _cheer,
    }

    style = args.style if args.style != "random" else random.choice(list(greetings))
    print(greetings[style](args.name))


def _wave(name: str) -> str:
    openers = ["Hey", "Hi", "Hello", "Howdy", "Yo"]
    emojis = ["👋", "🤚", "🖐️", "✋"]
    return f"{random.choice(emojis)} {random.choice(openers)}, {name}!"


def _celebrate(name: str) -> str:
    lines = [
        "You're doing amazing!",
        "Keep up the fantastic work!",
        "You absolutely crushed it!",
        "That's worth celebrating!",
        "Look at you go!",
    ]
    banner = " ".join(random.choices(["🎉", "🎊", "✨", "🥳", "🎈"], k=5))
    return f"{banner}\n{random.choice(lines)} {name}!"


def _cheer(name: str) -> str:
    cheers = [
        f"You've got this, {name}! 💪🔥",
        f"Go go go, {name}! 🚀⚡",
        f"Nothing can stop you, {name}! 🦾🌟",
        f"Believe in yourself, {name}! 🙌✨",
    ]
    return random.choice(cheers)


if __name__ == "__main__":
    sys.exit(main())
