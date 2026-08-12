---
video_id: WlSb8hdFtTY
title: EEVblog #1368 - Active Oscilloscope Probes COMPARED (Part 2)
url: https://www.youtube.com/watch?v=WlSb8hdFtTY
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 30, "3": 47, "4": 62, "5": 75, "6": 88, "7": 102, "8": 117, "9": 130, "10": 142, "11": 155, "12": 169, "13": 186, "14": 196, "15": 213, "16": 224, "17": 239, "18": 251, "19": 264, "20": 278, "21": 292, "22": 306, "23": 318, "24": 333, "25": 343, "26": 357, "27": 369, "28": 383, "29": 397, "30": 411, "31": 427, "32": 443, "33": 459, "34": 471, "35": 483, "36": 494, "37": 505, "38": 520, "39": 534, "40": 553, "41": 568, "42": 579, "43": 592, "44": 607, "45": 625, "46": 634, "47": 649, "48": 666, "49": 681, "50": 699, "51": 719, "52": 732, "53": 746, "54": 763, "55": 774, "56": 788, "57": 800, "58": 813, "59": 827, "60": 839, "61": 850, "62": 860, "63": 871, "64": 884, "65": 895, "66": 908, "67": 918, "68": 929, "69": 939, "70": 951, "71": 965, "72": 980, "73": 995, "74": 1007, "75": 1024, "76": 1036, "77": 1051, "78": 1062, "79": 1073, "80": 1087, "81": 1103, "82": 1116, "83": 1127, "84": 1140, "85": 1150, "86": 1162, "87": 1178, "88": 1194, "89": 1206, "90": 1218, "91": 1233, "92": 1249, "93": 1264, "94": 1278, "95": 1292, "96": 1306, "97": 1320, "98": 1332, "99": 1346, "100": 1360, "101": 1375, "102": 1393, "103": 1407, "104": 1426, "105": 1441, "106": 1455, "107": 1470, "108": 1484, "109": 1499, "110": 1512, "111": 1526, "112": 1544, "113": 1558, "114": 1571, "115": 1585, "116": 1604, "117": 1619, "118": 1635, "119": 1649, "120": 1661, "121": 1672, "122": 1684, "123": 1698, "124": 1717, "125": 1731, "126": 1744, "127": 1758, "128": 1773, "129": 1785, "130": 1798, "131": 1811, "132": 1824, "133": 1836, "134": 1851, "135": 1866, "136": 1880, "137": 1893, "138": 1904, "139": 1919, "140": 1934, "141": 1949, "142": 1963, "143": 1975, "144": 1987, "145": 1997, "146": 2012, "147": 2022, "148": 2034, "149": 2046, "150": 2060, "151": 2072, "152": 2086, "153": 2100, "154": 2114, "155": 2127, "156": 2141, "157": 2153, "158": 2168, "159": 2185, "160": 2197, "161": 2209, "162": 2223, "163": 2238, "164": 2253, "165": 2266, "166": 2278, "167": 2293, "168": 2305, "169": 2321, "170": 2336, "171": 2350, "172": 2363, "173": 2381, "174": 2394, "175": 2409, "176": 2422, "177": 2435, "178": 2448, "179": 2461, "180": 2473, "181": 2485, "182": 2503, "183": 2514, "184": 2529, "185": 2541, "186": 2553, "187": 2566, "188": 2579, "189": 2593, "190": 2606, "191": 2617}
---

**Dave Jones:** Hi, in the previous video, linked in at the end and down below, if you haven't seen it and you must watch it cuz this is part two. We looked at four different passive oscilloscope probes, the switchable 1 to 10 probe, the fixed

**Dave Jones:** times 10, the high voltage probe, and the transmission line resistive probe. And these were all passive probes. But now, in this video, we're going to take a look at what pretty much can be called all active probes because they contain

**Dave Jones:** some sort of active amplifier circuitry. Our first one we got is the high voltage differential probe. This is the EVblog HVP70. It's a 70 MHz high voltage differential probe. It's designed for measuring, look, 1,000 V RMS max. But you might

**Dave Jones:** think, well, this one can do 5 kV and this one only does 1,000 V. What's the difference? Well, you remember I said this is mains earth reference and I've done that video on how not to blow up your oscilloscope. You cannot use one of

**Dave Jones:** these or you can't use one of your other probes because if you hook your ground point up, that is like connecting mains earth to any point on the circuit that you connect this through and you can come a gutter and you can blow up your

**Dave Jones:** product, your board, whatever. You can even blow up your oscilloscope. You blow up your leads. You can really have a bad day. So unless the ground of your product is actually isolated from mains earth, you can't just go sticking this

**Dave Jones:** ground probe willy-nilly anywhere in your circuit because you can come a gutter and things like you know, mains switching power supplies or other things, they're of course mains earth reference. So yeah, you plug this on the wrong point and it's just going to

**Dave Jones:** vaporize. But what the high voltage differential probe does is let you let you safely put either the ground or the positive lead anywhere in your circuit. Well, as long as what the maximum here is is is 1,000 V RMS and your common

**Dave Jones:** mode which is connected through the ground plus minus 700 V good enough for any like you know main switch mode power supply you can just connect your probes up to anywhere and you're going to be completely safe. You're not going to

