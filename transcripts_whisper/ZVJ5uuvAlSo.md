---
video_id: ZVJ5uuvAlSo
title: EEVblog #324 - DC-DC Converter Testing - USB Supply Part 4
url: https://www.youtube.com/watch?v=ZVJ5uuvAlSo
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 17, "2": 37, "3": 57, "4": 73, "5": 90, "6": 110, "7": 126, "8": 150, "9": 170, "10": 190, "11": 215, "12": 235, "13": 251, "14": 275, "15": 295, "16": 319, "17": 336, "18": 356, "19": 372, "20": 388, "21": 404, "22": 420, "23": 436, "24": 457, "25": 477, "26": 497, "27": 518, "28": 538, "29": 554, "30": 574, "31": 594, "32": 614, "33": 635, "34": 655, "35": 671, "36": 691, "37": 711, "38": 735, "39": 759, "40": 784, "41": 804, "42": 824, "43": 844, "44": 868, "45": 884, "46": 900, "47": 921, "48": 937, "49": 957, "50": 973, "51": 1001, "52": 1022, "53": 1042, "54": 1062, "55": 1083, "56": 1111, "57": 1127, "58": 1155, "59": 1171, "60": 1192, "61": 1208, "62": 1228, "63": 1248, "64": 1264, "65": 1284, "66": 1304, "67": 1320, "68": 1337, "69": 1357, "70": 1377, "71": 1401, "72": 1421, "73": 1441, "74": 1466, "75": 1490, "76": 1510, "77": 1522, "78": 1538, "79": 1558, "80": 1578, "81": 1603, "82": 1623, "83": 1651, "84": 1671, "85": 1691, "86": 1712, "87": 1736, "88": 1764, "89": 1784, "90": 1804, "91": 1821, "92": 1841, "93": 1857, "94": 1881, "95": 1897, "96": 1917, "97": 1938, "98": 1958, "99": 1982, "100": 2006, "101": 2035, "102": 2059, "103": 2084, "104": 2104, "105": 2120, "106": 2144, "107": 2164, "108": 2185, "109": 2205, "110": 2225, "111": 2245, "112": 2269, "113": 2289, "114": 2309, "115": 2330, "116": 2346, "117": 2370, "118": 2390, "119": 2418}
---

**Dave Jones:** Hi, welcome to another video in the USB power supply design series. And I'm just going to do some measurements on this little 2 watt DC to DC converter. You've seen these before, it's one of these single inline package types. 5 volts in over here, 5 volts out.

**Dave Jones:** You can get ones with extra pins that have like a split supply as well, but I'm using 5 volts in, 5 volts out, and this one's 1000 volts isolation between input and output. You can get higher, and we'll go into some detail on

**Dave Jones:** why, hopefully, why that might be important. Now this is a Sengme brand, Sengme, however you want to pronounce it, brand. And I'd love to pull one apart, but they're fully potted. You can see the potting compound in there. It's effectively just a plastic, you know,

**Dave Jones:** outer box, a plastic potting box, which they've silkscreened, and then they put the circuitry on there, on a little circuit board of course, and then they gunk the whole thing up. But I might try and maybe open one, but yeah, it's just going to be completely gunked.

**Dave Jones:** I'd have to use some chemicals to de-gunk the thing to show you what's inside. Anyway, they're a dime a dozen. Industry standard footprints, this is one of the industry standard footprints available in the single in-line package one, but there's many different types available under many different brands.

**Dave Jones:** Sengme is just one of, you know, dozens and dozens, countless DC to DC converter manufacturers. This is a little 2 watt one, and 2 watts is specified at the output, and we'll look at the efficiency. I'm going to compare it with the data sheet, check minimum

**Dave Jones:** loads and efficiency and stuff like that. Might be a long video, so hang in there. And if we have a look at the data sheet for it here, there's not a huge amount of info. There are some specs, there's some typical output characteristics, but there's no

