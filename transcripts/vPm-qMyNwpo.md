---
video_id: vPm-qMyNwpo
title: EEVBlog #543 - PCB VIA Current Investigation
url: https://www.youtube.com/watch?v=vPm-qMyNwpo
source: youtube-asr
timestamps: {"0": 1, "1": 18, "2": 39, "3": 58, "4": 70, "5": 81, "6": 106, "7": 119, "8": 131, "9": 143, "10": 151, "11": 171, "12": 185, "13": 194, "14": 209, "15": 225, "16": 240, "17": 260, "18": 284, "19": 295, "20": 312, "21": 341, "22": 361, "23": 373, "24": 389, "25": 414, "26": 429, "27": 441, "28": 458, "29": 479, "30": 491, "31": 503, "32": 523, "33": 536, "34": 553, "35": 562, "36": 573, "37": 587, "38": 604, "39": 621, "40": 632, "41": 645, "42": 660, "43": 674, "44": 689, "45": 697, "46": 709, "47": 724, "48": 736, "49": 745, "50": 771, "51": 783, "52": 795, "53": 805, "54": 823, "55": 837, "56": 846, "57": 854, "58": 868, "59": 881, "60": 892, "61": 904, "62": 915, "63": 928, "64": 940, "65": 947, "66": 956, "67": 966, "68": 979, "69": 990, "70": 1002, "71": 1015, "72": 1027, "73": 1038, "74": 1047, "75": 1060, "76": 1076, "77": 1093, "78": 1107, "79": 1115, "80": 1126, "81": 1138, "82": 1145, "83": 1155, "84": 1167, "85": 1181, "86": 1193, "87": 1209, "88": 1228, "89": 1250, "90": 1258, "91": 1265, "92": 1274, "93": 1281, "94": 1295, "95": 1306, "96": 1319, "97": 1346, "98": 1357, "99": 1371, "100": 1380, "101": 1391, "102": 1407, "103": 1416, "104": 1430, "105": 1440, "106": 1451, "107": 1461, "108": 1474, "109": 1497, "110": 1507, "111": 1518, "112": 1532, "113": 1551, "114": 1566, "115": 1588, "116": 1610, "117": 1626, "118": 1636, "119": 1650}
---

**Dave Jones:** Hi, this video comes about because of a post that Simon, one of the EEVblog forum moderators, made on the forum asking a question of what is the typical plating thickness of a PCB via and that led on to how much current you can put through and stuff like that.

**Dave Jones:** And it's an interesting question and as it so happens, my little micro ruler actually has a handy little table on it, a very small one for the via amps for a typical 1 mil plated via for various temperature rises versus the via diameter.

**Dave Jones:** And that's the answer. Rough rule of thumb is that a typical PCB via is going to be about 1 mil thickness. That's 1 mil as in 1 thou, it's not 1 mm, 1 thousandth of an inch or around about 0.025 mm thickness.

**Dave Jones:** And but it's going to vary a lot depending on the manufacturing, the manufacturer, the manufacturing process and the manufacturing tolerances, but you know, that's a rough rule of thumb.

**Dave Jones:** And I've always taken as a PCB designer a nice safe value for how much an individual via can carry one single via is rough rule of thumb about 0.5 amps.

**Dave Jones:** So, if you want a trace to go from one side of the board to the other side of the board, it's got to carry 2 amps, you typically put at least four vias in there to be on the safe side, but it's a very interesting question and it also brings up the question of can you just plug or fill the via with solder to increase the current carrying

**Dave Jones:** capacity. And well, this comes back to the videos which I'll link in down below that both Mike from Mike's Electric Stuff and I have done on proving that uh solder PCB traces does actually make a difference.

**Dave Jones:** Not a huge difference, but it does make, you know, a a significant difference to the uh in decreasing the resistance of a PCB trace. And I was wondering, is that the same for a via?

**Dave Jones:** So, I thought I'd actually try it and also uh get out the uh via calculator and plot some graphs and do that. And well, don't know what we're going to get.

**Dave Jones:** Could be interesting. So, let's have a quick look at it. So, the first thing I'm going to do is use one of these uh calculators. This one is uh an awesome one.

**Dave Jones:** If you haven't got it, you definitely should get it. It's the Saturn PCB uh uh toolkit calculator. And uh it has all sorts of, you know, stuff. I'm sure I've shown this on the uh blog before, but if we go into uh uh via properties here, then we can actually set uh multi-layer boards, micro vias like this.

