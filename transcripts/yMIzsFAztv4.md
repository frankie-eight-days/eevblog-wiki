---
video_id: yMIzsFAztv4
title: EEVblog 1455 - Capacitors Produce Current During Reflow Soldering! WTF!
url: https://www.youtube.com/watch?v=yMIzsFAztv4
source: youtube-asr
timestamps: {"0": 0, "1": 18, "2": 31, "3": 42, "4": 57, "5": 73, "6": 84, "7": 100, "8": 111, "9": 130, "10": 145, "11": 159, "12": 174, "13": 194, "14": 206, "15": 223, "16": 232, "17": 240, "18": 254, "19": 266, "20": 281, "21": 295, "22": 306, "23": 320, "24": 328, "25": 351, "26": 363, "27": 377, "28": 395, "29": 405, "30": 416, "31": 426, "32": 439, "33": 451, "34": 464, "35": 478, "36": 490, "37": 501, "38": 518, "39": 532, "40": 545, "41": 555, "42": 564, "43": 574, "44": 587, "45": 600, "46": 623, "47": 633, "48": 641, "49": 663, "50": 675, "51": 689, "52": 709, "53": 728, "54": 740, "55": 754, "56": 765, "57": 774, "58": 795, "59": 808, "60": 818, "61": 834, "62": 848, "63": 857, "64": 868}
---

**Dave Jones:** Hi, I saw this on Twitter. Some leads are lighting up when they go through the reflow oven. Uh What the What's going on here? A lead across a capacitor, heated up, it lights up.

**Dave Jones:** I got to check this out. So, where does this come from? Well, I heard about this from Greg Daville on Twitter. Highly recommend you follow Greg. He does great like close-up macro photos of like SMD and soldering among other things.

**Dave Jones:** Really great. Anyway, he says, "Weird phenomenon. During reflow, some green lead power indicators are emitting slightly. Seems like maybe during reflow, solid polymer caps are having an effect on creating small electrical current.

**Dave Jones:** Does anyone know what this effect is called? Maybe some further reading." And he did a test with a 220 mic 50 V electrolytic surface mount cap like this, heat gun onto the cap with a lead, and sure enough, it lights up.

**Dave Jones:** So, very interesting. And Ian here pointed out this Stack Exchange article about somebody saw these leads light up in the reflow oven, but I suspect, if you notice, there's a thermocouple there.

**Dave Jones:** And the thermocouple looks like it might be touching a pad that's coincidentally near all those leads. So, I suspect that is not due to what we're seeing here cuz there's no capacitors.

**Dave Jones:** This is due to capacitive electrical coupling with if it is through the thermocouple, through the shielded bottom and everything else. So, I don't think anything's There's anything to see there, but there there there you go.

**Dave Jones:** I'll link in the thread down below, but fascinating. You can light a lead by heating up a capacitor. Hmm, let's do some experiments. I've got an ammeter. I will hook it up in a second.

**Dave Jones:** I'll show you that. It's on microamps range, and I've got a, you know, a selection of SMD electrolytics here. I've just chosen a 470 microfarad 16-V jobbie. I don't know the brand of these cuz this is one of these just generic cheap-ass kits.

**Dave Jones:** But it does have the split in the top there, which indicates that that is not a solid polymer capacitor. That indicates that it's an wet electrolytic type capacitor, which it looks like from the photo um similar to the one Greg's using.

**Dave Jones:** Somebody else on Twitter mentioned that it could be some sort of precharge / dielectric absorption of the capacitor. Link in dielectric absorption. Have I done a video on that?

**Dave Jones:** I'm sure I've mentioned it at least many couple of times in videos. Anyway, if I hook this up, I've just had this sitting here before. It was actually hooked up and shorted out with the load of the milliamp the microamp input here, which is what 1K or something like that.

**Dave Jones:** Um but anyway, I'm going to hook this up and watch watch the reading. There will actually be a charge. It jumped up to a couple of microamps there. So there is some sort of dielectric absorption charge building up, but it can't be that on its own because the lead would instantly just drain any of that away.

**Dave Jones:** Anyway, here we go. I've got my heat gun set to 100° C. So I don't want to, you know, take it to like reflow temperatures yet. I want to do it just a low temperature.

**Dave Jones:** So let's see what 100° C does. Here we go. Yep. Yep. Sure enough, it's going up, but not much. I mean, you know, 0.2 microamps. That's a sniff of an oily rag stuff.

**Dave Jones:** That's half a bee's dick. There's not a huge heat sink effect in this cuz this is like a Delrin plastic or whatever, but you know, look, heat is actually doing something to it.

**Dave Jones:** So, there you go. We're getting up to a microamp, but uh Greg said that he was um seeing like tens of microamps or something. Okay, I'll ramp the temperature up.

