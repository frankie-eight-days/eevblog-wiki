---
video_id: scXuW8KdYkQ
title: EEVblog 1726 - REPAIR of an EV Charger (Unusual Twist!)
url: https://www.youtube.com/watch?v=scXuW8KdYkQ
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 25, "3": 39, "4": 50, "5": 62, "6": 71, "7": 83, "8": 98, "9": 113, "10": 129, "11": 147, "12": 158, "13": 178, "14": 190, "15": 201, "16": 215, "17": 229, "18": 242, "19": 255, "20": 276, "21": 294, "22": 311, "23": 325, "24": 344, "25": 358, "26": 372, "27": 386, "28": 401, "29": 417, "30": 439, "31": 454, "32": 473, "33": 490, "34": 504, "35": 517, "36": 536, "37": 556, "38": 574, "39": 589, "40": 604, "41": 619, "42": 638, "43": 654, "44": 670, "45": 684, "46": 698, "47": 715, "48": 732, "49": 748, "50": 764, "51": 779, "52": 796, "53": 814, "54": 829, "55": 847, "56": 863, "57": 875, "58": 891, "59": 904, "60": 919, "61": 933, "62": 950, "63": 968, "64": 982, "65": 998, "66": 1013, "67": 1035, "68": 1052, "69": 1065, "70": 1079, "71": 1099, "72": 1112, "73": 1126, "74": 1146, "75": 1160, "76": 1174, "77": 1188, "78": 1203, "79": 1216, "80": 1232, "81": 1242, "82": 1255, "83": 1273, "84": 1287, "85": 1304, "86": 1317, "87": 1336, "88": 1351}
---

**Dave Jones:** Hi, do you remember this new energy EV charger in quote marks cuz there's no such thing as an EV charger. It's actually built into the car. It's what's called an EVSE or an electric vehicle supply equipment. But it's basically a

**Dave Jones:** little fancy screen with a relay in there that switches the power through to the car and the car has the charger in it. Anyway, I did a video um teardown of this thing and it wasn't great and I

**Dave Jones:** didn't recommend uh this thing um at all. I'll link in the video if you haven't seen it. But this thing has actually been a few used a few times. Um not by me, by someone else. But uh yeah, it's it's failed. So, I don't

**Dave Jones:** know. It's been used like half a dozen times or something um and it just, you know, periodically and it's just died. I do actually have um power hooked up to it at the uh moment. I've got 240 V

**Dave Jones:** going right up the uh clacker there. Nope. Nope. It's drawing uh some Don't know if you can see that, but it's drawing uh no volts. So, it should actually come up with the screen on the thing. Um and like just, you know,

**Dave Jones:** waiting for the to plug in for the car and everything else and it doesn't. It's deadskis. So, let's crack it open. See if we can see anything. First thing I do is check do we actually get anything up

**Dave Jones:** the uh clacker. This is an Australian uh 32 amp outlet. I've got one of these installed in my garage which uh powers my Zappi and it's 131 K. So, it's not like like there's an input fuse. I don't

**Dave Jones:** actually remember there being an input uh fuse on this thing. So, it's not like the input has popped. There's something there and we'll just go to earth as well and well, we've got eight meg there and open there. So, yeah.

**Dave Jones:** There you have it. Uh as I said, more detailed teardown in the previous video which I'll link in, but uh nothing obvious. Give it a smell. Nothing burnt. It's nothing obvious. And as I said, yeah, I don't think there's

**Dave Jones:** an input fuse. Goes into the relay. Oh, no. No, there we go. Yes, it does have a fuse. It's a little fuse and there's little brown jobby over there. So, I'll check that. Apart from that, the display board looks okay. Nothing doing there,

**Dave Jones:** really. So, it seems otherwise okay. So, let's check that fuse. To get that board out, got to take off all the uh mains connections here and get that out. I love these. These are just these little um press fit connections like that.

**Dave Jones:** That's the uh control wire for um going off uh the pilot wire or whatever it's called going off to the uh EV connector. Wonder if you get the grommets out, too, to try and get the board out. It's a bit