**Dave Jones:** But, uh what we want is the two-layer board, standard uh 1. uh 6 mm thickness. It gives you the 1.575. And then we can set our hole diameter like this.

**Dave Jones:** And then our plating thickness, we've got set to a, you know, sort of a rough standard uh 1 mil. That's the default thing, which is 1 mil, of course.

**Dave Jones:** Um 1 thou, which is 0.0254 mm plating thickness. And then down here, say for a 1 mm diameter hole, it uh we can solve that. And then it gives us the via current down here, 1.12 amps.

**Dave Jones:** And the uh via resistance as well, uh 0.33 mΩ. We don't care about the inductance and that stuff like that cuz we're only dealing with uh DC here. And then, of course, um you can calculate from the resistance and the current, you can calculate the power, of course.

**Dave Jones:** And uh it gives you the cross-sectional area. And it gives you the thermal resistance down here and the voltage drop and you know, uh it's really quite nice, but that is for a 1° C temperature rise and that's the thing.

**Dave Jones:** Uh when you're designing a board like this, you have to determine what is your acceptable temperature rise in that copper PCB trace usually or in this case the uh via, which is basically exactly the same except it has a less controlled manufacturing process than a uh a regular trace on a PCB.

**Dave Jones:** And uh you know, a default value might be a temperature rise of uh 10° C, but you know, quite frankly, when I'm designing boards, you know, belt and braces type stuff, I don't want to piss away 10° C all that power in my uh traces unless I'm doing it real high power stuff right on the edge and you know, I'm at the physical limits of how big I can make traces and

**Dave Jones:** stuff like that, then I'm going to set that temperature rise for 1° C cuz I'm basically, you know, very conservative. I don't want uh you know, almost any power at all dissipated in the via.

**Dave Jones:** Like for example, here we go. We've got 0.4 for a 1 mm diameter hole, 1° C temperature rise, we've got 0.4 mW there dissipated in our via. Fine, if we set that order of magnitude bigger to 10° C temperature rise, look at that, 4 mW.

**Dave Jones:** God, you can fly halfway to the moon on 4 mW. You've got to be kidding me. So, um what I'm going to do is uh well, what I have done is uh done uh all these values, uh whole diameter starting at uh 0.1 mm all the way up to 2 mm for two different temperature rises, 1° C and 5° C like that, and I've gotten the values out of this and tada,

**Dave Jones:** I've plotted them in a spreadsheet here and this is the graph we get. It's very interesting. Check it out. It's a four as I said for the one mil plating, the one thou plating of your via, which is going to be fairly typical, but it's going to vary a lot depending on the manufacturing process.

**Dave Jones:** And that's the thing with these vias. This is just going to be rough rule of thumb stuff. And does our rough rule of thumb that I've known of, you know, roughly 0.5 amps per via to be on the safe side.

**Dave Jones:** And well, let's have a look here on the vertical axis on the left-hand vertical axis, I've got the uh the calculated current capacity which the tool kit told me here, and that's from 0 to 4 amps up here.

**Dave Jones:** And on the right-hand vertical axis, we've got the via DC resistance in milliohms. So, these two traces here correspond to the uh via DC resistance. And these two traces, this one this series here and this one here, uh for as you can see, the red is for the 1° C temperature rise there, and the green is for the 5° C temperature rise.

**Dave Jones:** And it's a very interesting result. And check it out, it's basically linear um for the current capacity versus hole diameter there. But they are a couple of little kinks.

**Dave Jones:** You can see a a like, you know, little kinks in there. It's not it's not absolutely completely linear. So, I don't know where the Saturn PCB calculator is getting its uh how it's actually doing its calculations.

**Dave Jones:** It's obviously getting it from the IPC-2221 standard somewhere and taking into account thermal um you know, properties of copper and all sorts of stuff like that. So, I'm not exactly sure why we're getting that kink there at 1.6 um 1.5 1.6 amps.

**Dave Jones:** It drops back down and then continues up. And I've got that the same is for the 1° C temperature rise and the 5° C temperature rise. Now, you'll notice that the slope of the 1° C uh temperature rise one here is of course lower than the 5° C temperature rise.

