---
video_id: Tk_3rYKWIIg
title: EEVblog #1023 - Rigol DL3021 Electronic Load Teardown
url: https://www.youtube.com/watch?v=Tk_3rYKWIIg
source: youtube-asr
timestamps: {"0": 0, "1": 16, "2": 28, "3": 45, "4": 61, "5": 80, "6": 89, "7": 108, "8": 119, "9": 131, "10": 144, "11": 161, "12": 173, "13": 181, "14": 191, "15": 209, "16": 229, "17": 244, "18": 261, "19": 285, "20": 309, "21": 323, "22": 336, "23": 351, "24": 362, "25": 376, "26": 386, "27": 401, "28": 421, "29": 433, "30": 446, "31": 456, "32": 467, "33": 480, "34": 496, "35": 506, "36": 520, "37": 528, "38": 543, "39": 557, "40": 575, "41": 593, "42": 603, "43": 614, "44": 629, "45": 647, "46": 661, "47": 671, "48": 682, "49": 702, "50": 715, "51": 726, "52": 740, "53": 748, "54": 762, "55": 780, "56": 788, "57": 807, "58": 826, "59": 845, "60": 859, "61": 870, "62": 894, "63": 904, "64": 916, "65": 927, "66": 944, "67": 955, "68": 965, "69": 974, "70": 985, "71": 997, "72": 1008, "73": 1019, "74": 1029, "75": 1047, "76": 1068, "77": 1079, "78": 1088, "79": 1106, "80": 1128, "81": 1142, "82": 1152, "83": 1168, "84": 1185, "85": 1202, "86": 1220, "87": 1233, "88": 1245, "89": 1256, "90": 1273, "91": 1283, "92": 1295, "93": 1308, "94": 1321, "95": 1332, "96": 1347, "97": 1359, "98": 1373, "99": 1386, "100": 1401, "101": 1419, "102": 1440, "103": 1454, "104": 1465, "105": 1480, "106": 1491, "107": 1505, "108": 1519, "109": 1532, "110": 1547, "111": 1557, "112": 1568, "113": 1580, "114": 1599, "115": 1619, "116": 1629, "117": 1649, "118": 1659, "119": 1671, "120": 1685, "121": 1701, "122": 1718, "123": 1729, "124": 1748, "125": 1760, "126": 1776, "127": 1797, "128": 1808, "129": 1829, "130": 1841, "131": 1852, "132": 1866, "133": 1884, "134": 1895, "135": 1906, "136": 1919, "137": 1940, "138": 1957, "139": 1973, "140": 1993, "141": 2009, "142": 2023, "143": 2037, "144": 2051, "145": 2063, "146": 2073, "147": 2083, "148": 2092, "149": 2105, "150": 2121, "151": 2140, "152": 2151, "153": 2158, "154": 2184, "155": 2195, "156": 2212, "157": 2221, "158": 2241, "159": 2253, "160": 2263, "161": 2272, "162": 2284, "163": 2302, "164": 2311, "165": 2325, "166": 2340, "167": 2356, "168": 2371, "169": 2382, "170": 2393, "171": 2406, "172": 2417, "173": 2429, "174": 2443, "175": 2465, "176": 2478, "177": 2490, "178": 2506, "179": 2523, "180": 2534, "181": 2551, "182": 2563, "183": 2573, "184": 2581, "185": 2589, "186": 2599, "187": 2623, "188": 2646, "189": 2659, "190": 2674, "191": 2686, "192": 2695}
---

**Dave Jones:** Hi, we're going to take a look at Rigol's new DL3021 or through DL3000 series electronic loads. We love electronic loads here on the EV Blog. I've done like a do-it-yourself electronic load video, which I'll link in at the end and down below, which is incredibly popular.

**Dave Jones:** People build their own, but you can't beat a nice commercial electronic load for power supply testing, battery discharge testing, solar cell testing, all that sort of jazz. So, let's take a look at it.

**Dave Jones:** Now, this is the DL3021. It's actually the bottom range uh unit, $499 USD, which puts it about in the uh middle of the commercial electronic load market. Companies like Kikusui make sort of, you know, the top-shelf electronic uh loads.

**Dave Jones:** This is on par with like your BK Precisions and your Arrays and ITechs and uh ones like that. And then you've got your your much cheaper ones, your no-name uh clone copy ones, your Maynuos, or whatever they are on uh eBay, and things like that.

**Dave Jones:** So, it sits somewhere in between. It's a 200 W uh load, 150 V, 40 A. Now, don't confuse this with the DL3021A on the end of it. The A model is actually 300 bucks more, $799 USD retail.

**Dave Jones:** And what do you get? Well, having a look at the data sheet, I uh the manual for this thing and the specs, I'm having a hard time finding the difference.

**Dave Jones:** It seems to be the uh 0.1 mA resolution readback current uh as opposed to 1 mA for the non-A model, but apart from that, they're both 0.05% class electronic loads, which is what you'd uh expect in a precision DC electronic load in this uh price range.

