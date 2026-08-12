---
video_id: piquT76w9TI
title: EEVblog 1489 - Mystery Teardown!
url: https://www.youtube.com/watch?v=piquT76w9TI
source: youtube-asr
timestamps: {"0": 0, "1": 11, "2": 32, "3": 44, "4": 60, "5": 75, "6": 98, "7": 123, "8": 131, "9": 152, "10": 178, "11": 185, "12": 202, "13": 218, "14": 234, "15": 245, "16": 257, "17": 270, "18": 286, "19": 298, "20": 313, "21": 325, "22": 343, "23": 355, "24": 367, "25": 382, "26": 391, "27": 408, "28": 423, "29": 440, "30": 457, "31": 468, "32": 486, "33": 501, "34": 515, "35": 529, "36": 540, "37": 553, "38": 561, "39": 574, "40": 591, "41": 604, "42": 617, "43": 627, "44": 647, "45": 666, "46": 680, "47": 699, "48": 711, "49": 723, "50": 735, "51": 744, "52": 767, "53": 776, "54": 786, "55": 800, "56": 809, "57": 820, "58": 834, "59": 845, "60": 857, "61": 872, "62": 883, "63": 899, "64": 915, "65": 928, "66": 945, "67": 959, "68": 977, "69": 990, "70": 999, "71": 1012, "72": 1025, "73": 1037, "74": 1049, "75": 1064, "76": 1078, "77": 1093, "78": 1111, "79": 1124, "80": 1137, "81": 1157, "82": 1175, "83": 1183, "84": 1200, "85": 1215, "86": 1224, "87": 1241, "88": 1254, "89": 1271, "90": 1278, "91": 1291, "92": 1300, "93": 1312, "94": 1325, "95": 1332, "96": 1349, "97": 1360, "98": 1370, "99": 1384, "100": 1405, "101": 1414, "102": 1426, "103": 1440, "104": 1452}
---

**Dave Jones:** Hi, it's bizarro bit of industry kit teardown time. Up I got this in the mailbag. I I think it was from someone anonymous. Uh thank you very much who sent this in.

**Dave Jones:** And I guarantee you are not going to get this through airport customs. Um there's no chance whatsoever. This is incredible. What is this thing? I didn't tell you in the mailbag episode, but what it is is it's actually something you would totally not think of unless you're in this particular industry.

**Dave Jones:** It's an ultrasonic gas leak detector. It's got four ceramic ultrasonic sensors on top here. It's got a digital readout like this. I don't know you can set it up.

**Dave Jones:** Um somehow I'm not sure what the top interface is. We'll find out shortly. And the reason it's in this sort of like gas cylinder type you know construction like this is because this is explosion proof.

**Dave Jones:** Basically, this is rated to we'll find a standard on here somewhere. Here we go. It's the EXD standard plus of various other things. But this is basically a like explosion fireproof standard.

**Dave Jones:** Basically, means if there's any failure inside this thing, nothing can escape this thing. I mean it'd have to be some massive internal pressure for it to escape cuz this is a gas leak detector that's designed for use in potentially explosive you know industrial factory environments where you got you know pressurized gas pipes running everywhere filled with you know who knows what flammable pressurized material.

**Dave Jones:** And if if you get a leak in any of the pipes, you know you get a burst or a seal leak or something like that, then depending on the pressure differential, the temperature, and the type of gas, and you know size of the hole, and all sorts of things, um it can actually make an ultra-sonic sound and that is what's picked up by these four ceramic ultra-sonic sensors on here.

**Dave Jones:** So, I guess they're in this arrangement to get like a 360° thing. You're supposed to mount this like several meters off the ground like on a pole or something.

**Dave Jones:** That's why it's got like these big mounting posts here and it can be electrically earth of course down to mains earth here. So, you know, there's no sorts of funny business going on and it's just absolutely incredible that you wouldn't think an ultra-sonic sensor would look like this, but you know, sure enough there it is.

**Dave Jones:** So, it's maximum power consumption 160 W will see why hopefully in the teardown. So, this is a type NSM SU343A 30,000 serial number manufactured in 2013. Do not open when there's explosive atmosphere manufactured in the UK by Net Safety and it's the Banshee 343 for those playing along at home.

**Dave Jones:** And do not open when explosive atmosphere is present or when energized. Well, it's not going to be energized. I don't even know where the cable port is on this thing.

