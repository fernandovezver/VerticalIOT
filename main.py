# Made by: Andrés Ruiz Justo

import random

import pyupm_grove as grove
import pyupm_buzzer as upmBuzzer

# Create the button object using D3.
button = grove.GroveButton(3)

# Create the buzzer object using D4.
buzzer = upmBuzzer.Buzzer(4)

# Define the chords to be played.
chords = [upmBuzzer.DO, upmBuzzer.RE, upmBuzzer.MI, upmBuzzer.FA, 
          upmBuzzer.SOL, upmBuzzer.LA, upmBuzzer.SI, upmBuzzer.DO, 
          upmBuzzer.SI];

# Read the input and play a random sound from chords.
while 1:
    if button.value():
        ran = random.randint(0, 8);
        buzzer.playSound(chords[ran]);

# Delete the button object.
del button

# Delete the buzzer object.
del buzzer
