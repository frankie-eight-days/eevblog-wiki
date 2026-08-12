---
video_id: P8MpZGjwgR0
title: EEVblog #1081 - Are Bypass Capacitors REALLY needed? (Muntzing)
url: https://www.youtube.com/watch?v=P8MpZGjwgR0
source: youtube-asr
timestamps: {"0": 1, "1": 14, "2": 29, "3": 43, "4": 60, "5": 76, "6": 95, "7": 108, "8": 124, "9": 136, "10": 155, "11": 171, "12": 185, "13": 200, "14": 216, "15": 231, "16": 243, "17": 257, "18": 266, "19": 282, "20": 293, "21": 320, "22": 343, "23": 360, "24": 375, "25": 394, "26": 408, "27": 425, "28": 438, "29": 451, "30": 465, "31": 478, "32": 492, "33": 509, "34": 522, "35": 542, "36": 562, "37": 576, "38": 590, "39": 606, "40": 626, "41": 645, "42": 660, "43": 677, "44": 693, "45": 709, "46": 722, "47": 735, "48": 747, "49": 761, "50": 778, "51": 792, "52": 806, "53": 824, "54": 837, "55": 851, "56": 864, "57": 880, "58": 896, "59": 910, "60": 924, "61": 938, "62": 955, "63": 973, "64": 986, "65": 1002, "66": 1018, "67": 1032, "68": 1048, "69": 1063, "70": 1074, "71": 1092, "72": 1107, "73": 1126, "74": 1142, "75": 1157, "76": 1170, "77": 1189, "78": 1203, "79": 1218, "80": 1232, "81": 1247, "82": 1262, "83": 1274, "84": 1286, "85": 1299, "86": 1314, "87": 1331, "88": 1349, "89": 1363, "90": 1378, "91": 1394, "92": 1409, "93": 1425, "94": 1443, "95": 1464, "96": 1483, "97": 1495, "98": 1512, "99": 1525, "100": 1538, "101": 1552, "102": 1565, "103": 1580, "104": 1596, "105": 1609, "106": 1624, "107": 1639, "108": 1651, "109": 1665, "110": 1681, "111": 1696, "112": 1711, "113": 1726, "114": 1740, "115": 1753, "116": 1765, "117": 1782, "118": 1796, "119": 1812, "120": 1833, "121": 1847, "122": 1865, "123": 1877, "124": 1892, "125": 1906, "126": 1918, "127": 1931, "128": 1948, "129": 1965, "130": 1977, "131": 1993, "132": 2009, "133": 2024, "134": 2035, "135": 2049, "136": 2063, "137": 2075}
---

**Dave Jones:** Hi, in a previous video, which I'll link in at the end of this and down below, number 859 for those playing along at home, a very popular one on bypass capacitors and why you need them and how they work and all that sort of stuff.

**Dave Jones:** But I've always wanted to do a video doing some monthsing. What is monthsing? Well, let's actually have a look. Made a quick look. Madman Months was a used like a car salesman back in the day and he sold TV sets and

**Dave Jones:** things like that and I'll link all these in down below. There's an old Bob Pease article. What's all this monthsing stuff? Anyhow, and he talks about how Madman Months was famous for carrying around a pair of side cutters like this

**Dave Jones:** and whenever the engineers you know, designing the TV sets would show him the TV like they're proud of their creation, he'd go in there, start snipping out components, probably capacitors, resistors, whatever, start snipping them out and if the TV set still worked, then

**Dave Jones:** that component went. Once the TV set stopped working, put that last component back in, ship it. Well, that's the story anyway. How true it actually is, I don't know, but anyway, monthsing is the term for snipping out or removing components

**Dave Jones:** until your product works and then shipping it cuz obviously those components weren't needed. In particular, bypass capacitors. And it got me thinking can a product work with absolutely no bypass capacitors? Well, the obvious engineering answer to that is maybe or

**Dave Jones:** no, depending on the circumstances. So, I thought it'd just be an interesting and fun experiment to actually take a product, remove all the bypass or snip them out one by one and see where it stops working, if it does stop working

**Dave Jones:** at all. Let's go. So, I thought we'd have a try with this Gigatron TTL microcomputer cuz this is a classic double-sided PCB layout. You can see all the traces running vertically like this on the top mostly anyway, and

**Dave Jones:** you can see them all running horizontally on the bottom with you know, just some sprinkling of ground fills. There's you know, a couple of stitching points in the ground layer and stuff like that. So I'm not sure. I

