---
video_id: V93Rnco-wKg
title: EEVblog 1414 - MicSig DP10007 High Voltage Probe - Turning it up to 11
url: https://www.youtube.com/watch?v=V93Rnco-wKg
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 30, "3": 46, "4": 60, "5": 73, "6": 87, "7": 100, "8": 115, "9": 147, "10": 161, "11": 178, "12": 193, "13": 208, "14": 221, "15": 232, "16": 248, "17": 261, "18": 269, "19": 285, "20": 301, "21": 313, "22": 329, "23": 339, "24": 350, "25": 366, "26": 380, "27": 392, "28": 404, "29": 421, "30": 438, "31": 457, "32": 472, "33": 491, "34": 506, "35": 524, "36": 540, "37": 561, "38": 575, "39": 587, "40": 602, "41": 618, "42": 631, "43": 646, "44": 665, "45": 685, "46": 699, "47": 713, "48": 725, "49": 739, "50": 753, "51": 767, "52": 782, "53": 794, "54": 813, "55": 826, "56": 840, "57": 856, "58": 871, "59": 886, "60": 903, "61": 919, "62": 931}
---

**Dave Jones:** Hi, you've no doubt seen the EVblog HVP7070 meg differential uh probe. It's been in many videos. I've been selling this on my store for many years. I do actually have it now, have it back in stock, by the way. So, you can actually get it.

**Dave Jones:** Link down below. Anyway, it's one of the best high voltage probes on the market. It's designed by a Taiwanese company called uh Sapphire. And they actually uh rebadge uh their brand under all the top names. I mean, uh te- hang on.

**Dave Jones:** Hang on. Yep, there we go. LeCroy AP031 differential uh probe. Exactly Well, this one's actually uh 20 MHz bandwidth. My one's 70. But, um yeah, this is a Sapphire probe. And LeCroy and many other top brands in the industry rebadge

**Dave Jones:** Sapphire, cuz they make the best uh differential probes on the market. Anyway, it's not particularly cheap, though. It's, you know, it's it's a fairly decent investment. But, it is a top performance, top quality uh probe. So, anyway, um

**Dave Jones:** I saw that uh Mix Sig had actually released Whoop, upside down, all the electrons are going to fall out. A uh that they released their own line of lower cost uh differential probes. And I thought, "Ooh, okay, we'll have a squiz

**Dave Jones:** at them." But, unfortunately, they didn't have They only had two models, and none of them had uh the divide by 10 and divide by 100 uh range, which is what my HVP70 does. And I reckon this is better for general purpose use, for

**Dave Jones:** lower voltage use on lower voltage switch mode power supplies, or for just general mains use. The others are literally high voltage differential probes. They go into like the kilovolt range and stuff like that, which is great if you work on that uh sort of

**Dave Jones:** stuff. But, anyway, um yes, this is common mode uh plus minus 700 volts, linear range plus minus 700 volts on the divide by 100. And that's good enough for like a DC plus ACP. Anyway, that's good enough uh range for like 240 volt

**Dave Jones:** mains stuff. And of course, 110 Yankee uh mains stuff. So, more than good know, 6 months later or something it was, they came back and they released um this, which is you can buy it for general sale, and it's it's been

**Dave Jones:** available for a while. It's the DP10007. And sure enough, has the times 10 and times 100, or divide by 10, divide by 100. And it's and it performs pretty well. The spec sheets, I won't bother showing you, but they're

**Dave Jones:** identical practically identical. They matched every single spec. Now, I was actually going to offer this one for sale on the store, cuz it is significantly cheaper than the industry standard, so to speak, the Sapphire probes. But unfortunately, when

**Dave Jones:** I tested this, it did have a problem with the common mode rejection ratio, the CMRR. And it wasn't even close to meeting its spec. And I think some people on the EEVblog forum have confirmed that this is well. Anyway, the

**Dave Jones:** Mixig got to work on it, and they say they think they have actually fixed that issue, and apparently a new model is coming out. I it'll almost certainly be the same number, but it'll have like, I don't know, some sort of hardware tweak or

**Dave Jones:** something that fixes the common mode rejection ratio. But apart from that, it's not a bad probe. And I was going to sell it on the store, but because it had that issue, I didn't, and I kept on selling my Sapphire, my trusty Sapphire

**Dave Jones:** probe. Anyway, so people wanted to know, "What's the actual rating of this thing?" And that's what this video's about. I thought I'd actually test it, because I have my high-voltage AC standard here, which you can go up to

**Dave Jones:** 1,000 volts AC only at like 1 kHz. I can feed in an external frequency, but it only goes up to like couple of kHz tops or something. So, anyway, this will allow us to input up to 1,000 volts RMS into this and see where this

**Dave Jones:** sucker clips. Let's go. Oh, by the way, it does come with all the accessories. They are very large though. Like, you know, like the really high voltage stuff, not very very useful for you know, getting in there on

