---
video_id: kdCfAR06GeI
title: EEVblog #777 - Keithley 177 Microvolt DMM Repair
url: https://www.youtube.com/watch?v=kdCfAR06GeI
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 17, "2": 29, "3": 49, "4": 65, "5": 77, "6": 97, "7": 113, "8": 129, "9": 145, "10": 161, "11": 177, "12": 197, "13": 217, "14": 229, "15": 241, "16": 265, "17": 285, "18": 305, "19": 321, "20": 337, "21": 353, "22": 373, "23": 397, "24": 417, "25": 437, "26": 457, "27": 481, "28": 501, "29": 529, "30": 553, "31": 573, "32": 589, "33": 609, "34": 625, "35": 641, "36": 665, "37": 681, "38": 697, "39": 713, "40": 729, "41": 745, "42": 761, "43": 777, "44": 793, "45": 813, "46": 825, "47": 837, "48": 857, "49": 874, "50": 890, "51": 902, "52": 918, "53": 934, "54": 959, "55": 975, "56": 991, "57": 1015, "58": 1028, "59": 1048, "60": 1064, "61": 1084, "62": 1105, "63": 1125, "64": 1141, "65": 1165, "66": 1177, "67": 1194, "68": 1210, "69": 1226, "70": 1242, "71": 1259, "72": 1275, "73": 1287, "74": 1307, "75": 1327, "76": 1343, "77": 1360, "78": 1380, "79": 1392, "80": 1404, "81": 1424, "82": 1440, "83": 1456, "84": 1473, "85": 1489, "86": 1513, "87": 1537, "88": 1558, "89": 1574, "90": 1590, "91": 1606, "92": 1622, "93": 1638, "94": 1662, "95": 1683, "96": 1699, "97": 1715, "98": 1727, "99": 1743, "100": 1763, "101": 1788, "102": 1808, "103": 1832, "104": 1849, "105": 1865, "106": 1881, "107": 1901, "108": 1921, "109": 1938, "110": 1962, "111": 1983, "112": 1999, "113": 2019, "114": 2036, "115": 2065, "116": 2077, "117": 2105, "118": 2117, "119": 2141, "120": 2162, "121": 2186, "122": 2210, "123": 2227, "124": 2243, "125": 2259, "126": 2283, "127": 2299, "128": 2316, "129": 2332, "130": 2352, "131": 2364, "132": 2381, "133": 2397, "134": 2413, "135": 2433, "136": 2457, "137": 2478, "138": 2498, "139": 2514, "140": 2534, "141": 2551, "142": 2571, "143": 2588, "144": 2604, "145": 2620, "146": 2636, "147": 2656, "148": 2677, "149": 2697, "150": 2713, "151": 2729, "152": 2749, "153": 2770, "154": 2786, "155": 2810, "156": 2834, "157": 2859, "158": 2879, "159": 2895, "160": 2911, "161": 2927, "162": 2948, "163": 2964, "164": 2984, "165": 3000, "166": 3016, "167": 3029, "168": 3045, "169": 3065, "170": 3081, "171": 3093, "172": 3118, "173": 3134, "174": 3146, "175": 3162, "176": 3178, "177": 3194}
---

**Dave Jones:** Hi, I thought we'd have a shot at a repair video. This is an old mailbag sent in by Richard quite some time ago. And he killed it with about, or someone at the company killed it with about 30 kilovolts or so. It was, well, wasn't, I don't think it was

**Dave Jones:** directly into it, but it was nearby. And, well, yeah. It blew a few things. So I thought we'd just have a crack at it, see if it's actually repairable. It's not a bad model. If you can actually still pick these up very cheap on eBay.

**Dave Jones:** And they're still quite a venerable bit of kit, because they're really quite precise. 4.5 digit, they've got low voltage and current ranges. 20 microamps, for example, 20 millivolts, which you don't commonly get these days. 4.5 digit, really quite, you know, it's old school, but hey, still pretty useful.

**Dave Jones:** So let's have a shot, see if we can repair it. Let's go. I've showed a brief overview of this on the mailbag, but yeah, it's like a manual range job. None of this auto-ranging rubbish. But as I said, look, 20 microvolts, 20 millivolts with 4.5

**Dave Jones:** digit, that's really actually quite useful. 20 ohms range as well. It's not a bad bit of kit if you can pick one up. And I love the spec sheet on the base of the unit. Fantastic, don't need a manual. All multimeters should have this.

**Dave Jones:** 0.03% class, plus 1 digit. Awesome. You know, on all your basic voltage ranges. And yeah, as you can see, it's still pretty impressive. 0.04% on ohms and stuff like that. And made in the United States of America. One of the things I really like about this meter, look,

**Dave Jones:** full calibration procedure on this shielding plate here. It's got a, that's what this little clip here is for. Just shield it, you take that off and you get access to all the through-hole parts. Nothing special on here really, apart from the main logic device

**Dave Jones:** I think. Anyway, we do have some schematics for this thing. This comes from the EEVblog forum. Somebody got this one out of an eBay ad. Somebody actually took a photo, somebody selling it took a photo of the service manual, and it's not that

**Dave Jones:** bad. I don't think there's a really good scanning. And somebody else on the forum had this one, which they, it was a bad copy, but they sort of like filled in the blanks themselves with different colors and things like that. So yeah, we do actually have a half-reasonable

**Dave Jones:** schematic to go by anyway. And you can safely buy this anywhere in the world, because thankfully it has a switchable tap transformer, 240 volts or 110 here. So I'm going to keep it on 110 because it has one of these funny plugs on it, which I'm not going to bother to

**Dave Jones:** change, so I'll just power it from my 110 volt transformer here. Now this one in particular, Richard pointed out that he changed this diode bridge down here blue, so he has replaced that with some, just some single diodes, it's a bit how you're doing.

