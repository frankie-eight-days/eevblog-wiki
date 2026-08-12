---
video_id: UI0aVEko7ic
title: EEVblog #755 - Fluke PM2812 PSU Ebay Score
url: https://www.youtube.com/watch?v=UI0aVEko7ic
source: youtube-asr
timestamps: {"0": 1, "1": 16, "2": 29, "3": 39, "4": 48, "5": 61, "6": 74, "7": 87, "8": 109, "9": 118, "10": 132, "11": 147, "12": 157, "13": 167, "14": 175, "15": 185, "16": 197, "17": 212, "18": 225, "19": 241, "20": 252, "21": 265, "22": 280, "23": 286, "24": 298, "25": 312, "26": 324, "27": 333, "28": 346, "29": 361, "30": 373, "31": 381, "32": 392, "33": 406, "34": 421, "35": 440, "36": 454, "37": 464, "38": 477, "39": 496, "40": 508, "41": 522, "42": 531, "43": 546, "44": 558, "45": 573, "46": 582, "47": 593, "48": 605, "49": 613, "50": 629, "51": 640, "52": 647, "53": 662, "54": 674, "55": 688, "56": 701, "57": 714, "58": 733, "59": 745, "60": 761, "61": 777, "62": 788, "63": 799, "64": 812, "65": 827, "66": 848, "67": 856, "68": 872, "69": 882, "70": 898, "71": 909, "72": 923, "73": 934, "74": 944, "75": 952, "76": 961, "77": 971, "78": 988, "79": 998, "80": 1005, "81": 1021, "82": 1032, "83": 1045, "84": 1064, "85": 1083, "86": 1099, "87": 1111, "88": 1126, "89": 1134, "90": 1148, "91": 1164, "92": 1173, "93": 1185, "94": 1200, "95": 1212, "96": 1231, "97": 1254, "98": 1271, "99": 1284, "100": 1296, "101": 1324, "102": 1335, "103": 1352, "104": 1360, "105": 1374, "106": 1387, "107": 1402, "108": 1413, "109": 1423, "110": 1437, "111": 1452, "112": 1468, "113": 1484, "114": 1498, "115": 1512, "116": 1524, "117": 1536, "118": 1551, "119": 1562, "120": 1574, "121": 1589, "122": 1609, "123": 1619, "124": 1632, "125": 1651, "126": 1667, "127": 1681, "128": 1713, "129": 1725, "130": 1738, "131": 1754, "132": 1770, "133": 1785, "134": 1799, "135": 1810, "136": 1820, "137": 1836, "138": 1846, "139": 1859, "140": 1871, "141": 1884, "142": 1893, "143": 1908, "144": 1914, "145": 1926, "146": 1933, "147": 1945, "148": 1958, "149": 1968, "150": 1986, "151": 1996, "152": 2011, "153": 2019, "154": 2033, "155": 2045, "156": 2061, "157": 2075}
---

**Dave Jones:** Hi, check out what I scored on eBay for 30 bucks. A Fluke PM2812 programmable power supply one of these system power supplies. 30 volts 10 amps up to 180 watts and I couldn't resist.

**Dave Jones:** It was an absolute bargain. Why was it a bargain? Well, this is actually how it came. It's got no case on the thing and it was sold as like a parts unit working condition unknown.

**Dave Jones:** So, like they bought it and you know, there's a few like there's a loose board in here and stuff like that. But anyway, like I couldn't resist it for 30 bucks.

**Dave Jones:** I thought we'd take a look at it and maybe see if we can get the thing going. Now, this is actually a Philips design before Fluke actually bought Philips.

**Dave Jones:** This was I think it's about a early 90s vintage as of it's the 2800 series. There are different models available. There is one which is much smaller. It's only one which is the 2812.

**Dave Jones:** It's only a single output channel one and you'll see why they do that in a minute. It's actually quite modular and I've never used one of these before. I've I've seen them around but haven't had a look inside the thing and never used one.

**Dave Jones:** But you know, it's Philips made some good gear in this sort of form factor. So, I have no reason to doubt that it's not a pretty decent quality system DC power supply.

