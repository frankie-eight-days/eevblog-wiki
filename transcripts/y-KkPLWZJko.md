---
video_id: y-KkPLWZJko
title: EEVblog #512 - Rigol DP832 Bad Design Investigation
url: https://www.youtube.com/watch?v=y-KkPLWZJko
source: youtube-asr
---

**Dave Jones:** Hi, uh I was just going to have a quick play around with this Rigol DP832 power supply. This is just a uh trace out the output circuit and uh probe a couple of waveforms and uh stuff like that. Maybe

**Dave Jones:** uh see if I could possibly find out uh uh what's going on, investigate that uh power on uh spike a bit further, but got the guts hanging out. And one of the first things I noticed was that um

**Dave Jones:** suddenly like I couldn't see the display, but the fan would suddenly start revving up and then uh going crazy. And I found out what was happening without even probing the thing is that the power supply would actually reset

**Dave Jones:** after a little bit of time. And I'm going to leave it here and uh just see if it resets. So, I switched on all the outputs there and uh hopefully if I won't touch it cuz I think maybe, you

**Dave Jones:** know, the reset might have something to do with, you know, there might be an EMI issue. The board's all hanging out here, all the wires, the you know, the some of the digital stuff going here is all loosey-goosey hanging out in the breeze.

**Dave Jones:** And uh maybe that has something to do with it. But anyway, um I'm just going to leave it here. There's no load on it, of course. And I found that the damn thing reset. So, I'll just leave the

**Dave Jones:** video running and see if we can capture that. Usually it doesn't take too long. It only takes like a minute or two. No, as Murphy would have it, it's not going to reproduce the problem. The old white coat syndrome

**Dave Jones:** strikes again. I've left it for a couple of minutes and uh annoying. Anyway, what I was doing is I was adjusting the output voltage in steps just as a first uh thing just to see where it um you know, it got the uh

**Dave Jones:** transformer taps and uh stuff like that. So, maybe if I turn the voltage back up or something like that. Anyway, I'll leave it for another couple of minutes. I don't remember moving it or touching. I didn't move my multimeter it here out

**Dave Jones:** of the shot to to here, but I don't know. Better hold my tongue at the right angle. Hang on.

**Dave Jones:** Woohoo! Did I get it? Did I get it? I got it. See, it reset. It took bloody what, a 9 minutes on the camera here, but I got it. So, I was just in the other cubicle and heard the fan rev up. Bastard. So,

**Dave Jones:** the thing just resets itself. Let's turn that back on see if we can get it to reproduce even faster. I don't know why. I have no idea. I'm not probing anything, not touching anything. The outputs still seem to work, but I've

**Dave Jones:** got it under no load and the thing just reset itself. There we go. There we go. Got it. Bingo. What was that like a minute? There we go. It just switched off and reset. Why? I have no idea.

**Dave Jones:** My only guess is because it's, you know, it's hanging out here. It's not in the system. So, it may be an EMI issue getting in somewhere that's resetting this sucker. I don't know. All I can do really is

**Dave Jones:** fold this back in, screw it back in place, and run it as a bench supply for, you know, an hour and see if it see if it resets. Now, there's one thing I found is that this regulator in here,

**Dave Jones:** this tiny little that's an LM317, that's actually delivering the that isolated 5 volts for the main logic that we saw in the teardown, and I noticed that was getting really, really hot. And look at that. I mean, we're talking, you know,

**Dave Jones:** this isn't going to be super accurate, but look. I mean, it's not going to read over though. So, you know, I was getting close to 90 or something at one point. There we go. 95. It's crazy. That thing

**Dave Jones:** is getting super hot and I'm not sure if that's normal or not. Surely it can't be running that hot. Unbelievable. Have no idea why. Now, I've actually measured this thing and there's the 5 V that it's actually supplying and the input

**Dave Jones:** voltage, if I can actually get in there, correct ground. Yeah, there we go. 12 V. Now, I'm reading well over 100° on that now and I can should be able to get in there with a thermocouple and even confirm that. Look

**Dave Jones:** at that. That is ridiculous. 110° on the heat sink and this thing's only been on for like 10 minutes 115, 120. Unbelievable. No wonder something that regulator is just going to shut down and no wonder the thing's going to reset.

**Dave Jones:** So, clearly something is drastically wrong there because, you know, like an LM317 is only got an operational temperature range to like 120 125° or thereabouts and it's got built-in thermal overload protection. So, I think that's why this thing's resetting. Actually, as I think

**Dave Jones:** that even though I haven't measured it, I think the regulator is just getting too hot and it's shutting down for some reason. And of course, you can't have it operating at that temperature. It's just ridiculous. Let alone the like I was

