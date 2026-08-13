---
video_id: AI0Q6-h3EGU
title: EEVblog #101 - Hacking your own Peltier LAB Thermal Chamber
url: https://www.youtube.com/watch?v=AI0Q6-h3EGU
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 22, "2": 41, "3": 61, "4": 77, "5": 100, "6": 120, "7": 143, "8": 156, "9": 170, "10": 197, "11": 218, "12": 234, "13": 253, "14": 266, "15": 288, "16": 299, "17": 316, "18": 336, "19": 357, "20": 375, "21": 396, "22": 409, "23": 428, "24": 466, "25": 484, "26": 501, "27": 514, "28": 530, "29": 554, "30": 572, "31": 595, "32": 614, "33": 625, "34": 643, "35": 658, "36": 679, "37": 702, "38": 716, "39": 735, "40": 753, "41": 772, "42": 790, "43": 800, "44": 818, "45": 829, "46": 853, "47": 865, "48": 891, "49": 911, "50": 923, "51": 949, "52": 968, "53": 984, "54": 996, "55": 1022, "56": 1034, "57": 1045, "58": 1063, "59": 1085, "60": 1102, "61": 1122, "62": 1134, "63": 1150, "64": 1167, "65": 1183, "66": 1202, "67": 1219, "68": 1235, "69": 1245, "70": 1263, "71": 1281, "72": 1299, "73": 1316, "74": 1326, "75": 1343}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, one of the more obscure items for any engineering electronics lab is a thermal oven, a thermal incubator. Now, not many people

**Dave Jones:** realize or even think about, they might know about it, but they don't realize that pretty much all electronic components are affected in some way by temperature, be it the input bias current of an op-amp, a voltage regulator, whatever spec you can think of,

**Dave Jones:** components will often change and drift based on temperature. And if you're developing a robust product that you want to sell to the market, it's actually quite important to actually test the product over the standard, say, the standard commercial temperature operating range, which is

**Dave Jones:** from zero to 70 degrees Celsius. And I thought it'd be really great if my, if the EEVblog lab had a thermal oven, and I don't have much room, and traditionally thermal ovens are quite large, big, huge items, and they cost many thousands of dollars.

**Dave Jones:** I've used ones that cost tens of thousands of dollars, very expensive, and, you know, often difficult to get item unless you get it surplus somewhere. So I thought about possibly building my own with one of these, just a small one with one of these Peltier devices or something like that, but I thought, nah, there's

**Dave Jones:** got to be something on the market. So I did some searching, and sure enough, I picked up a thermal incubator on eBay for a hundred, about 180 bucks Australian, and here it is. Check it out. It's awesome. It's a thermal incubator. It's actually designed, this model is actually called the

**Dave Jones:** Herp Nursery 2. Go figure. It's designed for hatching reptile eggs and, you know, chicken eggs and all sorts of eggs, and the exact same model is also available as a wine cooler as well. They actually sell it as a wine cooler and a stubby beer cooler and stuff like that, and let's

**Dave Jones:** check it out and see if we can mod it and see if it's a decent lab thermal oven. So here it is. Let me give you a quick rundown on it. As you can see on the bench, it's, um, I'm not sure the exact height,

**Dave Jones:** it's about 55 centimetres or something like that high, and it's got a nice carry handle on the top here, which is brilliant. It's got a temperature display in degrees Celsius only. I'm not sure if you can actually buy it in a degrees Fahrenheit model.

**Dave Jones:** It's got up-down temperature buttons. It's got a light internally. It's not very bright, but it does light up the internals. It's got a really nice clear polycarbonate window on it, so you can actually see what your items are in there. It's got a nice handle, and let's open it up, and inside you can see that it's

**Dave Jones:** got a nice seal, nice rubber seal around the edges. It looks like the polycarbonate window is actually like a double insulated type thing, and inside you can see the fan, and it's actually a Peltier-controlled device, as we'll go into, and it's got a little shelf which just lifts

