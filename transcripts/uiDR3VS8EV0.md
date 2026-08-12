---
video_id: uiDR3VS8EV0
title: EEVblog 1520 - Troubleshooting a Faulty BM786 Multimeter
url: https://www.youtube.com/watch?v=uiDR3VS8EV0
source: youtube-asr
---

**Dave Jones:** Hi, it's multimeter repair time or at least evaluating a returned BM um 786. They don't fail that often. Still got the uh protective I don't know if they're using it with the uh protective uh film on it or they just had it in the

**Dave Jones:** box and they put it back. Hands up if you do that or hands up if you leave it in the comments if you actually use your film especially when it's like daggy like that and it's really obvious. I've

**Dave Jones:** used stuff for you know, donkeys years with the with the film still on it if it's like completely not obvious. Sometimes I've like used uh products and I go like I realized like 5 years later, oh there's a film there.

**Dave Jones:** Yeah, flapping around in the breeze there. Yes, the the Brymen meters do fail. Um there's not a 0% failure rate. I'm not actually keeping figures on this. I wish I did. Occasionally like I'll have to send out a new meter or

**Dave Jones:** whatever. I don't bother like I don't offer a repair service. I thought I'd have a look at this one uh because yeah, it like it doesn't turn on. Apparently, they showed me it's not the batteries. It's pressure on the battery pack?

**Dave Jones:** No. Okay, um let's crack her open and see what's what. And of course the 786 uses quite unusual uh battery pack. Pull that like the three the vertical three AAA's like that. That one's that one's sitting out a bit. But that

**Dave Jones:** looks good. So it it connects with one tab thing down there. So we've got a gold uh flash pad down there and a spring contact and that contacts that metal tab there. So the spring contacts that and then there's

**Dave Jones:** that little tab over there. So that tab's there. That should work. The spring's in place. Let me um let me measure the voltage here. Well again, 4.4 volts. That should work. I'm not seeing anything out of place there. You

**Dave Jones:** can see that mark on the PCB there where that that has made contact. So that's obviously touching. Something's failed in inside. And it's written there, nominal 4.5 volt battery. Negative on the pad. And we're getting positive. Okay, so the pad is the negative one.

**Dave Jones:** Oh, yeah, I can see that going down there. Yep. That spring, which is actually soldered to the PCB, it's not a uh it's not just flapping around in the breeze, sitting in that little holder there. So, I can uh hook a

**Dave Jones:** power supply onto that. Hang on. This is right up under the bench. Better make sure I've got it right. And they use a black terminal. I can't show you this. So, I've got this National Instruments Virtual Bench uses a black terminal for

**Dave Jones:** the positive. Uses all black terminals. It's only like the ring around the back. You can't actually see it. You got to uh it's just Anyway. So, we should be able to see like a couple of milliamps, whatever the draw is, if this actually

**Dave Jones:** works. Oh, no, no, it's current limit. Current limit. What? It's dropping to 0.8. Something's going on there. Oh. Yeah, I had it backwards. Oh. All right, that's embarrassing. So, that's the reverse protection diode there kicking in. All right, it's

**Dave Jones:** positive on the pad and negative on there. Here we go. Uh nothing. Can we see that LCD? No. No LCD. Well, it's dead, Jim. Not seeing anything obvious. You wouldn't expect to to take out the screen, I think, to get to processor.

**Dave Jones:** But the problem is, you take out the screen, you can't see if the thing's on or not. So, you know, you have to rely on the current draw. So, anyway, could it be a bad contact, like range switch

**Dave Jones:** contact? Because that's where the actual switch is in this thing to switch it on. Even though they they trust me to have the firmware and the firmware reprogramming tool, which they won't give to anyone else, but they won't

**Dave Jones:** trust me with the schematic. So, I don't know. Don't get it. Cuz, you know, like, what if I did want to have offer a repair service? You know? I mean, jeez, I'd like to you know, it's like the for

**Dave Jones:** something like this, just doing a video, you know, I've signed an NDA with them. I wouldn't actually release it. There's our There's the bottom. BTC is uh Brymen. That's Brymen branded. So, yeah, where's the um protection? I can't

**Dave Jones:** remember. Going to have to look at my own teardown photos. So, I do have teardown photos of this. There's no protection diode up there. Not on this side. And but solder wise, everything's looking good around there. No luckers. Be easy if I had a

**Dave Jones:** schematic. Anyway, like next um thing would be, I guess, remove the range switch. And because the range switch is, you know, you go for a mechanical fault. Anytime you've got a mechanical versus electrical, always go for the mechanical

