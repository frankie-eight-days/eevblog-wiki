---
video_id: Xfs0dglIVOM
title: EEVblog 1681 - Mailbag: Nice DIY CC Load,  Amazing Proto Boards, Ian Johnston
url: https://www.youtube.com/watch?v=Xfs0dglIVOM
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 26, "3": 43, "4": 57, "5": 74, "6": 86, "7": 99, "8": 113, "9": 129, "10": 149, "11": 162, "12": 173, "13": 188, "14": 206, "15": 218, "16": 230, "17": 243, "18": 254, "19": 271, "20": 287, "21": 300, "22": 311, "23": 326, "24": 342, "25": 356, "26": 370, "27": 390, "28": 404, "29": 421, "30": 436, "31": 450, "32": 467, "33": 480, "34": 495, "35": 512, "36": 525, "37": 539, "38": 552, "39": 571, "40": 591, "41": 610, "42": 623, "43": 635, "44": 645, "45": 660, "46": 677, "47": 690, "48": 703, "49": 718, "50": 733, "51": 747, "52": 759, "53": 771, "54": 788, "55": 802, "56": 817, "57": 828, "58": 840, "59": 852, "60": 866, "61": 876, "62": 892, "63": 903, "64": 921, "65": 932, "66": 945, "67": 957, "68": 969, "69": 980, "70": 989, "71": 1001, "72": 1014, "73": 1027, "74": 1043, "75": 1054, "76": 1066, "77": 1077, "78": 1088, "79": 1098, "80": 1110, "81": 1123, "82": 1134, "83": 1147, "84": 1159, "85": 1170, "86": 1184, "87": 1195, "88": 1208, "89": 1222, "90": 1238, "91": 1253, "92": 1269, "93": 1289, "94": 1303, "95": 1309, "96": 1325, "97": 1335, "98": 1349, "99": 1362, "100": 1378, "101": 1397, "102": 1410, "103": 1423, "104": 1438, "105": 1450, "106": 1463, "107": 1480, "108": 1499, "109": 1518, "110": 1530, "111": 1543, "112": 1556, "113": 1580, "114": 1599, "115": 1618, "116": 1635}
---

**Dave Jones:** Hi, welcome to everyone's favorite segment, mailbag. It's been a while and we're going to do it old school behind the camera here. Yes, we've got the trusty knife. Look at that bad boy. Um thank you very much to Daniel Nagy from

**Dave Jones:** Budapest in Hungary. Hi to all my Hungarian viewers. Do I get many from Hungary, do we? Um so if you want to send something into the mailbag, send it to Pierre mailbag. Got to put mailbag on it, otherwise I don't know and I like I

**Dave Jones:** think I've just ordered something. So mailbag, PO Box 7949, Parklea, New South Wales. Should be Northwest actually. They renamed the bloody thing. Northwest, New South Wales, 2153, Australia, not Austria. Let's go. Yeah, that is in the middle. And

**Dave Jones:** what do we have? Ta-da, a note. We'll need to read the note second cuz I like to be surprised. Uh we have 9-V 9-V Is that a 9-V battery? I assume we've got something that needs a 9-V battery and is very

**Dave Jones:** handily provided a 9-V battery for it. Uh bonus bubble wrap. Ooh, it looks like the Star Wars crawl. Look at that. Cool. And what do we got? Woah, this looks cool. We've got What's in here? Is that like a postcard

**Dave Jones:** or Uh yeah, it's a yep, it's a photo. It's a photo. Let's have a look before we look at the item. I assume that is Daniel's bench. There you go. Rate his bench. Nice and clean and simple. I like

**Dave Jones:** it. It's a lot bigger than I've had in some places, let me tell you. Um Yeah, terrific. We have a schematic. Look at this. Uh the Miquel CC2 electronic load. Aha, I guess that's what we've got here. We've

**Dave Jones:** got AN ELECTRONIC LOAD. AND of course I've done my There's been tons of people who've done a version of my very crude, simple electronic load over the years. So looks like we've got an LM4040 there. Um couple of

**Dave Jones:** LMC4682 there. Um that's a dual jobby and there's some IFR 1405 transistors there. He's put those in parallel there. They've got the same They've got exactly the same drive on each one by the looks of it. They've all

**Dave Jones:** got their own individual current sharing resistor there. And oh, we've got old school analog meter up here. Brilliant. And our power circuit, this is a classic reverse polarity protection circuit here. We've got the P channel MOSFET here, a VP 3203. I don't know that off

