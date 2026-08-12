---
video_id: VNsJ8qSk6CI
title: EEVblog #523 - REPAIR: HP 35660A Dynamic Signal Analyser
url: https://www.youtube.com/watch?v=VNsJ8qSk6CI
source: youtube-asr
timestamps: {"0": 1, "1": 13, "2": 29, "3": 43, "4": 58, "5": 95, "6": 124, "7": 137, "8": 147, "9": 170, "10": 184, "11": 199, "12": 213, "13": 225, "14": 236, "15": 249, "16": 273, "17": 293, "18": 301, "19": 319, "20": 340, "21": 363, "22": 381, "23": 399, "24": 418, "25": 446, "26": 466, "27": 477, "28": 497, "29": 507, "30": 522, "31": 537, "32": 549, "33": 569, "34": 580, "35": 591, "36": 605, "37": 629, "38": 643, "39": 653, "40": 660, "41": 676, "42": 691, "43": 704, "44": 715, "45": 726, "46": 743, "47": 757, "48": 769, "49": 778, "50": 794, "51": 803, "52": 816, "53": 827, "54": 838, "55": 849, "56": 862, "57": 870, "58": 888, "59": 908, "60": 922, "61": 937, "62": 952, "63": 964, "64": 980, "65": 990, "66": 1002, "67": 1018, "68": 1031, "69": 1047, "70": 1057, "71": 1076, "72": 1094, "73": 1105, "74": 1123, "75": 1139, "76": 1156, "77": 1166, "78": 1182, "79": 1198, "80": 1212, "81": 1228, "82": 1242, "83": 1257, "84": 1271, "85": 1285, "86": 1303, "87": 1312, "88": 1333, "89": 1347, "90": 1361, "91": 1374, "92": 1390, "93": 1403, "94": 1418, "95": 1437, "96": 1450, "97": 1462, "98": 1485, "99": 1496, "100": 1506, "101": 1523, "102": 1537, "103": 1554, "104": 1574, "105": 1582, "106": 1598, "107": 1613, "108": 1634, "109": 1647, "110": 1661, "111": 1676, "112": 1685, "113": 1704, "114": 1721, "115": 1734, "116": 1746, "117": 1761, "118": 1775, "119": 1790, "120": 1802, "121": 1810, "122": 1826, "123": 1838, "124": 1852, "125": 1864, "126": 1872, "127": 1885, "128": 1899, "129": 1920, "130": 1935, "131": 1944, "132": 1959, "133": 1974, "134": 1991, "135": 2008, "136": 2030, "137": 2038, "138": 2050, "139": 2065, "140": 2079, "141": 2091, "142": 2101, "143": 2111, "144": 2124, "145": 2140, "146": 2147}
---

**Dave Jones:** Hi, check out what I scored. It's a HP 35660A dynamic signal analyzer or DSA or sometimes known as an FFT analyzer in the industry and I can see myself.

**Dave Jones:** There we go, in the screen. Nice big CRT screen. This thing is an absolute beast and I've always wanted one of these for the home lab and never had one because they are quite pricey.

**Dave Jones:** Especially if you get one new and working, but this one is faulty. So hopefully we'll be able to repair this thing and get it back on track because I have been told that it is fully working apparently apart from the screen.

**Dave Jones:** The screen doesn't work for some reason. It went bust. Apart from that it was working beforehand. So you know, I don't know. Anyway, we'll find out. Hopefully it will get a decent repair video out of it.

**Dave Jones:** Could be very simple or could be very complex or could simply be BER beyond economical repair perhaps. So what is a dynamic signal analyzer or FFT analyzer? Well, it's a pretty specific instrument used in the sound industry, the vibration industry, the acoustic and underwater sonar industry and for measuring mechanical and plant vibration and shock response and all that sort of low frequency stuff which you get with

