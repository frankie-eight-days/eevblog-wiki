---
video_id: qmxpZmrMucM
title: EEVblog #1003 - Mailbag
url: https://www.youtube.com/watch?v=qmxpZmrMucM
source: youtube-asr
timestamps: {"0": 0, "1": 18, "2": 39, "3": 54, "4": 71, "5": 82, "6": 98, "7": 112, "8": 123, "9": 139, "10": 151, "11": 168, "12": 184, "13": 199, "14": 212, "15": 229, "16": 245, "17": 258, "18": 271, "19": 285, "20": 297, "21": 315, "22": 329, "23": 344, "24": 360, "25": 375, "26": 390, "27": 406, "28": 419, "29": 432, "30": 448, "31": 471, "32": 494, "33": 506, "34": 520, "35": 534, "36": 546, "37": 561, "38": 576, "39": 589, "40": 606, "41": 621, "42": 636, "43": 651, "44": 664, "45": 679, "46": 694, "47": 713, "48": 730, "49": 749, "50": 763, "51": 773, "52": 789, "53": 802, "54": 820, "55": 838, "56": 854, "57": 870, "58": 889, "59": 906, "60": 919, "61": 937, "62": 954, "63": 973, "64": 985, "65": 1002, "66": 1017, "67": 1032, "68": 1053, "69": 1071, "70": 1093, "71": 1120, "72": 1132, "73": 1146, "74": 1166, "75": 1190, "76": 1205, "77": 1217, "78": 1235, "79": 1253, "80": 1274, "81": 1290, "82": 1303, "83": 1318, "84": 1330, "85": 1342, "86": 1358, "87": 1373, "88": 1387, "89": 1403, "90": 1417, "91": 1434, "92": 1447, "93": 1460, "94": 1480, "95": 1501, "96": 1517, "97": 1532, "98": 1547, "99": 1563, "100": 1573, "101": 1596, "102": 1615, "103": 1635, "104": 1650, "105": 1662, "106": 1675, "107": 1689, "108": 1705, "109": 1717, "110": 1730, "111": 1746, "112": 1763, "113": 1776, "114": 1792, "115": 1803, "116": 1818, "117": 1834, "118": 1849, "119": 1865, "120": 1878, "121": 1888, "122": 1899, "123": 1910, "124": 1925, "125": 1940, "126": 1954, "127": 1972, "128": 1981, "129": 1994, "130": 2014, "131": 2042, "132": 2058, "133": 2074, "134": 2085, "135": 2097, "136": 2110, "137": 2123, "138": 2138, "139": 2158, "140": 2180, "141": 2197, "142": 2215, "143": 2233, "144": 2254, "145": 2281, "146": 2299, "147": 2314, "148": 2332, "149": 2345, "150": 2361, "151": 2381, "152": 2396, "153": 2414, "154": 2428, "155": 2443, "156": 2459, "157": 2476, "158": 2499, "159": 2515, "160": 2529, "161": 2542, "162": 2558, "163": 2571, "164": 2587, "165": 2601}
---

**Dave Jones:** Hi, welcome to everyone's favorite segment, mailbag. Yes, we've cracked a thousand and we're back into it. Thank you very much, person unknown from Bourke Street, Melbourne is where they posted it. So, thank you very much. I've no idea what it is. No idea who it is

**Dave Jones:** from. And yes, I'm cutting towards myself because it triggers people. All right, let's have a look. Ooh. It is from John. Good on you, John. Cleaning out spare PCBs and I found this old active processor card from an IMS

**Dave Jones:** POC model. I have also no idea what that is. Wow, look at that. One of those industrial uh blade thingamabob PCs. Two minute. Well, there's not much to tear down. I can take the lid off it, but uh

**Dave Jones:** yeah, have a quick squeeze. John has very kindly sent in this uh Alco what looks like Well, there's the number for those playing along at home. An Alcatel Lucent uh telecommunications PC processor. It's got uh multiple gigabit ethernet, I would assume, ports,

**Dave Jones:** USB port. So, I assume it's some sort of, you know, Intel processor based uh system. It's got uh expansion cards like this. I've taken off uh a lot of the uh top metal work. So, I'm not sure what

**Dave Jones:** that is, but CPU quad I don't know. You'd have to uh know what these things do, but obviously some sort of telecomes processor, modern phone system, I would assume, because, you know, they don't use the old twisted pair stuff coming in and uh analog

**Dave Jones:** systems. It's all done digitally these days. So, maybe that's what it's doing or maybe doing some trunk link or something, I'm not sure. Um anyway, this is another uh little uh power supply card that was actually mounted on a point one inch header on

**Dave Jones:** the back here. Huge heat sink. That's obviously the main processor. It might not be an Intel based uh system. We'll have a look. So, we've got our memory modules here. What are they? There you go. For those playing along at home,

**Dave Jones:** what is it? 4 gig PC2 5300. Meh, you know, but it's okay. So, we'll salvage those. Thank you very much. They might come in handy. Um and there's lots of stuff to salvage on this and you can see the engineering

