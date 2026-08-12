---
video_id: QVAQONKyMv8
title: EEVblog #368 - EPIRB Teardown
url: https://www.youtube.com/watch?v=QVAQONKyMv8
source: youtube-asr
timestamps: {"0": 1, "1": 21, "2": 32, "3": 40, "4": 64, "5": 82, "6": 91, "7": 115, "8": 125, "9": 148, "10": 164, "11": 177, "12": 190, "13": 210, "14": 225, "15": 236, "16": 261, "17": 275, "18": 294, "19": 310, "20": 320, "21": 328, "22": 346, "23": 355, "24": 372, "25": 387, "26": 406, "27": 419, "28": 428, "29": 442, "30": 461, "31": 478, "32": 491, "33": 505, "34": 517, "35": 533, "36": 548, "37": 561, "38": 577, "39": 589, "40": 604, "41": 616, "42": 633, "43": 646, "44": 661, "45": 681, "46": 705, "47": 717, "48": 727, "49": 741, "50": 761, "51": 778, "52": 805, "53": 828, "54": 860, "55": 875, "56": 887, "57": 904, "58": 919, "59": 940, "60": 964, "61": 986, "62": 1008, "63": 1022, "64": 1044, "65": 1056, "66": 1069, "67": 1079, "68": 1091, "69": 1108, "70": 1119, "71": 1139, "72": 1158, "73": 1170, "74": 1182, "75": 1198, "76": 1208, "77": 1225, "78": 1234, "79": 1251, "80": 1270, "81": 1284, "82": 1304, "83": 1315, "84": 1336, "85": 1345, "86": 1362, "87": 1372, "88": 1384, "89": 1395, "90": 1410, "91": 1421, "92": 1445, "93": 1455, "94": 1478, "95": 1498, "96": 1514, "97": 1540, "98": 1561, "99": 1575, "100": 1591, "101": 1604, "102": 1624, "103": 1637, "104": 1647, "105": 1664, "106": 1690, "107": 1704, "108": 1721, "109": 1745, "110": 1757, "111": 1776, "112": 1798, "113": 1814, "114": 1832, "115": 1861, "116": 1878, "117": 1892, "118": 1905, "119": 1922, "120": 1930, "121": 1942, "122": 1963, "123": 1977, "124": 2006, "125": 2029, "126": 2037, "127": 2057, "128": 2073, "129": 2092, "130": 2106, "131": 2120, "132": 2132, "133": 2149, "134": 2158, "135": 2169, "136": 2179, "137": 2192, "138": 2208, "139": 2216, "140": 2223, "141": 2239, "142": 2252, "143": 2262, "144": 2277, "145": 2297, "146": 2317, "147": 2333, "148": 2353, "149": 2371, "150": 2386, "151": 2407, "152": 2421, "153": 2436, "154": 2450, "155": 2465, "156": 2477, "157": 2497, "158": 2507, "159": 2520, "160": 2537, "161": 2552, "162": 2567, "163": 2586, "164": 2606, "165": 2620, "166": 2638, "167": 2651, "168": 2663, "169": 2677, "170": 2697, "171": 2721, "172": 2736, "173": 2757, "174": 2781, "175": 2798, "176": 2813, "177": 2824, "178": 2839, "179": 2856, "180": 2879, "181": 2899, "182": 2916, "183": 2926, "184": 2944, "185": 2957, "186": 2971, "187": 2985, "188": 2997}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. You don't have to worry about me getting lost in this video because I've got an EPIRB or an electronic position indicating radio beacon. One of these emergency beacons that you carry when you're hiking or you're out boating or something like that.

**Dave Jones:** If you get lost, get in trouble, you know, you're about to die, flick the antenna, push the big red button, and hopefully somebody comes to rescue you. Well, that's the plan anyway.

**Dave Jones:** I actually know quite a few people who've been rescued by one of these things for in under, you know, when they're hiking or canyoning or doing various things like that.

**Dave Jones:** Very popular little devices and life-saving devices. This is the older model EPIRB. This is the MiniSat Alert personal EPIRB from KTI. It's an Australian company designed and built here in Australia, designed for our local regulations cuz all countries use have different regulations for these things.

**Dave Jones:** This is actually an EPIRB, but they're also known as PLBs or personal location beacons. EPIRBs are traditionally designed for the marine environment. They can be self, like, floating, self-righting with an antenna, and self salt water activated and all that sort of stuff.

**Dave Jones:** This one is designed to carry in your backpack when you're hiking or something like that or maybe on a little boat or something like that. It's not a marine one.

**Dave Jones:** It's a personal locator beacon effectively. So, this is the older model 125 MHz. There it is, 125 MHz 243 MHz analog system. They've actually phased this out now, so I think if I activated this, I'm probably not going to get rescued here in the lab.

**Dave Jones:** In fact, the signal probably wouldn't get out of the lab here. You have to have pretty good conditions for a, you know, fairly open sky for these to be picked up by the satellites.

**Dave Jones:** Now, this one's compatible with the COSPAS-SARSAT satellite system, and it's the older analog system. The newer digital system is 406 MHz, and that sends out a digital digital signal in addition to a if you've got a GPS equipped unit, it can send out your exact GPS location.

