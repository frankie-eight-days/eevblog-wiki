---
video_id: crs_QLuUTyQ
title: EEVblog #1176 - 2 Layer vs 4 Layer PCB EMC TESTED!
url: https://www.youtube.com/watch?v=crs_QLuUTyQ
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 29, "3": 37, "4": 51, "5": 65, "6": 76, "7": 109, "8": 123, "9": 138, "10": 155, "11": 166, "12": 179, "13": 205, "14": 224, "15": 240, "16": 249, "17": 259, "18": 277, "19": 293, "20": 305, "21": 317, "22": 330, "23": 346, "24": 360, "25": 376, "26": 390, "27": 405, "28": 425, "29": 433, "30": 452, "31": 469, "32": 491, "33": 500, "34": 509, "35": 532, "36": 545, "37": 562, "38": 573, "39": 585, "40": 601, "41": 616, "42": 634, "43": 645, "44": 660, "45": 683, "46": 696, "47": 713, "48": 734, "49": 752, "50": 767, "51": 782, "52": 793, "53": 804, "54": 813, "55": 825, "56": 837, "57": 850, "58": 862, "59": 879, "60": 903, "61": 916, "62": 924, "63": 953, "64": 971, "65": 991, "66": 1003, "67": 1023, "68": 1044, "69": 1059, "70": 1073, "71": 1086, "72": 1099, "73": 1117, "74": 1142, "75": 1158, "76": 1175, "77": 1185, "78": 1209, "79": 1225, "80": 1242, "81": 1256, "82": 1269, "83": 1282, "84": 1297, "85": 1309, "86": 1321, "87": 1331, "88": 1349, "89": 1361, "90": 1375, "91": 1385, "92": 1408, "93": 1418, "94": 1436, "95": 1450, "96": 1461, "97": 1475, "98": 1499, "99": 1510, "100": 1520, "101": 1545, "102": 1560, "103": 1588, "104": 1604, "105": 1619, "106": 1640, "107": 1651, "108": 1672, "109": 1690, "110": 1705, "111": 1713, "112": 1727, "113": 1752, "114": 1770, "115": 1777, "116": 1787, "117": 1802, "118": 1815, "119": 1836, "120": 1853, "121": 1880, "122": 1899, "123": 1906, "124": 1925, "125": 1937, "126": 1954, "127": 1971, "128": 1982, "129": 1993, "130": 2008, "131": 2030, "132": 2041, "133": 2058, "134": 2070, "135": 2080, "136": 2100, "137": 2111, "138": 2126, "139": 2138, "140": 2151}
---

**Dave Jones:** Hi, in this video we're going to take a look at a two-layer PCB and a four-layer PCB and what difference having four layers makes to EMC/EMI or radiated emissions from the board.

**Dave Jones:** Now, this is the Gigatron TTL computer which you've no doubt seen in previous videos and this is the original from the designers and it's a two-layer PCB. There is no ground plane internally to this.

**Dave Jones:** So, all the signal traces you can see they go horizontal as effectively horizontal on the bottom and more vertical on the top and that's a traditional two-layer PCB layout.

**Dave Jones:** Yes, they've got some ground flood fill in here and stuff like that, but generally it's it's actually quite a nice neat layout. All the chips are in the same direction and it's quite a neat traditional two-layer layout.

**Dave Jones:** But, the problem with a two-layer PCB is that well, as we'll get into the finer details later, but it radiates like buggery. So, I took this exact layout and I've done a video on this.

**Dave Jones:** I'll link to it down below and at the end if you haven't seen it where I took exactly the same layout and actually produce a four-layer PCB. It's an absolutely identical layout.

**Dave Jones:** I have changed none of the traces whatsoever. It's completely identical. The only difference is you can see in there that I've actually got a huge internal ground plane. So, ground and 5 volts internally for there all the bypass capacitors, everything else is absolutely identical and what difference is this going to make to radiated emissions which is important if you're designing a product commercial product for sale, you have to meet various

