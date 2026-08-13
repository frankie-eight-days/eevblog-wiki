---
video_id: MNDisp8IKe0
title: EEVblog #529 - HP 35660A DSA Upgrade Investigation
url: https://www.youtube.com/watch?v=MNDisp8IKe0
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 41, "3": 57, "4": 73, "5": 89, "6": 105, "7": 121, "8": 145, "9": 165, "10": 185, "11": 206, "12": 226, "13": 246, "14": 266, "15": 278, "16": 294, "17": 315, "18": 331, "19": 351, "20": 375, "21": 396, "22": 420, "23": 440, "24": 452, "25": 472, "26": 488, "27": 509, "28": 529, "29": 545, "30": 561, "31": 585, "32": 602, "33": 622, "34": 638, "35": 658, "36": 674, "37": 690, "38": 710, "39": 727, "40": 743, "41": 767, "42": 787, "43": 803, "44": 819, "45": 840}
---

**Dave Jones:** Hi, in my previous tutorial video on op-amp voltage noise, where I used my HP 35660A dynamic signal analyzer here to measure the noise floor of some op-amps, or the power spectral density, really, of some op-amps. And I mentioned that I might investigate actually upgrading this thing

**Dave Jones:** because its noise floor is not great. I mean, we're talking about you know, in the order of 22 nanometers per second nanovolts per root hertz noise floor of this thing at 1 kilohertz there, so not very spectacular. So I talked about the possibility of

**Dave Jones:** opening this thing up, have a look inside and see what op-amps and components are used in the front end there, and see if I can maybe replace them with some modern, more modern ones, really, you know, designed for ultra, ultra low noise performance, and see if I could maybe

**Dave Jones:** do a drop-in replacement for some of those op-amps, perhaps, to increase the performance of this DSA. It's certainly possible, and I do have the service manual for this thing, but unfortunately it doesn't actually tell you on it. It's got full schematic and PCB overlay, but it doesn't

**Dave Jones:** have a BOM reference, and the schematic doesn't actually tell you which particular op-amp is used on the front end, which is really annoying. So I'm going to have to actually open this thing up, take out the main board, which I didn't do in a previous video where I actually

**Dave Jones:** repaired this thing, didn't take out that analog board, so I thought I'd take it out, have a look, see which chips used in it, and, well, go from there. So this video is more of just like a documenting reference for myself, really, to

**Dave Jones:** document the noise floor as it stands here on this thing, the original condition, and then look at the parts used, and then if we do the upgrade, then we have to see if we can improve the performance of it. Now for the reference measurements of the noise floor

**Dave Jones:** in this thing, I've got channel 1 range fixed to minus 51 dB volts RMS, that is the lowest range, it's 4 millivolts peak. Voltage range on the input, so that's all fixed. I'm measuring the power spectral density of this thing, and as the previous video, I actually made, I noticed I made

**Dave Jones:** the mistake of the vertical units here, instead of volts RMS per root hertz, I actually used volts per root hertz, and that gave me a figure before, over around 31.4, whereas I should be using volts RMS per root hertz, so that's what I'll use as the reference here.

**Dave Jones:** And at 1 kHz there, my marker frequency, this is over a frequency span of 1.6 kHz there, and basically if you enter 1 kHz as the span, then it actually says, oh I can't do that, I'll default to 1.6. And we're getting a reference value there with a 50 ohm terminated input

**Dave Jones:** on channel 1 of 22.2 nanovolts RMS per root hertz. And by the way, that was for a floating input with DC coupling. Now I'm actually measuring channel 2 here, and you can't just select channel 2, you've got to select dual mode, but there we go.

**Dave Jones:** We're getting a little bit higher, but it hasn't done the 100 averages yet. It's a little bit noisier there on channel 2 by the looks of it. 24.56 nanovolts RMS per root hertz for reference on channel 2 over 1.6 kHz span. And that's the figure with a 12.8 kHz span.