**Dave Jones:** And the only other physical damage on it is a blown resistor down in here, which is actually on the output here, so that's rather interesting, but I don't expect sort of, you know, blowing the output amplifier here would affect the rest of it, but it could.

**Dave Jones:** Hey, you never know. And it uses a pretty standard intercell ICL71C03. This one's dated 19th week 1980, and you might be able to still get one of those if you're lucky, but yeah, but if that sucker's blowing well, we're obviously not going to be able to fix it today.

**Dave Jones:** But first thing you do of course when you're looking to repair something like this is what we're going to do in a minute, you actually test it to find out what's wrong with it, but you also give it a good visual. Now we've

**Dave Jones:** got that blown resistor down here, we have a known blown diode bridge at blue open down there, so we're especially going to want to check out the voltage regulators and the voltage rails, although I'm sure Richard's already done that after he made that mod.

**Dave Jones:** And I can't see anything else visually blown, there's no blowholes in any of the chips really, although we're talking about 4000 series CMOS, and when the known failure mode of this, here's his letter, 30 kilovolts in close proximity to the DMM, you guessed it, it killed it.

**Dave Jones:** So when you've got stuff like that happening, yeah, you've got to suspect 4000 series CMOS stuff, they're not very robust. And we've got a fuse missing here, but that's neither here nor there, that's not going to stop us doing anything. So there is a chip

**Dave Jones:** missing from this socket down here, but I believe that is like an expansion type thing or something like that, I believe. So yeah, that's not actually a missing chip. This model's very interesting in that the front panel terminals, which look like high-quality tellurium copper of course, with the low ranges

**Dave Jones:** and being Keithley of course, the masters of low voltage, low current, look it just connects directly in to the top pins of these gang switches, so don't go taking that off, because, you know, well if you do make sure you record where they go, because you could easily

**Dave Jones:** goof that up. Just do some basic checks first to figure out what's wrong here, I've got my precision resistor, let's hook it up. Hey, it's like nah, that doesn't look good, does it? 20k range, 2k range, no, that should be reading 1k, so that's

**Dave Jones:** no good at all. And by the way, this thing, this meter does have a zero adjust on it, so if you put to voltage here, and you can actually tweak the thing, you probably go down low enough. There we go. You've got a

**Dave Jones:** low voltage ranges for example, you really have to zero this sucker out. Alright, and that's different again, so pretty much our resistance is completely shot. I mean, it's yeah, over range, okay. You know, and if we disconnect it, like it's measuring something, because it's flashing because it's over range, so

**Dave Jones:** it's doing something. It is, hey, hello, there we go, that's bang on. That's a k. Our 200k range is actually bang on. Let's step that up a bit. And oh, look at that. Oh, no. What? No, it's all over the shop. Yeah. What's going on?

**Dave Jones:** Wave my hand over it. Nope. There seems to be some sort of charging thing happening. So look, if I switch it to 200k, it's just going up and up. It's like it's charging up, and yeah, something's maybe it'll get to the 10k. Will it overshoot?

**Dave Jones:** I don't think so. Oh yeah, no, it is. It is overshooting. I thought it would taper off there, but slowing down, slowing down. So that's quite unusual. Put that to 10k, it's going to do exactly the same thing on the 10k range. So that's

**Dave Jones:** fascinating. But obviously the ADC's doing something and it's not far off. So sort of I suspect the ADC, you know, might be okay at this stage. Really, that's just, no. It's almost finished. Hmm. Now the voltage range seems to be doing a similar thing.

**Dave Jones:** I'm back to 20 millivolts here and that's supposed to zero out, but it's just doing that sort of charging, discharging thing like we saw before. So it is certainly one sick puppy. But check out the voltage! That's not too shabby whatsoever. Now let's

**Dave Jones:** actually go down a range. We're over-ranging there. Let's go down to 1 volt. Once again we've got that charging thing happening. It just keeps charging down like that. It's really weird. Look, it's bang on on the 20 range, and the 200 volt range as well.

**Dave Jones:** Oh, no, see? Now it's not. It's not consistent. Oh, that is one sick... look, now it's consistent. If I go up there, yeah, it's consistent again, but oh, there we go. See? Bang on. But... if I switch ranges, it just seems... ah, now

**Dave Jones:** it's come good! It was like flaky before. Let's over-range it. Oh, you saw it though! It was all crusty. Ah, it's these flaky issues, these intermittent faults, that can often be difficult to track down, because they... if they're not consistent, then you don't have a consistent trouble...

**Dave Jones:** a consistent fault to actually troubleshoot from. But now it's come good. What is there? You know, some sort of warm-up issue? Something or some sort of intermittent connection? Or something else? Hmm. Weird. I mean, you know, I dick around with the connections, and it's all fine.

**Dave Jones:** And... oh, no, there we go! No, there we go! It's done it again. Now when you're working on mains power gear like this, just remember safety first, of course. No matter how experienced you are, you can really come aguts it very easily. Now, yes, I've turned the power off.

**Dave Jones:** Now this fuse here is all exposed. That is a mains fuse. Here's the direct mains wiring coming in. And look, an exposed mains fuse. So we'll just whack some electrical tape over that. Just temporary, we can take it off later, just so we don't make a mistake

**Dave Jones:** and oops, accidentally brush it. And of course the golden rule of troubleshooting, thou shaltest voltages. So we'll just test the rails here. It's got plus 15 volts written there, minus 15, and plus 5 written here. Where do we find our ground, for example?

**Dave Jones:** Well, you could take a look. Like that star ground point for that capacitor, that looks like for all the world, like that's a common ground there. So I'll just try that first. Here we go. So we'll give that a burl. There's our plus 5 volts, and yep, 5.07.

