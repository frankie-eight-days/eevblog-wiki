---
video_id: -MKUsLi90O4
title: EEVblog #710 - Intercom System Repair
url: https://www.youtube.com/watch?v=-MKUsLi90O4
source: youtube-asr
---

**Dave Jones:** Hi, it's potential repair time. I say potential because I have no idea if I'm going to be able to fix this thing or not. What is it? It's one of these apartment building complex security entry systems, whatever you want to call them. And this

**Dave Jones:** one's actually from the EV blog corporate towers here. And it failed. And the reason I ended up with it is because the company that maintains our gear in the building here, this one broke down. This is the entry to the underground car

**Dave Jones:** park, the roller door that goes in to our building here. And it broke down and the company that usually services this sort of stuff said, "Sorry, they don't make this anymore and we can't buy it anywhere in the world

**Dave Jones:** and we can't fix it, blah blah blah." And well, I'm smelling a bit of there. I I suspect A, you can probably still get it somewhere or B, you can get like an upgrade or replacement unit. And it's an

**Dave Jones:** Aiphone brand. It doesn't This particular one doesn't have the model number on it, but this is the going to have a look under here. There it is. This is the GF model unit. What it does, of course, if

**Dave Jones:** you I'm sure you've seen these as you enter buildings, you drive up in your car or you walk to the entry and then you type in the number that you actually want, the apartment or office number and the phone rings

**Dave Jones:** here. I've got one on my wall here and then you can talk through here, speaker, microphone. And they've got a little LCD here to display various stuff. And then the person, if they want to let you in, they can push a button on the phone

**Dave Jones:** which then activates the door and lets you in. So, this is called the entrance station. And we take a look here, there's all the buttons. They got nice little rubber tips on them. Don't mind that at all. That looks like it's

**Dave Jones:** going to last a a fairly long time there. So, this is the GF. It comes in different physical configurations. You can get these like it depends on like the type of building, but hence why tada, we've got three

**Dave Jones:** separate modules because you can actually get different frames and then wire them in different physical configurations. So, we've got the one module here, which I believe is the one that's failed because well, there's nothing else in here. This is just a

**Dave Jones:** keypad with some LEDs to then light up. If you're wondering what that was, it's just a little diffuser there. And at night it just lights up the keypad so you can see the numbers you type in. So, that's got all the control electronics

**Dave Jones:** in it. And this I don't expect there to be much in there. That's just a speaker microphone interface. So, the fault is that um it it's getting power to it. I haven't actually measured it, but you can see that it's got a classic like

**Dave Jones:** when your LCD you haven't initialized the LCD, it comes up with I'll be able to power it up soon hopefully and you'll see that it comes up with just a blank line of characters. It's a two standard two line by 16 character

**Dave Jones:** LCD. So, it's got to be something to do with this module here and just wire them together in various configurations. And you can have up to I think this unit can have up to like a whole bunch of these like dozens of

**Dave Jones:** these and it can have a up to this system can have a have up to 250 phones hooked up. 50 phones per bus. And this hooks up to a bus a power supply and bus expansion unit and they're very

**Dave Jones:** simple. I mean, power is in here and then it's got a couple of other pairs over here. And it can you can add video to the system as well, but this is a voice only system. So, as I said, this

**Dave Jones:** is the GF model, and they claim you can't get it anymore. Well, it's got a date code of 2004 on it. There you go. That's not too old at all, although the system likely predates that. And sure enough, I think

**Dave Jones:** it is a discontinued model, but then the new one is the GT model. Looks almost practically identical, except it's got a vacuum fluorescent display instead of an LCD, and I'll be very Oh, we've got a real bug there, folks.

**Dave Jones:** There's your There's your problem right there. It's got a bug. Yeah, that looks like one crusty old bug.

**Dave Jones:** Anyway, I think what I was going to say there is that the companies who make these types of systems, they like, you know, alarm security systems like we looked at before with Ness and stuff like that. A huge thing with these companies is

**Dave Jones:** backward compatibility to ensure that new models you know, at least protocol compatible cuz there's bugger all interface with these, right? It's just like a two-wire interface, and you'd be mad if you didn't make it the new one backward

**Dave Jones:** compatible with your old ones cuz people these sorts of things fail. You know, these buildings last for like, you know, 30 years or something before they upgrade these things. So, like in our case here, just one particular unit fails, and of course,

**Dave Jones:** the people who use that door to the building are complaining to the strata committee that, you know, you know, I why do I pay my strata fees? You know, you've got to fix this. And these secure and the installation companies saying,

**Dave Jones:** "Oh, no, we can't. You're going to need a whole new system, blah, blah, blah." And that would it'd be hideously expensive to buy a whole new system. That's why I'd be very surprised if the new GT series would not be compatible with this

**Dave Jones:** GS. So, I think they're spinning a bit of BS there just to get themselves a nice juicy big contract to install a whole new system. Anyway, let's have a squeeze up in here. And how does that Oh, yeah. Oh, hello. Yep.

