---
video_id: kypSsA6EZzc
title: EEVblog #1139 - OCXO Oven Oscillator Repair
url: https://www.youtube.com/watch?v=kypSsA6EZzc
source: youtube-asr
timestamps: {"0": 0, "1": 29, "2": 55, "3": 75, "4": 108, "5": 133, "6": 158, "7": 183, "8": 200, "9": 236, "10": 254, "11": 276, "12": 295, "13": 318, "14": 333, "15": 344, "16": 377, "17": 416, "18": 442, "19": 472, "20": 489, "21": 507, "22": 526, "23": 544, "24": 564, "25": 584, "26": 602, "27": 622, "28": 657, "29": 688, "30": 704, "31": 738, "32": 750, "33": 781, "34": 810, "35": 834}
---

**Dave Jones:** Hi, in a previous video, which I'll link in down below and at the end if you haven't seen it, we took a look at this Australian-made Systron Donner from the early 70s. It's a timer counter / frequency counter, but it's not just a frequency counter. Timer counters do more. Anyway, we looked at the the teardown of this and also trying to calibrate the internal oscillator. It has two oscillators inside it. One is like just a you know, a crusty quartz crystal on the main board inside,

**Dave Jones:** you know, it's not temperature compensated anything like that. So, you know, it's going to be like in the order of like ppm stability a few ppm something like that. Not great. Probably back then, yeah, we're talking like tens of ppm perhaps, but in the back it does actually have an ovenized crystal oscillator, which of course is fantastic and which we want. But unfortunately, when I was tweaking the thing at the back, it's got an adjustment pot to tweak that oscillator.

**Dave Jones:** I couldn't get it working and I thought that I was mucking it like using this thing wrong or anything, but it wasn't. I think there's actually something wrong with it. So, I thought we'd get our Agilent frequency counter here. I've done a couple of videos on this, which I'll also link in how you can actually use a frequency counter as a gravity detector, which is a fantastic video.

**Dave Jones:** Highly recommend you check that out and I also did a ovenized oscillator upgrade on this thing too, I think. Anyway, I've now got this hooked up to the output of the ovenized oscillator on the back here. So, we're getting you know, somewhat over the nominal 10 MHz. So, let me just go and adjust that and see if we can actually make a difference. So, trust me. I got my tongue at the right angle and I'm twirling that and she ain't budging. So, I can take it

**Dave Jones:** all the way it's like a 10 turn pot five or 10 turn pot in there and I can take it like oh I just felt it go to the the end there and I can go to the extreme end on the other way, and it doesn't do any doesn't do diddly squat. So, obviously, there's something wrong. Has that pot, uh you know, broken? Um age There we go. I've gone extreme end the other way. We can't adjust that. You'd expect, you know, I'd at least like a

**Dave Jones:** maybe a 50 or 100 Hz either side of that 10 MHz uh adjustment range there, and we're just not getting it. So, I thought we'd uh crack it open, have a look. So, there's the puppy down in there. We'll see if we can uh extract that out. I don't know like what uh brand or anything. It's really hard to read that green on on the uh nickel finish or whatever it is. So, let's I'm trying I don't know how to get that out. It's got a big strap on there, something like

**Dave Jones:** that, and then all this cabling. Nah. Anyway, hopefully, it's not uh like a soldered shut or anything like that. That'll be a pain. So, it looks like we uh have to get in there. There it is up there. There's a couple of uh couple of screws. If we take those out, maybe it will should uh pop out, and we can get access to the uh strap, the nuts of which are on the uh bottom side there. So, let's give that a whirl. Wow, this is actually the first time I've

**Dave Jones:** noticed like a fan instrument fan getting quite warm. The hub on the back of that, um it's Trust me, that's like it's ridiculous. Like I didn't have it running that long to shoot the intro to this video. Crazy.

**Dave Jones:** So, there's our module monitor PC from uh Pasadena California. Interesting. So, there you go. The oven runs at 115 V AC. Um so, it must get that off a a tap on the uh transformer, cuz this is a 240-V uh unit. Serial number for those playing along at home, and there's the uh adjustment pot in the back, which you can see the thread like it goes all you know, a fair travel in and out there, but I'm getting diddly squat on that. So, let's try and hopefully we can open this

