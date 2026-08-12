---
video_id: i36yCY1pyrY
title: EEVblog #1301 - Arcade Machine Repair
url: https://www.youtube.com/watch?v=i36yCY1pyrY
source: youtube-asr
timestamps: {"0": 1, "1": 21, "2": 35, "3": 47, "4": 59, "5": 69, "6": 80, "7": 105, "8": 113, "9": 122, "10": 131, "11": 141, "12": 153, "13": 163, "14": 175, "15": 184, "16": 198, "17": 212, "18": 225, "19": 235, "20": 252, "21": 265, "22": 279, "23": 295, "24": 308, "25": 316, "26": 331, "27": 344, "28": 354, "29": 372, "30": 379, "31": 395, "32": 409, "33": 427, "34": 437, "35": 450, "36": 462, "37": 473, "38": 493, "39": 503, "40": 509, "41": 519, "42": 534, "43": 549, "44": 564, "45": 581, "46": 594, "47": 609, "48": 619, "49": 638, "50": 647, "51": 659, "52": 681, "53": 691, "54": 701, "55": 711, "56": 721, "57": 734, "58": 748, "59": 763, "60": 771, "61": 791, "62": 804, "63": 820, "64": 829, "65": 838, "66": 853, "67": 862, "68": 876, "69": 893, "70": 905, "71": 924, "72": 937, "73": 953, "74": 968, "75": 980, "76": 1001, "77": 1010, "78": 1026, "79": 1036, "80": 1045, "81": 1062, "82": 1082, "83": 1092, "84": 1107, "85": 1115, "86": 1130, "87": 1140, "88": 1149, "89": 1157, "90": 1172, "91": 1184, "92": 1199, "93": 1213, "94": 1230, "95": 1239, "96": 1254, "97": 1272, "98": 1282, "99": 1303, "100": 1314, "101": 1326, "102": 1337, "103": 1350, "104": 1360, "105": 1375, "106": 1386, "107": 1400, "108": 1412, "109": 1422, "110": 1436, "111": 1446, "112": 1460, "113": 1473, "114": 1491, "115": 1502, "116": 1516, "117": 1534, "118": 1548, "119": 1574, "120": 1589, "121": 1597, "122": 1622, "123": 1632, "124": 1645, "125": 1661, "126": 1676, "127": 1697, "128": 1706, "129": 1719, "130": 1727, "131": 1744, "132": 1768, "133": 1783, "134": 1797, "135": 1810, "136": 1818, "137": 1832, "138": 1846, "139": 1861, "140": 1872, "141": 1897, "142": 1920, "143": 1932, "144": 1945, "145": 1958, "146": 1971, "147": 1986, "148": 2000, "149": 2008, "150": 2020, "151": 2043, "152": 2056, "153": 2064, "154": 2086}
---

**Dave Jones:** Hi. Unfortunately, there's been a tragedy in the EEVblog lab. The arcade machine's on the blink. All that's coming out of it is just like this low-level mains hum. I don't think that's ever been there before, but usually it was going, you know, did it did it did it did it did it did it the 8-bit sound and just silence.

**Dave Jones:** Huxley was playing it today and no, she's gone on the blink, so tear down time. Now, it actually uh does still work, but it appears to be intermittent cuz it's initializing at the moment.

**Dave Jones:** Uh the monitor's obviously working fine and something to do with the uh well, the JAMMA board, the power supply, something like that. And that uh that hum I could hear before, I think it's gone now.

**Dave Jones:** Maybe it's only when it goes on the fritz. Anyway, there we go. We're in like Flynn. Um so, let me play it for uh a few minutes and Well, there we go.

**Dave Jones:** There we go. It just went. You saw it. Check video cable. There it is. Just went kaput. I can hear the high-frequency hum. I So, yeah, I was playing that for like 5 minutes tops.

**Dave Jones:** Turns out the hum is actually coming from the speaker. I thought it was coming from the power supply, but you can clearly hear that. Yeah, I reckon uh the power supply is uh gone kaput on that.

