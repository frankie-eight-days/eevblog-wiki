---
video_id: n47u2YQytjo
title: EEVblog #909 - Heart Defibrillator Teardown
url: https://www.youtube.com/watch?v=n47u2YQytjo
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 17, "2": 37, "3": 53, "4": 73, "5": 89, "6": 109, "7": 125, "8": 141, "9": 161, "10": 181, "11": 205, "12": 221, "13": 237, "14": 257, "15": 277, "16": 293, "17": 309, "18": 325, "19": 341, "20": 357, "21": 373, "22": 389, "23": 409, "24": 429, "25": 449, "26": 469, "27": 489, "28": 513, "29": 537, "30": 553, "31": 569, "32": 585, "33": 601, "34": 617, "35": 633, "36": 653, "37": 669, "38": 685, "39": 709, "40": 725, "41": 741, "42": 761, "43": 777, "44": 797, "45": 813, "46": 833, "47": 849, "48": 865, "49": 881, "50": 897, "51": 909, "52": 925, "53": 945, "54": 961, "55": 977, "56": 997, "57": 1017, "58": 1041, "59": 1061, "60": 1081, "61": 1097, "62": 1113, "63": 1133, "64": 1149, "65": 1165, "66": 1185, "67": 1213, "68": 1233, "69": 1253, "70": 1277, "71": 1297, "72": 1313, "73": 1333, "74": 1353, "75": 1369, "76": 1389, "77": 1409, "78": 1425, "79": 1437, "80": 1457, "81": 1473, "82": 1489, "83": 1505, "84": 1521, "85": 1541, "86": 1561, "87": 1581, "88": 1597, "89": 1613, "90": 1625, "91": 1641, "92": 1657, "93": 1681, "94": 1701, "95": 1721, "96": 1741, "97": 1761, "98": 1781, "99": 1797, "100": 1813, "101": 1833, "102": 1849, "103": 1861, "104": 1877, "105": 1893, "106": 1905, "107": 1921, "108": 1937, "109": 1953}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. We've got an exciting one for you today. It's an AED, an Automatic External Defibrillator. This one's called the Samaritan Pad, and these are, of course, designed to shock your heart and restart it if you have a heart attack.

**Dave Jones:** Fantastic! Thank you very much to George Miska for sending this one into the mailbag a long, long time ago. Sorry, I've only just got around to it. And this is a fully working one, but, ta-da! It is missing the battery pack. George actually,

**Dave Jones:** it had expired, apparently. So this was the battery pack that was in there. A whole bunch of CR123 lithium primaries in there. Just, you know, ultrasonically welded together. Got some hot melt in there as well to keep them together. Presumably they were, you know, shrink

**Dave Jones:** packaged up or something like that. And they were sitting inside here. Of course it's basically a single use type device. These are primary type things. This is actually one of these, like, public access devices where you might leave them in a public location in a building or, you know, some

**Dave Jones:** other area or something like that. And if somebody's having a heart attack then so goes the theory. Joe Average, hence the name, the Samaritan, a good Samaritan comes up, Joe Average, and uses this thing to hopefully attach to somebody having a heart attack.

**Dave Jones:** But these ones designed for such use are fully automatic, so you really can't kill you know, like a live person if they've just fainted or something like that. They're very smart, they automatically monitor the heart first to make sure. And then they give these LED indicators here.

**Dave Jones:** And it's got voice prompting as well. So this one's only got two buttons, power and shock here. And you turn it on and then it'll voice prompt you whether or not it's an adult or a child because adults will have a different energy

**Dave Jones:** level, shock energy level. Around about, this one's about 150 to 200 joules, but some of these can go up to 300 or 350 joules I've read. This one in particular sets 50 joules for a child, so lower energy. About 1 quarter the energy of an adult.

**Dave Jones:** And we've got our two pads here, it shows you exactly where to put the pads on the person. If it doesn't detect a heartbeat and everything else, or an erratic heartbeat, it decides whether or not to shock person. It'll say stand back and press the

