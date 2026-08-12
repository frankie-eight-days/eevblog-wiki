---
video_id: BFLZm4LbzQU
title: EEVblog #441 - How To Track Down Common Mode Noise
url: https://www.youtube.com/watch?v=BFLZm4LbzQU
source: youtube-asr
timestamps: {"0": 0, "1": 16, "2": 42, "3": 52, "4": 64, "5": 79, "6": 97, "7": 109, "8": 121, "9": 132, "10": 146, "11": 155, "12": 167, "13": 184, "14": 202, "15": 217, "16": 230, "17": 239, "18": 248, "19": 264, "20": 273, "21": 283, "22": 291, "23": 310, "24": 320, "25": 339, "26": 363, "27": 375, "28": 387, "29": 423, "30": 435, "31": 446, "32": 457, "33": 473, "34": 486, "35": 499, "36": 510, "37": 524, "38": 540, "39": 554, "40": 572, "41": 584, "42": 604, "43": 611, "44": 626, "45": 637, "46": 657, "47": 680, "48": 697, "49": 709, "50": 725, "51": 734, "52": 747, "53": 771, "54": 788, "55": 804, "56": 815, "57": 835, "58": 844, "59": 864, "60": 880, "61": 891, "62": 912, "63": 926, "64": 944, "65": 961, "66": 976, "67": 987, "68": 1001, "69": 1016, "70": 1026, "71": 1043, "72": 1056, "73": 1070, "74": 1081, "75": 1093, "76": 1105, "77": 1119, "78": 1130, "79": 1142, "80": 1155, "81": 1170, "82": 1185, "83": 1199, "84": 1213, "85": 1219, "86": 1232, "87": 1242, "88": 1261, "89": 1270}
---

**Dave Jones:** Hi, this is just going to be a quick little aside video from something I found during the testing of the review of this 18 power supply unit. I thought I'd just make a quick separate video about this rather than include it you know somewhere in the middle of this review video.

**Dave Jones:** So if you want to check the review of this thing, check it out. Now what I'm doing is I'm measuring the noise performance of the output noise of this power supply and the way I'm doing that is I've just got a my BNC to banana plug adapter there my going straight into the scope via a coax of course and I've got my scope set up for a bandwidth

**Dave Jones:** limit. Now that's quite important because the specs usually of a power supply let's take a look at it. The ripple here in this case there it is 20 hertz to 20 megahertz.

**Dave Jones:** So it's a 20 megahertz bandwidth limited range and that's what the bandwidth limit on your scope does and if you turn it off let's have a look at the display at the moment.

**Dave Jones:** Okay, that's with the bandwidth limit on let's turn it off. And you'll see that the noise is very significantly peak to peak noise there very significantly higher than if you've got the bandwidth limit down to 20 megahertz.

**Dave Jones:** So you definitely want to measure the performance over that limit but look what we're getting here. Okay, this is supposed to be a linear power supply quite quiet. Okay, now the spec is 1 millivolt RMS of course there it is 1 millivolt RMS there.

**Dave Jones:** Now RMS is the key it doesn't tell you anything about peak to peak but you look at this and you go well why are we getting the switching effect here?

**Dave Jones:** This is not a switching power supply. So where's it coming from? Is it coming from the um circuit in uh inside here is it coming like the display refresh or something like that?

**Dave Jones:** Is it coming from internal from the power supply? Well, we'll find out in a second. Let's take a look at it. 5 microseconds per division, three divisions, that's 66.6 kHz or thereabouts.

**Dave Jones:** Significant switching, you know, component there. It dominates that display. And if you weren't careful, if you just hooked this up and you didn't know what you were doing, you might think, "Well, this is coming out of this power supply.

**Dave Jones:** Well, this is a [ __ ] power supply. It's Look at this switching. It's horrible." You know, but is it coming from this power supply? Huh, you may guess the answer.

**Dave Jones:** No, it's not. And let's find out why. Now, the first thing we might check is that what happens when you disconnect it. Okay, you disconnect it, goes away. Not a problem.

**Dave Jones:** Let's connect one side of it to it. Not a problem. Connect the other side. Well, we're just getting 50 Hz garbage on there. Right, so let's not worry about that too much, but look, you can see the switching component, folks, is still I accidentally hit it.

**Dave Jones:** Switching component is still in there. There it is there. You can see it. So, it's coming It's definitely coming through this power supply. So, you still might think, "Okay, this power supply is the culprit." But let's switch the output off, okay?

**Dave Jones:** So, the relay, it should disconnect the output there. So, let's There we go. Switch all of the outputs off. There we go. Our outputs are physically disconnected. It's switched off and it's disconnected those outputs, but it's still there.

**Dave Jones:** You'll notice that the noise really doesn't change much at all whether or not you got that output on or off. And next up, you might think, "Well, is this BNC Look, is this coax?"