**Dave Jones:** There we go. Plus 15, yep, and minus 15. Yep, fine. So our voltage rails, no problems whatsoever. That's not the issue, bummer. You always hope it's the voltage rail, because that's the easiest thing to fix. Now as far as troubleshooting gear goes, the holy grail you'll want is not only the schematic, but

**Dave Jones:** you'll also want a troubleshooting checklist. And we actually have that bingo, a checklist of all the things that you need to know to actually have that bingo AD converter check step. One, two, three, we can actually just go through this and thoroughly check it.

**Dave Jones:** It kind of like takes all the fun out of the hunt, but I don't know, I don't think like we could skip say the, like it's already done the voltage test on another page. Like I wouldn't bother with the display checks, because our display obviously

**Dave Jones:** works, you know, nothing wrong there. It's like negative going signal lasting for 200 clock pulses, you know, we don't have to measure stuff like that. I'd jump straight into the AD converter checks, and this confirms my first guess would have been, well, thou shalt check

**Dave Jones:** voltages. We've checked the plus minus 15 and the 5 volt rails, and so next thing we check is the reference voltage. And there it is. We check test point 2, TP2, 1 volt, and we've got a list of test points here, but they are actually labeled on the board.

**Dave Jones:** Sometimes they're easy to miss, but anyway, it's down here. I've now got a clip lead, a ground clip lead here. This is actually the ground connection, it tells you on there, although you could figure that out, measure it for yourself. But no worries,

**Dave Jones:** so we'll check test point 1, which is supposed to be ground as well, and it is. And next one, test point 2, we're supposed to get 1 volt, precisely. And bingo, we're bang on. So nothing wrong with our reference voltage at all. Now here's one I wouldn't have guessed to do

**Dave Jones:** or I wasn't, you know, I wouldn't be game to do it with, certainly not at this point of the troubleshooting, is to actually force a voltage into the ADC. And actually the next step, it tells you that after measuring the 1 volts that we got there, it actually says to short out TP1 and

**Dave Jones:** TP2 there. And that will, that connects the reference output to U106, which is presumably the analog-to-digital converter input, and it should display 1 volt plus minus 2 digits. And if those are correct, the AD conversion is A-to-D converter chip, this inner cell one is functioning correctly.

**Dave Jones:** So yeah, we definitely want to check that. Rule that out right now. Now I wouldn't actually, like, directly short it out. A good way to short stuff out is to actually get your multimeter, put it on amps range, because A, it's fuse-protected, and you could even put a large fuse on the amps range.

**Dave Jones:** I've got the milliamps range, for example, and you can actually see, it gives you a direct readout if there's any overload current. Like, it shouldn't be in this case, but hey, you know, let's give it a bell. So hopefully, yeah, you can see that screen.

**Dave Jones:** We've got it on volts, I don't know which range we have to put it on, but we've got it on 2 volts here, so here we go. I'm going to short out those two test points. And let's see if we get 1 volt

**Dave Jones:** on the display. Bingo! 1.00.999. So there's nothing wrong with our analog-to-digital converter. Can rule that one out right now. Beauty! That's a huge relief. Now because we got precisely 1 volt on there, then, well, if steps 4 and 6 are correct, then the AD converter is functioning properly.

**Dave Jones:** If not, continue with step 7 and the rest of them. So technically, we can just, we don't have to do anything more. That analog-to-digital converter chip is working just fine. But, you know, as a matter of course, I might just go through and check a couple of things in here as well.

**Dave Jones:** Because remember, what we're seeing is perhaps some intermittent faults here, so yeah, we could have maybe just got lucky and you know, it just so happened, whatever the fault is, just so happened to be working to give us our AD converter. Because we've seen

**Dave Jones:** that it's spot on in some tests, and in other tests it's not spot on. So I think it's worthwhile just to continue with these tests, you know, probe around, do a few things, just keep measuring stuff, and hopefully, you know, like something might pop out.

**Dave Jones:** It's just worthwhile, it doesn't take much time. Although it might take time on the video though, unfortunately, as I explain things and stuff like that. Usually it doesn't take this long to troubleshoot stuff, but when you shoot in video, eh. And we can skip the next test because it's just

**Dave Jones:** checking the clock for the analog-to-digital converter, we know that works. So let's go TP3 should be, it should be the stored auto-zero voltage, there we go, it should be 1 volt plus minus 0.1 volts. And there's TP3, ah, that's near our blown resistor up there.

**Dave Jones:** Aha! Almost had an amps range there. Here we go, let's test our auto-zero. No, but with no, we're a volt. So no worries at all. So next step is U105 pin 11, that's our delta-sigma node voltage to the integrator. So unfortunately, it doesn't

**Dave Jones:** have any component designators on here, there's no silkscreen overlay. So we need ourselves the component overlay here from the menu, and no guess and surprise for guessing U105 was the one that we saw up there before with that output connector, that resistor is the

**Dave Jones:** one that's burned out. And we had measured a test point down in there before, which was 1 volts. So it's telling us now to measure pin 11. Pin 11, and yeah, we're a volt. No worries at all. Next step, pin 14 should be minus 1.2

**Dave Jones:** which is the output of the integrator. Aha! Look! Bingo! There it is. And that's what we're measuring. Look, we're up to step 10, U105, pin 14, minus 1.2 plus minus 0.2. It's nowhere near that, the integrator output voltage. Bingo! No surprises for guessing that

**Dave Jones:** output, that chip there, haven't actually looked at what it is yet, is probably cactus, because it was connected to the output here, it's had that resistor blown out of it, no surprises for guessing that that chip might be Gonski. Let's take a close look at that.

**Dave Jones:** There you go, it's the burnout resistor, and it's not a common thing, it's an ICL8052, is that an integrator chip? I'm not actually sure. I'm going to have to go to the data sheet. Now here's where it gets interesting. You know how over here I thought before that this ICL71CO3

