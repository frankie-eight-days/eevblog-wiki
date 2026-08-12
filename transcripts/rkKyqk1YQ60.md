---
video_id: rkKyqk1YQ60
title: EEVblog 1395 - Onkyo Repair SUCCESS
url: https://www.youtube.com/watch?v=rkKyqk1YQ60
source: youtube-asr
---

**Dave Jones:** Hi, in our previous episode, our intrepid adventurer was repairing an Onkyo TX-SR607 surround sound thingamajig receiver, and it had a non-working vacuum fluorescent display on the front, VFT. Although like the audio section worked, and everything was fine, and all the power supplies

**Dave Jones:** were fine except for one, which was traced down to on a different board to the front panel vacuum fluorescent display board. This is why we left the previous video because the intrepid adventurer didn't have time to finish it

**Dave Jones:** off that day, but he's back today to determine to find this fault because it was traced down to this board here and the negative 35-V supply voltage minus VP here, which was not being generated, which is the negative voltage required

**Dave Jones:** for the vacuum fluorescent display. And that was not on the vacuum fluorescent display board. It had to go through yet another board over here on the side and then through a right-angle board into this power supply video mux. It's actually

**Dave Jones:** got a video mux on there, so it muxes all the videos and things like that. So, it was narrowed down to that. And when we left off, we had actually tested this transistor here, so we had that and put

**Dave Jones:** it on an external tester, measured fine, it detected it as a transistor, it had gain, but that doesn't mean it's necessarily good. There be could be some weird obscure high-voltage breakdown in the part. When you got semiconductors like this, they can actually

**Dave Jones:** do, you know, weird and exotic things if Murphy's not on your side that day. But anyway, we're going to call that good. We could put in a replacement, but I think that's okay. So, it's got to be some other part here. But unfortunately,

**Dave Jones:** we can't power this all up and then start probing voltages. The All the the transistor was on the top through hole, but the other parts are surface mount on the bottom here, and you can't do that cuz the board has to

**Dave Jones:** plug into this right-angle board over here, which then has to go over to the display board in the front, which then also goes down to this bottom main power amplifier motherboard, which also eventually goes over to the mains power

**Dave Jones:** supply soft start switch. So, in order to power the thing up, all these things have to be connected, and it's otherwise it doesn't work, it doesn't power it up. So, unfortunately, yeah, unless we hack it, it's not easy

**Dave Jones:** to do that. So, we're not going to bother to do that. But, I'm 99% sure that the fault's going to be within here. We've tested this transistor. I think I tested that Zener, although this is a 36-V Zener, so unless you take that

**Dave Jones:** out of circuit and hook it up to an external power supply my 121GW multimeter here only tests up to 15 V. So, unfortunately, yeah, we won't be able to test that unless we hook it up to a power supply, but anyway, I did

**Dave Jones:** actually measure that and it was a diode in one direction, so it's not like it's open or anything. And these caps look okay, although I haven't taken them out, but really a cap like that wouldn't cause a complete failure in this. So,

**Dave Jones:** it's got to be one of the parts here. I think I might have measured that diode and it was okay, but anyway, I think what we've got left is we're going to go through and systematically test every single component in here until we find

**Dave Jones:** it. We'll desolder every component if we have to. So, we'll be we can measure the diodes, we can measure the resistors, although it's unlikely a resistor's gone open or something. Although, this one up here, this is curious. It's got list here.

**Dave Jones:** What this means is that it's a select on different model. So, we've got the SR607 up here, so it should be a 2.2 ohm, but I don't know why it's so drastically different. Look, 2.2 ohms half watt or

**Dave Jones:** 82 ohms half watt. It It just seems ridiculous. That spread in values. But anyway, I don't know if anyone's got any info about that model and why it's 82. It's got to be radically different type of display or something. I

**Dave Jones:** I don't know. Anyway, yeah, let's systematically test every part until we find the culprit. And if we don't find anything, well, then go deeper down the rabbit hole. Hey, I hope it's in there. Okay, so let's just check that zener

**Dave Jones:** again. We can at least check one direction. Yep, see. So, it's you know, it's at least a diode. So, it's not obviously blowing open or anything like that. Yeah, the other diode is on top here. So, it's a through

**Dave Jones:** hole jobbie. That's good. 0.55 that's okay for a you know, like a well, yeah, 1N4003. That's hunky-dory. Let's not look at the caps. Let's measure the easy stuff. We'll measure the resistors. Let's see if one of these is open.

**Dave Jones:** That would certainly explain it. Okay, we've got 220 ohms 1 watt R9001 1 watt here. Had to be on the front because the surface mount 1 watt or it would be quite big. 215 yeah, good enough for Australia. And R9010

