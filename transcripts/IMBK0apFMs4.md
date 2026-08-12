---
video_id: IMBK0apFMs4
title: EEVblog #230 - ArduCopter ArduPilot Troubleshooting
url: https://www.youtube.com/watch?v=IMBK0apFMs4
source: youtube-asr
---

**Dave Jones:** Hi, we're at still in the old lab today. A bit of an impromptu video. Thanks Phil. Phil's behind the brother and Phil's behind the camera. He's my brother-in-law and here comes Roge. Roge, you're on the vlog, mate. Hey Roge.

**Dave Jones:** Roge is my buddy and we're building up our ArduCopter CanyonCopter which we're going to modify and fly through a canyon and it's going to be really cool. Once we actually finish it. We're hoping to get it airborne today. We're hoping

**Dave Jones:** to get it off the ground and uh and we've run into a little snag. It was working fine this morning. Our motors was spinning and everything was fine. And then we decided to and then we want to hook it up to the PC to

**Dave Jones:** you know to get the comms and calibrate it and do all that sort of stuff and not it it just would not die. All the LEDs on our Ardu Pilot Mega, that's an Ardu Pilot Mega board and that's the IMU board which

**Dave Jones:** sits on top. It's got all the sensors and stuff like that. It's a standard ArduCopter ArduCopter sensor platform and and control platform for the copter and none of the lights none of the LEDs on it would come on. Crazy. When we hooked

**Dave Jones:** it up it seemed to have just completely died. So but we've had to do some impromptu troubleshooting and what we've narrowed it down to is a complete five a short on the five volt rail on this IMU board. Go figure. So if you have a look

**Dave Jones:** at the schematic here hand it over Phil. And let's take a look at the schematic here. We've got uh five volts five volts coming in here on the USB cuz you can actually power this board up through the USB. We narrowed it

**Dave Jones:** down. We disconnected it from all of our circuitry cuz we wasn't weren't sure what was causing the problem. So five volts coming in from the USB. It goes through a poly switch here one of these resettable fuses and that was sure

**Dave Jones:** enough was getting really darn hot. So, and that's the 5-V rail. The 5-V rail goes off to uh various uh chips and devices. One of the primary ones is the um uh RS232 FTDI uh chip set, which can

**Dave Jones:** which uh which which converts the USB into the RS232, so you can talk to your Arduino uh Mega uh board, and it runs from a uh it runs from the 5-V rail. So, it's a primary device, but there's other

**Dave Jones:** devices on here. There's this um analog-to-digital converter chip here. It It also runs directly uh from 5 V, and a couple of 3.3 V uh parts up here, but uh and there's two uh 3.3 V voltage regulators on there. I'm not sure why

**Dave Jones:** they need uh two 3.3 V voltage regulators on there. I don't know, noise isolation or uh something like that. I'm not actually sure. Maybe to uh share the current between them. I got no idea, but um basically, any one of those devices

**Dave Jones:** um could be shorted out. Uh or one of the other culprits um could be uh one of the bypass caps, cuz bypass caps can also uh short out as as well. They're fairly uh notorious for that. It can happen. So, one of the

**Dave Jones:** devices on here is shorted out. Either that or we've through, you know, cutting wires and soldering stuff and everything, we could have actually got a little solder jag on there, or we could have uh got a little bit of a wire jag

**Dave Jones:** that's shorting something out, but that looks pretty clean. So, it looks like it's uh almost certainly one of the components on the board. And let's actually measure it and uh have a look. And I've shorted out my probes here. I've only got a uh Amprobe

**Dave Jones:** AM220 left. Everything else is over in the new uh lab, but uh we'll compensate for the uh probe resistance there. So, we've shorted out that. It's a little bit dodgy, but there we go. And uh if we have a look at the

**Dave Jones:** output, the rail here, and there it is. It's 0.2 0.1 ohms. It's practically a dead short. There you go. So, it's a really serious short directly on the 5-V rail. And the way you troubleshoot these is either the brute

**Dave Jones:** force method of sucking parts off until you find the culprit and your short suddenly vanishes. You can do that. It's a brute force approach. It's not bad to start with your bypass caps or something like that instead of, you know,

**Dave Jones:** desoldering like a you know, an SO package device or something like that, which is you can ruin your chip. Really annoying and you can ruin your day. Or you can get a high-res ohm meter and actually trace it

**Dave Jones:** down. And you can actually follow it through if your multimeter's got enough uh resolution, which this one doesn't. This one's only 0.1 ohms. You'd need at least a 4.5-digit meter to do that, probably a 5.5-digit. And you can actually trace

**Dave Jones:** down the short or an LCR meter or something like that that has good low-res ohm low-res ohm functionality. And you can actually trace it down on the board until you find that it gets a bit lower in that direction and you see it