**Dave Jones:** info in terms of minimum output capacitance or anything like that. So anyway, we're going to give this a try. And this is a 1 kilovolt one, as you can see it's 2 watts output power capability, and it says it's an unregulated output, so it's not, you know, it doesn't have like a linear regulator

**Dave Jones:** output. It's 1000 volts isolation. It says 1000 slash 3000, but I'm pretty sure this is the 1000 volt isolation version. I think there's another version you can get which is 3000 volts isolation. And up to 80% efficiency. That's fairly typical of these little modules.

**Dave Jones:** Unfortunately, you know, you're not going to get one, or you know, you're going to pay a lot more if you want one that's optimized for a specific load and, you know, gets over 90%. But 80% is pretty typical. We'll test that. Working temperature range, minus 40 to plus 85.

**Dave Jones:** MTBF, which is the mean time between failures, is 350,000 hours. And if you do the math on that, that's like 14,500 days or 40 years or thereabouts. So go figure. It's got 15% load regulation here for a, I presume that's a load range of

**Dave Jones:** 10% to 100%. And we've got some ripple and noise figures here, less than 75 millivolts. These things aren't particularly quiet. If you want to make them quiet, you've got to put like a ferrite bead on the output as well as a linear voltage regulator too if you really want to bang that

**Dave Jones:** noise down. So we got down here, we got the 5 volt version here. It's 4.5 minimum volts input. We'll check that. Because if you're powering one of these things from USB, you can actually get less than 4.5 due to the drop of the cable and stuff like that.

**Dave Jones:** So maximum USB current, 500 milliamps. And it says 40 milliamps minimum load on this sucker, so I'm very curious to try that out and whether or not it works with no load. I'm pretty darn sure it does. And a maximum output of course of 400 milliamps

**Dave Jones:** at 5 volts. There's your 2 watts. So actually this is perfectly rated for a USB application. You might think, oh, you need 500 milliamps output. Uh-huh. No, it's not going to do you any good because remember that 80% efficiency figure up there. So let's assume that you can

**Dave Jones:** actually get 80% efficiency from this thing. Your USB can only in theory provide a maximum of 500 milliamps. So 500 milliamps into the DC to DC converter with 80% efficiency means you're only going to get out 400 milliamps. So it's absolutely perfect. So you

**Dave Jones:** actually need an 80% 2 watt DC to DC converter for a nominal 2.5 watt USB port. And it doesn't tell you anything about short circuit protection, under voltage, lockout, and stuff like that. So these are the sorts of things that we'll have to check.

**Dave Jones:** There are two more pages to the data sheets, but it's just pinouts and physical descriptions. And here's the setup. Nothing fancy, just got it on a breadboard here at the moment. I've got no output capacitance. I've got 2 meters here, this is my input voltage, and this is my

**Dave Jones:** input current coming from my bench power supply. I've got my trusty BK Precision 8500. Electronic load, so this I don't need extra multimeters. You know how I've often used 4 meters to do this DC to DC converter stuff? Well this one measures the voltage, current,

**Dave Jones:** and allows us to do the power and stuff like that as well. And it's just as precise as a Fluke 87 basically. So that's going to work a treat for measuring the output voltage and current. And I've got a couple of probes that allow us to probe

**Dave Jones:** the output on the scope up here. One set to DC and one set to AC. So let's go. Alright, now what we're looking at here I've got channel 1, which is the yellow waveform at the top, that's set to DC. So we can see our DC level at 1 volts per division

**Dave Jones:** there. So we're getting our 1, 2, 3, 4, 5, it's around about 6 volts there. It's actually 5.87 according to the BK Precision there. And channel 2, the green waveform here I've set up exactly the same, measuring the same point, but it's AC coupled.

**Dave Jones:** So it allows us to see the DC level the same time as AC. Would have been nice if the scope could do that on one probe, but it can't. So we've got the AC coupled waveform here at 200 millivolts per division, and you can see

