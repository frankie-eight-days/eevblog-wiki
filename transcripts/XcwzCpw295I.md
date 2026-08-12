---
video_id: XcwzCpw295I
title: EEVblog 1709 - Haasoscope Pro USB Oscilloscope: An Oscilloscope Oddity
url: https://www.youtube.com/watch?v=XcwzCpw295I
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 27, "3": 44, "4": 62, "5": 76, "6": 89, "7": 100, "8": 113, "9": 127, "10": 142, "11": 159, "12": 175, "13": 188, "14": 204, "15": 216, "16": 228, "17": 240, "18": 254, "19": 271, "20": 286, "21": 303, "22": 315, "23": 329, "24": 346, "25": 358, "26": 373, "27": 391, "28": 407, "29": 421, "30": 432, "31": 446, "32": 460, "33": 474, "34": 489, "35": 509, "36": 526, "37": 546, "38": 561, "39": 575, "40": 589, "41": 602, "42": 613, "43": 627, "44": 643, "45": 658, "46": 669, "47": 681, "48": 695, "49": 711, "50": 723, "51": 737, "52": 754, "53": 767, "54": 782, "55": 799, "56": 811, "57": 822, "58": 840, "59": 852, "60": 865, "61": 875, "62": 889, "63": 904, "64": 918, "65": 935, "66": 951, "67": 967, "68": 984, "69": 997, "70": 1015, "71": 1032, "72": 1049, "73": 1064, "74": 1079, "75": 1103, "76": 1119, "77": 1133, "78": 1146, "79": 1156, "80": 1170, "81": 1185, "82": 1203, "83": 1218, "84": 1237, "85": 1253, "86": 1267, "87": 1280, "88": 1293, "89": 1305, "90": 1319, "91": 1331, "92": 1343, "93": 1358, "94": 1372, "95": 1388, "96": 1405, "97": 1418, "98": 1430, "99": 1448, "100": 1462, "101": 1474, "102": 1489, "103": 1509, "104": 1524, "105": 1539, "106": 1550, "107": 1565, "108": 1579, "109": 1595, "110": 1609, "111": 1627, "112": 1640, "113": 1659, "114": 1674, "115": 1689, "116": 1702, "117": 1716, "118": 1727, "119": 1745, "120": 1760, "121": 1771, "122": 1785, "123": 1800, "124": 1817, "125": 1832, "126": 1847, "127": 1866, "128": 1883, "129": 1900, "130": 1921, "131": 1936, "132": 1959, "133": 1979, "134": 1990, "135": 2002, "136": 2018, "137": 2035, "138": 2056, "139": 2070, "140": 2082, "141": 2094, "142": 2110, "143": 2123, "144": 2140, "145": 2152, "146": 2167, "147": 2183, "148": 2198, "149": 2217, "150": 2241, "151": 2258, "152": 2273, "153": 2287, "154": 2301, "155": 2319, "156": 2339, "157": 2352, "158": 2368, "159": 2382, "160": 2400, "161": 2414, "162": 2430, "163": 2443, "164": 2457, "165": 2472, "166": 2488, "167": 2503, "168": 2516, "169": 2526, "170": 2545, "171": 2564, "172": 2580, "173": 2603, "174": 2620, "175": 2636, "176": 2653, "177": 2669, "178": 2684, "179": 2697, "180": 2711, "181": 2722, "182": 2734, "183": 2746, "184": 2755, "185": 2767, "186": 2779, "187": 2793}
---

**Dave Jones:** Hi, welcome to everyone's favorite segment, mailbag, where we open mail sent in randomly by viewers and companies or whoever. So, let's check it out. Thank you very much, uh, Andrew H from New York University. Hi to all my

**Dave Jones:** viewers in New York. Contains do-it-yourself electronics. Well, just so happens we like do-it-yourself electronics. And if you want to send something in, send it to EV Blog Mailbag. You got to put mailbag on it. PO Box 7949, Norwest, New South Wales

**Dave Jones:** 2153, Australia, not Austria. So, thank you very much, Andrew. Let's check it out. See what we've got here. I doubt it's what it says on the box. Cayen Tools for Discovery. I don't think that's it. I suspect it is something

**Dave Jones:** else, but we will find out. I don't think Andrew clued me up in on this. Oh, look at that thing. like a padding like a suspension thing. Wow, that's interesting. Must have had a a machine to like create the packaging for that.

**Dave Jones:** So, we got to Oh, no. There you go. Has scope um that Dr. Andy Hass might have clued me up on this. It's on the GitHubs. Um the Hassoscope Pro. Wow. We have a note. Dear Dave, you surely

**Dave Jones:** recall the infamous Hassoscope, king of the worst schematic in history. Oh, is that [laughter] that's where I remember it from. Uh, you did a two I did a two-hour video based on it, did I? Um, to explain how not to draw a schematic.

**Dave Jones:** I do remember it. I don't recall it being 2 hours, though. Well, I've learned quite a bit in the past, 7 years ago, really. Past seven years, much thanks to you. And now I've designed the Hassoscope probe is quite the upgrade

**Dave Jones:** with 2 gig of analog bandwidth. Wow. 3.2 gig sample per second. You're not going to get your full uh 2 gig analog bandwidth at 3.2 gig samples uh per second. Yes. Nyquist is still correct, but you can sync two of them. Okay. To

**Dave Jones:** oversample the analog signal, we get 6.4. Okay, fair enough. Um, all the designs are completely open source and open hardware. Beauty. I'll link in the GitHubs down below. Uh, it's been successfully funded on Crowd Supply. Nice work. And now goes for 999 Yankee