**Dave Jones:** mechanical any any sort of mechanical system or you know, acoustic type you know, underwater system. Of course I come from the seismic marine underwater background and these things DSA was as common as a general purpose oscilloscope in every lab and on every bench because they were just so incredibly useful for measuring the performance over frequency of very low frequency signals.

**Dave Jones:** Basically, DC up to 100 kHz pretty much is the frequency range of these things. And they've got Usually, they've got at least dual channel inputs and a signal source as well.

**Dave Jones:** So, you can generate a sign and noise and stuff. And the two wide dynamic range inputs You know, they've got various gain You know, really high gains in there.

**Dave Jones:** Sort of low noise stuff. Not absolutely, you know, industry-leading low noise stuff, but good enough for sound and vibration and mechanical and shock response. So, you'll hook these things up to accelerometers and things like that for doing drop testing, vibration testing, finding vibrational modes on circuit boards and things like that.

**Dave Jones:** I've done tons of testing like that with these dynamic signal analyzers or FFT analyzers. And you can get all sorts of real interesting parameters with this thing. You can get cross correlation between signals.

**Dave Jones:** You can get coherence between signals, which is a very important concept. I could do entire videos on those. But anyway, these are very specific instruments. And well, hopefully, we can repair this one.

**Dave Jones:** And they are a bit of a beast. I mean, check this thing out. Already taken the cover off it, and it weighs an absolute ton. It is enormous. And well, I don't even know how to get into the CRT in here.

**Dave Jones:** So, yeah, it's got some clips on here. I don't know. I've never actually taken one of these apart. I've used them for like, you know, more like 15 years or something.

**Dave Jones:** I've used these things. Never had an opportunity to take one apart, because they are They were always calibrated. They had the calibration stickers on them and if you took them apart in the lab, there would be hell to pay.

**Dave Jones:** So, um yeah, this is great. I finally get to look inside Well, no, sorry. I have looked inside not one of these HP ones. I've looked inside other brand ones.

**Dave Jones:** There's Ono Soki and if I'm pronouncing that correctly and Rockland and Stanford Research make one. I think it's the 785 which is a a pretty good DSA. And yeah, there's a whole bunch of Nisha companies making these, but pretty much you know, HP Agilent are still the ducks guts at them and they still manufacture them.

**Dave Jones:** Although there are a lot of PC based ones these days cuz pretty much all it is is basically you know, front end gain on here with you know, a wide dynamic range analog to digital converter and the source of course a signal audio signal source and then the rest is just you know, digitizing that and processing and getting the FFT result on that.

**Dave Jones:** So, a lot of the more modern ones are done on PCs of course. So, you get like a little box which plugs into your USB and you know, that's really all you need.

**Dave Jones:** So, you don't need the huge you know, processing built into the machines. Although having them stand alone like this is rather convenient for lots of uses. So, anyway, I might have to actually read the manual for this sucker to figure out the best way to get into it and there's the power supply.

**Dave Jones:** It's telling us our voltages and you know, the first thing you do when you're at troubleshooting something like this of course is measure the power supply voltages and we can tweak all the uh adjustment pots through there without having to take this out, but it is quite a beast and you can see the two shielded.

**Dave Jones:** Obviously they got two shielded cards like this for one for each channel and the front end stuff is shielded here, and then they've got the more, you know, digital type stuff up the back here, all connected in a classic arrangement with ribbon cables like that, and there's our processing board down there, which will generate the signal for the uh do all the processing and uh drive the screen

**Dave Jones:** and everything like that. And there's no There's actually no uh bus board down the bottom like that. All they do is uh sit in sit in connectors on the bottom like that, and they join them on the top instead of having your more traditional motherboard arrangement down the bottom.

**Dave Jones:** Just saves an extra board, really. And this uh beast, of course, has long since been uh discontinued. They do uh sell an upgraded model to this under a different part number still, but the good thing about it, you can go to the Agilent website and download the full service manual, complete with schematics and everything.

