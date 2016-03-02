import random

import pyupm_grove as grove
import pyupm_buzzer as upmBuzzer

button = grove.GroveButton(3)

buzzer = upmBuzzer.Buzzer(4)

chords = [upmBuzzer.DO, upmBuzzer.RE, upmBuzzer.MI, upmBuzzer.FA, 
          upmBuzzer.SOL, upmBuzzer.LA, upmBuzzer.SI, upmBuzzer.DO, 
          upmBuzzer.SI];

while 1:
    if button.value():
        ran = random.randint(0, 8);
        buzzer.playSound(chords[ran]);

del button

del buzzer