**Dave Jones:** Okay, let's take it up to 250° C, and hopefully um I don't melt any of my um stick vice here. I don't actually know what the temperature rating of this is, but anyway, and 0.3 Whoa.

**Dave Jones:** Whoa. Whoa. Whoa. Yep. Yep. That's something's No. Something's going on there. Yeah, I won't do that anymore. Okay, let's try that again on a metal surface this time so we don't damage anything.

**Dave Jones:** Oh, yeah, it's faster. Yep. Yep. It's going higher. Here we go. Here we go. Now we're talking. Now we're talking. Sure enough, once you get into the tens of microamps range, you should definitely be able to like light a really high efficiency Ah, there we go.

**Dave Jones:** It's dropping back down. It's dropping back. There you go. So, it peaked at about 30. That is clearly going back down. Okay? So, I've heated that up. So, what uh Greg said is that um it didn't work after he'd already heated it once.

**Dave Jones:** So, I'll wait for that to cool down a bit, blow on it, and then we'll see Oh, look, it's gone negative. Isn't that interesting? So, there's some interesting physics going on here.

**Dave Jones:** Like my first thought was that yeah, it was like a uh thermoelectric effect with the dissimilar metals um like in the junctions of the leads and the capacitors and all sorts of stuff, right?

**Dave Jones:** There's bond wires in the leads. There's uh you know, there's actual uh metals used inside the leads in the And there's the foil in the capacitors and everything else, right?

**Dave Jones:** But if it goes up to like uh 30 microamps or something or whatever we saw there, and then it comes back down, it peaks up and then starts coming back down, then we've got something very interesting happening with um almost certainly the dielectric material in here as if it's like it's boiling off or something, and then it's not going to happen again.

**Dave Jones:** So, if we reheat this, and then we find it doesn't happen again, then that indicates that there's something in the capacitor, most likely the dielectric, that like is boiling off or something like that.

**Dave Jones:** Doesn't really affect the capacitance, cuz everyone knows that you can reflow these things. They're designed to be reflowed, not continuously, um and certainly not repeatedly uh reflowed, but you can certainly uh reflow them once under the board, and everything's hunky-dory.

**Dave Jones:** They they still remain their capacitance still remains, their ESR remains, everything else, right? Here we go, but will it get back to 30-odd microamps? And you saw like it's slow at first, but then it's sort of like the heat got internal, and then it says going up.

**Dave Jones:** Here it goes. Here it goes. It's accelerating, but will it get high enough again? It's not. It was going up faster than that before, wasn't it? It's But yeah, it's not getting It's not getting this high.

**Dave Jones:** That's it. And it's going to drop. Right, it reached eight this time. Aha. Got you. Got you. Got you. Got you. And that's just Oh, no. It's Yeah, it's it's it's going to drop.

**Dave Jones:** Oh, it actually started dropping drastically there. All right, it's cooled down again. Let's try it one more time. At 30-odd microamps the first time. I should be recording this.

**Dave Jones:** The only difference between science and mucking around is writing it down. Oh, yeah, no. Yeah, I don't think we're going to get there. I think there's diminishing returns now.

**Dave Jones:** Oh, no. No. No. Hang on. You can do it. And then it goes down. Down. Down. Up. Up. Up. Is that just me moving it? Is that just me like doing the airflow?

**Dave Jones:** Anyway, yeah, like we we take it off, and immediately it drops back down. Okay, let's try that again, but I've got the 121G W here, which allows us to uh just log the current here.

**Dave Jones:** And this will uh potentially present a uh different load than the uh BM786. Multimeters can have different um shunt resistor values on the uh microamp and current amp. So, let's do exactly the same thing again.

**Dave Jones:** So, I'll start the data logging. Sure enough, ramping up. 32. And we're going back down, back down, back down. Okay, it's cooled down enough. Let's log that again. It's a cycle number two.

**Dave Jones:** And we don't expect it to go back to where we 30-odd microamps we got before. It's going to have a much flatter top on it. Can tell you that for nothing now.

**Dave Jones:** Now it's dropping. It's going to be a much smoother, more stretched-out graph. The like it's not going to have a really high peak on it. And if you're wondering what we did to that poor little sucker, even though that was you know, like 250 was like a reflow uh temperature uh cycle.

**Dave Jones:** Pretty fairly typical. So, like 407 microfarads for the 470 um dissipation factor. What else have we got? We can give you the ESR on that bad boy. 0.464. And for reference, here's a brand-spanker.

**Dave Jones:** I haven't cycled it at all. In fact, its series resistance is actually um higher. There you go. So, yeah. Um haven't damaged this at all as far as you know, your regular parameters go.

**Dave Jones:** All right, I'm going to work with a known quantity now. Uh so, I went to the bunker. All of this stuff comes from the bunker. And here's some Panasonic uh jobbies, 220 mic, 16 V.

