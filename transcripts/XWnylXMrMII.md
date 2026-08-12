---
video_id: XWnylXMrMII
title: EEVblog #660 - Electrocardiogram (ECG) Experiments
url: https://www.youtube.com/watch?v=XWnylXMrMII
source: youtube-asr
---

**Dave Jones:** Hi, in a previous video I did a teardown of this St. Jude Medical House Call Plus transmitter. It's designed to connect up to your pacemaker and extract the data from it and send it back via the phone line. Well, this particular

**Dave Jones:** model, the House Call Plus transmitter, has an ECG function as well. And we took a look at some of the circuitry last time and well, some people wanted me to play with this. So, okay. Let's see if we can actually get some ECG data out of

**Dave Jones:** this. Normally, it's just they've got a separate isolator thing goes across the transformer into an the ADC here into the DSP and then it's I, you know, presume like a snapshot of that is sent back or maybe even live data sent back

**Dave Jones:** to the medical center or your doctor or whatever it is. The I think it's a service online you subscribe to and then your doctor can access it and all that sort of stuff. But anyway, I thought it'd be interesting to see if we can

**Dave Jones:** actually get some ECG data out of this cuz these can actually go quite cheaply. I've seen there's one currently on eBay for like, you know, 26 bucks buy it now or something. So, it could be a really good way to get like an experimental ECG

**Dave Jones:** system cuz it's nice and safe. As I pointed out in the previous video, not only do we have a medical grade power supply with it and yes, I will do a separate teardown of that medical grade plug pack in it, but we've got a

**Dave Jones:** medical grade isolation transformer in here. We've got all the ground separation. We've got the high value high voltage resistors in here in series with it, in series with each of these leads and, you know, and the ground isolation. So, pretty much,

**Dave Jones:** you know, even if there's a lightning strike or something, you're not going to die if you've got these hooked up to both of your wrists. So, it's pretty darn safe way to experiment. So, let's probe around and see if we can extract

**Dave Jones:** data out of this cuz all it is all this circuitry around here is just the analog stuff. It's just going to be a an ECG amplifier, a difference amplifier, and then sending that buffering sending it over the transformer to the ADC over

**Dave Jones:** here. All right, so let's have a look at some of the circuitry here. And as I said, this is all the isolated side. You can see the big safety isolation here and also going under the two power resistors there. And of course, these

**Dave Jones:** aren't power resistors because they're dissipating a huge amount of power. They're 330 K pop here. They're used because they're high voltage resistors. So, that's what they're being used for. So, all the big safety isolation here. So, all these grounds are completely

**Dave Jones:** separated. Now, we've got ourselves an optocoupler here, the Vishay CNY64. And if you go and look at the data sheet for that thing, then this side over here, these two pins are the LED and this side is the

**Dave Jones:** phototransistor. So, it's sending data back in that direction. So, it's sending something from over in all this analog stuff. These are all just op amps and comparators and stuff like that. So, this is purely just an analog amplifier

**Dave Jones:** for the ECG signal which is picked up over here. So, it's obviously sending something back. So, we don't have to worry although we might want to probe off that to actually see what's coming out of it. But really, what we want out

**Dave Jones:** of this thing of course is an ECG signal to see if I can get my you know heartbeat out of the thing. So, anyway, there's data coming back across the transformer like this. And obviously, they're powering over the

**Dave Jones:** um transformer as well. So, they've got to be transferring that power over. I don't see how else they're doing it. Something has to be powering all these. Anyway, we should be able to pick data off here. Now, this is the ADC chip Sorry, that's

**Dave Jones:** the ADC chip there and that's our DSP uh processor and you know, we don't really want to read the digital data out of this ADC. That's just, you know, silly. So, what we want to do is probe the

**Dave Jones:** analog signal and look, there's a test point there, TP5. Look at that. That's handy and there's also other test points on this side here and well, they could be uh power uh supply test points, but you know, more likely they're actually

**Dave Jones:** uh signal uh test points. Anyway, uh worth checking out to see if we can actually tap off the signal from one of these test points. So, we don't even have to maybe, if we're lucky, don't even have to go in and reverse engineer

