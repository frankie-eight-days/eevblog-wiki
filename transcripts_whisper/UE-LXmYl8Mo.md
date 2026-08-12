---
video_id: UE-LXmYl8Mo
title: EEVblog #1352 - Aircraft Transponder TEARDOWN!
url: https://www.youtube.com/watch?v=UE-LXmYl8Mo
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 0, "2": 30, "3": 60, "4": 90, "5": 90, "6": 124, "7": 140, "8": 160, "9": 180, "10": 200, "11": 214, "12": 240, "13": 260, "14": 282, "15": 300, "16": 320, "17": 337, "18": 356, "19": 379, "20": 394, "21": 410, "22": 428, "23": 444, "24": 462, "25": 484, "26": 500, "27": 516, "28": 538, "29": 550, "30": 569, "31": 589, "32": 605, "33": 624, "34": 648, "35": 667, "36": 690, "37": 710, "38": 729, "39": 749, "40": 769, "41": 789, "42": 807, "43": 823, "44": 841, "45": 859, "46": 871, "47": 887, "48": 901, "49": 924, "50": 944, "51": 962, "52": 986, "53": 1004, "54": 1023, "55": 1038, "56": 1055, "57": 1083, "58": 1102, "59": 1138, "60": 1158, "61": 1178, "62": 1198, "63": 1213, "64": 1228, "65": 1248, "66": 1273, "67": 1293, "68": 1311, "69": 1326, "70": 1344, "71": 1354, "72": 1372, "73": 1390, "74": 1405, "75": 1425, "76": 1445, "77": 1465, "78": 1480, "79": 1500, "80": 1510, "81": 1525}
---

**Dave Jones:** Hi, got an interesting teardown for you today thanks to John from Moordale here in Sydney for setting this one into the mailbag. It was too good for the mailbag so we're doing a dedicated teardown video. We love aircraft instrumentation teardowns because they're always rather fascinating and this one's even more fascinating because it's Australian beauty.

**Dave Jones:** It's a MicroAir Avionics T2000 series ATC RBS. It's always known as a transponder. It's an aircraft transponder. This one's, I guess, for light or, you know, it's not for like your 747s or anything. It's more for light aircraft transponder. And anyway, designed and maybe made in Bundaberg in Queensland.

**Dave Jones:** World's best rum up in Bundaberg, Queensland for all you rum aficionados. Anyway, it does comply with various standards around the world so this isn't just an Australian one. I have no idea if this is operational. I have no idea if this is operational or not.

**Dave Jones:** Anyway, it's a transponder system that is part of the air traffic control, the TCAS or the, you know, collision avoidance system where the air traffic controllers, they send or other planes for that matter, can send out a signal on 1030 megahertz and this thing's just continuously receiving 1030 megahertz and then it'll actually, if it gets

**Dave Jones:** a signal, it'll respond with a unique code and the aircraft altitude as well if you've got it in a certain mode. There are different certain modes for this thing. Anyway, we've got antenna input and a D25 output. I don't know what that is.

**Dave Jones:** Maybe some RF adjustments would be my guess anyway. But yeah, so it receives on 1030 megahertz and then it returns what's called the squawk code on 1090 megahertz. So that's how it returns the unique ID. and you can actually set up, if you enter a new air traffic

**Dave Jones:** control airspace, they should contact you and say, you know, please they'll give you an identification, and you apparently enter it here and stuff like that. Sorry, I don't, you know, I'm sure the, there's quite a lot of pilots on the, who watch the EEV blogger and on the EEV blog forum, so I'm sure

**Dave Jones:** they'd tell us all the technical details, but anyway, it's got a dual line dot matrix screen here, have no idea if this one works, and, but yeah, designed and probably manufactured here in Australia, so let's whack this open and I think it's about 140 watts total transmit power

**Dave Jones:** that'd be like the peak, I guess, something like that, so yeah, designed to receive and transmit on the one antenna and, well, let's crack her open, nice screws on top and bottom the front panel, yeah, that'll all pull out, it's very nice, as is common with these aircraft instrumentations

**Dave Jones:** there, I presume that these are like a standard slot size that you put all your instruments in, they're designed to, like, you know, go into the cockpit in, well, you can put them anywhere, I guess any location, and yeah, you dedicate a wire and harnesses, and then you can just chop and change or choose your

**Dave Jones:** different types of instruments, and they all fit into like a standard rack size, I don't know I haven't looked that up, I'm sure it's a standard size just sit right back and you hear a tale, a tale of a fateful teardown, one instrument

