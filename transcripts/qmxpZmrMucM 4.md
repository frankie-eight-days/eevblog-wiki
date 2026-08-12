---
video_id: qmxpZmrMucM
title: EEVblog #1003 - Mailbag
url: https://www.youtube.com/watch?v=qmxpZmrMucM
source: youtube-asr
timestamps: {"0": 0, "1": 27, "2": 44, "3": 78, "4": 106, "5": 129, "6": 155, "7": 172, "8": 206, "9": 220, "10": 248, "11": 277, "12": 297, "13": 323, "14": 353, "15": 386, "16": 410, "17": 428, "18": 443, "19": 463, "20": 484, "21": 506, "22": 521, "23": 544, "24": 573, "25": 588, "26": 606, "27": 637, "28": 669, "29": 701, "30": 721, "31": 743, "32": 763, "33": 775, "34": 806, "35": 826, "36": 845, "37": 870, "38": 891, "39": 920, "40": 941, "41": 971, "42": 987, "43": 1021, "44": 1051, "45": 1074, "46": 1093, "47": 1134, "48": 1160, "49": 1205, "50": 1240, "51": 1269, "52": 1287, "53": 1306, "54": 1333, "55": 1355, "56": 1371, "57": 1388, "58": 1418, "59": 1438, "60": 1451, "61": 1481, "62": 1505, "63": 1532, "64": 1547, "65": 1573, "66": 1596, "67": 1615, "68": 1637, "69": 1664, "70": 1696, "71": 1721, "72": 1755, "73": 1780, "74": 1806, "75": 1839, "76": 1867, "77": 1890, "78": 1909, "79": 1940, "80": 1966, "81": 1990, "82": 1999, "83": 2019, "84": 2045, "85": 2078, "86": 2105, "87": 2123, "88": 2155, "89": 2180, "90": 2197, "91": 2230, "92": 2254, "93": 2284, "94": 2309, "95": 2345, "96": 2384, "97": 2404, "98": 2424, "99": 2440, "100": 2469, "101": 2496, "102": 2526, "103": 2556, "104": 2576, "105": 2596}
---

**Dave Jones:** Hi, welcome to everyone's favorite segment, mailbag. Yes, we've cracked a thousand and we're back into it. Thank you very much, person unknown from Bourke Street, Melbourne is where they posted it. So, thank you very much. I've no idea what it is. No idea who it is from. And yes, I'm cutting towards myself because it triggers people.

**Dave Jones:** All right, let's have a look. Ooh. It is from John. Good on you, John. Cleaning out spare PCBs and I found this old active processor card from an IMS POC model. I have also no idea what that is. Wow, look at that.

**Dave Jones:** One of those industrial uh blade thingamabob PCs. Two minute. Well, there's not much to tear down. I can take the lid off it, but uh yeah, have a quick squeeze. John has very kindly sent in this uh Alco what looks like Well, there's the number for those playing along at home. An Alcatel Lucent uh telecommunications PC processor. It's got uh multiple gigabit ethernet, I would assume, ports, USB port. So, I assume it's some sort of, you know, Intel processor based uh system. It's got uh expansion cards like

**Dave Jones:** this. I've taken off uh a lot of the uh top metal work. So, I'm not sure what that is, but CPU quad I don't know. You'd have to uh know what these things do, but obviously some sort of telecomes processor, modern phone system, I would assume, because, you know, they don't use the old twisted pair stuff coming in and uh analog systems. It's all done digitally these days. So, maybe that's what it's doing or maybe doing some trunk link or something, I'm not sure. Um anyway, this

**Dave Jones:** is another uh little uh power supply card that was actually mounted on a point one inch header on the back here. Huge heat sink. That's obviously the main processor. It might not be an Intel based uh system. We'll have a look. So, we've got our memory modules here. What are they? There you go. For those playing along at home, what is it? 4 gig PC2 5300. Meh, you know, but it's okay.

**Dave Jones:** So, we'll salvage those. Thank you very much. They might come in handy. Um and there's lots of stuff to salvage on this and you can see the engineering that has gone into this thing. Absolutely phenomenal. These things, I don't know what sort of volume they'd make these in, you know, like the thousands, tens of thousands, maybe. You know, these are not consumer stuff. You can see all the via fan out on the bottom of the processor and the other main chip down in there with the

**Dave Jones:** bypassing in there. Absolutely classic stuff. They've got little little tiny 0402 jobbies down in there for your bypassing. There you go. For those viewing in HD, you can probably just see those, but the amount of engineering which goes into these is a phenomenal.

