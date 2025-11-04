# 🎵 Retro POTS Telephone Simulator 📞

A nostalgic, interactive command-line simulator that brings back the experience of using a Plain Old Telephone Service (POTS) landline from the 1980s!

## Features

- **Authentic Dial Tone**: Experience that classic continuous beep when you pick up the handset
- **DTMF Touch-Tone Simulation**: Each button press displays the actual frequency pairs used in real phones
- **Interactive Operator**: Press 0 to connect with hilariously quirky operators from the past
- **Easter Egg Numbers**: Discover funny responses when calling special numbers
- **ASCII Art Interface**: Retro terminal graphics of a classic telephone

## Installation

Simply run the Python script:

```bash
./retro_phone.py
```

Or:

```bash
python3 retro_phone.py
```

## How to Use

1. **Pick up the handset**: Type `pickup` to begin
2. **Hear the dial tone**: That sweet, sweet beeeeeep
3. **Dial a number**: Type digits 0-9, *, or #
4. **Place the call**: Type `call` to connect
5. **Hang up**: Type `hangup` to end the call
6. **Exit**: Type `quit` to exit the simulator

## Special Numbers (Easter Eggs)

- **0** - Connect to the Operator (random funny operator responses!)
- **911** - Emergency services (with a twist)
- **411** - Directory Assistance
- **611** - Phone Repair Service
- **8675309** - Call Jenny (yes, that Jenny!)
- **555-xxxx** - Any number starting with 555 (movie phone numbers)
- **Random numbers** - Get busy signals, answering machines, wrong numbers, or even fax machines!

## Features in Detail

### The Operator Experience
When you dial 0, you'll be connected to one of several quirky operators:
- Mildred, who's been working since the 60s and loves to ramble
- The guy covering for Brenda who isn't supposed to be there today
- OPERATOR UNIT 3000, a malfunctioning robot with feelings
- The overworked operator who really needs a coffee break

### DTMF Tones
Each button displays the authentic dual-tone multi-frequency (DTMF) pairs:
- Different frequencies for each button
- Simulates the actual technology used in touch-tone phones

### Random Call Outcomes
When calling random numbers, you might encounter:
- Busy signals
- Answering machines with generic messages
- Wrong numbers (This is Patrick!)
- No answer
- Fax machines with authentic screeching sounds (well, text descriptions of them!)

## Technical Details

- Written in Python 3
- No external dependencies required
- Cross-platform compatible
- Uses ANSI escape codes for screen clearing
- Simulates time delays for authentic experience

## Fun Facts

This simulator recreates the experience of:
- Waiting for operators to connect your calls
- The unique sounds of different call outcomes
- The actual DTMF frequency pairs used in real phones (697-941 Hz & 1209-1477 Hz)
- The frustration of busy signals and wrong numbers
- The novelty of answering machines (in the 80s, these were high-tech!)

## Why This Exists

Because sometimes you need to remember what it was like when:
- You couldn't take your phone with you
- Long-distance calls were expensive
- You had to memorize phone numbers
- Operators were real people (mostly)
- Calling someone required actual physical button pressing

Enjoy your trip down memory lane! 📞✨