**Dave Jones:** measuring what 110° plus on the case after a minute or two, let alone the actual die temperature itself. So, yeah, it's going to thermally protect itself and shut down and I think what's happening there cuz this supplies the

**Dave Jones:** main 5 V rail, which powers all of the logic board, of course. So, you know, it'll just shut off the output and it'll reset like that. And of course, you can't run this thing at too hot a temperature anyway being right next to

**Dave Jones:** these two large filter caps here, even though they're 105° C rated, they're just going to die, you know, in very short order. So, there is something wrong here. Surely, this cannot be normal. So, I'm just wondering if there's anything

**Dave Jones:** that I've done in the teardown to cause increased power consumption. I mean, my supply seems to work just fine. So, I don't know. I'm I'm at a loss here. I wasn't I you know, I wasn't expecting to troubleshoot this thing. I thought I'd

**Dave Jones:** um you know, just be able to probe some waveforms and and you know, do a little bit of reverse engineering and stuff like that, but no. Now, I've got this bloody problem to contend with. What the And there's also a software bug

**Dave Jones:** in this thing which people on the forum have actually reported and confirmed, and I'll just confirm it here. What it is is if you set the current limit here below 10 milliamps, then it actually shows, even with no load, nothing

**Dave Jones:** connected at all, no trickery going on here whatsoever, um it will actually show 30 milliamps reading current. So, let's try that. Let's lower it. 14, 13, 12, 10. Here we go. Bang. Look at that. It jumps up and

**Dave Jones:** reads 30 milliamps. Crazy. Why? Unbelievable. Of course, when it goes down to zero, it's it reads zero, but anywhere from 1 to 10 to 9 milliamps, Look at that. 30. And then it just goes back to zero over

**Dave Jones:** that. Ah. What's going on there? Now, what I've done is put the lid back on here, and it well, it's not actually resetting now, presumably because it's got more airflow actually, you know, it's sucking in the air through here and out the back. So,

**Dave Jones:** we're getting some forced airflow there where we didn't have that before. It was just still in the air, and I can still get in here and and probe the uh heat sink in here and yeah, it it rises. It takes some time to get the

**Dave Jones:** correct contact on the thing, but it's still running incredibly hot. Check this out. Look at that. We're already up to 90 and remember that heat sink is right next to those caps as well. 92, 93. We're still rising.

**Dave Jones:** That's just crazy and you know, I'm not making the best contact there with the heat sink, of course, so you know, it it it is basically you know, round it to at least 100°. You got to be kidding me.

**Dave Jones:** And just to make sure I wasn't hallucinating this thing or that I there was some bizarre fault that happened in the teardown or something like that. I decided just to make sure I'd put this to the forum and I've left it overnight

**Dave Jones:** and sure enough there's a whole bunch of responses from other people. I asked if they could test their units and they have and they have absolutely 100% confirmed exactly what I'm getting. This heat sink some people are even getting

**Dave Jones:** 110° in the case like this poking their thermal couple through. Somebody showed a floor IR thermal image of the heat sink up to 130° C. Of course, to do that they have to take the case off and then there's no air

**Dave Jones:** flow and all that sort of stuff. So, you know, much higher temperatures than what you get in the case here, but it's absolutely confirmed it. The this thing the design of this Rigol DP832A is totally flawed. I have no idea how it

**Dave Jones:** even made it past the first design review meeting with a bloody 5-V sorry yeah, 5-V regulator for the main digital logic operating at a nominal around about 100° C. You got to be kidding me. You got to be me. It's

**Dave Jones:** It's one of the worst design oversights I've ever seen. It is absolutely bread and awful. This is bread and butter stuff for a power supply. One of the first things you're going to look at is the bloody thermal design of this thing.

**Dave Jones:** Verify the thermal design when you're designing this product. Unbelievable. Anyway, it definitely confirmed, but what I'm going to do is I'm just going to I've left this overnight. I haven't powered it up today, so I'm going to switch it on and see if I can get the

**Dave Jones:** heat sink through here. So, it's got the proper airflow coming out the back. Of course, the fan's on a minimum when you first start turn it on cuz it's not It's not loaded. So, potentially the heat sink could actually cool down even

**Dave Jones:** further when I ironically when the outputs are loaded because then it will turn the fan on greater at a greater speed. You'll get greater airflow over that heat sink and potentially could actually cool that heat sink down ironically. But anyway,

**Dave Jones:** I'll switch it on, see what I can get. As you can see, my ambient temperature's around about 23° C, which is, you know, a typical office ambient temperature. Now, I've only had it on for a couple of minutes and it's difficult

