---
video_id: 66s9easZKxU
title: EEVBlog #1103 - Omicron Labs Bode 100 Review & Experiments
url: https://www.youtube.com/watch?v=66s9easZKxU
source: youtube-asr
timestamps: {"0": 1, "1": 22, "2": 58, "3": 93, "4": 126, "5": 141, "6": 173, "7": 205, "8": 238, "9": 265, "10": 297, "11": 314, "12": 330, "13": 364, "14": 382, "15": 413, "16": 431, "17": 461, "18": 498, "19": 529, "20": 565, "21": 589, "22": 622, "23": 647, "24": 666, "25": 701, "26": 730, "27": 751, "28": 782, "29": 815, "30": 851, "31": 881, "32": 912, "33": 931, "34": 961, "35": 988, "36": 1000, "37": 1025, "38": 1051, "39": 1073, "40": 1097, "41": 1113, "42": 1126, "43": 1158, "44": 1171, "45": 1198, "46": 1228, "47": 1247, "48": 1261, "49": 1284, "50": 1308, "51": 1331, "52": 1355, "53": 1388, "54": 1420, "55": 1443, "56": 1472, "57": 1503, "58": 1532, "59": 1560, "60": 1574, "61": 1593, "62": 1624, "63": 1647, "64": 1673, "65": 1703, "66": 1725, "67": 1759, "68": 1789, "69": 1813, "70": 1838, "71": 1864, "72": 1895, "73": 1930, "74": 1953, "75": 1983, "76": 1998, "77": 2015, "78": 2040, "79": 2058, "80": 2083, "81": 2099, "82": 2120, "83": 2154, "84": 2174, "85": 2197, "86": 2215, "87": 2248, "88": 2264, "89": 2284, "90": 2315, "91": 2328, "92": 2353, "93": 2384, "94": 2405, "95": 2419, "96": 2441, "97": 2471, "98": 2490, "99": 2507, "100": 2529, "101": 2561, "102": 2576, "103": 2606, "104": 2637, "105": 2664, "106": 2687, "107": 2703, "108": 2720, "109": 2731, "110": 2758, "111": 2774, "112": 2798, "113": 2838, "114": 2866, "115": 2885, "116": 2900, "117": 2936, "118": 2967, "119": 2997, "120": 3023, "121": 3055, "122": 3082, "123": 3111, "124": 3137, "125": 3161, "126": 3179, "127": 3203, "128": 3219, "129": 3244, "130": 3275, "131": 3305, "132": 3332, "133": 3362, "134": 3382, "135": 3403, "136": 3433, "137": 3448, "138": 3479, "139": 3492, "140": 3518, "141": 3532, "142": 3549, "143": 3584}
---

**Dave Jones:** Hi, I'm super excited about this one. Thank you very much to Omicron Lab for sending in this baby in this very sexy case, which I believe is optional extra, but let's check it out. Let's check out the Bode 100. We'll have a look at all the stuff, but oh, hang on.

**Dave Jones:** Oh, I just smell versatility. Look at this. We've got the Omicron Bode 100. Um basically, it's a vector network analyzer, but different to the RF vector network analyzer that we looked at in that previous Siglent video. This is a much more versatile bit of kit for your average you know, electronics design engineer. Let's take a look at it. So, in this box, we get two passive probes, which I think are optional extras well. I think everything's basically optional extra. I think you just buy the base Bode 100

**Dave Jones:** unit, but I'm very excited about this. We've got a wideband injection transformer. We'll go into that. I've been wanting one of those for ages. I've been thinking about building my own. That'll have to be a separate video. Look at passive component measurement test jig. And another passive component measurement test jig. Test jig should take a look at We've got a power supply. Then we've just got various probes and things, a test board, whatnot, various coaxials and stuff like that. Cool. Let's check out what this thing can do. So, what is

**Dave Jones:** this thing and why am I so excited about it? Well, it's basically a vector network analyzer as I said or an impedance analyzer, whatever you want to call it, but it does have vector network analyzer capability, but instead of as we saw in the previous video being for RF type stuff, this is basically from DC to 50 MHz bandwidth. So, it's much more much more useful for more practical electronic stuff. Things like you know, measuring the stability of control circuits. I eat power supplies which I'm

**Dave Jones:** going to have to do a totally separate video on cuz that's like a 30-minute whiteboard thing in its own right via one of these voltage injection transformers. And I don't so I don't think I'll be able to demonstrate that in this video. Maybe. We'll have a look.

**Dave Jones:** So that allows you to measure the performance and stability and calculate what sort of output capacitors and things like that you need for not only your own DC to DC converters, but for off-the-shelf linear regulators and stuff like that. You can do complex impedances of various components. So I've done that before in an old video which I'll link in down below where I used a red Bataya to measure the impedance over frequency up to I think 40 or 50 megahertz like this one does.

**Dave Jones:** But I used that red Bataya to measure the parameters of a bypass capacitor that you typically use on a board. And that video, well, we did get a plot out of it, but it was a bit meh. You know, a bit how you doing. This though, the Bode 100, is a professional bit of kit for actually doing those sort of impedance measurements on individual components, capacitors, inductors, and all sorts of things. We could do things like measure the complex impedance of power planes and the effectiveness of bypass capacitors.

**Dave Jones:** I want to do a whole video on that. Yeah, being given the frequency range you can measure resonance stuff for things like near-field communication stuff. You can measure the performance of crystals, piezo transducers, and of course you could do like filter swept filter performance curves, you know, amplifiers, you could do EMC stuff, a whole range of stuff. So having a DC to 50 megahertz vector network analyzer impedance analyzer is a much more useful bit of kit for your average, you know, electronics engineer just designing, you

**Dave Jones:** know, like piece of non-RF type stuff. It just allows you to do a whole bunch of things and I can't wait to see like I can just think of like half a dozen dozen videos off the top of my head that I could use this bit of kit for that really I didn't have the capability to do it before this. So, thank you very much Omicron for sending this baby in. I've been actually trying to get my hands on like a, you know, a like a 100 MHz or a, you know, DC to 100

