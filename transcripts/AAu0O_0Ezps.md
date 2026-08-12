---
video_id: AAu0O_0Ezps
title: EEVblog #185 - Fluke 87V Multimeter GSM Fix!
url: https://www.youtube.com/watch?v=AAu0O_0Ezps
source: youtube-asr
timestamps: {"0": 0, "1": 23, "2": 33, "3": 52, "4": 67, "5": 78, "6": 87, "7": 96, "8": 111, "9": 124, "10": 142, "11": 162, "12": 188, "13": 202, "14": 230, "15": 240, "16": 253, "17": 266, "18": 282, "19": 301, "20": 313, "21": 330, "22": 339, "23": 354, "24": 370, "25": 384, "26": 401, "27": 417, "28": 436, "29": 458, "30": 470, "31": 484, "32": 491, "33": 504, "34": 516, "35": 527, "36": 539, "37": 558, "38": 574, "39": 590, "40": 599, "41": 614, "42": 622, "43": 635, "44": 651, "45": 670, "46": 687, "47": 707, "48": 718, "49": 729, "50": 747, "51": 760, "52": 774, "53": 797, "54": 814, "55": 829, "56": 837, "57": 847, "58": 868, "59": 883, "60": 900, "61": 921, "62": 941, "63": 956, "64": 978, "65": 991, "66": 1008, "67": 1032}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, back in October last year, quite a while ago, I showed the GSM mobile phone phone Fluke video thing, where if you put your GSM mobile phone next to a Fluke 87 5 multimeter, you could kill it.

**Dave Jones:** You could brick the thing, erase the firmware inside. I wasn't able to do it, but it did happen to someone, and Fluke said they'd look into it, take it seriously, and fix it.

**Dave Jones:** And I haven't really heard anything out of them for well, basically since then. And on just the other blog the other week, I sort of said, "Hey, Fluke, what's happening?" They got back to me straight away, and they said, "Hi, don't worry, we have been working on it, and we have fixed it.

**Dave Jones:** In fact, not only have they fixed it, they've given me as a world exclusive, basically, uh they've given me a pre-production prototype unit that actually fixes the problem. Fantastic.

**Dave Jones:** I can't believe a big company like Fluke would actually uh let me show, and I'm going to take it apart and everything, show a pre-production unit. Fantastic. It shows they're serious.

**Dave Jones:** You will actually be able to buy this fixed Fluke 87 5 in a couple of months' time, I believe it is. Don't quote me on that, but yeah, they will.

**Dave Jones:** It's not going to change. It's going to be exactly the same Fluke 87 5, except it's got a new revision PCB in here, which fixes the GSM mobile phone issue.

**Dave Jones:** Fantastic. Let's take a look at it. And once I get them open, here are the two units side by side. On the right-hand side here, we've got the new revision 11 unit, and the prototype one, and on the left, we have my old revision 9 unit.

**Dave Jones:** I know some people have the revision 10 PCB unit, but mine's up quite, you know, it's like 5 or 6 years old at least this meter that I've got here, but yeah, they're identical.

**Dave Jones:** You can see a color difference in the LCDs, and they've obviously changed the type of LCD Well, they changed the actual LCD they've used slightly as you'd expect. You know, the amount of time between these two units, they've probably refined quite a few things, but there really is essentially no difference at all.

**Dave Jones:** And if we take the top unit off like this, I've already unscrewed it, then we can get straight down to the board and compare the differences. We'll take a quick look at the backside here, and as you can see the shielding is absolutely identical between the two units, no difference at all.

**Dave Jones:** The tracking seems to be exactly the same. How all the speaker and everything works is exactly the same, and if we take off the shields, which have little clips on them, then we'll be able to see that there is no difference at all on the bottom of the boards, but the the actual type of mask solder mask used on this new revision PCB is actually different.

**Dave Jones:** It's less it's more opaque. You can't really see through it like the tracks really don't stand out like they do on the old one, but as you can see, it is actually an identical layout.

**Dave Jones:** I can see very few differences at all in the actual tracking. In fact, I I think there's essentially none. Actually, I think the top and bottom, as we'll see on the top side, there's a couple of little extra vias up the top here, but really the two boards are as identical as you can possibly get them.

**Dave Jones:** As you can see on the new board here, it is, rev 11 down there, and it's a It's got a a qualification sticker on it. I'm not actually sure what that is, but this is a pre-production unit.

**Dave Jones:** Hasn't actually gone into production yet, but I expect it will be absolutely identical to the one you'll be able to buy in a couple of months time. And my old board over here, as you can see, it's a rev 009.

**Dave Jones:** It's a rev 9 board. Um so, it's reasonably old. As I said, there is a rev 10 out there now. Let's take a look at the differences. Are there any?

**Dave Jones:** Effectively, uh basically, nothing on the bottom side. I've taken a reasonably careful look at them, and there really is nothing to speak of in the input circuitry, in in that uh circuitry in the middle there.