**Dave Jones:** There we go. Ta-da! We're in like Flynn. That's pretty much all I expected. Not much at all, just a processor and uh couple of miscellaneous stuff and Bob's your uncle. Actually, that's really interesting. I'll try and get this on an angle. That

**Dave Jones:** looks like that has got a conformal coating on the board. Um well, actually not hugely surprising because uh this is going to be used in an outdoors environment. Not surprising that they might whack a conformal coating on that

**Dave Jones:** board just to uh uh keep out the moisture over the long term. Yep, that makes sense. It's quite thin. You can see the part number on there M3620 ECFP, I think it is. No idea. M Motorola perhaps, but curiously, here we go. Here

**Dave Jones:** is the GFNS. So, that looks like it's laser etched V 200X. So, that could be the version number. So, the firmware could have been uh pre-programmed into here and uh laser etched. So, it could be a ROM, a mask ROM device uh

**Dave Jones:** processor or something like that. And please excuse, this is not easy to get when they've conformally coated stuff, but bingo, Microchip 24LC 128. There's our E squared PROM for storing all of the information cuz this um thing when it like uh powers up, it

**Dave Jones:** has like you can program all of uh like the apartment names and the things like that into it and you can actually program those directly through the front panel, I think, or through um some optional uh PC software which you

**Dave Jones:** hook up to this thing. So, no surprises for finding E2 prom in there cuz this is probably like a really old-school uh processor here which uh doesn't have building E2 prom. And of course, being a essentially a multi-drop system, you

**Dave Jones:** know, a professional multi-drop system, you probably would have expected like an RS485 or something like that, but no, look at this, DS14C232. We got ourselves an RS232 driver. Although, that might just be for the um uh the PC um interface, perhaps. I don't

**Dave Jones:** know. I think we have to take the board out. There might be some more on the bottom, but yeah, I mean, they're the only three chips on the top side here. And by the way, the way I ended up with

**Dave Jones:** this is that the uh strata manager uh was confronted with the ultimatum from the um maintenance company saying, "Yeah, you know, we can't uh find any replacement for this. Uh no, we've scoured the world, can't do it, and well, you're

**Dave Jones:** probably up for a new system." So, of course, he knew I was into this sort of stuff and go and went, "Well, you fix electronics, don't you?" Goodness. Anyway, not much on the bottom here. I do see a fuse, of course, when

**Dave Jones:** you're servicing this sort of stuff, you got to check a surface mount fuse like that. I wish it would be that easy, but as I said, I do see the LCD light up um as in the um as in power getting to it

**Dave Jones:** because I can see a row of characters. I'll power it up in a second. Um it's powered from 24 V DC, uh DC, but there's yeah, there's bugger all uh on the bottom here. Actually, yes, I think that RS232

**Dave Jones:** chip um is handling the uh PC interface cuz this is like a vertical uh TRS um jack here, which then the traces wiggle their way down there. Sorry, excuse the crudity of my finger. Basically down to here near the RS232

**Dave Jones:** chip and without buzzing that out, I'd say, "Yep, that's what she's doing." So, that's the PC interface when you hook the PC interface up, it just hooks up to your RS232 port. So, where the drivers are for the uh for the line,

**Dave Jones:** um I don't know. I mean, we've got ourselves something there, big D pack there, whether or not that's a transistor or a uh voltage reg, I'm not sure. Have to have a closer look. Actually, without out knowing more

**Dave Jones:** details of the system, I am speculating here, but I think it's actually sending data over the audio line. I think that's what's happening here. So, this processor will maybe encode some uh audio um you know, some sort of data over that audio pair.

**Dave Jones:** How it's actually doing that, I don't know cuz there's not a lot of miscellaneous circuitry there. I mean, you know, there's our resonator for the uh processor and that's about it unless that actually is like a custom uh you

**Dave Jones:** know, ASIC, which is which is doing all that. Um it may not just be an off-the-shelf processor. That's kind of like the only conclusion I can really come to at this point, I think. We've got ourselves some optocouplers there by the looks of it,

**Dave Jones:** but yeah, there's not much in there. So, let's power it up and see if we can replicate the fault. So, here we go, 24 volts. It says it draws uh 70 milliamps, so I'll set the current limit to 0.1 amp

**Dave Jones:** there and let's switch this puppy on and see what happens. So, I got the polarity correct. Yep. Well, anyway, it's already dead. I can't kill it much more. Well, yeah, you can always kill it more. You can always widerize it, I guess. Here we

**Dave Jones:** go. On. Ta-da! There it is. That's exactly what we were getting. So, as I said, the row of characters, and it's drawing about 60 milliamps. So, you know, that's about on. It's rated for 70. So, the current draw is there. We're getting

**Dave Jones:** good contrast on the LCD, but it's not booting up. Um presumably, unless the characters there normally like it scrolls when it's just idle. It scrolls the name of the installation company there. So, um yeah. Hmm. Anyway, that's a standard