**Dave Jones:** first. Don't assume it's electronicy. And flip. It's the mechanism. It's got a little bit of grease in there. It goes around there like that. Now, I've got to get it back in its original position. But anyway, contacts, they

**Dave Jones:** look good. Not seeing a problem there. They look the correct height. They're not worn. They're not pushed in. They haven't fallen out. So, contacts are good. But no, on a multimeter, on something like this that has a mechanical

**Dave Jones:** power thing, you definitely want to suspect that. But that's shiny as a C3PO. Look at that. So, the next would be You can see the switch wear down here. But that looks good. So, yeah, they've got labels around here. So, which one's

**Dave Jones:** actually the power switch? It's usually one that goes like right around. Okay, so I'm going to buzz this sucker out. 0.4 ohms. There you go. That is low. Jab it right up there. Right up the clacker. And see

**Dave Jones:** if we can get the positive. 0.3. There you go. So, that outer one is your positive. And that inner one, that's your negative. Okay. So, it's getting through to the contacts. There's no contam- Like you'd look for contamination on there as well. Like,

**Dave Jones:** you know, if it's customer return one, like you wouldn't rule out like say there's spilled something on it or something like that, but there's nothing nothing that's obvious. Quite happy with the looks of that. Few little normal wear marks from the range switch, but

**Dave Jones:** not a problem. I've I've had that before. People have returned not multimeters, but I've had people return stuff and uh yeah, and they've um they've fiddled with it. Oh, I didn't fiddle with it. But uh yeah, they have. So, I can't see

**Dave Jones:** any reason to suspect the range switch is at fault there. So, I guess now um I need to put it back together, feed in a voltage, and then make sure it's getting to the processor. Because, you know, like the processor could be active, it

**Dave Jones:** could be drawing nothing at all, but you know, it could be getting there and not I don't know the processor could be dead, the LCD driver could be dead. Anyway, I am going to rule out the range switch. That one there is the positive,

**Dave Jones:** did we say? And that inner one and then the second inner ring is the negative. Switch it doesn't look like to be switching any of the negative there. Cuz the negative I think this is the off position. I don't

**Dave Jones:** know, you know, how that actually lines up precisely. You can see the labels down here off AC volts. If you try and decode these things, it's not going to be switching the negative, it's going to be switching the positive. You know,

**Dave Jones:** like this we measured as the positive input. So, it's switching it through to this one. So, the contacts on the back of the switch, that one there is is doing the encode and the encode and like the switching between this and this. So,

**Dave Jones:** this ground here is doing the sensing to tell the processor which switch position it's actually in. So, that's what the negative is doing. So, obviously it's, you know, it's pulled high uh probably inside the micro and it's just it's so

**Dave Jones:** that's how it reads the switch position. But the next the next two rings, these two, uh well, at least this side of it. You can do other decoding on the other side, and that's why they have different ones on opposite sides like this, okay?

**Dave Jones:** So, they do decoding and you know, they do sweep power switching and decoding. Anyway, there's a gap in there. So in the off position, well, it's off. It's disconnecting the power, but as soon as you move it from here to the next

**Dave Jones:** position, which is the AC volts, boom, it joins the two of these like that. And you can see that it's got a little break in there. That's actually a break before make. So they're doing something They're doing some break before make thing in there.

**Dave Jones:** So I don't know why. Was that doing a power on reset? Is that a power on reset? Is that why they've got the make before break? Don't know. So if I had the schematic, be able to tell you. And

**Dave Jones:** uh then we're going to have to measure the voltage on the processor side. All right, so I don't have the resolution on the uh power supply here. I've only got the 1 milliamp, but occasionally it does flicker to one. So

**Dave Jones:** I've put the current meter, which is isolated from this thing, in series. So let's see if this works. Let's go to 100 milliamp range. Yeah, there you go. 0.68 milliamps. So there's something there, but I'm pretty sure that's not the

**Dave Jones:** operational That is not the operational current. Okay, so I've got it in the case, and I think I've switched it to off. Yeah, there you go. Really need a sharp probe here instead of this banana plug. It's all right, I got

**Dave Jones:** a current limit there. I've got a nice 30 milliamp current limit, as you can see up there on the power supply. So I mean, I can use this as a probe to point to. First time I realized that. Okay, so it's off.

**Dave Jones:** And switch it on. Yeah, there you go. 0.68. Uh is it getting to the processor? I don't know. That is the multimeter chipset. That's not the um processor. The processor's on the other side of this thing. So Now, of course, if I was

**Dave Jones:** getting serious onto this, I would like solder a uh little uh wire onto there. Well, onto here. You don't want to contaminate that pad, um cuz that will uh ruin your when the press fit, um, you know, contact spring