**Dave Jones:** any of the uh circuitry to find out where the signal path is and actually uh probe the thing. You don't want to be probing over here, by the way. This is all going to be the differential amplifier. You want to probe at the

**Dave Jones:** final driving point. The ECG signal should already be scaled up by all this uh circuitry and maybe level shifted or whatever on the ADC here so that it inputs the right signal level so you maximize your 10-bit um dynamic uh range

**Dave Jones:** of your ADC there. So, let's have a probe around. Now, first things first, we want to find a ground point on this thing and usually these um PCB mount studs here aren't a bad way to do it and

**Dave Jones:** uh they're, you know, well worth doing, but che- check out here. Here's a Here's a test point which says to ground. So, there might be separate grounds here. So, I'm just going to check these. I'm going to just make sure that these are

**Dave Jones:** grounded. And yep, so that stud there is grounded and if we go all the way up here and probe these other ones, we can see that yep, they're also because you can see that the ground is continuous. You see that dark green under the board,

**Dave Jones:** means it's all sharing a common ground. So, you know, wait wait hello. That that um that mounting pad there is is connected to this ground over here, but this one is not. That is bizarre, and they're on the same

**Dave Jones:** Look at that. They're on the same Looks like they're on the same ground plane. You can see all the dark green under there, but that one's not actually connected through. That's interesting. So, why is that so? Well, it's a trap

**Dave Jones:** for young players. If you have a look here, I've actually got it switched on. There we go. The LED is on, and we'll probe around at while it was switched on. Oops. So, look. If we probe between these two points here, look at that. We

**Dave Jones:** get -85k. That is completely screwy. But, if we disconnect, Ta-da! Look at that. We're grounded. So, what we obviously had there is enough voltage differential there to completely screw up and confuse this meter. So, just be careful when you

**Dave Jones:** probe around this sort of stuff if you are probing If you're doing resistance checking like this, make sure you got it unpowered. All right. The other thing I want to do is actually probe around to see if we got voltage on

**Dave Jones:** this side of the transform all the isolation here. So, to power all this sort of stuff. So, we got ourselves a big ass tantalum cap there. So, it's obvious that we're going to probe across that, and hello. We got 0 V.

**Dave Jones:** We got nothing across that cap. Cap next to it. 0 Another tantalum over here. 0 What's going on? Power's on to the unit. I've got the LED on. But, uh we're getting nothing across these caps. There's no power.

**Dave Jones:** It's almost as if there's no power coming across here at all to power this stuff. Huh? All right, so let's start probing around to see what we get here. We have established that that ground point. It's got a little wire

**Dave Jones:** connecting to the crystal there. So, we can conveniently hook on to there. Otherwise, we could have like soldered a wire on to one of the those mounting posts or something like that. So, that's convenient place to put point and let's uh

**Dave Jones:** let's measure a few things. Let's measure our power supply first. We're 1 V per division. There we go. So, we're looks like we're you know, 1.8 V there or something. That's probably the supply for the DSP, perhaps. Let's go over to this other channel over

**Dave Jones:** here. 1 V per division. There we go. 3.3 V. So, yep, that's all right. That's our typical 3.3 V rail. Yeah, 3.3. Everybody happy. So, all the power on this side is good. Now, of course, if you keep your

**Dave Jones:** ground probe on this side of the transformer and then probe the other side over here, there is no ground reference on this point. So, watch what happens. We're just going to pick up a whole bunch of 50 Hz

**Dave Jones:** crap, is it? Yeah. Yeah, there we go. Spot on 50 Hz. We're just picking up a whole bunch of 50 Hz crap cuz there is no longer any ground reference over there and it doesn't matter what part of this circuit

**Dave Jones:** you probe over here, you're just going to pick up 50 Hz crap. It's useless. So, just a little tip. If you didn't already know, if you already have got your ground reference point on the other side of an isolated transformer like this,

**Dave Jones:** you're not going to be able to measure anything on this side. So, don't even try. And actually, if I wanted to probe on this isolated side, I haven't even found a good ground point for it yet. There's a mounting screw there, but it's

