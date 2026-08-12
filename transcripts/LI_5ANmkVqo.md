---
video_id: LI_5ANmkVqo
title: EEVblog #1017 - Enter The World Of Atto Amps
url: https://www.youtube.com/watch?v=LI_5ANmkVqo
source: youtube-asr
timestamps: {"0": 0, "1": 12, "2": 27, "3": 50, "4": 64, "5": 86, "6": 109, "7": 125, "8": 143, "9": 165, "10": 184, "11": 196, "12": 209, "13": 227, "14": 242, "15": 260, "16": 273, "17": 287, "18": 303, "19": 322, "20": 339, "21": 354, "22": 369, "23": 384, "24": 396, "25": 414, "26": 429, "27": 444, "28": 460, "29": 474, "30": 493, "31": 511, "32": 525, "33": 539, "34": 552, "35": 566, "36": 581, "37": 592, "38": 608, "39": 622, "40": 636, "41": 648, "42": 661, "43": 674, "44": 689, "45": 698, "46": 714, "47": 730, "48": 747, "49": 763, "50": 780, "51": 794, "52": 809, "53": 821, "54": 834, "55": 844, "56": 861, "57": 877, "58": 890, "59": 909, "60": 924, "61": 938, "62": 956, "63": 968, "64": 983, "65": 1000, "66": 1014, "67": 1030, "68": 1047, "69": 1061, "70": 1073, "71": 1084, "72": 1102, "73": 1118, "74": 1132, "75": 1144, "76": 1162, "77": 1176, "78": 1189, "79": 1205, "80": 1218, "81": 1229, "82": 1251, "83": 1266, "84": 1282, "85": 1297, "86": 1309, "87": 1323, "88": 1336, "89": 1351, "90": 1363, "91": 1377, "92": 1393, "93": 1406, "94": 1421, "95": 1433, "96": 1448, "97": 1467, "98": 1480, "99": 1498, "100": 1512, "101": 1528, "102": 1543, "103": 1559, "104": 1574, "105": 1588, "106": 1601, "107": 1619, "108": 1632}
---

**Dave Jones:** Hi, this is a Keithley DMM 7510. It's a pretty schmick 7 and 1/2 digit multimeter, one of the best you can get. So, if we can have a look at what it can measure in terms of low current. Well,

**Dave Jones:** on its lowest range here, our decimal point is here on the microamps range. Move the decimal place three spots over and that's nanoamps. Move it three spots over again and that's picoamps. So, it basically has one picoamp resolution.

**Dave Jones:** Pretty schmick, but eh, this is amateur hour. This is what you want when you're measuring low currents. 35-year-old technology, the Keithley 617 programmable electrometer from the early 1980s. This is a fantastic bit of kit. Not only can it measure voltage, it can

**Dave Jones:** measure ohms. Thank you very much. Gigaohms, hundreds of gigaohms, if you're wanting to go that high. It can measure cool ohms for those playing along at home. Everyone loves cool ohms. And it can measure current. How low can

**Dave Jones:** it go? Well, how high can it go? Well, look at this, milliamps. No worries, microamps, no worries. Keep going. Ah, keep going. Ah, nanoamps, that's for amateurs. Picoamps, ha, that's for amateurs, too. Let's have a look. Its lowest range is a two picoamp

**Dave Jones:** range. And that's picoamps. That's puff. So, there's our decimal point. If you move, oh, sorry, you can't really black point is hopeless, isn't it? Move the decimal place three places over, that digit there is femtoamps. This one here is 100 attoamps.

**Dave Jones:** Atto. Most people don't even learn what atto is in engineering. It's like, huh, what prefix is that? 100 attoamps resolution. Now, pretty much there's only a couple of instruments that can well, that like mainstream instruments that I'm aware of

**Dave Jones:** that can beat this these days. There are a couple of modern ones that can go down to 10 attoamps resolution. But, this one can do a 100 attoamps. Absolutely amazing. 35-year-old bit of technology. For those playing along at home, that is 62.5

**Dave Jones:** electrons per second for 100 attoamps. Woah, this is heavy. So, what do you need something like this for? Well, basic physics and material research, new nanotube research, new polymers, and various other like, you know, real low-current electrochemical type

