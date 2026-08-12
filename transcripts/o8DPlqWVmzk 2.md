---
video_id: o8DPlqWVmzk
title: EEVblog #340 - USB 3.0 Eye Diagram Measurement
url: https://www.youtube.com/watch?v=o8DPlqWVmzk
source: youtube-asr
timestamps: {"0": 0, "1": 37, "2": 65, "3": 94, "4": 126, "5": 152, "6": 187, "7": 220, "8": 256, "9": 289, "10": 325, "11": 346, "12": 367, "13": 399, "14": 418, "15": 447, "16": 486, "17": 509, "18": 528, "19": 560, "20": 583, "21": 603, "22": 634, "23": 653, "24": 680, "25": 709, "26": 737, "27": 753, "28": 783, "29": 799, "30": 820, "31": 844, "32": 865, "33": 886, "34": 925, "35": 961, "36": 995, "37": 1023, "38": 1038, "39": 1071, "40": 1119, "41": 1151, "42": 1182, "43": 1208, "44": 1243, "45": 1275, "46": 1301, "47": 1331, "48": 1362, "49": 1373, "50": 1403, "51": 1441, "52": 1482, "53": 1503, "54": 1516, "55": 1539, "56": 1561, "57": 1581, "58": 1607, "59": 1641, "60": 1660, "61": 1679, "62": 1715, "63": 1744, "64": 1775, "65": 1791, "66": 1814, "67": 1847, "68": 1883, "69": 1916}
---

**Dave Jones:** Hi. Unfortunately, the Agilent 90000 series scope here, $140,000 worth, has got to go back. It's only a loaner. Not that I'd have much use for it here anyway. It'd probably just sit under the bench here gathering dust because it's absolutely useless as an everyday scope. It's just too high performance. It's too noisy. It's too convoluted to use. It's hopeless. But, I thought we'd do some quick tests before it goes back. Uh probing a signal which really only a scope of this caliber is capable of doing. I thought we'd measure

**Dave Jones:** USB 3.0 super speed and see what we can do. Let's go. And by the way, I'm not going to be doing serious, you know, in-depth measurements of USB 3.0 here. It's just playing around, see what we can come up with, maybe get an eye diagram, something like that, maybe even do some serial decoding of the data if that's possible. I don't even know if this thing has the software capability, uh software options to do that. I know it's physically uh capable of doing it.

**Dave Jones:** So, and I haven't read the USB 3.0 standards, none of that. So, don't and moan that I'm doing something wrong, not doing it right, I missed this, missed that. We're just going to have a play around, not reading the manuals, doing nothing, just a play around here, see if we can get something, um some sort of uh measurements and eye diagrams and stuff of a 5 gigabit uh per second USB 3.0 signal.

**Dave Jones:** It's going to be fun. All right. Now, what we're going to be measuring is one of these IC Box uh brand USB 3.0 RAID hard dual hard dual RAID hard drive uh systems here which I use for my backups. And I've uh taken it apart here so that we can access and probe the uh signals on the back there. And uh we'll have a look at the uh probe as well. I won't have the hard drives plugged in cuz I think we should actually get high-speed data in and out of this thing

**Dave Jones:** even though we haven't got the hard drives on there. You know, it should just do some comms and stuff like that. So we should at least be able to get some data out of this thing and that's what I'm going to probe. I'm going to probe the high-speed side of the USB connector because if you haven't seen the USB 3.0 connector there it is. It's um it is different to a standard connector.

**Dave Jones:** It's got two extra pairs on top here. It's backward compatible with USB 2.0 but it's got two extra high-speed pairs on the outside of the connector here and that's what's used one transmit one receive and that's what's used for the 5 gigabits per second data transfer in addition to the USB 2.0 the standard single pair up here with the 5-volt power as well. So there's a transmit and receive pair on there we can probe. So let's give it a go. And the cable of course is USB 3.0

**Dave Jones:** and it's got SS on there which stands for super speed which means it is 3.0 it's rated for that 5 gigabits per second and my HP DV7 notebook here it has also got a couple of super-speed USB 3.0 ports on it. Now if you have a look at the board inside this IC box here you can see this is the USB connector here and you can see that that differential pair on the top there that comes from the that's a standard USB pair there but you can see two

