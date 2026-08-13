---
video_id: 9lIC3ZzIht4
title: Junk box Digital Panel Meter Analysis CX101
url: https://www.youtube.com/watch?v=9lIC3ZzIht4
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 16, "2": 31, "3": 41, "4": 61, "5": 76, "6": 91, "7": 106, "8": 126, "9": 141, "10": 156, "11": 171, "12": 196, "13": 211, "14": 231, "15": 256, "16": 271, "17": 291, "18": 306, "19": 326, "20": 341, "21": 356, "22": 376, "23": 391, "24": 416, "25": 431, "26": 446, "27": 461, "28": 481, "29": 501, "30": 521, "31": 541, "32": 571, "33": 596, "34": 611, "35": 631, "36": 646, "37": 666, "38": 686, "39": 711, "40": 731, "41": 746, "42": 761, "43": 786, "44": 801, "45": 821, "46": 846, "47": 856, "48": 881, "49": 896, "50": 911, "51": 926, "52": 946, "53": 966, "54": 981, "55": 1001, "56": 1016, "57": 1026, "58": 1041, "59": 1066, "60": 1081, "61": 1096, "62": 1116, "63": 1131, "64": 1141, "65": 1166, "66": 1181, "67": 1201}
---

**Dave Jones:** Hi! For my battery leakage testing project, I thought it'd be really cool to actually add a voltmeter to every one of the four AA batteries. So I have a separate voltmeter display on there so that we can see if any of the cells actually

**Dave Jones:** go negative voltage, and whether or not that's related to any of the leakage, because it very well could be. So rather, you know, I've got a million multimeters here, but then, you know, this thing could run for months. And, well, continuous, yeah, you can turn off the auto

**Dave Jones:** power off on your multimeter. Usually that's a power on and off option. You can turn off the auto power off, but, you know, the batteries probably aren't going to last. You know, a typical meter with 300 hours? Yeah, it's probably not going to last.

**Dave Jones:** So I thought, I found these old panel meters. I've got a whole bag of these. I actually form a company that I used to work at. I can't remember which one now. But, like thrown out some old gear or something, and I had a whole bunch of these, you know, like a

**Dave Jones:** customized, I think it was part of a customized test rack or something. And, of course, all the circuitry inside was totally custom. It was, you know, of no use. But I saw, I think it was going in the dumpster or something, and I thought, oh, I'm going to, and I had a whole bunch of these panel meters

**Dave Jones:** on it. I can't remember what it did or even if I was involved in it or what. I can't actually remember. But, yeah, they had like dozens of these panel meters. So I thought, ha, I'll throw on those out. So I went in there and I opened the thing up, and sure enough, they had like a pin

**Dave Jones:** you know, a pin header thing on here, so I didn't have to desolder anything. Just pulled them out, snapped them out of the front panel, and I salvaged all of these panel meters. And you've probably seen this before, because I think I used it in the electronic load video, which is probably like a decade

**Dave Jones:** old now, at least. And, yeah, I don't think I've used one since. Maybe, maybe I have. But anyway, I totally forget what model number and spec this thing is. Well, apart from, I think, I believe it's a 2 volt panel meter. Usually they're like 200 millivolt panel meters, because they're 19, I know

**Dave Jones:** that's, I'm pretty sure it's, well, you can probably see the digits on there, can you? I think it's 19999. So yeah, I think, but I think this model is a 2 volt panel meter, or they might be mixed. I don't know, I never actually tested them after I got them out, I just knew that they were working.

**Dave Jones:** So anyway, I thought, I'd just have a look at getting this thing up and running, because I don't know the model, I don't know the pin out or anything, so let's crack it open. And looks like it's got some tabs there, and we'll see if there's a model number inside.

**Dave Jones:** I could probably go and watch my old electronic load video where I think I used this panel meter, maybe I showed how to hook it up, or how to figure out what it did, or whatever, I don't know. But that's pretty boring, watching my own video to get the answer, so I'm going to do it.

**Dave Jones:** There you go, it's got new CX101, yes, I remember that now. Okay. Underscore 1, don't know what that means. Yeah, because there are different variants, and I think these are like, you know, you put the resistors in a certain, or maybe jumpers, or resistors in a certain, maybe down here or, no?

**Dave Jones:** Yeah, anyway, there's a few unpopulated footprints, so yeah, you can get like different voltage range ones. 200 millivolts, 2 volts, 20 volts, maybe even 200 volts, I don't know, although it doesn't look like there's clearance on there really for, you know, a 200 volt jobby.