**Dave Jones:** the top of my head, so I don't know the aspects of that. Maybe I'll put up a data sheet here, but anyway, we've got a 12 V Zener diode here and a 10 K from gate to ground here. And basically, and this is

**Dave Jones:** designed to prevent hooking up the battery the wrong way. It's idiot-proof. So, if you put it back I won't go through the whole theory, but you put it up and put it back put the battery backwards, the P channel MOSFET doesn't

**Dave Jones:** turn on and your circuit is protected. But you if you put it the right way, you'll have a high enough gate source voltage here, which will switch the MOSFET on, no problems whatsoever. The thing I don't understand is though you

**Dave Jones:** don't actually need the Zener diode and the resistor here. The Zener diode here is only designed to prevent like if you had a higher voltage here in your battery than what the maximum VGS voltage of the MOSFET is. So, this one like you

**Dave Jones:** you've only got 9 V. So, having a 12 V Zener diode here, I I don't think that's doing anything. And you technically you don't need the resistor. So, if your battery voltage is less than the rating of the max rating of the MOSFET, then

**Dave Jones:** you can just put the gate straight down to ground and Bob's your uncle. And we're just driving a red power LED. Don't know why you had to put it across Vref there to turn on the transistor. It seems

**Dave Jones:** wouldn't you die whack it across the rail but maybe wanted to detect if the V ref has failed perhaps anyway and probably don't need your decoupling cap so you can do a bit of months in here you can months the

**Dave Jones:** circuit pretty sure you can get rid of that you can get rid of that you can get rid of that you can get rid of that and more better anyway let's have a look at the unit let's have a look at this thing

**Dave Jones:** liking the look of this already looks like a Bobby Dazzler and look at that that's a beautiful case I love those slope front instrument cases and an old school analog meter isn't that beautiful Daniel actually says in his note that

**Dave Jones:** this is an off-the-shelf case but he's got handmade cutouts and laser engraving on there and that's just beautiful thing of beauty a joy forever look at that that is gorgeous a lot of pride has gone into that good nice 10

**Dave Jones:** turn party no wackers um it's it's almost a shame that we've only got the of course I like the analog meter but you know of course you can put a meter in series and actually get the exact current if you're that desperate but

**Dave Jones:** often you know like oh yeah near enough just put your it's not mirrored so you can't you know it's hard to avoid parallax error there so you know if we if we look at it like that okay it might

**Dave Jones:** read zero there but look at an angle it's not zero anymore that's parallax error but yeah that is just wonderful what a huge amount of pride has gone into that I like the flush 9 volt battery connector external

**Dave Jones:** DC too beautiful and this slide out battery holders are neat too it's just got a spring here to put tension on that and look you can't really well you sort of can put it in backwards but different size things there help prevent that so

**Dave Jones:** that's just fantastic look at look at that hook it up to the power supply here. I got 10 volts and let's set it to 500 milliamps there. Oh, look at that. I got to get the tongue at the right angle.

**Dave Jones:** Oh, come on. Oh, the pot just doesn't have the resolution. Come on. Oh, that's going to have to be good enough for Australia. Look at that. That's pretty bang on. Bobby dazzler. So, that'll go up to a maximum of 2

**Dave Jones:** amps, will it? Well, it can go Yeah, 2.08 for there. 2 amps. Oh, it's a little bit over. The the meter there is not quite It's a little bit out at full scale. Look at that. Oh, smidge out. But, you know, analog meter

**Dave Jones:** for the win, right? Yeah. That's neat. I like it. That is beautiful. I like the effort, the pride and effort that's gone into that. Daniel, you can be very proud of that. So, give Daniel a rating out of

**Dave Jones:** 10 below for his uh little analog meter constant current electronic load. That's just fantastic. The CC2. I wonder what happened to the CC1? Or is that CC2 cuz it's 2 amps? I think it might be. That's terrific. Well done, Daniel. Oh, I

**Dave Jones:** ALMOST FORGOT THE TEARDOWN. OH, LOOK AT THAT. Isn't that it That is just as gorgeous as the like the the box that it's in. There you go. Got some uh seal pads there. We've got our dual transistor. Not sure why he went with

**Dave Jones:** dual. I'm not going to go through the thermal calcs and everything else. And well, good thing about duals you've got a bit of redundancy there, too. You know, if you blow your then Yeah, no worries. Um fused, beautiful,

