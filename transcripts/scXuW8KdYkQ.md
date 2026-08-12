---
video_id: scXuW8KdYkQ
title: EEVblog 1726 - REPAIR of an EV Charger (Unusual Twist!)
url: https://www.youtube.com/watch?v=scXuW8KdYkQ
source: youtube-asr
timestamps: {"0": 0, "1": 12, "2": 28, "3": 36, "4": 47, "5": 56, "6": 63, "7": 73, "8": 85, "9": 98, "10": 109, "11": 120, "12": 141, "13": 154, "14": 172, "15": 186, "16": 199, "17": 209, "18": 229, "19": 242, "20": 255, "21": 274, "22": 285, "23": 296, "24": 311, "25": 328, "26": 338, "27": 355, "28": 363, "29": 372, "30": 386, "31": 396, "32": 409, "33": 421, "34": 439, "35": 450, "36": 464, "37": 476, "38": 490, "39": 506, "40": 515, "41": 538, "42": 556, "43": 571, "44": 587, "45": 604, "46": 617, "47": 627, "48": 645, "49": 654, "50": 670, "51": 684, "52": 696, "53": 707, "54": 720, "55": 736, "56": 753, "57": 764, "58": 777, "59": 790, "60": 802, "61": 817, "62": 834, "63": 847, "64": 860, "65": 869, "66": 881, "67": 891, "68": 906, "69": 919, "70": 931, "71": 944, "72": 958, "73": 972, "74": 982, "75": 995, "76": 1007, "77": 1023, "78": 1037, "79": 1056, "80": 1067, "81": 1079, "82": 1099, "83": 1110, "84": 1126, "85": 1141, "86": 1155, "87": 1167, "88": 1178, "89": 1189, "90": 1205, "91": 1216, "92": 1232, "93": 1247, "94": 1259, "95": 1270, "96": 1287, "97": 1304, "98": 1313, "99": 1323, "100": 1348, "101": 1358}
---

**Dave Jones:** Hi, do you remember this new energy EV charger in quote marks cuz there's no such thing as an EV charger. It's actually built into the car. It's what's called an EVSE or an electric vehicle supply equipment.

**Dave Jones:** But it's basically a little fancy screen with a relay in there that switches the power through to the car and the car has the charger in it. Anyway, I did a video um teardown of this thing and it wasn't great and I didn't recommend uh this thing um at all.

**Dave Jones:** I'll link in the video if you haven't seen it. But this thing has actually been a few used a few times. Um not by me, by someone else. But uh yeah, it's it's failed.

**Dave Jones:** So, I don't know. It's been used like half a dozen times or something um and it just, you know, periodically and it's just died. I do actually have um power hooked up to it at the uh moment.

**Dave Jones:** I've got 240 V going right up the uh clacker there. Nope. Nope. It's drawing uh some Don't know if you can see that, but it's drawing uh no volts.

**Dave Jones:** So, it should actually come up with the screen on the thing. Um and like just, you know, waiting for the to plug in for the car and everything else and it doesn't.

**Dave Jones:** It's deadskis. So, let's crack it open. See if we can see anything. First thing I do is check do we actually get anything up the uh clacker. This is an Australian uh 32 amp outlet.

**Dave Jones:** I've got one of these installed in my garage which uh powers my Zappi and it's 131 K. So, it's not like like there's an input fuse. I don't actually remember there being an input uh fuse on this thing.

**Dave Jones:** So, it's not like the input has popped. There's something there and we'll just go to earth as well and well, we've got eight meg there and open there. So, yeah.

**Dave Jones:** There you have it. Uh as I said, more detailed teardown in the previous video which I'll link in, but uh nothing obvious. Give it a smell. Nothing burnt. It's nothing obvious.

**Dave Jones:** And as I said, yeah, I don't think there's an input fuse. Goes into the relay. Oh, no. No, there we go. Yes, it does have a fuse. It's a little fuse and there's little brown jobby over there.

**Dave Jones:** So, I'll check that. Apart from that, the display board looks okay. Nothing doing there, really. So, it seems otherwise okay. So, let's check that fuse. To get that board out, got to take off all the uh mains connections here and get that out.

**Dave Jones:** I love these. These are just these little um press fit connections like that. That's the uh control wire for um going off uh the pilot wire or whatever it's called going off to the uh EV connector.

