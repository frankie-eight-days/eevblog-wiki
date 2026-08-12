---
video_id: V0RWwSw96Sw
title: Jackery Battery Bank FAIL - Part 2
url: https://www.youtube.com/watch?v=V0RWwSw96Sw
source: youtube-asr
---

**Dave Jones:** Hi, back with a follow-up video to this uh Jackery power bank because I didn't have enough time to look at it yesterday. So, I'm back because uh people wanted me to look at it. Got a lot of interest. So, I've taken it out

**Dave Jones:** of the uh plastic enclosure um because uh what I thought was uh probably like a low-side battery protection um device down here. Um a lot quite a lot of people were saying, "Nope, these are uh dual uh MOSFETs and

**Dave Jones:** there's got to be a control circuit somewhere um either under the inductor or underneath or something." So, I did get it out and uh yeah, it was um it was stuck in there. So, but I managed to uh

**Dave Jones:** get it all out and tada! Looks like there is. That's where the MOSFETs are. So, there is a control. So, this is the battery protection controller. So, yeah, you had to get the entire board out to actually look at this sucker. Now, what is this?

**Dave Jones:** What is this? It's a 50 K Is that 50 or is that an That's a five, not an S. That's a 50 K U. So, we can look up that little six-pin jobby. So, yeah, um so, they would certainly be uh MOSFETs. So,

**Dave Jones:** yeah, my bad. Um I just assumed that they were low-side battery protection. But, nope. So, we'll have a search for that SMD code. Uh 50 K U, I don't know. We might get lucky, we might not. But, then again, you can look for battery uh

**Dave Jones:** protection ICs, six-pin uh jobbies. So, you know, look, you don't know what's faulty, whether or not it's the uh driver or whether or not it's the MOSFETs or whatever or there's something else going to it. Um don't know. So, I'm

**Dave Jones:** not getting anything 450 K U. Like, you can go like must include 50 you or something, but I'm just not it's just it's just not there. So, what we're going to have to do is search for SOT 23 6 and battery protection. So, if

**Dave Jones:** we do that, we get you know diode ink jobbies. They're probably like a similar as I said before there's probably like a whole bunch of pin outs that equivalent pin out devices and because they're designed for the same lithium ion battery, you know,

**Dave Jones:** single cell application and the only thing that would change was like would be like the voltage difference. You know, single cell or multiple cell or something like that. So, you could argue that uh Yeah, there's LCSC. There you go. Let's

**Dave Jones:** check out that. Win sock it's going to be one of these. It's not going to be like a TI jobbie or something, right? It's going to be considering that the that the one the main controller I see that they used is one that you've never

**Dave Jones:** heard of. Yeah, it's just going to be one of these you know, Asian sourced brands protection I see for one cell lithium ion blah blah blah blah blah blah and it's a DW01. I've seen that elsewhere. So, that's the package code

**Dave Jones:** on there, but you know, like they're designed for driving external fets like that and that's looks like what Well, these ones aren't series like that. These are definitely in parallel. There's no doubt about that because you can see that these See that right right

**Dave Jones:** there. There you go. Parallel not in series. So, then we go to Mouser here, you know, lithium ion lithium polymer like you know, Nishinbo data sheet, right? I I guess you'd you'd get to know all these if you're into,

**Dave Jones:** you know, designing your lithium ion battery products and stuff like that, but yeah, I I think it might be a hard time finding out the exact device here unless somebody happens to know. If you do, leave it in the

**Dave Jones:** comments down below. Yeah, but our odds of lucking upon it, um probably not great. Murphy's Law and all. There we go. Once again, this series. So, yeah, we've we've got parallel jobbies. Definitely. Or so we or a single and

**Dave Jones:** they've just put two in parallel to handle the extra current or so Although, this isn't consider this like hugely high power. All right, I don't know why they couldn't have just used the one MOSFET, but anyway, I mean obviously you can

**Dave Jones:** narrow it down based on uh cell voltage and stuff like that, but we're probably not going to find it here, right? You're better off going to like LCSC maybe. Okay, we're in battery management ICs. So, we want SOT23-6.

**Dave Jones:** SOT23-6. There you go. So, we want both of those. I just picked the first cab off the rank there. And once again, series. So, Now, once again, we get this DW01 everywhere. That seems to be like a jelly bean

**Dave Jones:** part. By the way, there were some people that said, "Ah, this is cracked down here." cuz they thought they saw a crack on there. No, that's just uh So, that's just some residue on the top there. So, get a bit of spit.

**Dave Jones:** And there you go. Like a bought one. Now, we can actually search for uh this uh MOSFET part and with a like a six-pin um wire DFN thing, but unfortunately, um it doesn't look doesn't look easy. I've searched for uh

**Dave Jones:** six-pin DFN and like this is on Mouser and I get all those and I did it on um LCSC and um LCSC, look their their their packages, they don't even have any six-pin DFNs. Now, at this stage, what

**Dave Jones:** I'm thinking is that uh this device could actually be a dual MOSFET a dual series MOSFET with dual gates like that. Hence, the two extra pins on it. So, I think yeah, um the configuration we've got might be the dual MOSFET series

