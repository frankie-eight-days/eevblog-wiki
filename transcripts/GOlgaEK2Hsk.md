---
video_id: GOlgaEK2Hsk
title: EEVblog #932 - How Does A HV Differential Probe Work?
url: https://www.youtube.com/watch?v=GOlgaEK2Hsk
source: youtube-asr
timestamps: {"0": 1, "1": 12, "2": 36, "3": 45, "4": 55, "5": 68, "6": 77, "7": 87, "8": 100, "9": 119, "10": 136, "11": 152, "12": 175, "13": 188, "14": 199, "15": 214, "16": 233, "17": 249, "18": 259, "19": 269, "20": 285, "21": 304, "22": 320, "23": 332, "24": 341, "25": 353, "26": 369, "27": 382, "28": 390, "29": 403, "30": 419, "31": 438, "32": 447, "33": 464, "34": 484, "35": 501, "36": 511, "37": 526, "38": 535, "39": 549, "40": 560, "41": 583, "42": 598, "43": 610, "44": 625, "45": 640, "46": 657, "47": 667, "48": 681, "49": 698, "50": 711, "51": 728, "52": 738, "53": 746, "54": 772, "55": 784, "56": 797, "57": 809, "58": 830, "59": 841, "60": 853, "61": 866, "62": 878, "63": 889, "64": 907, "65": 917, "66": 931, "67": 943, "68": 952, "69": 973, "70": 990, "71": 1001, "72": 1010, "73": 1028, "74": 1038, "75": 1055, "76": 1073, "77": 1083, "78": 1094, "79": 1110, "80": 1122, "81": 1138, "82": 1161, "83": 1177, "84": 1185, "85": 1201, "86": 1215, "87": 1228, "88": 1245, "89": 1260, "90": 1272, "91": 1287, "92": 1298, "93": 1309, "94": 1319, "95": 1337, "96": 1351, "97": 1361, "98": 1378, "99": 1390, "100": 1401, "101": 1411, "102": 1426, "103": 1434, "104": 1459}
---

**Dave Jones:** Hi, let's take a look at the high voltage differential probe. In this case the Lecroy AP031. Now, I don't believe this is actually designed by Lecroy. They just rebadge it from someone else.

**Dave Jones:** I actually forget who the original manufacturer is of this thing. And these are an essential tool for safe operation of your oscilloscope measuring high volt not only high voltage stuff, but measuring high common mode voltages, things like mains power supplies and things like that, which you can't do really safely with your regular oscilloscope probe.

**Dave Jones:** And I've done a whole video on that. So, click here if you haven't seen it how not to blow up your oscilloscope. So, it's a vital thing to understand that.

**Dave Jones:** But one of the ways, of course, how not to blow up your oscilloscope when measuring stuff is to use one of these high voltage differential probes. It allows you to measure your circuit.

**Dave Jones:** Just hook this onto basically any part of almost any circuit within reason. Being a high voltage mains power supply or whatever other high voltage systems, three-phase stuff. Doesn't matter what it is.

**Dave Jones:** You can hook these two probes up to any part of your circuit. By the way, I've just I've lost my black one. Hit black probe hook here. It's around here somewhere.

**Dave Jones:** Anyway, you can hook these up to any part of your circuit and you will be completely safe. And then you just plug the other end, the output. So, this is the input and you just plug the output into your oscilloscope.

**Dave Jones:** So, it converts the differential signal on here, hence the differential probe, and converts it to a single-ended signal which goes into your oscilloscope. Now, these generally don't have a particularly high bandwidth.

**Dave Jones:** I think this one's about 20 or 30 MHz or something like that. So, it's, you know, not designed for really high-speed stuff. But that's not the point. The point is this that it has not only a 10:1 range, I eat like a times 10 of your regular times 10 probe, it divides your input voltage by 10 that you're familiar with on your oscilloscope.