**Dave Jones:** that has gone into this thing. Absolutely phenomenal. These things, I don't know what sort of volume they'd make these in, you know, like the thousands, tens of thousands, maybe. You know, these are not consumer stuff. You can see all the via fan out on the

**Dave Jones:** bottom of the processor and the other main chip down in there with the bypassing in there. Absolutely classic stuff. They've got little little tiny 0402 jobbies down in there for your bypassing. There you go. For those viewing in HD, you can probably just see

**Dave Jones:** those, but the amount of engineering which goes into these is a phenomenal. No expense spared. Um we've got, obviously, uh some sort of custom custom connector with different length pins so that these ones are presumably be ground, the longer ones,

**Dave Jones:** so the ground makes contact first and then this one makes contact before this one. So, they're very specific in how they would like live, probably live power up these things cuz you don't want to shut down your whole rack when you change these

**Dave Jones:** things, but you want some sort of predictability in your power supply powering up and stuff like that. So, that's why they customize this with the different length pins to make sure it does first look little DC to DC

**Dave Jones:** converter modules down in there. Is that one of those TI ones off the shelf? You could salvage that. Lots of salvageable parts on this. Look at these Nichicon caps. Thank you very much. 220 mic 100 volt surface mount jobs. Wow. Got another

**Dave Jones:** look like a huge power brick down in there. I'm not sure what's going on. There's another another power brick down in there vertically. You'd suck that out. No worries. Put that in your parts bin. Um and these, check them out. Spared no

**Dave Jones:** expense. Ah, there you go. Upside down or the electrons are going to fall out. LTM 4600. These are These are DC to DC converter hybrid modules and these are Linear Tech ones. Really expensive. They're like, you know, 15 20 bucks each

**Dave Jones:** in volume. And they just put these all over the board, you know, because it doesn't matter. You're not trying to meet a consumer price point. You engineer this thing to work and be reliable. So, you don't want to be

**Dave Jones:** around with your time trying to design a DC to DC converter when you can just buy all these off-the-shelf modules and little hybrid bricks and stuff like that. Whack them on. Job done. You know, who cares if they cost 20 30 bucks a

**Dave Jones:** pop? There's another one in there. There's another one there. Who cares? You don't want to be wasting your time engineering a power supply solution for something like this. So, yeah, look, the amount of engineering is phenomenal in something like this.

**Dave Jones:** Anyway, let's go in and have a look at a couple of the chippies. What's that? Some sort of Intel job? That's some sort of bridge chip, I would imagine. Uh bit of Lattice glue logic down in there. Let's have a look under the heat sinks

**Dave Jones:** here. See what we've got. And yes, it is Intel, but rather interestingly, it's a Core 2 Duo. It dates from like 2007. It's a quite an old beast. So, we're talking, you know, 10-year-old processor tech here. But yet, none of that socket

**Dave Jones:** rubbish. It's It's soldered directly down onto the main board. No worries. It looks like we have Intel coming out the wazoo. Check out down here. Not only do we have some PCB mount fuses here, but look, we've got some two diode current shunt

**Dave Jones:** resistors down in there. So, obviously doing some uh current rail monitoring of some description. And that was a uh SAS drive controller card. Hard drive's been removed. And this puppy here is a shelf controller. Whatever that is, I don't know. You'd

**Dave Jones:** have to know your uh Alcatel-Lucent Telecoms uh systems. But once again, another big power brick on there. Look at that. Oh man, you can sell sell so many parts on these things. It's absolutely incredible. So, thank you very much, John, cuz these are a

**Dave Jones:** fascinating look at some highly engineered specialized telecom bits of kit. I don't know how large the design team would have been to make this thing, but it would have been absolutely enormous. And they, you know, like unsung heroes designing this sort

**Dave Jones:** of stuff. Really probably leading edge uh stuff at the time and a ton of engineering. And if you can get hold of old boards like this, I mean, 1 2 3 4 5 6 7 at least modules. Eight. You don't

**Dave Jones:** have to suck them out, but jeez, you can really reuse those. They're very nice. Whoop, another sneaky two over there. So, you can reuse a bunch of parts out of something that's seemingly, you know, like obsolete. Like you couldn't sell

**Dave Jones:** this on eBay even if it worked, probably. Um so, you know, it's just ancient tech. Don't know what's wrong with it, but those power supplies that still work. But really interesting. Thank you very much, John, for sending that one in. Guten Tag to all my German

**Dave Jones:** viewers. Uh specifically Ingrid Buse if I'm pronouncing that correctly from Kohl O with two little e's on the top. Um Thank you very much. I think I'm going to have to carefully open this one based on the description.

**Dave Jones:** So, sorry for you whoop big knife aficionados, but it seems like it Oh, yeah. Yeah, I might have done some damage with the big knife, I suspect. So, we'll slice and dice her open, and let's have a look. It is

