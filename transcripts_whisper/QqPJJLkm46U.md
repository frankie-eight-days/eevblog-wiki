---
video_id: QqPJJLkm46U
title: EEVblog #928 - Jaycar DMX RGB LED Lights Teardown
url: https://www.youtube.com/watch?v=QqPJJLkm46U
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 20, "2": 41, "3": 58, "4": 77, "5": 94, "6": 112, "7": 134, "8": 148, "9": 163, "10": 182, "11": 197, "12": 214, "13": 242, "14": 266, "15": 290, "16": 306, "17": 327, "18": 339, "19": 359, "20": 379, "21": 396, "22": 416, "23": 436, "24": 453, "25": 476, "26": 496, "27": 513, "28": 528, "29": 549, "30": 566, "31": 585, "32": 609, "33": 627, "34": 647, "35": 661, "36": 689, "37": 702, "38": 718, "39": 737, "40": 755, "41": 771, "42": 794, "43": 818, "44": 838, "45": 857, "46": 875, "47": 890, "48": 902, "49": 917, "50": 936, "51": 950, "52": 966, "53": 979, "54": 997, "55": 1017, "56": 1034, "57": 1050}
---

**Dave Jones:** Hi, we're going to do a quick teardown of this DMX stage lighting disco-y type light controller that I scored from the Jaycar sale, and if you haven't seen that, click over to the previous Jaycar video. I got two complete sets of these. There's actually four lights, came in a padded bag and everything else.

**Dave Jones:** We've got the DMX controller itself, and I got them for a dollar. So, like, you know, meh. Anyway, we're going to take a look at them. They look pretty crusty. You can smell the dodginess in this thing. The first thing you notice is that it doesn't really have a brand at all.

**Dave Jones:** I'll link to the Jaycar page down below. It's like, this was like a $400 set or something like that. I don't think they could sell them at $279 or whatever. And, like, there is no branding on these at all. The bag itself, the big padded bag, had Rave on it,

**Dave Jones:** so it was, like, sold under the Rave brand. But, yeah, there is just nothing on this controller at all. There is absolutely no branding whatsoever. So, you know, right there it sets off alarm bells that this is the cheapest heap of crap you're going to find.

**Dave Jones:** And, yeah, it just looks and feels like the cheapest quality thing possible. So here's the big padded bag. It came in with the Rave symbol. And it came with this foot controller as well, so you can suspend it, you can call up the menu, and you can go up and full.

**Dave Jones:** So, yeah, you've got four lights with it. And it came with a, this is supposedly non-working, faulty XLR socket. Controller doing really strange things. Hmm. Anyway, that's why it was in the dumpster for a buck. I don't know, I'll tell you what, I might have actually been ripped off for a dollar.

**Dave Jones:** Because these are pretty crusty. These actually fold out like this. These arms fold out so you can plug the controller, you can have the lights spread out. So there's actually the four sockets on the bottom here for the four lights and the controller interface, DMX in and out, and the menu, and enter, and power.

**Dave Jones:** Well, yeah, I'm going to violate the rule and actually power it up. Because I want to see if these things do actually work. Now I've no idea if you're going to be able to see this or not. Excuse the reflections from the lights overhead.

**Dave Jones:** But some of these LEDs in here look different to some of the others. So it's really unusual. This is supposed to be like a full RGB matrix. But when I look down there, some of that one is different to all the other ones around it.

**Dave Jones:** It's almost if it was like, you know, a different colored LED in there. You often find that in selectable colored LED lighting systems that you can buy for your home and stuff like that. You know, different color temperatures. And they do that by mixing white LEDs of a certain color temperature,

**Dave Jones:** mixing them with yellow and other, and maybe other colors, I'm not sure. But anyway, mix them with like yellow LEDs or something like that, just to change the color matrix. But yeah, they do look slightly different dye inside the LEDs in some pattern.

