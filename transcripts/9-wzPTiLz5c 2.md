---
video_id: 9-wzPTiLz5c
title: EEVblog #339 - Cypres Parachute AAD Teardown
url: https://www.youtube.com/watch?v=9-wzPTiLz5c
source: youtube-asr
timestamps: {"0": 0, "1": 33, "2": 69, "3": 95, "4": 125, "5": 152, "6": 182, "7": 224, "8": 241, "9": 262, "10": 288, "11": 307, "12": 339, "13": 352, "14": 379, "15": 401, "16": 430, "17": 458, "18": 480, "19": 506, "20": 520, "21": 555, "22": 569, "23": 616, "24": 659, "25": 684, "26": 725, "27": 744, "28": 761, "29": 779, "30": 800, "31": 834, "32": 861, "33": 900, "34": 933, "35": 971, "36": 1004, "37": 1039, "38": 1077, "39": 1099, "40": 1118, "41": 1160, "42": 1187, "43": 1227, "44": 1250, "45": 1283, "46": 1315, "47": 1347, "48": 1367, "49": 1406, "50": 1436, "51": 1476}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. You've seen this on the mailbag in a previous video. It's the Cypress Parachute Emergency Release System. So, you know, if you're parachuting and you get knocked out, or you're just too busy enjoying the view, and you forget to pull your chute, if you get to 700 ft or so, if you're going fast enough, this thing kicks in, blows a pyrotechnic charge through a cord, and boom, releases your parachute. And this is quite should be quite an interesting device. And I thought we'd tear it down.

**Dave Jones:** It could actually be a little bit difficult, but I expect there to be a whole bunch of interesting stuff in here. At least it's well-engineered, cuz this thing's got a 10-year lifetime, uh pretty much. You change the battery every couple of years. 10-year lifetime, and it should be built to, you know, an excellent standard in terms of shock, vibration, you know, moisture ingress, all sorts of stuff. So, could be really interesting. Let's check it out. And thanks to Steven in Carlsbad, California, who sent this in again. And

**Dave Jones:** here's the pyrotechnic charge, by the way. A lot of people said I'd be quite careful with this, cuz it could go off with quite a hell of a bang. And it's one-time use only. It's got a little cutter in there. So, presumably, when you apply a voltage on there, it's got a neat little sort of like a funo type connect the system here. And hopefully, well, let's plug it in. And no, it's not going to go bang, honest.

**Dave Jones:** But that looks quite robust and quite rigid. But you can actually disconnect that, so there's no um it does still have the battery inside, so there's no risk of it uh going off now. But little cutter in there, pyrotechnic charge uh fires the blade up through there, which you put the your nylon cord through, and it slices it. And uh that releases your reserve parachute. So, let's have a look at the unit itself and uh it looks like it's got a battery uh compartment on the top here. You're

**Dave Jones:** supposed to I think it's uh Where does it say? It's made in Germany, of course, and uh it was checked in 2007. Um and it did have a battery change sticker on it. There it is. Last battery change uh 10th month '09. So, you know, and it still works. Um so, presumably, you only have to change the battery every couple of years. You set it once, basically, at the start of the day before you go parachuting, you turn the thing on, and it just sits there

**Dave Jones:** waiting, waiting, waiting. There is a should be some sort of um sensor that senses the air pressure and uh and, you know, your rate of fall. Maybe there's an accelerometer inside or something like that. And uh if you're going fast enough at a low enough altitude, under 700 ft, and you're going above a certain speed, bang, it ignites the pyrotechnic charge. So, let's open this thing up and take a look. It's got a battery in here.

**Dave Jones:** Probably a lithium, of course, because it's got a This thing's got to work over temperature extremes. It's waterproof, so I'd expect it to be water sealed or hermetically sealed, the electronics anyway. Um so, it could be Hey, there we go. Yep, primary lithium batteries. That's uh exactly uh Germany German I'm I'm assuming they'd be lithium. I'm pretty darn sure they would be. And look, there's some sort of sensor in there. Is that a uh a uh thermo couple or something measuring the battery temperature? I'm not sure what's

**Dave Jones:** going on there, but that's what I exactly what I would have expected. Um same with like our GPS units and things like that that are designed to activate once and then be used long-term. They've got lithium primary batteries in them.

**Dave Jones:** So, yeah yeah, there we go. Okay. So, oh, okay, that's interesting. Check that out. There's the There's the battery connector and you Yeah, okay. So, you slide that in. Yep, that goes in there like that and there too Well, they're actually Cyprus branded. Um Where are we?