**Dave Jones:** to probe. I've got it going straight through there. I've actually took out some of the silastic between the the two filter capacitors there so I could actually get through and I am probing the heat sink, but you know,

**Dave Jones:** it's it's not ideal contact at all. But as you can see, I mean, you can never actually read too high on this thing. So, it's not like, you know, I can get bad contact and accidentally read high. So, I'm getting 75° C on that heat sink.

**Dave Jones:** I've got to put a bit of pressure on the thermal couple just to get, you know, I'm I'm right on the side of the heat sink. Trust me, it is That's not making good contact at all. So, I think the

**Dave Jones:** true temperature of the heat sink is greater than that, but we're up to 77 and at the moment and still climbing. 78. This is not looking good, folks. Here we go. Look at this. 91°. That is just insane, really. I mean, I

**Dave Jones:** you know, a lot of people might think, "Okay, what's the problem?" Right? But, it's all about design margin. And you saw what happened when we'll verify this again when we open it back up, but I'm sure that this is causing that 5-V reset

**Dave Jones:** problem. Now, the to run something at 90 to 100° uh to run a you know, an a 317 regulator or any heat sink at that sort of temperature for something dumb ass like a nominal, you know, 5-V rail to power

**Dave Jones:** uh you know, the digital circuitry in this thing is absolutely insane because there is no design margin in there. Um yeah, okay. Maybe this thing might work and might continue to work for most people for a couple of

**Dave Jones:** years or something until those caps dry out, of course. I hadn't not even mentioning the caps yet. Okay? Without resetting at all, right? There might just be adequate airflow in there. But, what happens if you stick this damn thing in

**Dave Jones:** a rack? You know, they I think they even sell a rack mount kit for it. If you've got uh you know, a rack can easily get 40 or 50° ambient in there, something like that. Raises Even if you raise the

**Dave Jones:** ambient temperature here in the lab by an extra 5°, that could be enough to actually reset uh to trip the thermal overload in the die in that LM317. And uh who knows what we'll check which try and check which LM317 they're using,

**Dave Jones:** but that'll vary based on batch. It'll vary They might have um you know, they might declare that they can source that from any manufacturer, so it's not going to be consistent across your entire production run of these units. All sorts

**Dave Jones:** of stuff. It's just It's just crazy. There is no way in hell that anyone could sensibly make a decision that says to run that heat sink at 90° would be a good idea for anything, let alone a production unit

**Dave Jones:** like this. It's disgusting. It's ah And I've managed to get almost 110°. Look at that, 108. Depends where I wiggle it. Disgusting. Who the hell designs 5-V regulator that runs quiescent at 109° C? What a Now, I'm going to see if I can actually

**Dave Jones:** verify that the reset problem I'm seeing on the on the unit is actually the 5-V regulator going into thermal overload and dropping out, so to speak. So, I've set up the scope. Nominally, it's There it is. We've got our 5-V output there.

**Dave Jones:** It's all pretty clean. Triggering it about 4 and 1/2 V on negative going. So, we'll just leave it there and I've got my outputs switched on, so I'll definitely be able to do uh tell when it's done that and well, let's see if it

**Dave Jones:** correlates. See if we trigger anything on the scope a drop out in that 5-V rail when this thing resets. Could take a while though. And look at the temperature that thing's running at, 141 and climbing when there's no airflow

**Dave Jones:** over it. Unbelievable. It's even got some additional little heat sinking on it due to the oscilloscope probe. Oh. And I only had to wait a minute or so and it's it has reset here, but I didn't get anything triggering on the scope

**Dave Jones:** over here. So, it looks like it didn't drop below that 4.5-V value. I mean, I you know, maybe I've got to tweak that up a bit. Maybe there's a voltage supervisor or something on the 5-V rail inside the main

**Dave Jones:** chip that or even could be a function inside the main processor or something a that's you know, is actually detecting a smaller drop out than what's there. Let me tweak it. No, it still couldn't get it to do it. I'm triggering at 4.8

**Dave Jones:** volts and the thing just reset itself, but I still couldn't detect drop in that 5 volt rail. So maybe my theory is wrong there, but jeez, I don't see what else it could be. I mean, you know, just as a rough indication as what

**Dave Jones:** temperature those caps are running that just by sitting near that heat sink it you know, 130° or whatever it is. There you go. They're almost up to 70° just the cans on there. Of course, there's no airflow it's going to help when there's

**Dave Jones:** airflow over these things of course, but that's how you can get with just you know, just the coupling over to those capacitors. Well, I'm at a loss now as to explain exactly what the mechanism is for resetting this unit. I could have

**Dave Jones:** sworn it must have been the drop out of that regulator, but I cannot seem to capture any drop out AC or DC coupled at any time base of this regulator. So I I don't know. But anyway, what I've done

