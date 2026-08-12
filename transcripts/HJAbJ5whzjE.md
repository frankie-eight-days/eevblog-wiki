---
video_id: HJAbJ5whzjE
title: EEVblog 1423 - Flaming Magic Repair Smoke!
url: https://www.youtube.com/watch?v=HJAbJ5whzjE
source: youtube-asr
---

**Dave Jones:** Hi, it's repair time. If you follow me on EV blog two, and you should, you would have noticed that I had a problem with one of my oyster lights in my kitchen. And well, it was sending alien signals or something. It looked like it

**Dave Jones:** looks like an alien spaceship and it was flashing a weird code. So anyway, I ripped it out. I've brought it into the lab here and I've hooked it up and that's what it's doing. Let me turn the lights off. So I've just got it hooked

**Dave Jones:** up to a LED string which I got out of ripped out of an old LCD dumpster TV. It's coming in very handy. I've used it for quite a few videos actually. The LEDs have got like 5-volts drop per LED. They're actually quite

**Dave Jones:** high and yeah, I do like they're in string configuration. I use them for all sorts of things. I've got two strings of those. Yeah, does anyone know their Morse code? What's that flashing? Yeah, it's hiccuping. So anyway, that is obviously hiccuping as

**Dave Jones:** they call it. That's one of the names for the fault. I don't know if you call it something else, but yeah, in the industry it's often called hiccuping and the mains power supply is hiccuping. Hiccup. It just can't start up. It's trying to

**Dave Jones:** start up the mains side of it, but the main switch inside, but it just can't do it. So it keeps restarting retrying retrying retrying and no, it just comes a gutter every time. So anyway, let's take this thing apart and see if we can

**Dave Jones:** find the culprit. All right, we're at the Tektronix microscope, but I got something a bit new for you today. I've now integrated my NI National Instruments virtual bench scope. It's just sitting right down here next to me and I've got my probes. I can have my

**Dave Jones:** oscilloscope probes. I can have power supply, function generator, logic analyzer, digital IO, everything integrated into my video capture system, which not only I can record with, but I can also stream as well. So, you'll see in my straight-ahead camera, I've also got my

**Dave Jones:** Tagarno microscope. Here it is, right under me. And there will be a B cam, but it's not hooked up at the moment. And also, there's my National Instruments screen. But one of the cool things I can do now is I've set it up so that I can

**Dave Jones:** now overlay Ta-da! This I can overlay the multimeter here. So, here's Here's the multimeter. Winner. And all the power supplies as well. And there's some digital IO in there as well. And I can stream that. And yeah, that's really

**Dave Jones:** cool, huh? So, anyway, let's get to it. Let's have a look at Sorry. Let's have a look at this. Okay, so let's have a look at the driver here. It's a Lucci thing. Model number for those playing along at home, it's a

**Dave Jones:** it's a dimmable jobbie. And it's a a 2 W LED that's individual LED. It's actually up up to 20 or 22 W output. So, it's actually rated for up to 80°. But yeah, anyway, let's have a look at what's failed here. Here's the

**Dave Jones:** output section. Now, I wouldn't expect There's no bulges in those caps, of course. The first thing you look for is bulges in the caps. But oh, I forgot to tell you that this actually comes with a heat sink over here. And it's just

**Dave Jones:** screwed in there. And I've taken that out because we want to see some stuff under there. There's a couple of extra caps. And anytime you see caps near or under heat sinks like this, yeah, you want to be suspicious of those puppies.

**Dave Jones:** So, anyway, I've taken that off. So, yeah, it's just a plastic package. So, that's just like they didn't even bother with the heat sink compound. So, they just bit how you doing? They just slapped it on there. But you know, better than

**Dave Jones:** nothing, I guess. These are a Shai caps on the output. Now, it's not going to be the output A because those caps looking good Nick and B there's multiple ones in parallel. So, like you know, I wouldn't be concerned

**Dave Jones:** with that and that's not going to cause uh the power supply to hiccup. Now, is this a secondary regulator? Yes, it is. This is a secondary regulator, okay? Cuz here's the primary secondary split. So, this is all the secondary side. This is

**Dave Jones:** the mains input over here. Like this and so these are my initial thoughts. I I'm pretty sure it's not going to be this secondary side. I mean, you can go in there obviously you do a visual on the

**Dave Jones:** uh caps but they these have got the vents on the top. I can't see any bulges whatsoever. They'd be in parallel if you actually follow the money on there. Yeah, parallel parallel parallel um and another one there. Is it? Don't know if

