# ircbot
A basic IRC bot implemented in python.

# Requirements
Python v3.5 (may work in earlier v3.x)

# Usage
don't

# WTF?
* network.py functions handle socket creation and character encoding/decoding
* irc.py functions formulate and return IRC command strings, (loosely) based on RFC 2812
* app.py functions are application-level/high-level, they should perform common multi-step or complex sequences
* bot.py is where everything gets executed, from startup to the main loop
* Yes, I'm a n00b, stop judging ;_;
