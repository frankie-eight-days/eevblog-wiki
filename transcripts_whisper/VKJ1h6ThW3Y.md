---
video_id: VKJ1h6ThW3Y
title: EEVblog #888 - Mailbag
url: https://www.youtube.com/watch?v=VKJ1h6ThW3Y
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 13, "2": 37, "3": 57, "4": 89, "5": 109, "6": 129, "7": 141, "8": 165, "9": 181, "10": 201, "11": 213, "12": 233, "13": 253, "14": 273, "15": 289, "16": 305, "17": 321, "18": 337, "19": 361, "20": 373, "21": 389, "22": 405, "23": 425, "24": 441, "25": 453, "26": 469, "27": 481, "28": 501, "29": 509, "30": 529, "31": 545, "32": 561, "33": 577, "34": 593, "35": 609, "36": 629, "37": 645, "38": 677, "39": 697, "40": 713, "41": 729, "42": 745, "43": 787, "44": 807, "45": 827, "46": 851, "47": 879, "48": 907, "49": 931, "50": 943, "51": 967, "52": 983, "53": 1003, "54": 1019, "55": 1043, "56": 1063, "57": 1079, "58": 1099, "59": 1115, "60": 1131, "61": 1147, "62": 1159, "63": 1183, "64": 1203, "65": 1219, "66": 1239, "67": 1259, "68": 1275, "69": 1295, "70": 1315, "71": 1335, "72": 1351, "73": 1383, "74": 1419, "75": 1443, "76": 1455, "77": 1479, "78": 1499, "79": 1515, "80": 1531, "81": 1539, "82": 1563, "83": 1583, "84": 1603, "85": 1619, "86": 1639, "87": 1659, "88": 1675, "89": 1703, "90": 1719, "91": 1759, "92": 1779, "93": 1795, "94": 1811, "95": 1827, "96": 1847, "97": 1863, "98": 1879, "99": 1895, "100": 1915, "101": 1935, "102": 1955, "103": 1971, "104": 1983, "105": 1999, "106": 2015, "107": 2031, "108": 2071, "109": 2083, "110": 2099, "111": 2119}
---

**Dave Jones:** Hi, welcome to everyone's favorite segment, Mailbag! Let's get right into it. Sorry, I did promise a couple of weeks back I'd do one every week, but yeah, I've been sick and had various other issues. So, I'm back into it. This one is from the heathen...

**Dave Jones:** it is addressed to the heathen down under. Yes, I'm a heathen! Well, no I'm not, because I acknowledge the existence of the flying spaghetti monster, so that doesn't make me a heathen at all. Just because I don't think there's any validity whatever particular god you happen to

**Dave Jones:** believe in, one of the many thousands. Nah, flying spaghetti monster's a go. He can talk like a pirate and everything. It's great! Anyway, let's see. Sorry, Christine Truen. Sorry, I can't pronounce that last name. That's too hard. Thank you very much, Christine. With a Y.

**Dave Jones:** That's not how you usually... I like that. Oh! Yeah. Okay. Oh! It's from the author! It's from the author! Oh dear. It's a fairy tale. Excellent. Christian mythology for kids. A secular family's guide. Oh, a secular! Oh, excellent. A secular family's guide to modern...

**Dave Jones:** Dear Dave, thank you for supporting the creation of this book by helping spread the word. Please enjoy a copy of the finished product. Christine. There you go. There's Christine. Excellent. She's an enthusiastic atheist and mother of two mindful and inquisitive boys. Fantastic. Christianmythologybook.com

**Dave Jones:** I'll link it down below because it's written by an atheist. Beauty. Aha! I remember this now. As it turns out, Christine is not a viewer, but her husband Dylan is, and apparently my voice gives Christine the shivers, so go figure. Anyway, I won't go into it, but

**Dave Jones:** suffice to say this was a Kickstarter. They wanted $13,000 to print the book, and it was successful, and they've sent me a copy. So I know this is off topic, so I'll spare you the details, but I just wanted to show you this.

**Dave Jones:** It's creepy. See anyone you know? Or think you might know? That guy there's looking a bit dodgy. Next up, one from Australia, you bloody beauty, from nobody. It's just a mailbag, and it's a dollar. It's a dollar to post something now. Unbelievable. But Australia Post hasn't been

