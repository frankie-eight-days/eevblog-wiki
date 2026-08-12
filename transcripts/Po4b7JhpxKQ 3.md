---
video_id: Po4b7JhpxKQ
title: EEVblog #1283- What is Mains Ripple Injection?
url: https://www.youtube.com/watch?v=Po4b7JhpxKQ
source: youtube-asr
timestamps: {"0": 1, "1": 13, "2": 23, "3": 36, "4": 47, "5": 63, "6": 79, "7": 90, "8": 104, "9": 140, "10": 163, "11": 187, "12": 199, "13": 214, "14": 234, "15": 251, "16": 272, "17": 282, "18": 296, "19": 310, "20": 322, "21": 332, "22": 347, "23": 359, "24": 372, "25": 385, "26": 404, "27": 414, "28": 427, "29": 437, "30": 450, "31": 458, "32": 471, "33": 486, "34": 495, "35": 517, "36": 526, "37": 545, "38": 559, "39": 578, "40": 585, "41": 601, "42": 613, "43": 628, "44": 640, "45": 660, "46": 672, "47": 688, "48": 699, "49": 710, "50": 725, "51": 749, "52": 766, "53": 778, "54": 793, "55": 806, "56": 827, "57": 836, "58": 848, "59": 864, "60": 876, "61": 891, "62": 908, "63": 919, "64": 935, "65": 944, "66": 955, "67": 973, "68": 997, "69": 1010, "70": 1024, "71": 1046, "72": 1063, "73": 1081, "74": 1102, "75": 1126, "76": 1139, "77": 1154, "78": 1165, "79": 1196, "80": 1204, "81": 1218, "82": 1232, "83": 1248, "84": 1262, "85": 1272, "86": 1278, "87": 1291, "88": 1302, "89": 1312, "90": 1324, "91": 1339, "92": 1351, "93": 1366, "94": 1379, "95": 1395, "96": 1405, "97": 1416, "98": 1430, "99": 1441, "100": 1453, "101": 1463, "102": 1471, "103": 1482, "104": 1492, "105": 1506}
---

**Dave Jones:** Hi, it's random bunker/dumpster item. I found this one in the previous that monster dumpster thing I found offsite. So, I'll link in that video at the end of that below if you haven't seen it.

**Dave Jones:** And I have no idea what this is, but it looked interesting. And of course, I love these thumbwheel switches. They're always fantastic. If you ever see one of those on a bit of kit, make sure you salvage them.

**Dave Jones:** They're great for the junk bin for various projects. And it's got some DIP switches and Zelweger, never heard of them. It's some sort of receiver test unit. So, it's not a receiver.

**Dave Jones:** Presumably, it transmits to a receiver and tests out receivers. We've got a power switch, FS out, full scale out, I guess. Decabit? What the heck is a decabit? And K22?

**Dave Jones:** I have no idea. We can set a level trimmer active, transmit. That's a momentary action switch. So, that'll be like a It's like transmits a pulse of various frequencies.

**Dave Jones:** And there's the list of frequencies on the back here. So, anywhere from 167 hertz all the way up to 2 kilohertz. There, you just set the DIP switch. But the back here is really kind of gives the game away, I think anyway.

**Dave Jones:** I'm not sure why it's just got a regular mains power cord. It doesn't have the insulation. So, this is right really old school before the regulations that we had put the insulation on the pins.

**Dave Jones:** Anyway, for some reason it goes through a neutral thing, but I think that's they're just like using that as a like a grommet entry. But I guess they had some other purpose for it at some stage.

**Dave Jones:** But anyway, we've got two different fuses on here. And we've got shrouded 4 mm active and RN, which would be return neutral, I'd be guessing. So, given that this thing transmits like lowish frequency stuff and we've got mains in and it looks like mains out with some fuses, I'd say this is designed for injecting those control signals onto control frequencies, control signals, control data, whatever it is, onto mains lines

