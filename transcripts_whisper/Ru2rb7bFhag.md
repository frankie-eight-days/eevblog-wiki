---
video_id: Ru2rb7bFhag
title: EEVblog #1016 - Crude Multimeter High Voltage Overload Testing
url: https://www.youtube.com/watch?v=Ru2rb7bFhag
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 0, "2": 44, "3": 64, "4": 84, "5": 102, "6": 121, "7": 145, "8": 160, "9": 175, "10": 187, "11": 203, "12": 219, "13": 232, "14": 249, "15": 263, "16": 281, "17": 294, "18": 313, "19": 328, "20": 348, "21": 362, "22": 385, "23": 405, "24": 427, "25": 444, "26": 468, "27": 488, "28": 510, "29": 530, "30": 551, "31": 567, "32": 589, "33": 609, "34": 637, "35": 654, "36": 670, "37": 693, "38": 706, "39": 721, "40": 748, "41": 770, "42": 786, "43": 805, "44": 822, "45": 840, "46": 857, "47": 875, "48": 887, "49": 905, "50": 919, "51": 937, "52": 950, "53": 965}
---

**Dave Jones:** Hi, I thought I'd have a play around with this that you've seen before. I'll link in the video, if you haven't seen it, it'll be at the end or down below. This is the Unity UT513 insulation tester. And this thing actually goes up to 5 kilovolts.

**Dave Jones:** So, 5 kilovolts, 2.5, or 1,000 volts. So I thought, aha! Could this be potentially useful for, you know, doing some very crude impulse overload testing on multimeters? So I thought I'd give it a try. But to do this, you have to be able to see the waveform.

**Dave Jones:** Yes, it can generate 5,000 volts into a high impedance, that's its job. But when you put it into a multimeter, they've got the MOVs in there that will clamp down and potentially, like, essentially go low impedance, short this thing out. And we just don't know what is going to happen.

**Dave Jones:** Most likely it's going to clamp to the MOV voltage inside here and this would have enough output impedance to actually continue to drive that. Anyway, I thought it'd just be interesting to have a look. So I don't actually have anything that can measure 5 kilovolts here at the lab.

**Dave Jones:** Yeah, I can cobble together a do-it-yourself high voltage probe. I'll link that in down below. And my EEVblog HVP70 probe, if you haven't seen it, sexy as, 70 megahertz. But it's only a, basically a 700 volt probe. It's designed for mains, you know, safe mains use and stuff like that.

**Dave Jones:** Discount coupon code linked in down below, by the way. Anyway, so what I've got, I got this from Charles at Triotest. Thank you very much, Charles. He loaned this to me. It's the Pintec HVP15HF. Yes, it's a high voltage probe. Let's have a quick squiz at it.

**Dave Jones:** Curiously, on the card here, it says 50 megahertz, 3 dB bandwidth, 1001 attenuation ratio. Basically, 15 kilovolts DC, 30 kilovolts peak, or 10 kilovolts RMS. But if you go in here to the manual, curiously, it says it's only 40 megahertz and only 10 kilovolts with a 20 kilovolt peak.

**Dave Jones:** So I don't know what's going on there. Anyway, bit of a discrepancy. Anyway, it's a fairly cheap and fairly nice high voltage probe. So this will be more than good enough for measuring the 5 kilohertz coming from this puppy. So let's have a look and see what we get.

**Dave Jones:** Alright, so what I've got is I've actually set my probe here to 1000 to 1. You can set that, this is on the Rodin Shorts RTB2004. So we're 1 kilovolt per division now. So I'm just going to go ahead and single shot trigger that.

**Dave Jones:** Trigger that. I've got it set to 5 kilovolts. Let's switch it on and see what we get. I haven't got it hooked up to the multimeter, so it's just hooked up directly to the probe. So there's basically no load on there except the 100 meg.

**Dave Jones:** Oh, let's try that again. Alright, one more time for the dummies. Here we go. Bingo! There it is. And our meter down here, I'll turn that off and be careful, is showing 100 meg. So that's, it's nominating, that's nominal input impedance. So it's bang on.

**Dave Jones:** And you can see that we've got a fairly, what are we at, 20 milliseconds per division. So it takes, you know, 60, 70 milliseconds to ramp up and switch on here. So obviously it's doing, it's not, I can't remember the tear down, which I'll link in down below.

**Dave Jones:** It's obviously not like ramping up and then like using a relay to switch it on. It's actually ramping up the output. It would have been, that's not really what I wanted, unfortunately. I wanted it to build up the high voltage to the capacitor bank,

**Dave Jones:** and then when you press the test button to, boom, discharge. And that's not the input capacitance of the probe either, because the input capacitance is only 1 picofarad. So, you know, it's bugger all. So that's going to have bugger all effect on the ramping up there.

**Dave Jones:** So if we just go in here, let's go in and have a, have a squeeze. You can actually see all the switching noise on there, which you expect, you know, which is fine for an IR meter. You know, it is what it is, basically.