**Dave Jones:** Hitachi chipset 16 by 2 display, and well, it's dead. But obviously, power's getting to it, but golden rule of troubleshooting, thou shalt test voltages. Now, the thing with probing conformally coated boards, of course, you've got to actually pierce

**Dave Jones:** through the conformal coating, because if you probe like you might be probing that down there and putting a little bit of pressure on it, but not actually piercing that conformal coating. And of course, that's an insulator. So, you

**Dave Jones:** have to really put a lot of force in there and have very sharp probes to actually probe through. Otherwise, you can think that you're getting nothing there. Your meter might be reading zero. You might think, "Okay, I'm making

**Dave Jones:** contact. I'm pushing like I normally do with the normal amount of pressure, and I'm getting nothing, but there is actually voltage there." So, anyway, let's uh uh sorry if I'm obscuring what I'm probing here. I'm going to probe this D pack

**Dave Jones:** down here. So, through zippity-do-da zippity-day. 24 volts. There we go. 24 volts on one pin and on the other. See, if I just probe that no like like light pressure, I don't get anything. But hey, bingo. There we go. 5.21. So,

**Dave Jones:** yeah, 5-volt rail, not surprising, and it's within specs. A little bit high, but within spec. So, that's all right. I'm assuming that's the rail. And of course, you can verify that. You just pick a easy to probe chip with a known

**Dave Jones:** rail pins. In this case, the E-squared prom, we know pins four and eight are going to be our power rails. As I said, light touch there, no voltage. You got to push down, pierce, bingo, there we go, 5.2. So, yeah, maybe oh, then maybe

**Dave Jones:** there's a little bit drop there, perhaps, but not at that sort of current. So, yeah, maybe that wasn't the uh rail. But, anyway, we do have a 5. Well, a basically a 5-V rail. So, that's just fine and dandy. And the fuse on

**Dave Jones:** here, yes, I have powered off. Yep, it's fine. And, you know, other basic things you might just basically probe things that are easy to probe. Um yeah, yeah, you can go you can argue, "Oh, yeah, let's just go through

**Dave Jones:** it systematically." But, you know, look, there's a big power resistor there. It's got 121 on it. So, that's a 120 ohms. The one at the end, of course, represents 1 0. And it's a big power resistor. Why is it a power resistor?

**Dave Jones:** Well, cuz it's dissipating a lot of power. What happens when things dissipate a lot of power? Well, they can possibly, if it's not designed right or there's an overload or stress or something, they can go open. So, why not

**Dave Jones:** check that? Because it's easy and it's trivial. And there we go, it's 120 ohms. Fine, rule that out. Now, I just had a look at the manual for this thing, which I'll link in down below, and it says actually to

**Dave Jones:** reset the thing, put the dip switch on for 2 seconds. Number one, dip switch number one. We have dip switch number one is already on. So, maybe well, there we go. Maybe no wonder like this is supposed to like reset all the

**Dave Jones:** firmware and everything in it. So, I'm like, "Well, that makes sense. Let's see what happens if we flip that switch back." That'll be embarrassing. All right. Nothing. Well, maybe the installers have tried to do that cuz they know that's

**Dave Jones:** what the dip switch does, perhaps. Well, let me re-power it. And uh that dip switch No. Okay. What? So much for that. Well, because that's a classic uh symptom of an LCD not being initialized like that, you got to assume

**Dave Jones:** that like either the processor is dead or not starting up or maybe the E2 prom is dead, which held the staff. But we've done the resetty thing and nothing's going. So, we're going to get the scope out and we're going to have a look at

**Dave Jones:** the uh to see if anything's oscillating and it sure as heck is. There we go. 4 meg, no worries whatsoever. Our processor is oscillating. So, and from memory, I'm fairly sure all these four status LEDs on the front

**Dave Jones:** aren't supposed to be on either. So, yep, our processor simply is not working. And because I can, I'll check the power supply and well, there's the 5 volts and well, we've got a bit of uh crustiness happening there, but uh

**Dave Jones:** nothing that would upset a digital system, I'm absolutely sure. So, yeah, I don't know. It's um yep, it's gone beyond the easy stage, I suspect. Now, because this is uh like a mast ROM uh device, essentially, um and

**Dave Jones:** our problem really is that uh you know, the thing is not booting and we're getting nothing on our LCD. It could be working for all I know, but the LCD could be uh dead. I've tried actually punching in the uh program uh code on

**Dave Jones:** the front here that's in the manual, but anyway, because our problem is that pesky LCD, let's try and probe some stuff to see if there's any Here we go. Any action happening on our screen. Let's got to be careful

**Dave Jones:** to make sure you're actually probing. No, I got a bit excited there as you do when you start seeing things like this. See, you will occasionally see something like that as you probing and unprobing and you think, "Aha, signal." But no,

**Dave Jones:** there's bloody well not. There's enough all there, so there's no data going to that LCD. And of course, next stop, I can probably when it powers on, see if there if I can capture anything. I'm on pin four there.