**Dave Jones:** Anyway, I don't know. We've got 12 volts and RGB in there, but yeah, these things, 10 millimeter LEDs, they look pretty crusty. But even for a dollar, just stripping the RGB LEDs out of these things, gotta be worth it. Check out this socket.

**Dave Jones:** Yeah, it's dodgy, alright? It's like it's fallen out of there, it's been stripped or something. Anyway, I'll see if I can actually plug it, mate it up and plug it in. Alright, let's power this baby up. And... Whoa, hello. Whoa, they flashed. Got some gobbledy gook on the display there.

**Dave Jones:** Um, menu, what? PU 75, PU 45, what? P37? Disk? No, it wasn't display, was it? No? What? It's all over the shop. Wow. I have no idea. You'd have to read the manual on that. Anyway, I'm going to try my foot controller. Menu?

**Dave Jones:** No. Up? Nope. And? Nope. Full? No, foot controller doesn't work. But you saw it, those LEDs came on. Let's try that again. Gotta let the cap discharge. There we go. Whoa. Yeah, red, green, and what? Yeah, anyway, they kind of sort of work.

**Dave Jones:** Anyway, let's tear down this puppy down, and this is going to be crusty as inside, I'm sure. Well, there you have it. That really is quite meh inside here. We've got ourselves a bunch of switching trannies here, which is what you'd expect. I'll show you those up closer in a minute.

**Dave Jones:** Oh, that's really how you're doing wiring on that dodgy as one hung low brand XLR connector. Geez, no genuine stuff in here. No siree, Bob. Anyway, we've got ourselves an Atmel processor there. We'll have a squiz at that. And a couple of probably, what are they, 7400 series?

**Dave Jones:** Something or other? I don't know. We'll take a look. But there's not much to do on there. The soldering's crusty as. Actually, let me show you that. What the hell's going on there? There's no solder on these pins. What is it on the other side?

**Dave Jones:** I don't know. But that's as dry as a dead dingo's donger. Unbelievable. That's an ATmega16 for those playing along at home. And we've got ourselves 20n03 n-channel MOSFETs down in here. The finest that AliExpress has to offer. And you'll notice Bugger all heat-sinking on these things.

**Dave Jones:** They just haven't bothered. So I don't know what the ratings of these LEDs are. I know absolutely nothing about this thing. It just says like power consumption 120 watts maximum. You know, like means absolutely nothing. So yeah, these things aren't going to be...

**Dave Jones:** Well, you know, the losses in them are going to be relatively small. But still, they're in power packages and they're not... There's no heat-sinking on those at all. And of course, 74HC595's classic chip. I used to love these when I was a kid.

**Dave Jones:** Serial addressable latches. Absolutely fantastic. Still used in a ton of stuff these days. Very common for dry, you know, individually addressable LED drivers and stuff like that. And of course, via DMX control, it allows you to set the brightness of the LED. So these are just PWMing the presumably...

**Dave Jones:** Well, hey, is there a constant current driver power supply? Looks like just... I hope there's... Are we going to find dropper resistors in the LED lights, which we'll take apart in a minute? It's looking likely. So apart from being a little bit dodgy, you know,

**Dave Jones:** like it's all cable-tied okay. And they've put protection sleeving over these, which go into those that swing... which goes into the arm that swings around here. So they've got to have that. That's all right. And the mains input was okay. They're actually... They went to the effort, look,

**Dave Jones:** to scrape off the anodizing there, although that's all... Ah, you know. No, they should... That's not properly crimped anyway. Our power supply's up under there somewhere. Hmm. Once again, we've got the finest that AliExpress has to offer. HSE power. It's a 100-watt, 12-volt output LED driver.

**Dave Jones:** It doesn't say... It's mostly in Chinese, but I couldn't get an actual data sheet, but there's, you know... It's a 100-watt supply and 12-volts DC nominal, so presumably it's 12-volts DC output, and it's not a constant current driver. So yeah, looks like we're going to find