**Dave Jones:** contact comes down on there like that. But, I'm too lazy for that, and I'm a glutton for punishment, so I'm just going to keep going, damn it. Now, the good thing is is that I do have my power

**Dave Jones:** supply hooked up, so and it's hooked up to the body meter as well, so it's the common, so it's already there as the, uh, common. So, I could actually, you know, probe around stuff like this. Let's probe a cap there. There you go.

**Dave Jones:** Yeah, 670. Okay. Well, 1.84 volts. 1.8 sounds like a voltage that you'd have. Once again, I don't don't have the schematic, so, you know. So, yeah, like we're getting something there. What's this one over here? Again, this is where

**Dave Jones:** the schematic would come in handy. That could be part of the like the true RMS, uh, thing or something, but, yeah, there's not much doing over here. All the processor goodness is on the bottom side, and it's under

**Dave Jones:** the LCD. Clearly, we've, uh, we're out of the realm of a like a simple problem, like a contact problem, uh, with the battery pack, a range switch, uh, problem. It's obviously there's power getting, um, to the circuitry. Uh, there is

**Dave Jones:** actually a slight history of Brymen, uh, processors actually just going tits up, um, like over a long period of time. Although, I think this is a fairly recent order. I think it's like only a year or less than a year old or

**Dave Jones:** something like that. But, in the, uh, 235, which I've been selling for a long time, like 7 or 8 years now, I think, a few of those have actually just, you know, it's just failed. The the main chip has,

**Dave Jones:** uh, failed. And so, yeah, we're not sure, you know, is it silicon rot in the die or something like that. I'm not sure what the, uh, deal is there, but, um, yeah, so, you know, maybe something's died in there,

**Dave Jones:** but, yeah, I mean, could be like the, uh, LCD driver chip. Yeah, we're we're getting into serious troubleshooting territory now. All right, so, I soldered a wire on. I've removed the, uh, LCD as well. Uh so, now we can access the other

**Dave Jones:** side of the board. So, just checking here. So, we can get this uh that's 4.5 V coming in. And our current is auto ranges back. That's annoying. Every time. There you go. 0.678 mA. Fortunately, you've got to be careful

**Dave Jones:** cuz it will time out. You remember auto multimeter has auto turn off. So, maybe we should feed a continuous uh voltage in, make it do something. I was going to say that you could actually uh put it to

**Dave Jones:** ohms mode, for example, put the probes in, and see if it then go to continuity mode, and see if it can go through, and uh even though you don't know what mode you're in, go through and see if it

**Dave Jones:** buzzes. But, uh yeah, 0.68 0.6 mA is not right. So, anyway, we can now flip that over. I probably should have put I'm just going to ruin that spring, aren't I? So, yeah, this goes over to the uh keypad, that one and that there.

**Dave Jones:** Seems something like the ground spring here, which goes to the It's not the battery negative. It's actually the uh guard ground of the circuit, which goes the that spring goes to the uh shielding in the back of the case. That you don't

**Dave Jones:** expect that to be ground. So, that's at some voltage there. Um I don't know whether or not that's correct. Once again, don't have a schematic, so don't know. But, I do know it's not zero. So, that's good. So, that you know, there's there's

**Dave Jones:** voltage going on in here. So, it's scope time now. Unfortunately, um I don't have this machine set up to view the scope like showing both at once. I haven't got my ATM set up for that. All right. So,

**Dave Jones:** I'll just probe the rail there uh the battery. There you go. 4.5. Okay. Well, let's see if we've got any oscillation on our clock, shall we? Oh, there's your problem. Uh yeah. No clock. Using times 10 probe, so we're

**Dave Jones:** not loading that down too much. But, yeah. Um oh, what's Oh, no. I thought that was a little blow hole there for a second. No. So, yeah, we're getting no no clock on our processor. So, that's a problem.

**Dave Jones:** Just occurred to me, what I could actually do is hook this up to the uh programmer and see if the like and power it through the programmer. Is that a short? Is that a short on a pin? No, it looks

**Dave Jones:** like a bit of plastic or No, that's a that's No, that's a bit of fluxy. That's not going to stop the processor working though. Okay, what I'm going to do is probe these caps here. So, if I probe those,

**Dave Jones:** you can see that there's not much happening there either side of those caps. Right, we're getting something little there. I expect that to be bulk decoupling for the chip here. I mean, you know, this this looks for all the

**Dave Jones:** world like, you know, power input pins, right? So, it seems like the processor is not getting It's not getting voltage. We've got a regulator over here. Is that it? Let me probe Ah, there. Okay, that's 4 and 1/2.