**Dave Jones:** But, yeah, there you go. It is actually significantly above the 5 kilovolts, though, according to this. I mean, 1, 2, 3, 4, 5. It's like, geez, you know, it's like at least 5.5, 5.7 kilovolts, something like that. All right, so let's try that again.

**Dave Jones:** But let's hook up the meter this time. So I've got the probes hooked up to there, and then the, well, the output of the IR tester hooked up to there, and then the high-voltage probe in parallel with that. So let's give that a burl.

**Dave Jones:** And I have actually tested this before. I know that the BM235 does actually survive this, but I didn't have a scope probe to actually do it. So here we go. Let's single-shot capture. And test, 5 kilovolts. Boom, there we go. Ah-ha, we've got some clamping.

**Dave Jones:** Look at that, no overshoot whatsoever. Bummer, because that's really what I wanted. So if we actually have a look at that, you can see it ramp up and then do some funny business. Anyway, you can see the internal oscillation in there for the switching converter,

**Dave Jones:** but there is no, there is no overshoot there whatsoever. And we're on 500 volts per division, so 500, 1,000, 1,500, about 1,800 volts. It's obviously being clamped by the meter there, because the output of the insulation resistance tester should be capable of more than that.

**Dave Jones:** But yeah, I was hoping to get like the 5 kilovolts and then boom, you know, but these things clamp ridiculously quickly, but the whole idea, the MOVs inside the meter do, but the whole idea was that I was hoping that it would charge up

**Dave Jones:** the capacitor bank inside and then boom, dump the energy. So I can't remember what the deal is there, but yeah, we've just got this slow ramp up, so that's no good. Anyway, the fact is the meter does survive, so still okay, but yeah, it's not the big surge overload thing that I wanted,

**Dave Jones:** because if you look at the proper test waveforms, the impulse waveforms for the cat testing on a meter, then they actually have a specific response over X number of microseconds and stuff. This is nothing like that. I just, you know, it's just very crude attempt at, you know,

**Dave Jones:** potentially doing it as like a go-no-go test for, you know, meters to see if they survive. And in case you're wondering, yes, new 121 GW EEVBlog meter coming out reasonably soon-ish. Anyway, it also has survived, but I haven't captured the waveform yet, so let's do exactly the same again.

**Dave Jones:** So this was the existing waveform for the BM235, so I expect a similar sort of clamping inside the 121 GW, or any multimeter with MOVs for that matter, that will clamp it down. So let's have a look and test. Boom. Oh, look at that.

**Dave Jones:** That's interesting. Wow. Look. That's the 121 GW just beeping due to overload condition. You can see the little display there. So I'll turn that off, and wow, look at that. It's jumped back down and it's jumped up again, so that's kind of like a more severe test, I guess.

**Dave Jones:** Let me take that out, let me take the scale out a bit, and we'll redo that, shall we? Let's give that a squiz. No! Okay. It's fine. So what's going on there? Have we got some sort of intermittent thing? Anyway, it is clamping a very similar voltage,

**Dave Jones:** and a very similar way to the BM235, which is exactly what you'd expect, and the meter survives just fine. But that's really... Yeah, why did we get that weird waveform? Did we have some... Oh, I remember there's a big high-voltage relay in the output of this thing.

**Dave Jones:** If you look at the teardown, and maybe that's... maybe that had some contact bounce or something? But anyway, that's really quite strange. Eh, we didn't see that again. Weird. Anyway, what we've got now is the poster child for cheap meters these days, the Anang AN8008.

**Dave Jones:** And I have tested this, and it did actually survive, but there's something... before I got the probe, but there is something interesting that happens to it. So let's actually do this. Okay, so 5 kilovolts, exactly the same. Let's go, and let's test it.

**Dave Jones:** Whoa! Look at that! And I'm not sure if you can hear that, but that is arcing over inside. It is hideous! It is absolutely hideous, but look at what we've jumped up to! Unbelievable, I'd better turn that off before it dies in the arse.

**Dave Jones:** It is obviously continuing to arc over there, just arc over. And you actually... that manifests itself as a high-frequency noise inside that thing. I'll see if I can capture the noise. Alright, let's try it again. 5,000 volts, got the external mic. Oh! Meter just turned off and died.

**Dave Jones:** This is not good. We've got some segments frozen on here, and it doesn't seem to do anything. Have we killed it? Has some, like, back EMF into this thing killed it or something? I don't know, I've done this several times, and it wasn't a problem.

**Dave Jones:** Damn! We might have killed it! No, we're actually good to go, we're back in action. So let's try that again, just took the batteries out. Some bloody soft-button crap. Anyway, try it again. Wow, yeah, we've killed... have we killed it? Stop! E-stop! Whoa!

