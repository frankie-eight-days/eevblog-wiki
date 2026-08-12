---
video_id: qXGqDDE9-4M
title: EEVblog #565 - Tektronix TDS3054 Oscilloscope Repair - Part 2
url: https://www.youtube.com/watch?v=qXGqDDE9-4M
source: youtube-asr
timestamps: {"0": 1, "1": 16, "2": 28, "3": 41, "4": 60, "5": 76, "6": 89, "7": 101, "8": 117, "9": 130, "10": 144, "11": 155, "12": 167, "13": 181, "14": 194, "15": 209, "16": 225, "17": 237, "18": 251, "19": 268, "20": 282, "21": 296, "22": 316, "23": 333, "24": 356, "25": 376, "26": 390, "27": 404, "28": 418, "29": 432, "30": 444, "31": 458, "32": 472, "33": 483, "34": 495, "35": 514, "36": 530, "37": 541, "38": 557, "39": 576, "40": 591, "41": 603, "42": 624, "43": 640, "44": 659, "45": 671, "46": 686, "47": 698, "48": 711, "49": 729, "50": 742, "51": 756, "52": 771, "53": 783, "54": 794, "55": 811, "56": 828, "57": 844, "58": 855, "59": 873, "60": 888, "61": 903, "62": 919, "63": 932, "64": 944, "65": 957, "66": 970, "67": 985, "68": 1001, "69": 1015, "70": 1028, "71": 1045, "72": 1070, "73": 1085, "74": 1098, "75": 1115, "76": 1130, "77": 1145, "78": 1165, "79": 1185, "80": 1200, "81": 1213, "82": 1231, "83": 1246, "84": 1257, "85": 1275, "86": 1289, "87": 1305, "88": 1321, "89": 1340, "90": 1361, "91": 1387, "92": 1401, "93": 1413, "94": 1427, "95": 1442, "96": 1455, "97": 1469, "98": 1485, "99": 1503, "100": 1522, "101": 1536, "102": 1549, "103": 1563, "104": 1579, "105": 1596, "106": 1607, "107": 1618, "108": 1639, "109": 1655, "110": 1676, "111": 1689, "112": 1702, "113": 1714, "114": 1727, "115": 1743, "116": 1758, "117": 1773, "118": 1785, "119": 1800, "120": 1816, "121": 1828, "122": 1855, "123": 1881, "124": 1899, "125": 1916, "126": 1928, "127": 1948, "128": 1960, "129": 1975, "130": 1988, "131": 2002, "132": 2015, "133": 2031, "134": 2045}
---

**Dave Jones:** Hi. Yes, it's New Year's Day and yes, I'm at work. Go figure. Anyway, I thought I'd do a quick follow-up. I have some more play around with this Tektronix TDS 3054 oscilloscope. If you haven't seen the previous video, I'll link it in down

**Dave Jones:** below. Didn't really have any time to troubleshoot it properly last time. It was just a teardown to see if there was anything obvious there at all and have a poke around under the microscope. There was nothing obvious, of course. We've

**Dave Jones:** got a faulty channel three here and we're not sure if it's in the hybrid or whether or not it's in the ADC or whether or not it's in part of the sample memory or something like that, but I asked for comments on the forum

**Dave Jones:** and sure enough, I got them and it turns out somebody had Well, Vincent actually, free electron on the forum, had the info that the hybrid amplifier chip in here actually has a high-frequency and a low-frequency differential driver output. So, it

**Dave Jones:** splits the signal into a high-frequency and low-frequency component and there's two line differential pairs which go over to the ADC there. So, and that might kind of explain it cuz it looked like the low-frequency content worked, but the high-frequency content

**Dave Jones:** didn't. So, possibly there could be something there. So, I'll have another look at the that under the microscope to see what's going on there. A few people asked, "Well, what's the next step?" Of course. Well, the next step

**Dave Jones:** I'll try and find some power supply rails that are common between these things because we've got different channels. Then it's good cuz we've got something to compare it with. So, maybe I'll try and find some power rails in there,

**Dave Jones:** measure those, make sure they're okay. But as I said, you know, look that it's the ADC there is digitizing that low-frequency component. So, you know, I'd be a bit surprised if there was any issue with the uh supply there maybe,

**Dave Jones:** but hey, you never know. And uh so we'll check that out. Uh we'll also probe The next step would be to probe the differential output of the uh channel here, and cuz as I said, we've got another channel, we can compare feed the

