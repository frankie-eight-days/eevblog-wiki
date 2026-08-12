---
video_id: Po4b7JhpxKQ
title: EEVblog #1283- What is Mains Ripple Injection?
url: https://www.youtube.com/watch?v=Po4b7JhpxKQ
source: youtube-asr
timestamps: {"0": 1, "1": 16, "2": 29, "3": 44, "4": 63, "5": 79, "6": 93, "7": 109, "8": 128, "9": 147, "10": 160, "11": 175, "12": 188, "13": 201, "14": 214, "15": 229, "16": 243, "17": 258, "18": 274, "19": 291, "20": 310, "21": 326, "22": 342, "23": 362, "24": 378, "25": 395, "26": 412, "27": 427, "28": 437, "29": 451, "30": 466, "31": 483, "32": 497, "33": 521, "34": 537, "35": 554, "36": 574, "37": 585, "38": 601, "39": 620, "40": 637, "41": 656, "42": 672, "43": 688, "44": 702, "45": 718, "46": 734, "47": 752, "48": 766, "49": 784, "50": 799, "51": 819, "52": 833, "53": 849, "54": 870, "55": 883, "56": 896, "57": 910, "58": 930, "59": 944, "60": 960, "61": 979, "62": 1002, "63": 1018, "64": 1035, "65": 1048, "66": 1063, "67": 1076, "68": 1090, "69": 1107, "70": 1124, "71": 1135, "72": 1148, "73": 1165, "74": 1181, "75": 1196, "76": 1211, "77": 1229, "78": 1245, "79": 1260, "80": 1272, "81": 1280, "82": 1291, "83": 1302, "84": 1315, "85": 1329, "86": 1342, "87": 1355, "88": 1366, "89": 1379, "90": 1393, "91": 1405, "92": 1419, "93": 1433, "94": 1447, "95": 1459, "96": 1469, "97": 1480, "98": 1492}
---

**Dave Jones:** Hi, it's random bunker/dumpster item. I found this one in the previous that monster dumpster thing I found offsite. So, I'll link in that video at the end of that below if you haven't seen it. And I have no idea

**Dave Jones:** what this is, but it looked interesting. And of course, I love these thumbwheel switches. They're always fantastic. If you ever see one of those on a bit of kit, make sure you salvage them. They're great for the junk bin for various

**Dave Jones:** projects. And it's got some DIP switches and Zelweger, never heard of them. It's some sort of receiver test unit. So, it's not a receiver. Presumably, it transmits to a receiver and tests out receivers. We've got a power switch, FS

**Dave Jones:** out, full scale out, I guess. Decabit? What the heck is a decabit? And K22? I have no idea. We can set a level trimmer active, transmit. That's a momentary action switch. So, that'll be like a It's like transmits a pulse of various

**Dave Jones:** frequencies. And there's the list of frequencies on the back here. So, anywhere from 167 hertz all the way up to 2 kilohertz. There, you just set the DIP switch. But the back here is really kind of gives the game away, I think

**Dave Jones:** anyway. I'm not sure why it's just got a regular mains power cord. It doesn't have the insulation. So, this is right really old school before the regulations that we had put the insulation on the pins. Anyway, for some reason it goes

**Dave Jones:** through a neutral thing, but I think that's they're just like using that as a like a grommet entry. But I guess they had some other purpose for it at some stage. But anyway, we've got two different fuses on here.

**Dave Jones:** And we've got shrouded 4 mm active and RN, which would be return neutral, I'd be guessing. So, given that this thing transmits like lowish frequency stuff and we've got mains in and it looks like mains out with some fuses, I'd say this

**Dave Jones:** is designed for injecting those control signals onto control frequencies, control signals, control data, whatever it is, onto mains lines which actually controls various appliances and stuff like that. Now, this might be very different in other countries. I've got no idea. Please

