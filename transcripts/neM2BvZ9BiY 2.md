---
video_id: neM2BvZ9BiY
title: EEVblog #1202 - LCD Repair Redux
url: https://www.youtube.com/watch?v=neM2BvZ9BiY
source: youtube-asr
timestamps: {"0": 0, "1": 38, "2": 72, "3": 104, "4": 132, "5": 144, "6": 177, "7": 194, "8": 215, "9": 245, "10": 275, "11": 309, "12": 322, "13": 349, "14": 382, "15": 395, "16": 429, "17": 465, "18": 498, "19": 530, "20": 556, "21": 573, "22": 594, "23": 612, "24": 629, "25": 645, "26": 671, "27": 703, "28": 713, "29": 740, "30": 777, "31": 802, "32": 826, "33": 852, "34": 881, "35": 896, "36": 933, "37": 949, "38": 984, "39": 1019, "40": 1050, "41": 1081, "42": 1108, "43": 1135, "44": 1159, "45": 1176, "46": 1196, "47": 1217, "48": 1245, "49": 1276, "50": 1300, "51": 1320, "52": 1344, "53": 1363, "54": 1378, "55": 1416, "56": 1447, "57": 1464, "58": 1496, "59": 1520, "60": 1553, "61": 1567, "62": 1608, "63": 1634, "64": 1666, "65": 1679, "66": 1698, "67": 1728}
---

**Dave Jones:** Hi. Well, that didn't last very long, did it? If you remember the previous video where I attempted to repair the LCD on this PM300 three-phase power analyzer here. Yeah, what what what what I was able to repair it at the time, but it has returned as I kind of suspected in the video. I didn't know how long the repair would last and sure enough it lasted couple of weeks or something or a month and then it's like it's dead again. Unfortunately, there's no other way to really fix these hot bar

**Dave Jones:** attachable flat flexes inside this. You have to watch the previous video for all the details on that. Oh, they're often called tape automated bonding or tab connections and they famously fail in like the Fluke scopemeters and things like that. And sure enough in this particular module here. So really after it's failed that second time after after trying to reheat the conductive tape connections on there and it still doesn't work. There's not much you can do except get a replacement. So that's what I did.

**Dave Jones:** I went I got this one from Digikey. Actually, what was it $40? Something like that. It's actually a new It's not a one hung low brand. It's actually a New Haven display one and it uses the exact same chipset as the previous one and it's available in like different types. I wanted like a you know a nice white one or something like that, but unfortunately nobody stocked that at all. So I had to get the same I think I got the same yellow one. They had like a

**Dave Jones:** blue one. Didn't want wanky blue. So I've gone with the same one. So let's rip this thing apart again and see if we can whack this replacement in here. I'm going to have to put the header connector on it. I think it's on the same side. I hope it is cuz I've seen some of these replacement modules, you can actually buy them on eBay and they I've seen ones with the connector on the other side. So, that'd kind of ruin your day. Anyway, it does have a backlight, so we'll have to

**Dave Jones:** uh bodge that one on, but that's no worries. You can just solder the wires on if you really need to. You don't need a connection. This is what it looks like now. So, that's L A. We'll do an A B comparison. Uh-oh.

**Dave Jones:** I think this one is the one with the connector on this side cuz the numbers here, they're the right way up over here. I was going by the anode and the cathode over here. If you flip that around, all the writing is the correct orientation. And if you have a look at the data sheet, it does show it in this orientation. So, that means that the connector is on the opposite side, but it's not going to matter because A, it's a ribbon cable. B, it goes via this little plug-in card which

**Dave Jones:** joins the top board, wedges between the top board and the bottom board down here. It's a weird cube construction. And we can just take the cable over to the other side. This one here, all the text is upside down. So, that's interesting. Have they installed it upside down or flipped it in software?

**Dave Jones:** Because it's just a graphic LCD module. It's a 240 by 64 graphic LCD. But, hmm. Here's a serial board for those playing along at home. Old school EPROM and upside down all the electronics going to fall out. That's a Hitachi H8. Oh, Hitachi fanboys, still a couple of them around. They go wild.