**Dave Jones:** Move it around. Look, it seems to a little bit changing a little bit there. It's sort of, you know, picking up stuff. So, I don't know. Is it the BNC?

**Dave Jones:** Well, let's use a different BNC. So, as you can see, the switching is still there even with this different BNC cable. So, it's not that. It's not picking it up.

**Dave Jones:** So, what do we try next to try and figure out the source of this switching frequency? Because, well, is it the power supply? Because that's the thing, right? If you're doing these these sorts of measurements, you have to know exactly where all your noise sources are coming from.

**Dave Jones:** And I know for a fact it's not within this power supply. So, I'm going to let you try and guess where it's coming from. We're going to try and hunt it down.

**Dave Jones:** So, what we're going to do now is, well, is there any any other lab gear around here sort of, you know, picking up noise? Maybe this coax ain't that good, right?

**Dave Jones:** Is it picking up noise somewhere or because it's not shielded all the way in? Maybe it's picking up noise somewhere else. Hmm. Well, let's try a very simple thing.

**Dave Jones:** Let's just switch the power supply off and see what happens. Aha! Look at that, folks. It's still coming through. It's being picked up. What do we do next? Let's pull the mains plug on this thing.

**Dave Jones:** Look at that. I just pulled the mains plug and it's still coming through. What do we try next? Well, let's try a real scope probe. You know, I got my 500 MHz Agilent scope probe here, right?

**Dave Jones:** It's a real fair dinkum probe. And look, I've even got my antenna earth loop there. And look, we're not picking up anything at all. Now, I'm using my scope probe to connect up to the power supply here and look, it appears to have gone, but let's stop that.

**Dave Jones:** Bingo, it ain't gone. Look, it's still there. There it is, three divisions, one, two, three. That's 66.6 kHz still there. So, we are getting a better result because this is a much higher quality five, you know, proper shielded, you know, oscilloscope probe as opposed to just, you know, some regular coax which may not have 100% coverage, but we're still picking it up.

**Dave Jones:** So, I've gone back to my regular coax here just so we can see the effect again. And mains cable or no mains cable on this supply, powered up or not powered up, it makes no difference.

**Dave Jones:** We're still getting that switching noise. Is this power supply magic? Is even when it's not powered, is it magically generating this switching frequency? No, of course not. It's picking it up somewhere.

**Dave Jones:** All right, so I suspect it's common mode noise being picked up through the main system and because this oscilloscope is mains earth referenced, and as you saw in my the mysterious oscilloscope phenomenon, you can actually get ESD impulses which jump onto the coax cable onto the lead and then into because this oscilloscope only has so much common mode rejection from the mains can actually generate input noise coupled through the earth system.

**Dave Jones:** Now, what I've got is this isolation transformer here. And this physically removes the mains earth and isolates this. So, it effectively turns this oscilloscope in it's not mains earth reference anymore.

**Dave Jones:** So, now you can use your scope probe to probe your circuits so you don't blow them up. Etcetera, but it it cuz it physically removes the earth on this thing, it's not recommended to do this, by the way, power your scope.

**Dave Jones:** Usually, you power your product through this thing and not your scope. Or you use a proper high voltage probe. That's for a different um video, but look, it's physically changed.

**Dave Jones:** Now, it's still there, but it's look, it's different. We've got different components picked up. We're still five microseconds per division there, but it's not that consistent 66.6 kHz we saw before.

**Dave Jones:** So, aha, we're getting closer to this thing. And you'll And you'll see that it'll instantly go back. If I plug the proper mains cable back into this thing, it'll instantly go back to exactly what we saw before.

**Dave Jones:** So, we're tracking this thing down. So, what we've got is some sort of switching device somewhere either in the room or on the mains distribution system that is causing this things.

**Dave Jones:** And just to show you that it's not the Agilent oscilloscope doing this, here it is on a Rigol scope. Five microseconds per division, exactly the same thing happening. So, what do you do?

**Dave Jones:** You start looking for things that are either within the direct vicinity that are switching or something that's connected to the mains system. So, you start by Well, I've got my lights up here, my LED lights.

**Dave Jones:** I'll switch those off. Does it make a difference? No, nothing. It's not those. Not a problem. Um is it the fluoro lights in the lab? Well, only one way to find out.

**Dave Jones:** No. Look at that. Still exactly the same. And it's none of my gear. I've turned all my gear off on the lab. I've switched the computer off in the office cubicle I've got in here, and I still can't find it.

**Dave Jones:** So, what is it? Let's go investigate under here. Now, here is all of my power boards. They're all connected down to the one, and there's a whole bunch more powering my electronics bench over there as opposed to my teardown bench.

**Dave Jones:** So, these ones here, there's a you know, there's a few things plugged in. Let's have a look. There's What have we got? No, we've just got a mains cable that's going off to nothing.

