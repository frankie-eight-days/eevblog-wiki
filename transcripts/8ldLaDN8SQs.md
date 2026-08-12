---
video_id: 8ldLaDN8SQs
title: EEVblog #895 - BEC Pro Model Airplane Regulator Testing
url: https://www.youtube.com/watch?v=8ldLaDN8SQs
source: youtube-asr
timestamps: {"0": 1, "1": 11, "2": 21, "3": 40, "4": 50, "5": 72, "6": 91, "7": 101, "8": 113, "9": 124, "10": 139, "11": 150, "12": 162, "13": 177, "14": 188, "15": 199, "16": 214, "17": 226, "18": 240, "19": 252, "20": 267, "21": 282, "22": 311, "23": 322, "24": 343, "25": 358, "26": 382, "27": 403, "28": 415, "29": 425, "30": 440, "31": 453, "32": 466, "33": 479, "34": 493, "35": 507, "36": 516, "37": 527, "38": 539, "39": 546, "40": 554, "41": 565, "42": 576, "43": 589, "44": 602, "45": 612, "46": 626, "47": 638, "48": 650, "49": 663, "50": 673, "51": 682, "52": 689, "53": 705, "54": 714, "55": 727, "56": 734, "57": 745, "58": 763, "59": 778, "60": 791, "61": 807, "62": 832, "63": 850, "64": 858, "65": 873, "66": 889, "67": 898, "68": 912, "69": 933, "70": 956, "71": 965, "72": 979, "73": 991, "74": 1001, "75": 1014, "76": 1023, "77": 1035, "78": 1049, "79": 1064, "80": 1075, "81": 1082, "82": 1096, "83": 1111, "84": 1127, "85": 1137, "86": 1148, "87": 1160, "88": 1179, "89": 1199, "90": 1213, "91": 1220, "92": 1238, "93": 1263, "94": 1277, "95": 1298, "96": 1309, "97": 1322, "98": 1334, "99": 1343, "100": 1353, "101": 1375, "102": 1390, "103": 1406, "104": 1421, "105": 1433, "106": 1445, "107": 1457, "108": 1469, "109": 1480, "110": 1507, "111": 1519, "112": 1532, "113": 1544, "114": 1562, "115": 1575, "116": 1589, "117": 1607, "118": 1622, "119": 1631, "120": 1642, "121": 1656, "122": 1666, "123": 1676, "124": 1688, "125": 1703, "126": 1726, "127": 1737, "128": 1747, "129": 1757, "130": 1769, "131": 1783, "132": 1798, "133": 1814, "134": 1823, "135": 1833, "136": 1842, "137": 1853, "138": 1859}
---

**Dave Jones:** Hi, I got this little, uh, voltage regulator block designed for use in, uh, model airplanes. Got it in a previous, uh, mailbag segment. Took a quick look at it and I, uh, goofed that up at the time.

**Dave Jones:** So, I thought I'd have a more detailed look at it. Uh, Keith sent this in and him and his model, um, airplane buddies wanted to know, um, if this thing was any good.

**Dave Jones:** It's, uh, from a company called Castle, uh, Creations and it's the BEC Pro. BEC is a battery eliminator uh, circuit designed, uh, to power these solenoids and the, uh, receivers and other things in a model airplane from the high voltage model airplane battery itself.

**Dave Jones:** So, you don't need a secondary battery and things like that. So, you wanted to know, this thing's cheap. It's like $38 or something, which is apparently cheap for one of these things and, uh, he wanted to know if it was any good or not.

**Dave Jones:** We took a quick look at it in a previous, uh, mailbag, but I thought we'd actually, um, check the output power, actually power the thing up and see if it's any good because it's supposed to have a contin- maximum continuous output current anywhere from, uh, from 8 amps up to, uh, 15 amps here depending on the input voltage.

**Dave Jones:** And it has an adjustable, uh, output voltage as well, anywhere from 4.8 volts to, uh, 12.5 volts. And if you take a look at, uh, the figures here that this thing claims, the input voltage, uh, anywhere specified anywhere from 16 to 48 volts depending on what type of, uh, battery you've got.

**Dave Jones:** Um, in this case it, you know, it tells you, uh, like an 8-cell battery, 10-cell and a 12-cell. That's what the, uh, S4 12 in series, uh, stands for.

