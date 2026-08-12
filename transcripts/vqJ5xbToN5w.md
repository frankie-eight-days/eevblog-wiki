---
video_id: vqJ5xbToN5w
title: EEVblog 1631 - $230 Micsig MDP700 HV Differential Probe Review
url: https://www.youtube.com/watch?v=vqJ5xbToN5w
source: youtube-asr
---

**Dave Jones:** Hi, let's take a look at the new Micsig MDP series high voltage differential probe. Now, this is the the new MDP series is the replacement for the DP series, uh which we've seen in many uh previous videos. In fact, Micsig

**Dave Jones:** actually developed this DP10007 uh variant of their uh DP line of high voltage probes uh at my request cuz I was looking at selling this. So, they actually designed this to actually meet um you know, try and meet the the same

**Dave Jones:** specs as my uh HVP 70 probe, which I still sell on ee veeblog.store down below, an excellent probe made by Sapphire, by the way. So, they did this version with the times 10 and times 100 uh ranges to match uh this cuz their

**Dave Jones:** normal one, including this new one, is a times 20 times 200. So, the new MDP series doesn't have this times 10 times 100, but they developed this for me. And then I tested it, and I'll link in the

**Dave Jones:** videos, if you haven't seen it, where it wasn't that great. It didn't meet its spec on the common mode rejection ratio, the CMRR. And I've done an excellent video, by the way, even if I do toot my own horn, on what is uh common mode

**Dave Jones:** rejection ratio and how to measure it. So, I'll link in that video down below, if you haven't seen it. And I've done a full uh teardown and reverse engineering video of uh this uh design as well. So, anyway, I didn't end

**Dave Jones:** up uh selling this, but Micsig did actually um sell it. So, quite a few people uh bought it, but they actually also confirmed my uh test that n- didn't quite meet the common mode rejection ratio. So, Micsig uh have developed this

**Dave Jones:** new MDP series, which actually replaces it. Look at that. Get the accessories, they're the same as the ones that came with the uh DP series, and it does look very different. So, we're going to take a uh look at this, and we're going to

**Dave Jones:** measure its uh common mode rejection ratio, and compare it with the other probes. But, if you want a more in-depth video, go and watch the previous ones on the DP10007 for the common mode rejection. So, anyway, comes in a sexy

**Dave Jones:** carry case here and it does look like a high quality bit of kit. And of course, you get the crocodile clips with it and you also get the big long easy hooks like this as well, the big grabbers. But

**Dave Jones:** yeah, this actually looks and feels a lot better than the existing design, you know, the plastic housing like this. It's much smaller, but it's a dual head approach. So, it's got the the high voltage differential part down here and

**Dave Jones:** then differential amplifier and then a driver in here, which drives to a receiver down here and then that drives your scope direct. And it's got the fancy pantsy stuff like 5 MHz bandwidth limit. So, this has a little micro in it

**Dave Jones:** and ADC and DAC and whatnot and you can actually zero out the offset on this. Very handy. So, nice little diecast alloy case as is the head as well. So, it's a better design than the previous one. And it's got the shorter cables

**Dave Jones:** like this cuz I know that a lot of people don't like the integrated probes like this. They prefer the shorter ones. I know a lot of people would have preferred to see just the banana jack straight in here and then they could

**Dave Jones:** make their own probes and little shorter ones so you can get higher bandwidth, less inductance, and less interference and stuff. But yeah, at least they've done these short as opposed to the much longer one on the previous one. So,

**Dave Jones:** yeah, this is a more betterer design. And this new design is actually a spin-off from their cutting edge Sigofet optical fiber probe technology. Hence, it looks very similar to the optical fiber probe. Look, there's the two heads. It's much shorter, but obviously,

**Dave Jones:** you know, they've got a similar sort of microcontroller in there with the offset stuff and things like that. So, yeah, it's spin-off technology from that. I don't want to toot my my horn, but I have done an excellent video on uh

**Dave Jones:** showing you demonstrating uh the practicality and use of uh these high voltage optical fiber probes. I'll link that one in as well. It's an awesome video. As you can see, they do offer this in the one we've got 20 times and

**Dave Jones:** 200 times switchable, 50 and 500, and 100 and 1,000. Sadly, they don't offer my preferred one, which is the uh 10 times. And interestingly, uh the output voltage is only uh plus minus 3 volts now as opposed to uh 7 volts that uh we