**Dave Jones:** same signal into a working channel and the faulty channel here, and we can check to see what the differential output there is on both that high frequency and the low frequency um pair on there. So, we can actually uh do

**Dave Jones:** some uh simple measurements, quick measurements, and uh check that out, and that'll tell us if there's anything wrong with this hybrid at all, cuz it'd be really nice to completely eliminate this hybrid module. And, you know, is it

**Dave Jones:** in here or is it up in the more conventional circuitry up in here? That'd be real nice to know. So, let's get to it. So, let's check this hybrid module again and see where these diff pairs come out. As I mentioned

**Dave Jones:** previously, obviously, these two pins here coming out of the hybrid are one of the differential pairs. We've got some capacitors there. We've got some resistors, by the looks of it, uh laser-trim resistors there. And these two pins are your differential pair

**Dave Jones:** output. And if you can see down in there, sorry, it's not going to Yeah, it hasn't focused on that, but you can see the differential pair winding its way out there like that. And they're nice thick traces, so you know know that's a

**Dave Jones:** controlled There's a ground plane under there, you know that's a controlled impedance pair running to the ADC chip over here. And if you have a look at these two over here, right next to it, well, they're also running as a

**Dave Jones:** differential pair down in there, but thinner. Well, that makes sense. That means that this one over here with the thicker traces is probably the high-frequency one, would be my guess, and this pair over here is the uh low-frequency pair, if um

**Dave Jones:** Vincent has got that right, and they do split the signal out and go over to the ADC like that. So, there you go. Um, so, one of the first things I I'm probably going to do because we can get the

**Dave Jones:** probes down on there. I might just do get the meter out, multimeter, and just do some resistance measurements and compare between the two modules. Actually, this is channel three here that we're looking at and you can see the same we're looking at channel two

**Dave Jones:** before. So, these are the high frequency pins there and then you've got your two low frequency pins coming out there and going over to the ADC over there. So, that's definitely a differential pair. So, I'm going to assume I can't see sort of any other

**Dave Jones:** ones sort of nearby. So, I'm going to assume, you know, you would think that they would be like right next to each other on the hybrid chip chip. So, that's definitely the best guess. So, in-circuit resistance measurements are actually can be quite handy if

**Dave Jones:** you've got like an AB comparison here. So, let like what I want to check is the capacitors are making contact down to the hybrid down in there. And the way I can do that is I can contact the top of the

**Dave Jones:** capacitor up there. This is the good channel. There you go, 21.8 ohms on one cap. This is on presumably that that high frequency pair. 21.8, the same. So, let's go over here. Make sure they're the same. Yep. And

**Dave Jones:** drat. I was hoping it'd be that easy, you know, I'd be able to find something, but no. That's fine on that pair there. Now, I can actually test the other pair. Let's just uh put the pins across there. 0.785

**Dave Jones:** meg. Okay, swap them. Not measuring anything low impedance there. 0.787. Okay, but anyway, the actual values don't matter because you can just probe around. Ah, there you go. There you go. That's That's slightly different. Let's measure a third channel over here.

**Dave Jones:** Uh there you go. Hey, hello. Let's go over to channel four over here. Did I get the right pins on channel three? Hang on. Hang on. Ah no, there we go. Okay, so channel four is no. All right.

**Dave Jones:** No, that's a bit of a furphy. Okay. No, we're chasing a red herring there. All right. Now I'm feeding in a 1 kHz 1 V peak-to-peak sine wave into both channels and you can see channel three there that high frequency content is

**Dave Jones:** just awful. The blue one there is channel two. So that's working just fine. And as I said, the amplitude is just fine and the low frequency waveform performance of channel three there is just fine. It's just got all this high

**Dave Jones:** frequency crap on it. So you know, that's that's really interesting in what Vincent said with those separate pairs with the high frequency and the low frequency content. So anyway, let's have a probe around. Now of course, when you're working on

**Dave Jones:** stuff like this, you have to be very careful. I've got the main section completely you know, separate over there like that, which is really good. The low voltage cabling comes over quite nicely to the main board. And so I can actually

**Dave Jones:** probe around this while I'm still feeding in the signals to the front panel here. So access is actually really quite good. But anyway, just want to keep away from that main stuff over there. And also there's a high frequency