**Dave Jones:** 100 ppm, they're all the same tempco. It's got slightly different ranges on constant resistance modes and things like that, but there's not much in it. I don't understand why they make an A version.

**Dave Jones:** It's just stupid. Just make the $499 version with the A functionality extra, whatever the hell that is. It probably doesn't cost you anything at all. It might be like software options or something like that.

**Dave Jones:** Just don't. Just make one model. Thank you very much. Anyway, there's deals uh the 3031 as well. Once again, a non-A version. It starts at uh 999 bucks, so 1,000 bucks goes up to 1,500 bucks.

**Dave Jones:** And the only difference in that is it's 60 amps capable instead of 40 amps, but it is 350 watts as opposed to this 200-watt model. So anyway, this 200-watt model good enough for say a larger solar panel uh testing, things like that.

**Dave Jones:** Large battery packs, stuff like that. Plenty capable uh for things like that. Now, it it's your traditional new Rigol look and feel with these rubber uh bumpers on them.

**Dave Jones:** You either like them or you don't. They're like, meh, whatever. Okay, we've got a large screen on. We'll power it up uh later cuz we want to tear it apart first.

**Dave Jones:** And we've got one knob on the thing and a keypad arrangement. Your various functions in here. And they've put the sense terminals on your front, your binding post, your USB on the front.

**Dave Jones:** And you know, your cursor keys, whatnot, and your various uh config keys up the top. It's a reasonable layout, but just look at this thing. The first time I saw this thing, my head started to like twitch to one side and I started to get a nervous tick because look at these bloody buttons here.

**Dave Jones:** Reverse italics buttons. Look at them. Look at them. Whoever designed that should be hung, drawn, and quartered. It's ridiculous. The italics sloping backwards and the buttons sloping backwards. Why?

**Dave Jones:** The humanity. Next up, I'm no graphic artist, but what the hell is up with the fonts on this thing? What is this function font? Look at like I I think I posted this on Twitter a photo of this.

**Dave Jones:** I think somebody counted four, maybe five different fonts used on this thing. It's just insane. The different fonts. Like Why? Why? Who designed this? They shouldn't be in the business.

**Dave Jones:** It looks like someone's just throwing up the font list. Illuminati confirmed. What the hell is that? What does that even mean? It's not even labeled. This is creepy. Now, I like the fact that they put the sense terminals on the front shrouded 4 mm banana plugs, but I would have liked just the old school screw terminals as well.

**Dave Jones:** So, and sorry, but the binding posts are a complete and utter fail. Why do companies keep making that do these electronic loads? They all seem to do it. Make ones with a no banana plug on them, no hole inside the thread inside the shaft there so that you can shove your wire securely in there.

**Dave Jones:** They just have these ridiculous dumb ass binding posts like this. They're so frustrating. Um you you have to end up making your own little adapter to convert them to what the hell you want.

**Dave Jones:** But check this out. This is kind of interesting. You see the thread here. I thought aha, that might be for some optional adapter. They actually include this plastic shroud in here, which just has some cutouts at the bottom for your wires, and that just sits on there.

**Dave Jones:** They got magnets on there, and that just it just attaches in there. The magnet over here is not great, and then you can just screw that eventually like straight into there.

**Dave Jones:** For like it's only 150 V rated, so it's designed for you know, so you can't touch these things, but like yeah, I don't know. Okay. Cute, I guess. Nice touch.

**Dave Jones:** Now, as for the key layout, it could certainly have been better. I mean, you've got all your constant current, constant voltage, constant resistance, constant power, and and your other looks like there's a pulse mode, a toggle mode, a list mode and stuff like that.

**Dave Jones:** So, I don't mind that. You know, your on/off button probably should have been down like here next to your output or something like that perhaps. Transient short is interesting.

**Dave Jones:** I'm curious to find out what does it just short out the internal current shunt? Not sure what that is. Anyway, you know, your cursor keys, the knob here is not pushable, and this the italics ones up there are so triggering.

**Dave Jones:** Anyway, it it's it's okay, but they could have done better. You know, I like the dedicated application button here, battery, OCP, and OPP. I'm curious to check out the battery functionality for measuring your characteristic curves of batteries.

**Dave Jones:** On the back, made in China of course, but look, it's fully featured for the bottom of the range unit. You got some digital IO for programmable control switching and test fixtures off and on.

**Dave Jones:** You've got your LXI LAN interface, fantastic USB device, or old school RS-232 serial current monitor output and voltage monitor output. Very handy for hooking those up to the scope.

**Dave Jones:** Nice. All right, so let's crack this thing open. Just take the handle off the side and the four feet on the bottom and slides off just like most others.

**Dave Jones:** And we're in like Flynn. Geez, I'll have to sit it up for you, but uh yeah, hang on. We'll take a squeeze. Ooh. I'll tell you what, this looks quite neat and tidy.

**Dave Jones:** I really like it. We'll show you up close. It's hard to sort of get in here without taking the whole blinking lot about like get detail on the board and get light in there and uh stuff, but I I I really quite like it.

**Dave Jones:** Anyway, thermal uh wires, we've got our uh entry on the side here and here through the uh hole the grill on the uh side of the unit. The fan inside then sucks the air from here, pushes it through our finned heatsink which has all our power on there.