**Dave Jones:** MHz vector network analyzer, you know, like second hand old, you know, HP or Agilent one or something like that on eBay, but this is like a modern USB type one and it's got all the software bells and whistles that we could possibly need. So, this will be a review video and I won't be tearing it down in this video. I'll link in a separate teardown video at the end. If you want to see how this baby works. And basically, it's we've got a signal generator output 0 to 50 MHz. I'll put

**Dave Jones:** up the specs here so that you can see the entire performance specs for this thing. And then we've basically got two inputs in here. Now, you don't have to use them all the time. You can get, depending on the measurement configuration, the thing that you're actually trying to measure, you might use one or both of these inputs here.

**Dave Jones:** And as I said, everything's optional with these a wideband injection transformer like test jigs for passive components. You whack your little surface mount component in there and it probes out. Oh, that's just isn't that just sex on a stick? Look at that.

**Dave Jones:** Unbelievable. And then we've got our main unit, which is actually very nicely designed and constructed. I really like it. We've just got a 10 W plug pack input here, an earth in terminal. You might need that depending on your system configuration and a simple USB type input. So, this is a very nice bit of professional kit and it want to be for the price cuz this is about 5,000 US bucks. And you might choke at that, but hey, try and get a professional you know, VNA 50 MHz vector network

**Dave Jones:** analyzer for less that can do all the stuff this one can. I think you'll be hard-pressed. They included some probes which feel very nice. Oh, that's ridiculously sharp. Unbelievable. That's probably the nice probe and nicest probe I've ever felt the rubber on that.

**Dave Jones:** Beautiful. Made in Germany. Oh, this is just absolutely gorgeous. You just got to feel this thing to know how good a quality this is. Manufactured by PMK, is it? I don't know. Uh designed for Omicron. And it's a And it's just a 10:1 scope probe probe, 50 meg bandwidth cuz that's the bandwidth of this thing and 12.5 puff. That's not particularly low capacitance which might be important. If you're doing that, you'd have, you know, active probes or some other solution, but that is very nice.

**Dave Jones:** But they're optional. And this bit of kit is a wideband injection transformer, the W WIT 100. They actually make a couple of these. One is designed for like even lower frequencies than this one. It's a physically a much larger unit. Has to be to get a bigger transformer. And it's a 1:1 transformer.

**Dave Jones:** This one I think goes for about 600 bucks and you might think that's ri- diculously expensive for just It is literally a transformer inside. A 1:1 transformer. But try and get 1 Hz to 10 MHz characters. I'll put up the characteristic response of this thing and try and get that performance out of a wideband injection transformer. It is ridiculously hard to get a flat bandwidth like that out of this thing.

**Dave Jones:** Anyway, this is used for doing voltage injection into DC-to-DC DC power supplies. Basically, you put it into the feedback path of the voltage divider, and that's how you actually get the magnitude and phase response, the characteristic response of a DC-to-DC converter that allows you to check allows you to analyze the stability of the circuit with various loads or choose the correct output capacitor or the correct ESR. All that sort of stuff designed to DC-to-DC converters. As I said, that is a whole couple of videos actually in its own

**Dave Jones:** right. But, suffice it to say, this is the going price for injection transformers. You can like kind of do it yourself, and you know, you can even use like a mains transformer as an you know, a crude you know, Clayton's injection transformer, but you know, nothing beats this. If you have to measure a DC power supply, you're going to be forking out the five or six hundred dollars for a proper injection transformer. And if you think the rest of the stuff's expensive, this SMD adapter that just allows you to put

**Dave Jones:** your SMD part in there, and the spring God, it's beautiful. And you can even adjust it like that as well. Fantastic. This thing is like a thousand bucks just for this contact SMD adapter. But, if you're serious about you know, testing passive components, um then you know, it's it's it's nothing to pay something like this for a good test jig. Try and build it yourself just in time. And for those who are just pulling their hair out over my pronunciation of Bode, that's how it's commonly pronounced here in Australia.

**Dave Jones:** Not a Bode, not Bodey, not Bode. I know that's how the guy pronounced his name, but that's not how it's commonly pronounced here in Australia. So, just deal with it, all right? That's how I call it. It's the Bode 100. And of course, no expensive bit of measurement kit like this would be complete without of course your requisite calibration and conformance certificate.

**Dave Jones:** That'll keep your QA manager happy, no doubt. Hello Marcus Mark. Marky Mark. And the Funky Bunch. Hmm. Mark Wahlberg in a previous in a new life. Has he given up the movies? Anyway, um and we get one for the injection uh transformer as well, which is fantastic, which is what you'd expect when you pay your 500 bucks. And the test adapter as well. So, you know, it's all there. Fantastic. So, this is basically one of the most professional bits of kit you can actually get for

**Dave Jones:** doing frequency response analysis, you know, vector network analyzer stuff up to that 50 MHz thing. Um so, let's take a look at the software here because that will pretty much explain everything. I guess I've had a quick play around with it and it looks very impressive. Of course, it's all about the software in a case like this. You know, like the hardware's like impressive in its own right, but it won't be for the money.

**Dave Jones:** But really, what you're after is the software that allows you to do, you know, really simple stuff like this. So, let's have a look at the Bode Analyzer Suite 3.12. That's the one that came on the CD. I'm not sure if there's a newer one. I'll try not to chop off some of this here.

**Dave Jones:** But basically, looks like we've got some uh recent I haven't done those. But let's have a look. We've got vector network analysis VNA and we've got impedance analysis as well. And the good thing about this is is that it shows you actually how to hook up the individual items and what they actually do. So, in this case, looks like we've got three of them. Didn't expand them all. Should by default. Anyway, we've got transmission and reflection analysis. So, yes, it can do S parameters just like the Siglent RF

**Dave Jones:** VNA that we looked at. It does S11 and S21, does it? Yes, S11 reflected and S21 transmitted, which is your basic two-port vector vector network analyzer. And you can simply just start the measurement right here. Or we can do gain phase analysis, which is your basically basic uh frequency response transfer that you get for a filter or something like that. So, in this case, it's your device under test. You know, it could be a simple RC filter or anything like that. Or it could be an

**Dave Jones:** amplifier or whatever. And this is how you hook it up. The output here, you're measuring the output directly. Well, you're measuring the input directly on channel 1 and the output on channel 2. And we can do reflection with the next external directional couplers as well. So, if you're into measuring directional couplers and stuff like that, beauty. This thing will do the business.

