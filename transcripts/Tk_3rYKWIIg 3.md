---
video_id: Tk_3rYKWIIg
title: EEVblog #1023 - Rigol DL3021 Electronic Load Teardown
url: https://www.youtube.com/watch?v=Tk_3rYKWIIg
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 31, "3": 48, "4": 64, "5": 82, "6": 98, "7": 114, "8": 129, "9": 147, "10": 162, "11": 177, "12": 189, "13": 205, "14": 222, "15": 244, "16": 265, "17": 283, "18": 302, "19": 319, "20": 331, "21": 347, "22": 364, "23": 378, "24": 393, "25": 407, "26": 421, "27": 439, "28": 452, "29": 469, "30": 480, "31": 496, "32": 508, "33": 522, "34": 538, "35": 555, "36": 570, "37": 589, "38": 603, "39": 620, "40": 636, "41": 653, "42": 669, "43": 682, "44": 696, "45": 712, "46": 726, "47": 742, "48": 758, "49": 775, "50": 788, "51": 802, "52": 823, "53": 839, "54": 854, "55": 870, "56": 889, "57": 902, "58": 914, "59": 927, "60": 944, "61": 958, "62": 972, "63": 984, "64": 997, "65": 1009, "66": 1025, "67": 1040, "68": 1054, "69": 1067, "70": 1079, "71": 1094, "72": 1106, "73": 1130, "74": 1144, "75": 1159, "76": 1176, "77": 1194, "78": 1215, "79": 1230, "80": 1244, "81": 1261, "82": 1279, "83": 1295, "84": 1310, "85": 1328, "86": 1342, "87": 1357, "88": 1375, "89": 1392, "90": 1408, "91": 1424, "92": 1442, "93": 1459, "94": 1475, "95": 1491, "96": 1507, "97": 1522, "98": 1540, "99": 1557, "100": 1570, "101": 1585, "102": 1613, "103": 1627, "104": 1646, "105": 1661, "106": 1679, "107": 1692, "108": 1710, "109": 1728, "110": 1751, "111": 1774, "112": 1797, "113": 1813, "114": 1829, "115": 1846, "116": 1863, "117": 1879, "118": 1892, "119": 1908, "120": 1930, "121": 1955, "122": 1973, "123": 1993, "124": 2014, "125": 2033, "126": 2048, "127": 2066, "128": 2079, "129": 2095, "130": 2109, "131": 2122, "132": 2140, "133": 2151, "134": 2161, "135": 2179, "136": 2193, "137": 2208, "138": 2221, "139": 2243, "140": 2256, "141": 2270, "142": 2284, "143": 2298, "144": 2313, "145": 2325, "146": 2343, "147": 2359, "148": 2372, "149": 2384, "150": 2401, "151": 2417, "152": 2434, "153": 2449, "154": 2465, "155": 2478, "156": 2498, "157": 2509, "158": 2527, "159": 2538, "160": 2553, "161": 2566, "162": 2579, "163": 2589, "164": 2602, "165": 2616, "166": 2632, "167": 2646, "168": 2661, "169": 2678, "170": 2695}
---

**Dave Jones:** Hi, we're going to take a look at Rigol's new DL3021 or through DL3000 series electronic loads. We love electronic loads here on the EV Blog. I've done like a do-it-yourself electronic load video, which I'll link in at the end and down

**Dave Jones:** below, which is incredibly popular. People build their own, but you can't beat a nice commercial electronic load for power supply testing, battery discharge testing, solar cell testing, all that sort of jazz. So, let's take a look at it. Now, this is the DL3021.

**Dave Jones:** It's actually the bottom range uh unit, $499 USD, which puts it about in the uh middle of the commercial electronic load market. Companies like Kikusui make sort of, you know, the top-shelf electronic uh loads. This is on par with

**Dave Jones:** like your BK Precisions and your Arrays and ITechs and uh ones like that. And then you've got your your much cheaper ones, your no-name uh clone copy ones, your Maynuos, or whatever they are on uh eBay, and things like that. So, it sits

**Dave Jones:** somewhere in between. It's a 200 W uh load, 150 V, 40 A. Now, don't confuse this with the DL3021A on the end of it. The A model is actually 300 bucks more, $799 USD retail. And what do you get? Well,

**Dave Jones:** having a look at the data sheet, I uh the manual for this thing and the specs, I'm having a hard time finding the difference. It seems to be the uh 0.1 mA resolution readback current uh as opposed to 1 mA for the non-A model, but

**Dave Jones:** apart from that, they're both 0.05% class electronic loads, which is what you'd uh expect in a precision DC electronic load in this uh price range. 100 ppm, they're all the same tempco. It's got slightly different ranges on constant resistance modes and things

**Dave Jones:** like that, but there's not much in it. I don't understand why they make an A version. It's just stupid. Just make the $499 version with the A functionality extra, whatever the hell that is. It probably doesn't cost you anything at all. It

