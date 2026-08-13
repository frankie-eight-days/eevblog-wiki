---
video_id: ag-MjKAfATw
title: Rode AI-1 USB Audio Interface Teardown
url: https://www.youtube.com/watch?v=ag-MjKAfATw
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 29, "2": 49, "3": 73, "4": 90, "5": 110, "6": 126, "7": 142, "8": 162, "9": 182, "10": 211, "11": 231, "12": 251, "13": 272, "14": 288, "15": 304, "16": 328, "17": 357, "18": 381, "19": 405, "20": 425, "21": 441, "22": 458, "23": 482, "24": 502, "25": 522, "26": 538, "27": 563, "28": 583, "29": 607, "30": 623, "31": 639, "32": 660, "33": 676, "34": 696, "35": 720, "36": 732, "37": 756, "38": 773, "39": 789, "40": 809, "41": 825, "42": 841, "43": 857, "44": 873, "45": 889, "46": 910, "47": 930, "48": 946, "49": 958, "50": 970, "51": 1002, "52": 1027, "53": 1047, "54": 1063, "55": 1079, "56": 1095, "57": 1111, "58": 1127, "59": 1147, "60": 1164, "61": 1192, "62": 1217, "63": 1241, "64": 1261, "65": 1273, "66": 1289, "67": 1305, "68": 1321, "69": 1337, "70": 1349, "71": 1366, "72": 1382, "73": 1406, "74": 1422, "75": 1438, "76": 1455, "77": 1467, "78": 1479, "79": 1491, "80": 1507, "81": 1523, "82": 1539, "83": 1555, "84": 1567, "85": 1596, "86": 1612, "87": 1632, "88": 1648, "89": 1668, "90": 1688}
---

**Dave Jones:** Hi, just a little impromptu second channel video teardown of this thing. It's the Rode, what is it? The AI-1, what do you call these? Like a USB audio interface kind of thing. Anyway, it's got a phantom power 48 volts microphone input. You can actually turn that off and on

**Dave Jones:** by pushing that. It's got mic volume and it's got headphone output and apparently you can push the button here and you can get the microphone to monitor, you can monitor the microphone in the headphone outputs. On the back it's got a USB-C interface

**Dave Jones:** standard, you know, Windows audio type interface and quarter inch balanced outputs for speakers. And it's, by all accounts, a very nice bit of kit. And it is all metal construction. It is very, very nice. Made in Australia, no worries. Look at that. Beautiful.

**Dave Jones:** I'm actually, I've contacted Rode. I'm looking to get a tour of their manufacturing facility here in Sydney actually. Design and manufacturing facility. So haven't heard back from them yet, but anyway, let's do a teardown of this thing, shall we? I'm going to be

**Dave Jones:** using this for my desktop solution. So like as in at the office, I'm going to be using it for because the plan, kind of, is to use the same mic. Like this is the mic the M5 I think it is that I use on top of my camera.

**Dave Jones:** I want the same mic to match at my office so that I can do voiceovers with the same mic to give the same voice quality. And stuff like that. Anyway, let's do a teardown, shall we? I'm recording this in 60 frames per second through my

**Dave Jones:** Tigano microscope. So there's no screws on this thing, but there are these little tab things there. So that's interesting. And as I said, this is all metal. It really, it feels built like a brick dunny. It really is super high quality. At Rode,

**Dave Jones:** don't make crap stuff. They make some of the best stuff in the industry. So let's, oi, hello. Hello. I was looking at the screen instead of looking here. It's probably a mistake. Oh. Oh. Ah. Ah. Oh, yeah, there we go. Got it. Got it.

**Dave Jones:** So, might have to go around here as well. That's interesting that they do that with, you usually find that with plastic stuff, the clips like that. So, oh. There we go. Oh, it's just a, it's just a fascia thing. Oh, I'm going to have to get a

**Dave Jones:** yep, one second. I'll just get a couple of what is it? T10? No. Yep. T10. Alright. So that's, that's really Oh no. No, that is actually plastic. Sorry, that felt for all the world like metal. It really did. Fooled. There you go. It is