**Dave Jones:** Fantastic. So, you know, that makes that makes that servicing and repairing these things so much easier. Uh this one doesn't really have a date code on it visible um anywhere, but uh based on some of the chips I can see through the top there, some of the digital logic, it's dated around about uh probably late 1990.

**Dave Jones:** That's a start, anyway. I've taken off a whole bunch of screws on there uh to get that back panel off. Still haven't read the manual. I probably should read the manual to figure out the order that I need to take this apart because this uh CRT here, I suspect you know, is not easy to get into because it looks like the chassis wraps around over the top here.

**Dave Jones:** So, hmm, I don't know. There you go. I didn't expect to find another massive digital board under here, which goes almost, you know, 3/4 of the way to the front there, and that just contains a lot of uh 74 series logic and uh some unpopulated memory there by the looks of it.

**Dave Jones:** And it looks like we've got a bottom the bottom board down here, of course, is for the GPIB and the uh is that a serial interface? This is really quite nice.

**Dave Jones:** Look at the metal EMI tabs on there. And it looks like this board maybe slides out. Ah. It's tough, but yep, it does. Beauty. I don't know why I'm taking it out, but I just feel like taking it out.

**Dave Jones:** Why not? There we go. I didn't see that. It's got a rotating pull ring there that you can get your finger in and pull the board out. Didn't even notice.

**Dave Jones:** Neat. And well, there you go. I mean, I thought the processor board was up in here. There's our huge classic MC68000 processor and uh all the miscellaneous stuff to go along with that.

**Dave Jones:** So, obviously that is the main processor board down in there. And the board that was on top is the main memory board. Obviously, only like half populated here. And almost all of this sucker is made in the USA.

**Dave Jones:** All the main boards and everything else is except for the CRT unit up here. And there you go. That's a Matsushita distributed by Panasonic made in Japan. There you go.

**Dave Jones:** It looks like, you know, a completely self-contained module in there for the CRT. So, you know, really, I the fault is most likely to be in there, you know, I suspect because there's lots of analog type stuff in there to go wrong.

**Dave Jones:** I mean, you know, the digital processor and all that sort of stuff unlikely to well, it's the least likely to be faulty. So, yeah, probably something inside that module.

**Dave Jones:** I've just got to figure out how to get that damn thing out. Now, this power supply module is rather interesting. I love the modular way it just flips out like that with these ribbon cables.

**Dave Jones:** That's the most interesting thing about this. Bit of gunk on there, bit of dust from 20 years. This thing has probably been in service and yeah, interestingly uses these standard IDC ribbon cables to output most of the power.

**Dave Jones:** So, that's rather fascinating. Now, originally thought that this was some sort of power connector going off maybe down to the CRT module which requires 12 volts DC at 1.4 amps down there, but no, that didn't quite make sense why they use an IDC for everything else and just that one going out really and and it looks like it goes down to the front panel.

**Dave Jones:** So, that is most likely the front panel switch. So, that's just a a soft switch presumably. It doesn't look like a mains rated cable or anything to switch the power supply off.

**Dave Jones:** So, what you've got here is most fascinating. This main ribbon cable coming out of the power supply just goes up under there and then pops out here like that.

**Dave Jones:** You can see it wiggling there and then that is the power for all those boards. I mean, you know, at first glance you would have, you know, sworn that's data going across there.

**Dave Jones:** Well, there could be some data maybe, but it's most likely that that's just all dedicated to power. And of course, we've got some signal going across the from this looks like a controller board for the two channels over to the two analog channels.

**Dave Jones:** And this one here is actually a data cable which then just wraps over there and goes down the side of that case. Rather fascinating and the other ribbon cable here is obviously just the power for the main processor board down the bottom here.

**Dave Jones:** Fascinating. And if you can see down in there, a whole bunch of test points on the PCB, little nice little hooks. I really like those. Um just, you know, soldered uh tinned wire hooks on there.

**Dave Jones:** Got power supply and all sorts of stuff. And there's lots of those, including over here on the uh analog um boards as well. Fantastic test points which we can hook on to.