**Dave Jones:** blow up your circuit. You're not going to blow up yourself. You're not going to blow up anything. These are great high voltage differential probes. Okay, just a quick recap with Dave Cat here on what this common mode voltage actually means.

**Dave Jones:** Well, this high voltage differential probe it basically is just a differential amplifier. It's just an amplifier like this that measures the voltage difference between the positive and negative input terminals like this and then it multiplies it by amplifies

**Dave Jones:** it by a gain of 10 or 100 depending on where you set the switch and then it just goes out to the BNC here to your oscilloscope. And of course the oscilloscope is going to be mains earth reference. So what this voltage here

**Dave Jones:** 1,000 V RMS maximum between the two terminals here is exactly as it says. It says you can have up to a maximum of 1,000 V RMS or basically the linear range the measurement range plus minus 700 V between these terminals

**Dave Jones:** either directions. So good enough for like mains measurement things like that and you can get higher voltage versions of these which go much higher. I think this is actually one of the lowest voltage ones on the market with times 10

**Dave Jones:** times 100 and we might explain why in a minute. Anyway, common mode voltage what that means is that between either of these inputs here either one positive or negative and this output it's output referenced and the output is of course

**Dave Jones:** going to your oscilloscope which is mains earth reference. So that's connected through to your mains which then could be connected back through your power point through to your product and I've done that whole video on how not to blow up your oscilloscope. So I

**Dave Jones:** won't recover all that. But basically this probe can handle up to plus minus 700 V between this is a voltage source here between either of these terminals and the output mains earth reference here. This is why you can pretty much

**Dave Jones:** for most practical circuits that are mains powered or lower voltage, you can connect your two probes up to any point in your circuit and you're not going to blow up anything. You're safe to measure any point in your circuit. So you can

**Dave Jones:** measure across you know like a shunt resistor in there or something like that to get the current waveform or whatever it is. Now here's a reverse engineer Dave Cadbury of a similar model to this one from the manufacturer Sapphire. This

**Dave Jones:** one will be exactly the same just some twite just some performance twite. Differences this is how these high voltage differential probes work and there's a big common misconception about these high voltage differential probes. People think that they're actually

**Dave Jones:** isolated that the inputs are somehow you know transformer or other isolated from the input. Well, that is not the case. All these things do is actually contain large value input resistors. In this case, it actually tells you down here.

**Dave Jones:** Read it. 4 meg each side to ground and 5.5 puff and that's exactly what you get. You get four 1 meg resistors to ground. Here's the ground terminal. Here is the output reference. I haven't drawn it but output

**Dave Jones:** ground over here like this and this comes from my reverse engineering drawing so I'll link that one in but basically yeah, that is connected through to here. So it's look it there it is. It's connected right through 4

**Dave Jones:** meg resistor and they've got a low value down here 25 so it's just a resistor divider in each leg and then they've got a FET differential amplifier here and some extra gain stage times 10 times 100 selected and that's it. That's all

**Dave Jones:** that's inside of one of these things but because they've got such high value resistors, you can plug them anywhere in your circuit and it's not going to cause a problem. But of course, it could potentially load down your circuit if

**Dave Jones:** it's a really high impedance circuit And course but that's the same with any probe. These things don't really perform as good as a proper oscilloscope one. This is only a 70 MHz bandwidth and with these long leads on the input, okay,

**Dave Jones:** you've got to twist them to get even half decent performance. And yeah, they're just not as good a performance as proper oscilloscope probes, but they're incredibly safe. And that's the reason that you want to use one of these. And you can probe any point in

**Dave Jones:** your circuit using a ground reference oscilloscope. They just uh like they they can't be beat. But the downside is is that because they have to have such large resistor divider ratios in order to be safe, then well, they're not great

**Dave Jones:** for low level measurements, which is why you won't find a high voltage which is why they're called high voltage differential probes. You won't find a Well, there are some low voltage differential probes, but like they're generally um high voltage because they

**Dave Jones:** have to have a huge divider ratio like that. And these are either battery powered in this case of this one four AA batteries in the back or you can power them because the power is output reference, you can actually power them

**Dave Jones:** from the USB port on your scope here if you've got an adapter cable. And our next probe, guaranteed to get every engineer all excited. Oh, it's the active FET probe. And they always come in impressive cases like this and

**Dave Jones:** this and this. Right, you never just get like a little like probe in a packet, whatever. No, they always come in beautiful cases like these. Let's take a look at them. So, here's a very typical active probe or

**Dave Jones:** the active FET probe or just FET probe because they've all got FETs right at the input here that actually amplify the signal before it comes in. So, they have active amplifier electronics inside the head as opposed to your passive probe here, which is

**Dave Jones:** just a basically a bit of a a resistor and a bit of coax, and the amplifier is inside the scope. Well, in this case, the amplifier is up here, which means they they have to actually be supplied by power. And it's very common for them

**Dave Jones:** to actually be powered from the oscilloscope under test. And look at these all lovely little pogo pins. And you usually buy them from uh the manufacturer of the oscilloscope cuz they've got their own interface. This one is your Agilent uh Keysight. So,

**Dave Jones:** those probes uh not only give it power, but they also, you know, tell it what type of probe it is and and things like that. Your signal doesn't actually come out on these pins. This is just power and um other data. Your signal, of

**Dave Jones:** course, goes into your input to your scope. So, it's just that's a regular BNC, but it just plugs in. It's all captive, and they usually have a little lever in there to clamp on the front of your scope. So, these things are usually

