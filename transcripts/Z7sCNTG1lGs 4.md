---
video_id: Z7sCNTG1lGs
title: EEVblog #1059 - Quick 861DW Hot Air Waveform Measurement
url: https://www.youtube.com/watch?v=Z7sCNTG1lGs
source: youtube-asr
timestamps: {"0": 0, "1": 10, "2": 24, "3": 39, "4": 51, "5": 70, "6": 84, "7": 94, "8": 118, "9": 130, "10": 151, "11": 171, "12": 191, "13": 202, "14": 212, "15": 224, "16": 237, "17": 247, "18": 257, "19": 266, "20": 275, "21": 287, "22": 301, "23": 316, "24": 328, "25": 345, "26": 360, "27": 373, "28": 384, "29": 397, "30": 409, "31": 423, "32": 436, "33": 449, "34": 459, "35": 474, "36": 495, "37": 508, "38": 525, "39": 540, "40": 560, "41": 573, "42": 583, "43": 594, "44": 604, "45": 618, "46": 626, "47": 638, "48": 654, "49": 670, "50": 684, "51": 700, "52": 711, "53": 724, "54": 745, "55": 770, "56": 783, "57": 792, "58": 802, "59": 817, "60": 831, "61": 839, "62": 860, "63": 869, "64": 878, "65": 886}
---

**Dave Jones:** Hi, just a follow-up video on this quick 861 DW hot air re-soldering station. I'll link in the previous video down below if you haven't seen it cuz this might not make much sense.

**Dave Jones:** Cuz some people wanted me to do some measurements on this thing and so let's have a quick look at that. But first of all, I wanted to clarify this is actually the DW model and I actually got the spec which I overlaid on the previous video wrong.

**Dave Jones:** By default, the website was showing the DE model and that's apparently a more powerful model. That's 1200 watts as opposed to this 1000 watt unit and it's also the DE model is the 200 liter per minute air flow model.

**Dave Jones:** This one's only 120. Hence why if I actually take this out, air flow, if we actually go up, it's maximum is 120. So this is actually a direct read out in liters per minute, which is quite nice.

**Dave Jones:** So that's the DW model and it's the DE model that goes up to 200 liters per minute. So that's just a clarification. So technically, this actually has the same air flow 120 liters per minute as the Atin / whatever you want to what brand you want to call it.

**Dave Jones:** It goes under many brands, the 858 DW. So does that mean that you know, this is the same power as that? Well, no because I this one's a 1000 watts heater capability as opposed to 700 watts for the Atin.

**Dave Jones:** But that's not the only difference. The a lot of people say, well, if they're the same liters per minute and they're the same air the same heater power, they should be the same.

**Dave Jones:** Well, that's not the case. It's all about the well, a good lot of it that has an impact of course, but a good lot of it will be to do with the internal element design and how they can actually transfer and the heat sink design in there and the heat fin design and how they can actually transfer as the heat blows out over the element, how efficiently it can actually transfer

**Dave Jones:** from the element to the air. And uh so, your better quality irons um like this one, the Quick is definitely a better design and better quality iron than the Atten one.

**Dave Jones:** Um and that's why its performance was roughly about double I got in the previous video. And there's some people saying, "Oh, I didn't uh use the the same size nozzles and everything else, and I was waving the Atten around too much and whatnot." And that's going to have some impact, but in all the testing I've done and some quite a bit of it was off camera, uh playing around

**Dave Jones:** with this thing. Uh yes, this is definitely the more capable iron than the Atten. But, you'd expect it. Um it's just a better designed and uh higher-priced unit. I know price is not the only specification cuz Louis Rossmann, of course, has done uh tests on this one, and he says it outperforms the uh the Hakko and the Weller that cost like three times the price.

**Dave Jones:** So, that'll have to do with uh you know, like I said, the design of the element and the air uh fin attachments and stuff like that. And I've done a actually a bit of uh research, not in hot air guns, but uh solar air heaters cuz I designed my own uh solar air heater once, and that was all an optimization uh problem.

**Dave Jones:** So, as you actually uh push the air through the like this long circular snaking path of the solar air heater, the more surface area it has to actually pick up the heat.

**Dave Jones:** And if you've just got And if you have little fins inside there, it's a more efficient. Again, the more surface area you have, but then it's a trade-off with uh blocking the air flow and stuff like that.

**Dave Jones:** It's actually quite uh complicated how you can transfer air, moving air, onto like thermal surfaces. And the whole, you know, design of heat sinks with moving air flow in product design, it actually is quite complicated.

**Dave Jones:** And you know, things like this are quite complicated if you get right down to them. People think, "Oh, it's just an element and push some air through. It There's a bit more engineering involved in that.

**Dave Jones:** And sorry, I can't take this one apart. I don't want to ruin it to show you any you know, the actual design inside. Maybe if we had a sacrificial one, we could do that.

