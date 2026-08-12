---
video_id: LI_5ANmkVqo
title: EEVblog #1017 - Enter The World Of Atto Amps
url: https://www.youtube.com/watch?v=LI_5ANmkVqo
source: youtube-asr
timestamps: {"0": 0, "1": 10, "2": 22, "3": 45, "4": 55, "5": 64, "6": 82, "7": 95, "8": 117, "9": 130, "10": 149, "11": 170, "12": 184, "13": 194, "14": 205, "15": 219, "16": 237, "17": 256, "18": 273, "19": 284, "20": 297, "21": 329, "22": 355, "23": 369, "24": 379, "25": 391, "26": 401, "27": 419, "28": 434, "29": 448, "30": 457, "31": 467, "32": 480, "33": 496, "34": 508, "35": 521, "36": 530, "37": 543, "38": 554, "39": 566, "40": 579, "41": 587, "42": 598, "43": 613, "44": 622, "45": 634, "46": 641, "47": 657, "48": 665, "49": 676, "50": 689, "51": 695, "52": 711, "53": 724, "54": 739, "55": 749, "56": 763, "57": 781, "58": 809, "59": 816, "60": 829, "61": 841, "62": 853, "63": 867, "64": 884, "65": 901, "66": 916, "67": 929, "68": 947, "69": 956, "70": 968, "71": 994, "72": 1019, "73": 1033, "74": 1047, "75": 1061, "76": 1073, "77": 1084, "78": 1099, "79": 1111, "80": 1122, "81": 1134, "82": 1146, "83": 1165, "84": 1179, "85": 1195, "86": 1205, "87": 1218, "88": 1224, "89": 1241, "90": 1264, "91": 1280, "92": 1290, "93": 1300, "94": 1311, "95": 1323, "96": 1333, "97": 1346, "98": 1359, "99": 1369, "100": 1382, "101": 1399, "102": 1409, "103": 1421, "104": 1436, "105": 1446, "106": 1459, "107": 1474, "108": 1488, "109": 1502, "110": 1512, "111": 1522, "112": 1535, "113": 1548, "114": 1563, "115": 1580, "116": 1597, "117": 1607, "118": 1621, "119": 1632}
---

**Dave Jones:** Hi, this is a Keithley DMM 7510. It's a pretty schmick 7 and 1/2 digit multimeter, one of the best you can get. So, if we can have a look at what it can measure in terms of low current.

**Dave Jones:** Well, on its lowest range here, our decimal point is here on the microamps range. Move the decimal place three spots over and that's nanoamps. Move it three spots over again and that's picoamps.

**Dave Jones:** So, it basically has one picoamp resolution. Pretty schmick, but eh, this is amateur hour. This is what you want when you're measuring low currents. 35-year-old technology, the Keithley 617 programmable electrometer from the early 1980s.

**Dave Jones:** This is a fantastic bit of kit. Not only can it measure voltage, it can measure ohms. Thank you very much. Gigaohms, hundreds of gigaohms, if you're wanting to go that high.

**Dave Jones:** It can measure cool ohms for those playing along at home. Everyone loves cool ohms. And it can measure current. How low can it go? Well, how high can it go?

**Dave Jones:** Well, look at this, milliamps. No worries, microamps, no worries. Keep going. Ah, keep going. Ah, nanoamps, that's for amateurs. Picoamps, ha, that's for amateurs, too. Let's have a look.

**Dave Jones:** Its lowest range is a two picoamp range. And that's picoamps. That's puff. So, there's our decimal point. If you move, oh, sorry, you can't really black point is hopeless, isn't it?

**Dave Jones:** Move the decimal place three places over, that digit there is femtoamps. This one here is 100 attoamps. Atto. Most people don't even learn what atto is in engineering. It's like, huh, what prefix is that?

**Dave Jones:** 100 attoamps resolution. Now, pretty much there's only a couple of instruments that can well, that like mainstream instruments that I'm aware of that can beat this these days. There are a couple of modern ones that can go down to 10 attoamps resolution.

**Dave Jones:** But, this one can do a 100 attoamps. Absolutely amazing. 35-year-old bit of technology. For those playing along at home, that is 62.5 electrons per second for 100 attoamps. Woah, this is heavy.