**Dave Jones:** It's also got times 100 as well or divide by 100. So, they correspond to a range of plus minus 70 volts on the one tenth range and the 1/100 range has plus minus 700 volts and it's got a common mode voltage of plus minus 700 volts.

**Dave Jones:** So, a brief recap on what common mode voltage actually means here. Now, this differential probe, it's just a differential amplifier. Just like say an op-amp is a differential amplifier, but it an op-amp of course has an a ridiculously high gain.

**Dave Jones:** This one has a relatively small gain of either times 10 or times 100 to compensate for the input attenuation here. So, we can put up to 1,000 volts RMS across here and well, that's no problem, but what we we're really concerned about is this common mode voltage and this is where you can come a cropper and I've done that video how to not to blow up your oscilloscope.

**Dave Jones:** What that common mode voltage means is it's then referenced to the output here. The ground of the output, the common of the output here is connected to your oscilloscope and that's then connected through to mains earth.

**Dave Jones:** I did that as a circuit ground, maybe that should be a mains earth ground, but then it's the difference in voltage between your mains earth here and either of your input voltages.

**Dave Jones:** So, I've drawn that as a voltage source there between any of those inputs and in the case of a high voltage differential probe like this, that can be up to plus minus 700 volts between the output here.

**Dave Jones:** I've drawn an extra terminal there, I probably shouldn't have drawn that, and the output and either of the input terminals. And that's important when you're measuring say a mains power supply or something like that and it is very high relative to the earth on your oscilloscope.

**Dave Jones:** Now, there's a common misconception about these high voltage differential probes. Some people think that they are isolated probes, i.e. they have like a transformer in there to isolate the input from the output like this, and nothing could be further from the truth.

**Dave Jones:** And we can prove that. The only thing we need is a multimeter. Let's measure between say the positive input and our output ground here, and I'm not touching it, so it's not my fingers in the way.

**Dave Jones:** Look, 4 meg, okay? And that's a very consistent 4 meg. I mean, we can swap that over, so if there was any like active uh circuitry stuff going on, you'd expect it to change.

**Dave Jones:** But it doesn't. Look, it's exactly the same. So, um we've got 4 meg between either of these inputs here and the output ground. And we can repeat the exact same thing for the negative input terminal and the output ground.

**Dave Jones:** You guessed it, it's that 4 meg again. It's very consistent. It is not isolated. And we can demonstrate that again using our high voltage mega here. So, we can select 500 V cuz we've got a 700 V maximum here, so we don't want to do 1,000 because, well, we could blow the ass out of our high voltage differential probe.

**Dave Jones:** They're not completely infallible, they have ratings for a reason. So, we're connecting between the output ground which goes to our oscilloscope and the input. So, we'll be able to measure that same resistance we got before, but instead of this multimeter only working at, you know, a a couple of volts, uh this thing will actually test it at 500 V.

**Dave Jones:** So, here we go. Let's test that, and bingo, we get the same 4 meg. It is genuinely a resistance. This thing is not isolated. So, how does this thing work if it's not isolated?

**Dave Jones:** Well, those resistance readings might have given you a bit of a clue, but there's only one way to find out. You know what we say here on the EEVblog, don't turn it on, take it apart.

**Dave Jones:** And needless to say, this puppy's going to have a fair bit of uh shielding inside there, so uh we might have to crack that open. In fact, we might have to uh desolder some cans to get to the front end.

**Dave Jones:** Practically all of it is shielded. We've got uh two separate uh sections here, so our outputs from here, so I'm guessing that uh this is the input and this is the output can, and maybe this is just some uh power supply uh stuff up here, just uh keeping that separate.

**Dave Jones:** But, uh look, we've got uh at least a couple of trimmers on there. There's another couple holes, so maybe they've got some trimmer caps down the bottom. These are obviously uh 10-turn pots here for uh frequency compensation and other sorts of trimming.

**Dave Jones:** And I got this uh can off here. It was just very lightly uh soldered onto the sides here, but it looks like this one has a couple of solder points down here.