**Dave Jones:** there's four in parallel or what not. No, there's another one that's not in parallel. So, we've got three in parallel. So, when you got three caps in parallel like that, it like it's not going to be the output caps and really

**Dave Jones:** the output driver side of things um you're generally not going to see like a uh hiccup hiccup hiccup hiccup um as we call it. That's usually a primary side thing where this converter can't start up. So, yeah, I would not be looking at

**Dave Jones:** the secondary side. I'd be looking at the primary side. Now, they've actually rubbed number off this chip. So, we can't see what this is. Maybe I can get a knife on there and try and scrape it off but I think that they've actually

**Dave Jones:** scraped the number off that chip. Anyway, you want to give a visual on here and uh one of the first things I notice is that there's discoloration around there. That resistor in there. Is that my imagination or is that a bit

**Dave Jones:** discolored, too? Uh that looks a bit how you doing, doesn't it? So, we'll get in there and measure that and you can see that on the bottom as well. Look, you can see the fiberglass and like you start seeing like the the

**Dave Jones:** the weave in the fiberglass pattern, right? You You don't see that anywhere else. That means this has been heated up to buggery, and uh yeah, it's just the fiberglass is not uh you know, your high-temperature, high-quality stuff. So, it's just start to discolor and and

**Dave Jones:** yeah, it's it's not looking good. Also, you can see the same thing effect happening over here, as well. So, that's under um what's that under? That's these big resistors over here. These are just um input resistors, are they? Yep.

**Dave Jones:** So, yeah, they're just input um limiting surge resistors, whatever. Anyway, um yeah, there's no major caps on the uh input, even though this is a full-wave bridge rectifier. Um they just don't need a massive amount of uh capacitance on the input. Now, of

**Dave Jones:** course, as I said, these caps are under and near the heatsinks here. So, you would suspect these puppies, right? 50 V, and they would be to do with the startup as well. I don't know what that What's that in there? Is that a ST25C?

**Dave Jones:** Is that just an external uh switching transistor? I have to look that one up. ST25C, it's a BJT. It's an NPN BJT. Um yeah, it's just a jelly looks like it's just a jelly bean BJT. No worries. And we've

**Dave Jones:** got a bunch of diodes in here, as well. Uh you could go in and you could uh measure those as a matter of course, but I'm I'm really quite concerned that that resistor there is heated up a lot, and

**Dave Jones:** it's right next to the caps as well, and little alone the heat from the heatsink, but that that that resistor um that's obviously gotten hot because it's just yeah. Um so, anyway, let's get turn on our multimeter, shall we? And let's have

**Dave Jones:** a probe in there. What what value is that? Brown black? Something or brown black burnt. Brown black burnt is the is the value of that resistor. Now, when resistors get hot like this, obviously they're not going to be in the

**Dave Jones:** kiloohms or the hundreds of kiloohms cuz Ohm's law, you'd need like thousands of volts before you do anything. Um actually heat them up. So, this is going to be a low value uh low value resistor. And was that a

**Dave Jones:** gold band on there? Like you know, like a silver or something like this one over here. Anyway, so that's supposed to be a low value. So, let's measure that, shall we? 287 K. K, no. No. That's nope. Um Houston, we've had a problem.

**Dave Jones:** Um the resistor is that that is goneski. That is goneski. I don't need to measure anything else. I mean, I could. I mean, I could whack I could go diode mode and I could go start checking my diodes and stuff, but you

**Dave Jones:** want to fix anything you come across 0.56. No, 0.67. I think we're good on the diodes. Just check diodes cuz they're easy, you know, and you can generally check them in circuit. 0.7, you know. No. No No workers. So, yeah, I can't see

**Dave Jones:** visually anything else. Really, I mean, these suckers they like it it's discolored. I mean, it's it's discolored and it's 270 K. No, that doesn't add up. That does not add up. So, we have come across a there and we

**Dave Jones:** could have found a culprit. Is it that easy? Is it one resistor? Let's hope so. Makes for a boring video, but anyway.

**Dave Jones:** Oh, wow. Wow, that that other joint I I haven't even desoldered that and that other joint's gonsky. That's the other thing that I should have looked for on my visual was joints and let's actually go down here. Oh, hang on. There there's a pin

**Dave Jones:** sticking out. No, that can't that can't be it. And oh, yeah, yeah, that one look yeah, yeah, yeah, there you go. It's is that just a that's just a trans that's just a transformer leg. Okay, that's right. Yeah, there you go. This sucker