**Dave Jones:** But, this one, even though it's analog, it I think the search and rescue helicopters, when they come out to rescue you, still have a 121 MHz {point} 5 MHz radio location finder on them so that they can pinpoint your location.

**Dave Jones:** Because when you activate one of these, and you the signal is picked up by the satellite, and they triangulate your position, it is very rough. You know, they can't actually get your exact location from that.

**Dave Jones:** So, when they call the helicopter, they fly out, and then they use a radio finder in the helicopter to narrow down your exact location. So, that's why these That's with these older analog ones.

**Dave Jones:** But, the newer digital ones, they can send out your exact GPS position, bang, they know exactly where you are, sends out a digital code that you pre-register, and they know who owns it, and they can contact your family to get additional info of exactly where you've gone, and all that, what equipment you're carrying, all that sort of thing.

**Dave Jones:** This is the older analog one. We're going to tear it down. Could be quite interesting. I wonder what's inside this thing. It's waterproof, it's shockproof, it's got a 10-year lithium battery in there.

**Dave Jones:** But, I hope I will try not to set the thing off. Let's go. And I've got to thank Julie Burton, who's a canyoning friend of mine for giving me this unit for the teardown.

**Dave Jones:** She doesn't need it anymore. It's an old one she used to carry on her canyoning and hiking trips. So, thank you very much, Julie. Now, as I said, it's a KTI manufactured by Kinetic Technology International here in Australia, made in Australia, not Austria, and its battery has expired July 2011, but it's still going to work because uh basically these have a 10-year lithium battery in here.

**Dave Jones:** I think this has a C-size a C-size lithium battery in it and they will typically have a 10-year shelf life, but they specify the replacement time as half of that or 5 years.

**Dave Jones:** So, this one would have the battery would have been installed and it was probably manufactured around 2006 or thereabouts, hence the July 2011 replacement date. And it is the Mini Sat Alert Personal Personally 121.5 MHz 243 MHz analog system.

**Dave Jones:** And there isn't really much to them at all. They're very simple units. They've got some instructions on the back here how to operate. Break the seal by raising the aerial and then fully extend upright.

**Dave Jones:** Press button until red light flashes. On land, place in a cleared area away from people and obstacles. At sea, attach beacons to your buoyancy vest. And there you go.

**Dave Jones:** And of course, it's got a test mode which we can try out because it doesn't transmit in that mode. And as you can see, it hasn't been used. Julie's never used this thing.

**Dave Jones:** Break seal to raise aerial because the whole idea of these is hopefully you never have to use it. Cuz if you have to use it, well, you know, it's going to cause a lot of grief to somebody, especially yourself if you've done an injury or something like that.

**Dave Jones:** So, it has never been broken because if you want to use it properly, you just extend the antenna up like that and push the button and it will transmit, but it has a test mode.

**Dave Jones:** If the antenna is down like this, we can just press it. Here we go. There we go. So, presumably it does like an actual self-test and maybe you know, actually transmits internally but not to the antenna.

**Dave Jones:** It disconnects that of course cuz you don't want this thing to actually transmitting to the antenna just for the test. So, maybe it's got a system in there that actually transmits the signal, something that reads it back and then verifies it.

**Dave Jones:** So, I'm guessing that there's a micro controller in here or something that uh That's fun. There you go. And so, yeah, it's probably got a micro in here to do that self-test functionality cuz I'm sure the self-test is just more than flashing an LED, you know, and the battery's working.

**Dave Jones:** I think it's probably a bit smarter than that to make sure that it's still operational. Anyway, it's got a lanyard here on the bottom. You open it up so you can attach a lanyard.

**Dave Jones:** Warranty void if broken. We love that stuff and uh and apparently you can these are repairable and you can replace the batteries in them. So, presumably there's a screw under there.

**Dave Jones:** If we undo that and that will probably pop that bottom off, probably a ring sealed around there but only one way to find out. Let's void this warranty. You bloody ripper.

**Dave Jones:** Here we go. There we go. There's the screw. Tada! Let's open this sucker up. And presumably there will be a uh some sort of way to detect that that antenna is down as well um because oh, wait, there we go.

**Dave Jones:** Look at that. Oh man, check that out. Okay, so that obviously goes right up through there and goes into that metal thread. I think I can see like a a metal threaded insert up there.

**Dave Jones:** So it goes all the way through and probably keeps it all together like that. So that's rather interesting. This one doesn't There we go. Yeah, two of them. Got two long rods.

**Dave Jones:** Oh that Yeah, there we go. We got some O-ring seals on there and presumably it comes apart. Maybe I have to break off this tape around here or something.

**Dave Jones:** There's the antenna by the way. It is an extendable antenna like that. So I'm pretty sure we won't transmit on this thing if we just disconnect the antenna and it's not going to get out of the office anyway, I think even if the antenna was extended.

**Dave Jones:** So we should be able to measure the output of this thing. So let me let me actually take this tape tape off cuz I think that's probably holding the two halves of the case together.

