---
video_id: 9-wzPTiLz5c
title: EEVblog #339 - Cypres Parachute AAD Teardown
url: https://www.youtube.com/watch?v=9-wzPTiLz5c
source: youtube-asr
timestamps: {"0": 0, "1": 26, "2": 41, "3": 58, "4": 76, "5": 89, "6": 105, "7": 116, "8": 127, "9": 137, "10": 152, "11": 163, "12": 176, "13": 195, "14": 210, "15": 225, "16": 241, "17": 257, "18": 271, "19": 285, "20": 297, "21": 313, "22": 333, "23": 346, "24": 368, "25": 397, "26": 413, "27": 424, "28": 442, "29": 455, "30": 484, "31": 503, "32": 524, "33": 540, "34": 551, "35": 561, "36": 577, "37": 594, "38": 611, "39": 628, "40": 647, "41": 675, "42": 686, "43": 704, "44": 725, "45": 739, "46": 761, "47": 775, "48": 787, "49": 800, "50": 816, "51": 827, "52": 849, "53": 862, "54": 879, "55": 894, "56": 910, "57": 921, "58": 933, "59": 946, "60": 969, "61": 981, "62": 999, "63": 1015, "64": 1028, "65": 1048, "66": 1061, "67": 1073, "68": 1088, "69": 1112, "70": 1132, "71": 1148, "72": 1164, "73": 1187, "74": 1209, "75": 1232, "76": 1245, "77": 1265, "78": 1283, "79": 1298, "80": 1309, "81": 1320, "82": 1330, "83": 1351, "84": 1362, "85": 1378, "86": 1393, "87": 1406, "88": 1423, "89": 1436, "90": 1452, "91": 1462}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. You've seen this on the mailbag in a previous video. It's the Cypress Parachute Emergency Release System. So, you know, if you're parachuting and you get knocked out, or you're just too busy enjoying the view, and you forget to pull your chute, if you get to 700 ft or so, if you're going fast enough, this thing kicks in, blows a pyrotechnic charge through a cord, and boom,

**Dave Jones:** releases your parachute. And this is quite should be quite an interesting device. And I thought we'd tear it down. It could actually be a little bit difficult, but I expect there to be a whole bunch of interesting stuff in here.

**Dave Jones:** At least it's well-engineered, cuz this thing's got a 10-year lifetime, uh pretty much. You change the battery every couple of years. 10-year lifetime, and it should be built to, you know, an excellent standard in terms of shock, vibration, you know, moisture ingress, all sorts of stuff.

**Dave Jones:** So, could be really interesting. Let's check it out. And thanks to Steven in Carlsbad, California, who sent this in again. And here's the pyrotechnic charge, by the way. A lot of people said I'd be quite careful with this, cuz it could go off with quite a hell of a bang.

**Dave Jones:** And it's one-time use only. It's got a little cutter in there. So, presumably, when you apply a voltage on there, it's got a neat little sort of like a funo type connect the system here.

**Dave Jones:** And hopefully, well, let's plug it in. And no, it's not going to go bang, honest. But that looks quite robust and quite rigid. But you can actually disconnect that, so there's no um it does still have the battery inside, so there's no risk of it uh going off now.

**Dave Jones:** But little cutter in there, pyrotechnic charge uh fires the blade up through there, which you put the your nylon cord through, and it slices it. And uh that releases your reserve parachute.

**Dave Jones:** So, let's have a look at the unit itself and uh it looks like it's got a battery uh compartment on the top here. You're supposed to I think it's uh Where does it say?

**Dave Jones:** It's made in Germany, of course, and uh it was checked in 2007. Um and it did have a battery change sticker on it. There it is. Last battery change uh 10th month '09.

**Dave Jones:** So, you know, and it still works. Um so, presumably, you only have to change the battery every couple of years. You set it once, basically, at the start of the day before you go parachuting, you turn the thing on, and it just sits there waiting, waiting, waiting.

**Dave Jones:** There is a should be some sort of um sensor that senses the air pressure and uh and, you know, your rate of fall. Maybe there's an accelerometer inside or something like that.