**Dave Jones:** and I'm measuring the frequency of that, you can see the automated cursors there jumping around. We've got a 50, very large amount of 50 hertz. And by the way, this is with no load. So the data sheet sort of implies that it needs like a 40 milliamp load minimum

**Dave Jones:** on the output. So this has no load and no output capacitance except for the input of the BK Precision. But that 50 hertz, wow! That's a, I really did not expect that at all. Now I have a sneaking suspicion that the electronic load is causing

**Dave Jones:** that, so let's disconnect. Hey, yep, there we go! We just get our switching noise. So just the fact of having that electronic load on there means we get that 50 hertz hum. Look at that. And by the way, you can probably see this

**Dave Jones:** waveform jump around occasionally. There we go. The that implies that you can see the switching noise on the waveform there, and that means that the trigger is sometimes switching, sometimes triggering on that noise on there. So that's why you're getting the waveform jumping around like that.

**Dave Jones:** So if you've ever got like a waveform that's not a noisy waveform like that, and you can't trigger off, well go into the trigger, the mode coupling menu, and there's various options noise, noise reject. If we, hang on, I need it to jump around for me consistently.

**Dave Jones:** But anyway, if you hit noise reject, that will reject the noise in the triggering system of the scope, and we should never see that jump around again hopefully. And if you really want to, you can switch in HF rejection as well, high frequency rejection too.

**Dave Jones:** But that should do the business. Just as a quick little test here, I'm going to leave my ground probes floating, I'm not going to connect those, and I'm going to use a poor man's, turn my scope into a poor man's differential probe here by connecting, by using

**Dave Jones:** two channels, and before we had the ground hooked up to the negative output, and we were probing the same channel twice. But now I'm using two different channels to, via the high impedance of the probe of course, that's important, to probe differentially the output ground and

**Dave Jones:** 5 volts. And I can do that up on the scope here by going into the math menu and subtracting channel 1 from channel 2. And you can do this on old analog scopes as well, but it also works on digital. So I end up with the white math waveform, which

**Dave Jones:** is channel 2 minus channel 1, which is effectively a differential probe. It's a poor man's differential probe because the common mode rejection ratio is pretty terrible with these probes, it has to do with the matching of the input impedances and stuff and it's, you know, it's, it's, but it works as a

**Dave Jones:** poor man's differential probe and we still get that 50 hertz there. So there you go, that's showing that it's, it wasn't the ground connections on our probe causing that. And the other thing, when you're probing DC to DC converters like this, and, you know, I've got a 500 megahertz

**Dave Jones:** scope here, you really don't want the full system bandwidth of this thing, so you really want, you know, you can see the huge amount of switching noise in there, and so, you know, if you really want to clean that up, because of the massive bandwidth of the scope,

**Dave Jones:** often you want to put on the 20 megahertz limit. And that comes into its own when you do the measurements, because you can see the output ripple and noise is specified as less than 75 millivolts peak-to-peak over a 20 megahertz bandwidth range. So turning on the full bandwidth of your

**Dave Jones:** 500 megahertz scope, or your 100 megahertz scope, and then complaining that the ripples are larger than claimed, well, you're making a mistake. So, you know, really, you want to turn on that bandwidth limit, which in this case is 20 megahertz. And the reason it's 20 megahertz is because to match the old traditional

**Dave Jones:** analog scopes, which for a long time, your entry-level analog scope was 20 megahertz. Now I suspect that if we wind up our load here, our 50 hertz is going to completely vanish. And, yep, as we go up the 50 hertz, let's take it to, say, that 40

**Dave Jones:** milliamps, you know, minimum. We're still, you know, it's still got some crap there, but let's see if a pure resistive load makes any difference. And, yep, that's with a pure resistive load there. And of course, and we're getting no 50 hertz at all.