**Dave Jones:** the PCBs and stuff like that in the giant crocodile clips. Look at that. It's enormous.

**Dave Jones:** So, here's the specs for those playing along at home, the DP10007. Maximum differential test voltage is rated as DC plus AC peak and some people on the forum seem to have verified that that is the case. And on the divide by

**Dave Jones:** 100 range, we're talking 700 volts DC plus AC peak. Now, of course, it's not going to due to the nature of how these things are actually designed and I've done a teardown of the and a reverse engineering of the 7 HVP70 differential

**Dave Jones:** probe and this one will the Mix Equal work exactly the same thing. They got a big input resistor compensated resistor divider network and stuff like that. So, it's not like you go over that and you magically going to blow up your probe. I

**Dave Jones:** don't think that is the case. So, anyway, we're going to take it up here with our AC voltage standard and see what's what. And yes, some people have complained that it's not great having the fixed leads on the long leads on the

**Dave Jones:** unit like this cuz that affects its high frequency performance. And yeah, I agree. It would have been better if they had like banana jacks on there. I have asked them about that, but I don't know. They don't really seem interested in

**Dave Jones:** redoing it cuz they'd have to redo the tool the casing and the tooling and the whole damn thing. But anyway, that's no different to the uh Sapphire probe. So, it it is what it is. So, we'll plug that

**Dave Jones:** in there, and what do we get? Sure enough, we get our 10 V AC RMS there. So, we're on the uh times 100 mode. So, yeah, let's take it up. And yes, this bad boy can go all the way to

**Dave Jones:** 11. Beauty. All right, so we've got 100 V RMS there. And by the way, the output voltage of this is going to clip at uh 7 V. So, there you go. So, I think that's what we're going to see here. We're

**Dave Jones:** looking for where at what point it actually clips. And when it exceeds that, like like I'm not going to take this thing to failure, okay? I don't even think I have the voltage to take this thing to failure. So, yeah, we just

**Dave Jones:** want to see where it clips. Now, unfortunately, I can't just dial this up. Like, I can change to 200 V and but well, it doesn't go instantly. There is some settling time. This thing's all analog goodness. So, and occasionally,

**Dave Jones:** it trips out like that. Um so, I've got to reoperate it like that. And bingo, we're now at 300 V. This This is RMS, of course. We don't Yeah, there's our peak-to-peak. 800 V, 850 V, sorry. 400 V,

**Dave Jones:** 500 V, 600 600 V. Oh, yeah, yeah, yeah, we're starting to clip there. And 700 V, you can see that we're clipping, right? I'm going to take this sucker up. So, let's call it Let's call that clip Yeah, that is definitely clipped. You

**Dave Jones:** can see it's clipped. So, it clips at like 500 and 56570. It just happens to be right on the edge there, doesn't it? 580 590. Let's say it can go up to 580 V before it RMS before it clips. 590,

**Dave Jones:** I'm pretty sure that is clipping. And it's giving us an overload flash there. You can see that. It's actually flashing that it's overloading. So, it does have a clip indicator. That's really very nice. Now, let's go back to 580. No,

**Dave Jones:** still It still thinks it's clipping. 550, still clipping. I'll find the point where it stops. Turn the studio lights off a bit. Okay, we're solid. We're at 420. 430 440 450. Just wait a bit. No. 460. It did

**Dave Jones:** seems to have a hysteresis cuz it It only turned off when I went back down to 420. So, Oh, 470. There you go. So, 460 Oh, no. No. No. No, it's good. Ah, that was just the uh settling time. This That

**Dave Jones:** was just the output uh settling time. So, 470 RMS. 480. Yeah. Okay, so let's just I'm not care if it's 475 or whatever. Okay, roundabout yeah, 4 470 uh RMS it'll go up to, but we saw that we still got well

**Dave Jones:** over that on the voltage here. So, let's go up. 580. It was another another 100 V RMS before the actual output waveform clipped. So, that's interesting. All right, I'm going to take this sucker up. I think I may

**Dave Jones:** have actually done this, but 600 V 700 V RMS. Okay. 800 V RMS. 900 V RMS. 1,000 V RMS. We're not blowing this sucker. I'm going all the way to 11. Here we go. 1,100 V RMS. As I said, yeah, you're not

**Dave Jones:** just going to magically blow it. No problems whatsoever. It just clips, so it still works. And take it back down to 500 and Bob's your uncle. No worries. Oh, by the way, of course there could be some degradation in the performance with

**Dave Jones:** frequency as well. So, this is only at 1 kHz, obviously, but it just shows that you're not going to blow the ass out of the thing. Oh, by the way, I've just put the probe back to 1:1 here, so you can

**Dave Jones:** see the actual output voltage. You know how it said 7 V maximum output voltage? Well, yeah, we're actually plus minus 7. We're 14 V peak. So, it does at least do the plus minus 7. So, we're at 500 V

