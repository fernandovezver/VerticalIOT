import time
import pyupm_grove as grove
import pyupm_buzzer as upmBuzzer
button = grove.GroveButton(4)
buzzer = upmBuzzer.buzzer(3)
chords = [upmBuzzer.DO, upmBuzzer.RE, upmBuzzer.MI, upmBuzzer.FA, 
          upmBuzzer.SOL, upmBuzzer.LA, upmBuzzer.SI, upmBuzzer.DO, 
          upmBuzzer.SI];
if button.value()==1:
	for chord_ind in range(0, 7):
		print buzzer.playSound(chords[chord_ind], 1000000)
    	time.sleep(0.1)
print "Exit"
del buzzer
del button