**Dave Jones:** additional pairs there AC coupled there they've got a series cap in there and two other differential pairs there the high-speed ones which are the additional pairs on the USB 3.0 connector there. And on the back of the connector here, you can see the standard four-pin arrangement in there for the standard USB 2.0. And then it's got two other uh well, it's actually got five pins. One's actually ground. And so it's got the two other pairs here. This is a through-hole connector. And I soldered it on to 0.1 in headers on there so that

**Dave Jones:** we can use the supplied adapter cable for our probe, which we'll take a look at to probe the signal without having to hold it in place. Now, I know this is not the best thing to do in terms of signal integrity. So if we're really probing this system properly, characterizing it at these sort of frequencies, we really have to probe it correctly. And I'll show you a proper probe in a second. But this will be good enough for today's experiment to allow us to measure the signal so I don't have

**Dave Jones:** to dick around trying to probe the thing properly. It'll do a reasonable job, but it won't be perfect. And here's the probe we're going to be using today. You've seen this before. I've showed it on one of the previous videos. An Agilent 1169A 12-GHz bandwidth differential probe. And it costs about $12,000 this probe. So it's about $1,000 per GHz. Go figure. Anyway, it comes with several of these little adapter cables. These are little coaxes, little micro coaxes. So it's got two of those in the end, one for the

**Dave Jones:** positive, one for the negative because it's a differential probe. And you can see that marked on there. Um and there there are several little adapters. These have got little coaxes. They'd be really top-quality coaxes. This one actually has its own part number. It is E2678A.

**Dave Jones:** There you go. I've no idea. You could probably pay a couple of hundred bucks for this little adapter, I'm sure. Um anyway, it came with the uh kit here and it has a little um a little uh two-pin um header on there which uh comes with a converter to convert into a 0.1 in uh header. So, it allows us to probe that directly.

**Dave Jones:** And here's the other probe it comes with. And if you really want to probe this thing properly, you would use this to probe directly onto um test pads or directly on the uh pads of the IC or the uh terminator that you're um using on your differential um pair transmission line. And you know, if you really want proper signal integrity, this is what you got to use. And uh we won't I don't think we'll bother with this today. Once again, it's got the same little micro uh

**Dave Jones:** coax inner face, but it's just got uh test pins that allow you to directly probe the circuit under test. And for those who really want to know, we're using an ASMedia ASM1051 chipset. All right, so I've got my probe hooked up here uh to one of the lines.

**Dave Jones:** I'm not sure whether or not it's transmit or receive, but this one seems a little bit uh cleaner than the other one. So, I'm going to assume it's the uh transmitter because it hasn't um you know, the signal hasn't degraded by the time it's got all the way down that 1 m long cable or or whatever it is. So, this is just you know, your basic regular oscilloscope um uh you know, it's uh triggering right in the uh oops, center of that bloody touch screen. Really annoying. I shouldn't

**Dave Jones:** poke at this thing. Anyway, we're talking 200 mV uh per division there. So, we're talking 200 400 600, you know, 7 or 800 mV peak-to-peak there for this differential signal. And uh as you can see, it's just all that random data in there, and we're looking at 500 picoseconds per division there. So, each one of those, you know, you can see one cycle there is, you know, that's 200 picoseconds per division. So, it's incredibly quick this thing. But, this is a 13 GHz 40 gig sample per second scope, and you

**Dave Jones:** can see that it is saying that we're operating at 40 gig samples a second using 2K points of memory. And obviously, the lower we go, it's only 1K points memory, so that's the minimum it's going to use is 1K of sample memory. Automatically adjust that sample memory at 40 gig. And if we go down, it's still 40 gig at 2K points.

**Dave Jones:** 40 gig at 8K points, 20K points. So, I can still do that sort of, you know, it still can do 40 gig samples second at 2 meg points, at 8 meg points. Right, we've got a massive and then it once it goes to 10 meg points, it drops down to 20 gig samples per second. Oh, gosh darn it.