**Dave Jones:** Now, if we can get it working, well, bonus. I mean, for 30 bucks, jeez. It's probably got 30 bucks worth of parts in it easy. And this is actually a modular configurable power supply not by the user I don't believe but you can actually order it in either a single output channel, dual output channel or triple output channel like this one here is and you can see why they sold a unit

**Dave Jones:** which is only this wide the 2812. They just make the case a bit shorter and they've only got the single output channel here. So, this is fully populated with the three output channels.

**Dave Jones:** And the good thing if you're buying like you know, like maybe a parts unit on eBay for example, like sold as non-working, then it's good to get modular stuff like this because well, we've got three identical bottom boards like this.

**Dave Jones:** We've got two identical top boards which look like I don't know, the ADC board or some sort of processing type board. And it looks well, we're supposed to have three identical boards on there, but obviously this board here looks physically different to these two, but at least we have two.

**Dave Jones:** And it means that we can swap these boards over. So, we can swap the base boards over. So, I'd be surprised if out of all these, we don't get at least one functional channel out of the thing.

**Dave Jones:** I'm just by you know, swapping boards. I'd be quite surprised if like you know, there's a fault on every single one of these channels. So, I'm not even sure if it's faulty at all.

**Dave Jones:** It may just power up and work just fine. So, having a modular type system like this very handy, especially if you haven't got the service manual for the thing.

**Dave Jones:** But thankfully, we do have the service manual for this. And it does have the schematics for almost all of the boards, but curiously, it doesn't have the schematic for this mains power supply here.

**Dave Jones:** And this is actually our first issue. Now, if we take a look at the back panel here, interestingly, this third channel here which has the boards in it obviously is not populated.

**Dave Jones:** So, I don't know why. Well, there is with that one missing board up the back here we saw, but like I don't see the function of having why you would need that board any boards in there populated at all if you weren't going to have the connector on the back.

**Dave Jones:** I mean, we can just solder a connector on there as we'll see soon. There's a room to solder one of these terminal block connectors on the back. But anyway, very very strange GPIB interface of course.

**Dave Jones:** Interestingly, three little what look like SMB Uh, tiny coax is down here for ready start and step. So, some sort of programmable thing. Actually, I just realized this why this board is different to this one here and this other one over here.

**Dave Jones:** Look, they've actually got a plate on here 60 volts 10 amp. So, this is 120 watt. This unit is capable of 180 watts total across all three channels like this.

**Dave Jones:** So, we've got a 30 volt 10 amp 60 watt unit over here. 60 volt 10 amp by the looks of it. I assume that, you know, when they configure this thing at the factory, they would have put the correct plate on there.

**Dave Jones:** It needs both of those boards. Maybe they're 30 volts each and it needs both of them to give a combined 60 watt 60 volt output. I should have thought of this before I started recording.

**Dave Jones:** Anyway, it's just dawned on me why they've got that extra board in there, I suspect. And that actually makes sense if you have a look at the ribbon cable.

**Dave Jones:** They've actually got like a daisy chain ribbon cables. There's quite a few daisy chained ones in it like cables in here and they deliberately haven't put an extra one there.

**Dave Jones:** So, obviously, it wasn't designed to have three channels, but I think that's why this is actually, I believe, a fully populated one that has 180 watts total output, but these two boards combined give a total 60 volts output.

**Dave Jones:** And yeah, bingo, that makes sense down in here, too. They've strapped these two boards together. There you go. There's some spade lugs on there and the output voltage is down in here strapped together like that.

**Dave Jones:** Not in parallel, but they're putting them in series. Anyway, before I got sidetracked there, the thing I wanted to show you is that yes, it is 110 and 220 volts capable.

**Dave Jones:** Supposedly, it gives you the different ratings on there, but it looks like it's factory configured to 115 volts. So, let's have a look inside. Now, if you have a look at this mains switch mode board here.

**Dave Jones:** Look at this. There's a jumper link in there, 110 volts and 220 volts. Thank you very much. So, you'd think, "Aha, you just swap that over to 220 volts there." But, let's have a look at these caps.