**Dave Jones:** No expense spared. Um we've got, obviously, uh some sort of custom custom connector with different length pins so that these ones are presumably be ground, the longer ones, so the ground makes contact first and then this one makes contact before this one. So, they're very specific in how they would like live, probably live power up these things cuz you don't want to shut down your whole rack when you change these things, but you want some sort of predictability in your power supply powering up and stuff like that. So,

**Dave Jones:** that's why they customize this with the different length pins to make sure it does first look little DC to DC converter modules down in there. Is that one of those TI ones off the shelf? You could salvage that. Lots of salvageable parts on this.

**Dave Jones:** Look at these Nichicon caps. Thank you very much. 220 mic 100 volt surface mount jobs. Wow. Got another look like a huge power brick down in there. I'm not sure what's going on. There's another another power brick down in there vertically. You'd suck that out. No worries. Put that in your parts bin. Um and these, check them out. Spared no expense. Ah, there you go. Upside down or the electrons are going to fall out.

**Dave Jones:** LTM 4600. These are These are DC to DC converter hybrid modules and these are Linear Tech ones. Really expensive. They're like, you know, 15 20 bucks each in volume. And they just put these all over the board, you know, because it doesn't matter. You're not trying to meet a consumer price point. You engineer this thing to work and be reliable. So, you don't want to be around with your time trying to design a DC to DC converter when you can just buy all these off-the-shelf modules

**Dave Jones:** and little hybrid bricks and stuff like that. Whack them on. Job done. You know, who cares if they cost 20 30 bucks a pop? There's another one in there. There's another one there. Who cares? You don't want to be wasting your time engineering a power supply solution for something like this. So, yeah, look, the amount of engineering is phenomenal in something like this.

**Dave Jones:** Anyway, let's go in and have a look at a couple of the chippies. What's that? Some sort of Intel job? That's some sort of bridge chip, I would imagine. Uh bit of Lattice glue logic down in there. Let's have a look under the heat sinks here. See what we've got. And yes, it is Intel, but rather interestingly, it's a Core 2 Duo. It dates from like 2007.

**Dave Jones:** It's a quite an old beast. So, we're talking, you know, 10-year-old processor tech here. But yet, none of that socket rubbish. It's It's soldered directly down onto the main board. No worries. It looks like we have Intel coming out the wazoo. Check out down here. Not only do we have some PCB mount fuses here, but look, we've got some two diode current shunt resistors down in there. So, obviously doing some uh current rail monitoring of some description. And that was a uh SAS drive controller card. Hard drive's been

**Dave Jones:** removed. And this puppy here is a shelf controller. Whatever that is, I don't know. You'd have to know your uh Alcatel-Lucent Telecoms uh systems. But once again, another big power brick on there. Look at that. Oh man, you can sell sell so many parts on these things. It's absolutely incredible. So, thank you very much, John, cuz these are a fascinating look at some highly engineered specialized telecom bits of kit. I don't know how large the design team would have been to make this thing, but it would have been absolutely

**Dave Jones:** enormous. And they, you know, like unsung heroes designing this sort of stuff. Really probably leading edge uh stuff at the time and a ton of engineering. And if you can get hold of old boards like this, I mean, 1 2 3 4 5 6 7 at least modules. Eight. You don't have to suck them out, but jeez, you can really reuse those. They're very nice.

**Dave Jones:** Whoop, another sneaky two over there. So, you can reuse a bunch of parts out of something that's seemingly, you know, like obsolete. Like you couldn't sell this on eBay even if it worked, probably. Um so, you know, it's just ancient tech. Don't know what's wrong with it, but those power supplies that still work. But really interesting.

**Dave Jones:** Thank you very much, John, for sending that one in. Guten Tag to all my German viewers. Uh specifically Ingrid Buse if I'm pronouncing that correctly from Kohl O with two little e's on the top. Um Thank you very much.

**Dave Jones:** I think I'm going to have to carefully open this one based on the description. So, sorry for you whoop big knife aficionados, but it seems like it Oh, yeah. Yeah, I might have done some damage with the big knife, I suspect.

**Dave Jones:** So, we'll slice and dice her open, and let's have a look. It is a painting. I don't know what that's of. I am not a uh art connoisseur. Oh, it's written on the back. Dear It's lengthy and very nice handwriting.

**Dave Jones:** In fact, I will for the record Here you go. Thank you very much, Ingrid. My name is Ingrid, and I am a big fan of your videos. Although, I do not know much about electronics. Um not uncommon. I became a pensioner 2 years ago, and my son gave me a laptop with internet.

**Dave Jones:** He realizes big electronics projects, even though he has no diploma. Awesome. You don't need any qualifications to do electronics at all. Um I once asked him where he got all that knowledge from, and then he mentioned a private internet electronic teacher.

