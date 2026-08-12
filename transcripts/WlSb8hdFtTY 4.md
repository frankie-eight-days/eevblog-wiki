---
video_id: WlSb8hdFtTY
title: EEVblog #1368 - Active Oscilloscope Probes COMPARED (Part 2)
url: https://www.youtube.com/watch?v=WlSb8hdFtTY
source: youtube-asr
timestamps: {"0": 0, "1": 20, "2": 33, "3": 45, "4": 60, "5": 75, "6": 98, "7": 112, "8": 128, "9": 142, "10": 163, "11": 172, "12": 186, "13": 198, "14": 214, "15": 223, "16": 236, "17": 247, "18": 257, "19": 268, "20": 283, "21": 299, "22": 313, "23": 331, "24": 339, "25": 351, "26": 364, "27": 373, "28": 389, "29": 400, "30": 413, "31": 431, "32": 452, "33": 464, "34": 473, "35": 481, "36": 490, "37": 498, "38": 509, "39": 522, "40": 537, "41": 563, "42": 571, "43": 579, "44": 590, "45": 602, "46": 616, "47": 625, "48": 637, "49": 652, "50": 666, "51": 676, "52": 689, "53": 711, "54": 721, "55": 732, "56": 742, "57": 753, "58": 764, "59": 777, "60": 790, "61": 802, "62": 813, "63": 827, "64": 837, "65": 844, "66": 854, "67": 861, "68": 873, "69": 889, "70": 900, "71": 913, "72": 921, "73": 935, "74": 948, "75": 959, "76": 973, "77": 986, "78": 1002, "79": 1011, "80": 1024, "81": 1036, "82": 1047, "83": 1056, "84": 1065, "85": 1073, "86": 1082, "87": 1099, "88": 1110, "89": 1122, "90": 1132, "91": 1145, "92": 1160, "93": 1180, "94": 1194, "95": 1204, "96": 1217, "97": 1231, "98": 1241, "99": 1255, "100": 1269, "101": 1279, "102": 1292, "103": 1302, "104": 1319, "105": 1328, "106": 1344, "107": 1362, "108": 1373, "109": 1385, "110": 1399, "111": 1412, "112": 1428, "113": 1446, "114": 1458, "115": 1470, "116": 1482, "117": 1497, "118": 1512, "119": 1530, "120": 1544, "121": 1554, "122": 1565, "123": 1576, "124": 1588, "125": 1608, "126": 1622, "127": 1639, "128": 1652, "129": 1664, "130": 1675, "131": 1685, "132": 1700, "133": 1717, "134": 1738, "135": 1750, "136": 1760, "137": 1773, "138": 1788, "139": 1806, "140": 1815, "141": 1826, "142": 1842, "143": 1854, "144": 1868, "145": 1878, "146": 1895, "147": 1907, "148": 1917, "149": 1940, "150": 1959, "151": 1972, "152": 1989, "153": 2000, "154": 2013, "155": 2021, "156": 2027, "157": 2043, "158": 2054, "159": 2065, "160": 2077, "161": 2087, "162": 2100, "163": 2110, "164": 2120, "165": 2131, "166": 2141, "167": 2153, "168": 2168, "169": 2179, "170": 2192, "171": 2199, "172": 2208, "173": 2219, "174": 2235, "175": 2243, "176": 2255, "177": 2266, "178": 2276, "179": 2289, "180": 2299, "181": 2311, "182": 2323, "183": 2346, "184": 2360, "185": 2370, "186": 2391, "187": 2402, "188": 2414, "189": 2427, "190": 2438, "191": 2450, "192": 2463, "193": 2475, "194": 2490, "195": 2505, "196": 2514, "197": 2524, "198": 2538, "199": 2546, "200": 2559, "201": 2568, "202": 2577, "203": 2591, "204": 2603, "205": 2610, "206": 2622}
---

**Dave Jones:** Hi, in the previous video, linked in at the end and down below, if you haven't seen it and you must watch it cuz this is part two. We looked at four different passive oscilloscope probes, the switchable 1 to 10 probe, the fixed times 10, the high voltage probe, and the transmission line resistive probe.

**Dave Jones:** And these were all passive probes. But now, in this video, we're going to take a look at what pretty much can be called all active probes because they contain some sort of active amplifier circuitry.

**Dave Jones:** Our first one we got is the high voltage differential probe. This is the EVblog HVP70. It's a 70 MHz high voltage differential probe. It's designed for measuring, look, 1,000 V RMS max.

**Dave Jones:** But you might think, well, this one can do 5 kV and this one only does 1,000 V. What's the difference? Well, you remember I said this is mains earth reference and I've done that video on how not to blow up your oscilloscope.

**Dave Jones:** You cannot use one of these or you can't use one of your other probes because if you hook your ground point up, that is like connecting mains earth to any point on the circuit that you connect this through and you can come a gutter and you can blow up your product, your board, whatever.

**Dave Jones:** You can even blow up your oscilloscope. You blow up your leads. You can really have a bad day. So unless the ground of your product is actually isolated from mains earth, you can't just go sticking this ground probe willy-nilly anywhere in your circuit because you can come a gutter and things like you know, mains switching power supplies or other things, they're of course mains earth reference.

**Dave Jones:** So yeah, you plug this on the wrong point and it's just going to vaporize. But what the high voltage differential probe does is let you let you safely put either the ground or the positive lead anywhere in your circuit.

