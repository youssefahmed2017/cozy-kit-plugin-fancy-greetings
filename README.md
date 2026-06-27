# cozy-kit-plugin-fancy-greetings

A [cozy-kit](https://github.com/youssefahmed2017/cozy-kit-plugins) plugin that adds emoji-rich greeting methods to the `Greeting` class.

## Installation

```bash
pip install cozy-kit-plugin-fancy-greetings
```

Or via the cozy-kit marketplace CLI:

```bash
cozy-plugins marketplace install fancy-greetings
```

## Methods added to `Greeting`

| Method | Description |
|---|---|
| `wave()` | Sends a cheerful wave with a random emoji |
| `celebrate()` | Congratulates the user with celebration emojis |
| `cheer()` | Gives the user an energetic cheer |

## Usage

```python
from cozy_kit.greeting import Greeting
from cozy_kit.plugins import plugin, add_plugin
import cozy_kit_plugin_fancy_greetings as fg

plugin(metadata=fg.METADATA, engine=fg.ENGINE)
add_plugin("fancy_greetings")

g = Greeting(name="Youssef")
print(g.wave())       # 👋 Hey, Youssef!
print(g.celebrate())  # 🎉 🥳 ✨ 🎊 🎈\nYou're doing amazing! Youssef!
print(g.cheer())      # Go go go, Youssef! 🚀⚡
```

## License

MIT