**Dave Jones:** You can see those down in there. There's some on the other side as well. Not even number, so that's interesting. And just dumps it out the back. So, the thermal design, that's as good as you can expect.

**Dave Jones:** And uh this is the 200 W model. So, the upper model is the 350 W model. So, presumably it either has some more power devices on there. I can see some extra footprints down in there.

**Dave Jones:** There we go. Looks like it's going to have uh the same heatsink and everything. Might drive the fan a bit quicker. We've got some extra footprints down in there.

**Dave Jones:** So, maybe it's just a matter of extra power on the uh upgraded unit. In that case, why does it cost like This one's $499. The other is a thousand bucks.

**Dave Jones:** Why does it cost 500 bucks more, double, to get the extra power if all the heatsinking and everything else is like you know, the rest of the design is going to be pretty much the same cuz it's 60 amps versus 40 amps.

**Dave Jones:** Like that's really gouging. Just make one model. Just make the 60 amp model for $499 and you'd kill the market probably. Come on. But okay, it's got some extra power devices, you know, and I don't mind paying for and like an increased power a with extra parts, but not double.

**Dave Jones:** That's just no, not on. Now, this is absolutely fascinating. Look, they've used a PCI expansion board in there for all of your IO capability. That's really quite nice. I like that.

**Dave Jones:** Nothing wrong with PCI slots. They're you know, readily available. They're never going to go obsolete. They're used in too many things. They're they're cheap. They're simple. They've got lots of contacts.

**Dave Jones:** They're reliable. They're proven. Everything else. Like it's nice to see a PCI board in there like that. That's off. Okay, our mains wiring. I like the earth terminal going off there.

**Dave Jones:** That looks properly crimped and shake proof washer. No worries. It's all heat shrunk. Goes on to the main PCB down here. That's the mains voltage selection. So, they're good doing some main selection around there.

**Dave Jones:** You can see the high voltage isolation slots in there. Very nice. And then they've got that wiring going over over there. Running through there. Cable tied nicely. And that goes over to the real clunking power switch on the front, which is actually mounted on the main PCB.

**Dave Jones:** So, once again, that's quite nice. They've left the tons of isolation space in there. So, no worries whatsoever. Rigol, innovation or nothing. Is this a new slogan? I don't think I've seen that before.

**Dave Jones:** Anyway, designed in China. They're quite proud of it and rightly so. They're doing lots of nice R&D. And that transformer looks nice there. Nice little small linear jobby because this is not a power supply.

**Dave Jones:** It's a load. So, it doesn't have to power much. It's just got to power all the digital analog circuitry. That's it. So, AC in, bridge rectifier. We've got our filter cap.

**Dave Jones:** We've got a couple of small heat sinks here. Have to get the thermal camera on those I suspect because Rigol have I up that in the past, although be careful getting the thermal camera onto just the anodized clear aluminum like this because your emissivity readings will be crap.

**Dave Jones:** So, you're better off maybe getting a thermocouple on there to measure that. But, of course, the test would be the old finger test. Leave it on for a while, and it shouldn't change with the what load it's producing and stuff like that.

**Dave Jones:** So, as long as you can keep your finger on there, it's under 50° she'll be right. No worries. So, that that all looks fine and dandy. You can see the high voltage isolation cutouts there around the MOSFETs.

**Dave Jones:** So, yep, they know what they're doing. Nice touch. And the electrolytic cap, that symbol there is a Samyoung. So, they're Samyoung KMG series. You know, yeah, par for the course.

**Dave Jones:** Now, for the main chip in there, I'm surprised to see a Spartan-6 in something like this. I mean, they must be running like a softcore uh processor in there.

**Dave Jones:** I would be guessing to do all this. I you know, they could do it all in VHDL or whatnot, but yeah, the my guess is they're running some sort of a softcore processor in that.

**Dave Jones:** But, all the rest of it is just all the uh all the miscellaneous, you know, analog and you know, it'd have the ADCs and the DACs and what not all around it, but that's uh that's pretty much all she wrote.

**Dave Jones:** But, the interesting thing to note is this ribbon cable here, of course, goes off to the front panel board. That's got another Actel FPGA. We'll have a quick look at that.

**Dave Jones:** But, the traces don't go off to the Spartan-6. Look, they bugger off all the way around here, right behind the transformer and everything else. They they're running all the way around here, coming right to the back, and going to that PCI card, which controls that.

**Dave Jones:** So, maybe the processor is actually on the front board, and that FPGA is just doing all the you know, the data acquisition stuff and things like that, because uh because otherwise, why would you have the IO card there flowing into the front panel board?

**Dave Jones:** So, yeah, I take that back. The Spartan-6's it might still be running a softcore, but it's it's not doing all the main uh processing and uh display stuff. And can't quite read that on the screen, but that's uh some sort of Freescale uh processor down in there is it holding the uh doing all the digital uh IO stuff.

**Dave Jones:** I can't actually get this PCI card out without actually taking out the main board. It just does not come out uh due to the uh D9 connector serial connector on the back.

