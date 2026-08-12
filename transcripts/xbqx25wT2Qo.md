---
video_id: xbqx25wT2Qo
title: EEVblog 1418 - The Most EMBARRASSING Repair!
url: https://www.youtube.com/watch?v=xbqx25wT2Qo
source: youtube-asr
---

**Dave Jones:** Hi, it's repair time, or at least attempted repair time. This one comes from the EV blog lab. This one I've had sitting around forever. The Keysight DSOX1102G. None of that black case rubbish that they've got these days. This is the good

**Dave Jones:** old beige box. And a 100 meg 2 gig sample per second jobbie. Very nice scope, of course. But yeah, this one is, as it says on the top, rooted, as we say here in Australia. Don't know when I put that

**Dave Jones:** sticker on, but it was at least a couple of years ago. When I powered it on, it came up with a uncalibrated error. And if I remember correctly, yeah, what I think one of the channels, I don't think it was both. Hopefully,

**Dave Jones:** it's only one of the channels, because when you've got when you're repairing a product and you've got something like in this oscilloscope that has two identical channels, you want to hope that only one of them failed. Because then

**Dave Jones:** you you know, you've got another channel that you can physically get probe comparison to. There it is. System concerns detected. Instrument is uncalibrated. Whether or not it lost its calibration and that's potentially another fault, or whether or not, most

**Dave Jones:** likely, it's related to the vertical problem. Now, I believe I first encountered this when I was using this to shoot a video and I was measuring some stuff and it just didn't seem right. The values seemed out, I think.

**Dave Jones:** Just didn't make sense. So, I yeah, I finally came to the conclusion that yeah, it was rooted. So, yeah, aside it went and I haven't had a look at this since. So, let's give it a burl and thankfully,

**Dave Jones:** it's got its own test generator built in. We can just hook that up to here and see. We don't need any external stuff. So, let's go. What what what I don't have the license code. Ah. Bummer. Thankfully, we have a backup.

**Dave Jones:** We've got our pro calibration signal and yeah, we're getting something. No wuckers. Let's uh let's trigger on that, shall we? Trigger type auto. Source, there's your problem. Source number one. There you go. Like a bought one. Anyway, we could

**Dave Jones:** tweak that with the pot there, of course, but anyway, that seems to work. So, 1 kHz, that's what you'd expect. I don't know what the signal level you'd expect, but uh let's compare it to channel two. Ah, that looks right. Uh

**Dave Jones:** 500 mV per division, 50 mV per division. One of them's obviously set up for uh 10 one to one there. This one will be set up for 10 to one. There it is. So, if we turn that back, no wuckers. And uh 50 mV

**Dave Jones:** per division. Now, it's making a it's making a fool out of me. Um it works. Oh, yeah, look. Look. Look. Look. Look. Look. There's your ground reference. Shift it. Whoa, look at that. It's shifted down. That's right. I remember

**Dave Jones:** now. Yeah, it wasn't the It's not like the signal failed. Yeah, it's all coming back to me. Yeah, look, the DC Yeah. Yeah, look. Look at that, the DC shifted. We're in DC mode, right? We're in DC coupling.

**Dave Jones:** And DC coupling and all of a sudden, yeah, look, it's gone negative. So, there's something wrong with the DC offset. So, yeah, if I put both to the same level there, I can cheat here and just set it to uh line uh triggering so

**Dave Jones:** we can at least see the waveform. Then we can swap between the two channels, right? Yeah, well, yeah, look. Yeah, look. The DC offset. I didn't even notice that. Yep. Yep. So, we've got actually got a DC offset problem

**Dave Jones:** on both channels. So, the sampling seems to work. The ADC's working. The triggering system's working. The uh you know, everything seems to be working, but we have a DC offset issue on both channels. That's annoying. Um so, there's probably something common

**Dave Jones:** to That's weird cuz I would have expected the DC offset to be generated when you you know, turn your vertical position control here. It adds a DC offset value to the signal being measured and I thought that would have

**Dave Jones:** been generated within the channel itself. So, oh, we just saw a reversal direction there. So, slight drift between the 50 hertz mains and the 1 kilohertz internal. It's going to go back. It's going to drift back. Lovely. Anyway, that's fascinating. I've done a

**Dave Jones:** video on clock drift actually. I might have to link it in up here if you haven't seen it. So, yeah, that's a bit of a bummer. I would have liked to have had like one functional channel. So, yeah, I wouldn't

