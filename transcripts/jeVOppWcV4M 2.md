---
video_id: jeVOppWcV4M
title: EEVblog #1360 - REPAIR - Aircon Control Panel
url: https://www.youtube.com/watch?v=jeVOppWcV4M
source: youtube-asr
timestamps: {"0": 0, "1": 29, "2": 55, "3": 67, "4": 94, "5": 121, "6": 151, "7": 178, "8": 207, "9": 231, "10": 254, "11": 268, "12": 297, "13": 322, "14": 344, "15": 369, "16": 400, "17": 412, "18": 430, "19": 452, "20": 480, "21": 494, "22": 514, "23": 545, "24": 570, "25": 603, "26": 638, "27": 653, "28": 683, "29": 697, "30": 715, "31": 753, "32": 777, "33": 793, "34": 815, "35": 846, "36": 874, "37": 898, "38": 917, "39": 950, "40": 971, "41": 997, "42": 1025, "43": 1065, "44": 1089, "45": 1117, "46": 1132, "47": 1156, "48": 1189, "49": 1212, "50": 1245, "51": 1276, "52": 1297, "53": 1326, "54": 1361, "55": 1373, "56": 1405, "57": 1432, "58": 1458, "59": 1482, "60": 1504, "61": 1527, "62": 1559, "63": 1579, "64": 1596, "65": 1614, "66": 1643, "67": 1671, "68": 1692, "69": 1733, "70": 1746, "71": 1780, "72": 1811, "73": 1832, "74": 1850, "75": 1869, "76": 1901, "77": 1927, "78": 1939, "79": 1967, "80": 1991, "81": 2020, "82": 2040, "83": 2054}
---

**Dave Jones:** Hi, in a video on my EV blog two channel, which I'll link in just about the background of the bench and everything here, I had a non sequitur about my air con unit on the wall here, and I'm going to have to actually move this cuz now it's actually really difficult to reach over my 900 mm long bench, and it's even further out from the wall. So, like a meter out. I've got to like reach over a meter to turn my air con off and on all the time, but one

**Dave Jones:** of the problems with this damn thing is that I slowly over the last couple of years, like I swear when I moved in like a decade ago, this thing used to work. You press the on off button, it just worked, and that's how it worked in my rented lab. It had the exact same uh controller in it. But, this one is a pain in the ass. It's been pissing me off for a long time, so I'm going to finally uh do something about it. So, let me show you what's actually

**Dave Jones:** happening here. When I press the on off button, it doesn't just turn off or on. Now, the only thing I do here is cool down this lab. I never ever heat it up, but it never gets that cold here in inside.

**Dave Jones:** I'm in the middle of one of these big high-rise uh you know, office uh tower kind of things, and it'll get up to like uh like 25° in here or something. So, I'm always cooling down, but it never drops below like 20 or 20 1 even in the middle of winter. It it stays, you know, so I've never ever in a decade had to use the heating function of this. So, I'm always using the cooling mode. So, all I want to do leave it on low fan speed so that,

**Dave Jones:** you know, you might be able to hear it in the background, but it's really hard. You'd really have to amp it up. Generally, when I shoot videos, I'm turning the air con off just so there's no little air con noise uh bleed, but generally, I just have it continuous low auto mode cool, and that's it. I've got my temperature set to like 21°. I There's got a timer thing. So, it's 22 It thinks it's 22 at the moment, hence why the air con's running, and uh that's

**Dave Jones:** the set temperature. So, I'll leave it set at that, and I just turn it on and off. That's all I want to do. It's not asking much of an air con system, but watch this. It'll probably make a fool of me, but I you can see it's like worn the silk screen's worn off that, but watch this, right? I pressed it. It went into heat mode. What the? This is an on-off button. I swear over the years I've been slowly convincing myself that it's like how hard I press the button, how long I

**Dave Jones:** press it, all sorts of you know my mind's just coming up with lots of weird convoluted explanations for what Oh, there we go. It it turned off. That's what I want it to do, right? But I obviously and I can turn it back on, but there you go. It goes into heat mode, it goes into cool mode, but it's still like continuous. And it it it just doesn't seem like it didn't turn off or on if I hold it down and then release it, it'll turn off, but it's not supposed I don't

