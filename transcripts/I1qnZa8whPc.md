---
video_id: I1qnZa8whPc
title: EEVblog 1708 - What's This SMD Part?
url: https://www.youtube.com/watch?v=I1qnZa8whPc
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 26, "3": 40, "4": 53, "5": 69, "6": 85, "7": 97, "8": 109, "9": 121, "10": 137, "11": 157, "12": 175, "13": 192, "14": 205, "15": 221, "16": 236, "17": 260, "18": 273, "19": 292, "20": 303, "21": 327, "22": 344, "23": 360, "24": 378, "25": 389, "26": 401, "27": 418, "28": 429, "29": 442, "30": 460, "31": 475, "32": 491, "33": 504, "34": 516, "35": 526}
---

**Dave Jones:** Hi, just a quick answer to one of my followers on X and I thought other people might find it interesting as well. Well, I've done many of these like Dave, can you identify this part? Um, so let's do this again. This comes from

**Dave Jones:** Juiced on X here. You can follow me on X. I post my daily whatevers there and I'm handle EEVblog. There you go. So, follow me over on the X Twitter is. Um, so Juiced, can you tell me what this

**Dave Jones:** part is? A DB30AD. First, have a look at the image here. The first thing you want to have a look at is the reference designator here on the silk screen. This is the white thing Q2 here. Now, Q indicates that it's a

**Dave Jones:** transistor. It's not a diode. If it was a diode, it'd be D1. If it was a voltage regulator, it may be reg one or V1 or something like that. And Q2 means just it happens to be the second transistor

**Dave Jones:** on the board. So, yeah, but Q indicates that it's a transistor. So, we know we're dealing with a transistor here. And I can tell just by looking at this is a SOT223 package, but we should not need that to help find this. Now, the

**Dave Jones:** next thing I notice in this is that this F symbol here. Anyone old school will know that F symbol there is the manufacturer's logo and that is classic Fairchild. They're one of the original you know, OG manufacturers of

**Dave Jones:** semiconductor. So, I know this is a genuine Fairchild jobby. And let's have a look what else we've got down here, okay? You have a look at the pin out and where things lead. Like there's no bypass capacitors near it, right? So,

**Dave Jones:** you know it's not a voltage regulator, but we already know it's a transistor. But even if the silk screen was there and didn't have Q or Vreg or something like that, you can tell it was this might be a voltage regulator if it

**Dave Jones:** had bypass capacitors on the input and output. So, it doesn't. And we've got a diode here. So, this is some sort of possibly reverse protection diode. And then if we follow this middle pin here, sorry I don't have my drawing program.

**Dave Jones:** This is just a quick and dirty. Aha, side motor L left, I guess. So, this is in some sort of robot motor drive left and right motors or something. So, we know that this is a motor drive transistor. So, it's probably a MOSFET

**Dave Jones:** for example. And we've got a reverse protection diode here to prevent back EMF from, you know, damaging this thing. So, that's looks like yeah, we've got a MOSFET driver transistor here. Now, the part number DB30AD. Pretty sure that's a red herring. That's

**Dave Jones:** the manufacturer's code. So, if you search for DB30AD transistor, I don't think we're going to find anything, okay? 30 V silicon bipolar transistor available at Mouser, right? It's not going to be that, okay? Could be, but I don't think so. No,

**Dave Jones:** these are old school a classic jelly bean part the BC549, okay? 559, no, it's it's not that, right? So, what you're searching for here is the 459 underneath. That's the part number. And there's there'll be letters in front of that, but it doesn't

**Dave Jones:** have those. They That's just what they do. I don't know why there's space there to put all the letters as well. So, this DB30AD, that is a red herring. That is the manufacturer's code. Sometimes they put it above like this. Sometimes they

**Dave Jones:** put it below. So, you can't be sure. So, yeah, if you tried searching, you you can search forever. You're never going to find that. That is the manufacturer's internal their manufacturing production code. And that tells them something internally, but you'll never find that

**Dave Jones:** in the data sheet. So, this tells them which production line, which facility it was manufactured at, when, and using what process, blah blah blah blah blah. They they'd be able to trace that. Um, but four 459 is the proper thing. We could just go