**Dave Jones:** electromagnetic conformity requirements and that varies in different countries. We won't go into that in this video. So, you can see our computer's operational here. It's got a 6 MHz main clock, which is not particularly fast, but remember, it's not the fundamental clock rate.

**Dave Jones:** It's In fact, you can have a 1 Hz clock on this, and it can still radiate like buggery because it's the edge rate of the signal. It's not just the fundamental frequency.

**Dave Jones:** So, we can actually use one of these H-field magnetic probes to measure the near-field emissions it's called, and I might go into a bit of that later. But, we can measure the emissions from this board, and we can put it under here, and we can see the difference between the two-layer board and the four-layer board.

**Dave Jones:** This is going to be neat. Now, what we're going to concern ourselves with in this video is, as I said, this is a near-field magnetic probe. It's called a H-field probe.

**Dave Jones:** There's also a voltage probe, which looks quite similar, but it actually operates quite differently, and I might have to do a separate video on like the differences between these two.

**Dave Jones:** But, this basically measures the radiated magnetic field from the PCB traces and the loop areas, as we'll talk about. And I've got my jig of repeatability here, which just means that the probe will be in exactly the same position, and then I can move the board over various points, and I can look straight down through there to actually center things, and we can get a direct comparison and then

**Dave Jones:** overlay various signals on both boards between the four-layer and the two-layer. How much difference do you think it's going to make? So, we're dealing with the radiated emissions that actually come out of the board rather than conducted emissions, which come out through cables and including the braid and the shield of this.

**Dave Jones:** This will be conducted mode radiation radiated emissions. The USB over here, I've got this powered by from an external battery pack by the way. So to do these measurements, we'll just remove any cables from there and we can get a direct comparison.

**Dave Jones:** So what I'm going to do is use my largest H field probe here, largest diameter because that's the most sensitive. You can get smaller ones but there's no point.

**Dave Jones:** The smaller ones are really useful when you're checking out differences between like individual traces and you know, stuff like that and I've got that going into my preamp over here.

**Dave Jones:** That's a 20 dB gain preamp 3 meg to 3 gig and we'll use our Rigol DSA815 spectrum analyzer here. We're using the EMI the electromagnetic interference filter type which gives us a industry standard 120 kilohertz resolution bandwidth filter here.

**Dave Jones:** You don't necessarily need that but if you're going to sort of get ball park pre-compliance measurements that you know, try and match what you might get in the field then you know, 120 kilohertz and our frequency span here.

**Dave Jones:** We'll just go to 100 megahertz at the moment. I can show you a wider span. It just allows us to look at some nice detail in here and our amplitude we've got units in dB microvolts.

**Dave Jones:** That's just a bit easier than dB millivolts. Doesn't really matter and we've just got a input attenuation of fixed 10 dB here because depending on where we put it, put it right over chip, we can actually see it saturate.

**Dave Jones:** I can probably show you that now. There we go. Out of range it just starts saturates. Oops. And we've got the input preamp on as well. And we're going to put it directly over the 6 megahertz crystal here and this is the response we get.

**Dave Jones:** If you have a look at this first peak here, bingo, that's our 6 megahertz fundamental and if we skip through 12, 18 and they're all the harmonics and that will extend all the way with LBJ.

**Dave Jones:** It'll actually keep going. If I actually change the span, let's go to 500 MHz there. Boom. Look at that. It extends all the way right up. We can go to like 1 gig or something like that, but it it starts to drastically drop off there.

**Dave Jones:** But, you can see that it really extends all the way up because of that edge rate. Okay, so what I've done is I've frozen that yellow reference there, and let me take it away, and let's plug in our four-layer board.

**Dave Jones:** And right under the crystal, it's exactly the same. Look at the difference here. Yes, you still get all the peaks, but very significantly reduced broadband noise here. We're five dB microvolts per division here.

**Dave Jones:** So, we're talking about, you know, a good 5, 10, 15 dB difference in sort of like the bulk noise here, and the peaks they're similarly like the five or 10 dB down from that.