**Dave Jones:** plastic. But the bottom of it is metal. Now apparently, by all accounts, this is a really low noise mic amplifier. I don't know, you know, how it compares with others on the market, but you know, you read reviews and stuff, and apparently it is, like demos and things, it is like

**Dave Jones:** stupidly quiet. So, we'll have a look. Okay. Is that just going to fall? Ah, it's just going to fall off. Aha! We're in like Flynn. There you go. So it's, it's coated on the back and not on the inside. Alright. Let's have a look.

**Dave Jones:** It apparently uses a genuine Nutrix connector on there. One of those universal jobs. And they've got a separate PCB for that. So that kind of makes sense, because this sort of form factor, when you've got, either you get a right angle version of this, I don't know, like if

**Dave Jones:** they were available in right angle, then you'd think that they'd use the right angle. But then the problem becomes trying to get the thing in. When you lower it into the case, it's harder because you, you know, because it's got to stick out

**Dave Jones:** the front of the case like that. So maybe having a, but look, they've got a custom plastic bracket and everything on the back of that. That is really quite nice. I like that. And the obviously they didn't have enough room on the board down the bottom, so they had

**Dave Jones:** to do this board up the top to have the USB-C connector and some flat ribbon cables. So they've gone to quite a significant effort. You can see the test points on there for production. Testing. But if we go Audio PCB, Rode Microelectronics, Rode Microphones, Australia.

**Dave Jones:** No worries. NAU88L25. What is that? What is that? Let's go to the, what is it? NAU 88L25. NAU88L25. Nuvoton. Product Brief. Yeah, we'll just go for the product brief, shall we? Should be right. There you go, there's how they're getting their ultra-low noise.

**Dave Jones:** Ultra-low noise, audio codec for headphones, headsets, right, with 124 dB class G headphone drive and advanced headset features. Ultra-low power, high performance, in this case you don't care about the power consumption, really. Because you've got the USB-C there, like who cares? Audio, but it would matter for some applications.

**Dave Jones:** Ground reference headphone, amplify advanced headset detection, single chip solution, microphones, ground detection, switching capability for smartphones, tablets, IK, personal computers. Smartphones, you wouldn't have a, oh it's a reasonably small chip, so you know, reasonably small package, but maybe not that good for a

**Dave Jones:** smartphone, perhaps. But anyway. Highly integrated, it's got an I2S interface of course, digital mixer, two high-quality audio digital analog converters. So they're, so obviously this is used for the DAC outputs, the two outputs on the pack, the two balanced quarter-inch outputs, one high-quality

**Dave Jones:** analog to digital converter. For the microphone, one monophonic differential analog microphone input, two analog, so it's all yep. All right, advanced on-chip DSP, includes dynamic range compressor as well. Okay, I didn't know it had dynamic range compression, whether or not they've, I can assume you can disable that.

**Dave Jones:** So whether or not they've got that enabled, I don't know. And programmable bi-quad filters of various filters to optimize audio quality, I don't think there's any, there's no filtering in this, it's just as is. So I think, they probably have the compressor disabled, I'm not sure, I have to read the manual.

**Dave Jones:** Don't know, I haven't used it yet. Supports various clocks, blah blah blah, up to 192 kHz sample rate, a DAC with auto-attenuate, 124 dB signal-noise ratio, auto-mute, what is it, ADC 121 dB signal-noise ratio. So it all sounds pretty schmick. And there's our block diagram.

**Dave Jones:** There you go. Okay, it's got bias, mic bias. Okay, does that, that doesn't do the so it's got an internal microphone amp, but it doesn't do the, I assume it doesn't do the 48 volt phantom power. So it doesn't do that on-chip. I didn't see that mentioned.

**Dave Jones:** So yeah, there you go. That's the heart of this thing. So let's go and see what else they got on here. Okay, a couple of little, couple of little jobbies down there. Little 6-pin SOT-23s, don't know what they are. They're for, they need a little LED.

