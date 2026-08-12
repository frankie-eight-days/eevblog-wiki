---
video_id: WTkrk2blxhY
title: EEVblog #547 - Dumpster Phone Teardown
url: https://www.youtube.com/watch?v=WTkrk2blxhY
source: youtube-asr
timestamps: {"0": 1, "1": 16, "2": 27, "3": 38, "4": 54, "5": 67, "6": 81, "7": 95, "8": 108, "9": 119, "10": 134, "11": 148, "12": 159, "13": 171, "14": 186, "15": 200, "16": 220, "17": 235, "18": 247, "19": 262, "20": 279, "21": 292, "22": 305, "23": 320, "24": 331, "25": 349, "26": 366, "27": 379, "28": 396, "29": 412, "30": 425, "31": 445, "32": 463, "33": 475, "34": 487, "35": 497, "36": 510, "37": 523, "38": 534, "39": 548, "40": 560, "41": 572, "42": 585, "43": 599, "44": 611, "45": 628, "46": 645, "47": 662, "48": 677, "49": 693, "50": 706, "51": 717, "52": 736, "53": 750, "54": 766, "55": 780, "56": 793, "57": 809, "58": 826, "59": 845, "60": 861, "61": 877, "62": 890, "63": 905, "64": 925}
---

**Dave Jones:** Hi, welcome to some dumpster diving teardown / salvage time. We've got some uh various office phone and internet uh protocol IP phones here courtesy of uh John who sent them into the previous mailbag video which I'll link in down

**Dave Jones:** below if you haven't seen it. And I um scored this one from my uh dumpster here in the EEVblog towers. It's a Panasonic one. So I thought we'd just open them all up uh quite quickly. Won't be very

**Dave Jones:** thorough teardown and see uh what's inside these things and see if there's any usable parts. Because you might be able to find these, you know, a company shuts down or whatever. Uh they just tend to toss these things out all the

**Dave Jones:** time. So is there anything worthy in them? We'll find out. First up, this Panasonic one that I found at model number KX-T7433. And it's your typical uh you know, system PABX uh type phone you might have in office. Lots of uh you know,

**Dave Jones:** pre-dialed numbers and stuff like that. And you know, it it does a few things but nothing particularly uh fancy at all. LCD display we might be able to salvage. And it even tells you, there it is, digital proprietary telephone. Made

**Dave Jones:** in Malaysia this sucker. Let's crack it open. Here it is. Pretty much what I expected. All uh single board construction. We've got the lever coming down here. Looks like to a micro switch down on the board like that. We've got

**Dave Jones:** ourselves the uh microphone down here. You could rip that out. That's for the speakerphone system. Look the uh jog shuttle thing here. Nice little optical encoder on its own PCB there. Very nice. We'll salvage that out. Get the speaker

**Dave Jones:** of course. And most of it, you know, most of the stuff on here uh not you know, hugely uh salvageable but you'd probably keep a board like that for, you know, some SMD uh rework training or something like that. Um

**Dave Jones:** you'd get the flat flex out of here. We'll get the LCD out of here. It's probably like a standard uh Hitachi chipset one perhaps. We'll I to have a look at that. But uh yeah, you know, there's a few salvageable items in here,

**Dave Jones:** that's for sure. That's the optical encoder board. It's a Mitsumi. Very nice, very usable. Standard electric mic insert, that's a keeper. And the board just unscrews out of there. The matrix and the uh LEDs, surface mount LEDs to

**Dave Jones:** light up the individual keys over here, all surface mounted on the bottom of the board and directly on. True single board solution in that phone. Very nice, only a double-sided uh layout there, that's really all they need. Um you know, you

**Dave Jones:** can forget the chips, these are all sort of uh proprietary jobs, you know, don't even worry about uh trying to salvage those. That micro switch over there was nothing of the sort. It was uh you know, not like a standard little one you can

**Dave Jones:** desolder or something like that, a lever-based one, unfortunately. But yeah, you keep that board for um maybe some parts salvage or SMD trading, you might get some regulators out of there or something like that. And it looks like we might have ourselves some

**Dave Jones:** bicolor SMD lids there. You can see how they manufacture these keypads here on the little uh lever arms there, all part of the one big plastic frame. Look at that, that's uh you know, uh once you've got that uh down uh pat on your assembly

**Dave Jones:** process, that's a very uh cheap and efficient way to do it and get nice um you know, a tactile uh well, nice spring feel on your keys. And here's the LCD module. Uh it's a rather curious uh 16

**Dave Jones:** character by three line display. And yes, it is standard uh Hitachi uh 44780 uh standard, but unfortunately, the connector over here, weird ass uh you know, fine pitch like uh 36-pin jobs, they're not standard pinout there, but you could certainly um hack into that

**Dave Jones:** and uh drive that display. And it's got little uh buttons here as well, and that's presumably why they've used a pin count, but you might want to uh keep those as well. In fact, I would keep this entire

**Dave Jones:** thing because it has the buttons and everything else. So, I'd probably keep that entire assembly. Check it out. It's even free standing. What a Bobby does love. And how about this toaster one? Very similar to the Panasonic one in

