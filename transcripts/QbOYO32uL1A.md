---
video_id: QbOYO32uL1A
title: EEVblog #630 - How To: Soniq LCD TV Troubleshooting Repair - Part 1
url: https://www.youtube.com/watch?v=QbOYO32uL1A
source: youtube-asr
timestamps: {"0": 0, "1": 24, "2": 38, "3": 56, "4": 71, "5": 81, "6": 95, "7": 110, "8": 122, "9": 132, "10": 143, "11": 154, "12": 167, "13": 183, "14": 193, "15": 210, "16": 217, "17": 234, "18": 246, "19": 261, "20": 277, "21": 287, "22": 301, "23": 334, "24": 341, "25": 357, "26": 372, "27": 386, "28": 398, "29": 418, "30": 438, "31": 449, "32": 466, "33": 474, "34": 488, "35": 497, "36": 511, "37": 527, "38": 542, "39": 552, "40": 568, "41": 581, "42": 593, "43": 601, "44": 610, "45": 630, "46": 641, "47": 650, "48": 659, "49": 671, "50": 684, "51": 695, "52": 709, "53": 722, "54": 732, "55": 744, "56": 768, "57": 779, "58": 787, "59": 808, "60": 827, "61": 840, "62": 849, "63": 860, "64": 875, "65": 884, "66": 906, "67": 920, "68": 930, "69": 938, "70": 951, "71": 961, "72": 974, "73": 991, "74": 1006, "75": 1019, "76": 1031, "77": 1044, "78": 1058, "79": 1074, "80": 1086, "81": 1095, "82": 1109, "83": 1122, "84": 1131, "85": 1145, "86": 1153, "87": 1170, "88": 1183, "89": 1204, "90": 1219, "91": 1230, "92": 1248, "93": 1264, "94": 1290, "95": 1305, "96": 1325, "97": 1342, "98": 1353, "99": 1366, "100": 1383, "101": 1395, "102": 1411, "103": 1423}
---

**Dave Jones:** Hi, just a quick little repair video on this TV. It's my mom's TV actually. It's a really crap brand Sonic thing, you know, just a one hung low brand and she said that it's been going on the blink the last couple of days and she said there was a picture down the bottom or something and the audio was breaking up and doing all sorts of jazz like that

**Dave Jones:** and the picture's finally gone now, but it does show a boot up picture. Anyway, I thought I'd take a squeeze at it. I bought it back to the lab and let's turn it on and have a look.

**Dave Jones:** Here we go. Now, up. Yeah, see? Now we're getting the boot image, which is interesting in its own right because of course if the if something's wrong with the like the power supply, like seriously wrong with the power supply, you wouldn't get that.

**Dave Jones:** So all of the display panel circuitry's working and all that sort of stuff, the on-screen menu, but the built-in digital tuner is not working at all. Um so well, it's not displaying image, but audio was coming out of the thing.

**Dave Jones:** So that's, you know, it's curious. It could be a power supply issue that is affecting the digital tuner or something like that, perhaps, but uh anyway, I don't know.

**Dave Jones:** Like I can't get it to come up with the menu or anything like that um even with the remote and my mom's been having trouble turning it off. So uh yeah, it's interesting.

**Dave Jones:** Um fault So it's not a complete failure and that display that boot image comes up every time. So I don't know. Um the most likely fault with these sort of things is always going to be the uh you know, the the capacitors in the power supply is going to be a major thing.

**Dave Jones:** But uh anyway, that could still be the case, but it's got a HDMI input. So what I thought I'd do is hook up my Takano microscope to the HDMI input and see if that actually comes up or not.

**Dave Jones:** Woah, well, I've plugged in the external HDMI and I did manage to get a menu there for a second. So, um let's see if I can call up the menu again.

**Dave Jones:** Here we go. We've got it. So, that's rather interesting. Why it's coming up now and the menu wasn't coming up before. So, that could indicate yeah, marginal power supply, something like that.

**Dave Jones:** But, look, I mean, there's nothing wrong with that image at all. It is absolutely bang on. Uh here we go, input source. Okay, HDMI one. That's the Takano microscope.

**Dave Jones:** I'm not sure if it supports the 60 frames per second input. No, I mean, we're getting nothing out of that at all. No signal. No, that's a loser. Uh-huh, it wasn't Takano microscope.