**Dave Jones:** applications where you're pretty much down to the level of counting electrons. It's ridiculous. Anyway, 100 attoamps resolution. And, please excuse me for turning it on before I take it apart, but I just had to show you that how low this thing could actually go.

**Dave Jones:** And, yeah, we can This is the actual I haven't got I've got nothing plugged into it at the moment. And, we can actually do Well, there we go. I had it on zero there, but there we go. It's

**Dave Jones:** actually counting. If you fart on the other side of the room, this thing's going to change by like 100 counts. So, I'm clenching my butt cheeks. Just I better not breathe, either. Woah. Anyway, look, we can zero check that,

**Dave Jones:** and it's got an internal minus internal one femtoamp offset there, and we can zero we can zero correct that before we take our measurement. Unbelievable. Now, it's actually got a voltage source output as well, voltage generator, 103 volts

**Dave Jones:** maximum. Very nice for powering stuff under test. It allows a higher resistance mode as well using the building voltage source and also it's got some monitor outputs as well. So you can actually will have a closer look at

**Dave Jones:** the schematic up there but it's got the obligatory IEEE 488 GPIB interface and it's also got outputs which tell you that the the completion of the measurement has done and external trigger as well. So you can trigger it and then it gives you a

**Dave Jones:** response when it's taken that measurement. So good for system integration. So you can see that you can actually get a preamp output here and also an amplified analog output as well and that might be handy for once again

**Dave Jones:** system integration stuff. Now of course you can't just use a regular BNC or banana jack inputs for this sort of thing. You've got to use a special low noise triaxial connector it's called. It's called triaxial because it looks

**Dave Jones:** like a regular BNC which is basically a bi-axial and this is actually got a third contact in there that gold one around there if you can see that closely. So don't just go plugging a regular BNC cable into a

**Dave Jones:** triaxial connector you'll bugger it up. So this actually provides a separate internal shield in there as like different for like internal guard different from the external output here and that's critical for really low noise measurements but you'll also find them

**Dave Jones:** on very high resistance meters as well ones designed once again they're ultra low current but like thousand very high voltage system high resistance meters for example will actually use these triaxial connectors for testing at 1000 volts and you know

**Dave Jones:** it you can pay like $1000 for a test cable that comes with this instrument but considering that one of these modern instruments is like $7,000 for the base model unit and like $15,000 for the uh for the top of the range model, then,

**Dave Jones:** you know, people are used to paying a thousand bucks for a special low noise triaxial cable manufactured by nude virgins. Now, unfortunately, I don't have a triaxial connector here in the lab handily. I can I'll have to order one so that I can you

**Dave Jones:** know, do some better experiments. So, I'll just plug some sharp probes up at Clacker and see if it's bang on. Let's have a look. Here we go. Tongue at the right angle. Oh, look at that. Bang on to the least significant digit. Awesome.

**Dave Jones:** So, I'm not going to go to the effort at the moment to measure all the other ranges that requires specialized setups to do. But, suffice to say that if it's bang on on the 1 milliamp range, odds of

**Dave Jones:** it being good on the other ranges are high. Confidence is high. Confidence is high. I repeat, confidence is high. And check it out, the building voltage generator, it works as well. So, let's set it to 5 volts, shall we?

**Dave Jones:** There you go. It's only a smidgen out, but this can actually go up to, as I said, a hundred odd volts. It actually will have an adjustable velocity thing, so should get there reasonably quick. Ta-da! There it is.

**Dave Jones:** 100.45, not bad at all. So, basic functionality seems to be there. Awesome. And I love gear that has the instructions on the top. Look at that. Beautiful. Why can't they do that these days? Anyway, let's do a tear down of

**Dave Jones:** this puppy and enter the world of atto amps. This is going to be interesting. So, what we're going to see inside here is, I'm guessing, this isn't just going to be running via the coax just across the cable over to the PCB. It's It's to be

**Dave Jones:** going into a nice big shielded block or something like that. There's two screws on the back. The rest of it's of course all going to be regular stuff. There's just going to be some magic on the on the front end. And whoop, yep. We're in

