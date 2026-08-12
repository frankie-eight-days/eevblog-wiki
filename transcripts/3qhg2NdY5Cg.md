---
video_id: 3qhg2NdY5Cg
title: EEVblog 1452 - Fluke PM3370B Combiscope REPAIR
url: https://www.youtube.com/watch?v=3qhg2NdY5Cg
source: youtube-asr
timestamps: {"0": 0, "1": 19, "2": 34, "3": 45, "4": 66, "5": 80, "6": 95, "7": 107, "8": 119, "9": 128, "10": 144, "11": 155, "12": 170, "13": 183, "14": 194, "15": 204, "16": 218, "17": 229, "18": 245, "19": 262, "20": 286, "21": 295, "22": 310, "23": 330, "24": 342, "25": 356, "26": 374, "27": 386, "28": 400, "29": 413, "30": 425, "31": 437, "32": 445, "33": 465, "34": 479, "35": 495, "36": 505, "37": 522, "38": 534, "39": 558, "40": 567, "41": 576, "42": 588, "43": 600, "44": 610, "45": 618, "46": 627, "47": 635, "48": 648, "49": 657, "50": 668, "51": 679, "52": 698, "53": 714, "54": 726, "55": 737, "56": 756, "57": 775, "58": 789, "59": 808, "60": 823, "61": 835, "62": 855, "63": 864, "64": 880, "65": 889, "66": 906, "67": 917, "68": 931, "69": 941, "70": 957, "71": 972, "72": 987, "73": 1000, "74": 1012, "75": 1032, "76": 1046, "77": 1056, "78": 1068, "79": 1090, "80": 1110, "81": 1127, "82": 1148, "83": 1155, "84": 1172, "85": 1187, "86": 1206, "87": 1213, "88": 1228, "89": 1237, "90": 1251, "91": 1271, "92": 1292, "93": 1303, "94": 1323, "95": 1344, "96": 1363, "97": 1374, "98": 1385, "99": 1397, "100": 1406, "101": 1421, "102": 1440, "103": 1454, "104": 1467, "105": 1482, "106": 1495, "107": 1510, "108": 1529, "109": 1539, "110": 1549, "111": 1566, "112": 1584, "113": 1597, "114": 1610, "115": 1622, "116": 1636, "117": 1647, "118": 1655, "119": 1667, "120": 1679, "121": 1695}
---

**Dave Jones:** Hi, in the previous video we took a look at this Fluke PM3370B that I scored on eBay for 99 bucks and it was almost a winner winner chicken dinner except that after about 5 minutes it would just power down and the screen would just go and actually collapse.

**Dave Jones:** So obviously something's happening with the like the high voltage EHT aspect of it or at least you know, that's one of the things um that's involved here. So let's have a troubleshoot of this thing and see if we can find the culprit, shall we?

**Dave Jones:** So obviously it's going to be power supply related. So we're having a look at the power supply board here which is you know, a fairly complicated little beast. We've got our mains input here.

**Dave Jones:** There's no refer caps on the input. We've got a full wave PTC. We've got a full wave bridge rectifier. We've got the the high mains high voltage caps, common mode choke and then primary side uh switching here and our main switching transformer and then a big secondary side and look at all those Nippon Chemicon caps.

**Dave Jones:** Oh, beautiful. Now the first thing you might suspect of course is the caps. You know, electrolytic caps famous for failing especially on a 20 year old scope. But unfortunately that doesn't really fit the symptoms.

**Dave Jones:** Like it works absolutely perfect for 5 minutes and then switches off and then restarts immediately when you uh power it back on and then 5 minutes. So you know, like when you have something that fails after 5 minutes like that's sort of like reasonably consistent.

**Dave Jones:** You're looking at more of like the thermal side of things. You know, I've I've done a video before repairing a oscilloscope where spoiler alert like one of the diodes actually had an internal thermal failure.

**Dave Jones:** After a set amount of time it was actually dying internal to the diode. Like the junction in there like the bond wires or whatever inside was like, you know, failing thermally when it heated up.

**Dave Jones:** To analyze this, yeah, you might go around with your freezer spray and stuff like that and start playing around with stuff, but of course the first thing you want to do is a visual inspection.

**Dave Jones:** And I won't bore you with the details, but I cannot find anything visual on here in terms of, you know, leaking caps or anything like that, any components that have heated up, diodes that have gone brown, resistors that have overheated or anything like that.

**Dave Jones:** There's no blow holes in any of the parts. So, I cannot find anything visual on this thing at all. And that includes the bottom side surface mount parts as well.