**Dave Jones:** and R9010 we've got the SR607. So, we need 2.2 ohms. And it's that one there. Yeah, that looks like a 2.2. It's a pain in the ass to get vertical one here. Not sure if you can see that. That should be

**Dave Jones:** 2.2. Hello. I'm making contact with that. Is that open? There in there. There in there. Solder joints look good. It's open. Huh, when you shot the probes together. Wow, winner winner chicken dinner. That one is open. There it is.

**Dave Jones:** 90 90 10 uh which is a 2.2 uh what half half what, so you know, it's a power jobby. So, this thing is going to heat up um and it it's gone open. That would explain why we're not getting our

**Dave Jones:** negative VP here. Okay, uh now that's kind of embarrassing. That was just uh too uh fixed exposure there cuz of the white paper. If you don't know, you know, you put the white paper in here, then everything else is dark, so you've got

**Dave Jones:** to like fixed exposure and overexpose the damn thing. Anyway, don't count your chickens yet, um but we've found an open resistor which should explain why we're not getting the voltage there. So, that's all it was. All I had to do was

**Dave Jones:** not give up and just spend another 5 minutes on this, but yeah, I had other stuff to do yesterday, so I released the video. And uh yep, that's a potentially all it is. That's the culprit. That explains I'm probably 90%

**Dave Jones:** confident if I replace that resistor, it's going to work again. Um so, yeah, I don't think it's failed due to uh like you know, overcurrent somewhere else cuz our transistor measures fine, our diode measures fine, this resistor here

**Dave Jones:** measures fine. So, you know, that is the main uh current path. So, uh you know, and it's not particularly high power, but there's nothing that's sort of like shorted out and taken out that. I think it's just, you know, it's just heated up

**Dave Jones:** and it's a poor quality resistor or whatever or it's just heated up for so long that it finally just went died in the ass and uh went open. Um I've misplaced the transistor that I took out. It was in the socket here and

**Dave Jones:** I measured it and I've come back today and I can't find it. So, our transistor's missing. D'oh! It's got to be within the 50 square meters of this lab. I found it. I found it. There it is, sitting on the sponge. Oh.

**Dave Jones:** Yes, I know the sponge is dry. So, there is the culprit. It's a little carbon composition jobby, and yeah, half a watt. It looks more like a quarter watt resistor to me. It depends on the temperature. I have done a video

**Dave Jones:** on this. A lot of people don't know that just because a resistor is rated at a quarter watt or a half watt or one watt or whatever, yeah, it can survive at that wattage, but you don't realize that that wattage

**Dave Jones:** is actually rated at a ridiculously high temperature. So, if you're dissipating, you know, half a watt in your half watt resistor, it's getting damn hot. Yes, technically it can survive. It's rated for that, but generally you don't want

**Dave Jones:** your components to get that hot. So, yeah. Anyway, so I have to reassemble this, unfortunately, to test this. I can't just power it up. I've got to like physically go to the effort to at least uh do a modicum of reassembly to test out

**Dave Jones:** theory that that's the resistor, and it should be. I'm 90 plus percent confident, unless Murphy is awake today, then well, we could come a gutser, but Confidence is high. I repeat, confidence is high. So, it's not a lot of effort to put this

**Dave Jones:** back together I get or at least get it to a point where you can actually power the thing up and test your hypothesis but uh test your repair. So, anyway, we'll just put a couple of screws back in there. Just get the boards basically

**Dave Jones:** back. The soft start should power up again. And yeah, it's just a few screws, just in case you don't want to come a gutser and have to unscrew them all again. We'll see if Murphy's sleeping today. All right, it's back together. Let's

**Dave Jones:** power it up. I think I've got plugged in most stuff. Oh, there's a few Hang on. No, is that receiver in the bottom's flapping around in the breeze. Need to put a screw in that. Yeah, you can't see it there, but

**Dave Jones:** there is like a metal um RF tuner on the back. And yeah, that's a metal can and you don't want that flapping around in there cuz it's just secured on the back by two screws. And if you don't put the

**Dave Jones:** screws in, it just flaps around in the breeze in the back and lays on the top of the power supply board down there. So, yeah, I didn't want that. So, that could ruin your day. Well, it released the magic smoke. Will it work?

**Dave Jones:** And now our standby LED's on. What? What? What? What? Oh, it's flashing. Now it's flashing. Wasn't doing that before. Wow. I was wondering if I forgot to plug something back in, but anyway, back in fluorescent display is not on,

**Dave Jones:** but that's that that's a like a logic function. It's detecting something it's not happy about. Let me give it a once over again. I may have forgotten to plug something in. Don't you want to know what it was? The

