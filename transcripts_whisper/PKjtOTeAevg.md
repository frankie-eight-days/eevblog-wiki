---
video_id: PKjtOTeAevg
title: EEVblog #776 - World's Smallest Digital Dosimeter
url: https://www.youtube.com/watch?v=PKjtOTeAevg
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 16, "2": 36, "3": 52, "4": 68, "5": 80, "6": 96, "7": 116, "8": 128, "9": 140, "10": 152, "11": 172, "12": 192, "13": 212, "14": 228, "15": 248, "16": 264, "17": 284, "18": 300, "19": 316, "20": 332, "21": 356, "22": 372, "23": 392, "24": 412, "25": 432, "26": 452, "27": 468, "28": 488, "29": 516, "30": 536, "31": 552, "32": 568, "33": 584, "34": 600, "35": 616, "36": 636, "37": 660, "38": 676, "39": 692, "40": 712, "41": 724}
---

**Dave Jones:** Hi, check it out. This is the world's smallest digital dosimeter, i.e. radiation meter slash Geiger counter, you could say. And here it is compared to an Australian 50 cent piece. It's absolutely tiny. Thank you very much to Andrey Bikinov who sent this in.

**Dave Jones:** And yes, it's full open source hardware. Woohoo! And it's got a sexy little display. It's called the Ultramicron. Let's check it out. It's in a tiny little case here. It's got a little micro USB on the side, which is used for charging and also for extracting

**Dave Jones:** the data, because it's a data logger. Even when the thing is switched off, it's actually continuing to log the radiation data and we can actually display it. This is the latest firmware built in the thing, and it's got statistics that can measure the internal battery voltage

**Dave Jones:** and the 360 volt high voltage that'd be for the Geiger-Muller tube in the side. It tells you the current up time, it's been going for 50 days, so you can just leave the thing running. I believe it's got like a 12 month battery life or thereabouts.

**Dave Jones:** And a simple three button interface. Shame they're not actually labeled here, but this is, you know, sort of like a almost prototypy kind of thing. And we can go back to the main screen here, and it shows our dosage level in this case micro rutgens per hour.

**Dave Jones:** So it's not the more usual micro sieverts, but it's an easy calculation to convert. It'd be nice if he added a software option to display both actually. We've got a little battery gauge there, and just an ongoing graph of this thing. It's brilliant.

**Dave Jones:** Love the little display and that little backlit dot matrix. And as you might have heard, it does have a vibration motor in there. So if I turn it on, if it goes over, there we go. A little vibration motor. And you can set it up so that the alarm goes

**Dave Jones:** off or it vibrates when it goes over a certain limit. And you can hear a slight beep every time it gets a tick on the thing as well. And there's a setup menu. We can actually get in here and we can set various things up.

**Dave Jones:** We can reboot all the data log in, and we can turn our vibration on and off if you, you know, wanted to extend the battery life as long as possible. You turn the vibration on the sound if you didn't want to do anything.

**Dave Jones:** You can set up a timer, sleep timer, and the alarm level once it hits a certain radiation dosage. So that's not just a current value, but that could be a cumulative value. And it shows the current value up there, plus your daily dose as well.

**Dave Jones:** So it really is quite neat. And you can switch between the weekly dose and the radiation maximum. Nice 10 minute dose. I really like the display on here. It really gives it like a solid segmented look. You can see this little grid in there,

**Dave Jones:** so it almost looks like that's a proper segmented display rather than a dot matrix. Really quite neat. Apparently that display is from a Nokia 2760. And here's the schematic. And yes, all in Russian of course down here, for those who can read their Russian.

**Dave Jones:** Fantastic. But we've got an STM32 processor in here. We've got ourselves a flyback step-up which is going to be generating our normal 360 volts. He's got 400 volts here, but I think it actually measures it. And that flyback pump there is being controlled of course, switching there, controlled via the

**Dave Jones:** micro here. And it doesn't look like he's tapping off the actual 400 volts and actually dividing that down at all. It looks like the detection's coming from the primary side over here, lower voltage going into the micro down here. And our micro USB input,

**Dave Jones:** all the requisite stuff here. We've got ESD protection and then of course the 5 volt comes into our little battery charger. It's just a microchip job, pretty standard. And then we've got ourselves some regulation down here. So that's generating plus 3 here, and then we've just got a

**Dave Jones:** charge pump inverter over here which gives us negative 3. There's the vibration motor with its own little MOSFET driver, no problems there at all. Not much happening, we've got else happening. We've got dual crystals here, 32 kilohertz watch crystal of course for the long-term data login.

**Dave Jones:** As I said, it can probably go for like a year in low-power mode actually logging. We've got another transistor driver for the buzzer over here. And the Nokia 2760 LCD display, too easy, that's just an I2C type serial interface. And I don't know what sensor is

**Dave Jones:** used over here, we'll find out in a minute, but that's just tapping via a 10 meg up to the 400 or 360 volt rail. And then AC coupled and just giving an impulse into a transistor and the impulse, that just converts it to 3 volts and

**Dave Jones:** goes into your micro. So it can detect the pulse from the Geiger multitube, too easy. And it's got a full parts list as well. And here we go, our sensor is an SBM-10. Well let's crack this puppy open and see what's inside. Woohoo!