**Dave Jones:** shock button, boom. And it will shock them with a biphasic waveform. And here's a look at the waveform. Around about 10 milliseconds or something like that, it's called biphasic because it goes positive first and negative. Older devices from you know, a few decades back didn't do this, they had a monophasic

**Dave Jones:** one where it only went positive and shocked you. But the newer models like these ones use a biphasic pulse like that. And for those playing along at home, this is the HeartSine Samaritan pad, SAM300P, manufactured by HeartSine Technologies Ltd. in the island, basically Belfast in the United Kingdom, so hi to all my

**Dave Jones:** Irish viewers, to be sure, to be sure. And there's the instructions on the back on how to use it, turn it on, remove the pads, place the pads on the bare chest, stand clear, if advised, press shock button. As I said it's got voice prompting so it'll have like a pre-recorded voice

**Dave Jones:** chip, one of those vocoder type chips pre-recorded in there. And if needed, begin CPR, so I think it only like has one go at it, or something like that. Anyway, certainly with the lithium primary batteries, this wouldn't be. Although you can actually get new pads for it, I think.

**Dave Jones:** Anyway, these were expiring 2017, so I don't know why this one expired, because it says December 2016. But George said that this one had expired, so here's your pads. Jeez, the person wouldn't want to be... Well they are in a hurry, aren't they?

**Dave Jones:** How do these bloody pads come out of here? Oh there we go, you just rip it, so yep. Yes, yes, there we go. So you just get that, you rip it, bingo, these are your two heart pads, there you go. I presume they've got a sticky, yep, and then a sticky adhesive

**Dave Jones:** thing, yep, you peel it off, yep, that's it here. Whoa, that smells nice, that would have a specific dielectric, you know, constant to get, you know, like to actually allow the current to pass and things like that, so they'd be specially designed pads.

**Dave Jones:** So you've got two of those, whip off, put them on the person, oh no, here we go, it tells you this one must go here, this one must go here, so there you go, you've got to get them around the right way. Presumably it's not going to work at all, it might detect it

**Dave Jones:** and if you've got them on back to front, maybe, I don't know, but yeah, there you go. Polarity. It's pretty easy, I mean average Joe could come along and, you know, whack these things on I think. And this one does actually come with a port on

**Dave Jones:** here, check it out, and it actually came with a cable that you plug in, USB cable, so you can actually monitor it. There is like another version of the model from this manufacturer that has like an LCD display that you can get there, actually the cardiac waveform and everything else, but

**Dave Jones:** yeah, so I don't know why you'd, maybe you can use this to monitor to the heart, anyway. And this one's actually reusable, you can actually just whip out the pad and the battery so you can just buy these, and that's quite neat, isn't it?

**Dave Jones:** I like that, so you know, you don't have to just buy an entirely new machine, because these go for about 12, this particular model goes for about 1200 US dollars, and it is a current model, so you can still buy it. So I don't know, you might pay an extra 100 or 200 bucks for the pads

**Dave Jones:** and the battery pack or something, but certainly cheaper than buying a good one. Anyway, you know what we say here on the EEVblog, don't turn it on, take it apart. Now you certainly wouldn't go taking one of these puppies apart if it was powered up, and, or if you've

**Dave Jones:** powered it up recently, because we're going to see a big class capacitor bank in here, which of course stores the high energy pulse, up to 200 joules as I said, for an adult, and 50 joules for a child, so maybe, whether or not they, I don't know

**Dave Jones:** whether or not they control the energy coming from one capacitor bank, or maybe they have two? Not entirely sure, we'll find out, but that's, we expect to find a big capacitor bank in there, electronic switching of course and maybe some inductors to control the

**Dave Jones:** you know, to take the edge off the pulse or something, and are we done? Taking out all the yeah, there's probably clips on here. Anyway let's check it out, and there'll be some micro or some description, and it wouldn't be surprised, it wouldn't surprise me if part