**Dave Jones:** Is this like up the top here? But jeez, I tell you what I so want to actually after this teardown I so want to put it back together and actually like design a little board that goes in there to drive this LED display and have a countdown timer on it.

**Dave Jones:** THAT'S LIKE OH MAN, YES, why not? It it's got to be done. So, yeah, who knew that when pipes leak, they can generate not only audible sounds, you know, that hissing sound, but they can generate ultra-sonic sound as well.

**Dave Jones:** And this is designed to measure a 40 m radius and works from 25 and kilohertz to 100 kilohertz and can work up to anywhere from 50 dB to 160 dB pressure levels.

**Dave Jones:** And it's got all sorts of you know, it's got fail-safe sensor systems and also apparently like self-cleaning sensors in there. So, I'm curious and it can actually generate and do self-tests and stuff like a periodic self-test.

**Dave Jones:** So, I believe it has like internal generation or something like that. So, I'm curious to see like what's happening in here. And it also can do like internal heating and stuff like that as well.

**Dave Jones:** So, I possibly expect to see you know, some sort of like you know, heating elements and I don't know. Tear it down. I guess I'll start by taking off this top cover here.

**Dave Jones:** Is this where the interface is because it has both a 4 to 20 milliamp current loop output and also an RS-485 output as well. So, this is going to have some serious O-ring sealing I suspect.

**Dave Jones:** So, Oh, yeah. I can see a gap in there. Yep. Yep. Yep. There we go. And yeah, it's supposed to have an infrared system as well. And I believe I can see an infrared transceiver down there as well.

**Dave Jones:** Think it's designed to like report back to like a central operator or something. So, I don't think there's anything internally like a buzzer or anything that goes off. So, don't Oh, no.

**Dave Jones:** Whoop. Uh Uh Hello. And that's it. What? I don't know. I have no idea what that is. Read the manual, I guess. So, I'll take off one of these ultrasonic sensors here.

**Dave Jones:** But, I'd imagine that you know, with this huge basically pressure vessel kind of thing, um I don't know if like the sensor will be actually have a sealed interface between the sensor itself and inside.

**Dave Jones:** Cuz it kind of seems to to the purpose of this huge thing if you've got this relatively tiny sensor head here, but Yeah, there we go. Yep, that's all.

**Dave Jones:** Wow, yep, that's what you'd expect. Look at that. This is all machine like this is all part of the machine part of this big head here. Oh, then how much are these things?

**Dave Jones:** Anyway, that Um anyway, that's got a connector interface like that. Um is that a like a high pressure connector interface? But there's your there's your sensor. So, it's just a three-pin jobby down in there.

**Dave Jones:** Once again, these are all that just the machining that goes into this, but oh does that come out? Yep, that comes out. So, there's our Oh, there you go.

**Dave Jones:** Each individually tested. That's our ultrasonic ceramic sensor head. Oh, we can take that apart later. It almost looks like inside this that almost looks like it's a port going in there.

**Dave Jones:** And that's yeah, sure enough that's got an O-ring on it. That might maybe part of the pressure self-cleaning system. So, you may have to hook up as a guess I'd say hook up a pressurized gas system.

**Dave Jones:** Ironically, to actually self-test like to actually apply pressure to the sensors to actually test them. Aha, no it turns out these are the actual um AXD rated cable glands that are designed to get the cables in and out to the terminals.

**Dave Jones:** Here's the diagram over here and this has all the terminals in the bottom here. Ah, there you go. So, here we go. Yeah, that's why they've got the cable here cuz this thing can be like hanging from a roof.

**Dave Jones:** There's various I'll put up a photo. There's various ways to like you know, mount this from the wall and um stuff like that. But, look at this. I mean, isn't this just glorious?

**Dave Jones:** And all these massively This whole thing is just, you know, one big machine to part. These gigantic cable glands coming in and out. But, this is what you need um in terms of like cable glands and like interface to go into something that's designed for an explosive containment atmosphere.

**Dave Jones:** I mean, it's just incredible. And yeah, they've they've gunked up that down there. So, yeah, no wuckers on that. So, that's how I guess cables from this board go into the main chamber, is it?

**Dave Jones:** Wow. That's got Grovely Detection Limited. So, I don't know. Is it another company who's involved in the design of this thing? But, yeah, there's your 4 to 20 milliamp current output and the RS485 interface as well.

**Dave Jones:** So, wow. Like, I can just What's going to be in the rest of this thing? Like, just the interface to get into this is incredible. And there you go.