**Dave Jones:** might be like software options or something like that. Just don't. Just make one model. Thank you very much. Anyway, there's deals uh the 3031 as well. Once again, a non-A version. It starts at uh 999 bucks, so 1,000 bucks goes up to 1,500 bucks. And

**Dave Jones:** the only difference in that is it's 60 amps capable instead of 40 amps, but it is 350 watts as opposed to this 200-watt model. So anyway, this 200-watt model good enough for say a larger solar panel uh testing, things like that. Large

**Dave Jones:** battery packs, stuff like that. Plenty capable uh for things like that. Now, it it's your traditional new Rigol look and feel with these rubber uh bumpers on them. You either like them or you don't. They're like, meh, whatever. Okay, we've

**Dave Jones:** got a large screen on. We'll power it up uh later cuz we want to tear it apart first. And we've got one knob on the thing and a keypad arrangement. Your various functions in here. And they've put the sense terminals on your front,

**Dave Jones:** your binding post, your USB on the front. And you know, your cursor keys, whatnot, and your various uh config keys up the top. It's a reasonable layout, but just look at this thing. The first time I saw this thing, my head started to

**Dave Jones:** like twitch to one side and I started to get a nervous tick because look at these bloody buttons here. Reverse italics buttons. Look at them. Look at them. Whoever designed that should be hung, drawn, and quartered. It's ridiculous.

**Dave Jones:** The italics sloping backwards and the buttons sloping backwards. Why? The humanity. Next up, I'm no graphic artist, but what the hell is up with the fonts on this thing? What is this function font? Look at like I I think I posted this on

**Dave Jones:** Twitter a photo of this. I think somebody counted four, maybe five different fonts used on this thing. It's just insane. The different fonts. Like Why? Why? Who designed this? They shouldn't be in the business. It looks like someone's just throwing up the font

**Dave Jones:** list. Illuminati confirmed. What the hell is that? What does that even mean? It's not even labeled. This is creepy. Now, I like the fact that they put the sense terminals on the front shrouded 4 mm banana plugs, but I

**Dave Jones:** would have liked just the old school screw terminals as well. So, and sorry, but the binding posts are a complete and utter fail. Why do companies keep making that do these electronic loads? They all seem to do it. Make ones with a

**Dave Jones:** no banana plug on them, no hole inside the thread inside the shaft there so that you can shove your wire securely in there. They just have these ridiculous dumb ass binding posts like this. They're so frustrating. Um you you have to end up

**Dave Jones:** making your own little adapter to convert them to what the hell you want. But check this out. This is kind of interesting. You see the thread here. I thought aha, that might be for some optional adapter. They actually include

**Dave Jones:** this plastic shroud in here, which just has some cutouts at the bottom for your wires, and that just sits on there. They got magnets on there, and that just it just attaches in there. The magnet over here is not great, and then you can just

**Dave Jones:** screw that eventually like straight into there. For like it's only 150 V rated, so it's designed for you know, so you can't touch these things, but like yeah, I don't know. Okay. Cute, I guess. Nice touch. Now, as for

**Dave Jones:** the key layout, it could certainly have been better. I mean, you've got all your constant current, constant voltage, constant resistance, constant power, and and your other looks like there's a pulse mode, a toggle mode, a list mode and stuff like that. So, I don't mind

**Dave Jones:** that. You know, your on/off button probably should have been down like here next to your output or something like that perhaps. Transient short is interesting. I'm curious to find out what does it just short out the internal current shunt? Not sure what that is.

**Dave Jones:** Anyway, you know, your cursor keys, the knob here is not pushable, and this the italics ones up there are so triggering. Anyway, it it's it's okay, but they could have done better. You know, I like the dedicated application button here,

**Dave Jones:** battery, OCP, and OPP. I'm curious to check out the battery functionality for measuring your characteristic curves of batteries.

**Dave Jones:** On the back, made in China of course, but look, it's fully featured for the bottom of the range unit. You got some digital IO for programmable control switching and test fixtures off and on. You've got your LXI LAN interface, fantastic USB device, or

**Dave Jones:** old school RS-232 serial current monitor output and voltage monitor output. Very handy for hooking those up to the scope. Nice. All right, so let's crack this thing open. Just take the handle off the side and the four feet on the bottom and

**Dave Jones:** slides off just like most others. And we're in like Flynn. Geez, I'll have to sit it up for you, but uh yeah, hang on. We'll take a squeeze. Ooh. I'll tell you what, this looks quite neat and tidy. I really like it. We'll

**Dave Jones:** show you up close. It's hard to sort of get in here without taking the whole blinking lot about like get detail on the board and get light in there and uh stuff, but I I I really quite like it.

**Dave Jones:** Anyway, thermal uh wires, we've got our uh entry on the side here and here through the uh hole the grill on the uh side of the unit. The fan inside then sucks the air from here, pushes it through our finned heatsink which has

**Dave Jones:** all our power on there. You can see those down in there. There's some on the other side as well. Not even number, so that's interesting. And just dumps it out the back. So, the thermal design, that's as good as you can expect. And uh

