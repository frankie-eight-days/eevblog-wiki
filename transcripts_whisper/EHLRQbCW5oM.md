---
video_id: EHLRQbCW5oM
title: Guest Video: Electronoobs - Building a POV Display
url: https://www.youtube.com/watch?v=EHLRQbCW5oM
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 16, "2": 29, "3": 43, "4": 60, "5": 74, "6": 99, "7": 122, "8": 138, "9": 150, "10": 167, "11": 180, "12": 204, "13": 224, "14": 242, "15": 258, "16": 276, "17": 297, "18": 315, "19": 336, "20": 356, "21": 375, "22": 395, "23": 412, "24": 432, "25": 444, "26": 465, "27": 486, "28": 503, "29": 521, "30": 543, "31": 559, "32": 577, "33": 595, "34": 613, "35": 628, "36": 651, "37": 666, "38": 688, "39": 704, "40": 718, "41": 743, "42": 762, "43": 779, "44": 798, "45": 813, "46": 829, "47": 848}
---

**Dave Jones:** What's up my friends, welcome back. I'm Electro-Noobs from the Electro-Noobs channel. Thanks to Dave Offer for a guest video, we all had the opportunity to share our channel with you guys. So, thank you very much Dave for doing this, you are awesome. If you're not familiar with my channel, well, I'm an electronic engineer here in

**Dave Jones:** Spain and I started my YouTube channel one and a half years back. I don't have a main topic on my channel, since I like to do any sort of electronic-related project, but you will basically find a lot of DIY videos where I show you how to make a project start to

**Dave Jones:** finish and also explain you how the circuit works at the same time. You will also find a lot of Arduino stuff, basic circuits, drones, 3D printing and much more. So, once again Dave, thank you for this opportunity for all of us and thanks to you guys for being so

**Dave Jones:** awesome. In this today's video we will see how to build a POV display, so please, enjoy. What's up my friends, welcome back. This is a Persistent Vision or better known a POV display and it's based on Arduino. The LEDs are blinking so fast while the propeller

**Dave Jones:** is spinning that you get the illusion that the light from the LEDs is drawing shapes, since the lights are always turning on in the same spot. In this project we will see how to show text, time as a real clock or any other shape, so how we manage to keep

**Dave Jones:** this so synchronized. The secret is this small magnet here and the Hall sensor. Ok, so let's see how to build our own homemade and Arduino-based POV display. So, let's get started. What's up my friends, welcome back. Let's see how to build this awesome POV display

**Dave Jones:** that could show text, time or any other shape. So, we have a line of LEDs here, in my case 8 green LEDs, 2 red and 1 blue. We also have a DC motor that will spin the entire propeller. The Arduino inside will control the LEDs and turn them on and off when needed.

**Dave Jones:** In order to synchronize each spin on the other side of the propeller, I've placed a Hall sensor switch. This sensor will give a low pulse each time that I place a magnet in front of it and a high pulse the rest of the time, as we can see here on my oscilloscope.

**Dave Jones:** I now have 5 volts. I approach the magnet and the voltage drops to ground. Simple, right? So here is how easy this will go. We will create an interruption inside of the Arduino code that will detect the low pulse given by the Hall sensor.

**Dave Jones:** Using a time counter, we measure the time it takes the propeller to make a full spin, by measuring the time between each pulse given by the Hall sensor. If we know the time for a full rotation, we could easily calculate the time for

**Dave Jones:** just 1 degree, just by dividing the full time that we have just measured by 360 degrees. Great, let's imagine for this example that we want to draw a full line at 45 degrees. I will use this prototype on a PCB to show you first how this works.

**Dave Jones:** Each time we detect a low pulse of the Hall sensor, we will also reset a second counter, named a lapse loop counter, and that will give us the zero point. So we start with all of the LEDs turned off. Inside of the main loop, we will always count the time with the second loop counter.

**Dave Jones:** We know the time it takes to make just 1 degree, so we could easily obtain the time it takes to make 45 degrees, in this case, by multiplying that value by 45. When the elapsed loop counter is higher than 45 degrees, we turn the LEDs on, and after just 1 more degree, I turn them off.