**Dave Jones:** And uh if you're going fast enough at a low enough altitude, under 700 ft, and you're going above a certain speed, bang, it ignites the pyrotechnic charge. So, let's open this thing up and take a look.

**Dave Jones:** It's got a battery in here. Probably a lithium, of course, because it's got a This thing's got to work over temperature extremes. It's waterproof, so I'd expect it to be water sealed or hermetically sealed, the electronics anyway.

**Dave Jones:** Um so, it could be Hey, there we go. Yep, primary lithium batteries. That's uh exactly uh Germany German I'm I'm assuming they'd be lithium. I'm pretty darn sure they would be.

**Dave Jones:** And look, there's some sort of sensor in there. Is that a uh a uh thermo couple or something measuring the battery temperature? I'm not sure what's going on there, but that's what I exactly what I would have expected.

**Dave Jones:** Um same with like our GPS units and things like that that are designed to activate once and then be used long-term. They've got lithium primary batteries in them. So, yeah yeah, there we go.

**Dave Jones:** Okay. So, oh, okay, that's interesting. Check that out. There's the There's the battery connector and you Yeah, okay. So, you slide that in. Yep, that goes in there like that and there too Well, they're actually Cyprus branded.

**Dave Jones:** Um Where are we? AirTech safety system. So, they've actually had them made for them. Doesn't actually say cuz you know, it's There it is. There's the little you know, matching symbol.

**Dave Jones:** They've got it specifically branded batteries. It looks like we have a fuse there in series with the batteries and up here, this is got to be I wouldn't know.

**Dave Jones:** There we go. It's a cap. There you go. So much for a thermal couple, it's an axial capacitor. Go figure. Why have they That is bizarre. Why have they put an axial capacitor in there?

**Dave Jones:** What is that? Uh it's a 10-V axial cap. Can't get the reading on there. But yeah. That's weird. There you go. Anyway, that's it and it looks like it is sealed around there.

**Dave Jones:** I see uh some silicone sealant around that. So, they've completely Uh yeah, it's hermetically sealed. You can see it. See it around here. It's actually been sealed. So, this is going to require some percussive maintenance to get apart, I suspect.

**Dave Jones:** We'll measure the battery here. It should be two lithium primaries in series. Bam, there we go. 7.3 V. We have a warning here. Do not remove seal. Okay. I won't remove the seal.

**Dave Jones:** I'll just break it. Tada! Warranty void. And this This is weird. This sort of This is where the This is the connector for the pyrotechnic charge and for some reason it's like got a separate little separate little compartment here.

**Dave Jones:** So, let me try and wiggle this thing off. It's rather unusual. Well, that's rather strange. It's a four-way connector there with two wires and there's going into just this little backshell thing here with a silicone adhesive on the wires there for some strain relief, I'm assuming.

**Dave Jones:** There's some surface mount couple of surface mount caps in there. So, they're probably to uh uh you know, uh keep out any uh uh noise or possibly uh ESD or something like that from I don't know, setting off the pyrotechnic charge perhaps.

**Dave Jones:** Um and it's all shielded, of course. There's a shielding wire in there and it's all Yeah, why they've gone to sort of that trouble, um it it beats me.

**Dave Jones:** And it is a shield uh uh fully shielded case here. Of course, you know, you wouldn't want to um you wouldn't want it to be set off by somebody's you know, radio or you know, something like that or you know, if they've got in-ear uh radio talking to each other or something else.

**Dave Jones:** Um you certainly wouldn't want the thing to go bang on you. That would ruin your day. So, it's it's it's weird. It's Yeah, it's a metal can, some sort of metal shielded can like foil shielded, I think.

**Dave Jones:** Yeah. Looks like it's foil shielded with a plastic over the top. So, we're going to have to might even have to get out the Dremel maybe. Mhm, I love the smell of Dremeled plastic in the afternoon.