**Dave Jones:** There's the base of that board. Each one of those got a ferrule on there. And it's just it's nice interfaces. A bit of protection stuff on the back. But, yeah.

**Dave Jones:** Geez, that's a just a really nice interface. And that down there is just yeah. They've just sealed that going into the main chamber. They've sealed the thread and also gunked up the entire cable.

**Dave Jones:** But, then you can have pressure, of course, being leaked through the cable, you know, through the gaps in the cable. So, I don't know how they're um taking care of that.

**Dave Jones:** But, um yeah, we'll find out. And of course, this probe thing sticking out here which they got two holes down the bottom there. So, I guess it can I don't know, go into either one.

**Dave Jones:** There's only one option to come through. but this would be the uh ultrasonic transmitter, which is designed to actually um you know, test this sensor because it can go down there and then it can simulate um generating the ultrasonic signal and uh test out each individual sensor periodically.

**Dave Jones:** Yeah, so the reason that they have to go to all this um interface here is because of course one of the uh risks in explosive atmospheres would be a spark due to a loose connection on something like this.

**Dave Jones:** You know, when it can draw significantly significant amount of power uh for example when it's uh doing its ultrasonic uh sensors and cleaning and testing and whatnot um inside as you saw like 60 W or something uh like that power consumption.

**Dave Jones:** So if you've got like a loosey-goosey connection on one of here um you know, and this is just out in the out in the open flapping around in the breeze, then that can cause a spark in the atmosphere.

**Dave Jones:** So they have to have um this interface just for the connections and then another interface inside the main um chassis itself with the other electronics um inside here. So yeah, just the connections need their own uh protective physical protective interface from the atmosphere.

**Dave Jones:** All right, I think I've loosened all those bolts off. Yeah, they can actually pop out. There we go. Six large ass bolts. So let's see. I don't know if I have to take the sensors off first, but let's try and get this Can we get this open?

**Dave Jones:** Wow. This thing is thick as. Let me tell you. It's absolutely incredible. So How much do these things cost brand new? I know that you can buy them. I checked on eBay.

**Dave Jones:** You can buy one for like 300 bucks second hand on eBay. But Woah! At the There we go. We're in. Uh There's a few loosey-goosey washers floating around in there, so I think somebody's had a had a hurry hacker on this.

**Dave Jones:** But, uh yeah, I don't see any other like um any other sealing inside there for the uh penetrator down there. Or I don't see Oh, is it No, no, there's no gunk in on the end of the uh cable.

**Dave Jones:** So, they're obviously allowing for uh the pressure uh to get to be able to like seep through the cable and stuff like that. But, I guess you know the standard um satisfy all that.

**Dave Jones:** I don't know. If you've got experience in those sorts of standards, leave it in the uh comments. But, wow, all the electronics here on this can. And that's interesting.

**Dave Jones:** We've got wires going up to the top here. And this is all gunked all in here. That That's that port that we took off on on the top, which didn't seem to do anything.

**Dave Jones:** But, there is something connected to there. So, there you have it. We've just got like a board on gigantic standoffs that just sits in there. Nothing fancy-pantsy, you know, there's a micro and and a few other um things, you know, they'd be like an ADC and stuff to measure the multi-channel eight four-channel ADC system to measure the ultrasonic uh sensors.

**Dave Jones:** And I don't know how they'd be uh sampling those. But, there's a couple of uh um adjustment. They aren't um trimmer pots. They're actually um like to set a code.

**Dave Jones:** So, I don't know. Does each one have like it, you know, a coded uh type system and address uh system, I guess, um for the, you know, RS 232 RS485 line.

**Dave Jones:** So, there's the entire PCB there. And uh these were the two uh cables coming in. You know, you've got your RS40 485 and you've got your uh connections for your heater and other stuff.

**Dave Jones:** We've got relays. They'd be, you know, uh large issue relays. They'd probably be um switching the heater off and on. Would that be the heater connection over there? I'm not too sure.

**Dave Jones:** Got a couple of ribbon cables going off. We got another thing out here, which is plus minus 20 volts. Is that Oh, no. No, heat heat one. Is that going off to the heater and M1?

**Dave Jones:** I don't know. It's got a couple of you know, buttons for like production testing or whatever and some extra mode jumper switches, something like that. But yeah, not a huge amount doing it.

**Dave Jones:** I really care about the PCB. That's not not the interesting thing here at all. Although I guess people want to know what the micro is. It turns out that's a Xilinx CPLD.