**Dave Jones:** And if you have found And if you plotted 10° C, you'd probably get a steeper uh ramp there yet again. So, I haven't plotted that one in. I don't know where it would actually end.

**Dave Jones:** But, there you go. You can see it's effectively pretty linear with or it appears to be um according to the calculations that the Saturn PCB calculator is using, fairly linear with respect to hole diameter.

**Dave Jones:** So, you double your hole diameter, roughly double your current capacity here. Now, do we get our rough 0.5 amp uh rule of thumb? Well, let's take the 1° C temperature rise, which is, you know, if you're going to design your board, why have it for 5 or 10° C temperature rise in your copper?

**Dave Jones:** That's just stupid. So, one is a good figure which I always uh tend to use unless um otherwise. And look, here it is. I mean, the smallest uh diameter you're going to be using on a standard drilled diameter on a standard board is about 0.3 mm.

**Dave Jones:** That's sort of one of my standard uh via small via uh hole sizes. And you know, it There it is. You know, we're roughly getting, you know, 0.6, 0.7, maybe uh current capacity for one of those vias.

**Dave Jones:** So, that's That rule of thumb pretty much holds true. That rough, to be on the conservative side, not anything under this curve, 0.5 is under that curve for all diameters.

**Dave Jones:** So, really, yeah, that's confirmed. And if you have a look at the uh via DC resistance here, you can see that it's not a linear uh curve as you'd expect.

**Dave Jones:** That is in up right tails up right drastically right at the bottom end sort of you know under that 0.5 mm it really starts to tail up like that fairly drastically.

**Dave Jones:** So, there's not a direct linear correlation there between the current capacity and the DC resistance of the via. So, that is certainly a very interesting graph and it would be fascinating to get some graphs of some other calculators as well.

**Dave Jones:** I mean this is just the Saturn PCB calculator specifically and I'm sure it's going to vary depending on the type of calculator and what calculation it's using to estimate that current capacity but I think this one's probably not a bad rule of thumb at all.

**Dave Jones:** I rather like it. All right, well let's do a practical test and see if we can actually measure a difference on a typical via or hole on a PC pad hole on a PCB.

**Dave Jones:** There is no difference practical difference between a via and a pad. They're just used for different things really but they're essentially they're constructed exactly the same way on a blank PCB.

**Dave Jones:** So, we don't necessarily have to use an actual via. We can use a component pad which is exactly what we're going to do here and we see if we can measure a difference in the resistance of this via after we actually plated through.

**Dave Jones:** Now, I'm not going to pick one at random here cuz we may actually need a special case and I found a board we need a four terminal measurement because I'm going to be passing current through the via and I don't want it to go anywhere else.

**Dave Jones:** I want all the current to flow through a via and then we want to be able to tap off voltages. So, I run me through some old boards and it was actually quite difficult to find a board with exactly the configuration of tracks which I needed which is this.

**Dave Jones:** This pad here is the one that we're going to actually target And I'm going to feed the current in here, and it goes down there, and it can go nowhere else because this trace is open down here.

**Dave Jones:** It can go nowhere else but through that via or pad there, and then out this side. So, that's it. And the good thing is it's got two tap points.

**Dave Jones:** They're all sense points directly on there. So, I can attach a wire to here, and it will sense the voltage on that surface of the pad there, and I can also attach a wire to here, and that will sense the voltage directly at that pad there.

**Dave Jones:** So, that should be pretty good. So, we're going to use a four-terminal resistance measurement, but we're not going to use, of course, the four-terminal measurement on our bench multimeter cuz it only measures at one current.

**Dave Jones:** We want to measure a much higher current. So, I'll I'll show you the test set up in a minute. But this one should work quite well. And this is Yes, this is a solder-coated board.

**Dave Jones:** So, those vias are actually plated through and solder-coated. So, they're not bare copper, and they're not gold. So, if you wanted to do this methodically, you would try this with not only different size vias and holes, but for each type as well for bare copper plus solder solder-coated one or you know, solder-coated ones like this, and also gold flash-plated ones as well.

**Dave Jones:** But we're just going to start out with this solder one to see if we can measure the difference. So, we'll measure the resistance of that pad before and after we fill it with solder, see if we can measure the difference.

**Dave Jones:** I'm pretty confident we will be able to. And in case you're wondering, this is an old board. This is a hydrophone calibration test box. Geez, when the Nixa's Thompson Marconi sonar.