**Dave Jones:** had landed on the bench for a five hour teardown a five hour teardown oh, and immediately we're in like Flynn, look at that, love it, all accessible beautiful, shot in glorious 4K for your edification, and there's the crusty D25 the shiny gloss on that board, has that got a little bit of a conformal

**Dave Jones:** coating on it, wouldn't surprise me to find a conformal coating there, some sort of like option board don't really know, but a couple of Melfs down there you know, I'm a Melf fanboy, yeah, but obviously given the D25, so I haven't looked at the pinout for this, so if I can find it

**Dave Jones:** I'll whack it up there, but yeah, this can interface with Garmin and others to get the altitude, like you know, proper altitude information, or it can hook up to barometric pressure sensors, which you can get the altitude information from that anyway, not sure if that's part of a system, but genuine hot snot up there

**Dave Jones:** so to stop the TO220 flapping around in the breeze, another what's it they've bodged, oh that's a diode, is it? yeah, it's a diode-y, and yeah, they've bodged that in more hot snot down here, once again to stop the capacitors vibrating, flapping around in the breeze, because

**Dave Jones:** obviously you get a lot of vibration on an aircraft so, you know, if you just had a freestanding TO220 package like that, it would vibrate loose in next to no time, trust me, I have experience in this where just stuff in a production environment that was wheeled around on a

**Dave Jones:** trolley, you know, even with like a trolley with big, like pneumatic crankshaft, you know, the vibration of that, you know, doing that you know, every, you know, like for three shifts a day, every day for, you know, six months, a year or something, was enough

**Dave Jones:** to just vibrate, just, the TO220, it just vibrated loose and just like snapped off, it just, the fatigue on the legs of this thing, the vibration it just hit the, you know, like it was the right resonant mode or something and it just, bleurgh, eventually just, yeah, fell off, so, that happens, so

**Dave Jones:** anyway, um, yeah, nothing interesting there, we've got a processor, we might have a squiz, there you go, the microchip fanboys go wild, I pick a 17C756 is it? Um, this design, by the way, dates from, uh, 2000, so, I think it's still in, uh, production, actually, I don't know, you know, these things often wouldn't

**Dave Jones:** uh, change over the time, this is the sort of application that you would have that would, um, you know, pretty much not change, you'd just, you know, keep buying the same PIC microchip part, that's why you can still buy you know, PIC micros from, you know, 25, even 30 years ago

**Dave Jones:** maybe, something like that, so anyway, not that unsurprising the PICs have a good following, um, especially here in, you know, designed in Australia this would have been like a go-to, or microchip would have been a go-to uh, micro solution back in, uh, 2000, stuff like that

**Dave Jones:** so, uh, yeah, when was this one manufactured? And of course, you see how I like it there, and, uh, it's like, left a big hole in the, uh, conformal coat, uh, for those who don't know, you, uh, conformally coat boards to keep out, uh, moisture from, uh, being an issue, and like

**Dave Jones:** you know, causing leakage on a board, and, uh, you know, mix it with enough crud and you start getting, uh, like low-impedance shorts, and that can ruin your day so, yeah, conformally coat, uh, stuff very, uh, common to find in aircraft and military, things like that, you know, industrial stuff

**Dave Jones:** where moisture could be a problem. And this side here has to be our RF section, so ta-da! Oh, it's upside down, all the electrons are gonna fall out Ooh, there you go, look at that, that's not your regular FR4 PCB, is it? No siree, Bob

**Dave Jones:** And we've obviously got some distributed element, uh, RF goodness going on here, like that, for example, is a capacitor, a long trace like that is an inductor and the frequencies, even traces, they start becoming inductors, they start becoming capacitors and when you have a large pad like that, so, this is effectively, this could be

**Dave Jones:** say, an inductor, capacitor to ground, because there'll be a ground plane under there, and then another inductor, so that could be an LC filter, and actually it says, uh, receive filter input there uh, plus 50 volts down there, so, now I was gonna say

**Dave Jones:** is there like a masthead amp? I don't think so, um, this is, you know, this is a big power jobby, look at that, it's obviously going, it's bolted, that'd be bolted down to the heatsink block, which is, uh, underneath, no doubt um, absolutely sure of that, looks like we've got a little tuned cap there

**Dave Jones:** so, yeah, that's our transmit section, and this'd be presumably, our receive section, if I can get that cap up that was a bit rude, wasn't it? Uh, there you go, goes under oh, okay, right, oh, it comes back like that, okay and then, oh, okay, and then it goes through a pin there

**Dave Jones:** alright, that makes sense, alright, so that's incoming, got an, uh, LC filter, and then, yeah, that must bugger off onto the bottom side of the board, so we really have to get this, uh, board out, but don't you love the ceramic power packages

