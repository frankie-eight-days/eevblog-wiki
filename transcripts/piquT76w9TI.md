---
video_id: piquT76w9TI
title: EEVblog 1489 - Mystery Teardown!
url: https://www.youtube.com/watch?v=piquT76w9TI
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 35, "3": 51, "4": 69, "5": 87, "6": 104, "7": 116, "8": 131, "9": 144, "10": 165, "11": 182, "12": 195, "13": 208, "14": 223, "15": 241, "16": 254, "17": 270, "18": 286, "19": 300, "20": 319, "21": 334, "22": 352, "23": 370, "24": 386, "25": 404, "26": 419, "27": 440, "28": 457, "29": 471, "30": 486, "31": 504, "32": 523, "33": 540, "34": 555, "35": 569, "36": 582, "37": 595, "38": 610, "39": 622, "40": 636, "41": 656, "42": 673, "43": 691, "44": 707, "45": 721, "46": 735, "47": 749, "48": 763, "49": 779, "50": 793, "51": 805, "52": 818, "53": 836, "54": 849, "55": 865, "56": 880, "57": 896, "58": 914, "59": 928, "60": 948, "61": 962, "62": 982, "63": 997, "64": 1014, "65": 1033, "66": 1047, "67": 1061, "68": 1078, "69": 1093, "70": 1109, "71": 1124, "72": 1139, "73": 1160, "74": 1175, "75": 1187, "76": 1204, "77": 1222, "78": 1236, "79": 1249, "80": 1263, "81": 1274, "82": 1286, "83": 1300, "84": 1315, "85": 1329, "86": 1341, "87": 1356, "88": 1369, "89": 1382, "90": 1394, "91": 1408, "92": 1420, "93": 1437, "94": 1450}
---

**Dave Jones:** Hi, it's bizarro bit of industry kit teardown time. Up I got this in the mailbag. I I think it was from someone anonymous. Uh thank you very much who sent this in. And I guarantee you are not going to get this through airport

**Dave Jones:** customs. Um there's no chance whatsoever. This is incredible. What is this thing? I didn't tell you in the mailbag episode, but what it is is it's actually something you would totally not think of unless you're in this particular industry. It's an ultrasonic

**Dave Jones:** gas leak detector. It's got four ceramic ultrasonic sensors on top here. It's got a digital readout like this. I don't know you can set it up. Um somehow I'm not sure what the top interface is. We'll find out shortly. And the reason

**Dave Jones:** it's in this sort of like gas cylinder type you know construction like this is because this is explosion proof. Basically, this is rated to we'll find a standard on here somewhere. Here we go. It's the EXD standard plus of

**Dave Jones:** various other things. But this is basically a like explosion fireproof standard. Basically, means if there's any failure inside this thing, nothing can escape this thing. I mean it'd have to be some massive internal pressure for it to escape cuz this is a gas leak detector

**Dave Jones:** that's designed for use in potentially explosive you know industrial factory environments where you got you know pressurized gas pipes running everywhere filled with you know who knows what flammable pressurized material. And if if you get a leak in any of the pipes,

**Dave Jones:** you know you get a burst or a seal leak or something like that, then depending on the pressure differential, the temperature, and the type of gas, and you know size of the hole, and all sorts of things, um it can actually make an

**Dave Jones:** ultra-sonic sound and that is what's picked up by these four ceramic ultra-sonic sensors on here. So, I guess they're in this arrangement to get like a 360° thing. You're supposed to mount this like several meters off the ground

**Dave Jones:** like on a pole or something. That's why it's got like these big mounting posts here and it can be electrically earth of course down to mains earth here. So, you know, there's no sorts of funny business going on and

**Dave Jones:** it's just absolutely incredible that you wouldn't think an ultra-sonic sensor would look like this, but you know, sure enough there it is. So, it's maximum power consumption 160 W will see why hopefully in the teardown. So, this is a type NSM SU343A

**Dave Jones:** 30,000 serial number manufactured in 2013. Do not open when there's explosive atmosphere manufactured in the UK by Net Safety and it's the Banshee 343 for those playing along at home. And do not open when explosive atmosphere is present or when

**Dave Jones:** energized. Well, it's not going to be energized. I don't even know where the cable port is on this thing. Is this like up the top here? But jeez, I tell you what I so want to actually after this teardown I so want

