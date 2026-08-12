---
video_id: o8DPlqWVmzk
title: EEVblog #340 - USB 3.0 Eye Diagram Measurement
url: https://www.youtube.com/watch?v=o8DPlqWVmzk
source: youtube-asr
timestamps: {"0": 0, "1": 18, "2": 34, "3": 51, "4": 63, "5": 77, "6": 94, "7": 108, "8": 121, "9": 134, "10": 152, "11": 170, "12": 187, "13": 205, "14": 219, "15": 235, "16": 250, "17": 268, "18": 284, "19": 299, "20": 320, "21": 335, "22": 351, "23": 367, "24": 383, "25": 397, "26": 414, "27": 426, "28": 440, "29": 457, "30": 474, "31": 491, "32": 506, "33": 521, "34": 535, "35": 550, "36": 566, "37": 580, "38": 600, "39": 617, "40": 632, "41": 648, "42": 662, "43": 680, "44": 696, "45": 707, "46": 719, "47": 733, "48": 750, "49": 762, "50": 778, "51": 791, "52": 810, "53": 825, "54": 841, "55": 856, "56": 874, "57": 896, "58": 914, "59": 930, "60": 947, "61": 963, "62": 983, "63": 995, "64": 1009, "65": 1021, "66": 1034, "67": 1052, "68": 1067, "69": 1081, "70": 1103, "71": 1128, "72": 1151, "73": 1168, "74": 1188, "75": 1202, "76": 1219, "77": 1236, "78": 1249, "79": 1263, "80": 1280, "81": 1305, "82": 1329, "83": 1343, "84": 1359, "85": 1373, "86": 1386, "87": 1401, "88": 1421, "89": 1439, "90": 1463, "91": 1489, "92": 1506, "93": 1524, "94": 1542, "95": 1563, "96": 1581, "97": 1600, "98": 1615, "99": 1634, "100": 1650, "101": 1669, "102": 1685, "103": 1705, "104": 1719, "105": 1733, "106": 1749, "107": 1761, "108": 1777, "109": 1795, "110": 1808, "111": 1824, "112": 1840, "113": 1857, "114": 1878, "115": 1898, "116": 1914, "117": 1929}
---

**Dave Jones:** Hi. Unfortunately, the Agilent 90000 series scope here, $140,000 worth, has got to go back. It's only a loaner. Not that I'd have much use for it here anyway. It'd probably just sit under the bench here gathering dust because it's absolutely useless as an

**Dave Jones:** everyday scope. It's just too high performance. It's too noisy. It's too convoluted to use. It's hopeless. But, I thought we'd do some quick tests before it goes back. Uh probing a signal which really only a scope of this caliber is

**Dave Jones:** capable of doing. I thought we'd measure USB 3.0 super speed and see what we can do. Let's go. And by the way, I'm not going to be doing serious, you know, in-depth measurements of USB 3.0 here. It's just playing around, see what we

**Dave Jones:** can come up with, maybe get an eye diagram, something like that, maybe even do some serial decoding of the data if that's possible. I don't even know if this thing has the software capability, uh software options to do that. I know

**Dave Jones:** it's physically uh capable of doing it. So, and I haven't read the USB 3.0 standards, none of that. So, don't and moan that I'm doing something wrong, not doing it right, I missed this, missed that. We're just going to have a

**Dave Jones:** play around, not reading the manuals, doing nothing, just a play around here, see if we can get something, um some sort of uh measurements and eye diagrams and stuff of a 5 gigabit uh per second USB 3.0 signal.

**Dave Jones:** It's going to be fun. All right. Now, what we're going to be measuring is one of these IC Box uh brand USB 3.0 RAID hard dual hard dual RAID hard drive uh systems here which I use for my

**Dave Jones:** backups. And I've uh taken it apart here so that we can access and probe the uh signals on the back there. And uh we'll have a look at the uh probe as well. I won't have the hard drives plugged in

**Dave Jones:** cuz I think we should actually get high-speed data in and out of this thing even though we haven't got the hard drives on there. You know, it should just do some comms and stuff like that. So we should at least be able to get

**Dave Jones:** some data out of this thing and that's what I'm going to probe. I'm going to probe the high-speed side of the USB connector because if you haven't seen the USB 3.0 connector there it is. It's um it is different to a standard connector.

**Dave Jones:** It's got two extra pairs on top here. It's backward compatible with USB 2.0 but it's got two extra high-speed pairs on the outside of the connector here and that's what's used one transmit one receive and that's what's used for the 5 gigabits per

