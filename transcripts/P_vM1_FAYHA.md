---
video_id: P_vM1_FAYHA
title: EEVblog #621- Stanford Research SR650 Repair - Part 2
url: https://www.youtube.com/watch?v=P_vM1_FAYHA
source: youtube-asr
timestamps: {"0": 1, "1": 16, "2": 30, "3": 44, "4": 56, "5": 69, "6": 81, "7": 98, "8": 114, "9": 123, "10": 132, "11": 141, "12": 156, "13": 175, "14": 185, "15": 197, "16": 210, "17": 233, "18": 242, "19": 263, "20": 272, "21": 282, "22": 310, "23": 317, "24": 331, "25": 351, "26": 361, "27": 370, "28": 384, "29": 394, "30": 403, "31": 416, "32": 426, "33": 436, "34": 448, "35": 456, "36": 465, "37": 483, "38": 497, "39": 506, "40": 521, "41": 533, "42": 547, "43": 565, "44": 583, "45": 597, "46": 610, "47": 620, "48": 639, "49": 649, "50": 660, "51": 677, "52": 685, "53": 699, "54": 720, "55": 730, "56": 741, "57": 750, "58": 761, "59": 785, "60": 793, "61": 815, "62": 828, "63": 841, "64": 853, "65": 869, "66": 880, "67": 896, "68": 910, "69": 924, "70": 935, "71": 946, "72": 957, "73": 966, "74": 976, "75": 987, "76": 997}
---

**Dave Jones:** Hi, in the previous video, we took a look at repairing the Stanford Research SR650 eight-pole elliptical filter I scored on eBay real cheap, and it turned out to be the mains filter at the back had a fire in it.

**Dave Jones:** And once I fixed that, well, it powered up and it seemed to at least go through the motions. And but I was playing around with this after the video, after I shot the video, and well, yeah, I noticed a few things that weren't quite right.

**Dave Jones:** I noticed them during the video, things like the you know, it didn't sound like the relays were working and you know, it's stuff like that and the in-out filter wasn't sort of working and well, yeah, a few things that hinted that there might be something more wrong with this.

**Dave Jones:** And some people also noticed in the video a few strange things which I found in here as well. So, there's more to the story here. It's not just the mains filter.

**Dave Jones:** We've got more to fix here. Beauty. Let's take a look at it. Now, one thing I noticed and also a few eagle-eyed viewers noticed this as well, check out this regulator in the back here.

**Dave Jones:** It's a 7805 5-V regulator. And look, it's got a sil pad on it, one of those insulating sil pads, but there's no matching heat sink. And also, it looks like it's had the screw in there.

**Dave Jones:** So, somebody has taken that heat sink off at some point. Why? And I eventually noticed, as did a few eagle-eyed viewers, that the display was dimming on this thing and even one person noted at the same time the fan was actually ramping up.

**Dave Jones:** So, we may or may not be able to actually see that here, but the this display will eventually dim after a few minutes. And well, that ain't right. And the fan actually speeds up and gets louder.

**Dave Jones:** So, why would a LED display like this dim? Well, all of the digital stuff in here, I believe, is uh powered from 5 V. It's pretty obvious that's the case.

**Dave Jones:** Probably that 5 V regulator that doesn't have the damn heat sink on it, cuz I think that's the only 5 V regulator in here. Oh, there we go. There we go, it's dimmed.

**Dave Jones:** It's dimmed. There we go. So, the only re- I better turn that off. That's that's not a good thing, okay? But, the only reason that would dim is if the voltage rail actually dips.

**Dave Jones:** I mean, if the voltage rail goes up, the display brightness is going to increase. So, that 5 V rail must be dipping. Now, the digital board at the back here, uh as I said, has its own 5 V rail and also all of the displays on the front.

**Dave Jones:** Uh those displays be multiplexed uh too, of course they have to be, there's not enough uh wires coming through to display all the segments, but they're multiplexed. But, that would be going through dropper resistors, and the uh effective brightness is going to depend of on the power value of those dropper resistors and the fixed 5 V rail in here.

**Dave Jones:** So, they that voltage rail must be dropping. So, let's take a look at it and measure it. First, we'll have a quick look at the power supply section here.