**Dave Jones:** So they, what, what are they, LED drives? What are they, what are they doing? Oh, okay, that could be, okay, because that's the switch interface. So you press the switch. So maybe, I don't know, maybe there's sort of like some, I don't know, are they, no, they're not an I squared C thing.

**Dave Jones:** No. So don't know what it's doing there. Okay, a bunch of other SOT-23 stuff. They don't look like regulators, so they look like some other type of amp. 4 volts, 100 mic, 50 volts, there you go. 50 volt caps. So they're for our phantom power.

**Dave Jones:** Obviously, well, they're our, no, they're, they look like AC coupling. They're two, oh sorry, I'll point it out. They're two AC coupling caps there. So what else have we got? SIM 052, that'd probably be a MUX. SIM for, you know, 4052. So your classic.

**Dave Jones:** Updated to the new version of X-Split, which is really quite nice, but it, it had the auto-loading. So you just it had the auto, like it had the hotkey, which was the spacebar, which paused the recording. So I actually just finished this recording, I went through like another 10 minutes of this thing, and it

**Dave Jones:** wasn't, it was paused. And I didn't notice. And so, here you go. So, sorry, I thought I, like, nailed the rest of that. So I've got to redo it. Bloody hell. Unbelievable. Anyway, where were we? We were, oh god. Now I've got to bloody edit this thing.

**Dave Jones:** This was supposed to be like a single take. Anyway, where were we? We were up to this 4052. Right? So I hate the fact that, here we go, that's a 4052 is a dual, um, what is it? A MUX-y, dual 4-channel analog MUX, D-MUX.

**Dave Jones:** Right? I hate how TI, um, like, label these things. Why can't they just put, like, the proper, like, it's a 4052. It's a 74HC4052. No, they put this CMO52 bullshit. That's really annoying from TI's point of view. Anyway, let's have a look at the rest of this.

**Dave Jones:** I now, like, know what's going on here because I just did it before. So, this is our phantom power. You can tell, like, our two high volt, our 50 volt caps here, okay? They're running quite close to the, uh, nominal 48, um, or these, no.

**Dave Jones:** Yeah. No, are they in parallel? No, no, they're not in parallel. So they look like, oh, okay, yep, yep, so they go up to here, so that would be yeah, that's trans, yeah, transferring the phantom power over by the looks of it. Are they doing just some protection resistors there?

**Dave Jones:** No worries. Anyway, so this is our phantom power, but our phantom power's actually generated over here. Look at this. We've got ourselves a diode capacitor pump there, and that is amplifying the voltage up. No, sorry, multiplying the voltage up. So that's generating the 48 volts.

**Dave Jones:** You want to have it over here because so then you can filter the crap out of it before it gets over to here. You don't want to have it close. Anyway, going down in here, we've now got some, uh, Japan Radio Corp JRC4580s.

**Dave Jones:** And there, of course, your standard op-amp. NJM, you know, Japan Radio Corp, like, rule for, like, low cost. Anyway, the, uh, like, you know, audio parts and stuff, like op-amps and things, little regulators and stuff like that. I think we're going to be using one in the new microcurrent, actually.

**Dave Jones:** Anyway, the 4580 is the classic audio op-amp, you know, it's got Nafl, half a b-stick distortion, 0.05% typical distortion, good enough for Australia. And, um, yeah, a lot of people swear by them, a lot of people don't. There's a lot of audio fools who either love them or hate them.

**Dave Jones:** You know, they'll advertise the fact that it has, you know, some brand or some people like the other brand better than others. Anyway, 4580s all the way through. Um, there was another 4580 all the way over here, we'll probably look at that later.

**Dave Jones:** So anyway, that's the, uh, generation, so that'll have an oscillator in there, just to drive our multiplier. And, uh, what else have we got? Um, yeah, right. So, now, I'll explain the signal path here. This is what I find interesting, a little bit puzzling I guess,