**Dave Jones:** of it's potted, maybe, IP56 rating, but you know, these things have to be quite rugged, it'll be designed to be thrown around and all sorts of stuff, so shock and vibration and moisture ingress and things like that should be well at least on the high voltage parts of it should be handled

**Dave Jones:** fairly well, so I like the little pogo pins on there, anyway, hang on, try and pry it open. Here we go, it was just stuck with age. Ta-da! Oh, we're in like Flynn. Look at that, isn't that lovely? I was wrong about the potting though, there is no potting, and

**Dave Jones:** there's our capacitor bank, we've got 5 caps, they could be in series perhaps, giving higher voltage, we'll check out the specs. We've got our, look at that, there's our switching MOSFETs Presumably they're MOSFETs Let's, yeah, it's interesting, it's all on one board so it's not very complex at all

**Dave Jones:** Let's wiggle these off and get right in there, and I'll show you all the individual parts. Bingo! Oops, check it out, I pulled the entire connector off the bare pins down there for the battery. Oops! And it looks like the whole board is just going to lift out

**Dave Jones:** Except for a, yeah, we've got ourselves the ribbon cable, there we go, which goes down to the, yeah, we've got ourselves the speaker, oh yeah, double-sided load, not a huge amount on the back there, we've got some MELF resistors, you know I'm a MELF, bit of a MELF

**Dave Jones:** fanboy, and of course the high voltage stuff, there's our diodes, look, you can automatically, instantly see they've got a diode across each cap. That's to prevent, and you can see that the caps are all in series, look at that So there's a reason there's a diode across each cap like that, is because

**Dave Jones:** when you charge up caps in series like that, and you discharge them, you don't want any differences in the capacitors to cause one capacitor to actually reverse charge, because then it could well, explode, and the magic smoke escapes, and you don't want your defibrillator

**Dave Jones:** exploding, because it'll cause somebody else to have a heart attack, and there won't be a second defibrillator around to resuscitate them! So yeah, there you go, you can see the ground plane all under there, all the digital stuff, because we're generating high current pulses

**Dave Jones:** down in here, you know, so this is all ground plane around here, that's all for the digital stuff, there's actually, we'll take a look at those but that's a fair beefy amount of digital goodness down in there, but it's not a huge amount to the

**Dave Jones:** energy section at all, we've got a couple of big-ass relays in here, looks like we've got a transformer in there, oh no, that's an inductor, no, I thought that was a transformer for a second, but one interesting thing is that they've got a backup battery, what is the backup

**Dave Jones:** battery for? Well look, I see a watch crystal down in there 32.768 kilohertz, that'd be an RTC chip, why have they got an RTC in this thing? I can only presume that it actually records the time and date of when the incident actually

**Dave Jones:** happened. In which case, well it's may not be that the date will be accurate, but the time may not be accurate because it's presumably set at the factory or whoever installed it in the location, but the thing with these is that they can sit there for years and the

**Dave Jones:** drift, unless you have a really schmick crystal in there temperature controlled or TCXO or something, it's going to drift like, you know like a couple of minutes a year, it could be even worse than that actually, with temperature extremes and things like that

**Dave Jones:** so yeah. Anyway, look, labelled sternum apex. Beauty. And this is a 2007 vintage, thank you very much. Cornell Dublia, for all you Cornell Dublia fanboys, there you go 600 mic, 400 volts working and made in the United States of America. Awesome. If you haven't

**Dave Jones:** heard about Cornell Dublia, they are, yeah, top shelf capacitor brand, so maybe they would have, maybe specifically characterised them for the purpose, maybe not, they're probably I don't know, you could go look up the part number and they're just not the shelf one

**Dave Jones:** probably. But anyway, they do all have an individual sticker on them so does that mean that they're a qualified part? I don't know about the requirements, well, I can tell you that the requirements to get one of these designed and produced and certified for

**Dave Jones:** manufacture and public use would be a ridiculous amount of red tape to actually do this, so maybe the parts in here need to be qualified for this particular use, I don't know. Is anyone in the medical electronics field can tell us if these would have been a, you know, a qualified