**Dave Jones:** second data transfer in addition to the USB 2.0 the standard single pair up here with the 5-volt power as well. So there's a transmit and receive pair on there we can probe. So let's give it a go. And the cable of course is USB 3.0

**Dave Jones:** and it's got SS on there which stands for super speed which means it is 3.0 it's rated for that 5 gigabits per second and my HP DV7 notebook here it has also got a couple of super-speed USB 3.0 ports on it. Now if

**Dave Jones:** you have a look at the board inside this IC box here you can see this is the USB connector here and you can see that that differential pair on the top there that comes from the that's a standard USB

**Dave Jones:** pair there but you can see two additional pairs there AC coupled there they've got a series cap in there and two other differential pairs there the high-speed ones which are the additional pairs on the USB 3.0 connector there. And on the back of the

**Dave Jones:** connector here, you can see the standard four-pin arrangement in there for the standard USB 2.0. And then it's got two other uh well, it's actually got five pins. One's actually ground. And so it's got the two other pairs here. This is a

**Dave Jones:** through-hole connector. And I soldered it on to 0.1 in headers on there so that we can use the supplied adapter cable for our probe, which we'll take a look at to probe the signal without having to hold it in place. Now, I know this is

**Dave Jones:** not the best thing to do in terms of signal integrity. So if we're really probing this system properly, characterizing it at these sort of frequencies, we really have to probe it correctly. And I'll show you a proper probe in a second. But this will be good

**Dave Jones:** enough for today's experiment to allow us to measure the signal so I don't have to dick around trying to probe the thing properly. It'll do a reasonable job, but it won't be perfect. And here's the probe we're going to be using today. You've seen

**Dave Jones:** this before. I've showed it on one of the previous videos. An Agilent 1169A 12-GHz bandwidth differential probe. And it costs about $12,000 this probe. So it's about $1,000 per GHz. Go figure. Anyway, it comes with several of these little adapter cables. These are

**Dave Jones:** little coaxes, little micro coaxes. So it's got two of those in the end, one for the positive, one for the negative because it's a differential probe. And you can see that marked on there. Um and there there are several little

**Dave Jones:** adapters. These have got little coaxes. They'd be really top-quality coaxes. This one actually has its own part number. It is E2678A. There you go. I've no idea. You could probably pay a couple of hundred bucks for this little adapter, I'm sure. Um

**Dave Jones:** anyway, it came with the uh kit here and it has a little um a little uh two-pin um header on there which uh comes with a converter to convert into a 0.1 in uh header. So, it allows us to probe that directly.

**Dave Jones:** And here's the other probe it comes with. And if you really want to probe this thing properly, you would use this to probe directly onto um test pads or directly on the uh pads of the IC or the

**Dave Jones:** uh terminator that you're um using on your differential um pair transmission line. And you know, if you really want proper signal integrity, this is what you got to use. And uh we won't I don't think we'll bother with this today. Once

**Dave Jones:** again, it's got the same little micro uh coax inner face, but it's just got uh test pins that allow you to directly probe the circuit under test. And for those who really want to know, we're using an ASMedia ASM1051

**Dave Jones:** chipset. All right, so I've got my probe hooked up here uh to one of the lines. I'm not sure whether or not it's transmit or receive, but this one seems a little bit uh cleaner than the other one. So, I'm going to assume it's the uh

**Dave Jones:** transmitter because it hasn't um you know, the signal hasn't degraded by the time it's got all the way down that 1 m long cable or or whatever it is. So, this is just you know, your basic regular oscilloscope um

**Dave Jones:** uh you know, it's uh triggering right in the uh oops, center of that bloody touch screen. Really annoying. I shouldn't poke at this thing. Anyway, we're talking 200 mV uh per division there. So, we're talking 200 400 600, you know, 7 or 800 mV

**Dave Jones:** peak-to-peak there for this differential signal. And uh as you can see, it's just all that random data in there, and we're looking at 500 picoseconds per division there. So, each one of those, you know, you can see one cycle

**Dave Jones:** there is, you know, that's 200 picoseconds per division. So, it's incredibly quick this thing. But, this is a 13 GHz 40 gig sample per second scope, and you can see that it is saying that we're operating at 40 gig samples a second

**Dave Jones:** using 2K points of memory. And obviously, the lower we go, it's only 1K points memory, so that's the minimum it's going to use is 1K of sample memory. Automatically adjust that sample memory at 40 gig. And if we go down,