**Dave Jones:** So, you know, it's a huge reduction there, and you wouldn't have thought so. You thought, "Aha, it's all just coming from the crystal. It's exactly the same crystal in exactly the same location." No, it's the radiated emissions, in this case the near-field radiated emissions coming from the traces and everything else on the board.

**Dave Jones:** But, because we got the ground plane in there, it's actually it lowers the loop area and does. We'll talk about this towards the end of the video, so stick around for that.

**Dave Jones:** Um and it just lowers the radiated emissions. It It makes a drastic difference. 15 dB is absolutely enormous. That could be the difference between passing and failing your compliance, and you know, it costing you, you know, five grand or 10 grand or something like that, and you got to respin your product.

**Dave Jones:** You could easily spend tens of thousands of dollars because you you failed your compliance. So, you know, and then you go, "Oh, well, should have used a four-layer board to begin with." You'll see that probe is actually quite a substantial distance above that board, too, but those are those radiated emissions, they're a killer.

**Dave Jones:** Let's just try another random spot here, straight over the addressing mode decoder chip here. This is the four-layer board. And that's our spectrum there. You can see it was it's much lower than we got before, and you can still see the fundamental and the harmonic spikes still in there, but it's going to be pick up a whole bunch of broadband noise, cuz this is a digital computer

**Dave Jones:** that's, you know, refreshing the screen, it's doing all sorts of processing in the background. Everything's going all over the place, and it's just, you know, generating a whole bunch of wideband noise.

**Dave Jones:** Oh, by the way, if you want to see what happens when we disconnect the power, it of course completely vanishes. Now, let's try the two-layer board. And this is the two-layer board.

**Dave Jones:** So, four-layer board in the yellow there, and you can see that actually the four-layer board actually has more prominent peaks in there because all the rest of it's being kept more down in the noise by the ground plane, whereas the two-layer board has once again, you know, a good 5 10 15 dB difference in the like the average broadband noise level there.

**Dave Jones:** And of course the peaks are once again 10 15 dB above the peaks on the four-layer board as well. That's a huge difference. And let's try right on top of the ROM here, just for just for kicks.

**Dave Jones:** So, that's our two-layer board. And there's our four-layer board. Much, much lower. Just over the accumulator chip there. That's our four-layer board. And there's our two-layer board. So, once again, you can see the broadband difference.

**Dave Jones:** It's it's quite remarkable. This is our accumulator chip again over a 250 MHz span this time. This is on the two-layer board. And you'll see what happens if we physically take the board away.

**Dave Jones:** I've got the board like a good like foot away from it now. And but you can still see some of the radiated emissions there even though it's not in the correct plane, which we'll talk about in a minute.

**Dave Jones:** There you go. There's our four-layer board. Once again, I've changed the scale here to 10 dB per division now. And once again, it's a 15 dB difference. It sort of gets a little bit closer up here, you know, around the like a 200 150 200 MHz uh range, but still significantly under.

**Dave Jones:** That could make or break your uh compliance, for sure. And the thing with these H field magnetic probes, and it's not like an issue with them, in fact, it's a feature, is that uh they are dependent upon the orientation.

**Dave Jones:** They work in the plane. So, if you've got your coil like this, it's picking up magnetic fields that are in that flat plane there. So, you'll notice that if we take this, there's our spectrum, and that that's over 250 MHz, and if we simply rotate that like that, it picks up different components.

**Dave Jones:** Look at that. So, you can actually use that as a feature. Using a uh smaller diameter one, you can get down there, and you can trace down uh your offending uh components and traces better.

**Dave Jones:** Um things like that. So, I I probably have to do a a whole separate video on this, but uh yeah, it does make a difference, the orientation. We've seen quite a significant difference here between the four-layer and the two-layer board.

**Dave Jones:** Makes a heck of a difference. Like typically like broadband noise in this particular case, about, you know, 15 uh dB or so, and that's a lot. But does that translate, if you measure say a 15 dB difference here, does it actually with your near field probes, does that actually translate to a 15 dB difference on your uh EMC testing when you put it through the test house and you test it