**Dave Jones:** This design's a bloody mess, let me tell you. It's terrible. Anyway, let's get this out of here. I know we'll leave it attached, won't we? There we go. There's our module. And there the two boards. Here's the original. Here's the new Newhaven one. Of course, say don't use exactly the same chips, but they do use the same chipset, which is the most important thing, which is the protocol that the software talks to the thing with, and that's the RA 6963 like a chipset core. Although you can

**Dave Jones:** get that core in from many manufacturers, these are Toshiba chips up there, and these are in something. I have no idea. You can see that they are very similar, but they you know, there's differences as you'd expect. Like this one uses a cutout in the PCB here for the crystal up here. This one uses a more modern surface mount one. We've got some extra stuff around here. Looks like a extra power supply, maybe as that looks like some local regulation. That's a switching converter.

**Dave Jones:** Why else would you have the inductor down in there? Basically, it's exactly the same and it looks like pin one is in the same position cuz you note the red up here and matching pin one over here. So, it looks like they might have actually installed this upside down. I couldn't actually get a data sheet for this exact one cuz this number you Google it and you just get tons of generic compatible ones, and you can actually potentially buy cheaper than this Newhaven one. I think it was 50 55 US dollars, which is

**Dave Jones:** not particularly cheap, but this is a quite expensive power analyzer, and I want my display to work work properly and work reliably, and hopefully it'll be a nicer clearer display as well cuz the last one was pretty dull and wimpy.

**Dave Jones:** So, yeah, hopefully it'll be a nice upgrade. Can potentially get it cheaper. There was one seller on eBay, but they wanted like 120 US dollars postage, which is yeah, not untypical for Australia. Even for such a small thing. Yeah, they just couldn't be bothered shipping it for a reasonable cost. You know, don't necessarily blame them. Anyway, this is the cheapest one I could find was actually on Digikey, believe it or not.

**Dave Jones:** Even AliExpress and other places like that, nah, you know, we're talking like 100 bucks or something. This is quite a common module, the the 24064, which as I said is 240 by 64 graphic LCD. And any product that uses this particular one that uses the hot bar attachment, the tab, the tape automated bonding, we'll take it apart again and have a squeeze. Might have another play around with it and see if I can get it going just for kicks. But anyway, let's install this one. Might suck out the

**Dave Jones:** connector, otherwise I've got to find I could I'm sure I've got one here, like a suitable cable in the lab somewhere, but I'd have to find it. I think it's easier just to suck the old one out and then just resolder it straight into here.

**Dave Jones:** Meh. I could even potentially like cut off the ribbon and reterminate the ribbon if I actually I I shouldn't have a connector, but the lab still a mess. It still looks like that. So in there somewhere is the stuff I require. So might just be easier to unsolder. Desolder. I just said unsolder. What the I swear they've bodged a fan into this thing. There's a little piss-ant fan on the bottom of that. And look, they just like hot snotted down. They've just bodged some wires directly across the main filter

**Dave Jones:** caps there. I reckon that's a design afterthought. And as we showed in the previous video, there's the culprit right there. This is a hot bar or tab tape automated bonding process that uses a conductive adhesive down in here to actually connect that directly onto the PCB. And yeah, these things are just notoriously bad and you can try and heat them up and like press down at the same time, so sort of simulate that hot bar thing like pressing down and let it cool down in the flick repair video I used an

**Dave Jones:** a pencil eraser, didn't I? But if it doesn't take, then you're just better off scrapping it. And the new display doesn't actually have that. I won't take it apart, but if you look down in there, that's just the backlight. And if you look down the other end, it's just the other end of the backlight like that. So, they're obviously using much more connect many more connections, much more many more connections on the zebra strips along here, whereas the original one, tada, there's a lot of room even though the zebra strips go all

**Dave Jones:** the way with LBJ right up here. So, obviously the new LCD has got different routing physical routing on it and it allows them to utilize the space for those connections up there without having to have the ones on the end. And if yes, they could have just had another zebra strip on the end and been done with it, but they decided not to. So, they come a gata. That technology's just dodgy. And it's important to hold these boards upside down when you suck them off because gravity