**Dave Jones:** like Flynn. And tada, there it is. There's our magic block. That's where all the magic's going to happen. And look at the external power supply over here. That's hilarious. In fact, oh. That transformer looks like it's bent. That is not

**Dave Jones:** camera angle. That's not my eye going wonky. That transformer is This thing's Can I just bend it back? Jeez. Check out down in the mains import down here. Look at this. It's right near the signal outputs. Look, not a single

**Dave Jones:** toss was given about making it, you know, aesthetically physically separate from the rest of it. But, you know, as long as you got your clearance on the PCB, it's all hunky-dory. So, what they're doing is running the mains

**Dave Jones:** traces down here. There's a little common mode choke there. Running them right down the edge of the board, right past all the active circuitry. Once again, if the clearance is there, okay, but, you know, it's not exactly modern design technique.

**Dave Jones:** And then they've got the the mains real clunking mains power switch on the front there. Not sure what that puppy's doing there. It's not labeled. I'll have to read the manual on that one. Hmm. Anyway, so I've got our mains

**Dave Jones:** input and then our line fuse is next to that. Oh, and the Motorola 6805 fanboys go wild. There it is in a socket. Thank you very much. And then we've got the obligatory SRAM next to that. Well, I

**Dave Jones:** can't read that. What is that? Is that Yeah, 6116. Of course it is. Absolute classic. And then we've just got our basic ROM. So, of course, 65 6805 processor and the TMS9914 up here. This is actually the GPIB

**Dave Jones:** interface chip and you can kind of tell cuz it's plugged into all the micro on the bus and then they all bugger off up here. Got some drivers and then it goes over to the GPIB connector. Sorry, IEEE

**Dave Jones:** 488. So we've got our date code there, 85. There it is. And yeah, it's some of the other chips down there. 85. I'm not going to You know, who cares about all the digital stuff? Not me. I want to see what's inside the can. And

**Dave Jones:** we've got some AC coupling to the chassis, of course, for our system noise reasons. Just a couple on there. Look at the braid they've got in there. By the way, little pro tip, when you're using your solder wick, don't throw away your

**Dave Jones:** used solder wick. Actually, you know, keep them in your offcuts from those. Keep them in your past drawer. They're very useful for really low impedance straps like this one. It probably doesn't need the low impedance. Somebody's put the strap in there, but

**Dave Jones:** yeah, they can they can be useful. Keep them. Oh, no. Some of the glue is starting to uh peel off there. Look at that. That's it. They've got a shield all the way, you know, the entire box is shielded as

**Dave Jones:** you'd expect on an instrument of this class. And it looks like the board in here, it's it's all going to be, you know, through hole stuff just like this. But it looks like they've got it on the one board with the power

**Dave Jones:** supply over here. This is, of course, a dedicated analog power supply for this analog section. The other transformer down here has got its own stuff for all the digital thing. It makes sense to separate those. But yeah, it looks like

**Dave Jones:** they've got it all on the one board and calibrated by 1065. Good on you, 1065. And inspected by 1300. Some of the unsung heroes of Keithley. Wonder where they are now. All right, let's reveal the magic here. Couple of

**Dave Jones:** little trimmer holes up there. You got to trim those at the right right angle. You're not allowed to probe through there unless you've got your tongue at the right angle and you've got a gray beard. SO, LET'S TA-DA!

**Dave Jones:** AH! CHECK IT OUT. OOH, I got some jazzy stuff going on here with this can. We'll take a closer look. But, of course, what you expect to find in one of these things is exactly what we see. Standoffs here. There is

**Dave Jones:** too much leakage on PCBs for this sort of stuff to be going into PCBs. So, we've got ridiculously low leakage relays here. Um we'll have to check those out. Let me see if I can can't even get a brand ET. Um phone home.

**Dave Jones:** Anyway, what you expect? PCBs have too much leakage. They get crap, contaminants, oil, dust, and condensation, all sorts of crap on them. So, you want point-to-point wiring on this sort of stuff. Teflon standoffs. Uh maybe not maybe they're not Teflon cuz Teflon can

**Dave Jones:** actually build up a static charge. Um that can be a trap for young players. Um but, yeah, you can see our input is going directly over here over to the standoff there into these transform into these relays, which are doing the range