**Dave Jones:** I guess that's me. Awesome. Since then, I watch your videos quite regularly, and I like to hear your charming voice, and the humor makes me quite laugh quite often. Next to the internet, I discovered other passion. I became an amateur artist. Awesome. I think painting is a great way to express yourself, especially when it comes to abstract terms. I agree. So, please keep it as a unique present. I will indeed.

**Dave Jones:** It's very nice. Thank you very much, Ingrid. That is lovely. I wish I had the ability to paint. I've thought about several times actually taking uh you know, classes doing what I would love to be able to paint. I wish I had a talent to paint or sculpt. I think that would be uh awesome. So, thank you very much, Ingrid, and to all those who watch without really, you know, having any interest in electronics. I get emails and comments like that all the time.

**Dave Jones:** Very surprisingly, but people just like my content. You can't like my voice. Nobody likes my voice. There's Ingrid and her son. Fantastic. Love that photo. Very nice. Good on you. Thank you very much Maco from Lodz in Poland. Awesome.

**Dave Jones:** Hi to all my Polish viewers. Good on you Nev from Adelaide. That's the return address. It just says Nev in Adelaide. That would have got back to him straight. It's a small place. No worries. Thanks. Hi to all my Adelaide Adelaide It's going to say Adelaidean viewers. Here down.

**Dave Jones:** We got a voltage detection stick. That's a bit Okay, back. They're the They're the Brymen distributors in Australia, Cabac. The volt finger. This thing's It looks a little bit dodgy. Good on you Nev. 2-minute teardown. Let's give it the finger. And we've seen these voltage detection sticks before, I'm sure. But let's have a look at it because Nev asked how these things work. Well, there's nothing to them. So these things basically work on capacitive coupling between the probe here, which got then goes through That's one plate of the

**Dave Jones:** capacitor, goes through a high value a current limiting resistor here. Uh there's just got a 74HC14 just for threshold type stuff. And then it basically the rest of it just drives the LED and the Well, the buzzer or whatnot. And well, that's all there is on this thing. It's basically nothing. So you might be thinking, well, where's the other plate of the capacitor? Where does How does current flow? Well, your hand This sits inside here. Your hand is around here like this. And it's capacitive coupling

**Dave Jones:** into your hand, which then flows down through your feet into the carpet or whatnot. And it We're talking minute amount of current. Absolutely minute. And there's only like, you know, 0.1 puff or something pico farads between like the wire you're detecting and here. But that's enough to make current flow when you got high impedance uh So yeah, they're just capacitively coupled. That's all it is. Thank you very much, Charles Alexian. I It's probably not how you pronounce it, but it's near enough. And I'm from Fresno in

**Dave Jones:** California. Hi to all my viewers in Fresno. I Have I been through I think I either driven through I think I've been through Fresno. I'm sure I have. Maybe I even stopped for lunch. I don't know. Can't remember. Um mailbag.

**Dave Jones:** EV blog executive towers. Yes, not Austria. And we do like typed letters as in typed on a real typewriter, a Brother SX4000 for those playing along at home. That's great. Triple 5 relaxing station. Looks like I've got a whole bunch of stuff I won't unbox. Well, go to the main bench.

**Dave Jones:** Mhm. I don't think I can help myself. Oh. Turns out there's actually a story behind the danger push button. Uh according to some old-timers, they were used to destroy decoder circuits in receiving equipment by igniting some of the charge that burned up the sensitive bits of the equipment.

**Dave Jones:** Apex in Los Angeles, I've been there. Um I've done a video on that. Might have to link it in down below. Had a case of them and had to And uh some of them have appeared to have the contacts wired in series as a simple means of redundancy.

**Dave Jones:** The contact action is unique. Apparently, employees from SpaceX found them and many of them are on their desks. Brilliant. Wait until you see this. This is very sexy. A glass device is a Bayard-Alpert style ion ionization gauge using vacuum systems. This style has been largely replaced by cold cathode types, but many are still to be found in use. It works by bombarding the positively charged spiral grid with electrons from the filament. Remaining gas will become positively ionized and fall to the negatively charged collector wire in the center, and this will

**Dave Jones:** represent an electrical current that is proportional to the gas pressure. Awesome. This one has a worn out filament. Ta-da! Look at that. Ah! Isn't that gorgeous? Wow! Look at that. It's got a port on it. And uh Wow!

**Dave Jones:** Very cool. Now, this tube here is apparently an experimental one that Charles made. And well, here we go. It's an experiment like I think the well, I'll let you read it. But um yeah, I don't know like pins two, and the grid is connected to first pin and eight. I don't Oh, no. Yeah, there we go.