**Dave Jones:** Pins four, five, and six are the ones that uh matter for us. They're the control pins, and uh you whack your scope in single mode, and let's switch it on. At a slow sweep speed, and bingo, it switches on, but there's nothing. Um

**Dave Jones:** it's just uh slowly ramping up there. We get absolutely nothing. And uh let's try it again. Oh. Sorry. Let's try it again.

**Dave Jones:** No. No. See, we'd expect to see, you know, after the processor's booted up, we'd expect to see a burst of activity um going to the LCD, but we don't. So, that basically, um well, that's going to stay low, but yeah, like I think we're on the

**Dave Jones:** first data pin now. So, let's have a look there, even if it's in four four-bit mode. No. Zip. So, that's obviously just staying low. It's not doing anything. Aw. But no, that's just a uh it's a furphy. And uh no. So, we're getting

**Dave Jones:** no data um out of the processor going to the LCD. So, it's not like the LCD has failed. Uh we're just getting no data on those pins. That processor is not booting up. This is not looking good. Has our custom

**Dave Jones:** uh ASIC/processor failed? Well, power supply's okay, the clock's okay. I got no data on it. What's left? So, really that is not looking promising, I'm afraid, because well, yeah, you've gone through the basics. You measure the power, you measure the

**Dave Jones:** oscillator, you measure the signals going to the screen, which are our main well, our only symptom that we've got is that the thing doesn't uh boot, things like that by the activity on the LEDs, and we're just getting no response. And

**Dave Jones:** of course, the system that you know, when you plug it into the system, it's not like it's it's still works like the audio and everything uh still works, and but you just can't uh see anything on the screen. So, it's not that. It

**Dave Jones:** definitely is uh dead as a dodo. And um why? I mean, there's nothing else on there. So, it oscillates, we've got power And the conclusion I'm coming to at the moment is um we've got ourselves a a rooted chip

**Dave Jones:** there. But yeah, I mean, it oscillates, but hey, you know, it can be rooted and uh and still oscillate, cuz the oscillator's going to be, you know, its own little free-running oscillator in there. It just needs an inverter and uh

**Dave Jones:** it can start up. So, yeah. Mm. Without more data on this thing, I don't know. Um E2PROM lines, maybe. That's my last resort. So, there you go. I've checked the lines on the I2C bus on the E2PROM there, and like it just boots up

**Dave Jones:** as you'd expect because of the pull-ups, and and then does nothing. There's no activity um for, you know, many hundreds of milliseconds after that, taking out the time base. No, it just doesn't boot up. So, it's not even trying to access

**Dave Jones:** the E2PROM. So, you know, I thought, all right, yeah, maybe the E2PROM has failed, and and the firmware in there's not that great that it doesn't do diagnostics, you know? Um but a well-designed unit, of course, well-designed firmware, of course, would

**Dave Jones:** of course initialize the LCD first before doing anything and then put, you know, if it failed the e-squared prom, then, you know, just read out garbage or whatever, didn't get a checksum or whatever it was, um it couldn't read or write a test bit,

**Dave Jones:** then it would actually display a fault code or, you know, fault information on there, but we're not getting anything. It's not even booting up the and not even initializing the LCD. It's not initializing the e-squared prom. That processor is

**Dave Jones:** cactus. Well, stop the presses. We found out what this chip is and I obviously didn't look hard enough, but a couple of people on the forum and Patreon pointed this out. Thank you very much. It's a Mitsubishi now Renesas, of course, M16 C

**Dave Jones:** processor. So, it's one of the old-school ones, but you can still get the Renesas still sell variant of this thing and tada, we have the pinout. So, now we actually have a few options because if we didn't know what that chip

**Dave Jones:** is, then, well, that probably would have been the end of it cuz we don't know, you know, any of the pinouts. So, we can't just, you know, you could probably, if you're really desperate, spend many, many, many hours or days on it and maybe

**Dave Jones:** you might get somewhere, get lucky, but now that we have the data sheet, we have something to follow. So, I suspect what it comes down to now is it's going to be one of two faults. Either the chip is

**Dave Jones:** dead, it's died in some way, blown in some way, who knows, I don't know, or the or the I don't know, the ROM inside is is failed after It's not that old though, it's only 10 years old, so, you

**Dave Jones:** know, you wouldn't expect it to fail, or Uh, so the chip is either faulty or there's something holding it in a reset state cuz clearly this is not booting up at all. So, it's not doing anything. The oscillator is running. Of course, the

**Dave Jones:** oscillator will always run. It's a free-running oscillator on these things. In this case, with a resonator here. But, um perhaps the processor is being held in a reset state. That was That could be the only really two things I can think of

**Dave Jones:** that would stop this thing executing and booting up like this. So, let's probe the reset pin. And there it is there, pin 12. It's as usual, it's a not reset. So, it's an active low. So, um if that pin pin 12 is

**Dave Jones:** low after this applies power, then we can trace it and figure out what's going on. Aha, here's a trap for young players that just got me. So, I'll share my experience here. I just lifted up this resonator here. I just sort of you know,