**Dave Jones:** is this board it when it was sitting here before it was resetting every 1 minute or 2 minutes absolute tops with monotonous regularity. Then I just put this paste fume exhaust I've got air blowing over it like this. It's been

**Dave Jones:** probably more than I'm pretty sure it's more than what was getting inside the case and all of a sudden bam, I've left for 10 minutes and it's not resetting at all. So it definitely looks like it has something to do with that the heat of

**Dave Jones:** that regulator, but the exact mechanism still eludes me. Now I've even got to the trouble to set up a window trigger here. Oh, oh, hang on. Yeah, I just saw that. I just saw it switch off. I don't know if you saw

**Dave Jones:** there was some dip in the waveform there. There was something. There was something there. I hadn't Damn it, I hadn't had the trigger on. I was too busy shooting this video. But anyway, looks like we may have finally got it.

**Dave Jones:** Let me switch this back on. Anyway, I've set up a window trigger here so that it can trigger anything outside of that those two windows there. So, I'm going to put it into single mode again and see if I

**Dave Jones:** can capture that. I've got it back on, but let's let's see what happens. Let's just leave it running. Well, no, it's switched off and reset, but we didn't capture anything even with that tiny trigger window there. But no,

**Dave Jones:** I still couldn't get anything there. So, I've gone back to AC mode and there it is. There's our AC coupled mode 50 ms time base there and I set up a window trigger mode just around that. So, let's up. There we go. Look at

**Dave Jones:** that. Did you see that? Look at that. There we go. So, we've got some sub Yeah. Yeah. I think we're we're getting very close to getting this. Anyway, you can see that right there. Looks like that's normal, you know, in quote marks, right? That's

**Dave Jones:** normal 5 V AC coupled output. We're only at 100 mV per division there. Now, let's trigger off that and see and watch it and see what happens. See if we can trigger anything when these switch off and it resets.

**Dave Jones:** Bingo. There we go. We finally got it. Yes, it triggered. You saw it. There you go. This waveform started I don't know, maybe a second before this thing reset itself. So, there you go. My theory was right. Well, you know, it

**Dave Jones:** could not be wrong, really. It had to be that voltage regulator. In this case, just doing, you know, just some subtle drop out there. It's, as you saw, we couldn't trigger on the 5-V any significant variation on the 5-V rail

**Dave Jones:** itself, but when you get down, you know, we're only talking like 100 mV per division. So, just that sort of noise or ripple that regulator is doing something, and it's not regulating as it should anymore. It's, yeah, it's still

**Dave Jones:** regulating at 5 V, but the AC component of it has actually changed. So, that is causing something on the digital board. I don't know what. I'm not going to go into the digital board and try and, you know, dissect why, you know, it doesn't

**Dave Jones:** matter. The fact is that regulator is overheating and is causing reset on the digital board somehow. So, that's what we captured there, and whoop. That is normally. So, you can see that it was, you know, double or triple in

**Dave Jones:** amplitude before when it actually fails. And we can no doubt capture that again. It'll be fully repeatable. You watch. Bingo. Too easy. There it goes. Switched off. Barely even had to turn around for, you know, 10 seconds, and we captured it.

**Dave Jones:** Woo. So, actually, this is a really good example of a little bit of a tricky real real-world troubleshooting scenario where I had a theory, okay, this regulator is overheating, it was dropping out, causing resets on the on the processor inside this thing in

**Dave Jones:** some manner, but you know, I my theory was almost blown blown out of the water. I expected the 5-V rail to just, you know, plummet down to zero or drop down to 3 V, or I don't know, do

**Dave Jones:** something stupid and allow, you know, a couple of volts or ripple to come through or something horrible like that. And I couldn't capture it even with a tight couple hundred millivolt window triggering around the 5-V rail that I

**Dave Jones:** had there before. I couldn't do it on that 5-V scale. So, I had to switch to AC and I originally couldn't even find it on AC as well. I'd done that before, but it turns out I wasn't setting my trigger point narrow enough.

**Dave Jones:** And in this case, I switched to the window trigger. And you can see it's probably just, you know, going over that top one. So, I had to set that I had had to use window triggering to go outside

**Dave Jones:** of the normal operational window to capture a really what is quite a small variation. And most circuits would tolerate that quite well, you know, if you've got an additional 3.3-V local regulator on your rail or you're just powering some 5-V logic, it's going to

**Dave Jones:** tolerate this sort of ripple generally no problem whatsoever. But there is something subtle on the particular processor inside processing circuitry inside this Rigol that is causing that thing to reset. So, if I wasn't absolutely confident that that regulator was dropping out, then I,