**Dave Jones:** Nothing going up to gear that I know is switched off. Aha, what is this? What is this? What is this? Hello, Mr. Quealy power. Hmm. Well, there's only one way to find out.

**Dave Jones:** I've now switched this down to 2 mV per division. You see we're getting the huge noise there. I'm still measuring the output direct on the power supply, by the way.

**Dave Jones:** Well, it's not switched on. There we go. Now it's switched on. There we go. So, we're picking up that noise there. What you would think is noise coming from this power supply if you didn't know how to measure things properly.

**Dave Jones:** Let's disconnect this stupid Quealy Look at that. Switching power supply. Look at it go up as I put it near that coax. Look. Bastards. So, let's I'm going to pull the cord on this.

**Dave Jones:** I'm just going to yank it. Here we go. Ta-da! We found our culprit, folks. One of these switching cheap-ass switching power supplies plugged into the same mains board as what I was powering my oscilloscope and my A10 power supply from.

**Dave Jones:** Bingo. Big trap for young players. So, there you go. We're now at 5 mV per division and you can see that we're still picking up noise and that is most likely more common mode noise between the earth and the neutral in the mains system, but we've gotten rid of that huge spike which we were getting before that was upsetting our measurements.

**Dave Jones:** So, we can try and track down our sources of this type of common mode noise. We can filter our mains and do all sorts of stuff like that to reduce it, but I'm pretty happy now that we've actually gotten rid of that huge um 66 kHz spike we're getting from that switching power supply.

**Dave Jones:** And of course, if we go back to our original issue and just disconnect it from there, bingo, we're no more noise and we can even go down to 500 microvolts, you know, per division and we're sweet there.

**Dave Jones:** Why is that not updating? Uh bloody firmware in this thing. I haven't got the latest firmware for this uh Rigol scope yet, so it has some uh freezing issues with the horizontal mode, but there you go, that's 500 microvolts per division.

**Dave Jones:** Switch that, put that in, we pick up a bit more. We put it over on our power supply over here and we're going to pick up a butt load of common mode noise.

**Dave Jones:** But that's not coming from our power supply. So you might be asking, well, why was this thing picking it up even though it's switched off and disconnected from the mains like that?

**Dave Jones:** Well, it's because um the internal circuitry and the internal transformer in here is um effectively uh via AC um coupling is effectively working as a very effective uh you know, pick up antenna, so to speak, and that's why uh this oscilloscope probe won't pick it up cuz this is a relatively high frequency pick up coil, okay?

**Dave Jones:** It's going to pick up, you know, ESD and lots of high frequency discharges and stuff like that as I've shown in previous videos. So the transformer inside here and the coupling uh to it is basically going to uh effectively work as a better uh lower frequency pick up antenna for that stuff.

**Dave Jones:** That's why if we disconnect it, bingo, we gone, okay? But we hook it up, this thing's entirely switched off, disconnected from the mains plug, so it's not actually picking it up through the mains earth, it's still working as a very effective antenna for picking up that common mode noise.

**Dave Jones:** And common mode noise uh comes in all types, folks. It can come from anywhere. Be careful. Watch this. Going to grab this coax with one hand, touch the screen over here.

**Dave Jones:** No, folks. It ain't magic. It's picking up the noise, the switching that refresh of the screen there. Look at that. Woohoo! And of course, that is one of the claimed Well, it is one of the disadvantages of these digital scopes is that they can be spewing out stuff, which can interfere with low value measurements.

**Dave Jones:** So, that's why, you know, a lot of the gray beards frown upon these digital scopes because they can, you know, be generating all sorts of crap. You won't get this sort of thing happening with an analog scope.

**Dave Jones:** So, what are we going to do when measuring our A10 power supply here? We know it's a linear supply. It's not spewing out any switching stuff. So, all these high frequency peaks in here are common mode noise coming from somewhere else in our measurement system.

**Dave Jones:** So, when we're measuring the noise on a linear power supply like this A10 power supply, we know that these high frequency switching components in here are effectively a common mode noise being picked up somewhere else in the system.

**Dave Jones:** So, really, you want to chop those out and only look at that in there. So, as you can see, even though we got rid of that main source, we're still picking up, you know, a lot of common mode noise in here.

**Dave Jones:** And unfortunately, that's going to be hard to get rid of. Now, even if I power both the scope and the power supply through a filter, a mains input filter board, so I've got both bits of gear, that's the only thing off that filter, we're still picking up this pain in the ass common mode noise here.

**Dave Jones:** Look at that. So, what's that coming from? Well, we go full circle back to something that we tested before. Our lights. Let's turn it off. Look at that, folks.

**Dave Jones:** Bingo. So, now we're talking. We've started to eliminate all of our problems here and getting towards more of the real noise performance of this um power supply. So, really we still have That's me, by the way.

