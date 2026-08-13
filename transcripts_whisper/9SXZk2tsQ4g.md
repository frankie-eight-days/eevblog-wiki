---
video_id: 9SXZk2tsQ4g
title: EEVblog #824 - GW Instek GDS-1000B Oscilloscope Teardown
url: https://www.youtube.com/watch?v=9SXZk2tsQ4g
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 25, "2": 49, "3": 61, "4": 81, "5": 101, "6": 117, "7": 137, "8": 153, "9": 169, "10": 185, "11": 201, "12": 221, "13": 237, "14": 253, "15": 269, "16": 289, "17": 301, "18": 321, "19": 341, "20": 357, "21": 373, "22": 389, "23": 405, "24": 425, "25": 441, "26": 465, "27": 489, "28": 505, "29": 529, "30": 545, "31": 557, "32": 573, "33": 589, "34": 609, "35": 629, "36": 641, "37": 657, "38": 673, "39": 689, "40": 713, "41": 733, "42": 749, "43": 765, "44": 781, "45": 797, "46": 809, "47": 825, "48": 845, "49": 865, "50": 885, "51": 901, "52": 917, "53": 937, "54": 953, "55": 969, "56": 985, "57": 1005, "58": 1025, "59": 1041, "60": 1061, "61": 1077, "62": 1097, "63": 1117, "64": 1133, "65": 1157, "66": 1177, "67": 1197, "68": 1217, "69": 1237, "70": 1249, "71": 1265, "72": 1289, "73": 1309, "74": 1329, "75": 1345, "76": 1361, "77": 1381, "78": 1397, "79": 1413, "80": 1437, "81": 1457, "82": 1473, "83": 1493, "84": 1513, "85": 1533, "86": 1549, "87": 1565, "88": 1581, "89": 1609, "90": 1629, "91": 1649, "92": 1669, "93": 1689, "94": 1705, "95": 1721, "96": 1741, "97": 1757, "98": 1781, "99": 1797, "100": 1813, "101": 1865, "102": 1889, "103": 1909, "104": 1933, "105": 1957, "106": 1981, "107": 1997, "108": 2013, "109": 2033, "110": 2049, "111": 2073, "112": 2093, "113": 2113, "114": 2129, "115": 2137, "116": 2161, "117": 2181, "118": 2201, "119": 2213, "120": 2233, "121": 2249, "122": 2265, "123": 2277, "124": 2293, "125": 2313, "126": 2329, "127": 2345, "128": 2361, "129": 2381, "130": 2397, "131": 2413, "132": 2429}
---

**Dave Jones:** Hi, welcome to another oscilloscope teardown. This one's going to be rather interesting, because this is a really bang-per-buck entry-level 4-channel 50 MHz scope. It's a GW Instec GDS1000B series. I've got the 1104B, but the 1054B is the 50 MHz version, 4 channels, for

**Dave Jones:** a street price of $386 it's currently going for. So it's cheaper than it's direct competitor, the Rigol DS1054Z. Let's check it out. This won't be a comparison, but I can't help it. Just a little bit before we do the teardown. And it's great to see competition

**Dave Jones:** in the market like this. They, I think they announced this scope back in June, but I think it's only been started shipping fairly recently. Although, I could be wrong on that. Anyway, we've got our hot little mitts on one, and we're going to tear it down.

**Dave Jones:** But check it out, it is substantially bigger than the Rigol, but it's the Rigol actually weighs 3 kilos, this is 2.7 kilos. Substantially lighter, actually. But yeah, look I mean, it's supposed to have the same size screen, but just sort of optical illusion type thing.

**Dave Jones:** This one actually GW Instek actually looks smaller, so it's not as effective use of space. But you'll notice that it's got all four separate vertical controls. Absolutely brilliant. Whereas the Rigol, you've got to dick around with just the single channel there to do it.

**Dave Jones:** So it's much better. So that's the advantage of having the bigger form factor, you can get the extra vertical controls in there. But the GW Instek does actually look quite wasted. You could have made it smaller and sort of compacted everything. It just seems a bit too big.

**Dave Jones:** Well, hey, wait until we see inside to see if they've wasted any space inside, but they could have tried to make it more compact. That's one of the advantages of the Rigol 1054Z anyway. And you'll notice that this is like a real off-yellow kind of, hopefully it shows