**Dave Jones:** But it's got like rivets on there that prevent me doing that down in there. But anyway, yeah, people think it's just an element and just a tube blowing some air motor to blow some air through.

**Dave Jones:** Well, no, there's a bit more to it than that that decides its performance. Anyway, um some people just wanted me to measure the waveforms and stuff. So, let's take a quick look at that.

**Dave Jones:** All right. So, what I've got is my Aim iProber 520. I've done a video on this. It's a very nice bit of kit. It costs a bit of money, but it's very nice.

**Dave Jones:** You can measure current using the clip-on toroidal attachment I've got here. We can actually just use it as a oscilloscope clamp meter. Basically, to turn our scope into a clamp meter to view the waveforms.

**Dave Jones:** And in this particular configuration, it gives out a well, the amplifier in here, the sensor and the amplifier give out a nominal 1 V per amp output. So, I've got that hooked into the scope here.

**Dave Jones:** And I've got this on the primary side of the filter in there. But I've also got a reference waveform captured from the secondary side there of the filter. I think somebody in the comments said that this filter was wired wrong or something like that.

**Dave Jones:** But no, everything's on the secondary side of the filter. Like it goes into the heating element and stuff like that. Anyway, the problem with Lewis's one that it made the lights in his lab flicker.

**Dave Jones:** And of course, the only you know, it's got a beautiful common mode filter in there. So, it can't be any like conducted RFI or something like that. So, it's got to be the the switching currents coming from the heating elements.

**Dave Jones:** And that would have to do with his you know the wiring configuration, the phase configuration, mains phase configuration in his lab and uh stuff like that. In fact, if this thing makes his lights flicker, I'm surprised that something else doesn't make them flicker, too.

**Dave Jones:** Because it's basically, as you saw in the teardown, it's just a triac in there and it's just a basic triac switching circuit with an RC snubber across it. And then, on top of that, we've got the filter in there, but yeah.

**Dave Jones:** So, anyway, it's got to be the the actual currents. All right, so let's actually check it out here. Now, I've actually captured a reference waveform here and that's this brown one here.

**Dave Jones:** It's I'll show you in a sec actually a live waveform, but I've captured that reference. That was on the secondary side of the filter. So, that was basically directly from the element.

**Dave Jones:** And And you can see, you know, it's with it's a classic triac type switching arrangement. And you'll see that these in in this case, we've got like a full cycle there and a full cycle there with a gap in between.

**Dave Jones:** And of course, that is, if you have a look at 5 milliseconds per division, that's 20 milliseconds across. That's 50 hertz, of course, cuz that's what triac circuits do in the heating element in this particular case, directly across the mains.

**Dave Jones:** So, that's all the triac does is switch the heating element off and on even in full or half cycles, as we'll see. So, I just captured that and where it's uh 2 amps per division here.

**Dave Jones:** So, 2 4 6, it's almost 8 amps peak. So, that's actually pretty beefy stuff. So, let's actually have a look at a live one. I'll actually turn on the element.

**Dave Jones:** So, now where the yellow waveform is our live waveform on the primary side. So, this is what's actually going out into the mains. And I've turned it on. I've only got like a speed of 10 liters per minute here.

**Dave Jones:** So, it's not much. And you can see that it's um if we we can like single shot capture that, and you can see that we've actually got a you know, sometimes it's a uh in this particular case is 1 and 1/2 cycles there.

**Dave Jones:** Sometimes you'll only get I think I've sure I've seen Let me capture it again. Oh, there we go. So, we've only got the half uh cycle there. So, the control algorithm has determined that, you know, it's it'll cycle this element off and on what it has to to keep to maintain the loop temperature that you've set it to, the set temperature on there, and that'll be based on the air flow as well.

**Dave Jones:** So, if you have higher air flow, you'll actually uh see that change. So, let me uh maybe let's go up, air flow up, and run it. So, that's air flow at the moment.

**Dave Jones:** That's a 10 50 L per minute. Let's go up to 200. You can hear that, so we should actually get a few more cycles on there perhaps. But uh anyway, and if we turn the air flow right back down, probably shouldn't need as many.

**Dave Jones:** There you go. It shouldn't need as many to maintain in this particular case 400°C, and you can see that it's not doing much at all at the moment. Just very occasionally it'll uh turn the element on and try and maintain that temperature.

**Dave Jones:** So, those current spikes, so let's actually single shot capture that. So, you can see that the filter's actually done a bit there. The amplitude is slightly less, probably you know, and it's going to take out any uh like slightly higher frequency stuff, but I don't really been playing around with this, and I don't really see any high frequency uh stuff in there.

