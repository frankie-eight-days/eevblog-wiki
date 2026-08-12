---
video_id: 8ldLaDN8SQs
title: EEVblog #895 - BEC Pro Model Airplane Regulator Testing
url: https://www.youtube.com/watch?v=8ldLaDN8SQs
source: youtube-asr
timestamps: {"0": 1, "1": 13, "2": 29, "3": 45, "4": 56, "5": 72, "6": 87, "7": 101, "8": 116, "9": 129, "10": 146, "11": 162, "12": 179, "13": 192, "14": 207, "15": 221, "16": 233, "17": 247, "18": 258, "19": 269, "20": 282, "21": 299, "22": 312, "23": 324, "24": 339, "25": 354, "26": 367, "27": 382, "28": 397, "29": 412, "30": 422, "31": 440, "32": 456, "33": 470, "34": 487, "35": 500, "36": 516, "37": 530, "38": 543, "39": 554, "40": 568, "41": 579, "42": 597, "43": 612, "44": 626, "45": 638, "46": 650, "47": 661, "48": 675, "49": 687, "50": 700, "51": 714, "52": 727, "53": 738, "54": 751, "55": 766, "56": 782, "57": 795, "58": 804, "59": 818, "60": 832, "61": 843, "62": 856, "63": 871, "64": 884, "65": 898, "66": 911, "67": 928, "68": 948, "69": 961, "70": 975, "71": 991, "72": 1007, "73": 1022, "74": 1035, "75": 1055, "76": 1073, "77": 1082, "78": 1098, "79": 1114, "80": 1129, "81": 1143, "82": 1157, "83": 1179, "84": 1197, "85": 1215, "86": 1228, "87": 1245, "88": 1263, "89": 1279, "90": 1296, "91": 1309, "92": 1324, "93": 1336, "94": 1348, "95": 1360, "96": 1375, "97": 1390, "98": 1406, "99": 1422, "100": 1443, "101": 1457, "102": 1471, "103": 1486, "104": 1501, "105": 1517, "106": 1532, "107": 1547, "108": 1562, "109": 1581, "110": 1601, "111": 1622, "112": 1632, "113": 1646, "114": 1661, "115": 1673, "116": 1685, "117": 1697, "118": 1711, "119": 1728, "120": 1742, "121": 1753, "122": 1767, "123": 1780, "124": 1793, "125": 1808, "126": 1819, "127": 1831, "128": 1844, "129": 1857}
---

**Dave Jones:** Hi, I got this little, uh, voltage regulator block designed for use in, uh, model airplanes. Got it in a previous, uh, mailbag segment. Took a quick look at it and I, uh, goofed that up at the time. So, I thought I'd have a more

**Dave Jones:** detailed look at it. Uh, Keith sent this in and him and his model, um, airplane buddies wanted to know, um, if this thing was any good. It's, uh, from a company called Castle, uh, Creations and it's the BEC Pro. BEC is a battery

**Dave Jones:** eliminator uh, circuit designed, uh, to power these solenoids and the, uh, receivers and other things in a model airplane from the high voltage model airplane battery itself. So, you don't need a secondary battery and things like that. So, you wanted to know, this

**Dave Jones:** thing's cheap. It's like $38 or something, which is apparently cheap for one of these things and, uh, he wanted to know if it was any good or not. We took a quick look at it in a previous, uh, mailbag, but I thought we'd

**Dave Jones:** actually, um, check the output power, actually power the thing up and see if it's any good because it's supposed to have a contin- maximum continuous output current anywhere from, uh, from 8 amps up to, uh, 15 amps here

**Dave Jones:** depending on the input voltage. And it has an adjustable, uh, output voltage as well, anywhere from 4.8 volts to, uh, 12.5 volts. And if you take a look at, uh, the figures here that this thing claims, the input voltage, uh, anywhere

**Dave Jones:** specified anywhere from 16 to 48 volts depending on what type of, uh, battery you've got. Um, in this case it, you know, it tells you, uh, like an 8-cell battery, 10-cell and a 12-cell. That's what the, uh, S4 12 in series,

**Dave Jones:** uh, stands for. And so, it can go anywhere up to 50 volts. And of course, it's going to have a varying, uh, output power capability. So, here is the output current and, um, Keith said that he set this one to 6.5 volts. So, I

