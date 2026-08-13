---
video_id: BjGdyajiSzM
title: EEVblog #915 - Dumpster Dive LCD TV Salvage
url: https://www.youtube.com/watch?v=BjGdyajiSzM
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 22, "2": 38, "3": 54, "4": 69, "5": 92, "6": 108, "7": 126, "8": 145, "9": 166, "10": 180, "11": 197, "12": 213, "13": 234, "14": 249, "15": 266, "16": 281, "17": 296, "18": 313, "19": 328, "20": 343, "21": 360, "22": 374, "23": 392, "24": 406, "25": 424, "26": 438, "27": 452, "28": 468, "29": 481, "30": 498, "31": 513, "32": 534, "33": 552, "34": 571, "35": 586, "36": 602, "37": 616, "38": 637, "39": 655, "40": 671, "41": 688, "42": 702, "43": 719, "44": 736, "45": 752, "46": 771, "47": 787, "48": 802, "49": 815, "50": 828, "51": 842, "52": 859, "53": 875, "54": 888, "55": 900, "56": 916, "57": 932, "58": 948, "59": 968, "60": 988, "61": 1004, "62": 1018, "63": 1034, "64": 1050, "65": 1068, "66": 1086, "67": 1102, "68": 1118}
---

**Dave Jones:** Hi, it's dumpster diving time again, and if you're subscribed to my EEVblog2 channel, you've no doubt seen this before. It's a 50-inch LG LCD TV, less than two years old, and I found it in the dumpster, and ta-da! Here's why. Look, it's had a big impact mark there, it's damaged the panel,

**Dave Jones:** we get some nice funky, um, look at that, it almost looks like lightning, or something like that. Anyway, um, they're very cool, they're artistic in their own right. Anyway, unfortunately that is beyond economical repair, be-ah, you'd have to replace the entire, uh, panel.

**Dave Jones:** So I thought we'd, uh, take it apart, see if we can actually use the, uh, LED backlight out of this thing for, I don't know, something, a big LED light panel, or something like that. Take the LCD glass out, and maybe use it as a big light panel.

**Dave Jones:** It's worth a shot anyway, and we might have some other usable parts in there, I don't know. Could be interesting. Let's go. It's a 50LB5610 for those playing along at home. So let's give this a boil, shall we? There's a few screws in here,

**Dave Jones:** and, uh, no, I don't have my cordless screwdriver, it's at the bunker, so meh, whatever. Um, a lot of people will complain, yeah, I should get another one. Just something therapeutic about taking out screws, these are rather short ones, actually. Now, of course, we've seen inside many, uh, TVs, this won't be, um, this'll be pretty unexciting.

**Dave Jones:** Uh, plasmas are more exciting, I might link in, uh, videos to my plasma teardowns, they're much more exciting, because high voltage, high power drivers, you know, take like 500 watts. These things take, bugger all, a 50-inch one like this might take 100, maybe.

**Dave Jones:** But, um, yeah, there's no high voltage driver stuff, it's just the LCD panel, uh, with the chip-on flex drivers in it. And, uh, what else have we got? We've got, um, well, there's going to be a power supply, of course, that'll be a typical single-sided thing.

**Dave Jones:** There'll be a LED driver, because this is a LED backlight. Is to see if we can, uh, convert this, maybe, into like a, a white light panel. You could use it for, uh, like a light box, for example, like old-school light box, good for seeing through printed circuit boards, and stuff like that.

**Dave Jones:** Or any arts and crafty stuff that you happen to do, uh, that needs a, a light table. Have I missed one? No. There we go. We're in like Flynn. Beauty. BVO. What does BVO mean? I don't know. Anyway, as you can see, there's bugger all in here.

**Dave Jones:** I'll give you a closer look. Now, you'll have to forgive the lighting in this video. I don't normally shoot from this side of the bench, but, yeah, there are other benches, I don't want to have to clear them off. Anyway, this one was clean, so, uh, the light's coming in from this direction here.

**Dave Jones:** That's why everything looks dark and shadowy and stuff like that. Whereas, usually, my videos are lit from, like, behind, like this, like, uh, above and behind, like this. And that's what makes them look, uh, so good. Anyway, we have our, uh, our speaker, um, boxes here.

**Dave Jones:** There are our little speakers in there, and they're just using those for some bass boost. Um, they, they would be sort of strategically designed. It is an LG, so it's, you know, life's good, right? And, anyway, um, as I said, a tiny digital board like this,

