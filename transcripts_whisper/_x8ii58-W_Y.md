---
video_id: _x8ii58-W_Y
title: EEVblog #982 - HP54616B 500MHz Oscilloscope REPAIR
url: https://www.youtube.com/watch?v=_x8ii58-W_Y
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 25, "2": 43, "3": 64, "4": 95, "5": 115, "6": 141, "7": 159, "8": 185, "9": 210, "10": 227, "11": 246, "12": 266, "13": 284, "14": 300, "15": 317, "16": 333, "17": 354, "18": 381, "19": 397, "20": 412, "21": 434, "22": 450, "23": 475, "24": 495, "25": 519, "26": 539, "27": 562, "28": 584, "29": 598, "30": 609, "31": 625, "32": 643, "33": 660, "34": 681, "35": 701, "36": 719, "37": 738, "38": 758, "39": 776, "40": 794, "41": 819, "42": 842, "43": 861, "44": 880, "45": 896, "46": 916, "47": 932, "48": 947, "49": 966, "50": 981, "51": 999, "52": 1024, "53": 1038, "54": 1058, "55": 1076, "56": 1097, "57": 1118, "58": 1137, "59": 1158, "60": 1177, "61": 1196, "62": 1213, "63": 1231, "64": 1251, "65": 1271, "66": 1289, "67": 1304, "68": 1318, "69": 1334, "70": 1347, "71": 1366, "72": 1385, "73": 1405, "74": 1421, "75": 1439, "76": 1456, "77": 1472, "78": 1485, "79": 1504, "80": 1524, "81": 1542, "82": 1559, "83": 1580, "84": 1598, "85": 1615, "86": 1631, "87": 1648, "88": 1663, "89": 1678, "90": 1694, "91": 1708, "92": 1725, "93": 1747, "94": 1766, "95": 1793, "96": 1812, "97": 1827, "98": 1844, "99": 1859, "100": 1873, "101": 1886, "102": 1903, "103": 1922, "104": 1940, "105": 1956, "106": 1970, "107": 1988, "108": 2009, "109": 2030, "110": 2047, "111": 2063, "112": 2079, "113": 2104, "114": 2125, "115": 2145, "116": 2166, "117": 2183, "118": 2202, "119": 2217, "120": 2236, "121": 2255, "122": 2275, "123": 2295, "124": 2312, "125": 2332, "126": 2346, "127": 2361, "128": 2376, "129": 2396, "130": 2411, "131": 2425, "132": 2446, "133": 2464, "134": 2482, "135": 2500, "136": 2515, "137": 2532, "138": 2552, "139": 2575, "140": 2594, "141": 2612, "142": 2637, "143": 2658, "144": 2676, "145": 2692, "146": 2706, "147": 2720, "148": 2733, "149": 2744, "150": 2757, "151": 2770, "152": 2786, "153": 2811, "154": 2826, "155": 2838, "156": 2856, "157": 2874, "158": 2895, "159": 2913, "160": 2927, "161": 2944, "162": 2958, "163": 2974, "164": 2993, "165": 3007, "166": 3020, "167": 3036, "168": 3050, "169": 3070, "170": 3093, "171": 3106, "172": 3125, "173": 3142, "174": 3160, "175": 3173, "176": 3187, "177": 3205, "178": 3230, "179": 3257, "180": 3272, "181": 3287, "182": 3304, "183": 3320, "184": 3338, "185": 3352, "186": 3369, "187": 3386, "188": 3400, "189": 3421, "190": 3438, "191": 3455, "192": 3469, "193": 3484, "194": 3500, "195": 3518, "196": 3535, "197": 3551, "198": 3567, "199": 3579, "200": 3596, "201": 3614, "202": 3630, "203": 3646, "204": 3660, "205": 3677, "206": 3691, "207": 3704, "208": 3717, "209": 3732, "210": 3742}
---

**Dave Jones:** Hi, it's repair time. I got myself a classic HP, none of these Keysight rubbish, or let alone Agilent rubbish. HP 54616B, 500 meg scope, 2 gig samples a second, 1 nanosecond peak detect. This is still a very potent scope these days, so if you can actually pick up one of these quite cheaply, if you can,

**Dave Jones:** they still go for a reasonable penny if it's a working and in good nick. This one's in reasonable nick, it does have, you know, some chips on the corners and stuff like that. It's obviously been dropped, it's got some paint on the top, it says power on, power's on, no signal.

**Dave Jones:** So, at least it should power on in theory. Anyway, I do like the form factor. You've heard me rave on about the 54600 series before and how I absolutely love that scope, and they're still very nice if you can pick one up, the mixed signal version, option interface, probe power, the calibrator output.

**Dave Jones:** And that's about all she wrote, so let's power it up, see what's wrong with it. Alright, fingers crossed. Didn't go bang, can hear the fan whirling. Oh, there we go, yes, HP, brilliant, copyright 1996, we're in like Flynn. Hello? Hello? The geometry of the screen looks really good, sorry about the flicker, you will get some of that, but that looks like it works.

**Dave Jones:** Well, there we go, we can move channel one. Oh, there we go, channel one, they just decided to pop up, what's the time base? No, the time, oh, hello, hello, the time base is there. 100 nanoseconds per division. It's not recognising the time per division.

**Dave Jones:** Oh, okay, so time division doesn't work, main delay doesn't work. Oh, trigger mode button doesn't work, measure, hey, measure works. Time, cursors, okay. I forgot to show you the BNCs, they look a little bit crusty, but they're physically intact, you could clean those up.

**Dave Jones:** Alright, so I'm feeding in one megahertz, one volt, peak to peak, sine wave, let's see if our auto scale works. Oh, can hear all the relays clicking, that's good. No active signal was found, please check connecting. Please check connections, I'm sure it was.

**Dave Jones:** Nah, it does, please check connections, it does not detect that signal at all. Channel two, auto scale again. Nah, nope, okay. So anyway, we can vertically, oh, there we go. Nah, we've got a trace now. Oh, nah, nah, that's one sick puppy. And nothing in the horizontal works at all.

**Dave Jones:** And the trigger, so trigger controls, horizontal controls, not active. Vertical controls are active, but kind of playing up. Measurements and stuff seem to work, but auto scale doesn't detect the signal. And run-stop mode and that sort of stuff works. And so, this is a weird set of symptoms here.

**Dave Jones:** I mean, what? I don't know. So when, you know, like, this scope has a comprehensive set of power on self-test and stuff like that. It'll test the acquisition ASIC, it'll test the ADC, it'll test, you know, the triggering system and other types of stuff when it powers up.

**Dave Jones:** So there's no errors when it powers on, so it obviously passes all that sort of stuff. But, yeah, it's not one healthy puppy at all. Thankfully our utility button works, so we can get into our service menu and let's run the self-test. Let's just go DAC.