**Dave Jones:** increase in another part of the board and you can narrow it down to one individual uh part. So, we're probably going to have to do that. Haven't done it yet. I've no idea. Your guess is as good as mine, but

**Dave Jones:** probably smart money might be on that F that RS232 FTDI chip because well, it's connected directly on there. Maybe maybe some ESD from the RS232 lines has shorted the rail internally or something like that. SCR latch-up. I've done a whole video on

**Dave Jones:** that. I should link in my SCR latch-up video that can easily cause the chip to short out and well, I don't know, but it could be one of the other devices, regulator or something or a bypass cap. I don't know.

**Dave Jones:** It's going to be a pain in the ass. I was hoping just to get this thing airborne and flying and jeez, impromptu troubleshooting. Well, I found a decent fluke and the wife was using it to measure the baby bath water

**Dave Jones:** temperature, go figure. So, this one didn't make it to the lab. So, I've got a 4 and 1/2 digit meter, so let's actually probe on this board and have a look. So, if you want to get in here, Rodge,

**Dave Jones:** and we will uh basically, what I'm um what I'm considering is that these are tantalums. There's a couple of tantalums and anytime you see tantalums there, um always suspect a tantalum cuz they're a real bastard, they are. Now, if we

**Dave Jones:** measure, let's say this tantalum here, these are on the 5-V rail, okay? What we're getting is there we go. Can you get the meter? Yep. Yep. 0.012 ohms, okay? I've shorted out my I've compensated for my probe resistance, so uh let's do it again.

**Dave Jones:** Okay? There we go. Okay, I've shorted out my probes and measure across that tantalum. We're getting 0.14 ohms, okay? That's not too bad. Let's measure across the FTDI chip, for example, which is that pin there, and one of these pins over here, 0.53

**Dave Jones:** ohms, okay? So, that's much higher. So, you know it's not going to be this chip if this measurement here is uh smaller in value than this one over here. So, you keep tracking around the board like this, but look at this big tantalum down

**Dave Jones:** here. He's got guilty written all over him, I reckon. So, let's probe him and bingo, 0.08 ohms, So, that's smaller than lower in value than this tantalum over here. So, it's most likely that that tantalum's the culprit. Um this schematic does show

**Dave Jones:** uh three tantalums across the 5-V rail, but these other two tantalums here, which are the only other two on the board, that I can see anyway unless I'm blind, are um obviously on the 3.3-V rail. So, my money is on that bastard tantalum there.

**Dave Jones:** So, I'm going to lift uh one end of that sucker, and I still got one iron left here. The uh two other irons but do have an iron left, so going to lift that. I think we might have a winner. Let's go.

**Dave Jones:** All right, so there we go. We've lifted that uh lifted one end of that tantalum there, and let's measure that and see what we get. Okay, here we go. Let's probe the rail. OH, NO. WHAT? OKAY. Not I uh

**Dave Jones:** called him guilty before uh finding he was innocent. So, going to have to lift another one, so let's uh get back here and hopefully it's one of the tantalums, but that that's weird. I uh could have sworn that would

**Dave Jones:** be cuz it had the lowest resistance, but maybe it's one of the devices. Who knows? Um although it was closest to that chip.

**Dave Jones:** Bang, there we go. Tantalum is lifted, and Ah, it's still shorted. Bastard. All right, well What? Fail. Um Yeah, there you go. I was hoping it would be 10 of them cuz that would have been an easy fix and if it is one of the

**Dave Jones:** chips, we could be screwed, at least for today. And I forgot to mention, sometimes a way to actually, uh, well, get rid of the short is you can actually blast the short right out. You get a really high

**Dave Jones:** current, uh, power supply, not high voltage, it's the same, uh, voltage, stick it across there and, uh, hopefully you can actually blow out, uh, the short if it's an SCR latch up in a chip or something, you can blow it open. So, at

**Dave Jones:** least, uh, that will actually get your board, uh, back operational, semi-operational again. So, not sure if that's going to be, uh, any good for us, but anyway, that's one of the methods as well for getting rid of a short. Doesn't

**Dave Jones:** help you fix it, but, uh, it might get you out of trouble anyway. Just another tip. We've got, uh, oh, we started out using, uh, cheap ass, uh, probes like this until we found some good Fluke probes. When you're doing

**Dave Jones:** stuff like this, trying to measure right down in the, uh, noise on the ohms range, really ultra sharp, professional probes, can't beat them. Don't buy the one Don't use the One Hung Low ones. They'll ruin your day. Your readings

**Dave Jones:** will fluctuate all over the place. You've got to penetrate any oxide coating on the solder joints and things like that. Really sharp probes. Trust me. All right, tracing this down, wasn't the tantalum caps. I've lifted up both of those in the 5-V rail. Bummer. So,