**Dave Jones:** Ta-da! Be able to It's a bit springy. It's springy but it is coming loose. See the copper shield in there? Well, I was expecting this board to be bigger but check it out.

**Dave Jones:** It's not that big at all. All circuitry is under that uh what looks like copper shield there and there's the looks like two C size batteries down in the bottom.

**Dave Jones:** Yeah, here it comes. It's just going to pull out. That's it. Too easy and there's our piezo transducer down there that makes the beeping noise when we test the thing but jeez, it's not much to it and I was spot on with the date.

**Dave Jones:** There it is, May 2006. 5 years replace 5 years after the date of manufacture. So, we've just got two C cells. Looks like it maybe has some protection stuff in the top.

**Dave Jones:** Let's have a look at the board, which is rather interesting. The first thing to note is a standard PC test socket here. These are for 2 mm uh probes.

**Dave Jones:** You can You can buy these from Digikey. They're just off-the-shelf stuff. I've looked at these Looked at using these before, and they're designed for 2 mm like actual uh like They're at the exact width of your multimeter probe.

**Dave Jones:** So, it can just plug directly into that. So, and look at that spring there. They've got this little Well, I It's not actually It's kind of like it It looks like it's a spring, but it doesn't do anything in that respect.

**Dave Jones:** That is clearly the sensor that is used in to detect whether or not that antenna is up or down. So, maybe it's some sort of uh you know, capacitive uh coupling thing or or something like that.

**Dave Jones:** Because when you raise that antenna, it's not going to physically uh move that spring at all. And it is electrically connected. Is that Is that grounded there? Looks like that point is grounded.

**Dave Jones:** They may still be using that as a capacitive coupling system through to the antenna. So, the circuitry may sense the antenna and uh measure that first before uh you know, switching on a solid-state relay or something like that to output the RF signal to the antenna.

**Dave Jones:** So, there's something going on there. It's rather unusual. And there's our 121.5 MHz crystal, which is used for both frequencies, of course. The other one is uh just double that frequency and yes, it is held down with a some sort of epoxy adhesive or something like that cuz this is designed to be shockproof.

**Dave Jones:** So, we can easily just slide that off there and bang, we've got our board out of there and of course, that is all O-ring sealed down in there cuz this thing is waterproof to like 3 m.

**Dave Jones:** So, it's got various O-rings over the place and it's rather nicely designed and we've got our board to take a look at that. We have to get rid of that shield.

**Dave Jones:** No problem. Should be easy peasy to get off. Just heat up the copper. I could cut it of course, but easier just to heat it up with the iron and then just pull it off.

**Dave Jones:** No drama. Got to have that third hand and I'm trying to get it on camera here, so ah. Hey, trying to get things on camera. Never works. Ta-da. And here's the board and as predicted, there's the microcontroller.

**Dave Jones:** It's a Motorola MC68HC705 with its own local oscillator is at 20 MHz, I think. Oh, is that could even be two No, that's 2 MHz. There you go, it's running at 2 MHz.

**Dave Jones:** And the rest of it is pretty much all analog slash RF stuff. There's the There's the button, of course, which the test slash activate button from the front and here's the antenna output up here and the crystal actually connects to the other side there.

**Dave Jones:** So, there's the two points for the crystal. So, there's going to be an RF oscillator by around here somewhere based on these transistors. These are all going to be uh transistors of some description and they've got to modulate the signal as well as well as double it because it has to be doubled to that 243 MHz as well.

**Dave Jones:** So, that's clearly all done in the analog domain, which I guess is not really surprising because there's not, you know, why do it digitally really? I mean, the new 406 MHz digital PLDs PLBs, of course, would be much more complicated and high-tech in terms of digital control and stuff like that, but in the end, it's just got to have 121.5 MHz oscillator.

**Dave Jones:** It's got to have a doubler in there to generate the alternate frequency and some sort of modulation thing probably. I don't know, happening around here perhaps that this would be the RF transmitter.

**Dave Jones:** I would suspect based on the size of the device. It's physically larger. These things output, I believe, an RF signal level of about 150 mW or something like that.

**Dave Jones:** So, you know, it's not terribly high in the scheme of things, but they obviously need that slightly larger output transistor there to do that. And the rest of it is I I would presume that's modulation cuz that sort of comes from the microcontroller down here into this area around here.

**Dave Jones:** So, it's probably got some switches and some probably another local oscillator or something to modulate the signal on top of that, but uh yeah, there you go. It'd be interesting to see the schematic of this thing.

**Dave Jones:** You could, of course, reverse engineer it. It's only a very simple uh double-sided board, but it would take a significant amount of time. So, but if anyone has a schematic for one of these things, um please post in the comments cuz it would just be interesting to see the uh arrangement that they've used to get one of these things working.

**Dave Jones:** So, there's not much really left to tear down on this thing. That's pretty much it. So, we may as well activate it. Let's go. So, what am I going to do with this is I'm actually going to uh eventually like uh disconnect the antenna cuz I don't want to accidentally transmit 121.5 MHz at uh full power even if it is inside the lab here cuz I believe uh