**Dave Jones:** terms of use that we just had in this this one made in Australia. Beauty. And here we go. It's actually a Nortel phone. Look at that. Attention to detail here. Look at the padding they've put in there, the dampening material for the

**Dave Jones:** speaker there just to improve the acoustics a bit. Nice attention to detail. Aha, standard header going to the LCD. That's what we want. Beauty. You know, still all SMD single board construction. Nortel chipset here. You know, you might be able to salvage you

**Dave Jones:** know, there's a might be able to salvage some transformers or something else on, but basically the same as the Panasonic one. Got ourselves a LCD on the back here. It's going to be a custom LCD, but we've got some

**Dave Jones:** zebra strips. Look at that. Definitely keep those. They're always handy cuz they're difficult to get just for you know, generic use like this. They're you know, you pretty much have to salvage those. Once again, same deal. It's all

**Dave Jones:** integrated double-sided PCB. You know, don't need multi-layer. All custom Nortel chipset whether or not they're full ASIC or whether or not they're you know, something else. It wouldn't surprise me. Nortel are huge. Things like inductors are always very

**Dave Jones:** handy to have in your junk box. So, you know, these are nice through hole ones. You'd probably suck those out. Couple of SMD ones over here. You might get those out as well. Maybe some of the electrolytics to throw in your kit. I

**Dave Jones:** mean, there's a 1000 V 16 mic low profile electrolytic. You can see how they've just gone for the single key construction. They haven't molded those into a frame at all. Two line by 20 character standard Hitachi display with ribbon cable. Ah,

**Dave Jones:** standard 0.1 inch header. Beautiful. Definitely reuse that sucker. Next up, this Polycom made in Thailand SoundPoint IP phone. There it is. Connects to your LAN PC. You probably could still use this as an IP phone, but well, you know,

**Dave Jones:** I don't really I use an IP phone at home, but I've already got a wireless system. So, let's crack it open. Looks like a 20 line by four character display. Beauty. Well, this one's not as built down to a price point as the

**Dave Jones:** previous ones. I mean, look, we've got you know, a separate membrane keypad over here with the membrane flex. We've got some flex cable going in there for the contact. The the handset contact up there. Look at that. So, you know, it's

**Dave Jones:** it's a bit different, but yeah, you definitely keep that board. They've got a header up there. Some sort of programming programming/production test header or something like that. Pulse transformer. Nothing else hugely salvageable in this thing though, but as

**Dave Jones:** I said, you could still use it as an IP phone if you wanted to. Well, there's a surprise, a TMS 320 DSP. Go figure. And we've got a KS 8081 Ethernet switch built into that. So, that just ties into

**Dave Jones:** our TMS 320 processor there. And then we've got our pulse transformer and the miscellaneous paraphernalia to interface to here. Ethernet connection. What I thought was a programming production header is actually a board-to-board interface and it's a bottom entry.

**Dave Jones:** There we go. There's a standard header. So, there's us Look at that. Beautiful. Standard 4 by 20 character as I said LCD module with the standard header pinout going to a female uh, pin header receptacle in the bottom

**Dave Jones:** of the board. So, you'd actually, that would be a keeper. You'd, uh, maybe, uh, suck, maybe remove that sucker, but, uh, the LCD, beautiful. You just pop that out. It's like a bought one. So, they've gone to a bit more trouble there.

**Dave Jones:** They've got a custom metal backing plate on this thing, which is sharp, by the way. It can cut you, uh, quite deep. Sliced me open there. What a bummer. But, uh, yeah, they've gone to a little bit more effort there than the previous

**Dave Jones:** phones, which were just, uh, you know, the carbon tracks on the back of the PCB. And this module on the side here was just designed to slide in to the side of the case here. It's got a big, what looks like a big graphic, uh,

**Dave Jones:** LCD, bunch of soft buttons, probably for a, um, you know, a soft dial directory, uh, quick directory type function. And there's a fair bit of guts in that. Check it out. A bunch of reverse mount, uh, surface mount LEDs there. Yeah, the

**Dave Jones:** blood's getting a bit worse. Ah, no worries. And, uh, it looks like it's a two-wire interface. This board just slides out and then the contact in the other side. So, power and data goes across that two-wire interface. Really

**Dave Jones:** quite neat. Got an Epson, uh, LCD driver there, by the looks of it. And, uh, not a huge amount more. So, these are the same, uh, reverse mount LEDs. They just, uh, shine through a hole in the board.

**Dave Jones:** Exactly the same as I used in my micro card here. Just drill a hole in your board, shine through. Neat solution. And that's a neat solution because you can mount all your components single-sided load. Instead of having a top mount LED,

**Dave Jones:** you'd have to run through this board a second processor your pick and place machine just to put your LEDs on the top side. That cost you time, that cost you assembly line time and money. And sometimes you can, you reuse, uh, little

**Dave Jones:** light pipes like this. Always, uh, handy just to have a little, uh, parts drawer filled with these things. You might be able to hack them into some product. And that two-wire system looks like it's cascadeable, too. This plugs into your