**Dave Jones:** socketed op amp there. Fantastic. Little trimmer in there. Is that full scale adjust there? And yeah. Look Look this. Beautiful. He's even put the heat shrink over these. Oh, look at Look at the all the heat shrink. A lot of pride's gone

**Dave Jones:** into that. Well done. I'm not sure if Daniel sells this. He doesn't have a website. Doesn't Actually, I don't think he sells it. But, that is gorgeous. He can be proud of that. Once again, rate it out of 10 down below. I was just

**Dave Jones:** thinking that you don't see many of these cases anymore, these sloping instrument cases with like the folded metal and stuff like that. You don't see them much anymore. Um these are traditionally used, like you'll find them in university

**Dave Jones:** engineering school labs and stuff like that, you know, because you know, they've built their own custom gear and exactly like this, actually. Um and yeah, these were common like folded sheet metal cases where, you know, they're kind of like the standard back

**Dave Jones:** in the back in the old days and when I was a boy. Yeah, you know, you would have like your folded metal chassis, but this is a gorgeous one with powder coating and everything else. And yeah, but like

**Dave Jones:** Yeah, it brings a tear to the eye. Next up, we've got one from the old Dart. Hello to all my viewers in the old Dart. Thank you very much, Kaylesh Haran. I think I've got that right. Now, I butchered that one, surely. It has

**Dave Jones:** been violated by DHL, by the looks of it. Look at that. It's been violated, security checked. So, I don't know. Did it get randomly x-rayed and it just showed up? So, So, if we just break their tape, that

**Dave Jones:** should get us in, should it not? No. Rather unpleasant. Should have just sliced the entire box. We have a note to me. It's come to the right place. Oh, something What's in here? OH. OH, LOOK. PROTOBOARDS. YOU KNOW WE LOVE

**Dave Jones:** PROTOBOARDS. Stamp basic. Oh, yes. I was clued up on these. These are really cool. These look quite clever. So, what else have we got in here? Components and assembled boards. Fragile. Fragile. Really? Fragile They got like little pins on them or something?

**Dave Jones:** Ooh, look at this. Demo. Okay, we have a working demo here. So, we'll power that up in a sec. And we've got ATtiny85 ATtiny85 and a whole bunch of pre-done boards. Yeah, these are very cool. Let's check them out. So, this is

**Dave Jones:** actually a Kickstarter and I wasn't able to find the Kickstarter, so I just emailed Klesh then to see if I can get the link. But anyway, these are designed to replace breadboards, you know, cuz you just got wires going all the usual

**Dave Jones:** problems with breadboards, right? And the whole idea is that this is called the stamp, so you got three types, the basic, the regular, and the pro here. And they're designed to have like interconnects on the bottom here. And

**Dave Jones:** I'll have to go through the manual for it cuz the manual is actually quite good. But if we have a look at our board here, we you can see that we can like solder SMD parts on here. We can like

**Dave Jones:** free solder to pads over here. We've got another like SMD over here with like variable width. These are some leads soldered up and we've got a battery. And then on the back, depending on the type you get, they'll have different

**Dave Jones:** configuration options here where you can actually just like solder bridge over like, you know, cuz here is the unsoldered one, you know, just the blank one. And you can actually solder like route pins in various configurations, route them you know, ground and positive

**Dave Jones:** and to you know, various things. So, very cool. So, you can effectively like sort of program these like, you know, wire up your breadboard so to speak with just like little individual jumpers and stuff like that. And it can get quite

**Dave Jones:** complex the actual configurations that you can actually get on this thing. So, yeah, the best thing to do is just have a look at their manual, and they explain that quite nicely. And here's our nice little demo here with our little micro.

**Dave Jones:** We've got a just a button here, and we can see we can change that. Nice. So, we've got like these They're those neo neo pixely things, are they? I assume that they are. And Oop. There we go. Look at that.

**Dave Jones:** Oh, it's pretty. Isn't that great? So, there you go. And that's all done with basically, you know, no dodgy jumper links or anything like that. It's all just like programmed, and you can solder You know, see you've got

**Dave Jones:** some dropper resistors on the bottom there, and you can just Yeah, solder all these things, and that's it. That's a great little demo. Just by it like bridging various links and stuff, you can configure your circuit. They're very

**Dave Jones:** handy to have in your junk bin. Let me tell you like I've got like trays full of like these little adapter boards and stuff, and they come in so handy. And these are more than just like little breakout adapter boards. These are like,

**Dave Jones:** you know, you can actually easily configure circuits without having to dick around stripping your little You know, fiddly piss ant wires on there and try to You know, like wire the damn thing up and stuff. So, yeah, you can