**Dave Jones:** up on camera. I have got my white balance set correctly for the color spectrum studio lights I'm using here. So hopefully this should be fairly accurate color. But it's kind of like the case is white, but the panel is kind of this yellowy

**Dave Jones:** color. I don't really like it. But apart from that, I really like the way it's laid out. The vertical controls are excellent. Yes, the knobs are pushable, push to zero there. And also for the trigger level as well, you can push that back to zero, you can push the horizontal position

**Dave Jones:** back to zero. Fantastic. The horizontal section, it's got separate search, which of course the Rigol doesn't have. So you know, a replay mode control directly there, which the Rigol doesn't have. Very nice. And I like how the trigger settings here are totally separate.

**Dave Jones:** But just like the Rigol, you don't get an external trigger, but that's not uncommon on a 4-channel scope. And other little niceties, a 50% trigger level button dedicated, the Rigol doesn't have that. So you know, it's got the same force button, which is okay.

**Dave Jones:** But yeah, I really like that run-stop. The auto set is not sort of recessed or anything like that. But the menus are, look at the buttons, it all looks very bland and amateurish. So I don't know who the user interface product designer is

**Dave Jones:** at GW Instec, but I don't know what they've got going. I mean, but this is the look of GW Instec products. I guess some people might like it. I personally think it just looks a bit amateur, that's all. In terms of like product design, it's not

**Dave Jones:** shout out, wow, that looks sexy. It just looks, I don't know, meh. But, big clunking power button. Oh, that feels like a real power button. Oh! Don't want to turn it on, we want to take it apart. But spec-wise, it is 1 gig sample per second, which is

**Dave Jones:** unfortunate given the 4 channels, because when you, I'm sure it will actually halve and then go down to a quarter, so only 250 meg samples per second, which is not enough for the 100 megahertz bandwidth. Fine for a 50 megahertz bandwidth scope though, but considering you only pay

**Dave Jones:** 386 US dollars for this puppy, oh, for a 4 channel scope, brilliant. It's got the same 7 inch colour display, I believe it's the same resolution as the Rigol, we might boot it up after the teardown of course. And it's got 50,000 waveform updates per second maximum, which is better than the Rigol's

**Dave Jones:** at 30,000 waveform updates per second. It's got 1 meg FFT which is fantastic, which we'll have to have a play with in a separate video, which the Rigol doesn't, so that's good for signal analysis stuff. And as I said, it looks like easier to use.

**Dave Jones:** And just like the Rigol, there's no auto probe detection or anything like that. One of the most unusual things about this though, is check it out. Let's go over the top here. Where's my scope? Where's my scope? Where's my scope? Where's my scope?

**Dave Jones:** Where is it? Where is it? Oh, there it is. Jeez, this is weird. So yes, it's actually very disconcerting at first when you actually look at this thing. I mean it's not uncommon on scopes these days, other brands I think do this, I can't remember, but it does have a carry

**Dave Jones:** handle. Look, there's nothing in it. Obviously they've got like the power supply, it looks like power supply tucked down the bottom here, and just one big possibly just one big main board at the back there, but it just looks weird. I don't know, it doesn't instill confidence

**Dave Jones:** in me, but I know that's not right, but I don't know it's just funny. And it's made in Taiwan, as I believe all GW INSTEC products are, because they're a Taiwanese company, not made in China. It's just different. Yay, Taiwan. And supposedly 30 watts

**Dave Jones:** power maximum, I don't know what it actually draws in practice, we'll have to compare it with the Rigol. And on the back we've got USB device, we've got LAN, which is pretty standard on even your entry level scopes these days, absolutely incredible. We've got an open collector go, no go

**Dave Jones:** output, whether or not that can be used to get our update rate, i.e. it's a trigger output as well, I don't know, you'd think it, expect it to say it there. And a curious calibration BNC, so I presume that's only for factory cow, but seems a bit of a waste.

**Dave Jones:** And the scale knobs have indents on them, they feel quite reasonable, but the position controls and the variable control up here and the trigger level, they don't have any indents and they feel a bit scratchy, a bit itchy and scratchy. Not... I don't know what to think about that, whether it's

**Dave Jones:** good or bad. Hmm. And no, you don't have to worry about it toppling over if you press the buttons, so even if you press them vigorously it's not going to fall over, hopefully. Woohoo! Alright, you know what we say here on the EEVblog, don't turn it on, take it