**Dave Jones:** Wonder if you get the grommets out, too, to try and get the board out. It's a bit tricky. All right, the board's out. So, our fuse is up there and that, of course, powers all of our via the high voltage um string series resistor uh network there.

**Dave Jones:** No. Well, there you go. The plot thickens. And we've got a common mode choke here. So, I tested the uh resistance of that. So, there's one side here and it's about uh just under 1 ohm and this side's just under 1 ohm.

**Dave Jones:** So, our mains input comes from here, goes to one side of the common mode choke, pops out the other side, and then goes over to the fuse. And we So, we know that common mode uh choke is intact and that fuse is intact.

**Dave Jones:** And this side here and this side here is down to the neutral. So, we know the neutral side is intact there. So, then we've just got an X class uh filter cap uh across the mains.

**Dave Jones:** It's X It's X class because it's across the mains. Think of X as across and Y is goes down to earth. So, Y class capacitor is a capacitor that's from either of the main active or neutral down to earth and the X class is one that's across active and neutral.

**Dave Jones:** So, that'll be an X class cap. And you'll notice that's exactly what's on there X2. There you go. Well, I haven't measured the series resistors. They're one of those could have gone ski, but at least we're getting the voltage to here.

**Dave Jones:** So we're getting nothing on the LCD screen. So it's almost as if it's not getting power. I mean, you know, it could be the screen that's gone, the micro that's gone or something like that, but you know, first rule, thou shalt measure voltages.

**Dave Jones:** Okay, we have 539 K resistors there. So total resistance is there you go, 131. But because that's in circuit, we could have something in parallel with that upsetting the apple cart, but there's something there.

**Dave Jones:** Totally forgot chasing a red herring down a rabbit hole there. Anyway, worth a check. This is actually a current transformer. I'll put up the data sheet for that here.

**Dave Jones:** And what we really need to look at is this DC to DC converter over here because that, if you have a look at the bottom, there you go, that's directly connected there as well.

**Dave Jones:** Those caps look intact. The vent holes there look like they're fine. There's no bulging, but yeah, it's built down to cost cuz this is a really el cheapo charger, one of the cheapest on the market.

**Dave Jones:** So it's most probable that that DC to DC converter has failed, I suspect cuz really, you know, there's not much else to go wrong. All right, well, let's measure the output of the DC to DC converter here and there's your problem.

**Dave Jones:** Yes, we are getting 240 V mains in there, but we're getting nothing out on the DC to DC converter. So no surprise that this puppy is not powering up at all.

**Dave Jones:** So something's failed on that module. Most likely cuz as I said, you know, they built this thing for, I don't know, 30 cents, 50 cents, something like that. It's just a module and well, it's coming a gutter.

**Dave Jones:** And when you're talking about a fire mode of like the complete screen, just like it just doesn't power on, then it's very likely to be a power supply issue.

**Dave Jones:** It's, you know, it's far less likely to be like the microcontroller at fault, anything on here like this. And that's why the golden rule of troubleshooting is thou shalt measure voltages.

**Dave Jones:** And yep, that's completely coming a gutter. I'm sure the 240 volts is getting in there. It's just the PCB traces straight in. But just for a sanity check, if you're really that interested, there you go.

**Dave Jones:** We're getting our 240 volts directly on the two pins. So, yeah, that module's gonski. There you go. I sucked the module out and there's a sneaky little half tap under here.

**Dave Jones:** These are all the same value. So, they're splitting that in half and then bridge rectifying that here. And they're using that as part of the sensing stuff here for ground faults or whatnot.

**Dave Jones:** And looks like we just got a protection diode directly across the positive output of the regulator here. And there's a little switching converter. I don't see any blow holes.

**Dave Jones:** There's the bridge rectifier. It It might have been gonski, but there's no no magic smoke has escaped. So, yeah. And that is a DK 1203 switching controller. I don't know that one offhand.

**Dave Jones:** I'll whack up the data sheet for that. But yeah, there's a opto-isolator between the primary and the secondary there. We've got our capacitive coupling between the primary and secondary.

**Dave Jones:** There's our big output diode. Okay, we can just check the bridge rectifier here. And yep, we should get both of those one diode drop. And then we have to change the probes around.

