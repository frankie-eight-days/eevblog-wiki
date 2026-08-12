---
video_id: 0Pplmg9Seao
title: EEVblog #417 - Fluke CNX3000 Wireless Multimeter Teardown
url: https://www.youtube.com/watch?v=0Pplmg9Seao
source: youtube-asr
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. It's not every day we get to teardown a Fluke multimeter, but yes, we've got one, the new CNX 3000, and it's wireless. So, we've got all the wireless attachments. We've got five items. Can you believe it?

**Dave Jones:** Ah, you know what we say here on the EEVblog? Don't turn it on. Take it apart. And here it is in its nice little padded bag. We've got the Fluke CNX 3000 meter. We've got the CNX i3000 wireless flex current clamp. We've got

**Dave Jones:** the CNX A3000 wireless AC clamp. And you guessed it, they keep calling them the 3000. Get out of here. Tight fit. We've got the CNX T3000, which is a K-type thermocouple temperature wireless adapter. And we've got the CNX

**Dave Jones:** V3000, which is a wireless AC voltage. That's all it does, it just measures AC voltage. And we've got all the bits and bobs as well, including this flexible current clamp. How do you do it? There we go. Just pops out like

**Dave Jones:** that. Goes in there. You lock it, and that's actually a current clamp up to That's the i2500-10, 2500 amps. So, woah, we can attempt to teardown. Well, we can't teardown this. This is actually molded sealed. So, let's teardown these and see what we've

**Dave Jones:** got. A new Fluke. Beauty. And here it is, the CNX 3000 wireless multimeter. Check it out, it's got a dot matrix display. I won't turn it on, cuz that's not in the spirit of Teardown Tuesday, but there it is. Ta-da! It's

**Dave Jones:** got the big new Fluke button on it for the wireless button, but apart from that, it's kind of like the equivalent of the Fluke uh 70 series really. So, it's effectively like a wireless um 70 series. That's what they want uh you to

**Dave Jones:** think anyway. Like instead of buying just a regular um you know, Fluke 70 series electrical multimeter, uh for a bit more you buy one of these instead and if you want then you can buy all the wireless accessories later. That's their

**Dave Jones:** plan anyway, I think. So, let's take a look at it. It's uh changed a little bit. This won't be a review of course. I don't like that tilting bail there. That's a bit of a uh And once again, that just uh that does

**Dave Jones:** actually uh break off. Can actually break that off. It's got a magnetic uh hanger as you saw hanging around my neck at the start of the video. All of these have uh magnetic hangers on them and uh couple of screws in there. They're

**Dave Jones:** probably self-tappers again, but uh we'll find out and let's have a look inside the battery compartment. Oh, look at that. Oh, look at that. It just like rises up. Watch this. Oh, look at that. Beautiful. And that just pops out there and three double A

**Dave Jones:** batteries. But what's missing here? Fuse access. Ah, fail. They've put some uh little spongy stuff. It's not actually rubber. It's I you know, it's just like foam uh stuff around the outside of that. So, that's what gave it that

**Dave Jones:** little whoop hydraulic uh lift thing. That's just to keep out uh dust and crap out of this thing. There you go. Looks like the uh I do like these. The um um uh battery contacts there are soldered directly down onto the board. You can

**Dave Jones:** see that in there. So, let's whip it apart and have a look. Yes, it does feel uh real nice and solid like a proper Fluke should. So, no worries there at all, folks. They usually don't disappoint on that

**Dave Jones:** front. So, we'll whip these out. These feel like self-tappers to me. Yeah, self-tappers. They're really Yep, the uh Yep, the classic Fluke self-tapper, the same design as all their other ones. So, they haven't haven't decided to change that at all.

**Dave Jones:** Interesting to see. I mean, this is a CAT uh four rated 600-V CAT four, so I'd expect to see some decent uh input protection circuitry, decent clearance, maybe a blast shield or two, and a uh lots of big MOV protection, all the

**Dave Jones:** usual jazz. Of course, the two HRC fuses. They'll all be in there. And uh not much else. Probably powered by an MSP430 again, would be my guess, like they do on the uh other Flukes. So, why not? So, let's try

**Dave Jones:** and get this sucker apart. I hate that you have to take off six self-tapping screws just to change the fuses. That's just, you know, that's really not on. Um they should have designed that uh bigger. You know, they could have had

