---
video_id: BFLZm4LbzQU
title: EEVblog #441 - How To Track Down Common Mode Noise
url: https://www.youtube.com/watch?v=BFLZm4LbzQU
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 29, "3": 47, "4": 62, "5": 77, "6": 92, "7": 109, "8": 123, "9": 140, "10": 152, "11": 167, "12": 180, "13": 199, "14": 216, "15": 230, "16": 243, "17": 258, "18": 271, "19": 282, "20": 297, "21": 310, "22": 323, "23": 339, "24": 355, "25": 368, "26": 384, "27": 400, "28": 423, "29": 439, "30": 452, "31": 473, "32": 488, "33": 502, "34": 521, "35": 540, "36": 556, "37": 575, "38": 589, "39": 609, "40": 623, "41": 639, "42": 661, "43": 677, "44": 689, "45": 704, "46": 716, "47": 730, "48": 742, "49": 764, "50": 776, "51": 789, "52": 802, "53": 818, "54": 832, "55": 844, "56": 860, "57": 877, "58": 891, "59": 906, "60": 926, "61": 946, "62": 962, "63": 982, "64": 996, "65": 1012, "66": 1029, "67": 1045, "68": 1058, "69": 1070, "70": 1083, "71": 1095, "72": 1112, "73": 1127, "74": 1142, "75": 1157, "76": 1170, "77": 1185, "78": 1204, "79": 1215, "80": 1227, "81": 1240, "82": 1258, "83": 1273}
---

**Dave Jones:** Hi, this is just going to be a quick little aside video from something I found during the testing of the review of this 18 power supply unit. I thought I'd just make a quick separate video about this rather than include it you

**Dave Jones:** know somewhere in the middle of this review video. So if you want to check the review of this thing, check it out. Now what I'm doing is I'm measuring the noise performance of the output noise of this power supply and the way I'm doing that

**Dave Jones:** is I've just got a my BNC to banana plug adapter there my going straight into the scope via a coax of course and I've got my scope set up for a bandwidth limit. Now that's quite important because the specs usually of a power

**Dave Jones:** supply let's take a look at it. The ripple here in this case there it is 20 hertz to 20 megahertz. So it's a 20 megahertz bandwidth limited range and that's what the bandwidth limit on your scope does and if you turn it off let's

**Dave Jones:** have a look at the display at the moment. Okay, that's with the bandwidth limit on let's turn it off. And you'll see that the noise is very significantly peak to peak noise there very significantly higher than if you've got

**Dave Jones:** the bandwidth limit down to 20 megahertz. So you definitely want to measure the performance over that limit but look what we're getting here. Okay, this is supposed to be a linear power supply quite quiet. Okay, now the spec

**Dave Jones:** is 1 millivolt RMS of course there it is 1 millivolt RMS there. Now RMS is the key it doesn't tell you anything about peak to peak but you look at this and you go well why are we getting the switching

**Dave Jones:** effect here? This is not a switching power supply. So where's it coming from? Is it coming from the um circuit in uh inside here is it coming like the display refresh or something like that? Is it coming from internal from the

**Dave Jones:** power supply? Well, we'll find out in a second. Let's take a look at it. 5 microseconds per division, three divisions, that's 66.6 kHz or thereabouts. Significant switching, you know, component there. It dominates that display. And if you weren't careful, if

**Dave Jones:** you just hooked this up and you didn't know what you were doing, you might think, "Well, this is coming out of this power supply. Well, this is a [ __ ] power supply. It's Look at this switching. It's horrible." You know,

**Dave Jones:** but is it coming from this power supply? Huh, you may guess the answer. No, it's not. And let's find out why. Now, the first thing we might check is that what happens when you disconnect it. Okay, you disconnect it, goes away. Not a

**Dave Jones:** problem. Let's connect one side of it to it. Not a problem. Connect the other side. Well, we're just getting 50 Hz garbage on there. Right, so let's not worry about that too much, but look, you can see the

**Dave Jones:** switching component, folks, is still I accidentally hit it. Switching component is still in there. There it is there. You can see it. So, it's coming It's definitely coming through this power supply. So, you still might think, "Okay, this power supply is the

**Dave Jones:** culprit." But let's switch the output off, okay? So, the relay, it should disconnect the output there. So, let's There we go. Switch all of the outputs off. There we go. Our outputs are physically disconnected. It's switched off and it's

**Dave Jones:** disconnected those outputs, but it's still there. You'll notice that the noise really doesn't change much at all whether or not you got that output on or off. And next up, you might think, "Well, is this BNC Look, is this coax?"

**Dave Jones:** Move it around. Look, it seems to a little bit changing a little bit there. It's sort of, you know, picking up stuff. So, I don't know. Is it the BNC? Well, let's use a different BNC. So, as you can see, the switching is still