**Dave Jones:** Measure calibrator output for 5 volts DC. Oh, okay, well, yeah, alright, I'm not too fussed on that. Hit any key to return. Okay, yeah, I'm not too fussed about the calibrator signal on the front panel. So let's test the ROM. Self-test passed. And the RAM self-test passed.

**Dave Jones:** So, sort of power up and internal tests seem to be fine. So with a weird set of symptoms like this, where, like, if it was just, like, the faulty channels, I would have expected, like, maybe one channel to be faulty, not both. For example, if it was, like, a front-end problem.

**Dave Jones:** The weird one is, like, it does not detect any of the horizontal or trigger menus, so I'm not sure what's going on there. But obviously all the display, all the power on self-test all run, so it would have tested the acquisition memory and stuff like that, I believe, when it boots up.

**Dave Jones:** And that seems to be all fine. So what do you do when you've got a weird set of symptoms like this? Well, thou shalt test voltages is the first thing. So let's open it up and see that everything's okay. We can get a service guide for this, but it doesn't have schematics.

**Dave Jones:** No first look on this thing. It's just got, you know, some basic troubleshooting stuff and things like that. So let's open it up and measure some voltages and see what's what. And here we go, we're in. It's really easy, just two screws on the back and the whole thing lifts off.

**Dave Jones:** So there's our CRT board, everything's accessible for that. But there's nothing wrong with the CRT system at all. And then we have our power supply down in there that's reasonably accessible. So we can get a good gander at that. And it's a little bit dusty, but it's otherwise generally quite clean.

**Dave Jones:** And there's the main processor board on the back. Everything pretty well accessible, TMS 320 DSP classic. And then you've got the custom HP stuff here. And these would be acquisition ASICs. This is the precursor to the MegaZoom ASIC technology, I believe. So yeah, the front end in the metal can, ADCs, acquisition ASIC.

**Dave Jones:** I hope it's not one of the acquisition ASICs that's failed. But then again, there's one for each channel. But neither channel works, so that's interesting. And then we've got the... well, that's not a BGA, it's a PGA part. It's a pin grid array part.

**Dave Jones:** I can actually see... There you go, you can see the pins under there. Pin grid array. So one of the first things you're going to do is go around the board and just have a look at the visuals, see if there's anything out of the ordinary.

**Dave Jones:** And I've had a look for blowholes in chips, burn marks, anything like that. And you wouldn't expect it on a 5 volt logic board like this. Pretty much everything's running at 5 volts, you know. Like, yeah, we can have a failed chip, but nothing's probably going to have the magic smoke released.

**Dave Jones:** So visually it's okay, and give it a smell test too, but nothing wrong. Okay, we'll just quickly measure the output power supply. The good thing about this, all the power's coming in here like this. And there's 5 different rails, I think it is.

**Dave Jones:** So let's go in there and give it a blow. Minus 15.7 is 1. Then we should have plus 15. Yep, there's quite a wide tolerance on that. Then we should have 5.1. Yep, pretty darn close. And then minus 5.2 is correct. It's not 5.1, it's actually minus 5.2.

**Dave Jones:** And then, well, minus 5.2. So they're all our rails. They are all good. So, damn. It ain't the power supply. Now here's where, even without the manual, you can start probing around at other power type regulators we've got here. So let's have a look at the middle pin of that one.

**Dave Jones:** 1.8. Okay, 1.8 sounds like a decent voltage for the acquisition ASIC there. Look, we've got these two power puppies here. Let's measure minus 12. That sounds spot on. And 11.88, fairly close to 12-ish. So they're obviously plus minus 12 volt regulators. What else have we got?

**Dave Jones:** There's another tiny little one over here. So let's have a look at him. 3.3 volts out. Perfect. Okay, something in there needs 3.3. So you have a bit more of a probe around, but yeah, like the power supplies are looking okay. So it looks like something else has possibly failed.

**Dave Jones:** That's where the rabbit hole seems to be leading anyway. Unfortunately our service and troubleshooting guide is pretty much useless beyond that. It just says, you know, run the, once you've checked the supply voltages and they're okay, you know, jump to step 9 or whatever, and then run the self-test service menus, which we've done.

**Dave Jones:** So, we're on our own. Here we go. I thought this was two separate parts under here, but it's not. It's just the one acquisition slash ADC, and that's a ceramic, so you know that's going to be a hybrid. So that's going to have the ADC plus the acquisition stuff.

**Dave Jones:** Does that have the acquisition memory? Probably. Anyway, there's a whole bunch of magic under there, but it looks like we can unscrew that. You notice that it's got the pins there. We should be able to lift that off. So let's get under there and just reseat it.

**Dave Jones:** Clean the contacts, put it back in, you know, do that for both of them. See if that makes a difference. So there's our socket. There's actually not very many pins on that. You can see not many of them are populated. These are little pogo pins.

**Dave Jones:** You shouldn't really go around playing with those, but you'd inspect them to make sure one's not, like, stuck down or something like that. You've got to get down there at an angle with the, you know, with the magnifier and have a look. And there's the acquisition hybrid.

**Dave Jones:** Ridiculously easy to replace, but, if you can get the replacement part, but, yeah. We're not going to see anything else. I'm not going to go try and take the cap off that. It's probably all encapsulated or whatnot. Yeah, there's nothing we can really repair in there anyway.

**Dave Jones:** So, yeah, let's just not bother. We're just worried about the contacts. Hang on! We got something! After replacing that, taking it out, giving it a bit of a jiggle, and putting it back in, we've actually got a waveform. Our time per division, I can go down.

**Dave Jones:** Well, it's still not responding very well, but our horizontal is kind of, sort of responding, and we kind of, sort of have a waveform. Ha ha! Let's go auto-scale and see if we can get it. No, no active signal. Oh, no, doesn't like it.

**Dave Jones:** But, hey, we're getting there. Yeah, look at this. We're getting something. Our volts per division is working. Can I get it a bit faster than that? Oh, come on, the horizontal time base is still dodgy as, but our volts per division is correct, 1 volt peak to peak.

**Dave Jones:** That's what I'm feeding in. The response actually looks fine. So the analog front end seems to be working just fine. Now I actually think that the vertical pot, at least channel 1 here, it's come good. So, no, no, it's not. See, I'm turning that down, 200 milli, 500 milli,

**Dave Jones:** it's, yeah, see, it jumped back to 500. Do you see it? So I'm increasing like, yeah, 200, 500, even though I'm going the same direction, it's sort of, yeah, it's sort of jumping around. You can get it to go all, and there's multiple relay clicks in there for some reason.

**Dave Jones:** So I think we've got ourselves a faulty rotary encoder here. But apart from that, we seem to have fixed channel 1. It seems to be working just fine. That's a 10 meg square wave. Everything works, seems to be working. The front end, you know, there's no problems with the dynamic range of that by the looks of it.