**Dave Jones:** Be careful. There you go. So, that's um we're getting very, very close to still one is a still a a burst in there that's triggering off that. So, it's obviously Well, probably we can move our trigger around and uh There we go.

**Dave Jones:** We can single shot a capture off that. So, there is some another burst event coming in there, but really um that, folks, now we can at least get a more decent measurement of our power supply.

**Dave Jones:** You can see how this is originally had a um a common mode noise source directly a switching power supply directly on there. We thought we eliminated the lights, but we didn't.

**Dave Jones:** Let's switch those lights back on. Look at that. Unbelievable. Woohoo! They're the LED lights I've got up the top, and they're not even supposed to be PWM and they're supposed to be constantly uh on at maximum brightness there.

**Dave Jones:** I can turn my other set of LED lights above does absolutely nothing, but those lights I've got up there, big switching noise. So, we came full circle there, and we're getting closer to eliminating everything.

**Dave Jones:** So, let's actually look at the differences in the uh quality of some coaxials. I've got this uh particular coax cable here. We're 2 mV per division. I'll keep it on that.

**Dave Jones:** And uh that, you can see, we're picking up lots of uh high frequency common mode noise there. Now, you'll see that the bulk of the uh ripple and noise in there is going to pretty much stay consistent between these.

**Dave Jones:** Now, let me try another uh coax cable here. It's roughly the same length, but it's going to be a different type with a different uh outer weave. So, here's this other one, and you can see that it is a particularly cleaner.

**Dave Jones:** I mean, if we put it near the screen there, there we go. That's why the other one was picking up uh so much crap. The The weave wasn't as good, shield wasn't as good, and it's picking up uh more of that uh stuff from the screen.

**Dave Jones:** Now, if we disconnect that, and we plug in our uh scope probe, our proper scope probe. This is the 350 MHz one which comes with the Rigol, and it's got a times one times 10 switch.

**Dave Jones:** So, we'll put it on times one, so it's operating just like a regular coax, and I've got this little um coax adapter. It's a bit loose, so uh please forgive me if uh it's the connection is a bit intermittent.

**Dave Jones:** There, I may have to hold it. There you go. Look at that. We're suddenly with this good quality um a properly shielded high bandwidth oscilloscope probe, look, it's not picking up nearly as much.

**Dave Jones:** So, our performance has gone from, you know, pretty, you know, uh sort of fairly ordinary. We're still at the same uh volts per division, 2 mV per division, but much cleaner with the scope probe.

**Dave Jones:** Now, let's put it on times 10, and then we have to uh compensate. We've got to go in here, and we've got to turn that to times 10, and then we're on 20 mV per division.

**Dave Jones:** We've got to uh we can't actually go down to 2 mV per division because we're we have to be 5 mV per division, and it's higher. Why is the noise higher on times 10?

**Dave Jones:** Well, it's because a times 10 oscilloscope probe is higher bandwidth than it is on times one. And if you don't believe me, here's the spec sheet for it. There it is.

**Dave Jones:** Bandwidth times one DC to 8 MHz, times 10 DC to 350 MHz. This is the spec sheet for this Rigol probe. And all probes are the same. That's why a lot of them only come times 10 because they give you the high bandwidth due to the input capacitance.

**Dave Jones:** I won't go into it. That's a whole separate video. But times 10 probes, that's why they're used, is because they are higher bandwidth. So, effectively we've gone from that 20 meg filtering on our scope to an 8 MHz bandwidth filtering.

**Dave Jones:** And that's why our times one probe is actually going to give us a lower noise measurement because it's bandwidth limited. So, all that high frequency noise, wherever it's coming from, is being attenuated.

**Dave Jones:** So, really, because the bandwidth of this power supply is specified from 0 to 20 MHz, we can't just use our scope probe on times one cuz it's only giving us in this for this probe only giving us an 8 MHz bandwidth.

**Dave Jones:** So, we have to put up with the fact that we're using a times 10 probe. And here's a Agilent one. This is my 500 MHz high quality Agilent probe.

**Dave Jones:** And that is five We can only go down to 5 mV per division because of the times 10. But there you go. That, folks, you still get the occasional high frequency glitch in there you might be able to see.

**Dave Jones:** In fact, we can probably even trigger off that. And there we go. Yep, we can actually trigger off that. See the occasional little high frequency pulse which is coming through, but not a big deal.

**Dave Jones:** So, there you go. Now, we can measure our noise with reasonable performance. Excellent. So, there you go. I hope you found that interesting. That just goes to show that there's more to a simple noise measurement than meets the eye.

**Dave Jones:** Common mode noise, go look it up. Go research it. Can be a real pain in the ass and a big trap for young and old players alike. Let me tell you.

**Dave Jones:** So, if you like that, please give it a big thumbs up and if you want to discuss it, jump on over to the EVE blog forum. Catch you next time.
