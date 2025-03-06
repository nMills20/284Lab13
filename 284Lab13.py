from gpiozero import LED, Button
from time import sleep
import random
led = LED(4)

right_button = Button(23, bounce_time=0.5)
left_button = Button(24, bounce_time=0.5)

player1Count = 0
player2Count = 0
gameCount = 0

def pressed(button):
    global player1Count
    global player2Count
    global gameCount
    if button.pin.number == 23:
        print (player1 + ' pressed first!')
        player1Count += 1
    elif button.pin.number == 24:
        print (player2 + ' pressed first!')
        player2Count += 1
    print(player1 + ' score is: ' + str(player1Count))
    print(player2 + ' score is: ' + str(player2Count))
    gameCount += 1

player1 = input ('Enter player 1 name: ')
player2 = input ('Enter player 2 name: ')
    
while gameCount <= 5:
    led.off()
    sleep(random.randint(2,8))
    led.on()
    right_button.when_pressed = pressed
    left_button.when_pressed = pressed
    
    if gameCount == 5:
        print('The final score is:')
        print(player1 + ' score is: ' + str(player1Count) + ' points')
        print(player2 + ' score is: ' + str(player2Count) + ' points')
        break