**Dave Jones:** Now, these are very nice Nichicon caps. Spared no expense there. Well, actually, um these are only 85° C rated, which is a bit unusual. Why they didn't use 105°?

**Dave Jones:** I have no idea. Anyway, um 680 microfarads each. But, this is why I was a bit cautious about thinking that I can just change that jumper over and, you know, she'll be right.

**Dave Jones:** Now, these are only 200 working volts. And if you're going to put this up to 240 volts, well, that's not good enough if these are in parallel, for example.

**Dave Jones:** And same for these ones here. These are Nippon Chemicon. Why they didn't use the same brand, I'm not entirely sure. Anyway, uh 200 uh and 50 volts. And if these are wired in parallel on the board, then what?

**Dave Jones:** That's going to ruin your day. So, I'm thinking that there is certainly a distinct possibility that this board, while it does have that jumper on there, uh it may not It may just be that they uh supply the board for 110 volts and use lower rated caps in here.

**Dave Jones:** Because that's only a single wire jumping over. It's not like you can easily configure in series and parallel combination on those caps. So, huh, I'm just I want to get this board out and check what this jumper is actually doing before I just whack it over there uh to 240 volts and and shove it in.

**Dave Jones:** I don't want to blow the ass out of these caps. That'll ruin your day. Um interestingly, they've got a uh nice big-ass uh heatsink just flapping around in the breeze there on top of that uh diode bridge under there.

**Dave Jones:** Thing I really like about this is that they've got these uh sliders in here, these sliding support posts. You can just look, slide those across like that and then they just pop out.

**Dave Jones:** Boom. Well, close to it anyway. I probably should have taken the cables off first, but yeah, they just pop out. Very nice. We've actually got a manufactured date code on this.

**Dave Jones:** 1996. There you go for the board. Hey, got to love the tin copper traces there for increasing the current handling. Yes, it does actually have solder mask up the top for the signal type stuff, but they're trying to increase their capacity there anyway.

**Dave Jones:** My hunch paid off because this here is the 240 V terminal and there's no trace connected to there at all and there's no trace on the top either. It goes absolutely nowhere.

**Dave Jones:** So, if I plug that into 240 V, well, thankfully, it wouldn't have blown up. It just wouldn't have done anything at all. So, this board is specifically laid out for 110 V.

**Dave Jones:** Bummer. So, uh that's all right. I do have a 110 V transformer here, so I can get it up and running, but you know, I don't want to use that all the time if I had to use this thing.

**Dave Jones:** So, that's a bit of a shame. So, I'm not sure what I'm going to do. Anyway, let's continue, shall we? Um this board here, even if you didn't have the you know, the service manual or configuration manual or anything like that for it, it's obvious what they're doing here.

**Dave Jones:** Now, it's got like DS and MS over here. That could be like, you know, data selector. Some sort of selection thing. They've actually got all these pads along here and this one over here, they're bridging just solder bridge those two.

**Dave Jones:** Bit of a bodgy thing, but you know, it's not that uncommon. And this one over here is on the second position there. So, obviously, if you had a third board over here and had an identical board, you would have a third address there.

**Dave Jones:** And when the processor talks to the board and it tells it, "Okay, I want to set channel one." It knows this is channel one because that's got the address there.

**Dave Jones:** That's almost certainly what that has to be. So, for troubleshooting purposes, if you had to swap these two boards, then of course you'd have to change that jumper if you want to move this one over here.

**Dave Jones:** You just move that jumper link over. And as it turns out, this is the digital to analog and analog to digital board. Has its own microprocessor on there. How do I know that without even taking it out?

**Dave Jones:** Well, I do have the service manual here complete with the schematics. I'll link it in down below. And as you can see, we were right on the money with the selection line there.

**Dave Jones:** There's the MS thing. I've got no idea what master select or something like that, perhaps. But yeah, this is for selecting the different channels, obviously. And we've got some serial data galvanic isolation here with on the transmit and reset lines.

**Dave Jones:** And if we go over here and have a look at the rest of it, tada! It's an 80 C31. They've got their own processor on there just to handle the analog to digital and digital to analog.

