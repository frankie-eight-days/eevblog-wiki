---
video_id: KFCRB4d991E
title: EEVblog #162 - Ceramic Capacitor Piezoelectric Effect on an Oscilloscope
url: https://www.youtube.com/watch?v=KFCRB4d991E
source: youtube-asr
timestamps: {"0": 0, "1": 22, "2": 52, "3": 62, "4": 86, "5": 96, "6": 115, "7": 132, "8": 142, "9": 164, "10": 172, "11": 186, "12": 197, "13": 207, "14": 221, "15": 233, "16": 245, "17": 258, "18": 272, "19": 287, "20": 296, "21": 314, "22": 329, "23": 340, "24": 359, "25": 379, "26": 394, "27": 407, "28": 419, "29": 435, "30": 450, "31": 466, "32": 482, "33": 503, "34": 523, "35": 532, "36": 545, "37": 566}
---

**Dave Jones:** Hi, welcome to the AAV blog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, I'm Dave Jones. I've got my Tektronix oscilloscope here, and I'm going to show you a rather interesting effect that you may not have seen before, or you've heard of, but you may not know that it actually applies to the humble oscilloscope probe.

**Dave Jones:** I've got my standard Tektronix 200 MHz P2200 probe here, and let's take a look at this effect. Okay, I've got my TDS 1012 digital storage oscilloscope here. The uh single channel, I've got it set up to 100 mV per division, 500 microsecond time base set to normal trigger, and the trigger level's at about 50 mV or thereabouts, and I've got my probe here set to uh times 10 position.

**Dave Jones:** I've taken off the uh ground probe and the um tip as well, because if you put the tip on, you'll notice that we uh pick up a fair bit of noise if we do that.

**Dave Jones:** So, we'll just take that off, and watch this. Look at that. Look at that effect. I'm just gently tapping that probe on the desk there, and you can see that there is an an actual uh shock response a stand a pretty standard shock response that is picked up by the probe.

**Dave Jones:** And you'll notice that this will change a bit depending on the surface I've got, obviously. If I tap it on the bench here, that's a hard surface, so that's generating a lot of uh G's into the actual probe itself.

**Dave Jones:** Now, if I put it onto the uh antistatic mat over here, which is spongier, it's a similar kind of response. It's uh slightly It's the same frequency response, but uh the response is a little bit dampened because of the surface we're actually doing it on.

**Dave Jones:** Now, one of the keys to this is the orientation, the physical rotation orientation of the probe when it actually strikes the surface like this. Now, if if I've got this switch on the other side here over here, that's the one that's the position that generates the most amount.

**Dave Jones:** Now, if I just rotate it so that the switch is on the top there, so I've rotated 90°. It still does it. We get a different response and it is dampened.

**Dave Jones:** And if we rotate it 90° again, so we're 180° where we were from before, you notice that there's once again, very little shock response. And we rotate it another 90° and we're getting back there, but we have to have the probe around facing the other side to get that effect.

**Dave Jones:** And if you're wondering if times one or times 10 position makes a difference, well, we'll put it on times one here and we'll do it again. There it is.

**Dave Jones:** It really doesn't make much difference at all. And if you're wondering what sort of voltage levels we can get out of this, well, this is 500 mV per division and let's do that, shall we?

**Dave Jones:** I can get that to well over 2 V peak-to-peak. And we don't have to just tap it on the bench, either. We can actually tap it with a screwdriver and use it as a set of jump sticks.

**Dave Jones:** Neat. But as you can see, the response is certainly a fair bit different. And you're wondering what this little waveform here was, which we picked a glimpse of there.

**Dave Jones:** It has nothing to do with this shock response, but I I thought I'd show you this anyway cuz it's another rather interesting effect. If you put the probe near the screen like that, you can pick up the backlight signal.

**Dave Jones:** You can pick up the EMC from the backlight on the screen like that. And it's rather interesting. That each each oscilloscope will have its own a waveform for the backlight inverter.

**Dave Jones:** You're wondering what happens when we short out the probe. Well, I've got some alfoil here as we call it in Australia. You guys might call it something different. But let's short that short that probe out like that.