**Dave Jones:** it's still 40 gig at 2K points. 40 gig at 8K points, 20K points. So, I can still do that sort of, you know, it still can do 40 gig samples second at 2 meg points, at 8 meg points. Right, we've got a

**Dave Jones:** massive and then it once it goes to 10 meg points, it drops down to 20 gig samples per second. Oh, gosh darn it. Can't keep up. Oh, what a heap of crap. Yeah, right. It's $140,000 bloody scope. It's brilliant. Okay, so you're still

**Dave Jones:** getting, you know, you can single shot capture that. Single shot captured it, and you can zoom in on that 8 meg of, you know, it's pretty crusty now cuz it's right down in there, but you know, it's still it's quite it's quite

**Dave Jones:** remarkable that sample rate and that amount of memory. But anyway, we're right down there, and we'll be able to have a look at this data. Now, of course, you know, you can't tell much from this at all. So, what we're

**Dave Jones:** going to do is try and get an eye diagram. So, haven't read the manual on this thing. I haven't used one of these beasties before. So, I'm going to go up in Well, hang on. No, let's see if we can

**Dave Jones:** get some persistence display on there. And let's have a look at that. So, let's go into uh measure and No, let's go into setup. Bloody touch screens. And display. Let's have a play around with that. Aha, color grade. There we go. Let's switch

**Dave Jones:** that on and see what Hey, there we go. We've got some persistence now that you're probably used to seeing on these high-end scopes. It needs time to to actually get the data, to acquire the data. And we're getting some persistence

**Dave Jones:** there. So, the red stuff is where you're getting more of the signal. Okay, it's right in you know, it's capturing that more times and down to like the green stuff there, which doesn't have which only happens very occasionally. And uh

**Dave Jones:** You can And it's got stats down here. There you go. It's got stats. White is biggest and like to how many times it's appearing on each individual capture. So, green is the lowest right up to white, which is the highest intensity.

**Dave Jones:** You probably can't see the white in there. Oh, it's you know, it's smack in the middle there, but there you go. That's the persistence display. I mean, it's operating very slow cuz it's got to do a ton of stuff. It's got 803 points

**Dave Jones:** there. But, that's the persistence display, but still that's not showing us a huge amount. What we really need to look at the signal integrity of a differential signal like this is to look at what's called an eye diagram.

**Dave Jones:** So, let's fumble around here and see if we can get an eye diagram which will allow us to analyze serial data, mask test measure eye pattern. There we go. There it is. We should be able to, you know, and it's

**Dave Jones:** got a ton of stuff that we can look at and we could spend days and days and days here analyzing the signal. In fact, it would probably take you a couple of days to set up the measurement. If you

**Dave Jones:** were doing really critical, if you were developing a USB 3.0 product and you really had to get critical measurements to make sure it passed the standard and all that sort of stuff, then, you know, you could spend days

**Dave Jones:** setting up and probing this just to get your one, uh, you know, set of measurements or something like that. So, really, you know, I don't have the time to, uh, do that. So, we're just playing around today and the USB standard would

**Dave Jones:** have, like, um, how, uh, oh, actually, that's just measuring. Okay? Ah, yeah, we're just in the measuring menu here. So, we're not, uh, and we can trigger on all sorts of stuff. Let's go into analyze. Let's go into serial data here. And, hey, here we

**Dave Jones:** go. Let's try a serial data wizard. That sounds good. We can do it all manually. Um, serial data analysis, here we go. We can turn on the real-time eye diagram. Actually, let's just switch that on. It should do

**Dave Jones:** that in real time. And at least points must be acquired for the Infiniium to recover the clock because it's got to recover the clock because we've only got one signal going in here. We only have the data going in. So, it's got to recover the

**Dave Jones:** clock signal from that before it can get that, um, before it can get that eye diagram. So, let's go into the serial data wizard, see what it can do. Looks like it's going to take us through clock recovery threshold, um, time

**Dave Jones:** interval measurements, real-time eye display clock, and acquisition. So, let's go in here and channel one. Yep. Second, uh, select the clock recovery method. It's got PCI Express, Fibre Channel, FlexRay. Um, so, let's leave it on its default second order

**Dave Jones:** PLL and see what we get. Auto scale the vertical, we don't need to do that cuz it's already pretty good there, I think. So, let's go next. Nominal data rate is 5 gigabits per second. I believe that's correct for USB

**Dave Jones:** 3.0. So, let's enter the damping factor damping factor for the PLL 0.707, that'll do. Not around. Going to use default or maybe somebody has set this up before me and they've had a play around. Turn on a time interval error

