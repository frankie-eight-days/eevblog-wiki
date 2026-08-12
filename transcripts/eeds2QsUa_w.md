---
video_id: eeds2QsUa_w
title: EEVblog #978 - Keysight 1000X Oscilloscope Hacked!
url: https://www.youtube.com/watch?v=eeds2QsUa_w
source: youtube-asr
timestamps: {"0": 0, "1": 10, "2": 32, "3": 55, "4": 70, "5": 90, "6": 118, "7": 127, "8": 147, "9": 168, "10": 180, "11": 191, "12": 203, "13": 210, "14": 218, "15": 233, "16": 250, "17": 274, "18": 288, "19": 301, "20": 319, "21": 335, "22": 347, "23": 359, "24": 371, "25": 384, "26": 396, "27": 407, "28": 427, "29": 437, "30": 450, "31": 476, "32": 494, "33": 502, "34": 516, "35": 529, "36": 539, "37": 551, "38": 569, "39": 585, "40": 601, "41": 615, "42": 628, "43": 649, "44": 669, "45": 683, "46": 698, "47": 714, "48": 729, "49": 739, "50": 765, "51": 780, "52": 808, "53": 840, "54": 861, "55": 879, "56": 899, "57": 910, "58": 925, "59": 937, "60": 955, "61": 968, "62": 981, "63": 1006, "64": 1019, "65": 1034, "66": 1046, "67": 1061, "68": 1076, "69": 1091, "70": 1105, "71": 1114, "72": 1132, "73": 1146, "74": 1163, "75": 1188, "76": 1206, "77": 1217, "78": 1236, "79": 1251, "80": 1273, "81": 1282, "82": 1298, "83": 1313, "84": 1329, "85": 1338, "86": 1357, "87": 1378}
---

**Dave Jones:** Hi. In a previous video we took a look at our first steps at trying to hack the Keysight 1000 X-Series oscilloscope and figure out how it did its product configurations and stuff like that.

**Dave Jones:** And I'll link that in down below if you haven't seen it. And we got into adding a modification here so that we found some product selection, well, not product selection, we found some module selection resistors on the bottom here and we removed those, replaced them with a pot um and so that we could uh play around with the different uh modes on that.

**Dave Jones:** We also added a uh UART interface which connects into the Windows CE uh U-Boot uh system which is how we were able to to find the information. So we got as far as finding the configuration resistors and the two ADC pins on the Speer uh 600 processor that were actually measuring the module the BLT module configuration.

**Dave Jones:** The BLT module is this one. You can see it there. This is the uh processor module is the MegaZoom 4 ASIC, the ADC, the FPGA, and the Speer 600 processor which is running the Windows CE operating system for the thing.

**Dave Jones:** We found them and we tweaked the pots and everything and we found that we could actually uh you know, modify these ID codes ID2 ID0 here and uh change the BLT module configuration which is this one here which sets the sample rate but not the sample rate of the scope.

**Dave Jones:** Um it in one point showed zero gig samples per second but it was still sampling. So that was interesting um and it may become important in the future. But what we need to do is find this this BLT product configuration here which sets more important stuff like the bandwidth um and also that would actually set the sample rate cuz the low-end EDU oscilloscopes are only one gig samples per second as opposed to

**Dave Jones:** 2-gig samples per second. So, the $450 scope they've artificially limited the sample rate in there as well as the bandwidth is set to 50 MHz. We still don't know why it's set to 200 MHz.

**Dave Jones:** We measured the performance in the previous video. It's about 131 MHz minus 3 dB point for the front end anyway. So, I changed these resistors on here and and I changed a couple of the other resistors on here and I could not find that BLT product configuration.

**Dave Jones:** Now, it makes sense that it's actually could be somewhere else. So, let's take a look at Tada! If it's not on that board, the processor board, and there's no reason to think that it necessarily is, then it could be on the main board here.

