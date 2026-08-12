---
video_id: YsTZuPN7wQQ
title: EEVblog #171 - Agilent U1272A Multimeter Teardown
url: https://www.youtube.com/watch?v=YsTZuPN7wQQ
source: youtube-asr
timestamps: {"0": 0, "1": 24, "2": 35, "3": 47, "4": 62, "5": 75, "6": 84, "7": 97, "8": 115, "9": 126, "10": 154, "11": 165, "12": 174, "13": 189, "14": 200, "15": 213, "16": 226, "17": 240, "18": 248, "19": 262, "20": 272, "21": 288, "22": 301, "23": 318, "24": 330, "25": 342, "26": 364, "27": 377, "28": 391, "29": 405, "30": 426, "31": 440, "32": 456, "33": 467, "34": 479, "35": 508, "36": 523, "37": 537, "38": 558, "39": 572, "40": 587, "41": 598, "42": 609, "43": 618, "44": 631, "45": 647, "46": 660, "47": 671, "48": 679, "49": 694, "50": 709, "51": 727, "52": 743, "53": 755, "54": 769, "55": 781, "56": 794, "57": 803, "58": 830, "59": 843, "60": 856, "61": 871, "62": 881, "63": 896, "64": 909, "65": 920, "66": 931, "67": 943, "68": 968, "69": 987, "70": 999, "71": 1014, "72": 1025, "73": 1039, "74": 1057, "75": 1075, "76": 1084, "77": 1098, "78": 1112, "79": 1123, "80": 1134, "81": 1148, "82": 1160, "83": 1171, "84": 1182, "85": 1196, "86": 1205, "87": 1213, "88": 1228, "89": 1239, "90": 1247}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, it's product teardown time. Yes, teardown, not product review, cuz I think I've decided for most products that are going to require a fairly in-depth review, my reviews are a bit too long because they include a quite a substantial teardown as well.

**Dave Jones:** So, I thought I'd just separate them out into product reviews and product teardowns cuz there's some people who like the shorter videos and they just like the teardown. So, it's teardown time today.

**Dave Jones:** It's the new Agilent U1272A multimeter. Uh it's not that new. It's been out for quite a few months now, but it's Agilent's big push into the Fluke 87 market.

**Dave Jones:** They directly pitch this against the Fluke 87 and we'll go into that in the review. And it's comes from the um it's completely redesigned by Agilent. It's not just an existing Escort design when they bought the uh existing Escort design group.

**Dave Jones:** So, let's tear it down and check it out. And before I do that, just a quick peek over the unit here. Let's have a look at it. It's quite a nice design.

**Dave Jones:** I really uh like the new uh styling of its design to grip in your hand like that and it does feel really rugged. And we'll go into the uh review of it later.

**Dave Jones:** But um and uh I just like to say thanks to uh Trio uh Smart Caul here in Sydney. In fact, they're just around the corner from my place. Actually, they gave me this one for review.

**Dave Jones:** So, if you're after uh any meters at all, there's no point actually uh importing them directly from the US or directly from China anymore. These meters are now not only these, but uh other test gear are now so cheap in Australia, you don't have to import them in So, thanks Trio Smart Caul.

**Dave Jones:** Check him out. So, let's open this thing up and take a look at what's inside. Oh, look, you can get the reflection of my boom of of my camera and there's my boom mic.

**Dave Jones:** Neat. These feel like self-tappers to me. They don't feel like metal inserts. Am I right? Yes, I'm right. There you go. Self-tapper. Pretty standard sort of stuff. Nothing unusual there, but because the fuses are actually in the compartment, you don't have to worry about opening the case like you do on say the Fluke 87 unit.

**Dave Jones:** Now, that was surprisingly hard to get open. I couldn't actually pry that end off. I had to sort of lever it up like that until it sort of snapped out and luckily I didn't snap anything at all.

**Dave Jones:** So, it would have been nicer from a disassembly point of view to put screws in there, but considering that you know, you really don't have to open this thing, then it's not really a problem.

**Dave Jones:** So, here it is. Ta-da! And my first impression upon cracking this thing open is I'm actually very very impressed. I like it. It's got everything and well, it seems to be doing everything right.

**Dave Jones:** They really don't seem to have cut any corners at first glance at all. We've got the shielding up here. We've got the spring terminal which connects to the shielding.

**Dave Jones:** We've got the huge HRC fuses here which we'll look at in a bit more detail. We've got I love the gold plated battery contacts like that. That I love these battery contacts that don't use any wiring at all.

**Dave Jones:** They just use these spring terminal clips to actually when they press down, they press on the PCB. I love that. That's what Fluke are doing in their new Fluke 28 and their Fluke 17 and other meters like that.