**Dave Jones:** Ah, wonderful. F for fail, perhaps? I don't know. Um yeah, uh the uh plastic uh popped off there and we're left with our metal shielded can. Ta-da! So, looks like we're going to have to get into this sucker as well.

**Dave Jones:** Ah, man. Rather interesting here, this looks to be like a flap that lifts up. So, I'm going to desolder that. That pops off off real easy. There we go.

**Dave Jones:** Ta-da! Hey, look at that. We have some configuration jumpers. And those jumpers would of course uh you know, let the manufacturer this thing sh- completely shield it and then uh presumably um uh do configuration afterwards.

**Dave Jones:** I don't know what type of uh configuration, maybe it's the uh you know, the uh level that it goes off at or something like that at you know, they maybe they have different uh models.

**Dave Jones:** Uh yeah, actually I think they do. They have different models that go off um at different levels, you know, based if you got uh like a single jumper or a tandem jumper or a student jumper or whatever.

**Dave Jones:** So, um no pun intended, they change the jumper switch based on the jumper. Now, we could try and desolder this all nicely, but really I think we're better off just prying and then cutting the thing open.

**Dave Jones:** Hey. Oh, look at that. Potting compound. What? So, yeah, I mean, you can just cut these things open. I mean, there's no um Don't use your good uh side cutters, by the way.

**Dave Jones:** Use your cheap 100 ones to do this, but uh yeah, we have potted electronics in there. There it is. Boing. Yeah, it's Ah, oh, hang on. No. Hang on.

**Dave Jones:** Hey, no. It's just like an outer uh an outer layer of potting or something. Anyway, let's open finish this off cracking it open and see what we've got. And I'm starting to see pressure sensor.

**Dave Jones:** There There it is. Classic uh shape uh classic style of pressure sensor. become clearer once we open this thing. And here it is, minus its metal can, a one big sticky gooey mess of uh easy entry potting compound.

**Dave Jones:** It's not solid uh potting compound, but it's this really It's called uh re-enterable uh potting compound. It basically um I've used this stuff before, and it's really neat because you can actually uh seal stuff, but then afterwards uh after it's sealed, you can you can penetrate it with a screwdriver, and you can get in there, and you can adjust pots and things like that, and then pull it back

**Dave Jones:** out, and it'll reseal itself automatically. So, that's why it's called re-enterable cuz you can re-enter it, and then it self-seals. That was Gee, a long time ago I used this stuff, but it's really neat.

**Dave Jones:** It really is neat stuff, and they've put this Mylar wrap around the Oh, man. How gooey and ugh That is That's really Yeah, this is just as I remember this stuff.

**Dave Jones:** Really sticky. So, they've put these uh like a Mylar type sheets or whatever they are capped on or whatever on between the um between the circuitry and the the boards and the metal can so that the metal can't short out the electronics.

**Dave Jones:** So, if it gets crushed or anything like that, it's still going to survive and not ugh not short Oh, man. This is yeah. Yeah. This is horrible as I remember.

**Dave Jones:** Terrible stuff. Terrible, terrible, terrible. But, so that's in there. That's all protected by that and then they've gunked it all up. This is a real fascinating uh They've gone to a bit more trouble than I had envisaged.

**Dave Jones:** This is great. It's like pulling, you know, cobwebs off something. It's uh So, we've got one main PLCC device here and another sock Oh, man. This is going to take forever.

**Dave Jones:** Yucko. There's our circuit. We've got a real-time clock. Crystal 32 kHz watch crystal there. The main oscillator The main crystal there for the oscillator for whatever that device is.

**Dave Jones:** It tell There's the pressure sensor. It's the classic uh a port type there and they've just used, you know, an off-the-shelf uh one. You can see why it's um how it's got that uh ridge on there.

**Dave Jones:** It's designed to have like a tube go over it. Uh so They've Oh, man. This is great. Oh. Hours of fun and enjoyment this re-enterable potting compound. I'm telling you, get some.

**Dave Jones:** It's brilliant. Uh I can't remember like the brand of stuff we used to use or the or the uh brand and model of the re-enterable stuff, but it's exactly the same.