**Dave Jones:** is a mongrel. And now, if the PCB designer didn't make those holes as tight as a nun's nasty, then we should be able to wiggle this loose. There will be a little bit of snap, crackle, and pop there. Might want to get in there and jiggle the individual pins one by one with a screwdriver. Just use the old finger.

**Dave Jones:** Wiggle, wiggle, wiggle, wiggle. Yeah, look at that. Beautiful, no pads lifted. Thank you very much. I'm a professional. All right, solder that onto the new display. Solder it on the lead connector. Hope that reaches. And it's good to go. Let's put it back together.

**Dave Jones:** That lead cable just reached. I had to sort of like even bend the connector a bit. Um going to power it on. Uh I haven't put the case back on yet, so let's give it a whirl. So, it's it is actually in upside down as per the previous one. So, let's give it a try. And nope, it doesn't like that. Bummer.

**Dave Jones:** What what what what? And get it got it out of there, disconnect the lead, and sure enough, it's uh like full contrast on everything. So, it's beautifully dark. I really like it. Fantastic compared to the other one, and it's supposed to be the same chipset.

**Dave Jones:** So, there's some sort of like a really marginal timing thing. Uh that'd be just my luck. Murphy, every time. No, hold on to your hat. All right, don't know if you can see that. I think you can just, but you can see the text on there.

**Dave Jones:** Beautiful. It's actually talking, so Houston, we just have a contrast problem, and that's excellent because we can fix a contrast problem. Is there a pot inside? So, this thing uh not working off the bat is a good thing.

**Dave Jones:** It means that we've got actually got something to do. It would have been boring video if it just worked off the bat. Now, uh to adjust the contrast, that's actually the VO pin, pin four on the connector here. Interestingly, they do have like a pot, an unpopulated potentiometer, that little surface mount jobby down there. So, I'm not sure what the deal is there. I haven't looked at the data sheet for this thing, but it doesn't really have any info on that.

**Dave Jones:** Have a look at what uh pin four is doing over here in terms of the contrast, and if we've got a pot inside this thing. So, let's whack it back open. Have a look. So, here's our driver board. Um so, this has just got a whole bunch of uh discrete 74 series logic. I don't see any pots on there, but I do see looks like a trimmer pot there or the a space for a trimmer pot. It's got two pins tied together, which is very common for a trimmer pot.

**Dave Jones:** So, I'm not sure if that has anything to do with it cuz the pins all the way over here and this is all the way over here. It doesn't kind of add up. And I don't see anything on the main board either.

**Dave Jones:** There's nothing hidden away in there, no sneaky little bugger. Nothing. I you'd expect it to be close to the to the board over there. Really see anything. So, it looks like the other one might have just been hardwired for the contrast, hence why uh this one is so out of whack. They specifically uh hardwired that for the previous one.

**Dave Jones:** Whether or not it's like uh two resistors, you know, it could have been those two down there setting it or, you know, who knows. All right, if we actually follow the money, on pin 1 2 3 4 there, snakes around there, goes over, drops down, and bingo, goes all the way with LBJ right around here, snaking right down to you guessed it, this area that we saw before. There's no resistor populated down in there, but it's near the pot here. So, aha, and of course the only

**Dave Jones:** reason that you would have a a trimmer pot on a board like this is for some sort of contrast adjust. So, maybe we can uh populate a pot in there and uh give it a tweak. And the data sheet says that uh the VO pin is nominally at minus 7.5 V and pin nine on the connector is the negative voltage generator of minus 10.

**Dave Jones:** So, I'm going to go pin two, which is ground. Let's have a look at pin four. Yeah, yeah. There you go, minus 11 volts. Yep, that's not terrific. Where's pin nine? Nine. Whoa. Don't short the pin. Oh, hello. Hello, we just saw it come good. Minus 10.2.