**Dave Jones:** bugger all, and the, uh, main power supply like this, and Bob's your uncle. Here's the two main boards up close. Look at this, uh, very low-profile, uh, switching transformer in here. I like that. That's pretty funky. Anyway, um, nice big, uh, bridge rectifier and its own little, uh, heatsink there.

**Dave Jones:** And, uh, there's our main filter cap. What's that? That looks like a Sam Young brand. But, look, um, surge protect. Rather interesting. I, I don't know. Do they have something in them? I would like to actually rip that out and have a teardown of that.

**Dave Jones:** But, look, they've got eyelets in here. Look at that. That is interesting. The fuse here, and the main capacitor. Do they just lift out? No, that was a bit of a red herring. I can't, uh, I can't seem to lift that out. I've got a screwdriver under there.

**Dave Jones:** Tried to lift it, didn't want to break it, but it didn't seem to budge. Anyway, also got it on this fuse over here, too. Wow, eyelets. Anyway, apart from our main logic board, our power supply, and almost certainly our lead driver board as well,

**Dave Jones:** uh, we've got our T-Con board. That's where I've done a video, uh, debugging that. You get, uh, where I had an intermittent fault in the cable that went to, uh, the T-Con board on a, uh, LCD, uh, TV. Anyway, common fault, the, uh, T-Con boards.

**Dave Jones:** But from this power supply, uh, here, going over to the main logic board, it doesn't split off anywhere else, so that'd have multiple layers, 12 volts, 3.35, all that sort of jazz. Um, and this one going off here, which must be going to the lead backlight.

**Dave Jones:** Lead backlight driver around here. And on the back of the panel here, we've got, uh, an info tag from New Optics Limited. They're actually a Korean company who specialize in, uh, backlight, uh, technology for LCD TVs, so they're the ones doing this, the NC500.

**Dave Jones:** And those wires are the lead driver, because it says lead there. Oh, as if it wasn't bleedingly obvious anyway. Together and rip out the electronics, because we don't need that, we only need this main power supply with the lead driver. Presumably the power supply will still work

**Dave Jones:** with the, uh, load disconnected for, um, all that, but you could leave it running if you really wanted to. It's just pissing away some more power. Before we take it apart, what I've got set up now is my, um, AIM-TTI iProber there with the, uh, wire clamp, wire attachment

**Dave Jones:** just over, uh, one of the leads. Looks like there's two lead outputs, presumably one on, uh, either side would be my guess. So there's the little, um, doodad that comes with it. Very handy little device, the iProber. I've done some, uh, stuff on that before.

**Dave Jones:** Let's plug it in. And I just want to see if it's, uh, constant current drive or, uh, PWM going to those leads, just for curiosity's sake. Whey! There we go. Look at that. There we go, it is PWM, and 120 hertz or thereabouts.

**Dave Jones:** And if you want to know the current, what you've got to do is, uh, set the probe to times 1, because we're not using a times 10 probe, it's a direct output. Uh, read the data sheet for the thing, and it tells you that it's, uh, 1 volt per, um, amp output.

**Dave Jones:** So if we have a look here, it's, uh, volts peak to peak. Uh, 200 and, let's call it, uh, 230 millivolts there. So, uh, 230 milliamps. I took out the speaker, and a nice touch. Look, little, uh, rubber rings in here, which, uh, press into the chassis down here,

**Dave Jones:** just for some, uh, vibration isolation. So that's very nice. I don't know, you might salvage those speakers for something, maybe. Eh. And I'd say we're going to want to keep our power button, uh, on the base of the thing down here to switch it off and on.

**Dave Jones:** Because then, uh, let's stand by on this thing, I don't know, it might be, you know, half a watt, if it's a good design or something like that. And here's our T-con board, so we definitely want to get that out. In fact, you could probably maybe resell that on eBay.

**Dave Jones:** I don't know, you might get 10 bucks for it. Maybe someone wants a, uh, T-con board. Don't forget the, uh, to include the ribbon cables with it as well. And we can get these panels off here. Here's the, one of the driver boards for the, uh,

**Dave Jones:** or the, well, it's not really a driver board, the, uh, the chips themselves are actually, as I said, chip-on, uh, flex, going to be further inside the panel. But that's a, um, that's one of the connecting boards, so we just, there's two of those.

**Dave Jones:** Uh, they don't make it like an entire meter long like that, because, well, it's just too hard. Split them into halves like that. Much easier to manufacture on, you know, most pick-and-place machines and, and PCB panels and stuff like that. These little white plastic clips here,

**Dave Jones:** I think these are going to be part of the white, uh, reflective, uh, backing surface, which we need to keep. And it does help if you get all the screws. D'oh! Okay, so I'm going to take the bezel off, because that's real easy.