**Dave Jones:** And that's with the resistive load, tiny little resistive load down in there, and disconnected from our electronic load. Now, here's an absolute classic example of burden voltage on the current range of a multimeter at work here. We've got 5 volts input voltage. That's

**Dave Jones:** measured, by the way, right at these two alligator clips there, right at the input terminals to the voltage regulator. So, obviously the voltage at our power supply up here will be higher because of the voltage drop. There'll be some slight voltage drop in the

**Dave Jones:** cable, but let's take a look at this. We're at 40 milliamps at the moment, and I'm going to turn up this output load and watch this input voltage here drop. Let's go up to a couple hundred milliamps, right? So, let's go, say, 200 milliamps output current,

**Dave Jones:** okay? Look at where we're at with this input voltage is 4 1⁄2 volts. That's right on the minimum input of what the data sheet claims for this DC to DC converter. And the output voltage of the DC to DC converter has dropped as well because it's not fully

**Dave Jones:** regulated converter. So, and we've got 260 milliamps input current. And you might think, aha! The voltage is being dropped by the leads coming from here. But no! Aha! Watch this. Ready? I will change, it's the burden voltage of the milliamp jack here, I'll turn it

**Dave Jones:** over to amps, bingo! We've got our same current, but look! The voltage has jumped right back up to 5 volts. There is no drop in these leads, or very little. It was all inside the burden voltage of that multimeter. What a bastard! Trap for young players.

**Dave Jones:** There's two ways around it, either to use my microcurrent if you really want to do this, then you have to be, if you really want, but you see with the 10 amp over here, okay, our resolution has dropped. So if you want to keep that resolution, okay, it's dropped

**Dave Jones:** to 4 1⁄2 volts. There it is. You have to compensate for the drop, the burden voltage, the drop of voltage in this meter by turning up your input voltage back to 5 volts. So as you increase this current here, you've got to increase your, you've got to adjust your power supply at the same time

**Dave Jones:** to track and compensate for the drop in there. And you'll notice if I switch it over to amps, now there's practically no burden voltage on the amp range, we're at 5 1⁄2 volts. Ah! Burden voltage. Trap for young players. Beware. But there are ways

**Dave Jones:** around it. Now as for this 50 hertz issue with this electronic load, it is rather puzzling. If I switch the amp, if I disconnect it, of course, it vanishes. Right? And if I switch it off via there, it vanishes. And, you know, there's hardly

**Dave Jones:** any load. It's like, you know, 1 milliamp load there, if anything. It's practically turned down to zero, but it really starts injecting that massive amounts, we're talking 200 millivolts per division there, so we're talking half a volt of 50 hertz hum into our measurement system here.

**Dave Jones:** Now unfortunately I'm not able to get rid of that, so that's just inherent in our test setup with this electronic load. It's basically picking up 50 hertz from inside the supply and then it's coupling that back into the DC to DC converter at low

**Dave Jones:** currents. Because of course, once you go up in current, it just vanishes. Even if you go up in a couple of milliamps there, and then it eventually just vanishes into the usual background noise. So that's our DC to DC converter causing the issue here, because it's only when measuring the

**Dave Jones:** output of the DC to DC converter, and even if I bridge the isolation in there, it makes absolutely no difference at all. So this is shorting the primary and secondary of our DC to DC converter, and the high frequency noise has dropped, but the 50 hertz remains

**Dave Jones:** and at the exact same scenario. So that's a minimum load thing on the DC to DC converter, causing that issue combined with our electronic load. Because if I disconnect the load and put just a resistive load on the output, of course it vanishes.

**Dave Jones:** So we're just going to have to put up with that for the time being, but it won't affect our measurements. Now there's something I hinted at there while I was shorting out the primary and secondary. The noise, the switching noise, vanished. And the reason we're getting switching

**Dave Jones:** noise, it's universal with these DC to DC converters. And what's causing it is the capacitance between the primary and the secondary of the transformer inside this DC to DC converter, because it's an isolated transformer and the capacitance of this thing will basically determine how much switching noise