**Dave Jones:** very pricey, you know, they start in the four-digit category and uh go up to like five digits. And this one here is a two-gig uh bandwidth probe. Uh 10:1 uh divider ratio. 1 meg uh input impedance. And this uh Siglent one here, active

**Dave Jones:** probe, it's a it's 1 gig uh with 1 megohm and uh 1.2 picofarads. Uh but, you might think, "Well, okay, this is 1 gig. Well, so is this. What's the difference?" Well, the difference is, remember, this is like practically the

**Dave Jones:** world's best passive probe, 3.9 pF. This one, 1.2 pF. And that's the difference. You remember our formula before, capacitance is the thing that matters at high frequency. And in the case of this uh Siglent uh active uh probe compared to this Tektronix one,

**Dave Jones:** both are 1 gig rated probes, but because it's only 1.2 uh pF, it's 132 ohms at 1 gig, whereas the passive probe is 40 ohms at 1 gig. So, that can make a heck of a difference to the signal that

**Dave Jones:** you're actually measuring. That load that load is going on the line that you're trying to probe. So, the lower the capacitance, the less you're going to load your line. But, if you are talking uh DC, then the passive probe

**Dave Jones:** still better. That's 10 mega DC. These are only a meg. So, you'd use an active FET probe over your passive probe when a signal integrity at high frequency really matters. Well, A, these can go higher. This is actually the fastest

**Dave Jones:** passive tender one passive probe you can get at 10 meg. This is And as I said, this thing with a resistor will, you know, if you build it right, will actually outperform this. And these can actually go up to 10 gig. So,

**Dave Jones:** yeah, anyway, so the only solution basically for above 1 gig measurement is either an active FET probe or a resistive probe. That's it. And if you're wondering, this Agilent one is one puff input capacitance. And this one here, haven't measured it, but it'll

**Dave Jones:** like it probably on be on par. Something like that. In the order of a puff, half a puff maybe. So, the great thing about active FET probes is you they can actually go beyond 10 gig and beyond the

**Dave Jones:** performance of a simple resistive probe like this. So, if you're on the bleeding edge of measurement, you're you're really going to be wanting an active FET probe. So, pretty much as a ballpark, maybe anything over 500 meg, you want to either be using active

**Dave Jones:** FET probe or a properly built and characterized resistive probe. And like it can cost you more money to actually characterize this than to simply buy the already characterized active FET probe. And basically, these single-ended active probes give about stop at a couple of

**Dave Jones:** gigahertz. Anything over that, then you start talking a fully differential probe, but not high voltage like we looked at before. These would be low voltage differential probes, high speed, low voltage. But, the one downside with these things is Murphy can get really

**Dave Jones:** expensive. Like these probes can cost thousands of dollars, even into the six-digit range. And their huge Achilles heel is the maximum input voltage. In this case, max input 20 volts peak. Okay? Seriously, you go over that and this probe will blow up. You'll probably

**Dave Jones:** find eBay's filled with like all this FET probe "Yeah, sold as is." I would not be buying a sold as is FET probe off eBay. Just saying. We've got one from Caltech Electronics here. This one's a little bit more robust. We're talking 40 volts

**Dave Jones:** peak here. It's a 1.2 gig probe. Once again, 10 to 1. This one's higher input capacitance though, three puff. But, as you can see, this one you can get like generic ones. You don't have to get these ones designed for your specific

**Dave Jones:** scope. You can get these cheaper ones that just plug into your like any scope and they're just actively powered once again from just the USB port on the front of your scope. Nice. And as I showed before, these things always come

**Dave Jones:** with like all these accessories. Let's take a look at them cuz they're very interesting. So, these are the ones that come with the Caltech probes. You got beautiful little ultra tiny mini grabbers there. You've got little ground and probe pins like that, spare

**Dave Jones:** ones cuz you're going to be using them all the time. Plus, you've got like little pins like that you that you can plug into headers. And often on your designs, when you if you know you're going to be probing like you know a

**Dave Jones:** really serious designs, maybe on a prototype board, you don't necessarily need it on a production layout. But, on a prototype board, you're trying to get it working. You're measuring your high speed DDR bus or whatever. Then, you might have dedicated test points on

**Dave Jones:** there, even dedicated connectors for these high speed probes. And the Siglent ones, once again, you get all these like spare tips cuz you're going to be going through them like there's no tomorrow. You might even want to directly solder

**Dave Jones:** the tips into your circuit so that you can physically remove your probes. The most interesting kit comes with the uh Keysight one. Once again, you've got a little tube with all the uh little pins in there. They just don't give you many,

**Dave Jones:** do they? A bit of a tight ass. Real expensive probe. You get ultra tiny mini grabbers, once again. Like, these things are just super super tiny. And then you like plug into there and give you all sorts of other little uh adapters like

**Dave Jones:** that. Um and the most interesting thing is they give you uh copper pads like this and they actually give you a bit of a chart here on you know, some of the different uh probe connection techniques. And this is not the video to

**Dave Jones:** go into really high-frequency uh probing techniques, of course. But you can Look, you can plug directly into the head with some long leads like that. And that'll give like, you know, 500 meg bandwidth here, they're saying. Or uh you know,

