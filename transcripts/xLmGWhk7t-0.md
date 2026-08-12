---
video_id: xLmGWhk7t-0
title: EEVblog #641 - Dumpster Cash Register Teardown
url: https://www.youtube.com/watch?v=xLmGWhk7t-0
source: youtube-asr
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. Yes, we've got a rather mundane item for you today. It's a cash register. I scored this one from the dumpster downstairs and well, I thought, you know, why not? I don't think there's going to be a huge

**Dave Jones:** amount in here. There's a thermal printer, there's a keypad, there's going to be a processor inside, there's a display up the top here and a vacuum fluorescent display on the bottom and the cash thing which I don't have the

**Dave Jones:** key for and it does actually work. It obviously came from a nearby cafe or something who got rid of it. Well, I thought we'd crack it open and have a look. Eh, you never know your luck. Now, this

**Dave Jones:** one's a Curren brand if I'm pronouncing that correctly. It is German and it's the QMP 3282 and obviously it has a this customizable keypad here which obviously you can actually get the overlays in here. There we go. It looks like it's had a couple

**Dave Jones:** of overlays and you can just print these out yourself and presumably program it yourself and looks like they've had a a couple of goes at that. So, there you go. Maybe you can see prices change over time and stuff like that and really

**Dave Jones:** there's the uh there's the overlay on the bottom and that's pretty much fixed. Is that stuck down? Yeah, it looks like it doesn't feel like a quality tactile dome, that's for sure. So, I might actually try and prize that off and have a look to see if

**Dave Jones:** they do have a proper metal dome in there. Feels very spongy and no tactile feedback at all, but you'd think that they'd have to be pretty good quality to, you know, last in an environment like this and obviously you've got the full

**Dave Jones:** rubber membrane on that because you're working in a cafe, there's spillage and all sorts of grime and grot all over the place and there you go. But, there it is. Made in Germany. Awesome. Thermal printer. Doesn't have any uh

**Dave Jones:** paper in it. But, uh anyway, let's have a look. And on the back here, it's definitely seen better days. Anyway, it's got a uh PC input, presumably like a serial uh port, and a scanner, probably another like a serial, maybe a

**Dave Jones:** custom interface. I don't know. Um and a vacuum fluorescent uh display on the back. I won't bother powering it up cuz that violates the rule, don't turn it on, take it apart. But, yeah, I have, and it does work. Now, because I didn't

**Dave Jones:** have the key for this thing, I thought I'd have to pick the lock to get the cash tray out. But, as it turns out, just get your finger in here and lift that up, and bingo, out pops the tray.

**Dave Jones:** There you go. I'm not sure if all cash registers have that, but this one certainly does. And we're in like Flynn. Look at that. Um obviously, it's got a uh solenoid in there that actually releases a catch. I could push that back

**Dave Jones:** in, but then it locks in place. Of course, get the uh software to actually release the mechanism um on that thing. And uh this tray just pops out. It's all crusty. They haven't bothered to clean that. And hey,

**Dave Jones:** looky what we have here. To change price. Key to pay, to scroll through products, cash in and pay out to finish. There you go. Somebody's written some notes and how to take daily totals and uh how to add to account, blah blah blah

**Dave Jones:** blah. Blah. But, no, nothing else hidden in there. And there's a solenoid in the back of this thing. There's a spring and uh the catch under there. You can get your finger off there, but uh there's a cable then going up through to

**Dave Jones:** the top there, which the uh process can then activate when you go open ca- when you finish the transaction and open the cash to draw. I'm not sure exactly how to get this top part he- here off. It's

**Dave Jones:** sort of Oh, yeah. Could be a couple of screws inside here or something like that holding it in. No, hang on. As it turns out, there's a thumb screw underneath here like this. And you whip that off and

**Dave Jones:** ta-da! Look at that. We're in. And that membrane keypad was stuck down on there and I just peeled that off in one piece and that's And I just pulled these straight out. I didn't have to get into the boards. Of course, these aren't

**Dave Jones:** They're just held in place by friction. That's all. So, you can just pull those out through the slot on the top here and I don't know, you might keep that for some sort of I don't know, interactive project or something like that. It's

**Dave Jones:** nice that it's clear and see-through. So, I think you'd keep that more for the things that you can't think of. Those sort of hack projects that you have no idea about yet, but might come in handy one day. And what do you know, I found

**Dave Jones:** the key. Look at that. Doesn't look too secure. And of course, that bottom tray was earth too. I That would be a local safety requirement to have that metal tray earth and I've just undone the screws there and ta-da!