**Dave Jones:** backlight high voltage backlight inverter here as well. And it's got a little caution on there. Want to stay away from that. Now to probe this what we can do, we can just use a single probe and do it single ended. That's

**Dave Jones:** just going to work fine for this uh signal probe each side independently, but we'll use uh two probes and we'll uh do a poor man's uh differential probe. So, we'll we'll subtract one signal from the other, but in this case, it's it's,

**Dave Jones:** you know, it's probably not going to make a huge difference. I'm going to connect the uh ground through to the common uh ground on here, otherwise we're going to pick up uh too much noise. I'll probably uh show you the

**Dave Jones:** effects of that in a minute. And um yeah, we've got uh both channels one and channel two set up. The math operation is channel A minus channel B. So, let's have a probe at this thing and see what

**Dave Jones:** we get. Right, I'm going to have a look at channel two, which is the good channel. And I'm looking at the high frequency output. And bingo, that's the differential pair there. And you can see clearly see the two uh

**Dave Jones:** signals, the uh blue one and the yellow one there, and the purple one is the math. This um Rigol scope isn't the fastest on this uh math operation. It's nothing like a real good analog scope with its uh subtraction mode, that's for

**Dave Jones:** sure. Um it's a bit slow as a wet week, really, on that math function. But anyway, we can see our 1 kHz, and you can see that the signal, sorry, I can't push the uh stop button and capture that

**Dave Jones:** um using both hands here, but um yeah, we're getting our 1 kHz signal, and we can see the differential signal there, which isn't really helping us a huge amount. Now, as I said, let's disconnect these ground wires here. In fact, we'll uh

**Dave Jones:** take them off like that, and let's probe that again. And uh here we go, and you'll see uh our Look at that. Noisy as. That is an awful waveform. So, you really need to connect your grounds in there to uh

**Dave Jones:** uh get your um noise down on that. And there we go. I've run some averaging on that and you can see it's bang on 1 kHz. Getting nice beautiful waveforms out of the high frequency part of channel two there. So that's our

**Dave Jones:** good channel. All right. Now let's take a look at channel two here. I've got averaging on so that's what cleans up the waveform but doesn't allow us to really to do proper real-time probing but there's the low frequency output.

**Dave Jones:** And that is just fine. Let me switch that averaging off there. That's a bit annoying. Okay, so this is channel two. What we'll call the low frequency output. Okay. Fine. And this is channel two. What we'll call the high frequency

**Dave Jones:** output and that's just fine as well. We're getting the same signal on both of those differential pairs. Now let's go over to the faulty channel. This is the low frequency pin. That's just fine. There's our 1 kHz signal. Not

**Dave Jones:** a problem at all and there's our high frequency pin. Not a problem at all. So bingo, we've just narrowed it down to something being wrong outside of this hybrid module. It is not that hybrid module there at all. At least not in

**Dave Jones:** this instance for this test signal and really it should be the same case for every you know, every test signal really. There's nothing wrong with that hybrid module at all. We can completely eliminate that. I was going to suggest

**Dave Jones:** you know, if that was an issue the next step in there might be to you know, get the freezer can in there or something on that chip and freeze it down. See if you know, is a thermal you know, a like a joint issue or

**Dave Jones:** something like that. A bond like a you know, what is that? Like a little BGA device or something soldered down to that ceramic hybrid module or something like that. Could be a bad joint under there, something like that, which would

**Dave Jones:** ordinarily show up with some of thermal cycling. So, you might get the freezer spray on there or something like that. So, but anyway, we don't have to do that because it is not an issue in there. We're getting exactly the same. This is

**Dave Jones:** the advantage of having a working channel side by side. You can just probe both and we know it's not that hybrid module. So, it's something in here. So, next thing is the touch test. Yo, that's pretty hot. That's pretty hot, too.

**Dave Jones:** And so, all of those ADCs are getting pretty darn hot. In fact, I might get the thermal camera out for this. I've got my new FLIR infrared camera, which I haven't showed yet. And woah, check this out. This is the

**Dave Jones:** new FLIR E-series. This is the E8. This is the top-of-the-range E8. So, thank you very much, FLIR, for sending this in. It's going to be a permanent fixture here in the lab. They've donated this to the lab here so that we can use it for

**Dave Jones:** specifically stuff like this. And um yeah, I will be doing a full review of it in the Well, it is a new year now, isn't it? But, yeah, go figure. Now, I can actually capture video from this FLIR camera via the USB port, but please

