---
video_id: Gr6gBjDxP5M
title: EEVblog 1653 - Alkaline Battery Leakage Testing 2 - Electric Boogaloo
url: https://www.youtube.com/watch?v=Gr6gBjDxP5M
source: youtube-asr
timestamps: {"0": 0, "1": 10, "2": 22, "3": 37, "4": 49, "5": 63, "6": 72, "7": 85, "8": 91, "9": 105, "10": 121, "11": 140, "12": 152, "13": 164, "14": 175, "15": 185, "16": 196, "17": 209, "18": 218, "19": 229, "20": 239, "21": 255, "22": 264, "23": 275, "24": 286, "25": 300, "26": 316, "27": 326, "28": 336, "29": 353, "30": 367, "31": 380, "32": 393, "33": 403, "34": 414, "35": 428, "36": 436, "37": 446, "38": 457, "39": 471, "40": 492, "41": 502, "42": 524, "43": 534, "44": 544, "45": 562, "46": 575, "47": 585, "48": 611, "49": 619, "50": 627, "51": 638, "52": 658, "53": 672, "54": 682, "55": 691, "56": 702, "57": 711, "58": 725, "59": 743, "60": 755, "61": 770, "62": 779, "63": 791, "64": 802, "65": 819, "66": 830, "67": 842, "68": 852, "69": 865, "70": 877, "71": 885}
---

**Dave Jones:** Hi, it's battery leakage time again. Ah, you remember my battery leakage test? This was many years ago now, and it basically failed. I got a whole bunch of different brands of batteries.

**Dave Jones:** I put them under a constant load of 1K or something. I can't remember exactly what it was. And basically none of them at all leaked. I couldn't get it to leak.

**Dave Jones:** And of course everyone has their favorite theory about why it didn't work and how it wasn't the right load and you know, all sorts of things, but like nobody had any concrete evidence of the best load to actually get batteries to leak or what under what best conditions.

**Dave Jones:** Everyone knows, you know, obviously if you leave them in the most valuable bit of kit you've got, then they're guaranteed to leak. So, it's not like I can get my most valuable calculators out and put the batteries in and hope they leak.

**Dave Jones:** No, not going to happen. So, anyway, that was a miserable fire, but I've still got the original batteries and you'll notice that they have eventually leaked. But this is many many years later, right?

**Dave Jones:** I've got Well, no, these ones didn't leak at all. I still got the original tubs that I had them in. This was back in the old lab when the old lab that got flooded, if you remember that.

**Dave Jones:** Here here you go, Duraleaks for you Duraleak fanboys. But these ones down here didn't. So, yeah, all those Duracells have eventually leaked. So, many years later I have done a follow-up video on this actually showing this.

**Dave Jones:** So, this is not the first time I've shown I'm not going to take them out. I'm not going to take an absolute mess. Here, make a mess on the bench here.

**Dave Jones:** But yeah, you can see Varta leaked as well. Once again, Duraleaks. Okay, Ultras. Yeah, okay. So, of course it's going to leak out of the negative end cuz that's where the seal is.

**Dave Jones:** That's the you know, the black ring, you know, you can see around there. Anyway, yeah, let's try it again. Because I was contacted by a viewer who guarantees me that he's got a just happened upon a circuit which guarantees leakage.

**Dave Jones:** It's happened every single time that he's actually done it and it's turned into a he reckons it's a battery leaking machine. And that yeah, it's like within like 30 days, 40 days or whatever of putting batteries into this circuit, it leaks.

**Dave Jones:** So, I've built it up here and I thought that hey, I'll give it a go. I've always thought that given that a constant resistor load on the battery didn't work, then I thought you know it maybe like it's a pulsed load or something like that perhaps.

**Dave Jones:** So, anyway, this is kind of like a pulsy load but kind of not really as you'll see in a minute. Thank you very much Logan Lack who came up with this is not the complete circuit here.

**Dave Jones:** It's actually three triple five timers and believe it or not I couldn't get couldn't find a stock of triple five timers in my lab here. I thought I had some but apparently I didn't.

**Dave Jones:** So, I had to go scrounging. I I did find this double 56 from way back like in my like original stock here like in like like the dust on these, right?

**Dave Jones:** These come from like the 1980s if you have a look at maybe some of the date codes and 93, 87, you know, like some like real original stuff like I had when I was a kid.

**Dave Jones:** I found a double 56 which is a dual triple five timer and then I found a scrounged one. Oh, insert a video here showing you how I scrounged this one.

**Dave Jones:** So, yeah, I didn't have to race to Jaycar to buy some triple fives. And I went searching for a 555 in a bunch of old boards and what do you know?

**Dave Jones:** Look at this, the only eight pin dipper on here is a 555. Woah, I'm not sure you can see that. Look at that and it's socketed. Winner winner chicken dinner.

**Dave Jones:** I've got a 556. So, that gives me the three 555s I need. Beauty. Yeah, got an old school double 5 6. Don't know what that date code there is on that uh double 5 6.

**Dave Jones:** Anyway, genuine TI. Both are genuine TI jobbies. So, basically, three 555 timers. And the circuit that he's got here is a classic uh astable 555 uh timer uh configuration uh and doing three LEDs, red, white, and blue here.