**Dave Jones:** But anyway, we've got the black blob, KFU. FR4 is just the flammability rating, that's what FR stands for. If you didn't know what FR4 PCB stood for, it's the flammability rating. FR4 technically has nothing to do with the actual, otherwise the material, well, it does, it's all part of the flammability rating, but

**Dave Jones:** your standard FR4 PCB, it actually stands for its flammability, how easily it catches fire and stuff. So there's E162023? Okay, so my, but no, I think that's the model number, the CX101. So let's Google that, shall we? Before we actually do that, it's going to be obvious that I think these two pins over here are your power pins.

**Dave Jones:** It's just obvious, they're going to have them separated, and there might be a link in here also to whether or not you have a common ground or an isolated ground. I want an isolated ground. Because I want to power all four of these obviously from a separate battery, like it's probably like a 5 volt panel meter

**Dave Jones:** or whatever, so a 5 volt source, but then I want the isolated ground. I don't want a common ground, so we should be able to actually measure that with an ohmmeter. So yeah, anyway, let's go have a look. Here we go, CX101 panel meter, new mini-LCD panel meter, circuit specialist, 17

**Dave Jones:** Yankee bucks a pop, 5 volt independent, that's the one, EEVblog, of course it's the EEVblog forum, everything's on the EEVblog forum, let's go look it up. Jeez, this middle button's not working properly. Of course it's on the forum, everything's on the forum, look at this.

**Dave Jones:** Oh, I'd like to build a constant current load like in Dave's video. There you go, it's number 102. And he's confused by the CX101, yeah, BG, BG version, works with common ground. Okay, thing doesn't seem to exist anywhere. A circuit specialist, there you go.

**Dave Jones:** Is this thing discontinued? Okay, so that was the CXBG, so it's the BG I was using, was it? I don't see it, but we just had a dash 1 there. Plain vanilla digital panel meter with ground reference input. It's also got a current

**Dave Jones:** sense shunt, there you go. No, 100k, no, I'm not seeing a current shunt. So maybe you can put one in? I don't know. No, but all those values are way too high for a current shunt. This one, miniature LCD, 5V, common ground, I hope it's not.

**Dave Jones:** The 101B is a 5V version, 101A is a 9V version, the BG is a 5V version which can use a common ground. Okay, right, well, our one is the CX101. So, current shunt's external, okay, there you go, signal to be measured, blah blah blah.

**Dave Jones:** Okay, yeah, that one's definitely common ground. Okay, so it looks like pin 6 is your ground input, like that. 3 and 4 are not connected. Okay, yeah, and then where you want your decimal point, neat. What else have we got? Hey, you can get a pack of 3 on eBay for 55 Yankee bucks.

**Dave Jones:** Glad I got a bag of these. EVblog Forum again! Shenzhen OPL display. CX101 LCD panel meters in stock. Yeah, nah, that's certainly very different. There you go, that one's got the jumpers on there. But it looks like this CX101 is like a thing, and it's probably got a common

**Dave Jones:** pin out. So yeah, here's the A, here's the BG version, so yeah, it looks like this is the modern equivalent. Oh, are they resistors? No, there's not any, no, no, there's no big resistors on the other side, because this one can go up to 1000 volts, that's why it's got the big resistors in there.

**Dave Jones:** So no, not the same thing, but I reckon the pin out's going to be the same. Yeah, 9 volt, 5 volts, common ground, oh goodness, I hope not. Well, we can measure it, and we can test it as well. 0.1%, plus one digit, schmick!

**Dave Jones:** These are really, these are nice panel meters. Two and a half times a second, true differential input and reference. Yeah, those pin outs, oh jeez, that's a dodgy data sheet, isn't it? Can I find better? Ah, this one's better. 100 megaohms input impedance.

**Dave Jones:** Auto zero, 7 to 11, this is the 7 to 11 volt version, or the 9 volt version. Once again, I, yeah, it can go up to 1000 volts. I think this CX101, we might have the OG here. We might have the original gangster CX101 design

**Dave Jones:** here, because this is not the A, this is like underscore one. So, yeah. Anyway, so in negative, so here we have a better pin out, I'm sure that is proper. So there's the common, input low, input high, okay? So you just join all those together, and power source, and okay, so

**Dave Jones:** that's just the common, but that won't be connected over, so that should be isolated from there. Only one way to find out? Let's measure it. So ohms, pins, okay, this is ground, and pin 5, 3, 4, 5. Oh sorry, no, I think it's that one.

**Dave Jones:** So none of these, none of these are connected electrically to the ground. So, ta-da! Floating! Bobby Dazzler. Alright, so let's apply power and see if this is a 5 volt version. Oh, we didn't check that number there, did we? I think that's a 3.