**Dave Jones:** don't have the PCB folder hand to have a look at that. But anyway, and it runs all 5 volts. So higher voltage excursion rails than your typical 3.3 volt one. Once it's 6.25 megahertz, so it's not particularly quick. But if we can get something like

**Dave Jones:** this to fail, then that'll be really interesting. And you note that it it has lots of bypass caps on here. Practically, I think there is one for every chip actually. So in you know, traditional time honored engineering practice, they've put a they've just

**Dave Jones:** specified in the design a bypass capacitor for each and every chip. Whether or not they're actually required in terms of the layout and the impedance of the traces and and the loop paths and all sorts of things. It doesn't matter.

**Dave Jones:** They you know, a typical double-sided 5 volt TTL digital board. And of course, the other good thing about this is that it has a ready output for us to see if it's failing or not. So we can just get

**Dave Jones:** it to do stuff. Like if the computer if the VGA output starts to wobble or or do something weird or you know, anything like that, we should be able to actually see failures pretty readily at the system level. So first of all, we'll

**Dave Jones:** start by actually just probing some key signals around here. Obviously, we can't probe everything. It's all too hard. There's just too many signals to probe. We won't know a specifically what point actually failed. We might be able to

**Dave Jones:** analyze it later if we can actually get it to fail, but let's measure some points just so that we have a baseline. And of course, using proper signal integrity techniques to measure them, and then start removing some caps. See

**Dave Jones:** what happens. Now, at this point, it's actually very important to get your grounding correct. And I actually shot more than 10 minutes of waffle talking about the correct ground probing technique and different probes and and things to use and how to set up

**Dave Jones:** your scope. So, I decided to rather than do that now, I left it to the end of the video. So, jump to about just over the 19-minute mark or 19 and 1/2 minutes, and you'll be able to see that right at

**Dave Jones:** the end. Right. So, now it's Mad Men months in time. I'm going to get my side cutters, I'm going to go in there and hopefully not short anything out. Be careful. And I'm going to trim off bypass caps and see if anything changes.

**Dave Jones:** And I've got my Mandelbrot running in the background, so I'll be able to see if anything changes. So, here we go. I don't know. I'll go over to the condition decoder. You see that? Yep, and I'll just trim

**Dave Jones:** off some caps. So, here we go. Here we go. It's one. Two. Three. Everything's still working. Our Mandelbrot still going. This is our instruction register. Kind of important. Nothing's changing yet. It's all looking pretty jazzy, but I wouldn't expect it

**Dave Jones:** to be a big deal. Well, yep, shorted it. Oops. Let me run that Mandelbrot again. Another one goneski. So, that's all around the instruction register, data register, bus buffer, bus access decoder, and the condition decoder. They're all without decoupling in that

**Dave Jones:** section. Address mode decoder, goneski. Yes. Look at this. Mad Men months uh technique is is working. Instruction decoder. Let's do the instruction decoder down here. We don't need to do any It's still working. Of course, you know, like

**Dave Jones:** we don't necessarily expect these to change. You would You would definitely see the signal integrity change if we were actually probing directly on these chips here. So, what I'll do now is I'll actually do the one on this or go like right in

**Dave Jones:** the nearest point down here to the signal. But, of course, it's not coming out of that chip. So, it's probably not going to do much if anything. Not. There we go. Because the signal integrity has to do with the loop area

**Dave Jones:** of the ground and the signal. So, the clock signal's coming from I don't know up here. It's coming from wherever and it's it's all forms what the signal integrity is all part of a big effectively a loop in here. What's

**Dave Jones:** called loop area. And that's the most important thing for generating and reducing electromagnetic interference. For example, if you've got If your clock's over here and your load's over here on your board and the current has to run right across the

**Dave Jones:** board and all the way back and you're really got very high frequency edges in there, then that loop area is what's going to generate huge electromagnetic interference. It's going to act as a huge antenna. So, you know, this thing

**Dave Jones:** would not If you had a design like that, it wouldn't pass like EMI EMC compliance and things like that. It'd just be spewing out radiating crap out there. You can alleviate that with ground planes and other things. This

**Dave Jones:** thing doesn't have a solid ground plane. It's just got like split ground planes with, you know, lots of hickelty-pickelty paths in there to do with wherever they could drop the uh vias down on the board. Anyway, still working.