**Dave Jones:** pushed it aside cuz it was covering exactly where the reset pin was supposed to be. So, to get access to that and see where the trace was going, I just sort of bent it up about 30° and I heard a

**Dave Jones:** crack. And oops, I forgot that this board was conformally coated. And well, if you do that, yeah, that's probably where the crack came from. But, it shouldn't have been enough to damage that. But, anyway, I then then probed

**Dave Jones:** the oscillator and I couldn't actually see anything. And I thought, "Oh, no. I've screwed the resonator on this thing and I don't know like I've cracked it internally or something dumb. Even though it was just you know, as you do

**Dave Jones:** all the time with through-hole parts, you sort of just move them aside that you know, you don't wiggle them back and forth or they'll just break off. But, it's okay if you just sort of move it once like that to get access to

**Dave Jones:** something as long as you don't push it back. Um and sure enough, I couldn't measure anything. Let's have a look. So, here it is here. I'm probing the pin like this, okay? So, I'm making good contact. There we go, but it's showing nothing.

**Dave Jones:** Look, no oscillation whatsoever. I thought, "No, I've screwed the pooch with this. I've damaged it." But, no. Uh-huh, it's a PEBCAK. Problem exists between the In this case, the oscilloscope and well, the chair I'm not sitting on. I.E., it's me, dummy, because I didn't

**Dave Jones:** realize that my scope from last time I used it was in high-resolution mode. And in high-resolution mode, it averages out and I was using a slow time base. 20 milliseconds per division. Watch what happens if I turn the time base up.

**Dave Jones:** Look at that. There it is. It's oscillating just fine, but because we're at a slow time base and I've got high-res mode turned on from before, which is not normally visible. There's nothing to tell you that. See, I mean,

**Dave Jones:** normally at any time base, you're going to see that signal and you go, "Aha, okay, I'm at the wrong time base." And do that. So, there you go. Just a trap for young players. Be careful what mode your scope

**Dave Jones:** is in. High-res mode, bit of a trap. Anyway, it turns out the reset pin comes over to a resistor and a capacitor, not surprising. And it's also right next to I'll show you. Right next to a teeny tiny

**Dave Jones:** I haven't chased the tracks yet, but right next to a teeny tiny five-pin SOT-23 there. So, that could be a power-on reset chip. So, uh-huh, that could be something wrong there. Anyway, so this resistor and this capacitor here, can probe this resistor

**Dave Jones:** and that is low. So, of course, the processor's not going to do anything. Uh-huh, we're getting somewhere. Oh, and by the way, the other thing I'm going to do as well is just pull these cables out here just in case they make

**Dave Jones:** a difference. Like like maybe the reset lines going out there or something holding them low. No, it's not that. And yep, that most certainly is a power on reset chip. Take a look at it cuz here's the uh

**Dave Jones:** here's pin uh 12, the reset pin. So, it snakes around there and bingo goes to an RC right in there and that goes over to this puppy right here and it's uh because of the bloody conformal coating next to impossible. But, I have

**Dave Jones:** gotten might be able to get it there anyway. I have gotten it under the Mantis, um which is uh well, the uh it's like the best thing on the planet for looking at uh the chip numbers, the Mantis scope, let me tell

**Dave Jones:** you. And it's um a BY3223. Now, please excuse the uh crudity of this. It's next to impossible to shoot this through the Mantis. You've got to get the right ocular path, one of the stereo paths on here. But, anyway, it's

**Dave Jones:** much clearer um to my eye through the Mantis scope than it might be on the camera here. But, anyway, you can see BY3223 is the marking code on there. To Google. Now, unfortunately, I can't uh find any data on it. And I've asked on Twitter,

**Dave Jones:** but nobody's gotten back to me. Not unusual for SMD codes like this. They're a pain in the ass. Anyway, doesn't really matter um cuz I know it's a a across the 5-V rail there. So, it's measuring the 5-V rail. We know the 5-V

**Dave Jones:** rail's there. So, I reckon that power on reset chip likely to be a dud. Anyway, the way we can prove it without uh desoldering it is to uh put a low impedance across the output to the positive rail so that uh drag it

**Dave Jones:** high. Do that maybe 100 ohm resistor and of course we've got to pierce through the conformal coating and we can do that with our sharp meter probes. And the way to do that is to put it in current mode

**Dave Jones:** here microamps mode and we if we get another meter, I'll show you why we can do that cuz you don't want to short it out with zero ohms. So Tada! We've got a 101 a 100 ohm sense resistor in there. So this is a

**Dave Jones:** this instantly becomes a 100 ohm resistor with nice sharp multimeter probe points we can get in there and short that pin. Let's do it. All right, let's give this a whirl. I'm going to short this out to the uh 100 ohms short to the positive

**Dave Jones:** rail. So we know that pin is low. I've measured it. So here we go. Let's see if the LCD does anything. Tada! Ah, look. There you go. There you go. The processor is working. Bingo! Sweet. Look at that. Winner. Bingo. There we