**Dave Jones:** two fuses across there. They could have designed a bigger battery compartment. Uh Bob's your uncle. Maybe had the batteries across that way, so you didn't need as much height. I don't know. They could have done it if they really wanted

**Dave Jones:** to. But, hey, tada! There we go. There's not much doing. There's no internal uh shielding on the back side of the case there. So, it's all on the board. Look at that. Not much at all, but hey, you don't need

**Dave Jones:** need much in a modern Fluke multimeter. And of course, there's one thing I uh forgot to mention on the front of this thing. It does milliamps only. There's no microamps, of course. It's not designed as an electronics multimeter,

**Dave Jones:** so that's fair enough. But, there's no 10-A range at all. It's just milliamps. That's it. 400 milliamps max is probably a couple of ranges in there, you know, 44400 or something, but ah, man, come on. So, the input front

**Dave Jones:** end here isn't very exciting at all. Yeah, we've got the usual 440 milliamp HRC fuse here. We've got the input thermistor. We've got the input protection resistor. We've got our fixed current shunt there because well, you don't need a 10 amp and multiple current

**Dave Jones:** shunts to be switched into place. Um, and we've got our three mobs there and well, that's all there is to it. It's pretty boring, actually. We've got a uh little isolation shield there, which is a little bit of a blast shield, I guess

**Dave Jones:** you could call it from the thermistor here and but it's just, you know, so it doesn't get bent over onto the precision high value resistor in there. There it is, metal shielded, of course, um to help get the noise down, but yeah,

**Dave Jones:** that's about it. We've got That's probably the That might be the wireless under there. We've got that under the under a shielded can. We might be able to get a look at that later. I don't know. There's some circuitry around

**Dave Jones:** here. Obviously, that's connected into the battery there. We've got a little polyfuse there and we've got a DC-to-DC converter just around there and some regulation there by the looks of it. So, that's all pretty standard. And up here,

**Dave Jones:** we've got a little module which looks like it's in a socket. We'll take a look at that in a minute. This is wiggling around there. I don't I don't like that at all. I think it'd vibrate out of

**Dave Jones:** there. Not too happy. Um, hey, no surprises, MSP430 processor there. We've got our big buzzer there. We've got a secret cow button. Looks like there's a little cow pad there. Did I Was there a matching uh button on the back? Little secret button

**Dave Jones:** there? No, that No, there's nothing there. So, yep. I don't know why they've done that as like a button uh type pad there, but anyway, um there's the um in-circuit uh programming uh JTAG port there for the MSP430.

**Dave Jones:** We've got this going off here. It's probably for the uh backlight. And then uh this going off to the LCD display by the looks of it. And really, there is not much in there at all. As I said, I

**Dave Jones:** do not like this module one bit. Look, it's just sitting there. You can just wiggle that back and forth. That would easily vibrate loose. Trust me. I'm not putting much force in that at all. What's But, anyway, um there we go.

**Dave Jones:** There's our um little uh antenna down there. And uh that is our uh wireless module inside that can. Looks like we can't get that off unless we uh desolder the can there. Yeah, I don't know what type of connector

**Dave Jones:** that is. Um I don't know. I It's probably not a custom Maybe it's a you know, it is uh designed for something else. But, if anyone knows what that connector is, let us know. So, if that other little

**Dave Jones:** plug-in module was our uh wireless interface, what's going on under that can down in there with that uh QFN package? I'm not sure. Maybe the uh true RMS converter or something. I can see a couple of uh large SMD caps under there. But, in the

**Dave Jones:** input jacks there, absolutely nothing uh special at all. But, there's uh nothing wrong with them. They're not quite as rugged as the other uh some other Fluke meters. But, uh yeah, they're not too bad. They're Of course, everything's

**Dave Jones:** just beautifully soldered in there. Really, you heard that one go crack, I'm assuming. And uh I don't see a shake-proof washer under there, though. But, uh that is pretty darn good. They go in there nice and solid. Well, that That is wiggling. Is that me

**Dave Jones:** wiggling the unit or is that Yeah, that's me wiggling the whole thing. There you go. They're pretty good. We're going to see down inside the jack there. They're all nice and solid. No problems whatsoever. Not the crap split

**Dave Jones:** type. Good solid input jacks. And just as an aside, you can see the solid metal molded in threaded insert in there. Very nice for the input jack. I like it. Now, you notice something here. Small attention to detail they've paid in the