**Dave Jones:** Let's go. Another one gone. Another one gone. Oh! That was me. I'm just actually got this uh load by here cuz you can at least see something going across there. I've snipped a few more now. I forgot to

**Dave Jones:** press uh record there. Go on, Ski. Tell you what. Mad Man Monster's right. Saved a few cents on our design already.

**Dave Jones:** Okay, I've now removed all the capacitors bypass caps from this side of the board uh where the um instruction register, the RAM, the ROM, everything is. And it's no problem whatsoever. I should have actually measured a few more signals around here. So, the clocks

**Dave Jones:** actually weren't really a good idea. And really, you know, you should see the LEDs up there stop uh chasing, too. The program stops.

**Dave Jones:** I have snipped the leads on every I Oh, no. No, one right near the SRAM. Right near the SRAM. There we go. I snipped every single bypass cap on that board except for the main filter cap on the input.

**Dave Jones:** This board this computer runs fine with absolutely no bypass caps. I'm not that surprised. If we turn on our reference waveforms there, you can see that uh there's a you know, little bit difference in there. Geez, we're we're really talking

**Dave Jones:** very minor differences. But But hey, you can see them, right? Nothing on the blue waveform. That looks absolutely identical. But the uh clock one, which is uh down in the middle of the board um down near the OR gates down there. Yeah,

**Dave Jones:** there's a little bit of change, but hardly maybe a little smidge up there, but basically nothing. It's identical. All the bypass caps are gone. So, if we actually zoom in on that waveform, where it's 2 nanoseconds per division, you can

**Dave Jones:** see that's probably like 2 and 1/2, maybe 3 nanoseconds rise time or something like that. So, you know, it's it's a pretty sharp edge for a TTL signal. Okay, what I've done now is actually taken out the the big bulk electrolytic

**Dave Jones:** cap there on the USB input. So, there are literally, unless I've missed one, not a single bypass capacitor on this entire board, either the bulk input capacitance or the ceramic 100 in bypasses on there. And that's what we get.

**Dave Jones:** That It basically has deviated very little. Oh, our blue one is now Our blue one has now changed a little bit from our reference point. Look at that. But, apart from that, like like there's practically no difference whatsoever on those clock signals. And

**Dave Jones:** quite frankly, I wouldn't expect difference much else. And the computer still works fine. Not one bypass cap. Like, I'm not kidding. They've all been lifted. Every single one of them. Like I said, that one is not a bypass cap. That's

**Dave Jones:** like a 47 puff. There, your crystal ones there. But, everything else, they've all been lifted. Every single one of these caps on every single one of these chips, and things still works just fine. Now, of course, some people might jump in and

**Dave Jones:** say, "Oh, LOOK, IT'S THE GROUND PLANE. This thing's got a ground plane. So, in combination with the power traces on there, it forms a capacitor." And when you've got big ground planes like internal layers, like a four-layer board, if we had a giant ground plane in

**Dave Jones:** the middle, and then the capacitive plane next to it, then yes, that is a thing. You can actually get away bulk distributed capacitance. In fact, you could write a PhD thesis on this. Um actually analyzing uh bulk capacitive ground planes versus

**Dave Jones:** individual caps. And there's, you know, a lot of uh uh science that actually goes behind that. And there's a lot of theory that says um and in and practical demonstrations that can show bulk distributed capacitance can be better

**Dave Jones:** than individual bypass caps like this. So, in theory, if you're doing a real high-frequency design, you want uh to put your ground planes. That's why you stack up in your PCB. When you actually stack them up, you don't want the ground

**Dave Jones:** plane down here and the uh positive plane up the top with your signal traces in the middle, um cuz not only is that a pain in the ass, you can't access your signal traces on the outside, but then

**Dave Jones:** that just screws up the capacitance between the layers. You're better off sandwiching them right together as close together as possible on the internal prepreg, uh what's called when they make up the multi-layer PCB. And then you get the distributed capacitor effect, cuz

**Dave Jones:** remember, a capacitor is just uh two plates separated by an insulator, and that's exactly what a PCB is. Two big planes, uh ground and power, for example, in this case 5 V, separated by um the FR4 dielectric material in there. So, it's

**Dave Jones:** one big bulk capacitance. But anyway, that doesn't really apply in this case because uh we don't have any full ground planes or full power planes or anything like that. So, the power uh traces are just going willy-nilly. So, there might