**Dave Jones:** Well, as long as what the maximum here is is is 1,000 V RMS and your common mode which is connected through the ground plus minus 700 V good enough for any like you know main switch mode power supply you can just connect your probes up to anywhere and you're going to be completely safe.

**Dave Jones:** You're not going to blow up your circuit. You're not going to blow up yourself. You're not going to blow up anything. These are great high voltage differential probes. Okay, just a quick recap with Dave Cat here on what this common mode voltage actually means.

**Dave Jones:** Well, this high voltage differential probe it basically is just a differential amplifier. It's just an amplifier like this that measures the voltage difference between the positive and negative input terminals like this and then it multiplies it by amplifies it by a gain of 10 or 100 depending on where you set the switch and then it just goes out to the BNC here to your oscilloscope.

**Dave Jones:** And of course the oscilloscope is going to be mains earth reference. So what this voltage here 1,000 V RMS maximum between the two terminals here is exactly as it says.

**Dave Jones:** It says you can have up to a maximum of 1,000 V RMS or basically the linear range the measurement range plus minus 700 V between these terminals either directions.

**Dave Jones:** So good enough for like mains measurement things like that and you can get higher voltage versions of these which go much higher. I think this is actually one of the lowest voltage ones on the market with times 10 times 100 and we might explain why in a minute.

**Dave Jones:** Anyway, common mode voltage what that means is that between either of these inputs here either one positive or negative and this output it's output referenced and the output is of course going to your oscilloscope which is mains earth reference.

**Dave Jones:** So that's connected through to your mains which then could be connected back through your power point through to your product and I've done that whole video on how not to blow up your oscilloscope.

**Dave Jones:** So I won't recover all that. But basically this probe can handle up to plus minus 700 V between this is a voltage source here between either of these terminals and the output mains earth reference here.

**Dave Jones:** This is why you can pretty much for most practical circuits that are mains powered or lower voltage, you can connect your two probes up to any point in your circuit and you're not going to blow up anything.

**Dave Jones:** You're safe to measure any point in your circuit. So you can measure across you know like a shunt resistor in there or something like that to get the current waveform or whatever it is.

**Dave Jones:** Now here's a reverse engineer Dave Cadbury of a similar model to this one from the manufacturer Sapphire. This one will be exactly the same just some twite just some performance twite.

**Dave Jones:** Differences this is how these high voltage differential probes work and there's a big common misconception about these high voltage differential probes. People think that they're actually isolated that the inputs are somehow you know transformer or other isolated from the input.

**Dave Jones:** Well, that is not the case. All these things do is actually contain large value input resistors. In this case, it actually tells you down here. Read it. 4 meg each side to ground and 5.5 puff and that's exactly what you get.

**Dave Jones:** You get four 1 meg resistors to ground. Here's the ground terminal. Here is the output reference. I haven't drawn it but output ground over here like this and this comes from my reverse engineering drawing so I'll link that one in but basically yeah, that is connected through to here.

**Dave Jones:** So it's look it there it is. It's connected right through 4 meg resistor and they've got a low value down here 25 so it's just a resistor divider in each leg and then they've got a FET differential amplifier here and some extra gain stage times 10 times 100 selected and that's it.

**Dave Jones:** That's all that's inside of one of these things but because they've got such high value resistors, you can plug them anywhere in your circuit and it's not going to cause a problem.

**Dave Jones:** But of course, it could potentially load down your circuit if it's a really high impedance circuit And course but that's the same with any probe. These things don't really perform as good as a proper oscilloscope one.

**Dave Jones:** This is only a 70 MHz bandwidth and with these long leads on the input, okay, you've got to twist them to get even half decent performance. And yeah, they're just not as good a performance as proper oscilloscope probes, but they're incredibly safe.

**Dave Jones:** And that's the reason that you want to use one of these. And you can probe any point in your circuit using a ground reference oscilloscope. They just uh like they they can't be beat.

**Dave Jones:** But the downside is is that because they have to have such large resistor divider ratios in order to be safe, then well, they're not great for low level measurements, which is why you won't find a high voltage which is why they're called high voltage differential probes.

**Dave Jones:** You won't find a Well, there are some low voltage differential probes, but like they're generally um high voltage because they have to have a huge divider ratio like that.

**Dave Jones:** And these are either battery powered in this case of this one four AA batteries in the back or you can power them because the power is output reference, you can actually power them from the USB port on your scope here if you've got an adapter cable.

**Dave Jones:** And our next probe, guaranteed to get every engineer all excited. Oh, it's the active FET probe. And they always come in impressive cases like this and this and this.

**Dave Jones:** Right, you never just get like a little like probe in a packet, whatever. No, they always come in beautiful cases like these. Let's take a look at them. So, here's a very typical active probe or the active FET probe or just FET probe because they've all got FETs right at the input here that actually amplify the signal before it comes in.

**Dave Jones:** So, they have active amplifier electronics inside the head as opposed to your passive probe here, which is just a basically a bit of a a resistor and a bit of coax, and the amplifier is inside the scope.

**Dave Jones:** Well, in this case, the amplifier is up here, which means they they have to actually be supplied by power. And it's very common for them to actually be powered from the oscilloscope under test.

**Dave Jones:** And look at these all lovely little pogo pins. And you usually buy them from uh the manufacturer of the oscilloscope cuz they've got their own interface. This one is your Agilent uh Keysight.