**Dave Jones:** which actually controls various appliances and stuff like that. Now, this might be very different in other countries. I've got no idea. Please leave it in the comments down below for your particular country and what it's like, but here in Australia we have what's called off-peak electricity and which means that particularly for hot water, like the real high energy intensity stuff in everyone's home, if you've got an electric hot water system,

**Dave Jones:** then if you have those coming on during the day, that's when you're paying like peak prices for electricity. So, what they do is they superimpose a signal onto the 50 hertz mains, not that 60 hertz rubbish here in Australia, and then that a signal activates some detection circuitry inside your fuse box which then either turns on or off your hot water system at during like off-peak times, it

**Dave Jones:** might be after midnight for example, when it's really cheap. So, not only does that lower the grid load during peak times, you know, when during the day businesses and everything's going and all that sort of stuff, they've got to like balance the load out.

**Dave Jones:** Midnight, not not not much is happening, so that's when you want to sort of like load up the grid with people's electric hot water during the night time. So, they can control that, they can control other things like street lights and other mains type infrastructure.

**Dave Jones:** And it's not uncommon for these mains control frequencies to actually upset some particular products cuz they've got, you know, little modulated high frequency signals on there and it can cause, you know, things lights to flicker and other, you know, things to happen um products if they're not well designed and well filtered and stuff like that.

**Dave Jones:** Anyway, that is my guess what this thing does. So, we won't turn it on. We'll take it apart and uh see if my suspicion is correct cuz I think that's I unless it's some sort of like, you know, some other custom industrial thing, I think that's what it's uh going to be doing.

**Dave Jones:** I don't know who Anemite is. Anyway, serial number 129. Geez, didn't make many. Anyway, it's in a classic uh Pac-Tec project case like this. Tons of products are made into Pac-Tec was like a brand back in the uh '70s, '80s uh '80s I think these were uh popular these uh Pac-Tec cases.

**Dave Jones:** You can still buy them. Um so, I just call them that. That's just a generic brand anyway. And I'm undoing a Phillips screw with a flathead screwdriver. Sue me.

**Dave Jones:** Anyway, let's crack it open. Is that Come on. And we're in like Flynn. Check it out. Wow, that's not uh old school through-hole stuff, but um yeah, all right.

**Dave Jones:** Let's see what's going on here. Okay, first things first, we've got an EEPROM here. Uh 1991 vintage, so there you go. It's not new. Uh so, oh jeez, that's that's 30 years old now, almost.

**Dave Jones:** Crikey. Uh I'll have a look what all that bundled up cable is later, but let's follow the money here. And okay, so we've got mains input. Let's follow the money.

**Dave Jones:** Heh. Heat shrunk. That's going over Ah ah check it out. That's going over to a uh C&K toggle switch. That's the power switch on the front. C&K toggle switch.

**Dave Jones:** Those things are uh 250-V mains rated, but yeah, it's pretty how you doing because if you get solder dags on there, they can get very close to the metal over here.

**Dave Jones:** So, this front panel, I don't think it's earth at all. So, yeah, not the best. Old school bugger safety, bugger clearance. Anyway, so our mains is switching there. It's Oh, okay.

**Dave Jones:** Yeah, it's coming back over here and it's going to the fuse. Okay. So, that is our input mains fuse after the switch and then it buggers off down to the board down here into a mains here.

**Dave Jones:** So, that's just a PCB mount 240 V primary and looks like a couple of windings on the secondary. Maybe two AC low voltage AC secondary windings. But, it also jumps over to here.

**Dave Jones:** So, aha, right away, this active output goes directly from the mains active over to here. So, obviously, if they're injecting anything, it's going to be on the return neutral here and aha, what's this transformer for?

**Dave Jones:** So, let's anyway, let's follow the neutral down here. Blue goes down to the board. Just got some mob protection down in there. Diode bridge. Oh, look, there's a bunch wire.

**Dave Jones:** That blue wire That blue wire is coming Oh, that's Is that some sort of Wow. Oh, hang on. Hang on. Oh, there you go. What Why it has to be that long?