**Dave Jones:** go. It's supposed to scroll like that. Um but maybe because well, I I haven't got the keyboard or anything hooked up anything hooked up. But anyway, it shows that the processor is now working initializing the LCD and Bob's your

**Dave Jones:** uncle. So I reckon that chip has to be faulty. It's got to be because all it is is a across the 5 V rail. It's measuring that if the 5 V rail dips, it just very cleanly resets the processor. That's what these little

**Dave Jones:** reset chips are designed to do. I But this one has died clearly cuz there's nothing else there. It's just across the 5 V rail. So how or why it died, I don't know. But anyway, let's whip it out. All right,

**Dave Jones:** I'm just going to get in there with two irons. You could do this several one of several ways. But uh there we go. Gone-ski. All right, that chip is gone, and the great thing about this is that we don't have to do anything because

**Dave Jones:** it's already got an RC circuit on there uh like a pull-up. It's already got a pull-up to VCC, which is what we want cuz it's an active low reset uh pin. So, we want it to be normally high, but on

**Dave Jones:** power-up, we want it to be low. So, it's got that RC circuit already on there. Beauty. And the great thing about these power-on reset chips that one of the few components in electronics that aren't strictly necessary. They're in

**Dave Jones:** there as just a nice bit of engineering, you know, so when so when you get brownouts and dips in your power supply and stuff like that, it doesn't lock up the chip. So, it it recovers and resets gracefully. But, it's not strictly

**Dave Jones:** necessary. So, anyway, I've removed the chip. Let's turn this on and see what happens. Oh. Oh. Oh. Oh, that just made a complete ass out of me, didn't it? I was talking that up like there was no tomorrow, and uh

**Dave Jones:** let's see if we can uh short that pin. Like, I don't know what value cap and resistor are in there, but let's see if we can uh short that. No, it obviously needs now to be shorted to ground.

**Dave Jones:** So, let's maybe short that out to ground. Uh No, it doesn't doesn't like that. Doesn't like that at all now. That's very, very surprising. Wow. Now, here's the really interesting thing. I'm now probing the reset line, which has a 10K resistor going high. I have

**Dave Jones:** actually measured it, and it is stuck low. Look at that. It damn thing is stuck low. No wonder it's not booting. Um so, there's probably nothing wrong with that chip at all. Is it the Have we got a fire in that processor after all

**Dave Jones:** that's causing it to go low? I'm going to have to do some uh visual inspection. I I did it before and it didn't look like there was a solder short or anything there. So, yeah, that's interesting. So, what I'm going to do is

**Dave Jones:** check the continuity of that. Should probably turn the power off. Don't. Check the resistance there. No, look at that. 12K to ground. So, it's not like it's it's not like it's like shorted to ground. So, it's not a short or anything

**Dave Jones:** like that. So, if we measure the pull-up resistor here, here we go. Measure the pull-up and it's bang on 10K and that's exactly what it says it should be and it's 12K um you know, it's like not a 12K

**Dave Jones:** resistor in there, but it's like the um PN junction in there is like or whatever else it's I believe it's only going to the PN junction. So, it maybe that chip is dodgy. So, unfortunately, it's doing exactly the same

**Dave Jones:** thing as what it was before, but uh once again, I can get it to get to that point. So, I can get the processor to power up, but I don't know whether or not it's still uh locked up or not, but I can get it to

**Dave Jones:** go as far as the uh Let's try that again. I'll hold it there. Oh, yeah, there we go. So, now it's working. It's actually scrolling scrolling that text. So, there you go. Yeah, I've got to hold that pin. I've

**Dave Jones:** got a short Oh, you can't see that. Sorry, but you've got a Yeah, and then it actually locks up. If I remove the short, there you go. It locked up halfway during the scroll there. And of course, that's possible because the

**Dave Jones:** process is reset. It's no longer working, but the character memory inside the LCD here actually keeps that data on the screen. So, that's why you'll still see the text there even though the process has gone away and reset itself. Right, so it

**Dave Jones:** seems like that 10K pull-up is just not enough to do the business. We know a 100 ohms works. So, I'm thinking about putting 1K across there now and well, just a just a budge this thing up and get it working again to the point where

**Dave Jones:** I can just switch the power on and have the damn thing reset and and work, then I think I'll just whack in like a 1K resistor. Try that. Lower the values until it works. I don't know why it's not working with a 10K pull-up.

**Dave Jones:** It should, but maybe there is something a bit fishy with the chip with the reset pin on that chip, perhaps. Well, this really is quite something. I've taken out the capacitor there cuz it could have been like a failed cap going

**Dave Jones:** to ground there, which was you know, had some sort of maybe a voltage dependency failure mode or something like that that was causing it to go low impedance. But I've taken that out. Exactly the same thing happens. I

**Dave Jones:** can't get it to work if I short well, 100 ohm short with the meter here um high. I tried a 1K resistor high. Nope, nothing. So, I think what I'm going to do is um just desolder that 10K and whack in a 100