**Dave Jones:** And really the only bit of wiring they've got in it is going to the piezo buzzer up here. They've got a nice little connector on it. It's not just dodgily soldered onto the board like this.

**Dave Jones:** It looks like a real high-quality connector. There's a programming interface. They've actually used a connector for that, but we'll go into that when we look at the board in more detail.

**Dave Jones:** They've got a secondary board up here for the input connectors, and they seem to be doing everything right. Although, I can't see any input protection devices on the top uh apart from this huge uh fusible resistor up here.

**Dave Jones:** That's like the low-value 1 K or less input fusible resistor. That's about all I can uh see up there in terms of that, but we might have to uh flip the board open to see what's on the bottom.

**Dave Jones:** Um but, I'm impressed so far. And they've done the case right. It's got the um it's got this extended part here, which goes into the case to form some blast protection around the outside of the unit in case of uh gross overloads.

**Dave Jones:** It's It's not actually just a a press-together case, but I expected, even though it's not waterproof, uh given the O-ring on the battery compartment, I expected there'd be a full O-ring around the outside of it.

**Dave Jones:** But, if you take a look here, it's not an O-ring. It's like um tape. It's like that uh plumber's tape like you use when you're um doing up a, you know, a a a tap when you're actually doing plumbing and stuff like like that uh Teflon sort of tape.

**Dave Jones:** So, I guess That's the first time I've ever seen that. And And the tape goes all around the outside like that instead of an O-ring. That's the first time I think I've ever seen that used in any product.

**Dave Jones:** Uh maybe they've um they didn't go because it's not actually waterproof, they don't actually need an O-ring. Maybe they've actually gone for just a Teflon tape, maybe to because it is uh dust proof, apparently.

**Dave Jones:** I still I what the IP rating is, but maybe they've done that to keep out the dust, but um if they used an O-ring, it wouldn't have worked unless um there was some weird molding in there because you need a flat surface for O-rings, and this bottom of the case is flat all the way along, but look, then it just curves down like that and goes around.

**Dave Jones:** So, uh and and O-ring um seal really wouldn't have worked on that anyway, but they've used Teflon tape. Find that rather unusual, but anyway, I don't mind it considering that's not a waterproof meter.

**Dave Jones:** And there it is, you can see some of that Teflon tape just sticking out of there like that. One of the first things I noticed that's different to most multimeter teardowns is that there's no main IC on the bottom here.

**Dave Jones:** They've just got and in fact, a quite an excessive uh number, not that that's a bad thing, I guess, but an excessive number of discrete uh SO packages and the and the passive components.

**Dave Jones:** They really haven't pushed the limits of the um of the design. So, they're not using 0402 components, they're sticking to big, nice SO packages, which are uh cheap, available, easy to solder, easy to repair, um and and likely give you a much higher uh yield in production as well.

**Dave Jones:** If you compare it to, you know, if you're trying to use some little BGA part or something uh silly like that. So, this almost is is if like it's an LCR meter in terms of uh the number of um discrete devices.

**Dave Jones:** So, it is a very discrete design. Uh I presume the main processor is on the bottom here somewhere. Here's presumably, it's not labeled, but that will be like a JTAG or an in-circuit programming header, I would presume, for the micro that's uh on the bottom.

**Dave Jones:** I would expect to see an off-the-shelf micro like an MSP430 or something like that. We'll find out when we flip the board over, but uh uh yeah, it's there's just lots of passive circuitry.

**Dave Jones:** The board is very clean. It seems like it's well laid out. Uh there's no solder residue on it at all, and I'll go into the individual components a bit later.

**Dave Jones:** There's a couple of um surface mount electrolytic uh caps there. There's a few components aren't missing, and rather unusual, this thing is rather curious here. It's got like an exposed uh gold pad here with this large uh large package capacity here, and another capacitor that goes off to this rather unusual thing which uh it's almost like a sensor pad which goes off under the bottom.

**Dave Jones:** Uh presumably goes under the board there somehow, and it's connected in here, and it's isolated, and they've taken off the uh solder mask, and they've taken off the ground plane, and and on the input side of the design, they've actually done a pretty good job.

**Dave Jones:** I like it. They've got this secondary board up here, which you don't see all that often. Uh and the contacts are made with these uh brass uh standoffs here, which go from the top of the board to the bottom.

**Dave Jones:** And because they are split uh contact input jacks, I don't know if you can see in in there, maybe not, but they are actually split uh jacks two-sided, so they use that to detect which uh side of the uh where if a if a probe is actually plugged into it, and because you don't need that on the voltage, only need that on the amps, they joined them together like that.

**Dave Jones:** But over here, they are separate, and they would actually tap uh those off to a sensor. They go through to and there's the two sense pins which go through to the board like that, but I I rather like that.