**Dave Jones:** is going to be coupled into your system. Now I said that this is a 1 kilovolt converter. You'll find that the higher voltage DC to DC converters here, i.e. if we use the 3 kilovolt version, or you can get 5 and 7 kilovolt versions of these

**Dave Jones:** type of switching regulators, the higher that isolation voltage, the lower your switching noise is going to be caused by your primary and secondary capacitance. Why? Because the greater isolation voltage means greater physical separation between the primary and secondary, and therefore lower capacitance. So how do we, so A,

**Dave Jones:** if you want to lower it, you can simply use a higher voltage rated DC to DC converter, but then they're bigger, more expensive. So, the way to fix it is to use a high voltage suppression cap. And you can buy caps for just this purpose.

**Dave Jones:** And here we go, we've got a 3 kilovolt 102 there, which means it's 1 nanofarad. Now if you have a look at the switching noise here, it's really high frequency stuff. And really, if you've got your bandwidth limit, if your scope turned on here, then you're pretty much fooling yourself in terms

**Dave Jones:** of the level of the actual switching noise. So if you switch that off, you can see that the massive high frequency stuff, you know, we're talking 70 odd megahertz, 70 plus megahertz here. So that gives us a value of what, you know, there's

**Dave Jones:** roughly, you know, 3 divisions there or thereabouts. So we're talking 600 millivolts peak to peak. But the issue is, look down here, I mean, we've got these horrible antenna ground leads all over the place. Horrible, look at the inductance of these things. So what we need to do is

**Dave Jones:** probe this sucker properly. And by that, I mean you want to get rid of this antenna ground lead here, and this tip and get what should have come in the packet with your probe, one of these little low inductance probing points. So look at the tiny amount of inductance there

**Dave Jones:** compared to this huge lead here plus the tip. I mean, no contest. And I know, everyone will mention it, yeah, this is crap, right? I'm trying to do this on a breadboard. It's, you know, it's going to be horrible to begin with. But

**Dave Jones:** we'll be able to see the difference. What did we get? 600 millivolts odd last time? So let's try and, the good thing about this is that it is thin enough to actually stick down into, sorry you can't see that, but I'm pushing that down into the

**Dave Jones:** probe point down into the breadboard there, and bingo! Look what we have. Same volts per division, 200 millivolts per division, but much, much smaller amplitude, and that's what's really there. So we're only talking now, you know, 200 millivolts or so, high frequency noise on there.

**Dave Jones:** And of course this thing's going to jump up and down like a jackrabbit, you know, I can fart halfway across the room and this thing's going to change around. But there you go, that is at least the proper way to attempt to probe such a thing.

**Dave Jones:** But I think I've digressed a fair bit, I don't really, I'm not here to measure the switching transient and trying to fix that and do it on a breadboard and all that sort of crap, I don't really care. I more care about the efficiency of this

**Dave Jones:** thing and its load performance and stuff like that. Right, so one of the first things I've noticed is that it essentially doesn't need any output capacitance on this thing. I mean, I've got no output capacitance at all, and we're driving, you know, let's take up the load to

**Dave Jones:** let's really bump up the load here. Quite significant output, let's go to its maximum actually. Ta-da! I love this electronic load. It's great, and we're still getting 4.93, that's with no output capacitance at all, input voltage of 4.9 volts, there it is. I've just got a little bypass

**Dave Jones:** cap on the input there, but no output capacitance at all, and if I add a 0.47 so half a microfarad, and you know, really there's nothing there, it doesn't affect the ripple or noise performance of this thing at all, it makes absolutely no difference, I'm not showing the scope

**Dave Jones:** screen there, but trust me, and makes absolutely no difference to the output, so there's no stability issues. Let's try a 47 microfarad electro, once again makes no difference to the switching noise of the output ripple, it's still all nice and stable over basically any