**Dave Jones:** bucks. Also including a Hassoscope ProB2 active probe available for 179 on the same site. Excellent. Um, another sucker the ser. Thank you very much, Dr. Andy H from New York. So, let's have a squeeze. This looks like it's the active probe.

**Dave Jones:** Oh, yeah. There's a little active probe in there. Oh, look at that. Oh, isn't that cute? I like that. Got a little 3D printed thing bob on it. How does I assume that clips off? Don't want to stab myself on the probe. There you go.

**Dave Jones:** There's our little active probe. Cool bananas. I can't see on the camcorder screen here what these are, but there's our front end amp over here. We've got our controlled impedance trace going over to uh the little SMA over here. And

**Dave Jones:** we've got our ground and our and our tip like that. Of course, you can, you know, get all sorts of, you know, you can solder on your own tip and everything. Um, if you're doing serious probing, you pretty much have to do that. You've got

**Dave Jones:** to either design your PCBs with probing in mind like high frequency probing in mind or you've got to do uh you know some tricky tricky shenanigans with the lowest impedance ground of course possible. The whole idea of an active uh

**Dave Jones:** probe is that they're a very low capacitance. Whilst you can get one gig bandwidth passive probes, their input capacitance even at a few puff is just too high. All you've got to do is uh run the numbers on uh the impedance of a

**Dave Jones:** capacitor at one gig of a couple of puff at one gig and uh yeah anyway um cool bananas. Uh let's look at the scope. I'll have to have a rewatch of that video. Well, watch the whole thing of

**Dave Jones:** course. Um I did do a 2hour video. [laughter] So I do remember. Yeah, and I think I relayed out the schematic. That's right. That's why it took so long. I like reorganized the schematic. I'll I'll link it in. Um yeah, I think

**Dave Jones:** that was quite a popular uh video actually. It was a good example. Um, and yeah, I relayed it out. Um, so please retain this information. Yeah, we got that on the other one. Just a European Union rubbish. Looks like uh USBC

**Dave Jones:** powered. Cool bananas. And this is not going to be just a bare board thing. Oh, doesn't that look schmick? Look at this. Wa, Bobby Dazzler. That is a beautiful PCB front panel. I've done a video on PCB front panels, but uh we've got our

**Dave Jones:** dual inputs here. Got two USB supplies here. Very handy to have two cuz you might want to do like two high voltage differential probes or you know external well or in this particular case power the uh two external active uh probes. So

**Dave Jones:** yeah, very nice. Got our 1 kHz probe compensation there uh and one split out. Okay, that's where he said you could uh sync the two channels uh together. And it's a 12bit jobby 2 gig analog bandwidth for 999

**Dave Jones:** Yankee bucks. That sounds great value. It's going to be all be in the uh well it's not all in the software but you know software plays a good part. Um sync in. There you go. Uh 50 ohms external

**Dave Jones:** trigger in. Okay. So it's interesting that that's not a high impedance uh trigger in. That's a uh 50 ohm input uh only. But this is designed for like high bandwidth, high frequency stuff. So anyway, um it's got a uh trig and an ox

**Dave Jones:** out, sync out and sync in. So um can you do more than one unit? Presumably you can cascade multiple units. Whoa, that's a Bobby Dazzler. 5V 2 amp powered and external J tag. Look at that. You don't have to open the thing to hack it. Nice.

**Dave Jones:** You know what we say here on the EV blog. Don't turn it on, take it apart. Not entirely sure what's stopping that from coming out of take the front panel off, but didn't look like there's anything holding it in there. Okay. Is

**Dave Jones:** this one of these sliding puzzle things? Because I slide it that way. Oh, I'm like something something's hidden internally in there. Um, that's weird. So, it looks like I can slide it. Can't Yes, I can slide. Yes. The entire thing

**Dave Jones:** out. There we go. What was Oh, it was the fan. Oh, right. Got it. Oh, the red PCB afficionados are going to be exciting. Uh, I went through a red PCB phase. One of my favorite uh colors. Anyway, this is version 1.27

**Dave Jones:** March uh 2025. Looks really neat. Lots of u neat lots of power supply solution over here giving the many different uh core voltages no doubt required for the um FPGA over here. This will be our so we'll have one big FPGA. We'll look at

**Dave Jones:** that. And uh we'll have our ADC over here, which is just handling both channels. We got ourselves some high frequency shielded relays over here by the looks of it. That's pretty groovy. Got a reset button there. That is neat,

**Dave Jones:** isn't it? I really like that. I really like the uh case it comes in. Solder mask on that is uh quite thick. So, it's hard to see, but all the uh split grounds are in. All the split grounds

**Dave Jones:** are in here. got all the uh tiny bypass, you know, all the little itty bitty bypass caps on there. Go, you can't even see them. The problem is with my camera, my camera, I've got uh red um focus peaking

**Dave Jones:** on here. So, everything that's in focus is surrounded by a red image. So, I literally can't see any components at all on my LCD screen here of my Sony NX80 camcorder. I just can't see anything. It looks like there's no

**Dave Jones:** components there at all cuz they're all surrounded. and in focus. I know they're in focus because um they've got the red surround on them which matches the PCB. Oops. Anyway, I do like the physical construction of that. The um the pins on

**Dave Jones:** here are bent over. That's interesting. They're they're like more of the um they're not like the solid foot uh type. They've got actual pins you can bend. And our FPGA there. I won't take the uh heat sink off, but conveniently it's the

**Dave Jones:** EP4 CE 30F 23C6N for those playing along at home. And the ADC over here is ADCR 12DL 2500 ACF. We'll go to the data sheet. But hey, this is not a full review video. This is just the mailbag. But

