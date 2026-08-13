---
video_id: bDxabiM-WF8
title: EEVblog #665 - Polar Wearlink Heart Rate Transmitter Teardown
url: https://www.youtube.com/watch?v=bDxabiM-WF8
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 17, "2": 29, "3": 41, "4": 57, "5": 77, "6": 89, "7": 113, "8": 125, "9": 141, "10": 157, "11": 169, "12": 185, "13": 201, "14": 213, "15": 229, "16": 245, "17": 257, "18": 273, "19": 293, "20": 317, "21": 337, "22": 349, "23": 373, "24": 385, "25": 405, "26": 417, "27": 433, "28": 449, "29": 469, "30": 493, "31": 509, "32": 525, "33": 541, "34": 557, "35": 573, "36": 585, "37": 601, "38": 625, "39": 641, "40": 657, "41": 677, "42": 701, "43": 721, "44": 741, "45": 777, "46": 793, "47": 809, "48": 829, "49": 845, "50": 877, "51": 893, "52": 913, "53": 933, "54": 949, "55": 969, "56": 989, "57": 1005, "58": 1035, "59": 1059, "60": 1075, "61": 1099, "62": 1119, "63": 1143, "64": 1159, "65": 1175, "66": 1191, "67": 1215, "68": 1227, "69": 1239, "70": 1255, "71": 1275, "72": 1287, "73": 1311, "74": 1327, "75": 1343, "76": 1363, "77": 1383, "78": 1395, "79": 1411, "80": 1427, "81": 1443, "82": 1463, "83": 1479, "84": 1495, "85": 1511, "86": 1527, "87": 1539, "88": 1555}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. Where is today's teardown? It's not up my sleeve, it's up my shirt. Yes, warning, nudity alert. This could get me banned from YouTube. Ta-da! Here it is. It is the, rip it off, the Polar Wearlink Coded Wireless Transmitter.

**Dave Jones:** One of these fitness trackers, Polar, one of the pioneers in the industry, you know, transmits to a watch, you get your heart rate, all that sort of jazz. I know wearables are all the rage and, you know, stuff like that. But yeah, these were one of the original.

**Dave Jones:** So I thought we'd take a look inside, see what's in there. Probably not a huge amount, but you never know. Could be interesting. And I thought we'd hook it up to the scope as well, see if we can get the signal out of this sucker too, and maybe see how it's coded.

**Dave Jones:** Let's go. Now if you haven't seen these before, it really is quite a nice design. As I showed, you can just rip it off here and they've just got these standard studs here embedded in the chest strap. And the chest strap contains internal conductors.

**Dave Jones:** Just going from there, just to a conductive fabric type pad here, which you usually have to moisten first in order to get good actual contact. And once you start exercising and sweating and stuff like that, then you get a decent contact. But that's basically

**Dave Jones:** all there is to the thing. And it is quite a nice little module. This isn't the one we're actually going to tear down. I'm currently wearing it. This is actually the wife's one. We've got two, so we can actually compare them, but I believe it's absolutely identical.

**Dave Jones:** So just powered from a coin cell battery and very low power, and transmits on around about 5.5 kilohertz. So it really is low frequency stuff. And I believe it's actually like a, it uses a loose coupling scheme. So it's a magnetic coil coupling at 5.5

**Dave Jones:** kilohertz or thereabouts. So the range is only like 0.8 meters or something like that. It's got to be within distance. And I'll link to a data sheet down below where Polar actually sell a little module that you can get that actually can get data out of these things.

**Dave Jones:** Well data, you know, it's just pulse rate. That's basically it. But these are supposedly coded in some way so that you can use more than one in the same area. So you know, two people side by side and they don't interfere, that kind of stuff.

**Dave Jones:** So yeah, they actually sell a little module and they tell you in the data sheet for that thing that you have to enable it the right, you have to orient it the right way. So if your board is like 90 degrees to it, it's not going to be nearly as effective

**Dave Jones:** as like that. So I'd expect some sort of coil coupling system, some sort of loose coupled system inside this thing when we tear it down. And this is the wife's watch here, and this one's actually connected through to here because this one will just power down.

**Dave Jones:** If it doesn't detect that, you know, any heartbeat signal at all then it's not transmitting. So this one's actually receiving from the one we're actually going to tear down on my chest at the moment. As you can see, it flashes up there to tell you that it's receiving the signal.