**Dave Jones:** That's a, that is a metal bezel. You can see the glass panel down in here like that. I can actually lift it up, and, uh, but we're going to have to get off this white tape, because that is holding down, ta-da! One of our drivers.

**Dave Jones:** There we go, that's actually a chippy. Now, it looks for all the world like our panel is just going to lift off. Look at that. What a bobby dazzler. And careful, because we've got the boards attached. Ta-da! It's off, and look what we're left with.

**Dave Jones:** A beautiful white, uh, light panel. It's gorgeous, isn't it? And there's our panel. Check it out, it's still, it's got the crack in there, but it's not, I mean, no, no, it's still protected, because this has a laminate film on the outside, but yeah, I wouldn't go trying to snap it

**Dave Jones:** or anything like that. It could be in serious trouble, but, uh, yep, we can safely remove that. No wuckers. And one of the first problems I've noticed is that you're not going to want to use this as, like, a ceiling panel, because it does, not sure if you can see that,

**Dave Jones:** but it is going to bow. It's just flapping around in the breeze there. Um, it's probably just being supported on the edges and its own weight will, uh, make it come down. So really, vertical, uh, panel, or flat for working on big stuff.

**Dave Jones:** So I didn't have to disconnect those like I thought. Anyway, I plugged the lead back in. I'm going to reconnect the processor board, because we don't want that. That's just pissing away power. Um, I'm going to plug it in and, um, see if she works.

**Dave Jones:** Alright, let's turn it on, see what happens. Yes, I am bare feet in the lab. Alright, I've got, uh, fixed exposure on the camera, so let's give it a bell. Ah. Wah, wah, wah, wah. Let's try that again with the processor board, uh, plugged in this time.

**Dave Jones:** And, ta-da! Look at that! Beautiful. It's not very white. To my, I'm not sure what that's showing up like on camera, but, uh, to my mind, that's not very, Oi! That, that dimmed a bit, didn't it? Was that my imagination? I'm not sure if you'll see that on camera.

**Dave Jones:** But yeah, you've got to have the processor board plugged in, otherwise it doesn't, uh, presumably, that's where the 120 hertz is generated from. And, uh, or, you know, something that enables it. So yeah, you've got to have the processor on. But there, there you go, we've got ourselves a LED panel.

**Dave Jones:** Beauty. And that's a nice, even light on that, too. I mean, you, offhand, I can't tell you where the, uh, LEDs are on that thing. The sides, the top, all around. What's he, like, there's no real hot spots on that at all. Amazing.

**Dave Jones:** And trigger warning, if you don't like fast flicker, if you don't like fast flicker, turn it off now, I'm going to change the frame rate of the camera. And that's one two thousandth of a second. Ha, ha, ha. Oops. And of course, if I set it to 120 hertz,

**Dave Jones:** it synchronises precisely with the LED backlight. Zero flicker whatsoever. But above and below that, yep, we can get the flicker. And if you're wondering what kind of light output we're getting, at, well, at one metre away, that's about a metre. The centre axis, we're getting about, let's call it,

**Dave Jones:** uh, 550, 550 lux or thereabouts. And we'll just compare the light output to the, uh, panels you've seen in my videos before. I've got these up as my, uh, studio lights on the ceiling. This is a high efficiency, uh, 60 watt, 600, uh,

**Dave Jones:** 6,000 Kelvin, uh, panel. So we'll get the difference. And at a metre, this one's rocking about 1,200. So let's, let's call it double. And sure enough, my 60 watt nominal panel draws just over 60 watts, 63 watts. And if you want to see the VA, there we go,

**Dave Jones:** 65.3, power factor 0.969. Very good, these panels. Or, well, the power supply that comes with it. Which, for those playing along at home, is a liffard. And our dodgy brother's hacked TV LED panel, uh, 40 watts, almost bang on. Uh, VA, 50.92, so that gives us a power factor of, uh,

**Dave Jones:** 0.8 for this particular LG, uh, 50 inch LCD TV that we've got here. So that includes the electronics, uh, of course, so who knows how much power they're, uh, still chewing and stuff like that. But, yeah, um, that's not too shabby at all.

**Dave Jones:** Half the light output at a metre for, eh, it's not half the power. Um, but still, it's, you know, it's, it's better than I thought it would be, I think. And if you do want to use this as a, uh, light panel, then you want to get the weight down

**Dave Jones:** out of the thing, but, unfortunately, most of the weight is in the steel, uh, chassis. I have weighed the LCD panel itself, and it's only about 2 kilos. So, that's all you're saving by taking out that, but you still need all the diffusion plate