**Dave Jones:** So, those probes uh not only give it power, but they also, you know, tell it what type of probe it is and and things like that. Your signal doesn't actually come out on these pins.

**Dave Jones:** This is just power and um other data. Your signal, of course, goes into your input to your scope. So, it's just that's a regular BNC, but it just plugs in.

**Dave Jones:** It's all captive, and they usually have a little lever in there to clamp on the front of your scope. So, these things are usually very pricey, you know, they start in the four-digit category and uh go up to like five digits.

**Dave Jones:** And this one here is a two-gig uh bandwidth probe. Uh 10:1 uh divider ratio. 1 meg uh input impedance. And this uh Siglent one here, active probe, it's a it's 1 gig uh with 1 megohm and uh 1.2 picofarads.

**Dave Jones:** Uh but, you might think, "Well, okay, this is 1 gig. Well, so is this. What's the difference?" Well, the difference is, remember, this is like practically the world's best passive probe, 3.9 pF.

**Dave Jones:** This one, 1.2 pF. And that's the difference. You remember our formula before, capacitance is the thing that matters at high frequency. And in the case of this uh Siglent uh active uh probe compared to this Tektronix one, both are 1 gig rated probes, but because it's only 1.2 uh pF, it's 132 ohms at 1 gig, whereas the passive probe is 40 ohms at 1 gig.

**Dave Jones:** So, that can make a heck of a difference to the signal that you're actually measuring. That load that load is going on the line that you're trying to probe.

**Dave Jones:** So, the lower the capacitance, the less you're going to load your line. But, if you are talking uh DC, then the passive probe still better. That's 10 mega DC.

**Dave Jones:** These are only a meg. So, you'd use an active FET probe over your passive probe when a signal integrity at high frequency really matters. Well, A, these can go higher.

**Dave Jones:** This is actually the fastest passive tender one passive probe you can get at 10 meg. This is And as I said, this thing with a resistor will, you know, if you build it right, will actually outperform this.

**Dave Jones:** And these can actually go up to 10 gig. So, yeah, anyway, so the only solution basically for above 1 gig measurement is either an active FET probe or a resistive probe.

**Dave Jones:** That's it. And if you're wondering, this Agilent one is one puff input capacitance. And this one here, haven't measured it, but it'll like it probably on be on par.

**Dave Jones:** Something like that. In the order of a puff, half a puff maybe. So, the great thing about active FET probes is you they can actually go beyond 10 gig and beyond the performance of a simple resistive probe like this.

**Dave Jones:** So, if you're on the bleeding edge of measurement, you're you're really going to be wanting an active FET probe. So, pretty much as a ballpark, maybe anything over 500 meg, you want to either be using active FET probe or a properly built and characterized resistive probe.

**Dave Jones:** And like it can cost you more money to actually characterize this than to simply buy the already characterized active FET probe. And basically, these single-ended active probes give about stop at a couple of gigahertz.

**Dave Jones:** Anything over that, then you start talking a fully differential probe, but not high voltage like we looked at before. These would be low voltage differential probes, high speed, low voltage.

**Dave Jones:** But, the one downside with these things is Murphy can get really expensive. Like these probes can cost thousands of dollars, even into the six-digit range. And their huge Achilles heel is the maximum input voltage.

**Dave Jones:** In this case, max input 20 volts peak. Okay? Seriously, you go over that and this probe will blow up. You'll probably find eBay's filled with like all this FET probe "Yeah, sold as is." I would not be buying a sold as is FET probe off eBay.

**Dave Jones:** Just saying. We've got one from Caltech Electronics here. This one's a little bit more robust. We're talking 40 volts peak here. It's a 1.2 gig probe. Once again, 10 to 1.

**Dave Jones:** This one's higher input capacitance though, three puff. But, as you can see, this one you can get like generic ones. You don't have to get these ones designed for your specific scope.

**Dave Jones:** You can get these cheaper ones that just plug into your like any scope and they're just actively powered once again from just the USB port on the front of your scope.

**Dave Jones:** Nice. And as I showed before, these things always come with like all these accessories. Let's take a look at them cuz they're very interesting. So, these are the ones that come with the Caltech probes.

**Dave Jones:** You got beautiful little ultra tiny mini grabbers there. You've got little ground and probe pins like that, spare ones cuz you're going to be using them all the time.

**Dave Jones:** Plus, you've got like little pins like that you that you can plug into headers. And often on your designs, when you if you know you're going to be probing like you know a really serious designs, maybe on a prototype board, you don't necessarily need it on a production layout.

**Dave Jones:** But, on a prototype board, you're trying to get it working. You're measuring your high speed DDR bus or whatever. Then, you might have dedicated test points on there, even dedicated connectors for these high speed probes.

**Dave Jones:** And the Siglent ones, once again, you get all these like spare tips cuz you're going to be going through them like there's no tomorrow. You might even want to directly solder the tips into your circuit so that you can physically remove your probes.

**Dave Jones:** The most interesting kit comes with the uh Keysight one. Once again, you've got a little tube with all the uh little pins in there. They just don't give you many, do they?

**Dave Jones:** A bit of a tight ass. Real expensive probe. You get ultra tiny mini grabbers, once again. Like, these things are just super super tiny. And then you like plug into there and give you all sorts of other little uh adapters like that.

**Dave Jones:** Um and the most interesting thing is they give you uh copper pads like this and they actually give you a bit of a chart here on you know, some of the different uh probe connection techniques.