**Dave Jones:** Can't keep up. Oh, what a heap of crap. Yeah, right. It's $140,000 bloody scope. It's brilliant. Okay, so you're still getting, you know, you can single shot capture that. Single shot captured it, and you can zoom in on that 8 meg of, you know, it's pretty crusty now cuz it's right down in there, but you know, it's still it's quite it's quite remarkable that sample rate and that amount of memory. But anyway, we're right down there, and we'll be able to have a look at this data.

**Dave Jones:** Now, of course, you know, you can't tell much from this at all. So, what we're going to do is try and get an eye diagram. So, haven't read the manual on this thing. I haven't used one of these beasties before. So, I'm going to go up in Well, hang on. No, let's see if we can get some persistence display on there.

**Dave Jones:** And let's have a look at that. So, let's go into uh measure and No, let's go into setup. Bloody touch screens. And display. Let's have a play around with that. Aha, color grade. There we go. Let's switch that on and see what Hey, there we go.

**Dave Jones:** We've got some persistence now that you're probably used to seeing on these high-end scopes. It needs time to to actually get the data, to acquire the data. And we're getting some persistence there. So, the red stuff is where you're getting more of the signal. Okay, it's right in you know, it's capturing that more times and down to like the green stuff there, which doesn't have which only happens very occasionally. And uh You can And it's got stats down here.

**Dave Jones:** There you go. It's got stats. White is biggest and like to how many times it's appearing on each individual capture. So, green is the lowest right up to white, which is the highest intensity. You probably can't see the white in there. Oh, it's you know, it's smack in the middle there, but there you go.

**Dave Jones:** That's the persistence display. I mean, it's operating very slow cuz it's got to do a ton of stuff. It's got 803 points there. But, that's the persistence display, but still that's not showing us a huge amount. What we really need to look at the signal integrity of a differential signal like this is to look at what's called an eye diagram.

**Dave Jones:** So, let's fumble around here and see if we can get an eye diagram which will allow us to analyze serial data, mask test measure eye pattern. There we go. There it is. We should be able to, you know, and it's got a ton of stuff that we can look at and we could spend days and days and days here analyzing the signal. In fact, it would probably take you a couple of days to set up the measurement. If you were doing really critical, if you were

**Dave Jones:** developing a USB 3.0 product and you really had to get critical measurements to make sure it passed the standard and all that sort of stuff, then, you know, you could spend days setting up and probing this just to get your one, uh, you know, set of measurements or something like that. So, really, you know, I don't have the time to, uh, do that. So, we're just playing around today and the USB standard would have, like, um, how, uh, oh, actually, that's just measuring.

**Dave Jones:** Okay? Ah, yeah, we're just in the measuring menu here. So, we're not, uh, and we can trigger on all sorts of stuff. Let's go into analyze. Let's go into serial data here. And, hey, here we go. Let's try a serial data wizard.

**Dave Jones:** That sounds good. We can do it all manually. Um, serial data analysis, here we go. We can turn on the real-time eye diagram. Actually, let's just switch that on. It should do that in real time. And at least points must be acquired for the Infiniium to recover the clock because it's got to recover the clock because we've only got one signal going in here. We only have the data going in. So, it's got to recover the clock signal from that before it can get that, um,

**Dave Jones:** before it can get that eye diagram. So, let's go into the serial data wizard, see what it can do. Looks like it's going to take us through clock recovery threshold, um, time interval measurements, real-time eye display clock, and acquisition. So, let's go in here and channel one. Yep.

**Dave Jones:** Second, uh, select the clock recovery method. It's got PCI Express, Fibre Channel, FlexRay. Um, so, let's leave it on its default second order PLL and see what we get. Auto scale the vertical, we don't need to do that cuz it's already pretty good there, I think. So, let's go next.

**Dave Jones:** Nominal data rate is 5 gigabits per second. I believe that's correct for USB 3.0. So, let's enter the damping factor damping factor for the PLL 0.707, that'll do. Not around. Going to use default or maybe somebody has set this up before me and they've had a play around. Turn on a time interval error measurement relative to the recovered clock.

**Dave Jones:** Sounds interesting. We'll turn that on and units in seconds. Next and we go into the real time eye. Here we go, turn on real time eye diagram. Bingo, that's what we want and that's what it should look like. It'll be a bit it'll be a lot fuzzier than that, I suspect, because our probing's not perfect. Use color graded display.