**Dave Jones:** don't know how to adjust it. We'll just keep it set to 6.5 volts for uh the purposes of today's experiment. And these are the maximum continuous output powers. Just multiply the 6.5 volts times the uh output current here at

**Dave Jones:** different input voltages. And it can be anywhere from 52 watts up to 97.5 watts in this tiny with this tiny little heat sink here. And as I mentioned in the previous mailbag, um you know, that sounds a bit sus. Because a heat sink

**Dave Jones:** like this is only going to have a certain amount of power dissipation capability. Uh roughly, I believe, about uh for this uh type and size one, about 6°C per watt. So, for each watt dissipated, it's going to uh increase

**Dave Jones:** by, you know, 6°. We'll go into uh details in a minute on that. And the uh these This is a DC-to-DC converter, of course, and it's going to have an efficiency uh of, you know, at best 90% at one of these particular things. They

**Dave Jones:** would have designed it at for one particular output current. Because you can design DC-to-DC converters with 90% plus efficiency if you choose the correct type of magnetics, i.e., the inductor here. That's what this uh big device is, the you know, the MOSFET, the

**Dave Jones:** output capacitance, and the switching frequency. And you can actually design it for quite reasonable efficiency. So, let's say it's 90%. Um if you're getting near 100 watts here, let's just say it's 100 watts. At 90% efficiency, this thing

**Dave Jones:** has to dissipate 10 watts. So, that's going to cause a temperature increase in our active semiconductors that are dissipating the power here. Uh namely, we've got our two MOSFETs here. These are D409s. You might think this is the

**Dave Jones:** MOSFET, but it's not. Dead giveaway here is not connected. An A for anode, and the other one would be the cathode here. That's uh the diode. And, of course, the uh inductor here will be dissipating uh power as well. But because that's not an

**Dave Jones:** active uh semiconductor with a maximum junction temperature where the magic smoke can escape, that one's much more hardy than the other. So, we're really concerned about these devices dissipating power. And because the heatsinks on the other side of the board and they've just got

**Dave Jones:** vias underneath these going down to the other side actually transferring the heat from one side to the other, we're going to get losses in there. So, you've got your junction to case losses and then you've got your case to

**Dave Jones:** PCB, then you've got your PCB from top side to the side those losses in the vias, then you've got your contact thermal resistance with the heatsink and then you've got the thermal resistance of the heatsink as well. And I've done a

**Dave Jones:** videos on thermal design and things like that. So, I'll link those in if you want to check them out, but yeah, we're really concerned about these heating up with such a small heatsink with a large power dissipation like this 50 to 100

**Dave Jones:** watts. You cannot design it to have 90% efficiency at each of these input voltages. When you design a DC to DC converter like this to operate over a wide voltage range and a wide output power range due to various factors in

**Dave Jones:** the design, you just cannot get a general purpose wide input voltage and a wide output current range to have a, you know, universal high efficiency across all the input voltages and all the output powers. So, if we have a look at

**Dave Jones:** the data sheet here for the actual device used in this, which is the LTC3824, which is a high voltage step down controller that goes up to 60 volts, is exactly what you would use here. It's a pretty decent

**Dave Jones:** controller and take a look at the efficiency and power loss versus load current graph on the right there. You can see that the top one with VIN equals 12 volts, look at it approaches that 90% efficiency that I

**Dave Jones:** was talking about there, but at higher input voltages VIN equals 40 volts, it's a different curve entirely. And we're looking at, say, you know, 40 volts depending like at a couple of amps, for example, but this, you know, is based on

**Dave Jones:** which particular transistor you pick and and inductor and everything else, right? Because this doesn't have the switching MOSFET built in, but, you know, you can see it drops down to, you know, it could be well under 80%, you know, 75%

**Dave Jones:** efficiency would be fairly typical of something like this at a higher voltage unless you specifically designed it for high voltage uh use only at one specific input voltage, and that's a disadvantage of a design like this is that, you know, the

**Dave Jones:** efficiency is going to vary quite drastically over that input voltage range and output current range as well. So, it's always going to be a compromise, which is why the specs for this thing actually show as the input voltage rises, you saw on the specs on

**Dave Jones:** the back of the thing that the uh maximum power dissipation in it drops. Uh the efficiency of a typical DC-to-DC converter, and it's going to have something like that. There's going to be a peak voltage and current where it is,