**Dave Jones:** The reason that they do that is this is an old school design, probably dates back to the early '80s. Got its own E-squared PROM and its own EPROM, by the way.

**Dave Jones:** It's not a microcontroller, it's a microprocessor. So, it needs that external 27C256. Fantastic. And here we go. These are our We've got our DACs here. And this 7528 here, this is only a lowly 8-bit DAC.

**Dave Jones:** So, I'm presuming that might be for maybe a coarser current set resolution, uh for example. And this DAC 8248 here, this is actually a dual 12-bit DAC. So, this is used for our voltage output control.

**Dave Jones:** Get decent resolution with 12 bits. Now, I pulled the board out here and this is rather interesting. Look at this. We've actually got two uh Analog Devices DAC 4248.

**Dave Jones:** So, this is different to the schematic. So, maybe they've Yeah, they've upgraded it from the 8-bit to to the 12-bit resolution from uh since that whatever version service manual I've got.

**Dave Jones:** You can certainly see that here. There we go. Look, physically smaller chip here for N302. And they've Yeah, so they've upgraded that. Interesting. Now, the interesting thing about this board is that even though I've got two DACs on here, you won't find any reference.

**Dave Jones:** I mean, you'll find some, you know, nice precision uh op-amps, OP200s, and the rest, but there's no voltage reference whatsoever. So, but you go over to this other board, which we saw has the We saw this one is actually slightly different to the other two.

**Dave Jones:** So, double-sided load here, which is really interesting through all on the top and then a whole bunch of surface mount on the bottom. And bingo, we're going to find another precision op-amp, but take a look down here.

**Dave Jones:** Woohoo! There it is. Ref02 with a nice 10-turn trimmer in there. Now, we can actually get down and see the main power supply board. That's the stuff that does all the magic, none of this digital 8031 microprocessor rubbish.

**Dave Jones:** And it's got a mounting plate {slash} heatsink. That's effectively what it is. They've got a seal big seal pad on the bottom like that to isolate that. And they've got These look like the output power transistors here.

**Dave Jones:** Um so, yeah, it thing's going to be reasonably uh efficient because this thing like it's obviously a switcher. Look at this huge transformer we've got here. So, we're going to have some output switching.

**Dave Jones:** That's how you can get, you know, 60 W per module into one of these. If you had like a 60 W linear supply or a 180 W linear supply total, well, you need a big thumping transformer and all the rest of it.

**Dave Jones:** So, we've got ourselves an output switching regulator. Uh I guess the only thing I don't like is that uh the main output uh filter caps here all underneath the heat sink.

**Dave Jones:** Yeah, that's not terrific, but we do have uh air flow from the fans at the back. So, I don't mind the system configuration of this thing at all. As I said, they've got this uh daisy chain data cable coming over here like this, and this just runs in parallel between all the boards, and it has different selection lines.

**Dave Jones:** So, the data's going to be the same, obviously. It can't can't send uh 8-bit data, but it's obviously sending serial uh data across. It's saying, "You know, please set the voltage and read back as well." So, it's doing that serially, and then we've got our main voltage output here, and it just has another daisy chain cable, and you can plug it in if you've only selling a single output

**Dave Jones:** module in this size case, you just don't populate both of these. Or in this case, we've got a 60-V uh option, I believe. I think it might even be able to go to higher uh voltages.

**Dave Jones:** Maybe you can uh cascade to 120-V uh total by putting the three uh sorry, 90-V total putting the three in series. So, they're obviously putting two 30-V modules in here to give you a 60-V output uh capability wiring them in series.

**Dave Jones:** And then they've got that just daisy chained up the top here. Once as I said before, showing that wired in, and hence why they've only got the single output wired in here.

**Dave Jones:** So, it is quite configurable from a customer point of view. You just order it, and they just, you know, easily make this thing to whatever uh requirements possible. And as I said, they put a different board over here if you want the 240-V option you're selling in different markets around the world.

**Dave Jones:** So, really is nicely configurable. And from our point of view, for buying these sorts of things on eBay, it's fantastic because we have these modular boards. I have no doubt that this bottom board is identical between all three.