**Dave Jones:** certified part for use in defibrillators? Let us know. And if you don't know, anything about 1 volt's reverse on an electrolytic capacitor is going to potentially do some damage to them, so having a single diode across them limited them to under 1 volt, Bob's your uncle.

**Dave Jones:** Guess we should actually read the user manual for this thing, it actually shows that it can do like 3 pulses here by the looks of it, 150 joules, 150 and then 200, so it gives you 1 shock and then waits, presumably waits 122nd CPR pause, so it'll give them a shock

**Dave Jones:** then I guess you're supposed to give them CPR and then shock them again! One interesting part of the PCB here is look, like here's the string, okay, so all the caps are in series like this, okay, they're 400 working volts each, so 1, 2, 3, 4, 5, we've got

**Dave Jones:** 2,000 volts maximum for our capacitor bank here at what was it? 600 mic, and you'll notice that the trace comes across here, cap plus and cap minus so they're actually, this isn't connected to anything except this would be maybe part of the production test jig

**Dave Jones:** or something like that would be my guess, and they've got some looks like some test stickers on here, they've gone through the testing process, so they might put that down to a bed of nails or something like that and then test across the capacitor bank directly

**Dave Jones:** okay, so what we've got here is the charging circuitry, the high voltage step up, because hey, this thing has to be charged to, well somewhere over 1,000 volts, something like that, it's a 2,000 volt maximum pack here, I think it's like normally 1,500 volts or something like that, our battery

**Dave Jones:** is straight into our input terminals here, so this is on the primary side of the transformer, we've obviously got a switching transistor here, I'm surprised that's just flapping around in the breeze, you know I'm not a fan of TO220s just flapping around in the breeze, and we've got a 10 turn trimmer

**Dave Jones:** thank you very much, there's no gunk on that to stick that down, so I don't know if somebody's tweaked that at the factory or not, anyway low impedance path switching the primary of the transformer here then it'll boost up on the secondary and

**Dave Jones:** use it to charge the capacitor bank, so that's obviously the location you want it from a low impedance point of view, so I don't know how long it takes to charge this thing up to 200 joules, and if I hold this up to the light

**Dave Jones:** we can see through the board here, and you can see the ground plane actually goes from primary to secondary over there, so this is not an isolation transformer. Oh, and there's our MOSFET on the back of the board by the way directly on the battery terminal, look at that, straight over to

**Dave Jones:** the secondary side. And this sense circuit here with these high value protection resistors, that's actually sensing the voltage directly across the capacitor bank, so these resistors are obviously providing most of the voltage drop across there, and this isn't so this only needs to be like low voltage amplification

**Dave Jones:** and that's actually a fairly common technique, dropping the voltage across some two high value resistors there, it's a technique to what's used inside these high voltage differential probes, if you don't know you might be familiar with these things, you might think that there's some whiz bang proprietary

**Dave Jones:** isolation transformer technology in there and stuff like that, no, if you want me to do a, I've always wanted to do a tear down or reverse engineering of one of these, and let me know if you want me to do it, and you'll find it's a similar thing, it's basically

**Dave Jones:** high value dropper resistors in here, actually, you know, this is like 101 division ratio up to, you know what is it, yeah, plus minus 700 volts and 700 volts common mode but there's actually no transformer isolation inside this thing. And the inductor that we've got in here looks like it's going to be in series

**Dave Jones:** with the output and in series with the patient under test PUT, P-U-T, PUT, patient under test, there you go, you're a PUT, if you connect it up to this thing, PUT Anyway, the inductor's going to be in series just to limit the energy that's being dumped to you, limit the

**Dave Jones:** rise time of the pulse that's going into you. Now curiously, in older architectures that weren't intelligent like this, they'll just dumb and they just use capacitor relay and inductor switching, they would have the inductor in series to actually create the monophasic wave form, but with the new biphasic

**Dave Jones:** stuff and all super intelligent and timed and everything else it's like, yeah, it operates slightly differently, but I believe but it's still going to limit, you know, you don't want that capacitor bank being dumped, boom, via an instant low impedance straight to the body, so you do want it controlled, so they've obviously got