**Dave Jones:** Bummer. As for the front panel uh board down in there, an Actel ProASIC3. I'm curious that they've used a like an Actel one and then a um Spartan one, a Xilinx one.

**Dave Jones:** So, you know, two separate uh brands. They probably have different uh development teams uh working on these. So, they just chose their flavor of FPGA. Actually, given that there's only the Actel ProASIC3 FPGA on there, Spartan-6 down there, I am going to say that that Freescale processor down in there is the main processor for this thing.

**Dave Jones:** And in fact, they call this a digital board. If you can see the text down in there, so it's not just an IO board. This is the digital board, so this is the digital processor board for the whole thing.

**Dave Jones:** So, that is the main processor. Kind of, you know, not a bad decision to put it onto a PCI card like that. You can swap it out uh later without changing your main uh board.

**Dave Jones:** That's, you know, and your display board as well. That's quite smart. Now, as for the input over here, very very nice. I love this and it's common that you'll find these on big loads like this.

**Dave Jones:** The huge binding post just huge bus bars directly out straight onto the PCB copper. Just massive pads, massive amount of copper on the PCB there. And it looks like we've only got the one current shunt resistor.

**Dave Jones:** That one down there, you might be able to might have get the macro lens on there, but you might to see little traces coming out there. That's the That's the pair coming out for the four-wire sense.

**Dave Jones:** There we go. You should be able to see that. Just a couple of one pair coming out there. That's just the sense wires going into the sense amp down there.

**Dave Jones:** Now, you might be thinking, "Hey, this is a shunt resistor." That's a 4.7 ohm huge couple of watt What is that? A 5 watt jobbie or something? I don't know.

**Dave Jones:** It's quite large power one. And no, that is not a current shunt resistor. That is not a low PPM Current shunt resistors don't have to be accurate, as I've said many times before, but they've got to have they've got to be very stable.

**Dave Jones:** So, they've got to have a low temperature coefficient. This looks like just a job logs power resistor. So, that's just part of some snubber RC snubber type network there happening.

**Dave Jones:** So, looks like we've only got the one current shunt resistor down there. Very low value jobbie. Now, whether or not that varies between the regular model and the A model, I doubt it.

**Dave Jones:** I think they're using the same current sense resistor. Um like well, the sense network could change. They could get extra resolution, but I think it's just probably like a software type difference there.

**Dave Jones:** So, this is the difference between they would be getting the non-A model, which we've got here, has 1 milliamp resolution, I believe, and the A model has 0.1 milliamps.

**Dave Jones:** So, you know, order of magnitude better, but they're probably still using the exact same current shunt resistor. And for you power trainee fanboys, there you go, International Rectifier. Can't quite make out that number on the LCD, but I'll read that back, include the data sheet.

**Dave Jones:** They're probably like matching devices in there all the way along. So, I've got it as I said, it's difficult to get this board out, so I'm not going to bother to see the other ones, but each channel has six of those, and presumably the A model with the 60 amp capability is going to have the extra two, so it'd have eight devices per side.

**Dave Jones:** There's certainly been a bit how you doing with the heatsink compound in there. Check that out. Geez. So, I'd like to go into more detail in trying to get that board out, but it looks a little bit ugly.

**Dave Jones:** I don't I don't think we're going to learn a huge amount more. Just suffice it to say it suffice it to say that this thing is quite well designed and manufactured.

**Dave Jones:** I I can't find any issues with this thing at all. So, up yeah. I'm just excited to power it up and have a little play with it. Not sure if you can see that, but the buggers have lasered off the markings on these four SO8 packages here around the current sense amp.

**Dave Jones:** STOP IT. JUST STOP IT. AND THEY'VE done the same bloody thing for the op amp around the MOSFETS THERE. WHY? AH, UNBELIEVABLE. Just see if we can see the other down in there.

**Dave Jones:** Not sure. Can't see it on the LCD. And that connected down in there, obviously going off to the sense wires on the front panel. Got a relay. Notice the isolation slot, and also some input divider or and or protection resistors.

**Dave Jones:** And once again, more high voltage slots there. Only 150 volts, so you know, you needn't do that sort of thing for those sorts of voltages, but hey, overvoltage and stuff like that, no worries.

**Dave Jones:** But it does show nice attention to detail and more slots cut around here. So, yeah, somebody just went "Yeah, I'll put a slot in cuz that's the thing to do." And I'm not sure what's going on with those plated holes input -1 2 3 4.

**Dave Jones:** Like, I don't get it because they're just one big copper pad with plated through holes. Um I don't know. They're not like current uh shunt jumpers or anything like that for big current shunts.

**Dave Jones:** Obviously, some sort of extra mechanical interface which they didn't use. They went for the other two big bolts down there, perhaps. Hm. All right. So, let's power this baby up and have a quick play around with it.

**Dave Jones:** Self-test, all righty-ho. Come on. You can do it. Wonder what OS it's running. Come on. It's only an electronic load. Self-test. Twiddle thumbs, twiddle thumbs, and here we go.