**Dave Jones:** Geez, those were the days. Don't even don't know if I got a date code on there, but hey, there's DLJ with a smiley face up there. This was a dual channel charge amplifier.

**Dave Jones:** So, you can tell in op-amp arrangement here with the dual dual capacitors in there and this was in a charge two channel charge amplifier configuration for the duct the device under test and the reference and then a power little power amplifier on here to drive a speaker sort of a self-contained calibration test box.

**Dave Jones:** Anyway, let's get to it. And I don't have the original files to check the exact whole size here but roughly based on my little whole gauge here it seems to be about 1.2 mm.

**Dave Jones:** Not that the actual diameter is going to matter. We just want to be able to see if we can see a difference. That's all we're going for here. The absolute value doesn't matter.

**Dave Jones:** Just want to see if it actually changes. So, my test setup here is my Rigol power supply set to constant current mode. I can just program in the current.

**Dave Jones:** You can see I've probably got Yeah, you can likely see that 1 amp constant current programmed in there at the moment and then I'm reading the voltage across directly across on my 6 and 1/2 digit Agilent bench meter here and there you go.

**Dave Jones:** You can see it's 655 mV or thereabouts and I'll show you the four terminal measurement down here. So, as I said before current flowing into this pad down here and you might be able to see that on the bottom of the board.

**Dave Jones:** Anyway, it flows around there on the bottom up through that via there and to the other side of the power supply. So, there's our current loop there. So, it's a direct short on the output of the power supply.

**Dave Jones:** Of course, the power supply puts a constant current through that and then I'm tapping off a sense line there. That's the negative sense line and this positive sense line goes on the bottom side as we saw before to the other side of the pad there.

**Dave Jones:** So, we're sensing directly on that pad or via there. And the reason I don't actually attach the wire directly to there is because there's no drop across here at all.

**Dave Jones:** It doesn't matter. Effectively infinite input impedance of the multimeter makes no difference whatsoever and I don't want to disturb that pad either. I want I don't want to like reflow the solder joint before and after.

**Dave Jones:** So, now we've got a control condition where we're measuring the exact voltage across that pad, the resistance of that pad, and we know the current flowing through it. So, Ohm's law, we can calculate the resistance of that pad.

**Dave Jones:** Now, all we need to do is I'll do this for different currents, 0.1 amps all the way up to 2 amps, so we can actually get a graph of this thing.

**Dave Jones:** And uh then I'll do it I'll do all that data before and after I fill that with solder and then with wire. So, as we saw before, 0.651 mV.

**Dave Jones:** I'm just going to ignore that last digit. You know, it's that's really a bit meaningless due to noise, but this will be more than good enough to check, I think.

**Dave Jones:** And with precisely almost precisely 1 amp flowing through that, Ohm's law tells us we're looking at 0.65 mΩ in that particular pad there. But as I said, absolute value doesn't matter.

**Dave Jones:** We want to see if that changes. And of course, I can go in here and I can just go 0. Yeah, select 0.1 amps. And we should see that drop by an order of magnitude to 0.065.

**Dave Jones:** There we go, it certainly does. It's linear. And you can see that with no current flowing through there, we're getting a bit of an offset. I've actually got you know, it's physically disconnected down there.

**Dave Jones:** So, what we're going to do is just null out that value. There we go. We've nulled that out, and we can now take our readings. And I can see a slight creeping up.

**Dave Jones:** I'm now at 2 amps. So, this is the highest I'm going to go, 1.310 mV. It's slightly going up. That's due to the heating up of the actual via down in there.

**Dave Jones:** And let's see if we can just do a crude temperature measurement on this thing with my thermocouple. Ambient here in the lab, 26.4° 26.5° C. Let's call it that.

**Dave Jones:** It's going up a bit maybe because I've got my hand a little bit close to there. Anyway, let's do a delta on that and see if we can get a physical measurement.

**Dave Jones:** I've got to press down. It really, you know, it's not the most accurate. If you had a nice thermal camera of a really good close-up macro lens, you might be able to get it, but we're getting about a two I don't know.

**Dave Jones:** I could leave it there for a bit, jiggle it around, try and get the maximum. You know, 2.2 degrees C, let's call it that. And I just went to my satin calculator program just to verify what you'd get for a 1.2 mm pad typical 1 mil plated.