**Dave Jones:** 459 transistor, but I'm going to go Fairchild cuz I know that's a Fairchild. So, fair Fairchild 459 transistor. Boom, FDT459N, N-channel enhancement mode MOSFET MOSFET. Here we go. There's our data sheet. F FDT459, it's in a SOT223 package. Go figure.

**Dave Jones:** There you go. And uh what can it be used for? Uh no notebook power supplies, DC motor control. Bingo. Then like you could use any MOSFET for motor control, but yeah, they just put it in there. Gives you

**Dave Jones:** that warm fuzzy. That is definitely it. Uh SOT223 package. Uh there's absolutely no doubt that it's an FDT 459N. So, there you go, Just. It's an FDT459N. Um yeah, so lesson uh for trap for young players out there, um just be aware of

**Dave Jones:** what rabbit hole you're going down with the part number there. In this case, 459 was it. What do you know what happens if we just go 459 transistor? I mean, you won't find it with just 459. Now, it's

**Dave Jones:** getting a bit Okay. Well, Wagner Electronics BF459. No, not there. 2SB459. No, it's not that. Um FMMT459 from Diodes Incorporated. Uh that is a bipolar transistor, actually. So, that's inter- that's interesting. Um so, yeah, 459. So, that 459 part number comes in

**Dave Jones:** both bipolar. Go away, cookies. So, that's interesting that um 459 part number comes in both like a high voltage NPN um bipolar transistor. You can tell by the symbol there, bipolar. It's not a MOSFET. Um it can but it's only in a

**Dave Jones:** SOT23 package. So, so straight off the bat, you would have ruled that one out cuz it doesn't come in any alternative packages there, but it certainly, you know, could have been a candidate, but wrong package. But, you could put 459, and then you could put

**Dave Jones:** SOT223 transistor like that. I wonder if that No, there you go. It's coming up in the SOT23. So, it's ignoring the SOT223 there. And yeah, it's just a bit harder. So, it looks like in this particular case, putting Fairchild in the front,

**Dave Jones:** knowing who that manufacturer was, and you can go search like symbols maybe with AI these days or Google image search or whatever, you might be able to say, "Please tell me who the manufacturer of this transistor is." And

**Dave Jones:** it I don't know, the AI might be able to help you out. Hell might be able to help you there, but yeah, Fairchild seems to be the particular keyword there. So, that's interesting. So, even putting in in the

**Dave Jones:** package there, that didn't help. You had to put in Fairchild, and then, boom, we got lucky FDT459, but it shouldn't have taken much longer to get there. It should have been obvious that that top number, the DB38D, that was a red

**Dave Jones:** herring. But, sometimes, you know, you can chase a red herring down a rabbit hole, and that might give you what you might think is a positive lead. I've been down this hole myself thinking that, "Aha, that's definitely the part

**Dave Jones:** number." It's not. It's the 459 there. Then, of course, we could guess that it's a MOSFET for example, 459 MOSFET transistor. Ooh, no, now we're getting SIA459.

**Dave Jones:** Vishay Siliconix, that's a P-channel jobby. Really? Oh, isn't that pesky? Look at that package. What the heck's that package? It's some sort of QFN thingy. And then, yeah, 22 weeks lead time. Thank you very much. No, thanks. But, that's interesting. That's a

**Dave Jones:** P-channel. That's opposite to what we want. We know this is an N-channel jobbie. So, yeah. You see how you can unfort- get unfortunate coincidences with part numbers there, and that can really ruin your day. It It really can. So, yeah, it's given

**Dave Jones:** us No. See? So, just put in MOSFET. Really? This is a nice example where you really had to put in Fairchild as the manufacturer, and that's where it came up. So, you know, got a bit lucky there that we

**Dave Jones:** could identify the manufacturer. Sometimes you can't if it's some, you know, obscure Asian thing or or it doesn't have any logo at all. It's just got like, you know, FN2 or something like that on it, right? And then you've got like no idea what

**Dave Jones:** that is. So, you have to do the look up those SMD look up tables and things like that, which I've done videos on. So, there you go. That's a Fairchild FDT459N. If you found that video useful and you

**Dave Jones:** like this style of video, please give it a big thumbs up. Helps with the engagement, especially with the views tanking on YouTube at the moment for various reasons. You might follow me on Twitter. I've been discussing that. And

**Dave Jones:** as always, comment and discuss down below. Catch you next time.