**Dave Jones:** to put it back together and actually like design a little board that goes in there to drive this LED display and have a countdown timer on it. THAT'S LIKE OH MAN, YES, why not? It it's got to be

**Dave Jones:** done. So, yeah, who knew that when pipes leak, they can generate not only audible sounds, you know, that hissing sound, but they can generate ultra-sonic sound as well. And this is designed to measure a 40 m radius and

**Dave Jones:** works from 25 and kilohertz to 100 kilohertz and can work up to anywhere from 50 dB to 160 dB pressure levels. And it's got all sorts of you know, it's got fail-safe sensor systems and also apparently like self-cleaning sensors in

**Dave Jones:** there. So, I'm curious and it can actually generate and do self-tests and stuff like a periodic self-test. So, I believe it has like internal generation or something like that. So, I'm curious to see like what's happening in here.

**Dave Jones:** And it also can do like internal heating and stuff like that as well. So, I possibly expect to see you know, some sort of like you know, heating elements and I don't know. Tear it down. I guess I'll start by

**Dave Jones:** taking off this top cover here. Is this where the interface is because it has both a 4 to 20 milliamp current loop output and also an RS-485 output as well. So, this is going to have some serious O-ring

**Dave Jones:** sealing I suspect. So, Oh, yeah. I can see a gap in there. Yep. Yep. Yep. There we go. And yeah, it's supposed to have an infrared system as well. And I believe I can see an infrared transceiver down there as well. Think

**Dave Jones:** it's designed to like report back to like a central operator or something. So, I don't think there's anything internally like a buzzer or anything that goes off. So, don't Oh, no. Whoop. Uh Uh Hello. And that's it. What?

**Dave Jones:** I don't know. I have no idea what that is. Read the manual, I guess. So, I'll take off one of these ultrasonic sensors here. But, I'd imagine that you know, with this huge basically pressure vessel kind of thing, um

**Dave Jones:** I don't know if like the sensor will be actually have a sealed interface between the sensor itself and inside. Cuz it kind of seems to to the purpose of this huge thing if you've got this relatively tiny sensor head here, but

**Dave Jones:** Yeah, there we go. Yep, that's all. Wow, yep, that's what you'd expect. Look at that. This is all machine like this is all part of the machine part of this big head here. Oh, then how much are these things? Anyway,

**Dave Jones:** that Um anyway, that's got a connector interface like that. Um is that a like a high pressure connector interface? But there's your there's your sensor. So, it's just a three-pin jobby down in there. Once again, these are all that just the

**Dave Jones:** machining that goes into this, but oh does that come out? Yep, that comes out. So, there's our Oh, there you go. Each individually tested. That's our ultrasonic ceramic sensor head. Oh, we can take that apart later. It almost looks like

**Dave Jones:** inside this that almost looks like it's a port going in there. And that's yeah, sure enough that's got an O-ring on it. That might maybe part of the pressure self-cleaning system. So, you may have to hook up as a guess I'd say hook up a

**Dave Jones:** pressurized gas system. Ironically, to actually self-test like to actually apply pressure to the sensors to actually test them. Aha, no it turns out these are the actual um AXD rated cable glands that are designed to get the cables in and

**Dave Jones:** out to the terminals. Here's the diagram over here and this has all the terminals in the bottom here. Ah, there you go. So, here we go. Yeah, that's why they've got the cable here cuz this thing can be like hanging from

**Dave Jones:** a roof. There's various I'll put up a photo. There's various ways to like you know, mount this from the wall and um stuff like that. But, look at this. I mean, isn't this just glorious? And all these massively This whole thing

**Dave Jones:** is just, you know, one big machine to part. These gigantic cable glands coming in and out. But, this is what you need um in terms of like cable glands and like interface to go into something that's designed for an explosive

**Dave Jones:** containment atmosphere. I mean, it's just incredible. And yeah, they've they've gunked up that down there. So, yeah, no wuckers on that. So, that's how I guess cables from this board go into the main chamber, is it? Wow. That's got Grovely Detection

**Dave Jones:** Limited. So, I don't know. Is it another company who's involved in the design of this thing? But, yeah, there's your 4 to 20 milliamp current output and the RS485 interface as well. So, wow. Like, I can just What's going to be in the rest of this