**Dave Jones:** Now, the transformer's over here, secondary of the transformer going over here, and we've got some voltage regulators. Obviously not dissipating much uh power at all, they're just free standing, got a tiny little piss ant heat sink on these things.

**Dave Jones:** So, but really, cuz they're only driving all the analog circuitry. Now, what we've got here is because we've got two different analog boards in this thing, all with their own separate taps, separate isolated because everything in this is isolated.

**Dave Jones:** So, the 5 V digital board will have its own tap and its own bridge rectifier and filter cap, and likewise for the two different supplies. We've got uh plus minus um I don't I don't know whether it's plus minus 12 or plus minus 15, but anyway, um split uh supply, and we've got an LM317 and an LM337 for one analog board, and another matching 317 and 337 for the other

**Dave Jones:** board. And that's our 5-V voltage regulator and as I said with the heat sink missing, that's a 7805. This one next to it is actually a uh tip uh power transistor.

**Dave Jones:** I believe that's uh driving the fan. So, that's pretty much all we have on the regulation side of things. Really quite simple. Now, of course, the power supply issues like this and power supply dipping will explain some of the stuff we saw in the previous video like the relays uh potentially not uh working if they don't have enough energy to operate the relays.

**Dave Jones:** So, maybe it's not just the 5-V rail uh the relays cuz the relays will be on the analog uh boards here. So, maybe the analog rails are out, too.

**Dave Jones:** But, anyway, let's stick to the 5-V rail. I'm measuring the 5-V rail uh with the meter here. Let's power it on and see what we get. Here we go.

**Dave Jones:** 4.99, everything's fine. Hello. Hello. It's ramping down. It's ramping down. And we might actually see This is interesting. There we go. It's ramping down. We might start seeing a dip on the display if it goes too low.

**Dave Jones:** I mean, you know, it's still not an issue at the moment. I mean, you know, still within that uh nominal 5-V uh spec you'd expect of a 5-V rail.

**Dave Jones:** So, 4.75. Here we go. Whoa. Whoa. Whoa. Whoa. It's dropping. It's dropping. Should see the display dim. Holy, it's going. I mean, the digital the processor is still working even though it's uh way outside it's under its uh nominal 4.75.

**Dave Jones:** Well, there's something seriously going on there. Haha. To give the digital credit, it's still working. The processor is still working at 3.9. Now, of course, that's a pretty much the kind of thing that you'd expect if your regulator is uh overheating and dropping out, you'd expect funny business like that.

**Dave Jones:** So, you know, how it started off at the 5 volts and then it ramped down, well, that's of course when it first powers on, the die is just fine.

**Dave Jones:** It's, you know, it's drawing the same amount of current as it later, but it hasn't had a chance to really heat up yet. So, once it does, bingo, it starts dropping.

**Dave Jones:** So, we need to whack as a first order we need to whack a heat sink back on there. Now, based on the I'm not sure of the original size heat sink that was on there, but hey, there's physical limits to how big it could have actually been.

**Dave Jones:** Likely to be very similar to one of these, probably slightly bigger, but it can't be very wide because there's that power transistor next to it. Can't be very tall because of the wiring.

**Dave Jones:** Can't stick out much cuz we've got a TO-92 there and other stuff. So, really I'll have a rummage around and see what I've got in terms of heat sink, but why is it missing?

**Dave Jones:** Like, did it I can't believe that it just, you know, it came loose through vibration or some other thing. It's like somebody's deliberately taken the bloody heat sink off.

**Dave Jones:** I don't really have much choice here. I've got a I've got a couple of these clip-on type heat sinks, but they're not very good, you know, what are they?

**Dave Jones:** 40° C per watt or something horrible like that. I've got this largest one. It's quite it's quite thin, but that would probably do the business if I can uh squeeze that in there.

**Dave Jones:** I've got a a screw-on one with a threaded hole, but that yeah, I could probably maybe screw that on, but you can't get the screw into the back of that thing.

**Dave Jones:** You can't actually get access. I might have to take the filter out again to get a a screw through there. It's all looking a bit yeah, I don't know.

**Dave Jones:** I'll try and squeeze this one in. See what that it I'm not sure of the specs of that. That's like, you know, maybe 15 20° C per watt, but hey, it should do it.