**Dave Jones:** design aspect of this thing. Here's the common terminal. Here's the milliamps terminal over here, and this is the voltage terminal. Now, the voltage terminal is the only one that has this raised bit of plastic around it. Now, that is

**Dave Jones:** not for support or anything else. It's actually a little arc shield between the pointy, you know, the sharp points of the metal contact down there and the fuse here. So, there you go. They've just put a little bit of attention to detail.

**Dave Jones:** They've gone, "Aha, we can have potentially there's that air gap there. It's quite significant, but it's a potential arcing point. So, we'll just put in that little bit of extra plastic around there just for the sharp corners because primarily

**Dave Jones:** sharp corners are where arcs are going to high voltage arcs are going to appear from, and they can just you know, kill that by just raising that plastic there. It doesn't cost them anything, but you've got to think about that at the

**Dave Jones:** design stage. And it's not just that either. They actually back it up with check it out. A matching one in here as well. That uh they've got that shield there and that one. So, it really you know, this is why it's CAT IV rated

**Dave Jones:** because there's no way it's going to arc from that jack in there over to that fuse holder in here. It's just not going to happen. And you'll notice some other uh, design and build quality things here. They've also got these shields

**Dave Jones:** that just hold in place around the mounting posts down there. They've got them on, uh, both sides of the unit. So, when you put this in here like this, you put in there like that, it fits over that mounting post and just provides a

**Dave Jones:** more rigid, uh, invi- you know, less, uh, movement room so that when the thing gets shocked, it's, uh, you know, and the case maybe gets, uh, uh, warped a little bit, it's, you know, it that mounting post just isn't

**Dave Jones:** going to break off. And the mounting post is molded integrated with the side of the case there, and it's, you know, it really is quite solid. They've, you know, the mechanical person who's, uh, who's designed that really knows what they're

**Dave Jones:** doing. I really like it. And there's the wireless module there, and of course, it's a, a, uh, Zigbee, uh, type. It uses the Zigbee, uh, hardware layer, but it does use a proprietary, uh, Fluke protocol layer called the FWCS.

**Dave Jones:** So, they don't, um, plan on opening, uh, that up, but they say it's not very difficult if you want to, uh, if you did want to tap into it or, uh, something like that. So, there's our little, uh,

**Dave Jones:** surface mount Zigbee antenna there, and it's all under the shield, and that is bummer, soldered down. Well, I've got a soldering iron, and there's no huge surprises there. It's an off-the-shelf Texas Instruments CC2530F128, and that is a, uh, Zigbee controller

**Dave Jones:** chipset. It's actually an 8051, uh, processor, 128K of flash, and all sorts of paraphernalia built in. We'll take a look at the block diagram in a second, but you can see the, uh, they've got an oscillator there. It's probably, uh, 32,

**Dave Jones:** uh, MHz oscillator. Is that another, uh, crystal there? Possibly for real-time clock. And up here we've got our programming interface, so you could just, uh, solder a connector directly onto that and, uh, hack this thing if you, uh, were really that way inclined.

**Dave Jones:** But, uh, apart from that, there's not much else on there. And there you go, there's the 32 MHz crystal oscillator. And there's the other crystal there, and it's got 24324 marked on it. And, uh, I entirely expected that to be a 32.768

**Dave Jones:** kHz watch crystal there. But, um, it Maybe it is, and it's just, uh, marked differently. I mean, there's 32 there, so I don't know. Um, I think it's probably got to be. And here's the block diagram for this thing. As you can see,

**Dave Jones:** it's got pretty much everything but the kitchen sink. We've got reset, watchdog timer, two oscillators, uh, mux and calibration, on-chip, uh, voltage regulator, uh, brownout, we've got sleep timers, power management, and memory memory arbitrator, an 8051 CPU core, 8

**Dave Jones:** KB of SRAM, 100 and this one has 128K of, uh, flash. And we've got interrupt control. There's a fairly powerful DMA in there. There's an analog comparator. There's an op-amp. There's a 12-bit, uh, delta-sigma ADC. It's got AES encryption

**Dave Jones:** and decryption. Um, I don't think this thing uses the encryption at all. I think it is, uh, sent as plain text. So, I you know, so you should be able to read it. If you can intercept it, you