**Dave Jones:** It just pulls out like that. Bob's your uncle. We're in like Flynn and uh that's the I've done a separate uh video on that. This is where I got the uh video uh feed out of this thing, the VGA video out, convert it to HDMI and uh power it from an external uh 5 V here, so VGA to HDMI uh converter, which then I then capture, so I can capture uh game footage and

**Dave Jones:** stuff. All right, so I'll take you through a guided tour of this. We've got ourselves a mains power supply over here. That's just uh 5 V 15 amps, as you can see.

**Dave Jones:** It I don't think it needs uh the 15 amps. It's just pairing a, uh, JAMMA board. Then we've got our JAMMA board over there. I'll show you that, uh, in detail in a minute.

**Dave Jones:** And then, uh, that pipe there is just for the, uh, coins. If you do want to use coins, this one actually, uh, I've got it actually bypassed. But there we go.

**Dave Jones:** You can see that for those playing along at home. So I'm sure the, uh, arcade aficionados will tell me what one that is. I don't know. Um, but I have used coins in it before.

**Dave Jones:** But anyway, it is, uh, disabled. And up here and they're the, uh, joysticks and the arcade buttons. Once again, the arcade aficionados might be able to tell us the, uh, brand and the model there.

**Dave Jones:** I don't know. I didn't specify this. I just had someone, uh, make it for me down in Wollongong. So I don't I don't know if they're around anymore. But see the micro switches on the bottom.

**Dave Jones:** Uh, big and beefy. Look at those. And then there's just a monitor. Um, and that's just a HP, um, LCD monitor, of course, compatible with the, uh, get Well, there's a 15 kHz or there's 30 kHz, isn't there?

**Dave Jones:** Uh, two different frequencies. I think this one might be set to the 30 kHz, uh, mode cuz a lot of LCDs, I believe, can't handle the old-school, uh, 15 kHz.

**Dave Jones:** There's not much in it. So I think the monitor's fine. So something's gone kaput in here and my money would be on the power supply there. All right. First thing we're going to do, of course, is measure that, uh, 5-V rail there.

**Dave Jones:** And nope. Well, there's your problem. 1.47 V. Okay, I won't even bother looking at the, uh, JAMMA board. I don't know. Is it one of these One Hung Low brand power supplies?

**Dave Jones:** Actually, before we do that, I just want to measure that again. You can see that our lights come on now. So our 5-V rail should be good. And sure enough, there we go.

**Dave Jones:** 5.18. They've adjusted it a bit high, so there's a bit of drop. And the JAMMA board's working. I can see it flashing its LEDs and stuff like that. So, yeah, everything's hunky-dory.

**Dave Jones:** So, it looks like we have like a drop out after about uh 5 minutes. That's interesting. Hmm. Confidence is not high. I repeat, confidence is not high. Uh by the way, there was an extra uh 12 volts um supply on that thing as well.

**Dave Jones:** Yeah, um one hung low, no namer. Yeah, this case doesn't instill a lot of confidence in me. All right, is it just going to be something lame like a cap, or is it going to be something more interesting?

**Dave Jones:** Okay, there we go. We're in like Flynn. Dodgy-looking label on that cap for starters. I was right that this didn't instill a lot of confidence. Um this looks really old-school.

**Dave Jones:** Just the switch on the the right-angle switch there. Nothing wrong there, Rubicons. They're all right. No wackers. Uh is there something else? The output uh caps they look uh there's no bulges in them, but yeah, they're a I don't know what brand that is.

**Dave Jones:** You Lee or something, I don't know. Another low ESR jobby there. You can usually tell by the green and the yellow. But yeah, certainly the uh design and layout leaves a bit to be desired.

**Dave Jones:** It I mean, it looks like something that was uh slapped together in the '80s or something. Uh I wonder if we could actually get a date code on this thing.

**Dave Jones:** But uh we've got our two primary side driver trainees up there. Look at that. They're all the way over there. Um that's interesting. Just totally old-school uh design and layout and build quality.

**Dave Jones:** Anyway, given that it's uh 5 minutes um use, that means, you know, something could be heating up. First choice wouldn't necessarily be the caps, cuz I they don't look like they're bulging at all.

**Dave Jones:** Um and these are Rubicons, so they should be okay. Not sure what one that is actually. I can't read that gold writing. It's really um, gold on green. It's really quite annoying.