**Dave Jones:** E162023. No, that doesn't seem to, digital multimeter PCB It doesn't really seem to be a thing, does it? Reproductive? No? Okay, this is another one, there you go, E162023 but, once again, it's this, I guess, newer version that has well, it's the one that has the high voltage jumpers and the

**Dave Jones:** dual row pin header on it. Alright, so let's up that to 5 volts, and 200 milliamps, drop it right down, and I've just bodged up a lead here I have this lead, so black, black there, yep, it works! Look at that! And it's slowly going down, that's what I'd expect

**Dave Jones:** because that is capacitive build-up, and yeah, so if you don't touch anything, it will go down. Yeah, so this is 100 meg input impedance this is high, it's not 10 meg, this is really high, so if we wiggle wiggle wiggle wiggle, yeah, around there, yeah, you'll see it go up.

**Dave Jones:** Whoa, hey, I just overloaded it there. And if we short the input, it'll go back down. Okay, so what I've got is another lead here, now that first one I'm going to skip because it's not connected, so I think I might be one short

**Dave Jones:** though, it looks like I have to short that pin to the one next to it, but I can just do that manually I guess, even though the other end is here, and conveniently, so that should be, so I short black, brown, and orange there, apparently

**Dave Jones:** according to the schematic, and that should be our input. So I'll hook that up to another floating power supply here, so not common. So this pin over here is apparently like a reference in and out or something so I'm not sure, but it seemed to be measuring something, so maybe this one's slightly different

**Dave Jones:** maybe it doesn't need, it's got an internal reference and you have to strap it externally to make it work, I don't know. So let's knock, oh sorry, it's offscreen you can't see it, but there's another power supply on the left-hand side here I'm going to take that down to one volt, so I'm going to hook that up, well we get one

**Dave Jones:** where's the other digits? Hello? Maybe if I short the input? No! Short the input does nothing. Okay well, yeah, maybe I have to strap those references. Yeah, you see RFH and ROH, so reference output high and reference high, and reference low, yeah, okay, so 9 and

**Dave Jones:** 10 have to be strapped together. Aha! Something's happened we've got 303, so I just strapped yellow to white there just shorted those together, and ah, there you go, I just shorted the pins out sure enough it went to zero, so, sorry I can't keep this like upright

**Dave Jones:** I need a, there we go, that's better. I'm going to touch the red wire there yeah, goes up, yep, no worries, and short it, goes back down to zero, no problem yeah it needed that, it's got an internal reference, but it needed you to feed that in

**Dave Jones:** so, yep, otherwise it wasn't going to do the business. We'll feed in our 1 volt, and we should, no! It's 200 millivolts alright, maybe that's why, maybe it didn't need the reference. Oh no, but I shorted them before and it didn't go down.

**Dave Jones:** So okay, let me adjust this power supply again 100, yep, yep, so unfortunately it's a millivolt one which is no good for my battery, because obviously the battery's 1.5 volts so 200 millivolts full scale is not going to cut it of course I can use a voltage divider, or I can try and figure out if there's

**Dave Jones:** anything in here, but anyway, it works, we have a nice little 5 volt isolated pedal meter here, very accurate, 0.1% plus one digit, very nice it's upside down so all the electrons are going to fall out. We do have an adjustment pot, which is interesting

**Dave Jones:** for such an accurate thing, they've just tweaked it, they haven't used precision components, so, yeah, unfortunately they're not labelled or anything. Maybe I figured this out before, maybe I should go watch my original video. I can't remember if I used a 2 volt or a 200 millivolt

**Dave Jones:** range for the pedal meter. Do it yourself, constant dummy load There you go, EEVLOG! Look at the old Outium board, I've done a video on that I manually spun that with my 3D space navigator because when you worked at Outium, as soon as you got a job, they gave you a 3D space

**Dave Jones:** navigator, so that you could, they were all the rage at the time, so that you could rotate the boards So I rotated that by hand and did a screen capture, and that's how I got my intro, look at this I put the episode number over there and everything.

**Dave Jones:** My Flying Spaghetti Monster Engineering Religion t-shirt, I need to put that back on the store. So anyway, there's my constant current load, and yeah, I would have just been measuring the voltage across the 1R across the bottom there, so, yep CX101, there it is, yeah, yeah, so I only needed the 200 millivolts because the burden

**Dave Jones:** voltage of that's not good. Ah, here we go, look at that! Common Ground LCD panel, there you go tweaked for zero. No, I can just, I whacked my 100 millivolts in and it measured it fine so I don't know why I thought that I had to use, maybe I found a data sheet back then that said this is what you