**Dave Jones:** And so, it can go anywhere up to 50 volts. And of course, it's going to have a varying, uh, output power capability. So, here is the output current and, um, Keith said that he set this one to 6.5 volts.

**Dave Jones:** So, I don't know how to adjust it. We'll just keep it set to 6.5 volts for uh the purposes of today's experiment. And these are the maximum continuous output powers.

**Dave Jones:** Just multiply the 6.5 volts times the uh output current here at different input voltages. And it can be anywhere from 52 watts up to 97.5 watts in this tiny with this tiny little heat sink here.

**Dave Jones:** And as I mentioned in the previous mailbag, um you know, that sounds a bit sus. Because a heat sink like this is only going to have a certain amount of power dissipation capability.

**Dave Jones:** Uh roughly, I believe, about uh for this uh type and size one, about 6°C per watt. So, for each watt dissipated, it's going to uh increase by, you know, 6°.

**Dave Jones:** We'll go into uh details in a minute on that. And the uh these This is a DC-to-DC converter, of course, and it's going to have an efficiency uh of, you know, at best 90% at one of these particular things.

**Dave Jones:** They would have designed it at for one particular output current. Because you can design DC-to-DC converters with 90% plus efficiency if you choose the correct type of magnetics, i.e., the inductor here.

**Dave Jones:** That's what this uh big device is, the you know, the MOSFET, the output capacitance, and the switching frequency. And you can actually design it for quite reasonable efficiency. So, let's say it's 90%.

**Dave Jones:** Um if you're getting near 100 watts here, let's just say it's 100 watts. At 90% efficiency, this thing has to dissipate 10 watts. So, that's going to cause a temperature increase in our active semiconductors that are dissipating the power here.

**Dave Jones:** Uh namely, we've got our two MOSFETs here. These are D409s. You might think this is the MOSFET, but it's not. Dead giveaway here is not connected. An A for anode, and the other one would be the cathode here.

**Dave Jones:** That's uh the diode. And, of course, the uh inductor here will be dissipating uh power as well. But because that's not an active uh semiconductor with a maximum junction temperature where the magic smoke can escape, that one's much more hardy than the other.

**Dave Jones:** So, we're really concerned about these devices dissipating power. And because the heatsinks on the other side of the board and they've just got vias underneath these going down to the other side actually transferring the heat from one side to the other, we're going to get losses in there.

**Dave Jones:** So, you've got your junction to case losses and then you've got your case to PCB, then you've got your PCB from top side to the side those losses in the vias, then you've got your contact thermal resistance with the heatsink and then you've got the thermal resistance of the heatsink as well.

**Dave Jones:** And I've done a videos on thermal design and things like that. So, I'll link those in if you want to check them out, but yeah, we're really concerned about these heating up with such a small heatsink with a large power dissipation like this 50 to 100 watts.

**Dave Jones:** You cannot design it to have 90% efficiency at each of these input voltages. When you design a DC to DC converter like this to operate over a wide voltage range and a wide output power range due to various factors in the design, you just cannot get a general purpose wide input voltage and a wide output current range to have a, you know, universal high efficiency across all the input voltages and all the

**Dave Jones:** output powers. So, if we have a look at the data sheet here for the actual device used in this, which is the LTC3824, which is a high voltage step down controller that goes up to 60 volts, is exactly what you would use here.

**Dave Jones:** It's a pretty decent controller and take a look at the efficiency and power loss versus load current graph on the right there. You can see that the top one with VIN equals 12 volts, look at it approaches that 90% efficiency that I was talking about there, but at higher input voltages VIN equals 40 volts, it's a different curve entirely.

**Dave Jones:** And we're looking at, say, you know, 40 volts depending like at a couple of amps, for example, but this, you know, is based on which particular transistor you pick and and inductor and everything else, right?

**Dave Jones:** Because this doesn't have the switching MOSFET built in, but, you know, you can see it drops down to, you know, it could be well under 80%, you know, 75% efficiency would be fairly typical of something like this at a higher voltage unless you specifically designed it for high voltage uh use only at one specific input voltage, and that's a disadvantage of a design like this is that, you know, the

**Dave Jones:** efficiency is going to vary quite drastically over that input voltage range and output current range as well. So, it's always going to be a compromise, which is why the specs for this thing actually show as the input voltage rises, you saw on the specs on the back of the thing that the uh maximum power dissipation in it drops.