**Dave Jones:** tricky. All right, the board's out. So, our fuse is up there and that, of course, powers all of our via the high voltage um string series resistor uh network there. No. Well, there you go. The plot thickens. And we've got a common mode choke here.

**Dave Jones:** So, I tested the uh resistance of that. So, there's one side here and it's about uh just under 1 ohm and this side's just under 1 ohm. So, our mains input comes from here, goes to one side of the

**Dave Jones:** common mode choke, pops out the other side, and then goes over to the fuse. And we So, we know that common mode uh choke is intact and that fuse is intact. And this side here and this side here is

**Dave Jones:** down to the neutral. So, we know the neutral side is intact there. So, then we've just got an X class uh filter cap uh across the mains. It's X It's X class because it's across the mains. Think of

**Dave Jones:** X as across and Y is goes down to earth. So, Y class capacitor is a capacitor that's from either of the main active or neutral down to earth and the X class is one that's across active and neutral.

**Dave Jones:** So, that'll be an X class cap. And you'll notice that's exactly what's on there X2. There you go. Well, I haven't measured the series resistors. They're one of those could have gone ski, but at least we're getting the voltage to here.

**Dave Jones:** So we're getting nothing on the LCD screen. So it's almost as if it's not getting power. I mean, you know, it could be the screen that's gone, the micro that's gone or something like that, but you know, first rule, thou

**Dave Jones:** shalt measure voltages. Okay, we have 539 K resistors there. So total resistance is there you go, 131. But because that's in circuit, we could have something in parallel with that upsetting the apple cart, but there's something there. Totally forgot chasing a red herring

**Dave Jones:** down a rabbit hole there. Anyway, worth a check. This is actually a current transformer. I'll put up the data sheet for that here. And what we really need to look at is this DC to DC converter over here because that, if you have a

**Dave Jones:** look at the bottom, there you go, that's directly connected there as well. Those caps look intact. The vent holes there look like they're fine. There's no bulging, but yeah, it's built down to cost cuz this is a really el cheapo charger, one of the

**Dave Jones:** cheapest on the market. So it's most probable that that DC to DC converter has failed, I suspect cuz really, you know, there's not much else to go wrong. All right, well, let's measure the output of the DC to DC converter here

**Dave Jones:** and there's your problem. Yes, we are getting 240 V mains in there, but we're getting nothing out on the DC to DC converter. So no surprise that this puppy is not powering up at all. So something's failed on that module. Most

**Dave Jones:** likely cuz as I said, you know, they built this thing for, I don't know, 30 cents, 50 cents, something like that. It's just a module and well, it's coming a gutter. And when you're talking about a fire mode of like the complete screen, just

**Dave Jones:** like it just doesn't power on, then it's very likely to be a power supply issue. It's, you know, it's far less likely to be like the microcontroller at fault, anything on here like this. And that's why the golden rule of troubleshooting

**Dave Jones:** is thou shalt measure voltages. And yep, that's completely coming a gutter. I'm sure the 240 volts is getting in there. It's just the PCB traces straight in. But just for a sanity check, if you're really that interested, there you go.

**Dave Jones:** We're getting our 240 volts directly on the two pins. So, yeah, that module's gonski. There you go. I sucked the module out and there's a sneaky little half tap under here. These are all the same value. So, they're splitting that

**Dave Jones:** in half and then bridge rectifying that here. And they're using that as part of the sensing stuff here for ground faults or whatnot. And looks like we just got a protection diode directly across the positive output of the regulator here.

**Dave Jones:** And there's a little switching converter. I don't see any blow holes. There's the bridge rectifier. It It might have been gonski, but there's no no magic smoke has escaped. So, yeah. And that is a DK 1203 switching controller. I don't know that

**Dave Jones:** one offhand. I'll whack up the data sheet for that. But yeah, there's a opto-isolator between the primary and the secondary there. We've got our capacitive coupling between the primary and secondary. There's our big output diode. Okay, we can just check the

**Dave Jones:** bridge rectifier here. And yep, we should get both of those one diode drop. And then we have to change the probes around. This will be the positive. Yep, there we go, and boom, like that. No worries. Diode bridge is intact. So, we should be