**Dave Jones:** So, what do you need something like this for? Well, basic physics and material research, new nanotube research, new polymers, and various other like, you know, real low-current electrochemical type applications where you're pretty much down to the level of counting electrons.

**Dave Jones:** It's ridiculous. Anyway, 100 attoamps resolution. And, please excuse me for turning it on before I take it apart, but I just had to show you that how low this thing could actually go.

**Dave Jones:** And, yeah, we can This is the actual I haven't got I've got nothing plugged into it at the moment. And, we can actually do Well, there we go. I had it on zero there, but there we go.

**Dave Jones:** It's actually counting. If you fart on the other side of the room, this thing's going to change by like 100 counts. So, I'm clenching my butt cheeks. Just I better not breathe, either.

**Dave Jones:** Woah. Anyway, look, we can zero check that, and it's got an internal minus internal one femtoamp offset there, and we can zero we can zero correct that before we take our measurement.

**Dave Jones:** Unbelievable. Now, it's actually got a voltage source output as well, voltage generator, 103 volts maximum. Very nice for powering stuff under test. It allows a higher resistance mode as well using the building voltage source and also it's got some monitor outputs as well.

**Dave Jones:** So you can actually will have a closer look at the schematic up there but it's got the obligatory IEEE 488 GPIB interface and it's also got outputs which tell you that the the completion of the measurement has done and external trigger as well.

**Dave Jones:** So you can trigger it and then it gives you a response when it's taken that measurement. So good for system integration. So you can see that you can actually get a preamp output here and also an amplified analog output as well and that might be handy for once again system integration stuff.

**Dave Jones:** Now of course you can't just use a regular BNC or banana jack inputs for this sort of thing. You've got to use a special low noise triaxial connector it's called.

**Dave Jones:** It's called triaxial because it looks like a regular BNC which is basically a bi-axial and this is actually got a third contact in there that gold one around there if you can see that closely.

**Dave Jones:** So don't just go plugging a regular BNC cable into a triaxial connector you'll bugger it up. So this actually provides a separate internal shield in there as like different for like internal guard different from the external output here and that's critical for really low noise measurements but you'll also find them on very high resistance meters as well ones designed once again they're ultra low current but like thousand very high

**Dave Jones:** voltage system high resistance meters for example will actually use these triaxial connectors for testing at 1000 volts and you know it you can pay like $1000 for a test cable that comes with this instrument but considering that one of these modern instruments is like $7,000 for the base model unit and like $15,000 for the uh for the top of the range model, then, you know, people are used to paying a

**Dave Jones:** thousand bucks for a special low noise triaxial cable manufactured by nude virgins. Now, unfortunately, I don't have a triaxial connector here in the lab handily. I can I'll have to order one so that I can you know, do some better experiments.

**Dave Jones:** So, I'll just plug some sharp probes up at Clacker and see if it's bang on. Let's have a look. Here we go. Tongue at the right angle. Oh, look at that.

**Dave Jones:** Bang on to the least significant digit. Awesome. So, I'm not going to go to the effort at the moment to measure all the other ranges that requires specialized setups to do.

**Dave Jones:** But, suffice to say that if it's bang on on the 1 milliamp range, odds of it being good on the other ranges are high. Confidence is high. Confidence is high.

**Dave Jones:** I repeat, confidence is high. And check it out, the building voltage generator, it works as well. So, let's set it to 5 volts, shall we? There you go. It's only a smidgen out, but this can actually go up to, as I said, a hundred odd volts.

**Dave Jones:** It actually will have an adjustable velocity thing, so should get there reasonably quick. Ta-da! There it is. 100.45, not bad at all. So, basic functionality seems to be there.

**Dave Jones:** Awesome. And I love gear that has the instructions on the top. Look at that. Beautiful. Why can't they do that these days? Anyway, let's do a tear down of this puppy and enter the world of atto amps.

**Dave Jones:** This is going to be interesting. So, what we're going to see inside here is, I'm guessing, this isn't just going to be running via the coax just across the cable over to the PCB.

**Dave Jones:** It's It's to be going into a nice big shielded block or something like that. There's two screws on the back. The rest of it's of course all going to be regular stuff.