**Dave Jones:** Uh the efficiency of a typical DC-to-DC converter, and it's going to have something like that. There's going to be a peak voltage and current where it is, you know, at its most efficient, but at lower than that, its efficiency is going to drop off.

**Dave Jones:** At higher than that, the efficiency is going to drop off. And when the efficiency drops off, you dissipate even more power in your heat sink here, and well, that ruins your day.

**Dave Jones:** So, let's see if this thing is actually can meet its claims here of a maximum continuous output current. Let's go. I'll just mention briefly though the capacitors cuz these will be a big uh failure point in these things.

**Dave Jones:** If these are wet electrolytic uh capacitors, then they can dry up and, you know, over time, and of course, the output the ESR increases and their life expectancy uh goes down.

**Dave Jones:** So, pretty terrible. We've got 105°C rated uh electro over here. This is on the input. And now our two output caps, um these actually don't look like wet electrolytic uh uh dielectric material.

**Dave Jones:** They actually look like a polymer capacitor or uh what's called a solid electrolytic capacitor. I.E. there's no liquid inside them, but they that doesn't mean they still can't um they still don't have a maximum uh lifespan.

**Dave Jones:** And the I'm not 100% sure that they're uh solid uh polymer types, but you would have to look up the specific data sheet. I didn't have any uh luck with that particular uh part number or whatever, but it's got no vent on.

**Dave Jones:** And there's no like score marks in the top for venting. And that if you see those, then that's a dead giveaway that it's a wet electrolytic uh capacitor, your traditional electrolytic capacitor.

**Dave Jones:** That's going to uh have a shorter lifespan at higher temperatures than than the solid types. And it's a myth that all of these uh surface mount types are solid.

**Dave Jones:** That is not necessarily the case. And just because it doesn't have a score mark, a vent in there on the top, um then that still doesn't mean guarantee that it's a solid type.

**Dave Jones:** This could still be a wet electrolytic type. Anyway, just thought I'd point out the difference there. Anyway, let's give them the benefit of the doubt. Those are uh properly uh spec'd solid uh capacitors.

**Dave Jones:** And by the way, that nice shine on there is a conformal coating. So, that's very nice. That's something for something that's uh used in like an outdoor RC plane.

**Dave Jones:** Anyway, let's hook this puppy up and see if we can measure it measure its performance. And they've basically got the uh wiring on this a bit back to front.

**Dave Jones:** Look at the nice beefy 16 gauge wires they've got on the input here, but the input is going to be lower current than your output. The output thing, as you saw, this thing has a maximum of 15 amps.

**Dave Jones:** And then you got a well, we've got two wires in parallel here. Okay, so it may do the business, but uh you know, we've got this these tiny little piddly connectors, which aren't going to do the current.

**Dave Jones:** You can, of course, uh put them in parallel like that, but, you know, 15 amps, uh these are going to get maybe 5 amps each, so, you know, like tops.

**Dave Jones:** So, really, you know, you can't do the maximum 15 amps with just these two. Anyway, let's uh cut these off and have a look at uh the wiring inside here to see if it's adequate.

**Dave Jones:** Ah, yeah, that's uh that's pretty decent. That's pretty decent. There you go. No worries. You put two of those in parallel, we'll be hunky-dory. So, to test a regulator like this, we need a power supply.

**Dave Jones:** Of course, I'm using my Rigol DP832. Uh now, this is only maximum capable of uh 30 volts uh 3 amps per channel, but because it's got two channels, or actually three here, we can put them in series.

**Dave Jones:** So, that's why I've got this wire here just looping the positive and negative like that, and then we can get a maximum of up to 60 volts. So, we can go right up to that 48-volt input uh capability easily with this.

**Dave Jones:** And the good thing about this is that it has a power output as well, but of course, uh any decent power supply is at least going to display voltage and output voltage and output uh current, but this will display our power as well.

**Dave Jones:** So, we know our power input to the uh module itself, and we know the power output. And the other bit of gear we need is an electronic load. You can actually use a resistive uh load if you've got those.

**Dave Jones:** You can cobble them together, but a a nice precision electronic load like this BK Precision 8601 can't beat it. And uh we've got and we can set the output uh current.

**Dave Jones:** So, uh what I'm going to do is actually set the output uh the constant output uh current to, in this case, uh 8 amps, and it'll tell us the output power.