**Dave Jones:** You got to get that in the right light, but I wouldn't rule out a dodgy joint somewhere. We've had those before, like a dry joint, you know, when the thing starts heating up after 5 minutes and or something else, you know, we've had like diode bridges repairs I've done in the past fail after I did an oscilloscope repair.

**Dave Jones:** I have to lick that one in. If I think of it, that one was really interesting. Oh, spoiler alert. Yes, the best part about that video was tracking that down.

**Dave Jones:** Anyway, it's an interesting video. I'll link that one in, but yeah, I wouldn't rule it out. I mean, self-tappers going into the into the metal. That's terrible, Muriel. Good thing is it's all single-sided, so you can have a good look at all the joints.

**Dave Jones:** Pass it to the left. Oh, yep. There's a definitely a good chance I've called that one. Look at the output connections over here. Uh, they look dry as a dead dingo's donger.

**Dave Jones:** These are the 5-V and ground outputs. Wow, dry as a dead dingo's donger. Unbelievable. And 12-V go over. Oh, this is just shocking. Wow, who soldered that? Stevie Wonder?

**Dave Jones:** And check out the main driver chip over here. It's almost as if somebody's had a go at that. Like everything else is wave soldered and that has been Harry hacked.

**Dave Jones:** That is terrible, Muriel. Wave soldered, so it looks like this is like a repaired board or something like that. Even the Oh, no, no, the driver up there looks all right, but yeah, get down to there, you can see the flux residue.

**Dave Jones:** They're okayish, but I'd go in there and resolder those as a matter of course. Is that actually a track that's been cut? No, no. It's just um, is that just a dead bug?

**Dave Jones:** Clean all that up, but ah jeez, you know, yeah, I would suspect that as the first port of call cuz what happens is, you know, these are carrying you know, I don't know what the draw of that board is.

**Dave Jones:** I'd have to look, but but let let's say it's drawing like 5 watts or something like that, you know, it's drawing an amp or something like that. So, these can these joints can actually heat up and just go open as you know, after like 5 minutes or something like that, but why it's only happened now, I you know, it's one of these marginal things.

**Dave Jones:** So, first thing I do is simply resolder all those and then put it back in, power it up and play it for like an hour or something like that.

**Dave Jones:** And if we don't get any drop outs, then yeah, I think we've solved it. Okay, I'm just curious to see what happens if we just heat up that joint there.

**Dave Jones:** So, let's just give her a whirl. See if she see if she crumbles or not. I'll go on this side here so we can hopefully see it on camera.

**Dave Jones:** Oh, look at that. Oh, yeah, that's that's not good. Oh. The fumes. Oh my god, you're going to have to suck it all out. Don't reuse the solder. Suck it all out.

**Dave Jones:** Put on fresh stuff. Now we're talking. Look at that. Those little notches in there, they're actually taken out of the copper PCB pad. So, yeah, that's not me physically taking a notch out on each one of those.

**Dave Jones:** There you go, like a ball one. These self-tapping screws into the metal work. They're awful, really. I could just strip that extra quarter turn, she's goneski. Yeah, it's got to be one of the most how you doing power supply like brick power supplies I've seen.

**Dave Jones:** Just the uh the lack of quality in the construction. I was surprised to find Rubycon caps in there actually. Well, it turns out when you make assumptions like that, you can come against uh Um and plug it in and it got a brief flash there, but not nothing.

**Dave Jones:** So, it's it could be a combination. I mean, those joints were as dry as a dingo's dong. So, I had to redo those. They were dodgy as. Something else like I didn't screw it back in.

**Dave Jones:** That was the whole idea. All right, so if we go back here and here and have a squeeze, I've actually, you know, I found a few more suspect joints and things like that and I've had a little bash at them cleaning them up and still No, I get exactly the same result.

**Dave Jones:** So, I've gone around with my LCR meter in impedance mode. I've measured some of the cap like I've measured well, most of the caps, almost all of them and they're all okay.

**Dave Jones:** Like they're down in the, you know, the expected 100 kHz type values you'd expect for these caps. So, if it was, say, like a cap on the secondary side, for example, then like these ones here might only be for the 5 volts, whereas this one here is probably for like the 12 volt output here.