**Dave Jones:** RMS, by the way, and if we go up to where we clipped, which was 580, wasn't it? Or slightly under that, 16 V and then we start to clip once we get above That's 590. So, 580 V there. So,

**Dave Jones:** yeah, it'll actually go to 8 V instead of the 7. So, that's actually over spec on the actual output voltage going into your scope. So, there you go. I hope I've answered that question. This is just like for basically the forum people

**Dave Jones:** who are commenting on this particular probe. And as always, the EEVblog forum, the number one destination for test equipment on the entire interwebs. I'm telling you, if you want to talk about test equipment, it's the place to do it. There's even a

**Dave Jones:** test equipment anonymous, in case you've got, you know, psychological problems collecting test equipment, which is quite common. Anyway, yeah, EEVblog forum link down below for this particular probe, anyway. But, yeah, it's cool that it gives you like an overload indicator there. Flashy

**Dave Jones:** flashy, but it's at like 470 or 480 V when its actual output clipping occurred at 580 V. So, and as you saw, it survived up to 1,100 V RMS. No wuckers. Rubbish. Everything has user serviceable parts inside it. All right, I can't

**Dave Jones:** finish this video until I open the damn thing. Um, not sure how, though. Ah, sneaky bastards, there's some trimmers under there. Even sneakier. So, here we go. We're in. We've got a metal shield covering the input section and

**Dave Jones:** the two input high voltage resistor strings as you'd expect. So, once we flip that over, I expect to see a whole whole bunch of there through probably SMD jobbies all in series and maybe some compensation caps across them just like

**Dave Jones:** in any high voltage diff probe. This looks like our output driver, does it? We've got the buttons on the top with the uh LEDs there to light them up. And oh, by the way, the strain relief, it's pretty good. That's not too shabby at

**Dave Jones:** all. And your metal threaded inserts everywhere. There's five screws to get this thing off. And there you have it. We've got ourselves a DC to DC converter there. No surprises whatsoever. That's an isolated jobby. That's an 0512. So,

**Dave Jones:** that'd be 5 V in and plus minus 12 V out isolated, of course. That's how you get your plus minus 7 V or 8 V as we've measured swing on this thing. Got a regulator up there. And that stuff on

**Dave Jones:** the bottom, that's got to be additional regulation as well. That's not part of the output driver cuz the output driver comes from up here. There's our output termination resistor. And what is that jobby? There you go. That's a THS3091.

**Dave Jones:** That's a high voltage low noise current feedback op amp. None of your standard op amp rubbish. Current feedback jobby. Really high bandwidth. That'll do up to 200 MHz at a low gain, of course. Um so, what's the output

**Dave Jones:** gain? Maybe 10 or something. I'm not sure. Anyway, that's certainly a suitable output driver. We've got ourselves a fair income relay there. No wackers. Made in Japan. All the best stuff's made in Japan. Although, the probe's made in China. So, there you go.

**Dave Jones:** Go figure. Anyway, um yep. Here's our differential amplifier. There's our differential amp. A THS4631. That's a high speed FET input op amp. So, we've got a couple of trimmers there and a little tin turn jobbies. Got a couple of variable caps up here. Of

**Dave Jones:** course, at this point you expect to see complete symmetry. So, in the two variable caps up there, as I said, there's your high voltage string there. There's your caps for each run. The reason that they have to use separate

**Dave Jones:** resistors cuz each resistor is only like, you know, 200 odd volts for that package size. I would have expected a larger package size than that. Actually, so I don't know. Maybe a bit how you doing. Um anyway, you saw it. It did actually

**Dave Jones:** survive the voltage. So, no wuckers. And yes, as I said, capacitors on there to compensate. But yeah, actually what is that? I can't Is that four meg like the I think the sapphire one's four meg. So, yeah, that's exactly what you'd expect.

**Dave Jones:** It's just that yeah, I'm surprised not to see larger packages there for bigger voltage offset. Anyway, there'll probably be some diodes in there for protection as well. Is there anything on the bottom? No, I don't Actually, ah they're probably relying on the input

**Dave Jones:** clamping of the op amp. I would say cuz I don't see any diodes in there, do you? And that micro there makes sense. It's another one of those busy bees that we saw in the previous video with the mixing current

**Dave Jones:** clamp the teardown thingo. So, yeah, that makes sense. You're going to reuse the the same family micro with in you know, most of your products where it's suitable. Anyway, there's not much else around there. That's about all she wrote, really. So,

**Dave Jones:** there you go. It's got a differential high voltage input string, differential amplifier, output current mode op amp cable driver, and just some control and miscellaneous stuff, and Bob's your uncle. So, there you have it. That's inside the DP10007

**Dave Jones:** high voltage differential probe. As I said, EVBlog forum link down below to discuss this thing and I'll keep you updated if I ever put it on the store if I get the like updated version with the common mode rejection ratio and I'll

**Dave Jones:** probably do some tests on that to confirm. So, anyway, liked it, give it a big thumbs up. Comment down below. Catch you next time.