**Dave Jones:** believe it's supposed to work like that. So, anyway, somebody in the previous videos um said, "Oh, they're pretty sure that these uh the keypad on this thing with all the buttons works as a like a ladder divider, basically a resistive divider, and that might explain uh you know it could be the contacts could be dodgy, it could be picking up noise from somewhere. Like who knows? You know, there's uh various things that can go wrong with like you know high impedance ladder uh dividers like this. So, I

**Dave Jones:** thought we'd actually you know take it off the wall cuz I want to move the damn thing anyway um and have a teardown and then just uh investigate possible uh fix for this or or if I I might want to put it back and then I could actually design a secondary possibly if I reverse engineer it, design a secondary button which then I could mount uh somewhere else and wire it in parallel. I assume it's like some sort of I assume like there's a might little micro in there

**Dave Jones:** that that communicates via RS485 some differential thing which goes back to the controller. So, I Yeah, I assume that's it. I probably don't want to go to the effort to reverse engineer the RS232 RS485 protocol or whatever it is and do that, but I don't know. Maybe I can like budge in some remote switch somehow or something. Anyway, let's take it off the wall. Do a tear down.

**Dave Jones:** I can't bloody well turn it off. Oh, I did did. I swear. I pressed it like five times before and it didn't turn Oh, duh. All right. So, it's probably got some bracket thing and it's probably painted onto the wall.

**Dave Jones:** When I had this place painted and painted when I rented it out, so usually you got to break the seal around the paint job. Now, it's not going to come off without a fight. I'll get back to you. Doll, totally forgot to show Yeah, it does have a brand on it. It's an Easem brand, but I believe the air con I've got like isn't Actron, but Doll, it turns out that's a Leasem. That's an L with like air coming out of it. Get it?

**Dave Jones:** Leasem. Anyway, Australian thing and yeah, I found a manual for it. So, yeah, but that doesn't help me get the damn thing off the wall. I was able to get the There's a bottom like stick on decal thing which hides the zone buttons there. I don't have multiple zones, but I still cannot get this damn thing off the wall. I know there's clips and there seems to be clips on the bottom, but Hang on. I think I got the bastard. Heard a crack.

**Dave Jones:** As I don't know if that was an injury from it or not, but it's off. Bloody clips on the bottom. OEM Electronics Proprietary Limited, Sydney, Australia. You can see all the hacks I had at it. And that's like That's crude as. Anyway, decent amount of cable. Ta-da! So, I'll disconnect that and bring it down to the bench.

**Dave Jones:** First of all, I'd better document what's connected to where cuz all but the black one is damn white. So, yeah, I'll put some markers on those. First of all, let's measure the voltage on this thing. Oh, one-handed technique, 17 and 1/2 volts. Wow, that's That is surprising. All right, so here it is, the least some controls. That's I guess the part number, is it?

**Dave Jones:** Interesting to find DIP switch controls on here. This is interesting. Like integral SNS, which would be sensor one here, which was actually connected. So, I do actually There is a sensor elsewhere in the room, but I've never actually checked at all if that actually works or whether or not it uses the internal sensor in here. I don't know. It regulates the temperature fairly well within plus minus half a degree, by the way. I've done temperature logging plots of this thing, and it gives, you know, a

**Dave Jones:** sawtooth plus minus, you know, like half a degree. I think we want no zones, so I don't know why zones are set. I'm pretty sure I've only got the one zone here. But anyway, it is set to remote sense.

**Dave Jones:** So, I don't know why the sense one line is connected. That's interesting. I'd probably rather have the integral sensor. I might experiment with that. Heat pump or cool elec. I don't know what that is, but yeah, we basically want cool elec.

**Dave Jones:** What is it Does this thing even heat up at all? I I don't know. Continuous fan or auto continuous fan. Definitely don't want continuous fan, so that's right. Three-speed fan. It does have It does seem to have three speeds cuz it goes through it on the display, and it does seem to move a larger volume of air with the different speed. So, there you go.

**Dave Jones:** Anyway, yeah, as I said, I was wrong about the um differential pair RS485. We've got common power, which, as you saw, 17 and 1/2 volts. So, there's probably just like a a 12-V linear reg on here or something, and then there'll be a 5-V linear reg for the micro cuz, you know, these things don't take much power. So, you don't need any of that switchy regulator rubbish. And the aux line is obviously what's sending the back so, or is it a just a resistor ladder line from the

**Dave Jones:** power as the YouTube commenters suggested. But anyway, I've got some cutouts in here for these electrolytic caps and a big whopping power resistor up there. That's because, well, they could just couldn't fit in cuz part of the case, yeah, it's curved down there.