**Dave Jones:** You can't see that, but that is uh the 4 and 1/2 volts. Okay, so the 4 and 1/2 volts going in and it'll be the output. Ah, I can You can't see that. There you go. Um yeah, that's uh the 3.3. So,

**Dave Jones:** we're getting our 3.3 volts there. Is there anything like 3.3 volts happening on the micro? There doesn't seem to be. So, why? The switch position is on. Um well, we know that because it switches it through to the regulator. See, here's

**Dave Jones:** where it'd be like super handy to have the schematic. Just saying, Brian. Anyway, we are on the right track. I think I'm going to solder a wire in there. I don't like that. Turns out that's actually a 3.5

**Dave Jones:** volt rail. There you go. But it doesn't seem like any of that is getting to the processor. I know there are different grounds in here for like the analog subsystem and things, but the but the actual processor um should just be a

**Dave Jones:** regular 3.3 volt or whatever, 3.5 in this case maybe uh processor. It should be sharing that ground. Like even if I use another multimeter, which you can't see here, cap there, like, I'm getting I'm getting 0.13 V. No, no, no, no, no. That's wrong. Now,

**Dave Jones:** this is interesting. On the other side here, we've got two transistors, Q19 and Q18, and here's our 3.3 3.5 V, okay? It ain't coming out. So, it's got a 10K pull-up unless there's a No, there's no no via jumping down to the other side.

**Dave Jones:** It goes through 10K resistor. What is that doing? Um it's just power Like, and it's a big fat trace, too, as if like it's a power trace rather than a signal trace, but it goes nowhere um except through this 10K

**Dave Jones:** resistor. Yeah, power switching going to the processor. Look, that's uh I've had a little little rework there. That is not a reflow. Somebody used some excess solder there. I assume that's from the factory, and the uh the customer hasn't uh

**Dave Jones:** done that, but you never know. But yeah, now we're getting into some interesting electronics debugging, at least. All right, so I hooked up the uh programmer to this thing. I actually programmed a good uh unit with the latest uh firmware

**Dave Jones:** to make sure everything was working fine. Then I plugged it into this one, and it doesn't work. So, the processor under here um this is it's just not detecting it. Uh the programmer doesn't detect it. And this thing you program in

**Dave Jones:** the off the switch off position. So, it actually uh supplies external power to here, so it bypasses any other switching that's um happening. So, yeah, if it can't read the processor, then yeah, something's wrong. But that doesn't explain why we're getting no voltage to

**Dave Jones:** the processor on uh when we switch this thing on. Since even if the processor was dead somehow, you know, the silicon just doesn't work, um then it will you'd at least get voltage to it. Found something that can

**Dave Jones:** actually uh switch this. Let's probe it here like this and if I switch on you can see that it switches through to there. So, yeah, it's actually um the the the big cap there. It's going to slowly discharge. Yeah, so that it it's doing

**Dave Jones:** the business, right? So, why does that power not get through to to the main processor seemingly? Um going to have to trace the trace. Yeah, so the output of that regulator, it drops through here. It doesn't go anywhere

**Dave Jones:** else and then through a zero resistor to here, right? So, that's it. That looks like that's the extent of the path. Hang on, we are getting our 3 and 1/2 volts there. Okay, so that's going through to here.

**Dave Jones:** So, what I thought was a Well, this could be like a star ground, okay? Because you don't know like because the voltage rails inside these multimeters are they're not floating's not the correct term, but they're shifted and they're, you know, they're

**Dave Jones:** all over the shop. So, unless we had the schematic, um hard to see, but basically that transistor's fine, right? So, we have the power coming in here. Where it goes through a zero ohm resistor, it goes into this transistor

**Dave Jones:** and it comes out this transistor here. So, that's fine, right? So, we're getting 3 and 1/2 volts going over here powering everything that that goes over to here. No, see that that must be a different ground, okay? So, that's why we're

**Dave Jones:** cuz I'm using the common ground at the moment. I'm not using two probes to probe a differential. Hang on, that's just switched off. So, I what what happened there? Okay, switch on. 4 and 1/2 volts goes through over to

**Dave Jones:** here, 3 and 1/2 volts out of the regulator, okay? It drops down, there's a whole bunch of vias there. It drops down here. Over to here and then switches through. Oh, no. Now, it doesn't. It did before. You saw it. What the What's wrong with

**Dave Jones:** that little sucker down there? Soldering wise, it looks fine. Oh. I swear I'm not going nuts, right? Wish I could replay the video right here in front of me. I'm sure that was switching it through. You saw that