**Dave Jones:** in that, uh, here's our microphone amplifier, right? This is our main chip, this does everything. It's all the way over here, if I was laying out this board, I would have put that as the first thing, because the most critical thing in here would be the trace

**Dave Jones:** length to the microphone input. So here's our microphone input over here. So, you know, you can understand that all the phantom power stuff has to be around here, okay? No worries whatsoever. But I would have whacked this as, like, up here, near, so that it didn't have

**Dave Jones:** to go very far. But look how far it has to go in this particular case, okay? It's gotta, it's gotta obviously come out of here, it's yeah. Okay, so they've got some sort of, like, pins under here. Anyway, so it obviously goes, I think

**Dave Jones:** does it go straight over? I think it comes into here, so it maybe comes into this. And then, they got like a preamp on the input? I'm not sure, I didn't think it needed, I thought this could handle the microphone directly. Anyway, it comes in and it goes into the mux

**Dave Jones:** here, okay? Because you need this much mux because it's gotta be able to switch the microphone directly analog from the microphone input over to the headphone output, so you get zero latency. And then it comes out of here, follow the money, there's the balanced

**Dave Jones:** no, here it is, yeah, follow the money out of here balance line over, got two AC coupling caps in here, they're 50 volt AC coupling caps so they come over, you can see that they're in series with the line that's how you can tell they're AC coupling, going over here, going over

**Dave Jones:** not sure what that is, got some pull-ups have we? But anyway, it's basically then gonna go into our directly into our microphone, our main chipset over here which has the microphone amp and everything else in it. So you know, running that halfway across the board, it's just puzzling, obviously it's doing

**Dave Jones:** just fine because the performance apparently is really superb like the low noise performance, everything else. So, you know, I'm just surprised from a PCB layout point of view, maybe, like you know, marketing might have driven the design and layout of this thing. They said, this is what it's gotta

**Dave Jones:** look like, that's it. PCB designer, make it fit. You know, but if I was the PCB designer, I probably would have put that up there first as a matter of course, because you can run line level stuff, like across the board, that's all fine.

**Dave Jones:** So when you're running line level stuff, it's no worries. But that microphone line is critical, so I'm just surprised that they're running it halfway across there, but it's fine, they're getting away with it. It's just, you know, it's just a rule that you're gonna follow.

**Dave Jones:** Anyway, one of the interesting things is down here. Look at this. 32F070. And that is a micro. Like a Cortex M0 48MHz 32K of flash memory. What the hell are they? Like I expected to find just like a USB audio, like a crystal semiconductor USB audio chip or something like that.

**Dave Jones:** But nope. Nope. A micro. Okay. Oh granted, well yeah, okay, they've gotta control things and stuff like that, but still. Okay. Anyway. It's got the USB-C interface and all that sort of jazz. So I just find that really interesting. So that micro. And then what I find hilarious is

**Dave Jones:** they've got this super powerful micro in here, next to it didn't have enough I.O. on it, so they had to use a 74HC595 serial to parallel I.O. expander in there. It's just hilarious. Like why? Anyway, they've got tons of 6-pin jobs all around the shop, or 5 or 6-pin

**Dave Jones:** SOT-23s. It's much more complicated than I expect, actually. There's a lot more stuff in here. There's another 4580 down in here, and then we've got all sorts of local regulation around here. This is interesting that they've got 3.9 ohm resistors in here. I don't think they're doing

**Dave Jones:** any current sharing with those. I don't, so I don't know like they're not, and I don't see any, are they? Oh they could be, yeah, they could be like current sense resistors. If they're doing that then that's impressive. Individual current sense for each regulator, so that's

**Dave Jones:** yeah, because you can see there's another VIA buggering off there somewhere, but that could just be power going off. No, no, they're not I don't think they're doing that. Although that's what that little amp, that could be an amp that's measuring, a diff amp, it's measuring the current.

**Dave Jones:** If they go into that sort of effort, great. As I said, it's a lot more complicated than I expected. I expected to find just like a USB audio interface chip, I expected to find like one big like, you know, commercial, you know, chipset that