**Dave Jones:** Up to pin eight. Uh let's power it up. I see nothing glowing glowing red hot. Aha! There we go. Sweet glowing goodness. Let's turn the lights out though. It was barely visible with the lights on. I've got a whole bunch of relays, a couple of LCDs, and these big huge stand-off slide switches. Only 3-amp jobbies, but look look at the width of those contacts.

**Dave Jones:** Wow! Actually, Charles included a note on this. So, he actually had these uh commissioned manufactured by uh Switchcraft to replace a Arcless great name, Arcless uh brand that they don't manufacture anymore. So, they had to replace them. So, they got them to custom make them for you. And they will.

**Dave Jones:** Companies will do this if you uh have significant uh volume and stuff like that. No worries. Hi to all my Austrian viewers, and sorry to Meinhard Kissich um for because this is a time-sensitive Kickstarter. Hm, sorry. Um yeah, this was like sent quite I don't even need that. This was sent quite a while ago, but it was like I just wasn't doing mail bags at that time. So, unfortunately, I couldn't uh couldn't do it. But let's check it out.

**Dave Jones:** There's obviously some hot Oh, look at that. Fancy pantsy. And there we go for the you QR code aficionados. And Is there hardware in there? No. Is it I got slice and dice that open. B B maths. Oh, we got some rulers. Oh, okay.

**Dave Jones:** Cool. PCB rulers. I spot a problem right off the bat. Sorry. Let's take a look at them, but they're they're flexible rulers. Min Harder is sending these cheat sheet rulers. And yeah, they're not PCB. They're made out of a you know, plasticky type thing. Anyway, these are designed to be well, let him say it himself. Designed to be little cheat sheets cheat sheets during exams during final exam.

**Dave Jones:** They have all the various formulas on them. Obviously, in these exams you're like it's an open book exam or something or you're allowed to like bring in a sheet of paper with all the formulas and and calculations and stuff on it. And they're all math related. They're not really not so much electronics related.

**Dave Jones:** So it's all the math math exams. I don't quite understand the B concept with all the um whole like the holes in it. I don't get it. And anyway, the one criticism the zero should start right at the end so you can do end stop measurements like that. Anyway, Min Harder reached the model's 2400 euro goal. Although I guess that buys you a lot of these. I don't know how much tooling would cost for one of these. Not a huge amount I'd imagine, but anyway, met the goal. So I'll link it in down

**Dave Jones:** below if you want one of these cheat sheet rulers for all you math nerds. That's not me. Sorry. And all my viewers from Ohio formally where Chris Gammell was from. And in particular Zach Kohler. At least we're not Detroit. Sorry. it's the old I might have to edit in the clip from that. Anyway, Cleveland versus Detroit, it's a internet meme YouTube meme thing.

**Dave Jones:** Fun times in Cleveland again. Still Cleveland. Come on down to Cleveland town, everyone. Under construction since 1868. See the sun almost three times a year. Looks like a Scooby-Doo ghost town. Buy a house for the price of a VCR. It could be worse though, at least we're not Detroit.

**Dave Jones:** We're not Detroit. What have we got? We've got a alarm clock thingy. Does it do anything else? Two minute tear down and one of those Oh, I could use those. Those Velcro straps. Sagan. It's for Sagan. Awesome, he's not here.

**Dave Jones:** But not sure what that is. What is that? Oh. Oh, what are they? Flashing fireflies. We have the American innovative USA alarm clock apparently. This one could allow you to set a different time for every day, which is rather interesting. Take it away. An expensive piece of rubbish. The Neverlate executive selling point was being Is that what it was called? To be able to set a different time for each day, a feature now covered in smartphones. The knob would tend to slip and double jump.

**Dave Jones:** Battery backup never worked. Audio worked well. Built down to a low price point apparently. Yeah, let's tear it apart. Well, this is rather odd. Like this sits on there like that. Speaker on the bottom, I get it because this sits off like that to direct the, you know, little like little acousticy kind of box to get that out. But look at that like the sides. Why are the sides like that? I don't entirely get it.

**Dave Jones:** Anyway, can this come apart? Yep. Wait. Hello. What's that? Hello Dave. Someone has pre-torn this apart. What? What is that? I got no idea what that is. But hello Dave. Someone knew at the factory that that's interesting. Check out how they've assembled the LCD on this thing. Look at that. The LCD module I haven't I don't think I I haven't seen that before. They've obviously designed that LCD controller to like sit in a cutout in the board and then they've just put the pads on the side and then bridge them