**Dave Jones:** aren't those relays a beauty? Thing of beauty. Joy forever. They are shielded Omron jobbies Japanese. Thank you very much. None of that Chinese relay rubbish. And interestingly, that one's got three and that one up there's got two. So, it must be um like like feeding

**Dave Jones:** that signal out um directly or something like that perhaps. Although, no, it's going into here. What's here? Is that triggering? So, that's the external split out there. I just noticed interestingly input zero and input one >> [laughter] >> That's hilarious. Another channel one

**Dave Jones:** and channel two rubbish. And we basically just got an FT 232 there um for the uh USB um serial interface. And Bob's your uncle. It's all happening in the uh FPGA as you'd expect. When I was a boy, these days it's um it's not hard

**Dave Jones:** to get a two big gig bandwidth um scope. You can see um it doesn't have a proper oscilloscope uh front end here. So, it's probably just one voltage input maybe with an attenuator like a you know 10x attenuator and that's uh that's about

**Dave Jones:** it. So, don't expect your you know your 1 millolt per division here. You're just not going to get it. Anyway, I do like how all the parts actually have the part number um silk screened on there. The exact um the full exact full part

**Dave Jones:** number. Very nice. Makes it just easy to identify in case you you know cuz some chips are just very hard to read, obscure. they might have some stupid manufacturer code on there or something like that. So, having the full part

**Dave Jones:** number on the board, if you got the space to do it, it's a very nice touch. My only criticism is I don't see why it really needs the fan like this. I mean, the fan's gone in here like this and

**Dave Jones:** it's blowing out in this direction. So, it's Yeah. And then put an arrow there. Like, blow up that way, please. And the heat sinks are in the correct direction. The fins are in the correct direction like this. But where's it going to go? I

**Dave Jones:** mean, it's not like this has uh vent ports like it's sucking in one side and outputting the other or something like that. But there is a benefit to it. It's not entirely wasted because it spreads the warm air around inside more better

**Dave Jones:** more easily and then it can uh just uh conduct uh through the case, dissipate uh through the uh top well mostly the top of the uh case in this particular case. Get it? I'm here all week. Yeah. Okay. I just I'm surprised that you need

**Dave Jones:** the fan internally for that. Like you could have got like a custom like a heat sink block and then put a thermal pad on top of there and then connected to the case up here. The problem with that is

**Dave Jones:** that this is a slide on case. It slides in. So, how do you make good thermal contact and slide it? It's you can only do that if you get like a screw down case. If this case just like screwed

**Dave Jones:** down on the top, then you could have done that. But because you've gone for an extruded aluminum case where the uh top lid actually slides in, h you can't really do that. It's one of the trade-offs of having using one of those

**Dave Jones:** nice extruded aluminum cases. All right, I downloaded the software from the GitHubs. And the GitHubs has uh yeah, all sorts of uh all sorts of stuff. It's fully documented. Everything else absolutely fantastic. Um and it's got ADC board or ADC firmware. Well, I guess

**Dave Jones:** he calls it the ADC board. Okay. It's It's the actual It's the main board. It's got Python stuff. What is that? So, it's got a Python version, does it? And anyway, I went into the distributions. It's got a Mac version by the looks of

**Dave Jones:** it and Windows. Um, that was only a couple of weeks ago. So, I downloaded that and I ran it and not only do we get this little uh command line um thing, but but here is the software and it is

**Dave Jones:** blindingly fast. Um I haven't done anything with it yet. Um this is just it immediately popped up like this and it's got voltage division voltage divisions as one volt per division to like plus minus 5 volts. It's like that doesn't

**Dave Jones:** seem right. It's almost as if like there's a bit there. It's like it's zoomed in or something displayed. What is that? AC coupled. We got our one megga ohms. So it's almost as if we're down in the noise there. I'm not sure

**Dave Jones:** what's going on. Uh, so trigger. So we're running, right? And then we can then we can single shot capture. No, we can't. Oh, yeah. Yeah, there we go. Okay. Right. There you go. But it's um it's super quick. Hang on. No. Run.

**Dave Jones:** Single run. There we go. [laughter] You can fiddle the PLL clocks, can you? That's all grayed out. Maybe there's a have to go into a advanced menu or something to do that. Uh gain 160 molts per division. So gain is minus 6. Okay.

**Dave Jones:** So it does have well 20 m volts per division. Okay. So we can go right down, but that's software. Not sure if that's hardware. I haven't looked yet. Not sure how we get the second channel up. We got

**Dave Jones:** all our measurements and stuff, but we got some live measurements down the bottom here. Four split channel one, four switch clocks, toggle PLL controls. Here you go. So we can fiddle the PLL controls. Wow. Or if you want to like

**Dave Jones:** overclock overclock the ADC and stuff, go for it. Over sampling alignment. Uh record to file update firmware. Do it via here. That's cool. Version 27.01. Jeez. Had lots of lots of sucks of the sav at that. Um so we got our grid.

**Dave Jones:** Okay. So we can turn off high-res. Turn on or off high res because this is a 12 bit. Got to remember this is 12 bits at 2 gig samples per second. It's a sorry a 2 GHz bandwidth at 3.2 gig samples per

**Dave Jones:** second. I've heard the fan come on. There's some rattling. I put my hand on it and it vibrates less, but I've heard it come on. So maybe it does get hot. And I think probably a better thermal solution. That that fan is now annoying

**Dave Jones:** me. I'm not sure. You're probably not hearing it, but that's enough to annoy the heck out of me. So yeah, I think a better thermal solution. Yeah, you got to couple it to the case, but as I said,

