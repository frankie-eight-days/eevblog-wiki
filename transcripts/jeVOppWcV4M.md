---
video_id: jeVOppWcV4M
title: EEVblog #1360 - REPAIR - Aircon Control Panel
url: https://www.youtube.com/watch?v=jeVOppWcV4M
source: youtube-asr
---

**Dave Jones:** Hi, in a video on my EV blog two channel, which I'll link in just about the background of the bench and everything here, I had a non sequitur about my air con unit on the wall here, and I'm going to have to actually move

**Dave Jones:** this cuz now it's actually really difficult to reach over my 900 mm long bench, and it's even further out from the wall. So, like a meter out. I've got to like reach over a meter to turn my air con off and on all the time, but one

**Dave Jones:** of the problems with this damn thing is that I slowly over the last couple of years, like I swear when I moved in like a decade ago, this thing used to work. You press the on off button, it just

**Dave Jones:** worked, and that's how it worked in my rented lab. It had the exact same uh controller in it. But, this one is a pain in the ass. It's been pissing me off for a long time, so I'm going to

**Dave Jones:** finally uh do something about it. So, let me show you what's actually happening here. When I press the on off button, it doesn't just turn off or on. Now, the only thing I do here is cool down this lab. I never ever heat it up, but

**Dave Jones:** it never gets that cold here in inside. I'm in the middle of one of these big high-rise uh you know, office uh tower kind of things, and it'll get up to like uh like 25° in here or something. So, I'm always

**Dave Jones:** cooling down, but it never drops below like 20 or 20 1 even in the middle of winter. It it stays, you know, so I've never ever in a decade had to use the heating function of this. So, I'm always

**Dave Jones:** using the cooling mode. So, all I want to do leave it on low fan speed so that, you know, you might be able to hear it in the background, but it's really hard. You'd really have to amp it up. Generally, when I shoot

**Dave Jones:** videos, I'm turning the air con off just so there's no little air con noise uh bleed, but generally, I just have it continuous low auto mode cool, and that's it. I've got my temperature set to like 21°. I

**Dave Jones:** There's got a timer thing. So, it's 22 It thinks it's 22 at the moment, hence why the air con's running, and uh that's the set temperature. So, I'll leave it set at that, and I just turn it on

**Dave Jones:** and off. That's all I want to do. It's not asking much of an air con system, but watch this. It'll probably make a fool of me, but I you can see it's like worn the silk screen's worn off that, but watch this, right? I

**Dave Jones:** pressed it. It went into heat mode. What the? This is an on-off button. I swear over the years I've been slowly convincing myself that it's like how hard I press the button, how long I press it, all sorts of you know my

**Dave Jones:** mind's just coming up with lots of weird convoluted explanations for what Oh, there we go. It it turned off. That's what I want it to do, right? But I obviously and I can turn it back on, but there you go. It goes into heat mode, it

**Dave Jones:** goes into cool mode, but it's still like continuous. And it it it just doesn't seem like it didn't turn off or on if I hold it down and then release it, it'll turn off, but it's not supposed I don't

**Dave Jones:** believe it's supposed to work like that. So, anyway, somebody in the previous videos um said, "Oh, they're pretty sure that these uh the keypad on this thing with all the buttons works as a like a ladder divider, basically a resistive

**Dave Jones:** divider, and that might explain uh you know it could be the contacts could be dodgy, it could be picking up noise from somewhere. Like who knows? You know, there's uh various things that can go wrong with like you know high impedance

**Dave Jones:** ladder uh dividers like this. So, I thought we'd actually you know take it off the wall cuz I want to move the damn thing anyway um and have a teardown and then just uh investigate possible uh fix for this or or if I I might want to put

**Dave Jones:** it back and then I could actually design a secondary possibly if I reverse engineer it, design a secondary button which then I could mount uh somewhere else and wire it in parallel. I assume it's like some sort of I assume like

**Dave Jones:** there's a might little micro in there that that communicates via RS485 some differential thing which goes back to the controller. So, I Yeah, I assume that's it. I probably don't want to go to the effort to reverse engineer the

**Dave Jones:** RS232 RS485 protocol or whatever it is and do that, but I don't know. Maybe I can like budge in some remote switch somehow or something. Anyway, let's take it off the wall. Do a tear down. I can't bloody well turn it off. Oh, I

**Dave Jones:** did did. I swear. I pressed it like five times before and it didn't turn Oh, duh. All right. So, it's probably got some bracket thing and it's probably painted onto the wall. When I had this place painted and