**Dave Jones:** capacitive load on the output. Excellent! And of course it's not very well regulated in terms of input-to-output regulation, and it tells you that. So let's wind up our input, and you see the output basically corresponds to the input, that's basically what it's doing.

**Dave Jones:** Almost precisely, actually. And it's supposed to work down to 4.5 volts, so let's see where it kills itself at its maximum output current of 400 milliamps, so we're down to 4.5. You could easily get that on a USB, if you had a big voltage drop, and it's working

**Dave Jones:** it's still working down to still working down to 4 volts input, and we're getting 3.8, so it seems to, it's diverging a bit more there, but really it's still working a treat at full load. No problems at all, wow! You'll see as I adjust

**Dave Jones:** the, actually, I'll probably put it up here, you can see the, you'll be able to see the frequency change, or turn that input voltage back up. Actually the scope's rather annoying here in that it's, in automated frequency measurement mode, it's tracking that individual, you know, it's tracking that high frequency

**Dave Jones:** stuff in there, because it's got such a deep memory, that when it samples, you know, it's got all that high frequency content in memory, and even when you go right, there we go, it's just jumped out, now we can see the switching frequency

**Dave Jones:** of the regulator, so to avoid that, a little trick you can do is just offset your waveform a bit, because it's right smack in the center now, if you center it, just offset it a bit from that center, and bingo, it'll find the peaks

**Dave Jones:** elsewhere in the waveform, and now it will track that. So we're looking at 160 odd kilohertz there, so for the switching frequency, now let's drop let's drop the input voltage here, we should be able to get all the displays on the screen there, yep, okay,

**Dave Jones:** that's it, drop our input, that's at 5 volts input, it's got 160 kilohertz, and as it goes down, we're going to have to switch that down, 4 volts, sorry, decreasing, oops, it's now, it's jumping all over the shop there, it doesn't like that,

**Dave Jones:** and it's decreasing, but interestingly, it really does continue to work at, look, we're talking 2, you know, 2 volts input, and it's still going at full output current, this is really a nice little DC to DC converter, works much further over the range

**Dave Jones:** than, way, there we go, and to start back up, we've got a we've got to hit a minimum threshold voltage output voltage has died, so there we go, it really did not like that, I had to cycle the cycle the load on the output here, and

**Dave Jones:** but it can certainly survive under voltage dropouts way below that 4 .5 volt datasheet rating, so that's brilliant, I like that, and we're still it looks like it's getting better than 80% efficiency here, because we're not at 500 milliamps for our input current, so let's do that, let's get a graph of the efficiency

**Dave Jones:** of this thing with output current. So what I want to do now is get a plot of the efficiency versus different output power levels, so what I'm going to do is use constant power mode here, which as you can see the little CW symbol on there, and

**Dave Jones:** basically that will keep a value of, well I'm going to start out, you know, in various increments all the way up from basically 0 to 2 watt, and I'll keep the input voltage the same at 5 volts all the way through, and we'll get, you know, a dozen or two dozen data points

**Dave Jones:** and we'll be able to plot the efficiency of this thing with four different load output powers. Uh oh, we have an intruder! Intruder alert! Intruder alert! Hey, look, you want to play? Wow, look, we've got an oscilloscope, electronic load, multimeters, a breadboard! Wow!

**Dave Jones:** Oh, yeah! They're pots! You want to play with the pots? You want to tweak the pots? You've got to hold your tongue at the right angle. Yes, oh, good boy! Wow, that's fun, isn't it? Alright. Yeah, isn't that cool? Pliers, you want some pliers?

**Dave Jones:** No, you don't want pliers, no you want a screwdriver instead. You want a screwdriver? Daddy will give you a screwdriver. How's that? Oh, yay! Oops, you shorted it out! Dude! Now I've had this thing going at a maximum 2 watts for over an hour now, and I'm getting