**Dave Jones:** back of the board here was touching that power supply, which is grounded, and yeah, like what? Yep, and it was it's Let's not do Let's not do it again. Hang on. Oh, no. Hang on. Now it's flashing. I swear

**Dave Jones:** the display was working a second ago. Oh god, it's What's going on? I swear I held it up like this and it was working. Okay, can see the standby LED's on. Hit that. It's not flashing. The display's working. The display's

**Dave Jones:** working, I swear. Look, game. It's very dim. Aux. There you go. TV, tape. It's working. When it What? See? No, it just went and it flashed. No, there's there's some sort of intermittent connection thing. Something's happening cuz I physically

**Dave Jones:** just moved that then. Okay, I'm going to put all these screws back in the back because they do hold all the boards in place. and of course all the boards are right angle connected so you could have a dodgy connection just

**Dave Jones:** by leaving some of the boards flapping around in the breeze. Right, so I screwed it all back together now. You know, the top's not on but yeah, everything's back in place so nothing should be flapping around in the breeze

**Dave Jones:** now and that's a problem with these designs when all the boards are basically held together with certain like physically with screws into the back panel and stuff like that. So anyway, let's power it up. There we go. We've got our standby which should be

**Dave Jones:** the default mode whereas before when we were actually playing around with this, it would actually power up by default on. So I don't believe that's the standard but I think this is correct. So let's hit that. Volume. It's very dim but that's common

**Dave Jones:** for vacuum fluorescent displays and I do remember it being very dim. That just happens with age unfortunately. Yeah, but anyway, it's working again. VCR, DCA, game, aux. It's good enough to make it usable. Like you can actually tweak

**Dave Jones:** the voltage and stuff for the vacuum fluorescent display to make it brighter with age but eventually you're going to come a cropper and they just fail. It's a thing with vacuum fluorescent displays like this. Not much huge amount you can

**Dave Jones:** do about it. We could modify it but I'm happy that it's working. So that is a winner winner chicken dinner. Pretty sure it was dim like this originally. It is a relative's one. I do remember it yeah, slowly dying over the years. It's

**Dave Jones:** pretty old. It's like at least 15 plus years old I think so yeah, anyway, there you go. Yeah, winner winner chicken dinner. We fixed it. It was in the end just a carbon film resistor that went open but I hope you

**Dave Jones:** enjoyed that trip down the rabbit hole, the repair rabbit hole where Uh, to the design and construction of this thing, we just had to, like, you know, slowly eliminate things one by one, check things. It was the last power

**Dave Jones:** supply that that we actually measured. Let that be a lesson to you. Thou shall measure voltages. And in terms of vacuum fluorescent displays, there are ones that are specifically negative 35 V rail that was dead that powered the vacuum fluorescent display,

**Dave Jones:** and that was it. It eventually went open. That happens with those carbon film resistors, you know? It It is one of the failure modes. Um, and yeah, whether or not it's just poorly rated. I mean, half a watt for That looks like a

**Dave Jones:** standard quarter watt jobbie to me. So, yeah, not terrific. So, whether or not it gets hot and everything, I don't know. But, anyway, there you go. Could be poor design. Could just be I don't know. Is this a standard fault in these

**Dave Jones:** sort of units? But, of course, if you were repairing these all the time, you'd, you know, you'd get a like a database of common faults and things like that. It's usually, you know, every product will have like a like a classical Louis

**Dave Jones:** Rossmann repairing his MacBooks. Like, there's, you know, like, half a dozen major things that fail, and that's and that's pretty much it. That covers like 95% of his repairs or something like that. It's just like a handful of common

**Dave Jones:** failures and stuff like that. So, I don't know. If you got one of these and you've had a similar failure, please let us know in the comments down below. But, yep, that's an interesting exercise. And certainly, I don't think, in the end, it

**Dave Jones:** was shorting against the chassis uh, there. It was I think it was just the the connections cuz all the boards in here are basically held in place by like rear panel screws and stuff like that. So, they got board-to-board inner

**Dave Jones:** connection. If there's any dicky contacts in there, when they're all like flapping around in the breeze, you just move something, it can, you know, move two other boards, and it just yeah, and the ribbon cables and stuff like that.

**Dave Jones:** It's It's all a bit how you doing. But, once it's all together, that's fine. That's rock. Yep, still on. Rock solid. There you go. No wackers. So, that works a treat. So, anyway, yeah, in the end, that was a real easy

**Dave Jones:** fix, but sometimes you got to go down that rabbit hole to find it. So, that being said, if you liked it, give it a big thumbs up. As always, discuss down below. Catch you next time.