**Dave Jones:** We're in. Awesome. Ooh, interesting. And there's our main processor board. It's interesting that they've got two like you know, they've got a daughter board sitting on top of that. So, we'll have a closer look at that in a minute and they've got a

**Dave Jones:** ribbon cable going over to a serial board at the back here. Obviously, that looks like an Altera Max PLD on there, actually. And then power supply under here with a nice little plastic cover on it. I rather like that.

**Dave Jones:** So, that's the main switch mode supply. And we've got some ferrites there. Cables wrapped through there a couple of turns just to take the edge off the EMI there. And that's a key switch on the side. Actually, that's probably what

**Dave Jones:** they That might be what the key is to change the modes actually on this thing rather It's got a mode switch on the side rather than the cash drawer. I'd have to actually try it. Yep, that's the key for the mode switch. There you go,

**Dave Jones:** not for the cash drawer. That's why I found it inside the printer compartment in there. They kept it in there. I don't know. This is like to set it up or something like that. Put in the different test modes or you know,

**Dave Jones:** programming modes or whatever. You'd have to read the manual. Now, of course, when you do tear downs like this, you're always looking at what sort of parts you can salvage. And there's a very nice little vacuum fluorescent display module

**Dave Jones:** there complete with all the driver stuff on the bottom. I don't know if you'd be able to get any data on that, but you could probably figure that out. I mean, it's only you know, there's not many wires on that

**Dave Jones:** interface there. So, that's a really neat board. And of course, the good thing about this interface here is that well, you've already got the working unit. So, you could get in there while it's operational and actually probe these pins and you know, work out what

**Dave Jones:** data format. Obviously, it's some sort of you know, serial type thing or four-bit interface or something like that. So, shouldn't be too hard to reverse engineer that at all. Wouldn't take that much time if you wanted to reuse that. That's a nice looking

**Dave Jones:** module. Ah, beautiful. And they've actually put this ferrite on as before they've installed this thing. How do I know that? Well, they got a nice big cutout here in the case where that ferrite actually pops up through. Otherwise, you wouldn't be able to get

**Dave Jones:** the damn thing up through there. And bingo, more salvage looking inside the display. We've got ourselves a power tip LCD module. They're a known brand. It's got the part number on there. No doubt you can get the data for that. And yep,

**Dave Jones:** I just checked. You bet we've got the data sheet for that thing. Fantastic. It turns out this is a standard Hitachi pin out LCD interface you're familiar with, but the extra pins, pins 15 and 16, which are normally the backlight pins,

**Dave Jones:** they're actually chip select, so two different pins. And then a reset pin, I think pin 17, and then a couple of others, which yeah, so perfectly usable. What a great score. Oh, hello, look what we have on the back here. That's a bit

**Dave Jones:** how you're doing. They've bodged something in there. I'm going to take a closer look. Aha, it's a 5-V undervoltage sense chip. It's a Motorola MC34164P-5. That's a 5-V version. Also comes in a 3-V version. What's that? Basically a reset

**Dave Jones:** chip, which it gives a reset output for this thing going into the reset pin when you get undervoltage. So, obviously some sort of hack here where they've had an issue with this product and you know, some sort of bug or something like that.

**Dave Jones:** They couldn't be bothered fixing, you know, the power supply's not ramping up fast enough for this thing to reset or something like that. They had issues with this particular LCD chipset in terms of reset and power on, and they've

**Dave Jones:** added this reset circuit for undervoltage lockout. So, or they've got, you know, for power glitches or something like that, the LCD might not reset properly, it might switch off or get corrupted or something like that. So, they've bodged on this reset chip.

**Dave Jones:** Interesting. And there's that Altera MAX PLD I was talking about, EPM3064 there. So, you know, a fairly old school PLD. And there's our RS-232 driver there, HA N2W1, old school Intercell stuff. There's an interesting way to clamp your

**Dave Jones:** wires down. Look at that. That actually is strain relief and sort of clamp, that actually works pretty good. I like that. But, it's clearly bodged in there because this is uh the um one of the standoffs for the uh rear

**Dave Jones:** board here. So, yeah, they've just They just haven't used that and uh it was molded in. There's a matching one over here as well. So, yeah, maybe a bit of an afterthought. If we have a look at the main board here, this uh daughter

**Dave Jones:** board on top is actually directly soldered in with that dual inline pin headers. So, they haven't actually bothered to uh put a connector in that. That's That's rather disappointing. So, you can't get that bastard out um without desoldering the whole blinking

**Dave Jones:** lot. How annoying. Anyway, what we have here is an Altera MAX um PLD again, and there's two more on the bottom board underneath this. So, they're really going to town there. And then, we have an Atmel um AT89C52.