**Dave Jones:** be a little tiny bit, I don't know, you know, half a bee's dick, a poofteenth of uh capacitance in there, but yeah, it's nothing. So, it's not that. This thing simply works fine without bypass caps. But I've worked on uh systems before

**Dave Jones:** with bypassing uh problems in them and just the act of probing, just the act of the capacitance of your probe is enough to cause your circuit to suddenly start working or failing depending on where Murphy is on that particular day. The capacitance

**Dave Jones:** of your probe affects the signal under test and it could you know, once again as I said, if this ringing goes low enough to affect the threshold then your gate could switch and then your system could be completely screwed and your

**Dave Jones:** capacitance can have a positive or negative effect on that. Okay, now let's actually just randomly probe some other signals on here. I've just gotten one of the pins of the I don't know whether it's the data address of the ROM chip

**Dave Jones:** and you can see of course there's data switching in there. We're referencing it to the clock here. We could actually reference it to channel two, but you can basically see what in the trade is known as an eye diagram

**Dave Jones:** in here. It's actually still pretty good. Like there's nothing really dipping down hugely low. This is with absolutely no bypassing at all. It's it's really quite nice. That's why the computer is still working. But although the computer is working,

**Dave Jones:** herein lies some of the problem. Now I've just probed pin five of U29 here which is part of the X register. I don't know what it's doing, but it it we just single shot captured this and it's interesting look at this. Look, we have

**Dave Jones:** like this little runt pulse going up here and that's obviously caused by you know, grounding type issues somewhere else in the system and then we've got this little glitch over here and things like that. So you know, the

**Dave Jones:** computer's working but you could really come a gutser on these especially if you're you know, your power supply is varying and something like that cuz once that passes the signal threshold well the like the uh TTL thresholds, um

**Dave Jones:** either positive VOL or VOH, then it can um change the level of your chip, or it can uh if we're talking about a flip-flop or something, it can get into a metastable state. I think I've done a video on metastability and things like

**Dave Jones:** that, and it can really ruin your day. So, that's, you know, a pretty horrible-looking waveform there. So, what I've done is actually uh resoldered the bypass caps around that particular chip, um and the source of it over here, and I've put those ones

**Dave Jones:** back. Let's see if it makes a difference. We're still going to see ugliness, but maybe some of the little glitchiness might uh go away. Okay, so here we go. Here's single-shot capturing some stuff. So, that looks that looks better than before.

**Dave Jones:** Of course, you know, we've still got, you know, stuff happening out here, wiggle wiggle wiggle wiggle, yeah, over here, uh caused by uh you know, uh ground bouncing um elsewhere, like in other parts of the circuit is switching

**Dave Jones:** over here. Actually, that one's going right down like that. That That's a legit I think that's a legitimate thing, like a legitimate 10 ns pulse happening there. So, yeah, but, you know, we've still got some other issues, but obviously, it's

**Dave Jones:** uh maybe it's a bit better. Mhm. Now, check this out. This is a rather interesting experiment in terms of uh like grounding layout and loop area and uh switching, how the, you know, the grounds relate to the various switching

**Dave Jones:** elements and going across uh ground uh domains, and I won't go into all the details, but there's lots of um this is where ground planes really come into play, which this one doesn't have, and I'll show you some uh variation on this.

**Dave Jones:** Now, I'll go to this output register up here, which happens to be very fairly clean. And you'll see what I mean by that in a second. Okay? Look at this. Check out the ground signal the ground there. Okay? There's very little in the way of

**Dave Jones:** like, you know, there's your regular noise down there, but there's no periodic switching noise as you'll see in a second. So note that as we say go over to this chip over here. I know you know, I'm just like probing random uh

**Dave Jones:** pins, right? But look at that. Look at the amount of switching noise on there. And no, this is not due to the bypass caps. I've actually soldered most of the caps back on this port. I think I'm only

**Dave Jones:** missing one or two. Okay, so let's go over to this chip over here. Just random probing. Look at that. Look at all that switching crap in there. You can see it. Isn't it horrible? And that is basically just due to the layout and signals

**Dave Jones:** crossing ground paths and doing all sorts of stuff. So this is like the high frequency That'll be the high frequency clock in there doing that. Okay, bonus. Let's go down to a chip over here for example, and you get the same sort of

**Dave Jones:** thing. Check this out. This one here fairly clean. That's part of that accumulator. Look at that. Interesting, huh? It's all to do with the layout. There's another one right next to it there. I don't know. Let's go down to this instruction decoder down