**Dave Jones:** a painting. I don't know what that's of. I am not a uh art connoisseur. Oh, it's written on the back. Dear It's lengthy and very nice handwriting. In fact, I will for the record Here you go. Thank you very much, Ingrid.

**Dave Jones:** My name is Ingrid, and I am a big fan of your videos. Although, I do not know much about electronics. Um not uncommon. I became a pensioner 2 years ago, and my son gave me a laptop with internet.

**Dave Jones:** He realizes big electronics projects, even though he has no diploma. Awesome. You don't need any qualifications to do electronics at all. Um I once asked him where he got all that knowledge from, and then he mentioned a private internet electronic

**Dave Jones:** teacher. I guess that's me. Awesome. Since then, I watch your videos quite regularly, and I like to hear your charming voice, and the humor makes me quite laugh quite often. Next to the internet, I discovered other passion. I became an

**Dave Jones:** amateur artist. Awesome. I think painting is a great way to express yourself, especially when it comes to abstract terms. I agree. So, please keep it as a unique present. I will indeed. It's very nice. Thank you very much,

**Dave Jones:** Ingrid. That is lovely. I wish I had the ability to paint. I've thought about several times actually taking uh you know, classes doing what I would love to be able to paint. I wish I had a talent to paint or sculpt. I think that would

**Dave Jones:** be uh awesome. So, thank you very much, Ingrid, and to all those who watch without really, you know, having any interest in electronics. I get emails and comments like that all the time. Very surprisingly, but people just like

**Dave Jones:** my content. You can't like my voice. Nobody likes my voice. There's Ingrid and her son. Fantastic. Love that photo. Very nice. Good on you. Thank you very much Maco from Lodz in Poland. Awesome. Hi to all my Polish viewers. Good on you

**Dave Jones:** Nev from Adelaide. That's the return address. It just says Nev in Adelaide. That would have got back to him straight. It's a small place. No worries. Thanks. Hi to all my Adelaide Adelaide It's going to say Adelaidean viewers. Here down.

**Dave Jones:** We got a voltage detection stick. That's a bit Okay, back. They're the They're the Brymen distributors in Australia, Cabac. The volt finger. This thing's It looks a little bit dodgy. Good on you Nev. 2-minute teardown. Let's give it

**Dave Jones:** the finger. And we've seen these voltage detection sticks before, I'm sure. But let's have a look at it because Nev asked how these things work. Well, there's nothing to them. So these things basically work on capacitive coupling between the probe here, which got then

**Dave Jones:** goes through That's one plate of the capacitor, goes through a high value a current limiting resistor here. Uh there's just got a 74HC14 just for threshold type stuff. And then it basically the rest of it just drives the LED and the

**Dave Jones:** Well, the buzzer or whatnot. And well, that's all there is on this thing. It's basically nothing. So you might be thinking, well, where's the other plate of the capacitor? Where does How does current flow? Well, your hand This sits

**Dave Jones:** inside here. Your hand is around here like this. And it's capacitive coupling into your hand, which then flows down through your feet into the carpet or whatnot. And it We're talking minute amount of current. Absolutely minute. And there's only

**Dave Jones:** like, you know, 0.1 puff or something pico farads between like the wire you're detecting and here. But that's enough to make current flow when you got high impedance uh So yeah, they're just capacitively coupled. That's all it is. Thank you

**Dave Jones:** very much, Charles Alexian. I It's probably not how you pronounce it, but it's near enough. And I'm from Fresno in California. Hi to all my viewers in Fresno. I Have I been through I think I either driven through I think I've been

**Dave Jones:** through Fresno. I'm sure I have. Maybe I even stopped for lunch. I don't know. Can't remember. Um mailbag. EV blog executive towers. Yes, not Austria. And we do like typed letters as in typed on a real typewriter, a Brother

**Dave Jones:** SX4000 for those playing along at home. That's great. Triple 5 relaxing station. Looks like I've got a whole bunch of stuff I won't unbox. Well, go to the main bench. Mhm. I don't think I can help myself.

**Dave Jones:** Oh. Turns out there's actually a story behind the danger push button. Uh according to some old-timers, they were used to destroy decoder circuits in receiving equipment by igniting some of the charge that burned up the sensitive bits of the equipment.

**Dave Jones:** Apex in Los Angeles, I've been there. Um I've done a video on that. Might have to link it in down below. Had a case of them and had to And uh some of them have appeared to have the contacts wired in

**Dave Jones:** series as a simple means of redundancy. The contact action is unique. Apparently, employees from SpaceX found them and many of them are on their desks. Brilliant. Wait until you see this. This is very sexy. A glass device is a Bayard-Alpert style ion ionization

**Dave Jones:** gauge using vacuum systems. This style has been largely replaced by cold cathode types, but many are still to be found in use. It works by bombarding the positively charged spiral grid with electrons from the filament. Remaining gas will become positively ionized and