**Dave Jones:** It just looks fantastic. So just reseating that acquisition ASIC seemed to have done the trick. Now when, I forgot to mention, when I was taking it off, the screw did seem a bit loose on one side of it. So maybe it just wasn't, because it relies on the screw pressure on that,

**Dave Jones:** the top bracket to actually keep the thing down. So one of the screws in that was loose. So maybe that's all it was, was contact pressure on the, because those pogo pins don't move much on that, on those sockets. So, you know, there's very little, you know, room for, margin for error there.

**Dave Jones:** So anyway, let's try that on channel 2, because channel 2 still does not work. These things get stupidly hot, by the way. Way too hot to touch. Houston, we have a problem. Oops, the ceramic substrate has just broken completely off like that. And unfortunately it looks like that is, yep, yep, there's three pins there.

**Dave Jones:** So that hybrid is completely buggered. Yeah, I, like, fixing that, like, you'd have to, like, this top is a ceramic as well. It's going to be potted on there. Like, repairing that, I just, like, I wouldn't even attempt to try that, I don't think.

**Dave Jones:** And there's our three pins there that actually connect into that. So unfortunately, they are required. Hmm. Now it turns out you can actually buy these on eBay. People sell second-hand tested, some are tested, some are, like, you know, sold as-is kind of thing.

**Dave Jones:** And they can range from $45 to, like, $100. That's US dollars, so that's pretty pricey. $45 is okay to get, like, a 500 meg bandwidth scope working again, but you'd want to repair the rest of the scope, make sure it's all hunky-dory, and be fairly confident that, you know, this was the only issue.

**Dave Jones:** But hey, you know, you can get them. And out of curiosity, I just checked to see whether or not you could get something like this pin grid array package here. It turns out that somebody on AliExpress is selling it for, like, $32. So even if that was busted, you could buy it.

**Dave Jones:** But hey, that's, like, a soldered-in part. So yeah, on a multi-layer board with, you know, 100-plus pins or something, yeah, wouldn't like to be sucking that one out. Right, so let's forget that second channel. That's not really fixable without a new hybrid. And work on some of these controls, because we know our vertical one works,

**Dave Jones:** but we might have, like, a dodgy rotary encoder. You'd expect that for the age. Rotary encoders fail. These were probably just, you know, the contact ones. So we might be able to get in there with some contact cleaner. But look, I mean, here's our horizontal that we want to get working, okay?

**Dave Jones:** So 50 nanoseconds per division. We turn that in the same direction, and I can get it to toggle, kind of. Oh, no, it's all over the shop. Look, it's trying to... there, there's something seriously wrong with that. But I am sort of, like, you turn in the one direction,

**Dave Jones:** and it sometimes toggles between 50, 100, 50, 100. There they are. They don't particularly look like happy little campers. Um, yeah. Old and crusty. This whole scope is old and crusty, but it's still in reasonable condition that, you know, you wouldn't go, hey, I'm not going to repair this.

**Dave Jones:** So I'm just going to get in there with some contact cleaner lubricant. This is EML type from Electrolube. Um, yeah, everyone's got their favorite contact cleaner, whatever. This one I just happen to have here in the lab, so I'll give this a burl.

**Dave Jones:** So we'll just test the keyboard here. You go into the service menu, it's got a nice little keyboard map like this. You can check everything. Isn't that wonderful? Yep. Yep. Shows which direction the pots go. Look, turns it that direction, turns it that direction, turns it that direction.

**Dave Jones:** Beautiful. And... saying it's getting something, which it kind of is. Um, because we have been able to get it working. Yeah, that button's definitely gone. Run button works. Everything's stopped. Auto store. Yep. Yep. Gone, gone, gone. Hold off. And, oh, the trigger, yeah, both directions.

**Dave Jones:** And, yep, so we've got a few dodgy buttons. Couple of dodgy encoders. So let's get the front panel off, and you do that by taking off all the nuts on here, the knobs and the brightness control, and there's a couple of tabs on the back

**Dave Jones:** apparently that will hold it on. Now that's a little bit tricky, but there are two hooks on there, and it does actually come off. Ta-da! There's our front panel. Pesky thing. Oh, it looks pretty crusty. Manufacture date, January 2000. It's not that old in the scheme of things.

**Dave Jones:** And we're in. There's our rubber membrane, so we can actually measure the contact resistance on these. The matching contacts on the PCB, all gold-plated, so that shouldn't be a problem. But once again, you'd go over with some isopropyl alcohol and just clean the board up.

**Dave Jones:** Now we can get in there directly and try and resurrect these contacts, although they could be long gone. But worth a shot. And what we'll do is just measure the contacts on there. See, they're still all right. They're not going to be zero.

**Dave Jones:** They're a couple of hundred ohms. They're just carbon-backed or whatever it is. So those buttons all look hunky-dory. They should, in theory, just need a wipe with some isopropyl alcohol and the matching pads and Bob's your uncle. No, we're still... Horizontal is still...

**Dave Jones:** These buttons here are dead. Interesting that it's an array of them like that. Some sort of row or column, perhaps, because these would be in a matrix, a keyboard matrix. Check it out. Looks like we've got a couple of either trellis or diodes down in there.

**Dave Jones:** I'm thinking that one of those is gone, and also the rotary encoders. They're actually using those on the same section as what those buttons have gone. Because it's a bit coincidental that they're all grouped physically together and they're all gone. That includes, you know, two pots and three buttons or whatever.

**Dave Jones:** So, hmm. Or they could also be a dual diode array, like a BAV99 or some sort of variant like that. Now that one's upside down, so all the electrons are going to fall out. It's labeled P44, and I've checked all of them, and they've all got that P44 on them.

**Dave Jones:** And if you Google P44 SMD or whatever, some sort of transistor with built-in bias resistors, I don't think it's that. I think it's probably a single or dual, well, I think it's a dual diode. There we go, 0.527, that's a diode drop. And if we go to the other pin down there, 0.527.

**Dave Jones:** And those two pins on that side are not shorted together. So it certainly looks like a dual diode, with the anode on the top pin and the two cathodes on the other one. Now, just got to go around and measure them all. Oh, and of course, when you're doing this,

**Dave Jones:** just make sure you're disconnected from the circuit of the test. So what I'm going to do is have a probe of these rotary encoders on a brand spanking new unreleased oscilloscope, and check it out, it's a Siglent SDS1102XE. It's the E edition, 100 megahertz, only 1 gig sample per second,

**Dave Jones:** and it uses the Zinc FPGA and ARM processor built into the one chip to get the cost down. So don't have an exact cost, it's just a bare-bones, entry-level, two-channel scope that's super responsive, got deep memory, deep FFT, and everything like that due to the Zinc processor.