**Dave Jones:** leave it in the comments down below for your particular country and what it's like, but here in Australia we have what's called off-peak electricity and which means that particularly for hot water, like the real high energy intensity stuff in everyone's home, if

**Dave Jones:** you've got an electric hot water system, then if you have those coming on during the day, that's when you're paying like peak prices for electricity. So, what they do is they superimpose a signal onto the 50 hertz mains, not that 60

**Dave Jones:** hertz rubbish here in Australia, and then that a signal activates some detection circuitry inside your fuse box which then either turns on or off your hot water system at during like off-peak times, it might be after midnight for example,

**Dave Jones:** when it's really cheap. So, not only does that lower the grid load during peak times, you know, when during the day businesses and everything's going and all that sort of stuff, they've got to like balance the load out. Midnight,

**Dave Jones:** not not not much is happening, so that's when you want to sort of like load up the grid with people's electric hot water during the night time. So, they can control that, they can control other things like street lights and other

**Dave Jones:** mains type infrastructure. And it's not uncommon for these mains control frequencies to actually upset some particular products cuz they've got, you know, little modulated high frequency signals on there and it can cause, you know, things lights to flicker and

**Dave Jones:** other, you know, things to happen um products if they're not well designed and well filtered and stuff like that. Anyway, that is my guess what this thing does. So, we won't turn it on. We'll take it apart and uh see if my suspicion

**Dave Jones:** is correct cuz I think that's I unless it's some sort of like, you know, some other custom industrial thing, I think that's what it's uh going to be doing. I don't know who Anemite is. Anyway, serial number 129. Geez, didn't make

**Dave Jones:** many. Anyway, it's in a classic uh Pac-Tec project case like this. Tons of products are made into Pac-Tec was like a brand back in the uh '70s, '80s uh '80s I think these were uh popular these uh Pac-Tec cases. You can still buy

**Dave Jones:** them. Um so, I just call them that. That's just a generic brand anyway. And I'm undoing a Phillips screw with a flathead screwdriver. Sue me. Anyway, let's crack it open. Is that Come on. And we're in like Flynn. Check it out.

**Dave Jones:** Wow, that's not uh old school through-hole stuff, but um yeah, all right. Let's see what's going on here. Okay, first things first, we've got an EEPROM here. Uh 1991 vintage, so there you go. It's not new. Uh so, oh jeez, that's that's 30 years

**Dave Jones:** old now, almost. Crikey. Uh I'll have a look what all that bundled up cable is later, but let's follow the money here. And okay, so we've got mains input. Let's follow the money. Heh. Heat shrunk. That's going over Ah ah

**Dave Jones:** check it out. That's going over to a uh C&K toggle switch. That's the power switch on the front. C&K toggle switch. Those things are uh 250-V mains rated, but yeah, it's pretty how you doing because if you get solder dags on there, they

**Dave Jones:** can get very close to the metal over here. So, this front panel, I don't think it's earth at all. So, yeah, not the best. Old school bugger safety, bugger clearance. Anyway, so our mains is switching there. It's Oh, okay. Yeah,

**Dave Jones:** it's coming back over here and it's going to the fuse. Okay. So, that is our input mains fuse after the switch and then it buggers off down to the board down here into a mains here. So, that's just a PCB mount 240 V primary

**Dave Jones:** and looks like a couple of windings on the secondary. Maybe two AC low voltage AC secondary windings. But, it also jumps over to here. So, aha, right away, this active output goes directly from the mains active over to

**Dave Jones:** here. So, obviously, if they're injecting anything, it's going to be on the return neutral here and aha, what's this transformer for? So, let's anyway, let's follow the neutral down here. Blue goes down to the board. Just got some mob

**Dave Jones:** protection down in there. Diode bridge. Oh, look, there's a bunch wire. That blue wire That blue wire is coming Oh, that's Is that some sort of Wow. Oh, hang on. Hang on. Oh, there you go. What Why it

