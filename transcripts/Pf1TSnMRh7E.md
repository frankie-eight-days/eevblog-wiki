---
video_id: Pf1TSnMRh7E
title: EEVblog 1612 - Siglent SDS1000X HD 12 bit Oscilloscope Teardown
url: https://www.youtube.com/watch?v=Pf1TSnMRh7E
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 34, "3": 51, "4": 67, "5": 83, "6": 103, "7": 117, "8": 132, "9": 147, "10": 162, "11": 175, "12": 187, "13": 200, "14": 213, "15": 230, "16": 244, "17": 262, "18": 283, "19": 298, "20": 314, "21": 328, "22": 343, "23": 360, "24": 373, "25": 390, "26": 407, "27": 425, "28": 440, "29": 451, "30": 466, "31": 479, "32": 496, "33": 512, "34": 527, "35": 540, "36": 552, "37": 568, "38": 583, "39": 598, "40": 609, "41": 622, "42": 636, "43": 652, "44": 663, "45": 678, "46": 688, "47": 704, "48": 718, "49": 733, "50": 745, "51": 760, "52": 774, "53": 787, "54": 800, "55": 816, "56": 836, "57": 848, "58": 862, "59": 876, "60": 894, "61": 907, "62": 924, "63": 938, "64": 949, "65": 965, "66": 986, "67": 1001, "68": 1013, "69": 1024, "70": 1040, "71": 1052, "72": 1066, "73": 1080, "74": 1094, "75": 1113, "76": 1125, "77": 1138, "78": 1151, "79": 1168, "80": 1187, "81": 1197, "82": 1213, "83": 1225, "84": 1237, "85": 1248, "86": 1259, "87": 1272, "88": 1286, "89": 1303, "90": 1316}
---

**Dave Jones:** Hi, it's a Siglent scope teardown time again. Thank you very much for Siglent for sending in not one but two of their new scopes. We've got the SDS 1204 XHD or the basically the 1000 XHD series here, four channel 200 MHz jobby. We've

**Dave Jones:** also got the new SDS 800 HD series and HD of course meaning 12-bit. This is 200 MHz. Both of these four channel. Now, I put a a poll on Twitter/X and the majority of people said they wanted to

**Dave Jones:** see the bigger bad boy first. So, let's take a look at it. Teardown time. Just one thing, I'm getting the 1000X out of the box here and I noticed that the Styrofoam rubber baby buggy bumper on the end is like bent in like that and

**Dave Jones:** well, I can feel that the scope is actually touching the bottom of the box. So, it looks like that has actually failed. So, let me get this out and have a squeeze. Yeah, I don't know. That should be

**Dave Jones:** adequate. Maybe the box isn't sized correctly. It's slightly too big and it just allowed it to slip out like that. Perhaps, I don't know. Anyway, it's worth looking into. I don't think there's any damage though. And of course, it's any color you like as long

**Dave Jones:** as it's black and for the film aficionados, here we go. Oh, yeah. So, this is the SDS 1204 XHD, the top of the range model. So, 200 MHz, 2 gig samples per second, 12-bit. We're talking 100 meg points of memory.

**Dave Jones:** We've of course seen the 2000 series before. So, it's basically a cutdown version of the 2000 series and 2000 series was excellent. So, I'll link in that video if you haven't seen it. So, I believe it's a similar sort of specs.

**Dave Jones:** So, you get the 100 meg point of memory, which is more than enough turn these days, and it's got a 10.1 inch capacitive touch screen, very nice, of course. You don't get the vertical controls over each vertical channel. Now, you can't,

**Dave Jones:** otherwise the oscilloscope would be like this wide or something crazy like that. So, nice sort of like width form factor here, and yes, we do have 50 amp inputs on all the channels. We've got the serial bus interface for the optional

**Dave Jones:** logic analyzer, two USBs on the front, and calibration, and all serial decodes built in for free, which is nice, of course. And but it does not have a built-in function generator, but you can actually get it, and you can do boat plots and everything

**Dave Jones:** else with that, but it's an external USB unit. So, yeah, not not built in, but that's what Siglent are doing these days. So, price-wise, you can actually get this for 999 Yankee bucks. Sorry, I'm not going to do

**Dave Jones:** all the prices in all the different countries. Work in US dollars. Street price 999 dollars, but that's only for the two channel version. As I said in previous videos, I do not recommend anyone buy a two channel scope anymore,