**Dave Jones:** fall to the negatively charged collector wire in the center, and this will represent an electrical current that is proportional to the gas pressure. Awesome. This one has a worn out filament. Ta-da! Look at that. Ah! Isn't that gorgeous? Wow! Look at that.

**Dave Jones:** It's got a port on it. And uh Wow! Very cool. Now, this tube here is apparently an experimental one that Charles made. And well, here we go. It's an experiment like I think the well, I'll let you read it. But um yeah, I

**Dave Jones:** don't know like pins two, and the grid is connected to first pin and eight. I don't Oh, no. Yeah, there we go. Up to pin eight. Uh let's power it up. I see nothing glowing glowing red hot. Aha! There we go. Sweet

**Dave Jones:** glowing goodness. Let's turn the lights out though. It was barely visible with the lights on. I've got a whole bunch of relays, a couple of LCDs, and these big huge stand-off slide switches. Only 3-amp jobbies, but look look at the width of those contacts.

**Dave Jones:** Wow! Actually, Charles included a note on this. So, he actually had these uh commissioned manufactured by uh Switchcraft to replace a Arcless great name, Arcless uh brand that they don't manufacture anymore. So, they had to replace them. So, they got them to

**Dave Jones:** custom make them for you. And they will. Companies will do this if you uh have significant uh volume and stuff like that. No worries. Hi to all my Austrian viewers, and sorry to Meinhard Kissich um for because this is a time-sensitive

**Dave Jones:** Kickstarter. Hm, sorry. Um yeah, this was like sent quite I don't even need that. This was sent quite a while ago, but it was like I just wasn't doing mail bags at that time. So, unfortunately, I couldn't uh

**Dave Jones:** couldn't do it. But let's check it out. There's obviously some hot Oh, look at that. Fancy pantsy. And there we go for the you QR code aficionados. And Is there hardware in there? No. Is it I got slice and dice that open. B B

**Dave Jones:** maths. Oh, we got some rulers. Oh, okay. Cool. PCB rulers. I spot a problem right off the bat. Sorry. Let's take a look at them, but they're they're flexible rulers. Min Harder is sending these cheat sheet rulers. And

**Dave Jones:** yeah, they're not PCB. They're made out of a you know, plasticky type thing. Anyway, these are designed to be well, let him say it himself. Designed to be little cheat sheets cheat sheets during exams during final exam. They have all the various formulas on

**Dave Jones:** them. Obviously, in these exams you're like it's an open book exam or something or you're allowed to like bring in a sheet of paper with all the formulas and and calculations and stuff on it. And they're all math related. They're not

**Dave Jones:** really not so much electronics related. So it's all the math math exams. I don't quite understand the B concept with all the um whole like the holes in it. I don't get it. And anyway, the one criticism the zero should start

**Dave Jones:** right at the end so you can do end stop measurements like that. Anyway, Min Harder reached the model's 2400 euro goal. Although I guess that buys you a lot of these. I don't know how much tooling would cost for one of these. Not

**Dave Jones:** a huge amount I'd imagine, but anyway, met the goal. So I'll link it in down below if you want one of these cheat sheet rulers for all you math nerds. That's not me. Sorry. And all my viewers from Ohio formally where Chris Gammell

**Dave Jones:** was from. And in particular Zach Kohler. At least we're not Detroit. Sorry. it's the old I might have to edit in the clip from that. Anyway, Cleveland versus Detroit, it's a internet meme YouTube meme thing. Fun times in Cleveland again. Still

**Dave Jones:** Cleveland. Come on down to Cleveland town, everyone. Under construction since 1868. See the sun almost three times a year. Looks like a Scooby-Doo ghost town. Buy a house for the price of a VCR. It could be worse though, at least we're not

**Dave Jones:** Detroit. We're not Detroit. What have we got? We've got a alarm clock thingy. Does it do anything else? Two minute tear down and one of those Oh, I could use those. Those Velcro straps. Sagan. It's for Sagan. Awesome, he's not here.

**Dave Jones:** But not sure what that is. What is that? Oh. Oh, what are they? Flashing fireflies. We have the American innovative USA alarm clock apparently. This one could allow you to set a different time for every day, which is

**Dave Jones:** rather interesting. Take it away. An expensive piece of rubbish. The Neverlate executive selling point was being Is that what it was called? To be able to set a different time for each day, a feature now covered in smartphones. The knob would tend to slip

**Dave Jones:** and double jump. Battery backup never worked. Audio worked well. Built down to a low price point apparently. Yeah, let's tear it apart. Well, this is rather odd. Like this sits on there like that. Speaker on the bottom, I get it because this sits

**Dave Jones:** off like that to direct the, you know, little like little acousticy kind of box to get that out. But look at that like the sides. Why are the sides like that? I don't entirely get it. Anyway, can this come apart? Yep. Wait. Hello.

**Dave Jones:** What's that? Hello Dave. Someone has pre-torn this apart. What? What is that? I got no idea what that is. But hello Dave. Someone knew at the factory that that's interesting. Check out how they've assembled the LCD on this thing. Look at that. The LCD