**Dave Jones:** There's just going to be some magic on the on the front end. And whoop, yep. We're in like Flynn. And tada, there it is. There's our magic block. That's where all the magic's going to happen.

**Dave Jones:** And look at the external power supply over here. That's hilarious. In fact, oh. That transformer looks like it's bent. That is not camera angle. That's not my eye going wonky.

**Dave Jones:** That transformer is This thing's Can I just bend it back? Jeez. Check out down in the mains import down here. Look at this. It's right near the signal outputs.

**Dave Jones:** Look, not a single toss was given about making it, you know, aesthetically physically separate from the rest of it. But, you know, as long as you got your clearance on the PCB, it's all hunky-dory.

**Dave Jones:** So, what they're doing is running the mains traces down here. There's a little common mode choke there. Running them right down the edge of the board, right past all the active circuitry.

**Dave Jones:** Once again, if the clearance is there, okay, but, you know, it's not exactly modern design technique. And then they've got the the mains real clunking mains power switch on the front there.

**Dave Jones:** Not sure what that puppy's doing there. It's not labeled. I'll have to read the manual on that one. Hmm. Anyway, so I've got our mains input and then our line fuse is next to that.

**Dave Jones:** Oh, and the Motorola 6805 fanboys go wild. There it is in a socket. Thank you very much. And then we've got the obligatory SRAM next to that. Well, I can't read that.

**Dave Jones:** What is that? Is that Yeah, 6116. Of course it is. Absolute classic. And then we've just got our basic ROM. So, of course, 65 6805 processor and the TMS9914 up here.

**Dave Jones:** This is actually the GPIB interface chip and you can kind of tell cuz it's plugged into all the micro on the bus and then they all bugger off up here.

**Dave Jones:** Got some drivers and then it goes over to the GPIB connector. Sorry, IEEE 488. So we've got our date code there, 85. There it is. And yeah, it's some of the other chips down there.

**Dave Jones:** 85. I'm not going to You know, who cares about all the digital stuff? Not me. I want to see what's inside the can. And we've got some AC coupling to the chassis, of course, for our system noise reasons.

**Dave Jones:** Just a couple on there. Look at the braid they've got in there. By the way, little pro tip, when you're using your solder wick, don't throw away your used solder wick.

**Dave Jones:** Actually, you know, keep them in your offcuts from those. Keep them in your past drawer. They're very useful for really low impedance straps like this one. It probably doesn't need the low impedance.

**Dave Jones:** Somebody's put the strap in there, but yeah, they can they can be useful. Keep them. Oh, no. Some of the glue is starting to uh peel off there. Look at that.

**Dave Jones:** That's it. They've got a shield all the way, you know, the entire box is shielded as you'd expect on an instrument of this class. And it looks like the board in here, it's it's all going to be, you know, through hole stuff just like this.

**Dave Jones:** But it looks like they've got it on the one board with the power supply over here. This is, of course, a dedicated analog power supply for this analog section.

**Dave Jones:** The other transformer down here has got its own stuff for all the digital thing. It makes sense to separate those. But yeah, it looks like they've got it all on the one board and calibrated by 1065.

**Dave Jones:** Good on you, 1065. And inspected by 1300. Some of the unsung heroes of Keithley. Wonder where they are now. All right, let's reveal the magic here. Couple of little trimmer holes up there.

**Dave Jones:** You got to trim those at the right right angle. You're not allowed to probe through there unless you've got your tongue at the right angle and you've got a gray beard.

**Dave Jones:** SO, LET'S TA-DA! AH! CHECK IT OUT. OOH, I got some jazzy stuff going on here with this can. We'll take a closer look. But, of course, what you expect to find in one of these things is exactly what we see.

**Dave Jones:** Standoffs here. There is too much leakage on PCBs for this sort of stuff to be going into PCBs. So, we've got ridiculously low leakage relays here. Um we'll have to check those out.

**Dave Jones:** Let me see if I can can't even get a brand ET. Um phone home. Anyway, what you expect? PCBs have too much leakage. They get crap, contaminants, oil, dust, and condensation, all sorts of crap on them.

**Dave Jones:** So, you want point-to-point wiring on this sort of stuff. Teflon standoffs. Uh maybe not maybe they're not Teflon cuz Teflon can actually build up a static charge. Um that can be a trap for young players.