**Dave Jones:** No, it seems to be still working. I've got to check the cow, but it seems to be doing the business. Let's open it up and have a look. Anyway, on the aiming, we are actually getting up to, like, 3,000 volts, so 1,000, 2,000, actually 3,500 volts in that initial climb,

**Dave Jones:** and then about, you know, 1, 2, almost, you know, 3,000 volt peaks on there. So, yeah, if we can survive that, that's not bad. So I don't actually expect to see anything on the top side here. I think it's arcing over in the range contact switches,

**Dave Jones:** and then I've done a video on this, demonstrating this beautifully, and I'll link it in at the end. Check it out, because it's absolutely brilliant. All right, so let's try that again, 5 kilovolts, here we go. That sounds horrible. Now, unfortunately, we can't power this up with the cover on,

**Dave Jones:** because then the range switch has the contacts, and it'll cover up everything else. So we're going to have to run it with it off. Remember, this meter does not have any MOV protection, so it's not doing any clamping. So the clamping is somewhere else, in diodes or whatever.

**Dave Jones:** It does have one PTC in there, which can limit the inrush current, but it's not doing any voltage clamping. Anyway, let's do the 5 kilovolts again, and see if we can get some arcing across those switches. Woo-hoo! There it is. There's the failure point.

**Dave Jones:** Oh, you can actually see some of the burn pit marks in there, from where it's arced over. Anyway, let's try it again. This is going to be great, watch. So as you can see, the little Anang 8008 actually survived that just fine, in quote marks.

**Dave Jones:** But don't go saying, look, this is fantastic, this $25 meter, you know, like, survives these 3.5 kilovolt pulses, these, you know, horrible pulses up here. No, it is, yeah, it does, but that's not the point of the cat ratings and everything else. The meter that we've got here, what I thought this might be able to do

**Dave Jones:** is to charge up its capacitor bank inside, and then dump the energy, impulse it into the meter. I was hoping it would do that, but basically all we've got is basically just a high voltage power supply generator, which then just clamps internally in meters,

**Dave Jones:** like, in good meters, like the BM 235 and the 121 GW, that actually have the MOVs inside, the metal oxide varistors that do the clamping, or gas discharge tubes in other meters, like Gossen that use GDTs, similar sort of thing. So in these meters, you saw that it actually safely clamped the voltage,

**Dave Jones:** so then the PTCs and other input protection resistors and other diode clamping can do their job. The Anang actually doesn't have that, doesn't have any MOVs in it. It's just got the PTC, so it's not surviving through good engineering, whereas something like this is surviving through proper engineering,

**Dave Jones:** proper independent UL certification testing and everything else, right? It's designed, those MOVs are doing their job clamping it down so that then the PTCs that come afterwards can protect the device and the input divider resistors. Yeah, this thing did survive this, but no, it doesn't make it a good meter.

**Dave Jones:** It's got no MOV protection, so we were just, you know, it's actually not that hard to protect against just a simple high voltage with input protection resistors and stuff like that. You don't necessarily need clamping MOVs just to do that, but the whole point is to dissipate energy.

**Dave Jones:** This has no ability to dissipate high voltage overload impulse energy, whereas something with MOVs that's safe and designed to do it does. So this is not a good test for that. But anyway, I just wanted to have a play around and see the Unity meter.

**Dave Jones:** It didn't quite do what I want, but that was fascinating. We found a fascinating result with an un-MOV protected meter. And you saw that the other ones, you know, were clamping nicely at the 1800 volt level, because these normally have like, you know,

**Dave Jones:** they might have like two 900 volt MOVs in series or whatever, and then they clamp at the 1800 volts or whatever, particular rated MOVs that you have inside these things. But that's typical, under 2 kilovolts. And then the rest of the input protection can do its job easily and safely.

**Dave Jones:** The MOVs are designed to dissipate the energy. So there you go, I hope you found that interesting. And if you did, please give it a big thumbs up for engagement. And as always, comment down below. And I'll link in those videos at the end here, check it out.

**Dave Jones:** The teardown of this was pretty interesting. It's not bad, it's got quirky software-y, you know, lock-up issues, which was seen here and in other videos. But you know, for a 5 kilovolt insulation tester, it's not too shabby. And thanks for Charles at TRIO Test for loaning me this high voltage probe.

**Dave Jones:** I'll link it in down below. It's a couple of hundred bucks. And I'll also link in my, which I haven't done a teardown of yet, my HVP70 probe, and there'll be a discount code down below for that one. But I've got to do a video on that.

**Dave Jones:** So if you're looking for a professional UL-listed probe, I didn't do this video just to plug this, but it's here, so why not? Yeah, I haven't really advertised this yet, but quite a lot of people have bought it already. In fact, my first shipment is almost sold out.

**Dave Jones:** So there you go, I'll link it in down below. That's for safe high voltage differential probe measurement on mains type stuff. So different to what we are doing here, really. Anyway, catch you next time. Thanks for watching.