**Dave Jones:** So, I had to, you know, I had to get the nice curvy look. They've had to cut away the PCB and then yeah, none of that surface mount rubbish. So, it's, you know, it's clearly an old design, you know, probably dates from like the '80s or something. Anyway, let's get this PCB out. It just seems to Oh, I don't know, there's two screws there. All right, there we go. Got it. That's rather neat.

**Dave Jones:** I like that. Exposed pad fingers there. They've got the solder coat finish. Let's flip it over and they've just got the nuts. Oh, I got to keep those square. Oh, no, they'd actually That's what the molding's for. It's pretty much what I expected. A micro, a few miscellaneous bits and bobs, and it's looks like that a rechargeable battery down there cuz you wouldn't have a fixed lithium in something like this, would you? I don't know, it could last forever. Anyway, that's for the real-time clock cuz this thing does have

**Dave Jones:** a timer. And you can see right up there. Geez, that's a weird layout, isn't it? I mean, you know, you've got your real-time clock chip. There's your 32.768 kHz crystal, and and your battery's all the way down there. So, yeah, that wasn't good planning on your PCB layout point of view. There you go, that's a bit of a surprise. We've got ourselves an ST micro in here. You know, I would have maybe expected an old-school PIC or, you know, like a Motorola part or something like that.

**Dave Jones:** But an ST 72C334 part of that series. So, here's the data sheet for that, but yeah, it's just a general purpose 8-bit micro designed for So, yeah, that's well and truly obsolete. You can't really get that from any mainstream suppliers now. You'd have to beg, borrow, steal one of those from the gray market if you wanted to replace them. So, you know, they probably bought up all the stock they could. You know, you buy like 10,000 of them, that'll do you for the next 20 years or whatever.

**Dave Jones:** But yeah, anyway, and it's just an 8-bit micro and looks like we have some We've got some LED drivers here. What are they? Oh, they're ULN2003 transistor arrays. Old school. So, you no doubt saw on the video you probably would have seen the multiplexing of the LEDs. So, they're doing all of the visual like the indicator LEDs plus the seven-segment displays are all part of the same big-ass matrix there. Switches. This micro like this is obviously a switch array. So, it's all going into the micro. Well, I don't I don't actually

**Dave Jones:** until I trace it out. I don't know for sure, but I might trace out the sense line down to branches off there. Thank you very much. But it goes down here. It goes down here. Aha, sense. There you go. That's the That's a thermistor.

**Dave Jones:** There's your temperature sensor. So, yeah, I like I suspect that the micro on here is not doing anything. It's just an interface to you know, switches and the LED display and everything to tell the aircon controller which will be up in my roof here. That'll be the Actron Airtron aircon controller. Yeah, so it might say oh, remote sense. But the remote sense might actually be on here. So, I don't think that the micro is actually sensing the temperature. Well, no, it does branch off, doesn't it? Maybe it does

**Dave Jones:** God, it goes under a switch there. Those two chippies down in there which it seems to go down to. That one looks like it's a little ST op-amp and this one is a you classic 393 in dual comparator.

**Dave Jones:** So, yeah, it looks like maybe it does go down to there somewhere. So, maybe and as I suspected that's a linear 5-V regulator but that's what the resistors there for. It's just a dropper. It's just a dropper. That's it from the 17.5 V rail.

**Dave Jones:** Old school. Now, that's switching rubbish. And what's that? Is it another 5-V reg? One for digital, one for the analog matrix, maybe? Anyway, first thing is the switches. I thought like that might might have been like a rubber membrane type thing, but it's not. That's a genuine tactile. So, really I wouldn't expect that to wear out. It's not like this has had like a million operations or anything. I do have a genuine fault in that like an intermittent contact in that tactile switch. Be I was hoping that it would be

**Dave Jones:** that and that it would you know, I might be able to like re-silver the bottom of the contacts or something like that on the rubber baby buggy bumper membrane, but no. It's a that's a real tactile switch. It still seems to have its tactile feel. So, I I'll measure that though. I will actually get the meter on there and make sure it just goes zero and it's not just dodgy ohms.

**Dave Jones:** Okay, we've got 14.2 K there. That does indicate that uh it could be the resistor ladder, but let's just Oh. Oh, I'm pressing that. Oh, yeah yeah, it's a bit a switch. Yeah, that's that's dodgy brothers. 3 ohms, 1 ohm.