**Dave Jones:** thing? Like, just the interface to get into this is incredible. And there you go. There's the base of that board. Each one of those got a ferrule on there. And it's just it's nice interfaces. A bit of protection stuff on the back. But, yeah.

**Dave Jones:** Geez, that's a just a really nice interface. And that down there is just yeah. They've just sealed that going into the main chamber. They've sealed the thread and also gunked up the entire cable. But, then you can have

**Dave Jones:** pressure, of course, being leaked through the cable, you know, through the gaps in the cable. So, I don't know how they're um taking care of that. But, um yeah, we'll find out. And of course, this probe thing sticking out here which

**Dave Jones:** they got two holes down the bottom there. So, I guess it can I don't know, go into either one. There's only one option to come through. but this would be the uh ultrasonic transmitter, which is designed to actually um you know,

**Dave Jones:** test this sensor because it can go down there and then it can simulate um generating the ultrasonic signal and uh test out each individual sensor periodically. Yeah, so the reason that they have to go to all this um interface

**Dave Jones:** here is because of course one of the uh risks in explosive atmospheres would be a spark due to a loose connection on something like this. You know, when it can draw significantly significant amount of power uh for example when it's uh

**Dave Jones:** doing its ultrasonic uh sensors and cleaning and testing and whatnot um inside as you saw like 60 W or something uh like that power consumption. So if you've got like a loosey-goosey connection on one of here um you know,

**Dave Jones:** and this is just out in the out in the open flapping around in the breeze, then that can cause a spark in the atmosphere. So they have to have um this interface just for the connections and then another interface inside the main

**Dave Jones:** um chassis itself with the other electronics um inside here. So yeah, just the connections need their own uh protective physical protective interface from the atmosphere. All right, I think I've loosened all those bolts off. Yeah, they can actually pop out. There we go. Six large

**Dave Jones:** ass bolts. So let's see. I don't know if I have to take the sensors off first, but let's try and get this Can we get this open? Wow. This thing is thick as. Let me tell you. It's absolutely incredible.

**Dave Jones:** So How much do these things cost brand new? I know that you can buy them. I checked on eBay. You can buy one for like 300 bucks second hand on eBay. But Woah! At the There we go. We're in. Uh

**Dave Jones:** There's a few loosey-goosey washers floating around in there, so I think somebody's had a had a hurry hacker on this. But, uh yeah, I don't see any other like um any other sealing inside there for the uh penetrator down there.

**Dave Jones:** Or I don't see Oh, is it No, no, there's no gunk in on the end of the uh cable. So, they're obviously allowing for uh the pressure uh to get to be able to like seep through the cable and stuff like that.

**Dave Jones:** But, I guess you know the standard um satisfy all that. I don't know. If you've got experience in those sorts of standards, leave it in the uh comments. But, wow, all the electronics here on this can. And that's interesting.

**Dave Jones:** We've got wires going up to the top here. And this is all gunked all in here. That That's that port that we took off on on the top, which didn't seem to do anything. But, there is something connected to there. So, there

**Dave Jones:** you have it. We've just got like a board on gigantic standoffs that just sits in there. Nothing fancy-pantsy, you know, there's a micro and and a few other um things, you know, they'd be like an ADC and stuff to

**Dave Jones:** measure the multi-channel eight four-channel ADC system to measure the ultrasonic uh sensors. And I don't know how they'd be uh sampling those. But, there's a couple of uh um adjustment. They aren't um trimmer pots. They're actually um like to set a code. So, I

**Dave Jones:** don't know. Does each one have like it, you know, a coded uh type system and address uh system, I guess, um for the, you know, RS 232 RS485 line. So, there's the entire PCB there. And uh these were

**Dave Jones:** the two uh cables coming in. You know, you've got your RS40 485 and you've got your uh connections for your heater and other stuff. We've got relays. They'd be, you know, uh large issue relays. They'd probably be um switching the

**Dave Jones:** heater off and on. Would that be the heater connection over there? I'm not too sure. Got a couple of ribbon cables going off. We got another thing out here, which is plus minus 20 volts. Is that Oh, no. No, heat heat one. Is that

**Dave Jones:** going off to the heater and M1? I don't know. It's got a couple of you know, buttons for like production testing or whatever and some extra mode jumper switches, something like that. But yeah, not a huge amount doing it. I really care about the PCB.

**Dave Jones:** That's not not the interesting thing here at all. Although I guess people want to know what the micro is. It turns out that's a Xilinx CPLD. So, wasn't expecting something like that in there. And the only thing that looks