**Dave Jones:** against the compliance standard? Well, the answer is unfortunately not. Um these near field probes, both the H field um magnetic field and the electric E field All this is, as I said, the near field.

**Dave Jones:** Whereas, all of the compliance testing is done in the far field, and I'll explain that in a minute because I have a Dave Cad. So, what's the point of using these near field probes if they're not sort of like quantitatively equivalent to what they do in the test house?

**Dave Jones:** Well, the good thing about it is that at the design stage or maybe if you fail compliance or something or you need to or you're doing some pre-compliance testing, you can go around your board and sniff all around your board with the H-field and the E-field probe to see if there's any issues, see if there you know, anything's radiating wildly and stuff like that.

**Dave Jones:** You can you might be able to see a big spike or something at one particular frequency. You might go, "Oh, we need to knock that down." Even though you don't even though it might be compliant, at the design stage you might go, "Well, you know, I'm not going to take any chances and I'm going to knock that problem on the head now before I send it across to the test house.

**Dave Jones:** So, we'll briefly talk about near field and far field here and how it relates to the electromagnetic radiation. Now, a you might have heard the term electromagnetic radiation. It's electro and magnetic.

**Dave Jones:** Contains electric and magnetic components and you can look at it. This is like the standard visual representation of it. The electrical field might like would go up in the z-axis like this and the H-field is 90° from that.

**Dave Jones:** So, they actually propagate in different orientations. And of course, this is the wavelength. And here's a cute little animation just to show you how that works as it propagates down.

**Dave Jones:** Now, what we actually have to look at though is what's called the wave impedance. And this is where the difference between near field is everything on this side and far field is everything on this side.

**Dave Jones:** Now, the wave impedance in ohms like this in the for this particular scale, please excuse the crud, didn't have time to build the scale, lot of pain it. From 10 ohms to 10,000 here.

**Dave Jones:** So, this is where you have to define far field and near field. Well, the electric field and the magnetic or H field, there is a difference between H and B, by the way.

**Dave Jones:** B is flux density. You might sometimes be hear it called B, but it's actually H magnetic field, as opposed to induced magnetic field, as opposed to magnetic flux density.

**Dave Jones:** Anyway, won't go into the details. So, the H or magnetic field actually has a very low impedance source in the near field, whereas the electric or E field has a very high impedance.

**Dave Jones:** I'll clarify that in a minute. But, basically it all comes down to the wavelength lambda here, and this is normalized to one here, and it's lambda on 2 pi, which is basically where we're going to normalize to that value.

**Dave Jones:** And, of course, let's take, for example, 100 MHz is a wavelength of 3 m. So, pi on 2, that's about a half meter. So, when you get to a half meter away from your product, this is where the electric fields and the magnetic field actually start to converge.

**Dave Jones:** It's not really clean, like this. There's a bit of, you know, overlap in here, and this is like the transition. There's going to be like a transition region in here, where the two fields eventually combine, and anything over roughly half a meter away at 100 MHz, the electric and magnetic fields combine to give you a singular impedance, which actually happens to be 377 ohms in free air.

**Dave Jones:** So, anything over the wavelength on 2 pi is deemed to be the far field, and anything closer, physically closer than that, like we just did with our probes here, is the near field.

**Dave Jones:** Now, this is why we have two different types of probes. One is the H field probe, the magnetic probe, the other is the E field or electric field probe.

**Dave Jones:** And the magnetic or H field is going to be generated by higher currents, i.e. uh sources that have a very a lower impedance. So, for example, if you've got a lot of current flowing in a in a particular uh trace, either due to an actual like heavy current switching or even very fast switching that's dumping a lot of energy into the bypass capacitors and the capacitance between the power planes and

**Dave Jones:** everything else, then that's generating typically be generating a magnetic field due to the low impedance and the high current. But very high impedance things that uh don't generate lots of current, then they generate electric fields and uh hence the bigger source impedance.

**Dave Jones:** So, you can generate electric fields from say uh just like a static power supply, for example, your 5-V power supply. Whereas all your switching stuff will dominate down in the H field here because there's lots of uh current being dumped into the trace uh or the load capacitance or the particular load itself when you're switching things.