**Dave Jones:** You can see like the solder thieving on those larger pads. This means that this thing has been reflow soldered, which is, you know, fairly common for these primary secondary side surface mount parts.

**Dave Jones:** And I've also gone around and looked at the solder joints, for example, like a classic thermal problem might be a dry joint. And once the component heats up, then that actually causes, you know, the component to expand slightly and the joint actually breaks.

**Dave Jones:** And I've gone around and, you know, like the through hole ones will be the classic for this, you know, large components, large like, you know, power components and stuff like that.

**Dave Jones:** But I've gone around the board. I can't see any dry joints on this thing at all. So, I'm going to rule that out for this stage, anyway. So, step two would be measuring the diodes.

**Dave Jones:** And I've gone and done that, so I'll spare the boring details, but yeah, I could not find any failed diodes at all. But as I said, this is more like a thermal thing after 5 minutes kind of problem.

**Dave Jones:** That's what it sort of indicates. So, just measuring the diodes on the board like this, I didn't expect to find anything and I didn't. The only component that that seemed to be open was this one here.

**Dave Jones:** And I suspect what it might be, but we might have to verify that with the schematics. I think that's a high voltage diode. Some commenters in the previous video mentioned the EHT section, and this is the tripler here.

**Dave Jones:** Obviously, this is our EHT driver transformer here, which will generate the anode voltage, and then that goes into the tripler here, and that will drive however many kilovolts are required for the CRT and that goes up to that's the nasty don't touchy in the CRT.

**Dave Jones:** There it is. So, but it's all discharged now. Everything's hunky-dory, but some people, a couple of people in the comments said, "Yeah, these Philips scopes, they are actually famous for having the tripler like arc over and fail, and then print some protection circuitry kicks in or something like that." But anyway, let's jump over to the schematics, see what we can see, just get a bit more background info

**Dave Jones:** before we start prodding and poking this thing. Unfortunately, there are no test points. So, once this thing gets plugged in, you know, it's not easy to like access stuff in there.

**Dave Jones:** So, it would have been nice if they had like various, you know, test points along the top that you could just probe. So, yeah, that could be annoying. If we get desperate, attach probes that the wires that then come out and then attach the probes later.

**Dave Jones:** Let's hope we don't have to resort to that though. And some commenters also talked about upgrading the memory on this thing, and here's this sample memory. There's eight of these, four on the other side, and these are 2K high-speed SRAMs, and you'll notice that there's an extra two pins on each one of those, an extra footprint.

**Dave Jones:** And you might even notice up here, tada, jumper links. 32K / 2K. These are 2K chips, and these are 8K chips over here to give you like 32K of sample memory.

**Dave Jones:** In theory, I think it's probably possible to simply move these jumpers over here and then populate these with the larger part and I have checked the manual and it does actually have the part number for the 38K parts instead of the 32K parts.

**Dave Jones:** So, in theory that's possible but you know, I maybe. But anyway, that's not for this video. We have the service manual here dates from 2000. It's very comprehensive. Only 478 pages.

**Dave Jones:** So, hats off. Unfortunately, it doesn't give a page number. It gives a section number. First section that's of interest to us is like the main system block diagram here.

**Dave Jones:** So, like we've got the front panel board here. We've got the main processor unit. This looks like the motherboard, the base motherboard or whatever. We've got a CRT of course and then we've got this looks like that's our power supply board over there.

**Dave Jones:** So, that's one of the things we're interested in. Shouldn't really have anything to do with the drive section. I think the EHT when you saw that thing actually collapse, that's an EHT high voltage EHT is extra high tension.

**Dave Jones:** That's a classic thing of where the EHT is dropping down and then the capacitors goes and all your image just collapses. Like it's not like the XY drive or anything like that.

**Dave Jones:** So, our power supply board is pretty basic stuff. We've got a line filter here. We've got our bridge rectifier there. There's a 10 volt voltage reference. There's our flyback transformer and and then the rectifier and then the 5 volt regulator.

**Dave Jones:** It's got to have more than that. It can't just be 5 volt output. There's got to be tons of rails specially for the analog and digital and all that.

**Dave Jones:** Anyway, there is a protection circuit cuz some people mentioned the protection circuit like shutting it down. So, it does actually have a power fail output but I suspect that's just going off to the processor so that it tells the processor Oh, power's failing quick, save your settings to your non-volatile RAM and stuff like that.