**Dave Jones:** Um but, yeah, you can see our input is going directly over here over to the standoff there into these transform into these relays, which are doing the range switching.

**Dave Jones:** And have you ever seen a 250 gigohm not megohm gigohm resistor before? Well, you have now. That's the input impedance of this thing, by the looks of it. Now, on a quick search, I didn't find anything for these relays here, but I'll have a better look look if I can.

**Dave Jones:** I'll include it, but these are going to be ridiculously low leakage hermetically sealed relays. Now, I've actually done a video on uh talking about one of the designs I did back in the day uh for a company I worked at where it was a once again measuring high resistances um and at high voltages, and we required a relay matrix in like a massive relay matrix, hundreds and hundreds of relays, and all

**Dave Jones:** the problems involved in actually designing one of the those things. It's one of my very old videos from like 7 8 years ago. I'll link it in down below and at the end of this video.

**Dave Jones:** Check it out. And whatever that little metal can there is, it's very important because they didn't want the metal can just flapping around in the breeze, so they had to actually have a strap tying that down to some sort of guard point.

**Dave Jones:** It's probably not going to be ground. It's going to be a guard point. There is a difference between ground and guard point. I might have to do a separate video on that cuz that's kind of an interesting topic in its own right.

**Dave Jones:** Now, you might be able to notice down in there or maybe not. Might be a bit hard, but all the magic of course is happening in our dual FET matched FET pair here.

**Dave Jones:** And you can see that one of the leads just in there and a bugger going into the PCB way too much leakage and whatnot. So, it goes they've bent it out at right angles like that directly to the standoff.

**Dave Jones:** So, you can see that the signal path comes in here from the coax and then it goes through the various relays and then goes to, you know, various input impedances and stuff like that to get the current of course because we're measuring current.

**Dave Jones:** We're going to trans put it through a resistor, measure the voltage across it basically. So, we've got the fixed and here's the fixed 250 gig resistor here. So, that'll be used for the two pico amp range there and that is directly on that node there.

**Dave Jones:** So, everything travels above the boards like, you know, Manhattan style, above the boards Manhattan construction technique, which is a technique of dead bugging components on copper clad board and then just point-to-point wiring.

**Dave Jones:** Might include a photo if there is one. And yeah, so it all stays off the PCB and goes directly into our jewel matched fit there, which of course is going to be a super duper special matched characterized one manufactured by nude virgins with gray beards.

**Dave Jones:** See if we can get the part number on that. It's got a 168 and then an 85 2A on there. Mhm. And T-TG on the front of that and an M.

**Dave Jones:** Is that It's not doesn't look like the Motorola job anyway. If I can pull up any data on that part, I doubt it. Like, you know, this could be a Keithley internal part number.

**Dave Jones:** Um you may not know what that uh jewel fit input is. Anyway, if you blow the ass out of that, uh yeah, good luck getting a new one. So, all you young whippersnappers out there are probably going, "Yeah, what's the big deal?

**Dave Jones:** Like, it's got some relays and a jewel fit input and bloody fancy pantsy triaxial connector, but whoop-de-doo." Um well, he go try and design something like this. Go try and design it, test it, and then get uh you know, a proper controlled uh characteristics in production environment, and you'll find out very quickly how difficult this is to get right.

**Dave Jones:** It's not rocket science, it's electron science. And you'll notice that the grounds are going all over the shop. Not only did did the uh shield here for this uh matched fit uh bugger off to somewhere else over here to some guard uh ground, but well, some guard terminal doesn't have to be ground, but the shielding for this case up here, which is isolated from well, supposed to be, it's touching

**Dave Jones:** there, isn't it? Did that cause an issue? Uh like that eventually touching there cause an issue? It may. It may do. I don't know. Mhm. Anyway, that like this ground is buggering off somewhere else.

**Dave Jones:** The shield for this is buggering off somewhere else. The triaxial I presume that that green wire in there is going into the triaxial shield guard inside there. So, it's buggering off downstairs somewhere, which we don't know about.

**Dave Jones:** And it's getting all this stuff right is not easy. Anyway, I've got ourselves a cat act um hybrid resistor uh network there. So, that's pretty nice. But apart from that, um you know, we've got like the 250 gig resistors.