**Dave Jones:** This will be the positive. Yep, there we go, and boom, like that. No worries. Diode bridge is intact. So, we should be getting a full wave rectified mains voltage across the cap here.

**Dave Jones:** Oh, damn. Here's the capacitor. Look at the clearance in there. Look at the Like hello. It's not like they've deliberately done that for a spark gap thing. There's no exposed solder mask there.

**Dave Jones:** Oh my god. Like, you know, who cares about clearance? We'll continue to measure stuff on here because that's the easiest thing to do cuz it's really annoying to like put 240 and dangerous to put 240 volts up to here and then just start probing around willy-nilly, you know.

**Dave Jones:** We have to get out our isolated probe, and then we need like little fine grabbers to like, you know, get onto like individual pins and stuff like that, and it's a real pain.

**Dave Jones:** So, anyway, let's measure the transformer next. Our primary 2.2 It's a bit low. Would have expected 5 to 10 ohms or something like that, but that's okay. Secondary side should be like almost Yeah, almost a short because there's, you know, the bugger all cuz the turns ratio is going to be small.

**Dave Jones:** That flyback transformer seems okayish. I've measured that diode there. It's fine. So, really, there's not much left on there. Um, it's the internal switching transistor is inside the driver there.

**Dave Jones:** And, of course, you're going to give it a visual inspection of the solder joints because these things are heat up, so you can get cracked solder joints, but everything looks pretty hunky-dory on here.

**Dave Jones:** Not really seeing any issues with the solder joints, so can basically rule out a cracked joint cuz that's a not an uncommon failure mode. But that is more to do with like, you know, high power, high current supplies that heat up a lot.

**Dave Jones:** This one's, you know, it it it's pretty wimpy. What is that, you know, a couple of watts? We'll just power this thing up on the bench again and just a sanity check, we will double-check that we're getting yep, absolutely nothing out of that.

**Dave Jones:** Measure the mains filter cap there, unpowered of course, and it's discharging. There you go, no worries. So, it was getting something on there. All right, we'll measure the full wave rectified voltage across the cap there.

**Dave Jones:** The safe way to do this is not to power it up and then probe it, is to get like some easy hooks like this, attach them before you connect it, and then plug it in.

**Dave Jones:** So, let's go. And yep, 336 volts, no worries. And you can see that's going to discharge and it'll take a while, but it'll get there. Or we can just use our low Z thing and that will very nicely discharge it.

**Dave Jones:** It'll be already gone. >> [laughter] >> But yeah, it can't even read it. It's so low. There you go, we're down to 1 volt. Oh, it's rising back up.

**Dave Jones:** Ooh, dielectric absorption. All right, it's oscilloscope time and of course you want to be safe. So, we've got the HVP 70 high voltage isolated probe here times 100. We'll set up the scope for times 100 probe input.

**Dave Jones:** And once again, don't go try probing when it's live. I've still got this disconnected, so let's power it up and see what we get, shall we? So, what we're going to measure is directly across the switching transformer there.

**Dave Jones:** That'll do to see if we at least get some sort of switching waveform. All right, so So, plug it in. We're 100 volts per division, see if we get any switching action at all.

**Dave Jones:** Oh, there was Well, yeah there's a little attempt there. There is an attempt. Where is our trigger level? There we go. So, we can single shot capture that. There we go.

**Dave Jones:** So, it's attempting. There you go. It is attempting to do something. So, we'll put normal mode there and we can see that yeah, it's it's it's just every like cup every second or whatever.

**Dave Jones:** It's attempting to do some switching. So, but it doesn't like it. She ain't sticking on. So, maybe secondary side regulation feedback perhaps. So, you can probably see that updating there.

**Dave Jones:** It is the same waveform and like every one two every three like every second that is updating. So, it looks like the switching controller is actually working. So, it's getting voltage, but it's entering some over protection over voltage over current protection hiccup mode.

**Dave Jones:** And this is quite common with these switching controllers. I've had a look at the data sheet and it does mention it does have a protection mode like this. It doesn't mention a second.

**Dave Jones:** It mentions like half a second. Um but yeah, still that is looks like we've got a secondary side problem here, not a primary side problem because we're switching that.