**Dave Jones:** got on the uh previous models. So, we'll see what that's like in terms of uh noise floor. But anyway, uh they do uh boast they boasted to me uh in an email that uh yeah, I will be happy with the

**Dave Jones:** common mode rejection ratio of this thing. All right, for testing this, we're going to get out the big gun, the Rohde & Schwarz MXO 4 scope uh like we used in the uh previous common mode rejection ratio uh video. And it's got a

**Dave Jones:** USB-C input. Nice, they do provide a very long lead here for connecting to your scope, but you could connect it to any other power source as well. Would have been nice to have a little shorty, I guess, but uh your mileage may vary.

**Dave Jones:** Now, if we compare the MDP series to the old uh DP series, the DP series, of course, had uh my one, the times 10 times 100 version, but then they jumped up to uh times 50 times uh 500. Whereas

**Dave Jones:** this is available in that times 20 times 200. Now, uh noise figures here, the 10007 had 15 less than 15 mV uh RMS there and 40 mV for the uh times 50. And if we go over here, they actually

**Dave Jones:** specify it for the 5 MHz bandwidth and the full bandwidth, they're both 100 MHz uh full bandwidth. And it's a little bit uh worse over here, 45 mV and a bit worse over here on the uh times 20 at 22

**Dave Jones:** mV as opposed to the 15 over here. So, we'll measure that, but uh yeah, it's it's not as good. Now, the common mode rejection ratio here, they are specified at uh different frequencies. At DC, of course, uh greater than uh minus 80 uh

**Dave Jones:** dB and that's exactly uh the same here. 100 kHz looks to be the same at 60 here. Well, they've got minus 60 here. They put 60 here, but I explained in my previous video why they have minus 60

**Dave Jones:** and some have 60 cuz they're just lazy and leave it off. But the old one only specified 1 MHz here and for the 10007, it's greater than 40 minus 45 dB here. Whereas the new series, they don't give

**Dave Jones:** you the 1 MHz figure. They jump up to 10 MHz and give you minus 30, which is worse, of course, than minus 45. It's 15 dB worse and a lot and that could be fine if they actually gave you the 1 MHz

**Dave Jones:** figure, but they don't. So, yeah, we're just going to have to measure this thing. And as I said, the output voltage 7 V for the previous one and the new ones are plus minus three, but technically that's neither here nor

**Dave Jones:** there as long as your scope is capable of actually measuring down that low and going into the noise floor as well. So, yeah. Check it out. But the difference in the attenuation here times 10 to times 20 hasn't impacted the maximum

**Dave Jones:** differential voltage, which is DC plus peak AC. Still 700 V on the either the times 200 or the times 100 range with the old model. So, it's still more than capable, of course, of doing like your general purpose mains power supply

**Dave Jones:** stuff. No worries whatsoever. So, what we're going to do is zero this. So, we need to short the input out. You can't do that unless you've got a banana to banana. So, you can put it on the current range of your meter, no worries.

**Dave Jones:** So, we shorted out our input here and then we press our zero button here and boop, you hear one beep, it's fine. If you hear three beeps, then it's failed for some reason. And by the way, this thing does have they do recommend a

**Dave Jones:** 10-minute warm-up period for this. So, just be aware of that. You can't just necessarily slap it on and uh your measurement if you're doing anything accurate. So, I've left it for about 5 minutes and you can see it's probably a

**Dave Jones:** little bit below the center line there. So, I'm going to actually zero that again. And it did its beep and see, it's actually gone up and now it's you know, the center of that noise is now in the

**Dave Jones:** center. I know it wasn't much, but it'll depend on the ambient temperature, how long you've had it powered up, blah blah blah. But just be aware of course that you have to set your scope up to uh times 20 probe. So, if your scope

**Dave Jones:** doesn't have to have that, then you'll have to do the uh multiplication manually, I'm afraid. And we use the standard uh 1 megaohm input termination. You don't need 50 ohm termination for this. You don't want that. So, just

**Dave Jones:** yeah, standard scope input. As a baseline, I think I've been I left that for half an hour. I had to do something else. I am probably tell by the time up there in the edit. Um and it's shifted

**Dave Jones:** uh what, 20 mil half a division, 20 millivolts maybe on average. So, just a bit of a baseline. But yeah, these things do drift cuz they have active uh amplifiers in there. Um so, yeah, just be aware of that. That's why it has a