**Dave Jones:** you know, I could have thought, "Okay, well, I've checked that and that's not the problem." You know, not an issue at all. It must be something else. You go away go away. You chase red herrings until the cows come

**Dave Jones:** home. But no, we nailed it because I finally got down to a point where I could trigger off something that was causing this to drop out. Now, a couple of people have already been a little bit confused by this issue. So, I'll make it

**Dave Jones:** very clear. This 5-V regulator that we're looking at here, it has absolutely nothing to do at all with powering these outputs or what load you put on the output, whether you have a load or not. It's a completely isolated

**Dave Jones:** circuit with its own tap on the transformer and its sole purpose is to power all the digital circuitry in the front here. So, that applications processor, the LCD, some of the IO stuff here at the back. That's all there is to it. You can load

**Dave Jones:** down this all the outputs to the 495 watts and the dissipation on that heatsink is going to remain exactly the same. Although, as I mentioned before, when you do load down the outputs, the firmware knows that or it's

**Dave Jones:** measuring the temperature of the main heatsink, but I can't see any thermometer on thermistor on there at all measuring the temperature of that. It does increase the flow rate of the fan. And as I said, the increased flow rate of

**Dave Jones:** the fan could actually have the effect of actually cooling down a little bit that 5-V heatsink, but it's got nothing to do at all with loading the outputs. Now, the question is how much load does this thing actually take? How much does all

**Dave Jones:** this digital stuff in here take? Well, let's have a look at it. Let's measure our power. Let's switch it on, shall we? Let me put my probe in here and we'll switch that on. Here we go. And it's powering up. It's

**Dave Jones:** powering up. It's not much at all. Aha, silly me. I figured out what's going on. Well, not silly me, silly Rigol. This connector here, which obviously carrying all of that 5-V over to the board, they've actually got the colors of the wires back to front. I

**Dave Jones:** assumed, huh, silly me, that the positive wire would actually be positive. It's not. It's actually negative relative to that regulator. So, ah, now I've pulled out the black wire there because the reason why we're only measuring like, you know,

**Dave Jones:** 20-30 milliamps before is because this ribbon cable here was taking that return current. So, here we go. Now, we should be able to get it. Measure the actual current. Here we go. If we break into the positive wire here, which is actually

**Dave Jones:** black. Bingo, there we go. We're getting 300 it's booting now. Probably can't see the screen. There we go, it's just booted up. There we go. And now after it's booted, we're getting, you know, let's call it say 700 milliamps,

**Dave Jones:** something like that. Let's switch the outputs on. Doesn't make any difference, of course, but yeah, you know, it's jumping around as you'd expect, but let's call that 700 milliamps. And the input voltage, about 11.8 volts, which will of course vary with the line

**Dave Jones:** voltage because it is bridge rectified with just some filter caps coming from the transformer. So, you know, that could vary, but let's just call it 12 volts. Now, if we're getting 12 volts in and 5 volts out, well, we've got a delta or a voltage

**Dave Jones:** drop across this regulator of 7 volts. And because it's a linear regulator, it's got to drop seven the power is going to be 7 volts times the current flowing through it, which is of course the output current, which is

**Dave Jones:** .7 amps. 7 volts times .7 amps, 4.9, let's round it to 5 watts. This thing is dissipating five freaking watts. Now, anyone with any electronics design experience knows that no way in hell you're going to use a heat sink of that

**Dave Jones:** size for 5 watts, even if you've got a fairly high air flow. Uh you know, go going through your design and good thermal management. It's just ridiculous. 5 watts? Did no one even stick their bloody finger on this or

**Dave Jones:** even think about it? I'm flipping the finger, that's for sure. Let's just go to a representative heat sink. You haven't wasn't able to find the exact one, but this is going to be fairly close. It's an Avid Thermalloy

**Dave Jones:** 1 TO-220 free free sink. well it's actually a PCB mount one. It's got a PCB mount tab. This one looks to have two PCB mount tabs. So um I'm not sure if there's any heat sink on the copper at

**Dave Jones:** the bottom side of this board. I haven't taken it out but anyway, we're going to be easily able to get some ball park stuff here. And if we have a look at it uh let's go in here. It's talk we're

**Dave Jones:** talking 24.4° uh C thermal resistance there uh per watt but this is what we're interested in down here. Let's have a look at the graph, shall we? And what we've got here is well we don't need to really worry

**Dave Jones:** about the thermal resistance. What we're talking about here because this is um power dissipated. We know we're dissipating 5 watts. Look, it's for heat sink of this size it's off the graph already. That should be ringing alarm bells, right? And this is the mounting