**Dave Jones:** There's a temperature overload going down into that. I'm not really concerned with that at this stage. I think there's something else. So, the output from that comes into here and that goes into our EHT converter.

**Dave Jones:** Aha, and that gives our negative 2.2 kV there. That'll be our anode voltage and then 6.3 V, that's classic voltage for the heater, the filament heater. And then there's our tripler, the high voltage multiplier as they call it, and then that goes off.

**Dave Jones:** That goes off, follow the money, follow the money as Deep Throat says. And then here's our graticule, yep. And so that gives us 14 kV. Okay, so that's what we're dealing with.

**Dave Jones:** Yeah, there's the 2.2 kV there. That's the anode voltage. I've got a 5 kV probe, so we could actually measure that. We're not going to be able to measure the 14 kV output of the tripler, which some people might have suspected it is.

**Dave Jones:** Okay, we've got our mains input here. Here's our bridge rectifier input varistor. So, yeah, like there's no bad reefer caps or anything like that. So, it's nothing to do with that and that doesn't fit the symptoms.

**Dave Jones:** But anyway, so this is our primary drive side here. Here's our transformer here. So, it's all switching. One thing I want to do when I put this back together is first thing I would check for is whether or not the processor is still operational, like all of the main digital power supplies are still up and whether or not it's just an EHT failure.

**Dave Jones:** So, I can probably get that by just once I put it back together just operating the controls and see if it like still responds to the rotary encoders and stuff like that cuz you can hear the click click click.

**Dave Jones:** And if all that still works, I don't even have to measure voltages to know that the digital section is still working. I should be able to get some sort of, you know, tactile um from that.

**Dave Jones:** Anyway, I'm not seeing anything in here that would shut it down. There's the feedback, of course, coming via the optocoupler here, but uh no, here we go. Here's our EHT converter here.

**Dave Jones:** There's a signal coming in here. Okay, so that that actually could shut it down, I guess. I won't go through the whole topology there, but yeah, does that come from the processor?

**Dave Jones:** I don't know. I might have to RTFM a bit further. Um but anyway, we've got 58 V high voltage there. So, you know, we can measure that point um after it fails, of course.

**Dave Jones:** The whole idea is that you want to hook up uh meters. This is where I've showed in previous uh oscilloscope troubleshooting videos. I think it was the where that diode one went.

**Dave Jones:** I had like four or five multimeters set up um just to monitor all the rails cuz I knew one of the rails was dropping after, you know, 5 or 10 minutes.

**Dave Jones:** This is a similar sort of thing. So, why you need more than one multimeter? This is one of the things you might have to measure, like, you know, several things at once.

**Dave Jones:** You don't want to get in there and start probing around cuz there's dangerous voltages and everything. So, you want to like attach all your probes first and then um have them all coming out to various meters, and then you can measure them all at once and just see where one uh drops out.

**Dave Jones:** So, 58 V HT, you know, if that's not happening, then uh then your high voltage stuff over here is not going to happen. We've got switching transistor down here.

**Dave Jones:** Um you know, so any of that fails, you know, so it could be, you know, I wouldn't rule out like a transistor failing thermally. I wouldn't rule out like diodes failing thermally.

**Dave Jones:** So, here's our tube EHT over here. It's 14 kV here. So, this is our tripler. So, that takes, yep, sure enough, five. That's why they call it a tripler, five to 14.

**Dave Jones:** It's near enough. Um so, we get our 5 kV here. So, this is our main this is our EHT well, EHT converter, as they call it. So, we've got a single diode here, and that um creates minus uh volts, which then is smoothed out by these to give us well, minus 2200 smooth out not switching.

**Dave Jones:** I'd more likely suggest like thermal fires in diodes or in here or something um because there's diodes inside these high voltage multipliers um here, but somebody mentioned that these actually contain reefer caps in them and they can arc over and that sort of stuff.

**Dave Jones:** I wouldn't rule that out. Here here's all the rails, so we've got plus five, minus five, yep. Minus five, uh plus minus 58, minus 12, minus 18, yep, plus 18, plus 12, yep, yep, yep, yep.

**Dave Jones:** So, there's lots of lots of voltage rails there, but I wouldn't be suspecting those. I reckon, you know, there there's there's something in this um EHT high voltage section.

**Dave Jones:** Yes, I think this is that component that was open, but I'm I'm going to look up that uh BYB412. Almost bingo. Um I I searched for that and I got this BY8400.