**Dave Jones:** And uh here is our main data cable going over to the CRT. That looks like the only thing going over. I'm not sure if that carries power and the uh data for the screen as well.

**Dave Jones:** But, yeah, um the nice modular construction like that at least allows us to troubleshoot. I mean, we can just um you know, probe the signals coming out of that IDC header down the bottom and see if we've actually got all of our required data going to the CRT module.

**Dave Jones:** So, we should be able to narrow it down to that pretty quickly. If you look down at the main processor board down in there, a classic uh multi-layer uh routed construction for all this DIP packaging, very typical of the time.

**Dave Jones:** I've uh explained this in previous videos, but on the top layer here, you'll pretty much see all of the routing lines going in this uh direction like this, so the vertical or the horizontal direction, depends on how you want to look at the board.

**Dave Jones:** And then the uh next layer inside, you can see this is a multi-layer board, oops. And you can see the traces going in there, the darker ones down in there.

**Dave Jones:** And they're generally going to go in this direction like this. And you can see that they're just at right angles like that. So, you know, clearly this thing has you know, most almost certainly been auto routed, I'd say.

**Dave Jones:** And uh you know, someone's manually placed all the uh chips, so there's some smarts gone into that. But uh then they've pretty much probably let the auto router uh do the job.

**Dave Jones:** This was pretty uh typical of the time because as I've explained in previous videos, you know, all this stuff doesn't operate at high speed. You know, we're talking uh what's the main crystal down here?

**Dave Jones:** You know, it's probably like 8 MHz or something like that, you know, 4 MHz. What does a uh 68000 run at? Like 8 maximum or something. So, you know, like under 10 MHz usually, not very quick at all.

**Dave Jones:** So, it really signal integrity is not a huge issue. Multi-layer board, it's got all the bypass caps. It's got tons of bypass caps. It's got the ground planes, everything else.

**Dave Jones:** So, not a problem whatsoever. So, it's all digital circuitry. You can just let the auto router rip. I mean, to manually route these by these sorts of boards by hand, I've done it.

**Dave Jones:** It's a pain in the ass, but this is one where it's very suited to an auto router. The algorithms are really easy when you've got one layer, you know, mostly going in one direction, another layer going in another one.

**Dave Jones:** You've got ground, power layer planes, and all that sort of stuff. Auto routers uh just the auto router algorithms just eat that sort of stuff up, really. Piece of cake.

**Dave Jones:** You can see exactly the same thing on the memory board as well. On this top side here, almost all the traces running in this direction. Yeah, you know, you've got the occasional, you know, wiggles going across, but generally, you know, the auto router's told to give priority to, you know, signals in that direction.

**Dave Jones:** So, you're not going to find a trace going from here right down to there cuz it just ruins that entire layer. So, the auto router is only going to know, "Oh, okay, I can only jump a, you know, a few handful of pins, half a dozen at most in both directions like that." Looks like we've got uh two traces between um pads up there, which is woohoo, you know,

**Dave Jones:** pretty big. I mean, you know, the big decision back in those days was, "Oh, well, does my PCB technology uh manufacturing technology and uh trace widths allow two two between pads like that?" There we go, you can see the two traces in there.

**Dave Jones:** If it does, you know, brilliant. But back then, you know, that was a huge huge decision. Not a big deal these days, obviously. But anyway, on the bottom side of that, you can see that they all go vertical like that.

**Dave Jones:** So, this layer, of course, there's some horizontal stuff on here because these are memories like maybe, you know, you would have told the auto router to you know, just route out the memory first or something like that or give priority to that layer in that direction or something like that.

**Dave Jones:** But as you can see, everything else this part of the circuitry or the miscellaneous stuff has been given priority in that vertical direction. Here we go. I just got these clips out here.

**Dave Jones:** Still haven't read the manual, of course, you know me. And there you go. There we go. We've popped out a front panel. You can see our CRT and it looks like yeah, I take out the screws here and this CRT module's just going to pull out.