**Dave Jones:** And my heart rate's about 85. That is quite high for me because I'm sort of animated, I'm talking behind the camera now and sort of moving around. So yeah, it's reasonably high. And yeah, getting higher as I keep talking here. But yeah, there you go.

**Dave Jones:** So that's the receiver, but you can actually get a module that you can plug into your microcontroller or something like that to actually receive the data for these things. So I don't think it's terribly complicated, probably some sort of you know, simple encoding scheme.

**Dave Jones:** It might have, you know, a random address of 256 or something, I don't know. Anyway, we'll find out. So before we do the tear down, let's see if we can actually get a signal, this, and actually detect it on the scope and find that

**Dave Jones:** 5.5 kilohertz carrier frequency and what sort of encoding they're doing. Alright, let's see if we can actually get something on a scope. Just got my scope probe here. I thought about maybe we could try the like a single loop on here and get that, but I think the signal level's going to be

**Dave Jones:** so low that we're not going to get anything. So what I'm just going to do is try and place it against my chest here, see if we get anything, get him picking up 50 hertz crap here, of course, at the moment. But I've

**Dave Jones:** got it on here, I've moistened it a little bit down in here, and if we place it on there, hey, look! There we go. We're getting, look at that. We're getting some spikes. Let's go in and have a look. So all the tests I'm going to do

**Dave Jones:** here just have it sort of attached like that. And well actually, let's try the loop method, but I don't expect that to be particularly effective at all. Once again, like our 50 hertz has gone there, but oh no, there we go. No, we can get something.

**Dave Jones:** Yeah, there we go. We are getting them. I'm rather surprised at that. Single loop there, yep, that's good enough. I might do that actually to get rid of the 50 hertz. Because one thing that this scope, this Tektronix MDO 3000 doesn't have, sorry I'm not on camera, MDO

**Dave Jones:** 3000 doesn't have is software low-pass or high-pass and high-pass filtering as part of the math function. So you know, really quite annoying it's got all this advanced math capability, all sorts of fantastic stuff this thing can do, but it can't do any software filtering to take out that

**Dave Jones:** 50 hertz, which is kind of annoying. So anyway, but hey, there we go, we're picking up some packets. I'm surprised at that single loop, I thought it would be too low-level, but that works a treat. So let's have a look at the data.

**Dave Jones:** And I can show you that coil orientation thing. If I put it vertical like this, okay, bingo, oh we were. Hang on, yeah, there we go. We're picking up, yep, we're picking up some of those, sorry I haven't triggered off this right yet, but there we go, we're picking up some packets

**Dave Jones:** there. Presumably the 5.5 kilohertz, we'll go in there and measure it in a minute. But if I put it sideways like that it's not, we're not going to pick up anything at all with that. And I'm down at 1 millivolt per division there.

**Dave Jones:** So like really low-level stuff. So check that out. Maybe we might deal with, maybe we might use an open loop like that, because check it out, we're getting nice big packets like that. There you go, so I might do that, and of course that's not going to

**Dave Jones:** have a, the orientation isn't going to matter a huge amount. So yeah, I think we'll stick with that, we'll just stick with the open loop thing there. So get rid of our ground lead, and we can capture some nice packets there, and we can trigger off those too.

**Dave Jones:** Real easy. Okay, so I've captured this, and it looks like we've got sort of three packets there, and it looks like this one here is missed. So at a first guess, maybe they're doing the, like the encoding may not be like data inside of here.

**Dave Jones:** These packets look like the same length, but we can go in and have a detailed look. But a missing one, so maybe that's how, you know, at a first glance they actually code these things. You know, each device has just a random code perhaps, or maybe it changes.

**Dave Jones:** Maybe it dynamically changes and hops around, who knows? Anyway, I've got no idea. So let's go in and have a look at this. We'll expand the zoom on our scope here. Let's go into the, there we go. Look at that. And we can have a look there.

**Dave Jones:** That's what I like about this MDO scope, is its wave inspector function is really quite nice. 5.39 kHz, there you go. So that is, yep, no problem. 5.46, okay, so there you go. We're very close to the nominal 5.5 kHz, so that is correct.

**Dave Jones:** And how much data we're actually how many packets, you can count those, or we can probably get the scope to do it. Let's do that. So if we go into the measure menu here, and we go add measurement, let's have a look at the measurement type.

**Dave Jones:** Source, we want channel 1 of course. We don't want a snapshot. This is, I hate these dual knobs here, it's, you'd never know which one to freaking, like it tells you A, B, but it's, ah, it's just it really is annoying. I hate the selection knob interface.