**Dave Jones:** zero function. All right, please excuse the crudity of the model. Didn't have time to build it to scale or to paint it. I'm using the same uh GaN uh MOSFET uh driver that I used in my uh Siglent

**Dave Jones:** uh video. So, if you want an very extensive uh technical video about how uh GaN uh fast GaN uh transistors work and high voltage uh probing and all that sort of stuff, then check out that uh video. But I've got all three uh probes

**Dave Jones:** hooked up. I've got the new MDP700 on channel two, DP10007 on channel three, and the HVP70, which is only 70 MHz uh bandwidth, on uh channel four here. Now, because the MDP uh 700 is actually uh shorter leads

**Dave Jones:** here, they do actually include um some extender leads here. So, I've put those in so it's not twisted as much here, but it's basically the same length as the other two probes here. So, I'm probing the switching output of this MOSFET here

**Dave Jones:** and you can see that the green trace here, which is the new MDP one, it is substantially larger than the other two. The ringing on there is substantially larger. That's the effective inductance of the leads. So, yeah, let me try and untangle it and

**Dave Jones:** see if we can get better. So, I've got the really short probes on there. You can see the difference that that makes. So, well, let me switch over to the green here and you can see that yeah, the ringing is shorter on that. But

**Dave Jones:** anyway, this isn't an extensive test. This is just a sanity test to show you that all three probes basically performing the same at 1 MHz switching frequency here and all the ringing is all has to do with the probing and but I've gone

**Dave Jones:** through that in the previous video. So, I don't know. Just wanted to have a play around with that. Simple sanity check just to make sure they're on par, but yep, they basically are. So, so you can see in there all three channels like

**Dave Jones:** that are all performing identically. They all do the same high frequency stuff. So, there you go. We can switch through those and yeah, pretty groovy. No worries. And all three of them have a 70 V differential voltage. I've

**Dave Jones:** currently got it to 65 V. That's on the lowest range anyway. So, I'm going to turn that up and turn the and the mix sig there started to flashy flash showing you that it's over range. The other ones don't

**Dave Jones:** actually have that. So, but let's keep turning it up and see which one craps out first. Come on. We're 79 V, 80 V. And yeah, it's definitely the DP10007, which is the orange one there. That's just yep. It's it's it's died. It's died. So, the

**Dave Jones:** others actually still have an ability to keep going above that. And you can see that it's clipped there at 91 volts. And the others start to yeah, do silly buggers as well. So, slightly better The others are slightly better than the old

**Dave Jones:** DP10007, but that's neither here nor there. That's just for funzies. All right. So, we've got the remote oscilloscope interface here. I've got the input to the MDP700 shorted on full 100 MHz bandwidth on channel two here. You can see that little sigma signal

**Dave Jones:** there. That is AC RMS basically. I've done a full video on that. Again, very interesting and informative video. What haven't I done? Um and we're talking mean of 13 mV RMS noise here. And that's on the times 20 range. And the spec is

**Dave Jones:** 20 to less than 22 mV. So, yeah, easily meets that. No worries. But you've got to remember this new probe is available in 100 MHz, which is what we've got here, which is and the MDP701, which is 150 MHz and the 702,

**Dave Jones:** which is 200 MHz. So, may but they don't break down the specification for that. So, maybe their noise figure is like on the highest 200 MHz one. I don't know why you wouldn't break it down per model, but anyway, there it is. And I've

**Dave Jones:** switched on 5 MHz bandwidth here. And you can see it's dropped, but I'll just clear the statistics there. And the sigma that we're looking at because you don't want RMS cuz RMS includes any DC offset. That's why you want AC RMS,

**Dave Jones:** which is the standard deviation, which is that sigma function there. And we're talking 5.4, and the spec is 8 mV. So, yep, meets it. And now on the times 200 range. Remember you've got to change your attenuation down here. So, I have actually changed

**Dave Jones:** that so we can go in there and have a look to verify that I've actually done that. Go into probe and you can see I've got 200 on there. So, our figures are correct and so let's clear that and we

**Dave Jones:** get 40.5 millivolts. The spec is 80. No worries and I've changed it to 5 megahertz bandwidth and let's redo that. Should only be a smidgen smaller. We're talking 31 now millivolts but once again, the spec is 70. So, yeah, it's ballsing it in.

