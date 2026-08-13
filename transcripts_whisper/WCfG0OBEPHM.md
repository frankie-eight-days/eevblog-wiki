---
video_id: WCfG0OBEPHM
title: EEVblog #519 - Ardusat Arduino Based CubeSat Satellite
url: https://www.youtube.com/watch?v=WCfG0OBEPHM
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 19, "2": 39, "3": 54, "4": 70, "5": 84, "6": 95, "7": 116, "8": 131, "9": 150, "10": 171, "11": 186, "12": 203, "13": 220, "14": 235, "15": 252, "16": 265, "17": 286, "18": 300, "19": 314, "20": 335, "21": 352, "22": 367, "23": 379, "24": 397, "25": 410, "26": 427, "27": 445}
---

**Dave Jones:** We've found Jonathan, also from Freetronics. And he's got the ArduSat board, the satellite board. Yeah, this is the payload processor module, which is one of the parts of ArduSat-1 and ArduSat-X. Those are two satellites that are currently at the International Space Station and they're just about to be deployed into orbit.

**Dave Jones:** And this is the board that will run experiments. Each one of these little rectangles is a complete microcontroller with all the supporting parts. And so each one of these is essentially equivalent to an Arduino Uno. In fact, it's running the Arduino bootloader. And this chip up here is a supervisor processor, which talks to each of them through multiplexes.

**Dave Jones:** So as far as they are concerned, they're an Arduino plugged into a computer and the supervisor can load new sketches onto them. And each one of these has access to all of the sensors on the satellite. And there's also some storage and various other things on here.

**Dave Jones:** The idea is that each of these runs totally independently. So you can have 16 experiments running simultaneously and they don't need to have any knowledge of each other. And the idea with that is that we can amortize the cost of the satellite across a whole lot of different people.

**Dave Jones:** And I've got a few other boards here as well. So just as an example, this is a little test stack that I've been playing around with on my bench. And this is representative of about the size of the final satellite. It's a 10 centimetre cube.

**Dave Jones:** And you can see in the middle there is the payload processor module. There's another one of these. There are currently five of these boards in existence. Two are here, two are in orbit right now, and another one is over in California at the ground station.

**Dave Jones:** This on the top is a prototype of a satellite power supply module. So it's got input from solar cells so it can charge. It's got a management processor so that it can do things like measure current consumption and battery state. And so it's got a couple of high current switch mode power supplies on here

**Dave Jones:** which supply power to the rest of the satellite through the bus. The satellite has a stacking bus that you can see there. So basically the idea is that it's like a stack of pancakes. So the satellite itself is just a series of modules that you build up and they all sit on the same stacking bus.

**Dave Jones:** And how do you keep it warm? Because it's in space! Well, the interesting thing is that keeping it warm is not really so much a matter of space being cold. It's more a matter of how do you control the heat. There are really three ways that temperature can be transferred between different parts of the system.

**Dave Jones:** And there is no convection because there's no air obviously, but you still have radiation. So if you have hot spots you can radiate heat. Basically the thermal profile of the satellite once it's in orbit, it orbits about every 92 minutes and it goes from about minus 40 degrees to about plus 80 degrees over that cycle.

**Dave Jones:** So basically the board is slammed down to minus 40 degrees and then it's slammed up to plus 80 every hour and a half. So it goes through something pretty severe. It's still within tolerances. It's still within a designable range. Exactly. It's not ridiculous.

**Dave Jones:** So the problem is that when it's on the dark side of the Earth, so when it's in shadow, it'll be radiating heat and then once it comes into sunlight it starts absorbing heat. Right. And it's just a matter of managing that. Excellent. The major problem is batteries because we all know batteries don't like getting cold.

**Dave Jones:** So what a lot of satellites do is have heating coils under the batteries. So when they're on the dark side they heat up and they keep the batteries warm. And what's the uplink to this thing? How does it communicate back to you? There is a radio module I don't have on this particular stack,

**Dave Jones:** but the satellite itself uses 2 metre and 70 centimetre ammeter transceiver modules in it. So in fact all of that information is published. So if you've got the right gear you can listen in on the telemetry. It's not encrypted or anything. And how do they deploy it?

**Dave Jones:** Do they just toss it out the window? Almost. They are deployed using a device called a P-POD, which stands for Poly-Pico-Satellite Orbital Deployer. And it's basically a big box with a spring in it and a door on the front. So what they do is the CubeSats go inside the P-POD,

**Dave Jones:** which is mounted on a slate on the end of a robotic arm on the space station. So they basically point the arm in the right direction and then release the door and the spring pushes them out. Pushes it out? Yeah. That's it? That's it.

**Dave Jones:** Awesome. So they take on the same velocity basically as a space station. Right. And then the orbit decays over about six months or so. Oh, six months. Yeah. They've got no propulsion so they can't actually change their orbit, but they have orientation control using things called magnet talkers,

**Dave Jones:** which is basically three big coils. So they react against the Earth's magnetic field. So essentially it just acts like a compass. Oh, because there's no friction you don't need. That's right. There's no friction. So all you do is you energize the coil and you can rotate.

**Dave Jones:** Oh, no way. Yeah. It's one of those things when you hear about it, it's like, oh, it's so obvious. Of course. I wouldn't have thought of it. Exactly. Yeah, with magnet talkers you can get about plus or minus five degrees pointing accuracy. Wow.

**Dave Jones:** And you can do that for any mass in theory. Yeah. That's right. Right? Exactly. And you do that on spacecraft, do you? No, that is done on a lot of satellites. Oh, on satellites. Otherwise it's done with reaction wheels. So basically a motor with a mass on it and you spin the wheel and then the spacecraft rotates in the opposite direction.

**Dave Jones:** Here I was thinking that they all use hydrazine fuel for their orientation. No. But one of the limitations with CubeSats is for safety reasons, they don't like you sending up anything that could be explosive or dangerous in any way. They have to go up totally inert.

**Dave Jones:** So they're not allowed to be powered up until after they have been deployed. All right. Interesting. Does that only apply to CubeSats? Only applies to little players or do the big players get a free pass? It really depends on how the deployment is happening.

**Dave Jones:** Yeah. So the thing is that CubeSats are pretty much second class citizens when it comes to space tech. So they're hitching a ride with other missions. If you're the primary mission, then you can specify what you want and it's done to see your requirements.

**Dave Jones:** Got it. There are some CubeSats now that are experimenting with active propulsion systems as well. Excellent. And people can upload their own sketches to this as well, can't they? Exactly. That's right. Fantastic. Sketch in space. Yeah. So there's a software tool that runs in your browser.

**Dave Jones:** So it's an IDE in the browser and you can plug your own Arduino into your laptop, test that your experiment works and then there's a little drop down and basically it says deploy to. You can deploy to your Arduino or deploy to satellite.

**Dave Jones:** Nice. It sends it via the internet to the ground station and it's then uplinked to the satellite and then it's loaded onto one of these processes and executed. Then the results are sent back to you. Did anyone think about putting a camera on it so that you can see real time that your LED's blinking?

**Dave Jones:** No. No. There are cameras on the satellite but they're not pointing at the board. Oh, right. Not pointing back at itself. Oh, right. Excellent. Thanks, John. I hope it works so it's being deployed in the next... Well, we don't exactly know. It's in the work queue for the astronauts once they get around to it.

**Dave Jones:** The way it works is there's no specific schedule. They have a list of things to do and they get through a certain number each day. So sometime in the next month or two they'll be deployed. Fantastic. All right. Good luck. Thanks. NASA Jet Propulsion Laboratory, California Institute of Technology