**Dave Jones:** before. Okay, well, this is starting to get very silly. This is where I have to start like almost reverse engineering and looking up part numbers and stuff like that. So, what I've done is I've actually hooked this up to the

**Dave Jones:** programmer here and I can't show you that for confidential other reasons, but it doesn't detect the chip. So, the interesting thing about this is that you program it in off mode. So, it actually bypasses all the power. It supplies

**Dave Jones:** power through the connection interface here, which is this little pin header over here. It doesn't detect the chip. So, even bypassing this regulator here, which we've determined switches on in when you actually switch the meter on, it switches that, but it also because

**Dave Jones:** multimeters have power off functionality, that's clearly what I believe that's what these transistors down here are doing. This is the auto off functionality. So, this is like a processor latch thing. Now, we've seen that it when we did have it actually latch power

**Dave Jones:** on the output here, but then it didn't later on. So, I I don't know what's going on there. Maybe I don't know. Processors half booting up and latching on and then dying. I I got no idea, but obviously

**Dave Jones:** the programmer is not being detected. So, there's something wrong with at least when you bypass it like everything else taken out of the equation from the multimeter circuit, this thing is not being detected when you plug into the

**Dave Jones:** programmer header. There's just no the chasing a red herring down a rabbit hole there. Um if we can't get this thing to detect when we at least plug it in here. So, could be the micro dead, could be

**Dave Jones:** some other part of the circuit that's being used by this external power thing. So, what I'm going to do now is I'm going to plug in the external power here and I'm going to work from there to see

**Dave Jones:** if we actually get power on this chip cuz I think these two have to be the power pin. Now, here's another interesting thing. I supposedly know the exact type of this microcontroller. I downloaded the PDF data sheet for it.

**Dave Jones:** It's not available in a 48-pin LQFP here. Um it's just not it it's just not available. Now, they do have a lesser range in a 48 uh like a slightly different variant in a 48-pin uh job, but the pin house don't match at

**Dave Jones:** all. So, and of course, look, like we've got a decoupling cap here. Like huge big vias. Like this is ground, okay? Like this is power, okay? And like a huge tans here, right? This has to These two have to be the power pin. And it doesn't

**Dave Jones:** match the data sheet at all. So, I think they've got some custom pin variant of that. The manufacturer's made it for them, which they'll do if you've, you know, significant enough customer. No worries. What I've done is just put a

**Dave Jones:** text to mark there so I know exactly where the off uh position is. I'm not going to get confused. So, that is definitely off. I can tell you that negative is over this side over here. 131 mV. That's what we're getting

**Dave Jones:** before, right? That is not working. That is not like that's got to be a power rail, right? And look at this pin over here, right? That is going through an inductor. Like that's got to be like a power rail. Doesn't matter if we get the

**Dave Jones:** probes around the other way, right? Probe between there and there, there and there. Like, you know, like something's got Got be a power rail in here somewhere. Right? even if you just you have no clue, you just randomly probe around at large

**Dave Jones:** traces with decoupling caps and large number of vias and stuff, right? There's just There's There's nothing. And I think the second one here Well, the second one here is red. There you go, 3.2 volts. So, we're getting our voltage

**Dave Jones:** in there. But once again, this is over this part of the circuit. So, is it It's nowhere near that power up thing. So, I don't know. We We just It's not getting through. There could be like a diode

**Dave Jones:** orient thing or something that activates that uh power on latching circuit and bypasses that somehow. There could be something tricky going on there. Um and it's just not getting through. So, you know, I wouldn't rule out that uh

**Dave Jones:** transistor pair that we've got there. That might be a cause in an issue in both the regular power on function via the switch and also via the external programmer as well. That'd be just my luck, wouldn't it? Bloody Murphy. Right, so what I can say

**Dave Jones:** now is that the micro You know, you can't say the micro is just Oh, the micro is faulty. Let's just replace the micro. You can't do that. There's no voltage going to it. So, of course it's not going to do anything. Course we're

**Dave Jones:** not going to get a clock like we couldn't measure before. Now, I've got to decide whether or not it's better to uh trace the power here via the range switch or and the battery or via the external programming header here. I

**Dave Jones:** don't know. I'm tempted to think the programming header, but Murphy will ensure whichever way I pick, it's going to make it harder. But ultimately, I think either way is going to lead to the same fault. Now, it's not like the uh

**Dave Jones:** processor or some other part like a shorted cap or something like that is shorting down the rail cuz we're measuring 3.2 volts on that rail, which If that 3.2 volts is not getting to the processor in any way, then we need to