**Dave Jones:** ohm. I mean, it's horribly low value, but geez, I don't know. What else can I do? I just tried a 270 ohm resistor in there and it didn't work. Unbelievable. This is I've now put a 100 ohm resistor

**Dave Jones:** in there. Not not a bloody sausage. Yeah, let's see if I can do this trick again with the meter.

**Dave Jones:** Yep. Yep, the meter works. You can't see that and maybe you can't see that also it's scrolling, but it is. Unbelievable. So, uh like it's the same value as this 100 ohms. What the hell's going on? There's some weird

**Dave Jones:** maybe I don't know voltage dependency issue with the input or something. I have no idea, but that is I've got a 100 ohm pull up there and that is not enough to do it. It's just locked up again. All right, let's have a

**Dave Jones:** look at this pin. Look at that. It's just It's not quite ground. And that's with a 100 ohm pull up. 100 ohm pull up, folks. Unbelievable. All right, check this out. I've now got my amps jack, so it's basically like 10

**Dave Jones:** milliohms or something. It's by effectively a dead short. Look at that. Even the contrast, it's now working. Look. And the contrast is correct now, but it's drawing 146 147 milliamps. Um whereas before like it's only rated for 70. So, I've managed to actually

**Dave Jones:** make it better because it was always a very Even when it was operating out there, the contrast was really low on this thing, but yeah, it's like you practically got to short what this thing out to make it

**Dave Jones:** work. Unbelievable. Okay, what I can do now, look at this. I got 10 ohms dialed in there now and I can actually 20 ohms, it's still working. 30 40, it stops. There you go. So, at 30 ohms in parallel with the

**Dave Jones:** 100 ohms I've got in there, it's working. But anything above that is no good. So, there's something like there there's something gone wrong with that reset pin and it's pulling everything lower. I can't see any board contamination or

**Dave Jones:** anything like that. So, that is that looks like the only way to get the damn thing working. And there it is. It's drawing 100 and 36 milliamps, which is more than what it's rated to draw, but we're sort of

**Dave Jones:** cuz we're like it this thing has failed. I'm pretty sure it's got it. There's nothing else there. That track doesn't go anywhere else. So, I think the chip has failed and we're now sort of just, you know, forcing it to work. And

**Dave Jones:** you know, that's it's not the ideal fix, but it kind of is not a bad fix if you can get it working and which it now seems to be. I reckon if I go put that back in, um

**Dave Jones:** she'll work a treat. So, you know, it's not like I'm dead shorting it out. I could put a like a, you know, a 22 ohm resistor in there or something up to the positive rail and well, yeah, it's it's going to draw a bit more

**Dave Jones:** current, but I think it'll be all right. And for those who think it might have been like a short on the board, contamination between pins, I've gone around there with the scalpel under the microscope and I've actually scraped out the

**Dave Jones:** conformal coating between the pins, scraped around between the trace and the ground plane around the resonator there. And um yeah, I it's still doing exactly the same thing. So, the only conclusion I can come to is that yeah, the input the

**Dave Jones:** reset input of that chip is fried in some way, shape or form. Now, the problem I've got here is that I've just tried I'm shorting 30 ohms across there that reset pin up to positive. And of course, I powered it on and because

**Dave Jones:** there's no initial reset pulse, it's um the processor doesn't have like an internal uh by the looks of it. So, it looks like or it's part of the failure mode perhaps that it's not working. So, even if I whack a 30 ohm or a 20 like 2

**Dave Jones:** ohm in there or even short it out, when I boot it up, power it up, it's not going to work. So, I need to actually power it up like this with a higher value and then short it out and it seems

**Dave Jones:** to work. So, uh it's not looking like an easy fix even though we found the problem. I think now we're getting somewhere. I've gotten medieval on its ass and I've actually lifted the reset pin. So, you'll notice that it's not working at

**Dave Jones:** the moment, but if I touch that pin, ta-da, I can get that to work and you'll notice that there's no current draw either. So, into that pin. Bingo, was there actually contamination on the board that or something that I

**Dave Jones:** couldn't get rid of with the scalpel? Hmm. Okay, so what I've done now is I've lifted the pin and sorry, I won't show you. It's pretty horrific, but I've lifted the pin there and I've glued it onto the

**Dave Jones:** resonator there just to take the stress out of there because if you accidentally bend this jumper wire, this isn't a permanent mod by the way. It's just a temporary to test it. Yeah, if you bend that, you can snap it right off and

**Dave Jones:** that's going to ruin your day. So, what I've got is I got to pull out resistor there and now I can um re-power that, but it doesn't boot up every time. Probably I don't know, making a fool out of me.

**Dave Jones:** It was like one in five times before and now it's like now it's not. So, trust me, it was kind of booting up, but yeah, it still seems to be one sick puppy. There is still something something wrong there. So, I don't know.