**Dave Jones:** So, it's an 8051. Yeah, a fairly modern 8051 uh processor. So, that's what's running this top board, which is of course the uh thermal printer uh board. That's the thermal printer interface there. So, um that is uh So, they've decoupled the

**Dave Jones:** functionality of that from the main processor under here. And they've got two Those two there are MAX II PLDs or MAX uh PLDs. They're not even MAX II. Need to have a look at that puppy there. And we've got ourselves an ST L6219

**Dave Jones:** stepper driver uh stepper motor controller there. And up here is an L293. That's actually a quad uh push-pull driver. It can uh source basically uh 1.2 amps uh peak on all four channels. Not a bad little beast at all. That's basically exactly

**Dave Jones:** what you need for a thermal printer interface. You need the uh push-pull driver up here for the uh heater for the thermal heater. And then you need uh the stepper motor uh driver down here as well. And presumably there's decoupled

**Dave Jones:** all of the hard task of actually controlling the thermal printer into the into the PLD here. They're not doing it all in software up here. So, you can see the traces actually running back down here to the Max 2 Max PLD. It's not a

**Dave Jones:** Max 2. Keep calling it a Max 2. So, the Tair Max, it's the original. And that RDC R8820 under there, I had no idea what that was, but it turns out there's an RDC semiconductor company. That's their name. And this R8820 is a 16-bit RISC

**Dave Jones:** DSP processor. Who the hell's ever heard of that? And it didn't make any sense for it to be like a its own architecture or whatever. And it turns out it's not. It's software compatible with the Intel 80C186. So, there you go. 16-bit 186 processor

**Dave Jones:** just from a you know, a cheaper, more obscure company. And then they've probably RISC'd it or some, you know, they've sort of like re-engineered it, but it is software compatible. So, you can presumably use all the software tools for the 80C186

**Dave Jones:** to actually develop the software for this thing. So, there you go. As I said, two other Max PLDs under there. There and there. So, I don't know. They're driving all of this and they're doing off you know, they're

**Dave Jones:** offloading lots of tasks from the two processors in here. The main processor down the bottom, the top one 8051 controller just controlling the thermal printer up there. So, they've they've really offloaded those tasks to all that glue logic and stuff like that, stuck it all

**Dave Jones:** together in those PLDs. They're probably not massively complicated, but uh, worthwhile to uh, cuz ultimately there's not much else in here, but you don't really need anything. I mean, you need a processor, you need some RAM and some

**Dave Jones:** ROM, and, uh, you need a driver board for the, uh, thermal printer, but apart from that, um, and and a communications interface, but apart from that, you don't really need much else. So, not entirely sure what they're doing in

**Dave Jones:** those two max, uh, PLDs on the bottom there. And that makes sense. A, uh, nickel-metal hydride backup battery there. Um, 70 mA hours, little tiny little thing that, uh, charges up. This explains why when I booted this thing,

**Dave Jones:** it went through an entire boot process and, uh, did all sorts of resets and calibrations and all sorts of, uh, uh, stuff. And when I powered it up a second time, it just instantly And that took some time to boot up. When I powered up

**Dave Jones:** the second time, it just booted up instantly. So, obviously it, uh, yeah, that was dead flat. Of course, you'd expect it to be. And that there looks like a decent little quality, uh, switch mode controller. I like that. It's, uh,

**Dave Jones:** well laid out and, uh, looks like it uses quality parts. That's really quite, uh, nice. Nice heat shrinking around, uh, the input, uh, looks like a a small common mode, uh, choke there and all the, uh, the power resistors are all,

**Dave Jones:** uh, the diodes, everything all raised off. And, uh, that is really quite nice. And Nippon Chemi-Con capacitors, no worries whatsoever. Yeah, Nippon Chemi-Con again. No dramas whatsoever. So, that's nicely engineered. Look at that. That's pretty decent. Good on the

**Dave Jones:** Germans. And this is interesting. Look at these two black wires here. These go off, uh, to the thermal printer, but they're not a supply output. Take a look. It's two ground pins. So, they're actually getting return high current

**Dave Jones:** return ground coming back from the from the thermal printer instead of it all traveling through that digital board there. So, they've got the power running over, but then a separate ground loop running back just for the thermal printer. So, you don't get all of those

**Dave Jones:** uh current pulses going through your ground plane on your uh board. It's a digital board um and primarily, so it shouldn't matter too much, but yeah, they determined that yeah, that was the best course of action is to return the

**Dave Jones:** uh ground from the thermal printer. So, all the power So, the power and data comes in here, but they're using this wire as the return ground path. Neat. And they've done this right. Look at this big ass earth strap going across