**Dave Jones:** I don't know if this board is 1 mil plated, but it's got some extra solder code on there, whatever. Near enough for a 2.2 degrees temperature rise delta on that pad and what maximum current it worked out to about 1.8, which is pretty close to the 2 amps that we're putting through.

**Dave Jones:** So, we're certainly in the ballpark. It's all working out. So, I've got all my data from 0.1 amps up to 2 amps in 0.1 amp increments, 20 data points, more than enough, and there are the voltages I get.

**Dave Jones:** We can plot that. That's for the bare pad. So, I'll do this again for the solder coated plot. But first of all, let's do a live test, see if it changes.

**Dave Jones:** Now, for the big test, we're currently 1.312 mV. And what I'm going to do is just fill this pad with solder. I'm going to do it live here, and we should see if the theory's right, should see this value drop.

**Dave Jones:** That's if they solder coating through that via makes a difference. This will confirm or deny the myth. The myth is that solder makes no difference whatsoever to that. You have to put a wire through.

**Dave Jones:** Well, we'll test the wire thing in a minute, but let's see if it makes a difference. I think it will. It won't be large, but we should see this value here drop.

**Dave Jones:** Now, we expect it to initially go up because I'm going to heat up the pad, but once it cool down could take like a minute to really cool down, but let's try it.

**Dave Jones:** Here we go. Okay, I'm on the pad. It's going up. Yep. Then apply some solder. So, what was it? 1.31? Something like that. There we go. I think it's flown all the way through.

**Dave Jones:** We'll have to check. Aha! Look. It does make a difference. There we go. It hasn't It's still cooling down. There you go. That is quite a significant difference. Myth busted that solder doesn't make a difference.

**Dave Jones:** It does. Fairly significant, actually. And the solder has kind of come all the way through, but just to be sure, I'll just coat the top side of that pad as well.

**Dave Jones:** So, it's got a nice beautiful even coat of solder, flowed all the way through, standard 60/40 solder. And we'll let that cool and take our measurements. And there is the data for the bare pad and the solder filled pad.

**Dave Jones:** And look at that. It dropped from 1.309 to .779. Almost half. Wow. Of course, this I expect this to vary a lot depending on the you know, the manufacturer the manufacturer of the board, the differences in manufacturing process tolerances, and all sorts of stuff for vias and holes.

**Dave Jones:** You know, there is quite a lot of manufacturing tolerance in these things, but on this particular solder filled board, certainly, look at that. A dramatic difference. Now, you could say that the other myth is that well, because the solder in the pad doesn't make a difference, you have to solder a wire through the pad if you want to or the via if you want to increase the

**Dave Jones:** current capacity of that via. Well, let's try it. I got a big ass resistor here. Um that leads, you know, like 1 mm diameter or something. Right, big chunky leads.

**Dave Jones:** So, I'm going to solder that through uh live here. And by the way, I can solder live. It doesn't matter if this soldering iron's earth or not because everything's floating here.

**Dave Jones:** So, I am able to solder on live equipment. Just be aware of that if you are doing a test like this just to make sure it's all floating and all your soldering iron isn't earth.

**Dave Jones:** Anyway, let's do it live. I'm at 2 amps. Uh there we go, 0.777. Will it make as big a difference? I.e. will it halve again? I I I don't know.

**Dave Jones:** I don't know. I've never actually tried it. Uh well, you know, I've done I've never actually done a controlled experiment on this. There we go. I've soldered it through.

**Dave Jones:** There we go. Should be soldered nicely on both sides. And uh yep. Yes, it has made a difference. It has made a difference. And in fact, look at that.

**Dave Jones:** Yeah. It's made a substantial I didn't think it'd make My gut feeling was it wouldn't make a huge amount of difference, but it Yeah, it certainly has. But uh the you know, but the solder also made a big difference.

**Dave Jones:** So, that one is certainly confirmed. Uh you do get uh lower resistance by soldering a uh copper wire through the pad like that. But because of course the copper is not directly touching the copper outer walls of the uh pad or via itself, you know, it's not going to make as huge a difference as it would if that hole or via was actually filled with solid copper to begin with.

**Dave Jones:** And there's all our data. Ta-da! To the spreadsheet. And here we go. I've entered the uh data in the tables here. And but that's just the uh voltages versus the current.

