---
video_id: yMIzsFAztv4
title: EEVblog 1455 - Capacitors Produce Current During Reflow Soldering! WTF!
url: https://www.youtube.com/watch?v=yMIzsFAztv4
source: youtube-asr
timestamps: {"0": 0, "1": 20, "2": 32, "3": 46, "4": 63, "5": 82, "6": 100, "7": 112, "8": 128, "9": 145, "10": 161, "11": 174, "12": 188, "13": 204, "14": 223, "15": 236, "16": 252, "17": 264, "18": 279, "19": 292, "20": 306, "21": 322, "22": 335, "23": 351, "24": 363, "25": 377, "26": 393, "27": 405, "28": 417, "29": 433, "30": 451, "31": 465, "32": 480, "33": 498, "34": 511, "35": 526, "36": 543, "37": 555, "38": 568, "39": 585, "40": 599, "41": 615, "42": 627, "43": 639, "44": 652, "45": 666, "46": 679, "47": 692, "48": 705, "49": 717, "50": 733, "51": 747, "52": 761, "53": 774, "54": 787, "55": 802, "56": 816, "57": 830, "58": 842, "59": 855, "60": 870}
---

**Dave Jones:** Hi, I saw this on Twitter. Some leads are lighting up when they go through the reflow oven. Uh What the What's going on here? A lead across a capacitor, heated up, it lights up. I got to check this out.

**Dave Jones:** So, where does this come from? Well, I heard about this from Greg Daville on Twitter. Highly recommend you follow Greg. He does great like close-up macro photos of like SMD and soldering among other things. Really great. Anyway, he

**Dave Jones:** says, "Weird phenomenon. During reflow, some green lead power indicators are emitting slightly. Seems like maybe during reflow, solid polymer caps are having an effect on creating small electrical current. Does anyone know what this effect is called? Maybe some

**Dave Jones:** further reading." And he did a test with a 220 mic 50 V electrolytic surface mount cap like this, heat gun onto the cap with a lead, and sure enough, it lights up. So, very interesting. And Ian here pointed out

**Dave Jones:** this Stack Exchange article about somebody saw these leads light up in the reflow oven, but I suspect, if you notice, there's a thermocouple there. And the thermocouple looks like it might be touching a pad that's coincidentally near all those leads. So, I suspect that

**Dave Jones:** is not due to what we're seeing here cuz there's no capacitors. This is due to capacitive electrical coupling with if it is through the thermocouple, through the shielded bottom and everything else. So, I don't think anything's There's anything to see there, but there there

**Dave Jones:** there you go. I'll link in the thread down below, but fascinating. You can light a lead by heating up a capacitor. Hmm, let's do some experiments. I've got an ammeter. I will hook it up in a second. I'll show

**Dave Jones:** you that. It's on microamps range, and I've got a, you know, a selection of SMD electrolytics here. I've just chosen a 470 microfarad 16-V jobbie. I don't know the brand of these cuz this is one of these just generic

**Dave Jones:** cheap-ass kits. But it does have the split in the top there, which indicates that that is not a solid polymer capacitor. That indicates that it's an wet electrolytic type capacitor, which it looks like from the photo um similar

**Dave Jones:** to the one Greg's using. Somebody else on Twitter mentioned that it could be some sort of precharge / dielectric absorption of the capacitor. Link in dielectric absorption. Have I done a video on that? I'm sure I've mentioned it at least many

**Dave Jones:** couple of times in videos. Anyway, if I hook this up, I've just had this sitting here before. It was actually hooked up and shorted out with the load of the milliamp the microamp input here, which is what 1K or

**Dave Jones:** something like that. Um but anyway, I'm going to hook this up and watch watch the reading. There will actually be a charge. It jumped up to a couple of microamps there. So there is some sort of dielectric absorption charge building

**Dave Jones:** up, but it can't be that on its own because the lead would instantly just drain any of that away. Anyway, here we go. I've got my heat gun set to 100° C. So I don't want to, you know, take it to

**Dave Jones:** like reflow temperatures yet. I want to do it just a low temperature. So let's see what 100° C does. Here we go. Yep. Yep. Sure enough, it's going up, but not much. I mean, you know, 0.2 microamps. That's a sniff of an oily rag stuff.

**Dave Jones:** That's half a bee's dick. There's not a huge heat sink effect in this cuz this is like a Delrin plastic or whatever, but you know, look, heat is actually doing something to it. So, there you go. We're getting up to a microamp, but uh

**Dave Jones:** Greg said that he was um seeing like tens of microamps or something. Okay, I'll ramp the temperature up. Okay, let's take it up to 250° C, and hopefully um I don't melt any of my um stick vice here. I don't actually know