**Dave Jones:** Have they got something in that? We'll have a look at that later. Let's follow the neutral. So, neutral goes down to the board. That'll be going over to the transformer over here as well.

**Dave Jones:** The return neutral here doesn't connect over to here. It goes through this other fuse and goes through this transformer here. Aha, so yeah, that would be going I bet you there's a trace going from there.

**Dave Jones:** Yeah, I can see it on the board through the board. Trace from there to there. So, that's our supply transformer for our circuitry and I believe it'll be going over there as well.

**Dave Jones:** So, it's going into this transformer. So, this is our signal coupling transformer in the neutral line, which goes out here. So, that makes sense. So, yep, I was right.

**Dave Jones:** It is injecting frequencies onto the mains neutral line. And then, it looks like we just got a couple of switching down in there, do we? For the secondary side of that injection transformer, we'll call that.

**Dave Jones:** And is that not an EEPROM? That might be a That might be a micro, unless that one's a micro, but it doesn't look like it. And nope, that's not a micro.

**Dave Jones:** That's a D71054, and that's a programmable timer chippy type thing. So, that's got to be a micro under there. All right. So, given the vintage, my money is on an EEPROM programmable PIC chip.

**Dave Jones:** That's where my money's at. Am I right? Ah, it's upside down. All the electrons are going to fall out. Ah! No! I was off the off the money. It is a big M, but it's not Microchip.

**Dave Jones:** It's a Motorola 60 68705 EEPROM version. Ah, beautiful. None of that E squared prom rubbish. And like I said, these thumbwheel switches, these are absolutely fantastic things. This one's actually great, cuz it's got a plus minus on there.

**Dave Jones:** That's really quite nice. But, these things are absolutely gorgeous. So, this dials in the command. So, obviously, like it's going to encode like a word, you know, a byte or word or whatever, onto the mains.

**Dave Jones:** And you just dial in the frequency. The trimpot here, curiously, goes over to three over there, which So, maybe that's like a you know, LM317 regulator or something, and it just sets adjusts the level or something like that.

**Dave Jones:** I don't know. There's not much else in there. Just a 74HC series logic. So, I'm not even going to bother to take that board out. There's nothing more interesting to see.

**Dave Jones:** What's going to be more interesting is if we actually power this thing up and have a look. And then I might do some Googley searching for this deck of it K22 cuz that's obviously some sort of protocol and Zellweger.

**Dave Jones:** Wonder if they're still around. Now, this is interesting. All this cable here, there's nothing. These two were all wired together. And if I pull that, yep. Just two bare wires in there.

**Dave Jones:** So, they weren't they're not electrically connected. What they're doing I think is using this as a capacitor. It's like a I don't know why it has to be that long.

**Dave Jones:** Maybe like they're increasing the capacitance or something. But they're using that as a capacitor. Oh, why you'd have the ends like tinned like that? Because what it's doing is it's tapping off the bridge rectifier down in there.

**Dave Jones:** It's tapping off the negative output of the bridge rectifier. So, it's tapping off that and then it's going into a 74HCT02. I can only presume that that is something to do with like they're detecting when the mains switches.

**Dave Jones:** That's their crude method of doing that. Wow. Pretty how you doing? So, anyway, a HCT02 is a quad NOR gate of course. It's going into it's soldered onto the pin there, pin three.

**Dave Jones:** So, that's one of the inputs of the first gate there. And so, they're yeah, like AC coupling in and the mains I've done that before in my clock mains clock circuit that I built when I was a teenager.

**Dave Jones:** Maybe I have to link in the video. It wasn't quite like that. You do AC couple it, but jeez, you know, wires like it's not like you need some huge voltage isolation or something.

**Dave Jones:** Anyway, seems a bit silly buggers, but that's what they decided to do. What? And I forgot to show you that it did have a neon light. So, is that Yeah, it's actually trust me, it's on.