**Dave Jones:** It's just, why have two? All other scopes get one just fine. Anyway, we've got all sorts of cool stuff here that we can measure. And I think if we go down here, look at this. Edge count. So let's go rise in edge count.

**Dave Jones:** I love the info display over here, shows you what it's doing. So let's, you know, I don't know, positive, let's just go rise in edge count. So okay, we'll add that to our measurement. I think it's added. Yep, there we go. Look at that, edges

**Dave Jones:** 23. So let's zoom into the other ones and see what we get if we use our control. See, and if I widen that window, is the count going to stay the same? Yep, 23. So it's pretty smart. It's counting those. It's doing a pretty good job.

**Dave Jones:** It's going to be off now, because it's counting some over here. But that, see, and of course if you go in, yeah, it's only got 10. So 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ooh, 11, but maybe it didn't have the full cycle there or whatever.

**Dave Jones:** Anyway, so that's near enough. It can give us a comparison between the two. Anyway, I actually might go in there and actually count them, but you know, how do you count the ones, you know, which ones do you actually count? Ah, it doesn't matter.

**Dave Jones:** I just want a comparative ballpark between these two packets here. So it's saying, it's counting 23 there. So if we move across to this one over here, is it the same? Looks like 23. Yep, it's an identical packet. So there you go. So there's nothing really, I mean, you know,

**Dave Jones:** that could be the encoding, the length of that packet, how many cycles they actually have. I'll have to compare that. So just remember this one has 23, and I can, well actually I'll do that right now. I'll put the Wwise one on. Got to remember not to mix them up,

**Dave Jones:** which one's which. And we will see if we get an identical number of counts. So here we go, let's capture it. I've put the Wwise one on. Hey! That looks identical. And there we go, it's exactly the same. It's skipping that packet there.

**Dave Jones:** So that is interesting. If we zoom into that, let's see if we get 23. There you go, I got it. 23. There we go. Yeah, it's basically the same. So, and it seems to be like the same length, I haven't measured it precisely, but it's pretty close.

**Dave Jones:** I suspect of course that the difference between the coded pulses, well the packets, is not between these, but between groups. So if I go all the way out let's turn that off, and I single shot say, well I can put in, hang on, I'll have to put it in roll mode.

**Dave Jones:** Scope again, I actually went to look for the roll mode in the horizontal menu, couldn't find it. Turns out that it's you just lower the time base over here, sorry, once you get to a certain I think it's 40 milliseconds per division, or whatever, anyway, it puts you in

**Dave Jones:** roll mode. So here we go. So there you go, so my heartbeat is the difference between these two here, and I can do my patented lab jumping exercise and increase my heart rate. So I'll keep that exactly the same and we'll do the patented lab jumping and come back.

**Dave Jones:** ... ... ... ... I don't want to do it! And here we go, let's put it back. There we go, it's quicker. And if I calm down, anyway, you won't see it on there, but we can go in and do direct measurements. And yes, for these sort of measurements, you definitely want a big record length so that

**Dave Jones:** you can get big timescales and then zoom into the data, so I'm using 5 meg, plus the high res mode as well, just to clean it up a little bit, do some boxcar averaging on the waveform. And I've also got the bandwidth turned on there, so input bandwidth

**Dave Jones:** 20 megahertz limited, you know, I don't need 1 gig worth of bandwidth here, it's just going to make my signal noisier. And of course if we turn on cursors here, there we go, I've set that between the two, the start of the two peaks there, and that of course is my

**Dave Jones:** heart rate. And it does change, I've verified that. 736 milliseconds delta there between my heart waveforms. But it's still heart pulses, you know, this is not like an ECG thing. You cannot get an ECG waveform out of this, it is purely just giving you a

**Dave Jones:** data burst at each pulse there, basically. So that's it. So yeah, I mean, it looks identical between the two units, so I don't know how they're coded. Let me strap the other one again on and try it. Here we go, I'll capture this again.

**Dave Jones:** And we can shift that waveform across. My heart rate has probably slowed down there a tad. In fact it's slowed down quite a bit there. Oh, bloody annoying. Okay. So there we go. 668 delta, and but you know, look, it's missing that pulse and then it gives us another two

**Dave Jones:** packets there. And of course if we zoom into those, it's exactly the same. And I've cleaned that waveform up a bit, used the loop method again with the probe. And getting the distance between those two, the time period, we're getting 44.8 milliseconds. Let's see if we get that with the other one.