**Dave Jones:** And in this case, it is actually telling us the output voltage. But, we need to do one more thing with this setup because these output leads are really actually quite wimpy.

**Dave Jones:** There's at like high currents, like we're talking 8 to 15 amps here. Uh we're going to get serious voltage drop across these leads. So, we're actually going to get power dissipated into that and our uh figure on here will not be accurate for our output power.

**Dave Jones:** So, um conveniently, we've got the second one here and we're going to actually uh wire it into the back of this BK Precision unit for the remote voltage uh sense terminal.

**Dave Jones:** So, it's going to sense the voltage directly on the output here. So, uh at at the moment, because there's no load, the output voltage at the terminals here is going to be exactly what the output voltage here.

**Dave Jones:** So, there's no current uh flowing at the moment through these cables, so there's going to be no voltage drop. But at 8 amps, it's going to be very significant.

**Dave Jones:** All right, let's test it. I've set both channels here to 24 V, so that's going to give us a 48-V output. And if we have a look at the uh data we had before, 48 V, its maximum rating is 8 amps uh continuous.

**Dave Jones:** So, I've set the 8-amp up here on the uh electronic load up here. We'll switch it on in a second. And um it should what it claims to have a maximum power dissipation capability uh based on uh the output uh current here of around about 52 W.

**Dave Jones:** Let's just call it 50 W or thereabouts. So, at 48-V input, uh you know, at 100% efficiency, uh and with 50 W output, we need to supply this power supply needs to be capable of supplying 48 V at 1 amp uh to give that 50 W.

**Dave Jones:** It's easily going to do that. It's got 3-amp output uh capability. So, I set the maximum output uh current here to 3 amps because, look, we don't need to protect this thing.

**Dave Jones:** I don't care, you know, it's not the design phase. This is supposed to be a finished product. It's supposed to work. So, I could set the limit, you know, if you were testing a design, your own DC to DC converter, you know, just to be safe, you would set the output current to 1.1 amps uh per channel or something like that.

**Dave Jones:** But, you do have to be careful setting a uh low safe, in quote marks, uh current output limit, because uh you can get uh certain like power on surge currents, and that may up and then this the power supply that you're powering your uh converter with may go into current limiting mode, it drops the voltage, and then that causes, you know, a problem with your converter, and well,

**Dave Jones:** that can ruin your day. So, anyway, I just got to set 3 amps. Let's go. So, what I'm just going to show you now is if I don't hook the voltage sense lead up to the rear uh voltage sense terminal in this, you'll know you'll see how much uh voltage drop we get across these cables at this uh 8 amps continuous current.

**Dave Jones:** So, let's turn our load on. We've got Yeah, everything's right. Let's switch it on, and we're getting 6. Uh 6.6 volts at the moment. So, let's switch it on.

**Dave Jones:** Bingo, it's dropped down to 6.18 volts. So, it's reading 6.18 volts directly on these terminals here, and so there's going to be some loss in these leads. I can actually measure the other uh two wires hooked onto here and see what we get.

**Dave Jones:** And you can see that if I use my meter here to actually probe directly onto uh the output of the uh brick here. So, I'm measuring just directly on the output terminals, you'll see it is still holding at 6.55 volts.

**Dave Jones:** So, it seems to be handling that 52 watts just fine, and still giving our uh set uh output voltage. But, you'll notice that it's only reading 6.1 up here.

**Dave Jones:** That's because of the loss in the wires. So, if we take these two wires and don't short them out. If we take these and plug them into the rear sense terminals and switch the uh voltage sense from the front terminals to the rear, we'll be able to get a more accurate reading.

**Dave Jones:** And this is actually important, cuz you'll notice that our BK Precision Load up here is uh calculating an output power of 48.93 W and that is a very significant error because our meter here is showing that it's 6.56 V here.

**Dave Jones:** So, if you go 6.56 V times the 8 amps which this is actually measuring, okay? Then, that's going to give us a value of 52.48 W. That's the true 52 and 1/2 W is the true output power being delivered from this module, but we've got that error, very significant error up there on the BK Precision.

**Dave Jones:** So, that's a trap for young players. Make sure you use the external reference input. I'll show you how it works. And here's the sense terminal on the back. You can actually see positive and negative sense terminal.