**Dave Jones:** here. What's that going to do? Oh, there's nothing on there. There we go. It's clean at that point. Starts to switch at that point. So that's interesting in that maybe one of the signals that's crossing one of the grounds going to this

**Dave Jones:** particular chip or part of the ground loop in there is not switching at this time, but then it suddenly started to turn on at that point, that point, that point, and so on. So, no amount of bypassing is going to fix that problem.

**Dave Jones:** That's a fundamental problem with like a double sided board like this where you can't do a nice solid low impedance low inductance ground plane over the whole thing. If you stitched all these pins together, and did this on a four-layer

**Dave Jones:** board, you wouldn't be getting stuff or you know, it's it's much more minimized this sort of switching effect. I mean, you know, have a look at the size of those excursions. And yes, I've put the bypass caps back.

**Dave Jones:** Okay, the first thing we're going to do when we're actually probing something like this, we care about signal integrity. And signal integrity has to do with the types of probe you use and the probing technique you use. So, the

**Dave Jones:** first thing you want to do above everything else is get rid of this antenna ground lead cuz that is an inductor. Any piece of wire of any length is an inductor. You want to get rid of it. So, that's going to cause

**Dave Jones:** ringing on your waveform. You're not going to be able to measure the true waveform in your circuit by using one of these. You're just not unless it's a sine wave, then you're okay. But when we're not, we're measuring TTL digital

**Dave Jones:** signals here. Not very fast, 6 MHz, but it doesn't matter if it's a 1 Hz signal, it doesn't matter. It's the transition where the waveform goes right up like that. That contains high frequency content where your ground lead

**Dave Jones:** is going to come a gutser on you. So, what you want is this little puppy that came with your probe. Should have. Hopefully you didn't toss it out. And you put it around there, and now you've got a nice low

**Dave Jones:** inductance ground path like that. And then we can go around and probe our circuit. Yes, it's not very convenient cuz you can only reach that sort of distance, but if you want to probe things properly, that's what you have to

**Dave Jones:** do. And it just so happens that we have a couple of test points on here for the main clock. So, we'll just do the main clock. So, we have a ground point here and one of the clocks here.

**Dave Jones:** In this case, it's the system clock. So, we can just whack that in there like that. Our ground plane and hook that on there. So, we now have a beautifully low impedance um the test point there to measure our

**Dave Jones:** clock signal with. So, that's how we measure signal fidelity properly. That will do proper high-frequency probing techniques is basically what we're doing. Now, the next thing we want is the choice of probe that we're using. In this case,

**Dave Jones:** we're using a passive probe, but I'm using the absolute best passive probes I've got here in the lab. These are 1 gig bandwidth Tektronix TPP 1000 for those playing along at home. Fantastic. 1 gig bandwidth analog passive probes. I

**Dave Jones:** don't know how they do it. It's absolutely black magic technology. It really is. And you want low capacitive probes. 3.9 puff 10 meg fixed times 10 probes. And these particular probes are matched for the system, right? So, these have got like

**Dave Jones:** the probe interface. There's like a one wire chip in there that identifies the probe. And you'll notice that there's no compensation adjustments on either on the end that plugs in the scope or on here. There's no traditional trimmer

**Dave Jones:** caps on here cuz these probes, what you do is you hook them up to the calibration port on here, and then you run the auto calibration routine. It identifies these probes. It knows the serial number, and it actually stores it

**Dave Jones:** inside the scope here. So, if we actually go over here, oh by the way, I'm using the Tektronix MDO 3000 here because this is the highest bandwidth scope I've got in the lab, 1 GHz bandwidth, and it has the matching best

**Dave Jones:** probes I have here in the lab. So, we can actually go into probe setup down here, and you can see that it's all right I've I've actually compensated these probes already, and it stores them. So, even if I swap this probe over

**Dave Jones:** to this channel, the compensation follows because it's smart enough it knows that's the serial number, and then it follows. It's absolutely brilliant. So, this is the best probing solution we could possibly have for measuring true signal fidelity of the clocks in this

**Dave Jones:** system as we remove those caps. Now, technically speaking, I do actually have better probes here in the lab. I have active FET probes, and if you really want to get serious, you'd be using an active FET probe. This is a Cal Test CT4121.

**Dave Jones:** It's a 1.2 gig bandwidth 10:1. It's 1 meg in parallel with 3 puff, 3 picofarad. So, that one's better than the 3.9 of the Tektronix there. And of course, it comes with all these different little probing attachments that allow you to probe