**Dave Jones:** Because ultimately, it shouldn't need much heat sinking because it's just powering the digital circuitry here, Z80 processor for those playing along at home, and your ROM and your RAM and your GPIB interface with your National Instruments chipset, and really not much else at all to actually power it.

**Dave Jones:** So, not a huge requirement, and you can tell from the design of the thing that hey, it's free standing, and B, there's not much room around it to put a heat sink, and they didn't design a a PCB mounted heat sink in there with the studs in the bottom like that one, for example.

**Dave Jones:** So, they didn't, you know, design that in. So, it you know, it must not be dissipating much power at all, but with absolutely no heat sink, clearly it's not enough.

**Dave Jones:** I wouldn't have expected it to fail so quickly, overheat so quickly though with no heat sink. I sort of maybe, you know, expected a bit more margin in there, but oh well, that's what it's doing, so.

**Dave Jones:** Let's put the heat sink on and see what happens. So, there you go. That's the best I could do with the heat sinks to hand. I might be able to find a more optimum one if I could salvage it from an old board or something like that, but it just wedged in there right next to the power transistor here.

**Dave Jones:** It's not shorted out there to the tab of the other transistor. You just have to be aware of that, and I just bent over the TO-220 there, but you know, you can't imagine there being much of a bigger original heat sink in there.

**Dave Jones:** So, that's got to do the job. Unless, of course, there's some other something else on the digital circuit actually loading down the regulator. Hey, we don't know yet. Let's just power it back up, see if we get that sort of same ramping effect, and let's measure the temperature of the heat sink.

**Dave Jones:** All right, let's power it up again. There we go. 4.991 and holding. Expect it to maybe drop a smidgen. As it starts to warm up, it shouldn't get that uh runaway effect that we got last time.

**Dave Jones:** And well, yeah. It's holding steady, so two thumbs. Keep going. We need to get in there and measure the heat sink, but I'll leave that on for like uh 5 minutes and uh see how see how warm that gets.

**Dave Jones:** Yeah, it's dropping a tad, but no big deal. Probably should measure the input voltage, too. Now, it's curious I did get the speed up of that fan again, but uh our supply hasn't dropped, so there's no correlation there.

**Dave Jones:** So, it might have a temp sensor in it. That's why it looks like uh I based on one track I saw, it looks like that power transistor's driving the fan.

**Dave Jones:** So, um yeah, it could it could have a temp temp sensor and then just uh PWMs the fan and controls the speed of it. And also, the problem I was getting last time of this uh AC DC coupling switch here not driving the relay, well, yeah, you should be able to hear that.

**Dave Jones:** That now works along with the one over here, and we're not getting that uh overload thing we were getting before. So, clearly that uh 5-V rail was just yeah, causing all sorts of issues.

**Dave Jones:** But, we need to go through, of course, systematically measure all the other uh rails. It's probably been on for like 5 minutes now. Haven't measured the uh temperature yet, but it's holding in there just fine, as you'd expect.

**Dave Jones:** So, uh yeah, that's the biggest heat sink you could uh imagine on that uh originally fitted to that device. So, it's obviously holding in there fine. There's no other overloads on the rail uh that we're aware of, and we've got our relay back.

**Dave Jones:** There's still no relay action for the uh filter here, but that could just be a mux uh to bypass. It may not actually be a relay in there for that.

**Dave Jones:** And we're looking at an actual uh tab temperature on the TO-220 there of, you know, it's it's getting upwards of 70° or thereabouts. So, yeah, it's it's not preferable, but it's it's not that bad at all.

**Dave Jones:** So, yeah, there's certainly no gross overload condition there. And the analog LM317 there is actually higher. Look at that, 72.4. And if we go over here, we're looking at for the 337, the other rail, you'd expect it to be pretty well matching and yeah, I mean, jeez, that's not great at all.

**Dave Jones:** This is pretty piss-poor thermal design in this thing. I mean, if you design this thing properly, it wouldn't even need a damn fan. And we'll just measure our 5-V rail there.

**Dave Jones:** Yeah, looks pretty clean, no worries, and we can go in there and AC couple that if we want and have a look. 5 mV per division. There we go.