**Dave Jones:** painted when I rented it out, so usually you got to break the seal around the paint job. Now, it's not going to come off without a fight. I'll get back to you. Doll, totally forgot to show Yeah, it does have a

**Dave Jones:** brand on it. It's an Easem brand, but I believe the air con I've got like isn't Actron, but Doll, it turns out that's a Leasem. That's an L with like air coming out of it. Get it? Leasem. Anyway,

**Dave Jones:** Australian thing and yeah, I found a manual for it. So, yeah, but that doesn't help me get the damn thing off the wall. I was able to get the There's a bottom like stick on decal thing which hides the zone buttons there. I don't

**Dave Jones:** have multiple zones, but I still cannot get this damn thing off the wall. I know there's clips and there seems to be clips on the bottom, but Hang on. I think I got the bastard. Heard a crack. As I don't know if that was an injury

**Dave Jones:** from it or not, but it's off. Bloody clips on the bottom. OEM Electronics Proprietary Limited, Sydney, Australia. You can see all the hacks I had at it. And that's like That's crude as. Anyway, decent amount of cable. Ta-da! So, I'll disconnect

**Dave Jones:** that and bring it down to the bench. First of all, I'd better document what's connected to where cuz all but the black one is damn white. So, yeah, I'll put some markers on those. First of all, let's measure the

**Dave Jones:** voltage on this thing. Oh, one-handed technique, 17 and 1/2 volts. Wow, that's That is surprising. All right, so here it is, the least some controls. That's I guess the part number, is it? Interesting to find DIP switch controls on here. This is

**Dave Jones:** interesting. Like integral SNS, which would be sensor one here, which was actually connected. So, I do actually There is a sensor elsewhere in the room, but I've never actually checked at all if that actually works or whether or not it uses the internal

**Dave Jones:** sensor in here. I don't know. It regulates the temperature fairly well within plus minus half a degree, by the way. I've done temperature logging plots of this thing, and it gives, you know, a sawtooth plus minus, you know, like half

**Dave Jones:** a degree. I think we want no zones, so I don't know why zones are set. I'm pretty sure I've only got the one zone here. But anyway, it is set to remote sense. So, I don't know why the sense one line

**Dave Jones:** is connected. That's interesting. I'd probably rather have the integral sensor. I might experiment with that. Heat pump or cool elec. I don't know what that is, but yeah, we basically want cool elec. What is it Does this thing even heat up

**Dave Jones:** at all? I I don't know. Continuous fan or auto continuous fan. Definitely don't want continuous fan, so that's right. Three-speed fan. It does have It does seem to have three speeds cuz it goes through it on the display, and it does

**Dave Jones:** seem to move a larger volume of air with the different speed. So, there you go. Anyway, yeah, as I said, I was wrong about the um differential pair RS485. We've got common power, which, as you saw, 17 and 1/2 volts. So, there's

**Dave Jones:** probably just like a a 12-V linear reg on here or something, and then there'll be a 5-V linear reg for the micro cuz, you know, these things don't take much power. So, you don't need any of that switchy regulator rubbish. And the aux

**Dave Jones:** line is obviously what's sending the back so, or is it a just a resistor ladder line from the power as the YouTube commenters suggested. But anyway, I've got some cutouts in here for these electrolytic caps and a big whopping power resistor

**Dave Jones:** up there. That's because, well, they could just couldn't fit in cuz part of the case, yeah, it's curved down there. So, I had to, you know, I had to get the nice curvy look. They've had to cut away

**Dave Jones:** the PCB and then yeah, none of that surface mount rubbish. So, it's, you know, it's clearly an old design, you know, probably dates from like the '80s or something. Anyway, let's get this PCB out. It just seems to Oh, I don't know,

**Dave Jones:** there's two screws there. All right, there we go. Got it. That's rather neat. I like that. Exposed pad fingers there. They've got the solder coat finish. Let's flip it over and they've just got the nuts. Oh, I got to keep those

**Dave Jones:** square. Oh, no, they'd actually That's what the molding's for. It's pretty much what I expected. A micro, a few miscellaneous bits and bobs, and it's looks like that a rechargeable battery down there cuz you wouldn't have a fixed

**Dave Jones:** lithium in something like this, would you? I don't know, it could last forever. Anyway, that's for the real-time clock cuz this thing does have a timer. And you can see right up there. Geez, that's a weird layout, isn't it? I

