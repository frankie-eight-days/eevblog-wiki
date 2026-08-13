---
video_id: OgsWOHdDn2w
title: EEVblog #812 - Varta 15min NiMH Charger Part 2
url: https://www.youtube.com/watch?v=OgsWOHdDn2w
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 22, "2": 41, "3": 57, "4": 78, "5": 95, "6": 114, "7": 130, "8": 144, "9": 165, "10": 180, "11": 196, "12": 210, "13": 224, "14": 249, "15": 262, "16": 277, "17": 291, "18": 306, "19": 322, "20": 338, "21": 356, "22": 372, "23": 388, "24": 404, "25": 424, "26": 438, "27": 450, "28": 462, "29": 478, "30": 492, "31": 508, "32": 526, "33": 548, "34": 568, "35": 584, "36": 602, "37": 624, "38": 640, "39": 658, "40": 678, "41": 696, "42": 716, "43": 738, "44": 752, "45": 766, "46": 784, "47": 802, "48": 822, "49": 838, "50": 854, "51": 872, "52": 888, "53": 902, "54": 916, "55": 934, "56": 948, "57": 978, "58": 994, "59": 1016, "60": 1034, "61": 1048, "62": 1068, "63": 1088, "64": 1106, "65": 1120, "66": 1140, "67": 1158, "68": 1172, "69": 1190, "70": 1204, "71": 1218, "72": 1234, "73": 1246, "74": 1262, "75": 1280, "76": 1296, "77": 1316, "78": 1330, "79": 1348, "80": 1364, "81": 1380, "82": 1396, "83": 1412, "84": 1426, "85": 1446, "86": 1462, "87": 1476, "88": 1490, "89": 1506, "90": 1520, "91": 1536, "92": 1554, "93": 1572, "94": 1594, "95": 1616, "96": 1630, "97": 1646, "98": 1660, "99": 1680, "100": 1692, "101": 1708, "102": 1724, "103": 1748, "104": 1766, "105": 1782, "106": 1802, "107": 1822, "108": 1846, "109": 1862, "110": 1880, "111": 1896, "112": 1912, "113": 1924, "114": 1948, "115": 1962, "116": 1978, "117": 1994, "118": 2014, "119": 2028, "120": 2046, "121": 2064, "122": 2078, "123": 2094, "124": 2110, "125": 2126, "126": 2140, "127": 2160, "128": 2178, "129": 2194, "130": 2204, "131": 2218, "132": 2230, "133": 2244}
---

**Dave Jones:** Hi, just a quick follow-up on this Vata 15 minute nickel metal hydride battery charger I looked at in the previous video. Did a tear down and kind of reverse-engineered the main switching topology and charging circuit for the batteries and things like that. And a lot of people wanted me to follow-up and actually probe this thing and see what's happening here,

**Dave Jones:** because one of the outstanding issues from last time I didn't have time to look at is how they're actually measuring the discharge current for this thing. We knew that the DC to DC converter was basically putting all the batteries in series and there was a measurement shunt resistor down the bottom down here.

**Dave Jones:** And we also knew that by nature of this dual MOSFET configuration for each battery cell here, so here's each battery and there's a pair of MOSFETs across each one. And let me show you the switching arrangement, how they can switch cells in and out,

**Dave Jones:** depending on which of these MOSFETs they turn on. So if you turn on the top one here, for example, then you're going to charge the battery. Okay, so it's going to go through there and around down to there. But if you turn the bottom one on, you can completely bypass that.

**Dave Jones:** Boom, and go straight down to the next one. So effectively they can switch in and out any one of these cells depending on the arrangement of these MOSFETs here. And it's rather clever actually, I like it. It's a nice implementation. Now for this example,

**Dave Jones:** if you have this MOSFET here, the lower MOSFET turned on, and you're bypassing this cell, what happens if you actually plug in the cell? Well, nothing, because the body diode inside here, okay, will actually be reverse biased. So the battery, this is the negative terminal of the battery, positive terminal's up here,

**Dave Jones:** so the cathode of the body diode here is going to be positive with respect to the anode here. So therefore the body diode is reverse biased, and because you haven't turned the gate on, that gate voltage is zero because it's an n-channel MOSFET,