**Dave Jones:** So, this is our main board. This is where the module plugs into here. The main board on the scope, thankfully, it's accessible. So, what we're looking for is another voltage divider resistor that would go through the connector.

**Dave Jones:** Now, if we actually have a look on here, because the other selection resistors are here, it would make sense for it to be on this header connector perhaps cuz that's closer.

**Dave Jones:** So, that one actually matches up with this one down here. But, this is all the function generator stuff around here and the demo signal and everything else. So, I don't think it's that.

**Dave Jones:** So, this one up the top here, which means that the signals Well, I don't know which ADC pins they're using. I don't know if they're all up in this one quadrant.

**Dave Jones:** I haven't checked the data sheet, but the signals would have to get from here over to here, which is no problem. You know, it's just a it's just a voltage divider.

**Dave Jones:** So, it's just a routing problem. But, anyway, so what we're looking for around here is that same voltage divider, i.e. two, and we need two i.e. two resistors from ground to power tapping off.

**Dave Jones:** Plus, we need two of them because we've got the two extra signals on the BLT, if you remember that. There we go. BLT product configuration. So, I've got two different ADC pins with two different voltages, 1.25 V and 0.7 V or thereabouts.

**Dave Jones:** So, we need to measure those. And it would make sense to put them on this main board anyway, I guess. We know that the low-end non-function generator module does not include the B and C on the front panel for the function generator parts, and most likely they don't populate any of this stuff as well to save cost on the non-function generator model.

**Dave Jones:** So, that makes sense that they would spin different versions of this board. Okay, they assemble different versions of this board based on what model they're actually selling, the generator or the non-generator version.

**Dave Jones:** They have four different models, but I don't think there's any difference apart from license keys from the other ones, and these product selection resistors. Anyway, so it makes sense that they're redoing this board anyway, so they can change the resistors.

**Dave Jones:** Can you see any suitable resistors around there? You bet you we can. Look at these puppies. Aha, just the right number of resistors we need, four of them. Going directly into pins of this module, which would go into the ADCs.

**Dave Jones:** So, you can see the traces there. They're not going anywhere else. There's one going here, and there's one going under there, which goes to there. And these are looks like these are joined together, going to a via there, which is most likely power.

**Dave Jones:** And these two are going down to most likely ground. So, they are two voltage dividers. You've got to put money on that. Unfortunately, they're underneath the module. What a pain in the butt.

**Dave Jones:** So, we're going to have to put some wires on there, get them out, um and then we'll be able to measure those pins. And what we're looking for, of course, is there those voltages we've got there.

**Dave Jones:** 1.25 V cuz this is measured from the ADC. We've confirmed that. 0.7 V. There's nothing else connected to it directly to the pins, which is exactly what you want in the exact configuration we want.

**Dave Jones:** It's got to be it. It's got to be. Feeling lucky. And it's probably no coincidence that we're looking for 1.25 V here. And what do we see on these resistors?

**Dave Jones:** Look, these two here are identical value, and these two are different. Okay? So, these two with identical values, that means we're that we're going to get a half rail point there.

**Dave Jones:** And we saw in the previous video that the rail was 2.5 V, I believe it was. So, bingo. We're going to measure 1.25 V on there and 0.69 V, give or take, on there.

**Dave Jones:** Let's go. And we'll just add some fresh solder under these pads so that we can get the mod wires on. And just like last time, it's worth going to an extra little bit of effort just to secure the pots elsewhere.

**Dave Jones:** I've glued the two pots together with super glue and then super glued them down to the board. Just a tiny little dab to keep it in place so that you take any stress off the wires.

**Dave Jones:** And I've just got those going over. Too easy. And a pro tip, make sure you have screwdriver access through. So, I actually angled it so that I could actually get those uh screwdriver through like that once it's open.

**Dave Jones:** All right, let's power it up. And 1.20 V, and near enough. And 0.7. Come on, 0.7. 0.67. We got them. And now it's all about finding out which way around I've got the pots, which one applies to which configuration bit, and which direction turns them in what voltage.

