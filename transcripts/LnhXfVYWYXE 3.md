---
video_id: LnhXfVYWYXE
title: EEVblog #70 - Turn your Rigol DS1052E Oscilloscope into a 100MHz DS1102E (Hack)
url: https://www.youtube.com/watch?v=LnhXfVYWYXE
source: youtube-asr
timestamps: {"0": 0, "1": 36, "2": 59, "3": 89, "4": 119, "5": 150, "6": 183, "7": 213, "8": 233, "9": 271, "10": 315, "11": 362, "12": 384, "13": 403, "14": 434, "15": 454, "16": 485, "17": 525, "18": 557, "19": 592, "20": 618, "21": 646}
---

**Dave Jones:** Hi, welcome to the EEV blog and electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, back in an earlier blog when I did a teardown on the Rigol oscilloscope, I made the suggestion that it might be possible to actually hack this thing to mod it to the 100 MHz version to be the same as a DS1102E model. And because the the two models, they looked they looked fairly similar and I thought it's got to be possible.

**Dave Jones:** And uh but I didn't really put any effort into it myself. I didn't really have the time or the inclination. So I opened it up to my uh viewers and they got to work and finally, yes, apparently it's been hacked. You can all you need is a serial cable and you can mod this thing to a 100 MHz version. So let's give it a go and see if it actually works.

**Dave Jones:** Now, there's a few people responsible for this this hack. Although I originally suggested the possibility, um there's uh three key people who came up with the uh Ross Moffett did uh a lot of the early work trying to do a hardware mod cuz that's what I thought it was and that's what everyone thought it would be would be a hardware modification. And then uh um Andreas, I think that's how you pronounce it, from uh Germany, he actually cracked the uh circuit. He came up with it and here's the circuit here

**Dave Jones:** with the as you can see, it actually uses a varactor um diode. It's basically a variable capacitor um which uh has two control lines which actually sets the bandwidth of this thing. One the first one is in the 20 MHz bandwidth limited mode and the other one, as it turns out, um if you do the combination, actually switches on the uh 50 or 100 the actual 50 MHz limit which is in the DS 1052E.

**Dave Jones:** And that's what it turns out to you can actually do it as a hardware mod if you actually switch those control lines, but but then a user called Bushman actually suggested that well he he actually came up with the serial port hack where you can actually just send it a serial port command and it just it just does it. You can actually all you got to do is change the model number and the firmware automatically selects that individual line switches are often bingo, it switches the firmware into the 100

**Dave Jones:** megahertz mode and let's give it a go. Okay, now before we do the mod, let's actually get a base level bandwidth and rise time measurement so we've got something to work with. And let's do the 50 standard unmodified unit here. What I'm doing is I'm feeding in a very fast rise time square wave and you can actually measure that you can use that as a measurement of the bandwidth using the standard formula of 0.35 divided by the rise time or the fall time. Now, what I've got it set here but

**Dave Jones:** we'll talk about it later. What I've got set here is 16 averages just to clean it up a bit equivalent time sampling but if you change it to real time it doesn't make much difference either. Now, as you can see the rise time is about 5.2 nanoseconds. Now that's about 65 megahertz bandwidth but that's kind of what I expected because the Rigol spec says it should be 7 nanoseconds or less than 7 nanoseconds so it is. But after we do the mod we should see that rise time

**Dave Jones:** actually improve with the same signal. So there's our base level measurement. Now I'm going to take a step-by-step through the procedure. I'm using HyperTerminal here. I've got a standard I've got it hooked up to the Rigol oscilloscope with a standard straight through serial cable. Now it's got to be straight through not the crossover type.

**Dave Jones:** Okay? So, you load HyperTerminal, let's set up a new test, COM1, and it's got to be 9600 baud, and eight data bits, uh no parity, one stop bit, and hardware flow control off. So, let's turn that on, and then you want to go into file, properties, and settings, and ASCII setup down here, and you want to turn on send line feeds, um and you want to echo the characters, and you want to append line feeds to incoming line ends. You press okay, and bingo. Okay, now let's do the actual

**Dave Jones:** mod. What you've got to do is you've got to type in asterisk IDN question mark, and then don't press enter, because that's actually a carriage return. What you want is a line feed, so you've got to hold down alt, and you've got to go 010 on the numeric keypad. And bingo, there we go. Wright Gold Technologies DS1052E, and that's my serial number and the revision number. So, next, we want to actually change the model number. So, we type in colon info colon model space DS1102 E. That's what we want to change it to.

