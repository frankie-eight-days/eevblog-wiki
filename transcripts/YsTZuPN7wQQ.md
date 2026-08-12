---
video_id: YsTZuPN7wQQ
title: EEVblog #171 - Agilent U1272A Multimeter Teardown
url: https://www.youtube.com/watch?v=YsTZuPN7wQQ
source: youtube-asr
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, it's product teardown time. Yes, teardown, not product review, cuz I think I've decided for most products

**Dave Jones:** that are going to require a fairly in-depth review, my reviews are a bit too long because they include a quite a substantial teardown as well. So, I thought I'd just separate them out into product reviews and product teardowns

**Dave Jones:** cuz there's some people who like the shorter videos and they just like the teardown. So, it's teardown time today. It's the new Agilent U1272A multimeter. Uh it's not that new. It's been out for quite a few months now, but

**Dave Jones:** it's Agilent's big push into the Fluke 87 market. They directly pitch this against the Fluke 87 and we'll go into that in the review. And it's comes from the um it's completely redesigned by Agilent. It's not just an

**Dave Jones:** existing Escort design when they bought the uh existing Escort design group. So, let's tear it down and check it out. And before I do that, just a quick peek over the unit here. Let's have a look at it.

**Dave Jones:** It's quite a nice design. I really uh like the new uh styling of its design to grip in your hand like that and it does feel really rugged. And we'll go into the uh review of it later. But um and uh

**Dave Jones:** I just like to say thanks to uh Trio uh Smart Caul here in Sydney. In fact, they're just around the corner from my place. Actually, they gave me this one for review. So, if you're after uh any meters at all, there's no point actually

**Dave Jones:** uh importing them directly from the US or directly from China anymore. These meters are now not only these, but uh other test gear are now so cheap in Australia, you don't have to import them in So, thanks Trio Smart Caul. Check him

**Dave Jones:** out. So, let's open this thing up and take a look at what's inside. Oh, look, you can get the reflection of my boom of of my camera and there's my boom mic. Neat. These feel like self-tappers to me. They don't feel like metal inserts.

**Dave Jones:** Am I right? Yes, I'm right. There you go. Self-tapper. Pretty standard sort of stuff. Nothing unusual there, but because the fuses are actually in the compartment, you don't have to worry about opening the case like you do on

**Dave Jones:** say the Fluke 87 unit. Now, that was surprisingly hard to get open. I couldn't actually pry that end off. I had to sort of lever it up like that until it sort of snapped out and luckily I didn't snap anything at all.

**Dave Jones:** So, it would have been nicer from a disassembly point of view to put screws in there, but considering that you know, you really don't have to open this thing, then it's not really a problem. So, here it is. Ta-da!

**Dave Jones:** And my first impression upon cracking this thing open is I'm actually very very impressed. I like it. It's got everything and well, it seems to be doing everything right. They really don't seem to have cut any corners at

**Dave Jones:** first glance at all. We've got the shielding up here. We've got the spring terminal which connects to the shielding. We've got the huge HRC fuses here which we'll look at in a bit more detail. We've got I love the gold plated

**Dave Jones:** battery contacts like that. That I love these battery contacts that don't use any wiring at all. They just use these spring terminal clips to actually when they press down, they press on the PCB. I love that. That's what Fluke are doing

**Dave Jones:** in their new Fluke 28 and their Fluke 17 and other meters like that. And really the only bit of wiring they've got in it is going to the piezo buzzer up here. They've got a nice little connector on it. It's not just

**Dave Jones:** dodgily soldered onto the board like this. It looks like a real high-quality connector. There's a programming interface. They've actually used a connector for that, but we'll go into that when we look at the board in more detail. They've got a secondary board up

**Dave Jones:** here for the input connectors, and they seem to be doing everything right. Although, I can't see any input protection devices on the top uh apart from this huge uh fusible resistor up here. That's like the low-value 1 K or

**Dave Jones:** less input fusible resistor. That's about all I can uh see up there in terms of that, but we might have to uh flip the board open to see what's on the bottom. Um but, I'm impressed so far. And they've done the case right. It's

**Dave Jones:** got the um it's got this extended part here, which goes into the case to form some blast protection around the outside of the unit in case of uh gross overloads. It's It's not actually just a a press-together case, but I expected,