**Dave Jones:** MOSFET like this, and that's what we've gotten that just put two in parallel to get the uh current requirement. So, I I think that's a reasonable hypothesis there. Um cuz otherwise, like yeah, it's not it's not really making sense. So, I

**Dave Jones:** reckon yep, they're a dual and they've got two of those pins are going out to drive uh two of those MOSFETs. So, I think what I need to search for now is uh dual MOSFET, not single. So, I'll search for

**Dave Jones:** dual MOSFET DFN6. And right off the bat, what do we get? Dual N-channel MOSFET. Uh no, that's wimpy. Once again, like we need that wide body part. That seems to be the I think I I think if we find it,

**Dave Jones:** we'll know it. Um cuz they it seems to be really quite oddball. A good thing to do is search Google Images, you might get lucky. Yeah, nah. There's probably there's got to be one person out there. Oh, yeah, I know that

**Dave Jones:** MOSFET, used it before. Now, what is the size of that moose fit? Because uh you can actually search for you can search for the size of the package. Get my engineering ruler out here. Look at that. Oh, 5 mm. So, it's 5

**Dave Jones:** by All right, let's call that 5 by 2. So, it's a 5 by 2 DFN. So, if we search for a 5 by 2 DFN, we might get lucky. And doesn't look like we're getting lucky. Like must include 5 by 2. Like we

**Dave Jones:** can go down list, but it's not must include 5 by 2. Uh Oh, DFN 6 DFN 5 by 2. There we go. Don't mind that. But that is that the only hit? Wow, a 5 by 2.4 mm. I think it was actually two, but uh now

**Dave Jones:** we're talking. Diotec Is this a winner winner chicken dinner? It's on Digikey, Mouser. So, I guess I could have searched Mouser or Digikey for parametric search. Anyway, teach Let's look at the S1 S1 S2. Okay, that that pin out doesn't show It would have

**Dave Jones:** been nicer if they showed them in series, but it's sort of like wraps around like that. So, I thought that they were in parallel like at first, and that kind of didn't make sense, but uh yeah. So, imagine those flipped one one

**Dave Jones:** on top of the other because the pins here are S1 and S2 and S1 and S2 here with the two separate gates. So, yeah. So, that makes sense for our W um what is it? The W whatever 01 the DW01,

**Dave Jones:** which seems to be like a generic thing. So, I could check the pin out of this um to see it's probably a generic DW01 cuz like it seems like everyone makes that. Seems like a jelly bean part for this

**Dave Jones:** sort of thing. And I just noticed that these two MOSFETs, they are in series, but they're actually uh back to back. So, yeah. Um that does make sense. So, let's measure the uh gates on those and uh see what we get. Uh My National

**Dave Jones:** Instruments virtual bench has died. Bloody thing. I hate PC-based bloody things. Um so, yeah, I'm going to have to use my uh meter here. And um I can't find my good little ultra miniature probes. They Here's I used them

**Dave Jones:** somewhere and I didn't put them back on my microscope bench. So, anyway, Yeah, they're connected. Yep. And these two over here will be connected as well. Yep. Okay. And then they are separate. They are separate. Yeah, they're separate drive. Okay. Right. So, yeah,

**Dave Jones:** those two devices definitely in parallel. They use two separate gate drives. So, that indicates that Well, they're obviously they're in parallel, obviously, right? To get the extra current. But they do have like the separate gates. The separate gate

**Dave Jones:** drives. So, it looks like they would be um the series configuration. That makes sense that we saw that series configuration that we saw before. And once again, see, that wide body does not show up. The wide body does that device that we

**Dave Jones:** found on Mouser before does not show up in the parametric search. Let that be a lesson to you. Okay, trap for young players. Um yeah. It it did not show up. Yet we found that no problems before, right? Yeah, if I go back,

**Dave Jones:** where is it? There it is there, right? And I was searching this. I was searching that section. MOSFETs. Anyway, let's go measure the gate voltage, shall we? Sorry, I can't show you my multimeter. Sorry, I can't show you on

**Dave Jones:** screen. So, you're going to have to take my word for it. I need the microscope to see where I'm probing here. And so, I've got USB external USB connected in. Aha! We now have 3 volts. We have 3 volts

**Dave Jones:** on that gate. 3.15 volts. That one's at 3.15 cuz they're parallel. Turn it the right angle. Come on. That one is zero, though. And we'll just verify the voltage across there. Yeah, 3.5 volts across the MOSFET. So, that's

**Dave Jones:** it's open just like we measured last time. Oh, I just realized that those two in series, they're the opposite direction. Anyway, there were some people that said I should charge up the battery pack even though it's at almost

**Dave Jones:** 3.6 volts, which is like the middle of the discharge curve. It should be fine. They think I should actually charge up the pack and see if that makes a difference. Well, yeah, before that that's a simple thing to do. So, that's

**Dave Jones:** worth a shot. I'll do that now. I'll just charge it up a bit more, hook it up to the bench power supply. I've done a video on that how to charge lithium ion cells with your bench power supply. I