**Dave Jones:** just put little solder blobs and the castellated edges. And these edges here, they're what's called castellated edges, and they allow you to like just join the boards together, solder them together in an array like that. So, that That is just a fantastic

**Dave Jones:** idea. So, unfortunately, I can't find the Kickstarter at the moment, but I will endeavor to link that in if Kailash gets back to me. So, that is great. I reckon that is terrific. Thumbs up, linked down below. And for example, this

**Dave Jones:** one here is got a little ATtiny 85 on it. You see how you can solder little itty-bitty parts on the top there and also on the bottom. Look at that. That's great. So, let's have a quick look at

**Dave Jones:** the manual here cuz this is the best way to get an idea of exactly the versatility in this thing. So, you can see, you know, all the problems with breadboards and and there's lots of like, you know, you like bad con- you

**Dave Jones:** get bad springs, bad contacts, dirty contacts. If you pull your radial resistors out of the bandolier tape, you know, they can have glue on the end and then you stick them in and the glue just acts as an insulator in your breadboards

**Dave Jones:** and man, you can really come a guts with breadboards, but they're still great cuz I'm old school, you know, but anyway, if you don't like breadboards, here you go. This is how you can like simplify a 555 timer into just this. Like, you know,

**Dave Jones:** there's no flying leads anywhere like this. Look, they've got an Arduino, a buck converter, switch, LED, stepper driver, all that can be reduced to an individual thing like this. So, you can see that the we've got the, you know, front side and the back

**Dave Jones:** side, but I'll show you the routing stuff here. So, you can get different types. You can get the basic, regular, pro and then you can get the pitch. So, they've got all these. You can order it like based on this part number by the

**Dave Jones:** looks of it. Very cool. So, you can get, you know, SOICs, SOPs, SOTs, VSSOPs, SMDs, QFNs and, you know, all and then junction boards and through-hole boards and so, you've got your castellated edges here. It looks like these are actually pulled back. I

**Dave Jones:** didn't look I I was actually going to um say that yeah, when you butt them up together, the pins would short, but no, it looks like they've thought about that. It looks like they've routed the bit extra. I've got to look under THE

**Dave Jones:** MICROSCOPE. OH, YEAH, I CAN see it. JUST WHOA, THEY NEED TO STICK OUT A FRACTION MORE, MAYBE. Uh oh, jeez, but yeah, that's the idea. Is that yeah, you butt these two boards up and in theory, they shouldn't um out

**Dave Jones:** together. So, you've got to actually solder either solder bridge them across or as you'll see later, you've got other options. So, yeah, um that's that's very cool. Yeah, but you've got to you got to control your manufacturing process. You

**Dave Jones:** got to watch your PCB manufacturer gets that right. Um that that's actually back like that. So, yeah, there's a bit of art in making sure your manufacturer doesn't uh screw that up on you uh when you actually um yeah, route these things

**Dave Jones:** out. So, um anyway, yeah, so you got pin pads, power pads, power routing traces, floating pads, edge pads, and all sorts of stuff. And uh then you got the through-hole board, and then you got the junction board. So, you can order these

**Dave Jones:** all these different types of boards. And wait until you see the flexibility here. So, here it is, right? So, you can route say like whoop. Say So, you've got this this blue one over here can go over to

**Dave Jones:** these pads here, and then the blue can connect to any one of these pins here, and then you should be able to bridge blue to brown here, for example. So, you bridge those, and then you can go So,

**Dave Jones:** you can get this purple one up here to any of these pins over here. So, you've got all this like route and same for like the you know, the red in this corner or the green in this corner or

**Dave Jones:** the brown up in that corner. You can route them in theory to any one of these pins. So, you can use those for power routing for example. And then you can solder bypass capacitors directly on there to go between power rails and

**Dave Jones:** things like that. So, yeah, I did like yeah, I you'll have to read the read the manual in-depth for yourself. But look, they've got a like a 20-pin job here, and they've got a similar sort of flexible arrangement going on here. And

**Dave Jones:** then this is an example of an LM 5164 buck converter here. So, you can put this entire buck converter There it is. Entire buck converter on the on the board like that. Isn't that neat? So, there you go. So, so you can see the

**Dave Jones:** solder bridges in there that they've just bridged those over. And it's just terrific flexibility. An entire buck converter Um, that one little board with no jumper links whatsoever. Yeah, so you can butt them up on on the side like this, so you can,