**Dave Jones:** These are actually These tabs are actually from the can. Thankfully, they're not all soldered. They just uh tacked it down, so hopefully I can and uh probably another couple of points over here, but anyway, we can start to see the structure of this thing.

**Dave Jones:** Note our high voltage isolation slots here and here, here and here like this. So, here's our input. There's obviously two uh separate sides to this. This is be like a symmetrical cuz it's a differential uh type probe, but I wonder what we're going to find under here.

**Dave Jones:** You might be able to start guessing. And we're in like Flynn. We've got ourselves a high voltage uh isolation shield here just so that uh nothing arcs or uh shorts over to the metal can, of course, and that's important cuz we've got a lot of through-hole components here, vertical.

**Dave Jones:** Check it out. It's all a bit It's all a bit how you doing, but uh look, numbers rubbed off the chips. Mongrels, they don't want us to know what these are.

**Dave Jones:** They're probably, you know, they're they're just op-amps, right? They're just sort of, you know, not jelly bean op-amps, but they're not going to be anything hugely special. Now, take a look Look what what we've got here, straddled across the isolation slot going right down here.

**Dave Jones:** These are all of our high voltage input components. So, you can see we've got ourselves some ceramic caps here. These will be for frequency compensation, as we'll see. And they've actually heat shrunk those, maybe to provide it's not maybe some insulation, but they're just around them like that.

**Dave Jones:** So, maybe some explosion protection or something like that. Like they do in MOVs for uh you know, input MOVs on multimeters and stuff like that. Um that might be my guess, but like you know, there's some resistors in here that are bent over.

**Dave Jones:** So, they're obviously maybe trying to isolate the leads on there, but then that's all exposed. And well, anyway, we've got some resistors here. It looks messy, but let me try and buzz it out.

**Dave Jones:** Now, you'll actually notice that it's virtually completely symmetrical, and that's what you'd expect from a uh differential front end like this. So, we got Oh, no. I thought we had a component missing in there.

**Dave Jones:** Nope. But, let me buzz all this out and I'll get you a Dave CAD drawing. And this is designed and or laid out by Mr. Woo. Good on you, Mr.

**Dave Jones:** Woo. Uh and it's Sapphire. Yes, I believe that's the original equipment uh manufacturer. They're the original designers of this thing, and it's re-badged under many different names. So, if I take off that heat shrink, you can start to see some of the structure here.

**Dave Jones:** Here's our input uh wire, our negative, our positive uh side of this circuit's going to be absolutely identical, of course. And that's in series with another resistor just end on end.

**Dave Jones:** I love how they've even got the uh silkscreen symbol down in there for two end-to-end resistors like that. That's kind of neat. So, there's two 1 mega resistors in series, and then that goes down to another 1 mega resistor, which then goes over the high voltage isolation uh slot there and bingo into another 100 mega resistor down into there.

**Dave Jones:** One meg, two meg, three meg, four meg. Does that ring a bell? And they've just got some 6.8 puff caps there. They're all 6.8. Yep. But they're 1 kilovolt jobs, so they're high voltage ceramic caps of course.

**Dave Jones:** And these don't connect anywhere on the underside. So if we go on the underside there, you can see that the capacitors don't actually connect. So it's not like you've got one capacitor across each resistor there.

**Dave Jones:** So it looks like we've got two Well, actually one, two, three series caps across the entire string of those four one meg resistors. And of course they could have used one big high voltage capacitor across there.

**Dave Jones:** But hey, it's not easy to get greater than a 1 kilovolt capacitor. So they used just used three one kilovolt ones in series, which gives you your voltage. Likewise with the resistor, they could have used just one big ass four meg resistor on the input there.

**Dave Jones:** But hey, you wouldn't have got the high voltage isolation. When you string components in series like this, the voltage ratings of each resistor and each capacitor add up. So that is effectively 6.8 divided by three.