**Dave Jones:** There you go, that's probably how they're encoding it. There's a time difference there between those. That one, the other one was 44.8 and this one is longer, as you can see. So I reckon that is how they're probably encoding it. Because there's nothing inside the packets, right?

**Dave Jones:** They're all like that, you know, 32 cycle burst or whatever. So and of course the difference between the first packet and the next first packet is your heart rate, so that time varies. So this time in here when they send the two extra packets, that must be, I presume

**Dave Jones:** the way that they encode these things. So the other, you know, it's probably, as I said like, you know, maybe 256 different possibilities or something. But it seems to be exactly the same each time. Aha, look at this, I just plugged it back on and

**Dave Jones:** like I just swapped it again and this one's different. So I reckon it maybe chooses a random or 1 of 10 or 1 of 256 or whatever, random time periods every time. It does that, look, it's very consistent okay? After it's powered on, by powered on I mean actually

**Dave Jones:** detecting a heart rate and actually transmitting. So it's very consistent like that, it's incredibly consistent yet what, look, I'll take the same unit, I'll unstrap it from my chest, okay? Leave it for, I'll just yap on for 10 seconds and I'll put it back and see if it varies.

**Dave Jones:** So this is exactly the same module, and you saw it was consistent before. Let's try that theory. No. Is that the same? That's what it was before. Argh, it's going to make a dick out of me. But maybe I've got to leave it off for longer.

**Dave Jones:** But anyway you can see, so I'll put the other one back on, and you can see that it... and this is... no it's, that's the same. Grrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr. And if it was skipping, if it was changing that between heartbeats or something like that, you'd expect it to

**Dave Jones:** just by me refreshing it, you'd expect me to actually show that. But nothing, so i'll switch it back, oh this is getting ridiculous. Getting very tiresome, sorry, this is a very tedious video. Ah, see that one's longer, look, that one's longer. It was here before the end of the packet was there, so it's changed.

**Dave Jones:** It's changed, so I reckon, and now it's consistent. See? Yeah. Yeah, so there's something going on there. Something definitely going on. Now here's an interesting thing I noticed, look it says coded on there, but it's got 31 next to it. And the other one

**Dave Jones:** maybe by sheer coincidence is also got 31. So maybe they preset that code in there, but as you saw on the screen there, it did actually hop around. It was actually changing, so yeah, I don't know, maybe it's a combination of hard coding plus maybe some random hopping

**Dave Jones:** between power-ups. I don't know. Grr, there you go, it's even longer again now. It's past that graticule marker down there, so you know, it's... yeah. It's changing all over the shop. But then, it's incredibly consistent. Once it's powered up, no problems whatsoever. Anyway, that's enough playing around.

**Dave Jones:** Sorry, that got a bit carried away there. Let's open this sucker up and see what's inside. Don't expect a huge amount, as I said, I expect a coil in there. An inductive coil, because that's what this data sheet implies, is that there is

**Dave Jones:** a coil and it gets coupling between the two and the orientation matters. So let's have a little squiz. Don't know if I have to take the battery out. Oh, no, I don't think I have to take the battery out first. Hey, it pops open!

**Dave Jones:** There's our o-ring. Ta-da! There's our coil. Too easy. O-ring seal, of course. These things, you know, you can swim with them and do all sorts of stuff, so it has to be o-ring sealed. It's got some crap in there. But there she is, wearing like Flynn.

**Dave Jones:** We've got ourselves the coil there. I don't know, it looks like quite a few layers on there. So yeah, that'd be a few. I don't know, anyone want to count the turns on there? There's probably at least three layers there, I think. And oh, there we go, it's got

**Dave Jones:** three. Hmm, that's interesting. Just three? There's not another matching wire coming out of there? No? Looks like there's somehow three wires coming out of that thing? Weird. Anyway, here's our contacts over here to our stud. That's a nice little system, they screw those in to bring those over to the

**Dave Jones:** pad, so I rather like that. Got ourselves a shield there, looks like we have one chip under there. Looks like we have a crystal down in there, probably I was going to say it looks like a watch crystal, but it's probably not. Can we

**Dave Jones:** lift that up? No, we have to undo that, so we'll take that apart. And not much else, a couple of caps, looks like we've got a transistor and well, not a huge amount there at all. So yep, well, this is pretty much what we expected.