**Dave Jones:** forgive me. I couldn't be bothered dragging the notebook over and you know, hooking it up and and doing that sort of stuff. So, you'll have to be content with just viewing the screen here, unfortunately. But, yeah, it still gives

**Dave Jones:** us a very good result here. And you can see the span where we're going from 22° sort of, you know, on the bench. This is the temperature scale. It's automatically adjusted this up to 96. So, you can see that the hottest

**Dave Jones:** objects, which are obviously that main chip, the die inside that main chip. There we go, 101. Well, you know, 90. It's basically 100° there on that main ASIC chip. Here comes my finger, there it is. That main ASIC chip down there

**Dave Jones:** and you can see that the the 480 C's, one there, one there, one there and there. And you can see the hybrid um chips up there, those hybrid ASICs. And which is you know, a differential amplifier and stuff. And then there's

**Dave Jones:** that mysterious sort of you know, fourth fifth bridging chip in there. That one's also pretty darn hot running at 90°. Anyway, the ADC's there are running at about 80, but the thing I want to check is that they're all running at about the

**Dave Jones:** same temperature. And you can pretty much see that there in the color gradient. I mean, I'm not going to dick around with getting the exact, you know, pointer on that. And the interesting thing about this, watch this, is if if I

**Dave Jones:** go closer, you'll notice that the hot spot offsets won't will be off on the chip because this is the parallax error due to the inbuilt camera. And also, please forgive me, I don't have a tripod for this thing either. Now, I've

**Dave Jones:** got my pointer in here and you can see that it's this is a really awesome camera because it has this MSX technology which overlays a real image of the board like that over the thermal image and it's really the resolution is

**Dave Jones:** really fantastic. I can read serial numbers of chips and everything. But anyway, you can see as it gets close here, there's parallax error, you can see that the closer I get I'm moving the camera towards the thing, then see that hot spot there that my

**Dave Jones:** pointer is pointing at should be in the center of that chip, but it's not. So, that's the parallax error due to the camera and the thermal sensor because ta-da, the camera is up here and the thermal sensor is down in here. So,

**Dave Jones:** there's a you know, you're going to get a parallax error, and there is a software option in here to actually um set that when you're up close. And you can see that we're already at our closest alignment distance there of 0.3.

**Dave Jones:** So, yeah. Anyway, um this is This is a really neat camera, and uh I will have to do a full review of this, but you can change the image mode. The user interface is a bit annoying. See, here's

**Dave Jones:** the difference between the MSX mode, which overlays the camera. Look, you can read all the serial numbers on there. It's just beautiful. And as opposed to just normal thermal image mode like that, which is, you know, pretty boring,

**Dave Jones:** even though this thing has 320 by uh 200 resolution on the damn thing. So, the resolution on the thermal is awesome. Or you can just do picture in picture like that. And or you can take out digital photos and things like that. Anyway, um

**Dave Jones:** yeah, this is not a review. I'm just playing around, but as you can see there, the uh as we get further away, that hotspot will line up properly with the center of the chip. There we go. It's getting much

**Dave Jones:** closer, so you can see that they're lined up in there. But anyway, um enough mucking around with my new toy here. Um that tells me that, you know, that ADC chip there isn't on channel 3, isn't um you know, faulty or anything

**Dave Jones:** like that. It's not heating up, so no real thermal issues there. That's interesting. Input termination overheat message. Hmm. Maybe because uh yeah, the fan is not on, and we're getting no cooling in this thing. Oops. All right. So, what I've

**Dave Jones:** started to do here is just have a probe around at some of the voltages. I won't uh show that up close. You have seen in the previous video, but there's a couple of like SOT-23s under there, and I've been probing

**Dave Jones:** around at those SOT-23s between the channels, and I found something rather interesting. There's a three-pin Hang on. Let's uh I put my probe on there on the shield for ground and I probe all three Ah jeez, that's hot.

**Dave Jones:** Damn it. Probe all three pins of this SOT23 and there's -2.576 -2.576 and 2.576. So, we've got 2.576 on all three pins of that SOT23 down in there. Whatever that device does, it's got the same voltage on all

**Dave Jones:** the pins. And I've checked the other SOT23s on the other channel here and they've got various voltages on them. One is 2.5 -2.576, but other ones have got, you know, 3.3 and other voltages on there. So, that is rather interesting.