**Dave Jones:** this is the 200 W model. So, the upper model is the 350 W model. So, presumably it either has some more power devices on there. I can see some extra footprints down in there. There we go. Looks like

**Dave Jones:** it's going to have uh the same heatsink and everything. Might drive the fan a bit quicker. We've got some extra footprints down in there. So, maybe it's just a matter of extra power on the uh upgraded unit. In that case,

**Dave Jones:** why does it cost like This one's $499. The other is a thousand bucks. Why does it cost 500 bucks more, double, to get the extra power if all the heatsinking and everything else is like you know, the rest of the design is

**Dave Jones:** going to be pretty much the same cuz it's 60 amps versus 40 amps. Like that's really gouging. Just make one model. Just make the 60 amp model for $499 and you'd kill the market probably. Come on. But okay, it's got some extra power

**Dave Jones:** devices, you know, and I don't mind paying for and like an increased power a with extra parts, but not double. That's just no, not on. Now, this is absolutely fascinating. Look, they've used a PCI expansion board in there for all of your

**Dave Jones:** IO capability. That's really quite nice. I like that. Nothing wrong with PCI slots. They're you know, readily available. They're never going to go obsolete. They're used in too many things. They're they're cheap. They're simple. They've got lots of contacts.

**Dave Jones:** They're reliable. They're proven. Everything else. Like it's nice to see a PCI board in there like that. That's off. Okay, our mains wiring. I like the earth terminal going off there. That looks properly crimped and shake proof washer. No

**Dave Jones:** worries. It's all heat shrunk. Goes on to the main PCB down here. That's the mains voltage selection. So, they're good doing some main selection around there. You can see the high voltage isolation slots in there. Very nice. And then they've got

**Dave Jones:** that wiring going over over there. Running through there. Cable tied nicely. And that goes over to the real clunking power switch on the front, which is actually mounted on the main PCB. So, once again, that's quite nice. They've left the tons of isolation space

**Dave Jones:** in there. So, no worries whatsoever. Rigol, innovation or nothing. Is this a new slogan? I don't think I've seen that before. Anyway, designed in China. They're quite proud of it and rightly so. They're doing lots of nice R&D. And that transformer looks nice

**Dave Jones:** there. Nice little small linear jobby because this is not a power supply. It's a load. So, it doesn't have to power much. It's just got to power all the digital analog circuitry. That's it. So, AC in, bridge rectifier. We've got

**Dave Jones:** our filter cap. We've got a couple of small heat sinks here. Have to get the thermal camera on those I suspect because Rigol have I up that in the past, although be careful getting the thermal camera onto just the

**Dave Jones:** anodized clear aluminum like this because your emissivity readings will be crap. So, you're better off maybe getting a thermocouple on there to measure that. But, of course, the test would be the old finger test. Leave it on for a while, and it shouldn't change

**Dave Jones:** with the what load it's producing and stuff like that. So, as long as you can keep your finger on there, it's under 50° she'll be right. No worries. So, that that all looks fine and dandy. You can see the high voltage isolation

**Dave Jones:** cutouts there around the MOSFETs. So, yep, they know what they're doing. Nice touch. And the electrolytic cap, that symbol there is a Samyoung. So, they're Samyoung KMG series. You know, yeah, par for the course. Now, for the main chip

**Dave Jones:** in there, I'm surprised to see a Spartan-6 in something like this. I mean, they must be running like a softcore uh processor in there. I would be guessing to do all this. I you know, they could do it all in VHDL or whatnot,

**Dave Jones:** but yeah, the my guess is they're running some sort of a softcore processor in that. But, all the rest of it is just all the uh all the miscellaneous, you know, analog and you know, it'd have the ADCs and the DACs

**Dave Jones:** and what not all around it, but that's uh that's pretty much all she wrote. But, the interesting thing to note is this ribbon cable here, of course, goes off to the front panel board. That's got another Actel FPGA. We'll have a quick

**Dave Jones:** look at that. But, the traces don't go off to the Spartan-6. Look, they bugger off all the way around here, right behind the transformer and everything else. They they're running all the way around here, coming right to the back,

**Dave Jones:** and going to that PCI card, which controls that. So, maybe the processor is actually on the front board, and that FPGA is just doing all the you know, the data acquisition stuff and things like that, because uh because otherwise, why would you have

**Dave Jones:** the IO card there flowing into the front panel board? So, yeah, I take that back. The Spartan-6's it might still be running a softcore, but it's it's not doing all the main uh processing and uh display stuff. And can't quite read that

**Dave Jones:** on the screen, but that's uh some sort of Freescale uh processor down in there is it holding the uh doing all the digital uh IO stuff. I can't actually get this PCI card out without actually taking out the main board. It just does

**Dave Jones:** not come out uh due to the uh D9 connector serial connector on the back. Bummer. As for the front panel uh board down in there, an Actel ProASIC3. I'm curious that they've used a like an Actel one and then a um Spartan one, a