**Dave Jones:** But, uh check out this 5-V ripple now. I am definitely not happy with that. Look at that. I mean, yeah, it's going down a minimum of 4.8, um but it is it is getting really bad now. So, I don't know. Seems to be

**Dave Jones:** getting progressively worse. The fire is uh getting worse. We need to just like we need to do something about that. All right, I've taken out that little 100-mic 25-V surface mount cap. Didn't have another uh suitable surface mount

**Dave Jones:** cap, so I just bodged in a uh regular axial one there. No worries, it's 220 mic, so uh at 50 V. Look at that. Clean as a whistle. So, it looks like we had a dodgy power supply there, a dodgy cap. That um that could

**Dave Jones:** explain on the rail why it took out um well, we don't know whether or not the voltage supervisory had been taken out or whether or not it's the pin. We still don't know uh in the micro, the reset

**Dave Jones:** pin, but that could explain it. The power supply could have actually taken out that reset circuit. So, yeah, that's as clean as a whistle now. Very happy with that. But, it still doesn't boot properly cuz I don't have a cap in

**Dave Jones:** there. No, this is not looking good, folks. I've got a proper pull-up in there. I've got a proper pull-down resistor. So, we've got, you know, the classic RC uh boot-up network. Values don't seem to matter. And um it's still

**Dave Jones:** pretty random whether or not it uh actually turns on. Oh, trust me. Look. Look Look at those. Look. Massive brightness on those LEDs. What the hell's What the hell is going on there? Oh, we're at current limit. We're at

**Dave Jones:** We're at current limit. Something's horribly wrong. Look, I've got it set for 200-mA current limit now, and we're at 197. No. No. Something Something's horribly wrong, folks. This is one sick puppy, I'm afraid. No. What the hell's going on there? Wow. So,

**Dave Jones:** we can actually get it to work, and the LEDs are back to normal again, but let's re-power that. I'm just uh And look, when we get that full brightness there, and the 197 milliamps, that's our 5-V rail. It's still fine.

**Dave Jones:** So, it's not like the 5-V rail is failing. There is something else horribly wrong. Look, I can cycle the power there. Now, it's No, it's still high again. No, it looks like it's going to stay in that state for a while.

**Dave Jones:** No, there we go. Now, it's normal, and it's working. Look. And it's drawing well, 96. Higher than what it's um supposed to. Nominal, um supposed to be 70 milliamps, but uh yeah, I Look. What's this video been going for, like

**Dave Jones:** 45 minutes or something? And well, I am out of uh well and truly out of uh time for today, because it is Yes, it's getting quite late. I better actually get home. Yes, I haven't got myself a proper new sports watch to

**Dave Jones:** replace. If you'll follow me on Twitter, I did lose the other one, the uh Timex one you've seen before. So, unfortunately, um Anyway, I'll get a new watch, but uh Look, I don't trust this thing at all. I

**Dave Jones:** mean, yeah, okay, we managed to sort of fix it, in quote marks, get to the point where Well, it's, you know, it it like the processor's talking the uh every It looks as if This is exactly what the

**Dave Jones:** screen you get when the thing is installed properly there. But, when we get these sort of issues with um you know, some bizarre reset issue and then now we're getting some ridiculous random over current thing. Uh it's like, you

**Dave Jones:** know, I throw my hands up and go, well, no, I'm not going to trust this um because uh there's something obviously uh something else seriously wrong with it. So, I think that's a loser. I wouldn't trust installing this back in

**Dave Jones:** and uh you know, unless I figure out what's going on with these the these two leads here and the high current uh consumption. It's just it's just way too dicky and well, I have no clue what that is. I have no schematic for this thing.

**Dave Jones:** All we know is what the processor is and uh I couldn't be bothered tracing it out and yeah, sorry folks. This is I I guess you could say that's a win, right? I reckon that is a repair win

**Dave Jones:** right there cuz we went through the whole flow of this thing and um I found that the you know, traced through the reset thing and all that and um and actually got it back up and and running. So, I

**Dave Jones:** I'm going to call that one a win even though I don't think I'm going to be able to put this thing back into operation. I'm going to tell them, nope, it's dodgy as. So, there you go. I hope you enjoyed

**Dave Jones:** that um uh 90 per 95% repair video. There you go. Hope you learned something. Um a lot of people say that even if I don't fix the things, they do like the uh troubleshooting procedures and uh stuff like that and um I I agree. Even if you

**Dave Jones:** know, I always continue to put up the videos even if I don't repair the thing because I think that they're uh worthwhile learning experiences. So, if you like that, please give it a big thumbs up and if you want to discuss it,

**Dave Jones:** EEVblog forum is down below and follow me on Twitter and uh and if you want to support me, Patreon is the way to do it. The Patreon link is down below as well. Thank you for everyone who um helps

**Dave Jones:** support the blog through the Patreon channel. It's And it's better than PayPal donations. I'm sort of going away from that. Patreons are much better system to support supporters. So, there you go. I think I've had a gutful of this.

**Dave Jones:** I'm going home. Getting something to eat. Catch you next time.