**Dave Jones:** I'm tracing it down here and, uh, it looks like my lowest point so far is this cap here. I find that the, um, uh, the board layout doesn't quite match, uh, precisely. There's a few, uh, minor differences, but this cap here

**Dave Jones:** seems to be my lowest value at 80 mΩ. So, and if I go If you trace that 5-V This is the 5-V rail, the, uh, brown one there. If you go up to say these pins up here, I'm measuring like 0.22 Ω, but

**Dave Jones:** this cap down here, I'm measuring 0.08 Ω. And then if you go to this cap, the big tantalum down here, which I thought was the culprit I lifted, it was like 0.11 ohms or thereabouts. So, this is my

**Dave Jones:** lowest culprit, and there's nothing else there. So, I think I'm going to suck out that bypass cap there and see what we get. Looks like we might have tracked it down. Murphy's Law again, I've sucked off a few of the tantalums, I've sucked

**Dave Jones:** off a couple of the ceramics as well. Thought I nailed it down, but turns out, check this out. Here's our lowest point I didn't check the actual I think's the magnetometer board or something. It's a little add-on board.

**Dave Jones:** Bang, the lowest resistance point is actually smack on that board. So, our short is either happening on that connector itself or more likely on that board because this board actually it's you know, it can actually short out. So, maybe during operation we

**Dave Jones:** shorted it out somehow, and it's caused a permanent short on that on that secondary daughter board there. So, I don't know. Anyway, it looks like it's either on that board or part of the connector or something like that. So,

**Dave Jones:** we'll have to suck that off. And good thing is I think it works without this. It's just an optional board you can put on. So, hopefully that won't stop us getting our copter flying today. And sometimes you're lucky. I just so happened to have a left

**Dave Jones:** out a little bit of solder wick left on the bench. It's all the rest of it's all gone to the lab, and I've got a little offcut of solder that I had left on the bench. So, sometimes you win, don't have

**Dave Jones:** to go there. So, anyway, I'm going to suck this uh thing off and uh see what's wrong with that board. Ground and VCC, I've got the board off. And it turns out I couldn't use my solder wick. I had to heat up all four pins at once

**Dave Jones:** and lift it off. Um wasn't doing that well, and should be No! No! No! You bastard! This is Ah! THE SHORT REMAINS. Are you kidding me? Look at that. That's across that tantalum that I thought was the culprit

**Dave Jones:** before. .1 ohms .09 directly across these pins here. It's See? It's It's lower. It's .04. So, the short is not up here because this is a lower value. It's got to be almost across these two pins here. Like there's

**Dave Jones:** something on the soldering down in there or something within the board itself. Often, if this is a brand new board, um the first thing you would expect and first thing would you would suspect and if you've never powered it up before,

**Dave Jones:** you would suspect that it was a board manufacturing error or an etching error and you get a little etch uh fault between, you know, two two tracks. That's uh fairly common. But, because this is a known working board that we're

**Dave Jones:** trying to uh troubleshoot here and those two pins definitely straight across there. Are you kidding me? Unbelievable. Murphy's uh killing us at every every turn here. And if we take a look at the Here's the You take a look over here on the board.

**Dave Jones:** Here's our two pins. On there, there's a GPS. It goes through there. There's Oh, maybe it's that. Maybe it's that cap there. That's what's left and it's um I don't know. Well, there's one cap I think Yeah, that looks like a cap

**Dave Jones:** there and it's uh Or maybe it's not. Maybe it's No, I think that's a pull-up resistor perhaps and there's something Well, that's it. It's got to be This is my lowest resistance point between these two pins here. So, there's

**Dave Jones:** got to be something around that area. This board, by the way, they've actually taken out all of the ground plane. So, you can't see the flood field ground plane, which goes all the way in between those pins, but got to have to probe

**Dave Jones:** some more. Oh, man. This is getting bloody painful, let me tell you. Unbelievable. Murphy gets you every time. Son of a You want to know what it is? Nothing to Murphy again. Nothing to do with the components, nothing to do with

**Dave Jones:** this magnetometer board. Won't be able to get that this ca- inside the bloody connect- And you know, it's not that uncommon, actually. And we probably should have guessed at that, cuz we were disconnecting and doing all sorts of

**Dave Jones:** things and then it stopped working. And this is the connector that we didn't even plug stuff into. It specifically has no GPS written on there. It's some sort of telemetry connector. We don't have anything on our copter that plugs

**Dave Jones:** into it. And if I can get a photo of the actual pins in here, it it shows that it's almost like something has really like a you know, like a you've got a screwdriver in there and just slammed it

**Dave Jones:** in and bent two of the damn pins in there. So, I don't know. Just freaky happened here. I don't know. Something has got in there and poked these two pins and shorted them together. Unbelievable. Man. Got to get the correct tongue angle