**Dave Jones:** not actually connected properly through. Yeah, I can see where one side of the one side of the capacity here probably goes down to the internal ground plane in there, but you know, there's no convenient hookup point and it looks

**Dave Jones:** like there's no ground test point like we got on these digital side over here. We got a few ground test points over here conveniently. So, yeah, you'd have to solder in something in there to do it. Anyway, I want to get this side

**Dave Jones:** first. Now, if we measure on the side of the transformer here, I've actually measured one side of the transformer is connected through to the main ground here and we're getting nothing basically on there. So, there's you know, there's no surprise that's

**Dave Jones:** just you know, 50 hertz crap. Don't worry about that. Um So, yeah, we we got nothing. There is nothing powering this side of the circuitry at all. And you've got to think, well, that's because that's under software art control and the thing

**Dave Jones:** hasn't connected. So, it's realized, oh, I don't have to measure anything. I don't have to do that ECG stuff because I'm not probably not connected through to the phone line and established a connection. Blah blah blah. So, that is incredibly disappointing. So

**Dave Jones:** much for an easy just be able to probe, you know, the output of the amplifier here and and get an ECG signal on the scope. It's not going to be that easy at all. Um you know, it's it's possible. You can

**Dave Jones:** obviously coax it into doing it eventually or you can hack into it to actually supply power to the circuitry and reverse engineer it and you know, figure out and just you know, eliminate all this other stuff like like tear out

**Dave Jones:** the transformer and just you know, wire in some power and on onto here and just you know, get the output of the final stage amp and Bob's your uncle, but jeez, very disappointed. And we're definitely getting no voltage on

**Dave Jones:** this side of the uh this side of the transformer here. Nothing. There's no power on these chips at all. Okay, so what I've done here because we're getting no power on this side at all, obviously uh the software

**Dave Jones:** is not driving this side or this getting no signal in this side, so there's no power over here. Here, so what I've done is I've sucked out that little puppy and uh we can actually see what's going on

**Dave Jones:** here and uh it's pretty obvious that uh the output of the transformer here um by you know, assuming that this side is the input over here, which it is, uh then the output here I don't even have to

**Dave Jones:** look up those two parts. I know that they're diodes, okay? So, we're getting um some rectification happening there to generate the power and that's our main filter cap. So, that's all that this thing is doing is just powering the

**Dave Jones:** transformer to get it's just nice isolation transformer purely to get power over here. That means the uh signal and data must be going back over the optocoupler here because we've already established if you look at the data sheet for this thing, then the LED

**Dave Jones:** is on this side and the phototransistor is on that side. So, there you go. It's much easier now to simply go and apply power to here. Uh we can have a look at the uh data sheet for these chips and try and

**Dave Jones:** figure out what the maximum uh voltage here cuz we don't have any uh schematic or uh specs or anything like that. Figure out the maximum voltage is whack a voltage across here and then we can start then probing around here and see

**Dave Jones:** if we can get a signal out. So, I'm just going to ignore all of the rest of the circuitry, not even going to bother to power it up anymore because it's completely isolated. Look at that. And uh then we should be able to maybe at

**Dave Jones:** least get this powered up, get an ECG signal out of here somewhere. But, before we do that, we have to find out which one of these pins is connected through to the ground plane. And it's pretty obvious, there's the positive of

**Dave Jones:** the cap there, so that's just going to be going through. That's going to be a diode that's going through, so I reckon this one here is connected through to the ground point. And the ground point's likely the negative side of that cap, and

**Dave Jones:** bingo, there it is. And you can go down, say the negative side of this cap down here. Yep, and as I said, there's no ground test point, so we should actually solder in just a little loop on there so that we can attach our

**Dave Jones:** ground probe down to that. But that entire ground plane there, you can see you can see down in there the via going right down in there. There it is, from the negative side, it's going nowhere except down to that ground plane

**Dave Jones:** down there. So, yep, that one is definitely connected through. So, that's our negative input, that's our positive input. Just look at the data sheets for these op-amps, you know, if their maximum voltage, say, they're a low voltage one, might be 6 volts, and you