**Dave Jones:** That was really the only way it was ever going to happen. Check out the RFI shield in they've gone to the trouble to do on this thing. There's the There's the front panel.

**Dave Jones:** But look at this. It's got Look Look at that gold wrap over that conductive wrap over the back of it like that and all the nice little RFI you know, tabs like that.

**Dave Jones:** It's just It's just a beautiful. They really spared no expense there. They really gilded the lily. And check that out. They've gone to the trouble to put what looks like some sort of you know, anti-glare filter or something like that on the over the front of the CRT.

**Dave Jones:** It's not a polarizing filter because regardless of what angle you put it at, I can still see my LCD watch. There you go. And check out those RFI tabs.

**Dave Jones:** Look at that. Basically connecting this front panel board through onto the main chassis down here. Brilliant. Actually, on second thought, I shouldn't take those out because that's taking the CRT out of the internal uh metal box.

**Dave Jones:** So, really what I want to do is there's I think there's a couple screws on the side and couple on the top, I think. Taking those out, this should just slide out.

**Dave Jones:** Although, that should pop out of there. And that, folks, is a really nice modular design. Look at that. I mean, that is fantastic. I really love that. We can now take that apart and work on that on its own.

**Dave Jones:** And of course, we can uh this cable looks long enough or if it wasn't, we just uh extend the cable to go in there and we should be able to probe and operate uh this while it's all connected and the power supply is uh still connected to the thing and we should be able to hook up the uh keyboard.

**Dave Jones:** You know, the keyboard just plugs down into there and easy to access. I like it. And a quick glance through the service manual for this beast, it doesn't show any schematics at all for the CRT unit.

**Dave Jones:** So, I don't Maybe they didn't have the rights to do it or they just uh deemed that uh that wasn't necessary. They only um did the schematics for the HP part of it, which is all the rest of the circuitry up to the input here.

**Dave Jones:** Now, of course, I still haven't uh measured anything at all on this thing. And uh I probably should at least do some uh uh voltage checks on the power supply, as I said, but I can't help myself, of course.

**Dave Jones:** I've got to pop this uh CRT system open. Although, I did switch it on, right? I I switched the thing on and some of these screws are hard. I did switch it on and uh it did seem that like it was accepting the button presses.

**Dave Jones:** Um and it was beeping as I remember and I could hear the input relays switching auto ranging and stuff like that. So, just as I remember using this thing.

**Dave Jones:** So, it's um that seems to uh tie in with what I was told that uh this thing did work apart from the CRT. So, I'm assuming that the power supply is correct.

**Dave Jones:** I mean, it's got you know, it does have uh 5 V and 12 V and plus minus 15 V and 18 V and stuff like that on it. But, uh I suspect that's not going to be the reason why the CRT's failed perhaps, although I could be wrong.

**Dave Jones:** But, and of course, you could argue that before you even measure power supply voltages, you look for obvious signs of damage and smell as well. Use all your senses.

**Dave Jones:** And uh so, it's worth just popping the lid off A for curiosity and B just to see if there's anything obvious, you know, is there any blown caps, you know, are they bulging, do they look like they're leaking, is something I don't know uh broken or something because somebody dropped the unit.

**Dave Jones:** I don't know. Who knows? But, uh definitely worth taking a look inside. Let's crack this thing open. Now, of course, uh dangerous as it warns you on the back, dangerous voltages are on in here.

**Dave Jones:** So, that even when it's powered off, they can still be charged up. So, just be very careful. You got to know what you're doing and uh Aha! I see the problem straight away.

**Dave Jones:** Haha! There we go. This was worth looking. Um can anyone see the issue? Look at that, the neck board here. And touch that, the neck board has come off.

**Dave Jones:** Look at that. It's just fallen off. There's the socket for the tube. It looks like the pins are all okay. Geez, I hope that's the only fault. That'd be fantastic.