**Dave Jones:** out, which you can put to different levels like that, and it's got a tray at the bottom that just slides in and out. Now you can actually take off this cover. It is actually quite hard, but I managed to get it off, and you can see the heat sink with the Peltier device behind it, and if you can see

**Dave Jones:** it, there's just a temperature sensor poking through up in there, so that's what it uses to sense the internal temperature of the chamber, and this sort of like an impeller, I'm not sure of the exact name for that, but this impeller type fan internally is just designed to circulate the air

**Dave Jones:** inside, so it keeps the internal temperature consistent throughout the chamber. It's a really nice design. I like it. And on the back here, nothing special. The model number is actually BCR25, so if you search for that you can actually find it. It is only 230 volts.

**Dave Jones:** It's claimed to draw about 65 watts during cooling, 55 watts during heating, and it also runs on 12 volts DC as well. As you can see, it's got a 230 volt AC input. It actually comes with a car cigarette lighter, so you can actually plug in 12 volts DC.

**Dave Jones:** You can switch between AC and DC, and it's got a normal and a mute mode for the fan. So if you're using it at night or something, and you want it to run a bit quieter, you just flick it to mute, and the fan actually runs a bit cooler.

**Dave Jones:** So let's crack it open and see what's inside. And I've taken the back off real easy. It just came out with half a dozen screws or so, and as you can see, the back panel is actually integrated with these nice little rubber feet here.

**Dave Jones:** It's got another external fan. As you can see, the huge Peltier device is actually under there. You probably can't see it, but it's tucked away down in there. Big heatsink on the back, and there's no surprises at all. Just a standard switch mode

**Dave Jones:** power supply. There's the AC-DC switch down there, and well, not much else. All a controller like this does is just switch the voltage to the Peltier device one way or the other, and it heats or cools based on a temperature sensor. Now there must be another controller up in the top here, so we might

**Dave Jones:** have to try and see if we can take the whole thing apart. But the only real concern I have with this is because the heatsink here, the back of the heatsink, is actually above the 240 volt switch mode power supply. If for some reason, I'm not sure if it does happen, but if you get

**Dave Jones:** condensation on this rear heatsink, it might actually drip down into the 240 volt power supply. But yeah, that remains to be seen, but something to watch out for. I've taken off four large screws in the back here, but down in these ridges down in here, it looks like it's actually been sealed somehow

**Dave Jones:** down in there, like a thermal kind of seal all the way around there. I can't actually get the camera down in there to show you, but it looks like you would have to actually crack that seal to actually get the thing apart. So I don't think I'm going to bother.

**Dave Jones:** And as it turns out, this front panel here just pops out. It's just held in with a couple of clips, and bingo! You can see there's four screws. There's two here and two here. You take those off and you can access the internal board.

**Dave Jones:** Well, after all the stuff falls out, fantastic! And if you can read that, it's Fasen Hanyi Computer Devices Code. There you go. Worldwidewebhanyi.com.cn. So a Chinese company. That's who obviously manufactures this under many different brands and names and different market segments, be it a wine or a beer cooler or an egg hatchery kind of thermal incubator.

**Dave Jones:** And let's take a look at the board, shall we? It just comes out with a couple of screws and no real surprises at all. 7805 voltage regulator. The two relays which are used to switch the voltage to the Peltier device, because that's all you have to do with a Peltier device,

**Dave Jones:** is just switch the voltage around like that, and you can heat or cool. So it's real simple. There's one main chip there. I don't recognize it, but yeah, it's probably like a maybe a custom little micro, obviously, something like that. There's a resonator, a resonator, there's a,

**Dave Jones:** there's the buzzer. That goes off to the NTC, and this one goes off to the internal LED. And that's all there is to it. It's pretty simple. And the good thing about the LED, check it out, here it is. It's just on a little board like that that just clips up in there.

**Dave Jones:** It's a really neat design. So if this, this thing isn't very bright, but obviously you can mod this real easy to any LED you want. Okay, let's actually give it a try. Let's operate it here. And you switch it on, and it first displays the set temperature.

