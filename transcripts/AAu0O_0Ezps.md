---
video_id: AAu0O_0Ezps
title: EEVblog #185 - Fluke 87V Multimeter GSM Fix!
url: https://www.youtube.com/watch?v=AAu0O_0Ezps
source: youtube-asr
timestamps: {"0": 0, "1": 18, "2": 31, "3": 46, "4": 61, "5": 80, "6": 91, "7": 104, "8": 119, "9": 134, "10": 149, "11": 164, "12": 178, "13": 197, "14": 215, "15": 232, "16": 247, "17": 262, "18": 282, "19": 296, "20": 313, "21": 330, "22": 343, "23": 360, "24": 374, "25": 390, "26": 404, "27": 417, "28": 432, "29": 447, "30": 461, "31": 478, "32": 490, "33": 501, "34": 519, "35": 533, "36": 549, "37": 564, "38": 580, "39": 597, "40": 609, "41": 622, "42": 635, "43": 655, "44": 672, "45": 687, "46": 712, "47": 725, "48": 739, "49": 755, "50": 771, "51": 793, "52": 812, "53": 826, "54": 837, "55": 852, "56": 870, "57": 886, "58": 904, "59": 921, "60": 936, "61": 949, "62": 966, "63": 981, "64": 995, "65": 1008, "66": 1032}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, back in October last year, quite a while ago, I showed the GSM mobile phone phone Fluke video thing,

**Dave Jones:** where if you put your GSM mobile phone next to a Fluke 87 5 multimeter, you could kill it. You could brick the thing, erase the firmware inside. I wasn't able to do it, but it did happen to someone, and Fluke

**Dave Jones:** said they'd look into it, take it seriously, and fix it. And I haven't really heard anything out of them for well, basically since then. And on just the other blog the other week, I sort of said, "Hey, Fluke,

**Dave Jones:** what's happening?" They got back to me straight away, and they said, "Hi, don't worry, we have been working on it, and we have fixed it. In fact, not only have they fixed it, they've given me as a world exclusive, basically, uh they've

**Dave Jones:** given me a pre-production prototype unit that actually fixes the problem. Fantastic. I can't believe a big company like Fluke would actually uh let me show, and I'm going to take it apart and everything, show a pre-production unit. Fantastic. It shows they're serious. You

**Dave Jones:** will actually be able to buy this fixed Fluke 87 5 in a couple of months' time, I believe it is. Don't quote me on that, but yeah, they will. It's not going to change. It's going to be exactly the

**Dave Jones:** same Fluke 87 5, except it's got a new revision PCB in here, which fixes the GSM mobile phone issue. Fantastic. Let's take a look at it. And once I get them open, here are the two units side by

**Dave Jones:** side. On the right-hand side here, we've got the new revision 11 unit, and the prototype one, and on the left, we have my old revision 9 unit. I know some people have the revision 10 PCB unit, but mine's up quite, you know, it's like

**Dave Jones:** 5 or 6 years old at least this meter that I've got here, but yeah, they're identical. You can see a color difference in the LCDs, and they've obviously changed the type of LCD Well, they changed the actual LCD they've used

**Dave Jones:** slightly as you'd expect. You know, the amount of time between these two units, they've probably refined quite a few things, but there really is essentially no difference at all. And if we take the top unit off like this, I've already

**Dave Jones:** unscrewed it, then we can get straight down to the board and compare the differences. We'll take a quick look at the backside here, and as you can see the shielding is absolutely identical between the two units, no difference at all. The

**Dave Jones:** tracking seems to be exactly the same. How all the speaker and everything works is exactly the same, and if we take off the shields, which have little clips on them, then we'll be able to see that there is

**Dave Jones:** no difference at all on the bottom of the boards, but the the actual type of mask solder mask used on this new revision PCB is actually different. It's less it's more opaque. You can't really see through it like the tracks really don't stand out

**Dave Jones:** like they do on the old one, but as you can see, it is actually an identical layout. I can see very few differences at all in the actual tracking. In fact, I I think there's essentially none. Actually, I think the top and bottom, as

**Dave Jones:** we'll see on the top side, there's a couple of little extra vias up the top here, but really the two boards are as identical as you can possibly get them. As you can see on the new board here, it

**Dave Jones:** is, rev 11 down there, and it's a It's got a a qualification sticker on it. I'm not actually sure what that is, but this is a pre-production unit. Hasn't actually gone into production yet, but I expect it will be absolutely identical to the

**Dave Jones:** one you'll be able to buy in a couple of months time. And my old board over here, as you can see, it's a rev 009. It's a rev 9 board. Um so, it's reasonably old. As I said, there is a rev 10 out there

**Dave Jones:** now. Let's take a look at the differences. Are there any? Effectively, uh basically, nothing on the bottom side. I've taken a reasonably careful look at them, and there really is nothing to speak of in the input circuitry, in in that uh circuitry in