**Dave Jones:** might just, you know, whack 5 volts on there, for example. And as it turns out, we've got nothing to worry about there. Look, we've got an LM317 voltage regulator here. There we go, so we could read those resistor values,

**Dave Jones:** figure out exactly what we've got there, but there you go. So, it's going to do the regulation for us. Beauty. All right, so I soldered on myself a ground test point here, and a couple of flying wires. I've got that going up to, well,

**Dave Jones:** I will have it connected to the bench power supply, and because this is a uh LM317, it's only got a LM317L low power version, it's only got a current limit of 100 milliamps. So, it's a good idea just to set your current limit on your

**Dave Jones:** supply to an arbitrary value of also 100 milliamps. So, I'm just going to start out at a low voltage, wind the wick up until we can see the LM317 regulate, cuz I haven't bothered to read the values on

**Dave Jones:** those resistors, and actually know what this thing operates at. And then you would set it like at least 2 V above that. So, I've got the probes uh just across the output capacitor there. Let's wind the wick up

**Dave Jones:** and uh see if we get any regulation on the output. Uh 1.6 V. Keep winding up. Winding up. It's drawing uh 710 mA. 4.2 V. 5.6 V input. So, 2.5 V out. Now, you've actually got to be uh careful here. This turns out

**Dave Jones:** this LM317 is not actually powering everything. Uh it's powering Well, it's obviously powering something, but the uh chips themselves, if we have a look at this LM uh 393 comparator, for example, dual comparator. There you go. It's 4 1/2 V. So, it's actually

**Dave Jones:** powered from the input directly. So, it's nothing to do with the LM uh 317 there. So, I've got 5 V going in, of course, and we're going to get, you know, 1/2 V uh drop on the diode, of

**Dave Jones:** course. So, yeah, got to be careful there not to wind up the input wick too hard because it turns out it actually bypassed that LM317 regulator there and went straight to these uh straight to the op amps and uh comparators. Now,

**Dave Jones:** these uh LMV824 op amps on here, if you look at the data sheet for those, well, they're only low-power uh devices. They're only uh up to 5.5 V uh voltage range. So, you know, really like 5 V input is fine for this

**Dave Jones:** sort of thing. You definitely don't want to go over 5.5 or 6 because of the uh diode drop. Then you risk it Well, you uh damage the op amp. So, um yeah. I mean, even, you know, even if you were

**Dave Jones:** down at like 3 V or something, it's probably enough uh dynamic range. You You know, these op amps can work down to low voltage. So, you know, it's pretty much is going to work. So, yeah, I reckon 5 V in there is just uh perfectly

**Dave Jones:** fine and dandy. Now, in terms of safety, of course, cuz I'm going to put these all I've already touched them. There you go. If I was going to eat it Jeez, no. I'm just fine because I we're only working at 5 volts from our

**Dave Jones:** isolated bench power supply, just like you used to for all your projects. There's nothing dangerous there at all. And yeah, we are connecting the ground ground reference in this circuit. But once again, you it's just like powering a regular circuit. And we've got the two

**Dave Jones:** big-ass 330k resistors in series there. We don't even need those for stuff that we're going to do here. So, this is all completely safe. You can muck around even beginners can muck around with this sort of stuff when you've only got like

**Dave Jones:** a an isolated 5-volt supply. No problems at all. And here we go. Yes, I've got my wrist strap on. No, it doesn't matter that I'm wearing the watch. And let's see. Let's probe a couple of the test points around here and and see what we

**Dave Jones:** get, shall we? So, now I've got it powered from my 5 volts. So, let's get in here and give it a whirl. And of course, this is not the best way to get an ECG, of course. Like right at the

**Dave Jones:** end of your arms like this is, you know, it's one of the worst ways to actually get it. They need to be like on your chest, proper chest sensors and things like that to do it properly cuz you

**Dave Jones:** might get you know, impulses and and noise coming from your muscles and you know, everything else. So, you've probably got to be in a relaxed state. Anyway, we just need to see. So, I'm just going to probe a random test point

**Dave Jones:** here. As we saw before, I'm going to probe TP8. And hello. Hello. What do we got there? We got something. All right, let me probe TP6. Oh, yeah. Hello. Look at that. We definitely had something there and all of a sudden it

