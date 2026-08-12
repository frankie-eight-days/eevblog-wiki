---
video_id: qcG4fcNIX7A
title: EEVblog #266 - Mailbag
url: https://www.youtube.com/watch?v=qcG4fcNIX7A
source: youtube-asr
timestamps: {"0": 0, "1": 20, "2": 54, "3": 72, "4": 101, "5": 117, "6": 152, "7": 172, "8": 203, "9": 222, "10": 246, "11": 267, "12": 288, "13": 307, "14": 345, "15": 364, "16": 395, "17": 434, "18": 454, "19": 471, "20": 495, "21": 514, "22": 539, "23": 578, "24": 608, "25": 631, "26": 647, "27": 661, "28": 686, "29": 711, "30": 744, "31": 775, "32": 793, "33": 821, "34": 846, "35": 886, "36": 925, "37": 960, "38": 979, "39": 1005, "40": 1021, "41": 1049}
---

**Dave Jones:** Hi, yes, it's mail bag time again where I open my mail. People just send me stuff, random stuff and I'm going to open it here. So, I got five items actually. Let's check it out. First one is CircuitCellar. No surprise. I know exactly what's in here. Get out the trusty Swiss Army knife.

**Dave Jones:** It should be Everyone has heard of CircuitCellar. So, no surprise. Which includes your interview. On behalf of CircuitCellar Audio Amateur and Elektor US staff in Vernon, Connecticut, I want to thank you for your contribution. Hello to all my viewers in Vernon, Connecticut, if there are any. I don't know. How big's Vernon, Connecticut? No idea. There you go. And uh Oh, I got two copies. Brilliant. I'm in the April edition.

**Dave Jones:** There you go, CircuitCellar magazine. I don't get a print copy of this. I've never gotten a copy. I've always gotten the digital copy of this. So, this is some real paper. April 2012. Let's open it up and have a look.

**Dave Jones:** There I am. Who is that ugly guy? Unbelievable. Why don't they let him in here for? 22, page 22. And there it is. There's my interview. Electronics engineering for the people. The people's engineer. Go figure. There's inside my old clock, home brew clock, home built clock. There's the uh famous photo of me with the multimeters.

**Dave Jones:** And there we go. I got three full pages, four. Four pages out of that. There you go. Go figure. Right in there with the microchip stuff. Huge full page microchip ad. I wonder how much they pay for that.

**Dave Jones:** Ah, there you go. I didn't have to pay a cent and I got four pages worth. Brilliant. Love it. So, there you go. If you want to read my article, get the latest copy of Circuit Cellar. Now, the next one is pure spam. I get this all the time. So, I know what's in here. It's from the domain renewal group. A bunch of predatory bastards who who get your name from the whois list on domains and they offer to renew your domain at a ridiculously inflated price.

**Dave Jones:** And they ship out probably millions of these. It's They're actually in Australia now. I don't think they used to be in Australia. I might send it back to them in their reply paid It's not reply paid. It's fixed postage here. Screw that. Anyway, what they do is they There you go. Ozcanyons.org.

**Dave Jones:** They're saying, "Oh, it's expired." Yada yada yada. So, they're making it out to be that they're they're Well, they're preying on the fact that, you know, you don't know anything about domain renewal and you'll you'll go out of business if you let your domain expire. And it's 1 year for 45 bucks. You got to be kidding me. I pay about 5 bucks a year and that's like the going rate. If you're paying anything more than 10, you're getting ripped off. You're getting shafted. So, there you go. I hate this mob.

**Dave Jones:** I think they used to be more than that actually. Maybe they're not getting enough bites now, but I hate them. THEY JUST AND THE NEXT ONE HERE IS FROM ENERGY MICRO. I was expecting this one. I think they've sent me a dev board. They emailed me and said they would send one.

**Dave Jones:** So, let's crack this sucker open and see what's inside. Ta-da! The EFM32 starter kit. It's a 32-bit microcontroller, really low energy one, apparently. So, that looks Let's have a look at that.

**Dave Jones:** Tension. They've got it in a nice static shielding bag. I like that. Well done. And ooh, it's got an LCD on it. Lovely. Excellent. There we go. We've got a It's the Tiny Gecko. Love the name. The EFM32 Tiny Gecko board.

**Dave Jones:** And if we take a closer look at that, we're going to see a 2032 battery there. We've got a J-Link. I think that's a debugger {slash} programming interface. Oh, no, there's a debug in out. And it's got a light sensor.

**Dave Jones:** There we go. And a couple of switches. And there's the EFM32 micro. Pain in the ass package, but it's got a touch slider. It's got one of those capacitive slider ones, so you can slide your finger along there, and you can decode that in software. It's got a 32 kHz crystal on there.