**Dave Jones:** I got myself a Raspberry Pi here and uh it loads it uh views that just fine. So, it certainly couldn't handle the 60 frames per second. So, anyway, this sucker is working.

**Dave Jones:** Um jeez, it's making an idiot out of me. Now, um well, I couldn't get the menu up before, but uh the menu didn't come up immediately and when I powered it on.

**Dave Jones:** So, I don't know, maybe some sort of uh you know, hey, hello. Hello, we're gone. We're gone. Yep. Hello. Yeah, I can see the backlight is still on. But, uh no, it's yeah.

**Dave Jones:** It's flaky. It's flaky. I reckon it's got to be got to be a power supply issue. Look, I can't even turn that off now. Uh it's dodgy as this thing.

**Dave Jones:** See, one uh well, where's the boot message? Tada. Oh, look, there's no boot. There's no boot message. I I the boot on sound, but the boot message, no, zip.

**Dave Jones:** So, there you go. And if I try menu now, no, look at this, nothing. So, yeah, it's dodgy. All right, I'm not going to muck around with this anymore.

**Dave Jones:** I reckon most likely odds on power supply issue. Let's take it apart. And for those playing along at home, there's your model number. And there's few screws around the outside.

**Dave Jones:** Yeah, self-tappers into plastic, as you'd expect. There's little arrow markers on there, so presumably I only take those out. And uh but there's other ones on the back here which don't Oh, here we go, some bigger ones.

**Dave Jones:** So, that's in the side, these two are at the bottom. Yeah, you got to keep track of the different size screws. Okay, that was a bit of fail on the error on the arrows there.

**Dave Jones:** They didn't say these four had to come off, and it doesn't say if the stand has to come off or not. But uh yeah, yeah, stand has come out, too.

**Dave Jones:** Ah. All right, one more time for the dummies. Yeah, bloody power cord is like fixed there. Ah, oops, warranty void. Warranty void if removed. Yes! Gone-ski. You bet your ass we're going to void the warranty cuz this thing's out of warranty, so uh even if it was in warranty, who gives a toss?

**Dave Jones:** Uh-huh, all right, hey, we're in like Flynn. Check it out. I expected there to be another metal shield on top of there, but there's not, it's just a bloody angle bracket.

**Dave Jones:** Look at that. Unbelievable. Man, that just That's a That's pretty cut price. Oh, this is a pretty lightweight cut price uh sort of thing anyway. Processor board, power supply board.

**Dave Jones:** Let's take a look. It's a Megmeet brand power supply. Go figure. Um single-sided board, common as you'll find in these things, but uh at first glance, where's my little poker?

**Dave Jones:** Uh the main DC filter cap on the input there. Uh basically nothing. There's no um Uh you know, there's no uh bursting on the uh rupture seam there. There's no uh expansions.

**Dave Jones:** Not bulging. These other caps aren't bulging at all. There's nothing oozing out of them. They're just cheap one hung low brand caps. I don't know. They're a Yeah, Samsung with a Samsung with an X.

**Dave Jones:** Um yeah, not that great. Uh same with the digital down here. Nothing much happening on the caps down here. So, that's fine. I mean, any issues are more likely to be up in the main mains power supply up here, but on first glance, yeah, nothing obvious with the caps.

**Dave Jones:** Might have to get the ESR meter out. One thing that was interesting is that the main ribbon cable going off to the LCD coming out of the main processor board here goes up under the power supply, but look, they've got like another buffer board up there sitting between there, and then this goes off to the LCD panel.

**Dave Jones:** So, yeah, it's like some sort of rebuffering chip for the for the long run or something like that. Meh. All right, the first thing I'm going to do is use my Bob Parker ESR meter here.

**Dave Jones:** I'll short the leads, zero that out, and let's measure the main uh DC filter cap here. So, let's plug it on. It's an 82 microfarad uh 450 V, and we're getting about 0.63 ohms.

**Dave Jones:** A rough chart on here. I mean, you know, that that looks like a good enough value to me. I mean, talking you know, 450 V at around about 82.

**Dave Jones:** That's pretty much what I'd expect. So, nothing grossly wrong there. And as I said, no physical deformity in the vent on the end of it. So, you know, no swelling, no rupture or anything like that.

**Dave Jones:** So, that's you know, you'd have to say that's good. Next thing you do is take that board out cuz to access the other capacitors, we have to access the bottom side of the board, of course.