**Dave Jones:** you know, at its most efficient, but at lower than that, its efficiency is going to drop off. At higher than that, the efficiency is going to drop off. And when the efficiency drops off, you dissipate even more power in your heat

**Dave Jones:** sink here, and well, that ruins your day. So, let's see if this thing is actually can meet its claims here of a maximum continuous output current. Let's go. I'll just mention briefly though the capacitors cuz these will be a big uh failure point

**Dave Jones:** in these things. If these are wet electrolytic uh capacitors, then they can dry up and, you know, over time, and of course, the output the ESR increases and their life expectancy uh goes down. So, pretty terrible. We've got 105°C

**Dave Jones:** rated uh electro over here. This is on the input. And now our two output caps, um these actually don't look like wet electrolytic uh uh dielectric material. They actually look like a polymer capacitor or uh what's called a solid

**Dave Jones:** electrolytic capacitor. I.E. there's no liquid inside them, but they that doesn't mean they still can't um they still don't have a maximum uh lifespan. And the I'm not 100% sure that they're uh solid uh polymer types, but you would have to

**Dave Jones:** look up the specific data sheet. I didn't have any uh luck with that particular uh part number or whatever, but it's got no vent on. And there's no like score marks in the top for venting. And that if you see those, then that's a

**Dave Jones:** dead giveaway that it's a wet electrolytic uh capacitor, your traditional electrolytic capacitor. That's going to uh have a shorter lifespan at higher temperatures than than the solid types. And it's a myth that all of these uh surface mount types

**Dave Jones:** are solid. That is not necessarily the case. And just because it doesn't have a score mark, a vent in there on the top, um then that still doesn't mean guarantee that it's a solid type. This could still be a wet electrolytic type.

**Dave Jones:** Anyway, just thought I'd point out the difference there. Anyway, let's give them the benefit of the doubt. Those are uh properly uh spec'd solid uh capacitors. And by the way, that nice shine on there is a conformal coating.

**Dave Jones:** So, that's very nice. That's something for something that's uh used in like an outdoor RC plane. Anyway, let's hook this puppy up and see if we can measure it measure its performance. And they've basically got the uh wiring on this a

**Dave Jones:** bit back to front. Look at the nice beefy 16 gauge wires they've got on the input here, but the input is going to be lower current than your output. The output thing, as you saw, this thing has a maximum of 15 amps. And then you got a

**Dave Jones:** well, we've got two wires in parallel here. Okay, so it may do the business, but uh you know, we've got this these tiny little piddly connectors, which aren't going to do the current. You can, of course, uh put them in parallel like

**Dave Jones:** that, but, you know, 15 amps, uh these are going to get maybe 5 amps each, so, you know, like tops. So, really, you know, you can't do the maximum 15 amps with just these two. Anyway, let's uh cut these off and have

**Dave Jones:** a look at uh the wiring inside here to see if it's adequate. Ah, yeah, that's uh that's pretty decent. That's pretty decent. There you go. No worries. You put two of those in parallel, we'll be hunky-dory. So, to test a regulator like this, we

**Dave Jones:** need a power supply. Of course, I'm using my Rigol DP832. Uh now, this is only maximum capable of uh 30 volts uh 3 amps per channel, but because it's got two channels, or actually three here, we can put them in

**Dave Jones:** series. So, that's why I've got this wire here just looping the positive and negative like that, and then we can get a maximum of up to 60 volts. So, we can go right up to that 48-volt input uh

**Dave Jones:** capability easily with this. And the good thing about this is that it has a power output as well, but of course, uh any decent power supply is at least going to display voltage and output voltage and output uh current, but this

**Dave Jones:** will display our power as well. So, we know our power input to the uh module itself, and we know the power output. And the other bit of gear we need is an electronic load. You can actually use a

**Dave Jones:** resistive uh load if you've got those. You can cobble them together, but a a nice precision electronic load like this BK Precision 8601 can't beat it. And uh we've got and we can set the output uh current. So, uh what I'm going to do is

**Dave Jones:** actually set the output uh the constant output uh current to, in this case, uh 8 amps, and it'll tell us the output power. And in this case, it is actually telling us the output voltage. But, we need to do one more thing with this