**Dave Jones:** there even with this different BNC cable. So, it's not that. It's not picking it up. So, what do we try next to try and figure out the source of this switching frequency? Because, well, is it the power supply? Because that's the thing,

**Dave Jones:** right? If you're doing these these sorts of measurements, you have to know exactly where all your noise sources are coming from. And I know for a fact it's not within this power supply. So, I'm going to let you try and guess where

**Dave Jones:** it's coming from. We're going to try and hunt it down. So, what we're going to do now is, well, is there any any other lab gear around here sort of, you know, picking up noise? Maybe this coax ain't that

**Dave Jones:** good, right? Is it picking up noise somewhere or because it's not shielded all the way in? Maybe it's picking up noise somewhere else. Hmm. Well, let's try a very simple thing. Let's just switch the power supply off and see what happens.

**Dave Jones:** Aha! Look at that, folks. It's still coming through. It's being picked up. What do we do next? Let's pull the mains plug on this thing.

**Dave Jones:** Look at that. I just pulled the mains plug and it's still coming through. What do we try next? Well, let's try a real scope probe. You know, I got my 500 MHz Agilent scope probe here, right? It's a

**Dave Jones:** real fair dinkum probe. And look, I've even got my antenna earth loop there. And look, we're not picking up anything at all. Now, I'm using my scope probe to connect up to the power supply here and look, it appears to have gone, but let's

**Dave Jones:** stop that. Bingo, it ain't gone. Look, it's still there. There it is, three divisions, one, two, three. That's 66.6 kHz still there. So, we are getting a better result because this is a much higher quality five, you know, proper

**Dave Jones:** shielded, you know, oscilloscope probe as opposed to just, you know, some regular coax which may not have 100% coverage, but we're still picking it up. So, I've gone back to my regular coax here just so we can see the effect again. And mains

**Dave Jones:** cable or no mains cable on this supply, powered up or not powered up, it makes no difference. We're still getting that switching noise. Is this power supply magic? Is even when it's not powered, is it magically generating this switching

**Dave Jones:** frequency? No, of course not. It's picking it up somewhere. All right, so I suspect it's common mode noise being picked up through the main system and because this oscilloscope is mains earth referenced, and as you saw in my the

**Dave Jones:** mysterious oscilloscope phenomenon, you can actually get ESD impulses which jump onto the coax cable onto the lead and then into because this oscilloscope only has so much common mode rejection from the mains can actually generate input noise coupled through the earth system.

**Dave Jones:** Now, what I've got is this isolation transformer here. And this physically removes the mains earth and isolates this. So, it effectively turns this oscilloscope in it's not mains earth reference anymore. So, now you can use your scope probe to probe your circuits

**Dave Jones:** so you don't blow them up. Etcetera, but it it cuz it physically removes the earth on this thing, it's not recommended to do this, by the way, power your scope. Usually, you power your product through this thing and not your scope. Or you use a

**Dave Jones:** proper high voltage probe. That's for a different um video, but look, it's physically changed. Now, it's still there, but it's look, it's different. We've got different components picked up. We're still five microseconds per division there, but it's not that consistent 66.6 kHz we saw

**Dave Jones:** before. So, aha, we're getting closer to this thing. And you'll And you'll see that it'll instantly go back. If I plug the proper mains cable back into this thing, it'll instantly go back to exactly what we saw before. So, we're

**Dave Jones:** tracking this thing down. So, what we've got is some sort of switching device somewhere either in the room or on the mains distribution system that is causing this things. And just to show you that it's not the Agilent oscilloscope doing this,

**Dave Jones:** here it is on a Rigol scope. Five microseconds per division, exactly the same thing happening. So, what do you do? You start looking for things that are either within the direct vicinity that are switching or something that's connected to the mains system. So, you

**Dave Jones:** start by Well, I've got my lights up here, my LED lights. I'll switch those off. Does it make a difference? No, nothing. It's not those. Not a problem. Um is it the fluoro lights in the lab? Well, only one way to find out.

**Dave Jones:** No. Look at that. Still exactly the same. And it's none of my gear. I've turned all my gear off on the lab. I've switched the computer off in the office cubicle I've got in here, and I still can't find it. So,

**Dave Jones:** what is it? Let's go investigate under here. Now, here is all of my power boards. They're all connected down to the one, and there's a whole bunch more powering my electronics bench over there as opposed to my teardown bench. So,

**Dave Jones:** these ones here, there's a you know, there's a few things plugged in. Let's have a look. There's What have we got? No, we've just got a mains cable that's going off to nothing. Nothing going up to gear that I know is switched off.