**Dave Jones:** There we go. It's shorted out with some alfoil and let's try it again. We can still get the response, but it's significantly significantly lower amplitude and it is a different response.

**Dave Jones:** Once again, we have the orientation the same around like that. And as you can see, it is it's A, it's changed frequency and B, it's a it's a it is a different response with multiple transitions negative and positive.

**Dave Jones:** And here's a cleaner response of that. I've turned the voltage level up and as you can see, you can see the really sharp drops on this waveform. It is remarkably different.

**Dave Jones:** And it's not just the probe, either. If we just set the probe down there and we tap the input compensation circuit like that, bingo, you can get another response.

**Dave Jones:** It's much lower in amplitude. It's totally different, but it also has a shock response. So, what's causing this? Well, it's probably a little bit complex, but what it ultimately is likely to come down to are the ceramic capacitors used in these probes for compensation.

**Dave Jones:** This probe here will have a ceramic compensation capacitor in it. Um some probes, this one doesn't, but some probes will actually have an adjustment pot there as well. So, they'll have an adjustable capacitor as well.

**Dave Jones:** And also in the in the probe connector over here has a similar sort of circuit. So, I've got my little Dave CAD drawing here of a multi-layer ceramic capacitor.

**Dave Jones:** And this is how they're constructed. They're actually That's why they call them an MLCC, multi-layer ceramic capacitor, because they are made up of multiple layers of multiple layers of metal between the dielectric um uh the dielectric material.

**Dave Jones:** And they're quite a complex construction. And they are highly These ones are highly susceptible to what's called the piezo-electric effect. And I won't go into detail of what the piezo-electric effect is, but it it is is basically um if like a a shock or vibration sensor will be a similar thing.

**Dave Jones:** It'll be a piezo-electric material like this, like a capacitor, essentially like a capacitor, but it's tuned for uh you know, a flat response, a flat shock response. But uh multi-layer ceramic capacitors can have exactly the same effect.

**Dave Jones:** It's not nearly as linear, but it can certainly generate some high voltages. And it works both ways. If you apply a shock or a vibration into the capacitor, it will generate a voltage.

**Dave Jones:** But likewise, it will also generate sound output if you input a specific frequency at a high enough level. It will actually generate a sound or what's called sing. Um it's called singing.

**Dave Jones:** These capacitors will actually generate a noise. So it works both ways. Now, the capacitors used in these probes are a very low value. So they're likely in NPO/COG capacitor, which is not a multi-layer ceramic capacitor.

**Dave Jones:** And they're not supposed to be susceptible to the piezo-electric effect. But apparently, they are. I you would have to go into much more detail to actually dissect these to actually figure out exactly what happened but and what's happening there.

**Dave Jones:** But based on the orientation, it's likely to be the internal capacitor. Now, don't confuse this piezo-electric effect with what's called the triboelectric effect, which typically applies to cables. Now, it may be having an effect on this as well.

**Dave Jones:** There may be a combined effect, but I can actually get that if I turn the volts per division down, okay, to 50 mV there, and I whack this cable on there, I can actually get an effect to happen.

**Dave Jones:** And that's probably the triboelectric effect, or maybe it's coupling up through into the probe. If I hold the probe and dangle it like that and sort of isolate the vibration going up, it's I can still get it, but it's maybe it's actually coupling into the the input circuit there, but yeah, I don't know.

**Dave Jones:** It's a totally different effect, but it's rather unusual. So, there you go. That's a rather unusual effect, which you may have to watch out for. If you've ever seen If you ever see like an impulse response like that, you know it might actually be something to do with the probe and somebody bumped it, tapped it during probing, or something like that.

**Dave Jones:** You might have to be careful. Might be a trap for young players, but give it a go. It's rather interesting. Try it out with your probe on your scope and see what you get.

**Dave Jones:** Catch you later. Hi guys. This is actually my entry for the my tektronixscope.com competition, which runs until the end of April. So, if you like this video, please go to the site and vote for it.

**Dave Jones:** And you can actually vote once every day up until the end of April from a different IP address. So, please get on there and vote for me if you like it, and hopefully I can win this thing, because now that I'm a officially an unemployed full-time video blogger, I think I need to.

**Dave Jones:** So, really appreciate it, guys. Catch you later.