**Dave Jones:** you got the slide on case, so it's it's harder to get an effective thermal solution there. Anyway, we've got a dual channels and the other channels doing that. Now, the channel one lead has turned from like white bluey to red. The

**Dave Jones:** channel 2 lead is white bluey, but it looks like they're doing the same thing. So, but I suspect shorting it out, I get my little 50 shorter plug, but I suspect that won't do anything. No, because it it it shouldn't have shouldn't have done

**Dave Jones:** anything. What's going on? Uh, do I have to calibrate it? No, that's just over sampling alignment. Didn't pop up with anything. It's just 800 meg any alias. Nice. Okay, so that changed it a bit. So, the problem is we don't have our

**Dave Jones:** traditional um oscilloscope controls here. Like where's the time base? Okay, we got time nanconds here. Is that like that's not like nanconds per division? It's interesting that it has a frame counter. It's doing 3 like 90. It's almost

**Dave Jones:** pushing 400 frames per second. 46,000 events at 81 hertz at 08 megabits per second. Uh sorry. Yeah. 08 megabytes per second. Okay. Um this is not yet. This is not like it's starting sound. It's not working like a traditional

**Dave Jones:** oscilloscope interface with your trigger in your m in the middle. Well, maybe that that is the trigger point. I can't. Oh. Oh, I can drag it. Okay. Uh, axis plot options. Oh, okay. Oh. Oh. Oh, fancy pancy. Okay. So, we can do our

**Dave Jones:** power spectrum now. We can do a ton of stuff. Okay. All right. And we can do log average. Oh my god. Okay. Pretty advanced. We can export stuff. But look, I go to like manual axes, right? So, let's just go minus2

**Dave Jones:** to + two. Okay. Okay, there we go. So, we've adjusted that, but that's in volts, right? That's in volts. And where is like we're like jumping to full scale here. I don't know. Did I do something to it in the tear down? I shouldn't

**Dave Jones:** have. AC coupled. Okay. Whoa. Hello. Whoa. That's changed dramatically. What's going on? 1 megga input impedance. I can hear the relay click for the 50 ohm, but no, we've got a 50 ohm input impedance. We should be getting a flat line there.

**Dave Jones:** What the heck's going on? Show FFT. Boom. Okay. But yeah, no, we can't see anything because we got no input signal. No board zero. Okay, because we've only got one board and channel one, two. Okay, that's just changed the color, is

**Dave Jones:** it? Trigger threshold. There you go. We can adjust our trigger threshold, but that's not helping me. What the heck's going on? Trigger time, faster or slower. There's no ability like I can change my type like X-axis is right. I can go manual but that's not

**Dave Jones:** what I want. Like I I expected a traditional oscilloscope. Um I would not call it an oscilloscope. I'd call it a sampling system or something like that because it hasn't got your traditional oscilloscope interfaces. Like it starts at zero over

**Dave Jones:** here and then just displays zero to 1200 nconds. I mean we can adjust that of course. Let's Let's adjust that to like We can't even set Oh, okay. The fan stopped rattling now. Oh, no. No, it's back. Oh, that fan's dodgy as Oh, change

**Dave Jones:** the fan, please. Yeah, better thermal solution required. Um, auto 100%. Okay, so manual. So, let's go from minus I don't know 100 to plus 100. 100 what? What are the units for the x- axis? Huh? I don't get it. Am I missing something?

**Dave Jones:** What am I missing? Anyway, our ADC board's only at 30°. It's not like it's getting hot there. I don't get what's going on here. I might have to email Andy. What's to t? I don't know. Uh, delta delta what? Some difference in

**Dave Jones:** trigger threshold or something. I I don't get it. And to change our offset, we've got to go like here. Oh, mill vololts there. Okay. It's almost as if something's something's wrong with the hardware. We should get a flat like I

**Dave Jones:** can understand. Okay. If it's always doing it's not doing the regular time per division. It's only going from zero nonds to, you know, it's just re-triggering. There's no pre-trigger information, etc. Right. I Okay, I can understand that. What I don't understand

**Dave Jones:** is why the data is doing this. Do I have to feed in a signal? I shouldn't have to feed in a signal. No, I'm going to have to get back to you on that. All right. It's the next day. Andy got back to me.

**Dave Jones:** Thank you very much, Andy. um and said, "Oh, it's a USB power supply issue." And sure enough, it was a USB power supply issue. So, he said, "Use a uh powered hub or, you know, use the external 12volt DC supply." Didn't have a powered

**Dave Jones:** hub, but I've got I'm using my little Beink Mini PC. And I thought these had it's rated on the Hassoscope as 5 volts, 2 amps. So, I believe my ports are capable of that. I'm using the supplied USB cable. Still didn't work. Anyway,

**Dave Jones:** I'm now powering it from an external. There we go. 12 volts and uh 6.7 watt. Um so, you know,.56 amps there. And sure enough, we get our flat trace. Winner winner chicken dinner. Or so you think. So, I got out my function gen, my RF

**Dave Jones:** function gen, tried to feed in a signal, and I got nothing. Um just to sanity check myself, I had to get another scope. I need really need to set up an integrated scope in this uh thing. There it is. It works. Okay. I've got a 50

**Dave Jones:** megahertz 100 m volt RMS signal and I plug it in to channel one. Got my tongue at the right angle and nothing. Absolutely nothing. 320 molts per division. We can change the gain. And yes, this is actually [laughter] this is

**Dave Jones:** actually voltage. It won't change the scale here. This voltage scale is like it's just like one one voltage and the voltage is 10 mill volts per division. So that you've got to multiply that one by the 10 molts per division over here.