**Dave Jones:** getting a full wave rectified mains voltage across the cap here. Oh, damn. Here's the capacitor. Look at the clearance in there. Look at the Like hello. It's not like they've deliberately done that for a spark gap thing. There's no exposed solder mask

**Dave Jones:** there. Oh my god. Like, you know, who cares about clearance? We'll continue to measure stuff on here because that's the easiest thing to do cuz it's really annoying to like put 240 and dangerous to put 240 volts up to here and then

**Dave Jones:** just start probing around willy-nilly, you know. We have to get out our isolated probe, and then we need like little fine grabbers to like, you know, get onto like individual pins and stuff like that, and it's a real pain. So,

**Dave Jones:** anyway, let's measure the transformer next. Our primary 2.2 It's a bit low. Would have expected 5 to 10 ohms or something like that, but that's okay. Secondary side should be like almost Yeah, almost a short because there's, you know,

**Dave Jones:** the bugger all cuz the turns ratio is going to be small. That flyback transformer seems okayish. I've measured that diode there. It's fine. So, really, there's not much left on there. Um, it's the internal switching transistor is inside the

**Dave Jones:** driver there. And, of course, you're going to give it a visual inspection of the solder joints because these things are heat up, so you can get cracked solder joints, but everything looks pretty hunky-dory on here. Not really seeing any issues with the

**Dave Jones:** solder joints, so can basically rule out a cracked joint cuz that's a not an uncommon failure mode. But that is more to do with like, you know, high power, high current supplies that heat up a lot. This one's,

**Dave Jones:** you know, it it it's pretty wimpy. What is that, you know, a couple of watts? We'll just power this thing up on the bench again and just a sanity check, we will double-check that we're getting yep, absolutely nothing out of that.

**Dave Jones:** Measure the mains filter cap there, unpowered of course, and it's discharging. There you go, no worries. So, it was getting something on there. All right, we'll measure the full wave rectified voltage across the cap there. The safe way to do this is not to

**Dave Jones:** power it up and then probe it, is to get like some easy hooks like this, attach them before you connect it, and then plug it in. So, let's go. And yep, 336 volts, no worries. And you can see that's going to discharge and it'll

**Dave Jones:** take a while, but it'll get there. Or we can just use our low Z thing and that will very nicely discharge it. It'll be already gone. >> [laughter] >> But yeah, it can't even read it. It's so low. There you go, we're down to 1 volt.

**Dave Jones:** Oh, it's rising back up. Ooh, dielectric absorption. All right, it's oscilloscope time and of course you want to be safe. So, we've got the HVP 70 high voltage isolated probe here times 100. We'll set up the scope for times 100 probe input.

**Dave Jones:** And once again, don't go try probing when it's live. I've still got this disconnected, so let's power it up and see what we get, shall we? So, what we're going to measure is directly across the switching transformer there.

**Dave Jones:** That'll do to see if we at least get some sort of switching waveform. All right, so So, plug it in. We're 100 volts per division, see if we get any switching action at all. Oh, there was Well, yeah

**Dave Jones:** there's a little attempt there. There is an attempt. Where is our trigger level? There we go. So, we can single shot capture that. There we go. So, it's attempting. There you go. It is attempting to do something. So, we'll

**Dave Jones:** put normal mode there and we can see that yeah, it's it's it's just every like cup every second or whatever. It's attempting to do some switching. So, but it doesn't like it. She ain't sticking on. So, maybe secondary side regulation

**Dave Jones:** feedback perhaps. So, you can probably see that updating there. It is the same waveform and like every one two every three like every second that is updating. So, it looks like the switching controller is actually working. So, it's getting

**Dave Jones:** voltage, but it's entering some over protection over voltage over current protection hiccup mode. And this is quite common with these switching controllers. I've had a look at the data sheet and it does mention it does have a protection mode like this. It doesn't

**Dave Jones:** mention a second. It mentions like half a second. Um but yeah, still that is looks like we've got a secondary side problem here, not a primary side problem because we're switching that. That's 100 V per division. 100 200 300

**Dave Jones:** We're switching that sucker. No worries, but yeah, it's just not going into regulation and that's what the feedback is on the secondary side with that opto isolator. So, I think we have to investigate the Let's just unplug it here. See what happens.