**Dave Jones:** That's 100 V per division. 100 200 300 We're switching that sucker. No worries, but yeah, it's just not going into regulation and that's what the feedback is on the secondary side with that opto isolator.

**Dave Jones:** So, I think we have to investigate the Let's just unplug it here. See what happens. Ooh, look at that. She's going down. She's still switching. It's still switching. Look at this.

**Dave Jones:** >> [laughter] >> It's still going. Wow, those like two microsecond pulses there of current aren't actually discharging that cap hugely fast, are they? So, [laughter] there you go. Shows how much Oh, oh, what's this lengthening?

**Dave Jones:** Look at that. Oh, oh, she stopped. She stopped. There you go. Okay, having a look at the secondary side here. We can see that we've got, of course we do, a classic TL 431 current shunt reference there and not much else.

**Dave Jones:** So, not much else can go wrong here. We will check the secondary side filter cap. We've got our diode secondary side diode over there. But, yeah, there's not much that can go wrong here.

**Dave Jones:** Pretty basic plain vanilla stuff here. So, yeah. Okay, I just want to check the VCC pin, which is pin two there, just to make sure that we're getting a decent voltage.

**Dave Jones:** Oh, helps if I put on DC volts, doesn't it? There we go. I'm 5 volts. No worries. So, the chip's powered up. I've turned the power off and it's still there.

**Dave Jones:** Still going. Come on, you can do it. You'll probably find it'll suddenly drop off a cliff eventually. There we go. There we go. Yep. Oh, it's clinging in there.

**Dave Jones:** Well, at this stage, I'd say the fire is most likely to be high ESR in the output caps. I'm not sure if those they're in parallel. Doesn't look like it.

**Dave Jones:** I can measure that, but I think statistically that's most likely and that will lead to excess ripple on the output, even though there's not a huge load on here, I don't think, cuz it's only powering the micro and the display takes a reasonable amount.

**Dave Jones:** Color whiz-bang display takes a reasonable It's got a dot matrix thing on it. It takes a reasonable amount, but any excess ripple in there could actually be triggering the hiccup mode in the controller here.

**Dave Jones:** So, I'm going to I can try and measure those in circuit first, but if not, easy to suck out. Although, having said that, it is trivial to measure the opto primary side of the optocoupler.

**Dave Jones:** So, I'm going to go ahead and do that. Although, having said that, it is pretty trivial to measure the primary side of the optocoupler feedback there. So, I'm just going to probe that.

**Dave Jones:** There we go. We're at 2 V per division. I've switched to my probe to 10:1. So, we are actually getting feedback on that optocoupler. So, that optocoupler is good.

**Dave Jones:** That's, as I said, on the primary side. So, the optical part of it's working. The the LED on the primary side of the opto Sorry, well, that's confusing. The primary side of the optocoupler is actually on the secondary side of the transformer.

**Dave Jones:** So, the LED is on the secondary side of the power supply. That's feeding back to the phototransceiver on the primary side. And sure enough, we are actually getting some switching on there.

**Dave Jones:** And that's exactly what you'd expect. Okay, let's measure the ESR at 100 kHz here. ESR is equivalent series resistance, and you measure it at 100 kHz is the typical value.

**Dave Jones:** And 0.2 ohms is pretty good. That's a 470 micro 25-V jobby. That seems quite high voltage. It's not 25 V on the output of that DC-to-DC, let me tell you.

**Dave Jones:** But anyway, yeah, that sounds about right. So, what's the other one? It's going to be So, whoa, 7.6 ohms. Well, there's your problem. That one is completely kamikaze. So, let's actually measure the capacitance of that.

**Dave Jones:** And at 100 Hz, there you go, 260 microfarads. It's supposed to be 470. So, yeah, wah wah wah wah. So, I did confirm that both of these were in parallel on the output.

**Dave Jones:** So, usually you've got enough redundancy, well, you should if you're designing a DC-to-DC converter like this, then, you know, you should have some redundancy that like if one of them goes, that it's not going to, you know, it's still going to struggle along, but nope, in this case, which one was it?

**Dave Jones:** Got to measure it again. So, one of them seems fine and one of them's come a cropper. So, that's, yeah, design margin just wasn't there, unfortunately. So, replace these caps, it'll probably come good.