**Dave Jones:** commercial airliners can still pick up um this distress uh frequency. I'm not sure if they still actively monitor it or or not, but they have the capability to do that and have done in the past in case the uh satellites don't actually uh capture them, but um what we can do is we can hook up a scope to the antenna output here and we can capture um we can

**Dave Jones:** have a look at the waveform and uh capture the signal. So, what I'll do is I'll do it first with the antenna down and we'll see if it's actually transmitting anything to the antenna at all and then we'll actually disconnect the antenna um and then activate it again um and then it should do its full activation and we should be able to capture the uh output signal and take a look at it.

**Dave Jones:** Now, I just uh noticed this. I'm pretty sure as I mentioned this is the output power transistor here driving. We've got a trimmer cap here just driving the antenna here, but look, then we've got it AC coupled.

**Dave Jones:** The output to the antenna here is AC coupled and it goes into this separate transistor arrangement over here, which as I said that metal bar there, um somehow capacitively detects whether or not uh that antenna is raised up or not.

**Dave Jones:** So, I think that's what that circuitry there is doing. It actually detects whether it So, the microprocessor before it uh starts to transmit, it probably reads at the antenna.

**Dave Jones:** It checks to see if the antenna's down. If it is, it goes into test mode, and it probably does that via that circuitry there. And it looks like it just goes straight back into a pin of the micro.

**Dave Jones:** Okay. So, what I've done is I've reverse engineered this little section around here with what looks like uh two transistors and that AC coupling cap to the antenna there.

**Dave Jones:** And unfortunately, it's not very exciting at all. Here's the antenna. It's got a um inductor on the output. This is the RF transmitter section. And it's uh it picks off that, AC couples it.

**Dave Jones:** There's a diode clamp there to ground. There's a voltage divider there driving an NPN transistor with a capacitor on the output going directly to the pin on the microcontroller, which presumably, of course, has an internal pull-up resistor.

**Dave Jones:** That's all there is to it. So, they've clearly split this board into two halves. Here's the RF uh oscillator stuff around here, all in this section, and then the RF transmitter up here.

**Dave Jones:** And it's clearly divided by these digital lines running through here like this. And the only coupling between this part of the circuitry on the left here and the RF part on the right is the um part we mentioned with that detection circuitry with that AC coupling cap picking off the signal from the antenna.

**Dave Jones:** And the other one is this little resistor in here, which couples this part, which I believe is the modulator, over to this RF section over here. and that's really there's another control signal coming in here like this in there.

**Dave Jones:** So, there's a digital control signal there and that probably shuts the transmitter off and on or does something. Perhaps it's another maybe it's a digital modulator some sort of uh test thing.

**Dave Jones:** Maybe it's got something to do with uh injecting a signal to test that the antenna's up or something like that. I'm not entirely sure. There's probably something else which looks like it run another control signal runs into here something like that.

**Dave Jones:** That's probably to switch between the two frequencies or something. So, there needs to be a control line coming from the micro. You can see that there and then this resistor going into this part of the circuitry around here and as I said this is the oscillator part of it here.

**Dave Jones:** So, that's probably the control signal. Scope time. Okay, I've hooked up the scope to the antenna output here and watch this. I can make it come and go. There we go.

**Dave Jones:** That's my 50 hertz AC coupling from the antenna. I put my hand on the antenna there and whee there we go. Isn't that fun? Absolutely nothing to do with the operation of this thing but just thought I'd show you that.

**Dave Jones:** It's neat. All right, let's see if we can capture something in test mode here. I have no idea what it's going to give out or do anything at all or how to trigger.

**Dave Jones:** That's why you got to experiment with these things to find out. So, I've got the channel one connected to the antenna output there. Single shot capture. We've got 100 milliseconds per division horizontal and one volt per division vertical set to trigger just above that.

**Dave Jones:** So, eh let's give it a go. Let's press the button and uh see if we can trigger something. Up, there we go. We got something. There we go. We got a spike and then boop another little another little So, that's clearly above 1 V per division.

**Dave Jones:** So, let's set it to 5 V per division and try that again, shall we? Here we go. Let's set the trigger point a bit higher. There we go, about 2 V or something.

**Dave Jones:** And trigger. Bang, there we go. So, at 5 V that's that's the battery voltage. Clearly, it's applying something to the antenna there. So, let's do that again. Let's go for a longer time base.

**Dave Jones:** 500 ms per division. Let's try it again. Push the button. Bang, bang, bang, bang. There we go. We got a bunch of pulses. We got that first one, positive.

**Dave Jones:** Got another one going negative there. I'm not That's a huge Is that something? Yeah, it's something's going on in there. We've got an RF packet. There we go. This sampling's quite poor cuz the memory depth isn't uh long enough here.

**Dave Jones:** This thing hasn't got enough memory at 4 meg uh 4 meg sample memory. But, that is uh we can have a look at that in more detail later cuz that is quite high.

**Dave Jones:** So, I can set our trigger level higher than that and capture just that RF packet. All right, so we've got the whole thing on the screen here and this is like the switch-on pulse, presumably when it like switches on the RF stage or something like that.