**Dave Jones:** That will give us the full line of LEDs at 45 degrees while spinning. And since the system is synchronized each loop with the Hall sensor, we will always have the line at exactly 45 degrees. I first upload the code to this prototype made on a PCB.

**Dave Jones:** As you can see, I have the battery in the middle, the sensor on one side of the PCB, and the LEDs on the other. The Arduino will do all the fast switching of the LEDs. I place the magnet on my workshop table and start spinning the prototype with my drill,

**Dave Jones:** at a medium speed. I get the Hall sensor close to the magnet and there you go. I always have a line at 45 degrees because the Hall sensor will synchronize the time and also reset the counter for each loop. Now that we know the basics of a POV clock,

**Dave Jones:** let's build this awesome project. I've got my 8 green, 1 blue and 2 red LEDs. For each LED we will need a 100 ohm resistor to limit the current and also to make sure that we won't burn the LEDs. The prototype is built using a 3.3V 8Mhz Arduino Pro Mini

**Dave Jones:** due to its size and voltage. With this Arduino I could directly use a 3.7V LiPo battery cell with no external voltage regulator and that will simplify the project a lot. But after some tests, I realized that I need more than 8Mhz to make this project fast enough.

**Dave Jones:** For that, this time I will use the Arduino Nano with a 2S 7.4V battery connected to the VIN pin. We will also need a Hall sensor switch. I've used the A3144 Hall sensor. Make sure you use a Hall sensor switch, not a linear sensor that will give you a linear output depending on the

**Dave Jones:** magnetic field. Finally, we will need some drilled PCB, a sliding switch, wires and a 3D printed case that I designed together with some 8mm screws, nuts and bearings. If you don't have a 3D printer, you should manage to build your own prototype as I did in this example

**Dave Jones:** and build a support maybe out of wood or acrylic. Just make sure that the PCB propeller is well balanced and keep heavy components as centered as you can. This is the schematic for this project. Download it from a link below and have it in front of you while soldering.

**Dave Jones:** I've used my dear Creality CR-10 3D printer and 3D printed this case for this project. You have the files in the description below as always. These files include the main case, the back lid, the motor support, the two legs for the bearings and the top bearing supports.

**Dave Jones:** This should be the final shape of the entire project. Use M3 screws and nuts to fix everything in place as I did on this piece of wood. Let's mount the project. First of all, on a separated small drilled PCB that will fit inside of the case, I solder the 8 green

**Dave Jones:** LEDs in a straight line. Then the two red ones and finally the blue one. All the LEDs are sharing the ground pin, which is the shorter one as you can see here, where all the negative pins are soldered together. Then to each of the positive pins I solder a 100 ohm resistor.

**Dave Jones:** Once that is done, I solder a long enough wire that will later be soldered to the Arduino pins. I glue in place the PCB on the 3D printed case so the LEDs are facing the hole in the case, so we will see the light on the other side.

**Dave Jones:** Now I solder each LED wire from digital pin D2 to D12 as in the schematic. I also connect the ground wire. Now on a separated smaller PCB, I solder in place the Hall sensor with a pull up 1K ohm resistor between 5V and the signal pin

**Dave Jones:** and solder 3 wires for 5V, ground and signal. I glue the Hall sensor PCB on the other side of the propeller, with the sensor on the outside of the propeller. Finally, I solder the 3 wires from the sensor to ground, 5V and digital pin 13, which is the pin that will create the interruption.

**Dave Jones:** I solder the slide switch and glue it on the back lid. Connect the battery through a jumper pin so I could later take it out for recharge. I connect the other pin from the switch to the VIN pin and we are done. Now when I turn on the switch, the Arduino is powered.

**Dave Jones:** I've placed the 8mm screw through the hole with nuts and washers and tied the nuts. I also add two 8mm hole bearings that will be placed on this 3D printed support. The screw will also have a 3D printed pulley connected to a DC motor that will spin the

**Dave Jones:** entire propeller. On the bottom part of the support, I place this neodymium magnet close enough to the Hall sensor. That's it. Before we look over the code, we have to make sure that the propeller is balanced. Without touching the propeller, it should always be as horizontal as possible.