**Dave Jones:** module I haven't I don't think I I haven't seen that before. They've obviously designed that LCD controller to like sit in a cutout in the board and then they've just put the pads on the side and then bridge them

**Dave Jones:** over like that. So that's a rather interesting technique to get a low form factor like that rather than have it you know a pin header sticking out and stuff like not that they needed it with all this depth

**Dave Jones:** and everything else. But that's that's rather neat. Anyway, we've got double-sided load on the is that the Yeah, that's the receiver board down there cuz there's our ferrite There's our good old AM ferrite rod and just a single chip AM FM

**Dave Jones:** radio receiver and like Bob's your uncle. Got a down at the bottom there and a 1 W 8 ohm speaker. It's like like yawn. But the engineering sort of neatness and cleverness with the LCD in that cutout kind of ended with these

**Dave Jones:** tiny Look how they've actually gotten these off board wiring little tiny like What are they? Four four five six core wires going over to the top switch contact board over here. That's hideous. Somebody had to hand solder all those. Look at the Look at

**Dave Jones:** the contact on the PCB. Wiper contact, they went to all that effort. I Yeah, it's a weird. And that cabling's just like for production, that's a nightmare. Why would you go with that? Unbelievable. And these things are bike safety flashes

**Dave Jones:** from over 15 years ago and it still works. Do you just bang them like start it. Oh, yeah. There we go. Look at that. Beautiful. I don't know how long do they flash for? Like a minute or something? And Oh, I I guess

**Dave Jones:** the vibration still keeps them going. Eh. Neat. But yeah, after a Wow, what do they you know, couple of coin cells in there? And you know, LR44s or or something like that. I'm not sure like they actually require a a bit of force

**Dave Jones:** to get them going. So, I'm not sure how they keep going on the bike bike. Maybe you know, you stick them on the frame and they did the vibration and might keep them going or something, but All right, interesting. Can't really tear

**Dave Jones:** those down. You'd have to dremel the whole thing apart, I think. And all my viewers in Singapore, we don't get many from Singapore, do we? I love Singapore, it's a good uh probably my favorite Asian stopover on the way cuz

**Dave Jones:** Australia, like it's down on the bottom of the planet or top depending on your perspective. And yeah, uh like we generally need a stopover if we're headed to uh Europe. So, you know, anyway, I've got Oh, sorry. Thank you. Uh no, from Yeah, person

**Dave Jones:** unknown. Um in Singapore. Oh, jeez, this is comprehensive. I'm a guy living in Singapore who wishes to remain anonymous. That's cool. Uh but have been watching your show ever since episode 395. Uh this note is going to be a little bit

**Dave Jones:** long, so read only underlined text if you don't have much time. We have got a black box. It's actually called a black box. Um, and it is black. Winner. Um, and it's like it's one of the Oh, it's a set-top

**Dave Jones:** box. 2 second tear down. This is a pay TV a piracy box. Um, I go figure. I I guess C1 stream box. And I didn't know that you could like just like it looks like a legit product. I mean, it's one of these

**Dave Jones:** little hacked together uh jobbies. You can see the little Wi-Fi module hacked in there and all sorts of stuff. And uh apparently he's ripped some uh parts out of this puppy, but um it connects to the Wi-Fi and downloads

**Dave Jones:** uh the encryption key stored in an off-site server in some undisclosed location. Unbelievable. Uh there you go. So, I don't know. Is anyone still getting pirate cable TV with, you know, um like I just get Netflix. I mean, yeah, I

**Dave Jones:** could probably get it off of Nicks, but it's just so convenient. I don't know. We don't have really Well, we do have cable TV here. We have Foxtel, but I don't think anyone bothers to uh you know, has any The market's not big

**Dave Jones:** enough to sort of hack together some uh box to get you Foxtel, I don't think. And not every home has it anyway. So, yeah. I don't know. Are you pirating your cable TV? Let us know down below anonymously.

**Dave Jones:** But NSA's tracking you anyway, so meh. And our anonymous friend has uh written very comprehensive details of um this box and how it works and stuff like that. So, uh for those playing along at home who want to uh have a read of that,

**Dave Jones:** go for it. Another one from Germany. This one comes from Allsdorf from uh Marcel Hansen. Thank you very much, Marcel. Let's check it out. No description. And it's just a lumpy thing. Oh. What? Why I have a dummy?

**Dave Jones:** Um Oh, you what? This is great. This is great. It's a It's a 50 ohm terminator dummy.

**Dave Jones:** Not a fan of dummies. They're not good for kids developments. I don't like uh They're not good for the mouth development. Their mouth doesn't form uh quite well apparently. So, but that Wow.

**Dave Jones:** A 50 ohm dummy. That's gold. Hi Dave, I'm sure you are familiar with terminators because electrons are shy and afraid of photons. They get scared when they reach the end of an open cable and run right back, the little buggers.