**Dave Jones:** Nothing visually wrong on here. I mean, you know, I'm not like I'm looking for any blowouts in any of the ICs or something like that. But really, if there was something like that wrong, then well, this thing likely wouldn't work at all.

**Dave Jones:** But we're seeing symptoms of like, you know, intermittent type symptoms that are indicative of a classic capacitor failure. So, you know, nothing visually interesting on the bottom of that main power supply board.

**Dave Jones:** So, I'll access few of the secondary side filter caps over here and measure that measure the ESR of those. And there you go. That's 1,000 10 V capacitor. It's basically a dead short at the 100 kHz at this thing measures that.

**Dave Jones:** So, you know, 1,000 it's you know, it's bang on. Really, nothing wrong there at all. We This chart saying it should be 0.1. We're getting 0.01. Not a problem.

**Dave Jones:** And there's another 1,000 uh 10 V and that's fine. Everything's Oh, that one that one's a bit high, though. I mean, you know, we're almost talking order of magnitude higher than the other ones.

**Dave Jones:** Now, that was that capacitor there. Now, curiously, that's a Chong brand, not the Sam Zong with a Samsung or however you pronounce it with an X, which these two are, which I just measured.

**Dave Jones:** And although that's not the same value cap, that's a 470 micro 35 V, but according to the chart on here, we expect a same value of around about 0.1 ohms.

**Dave Jones:** But hey, you know, that could be nothing. I that could be a red herring. I'm not going to chase that now. All right, I'm fairly happy with the caps I've measured on that board.

**Dave Jones:** There's nothing grossly wrong. So, um next thing, rather than jump straight into the digital board, I'm just going to power up this power supply, measure it on the scope.

**Dave Jones:** So, I'm going to use my LeCroy AP031 differential probe here set to 100:1 um attenuation ratio. So, if there's 450 V on that cap, for example, then I'll only get 4.5 V out of this thing, and I can measure that on the scope.

**Dave Jones:** Let's see if there's any ripple. So, let's power it on and see what we get. And there we go. We're at 1 V per division there. Don't Oh, there we Oh, that was interesting.

**Dave Jones:** It just uh it was mucking around there for a minute. There was a bit of uh bit of ripple on that. And let me just connect the power and do that again.

**Dave Jones:** I haven't actually switched the power on. So, we're basically just in standby power mode at the moment because be careful this is live. Always keep one hand in your pocket.

**Dave Jones:** Uh this um power supply is going to stay on all the time cuz this is just a soft standby function. So, you're always going to have that. So, what have we got there?

**Dave Jones:** We've got a 100, 200, 300 and something on there. There we go. We're getting a little bit of uh bit of ripple on that, but yeah, nothing serious. So, we'll have to power the thing up, of course, and well, I'll do that now.

**Dave Jones:** I'll press the standby button. Here we go. Boom. We jumped up. We're getting some ripple there. It doesn't look uh doesn't look that bad. I see the screen at the moment cuz the damn thing's lying down.

**Dave Jones:** There we go. We got some higher frequency ripple stuff. So, I presume Yeah, there we go. I heard heard it boot up. So, it's all booted up now, and we're getting some You probably can't see that, but some high frequency ripple on that thing.

**Dave Jones:** There you go. And uh that's pretty much what you'd expect. So, that's fine. There's nothing wrong with that main filter cap at all. And if you're curious to see how quickly this discharges well, let me unplug it.

**Dave Jones:** And um it's still holding a decent charge. Look at that. This is why you don't want to touch these things unless you've left them off for quite some time.

**Dave Jones:** And it's also recommended, you know, you put a dummy load across them or something like that, a big-ass resistor um you know, calculated that you can put across there and just drain that main filter cap.

**Dave Jones:** But, look at that. That main filter cap, that is still got 200 and, you know, 70 200 That'll give you a hell of a belt. And of course, something like this uh proper high-voltage differential probe is what you need to be safe measuring the primary side of a switching uh mains uh you know, power supply like this.

**Dave Jones:** The secondary side, that's okay. It's A, it's lower voltage, and B, it's uh isolated. So, you can actually use your regular scope on uh the secondary side of it.

**Dave Jones:** But, that primary side, you don't want to go around unless you've got one of these high-voltage differential probes. Worth every cent. And I'm just measuring another cap on the secondary uh side here.