**Dave Jones:** have expected the DC to be central, but it could just be like a power supply powering both of them or something like that cuz I know I remember from the teardown there are and as you'd expect like some local regulators surrounding

**Dave Jones:** the input circuitry. So, hey, what's No, that's just pick up from here. Yeah. Something just switched on. I've done a video on common mode rejection pick up as well. Hmm. Anyway, let's crack it open. And just to show you what it's supposed

**Dave Jones:** to do, of course, here's the black version. The black version works. The beige is the problem. There you go. Right, it's fixed. All you got to do is spray paint it black. Yeah, there you go. So, there's no

**Dave Jones:** change in the DC offset and the calibration output is DC reference. So, yeah, something weird happening with the rooted unit where it's based on the range like has DC offset issues, which is interesting cuz I mentioned before like the external

**Dave Jones:** voltage regulator like you know, powering that. If if that was a problem, then you'd expect it to be a problem on all ranges possibly. So, yeah, this is a This is A WEIRD ONE.

**Dave Jones:** GUESS WHICH UNIT THIS IS. Anyone remember? Um trust me, that's not a factory Those trim pots aren't factory fitted. D'oh! This is my original hack hack a unit. I did that video hacking this scope. So, oh, goodness. Yeah, I've I've screwed

**Dave Jones:** the pooch. Who knows what I've done to this thing? Um the poor bastard is probably I'm going to say right now there's like nothing wrong with that front end. I'm going to say I've done something horribly wrong to the scope. So, the first thing I'm

**Dave Jones:** going to have to go do is watch my video where I added these trim pots where um if memory serves me correctly, when it boots up, it reads a voltage divider and that tells it what bandwidth of the

**Dave Jones:** scope it is and stuff, but I like I don't remember that ever screwing up the left some screws out here, too. Look. That's a bit how you doing. Oops. So, yeah, I don't recall there ever being any issues with it. I can't remember.

**Dave Jones:** Anyway, d'oh! This is my hack scope. Yeah. So, this is not a Keysight failed instrument. This is a Dave fail. Yeah, I've done something horribly naughty to this. Okay, after that embarrassing revelation, don't hack your products, kiddies. You're going to come

**Dave Jones:** and get some like Uncle Dave. Anyway, because it seems to be like a good a calibration issue. It says it's uncalibrated and of course DC offset would actually is part of the calibration. I think you can do an auto

**Dave Jones:** calibration for DC offset. So, why it's actually lost its calibration, I don't know because I remember at the time the hacked scope was working. So, yeah. Anyway, I like maybe I around I I think I vague recollection of

**Dave Jones:** around with it more perhaps after the Yes, I checked it two videos that I did on this thing. So, maybe we can go into utility and service and start user cal, shall we? Well, let's do hardware self test. Let's

**Dave Jones:** see what pops up. Nope. They went self test failed. Trig comp and max. Oh, no. That's not good. There's more to this than perhaps it wasn't my hack. Although most likely it's something to do with it. But, you

**Dave Jones:** know, it's self test failed. It trig compensation I presume and and max. Yeah, what's going on? It is the one mega zoom 4 A6. So, it does max between No, does this max between the channels? I can't remember.

**Dave Jones:** Um anyway, I don't know what max they're talking about there. But, that's interesting that those self tests failed and not these. Anyway, let's run a standard user cal, shall we? So, we'll give that a whirl. Calibration factors are protected. Go to utilities

**Dave Jones:** option. We got a cal protected disabled. See, I would never have disabled the the protection on this thing. So, anyway, we're going to go disable that. Utility, options, auxiliary. Cal protect disable that. Back, back. Utility, service. Disconnect all inputs from the front

**Dave Jones:** panel before using hardware cal or use right start user cal. Okay. Oh, 7 minutes. I will get back to you. Yeah. All right. The good thing about this is you can actually operate this with the case actually off. You can probe as I

**Dave Jones:** saw in the hacked videos linked up here, cuz they're rather fascinating. They're 40 minutes long, so I haven't watched the whole damn thing again, cuz that bloody EE Vblog guy likes to bloody waffle on. Geez, you know? Anyway, you

**Dave Jones:** can see, look, it's shifting the DC offset there. So, it's it's doing that for each channel. So, it's going to be interesting to see what comes back at the end of this. I don't know, you know, what these waveforms are or whatever,