**Dave Jones:** It's how they get the cost down, no waveform gen, no mixed signal stuff, it's just your basic, entry-level, two-channel scope. So hopefully they sell it really cheap. Anyway, yeah, more details coming soon. We're going to have a look at the signals here. Now, it's only a two-channel scope, we can't view the external trigger

**Dave Jones:** because rotary encoders like these have three channels on them. So unfortunately, we don't have that third channel to actually view it, but anyway, let's take a look. I'm just doing two of them here, and we've got some roughly 5 microsecond pulses like this,

**Dave Jones:** and let's turn our rotary encoder. Of course, we're turning slowly, so we're not going to see anything at the fast time base like this, but if I change that, all we can see is just a little bit of that rising edge there changed,

**Dave Jones:** because it's a signal integrity thing. I'm grounding the ground points over here on my scope, and I'm probing over here on the front panel. It's horrible signal integrity, but at least it gets you the signal up on the screen, which is fine and dandy.

**Dave Jones:** We can't see that, so we have to expand our time base out, and then there we go, there are one millisecond per, so they're two milliseconds apart like this, so they'd be doing this, of course, for the multiplexing, because these things have to be multiplexed.

**Dave Jones:** So let's roll like this. I like how it automatically, it's got a roll button, and it automatically goes into roll and does the button like that. So that's, I don't think you can turn, yeah, you can, it's acquiring, it's acquiring, it's acquiring, there you go.

**Dave Jones:** But it automatically went into roll. That's kind of nice, I like that. Alright, so I'm going to turn one of the good knobs in this case. So let's turn it, and oh, hello. Hello, I'm continuously turning. If I stop, that's interesting. Look at that, the top one's vanished.

**Dave Jones:** And if I turn it the other direction, and stop, so I guess that depends on which contact point it ends up at. Anyway, this is a knob that actually works, because if you go have a look over here, this is the vertical on channel one,

**Dave Jones:** and it, you know, look, it's working fine and dandy, no problems whatsoever. So that looks like the genuine signal when the thing's working. So that's interesting, it's like they're clamped, that could be the diodes in there. But, hmm, fascinating. Anyway, what we want to do now,

**Dave Jones:** we're not too concerned with the details, we just want to see if there's a difference between the good rotor encoder that works, and one that doesn't. So let's actually just hook up three probes, and a scope that's actually got three channels, which is the new Keysight 1000X series,

**Dave Jones:** you can actually use the external input as a third channel. Albeit, it's a digital channel, so we can't, if we actually go in here and have a look, you see that we can't see the amplitude level changes, but we can actually see some of the data in there changing.

**Dave Jones:** So it's not, you know, it's not a true, it's not like a three or four channel scope, it's like a two and a half channel scope. Alright, so here's one of the advantages of a true four channel scope, like the Rigol 1054Z, is you can actually view, in this case,

**Dave Jones:** all three analog waveforms. We don't need this, we don't absolutely need this. I can troubleshoot this on a two channel scope, no problems whatsoever. Even a one channel scope, I can, you know, I don't need the timing information, I don't think it's going to be like a relative timing problem between two,

**Dave Jones:** it's going to be, you know, the rotary encoders fail, I can probe them one by one, or you know, two by two, no problems whatsoever. And here's one of the problems, it doesn't go into automatic roll mode, like it does on that Siglent, which was very, very nice.

**Dave Jones:** This is a working pot, I was going to say pot, a working rotary encoder. You'll notice that the two top ones, sort of like change between like full on, full off, you can get them in different configurations, depending on where you happen to end up leaving the encoder position.

**Dave Jones:** So that's just, you know, clamping in a different, like it's stopping in a different location. But the third channel, down here, is just, is not doing that same thing. So that could be to do with how it's, how the system is multiplexed, or something like that,

**Dave Jones:** because we've got like 2, 4, 6, 8, 10 encoders, and 10, 12, 15 buttons, or something like that, on a, like a 10-way ribbon cable. We're looking for something, or we're looking for a change, a difference in that, on the faulty pot. Or the one that's, you know, not working.

**Dave Jones:** I don't think the actual encoder is faulty. I think there's something to do with the multiplexing system, which is why a couple of the encoder knobs aren't working, and a couple of the buttons. Alright, so now I've got the horizontal control, which was not working.

**Dave Jones:** Well, no, it was kind of, sort of working. Oh, hello. Hello. That's clamping, oh, that top one. The middle channel there seems to be doing exactly the same as before, but this top one, look, it's clamped at low, which we didn't see. We didn't see that before.

**Dave Jones:** So that's interesting. So we're detecting something, but it doesn't go all the way with LBJ and actually change the, you know, change it properly, as you'd expect. It just sort of like toggles between two values. So that kind of, eh, something's going on.

**Dave Jones:** We'll just confirm another fully working one, which is the hold-off down here. That's working just fine and dandy, and that's doing the same as the channel one vertical. So that's a reasonable confirmation. I might check a couple of other working ones, but that's working identically.

**Dave Jones:** Now just as a little aside, we didn't actually need to get out the scope and probe these signals. We could fix this, like, almost without a scope, in that, you know, just by the symptoms, right? Several of the pots have gone, right? I keep calling them pots.

**Dave Jones:** Several of the encoders are gone, and several of the buttons, like, and they're in a physical grouping that all seem to have gone. So that indicates that, hey, there's nothing wrong with the actual encoder itself. It's how it's multiplexed. So, you know, we're just viewing the signals for kicks,

**Dave Jones:** but, you know, we know something else is wrong in the circuitry. Something's going on, right? So I've actually measured all these diodes in here, and they all seem to measure just fine and dandy. Like, some of them are actually shorted out on the PCB.

**Dave Jones:** They only use the one diode. Others seem to have the dual diode configuration in them. So I've measured them all, and they all seem okay. So I'm going to, like, go have a look at the main motherboard and see what we can see over there.

**Dave Jones:** Damn, that front end runs pretty hot, let me tell you. I can barely keep my hand on that. You notice how they've got the cutout here for the 4th channel? Because I believe this particular series comes in, like, a 4-channel version as well, if you want.

**Dave Jones:** But this is just the 2-channel with the external trigger. But yeah, that 500 megahertz bandwidth, what the bloody hell have they got in there? I'm now probing the main board here, the main keyboard connector. I love how you can just disconnect the keyboard

**Dave Jones:** and, like, access the top of this scope. It's a really nice scope to service. I just press the stop button, and it actually stopped all the gaps in there. Now, at this point, it'd actually be nice to have a schematic. I can't find the schematic for this exact one, the 54616B.

**Dave Jones:** But for the 5400B series, if you go to the actual Keysight website, it has what's called a CLIP, a Component Level Information Package, which basically is Keysight speak for the schematics and the parts and the bill of materials and everything else. And sure enough, you can actually download the CLIP,