**Dave Jones:** Yes, I'm still using my differential probe just because I can, and it's still hooked up. Um yeah, 12-V rail, no problems, no ripple whatsoever. So, I'll probe a few ones that I can actually uh probe around here, but I don't really um expect to find anything on this primary uh um you know, power supply here.

**Dave Jones:** So, it's more pointing towards the secondary uh the processor board at the moment, which I I was hoping. I'm rather surprised at that. The odds weren't The odds were uh much more that it was going to be the main power supply in this thing, but possibly not.

**Dave Jones:** Okay, I've measured another rail here, which is around about uh 25 V. This is 5 V per division. 5 10 15 20 25 V. There's a 35 V cap in there, and uh I Well, yeah, you can see the rail.

**Dave Jones:** There we go. It dropped a bit. Uh I've now switched it off. That was on before. So, now I'll switch it on. And uh See it Well, there we go.

**Dave Jones:** You can see it jump down a bit, but you know, look, there's no ripple on there. There's nothing wrong with that cap. I don't know. To measure all the other rails, uh yeah, it's a bit tricky, but Jeez, there's nothing obvious.

**Dave Jones:** Um yeah, I might have to start going down to the processor board down here and checking out the uh digital rails on that sucker. Now, they have actually been uh relatively kind and labeled the power rails uh down on here on the silk screen.

**Dave Jones:** So, there's as we looked at before, I'm just going to measure this is the 24 V rail. Rail. 20 It's nominally 24, but there's 25. There's nothing wrong there.

**Dave Jones:** Uh this should be plus 12. I assume it's the same rail uh same ground. Yep, it is. Plus 12. Uh plus five happening over here. 5. Yeah, 5.25. They've trimmed it to be on the high side.

**Dave Jones:** As you'd expect, and uh plus 5 V standby. Um So, yeah, the rails are good. I'm not going to go through and measure the uh ripple on all of those, but jeez, you know, not much wrong there at all.

**Dave Jones:** And this is uh switched on by the way. The thing is actually uh powered on and uh displaying something. So, yeah, under load, meh, those power rails are just fine.

**Dave Jones:** So, can pretty much rule out this board. Okay, next thing we're going to want to do is uh just have a poke around at some of the internal rails on here.

**Dave Jones:** The um uh SOT-223 packages there, they're dead giveaways that they're uh local voltage regulators. And yes, I've checked uh like the can of here is ground um is connected through the common ground.

**Dave Jones:** So, you can just put one probe on there and just uh probe around to your heart's uh content. All right, there we go, 3.3 V on the output of that regulator.

**Dave Jones:** Don't even need to measure the um input because, well, I know it's 3.3 V. It's obviously 3.3 V regulator, even though it's not marked. Exactly what you'd expect. So, you just go around and probe.

**Dave Jones:** 1.89, that's obviously a uh processor core voltage. Another 3.3 V local regulator there. What's this one? 3.3. So, they're all fine. I've got no problems with that at all.

**Dave Jones:** Be handy if they actually had proper voltage test points on this um uh silk screen overlay and uh you know, allowed you to uh play around with these things, but uh and measure them, but they don't.

**Dave Jones:** There's a 12 V. There's 5 There's 5. There's a couple of points marked there. It's actually a few uh just a little strap on there. So, jeez, the power supply is fine on this thing.

**Dave Jones:** So, what's the problem? I've got no idea. Now, this is interesting. Sorry, I'm looking up under the bench here and look, there's a line on that display and it's flickering in and out.

**Dave Jones:** We've got no input signal. I don't know what source is selected there, but yeah, that's that's it's not a well puppy, that's for sure. There's something going on here.

**Dave Jones:** Don't know what. Whoa, you see that red? What the hell was that? And just for kicks, I'll get out my Fleer thermal imaging camera more just to have a play around with and pretty much the things that are getting hot are the things I expect to get hot.

**Dave Jones:** A couple of free standing TO-220 packages over there. They're mounted on the heat sink. These ones over here are power power resistors presumably on the main rails. They get pretty hot.

**Dave Jones:** Actually, it's not good from this distance distance. I was measuring like up to 70° on those and the digital part of it was you know, the regular expect the individual regulators to be hot and stuff like that.

**Dave Jones:** So, nothing out of the ordinary at all. And the great thing is you can generate an external signal source cuz it's got a 5-V USB on here and a HDMI input.