**Dave Jones:** making money and all that sort of stuff because, well, they don't know how to operate a proper business. And they're slashing everything, and ooh, the internet's killed all our business. All it has? Geez, if anything, it's probably increased your business. Anyway, let's see what Person Unknown has sent.

**Dave Jones:** Oh, they've just stuck the flap on the address flap on the inside. Okay, we have a schematic. Looks like it's done in Eagle. And, hi Dave! Was always that kind of child who took apart old electronics, weren't we all? We have a PCB.

**Dave Jones:** Let's check it out. And we have a board from Daniel who's doing his Masters in Computer Science. Excellent. He wanted to send in something for mailbag. Anyway, it's a new electronic dummy load that he's working on. Ta-da! Here it is. Yeah, we've had many dummy loads.

**Dave Jones:** I think I really started something with my original dummy load video because the number of EEVblog forum threads, for example, with people doing their own dummy loads is phenomenal. But anyway, it's fantastic. And this looks like a decent looking board, except for a problem which Daniel's having.

**Dave Jones:** Let's take a look. It's to do, he's got two MOSFETs on here, but one is dissipating more power than the other. So he's having issues balancing the MOSFETs. As he understands the problem, the RDS is different for the same VG due to manufacturing differences.

**Dave Jones:** Yes it is, and there's various other parameters involved as well, and it usually involves a temperature differential, and also I was actually going to suggest the tracing on the board as well. So the first thing to look at with the offset problem, and I can see it straight away,

**Dave Jones:** you're going to have an issue. You're trying to match MOSFETs, I believe these two must be the two MOSFETs. You can see the heatsink outlines here and here, they're on separate heatsinks. And bingo, therein lies your first problem when you try and parallel MOSFETs together.

**Dave Jones:** In theory, you know, everything works great, you just parallel MOSFETs and they're supposed to be well behaved and all that sort of jazz, but if they're not tied to the same heatsink, you can get thermal, definitely get thermal differences between them, and you get an issue.

**Dave Jones:** So that is the number one problem. The second one is, does he have current-sharing resistors in the thing? To do that, we'll have to take a look at the schematic. So the first thing we'll do is take a look at the schematic here.

**Dave Jones:** Sorry, I ripped it. It looks very nice, I like how they're all separated into the separate subsections like that. And are there actual design notes on there as well? Anyway, it looks very good. And take a look here, where's my poker? I don't know, let's

**Dave Jones:** use this. Here's our MOSFETs, and well, there's your problem. Yep, there's our current sensor resistor down there. There it is, tapping off there, no problems. But there is no current-sharing resistor in the source here. So that is one problem. And the other problem is that they're on separate heatsinks,

**Dave Jones:** so they're not thermally matched, so therefore, yep, you're going to get an imbalance between, or you can get an imbalance of those two MOSFETs. If you get two from exactly the same batch that came from the same wafer and everything else, it can be more controlled.

**Dave Jones:** But yeah, it's not guaranteed. I mean, you're buying from Digi-Key, you know, they might come in the same tube, but you know, all the same reel or whatever doesn't mean they came from the same wafer. So you know, you can't guarantee that at all.

**Dave Jones:** So basically you have to work around the maximum parameters on the data sheet. And there's a whole lot of science between matching MOSFETs into it if you really want to get down to the nasty detail of, you know, the physics of the whole thing

**Dave Jones:** and everything else. But generally, if you thermally match them on the same heatsink close together, and you put in some source resistor there, I won't go through the calculations of calculating a source current-sharing resistor in there, but that should do the trick. By the way, there's some debate whether or not you should actually separately drive each

**Dave Jones:** MOSFET with its own feedback loop and things like that. And generally speaking no, you don't have to do that. But you know, so you can get away easily with that. So doing those two things I think could solve the problem here. And he's put the performance envelope curve on there, thank you very much.

**Dave Jones:** And as Daniel mentioned on here before, the traces for the two MOSFETs can make a difference as well, so that's not the title. If we flip it over we can have a look what's happening here. Here's the source, okay, this is coming from our

**Dave Jones:** there's our current shunt resistor there, and you'll notice that yeah, short trace here to this MOSFET, but then it's got to go through that, so the current for this MOSFET is actually coming through this trace for this MOSFET. That's a no-no. You should

**Dave Jones:** star that, and preferably keep them equal length, but you probably don't. But the fact that, you know, it's coming through there for the other MOSFET yep, that's a goof. So you want to fix that, you want that going straight across there like that.