**Dave Jones:** Now, we've got the old model DP1000Z uh seven in times 10 mode spec of 15 millivolts RMS noise. So, I'll just clear that, reset the statistics and we're talking uh 12.7 there. Yep, meets it. So, they're basically on par with the new model. So, yeah,

**Dave Jones:** it's neither here nor there. And we don't have a 5 megahertz bandwidth limit on the old model. So, yeah, I'm just not going to bother you know, cobbling together some external bandwidth with limit thing. Doesn't matter. And times 100 mode,

**Dave Jones:** reset that. We're looking at 23.6 millivolts. So, the previous model was almost half the noise on the higher attenuation setting than this new model. So, that's not terrific. And the EVBlog HVP70 on times 10 mode, let's give that

**Dave Jones:** a reset and we're talking 10.4 millivolts. So, that's the clear winner. And on times 100 mode, let's reset it. 37 millivolts. So, that is less than the new MDP70 but higher than the DP1000Z and again, we don't have a 5 megahertz

**Dave Jones:** bandwidth hardware limit on that so we're not going to test it. All All please excuse the crudity of the model. Didn't have time to build it to scale or to paint it. Uh I've shown the uh setup and gone through all sorts of stuff in

**Dave Jones:** the previous CMRR video. I'll just quickly uh briefly cover it here. Uh we've got a signal generator output here, which you can go up to 100 MHz, um and then we got that going into a 50-ohm uh terminator here, so we don't get any

**Dave Jones:** transmission line uh issues. And then whoop, I've got a uh just a banana breakout here, so that we can connect both of the inputs, short them out. Yes, we're actually shorting the inputs out to the positive uh output of the signal

**Dave Jones:** generator here, so that we're effectively putting a common mode signal on both of these wires here, shorted together, but so it's common mode signal relative to ground over here. And that's the whole point. Now, I'm not sure with

**Dave Jones:** the uh times 200 range of this new NDP700, I'm not sure how we're going to go with signal level, cuz I can only get uh 5 V uh maximum on our sig gen. We'll give it a go, but I'm not hopeful. It was already

**Dave Jones:** borderline with the uh times um 100 on here. So, then you just have the output of the uh sig gen in this case we'll do the uh DP1007 uh first uh just to get a baseline, uh and then the output of that is just

**Dave Jones:** going into uh channel 4, and then we're going to use the uh frequency response analyzer. Although, you don't need a frequency response analyzer to do this test. You can just do a spot frequency with an external uh so, you don't even

**Dave Jones:** need an internal sig gen. You don't need a response analyzer, just do it uh spot frequency wise, and I might show you that as well. So, how we set this up with the frequency response analyzer or the spot frequency is that uh we're down

**Dave Jones:** in the very low signal level here. So, I've got it on the times 200 uh range, which will give us the highest uh well, the highest common mode rejection ratio, the highest signal level. Now, I've got to have it in HD mode. So, I've got HD

**Dave Jones:** mode turned on, and you can see that gives us an effective resolution of 16 bits. That's very important. Now, um I discovered one thing on here is that I did have I do have average mode turned on. And watch this. If I

**Dave Jones:** put 20 averages on, okay? And I've set 20 averages, so we should actually get 18 bits of resolution on this thing, and I've got the signal level set to a maximum 5 volts uh peak to peak into a

**Dave Jones:** nominal uh 50 ohm load. I've got the start frequency 10 kHz, stop frequency 50 MHz. Uh the uh input is uh channel one, so that's from the function gen, and the output is uh channel four here. That's the output of the uh probe. So, I

**Dave Jones:** should be able to run that, okay? But watch up here. I expect right average of one I expect an average of 20. But we don't get it. It switches to an average of one. Now, I'm not sure why that's the

**Dave Jones:** case. Um I'll have to talk to Rohde & Schwarz about that, cuz I want my 20 averages, damn it. I don't care how long the frequency response is. If it takes 20 fast like 20 samples on each one. Anyway, here we go.

**Dave Jones:** We're getting our response from uh the red is the phase, so we should expect to see a phase uh change up here somewhere. And uh then our we're going up to 50 MHz on this one. And up and and there's our phase change.

**Dave Jones:** And which is fine, there's nothing wrong with that. Um and okay. So, at 10 MHz here, you can see that it's uh at 19 19 and 1/2 dB, which is terrible, Muriel. And by the way, we've got to get