**Dave Jones:** which includes the schematics for the 5400A series. But it's linked in to the information for the 5400B series. So, eh, I'm not sure what's going on. I'm not sure if they're exactly the same, but it could be close enough to help us out.

**Dave Jones:** Now, at a casual glance, these chips look like 74ACT244s, but noooope, they're not. They're actually 74AC11244, which is an entirely different pin-out chip. You won't find the ground and power in your conventional, you know, pin 20 and pin 10 over there. Hmm, trap.

**Dave Jones:** So these are actually super-fast bus drivers, and why they're using such, you know, high-performance variants in just the keyboard driver, and yes, that's where all the traces are going. You can probably, you know, see some traces running under there, and then of course it goes over to the 68000 processor there.

**Dave Jones:** So, you know, it's all, like, why are they using such fast beasts for the keyboard? I don't know. They're probably using them elsewhere on the board and bomb reuse, all that sort of jazz. So I'm just probing one of the pins there, and we saw this before.

**Dave Jones:** I'm just going back to this signal here, right? Which is, like, here's the ground down here, and it's sort of, like, clamped right up the top. It just doesn't seem right, especially considering that we're actually grounding this point properly. They've actually got a little grounding stake on the PCB there.

**Dave Jones:** So, you know, yeah, we've got a little bit of an antenna earth lead there, but, like, no, okay? This is, like, that's just weird. That's not something I expected to see. And then you've got all this crap down here. This is another line, right?

**Dave Jones:** Like, what? What is doing there? Like, give me a break. Like, you know, then they've got these pulses which don't go all the way up, they're sort of clamped below the rail. These ones are clamped there, and it's going tri-state and charging. What?

**Dave Jones:** So unfortunately the schematics aren't really going to help us a huge amount. It doesn't seem to make any sense. We kind of might know, like, it's going to be a similar architecture to this one, but it's not the same schematic. I've checked, you know.

**Dave Jones:** It's based on a similar architecture, but this actual upper model is different. So we don't have any exact schematics. But, you know, we can see we've got address and data lines there. But yeah, beyond that, it doesn't seem to be the same. Sometimes you need a third hand.

**Dave Jones:** Beauty. Hmm, doesn't seem to be much doing there. That's the output enable signal. That's just one line that I was sort of having issue with. Yeah, it correlates here and here. Kind of. Kind of, sort of. Yes, it does. And of course, one of the big problems with old gear like these

**Dave Jones:** are these lithium battery-backed SRAMs which hold the calibration and other data. So, you know, this one still seems to be hanging in there. And it's not uncommon to have them last 15, 20 years. But, you know, they're only supposed to have, like, a 10-year lifespan.

**Dave Jones:** This unit's, what, 2000. So this one's, you know, 16, 17 years old. I've measured every single diode on there. I've even sucked off a couple of diodes down here and now half the controls over here don't work and verified that it is a dual diode.

**Dave Jones:** And they're all, every single one of them is hunky-dories. So what's left? We've got the 68000 micro and we've got two bus drivers. Of course, one thing we haven't looked at yet is the bottom of the board. So I flipped it out, wasn't that hard,

**Dave Jones:** just take off a few screws and it pulls out. And, well, you know, we've got a significant amount of stuff on the bottom. It's all pretty jellybean stuff, you know, like 7-4 series logic passives and bypasses. Lots of tantalums, always look out for any dodgy tantalums.

**Dave Jones:** And if we go up there, there's our keyboard connector. Oh, nothing much doing around there. But there is an active device there going off to one of the pins, little SOT 23. So diode or a tranny, 1.2. Hello. That does not sound good.

**Dave Jones:** That does not sound good. Let's flip that polarity around on that. Hey, there we go, there's our diode drop. Okay. Ah, there's our dual diode. Looks completely dodgy. And considering it's going off to an open pin there, there's no other circuitry in parallel.

**Dave Jones:** There should be no other circuitry unless that pin buggers off somewhere else, but I doubt it. There's no other circuitry there to, like, actually affect our diode reading. So, aha! That's promising. But I just checked, and yep, the third pin there does bugger off

**Dave Jones:** to one of the 244s down there, so that could be upsetting that. Only one way to find out, suck it out and measure it. One of the good things is we can actually operate the scope with the board completely flipped out. Beautiful. And it measured just fine.

**Dave Jones:** I powered it up without it, actually, just for kicks. And no, exactly the same problem. And if you go around and check the actual pins on the encoders, they're all fine. I mean, I'm twiddling that, and you get all the various, you know,

**Dave Jones:** combinations on the three contacts there. So, like, they all seem to work just hunky-dory. It's not like one's, you know, stuck on, shorted, or something like that. Not that it should probably do anything. Okay, one interesting thing is that if I probe all of the output enable lines on both of these chips,

**Dave Jones:** there's actually two four-way buffers inside there, each with its own output enable. They're all joined, so it's a common output enable on all of them. The purple traces the output enable, as I said, and it seems to be doing its thing, okay? It's not doing anything weird during the time when it's,

**Dave Jones:** when the output is enabled, which is low. It's an active low pin. So, yeah, I, oh, hang on. What's going on over here? Let me capture that. No, that's okay too. When it's, you know, going active low, it's not doing anything weird. It's the other line, you know, one of the lines is going high

**Dave Jones:** and everything's hunky-dory. So there's a lot of action happening on that bus. So just from some probing around there, I'm inclined not to suspect these now, because they seem to be doing their business. So what's happening on the bus when it's disabled is none of these guys' business.

**Dave Jones:** So, but when you do the output enable, boom, it seems to be doing its thing. So, yeah, I think it would be a bit willy-nilly to go suck those off and replace them. Not that I'd have replacements anyway. I mean, it's not like the regular 244s.

**Dave Jones:** And I'm going to buzz out the cable too, just to make sure there's no cable breaks in there. Looks fine and dandy. Alright, I found a line here that if I press the button, any button on the front panel, then I can get that to go high like that.

**Dave Jones:** So all these buttons seem to do everything, like it's just one part of the matrix. But the ones that don't work, they actually don't give any response at all. So that, it almost makes me think that there's like a break in one of the lines

**Dave Jones:** on the front panel. So nothing shorted or anything like that, but some form of break perhaps. And if you can hear some noise in the background and you wonder what that is, it's Phil! Don't make me die, you bastard! And it's not that 10k resistor pack either.

**Dave Jones:** That's got a single common pin and they're all pull-ups to the 5 volt rail. So it's not that. And I think I know why some of those look like capacitor charging, because they deliberately have 2200 PARFOR 2.2 nanofarad caps. I believe they're all on the bottom.