**Dave Jones:** over like that. So that's a rather interesting technique to get a low form factor like that rather than have it you know a pin header sticking out and stuff like not that they needed it with all this depth and everything else. But that's that's rather neat. Anyway, we've got double-sided load on the is that the Yeah, that's the receiver board down there cuz there's our ferrite There's our good old AM ferrite rod and just a single chip AM FM radio receiver and like Bob's your uncle. Got a down at the bottom

**Dave Jones:** there and a 1 W 8 ohm speaker. It's like like yawn. But the engineering sort of neatness and cleverness with the LCD in that cutout kind of ended with these tiny Look how they've actually gotten these off board wiring little tiny like What are they? Four four five six core wires going over to the top switch contact board over here.

**Dave Jones:** That's hideous. Somebody had to hand solder all those. Look at the Look at the contact on the PCB. Wiper contact, they went to all that effort. I Yeah, it's a weird. And that cabling's just like for production, that's a nightmare. Why would you go with that? Unbelievable.

**Dave Jones:** And these things are bike safety flashes from over 15 years ago and it still works. Do you just bang them like start it. Oh, yeah. There we go. Look at that. Beautiful. I don't know how long do they flash for? Like a minute or something? And Oh, I I guess the vibration still keeps them going. Eh.

**Dave Jones:** Neat. But yeah, after a Wow, what do they you know, couple of coin cells in there? And you know, LR44s or or something like that. I'm not sure like they actually require a a bit of force to get them going. So, I'm not sure how they keep going on the bike bike. Maybe you know, you stick them on the frame and they did the vibration and might keep them going or something, but All right, interesting. Can't really tear those down. You'd have to dremel the whole thing apart, I think. And all my

**Dave Jones:** viewers in Singapore, we don't get many from Singapore, do we? I love Singapore, it's a good uh probably my favorite Asian stopover on the way cuz Australia, like it's down on the bottom of the planet or top depending on your perspective. And yeah, uh like we generally need a stopover if we're headed to uh Europe. So, you know, anyway, I've got Oh, sorry.

**Dave Jones:** Thank you. Uh no, from Yeah, person unknown. Um in Singapore. Oh, jeez, this is comprehensive. I'm a guy living in Singapore who wishes to remain anonymous. That's cool. Uh but have been watching your show ever since episode 395.

**Dave Jones:** Uh this note is going to be a little bit long, so read only underlined text if you don't have much time. We have got a black box. It's actually called a black box. Um, and it is black. Winner. Um, and it's like it's one of the Oh, it's a set-top box.

**Dave Jones:** 2 second tear down. This is a pay TV a piracy box. Um, I go figure. I I guess C1 stream box. And I didn't know that you could like just like it looks like a legit product. I mean, it's one of these little hacked together uh jobbies. You can see the little Wi-Fi module hacked in there and all sorts of stuff. And uh apparently he's ripped some uh parts out of this puppy, but um it connects to the Wi-Fi and downloads uh the encryption key stored in an

**Dave Jones:** off-site server in some undisclosed location. Unbelievable. Uh there you go. So, I don't know. Is anyone still getting pirate cable TV with, you know, um like I just get Netflix. I mean, yeah, I could probably get it off of Nicks, but it's just so convenient. I don't know.

**Dave Jones:** We don't have really Well, we do have cable TV here. We have Foxtel, but I don't think anyone bothers to uh you know, has any The market's not big enough to sort of hack together some uh box to get you Foxtel, I don't think.

**Dave Jones:** And not every home has it anyway. So, yeah. I don't know. Are you pirating your cable TV? Let us know down below anonymously. But NSA's tracking you anyway, so meh. And our anonymous friend has uh written very comprehensive details of um this box and how it works and stuff like that. So, uh for those playing along at home who want to uh have a read of that, go for it.

**Dave Jones:** Another one from Germany. This one comes from Allsdorf from uh Marcel Hansen. Thank you very much, Marcel. Let's check it out. No description. And it's just a lumpy thing. Oh. What? Why I have a dummy? Um Oh, you what?

**Dave Jones:** This is great. This is great. It's a It's a 50 ohm terminator dummy. Not a fan of dummies. They're not good for kids developments. I don't like uh They're not good for the mouth development. Their mouth doesn't form uh quite well apparently. So, but that Wow.

**Dave Jones:** A 50 ohm dummy. That's gold. Hi Dave, I'm sure you are familiar with terminators because electrons are shy and afraid of photons. They get scared when they reach the end of an open cable and run right back, the little buggers.

**Dave Jones:** Hence, the terminator was invented to keep the light out of coax cables. Yes, true story. It's on Wikipedia. Uh We have at uh First Advanced Industrial Labs, I love the name of the company. I wish I'd thought of it. Uh proudly present to the EVblog latest in termination technology. If you are planning to have another child or maybe know a fellow engineer who has a suitable host device, you are welcome to try it out. Thank you very much, Marcel.