**Dave Jones:** and pretty much you shouldn't even be buying an 8-bit scope anymore. 12-bits with this new HD is the new standard. So, yeah, I would recommend four channels HD 12-bit minimum these days. So, yeah, I don't know why they make the

**Dave Jones:** two channel, but I don't know, education, all that sort of stuff. But no, if you're after a scope, get a four channel. Trust me. So, the lowest price four channel 100 megahertz version, the 1104X, that's 1399 Yankee bucks, but the

**Dave Jones:** model you see here, the top of range the 200 megahertz is 1699. Still, for what you get, incredible bang for buck. And one of the things I absolutely raved about on the 2000 series was the diecast metal alloy handle.

**Dave Jones:** Wish this was feeler a vision, but ah, this is just gorgeous. Gorgeous. Why can't all scope manufacturers make a hand and like a diecast alloy handle like that? It's just the ducks guts. On the back here, we get a large cooling

**Dave Jones:** fan, we get a Kensington lock, external trigger input, auxiliary output for triggering. We get LXI LAN as standard, another USB port and a USB host as well. Very nice, but unfortunately Siglent have the trend has continued in having

**Dave Jones:** no HDMI output. So, unfortunately, the competition and even the much lower price competition has HDMI output. So, ah, that's an oversight. And if you compare it with the 2000XHD series, it looks like absolutely identical key layout on it. I can't see any difference

**Dave Jones:** whatsoever, but they've changed from the beige to the black. But, the difference comes in the serial interface. This is a HDMI connector here and that one uses a a cartridge connector in there for a module. So, different. Why can't they stick with the

**Dave Jones:** same probes? Maybe they're now standardizing on this across all their ranges. I mean, the 2000XHD only came out like a year ago when I did that video. So, yeah, they've changed it, unfortunately. But, the other difference is is that the 2000X actually has a wave

**Dave Jones:** gen built in instead of a separate USB dongle. I would use a comically long screwdriver, but unfortunately, not Phillips. Oh, yeah. So, you know what we say here at the EVblog, don't turn it on, take it apart. And they got Loctite

**Dave Jones:** on the screws. Nice touch. Ah, please, calibration void if seal broken my ass. And the feet, there's the mechanism, the snap plate for that. It's not the best feeling thing. It's a bit ah, it's a bit weak sauce, but anyway,

**Dave Jones:** I've seen worse. There's the gorgeous diecast alloy handle, BUT THIS ONE'S even more betterer than the 2000 cuz it's got a nicer textured surface. Oh, what a Bobby dazzler. All right, so let's take it off. Will it be the same as the 3000?

**Dave Jones:** Yeah. Yeah, sorry, the 2000. Yep. I was wondering if it was going to have the cutout for the BNC for the optional wave gen and it surely does. So, whether or not you can upgrade this, I don't know. And I'm pretty confident

**Dave Jones:** everything inside is going to be identical layout because you'd be mad to reuse everything. And once again, they've got these nice little alignment pins here on the side. So, let's Yeah, we're in. And tada, look at that. Was that Is that exactly the same power

**Dave Jones:** supply arrangement? I think it is. It is an identical layout, but the power supply is different to what we had in the 2000X and this unpopulated power protection board up here looks exactly the same, but this little board down here with the AC

**Dave Jones:** coupling on it, that has changed. Once again, it's branded Siglent the OEMs for a lot of Teledyne LeCroy lower end scopes. So, so yeah, the layout is slightly different. I'll put in a comparison photo up here, but yeah,

**Dave Jones:** it has changed. And the metal standoffs here that are over on the bent metal chassis here, very nice. They're all identical to what we had before. So, anyway, there you go if you fan aficionados, but meh, whatever. You can

**Dave Jones:** see it is actually mounted on a standoff there to get it in line with the back of like a flush fit with the back of the case. That power supply is significantly different to the previous one. I won't

**Dave Jones:** take it out, but you know, it's probably going to do the business. Looks very nice. All the earthing points are exactly the same. Looks like it's really quite nicely implemented and course outside the case, which adds extra shielding, and they've got got some

**Dave Jones:** decoupling on here. But, as I said, there's no populated components on that, which looks like some sort of DC protection board, cuz it's in series with the thing here, or some sort of Don't even think it has like a MOSFET