**Dave Jones:** And they're on some of the lines in there. There's an obvious reason why all this stuff is here, which you wouldn't expect to see on the keyboard. The keyboard is directly hooked on to the 68000 processor bus. So that's why it uses a 244 type buffer there,

**Dave Jones:** and yeah, why we're seeing all sorts of processor type random stuff on there. Because that's the 68000 doing its thing, there's a whole ton of other stuff tied onto the same bus. But as I said, effectively the keyboard selects. So it's only during those periods is it, you know,

**Dave Jones:** actually sampling the keyboard. You can see the bus actually do things if I auto-scale. So if I auto-scale that, I'm not pressing the key anymore, so it's not doing that. And the top one is the keyboard enable, so that you can see that it's, you know,

**Dave Jones:** it's actually not sampling the keyboard as much, I guess, during those periods when it's got to run all the other stuff on the bus. So that's why you get all that activity happening. That's just one of the data lines that is also hooked onto the keyboard system.

**Dave Jones:** And I've also just desoldered a couple of the pots here, and of course they measure fine outside of circuit, as they do in circuit. You know, you put your meter on there in the various combinations and you can see all of the states change and stuff like that.

**Dave Jones:** Nothing seems to be stuck, nothing seems to be open. Not that you'd expect that to be a problem. And after re-soldering, taking them out, doing whatever, checking everything else, checking for buttons, shorts as well on there, nope, can't find a thing. It still works exactly the same as before.

**Dave Jones:** And also, one thing you might suspect, because this is being used as a front panel, there's always stress on the controls and everything else. People are slamming the controls. There could be a cracked solder joint or something like that. But I wouldn't expect that to be an issue,

**Dave Jones:** just from an individual rotary encoder point of view, because like I said, they're normally open and normally closed, depending on where you stop the thing like this. So a short or an open on a rotary encoder should not affect any other controls, should only affect the individual one,

**Dave Jones:** which is not what we're seeing. So unless the solder joint's being used as a via and it's cracked and was relying on solder joints both sides, which is not the case here, there are no solder joints on the bottom, they're not being used as vias.

**Dave Jones:** So with the connector over here, I've re-soldered that, just as a matter of course, and I've actually buzzed out all the pins across the connector, and everything's just fine. All right, I think it's time to get a bit more methodical here. We've just been fart-arsing around,

**Dave Jones:** and you can argue that we should have done this earlier, but meh, whatever. So what we're going to do is we're going to check the outputs of the 244 or 11244 buffers here, and actually have a look. Now if we have a look at the schematic for the 54600A,

**Dave Jones:** it's fairly close to identical, but you'll notice that that uses HC244s, and we use 11244s, so the pin-outs are different, but I believe they've copied the functionality identically, and even the pin-out on the connector looks like it might be the same, and stuff like that.

**Dave Jones:** So, which makes sense, they'd reuse the front panel and things like that, and all the keyboard interface. So, let's probe the data outputs of these pins here and have a look. Now according to the schematic, we should have 6 data outputs that are the address lines,

**Dave Jones:** and we should have 8 data outputs that are the read-back lines. So let's have a look. On the ones, for the keyboard address lines, on the output of those, we expect to see just the keyboard data. But on the outputs that go back in,

**Dave Jones:** that go back in to the data bus, we expect to see a whole bunch of bus activity. So let's have a look. Let's start with the top chip here, U706 for those playing along at home. Let's start with pin 1, because it's pin 1, 2, 3, 4,

**Dave Jones:** and then 9, 10, 11, 12. So I'm going to start with pin 1 of the top chip there. Bingo, we've got ourselves that data bus, right? So that's all the data bus crap for the 68000 processor, so we're not worried about that at all.

**Dave Jones:** So let's expect all the other ones. Yep, that's pin 2. Pin 3, yep. Pin 4, we're looking for any, you know, short, I mean, we've got some runt pulses here, like low-level pulses here. So that looks like there's, you know, some sort of bus clamping issue.

**Dave Jones:** So that's, anyway, we'll keep looking, because we haven't found the source of that. Once again, that's pin 12, 11, 10, and 9. Okay, so they're all our data bus stuff. Now let's have a look at the other chip. The other chip must be the keyboard address data,

**Dave Jones:** which should be synced up, I'm only using single channel, but it should be synced up to that output enable pin. So this one, pin 1, yep. Bingo, there you go. That's just the selection data there, okay? So that's just the keyboard address data.

**Dave Jones:** So let's go pin 2. Bingo, same sort of thing happening. Pin 3. Ah, yes, like I said, there's only 6 of them. Two of them are the other direction, so that's fine. And bingo, the one next to it, 2. And the other 4, according to the schematic,

**Dave Jones:** I believe, should be also the keyboard address. So that's pin 9. Uh-huh, yep, we've got the data. 10. Whoa, hello. Hello. Hello. That doesn't look right, does it? We haven't seen that on the other ones. Pin 11. Bingo, pin 11. And pin 12.

**Dave Jones:** So that's interesting, that we don't see that on the other ones. So we've got some exponential, you know, capacitance decay there. So that's what we're looking for there. I'd expect them to all work identically, but they're not. So what's going on there? By the way, little tip,

**Dave Jones:** use normal mode on your scope here, when you're, it can automatically, as soon as you lift the probe off, it automatically stops triggering and shows you your last data points. This is interesting. Check it out. Probe one of those dodgy-looking lines. If I hold down the run button,

**Dave Jones:** stop button, it goes back to, you know, the good, like, what you'd expect to see on the other ones. You know, but of course, if we press any of the non-functional buttons, nothing, uh, nothing happens. Alright, if we get in there and correlate that

**Dave Jones:** with the output enable here, look at that, like it's discharged all the way to this level. That's very curious, isn't it? Here we go. Yeah, you can see the output enable, right? So it doesn't matter what the output here, it's like, it's tri-state,

**Dave Jones:** so we don't know what the bus is doing on that side. It could be entirely normal. But when the output enable goes low, we expect that output driver to drive in whatever direction it needs to based on the current, you know, keyboard mapping setting,

**Dave Jones:** whether or not the buttons push, the encoder's in a certain position or whatever. And you can see that, right? So the output, uh, enabler of that chip is working, so it's outputting that data. So the, uh, system's gonna, the processor's gonna be reading,

**Dave Jones:** like in the center of that. It goes high again, so it goes tri-state, and you'd expect it to charge up. Exactly what it does, it goes low, you expect it to go low for that period, it charges up. So the output driver on this thing

**Dave Jones:** seems to be working fine. But, you know, here's where having another unit to compare with would be fantastic, or have an experience, you know, if you're repairing these things all the time. And oh, yeah, I know that, I've seen that before, that's entirely normal.

**Dave Jones:** You know, so, but we just don't know. And why those lines are different to the other lines, I, you know, it could have to do with other stuff that's hooked onto the bus, and because we don't have the exact schematic. Ugh! And that good pin, in quote marks,