**Dave Jones:** So, assuming that is the fault, just there's a lesson to be learned there in that don't assume just because two caps are in parallel that, oh, the odds of two failing is, you know, pretty low.

**Dave Jones:** No, in this case, looks like only one's failed, so the other one's fine. These are remarkably small caps, low ESR jobbies, 470 mic, Chong X, 25 volts. The nearest I had was in low, well, either in low ESR or even non-low ESR, 470 microfarad 16 volts.

**Dave Jones:** So, normally you shouldn't go for a lower voltage, but I'm pretty sure these are overrated. I don't think this thing is outputting, you know, like even if it's outputting 12 volts, it'll be fine and dandy.

**Dave Jones:** So, and the height's okay. So, I'm just going to have to run with that. Yeah, they're just crazy small. All right, they're soldered back in, they're around the right way, I believe, and let's power it up and see what we get.

**Dave Jones:** And ta-da, 12.6 volts. So, those 16-volt caps will be just fine, and Bob's your uncle. Winner, winner, chicken dinner. All right, it's back together. Let's power it up, and ta-da, yep, yep, new energy.

**Dave Jones:** Winner, winner, chicken dinner. So, there you go, obvious, simple, obvious repair, but I hope you liked the uh, sort of more methodical approach to that. Yeah, we could have just opened this up and said, "Ah, 80% chance it's it's the caps.

**Dave Jones:** Just go check the caps and replace them." But, you know, it's that was a step-by-step, uh, thing just getting down to, well, pretty much it had to be those output caps.

**Dave Jones:** It was basically very unlikely to be like the, uh, TL431, for example. They don't usually, uh, fail. So, you know, the output caps, yep, they just dry out. They got the electrolyte in them.

**Dave Jones:** But, as I said, um, this thing hasn't had a lot of, um, user abuse. So, yeah. Uh, anyway, see the original video teardown. It's, uh, it's not something that I recommend.

**Dave Jones:** It's definitely built down to a price. So, interestingly, did they come a guts up by choosing these 470 microfarad 25 V? They're trying to do a good thing there by choosing, uh, a much larger voltage, more than double the rating of the 12 V output there.

**Dave Jones:** But, were they better off? Because these are so tiny, though, which means all the dimensions in there have to be smaller and, well, you know, it's it's just not going to be potentially as reliable as a larger one.

**Dave Jones:** Were they better off going with the larger 470 mic 16 V, which is, you know, enough rating for a uh, 12 V supply, but physically bigger and it's got more of the electrolyte juice in it, and it might have lasted a bit longer?

**Dave Jones:** But, anyway, it was interesting how we had two of those in parallel and just a partial failure on one of them was enough to come a guts up, and it just got, uh, too much ripple that the, uh, primary side switcher just didn't like that, and it come a guts up.

**Dave Jones:** Anyway, there was enough physical height cuz the transformer was just a little bit higher than these. So, it's not like they stick out. They had the height there, and, um, he chose poorly.

**Dave Jones:** >> He chose poorly. >> Yeah, yeah, all right. You're all screaming at me, "Dave, there's a blowhole in the top of that capacitor." Surely I would have seen that.

**Dave Jones:** No, I didn't. I only saw it on the edit um cuz I was looking at the vent. That's what those marks in there for. This is a vent that if there's overpressure inside, uh then it's going to usually like they burst along that seam.

**Dave Jones:** But, it's almost as if this is some sort of like just manufacturing handling fault, something like that. So, I checked the original video and have a look. Sure enough, it was in the original teardown video as well.

**Dave Jones:** So, this is from the factory because I did that teardown before I'd even powered the thing up for the first time. So, that was a fault from the factory.

**Dave Jones:** So, maybe not from the capacitor factory, maybe it was like the assemblers. They just poked something in there. There's no real damage, is there, to the like outer um sheath on that.

**Dave Jones:** So, yeah, I don't know, but anyway, um that is not an electrical fire. That is an assembly failure or manufacturing failure. Isn't that interesting? But, it worked when I first had it, but you know, it it just dried out over time because well, the thing wasn't sealed anymore and what what what what.

**Dave Jones:** Anyway, if you like that uh repair video, please give it a big thumbs up and as always, discuss down below and you can uh check out the evblog.store. Uh will be closed in like the first half of the new year or something.

**Dave Jones:** Anyway, catch you next time.