**Dave Jones:** They're not going to be cheap. I have 100 meg No, 100 I think we've got 100 gig. We've got 100 gig a 250 gig resistor and other There's a 100 meg one in there and various other uh Yep, there it is.

**Dave Jones:** There's your 100 meg one. There you go for the different ranges. They're going down in uh decades, of course, um to give you your different uh ranges. They're the shunt resistors, just like on a micro current, for example.

**Dave Jones:** Except it uses a fancy pantsy FET front end and really high value resistors. It's simply the voltage cross uh the voltage drop across a resistor. But yeah, the real is super duper special.

**Dave Jones:** Aha, if we get down in there, haven't fully removed the board yet, but check out Yeah, the triaxial guard is coming from that point down there, as is the uh shield for the can.

**Dave Jones:** So, it looks like as are two different wires buggering off there, buggering off somewhere else on the board. We've got ourselves a star grounding point there. So, it's all referenced back to that one point.

**Dave Jones:** So, they certainly know what they're doing. And here's the circuitry underneath there. So, that's actually all to do with like the uh the 100-V uh high-voltage uh power supply over here.

**Dave Jones:** And take a look at this and notice something interesting. Look at this big strap over here. This big crimp connector This from the 100-V output over here. They've got that going through what looks like, you know, a massive high-current uh lead.

**Dave Jones:** It's not doing that. It's going over to this capacitor here, which then couples into the ground and that ground is on the output which straps into which has an optional strap into the earth ground which then straps optionally into the output ground over here.

**Dave Jones:** And of course whether or not you include that ground guard strap there is all to do with your system implementation and how you do that. So you have to really know what you're doing when you're playing around you know implementing this sort of stuff and taking serious measurements.

**Dave Jones:** Not only in terms of using the instrument but your system setup and all your system grounding and things like that. It's really important. And looks like those extra system ground wires that star grounding I told you about is going over here.

**Dave Jones:** Looks like one of them's going into the main ribbon cable which then goes back up to the main connector at the top the main analog input board at the top.

**Dave Jones:** And thankfully we have full access to the schematics for this thing and all the theory of operation the whole works. I'll link in the manual down below. The regular manual has the all this stuff in it.

**Dave Jones:** It's not just the service manual that you know you used to be able to get. It's all in the main manual. Fantastic. They don't make them like this anymore.

**Dave Jones:** Anyway, take a look at the notes that they've got for just assembling this PCB. Look freon clean the PCB flow and touch up using rosin flux wash immediately after the flow what flow?

**Dave Jones:** In freon solder the polystyrene capacitors of polystyrene thumbs up love polystyrene they're super stable super stable capacitors used for you know high precision circuits like this one. After the freon you got to do that after the freon wash and then remove flux locally with freon and then clean thoroughly with meth methanol after flow and touch up in dashed areas.

**Dave Jones:** What? Components mounted on Teflon, so they are actually Teflon standoffs. That's interesting. So, uh static mustn't be a problem. Keithley know what they're doing. Uh and must not touch PC board or other components because, yeah, they have to be completely isolated.

**Dave Jones:** So, there you go. They're just like assembly steps. That's just great. And we have the schematic for the AD converter as well. No, it's a they've rolled their own analog-to-digital converter.

**Dave Jones:** It's a constant frequency charge balance single slope job. And well, you can do It's got theory of operation in the manual if you want to go into that. But, yeah, they basically uh rolled their own.

**Dave Jones:** It's not like they just bought Analog Devices ADC. Nah, bugger that. And of course, this is what everyone wants to see, the front end. How do they do this?

**Dave Jones:** Um how do they get like atto 100 atto amps femto amp uh levels on this thing? Well, let's take a look. The input, as you can see, you can see that the uh guard there, the three inputs.

**Dave Jones:** And the guard, as I said, goes down to uh mates down to the motherboard. So, it's all goes around in, you know, various configurations for that star ground and all that.

**Dave Jones:** And you can actually see that there are different symbols used for the different grounds here. And look over on the right-hand side near K301, uh over there that relay, you can see that that's actually a star ground point.

**Dave Jones:** And that might go back to the main board that we actually uh saw back down the bottom, that star ground point down on the bottom PCB. So, as we've seen in the teardown, it doesn't go to the PCB at this point.