**Dave Jones:** But apart from that, he wants feedback on the board, and I like it. I like the little breakout tab here with the rotary encoder, presumably that's done so that you can either use it on there, or presumably you can break it off just break off the tabs there, cut them out for a pair of side cutters, and mount that on the front

**Dave Jones:** panel. And he's kept that in the square of the thing, I don't know, maybe this fits into a box or something, but that's a neat way just to get your extra board, you don't have to get your extra board manufactured, it's all part of your panel.

**Dave Jones:** Very nice indeed. And everything laid out, this is right near here, yeah, your layout's good. Yep, there's no traces, you know, going from one side all the way to the other. It looks neat, it looks neatly laid out. Good layout, good placement, good

**Dave Jones:** component placement is 90% of your layout work, trust me. So you know, if you whack this chip over here, for example, when you knew you had to connect it through to this RS-232, or you say yeah, you had this RS-232 drive here, and you put it over here, and then you have to run

**Dave Jones:** from your micro over to here and then back over there, well that's poor layout. And your design is going to be completely screwed on a double-sided board like this. But yeah, that's, apart from that, that looks, so apart from the MOSFET thing, that looks fairly decent.

**Dave Jones:** Good on you Daniel, I'll link to it down below, it's all on GitHub, it's all open source, all the usual business. Next up, another one from Australia Express Post, thank you very much Greg Pool and he's from Oakey in Queensland, haven't been to Oakey?

**Dave Jones:** I think I've sent some stuff to Oakey once, but yeah, haven't been there. Let's have a look, it feels kind of, kind of like multimeter form factor, although it's a bit too heavy for a multimeter, it's about 700 grams or something, so, which is why it had to

**Dave Jones:** come in the 3 kilo satchel instead of the 500 gram satchel. They do have 1 kilo satchels now, just came out, but only available on Express. Sorry, little rant there. Let's see what Greg has sent. So yeah, if you want to send over 500 grams, you've got to jump up.

**Dave Jones:** If you want to know why, one of the reasons why I don't supply the multimeter, the manual, the printed manual with my BM 235 multimeter is because it actually puts it over 500 grams, which means for local postage, I've got to up it to the 3 kilo

**Dave Jones:** satchel, and pay and charge a lot more for the postage, just because the printed manual puts it over the 500 grams. So, yep. So anyway, let's have a look. It's pretty heavy, it's like a power brick or something, is it? Ah, old school.

**Dave Jones:** People complain about the weight of modern phones. It's the Telstra Walkabout. Oh yeah. Baby. That's more than a 2 minute teardown. Retro phone teardown. Separate video. Awesome. Thanks Greg. Wow, check it out. Thank you very much Greg. This is the Telstra Walkabout. It is actually the, well, it's not manufactured

**Dave Jones:** by Telstra. Telstra's like our national telecoms provider here in Australia. It's actually manufactured by Mitsubishi, and this was actually the first mobile phone in Australia. It's the MT398, and all those letters for those playing along at home. And it came out in 1986.

**Dave Jones:** Absolute classic. Look at this. None of this modern digital GSM rubbish. No sirree bob. This thing's analog all the way with LBJ. And love the antenna. Look at that. Obviously it didn't look like this. This is where the battery pack snapped in here

**Dave Jones:** down like that. And there we go. That's a little whip on there. That went inside the battery. That's kind of sort of clever use of space there, but yeah. Analog mobile phone. No coax up here. No coax that I could see to hook

**Dave Jones:** into your phone. Maybe they, no they wouldn't have it as part of the battery solution, so I don't know. Oh it could couple, maybe, I don't know. Anyway, it was the first Australian analog mobile phone from 1986. And I found some classic photos on the web.

**Dave Jones:** Check them out. And there's one reference that said this cost $5,000 when it came out in, I think there's another source that says 1987 so I think, you know, it probably came out somewhere else in 1986 Mitsubishi in some other country, I don't know, but anyway

**Dave Jones:** round about that vintage. So we're talking pretty close to 30 years old, but imagine if it did cost that much back in the day. Wow! None of this mobile phone plan rubbish. It's an Aussie Bonanza! Woohoo! Three in a row. This one comes from person unknown, but

**Dave Jones:** comes from North Sydney. Here in Sydney on the north side, obviously. No, surprisingly the harbour bridge does not link Australia to New Zealand, which a lot of Americans think, believe it or not. Um, no, it connects Sydney with North Sydney. Anyway, thank you very much unknown person, maybe we'll get a

