---
video_id: VIZNmHznYiE
title: EEVblog #861 - Rigol DP832 PSU FAIL & REPAIR
url: https://www.youtube.com/watch?v=VIZNmHznYiE
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 45, "3": 67, "4": 94, "5": 117, "6": 126, "7": 147, "8": 169, "9": 184, "10": 200, "11": 221, "12": 232, "13": 241, "14": 251, "15": 260, "16": 271, "17": 291, "18": 302, "19": 313, "20": 323, "21": 334, "22": 359, "23": 370, "24": 384, "25": 397, "26": 410, "27": 423, "28": 440, "29": 453, "30": 463, "31": 474, "32": 490, "33": 501, "34": 511, "35": 525, "36": 543, "37": 553, "38": 565, "39": 573, "40": 584, "41": 597, "42": 608, "43": 616, "44": 628, "45": 646, "46": 660, "47": 676, "48": 695, "49": 708, "50": 724, "51": 737, "52": 748, "53": 759, "54": 772, "55": 795, "56": 803, "57": 812, "58": 822, "59": 833, "60": 843, "61": 859, "62": 871, "63": 887, "64": 905, "65": 913, "66": 922, "67": 936, "68": 948, "69": 959, "70": 975, "71": 985, "72": 1003, "73": 1014, "74": 1034, "75": 1048, "76": 1072, "77": 1086, "78": 1095, "79": 1105, "80": 1123, "81": 1131, "82": 1149, "83": 1159, "84": 1170, "85": 1180, "86": 1197, "87": 1206, "88": 1217, "89": 1239, "90": 1249, "91": 1261, "92": 1285, "93": 1299, "94": 1314, "95": 1332, "96": 1342, "97": 1360, "98": 1372, "99": 1388, "100": 1403, "101": 1421, "102": 1436, "103": 1447, "104": 1459, "105": 1475, "106": 1489, "107": 1507, "108": 1520, "109": 1530, "110": 1550, "111": 1569, "112": 1583, "113": 1596, "114": 1613, "115": 1632, "116": 1638, "117": 1646, "118": 1657, "119": 1672, "120": 1684, "121": 1699, "122": 1709, "123": 1723, "124": 1732, "125": 1753, "126": 1765, "127": 1779, "128": 1788, "129": 1805, "130": 1816, "131": 1830, "132": 1849, "133": 1861, "134": 1872, "135": 1884, "136": 1897, "137": 1910, "138": 1920, "139": 1942, "140": 1960, "141": 1987, "142": 1995, "143": 2006, "144": 2016, "145": 2033, "146": 2043, "147": 2053, "148": 2067, "149": 2077, "150": 2090, "151": 2102, "152": 2112, "153": 2123, "154": 2134}
---

**Dave Jones:** Hi, you've no doubt seen my Rigol DP832 power supply in many videos before and there's been a few issues with this supply and I have to link in those videos down below if you haven't seen them but something funny happened with this the other day when I shooting some of that high-speed video footage.

**Dave Jones:** I didn't show this because it wasn't really I didn't really get an interesting shot out of it but I tried to shoot some because somebody asked for it try to shoot some high-speed video 1,000 frames per second of a relay actually contact relay in in there actually closing and opening and here's a shot of it by the way it's nothing exciting at all but what I did is I thought oh okay I'll try

**Dave Jones:** and put some current through this thing like the actual contacts on here the two contacts and actually or put a decent amount of power through it and then actually see what happens when I break that power for example or short it out and I didn't get anything out of that but what happened is I think the magic smoke has escaped from my Rigol DP832.

**Dave Jones:** I was using channel one here and I had it set for 30 volts 3 amps it's maximum capability for this channel I a 90 watts so I was basically putting this across the contacts and then I was using another channel to turn on the coil and then I'd activate or deactivate the coil after I press the camera record function to see if I could you know get

**Dave Jones:** anything interesting on the relay but look what's happened on this thing I first of all let's have a look at channel two here I've set channel two to the same 30 volts 3 amp current limit so the maximum it's capable of and if I switch on channel two it does exactly what you would expect bam the output jumps straight up to 30 volts like that I've got no load on there at all so you know,