**Dave Jones:** AirTech safety system. So, they've actually had them made for them. Doesn't actually say cuz you know, it's There it is. There's the little you know, matching symbol. They've got it specifically branded batteries. It looks like we have a fuse there in series with the batteries and up here, this is got to be I wouldn't know. There we go. It's a cap.

**Dave Jones:** There you go. So much for a thermal couple, it's an axial capacitor. Go figure. Why have they That is bizarre. Why have they put an axial capacitor in there? What is that? Uh it's a 10-V axial cap. Can't get the reading on there.

**Dave Jones:** But yeah. That's weird. There you go. Anyway, that's it and it looks like it is sealed around there. I see uh some silicone sealant around that. So, they've completely Uh yeah, it's hermetically sealed. You can see it. See it around here. It's actually been sealed. So, this is going to require some percussive maintenance to get apart, I suspect. We'll measure the battery here. It should be two lithium primaries in series.

**Dave Jones:** Bam, there we go. 7.3 V. We have a warning here. Do not remove seal. Okay. I won't remove the seal. I'll just break it.

**Dave Jones:** Tada! Warranty void. And this This is weird. This sort of This is where the This is the connector for the pyrotechnic charge and for some reason it's like got a separate little separate little compartment here. So, let me try and wiggle this thing off. It's rather unusual.

**Dave Jones:** Well, that's rather strange. It's a four-way connector there with two wires and there's going into just this little backshell thing here with a silicone adhesive on the wires there for some strain relief, I'm assuming. There's some surface mount couple of surface mount caps in there.

**Dave Jones:** So, they're probably to uh uh you know, uh keep out any uh uh noise or possibly uh ESD or something like that from I don't know, setting off the pyrotechnic charge perhaps. Um and it's all shielded, of course. There's a shielding wire in there and it's all Yeah, why they've gone to sort of that trouble, um it it beats me. And it is a shield uh uh fully shielded case here.

**Dave Jones:** Of course, you know, you wouldn't want to um you wouldn't want it to be set off by somebody's you know, radio or you know, something like that or you know, if they've got in-ear uh radio talking to each other or something else. Um you certainly wouldn't want the thing to go bang on you. That would ruin your day. So, it's it's it's weird. It's Yeah, it's a metal can, some sort of metal shielded can like foil shielded, I think. Yeah.

**Dave Jones:** Looks like it's foil shielded with a plastic over the top. So, we're going to have to might even have to get out the Dremel maybe.

**Dave Jones:** Mhm, I love the smell of Dremeled plastic in the afternoon. Ah, wonderful. F for fail, perhaps? I don't know. Um yeah, uh the uh plastic uh popped off there and we're left with our metal shielded can. Ta-da! So, looks like we're going to have to get into this sucker as well. Ah, man.

**Dave Jones:** Rather interesting here, this looks to be like a flap that lifts up. So, I'm going to desolder that.

**Dave Jones:** That pops off off real easy. There we go. Ta-da! Hey, look at that. We have some configuration jumpers. And those jumpers would of course uh you know, let the manufacturer this thing sh- completely shield it and then uh presumably um uh do configuration afterwards. I don't know what type of uh configuration, maybe it's the uh you know, the uh level that it goes off at or something like that at you know, they maybe they have different uh models. Uh yeah, actually I think they do. They have different models that

**Dave Jones:** go off um at different levels, you know, based if you got uh like a single jumper or a tandem jumper or a student jumper or whatever. So, um no pun intended, they change the jumper switch based on the jumper.

**Dave Jones:** Now, we could try and desolder this all nicely, but really I think we're better off just prying and then cutting the thing open. Hey. Oh, look at that. Potting compound. What? So, yeah, I mean, you can just cut these things open. I mean, there's no um Don't use your good uh side cutters, by the way. Use your cheap 100 ones to do this, but uh yeah, we have potted electronics in there. There it is. Boing. Yeah, it's Ah, oh, hang on. No. Hang on. Hey, no.

**Dave Jones:** It's just like an outer uh an outer layer of potting or something. Anyway, let's open finish this off cracking it open and see what we've got. And I'm starting to see pressure sensor. There There it is. Classic uh shape uh classic style of pressure sensor. become clearer once we open this thing. And here it is, minus its metal can, a one big sticky gooey mess of uh easy entry potting compound. It's not solid uh potting compound, but it's this really It's called uh re-enterable uh potting compound. It basically um I've

**Dave Jones:** used this stuff before, and it's really neat because you can actually uh seal stuff, but then afterwards uh after it's sealed, you can you can penetrate it with a screwdriver, and you can get in there, and you can adjust pots and things like that, and then pull it back out, and it'll reseal itself automatically. So, that's why it's called re-enterable cuz you can re-enter it, and then it self-seals.