**Dave Jones:** measurement relative to the recovered clock. Sounds interesting. We'll turn that on and units in seconds. Next and we go into the real time eye. Here we go, turn on real time eye diagram. Bingo, that's what we want and

**Dave Jones:** that's what it should look like. It'll be a bit it'll be a lot fuzzier than that, I suspect, because our probing's not perfect. Use color graded display. Yeah, why not? And which bits to include? God. Anyway, sample rate 40 gig sample per

**Dave Jones:** second, fast update sounds good. Main time base scale 40 whatever. Yeah, I just want to hang on. Display clock in the main yep, let's do it. Finish. Woohoo! Hey, look at that. We have our eye diagram. Done. Beautiful.

**Dave Jones:** Now, this thing takes a while to process, so don't expect instant results here. And what it's doing is recovering the clock signal from this data and then it's overlaying that data on there to give you what's called an eye diagram and as I

**Dave Jones:** suspected, this one's pretty fuzzy. It wasn't as good as the example that we I back in the setup menu there and it tells you how many waveforms it's captured. There we go, it's a thousand now and um we're at 100 picoseconds per division,

**Dave Jones:** folks. Check it out. So, that one that half cycle there is 200 picoseconds. And anyway, the eye diagram allows you to show um basically you want the widest eye possible. That black bit in the middle, you want that to be as

**Dave Jones:** big and as wide as possible because what this is showing is a whole bunch of stuff. It's showing the uh jitter of the signal uh mainly which will close the eye in this X direction like this and then you can close the eye in the Y

**Dave Jones:** direction and uh the USB 3.0 spec or any of these high-speed uh signal specs will specify how big that eye has to be in uh both the horizontal and uh vertical directions like that. So, in terms of jitter, so if um

**Dave Jones:** you were getting, you know, if you had a very poor quality clock on this thing on your system, for example, and you got lots of jitter on your waveform, when the waveforms overlay themselves on there like that, you see how there's

**Dave Jones:** some data points falling in the middle, you'll find that that eye will close, you know, it won't be big and wide like this black, it'll close like that because your jitter will be too your clock jitter will be too much and it'll

**Dave Jones:** what's called close the eye in that direction and that's bad. And there's other stuff like um uh symbol interference and stuff like that. You can go Google all that sort of stuff and you can spend uh days just

**Dave Jones:** looking at um you know, how these uh what these eye diagrams can tell you and stuff like that, but there you go, that is that is fascinating. That is the eye diagram. Can we turn off the color gradient

**Dave Jones:** on that display? Color grade, there we go. There we go. So, we've turned off our color grade and we can see just the raw data there shaking around and jumping. And uh but occasionally you're going to get some data in the middle

**Dave Jones:** there and that's why that uh color um gradient is a good thing. That that persistence measurement. But there you go. That is And of course we can change the vertical on that as well. But that's the eye diagram for what I believe is the

**Dave Jones:** transmit signal. So, let me just probe the other one. I'll disconnect it and oops. And we'll reconnect it here.

**Dave Jones:** There we go. That's the other one. Hang on. Does that look better or worse? That's a bit worse, I think. It's a bit worse. So, and yeah, there we go. That's got issues with uh overshoot. There you can see the So, uh

**Dave Jones:** that is clearly there the receiver on this IC box because we're getting um level issues there due to our non-perfect transmission line. All right. What I've done now is I've um turned on the RMS jitter measurement. So, it's attempting to measure our

**Dave Jones:** jitter in there and you can see those auto cursors set up at that point. And there's our RMS eye jitter at mean is 1.27 picoseconds. And if we uh go back in there and do that again and say choose peak to peak instead.

**Dave Jones:** There we go. It's much larger now because it's getting the peak to peak value of that jitter. You can see basically from the um opening of one eye to the other eye there, the distance between those two black points in the eye is the

**Dave Jones:** peak to peak jitter. And that's uh Where is it? Um We're talking 197 picoseconds or 86 picoseconds or thereabouts. And there's a whole bunch of other stuff we can measure. We can measure, you know, duty cycle distortion, Q factor

**Dave Jones:** crossing, and the height and the width of the eye, and stuff like that. So, you know, if you want to measure the eye width for example, I use measured data, extrapolate using standard deviation, and really you can go to town on

**Dave Jones:** measuring, you know, uh you know, just measuring this stuff correctly. Let alone probing the thing. I mean, we haven't even probed this thing correctly, let alone measuring it um to the exact specifications of the USB 3.0 standard. I'm sure it's very