**Dave Jones:** Ooh, look at that. She's going down. She's still switching. It's still switching. Look at this. >> [laughter] >> It's still going. Wow, those like two microsecond pulses there of current aren't actually discharging that cap hugely fast, are they? So, [laughter]

**Dave Jones:** there you go. Shows how much Oh, oh, what's this lengthening? Look at that. Oh, oh, she stopped. She stopped. There you go. Okay, having a look at the secondary side here. We can see that we've got, of course we do, a classic TL

**Dave Jones:** 431 current shunt reference there and not much else. So, not much else can go wrong here. We will check the secondary side filter cap. We've got our diode secondary side diode over there. But, yeah, there's not much that can go

**Dave Jones:** wrong here. Pretty basic plain vanilla stuff here. So, yeah. Okay, I just want to check the VCC pin, which is pin two there, just to make sure that we're getting a decent voltage. Oh, helps if I put on DC

**Dave Jones:** volts, doesn't it? There we go. I'm 5 volts. No worries. So, the chip's powered up. I've turned the power off and it's still there. Still going. Come on, you can do it. You'll probably find it'll suddenly drop off a cliff

**Dave Jones:** eventually. There we go. There we go. Yep. Oh, it's clinging in there. Well, at this stage, I'd say the fire is most likely to be high ESR in the output caps. I'm not sure if those they're in parallel.

**Dave Jones:** Doesn't look like it. I can measure that, but I think statistically that's most likely and that will lead to excess ripple on the output, even though there's not a huge load on here, I don't think, cuz it's only powering the micro and

**Dave Jones:** the display takes a reasonable amount. Color whiz-bang display takes a reasonable It's got a dot matrix thing on it. It takes a reasonable amount, but any excess ripple in there could actually be triggering the hiccup mode in the

**Dave Jones:** controller here. So, I'm going to I can try and measure those in circuit first, but if not, easy to suck out. Although, having said that, it is trivial to measure the opto primary side of the optocoupler. So, I'm going to go ahead

**Dave Jones:** and do that. Although, having said that, it is pretty trivial to measure the primary side of the optocoupler feedback there. So, I'm just going to probe that. There we go. We're at 2 V per division. I've switched to my probe to 10:1. So,

**Dave Jones:** we are actually getting feedback on that optocoupler. So, that optocoupler is good. That's, as I said, on the primary side. So, the optical part of it's working. The the LED on the primary side of the opto Sorry, well, that's confusing. The

**Dave Jones:** primary side of the optocoupler is actually on the secondary side of the transformer. So, the LED is on the secondary side of the power supply. That's feeding back to the phototransceiver on the primary side. And sure enough, we are actually getting

**Dave Jones:** some switching on there. And that's exactly what you'd expect. Okay, let's measure the ESR at 100 kHz here. ESR is equivalent series resistance, and you measure it at 100 kHz is the typical value. And 0.2 ohms is pretty good.

**Dave Jones:** That's a 470 micro 25-V jobby. That seems quite high voltage. It's not 25 V on the output of that DC-to-DC, let me tell you. But anyway, yeah, that sounds about right. So, what's the other one? It's going to be

**Dave Jones:** So, whoa, 7.6 ohms. Well, there's your problem. That one is completely kamikaze. So, let's actually measure the capacitance of that. And at 100 Hz, there you go, 260 microfarads. It's supposed to be 470. So, yeah, wah wah wah wah. So, I did

**Dave Jones:** confirm that both of these were in parallel on the output. So, usually you've got enough redundancy, well, you should if you're designing a DC-to-DC converter like this, then, you know, you should have some redundancy that like if one of them goes, that it's not going

**Dave Jones:** to, you know, it's still going to struggle along, but nope, in this case, which one was it? Got to measure it again. So, one of them seems fine and one of them's come a cropper. So, that's, yeah, design margin just wasn't

**Dave Jones:** there, unfortunately. So, replace these caps, it'll probably come good. So, assuming that is the fault, just there's a lesson to be learned there in that don't assume just because two caps are in parallel that, oh, the odds of two failing is, you know, pretty