**Dave Jones:** was the main ADC? Well, I'm right, it is, but so is this. It's got a second one. Oh, let's take a look at the data sheets. Now this had me thoroughly confused for a few minutes. I've got the data sheets for both of these devices.

**Dave Jones:** This is the ICL71CO3, which is this big puppy here, which I knew was the AD, well, you know, I assumed was like the sole ADC. And then we've got this puppy up here, which is the ICL8052A. And if you look over here, it's actually got ICL, this is another data sheet, when I searched for

**Dave Jones:** 8052, I got this data sheet, and it was the ICL8052 without the A on the end, but it's designed for another, it looks like companion chip, and it's got a ICL71CO3. So they've got a data sheet for a combined chip set. And it doesn't make sense until you actually look at

**Dave Jones:** this data sheet on its own, which is what we've actually got. We've got a combined ICL8052A and an ICL71CO3, and they've got the two different pin-outs on here for the two different chips on the one data sheet. Oh, that's confusing. And then we've got this

**Dave Jones:** Oh, that's confusing. But anyway, check it out, it's a pretty schmick device, it's designed for 4.5 digit meter, from 200 millivolts to 2 volt at full scale, and then you have the resistor dividers, of course, to do everything else. But it's got a medium quality reference in it,

**Dave Jones:** 40 ppm typical on board, it's not too shabby at all, 5 puff input current, oh, that's pretty awesome. It's got guaranteed zero reading, it's got guaranteed accuracy plus minus 1 count, that's where that spec comes from, over the full 20,000 count range, it's got 2 microvolts peak-to-peak noise over the 200 millivolt range,

**Dave Jones:** it's not too shabby at all. And here's the block diagram, which I've added some color. This is the smaller chip which we're having a problem with at the moment, which we measured the output voltage from, and we the output, what was it, the output of the integrator or something?

**Dave Jones:** And we'll have an issue with it, so that's in red, and the bigger chip is in green, which handles the multiplexer and the counter and the control logic and all that sort of jazz, and the direct analog input as well. So it's weird that they've actually put the analog input

**Dave Jones:** on the main chip, which handles all that, and then that's got to be fed out here, into the actual buffer and integrator itself. So, you know, this is kind of like where the magic is happening, and then fed back in, and then it's fed back in

**Dave Jones:** and displaying directly on our 4.5 digit display there. And if we have a look at our test procedure, we were trying to measure here this, pin 14 of U105, and we should have got minus 1.2 plus minus 0.2, and what we were getting, like 0.6 volts

**Dave Jones:** or something, that's the integrator output voltage. Now if we go over here and take a look, there it is, pin 14, there's our integrator output voltage. Something wrong happening here, this thing is not integrating at all. What can go wrong there? Eh, it could be one of these resistors blown, or it could also be

**Dave Jones:** the main integration capacity here, perhaps. It could certainly be the chip, the kitchen chip could be cactus, but we know that the internal reference is working fine, but that could be like, you know, a separate part of the silicon, like, you know, something else

**Dave Jones:** could be dead around here. So, eh, not sure what's going on there. Let's go back to the schematic. If we have a look at the schematic here, I can't actually see that output terminal on the back, so it's not coming from here, and if we go back to the board, we might see why.

**Dave Jones:** So if we have a look here, here's our output terminal, but it's the output negative terminal. Here's our analog output. So you can see the trace running across here like this. This is the resistor that's had the R's burnt out of it, but it's actually the ground terminal here.

**Dave Jones:** So, and that's connected through to pin 7 of the chip, which is actually the ground pins. And that's connected through to pin 7 here, big, fat-arse trace. And if we have a look there, pin 7, you might think is the ground, based on, you know, a usual pin-out of the chip, but it's not,

**Dave Jones:** because it's some analog, you know, weird-arse analog chip, doesn't follow the usual rules. Pin 7 is actually the plus 15 volts input for the internal reference. Now, we know the plus 15 volts is OK, so I think that's blown resistor there really has nothing to do with this

**Dave Jones:** chip here. It is just something on the output is, you know, fried through to the 15-volt rail. Maybe that's why the regulator and the diode bridge and everything was dead. But it seems that, well, this may or may not have survived. I mean, there's something seriously

**Dave Jones:** wrong with this section, most likely, because we're not getting the voltage output of our integrator that we actually expect. But, yeah, it's maybe, in a roundabout way, it's caused some damage here, but not directly into that pin, as you might think. Now, of course, one of the

**Dave Jones:** simplest things to do here is check our integration capacitor. There it is, it's a dead giveaway. It's a, it's not just a regular ceramic, it's a polytype, and it's going to be ultra-stable as these reference cats now need to be. Now, where luckily, these are, you know, these are, you know,

**Dave Jones:** luckily, this chip is actually socketed. Why it's socketed? Well, the other chipset is, part of the chipset is socketed too. It's a pretty critical chip, so they maybe decided, yeah, we need to socket it. That comes in handy. Hard to measure this in circuit.

**Dave Jones:** Normally you would unsolder one lead, lift it out, measure the capacitance. But in this case, we can just get in there, pop the chip out, and one lead of the capacitor will be free, of course, going nowhere, and we'll be able to measure it.

**Dave Jones:** And we don't need to be hugely accurate, of course, it doesn't matter, it's the type of capacitor. There we go, and it's 222.22 mic. No problems whatsoever. Scrap that, but hey, that's a test that you wanted to do. Just to make sure, just to rule out that integration capacitor hadn't failed.

**Dave Jones:** You can actually see, that's a 160 volt cap down in there. Fairly hard to damage, but you know, we know that this thing has had some, you know, a 30 kilovolt transient. It's blowing the arse out of this resistor. Some, you know, relatively high voltage, high power