**Dave Jones:** So, if one of these caps went on the 5 volt rail, you'd expect the 12 volt one to still be okay. All right, power's on. Actually, the LED is kind of on.

**Dave Jones:** It's measure No, 2.3. No, that's no good. This is the This is the 12. Yeah, I'm only getting 5 volts on the 12 volt rail and this is minus 12.

**Dave Jones:** No, 1.3. So, it's most likely to be something primary side related rather than an individual thing on the secondary side. So, let's have a look at the bottom here and by the way, it's always good like just with one hand just hold on to the plug just so that you don't cuz if you're powering this, unpowering it all the time, trying to troubleshoot something like this, you don't want to

**Dave Jones:** accidentally forget plugged in and then you start touching the thing. That could really ruin your day. Anyway, yes, it does have bleeder resistors across about two main caps here.

**Dave Jones:** So, that actually um that's for sharing as we'll see and also will help bleed those capacitors as well. So, it's safe to touch uh fairly quickly after power down.

**Dave Jones:** Of course, you can measure that. Anyway, we've got mains input over here. Input cap across here. We've got and there's a varistor as well. And we've got a common mode choke.

**Dave Jones:** And this is our bridge rectifier here. So, it comes in to our bridge rectifier. Here's our output of our bridge full wave mains bridge rectifier. Here it goes down to one of the caps.

**Dave Jones:** As you can see, they're actually split. Here's the other cap here. So, they're actually in series like this and it goes back and each one has its own current sharing and bleed resistor as well.

**Dave Jones:** And this here is your 240 V 110 V switch. So, it's currently these two terminals are shorted at the moment. So, this is just isolated. So, both of these caps are in series across the 240 V mains there.

**Dave Jones:** So, we'll just measure that. Okay, so let's probe across there and there and we should get 330. Yeah, 330. There you go. So, our full wave bridge rectifier is working just fine.

**Dave Jones:** All right, at this point it'd be really handy to have a schematic. Unfortunately, this being the one hung low that it is, it Wow, hang on. I just noticed the date code.

**Dave Jones:** 84. Yeah, that explains a lot. I I'm debating whether or not I should even repair this. I'm just going through orders and academic exercise. I'm thinking about Yeah, I I think the guy who built this cabinet has just like found any old power supply he had lying around.

**Dave Jones:** It didn't So, this thing is ancient. Couldn't get a date code from the chip, but we did get a part number and it's a KIA494. Killed in action. That tells you a lot.

**Dave Jones:** Anyway, it's obviously a clone of the Texas Instruments TL49 for absolutely classic PWM controller, which doesn't necessarily have to be used with a main switch mode like this. It's just a pretty much generic PWM controller.

**Dave Jones:** You can use it for power supplies like main supplies like this, other DC to DC converters, or other applications. It's like the 494 is just it's been around forever.

**Dave Jones:** It's used in tons of different things. Anyway, so it's a clone of that. So I couldn't get a schematic. So what I found is this one from Eric Taylor.

**Dave Jones:** Thank you very much. There's the website address there. So if you don't have the exact schematic, the next best thing rather than stabbing around in the dark is to at least know what the topology is going on here.

**Dave Jones:** Mains comes in here, full wave bridge rectified into these caps here. We've got two switching down here as we'll take a look at. We've got some isolation transformers here and here.

**Dave Jones:** And of course this is our main power transformer that's going from the primary over to the secondary side. This is very similar to the topology, I believe, to what's going on in here.

**Dave Jones:** Basically, they're 240 volts in, full wave bridge rectifier. We get our, you know, 230 volts DC across here. Then it goes into two switching power like this. And if you actually flip it over and have a look, you'll see it is exactly the same.

**Dave Jones:** Follow the money, okay? Call like this is just say it's the top side here. I don't know whether or not it is. Okay, goes into one side of the power The other side of the power there comes out, goes to the other switching transistor down here.

**Dave Jones:** So that there it is in the in in there like that. And then the other side of that goes back right around to tada, the negative or the other side of the uh mains DC input.