**Dave Jones:** We're in like Flynn. Now, I don't mind the interface. It's not too bad at all. Displays the current voltage with four-digit precision. Thank you very much. And we do get, even though this is not the A model, we do get the 0.1 milliamps.

**Dave Jones:** At least the display digit is there anyway. So, that is definitely 0.1 milliamps whether or not, you know, it could be as I said, just a software thing and it just counts up in 10s and only has 1 milliamp resolution.

**Dave Jones:** I don't know. But anyway, it displays our power and our resistance as well. So, let's put it in constant current mode. So, ranges here, we've got 40 amps and 4 amps.

**Dave Jones:** So, that doesn't give us it doesn't change our display resolution at all anyway. So, that's rather interesting. Our slew rate, our, uh, V on where it uh, switches on at, our voltage limit, 180 volts.

**Dave Jones:** It's 150 volts supply, so why it's 180 volts I don't know. And our constant current limit up to 70 amps. Once again, this is only a 40 amp supply.

**Dave Jones:** So, what's going on there? And by the way, if I start using the knob, there is no velocity control. Ah, why? It's not hard to implement a proper velocity control for that.

**Dave Jones:** That's just ridiculous. So, I can just type in one like that, and there you go. And I got to press like 1 amp, there it is, but like, give me a velocity control.

**Dave Jones:** It doesn't work on any of the, uh, input parameters at all. So, on constant voltage range, we have our selectable 15 volts or 150 volt range. That's all right, no worries.

**Dave Jones:** And our voltage, once again, the knob is almost useless. Ah, it's only for fine control. Frustrating. Anyway, uh, we can set our voltage limit and our current limit once again.

**Dave Jones:** And our constant resistance range, there you go. Anywhere from, whoop, which, anywhere down to 2 ohms on the 15 k ohm range, but it also has a 15 ohm, uh, range as well.

**Dave Jones:** 15 ohm range as well. And our resistance can go down to 80 milliohms there. Neat. And our constant power mode, we don't have any ranges on that. It's just fixed at the, uh, watt level.

**Dave Jones:** So, let's actually enter 200 watts, cuz that's our limit. Can we go above that? No, of course we can't. Boom. Whoop. Nope. Uh, setting has exceeded the power upper limit.

**Dave Jones:** Thank you. Then we've got our other function modes here. Let's, uh, continuous, config guide. I like this, how it's all just coming up like that. That is very comprehensive and pulse config guide.

**Dave Jones:** Once again, look at all the parameters you can set. Very nice. Read, apply. How do you Okay, we'll have to set those somewhere else presumably. Toggle config guide and then you've got the list mode as well.

**Dave Jones:** Automatically goes into the graph here. Shows you all your relevant parameters in a quite decent font there and I'm liking this. I really am. It's quite neat. Anyway, the list thing is like a a step-based sequence type mode you can go to.

**Dave Jones:** Useful for systematized power supply testing things like that. Now, what I'm really interested in is the battery mode and let's have a look. Once again, voltage and current displayed, milliamp hours, watt hours, which is what you know, the true capacity of a battery, our timer there, but unfortunately we can set the current.

**Dave Jones:** We can set our range from 4 amps or 40 amps. We can set our stop voltage. We can set our current stop as well and our or a timer-based stop, but we can't set a stop value on our watt hours.

**Dave Jones:** Why not? It's just a software thing. It can only do milliamp hours. You can't stop on watt hours. Like and that's where it'll switch on with the on voltage.

**Dave Jones:** Like just give me watt hours. Anyway, let's click the Illuminati button and see what that does. Oh, that's our graph. That's our graph. You can start to see it starting to accumulate there.

**Dave Jones:** So, the unlabeled Illuminati button, some people say I put this on Twitter and they said, "Oh, it's the CBS logo." Like I have no idea about CBS. So, yeah, whatever.

**Dave Jones:** It's the Illuminati button and yeah, we've got our graph mode. So, that means that in when you're in say constant current mode, you can do the graph. So, it's totally dependent upon constant power, depending on which mode you're in.

**Dave Jones:** I don't mind that. They could have bloody labeled it though. And then the other modes is our over current protection mode. You can just sequence like do a step sequence mode for testing your supplies for power and current.

**Dave Jones:** So, that's not bad at all. I like those three apps built in. And it looks like our on off button, there it is. Load just comes up. Tran whoop.

**Dave Jones:** Presumably, transient. And what a short do? Does it short out the terminals? I don't know what short does. RTFM. The most annoying part about this though is that I cannot select anything but constant current discharge.

**Dave Jones:** I mean, what if I want to test constant constant resistance mode, which is in the data sheets for you know, toy testing and things like that. I can't do it.

**Dave Jones:** I got constant current only. It's ridiculous. This is like just a software limitation. Why have a complete battery mode like this if that's all you're going to be able to do?

**Dave Jones:** It's ridiculous. Now for the finger test on these heat sinks down in here. Of course, this one's where we're not dumping any load into this at all. So, of course, that's completely cold.