**Dave Jones:** setup because these output leads are really actually quite wimpy. There's at like high currents, like we're talking 8 to 15 amps here. Uh we're going to get serious voltage drop across these leads. So, we're actually going to get power

**Dave Jones:** dissipated into that and our uh figure on here will not be accurate for our output power. So, um conveniently, we've got the second one here and we're going to actually uh wire it into the back of this BK Precision unit for the remote

**Dave Jones:** voltage uh sense terminal. So, it's going to sense the voltage directly on the output here. So, uh at at the moment, because there's no load, the output voltage at the terminals here is going to be exactly what the output

**Dave Jones:** voltage here. So, there's no current uh flowing at the moment through these cables, so there's going to be no voltage drop. But at 8 amps, it's going to be very significant. All right, let's test it. I've set both channels here to

**Dave Jones:** 24 V, so that's going to give us a 48-V output. And if we have a look at the uh data we had before, 48 V, its maximum rating is 8 amps uh continuous. So, I've set the 8-amp up here on the uh

**Dave Jones:** electronic load up here. We'll switch it on in a second. And um it should what it claims to have a maximum power dissipation capability uh based on uh the output uh current here of around about 52 W. Let's just call it 50 W or

**Dave Jones:** thereabouts. So, at 48-V input, uh you know, at 100% efficiency, uh and with 50 W output, we need to supply this power supply needs to be capable of supplying 48 V at 1 amp uh to give that 50 W. It's

**Dave Jones:** easily going to do that. It's got 3-amp output uh capability. So, I set the maximum output uh current here to 3 amps because, look, we don't need to protect this thing. I don't care, you know, it's not the design phase. This is supposed

**Dave Jones:** to be a finished product. It's supposed to work. So, I could set the limit, you know, if you were testing a design, your own DC to DC converter, you know, just to be safe, you would set the output

**Dave Jones:** current to 1.1 amps uh per channel or something like that. But, you do have to be careful setting a uh low safe, in quote marks, uh current output limit, because uh you can get uh certain like power on surge

**Dave Jones:** currents, and that may up and then this the power supply that you're powering your uh converter with may go into current limiting mode, it drops the voltage, and then that causes, you know, a problem with your converter, and well,

**Dave Jones:** that can ruin your day. So, anyway, I just got to set 3 amps. Let's go. So, what I'm just going to show you now is if I don't hook the voltage sense lead up to the rear uh voltage sense terminal

**Dave Jones:** in this, you'll know you'll see how much uh voltage drop we get across these cables at this uh 8 amps continuous current. So, let's turn our load on. We've got Yeah, everything's right. Let's switch it on, and we're getting 6.

**Dave Jones:** Uh 6.6 volts at the moment. So, let's switch it on. Bingo, it's dropped down to 6.18 volts. So, it's reading 6.18 volts directly on these terminals here, and so there's going to be some loss in these leads. I can actually measure

**Dave Jones:** the other uh two wires hooked onto here and see what we get. And you can see that if I use my meter here to actually probe directly onto uh the output of the uh brick here. So, I'm measuring just

**Dave Jones:** directly on the output terminals, you'll see it is still holding at 6.55 volts. So, it seems to be handling that 52 watts just fine, and still giving our uh set uh output voltage. But, you'll notice that it's only reading 6.1 up

**Dave Jones:** here. That's because of the loss in the wires. So, if we take these two wires and don't short them out. If we take these and plug them into the rear sense terminals and switch the uh voltage sense from the front terminals to the

**Dave Jones:** rear, we'll be able to get a more accurate reading. And this is actually important, cuz you'll notice that our BK Precision Load up here is uh calculating an output power of 48.93 W and that is a very significant error

**Dave Jones:** because our meter here is showing that it's 6.56 V here. So, if you go 6.56 V times the 8 amps which this is actually measuring, okay? Then, that's going to give us a value of 52.48 W. That's the true 52 and 1/2 W is the

**Dave Jones:** true output power being delivered from this module, but we've got that error, very significant error up there on the BK Precision. So, that's a trap for young players. Make sure you use the external reference input. I'll show you

**Dave Jones:** how it works. And here's the sense terminal on the back. You can actually see positive and negative sense terminal. So, just hook these wires directly to the output terminals of the power supply module that you're testing. So, we'll turn our remote sense terminal