**Dave Jones:** Oh, when I move I'm rotating that, pivoting that side to side. Oh, yeah, that switch is dodgy. IT'S DODGY AS. WOW, A tactile switch 96 ohms, 75 ohms for A TACTILE SWITCH. AH, WHO WOULD HAVE THOUGHT? THERE you go. That's a repair right there.

**Dave Jones:** We don't want a chicken dinner, I think. That's like a joystick. We've invented a joystick. Um yeah, the world's yeah, the Clayton's joystick. Wow. That right there is complete dodgy brothers. So, yeah, I'm not sure I have or maybe I might have to look through my old boards. This is why you keep like scrap boards and stuff. Maybe I I might find something similar cuz the shaft length is going to matter because it's got to come through the button like this and then it's got to

**Dave Jones:** push onto that. So, it's not like I have a stock of tactile buttons. Have to look through old projects and stuff like that. Hmm, and therein lies the uh the the dilemma. Do you store your parts based on project, which I do a lot of the time? Well, I've probably got half half. Half my stuff uh you know, switches like this. I would a project box containing just parts for a specific project that I was working on, you know, cuz if you want to pick up the project

**Dave Jones:** again, then all the parts are there, all your stuff, all your boards, all your development, whatever for it is all there in in that one box ready to go, ready to get back into it. If you don't ever want to work on those projects anymore, you can say, well, it's you're better off putting those into like a generic component bin labeled SMD switches. But, you know, how often do I need a to get an SMD switch?

**Dave Jones:** Not very often. All right, so what I've done now is hooked up the probes to the common terminal and ground. It's supposed to go to There you go. Let's try another button. 13.1 13.3 13.6 You're seeing a pattern? Nine like eight.

**Dave Jones:** Uh the these contacts are dodgy down here, by the way. Get the idea that yeah, this seems to be YouTube commentator was right that this is some sort of divider array, but he mentioned voltages go down to zero. But pressing these buttons does affect the AUX line. So that's in the So it shows that that AUX line is not like, you know, some sort of digital output coming from the micro or anything like that. It It's analoggy to do with the buttons, which is really interesting. Unfortunately,

**Dave Jones:** here's where Murphy gets you every time. You try and trace this out. This comes across to this via here, goes down, drops under there, which then goes under a damn switch. So doesn't go there. I guess I can trace that that resistor there with the AUX line. Yeah, I was right. There you go.

**Dave Jones:** This is how we start tracing this out, but I I'm not going to do a full reverse engineer of this. Jeez. It does seem that's connected through a 10k resistor. Well, there's two 10k resistors here, but I believe they go over to Yeah, this pin the micro over here. So the AUX line is Is that like I don't think that's a pull-up. No, the other side of that is not a pull-up. I'm just using a bypass.

**Dave Jones:** That'd almost certainly be the bypass cap for the chip down there. So it's not not pulling up to the micro rail. So Yeah, there you go. So they got that pin through a 10k to the AUX over here. But where else is it going? Hmm. Okay, I did find out that one of these 10ks does go down to ground here. So the AUX line is actually 10k to ground and you can I can show you that over here. There you go.

**Dave Jones:** 10k to ground and then the other side of that um well, exactly well, Here you go. It's exactly that 14.2, which is varied by the buttons there. So that's the 5 V rail. That's between aux and 5 V rail there. So it does have a built-in ADC. So yeah, I guess that I presume that they're not doing a switching matrix here, but they're yeah, reading the analog voltage from there and that would make sense if this is giving you a dicky contact, then you would expect that you know that

**Dave Jones:** the voltage would be all over the up and all over the place and it could be sensing incorrect things. And that's what I'm actually experiencing. I've been experiencing over the years is this thing just you know, just mucking around not being consistent at all. And of course if this was just your regular switch matrix, then the really the dicky contact on this wouldn't really matter because it would be you know, it doesn't matter whether it's couple of hundred ohms or zero or one ohm, five ohms,

**Dave Jones:** whatever it is. It doesn't really matter. It should It should either register or not on your key matrix. So yeah, obviously they're doing this as like an analog sense thing. So I don't think that the analog sense is going directly to the aux. Let's say it's going into the micro. Anyway, I think what we need to do is hook this thing back up and actually put a scope on the aux pin and see what's happening. Now before you go probing anything like this, you don't want to assume that the