**Dave Jones:** Hence, the terminator was invented to keep the light out of coax cables. Yes, true story. It's on Wikipedia. Uh We have at uh First Advanced Industrial Labs, I love the name of the company. I wish I'd thought of it. Uh proudly

**Dave Jones:** present to the EVblog latest in termination technology. If you are planning to have another child or maybe know a fellow engineer who has a suitable host device, you are welcome to try it out. Thank you very much, Marcel.

**Dave Jones:** Technical specs, impedance is 50 ohms of course, uh 20 dB noise reduction, and uh plus 400% sleep mode duration. Awesome. I just Is there anything better? Look at this. Look at this. It's just fantastic. 50 ohm dummy load.

**Dave Jones:** Thank you very much, Reflower. Flow R, Reflow capital R dot com. Um for what we've got in here. It sounds interesting. Looks like it sounds like there's multiple uh things in here. So, let's check it out.

**Dave Jones:** Oh. Oh, wow. Wow. We've got a kit and a sweet Oh, it's a Yes. Right. Has this been sitting here for a while? I'm not sure. I think I saw this. Um yeah, the reflower Was it a Kickstarter or

**Dave Jones:** something? Uh or it was talked about on the EEVblog forum or something like that. It's a mains in um and a red button on there with a thermal couple and it it's just a um a reflowing plate. So, you stick your

**Dave Jones:** board on the top and um apparently you can reflow your boards. So, I'm not It's not something I can demo on the mailbag. Wait, Dave. I hope you like my reflower project. It is really easy and convenient to use. It

**Dave Jones:** comes with a small test piece. We have everything you need. One screw open teardown. Oh, apparently it's quite easy. And this is the note. Uh yes, it was a a crowdfunding campaign. Apparently, this is the one that's shipped. So, that's the note that uh

**Dave Jones:** ships with it. A few issues and all that sort of stuff. I like that, you know, being honest and uh tell everyone about the uh you know, in issues that come with the shipped product. Anyway, I'll link it in. It's manymaker.com

**Dave Jones:** with a uh hyphen in there. But there it is. There's the reflower. It's just the plate on top. Gets hot. You stick in your mains. I don't know um uh if you have to hook an external thermal couple on. Haven't seen it yet,

**Dave Jones:** but uh presumably it will uh is programmable with a profile. So, you know, it's it's pretty crude. I mean, like all the corners are sharp. You could sort of like cut your like that. I could probably slice If I

**Dave Jones:** put my hand down there, I might be able to slice my hand open like that. So, it really is a uh you know, a sort of a or maybe, you know, a practically prototypey uh type thing, but they have uh shipped

**Dave Jones:** apparently and well, let's crack it open. Have a look. Sure enough, there was one giant screw on the bottom. And ta-da! We're in like Flynn. Oh, I got some real insulation. That's I don't know what sort of insulation that is. Some sort of

**Dave Jones:** fibery fibrous type um insulation. You need that, of course, to isolate cuz that thing's going to get hot. I mean, it's soldering temperature and there's not much doing down there at all. It's neat enough, I guess. It's all

**Dave Jones:** self-contained on one PCB. Mains straight in. It's mains uh fuse down there with with the proper shrouded uh fuse holder on there and uh well, that's about it. And they've got a 3-W uh DC-to-DC brick converter down there. I'm

**Dave Jones:** not sure why they needed a 3-W jobbie. That's actually a lot um cuz the heater is going to be uh mains uh heated, of course. Um so, yeah, I That's a fairly decent size brick. So, I'm not sure why

**Dave Jones:** they needed that sort of level, but it must all be all the smarts of it must be on the bottom of the board. But, it looks like there's like a little uh Wi-Fi modules down in there. Is that one of those uh

**Dave Jones:** ESP uh 8266s? And Lafras has very kindly included the PCB so we don't have to take this puppy apart and uh we should be able to see some Yep, mains isolation there. Look at that. Very nice. No worries whatsoever.

**Dave Jones:** And there's all your control stuff on the uh bottom side and that was going off to the uh Wi-Fi module over Yep, Wi-Fi. There it is over there. And a fan, buzzer, LED, and your uh thermocouple input. So, that's a neat

**Dave Jones:** little board. I like it. And they've included an experimenter's uh kit with some uh PCBs. These are for uh reflow soldering uh practices like the one that's got the thermal pad on the bottom. That's pretty neat. Um and yeah,

**Dave Jones:** we've got the uh well, a stencil, actually. That's probably not it. Maybe that's just a dummy board. I think that's the real Yeah, that's the real board for uh reflowing uh stuff, some paste, and uh thermal couple, and a um and I assume

**Dave Jones:** that's a spreader. Is it? Yep. Uh you really need a plastic like a just a simple uh plastic credit card or something like that does the job better than a fixed metal one like that for a spreader. A plastic card would

**Dave Jones:** have been much better. But yeah, that's a little experiment as kit that either comes with it or you can get separately just to get you started. So, that's interesting. It's not something I can play around with. I should play around