**Dave Jones:** And this is not the video to go into really high-frequency uh probing techniques, of course. But you can Look, you can plug directly into the head with some long leads like that.

**Dave Jones:** And that'll give like, you know, 500 meg bandwidth here, they're saying. Or uh you know, you can get a rigid probe tip with offset ground like that. So, it plugs in.

**Dave Jones:** And I love this uh Keysight head. It's got little LEDs on there that just light up it so you can see where you're actually plugging your probe into. Very nice.

**Dave Jones:** And then you've got a spring tip with ground blade like this. Uh and that'll give you like 2 gig bandwidth. And then you've got uh a copper pad which you can solder onto your circuit and that will give you like a flexible ground point.

**Dave Jones:** So, you know, often it's very difficult to apply pressure to like both of these points at the same time without one of them sliding around. Well, if you solder in like a large ground pad like like with that copper tape that they uh supply, then you know, you don't have to worry about your ground probes probes sliding around.

**Dave Jones:** Or you do have to keep an eye on it cuz Murphy's sure to slide off and short out one of your other pin sitting on your expensive $100,000 prototype board.

**Dave Jones:** Trust me, I've worked on $100,000 prototype boards. And if you blew that up, you Yeah, you're going to be having a bad day. But once again, you know, that might be a slightly reduced bandwidth to you know, this technique over here which is going to provide a lower inductance uh path.

**Dave Jones:** So, it's going to you know, you're going to get better performance out of it, something like that. And then you've just got, you know, if you want to put just pin headers on your board for various uh test signals.

**Dave Jones:** and then little short cables which run over and just plug into your probe tip. So all these different solutions for probing and you can even invent your own and as I said a lot of designers will solder on like like coax connectors directly onto the board and things like that.

**Dave Jones:** So you can plug on your own probes, your own resistive probes or active FET probes or whatever it is you're doing. So active uh FET probes, you can think of those as the Rolls-Royce of oscilloscope probes really.

**Dave Jones:** They're very nice but as with certain, you know, roll your own with a bit of RG174 coax and well you can get similar performance if you do it well enough but oh yeah, these can't be beat if you got the money.

**Dave Jones:** And these probes will usually require 50 ohm termination on your scope although this Cal Test one here, it actually well it comes with a 50 ohm terminator. Look at that, 2 gig 50 ohm in series in line terminator 2 watts.

**Dave Jones:** Oh, that's very nice. But this one actually lets you use it with a 1 meg input impedance scope just say no 50 ohm termination and it it gives you an actual attenuation setting of five times.

**Dave Jones:** So that's, you know, better for like low signal measurements. Nice. Okay, let's give you a probing example here. We've got a Raspberry Pi 3 for those playing along at home and we're going to probe one of the memory pins on the bottom here.

**Dave Jones:** I don't care which one. I've just picked one at random. We're getting a signal on it. So I'm using the 2 GHz active probe here the N2796 overkill for what we're doing.

**Dave Jones:** Well, overkill for this scope anyway because this is a 500 MHz bandwidth scope. So this active FET probe more than good enough for measuring the bandwidth that we got here.

**Dave Jones:** So I'll use this long lead here for my ground. I'll put it on the ground pin of the connector there cuz that's just very convenient. For those who care about such things, you You actually see what uh, I'm probing.

**Dave Jones:** Where is it? I think it's there. Geez, I can barely see that. This is where, you know, magnification, uh, comes in. Okay, I'm probing a point there. I don't know what it is.

**Dave Jones:** I don't care. There it is. There's our signal. It's made up of a whole bunch of, uh, stuff, but basically, uh, you can see, look, it's got some undershoot here.

**Dave Jones:** It's got a little bit of ringing there. It's got a little bit of ringing there. I'm going to hazard a guess that that's going to be due to our, uh, long ground lead there, right?

**Dave Jones:** So, that is our thing. But, we've got actually higher frequency stuff in here. Look at this. Oh, I just happened to capture one there. Look at this. Goes down, up.

**Dave Jones:** We're at, uh, what, 10 nanoseconds per division. We're almost as fast as we can get here, uh, with this, uh, scope. But, this actually does have some really fast, uh, pulses in here.

**Dave Jones:** So, something, you know, something you know, the bus is switching. It's doing whatever. I don't know what, uh, point we're probing. Check that out, right? There you go. Because that looks very sinusoidal, we're talking about that's our sin x on x interpolation there.

**Dave Jones:** So, this is like, sort of Once you see that, you know, okay, we're beyond the bandwidth of our scope here. These signals are just too fast. But, anyway, let's just go back to here.

**Dave Jones:** Okay, so, we'll just try and capture that sort of like the most frequent one there. There it is. Got it. Okay, so, I'll store that. All right, so, what I'm going to do now is I'm going to actually, uh, change the ground into this.

**Dave Jones:** Instead of having this longer lead, I'm going to go for one of the shorter, uh, little adapter ground adapter pins we've got in there. And it looks like there's a little bypass cap.

**Dave Jones:** I've determined that this right hand side is the ground. So, that's very convenient and because that's right next to the point that I want to test. Otherwise, as I, uh, showed you before that you might have to, uh, like install one of those copper pads or something.

**Dave Jones:** You might have to, like, scrape away some of the ground here or something like that and maybe put the copper tape over the top of the chip or something like that or you'd have to scrape away some other ground point somewhere or you know, soldering a little uh contact loop pin or something like that.