**Dave Jones:** So, those two power transistors are simply alternate switching that. And of course, they've got to be isolated, of course, from the uh drive side here. So, this is what this isolation uh or this gate drive transformer, as it's called, does here.

**Dave Jones:** Now, why they've got uh the two there, there might be a little like a little secondary thing that's powering that's tapping off some voltages, but I reckon that one there, that puppy, if you have a look, that configuration seems to have a dual winding in there.

**Dave Jones:** It seems to be implying one winding, two windings like that. So, that's equivalent to one gate drive and the second gate drive. And I'm sure if you actually traced all that out and followed the money, um then of course, it's not just a direct connection like that.

**Dave Jones:** There's other, you know, stuff in there. There's diodes and resistors and various whatnots, but basically, all that's doing is driving the two switching transistors there. Of course, in the middle here, goes to this is our main power transformer over here.

**Dave Jones:** I was going to call it a power but people have I complained that I call both transistors and transformers And well, that's true. They both have the, you know, going back since before I was born, they were called So, yep, that's just going to be the primary there and the secondary over here.

**Dave Jones:** They'll have multiple taps, of course, for different voltages. And that's about all she wrote. Yeah, there's no reason why we can't get in there, not with our regular regular crow probe.

**Dave Jones:** I've done a video of how not to blow up your crow probe crow cathode ray oscilloscope here in Australia. Your crow probe, as always, I'll link that in. So, we'll use our high voltage probe and we'll be able to see if these little puppies are switching.

**Dave Jones:** They're obviously doing something because we did actually measure the outputs at, you know, a volt, two volts, things like that. So, something's sort of sneaking through. So, there you go.

**Dave Jones:** I used my uh high voltage differential probe. I'll probe directly across the uh primary side of the transformer there. See if we can get a switching waveform. All right, power on.

**Dave Jones:** We are switching. There you go. That's 100 V per division. Getting something there. And switching frequency there, about 27 kHz. That sounds about right. But, the problem is uh we're only 20 V per division.

**Dave Jones:** I do have my probe set up correctly to 100 to 1. So, uh yeah, that seems a bit low, 20 V per division. Although, having said that, if you notice that uh this particular schematic here has a low ratio transformer, 1 to 2.4, with this AC series cap in here.

**Dave Jones:** And of course, we have the AC series cap in here like this. It's one side of the transformer here. There's only uh there's only one uh coil on the primary.

**Dave Jones:** And there's the AC cap going back over. And it jumps right back over to the center point of those two caps, exactly. So, this is practically an identical circuit um to what we've got here traced out.

**Dave Jones:** Except in this particular case, we've got a 1 microfarad uh film cap in here. And yes, I have actually measured it. And yes, it is bang on 1 mic.

**Dave Jones:** So, nothing wrong with that cap. So, with a small turns ratio transformer, they're kind of the levels uh that we'd expect for like you know, 5 V and 12 and and minus 12 V uh output.

**Dave Jones:** So, you know, I don't know about the waveform though. Okay, just for kicks, what we'll do is we'll uh probe the secondary side. So, I'm on one side of the output diodes there.

**Dave Jones:** That is uh that's not a transistor. That's actually a dual diode uh package. So, I'm probing one of those. We can actually go back to using our scope probe and the common ground.

**Dave Jones:** Because if you have a look, uh earth is connected to this, which is connected around to your ground because it's mains earth referenced output cuz we're measuring the output.

**Dave Jones:** Nothing on the primary side though because you'll blow your scope up and yourself probably, but on the secondary side completely safe to do. So, power that up and probe it and well, there's your problem.

**Dave Jones:** Yeah, that's one sick puppy. We're getting some volts on the output, but we're getting like just little lousy bursts, high frequency bursts, not what we actually want to have any decent current output.

**Dave Jones:** That's why we're getting like some voltage on the secondary, but yeah, obviously there's primary side drive problem. And I'm probing the diode output. It's actually on the choke there of the 5-V output and wah wah wah wah.

**Dave Jones:** Well, yeah, there's your problem. So, So, we're getting getting that on both the 5-V diode output and the 12-V diode output. So, that shows it's not the secondary. It is definitely a primary side drive problem.