**Dave Jones:** then no current is going to flow out of the battery at all, and all you've got over here is just a sense line. So bingo, you just alternate between those two FETs, and you can turn each individual cell off and on. Same here, if you turn this one on, you can bypass it.

**Dave Jones:** Now let's say you only plugged in this battery here, for example, then, okay, then it would detect that there's a voltage on here, so the microcontroller through the analog-to-digital converter is always checking these sense lines here, and it detects, ooh, you just plugged in that battery, okay, I will switch on this MOSFET,

**Dave Jones:** and bingo, we'll charge that battery. And then nothing plugged into the bottom one, so we'll turn on this FET, and bingo, current flows down through the current shut resistor, and we can measure it. Now of course, one thing we don't know is how they're actually doing the discharge.

**Dave Jones:** Let's say you had battery plugged into this third position over here, and it detected it, okay, but you put it in discharge mode, because it's got various, it's got charge mode, discharge mode, it's also got test mode as well, which will discharge the battery

**Dave Jones:** and then charge it so it can measure the battery capacity, get the accumulated charge. But, you know, if you turn both of these MOSFETs on, then, well, you're just going to short out your battery like that. And, well, you know, that's no good.

**Dave Jones:** You need to have, how are they actually measuring it? Because we, in the teardown of this thing, I couldn't really find any current sense resistor, so they must actually be switching it on, and possibly using this current shut resistor down here like this.

**Dave Jones:** So they might be actually discharging them all in series, just like they're charging them all in series, and then calculating the discharge current based on the differential sense voltage across the cell here. Because you'll notice here, if we go into discharge mode, bingo, we've actually got a slightly different discharge current for each one.

**Dave Jones:** So it kind of doesn't make sense. If they were all being discharged in series like this, then, you know, you'd think they'd just measure the one current, and then it'd be the same for all of them. But I don't know, maybe they're just calculating this,

**Dave Jones:** and they're actually multiplexing this. They're actually switching individual cells, like off and on, and actually measuring things like that. So what we want to do is actually get out the scope, and actually have a look if this thing is truly a constant current charge.

**Dave Jones:** We'll look at the charge first. Is it actually a constant current charge, or do they actually do multiplexing and switch these MOSFETs off and on? So let's take a look at the scope. Now before we just go in here willy-nilly, and actually hook up all of our channels,

**Dave Jones:** because we've actually got 8 MOSFETs on here. And ideally I'd like to actually get 8 probes on there, but we've only got a 4-channel scope here. But we do have our logic analyzer, so what I want to check first is just to see if the MOSFET drive signals on here

**Dave Jones:** are actually digital, and what signal level they're at. So what we'll do is we'll probe one of the MOSFETs here. I'm doing a bottom MOSFET. So let's have a look at the bottom. And bingo, we're at 5 volts per division. 5, 10, 15.

**Dave Jones:** We're driving these MOSFETs with 15 volts. And that's actually not surprising, given that you really have to turn these MOSFETs on hard, really drive them hard to get the lowest on-resistance possible. So you get to minimize the loss in them, the power dissipation in them,

**Dave Jones:** because they're only little SO8 packages to them. I think someone may have actually asked that question. You know, how do they get away with, you know, 8 amps charging on this thing with little SO8 packages? It's because the on-resistance is incredibly low. So they're driving them with 15 volts.

**Dave Jones:** Let's check the upper MOSFET now. Probe the upper MOSFET. It's, nope, it's sitting down at ground. It's sitting down there at ground. Nothing doing there at all. And, uh, it should be identical for all the next channels. This is the, well, channel 3 here,

**Dave Jones:** 15 volts once again, and they're all the same. And that makes sense when you've got, uh, no batteries, uh, plugged into this thing. You want this bottom MOSFET turned on so that you're basically bypassing each cell as we, uh, mentioned before. You don't want to be, uh, turning the top one.

**Dave Jones:** You only want to switch on the charge to a battery when you detect that there's a voltage across there. I'm going to use my, uh, logic analyzer here These are the new, uh, Keysight ones. Real tiny compared to the, uh, the huge ones that they actually had before.

**Dave Jones:** This is my new, uh, 3000 X-Series, uh, touch oscilloscope, which Agilent, uh, replaced my existing one with. Very nice, very compact. I rather like those. Pretty sexy. Now when you're probing something like this, make sure you turn the power off first. And even using these very tiny easy-hooks,