**Dave Jones:** It gives you your capacitance and then the voltage rating is 3 kilovolts total. And I do like how they added this little metal shield here over this front end where the cables come in.

**Dave Jones:** That just seals up the gap in the can there for the cable entry. Someone was thinking. Mr. Woo was thinking. Good on you, Mr. Woo. And you don't want the crap leaking out of your switching converter.

**Dave Jones:** That's why there's two inductors there and there, L1 and L2. After putting a bit of spin on that chip, it turns out someone at the Taiwanese factory is not very good at scrubbing off those numbers.

**Dave Jones:** So in true EEVblog style, we'll just speculate on what's going on here. Let's give it a go anyway. I won't I don't plan on really doing a full reverse engineering to this thing cuz it's a bit of a pain in the butt and I'm feeling a bit lazy today anyway.

**Dave Jones:** So I just want to show you that it wasn't an isolated probe basically and it was using input dropper resistors, high value dropper resistors to limit the current and provide that attenuation ratio on the front end.

**Dave Jones:** So anyway, we've got our positive and negative input here. We've got our four meg of resistance here, four meg worth of resistance here. We've got some compensation caps around here and around here.

**Dave Jones:** Then the two resistors in there are going to be the lower end of the divider. So we've got a four meg input divider and then it's going to go over to these two resistors here.

**Dave Jones:** Why they've got three caps? They actually look to be They're all in parallel. So I don't know why they've got so many in parallel. Anyway, we'll have a look at those values maybe to compensate for each frequency range, which is a common technique for like bypassing for example cuz they'll have a different impedance characteristic based on their value and their package size and everything else.

**Dave Jones:** But they're all identical ceramic capacitors. So that's a bit unusual having three in parallel. Anyway, four meg input resistor, whatever value that is down in there. Haven't looked at it so that'll give a fixed division ratio on both the positive and negative input.

**Dave Jones:** This 10 turn trimmer here, that's probably just used for an offset adjustment thing. And then we've got some trimmer caps in there just to trim these two values in there.

**Dave Jones:** And you probably saw the holes in the metal case, wherever that is. Think it's over on the other bench. But yeah, you can get to these after the fact after you've soldered it in the metal can to uh trim those.

**Dave Jones:** And then, it looks like you've got the output of this going over to here, another output going over here. That's going into this metal can package here. Haven't actually looked at that one yet, but based on the number of pins there and a common technique used in scope front ends, which I'm sure we've seen before uh when I've done scope tear downs and things like that, that's

**Dave Jones:** probably going to be a matched uh JFET pair. Very common to use a JFET uh differential uh you know, roll your own JFET input amp. So, I reckon that's what's going on there.

**Dave Jones:** That's uh probably a quad op-amp. And um this IC up here, what would that be? Okay, here's our output. It's probably coming Yeah, it looks like it's coming from there.

**Dave Jones:** So, yeah, yeah, it's coming Yeah, there's the output coming over there. So, yep, that's got to be our um output driver. So, that's converting the differential output. Um well, I'm not sure.

**Dave Jones:** Anyway, not sure of the arrangement of the op-amp there. That's I don't know. Anyway, um I reckon that's it's differential all the way probably through to there and then um differential to single-ended uh cable driver.

**Dave Jones:** So, that's just like a high-spec um you know, high slew rate uh low noise op-amp or something like that um to drive the output. And uh Bob's your uncle.

**Dave Jones:** We've got another couple of in here. I don't know what they'd be doing, maybe some offset uh stuff, things like that. Um there's another couple of down in there, two two of those back-to-back, but not sure what's maybe with some sort of I don't know, is there some sort of current mirror or something going on there?

**Dave Jones:** I'm not entirely sure. Anyway, um that's going to be the basic arrangement. And I tell you what, I think they've tried to actually scrub the number off that can.

**Dave Jones:** That's kind of what it looks like. The marks don't really show up. Is that a 39? 68, is it? So, let's go to Dave CAD reverse engineering edition. Please excuse the crudity of this model.

