# Camello
A clean and documented version of robot Kame, some like "Kame110"

Is a "try to organize" that project from JavierIH in a new, easy an functional site.

Of course i find Kame-8dof over internet, but it´s a lot o unorganized information and blank spaces.

This is really because it scheint to be a project for "programming freak" people, but Kame is soooo nice, that i think is too a beautiful project for parents the want to entusiasmate his children with tecnologie and robotic (my case)

## First:
a bunch of 3d plastic is necesary. I find a good version in Thingiverse, from the original proyect from JavierIH. This parts are there, here in GibHub as JavierIH, and from p123ad too. Thanks a lot to both.

### Basically the Plastic Parts are:

FOOTS (last foot parts):
* 4 x Foots

LEGS (middle foot part, of two):
* 4 x TopLegs
* 2 x BottomLegs Left
* 2 x BottomLegs Right (bottomslegs are in sg90 -poor- Servos and another version is for mg90s)

THIGHS ("brackets" here it is a diference too between the used servos):
* 2 x Lefts Thighs 
* 2 x Right Thighs

BODY
* Under and Top Body:
The original version from JavierL are very small. For beginning, it is not too ease to use many cabels or devices. The version from Sergei (Red Crab) is here very improved, i recomend it. This version have the smart feature too, that motor lid and brain lid are separated, because it is very hard to change motors, fix cabels or so in the JavierL version where all brackets close the lid in only one.
 
-- I want to improve all legs parts symetric, no right or left. By brackets is maybe not posible.
-- Another desire is to create a separate case for top servos and container for motherboard, battery and other electronic parts. Here is a good option the Kame Crab version from Serg0000

hier is the link to Javier .stl files:
https://www.thingiverse.com/thing:1265766

Another user "corioco" modified some parts to fix Tower Pro Sg90 servos, because a hole is missed (sg90 have one central hole)
https://www.thingiverse.com/thing:2827295

I find it to late, i think i make a aditional hole in this JavierLH model, but i recomend the "corioco" because sg90´s are cheaper.

Sergei do a very nice remake of crabs-kame version
https://github.com/serg0000/fatKame/tree/serg_dev

and look like the programation is for arduino too (my idee too)
i will try it before another improvements, because for the moment, i print and build the skelett.

The rasperry pi 2 version:
https://github.com/JavierIH/kame

Very funny TV-Show with JavierIH:
https://www.antena3.com/programas/el-hormiguero/secciones/ciencia-marron/kame-el-robot-impreso-en-3d-capaz-de-bailar-breakdance_201802215a8de6b70cf279b114c38345.html

## A little explaining about all the versions i find

**KAME** - Original(?) author JavierHL: a Raspery 2 + ESP wifi modul + Quality Motors

**miniKAME** - smaller version of Kame for arduino / ESP, the servos stay of quality (not for SG90). Author JavierHL.

**poorKAME** - a good adaptation version for the cheaper SG90 servos motors, especially Body and Brackets, because the motors screws holes are 4 (just one instead of two in SG90) 

**p123ad/kame** - very well CAD parts Documented version with diagrams and photos

**fatKAME** - a improved beatifull "Crabs" version of miniKAME with distance sensors and simple "obtacles avoid" funktion. The Control-Website offer 3 funktions more too.

**poorKAME-Punk** (with voltage regulator):
https://www.youtube.com/watch?v=6CAGECC3nNk&t=6s
https://www.thingiverse.com/thing:1428651

https://www.thingiverse.com/thing:3945903
https://github.com/manuel6662/kameqwerty

Board pins can be set to match this scheme in the function init of minikame library. Example:
````
board_pins[0] = D1; // Servo S0
board_pins[1] = D4; // Servo S1
board_pins[2] = D8; // Servo S2
board_pins[3] = D6; // Servo S3
board_pins[4] = D7; // Servo S4
board_pins[5] = D5; // Servo S5
board_pins[6] = D2; // Servo S6
board_pins[7] = D3; // Servo S7
````
At the end, i take the most parts from Sergei robot, but I build it whith a ESP8266, that its semst to be a bad idee, because the pins 9 and 10 are no able to run whith the Distance Sensor. I prepare another versions with ESP32, Arduino Uno, the have more digitals pins, and i want to try whit the Arduino-Nano-WiFi, because ist smaller. For the moment, this robot run very well with ESP8266 but no sensors.

The second Voltage Regulator for 5v for the servos is really not necessary, i draw it in my first plan, but the Servos run very well with direct connection to the 7.3V batterie.

![Kamelion Quadruped_Steckplatine](https://github.com/xastherion/Camello/assets/16471969/0bc6e907-17ca-42df-8fff-36a7f4d1afda)

## License
This project was build upon the great work from [JavierIH](https://github.com/JavierIH/miniKame)