**Dave Jones:** what the temperature rating of this is, but anyway, and 0.3 Whoa. Whoa. Whoa. Whoa. Yep. Yep. That's something's No. Something's going on there. Yeah, I won't do that anymore. Okay, let's try that again on a metal surface this time

**Dave Jones:** so we don't damage anything. Oh, yeah, it's faster. Yep. Yep. It's going higher. Here we go. Here we go. Now we're talking. Now we're talking. Sure enough, once you get into the tens of microamps range, you should definitely be able to like

**Dave Jones:** light a really high efficiency Ah, there we go. It's dropping back down. It's dropping back. There you go. So, it peaked at about 30. That is clearly going back down. Okay? So, I've heated that up. So, what uh Greg said

**Dave Jones:** is that um it didn't work after he'd already heated it once. So, I'll wait for that to cool down a bit, blow on it, and then we'll see Oh, look, it's gone negative. Isn't that interesting? So, there's some

**Dave Jones:** interesting physics going on here. Like my first thought was that yeah, it was like a uh thermoelectric effect with the dissimilar metals um like in the junctions of the leads and the capacitors and all sorts of stuff, right? There's bond wires in the leads.

**Dave Jones:** There's uh you know, there's actual uh metals used inside the leads in the And there's the foil in the capacitors and everything else, right? But if it goes up to like uh 30 microamps or something or whatever we saw there, and then it

**Dave Jones:** comes back down, it peaks up and then starts coming back down, then we've got something very interesting happening with um almost certainly the dielectric material in here as if it's like it's boiling off or something, and then it's

**Dave Jones:** not going to happen again. So, if we reheat this, and then we find it doesn't happen again, then that indicates that there's something in the capacitor, most likely the dielectric, that like is boiling off or something like that.

**Dave Jones:** Doesn't really affect the capacitance, cuz everyone knows that you can reflow these things. They're designed to be reflowed, not continuously, um and certainly not repeatedly uh reflowed, but you can certainly uh reflow them once under the board, and everything's

**Dave Jones:** hunky-dory. They they still remain their capacitance still remains, their ESR remains, everything else, right? Here we go, but will it get back to 30-odd microamps? And you saw like it's slow at first, but then it's sort of like the heat got

**Dave Jones:** internal, and then it says going up. Here it goes. Here it goes. It's accelerating, but will it get high enough again? It's not. It was going up faster than that before, wasn't it? It's But yeah, it's not getting It's not

**Dave Jones:** getting this high. That's it. And it's going to drop. Right, it reached eight this time. Aha. Got you. Got you. Got you. Got you. And that's just Oh, no. It's Yeah, it's it's it's going to drop. Oh, it actually

**Dave Jones:** started dropping drastically there. All right, it's cooled down again. Let's try it one more time. At 30-odd microamps the first time. I should be recording this. The only difference between science and mucking around is writing it down. Oh, yeah, no.

**Dave Jones:** Yeah, I don't think we're going to get there. I think there's diminishing returns now. Oh, no. No. No. Hang on. You can do it. And then it goes down. Down. Down. Up. Up. Up. Is that just me moving it? Is that just me like doing

**Dave Jones:** the airflow? Anyway, yeah, like we we take it off, and immediately it drops back down. Okay, let's try that again, but I've got the 121G W here, which allows us to uh just log the current here. And this will uh

**Dave Jones:** potentially present a uh different load than the uh BM786. Multimeters can have different um shunt resistor values on the uh microamp and current amp. So, let's do exactly the same thing again. So, I'll start the data logging. Sure

**Dave Jones:** enough, ramping up. 32. And we're going back down, back down, back down. Okay, it's cooled down enough. Let's log that again. It's a cycle number two. And we don't expect it to go back to where we 30-odd microamps we got before. It's going to

**Dave Jones:** have a much flatter top on it. Can tell you that for nothing now. Now it's dropping. It's going to be a much smoother, more stretched-out graph. The like it's not going to have a really high peak on it. And if you're wondering

**Dave Jones:** what we did to that poor little sucker, even though that was you know, like 250 was like a reflow uh temperature uh cycle. Pretty fairly typical. So, like 407 microfarads for the 470 um dissipation factor. What else have we

**Dave Jones:** got? We can give you the ESR on that bad boy. 0.464. And for reference, here's a brand-spanker. I haven't cycled it at all. In fact, its series resistance is actually um higher. There you go. So, yeah. Um haven't damaged this at all as far as

**Dave Jones:** you know, your regular parameters go. All right, I'm going to work with a known quantity now. Uh so, I went to the bunker. All of this stuff comes from the bunker. And here's some Panasonic uh jobbies, 220 mic, 16 V.