**Dave Jones:** event has happened, so it's not out of the bounds of reality that, you know, some sort of transient event could have blown our, you know, caused like a little blowout inside our sampling capacitor. That kind of would have, you know, explained some of the charge-up stuff we were seeing

**Dave Jones:** and things like that, perhaps, with the display before. But it's not there, that looks pretty good. And just to make sure, there we go, no problems whatsoever. We can increase the frequency, we can go up to 100k on that, no problems whatsoever, there's no leakage,

**Dave Jones:** everything looks fine. So our integration cap's fine. Next up, let's check our 100k resistor, unlikely to be dead, but because the chip's out of circuit, this pin's, these two pins are floating, bingo, we can measure that directly in circuit. So I've got one

**Dave Jones:** lead on one side, the other lead on the other side, lead on one side, there we go, that's 100k, spot on. Next up, those guilty-looking diodes in there, let's back-to-back, let's have a look at those, and here we go. Doesn't matter which way we get it, 0.5

**Dave Jones:** yeah. Ah, dodgy bloody alligator clip, hopeless. And yeah, that looks good. Ah, look at these horrible single-wipe sockets, there's no contact on the other side, I hate these things, they're awful. Horrible to see that in a Keithley instrument. Now let's go back to this output pin again, because

**Dave Jones:** this says output ground, and it just dawned on me that doesn't make sense. You know how I said that according to the data sheet, pin 7 there is connected through to the plus 15 volts for that, to power that internal reference. But if we have a look, so that didn't make

**Dave Jones:** sense that this output would have been plus 15 volts, and if we actually go over here to the actual schematic of the Keithley instrument, pin 7 is actually grounded. Ah, different to the data sheet. Now we'll go back to the golden rule of troubleshooting, thou shalt

**Dave Jones:** check voltages, and we'll actually check, even though we've checked the rails, let's just make sure the rails actually get to the chip. So we're looking ah, pin 8 is plus 15 volts, and pin 1 is minus 15 volts. So pin 8, plus 15 volts,

**Dave Jones:** there it is. Pin 1, minus 15, no workers. Now here's where I start to get a little bit concerned, because here's our analogue output, that's the one with the blown resistor on it. This is the resistor down here, going down to ground, that is blown.

**Dave Jones:** Why is that blown? But anyway, let's not wonder why, let's look where that's actually likely connected to, because it was probably connected up to something, when it blew. Otherwise, how could that blow? You've got to have current flow through there to blow the arse out of that

**Dave Jones:** resistor, and look where it's connect, look where the positive one is connected to. Sure, it's 100k, it's 100k series protect, well, we've got a low pass filter there, but here is protection resistor going into our main converter chip here, and here's all the analogue switching in here.

**Dave Jones:** So this chip just contains various analogue switching that controls the integrator here. So, ah, yeah, you've got to you can't help but get the heebie-jeebies thinking, mmm, have we actually damaged the input to this somehow? But, I still have confidence, because we are actually able to get this

**Dave Jones:** thing to measure bang-on. So it's, you know, like sometimes, so it's just sort of intermittent in some ways. So anyway, still haven't checked this AC coupling cap up here, we haven't checked this one down here, I don't think we've checked these diodes, so need to check a few more things around here first.

**Dave Jones:** So we'll check this puppy in here, that should be 4, it's just got 4 on it, so that'll be mic, so that'll be 4 microfarads, so it's this one here, this huge one. So we can't always get away with measuring in-circuit like this, it's still got the chips in, but because it's surrounded

**Dave Jones:** by analogue switches, I think we might be able to get away with it. So, there we go, 4.1 mic, but because we are measuring in-circuit, let's just use a little trick of swapping our probes just to see if there's any influence. No, it's

**Dave Jones:** basically exactly the same. So yeah, high confidence, that cap is just fine. But I wasn't as lucky on this one microfarad cap here. Yes, it measures one microfarad, but I had to remove the chip to measure it. Now I've gotten to the point

**Dave Jones:** where I was going to probe the output of our integrator here, pin 14 that we measured before, the 1.2 volts, because there is actually a waveform in the manual for that, and here it is, and here's why it's typically 1.2 volts that you're actually going to, you know, measure.

**Dave Jones:** Nominal, and it only briefly goes down to minus 10 during the integrate part, and then the reference integrate ramp, and then the auto zero for the next conversion. And yeah, I did that, but the thing is, like, working now, like rock solid. It's like rock solid working.

**Dave Jones:** 1.9 volts here, 1.9 volts. And you can see that the waveform is bang on to what it said in the manual here. It basically ramps down for 100 milliseconds, and we're at 100 milliseconds per division there. Oh yeah, here we go. Ramps down for 100 milliseconds, and then ramps up

**Dave Jones:** for 200 milliseconds, and then stays idle for 100 milliseconds, and then starts again. And it's basically, it's not quite down to minus 10 there, but yeah, close enough. So yeah, well that'd only be for full scale, wouldn't it? That would actually depend. I can actually show you that.

**Dave Jones:** Let me decrease my voltage to, say, 1 volt, and let's do that again. Let's single shot capture that. And it should be lower amplitude. Yeah, so the lower amplitude, the peak, what it goes down to there, it can go down to a maximum of minus 10 for full scale,

**Dave Jones:** but in this case it's only a volt, so which is like half of full scale. So it's only going down, well it's not even that, but yeah. It's only going down by, yes it is, half. 2 volts per division, 2, 4, 5. There we go, so it's going down to half of what it's capable of,

**Dave Jones:** because that's how these slope-based integrators work. They ramp down to a certain value, and once they hit that book, they ramp back up. So we might have gotten to the annoying point where this damn thing is working again. There's like the 10 millivolt range.