**Dave Jones:** has to be that long? Have they got something in that? We'll have a look at that later. Let's follow the neutral. So, neutral goes down to the board. That'll be going over to the transformer over here as well.

**Dave Jones:** The return neutral here doesn't connect over to here. It goes through this other fuse and goes through this transformer here. Aha, so yeah, that would be going I bet you there's a trace going from there. Yeah, I can see it on the board

**Dave Jones:** through the board. Trace from there to there. So, that's our supply transformer for our circuitry and I believe it'll be going over there as well. So, it's going into this transformer. So, this is our signal coupling transformer in the

**Dave Jones:** neutral line, which goes out here. So, that makes sense. So, yep, I was right. It is injecting frequencies onto the mains neutral line. And then, it looks like we just got a couple of switching down in there, do we? For the secondary side of

**Dave Jones:** that injection transformer, we'll call that. And is that not an EEPROM? That might be a That might be a micro, unless that one's a micro, but it doesn't look like it. And nope, that's not a micro. That's a

**Dave Jones:** D71054, and that's a programmable timer chippy type thing. So, that's got to be a micro under there. All right. So, given the vintage, my money is on an EEPROM programmable PIC chip. That's where my money's at. Am I right? Ah, it's upside down. All

**Dave Jones:** the electrons are going to fall out. Ah! No! I was off the off the money. It is a big M, but it's not Microchip. It's a Motorola 60 68705 EEPROM version. Ah, beautiful. None of that E squared prom rubbish. And like I

**Dave Jones:** said, these thumbwheel switches, these are absolutely fantastic things. This one's actually great, cuz it's got a plus minus on there. That's really quite nice. But, these things are absolutely gorgeous. So, this dials in the command. So, obviously, like it's going to

**Dave Jones:** encode like a word, you know, a byte or word or whatever, onto the mains. And you just dial in the frequency. The trimpot here, curiously, goes over to three over there, which So, maybe that's like a you know, LM317 regulator or

**Dave Jones:** something, and it just sets adjusts the level or something like that. I don't know. There's not much else in there. Just a 74HC series logic. So, I'm not even going to bother to take that board out. There's nothing more

**Dave Jones:** interesting to see. What's going to be more interesting is if we actually power this thing up and have a look. And then I might do some Googley searching for this deck of it K22 cuz that's obviously some sort of protocol and Zellweger.

**Dave Jones:** Wonder if they're still around. Now, this is interesting. All this cable here, there's nothing. These two were all wired together. And if I pull that, yep. Just two bare wires in there. So, they weren't they're not electrically connected. What they're doing I think is

**Dave Jones:** using this as a capacitor. It's like a I don't know why it has to be that long. Maybe like they're increasing the capacitance or something. But they're using that as a capacitor. Oh, why you'd have the ends like tinned like that? Because what

**Dave Jones:** it's doing is it's tapping off the bridge rectifier down in there. It's tapping off the negative output of the bridge rectifier. So, it's tapping off that and then it's going into a 74HCT02. I can only presume that that is

**Dave Jones:** something to do with like they're detecting when the mains switches. That's their crude method of doing that. Wow. Pretty how you doing? So, anyway, a HCT02 is a quad NOR gate of course. It's going into it's soldered onto the

**Dave Jones:** pin there, pin three. So, that's one of the inputs of the first gate there. And so, they're yeah, like AC coupling in and the mains I've done that before in my clock mains clock circuit that I built when I

**Dave Jones:** was a teenager. Maybe I have to link in the video. It wasn't quite like that. You do AC couple it, but jeez, you know, wires like it's not like you need some huge voltage isolation or something. Anyway, seems a bit silly buggers, but

**Dave Jones:** that's what they decided to do. What? And I forgot to show you that it did have a neon light. So, is that Yeah, it's actually trust me, it's on. It's just really faint. Anyway, we've got on slash error, so I don't know why the red