**Dave Jones:** So, here it is. I've got my little adapter. Careful cuz you can stab yourself with these little bastards. There we go. So, we have this little now ground pin which can sort of like, you know, pivot around like that and anyway, that will make better contact and this will be a higher frequency probe because it's a shorter inductive path.

**Dave Jones:** So, let's try that. We'll require the tongue at the right angle and probably some magnification here. Okay, I've got my ground point and I've got my probe point. Pan up.

**Dave Jones:** Pan up. Okay, let's have a look. I've changed my uh digitizer. Definitely getting 5 gig samples uh per second and I saved my reference waveform. So, let's single shot capture that.

**Dave Jones:** See if we can get it. No. There we go. Got it. Now, I can actually uh adjust that waveform there to show you. There you go. So, the orange one I've got there is the reference waveform and this new yellow one is the one that we just probed.

**Dave Jones:** And there you go. It is like it's of course like the same wave shape. You can see it's got the uh longer ground lead one, the orange one, has some extra undershoot there and comes back and takes more time to come back up like that.

**Dave Jones:** And the one up here got some extra wiggle wiggle wiggle year on the top there, some overshoot. And um so, you know, there are differences in probing right there.

**Dave Jones:** But at the moment, this is the loading of the line with a one picofarad, one puff active probe which costs a couple of thousand dollars. Okay, now I'm going to use my 500 megahertz uh passive probe here.

**Dave Jones:** It's the N28 uh 43. It's 11 picofarads. Okay? And yes, I've compensated this. You compensate it with your probe compensation on the front. So, everything's hunky-dory. I'm using my low inductance, high frequency uh ground probe attachment.

**Dave Jones:** So, that's equivalent uh to what we had before. So, um it we should get and because we've only got a 500 bandwidth scope uh here, then the bandwidth of the probe isn't really going to matter that much.

**Dave Jones:** Oh, my tongue at the right angle. And probe this. I think I got it. But, here's the interesting thing. I've changed uh the reference waveform to my uh low inductance uh short ground one before.

**Dave Jones:** So, the orange one is the best we could get with our active uh probe. So, the exact same ground point, basically the same ground length, and you can see that well, you know, our wave shape's the same, but look.

**Dave Jones:** Look at this. Um it's a much higher level down here. Okay, this is uh 200 mV uh per division. So, it's like, you know, 50-odd mV higher there. And it's actually lower down here, our yellow waveform there.

**Dave Jones:** So, you know, all although we can see like the wave shape and everything up here, it's like when the bus is loaded differently, cuz that's what this little uh you know, ramp up here is going here.

**Dave Jones:** I don't know the architecture of the Raspberry Pi. It it doesn't matter. But, I know there's something happening there with there. And down here, we're actually seeing a larger drop across the uh bus here, which is interesting, isn't it?

**Dave Jones:** I it you know, there's significant differences here. This is wasn't the exact example I wanted to show. I just like it's a random example, but you can see the difference here between a 500 meg passive probe and and effectively a because of the bandwidth of the oscilloscope of 500 meg active probe.

**Dave Jones:** They load down the circuit differently. And I know you want to see it. Okay, let's compare Dave's dodgy um homemade uh resistive probe here with a 1K resistor in the tip.

**Dave Jones:** We'll give that a whirl. Got a 50 ohm uh terminate that. But, scope can do that. No worries. Tongue at the right angle. Tongue the right angle. Fix that.

**Dave Jones:** Oh! Check this out. This is absolutely fantastic. Now, what we've got here, the orange waveform, of course, is our reference active FET waveform. That's a $2,500 active FET probe.

**Dave Jones:** Yes, it is compensated because you do still have to compensate them, and it stores it internally cuz it knows the serial number of the probe, etc. And the yellow one is Dave's do-it-yourself couple of buck resistive probe.

**Dave Jones:** Look at this. What's going on here? Well, it's obvious that what's happening at this point right here is that the bus is actually going open or something. I don't know the exact architecture of what's, you know, the pin I'm actually probing.

**Dave Jones:** It doesn't matter, right? It's like it's going open, and because the probe is 1 meg DC resistance, look at that, it's basically it's not going to discharge. Maybe if we got like a longer time period, it'd eventually do a similar like eventually discharge or whatever.

**Dave Jones:** But you see that the bus is actively changed, but because we're now loading this bus down with a 1K resistor or a 1.05K resistor cuz we've got the 50-ohm terminator as well, it boom!

**Dave Jones:** This is an This looks like for all the world, and it is an RC discharge curve. So, there you go. What's that, you know, 10 nanoseconds per division? I don't You can work that out, whatever, for those playing along at home.

**Dave Jones:** But you can see how the resistive probe actually completely changes the circuit that you're actually measuring. So, sure, let the signal integrity is excellent. Let's Let's take a look at this, actually.

**Dave Jones:** If you have a look at the bottom here, you can see that both of them undershoot almost exactly the same. But you remember how I said that the resistive probe can actually be more tolerant of longer ground leads.

**Dave Jones:** I think they're both about the same length. I think they're practically near identical. Remember how I said it can be more tolerant on these than active FET probes. This might be an example of this cuz this is not this is not some controlled experiment.

**Dave Jones:** This is just something I slapped together willy-nilly and this is the result that we actually got. This is fascinating, right? They both undershoot exactly the same but the active FET probe, the orange one, actually look it overshoots again when and it takes much longer to recover than the resistive probe.