**Dave Jones:** So, and and in terms of a pin impedance analyzer, look at all these Look at all the different stuff it can do here. This is just ridiculous. But it's great. This is how much effort they've gone to in the software. And this is really what you're paying for is the finesse in the software in this case. So, you know, cuz the hardware's not worth $5,000, right? It's like and and this little adapter here is not worth, you know, $1,000, right? But it's the it's the research and the you

**Dave Jones:** know, even though it's great a build quality as these things are, they're not physically worth that. But you're paying for all the software and R&D and everything else. So, anyway, we can do one port just reflection analysis. So, can we do like, you know, maybe distance to fault or something like that? We should be able to see things like that. Basic impedance analysis as well. It that's what we can use this thing for the impedance analyzer adapter the W big or the W SMC adapter. So, that

**Dave Jones:** allows us to measure our capacitors, our inductors, other surface mount components for to get a frequency and phase response over sorry, a magnitude and phase response over frequency. Shunt through we'll probably use that for measuring we'll just get a gain gain plot of the injection transformer, shall we? Shunt through with through resistance, series through voltage and current. So, if you had a current probe, I assume they sell a current probe. I haven't looked or you could use like a you know, an off-the-shelf one or something like

**Dave Jones:** that. Assume you can calibrate the input and stuff like that. So, you can use your standard voltage probe and current probe to measure that and or you can measure external bridges. So, it it all just installed quite nicely. There were no issues. I just plugged it in. No drivers to dick around with. It just worked. So, let's go in and let's try the impedance analyzer, shall we? If we go in and start measurement then it did when I booted it up before, it did actually go through a calibration

**Dave Jones:** procedure which took a minute or two. I'm not sure if it does that doesn't look like it's not looking like it does that this time. Maybe it was only the first time it started or something. So, it's probably got the hardware inside to allow automated calibration. All right, so let's go in and measure a don't know if you can see it, but a 0.1 nanofarad I think it's a 0805 ceramic cap. So, as I will link in at the end, I've done this with a crudely very

**Dave Jones:** crudely with a cobbled together system with a VNA with a red pitaya to give us the magnitude and phase response of or it just magnitude? I can't remember. Um, response of uh some bypass capacitors, but this is the professional way to do it. So, anyway, let's have a look at the um software and see what it has to offer here.

**Dave Jones:** Now, look at all the axes. Uh of course, you can do logarithmic or linear axes like that. Uh level, constant, or uh variable. And you can shape the level, too, which is a very interesting uh thing which is um really quite valuable if, depending on the frequency uh you're at, you might find that you get lots of noise at sort of the low end or high end or whatever, depending on the thing that you're actually trying to measure. And then you can actually shape the use this tool to

**Dave Jones:** actually shape How do How can we do it? Uh I guess we've got to just add the points in here, reference levels, full frequency range. I haven't I haven't actually tried this, but you can actually shape this output signal level based on the frequency so that you can give you uh like a greater signal-to-noise ratio, depending on um the type of thing that you're actually measuring. So, if you getting lots of noise and crap on your waveform at a particular freak at a low end or a high

**Dave Jones:** end, uh for example, you can shape the output signal level to give you a higher level to compensate so that you get greater signal-to-noise level. And that is the attention to detail you get in a professional bit of software like this.

**Dave Jones:** They've thought of everything. That's absolutely fantastic. Um and uh there we can set the receiver bandwidth. So, we can set our start frequency uh 40 MHz. It does go up to 50 uh MHz, this bit of kit. It's basically DC to 50 meg, which pretty much covers most stuff um you know, you would deal with in electronics in basic electronics design. Over that, you sort of start getting into the high-end side of town.

**Dave Jones:** You know, you'd probably be using a you know, a 20 30 thousand dollar bit of uh VNA kit from, you know, the likes of Keysight or something like that. Anyway, uh full range, we can that just gives us Oh, open short load calibration as well, which of course you need for a vector network analyzer. We did get some uh loads in the I think we got the calibration kit with it. This I love.

**Dave Jones:** Check it out. This has uh this screen will change depending on which particular mode that you're in. We're in the frequency response analysis mode at the moment and it shows us the internals of how it works. And at the moment we can we haven't got the 50 ohm turn No, we we don't. I think it's forcing us No.

**Dave Jones:** I have been able to do that before. I have been able to switch the 50 ohm internal 50 ohm load off and on. Uh anyway, um it's not letting it does let you do it at some stage. Anyway, you can see that the internal output path here can actually measure the internal reference and the receiver two can do that. So, that's how it's obviously using uh there's two receivers inside.

**Dave Jones:** So, that's how it can get the S11 reflected power coming the reflected measurement coming back. So, anyway, you can set all that stuff up. So, we've got our cursors. So, let's go from 100 hertz. Let's go over the full range, shall we?

**Dave Jones:** 50 meg. You have to you type in meg and we don't want to go really low frequency, otherwise it takes too long. You know, if you set it to 1 hertz can take like minutes. We haven't set it up.

**Dave Jones:** It's not letting us do it. I'll get back to you. Aha, it's not actually going to let us do this without This command is currently disabled. A calibration is required. So, we have to go through the calibration first. I hadn't actually used this impedance response one before. So, calibration it is. And of course that makes sense because we have to compensate for the jig. So, it's not going to just let us run the test willy-nilly, is it? And that's why we have this screw terminal thing here

**Dave Jones:** which allows us to open it. The open we're doing over the full frequency range, so it's compensating for all of our jig. Overload occurred. Whoa. I am not sure what happened there, but I just ran it again and it was fine.

**Dave Jones:** Maybe that was a glitch in the matrix. I am wearing a very static-y um pair of jeans on today. It's not good. I'm zapping everything. Okay, and then we take that back out and we do the short. Beautiful. And load, well, our load resistor in the box, we did actually get um 100 ohm 0.1% calibration resistors. Nice. So, I'll put that in there.

**Dave Jones:** And it's really quite good that they force you to do this because otherwise, if you're inexperienced, you will just Well, or if you're just excited to play around with it like I was, you would just run the test and you'd get something and and you know, you'd think that's your response, but you're not compensating for all of the leads and everything else. And that test fixture, that's an inductor in its own right in there with the shaft and everything else. And you know, you got to compensate for that.