**Dave Jones:** can probably, uh, read the data. It's got the radio registers, uh, CSMA, all that sort of stuff, radio interface, uh, demodulator, ADC, receive chain, the frequency synthesizer, the transmit, the modulator. Ah, it's all there. FIFO and all the

**Dave Jones:** frame control to handle all that, plus a couple of UARTs thrown in, couple of four timers in there, and whoa, Bob's your uncle. And these little surface-mount crystal packages seem to be all the rage these days. I I rather like them, actually. They're

**Dave Jones:** quite neat. And here we go. We've got the board out. Got a bit more circuitry on the back, which we'll take a look at. And here's the LCD, and interestingly, the LCD just sits in there like that, and it's it's just uh pushed in place,

**Dave Jones:** held in place with that foam back, and that's very un-Fluke-like. Um you know, I would have expected to see that on cheaper meters. I don't know why they've decided to do that, but anyway, they have. It's a LCD's manufactured from uh Handtronix.

**Dave Jones:** They're a a large uh manufacturer of reputable manufacturer of displays. Hello, I can see myself. Hello. And there we go, it's chip-on-board. You can see the You can probably see the little chip in there. There we go, it's

**Dave Jones:** all potted up in there, but that's a This is a dot matrix display, of course. I'm not sure of the exact resolution on it, but there you go, we've got a huge even backlight on the back of that thing, so they

**Dave Jones:** expect that to be nice and even, but apart from that, there we go, we'll take a look. Got a bit more circuitry on the boards up And standard Fluke range switch, by the looks of it. If we take a look down

**Dave Jones:** here, there it is. Standard fare. They haven't uh they haven't rocked the boat there at all. It's exactly the same as the mechanism they've been using for a long time. Not a problem. So let's take a look at the boards. And

**Dave Jones:** of course, we find our standard diode bridge plus one extra diode in there for our fuse protection as well. When the fuse blows, and they've used some much larger MELF resistors there, the old MELF package. I do like the MELF

**Dave Jones:** package, and they've used that to get high voltage, of course. They've put them in series there. There's where that uh uh blast shield goes around there like that. We've got a guard ring going around that. That's our um thick film hybrid resistor network on

**Dave Jones:** the top. That's also shielded. But apart from that, there's not much else on here. There's a couple of little uh uh components around, couple of LEDs. You'll notice that uh Note the uh soft button up there. Check that out. They've just uh put the LED

**Dave Jones:** directly in the middle, which of course lights up through the uh rubber through the clear rubber uh button on there. But, they've got still got the same uh dual like, you know, similar sort of uh pattern on their serpentine pattern that

**Dave Jones:** uh allows them to detect the carbonized rubber on either side, which presses down and presses the button, but apart from that, it's boring, folks. Sorry, there's nothing under the rubber at all. And this thing hasn't been released very long, but check it out.

**Dave Jones:** They're up to rev eight. There's another guard ring up there. Don't know what that's guarding, but uh something under that can. Hmm. There we go. I've lifted up another shield, and it's the LTFLK2. It's a Fluke uh custom special under

**Dave Jones:** there. So, that would be doing uh the, you know, the input uh switching and uh probably uh some true RMS stuff as well. And on the bottom of the range switch there, very nice uh dual wipe contacts. Not a problem, and um looks like a very

**Dave Jones:** good quality gold plating on there on the board, as you'd expect. Sure, it's very thick. So, there you have it. That's inside the Fluke CNX 3000, and it's a classic excellent uh Fluke design and build quality. I uh rather like it.

**Dave Jones:** And in interestingly, um if you remember my uh Fluke uh 28 Series 2, um these inductors here seem to be a uh weak point in the design in terms of uh uh shock because that inductor actually broke uh twice on me, very similar

**Dave Jones:** inductor, cuz ferrite is quite uh brittle. So, you know, in terms of uh shock, you know, that's probably one of the uh first things to go, actually, surprisingly. Um would be that ferrite inductor there. As you can And if you

**Dave Jones:** haven't seen it, uh see my Fluke 28 uh torture video where I take it through a canyon and drop it, do all sorts of things. Yeah, that sucker broke twice. So, there you go. But, anyway, thumbs up. That is uh superb classic Fluke

**Dave Jones:** build quality. Can't be beat. And yes, folks, it does work when we turn it back on. Ta-da! There it is with its uh dot matrix display. Mm, not too happy with that, but yeah. Anyway, so this is the CNX a3000