**Dave Jones:** up. So, I think I have to like they've got like a socket on the back of this thing. So, I think I've got to prize it prize it out of the socket there gently. Tada! You like that? Beautiful.

**Dave Jones:** Thing of beauty is joy forever. Yep, Murphy'll get you every time. Look at that. Solder. Time to get a bit medieval on its ass, I think. Meh, slightly medieval. Um trying to unsolder it didn't work. So, yeah, it was really jammed in there. Had to sort of crack her open. So, oops.

**Dave Jones:** Ah, still work. Think like that. Anyway, we've seen inside ovenized oscillators before. We're going to find some insulation. That's just a regular crystal oscillator that they just a particular cut, a more stable cut, but they keep at a temperature and then they insulate it. So, oops. Oh.

**Dave Jones:** Oh, hang on. That's coming out, but the adjustment pot is not coming out. Oops. Oops. There's our crystal. Um so, this is our heating element. You can see the coil wrapped around there. There's our There's our thermistor to regulate the temperature.

**Dave Jones:** Just got a single down in there. Bit of a helping hand from this end. Stubborn as a as a mule, this one. Try and get some pliers and pull the uh the foam insulation out of there. Aha, there we go. I think there's our culprit.

**Dave Jones:** Some solder down in there stopping it from coming out, I think. We'll break that out. It's still caught on some stuff. This is This is real tricky business. Give her a bit of a poke right up the clacker.

**Dave Jones:** I think WE'VE GOT IT. AH! AH, JEEZ. It's not it. There we go. Ah, we're in. We're in like Flynn. See the burn marks down the bottom? That's fairly typical. Now, for those who will no doubt mention it, I don't think that this is asbestos uh insulation here that they've got in this thing. I could be wrong, but I don't think it is. So, you know, any experts out there, please correct me, but I will uh treat it with care. Don't worry about that. Now, this is interesting because

**Dave Jones:** you can see the extensive burn marks on the back of this board, and that's caused by this power resistor, Welwyn, for all you Welwyn fanboys, fantastic. Um this big power resistor here. Now, like like that obviously gets really hot, and is that the heating element? But, like I don't think so because obviously, like we've got our wrapping around the outside here with our uh thermistor there actually measuring the temperature. So, I'm not sure is that like an additional heater or something like that? Anyway, it it is obviously uh

**Dave Jones:** designed to get hot, and there's your board for those that want to see it. There's your 10 MHz crystal. It's uh usually nothing fancy. Um you know, it's it's a nice particular cut or whatever, but uh anyway, the whole idea is that uh you know, you get a decent cut crystal, and you keep it at a uh very narrow temperature uh you know, a defined uh temperature range regardless of what the ambient temperature's doing, and bingo.

**Dave Jones:** Well, hence the name, ovenized crystal oscillator cuz it just sticks it in the oven and keeps it at a fixed temperature. That's why it might take uh some time to warm these things up, but once they're at temperature, they're pretty darn stable. So, desoldered our capacitator, our variable trimmer cap um from this other uh trimmer cap here. I'll measure that one, too. So, we're getting a nominal 15 puff. So, it's not open. Hey, she's working. So, it ain't the trimmer cap.

**Dave Jones:** Trimmer cap, see? You can see the slug coming out now. There you go. That's That's fine. That's gone to the full extension now. Seven puff. That's exactly what you'd expect. Seven puff up to like 20 or something like that. There you go, end of travel. And 20, exactly I called it.

**Dave Jones:** Brilliant. So, there's nothing wrong with the trimmer cap. It's not that. Something else. Well, it's not the other orange cap down there. That measures 100 n, bang on. And that woolen resistor, 925 ohms. It ain't open. Not sure what value it's supposed to be. Can't see it.

**Dave Jones:** Was able to read the value on the side and it does says 1.025 K. So, 920 ohms, well, it's already in circuit. I'd have to desolder it. And yep, desoldered. 1.025, it's marked. Near enough. Ha, that's a 7400.

**Dave Jones:** Classic. Date code on that, 1980. What? This is a like an old retrofit. I assume it's 8000. No, it would have to be They don't do 00 week, do they? And they do 01, so that's not it. Uh, think we might have our culprit.