**Dave Jones:** least significant digit there. Um, and everything's hunky-dory, right? Turn it off and on. But, look what happens to channel one. I've got it set to 30 volts, 3 amps.

**Dave Jones:** I switch on channel one. And even if I leave it for a while, it's it's not going to get up to 30 volts. Look at that. Barely gets Not even going to make 5 volts, I don't think.

**Dave Jones:** It There is something blowing in this thing. Like the output series pass transistor is blown, or something like that. If we have a very quick look at a Dave CAD drawing of a typical output on a power supply like this, and I've done this in various videos, so I won't go through it again, but basically there's a what's called a series pass output transistor here.

**Dave Jones:** It passes, because it's in series, hence the name. It's in series between the internal uh, supply from the transformer and the output. That's your regulation element there. So, it's called a series pass transistor, cuz it passes the current passes the power through.

**Dave Jones:** And there's an error amplifier here, which then taps off a divider on the output. And then there's a reference voltage, which will be uh, your adjustable control coming from your DAC, or from a pot, or whatever on your power supply, which sets your output voltage.

**Dave Jones:** And then this error amplifier just drives your transistor, be it a MOSFET, or a BJT like this. It doesn't matter. There's various configurations. And that error amplifier is just a loop that just keeps this output voltage at a constant level, because due to op-amp action here, these two voltages will the op-amp will do anything it needs to on the output here to keep these two voltages the same.

**Dave Jones:** So, if you set 1 volt here, then you're going to get 1 volt here. It'll drive this transistor and do whatever, and that's how it creates regulation and regulates your output.

**Dave Jones:** And this series pass transistor is a really quite a low impedance. You can think of it that way. So, really that's how it gets all the current through. Okay?

**Dave Jones:** It wouldn't do that if it was a really low impedance. So, when you switch this output on here, even if you got no load, you'd expect it to instantly switch to the 30 volts there.

**Dave Jones:** But we're not getting it. It's just slow this output voltage here is just starting out at zero for example and it's just I don't know slowly slowly rising up.

**Dave Jones:** I don't know if it's linear or what, but it seemed to have tapered off there. And as you saw it was only getting to like 5 volts or something like that even though we'd set it to 30 volts.

**Dave Jones:** It just wasn't getting there. It was taking forever. Whereas the good channel just went switch on bam right up to 30 volts here. So, what's going on? My best educated guess would be that the series pass transistor is blowing because it's the most likely thing to blow when you're shorting the output cuz that's what I was doing.

**Dave Jones:** I was basically shorting the output with the contacts. But hey, this is an adjustable current, you know, lab power supply. It's supposed to do this. I had the current set to 3 amps.

**Dave Jones:** So, if it you know, it should have current limited to 3 amps. Um and I you don't expect lab power supplies to blow when you short them. You expect them to go into current limit.

**Dave Jones:** Everything's fine. But it blew. I'm not sure whether or not it blew when I was turning the thing on or whether I was switching it off and getting back EMF or something.

**Dave Jones:** I don't know. But yeah, I reckon you know, educated guess is that we're blowing the output pass transistor cuz there's no other thing really. I mean it's you know, it's really quite difficult to blow like your error amplifier or something like that.

**Dave Jones:** That's usually got decent protection. And the series pass transistor, you know, often they'll be a diode across here as well a back diode for some protection as well. But I, know, I don't know about the configuration of this particular supply, but obviously for it to slowly ramp up over like a minute and not even get to its set voltage, obviously there's no low impedance here.

**Dave Jones:** It's just leakage trickling or something like that. So, let's see if we can confirm that. The way we're going to confirm this is to use my new BK Precision 8601 DC electronic load.

**Dave Jones:** This is a new model. You've seen my BK Precision 8500 electronic load before. BK Precision were kind enough to send me a replacement. This is their new model. quite similar, but it's got now dual line vacuum fluorescent display.

**Dave Jones:** It's much better functionality and the specs are improved in various ways and things like that. I might have to do a separate video actually tear down comparing the two and doing some comparisons and stuff like that.