**Dave Jones:** Technical specs, impedance is 50 ohms of course, uh 20 dB noise reduction, and uh plus 400% sleep mode duration. Awesome. I just Is there anything better? Look at this. Look at this. It's just fantastic. 50 ohm dummy load.

**Dave Jones:** Thank you very much, Reflower. Flow R, Reflow capital R dot com. Um for what we've got in here. It sounds interesting. Looks like it sounds like there's multiple uh things in here. So, let's check it out.

**Dave Jones:** Oh. Oh, wow. Wow. We've got a kit and a sweet Oh, it's a Yes. Right. Has this been sitting here for a while? I'm not sure. I think I saw this. Um yeah, the reflower Was it a Kickstarter or something?

**Dave Jones:** Uh or it was talked about on the EEVblog forum or something like that. It's a mains in um and a red button on there with a thermal couple and it it's just a um a reflowing plate. So, you stick your board on the top and um apparently you can reflow your boards. So, I'm not It's not something I can demo on the mailbag. Wait, Dave. I hope you like my reflower project. It is really easy and convenient to use. It comes with a small test piece. We have

**Dave Jones:** everything you need. One screw open teardown. Oh, apparently it's quite easy. And this is the note. Uh yes, it was a a crowdfunding campaign. Apparently, this is the one that's shipped. So, that's the note that uh ships with it. A few issues and all that sort of stuff. I like that, you know, being honest and uh tell everyone about the uh you know, in issues that come with the shipped product. Anyway, I'll link it in. It's manymaker.com with a uh hyphen in there. But there it is. There's the reflower. It's

**Dave Jones:** just the plate on top. Gets hot. You stick in your mains. I don't know um uh if you have to hook an external thermal couple on. Haven't seen it yet, but uh presumably it will uh is programmable with a profile. So, you know, it's it's pretty crude. I mean, like all the corners are sharp. You could sort of like cut your like that. I could probably slice If I put my hand down there, I might be able to slice my hand open like that. So, it

**Dave Jones:** really is a uh you know, a sort of a or maybe, you know, a practically prototypey uh type thing, but they have uh shipped apparently and well, let's crack it open. Have a look. Sure enough, there was one giant screw on the bottom. And ta-da! We're in like Flynn. Oh, I got some real insulation. That's I don't know what sort of insulation that is. Some sort of fibery fibrous type um insulation. You need that, of course, to isolate cuz that thing's going to get hot. I

**Dave Jones:** mean, it's soldering temperature and there's not much doing down there at all. It's neat enough, I guess. It's all self-contained on one PCB. Mains straight in. It's mains uh fuse down there with with the proper shrouded uh fuse holder on there and uh well, that's about it. And they've got a 3-W uh DC-to-DC brick converter down there. I'm not sure why they needed a 3-W jobbie.

**Dave Jones:** That's actually a lot um cuz the heater is going to be uh mains uh heated, of course. Um so, yeah, I That's a fairly decent size brick. So, I'm not sure why they needed that sort of level, but it must all be all the smarts of it must be on the bottom of the board. But, it looks like there's like a little uh Wi-Fi modules down in there. Is that one of those uh ESP uh 8266s?

**Dave Jones:** And Lafras has very kindly included the PCB so we don't have to take this puppy apart and uh we should be able to see some Yep, mains isolation there. Look at that. Very nice. No worries whatsoever. And there's all your control stuff on the uh bottom side and that was going off to the uh Wi-Fi module over Yep, Wi-Fi. There it is over there. And a fan, buzzer, LED, and your uh thermocouple input. So, that's a neat little board. I like it. And they've included an experimenter's uh kit with

**Dave Jones:** some uh PCBs. These are for uh reflow soldering uh practices like the one that's got the thermal pad on the bottom. That's pretty neat. Um and yeah, we've got the uh well, a stencil, actually. That's probably not it. Maybe that's just a dummy board. I think that's the real Yeah, that's the real board for uh reflowing uh stuff, some paste, and uh thermal couple, and a um and I assume that's a spreader.

**Dave Jones:** Is it? Yep. Uh you really need a plastic like a just a simple uh plastic credit card or something like that does the job better than a fixed metal one like that for a spreader. A plastic card would have been much better. But yeah, that's a little experiment as kit that either comes with it or you can get separately just to get you started. So, that's interesting. It's not something I can play around with. I should play around with on the mail bag here. So, I might