**Dave Jones:** Aha, what is this? What is this? What is this? Hello, Mr. Quealy power. Hmm. Well, there's only one way to find out. I've now switched this down to 2 mV per division. You see we're getting the huge noise there. I'm still measuring the

**Dave Jones:** output direct on the power supply, by the way. Well, it's not switched on. There we go. Now it's switched on. There we go. So, we're picking up that noise there. What you would think is noise coming from this power supply if you didn't

**Dave Jones:** know how to measure things properly. Let's disconnect this stupid Quealy Look at that. Switching power supply. Look at it go up as I put it near that coax. Look. Bastards. So, let's I'm going to pull the cord on this. I'm just going to yank

**Dave Jones:** it. Here we go. Ta-da! We found our culprit, folks. One of these switching cheap-ass switching power supplies plugged into the same mains board as what I was powering my oscilloscope and my A10 power supply from. Bingo. Big trap for young players.

**Dave Jones:** So, there you go. We're now at 5 mV per division and you can see that we're still picking up noise and that is most likely more common mode noise between the earth and the neutral in the mains system, but we've gotten rid of that

**Dave Jones:** huge spike which we were getting before that was upsetting our measurements. So, we can try and track down our sources of this type of common mode noise. We can filter our mains and do all sorts of stuff like that to reduce it, but I'm

**Dave Jones:** pretty happy now that we've actually gotten rid of that huge um 66 kHz spike we're getting from that switching power supply. And of course, if we go back to our original issue and just disconnect it from there, bingo,

**Dave Jones:** we're no more noise and we can even go down to 500 microvolts, you know, per division and we're sweet there. Why is that not updating? Uh bloody firmware in this thing. I haven't got the latest firmware for this

**Dave Jones:** uh Rigol scope yet, so it has some uh freezing issues with the horizontal mode, but there you go, that's 500 microvolts per division. Switch that, put that in, we pick up a bit more. We put it over on our

**Dave Jones:** power supply over here and we're going to pick up a butt load of common mode noise. But that's not coming from our power supply. So you might be asking, well, why was this thing picking it up even though

**Dave Jones:** it's switched off and disconnected from the mains like that? Well, it's because um the internal circuitry and the internal transformer in here is um effectively uh via AC um coupling is effectively working as a very effective uh you know, pick up antenna, so to speak,

**Dave Jones:** and that's why uh this oscilloscope probe won't pick it up cuz this is a relatively high frequency pick up coil, okay? It's going to pick up, you know, ESD and lots of high frequency discharges and stuff like that as I've

**Dave Jones:** shown in previous videos. So the transformer inside here and the coupling uh to it is basically going to uh effectively work as a better uh lower frequency pick up antenna for that stuff. That's why if we disconnect it,

**Dave Jones:** bingo, we gone, okay? But we hook it up, this thing's entirely switched off, disconnected from the mains plug, so it's not actually picking it up through the mains earth, it's still working as a very effective antenna for picking up

**Dave Jones:** that common mode noise. And common mode noise uh comes in all types, folks. It can come from anywhere. Be careful. Watch this. Going to grab this coax with one hand, touch the screen over here. No, folks. It ain't magic. It's picking

**Dave Jones:** up the noise, the switching that refresh of the screen there. Look at that. Woohoo! And of course, that is one of the claimed Well, it is one of the disadvantages of these digital scopes is that they can be spewing out stuff,

**Dave Jones:** which can interfere with low value measurements. So, that's why, you know, a lot of the gray beards frown upon these digital scopes because they can, you know, be generating all sorts of crap. You won't get this sort of thing

**Dave Jones:** happening with an analog scope. So, what are we going to do when measuring our A10 power supply here? We know it's a linear supply. It's not spewing out any switching stuff. So, all these high frequency peaks in here

**Dave Jones:** are common mode noise coming from somewhere else in our measurement system. So, when we're measuring the noise on a linear power supply like this A10 power supply, we know that these high frequency switching components in here are effectively a common mode noise

**Dave Jones:** being picked up somewhere else in the system. So, really, you want to chop those out and only look at that in there. So, as you can see, even though we got rid of that main source, we're still picking up, you know, a lot of

**Dave Jones:** common mode noise in here. And unfortunately, that's going to be hard to get rid of. Now, even if I power both the scope and the power supply through a filter, a mains input filter board, so I've got both bits of gear, that's the

**Dave Jones:** only thing off that filter, we're still picking up this pain in the ass common mode noise here. Look at that. So, what's that coming from? Well, we go full circle back to something that we tested before. Our lights. Let's turn it off.

**Dave Jones:** Look at that, folks. Bingo. So, now we're talking. We've started to eliminate all of our problems here and getting towards more of the real noise performance of this um power supply. So, really we still have That's me, by the way. Be careful. There