**Dave Jones:** apart, let's go! Void that warranty, beauty. Well, turns out there is no warranty void if not remove sticker. Beauty! GW Instec support hacking, I like it. And there's just 4 screws on it, let's lift... hopefully. I think I got them all. No, no, she's not going to let me in.

**Dave Jones:** No, mongrel. Aha! Just a couple of little clips under there. There we go. And we're now in like Flynn. Wow! Now the first thing I noticed was just the general, like, wasted space. Where is everything? I expected like one big board, but we've got a

**Dave Jones:** board effectively half the size of the case, one just interface board, which is just, looks like there's no active circuitry on there, just some terminators going off to the LCD there. But there's one other thing. Can you spot it? That, I just instantly went, what the?

**Dave Jones:** Look! The fan! It's sucking from the outside, okay, there's a vent on the back, and it's blowing out the other side! Like, what the? Where the hell? Like I thought, okay, it's, you know, something's getting hot on the front end, okay, and it's blowing right into the front end can, but

**Dave Jones:** look at it! Look at it! That is the... What have they done? What were they thinking? When they put a fan like that, that has to suck in there and then instantly just reflect off the shield in there, and then just go out here, and what

**Dave Jones:** it's not flowing over the power supply at all. It's not flowing over any of the, you know, active circuitry. In fact I can't even see any of the active circuitry, got to be on the underside. Where's our main processor? That's our ADC, obviously.

**Dave Jones:** Got our four analogue channels, got some power supply stuff, and well, maybe it's under here is the main well, actually I can see the traces going off there now, but yeah, so I think our main processor, but where does that air, why even have the fan at all?

**Dave Jones:** Unbelievable! Okay, I see what they're doing now. If you have a look at the case, this is why I said, oh yeah, like the power supply's in here. You'll notice that here is the inlet grill down here, it actually has a surround around it

**Dave Jones:** so the air comes in through the back, it's blown out here onto this can, and then over here, but it can't go anywhere, because they haven't put the, any vents in the side here, so that's good. So all the air essentially has to be pushed across the power supply, and then

**Dave Jones:** out this vent on the other side with this lip here, effectively you know, it's not a seal, but it effectively contains the air path going in and then across the power supply, but like it's got extra air resistance here, you're not getting efficient volume of air movement, you know, volume per

**Dave Jones:** hour or whatever you want to calculate it in. You know, much better off sticking the fan on the side here and then blowing it across, but they've only got a certain depth but they probably could have, I don't know, I still don't like it.

**Dave Jones:** But it does show that they do, did actually think about it and thought about the air path, and it's mostly over the power supply, that's pretty much the only thing the fan's doing, so the rest of the circuitry can't get that hot at all, because there effectively is no air flow for it.

**Dave Jones:** And the power supply looks fairly average and low cost, doesn't really instill a huge amount of confidence in me, but as I said, that big clunking power switch feels really solid. Yes, it is a real power switch. Why they've got this extra jumper wire going

**Dave Jones:** over here like this, I don't know. Anyway, they've got the requisite common mode choke and filter and stuff like that on the input, and well, you know, it's passable. Well hello sailor, look at the primary input cap. It's a Nippon Chemicon. Beauty, I'm surprised.

**Dave Jones:** And likewise all the ones on the secondary side here, they're all Nippon Chemicon as well. Fan-freaking-tastic, well done in such a cheap scope. Unbelievable. So whilst that power supply might look cheap, it's not all in appearances. Looks like they've got quality parts, they've got

**Dave Jones:** thermistor protection down here, there's no fuse protection in it, but that's good enough. They've got a transorb there by the looks of it, and all the requisite stuff. Quality caps, excellent. Just, I don't still get the heebie-jeebies about that fan. It's probably not drawing

**Dave Jones:** too much power, just a standard .1 inch ribbon header there going over for the main power. But you'll note that up in here on the main board, they do actually have some of the solder masks removed and tin coating on a couple of the tracers

**Dave Jones:** running up there to presumably the main processor up here. So just to get a little bit lower impedance and extra current carrying capacity. And if you're wondering about the earthing on that, I would have done it better coming straight from there, but you know, they've done the pin thing, so there's

**Dave Jones:** a pin on the bottom of that in the center, it goes over to this grounded stud which then just connects on the bottom and goes down to the main chassis down there. Hmm, it's adequate. Well this is rather unusual. The main board here is effectively just