**Dave Jones:** switching or anything. So, yeah. It's interesting. So, the power supply in the 2000X was done by Mean Well, which is a big name reputable manufacturer. This one is done by Mornsun. Yeah, they're a name as well. I I don't know. Leave it in the comments

**Dave Jones:** if you think Mean Well or Mornsun, who did it better. And the main DC filter cap is a Samzon with an X. So, yeah, whatever. Well, check it out. Yeah, they're cutting costs on this one compared to the 2000X. We've only got

**Dave Jones:** three heatsink devices here, whereas on the We got five on the 2000X. And the one up here, which was a, you know, I don't know, Arctic 7 or something, FPGA, it's a much smaller one now, and the heatsink's a lot smaller. So, that's

**Dave Jones:** interesting. I'll see if I can get the cans off. I'll take some high-res photos, always available on evblog.com, which links to my Flickr account. So, you can check out the high-res photos there, but let's go to the videotape,

**Dave Jones:** and see if we can compare these. But, of course, you expect a cost reduction here, because, well, it's a lower price scope. I don't know the exact, maybe I can put it up here in the edit. Like, you know, half the price of the 2000X or

**Dave Jones:** something, you know, rough order. So, yeah, they've saved some cost on the PCB. So, So, let's compare it to the 2000HD, shall we? So, this is the 1000HD here, and this is the 2000HD, which is only like a year old. I just did the

**Dave Jones:** teardown video like a year ago. So, it is radically different. You can see how the 2000HD has a bigger Sorry, you can't see it, but that's an Artix 7 FPGA. And then you got the two 12-bit analog-to-digital converters here. So,

**Dave Jones:** this is the acquisition ASIC. And then it looks like you've got that Lattice display FPGA there, or is it a I can't remember if it's a PLD or FPGA. Doesn't matter. Anyway, it's logic gates. And then you got the Xilinx Zynq, of course, which is

**Dave Jones:** used in practically every lower-cost scope these days cuz it's all-in-one. It's got the FPGA fabric, it's got the ARM processor or multiple multiple ARM processors in it. You know, so I can run the operating system and everything else

**Dave Jones:** and Bob's your uncle. And then the Spartan 7 FPGA, which I think I said has something to do with the logic analyzer down here last time. Something like that. You can see that Well, you can see where they've saved the cost. The ADC is

**Dave Jones:** exactly the same cuz you got to have it. You've got to have that 12-bit high-quality 12-bit ADC. So, it's the National Semiconductor jobby. It's the ADC 12D1000. It's exactly the same on both. You can see that there. And it's

**Dave Jones:** not like they've skimped like having just one to multiplex all four channels here. They've got one per two channels, exactly the same as on the 2000 HD. So, that's interesting. But up here, they've just got a Zynq UltraScale.

**Dave Jones:** That's a different one and it's in a different package and everything else to what we got up here, of course. So, the 2000 is an XC7Z020.

**Dave Jones:** And the 1000 is a XCZU2CG. Let's play along at home. You can go check, compare the specs on those. I'm not going to do it in this video, but obviously that's running the OS in the ARM core in there. And that's it. Bob's

**Dave Jones:** your uncle. We've got the Xilinx Zynq and there's the sample memory there. There might be some on the other side. I'm not going to get the board out to see on the other side. It's not that important, but like there's nothing

**Dave Jones:** else. So, this is obviously doing the logic analyzer as well. So, the logic analyzer is coming in via this ribbon cable here. The HDMI connector is actually on a front panel board down in there. So, yeah, that's a bit different. Whereas,

**Dave Jones:** over here, we actually had the logic analyzer and that was down on the main PCB down here and we had the big card edge connector poking Well, not right out the front, but a significant way. So, they had to put that HDMI connector

**Dave Jones:** down there so that it was a flush with the front panel. But, comes through that ribbon cable. So, that's obviously buggering off somewhere. Unless there's some extra processing magic on the bottom. But, I doubt it. And this ribbon cable here is the one

**Dave Jones:** that goes off to that back panel PCB that has all the external trigger and all that sort of jazz there. But, yeah, there's nothing else in here, obviously. You know, this is all power supply stuff. We've got more power

**Dave Jones:** supply stuff down here. Is that a PLL for driving the clock, I believe? Um, and not much else. Let's have a look at the front end. Now, if we compare the two front ends, this is interesting because this is the