**Dave Jones:** unit over here, and then another one can plug into here, and so forth. Not how many, not sure how many you can plug in, but uh, yeah, that's rather neat. And that Epson parts actually a fairly beefy 32-bit microcontroller, but you know,

**Dave Jones:** it's not like you'd reuse this. There it is, you could possibly reuse that graphical LCD. It's a PC3721WN, but you search that or you get is some brokers. So, might be hard to find the equivalent or a data sheet for that one,

**Dave Jones:** but you'd keep it just in case. And another really simple Polycom. And the good thing about this phone is that couple of screws on the back, easy and quick, and these pop off. You can salvage the parts. Too easy. Here's an

**Dave Jones:** interesting alternative to screws because of course the screws take time and effort to actually punch in. There's just a standoff behind there, and that's just like a hot melted, you know, rubber or something like that, and that just keeps the board off the

**Dave Jones:** standoff there. And we have one of ourselves a chip on glass COG display. Yeah, not quite as usable as the 0.1-in headers, but certainly yet another keeper. The problem with a product like this with that huge Texas Instruments BGA in

**Dave Jones:** there, not quite sure what that is, TNA or something, but anyway, yeah, look, you know, look at all the components they've got, maybe some 0603s, you know, some 0402s down in there, double-sided load, very dense, all that sort of stuff. That just costs more to

**Dave Jones:** make than the other phones we've seen. Getting a bit sick of Polycom by now. You can see the attention to detail on the acoustics. They've got rubber surrounding this dual rubber surrounding this electric mic in there. Nice. TMS320

**Dave Jones:** DSP again and that Micrel chipset. The other one was a Micrel, but it was rebranded some other name, but basically the same part. Scored another one of these identical graphics LCDs, and you'll notice that they've Um, uh, learned their lesson here. Look, they've

**Dave Jones:** gone for the reverse mount SMD LEDs even though they're using the, uh, BGA package over here. They've decided to not, uh, you know, we can get away without using any bypass caps on the back. So, only single-sided load except

**Dave Jones:** for that connector down there. And a Nortel Networks, uh, Ethernet phone. Once again, you could reuse this. I don't have the power adapter or, uh, stuff for it. So, that makes it a bit difficult. You probably, uh, likely, uh,

**Dave Jones:** power over Ethernet as well. Made in Australia. Again, beautiful. This is the I2004 model NTEX00. This microphone's really interesting. You can see like a micro grill or something down there in like a big horn arrangement with the standard electric

**Dave Jones:** mic at the bottom like that. But, they've gone to a bit of trouble there to do that. They've decided to do their switches as membranes there. So, we've just got the, uh, carbon button on an extended membrane coming out there. I

**Dave Jones:** don't know about that. We've got ourselves a bonafide budge there. Look at that. Looks like a, uh, decoupling budge. We keep seeing the same things over and over. TMS320 DSP. We've got an Epson micro over here. And, uh, here we've got a, uh, Net

**Dave Jones:** Silicon, uh, device for the, uh, Ethernet interface. And check out the, uh, light pipe they've got there. Half pipe going over just to light that, uh, red light on the front. Gone to a bit of effort. And there it is. Not often you

**Dave Jones:** get one of those. So, we'll keep that. Might be usable for something. Unfortunately, the LCD on this one not really reusable. It is a complete, uh, custom job by the looks of it. And we've got the heat bar connectors down here.

**Dave Jones:** So, you know, we can just peel that off. And well, once you do, um, not really reusable, unfortunately. Check out this piece of engineering, uh, acoustic porn. I've never seen them anyone go to this much trouble in a phone. Look at this,

**Dave Jones:** not like a mylar cone, not just a crappy paper cone speaker in there, but it's got a rubber acoustic seal in this, completely sealed like six screws there and then a a vent port on the back for presumably

**Dave Jones:** better bass performance. That's just one complete assembly they've popped in there and this port vents out the top of the case here. Like oh, the bottom of the case down near the desk. Unbelievable amount of effort for the acoustics, but hey, thumbs up.

**Dave Jones:** Somebody went to town on that. Gilded in the lily. And lucky last, a different manufacturer, Cisco Systems IP Phone 7960. What's inside this puppy? We'll find out. Well, this one's actually a bit old school compared to some of the others. Look, we've just got

**Dave Jones:** you know, Molex connector type wiring up to a board here soldered directly through, none of the flat flex we've seen. We do the LCD once again probably you know, not hugely reusable because you know, it's this instead of being a

**Dave Jones:** hot bar attachment soldered down, you could reuse it cuz it's a press fit, but then you've got a you know, push it down onto your board contacts. We've got some shielding over this so they've you know, taken themselves seriously there and

**Dave Jones:** we've got ourselves a a daughter board here just for the Ethernet interface and power. Phew, go figure. We do have some form of part number on there, but you know, the odds of reusing this you know, probably more

**Dave Jones:** effort than it's worth. We could desolder this, but uh screw that. Literally. Ta-da! We're in like Flynn. After your trouble, you cop a couple of big ass custom Cisco chips. We've been mooned. So, we end up with a box of crap and a

**Dave Jones:** box of useful stuff. Beautiful. Catch you next time. And don't forget the small kiddie of screws.