**Dave Jones:** Anyway, very nice. So, what we're going to do Okay, I've just got channel one which is our blown output just connected here and I haven't got any I have not got the load switched on, but it will sense the voltage and display it here on the terminals, okay?

**Dave Jones:** So, this is not a load. It's like open circuit high impedance. So, let's switch it on and see if this voltage tracks this. It should So, what we're checking for here and just that we you could use a multimeter.

**Dave Jones:** You don't need to use an electronic load for this, but this happens to work as a nice precision 0.05% voltmeter as well. Excellent specs on the thing. So, basically we're measuring the voltage on the output just to see if it's really on the output terminals here or whether or not the display is just displaying something ridiculous and we might be getting our 30 volts there.

**Dave Jones:** I don't know. Who knows? Let's test it. So, let's switch it on and No, look, the two are tracking. There you go. They're both tracking. So, this is genuinely the voltage on the output.

**Dave Jones:** This power supply is definitely blown. So, just for curiosity's sake, I'm going to actually going to switch this off and see how quickly it drops back down. Yeah, pretty quick.

**Dave Jones:** That's what you'd expect a power supply to drop back down to. Okay, so but now I'm actually going to switch on the load to see if um the output transistor here can actually drive any load at all.

**Dave Jones:** My guess is it won't. I think it's blown and or there's something in the past regulation element that has blown and it can't provide output current. So, we'll put a constant current load, so that's what CC is here, constant current mode.

**Dave Jones:** Um I've set it for a constant current load of 0.1 amp, so it's not high, you know, just a very low current, 100 milliamps, you know, bugger all. So, let's switch that on.

**Dave Jones:** So, I've now got a load on the output. Let's switch it on. What do we get? What? See? Doesn't even Doesn't even charge up now. It doesn't get to anything.

**Dave Jones:** And if I change the constant current on that to like even 0.01, okay, so 10 milliamps. 10 milliamps. Right? It can't even drive 10 milliamps. This thing is buggered.

**Dave Jones:** So, there you have it. I killed this thing by just shorting the output with a relay contact. That's all I did, just opening and closing it. It should have current limited at the 3 amps, you know, I was being a bit brutal to it, but hey, lab supplies supplies like this are supposed to survive shorting the output.

**Dave Jones:** That's the whole idea of having the current limit and the maximum spec to 3 amps. If it can't survive that, it shouldn't damn well let me set it as a constant current.

**Dave Jones:** So, maybe I got some, you know, some back EMF from the contacts opening, the arc or something. I don't, you know, and it killed something in there. But, before I did this, I just start tested.

**Dave Jones:** I actually just had my leads like this um coming out and I just shorted the two leads together and it worked just fine. So, what I'm going to do is just do that on channel two.

**Dave Jones:** I won't try and use the killer relay. I don't want to kill my other uh channel, but yeah, look, I'll show you. I 30 volts 3 amps, okay? Here we go.

**Dave Jones:** Boom. And it's gone down, but it's gone up to 3 amps. There it is. And of course the output voltage is almost zero because, you know, it's just a little drop bit of drop across the leads and everything's hunky-dory, right?

**Dave Jones:** It can survive that just fine. It current limits at the maximum 3 amps, but I effectively did just that by hooking it across these two relay contacts, turning on the coil, and shorting out the contacts.

**Dave Jones:** That's all I did. I swear. It's a shame I don't have footage of it. You know, the unfortunate thing about this power supply is that it's a little hard to troubleshoot.

**Dave Jones:** You can't just open it up and then just probe around. You've got to actually take a few things apart. So, yeah, this may not be easy. But the good news is it's not too bad once you actually swing this top board open like this.

**Dave Jones:** You can you could actually just power it up and leave it open. So, it'd all be a bit hairy-scary, but yeah, you can actually do it. So, you can actually access the bottom board down here and you can access the top board just teetering on the brink of death here.

**Dave Jones:** Now, we've got this is a three-channel power supply, two 30-volt ones, and one 5-volt one. So, I would have I can't remember from the previous teardown which channel was what.