**Dave Jones:** Whether or not that's a schematic error because this is exactly what you this is the exact diode you would have. Anyway, this is these are interesting beasts. So, these are temperature high temperature high voltage parts and they're specifically for color televisions and monitors, high voltage applications for multipliers, slot wound diodes, split transformers.

**Dave Jones:** So, it uses a high temperature alloy construction. This package is hermetically sealed and fatigue free as coefficients of expansion of all used parts are matched. Interesting, the package is designed to be used in an insulating medium such as resin oil or SF6 gas.

**Dave Jones:** So, they're designed to be like potted. So, the BY8412, yeah, we're talking 14 kilovolts, although it's only used in the two kilovolt section. So, here's the interesting bit and probably why I couldn't measure to because the BY8412 has a forward voltage.

**Dave Jones:** This is a forward voltage. You're used to 0.6 volts on your diodes. Uh-uh. These are special snowflakes. They This has a forward voltage of a maximum 52 volts. It doesn't even tell you what the typical is.

**Dave Jones:** But that's at 100 milliamps. So look, a forward voltage going up to like 45 volts. Unbelievable. So our multimeter is only going to push like a couple of milliamps through there top.

**Dave Jones:** So we're like we're down here. So we don't even know what we're going to measure. I will retry that with the 121GW. Next logical step is to reassemble it um and then check as I said to see if the digital section is still up and running when the if it's just contained to the EHT section.

**Dave Jones:** And then that will rule out if it's a primary side mains thing uh that's it could be primary side mains, but I remember hearing a high frequency hum when it switched off.

**Dave Jones:** So all these things are important. Like all these symptoms that you get, they direct where you're going to shift your focus in the troubleshooting. So in this particular case, I know it's not like it you know failed ESR and failed electrolytic cap uh in the primary side for example.

**Dave Jones:** That's just that's just not the symptom. Something heating up or building up charge that then arcs over or something like that. It's something in the high voltage side of things.

**Dave Jones:** So I'd be very surprised if it had say multiple faults. But it is possible that there is say a problem with a one of the digital supplies and then that causes the EHT that we remember we saw that that EHT driver line coming in or or something like that.

**Dave Jones:** So it could be so the digital could could be failing and then shutting down the EHT and stuff like that. But yeah, that's why we need to check um if this thing's still operational and doing stuff.

**Dave Jones:** So let's go back, reassemble it. So there's that little sucker down there. It doesn't look like any diode that you have ever seen. It almost looks like shriveled up or something, like a little sausage or something.

**Dave Jones:** So, if we measure that, let's get in there. I think I've got that around the right way. But, if I haven't, let's swap it. And you'll notice that that is open.

**Dave Jones:** And if we get ohms on that, there's something there, 30 meg or something. And open the other direction. That's interesting. So, but if we get a 121 GW, that has a 15-V compliance voltage, 10.7 V they are.

**Dave Jones:** And of course, in the other direction, we'll get zippity-doo-dah. There you go. So, if you didn't have a higher voltage diode tester, then you wouldn't be able to test something like that.

**Dave Jones:** What a sneaky little bugger. You might think that's open, and you could chase a red herring down a rabbit hole thinking that that diode is no good. Of course, you could physically or lift one leg and then hook it up to your power supply and and put some current through it and test it that way, of course.

**Dave Jones:** Those things are annoying to test. But, using a regular meter, you would think that's busted any day of the week. So, you got to be careful. I've got my 5-kV high-voltage probe here, which is 100:1.

**Dave Jones:** So, I set up my scope with a 100:1 division ratio on 500 V per division, and we know it's -2200 V. All right, so let's power it up. It's on.

**Dave Jones:** Hey, -2200 V. We're good. All I've got to do now is wait. So, I'll wait for it to fail, and then if this doesn't go back, if this doesn't collapse at 2200 V, then we know it's just the tripler arcing over, almost certainly.

**Dave Jones:** So, I can hear the clicks as that process that your knob. So, when this thing fails, assuming it's going to fail, Murphy's going to give me a break, then if we can hear still hear that, it means that almost certainly all the digital rails, they're all still working.

**Dave Jones:** You wouldn't believe it. I JUST PRESSED STOP. LIKE I WAS GOING TO GO for another clip and it just happened. No, the digital rotary encoder, that's dropped down to zero.

**Dave Jones:** Everything's gone. So, the whole thing's gone. So, damn it. We're going to have to probe um further. Okay, I've got some more probes hooked up now. All right. So, what I've got here is the yellow one, our uh 2.2 kilovolts.