**Dave Jones:** dropper resistors inside those LED arrays. Hmm. Because all we're doing here is basically generating just a 12-volt power supply, and then over here we're just using these MOSFETs to pulse-width modulate the 12-volts going to whatever LED strings. I mean, how many have we got there?

**Dave Jones:** 2, 4, 6, 8, 10, 12. So we've got three of those per array, and that makes sense, because you've got to have one for the red, green, and blue, and sure enough, if you look at the wires, we will have three for each one.

**Dave Jones:** What? Plus, yep, plus 2 power. So we've got ourselves 145 RGB LEDs in here, and we're going to have a dropper resistor in each string, because you can't fit, you know, it's not like they're all in one string, because we've only got 12-volts compliant voltage.

**Dave Jones:** So we're going to have multiple parallel ones with dropper resistors in there. Presumably they might have sprung for dropper resistors, but this is not going to be big power anyway. I mean, the wiring we're talking about here, this is really pissant wiring in there,

**Dave Jones:** so, you know, really, these things are not high power at all. These will be, these LEDs will be from whatever stall in the Shenzhen market that they were able to get them from that month, no doubt. And let's take a look, I mean, that's just,

**Dave Jones:** that is, yeah, some crappy polycarb. Anyway, yeah, these weren't for heat-sinking. If you're thinking that the aluminium around the outside here, nah, it's just for show. There's no heat-sink at all. These are getting the illusion of high power without the expense. So let's have a look.

**Dave Jones:** You can see some jumper links in the center of the boards there. I demagnetized this the other day. I've got to magnetize this puppy. And there we go, sweet. So, you've got to get one of those magnetizers, demagnetizers, if you don't have one, by the way.

**Dave Jones:** And here we go, we're in like Flynn and little pissant 1206 dropper resistors. Thank you very much. You can see how they've glued those down, so they've actually wave-soldered the entire back of this thing. You can see those little red marks. They're the glue underneath the resistors holding them down,

**Dave Jones:** so they go through the bubble bath, solder bubble bath. I mean, look at this, they didn't even bother with a proper connector on there. I mean, they had the through-hole thing for the connector, and they just went, ah, nah, screw that. And unbelievable.

**Dave Jones:** Those pins are sticking out a long way. They're sharp as. But, yeah, that's really pathetic. What else is there more to show you in this thing? It's just, sorry, it's boring as. A completely crappy, built-down-to-a-price DMX LED lighting disco-y type thing. Yes, it did actually have, it has actually a microphone inside here,

**Dave Jones:** so you can, one of the modes is actually just to set it up, so you don't have to do any DMX control at all. You can just buy these, set them up at your party or whatever, your rave, and just have the lights just flash in different colours

**Dave Jones:** just based on the music and everything else, how complicated that is in there. It's not going to be doing FFT or anything fancy like that, getting the spectrum or whatever, and doing the colours, so it's just, yeah, faking some light show based on the audio level,

**Dave Jones:** but that is just crap quality. That is awful. Anyway, if you've got any ideas what I can do with that, because they're of it, like, as a controller it's no good, even like the chassis is just the crappest quality. Chassis, unbelievable. But I don't know, is that any good for anything?

**Dave Jones:** Shenzhen market no-name RGB LEDs? I don't know, 10mm RGB LEDs, that's a reasonable score. You know, you could de-solder those and put them in your parts drawer or possibly use them for something. I don't know, but who knows what the specs on those things are.

**Dave Jones:** Couldn't really care less. I'll tell you one thing though, they've done a reasonable job getting that layout single-sided with, you know, they've only got a few links. You can maybe see those little jumper links down in there. I don't know, but you've got away with that without any links.

**Dave Jones:** But I hate the white solder mask, it's hard to see the traces underneath. Real pain in the arse. Okay, so let's power this turd up and see how much current she draws. There you go, it's only 1.5 watts. That's full power, wow. So there you go, the green draws 5.6 watts,