**Dave Jones:** um, is doing a similar sort of thing here. It's just, you know, it's just charging up there. If it happens to be low, it's just charging up. So I would say that's not an issue, it just depends on the output state there. So, yeah, okay.

**Dave Jones:** I'm going to say that chip is probably okay. Oops, had a little bit of an issue here. Look at this. Vertical cowl factors failed. Um, yeah. Oops! What happened is the probe I had for the output enable line on the chip accidentally shorted out to the chassis here,

**Dave Jones:** and, yeah. Oops! Yeah, let that be a lesson to you. So I'm actually going back to now suspecting like a break on the board or something like that again. Um, so I have got some alfoil on the pins here, just shorting them all together.

**Dave Jones:** Neat trick, just so that you can go in there and A, check all the continuity of the pins, which I've already done, but then it allows you to just probe around and see that everything's okay. Now if we go in here and we probe the anode

**Dave Jones:** of the diodes, for example, that common anode, right? We're getting four or five on there that aren't connected, so that's probably too many. Um, so that's got to be a configuration thing. And if I actually do some of the foldy controls here, for example,

**Dave Jones:** I can hear it come in and out as I rotate that on the encoder pins like that, and the top pin of all the encoders seems to be permanently connected to a pin. And that's for the good ones, like if I go, you know, a vertical control over here,

**Dave Jones:** that's exactly the same. So everything, and it's only the other two pins which actually, compared to all the pins referenced on here, um, that they actually short out. So, um, those pots seem to be working exactly as per the other ones. Buzzed out the ribbon cable,

**Dave Jones:** the buttons and the encoders and everything else. Everything seemed to be fine, but there doesn't seem to be anything wrong with the chips up in here. It's got regular tri-state bus activity. Everything's, everything seems to be doing okay up there. Um, you know, nothing that I really suspect.

**Dave Jones:** So it sort of brings me back to the encoder front panel button board. So I'm just going to systematically go in here, find the bus that all of the, because this is a multiplexed thing, I'm going to find the column, row or column,

**Dave Jones:** um, that all of the buttons and hopefully the encoders are hooked up to, systematically trace out those and where they go back to. But I've already buzzed those things out, but I'm being forced to go back there. So I'm pretty sure it's got to be on here.

**Dave Jones:** It's got to be. Let's go. So what I'm doing is just using a whiteboard marker here to just mark these, because you can rub them back off easily. It's not a permanent marker. So what I'm doing is I'm starting out the buttons here,

**Dave Jones:** and these are the buttons that are failing. This group in here. Because all the ones at the top work just fine and dandy. So I'm tracing out this side here. You see that there's a test pad there, a test pad there, and it goes down.

**Dave Jones:** Anyway, so what I've got here is they're all connected. Yep, it's common to there. That goes down to that one. It buggers off over to here as well. So they're all connected, no problems whatsoever. You might be able to actually see, this is just one of the curious things here.

**Dave Jones:** See this trace, this via here, buggers off up here, and it goes off here, and they've got that hole there, so they're just like disconnecting those to give you like different configurations or whatever. And they actually drill it out, and you follow it up there,

**Dave Jones:** and it actually goes to another hole up here. It actually goes nowhere. So, you know, you follow the things off, and they bugger off to nowhere. Anyway, I'm going to flip it over and see if we can trace that. It might not be that particular row or column

**Dave Jones:** or whatever it is. Murphy will say it's the bloody other one, you watch. I think I found something! Check this out! I thought, like, maybe it could be like a busted via on here or something like that. You know, it can happen, like a manufacturing thing,

**Dave Jones:** and over time it's just gone dodgy, you know, with a bit of flex and stuff like that. Okay, so this one's actually, this via actually pops up, like goes on the other side over to here. And then this trace snakes off over here,

**Dave Jones:** over here, around to here, but that is not connected. And it's not because it's got the solar mask or the tented via there. You can actually probe these. They're not, you know, like, tented right down. So it's busted! I swear! I swear! It's busted!

**Dave Jones:** There is nothing in there! I found it! Oh, this is a beauty! The failure is right there. Can anyone see it? Can you see it? Anyone? Bueller? Bueller? Bueller? Maybe with the light at the right angle? Let's go in for a closer look.

**Dave Jones:** Pause the video now if you want to try and figure it out. So here's our via going off around here, and it's not connected to the trace on the other side, and as I said, it's not the via. But look what happens if I get this in the right light.

**Dave Jones:** Looky what we have here. Look at this. What is this? That is a crack in the PCB, and look at that down in there. You mongrel! Look at that! Right across the PCB, it looks like that trace. I haven't buzzed that one out,

**Dave Jones:** but it looks like that one there is broken too, and that could be the rotary encoders. Well, it's got to be. This track is broken, which probably, it could explain why. I basically buzzed this thing out before, pretty similar to what I'm doing now,

**Dave Jones:** just not as systematically, and I had, you know, I couldn't find anything, so that led me up to the chips on the main board, and, you know, down that rabbit hole, chasing a red herring, and there's a bloody cracked front panel. Do you believe it?

**Dave Jones:** Well, it's probably pretty obvious, and people are probably screaming out, yeah, of course, people have been banging these knobs and everything else, maybe because it's got a cracked front panel on the thing. Maybe it's been dropped, it got some force on some of the knobs,

**Dave Jones:** and it's cracked. Why, as I was saying before, why I probably measured it right before is because when I was putting, probing the board, it could be intermittent. So when I actually screw the board in, it could work fine, when I unscrew it and then probe it,

**Dave Jones:** and put pressure on the board with the probe, you're flexing it a little bit, maybe it could touch, something like that, but, wow, look at that. Look. Ha ha ha! Bingo. Winner winner, chicken dinner. And there's a close-up of it, with the solder mask scraped away.

**Dave Jones:** You can certainly see how that could be intermittent, based on pressure, if you applied it to the front panel. What a mongrel. Alright, here we go, I've repaired those tracks. Let's power it back up, and see what we get. Come on. And, yeah, it seems to have, like, lost its calibration stuff.

**Dave Jones:** So, oops. Yeah, not sure what happened there. The battery-backed SRAM thing might be going. But anyway, let's now... Time per division. 50, 100. No, I haven't fixed it yet. Dammit. But the mode button works, there we go. Source. Mode. Slope. External trigger. Hey!

**Dave Jones:** And the horizontal... Nah, I've still got a broken track somewhere. Dammit. And I had to suck out one of the rotary encoders here before I seen this one, which was under the rotary encoder. Look at that. Cracked right through. So there's the other one there.

**Dave Jones:** This one up here is cracked as well, but it doesn't go off. It's just one of those ones that just buggers off to a hole, so that's nothing. So, sneaky little bugger. Woo-hoo! We now have a fully working front panel. Look at this!