**Dave Jones:** It's just really faint. Anyway, we've got on slash error, so I don't know why the red thing's flashing, but anyway, it's flashing and we've got it hooked up on our output here.

**Dave Jones:** I've got no load connected, so I've got my EEVblog high voltage probe here because it's a proper way to safely measure mains voltage and other stuff. Anyway, so we are at 704 volts peak-to-peak, 245 volts AC RMS because yes, my mains voltage here in the lab and at home as well is right on the high side of the allowable limit.

**Dave Jones:** It's like 246, 247 commonly, so it's getting up there. Even though Australia is supposed to be nominally 230 volts, not 240. Anyway, so we've got a signal there. I've got it set to deck a bit, and I'm going to pulse the transmit, and I don't see anything pulsing on there.

**Dave Jones:** So, maybe I need to set the dip switches. And adjusting the level here gets me zippity doodah. Not sure what the deal is. K22, it's still flashing. I presume it's flashing error.

**Dave Jones:** And I've connected this FS output to the scope as well, and I'm triggering from that. Presumably, it's a 5-volt TTL signal, and I'm still getting still getting nothing. I can't There's just nothing coming out of that.

**Dave Jones:** So, there is genuinely an error there. Whoa, hang on. I just played around with the code here, and it stopped flashing. Look. I was I was going up 969.

**Dave Jones:** 169. Wow, okay. 069 will that Aha, got it. Got it. It's a code. Oh, active. There we go. So, here we go. I'll just hit active. So, it's transmitting and boop foot flash flash flishy flash and then that one's not labeled and the active turns off.

**Dave Jones:** So, it transmits for like 5 seconds or something and then switches off. Oh, 69 winner. Okay, so what I'm going to do is actually uh single shot capture this.

**Dave Jones:** There we go. And the it looks like there's no data encoded on that. So, I don't know what that FS output is just like a clock. Nope, silly me.

**Dave Jones:** I just wasn't thinking fourth-dimensionally. Let's do that again. Slower time base and bingo, we of course have a uh there's the data encoded there. So, that is 69 encoded in I presume deca bit.

**Dave Jones:** Um critical, I guess. Okay, I'm just going to repeat that same thing. So, that's 69. I'm going to repeat it with the uh that's positive 69. I'm going to repeat it with 000.

**Dave Jones:** So, let's try that again. Single shot capture, trigger. Yeah, that is different to Yeah, that's different to what we had before. Yep, so it's encoding that on there. Let me do a higher frequency.

**Dave Jones:** Actually, this thing's pretty intelligent. Check it out. If you just like randomly flip the dip switches, it gives you an error. So, it knows that uh you know, you're either not selected a proper frequency or you haven't selected a and or a uh proper command on this.

**Dave Jones:** Let's go to 2 kHz. So, I need 1 3 4 and 6 on. No? 1 3 4 and 6. Um that should be right. Aha, they're actually grayed out.

**Dave Jones:** So, I'll go for 1 2 4 and 6. 1 2 4 and 6. There you go. So, it knows. That's brilliant. So, let's trigger that again, shall we? Single shot capture.

**Dave Jones:** Oh, yeah, we've got some higher frequency switching stuff in there. I can see it. But, because this is AC coupled, it's a bit how you doing? And there you go.

**Dave Jones:** That's just a higher frequency clock. Sure enough, if we measure that frequency of channel 2 1.59 kHz. I've got it set to 1,600. Good enough for Australia. Might get more accurate if I go in.

**Dave Jones:** But, 1.584. There you go. So, yeah, that just changes the clock rate. Effectively, it looks like like the data rate like the modulation rate is the same, but the frequency just sets the higher clock rate.

**Dave Jones:** That's interesting. And even a sticking a 50-W load on this thing, unfortunately, um still doesn't do anything. The yellow is the mains waveform there, and you can see that there's no modulation change at the actual point of switching there.

**Dave Jones:** So, you know, we can go in there and there's just like it's just nothing. So, this thing could be faulty, I suspect. Maybe, you know, the switching training or something like that.