**Dave Jones:** 1000HD up here and this is the 2000, which is the higher bandwidth 350 MHz jobby. So, you can see that the lower performance 200 MHz front end has four relays on here and two trimmer caps. So, someone's got to

**Dave Jones:** So, you know, it's a bit of how you do it um in terms of front ends these days. And the 350 MHz jobby, although I think they have a 500 MHz version in the 2000X series, but that's I think a different

**Dave Jones:** front end. I've only got the 350 MHz version, which we're looking at here. And both of them have a 50 ohm input path and there's another variable resistor here, which is not over here. This one does have more discrete SOT23

**Dave Jones:** down here. So, that's like, you know, a little bit extra, but like nothing to write home about, right? And a classic 748C595 here, of course. And you might think that the programmable chip has changed, but it hasn't. It's exactly the same.

**Dave Jones:** It's the net semi 6518 there. So, sorry, you can't see it here, but I've checked on different angles of the light where it shows up. It's exactly the same programmable gain amplifier front end here. So, yeah, that's interesting, isn't it?

**Dave Jones:** Look at the soldering on the 2000. They almost look like they've been they've been hand touched up, haven't they? So, something's doing there. But, yeah, there you go. So, there's a couple of manual trimmers, so it's not as an

**Dave Jones:** advanced, I guess, for want of a better term, as the 2000X, but it's lower bandwidth and I can have a couple of manual cheap tweaks, but obviously it's a little bit cheaper, but you know, yeah, probably the most expensive part in here is the

**Dave Jones:** programmable gain amp. The relays might be in Japan, of course. They haven't skimped there. But, it's kind of curious that they've just added an extra relay and the manual trimmers. I don't know why they just didn't reuse this 350 MHz front end

**Dave Jones:** in the 2000X that they well, the answer is obvious. They're saving money somewhere. I just don't really see it. Anyway, unless like some of these jobbies down here are super expensive, but like nice matched pairs or something, but

**Dave Jones:** uh, yeah. Anyway, interesting, huh? As you can see in the back of the case here that this vent system here, the grill is actually behind here. So, it's all exactly the same, all the same metal work, everything else, but that's what I

**Dave Jones:** expect. I would have been surprised if it was different. And well, it works. Um, only problem is uh I can't read Chinese. Oh, now this is interesting. Check this out. On the 2000 uh, XHD, in the maintenance menu here, I just noticed

**Dave Jones:** it's got a front-end tweak wizard option. Um, I don't know if I've ever seen that before. I don't know if I noticed that in the previous video. Anyway, the new 1000 uh, XHD does not have it. So, that's interesting. Now, of

**Dave Jones:** course, we have different front ends. Of course, this one has the uh, tweaks like the manual tweaks in it, uh, the pots that we uh, saw, and the and the trimmer caps that we saw, and this one didn't.

**Dave Jones:** So, maybe that's what it's doing. I don't know. Let's go in and have a look, shall we? Tweak wizard. Warning, Will Robinson. Authorized operator only. Yeah, I'm authorized. Connect a supported SDG to the oscilloscope through USB or use manual

**Dave Jones:** mode. Manual. Uh, click next if oscilloscope initialization completed. Uh, uh? Uh? Hope I don't ruin it. Um, connect AWG to C1 tweak uh, C1 to T1. Uh, yeah, no, this is getting nasty. Okay, I won't go there. Sorry.

**Dave Jones:** Well, this is interesting. This does auto memory management, right? You can't do fixed like you can the only option is fixed sample rate. Whereas over here, right? It's got fixed memory. So, you've no longer got um, that option on the

**Dave Jones:** 1000. You don't have fixed memory. So, yeah, that's really annoying. There's like we can uh, and it times out, too. We can change that time out thing here if you want. So, we can actually uh, tweak that if we go into acquire. You've

**Dave Jones:** got to hit menu, which is kind of annoying. Um, and then we can go into the fixed sample rate and 2 gig samples per second gives us 20 meg points. So, we're going to uh, drop that sample rate

**Dave Jones:** there. Oh, and uh, 1 meg point. There you go. We can go to 2.5. So, that's nearest to the uh, two that we have over here with 1 millisecond per division. But, if you know why this does not allow you to fix the

**Dave Jones:** memory size, um please leave it in the comments cuz I don't know from an architecture point of view why you would need to do that. The only thing I can think of is that they're making it easier for the user cuz the Keysight

