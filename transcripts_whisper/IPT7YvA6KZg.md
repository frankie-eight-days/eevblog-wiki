---
video_id: IPT7YvA6KZg
title: EEVblog #312 - Photocopier Teardown Follow-up
url: https://www.youtube.com/watch?v=IPT7YvA6KZg
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 16, "2": 32, "3": 48, "4": 68, "5": 89, "6": 113, "7": 133, "8": 153, "9": 170, "10": 190, "11": 206, "12": 226, "13": 242, "14": 266, "15": 283, "16": 303, "17": 319, "18": 343, "19": 363, "20": 384, "21": 400, "22": 428, "23": 444, "24": 460, "25": 480}
---

**Dave Jones:** Hi. Just a quick follow-up on the photocopier tear-down, because I forgot one thing. This paper feed mechanism, you know, the thing with the big springs that sits on top and you lift up and you can put the photos? Well, that's a complete mechanism

**Dave Jones:** in its own right. And I just lifted it off, complete with springs and everything, and I forgot to tear it down. So here it is. We've basically got another motor controller board in here with a huge stepper motor. So there's some interesting stuff in here

**Dave Jones:** as well. It's got the paper sort of, you know, feed tray here which changes it, you know, you can adjust the distance of the paper to be fed in. And it's got a controller board, another stepper motor, it's got some sensors on the back

**Dave Jones:** of that we'll take a look at, so just a little extra. Now this paper feed tray is interesting here. As you change this slider to adjust the paper width like this, it basically pushes these two plastic arms here, here we go, pushes these two plastic arms

**Dave Jones:** on a very nice little rolling cog system like that. A little linear cog system, not sure what you call it. And it basically puts this little plastic tab here in between a sensor as you move along. There's actually two sensors in there, you can see them there.

**Dave Jones:** And as you move it along, it will engage like that one sensor there actually corresponds to one paper point here, so no sensor at all corresponds to that paper point. Then the next paper point corresponds to the first sensor there being triggered. And then as you move it along,

**Dave Jones:** as you move it in like that, then you'll get two sensors triggered, and then as you move to the last position there, you'll get just that last sensor. And it's rather interesting that they actually, these sensors are pretty much standardized all throughout the photocopier.

**Dave Jones:** And inside here, and on here, they've got these paper flaps to indicate, you know, whether or not there's paper there. And when you push down on that, they had this, once again, the same optical sensors as well, plugged into here and here, and the wires

**Dave Jones:** going out there. And they could detect, once again, that lever. So as you press down on that lever there, or as the paper presses down on that lever, it either engages the sensor, or it doesn't. And I must have pulled out like a dozen of these

**Dave Jones:** little optical sensors throughout the entire photocopier. And they're pretty much standardized on them, and it'll basically contain an LED and a phototransistor. And you can see the little slit in there, and the slit in the receiving side over there. And if you have a look at this board here, you can see the diode

**Dave Jones:** symbol on there, and of course anode and cathode. So there's just got a diode on that side, and on this side, the emitter and collector of the phototransistor there. And it's actually a Roam 574. Now 574 might be familiar to you, because that's the wavelength of a

**Dave Jones:** green LED. But I don't think it uses a green LED, I think that's the model number. Let's Google it. And sure enough, you Google Roam 574, and you get the complete sensor system. It's a Roam photo-interrupter, and there it is. It's complete in the case with the

**Dave Jones:** mounting pins on it. And it's got a small slit, 0.5mm for high precision. It's designed for optical control equipment, fast response, well of course it's going to be. And it's got a built-in visible light filter as well. Forward current has absolute maximum ratings.

**Dave Jones:** Let's go down here and have a look at the characteristics. The forward voltage, typically 1.3 volts at 50 milliamps drive current for the LED. And as for the output characteristics here, we're talking 800 nanometers typical sensitivity. It doesn't give you a min or max, but as it has like a daylight, like a light,

**Dave Jones:** a visible light filter on it, it's not going to go too much lower than that. So that puts it up into the infrared category. So the LED would be matching infrared as well. And we've got another motor drive PCB down in here, and you can see the

**Dave Jones:** similar power package before, SLA7044M. Another couple of power devices there, you can tell by those center pins which are really trying to get the heat out from the die in there. And you could probably reuse that board in some way, shape, or form.

**Dave Jones:** But of course we have a beautiful, big, beefy stepper motor here, which goes into a belt system in there, through another sensor, there's another one of those optical sensors, you can see it clipped into there. They're standardized all the way throughout the photocopier.

**Dave Jones:** Another clutch there, I think there's another clutch down the bottom here as well. They're all over the place. And if I try and get this mechanism apart, it might require a bit of percussive maintenance maybe, but it should just sort of slip off somehow

**Dave Jones:** off all these clutches. Maybe I've got another screw in there. And of course there's always a screw you forget that's hidden away in there. And these things are just absolutely amazingly designed. There's so much that goes into them. We've got another couple of

**Dave Jones:** clutches down in here. Does that pull off? Anyway, we've got another clutch here, we just take off this plastic bit there, and it slides straight off. So there was another at least three clutches in there. Beautiful. They're a, they're an Ogura again, clutch

**Dave Jones:** Co, a Mic 5 NE, 41, 24 volt DC, 3.7 watt clutch. Beautiful. And there's quite a few in there and all the cogs and stuff like that, if you're into those sort of things. And now I can probably get the stepper motor out too.

**Dave Jones:** Here comes the stepper motor. Ah, yeah. Now we're talking. Here we go. Look at this puppy. What have we got here? That looks like we've got an Astro Syn, I think it is, stepper, 23 KM KO36P5V. And that looks really really beefy. I like, looks like

**Dave Jones:** you can really do some cool stuff with that. And of course when you're ripping these out, don't throw out the cables as well, because they often use weird-ass connectors that you'll need. So definitely salvage the cable out of these things. Once you undo the screws to this thing,

**Dave Jones:** you can see the big roller inside there with the big rubber pads on there to really grip the paper nice and solid. And on this side of the mechanism here, we're in for a bonus. Three solenoids. Fantastic. And there we have it. Three solenoids.

**Dave Jones:** These photocopiers are a goldmine. You've just got to imagine how many engineering hours went into just designing all this solenoid and paper handling mechanism and the cogs and the gears and everything else. It's just absolutely incredible, all the clutch systems. Ah, this is

**Dave Jones:** just the top paper handling mechanism. Incredible.