**Dave Jones:** but it's obviously generating those internally and using those. Seems like an oddball waveform to use for calibration, doesn't it? Yeah, I don't I'm not really concerned with like doing this calibration with the back off and stuff like that. It doesn't really

**Dave Jones:** matter. Like, it's the front-end cans or or the steel shield and the stuff like that. So, no worries. So, after all that, we got the super useful message, user cal failed. Okay, well, thanks for that. And you can see that the DC offset

**Dave Jones:** is way below where it should be. Unless you go to 200 mV or 500 mV, it's suddenly jumped back down to Oh, look at Yeah, see how it goes like 1 2 5 gets towards the end 10 is perfect. I guess the only thing left

**Dave Jones:** to do, really, is restore this thing physically to what I had before. So, like I could go and watch my own bloody videos and work out where to what the voltage reference points were and to set the trim pots and everything back to where

**Dave Jones:** I'm better off trying to just No, physically removing the entire hack, putting back the resistors if I've still got the values. I think I'll try and just physically restore it first things first and get back to where it

**Dave Jones:** originally was. I might have to crack out the UART, too. Yeah, it looks like I've removed all four of the resistors there and replaced them with the trim pot. There were two separate voltage dividers there and two trim pots. So,

**Dave Jones:** yeah, I don't have the original resistors. So, hopefully somewhere in my video I've got the original values. Now, as it turns out, these resistors in here that I took off going up to the trimmers up here we actually have in the original

**Dave Jones:** video. Here it is the EIA codes for these and yeah, sure enough we've got two 10K resistors in there as a voltage divided to give mid-rail, which is 1.25 volts, and the other one to give 0.69 volts. So, yeah, we've got

**Dave Jones:** the exact values. They actually were marked on the top, whereas the ones on the processor board aren't. But, we've got the voltages for those two. Of course, I don't have any bloody 4K7s, do I? 470 ohms, 470K. Bloody Murphy. Aha, we might be getting

**Dave Jones:** somewhere. I replaced those resistors on the main board. Haven't actually measured the voltages yet. Values are supposed to be 12.1K and 4.64K, but a 12K but in E12 series instead of the E96, the 12K and the standard 4.7K

**Dave Jones:** and that gives you 0.7 instead of 0.69 volts. So, it's going to be good enough for Australia and look, it's obviously detected that change cuz we never had this on boot up before. System clock is defaulted. Instrument is uncalibrated.

**Dave Jones:** The default setup was loaded. So, that's promising. So, may you know, maybe this could be as simple as I was simply tweaking fiddling with. Don't twiddle with your knobs, let me tell you. I was I was fiddling with my trim pots and maybe I

**Dave Jones:** can just completely and utterly screwed it up and put it into some mode that it didn't like and that just like I don't know corrupted the default boot up and maybe the calibration, although it shouldn't, but you know, you never know.

**Dave Jones:** You're lucky in the big city. So, yeah, I'm going to run through the system check again, but before I do that Look look look at this. Look at this. Look at this. Ah. Yeah. Yeah. There's no DC offset. Let me plug the probe back

**Dave Jones:** in. Is that all it was? Is it I Yeah, twiddle the uh trim pots. Hang on. All right, there's our signal, and sure enough that looks good. I mean, yeah, I'm sure it's probably lost its calibration values, but I don't know, maybe I don't

**Dave Jones:** don't know how we fix that, cuz I don't think there's any like user calibration, at least the data's not available for it, but you know, anyway, we can check exact signal levels before, but our DC offset issue is gone, and I

**Dave Jones:** guarantee you it's gonski on channel two as well. I don't even have to trigger off that to know. Yep. Yep, we fixed our DC offset issue. So, that is fascinating. Just trimming the pots, and remember we've got two different pot types of

**Dave Jones:** pots in there we got four pots in this thing, two different types. One is the product configuration, which was the ones I just changed there on the main board. There's two voltage dividers on there, two different voltages, which

**Dave Jones:** give you Here's the screenshot of the original data dump for it. And then we've got the BLT ones. BLT, of course, in Australia is a bacon, lettuce, tomato sanga, and those BLT trim pots, they change the module configuration. So, and

**Dave Jones:** and I haven't fixed those yet. They're still the original trim pots at whatever values I left them at. Couldn't be bothered hooking up the UI yet, but yeah, if I just put in the default resistor values from before, but