**Dave Jones:** Then after a few seconds, it switches to the temperature inside the chamber, which here in the EEVblog lab, 18 degrees C. It only has one degree C resolution. There it is. It's dropped up somewhere between 17 or 18. And basically, when you push the temperature up or down button, that just sets the, sets the temperature set

**Dave Jones:** point. Now it can go down to 2 degrees Celsius at its lowest range, but that's going to depend on your ambient temperature. And on the high side here, it goes up to 60. So, and it stops at 60. So it's got a maximum range of 2 degrees, or maximum set point range of 2 degrees Celsius

**Dave Jones:** to 60 degrees Celsius. That's not quite the commercial temperature range of 0 to 70, but for a $180 buck chamber, beauty. I'll switch the fan over from normal to mute, and see if you can hear the difference. Here, here we go. So that's now mute, and it really is quite low.

**Dave Jones:** You could, I don't know if you could sleep with it in the same room or not, but yeah, it's pretty darn quiet when it's on mute. And it's not too loud at all when, when it's in normal mode. So I like it. Of course, one of the major things

**Dave Jones:** any good lab thermal oven needs is to get cables in and out of it. Because there's no point just putting your product in there and having to take cables out the front door, and trying to seal around that. That's crap. So it needs a test port.

**Dave Jones:** Now, what I'm going to do is take a standard 40 millimeter water pipe, one of these PVC joiner pipes, because it's a pretty good size for an IEC cable, plus other cables. So you need at least an IEC power cord to be able to fit through

**Dave Jones:** your test port, plus maybe some coaxes, and you know, other sorts of multimeter probes, and other sorts of test cables. So what I'm going to do is, I'm going to get a hole saw, and I'm going to drill straight through the side. I expect there to be some foam in there,

**Dave Jones:** so I might, um, do it as a, a two-step, uh, drilling process. But let's give it a go. Don't turn it on, tear it apart. Ha ha, let's go. Okay, I've drilled through just the outer case, and as you can see, here's the, uh,

**Dave Jones:** here's the internal foam. So that's pretty solid stuff. I like it. And as you can see, the hole saw cut out that, um, foam very nicely. It's a beautiful, beautiful cut. I, I thought it would, um, shatter or something like that, but it's a very hard cell,

**Dave Jones:** uh, foam. So there's the inner chamber, and all we have to do is drill through that one. Easy. And there you go, no problems at all. You can hole saw straight through it. You have to do it a bit, uh, slowly, but the foam is still in perfect, um, perfect condition.

**Dave Jones:** Now, because I, this is a 48 millimeter diameter, uh, pipe, I only had a 54 millimeter diameter, uh, hole saw, so it's going to be slightly too big, but I can, uh, fill that up with, um, some sort of, uh, silicon or something like that.

**Dave Jones:** So that's not a problem. Actually, I just realized I had another 40 millimeter piece here, which has some threading on the outside, and this actually fits in absolutely perfect. It's got a ridge right around the top here, and that just slides in, and it actually goes, it just sort of screws directly in place.

**Dave Jones:** So a 54 millimeter hole saw, spot on. I love it. Look at that. So now I've got a threaded port, so I can bring out something at right angles, or something like that if I need to. Fantastic. And as you can see inside, it just

**Dave Jones:** didn't, it just wasn't long enough to actually protrude all the way through, but I just put some silicon in there, and beautiful, we have a test port. Now, of course, adding a cable access port on the side like this is going to, um, obviously affect the thermal integrity of the chamber,

**Dave Jones:** and its performance isn't going to be as good. So how do you get your, how do you actually seal it up after you put your cables through? In the time-honored tradition of thermal chambers even, I've used this on a $50,000 thermal chamber. A rag!

**Dave Jones:** You just feed your cables through, stuff your rag in there, and it'll still be pretty darn close to its normal thermal performance. And let's try out the internal light. It's actually hard to see here, but let's switch it on, and it's pretty poor.

**Dave Jones:** It's, you know, it'd have to be pretty much pitch black, so that light's pretty useless. So if you really need a good light for it, I think that's begging to be hacked and put in a decent, um, high brightness, high luminosity LED. And I've made a quick mod to the LED.