**Dave Jones:** mean, you know, you've got your real-time clock chip. There's your 32.768 kHz crystal, and and your battery's all the way down there. So, yeah, that wasn't good planning on your PCB layout point of view. There you go, that's a bit of a surprise. We've got

**Dave Jones:** ourselves an ST micro in here. You know, I would have maybe expected an old-school PIC or, you know, like a Motorola part or something like that. But an ST 72C334 part of that series. So, here's the data sheet for that, but yeah, it's just a

**Dave Jones:** general purpose 8-bit micro designed for So, yeah, that's well and truly obsolete. You can't really get that from any mainstream suppliers now. You'd have to beg, borrow, steal one of those from the gray market if you wanted to replace

**Dave Jones:** them. So, you know, they probably bought up all the stock they could. You know, you buy like 10,000 of them, that'll do you for the next 20 years or whatever. But yeah, anyway, and it's just an 8-bit micro and looks like we have some We've

**Dave Jones:** got some LED drivers here. What are they? Oh, they're ULN2003 transistor arrays. Old school. So, you no doubt saw on the video you probably would have seen the multiplexing of the LEDs. So, they're doing all of the visual like the

**Dave Jones:** indicator LEDs plus the seven-segment displays are all part of the same big-ass matrix there. Switches. This micro like this is obviously a switch array. So, it's all going into the micro. Well, I don't I don't actually until I trace it out. I don't know for

**Dave Jones:** sure, but I might trace out the sense line down to branches off there. Thank you very much. But it goes down here. It goes down here. Aha, sense. There you go. That's the That's a thermistor. There's your temperature sensor. So,

**Dave Jones:** yeah, I like I suspect that the micro on here is not doing anything. It's just an interface to you know, switches and the LED display and everything to tell the aircon controller which will be up in my roof

**Dave Jones:** here. That'll be the Actron Airtron aircon controller. Yeah, so it might say oh, remote sense. But the remote sense might actually be on here. So, I don't think that the micro is actually sensing the temperature. Well, no, it does

**Dave Jones:** branch off, doesn't it? Maybe it does God, it goes under a switch there. Those two chippies down in there which it seems to go down to. That one looks like it's a little ST op-amp and this one is

**Dave Jones:** a you classic 393 in dual comparator. So, yeah, it looks like maybe it does go down to there somewhere. So, maybe and as I suspected that's a linear 5-V regulator but that's what the resistors there for. It's just a dropper. It's

**Dave Jones:** just a dropper. That's it from the 17.5 V rail. Old school. Now, that's switching rubbish. And what's that? Is it another 5-V reg? One for digital, one for the analog matrix, maybe? Anyway, first thing is the switches. I

**Dave Jones:** thought like that might might have been like a rubber membrane type thing, but it's not. That's a genuine tactile. So, really I wouldn't expect that to wear out. It's not like this has had like a million operations or anything. I do

**Dave Jones:** have a genuine fault in that like an intermittent contact in that tactile switch. Be I was hoping that it would be that and that it would you know, I might be able to like re-silver the bottom of the contacts or

**Dave Jones:** something like that on the rubber baby buggy bumper membrane, but no. It's a that's a real tactile switch. It still seems to have its tactile feel. So, I I'll measure that though. I will actually get the meter on there and make sure it just

**Dave Jones:** goes zero and it's not just dodgy ohms. Okay, we've got 14.2 K there. That does indicate that uh it could be the resistor ladder, but let's just Oh. Oh, I'm pressing that. Oh, yeah yeah, it's a bit a switch. Yeah, that's that's

**Dave Jones:** dodgy brothers. 3 ohms, 1 ohm. Oh, when I move I'm rotating that, pivoting that side to side. Oh, yeah, that switch is dodgy. IT'S DODGY AS. WOW, A tactile switch 96 ohms, 75 ohms for A TACTILE SWITCH. AH, WHO WOULD HAVE THOUGHT?

**Dave Jones:** THERE you go. That's a repair right there. We don't want a chicken dinner, I think. That's like a joystick. We've invented a joystick. Um yeah, the world's yeah, the Clayton's joystick. Wow. That right there is complete dodgy brothers. So, yeah, I'm not sure I have

**Dave Jones:** or maybe I might have to look through my old boards. This is why you keep like scrap boards and stuff. Maybe I I might find something similar cuz the shaft length is going to matter because it's got to come through the