**Dave Jones:** I didn't have time to build it to scale or to paint it. This is a very, very rough schematic of what's going on here. In fact, I'm not actually entirely sure what's going on here.

**Dave Jones:** This chip, which I thought at first, oh yeah, that's going to be an op-amp, a quad op-amp. But, I don't actually think it is. Anyway, let's have a look at this thing.

**Dave Jones:** As we've seen, we've got our uh four 1 meg resistors in series and our four 6p8 caps in series for some frequency compensation on that. And they're all they're 1,000-V caps of and they're going into the 25K here and the trimmer, which is just used for an offset balance adjustment there.

**Dave Jones:** So, you know, we've got a pretty good division ratio here. This is why it can survive and measure all the high voltages. It's basically differential input. And then, I believe it's going into a dual matched JFET here cuz this is very typical front ends.

**Dave Jones:** Although, I couldn't really find any info on that part number that I saw down here. It said it was like an N-channel JFET, but it didn't say it was dual or anything else.

**Dave Jones:** So, from some obscure company that's probably not even around anymore. Anyway, um I believe that is a dual JFET input. That makes sense. We've got some diode clamping here for input protection.

**Dave Jones:** By the way, these three caps here, 120 puff, 82 puff, and 82 puff, and then probably a much smaller trimmer cap value here just to trim the frequency compensation on this thing after it's all assembled in the metal cans, everything else is on.

**Dave Jones:** You get in there and hold your tongue at the right angle and tweak these, tweak your balance adjustments, and there's a couple of other pots in here which I haven't uh reverse engineered and uh showin.

**Dave Jones:** So, it's kind of unusual that they've got the three in parallel. Not entirely sure why they're actually doing that. Um they're all the same type of ceramic. So, maybe they're just trying to get a tighter tolerance or something by putting the three in parallel like that.

**Dave Jones:** That's all I can think of so that the trimmer has a better uh more accurate, more controllable adjustment range perhaps. Anyway, going into two JFETs and then um after that, I'm not sure what that puppy there's doing, but it by just looking at the pinout and everything else, it doesn't seem to be an op-amp.

**Dave Jones:** So, what I think it is and because it just didn't make sense in this sort of arrangement here to have an op-amp directly um on the output here. It's not that one.

**Dave Jones:** Forget that for a second. A differential JFET front end like this usually needs some extra transistors here and usually formed a forming a current uh source down here. So, that's a usual arrangement.

**Dave Jones:** So, I think my guess is that that puppy's actually one of those uh transistor array uh chips and I couldn't make heads or tails of the number. The number the partial number that I got off that certainly didn't make sense in terms of a quad uh op-amp part number.

**Dave Jones:** So, I believe that's some form of uh transistor array array. They were uh quite common back in the day. You can still get them in various forms. TI and other uh companies make them and stuff like that um and lots of obscure uh providers back in the day.

**Dave Jones:** Uh matched transistor uh things. The reason that they're good is because they're matched on the same die. If you try and do a discrete front end like this with all separate two separate JFETs and then separate uh bipolar usually bipolar uh transistors, it won't be uh JFETs.

**Dave Jones:** So, these will be BJTs in here. So, a whole like I'm missing a whole section of circuitry there. I mean, this is not just two resistors and a current you know, there's going to be you know, like usually these have like uh four like five or six transistors usually in a current in a differential configuration with the emitters tied together and stuff like that.

**Dave Jones:** Anyway, I reckon that's what that puppy is doing there. So that makes sense and then the output the differential output is then going over to this puppy which has had the number rubbed off so I don't I can't even get a partial on that one.

**Dave Jones:** So that'd be converting the differential into the single ended driver to drive your coax over here and that's about all she wrote. There's a couple of other transistors in there.

**Dave Jones:** I haven't bothered to reverse engineer all that. There's a couple of other trimmer adjustments in here which are probably well don't this one might be output gain for example and this one here might be current source adjustment.