**Dave Jones:** Um troubleshoot the Yeah, couple of little bent pins on there. Maybe I won't try and bend them back. I'll definitely just try and stick the socket back on. And I don't know, vibration maybe has caused the board to fall off.

**Dave Jones:** The board looks in good nick. Um anything else on the on the board? There is a fuse. There's a fuse down in there. It looks intact. But I will measure that.

**Dave Jones:** So there it is down in there. It's socketed. Very nice little M205 glass jobby. And uh caps look good. Diodes, nothing seems broken. Although those diodes look funny because they've got like a purple silk screen on them.

**Dave Jones:** It almost looks like they're burnt, but they're not. So uh And of course there's a reason that they have uh the protection around here. Nasty voltages straight out of there.

**Dave Jones:** You don't want that. But apart from that, sorry, it's hard to get the camera right in there, but it does look pretty good. And of course well, it's definitely not going to work with that bloody neck board hanging off like that.

**Dave Jones:** So I'm going to uh plug that back in and then just fire this thing up and see if we get lucky. Oh, that'd be awesome if that's the only issue.

**Dave Jones:** I can't be that lucky though, surely. Murphy's got to get me somewhere. And that pushed it on there, very nicely. No, no issues there at all. So, hopefully, um power this up and well, see what happens.

**Dave Jones:** Here we go. Let's give it a go. Let's give it a whirl. Actually, what I've done, which is a little bit more convenient, just slide the CRT back in there and uh hook the power switch back up and uh just have the front panel in position.

**Dave Jones:** So, here we go. Uh now, come on. It can't be that easy. Murphy'll get me. It's powering up, powering up. These things can often take a bit of time to Wait, look at that.

**Dave Jones:** Look at that. We're in. We're in. But, look at how adjustment Oops. Um our rotation is a little bit out. Um no, it's uh flickering on camera there. That's just the power on test in progress, copyright 1988, Hewlett-Packard Corporation.

**Dave Jones:** But, it looks like apart from a uh trace rotation issue, we have a working DSA. Searching for application. Blah blah blah blah blah Wait, that looks good. There we go.

**Dave Jones:** Calibration in progress. It's always doing a self-cal. I can hear the little reed relays clicking. You probably can't hear that, but trust me, I can hear those a mile away.

**Dave Jones:** And we have, folks, a working DSA. Uh well, presumably. Woohoo! Fantastic. Look at that. Oops, sorry. Gone out of focus there a bit. Beautiful. Bob's your uncle. Now, of course, that is uh very much a physical uh rotation uh issue in this thing.

**Dave Jones:** It's not like, you know, I can just uh tweak the uh pots on the top and and fix this sucker. Something has uh physically happened to the uh rotation in this CRT.

**Dave Jones:** So, I think we're going to have to take it apart again and take a closer look. But, hey, at least it's working. At least turn the brightness up a bit.

**Dave Jones:** Doesn't seem to be any particular burning in the screen at all. So, you know, it looks really good. So, let's have a look at what we've got here. I got the lid back off and probably, you know, this isn't really this issue really isn't surprising considering that the neck board fell off.

**Dave Jones:** You know, neck boards don't just fall off on their own. It's got to vibrate loose or be shocked loose or a combination of both. I don't see any physical signs of trauma on the main case of the unit.

**Dave Jones:** So, I don't think it's been dropped. It's possibly just vibrated loose over time and eventually just, you know, popped off with the springiness of the socket there perhaps. But, uh let's have a look in here.

**Dave Jones:** And that cable is also a bit annoying, but uh Hello. What Hey, hello. Hello. That assembly there looks like some sort of magnet assembly is I take it that's not normal.

**Dave Jones:** Notice that it was out here. It was protruding out here and sunken down in there. So, something has happened there. I'm not sure if some other something else has broken off.

**Dave Jones:** I mean, there's nothing in there. So, unless uh So, there's nothing, you know, rattling around in there. So, there's nothing loose. It's just a plastic ring assembly with uh uh possibly uh magnets in there.