**Dave Jones:** So, you just loop your Raspberry Pi through that and bingo, look at this, see? There it is. You can see the menu for a minute and then it it's flickering.

**Dave Jones:** It's flickering and then oh, it really doesn't like that. Now, interestingly, you can actually buy this complete replacement board, the MIP 329FL or the MIP 320FL1 board on eBay.

**Dave Jones:** You can get it for about 35 bucks shipped or something like that. So, there's actually quite a few people selling those. So, they're obviously used in a few sets.

**Dave Jones:** But anyway, I can't find a schematic for it or a schematic for this particular TV either. So, you know, we're we're pretty much going to have to do without.

**Dave Jones:** Oh, by the way, a handy tip if you want to discharge these caps, you can actually use one of these meters if you got one that has this low input impedance voltage mode.

**Dave Jones:** So, you can actually just use that and then can we see that? There we go. And then whack that across the main filter cap and bang 4.6 that was up to like still up to like 50 volts or something like that.

**Dave Jones:** But now we've actually discharged it using the internal low impedance of the meter. So, that can actually be really quite handy. Not only for eliminating ghost voltages but in this case bleeding out voltages before you work on gear.

**Dave Jones:** Check this out. Taking out the main processor board, measuring the main filter cap here it's a 470 mic 35 volt and I'm getting .15 ohms which sounds okay, but according to the chart which is still like a very rough guideline, it should be about .1.

**Dave Jones:** So, that kind of is reading a bit high. I'll just swap the probe. Shouldn't make a a rat's difference, but just verifying yeah not .1 five there. So, I don't know.

**Dave Jones:** Considering that I don't have any other leads on this thing, I don't know. Might just be worth quickly swapping that one out. And check this out. There's another couple of 470 mics on there.

**Dave Jones:** Now neither of these appear to be low ESR types. They're just you know ordinary crap electrolytic caps of whatever brand and model and basically only one voltage rail difference there and you know we're looking at .

**Dave Jones:** 22 ohms there. So, you know, that's under the chart figure of .25, but still you know, I I don't know. Red herring. I mean, you're really looking for these things to stand out.

**Dave Jones:** They should be you know grossly different, but when you're talking about an intermittent problem like this, it could mean that often means that the capacitors could be on their way out, for example, or some components on its way out, some components marginal, usually caps, because they got an electrolyte in them that dry up and increase the ESR on the things, especially when they heat up during operation and things like that.

**Dave Jones:** So, you could be looking at a marginal value there, but once again, when you've got two side by side and they measure exactly the same and they're not in parallel, then well, you know, you can be pretty sure that those two are are okay.

**Dave Jones:** Now, the problem here is that the symptoms aren't really consistent. I've had anything from, you know, not switching on at all to not switching off at all to getting audio through, but no video to the picture breaking up, we're getting red lines through, all sorts of jazz like that.

**Dave Jones:** So, gee, yeah, I don't know. You know, BGA, it could be a thermal thing happening with the BGA, perhaps. Who knows? Yeah, nothing's really pinpointing this fault down to to any particular area at all.

**Dave Jones:** So, you just got to generally bum around hoping to find something. Well, I've powered it back up again, been playing around with it and I'm getting nothing on the screen now at all.

**Dave Jones:** So, you know, the backlights are working, everything's just fine. All the all those power rails look good and and, you know, it's given the boot up thing and everything's hunky-dory.

**Dave Jones:** So, I don't know. It seems to be getting progressively worse and worse, pretty much. So, not sure what the deal is. Anyway, I'm going to have to leave it there because I'm running I've run out of time to do this and uh well, yeah, I don't know.

**Dave Jones:** I'll have to have another crack at it, but my my mom wants a TV back, and well, it could be uh uh I don't know, beyond economical uh time repair, anyway, um in terms of getting her TV back.

**Dave Jones:** So, mhm, I don't know. Anyway, uh hope you enjoyed that. Yeah, sorry, it's a non-event. Again, people will be pissed off. Oh, well. So, if you're a bit peeved off I didn't fix it in this video, well, tough luck.

**Dave Jones:** Don't leave some stupid comment, "Hey, why didn't you fix it? Why didn't you upload the video? Mhm, at least you fixed it. Mhm." God. Unbelievable. I'll get people coming in like that, anyway.

**Dave Jones:** Catch you next time.
