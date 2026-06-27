"""
fancy_greetings engine — emoji-rich methods patched onto cozy_kit.greeting.Greeting.
"""

import random


def wave(self) -> str:
    """Send a cheerful wave to the user."""
    openers = ["Hey", "Hi", "Hello", "Howdy", "Yo"]
    emojis = ["👋", "🤚", "🖐️", "✋"]
    return f"{random.choice(emojis)} {random.choice(openers)}, {self.name}!"


def celebrate(self) -> str:
    """Congratulate the user with a burst of celebration emojis."""
    lines = [
        "You're doing amazing!",
        "Keep up the fantastic work!",
        "You absolutely crushed it!",
        "That's worth celebrating!",
        "Look at you go!",
    ]
    banner = " ".join(random.choices(["🎉", "🎊", "✨", "🥳", "🎈"], k=5))
    return f"{banner}\n{random.choice(lines)} {self.name}!"


def cheer(self) -> str:
    """Give the user an energetic cheer."""
    cheers = [
        f"You've got this, {self.name}! 💪🔥",
        f"Go go go, {self.name}! 🚀⚡",
        f"Nothing can stop you, {self.name}! 🦾🌟",
        f"Believe in yourself, {self.name}! 🙌✨",
    ]
    return random.choice(cheers)


# ── lifecycle hooks ───────────────────────────────────────────────────────────

def on_install(ctx) -> None:
    print(f"[fancy_greetings] installed v{ctx.version} — wave(), celebrate(), cheer() added to Greeting.")


def on_enable(ctx) -> None:
    print(f"[fancy_greetings] enabled.")


def on_disable(ctx) -> None:
    print(f"[fancy_greetings] disabled.")


def on_uninstall(ctx) -> None:
    print(f"[fancy_greetings] uninstalled.")


def on_update(ctx, old_version: str) -> None:
    print(f"[fancy_greetings] updated {old_version} → {ctx.version}.")