**Dave Jones:** and the metal backing panel and the electronics and, yeah, the plastics and everything else. So, you're not saving a huge amount of weight there. And, of course, one of the good things you can use a light box for is for seeing through boards

**Dave Jones:** to see the different, uh, layers. In this case, you can see the, uh, ground planes in there really very nicely on that board. Look at that. Anyway, million and one uses for a light box. I mean, I don't know why you'd want a 50-inch diagonal,

**Dave Jones:** uh, light box, but, meh. Anyway, you might. And because we can, let's have some fun with my Spectra 1 spectrometer. You haven't seen this, uh, before. I've had it for a little bit, and I want to do some cool videos with it. And, um, it's basically one of, uh,

**Dave Jones:** one of the cheapest spectrometers, um, on the market. It's not particularly cheap. It's like 800 euros or, uh, something. But it's basically a fiber-optic, uh, interface. And there we go. There's our fiber-optic interface. But they give you, like, a little nice little, uh,

**Dave Jones:** lens with it as well that we can, uh, put this directly on our panel and, uh, have a look at the light spectrum from it. Awesome. This is the software that comes with it. And it shows us the spectrum. If I point it up

**Dave Jones:** towards one of the lights I've got here in the lab, we can see the color spectrum. It'll show you the peak response. And we can actually have a look at the monitor here. And watch this. I'll show you something cool. Okay, so if we point it to the white,

**Dave Jones:** we get green and some blue and some yellow down in there. If we just look at the blue, bingo, the others vanish. And if we just look at the green, the others vanish as well. Neat. Alright, now let's take a look at our commercial panel,

**Dave Jones:** just as a reference. Now I'm not kidding when I have to put this all the way across the room and it's still peaking, unfortunately. Haven't totally figured out this software yet, but I believe that this is as high as it goes. So, yeah, we are saturated.

**Dave Jones:** But anyway, you can see the spectrum with the blue, the green, and the yellow peaks there. That's very typical of a white LED. I want to actually do a separate video on this so we can actually get a capture. Like, we'll just get a single shot sequence

**Dave Jones:** of that. There we go. That one's not bad, actually. Spot on. So that's our reference. And this is a nominal 6000 Kelvin panel, CRI greater than 80. You can see our blue peak there at 450 nanometers, another one at 532 in the green, and

**Dave Jones:** peaking around 600 in the yellow over there. Now if we have a look at our Dodgy Brothers panel here, I'll capture that. Here we go. Stop. Take single shot capture, and whammo, the color rendering index isn't nearly as good on this thing as our other

**Dave Jones:** commercial panel, and I guess you wouldn't really expect it to, and it does have kind of the... a bluey tinge, so let's try and get the two side by side and compare them. Okay, I'll have a play around with our Dodgy Brothers panel, and I'll

**Dave Jones:** see if I can... I'll spare the details, but I'll see if I can capture the same amplitude. You can see similar response, but the peaks and troughs are different. And here we go. After a bit of fiddling, I was able to capture almost

**Dave Jones:** the same intensity. The other one was about 135 peak in the blue, this one's... let's call it very similar. Now, I don't want to get into a tutorial on CRI, or color rendering index here, but have a look. On the left hand side here, we've got our

**Dave Jones:** TV, our hacked TV LED backlight, and on the right we've got our commercial panel, not a really top quality one as far as CRI goes, just a greater than 80. As a reference, 100 is like proper daylight, the sun. But you can see

**Dave Jones:** that even with the same intensity, virtually the same intensity scale here, you can see that the blue of the hacked TV is very prominent, and it dips all the way, practically down to zero between the blue and the green, whereas our commercial LED panel

**Dave Jones:** at a nominal 6000 Kelvin has a lot more energy content there between the blue and the green. That's why our hacked TV looks very bluish, because the blue, the energy in the blue there dominates, it's not spread out, it's not more of a full spectrum, and

**Dave Jones:** here's a spectrum comparison of daylight, for example, and see it's got a broad energy content right over the whole thing. And that's why, yeah, it doesn't look like it's a nice white, looks very bluish, and you can get regular compact fluorescents and things like

**Dave Jones:** that that do a similar thing. Now if you haven't seen these films before, there's actually a lot of technology which goes into these. You can see there's four separate layers here, on the bottom we have a diffuser sheet, it's like really thick. But then we get onto

**Dave Jones:** these films, and these are absolutely fascinating, and check it out, even at 1 milliamp these things light up okay! And if I change it, I can change that to 0.1 milliamps, so 100 microamps, and even 10