**Dave Jones:** complex. I don't think I've ever read the USB 3 standard actually, but I'm sure it contains all of this stuff, which would be critical to get correct signal integrity. And if you're designing a USB 3.0 product, you really

**Dave Jones:** need to get this sort of stuff um right. And it would you know, be over a standard length and type of cable and, you know, into a specific load and all sorts of stuff. So, um you know, really you can probably spend

**Dave Jones:** weeks actually characterizing your system for the to make sure it meets the correct performance targets. I'm just around with the clock recovery here. And really, if you don't get it right, you're screwed. I mean, if we set that

**Dave Jones:** to PCI Express, for example, we're just, you know, we're just not going to get anything there. And if we set the first order PLL nominal data rate, say at 2.5 gigabit, we've got nothing. At 5 gigabit, there There we go.

**Dave Jones:** We are recovering a clock there. So, second order PLL, which is what we were using, and uh explicit second order PLL. Clock frequency 5 gig. Yeah, loop bandwidth we've got bugger all there. So, there we go. Whoop. Hey, hey, doesn't like that.

**Dave Jones:** 5 gig. There we go. Bang. We're spot on there, and I've got um we're measuring the transition bits there, and that's the de-emphasis bits, and what we're looking at before, which was both combined. There we go. Bang. That's the

**Dave Jones:** usual way you want to do it. And we can do mask tests, and we can set up, you know, we can set up automatic mask testing, which you've seen on like the cheaper Agilent 3000 X-series scopes and stuff like that. You can set up eye

**Dave Jones:** diagram mask test, but it wouldn't be capable of doing USB 3.0 cuz the bandwidth just isn't high enough. So, you know, we can turn on mask testing, but I'm not going to muck around with that. It just tells you if it passes a passes or fails

**Dave Jones:** a preset up condition um for your mask. You know, if your eye is too small, it'll automatically tell you. It'll tell you how uh how often it fails, you know, how many times per second it fails, and whether or not that meets a standard.

**Dave Jones:** Blah, blah, blah. And if you want to get your USB uh 3 product actually uh you can send it to a uh, lab and they will measure they'll know how to do all this sort of stuff, know how to analyze

**Dave Jones:** it, use these instruments like these and they'll, uh, provide you a report telling you if your, uh, product passes or fails the USB 3.0 spec. And we'll try and, uh, see if we can maybe do some serial decoding perhaps. I'm not sure if

**Dave Jones:** this one's got it, but um, set up. Geez, these touch screens are really touchy, pun intended. Um, serial decode. Hey, there we go. Well, hey, it's already on USB 3.0 and here's some of the stuff USB 3, 2, SPI, SATA, um, PCI

**Dave Jones:** Express Gen 3, all sorts of stuff, JTAG, LIN, InfiniBand, whoa, FlexRay, whoa, Ethernet, um, 10 gig, it does 10 gig, um, uh, Ethernet as well, but we want USB 3.0. Show decode, is that that's grayed out. So, data source one, channel one,

**Dave Jones:** bang. Uh, descramble. Uh, show decode. It's not there's no auto setup. It's all, uh, it's all it's all gone. It's not going to let us, uh, do it. I'm not sure what's going on here. Now, this looks interesting. I've gone

**Dave Jones:** into the, uh, jitter, analyze jitter menu up here and where looks like we can get a whole bunch of, uh, various jitter measurement stuff. So, this looks really quite neat. Data, time interval, data rate, clock recovery rate, de-emphasis, it's all there. Time

**Dave Jones:** interval error. And let's select something. Geez, we could really go to town here. It's not giving us anything. Maybe we don't have an No, maybe we haven't started it. Probably I didn't set it up right. Anyway, it does it will allow you to do

**Dave Jones:** all sorts of bit error rate stuff. Ah, man, you name it, this scope can almost certainly do it. Oh, I'll try the jitter wizard here. Worked for us before with the eye diagram. So, let's select measurement. I've selected the data rate. So, data

**Dave Jones:** rate fully automatic channel one. Yeah. Let's go in here. Thresholds individual sources channel one. Yeah. Whatever. Plots a histogram of all data rate measurements. Yeah, this is what we need. Turn on measurement histogram. You bet. It's not automatically showing up.

**Dave Jones:** Yeah. Jitter spectra turn on the jitter spectrum. You bet. Finish. Hey, there we go. There we go. That's a histogram of our data rate. Now, where's the scale for that? Measurement histogram. Data rate. Uh There we go. We're actually at standard