**Dave Jones:** I've converted that into resistance down here. And then I've plotted all this data. And ta-da! Look at our graph. Uh linear as you'd expect. A little bit of tailing up, a little bit of non-linearity at the bottom end there.

**Dave Jones:** But uh basically linear from 0.1 amps all the way up to 2 amps. And look at that dramatic drop. It's like I don't know the exact figure. Maybe at least 40% um there.

**Dave Jones:** You know, it's like quite a significant drop just from So, this is the bare via to the solder plugged via. So, just filling it with solder, we definitely busted that myth.

**Dave Jones:** Um, it does uh quite significantly and drastically reduce the resistance of that via and hence increase its current uh handling capability for a given temperature rise. And then um, once again, it halves yet again for the wire.

**Dave Jones:** So, if you go from the solder coat to the wire there, what is it? Maybe a third or something like that? But, yeah, there you go. Um, so, the wire one is confirmed.

**Dave Jones:** Yes, it does make a difference. But, the solder one does too. And uh well, I haven't seen any um data on this before, I don't think. There's probably something out there, but um yeah, this is quite interesting bit of uh research here.

**Dave Jones:** I'd love to actually do it further and do all the different types of vias with the different hole diameters and get a whole parametric curves and something like that.

**Dave Jones:** That'd be fantastic. That'd be a nice little um experiment to do. Like a bare just a bare via with just uh you know, with no uh gold coating, no solder coating.

**Dave Jones:** So, just the bare copper via and then the uh solder coated via as we did here. And then also a gold plated one, for example, or maybe a silver plated uh one, for example.

**Dave Jones:** And that would be most interesting. But, as I said, I think the data is going to vary a lot depending on the actual uh PCB and the manufacturing process used.

**Dave Jones:** Cuz there's a lot of tolerance, very large tolerances. It's not like 5, 10%, you know? We could be looking at, you know, a 100% um you know, something like that difference in, you know, like doubling the values, stuff like that for uh various uh manufacturers and their manufacturing process technology and what they guarantee in terms of their uh plating minimum plating thickness and stuff like that.

**Dave Jones:** I have no idea what that board was. I used the plating thickness used in there, you know, but it did work out to basically very similar, as I said, to that, uh, value, which I've got here.

**Dave Jones:** If I have a look at it, there it is. Um, it worked out to that, uh, 1.8 amps down here that for that 2.2° temperature rise, which we actually, uh, measured.

**Dave Jones:** And, uh, with hindsight, it's not really surprising that the value actually dropped filling the hole with solder because, as I've linked in a previous video showing that it does make a difference on traces on a PCB if you coat them in solder.

**Dave Jones:** Not nearly as much as, uh, it does does seem to here, at least in this particular, um, example, because the top of a PCB is a fairly uniform thickness, whereas I've, um, just picked this, uh, page off random off the internet, PCB007.com.

**Dave Jones:** Thank you very much. Um, the this shows a typical double-sided uh, plate-through hole. And, you know, these corners here, um, where the copper attaches, you know, very thin and this is much thinner, of course, than the consist and it's less consistent than the thickness of the copper on the top.

**Dave Jones:** So, if it makes a difference on the top, imagine what the variability in the corners, in the connection in the corners down there are like that. And when you then have a nice big solder fillet on top and then going all the way through, you'd expect it, uh, to make a larger difference than it does if you just solder coat a very consistent amount of copper on the top

**Dave Jones:** of the board here. And this one actually shows a copper, uh, wire going through as we experimented with there. And of course, you notice that it's not touching either side, whereas if it was, if it was like, uh, just like jammed in there, then you probably it probably would lower it a lot more cuz you'd have direct copper contact with sort of that side and upper, uh, surface in the corners there.

**Dave Jones:** So, if you really jammed it in there, but putting wire in there does make a difference by lowering the resistance, but still there's no direct contact. So, you got to go through the actual solder to get from the copper on one side to copper to the other to lower that resistance, but it still does make a significant difference.

**Dave Jones:** So, it all works out. I found that really interesting. I love getting data like that and plotting it and actually measuring. So, I hope we busted a couple of myths there.

**Dave Jones:** Yes, you can just solder vias. Fantastic. Who knew? There you go. Well, I hope that's cleared that up and you found that interesting. If you do want to discuss it, jump on over to the EV blog forum.

**Dave Jones:** Catch you next time.