**Dave Jones:** It's only around the processor up the top, as you'd expect, cuz that's where we had our RF sensitivity problem. I forgot to mention one item here. This uh tantalum cap here is actually been moved up on this new one, as you can see, and there's two unpopulated new unpopulated footprints there.

**Dave Jones:** So, that is a minor change on the new board to that uh middle circuitry. But, up here on the top, as you'll see, there are quite a few uh differences.

**Dave Jones:** Let's play spot the difference. Now, I can see one extra capacitor there that's not over here like that. It's to do with that resistor there. So, maybe that's some sort of uh low-pass extra uh low-pass filtering or uh something like that, perhaps.

**Dave Jones:** I can see an extra resistor added here that's not over here. Now, they've changed this in the footprint of this device. Um I don't think that's of any significance.

**Dave Jones:** It's probably just that uh this one's more readily available or something, perhaps. But, apart from that, if you remember from the GSM video, this left-hand side of the board here was the one that was sensitive.

**Dave Jones:** So, uh really they've only added um the two extra components there. All of the main differences, I don't see any differences around here at all. No differences there, but all of the difference um the main difference seems to be over here.

**Dave Jones:** They've got all these extra uh passives. There's a couple extra resistors and a couple extra capacitors up here like this. Now, um whereas before, this is the previous board and it had some unpopulated uh pads there.

**Dave Jones:** So, there were supposed to be components there, but they left them off for I don't know, whatever reason you can uh think of. It would require Fluke to actually tell us that, but um they've actually changed the layout slightly and there's definitely um you know, four or five extra components there.

**Dave Jones:** Now, this is the JTAG uh interface for the processor, and I think uh back at the time of the GSM video, somebody guessed that it may have had something to do with uh you know, locking up the JTAG and reprogramming and reflashing the unit accidentally or something like that.

**Dave Jones:** And that's probably the most viable um explanation or something like that. But, I can't see that there's any change into that. I can't see that those components are actually related to the JTAG interface at all because the traces for these JTAG pins just go straight onto the processor.

**Dave Jones:** Um so, really, you know, I I I can't see any difference in the tracking there at all. They seem to have done all the tracking on the inner layers, and um if you have a look at the uh bottom uh of the bottom side of the board as well, um the the tracking's pretty much um identical on on the bottom sides of the board as well.

**Dave Jones:** They've just added in the extra components. So, they've done well to keep the existing layout absolutely uh um spot-on and just add the extra components in there and possibly trace them on the internal layer.

**Dave Jones:** So, there you go. That's the difference. They've added a couple of extra parts. It's exactly the same um MSP430 processor. There's no real difference there. Uh and if you want to see the high-res uh photos, I'll actually link those.

**Dave Jones:** They're up on my Flickr account. So, you can actually, if you're really keen, you can go in there and have a look at the high-res photos yourself and see the differences.

**Dave Jones:** But really, they've just added a few extra components and uh that's about it. There's just a close-up view of the markings on the new Rev 11 board. They've still got copyright 2002 Fluke.

**Dave Jones:** And my older board, as you can see, uh there it is, the Rev 9. And uh really, there's apart from that, there's very few differences on the top um side here.

**Dave Jones:** Here's the actual uh new serial number sticker. Now, curiously, they're actually calling it a Rev X. So, you know, a Rev 10. But the actual PCB is Rev 11.

**Dave Jones:** And if you're curious about what's under the range switch, then well, it hasn't changed at all. And that includes the two um uh the actual uh contacts themselves. They're um identical.

**Dave Jones:** They haven't changed the build there at all. Have they taken the opportunity to uh tweak the design in any other way? No. Well, inside is exactly the same. They still use the uh the you know, the crusty old 9-V battery snap, which uh the wiring actually goes under the under the main fuse like that.

**Dave Jones:** And they haven't added a fuse compartment access. You still have to undo the screws of the case to get at the fuses. Those little annoying uh quirks of the 87 that uh if they fixed those, they would, you know, it would be the perfect uh meter, almost.

**Dave Jones:** But um they have changed those things on the Fluke 28 Series II. So, which is basically a Fluke 87 V in a new ruggedized redesigned package which uses a nice AA battery compartment with fuse access.

**Dave Jones:** But, yeah, they haven't really tweaked the design at all. Now, they have actually changed the back tooling of the case here and they have actually taken off the TUV mark.

**Dave Jones:** This is the old my old meter and this is the new one. There's now no TUV mark there. I'm not sure what the deal is. And now it says made in USA of US and non-US parts.

**Dave Jones:** Why did you have to put that? To be politically correct? Just to meet the letter of the law? Crazy. I don't know. It's made in the US, it's made in the US.

**Dave Jones:** Everyone knows all the parts come from bloody China. Geez. And curiously, they've taken off the patents as well. What? Have the patents expired? I don't know. And it still has this ridiculous thing referred to the manual for additional capabilities.