**Dave Jones:** the analog inputs, the ADC is probably a little bit of triggering. No, that'd be the pass-fail outputs or something, but it's probably some triggering stuff on there, perhaps maybe on the other side of the board. We'll have a look. But this daughter board here is actually

**Dave Jones:** the processor board. This is the bottom of it, and there's a heatsinked component on the top. Because if you have a look down there, the main board is actually cut off like this and goes all the ends cut off right down to the bottom

**Dave Jones:** down here like this. So your main processor's on that board. What the what? Like, why have they done this? Some sort of upgradeable capability? They didn't want to change the main analog board? I don't really get it. This one's marked as a 4-channel, of course

**Dave Jones:** if they did the 2-channels, they'd only populate the 2-channels down here. You can buy a 2-channel version, but only in the 70 MHz version. And speaking of which, the 2-channel 70 MHz version is even cheaper. So if you don't need the 4-channels and you're happy with the large size, you can actually get this

**Dave Jones:** for like $356 street price or something for the 2-channel 70 MHz version. But I would highly recommend going for the 4-channel 50 MHz version any day of the week. I can't see any compelling reason to buy the 2-channel 70 MHz version for, you know, $20 cheaper or whatever it is,

**Dave Jones:** $30 cheaper over the 4-channel version. No way. Go for the 4-channel every time. Now, the main board actually uses, I've never heard of them, Jamecon brand caps. Yeah, they aren't name brand at all. So maybe that's quite curious because the power supply, maybe they farm that out, which is quite common

**Dave Jones:** with companies, farm that out to a different, like a specific power supply specialist company to do that, and they handle the bill of materials and they specified Nippon, Jamecon. But you know, when Goodwill did these, now they're purchasing people just went, ah, let's get Jamecon, we can get those

**Dave Jones:** this week, super cheap. I'll tell you what, I'm not impressed with how they're holding this board down. They've got high frequency surface mount board-to-board interconnect connectors on here going down to the base board, but they're holding these in with plastic clips. This seems to be just a free-standing

**Dave Jones:** standoff, I didn't realize that, so I shouldn't have taken that out. But yeah, not impressed with that mounting scheme at all. Come on, screws. Hang on, I don't remember taking that screw out. What the? What's going on? Anyway, they've got a, looks like a little springy

**Dave Jones:** shield thing connecting the ground on the main board here down to there, but why don't they just screw it? What have they added that and done away with the screw for? I don't get it. And the other thing of course is that there's absolutely like no shield

**Dave Jones:** in this. The power supply is not shielded from the outside world, the power supply is not shielded from the main ADC and other stuff. I mean, sure, the analog front end is you know, shielded, that's a given, but apart from that, the power supply

**Dave Jones:** you know, it's just flapping in the breeze there, but I suppose it's past FCC and all that, so yeah, but it's a stark contrast to the Rigol DS1054Z which is why it's so heavy. It's just chock full of shielding. Shielding right up to the wazoo.

**Dave Jones:** Well, here's the main processor board, and it is bizarre. It is so not what I expected. Under the tiny little heatsink here, which is going to have no airflow of course, as I explained before, that's most likely an FPGA. I don't think GW Instec

**Dave Jones:** have spun their own ASIC, although to get like 50,000 waveform updates per second, it's supposedly on spec at least, it's you know, quite a fast scope. I've yet to try it out with responsiveness and you know, everything else, but it's fairly grunty, so I'm assuming that's like an FPGA and

**Dave Jones:** not some sort of applications processor, but it drives the LCD directly. So we've got our sample memory here, we'll take a closer look at exactly what type, and they've got 10 meg per channel by the way, which is not shared apparently, although I'm yet to confirm that.

**Dave Jones:** We've got flash memory and just the main processor slash FPGA, but is it an FPGA? I don't think it can be, or just never, like it might be a hybrid one with you know, like a zinc or something like that, with a built-in ARM Cortex processor, because look, it's got

**Dave Jones:** LC, where's the LCD driver? Right? This goes directly out. I don't think it's one of those like media processors or you know, shark or anything like that, because there's just not enough grunty in it to get 50,000 waveform updates per second usually, so that's you know

**Dave Jones:** quite grunty. So I don't know what's under there, and unfortunately the heatsink is glued on, I don't want to take it off because that could require some force and I'd probably bust the decent likelihood of busting the little fragile BGAs on there. And it looks like our main sample memory here, these are