**Dave Jones:** Absolutely no doubt whatsoever. These boards are identical over here. Uh these boards are the same apart from the address selection and things like that. So, you know, we can just swap things around and hopefully get at least one of them working.

**Dave Jones:** And these vertical riser boards here, you know, with the surface mount stuff on it, no surprises whatsoever. These uh companies like this, they're not, you know, building a million of these things.

**Dave Jones:** They're not going to re-spin the board because they want to should change some parts or uh something like that. You know, they're going to and upgrade the models between, you know, from previous generations and things like that.

**Dave Jones:** It's going to say, "Oh, yeah, let's just whack in a modern, you know, surface mount board in here. Everything else completely through hole. We'll just keep that. It works a treat.

**Dave Jones:** Why redo it? So, we'll whack in a little uh surface mount control board." And what do we got there? I can barely read that on the screen. I think it's some uh 4,000 series CMOS stuff.

**Dave Jones:** Beauty. And you'll notice on the backside of that board there, look, they've got a resistor mounted on some standoffs. And I'll show you a few more examples of that in here as well.

**Dave Jones:** Obviously, a select on test resistor. And they've got another one of those right down in there as well. And also another one right up near our output there. And of course, these things are designed, as I said, either select on test or some sort of like uh you know, product uh configuration after the fact.

**Dave Jones:** So, this allows them to do uh some sort of uh product uh configuration and or trimming after they've actually had the boards manufactured. It's easy way to do it.

**Dave Jones:** You just solder the post in there and then someone can come along on their production line uh test jig and then just go, "Right, we need this model this week.

**Dave Jones:** Well, let's put that resistor in there." And you'll notice that this middle board here, aha, screw missing down there. Someone's had a go at this puppy. And it's interesting to note the tiny little ferrite bead around our negative sense line there.

**Dave Jones:** Not around the positive sense line. No, thank you. Just around the negative. Taken the edge off something there. So, there's only one thing left to do, power this thing up.

**Dave Jones:** I've actually disconnected these two internal boards like this, so they're not actually connected. I'm going to uh bet on this uh channel over here being the winner considering that this one looks like it's been disturbed within some way.

**Dave Jones:** So, I've got my 110 V transformer. So, let's uh switch this on and fingers crossed. Fan going. Initializing. Can't see it, but there it is. Processor's working. Beautiful. Initializing.

**Dave Jones:** Geez, it's taking a long time to initialize. That's for sure. Wow. Come on. There's no smoke escaping, but uh error 1 1. What the to the manual. But actually, I just cleared that.

**Dave Jones:** I just and I've got my voltage and my current made in here set in here. V set 1 V. What? I just press my select button and it just reinitialized there.

**Dave Jones:** So, maybe you should uh maybe we might have to reset the processor. Maybe it's all like it's configured for that second board and it's looking for that second board and it doesn't like it.

**Dave Jones:** That would be a reasonable initial guess. Anyway, not the most user-friendly thing to use of course. Um but yeah, I mean, geez, if you can pick it up for the 30 bucks like I did and at least get one operational channel, it's an absolute bargain.

**Dave Jones:** And sure enough, I looked at the reference manual and it lists all the error messages of course and that error 1 1, this is the source of the error in this case.

**Dave Jones:** It comes from the output and this one is a well, it's a summation of all the error codes in decimal, but basically what that translates to is yes, it's the output channel is not responding.

**Dave Jones:** So, yeah, probably no wonder because I haven't plugged in um that second 60-V channel. So, that's probably it. It's already hard-coded in the firmware to uh to be configured as this particular type of output model.

**Dave Jones:** So, it's just not seeing the board. Bingo. So, yeah, let's plug it in. By the way, I just noticed under this heatsink, there's our current shunt. There we go.

**Dave Jones:** It's not a four-terminal job, but uh they would be uh tapping that off somewhere, I'm sure. They've actually got three extra caps right under that heatsink in there. Geez, they could have done a bit better than that, I think.

**Dave Jones:** And of course, just before I uh put this back on and power up this channel here, you just go over visually and check for you know, any leaking caps, any blow holes in parts, any burnt resistors or or diodes or anything else.