**Dave Jones:** Okay, so what I'm doing now is just probing pin 11, which is one of the drive outputs. There's two, pin eight and pin 11, and there you go. There's the 27-kHz drive signal coming from the PWM controller.

**Dave Jones:** Capture that. There you go. That seems to be doing its Well, it's doing something anyway. And there's the other drive signal there. So, whoa, it's Yeah, it's playing up.

**Dave Jones:** Yeah, like that should be consistent and it's not. There's really something wrong there. That should be like a consistent output. Yes, it is the 27-kHz if you actually measure it, but yeah, there's all sorts of weirdness happening there.

**Dave Jones:** So, you know, it could be anything like could be a sense, you know, the feedback, the voltage reference, or anything like causing an issue, Um, but it does seem at least to be the PWM chip seems to at least be working because it's outputting something.

**Dave Jones:** Right, so what I want to do is I just want to go back to measuring that primary side transformer now that we've got more information on the secondary, well, the actual drive side of that, the PWM control side of that.

**Dave Jones:** And there's our signal again, but if we actually run that you can see it's just going silly buggers. I mean, it's just all over the shop. So, yes, if you go, "Oh, yeah, okay, that's a bit repetitive there." But then you've got big periods in here where it skips and everything.

**Dave Jones:** And I thought that this chippy it didn't skip like that. It's supposed to just be consistent and change the duty cycle. So, it's just nuts. It's just all I Look at that.

**Dave Jones:** Look at that. What's going on there? All right, because that output is just complete silly buggers. We kind of have a look at the power supply for the driving chip.

**Dave Jones:** So, I determined that this link over here goes over to pin 12 and that's the VCC supply for the chip. I think it's like on this schematic here it's 16 volts.

**Dave Jones:** I'm not sure what the maximum is. So, well, hello. Unless that settles, that is not a great power supply, is it? That could explain why we've got serious problems.

**Dave Jones:** So, it's 15 volts with a ton of ripple on there. Maybe one of the bypass caps for that rail is gonsky. That's pretty terrible, but there is a supply there, but yeah, you can't have that much ripple.

**Dave Jones:** That's Oh, yeah, look. Look, it's going silly. Yeah, it's going silly buggers. So, whoa. Whoa, now we're getting huge transients on there. Wow. That's your power supply for your control chip.

**Dave Jones:** There's your problem. What's causing that though? It's obviously getting an initial uh from the uh primary side to uh to power that chip. Oh, there we go. Look at Whoa, look, it's just jumping.

**Dave Jones:** It's just Oh, it's got the heebie-jeebies. And even replacing the uh cap down there, it was 4.7 mic 50 volts with 100 mic, and it tested reasonably okay, and no, it's still there.

**Dave Jones:** So, not even like a 20-V increase in the capacitance there can uh smooth that puppy out though. It's a bit better, but yeah, not magically better, and it's still um doing that weird ass thing.

**Dave Jones:** Seems okay at the moment, but you saw it before. Yep, there there it goes. It's just It's It's playing silly buggers again. This thing's just going uh No. No, no, no, no, no.

**Dave Jones:** Okay, now from what I can actually uh gather here is that uh this little secondary transformer in here is actually in series with the uh primary side uh power switching uh transformer.

**Dave Jones:** So, that's just tapping that off, and that's um just all that sort of stuff. You can actually see it coming over. This is actually a center-tapped uh This is the main primary side one.

**Dave Jones:** Center-tapped, it jumps over there. There's the primary side for the secondary uh transformer the auxiliary transformer, we'll call it. There's the secondary side tap, and that's got all those all those components in there all those resistors and diodes there.

**Dave Jones:** So, that looks like Is that like a full bridge? Uh That could be a bridge configuration there. And that's going in, but that's not actually powering the rest of the uh circuit.

**Dave Jones:** What that's um That's just uh sensing. The power is actually tapped off from up here on the gate driver transformer here. There's actually on the center tap um on the secondary side, that actually goes directly to VCC here.

**Dave Jones:** If we have a look, here it is here. Here's the center tap for that. There's that's a jumper link that goes over. Follow the money, there's a resistor, and that goes to pin 12, and that's our VCC there.