**Dave Jones:** a choice inductor in there. And you'll notice on the back side of that inductor there's two diodes in series missing here so that's rather interesting. They would have been used to clamp any back EMF from that inductor, presumably but yeah, they've decided not to fit those

**Dave Jones:** there's a couple of missing capacitors over here, don't know what's going on there, but yeah they're the only, there's two obvious emissions. Why they've got two there is because diodes can actually, what they can do is they can fail short, so like as in a short

**Dave Jones:** circuit, that's typical failure mode for a diode, so if you've got one just across there, especially high voltage, high energy stuff like this, if it shorts out, it's going to, could ruin your day. But if you've got two of them, then one, then the other can take

**Dave Jones:** over and bingo, you know, it's not a problem really. So that's not an uncommon technique on high reliability stuff, which presumably this thing has to meet various reliability standards and things like that, so, which is why I'm surprised that, you know, none of the high voltage stuff is actually got

**Dave Jones:** any pot in, and there's a couple of things flapping around in the breeze here, you know vibration, although this one's, like this one's designed to sit stationary in like a, you know, in emergency brake glass kind of situation. It's not designed to, you know, be out in the field

**Dave Jones:** with ambulance officers and things like that, but yeah you know, I'm probably like, there's no celastic anywhere holding anything down or potting or anything like that, but still it's, you know it's obviously good enough. Let's take a look at the main power packages, there's actually

**Dave Jones:** three of these babies here, this one, this one, and this one over here, and these aren't just regular MOSFETs, these are IGBT superfast 1200 volt transistors designed for, you know, really high fast high energy switching, and no surprises for finding those puppies in there at all.

**Dave Jones:** And the other two packages in that little bank there aren't transistors these are actually SCRs, 30TPS12s, once again from International Rectifier, no one hung low rubbish in you know, a medical grade device like this. And SCRs kind of make sense here because what an SCR does of course, might have to do a Fundamentals Friday on them, is that once you trigger

**Dave Jones:** them on the gate, then they stay latched on and they will deliver, they'll stay on and in this case deliver the energy from the capacitor bank through to the PUT, the person under test, and so the rest of once triggered, the rest of the circuitry can like fail, and it doesn't matter

**Dave Jones:** this baby is still going to stay latched on until the energy's bled away and the voltage threshold is you know, over, it's done. So yeah, SCR makes sense. And they're 1200 volt packages, but even those, a small fry compared to the big daddy over here

**Dave Jones:** which is doing all the business, thank you very much an IXIS CS2022 MOFI it's an MOF1, whatever the hell that is anyway, in this fantastic ISO Plus I4 package, and the reason it's called ISO Plus, if you can, maybe you can see it, there's a hugely wide pin spacing

**Dave Jones:** there's two pins over here close together and then massive pin spacing here, I'll flip it over, there it is, there's the massive spacing across there, and that's how they get the 2200 volts isolation of this baby, I mean this is a serious bit of kit, and that's a phase control thyristor

**Dave Jones:** kinda otherwise known as an SCR, let's not get into the differences, but yeah, thyristor, SCR. Same thing. Works the same way, once you latch those things on, bam, they're staying on until the voltage drops down to bugger all. Now please excuse the crudity of the model, I didn't have time to build it to scale or to paint it!

**Dave Jones:** This is the Davecad reverse engineering edition, and I've just done a little bit of reverse engineering, maybe not 100%, but it's going to be close enough for the purposes of today's experiment. And just the, basically the charging of the capacitor bank and the

**Dave Jones:** discharging to the sternum and the apex positive and negative terminals on here. So let's have a look, we've got ourselves the six CR123 batteries over here, obviously, we've got a couple of MOSFETs driving the transformer, and of course that transformer there is that one there, so there's our battery input right there

**Dave Jones:** and that's one of the MOSFETs and the other MOSFET is on the bottom there. So they're just driving the primary of that transformer, there's a current sense resistor, that's that baby there, 68 milliohms, and the secondary of the transformer has just got, well, either