**Dave Jones:** on. Bingo. So, let's try that again, shall we? 8 amps constant current load on this thing, 6.59 V with no load. Turn it on. Bingo, it drops down to 6.58 exactly 5.5 exactly what we saw on the multimeter before.

**Dave Jones:** So, that's a big trap for young players and bingo, it's showing the 52.46 W. So, now we're getting accurate measurement. Trap for young players, voltage drop on the output leads. Now, just because this thing works doesn't mean that it's any good. Okay, it's

**Dave Jones:** outputting the set 6.5 5.5 V no problems at the rated 8 amps continuous output for a 48 V input. No worries, but what's the efficiency of it? How hot does it get? Is it going to last 5 minutes? Is

**Dave Jones:** it going to last 5 hours? Is it going to last 5,000 hours? Because it may shut down any second because of thermal overload. We don't know. So, if we have a look at the input powers here, look 35.25

**Dave Jones:** W 35.25 W. Okay, so we add those together because we've got series. Well, hang on, folks. You'll see something starting to happen. The voltage is going up. The input power is, I think, and hang on. Hang on. Yeah, that's starting to smell pretty

**Dave Jones:** toasty. I think we've got a problem. Anyway, we add up uh, these two powers here. That's our input power. Oh, bingo. Whoop, it just died. I think, yep. Yep, it's cutting out. It's cutting out. This thing cannot handle that with a free air heat sink.

**Dave Jones:** And that's what I was about to get to. What we need to do now is measure the heat sink temperature here and see what we're doing. We can use a direct uh, thermal couple probe, but hey, I've got

**Dave Jones:** a Flir uh, E8 here. So, we'll give that a whirl. And as soon as it's powered up, here it goes. Hunky-dory. Let's measure the center here. Hopefully, you can see that. 160°. Yep, it's way too hot. I'm switching

**Dave Jones:** that off now. So, that is ridiculous, folks. 160 odd something degrees here. Um, hopefully you saw the uh, temperature up here. 161° with free air, but that's what I would have expected with such a tiny heat sink. It's not

**Dave Jones:** going to work in free air like this. But, hey, if you have a look at the uh, data sheet for this thing, it actually tells you that it's rated for uh, a certain particular air flow over the heat sink. And of course, the thing is

**Dave Jones:** if that heat sink is getting to 160°, then imagine what the uh, junction temperature in the poor little MOSFETs in there are getting to. It's like these things will shut down, burn up, the magic smoke will escape. So, it

**Dave Jones:** obviously cannot do its rated current with no air flow, but that doesn't surprise me at all. And we are actually measuring this out of its spec. We need an airflow over it. Anyway, let's take a snapshot here. Let's go 34.8

**Dave Jones:** W, double that, and then we can calculate our efficiency. So, what we've got here is 69.7 W input power, 52.4 W output power, which you saw here like this. So, that gives us just divide 52.4 by 69.7 output power over input power, and we

**Dave Jones:** can get our efficiency here. So, you know, around about let's call it 75% efficiency. So, you know, that's fairly typical of what you'd expect of a DC-to-DC wide-range DC-to-DC converter like this. But, that means that heatsink, that poor piss-ant little

**Dave Jones:** heatsink there has to dissipate a lot of power. How much power does it have to dissipate? Well, you subtract 52.4 W from 69.7 W, and that leaves you with 17.3 W it's got to dissipate in that tiny little heatsink. We can have a

**Dave Jones:** look at the data sheet for the Well, not this exact heatsink cuz I don't know the exact heatsink, but I've got one the nearest I could find was this one. It's basically the third one down there on the list, the 625-45.

**Dave Jones:** And you can see the thermal performance graph here for the heatsink to ambient thermal resistance in degrees C per W on the vertical axis there versus airflow on the horizontal axis there. And we're looking at around about 440 LFM here for

**Dave Jones:** the starter sheet spec of 5 mph airflow. So, if we actually look at the graph here, it's the It's the third one down, and then we take 440 LFM, and we then extrapolate that back across, we get a thermal resistance of

**Dave Jones:** the heatsink of about 8° C per W. 8° C per watt is quite large and we remember we said before that we had about 17.3 watts dissipation in this thing due to the 75% efficiency at this particular input voltage. That equals multiply