**Dave Jones:** button like this and then it's got to push onto that. So, it's not like I have a stock of tactile buttons. Have to look through old projects and stuff like that. Hmm, and therein lies the uh the the dilemma. Do you store your

**Dave Jones:** parts based on project, which I do a lot of the time? Well, I've probably got half half. Half my stuff uh you know, switches like this. I would a project box containing just parts for a specific project that I was working on, you know,

**Dave Jones:** cuz if you want to pick up the project again, then all the parts are there, all your stuff, all your boards, all your development, whatever for it is all there in in that one box ready to go, ready to get back into it. If you don't

**Dave Jones:** ever want to work on those projects anymore, you can say, well, it's you're better off putting those into like a generic component bin labeled SMD switches. But, you know, how often do I need a to get an SMD switch?

**Dave Jones:** Not very often. All right, so what I've done now is hooked up the probes to the common terminal and ground. It's supposed to go to There you go. Let's try another button. 13.1 13.3 13.6 You're seeing a pattern? Nine like

**Dave Jones:** eight. Uh the these contacts are dodgy down here, by the way. Get the idea that yeah, this seems to be YouTube commentator was right that this is some sort of divider array, but he mentioned voltages go down to zero. But pressing these

**Dave Jones:** buttons does affect the AUX line. So that's in the So it shows that that AUX line is not like, you know, some sort of digital output coming from the micro or anything like that. It It's analoggy to do with the buttons, which

**Dave Jones:** is really interesting. Unfortunately, here's where Murphy gets you every time. You try and trace this out. This comes across to this via here, goes down, drops under there, which then goes under a damn switch. So doesn't go there. I guess I can trace

**Dave Jones:** that that resistor there with the AUX line. Yeah, I was right. There you go. This is how we start tracing this out, but I I'm not going to do a full reverse engineer of this. Jeez. It does seem

**Dave Jones:** that's connected through a 10k resistor. Well, there's two 10k resistors here, but I believe they go over to Yeah, this pin the micro over here. So the AUX line is Is that like I don't think that's a pull-up. No, the other side of that is

**Dave Jones:** not a pull-up. I'm just using a bypass. That'd almost certainly be the bypass cap for the chip down there. So it's not not pulling up to the micro rail. So Yeah, there you go. So they got that pin

**Dave Jones:** through a 10k to the AUX over here. But where else is it going? Hmm. Okay, I did find out that one of these 10ks does go down to ground here. So the AUX line is actually 10k to ground and you can I can

**Dave Jones:** show you that over here. There you go. 10k to ground and then the other side of that um well, exactly well, Here you go. It's exactly that 14.2, which is varied by the buttons there. So that's the 5 V

**Dave Jones:** rail. That's between aux and 5 V rail there. So it does have a built-in ADC. So yeah, I guess that I presume that they're not doing a switching matrix here, but they're yeah, reading the analog voltage from there

**Dave Jones:** and that would make sense if this is giving you a dicky contact, then you would expect that you know that the voltage would be all over the up and all over the place and it could be sensing incorrect things. And that's

**Dave Jones:** what I'm actually experiencing. I've been experiencing over the years is this thing just you know, just mucking around not being consistent at all. And of course if this was just your regular switch matrix, then the really the dicky

**Dave Jones:** contact on this wouldn't really matter because it would be you know, it doesn't matter whether it's couple of hundred ohms or zero or one ohm, five ohms, whatever it is. It doesn't really matter. It should It should either

**Dave Jones:** register or not on your key matrix. So yeah, obviously they're doing this as like an analog sense thing. So I don't think that the analog sense is going directly to the aux. Let's say it's going into the micro. Anyway, I think

**Dave Jones:** what we need to do is hook this thing back up and actually put a scope on the aux pin and see what's happening. Now before you go probing anything like this, you don't want to assume that the ground wire on there, that black one is

**Dave Jones:** mains earth referenced. If you do and it's not, then you can come a gutser because I've done a video how to not to blow up your oscilloscope about ground earth referencing and stuff like that. So before you do that, you can either

**Dave Jones:** just use your We'll talk about this in a minute. High voltage differential probe like this, which it makes it safe or you can actually check it. So I'm just going to check that now to see what's what. So

**Dave Jones:** I'm just going to I know this is mains earth referenced down here and that's the measurement thing we're using or Or could use like your portable scope or whatever, but anyway, let's let's have a squeeze. Put your tongue at the right