**Dave Jones:** It's all uh off-the-board construction that in input signal goes to those those rows of uh standoffs and those relays that we actually uh saw there with the, you know, it's just up in free air.

**Dave Jones:** So, it's not touching the board, so it's completely isolated, air-gapped isolated from everything. Goes into those special squirrel relays, which I still can't find uh any data on those, but they they'd be ridiculously low leakage.

**Dave Jones:** And you can see that, um, ah, if you go through R334355 and 332 there, um, then you can see the 250 gigohm resistor permanently going down to ground. So, that's like 250 gigohms is that permanent input resistance there.

**Dave Jones:** And then the other ones up the top there, right at the very top, there's the 100 gig uh, 330 there. And then 331 100 meg, then they'll go down in decades.

**Dave Jones:** 100 K and so forth for the uh, various ranges. Now, of course, this isn't uh, those don't go down to ground. They're part of the feedback loop. Uh, part of the feedback amplifier.

**Dave Jones:** And of course, if you look at the theory of operation, this is actually a feedback amplifier. So, the uh, the shunt resistor in quote marks, the uh, resistor that the current needs to flow through to convert it to voltage, is in the feedback loop of the op amp.

**Dave Jones:** And the op amp here, you can see it there, U309, a Linear Technology LT101, too. And that's a pretty schmick op amp, but it's only picoamp level input, right?

**Dave Jones:** So, it's not good enough picoamps. Ugh. That's, you know, that's amateur hour. So, they use Q308, the dual matched JFET input, as the uh, high impedance input required to get the attoamp level.

**Dave Jones:** So, this is a very special matched uh, transistor, hand probably hand selected, hand tested, uh, hand graded, everything else. And I looked in the uh, manual, the parts list for it, and they don't actually give a part number.

**Dave Jones:** So, you know, it's super special secret squirrel uh, stuff, presumably. If anyone does know, um, please tell us down below. Anyway, that is what gives you your extremely ridiculously high input impedance.

**Dave Jones:** The only thing that can do the job here is JFETs. Not this MOSFET rubbish, like really special matched uh, JFETs there for the front end. but apart from that, um, that's where all the magic happens and physically as well where the magic happens.

**Dave Jones:** It's all off the board, choosing these components like the matched JFET, like the relays, mounting them off the board, but everything else is just pretty much off the shelf.

**Dave Jones:** The LT1012 and U304 up the top there, whatever that is. They got a volt 6.3 volt voltage reference Zener and you know, like the rest of it's pretty ordinary stuff, really.

**Dave Jones:** So, um yeah, all the special stuff, transistor, relay, Manhattan construction. That's the ticket, laddie. So, there you have it. I hope you enjoyed that interesting look inside the Keithley 617 electrometer.

**Dave Jones:** And these things, they're still available for all sorts of physics and materials research and all sorts of weird and wonderful stuff. Don't have much use in regular electronics, of course.

**Dave Jones:** They might be used in semiconductor, you know, fabs and other places for various things, but you know, your your general purpose electronic lab is not going to need to go down to attoamps like this thing can or even femtoamps, really.

**Dave Jones:** So, you know, you might go picoamps, you know, nanoamps is quite common for low power stuff, but you know, even picoamps is like usually several orders of magnitude beyond what your regular electronics person ever needs to deal with, but these things are very specialized bits of kit.

**Dave Jones:** They have their place. That's why they're so expensive, you know, having the matched FET front end and all the special relays and everything else, you know, and they don't manufacture these in high volume, which is why that they can charge, you know, 7, 8, 10, 15 thousand dollars for these sorts of things.

**Dave Jones:** They are precision bits of kit. Lots of engineering goes into them, but you might look at it and go, oh, you know, meh, whatever, but there's that Try and do it.

**Dave Jones:** I dare you. Try and measure, you know, hundreds of gigohms, teraohms, and femtoamps and attoamps. It's just crazy different world. Anyway, if you liked it, please be give it a big thumbs up.

**Dave Jones:** As always, our high-res teardown photos on evblog.com linked in down below. If you want to discuss it, comments, all that sort of stuff, link to the EVblog forum. Hope you liked it.

**Dave Jones:** Catch you next time.
