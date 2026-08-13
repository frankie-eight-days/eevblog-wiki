---
video_id: oFTPTmZ7pDU
title: EEVblog #960 - Mystery Merry Mailbag Teardown
url: https://www.youtube.com/watch?v=oFTPTmZ7pDU
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 15, "2": 30, "3": 55, "4": 83, "5": 107, "6": 139, "7": 155, "8": 175, "9": 195, "10": 219, "11": 239, "12": 263, "13": 279, "14": 299, "15": 319, "16": 335, "17": 347, "18": 367, "19": 383, "20": 399, "21": 411, "22": 423, "23": 451, "24": 463, "25": 483, "26": 507, "27": 527, "28": 543, "29": 563, "30": 583, "31": 607, "32": 623, "33": 651, "34": 671, "35": 691, "36": 707, "37": 727, "38": 747, "39": 767, "40": 787, "41": 803, "42": 819, "43": 839, "44": 855, "45": 879, "46": 895, "47": 915, "48": 935, "49": 955, "50": 971, "51": 987, "52": 1003, "53": 1027, "54": 1051, "55": 1075, "56": 1099, "57": 1119, "58": 1143, "59": 1167, "60": 1187, "61": 1203, "62": 1231, "63": 1247, "64": 1267, "65": 1283, "66": 1295, "67": 1315, "68": 1327, "69": 1343, "70": 1363, "71": 1379}
---

**Dave Jones:** Hi! I thought I'd just do one last mailbag item for the year, because this one just turned up and it was so big, I had to open it. And it is Christmas Eve, so, hey, why not? And it does actually contain one of my favourite items.

**Dave Jones:** I don't know exactly what, but one of my favourite categories of items. So thank you very much, Matthew Trenish, for sending this one in. It costs a lot. He's from New York, I believe. And it costs a lot to send heavy stuff like this, so I really appreciate it.

**Dave Jones:** Thank you very much. And to everyone who's sent in a mailbag this year. So let's find out what's inside this puppy. Hang on. It's not particularly heavy, but it is certainly big. And there's a lot of air in here, so let's... here we go.

**Dave Jones:** We've got lots of padded stuff. Lots of air. Sorry, can't see this. Actually, it's probably not that big. Let's have a look. We have a note. Don't want to spoil it for myself. And it comes in a case. Ta-da! Is it on the front?

**Dave Jones:** You've probably seen it before me. No, there's no label in. No label in. It's just a nondescript case. Let's have a look. Ooh! I'm looking on the screen here. I haven't seen it. You probably know more than me. What is it? IBM! IBM what?

**Dave Jones:** What? It's actually in the case. Wow! Look at this. It's like 8-inch floppy disks. What? Cleaning fluid? It's obviously an IBM disk drive in a box. What the? That's not what was written on the case. In the box and the documents it said

**Dave Jones:** brush. It said test equipment. Oh! And I got a vintage computer. What the? What on earth? Wow! Unload diskette when not in use. Do not touch diskette when running. It's almost like the disk couldn't fit in there. What does it? Disk slot on the top.

**Dave Jones:** What is this thing? I'm going to have to read the note. Hi Dave. Greetings from Pookercy. Pookercy. Suburb somewhere. I've been a long time viewer and a big fan and I started watching back in the college days studying and have continued to watch since I graduated 5 years ago.

**Dave Jones:** Thank you very much. His first job out of college was with IBM in Pookercy. Pookercy. No. Sorry. I can't pronounce it. I've since quit and moved on to better opportunities. Back then I worked for IBM. Coworkers made a frequent habit of checking the electronic recycling bins.

**Dave Jones:** Ah, beauty. They are mainframe diagnostic devices. Wow! So apparently it's just more than a floppy device. It's some sort of mainframe diagnostic device. Um, spoiler for the teardown. I don't want to read a spoiler for the teardown. Goodness gracious me. Um, thank you very much.

**Dave Jones:** This is an interesting bit of kit. Oh, probably a 5 minute teardown. Let's go. And well, this is a bit of test equipment. I just foolishly assumed that it would be some sort of, you know, familiar bit of bench test gear. Electronics test gear.

**Dave Jones:** But it's not. It's a specific bit of test gear for, in this case, IBM mainframes we believe. Hey, I shouldn't have assumed such a thing. I spent many years designing countless production test gear and special purpose test gear for, you know, some products that only, you know, only make 10 of them.

**Dave Jones:** But they needed a bit of special purpose test gear to do it. Um, and this is very niche sort of thing. I mean, you know, how many of these IBM mainframes did they sell? That's interesting. Is that like a lead? That's a lead.

**Dave Jones:** Could that be a lead character display? Wow, I don't know. But anyway, the keypad's really interesting. And yeah, this is a specific bit of kit. So let's take a look at it. First of all, we've got a whole bunch of instructions under there.