**Dave Jones:** So, you're going to come up with a little cheat sheet like this and get your tongue at the right angle and get in there and tweak them. So, once you got that information, which pots do what, then I can adjust them and find the window that the product IDs come up at.

**Dave Jones:** That's a you know, quite a laborious trial and error type thing cuz you got to reboot the thing every time cuz it's not going to live update those values.

**Dave Jones:** So, you're going to tweak it once, reboot, and all that sort of jazz, but cycle each of the four configuration things through all of there I believe there's four configuration options for each one.

**Dave Jones:** So, yeah. At least I have the pots now to do it. Eh, eh, and eh, eh. Beauty. All right, here we go. I've got hooked up to the terminal program here and we're going to boot it.

**Dave Jones:** The pots are at mid-level, so whatever, like both at uh 1.25 volts or near enough and depends how it comes set from the factory. Power it up. Come on.

**Dave Jones:** What do I got? What do I got? Ooh, it's working. It's working. Ta-da! We're in like Flynn. Let me change the horizontal. There we going up to 2 gig.

**Dave Jones:** Oh, timeout while trying to stop Talon clocks. Hardware error. Hardware error. OH, NO! IT doesn't like that at all. So, what do we got? Um product configuration 200 MHz, 4 gig sample a second, uh unknown config 43.

**Dave Jones:** Yeah, we have to change that back. Uh ID3 and ID There we go, 1-V and 1.37 V ID3 ID4. So, it really is not a happy camper. But, that's good.

**Dave Jones:** We're on our way. All right. So, I figured out what all my pots do and I have changed the BLT module back to its original factory configuration that we had.

**Dave Jones:** And I have modified the product configuration just randomly. I put one down to 0-V so it's now ID0 and it's ID2. It was showing BLT product config 24 before.

**Dave Jones:** Now, it's showing product config 02. But, nothing here seems to have changed. The bandwidth is still the same. The board revision FPR, yes, it was FPR before. And now it's saying LP1.

**Dave Jones:** So, whatever that means. The bulb width is still the same. 4 gig samples a second is still the same. The LAN fire is still the same. And if we go into the service manual here, we can still see that it's a DSOX1102G.

**Dave Jones:** The same 100 MHz bandwidth. Nothing looks to be different. So, WE'VE GOT ONE. WINNER WINNER chicken dinner. Look at this. Product config 00. I set both of the pots on the product config to zero and bandwidth has changed.

**Dave Jones:** 70 MHz bandwidth and Keysight sell the 70 MHz bandwidth model. So, I've got to do the measurement to actually confirm to find the minus 3 dB point on that.

**Dave Jones:** But, hey. Hey, notice the screen as well. 1 gig sample per second. Let me change that time base. Yep. There you go. We've got it. I've changed the time base there.

**Dave Jones:** And that limits the sample rate as well. So, bingo. We've got it. It looks like you can change the bandwidth and the sample rate at least with just the configuration resistors.

**Dave Jones:** I hope that's the case. Now, this is interesting. The data on the oscilloscope, it still says it's an 1102G, but the bandwidth has changed to 50 MHz. So, that's different to what we've got over here, which is the bandwidth 70 MHz.

**Dave Jones:** So, what's going on? I'm going to feed in a signal and let's find out what the actual analog bandwidth of this thing is. See if it's changed. Well, this is strange.

**Dave Jones:** I'm feeding in a 50 MHz signal here and I've confirmed that it's 1 V peak-to-peak on my 500 meg bandwidth scope and it's 1 V peak-to-peak here. So, so much for the 70 MHz bandwidth here and so much for the 50 MHz bandwidth as it says it is in the configuration service menu on the scope.

**Dave Jones:** What? I kid you not. This is a 200 MHz signal on the input confirmed as 1 V peak-to-peak on my 500 meg scope and 50 ohm terminated and it's still not 3 dB down.