**Dave Jones:** Look at that. So, this could be an example of where this cheap ass do-it-yourself resistive probe is actually outperforming this $2,500 active FET probe in terms of signal integrity.

**Dave Jones:** But once again, this is not a completely controlled experiment. But this is what you can actually get. But of course, the limitation is that it loads it down much more.

**Dave Jones:** 1K as opposed to 1 meg, right? There's a huge difference there. And you might know, what's the difference between this load you know, look, it's it's dropping with the 1K.

**Dave Jones:** Is that the effect of the 1K load over here? Well, it's actually not. If we actually measure that cuz you remember it's a divide by 21 probe as opposed to the active FET probe which was divide by 10.

**Dave Jones:** So, if we actually set up our cursors here and go I've set them precisely to the same ground point here. Our resistive probe is we're getting 55 millivolts there.

**Dave Jones:** So, if you get your confuser out, 55 millivolts times 21, which is our probe, 1.155 volts. And this is a looks like it's a 1.2 volt bus. So, it's like it could be like it's maybe 50 millivolts under but we have to measure the other one actually.

**Dave Jones:** So, if we adjust that, we're talking about uh 60 mV there. So, it's uh actually precisely six divisions there, and we were on uh 200 mV per division, so that's precisely 1.2 V.

**Dave Jones:** So, the resistive probe is actually measuring 50 mV less, and that could be the load the extra loading of the 1K uh load. Once you you'd have to check out the uh driving strength of the driver actually used in this, which is the whatever uh micro is used on the Raspberry Pi or whatever.

**Dave Jones:** But, because as I said, we can't actually put in a a actual uh ratio, it doesn't let us put in our own uh user-defined value. It only does um you know, these fixed ones.

**Dave Jones:** But, if it did do that, um then we could actually get, you know, well well we've we've measured it. We see that it's basically 50 mV under. So, that could be like an extra 50 mV uh drop caused by the loading of the probe.

**Dave Jones:** That's what it seems to be the case. But, once again, this isn't exactly a uh you know, a really proper set up controlled experiment. But, possible, and it's kind of like, you know, the sort of uh value that I'd expect.

**Dave Jones:** But, you can definitely see the loading there. And by the way, no, this is not just a uh like a freak uh capture where now you know, the bus did something different than before.

**Dave Jones:** This happens every single time. No matter how many times I capture this, um the 1K probe is definitely totally different to the uh active FET probe here. And you can see, obviously, the bus was floating there, and then it went boom, no.

**Dave Jones:** I'm going to go actively low. Next up, quite a common uh requirement in electronics is to look at current waveforms, not just measure it with your multimeter, but you know, really see the waveform, what it's like.

**Dave Jones:** And this is where a current probe comes in. In particular, one of these clamp current probes, which have a Hall effect uh sensor and a core which just clamps right so you put your wire through there and you can measure your current simply and easily because of course if you try and use your regular oscilloscope probe, okay, how do you measure the current?

**Dave Jones:** Well, you can put a current shunt into your circuit of course or you could design in a current shunt into your circuit. That's relatively a common but then of course you got the grounding issues.

**Dave Jones:** Sure you can use a differential probe but differential probes are like designed for like high voltages. They're not designed for low voltages across current shunts so you know pretty useless there.

**Dave Jones:** So you'd need like a super expensive multi-thousand dollar differential high bandwidth like low voltage high bandwidth probe to actually do it. Well, bugger that. Yeah, a current This is where the current probe comes in.

**Dave Jones:** You can just put a loop of wire through. It's not always convenient of course because well, if you want to measure current in a circuit, I'll show you another solution for that up next but if you've got like a wire available then a current clamp like this is absolutely fantastic.

**Dave Jones:** So there are a couple of downsides and you've got to have like a wire accessible to put your clamp probe through like this. B is that they're usually only designed for higher currents like in this Mixig one here the CP2100B which I see and sell on the EV blog store by the way.

**Dave Jones:** It's awesome value for money. It has like only a 10 amp and 100 amp range and you can't really get a huge amount better than that unless you go like really exotic expensive.

**Dave Jones:** So they're not for low current measurements. So let's say you wanted to measure the mains current consumption of a complex product like this that either you own or you're developing or whatever.

**Dave Jones:** Well, that's actually quite difficult and you know you've got to get into the power supply and you've got to somehow like maybe get a loop through there or you've got to lay install a current shunt and use some isolated and high voltage amplifier.

**Dave Jones:** It gets a bit you know, hairs on the back of your neck start going up but in this case it's easy. There's our mains input cable for this. There's our brown active wire and we simply clamp around that.

**Dave Jones:** Bingo. That is our current waveform for this oscilloscope. As you can see, uh pretty poor power factor of course, you know, not terrific. And the good thing is most oscilloscopes will have support for current probes.

**Dave Jones:** So, if I call up uh the channel one menu here and we just go into probe like this and I units um you know, any good scope these days will have volts and amps.

**Dave Jones:** So, that's why I was able to have 200 milliamps. If you're paying attention you would notice that 200 milliamps per division. So, this has support for current probes. And of course you can set just like uh the ratio of your voltage probe, you can set the ratio of your current probe.

**Dave Jones:** And of course you set that to match the value on the front here. Once you've done that, bingo, it's calibrated. Bob's your uncle. You can measure that's our mains waveform for this scope.

**Dave Jones:** Brilliant. Try and get that that simply any other way. It's just no. So, you can now get these for like a couple hundred bucks with like 2 MHz bandwidth isn't too shabby, okay?