**Dave Jones:** know why. Um that That is what we need to fix here. So, let's start off by doing a sanity check of what what I know as the system. Well, in the initial system ground over here and the ground

**Dave Jones:** over on the thing, yep, it's the same ground. So, let's go from here and find out which pins is this one over here. Once again, that's also ground. That's what I suspected, right? It's the negative of the cap there. It's right.

**Dave Jones:** Everything's hunky-dory. Don't know why that cap's missing over there, right? But all this all this stuff here, right? This is ground. This is definitely the ground pin. This looks like a power pin cuz it's coming through an inductor. You

**Dave Jones:** usually would have the inductors in the positive rail. So, we've definitely got our correct ground pin, but we're getting nothing coming from over here. And of course, this is our 3.2 V power pin, right? We're getting nothing. So,

**Dave Jones:** obviously, you know, we're not going to have like a PCB break or something like that. That's like the most It's It's not impossible, but it's the most unlikely scenario, right? So, I'd say that yeah, there's some sort of um power

**Dave Jones:** latching switching circuit. And I don't think that the battery input is going to be connected to here. No, and it's not. So, what we can safely do now, I think, is plug in because I You don't want to

**Dave Jones:** be probing with two probes. So, I'm going to plug in the ground and I'm going to reconnect the ground over to here so that I am hooked on. So, now I can just probe with a single probe and go around

**Dave Jones:** because, you know, it's it's going to be a common ground for the processor. If you're trying to debug the multimeter chip, which is the one on the other side, that's when all bets are off. That's when all the grounds are

**Dave Jones:** different and everything else, right? And you're going to come a gutser if you're trying to do that. But this is just the processor, right? The ground is connected through to the battery and through to there and through to the

**Dave Jones:** processor. No worries. But the analog circuitry, just be aware, very different scenario. Okay, so let's check again. We have 3.3 volts. Was that 3.2 before? Anyway, we had Yeah, 3.3 volts coming in. Right, so where is that pin going?

**Dave Jones:** I'm going to have to flip it over. Actually, I will trace this There we go. There we go. It's that fatty It's that fatty running off there. It's running to that resistor there, is it? Is that a zero ohm resistor? It is a zero ohm

**Dave Jones:** resistor, so it's a jumper. Okay. So, yeah, we've got this fatty trace going off here off here. It's going down here. Okay. Hello. There we go. 4.5 volt bat, but it's not connected through to the battery, which is 2.2.

**Dave Jones:** That's interesting. Okay. So, it comes over to here. Boop boop boop boop boop and it jumps up. Uh is it Is it that via there? Yeah, there it is. Okay. So, it's jumping up over there. Okay. So, we've

**Dave Jones:** got two inputs here. Aha. This is now starting to make sense from a physical layout point of view. Here's our battery input here, okay? And here is our input for our uh external programmer, right? So, we've got both and we can see that

**Dave Jones:** buggering off on the other side there. Flippity do da. What was it? This one here. Uh it's going on an internal layer. Bugger it. But yeah, it's around here. There's something. I reckon there's something in that power latching circuit. There's got

**Dave Jones:** to be. That's the only thing that making that makes sense. Aha. Once again, there it is. Our 3.3 volt going into there, right? And it's not And it's not coming out. Exactly the same thing is going on here. Exactly the same thing. You

**Dave Jones:** remember how it switched through before? So, from there to there, that's how it was uh switching and this is just the uh base {slash} gate here. Maybe it's that puppy. I think this is part of the latching circuit, but I think this is

**Dave Jones:** the main one that switches the power through to here. So, I'm suspecting that little bad boy, Q18. So, we need a need a partner we need a definitive part number on that. Yeah, there you go. You get that. That

**Dave Jones:** is B0329. Okay, so this is some form of soft latch power circuit. Where have we seen this before? Uh check it out here in my uh extremely popular uh soft latch power circuit video. We have a uh P-channel MOSFET

**Dave Jones:** with an uh N-channel bipolar pulling uh the gate down to ground. And uh you can have a third transistor over there do the latching function and stuff like that. But anyway, um in that particular case we'd have like

**Dave Jones:** the micro like doing that. Yeah, this is the exact same arrangement here. Now, I couldn't find any info on this B0329, but I think that is a P-channel MOSFET cuz it matches the pinout for a P-channel MOSFET. So, we've got a

**Dave Jones:** voltage coming in here to the source, and then we've got the uh pull-up resistor, which goes through two of these like that. And then we've got this would be an N an N-channel bipolar transistor, and that is just going to