**Dave Jones:** Yeah, why not? And which bits to include? God. Anyway, sample rate 40 gig sample per second, fast update sounds good. Main time base scale 40 whatever. Yeah, I just want to hang on. Display clock in the main yep, let's do it. Finish.

**Dave Jones:** Woohoo! Hey, look at that. We have our eye diagram. Done. Beautiful. Now, this thing takes a while to process, so don't expect instant results here. And what it's doing is recovering the clock signal from this data and then it's overlaying that data on there to give you what's called an eye diagram and as I suspected, this one's pretty fuzzy. It wasn't as good as the example that we I back in the setup menu there and it tells you how many waveforms it's captured. There we go, it's a thousand

**Dave Jones:** now and um we're at 100 picoseconds per division, folks. Check it out. So, that one that half cycle there is 200 picoseconds. And anyway, the eye diagram allows you to show um basically you want the widest eye possible. That black bit in the middle, you want that to be as big and as wide as possible because what this is showing is a whole bunch of stuff. It's showing the uh jitter of the signal uh mainly which will close the eye in this X direction like this and

**Dave Jones:** then you can close the eye in the Y direction and uh the USB 3.0 spec or any of these high-speed uh signal specs will specify how big that eye has to be in uh both the horizontal and uh vertical directions like that. So, in terms of jitter, so if um you were getting, you know, if you had a very poor quality clock on this thing on your system, for example, and you got lots of jitter on your waveform, when the waveforms overlay themselves on there like that, you see how there's

**Dave Jones:** some data points falling in the middle, you'll find that that eye will close, you know, it won't be big and wide like this black, it'll close like that because your jitter will be too your clock jitter will be too much and it'll what's called close the eye in that direction and that's bad. And there's other stuff like um uh symbol interference and stuff like that. You can go Google all that sort of stuff and you can spend uh days just looking at um you know, how these uh

**Dave Jones:** what these eye diagrams can tell you and stuff like that, but there you go, that is that is fascinating. That is the eye diagram. Can we turn off the color gradient on that display? Color grade, there we go.

**Dave Jones:** There we go. So, we've turned off our color grade and we can see just the raw data there shaking around and jumping. And uh but occasionally you're going to get some data in the middle there and that's why that uh color um gradient is a good thing. That that persistence measurement. But there you go. That is And of course we can change the vertical on that as well. But that's the eye diagram for what I believe is the transmit signal. So, let me just probe the other

**Dave Jones:** one. I'll disconnect it and oops. And we'll reconnect it here. There we go. That's the other one. Hang on. Does that look better or worse? That's a bit worse, I think. It's a bit worse. So, and yeah, there we go. That's got issues with uh overshoot. There you can see the So, uh that is clearly there the receiver on this IC box because we're getting um level issues there due to our non-perfect transmission line.

**Dave Jones:** All right. What I've done now is I've um turned on the RMS jitter measurement. So, it's attempting to measure our jitter in there and you can see those auto cursors set up at that point. And there's our RMS eye jitter at mean is 1.27 picoseconds. And if we uh go back in there and do that again and say choose peak to peak instead.

**Dave Jones:** There we go. It's much larger now because it's getting the peak to peak value of that jitter. You can see basically from the um opening of one eye to the other eye there, the distance between those two black points in the eye is the peak to peak jitter. And that's uh Where is it? Um We're talking 197 picoseconds or 86 picoseconds or thereabouts.

**Dave Jones:** And there's a whole bunch of other stuff we can measure. We can measure, you know, duty cycle distortion, Q factor crossing, and the height and the width of the eye, and stuff like that. So, you know, if you want to measure the eye width for example, I use measured data, extrapolate using standard deviation, and really you can go to town on measuring, you know, uh you know, just measuring this stuff correctly. Let alone probing the thing.

**Dave Jones:** I mean, we haven't even probed this thing correctly, let alone measuring it um to the exact specifications of the USB 3.0 standard. I'm sure it's very complex. I don't think I've ever read the USB 3 standard actually, but I'm sure it contains all of this stuff, which would be critical to get correct signal integrity. And if you're designing a USB 3.0 product, you really need to get this sort of stuff um right. And it would you know, be over a standard length and type of cable and,