**Dave Jones:** 1 gig bit each, so arranged in 64 meg by 16 bit. So we're talking, you know, well there's 2 of them, so there's 2 channels per chip. So we're looking at 128 megabytes per chip, meg samples per chip, so we're looking at 64 meg

**Dave Jones:** samples per channel. No wonder they can do the full 10 meg samples per channel on this thing. So what are they using the extra for? Maybe for the variable intensity display and the history mode and stuff like that. So more than what they need.

**Dave Jones:** And those 2 puppies look like Texas Instruments 1210B, they're USB transceivers and that one there looks like I'm guessing is going to be the Ethernet controller. Yes, it's all on the board, not right next to the connector, so it's all going through these high frequency board-to-board interconnects, and

**Dave Jones:** going all the way over the board along the yellow brick road, over the rainbow, to our rear panel. And that is an analog device, it's ADP 5052 that's just a power supply jobby. Wait, hang on, hold onto your hats. This wiggles. This wiggles, it's off!

**Dave Jones:** It's a zinc! I was right! There you go, it's a zinc. Yeah, that was a good bet, because it couldn't just be an FPGA, because it needed applications processor to actually run an OS and everything else, so they're not going to put that in some soft core, so the zinc is a

**Dave Jones:** nice chip. It's basically a Xilinx FPGA, plus it's got an ARM core, or maybe 2 inside. We'll have to check the part number. Well that heatsink was pretty piss-poor, wasn't it? And this puppy is a real beast, it's a zinc 7000 series, it's got an ARM Cortex A9 in there, 1 gig

**Dave Jones:** whoa! And it's 2.5 DMIPS per megahertz, so incredible processing power. It's got a Neon Media processor in, whatever that does, but hey, it's I don't know, maybe they're making use of that. It's got vector floating point units, and more bells and whistles than you can poke a stick at.

**Dave Jones:** But of course that's just the ARM Cortex processor in it, it's actually a Xilinx FPGA, it's the Artex 7 architecture, and this one's actually the bottom of the range one, actually in terms of number of logic elements in there, it's the cheapest one.

**Dave Jones:** It's got 35,000 flip-flops, it's only got 28,000 logic elements, so not a big FPGA, but it's got DSP units, you know, and block RAM, like 30 odd K of block RAM or something like that, so you know, it's doing a decent amount of stuff in there.

**Dave Jones:** But that's basically it, that's all there is in it. It's basically an ADC which we'll take a look at, coupled onto a zinc ARM Cortex processor, a really fast one with some FPGA fabric, and bingo, you've got yourself like a modern 30, you know, whacking some software of course, lots of software magic, but do that

**Dave Jones:** and basically that's all the hardware required for a modern you know, 50,000 waveform updates per second variable intensity display scope. It's incredible. Geez, when I was a boy, this thing would have taken a room full of stuff. And is this puppy here a JTAG programming header or a

**Dave Jones:** serial debug console interface? Not entirely sure, not silkscreen labelled. Aww. And absolutely no surprises at all for finding a HITITE analogue to digital converter in here. They're in everything. This is the chip of choice in these low-end scopes. This is a 1 gig sample

**Dave Jones:** per second single channel converter, or a 250 meg sample per second 4 channel, or 500 meg samples per second 2 channel. That's why this thing is going, because they've only got one of them for the entire scope. You know, save cost, because these things aren't exactly cheap when you're pinching pennies

**Dave Jones:** on a scope like this, so we have to share that between all 4 channels. So unfortunately the 1 gig sample per second does drop down to 250 meg samples per second on when you've got all 4 channels on, so that's not enough to actually

**Dave Jones:** get a proper recreated signal on a 100 megahertz bandwidth analogue input channel. But it's okay for the 50 meg bandwidth model. And if we pop the hood on the front end, here we go. 4 identical channels of course, we're in like Flynn, and it looks pretty basic.

**Dave Jones:** There's probably some on the backside as well, but I'll have to take the entire board out to get a look, so it looks pretty basic. Exactly what you'd expect from a modern 100 megahertz front end. And unfortunately we can't get this board out without taking out the whole

**Dave Jones:** thing from the front panel, so I have to take all the knobs off. There's our membrane for the front, no wuckers at all. We're going to have a main keypad PCB underneath this, but let's swing this around. The reason why we couldn't get it out is because