**Dave Jones:** angle. Yep, that's mains earth reference. So, no, it's got zero. Why has it got absolute zero? It's kind of a little bit interesting that it had absolute zero there. So, I'm going to see if I can measure any voltage on that. No, there's

**Dave Jones:** no AC voltage. That is genuinely connected. Yep, there we go. And I double-checked that with my BM235, and sure enough, yep, it's zero point Yeah, this one has an extra digit. This is the new BM786. Hopefully it'll be available

**Dave Jones:** very shortly. 0.04, but maybe there's like a little bit of residual voltage on there due to like the ground going from the air con unit through to the scope here, and that's maybe just causing it to offset a little

**Dave Jones:** bit. That's sort of to be expected when you start introducing even very minute voltages into a pretty precision measurement thing like the ohms range on a multimeter screen. So, we could hook our scope probe straight up. Oh, that's a bit of a

**Dave Jones:** bummer, cuz I wanted to use the new Mix Egg and DP10007. And this is a new model, which they designed at my request, cuz I wanted a times 10 times 100 one. They've got others in this DP10000 series that have a different divider

**Dave Jones:** ratios, but I wanted one to match my HVP70 probe. A potentially lower cost option for that. I've got to fully test this one, but everyone says, you know, it's a pretty decent performer, and it's lower cost than the HVP70.

**Dave Jones:** So, I might eventually carry this on the EV blog store. That's the plan. But yeah, they specifically made this to my request, like took them like six or nine months, and they eventually said, "Yep, we can do a times 10 times 100 design."

**Dave Jones:** So, you should see the specs of this match almost precisely the HVP70, except it's uh it's a little bit wider bandwidth but otherwise very similar specs all round. Anyway, I'm probing the aux line there and uh huh if we single

**Dave Jones:** shot capture that, look at that. So, that's you know, it's got some ripply doodar on there and periodically is that going to be a 50 hertz thing? Oh no, 515 hertz. There you go. That's interesting like it's doing some sort of periodic

**Dave Jones:** scanning or something like that perhaps. I can't get a consistent trigger on that so uh huh at a long ah it's packet based. There you go. It's packet based. Trap for young when basically if you see an otherwise periodic you know, if you

**Dave Jones:** zoomed in like this if you see like what what you think you know, you do single shot capture like that and this looks periodic. If you zoom out like this this is just a how to use a scope thing and

**Dave Jones:** it appears periodic like that but you've got your trigger level set to where you think it should trigger from and if you actually put your scope into run mode and it doesn't trigger like that at the trigger level you thought it

**Dave Jones:** does either above or below like that then obviously it's got it's not completely periodic so then you know to zoom out and uh huh of course it's a packet based thing at there you go 2.7 odd hertz something like that. And

**Dave Jones:** there's a too is a packet on there whether or not it's like an actual packet whether it's supposed to do that or whether or not that's just I don't know it's a noise pick up on the line. I

**Dave Jones:** like have no idea the air con's not actually working at the moment so anyway, let me switch it on and see if you can see a difference. Okay, here we go big power button. Oh. Do you see anything in that? Let me

**Dave Jones:** press it again. It's gone oh that's not analog level. It's So, yeah, it it seems to be doing some packety-based thing there. I like I don't You know, it's kind of not what you expect, is it? I don't know. If

**Dave Jones:** anyone's got any details about this, you know, if you're into this air-con uh control air-con market air-con controllers and stuff like that. So, the YouTube commenter uh asked Steven G, um I'm not sure where he's getting his voltages uh from, but yeah, here's his

**Dave Jones:** uh post where he says, "Yeah, like the voltages uh when you press the buttons." And that uh makes sense from a point of view of that uh it was possibly confusing my on-off button cuz it's down it's supposed to be

**Dave Jones:** like 0 V, but where's he actually measuring that from? I don't know. I'd have to do more. It's It's certainly not on the AUX line, that's for sure, because this is the AUX line here. So, yeah, mhm. But, it does make sense in

**Dave Jones:** that uh it could be confusing the on-off button with a because it's, you know, saw the dodgy resistance there, um it causing a problem, a conflict with the next one up the threshold level, which was the uh heat cool thing. So, that's

**Dave Jones:** why it was sort of like jumping into heat or cool mode randomly when I tried to turn it off or on. So, that makes sense. Okay, so the way we can trigger on this is our pattern looks like every