**Dave Jones:** switching. And have you ever seen a 250 gigohm not megohm gigohm resistor before? Well, you have now. That's the input impedance of this thing, by the looks of it. Now, on a quick search, I didn't find anything for

**Dave Jones:** these relays here, but I'll have a better look look if I can. I'll include it, but these are going to be ridiculously low leakage hermetically sealed relays. Now, I've actually done a video on uh talking about one of the designs I

**Dave Jones:** did back in the day uh for a company I worked at where it was a once again measuring high resistances um and at high voltages, and we required a relay matrix in like a massive relay matrix, hundreds and hundreds of relays, and all

**Dave Jones:** the problems involved in actually designing one of the those things. It's one of my very old videos from like 7 8 years ago. I'll link it in down below and at the end of this video. Check it out. And whatever that little metal can

**Dave Jones:** there is, it's very important because they didn't want the metal can just flapping around in the breeze, so they had to actually have a strap tying that down to some sort of guard point. It's probably not going to be ground. It's

**Dave Jones:** going to be a guard point. There is a difference between ground and guard point. I might have to do a separate video on that cuz that's kind of an interesting topic in its own right. Now, you might be able to notice down in

**Dave Jones:** there or maybe not. Might be a bit hard, but all the magic of course is happening in our dual FET matched FET pair here. And you can see that one of the leads just in there and a bugger going into the PCB way too

**Dave Jones:** much leakage and whatnot. So, it goes they've bent it out at right angles like that directly to the standoff. So, you can see that the signal path comes in here from the coax and then it goes through the various relays and then goes

**Dave Jones:** to, you know, various input impedances and stuff like that to get the current of course because we're measuring current. We're going to trans put it through a resistor, measure the voltage across it basically. So, we've got the fixed and here's the

**Dave Jones:** fixed 250 gig resistor here. So, that'll be used for the two pico amp range there and that is directly on that node there. So, everything travels above the boards like, you know, Manhattan style, above the boards Manhattan construction technique, which

**Dave Jones:** is a technique of dead bugging components on copper clad board and then just point-to-point wiring. Might include a photo if there is one. And yeah, so it all stays off the PCB and goes directly into our jewel matched fit

**Dave Jones:** there, which of course is going to be a super duper special matched characterized one manufactured by nude virgins with gray beards. See if we can get the part number on that. It's got a 168 and then an 85

**Dave Jones:** 2A on there. Mhm. And T-TG on the front of that and an M. Is that It's not doesn't look like the Motorola job anyway. If I can pull up any data on that part, I doubt it. Like, you know, this could

**Dave Jones:** be a Keithley internal part number. Um you may not know what that uh jewel fit input is. Anyway, if you blow the ass out of that, uh yeah, good luck getting a new one. So, all you young whippersnappers out there are probably

**Dave Jones:** going, "Yeah, what's the big deal? Like, it's got some relays and a jewel fit input and bloody fancy pantsy triaxial connector, but whoop-de-doo." Um well, he go try and design something like this. Go try and design it, test

**Dave Jones:** it, and then get uh you know, a proper controlled uh characteristics in production environment, and you'll find out very quickly how difficult this is to get right. It's not rocket science, it's electron science. And you'll notice that the grounds are going all over the shop.

**Dave Jones:** Not only did did the uh shield here for this uh matched fit uh bugger off to somewhere else over here to some guard uh ground, but well, some guard terminal doesn't have to be ground, but the shielding for

**Dave Jones:** this case up here, which is isolated from well, supposed to be, it's touching there, isn't it? Did that cause an issue? Uh like that eventually touching there cause an issue? It may. It may do. I don't know. Mhm.

**Dave Jones:** Anyway, that like this ground is buggering off somewhere else. The shield for this is buggering off somewhere else. The triaxial I presume that that green wire in there is going into the triaxial shield guard inside there. So, it's buggering off downstairs somewhere,

**Dave Jones:** which we don't know about. And it's getting all this stuff right is not easy. Anyway, I've got ourselves a cat act um hybrid resistor uh network there. So, that's pretty nice. But apart from that, um you know, we've got like