**Dave Jones:** pull that down to ground. So, and which is our ground is here. Yep, it does. So, there you go. So, that is ground. So, it's just simply latching that uh down to ground. No worries. I'm suspecting that cuz the bipolar transistors are

**Dave Jones:** more rugged than MOSFETs. If If you're going to have a transistor fail out of these two, your money should be on the MOSFET. Which in so I'm just going to go to my MOSFET kit, find a P-channel MOSFET, and I'm just going to replace

**Dave Jones:** that. Cuz it takes 2 seconds. Wiggle wiggle wiggle, yeah. Come on. You can do it. Go onski. Okay, what I've got is a uh BSS84. It's a small signal uh P-channel MOSFET. Should do the business. Got our 3.3

**Dave Jones:** volts coming in here. Do we get our 3.3? No. We've come a cropper. That ain't it, folks. What what what what. You see now a problem here is that that transistor, of course, it's not going to switch on

**Dave Jones:** because that like that is not grounded. So, I should have actually checked that before. Maybe I was wrong. Maybe the N-channel Now, the interesting thing is if this was an NPN a functional NPN bipolar, we should be able to measure

**Dave Jones:** the diode drop on the gate there, the base emitter. Cuz this is the emitter, this is the base, and we ain't measuring anything there. That's either not a a bipolar transistor or it's um buggered. So, that's an A603G,

**Dave Jones:** and I can't find, once again, can't find any information on 0603G. Now, what I've done is I've um compared to another unit because I have one. Sure enough, there's no NPN uh junction in there. So, this is not a

**Dave Jones:** bipolar. I think this is a MOSFET. Get the multimeter back out. So, what we expect is actually I've got the external power plugged in. We expect a positive signal on there, and I've compared that with a good unit, and yeah, we get 3.3 V

**Dave Jones:** there. So, the micros obviously like you know, doing that and switching that on. So, it but it's not doing that. So, I don't know. That's going to be hard driven, so we can't just short it out cuz then we'd be shorting out the output

**Dave Jones:** uh gate, but we could actually remove that resistor there and actually um you know, connect that to the input, and that would latch on the circuit. Or, of course, you know, we could just bypass the main uh switching MOSFET here, um

**Dave Jones:** switching that through. But, yeah, um I've I've confirmed on a good unit that that's what that does. You get a N-channel uh jobbie here, which then latches and pulls on the P channel here and switches the power through to here. And I've I've

**Dave Jones:** confirmed that. So, that's that's definitely what's going on. So, it could still be a dead micro. The boot code in the micro is like putting that high somehow. So, you'd have to follow the money there. But once again, we could

**Dave Jones:** have saved 3/4 of our time here if we had actually had the schematic. Okay, at this point I'm done screwing around with this thing. I'm going to short out the power transistor here. And so, I remove that one I put in. I'm

**Dave Jones:** just going to short there to there, and that will permanently switch on the power to this thing, and we'll see if the damn thing works. Just going to measure the voltage here. No, see we're still getting nothing out

**Dave Jones:** of there. So, it's not latching that on. Let me try my uh see if I can connect to the chip on my programmer here. Chip ID from IC. No, it's got no. I'm getting nothing. Measure the voltage between

**Dave Jones:** there and there. And that should be our 3.3 V. There it is. See if we get that over here. 1.77. Let me compare a good unit. Okay, so here is a good unit in uh programming mode. You can see it's got the dashes

**Dave Jones:** across here. It's switched the micro on. Uh it's in off position, but we're powering it through here. And 3.3. No, 1.6. Here to there is 3.3. Back to the bad board here. 3.25. Okay, right. So, we've got the same conditions. So, the

**Dave Jones:** chip Let's just assume that's getting through to there. Right? So, the chip is being powered. Okay? And we're getting nothing on the programmer. Um so, whereas the programmer tells me the chip ID, and it it works on the good

**Dave Jones:** board and doesn't work on this one. So, the only other reason I can think of that this micro is uh not working apart from it failing is we go back to the mechanical side of things and a crystal.

**Dave Jones:** Um there. It was there. I decided to remove the uh crystal cuz fuzz in uh crystals are a thing. So, they're a mechanical uh part. And unfortunately, I lifted the pad. This is a real dog to get off. I could not get this off

**Dave Jones:** properly with either hot air or with uh dual soldering irons. It just lifted the whole pad off. So, unfortunately, um yeah, that's a bit of a fail. You can see the caps are on the uh bottom here, and you can see they they that they've

**Dave Jones:** got a uh 10 meg resistor across there. So, unfortunately, that's I'm going to have to wire a mod wire into there around to there. The uh 121 GW actually has the same, except it's uh through hole. And one of them is 4.9152.