**Dave Jones:** So, as always, follow the money. Follow the wiring. Take it from I think it's this one. I think it does actually go up to here. So, I think we could be in luck in that this top board actually does channel one, which is rather interesting in terms of arrangement.

**Dave Jones:** I would have thought, you know, you'd have your two big ones on the bottom, but nope. It looks like it's this one anyway. Not sure if you can see that, but you can definitely see I can definitely see the wires in this bundle here going off to channel one there.

**Dave Jones:** So, yep, I think that's a winner. I think it's that top board. Nice. And as it turns out, I just happen to have a second board here and you'll know the reason why if you've seen the previous video.

**Dave Jones:** It had to do with the fact that this previous board board had a design fault that used too small a heat sink here. It got way too hot over the maximum junction temperature of the voltage regulator poor design and they had to re-engineer it with this much bigger heat sink here.

**Dave Jones:** So, I've done a separate video on that. So, I just happen to have a board and tada, I should have a spare series pass transistor. You can always tell the series pass transistor, it's the one on the monster heat sink here.

**Dave Jones:** And if that's not a dead giveaway, then once again, follow the money. Here's the two big spade lugs here for the output voltage that goes Look, there's our output current sense resistor.

**Dave Jones:** There we go. It's just tapping off. You can see the two Look, see the two traces coming out there going off to an amplifier in there and that will be doing the current sensing.

**Dave Jones:** But yeah, the two big traces just go off. So, I can't see precisely where those traces go, but there it'll they'll go maybe under the heat sink and into our output series to our series pass transistor right there.

**Dave Jones:** And we can just follow some traces here. Here's negative over a huge cap there and there it is. That negative point there. So, that's how that's going to be our ground and it's snaking its way over to there, which is tada, that the bottom leader of that resistor there and that goes off straight to a spade lug.

**Dave Jones:** So, that's obviously the negative output in this Chinese symbols there even though the silk screen is a bit dodgy on that one. That's going to say negative in Chinese, I'm sure.

**Dave Jones:** And then our resistor jumps across here and that goes to the other huge trace here. So, obviously, they got that directly across the output rail. So, that's a bleeder resistor.

**Dave Jones:** So, what that bleeder resistor is doing is actually discharging the output capacitor. You may have seen it in the shop before, I don't know, right down. There's actually a electrolytic capacitor.

**Dave Jones:** I don't know what value, maybe a couple hundred micro or something like that, directly on the output terminals, a couple hundred microfarads. Um so, that actually just discharges that capacitor, and you saw that.

**Dave Jones:** You remember when we switched the uh the power supply off, even with no load, it dropped back down to zero, and that's the bleeder resistor actually discharging that um output capacitor there.

**Dave Jones:** But, you might be thinking, "Well, how can they get accurate current uh control?" Cuz this is like 0.05% current adjustment and stuff. Um if we've got a constant Basically, a you know, this resistor is going to take a you know, a reasonable amount of current on the output.

**Dave Jones:** Well, you'll notice that current sense resistor is on the other side of this bleeder resistor here. So, the output it's sensing the current going out here, not through there.

**Dave Jones:** So, this can be any value you like. And that transistor is a CEP60N 15, and that's 150-V uh well, 30 or 60 amps, depending on the package, or even higher um N-channel MOSFET.

**Dave Jones:** So, you know, something typical you might find in an output power supply like this. But, this could be the culprit because in MOSFETs have a downside in that they aren't nearly as robust as BJTs, bipolar junction transistors.

**Dave Jones:** They're almost bulletproof. You know, you put in a 2N3055 in your power supply, and Bob's your uncle, right? You're never going to blow that thing. They're just robust as anything.

**Dave Jones:** Whereas, MOSFETs are pretty delicate little flowers, you know? You got to be careful. They can be damaged by ESD or you know, any You got to be careful with them.

**Dave Jones:** Although they have, you know, often much superior performance characteristics. So, there's advantages to using them in series pass applications like this, but yeah, I think we might have come a cropper there.

**Dave Jones:** I can actually see also as that a couple of diodes down in there perhaps for protection. And just for completeness, the series pass transistor is not the only thing in the current path there.