**Dave Jones:** That was Gee, a long time ago I used this stuff, but it's really neat. It really is neat stuff, and they've put this Mylar wrap around the Oh, man. How gooey and ugh That is That's really Yeah, this is just as I remember this stuff. Really sticky. So, they've put these uh like a Mylar type sheets or whatever they are capped on or whatever on between the um between the circuitry and the the boards and the metal can so that the metal can't short out the

**Dave Jones:** electronics. So, if it gets crushed or anything like that, it's still going to survive and not ugh not short Oh, man. This is yeah. Yeah. This is horrible as I remember. Terrible stuff. Terrible, terrible, terrible. But, so that's in there.

**Dave Jones:** That's all protected by that and then they've gunked it all up. This is a real fascinating uh They've gone to a bit more trouble than I had envisaged.

**Dave Jones:** This is great. It's like pulling, you know, cobwebs off something. It's uh So, we've got one main PLCC device here and another sock Oh, man. This is going to take forever. Yucko. There's our circuit. We've got a real-time clock.

**Dave Jones:** Crystal 32 kHz watch crystal there. The main oscillator The main crystal there for the oscillator for whatever that device is. It tell There's the pressure sensor. It's the classic uh a port type there and they've just used, you know, an off-the-shelf uh one. You can see why it's um how it's got that uh ridge on there.

**Dave Jones:** It's designed to have like a tube go over it. Uh so They've Oh, man. This is great. Oh. Hours of fun and enjoyment this re-enterable potting compound. I'm telling you, get some. It's brilliant. Uh I can't remember like the brand of stuff we used to use or the or the uh brand and model of the re-enterable stuff, but it's exactly the same. Has the same sticky consistency after it's set. I think it was a two-part.

**Dave Jones:** Um stuff and uh yeah. We used this for where like we had to um adjust pots and things after Well, we had to potentially uh adjust pots after it was all sealed. So, it is. And well, you know, it's a two-bolt construction. They've got 0.1-in header soldered directly on there. Looks like there's no socket there. It's directly soldered across.

**Dave Jones:** And uh that's all there is to it. It's not high-density stuff. I mean, you know, we've got these um larger uh TO-220s. Look Look like Well, they were TO-220s, but they've had their tabs uh chopped off. I'm not aware of an actual commercial There's a bit of Mylar insulation as well between um these devices so these tabs don't short out presumably. Um so, they've put that all the way down in there. They put some on the back as well against the connector, but I don't I

**Dave Jones:** recall there being a package like that with a half-moon chopped off. It certainly does look like they've chopped off the tabs to make this fit. Hmm. And you can see them. They've clearly been chopped off, all right. And uh I wonder who would have done that. Even the uh manufacturer, they probably wouldn't have had a bar of that. Um, the actual uh device manufacturer themselves, I don't know, maybe you could um order them with yeah half of their tab chopped off, but more likely uh done at the

**Dave Jones:** assembler or something like that. They would have designed uh a jig to chop that off without putting much uh physical uh strain on the device at all. Um, so you don't affect the long-term reliability of the device. But, uh here you go. It's a rather rather interesting that they've gone to that much trouble. Um, presumably, of course, the big uh power devices are for um firing the uh pyrotechnic charge, which I assume uh requires uh you know, probably a substantial amount of current. I don't know. I'm not

**Dave Jones:** into uh firing the circuitry required to fire pyrotechnic charges, but uh that would be the only reason why you'd have uh large power devices like that in such a device. And, of course, with the jumper there, you'd have to be very careful that uh you know, you like gunk this after you've put that jumper in place, cuz you wouldn't want to get a bad contact on that because you slid it uh you know, over some potting compound. But, isn't that wonderful? Oh, it's great stuff. I love

**Dave Jones:** it. I'm going to have a hours of fun with this. Now, the other really annoying thing about this is that there's a whole bunch of circuitry on these boards in here on the you know, on the other side of the board. So, to really do a proper teardown, I'm going to have to desolder I'm going to have to clean off all of the gunk and uh desolder um these boards. That's really rather annoying. And, these uh pressure sensors, they're they're available in uh several types. One is the um absolute uh

**Dave Jones:** pressure sensor which measures the difference between the pressure on the port and an absolute vacuum inside. Another type is the differential pressure sensor. These will have two ports on them where it measures the difference between one pressure and another. This is obviously not a differential type in that case. It's most likely a gauge uh uh sensor which measures the pressure coming in the port to the ambient pressure. And there was something in the manual. I don't recall. I'm not going to check it about this thing, you know,