**Dave Jones:** It's 0.86 V. It's not 0.707. What? This thing has greater than 200 MHz bandwidth on the analog front end. That explains why it's 200 why it was showing 200 MHz before if you remember that in our original configuration and maybe why they're supplying 200 meg probes with it so that later they can upgrade the bandwidth or provide a 200-meg model.

**Dave Jones:** Wow. In fact, I confirm that the minus 3-dB bandwidth of this front end uh is 224 MHz in this mode. Wow. Now, unfortunately, when I try to combine different modes, like for example, going ID 1 and ID 2 here or ID 2 and ID 1 to give us a BLT product config of 12, then uh yeah, we get all the stop telling clock error messages, and we get basically no waveform.

**Dave Jones:** You can see that uh the channel is on there, but uh yeah, nobody's home. So, there are various modes like that. Um so, it's just a matter of finding a product configuration that actually actually gives you the results that you know, the combination of bandwidth and sample rate that you actually want.

**Dave Jones:** I think we have a problem here. I've set the product configuration to uh 10, and that gives us the 2.5 gig sample per second, which is fantastic. That gives us the full 5-gig sample rate, but Uh what what what's going on here?

**Dave Jones:** Something is seriously wrong at very slow time bases. So, it's obviously not uh designed to do that. So, your 2.5 gig samples uh comes at a price there. What the you know, yeah, okay, let's not use that one.

**Dave Jones:** Now, I've actually done a table here of uh the various uh configuration options with config 1 all at zero first, both zero volts and the and zero ID. The volt The ID corresponds to the volts.

**Dave Jones:** And then, I incremented the ID um of the product config zero uh bit there, and these are the voltages I just happened to turn the pot to. I wasn't determining the window uh values or anything like that.

**Dave Jones:** I haven't determined those. But, you know, they're going to be like an equal equidistant kind of thing between there for the eight Well, for the Yeah, for the nine configurations possible there.

**Dave Jones:** And that directly corresponds to the code over here. And I've determined that when you put this on, it goes up in increments of 10. So, if you combine this bit of one and this bit of one here, your code, your product config code, according to that boot dump, will be one one.

**Dave Jones:** So, like that config one is first, and then the config zero is the second digit there. And then this is the bandwidth from the dump that was that the boot dump says that it's set to.

**Dave Jones:** This is the revision, whatever that means. I don't know, but it seems to be separated once you go up to five, but that seems to be five to eight there is LP2, and this is LP1.

**Dave Jones:** And you'll notice anything with no wave here means you get no waveform on the screen. You get all those boot clock errors and things like that. But, all of the ones in LP mode, LP1, were 220 meg, and the ones here in LP2 were a combination of the 50 meg bandwidth which they sell and the 140 and 140 odd meg bandwidth, which is 100 megahertz limited.

**Dave Jones:** So, that seems to be a combination of an actual 50 megahertz front end limited bandwidth and the 100 meg bandwidth as well, not the full 20. So, it seems to have three different modes there.

**Dave Jones:** I don't know where the 70 meg one comes in. We have We have not seen I mean, we've seen it up here in the dump mode, but it doesn't correspond to an actual measured bandwidth yet that I've found, anyway.

**Dave Jones:** And of Of the sample rate does change on this lower on any of the 50 meg bandwidth limit modes, it changes to 1 gig samples per second exactly as the product data sheet tells you it does so.

**Dave Jones:** Obviously, you're going to hack it, you're going to want the 204 220 meg analog bandwidth with the two gig sample rate there. And as I mentioned, don't touch the 2.5 gig sample rate cuz that seems to have some sort of memory sample issue.

**Dave Jones:** Don't recommend that at all. So, I'm going to call it quits for this video now, but there you have it. Absolutely fascinating. I didn't think we'd be able to hack the bandwidth of this thing just by setting those product code resistors on there.

**Dave Jones:** That is absolutely amazing. The analog bandwidth of this 220 meg front end obviously, they you know, there's a reason that they built that either they had the existing design and they said, "Ah, why not?" Or they but there's software options in there to do that.