**Dave Jones:** And 100 kHz span with 10 kHz marker. And by the way, these are all performed with a flat top window in, so I can repeat that, the 100 kHz one with a HANIN window. There we go, for reference. And that's the 100 Hz response, once again, a flat top window.

**Dave Jones:** And that's the 10 Hz response after only 23 averages, because it does take 32 seconds per record length. So it takes quite some time to get to 100 here. That'll probably do. And we've got 163 nanovolts per root hertz at 1 Hz there.

**Dave Jones:** Alright, let's see if we can take the channel 1 board out here, so I'm going to have to unscrew these rails here, take off the ribbon cables, and hopefully it'll lift out, but there's got to be a coax going through to the BNC on the front panel.

**Dave Jones:** So I hope I don't have to take off the front panel and then undo the BNC housing and all that sort of jazz. We'll see. Actually, I don't even think I have to take that board out, because this shielded top just lifted straight off.

**Dave Jones:** And you can see the shielded CAN in there, but I believe one of those two op-amps down there is the front end op-amp. I can see, and you probably can't see it down there, ah yeah, there we go. A couple of metal CAN transistors down in there, I believe they're the FET

**Dave Jones:** buffer front end, but I believe one of the first, well the first op-amp in the chain is one of those puppies. And if we have a look at the schematic here of the front end, please excuse the lack of screen capture here, here's the BNC

**Dave Jones:** on the input over here, and then we have all of our read relays to do the various AC-DC coupling, shorted out input test signals, things like that, input attenuation path, input 50 ohm termination down here, and stuff like that. And then it goes into

**Dave Jones:** check this out, here we go, there's our looks like they've got a FET, a matched FET input buffer there, with an unknown op-amp. Doesn't actually have the number on it, I kind of assumed it might have maybe been a generic NE5534, but I just looked at the number in there, and that doesn't look to be the case.

**Dave Jones:** Because there is no BOM here, so that's U1 and U2, it's a differential thing, so they've got a low and a high FET buffer there, so instead of using a FET input op-amp, they've used a FET they've used a matched FET pair on the input, and effectively turned it into a FET input op-amp.

**Dave Jones:** Because FET input op-amps generally have higher input noise voltage density than your bipolar op-amps. So really, that's maybe why they've gone for that FET input. I mean, I don't know what the state of the art in FET input op-amps was back in when this was designed back in the late 80s, and

**Dave Jones:** probably even before that, carry on from previous DSA designs, I'm not sure. Because, you know, this isn't one of their oldest DSAs, not by a long stretch. But anyway, yeah, so that op-amp is probably you know, as a first guess, without knowing what this transistor is, because as I said,

**Dave Jones:** they don't have a BOM for this thing, all they've got is a component overlay, and nothing's marked on there, so we'd have to look at the metal can there to figure out the transistor. But probably as a first guess, I would say that

**Dave Jones:** op-amp maybe dominates that in terms of the buffer there. And then it goes to the next sheet over here, but if we go to our component overlay, here's our component overlay, and this is what we looked at on the board there. Here we go, there's our two op-amps on the top,

**Dave Jones:** U1 and U2, so they're definitely our two op-amps. And with inside that front-end shielded can there, that is just all of your relays, K, there they are, and there's Q1 and Q2, so there's your two matched transistor pairs there. So they're inside the

**Dave Jones:** can, so that'd be annoying, we'd have to take the can off probably to see the part number on those suckers, but let's go back to those dip chips there, U1 and U2. And they are not NE5534s, they are a signetics. You know, it almost looks like a

**Dave Jones:** maybe a HP part number on that sucker, we may be able to track that. I think, as a first guess, 27-0715, but it's got FGK2563 on it, that is not familiar at all. You can see the date code there, first week 1990. And they've used those also in a couple

**Dave Jones:** of locations, 2563 there, and there as well, I don't know where they are in the circuit, but yeah, there's certainly quite a few of them. Ta-da! We have the board out. It wasn't easy to get out, but it did come out. Yeah, no coax, it uses