**Dave Jones:** being set to ground pressure and then it or it continually samples against uh I think it continually samples or something like that um to take out the effects of air pressure changes. And of course, I think desoldering this thing is too much of a pain in the butt. So, easiest way to do it is to just get in there.

**Dave Jones:** Thankfully, they've used 0.1 in and cut all of these pins all the way around this thing and hopefully we can pop the two boards apart. Almost almost there.

**Dave Jones:** Uh this is just so un-electronic. It's not funny. Hey, tada! Uh we finally There was an extra bastard connector in there or something, was it? That's what was causing the problems. Over a Maxim device and bingo, we're in. The main thing that strikes you here is just how old school this design really is. I mean, there's a Motorola MC68HC68 uh real-time clock chip. There's the real-time clock crystal there. We've got a just a 74 series gate there and this I can barely make out the number on it but I'm

**Dave Jones:** but it's definitely a Motorola ZC4 something or other. Well, it's definitely a microcontroller / processor or definitely a microcontroller cuz there's no external memory on this thing but can't quite make out the rest of it. Unfortunately, there's some crap and gunk on there but yeah, it's some sort of old school mode Motorola which is now Freescale processor on the thing.

**Dave Jones:** And on the back here, it's even more old school. We've got a maximum ICL 7109 in a PLCC package like that. That is a 12-bit ADC for sampling the pressure sensor of course and you know, really incredibly old school stuff. So, it's on a legacy design. Maybe they've had this design around for you know, 15 years or something and they just haven't bothered to upgrade it. Really, I don't really blame them because you probably have to get this thing qualified and all sorts of things for

**Dave Jones:** in terms of you know, a critical application like this that saves people's lives. So, you know, it's probably all coded in assembler and they would have maybe had to get all the source code approved like they do in you know, intrinsically safe and and other products and stuff like that. So, um and and other life support applications.

**Dave Jones:** So, you know, couple of caps here with the leads bent over, you know, very sort of hackery kind of stuff and it just looks like we've got some old style mouth resistors here and a LT1079 which is a precision op-amp. So, that's all that's on that board. um you know, an op-amp. So, they've got some uh gain and stuff. Uh you know, they've got the ADC and they've got the processor with old school processor with a real time clock and presumably that's a voltage regulator over there for that, but uh

**Dave Jones:** yeah, not much else. And on the back of the board here, they've got an LT1020, which just is is just a positive voltage regulator. And check out this board up here. We look at these little resistors soldered in in this package over here. I don't know what that is, um but they've obviously decided to board that in. There's another board here with another uh 100 in cap. And is that a Is that a diode in there? Anyway, that is, you know, board central, really. And uh

**Dave Jones:** But, you know, they've decided that you know, these are all probably hand you know, they're all handmade. They're not produced in uh massive volumes. They're probably produced by the thousands or something like that. They're certainly not produced by the millions. And they've got a couple of electrolytics on this board. They're 105° uh rated. They would be absolute uh primo prime spec, you know, this is a high reliability device, uh you know, 10-year uh lifespan. I'm surprised they used electrolytics in here at all actually, but I guess they uh deemed

**Dave Jones:** they had to um in that particular location. Now, as the Let's take a look and see if we can figure out what these TO220s are. Probably just some power transistors. And you're able to just see that marking in there. It's a BUK455, which is a power MOSFET. No surprise.

**Dave Jones:** So, they're clearly uh using those to uh maybe in uh a H-bridge uh configuration, who knows, to uh drive the pyrotechnic um firing device on there. So, there you have it. There's the Cypres, made in Germany. Hi to all my German viewers. Uh parachute uh emergency deployment system, or whatever it's called. Anyway, um it was rather interesting. Uh pretty much exactly what I expected in there. It was just a pressure sensor with a micro processor in there. Um so, you know, really there's um nothing else

**Dave Jones:** uh in there. I didn't There's no like uh you know, accelerometer or anything like that. So, obviously they're clearly just using the pressure sensor to detect the height. And well, you know, really, okay. Um it's like only it deploys about 4 seconds before you hit the ground. So, well, obviously they've done their testing on this thing and determined that, you know, it's it's good enough.

**Dave Jones:** It does the job. Well, I haven't sat down to think about it. I'm not entirely sure how the pressure sensor was working in such a sealed a reasonably well-sealed enclosure like that. So, you know, anyway, they are able to get this sucker to uh uh actually release, you know, 4 seconds before you hit the ground. And it's got to be ultra reliable. People's lives depend on these things, and people's lives have been saved by this thing by it firing at the right time. So, if you got any better ideas on exactly

**Dave Jones:** how they've implemented this possibly, jump on over to the forum and discuss it.