**Dave Jones:** about 45 degrees on the top of the unit there, so it's staying relatively cool, really. You know, that's only 25 degrees C above ambient. So here's our results in DaveCAD, 0.1 watt increments all the way up to its rated value of 2 watts here.

**Dave Jones:** And you put those in the PC, and here they are! P out, V out, V in, I in, P in, and calculate the efficiency as well, and ta-da! And here's the final plot! If you plot the efficiency on the Y axis here versus power output on the

**Dave Jones:** X axis from 0 load to 2 watts load, you can see the efficiency. And it's a classic sort of graph, and it drops right down, of course, at the lower end. But the majority of the range, you know, a good half of the range, is 80%

**Dave Jones:** or more from a watt to 2 watts, and then even from, you know, a half watt upwards, it's still, you know, 75% there, or just over 70, sorry, at half a watt. So it's still pretty darn good, 70-80%. And of course at very low loads, you expect it to be very

**Dave Jones:** inefficient, but that worked a treat! If we just have a quick look at some of the output noise here, pretty horrible stuff. I can knock that on the head there, that's 50 millivolts per division, I can knock some of that on the head there by putting a

**Dave Jones:** RFI suppression cap between primary and secondary, and that's 1 nanofarad, knocks it on the head a little bit. And the data sheet claims less than 75 millivolts peak-to-peak ripple and noise at, well, presumably at full rated output current, so we've got the full output current here, 400 milliamps,

**Dave Jones:** 2 watts, and we're basically getting 50 millivolts per division there, there you go, it's certainly in the ballpark and that's with, you know, dodgy breadboard, dodgy grounding and probing and all that sort of stuff. So yeah, it's certainly meeting all its specs so far.

**Dave Jones:** What we're going to do now is test its switch-on performance at full load to see if it overshoots. So we've got full 2 watts output, constant power load, and let's switch it on. Well, switch it off first, input is switched off, and I'm about to

**Dave Jones:** switch the input on, and hey, there we go. Look at that, that's 1 volt per division, so if we take a look at that, we're looking at 1, 2, 3, 4, 5, 6, we've got some overshoot there, goes to just over 6 volts, got some ripply stuff happening there,

**Dave Jones:** some of that 50 hertz stuff is kicking in, but then it jumps back down after, what, 50 milliseconds? Yeah, 50-odd milliseconds, jumps back down and then regulates, basically. Not that this thing is actually regulated, it's just following the input voltage, basically. So if you're

**Dave Jones:** powering real critical stuff with these unregulated in quote marks, unregulated DC-to-DC converters, then yeah, you'd have to watch out for that sort of overshoot. And let's see if it starts up at the full 2 watts at lower voltages. Let's see if it starts up at 4 volts, so let's switch the input voltage off,

**Dave Jones:** switch it on, bang, no problems at all. 4 volts, once again, overshoot, that overshoot to 5, no worries, so it starts up well below its rated input voltage into full load, because it's claiming 4.5, you know, minimum 4.5 input volts. But let's give that another go at 3 volts

**Dave Jones:** this time, 3 volts input. Bang, no, it didn't like that, it switched back off, didn't like that at all. Bang, no, it really, no, it doesn't like that. Let's 3.5, let's say, reset, and bang, there we go, 3.5 volts, not a problem. Sorry, 3.3 volts, not a problem.

**Dave Jones:** And our output current, of course, we're still outputting 2 watts constant power load, and we're getting 0.7 amps out at 2.87. So this thing certainly does exceed its datasheet specs, and I'm getting a lot of confidence with this thing. Right, now let's stress this puppy, let's go

**Dave Jones:** over the 2 watts and see if we can hurt it. Oh, that's a bit touchy, this knob, sometimes it increases 2.5 watts, and we're still kicking in there with our set, of course. We're still kicking in there, we've got 4.85 volts out, and