**Dave Jones:** So, that's why you need to use these two different probes. And the magnetic field probes, they are sensitive to orientation like this and like that as well as I talked about on the plane.

**Dave Jones:** Whereas the electric field is not sensitive. You can just put that in any orientation, and it's not going to make a difference. So, if I use my E field probe like this, and let's say I probe this power trace over here like this, you can see it's really not going to make any difference the orientation that I put that in.

**Dave Jones:** It's just completely insensitive to that because there's no magnetic field coupling. It's electric field coupling, and it's just purely the distance. But if you take a magnetic loop probe like this, and I just change the orientation like that, wow, that makes a big difference.

**Dave Jones:** It really brings out the peaks if I put it vertically like that. If I put it horizontal, it gets more of the current flowing through the trace. And if we use our smallest H-field probe, let's just have a look at let's say this like blank area over here.

**Dave Jones:** This is our four-layer board like this, or maybe right over on the edge of the corner of the board right over here like this, and let's compare that with our two-layer board here.

**Dave Jones:** Bingo, look at that. Because we've actually got a power trace actually running right around this corner as well, which we actually physically removed. And you can actually see that the power trace actually running all the way around there like that.

**Dave Jones:** So, that's just going to radiate like buggery. But even if we go over just the ground plane there, you can see it's much, much higher than we get with the four-layer board.

**Dave Jones:** And this is why at the EMC test house, they'll test in the far field here because it binds the electric and magnetic fields together. And basically the typical testing distances would be like 1 m, 3 m, 5 m, 10 m, for example, away.

**Dave Jones:** It depends on the type of product they're testing and to which standard they're actually testing to. But say if you put it 10 m away, then you can have a larger rotating turntable so that your product rotates around like this on the turntable and they can measure all the axes like this when they while they have their super expensive, you know, biconical super calibrated measurement antenna 10

**Dave Jones:** m away measuring over say 30 MHz to 10 GHz far field, for example, might be a typical uh, range. And then there'll be a standard like uh, envelopes that you have to get under and also peaks and things like that.

**Dave Jones:** And it gets, you know, the standard gets uh, quite complicated, but uh, yeah, just the uh, near field uh, testing that we do here doesn't really translate to the far field, but you can certainly uh, get an indication of whether or not you've got any nasties on your board.

**Dave Jones:** So, why does this happen? Why does a four-layer board make a huge difference compared to a two-layer board when it's an identical layout? All the traces are exactly the same length, all the chips are in the same location.

**Dave Jones:** It's got just the same number of bypass capacitors. Everything's hunky-dory. They should be identical, right? Well, it all comes down to loop area, which you've heard me talk about in many videos before, and a huge general rule of thumb when you're laying out boards is not only to keep your traces as short as possible, but to keep the what's called the loop area as small and tight as possible.

**Dave Jones:** So, the tighter your layout and the tighter your loop area, the less problems you're going to have with EMI in generation and EMI and susceptibility to electromagnetic interference as well.

**Dave Jones:** So, you have a source and you have a destination on your PCB, a trace going from one side from the source to the load. Now, the loop area is actually the total area that includes the ground for that entire loop, but it also includes the power system with the bypass capacitors.

**Dave Jones:** And I've done a whole video on that actually showing the return path for currents and why you need bypass capacitors. I'll link that one in. It's really fascinating. So, that it has to do with the entire loop area and the bypassing.

**Dave Jones:** And on a two-layer board like this one here, the original one, you just don't have the luxury of having or often don't have the luxury of having a very tight loop area for all of your signals.

**Dave Jones:** You might, by either accident or good design, have them for certain traces, but when you've got, you know, what, two dozen chips spread over on this on a large board like this, you just can't possibly have every one of the traces having a short loop area.

**Dave Jones:** So, something's going to radiate somewhere. In fact, probably the majority of them are just have large loop areas and hence are generating a larger magnetic field in this case, um, a bit electric field as well.