**Dave Jones:** 0.47 amps or thereabouts, and the red is a measly 1.4 watts. This is hopeless. This is assuming, of course, that the MOSFET is completely on. And look, even the pattern is not complete. I'm assuming that, like, it is like not universal pattern in there.

**Dave Jones:** Like it's not symmetrical, consistent, whatever you want to call it. Well, the blue, 5.7 watts as well. So blue and green are the same, but the red is completely piss poor. The blue, though, does seem to have a symmetrical pattern on it. Yeah, and the green, but the red, oh!

**Dave Jones:** So as you'd expect with heaps of crap like this, you know, just one hung low, slapped together, no name stuff. Like, they're not even, the intensity, power, and LEDs and everything else, not even controlled between the red, green, and blue channels. That's a massive difference there.

**Dave Jones:** I'm not going to bother getting my spectrometer out, and, you know, light meter and things like that, and getting readings. It's just not worth it. These things are just crap. Yeah, they kind of work, you know, you buy them from JK, you set them up at your party, and you switch the microphone on.

**Dave Jones:** No, I reckon nobody used these with the DMX. I, like, I'd be very surprised, because usually, you know, DMX implies some, you know, you're at least doing something semi-professionally. I don't know, I'm sure there's a lot of people who jump down my throat on that.

**Dave Jones:** But, you know, you go into effort to control this, you have to do software to control it and everything else. You've got to have a controller, and the whole works. I reckon most people who bought these would just be, like, using the internal mic.

**Dave Jones:** They just want some lights to flash at your party. And well, you know, it's probably going to do the job, but yeah, it's just really built down on cost. It's a heap of crap, really. But I think, you know, it kind of sort of works.

**Dave Jones:** Hmm. So I guess I was pretty naive to think that they, that would be a full RGB matrix array at any sort. Well, I knew it wasn't going to be, like, a high-powered thing, and yeah, it's not. It's, you know, bugger all. But yeah, and the, you know, the efficient,

**Dave Jones:** these LEDs would be, like, the super-crappest ones I could get. As I said, whatever came, whatever they could get at the markets, at Shenzhen markets at the time, probably went in this thing. If you bought them, like, a year later, they wouldn't have the same LEDs,

**Dave Jones:** they wouldn't have the same parts, they'd have something else slapped in them. Terrible, Muriel. And when I picked these up at the Jaycar Sale, I didn't even know what they were. I just saw, oh, look, lights. They look like, I don't know, some form of crappy studio light or something like that.

**Dave Jones:** I used to assume that they were white LEDs, and that you could control them off and on or something like that. I didn't know that they were full color, so I thought, I don't know, maybe they'd be useful as some studio lights down in the bunker or something like that,

**Dave Jones:** but the RGB ones like this, they're useless to me. And I got two sets of these. So I've got eight light sets, but I only got one controller, though. But I've got two foot switches. Oh, the foot switch. Hang on. Actually, the foot controller's probably going to be the most useful thing out of this,

**Dave Jones:** because, you know, you could have these under your bench, and you could control stuff. You could control, like, a paste dispenser, or, you know, anything. Use your imagination. And if we flip that out, we've just got a bit of perspex under there, and there's our switch.

**Dave Jones:** Oh, that is so how you do it. Is that hot snot down in there? I think it is. So these are really built down to price. I'll just have a quick squeeze inside, but that's terrible. But still, you know, hey, it's a nice and sturdy box.

**Dave Jones:** It's all together, you know. It's got a XLR interface on it, so that might be the handiest thing out of that. Maybe that's worth a buck. And that's the finest hot snot, and dry as a dead dingo's donger joints down there. Look at that.

**Dave Jones:** So, did I get a bargain for a buck, or did I get ripped off? Let me know in the comments down below. Catch you next time. Go to Beadaholique.com for all of your beading supplies needs!