**Dave Jones:** So, what I'll do is I'll um turn the power off and I'll measure the resistance of that and uh see if things are shorted. Um just be careful when you're probing around here, by the way, cuz I was using uh as I said before,

**Dave Jones:** this is ground, this uh metal shield around here. So, if you're accidentally probing and accidentally touch things, you can short stuff out, but the power's off at the moment cuz I'm measuring resistance. And uh these two pins on that SOT23, look at that, completely

**Dave Jones:** shorted. Huh, I don't measure that on that same, presumably the same top SOT23. I'm going to assume that all four channels are identical. There's a like a different layout in terms of where they're placed on each channel on the

**Dave Jones:** board, but there seems to be, you know, the same sort of components on each channel. So, the the two pins on that SOT23, the third one over here is not really anything. There's like, you know, a K between there or something like

**Dave Jones:** that. But if I go over to one of the channels over here, for example, this one and measure that sot 23 that sot 23 the pins. There you go. It's like 55k and I can do that on these other channels over here.

**Dave Jones:** And look, there it is 54k and I think the well, it's for completeness. Let's measure this channel over channel one over here. Uh, 2.5k. Yeah, I don't know. Anyway, still right, it's not a dead short. So, whatever that little beastie

**Dave Jones:** there is, the bloody thing I think is shorted out and that could certainly explain what's happening here. I'll try the thermal camera again and try and get a close up of that uh little sot 23. No, I can't really see anything obvious.

**Dave Jones:** It'd be like up under there. It's like there but on the uh thermal imaging camera it'd be you know, it'd show up as a as a hot spot if there was significant current flowing through there but that sucker

**Dave Jones:** is is short. I I really suspect it. I mean, you know, I could be wrong, right? But, you know, it just it just doesn't doesn't feel right. Aha, there's the little culprit that I suspect and under the Mantis microscope because it's got

**Dave Jones:** uh better optics and you know, and the 3D effect, it looks like there is a split in the top of the case on that little tiny split. I'm not sure how this is going to show up in HD on my

**Dave Jones:** camcorder camera here. Um, it's not showing up. I'm viewing this through my macro lens on the camcorder. I was hoping that it would uh do it but no, I'm at full zoom here and that's the best I can get. Let's see if

**Dave Jones:** I can film this under the Mantis. And there we go. You can see the top of that. So, this is really hard to get in focus, but look. Look at that just on the seven there. There is a looks like a big split

**Dave Jones:** right in the center of that sot23. That for all the world looks like a blowout hole. That I think the magic smoke has escaped from that thing. I have no idea what it is. It's just got 27 marked on

**Dave Jones:** it, but those two pins on the left there, of course, are shorted and the other devices which are also marked at 27 in the circuit, those ones aren't a dead short. So, magic smoke every time. The active ingredient in every

**Dave Jones:** component. If it escapes, they don't work anymore. I completely forgot that I had these real sexy tiny Pomona test leads someone sent into the mailbag. These are perfect for really tight quarters probing on boards like this. I'm going to get back in there with

**Dave Jones:** these. Oh, I just love them. They're so Look at needle point sharp. Oh, beautiful. So, I'm back probing around on here. And yeah, the other sot23s on the other channels, they're measuring plus 3.3 V presumably 3.3 V rail, and then plus 2.5

**Dave Jones:** V, but the blowing sot23 in here is measuring minus 2.5 V on its pins. So, yeah, that is just That is rather curious. See, there's 3.3 on one of the pins of uh one of the sot23s, one of the good ones.

**Dave Jones:** And there's, you know, 2.44 and 2.457, whereas our faulty one with the magic smoke that's escaped, presumably, minus 2.57 and minus 2.5 and well, minus 2.5 on all the pins. So, yep, something ain't right. So, it's marked uh 27 on the top of it.

**Dave Jones:** And these bloody cryptic SOT23 things, I don't do, you know, I'm not in the repair trade. If you're doing this all the time, you might sort of, you know, have an inkling what uh that could be. Is it a little uh three-pin SOT23 uh

**Dave Jones:** voltage regulator? I don't know, could be cuz the others have a 3.3 V input and then um 2 and 1/2 outputs. So, it could certainly be a 2.5 V regulator. That doesn't explain why there's not 3.3 V on