**Dave Jones:** Oh, it's all over the shop. It's all over the shop, but we're getting we're getting something. Oh. Oh. All right. This is rather rather unusual. Hmm. Oops. Trap for young players. Look at this. TP8 that we had before. Watch. If I

**Dave Jones:** touch the anti-static mat Look at that. So yeah. Oops. Um something's going on there. Okay, let's not touch the anti-static mat even though this is Yeah, people will go oh yeah, the anti-static mat is conductive. No, they're dissipative. Um so they're you

**Dave Jones:** know a ridiculously ridiculously high resistance. Um but uh it's obviously enough to pick up um something. I mean, we're dealing with very low-level signals here. So, I'm not going to touch the bench at all and uh let's have a look. See if we can uh AC

**Dave Jones:** couple that sucker and uh yeah, I'm not sure what's going on there, but uh Is that a cardiac pulse? No, I don't think so. No, we've got an oscillator there. Just fine and dandy.

**Dave Jones:** Test point one. Uh that's going to be No, we're getting zippity-do-da at the moment. All right. So, what I've done is I've got it up on a wooden frame isolated here. So, none of the input circuitry is touching the uh ESD mat at

**Dave Jones:** all and we're going to probe TP8 again. Hello. What have we got there? And there you go. That's exactly the same signal that I was probing before, but I don't have the wrist straps on anymore. So, let me actually

**Dave Jones:** just touch them again. Here we go. Ta-da! So, I'm now holding I'm just holding them. I haven't put them on, but there you go. Have we got something? Okay, what I'm probing now is actually the output to that optocoupler. Okay, so

**Dave Jones:** what's driving that LED on the optocoupler there, and you can see jitter on the signal, and I'm if I'm not mistaken, this might actually change with my pulse rate. So, I'm going to jog here. I'm jogging on the spot. See if I can

**Dave Jones:** get my pulse rate up. Here I am. Come on. Come on. It's hard to get my I'm quite fit. It's hard to get my pulse rate up. I'm sorry. Hang on. Lost my probe. I have a naturally low

**Dave Jones:** heart rate, by the way. But, I don't know. I reckon I reckon if I get my heart rate up, I reckon there's more jitter there. And if I stand still again, and relax, you can almost see it beating

**Dave Jones:** to my chest. I I was moving my arm there. Sorry, I was putting my hand over my chest to And I think it's jittering to my heartbeat. I think. That could be an illusion, but that's the impression I'm getting.

**Dave Jones:** Now, back to the signal that we're getting on test point eight here. It's a Whoa! Don't not sure what happened there, but yeah, it's a complete furphy, because well, it's nothing like an ECG signal, and it's not even in the same ballpark.

**Dave Jones:** In fact, we're using the wrong measurement technique on the scope here cuz we're talking, you know, heartbeat like once per second, you know, boom, boom, boom, right? So, obviously, we need to get into our Let's go into a horizontal

**Dave Jones:** menu here. We need to get our time base instead of put it on your usual time base, you want it in roll mode like this. And this is what roll mode is actually good for. And there's nothing on this test point that I can see

**Dave Jones:** anyway, but if we move it over to another one, TP6, bingo. Look at that. Hang on, we're still got some crap on here. But, boom, boom, boom, boom, boom. There we go, and that follows my heartbeat. So, that's that TP6 test point down in

**Dave Jones:** there. It's the output of one of the uh quad op-amps there, and I've checked uh some of the output other outputs, and I can't really find anything. This is like the best sort of signal I can find that

**Dave Jones:** actually matches my uh cardiac pulse. So, you can clearly see my pulse in there. And watch this, if I go like that, I can make it See? I can make it do stuff because I'm just, you know, this is, as I said, this

**Dave Jones:** is not the best technique for doing this sort of thing. You're going to pick up all sorts of crap, but cardiac pulse is definitely in there. Right, and I should be able to prove that by closing my eyes

**Dave Jones:** and uh measuring my pulse, and I'll tap on the oscilloscope every time I feel my pulse. So, ready? Let's make sure I got a good waveform there. Yep, see, lip, lip. So, here we go.