**Dave Jones:** those, that equals 138 degrees C temperature rise above ambient. If ambient's like 20 degrees, we're looking at 150 more than 158. So, pretty close to what we got there even with the no even with the air flow over this

**Dave Jones:** thing, the nominal rated air flow. Notice we measured 161 degrees C. So, maybe the heat sink we've got slightly better than that cuz we were getting no air flow, but still this is way above the maximum junction temperature of the

**Dave Jones:** semiconductors. And if we actually have a look at the MOSFET used here, the AD409, then we can see that the maximum junction temperature, absolute maximum, junction and storage can temperature 175 degrees C. Of course, we are going to

**Dave Jones:** you might say, "Well, it's under that." Well, no, it's not because you have to look below that at the junction to ambient and what junction to case and then you've got a couple of degrees C per watt there you've got to add it on. Then

**Dave Jones:** I said you've got the vias and check out my other video which I've linked in where you can I go through the detailed calculations and show you how to do that. So, it's certainly going to add up that this thing there's no margin in

**Dave Jones:** this at all. If it does work, it's going to be extremely borderline for this particular performance. And you can look at the actual diode used here as well and look at its maximum junction temperature right down the bottom there

**Dave Jones:** plus 150 degrees C. So, once again, it's actually going to be higher than this if our heat sink's already at well, 161 and not with any air flow over it, but you've got all these junction to case and then the vias going through and then

**Dave Jones:** the thermal resistance of the insulating conductive a in there, the thermal pad, and everything else. It's just Oh, it's really borderline. And because everyone's going to want me to do it, uh what happens when I blow some air over

**Dave Jones:** this thing? Well, let's find out. I've got this little Soonon fan here, and the 5 mph is 2.2 or thereabouts m/s. So, I'm going to get my anemometer here, and uh I've set it so it's around about Yeah,

**Dave Jones:** you know, near enough to that. So, now we can blow our rated Well, you know, reasonably close to it. Our rated 5 mph airflow over this thing. So, we can re-power it up and measure it again. And check it out. This thing's actually

**Dave Jones:** doing amazingly well now. It's always amazing what airflow can do. We're looking at uh what, 70 72, something like that? Over 70°. That's certainly now certainly within a decent ballpark. So, yeah, I'm pretty darn happy with that. Look, the board's on an angle there, so

**Dave Jones:** I'm probably blowing across the parts as well. So, that's probably not the best. So, what I'm going to do is because the whole idea was just to just to do the heatsink. So, I'll flip it on that side where the board is down, and

**Dave Jones:** see if that see if it increases. I probably would expect it to increase a little bit like that when there's no now no airflow on the bottom. It's only under over the parts, which is certainly going to help. But, just over the

**Dave Jones:** heatsink. So, let's have a look at that now. I've had it going there for a while, and that's actually rather surprising. I'm getting under 70. Now, I would have expected that to increase, but uh I guess more airflow

**Dave Jones:** Yep, angled differently now over the fins, so I guess it's it's more efficient. And if we try and have a sneaky peek under like that, uh yeah, we've got the board on a bigger angle now, but yeah, we can like the

**Dave Jones:** case of the MOSFETs, for example, you get in there where let's call it 100 degrees C, but that's probably still okay. Um yeah, I don't mind that at all, special for the amount of power that we're delivering and that we're

**Dave Jones:** dropping. That's Yeah, it's going to do the business. So, at 48 volts, we're cooking with gas, but does it work down at 16 volts input for a continuous output current of 15 amps? Well, I've changed to my PowerTech MP

**Dave Jones:** 3090 switch-mode supply here. It can only go up to 15.3 volts, but I'm going to, you know, say that's got to be near enough. Anyway, um I've got the constant current output set to 15 amps. We've got our 6.57 volts,

**Dave Jones:** exactly the same as before. Let's see what it does. What? What? What? What? It's dropped down to 1 volt. It's not It's dead. So, let's say go to 12 amps here and see what it does for 12 amps.

**Dave Jones:** Oh. There we go. And yep, she's working at 12 amps. We're getting the output power 78.5 watts there. So, yep, I'll leave that for a while and get some temperature. No, hang on, it's starting to drop. Starting to plummet.