**Dave Jones:** wireless clamp meter uh 400 amps uh CAT III 600 V CAT IV 300 V rated. Of course, classic uh you know, clamp configuration like that. We'll get in there. You can have a look at the uh laminated cores inside there. So, we'll

**Dave Jones:** crack this open. And by the way, um yeah, these things do have data logging. And the data logging is done, if you're curious, is done internally to all of these remote units. The uh CNX 3000 multimeter itself does not have logging

**Dave Jones:** capability. It just acts as a star net uh the the star controller for the wireless network. And that's pretty much it. So, yeah, the multimeter itself, no data logging, but these things do have data logging built in. So, let's check it

**Dave Jones:** out. And uh we'll open this up here. Battery compartment. Ta-da! Two double A's. Nothing very exciting there. Three screws, and we'll lift this sucker right out. And there you go. You can see the uh laminated core right down inside the clamp there.

**Dave Jones:** And that goes all the way There's multiple laminations in there on both sides. And that goes all the way around to the sensor, which will be in the main unit itself. Ha ha! Look. There we go. We have the same module again. We've got

**Dave Jones:** a matching module. We won't have to take that apart again, I'm sure. Look at that. Quite nice uh build quality there. I like it. And that's a real nice big spring clamp mechanism. I don't think that's going to fail anytime soon. And

**Dave Jones:** yeah, I have no doubt that modules are absolutely identical. Um you know, might have some firmware differences of course because this isn't the star hub controller or something or maybe it is identical firmware. I don't know, but yeah, I'm

**Dave Jones:** not going to take the can off that. That'll be absolutely identical. Same connector system. And as with the CNX meter itself and all fluke meters, lovely deep ridges on the case there that go around inside there just in case

**Dave Jones:** there is any arc over or anything like that. It's not going to blow your hand off. It's going to be any explosion is going to be pretty well contained inside the case. Now, sorry folks, but I don't seem to be able to prize these two

**Dave Jones:** halves apart here. Maybe they're glued or thermally bonded or something like that after manufacture. I mean, you know, it it wouldn't surprise me. In fact, I'd expect them to be fused together somehow. So, sorry, I'm not going to be able to show you the

**Dave Jones:** hall sensor in there. Bummer. Actually, sorry, that's not going to be a hall sensor because this is not a DC current clamp. It's AC only. So, that's just going to be a current transformer in there, not a hall effect type. But

**Dave Jones:** that's fairly high quality construction here. Really, it should be fairly reliable. They've got a threaded metal insert down in there. Nice big solid threaded screw which, you know, holds the main pivot point for the main clamp down there. So, it should be

**Dave Jones:** really rugged and last quite some time. And we've found the memory there. It's an Atmel 25 DF081 and that's an 8 megabit flash memory, but it's very low voltage. It's a 1.65 V interface there. So, looks like we have

**Dave Jones:** a bunch of test points there. They may be for production or so or programming, something like that. I don't know. Soldering, of course, absolutely first class. Maybe we've got some sort of amplifier or something there, perhaps. But there's yeah, there's not much on

**Dave Jones:** here. Some more test pads down there, but there's not much on the top side here at all. So, we've got to find the processor probably on the bottom side. And that chip there's got 25 TI AFB on it. So, I'm not entirely sure what that

**Dave Jones:** uh sucker is. It looks like it's you know, it looks like some sort of regulator or something like that based on the huge uh uh tracks coming out of it and relatively huge and the uh caps as well, huge big ceramic cap

**Dave Jones:** there. We've got a tantalum on the input, so yeah, that's probably some sort of uh regulator. So, let's pop this thing over and uh see if we can look at the processor on the bottom. And there's the big Fluke button

**Dave Jones:** on the uh front there. And you can see it lights up, of course. There's there's the LED in the center of it and then they've got uh no less than uh four pads there. So, that's going to be a pretty

**Dave Jones:** reliable uh switch on that sucker. And there's the input there from the sensor and uh can see a uh resettable poly switch fuse there. Not much else, some analog uh stuff. Probably got some amplifiers in there and uh

**Dave Jones:** couple of miscellaneous components, but it looks like um the LCD is uh got a uh zebra strip in it and uh we're going to have to take out that. It's going to have the processor underneath the LCD cuz there's nothing else on this