**Dave Jones:** The lower cost version of this does like 700 kHz or something. So, unless you go for some exotic expensive like you know, Tektronix one manufactured by gray-bearded uh nude virgins that might have you know, 50 or 100 MHz bandwidth or something like that, then you know, they are fairly bandwidth limited but good enough for most switch mode power supply stuff.

**Dave Jones:** So, yeah, current clamp probes. Highly recommend you get one, they're great. Next up we've got our most unusual probe on this list and it's the positional current probe. It's unusual because well, as As as I know, please correct me in the comments, but only one manufacturer in the world makes this and it's the Aim TTI I Prober 520.

**Dave Jones:** And if you've been watching, I did this a review back in this back in 2012. So, yeah, it's been around for a while, but still nobody else has done anything.

**Dave Jones:** Now, you remember before when I said with those clamp current probes, you've got to have a wire available. You either got to have like a wire as part of a harness or you've got to break into your PCB and actually wire in a big loop of wire so that you can get the big current probe head over it and things like that.

**Dave Jones:** Well, what if you don't want to do that or you can't do that for whatever reason? Well, this is where the positional current probe comes in. With this, it has a magnetic sensing head on here that is as per its name a positional current probe.

**Dave Jones:** All you've got to do is put your probe over a trace on your PCB and it can measure the current flowing through it. And I've done a whole review of this and I'll link it in, but basically it's got a calibrator in there.

**Dave Jones:** I'm not sure if you can see that. Uh there's a little trace in there. Okay, there's a little PCB trace. Okay, at the moment it's basically zero like this.

**Dave Jones:** If I put it in there, I've got it to generate an AC current. I can't remember how much, you know, it's I don't know, 50 milliamps or something throw it flowing through it.

**Dave Jones:** If I put that there, bingo. Look at that. There's current flowing through that trace, an AC current. And if I turn it, if I rotate it like this, this is why it's called a positional current probe cuz it depends on the rotational position of the head.

**Dave Jones:** If I put it in this axis to the trace we're trying to measure, it measures basically nothing. But, you rotate it like that and you get the full current Yeah, you can measure the current flowing through the trace.

**Dave Jones:** It's brilliant. There's nothing else on the market like it. So, if you need something like this, you need it. Now, its bandwidth is actually not too bad. It's better than the current probe we saw before.

**Dave Jones:** It's actually 5 MHz, but it has You can actually set the bandwidth down to 500k or even 2 Hz down here and you can adjust the trace position up and down on your scope and also the sensitivity.

**Dave Jones:** And it's got three different modes. One is wire, comes with this ferrite clamp you put on there and it works just like a current probe. So that actually contains the magnetic field in there and you're in wire mode.

**Dave Jones:** So that makes it act like just exactly like a current clamp probe. And I'll do exactly the same thing I did before as measuring this oscilloscope waveform and bingo.

**Dave Jones:** There it is. It's exactly waveform and you can calibrate the thing. The only disadvantage is it is a bit more like dependent upon where the wire is in there.

**Dave Jones:** So if I move it like that you can see the amplitude does change a bit. So it's not quite as accurate as a proper current clamp probe but you know, it it does a reasonably good job.

**Dave Jones:** And the next mode is the PCB trace mode that we actually saw. So you know, when the current flows through the trace there. And here's where you have to adjust the sensitivity and it's a little bit how you're doing.

**Dave Jones:** It's not like it allows you to see the waveform but actually getting it calibrated, that's much trickier. But the value in this is actually being able to see the actual waveform.

**Dave Jones:** You don't nece- the same with most current probes. You just want to see the waveform. You don't really care too much about the absolute accuracy of it. And the final mode is magnetic fields and you can measure those directly in microtesla.

**Dave Jones:** So if we go to the menu here we can just have a quick whiz at it. Yeah, as I said like a DC to 5 MHz. Like the noise equivalent in a toroid, 6 milliamps RMS.

**Dave Jones:** So it's not for you know, really low current measurements. Just like most magnetic current probes. And then magnetic field measurement scale 250 microtesla, 200 amps per meter per volt output.

**Dave Jones:** And in wire mode plus minus 10 milliamps to plus minus 10 amps. And of course it's basically isolated. So you can actually stick this thing right into the guts of a switch mode power supply.

**Dave Jones:** You know, it does have like bare wire voltages and cat ratings and stuff like that, but you know, like look at it, right? You can your hands all the way back here.

**Dave Jones:** Stick this right right up the clacker I inside, you know, down through the transformers and all the filter caps and all the heat sinks alive heat sinks and everything else.

**Dave Jones:** Stick them inside your power supply and safe as. And you can see here that, you know, for like piece of sensitivity, it's not completely linear like, but good enough for Australia.

**Dave Jones:** At least you get to see the waveform. Now, I couldn't be asked to set up another like experiment just to demo this. I've done a demo of where you can actually use this to trace higher frequency signals through a PCB power plane.

**Dave Jones:** You can do lots of other cool stuff like that. So, I'll just steal the video and the segment from my previous video. Here it is now. Linked in down below.

**Dave Jones:** Hi. It's product review time. Now, what I'm going to do is try and attempt to trace out a real ground current on a PCB like this. And as you can see, there's a split PCB plane in there.

**Dave Jones:** So, I've got my current going in over here, coming out over here, and it's got to go through that tiny little trace down in there. That's the only way that it gets from there through to there.