**Dave Jones:** try and pull up some info on these, um, yeah, beautiful sure they cost a small fortune, manufactured by Nude Virgins, and, uh, terrific, I don't recognize the, uh, symbol on there so, but I'm sure that the RF aficionados do, um, look at that

**Dave Jones:** that's interesting, like, why that trace there with a whole bunch of V's, and just a cap going over to it, that's fascinating, hmm anyway, um, it's not a huge amount in the RF section, you know you'd need an RF, uh, you know, a power amp, uh, here

**Dave Jones:** and you need an RF receiver and RF filters and that's about it I mean, it's, you know, probably very simplistic and there's the front guts of it, I love how, uh, all that, look at that that's just one big machined piece of aluminium

**Dave Jones:** there, absolutely terrific, there's not many wires going off but, uh, there you go, that'd be another pick, there's absolutely no reason to suspect, uh, that wouldn't be, probably be the same part for bomb reuse, is it? yep, you betcha that's the same no way

**Dave Jones:** I'm sure they'd have, uh, good quality encoders, you know, ALPS or something like that, perhaps and that's just a little LCD backlight down there and that's just the LCD interface connector that's all she wrote, but anyway, it's a, uh, nice neat little compact design, I really like it, well there you go

**Dave Jones:** that's obviously a specific power supply board, I didn't, I thought it was integrated with this one before, but it's not, it's its own interface and this little puppy here is not going to reveal what it is, hmm aha, this starts to get interesting, you'll see that the

**Dave Jones:** D-connector is attached to the, well it's not attached to, but, you know, it's surrounded by that metal plate on the back, and then that, ah, bloody hot snot, and then that just pops out like that, got a little, oh, bit of insulation there, and, ah, discrete wiring inside this thing, not

**Dave Jones:** unusual, ah, to find something like that, oh, look at the MELF resistors oh, gotta love the MELF, MELF, MELF MELF, that'd be a, ah, real pain if you forgot to put that, ah, back plate on before you actually soldered that D-connector in, um, yeah, that'd ruin

**Dave Jones:** your day, but you've been there, done that kind of thing, so there you go, there's a little slot in there, which is not wide enough for the connector, but oh, it's got some ferrites on there too, but I'm sure if you whack it through at an angle, you could eventually get that

**Dave Jones:** out, so, or in or out, so yeah it's all sort of, ah, integrated together, of course um, you know, price is no object, so they're not optimising this thing for, ah, you know, high volume assembly or something like that, you know they'd only make like thousands of these a year or something, it wouldn't be

**Dave Jones:** ah, you know, hundreds of thousands, so, anyway, ah, yeah so, you know, look, that wire's soldered, that's a power supply output, obviously going over to the, ah, transmit and, ah the RF board, and it's just got wires soldered on there, so yeah, you've got to, ah, de-solder those, so there's a

**Dave Jones:** specific, ah, assembly step, and a specific unassembly step, which involves soldering, hmm, yeah, so it looks like we're going to have a transmit block here, and a receive block over there, and little, ah, penetrators going through, each with little, ah, ferrites on them, that'd just be for, ah, power

**Dave Jones:** and, ah, maybe some, ah, control and signal, and that's about it and there we go, there's the bottom of our board you can see that penetrator coming, what I, ah, presume is the transmit block here, and this would be the, ah, receive block, couple of little 10-turn trimmers down in there

**Dave Jones:** and, ah, ah, is that some 7-4H logic? Nothing particularly special down in there at all, there's a bit of analog-y goodness, maybe a couple of op-amps and things, but, ah, not much, again, this is on a special, ah, you know, like a, probably some

**Dave Jones:** sort of Rogers, ah, controlled impedance material, they're tightly specifying this, no doubt you wouldn't just farm this out to one of the $5 PCB makers in China that's for sure, um, no, you'd want to, ah, it'd all be specifically saying, yep, I want this Rogers material XXXX

**Dave Jones:** um, and, yes please. If you desolder the penetrator down in there you get the board out, ah, 11-3, is that 11, I oh, I don't know if that's, no, it says a serial number, 1113 11113, don't know what that is, um, but yeah, you get that out, and, ah, yep

**Dave Jones:** it's all, um, no traces on the bottom there, of course, that could be a multi-layer board, I don't think it is, I think it's all, that's a, yeah, I think that's a single-layer jobby, there it is, for those playing along at home, capture