**Dave Jones:** note inside. So it's bloody heavy. And it rattles. So it's got a Farnel sticker on it. I doubt it's a Farnel item though. Okay, we've got some gaffer tape. Put it in. Okay. Tighten it at the right angle. Here we go. What have we got?

**Dave Jones:** Oh! Wow! I had one of these! Oh! An old Scalelectric kit? No. For his old Scalelectric kit? No! I had one of these! Wow! Wow, that brings back memories, hang on. Oh, I can smell the memories back in the old garage with my old HO Scale

**Dave Jones:** train set! It's a Triang! It's a Triang train controller! Fantastic! Thank you very much Ian! Teardown! Already! I can remember tearing this down when I was like seven! Great! There's not much in it. Oh! It's got that real electronic smell. Beauty. Oh, this puppy brings back way too many

**Dave Jones:** memories! Look at this! Built in Australia. Beautiful Triang. Ian asks found the old, powering an old Scalelectric kit, but it's not for Scalelectric. It's for, I believe, hobby railways. I mean, Triang were famous for that. And if memory serves me correctly, that is an overload switch, so it'll pop out

**Dave Jones:** if you overload the thing, so you can just press it back in to reset it. And forward and reverse voltage! That's it! Is that a pot? No, that's not a pot under there. No, it's one of these studs that has just fallen out.

**Dave Jones:** But yeah, absolute classic. We've got, there's our controlled output, our 12 volts DC. Uncontrolled output, you would typically use those for you know, accessories, points, you know, lights and things like that. And 15 volt AC output as well. I don't ever recall using, requiring the 15 volt AC

**Dave Jones:** output for anything, but anyway, that's obviously coming directly out of the transformer, and this is coming out of the rectified DC side. But as Ian says in here, the most interesting thing about inside is the rectifier. Yes! And we'll take a quick look at it.

**Dave Jones:** Ah, Hitachi V212. I love that scope, the trace was nice and sharp. Beautiful little analog scope, the Hitachi one, and they had like a 40 megahertz version, and ah, beautiful. Anyway, that was actually the first scope I used at my first job in 1989.

**Dave Jones:** I think it was? Yep. So there you go. Anyway, love that little thing. Let's take a look inside. Inside is just hilarious. We've got ourselves our transformer here, we're getting our 15 volts AC out of here, and none of this regulation rubbish, no active circuitry in here.

**Dave Jones:** We've simply got our rectifier, which we'll take a closer look at, and our nichrome, presumably, nichrome resistance wire, and there's a knob on the backside of that with the lever in there, and that goes either direction to switch the direction of the thing, it's rather clever, but yeah, there's no

**Dave Jones:** regulator inside this thing, and we have a rectifier, but like there's no even output smoothing cap, so that's why you get that, because it's rectified, but yeah, you don't but it's not smoothed at all, it's not even, like you wouldn't even call that 12 volts DC, it's like, you know, 100% ripple.

**Dave Jones:** And here it is, for those who haven't seen one before, believe it or not, that is a diode, it's a rectifier, and also, believe it or not it actually works not too dissimilar to, you know, the regular silicon diode you're used to, because it's called a metal plate rectifier

**Dave Jones:** or a selenium rectifier, or, you know, a plate rectifier, whatever you want to call it, and the plates in there are coated with either selenium, hence the name selenium rectifier, or a copper oxide, and both of those are actually a semiconductor, so this essentially is

**Dave Jones:** a semiconductor diode, it just uses these big metal plates in there, but they're horribly inefficient, I mean these things date back to the 30s and 40s and things like that, so why it's still used in a trying power supply like this, but that was a, when I was a kid in the 70s

**Dave Jones:** this was not uncommon, you'd get battery charges with these things in them for example, and when I first actually opened this, I had no idea what this was, because, you know, I was growing up in the 70s, I started my electronics hobby stuff in the 70s

**Dave Jones:** and, you know, silicon diodes, I could buy it at my local Tandy store or, you know, Dick Smith store, so it, like these things were just a complete mystery to me, because we didn't, you know, I couldn't find any information on them, didn't have any information in my

**Dave Jones:** data books and archives and magazines and things like that, and I just had no idea, I knew it was some, it had to be some sort of rectifier, but I didn't actually know how it worked or what was in it, because we didn't have access