**Dave Jones:** like a microcontroller in here that I can find is this thing. Near to impossible to read the number on. But maybe I can get that. I know it's an NXP jobbie. But I can't read on the camera or the

**Dave Jones:** screen. Yeah, sure enough that's an 8051 jobbie. No surprises there really cuz you know, this would have dated back to an old design. I'm sure many decades old and you know, 8051 is all you need for something like this application. Why

**Dave Jones:** it's got you know, a CP a Xilinx CPLD in there. That's a bit confusing. Got the ULN 2803 relay. That's for driving the relays and stuff. Other miscellaneous stuff for acquisition and whatnot. I couldn't pull a part number off that, but that's

**Dave Jones:** obviously doing like the ADC interface. There's got an LTC. Probably serial converter up there, something like that. And a few other CMOS stuff and Bob's your uncle. What's underneath? Well, first of all, got a heat sink on the bottom there and that's

**Dave Jones:** got some don't know if you can see that some bent over TO220s there. So, that's just doing some regulation and so that they're your voltage regs tied onto there. It's just using that as a small internal heat sink and there you go.

**Dave Jones:** Um They're interesting. They look like little reed relays maybe. Are they Oh, no. They're No, THEY'D BE OPTOCOUPLERS. OH, YEAH. There you go. The component of the week award goes to this what looks like a do-it-yourself opto-isolator. We've seen this once

**Dave Jones:** before. I can't remember what it was in. But obviously, look at the PCB clearance in here. We've got like at least an inch of PCB clearance and surprise there's not a routed slot under there for good measure. But basically, yeah, infrared

**Dave Jones:** LED and infrared photo transistor on this side here and this is the isolated electrically isolated interface going over there. So, and is that one of those DC-to-DC converter isolated converter blocks up there? Maybe, but look at the Look at the fuse. Oh, my. They've

**Dave Jones:** soldered it down to the board. Oh, it's terrible, Muriel. By the way, all of these boards are conformally coated. You can tell by the sheen on them. So, it's often not easy to read part number through that. But yeah, no surprises for

**Dave Jones:** finding conformally coated board. But yeah, that's obviously interface. These are your four sensors. So, yeah, they're they're just getting that data across the So, they're doing Are they doing the digitization here and then getting it over digitally? No, well, it turns out these

**Dave Jones:** are our 4000 series CMOS. These are 4051 analog muxes and this is a 4093. So, yeah, it's it's all analog on this side. Aha, it turns out this device down here is an SA614. This is an FM intermediate frequency

**Dave Jones:** modulator down here. So, yeah, that's how they're That's how they're doing it. So, they're just boxing the four channels by the looks of it and they're just going to get in some optical isolation and then you've just got an IF

**Dave Jones:** amplifier down here and then this sampling is done on the digital board. I was just checking that there was nothing else inside that can. Got an insulating sheet. They've got a couple of these insulating things on the on the side of

**Dave Jones:** the can there, but no, that's about all she wrote. So, yeah, right off the bat I'm not seeing this supposed like heater interface thing and the channels, the four channels there that are going down. Sorry, it's I haven't

**Dave Jones:** got much light in there. Put some extra light in there. You can see that they've got this potting compound in here and all of these wires, they're all this is how they of course get the pressure interface going over to the

**Dave Jones:** sensor itself. why they had to use the connector interface cuz they would have used a pressure rated connector as well for that particular interface on over on the sensor here. So, yeah, that would go over to the other side of this

**Dave Jones:** connector here and this would be a proper pressure rated connector. So, yeah, you you know, you take all the issue out by having the the interface there, but there you go. They've got something down here. Got a little tiny board down

**Dave Jones:** there. I think yeah, the ribbon yeah, tiny cable did go off to it. I assume that's like a little temperature sensor maybe down there and it's just attached to the chassis like that, but yeah, there you go. So, but

**Dave Jones:** interestingly, look what's in here or not in here is these threaded things. These go down to those what I thought was like the ultrasonic transducer to generate like the test signal, but these just don't seem to go anywhere. Um there there's no cables

**Dave Jones:** going to them. There's no nothing. So, there's nothing doing there at all. Yeah, so I can only think that uh this is like a option that um is not installed in this model, perhaps, because obviously, you know, there's a