**Dave Jones:** Electromagnetic field, we'll say, generating a larger electromagnetic field and hence why we see the huge increase in radiated emissions. So, this is the original two-layer board. And what we'll go in here is we'll go in and just inspect a single signal.

**Dave Jones:** Let's say the address zero pin to the RAM chip. That's it, cuz it's only got, uh, two connections on there. Now, we can actually go in in there and have a look at this.

**Dave Jones:** This is the RAM chip and this is the driving, uh, chip here for that address, uh, decoder. Now, look, it's got a nice short trace there. Look at that.

**Dave Jones:** That's really neat, isn't it? And in this particular case, the ground of the, uh, driver chip is here and the ground of the RAM is over here. Now, this is actually a reasonably short, uh, path for a, look, it has to snake, it's got to go all the way around here.

**Dave Jones:** That's a reasonably short path for a, uh, two-layer, uh, complex two-layer board like this. But if you turn the top on, there might even be a shorter path. Uh, no, yeah, like it might jump back over a via here.

**Dave Jones:** Yes, it does. Look at that. That's handy. They just happen to put in a via here and a via here. So, the path is actually shorter. It goes through here like this and goes back over to here and that is kind of the shortest path.

**Dave Jones:** Otherwise, it's got to go all the way over here on the bottom and all the way around on that green layer there, but still, that's relatively short. So, you might think that's not too much of a problem.

**Dave Jones:** But, aha, what about the bypassing? When your signal transitions like this, the capacitive load and the capacitive traces and everything else actually a capacitor, when you apply voltage to it, it first when you transition up like that, it appears as a short circuit, and that generates a little gulp of current, and that current should come from the bypass capacitor.

**Dave Jones:** So, let's have a look at the bypass capacitor for these two devices. Look at this. Here's the VCC pin of the RAM chip. The bypass capacitor goes down to this ground here.

**Dave Jones:** And look, the the two chips are actually sharing a very short power path. So, that's almost ideal. So, if you just look at that from a point of view of like the loop area, from a point of view of just the power pins, everything's reasonably hunky-dory for this particular trace.

**Dave Jones:** Remember, we got hundreds of these traces on the board, each with their own loop area, cuz they're all switching, and they all intermix. That's why you get all that huge broadband noise measured across the spectrum.

**Dave Jones:** Now, but the problem is the ground for this. Here's where we might come a gutser. It goes up here. Oops, where else does it go? Look at this. It's got to go all the way over here, all the way over here, all the way over here.

**Dave Jones:** If it's just on this layer, then it's just snakes its way back through there, and it comes back through the trace. That's a huge loop area. Now, of course, if we turn on the top layer, we might be lucky, and we might get some via stitching in here.

**Dave Jones:** Let's have a look. Actually, this one's not too shabby. The ground from here goes on the bottom layer, the green layer over to here, then jumps up onto the top layer, the red goes through this via, and there's another one up here as well, goes down here, and then can drop down to the bottom layer like this, and then go to the pin like that, but you

**Dave Jones:** know, it's it's a bit higgledy-piggledy. It's not ideal. There's only one There might only be one lousy via in there, which is going to be higher impedance at higher frequencies.

**Dave Jones:** It's got more inductance, right? So, that is the problem, the inductance of your vias, and all the and your inductance of your ground paths and your loops and all that sort of stuff comes into play.

**Dave Jones:** So, you know, we're we're still kind of within this area, but it's going to be much higher inductance, and it's just running all over the shop. And if you were the PCB layout person, you forgot If you didn't put this like via stitching in here like this, then wow, it'd be like traveling all over the board, and the loop area would be larger and larger, and generating a greater electromagnetic

**Dave Jones:** field for a given particular switching current. But, if we go over to the four-layer board, we have a look at exactly the same signal like this, you'll notice that Well, there's no more flood-filled ground planes on the top and bottom, cuz the whole board is one ground plane.

**Dave Jones:** So, now the trace is exactly the same, but this ground pin can go all the way over to here, this ground pin. Not only it's the same length path, but it's lower inductance, because it's a big solid ground plane going right over, and then that's solid ground plane is also connected over that entire area right up to this bypass capacitor here, and likewise for the power, cuz we've got a