**Dave Jones:** you know, butt the different types. Um, you know, so this one has like a 5 V linear regulator thing, and then it's got like an ATtiny. And as we mentioned, they've got these purpose-built uh, castellated holes. So, castellated

**Dave Jones:** edges, castellated uh, holes, that's the that's the terminology for when you uh, basically uh, how you put the how you design those on a PCB is you just put a just a normal pad. There's nothing special. There's no such thing as a

**Dave Jones:** castellated hole like component kind of thing. Well, you could technically. Well, that's what they've designed here. So, it's a little bit more complicated than that. But if you want to do a basic castellated edge, um, this one's a bit

**Dave Jones:** more advanced, then you just put a hole right on the edge of your PCB and just tell them to route across. So, they actually build it as a regular plated through hole, except at the end of the manufacturing process, the routing bit

**Dave Jones:** comes along and just shaves off half the half the hole. And you can be left with little daggy bits that short out and all sorts of things. So, you know, there's a bit of there's a bit of art there. So, to

**Dave Jones:** design that, they would have had to tee this up with the manufacturer to make sure the manufacturer could do exactly what they wanted here. Um, so yeah. Anyway, um, so oh, so you can get selective. Oh, oh, I just realized

**Dave Jones:** there's two variants. You can get ones that actually manually put the gap in there, or you can get ones that have no selective connectivity. OH, WELL, was that up in the part number? That's not up in the part

**Dave Jones:** number. How do you select your uh, selective connectivity? I'm not sure. Anyway, I won't go into the details, but it's very cool that you got both types. They've thought about this. So, you can put these on pin headers, which then go

**Dave Jones:** if you want to plug it extend it on your regular breadboard, you can do that, no worries. Um, and then you can route it like manufacture them into cubes like this and right-angle stuff like that. I've done lots of that in industry, like

**Dave Jones:** you know, mount uh, boards in into cubes and different angles and all sorts of things like that. Very handy. So, you know, you can that's just yeah, a cool way you can solder those together, and then you can use jumper links. These are

**Dave Jones:** the These are the selective ones. So, you just solder your regular jumper, and then you can just put jumper links in there to select which ones you want. It's great. Or you can use jumper pins. They They gave me some jumper pins here.

**Dave Jones:** Um so, you can just like solder those directly on if you want a bit more low profile and more permanent um kind of thing. And you can put zero ohm resistors in there, and it's great. And then you can stack them

**Dave Jones:** like this, so you can have like a soldered like that. Like, you know, permanently soldered together um if you want a really low form factor thing. So, if you're designing something fairly low form factor, but you don't want to

**Dave Jones:** design an entire custom piece of it, you can get away with doing so you know, using these boards to do a reasonably low profile QB solution or something. Or you can have ones that yeah, you can actually plug them together like this.

**Dave Jones:** Just selective plug-in. And it looks like they've thought about the width. Like, it looks like it matches the Raspberry Pi width here. Isn't that great? So, they've thought about everything. And there's more like color coding to the pads and things like that that you can

**Dave Jones:** do here. And this is This is really remarkable. This is the most flexible thing that I I think I've ever seen in terms of these proto boards. Wow. They've you know, hats off. They've really gone to town here um in in what you can actually do

**Dave Jones:** with these things. Hats off. Progress in Electronics. This is great. This is progress. Yes, I like it. So, yeah, huge thumbs up to that. I'm very very impressed. So, hopefully he'll get back to me with the Kickstarter link cuz as

**Dave Jones:** I'm recording this, it's not yet available, but he says he'll hopefully get it the Kickstarter operational when I release this video, hopefully. So, check the link down below. They thought of everything. This is terrific. Although, Murphy's law, you'll get these and it just won't

**Dave Jones:** do exactly what you want. There'll be one jumper link. Bloody bastard. Hi to all my viewers in Scotland. You might recognize this guy. Ian Scott Johnson, fellow YouTuber. I'll link him in down below. I'll definitely check out his channel. It's awesome. And

**Dave Jones:** I had to Google what this was. I had to Google Lens it and Google Lens says this is a Scottish Highland cow. So, cool, I guess. Anyway, up to Yeah, let's see what Ian I think I know what this is

**Dave Jones:** cuz he did clue me up he was sending something, but let's have a squeeze.

**Dave Jones:** OH, THESE BLOODY um these you know, if you don't cut every single fiber in these things, they really get stuck. These are bloody tapes. Look at them. Unbelievable. Jeez, THAT WAS AN EFFORT. THEY'RE PRETTY strong those um fiber