**Dave Jones:** We've also got our current sense resistor that we looked at here. So, just for you know, these are usually pretty robust. It's going to be almost impossible to damage this thing is that really gross overloads.

**Dave Jones:** We'll just check that. Double check it. Yep, it's still intact. Yeah, just as a matter of course. So, there's not much that can go wrong here. As we saw this filter capacitor before, the output of that filter cap, big fat trace there.

**Dave Jones:** Looks like they've got another bleeder resistor on the main filter caps. That's quite nice attention to detail. Big fat trace disappearing under the heat sink. Guess where it's going.

**Dave Jones:** It's going to one side of the MOSFET. And of course, the other side of the MOSFET comes out. So, really that's the only thing in the path. Unless there's as I said, there's some sort of, you know, control circuitry thing blowing, but I don't have the schematic for this thing and that's the last thing that you would expect.

**Dave Jones:** Because when you're mucking around with this thing, shorting the output, and you know that's what you were doing, and then all of a sudden it failed like that, you know, okay, we might have popped the series pass transistor.

**Dave Jones:** That's best guess. So, yeah, you wouldn't go mucking around chasing red herrings down a rabbit hole here with the circuitry unless you've looked at the series pass transistor. But, just as a matter of course, let's see if we're actually getting a voltage on our the input to the pass transistor, the output of that capacitor that sit there.

**Dave Jones:** So, So, just measure that. So, once again, it's unlikely to be uh the issue, but hey, let's uh probe the voltage on the output of that cap just to be 100% sure that it that there is voltage getting to the series pass transistor just as a matter of course.

**Dave Jones:** So, let's switch it on. And Oh. Oh. Hello. It's on. The lights are on, but nobody's home. I'm definitely making I'm making contact. Wow. Something else Something else has blown.

**Dave Jones:** Like uh it's not the capacitor. Something Maybe there's a fusible element. You know, a fuse in here somewhere. It might be a PCB mount fuse that's actually blown instead of I hope so.

**Dave Jones:** Um cuz last thing I want to do is replace the series pass transistor on the heat sink. What a pain in the butt. So, wow, there's no voltage getting to that.

**Dave Jones:** I haven't disconnected anything. All everything's still coming in. All my like even if I disconnected the control cables, it wouldn't have made any difference. That This is nothing to do with actual uh control.

**Dave Jones:** So, wow. Yep. Gone-ski. I'm not on AC. No, I'm on DC. Wow. There you go. It may not be the series pass transistor. My potential apologies to the series pass transistor.

**Dave Jones:** Mhm. Actually, I don't remember any relay. I don't see any relays in this thing. I'm just going to I didn't switch the output on there, but there we go.

**Dave Jones:** I'm switching Hey, there we go. I'm switching the output on. That's interesting. And 1.7 not to it like No. Um no. Okay, that's interesting, but I would have expected a voltage to be there regardless of whether or not I switched on the output.

**Dave Jones:** It shouldn't matter. It should always be energized. That cap should always be powered up. Yeah, no, there's something definitely wrong. I don't know what's going on. Could be being back powered somewhere.

**Dave Jones:** I don't know. No, it's still not right. Bingo, found the culprit. There it is. There's the fuse. Here was the input. Okay, this is the tap coming from the transformer.

**Dave Jones:** You can see it going off here. The big thick traces going off into the rectifier over here. And it's in series with a fuse. There it is. PCB mount fuse.

**Dave Jones:** 17 meg gonsky. Now, ordinarily you might have to take out all these screws down in here. I think there's six or seven of them to get the board out so you can access the bottom of the board to suck out a component like that.

**Dave Jones:** But in this case, we've got easy iron access to it. We just heat up the top one pin at a time, lift it up so we can lift the component out.

**Dave Jones:** No problem. I've taken it out. There it is. Gonsky. And then we just apply some solder to the back to the top there. And then we get our trusty solder sucker or solder wick or whatever floats your boat.

**Dave Jones:** And suck it out. Oh, that lovely sound. So, that we can put it straight back in. Beauty. Bloody stupid cheap ass solder suckers. It came with little these these three little knobby things here and these are supposed to go in the side there and hold the thing on.