**Dave Jones:** And setup procedure, disconnect procedure, keyboard key definitions, and it's got yes, no keys, failure procedures, all that sort of stuff. Neat. Anyway, we didn't actually get the disks. All we got is a couple of empty pouches. Bummer. But not that it's going to work or do anything useful anyway.

**Dave Jones:** Now the first interesting thing to note is the floppy drive is on the top here, and obviously the floppy doesn't go all the way into this thing. Because if you have a look here, and here's the floppy drive pouch, and it'd come out to here, it would

**Dave Jones:** you know, it'd stick out a bit. Like there's no motorized thing that takes it in or anything, so it's going to stick out a little bit. But of course the head's going to be in there on the side, and that's just fine. You know, do not touch the disk when running,

**Dave Jones:** because then you can cause friction inside the thing and yeah, no, it upsets the Apple Car. And I have no idea what R-loop, S-loop, parallel IO, IPL reset, whatever that is. I've got no idea what this thing actually does, but hey, it's a specialized bit of test gear

**Dave Jones:** unless you had the full instructions for it, or you were familiar with using these things, you wouldn't have a clue. But there would have been some you know, design team of engineers that actually designed and built this thing. They put a lot of work into it.

**Dave Jones:** It's going to have software and everything else in it, because it is basically a little computer, a diagnostic type computer that plugs in and does whatever tests it needs to do into whatever mainframe-y type thing it plugs into. So I'll disconnect all this.

**Dave Jones:** It's obviously designed to go into this portable carry case designed for field service techs or something like that to go into the field and repair IBM mainframe stuff. So I'll take it all out and we'll have a squeeze inside. Actually I'm going to violate my rule.

**Dave Jones:** I'm going to power it up, because I don't want to take it all apart. I haven't got time to take it all apart and put it back together. Today it's Christmas Eve, I've got to get out of here. So I'll power it up first

**Dave Jones:** and see if it does anything. It's 110 volts, so here we go, fingers crossed. There's a fan. I can hear the drive doing something. We've got some LEDs. Hello? Enter. Nope. I love how it's got yes, no buttons. Backwards, return, forward. No. So, it powers

**Dave Jones:** up. No magic smokes escaping. But yeah, nothing. Oh, is that a big... no, I thought that was a heatsink. Yeah, that could be it. Yeah, that's a big heatsink on the back of that, I think. But nothing on the display here, so that's a bit of a bummer.

**Dave Jones:** Ah, well. For those playing along at home, it's the 901X, is it? Here's our first peek inside this puppy. We can see the floppy drive mechanism here, and so that's the entire top half. Oops. Looks like the belt has seen better days. Well, no, the belt's actually intact.

**Dave Jones:** It's just come off. Huge big flywheel there for it, but nice neat cabling all tied up. Somebody's taken pride in that. Definitely even tagged all the individual wires. Beautiful. So here's the entire floppy mechanism we've got out. The board's really interesting. I'll show you that in a second.

**Dave Jones:** Absolutely fascinating, but that's... oh, there we go. Is that a head? Well, that'd be the motor drive. The power stuff there, yep. There's our motor soldered directly under the board, is it? Interesting. Anyway, up here it looks like we've got some track sensors there.

**Dave Jones:** Of course, we've got the motor in here that drives the head back and forth. We've got our worm drive in there, and there is our head. There we go. Is that a single or double-sided jobby? And there's the other side, so double-sided head for this puppy.

**Dave Jones:** Check out the PCB! And yes, it is a PCB. It looks like a matrix board with the square pads on there at first glance. But look, you can actually see all the etched traces in there. So this must have been like an internal IBM thing of how they did, you know,

**Dave Jones:** maybe prototypes or short-run boards or something like that. They just did as a matrix layout. I mean, half those pads aren't connected, yet they've left them in there. It's, like, bizarre. Did they have some rapid prototyping system that allowed them to make boards like this easily?

**Dave Jones:** Otherwise, you know, if you're going to etch a board and do it, you know, why not just etch a proper board? Why use a system like this? No, they wouldn't have placed them down afterwards, would they? No, it's weird. I... Maybe I might have seen this somewhere once, but I can't...

**Dave Jones:** It kind of rings a bell, but I can't remember. If anyone knows if this particular technique has a name, if it was specific to IBM or whatnot, then please let us know. But that's very, very unusual. Anyway, we have some date codes in here.

**Dave Jones:** 87th... no? 8782. 82nd week, 87. That doesn't sound right. Hmm. Anyway, look at these cans. Metal cans. IBM-specific part numbers. Are they some custom silicon? Hang on. And there's the back pattern on that. Look! Completely fascinating! Wow! Oh, look at all the right angles.