**Dave Jones:** surface temperature rise from 0 to 100° C above ambient and that's the key of course. And what were we measuring on this thing? Well with no air flow, you know, we were getting basically um you know, 100 you know, well over 100 130 or

**Dave Jones:** something like that. And this is the ball park that we're operating up here at 5 watts with this size heat sink. I mean it's going to be very similar. We're just talking ball park calculations here. We're looking at 100°

**Dave Jones:** C rise above ambient and that's exactly what we're getting. It's ridiculous. I could go into there, you know, draw the thermal uh graph of all the things in there and the heat sink compound and the bloody you know, everything the junction

**Dave Jones:** case and all that. And imagine what the if this is what the heat sink temperature is at, imagine what the junction's at. Well, we actually don't even need to guess what the junction's getting at because let's look at the

**Dave Jones:** data sheet for the LM 317. Just take a typical one from Fairchild for example. Let's go down here. Let's get the thermal characteristics. Well, here it is. Um, there we go. Thermal resistance junction to case. We already know that

**Dave Jones:** but let's assume that there's no loss between the case and the heat sink, right? Let's assume that it that's just fine. Well, the case, there it is. 5° C per watt. We're trying to dissipate 5 W in this thing. The junction is going to

**Dave Jones:** be 25° C at least above that's above the already measured and quantified uh temperature on that heat sink which even in the case with the proper air flow and everything else is over 100° C. You got to be kidding me.

**Dave Jones:** Ah, facepalm. Hang on, double facepalm. Well, enough of that fiasco. I may as well um do a little bit of poking around of what I originally did before I bloody discovered this ridiculous issue. Anyway, I was just going to have a look at the a little

**Dave Jones:** just a little bit at the output circuitry here and see exactly what we've got and it is very easy. You've probably already guessed it but I've drawn a simple Dave card here and this is basically what we've got on the

**Dave Jones:** output. We've got the 1000 mic output uh filter cap right on the front panel terminals as you saw. I haven't shown the sense wires going back out. They're obviously going back to a sense amp but yeah, there's nothing in this

**Dave Jones:** at all really. There's no output relay switching of course or any sort of electronic Well, there's electronic switching but it's done by the series pass MOSFET that we've got in here but we've basically got a big Schottky diode in there. There we go.

**Dave Jones:** We've got some Schottky diode protection across the output as you typically find. Then we've got a couple of MOVs here going to mains earth here. And remember, this output is not mains earth reference. It's actually floating. So, these things are going to

**Dave Jones:** uh chassis earth ground. And then, we've got a another couple of MOVs on our high side current sense resistor here. So, there's our high side current sense resistor. We saw that uh close up. The traces go off there to There's our high

**Dave Jones:** side current amp. They've rubbed the number off that, the bastards. But, and of course, the output of uh that will be tied into the constant current uh circuitry, which then controls the gate. So, that'll all be uh analog loop stuff

**Dave Jones:** going on in there. And then, we've got a bleeder resistor across here. That's that one down in there. There we go. It's a fairly uh large one. And then, we've got another bleeder resistor across the um filter caps. There our

**Dave Jones:** main three filter caps up here. There they all are. Boom boom boom. Uh they're 2,200 mic each. Uh 63 V. And we'll measure some uh We'll get the scope out, and we'll actually measure some things on here and have a look at the gate

**Dave Jones:** waveform there. But, uh and basically, the input here um as I mentioned in the uh teardown, that they actually Well, I mentioned that there were triacs in there, but I didn't mention that they're actually switching the secondary uh taps

**Dave Jones:** on the transformer here. The transformer taps coming in here. And there are two triacs in there. There are two triac uh drivers down in there as we saw in the teardown. But, that's what they're using instead of uh more traditional relays uh

**Dave Jones:** to select the secondary taps because uh yeah, because this is a linear supply, you want to you need uh some sort of tap on there. Imagine you're delivering only 3.3 V out of here, and you're getting, you know,

**Dave Jones:** 40 V out of your uh transformer. That's a lot of power to dissipate in your uh linear regulator like that. In your part series pass transistor to it's called. So, really, you want to choose the uh they've got a couple of selections on

**Dave Jones:** those uh taps there. So, that's basically um what they're doing. There's nothing in here at all. There's no output relay switching to switch when you press that on-off button on the front, all it's doing is just effectively grounding that gate and

**Dave Jones:** pulling the output down to zero. So, it's not actually isolating the um output at all. It's just switching off the output series pass transistor. So, we'll just see where those uh voltage taps actually occur. You can see I've

**Dave Jones:** got the full uh 31 V output voltage. I'm measuring the uh voltage and also looking at the waveform. Uh so, this is identical to that. You can see the voltage down there, 54. Um we're getting Yeah, basically uh 54 V