**Dave Jones:** a beautiful little right-angle BNC there to connect down to a mating BNC right down the bottom, which then has the coax which goes to the front. Just beautiful design, absolutely stunning. I love it. So the high-res photos of this, by the way, will be up on my Flickr account for those interested.

**Dave Jones:** Well actually it wasn't hard to find out what this mystery labelled chip is. Yes, I was right, it is just a Signetics NE5534 classic audio op-amp. But it's got some weird-ass, you know, custom HP part number on it, and it's used all throughout this thing, there's like a dozen of them

**Dave Jones:** on this board. The reason I know that is because that's U4 and we can see U4 on the schematic, and it is one of the rare chips in there that is actually labelled NE5534. So it's got to be it. If we just have a quick look at the input front end here,

**Dave Jones:** nice little Koto relays, I'll have to check out the part number on those, but look at that beastie, that's actually the 50 ohm input terminator. Go figure. And those Koto reed relays, of course, Koto, one of the premium brands in the business, 2900 series reed relays, exactly what we want.

**Dave Jones:** They're hermetically sealed, of course. Epoxy-coated shells provides magnetic shielding, optional electrostatic shield to reduce capacitive coupling, and optional coaxial cable shield as well. So, you know, really purpose-designed for one of these front ends. Really is quite a nicely laid out board, as you'd expect.

**Dave Jones:** Look at the big ground split right down there, beautiful. I love it how you can see through these old-style boards, they're just superb quality. I love them. And yeah, bloody HP part numbers on everything. Real pain in the ass, look at that. And I count 17

**Dave Jones:** of those Signetics NE5534s on there. There's a whole stack of them over in this section here. They've almost used those exclusively for the op amps. And there is under the metal shield. And you'll note that, yeah, they've removed the ground plane from under there as well.

**Dave Jones:** And there's our, you know, it's basically all of the input switching. It comes in down the bottom here, of course. And then, so a signal comes in here from the front panel, we've got our 50 ohm terminators, and the relays to switch that on, and the relays to ground the input and stuff like that.

**Dave Jones:** And then we've basically got our front end stuff in here. This is all our high impedance FET stuff. And then these are our two up the top here, they're our first op amps combined with that FET buffer. But it's interesting to note that they actually have

**Dave Jones:** put the FET inputs under the shielded can, and haven't put the op amps under there. You'll notice a couple of guard traces going from just directly on the metal can there, around probably around the back of the input pins to the op amp.

**Dave Jones:** And both the FETs on the input, they've got 550460 labelled on them, and a national semiconductor and another mark on the other side. And there it is, national semiconductor D8952. So I'm not sure what that part number that actually translates to yet, haven't been able to find anything on that.

**Dave Jones:** But these input op amps, definitely NE5534, so unless they're really specially selected from Signetics, I doubt it. Because this is not a particularly low noise unit by any stretch as we've seen. Then yeah, they're at 1 kHz, I think about 3 nanovolts per root hertz.

**Dave Jones:** Can certainly get a lot better than that these days in terms of like an AD797 or something like that. But not really directly pin-compatible replacement because there is compensation on those amps, compensation used on those amps which may not be compatible with any replacement chip.

**Dave Jones:** You just have to be very careful. So I don't know, I'm going to have to mull this one over. I haven't got enough time to mull it over today. But it's a shame they're not in sockets, of course. It would have been really easy just to, you know, suck it and see, really.

**Dave Jones:** Well I could certainly do that, suck off the solder and see, no pun intended. It might be worth a try. So you know, really the input noise is probably going to dominate in the front end here, combination of the FETs plus the op amp, and it's going to be the

**Dave Jones:** input current noise as well as the input voltage noise, combination of both and the whole thing there. So you know, it might be worthwhile, you know, trying to upgrade this section, see if we can get better performance. So anyway, if anyone has any thoughts on that, please leave it in the comments.

**Dave Jones:** Catch you next time. www.austincosmetic.com