**Dave Jones:** Okay, I can whack it up to the 200 millivolt range, I'll go up, there it, well, actually I should just go all the way up to 1 there, and go down a range. 100 millivolts, no whackers. And 1 volt, 10 volt, it's working just fine.

**Dave Jones:** Let me check the resistance. Okay, but our resistance is still the same, it's just slowly rising up. So it should be, so it could be something wrong with our resistor current source. Hey, we might have something new to track down. That'd be nice,

**Dave Jones:** because that voltage seems to, no matter what I do with it, I jiggle things around, do all sorts of stuff, and it's working, oh there we go, like 1.02k. Aw, aw, stop working, damn you. Yeah, that's near enough. So it works there, but it didn't work for the, oh, no, look, yeah, see it's all,

**Dave Jones:** these aren't, these leads aren't dicky, are they? No, no, no, see something's wrong with the resistance, I'm not sure what. So, as I said, there is a separate resistance current source for this thing, maybe we should take a look at that. Oh, no!

**Dave Jones:** The voltage is playing up again! Oh, doh! What the hell is going on here? It was rock solid before, I was playing with it for a while, and it was absolutely bang on! And now it's just oh, look, that's fine! Now it's come good!

**Dave Jones:** Oh, bloody intermittent faults, hate them! But, before I start mucking around with that ohms source up here, I'm actually going to have a look at this chopper amp down here. And it actually says that down in here, it actually, for the ohms source

**Dave Jones:** and the resistor checks, it actually says go and check the chopper amp first. So yeah, I thought that was worthwhile too. So, now I'm going to go through the procedure for the chopper amp. Damn! Look at that, that's the ohms range, I shorted it out, and we're getting this

**Dave Jones:** garbage here. Oop, it just came good when I gave it a bit of a wiggle. What's going on there? But that doesn't account for counting up like that. Something weird-ass going on there. Back on the ohms range, I did actually test all of the AC volt range, I got my

**Dave Jones:** function gen out here and put in and measured all the test points, and it all measured fine. So AC voltage was actually fine. And now back on the ohms, yeah look, it's counting up, and if I selectively, like I'm really putting pressure on those

**Dave Jones:** banana plugs now, so it's not a front panel contact thing. I'm going to wiggle the internal wires with the tongue at the right angle. Wiggle is actually a time-honoured technique, and there is a, there are units of wiggles. They're colour-coded with skivvies, and Australians will get what I'm talking about.

**Dave Jones:** And so it's not that. So there's nothing, no funny business going on there. But you saw it before, didn't we? That it went down to zero, and this, and if I change ranges, you watch, it'll bloody go down to zero. No it doesn't!

**Dave Jones:** Ah! Ah! Now actually, like 20 minutes ago this actually was working, it was zero. I was actually getting zero on there, and so I don't know what the, how the deal is. This thing is weird. Let's just touch in this, the main converter here, and

**Dave Jones:** was got, yeah, it started going back down, and then I touched it again and it went back up. Bloody dual single-wipe sockets. I'm going to, actually I haven't taken that chip out yet, I'm going to take it out and see if there's any corrosion and then reseat it.

**Dave Jones:** No, well it wasn't that, I just reseated the chip and checked it out, and yeah, we're still oh, there we go, just, just, like came good. Just came good. No, it's gone again. No! And if we actually measure the current source in the ohms range, it's supposed to be a milliamp, and

**Dave Jones:** sure enough, it's actually a milliamp. And sure enough, yeah, you know, it's good enough. You can see, that's actually measuring our shunt resistor inside here. So there you go, if we change ranges, we can see our shunt resistor actually changing there. But yeah, that's a milliamp.

**Dave Jones:** So the current source is okay, but once again everything, no, that's good now, it's come good, right? And then, I don't know, bang, there we go, like, jeez, gang switches or something? Intermittent gang switch? Okay, I think we might have it. I think it was what I suspected before, Dickey

**Dave Jones:** range switch. Watch this. Ta-da! There we go, it, there we go. That ohms button, right there. That is the culprit. And I couldn't repeat that before, but Dave too is feeling quite chuffed, because while I was out, he had a play around with it

**Dave Jones:** and he, yes, narrowed it down to the, the range. The ohms switch, and that makes perfect sense. Now if we actually leave it, I think it'll go bad, won't it? It'll, I think if we don't touch it, I think it eventually goes bad again.

**Dave Jones:** So, okay. So, what I suspect, I'll show you what I suspect is happening here, okay? You remember how we've traced this blown resistor before? You remember how we had the blown resistor on the back, okay? That one's had the arse blown out of it.

**Dave Jones:** So some high-power event has happened through at least this ground terminal. And you've got to think, well, maybe it's happened through here before. You know how I said I suspected this, the front end of this, with these analog switches here, might have been damaged in some way.

**Dave Jones:** But we've already proven that this ADC works absolutely fine. There's no problems whatsoever. It's, you know, yeah, there's an intermittent issue, but it does measure bang-on. Okay? So as I said, like, could have blown the input, but it also could have pitted. I, you know, if you get a

**Dave Jones:** if you get an arc on that contact in there, it could have pitted. I reckon it's the center contacting there, because it happens in ohms mode, which is there, and in non-ohms mode, i.e. volts or anything else, over on this side. So it's most likely to be that common thing.

**Dave Jones:** And if, of course, that's not making contact, the input here to our ADC is floating. Hence why we're going to have that charge. It's going to act as a high impedance. It's no longer being driven by a low-impedance source wherever it comes from

**Dave Jones:** where it comes from the chopper amp down here, or whether it comes from the AC converter, et cetera, via the switch configurations. It's charging up. Slowly, because it's a high impedance source. So that's what's doing it. And when we go in there and

**Dave Jones:** touch it again, we're making good contact in there, and it's coming good. So it looks like that is a pretty good bet that it is the ohms contact. And that was the conclusion I was coming to a little bit back, but as I said, I went in there and checked the chopper amp,