**Dave Jones:** No, no, it doesn't like that. Doesn't like that at all. Nope. Nope, it's dropped out of regulation. Wham, gonsky. Anyway, as expected, it's much more efficient down at this 15.2 volts 5 amps, looking at 76 watts input power, 65.5

**Dave Jones:** watts output power, about 86% efficiency there at the lower input voltage. And because of that increased efficiency, it's running at a much cooler 56° on the heat sink there. Once again though, in free air, nope. You really want that 122, nope, nope, nope, nope,

**Dave Jones:** nope. Well, you really want the air flow. So, if you're using this thing for its intended purpose for a model aircraft, you want some sort of, you know, like the heat sink, I don't know, poking out the bottom. I don't know

**Dave Jones:** where this would be mounted on a typical aircraft. You don't actually want it like inside the fuselage with no air flow and just like that it's not going to do the job. You really need the air flow over it makes a hell of a

**Dave Jones:** difference. Anyway, the reason that we're seeing the discrepancy versus the data sheet like the cool temperature we got on this operating versus the data sheet that I pulled out. This looks like it's about 4° C per watt, whereas our

**Dave Jones:** data sheet said about 15° C per watt. Obviously, you know, there's like just the design of the heat sink. It's a similar dimension everything else, but I think the fins are actually larger on this one. So, larger surface area I

**Dave Jones:** think the data sheet one had smaller surface area fins on it. So, yeah, that could probably double your thermal resistance of it and then that makes a huge difference. If you just looked at the data sheet value, then you would

**Dave Jones:** think, "No, this design is not viable. They you know, they haven't left adequate margin." But when you actually you know, do some tests on this granted they're not massively controlled tests, but they're you know, going to give you

**Dave Jones:** a decent back of the envelope performance figures, then you know, this thing is actually a pretty reasonable design at the higher input voltages. But as you've seen here, I'm only I've been operating now 10 amps output current by

**Dave Jones:** the way. So, 65 watts output power. But no, it basically from what I see further testing required of course, but it basically does not meet that 15 amps at output continuous output current at 16 volts. It can't even do it

**Dave Jones:** momentarily by the looks of it. So, yeah, I don't know what's going on there. Further testing required, but at the higher input voltages, certainly, it worked just fine. And there's reasonable margin on the design long as you got the

**Dave Jones:** airflow. So, there you go. I hope that's actually finally answered Keith's question. This video was longer than what I thought it would. It's come for about half an hour or so, but hopefully this is like a tutorial on

**Dave Jones:** sort of how to rough and ready tutorial. How do I characterize a DC-DC converter? But, like we There's a ton more stuff we can do with this. We haven't measured it over the full envelope range, and we haven't even checked the output ripple,

**Dave Jones:** and you know, like tons of stuff. We could go recharacterize this at every input voltage over every output current, get characteristic curves for the thing, and you can spend days and days and or weeks and weeks actually characterizing just a

**Dave Jones:** one brick like one regulator brick like this if you want to do it properly. So, we've just done, you know, a couple of simple spot checks today. Higher input voltages seems to work just fine given sufficient airflow. So, anyway, I hope

**Dave Jones:** you found this useful, and I will link in at the end of this video the extensive design tutorial. It runs for about 22 minutes. It's well worth watching on SMD thermal design, how to actually dissipate power in SMD packages

**Dave Jones:** like is used on this one, and it takes into account the via thermal resistance, and goes through all the calculations and graphs and everything else. So, well worth watching. Anyway, if you enjoyed it, please give it a big thumbs up. As

**Dave Jones:** always, links down below to yeah, or the forum or that sort of jazz. And don't forget if you want to support me, there's a Patreon link somewhere down in the bottom corner right at the end of this video. Thanks

**Dave Jones:** for everyone who supports me on Patreon. Awesome. Catch you next time. The copper will have a thermal resistance, too, but it can get quite complicated. So, I'm I'm assuming there's no loss in the in that copper itself. The next one is the via.

**Dave Jones:** The heat actually has to remember that 10 watts of heat or whatever it is has to transfer through the via. It's going to have a specific thermal resistance. And then it's got to get through that sill pad that we put in there. That sill

**Dave Jones:** pad will have a thermal resistance. Look up the data sheet for it. It'll tell you what it is. Typically, uh and then we're going to have the thermal resistance of the bar here.