**Dave Jones:** Right down to one nanosecond per division. Thank you very much for playing. And there's our horizontal adjust as well. And all our buttons work. What a bobby dazzler. So let's check it out. Let's feed in a 500 meg signal. What do we get?

**Dave Jones:** Ta-da! Winner! Yeah, it looks a bit fuzzy, because we've got some trigger jitter, plus the way it's doing it, we can actually tidy this up if we go into the display menu. I mean, you whack on your average, and Bob's your uncle. There we go.

**Dave Jones:** We just tidied that up very nicely. You'll be able to see the difference there. If we turn vectors off, we'll be able to see in dot mode, sort of, you know, more of what it's actually doing there with that persistence type display. And of course, we can hit the auto store button.

**Dave Jones:** You don't get this on modern, you know, you've got to go and turn the persistence on. You know, you turn the store mode on, and then it just, you know, makes it all really fuzzy like that. So if we actually go in and adjust the trigger level,

**Dave Jones:** you're going to see it doing that. There we go. And we're in, actually, auto trigger here. You notice how it just shot back there? We're actually in, if we go into trigger mode here, we've got, there we go, yeah, we're in auto level mode.

**Dave Jones:** So if you went into normal mode, normal trigger mode, we'll see it just, it won't trigger at all once it goes above there, rather than jump. But if we go to auto level, it'll automatically check the input, and we can just hit the erase button here,

**Dave Jones:** and that'll refresh our screen. So we don't want auto store mode on. And of course, we can whack it in single shot mode there as well, and we'll get a beautifully tidy, if we erase the screen, there we go, let's single shot that.

**Dave Jones:** Run, run, run, there we go. We get our beautiful 500 meg signal. Ah, it's like a bought one. It's a little bit down, because if I adjust that to, say, drop that to 400 megahertz here, here we go, you'll see that it's, yeah, a little bit higher.

**Dave Jones:** There you go. And then I'll whack that down to 100 megahertz. Oh, sorry. Time base is way off there. There we go. There's our 100 meg signal. So that front end works absolutely perfectly. And of course, that's with the 50 ohm mode on there.

**Dave Jones:** We can turn it back to the 1 meg, and of course it goes off the screen there. But that works fine and dandy. No worries whatsoever. So we now have a winning, single channel only, 500 meg scope. But we don't know if the second channel's working,

**Dave Jones:** and whether or not we want to shell out, what was it, the 45 US dollars for the extra hybrid ADC module on there. But what we can do is just swap, because it's easy, just take the heat sink off, couple seconds, swap it over to channel 2,

**Dave Jones:** and try out and see if that hybrid works on channel 2. If it does, you know you're going to want to buy that hybrid for 45 bucks. So what I did is took the ADC hybrid out, put it in channel 2 here, and sure enough, there's our 500 meg signal.

**Dave Jones:** No worries. So it's, well, you'd have to weigh it up yourself, but I think it's worth spending the 45 US dollars buying another tested hybrid module, whacking it in there. We've already got the heat sink, because unfortunately, you know, we had that broken module.

**Dave Jones:** Yeah, that's not really repairable, I don't think, unless anyone knows a way to easily repair hybrid modules like that. But it goes, meh, no, forget it. Pay your 45 bucks and get your module. Might be able to get it cheaper somewhere else, or something like that, but beauty.

**Dave Jones:** So there you have it. I hope you enjoyed that repair of this classic HP 54616B dual-channel 500 meg scope, and it's still, you know, quite a decent scope. Yeah, it's only got like 5K of sample memory or something like that, but it's 500 meg bandwidth, dual channels,

**Dave Jones:** it's 2 gig samples per second, you know, so it's not like it's doing interleaved, you know, one of the older, the lesser ones in the 600 series. You've got to watch out. I think it's only the 616, if memory serves me correctly, that actually has the 2 gig samples per second.

**Dave Jones:** The others are like 20 meg sample rate or something like that, and it's got to do the interleaved sampling. So just, yeah, a trap for young players, that one. If you're buying one of these second-hand, just make sure you get one that's sampling at the full 2 gig sample per second.

**Dave Jones:** But that, I mean, I've got to go through, find out what that calibration issue, but it seems to be working just fine with the power-up defaults and everything. It probably needs a good cow and a good thorough testing, but that is a winner.

**Dave Jones:** Awesome! So I hope you enjoyed that, and how we, you know, chased some red herrings down a rabbit hole, as I like to say here, and we found that A, we had a broken hybrid in there, you know, measured power supplies all fine,

**Dave Jones:** we narrowed it down to a broken hybrid module, and then the other hybrid module in there also had some dicky connections on the, you know, the screws weren't holding the hybrid module down in there. Then we started to work on the keyboard, and that one is where we went down the rabbit hole

**Dave Jones:** and chased it all over the place, and it's probably a good example of where, if I did a more thorough inspection, and I really thought about it, that, you know, it's most likely a broken trace. But, you know, a broken trace on the PCB?

**Dave Jones:** Okay, I think it actually did hit the horizontal control on here, I think that's where the force of the impact was, but it didn't break the knob or anything like that, but there's only three screw mounts on that PCB in there, so it does tend to flex a little bit if you push these in there,

**Dave Jones:** it's just got some plastic clips otherwise. So it's not the best-designed front panel, but I don't feel too embarrassed ultimately that, you know, I didn't find that first glance, because I did the right things, I buzzed them out and everything else, and I thought it was fine,

**Dave Jones:** and it may have been intermittent at the time, but I eventually came back to where pretty much it had to be that front panel, and sure enough, when you go back in there and methodically test it and visually inspect it, if I did a proper visual inspection on that board,

**Dave Jones:** I might have found it, but you've got to get the light at the right angle and everything else just to see that, so, you know, if you're familiar with scope repairs like this, you might, maybe it's a common problem, you know, people are familiar with broken PCBs,

**Dave Jones:** like, you know, you'd suspect like a rotary encoder problem with a unit of this age or something like that, no, they're all good, you clean them all up, you test them, you know, you look at the output, buzz the output while you're actually rotating

**Dave Jones:** the knobs on there, and you can see that all of those worked and all the ribbon cable was intact and everything else, and well, I suspected the drivers at one step, but anyway, you've seen it. You've just spent an hour watching this, haven't you?

**Dave Jones:** You know the story. Anyway, that is a very interesting one. So if you found that interesting, please give it a big thumbs up. It's not often that I get one that, you know, is as interesting as this one with a couple of combined faults

**Dave Jones:** and, you know, a real tricky one possibly intermittent, so there you go, I hope you enjoyed it. If you did, yes, I said give it a big thumbs up, didn't I? And discuss it down below, all that sort of stuff, yeah, you know what to do.

**Dave Jones:** Catch you next time.