**Dave Jones:** So, just hook these wires directly to the output terminals of the power supply module that you're testing. So, we'll turn our remote sense terminal on. Bingo. So, let's try that again, shall we?

**Dave Jones:** 8 amps constant current load on this thing, 6.59 V with no load. Turn it on. Bingo, it drops down to 6.58 exactly 5.5 exactly what we saw on the multimeter before.

**Dave Jones:** So, that's a big trap for young players and bingo, it's showing the 52.46 W. So, now we're getting accurate measurement. Trap for young players, voltage drop on the output leads.

**Dave Jones:** Now, just because this thing works doesn't mean that it's any good. Okay, it's outputting the set 6.5 5.5 V no problems at the rated 8 amps continuous output for a 48 V input.

**Dave Jones:** No worries, but what's the efficiency of it? How hot does it get? Is it going to last 5 minutes? Is it going to last 5 hours? Is it going to last 5,000 hours?

**Dave Jones:** Because it may shut down any second because of thermal overload. We don't know. So, if we have a look at the input powers here, look 35.25 W 35.25 W.

**Dave Jones:** Okay, so we add those together because we've got series. Well, hang on, folks. You'll see something starting to happen. The voltage is going up. The input power is, I think, and hang on.

**Dave Jones:** Hang on. Yeah, that's starting to smell pretty toasty. I think we've got a problem. Anyway, we add up uh, these two powers here. That's our input power. Oh, bingo.

**Dave Jones:** Whoop, it just died. I think, yep. Yep, it's cutting out. It's cutting out. This thing cannot handle that with a free air heat sink. And that's what I was about to get to.

**Dave Jones:** What we need to do now is measure the heat sink temperature here and see what we're doing. We can use a direct uh, thermal couple probe, but hey, I've got a Flir uh, E8 here.

**Dave Jones:** So, we'll give that a whirl. And as soon as it's powered up, here it goes. Hunky-dory. Let's measure the center here. Hopefully, you can see that. 160°. Yep, it's way too hot.

**Dave Jones:** I'm switching that off now. So, that is ridiculous, folks. 160 odd something degrees here. Um, hopefully you saw the uh, temperature up here. 161° with free air, but that's what I would have expected with such a tiny heat sink.

**Dave Jones:** It's not going to work in free air like this. But, hey, if you have a look at the uh, data sheet for this thing, it actually tells you that it's rated for uh, a certain particular air flow over the heat sink.

**Dave Jones:** And of course, the thing is if that heat sink is getting to 160°, then imagine what the uh, junction temperature in the poor little MOSFETs in there are getting to.

**Dave Jones:** It's like these things will shut down, burn up, the magic smoke will escape. So, it obviously cannot do its rated current with no air flow, but that doesn't surprise me at all.

**Dave Jones:** And we are actually measuring this out of its spec. We need an airflow over it. Anyway, let's take a snapshot here. Let's go 34.8 W, double that, and then we can calculate our efficiency.

**Dave Jones:** So, what we've got here is 69.7 W input power, 52.4 W output power, which you saw here like this. So, that gives us just divide 52.4 by 69.7 output power over input power, and we can get our efficiency here.

**Dave Jones:** So, you know, around about let's call it 75% efficiency. So, you know, that's fairly typical of what you'd expect of a DC-to-DC wide-range DC-to-DC converter like this. But, that means that heatsink, that poor piss-ant little heatsink there has to dissipate a lot of power.

**Dave Jones:** How much power does it have to dissipate? Well, you subtract 52.4 W from 69.7 W, and that leaves you with 17.3 W it's got to dissipate in that tiny little heatsink.

**Dave Jones:** We can have a look at the data sheet for the Well, not this exact heatsink cuz I don't know the exact heatsink, but I've got one the nearest I could find was this one.

**Dave Jones:** It's basically the third one down there on the list, the 625-45. And you can see the thermal performance graph here for the heatsink to ambient thermal resistance in degrees C per W on the vertical axis there versus airflow on the horizontal axis there.

**Dave Jones:** And we're looking at around about 440 LFM here for the starter sheet spec of 5 mph airflow. So, if we actually look at the graph here, it's the It's the third one down, and then we take 440 LFM, and we then extrapolate that back across, we get a thermal resistance of the heatsink of about 8° C per W.

**Dave Jones:** 8° C per watt is quite large and we remember we said before that we had about 17.3 watts dissipation in this thing due to the 75% efficiency at this particular input voltage.