**Dave Jones:** Xilinx one. So, you know, two separate uh brands. They probably have different uh development teams uh working on these. So, they just chose their flavor of FPGA. Actually, given that there's only the Actel ProASIC3 FPGA on there, Spartan-6 down there, I am going to say

**Dave Jones:** that that Freescale processor down in there is the main processor for this thing. And in fact, they call this a digital board. If you can see the text down in there, so it's not just an IO board. This is the

**Dave Jones:** digital board, so this is the digital processor board for the whole thing. So, that is the main processor. Kind of, you know, not a bad decision to put it onto a PCI card like that. You can swap it

**Dave Jones:** out uh later without changing your main uh board. That's, you know, and your display board as well. That's quite smart. Now, as for the input over here, very very nice. I love this and it's common that you'll find these on

**Dave Jones:** big loads like this. The huge binding post just huge bus bars directly out straight onto the PCB copper. Just massive pads, massive amount of copper on the PCB there. And it looks like we've only got the one current shunt

**Dave Jones:** resistor. That one down there, you might be able to might have get the macro lens on there, but you might to see little traces coming out there. That's the That's the pair coming out for the four-wire sense. There we go. You should

**Dave Jones:** be able to see that. Just a couple of one pair coming out there. That's just the sense wires going into the sense amp down there. Now, you might be thinking, "Hey, this is a shunt resistor." That's a 4.7 ohm huge couple of watt What is

**Dave Jones:** that? A 5 watt jobbie or something? I don't know. It's quite large power one. And no, that is not a current shunt resistor. That is not a low PPM Current shunt resistors don't have to be accurate, as I've said many times

**Dave Jones:** before, but they've got to have they've got to be very stable. So, they've got to have a low temperature coefficient. This looks like just a job logs power resistor. So, that's just part of some snubber RC snubber type network there

**Dave Jones:** happening. So, looks like we've only got the one current shunt resistor down there. Very low value jobbie. Now, whether or not that varies between the regular model and the A model, I doubt it. I think they're using the same

**Dave Jones:** current sense resistor. Um like well, the sense network could change. They could get extra resolution, but I think it's just probably like a software type difference there. So, this is the difference between they would be getting the non-A model,

**Dave Jones:** which we've got here, has 1 milliamp resolution, I believe, and the A model has 0.1 milliamps. So, you know, order of magnitude better, but they're probably still using the exact same current shunt resistor. And for you power trainee fanboys, there you go,

**Dave Jones:** International Rectifier. Can't quite make out that number on the LCD, but I'll read that back, include the data sheet. They're probably like matching devices in there all the way along. So, I've got it as I said, it's difficult to get this

**Dave Jones:** board out, so I'm not going to bother to see the other ones, but each channel has six of those, and presumably the A model with the 60 amp capability is going to have the extra two, so it'd have eight

**Dave Jones:** devices per side. There's certainly been a bit how you doing with the heatsink compound in there. Check that out. Geez. So, I'd like to go into more detail in trying to get that board out, but it looks a

**Dave Jones:** little bit ugly. I don't I don't think we're going to learn a huge amount more. Just suffice it to say it suffice it to say that this thing is quite well designed and manufactured. I I can't find any issues with this thing at all.

**Dave Jones:** So, up yeah. I'm just excited to power it up and have a little play with it. Not sure if you can see that, but the buggers have lasered off the markings on these four SO8 packages here around the

**Dave Jones:** current sense amp. STOP IT. JUST STOP IT. AND THEY'VE done the same bloody thing for the op amp around the MOSFETS THERE. WHY? AH, UNBELIEVABLE. Just see if we can see the other down in there. Not sure. Can't see it on the LCD. And

**Dave Jones:** that connected down in there, obviously going off to the sense wires on the front panel. Got a relay. Notice the isolation slot, and also some input divider or and or protection resistors. And once again, more high voltage slots

**Dave Jones:** there. Only 150 volts, so you know, you needn't do that sort of thing for those sorts of voltages, but hey, overvoltage and stuff like that, no worries. But it does show nice attention to detail and more slots cut around here. So, yeah, somebody just

**Dave Jones:** went "Yeah, I'll put a slot in cuz that's the thing to do." And I'm not sure what's going on with those plated holes input -1 2 3 4. Like, I don't get it because they're just one big copper

**Dave Jones:** pad with plated through holes. Um I don't know. They're not like current uh shunt jumpers or anything like that for big current shunts. Obviously, some sort of extra mechanical interface which they didn't use. They went for the other two

**Dave Jones:** big bolts down there, perhaps. Hm. All right. So, let's power this baby up and have a quick play around with it. Self-test, all righty-ho. Come on. You can do it. Wonder what OS it's running. Come on. It's only an electronic load.

**Dave Jones:** Self-test. Twiddle thumbs, twiddle thumbs, and here we go. We're in like Flynn. Now, I don't mind the interface. It's not too bad at all. Displays the current voltage with four-digit precision. Thank you very much. And we do get, even though this is