**Dave Jones:** These linear regs down here, back of the finger. Hang on. It is Ry Gall, so Ah, yay. Yay. Bloody hell, that's too hot to touch. Unbelievable. Have they done it again?

**Dave Jones:** Okay, so that one there is 80°. Come on. This is not a rocket science, Ry Gall. That is too hot for a simple supply. I mean, like the junction temperature has like is well above that.

**Dave Jones:** That's just that like granted, okay, we don't have the top in the case. So, we got like I can sort of put the case back I can Well, I can put something on the top and that's going to simulate the airflow.

**Dave Jones:** Let me do that, but that's just That's just wrong. I'm afraid that the one next to it there is even worse. This one's up to 88. Ah, unbelievable. Okay, I've put the lid on the top and you can see it going down.

**Dave Jones:** It's dropping. I've got like just boxes on the top like that just to simulate cuz the air in the side in the intakes going to be the same. Okay, it's getting down towards 75°.

**Dave Jones:** So, yeah, that's knocking like 13° off, but that is still just no excuse for being that high for a basic linear regulator when you have all that space inside.

**Dave Jones:** It's just insane. Now, and that's not to say that it's like, you know, going to fail or anything like that. There's still margin inside, you know, the die temperature of a 7805 or whatever can go up to What is it?

**Dave Jones:** 120° C or something. But so, it's not going to fail. I don't recall that being a nearly as bad as I think it was over 100° for the for the DP832 power supply which they had to fix, but come on.

**Dave Jones:** No. No. No. No. No. No. Now, curiously, the Rigol DP832 powers up much, much quicker than the electronic load. Why? They've I can't remember the teardown, but they've changed our processors or whatnot and maybe changed OS.

**Dave Jones:** I don't know. What's going on? But there's a huge difference. I mean, that's fine. This one takes forever, but meh, whatever. Now, I've got it uh hooked up to the 832.

**Dave Jones:** I've got simple constant current load of 1 amp. Uh we're getting 1.004 over here, and we're getting 0.997 8. That's like a discrepancy of 0.6% between them. Um What the?

**Dave Jones:** That's way out of spec. Oh, duh. I'm on the 40 amp range. Let's go Up. What? Turn off the load. You can't change ranges unless you uh have the load turned off.

**Dave Jones:** There we go. 4 amp range. Uh No. It's exactly the same. Uh Like, assuming that Let's just assume that it's 1 amp. That's like 0.3% out uh 0.2% out.

**Dave Jones:** It's supposed to be 0.05% plus 0.05% full scale. Seems out of spec. And let's just uh check the voltage. 29.977 and right on the terminals where it should be measuring it, 29.981.

**Dave Jones:** It's not too far off, but technically, that might be close to or out of spec as well. Okay, people wanted to know the current. Well, it looks like the DP832 is bang on, 1.005.

**Dave Jones:** I'm not going to quibble one least significant digit uh compared to the 7 1/2 digit uh Keysight here. So, we're going to take that as absolute uh because yeah, its accuracy is like order of magnitude better or something than what we've uh got here, and we're getting 0.998.

**Dave Jones:** One. That's out of spec. Rigol, please explain. Okay, let's do our dreaded constant resistance mode. We've got it set to uh 10 ohms. Let's switch on our supply here, and absolutely nothing.

**Dave Jones:** I switched it down to 2 ohms. We're getting no hiccup in at all, even though you can see that the 3 amp current limit is enabled on the DP832.

**Dave Jones:** Nothing's hiccup in. Nope. Stable as. And the short button does exactly what you expect. It shorts it out. 0.01 ohms. Um so, it doesn't do that with a relay.

**Dave Jones:** It does that using the using the MOSFET load to actually do that. Now, as for the graph functionality on this thing, the Illuminati mode, um it's there's no way like you can't like there's no auto scale button or anything like that to just like auto scale that in.

**Dave Jones:** That would have been really nice. Um please implement something like that. Just so that you can see the fine detail in there. And we can choose our data. Current U is voltage, R is resistance, P is power.

**Dave Jones:** Why can't we do the voltage and current on the same graph? Why can't we have another Y axis over here and uh do them in different colors? Um yeah, please.

**Dave Jones:** That'd be nice. And I've plugged in my USB stick here. It says it was detected, and I'm going to print. Saving image. Great. I love that feature. Presumably, hopefully, um but what?

**Dave Jones:** Failed. Why? Uh Okay. Let's try another USB stick. Maybe it wasn't the right format or capacity or whatnot. Saving image. Come on. Unbelievable. Hey, check this out. I was just logging here.

**Dave Jones:** I pressed the utility button. It switches off the bloody output. Look. Why? That's ridiculous. Look at this. It does the same thing. It doesn't do it for option, but it does it for store.

**Dave Jones:** You push the bloody store button and it's there. Anyway, look, it looks like there's a D drive there. I presume that cow data is that the C is probably internal.

**Dave Jones:** How do we get to D? Like that. There's a D drive there. Save. I don't know. Okay, whatever. Uh what? What? Okay. I don't know. Do we have to do D Do we have to select D before we did the bloody print thing?