**Dave Jones:** things with, you know, real low impedance and everything else. Sometimes you got to even uh roll your own. Well, I do have one slightly better. I've got this Agilent N2796A active probe, and it's only 1 picofarad input, 1 puff input capacitance. Do you

**Dave Jones:** believe it? Absolutely crazy. Similar sort of thing, and it's even Look, it looks like I don't know. It looks like a prawn or something. Um and it's got little lights on there and everything. Anyway, these are, you know, real If you

**Dave Jones:** really want to probe uh signal fidelity and high frequency stuff properly, then active fit probes are the way to go. But in this case, for our 6.25 meg fundamental frequency, the harmonics are going to be much more. We're just going to use our these one

**Dave Jones:** gig passive probes are more than enough. We can do it with, you know, we can do it on our Rigol, 200 meg Rigol scope as well. But you know, I'm just using the best scope and the best in terms of bandwidth and the

**Dave Jones:** best passive probing system I've got in the lab here. And we've got another clock signal up here which we can measure as well. This one's a little bit trickier. Sort of like hold that in place. It's a little bit how you doing?

**Dave Jones:** But we can do it. No worries. All right, so we've got our live signals here. Now setting up your scope is for a proper signal fidelity measurement is just as important here. And you can see that well, we can actually turn on our

**Dave Jones:** frequencies. You can see that both channel one and channel two, both two volts per division. So the yellow waveform here is clock one down towards the bottom of the board and the blue waveform is clock two up the top of the

**Dave Jones:** board. They're and they're both 6.25 megahertz. But you can see that there's some skew actually between them. That's inherent in the board cuz yes, I have de-skewed these probes. So if we go in here and look at our probe setup here,

**Dave Jones:** we can actually de-skew them. You can actually set up a propagation delay 5.3 nanoseconds in this case per probe and I've automatically this has automatic de-skew and all that sort of jazz. So if one probe was longer than the other, you

**Dave Jones:** might be like you might have to change the skew on these things. Or you can actually compensate for the skew on your board as well, not necessarily in your probe. But we don't want to do that. Okay? So we're happy, but we're not

**Dave Jones:** actually interested in the timing of the waveforms. We're just interesting in what the waveform looks like. There is our waveform. Now, here's the thing, right? We can actually go into acquire here. I'm actually in average mode at the moment. So, I've actually got I'm

**Dave Jones:** displaying I've I've got a record length of 100k, fast acquisition mode is off, and average and I'm doing 16 averages here. Of course, if we go into sample mode, that's the crap that you get because the waveforms are always, you

**Dave Jones:** know, changing. There's always noise and and whatnot crap on there. So, if you turn on our fast acquisition, for example, that will that will give us that in really that's updating, you know, 100,000 or a million waveforms per

**Dave Jones:** second or whatever this scope is capable of doing. But, it's only got like 250 samples or something. So, let's go down to our record length and you can see here how the record length can change some things. Just notice how it's

**Dave Jones:** slowing down. All that crap is still there. Look at that. The the channel one down the bottom of the board is the worst here. And all that crap is coming from other switching elements inside your computer here. So, actually,

**Dave Jones:** let's see if I can I get it to change. Let's turn on the Mandelbrot. As your program does things, you might see differences here. So, let's have a look at this. I'll I'll press start and reset it. Boom, we're back at the menu.

**Dave Jones:** Maybe I don't know, not as much variation. But, in in theory, right? That is possible. If we do something in our circuit, we could see variations in our signal fidelity because of all, you know, the non-optimized ground layout and stuff

**Dave Jones:** that we've got on this board. But, yeah, you can see the record length of how it's slowing down. But, really, you know, I'm happy to get an average. If you're looking at signal integrity, you don't want the other crap in there to affect it really.

**Dave Jones:** It depends on what you're after though. Sometimes you may want to see how other parts of your circuit in this particular case, if we're chopping off some of the capacitors on the other side of the board, for example, that might upset the

**Dave Jones:** clock at this particular part of the circuit so that we're actually probing. You know, so you may or may not want to see that. But of course, if you want the signal integrity at that point, the best way to do it is to simply

**Dave Jones:** Well, you can turn on high-res mode which does a boxcar averaging of like you know, like 16 or something like that in a row at the sample thing. But the best way to do it is just with a nice