**Dave Jones:** Is there any correlation there? There should be. And if I stop that and turn on the cursors here, we see that we've got a delta of about 980 millihertz there, which of course is slightly faster than 1 hertz, so slightly higher than 60

**Dave Jones:** beats per minute. Works out to around about 61 beats per minute there. That's much higher than my naturally resting heart rate cuz I'm working here and doing all sorts of jazz. So, you know, it's a little bit elevated. Anyway,

**Dave Jones:** let's take that as a baseline. I'll keep the same uh roll rate and time base, and we'll be able to see let's now do some exercise and see if we can increase it. Whoa. There we go.

**Dave Jones:** And here we go. I got a few jumps in there, and yeah, you can see it's now much, much quicker. And there you go. We've got a delta of 2.17 hertz there, which works out to about 130 beats per minute. And I'm back on

**Dave Jones:** regular time base mode now, and unfortunately, I can't turn averaging on at such a slow time base. And averaging doesn't work in roll mode either, but I can like change to high res mode, which does that boxcar rolling average, but still

**Dave Jones:** we can't really clean up that signal much, and we're not really going to be able to see that cardiac pulse, I'm afraid. Here we go. Settle out. Yeah, we're you know, it's kind of sort of there, but and because I know some people ask, no,

**Dave Jones:** it's not the scope grounding here. If I use something like my uh Lecroy uh differential probe here, it's just it's just even noisy. I mean, a single point ground cuz our power supply is floating. So, a single point oscilloscope uh

**Dave Jones:** ground there is not going to do anything, but that's just picking up all sorts of crap. So, that's no good at all. And yes, I've tried all sorts of things like my Australian safety boots here. Um you know, just to isolate

**Dave Jones:** myself from the floor and uh you know, stuff like that. And well, nothing's working. I'm not catching a break. You know, I can't seem to get like an ECG an actual ECG uh waveform out of the thing, which is a bit of a

**Dave Jones:** bummer, but it probably needs uh needs some more work and stuff like that. We you know, really tricky business trying to uh probe this sort of thing. You got to eliminate all sorts of uh you know, environmental uh stuff and test setup

**Dave Jones:** and uh probing issues and things like that um from the equation. So, that's not uh easy at all. You have to systematically go through and uh cater for those things. But anyway, I think I did get at least something out

**Dave Jones:** of that. See if there's any correlation between my tapping and the slight modulation on that waveform. Here we go. Make sure yeah, everything's fine. Okay. Here we go.

**Dave Jones:** Any correlation? So, obviously what they're doing is uh you know, squaring up this signal really early and getting some sort of you know, uh uh you know, modulation of a clock out of it and uh decoding it that way. So, I'm not even

**Dave Jones:** sure if this thing actually you know, can record like an an ECG signal as such. So, yeah, I'm not not entirely sure what's going on there, but I'm pretty sure I found that that is modulating in time with my heartbeat. If

**Dave Jones:** I, you know, if I hold my hand there and do do do, you know, I can actually uh correlate it to um what's going on on that uh scope there. Anyway, it requires uh further investigation and decoding and uh stuff like that, but there you

**Dave Jones:** go. That was my first crack at that thing anyway. So, that's all I got time for today uh unfortunately for playing around with this thing, but I'll whack up this video anyway. I don't like leaving things around um you know, until

**Dave Jones:** I absolutely complete them cuz I might not get around to uh playing with this thing again, but there you go. There's just a couple of little uh experiments. I was a bit disappointed I couldn't just get, you know, a single-ended ECG

**Dave Jones:** waveform out of this thing. Um although that maybe that was unrealistic, but anyway, I think I've found a correlation there with that uh digital um output. So, yeah, maybe that's how it's actually doing it. It's probably squaring it up

**Dave Jones:** early and I don't know, you might have no chance of getting an ECG out of this particular uh circuitry here. So, anyway, I hope you enjoyed that uh fun little playing around. And if you've got any uh ideas or suggestions, please

**Dave Jones:** leave it in the comments. Catch you next time.