**Dave Jones:** So, you know, just give it the what for. The fuses are intact, so it obviously hasn't been uh overloaded in any way. They look like the original ones. And yeah, so it should be okay to power up.

**Dave Jones:** All right, let's see if we get same thing. Initializing. Come on. You can do it. Uh error 2 1. Let's find out what that one is. Actually, I got that wrong last time.

**Dave Jones:** What it is is uh that it 2 1 is now now no output response from channel 2. That's what it means. So, this before we're getting no output response from channel 1, which was interesting because well, we have channel 1 and now um unless there's more than one error, which I don't know how to look at, um then Yeah, oh, one.

**Dave Jones:** Okay, one is enabled. So, does now does one now work? Let's have a look. V set 1 V. Okay, so now it just comes down to a PEBCAK thing and uh I'm not using it correctly cuz it it went into standby mode and well, that is standby, right?

**Dave Jones:** There is no power switch on this thing. It just always runs. It's a system power supply. So, that's what it's doing. Enabled one and then we can uh the uh well, actually channel one select.

**Dave Jones:** Hello. No, we don't want that. There we go. And we set it for one one volt. What do we get? Ta-da! One volt on the output. Winner winner chicken dinner.

**Dave Jones:** Bloody beauty. Okay, just a quick check of the other voltages. Let's say five volts. So, V set five enter. Beauty. 10 Winner winner. 20 Whoa! Whoa! Whoa! What happened there?

**Dave Jones:** Holy hit job. Whoa! It doesn't like that. That's one sick puppy. Aha! I think it might be a trap for young players there. Let's go into our current output.

**Dave Jones:** Ta-da! Our current set is very low. So, obviously uh like excess leakage at the higher voltage and that's what it's doing there. That's why it's um throttling back. So, even um output uh current protection enable disable.

**Dave Jones:** It doesn't matter if we've got it disabled. So, let's set that. I set to an amp. There we go. Excuse my hand in the way there. There we go.

**Dave Jones:** So, now our current output is set to an amp and our voltage there we go. Now, if we set this V set 10 no dramas whatsoever. Here we go.

**Dave Jones:** 20 It'll work now. Yeah, there we go. Trap for young players. Go all the way with LBJ. Go to 30. Beauty. Winner. So, I have to test it under load, of course.

**Dave Jones:** Get out my electronic load, but you know, I have little doubt it's going to work, I think, channel one. But, the problem is, look, um we can't select uh channel two cuz we got that error message when we boot it up, so that's understandable.

**Dave Jones:** It's not talking to channel two, hence why they were getting the boards, you know, maybe using this as a part unit or something. It looks like channel two has failed in some way, shape, or form.

**Dave Jones:** Okay, how many of you saw that and were screaming at the screen because I didn't plug this in. I'm not sure if you noticed that, but I just noticed that.

**Dave Jones:** Oh, of course channel bloody two's not going to work if I don't plug in the damn data cable. Oh, oh, let's try that one more time, shall we? Here we go.

**Dave Jones:** Initializing. Come on. Woohoo! Look at that. Select. Can we select channel two? Look at that. We're in like Flynn. Beautiful. Now select channel two. Uh well, let's get the hell out of standby.

**Dave Jones:** Oh, no. No, we disabled our bloody thing. These system power supplies pain in the butt. Enable. Yeah, enable number two. There we go. Ah, now we're talking. The Yeah, I set it to a volt.

**Dave Jones:** And is it? What? It's a little bit jumpy. Yeah, it's a little bit jumpy. Oh, maybe we've got our um duh. Yep, let's try that. Let's set that to an amp.

**Dave Jones:** And no, it's still a Uh it's still a bit jumpy. Don't like that. I think we have an issue on channel two there. Hmm, Mhm, of a stability problem, but not at 10 volts.

**Dave Jones:** Looks uh rock solid at 10. And let's go all the way with LBJ again, right up to 60. Oh, it's taking a while to ramp up. Oh, look at the current.

**Dave Jones:** Oh, some sort of No, what's going on there? Yeah, don't like that. So, this is interesting now. What I've done is changed the current limit from 1 amp down to 0.1 amp.