**Dave Jones:** I've put a Cree Star LED on here to replace the other one, and the actual resistor up here, this is the one used up here, that's the series dropper resistor, so I've just paralleled that with another 330. Um, that should give it some extra brightness, so let's give that a try.

**Dave Jones:** And here's the Cree LED mod. Let's check it out. Piece of cake! Lights it up beautifully. Winner! Now the internal dimensions of the chamber, they're about 370 millimeters by 270 millimeters by about 220. And, well, what does that mean for real testing, real gear and stuff like that?

**Dave Jones:** Well, let's take our Rigol DS1052E oscilloscope, and it fits no problem at all. Heaps of room for the cable to come out the side. You can actually test, um, you know, bits of gear like an oscilloscope. Beauty! Now, just because equipment can physically fit in the chamber, it doesn't mean it's a useful

**Dave Jones:** test chamber if that equipment generates too much heat, um, to, which means the chamber can't get down to its, um, and down to, or up to, or usually down to, its, um, set point temperature. So we've got the Rigol DS1052E oscilloscope in here, it's just measuring the probe compensation, and, well,

**Dave Jones:** let's check it out. There we go, it's current, there we go, there's a reference, um, point, and it's currently at, uh, the ambient temperature, which is, um, 17 degrees here, and I've set it down to 2 degrees, and let's leave it for quite a while and see if it gets down to 2 degrees.

**Dave Jones:** I've come back four hours later, and, well, not really surprising, it doesn't work! Epic fail! 21 degrees! I've still got it set for 2 degrees, and, well, it just, the, uh, Rigol is just generating too much heat, it just can't handle it. Um, you know, I was hoping that maybe it might have dropped it, you know, 5 or

**Dave Jones:** something, but, nah, it's generating, uh, probably, I don't know, 20, 25 watts continuous, uh, power in operation, and it doesn't work, so, um, but we can certainly get it to work by, uh, switching the Rigol off, letting it cool down, and then instantly turning it on, and that's a way you can test, um, products

**Dave Jones:** that generate too much heat. Well, I've had the Rigol in there overnight for about 9 hours soaking, so it should have, um, really got down to the temperature. It got down to 3 degrees Celsius, and I have been tracking it with the, uh, Fluke reference probe here, and it is spot-on, my display

**Dave Jones:** up here, so that's pretty darn, um, it's about as accurate as you can get, really, um, with the single digit precision. But, yeah, it's been soaking for 9 hours, it's only rated to operate down to 10 degrees Celsius, this Rigol. Let's see if it works at 3 degrees.

**Dave Jones:** Okay, here we go, switching on. And, hey, lit up, and, yeah, there we go, we've got the welcome screen. Will it, uh, yeah, we've got a waveform, we've got no measurements. Let me, uh, turn those measurements on, and we'll take a look. Okay, I've turned the measurements screen on, I opened the door very

**Dave Jones:** quickly, it, um, actually retains, even if you open the door for a few seconds and poke around, it still retains the temperature. As you can see, it's, um, 4.5 degrees Celsius, so that's not, um, too bad at all. I opened that door, pressed a few buttons, and came back.

**Dave Jones:** But, there you go, the Rigol works down at, or it appears to work quite fine, down at, uh, 2 degrees. I'm not sure if it's going to meet its full spec, but, hey, it does work. And just for fun, let's do a quick test with some basic meters.

**Dave Jones:** I've got my Gossen metriwatt meter outside here. It's, um, I've been feeding in 10 volts, same voltage to all the meters. And inside, I've got a Fluke 875, which will be our reference, really. I've got a real cheap and nasty Vichy VC99. I've got the winner of the $100 shootout, the BK Precision.

**Dave Jones:** So, let's, I've, I've just put them in, so they're all measuring spot, a pretty close spot under 10 volts. So, let's drop the temperature down to 2 degrees, well outside their specced range, and see what happens. And the multimeters, they've been in there for quite a few hours now, and as you can see,