**Dave Jones:** thing's flashing, but anyway, it's flashing and we've got it hooked up on our output here. I've got no load connected, so I've got my EEVblog high voltage probe here because it's a proper way to safely measure mains voltage and

**Dave Jones:** other stuff. Anyway, so we are at 704 volts peak-to-peak, 245 volts AC RMS because yes, my mains voltage here in the lab and at home as well is right on the high side of the allowable limit. It's like 246, 247

**Dave Jones:** commonly, so it's getting up there. Even though Australia is supposed to be nominally 230 volts, not 240. Anyway, so we've got a signal there. I've got it set to deck a bit, and I'm going to pulse the transmit, and I don't see anything

**Dave Jones:** pulsing on there. So, maybe I need to set the dip switches. And adjusting the level here gets me zippity doodah. Not sure what the deal is. K22, it's still flashing. I presume it's flashing error. And I've connected this FS output to the scope as

**Dave Jones:** well, and I'm triggering from that. Presumably, it's a 5-volt TTL signal, and I'm still getting still getting nothing. I can't There's just nothing coming out of that. So, there is genuinely an error there. Whoa, hang on. I just played around with the

**Dave Jones:** code here, and it stopped flashing. Look. I was I was going up 969. 169. Wow, okay. 069 will that Aha, got it. Got it. It's a code. Oh, active. There we go. So, here we go. I'll just hit

**Dave Jones:** active. So, it's transmitting and boop foot flash flash flishy flash and then that one's not labeled and the active turns off. So, it transmits for like 5 seconds or something and then switches off. Oh, 69 winner. Okay, so what I'm

**Dave Jones:** going to do is actually uh single shot capture this. There we go. And the it looks like there's no data encoded on that. So, I don't know what that FS output is just like a clock. Nope, silly me. I just wasn't thinking

**Dave Jones:** fourth-dimensionally. Let's do that again. Slower time base and bingo, we of course have a uh there's the data encoded there. So, that is 69 encoded in I presume deca bit. Um critical, I guess. Okay, I'm just going to repeat that same thing. So, that's

**Dave Jones:** 69. I'm going to repeat it with the uh that's positive 69. I'm going to repeat it with 000. So, let's try that again. Single shot capture, trigger.

**Dave Jones:** Yeah, that is different to Yeah, that's different to what we had before. Yep, so it's encoding that on there. Let me do a higher frequency. Actually, this thing's pretty intelligent. Check it out. If you just like randomly flip the

**Dave Jones:** dip switches, it gives you an error. So, it knows that uh you know, you're either not selected a proper frequency or you haven't selected a and or a uh proper command on this. Let's go to 2 kHz. So,

**Dave Jones:** I need 1 3 4 and 6 on. No? 1 3 4 and 6. Um that should be right. Aha, they're actually grayed out. So, I'll go for 1 2 4 and 6. 1 2 4 and 6. There you go.

**Dave Jones:** So, it knows. That's brilliant. So, let's trigger that again, shall we? Single shot capture. Oh, yeah, we've got some higher frequency switching stuff in there. I can see it. But, because this is AC coupled, it's a bit how you doing?

**Dave Jones:** And there you go. That's just a higher frequency clock. Sure enough, if we measure that frequency of channel 2 1.59 kHz. I've got it set to 1,600. Good enough for Australia. Might get more accurate if I go in. But, 1.584.

**Dave Jones:** There you go. So, yeah, that just changes the clock rate. Effectively, it looks like like the data rate like the modulation rate is the same, but the frequency just sets the higher clock rate. That's interesting. And even a sticking a 50-W

**Dave Jones:** load on this thing, unfortunately, um still doesn't do anything. The yellow is the mains waveform there, and you can see that there's no modulation change at the actual point of switching there. So, you know, we can go in there and there's just like

**Dave Jones:** it's just nothing. So, this thing could be faulty, I suspect. Maybe, you know, the switching training or something like that. Switching circuitry could be cactus. So, it is supposed to result in like a, you know, 5-10% ripple on your