**Dave Jones:** ground wire on there, that black one is mains earth referenced. If you do and it's not, then you can come a gutser because I've done a video how to not to blow up your oscilloscope about ground earth referencing and stuff like that.

**Dave Jones:** So before you do that, you can either just use your We'll talk about this in a minute. High voltage differential probe like this, which it makes it safe or you can actually check it. So I'm just going to check that now to see what's what. So I'm just going to I know this is mains earth referenced down here and that's the measurement thing we're using or Or could use like your portable scope or whatever, but anyway, let's let's have a squeeze. Put your tongue at the right

**Dave Jones:** angle. Yep, that's mains earth reference. So, no, it's got zero. Why has it got absolute zero? It's kind of a little bit interesting that it had absolute zero there. So, I'm going to see if I can measure any voltage on that. No, there's no AC voltage. That is genuinely connected. Yep, there we go. And I double-checked that with my BM235, and sure enough, yep, it's zero point Yeah, this one has an extra digit. This is the new BM786. Hopefully it'll be available very shortly. 0.04, but maybe there's

**Dave Jones:** like a little bit of residual voltage on there due to like the ground going from the air con unit through to the scope here, and that's maybe just causing it to offset a little bit. That's sort of to be expected when you start introducing even very minute voltages into a pretty precision measurement thing like the ohms range on a multimeter screen.

**Dave Jones:** So, we could hook our scope probe straight up. Oh, that's a bit of a bummer, cuz I wanted to use the new Mix Egg and DP10007. And this is a new model, which they designed at my request, cuz I wanted a times 10 times 100 one. They've got others in this DP10000 series that have a different divider ratios, but I wanted one to match my HVP70 probe. A potentially lower cost option for that. I've got to fully test this one, but everyone says, you know, it's a

**Dave Jones:** pretty decent performer, and it's lower cost than the HVP70. So, I might eventually carry this on the EV blog store. That's the plan. But yeah, they specifically made this to my request, like took them like six or nine months, and they eventually said, "Yep, we can do a times 10 times 100 design." So, you should see the specs of this match almost precisely the HVP70, except it's uh it's a little bit wider bandwidth but otherwise very similar specs all round. Anyway, I'm probing the aux line there and uh huh if we single

**Dave Jones:** shot capture that, look at that. So, that's you know, it's got some ripply doodar on there and periodically is that going to be a 50 hertz thing? Oh no, 515 hertz. There you go. That's interesting like it's doing some sort of periodic scanning or something like that perhaps.

**Dave Jones:** I can't get a consistent trigger on that so uh huh at a long ah it's packet based. There you go. It's packet based. Trap for young when basically if you see an otherwise periodic you know, if you zoomed in like this if you see like what what you think you know, you do single shot capture like that and this looks periodic. If you zoom out like this this is just a how to use a scope thing and it appears periodic like that but you've got your trigger level set to where you

**Dave Jones:** think it should trigger from and if you actually put your scope into run mode and it doesn't trigger like that at the trigger level you thought it does either above or below like that then obviously it's got it's not completely periodic so then you know to zoom out and uh huh of course it's a packet based thing at there you go 2.7 odd hertz something like that. And there's a too is a packet on there whether or not it's like an actual packet whether it's supposed to do that

**Dave Jones:** or whether or not that's just I don't know it's a noise pick up on the line. I like have no idea the air con's not actually working at the moment so anyway, let me switch it on and see if you can see a difference.

**Dave Jones:** Okay, here we go big power button. Oh. Do you see anything in that? Let me press it again. It's gone oh that's not analog level. It's So, yeah, it it seems to be doing some packety-based thing there. I like I don't You know, it's kind of not what you expect, is it? I don't know. If anyone's got any details about this, you know, if you're into this air-con uh control air-con market air-con controllers and stuff like that. So, the YouTube commenter uh asked Steven G, um

**Dave Jones:** I'm not sure where he's getting his voltages uh from, but yeah, here's his uh post where he says, "Yeah, like the voltages uh when you press the buttons." And that uh makes sense from a point of view of that uh it was possibly confusing my on-off button cuz it's down it's supposed to be like 0 V, but where's he actually measuring that from? I don't know. I'd have to do more. It's It's certainly not on the AUX line, that's for sure, because this is the AUX line here. So,