**Dave Jones:** Um, yeah. All right, so we need to adjust that. Maybe let's try the soldering in a trimmer pot, maybe. Geez, I've got to find one in the lab now. But, of course, the issue with doing that is uh the VZ in this case is actually coming from the main board over here. So, we sort of have to like either disconnect it from over here or change it over here. There's a couple of ways you can do it. You can, of course, do the contrast on the LCD board itself

**Dave Jones:** using its own uh supplied voltage. That's no problem, and then disconnect uh the wire. You can either snip it or disconnect it on the board over here or do whatever. Or, you can supply the voltage from over here. But, uh anyway, I might actually go back to that driver board and and just have a look where that pin's coming from. It's actually hard to see the uh traces here cuz they're on the top side. Pin one, two, three, four. And, if we trace pin four there, it actually snakes just along the

**Dave Jones:** top there. You can barely see it. But, it goes over to the zero ohm jumper link there. So, follow the money on the zero ohm link. It goes to that cap there. Goes to the negative of that cap.

**Dave Jones:** The good news with that is that if we generate the uh VZ, generate the contrast on the board, then we can just disconnect that jumper there. Excellent. So, I'm just going to uh disconnect that jumper. Um, just so that it in case this is a trace on there that I can't see is overriding that. And, maybe if you get lucky, the LCD might actually bias it to the correct uh value itself, but then again, it may not. The data sheet has no information on that whatsoever. So, if you can't reliably

**Dave Jones:** trace things that you're actually doing because it's a multi-layer board or whatever, you can't see the traces going off. I haven't like just hacking around little things like this that you can always put back is often a quick and easy way to do it. So, anyway, I've disconnected that.

**Dave Jones:** Let's see if that There you go. So, it was overriding that. It was making a difference. So, now we've got nothing. If I measure that V0 pin, we'll find that there's probably nothing like what we need on there. Yeah, 2.3 V. Nope. We need like minus Well, according to the data sheet, like a nominal minus 7.5 or thereabouts. So, we can potentially do that on the LCD board itself, which I'd prefer. I'd prefer to modify the LCD than modify that the driver board in there, I think. Meh, six of

**Dave Jones:** one, half dozen of the other. Okay, let's just have a squeeze around here. I've determined that this is the ground, of course. The positive is going to ground because these are negative voltages over here. So, it's fine. So, that those terminals aren't in reverse. So, don't worry about that. This one here is our negative 10.2. So, that's our generator. You'll see that goes down there, goes through that resistor over to this transistor over here. This pin here, 2.9. Well, that goes through that unpopulated resistor, and that is the

**Dave Jones:** trace that buggers off to our V0 pin to LCD drive, basically, which then will go somewhere else in the bias of the chips and everything else. But, we're going to feed it in at this point or at the connector over there. These two shorted terminals of our trimmer pot are actually connected to the this side of the resistor here. So, we've got our minus uh 10. We should be able to generate our minus seven by doing some funny business around here.

**Dave Jones:** And for those curious, that looks like an LM324 down in there. So, to generate the various uh bias levels for the LCD. Maybe if we populate that and the trimmer, that might do it. We might actually leave out the one going off to the pin cuz it looks like this is where it's doing the business. So, that's just a furphy. But like if you wanted to control it um externally from the board, I get But then how's it getting over? If that's not populated, how's it getting

**Dave Jones:** from pin four of the connector currently, where we saw all the dark contrast there? So, hmm maybe there is another trace buggering off somewhere uh from pin four, but I didn't see it. Okay, that might look a bit ugly, but I had ready access to through-hole just whacked in a 50 K pot in there without doing the other resistors and I've gone to the extreme ends of both ranges. It makes no difference. So, I'm going to whack that other one over there in series. I'll just

**Dave Jones:** whack in a 1 K. Meh, nice round value. Actually, I soldered it in a uh 1.2 K because you don't want to like blow your wad of 1 K resistors. If you've got like a like an 0603 resistor kit, 0805 resistor kit, 0402 resistor kits as you should have in any good lab. Uh you might have like 10 or 100 of each. You don't want to piss away all your like nice round 1 K. So, if you've got a value like this that doesn't matter. 1