**Dave Jones:** over half an amp there, not a problem. So let's 4.7 volts, there you go, 3 watts. Get the wet finger on that, yeah, it's getting pretty hot now, I'm going to get the old thermometer out and see what temperature it's at. And while we're over 50 degrees

**Dave Jones:** on the left hand, or because I think it's back to front, it's the right hand side of the device, looking from the silk screen, it is hotter on that side than it is on the other. It's a bit cooler on that side, but this side here

**Dave Jones:** is certainly, certainly getting quite warm. So, but it's still holding in there, it's delivering. It's delivering 3 watts, and it's only a 2 watt rated device, so it's doing pretty well. I wonder if, I wonder how long it will actually go like that.

**Dave Jones:** And you can see our output ripple has drastically increased. But I just hit the switch and restarted that thing, even at 3 watt load, it restarted. No drama. So, oops, I just killed it with that cap, obviously, because I plugged the cap in live.

**Dave Jones:** Let's boot it up, there we go. So our ripple is, I don't know, it's still quite significant. It's a little bit higher without the cap. Now, 5 minutes later, it's still holding in there at 3 watts. Not a drama, so I mean, it's getting, it's getting bloody hot.

**Dave Jones:** I can't touch that, but still, I'm pretty impressed. It's certainly creeping up towards 60 degrees here. I mean, this is not the best probing solution, I'm just holding my thermocouple on the plastic top of the case here. It's going to be hotter inside, of course,

**Dave Jones:** the circuitry, the thermal resistance of the case is going to be fairly high, but there you go, yeah, we're crack 60. And of course you certainly wouldn't design your product to overload this thing, so you would work within the 2 watt stated specification, of course, but

**Dave Jones:** it can deliver a temporary increase in output power at the very least. And I think it's time to get a bit brutal. I'm going to short the output. Here we go, see if we can survive a short circuit. It doesn't say in the data sheet

**Dave Jones:** if it's short circuit proof. Wham! There we go. With the shorted output 5 volts input, we're getting 370 milliamps on the input there, and I'm just going to leave it shorted, because I'm a cruel bastard. I'm going to leave that shorted and see what happens.

**Dave Jones:** Well, it's still going, and of course with a shorted output, 5 volts times 0.4 is that 2 watts, so it's delivering the full 2 watts into no load, so where's it all going? Well, head's all going into there, so this poor little package

**Dave Jones:** now has to dissipate 2 watts instead of delivering 2 watts to the load and being 80% efficient. Only going to normally dissipate 20% of that 2 watts. Check it out, we're getting up to 100, almost 100 degrees Celsius on this sucker, in fact I'm sure it is

**Dave Jones:** and of course it'll be hotter inside, but it's been like over 10 minutes, maybe 15 minutes, and with this sucker shorted out, and it is still, still hanging in there. Cannot kill it, I'm sure it will eventually die, but geez, it can certainly handle a

**Dave Jones:** 10 minute complete short on the output. Great stuff. Well, there you have it, I think I'll put it out of its misery there. Remove the short, bang, and it should drop back to normal. But I hope you liked that, that was just some

**Dave Jones:** quick little tests on a nice little 2 watt DC to DC converter. It's a robust little sucker, it seems to exceed all of its specs and works quite well. It is an unregulated type of course, so its output voltage effectively follows the input voltage, but I, you know, that's exactly what I

**Dave Jones:** want here. I don't need a regulated, a fully regulated converter because I've got a following regulator afterwards, so it doesn't matter a rat's arse really, but it's a neat little whoa, whoa, whoa, hot, hot, hot, hot, hot, hot, hot, oh man, hot potato, hot potato.

**Dave Jones:** Anyway, there you go, that's a little 2 watt converter, hope you liked it. And as always, if you want to discuss it, jump on over to the EEVblog forum, and if you liked the video please give it a big thumbs up. Catch you next time.

**Dave Jones:** Mmm, toasty.