**Dave Jones:** yeah, mhm. But, it does make sense in that uh it could be confusing the on-off button with a because it's, you know, saw the dodgy resistance there, um it causing a problem, a conflict with the next one up the threshold level, which was the uh heat cool thing. So, that's why it was sort of like jumping into heat or cool mode randomly when I tried to turn it off or on. So, that makes sense. Okay, so the way we can trigger on this is our pattern looks like every

**Dave Jones:** uh 500 ms. So, I'm going to change my told off time here to uh oh, it's all over the shop. Oh, jeez, that's a that's jumping around. Oh. Anyway, let's set it to like, you know, I don't know, 400 ms or something like that. There you go. We should be able to trigger off that fairly reliably. Where's my trigger point? Yep.

**Dave Jones:** There you go. So, I'm sure I've done videos on this. So, what happens is after the trigger, it waits another 400 ms before it arms the triggering system again, so that Yeah, it'll arm within that dead period. It'll uh re-arm about there, something like that. And then it'll capture the next packet. So, that's how we can reliably trigger on that. So, there you go.

**Dave Jones:** Okay. Now, watch that. I am going to turn the on-off button. Oh. Oh, has that changed? Oh, wait. Hello. Press it again. No, so it's changing my It's certainly changing. You can see. Is it back on? Oh god, I can't see it cuz it's back to front panel's back to front. Ah. Okay, that's all that's all aircon on. That's aircon completely off.

**Dave Jones:** So, that's completely off. So, I've got all pulses there. So, aircon and now it's on auto cooling. So, what I'm going to guess here is that maybe it It just continuously sends out the last button that was pressed, perhaps. And then the different combinations are what you see here. I I don't know. Leave it in the comments down below if you've got a better idea of what's going on here, but that that seems to be the case cuz this is just repeating, repeating. I'm not touching

**Dave Jones:** these buttons. This is just like this code just changes and stays changed every time you press a button. So, let me go off again. And hopefully we'll get all of them back again. Okay, yep. It's off and yep, we get all of them back. So, that seems consistent.

**Dave Jones:** So, I think we're onto something there. So, it seems to be just transmitting, yeah, over and over again the last key that was pressed. And then the controller that it's going to, the aircon controller, knows, well, you know, I'm not going to do that again because you've already pressed that button. But ah, okay.

**Dave Jones:** Right. No, so the micro, right? Because the on-off button is the same for both on and off. So, it needs to know that you've pressed it again. So, when you turn it on, it switches to another mode. So, it's not outputting what key, it's outputting the last key and mode.

**Dave Jones:** Something like that. It's a bit how you're doing. It's not what I was expecting. So, doesn't look like it'd be something easy to sort of like build another controller to do it. You'd have to spend a bit of time reverse engineering this and figure it all out. It's It's certainly not that voltage level system that Steven on the comments was alluding to, but that that might be like internal. But, that certainly pointed to the switch. So, yeah, that switch array they are probably are using like an ADC

**Dave Jones:** internal to the micro to detect the switch and that's we're just getting that dodgy switch. So, anyway, I think that's enough [ __ ] around with the waveforms there. I think I'll just go in there and see if I can find a replacement switch and then just get this back up and running at the very least. And if we power it from an external lab supply here, it does actually well, it powers up, but it just ends up flashing, does a little power on cycle and then flashes zone one here.

**Dave Jones:** So, and of course the the power button does absolutely nothing as you'd expect because it's got nothing to do with the power of this unit. It's designed to talk with the with the main controller. So, unfortunately, I've I've probed the aux line here and we just get no volts. So, it's not doing anything.

**Dave Jones:** Yeah, it's doing Okay, so after it's power on sequence, it Yeah, it's but it's well, no, it's periodically doing something, is it? I need to trigger off that. No, I can't trigger off anything there really on the positive side or on the lower side either. So, getting diddly squat. So, it's not It's not doing anything. Yeah, is that can signal being actually provided by must be provided by the controller, I would assume. And then the LM 339 that we saw on here, the dual comparator, that's exactly what you'd need to decode

**Dave Jones:** this. So, you just decode it at you know, two different threshold levels, and turn it into a digital signal, which this thing which the micro can then decode very easily. So, yeah, it looks like this thing is just a passive slave.

**Dave Jones:** It doesn't do anything without the signal being generated by the master controller. So, it seems to just sit at mid-rail there as you saw, and then just pulses up and down. So, yeah, it doesn't do us anything. Completely forgot. Oh, well, not completely because I did eventually remember that I do actually unlabeled I really have to label I do have a thing full of switches. But, unfortunately, these are No, hang on.