**Dave Jones:** Ok, so this is the finished POV clock with the code already uploaded to the Arduino Nano. Now let's look over the code that you could also download from a link below. Make sure you read all the comments in the code in order to understand it.

**Dave Jones:** This is the POV clock code. You also have the POV text display code below, but I will only explain this one. Ok, so first, read all this part where I define the variables that we will need, such as counters, time constants and so on.

**Dave Jones:** In the setup void, we prepare the registers for the pin state interruption. That will create the interruption service routine each time pin 13 in this case will change its state. Also, we define digital pins 2 to 12 as outputs and set them to low using these registers.

**Dave Jones:** We will use register control for this project instead of digital write, since in this way the switch will be much, much faster. Just as an extra example, in a new sketch I use digital write high on pin 3, followed by digital write low with no delay in between.

**Dave Jones:** Since the Arduino Uno works at 16MHz, this should create a very fast pulse. I upload the code and observe the signal on the oscilloscope. Now I do the same but using register control that will change the output value of any pin directly by changing the register value.

**Dave Jones:** As you can see, the time difference between those two examples is huge. That's because digital write is a pre-written function that takes a lot more to be executed. Ok, back to our code. In the interruption routine, we measure the time it takes to make a full rotation,

**Dave Jones:** counting the time between each pulse, given by the whole sensor on digital pin 13. In the void loop, we count the time that has passed since the last reset which occurred at the last whole sensor pulse. So we know the time it takes to make just one degree,

**Dave Jones:** so we could easily calculate how much time it takes to make any amount of degrees. Using another timer, we count seconds, minutes and hours. So for example, if it's 3 o'clock, we should have an hour indicator at 90 degrees. 90 degrees. So using an if statement, when the elapsed loop counter is higher than 90 degrees,

**Dave Jones:** I've turned on the green LEDs and after just one degree, I've turned them off. That should give me the line at 3 o'clock. That's it. You've got your POV clock. And by the way, this is not real time since the clock will reset each time you turn off the

**Dave Jones:** Arduino. If you want real time, just start the Arduino at exactly 12 o'clock and you're good to go. I mount everything inside of the 3D printed case, I upload the code and close the case. I power the POV clock and turn the DC motor.

**Dave Jones:** The speed shouldn't be too high but neither too low. There you go, I've got myself an awesome homemade POV clock. Pretty cool, right? You've got an example code for writing text as well in the description below. Download it and read all the comments in the code in order to understand how it works.

**Dave Jones:** It's more than the same as in this example, just turning on and off LEDs at a fast enough speed so your eyes won't tell the difference. I've first used the blue LED to create the perimeter of the clock. But I've made an error using the green LEDs for the lines, since those are not that bright,

**Dave Jones:** so I've decided to not turn the blue LED because that is so bright that you can't see the lines anymore. Here, in case of the prototype that I've made before, look how bright are the white LEDs. So there is definitely space for improvement for this project, maybe using white LEDs for the

**Dave Jones:** lines. So, we have learned how the POV display works, how to make one, how to use registers to control the digital outputs and how to manage pin change interruption and count time and get everything synchronized. Also, how to use a Hall sensor and a magnet to count each rotation speed.

**Dave Jones:** By the way, there is no battery charging included in this schematic. Probably that will be a future upgrade. For now, just unplug the battery for external recharge and you're good to go. If you like this kind of projects, check my Patreon page and support my workshop through there.

**Dave Jones:** I would really really appreciate that guys, since I spend a lot of money and time for each project like this. Also, check my Electro Noobs webpage for a lot of more tutorials and also my Q&A forum and create a new question there so me or any other member could answer it.

**Dave Jones:** I hope that you enjoyed this tutorial on POV display. If so, don't forget to click the like button like crazy and share the video with your friends. If you have any question about this video or any other, just leave it in the comment section below

**Dave Jones:** or on my Q&A page. Also, don't forget to subscribe and watch all of my other great tutorials. Remember, if you consider helping my project, check my Patreon page as well. Thanks again and see you later guys.