**Dave Jones:** So, that's just a spike as we saw. It's, you know, there's nothing much doing there. But, then we've got this RF pulse here. We've got another one here, here, here, here.

**Dave Jones:** So, it does five RF pulses, by the looks of it, and then presumably switches the antenna off again. That's what happens in test mode. All right, let's see if we can capture this RF waveform.

**Dave Jones:** So, I've set it to 5 V per division. Now, the trigger level um at about 10 V. So, because we know that that start and end pulse only went to 5 V.

**Dave Jones:** So, we want to trigger above that only on those RF pulses. I've gone faster on the horizontal, 100 microseconds per division. So, just as a rough guess. So, let's go to a single shot capture mode.

**Dave Jones:** Let's do that. I'll press the test button. Bang! We captured it. Too easy. There you go. So, it looks like it's about 10 15 V. This is when 1 megaohm input impedance, by the way.

**Dave Jones:** I haven't got this like 50 megaohms input impedance. So, there's the waveform. If we zoom in and we'll turn on some measurements. Bingo. 100 25.5. I think if we got in there a bit more precise, the frequency counter on this thing isn't the greatest from the measured data.

**Dave Jones:** So, there you go. But, that would be 121 .5, of course. And if you have a look at the length of the burst here, 5 microseconds per division, 5 10 15 20.

**Dave Jones:** It's about 23 microseconds or thereabouts RF burst at 121.5 MHz. Let's capture that again at a much faster time base, 10 nanoseconds per division. Bang! It's still only It's still saying it's 124 .5 MHz.

**Dave Jones:** It's not 121 .5. That's interesting. So, maybe it offsets. It looks like that is the true frequency there. So, it it is offsetting that, I guess. So, it doesn't um, transmit on the 121.5.

**Dave Jones:** So, it tests it at 124.5. So, with this coupling circuit here, I think what's probably happening is that when that, uh, grounding bar is close to the antenna, of course, it's got more capacitive coupling.

**Dave Jones:** So, when it does those, um, test burst transmissions there, it, uh, there is some capacitive coupling and the amplitude is enough to either, um, presumably, uh, like, not or switch on or switch off of this transistor, which the microcontroller can detect at those lower, um, 23-microsecond, uh, time burst time periods, which we looked at.

**Dave Jones:** So, it turns on the RF transmitter and sees, and this circuit just picks up, um, a a the coupled AC coupled signal from the antenna, which the antenna's characteristic is going to change depending on whether or not the antenna's vertical or whether or not it's laying flat right against this grounded bar here.

**Dave Jones:** Now, what I'm going to test is that modulation point down Well, well, what I thought was a modulation point coupling over to the RF, um, stage. So, I'm going to probe that at the same time as doing the test signal.

**Dave Jones:** So, let's give that a go. Let's, uh, uh, single shot capture mode and press the test button. Bang! And way, there's the Woohoo! It's way up there. Let's, uh, change channel.

**Dave Jones:** Looks like we've got to go down in channel two. So, there you go. Let's Let's try that one more time for the dummies. Bang! There we go. Look at that.

**Dave Jones:** That is, uh, 5 V per division. So, that point sits at five Uh, it could just be coupling over. So, I'm not sure what's going on there, but uh clearly that could just be coupling possibly between Yeah, obviously it's going to do that.

**Dave Jones:** It's probably going to couple over. So, I'm not sure whether or not that green channel two signal's controlling that or vice or it's just coupling over. It seems to be sitting at 5 volts and then just and then just couples it.

**Dave Jones:** It seems to step down a bit there. So, let's go out and uh at a longer time base and let's try and capture that again. And there we go.

**Dave Jones:** I captured that at a long time base and you can see what's happened. There's a slight change in that point there after the RF burst. So, there's It's kind of doing something in there.

**Dave Jones:** I'm not exactly sure what. I'm not exactly sure what that's telling us at this stage, but oh well, it's interesting. Now, what I'm going to try is probe the output of that circuit that I reverse engineer, which goes back to the micro there and I know that this is a you know, a 5-volt logic input signal, so I can set my vertical scale to 1 volt per division.

**Dave Jones:** So, I'll probe that and let's have a go. Let's see what we can pick up. Once again, when we do the test thing. And single shot test. Boom, test mode.

**Dave Jones:** Bang, there we go. So, Aha! Aha! Can you see what I see? It goes from 0 volts to 5 volts and back down there, but there's also those green pulses that correspond with the RF burst.

**Dave Jones:** So, let's once again, zoom in on this. There we go. There's some uh that's just coupling. That's I think we've coupled in some uh noise there. That's our antenna earth lead there, just picking up some of the RF, but that is supposed to be a digital signal if I probed that properly.

**Dave Jones:** Anyway, let's uh single shot capture that again. Going to test mode. Boom. There we go. So, it drops down low. So, that's So, that's actually detecting. So, that's pulling it low.

**Dave Jones:** So, it's detecting that there's that RF signal there. You see how it only goes low? Let's have a look here. See how it only goes low after the yellow the yellow RF amplitude there has ramped up to enough signal level that it actually detects and then bang, it goes low.