**Dave Jones:** low. No, in this case, looks like only one's failed, so the other one's fine. These are remarkably small caps, low ESR jobbies, 470 mic, Chong X, 25 volts. The nearest I had was in low, well, either in low ESR or even non-low ESR,

**Dave Jones:** 470 microfarad 16 volts. So, normally you shouldn't go for a lower voltage, but I'm pretty sure these are overrated. I don't think this thing is outputting, you know, like even if it's outputting 12 volts, it'll be fine and dandy. So,

**Dave Jones:** and the height's okay. So, I'm just going to have to run with that. Yeah, they're just crazy small. All right, they're soldered back in, they're around the right way, I believe, and let's power it up and see what we get.

**Dave Jones:** And ta-da, 12.6 volts. So, those 16-volt caps will be just fine, and Bob's your uncle. Winner, winner, chicken dinner. All right, it's back together. Let's power it up, and ta-da, yep, yep, new energy. Winner, winner, chicken dinner. So, there you

**Dave Jones:** go, obvious, simple, obvious repair, but I hope you liked the uh, sort of more methodical approach to that. Yeah, we could have just opened this up and said, "Ah, 80% chance it's it's the caps. Just go check the caps and replace them."

**Dave Jones:** But, you know, it's that was a step-by-step, uh, thing just getting down to, well, pretty much it had to be those output caps. It was basically very unlikely to be like the, uh, TL431, for example. They don't usually, uh, fail.

**Dave Jones:** So, you know, the output caps, yep, they just dry out. They got the electrolyte in them. But, as I said, um, this thing hasn't had a lot of, um, user abuse. So, yeah. Uh, anyway, see the original video teardown. It's,

**Dave Jones:** uh, it's not something that I recommend. It's definitely built down to a price. So, interestingly, did they come a guts up by choosing these 470 microfarad 25 V? They're trying to do a good thing there by choosing, uh, a much larger voltage,

**Dave Jones:** more than double the rating of the 12 V output there. But, were they better off? Because these are so tiny, though, which means all the dimensions in there have to be smaller and, well, you know, it's it's just not going to be potentially as

**Dave Jones:** reliable as a larger one. Were they better off going with the larger 470 mic 16 V, which is, you know, enough rating for a uh, 12 V supply, but physically bigger and it's got more of the electrolyte juice in it, and it might

**Dave Jones:** have lasted a bit longer? But, anyway, it was interesting how we had two of those in parallel and just a partial failure on one of them was enough to come a guts up, and it just got, uh, too

**Dave Jones:** much ripple that the, uh, primary side switcher just didn't like that, and it come a guts up. Anyway, there was enough physical height cuz the transformer was just a little bit higher than these. So, it's not like they stick out. They had

**Dave Jones:** the height there, and, um, he chose poorly. >> He chose poorly. >> Yeah, yeah, all right. You're all screaming at me, "Dave, there's a blowhole in the top of that capacitor." Surely I would have seen that. No, I

**Dave Jones:** didn't. I only saw it on the edit um cuz I was looking at the vent. That's what those marks in there for. This is a vent that if there's overpressure inside, uh then it's going to usually like they

**Dave Jones:** burst along that seam. But, it's almost as if this is some sort of like just manufacturing handling fault, something like that. So, I checked the original video and have a look. Sure enough, it was in the original teardown video as

**Dave Jones:** well. So, this is from the factory because I did that teardown before I'd even powered the thing up for the first time. So, that was a fault from the factory. So, maybe not from the capacitor factory, maybe it was like the

**Dave Jones:** assemblers. They just poked something in there. There's no real damage, is there, to the like outer um sheath on that. So, yeah, I don't know, but anyway, um that is not an electrical fire. That is an assembly failure or manufacturing failure. Isn't

**Dave Jones:** that interesting? But, it worked when I first had it, but you know, it it just dried out over time because well, the thing wasn't sealed anymore and what what what what. Anyway, if you like that uh repair video, please give it a big thumbs up

**Dave Jones:** and as always, discuss down below and you can uh check out the evblog.store. Uh will be closed in like the first half of the new year or something. Anyway, catch you next time.