**Dave Jones:** One sad-ass looking burned tantalum there, which was close to the resistor. In fact, it's just physically tied onto there. And bloody LCR meter turned off. Trust me, it's You won't have to trust me. Look at the value. Come on. Slow as a wet week. Ha, look at that.

**Dave Jones:** It's It's It's a short. Don't pull little tantalum. Jeez, why would you design it connected to the power resistor? Crazy. That's one poor little bastard. 2. I can still read it though. 2.2 Mike 25 volts. So Please excuse the crudity of the model.

**Dave Jones:** Didn't have time to build it to scale or to paint it. We'll just wax some film caps in there. Going to put another 10 in there. So yeah, whack a film cap in just to power it up again and just like see if that was the problem. And that's if it's not then that's probably as far as I I could be bothered to take it I think.

**Dave Jones:** All right. For the purposes of today's experiment we'll just leave it flapping around in the breeze. So let's switch her on and uh see. Yep, we've still got 10. That's a good start. Still oscillates and it's higher than before, isn't it? A couple of hundred hertz higher. All right, let's trim this.

**Dave Jones:** Got to be careful not to touch anything cuz it was high voltage. We're trimming. Wait, no we're not. Yeah, it's going down. It's going down, but I don't think it's going to go all the way with LBJ. So but it is certainly certainly trimming. You know, what is that? A 10 hertz adjustment range or something like that? Yeah, it's coming down. I think I need to I think it needs time to time to warm up in its original uh configuration before it Yeah, yeah, it's dropping. So I think we have a winner

**Dave Jones:** winner chicken dinner. Um but yeah, I'd like I'd have to physically reassemble it. That capacitor arrangement with the films that were too physically big. I'd have to do it, but I think we've proven that it actually has fixed this thing. And so that's what it was. I mean the cap was connected right up to the power resistor like that physically connected so the heat's conducting through the leads as well as being radiated so like they were burn you can see the burn marks on it and stuff like

**Dave Jones:** that. So there you go. Um It was a It was a tantalum. So, for this video, I'm just going to finish this one up quick. I At the moment, don't have time to go find a suitable physical form factor cap for in there and and replace the thing in physically.

**Dave Jones:** Like, you wouldn't do this like long-term. Like, especially for like a a frequency counter of this age, like you wouldn't like an eight-digit counter of this age, you probably wouldn't bother. So, I just sort of did this as like a troubleshooting exercise video. If you were serious about this, I've got an external 10 MHz reference anyway. I wouldn't bother using the internal ovenized oscillator. I've already got this one with a probably a much better ovenized oscillator in it anyway if I wanted stand-alone without my external 10 MHz rubidium reference.

**Dave Jones:** Geez, you can see it really uh really dropping now. So, it's going to come down. Thermally, it's not very good. It's you know, the coil's half out there. Maybe I'll get the thermal camera. Oh, I'll tell you what.

**Dave Jones:** That uh that yellow wrapping around the thing in that coil that I said was like on here, in fact, it looks like um that's not working The power resistor in there is not working. There it is there. Like, it looks like nothing's heating up. Even that spot there is like is nothing. That's just like where I touched it. So, really um nothing to see here. Move along now. Um it's just not heating up at all. So, yeah, I wouldn't even bother like fixing this old crappy uh Well, I'm sure it was

**Dave Jones:** good for the day, but you know, this what you know, 45-year-old ovenized oscillator wouldn't bother. Like, you would get um you know, if you really wanted to uh restore this and put an ovenized oscillator in it, then you would simply just buy one of the new you know, or refurbished uh 10 MHz oscillators like a ovenized oscillators like I did for this one. Oh, it's coming back down. There you go. We could eventually trim that one right in. but uh yeah, I you know, you would get one

**Dave Jones:** of those um ovenized oscillators um and there's plenty of room inside this to retrofit it if you really wanted to. So, anyway, yeah, I'm not going to uh not going to bother repairing that uh I just wanted to troubleshoot. So, I hope you found that interesting. We can call it a repair even though we didn't uh finish the job off, but a troubleshooting and repair. If you like that video, as always, give it a thumbs up. Comment down below.

**Dave Jones:** Catch you next time.