**Dave Jones:** big power plane on there. So, the loop area is a little bit smaller in here, but it's much lower inductance, so it's going to be much more effective. And also, you've got the shielding provided by the ground and the power planes, which makes a difference with magnetic electric fields.

**Dave Jones:** We won't go into the details, but it makes a big difference. And that loop area, if you don't keep that small, Faraday's law is going to screw you over and the greater the area, just like the reason why you have two different size magnetic H-field probes.

**Dave Jones:** They've both got one loop in there. There's just one loop. That's it. But this one is a larger diameter, so it's more sensitive. It works in the reverse if you've got a larger loop on your PCB, it generates more and it receives more if it's bigger.

**Dave Jones:** And that's just a singular example of one particular trace. Remember, you've got hundreds of different traces, each with their own loop area. And let's have a quick look at the power system on Once again, we're back on the two-layer board.

**Dave Jones:** So, this is actually the VCC or power pin. You'll notice how it's just running Look, it's got to run right around here like this. So, imagine if you had a source up here and a destination down here and it's got to go all the way back through that power and the local D coupling you know, wasn't right and the split ground planes were split.

**Dave Jones:** And that's the problem. Split ground planes are always a killer cuz they're instantly going to generate more loop area. And then if you have traces running across splits, that's really bad for EMC and there's all sorts of stuff like that.

**Dave Jones:** So, you know, look it's just it's just a problem and it's nothing wrong with this layout. This is a good two good layout two-layer board that I put in via stitching in there to try and sort of, you know, shorten the grounds everywhere.

**Dave Jones:** When you flood fill a two-layer board like this, yeah, you should just pepper everything with vias. Sometimes you can screw it up and it might cause a loop where you didn't want it to go or something like that.

**Dave Jones:** But in in general, yeah, the more you stitch those planes together, the better the luckier you're going to get and you're going to avoid Murphy and you're going to hopefully, you know, not be too bad.

**Dave Jones:** But, there's absolutely no competition compared to a solid ground and solid power plane across the board. Now, if you had a three-layer board, you wouldn't do a three-layer board cuz they manufacture them in two in even numbers, but let's say you did and you only had the ground, then you'd still have the power like this and you might still have at lower frequencies, for example, because the bypass capacitors work at

**Dave Jones:** different frequencies and they have different responses. Done videos on that. So, the lower frequency current has to flow in much bigger loops than the higher frequency stuff does. Whereas, if you have that nice solid ground and power plane, then the loop areas are going to be much much smaller.

**Dave Jones:** Check this out. I found one that's worse. This one has a source in two destinations. It's the Y0 pin. I don't know what it does. It's a TTL computer.

**Dave Jones:** So, it connects this chip here, this one, and this one here. And the ground's actually pretty good. If you look at this, say between this chip here, goes over to this one here, right?

**Dave Jones:** So, it's oh, and there. So, right? So, that's a relatively short ground path, but let's look at the bypass capacitors, which as as I said, is where all that high frequency uh stuff comes from, the high frequency bypassing.

**Dave Jones:** That's why you have the bypass capacitors. Look, this one goes up and goes up to here and then it's connected to this bit of ground up here. And that bit of ground is like split on this half.

**Dave Jones:** It's split by this power rail running right through the guts of this. So, unfortunately, that's like it's going to have a hard time getting back. So, that loop area is going to be much larger for this actually trying to get back between these particular chips.

**Dave Jones:** And then the bypass capacitor for this chip here is over on this particular ground, which is not via stitched over to this one, which has to go all the way Yeah, it doesn't even go all the way across and maybe there's some via stitching in there, but it's it's like connected to a totally different split ground plane.

**Dave Jones:** And it might make its way back higgledy-piggledy somewhere, but yeah, that's yeah, no wonder this thing has a lot more um EM radiation than the four-layer board. Cuz the four-layer board would just flood that top and bottom under the chip with very low inductance, very low impedance uh ground and power loop paths for the bypass capacitors and the signal.