**Dave Jones:** ta-da! There's our BNC nuts. Mongrels. But there's our screen, there's all our keys, everything else, everything's hunky-dory. Our LED backlights and things like that for the buttons are surface mount on there, so that's all hunky-dory. What switches are these? We've got 124C3, there's no brand on these things by the looks of it.

**Dave Jones:** 112C2, so these are the indented ones, and these are the just regular non-indented ones, which feel a bit itchy, scratchy. And certain things have to be assembled in certain ways. The PCB mounting power supply studs on here for example stop me actually lifting this board out, so I've got

**Dave Jones:** to actually take these screws off and move that before I can physically get this board out, so eh, just, you know, small things like that. But ta-da! We're in like Flynn, and yep, we've got some stuff on the back anyway. And these things here look like 4000

**Dave Jones:** series CMOS 4094, so 8-bit shift registers, so that's obviously, you know, how they're getting some control data to each channel. They're just, you know, saving some lines going over the PCB there. And that's around our calibration output, nothing much happening there at all, we've got a TL074

**Dave Jones:** classic and another one of those 4094s. And curiously we have an unpopulated part there with a heatsink pad on the bottom, not sure what that is, that's basically just below the analog to digital converter, that's on the flip side, so I, would that some sort of clock PLL?

**Dave Jones:** Or something? Perhaps looks kind of something like that maybe, but like, why is it not there? I don't know. Speaking of which, I did forget next to our ADC there, we've got an 1102TI4A, whatever the hell that is. I don't think it's a HITITE, not sure if it's a

**Dave Jones:** HITITE one or not. Diff pair coming out here with 200 ohm series resistors there, so yeah, it's doing something like that, some clocky thing. Tell you what, there's not much doing on this front end here, of course we're going to have a discrete FET front

**Dave Jones:** end perhaps, and we've got ourselves a relay, and a trimmer cap, no worries, it's all pretty standard, a TL074 thank you very much, of course that's not doing any high frequency stuff, that's just doing some level and bias stuff. And pretty much all discrete front end.

**Dave Jones:** And likewise, if we flip it over the other side, it's still all discrete, there's nothing else happening there. It looks like this could be our main puppy over here. And nope, it's not that, that's an analog device, that's AD5207 that's just a digital pot.

**Dave Jones:** You know, a squared pot 256 positions, so that's just doing some level adjustment and under digital control. What else have we got on the front end? That's our TL074, we've got ourselves a 4053 MUX, so analog switch, there's a TL071 jeez, as it looks like, is this entirely

**Dave Jones:** discrete front end. Oh hang on, it's just dawned on me that these aren't all identical. Look at them. This channel here, yeah that's channel 1, is identical to channel 3. Look, we've got two 14-pin packages, three 14-pin packages there, or 14 and 16

**Dave Jones:** I think that, yeah, 16, that's 14. But this one has an SO8 in here instead of this 16-pin package, and this fourth channel doesn't have either. What the? Apart from that, all the discrete stuff looks the same. Okay, so there's all our discrete amp all in there.

**Dave Jones:** That's the same, but this stuff here differs. Weird. And this one here is an additional 4053, so we've got two 4053s, or one in these channels. This puppy here is a bit different, it's a TL072, so it's a dual op amp, whereas we've got

**Dave Jones:** one TL071 on each channel. But why does like channel 2 here have a TL072 in it, and none of the others do? Eh? So that's interesting. All discrete front end, and where have we seen this before? The Rigol DS1054Z. I've done a complete

**Dave Jones:** reverse engineering video of the front end of the Rigol, so it'll be really interesting to do a reverse engineer of this one and see if it's the same. But it's basically all discrete transistor, the 4053s, if memory serves me correctly, exactly the same as what's on the

**Dave Jones:** Rigol, the TL074s and everything like that. It's got a discrete transistor diff amp output and things like that, so I won't reverse engineer this one, but I'll put the high res photos up for anyone who wants to have a crack at that. It'll be interesting to see how equivalent

**Dave Jones:** it is to the Rigol. Hmmmmmmmm. So you can really see how GW Instec are being clever here in that they can sell, and why they can sell this cheaper than the Rigol, which was already super cheap. They've got basically an equivalent discrete transistor analog front end, and

**Dave Jones:** the ADC is different. I don't think the Rigol used the Hitite one, so I'm not sure of the price comparison difference there, but take a look at the teardown photos of the Rigol and you'll see that it's got a lot more horsepower in there than