**Dave Jones:** Otherwise, you know, they they're forcing you to do a professional measurement. So, let's do our load. By default, it was 100 ohms. And oh, short delay time so that you can manually switch it in. They thought of everything. Little touches like that. It was like you wouldn't think of that from day one when you're writing this software.

**Dave Jones:** And that would come about because oh, wouldn't it be nice if like oh, it's frustrating. I've wish it would delay by 5 seconds minutes so I can run over and like press the short it out or something like that. So, there's our 100 ohms.

**Dave Jones:** Beautiful. We're ready to go and it's enabled our measurement now. Cool. .1 mic. 100 N cap back in there and okay, let's run from 100 hertz to 50 meg. Um, I'm just going to leave all the uh stuff default. We'll figure that out later. We don't want to run continuous. Let's just run a single sweep.

**Dave Jones:** Uh, that wasn't very exciting, was it? We can auto optimize. Look at that. And here's what I'm talking about in terms of that uh shaped variable and we can shape the level. So, we're getting all this noise down at the low frequency end of the spectrum. Um, so our signal level's obviously too low. So, we need to boost that up uh to compensate there.

**Dave Jones:** And by the way, I do like this receiver one and receiver two signal levels. Let's just run that again. Just run a single sweep. You can see receiver level one, whoop, the green bars went up. They'll turn red if they're going into overload. So, you can see the signal level. Would have been nicer to have them maybe longer or something like that. I don't know why they couldn't have spread them, you know, made them double that length or triple that length or something. But, it's awesome that

**Dave Jones:** they have that cuz you don't want to be measuring down in the noise um and you don't want to be uh peaking as well. But, it does tell you if you're getting overload, by the way. So, that's what we can use our um variable shaping. Let me play around with it. Let's see if I can get it. And we should get a smoother response down here. So, what we can do is double click here. And we're getting like uh 10K. I think below 10K, for example. Can we double click like that

**Dave Jones:** and can we drag a second one? So, there you go. That's fantastic. So, at 10 kilohertz, let's just do the 10 kilohertz jump there. So, well, actually, we want it above, don't we? Uh, 10 DBM higher at uh anything below 10 megahertz. So, let's try that. But, let's have a look. No, receiver one. Oh, nice. See? Got an extra wiggles down in there. Aha, so we can drag the reference level down like that. That's really groovy, isn't it? Wow, we're getting much greater variance now.

**Dave Jones:** So, let's go right up to 13 dBm there. Is that better? I think that's a bit better than before. Uh I don't know. Anyway, that's what the shaping tool's for. Duh, stupid me. That was a PEBCAK. I was actually measuring my 1 nF, uh not 100 n. So, uh Here's our 100 n uh response, and that's why it was sort of like off the scale, off the 50 meg, and we didn't uh get any response from that. So, here we go. But, now we can see the magnitude and phase

**Dave Jones:** at uh What is it? I don't know. We could use our cursor there, I'm sure. Oh, no, that's just zoom in. There you go. Can we uh reset zoom? There we go. So, now we can actually see the red trace here, trace one, which is the impedance, and you can get reflection and admittance, and it's absolutely fantastic. Um and or you can set it. Ooh.

**Dave Jones:** math math Uh Which function? Oh, that's it. plus up No. How do How do I reset that? No. There we go. Anyway, we can see our classic uh response here at um dipping at a particular the resonant frequency for that particular multi-layer ceramic capacitor, and I've done a whole uh tutorial video on bypass capacitors, which I'll link in at the end, explaining all this. But, there you go.

**Dave Jones:** We can actually measure that capacitor, and that gives us a fantastic response. And you can see that the phase uh changes here drastically as well on the blue. Here it goes from uh -90 to +90 at that uh resonance point, as you'd expect. But, hey, if we can do one capacitor, we can do two to try and combine the responses, which is what I tried to show in my previous video. So, the 100 n uh so, the 1 n unfortunately the 1 nF uh cap is going to be beyond

**Dave Jones:** the 50 MHz uh range to get that resonant uh frequency. So, let's do like a 10 microfarad or something so can So, let's combine a 100 n and a 10 mic cap in parallel and see if we can get the double dip response in there. All right, so there's the response for a uh 10 microfarad 0603 cap just uh some 100 low one out of the kit. So, I'll try and put both in there at the same time, combine them, and we should get the dual response in there

**Dave Jones:** happening one at the 1.8 mega whatever it is and the one at like 11 MHz. Okay, I'll just uh run that again because I uh just got another 0603 uh package one. Happens to be around about the same uh resonant frequency there. As I said, that's going to change in the previous video analyzing bypass caps, that's going to change with the type of uh package that you have, and all sorts of uh construction things to do with the multi-layer ceramic capacitor. Anyway, so, I'll now combine

**Dave Jones:** the two of those. Let's see if I can do it without soldering. I don't want to have to dick around soldering the two of I can get both of them. Hold your tongue at the right angle both to contact at once, hopefully.

**Dave Jones:** We ought to get the dual response. YEP. OH, NO, WE ONLY get the one one response. Bummer. Got to get this bastard. We got it. I've got to hold them together here. You can see the broader response like this. In fact, let's let's do continuous, shall we?

**Dave Jones:** Watch this. Right? If I take my tweezers. Oh, there we There we go. There we go. We can see the much broader response there over which the uh the two capacitors combined is a lower resistance like that. So, now let me now separate Oh, what? Yeah, there we go. We're we're back to the single one. Only have to touch it slightly and you combine the two like that.

**Dave Jones:** Or if you go back to just the original one, uh or the original one over here. There we go. So, you got that sharp response combined with the like 1 and 1/2 meg or whatever it is combined with the one at just over 10 or 11 meg and they both together they will give you a broader response. Cool, huh?

**Dave Jones:** And that's a much better response. That that's a much more professional measured response than we got with our cobbled together red potato system, that's for sure. So, then of course we've got our cursors here, so you can set them up and you can get deltas as well for those things. So, you know, it's got all the functionality you need. So, we can copy the image to the clipboard, so you can put it in your design notes and meeting notes and things like that.