**Dave Jones:** not the A model, we do get the 0.1 milliamps. At least the display digit is there anyway. So, that is definitely 0.1 milliamps whether or not, you know, it could be as I said, just a software thing and it just counts up in 10s and

**Dave Jones:** only has 1 milliamp resolution. I don't know. But anyway, it displays our power and our resistance as well. So, let's put it in constant current mode. So, ranges here, we've got 40 amps and 4 amps. So, that doesn't give us it doesn't change our

**Dave Jones:** display resolution at all anyway. So, that's rather interesting. Our slew rate, our, uh, V on where it uh, switches on at, our voltage limit, 180 volts. It's 150 volts supply, so why it's 180 volts I don't know. And our

**Dave Jones:** constant current limit up to 70 amps. Once again, this is only a 40 amp supply. So, what's going on there? And by the way, if I start using the knob, there is no velocity control. Ah, why? It's not hard to implement a

**Dave Jones:** proper velocity control for that. That's just ridiculous. So, I can just type in one like that, and there you go. And I got to press like 1 amp, there it is, but like, give me a velocity control. It doesn't

**Dave Jones:** work on any of the, uh, input parameters at all. So, on constant voltage range, we have our selectable 15 volts or 150 volt range. That's all right, no worries. And our voltage, once again, the knob is almost useless. Ah, it's

**Dave Jones:** only for fine control. Frustrating. Anyway, uh, we can set our voltage limit and our current limit once again. And our constant resistance range, there you go. Anywhere from, whoop, which, anywhere down to 2 ohms on the 15 k ohm

**Dave Jones:** range, but it also has a 15 ohm, uh, range as well. 15 ohm range as well. And our resistance can go down to 80 milliohms there. Neat. And our constant power mode, we don't have any ranges on that. It's just fixed

**Dave Jones:** at the, uh, watt level. So, let's actually enter 200 watts, cuz that's our limit. Can we go above that? No, of course we can't. Boom. Whoop. Nope. Uh, setting has exceeded the power upper limit. Thank you. Then we've got our

**Dave Jones:** other function modes here. Let's, uh, continuous, config guide. I like this, how it's all just coming up like that. That is very comprehensive and pulse config guide. Once again, look at all the parameters you can set. Very nice.

**Dave Jones:** Read, apply. How do you Okay, we'll have to set those somewhere else presumably. Toggle config guide and then you've got the list mode as well. Automatically goes into the graph here. Shows you all your relevant parameters in a quite

**Dave Jones:** decent font there and I'm liking this. I really am. It's quite neat. Anyway, the list thing is like a a step-based sequence type mode you can go to. Useful for systematized power supply testing things like that. Now, what I'm really

**Dave Jones:** interested in is the battery mode and let's have a look. Once again, voltage and current displayed, milliamp hours, watt hours, which is what you know, the true capacity of a battery, our timer there, but unfortunately we can set the current. We can set our

**Dave Jones:** range from 4 amps or 40 amps. We can set our stop voltage. We can set our current stop as well and our or a timer-based stop, but we can't set a stop value on our watt hours. Why not? It's just a software thing. It can

**Dave Jones:** only do milliamp hours. You can't stop on watt hours. Like and that's where it'll switch on with the on voltage. Like just give me watt hours. Anyway, let's click the Illuminati button and see what that does. Oh, that's our

**Dave Jones:** graph. That's our graph. You can start to see it starting to accumulate there. So, the unlabeled Illuminati button, some people say I put this on Twitter and they said, "Oh, it's the CBS logo." Like I have no idea about CBS. So, yeah,

**Dave Jones:** whatever. It's the Illuminati button and yeah, we've got our graph mode. So, that means that in when you're in say constant current mode, you can do the graph. So, it's totally dependent upon constant power, depending on which mode you're in. I don't mind

**Dave Jones:** that. They could have bloody labeled it though. And then the other modes is our over current protection mode. You can just sequence like do a step sequence mode for testing your supplies for power and current. So, that's not bad at all.

**Dave Jones:** I like those three apps built in. And it looks like our on off button, there it is. Load just comes up. Tran whoop. Presumably, transient. And what a short do? Does it short out the terminals? I don't know what short does.

**Dave Jones:** RTFM. The most annoying part about this though is that I cannot select anything but constant current discharge. I mean, what if I want to test constant constant resistance mode, which is in the data sheets for you know, toy testing and

**Dave Jones:** things like that. I can't do it. I got constant current only. It's ridiculous. This is like just a software limitation. Why have a complete battery mode like this if that's all you're going to be able to do? It's ridiculous. Now for the

**Dave Jones:** finger test on these heat sinks down in here. Of course, this one's where we're not dumping any load into this at all. So, of course, that's completely cold. These linear regs down here, back of the finger. Hang on. It is Ry