**Dave Jones:** All the electrons are going to fly off the bends there. We've got ourselves a little mod wire down in there, but yeah, that's really interesting that they've used that technique. Wow. I mean, the annoying part about, you know, using a technique like this is

**Dave Jones:** you've got bugger all routing space. Yeah, you can get, you know, two tracers down between pads there, but geez, as a PCB layout engineer, I wouldn't want to have that limitation. Horrible. That looks like a real date code. There you go. National Semiconductor, second week, 85.

**Dave Jones:** So, you know, this would have been for mainframes designed in the 70s, I don't know, but they could have been manufacturing these still. I mean, they would have only manufactured these probably in the dozens or, you know, hundreds. How many of these things in service

**Dave Jones:** text did they go out there have fixing these mainframes? It wouldn't be, I wouldn't suspect it'd be in the thousands. And you know I had to decap that big baby. There it is! It looks like we've got like a, maybe a ceramic... It's not a hybrid, because there's no other, you know, hybrid

**Dave Jones:** laser trim resistors or any other components on there. So it's just basically a mounting board for this little tiny chip they've got in the middle there. Look at the pitch on that. It's tiny. Is that like an early BGA thing? I don't know.

**Dave Jones:** I'm not sure if we can even get under there to have a look, but yeah, that is that is cute, isn't it? Wow, gone to a lot of trouble. This is obviously the part of the floppy drive controller, but you know, just the engineers that worked on this module alone

**Dave Jones:** let alone the test gear that we've got here, this customised test gear, which wouldn't have been, you know not a consumer item or whatever. Whole teams worked on this sort of stuff. Fantastic. And I'll tell you what, is this a multi-layer board? They've got a big fat ground plane

**Dave Jones:** running through the centre of that. Wow! And yep, they were really fond of this alright. It extends right through the main board, although this one here is different. It doesn't have that ground plane in the middle. You can see the difference between the dark and the

**Dave Jones:** light side of the force there. But yeah that's like, they're obsessed with this. I've got to find out more info. What is it? So I asked on Twitter if anyone knew what this was, and Bruhaha says I don't know the name, but IBM used it a lot.

**Dave Jones:** Yep. And Mark Morin says it's LGA, stands for Linear Grid Array. I actually checked, and it's I believe it could be Land Grid Array. So that's the name for that sort of technique. Land Grid Array. There you go. I guess we can Google that one.

**Dave Jones:** Here we go, we've got some more custom IBM goodness in there. Surely they have not designed all this custom silicon just for this test jig. So they're probably repurposing them, maybe from the mainframes themselves. Who knows the logic from those? I don't know.

**Dave Jones:** The processor? I don't know. Let's, ugh. Hey, hello. Hello, we've got ourselves a real in quote marks PCB. Look at that. Once again, fond of right angles. Oh, all this auto-router stuff. And you can tell it's auto-router rubbish because look at this. The trace comes here, right angle, up to the middle

**Dave Jones:** of that pin, and then in the middle of the line of those, and then over. No PCB designer in their right mind would do that. Like even a beginner would not do that. You would know, you know, look, even if you're doing right angles, go all the way over here, and then this straight in.

**Dave Jones:** Like, it's just, yeah, it's dumb. This thing's auto-router. Oh wow. And it's interesting that this just pops off like that. I mean, there was nothing holding that, the only thing holding it in was the screws and the force. Star Wars again. And yeah, these just did not

**Dave Jones:** can I just, yep, I can just whip them out. Look at that. Is that our, no, we've got lots of them. I don't know where or what the processor is. It's a combination of a whole bunch of stuff. But anyway, I assume extremely similar under, oh, that one's high.

**Dave Jones:** It's a double. It's got a piggyback. Look at that. Advanced technology. And all the chips on here, look, you know, they're made by Motorola, National Semiconductor, but they've got almost certainly IBM part numbers. There we go, 19th week, 82. But yeah, these would all be custom IBM part numbers there.

**Dave Jones:** They would have their own extensive bill of materials system, so the designers of this would have gone, well, we have to use these. They would have looked up the IBM catalogue of parts, and you could probably only use the pre- authorised catalogue of IBM parts that each have the individual part number

**Dave Jones:** and that have their own internal documents which map the IBM part number against the actual. I mean, this could be, you know, a 74LS245 or something like that, you know, bus transceiver or some other thing. You know, it could just be regular jelly bean logic, but hey,

**Dave Jones:** IBM are so big, and so bureaucratic, they have their own part numbering system, and they get them, you know, they'd buy 100,000 chips at a time or something, and get them all silkscreen with their own custom numbers on them. And these are obviously resistor