**Dave Jones:** So, that's powering that. So, there's no like auxiliary uh transformer, auxiliary oscillator actually powering this rail here. So, how it's actually And there's no other oscillator on the primary side here.

**Dave Jones:** Um which is interesting, which, you know, there's no like extra auxiliary winded on here and an oscillator on this side, which then drives um uh which then, you know, is rectified and gives our power supply over here.

**Dave Jones:** So, I'm not exactly sure how it's actually getting uh our main supply here and why it's so upset and uh you know, just going ballistic there. So, these two There's two primary side electrolytics here.

**Dave Jones:** I've actually um taken those out, measured those. They were fine, but I replaced them anyway. Everything's hunky-dory. I've measured the uh diodes in here. They seem fine. And upon some further tracing, I've determined that the uh 16/15 V I believe it is is coming through a series resistor, a series diode, actually coming from the 12-V tap, which is actually uh you know, one of the outputs uh down here, basically.

**Dave Jones:** But um yeah, once again, it's uh there is no primary side uh separate oscillator to actually power this thing. So, it looks like it's bootstrapped in uh you know, some way.

**Dave Jones:** It's like uh god, how much further do I have to trace this thing? It's just It's just ridiculous. I could waste hours and hours going down this rabbit hole.

**Dave Jones:** And given that that is the waveform on the output of this cap here, even when I put in the much larger cap there on the rail, it's almost as if um there's something wrong uh, possibly with the, uh, driver transistors in here and it's just drawing, um, excess, uh, current or something like that.

**Dave Jones:** Because to get that much ripple on that, uh, rail is just, yeah, there's something loading it down. So, something to do with the chip, perhaps even. Like, I don't know.

**Dave Jones:** Could be like, uh, quite a few things. And if you go in there and actually measure the bases of the, uh, transistors in there, they all seem hunky-dory. I've measured them all and they all seem fine.

**Dave Jones:** So, yeah. Um. And well, I was about to abandon this, but, tada, it now magically works. I'll explain why in a second. Got it hooked up to my electronic load there, drawing a constant current of 1 amp and, uh, it works an absolute treat.

**Dave Jones:** So, what was wrong with this thing? Well, unfortunately, I can't tell you the exact reason because what I did is that I, uh, went back to my original hunch that, look, it I think it's a solder joint at, uh, fault here.

**Dave Jones:** There's a little micro crack in the solder joint because over time especially like 35 years or something like this. Even though this power supply hasn't really been stressed a lot, the thermal, uh, changes in the components every time it powers up and powers down, they, you know, metal things, they expand and contract with, uh, temperature changes.

**Dave Jones:** And that can cause micro cracks that are almost sometimes impossible to see. So, what I did is just like, I was going to completely abandon this as I'll explain in a minute.

**Dave Jones:** Um, there's just there was no point. I wasn't going to reuse this thing cuz sometimes you just have to, give up and say, "Look, it's not worth it. It's beyond economical repair." Not in terms of parts cost to fix it, but in term of you in terms of your time investment.

**Dave Jones:** And I was never going to reuse this thing anyway. So, it was pretty much it just an academic exercise to actually get this thing, uh, working again. Yes, I switched it off now.

**Dave Jones:** So, what I actually did was just went in there and I just resoldered any joint that so much as looked at me the wrong way and I soldered like, I don't know, a dozen or two joints and yeah, it's it's magically working again.

**Dave Jones:** So, unfortunately, unless I can systematically track down where that that actual fault cuz we did a reasonable amount of like reverse engineering detective work there and we and I I did pretty much all the basic stuff you should be doing to track down the fault and still it was kind of like a weird issue that something to do with like the power supply bootstrapping when it powers up and things like that and

**Dave Jones:** keeping it running and and stuff like that. So, yeah, not great. But anyway, it's fixed itself. So, anyway, it was obviously a solder joint somewhere. I can't tell you if it was on the secondary side or somewhere over on the primary side cuz I sold I resoldered the chip yet again.

**Dave Jones:** I'd already done that uh before, by the way, and another couple of other suspect joints and there were stuff in there that I I resoldered individual joints and then repowered it, but I didn't In the end, I didn't want to just keep doing one joint, repower it, see if that caused a problem.