**Dave Jones:** anyway, it seems to have come good, but anyway, changing those product configuration bits you So, with those there's only two bits on the product configuration, but because we're talking about multi-level ADC reading, you can have as many levels as you want. I think

**Dave Jones:** there might have been four levels from memory per bit. So, that gives you a fair number of configurations. Anyway, there are configurations where you can completely come a gata and it just doesn't do the DC offset properly. Um so, yeah, it was

**Dave Jones:** it was those two trim pots on the main board that I was obviously around with, but I swear I would have had this working when I put it back together and close the case, and I swear I had used

**Dave Jones:** the thing. Now, possibly I could The only thing I can think of here is that I might have been The trim pot might have been right on the noise margin, right? If you know, it just being between one

**Dave Jones:** mode and another mode and I thought, "Oh, yeah, no worries. I'm in the middle." I mean, that obviously didn't might not hold my tongue at the correct angle, and um I think it's just slowly drifted into over time. Um or you know, just like

**Dave Jones:** different temperature or whatever it is, you know, the moon's not at the right phase at the moment, and it's changed product configurations, and that's just completely screwed around with it. There you go. That's a repair of my own goof.

**Dave Jones:** Fantastic. Okay, I'm going to start to use the calibration again. Hey, look. I've got my wave gen output back. Did those Did that product configuration disable the wave gen? Oh, boy. Hang on. Um anyway, I'm going to disable cal protect, and I'm going to

**Dave Jones:** go into my wave gen. I got it. I got MY WAVE GEN'S BACK. SO, it looks like the product configuration can override the license in the thing. So, it obviously had the license in there, but if it didn't have the product

**Dave Jones:** configuration, it goes well, I physically goes, I don't care that there's a license installed, you don't have a hardware SigGen installed in this thing. But, do they sell this without the hardware SigGen? I can't actually remember. Yes. Yes, I think

**Dave Jones:** they might. So, there you go. I think that's um something that we didn't know before from that original hacking video. So, I think we've learned something new. This video wasn't completely worthless. Anyway, I'm going to go in there and

**Dave Jones:** start that user calibration. No wackers. We'll come back in 7 min waveforms. Yeah, the same as last time. Yeah. So, they've got all sorts of cruddy things. Yeah, look, it's all over the shop. Anyway, come back in 7 minutes. I

**Dave Jones:** reckon it's going to work. Well, actually, I hope it doesn't because then we'll actually have something some hardware fault to actually troubleshoot rather than just a fixing a stupid Dave goof. User cal passed. Winner, winner, chicken dinner. There you go. We can get to a point

**Dave Jones:** where you have got an invalid product configuration and it won't pass user calibration. You would have thought that well, you wouldn't allow that, right? I don't know, just in case, like from a programming point of view. I don't know.

**Dave Jones:** Programmers out there, tell me. Is this like a a lapse in and a bit of an oversight here or is this oh, well, no, of course, you know, you dick around with the hardware, you get what you get and you don't get

**Dave Jones:** upset. But, I would have thought that like any product configuration should not be able to screw up the calibration and the DC offset and things like that. I mean, I I don't even know how that happens. Surely, you'd have a robust

**Dave Jones:** enough system so that well, if you did get into the wrong mode for insert reason here, like you have a user is around with trying to hack the thing. And then yeah, it screws up the DC offset and

**Dave Jones:** looks like for all the world like a hardware failure. Like I thought this was a hardware failure. And like my mind instantly went into hardware mode and it well, it's well technically was hardware but not in the way

**Dave Jones:** that you'd expect. Like user calibration and and DC offset and you know, adjustments between vertical levels that should have nothing to do with the product configuration. So, anyway, yeah, I don't know, programmers out there? Let us know what you think. Have you

**Dave Jones:** been involved with something like this before where you've dotted all your eyes and crossed all your T's so that no matter what the users do, they can't possibly um you know, screw it up in this way. But yeah, trust me to do

**Dave Jones:** it. And it seems to be bang on calibration. I'm feeding the sig gen out which I've set to 500 millivolts peak to peak here and you can see I'm reading 508. So, that's that's not too shabby at all, is

**Dave Jones:** it? So, it can measure each range 310 315. Like you know, that's good enough. Like scopes are not that accurate. They're only like you know, the 3 to 5% accurate or something like that. Like a really good scope will be like 2%