**Dave Jones:** Switching circuitry could be cactus. So, it is supposed to result in like a, you know, 5-10% ripple on your mains there, but obviously, nothing's doing there at all. So, it's got to be faulty.

**Dave Jones:** Anyway, let's go to the Google is and see if we can investigate this Decabit and K22 stuff. As it turns out, there's a Wikipedia page for this. Zelweger off-peak system is a brand name for an electric switching device used to control off peak electrical loads such as water heaters and and uh, and and probably uh, you know, street lamps and other uh, type stuff.

**Dave Jones:** Uh, carry a current it's called like ripple uh, injection stuff like that. Goes under various names, but uh, yeah, uh, Zellweger is one of the big players in here and yeah, they talk about uh, things like uh, stereo amplifier stereos can pick up the noise and all that sort of stuff.

**Dave Jones:** Um, uh, ceiling fans can pick up the uh, can pick up the ripple on there. Um, telephone lines and all sorts of stuff. There you go. In some parts of the Sydney, uh, 1,042 hertz signal usually consists of several bursts of a few seconds off and on for period of up to 50 seconds on coded uh, to affect only selected equipment of course.

**Dave Jones:** Um, there you go. Radioactive risk of one type of Zellweger meter. It contains low risk radioactive material. There you go. Anyway, so that's interesting and there's a uh, thing for bloody Queenslanders up there, some for Sydney, uh, North Coast and stuff like that and it looks like there are different uh, brands and things like that.

**Dave Jones:** So, uh, if we go down here, yeah, technology utilized various hardware telegrams they use K22 decabit LG. Oh, Amemet is um, that company in the land the sticker we had on the back, but of course it's uh, Zellweger and uh, yet the Zellweger standard, but this Zellweger model, maybe they had their own standard, but uh, they support uh, it looks like decabit.

**Dave Jones:** I don't know the history of that. Anyway, these are the different uh, companies Endeavour Energy, Ausgrid and all those sort of uh, Jemena I've heard of. Um, some of them I haven't heard of, but they um, yeah, they have all these different uh, standards.

**Dave Jones:** Decabit um, sounds like one of the major players, but K22's in there too. Then we have this huge document here which I'll link in down below. Ripple injection load control systems Australian power quality and reliability center, and from the University of Wollongong.

**Dave Jones:** It's very comprehensive. So, look, I won't go through the whole thing, whole executive summary and stuff like that. Ripple injection allows access to cheaper off-peak electricity and all that sort of jazz.

**Dave Jones:** Mitigation, there's the ripple injection methods for those playing along at home or into your infrastructure, and it's generally applied at the 11 kV transmission level. Um because there's various step-down voltage phases in the distribution of electricity, and it's typically done at the 11 kV which will then go through the transformers on the street poles or underground or you know, at ground level that then will transform that down to 240 V which goes

**Dave Jones:** to your home and stuff like that. So, there's little schematics there. There you go, check it out. So, they inject it, yeah, coupling capacitors at the substation bus bar there.

**Dave Jones:** And then 11 kV and then it's step down and then it goes into your Yeah, that's the 240 V house. There you go. So, and here's a photo of a typical injection equipment.

**Dave Jones:** I can't see much, but it's got injection capacitors and you know, tuning coils and isolation transformer, compensation caps, absorption coils. Hmm, interesting. Sure you power efficient autos are getting pretty moist right about now.

**Dave Jones:** And here's the K22 protocol coded pulse algorithm. This is from Zellweger as well. So, you know, looks like there they go. They they own the market. There you go, there's the decabit coded pulse and that's I think what we saw.

**Dave Jones:** We just saw like those pulses there on the screen depending on the setting and stuff like that. Unfortunately, we didn't see it rippling on the mains though, unfortunately. So, this is what it's going to look like here, and I actually saw this the other week.

**Dave Jones:** I was doing some mains stuff playing around with it, and I definitely saw that um here in the lab. So, I like hopefully I'll be able to capture it again.