**Dave Jones:** Check out the test pads there of course. There for the production bed of nails tester. So we've got ourselves our drive transistor here, our main cap here, this large value cap, it's going to form a resonant LC tank circuit with our coil here.

**Dave Jones:** So nothing hugely fancy going on there at all, pretty basic. The microcontroller's going to detect the heartbeat signal and then just encode it somehow and then just do a little burst transmission. Pretty easy. And there we go, not much else. I don't know if there's anything on the bottom

**Dave Jones:** of that, probably not, I'd be a bit surprised. We don't need a huge amount more. Macro lens time to see that part. Now you might be able to see it in HD, if you're watching in HD, but I can't. Could be a possibility.

**Dave Jones:** I can see that's manufactured by ST though. Yeah, it's certainly ST, but what is that? TR06-37B 82D VP830? Hmm. Sounds custom-y. And of course by custom I don't necessarily mean a custom ASIC. It could just be, you know, an ST microcontroller actually rebadged.

**Dave Jones:** That's, you know, likely what it is. I mean, you could start looking at the pinouts, get the typical ST micros. There's our crystal hooked up to there, so you know that the two crystal pins are there and, you know, so on and so forth.

**Dave Jones:** Power across there and there, so you can probably find out if that was an off-the-shelf ST micro, probably find out what one fairly easily. Now I had a brief look through the ST microcontroller website, through the parametric search engine there, and searched for

**Dave Jones:** 24-bit, sorry, 24-pin micros, which this one is. And really the only one I could find was the STM7260, and that is a 5-volt only part. It doesn't come in 3 volts, which it must because this thing is powered from a single lithium coin cell battery, so

**Dave Jones:** it must work, you know, like 2.5 volts upwards. So really, yeah, I don't know. Does anyone? Hmm. And that device also is designed for USB applications and the pinouts don't match the, you know, the oscillator was on these two pins over here and not these two over

**Dave Jones:** here. So yeah, I don't know, maybe I missed it, but it wasn't in their low-power series, wasn't in their ARM series, wouldn't expect an ARM of any form of ARM in this. It's got to be some sort of low-power micro-sustance, something like that.

**Dave Jones:** But it could be, yeah, could be some custom silicon. Don't know. And if we lift the board out there, we can see that there's not much action going on the back there at all. It's just got some flood fill, some extra traces, and

**Dave Jones:** the contact pads for the battery compartment. So that is all she wrote. That's pretty much all I expected in this sort of thing, I just thought it might be interesting to, you know, just take a look. And also the coding scheme used as well, which we didn't discover a massive amount

**Dave Jones:** really. It doesn't look to be anything fancy whatsoever. Now there's a thumbnail for you on the YouTube video. I'm going to probe myself, because you have to have it hooked up under here to get a response out of it of course, and get it to actually activate and transmit.

**Dave Jones:** And I've got a probe like this! This is great! I feel like Iron Man! It's awesome! Let's go to the scope. And there you go, that is directly on one side of the coil. Bingo. So that's actually what we're transmitting. And here we go, if I correlate between

**Dave Jones:** the transmit coil and what we're picking up with the inductive loop, of course, exactly the same thing there. Just wanted to show that. So we're down at 1 millivolt per division and we're up at hundreds of millivolts per division on that one directly on the

**Dave Jones:** transmit coil. So there you have it. Not much of a teardown, more playing with the scope and just mucking around trying to probe the signal than actually taking a look inside. But if you have any further info on exactly, you know, what the custom device

**Dave Jones:** there is, or the micro that it is, then please let us know. Or the actual encoding scheme used. But I, you know, on a quick Google I couldn't find the document, just sort of got some, you know, that module which I'll link in down below, data sheet for that from Polar themselves

**Dave Jones:** that sell this little module that you can plug into your microcontroller so you can actually, you know, get one of these transmitters, one of these and whack it on your chest and you can, you know, have your little Arduino or your other wearable electronics or something else can

**Dave Jones:** do that. Like you can have something like your chest you know, beats kind of, you know, you can have like a big LED thing on your chest that beats in time with your heart or something like that. You know, a shirt that actually

**Dave Jones:** you know, beats in time with your heart. Something, you know, really well, that's about all you can do. Something timed with your heartbeat pretty much. Because that's all this thing's going to do. But there you go. Hope you enjoyed that video quick as it was, or maybe not so quick with all that waffle at the start, measuring.

**Dave Jones:** Anyway, links below. Catch you next time.