**Dave Jones:** out of those uh filter caps with 31 V output voltage. Now, I'll lower my uh voltage in 1 V uh output voltage in 1 V increments and see where the tap drops. And of course, in that you'd normally

**Dave Jones:** hear a relay clicking in a regular uh power supply, but this one uses a triac switching. And bingo, there it goes. It looks like it when it goes from 20 21 from 22. Once we get down to 21, it

**Dave Jones:** drops down to 35 V. So, we're getting, you know, a 15 V um uh delta there. So, it's got to dissipate uh 15 V uh best case there. 14 13 12 11 10. There we go. We've got to drop down

**Dave Jones:** to 10 V and then we drop down to our next tap, which is seven about 17 and 1/2 V. So, there you go. And they will be the two taps. We won't find any more than that because we've only got uh two triacs

**Dave Jones:** on these things. And as we saw in the teardown, there is only a single uh TO-220 uh MOSFET in there. And you know, a lot of people are probably going to argue, "Well, you know, they're 90 W is this

**Dave Jones:** particular channel." This is one of the uh 30 V uh 3 amp channel. So, 90 watts dissipation. Is this enough heat sink and air flow? I don't know. You can try and get the data sheet and stuff like

**Dave Jones:** that. But, what we should probably do is measure the temperature on that heat sink at a full 90 watt load and see what it gets to. Yeah, you know, some designs would actually parallel up the MOSFETs there just to so you're not actually

**Dave Jones:** stressing just the one individual MOSFET. You're spreading the power against a couple of them. But, Rigol, well, now I'm doubting their design decisions after that ridiculous LM317 fiasco. But, anyway, they've Assuming they've done it right, they've determined that, "Well, no, we can get

**Dave Jones:** away with a single MOSFET on there." So, anyway, let's let let load it down and see if we can measure temperature on this thing somehow. But, yeah, there's no real easy way for me to stick my thermocouple on that and get a really

**Dave Jones:** good connection, I'm afraid. And just as we saw in the review, it can't actually deliver the full 90 watts on that channel. But, I was able to just, you know, shut the voltage down. I was able to get, you know, 85. It can do a couple

**Dave Jones:** of watts more than that. But, let's just That'll do. 85 watts output. So, I'm drawing 85 watts. I've got the lid kind of sort of closed. So, we're getting an extra air flow over the top instead of through here. But, it's going to be, you

**Dave Jones:** know, it's going to be reasonably close. And I am probing the main filter cap as well. And as you can see there, we got 10 volts per division. 10, 20, 30, 40. So, you know, 46 volts minimum. Plenty of margin in

**Dave Jones:** there for the ripple. And some initial probing of the heat sink there, it's at least to 45 degrees. So, you know, as I said, it is quite difficult. I'm not going to get in there and actually, you know, I can't really probe the

**Dave Jones:** MOSFET itself. It's getting up there, but I wouldn't call that particularly hot. And of course, the you probably can't hear it, but the fan actually has turned on louder. And we have been able to hit 70 there, so

**Dave Jones:** there you go. I don't know. You know, I'm not going to go into the full thermal calculations, but that you know, that's not too bad. That's what you'd expect really, you know, that's a ballpark of what you'd expect for a full

**Dave Jones:** load on this thing. So, you know, not a problem. And I just took that back out and with no air flow, there you go, it's jumped up to 84. It's a bit hot, but you know, there's no air flow, so you'd

**Dave Jones:** expect it. Okay, I'll have a quick probe of the gate of the series pass MOSFET there. And as I said, that actually controls switches the output off and on and we'll actually see that here. What I've got dual channels here. Channel

**Dave Jones:** one, which is the yellow waveform, is the gate voltage there where it 5 volts per division on both channels. So, 5 10 15 20 25 30 30 volts output by the way, set 30 volts there. The output is actually switched on at the

**Dave Jones:** moment and as you can see, if you switch it off, up, run it. There we go. We can see our output and channel two is our output waveform. So, our output voltage. So, we're smack on 30 volts there. And if we

**Dave Jones:** just single shot capture that, bang, there we go. We can see the rise there. It's got some little something happening down there. I'm not sure what, but anyway, that's still there's no overshoot on that output at all. It's ramping up. The output ramps

**Dave Jones:** up to 30 volts and of course, directly controlled from the gate voltage. So, if you actually bring that up, you'll find that those two waveforms are virtually perfectly superimposed there because there's you know, there's nothing else switching the

**Dave Jones:** output. It's just that actual gate series pass transistor via the gate there. And I'm afraid I'm no real closer to that uh, turn on uh, glitch when you actually power the thing on. So, I don't know. That was the aim of this when I