**Dave Jones:** Impress your boss. So, was your $5,000 well spent? No wuckers. You know, something like this could easily pay for itself in next to no time. It's it's cheap for a professional bit of measurement kit. Anyway, trace one and trace two we can actually set like Y maximum like 10 1 milli, so we can change our scale there. 10 milliohms like that. Can change your phase response axes as well. So, we can get reflection as well. There you go.

**Dave Jones:** For those curious. And admittance, which is basically the inverse cuz that's basically the definition of it. Instead of peaking down like that, it peaks like that. And have a look at the formats we can do. Magnitude's not the only one. We can do magnitude in dB as well. We can do well, phase cuz that's what we've got down the bottom here.

**Dave Jones:** We can do radians for those radian fanboys. Got polar imaginary, um, RS, LS, CS, quality factor as well. The quality factor if your capacitance there. Fantastic. We can do all these stuff and get all these measurements, even the um, uh, tan theta as well. Terrific. We can measure the performance of our components. Of course, it it'd be really nice if this went higher than 50 meg, but as I said, 50 meg is really quite capable for you know, the majority of basic electronics applications.

**Dave Jones:** Certainly more than enough. Um, it's probably several orders more than enough for uh, your like a DC-to-DC uh, power supply analysis and stuff like that. But when you're analyzing components like this, especially the lower value ones, of course, you need the, you know, the hun- you need the hundreds of megahertz, probably even a gig if you're into but basically then you're measuring RF components and you need like an RF uh, VNA, basically. And as you'd expect, you can't actually uh, do things like averaging and stuff like that. So, I can

**Dave Jones:** uh, view here. We can do average measurement. Um, we can set 10 sweeps. That's enabled. Yeah, there we go. Completed sweep. So, it will, if you set it to continuous, it's not a good waveform cuz it's it's fairly clean here, but uh, you know, we can change that and uh, and another good thing is that you can go into view auto access placement and you can go one axis per chart.

**Dave Jones:** So, there you go. If you didn't If you didn't like your split axes on the uh, left-hand uh, side there, you can just separate them. Brilliant. So, we should be able to smooth out some of that if we did some averaging, for example. So, if we turn on the average and just go for our continuous, we'll have to do that over a couple of sweeps, but that's one way to reduce your uh, a bit of your noise.

**Dave Jones:** And uh, No, that's a genuine response. Look at that. But ordinarily, we would have been able to get rid of that crap. This is not the best example. And let's just use the other test jig, actually, to measure a top-quality Chong X brand brand One Hung Low brand um electrolytic. So, let's whack that in.

**Dave Jones:** And well, you can see it. I've already got the response of it here. Um we can run that again. But yeah, you can basically see that uh you know, the um impedance is down Well, what is it? Let's go down here. Here you go. You green up there. You By the way, you can just type in Like if you wanted the impedance at 100 kHz for example, there you go. It immediately jumps over 82 uh {point} 782 mΩ. Um And this is why for a electrolytics, for

**Dave Jones:** example, they measure the ESR at typically 100 kHz. That's what it's specified at because it's basically resistive around that uh particular frequency. But uh like as you can see, like above that, the inductance um is going to dominate, and uh it's going to just go back up in impedance like that. So, really, these are, you know, electrolytics like these uh really only have a low impedance around, you know, a quite a narrow uh range. That's why, you know, these aren't particularly good for like bypassing an IC, for example. And also,

**Dave Jones:** what we've measured there is um basically the uh the ESR, the equivalent series resistance in mΩ there, 82 mΩ in this particular case at 100 uh kHz there. And so, it allows you to measure all sorts of parameters of your capacitor, not just that, but you know, you can measure, you know, we can go in there and measure our Q, for example.

**Dave Jones:** For all you Q fanboys, there you go. So, that's where you want the Q right down there. It's zero, you know, it's it's pretty good over a reasonable range, but above that, yeah, it starts to go to crap. And then there's some Actually, look, it comes back down there. So, there's some parasitics above, you know, the 10 MHz that's making it come back down. So, that's interesting. So, that is impressive functionality just for that one thing. How do we get home? Do we just go new? Just for the impedance

**Dave Jones:** analysis here. But then we can do one port reflection and stuff like that. In fact, let's just try that. Live, let's just leave our coax flapping in the breeze, shall we? Do our one port, discard all our changes before.

**Dave Jones:** And oh, yeah, and you can save to like memory and stuff like that. Where is it? Uh uh Yeah, measurement to new memory and things like that. You can set up multiple memories and do all sorts of other stuff. It's really quite cool. So, anyway, let's just go single.

**Dave Jones:** Shazam. Now, sadly, I'm I'm just using the coax like this. Sadly, the uh you know, it it doesn't like doesn't seem to give us like a distance to fault kind of thing or anything like that, even though in theory, um it should be capable of doing that. Um you can make it out, but it just doesn't have that uh functionality built in, unfortunately.

**Dave Jones:** So, that's just uh regular reflected stuff. So, there's our So, if we take off our 50 ohm, we can plug in a short, can we? There's our short. Heh. Neat. But, yeah, anyway, that's just our um single port uh reflected measurement.

**Dave Jones:** Okay, let's do our wideband injection transformer. I'm very excited about this for power supply measurement, as I said, cuz we're working on the microcurrent and other stuff. And I'm definitely um psyched to do videos on this. So, let's uh see if we can get a performance plot of this thing. It came with the uh little isolated adapter because this is um I'm not sure of the isolation voltage of this thing.

**Dave Jones:** But, uh you know, like several hundred Oh, by the way, made in Austria. Thank you very much. Probably uh hand hand wound by nude Austrian virgins the transformer in there, no doubt. So, let's do a a shunt through, shall we?

**Dave Jones:** Let's give it a whirl. Discard what we had before. Let's go. So, we wanted uh it's got 10 MHz. So, let's go to 20 meg, shall we? 100 Hz. And let's just uh let's just leave everything default and sweep that.

**Dave Jones:** And there is our response. Bingo. So, this is our uh impedance magnitude plot, and you can see at 10 meg, bingo. It's just gone to town at 10 meg. So, they were right with the uh 10 meg bandwidth, but that's the uh impedance um basically the impedance of the thing, but let's go measure uh the amplitude response. I just wanted to show you the impedance there. So, let's go back through, and we can now go gain phase.