**Dave Jones:** So, wasn't expecting something like that in there. And the only thing that looks like a microcontroller in here that I can find is this thing. Near to impossible to read the number on.

**Dave Jones:** But maybe I can get that. I know it's an NXP jobbie. But I can't read on the camera or the screen. Yeah, sure enough that's an 8051 jobbie. No surprises there really cuz you know, this would have dated back to an old design.

**Dave Jones:** I'm sure many decades old and you know, 8051 is all you need for something like this application. Why it's got you know, a CP a Xilinx CPLD in there.

**Dave Jones:** That's a bit confusing. Got the ULN 2803 relay. That's for driving the relays and stuff. Other miscellaneous stuff for acquisition and whatnot. I couldn't pull a part number off that, but that's obviously doing like the ADC interface.

**Dave Jones:** There's got an LTC. Probably serial converter up there, something like that. And a few other CMOS stuff and Bob's your uncle. What's underneath? Well, first of all, got a heat sink on the bottom there and that's got some don't know if you can see that some bent over TO220s there.

**Dave Jones:** So, that's just doing some regulation and so that they're your voltage regs tied onto there. It's just using that as a small internal heat sink and there you go.

**Dave Jones:** Um They're interesting. They look like little reed relays maybe. Are they Oh, no. They're No, THEY'D BE OPTOCOUPLERS. OH, YEAH. There you go. The component of the week award goes to this what looks like a do-it-yourself opto-isolator.

**Dave Jones:** We've seen this once before. I can't remember what it was in. But obviously, look at the PCB clearance in here. We've got like at least an inch of PCB clearance and surprise there's not a routed slot under there for good measure.

**Dave Jones:** But basically, yeah, infrared LED and infrared photo transistor on this side here and this is the isolated electrically isolated interface going over there. So, and is that one of those DC-to-DC converter isolated converter blocks up there?

**Dave Jones:** Maybe, but look at the Look at the fuse. Oh, my. They've soldered it down to the board. Oh, it's terrible, Muriel. By the way, all of these boards are conformally coated.

**Dave Jones:** You can tell by the sheen on them. So, it's often not easy to read part number through that. But yeah, no surprises for finding conformally coated board. But yeah, that's obviously interface.

**Dave Jones:** These are your four sensors. So, yeah, they're they're just getting that data across the So, they're doing Are they doing the digitization here and then getting it over digitally?

**Dave Jones:** No, well, it turns out these are our 4000 series CMOS. These are 4051 analog muxes and this is a 4093. So, yeah, it's it's all analog on this side.

**Dave Jones:** Aha, it turns out this device down here is an SA614. This is an FM intermediate frequency modulator down here. So, yeah, that's how they're That's how they're doing it.

**Dave Jones:** So, they're just boxing the four channels by the looks of it and they're just going to get in some optical isolation and then you've just got an IF amplifier down here and then this sampling is done on the digital board.

**Dave Jones:** I was just checking that there was nothing else inside that can. Got an insulating sheet. They've got a couple of these insulating things on the on the side of the can there, but no, that's about all she wrote.

**Dave Jones:** So, yeah, right off the bat I'm not seeing this supposed like heater interface thing and the channels, the four channels there that are going down. Sorry, it's I haven't got much light in there.

**Dave Jones:** Put some extra light in there. You can see that they've got this potting compound in here and all of these wires, they're all this is how they of course get the pressure interface going over to the sensor itself.

**Dave Jones:** why they had to use the connector interface cuz they would have used a pressure rated connector as well for that particular interface on over on the sensor here. So, yeah, that would go over to the other side of this connector here and this would be a proper pressure rated connector.

**Dave Jones:** So, yeah, you you know, you take all the issue out by having the the interface there, but there you go. They've got something down here. Got a little tiny board down there.

**Dave Jones:** I think yeah, the ribbon yeah, tiny cable did go off to it. I assume that's like a little temperature sensor maybe down there and it's just attached to the chassis like that, but yeah, there you go.

**Dave Jones:** So, but interestingly, look what's in here or not in here is these threaded things. These go down to those what I thought was like the ultrasonic transducer to generate like the test signal, but these just don't seem to go anywhere.

**Dave Jones:** Um there there's no cables going to them. There's no nothing. So, there's nothing doing there at all. Yeah, so I can only think that uh this is like a option that um is not installed in this model, perhaps, because obviously, you know, there's a there's a purpose for that.