**Dave Jones:** And a few other miscellaneous devices. All mounted under the LCD there. Excellent. Supplied with the USB cable. You get the IAR and the IAR embedded workbench, C compiler presumably. Like that's usually code limited to like, you know, 32K or something like that. Don't quote me on that, but that's a lot of pink Ah, nothing. Nothing. Not a sausage. At least I got a some bubble wrap to pop.

**Dave Jones:** Ah. No. Can't even pop this stuff. Hopeless. And no, nothing. It's just padding. Comes from uh Norway, by the way. Came all the way from Where is it?

**Dave Jones:** Norway. Beautiful. Hi to all my viewers in Norway. Now, check out the back of the board here. I rather like this. They've actually gone and put the schematic of the op amp there with the footprints I used so that you can solder in the various components in there to presumably use an op amp on the top side. I really like that. It's rather neat, but uh uh if you don't know about the energy micro boards EFM uh the chips, the EFM 32 range there, ultra low power

**Dave Jones:** uh 32-bit micros, 180 microamps per megahertz megahertz execution, uh 900 nanoamps in deep sleep mode, whatever deep sleep mode means. Presumably, that means with the real-time clock still uh going, and 20 nanoamps in shutoff mode, whatever shutoff is. That's presumably doing absolutely nothing. I don't know if that has wake up on interrupt or anything like that. Check out the data sheet if you want further details, but 4 to 32k uh flash memory, 1 to 4 kilobytes SRAM, and it's got a built-in LCD controller, as you'd expect, 4 * 24

**Dave Jones:** segments, and the LCD controller itself only uses 900 nanoamps. So, if you're after a low-power micro, well, check them out. They're worth a look. And this board, this tiny Gecko Gecko development board runs for about 74 bucks, and you can get it from Mouser and Digi-Key, too, I think. So, it's not bad value.

**Dave Jones:** And they've partnered up with Segger, and that's what the J-Link USB header is there. It's the Segger uses the Sega J-Link debugger. That's the tiny gecko. Can't they put like a little picture of a gecko on the board or something like that? That would have been really cool.

**Dave Jones:** Look at this. Plenty of room on the bottom side to put a gecko. Instead, they just put their name and they just put the the lead free crap. Who cares? I want an animal on the board. Because we get a nice looking gecko on the box here, but why not put that on the silk screen? Come on. Now this one here is interesting. It looks like it's been through the wars here.

**Dave Jones:** It's a It's a little bit beat up and it contains a do-it-yourself electronics kit worth well, presumably 9 euros or that could just be the thing they put on the worth they put on the customs form and it's from Deutsche Post. Love the Germans. Hi to all my German viewers.

**Dave Jones:** I think you're the third or fourth highest. Got a huge contingent of viewers in Germany. And it comes from I cannot read that and I'm not even going to try and pronounce it. Anyway, thank you very much. So let's crack this thing open. I have no idea what this one is. So this one is a uh This one is a random.

**Dave Jones:** It's uh Nice silver tape there. I rather like that. All right, here we go. Tada. Got some paper. Have we got a German newspaper? We do. There we go. All right, German uh viewers will no doubt be able to read that because I can't. Uh Apart from Guten Tag, that's about all I know. So there you go. I have no idea what paper that that is. It's the Der Kleine uh, I'm not even going to pronounce it. I cannot pronounce stuff.

**Dave Jones:** I'm hopeless. So, there you go. You got some paper. Hi Dave. Thanks for uh, I can't read the handwriting. Thanks for uh, something about Keycad. No worries. Have fun with this toy with Oh, let me open it. Oh, there's a Oh, CD.

**Dave Jones:** If everything else fails, you can at least use it at the uh, all the I can't read your handwriting. Sorry. Works with Arduino IDE. Cool. OH, LOOK. OH, WHAT DO WE HAVE HERE? HEY, this looks nice. We've got surface mount uh, parts. Excellent. 100 micro farad C.

**Dave Jones:** This is the thing. Um, people always talk about uh, why don't I do a surface mount kit or something like that? And this is why, because you have to individually cut or tape or label or something these individual surface mount parts because they're a pain in the ass.

**Dave Jones:** I mean, you know, there's no markings on these surface mount caps, right? So, you've got to um, just uh, you know, you've got to separate them into a bag and then identify them and it's just Yeah, it's just too much hassle.

**Dave Jones:** Excellent. 250 degrees C max to the center of the board. Awesome. Little 0805 diodes. Put them around once. Sorry for the mess. The AVR is uh, pre-programmed with little demo. Cool. Please connect to a sound a serial uh, terminal. 96 board. 8N1, not Arduino IDE. Awesome. So, that's this little board here.