**Dave Jones:** does the ADCs and the DACs, and you know, these things are off the shelf, right? Like it's a superb performance one, you know, it's like an industry-leading kind of performance one. I expect to find that, I expect to find the 48 volt phantom generation, maybe some, you know, analog

**Dave Jones:** housekeeper, and two more crystals! Two more crystals! Why? Why do we need two more crystals? Already got a crystal over there for the micro, of course. And why have we got two more crystals? Oh, okay, that'd be the sample rate, of course, for the, yep, okay.

**Dave Jones:** No worries. Why they couldn't generate that from the one clock and just run everything from the one? Don't get it. Anyway, not sure what the 4580s up here are doing, because it's not like they're amplifying the mic, so all over the shop they've got three of them up there.

**Dave Jones:** Are they driving the balance? They could be driving the balanced output here, maybe. So TRS output there. So, and this 4580 down here is probably doing the... no? No, that could be driving the balanced output, actually. If you have a look up here, coming up, there's proximity to there, and then these

**Dave Jones:** go over to here like this, so yeah, that makes sense. Okay? Okay, this ribbon cable's obviously for the USB interface. So anyway, there's lots of there's a lot more op amps and stuff in here than I expected. I'm very very surprised. Obviously these, the power dissipation in these regulators is naffle,

**Dave Jones:** so they're obviously cut. That's going to be plenty just on the PCB there. But yeah, the other thing is, is that if you have a look here, you can see that the connectors go below the capacitors down in there. So this is your

**Dave Jones:** 3D envelope design. And this is sometimes, you know, if you've got to do all this manually, it's rather tricky. Rota probably using Altium Designer, but any high-end package these days, including Altium Designer, have 3D DRC, 3D design rule checking. So if you go to all the effort

**Dave Jones:** to 3D model your components, and it is a lot of effort if you're just doing a one-off, like, so guilty as charged, I don't bother a lot of the time. Although when I worked at Altium, we had people who did 3D models for us.

**Dave Jones:** So you just go, oh, can you give us a 3D model for this? Yeah, no worries. Comes back, you know, 10 minutes later and it's done. But for a company like Rode, who manufacture, design and manufacture a lot of different products, I'm not sure how many they have, but they would have a huge

**Dave Jones:** catalog of parts, and you want to reuse, as a designer at Rode, you wouldn't necessarily, you know, you'd be encouraged, you should be encouraged anyway, or as a professional you should just know this, is that you want to reuse the existing parts in your catalog.

**Dave Jones:** So you don't want to have yet another reel of components, because they manufacture their own boards. So they've got, they'd have their own in-house pick-and-place machines probably, and you know, they'd all be loaded up with the components, and you don't want, when you design a new product, the last thing you want to do is use yet another

**Dave Jones:** component. That you've got to stock, purchase, stock, store, put on the pick-and-place machines, change over, everything else. So they're trying to reuse as many parts as possible. So doing a 3D model for every single component would be very beneficial to them. And then, when you did that,

**Dave Jones:** you could, like, import not only the main board down here, but you can import this board with 3D models of these, 3D models of the ribbon cable, 3D models of all these connectors and these plastics and everything else, and you could do the knobs,

**Dave Jones:** and you could do everything. And you could see, at the design stage, that that capacitor is not going to foul with that. You can be 100% confident that's going to work, because the software will give you a, like, it'll just flag it and say, these two components are

**Dave Jones:** touching. You know, when you put this board in, you know, it can, like, software insert the board, and it knows that they're going to foul. And, you know, it really is a very valuable tool. And it can save a lot of re-spin and, you know, get it right the first time

**Dave Jones:** kind of thing. So, yeah. We got a version number up there. What's their version number system? Yeah, I have no idea what 34370115 is. Anyway. There you go. So that's the that's the Rode A1-1. And it's quite nice. Oh, by the way, I forgot to show these solder

**Dave Jones:** joints here. Yeah, we're still running, yeah, I haven't paused it yet. Look at this. This looks a bit, how are you doing? Look at that. That looks dry as a dead dingo's donger. That's not, it's not great at all. You can still see