**Dave Jones:** Um it seems very solid. It looks like there's um some O-rings possibly around the input sockets as well, but considering that they've designed this to be sort of splash and dust-proof and things like that over the Fluke 87, uh that's I that's something that you'd expect.

**Dave Jones:** They've got the two big HSC fuses, 440 mA and 11 A. I love it. They've got the high-voltage isolation there with the extruded plastic uh coming through as well.

**Dave Jones:** There's a lot of thought gone into that. I presume the input protection devices are around here and they're on the bottom side of the board. We'll find out that when when we flip it open, but I like that.

**Dave Jones:** I'm quite impressed. And if you look down there, it is actually a rev 004 board. So, they've had a few uh goes at this. They have actually refined it.

**Dave Jones:** It hasn't been out all that long, but they probably would have went through uh three or four four refinements before they actually released it to production. And there's the standoffs uh for the uh serial communications interface.

**Dave Jones:** You can actually buy a very cheap USB uh interface for it, and uh that just goes through hooks up to the bottom like that, and that's just your typical um RS-232 type uh isolated optical interface.

**Dave Jones:** Let's go through the devices on the board here, shall we? I won't show you all the parts up close cuz it's really hard to get a good image of the uh chip number on the device, but I've taken a look at them, and they must be big fans of Maxim.

**Dave Jones:** They've used lots of Maxim parts on here. Um I don't know. Maybe they got a bulk discount, and uh presumably no supply problems cuz you can buy these meters, so go figure.

**Dave Jones:** Um down here we've got a MAX uh 4611, which is a uh quad switch. There's quite a few. There's one here, one here, uh one over here. There's one there.

**Dave Jones:** And uh well, what else have we got? We've got a MAX 4582, which is an eight-way mux here. We've got another one here. We've got a 4,000 series um CMOS device, a 4053 here.

**Dave Jones:** Excellent. Got to have one of those on every meter, I think. Think it's compulsory, pretty much. There's a 74, couple of 74HC series logic here, a HC132 here, a HCT74 here.

**Dave Jones:** There's another Maxim mux up here, the 4583. There's another 4583 there. And there's a 7600 switch capacitor voltage inverter here. And this is the ADC. It's actually an SPI TI part.

**Dave Jones:** It's the ADS 1242. And it's a 24-bit four-channel ADC. It's got a built-in programmable gain amp. It's got 600 microwatts power consumption, which is necessary in a battery-powered device like this.

**Dave Jones:** 21 effective bits. 50 and 60 hertz rejection built in, so you don't need to actually select that in the software. It's got both both mains frequencies built in, so it rejects those.

**Dave Jones:** A lot of meters on the market will actually have a menu option to select 50 or 60 hertz rejection. You don't actually need that need to do that on this meter.

**Dave Jones:** And there's a Burr-Brown OPA340 here. And down here it looks like I think it's a Maxim LM285 1.2 volt voltage reference, but it's a pretty crude uh voltage reference, that one.

**Dave Jones:** So, it's obviously not used for the ADC up here. The ADC has to have another another precision voltage reference around it, but I can't really see one there. Maybe it's on the other side of the board.

**Dave Jones:** And one of the other big things you'll notice missing well, from the top side of the board anyway, is the thick film precision resistor network. We can't see it yet.

**Dave Jones:** It's got to be on the bottom there somewhere. And for the true RMS conversion, there's a bog standard AD637 true RMS converter chip there. No surprises in that. Well, that came apart quite easily.

**Dave Jones:** There's a couple of clips here on the side which actually retain the board, three self-tapping screws, and there's the LCD module with the zebra strips in there which actually connect through to the board.

**Dave Jones:** Oh, sorry, it's only the top one there. As you can see the contacts on the board up there. And it's pretty typical construction. There's a few looks like they've individually barcoded the internal parts there.

**Dave Jones:** The range switch is fairly typical. Um they've got, you know, fairly good quality sort of brass contacts in there. I don't mind it at all. Looks like fairly good quality plating on the board itself.

**Dave Jones:** But once again, there's not any significant current actually going through that. It's just It's It's really just a signal thing. And they have actually labeled a bit of attention to detail there.

**Dave Jones:** They've labeled the individual channel positions like that. I like it. And it looks like I was way off the mark with this shielding thing here. It's It's just an extra shield on the top which actually connects via this spring here.

**Dave Jones:** And um really it has nothing to do with this weird sort of pad configuration on the top that actually that actually connects through to a cap a large cap on the top side of the board.

**Dave Jones:** And I really like the design effort they've put into the backlight. Once again, they've eliminated the wiring with these two spring terminal interfaces here which connect through to the backlight on the LCD.