**Dave Jones:** there's a purpose for that. And they do specifically say that this does have um cells cleaning. Yeah, and here's the uh detail on that. It has it says it has a patented fail-safe sonic cow system. Our fully diagnostic system runs an

**Dave Jones:** automated broadband self-test every 15 minutes applying a true pressurized gas leak to confirm each sensor's detection capability and removes any potential external contaminants such as sand, oil, or dust. And well, sure enough, I mean, you know, to do it at each individual uh

**Dave Jones:** sensor, you need an individual um you know, transmitter transducer there to generate the acoustic um the ultrasonic signal that's going to go into the sensor. So, I Yeah, but there's nothing hooked up to it. It's It's just there's no wiring at all. So,

**Dave Jones:** it's just a cylinder. So, yeah, an option not fitted, perhaps. And the good news, that display board down in there, aha, it's just got a ribbon cable interface. So, yes, I could design a board that just uh connects to the other

**Dave Jones:** end of this ribbon, and um I I can get that board out, and then I can uh like reverse engineer that. Looks like it just has some um you know, serial uh display uh drivers. Um just like the old

**Dave Jones:** 4000 series CMOS or something would be my guess. And then uh yeah, I can just drive that display. That might be a nice little mini project. Um leave it in the comments down below. If I get enough thumbs up on this video,

**Dave Jones:** and I'll leave a comment down below if you actually want me to uh do a little mini project, actually designing um a little counter interface for this thing. In fact, you wouldn't even need a microcontroller. You could just if it's

**Dave Jones:** like a serial thing, you could just have a couple of, you know, 74 series counters or something like that. And uh you know, it it's um and then the infrared um thing to actually reset the thing. And we've got, of course, no

**Dave Jones:** shortage of space inside this thing for like, you know, you could have a battery pack that lasted forever. You could have this digital display you know, work for like a decade or something. And you could have a little remote control

**Dave Jones:** system that sort of like resets it. And that'll be groovy. Yeah, if I get enough thumbs up down below for the comment in this video, I might do that project. And there is inside the uh ultrasonic ceramic sensor. That's all the details

**Dave Jones:** we've got. It's, you know, some proprietary uh sensor thing. They've got like a the green earthing wire going there uh just to make sure that the uh metal work is earthed. But uh yeah, it's just two pins. I don't know what

**Dave Jones:** don't know what that is in there. Is that might have a little bit of Is that gunked up? Is that Is there some like preamp circuitry under there or something like that? But anyway, anyway, that's just a real high pressure

**Dave Jones:** capability uh ceramic ultrasonic sensor. And of course, the uh specialized uh pressurized um pressure rated, I guess, um interface connector down there. So, that's all she wrote. So, there you have it. I hope you found that as interesting

**Dave Jones:** as I did. Cuz when I took this out of the mailbag, I had no idea what this thing was. Of course, spending a long time in the underwater uh marine industry, I'm used to like uh seeing like pressure vessels uh like this for

**Dave Jones:** uh you know, ocean bottom electronics, underwater high pressure um stuff. But in this particular case, it's not Well, it's basically it is a high pressure um chamber. It's designed to if, you know, if something goes wrong with any of this

**Dave Jones:** electronics and I don't know where that heater was. Um, so I don't know um obviously it's not inside this thing, you know, and so it can take a significant amounts of power and you know, you get a spark from one of the

**Dave Jones:** connections or something like that and you've got a pressure leak cuz you have to assume worst case scenario you do actually have a pressure leak and at the same time this electronics has failed um then you don't want uh you know, the gas

**Dave Jones:** igniting or whatever in your factory whole factory goes up. So these are why these are intrinsically safe um and pressure rated to the EXD uh standard. I won't pretend to know all the ins and outs of that, but uh yeah, it's an

**Dave Jones:** international um standard for you know, these sorts of uh contained devices so that they don't ignite flammable atmosphere. And it's like it just looks like you know, some mine or bomb or something like that. It's just you know, uh demonetized now.

**Dave Jones:** You know, as I said yeah, try and get one of these bad boys through airport security. Please leave it in the comments down below if you actually have tried to take this on your carry-on. Good luck explaining it, especially with a

**Dave Jones:** countdown timer. Anyway, if you liked it, give it a big thumbs up. As always, discuss down below in the comments or over on the EV blog forum. Catch you next time.