**Dave Jones:** I got in there with the scope, and I checked the waveform, and it was 390 hertz, exactly what it should be. And everything was, you know, everything with the chopper amp and everything else was hunky-dory. We checked out everything around here except when it was failing.

**Dave Jones:** That pin 14, that will get in the, we weren't getting the minus, what was it, 1.2 volts? We can go back and check it with this switch in the good position. So I just measured it, and well, I'll show you. You remember how we were getting,

**Dave Jones:** we were supposed to get in our checklist, our very first checklist where we actually found an issue. Minus, it's supposed to be minus 1.2 on pin 14 of U105. That's the smaller chip of our chipset there. Plus minus 0.2, okay? And we're getting

**Dave Jones:** we still are not getting that. We're still getting exactly what we were before. And specifically says to put it on the 2 volt voltage range, okay? And that's where we're on, and it's not there. And it's nothing to do with the switch, is it?

**Dave Jones:** So I don't know what the deal is there. Our integrator output is not there. So I thought, bugger it. Why use one of these newfangled digital meters? Let's get out a real meter. Simpson 260 here. So let's try it out. Let's measure that as well.

**Dave Jones:** Eh, it's exactly the same. There you go. Hmm, in fact if I squint one eye and line up the needle, it's bang on 0.66. Ha ha, beauty. Hold onto your hat though, folks. Okay, we're like, yeah, we're all hunky dory here. If I put a little bit of

**Dave Jones:** pressure, it was doing it. Hey, there we go. It was doing it before. The voltage switch is now doing, look at that. The voltage switch is doing the business. I'm putting no other pressure anywhere else except that voltage switch. And now sort of, maybe I'll, oh, there we go.

**Dave Jones:** Come in from this direction. Ah, it's going to be good now, you watch. But you saw it, you saw it. We have it on videotape. So, yeah, have we got multiple dodgy switches? Ah, I wouldn't put it past Murthy. Okay, so we've discovered

**Dave Jones:** something funny. This is great. The contact here, we're reading ohms. This is the 10k resistor. Yeah, the precision 10k. And if you notice, I'm not sure if you can see that, if I fiddle with this, I'm getting negative ohms, which is only possible

**Dave Jones:** with active components. Wow, yeah, we're getting some. So we've got a whole bunch of, at least the ohms and voltage switches that we've found are dicky, right? So that's got to be the entirety of the problem, right? That's got to be the entire problem, is, you know, it explains when

**Dave Jones:** you've got a bad contact, as I said, you get high impedance state, you're charging up, negative again, right? This is in. This is engaged. The worst reading ever. Negative 0.7k. There we go, it's bang on again. Oh wow, what a shocker. Alright, I am convinced that this thing

**Dave Jones:** is evil. It even measures evil. So yeah, I think that is the whole thing, the bloody gang switches. As I, you know, originally sort of started to suspect there, although we still have to, you know, try and clean and fix them. We did waste a lot of time

**Dave Jones:** if you remember this AD converter checklist, we should have actually stopped at that point and not measured the rest of this. But, you know, I had good reason to think that, because intermittent, you know, the symptoms, you know, we knew that there was some sort of

**Dave Jones:** transient event, there could have been some circuit damage, so it was worthwhile going through and checking these, but if we didn't, we wouldn't have found that discrepancy in the integrator output voltage there. Still don't know what the deal is there, but I'm not concerned about that, because the ADC works.

**Dave Jones:** Okay, absolutely works, bang on. So, I'm not sure if the manual's just wrong in that respect, or there's some other thing, but anyway, so that's just a red herring. So we, you know, wasted a bit of time there checking some of the components around

**Dave Jones:** you know, around the ADC, here around the integrator and stuff like that, but you know, it's like, you know, five minutes worth of work if I didn't have the camera on or something. So, you know, not a huge amount, but yeah. Bloody switches!

**Dave Jones:** And these switches are usually pretty good, but you've got to remember the age of this thing. It's like chips are like 1981 vintage here. This thing is almost 35 years old, okay? And as I said, still a useful meter if, you know, it's reliable.

**Dave Jones:** But yeah, so something's gone dicky here, but I know a lot of these meters are still going fine after these 35 years. So anyway, I think, as I suspect, we might have had a transient event which has actually pitted, arced over, damaged one of the contacts in there, making it sort of really unreliable

**Dave Jones:** in the voltage, you know, at least the ohm switch, and probably at least the voltage switch as well in there, but now you can see this metal strapping actually joining all of these switches together. And so, unfortunately, you can't just, like, desolder the two suspect switches, and

**Dave Jones:** I don't even think they're disassemblables to actually fix them. So, you know, but even if you wanted to get them out, you've got to desolder all of them, and oh man, that's the stuff nightmares are made of. So about all we can do is

**Dave Jones:** hopefully get down between the pins there with some contact cleaner, and give it a go, there's many different types of contact cleaner, this one will do the business. This is highly flammable, by the way, you don't want to squirt this on like powered up stuff.

**Dave Jones:** So, and you've got to let it evaporate before you turn it back on as well. But hopefully, you know, we can maybe get down in there, and yeah, it's vanishing, it's going down the holes, so maybe we can get something happening down in there.

**Dave Jones:** But as I said, like, if the contacts are pitted, and things like that, you know, the odds are not good of this thing actually, you know, being super reliable in the future. I wouldn't bet any money on it at all, it could be too far gone if those contacts are really

**Dave Jones:** you know, it's not just dirt, it might just be dirty contacts, but if it truly is like a, you know, some sort of arcing event, then yeah, we could be screwed. So while that stuff's in there, you just want to operate these puppies, give them a bit of a wiggle,

