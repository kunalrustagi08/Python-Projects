'''
Create a method / function called Shoot.

This method will receive 3 parameters:Bullet Name, Bullet Speed & Bullet Force

Here, the only mandatory parameter is Bullet name, the other two should be
 "optional parameters" with predefined values, that is, it is not necessary
 to pass them a value, since they have one by default.

The method must print all three parameters. Call this method without assigning
 a value to the optional parameters and then call it again assigning values
 ​​to the optional parameters.
'''


def shoot(name, speed=2500, force=16000):
    # Speed is fps and force in pounds

    print(f'Bullet name: {name}')
    print(f'Bullet speed: {speed} fps')
    print(f'Bullet force: {force} pounds of N')


shoot('.50 BMG')
shoot('.22 Swift', 4000)
shoot('.221 Fireball', 2650, 14000)