**Dave Jones:** So it gives you 10 molts per division. Never seen anyone do it like that before. Why just change the scale? It there is nothing. There is nothing there. There's no signal at all. Anyway, the first issue is that this thing

**Dave Jones:** should either work or it shouldn't. uh from that external 5volt uh power supply. If the power supply is not adequate, it should not communicate with the software. And you saw it, it was like it appeared as though it was

**Dave Jones:** working 300 frames per second updating where it's now doing, by the way, if you look in the bottom corner here, like 900 frames per second, but it was it it appeared as though everything was working and functional. It was talking

**Dave Jones:** to it. It was getting the coms and everything in the serial thing. Everything appeared as though it was working. So you cannot have a product where it appears to work like that but then your ADC doesn't work because

**Dave Jones:** clearly like it was just getting full scale excursions on the ADC input or something like that right um so yeah you can't have a product that does that um because people [laughter] myself included thought that it was working and

**Dave Jones:** there was something else at fault. So yeah you can't have that. You can't have it communicating and talking and appearing to work, but having a low enough supply voltage or whatever the issue was with the external USB uh

**Dave Jones:** supply there to cause it to stop working. No, that that is a product failure right there. Sorry, Andy, but yeah, that's that's that's got to be fixed. Um, and this is not drawing much. It's only like, you know, 6.7 watts. So,

**Dave Jones:** it's not drawing that full 5 volts, 2 amps um thing. That's 10 watts. So, you know, anyway, I'm getting absolutely no signal. So, I'm going to try channel two. Channel two has an offset. I'm not sure why. Um, and you can't change the

**Dave Jones:** the independent you can't independent looks like you can't independently change the volts per division for both channels. Why? I don't get it. Anyway, um, the channel one is showing up as red. It's showing up as red. So, I'm not

**Dave Jones:** sure what that means. Channel two is blue. So, let me let me plug that in to blue. No. No. I'm getting nothing. Right, it is running. It is updating. [laughter] Right, it shouldn't matter where the trigger Well, it shouldn't matter where

**Dave Jones:** the trigger level is, right? And we're a 320 molts per division. So, we should be seeing like 100 millolts RMS, which is a couple hundred millolts um peakto peak. It It doesn't work. So, I I don't know what to tell you. I'm using the external

**Dave Jones:** 12vt supply channel one, neither channel one nor channel two. And look, I'll take I'll take that signal again and I'll plug it in here and boom. And the um AC and the one one megga ohm input makes no

**Dave Jones:** difference whatsoever. I I I don't know what to tell you. [laughter] I can hear the relay click with the 1 megga. You're probably not hearing that, but trust me, that is clicking. And as I said, it doesn't have a proper um time

**Dave Jones:** per division here. And the time base here is like time factor. What does time factor mean? Like nobody uses the term time factor so slower. And you'll see it changed down here. That is just no. No. That is just

**Dave Jones:** that is just silly to have time factor um as a thing. So I don't know. There you go. That that is not the signal. That is not the signal there. No, the gain makes no difference. Something's gone horribly I can only assume

**Dave Jones:** something's gone horribly wrong with this unit. That would be just my luck, too. Bloody Murphy. I get sent a a unit that's somehow dud. Actually, I don't even know what the memory size is, the memory depth on this thing. Um, it can't

**Dave Jones:** be that high because, you know, if you're getting a dump in a thousand um frames per second, as in frames, as in one buffer, capture frame, one entire window, then yeah, I assume that's what it is. But anyway, and they're counted

**Dave Jones:** as events. They're not events. This is an oscilloscope. like we're we're not in counting event mode. Winner winner chicken dinner. Finally got it working. I emailed Andy who responded pretty much instantly. Thank you. Um who said, "Uh, hey, that's weird. Um, try

**Dave Jones:** >> [clears throat] >> uh disconnecting the USB, turning off the power, reparent. Hello, it tried to turn it off and on again. Connect the 12volt external power first and then connect the USB C." And sure enough, it works. and he said the six watts I was

**Dave Jones:** getting before didn't sound right. Should be about 10. And sure enough, it's now, not sure if you've seen that. It's now 10 watts. Um, so there you go. I'm like, why would it do that? Um, yeah, that's another thing to be fixed.

**Dave Jones:** Anyway, we have a waveform. Hallelujah. We can also get that on channel 2. And I think I figured out why the lead is red on channel one and blue on channel two, cuz that's what the colors are on the

**Dave Jones:** screen. Huh. There you go. But it starts up. I think it powers up that um it's blue on channel one. So, I don't know. So, there you have it. And we can go to the time base, which is the time. Oh,

**Dave Jones:** god. Oh, my mouse is Whoa. This Oh, no. Okay, we're back. This is interesting. We're back down to 270 frames per second. That's interesting. Compared to the thousand we were getting before. H interesting. Um I'll go to the Yes. the

**Dave Jones:** time base, the time factor. There we go. There we go. Oh jeez, there's a fair bit of uh trigger jitter there, isn't there? Okay. Whoa. Why is it not solidly triggering on that point? I don't like that. Yeah, we got that's a

**Dave Jones:** it's only a 50 megahertz signal, so I'm not sure what the deal is there. Where and also it shows 192 millolts here. I'm supposed to be 100 millolts RMS. I mean, it's an RF sig gen. So, it's going to

**Dave Jones:** assume that there's a 50 ohm load. I'm not using the onemeg input impedance. Let's try the 1meg. That's interesting. There's not much difference there between the one meg and the uh 50 ohm. So, anyway, um yeah, it doesn't it doesn't like that triggering.