**Dave Jones:** the 250 gig resistors. They're not going to be cheap. I have 100 meg No, 100 I think we've got 100 gig. We've got 100 gig a 250 gig resistor and other There's a 100 meg one in there and various other

**Dave Jones:** uh Yep, there it is. There's your 100 meg one. There you go for the different ranges. They're going down in uh decades, of course, um to give you your different uh ranges. They're the shunt resistors, just like on a micro current,

**Dave Jones:** for example. Except it uses a fancy pantsy FET front end and really high value resistors. It's simply the voltage cross uh the voltage drop across a resistor. But yeah, the real is super duper special. Aha, if we get down in there, haven't

**Dave Jones:** fully removed the board yet, but check out Yeah, the triaxial guard is coming from that point down there, as is the uh shield for the can. So, it looks like as are two different wires buggering off there, buggering off somewhere else on

**Dave Jones:** the board. We've got ourselves a star grounding point there. So, it's all referenced back to that one point. So, they certainly know what they're doing. And here's the circuitry underneath there. So, that's actually all to do with like the uh the 100-V uh

**Dave Jones:** high-voltage uh power supply over here. And take a look at this and notice something interesting. Look at this big strap over here. This big crimp connector This from the 100-V output over here. They've got that going through what looks like, you know, a

**Dave Jones:** massive high-current uh lead. It's not doing that. It's going over to this capacitor here, which then couples into the ground and that ground is on the output which straps into which has an optional strap into the earth ground which then

**Dave Jones:** straps optionally into the output ground over here. And of course whether or not you include that ground guard strap there is all to do with your system implementation and how you do that. So you have to really know what you're

**Dave Jones:** doing when you're playing around you know implementing this sort of stuff and taking serious measurements. Not only in terms of using the instrument but your system setup and all your system grounding and things like that. It's really important. And

**Dave Jones:** looks like those extra system ground wires that star grounding I told you about is going over here. Looks like one of them's going into the main ribbon cable which then goes back up to the main connector at the top the main

**Dave Jones:** analog input board at the top. And thankfully we have full access to the schematics for this thing and all the theory of operation the whole works. I'll link in the manual down below. The regular manual has the all this stuff in

**Dave Jones:** it. It's not just the service manual that you know you used to be able to get. It's all in the main manual. Fantastic. They don't make them like this anymore. Anyway, take a look at the notes that they've got for just

**Dave Jones:** assembling this PCB. Look freon clean the PCB flow and touch up using rosin flux wash immediately after the flow what flow? In freon solder the polystyrene capacitors of polystyrene thumbs up love polystyrene they're super stable super stable capacitors used for you

**Dave Jones:** know high precision circuits like this one. After the freon you got to do that after the freon wash and then remove flux locally with freon and then clean thoroughly with meth methanol after flow and touch up in dashed areas. What?

**Dave Jones:** Components mounted on Teflon, so they are actually Teflon standoffs. That's interesting. So, uh static mustn't be a problem. Keithley know what they're doing. Uh and must not touch PC board or other components because, yeah, they have to be completely isolated. So, there you

**Dave Jones:** go. They're just like assembly steps. That's just great. And we have the schematic for the AD converter as well. No, it's a they've rolled their own analog-to-digital converter. It's a constant frequency charge balance single slope job. And well, you can do It's got

**Dave Jones:** theory of operation in the manual if you want to go into that. But, yeah, they basically uh rolled their own. It's not like they just bought Analog Devices ADC. Nah, bugger that. And of course, this is what everyone

**Dave Jones:** wants to see, the front end. How do they do this? Um how do they get like atto 100 atto amps femto amp uh levels on this thing? Well, let's take a look. The input, as you can see, you can see that the uh guard there, the

**Dave Jones:** three inputs. And the guard, as I said, goes down to uh mates down to the motherboard. So, it's all goes around in, you know, various configurations for that star ground and all that. And you can actually see that there are

**Dave Jones:** different symbols used for the different grounds here. And look over on the right-hand side near K301, uh over there that relay, you can see that that's actually a star ground point. And that might go back to the main board that we actually uh saw back