**Dave Jones:** get them like half in, maybe you could like spray them in different orientated with the switch in the different positions and things like that, but generally that lubricating oil's going to get down in there, so that's alright. And we'll just let that puppy dry upside down, so the

**Dave Jones:** some, you know, excess lubricant maybe, hopefully falls back out of those top contacts. And what do you know? We're looking pretty decent now. No worries at all. That's I can't get it to fail yet, although it's going to require significant playing around to, you know, to verify that.

**Dave Jones:** Because if you just see it once, then you know, if you see one little bit of dickiness, you know that yeah, it's, you know, you wouldn't trust this thing, but the first minute of playing around seems fairly solid. And likewise on the voltage range here, we're hunky dory.

**Dave Jones:** Yeah, that's all looking, it's all looking pretty good. Although I might actually go through and spray all the switches actually, just as a matter of course. You probably would in an instrument of this age anyway. So that was a given. And that might have been some people's

**Dave Jones:** first port of call was to go, has it got dicky switches in there? But, you know, because we had the note which said, oh yeah, look there was the diode bridge was blown, we've got the burnout resistor on the output, all sorts of things, you know, slowly charging up, all that sort of jazz.

**Dave Jones:** You know, like the first thing you wouldn't have thought of, the first thing, or I didn't anyway, is that it'd be the gang switches. And as I was playing around with it, like to start off with, it didn't seem to be any repeatability.

**Dave Jones:** In like, you know, as I touched them, it didn't seem to do anything like that. And as you may have seen on the video at one point, you know, just sitting here, it would suddenly come good. It'd go bang. You know, and so yeah, without actually physically

**Dave Jones:** disturbing anything. So yeah, it could have been something electronic, but eh, unfortunately, because this is the electronics engineering video blog, it wasn't. It looked like we've had a mechanical issue here. Bloody mechanical crap. Now it's interesting to note that the switches under question here,

**Dave Jones:** these ones here, they're, you see how they've got the holes in the top of them there, they've actually got gaps down there and the lubricant can, you know, you can actually see it vanishing down into the contacts. These ones over here seem to be much better

**Dave Jones:** sealed, or almost fully sealed. So I'm not sure how I could, if spraying those is going to be of any benefit whatsoever, because there doesn't seem to be any path to actually seep down into the contacts, but these ones definitely do. So there you go, that was a bit of a wander up the garden path there.

**Dave Jones:** Red herring with the integrator output voltage and stuff like that. Still not entirely sure what's going on there, but I'm, you know, 100% confident that this puppy is now working. Apart from the switches, still don't know. Still need to do lots of, you know, dicking around and testing with it

**Dave Jones:** to make sure it's all good. But there you go. That's what can happen. You know, if you've got something like this, that's what can happen. You know, because you don't know whether or not given the symptoms of this thing and the story behind it

**Dave Jones:** with the 30 kilovolt impulse and the burnout resistor and the burnout diode bridge and all that sort of stuff, it can easily lead you up the garden path like that. I might have saved, as I said, a little bit of time if I actually believed the

**Dave Jones:** follow the instructions precisely, and it said, oh don't worry about the ADC anymore, you know, don't look here, it's fine. But, you know, it's worthwhile going through those sort of checks, because it could have been turned out to be an intermittent component issue.

**Dave Jones:** But it looks like, no, it wasn't, it's just a bloody dicky contacts. And it just goes to show how you can easily spend hours and hours, you know, debugging and trying to fix these sorts of things, being led up all sorts of garden paths everywhere by just, you know,

**Dave Jones:** sometimes you get lucky and you'll choose the right path, other times you'll just go in an entirely different direction, because, you know, it seemed reasonable at the time, and we ultimately didn't waste too much time on this. I know this video's probably like 45 minutes long or something like that, sorry about that.

**Dave Jones:** But anyway, it's interesting, I hope you learned something. Just from the procedure and things like that of actually doing it. Even if the procedure didn't turn out to be the most efficient one, in this case we still ultimately found the problem, and it would have, you know, there's no doubt it would have popped out in the end.

**Dave Jones:** I was strongly suspecting there that it was the gang switches at that point. But yeah, oh, bloody dicky intermittent faults. They can be a real pain in the butt. And yeah, sorry, I guess the EEVBlogger repair curse strikes again, because I didn't get a real interesting electronics troubleshooting

**Dave Jones:** fault on this one. I said, bloody, you just squirt some stuff in the switches and fixed. So yeah, hopefully one day I'll get something that has a really good, you know, electronic fault that I can trace down and fix, but I don't seem to have much luck there.

**Dave Jones:** Geez. Anyway, hope you enjoyed it. If you did, please give it a big thumbs up, discuss all that sort of stuff down below. If you like the t-shirt, I'll probably link that in down below as well. You want one of these triple five timer t-shirts or any of my t-shirts?

**Dave Jones:** Because I do actually make a decent commission on these shirts. So Beauty, thank you very much. I've also got available from nowadays, these are regularly available from Teespring, but there's also, a viewer put me on to a UK provider, which basically does the same thing, and apparently

**Dave Jones:** the postage is much cheaper in the EU. So if you're in the EU, I think you can get postage a lot cheaper, so I'll put in links to the t-shirts on those sites as well. So thank you very much, Richard, for sending that one in, and as much as I'd love to keep this thing, the lab's

**Dave Jones:** getting a bit crowded, I've already got tons of meters, so I think I will give this one away to a worthy viewer. I think that's a nice thing to do. So if you're preferably a youngster and you don't have many meters, so if you've got like a ton of meters, please don't apply.

**Dave Jones:** Australia only, otherwise it's too expensive to ship overseas, it's not really worth it. So if you're in Australia and you're a youngster and you want this puppy, leave it in the comments and I'll pick someone and send it away. Catch you next time.