**Dave Jones:** Gall, so Ah, yay. Yay. Bloody hell, that's too hot to touch. Unbelievable. Have they done it again? Okay, so that one there is 80°. Come on. This is not a rocket science, Ry Gall. That is too hot for a simple

**Dave Jones:** supply. I mean, like the junction temperature has like is well above that. That's just that like granted, okay, we don't have the top in the case. So, we got like I can sort of put the case back I can Well, I can put something on the

**Dave Jones:** top and that's going to simulate the airflow. Let me do that, but that's just That's just wrong. I'm afraid that the one next to it there is even worse. This one's up to 88. Ah, unbelievable. Okay, I've put the lid on the top and

**Dave Jones:** you can see it going down. It's dropping. I've got like just boxes on the top like that just to simulate cuz the air in the side in the intakes going to be the same. Okay, it's getting down towards 75°. So, yeah,

**Dave Jones:** that's knocking like 13° off, but that is still just no excuse for being that high for a basic linear regulator when you have all that space inside. It's just insane. Now, and that's not to say that it's like, you know, going to fail or

**Dave Jones:** anything like that. There's still margin inside, you know, the die temperature of a 7805 or whatever can go up to What is it? 120° C or something. But so, it's not going to fail. I don't recall that being a

**Dave Jones:** nearly as bad as I think it was over 100° for the for the DP832 power supply which they had to fix, but come on. No. No. No. No. No. No. Now, curiously, the Rigol DP832 powers up much, much

**Dave Jones:** quicker than the electronic load. Why? They've I can't remember the teardown, but they've changed our processors or whatnot and maybe changed OS. I don't know. What's going on? But there's a huge difference. I mean, that's fine. This one takes forever, but meh, whatever.

**Dave Jones:** Now, I've got it uh hooked up to the 832. I've got simple constant current load of 1 amp. Uh we're getting 1.004 over here, and we're getting 0.997 8. That's like a discrepancy of 0.6% between them. Um What the? That's way out of spec. Oh,

**Dave Jones:** duh. I'm on the 40 amp range. Let's go Up. What? Turn off the load. You can't change ranges unless you uh have the load turned off. There we go. 4 amp range. Uh No. It's exactly the same. Uh Like, assuming that Let's just assume

**Dave Jones:** that it's 1 amp. That's like 0.3% out uh 0.2% out. It's supposed to be 0.05% plus 0.05% full scale. Seems out of spec. And let's just uh check the voltage. 29.977 and right on the terminals where it should be measuring it, 29.981.

**Dave Jones:** It's not too far off, but technically, that might be close to or out of spec as well. Okay, people wanted to know the current. Well, it looks like the DP832 is bang on, 1.005. I'm not going to quibble one least significant digit uh

**Dave Jones:** compared to the 7 1/2 digit uh Keysight here. So, we're going to take that as absolute uh because yeah, its accuracy is like order of magnitude better or something than what we've uh got here, and we're getting 0.998.

**Dave Jones:** One. That's out of spec. Rigol, please explain. Okay, let's do our dreaded constant resistance mode. We've got it set to uh 10 ohms. Let's switch on our supply here, and absolutely nothing. I switched it down to 2 ohms. We're

**Dave Jones:** getting no hiccup in at all, even though you can see that the 3 amp current limit is enabled on the DP832. Nothing's hiccup in. Nope. Stable as. And the short button does exactly what you expect. It shorts it

**Dave Jones:** out. 0.01 ohms. Um so, it doesn't do that with a relay. It does that using the using the MOSFET load to actually do that. Now, as for the graph functionality on this thing, the Illuminati mode, um it's there's no way like you can't like

**Dave Jones:** there's no auto scale button or anything like that to just like auto scale that in. That would have been really nice. Um please implement something like that. Just so that you can see the fine detail in there. And we can choose our data.

**Dave Jones:** Current U is voltage, R is resistance, P is power. Why can't we do the voltage and current on the same graph? Why can't we have another Y axis over here and uh do them in different colors? Um yeah, please. That'd be nice. And I've

**Dave Jones:** plugged in my USB stick here. It says it was detected, and I'm going to print. Saving image. Great. I love that feature. Presumably, hopefully, um but what? Failed. Why? Uh Okay. Let's try another USB stick. Maybe it wasn't the right format or capacity

**Dave Jones:** or whatnot. Saving image. Come on. Unbelievable. Hey, check this out. I was just logging here. I pressed the utility button. It switches off the bloody output. Look. Why? That's ridiculous. Look at this. It does the same thing. It

**Dave Jones:** doesn't do it for option, but it does it for store. You push the bloody store button and it's there. Anyway, look, it looks like there's a D drive there. I presume that cow data is that the C is probably

**Dave Jones:** internal. How do we get to D? Like that. There's a D drive there. Save. I don't know. Okay, whatever. Uh what? What? Okay. I don't know. Do we have to do D Do we have to select D before we did the bloody print thing?

**Dave Jones:** Is that what's going on here? How do you get rid of that? Oh, look at Wow, it just ah Ah, on. Okay, print. Saving image. It's going to work this dot failed. Yay! I think I finally found a USB stick that