**Dave Jones:** even though it's not waterproof, uh given the O-ring on the battery compartment, I expected there'd be a full O-ring around the outside of it. But, if you take a look here, it's not an O-ring. It's like um tape. It's like

**Dave Jones:** that uh plumber's tape like you use when you're um doing up a, you know, a a a tap when you're actually doing plumbing and stuff like like that uh Teflon sort of tape. So, I guess That's the first

**Dave Jones:** time I've ever seen that. And And the tape goes all around the outside like that instead of an O-ring. That's the first time I think I've ever seen that used in any product. Uh maybe they've um they didn't go because it's not actually

**Dave Jones:** waterproof, they don't actually need an O-ring. Maybe they've actually gone for just a Teflon tape, maybe to because it is uh dust proof, apparently. I still I what the IP rating is, but maybe they've done that to keep out the dust, but

**Dave Jones:** um if they used an O-ring, it wouldn't have worked unless um there was some weird molding in there because you need a flat surface for O-rings, and this bottom of the case is flat all the way along, but look, then

**Dave Jones:** it just curves down like that and goes around. So, uh and and O-ring um seal really wouldn't have worked on that anyway, but they've used Teflon tape. Find that rather unusual, but anyway, I don't mind it considering that's not a

**Dave Jones:** waterproof meter. And there it is, you can see some of that Teflon tape just sticking out of there like that. One of the first things I noticed that's different to most multimeter teardowns is that there's no main IC on the bottom

**Dave Jones:** here. They've just got and in fact, a quite an excessive uh number, not that that's a bad thing, I guess, but an excessive number of discrete uh SO packages and the and the passive components. They really haven't pushed

**Dave Jones:** the limits of the um of the design. So, they're not using 0402 components, they're sticking to big, nice SO packages, which are uh cheap, available, easy to solder, easy to repair, um and and likely give you a much higher uh

**Dave Jones:** yield in production as well. If you compare it to, you know, if you're trying to use some little BGA part or something uh silly like that. So, this almost is is if like it's an LCR meter in terms of uh

**Dave Jones:** the number of um discrete devices. So, it is a very discrete design. Uh I presume the main processor is on the bottom here somewhere. Here's presumably, it's not labeled, but that will be like a JTAG or an in-circuit programming header, I

**Dave Jones:** would presume, for the micro that's uh on the bottom. I would expect to see an off-the-shelf micro like an MSP430 or something like that. We'll find out when we flip the board over, but uh uh yeah, it's there's just lots of passive

**Dave Jones:** circuitry. The board is very clean. It seems like it's well laid out. Uh there's no solder residue on it at all, and I'll go into the individual components a bit later. There's a couple of um surface mount electrolytic uh caps there. There's a

**Dave Jones:** few components aren't missing, and rather unusual, this thing is rather curious here. It's got like an exposed uh gold pad here with this large uh large package capacity here, and another capacitor that goes off to this rather unusual thing which uh it's almost like

**Dave Jones:** a sensor pad which goes off under the bottom. Uh presumably goes under the board there somehow, and it's connected in here, and it's isolated, and they've taken off the uh solder mask, and they've taken off the ground plane, and

**Dave Jones:** and on the input side of the design, they've actually done a pretty good job. I like it. They've got this secondary board up here, which you don't see all that often. Uh and the contacts are made with these uh brass uh

**Dave Jones:** standoffs here, which go from the top of the board to the bottom. And because they are split uh contact input jacks, I don't know if you can see in in there, maybe not, but they are actually split uh jacks two-sided, so they use that to

**Dave Jones:** detect which uh side of the uh where if a if a probe is actually plugged into it, and because you don't need that on the voltage, only need that on the amps, they joined them together like that. But

**Dave Jones:** over here, they are separate, and they would actually tap uh those off to a sensor. They go through to and there's the two sense pins which go through to the board like that, but I I rather like that. Um it seems very solid. It looks

**Dave Jones:** like there's um some O-rings possibly around the input sockets as well, but considering that they've designed this to be sort of splash and dust-proof and things like that over the Fluke 87, uh that's I that's something that you'd

**Dave Jones:** expect. They've got the two big HSC fuses, 440 mA and 11 A. I love it. They've got the high-voltage isolation there with the extruded plastic uh coming through as well. There's a lot of thought gone into that. I presume the