**Dave Jones:** board at all. What's an Ardent A? No idea. And there's the LCD with the zebra stripes on it. Nothing much doing there. And if we have a look under the main board here, we can see the LED backlight on the thing. You can

**Dave Jones:** see the two LEDs up the top there. There they are. And yep, you guessed it, TI MSP430 yet again. Ah, and here you go, you can see that light pipe backlight there. The light enters along this edge here, and then it curves

**Dave Jones:** into there. And of course, they've got reflective strips along the outside there, which helps contain the light in the middle. And then it's emitted evenly, spread and should be spread fairly evenly. This little bit of rubber up under there, when you put those

**Dave Jones:** together, it somehow holds that module in place. Like it puts pressure on it. I wonder if the CNX 3000 did that. Oh, I won't take it apart again. I'll have to review my photos or video footage. And sorry,

**Dave Jones:** folks, that's all she wrote on that. Nothing much more interesting to show you, I'm afraid. Next. Ah, if you want to see the screen on that, turn it on. Towards you, it's the A3000. And not much doing. Next up, the CNX V3000

**Dave Jones:** wireless AC voltage. That's all it does, folks, is measure AC voltage. Cat 3, Cat 4, 600 volts. That looks really nice and rugged. I like it. Yeah, they've all got these these magnetic hangers on them, of course, really super

**Dave Jones:** strong. And it latches onto the battery there. It's curious to note that on the clamp meter, they actually use one of these latching retaining hooks for the battery compartment, but on this one, old-fashioned screw. Go figure. But, it

**Dave Jones:** is at least metal threaded insert, so let's uh How do I God, how do you pop that open? Well, that's a bit That's a bit silly. There we go. Two AA batteries. And four screws. I think this sucker's

**Dave Jones:** just going to pop open. It's almost begging to be opened. Ta-da! And there we go. Ah, looks Here we go. We've got Of course, we've got the same module again. And yeah, look, we've got a little retaining That's that That's

**Dave Jones:** actually rubber. There you go. That's actually a rubber insert. There's the metal plate in there for the for the magnet system to retain against. And that's a little rubber molded rubber thing which then holds that module in place. All right, so we

**Dave Jones:** have our Zigbee module there. We have another DC-to-DC converter with the inductor there. We have There's a little poly switch down in there. Under there, we have exactly the same custom Fluke chipset as we saw in the multimeter. Got the programming

**Dave Jones:** header interface there. We've got the LCD on top once again. Wait, it's almost as if like you don't have to take it Not pointless taking the thing apart actually. You got No, it's going to be the same under there. It's going to be

**Dave Jones:** an MSP430 processor, and that's all she wrote. On the input side here, check this out. Of course, this is different because they've got like a different input connector form factor. But, this looks really solid. I like this. You

**Dave Jones:** know, big solid molded connection on there for the uh for those banana jacks. And really, there's you know, and they've bolted it directly onto the board there uh these two screws. And they've got one mouth resistor there. You'll notice that

**Dave Jones:** there's no what mouths on this thing at all, which is uh quite surprising all the way unless they're on the uh other side. But uh I don't see any through-hole uh pads for the mouths at all. So, there you go.

**Dave Jones:** All they've got is this uh mouth input protection resistor here. They've got an input uh cap and then uh AC coupling cap and then they've just got uh the hybrid uh thick film uh resistor divider network. And that's um

**Dave Jones:** that's pretty much all she wrote. I mean, but this thing doesn't have to do any uh range switching or anything, I don't think. Um well, a couple of lower ranges from the divider, but that's it. I mean, so really it's just fixed

**Dave Jones:** functionality, but I did uh expect to see at least some mouths in there. So, I don't know. Um Fluke know what they're doing on the input protection uh side of things. This is uh CAT IV 600-V uh rated. So, I guess

**Dave Jones:** they've determined uh that due to the limited functionality in this thing, they simply don't need input mouth protection. Now, this is a bit fascinating. Check it out. Here's the positive input uh jack here, and it just goes through that mouth resistor on the

**Dave Jones:** top in series with the mouth resistor, goes through that uh via, and then on a center layer around this cutout here, which has this uh rather large uh uh shield on it. Look, they've actually put like a blast shield around there,

**Dave Jones:** which then goes in the middle of the board. So, they're almost like that's like a fusible track or something. So, on gross overload conditions, that's designed to uh uh break, I'm assuming. Then there's the uh AC input coupling cap, of course, and