**Dave Jones:** you can get a rigid probe tip with offset ground like that. So, it plugs in. And I love this uh Keysight head. It's got little LEDs on there that just light up it so you can see where you're

**Dave Jones:** actually plugging your probe into. Very nice. And then you've got a spring tip with ground blade like this. Uh and that'll give you like 2 gig bandwidth. And then you've got uh a copper pad which you can solder onto your circuit

**Dave Jones:** and that will give you like a flexible ground point. So, you know, often it's very difficult to apply pressure to like both of these points at the same time without one of them sliding around. Well, if you solder in like a large

**Dave Jones:** ground pad like like with that copper tape that they uh supply, then you know, you don't have to worry about your ground probes probes sliding around. Or you do have to keep an eye on it cuz Murphy's sure to slide off and short out

**Dave Jones:** one of your other pin sitting on your expensive $100,000 prototype board. Trust me, I've worked on $100,000 prototype boards. And if you blew that up, you Yeah, you're going to be having a bad day. But once again, you know, that

**Dave Jones:** might be a slightly reduced bandwidth to you know, this technique over here which is going to provide a lower inductance uh path. So, it's going to you know, you're going to get better performance out of it, something like that. And then

**Dave Jones:** you've just got, you know, if you want to put just pin headers on your board for various uh test signals. and then little short cables which run over and just plug into your probe tip. So all these different solutions for probing

**Dave Jones:** and you can even invent your own and as I said a lot of designers will solder on like like coax connectors directly onto the board and things like that. So you can plug on your own probes, your own

**Dave Jones:** resistive probes or active FET probes or whatever it is you're doing. So active uh FET probes, you can think of those as the Rolls-Royce of oscilloscope probes really. They're very nice but as with certain, you know, roll your own with a

**Dave Jones:** bit of RG174 coax and well you can get similar performance if you do it well enough but oh yeah, these can't be beat if you got the money. And these probes will usually require 50 ohm termination on your scope although this

**Dave Jones:** Cal Test one here, it actually well it comes with a 50 ohm terminator. Look at that, 2 gig 50 ohm in series in line terminator 2 watts. Oh, that's very nice. But this one actually lets you use it with a 1 meg input impedance scope

**Dave Jones:** just say no 50 ohm termination and it it gives you an actual attenuation setting of five times. So that's, you know, better for like low signal measurements. Nice. Okay, let's give you a probing example here. We've got a Raspberry Pi 3 for

**Dave Jones:** those playing along at home and we're going to probe one of the memory pins on the bottom here. I don't care which one. I've just picked one at random. We're getting a signal on it. So I'm using the

**Dave Jones:** 2 GHz active probe here the N2796 overkill for what we're doing. Well, overkill for this scope anyway because this is a 500 MHz bandwidth scope. So this active FET probe more than good enough for measuring the bandwidth that

**Dave Jones:** we got here. So I'll use this long lead here for my ground. I'll put it on the ground pin of the connector there cuz that's just very convenient. For those who care about such things, you You actually see what

**Dave Jones:** uh, I'm probing. Where is it? I think it's there. Geez, I can barely see that. This is where, you know, magnification, uh, comes in. Okay, I'm probing a point there. I don't know what it is. I don't care. There it is. There's our signal.

**Dave Jones:** It's made up of a whole bunch of, uh, stuff, but basically, uh, you can see, look, it's got some undershoot here. It's got a little bit of ringing there. It's got a little bit of ringing there. I'm going to hazard a guess that that's

**Dave Jones:** going to be due to our, uh, long ground lead there, right? So, that is our thing. But, we've got actually higher frequency stuff in here. Look at this. Oh, I just happened to capture one there. Look at this. Goes down, up.

**Dave Jones:** We're at, uh, what, 10 nanoseconds per division. We're almost as fast as we can get here, uh, with this, uh, scope. But, this actually does have some really fast, uh, pulses in here. So, something, you know, something you know, the bus is

**Dave Jones:** switching. It's doing whatever. I don't know what, uh, point we're probing. Check that out, right? There you go. Because that looks very sinusoidal, we're talking about that's our sin x on x interpolation there. So, this is like, sort of Once you see that, you know,

**Dave Jones:** okay, we're beyond the bandwidth of our scope here. These signals are just too fast. But, anyway, let's just go back to here. Okay, so, we'll just try and capture that sort of like the most frequent one there. There it is. Got it.

**Dave Jones:** Okay, so, I'll store that. All right, so, what I'm going to do now is I'm going to actually, uh, change the ground into this. Instead of having this longer lead, I'm going to go for one of the shorter, uh, little adapter ground

**Dave Jones:** adapter pins we've got in there. And it looks like there's a little bypass cap. I've determined that this right hand side is the ground. So, that's very convenient and because that's right next to the point that I want to test.

**Dave Jones:** Otherwise, as I, uh, showed you before that you might have to, uh, like install one of those copper pads or something. You might have to, like, scrape away some of the ground here or something like that and maybe

**Dave Jones:** put the copper tape over the top of the chip or something like that or you'd have to scrape away some other ground point somewhere or you know, soldering a little uh contact loop pin or something like that. So, here it is. I've got my

**Dave Jones:** little adapter. Careful cuz you can stab yourself with these little bastards. There we go. So, we have this little now ground pin which can sort of like, you know, pivot around like that and anyway, that will make better contact and this