**Dave Jones:** down the bottom, that star ground point down on the bottom PCB. So, as we've seen in the teardown, it doesn't go to the PCB at this point. It's all uh off-the-board construction that in input signal goes to those those

**Dave Jones:** rows of uh standoffs and those relays that we actually uh saw there with the, you know, it's just up in free air. So, it's not touching the board, so it's completely isolated, air-gapped isolated from everything. Goes into those special

**Dave Jones:** squirrel relays, which I still can't find uh any data on those, but they they'd be ridiculously low leakage. And you can see that, um, ah, if you go through R334355 and 332 there, um, then you can see the

**Dave Jones:** 250 gigohm resistor permanently going down to ground. So, that's like 250 gigohms is that permanent input resistance there. And then the other ones up the top there, right at the very top, there's the 100 gig uh, 330 there.

**Dave Jones:** And then 331 100 meg, then they'll go down in decades. 100 K and so forth for the uh, various ranges. Now, of course, this isn't uh, those don't go down to ground. They're part of the feedback loop. Uh, part of the feedback

**Dave Jones:** amplifier. And of course, if you look at the theory of operation, this is actually a feedback amplifier. So, the uh, the shunt resistor in quote marks, the uh, resistor that the current needs to flow through to convert it to

**Dave Jones:** voltage, is in the feedback loop of the op amp. And the op amp here, you can see it there, U309, a Linear Technology LT101, too. And that's a pretty schmick op amp, but it's only picoamp level input, right? So, it's not good enough

**Dave Jones:** picoamps. Ugh. That's, you know, that's amateur hour. So, they use Q308, the dual matched JFET input, as the uh, high impedance input required to get the attoamp level. So, this is a very special matched uh, transistor, hand probably hand selected,

**Dave Jones:** hand tested, uh, hand graded, everything else. And I looked in the uh, manual, the parts list for it, and they don't actually give a part number. So, you know, it's super special secret squirrel uh, stuff, presumably. If anyone does

**Dave Jones:** know, um, please tell us down below. Anyway, that is what gives you your extremely ridiculously high input impedance. The only thing that can do the job here is JFETs. Not this MOSFET rubbish, like really special matched uh, JFETs there for the front end. but apart

**Dave Jones:** from that, um, that's where all the magic happens and physically as well where the magic happens. It's all off the board, choosing these components like the matched JFET, like the relays, mounting them off the board, but everything else is just pretty much off

**Dave Jones:** the shelf. The LT1012 and U304 up the top there, whatever that is. They got a volt 6.3 volt voltage reference Zener and you know, like the rest of it's pretty ordinary stuff, really. So, um yeah, all the special stuff, transistor,

**Dave Jones:** relay, Manhattan construction. That's the ticket, laddie. So, there you have it. I hope you enjoyed that interesting look inside the Keithley 617 electrometer. And these things, they're still available for all sorts of physics and materials research and all

**Dave Jones:** sorts of weird and wonderful stuff. Don't have much use in regular electronics, of course. They might be used in semiconductor, you know, fabs and other places for various things, but you know, your your general purpose electronic lab is not going to

**Dave Jones:** need to go down to attoamps like this thing can or even femtoamps, really. So, you know, you might go picoamps, you know, nanoamps is quite common for low power stuff, but you know, even picoamps is like usually several orders of

**Dave Jones:** magnitude beyond what your regular electronics person ever needs to deal with, but these things are very specialized bits of kit. They have their place. That's why they're so expensive, you know, having the matched FET front end and all the special relays and

**Dave Jones:** everything else, you know, and they don't manufacture these in high volume, which is why that they can charge, you know, 7, 8, 10, 15 thousand dollars for these sorts of things. They are precision bits of kit. Lots of engineering goes into

**Dave Jones:** them, but you might look at it and go, oh, you know, meh, whatever, but there's that Try and do it. I dare you. Try and measure, you know, hundreds of gigohms, teraohms, and femtoamps and attoamps. It's just crazy different world. Anyway,

**Dave Jones:** if you liked it, please be give it a big thumbs up. As always, our high-res teardown photos on evblog.com linked in down below. If you want to discuss it, comments, all that sort of stuff, link to the EVblog forum.

**Dave Jones:** Hope you liked it. Catch you next time.