**Dave Jones:** the flux, like, bubbly residue around that. It's not terrific. This lead-free rubbish, you know, like, and they haven't bothered to, you know, clean around here either. So they've got flux residue, they haven't done the, and that's a, you know, that one's a bit frosty

**Dave Jones:** the snowman happening there. And it's not, it's not terrific. It probably looks worse than it is, but yeah, I'm just surprised that I expected the quality to be a bit more controlled, a bit better. Maybe someone was rushing that and, you know, didn't use the right

**Dave Jones:** you know, thermal mass iron, the right temper, you know, you'd think they'd have that right. You'd think they'd have that down pat. Anyone who's doing that sort of production soldering should be able to nail those joints, no worries. Because that's not a huge ground plane

**Dave Jones:** or anything, it's not like it's going into a big 12-layer board or something. And so yeah, that should, they should have been able to do better than that. Very disappointed. I'm not going to bother to take the board out, because I don't think there's anything

**Dave Jones:** on the bottom side of that board that would surprise me, because you want to minimize, you wouldn't go double-sided load unless you absolutely have to. You wouldn't have components on the bottom, because that increases your production thing. You've got to flip it over, you've got to glue components.

**Dave Jones:** A lot of extra production effort required to put components on the bottom side. So only if you had, like, high-density BGAs or something that required decoupling on the bottom of the board would you consider that. Or unless you're doing some ultra-miniature thing, this thing

**Dave Jones:** didn't need to be ultra-miniature. It's obviously, like, it is quite small and compact. And I just love the machined case. It's just, you know, it's beautiful. It is fully machined, isn't it? Look, you can see the machining in there. I think it's, or is it like

**Dave Jones:** die-cast and then sort of machined? No, it looks, you know, it looks like it's a machined case. Please, please correct me if I'm wrong. I'm not the world's best mechanical expert in that case, but at least that top surface has been machined out, so maybe it's cast and then they might machine it

**Dave Jones:** down, the rim down or something like that. I don't know. Anyway, it is a beautiful case, I'm very impressed. And the design and build quality is pretty good, apart from a few how-you-doin' joints in there. And maybe a questionable decision with the placement of the ADC, but they

**Dave Jones:** obviously, my camp, but they obviously get away with it. So, there you go. Really is a nice bit of kit. And as I said, overly complicated for what it, maybe it's not overly complicated, I don't know, I'd love to see the schematic of exactly what they're doing there.

**Dave Jones:** It just has more stuff. More analogue-y stuff, more op-amps and stuff than I expected. I expected just, like really, I expected just a like an off-the-shelf, you know, crystal semiconductor, like USB audio interface going to, I expected the chipset that did like the microphone amplifier, the

**Dave Jones:** like the dual-channel driving, and the whole works, you know, the DACs and the ADCs. I expected that, that, I expected maybe a couple of op-amps to, you know, bridge the, you know, the sound between the zero-latency thing between the microphone and the headphones and stuff like that.

**Dave Jones:** But, you know, and the 48 volt phantom power thing, but everything else is like, there's a lot of, it's just a lot of extra stuff in there. Anyway, a little bit surprised by that. But that's the Rode AI-1. I hope you enjoyed that little

**Dave Jones:** impromptu teardown. Now I've got to bloody edit this video or join the clips together because the stupid program paused on me, and I didn't notice. Like, there's a counter in the top corner, that's, if you don't know, it's sort of, there it is there, and I'll

**Dave Jones:** switch over. There it is there. So you can see it. You can see it, and it would have, this frame counter would have stopped, you know, and I just didn't notice it. Oh! Anyway. There you go. I hope you enjoyed that. If you did,

**Dave Jones:** please give it a big thumbs up, and as always, discuss down below. Because I read the comments. Usually. Second channel. You know, you get what you get on the second channel. Including my comments, including my replies. Anyway. Catch you next time. Now how do I turn this thing off?

**Dave Jones:** It paused on me and I didn't notice.