**Dave Jones:** with on the mail bag here. So, I might do a separate video on that. And it it's got a fair way to go to be like a commercial uh quality, you know, a commercial quality product. It's sort of

**Dave Jones:** a bit proto type here at the moment, but you know, I am I'm curious to see how well it works cuz you really um cuz fiberglass is like a thermal insulator. So, you've got to stick that on the

**Dave Jones:** surface. Okay, the surface heats up, and yeah, you might be able to you'll eventually get the heat uh transferring through to your boards, but it's by no means the best way to do it. Um in fact, these generally uh a hot plate like this

**Dave Jones:** under a board would be used as a preheater. So, um yeah, not really for soldering. So, I'm you know, I think it might have to stay there too long uh to get the heat transferred to the pads on the top. You

**Dave Jones:** know, it might be okay if you've got one of these uh you know, thermal pads on the bottom which then can conduct heat through to there, but that's that's like preheater uh type stuff. So, yeah, I don't know how well

**Dave Jones:** this concept's going to work. They've taken basically a preheater concept and tried to make it into a uh you know, a reflow oven replacement, which it's not. I I find it hard to believe it's going to do a you know, as as good a job as a

**Dave Jones:** thermal oven. Just the thermals don't make sense to me, but hey, I haven't tried it yet, so I have to do that in a separate video and I'll link it in down below if you want to check out the

**Dave Jones:** reflower. There was a thread a while back on the EV blog forum on this, I think. Hi to all my Canadian viewers and uh Andrew in particular, no last name. Uh we have a gift. Thank you very much.

**Dave Jones:** So, let's see what we've gotten from Canada. It is a Hi Dave, greetings from Vancouver. I love Vancouver, great city. To this day, I still regret when I was in Vancouver deciding not to go to a Steven Seagal concert.

**Dave Jones:** Concert, not movie, concert. Long story. Anyway, um do not open this on camera. Okay. And we've got a Trezor, the original hardware wallet. Okay, it's a um Oh, okay, it's a it's a Bitcoiny wallet, is it? Trezor. What other What other type

**Dave Jones:** of digital wallet would you have? I'm not sure. Hardware wallet, doesn't say anything about Bitcoin or anything like that, but uh usually that's what the hardware wallets are for, for storing your Ethereum or your Bitcoin or your 10 million other bloody altcoins. And

**Dave Jones:** sure enough, this is a Trezor hardware crypto Bitcoin wallet um with a little LCD designed to securely store your crypto uh currency. And the letter, Hi Dave, I'm in Vancouver, more on the IT side. So, how it works is the private

**Dave Jones:** keys never leave Trezor and the device will show the recipient's address directly on display, so you can be sure you're sending the funds to where they want to go. Think of it as a drastically overgrown one-time password token, which

**Dave Jones:** adds an unhackable something you have, something you know. Um it makes them a high-value target, no kidding. Um so, he wants the insight into the overall build quality and durability of devices well of its tamper resistance and tamper

**Dave Jones:** evidence stuff. And yes, um I have read this as well. Someone's performed a power line monitoring attack and they were on this, an early version of this, and they were able to retrieve the private key from it, but it is it has

**Dave Jones:** since been fixed uh like 2 years ago, uh 2015 I believe that was uh fixed. So, that was a long time ago. And yes, I did not open the other letter on camera, which says do not open this on camera.

**Dave Jones:** And I've opened it and this is why I can't do a teardown right now. There's something in the additional in that envelope that uh yeah, it's just I can't tell you about and I won't be doing a teardown of this right now, but possibly

**Dave Jones:** in the future, we'll see. Sorry, secret squirrel stuff. That crazy Aussie bloke, that's me. Um let's open it up. Uh thank you very much, Bond and Broon. I I can't pronounce uh let us NATO.nl. Um Netherlands, isn't it? NL, this is

**Dave Jones:** going to be I don't know. It's kind of wrapped in electrical tape, is it?

**Dave Jones:** Got it. Wow, it's a cheap ass multimeter. It's already broken. Oh dear. Oh, look it comes on. 2-second teardown.

**Dave Jones:** Do I have to? At least this one has a ceramic fuse over there for the 10 amp range. Uh like, you know, whatever. Hi to all my Spanish viewers, in particular Alberto Piganti. Good on you, Alberto. Uh we don't get too many

**Dave Jones:** from Spain, although Spain probably punches above its weight in mailbag, possibly. I don't know. Oh, but Spain's a big country, isn't it? I haven't been to Spain. Let's have a quick squeeze. What do we got? We have something in a black felt

**Dave Jones:** Oh, I'm sensing retro. Craig. We haven't ever had a Craig cal- It's a No. It's a learn learn thing. It might be one of those um the Craig M100. It could be one of those uh language translator things. Linguistico.