**Dave Jones:** uh 500 ms. So, I'm going to change my told off time here to uh oh, it's all over the shop. Oh, jeez, that's a that's jumping around. Oh. Anyway, let's set it to like, you know, I don't know, 400 ms or something

**Dave Jones:** like that. There you go. We should be able to trigger off that fairly reliably. Where's my trigger point? Yep. There you go. So, I'm sure I've done videos on this. So, what happens is after the trigger, it waits another 400

**Dave Jones:** ms before it arms the triggering system again, so that Yeah, it'll arm within that dead period. It'll uh re-arm about there, something like that. And then it'll capture the next packet. So, that's how we can reliably trigger on

**Dave Jones:** that. So, there you go. Okay. Now, watch that. I am going to turn the on-off button. Oh. Oh, has that changed? Oh, wait. Hello. Press it again. No, so it's changing my It's certainly changing. You can see. Is

**Dave Jones:** it back on? Oh god, I can't see it cuz it's back to front panel's back to front. Ah. Okay, that's all that's all aircon on. That's aircon completely off. So, that's completely off. So, I've got all pulses there. So, aircon

**Dave Jones:** and now it's on auto cooling. So, what I'm going to guess here is that maybe it It just continuously sends out the last button that was pressed, perhaps. And then the different combinations are what you see here. I

**Dave Jones:** I don't know. Leave it in the comments down below if you've got a better idea of what's going on here, but that that seems to be the case cuz this is just repeating, repeating. I'm not touching these buttons. This is just like this

**Dave Jones:** code just changes and stays changed every time you press a button. So, let me go off again. And hopefully we'll get all of them back again. Okay, yep. It's off and yep, we get all of them back. So, that seems consistent.

**Dave Jones:** So, I think we're onto something there. So, it seems to be just transmitting, yeah, over and over again the last key that was pressed. And then the controller that it's going to, the aircon controller, knows, well, you know, I'm not going to do that again

**Dave Jones:** because you've already pressed that button. But ah, okay. Right. No, so the micro, right? Because the on-off button is the same for both on and off. So, it needs to know that you've pressed it again. So, when you

**Dave Jones:** turn it on, it switches to another mode. So, it's not outputting what key, it's outputting the last key and mode. Something like that. It's a bit how you're doing. It's not what I was expecting. So, doesn't look like it'd be something easy to sort of

**Dave Jones:** like build another controller to do it. You'd have to spend a bit of time reverse engineering this and figure it all out. It's It's certainly not that voltage level system that Steven on the comments was alluding to, but that that might be like

**Dave Jones:** internal. But, that certainly pointed to the switch. So, yeah, that switch array they are probably are using like an ADC internal to the micro to detect the switch and that's we're just getting that dodgy switch. So, anyway, I think

**Dave Jones:** that's enough [ __ ] around with the waveforms there. I think I'll just go in there and see if I can find a replacement switch and then just get this back up and running at the very least. And if we power it from an

**Dave Jones:** external lab supply here, it does actually well, it powers up, but it just ends up flashing, does a little power on cycle and then flashes zone one here. So, and of course the the power button does absolutely nothing as you'd expect

**Dave Jones:** because it's got nothing to do with the power of this unit. It's designed to talk with the with the main controller. So, unfortunately, I've I've probed the aux line here and we just get no volts. So, it's not doing anything.

**Dave Jones:** Yeah, it's doing Okay, so after it's power on sequence, it Yeah, it's but it's well, no, it's periodically doing something, is it? I need to trigger off that. No, I can't trigger off anything there really on the positive side or on

**Dave Jones:** the lower side either. So, getting diddly squat. So, it's not It's not doing anything. Yeah, is that can signal being actually provided by must be provided by the controller, I would assume. And then the LM 339 that we saw on here, the dual comparator,

**Dave Jones:** that's exactly what you'd need to decode this. So, you just decode it at you know, two different threshold levels, and turn it into a digital signal, which this thing which the micro can then decode very easily. So, yeah, it looks

**Dave Jones:** like this thing is just a passive slave. It doesn't do anything without the signal being generated by the master controller. So, it seems to just sit at mid-rail there as you saw, and then just pulses up and down. So,

**Dave Jones:** yeah, it doesn't do us anything. Completely forgot. Oh, well, not completely because I did eventually remember that I do actually unlabeled I really have to label I do have a thing full of switches. But, unfortunately, these are No, hang on.