**Dave Jones:** Because the return path wants to take the lowest impedance. And I'll have to I think I did do a video on this. Takes the lower impedance. So, if you have the ground uh and power under here, then the return current will actually follow and flow the high-frequency return current will flow and follow this particular trace.

**Dave Jones:** Or it'll try to. But if you don't let it, because you've split your ground plane right through, yeah, you've got a huge loop area. It's just spewing out the radiation.

**Dave Jones:** So, there you go. It's all about loop area when you're laying out boards and when you're the difference between two-layer, four-layer, everything else. But not only just loop area, it's at particular frequencies, at different types of bypass capacitors, different currents, different capacitive loads and things like that.

**Dave Jones:** Um different whether or not it's generating electric field or magnetic field or electromagnetic combined field and things like that depending on the source impedance and the load impedance and all sorts of things.

**Dave Jones:** It gets really complex. So, does this mean that two-layer boards are just inherently horrible and you should avoid them at all costs? Well, no. You can actually do quite decent uh layouts and approaching the performance of a four-layer board on a two-layer board if you're careful and you're lucky with the layout.

**Dave Jones:** Unfortunately, with the design of this sort of complexity, this many number of chips spread over this, you know, convoluted arrangement, you're you're just going to get issues. A four-layer board's just going to be, you know, it's just going to bury the performance of for this particular design here.

**Dave Jones:** But, there are some good practices you can do on two-layer boards like try and keep your ground and power on top of each other wherever humanly possible. Don't try and split the ground.

**Dave Jones:** Do extra via stitching and flood fills and stuff like that to try and keep it as tight as possible. In fact, a well-laid-out two-layer board might actually have less radiated emissions, i.e.

**Dave Jones:** have better performance than a poorly-laid-out four-layer board. So, it you know, but four-layer it's just going to four-layers, having the ground and power planes just makes it much easier and you're less likely to screw up.

**Dave Jones:** Just remember split ground planes really bad. So, if you got to chop up your ground and power planes four-layer board, that can cause problems, too. But, like there's lots of When you go down the rabbit hole on designing PCB layouts for EMI EMC performance, there's just a almost an infinite number of things to consider.

**Dave Jones:** I might do some more videos on that if you want me to. Let me know in the comments down below. But, there have been and there are like entire books devoted to just doing this sort of stuff.

**Dave Jones:** So, yeah, it can get quite complex. And there might actually be a follow-up video to this if I can organize it of actually comparing these two-layer and four-layer boards in an actual EMC test house or maybe on an outdoor test area called an Oates, an an outdoor area test site.

**Dave Jones:** So, but that obviously requires a lot of planning and facilities to do that. I don't have that here. So, you could do that in the far field. You can do like far field tests in your lab.

**Dave Jones:** you can get you can buy an expensive EMC antenna. You can sort of roll your own, but they're a bit how you're doing. And but anyway, it can give you a decent indication.

**Dave Jones:** You can put it a meter, 2 m away. You can Companies even make their own RF and anechoic chambers and and stuff like that. And but you know, you can do that sort of stuff, but just using your H-field and your E-field probes going around your board, you can like and just check in for any sort of nasties hidden in there, that can really save your bacon when you uh go for

**Dave Jones:** testing later. So, while there may not be a direct correlation between the near-field test we did here and the far-field ones you'd get in a EMC compliance testing, it's you know, it's not a bad sort of correlation.

**Dave Jones:** So, the two-layer one would absolutely definitely perform worse than the four-layer board in a true EMC compliance test over the full spectrum. There's no doubt about it. So, anyway, I hope you like that video.

**Dave Jones:** Hope you learned something. If you did, please give it a big thumbs up, and there will be more videos hopefully coming on this soon. I want to show you how you can construct your own near-field probes.

**Dave Jones:** And also, I'd like to do something getting a heat map of H-field radiation on a large board like this. So, maybe we'll have a do-it-yourself project for that as well.

**Dave Jones:** So, we'll see what happens. Catch you next time.