**Dave Jones:** one pin of that thing though. So, I don't know. Is it like a a dual diode or something like that? But, it is labeled It looks like CP, but uh I think it might be CR cuz the others are CR. It's

**Dave Jones:** labeled CR140 on the um silkscreen there. Now, of course, uh CR is a um standard designator. It means diode. So, possibly it's some sort of uh diode, you know, could be like a dual diode or a a single diode or something like that,

**Dave Jones:** like a BAV99 or um something equivalent like that. No, I checked and it's definitely CP140. It doesn't look like the R has been uh chopped off at like the, you know, the little leg of the R has been chopped off

**Dave Jones:** by one of the uh vias there. But, considering that an identical one on another channel is labeled CR, which indicates a diode, it has the same marking on the top, 27. Well, yeah, my best guess is that's a diode of some

**Dave Jones:** sort. Doh, silly me. I just realized that the two uh left-hand pins there on that SOT23 are actually uh shorted on the PCB. So, that's not inside the package. But, anyway, um that is definitely I reckon there's a blowhole

**Dave Jones:** in the top of that sucker. And yeah, I really suspecting something's wrong there. And a bit of Googling and I tracked it down to a possibly a Fairchild MM, uh BD 1204 cuz it shows 24 there, but 27 is used for

**Dave Jones:** the 1204, which is a ramp in arrangement, uh well, the 1204 pin arrangement, which is the common cathode small signal diode, just as I suspected. Bingo, that's got to be it. Now, I should probably also double-check the signals going to the ADC down here to

**Dave Jones:** make sure those differential signals are getting from that hybrid down to there as well. I mean, this diode I I reckon that diode is gone. I mean, I reckon, you know, it's blowing the ass out of that diode, but, you know, usually they

**Dave Jones:** they might only be in there for protection or something like that. So, you know, why it's blowing, well, let's ignore that for the minute, but the fact is, you know, that may not affect or conti- you know, affect its current

**Dave Jones:** operation. There could be something else um causing the issue, but anyway, I probably should double-check. Power it up again, feed in the signals, and just double-check that the signals are going there, but I'll have to use um you know, something like these uh

**Dave Jones:** probes because the regular um scope probes I just can't get in there in that tiny pin pitch, especially right next to that uh shield there and probe those pins. It's really quite annoying. Anyway, that diode there, is it

**Dave Jones:** a diode? There we go. But, let's check it the other direction. And yeah, it's exactly the same, so eh, it's in circuit. What do you do? Actually, instead of probing those, it really, you know, cuz there's nothing going to be wrong with the PCB traces

**Dave Jones:** from there to, you know, the 1 cm it takes to get from the hybrid module to the ADC. So, you know, if there was anything wrong, it'd be the solder joints on the chip. So, I just reflowed those. So, I just used uh just dabbed my

**Dave Jones:** flux pen on there and just, you know, got down on and just reflowed the joints down in there. and well, let's power it back up. See if it made a difference. I doubt it, but hey, it's worth a shot.

**Dave Jones:** And of course, no, I'm never that lucky. Bummer. And well, I went the whole hog and I lifted that one pin on that faulty diode there and no, makes no difference whatsoever. So, uh goodness. Let's have a look at that diode there

**Dave Jones:** that I've I've lifted the pin up on so we can actually access the pin. There we go. It's still acting as a diode. There we go, 0.55. Sounds a bit right. Haven't checked the data sheet, but that does sound right.

**Dave Jones:** Other direction? Oh, hello. Hello. I'm making correct contact there. Yes, I am. There you go. Ooh. Yeah, that thing is yep, that's it. There's something wrong with that diode. Yeah, that doesn't work well at all. What I'm going to do now is just apply

**Dave Jones:** power to the bare board here so I can access the backside cuz so we shouldn't need any of the uh you know, the screen and keyboard and stuff hooked up for this sort of thing. So, I can access possibly some uh you

**Dave Jones:** know, power stuff on the bottom. I mean, you know, we've got lots of bypass caps here. I'd like to test uh the voltage rails. Here's the third channel, you know, 1 2 3 4. Uh there's some ferrite uh beads in there for those channels.

**Dave Jones:** I've already tested those. Those are uh fine. They're not open or anything like that. I'm not sure if like, you know, there's one of those per channel or something like that. But anyway, all the bypass caps there are on the bottom. I