**Dave Jones:** that in 4K, but yeah, you can see the, ah, you know, serious RF engineering, the, ah, typical cans, you know, if you do, like, I've done I might have to link in, like, a good spectrum analyzer, ah, teardown on stuff like this, and you'll find these sort of, you know, individually, ah, shielded

**Dave Jones:** modules like this on controlled impedance, and, ah, you'll find these sort of, you know, controlled impedance boards with, ah, penetrators, ah, the, ah, go-to thing for getting, ah, signal and power between modules. Two stubborn screws in there, but this will all pop out, so this

**Dave Jones:** is the shielded can, ah, there we go, no wuckers, oh, oh, there we go, there's our channels, oh okay, aha, check it out, this is where the input from our board came in so this is obviously some sort of, ah, cavity filter, they call it a cavity filter

**Dave Jones:** because there's actually a cavity in there, it's an RS cavity filter um, I've, ah, seen these as, like, um, like tubular coaxial, ah, type ones, but yeah, look you can see that each element has a tuned slug inside, so you're able to tune each one

**Dave Jones:** so that's like a five element tuned cavity RF filter Isn't that fascinating? Through there. So there you go. That's what's on this side. And it looks like there's another one under there, is there? I can't see any other reason for these shorties here.

**Dave Jones:** Hmm. Wow, I wouldn't expect it. Like a five-stage cavity filter in something like this. I thought it was a fairly simplistic application, but maybe they need this to get the discrimination required. So, yeah, on the transmit side or the receive side. I assume it's the receive side.

**Dave Jones:** Yes, Dave, of course it's the receive side because, A, we saw the power transistor going directly to the output before, and this, if I flip this over, you might remember that. There you go. There's our RF filter. So here's our input coming back from our antenna.

**Dave Jones:** This is our input, controlled impedance trace, little itty-bitty. So we've got an element filter there on the board, and then that goes into, oh, yeah, the receive filter input, and that is our receive filter. It looks like, you know, a five-stage RF cavity filter, tuned.

**Dave Jones:** Look at that. Wow. So some gray-bearded nude virgin at the factory has to sit there and tune all those. Brilliant. And I'm going to get this board out of here, too, but everything has a procedure, so I've got to get this BNC off

**Dave Jones:** before I can do that. Before I can desolder the pin on the other side to then angle the board out. So, yeah, we're going to have a little leftover bits. All right. I got the pin down there desoldered, all the screws out and everything,

**Dave Jones:** and flappity-doo-dah. Oh, hello. Hello. The surprises aren't done yet, the RF goodness. I've got a bit of rigid coax there. Isn't that fascinating? Fascinating. Wow. I would not have expected that at all. But anyway, aren't these just beautiful machined blocks? Absolutely fantastic. Obviously, this is the base of our output power transistor there.

**Dave Jones:** As I said, it just goes down to the main block, use the entire case as a heatsink. But what is that rigid coax doing? Hmm. So check this out. It seems to go from over this point, to over to here, which the only thing it seems to go to,

**Dave Jones:** is a little trimmer cap on the end there. So is that some sort of, like, tuned stub? Something like that, perhaps. Wow. Fascinating, huh? Fellow engineers, pray with me. Ohm. Ohm. Ohm. Ohm. Ohm. Ohm. Ohm, ohm, ohm. So there you go, if you tuned cap aficionados,

**Dave Jones:** there you go, that's just like right on the end of that rigid coax there. So, yep, and it comes from the output of this bad boy here. I presume it's an output. Lots of little ohm bridges, I'll call them. Why not? 4K screenshot.

**Dave Jones:** Aha, I originally thought that this was a cavity filter, but it's not. It is what looks like a comb, what's called a comb line filter. And you only notice this if you get it out. And you can see the ports down here, they've got little plastic

**Dave Jones:** sleaze inside to then put the little tuning well, they're usually, you know, they're often like screws, tuning screws, but in this case, these little aluminium pins just slide inside there and they cut them off to a certain length and they tune these. So some

**Dave Jones:** grey-bearded nude virgin sits there and tunes these things and then they seal them up with the plastic on the end by the looks of it. And, but the interesting thing about this is that I was wondering why, like, these lengths down here were different lengths.

**Dave Jones:** And I thought, well, maybe it formed part of the cavity, you know, because when it was all together, I thought, oh, you know, maybe it's all like shares a cavity, but it doesn't. And you'll notice that there's no insulation here whatsoever. So this is all connected to the chassis block.

**Dave Jones:** This is just basically, well, there is a hole in the middle of going down here, but apart from that, look at the pins, okay? The pins, there you go. They're just soldered onto the aluminium block there. That's it. It's not like they go through any insulation to a cavity inside.