**Dave Jones:** has heated up so much that it's just delaminated. The copper's just delaminated from that. Wow, yeah, that's gonsky. Need to turn it the right angle there. Geez, there we go. Got that characteristic burny smell, that earny burny smell.

**Dave Jones:** And yeah, that that is one sick Oh, look at that. That's cracked the buggery. Wow. Wow, that sucker's had a harsh life. Look at that. So, that's Well, no, I thought that was brown black something. It's red. What is it?

**Dave Jones:** Red brown? Something. I don't know. That's just that's terrible, Muriel. Wow. Yeah, that is completely gone. No wonder. Wonder if we can just like is it just going to fall apart? I wonder if we just grab that with two pliers, is

**Dave Jones:** that going to come apart? I don't know. Still strong as a melee ball. But uh yep, it's it is completely cracked. It's gonsky. And that of course is probably open. The 270k was measuring in circuit and yep, yep, it's just it's it's

**Dave Jones:** gonsky. So, it could just be the resistor that just heated up so much that it eventually went open and I can guarantee it'll do exactly the same thing now if we power this up because is resistor's missing. It was open before.

**Dave Jones:** It's still open. So, yeah, maybe that's it. Maybe did they have the wrong resistor value? So, it's got to be like a piss-poor design because like you wouldn't design it so that resistor heated up so much that it failed like

**Dave Jones:** that. And it's not like because and like an ambient thing because it's inside the oyster light. I mean, that doesn't help, right? The fact that it's it's got no air flow in those sealed oyster lights upside down on the roof, but

**Dave Jones:** Oh, wow, you know? That's just That That's a harsh life. It's not good. Don't know. It could have been brown. It could have been black. That's just faded. It could be gold that's just faded. I'm That third band

**Dave Jones:** it does matter. It matters a lot cuz that's the That's That's the multiplier. So, I'd be tempted to go with gold, maybe. So, we're talking like 1 ohm. Silver would be Yeah, like It does look red on the screen here, but

**Dave Jones:** when I look at it with my eyes under my improper color lights here, it It looks brown. So, I think it's brown black. Um and it's just Yeah, it I know it does look red on camera, but when I look at it straight, it's

**Dave Jones:** actually it's it's more brown. So, Mhm. Anyway, that's what I'd expect. Yeah, I'd expect like in the order of like ohms-keys. So, where is it in circuit here? There it is there. That's one of the transformer taps. These are the transformer taps along

**Dave Jones:** here. I don't really want to reverse engineer this. So, No, that's a large value resistor in there. Yeah, so I'd say that's just a current shunt resistor. Is it? Don't know. I'd have to look up a typical primary side

**Dave Jones:** switcher for that cuz this obviously it's not doing the regulation on the primary side. It's doing the regulation on the secondary side here. That's the only reason why you'd have the SO8 controller there, which I think they've rubbed the numbers off that puppy as

**Dave Jones:** well, I think. The conformal coating doesn't help cuz, you know, you like you can still see the diode marking on the diode bridge over here. It Yeah, I tried to scrape that away and it says that there's there's nothing

**Dave Jones:** under there. But yeah, I don't know. And just throw in a couple ohms or something and see if it gets it back on track. So, I'll actually leave this one sticking up a bit. Why not? That's That's not going

**Dave Jones:** to touch the heat sink. Just leave it Leave it up there like that rather than have it right down on the board. That gives it some extra heat sinking due to the legs. Oops, that pad's lifted. Didn't go through. That's a bit cleaner.

**Dave Jones:** Hopefully, she'll go through now. That's the problem with lifted pads. Really rather annoying to try and get these back through. I think I got it. Yep, sweet. So, I'll just leave that flapping around in the breeze up there

**Dave Jones:** and Bob's your uncle. So, here's our main primary switching transistor over here. You can see that goes over to the coil there and that's our resistor in there now. So, I'm you know, it seems like that is not in the way of

**Dave Jones:** It goes under there. It goes over to here, which is then that small little TO-92 transistor we saw before. So, I'm not seeing how that's part of the main line. So, I'm not seeing how that resistor is in series with the main

**Dave Jones:** switching transistor there. So, that shouldn't be a problem even if we make that too low. I don't know. But yeah, if it was if it was in series, um, then obviously the value is going to matter, but, um, yeah, cuz it's in there. I

**Dave Jones:** don't know, there's this extra switching in here. That's like it's it's probably doing some like power factor correction as well, something like that. So, it's obviously doing something different. So, it may be as I said like it could be some other sense resistor or