**Dave Jones:** Why don't you just print the capabilities on there for goodness sake? And there's absolutely no differences on the internal molding of the case or the piezo transducer there. Absolutely nothing.

**Dave Jones:** Identical. And you can probably see the slightly greener tinge here on the new display. It's got that more of that old school green LCD tinge to it. And dare I say, they've actually thickened up the digits possibly a tad.

**Dave Jones:** They these ones look a little bit thicker than my older ones here and the contrast seems much better, especially on the high angle like this. It's I think that's a bit hard to get on camera there, but they seem to improved the contrast a bit, which is great.

**Dave Jones:** One difference I did notice is the beep. The beep has actually changed. I'll see if we can get it here. Listen. beep The new one is definitely softer and a slightly different pitch.

**Dave Jones:** The old one was much louder. And they haven't fixed another annoying quirk which I didn't like is that the backlight comes on when you switch to 4 and 1/2 digit mode.

**Dave Jones:** Watch this. And it still does it on the new one. Why? It just takes a gulp of battery current when you do that. Crazy. Just pissing away the current.

**Dave Jones:** And if you're interested in the backlights, there is a minor difference. I probably prefer the old one, but uh there's there's really nothing in it. But the contrast is much nicer, I think, on the new one using the backlight, especially the high angle here where it starts to vanish.

**Dave Jones:** You'll notice that the other one is vanishing, whereas the new one stays much sharper. So, the LCD is much improved. And now for the big test everyone wants to see.

**Dave Jones:** Here's my old one. Here's the new one. Got my phone here. Let's try it. Yep. The old one still plays up. There it is. Still goes burko a bit.

**Dave Jones:** And let's try the new one. Nope. Exactly the same thing. Seems not solid. No problem at all. The audio is probably horrible. It's uh the phone is no doubt interfering with the audio.

**Dave Jones:** That's uh 218 hertz interference there from the GSM. But no, the meter works as you'd expect. Flick have fixed it. Beauty. And just for kicks, I'll try my UHF walkie-talkie I've got here.

**Dave Jones:** This didn't actually cause the problem last time, but I'll actually key it. And this is the old meter, by the way, and you can see the bar graph there go up as I as I actually key the mic in like that.

**Dave Jones:** And it doesn't kill it, but let's take a look at the new one and see if it does the same thing. Uh well, let's switch it to millivolts like we had the other one on.

**Dave Jones:** There we go. The bar graph goes up exactly the same, so it's it's still, you know, it's it's not going to be completely immune to all RF. That's crazy.

**Dave Jones:** It does it does actually have a spec for that, but yeah, it certainly doesn't crash with something like this half-watt walkie-talkie basically transmitting right on top. And I thought I'd just show you the new Fluke TL 175 probes that they're supplying with the meter now.

**Dave Jones:** They They aren't supp- I don't believe they're supplying these old TL 75. It's been replaced by this TL 175 because of the new regulations, the new CAT regulations. It's actually got a switchable See that?

**Dave Jones:** It actually switches around and actually it's got a shroud which comes out and actually protects the exposed end like that because in I apparently, you in to actually meet the CAT four requirement, you need to have that shroud on your meter.

**Dave Jones:** So, this one in There it is in CAT three and CAT four position, it's got the shroud. In CAT two position, it doesn't have it. So, that's just a a sort of a more of a legal requirement to actually meet the requirements of of the CAT or UL or who whoever actually uh, handles those sort of things.

**Dave Jones:** So, they are new probes and if you compare it with the old one, it is much longer. Um, I I much prefer the shorter, uh, probes. I much prefer the older one in terms of, uh, handling, but the, um, the in in terms of the strain relief on the cable at the end is very nice indeed.

**Dave Jones:** Um, yeah, I'm not sure I'm a big fan of the, uh, of the shroud that comes out like that. I don't know. It'll probably just wear out eventually, but, uh, yeah, there is, um, sharp as I always have been really and, uh, they differ on the meter itself.

**Dave Jones:** As you can see, they're got much longer, uh, exit for the cable coming out of the, uh, right angle right angle connector there and as with the top end, they're very nicely the rubber on that is, it's beautiful, but once again, I don't know if I'm a big fan of having them actually stick out.

**Dave Jones:** Uh, that farther, it just, uh, not as nice and compact as the old style one. So, I don't know. I'm in two minds, but there you go. That's a new Fluke TL175 probe.

**Dave Jones:** There you go. Fluke actually fixed it and they did it reasonably quickly in the scheme of things. Uh, for a huge company like that to spin a new revision PCB and test it for the world's pretty much the world's, uh, leading multimeter, that's that's quite good work and so thanks for Fluke for letting us actually show you this.

**Dave Jones:** I'm not aware big company that would actually have the guts to show a pre-production prototype like that. It shows that they're damn serious. I love it. Thanks, Fluke. See you next time.

**Dave Jones:** And remember, if you're going to try this at home, wear protection.