**Dave Jones:** And it seems to be working reasonably well. So, I can uh pretty much set it to uh anything. It's uh It's the output capacitance has got to discharge there.

**Dave Jones:** There's no load. Which is fair enough, I guess. Um but although this is a two-quadrant uh supply, so you'd think it would be able to sink that back down.

**Dave Jones:** Um instantly, but anyway, um yeah, let's I don't know about the architecture of it uh as such, but yeah, I mean, I was up to I was able to go up to 40 volts there before.

**Dave Jones:** Haven't got any higher than that, but uh it's jumping around. It's nice and stable. Let's go up to 50. Yeah, no worries. Let's go up to 60, which is its maximum output capability.

**Dave Jones:** What? Can't do 60. But uh that's all right. Maybe there's some, you know, there is some uh performance limit. Maybe it doesn't actually reach its claimed. So, although there's no load, so it should.

**Dave Jones:** So, it's not like it's, you know, because there is like a wattage uh limit, so there's like a performance envelope for these um uh power supplies or where they won't deliver, of course, the maximum uh voltage at the maximum current, for example, but anyway, it's going up to 50, and well, mhm, I've got my BK Precision Electronic Load uh set up over there.

**Dave Jones:** Sorry, it's uh not easy to get both of these in the same shot here. Uh Um and there we go. I'm drawing 0.1 amps constant current at 30 volts.

**Dave Jones:** It goes over voltage on there if I go any like if I go up to 40 volts, it doesn't like that at all. So, it's everything's hunky-dory, nice and stable on the second channel at you know, 0.1 amps, no problems.

**Dave Jones:** So, I've actually set 1.1 amps on there now and I'm drawing 1 amp at 10 volts. So, 10 watts and it's nice and stable, no problems whatsoever. Yep. So, I don't know what was going on before.

**Dave Jones:** Hmm. By the way, I forgot to show you the processor board on the bottom. We've got ourselves a Panasonic lithium battery in there. Don't know how long that puppy's been in there, but uh looks sort of factory original kind of, but let's let's measure that's not leaking.

**Dave Jones:** So, let's try it out. And 3.3, no worries at all. Although, you know, if you're going to put this back into service, if it is the original one, you'd you know, you'd just change it as a matter of course probably.

**Dave Jones:** Because we are talking 95 vintage board there. So, yeah. That's our version number 2705 two. And let's check out the processor. Aha, we've got ourselves an Intel 88C196. That's part of the MCS-96 family microcontrollers and uh yeah, pretty old school, you know, well discontinued now, but hey, you know, these were very common back in sort of you know, industrial controllers and then automotive stuff and things like

**Dave Jones:** that back in the day. So, the only thing left for this apart from a cover is the spaces to hold this puppy in. I think I might know where I can find some.

**Dave Jones:** Surely somewhere in here I've got I'm looking for. Hmm, I just have to find it. Only 330 tins. Hmm, where's Wally? Can you see him? More bloody couch feet.

**Dave Jones:** Never know when you might need EHT stand-off rings. Bloody bet your ass. Look at those. Damn handy. More couch feet. That's just nuts. More couch feet. I swear I'm not doing the same one.

**Dave Jones:** I'm going through them. More. Nope. Nope. And nope. And again, you guessed it. Nope. Wow, check it out. I might have actually found a new packet of little miniature screws and nuts.

**Dave Jones:** Check it out. Wow, nice. All right, pivot spaces. Not what I want though, but neat. Surely I can find the spacer I want out of all these. Wally's in there somewhere, surely.

**Dave Jones:** I think I'll call that one a win. What do you think? Awesome. Look at that. And surely I can find my matching self-tapper in that lot. Actually, the one on the left there might do the business.

**Dave Jones:** Shame I've only got one of them. Hmm. And I found the three on the right there, the original ones on the left, and well, that ain't too shabby at all.

**Dave Jones:** She'll be right. And I didn't even have to resort to bodging in just regular metal threaded ones instead of self-tappers because, well, yeah, I got a few of those.

**Dave Jones:** Oh, black ones. Ooh. Well, I'm walking back from the bunker. Scored my parts. Think I got a reasonable match, but it was light when I walked there, and now I'm walking back, it's dark, it's raining.