**Dave Jones:** Now because this thing is continuously running, I've got to be careful here and he does warn me that I shouldn't touch anything inside because there is 360-odd volts have we got. Yeah, looks like we might be able to crack something. Whoa, open there.

**Dave Jones:** It's alright. Here we go. Ta-da! Oh, there we go, we've got our battery stuck to the back. And there is our Geiger multitube down in there. Fantastic, look at that. And that's a nice little bit of fit to envelope design there. Got a cut out in the board around here for our little

**Dave Jones:** Geiger multitube and of course the right angle micro SD. We've got a 100 milliamp hour battery in there, tiny little lithium ion job. There's our flat flex connector down there for our Nokia LCD. That's all doing the business very nicely, I like that.

**Dave Jones:** And what else we got? That looks like our surface mount one of our surface mount crystals, our STM micro of course. And it's all just very nice, I don't know what else to show you. I won't go much further. Of course there's our vibration motor

**Dave Jones:** there, you can see the counterweight there just spinning around. That's actually really quite a decent one, you can really feel it when this thing vibrates, let me tell you. But of course all the magic happens because of this Geiger multitube here. We might be able to actually lift that out a tad.

**Dave Jones:** We've got our piezotransducer under there, but yeah, it's not much else. Really nice bit of work to get that into the world's smallest digital dosimeter. I love it! And I suspect also that these little pins sticking up here and over here are designed to keep

**Dave Jones:** the board stuck down when like pushed down to the right height, nice and snug so it doesn't rattle around when you put the lid on. Crude, but effective. The only real radiation source I have in the lab here is a smoke alarm which of course contains one microcurie

**Dave Jones:** of americium. So yeah, these are well, the ionizing smoke detectors do. And as you can see, we were getting like 7 or 8 background before of micro rutgens per hour, but now we're like up to 28 or something. So you know, it's quite significant.

**Dave Jones:** See the decent spike there. So it's unusual that the display sort of shifts in this direction. I would have preferred it to shift in the other direction, but anyway you can see how we had the background before and now it's really spiked up there.

**Dave Jones:** Neat. So it works. If I hold it right on top, I'm actually getting as high as 35 now, so that's pretty decent. Now americium-241 here, it's primarily an alpha particle emitter. It does emit some gamma radiation as well. And the Geiger molecule is primarily, I believe, this particular model

**Dave Jones:** gamma radiation. And the alpha particles of course will be shielded by, you know, thin stuff. You know, paper, like any real, any object or anything like that. Beta particles need, you know, like tinfoil or something like that. And ionizing gamma radiation, well that needs

**Dave Jones:** you know, lead, like big thick, you know, stuff or you know, a meter of water or something to stop it. It requires big bulk mass. But yeah, these little alpha smoke alarms I mean, you know, you wouldn't stick them, you wouldn't strap them under the side of your head, but they're

**Dave Jones:** generally not too bad. And I've hooked it up to my USB port. I had to install an STMicro virtual com driver, so it's using like a serial port interface. I've selected COM3 here. Unfortunately I can't speak Russian, so I don't know what any of this means, but I am actually

**Dave Jones:** reading the live data out of it, and hopefully I might be able to extract some of the data out. Because this thing's been running since he sent it to me, and of course it's been up in a plane at high altitude, you know, 30,000 feet

**Dave Jones:** or something, so that it's going to get a lot more radiation up there. So we should be able to see that, actually, if we could download the logged data from it. And if it passed through any airport x-ray scanners or other stuff, for example, then we might be able to see some spikes

**Dave Jones:** there. But yeah, my Russian's a little bit rusty. But here we go, I hit this button here, and it looks like it's downloading something. So let's see what happens when she gets to 100%, shall we? Hopefully it's in, you know, some Excel file

**Dave Jones:** or a CSV file or something like that, perhaps. But we'll see what happens. Here we go. Oh, here we go, we got did we get something? Here we go. Look, we got something. So this is pretty good. I like this. This is today, of course, it's the 4th.

**Dave Jones:** And if we go back, we can see that it's been just sitting, it's been sitting in my lab here for a while though. Unfortunately it doesn't seem to go back any further than that. Aw, that's a bit disappointing. I was hoping to see, I was hoping to see something.

**Dave Jones:** It was definitely shipped before that, I'm sure. But you can actually see today where I had it sitting next to the smoke alarm there. I had it sitting there for a couple of hours. I actually went to the gym and then went home and came back and

**Dave Jones:** finished this video off. So it was a couple of hours there, and it was sitting like you know, right next to it. Or right on top of the smoke alarm radiation source. So that was the regular background before I put it close. And now it's like it's dropped back down to like

**Dave Jones:** 8. So you know, it's just the natural background radiation. So that is the Ultra Micron. That is one very cool little gadget. I love it. The world's smallest digital dosimeter. Fantastic, thank you very much Andre for sending that in. And yes, full open source hardware and

**Dave Jones:** I'll provide a link to the GitHub repository down below. We can download all the details for it. Fantastic. I'm not sure if he actually sells it or not. So if you liked it, please give it a big thumbs up because that always helps a lot.

**Dave Jones:** If you want to discuss it, jump on over to the EEVblog forum and leave YouTube comments. Catch you next time.