**Dave Jones:** here, um, there is still the potential to short out between the, uh, pins. So, yeah, you don't want to short your gate pin out to your, uh, source terminal there. That could be bad news. And you don't want them flapping around in the breeze

**Dave Jones:** either when you're, uh, like, because I'm going to have to probe some, uh, analog, uh, some other stuff on here too. I know I might need to get in there, but anyway, for now, for the purposes of this experiment, got to put some batteries in here.

**Dave Jones:** Just want to have a look at all eight, uh, gate signals, so I've just, uh, taped those down so they're not going to flap around in the breeze and accidentally, you know, like if I put, uh, any, uh, accidentally touch these, they're not just going to fall down

**Dave Jones:** and accidentally short out. And there's no worries with the, uh, input voltage range of these digital channels either. They're, uh, plus minus, uh, 40 volts, uh, capable. Um, just set it to, uh, CMOS triggering here, which is 2.5 volts, yeah, whatever. Good enough.

**Dave Jones:** I could, I should actually change that user, threshold, I've got a touch screen here. I can change that user threshold up to, you know, I don't know, 8 volts, there we go. It only goes up to 8 volts maximum, that'll do. Actually, there was a trap for young players here.

**Dave Jones:** Uh, if you read the specs for this, uh, for the digital channels here, sure it can accept up plus minus 40 volts, but the dynamic, the input dynamic range of these digital channels is only, uh, 10 volts around the threshold of the gate.

**Dave Jones:** 10 volts around the threshold voltage, so whatever threshold voltage you set. So if we had 2.5 volts before, in theory, well, according to the spec sheet, uh, then the maximum input dynamic range would only be 12.5 volts, but it'd probably still work, but yeah.

**Dave Jones:** Um, yeah, that's not terrific. So there's a trade-off there between the usable dynamic range and the, uh, maximum input threshold voltage versus, uh, maximum input voltage versus your threshold voltage. How nasty. Oh, don't want that. Bloody touchy-feely scopes. And I'm sorry that it's next to impossible to get all of this

**Dave Jones:** in one shot, uh, inserting this, the screen at a reasonable resolution and the schematic as well. Anyway, I've got the 8 digital channels, uh, up here, and they're actually as per the schematic here. So, uh, channel like D0 at the bottom here is this lower MOSFET, then channel 1,

**Dave Jones:** 2, 3, 4, 5, 6, 7, 8. So we've got it switched on, and as you can see, the, uh, the lowest, um, the lower MOSFET for each one is actually switched on. So what I'll do is I'll, uh, well, high, switching on being high, that

**Dave Jones:** is, and let's plug in a battery. And we'll see. I'll plug it into the bottom one here, okay? So we should see these two MOSFETs switch. D0 should drop, uh, low, and D1 should go high. So we're switching on the upper MOSFET to charge,

**Dave Jones:** we're, and we're turning off the lower MOSFET, which is a disable. So here we go. Bingo! There we go, it just switched. You saw it? Hey! Hello! Hello! We have ourselves a pulse that's walking away from us. This thing looks like it might be,

**Dave Jones:** well, it's switching off. Hmm. Now I've got this at a low time base, that's 200 milliseconds, uh, per division. So I'm not, uh, triggering off anything at the moment, it's just free running. Let me plug in another battery. Okay, I've plugged in a second

**Dave Jones:** one, and there's something happening. Hey, look at that! That's interesting. Let's try and capture that. At the moment I'm just free running, I need to trigger off these digital channels. So we'll trigger off the D0 down here. So we can just go into trigger, source,

**Dave Jones:** and then we can choose D0 down here. So let's trigger off D0. There we go. And we can zoom that out. There we go. That's interesting. Wow! And I suspect if we put in the third and fourth batteries, we'll see some extra stuff happening up here.

**Dave Jones:** So I'm not sure of the time period, it's probably like a second or something. But I think it might be, uh, switching those off every second. I'm going to plug in all four batteries. Let's switch this puppy on and, uh, see what happens.

**Dave Jones:** Here we go. There we go. We've got something convoluted happening here across, uh, well, except for the fourth channel. So I don't know what's happening in channel four. Maybe it's not charging. Huh. There we go, it just had a dicky contact. But as you can see, they're