**Dave Jones:** K, 1 K 2, doesn't matter. Take it from the 1 K 2. And what we've got now is the minus 10 volts that we had there, that's now being fed through via the resistor we soldered it in to the another resistor which is in series with this trimmer pot, which then could bugger off to the chip-set to do the contrast. So, that's the plan. Hello. Hey.

**Dave Jones:** Winner, winner, chicken dinner. There you go. Look at that. Beautiful. Now, the contrast isn't great because, of course, our trimmer pot could be anywhere. And once again, we haven't got the backlight. It's just flapping around in the breeze. So, let me see if we can make a difference.

**Dave Jones:** Well, that's interesting. I went to the extreme ends of uh the trim pot, both ends, and it did nothing. So, that's a consistent contrast. So, to anyway, we're we're getting somewhere. So, it maybe the 50K isn't enough. Maybe I shouldn't have put the 1K in series.

**Dave Jones:** Maybe I should have put like a 100K in series. Could be swamping it. Oops. Okay, what I did instead of the fixed resistor is I soldered in a 5K resistor, 5K trimmer on that resistor that was in series with this one. This one still does nothing, but ta-da! Winner, winner, chicken dinner.

**Dave Jones:** Look at that. That's beautiful. And yes, the 5K does adjust the contrast nicely, whereas the other trimmer one, which had the thing on here, um it doesn't adjust anything at all. So, I may uh whip that off, and I physically remove that trimmer, and what do you know? So, that trimmer was a furphy. Uh the obviously it has a purpose, but maybe uh like the external input and that uh transistor there. I don't know the configuration.

**Dave Jones:** Haven't bothered to uh trace it out. But look at that. That's beautiful. And that's with no backlight. Still flapping around in the breeze. The contrast on that is just fantastic. It was much better than the old one was, that's for sure. Worth the upgrade just right there in the uh contrast. I don't think we need a backlight, do we? Hm. And by the way, yes, the orientation is exactly the same as the other one. So, you'll notice like the text is obviously up the right way now, but the text on this side is

**Dave Jones:** like that. So, I believe that's the proper orientation. So, I think the software is actually flipping that for the purposes of cable management or doing whatever inside there. And that there's nothing wrong with that at all. That's fine. Now, of course, you can either leave that trimmer in there ordinarily like if you want to adjust it cuz that's it's just holding on by two pads there. It's a bit how you're doing.

**Dave Jones:** You'd normally like either do it nicer, like maybe mount it off on the side here, glue it down, run some little mod wires over there, and you know, do it nice and professional like that. Or you could just coat the whole thing in hot snot, and that would allow you to screw it without putting any pressure on the solder pads down there, which are tiny.

**Dave Jones:** They're only little 0605. There's going to be no stress on this thing whatsoever once it's in there. So, I I attempted just to leave it. Put some hot snot on there just to stop it flapping around in the breeze, but it's not going to flap around in the breeze. Of course, if this thing was on like a mobile trolley, test trolley, or something like that, you're wheeling it around all the time, sure you would sort of glue that down to stop it vibrating and stuff like that. But just

**Dave Jones:** for lab use, I don't know. Maybe I'll just put a bit of hot snot on it. So, for those curious about the adjustment range, goes all the way down like that. Depends on the angle. The angle on the Sorry about the uh screen reflections off the overhead lights. All that angle's pretty good. Fairly happy with that. And that is an after comparison.

**Dave Jones:** So, I'll try and put up the uh before and after shots there. And it the uh the film on the front of this actually um it kills the contrast a little bit. And yes, I do have the backlight on. Here you go.

**Dave Jones:** But wait, hold on to your hat. All of this may have been for zip. Thank you very much to Keen Mazels, who you've probably seen on the blog before. Anyway, he pointed out yes, I do upload this video early to patrons and supporters. He noticed I've had to come back and reshoot cuz he noticed that there's a driver transistor here inductor. What they're doing, this is very likely a software controlled contrast adjustment. Generating the voltage is not a fixed thing. And oh, that's really obvious, but I didn't