**Dave Jones:** the GW Instec. Well, not necessarily horsepower, but there's certainly just a lot more chips to handle. It had multiple FPGAs to do it, plus a main application processor, whereas the GW Instec is doing everything in this tiny little zinc. That's basically the entire processing engine for this thing, and if you

**Dave Jones:** can get away with it, well, you know, which I'm sure you can, it's a super duper powerful chip, then that's very clever and cost effective. So I'd love to know the actual bomb cost of this compared to the Rigol, it'd be very interesting

**Dave Jones:** to see, but of course we're never going to get that information, that's super duper proprietary. But there you go, an incredibly simplistic design for a modern, you know, 4 channel 50, 100 megahertz bandwidth scope with variable intensity display and all the bells and whistles.

**Dave Jones:** Absolutely incredible. ... ... Forgot the bloody heatsink, didn't I? D'oh! Alright, will it work? Here we go! ... Yes! It's booting! It's taken a while, and that fan's a bit noisy too. Bloody whiny little thing, no wonder. And we're in like Flynn. Well, I'll tell you what, I'm

**Dave Jones:** actually quite impressed with the basic responsiveness of this thing, it's actually really it's practically instant, it's better than the Rigol, it's faster, that zinc processor's really kicking some arse. Oh, hello, what's that? Whoa. Whoa. What's going on here? Now, I've got 4 channels on there

**Dave Jones:** and we're at... what are we? Where's the horizontal? 5 nanoseconds per division, so we're almost... yeah, we are as fast as we can go. And we've got some funny business happening on channels look! 2 and 3! No, just 3, is it? Sorry, just 2.

**Dave Jones:** Oh, no, look! Look, it's going from... like, there's little... there's periodic pulses in there. Oh no, that's not a division. But jeez, look at that! So, and the blue which is the second channel, didn't the second channel have that extra TLO72 in it?

**Dave Jones:** It's like, it's different. I'm at 100 millivolts per division, I've got nothing plugged in, and why is channel 2 noisier than the rest? And there's this periodic artifact here. What the 100 millivolts per division? Check it out. There we go, let's... whoa, look at that!

**Dave Jones:** That looks like a sine x on x interpolation thing. 3 and 4 3 and 4 don't display that, but 1 and 2 when you go all the way down, what the? Look at that! Wow! What's going on? Is this super quick though? I've got to admit, that display update is really fast.

**Dave Jones:** And you can see the difference when I switch between 100 and 200 millivolts, you'll be able to hear the relay click, right? So it's absolutely rock solid flat on 100 millivolts, and it switches to 200 millivolts and then we get some extra noise, and then that will decrease

**Dave Jones:** as we go up. So that's to be expected. So 100 millivolts is the changeover point, but why are we getting... why are we getting that? Why are we getting... that's very disconcerting. Okay, so if I go to record length here, to the acquire menu, you can do

**Dave Jones:** 10,000 points, 10k points, 100k points, it's not going to make a difference. Of course up to 10 megapoints, there is no auto memory on this thing, so you've got to choose your weapon before you go into battle. And that's it's got peak detect, it's got averaging of course, averaging will

**Dave Jones:** should fix all that. I like the variable knob, by the way. The variable knob is a winner. And it's pushing the variable knob rubbish so it accidentally, you know, you don't get the thing that you want to select, and it's right there, you can use your thumb, so we can go

**Dave Jones:** like 32. Thank you very much. But, even with 32 averages, we've still got that crud on our 100 millivolt channel there. What the? Okay, so watch this, I've got them all on 100 millivolts per division here, okay, and we'll run it, and you'll see that there's a bit more, a bit of a shimmy

**Dave Jones:** there on channel 3, and if we stop that, and then we actually scale I know this isn't fair, okay, it's actually, we're working with very few bits now, okay, so you expect it to expand the noise up but look at that! Perfect sine x on x!

**Dave Jones:** So it's obviously doing that at the display processing point, because there's very few samples there. I mean, we're getting like, you know, bugger all, so if we, there's our you know, jeez, can you even see our, is there even a dot there? Yeah, there's one dot

**Dave Jones:** there, you know, so it's like, doop! And, you know, so we're down at a couple of bits so, you know, don't think that's, you know, it's a display processing artifact, it's not necessarily, I don't believe it's like a problem with the layout of the PCB and the analog-to-digital converter

**Dave Jones:** there's no sort of, you know, layout issues and noise and things like that, like just a tiny bit, but when you magnify it up like this, because this is where we actually sampled it at, right? 100 millivolts, that's what it actually looks like.