**Dave Jones:** And then when it presses against here they just match up to the mating contacts on the board. Really good design practice, really good attention to detail. Curiously, they've added a plastic spacer up here.

**Dave Jones:** I'm not sure exactly of its function. Maybe it's a afterthought, I don't know, or maybe it's purpose designed into the unit itself. I'm not quite sure. No surprises at all.

**Dave Jones:** There's the thick film resistor network, but it does have a rather nice shield over the top of it. I love it. And there are multiple contacts in there. There's one at the end there and there's multi You can't really see it, but there's multiple ones in there cuz these thick film resistor networks set the range precision because you got one voltage reference and then it gets divided down for the various

**Dave Jones:** ranges. So there's multiple laser trimmed resistors on this hybrid substrate in there and that pretty much along with the along with the main voltage reference determines the accuracy and the long-term stability of this, but they've gone to a lot of trouble to shield that, which is quite nice.

**Dave Jones:** And there's the input jacks. I like them with the O-ring seal around the edge like that. And the input circuitry, we can finally see that. There's four PTCs up here, no less than four all individually heat shrunk.

**Dave Jones:** There's another input fusible resistor here and that's lovely, nicely heat shrunk there. I love it. It's got the turrets in there. It's not in It's not soldered directly into the board.

**Dave Jones:** It's in there They've gone to the effort to put the PCB turrets in there, which help support the resistor. I love it. There's your 10 amp current shunt. That that would have been tweaked to actually get the accuracy required.

**Dave Jones:** There's another couple of input power resistors over here and it's really I'm quite impressed. Agilent have really upped their game on the input input side of things. I really can't fault that at all.

**Dave Jones:** And it looks like are they a couple of gas discharge tubes as well. Brilliant. And the main processor is an NEC 78F0485, which is a 78K series micro. So, it not terribly unsurprising, I guess.

**Dave Jones:** Some classic 74HC595 devices up here. Fantastic. I love it. I don't know what this does. It's an ATMLH um 9362, it says. But, really I don't know. I presume it's uh the voltage reference.

**Dave Jones:** I presume this is another voltage reference over here. But, apart from that, there's not much else on the bottom of the board. There's a couple of diodes over here.

**Dave Jones:** And that about does it. So, overall, I'm very very impressed with the layout of this board. Layout, uh component selection choices, soldering is first class. There's no soldering residue.

**Dave Jones:** The design I I can't really uh fault it at all. Um probably the only thing which I said they could have could have refined a bit more is not to have the uh flying lead here going over to the piezo buzzer.

**Dave Jones:** Cuz they've gone to the effort to do the uh battery and the backlight LCD and stuff like that with the uh spring terminals. So, I don't know why they didn't go the whole hog there.

**Dave Jones:** But, apart from that, it's a beautifully designed meter. And the LCD sort of hinges back into place with these nice little retention hooks on the end here. So, you just slide it in there like that.

**Dave Jones:** And it's got some actual alignment tabs there. And they go into little cutouts in the board. And the LCD can't move. Nice design. Even with the lack of support for the PCB, it's only held in with a single screw down here.

**Dave Jones:** Once it's in these retaining hooks on either side here, it is actually quite rigid inside there. I'm quite I'm quite surprised. Um they've really done well to get it like that.

**Dave Jones:** I think it's by design and not really by accident. And there are the additional support posts here which would actually help actually press the board and sandwich it inside the case.

**Dave Jones:** So, to stop it to stop any vibration modes and things which are set up when you actually drop the thing or heaven forbid you do actually vibrate it during transport or something like that.

**Dave Jones:** Really seems like a nice solid design. And it's back together. No screws left over. It's really nice and tight. I love it. Let's turn it on and see if it works.

**Dave Jones:** It works. Beauty. So, there you have it. And you probably don't need to guess my verdict. It was pretty clear. I thought this was a superbly designed and built meter.

**Dave Jones:** One of the best I've seen. I really like it. Hats off to Agilent, the design team there, for doing this. I like it. It feels like it's designed properly.

**Dave Jones:** Feels rugged, solid. I guess time will tell. Is it as good as construction quality as Fluke? Well, it's I think it's pretty much on par. But yeah, time will tell in terms of ruggedness and ruggedness and product reliability and stuff like that.

**Dave Jones:** It's a completely new design. It, you know, it needs to prove itself. But really, I couldn't fault it. And if you like my videos, don't forget to subscribe to the YouTube channel.

**Dave Jones:** There's a subscribe button just up there somewhere where you can sign up to the RSS feed, the podcast, iTunes, whatever, the Facebook page. I'm on Twitter. I tweet a lot.

**Dave Jones:** So, make sure you sign up, comment, rate it, thumbs up, all that sort of stuff. Thanks. See you.