**Dave Jones:** And trust me, all that waveform there is just RF pickup. That's a That green signal's actually a digital signal. And just for those who don't believe me that the that green signal there is being picked up by this antenna earth lead cuz that's pretty much what it is when you're talking about RF stuff, I will get rid of that.

**Dave Jones:** Bugger that off and we'll use our little um high frequency ground probe on there. They're a bit tricky to sort of hold in place, so I won't probably won't be able to get it on camera at the same time, but uh let's give that a go with exactly the same conditions and see what we get.

**Dave Jones:** Actually, it's not too bad at all. Look at that cuz they've got that convenient uh via there that the ground connects into, so let's keep that on there and then we'll single shot capture this waveform again.

**Dave Jones:** And single shot, turn push the test button, and there we go. Much reduced. We're still picking up some crap on there, of course, but as you can see, it's much cleaner now and if you didn't believe me before, you will believe me now that where you can see where once this RF amplitude ramps up to a certain signal level, that switches on the transistor here.

**Dave Jones:** Once it gets to a certain signal level, that transistor switches on. It's just an open collector output with a pull-up resistor there. So, it switches low like that once it gets to the level and that the microcontroller can then detect that there's RF on the output.

**Dave Jones:** So, I can detect it's testing there that the RF transmitter works. And now, let's probe this point in the circuit where a digital line comes from the microcontroller somewhere into that RF section.

**Dave Jones:** So, I expect that to be some sort of gating pulse for the RF oscillator. Let's give it a go. And there you have it. It is some sort of gating pulse for that RF transmitter there.

**Dave Jones:** Once again, I've got the antenna earth lead back on, so we're picking up crap here. It's actually a digital It's truly a digital signal here. This is a pain in the ass trying to probe You know, if you're looking at signal integrity in an RF design like this, probing is absolutely everything.

**Dave Jones:** I mean, look at that. You would think that there's something wrong with your design when you get all this on it. If you don't actually know what's happening with your probing.

**Dave Jones:** Anyway, it's clearly some sort of gating pulse, but there's a long time there. By a long time, I mean like, you know, 7 8 microseconds or something before it by the time that goes low before the RF transmitter actually switches on.

**Dave Jones:** But, it it is certainly some sort of gating type pulse. And there's another digital line which comes across over here like this. I'm not sure which way it goes, of course, but uh I'm going to prove that under the same conditions again and see what we get.

**Dave Jones:** Press the test button. Bang, no, we're just getting noise on there, so it doesn't seem to be doing anything at all, really. That's quite boring. Not at all happy with that.

**Dave Jones:** There we go. We've got it doing something now. There we go. Okay. It's doing Okay, we've got a much longer time base there. So, it's it does something over here when it switches on and then and it's really it is doing so it is some sort of test signal which is rather interesting.

**Dave Jones:** Let's have a look at the frequency of that. 1.475 kHz there. Now, this is interesting when the you can just see the yellow RF pulse there switching on. This changes frequency from changes frequency from Actually, it's going down.

**Dave Jones:** It's going down. Hang on, I don't have to probe that anymore. What am I doing? I No, it's 700. Look. It's going up in frequency as I go along.

**Dave Jones:** As I scroll this back to the start if I go all the way back, look. It's going up in frequency. So, that's the modulation tone. There you go. That is the modulation the decrease in modulation tone bingo from the microcontroller.

**Dave Jones:** So, the microcontroller is doing that in software. It starts out at about 1.4 kHz. So, bingo, we have found the modulation signal for they use this for the homing.

**Dave Jones:** It's a decrease in modulation signal on the carrier. It starts off at 1.475 kHz. Let's call it 1.5. And then it slowly decreases in frequency. It's going down and down and down.

**Dave Jones:** 1 kHz da da da And then it goes all the way down to when the RF switches on, bang, there it is. That's where the uh you can see the yellow pulse there.

**Dave Jones:** That's the RF burst we've been looking at. So, it gets down to 700 Hz. So, it goes from 1.5 kHz down to 700 Hz. That's all being software driven, software timing in the micro.

**Dave Jones:** And then, bang, after the RF burst there, then decreases again. And of course, it goes through that five times. And but this is only the test mode, by the way.

**Dave Jones:** So, it we'd expect to see operational differences when we're actually transmitting a real signal. So, that's probably all signals. I was hoping to find that one. So, that's probably all the signals I wanted to probe at.

**Dave Jones:** I'm going to for now anyway, so let's go into let's um uh basically get rid of the antenna so it will think that you want to transmit for real.

**Dave Jones:** And let's actually transmit for real. So, here it is. Let's break the seal. How easy it is it is it to break the seal on this thing? Too easy.

**Dave Jones:** There we go. Lifted up our antenna. You extend it. And if we press that button, bang, it's going to transmit for real because you can see the you see the metal clip in there.

**Dave Jones:** So, it's not going to get that coupling anymore. So, it's not going to detect that signal using that uh I believe that it may still use that for something, but anyway, it's it's going to go right.