**Dave Jones:** here. It's important. And let this be a lesson to you. Don't start sucking out components until you're absolutely 100% sure you've traced out every path and you've nailed it. Cuz if I did, uh maybe if I had a slightly better

**Dave Jones:** meter, I could have done it. But yeah, I'm blaming my tools. All right, what can I do? But, yeah, let that be a lesson to you. Don't start desoldering components willy-nilly. All right. Pretty darn confident that it's going to light up now.

**Dave Jones:** No props attached. And let's power it from our USB. Woohoo! Hey, we have lights. It's working. There you go. It's like Christmas. Just like Christmas time. And there you go. That's a absolute textbook classic example of being led up the garden path in

**Dave Jones:** troubleshooting. We started out, found our 5-V rail was shorted, then we thought it might have been the FTDI up here. That was the first culprit. We worked our way across the board and down, then we noticed the tail of them.

**Dave Jones:** Aha, classic culprit. No, wasn't them. We narrowed our resistance down even further. It looked like that board, the IMU, sorry, the little magnetometer board. And we thought we had a classic fire mode with that magnetometer board, where it pushed down

**Dave Jones:** and shorted something out while we were mucking around with it. And it turns out that happened to be just next to the least possible thing I would have suspected, because my mind was shut off from it, was the connector that we

**Dave Jones:** weren't using. Who would have suspected a connector that we don't plug into would have shorted pins, especially when the board was working? Unbelievable. Man, that's classic Murphy 101. So, there you go. KEEP YOUR MIND A BIT MORE OPEN next

**Dave Jones:** time, but jeez, what a classic. See you. First flight test. We have no idea. We haven't even spun the motors up with props on yet. All right, first flight test. We've finally got it armed and uh Go for it, Rods. Give it a bit of

**Dave Jones:** throttle. It's pretty twisting. Yeah, it is. It's off. It's off the ground. WELL, WE GOT SOMEWHERE. OKAY, it seems to be moving to the Which way is it actually facing? Uh Yeah, which is front? The front is here.

**Dave Jones:** Front is here. So, I'm standing in front of it. So, it's moving to the left. I don't even know what mode we're in at the moment. Oh, okay. I'm pretty sure it's for that one. It's just going left though. So, it's

**Dave Jones:** unbalanced. Does that mean it's unbalanced or It is kind of unbalanced, isn't it? Yeah.

**Dave Jones:** Woo. You're getting a bit close there, Rodge. Took my feet off. All right, we're running out of gas. I don't know how we land it now.

**Dave Jones:** What? So, we can't actually switch them off even at minimum throttle? That's weird. I'll try and reach the battery, but Wait until it dies. Well, it's slowing down. Yeah.

**Dave Jones:** Not quite as loud as I thought it would be. Mhm. These seem to be going a lot faster than these. Well, we probably don't want to drain it. We probably should uh attempt to uh Oop. Oop. Okay. Some have just stopped.

**Dave Jones:** Yep. I'm in the garden. Oh, in the garden. That's going to stop us. Hang on. That one's definitely spinning funny, number one. All right.

**Dave Jones:** That's just bizarre. I mean, well, give it some more throttle, but It's a very fine line between taking off and hovering and Yeah. And it moves pretty quickly. And And then you can't just drop the throttle cuz the thing will just fall.

**Dave Jones:** Yeah. It's a good lawn, Mom. Very fine line. I've almost half half throttle. That's half.

**Dave Jones:** You can see how with some practice you could absolutely cane in this. Very touchy. I can't get over how touchy it is.

**Dave Jones:** It keeps going away from number one. Yeah. So Yeah, but it's So Well, actually, that's that was going backwards. Yeah, it's been doing it the whole time. Or unless you want to No. the battery uh Pull off? Pull off.

**Dave Jones:** It's really stable now. Hey, I know. It's excellent. Hey. It's very stable. Really hard just to get it over there.

**Dave Jones:** It just seems to want to face a particular direction. Right. Okay. Fly here. Yeah.

**Dave Jones:** Come minimum throttle. Full left and it ain't shutting down. Huh. Yeah. At least it does something now. Oh, have a fly. Might as well use our battery up. It's almost fun having it dangle down. Yeah.

**Dave Jones:** Okay. If people see this video and it's like 2 ft away from a wall there, they're going to They're going to That's not the place to test it. Oh, in that mode it's doing its own throttle control. Oh, okay. Right.

**Dave Jones:** But you can steer it. Yep. Well, I think it's trying to maintain its altitude at zero. Right.

**Dave Jones:** Woah. Nice work. All right. We really should be down the park, then we don't have to worry.

**Dave Jones:** Here we go. I think we're running out of battery, are we? Yep. We're out. just drop that stick anytime.