**Dave Jones:** Not a drama whatsoever. So, that 5-V rail is just running hunky-dory. And we'll just check the input voltage to the regulator, see if it's well designed or see if there's any filtering issues.

**Dave Jones:** And well, the filter looks reasonable, you know, we've got about a 1-V ripple on there. And 2 V per division, we're looking at 2 4 6 8. Well, it's peaking around 9 there.

**Dave Jones:** Well, that's a little bit high, especially when you haven't designed in a proper heat sink in there, and that's why it's running at that temperature. I would have, you know, dropped that down to about eight, but then that's not counting for aging of the cap and stuff like that as it loses its as it dries out with age and things like that, you'd expect to get more ripple on

**Dave Jones:** there, but yeah, that's why it's running a bit hot, but it's certainly not, you know, crazy out in the ballpark like 12 V or something like that. So, that's not too bad.

**Dave Jones:** And we'll measure the LM317 rails. And these are really annoying cuz there's no voltage test points on this board at all. It's really damn annoying. You got to figure it out for yourself, and you can't see the traces cuz they're on the bottom and I had to buzz a few things out and use a bit of common sense and I finally found the ground point on there and uh it's just ridiculous.

**Dave Jones:** Anyway, that's our output voltage of the LM317 and that's around about we're 5 V per division, so around about 15 and 1/2 V or thereabouts. And the input voltage, if I can get in there And yeah, there we go.

**Dave Jones:** There's our input voltage. So, you know, 5 10 15 20. Whoa, jeez, look at that. That's really overkill and the ripple doesn't matter a rat's. But yeah, that's pretty gross overkill for a 15 V rail.

**Dave Jones:** No wonder they're getting that thing up to 70°. Unbelievable. We're getting exactly the same on the negative rail, too. Check it out, you know, around about that 22 24 V, something like that.

**Dave Jones:** Nuts. So, unfortunately, yeah, EEVblog curse again. It's incredibly simple, nothing complex as I was hoping. Like a regulator would have been blown, at least something, but no. Anyway, all it was was a missing heatsink.

**Dave Jones:** Why that heatsink was missing, I don't know. Absolute mystery, ridiculous. Didn't find it inside the box. I don't know. Somebody's been playing around with this thing. It's ridiculous. Anyway, we're getting our AC and DC coupling on there properly.

**Dave Jones:** We've measured all the voltage rails, the plus minus 15 V rails on both analog boards. We measured the input to make sure that the ripple is well above the minimum dropout voltage of the regulators and yeah, pretty piss-poor design in there.

**Dave Jones:** Not that happy with that at all. The margins in there maybe they might be slightly different because I've got I'm running over 240 V here in the lab, like in 245 or something nominal, I think, here in the lab.

**Dave Jones:** So, quite a high supply voltage. So, mine might be on the high side of the margin, that's for sure. Or they certainly will be, but yeah, anyway, not that pleased with the power supply thermal design of this thing.

**Dave Jones:** Pretty poor. As I said, they could have done away with that fan. Mounted design the power supply properly and then mounted on some big aluminum blocks down to the chassis or something.

**Dave Jones:** And really this thing doesn't consume a huge amount of power. So, you could easily get away with putting those things to the chassis and having this a completely fanless design.

**Dave Jones:** It's just no excuse for it. It's just It's just poor form. It really is laziness. So, I'm going to have to do some more work testing this thing, but we can do you know the AC and DC coupling works a treat now.

**Dave Jones:** It seems to the relays haven't actually measured it, but we can go up in the input gain. Notice the overload LED slightly starts to come come on at the maximum gain.

**Dave Jones:** We can actually make that go away. Put a terminator on the input here cuz we've got channel A selected and bang, it's gone. And similar thing on B, we can go over and we can test B.

**Dave Jones:** Look at that. Beautiful. And we can go A minus B here the differential input mode we're still overloading. We'll need a second terminator on there. Look at that. Bob's your uncle.

**Dave Jones:** What a Bobby dazzler. I love it. It's a winner. Anyway, I hope you enjoyed that little follow-up video even though sorry, there wasn't much happening there at all. What a bummer.

**Dave Jones:** Anyway, just a missing heatsink. Meh. Hope you enjoyed it. Catch you next time.