**Dave Jones:** This, I believe, is a comb filter. I'm sure the RF aficionados will correct me down below in the comments, but basically, this always freaks me out. Right, because this is actually connected down to, like, this chassis is grounded. So effectively, what you're doing is shorting the output

**Dave Jones:** of the antenna. Here it is. The output of the antenna, okay, is going basically through copper, through copper. Sure, these are little inductors, right? And you've got an LC filter there, but then that goes directly into here. So you're basically at DC, mind you,

**Dave Jones:** hold on to your hat before you launch into the comments, DC, then it's, you're shorting the antenna output directly to there. But basically, it comes in here. But because it's one gig, but even shorting direct, effectively shorting directly to ground here, uh-uh, you ain't doing that at one gigahertz, right?

**Dave Jones:** So it's effectively, I'm surprised it's like, it's not going into, like, the top bit here. I'm sure the RF aficionados will tell us why. But anyway, it's going, it's basically going directly into here, and then they're using these as also parts of the circuit.

**Dave Jones:** So, yeah, it's a bit of a machine. But it's also, um, part of the, uh, tuned comb. So this is a, uh, comb filter. And, uh, here's some, like, I found an online comb filter calculator. It's not accurate, but, you know, just, here's some, uh, possible, you know,

**Dave Jones:** you can calculate, uh, these sort of things and how they work, and you can get different types of, uh, comb filters and things like that. But yeah, this is shorted directly to the chassis. You've got the signal. This, this always freaks me out.

**Dave Jones:** Like, it's just, you know, it's, it's RF voodoo, right? When you have the output of the antenna shorted directly to your metal case. Yet, it works, because it's one gig. And things operate very differently at high frequency. But yeah, that's it. There you go.

**Dave Jones:** It's a comb filter with some of the combs actually, you know, um, milled into the grounded chassis. It's absolutely remarkable. Um, yeah. Anyway, I'm sure the, the RF aficionados are really getting excited about that one, 'cause that, that really is just amazing. I'd love to, uh, talk with the, uh, designer about that one.

**Dave Jones:** Yeah, I'm, I'm just surprised, um, to find this sort of thing in just a, you know, a one gig, uh, transmitter and receiver. Well, the, this is a receiver filter. It's not a transmit filter. So, very interesting. Please, leave it in the comments if you've got more detail on that.

**Dave Jones:** So, there you go. That's absolutely fascinating, uh, teardown. And I'm sure a lot of our RF aficionados will, uh, really appreciate the, uh, design effort that's gone into this, uh, bad boy. There you go. Single-sided board. If anyone can, uh, recognize the material, please leave it in the comments.

**Dave Jones:** But, uh, yeah. Um, that's much more RF-y goodness. And, um, certainly more screws. Look at all the, look at all the screws and washers and, and things that I expected to find in here. I expected, you know, an output power tranny to be bolted to the, uh, chassis, and that's about it.

**Dave Jones:** I didn't expect, like, uh, cavity filters and, um, other stuff that we're seeing in here. So, anyway, um, if you've got any idea why they need to go to that sort of effort, as I, I can only think that, you know, it's, uh, discrimination, uh, signal discrimination, uh,

**Dave Jones:** requirements for, uh, you know, the standards or whatnot. Um, but yeah, that's interesting. So, yeah. Cavity receiver and the output, uh, power driver. What is it? Like a three-stage or two-stage thing or, uh, something like that? Anyway, I'm sure somebody will analyze that.

**Dave Jones:** So, as I said, always very interesting, these, uh, industry-specific bits of kit. Aircraft electronics, absolutely fascinating. So, if you like, that, please give it a big thumbs up. As always, you can discuss down below in the comments or over on the EEVblog forum, which each forum, each video gets its own, uh, forum thread to discuss.

**Dave Jones:** That's what I've been doing for the last 12 years, almost since day dot. And, if you haven't joined the EEVblog forum, join it. And, if you haven't joined my other channels over here, please do. I'm currently, like, 44,000 subs on Odyssey or something like that.

**Dave Jones:** So, I'm still, like, like, top 10 in the world for Odyssey, uh, subscribers, growing hugely. And I very rarely say it, but thank you to all my, uh, patrons as well. I've got, like, 1,300, uh, patrons. Oh, the link is always, uh, down below.

**Dave Jones:** And Subscribestar as well. Not, uh, huge growth on, uh, Subscribestar, but I've got, like, 17, uh, subscribers over there on Subscribestar. So, thank you very much for all those who support the channel. Catch you next time. Subtitles by the Amara.org community