**Dave Jones:** Ah, it's a bit dodgy, bro. Ah, there we go. Supposed to lock forward, but moving it around shuffling around on the bench pushed it back. Yeah, bit dodgy, brothers.

**Dave Jones:** There's our culprit. It's a little 5 amp jobby. Now, you know, like 3 amp current limiting on the output. Okay, it's a reasonable value to reasonable value to expect in a design like that.

**Dave Jones:** But why it's blowing? I don't know. It's It's like it was, you know, inrush current from the caps or like what? Why? I don't know. Is it just a cheap ass one hung low brand that's sort of just dodgy and has failed or is there some more systemic design issue here in terms of, you know, actually failing.

**Dave Jones:** I don't know yet. Looks like it's got all the requisite stuff on there. Look at that. UL, it's all all hunky-dory. So, of course with that board I had a direct replacement 5 amp fuse.

**Dave Jones:** No worries. So, I've whacked it in there. Hopefully I've connected everything back up correctly and I'm going to turn it on. Here we go. Big test. Come on. Power up.

**Dave Jones:** 30 volts, 3 amps, switch on. Whoa, 39 volts. Nope. Nope. Nope. Fail. It's not regulating. There's more than the fuse. Aha. And also, it's not just the voltage. Check it out.

**Dave Jones:** It's drawing 0.7 amps, 27 watts. Where on earth is 27 watts going? Wow, that's a lot of power. There's nothing on the output. I swear. Nothing up my sleeve.

**Dave Jones:** Actually, I'm kind of glad that didn't work because it's kind of a bit boring. Just We just popped a fuse. Whoop-de-do. Hmm, this is more interesting. And well, I guess you could say maybe I should have checked the series pass transistor as well, but you know, I was feeling lucky.

**Dave Jones:** Turns out I wasn't. Anyway, but my first guess is still that series pass MOSFET because it's got to be to get 38, 39 volts or whatever it was on the output.

**Dave Jones:** That's probably the transformer tap here. So, it's like it's shorted or something like that where it's drawing those 27 watts. I I don't know. Okay, here we go. You can see some components heating up there.

**Dave Jones:** There we go. I just switched it on and yep. Let's have a squeeze under there. Oh, that little heat sink there. There you go, 60°. It's that little that little tiny that little tiny one in there.

**Dave Jones:** It's not the pass transistor. You can see the pass transistor there. It's not getting that hot at all. It's that puppy. Interesting. And if you're curious to know the rail voltage there, the output of the rectifier and the transformer, there we go, 53 V.

**Dave Jones:** It's a 63 V cap. So, that seems a bit high for a 30 V rail, but I don't know. I can't remember if we've measured this in previous videos or not, but yeah, I don't know.

**Dave Jones:** It seems a bit high, but hey, it's just a transformer and a rectifier. So, I'm sure it is what it is. You can really see that little heat sink there is like 90 7°.

**Dave Jones:** Something like that. I have not got the output switched on, by the way. Wow. So, that's that little puppy in there. Woo. Now, the great thing about having a spare board like this, you can test your hypothesis.

**Dave Jones:** So, let's have a look. I've got it's powered on. The output is not on. And that same heat sink is only you know, 37° or thereabouts. In fact, this little puppy next to it is a little bit hotter.

**Dave Jones:** So, it is uh significantly different. Hmm. But, hang on. I'm not just going to jump in and take that bait. I had a look at the part number on this.

**Dave Jones:** This is a BD136 and a bipolar And these are pretty robust little things. Why is this getting super duper hot? Yet, the main regulator here doesn't. I suspect that there's nothing actually wrong with this.

**Dave Jones:** It's just sinking the current that maybe the failed uh pass transistor here is dumping into this thing. So, yeah, once again, you don't want to chase those um red herrings down a rabbit hole.

**Dave Jones:** So, uh we're let's have a look at the data sheet for this um N-channel MOSFET here. And it's uh gate, drain, and source. Let's go between gate and drain.