**Dave Jones:** one diode, which is missing, or three in series like this, and that just charges the capacitor bank up. And as we've mentioned before, we've got our five big main storage caps, 600 mic, 400 volts each in series with their reverse protection diodes on there to stop

**Dave Jones:** them charging in reverse sense, limiting the voltage to under a volt to keep the electrolyte safe inside the things, because anything over a volt can damage electrolytic capacitors. Now our output from the cap here, it charges up, okay, so when you first power it on, it'll obviously start this up, it'll charge up the capacitor

**Dave Jones:** bank ready to do a discharge, how long that takes to charge up I don't know, there could be other detection stuff in here, and anyway, we're not gonna actually, there are various, there is another tap point coming off the capacitor bank as well, which goes off to an amplifier.

**Dave Jones:** Anyway, as there are sensing amplifiers directly on the apex and the sternum terminals here, so they just go off to all the control circuitry, etc. Anyway, as soon as you turn on the power, it charges up the capacitor bank, and then it's ready for action.

**Dave Jones:** Now, it's not going to discharge until such time as these two SCRs turn on here to go, and the relay to go out to the sternum, or these IGBTs turn on, or these SCRs here turn on. So obviously these would all be switched off

**Dave Jones:** in the normal state, the relays would be off, so you'd be relay isolated, there's the two relays there, so you'd be completely safe. The big ICSIS SCR is that one there, and the big inductor here, the big storage inductor is that puppy that we've seen in there.

**Dave Jones:** And then we've got the TPS SCR, that one's on the other side here, and two other TPS SCRs which are identical are those two there, and the IGBTs as we've seen are those two on the front there, and the two relays and the two terminals.

**Dave Jones:** And there's the other sense one on which I haven't drawn that, it comes off the main capacitor bank here. Okay, so this is what I think happens when you actually press that shock button. We've got our charge stored on our capacitors here, it's going to go out here, and first of all it needs

**Dave Jones:** to be a positive peak, okay? So our sternum is the positive terminal, our apex is the negative terminal here, so obviously it's not going to be shuttered down here, it's going to go through the inductor and of course that's going to limit the inrush current to the patient

**Dave Jones:** under test, the putt. And then these two SCRs are going to turn on, the relay's going to switch on, and bingo, it's going to go out the sternum through the poor little dude here, like this, and through the dude, and then out, well, please excuse the crudity of this, through the

**Dave Jones:** apex terminal, and then where does it have to go? Well, they have to turn this relay on of course, and then they have to turn this SCR on here. So bingo, like that, so current flows through the poor schmuck like that. And now you can probably see why we need a big beast

**Dave Jones:** 2 kilovolt isolated thyristor here, is because look, it's directly across the capacitor bank there, so which has a maximum of 400 volts times 5, 2 kilovolts so you need a matching 2 kilovolt thyristor in here, and likewise for this little snubber network across the thyristor here, you need

**Dave Jones:** that 2 kilovolt rated cap there as well, but this might come into effect when we go to the negative, so now we have to actually produce our negative poles, but we haven't actually dissipated all the energy in our capacitor bank, because there is no second capacitor bank

**Dave Jones:** in here, no second storage element in order to give us that negative shock pulse, that biphasic response that we actually need. Sure, this inductor's going to charge up, there's going to be some magnetic field in that inductor, but you know, just look at it, you know, it's

**Dave Jones:** tiny compared to any energy storage in these 5 caps, a little tiny magnetic field in there, so that's not going to do the business. So now we need to reroute this so we can use the rest of the energy in our capacitor bank to shock them in the other direction.

**Dave Jones:** Let's give it a go. So I've got some charge still in our capacitor, it's still going to be positive and negative here, so we need to flip it around. So what do we do, okay, we've got our little dude here again, and he's getting