**Dave Jones:** switching something in there. So let's turn that down to, uh, well, 200 milliseconds per division. Let's see if we get anything. No. Let's turn it down to 500. There's got to be a period there. There we go. One second. There you go. Interesting.

**Dave Jones:** And what I'm just doing here is actually, uh, labeling the channels. I've made them bigger to fit the full screen, because we're just looking at the digital here. And, uh, I like the new, uh, QWERTY keyboard on this thing, because we can just go in here

**Dave Jones:** and then bingo, with the touch screen, we can just, you know, type in anything we want. What I like is that, um, we've got an auto-increment, uh, function here. So I can select, I've already labeled, uh, this bottom one, bypass 1, bypass 2, it automatically

**Dave Jones:** incremented to bypass 3. We can apply the new label, and then we can go, uh, OK, we want, we've already got those three. That one, D6, apply new label. Bam! Too easy. OK, so that makes it easier. Bypass channel 1, and charge channel 1, and so on for the

**Dave Jones:** other channels. And as you can see, we're 500 milliseconds up per division, so each second is a new cycle. I just realized I labeled these different to what I've got on the, uh, schematic here. Oops, anyway. Um, let's just say, like, number 1 down here, OK,

**Dave Jones:** for the first 500 milliseconds, it's actually bypassed. That battery is not being charged. And then, uh, for the next 500 milliseconds, you can see that, uh, it does charge, because then the charge goes high, charge line goes high for 500 milliseconds. And then, of course, the bypass,

**Dave Jones:** these are always alternate, uh, ones. I don't think, um, there's a scenario where you're going to have both, uh, charge and your bypass on at the same time, because, well, you'd be shorting your battery out. So, as you can see, they have, uh,

**Dave Jones:** for the first 500 milliseconds, uh, number 1 battery is on, number 2 is off, number 3 is on, number 4 is off. So they're doing 2 at once here, and then alternating between them. But we've also got this little data that's going on in there.

**Dave Jones:** I'm not sure what that business is. That might have to do with the measurement. But whatever it's doing in there for 20, 40, 50, uh, milliseconds, that's not a coincidence, I think. That's precisely 50 milliseconds. Something's going on in there. Anyway, you can see how they're always, uh,

**Dave Jones:** alternate for each, uh, channel. You'll never get both of those MOSFETs on at the same time. One's high here, one's low here. And here's a limitation with the, uh, memory on this scope. Even though we've got 4 meg, uh, sample memory, okay, but because we

**Dave Jones:** got such a slow, uh, time base, we're looking at, you know, this sample rate for our digital channels, 50k samples per second, right? Because we're capturing, like, you know, 2 seconds, we've got, like, uh, what is it, uh, you know, 5 seconds worth of

**Dave Jones:** data there on this thing that we're actually capturing. When we actually go in, there's a limit to how far we can see. It shows a block, because that's one entire sample like that. So, there's a limit to, uh, what we can see there.

**Dave Jones:** To get around that, you would need either a deeper memory, uh, scope slash logic analyzer, or you need a logic analyzer with, uh, sample compression, or you could do it using, um, segmented, uh, segmented memory as well. Okay, so we've figured out what it's doing.

**Dave Jones:** Charging it certainly is multiplexing these batteries. Let's now turn it back on. I'll put it into discharge mode and see what happens. I'll do this off camera, because it could get fiddly. Hang on, I've got to move the camera. Alright, so I'll switch it on.

**Dave Jones:** We're in charge mode. Excuse me, I've got to, uh, discharge. There we go. We're discharging all four batteries, around about 400 milliamps. What's going on here? Let's run it. Come on. You can do it. Hey! Look at that! So that's really interesting. There is

**Dave Jones:** not, yeah, we're definitely updating. There's nothing updating there. I'm at 500 milliseconds per division, unless it's doing it out at 10 seconds. Maybe I can you know, leave it like that, but I know. We would have seen something. It looks like they're all

**Dave Jones:** the bypass FET for each one is on. Okay, so let's have a look at the circuit arrangement, but it's not doing any multiplexing during discharge. Well that's damn confusing. We've got the discharge MOSFET on for each one of the channels, and that's the path that would be