**Dave Jones:** average like that. There you go. We've got our two waveforms. Now we can actually store those as reference waveforms. Okay, so I'm just going to choose 100k there as end 16 averages there as our reference. So we'll just stop that and now we've got

**Dave Jones:** our nice two reference waveforms with all our capacitors in place. So now we can actually go in and store these. We can go into menu here, source one destination reference waveform one. By the way, the scope's a bit weird. If you

**Dave Jones:** want to actually store your references, you don't press your reference button. You actually have to go into save recall down here. Maybe it's intuitive, maybe not. Anyway, there we go. So we save that and then we can save our source.

**Dave Jones:** Save channel two and save like that. And now we have our probably saw the white reference waveforms here. So now we can turn our reference waveforms off and on. So now we can actually see if our waveform changes. There you go. It's

**Dave Jones:** doing that because of the reference, but the reference is still there and so we've always got that reference wave waveform to compare to. But there we go. So, if we see any changes, we can just use the reference to highlight the Oh,

**Dave Jones:** by the way, yes, these are actually like real little things happening in the circuit because we're using proper high-fidelity high-frequency probing techniques here. This stuff's actually happening. There's some sort of transition thing that's causing a ground like a little bounce, you know, in the

**Dave Jones:** ground system or whatever. This edge here is pretty good on the top of the clock, but look at the, you know, look at the ringing on that. It's pretty terrible, right? And then undershoot on there, right? But this is

**Dave Jones:** actually what's happening in our circuit. This is real stuff because we're probing it properly. We know there's very little effect, you know, negligible half a bee's dick to do with our probes. So, we're we're doing the absolute best we can. So, that's

**Dave Jones:** actually what's happening in the circuit anyway. So, there you go. I hope you enjoyed that video and look at Munson. Was Mad Men Munson right that you can remove capacitors and your product still works? Well, yeah, obviously yes. In this

**Dave Jones:** particular case, we removed them all and it still works. And I still you would have to try this over like the voltage limit range like say the 5-V plus minus 5% over temperature and all sorts of other qualification

**Dave Jones:** type things if you were going to ship a product with no bypass capacitors, which I do not recommend by the way. So, do not take this video as a recommendation that you don't need bypass capacitors cuz you do. In fact, they can be

**Dave Jones:** absolutely critical. And but don't go overboard with bypass capacitors because it's a whole science and you don't want the things to resonate. Anyway, I've got that whole video looking at bypass capacitors and that really only scratches the surface. Like I'll link in

**Dave Jones:** some like papers down here. Here's like a IBM paper on decoupling caps and and ground planes and and capacitor impedance and you can go to town. Look at that Look at the mappings they've got. It's just absolutely insane. You can do like PhD

**Dave Jones:** theses on just on bypassing. I mean, it's absolutely crazy, you know, and and lower your inductance from your pad to your via to drop down to the ground plane. It can make a hell of a difference in there. And there's tons of

**Dave Jones:** stuff and you know, TI and almost every manufacturer has discussions about bypassing because it is actually critical. You know, if you go into our FPGAs, for example, they they've got like how many pages is this document? I don't know. This is

**Dave Jones:** just a document on power supply designing power supplies and bypassing your FPGA and power delivery systems just for Xilinx FPGAs and and stuff like that. Like it goes into the same stuff I've done in the video and then shows

**Dave Jones:** you and then tells you how long your traces can be to your vias and you know, all sorts of stuff. It's just placement around the under the chip and all sorts of stuff. I've done probably previous videos on that and they go to town and

**Dave Jones:** they go to town for a reason because bypassing is important. So, this was just a bit of fun to see if monthsin worked and it kind of did in this case. Be nice to get and I might do it in

**Dave Jones:** future videos, get more advanced products and actually remove probably can't snip out little I don't recommend snipping out little surface mount ceramic caps they will shatter and then take your pads off your board, ruin your day. Anyway, it'd be nice to you know,

**Dave Jones:** get a more high-tech product perhaps and do some monthsin. Anyway, I also may there'll be a an excellent I'm hoping spin-off video to this one as well in the future. So, maybe look out for that. Anyway, if you liked it,

**Dave Jones:** please give it a big thumbs up because that always helps a lot. Subscribe and all that sort of stuff. You got to get that notification bell. Where Where it? I don't know. Down here, somewhere, up there. Down there.

**Dave Jones:** Whatever. You know. All YouTubers say the same crap. Catch you next time.