**Dave Jones:** So, that's you know, that's not like the focusing coil or the uh deflection coil or anything like that. You can see those in there. But, yeah, that's just hanging around flapping around in the breeze there.

**Dave Jones:** So, and well, so let's have a poke in there. That's not really anything to do with the rotation as I expected. So, um it's the physical uh assembly of the coils in there.

**Dave Jones:** We're going to have to get in there and uh manually rotate those suckers. Looks like we're going to have to get in there and uh rotate our coil assembly and uh fix this sucker up.

**Dave Jones:** What we have to do is undo this clip in here and rotate the entire uh deflection assembly around the shaft there. So, that will fix um our rotation issue.

**Dave Jones:** So, um really, you know, that's obviously uh come uh loose or something like that during the uh vibrational whatever event um caused the neck board to fall off. So, really, easy fix.

**Dave Jones:** By the way, when you're tightening these uh things back up, don't do them up too tight. You don't want to crack the uh neck of the tube down in there.

**Dave Jones:** And if I hold my tongue at the right angle and just uh poke that board in there, bingo, we have ourselves a nicely aligned screen. Oh, what Oh, what, you know, it looks reasonably good anyway.

**Dave Jones:** And because we've got some dead spots on the CRT around the corners here, then uh we can pull in uh the horizontal width back in with the horizontal width control, which is uh that puppy down in there.

**Dave Jones:** So, we're going to adjust that after it's all uh back in, not a problem through the uh adjustment controls on the top of the case. Now, I was able to uh uh find out where this magnet assembly goes back in.

**Dave Jones:** There's a little uh key and slot up the top and down the bottom. So, I was able to uh push that back in and then I put some uh silicon back in there to uh hold it back in place.

**Dave Jones:** Obviously, it's uh uh you know, broken loose or come loose or something and that also um had effect on the uh deflection uh coil assembly around here, which of course is what caused that um uh rotational issue, so which we've uh fixed up.

**Dave Jones:** But, uh I don't exactly know what those I mean, I'm not big on my uh uh CRT um you know, systems uh knowledge, but uh those um permanent magnets, there's four of them around there.

**Dave Jones:** I presume that they're permanent magnets, probably um helping with some sort of focusing. I mean, they I don't think you know, they're not like uh convergence magnets uh for example, because you'd only get those in a color CRT and of course this is a mono CRT.

**Dave Jones:** So, so might have to do a bit of research on that one and uh uh see what they are. But, if anyone knows exactly uh what their uh purpose is in there, then uh please let us know.

**Dave Jones:** Doesn't seem to make a huge difference regardless of the rotational um rotational position of them or, you know, whether or not they're skewed at some angle or something like that.

**Dave Jones:** Um does I can't see a visible uh difference on the image. And I've uh just quickly reassembled it just so I could have a decent uh play around with it and you can see the the dark fringing around the corners of the CRT still.

**Dave Jones:** So, I still have to uh deal with that. I'm not sure what's gone wrong there, but anyway, I wanted to test the rest of the functionality. And uh as you can see, this thing has extensive internal uh self-test.

**Dave Jones:** I mean, there's a TMS uh 320 DSP uh processor in this thing. There's gate arrays. That, uh, uh, DSP processor's probably, I don't think I saw it on the board under the the horizontal board under the CRT.

**Dave Jones:** So, it's probably on the big, uh, vertical board we saw in there doing, uh, doing the DSP goodness. Of course, you know, you do all that in one processor these days.

**Dave Jones:** Uh, you know, basically to, uh, drive the CRT and everything else and and handle the GUI and the keyboard and the comms and and to do the DSP, too.

**Dave Jones:** But, anyway, it's got a ton of, uh, internal self-test, this thing. I love it. All these gate arrays, all the ADC, everything, everything passes. Beautiful. Look at that. So, and we can set it to, uh, loop test as well.