**Dave Jones:** actually worked. It just says saving image and saving. Oh, thank goodness. Huh, and it saves it in bitmap format. How quaint. Okay, let's go into the utility here. Have a look at the all the interface stuff. GPIB, nice. USB,

**Dave Jones:** RS232, nice. All the requisite stuff and LXI LAN as well. That's I'm sure that'll work a treat. And there's the firmware versions and stuff for those playing along at home. Uh system boot time times been booted 34 times

**Dave Jones:** FPGA version all the requisite stuff. Last calibrated 1st of the 9th. And yep, you betcha, we've got software options LAN official digital IO high resolution official. The like I Is that the A version? Have I been upgraded? I don't know. Slew rate

**Dave Jones:** and frequency cuz they those three things, the high resolution slew rate and frequency, seem to have been the major differentiators with the A version. So, I don't know. Have I been uh given the A version and no sticker on

**Dave Jones:** it? Um install I So, maybe I have. Now, I don't mind the uh list mode here. It actually works quite good. Uh basically, you set the number of steps that you want as six maximum. I'm not sure. Anyway, what what can we go up to? No.

**Dave Jones:** Heaps. So, anyway, we can set it back to two. So, we'll go two steps, and then I've set uh I you just use cursor keys over here just to set Okay, we want 1 amp. We're in constant current mode. We can change

**Dave Jones:** our range. So, we want 1 amp 1 amp for a duration of 1 second, and then we want uh 2 amps for a duration of 1 second, and circles I loop, you know, how many times you want to loop through. So, we can now run

**Dave Jones:** that, and it should hopefully No. What's it doing? Huh? Well, why isn't it going on to the next step? Hello. McFly. One other thing I noticed, if you've actually got this on and you go to something else, it just it'll go

**Dave Jones:** to that mode and switch it off. You shouldn't be able to do that. That's just wrong. You should uh you know, it should tell you sorry, you know, you've got to switch it off. Cuz you usually when you switch it on, you're doing

**Dave Jones:** something. You don't want to accidentally hit buttons and cause it to goof up. Now, it looks like why this isn't working may the trigger it needs to trigger to go to each state. It doesn't automatically do it based on the

**Dave Jones:** duration. You can do uh trans transient. Um I'm not sure what's going on there. Uh bus uh bus triggering? Uh is that like your interfaces, your RS232s, and uh LAN and whatnot, or your digital IO interface where you can feed in external

**Dave Jones:** signal and cause it to step through, but there's no like time-based mode or automatic or anything like that. So, that when we start this, it just stays in the same duration there, and it's 1 second. It doesn't automatically go to

**Dave Jones:** the next. So, I'm not sure what's going on there. RTFM maybe? Aha, tran tran button. Let's go. There we go. Let's press it.

**Dave Jones:** Yes, there we go. It's sequencing through. There you go. You can see it's sequencing through. Green on each Oh, no, sorry, cuz it only cycled through huh twice. We only had number two circles, but there you go. You saw it.

**Dave Jones:** You can sequence through. Nice. And you can apparently uh record that to USB as well. So, if I go back, well, no, I just pressed on, and then trans, and boom boom boom boom boom boom. And it should end, and it ended the

**Dave Jones:** recording, did it? Let's see what we got. Well, that's lame. All it did was record the voltage. Why can't it record all the parameters here for each step? That's just it's just dumb. Okay, I'm going to do a

**Dave Jones:** battery discharge test. I've got a Duracell Ultra in there, fresh out of the pack. You can see I'm using the external sense lines here. I've just got it hacked in there a bit. How you doing? And I'm going to do a very brutal 1-amp

**Dave Jones:** constant current discharge, because you can't do anything else. You can't do constant resistance or anything. Bloody ridiculous. Anyway, um I've got the stop voltage set to 0.8 volts. I don't care about the uh timeout. I don't care the

**Dave Jones:** current uh timeout. I don't care about stopping 0.5 volts turn on. Everything's hunky-dory. It doesn't matter whether I not I go out of battery mode. It shows I was mucking around just with one before um just to make sure the setup works,

**Dave Jones:** and um it shows the previous info there. It doesn't clear it. Even if I uh go in there and you know, change the change the app or whatever. Look, anyway, um let's do it. Let's start it, shall we? So, here we go. Constant

**Dave Jones:** current discharge, uh 1 amp. And we should presumably these will clear, the time will reset, and we'll start again. Let's give it a whirl.

**Dave Jones:** There we go. All right. Uh it's dropping. It's dropping fairly drastically already, as you'd expect, because it's pretty brutal, 1 amp on a poor um innocent AAA cell. But anyway, it will eventually get a figure here. Now, we can actually call up the graph.

**Dave Jones:** Okay? Look, there it is, right? It'll start, but we can't choose both. Like, we can't get the figure. Like, it's just like a like a Why can't I have all the information on here and it resets the graph? What