**Dave Jones:** Has the same sticky consistency after it's set. I think it was a two-part. Um stuff and uh yeah. We used this for where like we had to um adjust pots and things after Well, we had to potentially uh adjust pots after it was all sealed.

**Dave Jones:** So, it is. And well, you know, it's a two-bolt construction. They've got 0.1-in header soldered directly on there. Looks like there's no socket there. It's directly soldered across. And uh that's all there is to it.

**Dave Jones:** It's not high-density stuff. I mean, you know, we've got these um larger uh TO-220s. Look Look like Well, they were TO-220s, but they've had their tabs uh chopped off.

**Dave Jones:** I'm not aware of an actual commercial There's a bit of Mylar insulation as well between um these devices so these tabs don't short out presumably. Um so, they've put that all the way down in there.

**Dave Jones:** They put some on the back as well against the connector, but I don't I recall there being a package like that with a half-moon chopped off. It certainly does look like they've chopped off the tabs to make this fit.

**Dave Jones:** Hmm. And you can see them. They've clearly been chopped off, all right. And uh I wonder who would have done that. Even the uh manufacturer, they probably wouldn't have had a bar of that.

**Dave Jones:** Um, the actual uh device manufacturer themselves, I don't know, maybe you could um order them with yeah half of their tab chopped off, but more likely uh done at the assembler or something like that.

**Dave Jones:** They would have designed uh a jig to chop that off without putting much uh physical uh strain on the device at all. Um, so you don't affect the long-term reliability of the device.

**Dave Jones:** But, uh here you go. It's a rather rather interesting that they've gone to that much trouble. Um, presumably, of course, the big uh power devices are for um firing the uh pyrotechnic charge, which I assume uh requires uh you know, probably a substantial amount of current.

**Dave Jones:** I don't know. I'm not into uh firing the circuitry required to fire pyrotechnic charges, but uh that would be the only reason why you'd have uh large power devices like that in such a device.

**Dave Jones:** And, of course, with the jumper there, you'd have to be very careful that uh you know, you like gunk this after you've put that jumper in place, cuz you wouldn't want to get a bad contact on that because you slid it uh you know, over some potting compound.

**Dave Jones:** But, isn't that wonderful? Oh, it's great stuff. I love it. I'm going to have a hours of fun with this. Now, the other really annoying thing about this is that there's a whole bunch of circuitry on these boards in here on the you know, on the other side of the board.

**Dave Jones:** So, to really do a proper teardown, I'm going to have to desolder I'm going to have to clean off all of the gunk and uh desolder um these boards.

**Dave Jones:** That's really rather annoying. And, these uh pressure sensors, they're they're available in uh several types. One is the um absolute uh pressure sensor which measures the difference between the pressure on the port and an absolute vacuum inside.

**Dave Jones:** Another type is the differential pressure sensor. These will have two ports on them where it measures the difference between one pressure and another. This is obviously not a differential type in that case.

**Dave Jones:** It's most likely a gauge uh uh sensor which measures the pressure coming in the port to the ambient pressure. And there was something in the manual. I don't recall.

**Dave Jones:** I'm not going to check it about this thing, you know, being set to ground pressure and then it or it continually samples against uh I think it continually samples or something like that um to take out the effects of air pressure changes.

**Dave Jones:** And of course, I think desoldering this thing is too much of a pain in the butt. So, easiest way to do it is to just get in there. Thankfully, they've used 0.1 in and cut all of these pins all the way around this thing and hopefully we can pop the two boards apart.

**Dave Jones:** Almost almost there. Uh this is just so un-electronic. It's not funny. Hey, tada! Uh we finally There was an extra bastard connector in there or something, was it? That's what was causing the problems.

**Dave Jones:** Over a Maxim device and bingo, we're in. The main thing that strikes you here is just how old school this design really is. I mean, there's a Motorola MC68HC68 uh real-time clock chip.

**Dave Jones:** There's the real-time clock crystal there. We've got a just a 74 series gate there and this I can barely make out the number on it but I'm but it's definitely a Motorola ZC4 something or other.