**Dave Jones:** use. There's the reference there that you have to tie back, we just did that One of the three pins that are unused at the moment are your decimal points, so you just strap it to whichever decimal point you want to use, it's not like an auto-arranging thing.

**Dave Jones:** Panel meter is designed for 0 to 200 millivolts input, this will do from 0 to 2 volts or 0 to 2 amps, so my display of 1999 will read directly in milliamps with a 1 ohm load. Oh, okay, that's why, I was using a

**Dave Jones:** divider, okay, so yeah, that makes sense, I was using a divider there, and yep, okay, but we don't need that, so there you go, there's my battery capacity logger that I had at the time. I've still got that board somewhere, I'm sure. Geez, look at the date code on that, 2004, wow

**Dave Jones:** I can't remember what I built that for at the time. Yeah, DLJ with a smiley face there, look at that, it's working on something S, S, that's a Sercel part number, so that must have been for Sercel when I was working at Sercel at the time, so yeah, the part number started with S there

**Dave Jones:** so, oh yeah, it's got Sercel on it, there you go. Anyway, that's got nothing to do with this. Oh, pretty comprehensive video, look at this. So anyway, yeah, that's the answer it looks like I didn't figure out a way to internally strap it, it looks like I just used

**Dave Jones:** an external divider there, so in low yeah, so it's just divider, you know, because you've essentially got a, even though I tied this as a common here, you don't have to. You saw it, it worked fine as an isolated thing. Yeah, so I definitely don't want to put that in

**Dave Jones:** because I was just powering it all from the one 5V, so I commode it. But in this case, no, I want to power the power supply, I want to have a separate 5V supply for the four, because I've got four panel meters across four individual batteries that are all electrically

**Dave Jones:** connected together. So yeah, you don't want common ground, you're going to come a gutsy, you're going to short out your battery that'll ruin your day. Although it's not going to explode, it's just an alkaline, you know it'll just get warm. So there you go, that's the answer.

**Dave Jones:** Old school daycad, could have saved myself this video by just simply watching my old video. But that's no fun, is it? Like I could try and reverse engineer it and try and feel like there's nothing written under there, is there? Which reference does it use by the way?

**Dave Jones:** LM285, there you go. Yeah, like if it had like a 2V thing I'm sure they would have labelled it. Not guaranteed, but yeah, it's the nice thing to do. And you saw on the other models that they had it, but yeah, this might be one of the original OGs

**Dave Jones:** just so they're all 200mV. Hey, long shot, if you do actually have a circuit for this or any more details about any potential strapping in there for a 2V mode, then let me know. But it looks like, like I don't see, like there's no 0Ω

**Dave Jones:** jumpers in there. I'd expect to see like a voltage divider thing, like maybe like 2Ω. There's more than, well there's at least that one missing and that one there. They're both missing, R5, Q1, what's that, C? Is that a, no? Yeah, that's a resistor.

**Dave Jones:** So there's 2 resistors missing there, 2 resistors missing there, and if it did actually have a strappable 2V mode, I would have expected to see one of them strapped with a 0Ω in there, just a link bypassing, and if you wanted to put 2V

**Dave Jones:** then you put in your x10 voltage divider in there. So yeah, I doubt that this has 2V capability built in, which is a bit of a bummer. I can put in the external resistors, but yeah, it just adds to the work. I thought I could maybe wire it

**Dave Jones:** straight in. I thought from memory that these were 2V, but that was from my rusty memory of the original video from a decade ago, and I used resistors to use the voltage divider. So I'm going to have to do that here, I'm going to have to do it 4 times.

**Dave Jones:** That's a bit of a bummer, but anyway. Yeah, so if this battery leakage thing does work, then I want to actually design a proper PCB with these 4 panel meters and I'll have the individual cell holders and everything. It'll be quite jazzy, it'll have the 3 555s on it, and yeah,

**Dave Jones:** it'd just be nice to be able to do that. Of course I could data log the batteries as well, we're talking about a month, or months. Yeah, you might leave them there for 3 months, 6 months, who knows? And these panel meters don't use much power,

**Dave Jones:** so I can probably run it off like a, just the panel meters off a battery and they'll run forever. Maybe. Or just a separate 5V external plug pack supply, something like that. Anyway, there you go. Panel meter. It works, but yeah, needs some additional voltage divider doodads.

**Dave Jones:** So if you liked that video, give it a big thumbs up, and as always, discuss down below. Catch you next time.