**Dave Jones:** So, maybe that uh big nice common mode filter that they've got in the back of this thing, maybe it's not needed at all, but hey you'd have to do a full broadband uh compliance test and all that uh sort of stuff.

**Dave Jones:** But, it's a very nice touch to have one in there. But, so a mains filter like this simply isn't going to uh sort of like, you know, smooth all this out so that you don't get any transitions at all.

**Dave Jones:** That's not how it works, unfortunately. It's only designed for your more high frequency stuff. So, yeah, there you go. We have like 8 amp, almost 8 Well, no, coming from the mains, let's call that 7 amp peak.

**Dave Jones:** And this is for 240 V mains. Yes, I do actually have 240 V here in the lab. And you can see that the RMS current there is about uh you know, 2.6.

**Dave Jones:** I think it was going about uh 3 amps RMS or so. So, that gives us about, you know, a 700 W capability, roughly. But, hey, we didn't like fully like turn the heater on the full way.

**Dave Jones:** Okay, let's have a look at the RMS current here. If I try and ramp this right up. Here we go. I'll go up in temp. So, it's on mostly off.

**Dave Jones:** 4 and 1/2. Did it reach 4 and 1/2 amps there? Something like that. Maybe four. Four to four and a half. And of course, uh four and a half amps, that's just over 1,000 W.

**Dave Jones:** 1,080 or something. So, you know, like that's like basically meeting its spec in terms of the 1,000 W heating element capability in this thing. So, as you can see, it's just not always turning that element on and delivering the full power.

**Dave Jones:** It just needs to do it periodically to maintain the set temperature. So, let's do the same for the uh At 10. And look, I mean, there's just no competition in the in the engineering between these two.

**Dave Jones:** Oh, goodness. And of course, this is a totally different beast cuz this actually contains the motor inside here. It's not doing it in the base unit like the Quick and all of your other professional ones do and have the hose coming over.

**Dave Jones:** Very different. And here we go. We're got the At 10 up and running. You can see peak current considerably less. Let me turn it on and bingo, we get full sine wave.

**Dave Jones:** None of this uh triac chopping rubbish. We get the full sine wave when it's hit 10 amp. Hang on. Much lower peak power capability. So, to get our spec 700 watts, let's go here.

**Dave Jones:** It should be 2.9 amps. We're getting 2.6. You saw it there. Um so, this is not meeting its rated 700 watt capability. So, there you go. I hope you found that little follow-up interesting there.

**Dave Jones:** And yeah, the At Hand What was it getting? 620 watts or something? You know, it's not grossly under its rated 700 watt capability, but the Quick actually seemed to be doing maybe slightly at least meets its 1,000 watt rating, heating element rating, and uh maybe slightly over.

**Dave Jones:** So, it's a genuine rating. And it really I The Quick is just a much better unit. Yes, this kind of sort of, you know, does the job, but as I said in the previous video, if uh you know, the what they're 200 say $200 difference or $250 difference between these two, and this one you have to put longer on your particular device or your board that you're repairing, and you

**Dave Jones:** screw that up, and you're you know, you could ruin you know, a $500 job. You can easily ruin you know, $250 just gone. Bam, like that. So, and anyway, um I found the actual catalog for the tips you can get for the Quick as well.

**Dave Jones:** And it's got a huge range of them, BGA, quad flat packs, and all sorts of ones. Whereas, the At Hand is just a bit of a more of a toy.

**Dave Jones:** I don't know. You might be able to get some attachments for the At Hand as well. But, it's probably a whole bunch of you know, third-party add-ons cuz this is actually sold under you know, dozens of different brands.

**Dave Jones:** I don't actually know who the original equipment manufacturer is, whether it's At Hand or someone else. I can't recall, but so yeah, the problem with Lewis's flickering lights is basically is almost certainly I think the drawing the current from the triac.

**Dave Jones:** Just the switching triac peak currents, but almost every large power, you know, device heating element type device on the market works in a similar triac switching way. It does the same thing.

**Dave Jones:** So, you know, there could be something subtle in there you know, causing his lights to flicker, but if he probably puts it on a separate phase or something like that, that might fix it.

**Dave Jones:** Some other filtering, I don't know, might fix it. There might be other some other high frequency conducted or radiated. I don't think it's conducted cuz of that filter. Maybe there's, you know, some radiated stuff being picked up in who knows what common modes things somewhere else that it can like analyzing a problem like this can be real complicated.

**Dave Jones:** You start by just isolating you know, phases for one thing and you know, move it to a different circuit in the other part of the lab and stuff like that.

**Dave Jones:** My lab for example, one wall uses a different I don't know for whether or not it's a different phase, but it's different definitely a different circuit to the other one.

**Dave Jones:** So, you try and just move stuff around like that as a first port of call, but anyway, hope you found that interesting and if you did, please give it a big thumbs up.

**Dave Jones:** Catch you next time.