**Dave Jones:** Let's check it out. This is great. Some nice little hardware here. Oh, wait. Whoa. We've got chips and all sorts of things flying out here. Hang on. This could be messy. Yeah, there's there's chips and other stuff in there. And this is a uh rather cute-looking uh cute-looking board. I like it.

**Dave Jones:** Not sure what it does. Blog, there we go. Blog.spitzenfell.org. Thank you very much. There's the address. So, check it out. Blog.spitzen, if I'm pronouncing spitzenfell.org, if I'm pronouncing that correctly, I'll put the link up so that uh you can put it in. And it's obviously some sort of little uh AVR demo board. Lost in time surrounded by evil and low on gas.

**Dave Jones:** What's that a quote from? Lost in time surrounded by evil and low on gas. It sounds like a quote from something. I'm not sure. I uh not aware of that one, but uh if anyone is, please let me know. I have to check it out. And there's the other uh other parts in there, the LEDs with the uh little surface-mount AVR. Micro is pre-programmed. That. So, you must have one of those um uh must have one of those uh ZIF sockets to handle the PLCC uh 28

**Dave Jones:** package there. So, there you go. What else have we got? And the CD is uh presumably Yep, software. So, excellent. Thanks for that. Sorry I can't uh pronounce your first name, Laiter, but thank you very much from spitzenfeld.org.

**Dave Jones:** That's brilliant. I'll have to build that up and uh see what it does. That'll be fun. That's a nice therapeutic board to build, I think. It's kind of lots of therapy in that. Lots of satisfaction. I love round boards. They're neat. Brilliant. Thank you very much. And this just arrived this afternoon and I know exactly what it is. Micro currents. Woohoo! I've got 50 apparently. 50 assembled micro currents.

**Dave Jones:** I know I had 200 manufactured but they won't be ready until um early next week. But they said they'd ship me 50 and uh Tada! Here we go. There's the boards. Ah, these are bloody foam peanuts. Let's see if I can get them out without spilling the foam peanuts.

**Dave Jones:** Tada! They left them on the panels. Excellent. And there we go. Here's my completed micro current boards. Awesome. Look at that. They look neat on the panel. I'll put them down and we'll get a close-up of them. And this is my new panel from uh Circuit Labs in New Zealand and it looks very nice indeed. I like it. EE Vlog micro current because I added the EE Vlog on there as you might know. Seems to be no issue with the construction there at all. I can't see any component

**Dave Jones:** loading issues but I guess we won't know until we fire one of these up and that means I've got to break these out of the panel. Now ordinarily you'd use a a cutter on here to actually like a wheeled cutter to go along and slice these off but uh we don't have that so next best thing is just to give them a little little wiggle like that and uh that should they should break off fairly easily without doing too much with well, without doing any damage to the uh

**Dave Jones:** to the rest of the board. There we go. Snapped off pretty easy. And uh then once you've got these ends off, you can uh leverage the full board there to give it a little bit of a wiggle and off it comes. And that's the uh beauty of the V-scoring. And now it's quite uh and now it's quite uh wobbly.

**Dave Jones:** It's uh you can do the old Rolf Harris wobble board thing. There you go. Maybe I can do tie me kangaroo down, sport. Tie me kangaroo down. All together now, tie me kangaroo down, sport. Okay, I'll uh spare the Yanks that.

**Dave Jones:** So, let's uh see if we can then take a board and snap it off. Easy. Not a problem. There you go. There's the uh before shot and the after shot. This is a new uh Circuit Labs New Zealand board and uh I rather like it. I like the bigger font. It's got EEVblog on the front and it's a more metallic uh shiny face on it. I think it's rather neat. I like it.

**Dave Jones:** And does it work? I've whacked a battery in there and uh hey, the LED comes on. That's a good start. At least the battery detection uh voltage works. And the nanoamp range works, no problems at all. I'm feeding in 100 nanoamps and pretty darn close.

**Dave Jones:** And the microamp range, look at it. Spot on. And I'm feeding in 99.9 milliamps and the milliamp range, pretty darn close to spot on, too. Awesome. I declare this one to be a winner. So, there There go. That's the EEVblog mailbag. I hope you like that one. And if you want to uh send me stuff, please do. Here's the address. PO Box 7949 Baulkham Hills, New South Wales 2153 Australia.

**Dave Jones:** Not Austria. Okay, get it right. And yeah, by all means send me stuff and I'll open it on air. Can be anything. Bizarre? I don't care. Send it. Catch you next time.