**Dave Jones:** will be a higher frequency probe because it's a shorter inductive path. So, let's try that. We'll require the tongue at the right angle and probably some magnification here. Okay, I've got my ground point and I've got my probe

**Dave Jones:** point. Pan up. Pan up. Okay, let's have a look. I've changed my uh digitizer. Definitely getting 5 gig samples uh per second and I saved my reference waveform. So, let's single shot capture that. See if we can get it. No. There we

**Dave Jones:** go. Got it. Now, I can actually uh adjust that waveform there to show you. There you go. So, the orange one I've got there is the reference waveform and this new yellow one is the one that we just probed. And there you go. It is

**Dave Jones:** like it's of course like the same wave shape. You can see it's got the uh longer ground lead one, the orange one, has some extra undershoot there and comes back and takes more time to come back up like that. And the one up here

**Dave Jones:** got some extra wiggle wiggle wiggle year on the top there, some overshoot. And um so, you know, there are differences in probing right there. But at the moment, this is the loading of the line with a one picofarad, one puff active probe

**Dave Jones:** which costs a couple of thousand dollars. Okay, now I'm going to use my 500 megahertz uh passive probe here. It's the N28 uh 43. It's 11 picofarads. Okay? And yes, I've compensated this. You compensate it with your probe

**Dave Jones:** compensation on the front. So, everything's hunky-dory. I'm using my low inductance, high frequency uh ground probe attachment. So, that's equivalent uh to what we had before. So, um it we should get and because we've only got a 500 bandwidth scope uh here, then the

**Dave Jones:** bandwidth of the probe isn't really going to matter that much. Oh, my tongue at the right angle. And probe this. I think I got it. But, here's the interesting thing. I've changed uh the reference waveform to my uh low inductance uh short ground one

**Dave Jones:** before. So, the orange one is the best we could get with our active uh probe. So, the exact same ground point, basically the same ground length, and you can see that well, you know, our wave shape's the same, but look. Look at

**Dave Jones:** this. Um it's a much higher level down here. Okay, this is uh 200 mV uh per division. So, it's like, you know, 50-odd mV higher there. And it's actually lower down here, our yellow waveform there. So, you know, all

**Dave Jones:** although we can see like the wave shape and everything up here, it's like when the bus is loaded differently, cuz that's what this little uh you know, ramp up here is going here. I don't know the architecture of the

**Dave Jones:** Raspberry Pi. It it doesn't matter. But, I know there's something happening there with there. And down here, we're actually seeing a larger drop across the uh bus here, which is interesting, isn't it? I it you know, there's significant

**Dave Jones:** differences here. This is wasn't the exact example I wanted to show. I just like it's a random example, but you can see the difference here between a 500 meg passive probe and and effectively a because of the bandwidth of the

**Dave Jones:** oscilloscope of 500 meg active probe. They load down the circuit differently. And I know you want to see it. Okay, let's compare Dave's dodgy um homemade uh resistive probe here with a 1K resistor in the tip. We'll give that a

**Dave Jones:** whirl. Got a 50 ohm uh terminate that. But, scope can do that. No worries. Tongue at the right angle. Tongue the right angle. Fix that. Oh! Check this out. This is absolutely fantastic. Now, what we've got here, the orange

**Dave Jones:** waveform, of course, is our reference active FET waveform. That's a $2,500 active FET probe. Yes, it is compensated because you do still have to compensate them, and it stores it internally cuz it knows the serial number of the probe,

**Dave Jones:** etc. And the yellow one is Dave's do-it-yourself couple of buck resistive probe. Look at this. What's going on here? Well, it's obvious that what's happening at this point right here is that the bus is actually going open or something. I don't know

**Dave Jones:** the exact architecture of what's, you know, the pin I'm actually probing. It doesn't matter, right? It's like it's going open, and because the probe is 1 meg DC resistance, look at that, it's basically it's not going to discharge. Maybe if we

**Dave Jones:** got like a longer time period, it'd eventually do a similar like eventually discharge or whatever. But you see that the bus is actively changed, but because we're now loading this bus down with a 1K resistor or a 1.05K resistor cuz

**Dave Jones:** we've got the 50-ohm terminator as well, it boom! This is an This looks like for all the world, and it is an RC discharge curve. So, there you go. What's that, you know, 10 nanoseconds per division? I don't You can work that out, whatever,

**Dave Jones:** for those playing along at home. But you can see how the resistive probe actually completely changes the circuit that you're actually measuring. So, sure, let the signal integrity is excellent. Let's Let's take a look at this, actually. If

**Dave Jones:** you have a look at the bottom here, you can see that both of them undershoot almost exactly the same. But you remember how I said that the resistive probe can actually be more tolerant of longer ground leads. I think they're

**Dave Jones:** both about the same length. I think they're practically near identical. Remember how I said it can be more tolerant on these than active FET probes. This might be an example of this cuz this is not this is not some controlled experiment.

**Dave Jones:** This is just something I slapped together willy-nilly and this is the result that we actually got. This is fascinating, right? They both undershoot exactly the same but the active FET probe, the orange one, actually look it overshoots again when

**Dave Jones:** and it takes much longer to recover than the resistive probe. Look at that. So, this could be an example of where this cheap ass do-it-yourself resistive probe is actually outperforming this $2,500 active FET probe in terms of signal