**Dave Jones:** And there you go. For those playing along at home, you can look them up. And uh you can get the data sheets. I don't think we're going to have a shortage of them for testing. And the Panasonic that's been sitting there for like 10

**Dave Jones:** years. Here we go. What happens if we hook it up? Whoa, look at that. That jumped up a lot. Wow. Okay, so here we go heating up the Panasonic. Yep, she's rising similar to the other one we had. So,

**Dave Jones:** two entirely different brands and it's going back down. So, what did it reach 16.something there and this is our second time. No, there you go. It's dropping back down. So, check this out. This is absolutely fascinating. We have

**Dave Jones:** the data here. The orange one here is the no-namer. That was the first test and then the blue was the second test. So, you can see how that the first test it peaked right up to like 33 microamps or something like that and

**Dave Jones:** then it just dropped fairly quickly and then here this must be where I removed the heat gun and then it dropped off and it went negative down here. But as you can see, the second test I've had to

**Dave Jones:** sort of like shift the data here to cuz I didn't like line up the exact you know thermal profile. So, they've just been shifted. You can see I think it does take a similar amount of time to get to

**Dave Jones:** the peak though. But then it just stays there. It's like it just stays there and then this must be where I remove the heat. So, then you got the Panasonic one. The gray one is the first test here and you can see it's

**Dave Jones:** kind of got like a little humpy sort of not a not a hump plateau of like a front porch so to speak and then it ramps up and goes off and it has a it doesn't have the same sort of nice profile that

**Dave Jones:** the no-namer does. It sort of like goes down a linear slope and then it's got a larger slope like this and then it goes negative and then it starts oscillating. Is there more data to that actually? Yeah, I thought there was. There it is.

**Dave Jones:** Yeah, there's extra data. It went like this. Now, I can't remember if I actually took the heat gun off at this point where it negative or if I kept it on there like that. But there's some interesting little negative action

**Dave Jones:** happening there. But anyway, the second test is the yellow one here for the Panasonic jobbie and it actually ramped up quicker if you you know, I don't know exactly where the heat started, but if you shift it over, yeah, it sort of

**Dave Jones:** ramped up to its peak quicker and then it sort of went down and then it did a sort of like a plateau kind of thing. So it's a different profile to what we got for the no namer. So that's interesting

**Dave Jones:** and these are the same heat, same heat flow. Same route, you know, roughly the same distance, all the conditions are basically the same into the same load meter and yeah, they're different profiles. So there's something happening there interestingly with the internal

**Dave Jones:** chemistry and or the physics. I don't know. It could be some obscure physics thing. It could be a combination of obscure physics and chemistry stuff. It could just be pure chemistry. It could be metallurgy type, you know, there

**Dave Jones:** could be some thermoelectric effect as I said happening there. It could be a combination of any of those or all of those. I don't know, but it's it's absolutely fascinating. Is it not? You can generate tens of microamps by

**Dave Jones:** heating up your electrolytic capacitors. And unfortunately, I haven't been able to find any LEDs. I found LEDs that work at 30 microamps when I put them on my current generator, they work fine. When I put them on the cap, either cap, they

**Dave Jones:** don't work. I found a red one, couldn't find a green one yet, but anyway, now the reason why my LEDs didn't light is likely because they're non-linear devices. Yeah, sure you can push that 30 microamps through, but if there's not

**Dave Jones:** the compliance voltage required, then like the actual voltage generated on the cap in this case, then well, they're not going to light. So I definitely have the LED that lit in room light with 30 microamps and it does nothing with this

**Dave Jones:** cap. So yeah, you got to get a specific like really high efficiency LED and stuff like that. So, it is, you know, don't be disappointed if you try this and it doesn't work. But, you saw Greg's LED actually light up, so

**Dave Jones:** I'm sure it works. I've just got to find one. So, yeah, an interesting follow-up experiment might be to actually plot the voltage as well as the current as well. So, then you can actually see the compliance voltage and the actual power

**Dave Jones:** delivered the power and the capable power actually delivered from this thing. It's not much, but it is enough to light up certain types of LEDs. But, that is interesting. I might have to ask one of the capacitor manufacturers. I'll

**Dave Jones:** reach out cuz I have a contact and we'll see if they have any theory that explains this. But, if you do or if you've got if this is like known thing and it's published somewhere or it's in some app buried away somewhere, then

**Dave Jones:** please leave it in the comments down below. So, thanks to Greg for finding that. It's absolutely fascinating. There's some weird stuff happening here. Something very interesting. So, if you want to experiment yourself, it's it's pretty easy to do. So, it's good

**Dave Jones:** fun and I might do follow-up videos on this if there's enough interest and things come to light. I'm here all week. Catch you next time.