**Dave Jones:** do a separate video on that. And it it's got a fair way to go to be like a commercial uh quality, you know, a commercial quality product. It's sort of a bit proto type here at the moment, but you know, I am I'm curious to see how well it works cuz you really um cuz fiberglass is like a thermal insulator.

**Dave Jones:** So, you've got to stick that on the surface. Okay, the surface heats up, and yeah, you might be able to you'll eventually get the heat uh transferring through to your boards, but it's by no means the best way to do it. Um in fact, these generally uh a hot plate like this under a board would be used as a preheater. So, um yeah, not really for soldering. So, I'm you know, I think it might have to stay there too long uh to get the heat transferred to the pads on the top. You

**Dave Jones:** know, it might be okay if you've got one of these uh you know, thermal pads on the bottom which then can conduct heat through to there, but that's that's like preheater uh type stuff. So, yeah, I don't know how well this concept's going to work. They've taken basically a preheater concept and tried to make it into a uh you know, a reflow oven replacement, which it's not.

**Dave Jones:** I I find it hard to believe it's going to do a you know, as as good a job as a thermal oven. Just the thermals don't make sense to me, but hey, I haven't tried it yet, so I have to do that in a separate video and I'll link it in down below if you want to check out the reflower. There was a thread a while back on the EV blog forum on this, I think. Hi to all my Canadian viewers and uh Andrew in particular, no last name.

**Dave Jones:** Uh we have a gift. Thank you very much. So, let's see what we've gotten from Canada.

**Dave Jones:** It is a Hi Dave, greetings from Vancouver. I love Vancouver, great city. To this day, I still regret when I was in Vancouver deciding not to go to a Steven Seagal concert. Concert, not movie, concert.

**Dave Jones:** Long story. Anyway, um do not open this on camera. Okay. And we've got a Trezor, the original hardware wallet. Okay, it's a um Oh, okay, it's a it's a Bitcoiny wallet, is it? Trezor. What other What other type of digital wallet would you have?

**Dave Jones:** I'm not sure. Hardware wallet, doesn't say anything about Bitcoin or anything like that, but uh usually that's what the hardware wallets are for, for storing your Ethereum or your Bitcoin or your 10 million other bloody altcoins. And sure enough, this is a Trezor hardware crypto Bitcoin wallet um with a little LCD designed to securely store your crypto uh currency. And the letter, Hi Dave, I'm in Vancouver, more on the IT side. So, how it works is the private keys never leave Trezor and the device will show the recipient's address

**Dave Jones:** directly on display, so you can be sure you're sending the funds to where they want to go. Think of it as a drastically overgrown one-time password token, which adds an unhackable something you have, something you know. Um it makes them a high-value target, no kidding. Um so, he wants the insight into the overall build quality and durability of devices well of its tamper resistance and tamper evidence stuff. And yes, um I have read this as well. Someone's performed a power line monitoring attack and they were on this, an early version of this,

**Dave Jones:** and they were able to retrieve the private key from it, but it is it has since been fixed uh like 2 years ago, uh 2015 I believe that was uh fixed. So, that was a long time ago. And yes, I did not open the other letter on camera, which says do not open this on camera.

**Dave Jones:** And I've opened it and this is why I can't do a teardown right now. There's something in the additional in that envelope that uh yeah, it's just I can't tell you about and I won't be doing a teardown of this right now, but possibly in the future, we'll see. Sorry, secret squirrel stuff. That crazy Aussie bloke, that's me. Um let's open it up. Uh thank you very much, Bond and Broon. I I can't pronounce uh let us NATO.nl.

**Dave Jones:** Um Netherlands, isn't it? NL, this is going to be I don't know. It's kind of wrapped in electrical tape, is it?

**Dave Jones:** Got it. Wow, it's a cheap ass multimeter. It's already broken. Oh dear. Oh, look it comes on. 2-second teardown.

**Dave Jones:** Do I have to? At least this one has a ceramic fuse over there for the 10 amp range. Uh like, you know, whatever. Hi to all my Spanish viewers, in particular Alberto Piganti. Good on you, Alberto. Uh we don't get too many from Spain, although Spain probably punches above its weight in mailbag, possibly. I don't know. Oh, but Spain's a big country, isn't it? I haven't been to Spain. Let's have a quick squeeze. What do we got?

**Dave Jones:** We have something in a black felt Oh, I'm sensing retro. Craig. We haven't ever had a Craig cal- It's a No. It's a learn learn thing. It might be one of those um the Craig M100. It could be one of those uh language translator things. Linguistico.

**Dave Jones:** Linguistico. Yep, I was right. And we've got a big What is this? It's a book. ABC Basic Connec- Oh, Alberto. It's Alberto's book. ABC Basic Connections. Woohoo! Hey. Ah, it's It's a wrap for our protection. Let's have a quick squeeze. Alberto, is this like a Kickstarter?