**Dave Jones:** integrity. But once again, this is not a completely controlled experiment. But this is what you can actually get. But of course, the limitation is that it loads it down much more. 1K as opposed to 1 meg, right? There's a huge

**Dave Jones:** difference there. And you might know, what's the difference between this load you know, look, it's it's dropping with the 1K. Is that the effect of the 1K load over here? Well, it's actually not. If we actually measure that cuz you

**Dave Jones:** remember it's a divide by 21 probe as opposed to the active FET probe which was divide by 10. So, if we actually set up our cursors here and go I've set them precisely to the same ground point here.

**Dave Jones:** Our resistive probe is we're getting 55 millivolts there. So, if you get your confuser out, 55 millivolts times 21, which is our probe, 1.155 volts. And this is a looks like it's a 1.2 volt bus. So, it's like it could be

**Dave Jones:** like it's maybe 50 millivolts under but we have to measure the other one actually. So, if we adjust that, we're talking about uh 60 mV there. So, it's uh actually precisely six divisions there, and we were on uh 200 mV per

**Dave Jones:** division, so that's precisely 1.2 V. So, the resistive probe is actually measuring 50 mV less, and that could be the load the extra loading of the 1K uh load. Once you you'd have to check out the uh driving strength of the driver

**Dave Jones:** actually used in this, which is the whatever uh micro is used on the Raspberry Pi or whatever. But, because as I said, we can't actually put in a a actual uh ratio, it doesn't let us put in our own uh user-defined value. It

**Dave Jones:** only does um you know, these fixed ones. But, if it did do that, um then we could actually get, you know, well well we've we've measured it. We see that it's basically 50 mV under. So, that could be

**Dave Jones:** like an extra 50 mV uh drop caused by the loading of the probe. That's what it seems to be the case. But, once again, this isn't exactly a uh you know, a really proper set up controlled experiment. But, possible, and it's kind

**Dave Jones:** of like, you know, the sort of uh value that I'd expect. But, you can definitely see the loading there. And by the way, no, this is not just a uh like a freak uh capture where now you know, the bus

**Dave Jones:** did something different than before. This happens every single time. No matter how many times I capture this, um the 1K probe is definitely totally different to the uh active FET probe here. And you can see, obviously, the bus was floating there,

**Dave Jones:** and then it went boom, no. I'm going to go actively low. Next up, quite a common uh requirement in electronics is to look at current waveforms, not just measure it with your multimeter, but you know, really see the

**Dave Jones:** waveform, what it's like. And this is where a current probe comes in. In particular, one of these clamp current probes, which have a Hall effect uh sensor and a core which just clamps right so you put your wire through there

**Dave Jones:** and you can measure your current simply and easily because of course if you try and use your regular oscilloscope probe, okay, how do you measure the current? Well, you can put a current shunt into your circuit of course or you could design in

**Dave Jones:** a current shunt into your circuit. That's relatively a common but then of course you got the grounding issues. Sure you can use a differential probe but differential probes are like designed for like high voltages. They're not designed for low voltages

**Dave Jones:** across current shunts so you know pretty useless there. So you'd need like a super expensive multi-thousand dollar differential high bandwidth like low voltage high bandwidth probe to actually do it. Well, bugger that. Yeah, a current This is where the current

**Dave Jones:** probe comes in. You can just put a loop of wire through. It's not always convenient of course because well, if you want to measure current in a circuit, I'll show you another solution for that up next but if you've got like

**Dave Jones:** a wire available then a current clamp like this is absolutely fantastic. So there are a couple of downsides and you've got to have like a wire accessible to put your clamp probe through like this. B is that they're

**Dave Jones:** usually only designed for higher currents like in this Mixig one here the CP2100B which I see and sell on the EV blog store by the way. It's awesome value for money. It has like only a 10 amp and 100 amp

**Dave Jones:** range and you can't really get a huge amount better than that unless you go like really exotic expensive. So they're not for low current measurements. So let's say you wanted to measure the mains current consumption of a complex

**Dave Jones:** product like this that either you own or you're developing or whatever. Well, that's actually quite difficult and you know you've got to get into the power supply and you've got to somehow like maybe get a loop through there or you've

**Dave Jones:** got to lay install a current shunt and use some isolated and high voltage amplifier. It gets a bit you know, hairs on the back of your neck start going up but in this case it's easy. There's our mains input cable for this.

**Dave Jones:** There's our brown active wire and we simply clamp around that. Bingo. That is our current waveform for this oscilloscope. As you can see, uh pretty poor power factor of course, you know, not terrific. And the good thing is most

**Dave Jones:** oscilloscopes will have support for current probes. So, if I call up uh the channel one menu here and we just go into probe like this and I units um you know, any good scope these days will have volts and amps. So,

**Dave Jones:** that's why I was able to have 200 milliamps. If you're paying attention you would notice that 200 milliamps per division. So, this has support for current probes. And of course you can set just like uh the ratio of your

**Dave Jones:** voltage probe, you can set the ratio of your current probe. And of course you set that to match the value on the front here. Once you've done that, bingo, it's calibrated. Bob's your uncle. You can measure that's our

**Dave Jones:** mains waveform for this scope. Brilliant. Try and get that that simply any other way. It's just no. So, you can now get these for like a couple hundred bucks with like 2 MHz bandwidth isn't too shabby, okay? The