**Dave Jones:** tapes or whatever you call them. We'll read the note in a sec, but he has sent one of his creations. It's very well packaged.

**Dave Jones:** This sucker will be quite useful. Look at this. This is one of his custom creations. This is great. It's specialized bit of kit if there ever was one. It's a DMM digital multimeter continuity tester. So, it's designed to

**Dave Jones:** plug into your multimeter and then you can set your mark space ratios for the pulses that go into your multimeter and you can see if it beeps. You can test the response time of your multimeter. It doesn't get more

**Dave Jones:** specialized than that. Version 1.2 for those playing along at home. And yeah, isn't that a nice little build? I like that and 9-V battery holder on the bottom. That is sweet as. Let's give it a burl. So, 9-V battery

**Dave Jones:** in. Got a little slide switch on the side here, and DMM continuity tester version 1.2 is just updated the firmware. So, we can set our mark and space ratios in milliseconds here, and our period, and then and gives you the readout in hertz

**Dave Jones:** there. So, we can just Yeah, we can just change that. Look at that. Why doesn't that give 1.1 ms? Oh, it can only go up Oh, no, it can. Is that a key bounce thing? Not sure what's going

**Dave Jones:** Can I get five? Oh, I adjust. Yeah, I think that might be a key bounce thing. And here's his note, and he's got some example times for various multimeters here. We'll confirm these, and there's his web address for those playing along

**Dave Jones:** at home. Definitely, if you're not subscribed to Ian, you definitely should be. So, and we've got a schematic. Beauty. So, we've got an Arduino Pro Mini here. We've got just a little LCD module. Yeah, regulation and switches, and this

**Dave Jones:** is a whole shebang, basically. There's our two connector interface. We've just got two MOSFETs here. So, basically, this is the driver which comes from the micro over here. It's driving and just the gate. It's just pulling that down to

**Dave Jones:** ground, and then just basically just switching on the MOSFET here. Very in the straight across the terminals. Very simple. So, we simply plug it in, and then it's it's continually shorting these out at a Well, at a frequency

**Dave Jones:** there of 3.9 hertz. So, 4 hertz there, and you can see like it's not beeping there, right? So, all we do is we just increase this until we can get it to No, I might have to hold Yep, yep, yep,

**Dave Jones:** there we go. So, we got it there. And you can see it's doing So, you 3.7 hertz there, and that's what that is. So, so the BM235 is uh about 16 reliably at 18 milliseconds. Uh yeah, let's just say

**Dave Jones:** reliably at 20 milliseconds mark there. So, that's a total period of 270 milliseconds there. So, can we lower that?

**Dave Jones:** We can see that we're getting silly now. We're getting It's just continuously beeping, but it is actually detecting that. So, a space is just going to as we increase the space, our frequency is going to go down. So, of course, all we

**Dave Jones:** really care about here is the mark, which is basically closing the contacts, you know, turning on that MOSFET, shorting out your two input terminals here. So, that's the That's the thing that you know, the other the space and

**Dave Jones:** everything is just like how it actually repeats. So, it seems to be yeah, about 18 milliseconds reliably there. I mean, that's still That's more than anyone needs. No one will ever need more than 640K of memory. The BM2257

**Dave Jones:** is way faster. We're talking uh three? Two, yeah. Let's Let's just say three milliseconds there. Woah. And the fastest bad boy on the block, the BM786, um up, down, down, down, down, down, down. We're in microseconds now, hundreds of

**Dave Jones:** microseconds. And Look at that. That's as low as it goes, and it's still doing it. 10 MICROSECONDS. CAN'T GO ANY LOWER. AND THE VENERABLE FLUKE 87V, WELL, I think we're going to have to go a fair bit quicker than this.

**Dave Jones:** Or slower, sorry. Woah. There we go. That's pretty good. YEAH, 0.88. WOAH. 880 MICROSECONDS. There you go. It's not too shabby. So, thank you very much, Ian. That is a cool bit of like really niche test kit that

**Dave Jones:** pretty much only multimeter reviewers or curious individuals would need. So, yeah, this is going to be very handy and my will be my standard bit of kit for testing multimeters going forward. Super duper handy. I don't think Ian Anyway, I'll

**Dave Jones:** link in Ian's channel. I don't think he sells them, but I guess if you want to buy it off him, he'll probably make one for you. Anyway, awesome. Thanks, Ian.