**Dave Jones:** And there you go. For those playing along at home, you can look them up. And uh you can get the data sheets. I don't think we're going to have a shortage of them for testing.

**Dave Jones:** And the Panasonic that's been sitting there for like 10 years. Here we go. What happens if we hook it up? Whoa, look at that. That jumped up a lot.

**Dave Jones:** Wow. Okay, so here we go heating up the Panasonic. Yep, she's rising similar to the other one we had. So, two entirely different brands and it's going back down.

**Dave Jones:** So, what did it reach 16.something there and this is our second time. No, there you go. It's dropping back down. So, check this out. This is absolutely fascinating. We have the data here.

**Dave Jones:** The orange one here is the no-namer. That was the first test and then the blue was the second test. So, you can see how that the first test it peaked right up to like 33 microamps or something like that and then it just dropped fairly quickly and then here this must be where I removed the heat gun and then it dropped off and it went negative down here.

**Dave Jones:** But as you can see, the second test I've had to sort of like shift the data here to cuz I didn't like line up the exact you know thermal profile.

**Dave Jones:** So, they've just been shifted. You can see I think it does take a similar amount of time to get to the peak though. But then it just stays there.

**Dave Jones:** It's like it just stays there and then this must be where I remove the heat. So, then you got the Panasonic one. The gray one is the first test here and you can see it's kind of got like a little humpy sort of not a not a hump plateau of like a front porch so to speak and then it ramps up and goes off and it has a it doesn't

**Dave Jones:** have the same sort of nice profile that the no-namer does. It sort of like goes down a linear slope and then it's got a larger slope like this and then it goes negative and then it starts oscillating.

**Dave Jones:** Is there more data to that actually? Yeah, I thought there was. There it is. Yeah, there's extra data. It went like this. Now, I can't remember if I actually took the heat gun off at this point where it negative or if I kept it on there like that.

**Dave Jones:** But there's some interesting little negative action happening there. But anyway, the second test is the yellow one here for the Panasonic jobbie and it actually ramped up quicker if you you know, I don't know exactly where the heat started, but if you shift it over, yeah, it sort of ramped up to its peak quicker and then it sort of went down and then it did a sort of like a plateau kind of thing.

**Dave Jones:** So it's a different profile to what we got for the no namer. So that's interesting and these are the same heat, same heat flow. Same route, you know, roughly the same distance, all the conditions are basically the same into the same load meter and yeah, they're different profiles.

**Dave Jones:** So there's something happening there interestingly with the internal chemistry and or the physics. I don't know. It could be some obscure physics thing. It could be a combination of obscure physics and chemistry stuff.

**Dave Jones:** It could just be pure chemistry. It could be metallurgy type, you know, there could be some thermoelectric effect as I said happening there. It could be a combination of any of those or all of those.

**Dave Jones:** I don't know, but it's it's absolutely fascinating. Is it not? You can generate tens of microamps by heating up your electrolytic capacitors. And unfortunately, I haven't been able to find any LEDs.

**Dave Jones:** I found LEDs that work at 30 microamps when I put them on my current generator, they work fine. When I put them on the cap, either cap, they don't work.

**Dave Jones:** I found a red one, couldn't find a green one yet, but anyway, now the reason why my LEDs didn't light is likely because they're non-linear devices. Yeah, sure you can push that 30 microamps through, but if there's not the compliance voltage required, then like the actual voltage generated on the cap in this case, then well, they're not going to light.

**Dave Jones:** So I definitely have the LED that lit in room light with 30 microamps and it does nothing with this cap. So yeah, you got to get a specific like really high efficiency LED and stuff like that.

**Dave Jones:** So, it is, you know, don't be disappointed if you try this and it doesn't work. But, you saw Greg's LED actually light up, so I'm sure it works. I've just got to find one.

**Dave Jones:** So, yeah, an interesting follow-up experiment might be to actually plot the voltage as well as the current as well. So, then you can actually see the compliance voltage and the actual power delivered the power and the capable power actually delivered from this thing.

**Dave Jones:** It's not much, but it is enough to light up certain types of LEDs. But, that is interesting. I might have to ask one of the capacitor manufacturers. I'll reach out cuz I have a contact and we'll see if they have any theory that explains this.

**Dave Jones:** But, if you do or if you've got if this is like known thing and it's published somewhere or it's in some app buried away somewhere, then please leave it in the comments down below.

**Dave Jones:** So, thanks to Greg for finding that. It's absolutely fascinating. There's some weird stuff happening here. Something very interesting. So, if you want to experiment yourself, it's it's pretty easy to do.

**Dave Jones:** So, it's good fun and I might do follow-up videos on this if there's enough interest and things come to light. I'm here all week. Catch you next time.