**Dave Jones:** Let's give that a whirl. We will need We'll need our T-piece for that. So, there we go. Channel one on there. And are we good to go? Discard.

**Dave Jones:** Okay, let's just set standard levels, and let's give it Well, we need that 20 meg, 10 Hz to 20 meg. We can go further than that. Yeah. See how it is slower at the start there? If you went to 1 Hz, it'd probably take a few minutes. So, boom and then boom. Oh, she shot up.

**Dave Jones:** Oh, okay. Ah, yeah. There we go. Didn't have our 50-ohm terminator on. So, let's redo our 50-ohm terminator. Do that again cuz our magnitude shot up there um past 1 MHz and we should find it should now roll off.

**Dave Jones:** So, let's do that again. But, check it out. It is basically ruler flat. I'll zoom in on this. Can I zoom in while it's doing it? You bet I can. There we go. So, up. Look at that. That is uh you know, that is uh magnitude in dB. So, it's ruler flat. Look at that. Ruler flat up to pretty much up to 1 meg. Um uh but and then it's going to drop off, you know, and then at 10 meg or Sorry, past 10 meg. We can get our cursor

**Dave Jones:** there. We can actually measure that. It does It doesn't really snap. Would've been nice to have like auto I guess that's the only thing that's missing. I don't seem to have seen it is that like auto peak detection and stuff like that. That that would've been nice to have that.

**Dave Jones:** But, uh yeah, at uh 12.6 meg there, it's um rolled off. So, there you go. To get a ruler flat response like that in a to 10 MHz is just insane. Let's go down to 1 Hz and we'll see that'll actually take a while, I think.

**Dave Jones:** Yeah, it's not it's not doing anything at the moment. Yep, there we go. It's just going to take a while. But, to get a ruler flat performance on that sort of injection uh transformer over that bandwidth, wow. Um that is really nice. Um you'd have a hard time doing it you know? So, if you think you're 5 or 600 bucks for an injection transformer, which is the market rate for a good injection transformer, um, I'm not aware of any really cheaper. I'm not sure if anyone makes any cheaper than like 500

**Dave Jones:** bucks or something like that. Um, that that's what you're paying for. You're paying for that performance. Good luck trying to get a an off-the-shelf pulse transformer or something or winding your own. Uh, you might be able to wind your own if you know what you're doing, but a lot of experimentation.

**Dave Jones:** You'll spend more than that in an in hours just trying to, um, dick around trying to get that going. But, anyway, look down at 1 Hz there, it's bug raw. But, if you need to go even lower than that for specific, um, uh, control loops and stuff like that, then they do sell a much physically bigger one cuz it's got to have a physically bigger, uh, transformer in it that goes basically, you know, almost down to DC, which is ridiculous. I'm not sure of the exact

**Dave Jones:** frequency. Anyway, if you think this one's low frequency performance is good, they sell another one, which is even better. There you go. That's just fantastic response. Brilliant. And if we go in here and have a look at our transmission and reflected our S-parameter, uh, VNA stuff. Let's go in here. Let's have a look at our hardware setup. So, this is our transmission and gain. So, this is S21 parameters, of course, and it shows how the internal reference has been switched. Ooh. Oh, look, can even We can live switch it.

**Dave Jones:** There we go. Beautiful. It even it's realized what we're doing and it's changed it from S21 to the frequency response of the DUT. That is really nice. I like that. Brilliant. Anyway, um, so there's our S21 set up and uses receiver one internal.

**Dave Jones:** So, even I've got the coax hooked up here, it's not actually doing anything in that particular mode. And impedance and reflection, there, of course, we don't need anything else. So, we can do our S11. So, let's just run that.

**Dave Jones:** Now, I've just still got like just the transformer hooked up. There you go. So, there's our gain and our reflection as well. Now, the really good thing about this is that because we've got trace one and trace two, it's put them on here, but check this out and this is what the signal analyzer didn't have. Let's say we wanted a polar plot for trace one.

**Dave Jones:** Bingo, we get ourselves that polar plot there. And that's optimized, but it knows that trace two is a magnitude reflection magnitude measurement, so it it splits the screen like that and we can actually use our cursors like that to go to show the relationship between the different display systems cuz that's all they are. We're measuring the same thing whether it's a polar plot like this or a magnitude frequency response like this, it's exactly the same thing.

**Dave Jones:** It's just a different way to actually display it. So, that's really cool. It has that capability. That's just awesome. But, you know, if we wanted, we could Well, then we can do the impedance there. That's it's just really very impressive capability to be able to split those.

**Dave Jones:** And if we had a larger screen, I'm sure we'd be able to display more there. There's our Nyquist. Wow, there's our imaginary. Can we zoom in on that? Optimize The optimized zoom works really well. Just get you straight in there. Beautiful.

**Dave Jones:** This works so well. I'm very very impressed with this. It's great. And of course, you might have noticed there that our um our gain because we're doing gain here, then we don't have a Smith chart response cuz that is only applicable to the uh reflection uh thing. So, we'll have to go down to trace. I mean, we could do it up here.

**Dave Jones:** Let's do it up here. Let's let's select reflection, okay? And then our measurement uh and then our type, bingo! We get our Smith chart and our VSWR. And so, bingo! We're in like Flynn. Look at that. I'm kind of disappointed. Does that scale with the window? Yeah, it it does. So, if you had a bigger screen, you're going to get a bigger response on there. So, that's groovy. And you can combine the two. I mean, if you wanted to have your polar your gain polar plot down here, you

**Dave Jones:** could do that. Hopefully. Yay! Didn't make a fool out of me. There you go. That's fantastic. And then you can just move your cursors along on both of those and it Let's scale this one. Optimize that. Look at that. Beautiful.

**Dave Jones:** That's just It's just brilliant. Like, you know, imagine if this thing went to a gig. Like, it'd be be fantastic. But, that's the problem with these sort of vector network analyzers. They're They're basically either designed for your lower frequency end, like this one, like DC to 50 meg or DC to 100 meg or whatever it is, or they're designed for your more RF stuff. So, they might start at like 10 kHz or something like that and go up to, you know, 5 gig, 10 gig, 50 gig, if you want