**Dave Jones:** taken. But as I said, because the positive terminal of the battery is up here, the body diode of the MOSFET is switched off here, here, here, here, and here. So like, where is the discharge path? Where is the discharge path from this battery?

**Dave Jones:** Where's it going? It can only go two directions. That way, or that way. And if it goes this way, and yeah, there could be something over on this sense line here that's, you know, pulling it down, and you know, allowing current to flow

**Dave Jones:** through, and, but like, meh, where's the other, and then are they sensing this resistor? I couldn't see any sense lines connected, any like differential lines across that resistor, and then, even if you did do that, if it was flowing this way, somehow, how would you discharge your AAA?

**Dave Jones:** Because your AAA is connected here! So, like, I I... And also, we're talking like half a watt as well, because it's like 400 milliamps discharge, right? So that's in the order of half a watt. That's got to be dissipated somewhere. And by the way,

**Dave Jones:** I have checked the output of the DC to DC converter, it's basically zero, so I don't see a discharge path here. How is current getting out of these batteries? The top MOSFET is switched off, and yes, it's not just the digital channel, I did actually get

**Dave Jones:** back in there with the scope, and did actually check, and the gate voltage of these upper MOSFETs is actually zero, so it's not partially turned on or anything like that. Anyway, let's go back to charging, shall we? I don't know what the discharge thing is happening

**Dave Jones:** there, so let's just, I can just reset the damn thing, and we will go back to 500 microseconds, that's no good. We'll go back to our 500 milliseconds, and what I want to do is just take out a battery or two, and so there we go.

**Dave Jones:** So there's only two batteries being charged at any one time, because we've got our 4 amps discharge instead of 8. So let's take out this top one. What change have we got? There we go, we've definitely, it's bypassed, it's switched into bypass mode there.

**Dave Jones:** Although, hang on, yep, there we go, it just took time to update. So let's now take off... Oh, it doesn't matter, because there, it doesn't matter which order, so we can take out the top one here, just because I've got access to it.

**Dave Jones:** And let's see if we've got, what happens when we've got two batteries. Bingo! On for the full period. So there you go, that's the 8 amps, that's the difference between the 8 amps and the 4 amp charge. Now, they're basically both on for the entire

**Dave Jones:** period. And by the way, I have actually tried to get in there with my 10 amp, with my meter in 10 amp mode, and actually measure the charge current, but it looks like the drop is too much, the voltage drop in there, and you know, due to the

**Dave Jones:** leads and the burden voltage of the meter and everything else, and it just, it just does not charge. So yeah, it's tricky business, sort of, you know, if you want to measure the current here, you've got to do it right, you've got to set up everything correctly

**Dave Jones:** and, well, you know, you can't just bodge in a meter and expect a measurement. Because, you know, the safety cutouts in here, you know, even a few millivolts difference can be the difference between shutting the thing off or not. So I'll show you that on camera, maybe it might

**Dave Jones:** work this time, because I've discharged this one a little bit, I don't know, let's have a look. So I've put in a bit of, oh, there we go, no, oh, hello! No, see, it just shut off. But there you go, we did see like 7

**Dave Jones:** and a half amps on there very briefly. So we can try that again before the, you know, we've only got a second before it gets to its next detection window. And there we go, 7, 7 and a half, yep, and just switches off.

**Dave Jones:** But there you go, it does actually charge at, well, 7 and a half, 8, eh, you know, near enough. And if I discharge just one battery, then well, it's exactly the same as before. All of the bypass FETs are turned on and all the

**Dave Jones:** charge FETs are turned off. Now, I think it's appropriate at this point that we break out a tool that's incredibly valuable if you've got it. It's this AIM TTI iProber 520. It's a positional current probe and you might have seen this, I've used

**Dave Jones:** it just a couple of times in videos, but it's incredibly handy. What it is, is it's basically an isolated probe with a magnetic field measurement coil on the end, and can basically give you, allows you to get in there and probe individual traces

**Dave Jones:** and look at the current flowing through them. Perfect for an application like this, where you've got like, you know, substantially high currents, not easy to break into things, and we can just put this on the trace here, for example, and hook it up to our scope.