**Dave Jones:** straight into the divider. And you know, really that's all she wrote. And then they've got an inductor down here on the uh surface mount inductor on the negative line. But that's rather fascinating. There you go. Um that's all you need for a a fixed AC

**Dave Jones:** measurement. Uh you know, effectively like a multimeter input uh that only does um high voltage AC. But once again, folks, as you'd expect, very rugged, very rigid, well-designed case. I mean, even that half of the case, if I try and flex it like that,

**Dave Jones:** it's very strong, very rugged. I really like it. They've done the same uh thing around here with the post. Look at that. They've embedded them in there, so and then this is directly molded into the top side of that there. Very strong,

**Dave Jones:** very rigid. That's why when you put these together like this, and they go in there, and you know, and you try and twist these things, you just cannot, you know, there's no giving these. They're super strong, super rugged. I really

**Dave Jones:** love the design of this thing. And that input jack there, fully molded into the bottom of that. Look at that. There's huge big uh threaded inserts into that. Massive. I really like it. Solid. Last you a lifetime. And yeah, I'm not going

**Dave Jones:** to bother with the LCD. I did have a quick look under it, exactly the same MSP430 as before. So, next. Let's switch that one on as well. That's the V3000. Look like a U, but that's all they could

**Dave Jones:** do there. There you go. Terribly exciting. Volts AC. It's got a log button. It's got a RF Zigbee connect button and a backlight. And uh really, that's all there is to it. It's not that even, actually. You can see the hot

**Dave Jones:** spots on the LED there. So, yeah, that that light pipe, it works okay, but jeez, it's not as good as some meters, that's for sure. And I'm telling you, I really like these things. They're just built so solid and tough. You could

**Dave Jones:** throw them in the toolbox, and oh, they're built like the proverbial brick dunny. Love it. And by the way, it doesn't actually say where they're made, but I assume that they're made in the Everett plant in Washington, but yeah, I don't

**Dave Jones:** know. They don't actually say made in China, so with Fluke, you've got to assume that it's USA, but I'd be stamping made in the United States of America. Uncle Sam approved. Next up, the CNX i3000 wireless iFlex. That was

**Dave Jones:** that funny-looking flex current uh clamp. Well, it's not a clamp, it's a flexible interface. And as you can see, they've got like a custom interface. It looks like they've got three connections there, but it's actually not. This one

**Dave Jones:** over here is just a dummy one, and they actually use both of these. So, I'm not sure why they've decided to do that. You can see that this Maybe you can't see down there, but that one's just a dummy.

**Dave Jones:** Um the two contacts are actually there and there, so not sure why they decided on that. Crazy. Well, once again, this will be very quick, folks. Not much to write about at all. Um they've done It looks like they've used Have they used like

**Dave Jones:** the same case down here? They may have with the same cutout there, but the two two connections are over this side now. So, they may have used them same molding there. Interestingly, there's a cap missing there, which And they've actually

**Dave Jones:** put paste on the pads, which you know, you don't normally find. There's another unpopulated one up there. It's got some paste on there, but yeah, nothing much happening. They've used the two uh terminal screw interface here. Looks like there's a

**Dave Jones:** Looks like there's a polyfuse there, and well, not much else. Is that an amp? We'll have to take a look at that. That chip there looks like an Analog Devices uh OP 1966, but I can't find the info on that anywhere.

**Dave Jones:** And they've got the poly switch there for the battery contacts, and there's the uh ATmega uh SPI flash again. And we've got our ZigBee module and a bunch of other analogy type stuff. Um yeah, not that exciting. Sorry, I'm not going to

**Dave Jones:** go into detail. It's like yeah, whatever. I don't even think I'll take the rest of the board out because, well, we know what's on the back of it. But that is basically the uh input circuitry pretty much there for that uh clamp

**Dave Jones:** system Well, the um for that uh flexi sort of current clamp system up to 4,000 amps. Oh, excitement plus here, folks. There it is, the i3000. Woohoo! Last but not least, we have the CNX T3000 wireless K-type thermometer. There you

**Dave Jones:** go, standard uh K-type thermocouple input, 30 volts max. Not terribly exciting. Crack it open. Expect to see uh exactly the same stuff. Now, this one's a bit more interesting. We've got a bit more uh input circuitry down in