**Dave Jones:** Then we've got the green one, channel two, that's at uh 20 volts per division. That's our 58-volt rail there. And the blue one, that's our 12-volt rail there. So, I'm measuring the three different rails on here, the 58-volt, the uh 2.2 kilovolts, which actually gets back uh fed back here, by the way.

**Dave Jones:** I just noticed that. And the uh 12-volt here. I'd like to probe this power HT input, but unfortunately, that's a surface-mount. Uh there's both surface-mount devices on the back side of the board and the back bottom side of the board is right down in there, right down the bottom.

**Dave Jones:** So, you can't probe that and the board has to be in there, unless you've got like service extender cards, um there's nothing you can do about it. If you got desperate enough, of course, you have to take the board out, then you which is a pain in the ass, then you've got to solder wires on and then you've got to have them coming out and then you've got to probe

**Dave Jones:** everything and well, we're not there yet. Okay, so I've set this up to trigger when the 2200-volt rail, when it actually collapses uh like we saw before. So, I've got my uh trigger source set to either slope there, just so that you don't do a brain fart and cuz it's got a it's negative voltage, so it's transitioning high.

**Dave Jones:** Hey, we got it. There we go. I did actually turn it back to uh 10 milliseconds per division. I think I should have done it slower than that, but uh that was our 12-V rail.

**Dave Jones:** That's uh dropping, so our 12-V rail's switching off. Wow. That's interesting. Uh the trans- Oh, that high-pitched squeal is annoying. So, I'm going to switch that off. That we triggered on our uh 2.2 kV.

**Dave Jones:** So, as that transition up, you can see it hit the uh trigger point there, but you can see the 12-V that was already decaying. That was starting to decay before that, but interestingly, the 58-V rail has been zero all that time.

**Dave Jones:** So, it looks like that 58-V HT rail there is dying uh before we actually get um our 2.2 V kilovolts shutting off. And of course, if this dies, then there's no switching.

**Dave Jones:** There's no voltage for uh the primary side switching. And then, of course, if this This would fail first, and then this would fail after. Hoy, we're getting somewhere, I think.

**Dave Jones:** I could now set my trigger point on there if I really wanted to uh capture that 58-V uh rail failing. Why not? I'll actually wind that back to like 100 milliseconds uh per division, and I'll just leave that set up.

**Dave Jones:** All right, got it. Uh then don't worry about like any sort of like little rises like that. Probing's not perfect on this. I'm using mains earth grounding for this sort of thing.

**Dave Jones:** I don't actually have uh the ground leads from the any of these probes actually hooked up to these boards. It's going via the mains earth here and going back to the power strip under the floor here and going back.

**Dave Jones:** So, you know, that's just for ease. Like, we're not looking at signal integrity here. Our 58-V rail has plummeted. Once that starts happening, yeah, of course, then our 2.2 kV rail starts then decaying or negative 2.2 kilovolts starts decaying and our 12 volt is decaying as well.

**Dave Jones:** So yeah, that sudden drop on your 58 volts, that'll definitely do it cuz there's no more volts to switch. So yeah, no more high tension. So looking at the schematic here, this is the point where we're measuring plus 58 volts VHT, which is interesting cuz I can't yet find that anywhere else in the circuit.

**Dave Jones:** It just says plus 58 volts. It doesn't have the HT on the end of it. So I don't know if that's after some sort of switching element somewhere else in the schematic I haven't found yet.

**Dave Jones:** The signal was coming from like power HT here. If this was like shutting off this switching, then it wouldn't I would expect it wouldn't shut off the 58 volts rail, the 58 volt rail would be there and it'd simply switch off all the the switching transistor here and it just wouldn't switch.

**Dave Jones:** But our power rails actually failing. So either there's a switching there or somewhere else in the schematic or if that's coming directly from the switching transformer, then it could actually be the primary side switcher failing because we saw that the 12 volt rail was also failing as well and this 12 volt rail is in here.

**Dave Jones:** That's why I was measuring the 12, the primary side of the mains which then generates this 58 volts and 12 volt VHT on the secondary side. So if both of these are failing, maybe we have to go back and look at the actual primary side main switcher.

**Dave Jones:** Okay, the answer is always more probes. So I've got two different high voltage differential probes now doing the primary side. Okay, so there we go. We've got some primary side switching.

**Dave Jones:** The red one there is our mains input DC. That's at 100 volts uh division, 330 odd volts, something like that. And we'll wait for it to drop out again.