**Dave Jones:** Maybe maybe I can find one. Oh, that's a bit shorty. Oh, that's super long shaft. Look at that. Oh, that one might do it. I can always cut the shaft to length, and yeah, might be through-hole, but I can fix that. There you go, successfully chopped off and converted to surface mount. No wackers, I'll trim those leads. They're a bit long, but yeah, just trim the leads and we're good to go. There you go, like a bought one from brown to black. No worries. And it's got a nice snappy feel to it. Okay,

**Dave Jones:** let's just re-verify that dodgy brothers resistance there. Need the old third hand. Oh, yeah, 100 190 ohms 170 ohms. Wow. Can I get it right down? I'm pushing really hard ON THAT. THREE OHMS two ohms. Yeah. Dodgy. Now, let's put in our new switch.

**Dave Jones:** 14.2 K. Press it, and zero. Thank you very much. I don't think we're going to have any more issues. That looks pretty darn repeatable to me. And give it a little wiggle wiggle wiggle yeah down the bottom. No, it's all good. All right, let's see if this sucker works.

**Dave Jones:** Here we go. One push. Oh, nice clicky. Nice clicky. AND OH, BEAUTIFUL. FIRST GO. Got to do it a couple of times. Where are my poor egg on? Oh, it's flashing run. I don't know why it flashes run.

**Dave Jones:** But yeah. Yep. Fixed. And there we go. Auto heat cool. Yep. Winner winner chicken dinner. That is fixed. So, it was the like a switch. I thought maybe it might be like a membrane type thing. Turned out to be a tactile switch. Usually it's pretty rare that those tactile switches uh fail like that. Have seen it before, but it's not something It's not my initial conclusion that I'd jump to for something like this. And as I said, if this was arranged this was designed as a switch

**Dave Jones:** matrix in the micro as you'd normally do it, you know, you'd have a bunch of digital lines for the common done bunch of digital lines for the rows and then you multiplex them and you scan continuously scan the keyboard. It it really it doesn't matter whether or not that switch is a couple hundred ohms. It would still work and it wouldn't confuse it with other buttons on there, but that's not how they implement that. So, they've implemented obviously using some sort of resistor divider thing. I don't

**Dave Jones:** know. We could like reverse engineer this. If anyone actually does have a reverse engineered or a schematic for this thing, please leave it in the comments down below. But yeah, obviously it is what Steven said in the comments.

**Dave Jones:** They're obviously trying to do some sort of resistor dividery type keypad arrangement. I you know, I'm trying to read that values. That's a dicky design decision that can come back to bite me. Basically, it's been bugging me for years. I can't believe I put up with it. Um, think I did actually try to take the thing off the wall before and I just couldn't get the damn thing off. So, I go, "Ah, bugger it, you know?" And so, I finally It took a lot of effort to get that off

**Dave Jones:** the wall, but yeah, it was like somehow painted on. It's been on there for like 15 years. It's never been taken off ever since uh this building was built probably, you know, 17, 18 years or something like that. And yeah, that switch finally come a guts uh and was causing it to like put it into heating and cooling mode and doing all sorts of these weird modes. Like you'd come up with all these convoluted theories. Oh, like if I hold it on for a bit longer,

**Dave Jones:** if I press it twice in a row quickly, it'll do this and that. But, no, it was just There was no method. And sometimes you might think, "Oh, it might repeat it a couple of times." So, you might think you found something and something else is playing up with it. No, it was just a dodgy switch contact with a a dodgy-ass implementation of a keypad matrix uh you know, or a keypad um input design, sensor design, and that was just causing different modes. That's it. That was a

**Dave Jones:** real interesting repair. So, I'm going to call that a repair video. Actually, it was going to be like a maybe a reverse engineering video. But anyway, if you've got details about that command system, yeah, please leave it in the comments down below. You got any other info, please let me know. Anyway, hope you found that interesting. If you did, please give it a big well, a thumb.

**Dave Jones:** There it is. Foreground thumb cuz I'm zoomed in a lot. Give it a big a thumbs up. And as always, you can discuss in the comments down below, EV blog forum, alternative platforms, all that sort of stuff. You know the drill. Ring the subscribe bell and all that YouTuber stuff we say.

**Dave Jones:** Hope you liked it. Catch you next time. Mhm.