**Dave Jones:** It's got an oscilloscope output here, and we can actually look at the charging and discharging waveforms through various PCB traces. So, let's give it a go. Now, because of the relative nature of the measurement on this thing, if you want an absolute quantitative measurement,

**Dave Jones:** i.e. it to be calibrated and accurate in terms of volts per amps output, then you've got to actually calibrate the thing with this built-in calibrator. There's a little PCB trace down here. I've done this in a previous video, but I might just run over it again.

**Dave Jones:** Now you've got this calibration chart inside here, and basically you need to know the trace width you're measuring. I think my ones, it's complicated because there's actually the one with the link installed, so it's a link with a PCB trace underneath, and it's

**Dave Jones:** like, you know, it's all completely dodgy. Anyway, we'll have a go. I think it's about 3 millimeters wide, so we're looking at around about the calibrator output of 3 volts peak-to-peak. So let's set that up. So what we want to do here, stick this in the calibrator, whack it

**Dave Jones:** on AC here, and you'll notice how it's a little bit fiddly. You want to get in the position so it's the highest amplitude. You basically can't go over pretty much, and you'll notice that if I rotate it it drops in amplitude because, well, it's

**Dave Jones:** perpendicular to the trace. So, and of course if we go in the other direction, I can show you this as well. If you have DC, switch it to DC instead of AC, you'll notice that one way is positive and the other way is negative.

**Dave Jones:** So you can actually detect current in both directions with this thing. Anyway, we need to set this thing to 3 volts peak-to-peak. So I adjust the sensitivity here until we're just around about, hey, we're over there. Let's turn it down. Whoa there, silver sovereign.

**Dave Jones:** Alright. 3 volts peak-to-peak. There we go, we're ready to go. Hopefully that'll give us, you know, roughly an absolute value, but like I said, we don't need an absolute value here measuring this thing. Adjust to get, just to see the waveforms is enough.

**Dave Jones:** You don't actually need a quantitative measurement, but hey, you know, I just thought I'd do that for kicks. And then when you're mucking around with current probes like this, you can actually go into your channel, go into your probe setup here, and instead

**Dave Jones:** of the regular volts, volts per division, we can change this to amps per division, and then the probe itself, it's already, actually just happens to already be set up at 1 volts per amp, which is exactly what we set this thing up for, so now our

**Dave Jones:** peak-to-peak value here will actually be in milliamps instead of volts. It's just nicer. Most modern scopes you'll be able to set up current probes like this. It's very handy. Now let's actually put our probe on here and see if we're accurate. I think

**Dave Jones:** it's going to be pure luck if we're actually accurate or not. That's actually, I got it round backwards, you see how it went negative there? So we just spin it around, not that it matters positive or negative, but there we go, looks like we've got some ripple

**Dave Jones:** in there. We might be able to trigger on that but you'll notice that we're at 2 amps per division, hopefully you can see that, 2 amps per division so 2, 4, 6 yeah, we're kind of you know, 7, we're kind of, sort of, not

**Dave Jones:** not there. Hang on. What's gone wrong? Something's happened. Oh, the battery's actually full and it just cut off. Go figure. But we got within a reasonable ballpark there, just over 6 amps or something like that, and you'll notice that, hey, there we go

**Dave Jones:** that is our current switching off and on. There it is, you can see it. Bingo, we're capturing exactly what we did before if we go to 500 milliseconds per division, then we'll actually see that current yep, bang, bang, bang, there we go. Now let's see if we can

**Dave Jones:** have a look at that ripple. I've gone into AC mode, oh damn it we're full again, another bloody full battery. And there we go, that's our AC ripple look at that, we're at 10 microseconds per division, about 2 divisions there around about 50 kilohertz

**Dave Jones:** switching frequency or thereabouts. So that is our DC to DC converter. So and there we go 500 milliseconds, you'll see it switch, bang, bang, bang. So what I'm effectively measuring down there, that link on the bottom, that's actually just in here it's before this

**Dave Jones:** shunt, I can't quite get in there with the shunt unless I get rid of all of these anyway but still, it's that ground trace that comes out of there. So we're effectively measuring the current through that shunt. And yes of course the good thing about having a mixed signal

