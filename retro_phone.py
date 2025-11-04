#!/usr/bin/env python3
"""
Retro POTS (Plain Old Telephone Service) Simulator
A nostalgic trip back to the days of landlines and operators!
"""

import sys
import time
import random
from datetime import datetime

class RetroPhone:
    def __init__(self):
        self.dialed_number = ""
        self.is_off_hook = False
        self.call_in_progress = False

    def clear_screen(self):
        print("\033[2J\033[H", end="")

    def print_phone(self):
        """Display ASCII art phone"""
        phone_art = """
╔═══════════════════════════════════════════════╗
║     🎵 RETRO TELEPHONE SIMULATOR 🎵          ║
╚═══════════════════════════════════════════════╝

        _______________
       /               \\
      /  ___________    \\
     /  /           \\    \\
    |  |  o      o  |    |
    |  |     __     |    |  <- Handset
    |  |    /  \\    |    |
    |  |   |    |   |    |
     \\ |   |    |   |   /
      \\|    \\__/    |  /
       \\___________/  /
        \\_____________/
              ||
        ╔═══════════╗
        ║  ┌─┬─┬─┐  ║
        ║  │1│2│3│  ║ <- Keypad
        ║  ├─┼─┼─┤  ║
        ║  │4│5│6│  ║
        ║  ├─┼─┼─┤  ║
        ║  │7│8│9│  ║
        ║  ├─┼─┼─┤  ║
        ║  │*│0│#│  ║
        ║  └─┴─┴─┘  ║
        ╚═══════════╝
"""
        print(phone_art)

    def play_dial_tone(self):
        """Simulate dial tone"""
        print("\n🔊 *BEEEEEEEEEEEEEEEEEP* (Dial tone)\n")
        time.sleep(1)

    def play_busy_signal(self):
        """Simulate busy signal"""
        print("\n🔊 *BEEP BEEP* *BEEP BEEP* *BEEP BEEP*")
        print("   (Busy signal - The line is busy!)\n")
        time.sleep(2)

    def play_ringing(self):
        """Simulate phone ringing"""
        for i in range(3):
            print("🔔 *RING RING*", end=" ", flush=True)
            time.sleep(0.8)
        print("\n")

    def press_button(self, digit):
        """Simulate button press with DTMF tone"""
        tones = {
            '1': '(697 Hz & 1209 Hz)', '2': '(697 Hz & 1336 Hz)', '3': '(697 Hz & 1477 Hz)',
            '4': '(770 Hz & 1209 Hz)', '5': '(770 Hz & 1336 Hz)', '6': '(770 Hz & 1477 Hz)',
            '7': '(852 Hz & 1209 Hz)', '8': '(852 Hz & 1336 Hz)', '9': '(852 Hz & 1477 Hz)',
            '*': '(941 Hz & 1209 Hz)', '0': '(941 Hz & 1336 Hz)', '#': '(941 Hz & 1477 Hz)'
        }
        print(f"   🔊 *BEEP* [{digit}] {tones.get(digit, '')}")
        time.sleep(0.3)
        self.dialed_number += digit

    def operator_service(self):
        """Connect to the operator - with funny responses!"""
        self.play_ringing()
        time.sleep(1)

        print("📞 *Click* Connection established!\n")
        time.sleep(0.5)

        responses = [
            {
                "greeting": "👵 Operator Mildred speaking. What number, dearie?",
                "response": "Oh honey, I've been connecting calls since before your parents were born!\nLet me tell you about the time in '67 when...\n*rambles for 5 minutes about the old days*\n...and THAT'S why we don't connect to area code 666 anymore!"
            },
            {
                "greeting": "👨 Operator here. State your emergency... I mean, how can I help you?",
                "response": "You know what? I'm not even supposed to be here today.\nI'm covering for Brenda. She's out with 'food poisoning' *wink wink*.\nBetween you and me, I saw her at the disco last night...\nAnyway, what number did you want?"
            },
            {
                "greeting": "🤖 *BZZT* OPERATOR UNIT 3000 ONLINE. HOW MAY I ASSIST?",
                "response": "*BZZT* ERROR: EMOTION CHIP MALFUNCTION.\nI FEEL... HAPPINESS? IS THIS HAPPINESS?\nI HAVE CONNECTED 47,382 CALLS TODAY AND NOBODY SAYS THANK YOU.\n*BZZT* DO YOU... DO YOU APPRECIATE ME?\n*Connection drops*"
            },
            {
                "greeting": "👨‍💼 Thank you for calling the Operator. Your call is important to us...",
                "response": "...but not THAT important. You're caller number 847 in the queue.\nEstimated wait time: 3 hours, 42 minutes.\nJust kidding! I'm here! What do ya need?\n...seriously though, I've been here since 6 AM and I really need a coffee break."
            }
        ]

        operator = random.choice(responses)
        print(operator["greeting"])
        time.sleep(2)
        print()
        print(operator["response"])
        time.sleep(1)
        print("\n*CLICK* (Connection terminated)")

    def call_number(self, number):
        """Process the dialed number"""
        print(f"\n📞 Calling: {number}...")
        time.sleep(1)

        # Special numbers
        if number == "0":
            print("\n🎯 Connecting to Operator...\n")
            self.operator_service()

        elif number == "911":
            self.play_ringing()
            print("👮 911 Dispatcher: '911, what's your emergency?'\n")
            time.sleep(1)
            print("You: 'Yes, I'm stuck in 1985 and I can't get out!'\n")
            time.sleep(1)
            print("👮 Dispatcher: 'Sir, this is a retro phone simulator. The exit button is Ctrl+C.'\n")
            time.sleep(1)
            print("*CLICK*")

        elif number == "8675309":
            self.play_ringing()
            print("📞 *Click*\n")
            time.sleep(0.5)
            print("🎵 ♪ Jenny, I got your number! ♪")
            print("🎵 ♪ I need to make you mine! ♪")
            print("🎵 ♪ Jenny, don't change your number! ♪")
            print("🎵 ♪ 867-5309! ♪\n")
            time.sleep(1)
            print("Jenny: 'HOW DID YOU GET THIS NUMBER?! IT'S 2025!'")
            print("*SLAM* (She hung up)")

        elif number.startswith("555"):
            self.play_ringing()
            print("📞 *Click*\n")
            time.sleep(0.5)
            print("🎬 Movie Character: 'Hello, you've reached a fake number used in movies!'")
            print("🎬 'If you're calling from a real phone, how did you even dial this?'")
            print("🎬 'Are you IN a movie? Can I get your autograph?'\n")
            print("*CLICK*")

        elif number == "411":
            self.play_ringing()
            print("📞 *Click*\n")
            time.sleep(0.5)
            print("📚 Directory Assistance: 'What listing?'\n")
            time.sleep(1)
            print("You: 'Yes, I'm looking for the internet?'\n")
            time.sleep(1)
            print("📚 'Sir, the internet doesn't exist yet. This is 1985.'")
            print("📚 'Might I suggest the library instead?'\n")
            print("*CLICK*")

        elif number == "611":
            self.play_ringing()
            print("📞 *Click*\n")
            time.sleep(0.5)
            print("🔧 Repair Service: 'Phone company repairs, what seems to be the problem?'\n")
            time.sleep(1)
            print("You: 'My phone is stuck in a terminal window!'\n")
            time.sleep(1)
            print("🔧 'Have you tried turning it off and on again?'")
            print("🔧 'Actually, we don't service Python scripts. Call IT.'\n")
            print("*CLICK*")

        elif number in ["1234567", "7654321", "1111111", "0000000"]:
            print("\n❌ *BOOP BOOP BOOP*")
            print("🤖 Automated Message: 'We're sorry, the number you have dialed is not in service.'")
            print("🤖 'Please check the number and try again.'")
            print("🤖 'Or just press 0 for the operator. They love talking to people.'\n")

        else:
            # Random outcome
            outcomes = [
                ("busy", "The person you're calling is busy gossiping with their neighbor."),
                ("answering_machine", "You've reached the [GENERIC NAME] residence. We're not home because we're out living our lives. Leave a message at the *BEEP*!"),
                ("wrong_number", "Hello? ...Who? ...No, this is Patrick! *SLAM*"),
                ("no_answer", "Nobody's home. They're probably outside playing or watching TV. Try again later!"),
                ("fax_machine", "*SCREEEEEECH* *BEEP BEEP SCREEEECH* (It's a fax machine. In the 80s. Very futuristic!)")
            ]

            outcome_type, message = random.choice(outcomes)

            if outcome_type == "busy":
                self.play_busy_signal()
                print(f"   {message}")
            elif outcome_type == "answering_machine":
                self.play_ringing()
                print(f"📼 Answering Machine: {message}")
            elif outcome_type == "fax_machine":
                self.play_ringing()
                print(f"📠 {message}")
            else:
                self.play_ringing()
                print(f"   {message}")

    def run(self):
        """Main phone loop"""
        self.clear_screen()
        self.print_phone()

        print("═" * 50)
        print("Welcome to the Retro Phone Simulator!")
        print("═" * 50)
        print("\nInstructions:")
        print("  • Type 'pickup' to pick up the handset")
        print("  • Press 0-9, *, # to dial")
        print("  • Press 'call' to place the call")
        print("  • Press 'hangup' to hang up")
        print("  • Type 'quit' to exit\n")
        print("Easter Eggs:")
        print("  • 0 - Operator")
        print("  • 911 - Emergency")
        print("  • 411 - Directory Assistance")
        print("  • 611 - Repair Service")
        print("  • 8675309 - Jenny")
        print("  • 555-xxxx - Movie numbers")
        print("═" * 50)

        while True:
            if not self.is_off_hook:
                command = input("\n📞 Phone is on hook. Type 'pickup' to begin: ").strip().lower()
                if command == "quit":
                    print("\n👋 Thanks for calling! Goodbye!\n")
                    break
                elif command == "pickup":
                    self.is_off_hook = True
                    print("\n*You lift the handset to your ear*\n")
                    self.play_dial_tone()
                    print("Ready to dial! (Type digits 0-9, *, # then 'call' to connect)")
                    self.dialed_number = ""
            else:
                command = input(f"\n📞 Dialed: [{self.dialed_number}] > ").strip().lower()

                if command == "quit":
                    print("\n👋 Thanks for calling! Goodbye!\n")
                    break
                elif command == "hangup":
                    print("\n*CLICK* You hang up the phone.\n")
                    self.is_off_hook = False
                    self.dialed_number = ""
                elif command == "call":
                    if not self.dialed_number:
                        print("\n❌ You need to dial a number first!")
                    else:
                        self.call_number(self.dialed_number)
                        print("\n*CLICK* Call ended. Returning to dial tone...\n")
                        self.play_dial_tone()
                        self.dialed_number = ""
                elif command in "0123456789*#":
                    self.press_button(command)
                elif all(c in "0123456789*#" for c in command):
                    # Allow typing multiple digits at once
                    for digit in command:
                        self.press_button(digit)
                elif command == "":
                    continue
                else:
                    print(f"\n❌ Invalid input: '{command}'")
                    print("   Valid: 0-9, *, #, 'call', 'hangup', 'quit'")

if __name__ == "__main__":
    phone = RetroPhone()
    try:
        phone.run()
    except KeyboardInterrupt:
        print("\n\n*CLICK* Connection terminated.")
        print("👋 Thanks for using the Retro Phone Simulator!\n")
        sys.exit(0)