**Dave Jones:** That equals multiply those, that equals 138 degrees C temperature rise above ambient. If ambient's like 20 degrees, we're looking at 150 more than 158. So, pretty close to what we got there even with the no even with the air flow over this thing, the nominal rated air flow.

**Dave Jones:** Notice we measured 161 degrees C. So, maybe the heat sink we've got slightly better than that cuz we were getting no air flow, but still this is way above the maximum junction temperature of the semiconductors.

**Dave Jones:** And if we actually have a look at the MOSFET used here, the AD409, then we can see that the maximum junction temperature, absolute maximum, junction and storage can temperature 175 degrees C.

**Dave Jones:** Of course, we are going to you might say, "Well, it's under that." Well, no, it's not because you have to look below that at the junction to ambient and what junction to case and then you've got a couple of degrees C per watt there you've got to add it on.

**Dave Jones:** Then I said you've got the vias and check out my other video which I've linked in where you can I go through the detailed calculations and show you how to do that.

**Dave Jones:** So, it's certainly going to add up that this thing there's no margin in this at all. If it does work, it's going to be extremely borderline for this particular performance.

**Dave Jones:** And you can look at the actual diode used here as well and look at its maximum junction temperature right down the bottom there plus 150 degrees C. So, once again, it's actually going to be higher than this if our heat sink's already at well, 161 and not with any air flow over it, but you've got all these junction to case and then the vias going through and then

**Dave Jones:** the thermal resistance of the insulating conductive a in there, the thermal pad, and everything else. It's just Oh, it's really borderline. And because everyone's going to want me to do it, uh what happens when I blow some air over this thing?

**Dave Jones:** Well, let's find out. I've got this little Soonon fan here, and the 5 mph is 2.2 or thereabouts m/s. So, I'm going to get my anemometer here, and uh I've set it so it's around about Yeah, you know, near enough to that.

**Dave Jones:** So, now we can blow our rated Well, you know, reasonably close to it. Our rated 5 mph airflow over this thing. So, we can re-power it up and measure it again.

**Dave Jones:** And check it out. This thing's actually doing amazingly well now. It's always amazing what airflow can do. We're looking at uh what, 70 72, something like that? Over 70°.

**Dave Jones:** That's certainly now certainly within a decent ballpark. So, yeah, I'm pretty darn happy with that. Look, the board's on an angle there, so I'm probably blowing across the parts as well.

**Dave Jones:** So, that's probably not the best. So, what I'm going to do is because the whole idea was just to just to do the heatsink. So, I'll flip it on that side where the board is down, and see if that see if it increases.

**Dave Jones:** I probably would expect it to increase a little bit like that when there's no now no airflow on the bottom. It's only under over the parts, which is certainly going to help.

**Dave Jones:** But, just over the heatsink. So, let's have a look at that now. I've had it going there for a while, and that's actually rather surprising. I'm getting under 70.

**Dave Jones:** Now, I would have expected that to increase, but uh I guess more airflow Yep, angled differently now over the fins, so I guess it's it's more efficient. And if we try and have a sneaky peek under like that, uh yeah, we've got the board on a bigger angle now, but yeah, we can like the case of the MOSFETs, for example, you get in there where let's call it 100

**Dave Jones:** degrees C, but that's probably still okay. Um yeah, I don't mind that at all, special for the amount of power that we're delivering and that we're dropping. That's Yeah, it's going to do the business.

**Dave Jones:** So, at 48 volts, we're cooking with gas, but does it work down at 16 volts input for a continuous output current of 15 amps? Well, I've changed to my PowerTech MP 3090 switch-mode supply here.

**Dave Jones:** It can only go up to 15.3 volts, but I'm going to, you know, say that's got to be near enough. Anyway, um I've got the constant current output set to 15 amps.

**Dave Jones:** We've got our 6.57 volts, exactly the same as before. Let's see what it does. What? What? What? What? It's dropped down to 1 volt. It's not It's dead. So, let's say go to 12 amps here and see what it does for 12 amps.

**Dave Jones:** Oh. There we go. And yep, she's working at 12 amps. We're getting the output power 78.5 watts there. So, yep, I'll leave that for a while and get some temperature.

**Dave Jones:** No, hang on, it's starting to drop. Starting to plummet. No, no, it doesn't like that. Doesn't like that at all. Nope. Nope, it's dropped out of regulation. Wham, gonsky.