**Dave Jones:** to the internet like we did these days, but yeah, fascinating old things, these plate rectifiers but they're horrible things, absolutely horrible. So that is certainly one crappy, inefficient power supply, it's probably the worst 12 volt DC power supply you could possibly get, but hey, you know, these things worked for powering your

**Dave Jones:** trains and your points and everything else, these things worked just fine back in the day, so yeah, oh yes, my old HO train layout, I had a 16x8, 16x8 HO scale train layout in the garage. Beauty. And if you're wondering why they actually contain multiple plates down in

**Dave Jones:** here, it's because each, they're actually multiple ones in series, it's, the reason is because they had very poor, like as in a couple of volts reverse breakdown voltage, none of this you know, 50, 100 volts or 1000 volts you're used to with regular

**Dave Jones:** silicon diodes, no siree bob, a couple of volts, so you had to string them in series to get adequate reverse voltage. Unbelievable, these things were just awful. Alright, just for kicks I've put a 22 ohm 10 watt resistor on the controlled output, and we've got it off at the moment, 2 volts per

**Dave Jones:** division here, and if we switch it on, bam! Look at this, 2, 4, that's what we're getting quite a high output voltage, that's incredible actually. That's like, that's barely on, so that's off, and that's on. The average here, we're getting about 5.3 volts.

**Dave Jones:** Remember this is into a 22 ohm load, and we turn it up, and we're looking at 12 volts peak now, and 7.1 average, but if we turn it up here we go, all the way, and yep, there we go, about 13 volts average there.

**Dave Jones:** So you know, but look at it, I mean, it's direct current, yeah, it's not going negative, there's our ground point, but jeez, not very good is it? And if I center it here, that's what we had before, I'm now on 5 volts per division,

**Dave Jones:** and if we go the other direction, there we go, you can see it go in the negative direction as well. Just a bit of noise on there, you can see the yeah, that's just the crusty old pot. I got one from Switzerland, hi to all my Swiss viewers, I love Switzerland.

**Dave Jones:** Went to Switzerland for lunch one day, as you do when you're in Europe, so I unfortunately haven't seen much of Switzerland, I've seen Geneva, but that's about it. So thank you very much, Jorg, Jorg? Sorry, Schneider, thank you very much, from Biel? Bien?

**Dave Jones:** Something like that. Anyway, let's have a look. I noticed while watching some of the teardowns that using a screwdriver from PB Swiss Tools, yes I do, somebody sent them into my mailbag. Thank you very much, I forget who sent them in. That's his favorite brand,

**Dave Jones:** a friend of mine, manufacture assembling and imprinting tools by PB Swiss Tools. Ah, okay, cool. So let's have a look. Spoiler. Ta-da! Oh, yeah, baby. I don't even have to look at that. Oh, it's personalized, look at that. Bloody ripper! EV log, oh, look at that.

**Dave Jones:** Oh, nerdgasm, nerdgasm. Oh, yeah. Baby, that's a beautiful Swiss tool set. That's got the one with all the shafts, jeez, they're long too. So if you're really needed yeah, okay, yeah. It's fantastic. Beautiful. Oh! Chocolate! Ladderach. Ladderach chocolate? Anyway, it's Swiss chocolate. Beauty.

**Dave Jones:** Oh, look at that! What a bobby dazzler! Thank you very much, Jorg. I'm sure I'm pronouncing your name incorrectly, because I'm totally incapable of pronouncing names, but this is just fantastic. We've got torques, we've got large phillips, large flats, we've even got a pretty sharp, look at that, sharp point

**Dave Jones:** there. Bloody ripper. And we've got a couple of smaller ones here. Excellent. They're just, they're great for like trimming and stuff like that. You've got to have the spin top on them. Fantastic, so that you can get in there and go eh, eh, eh, eh, eh, eh, eh, eh, eh, eh.

**Dave Jones:** There's the money shot for those playing along at home. Ah, beautiful. Nerling. Swiss made, thank you very much. And these are supposed to be ESD. Jorg says that from 1 meg to 1 gig, I would have expected static dissipative, but anyway, let's try and measure it.

**Dave Jones:** I would actually expect nothing with the meter. And yep, sure enough. Let's dig her in and zippity doo dah. Yes, because they're not conductive, they're static dissipative. Let's get something a little bit better. I've got the Keysight U1461A meter. We haven't seen this here, I don't think I've actually done a teardown on this.