**Dave Jones:** Or anyway, they plan to have like a more models in the future that have 200 megahertz bandwidth. It might be why they're supplying 200 megahertz bandwidth probes as standard with this thing even with the 50 megahertz model, I believe.

**Dave Jones:** But yeah, I'm not going to say like it's totally hacked now, but it shows that you can actually do this because the one of the problems is is I've got the 1102G.

**Dave Jones:** I've already got the fully populated model here. So, you know, really I need to try this hack on the base model 50 megahertz unit with the function gen. If you're going to buy one of these, make sure it has the function gen so that you can get that possibility in the future.

**Dave Jones:** And I did note that on some of the modes that I was using, it would actually the bandwidth 100 megahertz bandwidth software option and also the wave gen would actually vanish.

**Dave Jones:** In fact, where is the wave gen? Wave gen doesn't seem to be there. Oops. The wavegen generator instrument has not been enabled. There you go. So, wait. So, the current mode I've got this set to um has disabled the wavegen.

**Dave Jones:** So, like there are so many options on this thing, but I've seen that it does actually vanish a few times. So, it it's absolutely fascinating and I haven't even gotten through all of the possible And not only just the product config, but I haven't even changed the uh module config.

**Dave Jones:** So, maybe that's uh the error we saw in the 2.5 gig uh sample rate with the memory problem and all that. That might be a that might be fixable by changing the other uh the other resistors in there on the processor board, which is the module config.

**Dave Jones:** This is product config. There's like so many combinations of uh of code things in this. It's you know, it it'll take you forever to go through and systematically check them all.

**Dave Jones:** But I in theory I can do that now. I've got the pots in there. I can tweak the uh the product config pots from the top here and I can uh config the set the change the module config ones from the pots on the side.

**Dave Jones:** So, that's uh we're on our way. But this is absolutely fascinating to be able to get that extra bandwidth. Terrific. Um like I haven't done any measurements on this yet with the uh you know, pulse response and all that sort of stuff.

**Dave Jones:** But you know, the analog bandwidth is there. It's probably there for a reason. I'd you know, I'd say it's good. So, if you can actually buy the uh EDU function gen version and then increase the bandwidth to 200 meg um and the uh sample rate to 2 gig, then this thing I think's going to be really, really popular.

**Dave Jones:** Why wouldn't it be? Um, even without like the serial decode and stuff like that, if you can do that to the 50 meg version, then that's going to be terrific.

**Dave Jones:** But, uh yeah, that remains to be seen. But, it's looking promising. But, of course, it must be said downsides of hacking your scope hardware-wise like this is that, uh you instantly you lose your 3-year warranty cuz this puppy has a decent warranty on it.

**Dave Jones:** If you start going in modifying the resistors in there, they're going to know and your warranty is void. So, yeah, that's the risk you uh take. So, ultimately, you can actually get useful bandwidth uh increase in this by the looks of it.

**Dave Jones:** Hopefully, it'll work work on the 50 MHz uh model as well. I couldn't get the model number there to change, but uh you know, who cares, right? As long as the thing actually uh works, then you know, who cares what actually shows up.

**Dave Jones:** But, yeah, um it's to be repeated on the 50 MHz model, but it's looking very, very promising that all that stuff is in the configuration resistors. Haha. Good on you, Keysight.

**Dave Jones:** They were just asking for people to uh modify and have a play around with this thing, and that's certainly what we did. So, that is some progress anyway. All sorts of things yet to be confirmed, and then there's probably people working on like the keygen hacks and uh things like that.

**Dave Jones:** I'm no good at that sort of thing, so I won't be uh doing that sort of stuff. But, the hardware hacks work. And if you like this video, please give it a big thumbs up cuz that always helps a lot, and I'll link to the uh hacking thread on the EEVblog forum down below, and that's where everyone should consolidate their information uh for this thing as it comes to hand.

**Dave Jones:** Hope you liked it. Catch you next time. Mhm.