**Dave Jones:** you go. So, that's um we're getting very, very close to still one is a still a a burst in there that's triggering off that. So, it's obviously Well, probably we can move our trigger around and uh There we go. We can single shot a

**Dave Jones:** capture off that. So, there is some another burst event coming in there, but really um that, folks, now we can at least get a more decent measurement of our power supply. You can see how this is originally had a um

**Dave Jones:** a common mode noise source directly a switching power supply directly on there. We thought we eliminated the lights, but we didn't. Let's switch those lights back on. Look at that. Unbelievable. Woohoo! They're the LED lights I've got up the top, and they're

**Dave Jones:** not even supposed to be PWM and they're supposed to be constantly uh on at maximum brightness there. I can turn my other set of LED lights above does absolutely nothing, but those lights I've got up there, big switching

**Dave Jones:** noise. So, we came full circle there, and we're getting closer to eliminating everything. So, let's actually look at the differences in the uh quality of some coaxials. I've got this uh particular coax cable here. We're 2 mV per division. I'll keep it on that. And

**Dave Jones:** uh that, you can see, we're picking up lots of uh high frequency common mode noise there. Now, you'll see that the bulk of the uh ripple and noise in there is going to pretty much stay consistent between these. Now, let me try

**Dave Jones:** another uh coax cable here. It's roughly the same length, but it's going to be a different type with a different uh outer weave. So, here's this other one, and you can see that it is a particularly cleaner. I mean, if we

**Dave Jones:** put it near the screen there, there we go. That's why the other one was picking up uh so much crap. The The weave wasn't as good, shield wasn't as good, and it's picking up uh more of that uh stuff from

**Dave Jones:** the screen. Now, if we disconnect that, and we plug in our uh scope probe, our proper scope probe. This is the 350 MHz one which comes with the Rigol, and it's got a times one times 10 switch. So, we'll put

**Dave Jones:** it on times one, so it's operating just like a regular coax, and I've got this little um coax adapter. It's a bit loose, so uh please forgive me if uh it's the connection is a bit intermittent. There, I may have to hold

**Dave Jones:** it. There you go. Look at that. We're suddenly with this good quality um a properly shielded high bandwidth oscilloscope probe, look, it's not picking up nearly as much. So, our performance has gone from, you know, pretty, you know,

**Dave Jones:** uh sort of fairly ordinary. We're still at the same uh volts per division, 2 mV per division, but much cleaner with the scope probe. Now, let's put it on times 10, and then we have to uh compensate. We've got to go in here, and we've got

**Dave Jones:** to turn that to times 10, and then we're on 20 mV per division. We've got to uh we can't actually go down to 2 mV per division because we're we have to be 5 mV per division, and it's higher. Why is the

**Dave Jones:** noise higher on times 10? Well, it's because a times 10 oscilloscope probe is higher bandwidth than it is on times one. And if you don't believe me, here's the spec sheet for it. There it is. Bandwidth times one DC to 8 MHz, times

**Dave Jones:** 10 DC to 350 MHz. This is the spec sheet for this Rigol probe. And all probes are the same. That's why a lot of them only come times 10 because they give you the high bandwidth due to the input

**Dave Jones:** capacitance. I won't go into it. That's a whole separate video. But times 10 probes, that's why they're used, is because they are higher bandwidth. So, effectively we've gone from that 20 meg filtering on our scope to an 8 MHz

**Dave Jones:** bandwidth filtering. And that's why our times one probe is actually going to give us a lower noise measurement because it's bandwidth limited. So, all that high frequency noise, wherever it's coming from, is being attenuated. So, really, because the bandwidth of this power supply is

**Dave Jones:** specified from 0 to 20 MHz, we can't just use our scope probe on times one cuz it's only giving us in this for this probe only giving us an 8 MHz bandwidth. So, we have to put up with the fact that

**Dave Jones:** we're using a times 10 probe. And here's a Agilent one. This is my 500 MHz high quality Agilent probe. And that is five We can only go down to 5 mV per division because of the times 10. But there you

**Dave Jones:** go. That, folks, you still get the occasional high frequency glitch in there you might be able to see. In fact, we can probably even trigger off that. And there we go. Yep, we can actually trigger off that. See the occasional

**Dave Jones:** little high frequency pulse which is coming through, but not a big deal. So, there you go. Now, we can measure our noise with reasonable performance. Excellent. So, there you go. I hope you found that interesting. That just goes to show that

**Dave Jones:** there's more to a simple noise measurement than meets the eye. Common mode noise, go look it up. Go research it. Can be a real pain in the ass and a big trap for young and old players alike. Let me tell you. So, if you like

**Dave Jones:** that, please give it a big thumbs up and if you want to discuss it, jump on over to the EVE blog forum. Catch you next time.