**Dave Jones:** Linguistico. Yep, I was right. And we've got a big What is this? It's a book. ABC Basic Connec- Oh, Alberto. It's Alberto's book. ABC Basic Connections. Woohoo! Hey. Ah, it's It's a wrap for our protection. Let's have a quick squeeze. Alberto, is

**Dave Jones:** this like a Kickstarter? Awesome. Hi Dave, I'm Alberto. Uh you probably remember me from pinouts.on uh pighigh. piggy. pighigh.xxx.com. That sounds legit. Um I'll link it in down below. It is legit, trust me. Um it's safe for work. I'm super excited

**Dave Jones:** now that I'm running a Kickstarter campaign for my latest book, ABC Basic Connections. Send you a pre-release copies. Tell me what you think. I hope you love it. More information, abcthebook.com. And unfortunately, it's already ended on Indiegogo, but raised 115,000

**Dave Jones:** euros, double the target for this Basic Connections. And it's beautiful. Ring binder, love it. And e-reader as well. You don't get an e-reader anymore, do you? It's basically just information on Arduino and stuff like that. So, here's all the different

**Dave Jones:** pinouts and things, which I I believe a lot of, maybe all of them, are available on the website, but this is in book form. And so, we're just showing, you know, schematic symbols and stuff like that. We've got some Ohm's law stuff,

**Dave Jones:** Ohm's law triangles. We've got the resistor stuff. It's beautiful, beautiful quality. I love the artwork and everything in this. It's just absolutely fantastic. Now, this doesn't have the Creative Commons on it. The ones I saw on the website actually have

**Dave Jones:** Creative Commons. So, anyway, this is how to hook up all sorts of stuff to Arduino. This is absolutely brilliant. I like I can like the graphic layout of this. Imagine how long this took. It's absolutely stunning. I love it. Awesome work. And

**Dave Jones:** it Yeah, I can see why it actually Warning, Wil Robinson. Why it got 115,000 euro back. This is a lovely reference resource. You know, sure, yeah, you can just do it as a PDF, but it it's not the same as having this.

**Dave Jones:** And look at this. Oh, foldout porn. Oh, look at this. Centerfolds. Oh, yeah. This is This is fantastic. Anyway, if you are dealing with Arduinos, you're a beginner, and you want a nice reference book for hooking up stuff,

**Dave Jones:** check it out. Do yourself a favor. Hello. Buongiorno. Hands up if you had one of these. I can type that in and go hands up if you have one of these. A Craig M100. Of course any smartphone can do the

**Dave Jones:** translation I can even probably you know listen to the person's voice can't it and then just automatically tell you what they said. I DIFFERENT WORLD. WOW, LOOK HOW OLD SCHOOL THIS puppy is. 1979.

**Dave Jones:** I kid you not. Wow, what's an SL 9200 44th week 79 made in Singapore. A lot of chips were made in Singapore back in the day. Wow, look at that little budge board over there. Is that a is that a

**Dave Jones:** little uh convert is it a No, that's an inductor is it? So that's a little switching No, switching what? Thought some sort of switching converter. Anyway, look at the finest budge board over here. Vertical resistors. Fantastic. Thank you very

**Dave Jones:** much. So it's basically just a processor a vacuum is it Yeah, I presume vacuum fluorescent display down in there and the cartridge ROMs which you can There you go. That's the Italian ROM. Wow, copyright 1980. Wow. So there it is.

**Dave Jones:** Oh, look at that. Beautiful. So yeah, it's just a like it doesn't it just doesn't do anything fancy. It's just you typing the word and then maps it to a ROM entry and then displays the mapped word. But anyway, there you go. You can

**Dave Jones:** put three different languages inside this thing. This would have been the ducks guts back in the day. This would have been like black magic technology back then. Oh, I can't get enough of the nipple. You know, I love it.

**Dave Jones:** Well, I'm curious to know now. I can't read the Well, I guess I could just translate the manual, couldn't I using one of my newfangled smartphone thingies or Googly or whatever it is, but it does have like a learn I presume that's that

**Dave Jones:** learn button on the front, but this is like a ROM-based thing. So, like I wouldn't expect it to do anything like algorithmically fancy. I expect it just to map words in one language to another and that's it based on the ROM.

**Dave Jones:** Uh you know, entering content they probably sort putting them in alphabetical order in the ROM or whatever and then translate them over, but I don't know. Um Hmm, maybe it does a little bit more, but I wouldn't have thought so. And

**Dave Jones:** unfortunately, it doesn't work. The LED comes on, but yeah, it's nobody's home. So, that's an absolutely fascinating little module there how they've bent the pins over on just a standard ROM, put a lovely little label on there, and made

**Dave Jones:** their own little sort of, you know, like little plug-in thing with a handle. That's It's really rather clever. I like it. So, anyway, thanks for everyone who sent in something for today's mailbag and sorry if I haven't gotten around to

**Dave Jones:** yours yet. I will endeavor to do it next time. Anyway, if you like mailbag, please give it a big thumbs up. Catch you next time.