**Dave Jones:** lower cost version of this does like 700 kHz or something. So, unless you go for some exotic expensive like you know, Tektronix one manufactured by gray-bearded uh nude virgins that might have you know, 50 or 100 MHz bandwidth

**Dave Jones:** or something like that, then you know, they are fairly bandwidth limited but good enough for most switch mode power supply stuff. So, yeah, current clamp probes. Highly recommend you get one, they're great. Next up we've got our most unusual probe

**Dave Jones:** on this list and it's the positional current probe. It's unusual because well, as As as I know, please correct me in the comments, but only one manufacturer in the world makes this and it's the Aim TTI I Prober 520. And if

**Dave Jones:** you've been watching, I did this a review back in this back in 2012. So, yeah, it's been around for a while, but still nobody else has done anything. Now, you remember before when I said with those clamp current probes, you've

**Dave Jones:** got to have a wire available. You either got to have like a wire as part of a harness or you've got to break into your PCB and actually wire in a big loop of wire so that you can get the big current

**Dave Jones:** probe head over it and things like that. Well, what if you don't want to do that or you can't do that for whatever reason? Well, this is where the positional current probe comes in. With this, it has a magnetic sensing head on

**Dave Jones:** here that is as per its name a positional current probe. All you've got to do is put your probe over a trace on your PCB and it can measure the current flowing through it. And I've done a whole review of this and I'll link it

**Dave Jones:** in, but basically it's got a calibrator in there. I'm not sure if you can see that. Uh there's a little trace in there. Okay, there's a little PCB trace. Okay, at the moment it's basically zero like this. If I put it in there, I've

**Dave Jones:** got it to generate an AC current. I can't remember how much, you know, it's I don't know, 50 milliamps or something throw it flowing through it. If I put that there, bingo. Look at that. There's current flowing through that trace, an

**Dave Jones:** AC current. And if I turn it, if I rotate it like this, this is why it's called a positional current probe cuz it depends on the rotational position of the head. If I put it in this axis to

**Dave Jones:** the trace we're trying to measure, it measures basically nothing. But, you rotate it like that and you get the full current Yeah, you can measure the current flowing through the trace. It's brilliant. There's nothing else on the market like it. So, if you need

**Dave Jones:** something like this, you need it. Now, its bandwidth is actually not too bad. It's better than the current probe we saw before. It's actually 5 MHz, but it has You can actually set the bandwidth down to 500k or even 2 Hz down here and

**Dave Jones:** you can adjust the trace position up and down on your scope and also the sensitivity. And it's got three different modes. One is wire, comes with this ferrite clamp you put on there and it works just like a current probe. So that

**Dave Jones:** actually contains the magnetic field in there and you're in wire mode. So that makes it act like just exactly like a current clamp probe. And I'll do exactly the same thing I did before as measuring this oscilloscope waveform and bingo.

**Dave Jones:** There it is. It's exactly waveform and you can calibrate the thing. The only disadvantage is it is a bit more like dependent upon where the wire is in there. So if I move it like that you can see the amplitude does change a bit. So

**Dave Jones:** it's not quite as accurate as a proper current clamp probe but you know, it it does a reasonably good job. And the next mode is the PCB trace mode that we actually saw. So you know, when the current flows through the trace there.

**Dave Jones:** And here's where you have to adjust the sensitivity and it's a little bit how you're doing. It's not like it allows you to see the waveform but actually getting it calibrated, that's much trickier. But the value in this is actually being able

**Dave Jones:** to see the actual waveform. You don't nece- the same with most current probes. You just want to see the waveform. You don't really care too much about the absolute accuracy of it. And the final mode is magnetic fields and you can

**Dave Jones:** measure those directly in microtesla. So if we go to the menu here we can just have a quick whiz at it. Yeah, as I said like a DC to 5 MHz. Like the noise equivalent in a toroid, 6 milliamps RMS.

**Dave Jones:** So it's not for you know, really low current measurements. Just like most magnetic current probes. And then magnetic field measurement scale 250 microtesla, 200 amps per meter per volt output. And in wire mode plus minus 10 milliamps to plus minus 10 amps. And of

**Dave Jones:** course it's basically isolated. So you can actually stick this thing right into the guts of a switch mode power supply. You know, it does have like bare wire voltages and cat ratings and stuff like that, but you know, like look at it,

**Dave Jones:** right? You can your hands all the way back here. Stick this right right up the clacker I inside, you know, down through the transformers and all the filter caps and all the heat sinks alive heat sinks and everything else. Stick them inside

**Dave Jones:** your power supply and safe as. And you can see here that, you know, for like piece of sensitivity, it's not completely linear like, but good enough for Australia. At least you get to see the waveform. Now, I couldn't be asked

**Dave Jones:** to set up another like experiment just to demo this. I've done a demo of where you can actually use this to trace higher frequency signals through a PCB power plane. You can do lots of other cool stuff like that. So, I'll just

**Dave Jones:** steal the video and the segment from my previous video. Here it is now. Linked in down below. Hi. It's product review time. Now, what I'm going to do is try and attempt to trace out a real ground current on a PCB like this. And as you

**Dave Jones:** can see, there's a split PCB plane in there. So, I've got my current going in over here, coming out over here, and it's got to go through that tiny little trace down in there. That's the only way that it gets from there through to