**Dave Jones:** Here we go. So, sorry if you can't see that. Doesn't matter. What? 2.5 ohms. That doesn't sound very good between gate and drain. Let's go between drain and source.

**Dave Jones:** What? Look at that. Dead short between drain and source. Gate and source. There we go. Let's swap the probes around. Get a different polarity. Gate and drain again. 2 and 1/2 ohms.

**Dave Jones:** Yeah. Let me have a smell. Yep. Culprit. And if I get our good board, just to show you, let's go between gate and drain again. Here we go. Ta-da!

**Dave Jones:** Open. Exactly what you'd expect. You'd expect the gate to be open. And drain and source. There we go. 4 and 1/2 K. Yep. I think something's gone horribly wrong with the uh pass transistor.

**Dave Jones:** As you'd expect, it's MOSFET little delicate flowers they are. And well, I don't know actually. Hey, look at this board. You know how I showed you before that there were uh uh, some diodes in there.

**Dave Jones:** This is the old board. No diodes in there. Look. Here we go. There's the new one. They've added some diodes. I didn't notice that. So, they've upgraded. Maybe protection on this board perhaps, but huh, maybe a fat lot of good it did.

**Dave Jones:** So, we're at a point that there's a pretty good bet that our past transistor here is failed. So, luckily I have the spare board. I have the exact type.

**Dave Jones:** It's not like I'd have one of these uh, puppies lying in my junk bin. You'd have to be really into um, your past transistors to have one of those.

**Dave Jones:** I might have something maybe kind of sort of would work, but uh, yeah. No, I've got the real one, so I'll just swap it. Well, hello. Look at this.

**Dave Jones:** I have not touched that. I just took the board out from the metal bracket there. Look at the hand solder residue on that. It's nothing. Look, here's another. Um, here's the other in the BD136 on the uh, heat sink.

**Dave Jones:** It's not It's properly um, soldered. And this one? Somebody's had a go at that. Look, you can even see a scratch mark on the board from the iron, I think.

**Dave Jones:** What? And just to verify, we've got it out. Here we go. And nope, that is not normal for a MOSFET. The gate is supposed to be open. Nope, gone ski.

**Dave Jones:** So, there you go. Replaced. Of course, don't forget to put uh, the heat sink compound on the back of the thing first, just a little bit. And uh, make sure you screw it in nice and tight before you do the solder joints.

**Dave Jones:** And we're back in circuit. And let's do the drain and source. There we go, 4 and 1/2 K. I think that's the value we're getting before. Yeah. And the gate.

**Dave Jones:** There you go. Ah, megs. Yep, good enough. Okay, so what are the odds of it working? Well, I don't know with Murphy, you never know. So, everything's plugged back in correctly.

**Dave Jones:** Let's have a whirl. And Come on, you can do it. I've set it to 5 volts as playing around before, so let's switch on. 5 volts. Winner, winner. Let's go right up to 30.

**Dave Jones:** Bingo. We fixed it. It was exactly Well, I'm yet to do a load test, but it was pretty much what I thought in the first place. It was that damn it series pass transistor.

**Dave Jones:** N-channel MOSFET, easily damaged if you don't design your product right. Clearly, there's something wrong with this Rigol if we can just, you know, um uh blow up a series pass transistor like that.

**Dave Jones:** That's just crazy. And we blew the fuse, of course, so that we gave us a bit of early hope that Oh, maybe it's just the fuse, but no, it was the pass transistor.

**Dave Jones:** So, there you go, but it's it was really quite worrying that this transistor had been desoldered. You saw that. It had It had been hand soldered in like I don't know, and I'm not exactly sure why, whether or not it was a production step afterwards.

**Dave Jones:** It could be, that could be a normal production step. In that case, they need to use some um no flux solder or clean it up or something. But, yeah, anyway, um that's it.

**Dave Jones:** Winner, winner, chicken dinner. What the photon is going on here? My BK Precision Load is dead. I I haven't even hooked it up yet. I just get like go to the turn the power on.

**Dave Jones:** Like, I swear this is the same power cord. Look. It works. And I plug it into here. Nothing. What a bloody Murphy? Unbelievable. The damn fuse is blown. Would you believe it?