**Dave Jones:** USA. BUT ALSO, AUSTRALIA. AUSSIE, AUSSIE, AUSSIE. OI, OI, OI. Cuz for those Yanks who don't know, red, white, and blue is also the color of the Australian flag. Beauty.

**Dave Jones:** None of that Yankee rubbish. Um anyway, uh 555 uh timer here just powered from four uh AA batteries uh in series. Uh 680 ohm uh driver for the LEDs.

**Dave Jones:** And basically, basically, three different uh astable um circuits uh driving a red, a white, and a blue LED here. So, basically, identical circuits just three times over. Um so, yeah, uh 10 mic here.

**Dave Jones:** Um a 470 10 mic and 470k basically give us a 0.15 hertz. So, as you can see here, they're flashing slowly. Got them powered from uh 6 volts. Um interestingly, I thought this was very low.

**Dave Jones:** 130 ohm uh discharge resistor cuz pin 7 is the uh discharge pin. So, very heavy uh discharge uh current here. In fact, when this thing discharges, it's going to pull the current through the 130 ohm through the discharge transistor down to ground.

**Dave Jones:** So, this circuit's actually going to draw more when it's in the discharge half of the cycle than it is um uh for the LEDs here. So, it's going to draw a lot more current.

**Dave Jones:** And you can actually see the uh live current up there. There you go, 64 milliamps, 88 milliamps, 91, 65. It's going to drop back down. And if I actually uh of course, these are going to get like out of order.

**Dave Jones:** They're going to be asynchronous due to uh you know, 555s aren't precise. Go figure. Um like the internal uh threshold volt variations in the internal threshold voltages of the 555, variations in the value of the resistors, and the charge cap here.

**Dave Jones:** So, but if we restart that again, you'll find that they all synchronize, no worries. And the blue looks white, but trust me, it's actually blue. It's just overexposed. But they will eventually get Yeah, there you go.

**Dave Jones:** They're already kind of like unsynchronized already, just due to variations. So, and interestingly, these two down here are from the different You might think cuz they're on the same die that they're synchronized.

**Dave Jones:** They're not. They're actually on different dies. They're different chips. So, there you go. That's the variability in 555 timers. So, we're getting like this varying pulse kind of thing from the battery.

**Dave Jones:** But yeah, sorry. You'll Let me restart that, and you'll notice the current up here. Right? It'll start out. That's just the LED current, 17. Okay? Cuz we're not in discharge, so only 17 milliamps.

**Dave Jones:** And then when it enters discharge mode, like boom, 88. And then when they start turning on, you'll get sort of like it'll drop a bit, and you'll get variations on that depending on how many LEDs are on and which one's in discharge mode.

**Dave Jones:** So, yeah, I found that 130 ohms didn't work at all. And of course, with such a low discharge resistor value, you're going to get like a 50 50 duty cycle, basically spot on.

**Dave Jones:** So, yeah, I found 130 was too low. These things didn't work at all. They only worked for like one cycle, and then stopped working. I had to up this to 180 ohms before they would all work.

**Dave Jones:** So, yeah, I've got 180 ohms in there at the moment. You can see that there. I've got the 470 K. I've got the 10 mics in there. And Bob's your uncle.

**Dave Jones:** I duplicated that three times. There's the schematic for the 556 with the different pin numbers there. So, one and two, one, two, six, and five, and four, for example, they're all the timer one.

**Dave Jones:** And 13, 12, eight, 10, and nine are the pins for timer two. Basically, they're all on one side. So, along the bottom side there is timer one, along the top side there is timer two, and you got power and ground down there like that.

**Dave Jones:** So, um yeah, very simple circuit that we got here. Um and let's just play around with the uh threshold voltage here. Now, of course, the triple five timer uh only operates down to 4 and 1/2 V Well, the the NMOS version of the CMOS version goes uh lower, but the uh NMOS version um only operates to 4 and 1/2.

**Dave Jones:** So, I expect the Let me adjust the sup My mouse is dead. So, let's actually adjust the voltage here, and you'll see it should work down to Well, it should work down to 4 and 1/2.

**Dave Jones:** Yeah, it's still going at 5.6. Just. Take it down to 5.5. Will they come back on? It's struggling. Don't build this circuit, folks. But, I want to duplicate it exactly because he's had multiple brands of batteries, multiple times, every single time they have leaked.

**Dave Jones:** So, I don't know. There's some magic sauce here in the discharge curve of this thing that's that's just causing them to leak, but that's what I want to test.

**Dave Jones:** So, let's take it down to five. So, maybe this is the very low discharge value that we've got. Five? Is five still going to Five isn't going to work.

**Dave Jones:** I I didn't test this enough. There you go. They're they're not going to go back on at five. So, that 130 ohms is a real killer. So, why would these LEDs actually uh stop oscillating even though we're still at the operational voltage of uh well above the 4 and 1/2 V operational voltage of these chips?

**Dave Jones:** Well, uh with this low value discharge resistor in here, remember there's a there's a discharge transistor in here, okay? And I think that is being uh that has such a high voltage on it due due the large current.