**Dave Jones:** deviation. We're uh sorry, our mean is 7.4 gigabits per second. What's going on there? Uh There it is. Mode uh 5 gigabits per second mode minimum maximum. Hey, I don't know what's going on there.

**Dave Jones:** But uh there you go. We can actually get up uh measurements. There we go. Data rate. Oh, yeah. Well, it is actually telling us that we are at 7 gigabits per second. Uh definitely has to be something wrong there cuz it's showing

**Dave Jones:** our minimum is 3.7, our max is 12.8 gigabits. There's something something screwy really going on there. So, I don't know. I'm not going to spend time mucking around trying to get that sucker working, but you see that it can

**Dave Jones:** do neat stuff like that and much, much more as well, I'm sure. Well, as for this serial decode thing, I relented and I called up the help for USB 3.0 and it says, you know, I show decode. I presume this scope does not

**Dave Jones:** have the USB 3.0 serial you know, it says it requires the USB 3.0 software. So, I can only presume because it's grayed out, these things were all grayed out. It didn't um it hasn't got the software option built

**Dave Jones:** in for that. Bummer. I'm sure that costs thousands of dollars when the scope costs $140,000. So, no doubt you've got to pay for all these individual software options. So, yeah, I think it's just it's just not going to let us

**Dave Jones:** do that. There's no auto setup, no nothing. Um So, looks like it doesn't it doesn't have it. Show decode, can't do it. What? What I've called up here is one of the demos where for the real-time eye with

**Dave Jones:** mask testing and it's put if I can close this stupid screen. There you go. It's it's showed us a really clean eye. Check out that. I mean, you know, check out the amount of black pupil in there for want of a better term, you

**Dave Jones:** know, it is you know, that is a really clean differential signal. That's a beautiful eye diagram. That's just, you know, if you see that sort of stuff on your if you see that sort of waveform on your system, you know, you're you're really

**Dave Jones:** sitting sweet. You laid out your board properly. You got all your controlled impedance traces correctly, all your terminations right, you know, all your shieldings right, you've got low clock jitter because, you know, look at the you know, the the width in there is just

**Dave Jones:** ah, it's just beautiful. So, this is a demo. Um if you probe the thing properly and design your system properly, you might, you know, you might never achieve that in your system. You know, it's all about meeting the specs and the uh tolerances and what

**Dave Jones:** is actually achievable in a practical system. But that I don't know if I can do anything else with that demo. I think it just displays um it was just a demo file really and it allowed me to uh

**Dave Jones:** uh maybe I can do Here we go, USB 3 serial decode. Maybe this is what it would have looked like um if we were actually able to do that. Yeah, there we go. This is This is what we would have got if we had

**Dave Jones:** um were able to get that serial decode option working. There's the USB uh packets, the time, and all sorts of stuff. And you can analyze that until the cows come home. Good stuff. More neat stuff this can do is uh FPGA

**Dave Jones:** dynamic probing. And uh this is the demo of it and if you insert a uh core, a specific core in the FPGA and you probe it, um then you can get all sorts of stuff. It helps us set up your scope and

**Dave Jones:** get real-time analysis of what's happening inside your FPGA. Neat. Sure it costs a fortune, of course. So, there you go. I hope you found this rather interesting. If you want to check out more, um go search for, you know,

**Dave Jones:** Google uh eye diagram uh measurements and stuff like that. I'm sure there's 10 million app notes and uh things out there which will um explain just what a valuable tool this is for um doing signal integrity measurements on

**Dave Jones:** differential um high-speed serial lines like this and um pretty much in all you know these high end scopes. This is one of the main things that they are capable of doing is measuring and analyzing and you know extracting the clock from the

**Dave Jones:** signal and displaying an eye diagram which is essentially the data waveform overlaid again and again and again on the recovered clock which it controls the horizontal axis is the recovered clock from the signal itself and from that you can tell

**Dave Jones:** an awful lot about the signal. But it was just good fun having to play around with this and see what the scope is capable of. I really rather like it. It's been fun and if you get a chance to play with one of these

**Dave Jones:** high end scopes by all means um play around with the eye diagram stuff because it can be a great deal of fun and you can learn a lot about signal integrity. You know if I could I could you know probe this in different ways

**Dave Jones:** and stuff like that and see how the signal integrity changes but haven't got the time. So if you want to discuss this jump on over to the EEVblog forum. The link is below the video there or above if you're on the blog website. And

**Dave Jones:** remember if you like it please give it a big thumbs up. Catch you next time.