**Dave Jones:** there. There's the split ground plane there. So, we shouldn't get any current flow around in here. We shouldn't get any current flow in the ground fill down in there. We shouldn't get any current flow down in here. We should just get

**Dave Jones:** the current flowing through there through that tiny little trace there, if you can see it, and down around through to here. Now, I'm using a 1 kHz signal here, but it would work for DC as well. But, just remember

**Dave Jones:** you've got the Earth's magnetic field as well. So, when you move this thing around, you know, where you you're going to get an offset uh shift like that. So, just be careful, but here we go. There's our reference waveform, and we don't

**Dave Jones:** have to worry about the calibration on this pot at all because we don't care about the magnitude. We're just tracing currents here on this board, part of the ground plane, and you'll see we've got absolutely nothing there at all. We can change the

**Dave Jones:** orientation, and we get that offset, but there's no 1 kHz signal. There's nothing flowing through that part the ground plane, but here there most certainly is. Once again, if we get the wrong orientation, it's going to vanish like

**Dave Jones:** that if we hold it vertical, but if we keep the correct orientation according to the magnetic field of how it should flow, then bingo, we still get the waveform. See the currents going both sides of that hole there? Here like

**Dave Jones:** this. And once again, it does some of it does flow down around there like that, but the majority of it's going to flow through this top part here. And it's going to flow up here, and you'll notice that it won't flow down

**Dave Jones:** into that little fill, that little void down in there. There is no current flow there at all. So, you can see the current flowing through here. And likewise, there's going to be nothing flowing down here. They're electrically shorted together, but there's no current

**Dave Jones:** flow. And this is a great visualization uh learning tool as well as a real practical tool for determining where your currents are flowing in your ground planes. And there it is flowing down there. And it's look, it's not going

**Dave Jones:** down this little bit down here. Very little down there at all, tiny little bit flowing through those two pads there. But as you can see, it's all going to flow through that trace there, that one tiny little trace which connects the two

**Dave Jones:** split ground planes. And it's going to flow up here, and all the way over to there. And look, down here, there's nothing in this little void down here. So, right that out. There's no current flow through any of this

**Dave Jones:** stuff down here because that's where it flows, through that bottleneck there, around here, and down into there. So, yes, this thing isn't cheap, but it's unique, and there's nothing like it. So, I'd recommend this if you're doing like

**Dave Jones:** lots of mains big switch mode power supply design and stuff like this. Just being able to get in there and see waveforms just without around. It's worth its weight in gold. And the last probe, we've got the EMC probe. Of

**Dave Jones:** course, I've done like what, half a dozen videos on using EMC probes. So, like yeah, I've already spent enough time on this video. I won't go through it again. I've even done a video on how to make your own one for like what what

**Dave Jones:** was it, 10 bucks or something like that. So, 10, 15 dollars or 20 bucks. Yeah, you can make your own. Of course, you get magnetic ones like this, which I actually have the loop, and you get them in different loop

**Dave Jones:** sizes, and this one here actually has a loop in there. So, these are called H field or magnetic field probes, and then this one here is called an E field or electric field probe. And well, I've done very interesting videos on

**Dave Jones:** differences between magnetic, and I've demonstrated on the magnetic and electric fields and things like that. But, great for doing EMC, electromagnetic conformity, pre-compliance for your products. And generally, the output levels of these are very low. So, you use a wideband RF

**Dave Jones:** signal amplifier. In this case, this goes up to 3 gig from Tech Box. And but, you can as I said, like you can just make your own out of a bit of coax. It's basically just a bit of coax in there,

**Dave Jones:** and that's it. Um and you can buy these amplifiers for like 10 bucks on eBay. Well, not this one, but like a little bare board one. And Bob's your uncle, you've got yourself a EMC pre-compliance. Very handy for like tracing down EMC faults

**Dave Jones:** and things like that. Once again, I'm not going to set up experiments again just to demo this. I'll link in my EMC videos, but that is another different type of probe. Highly recommended you should have one just because like just

**Dave Jones:** make one yourself. I mean, this set costs, you know, a couple hundred bucks, and it comes with like the calibration charts and everything else. And which is fine, but these do-it-yourself ones, once again, for 10 20 bucks just like

**Dave Jones:** your Here it is. Just like your transmission line resistive probe down here, I'd like why not? Just have a couple of these made up for when you need them. So, there you go. I hope you enjoyed this little two-part series on looking at all

**Dave Jones:** of the different types of probes available for oscilloscopes. There might be other obscure ones out there. Please leave it in the comments down below if you think I've forgotten something important or something exotic like this, you know, I prober thing. There are

**Dave Jones:** other I'm sure there are other exotic oscilloscope probes out there, but I think I've pretty much covered, you know, all of the general ones that you're going to find or have potential use for in the future. So, yeah, you've got your times one

**Dave Jones:** times 10 switchable probe with your scope, but there's a lot more out there that allows you to do all different types of measurements under lots of different scenarios that you might encounter in electronics. So, I hope you like that, and if you found it useful,

**Dave Jones:** please give it a big thumbs up. And as always, discuss down below in the comments over on the EVblog forum. Each video has its own forum link linked in down below where everyone discusses this stuff. And of course, you can check me

**Dave Jones:** out on the other platforms where I occasionally release exclusive material not on YouTube. Hmm. Catch you next time.