**Dave Jones:** started this uh, yesterday was maybe to get down into that detail, but who cares now? I mean, we've got that show stopper which is the bloody LM317. And here's another thing, the LM317 they're using, check out the ridiculously thin tab on that. That is

**Dave Jones:** just well, that is really piss ant thin tab ones. Absolutely horrible. And you can see the difference on these two devices over here. Whereas this has got like a normal thickness tab on it. That's what a, you know, a proper

**Dave Jones:** well-designed TO220. These ones are little piss ant thin tabs on them. Look hopeless. So, that LM317, I mean, you've just got less thermal mass right there. And for the record, that looks to be an ST brand 301 LM317T.

**Dave Jones:** And when I check the data sheet for the ST brand LM317, and just like all the others, you know, maximum junction operating temperature is, you know, around about that 125° C mark. And we found we've, you know, proven by

**Dave Jones:** measurement and based on the data sheet values, the junction to case and that sort of stuff that they're operating above that. They're operating above the recommended junction temperature. It's just It's just complete fail right there. So, there's something I wasn't expecting when I

**Dave Jones:** started probing this thing yesterday. I noticed an issue where it would reset. I tracked it down to a bloody overheating piss poor designed 5-V regulator for the main logic. Can you believe it? Bloody ridiculous. I'm pissed off. This

**Dave Jones:** is a huge serious design oversight. No one in their right mind would deliberately design a little LM317 with that piss ant heating to run at five bloody watts and think that you can get away with it right next to the output

**Dave Jones:** filter caps. These power supplies are going to fail in the field, no doubt about it. Probably even see the resetting feature I had or in a couple of years time those caps are going to dry out. It's just absolutely shocking

**Dave Jones:** how this thing even made it past the bloody design review meeting, let alone into production, let alone into people's hands. How many months has this thing been on uh sale for now? And well, yeah, okay, nobody's found it. Okay, maybe a

**Dave Jones:** few units, I don't know, it might have experienced issues that that we haven't heard of, but this is a huge, very serious design oversight and Rigol need to explain what the hell happened here. And I don't think they can explain this

**Dave Jones:** away. How? Like, you know, apart from we missed it or we swept it under the somebody found it and they'll told to "Oh, it's not a problem. Shut up. Go back to your bench." you know? And it's ridiculous. A hundred plus degrees C on

**Dave Jones:** a on a you know, on a regulator? And it's just quiescent static current driving the thing as measured by multiple people through the case with the proper airflow. Yeah, they'll probably do like a firmware upgrade. Oh, we can fix that firmware upgrade. Make

**Dave Jones:** the fan run all the time. God, man, unbelievable. And there's probably going to be some people who will say, "Well, what's the problem, right? Nobody's had an I Look, it just reset it again." Oh, bloody hell. Uh people are going to

**Dave Jones:** a few people say, "Oh, you know, Rigol might even say, 'Oh, had no problems in the field, no returned units.'" That's beside the point. The point is is that this is has no design margin in it whatsoever. You mount this thing in a

**Dave Jones:** bloody rack, right? Sits in a rack, your ambient goes up by 20 or 30 degrees Celsius, you're just going to be screwed. Those regulators are going to shut down. You you know, who knows what regulator, what the thermal cutout is in

**Dave Jones:** that particular type of regulator. You got variations in your junction to case. I don't even think Yeah, they put some heat sink in there. There's going to be variations in that. There's going to be variations in the airflow on the fan.

**Dave Jones:** Huge variations. Going to be variations in the life of those caps and all sorts of stuff. It's just it It's just bad engineering. It's not going to work. Needs to be fixed. Anyway, Rygo, explain because this power supply now gets a huge thumbs down until

**Dave Jones:** this problem is fixed. I think it needs to be fixed before you sell any more of these bloody things. Unbelievable. What can you do? Well, you know, it's tempting to sort of move that 5-V reg over to you know, an existing heat sink on here,

**Dave Jones:** but then you break your isolation stuff between your isolated 5-V power to digital and your output. So, that's not really going to work. Might You've got There's a couple of mounting holes in there. They probably could solve it by

**Dave Jones:** manufacturing some sort of custom heat sink or something which goes in there. And yeah, that'll probably be a fix. Maybe, you know, that Well, it probably would be a half reasonable fix if they up the size of that heat sink by you

**Dave Jones:** know, four or five times or something like that. But, it definitely involves something custom. Other than that, it probably have to relay out the board or something like that. This is clearly unacceptable. Anyway, let's see. I'll definitely let

**Dave Jones:** Rygo know about this and let's see we hear back from him cuz this is just complete utter Catch you next time.