**Dave Jones:** And they do specifically say that this does have um cells cleaning. Yeah, and here's the uh detail on that. It has it says it has a patented fail-safe sonic cow system.

**Dave Jones:** Our fully diagnostic system runs an automated broadband self-test every 15 minutes applying a true pressurized gas leak to confirm each sensor's detection capability and removes any potential external contaminants such as sand, oil, or dust.

**Dave Jones:** And well, sure enough, I mean, you know, to do it at each individual uh sensor, you need an individual um you know, transmitter transducer there to generate the acoustic um the ultrasonic signal that's going to go into the sensor.

**Dave Jones:** So, I Yeah, but there's nothing hooked up to it. It's It's just there's no wiring at all. So, it's just a cylinder. So, yeah, an option not fitted, perhaps.

**Dave Jones:** And the good news, that display board down in there, aha, it's just got a ribbon cable interface. So, yes, I could design a board that just uh connects to the other end of this ribbon, and um I I can get that board out, and then I can uh like reverse engineer that.

**Dave Jones:** Looks like it just has some um you know, serial uh display uh drivers. Um just like the old 4000 series CMOS or something would be my guess. And then uh yeah, I can just drive that display.

**Dave Jones:** That might be a nice little mini project. Um leave it in the comments down below. If I get enough thumbs up on this video, and I'll leave a comment down below if you actually want me to uh do a little mini project, actually designing um a little counter interface for this thing.

**Dave Jones:** In fact, you wouldn't even need a microcontroller. You could just if it's like a serial thing, you could just have a couple of, you know, 74 series counters or something like that.

**Dave Jones:** And uh you know, it it's um and then the infrared um thing to actually reset the thing. And we've got, of course, no shortage of space inside this thing for like, you know, you could have a battery pack that lasted forever.

**Dave Jones:** You could have this digital display you know, work for like a decade or something. And you could have a little remote control system that sort of like resets it.

**Dave Jones:** And that'll be groovy. Yeah, if I get enough thumbs up down below for the comment in this video, I might do that project. And there is inside the uh ultrasonic ceramic sensor.

**Dave Jones:** That's all the details we've got. It's, you know, some proprietary uh sensor thing. They've got like a the green earthing wire going there uh just to make sure that the uh metal work is earthed.

**Dave Jones:** But uh yeah, it's just two pins. I don't know what don't know what that is in there. Is that might have a little bit of Is that gunked up?

**Dave Jones:** Is that Is there some like preamp circuitry under there or something like that? But anyway, anyway, that's just a real high pressure capability uh ceramic ultrasonic sensor. And of course, the uh specialized uh pressurized um pressure rated, I guess, um interface connector down there.

**Dave Jones:** So, that's all she wrote. So, there you have it. I hope you found that as interesting as I did. Cuz when I took this out of the mailbag, I had no idea what this thing was.

**Dave Jones:** Of course, spending a long time in the underwater uh marine industry, I'm used to like uh seeing like pressure vessels uh like this for uh you know, ocean bottom electronics, underwater high pressure um stuff.

**Dave Jones:** But in this particular case, it's not Well, it's basically it is a high pressure um chamber. It's designed to if, you know, if something goes wrong with any of this electronics and I don't know where that heater was.

**Dave Jones:** Um, so I don't know um obviously it's not inside this thing, you know, and so it can take a significant amounts of power and you know, you get a spark from one of the connections or something like that and you've got a pressure leak cuz you have to assume worst case scenario you do actually have a pressure leak and at the same time this electronics has failed um

**Dave Jones:** then you don't want uh you know, the gas igniting or whatever in your factory whole factory goes up. So these are why these are intrinsically safe um and pressure rated to the EXD uh standard.

**Dave Jones:** I won't pretend to know all the ins and outs of that, but uh yeah, it's an international um standard for you know, these sorts of uh contained devices so that they don't ignite flammable atmosphere.

**Dave Jones:** And it's like it just looks like you know, some mine or bomb or something like that. It's just you know, uh demonetized now. You know, as I said yeah, try and get one of these bad boys through airport security.

**Dave Jones:** Please leave it in the comments down below if you actually have tried to take this on your carry-on. Good luck explaining it, especially with a countdown timer. Anyway, if you liked it, give it a big thumbs up.

**Dave Jones:** As always, discuss down below in the comments or over on the EV blog forum. Catch you next time.