**Dave Jones:** oscilloscope like this digital analogue in the same scope is we can actually correlate the analogue channel up here with all the digital stuff that we saw down here. So we capture it and bingo, here's the analogue you can see that it switches, the charge switches off, bam

**Dave Jones:** like that, when our charge level here actually goes low and switches back on. And then we've got a large amount of ringing there when the DC to DC converter starts back up, that constant current source. Because you can see the current's actually dropping to zero.

**Dave Jones:** If you remember the schematic, it's not just bypassing the battery, which it can do, it's actually switching off the converter. Because if it was just bypassing the battery, we would still see the constant current flowing through that PCB trace. But it wouldn't be flowing through the batteries, but we're

**Dave Jones:** not. So it is physically switching off the DC to DC converter, that constant current source, and then switching it back on, boop, it takes a little while to recover there. What does it take? Ah, a few, only a couple of milliseconds? Yeah, no

**Dave Jones:** worries. And then the charge switches back on. So bingo, it's nice to be able to correlate things like that. This is where, if you've got like a USB logic analyser for example, then you've got your analogue scope trying to correlate the two. It's just much nicer

**Dave Jones:** when you have the one instrument like this. Okay, so what I want to do now is actually turn it into discharge mode. Okay, so let's get, there we go, we've got our charge mode up there, okay, so we've got our 6 amps, we're 2 amps

**Dave Jones:** per division, and let's switch it and see what's flowing through that trace. I think I've got the right button here. Bam! Hello? Hello? Hello? 500 millivolts per division! Bingo! Look at this! It's gone negative. It's gone negative. You saw it. From charge mode

**Dave Jones:** going into discharge mode, the current through that trace is negative. That is, like I haven't changed the position of the probe, so it's gone from positive to negative. It's flowing the other direction. Wow! That's interesting. Like I said, I'm measuring this point here,

**Dave Jones:** so when it's charging, current is flowing down through here like this, but when we set to discharge mode, current's flowing up. It's definitely flowing through that trace. You saw it. What was it? 600 odd milliamps there. We've got an error. We know it's

**Dave Jones:** measuring about 400 milliamps on this thing, but there was definitely current flowing back through. So how the hell is it doing that? Wow! Is this going negative or something? What? By the way, if you're curious to know how accurate the voltage is on this thing,

**Dave Jones:** I'm going to it's 1.37 1 on there, and on the display here, sorry I can't show you, 1.32. So near enough. I think there might be some more error up at 8 amps. So let's measure the charge. I'm now charging at 8 amps.

**Dave Jones:** Wow! Look at that! 1.84 volts. Wow! That's above the recommended cutout, which is usually 1.8. And it's displaying 1.59. There we go. 1.6. So there's a 200 millivolt discrepancy there. So the differential measurement, or maybe they're not even doing differential measurement, is quite poor.

**Dave Jones:** So that, yeah, that's not good at all. That's a bit how you do it. By the way, I've shown this in previous videos, but I'll just say it again. Another trap for young players. Watch this. If I turn this probe, you might be able to see

**Dave Jones:** the green trace move there. That's at 2 amps per division. That is the Earth's magnetic field doing that, and it's actually worse. I didn't compensate for that before. If I'm now at 500 milliamps per division, ooh, look at that! Whee! That's not terrific, is it?

**Dave Jones:** Right in the middle of nowhere. So you've actually got a trace position control on the unit itself, so you've got to center that down there when you've got it in position. And it's actually not too far off the displayed value now that I've actually

**Dave Jones:** zeroed that thing. It's 500 milliamps per division there. And we're getting, you know, around about, you know, that 350 or 400 watt it's actually displaying on the thing. So it's not too far off. So absolute calibration, eh, you know, it's going to be within

**Dave Jones:** you know, we can, like 20% or something. Now what I'm going to check now is a trace up the top. I don't know, like, the width. I haven't set the width properly yet. I have to recalibrate and get absolute. I just want to see if there's anything there.

**Dave Jones:** If there's anything flowing into this. So if it's like going somehow back up the chain and out here. So there's a trace right on top here. If I zero that, and nope. Nothing. It's not budging. So there's nothing flowing through that trace going back to the DC to DC

**Dave Jones:** converter. So I'm still none the wiser where this damn current is coming from or going. I think I'm going to have to disconnect all these clips again, because we've done that. We've, you know, figured out that the thing's multiplexed and everything. Have another