**Dave Jones:** So I reckon that's what's going on there. So if anyone actually has a complete schematic of this thing, I'd really like to see it. Anyway, this wasn't really a 100% reverse engineering video.

**Dave Jones:** It was just to show you what's inside one of these differential probes and then they're not actually isolated. They the reason that they're safe is because they use these resistors in series like this and you're protected.

**Dave Jones:** So if you're holding on to the output and the grounded output like this and you've got hundreds of volts 500 volts floating around in here relative to the ground that you're holding on to you're pretty darn safe because you've got four meg in either lead like this and you've got multiple capacitors in series as well.

**Dave Jones:** You know, like you if you just had the one cap in there you could get a single fire then it might render it a bit unsafe. It could go through the 25k to ground and your output, you know, this is your ground reference output here so that could you know, if you're holding on to that doing whatever then you know, it could be a problem.

**Dave Jones:** But these are very safe probes just by nature of the four one meg resistors in series and the high voltage isolation slots and the rated caps and everything else.

**Dave Jones:** So, Bob's your uncle. It's how it works. It's just a basic JFET differential amplifier with a big attenuator on the front end. And just for kicks, there's inside the DC to DC converter and they rubbed the number off yet again.

**Dave Jones:** Why? Protect a crummy discrete DC to DC converter. Give me a break. And we'll just have a quick squeeze at what rails we've got here. Of course, nothing's marked on here.

**Dave Jones:** There's no voltage rails, no ground points marked. But of course, for ground, you almost always take the ground plane on Well, the plane on there, the main plane, it's almost certainly going to be ground.

**Dave Jones:** And then, as I think I mentioned before, we've got the two inductors there and there. I think this is only going to be giving out There we go, 9 and 1/2 volts.

**Dave Jones:** And the other one should be negative similar. Yep, -9.5. So, there you have it. That's inside the LeCroy AP031 / Sapphire 9001 differential high voltage differential probe. So, I hope you found that interesting just how these things work.

**Dave Jones:** With the front end, I mean, the exact reverse engineering details aren't aren't a huge big deal. But the fact that it uses those two big resistive dividers with a differential FET front end, that's what we wanted to know.

**Dave Jones:** Rather interesting little beast this one is. Ancient. I don't know the date on this one. They've rubbed off all the bloody codes on there. Anyway, this design must date back a long time.

**Dave Jones:** I got this one back when I was still working at Siracell, I think. So, 5 and 1/2 years EEVblog full-time, 4 years at Altium, you know, it's probably a good 10 years ago I got this and it was an old model back then.

**Dave Jones:** It might be a more modern variant these days cuz it is pretty how you doing. It's all through-hole design. I'd be surprised if they haven't done a new modernized version of it or something like that, but it's probably still identical.

**Dave Jones:** But, you probably wouldn't manufacture still manufacture that one today. I would modernize it with some surface mount stuff at least just to you know just to make it neater and tidier and get your production cost down.

**Dave Jones:** But, the design would still be as valid as it was back then. And well, you know, there's some like the fit front end might have gone obsolete or something like that.

**Dave Jones:** The transistor array might have gone obsolete. You might, you know, modernize those or something like that. But, the basic technique and everything else would remain very much similar. And there's other ones on the market as well.

**Dave Jones:** You can get them for like 300 bucks on eBay these days. Not this particular model, but there's another one. Actually, I see I think I can get my hands on one of those.

**Dave Jones:** It'll be interesting to do a a teardown of the cheap $300 eBay one. And see Anyway, hope you enjoyed it. Catch you next time. Hi. I just read a post on the EE Vblog forum where somebody was asking about the oscilloscope probes and how they can be potentially dangerous if you hook this ground lead up to the wrong point in your circuit.

**Dave Jones:** You can blow up your circuit. You can blow up your scope. Bang! And it really is a big trap for young players. And I've mentioned it before, but they wanted to know exactly under what circumstances that could happen.