**Dave Jones:** mains there, but obviously, nothing's doing there at all. So, it's got to be faulty. Anyway, let's go to the Google is and see if we can investigate this Decabit and K22 stuff. As it turns out, there's a Wikipedia page for this.

**Dave Jones:** Zelweger off-peak system is a brand name for an electric switching device used to control off peak electrical loads such as water heaters and and uh, and and probably uh, you know, street lamps and other uh, type stuff. Uh, carry a

**Dave Jones:** current it's called like ripple uh, injection stuff like that. Goes under various names, but uh, yeah, uh, Zellweger is one of the big players in here and yeah, they talk about uh, things like uh, stereo amplifier stereos can pick up the noise and all that sort

**Dave Jones:** of stuff. Um, uh, ceiling fans can pick up the uh, can pick up the ripple on there. Um, telephone lines and all sorts of stuff. There you go. In some parts of the Sydney, uh, 1,042 hertz signal usually consists of several bursts of a

**Dave Jones:** few seconds off and on for period of up to 50 seconds on coded uh, to affect only selected equipment of course. Um, there you go. Radioactive risk of one type of Zellweger meter. It contains low risk radioactive material. There you go.

**Dave Jones:** Anyway, so that's interesting and there's a uh, thing for bloody Queenslanders up there, some for Sydney, uh, North Coast and stuff like that and it looks like there are different uh, brands and things like that. So, uh, if we go down here, yeah, technology

**Dave Jones:** utilized various hardware telegrams they use K22 decabit LG. Oh, Amemet is um, that company in the land the sticker we had on the back, but of course it's uh, Zellweger and uh, yet the Zellweger standard, but this Zellweger model, maybe they had their

**Dave Jones:** own standard, but uh, they support uh, it looks like decabit. I don't know the history of that. Anyway, these are the different uh, companies Endeavour Energy, Ausgrid and all those sort of uh, Jemena I've heard of. Um, some of

**Dave Jones:** them I haven't heard of, but they um, yeah, they have all these different uh, standards. Decabit um, sounds like one of the major players, but K22's in there too. Then we have this huge document here which I'll link in down below.

**Dave Jones:** Ripple injection load control systems Australian power quality and reliability center, and from the University of Wollongong. It's very comprehensive. So, look, I won't go through the whole thing, whole executive summary and stuff like that. Ripple injection allows access to cheaper off-peak electricity

**Dave Jones:** and all that sort of jazz. Mitigation, there's the ripple injection methods for those playing along at home or into your infrastructure, and it's generally applied at the 11 kV transmission level. Um because there's various step-down voltage phases in the

**Dave Jones:** distribution of electricity, and it's typically done at the 11 kV which will then go through the transformers on the street poles or underground or you know, at ground level that then will transform that down to 240 V which goes

**Dave Jones:** to your home and stuff like that. So, there's little schematics there. There you go, check it out. So, they inject it, yeah, coupling capacitors at the substation bus bar there. And then 11 kV and then it's step down and then it goes

**Dave Jones:** into your Yeah, that's the 240 V house. There you go. So, and here's a photo of a typical injection equipment. I can't see much, but it's got injection capacitors and you know, tuning coils and isolation transformer, compensation caps, absorption coils. Hmm,

**Dave Jones:** interesting. Sure you power efficient autos are getting pretty moist right about now. And here's the K22 protocol coded pulse algorithm. This is from Zellweger as well. So, you know, looks like there they go. They they own the market. There you go, there's the

**Dave Jones:** decabit coded pulse and that's I think what we saw. We just saw like those pulses there on the screen depending on the setting and stuff like that. Unfortunately, we didn't see it rippling on the mains though, unfortunately. So, this is what it's

**Dave Jones:** going to look like here, and I actually saw this the other week. I was doing some mains stuff playing around with it, and I definitely saw that um here in the lab. So, I like hopefully I'll be able to capture