**Dave Jones:** here. Up the top, exactly the same, you know, we've got It's the same molding, same casing, everything works same as before for the other modules. But uh down here, we have a uh thick film hybrid there. There it is. There's the

**Dave Jones:** uh No, there's a um Linear Technology part there we'll take a look at. Another uh QFN package there. And down in there looks interesting. It's all like gunked up. But that's the uh input connector. Let's take a look. And there's an LT6010

**Dave Jones:** there, a precision op amp designed for uh surprise, surprise, uh thermocouples. You know, low input uh bias current, you know, 100 uh picoamps or something like that. So, pretty schmicko little part. And there's that LTFLK2 Fluke custom chipset again.

**Dave Jones:** Pops up all over the place. So, apart from that, we've got uh There's the uh two input uh pads down in there, you can see they're huge and chunky. Check those out. Huh, enormous. They've got two inductors uh leading from them. You

**Dave Jones:** know, totally differential. Look, you can see the uh two inductors there. You can see the uh cap across both of them. Two more inductors. So, we've got input filter in there and that all goes into uh some uh precision resistors there and

**Dave Jones:** that's measured by the uh LT Fluke. And so, I'm not sure what the uh precision op-amp all the way up there is doing. If it's look like it's not like near the input to the uh uh thermocouple down here, but this

**Dave Jones:** could be just a switching uh chipset or something like that. Could just be switching it through and then it uh goes into the 6010 up there. Who knows? Um not sure. We've got a couple of uh uh five- and six-pin SO-23s and uh

**Dave Jones:** that's all she wrote. So, let's see if we can get that board out at least. Now, you can see the um input jacks down in there. They're actually a spring terminal. And those spring contact inputs, of course, uh contact these two large studs

**Dave Jones:** here, which are actually press-fitted into the board down uh press-fitted and uh soldered into the board down here like that. And you can see the massive uh traces up there. I don't You know, they're not doing it for the uh current.

**Dave Jones:** They're doing it for uh thermal reasons, I can only assume. And there you go. RT1, there's a thermistor in there, which measures the temperature directly at those two input contacts. So, they're obviously trying to compensate for um any effects due to the uh metal, any

**Dave Jones:** thermal effects due to the metal contacts right down at the input. They've gone to a lot of trouble to do that. Fantastic. Because, of course, what is a thermocouple? It's just a contact with two dissimilar metals. And there's the thermocouple probe right

**Dave Jones:** there. And really, that's effectively a similar thing which is going to happen or could potentially happen on your input jacks here if you have dissimilar metals. It can generate a voltage and that changes with temperature. So, you've got

**Dave Jones:** to be very careful. So, they've added the extra thermistor in there. So, I'm not actually sure what metal they've actually used in here, but they've determined that it's going to have enough effect that they have to measure the temperature at that point and

**Dave Jones:** potentially compensate for it. So, wow, that is that's really quite interesting. I like that. And I was going to say maybe that's what that 6010 is doing there. It's actually reading that individual channel there, but yeah, I can't really seem to see where it goes.

**Dave Jones:** It seems to go into this resistor network down in here. So, that's just a compensation network or something. I'm not sure if they actually separately measure that into the analog to digital converter and then do something in software with that or

**Dave Jones:** whether or not that's just it. It looks like it just may actually be, you know, compensating in an analog fashion, but yeah, not entirely sure. Well, this module is, you know, rated at like half a degree absolute accuracy

**Dave Jones:** and a 0.1 degree resolution Celsius of course and 0.01% full scale temperature coefficient per degree C. So, you know, it's a reasonably high spec temperature module. That's for sure. And we'll switch that one on for fun. T3000. Sounds like Terminator. 24.9° here in

**Dave Jones:** the lab. There it is. Not terribly exciting. So, there you have it. That's the Fluke CNX 3000 wireless multimeter series. Very, very funky. Um yeah. Haven't used them yet. So, I can't give you a review on these things yet, but uh yeah. Very

**Dave Jones:** interesting, very well-built. Uh as you'd expect from Fluke. Absolutely first class and uh worth every cent. I'm sure. Hope you enjoyed it. If you want to discuss it, jump on over to the EEVblog forum. Catch you next time.

**Dave Jones:** Oh. Damn, that hurts. Oh. Ah. Hi. Welcome to Teardown Tuesday. Oh, I didn't know I got the bloody mic. Oh.