**Dave Jones:** Why are we getting so much trigger jitter? There's no trigger filters or or anything here. We've just got rising condition, ring rising, falling. There's no either or. Um, so you know it hasn't got that basic scope functionality. And

**Dave Jones:** of course, uh, yeah, we do that and it's just going to auto trigger. And of course, we can single shot capture that. Hello. Single. Single. Single. Why is it not turn normal? Single. Why is it not capturing that now? Because

**Dave Jones:** this trigger threshold is moving like this. I I think it does have pre and posttrigger data because it seems Yeah, it's it's like triggering in the middle, but the time bases like just the way the axes are labeled. I just I just don't

**Dave Jones:** like it at all. No, no, no, no, no, no. So, why is that not singleshot triggering? I don't know. Run. Look, it's it's a relatively stable trigger. It's not as good as I was expecting. Um it's not like we're right up at the 2

**Dave Jones:** gig bandwidth or anything. Um, it's only 50 megahertz. We stop that and we single shot. I'd expect to see like a different weight. It It's not refreshing. I'd expect to see a different waveform. It's not. Single shot's not working. Anyway,

**Dave Jones:** let's adjust our gain here, shall we? There you go. Okay. 320 molts per division. That's like the highest input um that we can do. So, you multiply that by what is it? Yeah, five. Five divisions there. So, we can go all the

**Dave Jones:** way. So, let's let's go for a lowle signal. So it is designed for lower level uh signals. You can of course use a times uh 10 or a divide by 10 uh probe. There we go. There's a 1 millolt

**Dave Jones:** RMS signal. Why have an 8 m volt per division r? Is that a there's no relay click there. Is that changing at all? Feeding directly in with an RG58 coax. Presumably it's the 50 ohm termination inside the scope. Haven't actually put

**Dave Jones:** an ometer on there to measure it. um 1 millolt RMS coming from my Ry Gold DSG815. You can see that the signal's there. You know, it's it's low level. It's 1 millolt RMS, but you know, I expected better than that. 10 millolts RMS

**Dave Jones:** signal, and we're still pretty How you doing? Okay, so yeah, I'm not sure of the exact attenuation. Have to have a look at the schematic, but oh my god, I'm getting into a full review. This is ridiculous. This is supposed to be just

**Dave Jones:** a mailbag thing. So yeah, it's almost as if we're we're supposed to have a 12 bit ADC and we're supposed to I wonder what true range we're actually on and whether or not we're down in the down in the

**Dave Jones:** noise there and and interpolation is there like I don't see any like sinx onx interpolation settings or anything like that. Let's try the spectrum analyzer. Show FFT and Okay, there's our FFT. Can we do anything on that? Can we zoom? No,

**Dave Jones:** we can't zoom in. We can just drag it around. Can we left? No. Okay. Just check it. See if it aliases there. No, it doesn't. Just vanishes into obscurity. And And that's even without the 800 MHz anti-alias on, which I can hear a relay,

**Dave Jones:** by the way, with the 800 MHz anti-alias. So, something's doing there. Back to 100 millolts. It's It's jittering like buggery now. So, it looks like the FFT functionality just it doesn't have any ability to do anything apart from just

**Dave Jones:** do the full sweep. I can't even change that. Now, I can't change any of the parameters of the FFT by the looks of it. So, that's not a lot of use. Okay. Well, I'm 200 megahertz now, and you can

**Dave Jones:** see Well, let's turn off the 800meg anti-alias. It's just it's it's useless. Like this is a 200 megahertz signal and this is supposed to be two gig bandwidth, right? Okay. Trigger threshold. Okay, we're in normal mode. Now we're in auto. Okay. Yep, that's

**Dave Jones:** working as expected. But look at the there's just no sampling resolution there at all. And that depth we had. Oh, okay. Oh, is it the No, no, no, no. The depth is the memory depth. No.

**Dave Jones:** Oh my god. No, this is only 200 meg only. Right. Turn off the second channel. Maybe it's multipplexing between the two channels. No, I'm I'm I'm still not getting anything there. Like the triggers right in the middle. It's very simple. Rising edge 200 MHz

**Dave Jones:** sine wave. And that's what we get. No, hang on. It says down sample too small. And I've disconnected my coax and it's still showing a sine wave. This is interesting. I just switched the power off and like so 12 volts is

**Dave Jones:** completely off. So it's being powered. It switched back to being powered from the 5V USB and I got this down sample too small but it's still updating the screen. And look, we're getting [laughter] we're still getting like that triangle

**Dave Jones:** wave. [laughter] Wait, I I've completely repowered this thing again. And I've talked to Andy again, and he said, um, for really fast triggering, you've got to set this toot, this, um, time over threshold, he calls it, uh, to zero. Why? I don't know.

**Dave Jones:** Okay. But now look at the waveform that I'm actually getting. The triggering still sucks ass. Okay. [laughter] Like it's just jumping around like a jack rabbit. Um, which is crazy. But I am actually getting a better looking sine wave now. Okay. Now it is better

**Dave Jones:** looking. This is still 200 megahertz. So why is it why does it look different? Why does it magically look different now? And he said, uh, yes, it does actually, um, have when you have the, uh, the sample rate halves when you have

**Dave Jones:** the two channels on that and you can see that. Okay. But I was turning off the two channel thing before and I wasn't getting this sort of sine wave. I'm sure I'm going to have to review my footage,

**Dave Jones:** but damn. Okay. I like But yeah, I there's too many inconsistencies with this thing. And I've set time over thresh. What is delta? Don't know what delta is, but anyway. But time over the threshold is not helping. Okay, with a