**Dave Jones:** I need to do a teardown. It's IP 67 rated and it's got a mega built in 50 volt range up to 1000 volts. And that 50 volt range is actually very handy having such a low voltage range specific applications. When I was working in

**Dave Jones:** the seismic industry, we had a, and testing our seismic underwater cables which would have hydrophones on them, and they were actually limited to 50 volts. You put any higher than that on, you risk actually blowing the hydrophones on things, and we'd have to test the lines, and it was actually

**Dave Jones:** wasn't easy to get a mega with a 50 volt range back then. This was, you know, like a decade ago. You know, you might be able to get one with 100 volts minimum or something, but getting, you know, having a low voltage can be handy.

**Dave Jones:** Anyway, let's give this a go, and see. We've got our... oh, I'm seeing flicker. I'm seeing flicker on the display here, but let's give this a burl here. I'll just bring this better into shot for you. And let's probe this. No touchy with these megas, even at 50

**Dave Jones:** volts, you know, shouldn't be touching it. Anyway, let's go. And you've got to hold it down. 66 gig, but wait for it. Trap for young players. Got to charge up. There we go. About 23 gig, or thereabouts, at 50 volts. Beauty. Alright, let's up that to 1000 volts

**Dave Jones:** and give it a burl. There we go. 15 gig at... eh, 17 gig at 1000 volts. So, so much for their claim here. Surface resistance of the dissipative plastic is 1 meg to 1 gig. It's much higher than that, but it doesn't matter, as long as it's

**Dave Jones:** dissipative, that's fine. And what I'm going to do is actually the internal black plastic, I mean this was the outer rubber, so let's go back to 50 volts, just for interest's sake, and... there we go, 130 meg. So that's right for the plastic.

**Dave Jones:** So they are talking about the plastic inside, not necessarily the outer rubber type coating here. And 1000 volts. Oop. Come on, you can do it. There we go. 0.33 meg, 0.2 meg at 1000. Well it's actually dropped right down to 250, you saw it there.

**Dave Jones:** Just couldn't deliver enough current. And this tiny little set that snaps out, double-ended, oh that's just beautiful. Brings a tear to the eye. So thank you very much Jorg and your friend for producing this. Fantastic. This one's going straight to the pool room.

**Dave Jones:** Next up, I've got one from Italy. Hi to all my Italian viewers, this one's from Gabriele Galazzi. Thank you very much Gabriele. Let's have a look. It's relatively light, but it's a bit big. Trying to get through the bigger ones on here. So we'll see what happens.

**Dave Jones:** Yes, cutting towards myself because I'm a professional. Alright, here we go. And it's in one of these, oh great, nothing else. Some old newspapers, Italian newspapers. It's in one of these frustration-free, like Amazon-like frustration-free packaging. Let's have a look. It looks totally legit.

**Dave Jones:** From, oh, gtronics.net. I'm pretty sure Gabriele has sent stuff in before. I wanted to give this kit to Sagan, but probably even if he's used to deal with scopes and all kind of, he'll still be too young. Aw, bummer. Okay, it's a kit.

**Dave Jones:** Spoiler. Fail. There we go. Alright, we're in luck then. We've got instructions. It's a proto-shield for Arduino and Genuino. Genuino. Is that genuine Arduino? I don't think so. Anyway, it's a breadboard-y type kit. Awesome. Thank you RS Gabriel. We'll take a look. We've got ourselves another Bobby Desler

**Dave Jones:** here. Check this thing out. Isn't it beautiful? It's a breadboard interface, or a breadboard with all sorts of Arduino interfaces here. Look at this. We've got an Arduino which plugs on the bottom. There's the Genuino, that's their version of the Arduino, but it plugs in the bottom there

**Dave Jones:** and look, you can actually, and you've still got the headers on the top where you can plug your shields into. We've got LCD and we've got switches and we've got the Arduino Nano. Look at this, the Arduino Micro, the Arduino Mini. You can plug in all different types of Arduinos into

**Dave Jones:** this thing, and then of course break out all the I.O. onto, and I got a whole bunch of these. I'm sure these come with the standard kit. And we've got other stuff up the top. We've got some output LEDs, we've got more interface.