**Dave Jones:** Is that what's going on here? How do you get rid of that? Oh, look at Wow, it just ah Ah, on. Okay, print. Saving image. It's going to work this dot failed.

**Dave Jones:** Yay! I think I finally found a USB stick that actually worked. It just says saving image and saving. Oh, thank goodness. Huh, and it saves it in bitmap format.

**Dave Jones:** How quaint. Okay, let's go into the utility here. Have a look at the all the interface stuff. GPIB, nice. USB, RS232, nice. All the requisite stuff and LXI LAN as well.

**Dave Jones:** That's I'm sure that'll work a treat. And there's the firmware versions and stuff for those playing along at home. Uh system boot time times been booted 34 times FPGA version all the requisite stuff.

**Dave Jones:** Last calibrated 1st of the 9th. And yep, you betcha, we've got software options LAN official digital IO high resolution official. The like I Is that the A version? Have I been upgraded?

**Dave Jones:** I don't know. Slew rate and frequency cuz they those three things, the high resolution slew rate and frequency, seem to have been the major differentiators with the A version.

**Dave Jones:** So, I don't know. Have I been uh given the A version and no sticker on it? Um install I So, maybe I have. Now, I don't mind the uh list mode here.

**Dave Jones:** It actually works quite good. Uh basically, you set the number of steps that you want as six maximum. I'm not sure. Anyway, what what can we go up to?

**Dave Jones:** No. Heaps. So, anyway, we can set it back to two. So, we'll go two steps, and then I've set uh I you just use cursor keys over here just to set Okay, we want 1 amp.

**Dave Jones:** We're in constant current mode. We can change our range. So, we want 1 amp 1 amp for a duration of 1 second, and then we want uh 2 amps for a duration of 1 second, and circles I loop, you know, how many times you want to loop through.

**Dave Jones:** So, we can now run that, and it should hopefully No. What's it doing? Huh? Well, why isn't it going on to the next step? Hello. McFly. One other thing I noticed, if you've actually got this on and you go to something else, it just it'll go to that mode and switch it off.

**Dave Jones:** You shouldn't be able to do that. That's just wrong. You should uh you know, it should tell you sorry, you know, you've got to switch it off. Cuz you usually when you switch it on, you're doing something.

**Dave Jones:** You don't want to accidentally hit buttons and cause it to goof up. Now, it looks like why this isn't working may the trigger it needs to trigger to go to each state.

**Dave Jones:** It doesn't automatically do it based on the duration. You can do uh trans transient. Um I'm not sure what's going on there. Uh bus uh bus triggering? Uh is that like your interfaces, your RS232s, and uh LAN and whatnot, or your digital IO interface where you can feed in external signal and cause it to step through, but there's no like time-based mode or automatic or anything like that.

**Dave Jones:** So, that when we start this, it just stays in the same duration there, and it's 1 second. It doesn't automatically go to the next. So, I'm not sure what's going on there.

**Dave Jones:** RTFM maybe? Aha, tran tran button. Let's go. There we go. Let's press it. Yes, there we go. It's sequencing through. There you go. You can see it's sequencing through.

**Dave Jones:** Green on each Oh, no, sorry, cuz it only cycled through huh twice. We only had number two circles, but there you go. You saw it. You can sequence through.

**Dave Jones:** Nice. And you can apparently uh record that to USB as well. So, if I go back, well, no, I just pressed on, and then trans, and boom boom boom boom boom boom.

**Dave Jones:** And it should end, and it ended the recording, did it? Let's see what we got. Well, that's lame. All it did was record the voltage. Why can't it record all the parameters here for each step?

**Dave Jones:** That's just it's just dumb. Okay, I'm going to do a battery discharge test. I've got a Duracell Ultra in there, fresh out of the pack. You can see I'm using the external sense lines here.

**Dave Jones:** I've just got it hacked in there a bit. How you doing? And I'm going to do a very brutal 1-amp constant current discharge, because you can't do anything else.

**Dave Jones:** You can't do constant resistance or anything. Bloody ridiculous. Anyway, um I've got the stop voltage set to 0.8 volts. I don't care about the uh timeout. I don't care the current uh timeout.

**Dave Jones:** I don't care about stopping 0.5 volts turn on. Everything's hunky-dory. It doesn't matter whether I not I go out of battery mode. It shows I was mucking around just with one before um just to make sure the setup works, and um it shows the previous info there.

**Dave Jones:** It doesn't clear it. Even if I uh go in there and you know, change the change the app or whatever. Look, anyway, um let's do it. Let's start it, shall we?

**Dave Jones:** So, here we go. Constant current discharge, uh 1 amp. And we should presumably these will clear, the time will reset, and we'll start again. Let's give it a whirl.

**Dave Jones:** There we go. All right. Uh it's dropping. It's dropping fairly drastically already, as you'd expect, because it's pretty brutal, 1 amp on a poor um innocent AAA cell. But anyway, it will eventually get a figure here.

**Dave Jones:** Now, we can actually call up the graph. Okay? Look, there it is, right? It'll start, but we can't choose both. Like, we can't get the figure. Like, it's just like a like a Why can't I have all the information on here and it resets the graph?

