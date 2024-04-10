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
import spi_screen as SPI
import threading
import random as rand
import Adafruit_BBIO.ADC as ADC
# import (joystick API) as JOYSTICK

# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

easy_words = ["CAFE", "FACE", "HAIR", "JADE", "NAAN", "UBER", "ZAPS", "IBEX",
              "GAWK", "EDGE"]
        
medium_words = ["HEART", "FIFTY", "EIGHT", "MOUNT", "ROUTE", "PRIZE", "UNITY",
                "WHICH", "YOUTH", "VITAL"]
        
hard_words = ["FABLED", "CASUAL", "EIGHTH", "EMERGE", "ABACUS", "IAMBIC",
              "VACATE", "WOBBLE", "EAGLET", "DABBED"]
              
code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', '0': '-----', }

# list of alphanumeric for check
alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

# None

# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

class GameCode(threading.Thread):
    red_led = None
    green_led = None
    spi = None
    buzzer = None
    display = None
    potentiometer = None
    
    def __init__(self, red_led = "P2_4", green_led = "P2_6"
                       buzzer = "P2_1", spi = "", potentiometer = "P1_19",
                       xjoy = " ", yjoy = " ", butjoy = " ", i2c_bus=1, 
                       i2c_address=0x70):
                       
        self.red_led         = LED.LED(red_led)
        self.green_led       = LED.LED(green_led)
        self.buzzer          = BUZZER.PWM.stop
        self.spi             = SPI.blank()
        self.display         = HT16K33.HT16K33(i2c_bus, i2c_address)
        self.potentiometer   = POT.Potentiometer(potentiometer)
        self._setup()
        self.unpressed_value = HIGH
        self.pressed_value   = LOW
    def _setup(self):
        """ Initialize the hardware components."""
        
        ADC.setup()
        
        spi.blank()
        
        time.sleep(5)
        #Turn on the SPI
        
    def initial_spi(self):
        """ Starts the interface between the player and the game, describing
        what the objective is for the player and prompting a difficulty 
        choice"""
        
        self.spi.text("welcome to morse code decode", fontsize=24, 
        fontcolor=(255,255,255), backgroundcolor=(0,0,0), justify=CENTER, 
        align=TOP, rotation=90)
        
        time.sleep(3)
        
        self.spi.blank()
        
        time.sleep(1)
        
        self.spi.text("this device is a bomb", fontsize=24, 
        fontcolor=(255,255,255), backgroundcolor=(0,0,0), justify=CENTER, 
        align=TOP, rotation=90)
        
        self.spi.text("your job is to defuse it", fontsize=24, 
        fontcolor=(255,255,255), backgroundcolor=(0,0,0), justify=CENTER, 
        align=CENTER, rotation=90)
        
        self.spi.text("choose your difficulty level", fontsize=24, 
        fontcolor=(255,255,255), backgroundcolor=(0,0,0), justify=CENTER, 
        align=BOTTOM, rotation=90)
        
        time.sleep(5)
        
        self.spi.blank()
        
        # IMPLEMENT LEVEL SELECTION AS VARIABLE NAME "LEVEL"
        
        
    def level_select_wordchoice(self):
        """ This function takes an input from the user about the desired 
        difficulty and then randomly picks a word from the potential word
        arrays"""
        
        if level == "easy":
            word = rand.choice(easy_words)
        elif level == "medium":
            word = rand.choice(medium_words)
        elif level == "hard":
            word = rand.choice(hard_words)
       
    def LEDs(self):
        """ Turn on the correct LED given when an answer is submitted, then
        turn the LED off after a time interval of 1.5 seconds
        """
        if self.correct_answer:
            # Checks if the correct answer has been given, and turns on the
            # green LED if it is
            self.green_led.on() # Is this a time that the LED will be on
            time.sleep(1.5)
            self.green_led.off()
            
        if self.incorrect_answer:
            # Checks if the incorrect answer has been given, and turns on the
            # red LED if it is
            self.red_led.on()
            time.sleep(1.5)
            self.red_led.off()
        # End def

    def stickjoy(self):
        """ Set the up/down, left/right, and push button thresholds on the
        joystick"""
        
        xval=int(ADC.read(self.xjoy))
        yval=int(ADC.read(self.yjoy))
        # self.butjoy=butjoy
        
        
            
        
    
    

        
        self.spi.text("easy", fontsize=24, fontcolor=(255,255,255), 
        backgroundcolor=(0,0,0), justify=CENTER, align=TOP, rotation=90)
        
        self.spi.text("medium", fontsize=24, fontcolor=(255,255,255), 
        backgroundcolor=(0,0,0), justify=CENTER, align=CENTER, rotation=90)
        
        self.spi.text("hard", fontsize=24, fontcolor=(255,255,255), 
        backgroundcolor=(0,0,0), justify=CENTER, align=BOTTOM, rotation=90)
        
    