**Dave Jones:** works like this. It's, you know, setting its automatic memory depth or bust, and yeah, so maybe they're just taking that option away cuz it's just an extra thing that confuses users, but I don't know. I'd like to know Well, you do know what

**Dave Jones:** your memory depth is set at. It's it's there clearly, but still I don't know. Leave it in the comments if you think that sucks. Okay, so on the 2000X we've got peak to peak 536 microvolts there. I've set it to 200 MHz bandwidth, so it

**Dave Jones:** matches the other one cuz this is a 350 MHz bandwidth scope, and there you go. Yep, it does have the It does have the microphonics on the input. Of course it does. There There you go. Does the 1000X HAVE THAT?

**Dave Jones:** OH. OH, HELLO. HANG ON. WOW, IT'S FIXED. OH, LOOK AT THAT, BILLY. WOW, that's a great improvement. Is that the best scope on the market? I'm really thumping that. Wow, that's incredible. It's I mean I saw a little bit of

**Dave Jones:** something over there, but and even single shot trigger, which is just above there. No, look at that. Oh, yeah, just got it, but jeez, I really thump. There's a lot of force in that, trust me. That could be one of the best scopes ON

**Dave Jones:** THE MARKET. WOW, TERRIFIC. SO, they've either decoupled the physical connection in there, but I can't see why. I think that BNC is going to go directly into the front end board. Yes, in fact, you you see it soldered in the teardown

**Dave Jones:** thing. So, it's directly coupled into there. So, they're just using non-microphonic capacitors in there. Fantastic. I hope that was deliberate, and it's not just like a random bill of materials thing. I hope that's consistent. Leave it in the comments

**Dave Jones:** down below if you've got one of these puppies and you can test this. So, 65 microvolts standard deviation, let's go over here. It is lower 456 microvolts as opposed to 630 and 45 as opposed to 62. So, there you go. Um that is more

**Dave Jones:** betterer, but you can see that I think the 2000X is updating faster, but if you look at the spec sheet, the 1000X actually has 120,000 waveform updates per second as opposed to 100,000 waveform updates per second. So, technically it's faster, but that

**Dave Jones:** actually looks slower to me. And by the way, I've got them both on 1 megaohm input cuz that's my standard test, but it makes no difference if I will get the similar or same ratio when I put it on

**Dave Jones:** 50 ohms. There you go, 50 ohms 45 microvolts standard deviation 57 microvolts standard deviation. Of course, YOU KIND OF expect that because not only A is it a different front end, but this has a 350 MHz front end, which

**Dave Jones:** you don't get a free lunch. Even though you set the software bandwidth limit to 200 meg on here, you still get a noisier front end when it's baked into your physical design. The higher the bandwidth front end, even if you're

**Dave Jones:** software limited, it's still going to give you a higher noise floor. It just is. All other things being equal, of course. So, totally expect that, but yeah, that's a significant difference. Oh, I just noticed that my trigger level

**Dave Jones:** was down in the noise here. It's now above, just like it is on this one, and still I think this is faster. I mean, that's visibly faster. I don't even have to measure the trigger output to see that's faster. Does everyone agree?

**Dave Jones:** Anyway, sorry, I've got to head home. I'm actually sick at the moment. Maybe you've heard it in my voice and I can't concentrate at all. So, I'm going to keep this video short. Let me know if you want to do a full review or if you

**Dave Jones:** wanted me to test specific things. I can do do that quickly and whack it up on the second channel. But yeah, I'm sure this is a winner. Siglent maker, great scopes. The bang for buck is probably one of the best on the market.

**Dave Jones:** Shame it doesn't have a HDMI output. That would have been really nice. I mean, even the $299 Rigol has the HDMI output now. So, uh I don't know. And of course, it's you know, it's pretty thick. If you're after

**Dave Jones:** a slimline scope, then you're not going to get that. And even the new 800 series, that's thick as as well. So, yeah, it's nothing like the Rigol DHO 800. So, yeah, and no HDMI output on it either. So,

**Dave Jones:** but of course, they do have a really nice web interface on this. So, you can actually capture the screen that way. Ethernet LAN is built in. So, yeah, no worries. You can do it that way. Just HDMI external monitor is just or

**Dave Jones:** external HDMI capture is just a really nice. And I thought we'd get that with all scopes now, but no. Anyway, if you like that video, please give it a big thumbs up. As always, discuss down below. Catch you next time.