**Dave Jones:** something like that, but it obviously heats up. So, it's important to get that value right. It's going to be critical and well, I don't know, cross your fingers and hope, um, I've got the value right. But anyway, um, yeah, let's just

**Dave Jones:** power it up, whatever. All right, let's give it a belt, see if we get anything.

**Dave Jones:** Woah! Magic smoke released. Holy crap. I guess that's the wrong value. Woah! What what what what Yep, I would say, uh, that wasn't, uh, gold that band. That's what happens when you underestimate the value. The actual resistor's fine,

**Dave Jones:** uh, but look at the input It was obviously drawing like probably an order of magnitude more current and those input resistors from the mains. Nothing else seems fried, um, which is really interesting, but those Wow! Look at those input resistors

**Dave Jones:** there. They are just uh, they're burnt. They are horrid. That is unbelievable. Um, yeah, I've completely come a gutser. I am I don't think I'm going to bother to fix this now. I'll just probably upload this as a hilarious what not to do. Um,

**Dave Jones:** yeah, I got a bad my spidey sense gave me a bad feeling just before I was about to switch it on. I thought, "Oh, no, I'm going to come a guts or I think I've got I should have gone up in value rather

**Dave Jones:** than down. Um, yeah, that was dumb, wasn't it? Actually, I presume that's an input fuse there. That just it goes to show how poorly that's rated. That input I'm going to cut that off because like that that should have popped before all of those

**Dave Jones:** just absolutely cooked. Um, yeah, I think they've rated that wrong. Oh, no, so much for that. I thought that that'd be a little axial fuse in there, but it's not. It's just a resistor. Anyway, oh boy, those puppies cooked. Sorry if you got

**Dave Jones:** that fan noise in the background. That's my filter going berserk here trying to get rid of the wretched smell from this sucker. Uh, yeah, well, that's embarrassing. That's double facepalm worthy. Yeah, please leave it in the comments down below. I'm an absolute

**Dave Jones:** dill, but I thought I had the right value, but then I like I knew that. I should have actually like at least attempted to reverse engineer this, see what was going on there, see exactly where the resistor was. The lower value

**Dave Jones:** was always going to be a concern, but I I thought it was gold in there, but uh, it's yeah, that multiplier band is going to come a guts or obviously. Yeah, I was off by at least an order of magnitude, but it

**Dave Jones:** seemed a reasonable at the time cuz if you have a look here, here's the resistor here, and it goes under there, and it goes to this small TO-92 um, MPN transistor that we looked at. So, it's not like, you know, that's

**Dave Jones:** going to be carrying amps or anything, so it's not the like emitter resistor in the main switching transistor which you'll be in series with the uh transformer over here. So, it's like it's not that. It's somewhere else in

**Dave Jones:** here doing something, but obviously, given the uh size of that uh resistor and the fact that it's heating up, yeah, it was obviously um doing something more important and dissipating a fair bit of power. So, with hindsight, yeah, that was just a

**Dave Jones:** dumb 1.8 ohms was a dumb choice. Um yeah, just didn't put the thinking cap on enough. No. All right, I've decided to do a basic reverse engineering here. It's not complete, so please excuse the crudity of the model. Didn't have time to build

**Dave Jones:** it to scale or to paint it. So, I'm going to work out where I goofed up. Uh my first goof was uh not remembering that this is a dimmable uh LED controller, which means that it has to start up at low voltages, which

**Dave Jones:** means it's going to need some sort of low voltage uh start up, you know, just in case the dimmer when you turn it on is like set to like a low voltage, like, you know, 50 volts, you know, something

**Dave Jones:** like that or whatever it is. Anyway, um yeah, we've got 240 in, you know, there's some filtering and other stuff over here. And including the resistors that burnt the hell out. And then we've got a bridge diode bridge rectifier. And

**Dave Jones:** then we've just got a main small uh filter cap, which is uh here. And then um here is our mystery resistor right here. And it looks like yeah, we've got a Zener basic Zener um circuit here with a emitter follower transistor here.

**Dave Jones:** That's a little uh TO-92 jobby in there. And um and that just powers the eight-pin chip. I still don't know what that uh chip is. Look up uh dimmable flyback uh LED controller or something like that. And there's 10 million of

**Dave Jones:** them. But it's more likely to be one of like the lesser-known like Asian variants or something like that. Anyway, um yeah, and then of course, the DC, the main couple hundred volts DC, powers the transformer over here, just like I suspected with of course the

**Dave Jones:** main switching MOSFET here. And then the other one watt resistor down in here, which I knew was the series resistor for that. And obviously that like then they're tapping that off somewhere else. I didn't bother, you know, going into