**Dave Jones:** So, uh, that's pretty good. It's got a whole bunch of stuff and, uh, you know, it it looks as, uh, claimed, you know, um, pretty much 100% functional, although I've yet to stick a signal here.

**Dave Jones:** But, jeez, you know, it's looking pretty good apart from the, uh, dark fringes on the CRT there. And unfortunately, with that horizontal width, uh, that here is about as close as I can get to If I keep going, it goes back the other way.

**Dave Jones:** So, there you go. That's about as good as I can get. Unfortunately, um, with that. So, you know, I I can still I can start seeing the negative, uh, sign down there on my number down in the bottom corner on the vertical axis.

**Dave Jones:** So, it's not too bad. You can still, uh, read the menus, of course, but would have been ideal if I could squeeze that in a bit more, then I didn't have to worry about the, uh, dead spaces there.

**Dave Jones:** And by the way, if you are adjusting, uh, these things, use one of these, um, non-conductive, non-magnetic, uh, plastic adjustment alignment tools, especially for that particular control, which is not just a uh, pot, but it's actually a slug-tuned inductor.

**Dave Jones:** Because if you use a screwdriver and stick it in there, it's I'm not even touching that, you're going to affect it because that's going inside the coil itself. All right, so let's just do a quick test to see if it works.

**Dave Jones:** I've got the source hooked up to channel one here. If going to source, let's just set random noise and the levels are okay. Just give us some sort of level because if you get nothing and you press start like that, of course, you know, we're down in the noise floor down here, you know, minus 85 dBV.

**Dave Jones:** So, let's plug it in. And well, let's start that again. I set it to 100 averages. So, as you can see, we're getting ourselves a pretty flat line there, which is what we expect after averaging all that random noise.

**Dave Jones:** So, it's working over the full frequency range, which is basically DC to daylight or what daylight is on a uh DSA, dynamic signal analyzer, 100 kHz. Woohoo! And if we set the trace type here to instead of frequency, we can set it at frequency domain, we can set it to the time domain, and there's our random noise.

**Dave Jones:** We can go in and we can do a fixed sine wave if we want. And there is our fixed sine wave. Beauty. Set it to 1 kHz. There you go.

**Dave Jones:** And we we've got continuous trigger, that's why it's not getting a stable display, but if we set the channel one trigger, not a problem. The source and the channel one input works perfectly.

**Dave Jones:** And the same thing on channel two. Beautiful. I Well, you know, on a basic check, this is a fully working DSA. Awesome. So, there you go. I hope you found that at least somewhat interesting.

**Dave Jones:** I was hoping that it would be a decent troubleshooting video, at least after getting out the multimeter, for sake. Uh let alone the scope, but it turns out it was a pretty done trivial and obvious um fix, and I need to do more with this.

**Dave Jones:** And uh uh but it looks in in pretty good shape, so I should be able to do some really cool videos with this uh DSI. And if you do want me to do something, um please leave it in the comments.

**Dave Jones:** But uh yeah, this is a really nice bit of kit. I mean, it's absolutely huge. I don't know where I'm actually going to put the damn thing. It's probably not going to really sit up on my uh rack there, so I don't know.

**Dave Jones:** I might just have to keep it under the bench and whip it out when I need it. It's not an everyday use tool, at at least not the stuff I work on these days.

**Dave Jones:** It used to be at my uh former job. I used to use these things almost every day um sometimes. And uh they are really nice instruments. A little bit obscure, but anyway, could do some interesting stuff with it.

**Dave Jones:** So, yeah, Murphy got me on the troubleshooting thing. Every time, I always hope when I get something that doesn't work, I always hope that, you know, it'll take me days to fix and hours and troubleshooting and aha, it'll be some obscure fault or something, but nah, too easy.

**Dave Jones:** So, I don't know what happened to it. They probably, you know, whether it was doesn't look like it's been dropped or something. I don't know. Anyway, um it's not in bad shape.

**Dave Jones:** So, hope you liked it. Catch you next time.