**Dave Jones:** decent look at the at the traces in there. See if I can see anything. Hmm. And oh! Stupid me. If I spent a few more minutes actually reverse engineering this board before I went off half-cocked and did the schematic, yes, I would have found

**Dave Jones:** the discharge path. Here it is. It's bleedingly obvious. There's actually here, okay, here's the positive terminal of the lower battery here. Here's the shunt I was measuring before by the way, that ground shunt. And here's the top MOSFET. Here's the positive terminal. Okay, it actually

**Dave Jones:** there's a trace that goes off under there and it snakes off around there around there, around there into, bingo, Q25 here. That's got to be a little that's a little SOP23 MOSFET. And then there's two 6R2 resistors in parallel under that, that actually then

**Dave Jones:** go back to ground on the other side. Here's that current shunt resistor in there. And so the other side of that. Bingo. And it wasn't so obvious on these ones here, for example. Here's the next one and then the next one. So there's actually four of these

**Dave Jones:** duplicate discharge transistors discharge MOSFETs, and this actually drops down through some vias into a trace and actually ends up under the chip here. Actually under the thing. So there's vias under there and it goes on the other side. So you've just got to follow these things carefully.

**Dave Jones:** And of course, what does that translate into? Well, here it is. Positive terminal of the battery and we've got ourselves a once again, it'll be like an N-channel MOSFET there. And two 6R2s in parallel, so 3.1 ohms 1.3 volts divided by, you know, roughly

**Dave Jones:** 3.1 ohms gives us around about that 400 odd milliamps we'll see in. Bingo. And then they can just measure the drop across this. But of course, some of you might be saying Dave, I actually saw the current change direction through this current shunt.

**Dave Jones:** What the hell's going on? Well, it's easy if you think about it. During charge, okay, it comes down through the ladder of MOSFETs like here through here, and then down the battery so the current is flowing in this direction when it's charging, okay, which is

**Dave Jones:** what we got. And when we discharged, it was flowing in the other direction. How does it do that? Well, of course the positive terminal of the battery, it's now flowing out here like this, so of course we're doing conventional current flow none of this electron current flow rubbish

**Dave Jones:** okay, so going from the positive through the MOSFET, down through here and it's going into ground, but there's as always, right Kirchhoff's current law like there must be a loop there, right so that current, where does it go? It goes through the ground plane

**Dave Jones:** and then bingo back up through there like that so that's why the current changes direction. Now I know that I said this was going to be a quick video, and well, as always, that was the intention but you know, I got carried away

**Dave Jones:** got a little bit excited you know, I went down the rabbit hole and anyway, we eventually found out what the hell was happening here. Yes, these are all multiplexed and we found the discharge path in the thing and we realized that the voltage sensing on there

**Dave Jones:** wasn't that great, you know it's not terrific so it's really, it's kind of like a clever design, like I really like the way that they've done the switching in this thing, it really is quite clever, but you know, in the end it's not a great

**Dave Jones:** you know, accurate implementation in terms of charging and voltage detection and that sort of thing so yeah, it's a bit rough and ready but hey, you know, it's built down to a cost and that's what you get. But anyway, I hope you liked that little adventure here

**Dave Jones:** we got to play around with our little current probe, this is always fun to play around with, if you ever get a chance to get one of these puppies they're not cheap, I think, don't quote me but they're like 700 bucks or something

**Dave Jones:** but these are really great you know, you don't have to break in to the power supply, and it's insulated so you can get in into, you know really high voltage stuff, get in there like, you know, high voltage switch mode power supplies and actually probe stuff

**Dave Jones:** and get the waveforms, it's absolutely fantastic incredibly valuable tool for stuff like that, it would have been really ugly if we had to get in there and, you know, hack in current shunts and meters and things like that, you know, cut the traces

**Dave Jones:** and ugh, it's just, yeah really quite ugly, so this is a really handy tool, and that's a really good example of using it, we did some good examples of mixed signal capture there and things like that a bit of reverse engineering and circuit

**Dave Jones:** tracing, and had a bit of all this video, so I hope you enjoyed it if you did, please give it a big thumbs up and if you want to comment, EEVblog forum link down below, all that shiz catch you next time