**Dave Jones:** I can just budge that in just to try it. And uh yeah, she'll be right. There we go. And you got to ask yourself, do you feel lucky? Well, do you, punk? Those two holes there. Oh, no. Then um I might be able to

**Dave Jones:** solder the crystal down to those two vias, but whatever. I got the right gauge wire. Yes, I do. Look at that. Oh, beauty.

**Dave Jones:** All right, we'll just push that out of the way. I can just solder the crystal onto what's remaining of the of that pad and that one.

**Dave Jones:** All right, we have a crystal budged in there. Um I don't know what pad that's Well, it's not even touching that pad, I don't think, or it might be slightly. But that's just the case if it's ground. Hey, if not, eh, probably doesn't

**Dave Jones:** matter. It'll oscillate. Plug our programming header back in. Nope, still not reading the ID. Still not reading the chip ID. Oh, so much for that. That was worth a try. It's oscillator-in. Maybe there was nothing wrong with that

**Dave Jones:** crystal at all. And yeah, the reason it wasn't oscillating before is cuz it wasn't getting power. Damn. I should have actually um uh re-checked the oscillator when we discovered that there was no power to the chip. I should have

**Dave Jones:** re-checked it after after we forced the power on. Yeah, I just butchered that board for no reason. Let that be a lesson to you. Oops. So, yeah, I had no trouble like I thought it'd be easy to get that crystal out, but it it wasn't.

**Dave Jones:** The adhesive on the bottom of the page just gave away and boom, once that happens, you know, it's like you can repair stuff like that. You could get some like adhesive copper and I could actually repair that pad perhaps

**Dave Jones:** and you know, it's a loss to do a proper repair on this. That's what I'd So, yeah, you can see there that is oscillating just fine and dandy. It's not talking to the programmer. So, I can only presume, yeah, the chip is dead.

**Dave Jones:** The internal oscillator is working, but something else has died. That's the only conclusion I can come to now. Please leave your thoughts and comments down below. I'm going to leave it at that. Sorry, you know, I know a lot of people

**Dave Jones:** don't like like the unhappy ending, but there are a lot of people who think the journey is what matters and this has a quite a decent little journey we went on here. This sort of stuff doesn't take me

**Dave Jones:** long, by the way, if I'm not shooting a video. It doesn't take me this long. I'm not yapping on. I don't have a spare chip. I could, you know, even if I like I would have to rip one off another board and I

**Dave Jones:** don't have a junk 786. I could get one from Brymen, but then even if I did, that would prove that it was the chip, but then it would lose its calibration values cuz I don't believe there's an external e-square prom in

**Dave Jones:** here. I think it's all internal. It's in the protected mode of the chip, the calibration values. So, you can update the firmware and you don't reset the calibration values, but if you physically change the chip, yeah, you're going to lose some of the calibration

**Dave Jones:** values. It might still be basically, you know, it might still be within spec, but it's not going to be tweaked. I think we come down to the micro, but if you've got a better guess, I could go and trace the signals for the

**Dave Jones:** programmer and stuff like that, but I jeez, now we're getting fancy pantsy. I don't even know the pin out. Anyway, I'm going to leave that as a part one. So, if you enjoyed that troubleshooting journey, give it a big thumbs up and as

**Dave Jones:** always uh discuss it down below and over on the EVblog forum. And uh thank you to all my patrons as well. I uh put the videos up first on uh the patron account. Um in fact, I put this one up

**Dave Jones:** as a partial one last night, like a 30-minute edit um original edit. Never intended to repair it. I just thought, you know, I went I just started down the rabbit hole. Thought it might be interesting and easy to see why it

**Dave Jones:** failed. And I think, yeah, I think the micro has just died and then it doesn't latch on. Yeah, we got carried away uh replacing a few parts we shouldn't have there, but that's all part of, you know, troubleshooting with hindsight. Yeah, I

**Dave Jones:** you know, I give to think few things. I'm trying to shoot a video at the same time and you know, I trying to yeah, so that might have distracted me. But yeah, I shouldn't have butchered that crystal. That was a bit mean. Anyway, you can

**Dave Jones:** also uh catch some exclusive videos which aren't on the YouTubes. Uh they're over on my Odyssey channel. And I've got a new product right inside the door there. There's a whole bunch of new products um that I'll um do an unboxing

**Dave Jones:** of that. And I will uh cuz I haven't seen it yet, I'll do an unboxing of that. I'll whack it on my Odyssey channel as an exclusive. So, check that out if you want. Anyway, catch you next time.