**Dave Jones:** to spend $100,000, you know. Um stuff like that. So, they're you know, this is designed for the lower end sort of stuff, which if you're not into the RF side of things, this is much more useful for power supply measurements, larger larger component bypass component analysis, and you know, as I say, you could probably do some ground plane analysis with it. Um and a whole host of other stuff. So, it really is incredibly useful, and it's it's money well spent. This is a professional tool. I haven't encountered

**Dave Jones:** any issues with it so far. It looks very, very polished. But, that's what you expect. This is one of the best measurement solutions, one of the the measurement kits for this sort of um you know DC to 50 MHz lower end VNA uh type stuff. It's just all purpose design. It's basically the company does some other stuff, but this is their basically their main product, their main focus. No wonder it's very polished. And once again, you can do gain calibration on here, and you can do impedance

**Dave Jones:** calibration. There's one thing I uh think is missing here, and when you actually go back out and come back into this function, it forces you to recalibrate every time. I don't see an option to actually save the calibration at all. I mean, saving is just the uh just the bode uh file or whatever. So, uh maybe that does save it. I don't know, you know?

**Dave Jones:** Test or whatever. And will that prevent us from doing that every time? I don't think so. I'll test that. And by the way, you can export a PDF report, Excel. Fantastic. I don't know why I didn't try to No idea what Touchstone is. Um I'm sure a few people are screaming at me.

**Dave Jones:** Yeah, I know what Touchstone is. Touchstone is Touchstone every day. Um yeah, anyway, very uh comprehensive. So, look, right? So, I've saved that, so we can open. Okay, so let's go back out. Stick around here. Start measurement. Impedance analyzer.

**Dave Jones:** Bingo. We can't, right? We're forced to redo that calibrate. And if we go test, there we go.

**Dave Jones:** Oh, yeah. Yeah, there we go. It saved it. Nice. They thought of that. Brilliant. Well done. And for this adapter here, check it out. We got a very nice little uh short end load. You can see the uh on on the back there, there's a short on the top, and there's a the 100 ohm required 100 ohm on the bottom, and that can just use pull that back, and that just goes in. Ah.

**Dave Jones:** Does go in there like that. So, you can do your uh open short load compensation. Beauty. Okay, so what we're going to do now is have a look at an intermediate frequency filter there and also a crystal. I don't know what the frequency is there. I can't read it.

**Dave Jones:** So, we're going to have a squeeze at that and let's go into our S parameters transmission reflection measurement. Here we go. Discard changes. And let's go in to 100 kHz to 40 MHz. I don't think it's probably going to be like a an 8 MHz crystal or something like that.

**Dave Jones:** So, I've got to hook up the crystal first. Let's just use all default parameters. Oh, bingo. There we go. Looks like something's happening around about 12. Let's go to auto optimize. And let's do that again. There we go. And you'll notice that it does the dual sweep there because the it's got to change when it does the device under test the S21. It's got to do one sweep for that and then and then it does the other arrangement, which is the reflection. So, it can't do

**Dave Jones:** those at the same time. It does those at as different sweeps. So, look at that. There we go. Looks like we've got our 12 MHz. So, let's go in and let's say I don't know 6 MHz to give that a whirl. Oh, there we go. That's much better. We didn't see it before. We didn't capture the reflection on there cuz we weren't in enough. If we actually get some more points on that, we'll get higher resolution on that.

**Dave Jones:** Whoa, look at that. That's serious business. There you go. Got some artifacts there that we didn't see before. So, let's actually uh let's go 10 meg to 14 meg, shall we? Wow, look at that. You can really see.

**Dave Jones:** We can actually zoom in on that if we really wanted to. There we go. Look at that. But that is our That is our resonant frequency of our crystal. Just a smidge under 12 megahertz there. It's not quite bang on, is it?

**Dave Jones:** So, by the way, this I believe does have like a 2 ppm crystal reference in it. It's pretty good. 11.5 meg, 12.5 meg. There we go. Let's give that a whirl. Bingo. Wham, look at that. Boom. There's the reflection characteristics. There you go. Um, by the way, we can add oats as well. So, that's handy. Just when you do your screenshots and stuff like that describing your test setup and things like that. That's neat. Someone was thinking. So, this is actually really cool cuz what it shows us is the

**Dave Jones:** multiple resonant points of this crystal. These are the two primary ones. I mean, we can reset the zoom there. Like we've got other ones here, but they're lower amplitude. What we're interested here is these two points here. Now, one of those is going to be the the series resonant frequency and the other one's going to be the parallel resonant frequency depending on how you load the crystal and actually resonate. It's going to have slightly different. So, if we actually go in there and for the reflection, if

**Dave Jones:** we get the Q, here it is. Let's have a look at that. Oh, we're off scale. Let's auto optimize there. Look at that. There's our parallel resonant frequencies. And that one is close to pretty close to 12 there. We would have to, you know, go finer and get like 11.9, 12.1 or something like that. Or simply just get more points. There we go. Whoop.

**Dave Jones:** Whoop-dee-doo-dah. Beautiful. Ah, fantastic. So, that's a smidge under smidge under 12. There you go. 11.997. Uh there you go. You can calculate the uh calculate the error there, whether or not that's error in this crystal, which probably isn't as good as the one inside the Boat 100. Um cuz I believe it's a two PPM class job. But isn't that neat?

**Dave Jones:** There you go. Oh, and we've got a memory display on there, so we can actually um that's the good thing about the memory display. You can actually overlay previous results and stuff like that. Fantastic. So, you don't have to like post-process any of this stuff. You don't have to export it and you can you know do it inside the program and then do that one nice PDF report or screenshot. Beauty. And you can see the ridiculous amount of ridiculous value of Q there for the for the crystal. Look at that. The

**Dave Jones:** 21,000, 22,000, something like that. And zero down here just at either side. That's how selective quartz crystals are. Cuz they resonate at that one frequency and that's it. That's what makes them brilliant. So, hopefully you can see by this that uh this is a brilliant tool for analyzing like just components, crystals, uh resonators, filters, um the piezo ceramic transducers and stuff like that.

**Dave Jones:** I would have loved to have had this when I was walking working on underwater hydrophones and stuff like that to characterize them. You know, we used you know, not as modern instruments as this to do that back in the day. And this is just fantastic. We can go and go to town with all the different measurement um options and stuff like that. It's brilliant. This is just something you can't do. Like you can kind of like cobble this together with other tools, but like no, you get this and you do the