**Dave Jones:** there's really no difference. The Vichy has got down to 0.997, um, at one stage. It seems to jump around a bit, but, yeah, the performance is still reasonable. But, um, we have, we would have to sweep the multimeters over a much bigger, uh, temperature range to actually, um, see a performance

**Dave Jones:** difference. So, that was a bit disappointing, but worth a try. And I've let them ramp and soak up to 56 degrees Celsius, and these are the meters. The Fluke's still on 10, but the, uh, one hung low brand Vichy cheapy has, uh, drifted upwards, and the BK Precision is still holding in there at 9.99.

**Dave Jones:** And just for fun, let's actually test an Arduino board. Let's measure the 5 volt and 3 volt voltage regulators on it. At room temperature, this is currently at room temperature, 5.015 volts and 3.407 volts. Let's take it down to 3 degrees and see how much it changes.

**Dave Jones:** Okay, the Arduino has been in there for quite some time now, and, um, so it's definitely stabilized. As you can see, there's not much change at all. The 5 volt rail, 1 millivolt. That's all it's changed by, but that's got a good voltage regulator in that.

**Dave Jones:** But the 3.3 volt rail, there is some measurable change. Uh, it's changed by 5 millivolts, which doesn't sound like much, but is it allows you to characterize the performance, um, of this device over temperature. We've only done a 12 degree C, uh, temperature change here, which isn't much.

**Dave Jones:** So, um, you would ideally do it, say, from 5 to 60 degrees or something if you were actually trying to measure the performance, but that just gives you a quick indication of what you can do with a thermal chamber. You can measure all sorts of parameters

**Dave Jones:** of your circuits and your designs. It's great. And I've ramped the Arduino up to 57 degrees, let it soak, and there it is. And as you can see, the 5 volt rail hasn't moved, but the, uh, 3.3 volt rail has. So from that, uh, over the whole range, you can actually get, uh, performance data

**Dave Jones:** on that particular chip. And I wanted to check out its thermal performance suit too, so I got one of my, uh, Thermocron iButton temperature loggers, and here's the results I got. As you can see, um, overall, this is the overall response, and it looks like it actually rises up quite sharply,

**Dave Jones:** but I'll show you the positive and negative ramps, um, later. But you can see the general, um, shape of them going from ambient down to zero, from, um, well, ambient down to about 4 degrees in this case, 4 degrees up to about 58 degrees, stable at 58 degrees, and it actually,

**Dave Jones:** the thing about the thermal chamber is it does actually maintain its thermal stability quite well at 0 plus minus 1 degrees. So it's, it's pretty good for a chamber like this. I think it's really great performance. Now, let's take a look at the positive thermal ramp.

**Dave Jones:** Here it is. We've got degrees Celsius on the y-axis, and we've got minutes on the x-axis, and as you can see, it probably takes in the order of 90 minutes to do a full ramp from its lowest temperature up to its highest temperature.

**Dave Jones:** And if you look at the negative ramp, um, it actually takes longer to cool down from 60, from 58 degrees down to about 4 degrees. It, you know, it takes a good, um, two hours to actually get there. So as you can see with those thermal profile tests, it's,

**Dave Jones:** it's not a fast thermal chamber, but, you know, it uses just a Peltier device. It's not, it's not refrigerated, it's not a proper thermal chamber, but I think its performance is excellent for the price. It's more than good enough for, um, for you to have in your lab as, as a general purpose,

**Dave Jones:** um, thermal test chamber. I don't know how you could possibly get better value for money. It's awesome. So there you go, the BCR25 thermal chamber for 180 Australian bucks, and you can probably pick it up even cheaper than that. Um, I highly recommend, if you're serious about electronics,

**Dave Jones:** pick one up, because there's no way you can build one of these yourself with the polycarb window, the control, the excellent thermal insulation, the seals, the door, everything, the great carry handling case. You can't build one yourself for the same price. It's crazy.

**Dave Jones:** So get one for your lab, and you can test all your new circuits, equipment, all sorts of things over temperature. Can your latest design? Yeah, it might work at room temperature, but hey, does it play up at higher or lower temperatures? Get one of these babies and find out.

**Dave Jones:** Beauty.