**Dave Jones:** think this thing had software contrast control. It's not in the firmware anyway. But if you RTFM, if you read the freaking manual, you'll see that there is actually after you power it on, you can actually press the arrow keys to adjust the contrast. So, I'm going to whack that back in and try that and and remove my trim pot and hopefully it'll have enough range. It may or may not, it's not guaranteed. All right, let's power it up. I've put that link back. I've removed my resistor.

**Dave Jones:** We've got our dark screen, but I'm supposed to be able to without touching any other keys, supposed to be able to press and hold this key. Oh, I can see it. Maybe I can stay there. No, it may not have may not have the range. Yeah, yeah, it's going darker. Yeah, it doesn't have the range.

**Dave Jones:** That wasn't a solution. So, that wasn't a lost cause going through all that. There you go. It just doesn't have the range. Wow, so the designers just didn't cater for the fact that there would be other unfortunately just putting the pot back and leaving that link in place. I thought I might be able to be clever and actually change the range of that, but yeah, no. Maybe I can get in there and trim it a bit, but it's annoying. So, what I want to try and do is actually get um, electronic

**Dave Jones:** control and I've only got very partial electronic control with the original configuration in there. And if I put the trimmer in there, it doesn't really help. But, watch this. If I put the trimmer across pins one and four, which is the V0, so if I load down the V0, watch this. Get the tongue at the right angle.

**Dave Jones:** Look at that. I can adjust the contrast electronically. Fantastic. And of course, you don't really want a trimmer pot in there that we've got electronic control now. So, if we have a look at the resistance value, 4.3k. All right, no worries. So, that seems to be a reasonable value. So, I'll just whack in a 4.7k either directly across the pins in there, but then that could short out to the front panel. Maybe I could do it in there cuz the trace comes all the way here. So, between there and ground. And

**Dave Jones:** that should do it. And that will have full electronic control. Beauty. So, there you go. Got a resistor from that point around to the ground of the cap over there. So, let's see if that does the business. Ta-da!

**Dave Jones:** Fantastic. Yes, of course we didn't have to be 4.3, but 4.3 happens to be exactly an E24 value that I had in my kit. A 3K9 might have worked, but it looks like that range is fan-freaking-tastic. Look at that. Ah, beautiful. And there you have it. We now have a perfect replacement fully installed with electronic contrast control. Fantastic. But, it didn't We We had to fight for that. It didn't just happen like off the shelf. Just put in a module because there's variations in the In this case, the contrast voltage range

**Dave Jones:** in the actual product. So, yeah, that was actually I was hoping for something interesting like that at least. I didn't would have been disappointed if it just worked, right? So, there you go. I hope you enjoyed that little repair redux there that we had to go back and fix our repair, you know, like a month later it was gone again. A lot of people in the comments said, "Yeah, it's not going to last." And it like apparently people don't even bother to fix these things. They just simply

**Dave Jones:** buy the replacement module. It's not worth the grief. So, these things are just horrible. These are hot bar you know, tape tab or tape automated bonding connections. Just a pain in the butt. So, the new one avoids that of course as I said by having the extra contacts on the unused areas of the zebra strips here and you can see you can see the contacts. Many more so the new one would have many more contacts along there and along there as well which allows it to do away with

**Dave Jones:** that. And these things fail in all sorts of things. I think they use them like in you know, LCD TVs and all sorts of stuff. The technology is probably better these days, but this is from like 2000. Of course there's lots of products.

**Dave Jones:** People are talking about the same failures in Game Boys. I've seen it in Fluke. It's very famous in Fluke scope meters back in the day. I've done a video fixing that as well. And ultimately it's going to be a band-aid fix hit or miss. Some people said they've never been able to repair these things and and that's not surprising.

**Dave Jones:** So, I don't think there's any magic bullet. You can actually get in there maybe scrape away everything if you're absolutely desperate and it was some weird custom module or something. You can get in there and scrape away the contacts and actually wire them little mod wires over to each one down to the contacts, down to the pads down in there, but jeez, yeah. You'd have to be pretty desperate. So, anyway, if you like that video, please give it a big thumbs up. And as always, discuss in the

**Dave Jones:** comments and over on the EEVblog forum. Catch you next time.