**Dave Jones:** job properly. And we should be able to do some more analysis through some sort of through Uh where's the through one? If they Yeah, series through they call it. There it is. So, let's do that. Discard changes. So, we're not doing our VNA, so we're not going to get any reflection uh type stuff from this, but uh we can run our uh 10 meg to 14 meg there.

**Dave Jones:** Zippity do-da, zippity day. So, we'll just zoom into that, but we'd better actually perform a through calibration on this thing. So, let's try that, shall we? So, pending calibration, full range. Let's just do the full range through calibration. Start.

**Dave Jones:** Boop boop boop boop boop. So, we're taking out the uh cables. We're compensating for that. Beautiful. Done. Advanced settings, we don't want any of that. Open short load, not not worried about that. So, we're good to go. So, let's actually widen that from 10 to 14 MHz.

**Dave Jones:** And do a sweep on that. There we go. Now, we should be able to actually work out the parallel capacitance of this particular crystal. Okay, so to get our parallel capacitance, let's turn off trace two here cuz that's annoying. Instead of impedance, let's go to admittance. Oh, do we have to redo it?

**Dave Jones:** Nope. Auto optimize. There we go. So, what we want to do is go away from the resonant point and we should be able to change the units or the format. Yep, there we go. There's the parallel capacitance, CP.

**Dave Jones:** Beautiful. And that should give us Oh, sorry. Wrong one. Um Let's go up here. Admittance. There we go. Parallel capacitance. Ta-da! And bingo, that gives us the result up there. There we go. So, we want to go away from the resonant optimize.

**Dave Jones:** There we go. Want to go away from the resonant point and you'll find that the trace capacitance area is just over smidgen over half a bee's dick over three picofarads. Fantastic. Because the crystal, of course, the reason that we're able to characterize this crystal is because it's not just a capacitor. Um you know, it's not just the two plates with the quartz. It's has parasitic components just like any capacitor does. There's a series resistor, series inductor, and a um another series uh cap in there uh

**Dave Jones:** basically in parallel with that. But oh, there you go. We can measure directly with this thing the the parallel capacitance. Brilliant. So, from those resonant frequencies there and these measurements, we can calculate things like the series inductors. You can calculate the quality factor and all sorts of stuff uh to do the all the all the parameters of your actual crystal under test. Fantastic. It's just using your basic uh formulas for your equivalent series um of your crystal.

**Dave Jones:** And I just switched over to our IF uh filter there, which should be a standard uh 10.7 meg. And sure enough, I'm still on the admittance um parallel capacitance uh range here. And sure enough, you can see the see the peak there at your Well, basically, yep, at 10.7 meg. Beauty. But of course, you know, that's you don't have to do the admittance. You can go back and do all your other stuff.

**Dave Jones:** And single whoop. Auto optimize. There we go. Woo! You can really see that impedance go right down to buggery. Well, not buggery, but you know, it goes right down there um at that resonant point. And once again, we're getting uh this noise and crap in here cuz they're they're like it's right down. Now, we can uh cuz it's right down in signal level, so we can fix that up by either changing our magnitude or we might be able to change our receiver bandwidth.

**Dave Jones:** Let's go down. Let's drop that by an order of magnitude down to 30 Hz and let's sweep that again. And yep, we're getting an improvement. It's going to be slower, of course, with the uh recei- with the lower receiver bandwidth, but we should see this clean up a tad.

**Dave Jones:** Bit more accurate. Yep. Yeah. Go back to 300. Drop that down to 10 dB. Run it again. Yeah, it's a bit better. There you go. And uh well, what was that? Uh can we go to zero? Not going to overflow, are we? Look at our receiver signal level down there.

**Dave Jones:** Nah, it's hunky-dory. There you go. So, we were right down in the noise there, pretty much. So, I think we'll leave it there. There is a ton more stuff I can do with this thing um which I will save for other videos um cuz I don't want to spoil it. Things like I would definitely going to do a separate video on uh the wideband injection uh transformer and uh using that to do voltage injection, which is one of the techniques to um do uh power supply regulation stability uh

**Dave Jones:** testing and stuff like that. So, we can It's a whole bunch of videos. If you want to see me do If you've got a suggestion for me to do a video on something, now I've got this bit of kit here in the lab, um there's just no shortage of stuff I can do videos on.

**Dave Jones:** It's absolutely fantastic. So, thank you very much, Omicron Lab. Obviously, that gets a massive thumbs up. Um it's just You could argue, yeah, it's a lot of money to pay, but the software looks very professional, very comprehensive. Haven't found any issues. Um and I haven't done a teardown yet. I'm going to have to do a separate teardown, but I'm sure the hardware's really nice inside. Anyway, and I want to see, hopefully, we can see inside this wideband injection transformer if they haven't potted it. I don't know. Feels a

**Dave Jones:** bit hefty, but yeah, this is a brilliant bit of kit. And if you, you know, if you've got a lab budget or something like that and you're wondering what else to buy, you know, and like five grand is suitable, get something like this.

**Dave Jones:** There's just so much stuff you can do with this, especially like if you're into power supply design and stuff like that, something like this is an absolute no-brainer. Maybe muck around with PCB, you know, bypass bypassing and stuff like that. Let me know in the comments what you would what type of video you'd like to see with a bit of kit like this. It's just absolutely incredible. So, yeah, I think it's worth every cent. So, yeah, it's not for every every lab, and yes, it is

**Dave Jones:** pricey, but I'm not really aware of as comprehensive a solution as this for anything less cost. If there is, let me know, and I'll check it out, but yeah, this is just absolutely fantastic. I love it. Works brilliantly.

**Dave Jones:** Oh, I'm just picturing all the videos I can do with this. It's fantastic. Anyway, I hope you liked the video. If you did, please give it a big thumbs up, and there should be videos at the end here. Hopefully, a teardown, maybe if I get that done and uploaded. After I might release them at the same time.

**Dave Jones:** I don't know. Anyway, I hope you liked it. As always, discuss on the EEVblog forum down below. Catch you next time.

**Dave Jones:** Mhm.