**Dave Jones:** But I scored my parts. Was it worth holding all those parts to get these? Hmm, what's the moral of story? I'll let you figure it out. So, there you have it.

**Dave Jones:** That's the Fluke PM 2800 series, more specifically the 2812. And it's quite a nice unit. Looks like I've scored a winner here for 30 bucks. I need to do some more performance testing on it.

**Dave Jones:** Got to install my screws that I just got and spacers and stuff. Put it all back together. Got to build a case for it. If you got any good ideas for building a case, I'm not thinking, you know, like a sheet metal folded metal case or something like that.

**Dave Jones:** I'm thinking maybe a nice wooden case to for this puppy to go into. What do you think? Hmm, got any good ideas? Let me know. Anyway, I thought that this thing would be faulty in some way, shape, or form.

**Dave Jones:** Initial impressions is it looks like it actually works. I'm not sure what happened to the intermittent thing on this second channel. Could have been like a loose sense connection at the back or something.

**Dave Jones:** I'm not entirely sure. Have to do some more performance testing, but it seems pretty good. I expected to have to swap whop some of these boards. And this is one of the holy grails of uh of buying stuff on eBay and repairing things like this.

**Dave Jones:** Even if you can't get the schematic, if you got modular based ones like this, you can swap boards. You got to know a good board. You can compare parts with.

**Dave Jones:** You don't necessarily need a schematic even if you had a faulty board. So, you know, I was expecting to have to fix this, but I didn't. But even if I had to, it doesn't matter.

**Dave Jones:** Turns out the schematics for this, I've only got the schematics for the top board and the processor board. That's it. Don't have the schematics for the back board here.

**Dave Jones:** So, the analog to digital, digital analog, I've got the schematic for that. Don't have the schematic for that. It's not in the service manual, nor the power supply, nor the actual switch mode power supply base board itself.

**Dave Jones:** What a bummer. So, if anyone's got those schematics, please link them in. But the service manual I got doesn't have them, I'm afraid. So, anyway, um, these are uh quite a reasonable uh power supply.

**Dave Jones:** If you want to have a look at these on eBay, there's a 2811 going at the moment, which is the small one here, single output, for like 150 bucks, fully working.

**Dave Jones:** It's like, you know, bargain, if you can score one. But yeah, 30 bucks, winner winner chicken dinner. And some people might be wondering, can we put binding posts on the front here, just like we did for those uh HP/um Agilent supplies, not this Keysight rubbish.

**Dave Jones:** Can we do it on these? Well, yeah, there's nothing stopping you, but they don't have It looks like it's not a stand It's not an option at all on these models to put front panel binding posts.

**Dave Jones:** These are system power supplies, designed to be used you know, bolted into racks, screw terminals at the back, and you know, most likely uh PC controlled via GPIB. The front panel is just for kicks, you know, so yeah, really I mean, but there's nothing stopping you.

**Dave Jones:** You could actually, you know, drill out these front panels. There's enough room there to actually put them in. So, if you're really keen, it's a really thick front panel.

**Dave Jones:** You could You could do it if you were, you know, really keen, but uh the front panel might look a bit messy, because this back You'd have to have a mount, maybe a mounting plate on the front or or something.

**Dave Jones:** Heck, the plastic's maybe even strong enough like if you had a metal backing plate or something like that, you can mount the binding post on there, and then just drill a few holes in here for the wires to go through.

**Dave Jones:** That might work. It's doable. So, that was yet another hopeful repair video. Just popped like an eBay, and well, this bloody thing works. Unbelievable. Can't cop a break. Was hoping to get something reasonably faulty, so that we could do a repair video on it, but no No such luck.

**Dave Jones:** Murphy gets me every time. It's either fully working like this, or apparently fully working, or it's just beyond economical repair. And so, anyway, we got what we got. If you liked that video, please give it a big thumbs up on YouTube cuz that always helps a lot.

**Dave Jones:** The other direction thumb, you know what I'm talking about. You want to discuss it. Links down below. All that sort of jazz. Catch you next time.
