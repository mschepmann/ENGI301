"""
--------------------------------------------------------------------------
Morse Code Decode Game
--------------------------------------------------------------------------
License:   
Copyright 2022 Erik Welsh

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Use the following hardware components to make a game involving morse code
deciphering:

  - HT16K33 Display
  - Red LED
  - Green LED
  - Potentiometer (analog input)
  - Joystick
  - SPI Screen

Requirements:
  - Hardware:
    - When the device powers on, SPI screen will display an introduction screen 
    with instructions and then difficulty level settings. Once the game is
    started, the buzzer will sound morse code and the 7-hex display will be a
    countdown timer. If the user deciphers the code correctly, a green LED will
    turn on and the buzzer and timer will stop; if the user is incorrect, a red
    LED will turn on, the buzzer will play a tone, and then the game will
    continue. At the end of each round, the user will have an option, using a
    joystick, to power off or keep playing.
    - User interaction:
      - The first point of user interaction will be selection of the difficulty
      level. There will be two difficulty aspects: The first will account the 
      time intervals it takes for the morse code to be sent to the buzzer; the 
      second will vary the time the player has to solve the puzzle. The user
      will depend heavily on the joystick to change position of the cursor on
      the SPI screen and choose numbers for input. They will use the button
      function in the joysitck to act as an "enter" button.

Uses:
  - HT16K33 display library developed in class
  - 

"""

import time
import ht16k33 as HT16K33
import led as LED
import buzzer as BUZZER
import potentiometer as POT
import word_to_morse as MORSE
# import spi_screen as SPI
# import (joystick API) as JOYSTICK

# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

# None

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

# None

# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

class GameCode():
    red_led = None
    green_led = None
    spi = None
    buzzer = None
    display = None
    potentiometer = None
    
    def __init__(self, red_led = "P2_4", green_led = "P2_6"
                       buzzer = "P2_1", spi = "", 
                       potentiometer = "P1_19", 
                       i2c_bus=1, i2c_address=0x70):
                       
        self.red_led        = LED.LED(red_led)
        self.green_led      = LED.LED(green_led)
        self.buzzer         = BUZZER.PWM.stop
        self.spi            = 
        self.display        = HT16K33.HT16K33(i2c_bus, i2c_address)
        self.potentiometer  = POT.Potentiometer(potentiometer)
        self._setup()
        
    def _setup(self):
        """ Initialize the hardware components."""
        #Turn on the SPI
        
    
    def word_choice(self):
       # Create arrays of words that can be chosen for the game
       
        easy_words = ["CAFE", "FACE", "HAIR", "JADE", "NAAN", "UBER", "ZAPS", 
        "IBEX", "GAWK", "EDGE"]
        
        medium_words = ["HEART", "FIFTY", "EIGHT", "MOUNT", "ROUTE", "PRIZE",
        "UNITY", "WHICH", "YOUTH", "VITAL"]
        
        hard_words = ["FABLED", "CASUAL", "EIGHTH", "EMERGE", "ABACUS",
        "IAMBIC", "VACATE", "WOBBLE", "EAGLET", "DABBED"]
        
    