**Dave Jones:** Once again, don't hit enter, but type in alt 010. And next, we want to type in colon info serial space and then, we want the serial number, but we want to change that D to a B. Okay? So, we'll type in DS 1 E B instead of D, double 1 08 00915 And once again, don't hit enter. Just type alt 010 and that's it. That's the entire mod. It should be um programmed into the flash memory. So, let's give it a go.

**Dave Jones:** Okay, we've done the mod. So, let's repower the scope. As you can see, rise time 5.3 nanoseconds. Now, we'll just repower it. And here we go. Let's see if the mod has worked.

**Dave Jones:** Bingo, there it is. You can see the wave shape's changed. Look, you can see the see the extra ringing up there and down there. And there it is, 3.2 nanoseconds. Beauty, it works. And as you'll see, we'll change the time base. It used to go down to 5 nanoseconds maximum. Now, it goes down to 2 nanoseconds maximum.

**Dave Jones:** We now have a 100 MHz 1102E scope. And let's go into the utility menu and check out system info. Bingo, there it is. DS1102E and the serial and the new serial number and terrific. Thumbs up, it works. And after you've done the mod, you should also do a self-calibration. So, you go into the utility menu and you go through and self-calibration.

**Dave Jones:** Disconnect all the inputs and run the stop. And that takes some time, but if you let it go through there, it recalibrates the input channels and all should be right. Okay, let's do another benchmark comparison. I don't actually have a Rigol DS1102 scope to compare it with, but I reckon I got the next best thing.

**Dave Jones:** It's a Tektronix TDS 1012. It's the same specs effectively, 100 MHz analog bandwidth, 1 gig sample per second. And I'm feeding in exactly the same signal I fed in before. And as you can see, the wave shape is almost identical, and our rise time is actually it's actually not as good. It's actually 4.4 nanoseconds, and the fall time is 3.3 nanoseconds. But uh so there you go. Maybe the um the obviously the maybe I should get in there and measure it manually, but the looks like the Rigol is slightly better

**Dave Jones:** than the Tektronix unit in this case. But that's an excellent confirmation that the mod is genuine and it works. Now, as you saw the rise time uh with the modified scope, it was about 3.4 nanoseconds. And that matches the uh Rigol 1102 data sheet precisely, which says it should be less than 3.5 nanoseconds. So I know that's not really a true performance uh measurement because the 0.35 um on the rise time formula that that industry uh standard formula is is really designed for a a a Gaussian response um

**Dave Jones:** analog scope. Uh digital scopes are actually they can actually be higher than that. Actually, it's slightly less than uh 0.35. It's like uh 0.34 if you want to get technically into the theory um for a standard Gaussian response. But digital scopes don't actually have um or typically don't have a Gaussian response or a single pole response, which is what the 0.35 formula is. Anyway, let's not really go into the details. It's close enough. Um I really I know I don't have to do a full performance measurement on

**Dave Jones:** this thing to know that it's definitely cracked. We've got an a DS1102E 100 MHz bandwidth. No problems at all. So there you go. It does actually work. I can't believe how easy it was. It was trivial. My money was on that Rigol I at least go to the effort to uh to change the bill of materials and do a few component changes on the board and maybe even have separate firmware just to you know just to stop simple hacks like this and eating away their their margin cuz

**Dave Jones:** they're clearly making you know an extra three $400 just for typing in a different command and slapping a different badge on the thing. Rigol caught with their pants down again. Now there was some talk from people that oh we should try and keep this mod quiet so that it doesn't ruin it and things like that because no doubt Rigol are going to once they hear about this they probably already know about it but once they hear about it that everyone's doing it then no doubt they're going to

**Dave Jones:** actually stop they're going to change the firmware and stop it this simple mod but unless they change the board you can actually mod it mod the bandwidth with a hardware mod by tying one of those control lines so unless they change the hardware as well it's not going to be too hard to still mod this thing and you can probably get the old firmware and burn it in so you know it may not work for you know for all models in the future but it certainly works now so if you've got one

**Dave Jones:** of these babies get yourself a serial cable and mod it to the 100 megahertz one. Beauty.