**Dave Jones:** Awesome. Hi Dave, I'm Alberto. Uh you probably remember me from pinouts.on uh pighigh. piggy. pighigh.xxx.com. That sounds legit. Um I'll link it in down below. It is legit, trust me. Um it's safe for work. I'm super excited now that I'm running a Kickstarter campaign for my latest book, ABC Basic Connections. Send you a pre-release copies. Tell me what you think. I hope you love it. More information, abcthebook.com.

**Dave Jones:** And unfortunately, it's already ended on Indiegogo, but raised 115,000 euros, double the target for this Basic Connections. And it's beautiful. Ring binder, love it. And e-reader as well. You don't get an e-reader anymore, do you? It's basically just information on Arduino and stuff like that. So, here's all the different pinouts and things, which I I believe a lot of, maybe all of them, are available on the website, but this is in book form. And so, we're just showing, you know, schematic symbols and stuff like that. We've got some Ohm's law stuff,

**Dave Jones:** Ohm's law triangles. We've got the resistor stuff. It's beautiful, beautiful quality. I love the artwork and everything in this. It's just absolutely fantastic. Now, this doesn't have the Creative Commons on it. The ones I saw on the website actually have Creative Commons. So, anyway, this is how to hook up all sorts of stuff to Arduino. This is absolutely brilliant. I like I can like the graphic layout of this. Imagine how long this took. It's absolutely stunning. I love it. Awesome work. And it Yeah, I can see why it actually

**Dave Jones:** Warning, Wil Robinson. Why it got 115,000 euro back. This is a lovely reference resource. You know, sure, yeah, you can just do it as a PDF, but it it's not the same as having this. And look at this. Oh, foldout porn. Oh, look at this. Centerfolds. Oh, yeah.

**Dave Jones:** This is This is fantastic. Anyway, if you are dealing with Arduinos, you're a beginner, and you want a nice reference book for hooking up stuff, check it out. Do yourself a favor. Hello. Buongiorno. Hands up if you had one of these. I can type that in and go hands up if you have one of these.

**Dave Jones:** A Craig M100. Of course any smartphone can do the translation I can even probably you know listen to the person's voice can't it and then just automatically tell you what they said. I DIFFERENT WORLD. WOW, LOOK HOW OLD SCHOOL THIS puppy is.

**Dave Jones:** 1979. I kid you not. Wow, what's an SL 9200 44th week 79 made in Singapore. A lot of chips were made in Singapore back in the day. Wow, look at that little budge board over there. Is that a is that a little uh convert is it a No, that's an inductor is it? So that's a little switching No, switching what?

**Dave Jones:** Thought some sort of switching converter. Anyway, look at the finest budge board over here. Vertical resistors. Fantastic. Thank you very much. So it's basically just a processor a vacuum is it Yeah, I presume vacuum fluorescent display down in there and the cartridge ROMs which you can There you go. That's the Italian ROM. Wow, copyright 1980.

**Dave Jones:** Wow. So there it is. Oh, look at that. Beautiful. So yeah, it's just a like it doesn't it just doesn't do anything fancy. It's just you typing the word and then maps it to a ROM entry and then displays the mapped word. But anyway, there you go. You can put three different languages inside this thing. This would have been the ducks guts back in the day. This would have been like black magic technology back then.

**Dave Jones:** Oh, I can't get enough of the nipple. You know, I love it. Well, I'm curious to know now. I can't read the Well, I guess I could just translate the manual, couldn't I using one of my newfangled smartphone thingies or Googly or whatever it is, but it does have like a learn I presume that's that learn button on the front, but this is like a ROM-based thing. So, like I wouldn't expect it to do anything like algorithmically fancy. I expect it just to map words in one language to another and

**Dave Jones:** that's it based on the ROM. Uh you know, entering content they probably sort putting them in alphabetical order in the ROM or whatever and then translate them over, but I don't know. Um Hmm, maybe it does a little bit more, but I wouldn't have thought so. And unfortunately, it doesn't work. The LED comes on, but yeah, it's nobody's home.

**Dave Jones:** So, that's an absolutely fascinating little module there how they've bent the pins over on just a standard ROM, put a lovely little label on there, and made their own little sort of, you know, like little plug-in thing with a handle. That's It's really rather clever. I like it.

**Dave Jones:** So, anyway, thanks for everyone who sent in something for today's mailbag and sorry if I haven't gotten around to yours yet. I will endeavor to do it next time. Anyway, if you like mailbag, please give it a big thumbs up. Catch you next time.