**Dave Jones:** this screw right. The probe is set up for the uh times 100 ratio there. Um and but at 1 MHz, which is But we don't have a spec for the DP1007. Remember, this is the older uh design. Uh we're talking

**Dave Jones:** about uh minus 40.45 dB, and the spec is minus 45 dB. And this is why I went back to when I first tested this, I went back to um Mixig and I said, "Hey, this doesn't meet the spec." And they said, "Oh, okay, we'll

**Dave Jones:** test it." And they confirmed it didn't and they said they'd work on it. 6 months later, "Oh, sorry, we're still working on it." 12 months later, "Oh, we're still working on it." And what, a year or two 2 years later?

**Dave Jones:** Bingo, we've got the new design uh came out. So, that's the old DP10007 and it doesn't even specify at 10 MHz. So, yeah, the old one wasn't a great probe. Let me show you the uh HVP70. Okay, so I

**Dave Jones:** just connected up the HVP70 probe. It's only got 70 MHz uh bandwidth, but we're only going to 50 meg anyway. And everything's the same. It's the same gain. It's on times 100, so I don't have to uh make any other changes and I can

**Dave Jones:** just run this again and we should see it becomes signifi- it should be significantly better. So, at 100 kHz there, we're at like minus 63 dB or something, 64 dB. So, come on. You can do it. And we're going to phase change there.

**Dave Jones:** Like I said, phase change is not a problem. And we've got another phasey. But, the problem here is is that we're down in the noise. Okay, you can see the waveforms at the top. They're not that terrific. But anyway, at 10 MHz, it's

**Dave Jones:** better, right? At 10 MHz, it is minus 43. So, way better and its spec is minus 40, I think. Okay, so I've got the MDP700 in and we'll just change that to uh 200. Apart from that, we can just rerun that

**Dave Jones:** and see what we get. Woah, bit of a jump there, but you can see Look at the signal levels at the top. Okay? We're down in the noise. This is where the averaging would have helped, but it won't let me do the aver-

**Dave Jones:** Oh, no, th- this one's got 18-bit HD now. It's switched to 18 Oh, Not It was 18-bit down there. So, I'm not sure what was going on there. That's interesting. Uh Anyway, um yeah, it's a bit higgledy-piggledy, isn't it? And we

**Dave Jones:** don't get a smooth response, but we're down in the noise. Look at the signal level it's trying to measure it down there. It's 100 mV, but that's gained up by 200. Okay? So, it's it's right down in the noise. Anyway, we do have a spec

**Dave Jones:** over -30 dB at 10 MHz, and we're getting -46. So, it is substantially better than uh than the spec. That's pretty good. There's So, let's actually do this. Let's go back and just do this as a spot frequency thing. I said I'd show

**Dave Jones:** you that. So, generator, 5 V peak-to-peak in our on our signal generator, and uh let's say at uh let's do the 10 MHz thing again, okay? Turn our sig gen on. There we go. That's channel one. Turn on channel four. And

**Dave Jones:** channel four, we're going to have to turn it right down. Okay? You can see that we are down in the noise, right? We're at 500 µV per division, but but we're only 12-bit, okay? So, we need Unfortunately, it's reset all of our

**Dave Jones:** stuff. So, we have to go back in. We have to switch HD mode on, right? Because it's just Now we're sig getting 16-bits, but look at that, right? There's almost You can kind of sort of see there. It's out of phase, right?

**Dave Jones:** It's dipping here, and it's going up there. You can almost see it. Okay? So, we can't have to turn some averages on here. We're in sample mode. So, we'll turn on some averages, right? And that we've only got the one average. So,

**Dave Jones:** let's just go 20 averages, right? And we can kind of sort of get our um signal level there. So, you can see it's that frequency response graph is going to be very how you doing cuz we're down in the

**Dave Jones:** noise, okay? So, that is 10 MHz, but it's also reset our probes. So, we've got to go in our user-defined probe and set our bandwidth of our probe. Let's take that down to the 100 where it's supposed to be, okay? Maybe we'll get

**Dave Jones:** some No, no improvement there. And manual attenu- manual And of course you can set the attenuation, but it makes no difference, right? But we can actually set that to the times 200 there, but it just changes the scale. It doesn't

**Dave Jones:** physically change uh the res- the signal level into the uh scope. So, yeah. There you go. Um yeah, try and get a signal out of that. So, let's turn our on our sigma or standard deviation measurement AC for uh