**Dave Jones:** here like this over to the main uh plate up the top, all nicely crimped and screwed into place and uh yeah, that's the yep, earthing on this thing's done right. Aha, that ground return, a budge afterthought. Look at this. They're

**Dave Jones:** obviously skipping some of they need an extra low impedance path from there to there, and they've budged on this connector, which is that return ground. Oops. They found that Oh, they designed and built the thing, and then found that oh, they were getting some

**Dave Jones:** issues with their board and probably scratching their head for a couple of weeks trying to figure out what was going on, and then some poor bastard chased and traced out the ground, and uh well, there's an internal ground plane

**Dave Jones:** in here, but then try they'll probably getting some excess ground bounce on there or something like that when this printer operated, this thermal printer, and uh yeah, they decided well, to fix it, well, we're not going to respin all

**Dave Jones:** of this, are we? No, and have a separate return path on the inner planes and stuff like that. No, bugger that. We'll just put a um we'll just put some extra low impedance path in there, and then just return this to those spare

**Dave Jones:** pads that they had on that power supply. Uh all right, I was going to say it was well engineered. It's a budge. Now, I guess it depends on what you're into, but I personally wouldn't save that thermal printer module. I can't think of

**Dave Jones:** a a good use for that. There's a little contact switch down in there. There we go. That's neat. Yeah, I don't know. Not really worth salvaging. I don't know if if you guys do actually keep something like this when you tear us apart, tell

**Dave Jones:** us apart and tell us why. Um but yeah, I know the answer because I answered it before in that it's for those things you can't think of, right? All right, we'll hoard it. Caution, do not touch the flat

**Dave Jones:** oval plate. What's under here? Ooh. Scored a nice little stepper motor out of that. Yeah, that's a keeper. That goes in the motor box. And there is the thermal printed head on this thing. That's the header that connected up to

**Dave Jones:** it. And uh you can see that they've got some drivers gunked down on there. Some chip on board stuff happening down there. And I'm not sure how many uh pixels, if that's the correct term, dots across there. Uh that one here is. I might be

**Dave Jones:** able to get the macro lens on that. Oh wow, look at that. We can see it. There we go. You can see the individual lines like that. Look at all those fine traces. I can barely see this on the LCD

**Dave Jones:** screen of my camera. They'll probably show up really well in full HD. But you can see that each one of those chips drives, however, if anyone's keeping count there, drives however many uh dots on that on that thermal head there. So, you can

**Dave Jones:** see the chip all gunked up inside there, but yeah, it'd be interesting to get a data sheet on one of those uh driver chips, that's for sure. Hmm. So, there you have it. That's inside one of these thermal printers. Isn't that

**Dave Jones:** rather interesting? I haven't had a look at in detail inside one of these things before, but uh fascinating stuff. If anyone does have any data on these things, then uh please share it. And this one's fancy pantsy. It's got a paper cutting mechanism on

**Dave Jones:** top. I just prized that open, and there's the There's the paper cutter there. It's angled to uh slice more easily through the paper, and that's just driven by this uh worm drive here on this motor. Nice. So, no, you know,

**Dave Jones:** the cheap ones will just have like a perforated edge on the outside where the motor just uh spits the uh paper out, and then you use it has to tear it off. This one actually uh cuts your receipt

**Dave Jones:** for you. Ooh. Actually, I'm rather inclined to keep that as a complete mechanism like that, cuz it's not often that you'll be able to, you know, get something that just shears off something like that based on a motor input. So,

**Dave Jones:** yeah. Hmm. Anyone got any creative uses for that? So, there you go. I hope you enjoyed that teardown Tuesday. And even something mundane as a cash register, um you know, contains um you know, some fairly uh decent uh processing in it,

**Dave Jones:** and you can salvage some nice parts from it. You get a couple of motors, you get a cutting mechanism, nice vacuum fluorescent display, that's just beautiful, a nice reusable uh 128 by 64 dot matrix display, a power supply, nice

**Dave Jones:** little power supply you can reuse, main switch mode job. Well worth the salvage. So, there you go. As always, uh the data sheets for the things I found in this will be linked in down below, so check it out.

**Dave Jones:** And if you want to discuss it, jump on over to the EEVblog forum, or you can always leave a YouTube comment. Yes, I do read all the comments, or you can leave a comment on EEVblog.com. However you prefer to do it, I do read virtually

**Dave Jones:** all of them and I try to respond where possible. By the way, if you do want me to respond to your comment on YouTube or wherever, generally within like the first 24 or 48 hours of uploading the video, I'm going to be checking the

**Dave Jones:** comments on that video. So, you know, there's more chance that I'm going to reply there. Anyway, I hope you enjoyed that and if you did, please give it a big thumbs up. Catch you next time.