**Dave Jones:** have to link it in. Get back to you. Oh, no, check it out. Something's happened to my Rohde & Schwarz NGP800 power supply. Check out the screen. Check it out. Like there's something seriously wrong with that um screen. It's like

**Dave Jones:** there's some sort of artifact on it. I don't know what's going on there. Is it got like it seems like stripy or something as well. So, it's got a driver. Seems to have a driver issue. Anyway, there you go. I've

**Dave Jones:** got that charging at 1 amp and I'll get back to you. Okay, it's up to 3.93 volts. I'm charging at 2 amps. Actually, if I turn that off, it actually drops down to 3.8, but that's a you know, that's pretty decent. So, I'd

**Dave Jones:** say I'm just going to run with that. I don't want to wait any longer. So, I'll solder that back on see if it powers up. I doubt it though. Unfortunately, nope, that is a fail. And somebody suggested plug it up at their own clacker and

**Dave Jones:** infinite power. And yeah, nah. So, no charging there wasn't a battery threshold voltage thing that was under locking it or whatever. Nah. And I think it's likely that this is that Jelly Bean DW01 cuz the pin pinout seems to match.

**Dave Jones:** I mean, ground here is uh pin six over here. And if we jump over to the data sheet, you can see that pin six is ground. Uh pin pin five is VCC through a resistor. And well, it yeah, that seems to be it.

**Dave Jones:** And yeah, I'm assuming that trace goes up there to pin five. So, it's through a resistor and then you've got a bypass uh cap on there going down to ground. So, that matches up. Uh pin two over here is

**Dave Jones:** the input current sensor charger detect. And you can see that's through a 1K resistor there, right? So, that seems to match up. And pin three is the charge control gate. So, that yeah, I assume that via I'm not even going to buzz it

**Dave Jones:** out. I'm pretty pretty certain. And pin four is a test pin. It looks like nothing connects uh to that. And pin one is uh MOSFET uh gate detection. And I think that will go you'll probably find that uh that pin

**Dave Jones:** one goes up there to that via which drops down to the MOSFET. So, that appears to be a generic um DW01 uh battery protection IC of some. Who cares what the manufacturer is, right? Um you actually in fact the yeah, it it doesn't

**Dave Jones:** have DW01 on it, but you know, I I think it's an equivalent type part. Same pinout. Measure the voltage across the chip. Yep, we're getting in there 3.8 volts there. So, the the chip is getting voltage. Now, I'm actually going to

**Dave Jones:** check this switch. Oh, yeah. That works. Okay. Just wanted to Just wanted to make sure. Right. So, what we can do now is we can just uh bypass the uh MOSFETs here. So, just basically get a small little bodge wire to go over

**Dave Jones:** here. You can replace it with a fuse or I'm just going to use a little tiny bit of you know mod wire like this which will act as a fuse and that will go over and let's just see if the thing powers

**Dave Jones:** up. Yeah, cuz I don't want to desolder these now. It's easier just to bridge it. Put our little budge wire in there. And just tack that onto there like that. And we are now budged up. Nothing's getting hot. No magic smoke is

**Dave Jones:** escaping. What happens if we push the button? Nothing. What happens if we plug in an external charger? Nothing. All right. Looks like do we have a controller fire? Were we chasing a red herring down a rabbit hole? With the moose fits there and the charge

**Dave Jones:** control cuz we have well and truly bypassed that now. Let me double check. Our boost converter 3.3 volts there. So yeah, like our input is nothing. Like there's stuff there. There's voltage there. Okay, we've got our external power now.

**Dave Jones:** There's our input. Okay, so there's our 5-volt input and there's our boost converter is 4.4 now. Something is but it's not it's not working. I think we might have a faulty controller. That was probably the least likely scenario because like these

**Dave Jones:** battery protection things and MOSFETs they kind of like fail all the time. They're a bit notorious. So damn. I can get in there. I I've already spent enough time on this today. I want to do other stuff unfortunately. So I'd really

**Dave Jones:** have to resolder that. Extend that to get it out to physically get that out. I think. From there to be able to get in there and probe that chip. So, that's that's a pain in the butt. But, um yeah, we've basically

**Dave Jones:** ruled out the protection there. That's interesting, huh? Who would have thought? And I've just plugged it into a monitor here and now it like we're we're getting nothing out of this. So, that's interesting, is it not? It looks uh Who Who bet on the

**Dave Jones:** controller? I don't think many people bet on the controller. Everyone was saying, "Oh, yeah, MOSFET." Or it was the uh looks like a WDO1. If you do actually have a specific part for that, leave it in the comments down below that matches

**Dave Jones:** that. But, we found the exact um part number for the MOSFETs though. So, it like it even matches the code on top of the chip. So, yeah, we definitely found that. That's a diode ink jobbie. But, there you go. That is

**Dave Jones:** interesting, is it not? Anyway, sorry. I got to get get on to other things. So, uh another quick edit and upload. Anyway, thoughts and comments down below. Hope you found the interesting. It's uh yeah, looks like something to do

**Dave Jones:** with the controller is not happening. So, no, no, bypass battery protection. The voltages are there. So, Interesting, huh? Catch you next time.