**Dave Jones:** Maybe maybe I can find one. Oh, that's a bit shorty. Oh, that's super long shaft. Look at that. Oh, that one might do it. I can always cut the shaft to length, and yeah, might be through-hole, but I can fix that. There

**Dave Jones:** you go, successfully chopped off and converted to surface mount. No wackers, I'll trim those leads. They're a bit long, but yeah, just trim the leads and we're good to go. There you go, like a bought one from brown to black. No

**Dave Jones:** worries. And it's got a nice snappy feel to it. Okay, let's just re-verify that dodgy brothers resistance there. Need the old third hand. Oh, yeah, 100 190 ohms 170 ohms. Wow. Can I get it right down? I'm pushing really hard ON THAT.

**Dave Jones:** THREE OHMS two ohms. Yeah. Dodgy. Now, let's put in our new switch. 14.2 K. Press it, and zero. Thank you very much. I don't think we're going to have any more issues. That looks pretty darn repeatable to me. And give it a

**Dave Jones:** little wiggle wiggle wiggle yeah down the bottom. No, it's all good. All right, let's see if this sucker works. Here we go. One push. Oh, nice clicky. Nice clicky. AND OH, BEAUTIFUL. FIRST GO. Got to do it a

**Dave Jones:** couple of times. Where are my poor egg on? Oh, it's flashing run. I don't know why it flashes run. But yeah. Yep. Fixed. And there we go. Auto heat cool. Yep. Winner winner chicken dinner. That is fixed. So, it was the like a switch.

**Dave Jones:** I thought maybe it might be like a membrane type thing. Turned out to be a tactile switch. Usually it's pretty rare that those tactile switches uh fail like that. Have seen it before, but it's not something It's not my initial conclusion

**Dave Jones:** that I'd jump to for something like this. And as I said, if this was arranged this was designed as a switch matrix in the micro as you'd normally do it, you know, you'd have a bunch of digital lines for the common

**Dave Jones:** done bunch of digital lines for the rows and then you multiplex them and you scan continuously scan the keyboard. It it really it doesn't matter whether or not that switch is a couple hundred ohms. It would still work and it wouldn't confuse

**Dave Jones:** it with other buttons on there, but that's not how they implement that. So, they've implemented obviously using some sort of resistor divider thing. I don't know. We could like reverse engineer this. If anyone actually does have a reverse engineered or a schematic for

**Dave Jones:** this thing, please leave it in the comments down below. But yeah, obviously it is what Steven said in the comments. They're obviously trying to do some sort of resistor dividery type keypad arrangement. I you know, I'm trying to read that values. That's a

**Dave Jones:** dicky design decision that can come back to bite me. Basically, it's been bugging me for years. I can't believe I put up with it. Um, think I did actually try to take the thing off the wall before and I just couldn't get

**Dave Jones:** the damn thing off. So, I go, "Ah, bugger it, you know?" And so, I finally It took a lot of effort to get that off the wall, but yeah, it was like somehow painted on. It's been on there for like

**Dave Jones:** 15 years. It's never been taken off ever since uh this building was built probably, you know, 17, 18 years or something like that. And yeah, that switch finally come a guts uh and was causing it to like put it into heating

**Dave Jones:** and cooling mode and doing all sorts of these weird modes. Like you'd come up with all these convoluted theories. Oh, like if I hold it on for a bit longer, if I press it twice in a row quickly,

**Dave Jones:** it'll do this and that. But, no, it was just There was no method. And sometimes you might think, "Oh, it might repeat it a couple of times." So, you might think you found something and something else is playing

**Dave Jones:** up with it. No, it was just a dodgy switch contact with a a dodgy-ass implementation of a keypad matrix uh you know, or a keypad um input design, sensor design, and that was just causing different modes. That's it. That was a

**Dave Jones:** real interesting repair. So, I'm going to call that a repair video. Actually, it was going to be like a maybe a reverse engineering video. But anyway, if you've got details about that command system, yeah, please leave it in

**Dave Jones:** the comments down below. You got any other info, please let me know. Anyway, hope you found that interesting. If you did, please give it a big well, a thumb. There it is. Foreground thumb cuz I'm zoomed in a lot. Give it a big a thumbs

**Dave Jones:** up. And as always, you can discuss in the comments down below, EV blog forum, alternative platforms, all that sort of stuff. You know the drill. Ring the subscribe bell and all that YouTuber stuff we say. Hope you liked it. Catch you next time.

**Dave Jones:** Mhm.