**Dave Jones:** shocked like this, what can we do? Now I'm not sure if the relays actually switch off at this point and then switch back on, they don't necessarily have to, I suspect they may not, because the waveform travels directly negative, so the relays would probably

**Dave Jones:** switch on, but what happens is that these two SCRs here, they turn off, okay, and then they switch on the IGBTs here, so that current so, well, let's draw it, okay, relays on through the IGBT like this, and then through here and this SCR turns off, it was on before

**Dave Jones:** but we go to our capacitor bank, now what haven't we switched on yet? Bingo, our big ICSIS SCR slash thyristor up here, okay, the capacitor bank is now through here like that. So now we've got the positive here, and the negative actually here

**Dave Jones:** because this is negative of the capacitor, that was opposite to what we had before, we had the positive sternum here, and the apex was at the negative, so bingo we've now swapped it over and we shock them in the other direction current is now flowing this direction

**Dave Jones:** instead of that direction like it was before. Too easy. And you'll note also that this TPS SCR down here isn't as highly rated as the ICSIS one up here because we've now got a lower voltage because we're on the negative part of our waveform, it's a lower voltage

**Dave Jones:** lower energy shock, so therefore this SCR doesn't need to handle as high a voltage as this ICSIS one did with the huge monster pin spacing, so here it is that one is not nearly as high rated as that one with its monster pin pitch on there, it's 2 kilovolt isolation

**Dave Jones:** and likewise these two TPSs, they don't have to handle the same as well. You'll also note that the inductor here, there's going to be some back EMF in that, and they did actually put two diodes in series on the back there as we've noted before, but they haven't populated them so clearly

**Dave Jones:** well, they don't care about because these SCRs are switched off so it's not a problem for the patient, it's just a matter of voltage rating for the two TPS parts in series there, but anyway that's it, and of course in this case, this snubber network here

**Dave Jones:** is probably doing something as well, you'll note the two different value resistors in series with those diodes there, so it's probably operating in the negative side like that. So there you go, and hopefully our little putt here is revived. That's the plan anyway

**Dave Jones:** before you just go into CPR. So there you go, I hope you enjoyed that look inside the Samaritan pad AED automatic external defibrillator, and thank you very much George for sending this puppy in, it's really quite interesting, and it's a reasonable design, I just would have expected a bit more mechanical robustness in there

**Dave Jones:** but as I said, it's not really for field use, it's designed for locking in a cabinet and or storing like in an office environment or something. A lot of offices will have one of these and you might have somebody who's done half a day's training

**Dave Jones:** on how to use them or a couple of people, something like that, and well, you hope it's not one person and then that's the person that has a heart attack. Anyway these things are pretty foolproof, because there's a voice prompt and everything like

**Dave Jones:** that, and yeah, by the way, all the voice, oh I didn't look at the voice stuff, there might be a voice chip in there. Oh, hang on. Yep, there it was, hiding under the label exactly what I suspected. It's the classic chip called ISD4004

**Dave Jones:** series, they've been bought out by various companies over the years anyway, I don't know. But yeah, they're still the in thing. Single chip voice recorder, you pre-program in the voices in there, and then this one's an SPIR control, but you know, there are dumber ones

**Dave Jones:** that you can just, you know, like five different playback messages or whatever and you just stroke the pin and boom, it plays it back. So too easy. And there's some more analogue-y goodness and stuff down there, sense amps and you know, things like that.

**Dave Jones:** Maybe I'll post some high-res teardown photos of this puppy, as I do with most teardowns, but if you're interested then you can maybe take a look at that. But anyway, I hope you enjoyed that teardown, thank you very much George for sending that in.

**Dave Jones:** If you want to discuss it, link's down below, and if you liked it, big thumbs up and all that sort of jazz. Yes, it does help with the search engine rankings and you know, Google-fu and things like that, YouTube-fu. Catch you next time.

**Dave Jones:** ...has an ECG function as well, and we took a look at some of the circuitry last time, and well, some people wanted me to play with this. So okay, let's see if we can actually get some ECG data out of this. There we go.

**Dave Jones:** ... ... ... ...