**Dave Jones:** There you go. Working a treat now. Um it was the correct rating fuse. It was half an amp because you have different cuz this is like a selectable voltage range on the back.

**Dave Jones:** You have different fuse ratings for different mains voltages and it is the label on the back says half amp for 240 V and that's what was in there and it blew.

**Dave Jones:** Replaced it with a half amp and fine. What the I These things just happen. I with monotonous regularity in the EV blog lab. Is it the EV blog curse?

**Dave Jones:** I don't know. All right, let's check this puppy out. Let's switch it on. 30 V. Let's just go the current limits 3 amps. Let's just go constant current 1 amp, shall we?

**Dave Jones:** Just for simplicity, turn it on. Yep, drawing an amp. No worries. Works a treat. So that's all it was. Is it a blowing N-channel series pass transistor in there?

**Dave Jones:** Why? I don't know. Okay, what we're just going to do now is just do some shorts on the output. Once again, set to 3 amps, 30 V, 3 amps, okay?

**Dave Jones:** Boom. There it is. Okay. It's recovered just fine. And Okay. Whoa, hey, there we go. Got some sparks. Woohoo! Beautiful. Catching that? But I know what everyone's thinking. Dave, we want to see the killer relay.

**Dave Jones:** Try it again. Okay, this is exactly the same thing I had when I was shooting my high-speed video. Channel one output here, 30 V, 3 amp maximum limit set is across the normally opened contacts here and I've got second channel here, 12 volts hooked up to the coil.

**Dave Jones:** So, I'm just going to switch it on, and let's see. No. Uh seems to be working. Seems to be working just fine. Fine. Yep. All right, so your guess is as good as mine as to why it died.

**Dave Jones:** But, I swear that's all I was doing to it. And I think I like did it a couple of times. Um I think, you know, three or four times.

**Dave Jones:** I got a couple of shots out of the thing. And uh I can manage to kill channel one in this case. No. No. Seems rock solid now. So, there you go.

**Dave Jones:** I hope you enjoyed that video. It's a bit longer. I got 42 minutes worth of footage. Wow. Sorry. I was I was hoping it'd be a quick, but uh yeah, in the end it was exactly what I thought.

**Dave Jones:** It was the uh series pass transistor in there. And uh that BD139, my guess is it's uh being used to drive the gate um in there. So, because it's high capacitance or whatever these are power uh transistors usually are.

**Dave Jones:** Maybe it's, you know, it's used in there, and that was uh shunting all of that uh power because, you know, the gate, as you we measured it, the gate was like shorted out to the drain and source.

**Dave Jones:** So, it was just dumping everything from the rail. How it was actually measuring it on the output cuz the shunt resistor is out here for the output. But, yeah, I don't know.

**Dave Jones:** You need the circuit or to trace it out or something. Couldn't be bothered, but there you go. Hope you enjoyed that look at uh this troublesome Rigol DP832. This is not the first issue we've had with it, of course.

**Dave Jones:** There's a few been a few notorious issues with it, but I thought they were done and dusted, but apparently not. I don't know. Did I get unlucky, but it doesn't matter.

**Dave Jones:** I would not expect a lab power supply of this price and grade to blow a pass transistor in it. Why? When it was, you know, it should current limit 3 amps, handle it properly.

**Dave Jones:** I have no idea what went wrong. So, maybe Rigol, you should look into it. Anyway, if you liked it, give it a big thumbs up. Catch you next time.

**Dave Jones:** Thanks for watching. If you like this video, click here to watch similar ones. You can also give the video a big thumbs up by clicking down below. Don't forget to subscribe to my channel by clicking the little icon down in the corner here.

**Dave Jones:** You can also sign up for email notification alerts so you get notified as soon as I release a new video. No worries. That's the way to do it. And you can also comment on each video down below and all the hardcore discussions happen on the EEVblog forum.

**Dave Jones:** There's a separate forum thread for each video. And yes, I do read and respond to all comments where possible. And if you want to help support the channel, I accept donations on Patreon.

**Dave Jones:** You can buy merchandise and other things linked somewhere here. Check it out.