**Dave Jones:** What the hell is going on here? Like, I can't do both. That is just ridiculous. And we're done. That didn't take long at all. Battery test completed. I assume I press okay to get rid of that.

**Dave Jones:** And there it is, of course, that the load is disconnected. As so, the voltage is actually recovering. It would have gone down to 0.8 volts on the terminals of the battery cuz we are doing the voltage sense down here.

**Dave Jones:** And there you go. For the record, 263 milliamp hours or 0.268 watt hours for a 1 amp discharge on a basically one of the best double A you can get, the Duracell Ultra.

**Dave Jones:** So, yeah, it's not great because AAA's aren't designed to handle 1 amp constant current loads. That's just crazy, you know? You'd use a AAA or higher for something like that.

**Dave Jones:** But there you go. It works, but yeah, it's it's crude. And look, go into our graph. Where's our graph? Where's our data? Like, it's just ridiculous. Can we play back?

**Dave Jones:** Can we play back? Oh, maybe we should have pressed record and it would have dumped it to the USB stick, damn it. USB was not detected. We've got to press record.

**Dave Jones:** Okay. Oh. But to record like this, I've got to be in the Illuminati mode, right? So, I got like I don't know. Back? Can I like go if I go out of there?

**Dave Jones:** Is it Oh, no, it's still in record. So, maybe that actually works. Maybe that is going to work. Here we go. I'll start it again. Bingo. There's a bit more capacity left in that battery, of course, due to the electrochemistry recovery in there due to the very steep discharge, but hopefully, we're actually dumping that to the USB stick.

**Dave Jones:** So, that'll be done in short order. We'll only get another few tens of milliamp hours out of that puppy, surely. Okay, we're done. Didn't take long at all. We got an extra 23 milliamp hours out of that.

**Dave Jones:** There you go. And once again, it's recovering. And presumably, if we go back to the gra- It's recording like I don't know. Do I just take the USB stick out?

**Dave Jones:** Like, do I press unrecord? What do I do? Like, I don't I think it's only going to record I'd be very surprised if it actually recorded this data. Well, I think I'm going to call it quits on uh having a play around with this thing for now.

**Dave Jones:** This was not designed to be a full review. It was just a teardown and initial uh play around. And the kind of initial verdict is like like I don't mind the design and build of it apart from that ridiculously hot Well, not as ridiculously hot as the DP832 that heatsink inside there.

**Dave Jones:** I Anyway, the design of the front panel isn't the best. Those fonts are ridiculous, but at the end of the day, that doesn't really uh matter. It's about the functionality of it.

**Dave Jones:** I was disappointed by the battery mode. Some of the other uh modes are, you know, like it it has all your basic load functionality. It would take, by the way, a lot of work to extensively test all the different modes of a uh advanced electronic load like this one.

**Dave Jones:** So, yeah, that would like be a 40-minute video in its own right, I think, if I did that. But, um there's like just basic things missing from the battery test, the display mode and stuff.

**Dave Jones:** The USB was it has to be a a certain format, and it didn't even tell me that it was wrong, and it's just uh there appears to be uh accuracy issues with this thing.

**Dave Jones:** Maybe more extensive uh requirements on that, you know, like it's only an amp, it's not like a 40 amps or whatever. It was like it it should have been better than that.

**Dave Jones:** So, I don't know what's going on there. Rigol need to look at that, and I don't know, there's just not a huge amount of spit and polish on this thing.

**Dave Jones:** It's like, "Yeah, okay, it's a load, it'll do the basic job." But, there seems to be, you know, quite a few issues with it, which they can fix in firmware updates and uh stuff like that.

**Dave Jones:** But, um initial impressions are that it's just a run-of-the-mill electronic load, really. Um you know, bang for buck, there are better ones. Uh just you you know, if you just want a basic electronic load, you can get one for two, 300 bucks on eBay, one of those rip-off uh brands, and they do more than an adequate uh job just for a basic electronic load for testing uh power

**Dave Jones:** supplies or uh something like that. So, at the end of the day, it's like nothing hugely to recommend this thing yet. It, you know, if it they improve the uh functionality and solve the uh whatever accuracy issues it might have, and if they gave you the A model, all of it, like I don't I presume that mine has the extra A uh functionality, but it doesn't have the uh label on there.

**Dave Jones:** But, those options are a ridiculous price. Like, what was it? 400 bucks? Or was it double or something just to get the A model? It's It's crazy. Just have one freaking model.

**Dave Jones:** Um maybe two if you want the difference between the uh 300 W and the 200 W model, fine. But, uh like it doesn't justify the price difference. So, no, they haven't got themselves a killer electronic load here, I'm afraid.

**Dave Jones:** Um it's just meh, another electronic load on the market. They've all got their own little quirks and issues and whatnot. And this one is no exception. So, there you go.

**Dave Jones:** If you like this look at the Rigol DL3021, please give it a big thumbs up. Full of frame, thumbs up. And if you want to discuss it, down below.

**Dave Jones:** Catch you next time.