**Dave Jones:** So, I just, you know, did a few dozen and yeah, it's come good. So, it was a micro crack. It seems to be operating, you know, more than the 5 minutes under a decent load and yeah, Bob's your uncle.

**Dave Jones:** So, that's fixed, I guess, in quote marks, but I have absolutely no plans to reuse that thing whatsoever. So, that you know, that was a real I hope you enjoyed that.

**Dave Jones:** That was a real interesting academic exercise just going through things even though we couldn't find the exact culprit. Leave it in the comments down below if you want to have a guess at exactly what mechanism actually caused the stuff we were seeing.

**Dave Jones:** But before we call it quits on this and we go back and actually fix the arcade machine, we'll just probe a few things when it's working. So, let's just start with the primary of the main switching transformer and there it is there.

**Dave Jones:** There you go. Once again, it is the 20 7 kHz or thereabouts, but that's the that's the proper waveform we should be getting and it's completely consistent. No skipping, no funny business at all.

**Dave Jones:** That's our 50 volts per division for those playing along at home. And if we probe our output here, then that VCC power supply, it's actually um much more than 15 volts actually.

**Dave Jones:** Look at that. It's 5 10 15 20 20 5 volts. Thank you very much with bugger all ripple. So whilst I can't tell you the exact mechanism at play there, I hope you found that an interesting example of you know having a suspicion up front that it was a like a solder joint a thermal type issue and then going down the rabbit hole and doing your basic checks and you

**Dave Jones:** know Murphy will get you every time in that it's not going to be something simple. Never is for me because well, you know. And then you follow it down, you start to you know suspect your electrolytics and other components and your diodes and your transistors and you start measuring things and everything's you know looking just fine and then you eventually come back to it where you couldn't see any physical fault before

**Dave Jones:** and the symptoms that you were getting were like not quite easy to understand unless you reverse engineer the whole thing and spend a lot of hours at it and stuff like that and in the end it was you know looks like it was just a a solder joint that's come a gutser.

**Dave Jones:** So, yeah. You get them sometimes. Anyway, leave your comments down below. And then to top it off, I never actually had that like 5 minute thermal fault on the bench here.

**Dave Jones:** Just by literally like taking it out, unscrewing it, physically handling and doing all that sort of stuff, it it never actually showed those symptoms on the bench here. It simply had those weird intermittent bursty, you know, a failure mode uh uh kind of thing.

**Dave Jones:** So, yeah, it's like when you can't get a repeatable symptom like that when you take it out onto your bench to work on it, uh ruins your day. Sucks your life away.

**Dave Jones:** And the reason I don't want to do that is because look, I don't have to power it through this wiring harness here. It's got a PC power supply four-pin Molex connector on it for the 5-V and 12-V uh supplies required for this thing.

**Dave Jones:** And I've got a million dumpster PCs with perfectly good uh you know, relatively modern compared to that ancient piece of crap. No, that's just not worth it. So, I'm just going to get a uh PC supply, whack it in here, and Bob's your uncle.

**Dave Jones:** I'll get this thing back up and running. Uh bugger it, even a PC power supply is too messy. I found this in the uh junk bin of power adapters.

**Dave Jones:** I've I've got dozens and dozens of things. Uh 5-V 2-A, 12-V 2-A. That'll work a treat. So, there you go. That's a completed installation. I just put a uh mains cable in, cable clamped.

**Dave Jones:** I've got a double adapter in there. The little uh plug pack is uh clamped down the bottom there, and that just uh I just splice that in line with the existing uh power lines there, and I just replaced the um bare wire mains cord going up to the monitor with just a regular one, and Bob's your uncle.

**Dave Jones:** That's it. Neat and tidy. And as you'd expect, it works an absolute treat. Haha, winner winner chicken dinner. And that's better than that uh 30-year-old uh power supply I had in there.

**Dave Jones:** That was just garbage. So, don't know why they uh installed that to begin with. That's just insane when you could have just used a PC power supply. That's what it was designed for.

**Dave Jones:** So, yeah, nuts. Anyway. Woo! So, if you liked that video, please give it a big thumbs up. And as always, comment down below. Catch you next time. Woo! Yeah.

**Dave Jones:** Power up. Woo!