**Dave Jones:** 200 megahertz signal, it's not helping at all. So I like there's nothing else to adjust, right? I stop it and then it's still the singleshot trace doesn't work. Oh, I figured out the single shot thing. You got to put it in single mode

**Dave Jones:** and then you've got to hit the run button. Are you kidding? [laughter] And look how it's jumping around. You just saw it jump severely there. Oh god, no. No, no, no. This thing's Sorry, Andy. This is just too painful. Sorry, Andy. This is just

**Dave Jones:** too painful. I can't I can't use this thing. It's got no proper oscilloscope functions. It's got Looks like it has no signs on X interpolation. That looks like linear interpolation to me. No, sorry, Andy. This software needs a lot

**Dave Jones:** of work. needs a lot of work. I like the hardware. The hardware seems really good. Apart from the fan, I can still hear the fan. Um, you mentioned that the fan might have come loose. I don't know. Maybe, but it's rattling like buggery.

**Dave Jones:** Um, it was still stuck to the top. It was still stuck to the lid, but I can put my Yeah, I can put my hand on it and Yep. It stops. It stops that. It's getting quite warm. It's getting quite

**Dave Jones:** warm cuz uh, you know, this thing's drawing 10 watts. fan's a bit dodgy. And Andy has very quickly fixed the uh jitter issue that we were um seeing. It's quite a bit later now because I've had other things

**Dave Jones:** to do, but uh yeah, he very quickly fixed the jitter thing. Um so I've got to update the uh firmware and this new version of the software with some uh new stuff as well. So I've downloaded that from the GitHubs and I'm running it and

**Dave Jones:** it doesn't seem to run now. So, I presume that's because it's the new software with the old firmware. So, let me with the Yes, new software with the old firmware. For some weird reason, the old software shutting down. That's

**Dave Jones:** weird. I'll try the new software again and try and update the firmware. Okay, so I turned it on. Now, I'll plug it in.

**Dave Jones:** No. Do I have to like reboot or something? There's no end to problems with this thing. Unfortunately, it's not polished. It's not doing I swear it was talking before. [sighs and gasps] No, I accidentally ran the Well, I

**Dave Jones:** didn't accidentally. I ran the old software again. So, maybe that's triggered it. Maybe I have to reboot this thing. Oh, again. All right. Now, it's working. It is running. So, I don't know. confusion with the old software or

**Dave Jones:** something. This is the new software that with the old firmware. So, but I need to update the firmware to fix the trigger high frequency uh trigger jitter. Andy found that there was a bug in there. Let's go file update

**Dave Jones:** firmware. Coincidence auto RPD was not found. So, there's wrong path somewhere. So, I've got the path here, but it doesn't because I'm running the executable from the distribution subdirectory. Um, I guess it doesn't know where the ADC board, it can't go back enough

**Dave Jones:** directories and then into the ADC board firmware perhaps. Okay, it looks like it's going back one directory and then ADC board firmware. So, I've copied the ADC board firmware into one subdirectory under where I'm executing that from. So, maybe let's try

**Dave Jones:** that again. File update firmware. Aha, winner winner chicken dinner. So, that's another thing that needs to be sorted. Um, yeah, like just uh pop up a sub pop up a window and ask where the firmware file is. That's just way easier

**Dave Jones:** rather than hard code in there. Uh, do you really want to update the firmware? Yeah, Andy's told me do not unplug it while it's updating. Um, that would be you would have an unpleasant day. Um, so yes, erasing flash. All right, it's on

**Dave Jones:** the way. Let's wait. Write in. Write in. This is all good. This is one big ass project. There's a lot of stuff to write. Took 68 seconds. Now we're reading. [laughter] It's doing a check some, is it? Yep.

**Dave Jones:** Yeah, it's verifying the right. Tell you what, it's a lot of work to develop a project like this. So, once again, hats off to Andy for um seeing this project um through. It's It's really quite something. Verified. There you go. Took

**Dave Jones:** 138 seconds. Uh clock uh clock out ENA enable or something. Now, false and was zero. Okay, I guess I reboot now. Oh, should be a message there like please reboot now. Otherwise, I don't know. Okay, I assume it's done. I'm

**Dave Jones:** going to reboot it. It's written. It's verified. And it says it took 138 seconds. So, I think we're good. So, I'm going to disconnect the USB. And I'm going to recycle the power. And from Windows, I think I'm going to have

**Dave Jones:** to restart the software, too. Fair enough. Yep, we're back in. Uh, is there a firmware? Oh, I don't know even what version it is. Python version. No, firmware version 27. I'm not sure what it was before, but anyway, we got

**Dave Jones:** firmware version 27 now. So, let's see if we can do our 200 meg signal again. See if we get the same sort of jitter. I'm pretty sure I'm feeding in a signal. 100 mill volt signal. What's going on? No, I'm going to reboot

**Dave Jones:** the whole thing again. uh really doesn't like if I just connect the USB before I like I pair it up, connect the USB, and then I start the software. It doesn't seem to like that. Found no device. Oh,

**Dave Jones:** now it's it's weird. It's just it's it doesn't seem consistent. Okay, I've turned the power on. Haven't plugged in the USB. I'm waiting. It's listening. It's listening. And it's it's not going to do it. Right. If I plug that in, it's not

**Dave Jones:** going to do it. Start it up again. There we go. And now it's Now it's running. Now I'm getting a signal. I haven't touched the signal. So why I was not getting a signal before and now I am.