**Dave Jones:** it again. But, obviously that's a time of day thing. I can't even remember when I was testing. It might have been late at night or something like that. So, I might have to I don't know, come in after 10:00 p.m. or something and try

**Dave Jones:** and capture it. But, I did actually see this modulate this ripple modulation um on my mains uh signal on the scope the other day. And of course, I knew exactly what it was um cuz I've seen it many

**Dave Jones:** times before. And yeah, it just pops up occasionally. Um so, if you products aren't So, this is what we would have seen. Uh we would have seen like that it for uh how long's a packet or whatever a

**Dave Jones:** second or whatever. We would have actually seen half a second. We would have actually seen that ripple on there for like half a second then go away. And then that when you have ripple, that's encoded as a one. And the

**Dave Jones:** lack of ripple is encoded as a zero or vice versa, however you want to uh decode it. There you go. Um and that's 750 hertz on a 50 hertz signal. So, that's what it looks like. So, by all means, safely monitor your own

**Dave Jones:** main signal. You can actually do that with a If you want to do it safely So, if you want to do this safely with a crow, yes, crow, um not an oscilloscope rubbish anyway, cuz we're in Australia. It's crow. Give me a break. Anyway, so

**Dave Jones:** if you want to do it safely, um I just use a regular isolation, you know, step down AC step down transformer, 110 or 240 volts down to, you know, 10 volts AC or something like that. And then you can safely probe the with your

**Dave Jones:** regular scope um the, you know, AC signal. And if you sit there long enough and twiddle your thumbs, you'll eventually capture or you might be able to set up a trigger, of course, because uh the levels are reasonably

**Dave Jones:** high. You should be able to set up a trigger unless you get get other glitches on the mains. Maybe you can set up a capture um a peak capture to um get trigger off and single shot capture um some of this uh

**Dave Jones:** mains frequency. So, So, an entire signal injection can run for approximately uh 3 minutes. So, that's actually quite that's quite significant. So, you do stand a good can- chance of a chance of capturing that if you are actually uh

**Dave Jones:** probing the mains and looking for it. Like I said, I just saw I was randomly doing some uh uh unrelated mains testing the other day. I had my high voltage probe hooked up and sure enough, there was the

**Dave Jones:** ripple. So, apparently there is an Australian uh standard for this for those playing along at home, and looks like maybe, you know, 4 to 6% uh modulation value. So, that's uh quite substantial. You should definitely be able to see it. And they tell you that

**Dave Jones:** uh receiving relays, that'd be like in your fuse box to uh decode this, can work down to signals of approximately 2 V, but signal levels due to amplification of up to 30 V have been recorded in the field. Um it's it was only approximately

**Dave Jones:** uh 5 V might be a typical uh injected thing for uh 240 V signal. So, there you go. That's uh fascinating stuff. Shame it didn't work. I could maybe attempt a troubleshoot and repair and see why it's not actually injecting uh this stuff.

**Dave Jones:** It's coming out of the BNC connector, but yeah, maybe one of the switching has gone or uh something like that, perhaps. But, it's fascinating how you can get this ripply stuff on your mains. So, if you ever see something

**Dave Jones:** like that, and it looks a bit how you doing like this, you know what it is. So, let us know in other countries cuz I have no idea if this is uh just you know, an Aussie thing. I believe it's in

**Dave Jones:** New Zealand as well, or whether or not this is a common in your country. Do you get uh this or what do you call it? Is it, you know, off-peak uh ripple? Is it ripple injection? Is it called something

**Dave Jones:** else? And what are the uh typical Who are the players in the market? Cuz Zelweger seem to own the market here by looks of things, and let us know in the comments down below. So, I hope you enjoyed that video. If you did, please

**Dave Jones:** give it a big a thumbs up. And as always, you can discuss it down below and over on the EV blog forum and subscribe over on EVblog.tv if you want decentralized instead of this centralized YouTube rubbish. Catch you next time.