**Dave Jones:** the middle there. It's only around the processor up the top, as you'd expect, cuz that's where we had our RF sensitivity problem. I forgot to mention one item here. This uh tantalum cap here is actually been moved up on this new

**Dave Jones:** one, as you can see, and there's two unpopulated new unpopulated footprints there. So, that is a minor change on the new board to that uh middle circuitry. But, up here on the top, as you'll see, there are quite a few uh differences.

**Dave Jones:** Let's play spot the difference. Now, I can see one extra capacitor there that's not over here like that. It's to do with that resistor there. So, maybe that's some sort of uh low-pass extra uh low-pass filtering or uh something like

**Dave Jones:** that, perhaps. I can see an extra resistor added here that's not over here. Now, they've changed this in the footprint of this device. Um I don't think that's of any significance. It's probably just that uh this one's more

**Dave Jones:** readily available or something, perhaps. But, apart from that, if you remember from the GSM video, this left-hand side of the board here was the one that was sensitive. So, uh really they've only added um the two extra components there.

**Dave Jones:** All of the main differences, I don't see any differences around here at all. No differences there, but all of the difference um the main difference seems to be over here. They've got all these extra uh passives. There's a couple extra

**Dave Jones:** resistors and a couple extra capacitors up here like this. Now, um whereas before, this is the previous board and it had some unpopulated uh pads there. So, there were supposed to be components there, but they left them off for I don't know, whatever

**Dave Jones:** reason you can uh think of. It would require Fluke to actually tell us that, but um they've actually changed the layout slightly and there's definitely um you know, four or five extra components there. Now, this is the JTAG

**Dave Jones:** uh interface for the processor, and I think uh back at the time of the GSM video, somebody guessed that it may have had something to do with uh you know, locking up the JTAG and reprogramming and reflashing the unit

**Dave Jones:** accidentally or something like that. And that's probably the most viable um explanation or something like that. But, I can't see that there's any change into that. I can't see that those components are actually related to the JTAG interface at all because the traces for

**Dave Jones:** these JTAG pins just go straight onto the processor. Um so, really, you know, I I I can't see any difference in the tracking there at all. They seem to have done all the tracking on the inner layers, and um if you have a look at the

**Dave Jones:** uh bottom uh of the bottom side of the board as well, um the the tracking's pretty much um identical on on the bottom sides of the board as well. They've just added in the extra components. So, they've done well to

**Dave Jones:** keep the existing layout absolutely uh um spot-on and just add the extra components in there and possibly trace them on the internal layer. So, there you go. That's the difference. They've added a couple of extra parts. It's exactly the same um MSP430

**Dave Jones:** processor. There's no real difference there. Uh and if you want to see the high-res uh photos, I'll actually link those. They're up on my Flickr account. So, you can actually, if you're really keen, you can go in there and

**Dave Jones:** have a look at the high-res photos yourself and see the differences. But really, they've just added a few extra components and uh that's about it. There's just a close-up view of the markings on the new Rev 11 board.

**Dave Jones:** They've still got copyright 2002 Fluke. And my older board, as you can see, uh there it is, the Rev 9. And uh really, there's apart from that, there's very few differences on the top um side here. Here's the actual uh new serial number

**Dave Jones:** sticker. Now, curiously, they're actually calling it a Rev X. So, you know, a Rev 10. But the actual PCB is Rev 11. And if you're curious about what's under the range switch, then well, it hasn't changed at all. And that

**Dave Jones:** includes the two um uh the actual uh contacts themselves. They're um identical. They haven't changed the build there at all. Have they taken the opportunity to uh tweak the design in any other way? No. Well, inside is exactly the same. They

**Dave Jones:** still use the uh the you know, the crusty old 9-V battery snap, which uh the wiring actually goes under the under the main fuse like that. And they haven't added a fuse compartment access. You still have to undo the screws of the

**Dave Jones:** case to get at the fuses. Those little annoying uh quirks of the 87 that uh if they fixed those, they would, you know, it would be the perfect uh meter, almost. But um they have changed those things on the Fluke 28 Series II. So,

**Dave Jones:** which is basically a Fluke 87 V in a new ruggedized redesigned package which uses a nice AA battery compartment with fuse access. But, yeah, they haven't really tweaked the design at all. Now, they have actually changed the back

**Dave Jones:** tooling of the case here and they have actually taken off the TUV mark. This is the old my old meter and this is the new one. There's now no TUV mark there. I'm not sure what the deal is. And now it

**Dave Jones:** says made in USA of US and non-US parts. Why did you have to put that? To be politically correct? Just to meet the letter of the law? Crazy. I don't know. It's made in the US, it's made in the

**Dave Jones:** US. Everyone knows all the parts come from bloody China. Geez. And curiously, they've taken off the patents as well. What? Have the patents expired? I don't know. And it still has this ridiculous thing referred to the manual for