**Dave Jones:** And it's just when you bring it in, they're clearly doing, not that there's anything wrong with that, I guess, in fact you could argue that it's probably a good thing, they're actually doing the processing on the expanded scale waveform like that, interesting. But anyway, my real concern is just these little artifacts

**Dave Jones:** and once again, I believe that they're display artifacts caused by the display engine, not necessarily sampling artifacts, because we go into dot mode and you probably put a rule across there, like there's, like bugger all, right? So it's not a sampling issue there's something happening with the display there that

**Dave Jones:** happens only under 50, only at faster than 50 nanoseconds per division, so 20, 10 and 5 nanoseconds per division it displays that, so not a show-stopper but just interesting to note, I think GW Instec should take a look at that. And of course if we switch

**Dave Jones:** over to 200 millivolts per division, we expect that noise to actually go up, because you can hear the relays click bang, we go in, and then of course if we stop that and we expand those then we're, yeah, we're really going to get some artifacts.

**Dave Jones:** But there's nothing unusual there because we're actually, you know, expanding that in, but yeah, this isn't sort of the quietest scope, so anyway I'm not, I'm being a bit fussy, I'm being a bit fanny fuss pot here, but let's go down to 50 millisecond, sorry

**Dave Jones:** 1 millivolt per division, and that's noise floor, that's going to clean up, that's because of the high sample rate, the high update rate, I've done a whole video explaining why digital scopes like this are inherently noisy in quote marks like this, but that's fairly, I think that's

**Dave Jones:** on par with the Rigol 1 at 1 millivolt anyway. And that'll certainly drop if we turn our 16 averages on, no workers. One thing this doesn't have though is a high resolution mode, which is quite disappointing, it's only got your regular average mode

**Dave Jones:** doesn't have that boxcar averaging. You know a lot of low end scopes are getting that these days, so it's a bit of a shame this one doesn't have it. And why the hell have an app button on it if you're not going to actually have any apps in here?

**Dave Jones:** I mean do they have any on their website? But like, there's just none. Anyway, enough playing around with this thing, I'm going to go edit a teardown video. I'd love to play with this some more and I almost certainly will, but hope you enjoyed that teardown.

**Dave Jones:** As I said, high res teardown photos on EEVblog.com if you want to have a go at reverse engineering that front end, see if it's the same as the Rigol scope, that'll be really interesting. It's probably extremely similar topology, if not, you know, it may not be exact values and

**Dave Jones:** component parts and things like that, but in fact the op amps were different. This thing used the standard TL074s, and if I remember rightly the Rigol used TLV versions or, you know, like something like that. Just, you know, slightly better specced parts, but

**Dave Jones:** very interesting price point, this thing. It's less than the Rigol for a 4 channel scope. I have no idea if it's hackable, the firmware, like I don't believe you can get a, you have to buy it as the 100MHz unit, I don't believe there's like a software upgrade key to actually

**Dave Jones:** do that, you know, if we go into utility and, you know, pro compensation system, you know, there's nothing like in terms of, you know, we can do self-cal, you know, QR code yay, thank you! But you know, there's nothing in terms of like a software options for doing that.

**Dave Jones:** Firmware version 1.09 for those playing along at home, but this was rather interesting, like you know, corners have been cut, stuff like that, construction's not nearly as good as the Rigol, could have been much smaller, even with the 4 channels like this, they could have, you know, there's a lot of wasted space, as you saw, a lot of

**Dave Jones:** wasted internal volume and things like that. Didn't really like the fan, but I like the zinc processor and FPGA combo in there, that's real fantastic. It seems, on first play, couple of minutes, it seems really responsive. We're going to have to test it

**Dave Jones:** for the claimed 50,000 waveform updates per second, there'll be some sweet spot in the time base where that works, but I don't think there's an option to get our trigger output, which is a bit disappointing, so we may not be able to easily measure that waveform update

**Dave Jones:** rate. But the hardware is, you know, passable, especially for the price point, so I'll give it that. But yeah, just a shame about that, it's not, maybe a little bit smaller or something like that, but anyway if you like the teardown, please give it a big thumbs up, and if you've got any comments, leave them

**Dave Jones:** down below, I always read all the comments, leave them at evblog.com there'll be a huge nerd fight over on the forum about all this, I'm sure, but anyway catch you next time.