**Dave Jones:** to get rid of any uh DC offset, so we'll add that for uh channel one, and then we'll also add that for channel uh four as well, okay? So, there you go. We can get both of those, and we can turn our

**Dave Jones:** statistics on, okay? And boom, we now have, right, figures that we can actually work with. So, a mean here of 9.2 mV, okay, divided by 1.78 V, okay? And then we get our log of that, and then we multiply that times 20, and

**Dave Jones:** that gives us minus 45 dB, okay? And our 10 MHz spec is minus 30 dB. So, it's it's balls in that in. Absolutely balls in that in. No problems. And I can now switch it to the uh times 20 mode, and

**Dave Jones:** I'll show you that it'll just drop right off. Here we go. And times 20. There you go. Um it's no better. The DC offsets uh changed, and I can zero offset that, of course.

**Dave Jones:** There you go. That was uh zero offsets, and right, there's just nothing there. You're just measuring unicorn farts here, pretty much. But if we go up to 100 MHz, we find that we do actually get something, okay? So, now we've actually

**Dave Jones:** got some signal to work with here. And it's interesting, you can see the wavering of the average there, and that's because the DC offset is drifting. We're right We're so far down in the noise that that DC That the just

**Dave Jones:** in the just the gentle drift in the DC offset in this thing is why it has a zero offset button. Um is is causing that, and it's moving slowly cuz we've got 100 averages turned on now. If we

**Dave Jones:** turn the averages off, you know, you'd see it go burko. We turn average back to sample there. That's what we're dealing with. That's what we're dealing with. Now, YOU'LL NOTICE THAT AT 100 MHZ, our signal level's actually dropped here.

**Dave Jones:** It's not a problem from a measurement point of view cuz what we're actually measuring at that particular point of the like the channel one input is is fine. So, our measurements are correct, but our signal level has dropped cuz we

**Dave Jones:** do actually have some system capacitance there. So, let me actually disconnect the cables, and you'll see the amplitude actually go up a bit. There you have it. I physically disconnected them. So, that's interesting, huh? But, as I said,

**Dave Jones:** it doesn't make a difference if the amplitude actually drops as long as you're measuring it correctly at the channel one input, which we are. All right, so let's reset our stats here. And what have we got? And we've got a

**Dave Jones:** mean of 26.2 mV and divided by 804 0.5 mV. We get log of that, and we multiply that by 20, and we're getting minus 29.7. Pretty close to 30. And what is our spec at 100 MHz? Minus 26

**Dave Jones:** dB. So, yeah, um it's It meets the spec. So, yeah, it's a It's a reasonably decent probe for CMRR. So, there you have it. That's the MDPR700 there. Um street price of about 260 euros from Batronix there 220 US. I mean

**Dave Jones:** they've got like a ticket price of 499 there. That's pretty pricey. But 220 bucks street price is excellent. Oh yeah, look you can buy the MDP702. There you go. Oh it's jumped up to 400 euros for the 200 megahertz one. Yeah, as I

**Dave Jones:** said I would not spring for the extra money for the bandwidth here because it's all about the probing and when you've got just the banana plug interfaces like this, you know, you're going to struggle to get your performance with your probing at those

**Dave Jones:** sort of frequencies. So 100 megahertz is already more than enough. That's why my HVP70 is only 70 megahertz because it comes with the banana plug leads. You can't get a higher frequency interface for your higher frequency interconnect. So

**Dave Jones:** yeah, I don't know why they bother manufacturing that actually. Yeah, I'd just get the 100 megahertz version or even like a 50 megahertz even that like the old school 20 megahertz high voltage differential probes is still incredibly useful. So yeah, I think just stick with

**Dave Jones:** the 100 megahertz jobby and you'll be fine. But it does seem to me it's performance specs. So I'm reasonably pleased with that now. But yeah, they couldn't fix the DP series. They they they tried for like a year and they

**Dave Jones:** couldn't fix it. Anyway, thoughts and comments down below and I ran out of time for the teardown. So if you want to see a teardown of this thing, maybe even another reverse engineering video, please leave it in the comments down below. But you've got

**Dave Jones:** to interact on the video so I know that you like them. You've got to watch them. You've got to thumbs them up and you've got to subscribe and all that sort of stuff so I know I can get the metric that you enjoy this

**Dave Jones:** sort of stuff. So anyway, hope you enjoyed it. Catch you next time.