**Dave Jones:** No. No. Sorry, Andy. This is just there's there's there's too many issues with this. I'm having way too many reliability issues with this thing. Anyway, let's see if we can uh trigger on this sucker. Uh no is the answer to

**Dave Jones:** that. He must have unless he hasn't included the firmware in the new build. He did put the firmware he sent the firmware to me separately, but then he said and sent an email a couple of days later saying, "Oh, no. I've updated the

**Dave Jones:** software or you can just do update the entire software." Um which so I presumed it just had the latest firmware in it. But no, there doesn't seem to be a high frequency trigger fix. No, I just realized I'm still running the old

**Dave Jones:** version. So, it looks like it Andy didn't update the GitHub thing. I have to do the direct links that he emailed me. So, yeah. No, I I just assumed it was he had updated the GitHub, but he hasn't.

**Dave Jones:** So, I'm gonna Yeah. Okay. I have to do all that again. I'll spare you the details, but I've got the new versions downloaded now. Woohoo! There it is. Firmware version 28 required for new trigger phase calculation. [laughter] All right.

**Dave Jones:** And I just realized why the firmware wasn't detected because if you ran the Python version, that was in a subdirectory under or two subdirectories under the distri the Windows or Mac distribution version. So that's why it couldn't find the path. If you ran the

**Dave Jones:** Python version, it would actually find the path. So, that's something that needs to be fixed. So, if I show you Hassoscope Pro 29, he did the fix in version 28, but I'm going to install the new 29 uh firmware. So, ABC board

**Dave Jones:** firmware. So, I can copy that, but if you see, if we go into software, there's the Python version. So, if you go down one directory, it'll work for the Python version. But we have to go to No, we we

**Dave Jones:** have to put it here. No. Yes. Here. The ADC board firmware there. And now it will find the version 29 firmware. So we'll do that again. Update firmware. Yes, I do. It found it. No worries. I'm getting the hang of this. All right. I

**Dave Jones:** finally got the latest version 29 installed. And let's um I still don't like this slower faster thing. Um Hey, there we go. Yes. Yes. Okay. high frequency jitter fixed. No workers. And I think there's a few other improvements

**Dave Jones:** and stuff like that. So, let's go up to 320 meg. 320 mgahertz. That should give us uh 10 samples. So, obviously, we're not going to get to our 2 GHz analog bandwidth here with 3.2 gig samples per second. That is not a thing.

**Dave Jones:** Unfortunately, we're still supposed to be 50 ohm input termination because the 1 megga ohm is off, right? And we're 179 mill volts RMS and I'm feeding in 100 millolts RMS. So, uh that's, you know, proper RG58 coax. Um that should be matching, but it's

**Dave Jones:** not. You know, I can understand if you switch it to one meg and then it's out ski, but uh no. So, I'm not sure what's doing there. I'm actually measuring 55 ohms input impedance there. So, that's a fair bit that's like 10% out from the

**Dave Jones:** nominal 50 ohms. So, I'm not sure what's doing there. Where's our second channel gone there? There used to be a like a in the older version, there used to be a two channel version there. Okay, now we have trigger stabilizer

**Dave Jones:** option. Okay, I'm going to try my Leo Bodner um Pulse Gen and see what we get with that. The good thing is I can just use that 5V USB power output to power the little That's great. [laughter] Whoa. Whoa. There. There we go. There we

**Dave Jones:** go. Whoa. There big fella. Slower. There you go. So, there there is our sig gen. But we do have some ringing on that input there. That's That's not the best. Um, so there's a little bit of mismatch there. Don't know

**Dave Jones:** if that's that 55 ohms versus the 50 ohm and 26.32. So 32 is 1 gig. Um, that's not 2 GHz bandwidth, but I think we're at the limit of our Leo Bodnar pulse gen there. But um, yeah, we're getting some ringing

**Dave Jones:** on that. I don't know. I'm not going to do a direct comparison with another high bandwidth, like a one gig bandwidth um, scope that I've got here. But but anyway, there you go. I spent um way too much time on this for a mailbag, but I

**Dave Jones:** wanted to win. Damn it. I wanted to win um and get this thing working. Thank you very much, Andy, for uh being patient with me and uh doing the updates and stuff like that. This unfortunately needs a lot of work. The software needs

**Dave Jones:** some more work. It doesn't like, you know, like I can't even do like a bandwidth limit. Like where's where's my st industry standard 20 MHz bandwidth limit? And there's a ton of other stuff. It doesn't work like a regular

**Dave Jones:** oscilloscope. The user interface needs work. Hey, but it's all completely open source. So, somebody come along and take it and just pay. All it needs is update to the user interface. A few little polishes. And so, the hardware looks

**Dave Jones:** pretty good. Apart from that um it being able to power it um from the USB and it thinking that it works and it doesn't. And then you have to like power it from the external 12 volts. That's no. No.

**Dave Jones:** That's that that's got to be fixed. But as long as you know that, as long as you know the limitation of that. Um, and there's a few issues with getting it to talk. Uh, you know, you got to power it

**Dave Jones:** up in a certain sequence and things like that. But anyway, it's a very interesting bit of kit. And seriously, hats off. This is a lot of work to actually get this thing to market. Um, and I'll leave the link down below. You

**Dave Jones:** can actually, um, buy this. It's the new Pro model. You've been able to buy the other one, which is was crowdsourced. I believe that's pretty popular, the old um, uh, Hassoscope one. um and like sold thousands of them and you can still get

**Dave Jones:** that one I believe. But uh this is a new pro model. Needs a bit of work in the software side of things, but yeah. Anyway, it's interesting. Thank you very much Andy. I'll link it in down below.

**Dave Jones:** >> [music]