**Dave Jones:** the hell is going on here? Like, I can't do both. That is just ridiculous. And we're done. That didn't take long at all. Battery test completed. I assume I press okay to get rid of that. And there it is, of

**Dave Jones:** course, that the load is disconnected. As so, the voltage is actually recovering. It would have gone down to 0.8 volts on the terminals of the battery cuz we are doing the voltage sense down here. And there you go. For

**Dave Jones:** the record, 263 milliamp hours or 0.268 watt hours for a 1 amp discharge on a basically one of the best double A you can get, the Duracell Ultra. So, yeah, it's not great because AAA's aren't designed to handle 1 amp constant

**Dave Jones:** current loads. That's just crazy, you know? You'd use a AAA or higher for something like that. But there you go. It works, but yeah, it's it's crude. And look, go into our graph. Where's our graph? Where's our data? Like, it's just

**Dave Jones:** ridiculous. Can we play back? Can we play back? Oh, maybe we should have pressed record and it would have dumped it to the USB stick, damn it. USB was not detected. We've got to press record. Okay. Oh. But to record like this, I've got to be

**Dave Jones:** in the Illuminati mode, right? So, I got like I don't know. Back? Can I like go if I go out of there? Is it Oh, no, it's still in record. So, maybe that actually works. Maybe that is going

**Dave Jones:** to work. Here we go. I'll start it again. Bingo. There's a bit more capacity left in that battery, of course, due to the electrochemistry recovery in there due to the very steep discharge, but hopefully, we're actually dumping that

**Dave Jones:** to the USB stick. So, that'll be done in short order. We'll only get another few tens of milliamp hours out of that puppy, surely. Okay, we're done. Didn't take long at all. We got an extra 23 milliamp hours

**Dave Jones:** out of that. There you go. And once again, it's recovering. And presumably, if we go back to the gra- It's recording like I don't know. Do I just take the USB stick out? Like, do I press unrecord? What do I do? Like, I don't I think it's

**Dave Jones:** only going to record I'd be very surprised if it actually recorded this data. Well, I think I'm going to call it quits on uh having a play around with this thing for now. This was not designed to be a full review. It was just a teardown

**Dave Jones:** and initial uh play around. And the kind of initial verdict is like like I don't mind the design and build of it apart from that ridiculously hot Well, not as ridiculously hot as the DP832 that heatsink inside there. I

**Dave Jones:** Anyway, the design of the front panel isn't the best. Those fonts are ridiculous, but at the end of the day, that doesn't really uh matter. It's about the functionality of it. I was disappointed by the battery mode. Some

**Dave Jones:** of the other uh modes are, you know, like it it has all your basic load functionality. It would take, by the way, a lot of work to extensively test all the different modes of a uh advanced electronic load like this one. So, yeah,

**Dave Jones:** that would like be a 40-minute video in its own right, I think, if I did that. But, um there's like just basic things missing from the battery test, the display mode and stuff. The USB was it has to be a a

**Dave Jones:** certain format, and it didn't even tell me that it was wrong, and it's just uh there appears to be uh accuracy issues with this thing. Maybe more extensive uh requirements on that, you know, like it's only an amp, it's not like a 40

**Dave Jones:** amps or whatever. It was like it it should have been better than that. So, I don't know what's going on there. Rigol need to look at that, and I don't know, there's just not a huge amount of spit

**Dave Jones:** and polish on this thing. It's like, "Yeah, okay, it's a load, it'll do the basic job." But, there seems to be, you know, quite a few issues with it, which they can fix in firmware updates and uh stuff like that. But, um initial

**Dave Jones:** impressions are that it's just a run-of-the-mill electronic load, really. Um you know, bang for buck, there are better ones. Uh just you you know, if you just want a basic electronic load, you can get one for two, 300 bucks on eBay, one of those

**Dave Jones:** rip-off uh brands, and they do more than an adequate uh job just for a basic electronic load for testing uh power supplies or uh something like that. So, at the end of the day, it's like nothing hugely to recommend this thing yet. It,

**Dave Jones:** you know, if it they improve the uh functionality and solve the uh whatever accuracy issues it might have, and if they gave you the A model, all of it, like I don't I presume that mine has the extra A uh functionality, but it doesn't

**Dave Jones:** have the uh label on there. But, those options are a ridiculous price. Like, what was it? 400 bucks? Or was it double or something just to get the A model? It's It's crazy. Just have one freaking model. Um maybe two if you want the

**Dave Jones:** difference between the uh 300 W and the 200 W model, fine. But, uh like it doesn't justify the price difference. So, no, they haven't got themselves a killer electronic load here, I'm afraid. Um it's just meh, another electronic load on the

**Dave Jones:** market. They've all got their own little quirks and issues and whatnot. And this one is no exception. So, there you go. If you like this look at the Rigol DL3021, please give it a big thumbs up. Full of frame, thumbs up. And if you

**Dave Jones:** want to discuss it, down below. Catch you next time.