**Dave Jones:** It's not a great discharge transistor in there. It's not designed for uh uh these high currents and uh you can't actually find a maximum current in the data sheet, at least I couldn't, um for the internal um discharge transistors.

**Dave Jones:** You can get the output current, which is a couple hundred milliamps, uh but the discharge transistor, noopsie. Um anyway, uh so 130 ohms. So yeah, if the if the voltage drop across this pass transistor is too high, then the discharge voltage is never going to get low enough for the output to then re-toggle for for that flip-flop inside to go flip-flop and then um now flip.

**Dave Jones:** And then uh the output goes high and it changes state and it keeps oscillating. So if we actually measure that voltage, so let's let let's do that. Where's it?

**Dave Jones:** Pin seven. So so we're talking the red LED here. So the LED's on. So there's our 6 volts. So it's not dropping anything cuz it's And then, bingo, there you go, 1.15 volts.

**Dave Jones:** That is a lot. So that is So if we drop our voltage, right, then due to the internal threshold voltages, let let's go down to 5 volts where it's going to stop.

**Dave Jones:** Yeah, it's right. It's it it stopped now. There you go, 1.78. 1.78. NO wonder it's stopped um oscillating. So yeah, there So there's your problem. So what we can do is we can actually um physically remove that and we can Let's whack in a 100k resistor, okay?

**Dave Jones:** So we'll get practically no voltage drop across that and it's instantly started to work again and that will work and that'll work down to 4 1/2 volts. Pretty sure that will continue to operate.

**Dave Jones:** Yeah, at 4 1/2 volts it might even go below that, but now we're in the uncharted and we're out of spec. It might even go down to four, maybe.

**Dave Jones:** Memory from when I was a kid playing around with this sort of stuff. Yeah, at about about a volt per cell. Yeah, it's it's kind of still still hanging in there.

**Dave Jones:** So I might actually mod I might actually keep that modification because um we're still got the heavy discharge current from the two other LEDs over here. So, I might actually just keep that so it's like an indicator.

**Dave Jones:** So, that it indicates uh so that when I come in to check the experiment is still going, um it'll still work down to at least a volt per cell there.

**Dave Jones:** So, yeah. Um can it go even below that? Oh, 3.8. Woah! Woah! Come on! You can do it. Yes! It still goes even though the operational voltage is 4 1/2 volts.

**Dave Jones:** So, I think I'll keep that I think I'll make that modification to the circuit. Fingers crossed I don't goof it, right? But yeah, that that that's why you can't um see those uh that's why the other ones have stopped oscillating because the threshold voltage internally with the 555, you remember the triple five timer has the 5K 5K and 5K resistor.

**Dave Jones:** A lot of people say that's where the number comes from, but uh um the 5K 5K 5K and that sets the internal threshold voltages for the where it turns off and on.

**Dave Jones:** Um and yeah, with that huge voltage, and you'll notice I can measure that again, and you'll notice that we'll get naff all. Two three millivolts. Three millivolts. Because there's hardly any discharge current cuz it's still 100K this time, right?

**Dave Jones:** So, the transistor's turning fully on and there's no uh saturation voltage on that uh transistor. It's bugger all cuz there's bugger all current flowing through it. Bonjour mesdames. It works.

**Dave Jones:** So, I'm going to keep that modification. So, let's see. Um anyway, thoughts and comments down below. I'll go get go to local shopping center. I'll get some brand new Duraleaks, and I'll whack these in here.

**Dave Jones:** Um maybe if I can set up like some sort of uh you know, leakage cam or something like that, I'll try and do that so you can actually watch it live over the next I'll get back to you in like a month or two, and we'll see if these things leak.

**Dave Jones:** If they do, then I'll build up this circuit in bulk, um and then we'll we'll test a whole slew of brands of batteries. So, as unlikely as this circuit seems to be, because it's essentially like just a constant once it gets on the below a threshold and it stops blinking, it's just like a constant discharge um current.

**Dave Jones:** But, who knows? Who knows about the chemistry of the batteries and what best to cause and under what humidity conditions and other things and and then you got the batches of the batteries as well.

**Dave Jones:** If you just happen to get a good batch, it's never going to work. I mean, that could have been my problem all along is that I said, "I but I had like what, eight different brands or something?" And none of them none of them failed with the constant resistor on there.

**Dave Jones:** So, that's essentially what you're putting on this thing when you um when you actually do that. So, I you know, once it gets down to a low enough voltage, but who knows?

**Dave Jones:** Maybe the time maybe the changing currents, the pulsing currents, cuz that was always my thought is that, you know, some sort of like pulsating like high pulsating high pulsing current or something like that.

**Dave Jones:** But, yeah, but once again, it takes a long time to experiment with stuff like this. And I've got a viewer who absolutely assures me. He sent me photos and said, "Yeah, multiple battery it's leaked every single time." I'm going to go for it.

**Dave Jones:** So, I'm going to get some Duracell's. Going to get some Duracell's. Going to go down to the shops. I'm going to get some brand new Duracell's. I'm going to whack them in.

**Dave Jones:** And uh I'll get back to you in like a month or two. Catch you next time.