**Dave Jones:** Anyway, as expected, it's much more efficient down at this 15.2 volts 5 amps, looking at 76 watts input power, 65.5 watts output power, about 86% efficiency there at the lower input voltage.

**Dave Jones:** And because of that increased efficiency, it's running at a much cooler 56° on the heat sink there. Once again though, in free air, nope. You really want that 122, nope, nope, nope, nope, nope.

**Dave Jones:** Well, you really want the air flow. So, if you're using this thing for its intended purpose for a model aircraft, you want some sort of, you know, like the heat sink, I don't know, poking out the bottom.

**Dave Jones:** I don't know where this would be mounted on a typical aircraft. You don't actually want it like inside the fuselage with no air flow and just like that it's not going to do the job.

**Dave Jones:** You really need the air flow over it makes a hell of a difference. Anyway, the reason that we're seeing the discrepancy versus the data sheet like the cool temperature we got on this operating versus the data sheet that I pulled out.

**Dave Jones:** This looks like it's about 4° C per watt, whereas our data sheet said about 15° C per watt. Obviously, you know, there's like just the design of the heat sink.

**Dave Jones:** It's a similar dimension everything else, but I think the fins are actually larger on this one. So, larger surface area I think the data sheet one had smaller surface area fins on it.

**Dave Jones:** So, yeah, that could probably double your thermal resistance of it and then that makes a huge difference. If you just looked at the data sheet value, then you would think, "No, this design is not viable.

**Dave Jones:** They you know, they haven't left adequate margin." But when you actually you know, do some tests on this granted they're not massively controlled tests, but they're you know, going to give you a decent back of the envelope performance figures, then you know, this thing is actually a pretty reasonable design at the higher input voltages.

**Dave Jones:** But as you've seen here, I'm only I've been operating now 10 amps output current by the way. So, 65 watts output power. But no, it basically from what I see further testing required of course, but it basically does not meet that 15 amps at output continuous output current at 16 volts.

**Dave Jones:** It can't even do it momentarily by the looks of it. So, yeah, I don't know what's going on there. Further testing required, but at the higher input voltages, certainly, it worked just fine.

**Dave Jones:** And there's reasonable margin on the design long as you got the airflow. So, there you go. I hope that's actually finally answered Keith's question. This video was longer than what I thought it would.

**Dave Jones:** It's come for about half an hour or so, but hopefully this is like a tutorial on sort of how to rough and ready tutorial. How do I characterize a DC-DC converter?

**Dave Jones:** But, like we There's a ton more stuff we can do with this. We haven't measured it over the full envelope range, and we haven't even checked the output ripple, and you know, like tons of stuff.

**Dave Jones:** We could go recharacterize this at every input voltage over every output current, get characteristic curves for the thing, and you can spend days and days and or weeks and weeks actually characterizing just a one brick like one regulator brick like this if you want to do it properly.

**Dave Jones:** So, we've just done, you know, a couple of simple spot checks today. Higher input voltages seems to work just fine given sufficient airflow. So, anyway, I hope you found this useful, and I will link in at the end of this video the extensive design tutorial.

**Dave Jones:** It runs for about 22 minutes. It's well worth watching on SMD thermal design, how to actually dissipate power in SMD packages like is used on this one, and it takes into account the via thermal resistance, and goes through all the calculations and graphs and everything else.

**Dave Jones:** So, well worth watching. Anyway, if you enjoyed it, please give it a big thumbs up. As always, links down below to yeah, or the forum or that sort of jazz.

**Dave Jones:** And don't forget if you want to support me, there's a Patreon link somewhere down in the bottom corner right at the end of this video. Thanks for everyone who supports me on Patreon.

**Dave Jones:** Awesome. Catch you next time. The copper will have a thermal resistance, too, but it can get quite complicated. So, I'm I'm assuming there's no loss in the in that copper itself.

**Dave Jones:** The next one is the via. The heat actually has to remember that 10 watts of heat or whatever it is has to transfer through the via. It's going to have a specific thermal resistance.

**Dave Jones:** And then it's got to get through that sill pad that we put in there. That sill pad will have a thermal resistance. Look up the data sheet for it.

**Dave Jones:** It'll tell you what it is. Typically, uh and then we're going to have the thermal resistance of the bar here.