**Dave Jones:** There's the split ground plane there. So, we shouldn't get any current flow around in here. We shouldn't get any current flow in the ground fill down in there. We shouldn't get any current flow down in here.

**Dave Jones:** We should just get the current flowing through there through that tiny little trace there, if you can see it, and down around through to here. Now, I'm using a 1 kHz signal here, but it would work for DC as well.

**Dave Jones:** But, just remember you've got the Earth's magnetic field as well. So, when you move this thing around, you know, where you you're going to get an offset uh shift like that.

**Dave Jones:** So, just be careful, but here we go. There's our reference waveform, and we don't have to worry about the calibration on this pot at all because we don't care about the magnitude.

**Dave Jones:** We're just tracing currents here on this board, part of the ground plane, and you'll see we've got absolutely nothing there at all. We can change the orientation, and we get that offset, but there's no 1 kHz signal.

**Dave Jones:** There's nothing flowing through that part the ground plane, but here there most certainly is. Once again, if we get the wrong orientation, it's going to vanish like that if we hold it vertical, but if we keep the correct orientation according to the magnetic field of how it should flow, then bingo, we still get the waveform.

**Dave Jones:** See the currents going both sides of that hole there? Here like this. And once again, it does some of it does flow down around there like that, but the majority of it's going to flow through this top part here.

**Dave Jones:** And it's going to flow up here, and you'll notice that it won't flow down into that little fill, that little void down in there. There is no current flow there at all.

**Dave Jones:** So, you can see the current flowing through here. And likewise, there's going to be nothing flowing down here. They're electrically shorted together, but there's no current flow. And this is a great visualization uh learning tool as well as a real practical tool for determining where your currents are flowing in your ground planes.

**Dave Jones:** And there it is flowing down there. And it's look, it's not going down this little bit down here. Very little down there at all, tiny little bit flowing through those two pads there.

**Dave Jones:** But as you can see, it's all going to flow through that trace there, that one tiny little trace which connects the two split ground planes. And it's going to flow up here, and all the way over to there.

**Dave Jones:** And look, down here, there's nothing in this little void down here. So, right that out. There's no current flow through any of this stuff down here because that's where it flows, through that bottleneck there, around here, and down into there.

**Dave Jones:** So, yes, this thing isn't cheap, but it's unique, and there's nothing like it. So, I'd recommend this if you're doing like lots of mains big switch mode power supply design and stuff like this.

**Dave Jones:** Just being able to get in there and see waveforms just without around. It's worth its weight in gold. And the last probe, we've got the EMC probe. Of course, I've done like what, half a dozen videos on using EMC probes.

**Dave Jones:** So, like yeah, I've already spent enough time on this video. I won't go through it again. I've even done a video on how to make your own one for like what what was it, 10 bucks or something like that.

**Dave Jones:** So, 10, 15 dollars or 20 bucks. Yeah, you can make your own. Of course, you get magnetic ones like this, which I actually have the loop, and you get them in different loop sizes, and this one here actually has a loop in there.

**Dave Jones:** So, these are called H field or magnetic field probes, and then this one here is called an E field or electric field probe. And well, I've done very interesting videos on differences between magnetic, and I've demonstrated on the magnetic and electric fields and things like that.

**Dave Jones:** But, great for doing EMC, electromagnetic conformity, pre-compliance for your products. And generally, the output levels of these are very low. So, you use a wideband RF signal amplifier. In this case, this goes up to 3 gig from Tech Box.

**Dave Jones:** And but, you can as I said, like you can just make your own out of a bit of coax. It's basically just a bit of coax in there, and that's it.

**Dave Jones:** Um and you can buy these amplifiers for like 10 bucks on eBay. Well, not this one, but like a little bare board one. And Bob's your uncle, you've got yourself a EMC pre-compliance.

**Dave Jones:** Very handy for like tracing down EMC faults and things like that. Once again, I'm not going to set up experiments again just to demo this. I'll link in my EMC videos, but that is another different type of probe.

**Dave Jones:** Highly recommended you should have one just because like just make one yourself. I mean, this set costs, you know, a couple hundred bucks, and it comes with like the calibration charts and everything else.

**Dave Jones:** And which is fine, but these do-it-yourself ones, once again, for 10 20 bucks just like your Here it is. Just like your transmission line resistive probe down here, I'd like why not?

**Dave Jones:** Just have a couple of these made up for when you need them. So, there you go. I hope you enjoyed this little two-part series on looking at all of the different types of probes available for oscilloscopes.

**Dave Jones:** There might be other obscure ones out there. Please leave it in the comments down below if you think I've forgotten something important or something exotic like this, you know, I prober thing.

**Dave Jones:** There are other I'm sure there are other exotic oscilloscope probes out there, but I think I've pretty much covered, you know, all of the general ones that you're going to find or have potential use for in the future.

**Dave Jones:** So, yeah, you've got your times one times 10 switchable probe with your scope, but there's a lot more out there that allows you to do all different types of measurements under lots of different scenarios that you might encounter in electronics.

**Dave Jones:** So, I hope you like that, and if you found it useful, please give it a big thumbs up. And as always, discuss down below in the comments over on the EVblog forum.

**Dave Jones:** Each video has its own forum link linked in down below where everyone discusses this stuff. And of course, you can check me out on the other platforms where I occasionally release exclusive material not on YouTube.

**Dave Jones:** Hmm. Catch you next time.