**Dave Jones:** accurate or something. So, yeah, they're they're not that great. So, let's change the range again. 310 measuring 315. No wackers. 120 measuring 121. Go back down even more. Bring it up to near full scale. When you're testing calibration like this, you want to do go

**Dave Jones:** near full scale. 344. We're getting down into small signal levels now. So, 130. So, yes, I know that the calibration could have screwed up the wave gen as well, but it's unlikely that both of them out by the

**Dave Jones:** same amount. So, I can double check with another uh or another function gen, of course. No, I'm I'm fairly confident that this is actually okay. Yep, 70 mV, no wuckers. Even down to the smaller signal levels, 9.6, we're measuring 9.8,

**Dave Jones:** no wuckers. And that's 1 mV per division, which isn't true 1 mV per division, cuz this scope is only This is only Now we're getting into the digital stuff, but 6.7, measuring 6.8. Let's go up to 12 V peak-to-peak. Yep, 12.1.

**Dave Jones:** Yeah, that's a winner. So, that's kind of disappointing, actually. Um going to have to go through and uh fix up the other uh resistors, the uh bacon, lettuce, tomato resistors in there, and uh put those back to their original

**Dave Jones:** values. But yeah, it looks like it was the product configuration that was screwing it up, which kind of makes sense. Um cuz the other ones were just like uh modes or something. I don't think I ever I can't recall details of and followed

**Dave Jones:** uh through some other people took the reverse engineering further than I did in those two videos, and discovered all sorts of stuff. But I would change those back. But yeah, it's a product configuration that we uh came a gutser

**Dave Jones:** on here. Oh, well, what would I have done next? I would have got in there, checked any voltage regulators, of course. First rule of troubleshooting, thou shalt measure voltages. So, I would have looked for any little uh SOT223

**Dave Jones:** um regulator-looking package, either for the main one for the whole board, or as I said, that I believe there's some local uh regulation around there. Is there? Let's have a look. Yeah, I'm not sure if there would have been any

**Dave Jones:** voltage regulation in there or in the can. We'd have to take it off. Uh but there doesn't seem to be any like that over there. That could be a voltage regulator, for example. That But that's more got to do with the uh trigger

**Dave Jones:** system, which by the way, the uh trigger system on this scope, you can actually use it like as a third uh channel. They don't advertise it very well, but it like it's digital only, doesn't have the full analog front end. But you can

**Dave Jones:** actually display the signal. Yeah, you used to be able to get this back in the old day. I had an analog scope. What was it? A COS 6200. And it was a 12 channel scope or was it 14 channels? Yes, I kid you not. It's

**Dave Jones:** because you could get It was a four channel scope, but then you could also get the trigger view as well. This is what it was called on analog scopes, trigger view. And then you could also double those number of

**Dave Jones:** waveforms cuz you could get get get the displayed sweep waveforms as well. And then and then it had an extra channel somewhere. I don't It was I think it was at least 12 channels. Anyway, the COS 6200, I believe it was. Geez, why why did I

**Dave Jones:** ever sell that? That was a great scope. Anyway, yeah, I would have measured all voltages. I would have certainly checked because when you dick around and solder and hack things like this, I would go in there and visually inspect,

**Dave Jones:** check for any like little solder balls cuz when you're soldering on a product, bit of a pro tip here, you can often get like, you know, it can the solder can spit, give little, you know, splashes and you may not see this

**Dave Jones:** at the time you're doing it and it may leave a solder ball or a solder splash somewhere, which can then flap around in the breeze and move around in your product or you know, and short between pins or something like that. So you give

**Dave Jones:** the board a good visual inspection, then you might give the board a good clean as well if you've, you know, been hacking around on it once you restore it to its configuration or you do do your repair. You want to get in there with a hard

**Dave Jones:** bristle brush and give it a good wipe with your isopropyl or whatever it is you use. So yeah, I would have got in there and measured voltages, visual, have a good tidy up and yeah, then well, I don't know if if

**Dave Jones:** still wouldn't have worked after that. I don't know what I would have What I would have done because can't get the schematics for this thing and it happened on both channels and well, it's not actually a real hardware fault. It

**Dave Jones:** seems to be just like a software induced fault. So, that's weird. Anyway, that is fascinating. Um not entirely pointless video, but yeah, a bit embarrassing, but I always post my embarrassing I don't care. Anyway, hopefully you learned something. So,

**Dave Jones:** anyway, if you liked it, please give it a big thumbs up and as always, comment down below. Catch you next time.