**Dave Jones:** But, obviously that's a time of day thing. I can't even remember when I was testing. It might have been late at night or something like that. So, I might have to I don't know, come in after 10:00 p.m.

**Dave Jones:** or something and try and capture it. But, I did actually see this modulate this ripple modulation um on my mains uh signal on the scope the other day. And of course, I knew exactly what it was um cuz I've seen it many times before.

**Dave Jones:** And yeah, it just pops up occasionally. Um so, if you products aren't So, this is what we would have seen. Uh we would have seen like that it for uh how long's a packet or whatever a second or whatever.

**Dave Jones:** We would have actually seen half a second. We would have actually seen that ripple on there for like half a second then go away. And then that when you have ripple, that's encoded as a one.

**Dave Jones:** And the lack of ripple is encoded as a zero or vice versa, however you want to uh decode it. There you go. Um and that's 750 hertz on a 50 hertz signal.

**Dave Jones:** So, that's what it looks like. So, by all means, safely monitor your own main signal. You can actually do that with a If you want to do it safely So, if you want to do this safely with a crow, yes, crow, um not an oscilloscope rubbish anyway, cuz we're in Australia.

**Dave Jones:** It's crow. Give me a break. Anyway, so if you want to do it safely, um I just use a regular isolation, you know, step down AC step down transformer, 110 or 240 volts down to, you know, 10 volts AC or something like that.

**Dave Jones:** And then you can safely probe the with your regular scope um the, you know, AC signal. And if you sit there long enough and twiddle your thumbs, you'll eventually capture or you might be able to set up a trigger, of course, because uh the levels are reasonably high.

**Dave Jones:** You should be able to set up a trigger unless you get get other glitches on the mains. Maybe you can set up a capture um a peak capture to um get trigger off and single shot capture um some of this uh mains frequency.

**Dave Jones:** So, So, an entire signal injection can run for approximately uh 3 minutes. So, that's actually quite that's quite significant. So, you do stand a good can- chance of a chance of capturing that if you are actually uh probing the mains and looking for it.

**Dave Jones:** Like I said, I just saw I was randomly doing some uh uh unrelated mains testing the other day. I had my high voltage probe hooked up and sure enough, there was the ripple.

**Dave Jones:** So, apparently there is an Australian uh standard for this for those playing along at home, and looks like maybe, you know, 4 to 6% uh modulation value. So, that's uh quite substantial.

**Dave Jones:** You should definitely be able to see it. And they tell you that uh receiving relays, that'd be like in your fuse box to uh decode this, can work down to signals of approximately 2 V, but signal levels due to amplification of up to 30 V have been recorded in the field.

**Dave Jones:** Um it's it was only approximately uh 5 V might be a typical uh injected thing for uh 240 V signal. So, there you go. That's uh fascinating stuff. Shame it didn't work.

**Dave Jones:** I could maybe attempt a troubleshoot and repair and see why it's not actually injecting uh this stuff. It's coming out of the BNC connector, but yeah, maybe one of the switching has gone or uh something like that, perhaps.

**Dave Jones:** But, it's fascinating how you can get this ripply stuff on your mains. So, if you ever see something like that, and it looks a bit how you doing like this, you know what it is.

**Dave Jones:** So, let us know in other countries cuz I have no idea if this is uh just you know, an Aussie thing. I believe it's in New Zealand as well, or whether or not this is a common in your country.

**Dave Jones:** Do you get uh this or what do you call it? Is it, you know, off-peak uh ripple? Is it ripple injection? Is it called something else? And what are the uh typical Who are the players in the market?

**Dave Jones:** Cuz Zelweger seem to own the market here by looks of things, and let us know in the comments down below. So, I hope you enjoyed that video. If you did, please give it a big a thumbs up.

**Dave Jones:** And as always, you can discuss it down below and over on the EV blog forum and subscribe over on EVblog.tv if you want decentralized instead of this centralized YouTube rubbish.

**Dave Jones:** Catch you next time.