**Dave Jones:** input protection devices are around here and they're on the bottom side of the board. We'll find out that when when we flip it open, but I like that. I'm quite impressed. And if you look down there, it is actually a rev 004 board. So,

**Dave Jones:** they've had a few uh goes at this. They have actually refined it. It hasn't been out all that long, but they probably would have went through uh three or four four refinements before they actually released it to production.

**Dave Jones:** And there's the standoffs uh for the uh serial communications interface. You can actually buy a very cheap USB uh interface for it, and uh that just goes through hooks up to the bottom like that, and that's just your typical um

**Dave Jones:** RS-232 type uh isolated optical interface. Let's go through the devices on the board here, shall we? I won't show you all the parts up close cuz it's really hard to get a good image of the uh chip number on the device, but I've taken a

**Dave Jones:** look at them, and they must be big fans of Maxim. They've used lots of Maxim parts on here. Um I don't know. Maybe they got a bulk discount, and uh presumably no supply problems cuz you can buy these meters, so go figure.

**Dave Jones:** Um down here we've got a MAX uh 4611, which is a uh quad switch. There's quite a few. There's one here, one here, uh one over here. There's one there. And uh well, what else have we got? We've got a

**Dave Jones:** MAX 4582, which is an eight-way mux here. We've got another one here. We've got a 4,000 series um CMOS device, a 4053 here. Excellent. Got to have one of those on every meter, I think. Think it's compulsory, pretty much. There's a

**Dave Jones:** 74, couple of 74HC series logic here, a HC132 here, a HCT74 here. There's another Maxim mux up here, the 4583. There's another 4583 there. And there's a 7600 switch capacitor voltage inverter here. And this is the ADC. It's actually an

**Dave Jones:** SPI TI part. It's the ADS 1242. And it's a 24-bit four-channel ADC. It's got a built-in programmable gain amp. It's got 600 microwatts power consumption, which is necessary in a battery-powered device like this. 21 effective bits. 50 and 60

**Dave Jones:** hertz rejection built in, so you don't need to actually select that in the software. It's got both both mains frequencies built in, so it rejects those. A lot of meters on the market will actually have a menu option

**Dave Jones:** to select 50 or 60 hertz rejection. You don't actually need that need to do that on this meter. And there's a Burr-Brown OPA340 here. And down here it looks like I think it's a Maxim LM285 1.2 volt voltage reference, but it's a pretty

**Dave Jones:** crude uh voltage reference, that one. So, it's obviously not used for the ADC up here. The ADC has to have another another precision voltage reference around it, but I can't really see one there. Maybe it's on the other side of

**Dave Jones:** the board. And one of the other big things you'll notice missing well, from the top side of the board anyway, is the thick film precision resistor network. We can't see it yet. It's got to be on the bottom there somewhere.

**Dave Jones:** And for the true RMS conversion, there's a bog standard AD637 true RMS converter chip there. No surprises in that.

**Dave Jones:** Well, that came apart quite easily. There's a couple of clips here on the side which actually retain the board, three self-tapping screws, and there's the LCD module with the zebra strips in there which actually connect through to the board. Oh, sorry, it's only the top

**Dave Jones:** one there. As you can see the contacts on the board up there. And it's pretty typical construction. There's a few looks like they've individually barcoded the internal parts there. The range switch is fairly typical. Um they've got, you know, fairly good

**Dave Jones:** quality sort of brass contacts in there. I don't mind it at all. Looks like fairly good quality plating on the board itself. But once again, there's not any significant current actually going through that. It's just It's It's really just a signal thing.

**Dave Jones:** And they have actually labeled a bit of attention to detail there. They've labeled the individual channel positions like that. I like it. And it looks like I was way off the mark with this shielding thing here. It's It's just an extra shield on the top

**Dave Jones:** which actually connects via this spring here. And um really it has nothing to do with this weird sort of pad configuration on the top that actually that actually connects through to a cap a large cap on the top side of the

**Dave Jones:** board. And I really like the design effort they've put into the backlight. Once again, they've eliminated the wiring with these two spring terminal interfaces here which connect through to the backlight on the LCD. And then when it presses against here they just match

**Dave Jones:** up to the mating contacts on the board. Really good design practice, really good attention to detail. Curiously, they've added a plastic spacer up here. I'm not sure exactly of its function. Maybe it's a afterthought, I don't know, or maybe