**Dave Jones:** details around the controller chip. But then you've got a tap coming off the primary of the transformer here, which goes via a diode, and that goes into buy basically bypassing the 180k. And the other resistor up here, the 180k

**Dave Jones:** one watt jobby, that's the other one watt resistor up here, which wasn't cooked at all. So, you wouldn't expect that 180k to be dissipating much at all, because it's basically in parallel with the coil over here, and which of course can be low impedance

**Dave Jones:** to then drive directly into our main Zener dropper down here. Obviously, this is going to be a Zener. I don't know the voltage, but I did, there it is, tiny little jobby down there. It's a sad looking thing, but it has had the snot

**Dave Jones:** blown out of it. It's measuring like three ohms, so yeah, that's no good at all. So, that probably that's not one of the original faults. That would have happened in my goof up. And we can see how it's blown here. This

**Dave Jones:** I totally goofed up. I you know, I thought it was some other, you know, current sense resistor or something dumb like that. I just, you know, I didn't have my brain engaged, and of course it's a if you did some basic reverse

**Dave Jones:** engineering, you would have seen that this was a Zener dropper, basically. So, this needs to be in the order of tens of Ks. So, that resistor value probably is either 10k or 20k. So, that third band, which I

**Dave Jones:** thought was gold, was actually I think it was orange. So, uh yeah. So, I think this was originally a 20K resistor. And here I am going putting in a 1.8 ohm. So, I was only out by four orders of

**Dave Jones:** magnitude. D'oh! So, we can see now how it snotted itself. Um yeah, we've got our high voltage DC here basically going straight through the coil like this and then straight across through the diode. I'm surprised like the diode uh survived and

**Dave Jones:** a straight through basically a short circuit, which then um snotted the uh Zener down here. So, it it turned it failed uh short circuit. So, if either of those failed open, then um yeah, we wouldn't have had the magic smoke

**Dave Jones:** escape. It just would have went pop. And uh pop goes the weasel. And yeah, it it would have been fine. We wouldn't have burnt the um in- input protection resistors over here. They wouldn't have turned completely black and charred like

**Dave Jones:** that. So, yeah, we just um it looks like I haven't measured this other diode. That could be shorted as well. Um likely. So, yeah, it just boom went straight down like that. So, this should have been, you know, 10 or 20K,

**Dave Jones:** something like that. And yeah, complete goofarama. I chose poorly. You chose poorly. And what that Zener voltage there would have uh been, uh you know, it's like in the order of maybe 20s, you know, the tens of volts, 20 volt. I mean, there's,

**Dave Jones:** you know, a 50-V uh rated cap. Both of these caps are 50-V uh rated here. And I won't go into details about, you know, how all this works. It doesn't really matter. If anyone does know, um they can, you know, guess based on the basic

**Dave Jones:** at least some of the pinout I've got here, um exactly what chip that is, please leave it in the uh comments down below. And if you do want me to do a complete reverse engineering, Well, if we got that chip, we probably shouldn't

**Dave Jones:** have to. They probably got an example circuit in there. It's probably almost identical to the example application circuit. They usually are. Very few differences usually. Anyway, if you want me to do a full reverse engineering, then you know, leave it in

**Dave Jones:** the comments down below. But I like we just needed to know where I goofed. And that's what it is. It looks like it was a Zener dropper circuit doll. So yeah, that was embarrassing, wasn't it? But anyway, I hope you found that valuable.

**Dave Jones:** My goof is your gain, I guess in terms of yeah, just you know, like a couple of more minutes. If I didn't rush this thing, a couple of more minutes just figuring out exactly what that resistor was doing would have prevented this.

**Dave Jones:** Obviously, if I knew it was a Zener dropper like this, there's no way I would have made that like, you know, ohms. I would have made it tens of ohms, something like that. And I would have probably guessed you know, it's not

**Dave Jones:** going to be like in the hundreds of K region. It's going to be in the tens of K region. If you do your Zener dropper calculation and stuff like that assuming like, you know, a milliamp or two drawing here and the minimum Zener

**Dave Jones:** current. You can work out, you know, a basic you know, ballpark resistor value. And it's going to be in the tens of K region, something like that. So yeah, I definitely wouldn't have made that mistake if I simply

**Dave Jones:** went spent a little bit more time doing the reverse engineering. So that let that be a lesson to you. Anyway, I hope you found that valuable. If you did, please give it a big thumbs up. As always, discuss down below.

**Dave Jones:** Catch you next time. Mhm.