**Dave Jones:** I'm not in test mode anymore. I'm transmitting for real. So, it won't stop after like, you know, 5 seconds or whatever it has been now, and it'll transmit at full signal power and give the proper homing signal and all that sort of stuff.

**Dave Jones:** So, what I'm going to do is I'm going to disconnect the antenna, of course, even though I don't think it's going to pick it up in the uh office.

**Dave Jones:** Here, there's all, you know, it's got a metal roof and everything. So, you know, I don't think the satellite's, not that they can pick up this anymore, I believe.

**Dave Jones:** But, just to be on the safe side, I will disconnect the antenna. Well, I don't actually have to disconnect the antenna. What I'll do is I'll just take the entire board out of here, and uh bang, we no longer have the antenna connected.

**Dave Jones:** So, that shouldn't, um it'll be transmitting, but uh it really won't be going anywhere. Be horribly, horribly inefficient by orders of magnitude. All right, let's transmit for real, shall we?

**Dave Jones:** I'm in trouble. I'm near death, and uh I've got to hit that uh magic button on my EPIRB. Let's give it a go. I'm probing the uh antenna output.

**Dave Jones:** We can probe other stuff as well. So, here we go. There we go. It's it's now blinking and flashing. So, it is definitely transmitting. So, let's give it a go.

**Dave Jones:** Here we go. Haha! Look what we have on the scope. Tada! We have bursts. We have RF bursts. Check it out. Look at that. So, let's let's capture a whole burst.

**Dave Jones:** There we go. That one, of course. There we go. 121.2 MHz, that will actually be 121.5 if the software frequency counter, the automated cursor-based thing, isn't the best, but that will certainly be 121 down at the lower time bases there.

**Dave Jones:** So, bang! There we go. It might be a spectrum analyzer time, actually. And I just did a quick check for what the modulation requirements are for this thing. And apparently for E-perb, it must go modulate either downwards in frequency or upwards.

**Dave Jones:** It can be either, anywhere in the range from 300 Hz to 1600 Hz, but it must have at least a spread in there of 700 Hz modulation. And if it's a PLB instead of an E-perb, apparently that has a requirement of only modulating upwards in frequency instead of downwards.

**Dave Jones:** And of course, the 406 MHz digital models can still optionally have this 125 121.5 MHz modulated carrier in here as a homing beacon that is still used by the search and rescue helicopters.

**Dave Jones:** All right, it's crude measurement time. I've got a just a flying wire here, not actually directly connected, but just a coupled nearby to the antenna connector. And of course, we've seen on the oscilloscope, it's transmitting in those bursts.

**Dave Jones:** And I've got the Rigol spectrum analyzer set up. So, let's check it out. And we've got the Rigol DSA815 spectrum analyzer here. And the dreaded auto button. On oscilloscopes, don't like them, but on spectrum analyzers, they're not bad for just getting a first whack at a signal there.

**Dave Jones:** And bingo! There it is. We're at a center frequency of 121.7 MHz. And as you can see, it's jumping or it's not the usual, you know, carrier nice clean carrier with the side bands.

**Dave Jones:** It's chopping back and forth because look at what's happening on the scope over here. It's jumping all around. So, we can get a better look at that if we go into single shot capture mode instead of just continuous mode.

**Dave Jones:** So, if we hit the trigger sweep button here, it gets us into the trigger sweep menu and mode. We're in continuous mode at the moment but let's go into single shot capture mode and bingo, we've captured that and you can see our carrier here.

**Dave Jones:** As you can see, center frequency 121.53 megahertz. There it is. So, we've got that no problems. Let's go into trigger sweep again. Let's turn that back to continuous. Okay, it's jumping all around the shop.

**Dave Jones:** It's not the easiest thing to measure. Now, let's go into span and let's take it out and see if we can get the 220 odd megahertz hertz frequency. What is it?

**Dave Jones:** 240 3? Yes, 243 megahertz double because I don't think this thing There it is. Bang. Because this thing There's the 200 There's the alternate frequency of 243 megahertz. Now, I don't think it's actually got a I don't think it's got a frequency doubler in there.

**Dave Jones:** It just relies on getting the first harmonic there from the signal. So, I don't think it's actually got I don't think actually jumps frequency to 200 43 megahertz. It doesn't double it.

**Dave Jones:** It just relies on the fact that that is a harmonic of that signal and you can clearly see it there. If we go back into the center frequency, we can bring that over.

**Dave Jones:** I can measure it again, of course. But uh Where is it? 240 Bang. There it is. 243 megahertz or thereabouts. So, that There's our two signals which it's outputting.

**Dave Jones:** Now, let's see if we can have a look at the uh modulation on this thing. So, what we can do here is actually go into what's called zero span mode, and that should allow us to look at Bang!

**Dave Jones:** Look at that. We've got that You can see it modulating. You can see the frequency there modulating. And if you remember from before from this oscilloscope shot, that's essentially the same waveform we got for the actual um digital modulation signal.

**Dave Jones:** All right, I'm going to use the uh demodulation function of the DSA815 here. So, I've got it hooked up to some headphones here, and let me put the mic near it, and you'll be able to hear the modulated signal.