**Dave Jones:** it's purpose designed into the unit itself. I'm not quite sure. No surprises at all. There's the thick film resistor network, but it does have a rather nice shield over the top of it. I love it. And there are multiple

**Dave Jones:** contacts in there. There's one at the end there and there's multi You can't really see it, but there's multiple ones in there cuz these thick film resistor networks set the range precision because you got one voltage reference and then

**Dave Jones:** it gets divided down for the various ranges. So there's multiple laser trimmed resistors on this hybrid substrate in there and that pretty much along with the along with the main voltage reference determines the accuracy and the long-term stability of this, but they've

**Dave Jones:** gone to a lot of trouble to shield that, which is quite nice. And there's the input jacks. I like them with the O-ring seal around the edge like that. And the input circuitry, we can finally see that. There's four PTCs

**Dave Jones:** up here, no less than four all individually heat shrunk. There's another input fusible resistor here and that's lovely, nicely heat shrunk there. I love it. It's got the turrets in there. It's not in It's not soldered directly into the board.

**Dave Jones:** It's in there They've gone to the effort to put the PCB turrets in there, which help support the resistor. I love it. There's your 10 amp current shunt. That that would have been tweaked to actually get the accuracy required. There's

**Dave Jones:** another couple of input power resistors over here and it's really I'm quite impressed. Agilent have really upped their game on the input input side of things. I really can't fault that at all. And it looks like are they a couple of gas discharge tubes as

**Dave Jones:** well. Brilliant. And the main processor is an NEC 78F0485, which is a 78K series micro. So, it not terribly unsurprising, I guess. Some classic 74HC595 devices up here. Fantastic. I love it. I don't know what this does. It's an ATMLH

**Dave Jones:** um 9362, it says. But, really I don't know. I presume it's uh the voltage reference. I presume this is another voltage reference over here. But, apart from that, there's not much else on the bottom of the board. There's a couple of

**Dave Jones:** diodes over here. And that about does it. So, overall, I'm very very impressed with the layout of this board. Layout, uh component selection choices, soldering is first class. There's no soldering residue. The design I I can't really uh fault it at all. Um

**Dave Jones:** probably the only thing which I said they could have could have refined a bit more is not to have the uh flying lead here going over to the piezo buzzer. Cuz they've gone to the effort to do the uh

**Dave Jones:** battery and the backlight LCD and stuff like that with the uh spring terminals. So, I don't know why they didn't go the whole hog there. But, apart from that, it's a beautifully designed meter. And the LCD sort of hinges back into place

**Dave Jones:** with these nice little retention hooks on the end here. So, you just slide it in there like that. And it's got some actual alignment tabs there. And they go into little cutouts in the board. And the LCD can't move. Nice design.

**Dave Jones:** Even with the lack of support for the PCB, it's only held in with a single screw down here. Once it's in these retaining hooks on either side here, it is actually quite rigid inside there. I'm quite I'm quite surprised. Um

**Dave Jones:** they've really done well to get it like that. I think it's by design and not really by accident. And there are the additional support posts here which would actually help actually press the board and sandwich it inside the case. So, to stop

**Dave Jones:** it to stop any vibration modes and things which are set up when you actually drop the thing or heaven forbid you do actually vibrate it during transport or something like that. Really seems like a nice solid design. And it's back together. No screws left

**Dave Jones:** over. It's really nice and tight. I love it. Let's turn it on and see if it works. It works. Beauty. So, there you have it. And you probably don't need to guess my verdict. It was pretty clear. I thought this was a

**Dave Jones:** superbly designed and built meter. One of the best I've seen. I really like it. Hats off to Agilent, the design team there, for doing this. I like it. It feels like it's designed properly. Feels rugged, solid. I guess time will tell.

**Dave Jones:** Is it as good as construction quality as Fluke? Well, it's I think it's pretty much on par. But yeah, time will tell in terms of ruggedness and ruggedness and product reliability and stuff like that. It's a completely new design. It, you know, it

**Dave Jones:** needs to prove itself. But really, I couldn't fault it. And if you like my videos, don't forget to subscribe to the YouTube channel. There's a subscribe button just up there somewhere where you can sign up to the RSS feed, the

**Dave Jones:** podcast, iTunes, whatever, the Facebook page. I'm on Twitter. I tweet a lot. So, make sure you sign up, comment, rate it, thumbs up, all that sort of stuff. Thanks. See you.