**Dave Jones:** Well, it's definitely a microcontroller / processor or definitely a microcontroller cuz there's no external memory on this thing but can't quite make out the rest of it. Unfortunately, there's some crap and gunk on there but yeah, it's some sort of old school mode Motorola which is now Freescale processor on the thing.

**Dave Jones:** And on the back here, it's even more old school. We've got a maximum ICL 7109 in a PLCC package like that. That is a 12-bit ADC for sampling the pressure sensor of course and you know, really incredibly old school stuff.

**Dave Jones:** So, it's on a legacy design. Maybe they've had this design around for you know, 15 years or something and they just haven't bothered to upgrade it. Really, I don't really blame them because you probably have to get this thing qualified and all sorts of things for in terms of you know, a critical application like this that saves people's lives.

**Dave Jones:** So, you know, it's probably all coded in assembler and they would have maybe had to get all the source code approved like they do in you know, intrinsically safe and and other products and stuff like that.

**Dave Jones:** So, um and and other life support applications. So, you know, couple of caps here with the leads bent over, you know, very sort of hackery kind of stuff and it just looks like we've got some old style mouth resistors here and a LT1079 which is a precision op-amp.

**Dave Jones:** So, that's all that's on that board. um you know, an op-amp. So, they've got some uh gain and stuff. Uh you know, they've got the ADC and they've got the processor with old school processor with a real time clock and presumably that's a voltage regulator over there for that, but uh yeah, not much else.

**Dave Jones:** And on the back of the board here, they've got an LT1020, which just is is just a positive voltage regulator. And check out this board up here. We look at these little resistors soldered in in this package over here.

**Dave Jones:** I don't know what that is, um but they've obviously decided to board that in. There's another board here with another uh 100 in cap. And is that a Is that a diode in there?

**Dave Jones:** Anyway, that is, you know, board central, really. And uh But, you know, they've decided that you know, these are all probably hand you know, they're all handmade. They're not produced in uh massive volumes.

**Dave Jones:** They're probably produced by the thousands or something like that. They're certainly not produced by the millions. And they've got a couple of electrolytics on this board. They're 105° uh rated.

**Dave Jones:** They would be absolute uh primo prime spec, you know, this is a high reliability device, uh you know, 10-year uh lifespan. I'm surprised they used electrolytics in here at all actually, but I guess they uh deemed they had to um in that particular location.

**Dave Jones:** Now, as the Let's take a look and see if we can figure out what these TO220s are. Probably just some power transistors. And you're able to just see that marking in there.

**Dave Jones:** It's a BUK455, which is a power MOSFET. No surprise. So, they're clearly uh using those to uh maybe in uh a H-bridge uh configuration, who knows, to uh drive the pyrotechnic um firing device on there.

**Dave Jones:** So, there you have it. There's the Cypres, made in Germany. Hi to all my German viewers. Uh parachute uh emergency deployment system, or whatever it's called. Anyway, um it was rather interesting.

**Dave Jones:** Uh pretty much exactly what I expected in there. It was just a pressure sensor with a micro processor in there. Um so, you know, really there's um nothing else uh in there.

**Dave Jones:** I didn't There's no like uh you know, accelerometer or anything like that. So, obviously they're clearly just using the pressure sensor to detect the height. And well, you know, really, okay.

**Dave Jones:** Um it's like only it deploys about 4 seconds before you hit the ground. So, well, obviously they've done their testing on this thing and determined that, you know, it's it's good enough.

**Dave Jones:** It does the job. Well, I haven't sat down to think about it. I'm not entirely sure how the pressure sensor was working in such a sealed a reasonably well-sealed enclosure like that.

**Dave Jones:** So, you know, anyway, they are able to get this sucker to uh uh actually release, you know, 4 seconds before you hit the ground. And it's got to be ultra reliable.

**Dave Jones:** People's lives depend on these things, and people's lives have been saved by this thing by it firing at the right time. So, if you got any better ideas on exactly how they've implemented this possibly, jump on over to the forum and discuss it.