**Dave Jones:** you know, into a specific load and all sorts of stuff. So, um you know, really you can probably spend weeks actually characterizing your system for the to make sure it meets the correct performance targets. I'm just around with the clock recovery here. And really, if you don't get it right, you're screwed. I mean, if we set that to PCI Express, for example, we're just, you know, we're just not going to get anything there. And if we set the first order PLL nominal data rate, say at 2.5

**Dave Jones:** gigabit, we've got nothing. At 5 gigabit, there There we go. We are recovering a clock there. So, second order PLL, which is what we were using, and uh explicit second order PLL. Clock frequency 5 gig. Yeah, loop bandwidth we've got bugger all there. So, there we go.

**Dave Jones:** Whoop. Hey, hey, doesn't like that. 5 gig. There we go. Bang. We're spot on there, and I've got um we're measuring the transition bits there, and that's the de-emphasis bits, and what we're looking at before, which was both combined. There we go. Bang. That's the usual way you want to do it.

**Dave Jones:** And we can do mask tests, and we can set up, you know, we can set up automatic mask testing, which you've seen on like the cheaper Agilent 3000 X-series scopes and stuff like that. You can set up eye diagram mask test, but it wouldn't be capable of doing USB 3.0 cuz the bandwidth just isn't high enough. So, you know, we can turn on mask testing, but I'm not going to muck around with that. It just tells you if it passes a passes or fails a preset up condition

**Dave Jones:** um for your mask. You know, if your eye is too small, it'll automatically tell you. It'll tell you how uh how often it fails, you know, how many times per second it fails, and whether or not that meets a standard.

**Dave Jones:** Blah, blah, blah. And if you want to get your USB uh 3 product actually uh you can send it to a uh, lab and they will measure they'll know how to do all this sort of stuff, know how to analyze it, use these instruments like these and they'll, uh, provide you a report telling you if your, uh, product passes or fails the USB 3.0 spec. And we'll try and, uh, see if we can maybe do some serial decoding perhaps. I'm not sure if this one's got it, but

**Dave Jones:** um, set up. Geez, these touch screens are really touchy, pun intended. Um, serial decode. Hey, there we go. Well, hey, it's already on USB 3.0 and here's some of the stuff USB 3, 2, SPI, SATA, um, PCI Express Gen 3, all sorts of stuff, JTAG, LIN, InfiniBand, whoa, FlexRay, whoa, Ethernet, um, 10 gig, it does 10 gig, um, uh, Ethernet as well, but we want USB 3.0. Show decode, is that that's grayed out. So, data source one, channel one, bang.

**Dave Jones:** Uh, descramble. Uh, show decode. It's not there's no auto setup. It's all, uh, it's all it's all gone. It's not going to let us, uh, do it. I'm not sure what's going on here. Now, this looks interesting. I've gone into the, uh, jitter, analyze jitter menu up here and where looks like we can get a whole bunch of, uh, various jitter measurement stuff. So, this looks really quite neat.

**Dave Jones:** Data, time interval, data rate, clock recovery rate, de-emphasis, it's all there. Time interval error. And let's select something. Geez, we could really go to town here. It's not giving us anything. Maybe we don't have an No, maybe we haven't started it.

**Dave Jones:** Probably I didn't set it up right. Anyway, it does it will allow you to do all sorts of bit error rate stuff. Ah, man, you name it, this scope can almost certainly do it. Oh, I'll try the jitter wizard here.

**Dave Jones:** Worked for us before with the eye diagram. So, let's select measurement. I've selected the data rate. So, data rate fully automatic channel one. Yeah. Let's go in here. Thresholds individual sources channel one. Yeah. Whatever. Plots a histogram of all data rate measurements. Yeah, this is what we need. Turn on measurement histogram. You bet.

**Dave Jones:** It's not automatically showing up. Yeah. Jitter spectra turn on the jitter spectrum. You bet. Finish. Hey, there we go. There we go. That's a histogram of our data rate. Now, where's the scale for that? Measurement histogram. Data rate.

