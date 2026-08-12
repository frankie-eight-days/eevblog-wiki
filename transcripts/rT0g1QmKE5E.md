---
video_id: rT0g1QmKE5E
title: Brymen BM2257 MOV Leakage Testing
url: https://www.youtube.com/watch?v=rT0g1QmKE5E
source: youtube-asr
timestamps: {"0": 1, "1": 17, "2": 31, "3": 45, "4": 64, "5": 77, "6": 90, "7": 102, "8": 116, "9": 130, "10": 146, "11": 160, "12": 176, "13": 188, "14": 204, "15": 218, "16": 240, "17": 253, "18": 266, "19": 281, "20": 300, "21": 312, "22": 333, "23": 348, "24": 365, "25": 382, "26": 396, "27": 412, "28": 432, "29": 449, "30": 473}
---

**Dave Jones:** Hi, some people on the EV blog forum have been talking about the leak of potential leakage current at high voltage in the new BM 2257 multimeter with the MOV configuration that I just released a video this morning on the

**Dave Jones:** main channel. So this is the input configuration here and in voltage mode we're basically using this path here and we've got three MOVs in series like this. So these are a CNR brand varistor or MOV as they call it metal oxide

**Dave Jones:** varistor, that's what it stands for. They're a 5D621K. So there's two of those in series, that means they're normally 620 V rated each and then there's then there's another one which is a 561 and the one in there

**Dave Jones:** just means one like an 10 in there. So it's 560, so 560 V. So we've got a total nominal clamping voltage of 1800 V there. So in theory, right? Not in practice, but in theory they should start to conduct at 1800 V. So obviously

**Dave Jones:** this is way over the 1000 V rating of the meter. In fact, well, this is only 600 V CAT III rated, but it measures up to 1000 V. In fact, it can go over that. I've actually done a video measuring

**Dave Jones:** that. I can link that in. And of course these won't have like a really sharp instant turn on. It doesn't actually work like that, but I normally they're designed to of course protect the input circuitry of the meter over here from

**Dave Jones:** any you know high voltage transient. So that's what all the UL testing is designed to do. They put input transients on the input here, very you know various like half wave forms and stuff like that, really you know big

**Dave Jones:** peak energy stuff in there to see if the MOVs can actually survive that well and the meter can actually survive that overload protection. But these MOVs, these are going to have a leakage current through them. So you know we've

**Dave Jones:** got our nominal 10 megaohm input impedance there. So what happens to our nominal 10 input impedance at say 1000 V? Well, it's interesting. So let's measure it. So you can actually get this entirely from the data sheet and this is

**Dave Jones:** the post by Fluffy Dust. I'll link in the data sheet down below for these CNR brand MOVs. It has these characteristic curves in here which is basically a voltage versus current down here and this is they've split it down here. You

**Dave Jones:** can see this is when it's at max clamping voltage. So this is how much current it'll actually clamp through and over here is what we're interested in. This is the leakage current. Now, because as I said, we have them in

**Dave Jones:** series like this, if we put 1000 V here we're pretty much going to have an even voltage split across here. We're not 100% sure, but let's just assume it's an even voltage split across here. So 333 V per MOV here. So if we go to our leakage

**Dave Jones:** current graph here, these are the characteristic curves for the different models. So we're looking at the third one down, the 621K and the fourth one down, the 561 here. And so it splits off down here as well. So third and fourth.

**Dave Jones:** So I've put in 333 V. So I've put a line across there and then where it intersects with the particular characteristic curve for that MOV, then we drop that down and we're down here at 10 to the minus six. That's one microamp

**Dave Jones:** there. So 1 2 3 4 5 6 7 8 9 and this is 10 microamps here. So one microamp here, this one where it intersects, that red dot there is three microamps and that one is five microamps. So let's just

**Dave Jones:** take the worst case of five microamps here. Using Ohm's law, that's going to be 200 megaohms equivalent resistance at 1000 V because remember we're 333 V per MOV. So yeah, 200 meg, that's pretty high. So if you put 200 meg across here in parallel

**Dave Jones:** with effectively in parallel with your 10 megaohm input impedance through here down to ground then basically that should not have much impact at all. You can go through the calculations. 200 meg in parallel with 10 meg is about 9.5

**Dave Jones:** meg. So what happens in practice? Well, we don't actually know. That's why we're going to measure it. Let's go. So in theory this is going to work. We should see 10 megaohms. So we're going to be able to calculate that based on the

**Dave Jones:** current reading. So I've got the current meter in series with the 10 megaohm input impedance on the new 2257 here and you see I'm feeding in 100 V and at 100 V it's basically bang on there, right? We expect 10

**Dave Jones:** microamps, that's 10 megaohms equivalent. Just use Ohm's law. So as we increase this voltage here up to 1000 V, we expect this to this current leakage current to increase because it's the extra resistance of those effective resistance of those MOVs in parallel

**Dave Jones:** with the 10 meg. So it's dropping from 10 megaohms. So expect that to go up. So let's actually see what happens. I'll use my Keithley high voltage source here and here we go. So I do know that this

**Dave Jones:** survives at 1000 V. In fact, it survives on way over 1000 V. I've tested it. So anyway, let's go up 200 V. We're still looking at basically 10 megaohms, right? It is not increasing. So 400 V, nope. 499, there you go, five 600 V, 700 V. We

**Dave Jones:** are not increasing. We are not increasing our current here. So that's interesting, isn't it? There you go. It's still effectively staying at 10 meg, you know, give or take the little bit of error in there and whoa, 1000 V, there it is. So it's

**Dave Jones:** actually better than predicted. We predicted that it should drop to what is it? 9.5 meg, which should go up to like 105 or something microamps on here, but it doesn't. It's still effectively 10 megaohms input impedance. Now I can go higher cuz this goes all

**Dave Jones:** the way to 11. Look at this. And look at that, even at 1100 V it's still effectively 10 megaohms. I mean I can put that into the confuser here and get the precise value and that's 10.02 meg. So like it's still

**Dave Jones:** it's it's as if those MOVs aren't there. Now I can actually go higher than that. I can actually take it to 1200 V if I do the other dials. There you go, 1200 V. Still no problem whatsoever. So it looks

**Dave Jones:** like Brymen have chosen these MOVs and designed this so that leakage is not a problem even at 1200 V. So yeah, there you go, tested. Oh, for those curious to see the AC, let's check it out cuz I've got a high

**Dave Jones:** voltage AC generator as well. 100 V, there you go and 200 won't go into the calculations, but knock yourself out. 300 V, oops, it tripped there. It's a bit touchy, my EDC high voltage reference standard. And there you go. So yeah, there you go,

**Dave Jones:** the current's a little bit higher than expected. It's interesting, 500 V. It it takes time to settle down here when I switch it. It's just the nature of the response loop of the standard. 600 V, still pretty 10 megaohms-ish,

**Dave Jones:** isn't it? 700 V. Oh, there you go, 72 microamps. 800 V. So 82.6 microamps. Interesting, 900 V. So yeah, now the leakage looks like it starts coming into play, but really that's nothing to quibble about. So 1000 V AC

**Dave Jones:** 104 microamps or 103.6. There you go, 1100 V AC. For those curious, that is 9.63 meg. So I'm still not a big deal at all. No worries. Catch you next time.