**Dave Jones:** can maybe check some uh supply rails for that uh third channel there. So, because you know, like there's nothing on the top and there's no uh test points, you know, it'd be nice if there was, you know, here's a 2.5 V

**Dave Jones:** rail. Here's the 3.3 V rail. Please test it. But nah. And the good thing about these extra channels again, as you can see, is that I'll put my probe on the ground over here, and I can probe these caps, and you can see we got

**Dave Jones:** -2.5 V there on that cap. Sorry, you can't see it. And then +2.5 V on that channel. So, it looks like the ADC is operating plus minus 2.5, at least on those caps. Um so, there's some rail. And look, this

**Dave Jones:** is the folded channel, this is channel three, -2.5, +2.5, they're all probably running from the same regulator. I don't know if they have local regulation or not, they could do, that's what one of those little sub-23s. -2 +2.5,

**Dave Jones:** -2.5. So, and all the other channels, there you go, they're doing exactly the same thing, and the layout is duplicated across the channels. The PCB layout designer, of course, is not going to make their life hard, so they're going

**Dave Jones:** to duplicate the layout on all of them. So, you know, you can easily compare channels. So, this is our folded channel three, and those two caps there are just hunky-dory. In the 3.3-V rail on the main processor over

**Dave Jones:** here, powering all the you know, the heavy-duty digital stuff, that's all just fine as well. I can't find any other voltages on these ADC channels. It looks like it's just operating from plus minus 2.5 V. So, yeah, all look, the voltage rails are

**Dave Jones:** fine. I don't know. I'm starting to give up again. And one thing left to try is the old freezer spray. I don't have any freezer spray at the moment, going to use the air air duster, just turn it

**Dave Jones:** upside down, instant freezer spray. Brilliant. So, I'm going to spray that third channel ADC, and uh anything? I can't watch and spray at the same time. No. Let's try that center chip. No. Memory. No.

**Dave Jones:** No. No big ASIC chip. Nothing. Not a sausage. No hybrid. Just in case. No, hybrid's fine. Let's really go to town on that. Oh, there we go. Look, we got an offset. Hello. Ooh. Ooh. Ooh. Look at that.

**Dave Jones:** Look at that. Wow, drifted back. I mean, you'd expect that, but it's not like it's suddenly vanished or anything. Let's see if I can isolate that.

**Dave Jones:** All right. I'm just doing the little chips around it. And Well, let's see if I can get an offset on channel two, the blue one.

**Dave Jones:** Oh, yeah. Look. Look at that. Look at that. It's coming back. Oh, that's beautiful. That is beautiful.

**Dave Jones:** That's fantastic. Look at channel two. It really It What? It hasn't recovered. Hasn't recovered. It's giving channel two another spray. Look at that. Woohoo! And so, yeah, it's not surprising that, of course, channel three. But we didn't see channel two do an

**Dave Jones:** offset. Channel three is giving us an offset. So, that's interesting. Um There we go.

**Dave Jones:** Anyway, that's I you know, I would expect that. It's not like it's changing the high frequency performance on there at all. So, yeah, I don't know. That's fun, but we haven't found anything. So, sorry, I think I'm going to call it quits for

**Dave Jones:** today on this one again. I've already spent an hour or something on it and well, you know, I've got some other things to do. And well, I think we've got some progress. I'm pretty sure I found a faulty diode in there, but well, it's

**Dave Jones:** not affecting the channel at all. I remove it from the circuit, the channel still does the business. I've reflowed the joints on that channel three there. I've checked the voltage rails. We've verified the signals coming out of the

**Dave Jones:** hybrid there. So, we're pretty confident it's not the hybrid module at fault. And well, I don't know. Is it one of the memories or something? But look, there's not like there's a memory per channel. So, they're clearly like

**Dave Jones:** I'm sharing those between the channels. Of course, the ADC's are 9-bits each. So, that's an oddball value. So, you know, you're probably going to share the memories anyway, but I like I don't know. Once again, I'll you know, open the

**Dave Jones:** comments if anyone's got any better ideas, but anyway, I hope you found that interesting that little troubleshooting procedure to at least I think find a faulty diode. That's at least progress. Something's magic smokes escaped from that. So, that's not bad, but

**Dave Jones:** unfortunately Murphy has conspired to ensure that we don't find the fault yet again. The EVBlog repair curse strikes again. This one will have to go on the working progress list. Catch you next time.