**Dave Jones:** Uh There we go. We're actually at standard deviation. We're uh sorry, our mean is 7.4 gigabits per second. What's going on there? Uh There it is. Mode uh 5 gigabits per second mode minimum maximum. Hey, I don't know what's going on there.

**Dave Jones:** But uh there you go. We can actually get up uh measurements. There we go. Data rate. Oh, yeah. Well, it is actually telling us that we are at 7 gigabits per second. Uh definitely has to be something wrong there cuz it's showing our minimum is 3.7, our max is 12.8 gigabits. There's something something screwy really going on there.

**Dave Jones:** So, I don't know. I'm not going to spend time mucking around trying to get that sucker working, but you see that it can do neat stuff like that and much, much more as well, I'm sure. Well, as for this serial decode thing, I relented and I called up the help for USB 3.0 and it says, you know, I show decode. I presume this scope does not have the USB 3.0 serial you know, it says it requires the USB 3.0 software.

**Dave Jones:** So, I can only presume because it's grayed out, these things were all grayed out. It didn't um it hasn't got the software option built in for that. Bummer. I'm sure that costs thousands of dollars when the scope costs $140,000.

**Dave Jones:** So, no doubt you've got to pay for all these individual software options. So, yeah, I think it's just it's just not going to let us do that. There's no auto setup, no nothing. Um So, looks like it doesn't it doesn't have it. Show decode, can't do it. What?

**Dave Jones:** What I've called up here is one of the demos where for the real-time eye with mask testing and it's put if I can close this stupid screen. There you go. It's it's showed us a really clean eye. Check out that. I mean, you know, check out the amount of black pupil in there for want of a better term, you know, it is you know, that is a really clean differential signal. That's a beautiful eye diagram. That's just, you know, if you see that sort of stuff on your if

**Dave Jones:** you see that sort of waveform on your system, you know, you're you're really sitting sweet. You laid out your board properly. You got all your controlled impedance traces correctly, all your terminations right, you know, all your shieldings right, you've got low clock jitter because, you know, look at the you know, the the width in there is just ah, it's just beautiful. So, this is a demo. Um if you probe the thing properly and design your system properly, you might, you know, you might never achieve that in your

**Dave Jones:** system. You know, it's all about meeting the specs and the uh tolerances and what is actually achievable in a practical system. But that I don't know if I can do anything else with that demo. I think it just displays um it was just a demo file really and it allowed me to uh uh maybe I can do Here we go, USB 3 serial decode. Maybe this is what it would have looked like um if we were actually able to do that. Yeah, there we go. This is

**Dave Jones:** This is what we would have got if we had um were able to get that serial decode option working. There's the USB uh packets, the time, and all sorts of stuff. And you can analyze that until the cows come home. Good stuff.

**Dave Jones:** More neat stuff this can do is uh FPGA dynamic probing. And uh this is the demo of it and if you insert a uh core, a specific core in the FPGA and you probe it, um then you can get all sorts of stuff. It helps us set up your scope and get real-time analysis of what's happening inside your FPGA.

**Dave Jones:** Neat. Sure it costs a fortune, of course. So, there you go. I hope you found this rather interesting. If you want to check out more, um go search for, you know, Google uh eye diagram uh measurements and stuff like that. I'm sure there's 10 million app notes and uh things out there which will um explain just what a valuable tool this is for um doing signal integrity measurements on differential um high-speed serial lines like this and um pretty much in all you know these high end scopes. This is one

**Dave Jones:** of the main things that they are capable of doing is measuring and analyzing and you know extracting the clock from the signal and displaying an eye diagram which is essentially the data waveform overlaid again and again and again on the recovered clock which it controls the horizontal axis is the recovered clock from the signal itself and from that you can tell an awful lot about the signal.

**Dave Jones:** But it was just good fun having to play around with this and see what the scope is capable of. I really rather like it. It's been fun and if you get a chance to play with one of these high end scopes by all means um play around with the eye diagram stuff because it can be a great deal of fun and you can learn a lot about signal integrity. You know if I could I could you know probe this in different ways and stuff like that and see how the

**Dave Jones:** signal integrity changes but haven't got the time. So if you want to discuss this jump on over to the EEVblog forum. The link is below the video there or above if you're on the blog website. And remember if you like it please give it a big thumbs up. Catch you next time.