**Dave Jones:** So, you can clearly hear the uh modulation repetition rate there of between 2 and 4 hertz is what it uh information that I found, and uh that's clearly between 2 and 4 hertz, and uh you can sort of hear like a sweeping whip whip whip within those within that repetition rate.

**Dave Jones:** Now, it's usually quite difficult to detect um these uh burst RF uh signals on a spectrum analyzer like this because there's all these frequency components that jump around in there, and they're not actually uh real.

**Dave Jones:** So, what we need to do is go into the uh bandwidth detection over here and change the video bandwidth like this. And if we lower that, we should find that bingo, our signal or our carrier pops out of that just nicely.

**Dave Jones:** There we go. When we decrease it to a video bandwidth of 300 hertz, 1 kilohertz, it really you know, it starts to play funny business and go crazy like that.

**Dave Jones:** But if we turn it down, then we can actually see the carrier signal itself. And if we change the span, of course, we can uh Up. No, going the wrong way.

**Dave Jones:** Change our span, let's go up. Up, way up. Way up. And bingo, there we have our 121.5 and our 243 megahertz. We've got some other stuff jumping in here.

**Dave Jones:** I'm not sure what that's what's going on there, but we can clearly see our two carriers. There, there it is. 121.5 and 243. Brilliant. And we should be able to get better performance um on a spectrum analyzer that has uh gating capability for burst type signals.

**Dave Jones:** I don't think this uh Rigol one has it, or at least I haven't found it yet. Now, if we probe this uh modulation signal we found before, and if we have a look at that, we can see, if we trigger off uh channel two here, there we go.

**Dave Jones:** Trigger off channel two, we can see our modulation signal. Okay, now let's actually have a look at that signal we had coming back before, if you remember, from the uh detection circuitry on the antenna.

**Dave Jones:** And I'm dual wielding probes here, using my third hand. And uh there's the signal, the yellow one is the return from that detection circuitry there. Slightly out of phase, but it's at the exact signal that's being inputted to the RF circuitry.

**Dave Jones:** So, if we Up. If we disconnect that and we actually have a look at what's happening here, the microcontroller is outputting the modulation signal through here, through some AC coupling into the oscillator down here, which amplitude modulates it, and then it goes through the RF transmitter, and that's tapping off and that detection circuitry is reading it back and feeding it back in.

**Dave Jones:** So, that microcontroller knows that it's actually transmitting the proper location it's transmitting that home-in modulation data, and presumably it'll, you know, stop flashing and or do whatever, you know, error error.

**Dave Jones:** And uh uh when if it doesn't detect that output signal. So, it's when you when it's flashing like that, you know that it's it's doing that transmitting, and well, you know, somebody's going to pick it up and they're going to be on their way.

**Dave Jones:** So, presumably, um if you get nothing on the output, means part of the RF circuitry is blown, and I presume it will take uh will turn off the flashing lights.

**Dave Jones:** And of course, there's no need to speculate about that. Let's actually test it. I've removed the AC coupling cap that detects the output signal from the antenna, and let's see if this thing actually ha um continues to flash the LEDs and transmits.

**Dave Jones:** I wonder if it does. Let's have a look. All right. No. There you go. No, it's still doing it. Look at that. I have disconnected that AC coupling cap.

**Dave Jones:** Getting desperate now. Remove the AC coupling cap, the 10K resistor, and the output transistor. So, that open collector one. So, it's got nothing to uh switch low with, so that pull-up resistor on the uh circuit there, if we remove that transistor, we remove the AC coupling cap, 10K, and the transistor.

**Dave Jones:** Ah, that should that should stop that. So, let's do it. No, it's not detecting it. There you go. That's pretty conclusive that it doesn't check that output when it's transmitting.

**Dave Jones:** Ah, man, it's still modulating. It It's It It's still picking it up on the scope. This is ridiculous. What's going on? Well, duh, that's embarrassing. I was probing the wrong trace.

**Dave Jones:** I got mixed up on which trace was coming back. I was probing that second pin instead of the third one, which is the one that comes back. Ah, duh.

**Dave Jones:** Anyway, we did prove there that uh you remove that output um sampling there that that output detection circuitry, and it's not It's doesn't care about uh sampling that during the uh transmission period.

**Dave Jones:** And I've replaced the components, and now I am probing the correct pin here. So, that is the return pin instead of what looks like another either another return pin or a transmission pin.

**Dave Jones:** And let's take a look at the waveform coming back from that detection circuitry. And there it is. It is actually demodulating that output signal correctly. So, there you have it.

**Dave Jones:** That's the KTI minisat personal ELB the old 121.5 MHz analog models. And that was just a little bit of playing around with it. There could be some more uh interesting stuff going on in the circuitry and stuff.

**Dave Jones:** So, if anyone's got a schematic, uh we'd love to uh see it. And if you want to discuss this, jump on over to the EV blog forum. And if you like Teardown Tuesday, please give it a big thumbs up.

**Dave Jones:** Catch you next time.