**Dave Jones:** additional capabilities. Why don't you just print the capabilities on there for goodness sake? And there's absolutely no differences on the internal molding of the case or the piezo transducer there. Absolutely nothing. Identical. And you can probably see the slightly

**Dave Jones:** greener tinge here on the new display. It's got that more of that old school green LCD tinge to it. And dare I say, they've actually thickened up the digits possibly a tad. They these ones look a little bit

**Dave Jones:** thicker than my older ones here and the contrast seems much better, especially on the high angle like this. It's I think that's a bit hard to get on camera there, but they seem to improved the contrast a bit, which is great.

**Dave Jones:** One difference I did notice is the beep. The beep has actually changed. I'll see if we can get it here. Listen. beep The new one is definitely softer and a slightly different pitch. The old one was much louder. And they haven't fixed

**Dave Jones:** another annoying quirk which I didn't like is that the backlight comes on when you switch to 4 and 1/2 digit mode. Watch this. And it still does it on the new one.

**Dave Jones:** Why? It just takes a gulp of battery current when you do that. Crazy. Just pissing away the current. And if you're interested in the backlights, there is a minor difference. I probably prefer the old one, but uh there's there's really

**Dave Jones:** nothing in it. But the contrast is much nicer, I think, on the new one using the backlight, especially the high angle here where it starts to vanish. You'll notice that the other one is vanishing, whereas the new one stays much sharper.

**Dave Jones:** So, the LCD is much improved. And now for the big test everyone wants to see. Here's my old one. Here's the new one. Got my phone here. Let's try it. Yep. The old one still plays up. There it is.

**Dave Jones:** Still goes burko a bit. And let's try the new one. Nope. Exactly the same thing. Seems not solid.

**Dave Jones:** No problem at all. The audio is probably horrible. It's uh the phone is no doubt interfering with the audio. That's uh 218 hertz interference there from the GSM. But no, the meter works as you'd expect. Flick have fixed it. Beauty.

**Dave Jones:** And just for kicks, I'll try my UHF walkie-talkie I've got here. This didn't actually cause the problem last time, but I'll actually key it. And this is the old meter, by the way, and you can see the bar graph there go up as I

**Dave Jones:** as I actually key the mic in like that. And it doesn't kill it, but let's take a look at the new one and see if it does the same thing. Uh well, let's switch it to millivolts like we had the other one

**Dave Jones:** on. There we go. The bar graph goes up exactly the same, so it's it's still, you know, it's it's not going to be completely immune to all RF. That's crazy. It does it does actually have a spec for that, but yeah, it

**Dave Jones:** certainly doesn't crash with something like this half-watt walkie-talkie basically transmitting right on top. And I thought I'd just show you the new Fluke TL 175 probes that they're supplying with the meter now. They They aren't supp- I don't

**Dave Jones:** believe they're supplying these old TL 75. It's been replaced by this TL 175 because of the new regulations, the new CAT regulations. It's actually got a switchable See that? It actually switches around and actually it's got a shroud which comes out and

**Dave Jones:** actually protects the exposed end like that because in I apparently, you in to actually meet the CAT four requirement, you need to have that shroud on your meter. So, this one in There it is in CAT three and CAT four

**Dave Jones:** position, it's got the shroud. In CAT two position, it doesn't have it. So, that's just a a sort of a more of a legal requirement to actually meet the requirements of of the CAT or UL or who whoever actually

**Dave Jones:** uh, handles those sort of things. So, they are new probes and if you compare it with the old one, it is much longer. Um, I I much prefer the shorter, uh, probes. I much prefer the older one in terms of, uh, handling, but the, um,

**Dave Jones:** the in in terms of the strain relief on the cable at the end is very nice indeed. Um, yeah, I'm not sure I'm a big fan of the, uh, of the shroud that comes out like that. I don't know. It'll

**Dave Jones:** probably just wear out eventually, but, uh, yeah, there is, um, sharp as I always have been really and, uh, they differ on the meter itself. As you can see, they're got much longer, uh, exit for the cable coming out of the,

**Dave Jones:** uh, right angle right angle connector there and as with the top end, they're very nicely the rubber on that is, it's beautiful, but once again, I don't know if I'm a big fan of having them actually stick out. Uh, that farther, it

**Dave Jones:** just, uh, not as nice and compact as the old style one. So, I don't know. I'm in two minds, but there you go. That's a new Fluke TL175 probe. There you go. Fluke actually fixed it and they did it reasonably quickly in

**Dave Jones:** the scheme of things. Uh, for a huge company like that to spin a new revision PCB and test it for the world's pretty much the world's, uh, leading multimeter, that's that's quite good work and so thanks for Fluke for letting

**Dave Jones:** us actually show you this. I'm not aware big company that would actually have the guts to show a pre-production prototype like that. It shows that they're damn serious. I love it. Thanks, Fluke. See you next time.

**Dave Jones:** And remember, if you're going to try this at home, wear protection.