**Dave Jones:** pull-up packs here, but hmm, what's that puppy? I don't know. Does anyone play along at home? There's one thing you don't see on here, is bypass capacitors. Where are they? Well, maybe that's what some of these puppies are. Some would be pull-ups, some would be maybe bypass capacitors

**Dave Jones:** in a SIP, a single-in-line package perhaps. Hmm. I broke a couple of these off. Let's see if we can probe that. I'm getting something. Yeah, 3k. There you go. Here's a resistor array. And this puppy here is most likely capacitor array. Is it?

**Dave Jones:** No! No. No, that's 170 ohms. Thank you, 89 ohms. Wow. Okay, that's interesting. So where's all the bypass caps on here? Low enough they didn't need it. So anyway, these are our 3 boards. Board number 2, which is mostly big chippies. This one's a little bit more discreet-y.

**Dave Jones:** There you go. Not sure what's going on there, but they're the 3 boards that have to have that's the processor system. Hmm. Ah! They couldn't even route this properly. Look, they're going up between the pins and then right angle. What the? What? Unbelievable.

**Dave Jones:** And here's inside the keyboard. Wow. They've got some sponge on here, and some tactile dome. The keys all sat on top of there, so they're little tactile domes. We've got our matrix-type board construction again. We've got a big foam pad under there, so we've got all the circuitry for that.

**Dave Jones:** But look at that! That is sex on a stick. Wow, look at that display! Wow, this looks like some sort of weird alien technology that crashed at Roswell. And like, brilliant! Wow. These are presumably character-based displays. I need to get a macro lens on these.

**Dave Jones:** Wow, look at this! In a DIP package, these are 4 character displays. We've got 1, 2, 3, and 4. And they're 7 high by 5 digits. Wow. Obviously, look, so you can see the bond wires going between these, so obviously we've got individual column drivers

**Dave Jones:** like that, and then this would be your row driver, I see here. Remarkable. And there's some serious heat dissipation going on there. Look at that monster heat sink! I've done some random poking around with the diode test to hear it. I can't get anything to light up, so

**Dave Jones:** yeah, not sure what the deal is. But hold onto your hat, using a super-secret multimeter that has a 15 volt diode test range. We don't need the 15 volts, it's actually a 1.8 volt drop, but it gives us more current capability. Here I'm measuring 1.85 volts drop.

**Dave Jones:** Bingo! I can light those puppies up. It's a little LED display. Isn't that cute? Wow! LED dot matrix display. Brilliant! So thank you very much, Matthew, for sending this puppy in. This was incredibly interesting. Like, all this custom IBM chip tech, the matrix layout

**Dave Jones:** PCBs, the old 8-inch floppy, and wow! These beautiful little LED dot matrix displays. If anyone's got any data on these things, I mean, easy to find the pinout now, you just hook it up and, you know, fairly trivial. And you could drive I could, you know, use this as a display driver.

**Dave Jones:** That'd be a cool project if I've got time to actually hook up and drive this thing multiplexed, obviously. But wouldn't that be awesome to get that puppy up and running? Oh yeah! So there's an awful lot of engineering that just goes into, you know, sort of a low

**Dave Jones:** volume, probably in the hundreds or something like that at best I'd be guessing. A custom bit of test jig, it might be for testing floppy drives in the field or something, not entirely sure, but something to do with IBM mainframes, so the service techs

**Dave Jones:** take these into the field and, you know, fiddle a few things and repair your mainframe for you. But, you know, there's a lot of engineering that goes into this, all the custom firmware, the processing, everything else you know, a team worked on laying out all these boards.

**Dave Jones:** As I said, they probably didn't roll custom silicon for this, I'd be surprised if they did. You know, it probably wouldn't have been worth it, but hey, IBM be an IBM, who knows? But if anyone's got any info, detailed info at all on these things, they worked at

**Dave Jones:** IBM, they know what this thing is, somebody out there's got to know, please leave it in the comments. So thank you very much Matthew, that was awesome, if you liked that video please give it a big thumbs up, because that helps a lot

**Dave Jones:** these days with the engagement and all that YouTube crap going on and stuff like that, and it's I'm off to a Christmas party, it's Christmas Eve here, I just got an hour or two to drop by the lab, so I hope you like this video, and

**Dave Jones:** by the way, I have Batterizers. Batterizer update, if you haven't been following the EEVblog forum, they did deliver, it is somebody sent them, somebody sent my ones, haven't been delivered yet, but somebody sent them to me, they are on a DHL truck but I probably won't get those until after, well I obviously won't get

**Dave Jones:** them until after Christmas, hopefully, and we can run some tests It's looking pretty, go check out the EEVblog, the 300 page EEVblog forum, it's absolutely fascinating on that, everyone's, a few people have got them and they're testing them and yeah, told you so.

**Dave Jones:** Catch you next time. you