**Dave Jones:** Unfortunately there is no power supply circuitry on board, but you can plug in a DC jack here, but yeah, there is no circuitry on there to actually produce those separate power supplies, so that's a shame. But look at the bottom of this thing.

**Dave Jones:** Look, they've got all the push buttons, all the info you need on the back of this. This is just brilliant. If you're working with Arduinos, oh man, you've got to have one of these. Here you go, here's the LCD I2C interface, the external USB 2.0 serial interface

**Dave Jones:** and we've got some prototyping area and stuff like that. The push buttons, and look, all the pinouts, they've labelled them all. And you can just of course plug and unplug your Arduino from the bottom there. It's just... oh, and there's the LCD configuration.

**Dave Jones:** It's got everything! More stuff than you poke a crow probe at. And it looks like I've got a starter kit of LEDs and resistors and some trannies in there, and all sorts of stuff. Fun for the whole family, and let's have a look.

**Dave Jones:** Thanks for the entertaining blog, thank you very much. And he wanted to give this kit to Sagan, but yeah, he's probably, he is a bit too young to play with breadboards, I don't want to start him on that yet, I don't think. Anyway, it's a prototyping shield for Arduino,

**Dave Jones:** it's a little bigger and usable than a little standard proto shield. No kidding! It's called the Proto Shield Plus, it's used to quickly test ideas, key features artworks with Arduino, and all sorts of versions of Arduino. LCD ready, IO expander on board, it's a PCF8574 expander, and all

**Dave Jones:** sorts of stuff. It is absolutely brilliant, I will link this in down below. And I have got the manual for the thing, and the manual looks really good. Check it out! Look at this! User manual version 3. Look at this! Ah, beautiful all-colour code, ah,

**Dave Jones:** beautiful photos. Ah, it's very professionally done. I like it. Using the proto shield, using all sorts of different things, the USB, serial signals, it's all there. Winner winner, chicken dinner! Huge thumbs up for this. Nice. So the entire starter kit that you see here

**Dave Jones:** are 69 euros. That includes the Arduino on the bottom and everything, and the kit and the wires and the LCD and everything. You can get like a stripped down version of this cheaper without the LCD, if you just sort of want, and if you've got your own Arduinos, barebones, a little bit cheaper.

**Dave Jones:** But yeah, that is a bargain. So that's got to be the most comprehensive and flexible Arduino prototyping platform I've seen. Very nice. Shame it doesn't have any extra power supply stuff, that would have been nice on there, but you know, you're powering through the Arduino.

**Dave Jones:** And you've got access to the 3.3 and the 5 volts, but yeah, I don't know. Just when you're working on breadboard, just would have been nicer to have that. But hey, you can supply them from external power supply, no worries. But that is incredibly

**Dave Jones:** flexible, and that's very well done. A lot of effort has gone into designing that. A lot of thought. That would have taken a while. Awesome. From Switzerland to Sweden! Hi to all my Swedish viewers. This one comes from, oh I won't mention the company, because that might

**Dave Jones:** kind of be a bit of a spoiler. I still don't know what it is, but it sounds interesting. The name of the company sounds interesting anyway. So let's, oh sorry, this is like, this is a weird one. This is some weirdo thing happening here.

**Dave Jones:** Let's slice her open. Alright, that's better. Couple of boxes. Note, hi Dave! Turning these in line with email discussion. Oh! Right! Returned multimeters! Oh yes, I remember why! Yes, because he ordered two microcurrents and accidentally sent two multimeters. Sorry about that. Well, that's not really an interesting mail bag, is it?

**Dave Jones:** Back in the stock. So sorry, Thord! What an excellent Swedish name, Thord. Oh Swedish, I'm going to be called Thord. So thanks to everyone who sent something into today's mail bag. Sorry if yours is still on the shelf, I'm getting around to it.

**Dave Jones:** I had, I've got like over 30 items on the shelf, or I had before I started this, so I'm slowly getting around to it. Anyway, if you like mail bag, please give it a big thumbs up. Catch you next time. You are not going to believe what

**Dave Jones:** this puppy is. It is a little pocket open source Geiger counter. And this is one of the coolest things I've ever gotten in the mail bag. Check this out. Ta-da! Wow! Look, and yes you did hear a vibration motor there. It's a little Geiger counter slash

**Dave Jones:** digital dosimeter. It's called the Ultra Micron and isn't it cute? It's just absolutely tiny. This is the size of it compared to an Australian 50 cent piece.