**Dave Jones:** Let's just uh rearrange those a little bit. Hey, I got it. And there you go. That's interesting. Yeah, the primary side is still switching but at a much lower rate, like 2 kHz.

**Dave Jones:** That's why I can hear that 2 kHz buzz. Yeah, you know, it's roughly 2 kHz odd, whereas I didn't can't remember what frequency it was before but it was much higher.

**Dave Jones:** Primary side uh failed but you can see that the mains DC is still there, so it's not any of the primary rectification diodes failing or anything like that. So, I'll switch that off now and um wait, there we go.

**Dave Jones:** So, that means all this goodness here, we were looking at the switching across this diode here cuz it was a convenient uh location. And um yeah, it just it dropped in frequency and um that would affect all of the outputs, which are all of the outputs here, which are, you know, all of your voltage rails.

**Dave Jones:** So, everything's dropping. So, um in that includes your EHT. So, uh looks like um people who uh suspected that it was like the uh tripler failing and stuff like that, it doesn't seem to be.

**Dave Jones:** It's like something in the primary side of the mains switching that's going. Hmm. Well, this is interesting. It's been running for 31 minutes. Never had it go nearly this long.

**Dave Jones:** What I did is I actually resoldered um I I reinspected it all, couldn't find anything. So, I thought I'd resoldered all like the power uh components anyway and I put it back together and it failed after about 4 and 1/2 minutes.

**Dave Jones:** But uh and then I thought, "Hmm, I'll time this um to see like, you know, if it's like if it's fairly repeatable or not." And sure enough, the second time I do it, it's still been going 32 minutes.

**Dave Jones:** So, I don't know what the heck's going on. Anyway, it's 10:00 p.m. I'm going home. Well, I've come back the next day, 3 hours and 44 minutes later. Um I powered it up this morning and it's still going.

**Dave Jones:** So, it's not very bright, but yeah, it's still going. Has not conked it since the very first time that I put it back together. So, really, you can only deem this fixed um at this point cuz there's nothing there's no failure that like to speak of that you can troubleshoot any further.

**Dave Jones:** So, I think the next step is um to basically put the lid back on, seal it all up so it's a bit warmer inside and maybe, you know, it things might heat up in there or something like that.

**Dave Jones:** So, I don't know. That's it's got to be the next step. So, if I put the lid on, everything works, and I leave it powered up for days, you know, a day or something, and it doesn't fail, then well, like what's left?

**Dave Jones:** I can kind of Maybe I can freeze some stuff again to try and induce failure, but it fails after turning on, which indicates that there's a heat thing, but of course, doing thermal stressing and stuff like that might be able to induce some failures, but there's like there's nothing I can do at this point.

**Dave Jones:** So, yeah, I'll put it back together. So, maybe there's a component that's like was dodgy, but it's now healed itself maybe after some thermal stressing cuz what I've done is I I did freeze the active diodes and some other active components.

**Dave Jones:** I measured them just to make sure, you know, like they didn't go open. I've measured the ESR of every cap on there in circuit ESR. It's a bit of trouble to actually remove everyone, but I've done those in circuit and they all seem fine.

**Dave Jones:** Everything looks visually perfect. I've resoldered a lot of the well, all the major power components like the transformers and the devices connected to the heat sink like some of the you know, power switching transistors and stuff like that.

**Dave Jones:** So, I've done I I I've done those, but as I said, first time I powered it up, it failed. But then, after that, boom, it's like it it seems rock solid.

**Dave Jones:** So, anyway, I there's nothing more I can do. So, this unfortunately is going to have to conclude part one. And this is just like the nature of uh troubleshooting stuff like this.

**Dave Jones:** Um if there's no fault, then unless you can induce it to come back, then you know, you can only speculate. Of course, I can come up with, you know, half a dozen different theories about what could cause something like this.

**Dave Jones:** And please, if you've got your favorite theory, leave it in the comments down below. I'll link in the schematic and service manual down below, so you can have a look yourself.

**Dave Jones:** But it does seem to be something at least isolated to the primary side of uh the mains uh part of it. So, yeah, I don't know. Leave your favorite theory in the comments down below.

**Dave Jones:** But anyway, it's about the journey. So, I hope you found that interesting. So, at this stage, it's fixed until part two. Anyway, I hope you found something useful in that video.

**Dave Jones:** Catch you next time. Nope, the bloody thing won't fail. I've had it going for an hour and almost 2 hours now um with the case on, and it does actually get quite uh warm on top, but not nothing.

**Dave Jones:** So, I
