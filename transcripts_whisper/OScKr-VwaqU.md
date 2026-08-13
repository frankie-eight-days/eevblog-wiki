---
video_id: OScKr-VwaqU
title: EEVblog #876 - NI VirtualBench Review
url: https://www.youtube.com/watch?v=OScKr-VwaqU
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 12, "2": 36, "3": 52, "4": 68, "5": 84, "6": 108, "7": 124, "8": 140, "9": 156, "10": 176, "11": 192, "12": 212, "13": 228, "14": 240, "15": 260, "16": 276, "17": 288, "18": 308, "19": 328, "20": 352, "21": 368, "22": 388, "23": 404, "24": 424, "25": 444, "26": 468, "27": 480, "28": 500, "29": 520, "30": 536, "31": 552, "32": 584, "33": 608, "34": 632, "35": 656, "36": 676, "37": 692, "38": 712, "39": 728, "40": 748, "41": 764, "42": 780, "43": 800, "44": 816, "45": 832, "46": 852, "47": 872, "48": 892, "49": 912, "50": 932, "51": 944, "52": 964, "53": 980, "54": 1000, "55": 1020, "56": 1044, "57": 1068, "58": 1088, "59": 1104, "60": 1124, "61": 1152, "62": 1176, "63": 1200, "64": 1224, "65": 1236, "66": 1256, "67": 1276, "68": 1292, "69": 1308, "70": 1324, "71": 1340, "72": 1356, "73": 1380, "74": 1404, "75": 1424, "76": 1444, "77": 1464, "78": 1484, "79": 1500, "80": 1524, "81": 1544, "82": 1556, "83": 1580, "84": 1604, "85": 1620, "86": 1644, "87": 1656, "88": 1676, "89": 1692, "90": 1716, "91": 1736, "92": 1760, "93": 1776, "94": 1796, "95": 1812, "96": 1836, "97": 1852, "98": 1872, "99": 1884, "100": 1904, "101": 1920, "102": 1936, "103": 1952, "104": 1972, "105": 1988, "106": 2008, "107": 2032, "108": 2048, "109": 2068, "110": 2084, "111": 2100, "112": 2116, "113": 2132, "114": 2156, "115": 2176, "116": 2200, "117": 2220, "118": 2236, "119": 2252, "120": 2268, "121": 2280, "122": 2300, "123": 2312, "124": 2328, "125": 2344, "126": 2356, "127": 2372, "128": 2392, "129": 2404, "130": 2420, "131": 2440, "132": 2456, "133": 2472, "134": 2496, "135": 2512, "136": 2536, "137": 2556, "138": 2572, "139": 2588, "140": 2612, "141": 2632, "142": 2656, "143": 2676, "144": 2692, "145": 2708, "146": 2724, "147": 2748, "148": 2768, "149": 2784, "150": 2804, "151": 2820, "152": 2836, "153": 2856, "154": 2872, "155": 2892, "156": 2908, "157": 2928, "158": 2948, "159": 2964, "160": 2980, "161": 2996, "162": 3012, "163": 3028, "164": 3048, "165": 3068, "166": 3088, "167": 3108, "168": 3124, "169": 3140}
---

**Dave Jones:** Hi! As promised, we're going to take a look at this national instrument's virtual bench. Have a play around with it. Now, I've done a teardown video of this thing and it's beautiful inside. Oh, you've got to check it out. So click here if you haven't seen that.

**Dave Jones:** Definitely watch that first. Now, this is a roughly US$6,000 instrument. It's a 4-channel, 350 MHz oscilloscope. That's why you're paying so much. You're paying for the bandwidth. The lower model one for this, about US$2,000, 2-channel only, 100 MHz. This is the top-of-the-line 350 MHz, 4-channel,

**Dave Jones:** arbitrary waveform generator, 14-bit, all the usual stuff. External trigger, of course, very nice to have the 4-channels plus the external trigger. 5.5-digit multimeter, should do all your regular stuff. 5.5 digits is, you know, pretty much all you want in this class of instrument.

**Dave Jones:** Got a nice DC power supply in it, plus minus 25 volts at 1 amp, so there's 50 watts and 6 volts, 3 amps up to. All digitally programmable, quite accurate. Everything else, I believe the specs on your digital multimeter are pretty good too.

**Dave Jones:** It's got 8 channels of digital I.O. here, and also it's a mixed-signal oscilloscope. So you get 16 digital channels for your logic analyzer as well. 1 MB sample memory per channel, which is not a lot in the scheme of things. So quite disappointed by that.

**Dave Jones:** And it's also somewhat disappointingly for a bench instrument like this, like a USB sort of like educational type tool, it's only an 8-bit regular 8-bit converter. Would have much preferred to see a higher resolution converter inside this thing. Even if you had to sacrifice bandwidth, would have been very nice to get like a 12-bit converter.

**Dave Jones:** You could do some nice DSP stuff combined with the function gen. You could do, you know, bode plotting and really, you know, decent stuff like that. So they haven't done that. It's just a regular 8-bit digital scope. It's the hardware in here, as we saw in the teardown,

**Dave Jones:** absolutely, you know, top-notch hardware in here. In fact, it's more capable than the specs that this thing's got. I don't believe it has intensity-graded display. We'll check out the software and things like that. So it's basically a complete lab in one box. You've got the mixed-signal

**Dave Jones:** scope, the function generator, the multimeter, the power supply, the digital I.O. you can play around with, and all tied into National Instruments software. I'm pretty sure the software will be pretty decent. But that's basically what we're going to test today. We're going to plug it in, have a play around with the software.

**Dave Jones:** So let's actually plug this sucker in. It is Wi-Fi. It's got Wi-Fi connection and also Ethernet and USB as well. So I'm not sure which one we'll use. It'll be a lucky dip. So let's plug it in. And... I don't know if you heard that, but that fan was pretty loud for a couple of seconds.

**Dave Jones:** And we've got a little light down there. Ooh, it's blue. Look at that. That fan noise, obviously it's a temperature-controlled fan, but that's the power button. It's got, I believe, it's got some extra LEDs across here for various status and things like that.

**Dave Jones:** But apart from that, it's pretty boring so far. And you get four of the probes with the four-channel unit. These are multi-contact brand. You get the regular easy hook. You get the BNC adapter. I always love the BNC adapter. You get the little high-frequency ground

**Dave Jones:** probe. And, well, what's the specs on these things? And these are fixed 10 to 1 probes. 500 MHz, so much better than the specs. So yeah, they're spared no expense. That's why the scope actually doesn't, well, the scope, the unit doesn't have x10 probe detection.

**Dave Jones:** It just assumes that you're going to use x10 probes with it, presumably, because that's what's supplied. So I hope you can change that in software so you can just feed coax and stuff straight in. And they actually look pretty decent. Look at that.

**Dave Jones:** They look fully insulated right around the top there. Very nice. Let's have a look at that. We've got our little high-frequency ground adapter there. That's very nice. I like that. Geez. Nicely formed. Brilliant. Better than the little dicky spring ones. And I love the BNC

**Dave Jones:** adapters. They're so handy. I use the damn things all the time. And you get a whole bunch of other stuff with it. I love the national instrument screwdriver. I've had plenty of these kicking around, because I've been to lots of national instruments training courses and seminars and stuff over the years.

**Dave Jones:** And they've been giving this away for, I don't know, 20 years now. And I've still got them, and they're just incredibly useful. And we have the Phoenix connector for the digital I.O. Very nice. We can get in there. That's why they supply the screwdriver.

**Dave Jones:** And it is the correct height. Look at that. Beautiful. And I'll tell you what, I'm enjoying the 16 channel logic analyzer probe. That's pretty spiffy. I don't like my chances of opening that. I assume it's got some MSO logic analyzer input cable. There it is.

**Dave Jones:** 25 volts max. I assume it's got some buffer circuitry in there to drive the differential, probably differential drivers to drive the line. And that is really nice quality. Where's my mini grabbers? I swear, I can't find the mini grabbers. So they've just given you those.

**Dave Jones:** What? Come on. And we've got some UL rated CalTest brand. I don't think I've heard of CalTest brand pros before. They're reasonably sharp, very nice silicone leads, very flexible, and they just, yeah, they feel real high quality. Hey! The fan is starting up.

**Dave Jones:** I'm not doing anything with it. It started up. I've got a pro plugged in. I've got it hooked into the function gen, but I haven't talked to them to set it up, and that's reasonably annoying that fan. Don't like it. There's a little whine in there, and

**Dave Jones:** it does sound quite whiny. Not impressed with that at all, and imagine if you had a classroom full of these things, like 20, 30 of them, it could get real annoying real quick. I'm not sure if you can hear that, but the fan is quite, like it's low enough, it just dropped down

**Dave Jones:** a little bit further. But it's whiny and rattly and it just feels really cheap. And I can't imagine what this thing's going to sound like when it's under like full load, that FPGA and that Kintex FPGA is going full pelt, and the fan's got to try and keep up.

**Dave Jones:** If you had a classroom full of these things, 20, 30 of them, it could get real annoying real quick. Ah, shame. Because otherwise the hardware is brilliant, but the fan? It's a bit of a fail. And we have ourselves a quick start guide, it's showing to connect it up to the USB port, I believe there's a drive

**Dave Jones:** in there with the software installer already installed for the PC, so that is very nice, we shouldn't have to download anything. That's beautiful. Assuming it works. By the way, this supports both PC, well only PC and iPad. There's no support at all for

**Dave Jones:** Android tablets, so... I don't have one of those bloody iPad thingies. Now that's attention to detail, check it out, they've actually got one of these lock-in jacks on the USB cable. Absolutely brilliant. And in a classroom environment, students throw these things all around, you don't want your bloody USB cable to come out.

**Dave Jones:** These can fall out quite easily, so that is a very nice touch. Thumbs up. Alright, here we go, let's give this a burl. I've got the USB cable, it's all the way on the bench over there, I've got to run it through like a 5 meter

**Dave Jones:** USB cable, so let's plug it in. This is not my main screen, it says, yep, installing device driver, blah blah blah. Here it is. And searching, searching. Anyway, it knows what it is, NI VirtualBench 8034 USB device. And it looks like you have files waiting

**Dave Jones:** to be... no, hang on. Files waiting to be burned to disk? Ooh, do I? No I don't. Well I'm young. Come on, well I'm young. Anyway, the best storage device is there, is it? Okay, it's taken a while, but we're getting there. Interface 1 of 3, 2 of 3,

**Dave Jones:** 3 of 4, sorry, and that'll be 4 of 4, and it's actually, it says it's like a CD drive. There it is. That is the actual drive that we got. And here's the software on it. Awesome! VirtualBench, and that's what it told us, run VirtualBench launcher.

**Dave Jones:** So here we go, we've installed everything. That worked hunky-dory, I like this. So you don't have to download anything, you don't have to put in a CD. Brilliant, here we go. Oh, run VirtualBench, there we go. It's going to pop up. Do you agree to allow

**Dave Jones:** periodically collect non-personal usage data? No! Piss off. No! Go away. Alright, here we go. Allow access. Oh! That's it! That's it! We're in like Flynn! Wow! I expected it to install software or whatever. That is brilliant! That is absolutely brilliant! Huge thumbs up to that.

**Dave Jones:** Wow! I've got the 1 kHz signal on the front, it hasn't triggered but, wow! That's terrific! Beautiful! Okay, the first thing I'm going to do is hit the dreaded auto button, auto setup. I just want to see if it stops, if it actually triggers on the 1 kHz

**Dave Jones:** signal. So, performing auto setup. Blah blah blah. Yep, there we go. Yep, we're in. Beautiful! And where's our time base? Oh, phosphor intensity. It does have variable intensity. Display! Brilliant! Okay, we'll test that later. But that's great. Okay, so here's our time per division.

**Dave Jones:** And yeah, okay, it's a USB scope, you know. Right. But I don't, like, first glance I don't particularly mind this. Here's the function generator over here. So that's like a level indicator for the function generator. That's the output voltage level. Wow, it can go to plus minus 12 volts.

**Dave Jones:** That's a big signal range. I wonder if it can do that into 50 ohms. That's interesting. And look, here is up here, I've got look, I don't mind that, how you highlight the you highlight the digit you want, and you go up and down

**Dave Jones:** Hey! Oh, I've seen a hell of a lot worse than that. Actually, I really like that. I really like that. Presumably you can just type in oh no, hang on. What if I delete everything? One. I can probably just type in one. Oh, look at that!

**Dave Jones:** One hertz, one kilohertz, one megahertz. Playing around with the function gen, haven't I? Forget the scope. It's just there, it's in your face, the function gen as well. But look, everything's here actually. This is the first time I've used it. So you've got the scope of course, which is

**Dave Jones:** this panel here. Can we move it? Can we acquisition? No, there's all your averages, peak detect, digital phosphor, there it is. It does support hence all the hardware that Kintex, that real kick-ass Kintex FPGA in there and everything else, that's what they're using it for.

**Dave Jones:** So it's got digital phosphor display. Very nice. Okay. Excellent. It's got peak detect mode. Seems to be really fast updating too. This is really quick updating. So I think they've got this right. They're probably only transferring on the USB, they can't transfer all the

**Dave Jones:** one meg worth of data, so that's not being continually transferred. I don't know how many times this is updating per second. You know, 15, 20 times a second or something, it kind of looks like. It's really quick and responsive. I really like that.

**Dave Jones:** That's great. But yeah, it's not, it can't dump the one meg of memory each time. So it's obviously, it's taking the one meg sample memory but then it's going to be just doing the display data and then streaming the display data to the

**Dave Jones:** PC via the USB portal, via Wi-Fi or Ethernet or whatever you happen to connect to. But when you stop it, when you stop it, that's the point where it would upload the one meg points of memory. So if we go like this, we go way out like that, and we just

**Dave Jones:** go auto mode. So let's go out like that, and we should be able to, let's have a look at that, let's stop that, okay, and it should give us the one meg capture, and we should be able to zoom in that and see, oh, there we go, well I

**Dave Jones:** don't know. You'd have to do the math on the time base to figure out that might be the limit of our one meg point memory. Does it say? How much memory it's used? Doesn't say. Is that a bit of a fail? I'd like to see how much,

**Dave Jones:** I assume it's using all the memory all the time, so I would have liked to have seen that actually displayed. Anyway, this is working great so far, I really like it. Anyway, so we've got all these panels, it looks like we can't drag the panels around and rearrange it, not that you'd

**Dave Jones:** really want to. What's in the file menu up here, you can import configurations, connect, configure network, blah blah blah, export screenshot, very nice, PNG, please, yes, thank you very much PNG. Awesome. Great stuff. Here's the digital I.O., look, we can just, can we just go down,

**Dave Jones:** oh, digital I.O. in the bottom corner down here. Why can't I just set all to, oh, set lines to output, okay, because I haven't actually turned them to outputs. There we go, and I can turn the output on or off. Oh, that colors, the green,

**Dave Jones:** okay, yeah, alright, that's fine. You know, just, like, don't use green, put one, so that everyone knows it's high, you know, like, yeah, but anyway, that's minor. MSO trigger, that's interesting, so you can actually, if you're using all of your 16 channels, you can

**Dave Jones:** use some of your external digital I.O. as the MSO trigger, and the function generator start as well. That is very flexible. That is very flexible, I like that. I like that, I'm impressed. Okay. And here we go, we can now set our voltage and our current limit.

**Dave Jones:** So this is our power supply, this is our 6 volts, like a bigger font please, like that tiny little 6 volt font there. Anyway, that's really quite nice, if we, so if we just highlight that and go, I want 5 volts please, thank you very much, Bob's your uncle.

**Dave Jones:** Very nice. And then your plus minus 25 volts here, you can actually turn the output off or on, there it is, now it's live reading. So this is your set voltage, your set current, and your read voltage and current, 1 millivolt resolution, 1 milliamp resolution.

**Dave Jones:** This is great, you're certainly getting your money's worth. This looks very nice, constant voltage mode, it'll tell you when it switches over into constant current mode if we just go short of the output and go into constant current. Here is our, we're on the 100 millivolt range, sorry, I'll just drag

**Dave Jones:** this over here like this, and we're now on our digital multimeter panel down here. Volts DC, volts AC, like the fonts are a bit small, I would have liked them to be larger than that, but anyway. And then continuity range and, nah, it's fixed.

**Dave Jones:** Okay. But yeah, we go down to 100 millivolt range, 1 microvolt resolution, everything's hunky-dory. I like this thing. I like it, they've done it really well, but that's what you'd expect. You'd expect national instruments to produce, you know, competent, you know, useful software.

**Dave Jones:** It's exactly what you expect. Alright, I've got the scope plugged into the function generator, let's check out the function gen itself. I've got it set to 1 volt peak-to-peak, and here's the signals we can choose. Sine, square, triangle, this is all very 1970s and DC level as well, but we can also

**Dave Jones:** choose arbitrary waveform, which is wonderful. But, if we go in here and browse, yeah, browse what? Browse the CD drive? Why does it keep moving? Like, it's looking for a text or a CSV file. Where are the files? Where are the built-in waveforms?

**Dave Jones:** Everyone once expects built-in waveforms to an arbitrary function generator, especially in an educational lab environment. That's a huge oversight, that's crazy! Why can't they provide that? Maybe they're in here, they wouldn't be in licensing, they wouldn't be in documentation, these are just different languages, right?

**Dave Jones:** I mean, come on! There's just nothing, there's nothing there. That's a huge huge fail. Massive fail. Well, let's go back to our sine wave, shall we? We've got our 1 MHz sine wave, but can we do anything else with it? Can we modulate it?

**Dave Jones:** No. We can change the DC offset, it looks like we can change the duty cycle of the, yeah, that's no worries at all, okay, great, but this is rudimentary functionality. I'm very disappointed by that. Especially for an educational tool of this price level.

**Dave Jones:** Nuts. And well, here we go, I've used an external function generator to do my standard 1 MHz carrier with 1 kHz AM modulation with 100% modulation, and triggering is very typical of most scopes, so that jittering is you know, that's fairly normal, don't worry about that at

**Dave Jones:** all. But what we're looking at is the intensity graded display, and it's there, you know, it's actually doing a half reasonable job. But yeah, that's okay. It gets a pass. But will it alias? That is the question. Let's have a squiz. No, it's doing pretty alright.

**Dave Jones:** Yep. Excellent. No aliasing on that. Many better scopes have failed that one. That's great. Thumbs up. And some of you might be thinking, Dave, what's up with the fuzziness of this line? Is this scope noisy? No, I've done a whole video on that, and that is

**Dave Jones:** very normal for a high bandwidth scope like this. High bandwidth scopes are inherently noisy, and high bandwidth and high update rate scopes are even noisier. Again, because they're actually capturing the real stuff that's there. Low end scopes appear less noisy, because they're just not fast enough to actually display it.

**Dave Jones:** So that's no problems whatsoever. Maybe if we can turn some averaging on, we might get that. So let's have a play around with the input here. Here we go, we can have our AC or DC coupling. There we go, we can do the times 1

**Dave Jones:** times 10 probe attenuation there. And if we do the 20 MHz bandwidth, maybe we'll see it clean up a bit. There we go. And also, because it's only an 8-bit sampling converter, 256 levels, I'm doing a 1920x1080 screen capture here, so obviously it's got to do some pixel doubling

**Dave Jones:** interpolation, all that sort of stuff. You can set the input impedance to 50 ohms. Excellent. Selectable. Nice. Now let's check out the triggering here on the menu. What have we got? Edge, pattern, pulse width, pretty basic. Nothing fancy-pansy there at all. You can trigger from any of the digital

**Dave Jones:** channels, all the digital I.O. channels, the trigger B and C, the line frequency or the function gen start, very nice. That's actually quite flexible in terms of sources. Rising, falling, either, you've got to have the either. And noise reject. There we go. That's pretty basic.

**Dave Jones:** It'll do all the things. This looks like, ta-da! We can pop out these panels. These are good. So you can just leave them anywhere. If you're using these all the time, they don't snap into place anywhere. But if you're using them all the time, just break out the panels and leave them there.

**Dave Jones:** Nice. And by the way, you can just move the waveform up and down, just grab it and drag it, or you can do the thing on the side there. There's no button to center it, but that's neither here nor there. And the trigger level, you can just set like that.

**Dave Jones:** I like it how it shows the level as you hold it and drag it. And if it's off the screen like this, it actually puts it right up there like that. So you can just drag it back down. So trigger and waveform movement works just

**Dave Jones:** hunky-dory. Now if we go up here, we've got our acquisition stuff. It's not immediately obvious, you know, I'd like to see like an acquisition button or something like that, but you know. Whatever. It's got peak detect mode, awesome. There we go. Hey, I expected a bit more noise on the peak detect mode there.

**Dave Jones:** What's going on? Anyway. Digital phosphor, okay. Acquisition, and here's our averaging. And there we go, we'll see it go to a nice thin line. Because it's averaging out the noise there. No wuckers. It doesn't have any high resolution mode at all. There's no high resolution mode.

**Dave Jones:** Why? I would have expected that on a scope like this. Or is that? Alright, that's sampling mode. Okay, so it's not real-time mode. It's equivalent time sampling. That's what's going on there. But that's really I expected more functionality for the money. I really

**Dave Jones:** did. Anyway, we've got, we can do persistence, no worries at all. So if we go off the trigger, yep, our persistence shows up. It resets the persistence when you move the trigger, like that. Okay. Some scopes can clear it, some scopes don't. Depends on your preference.

**Dave Jones:** And what else have we got? We've got clear display, and we've got pinout, which we've seen before. That's fine and dandy. But yeah, no high resolution mode. Quite disappointed. Yeah, no box car averaging on the thing. Thumbs down. Well let's go into more.

**Dave Jones:** We always want more. Let's check it out. Like, they've got tons of room here. Why does it have to be more? Look at all this unused room here. Why bother having more? Why not just put FFT there? And the reference wave, like math and FFT,

**Dave Jones:** why not just put them there? That's just dumb. I don't know. Yeah, they got 90% with the user interface and then gave up. Store from the analog channel, so we can actually store the data. We can capture, we can load from files. Okay, so what does it expect when we

**Dave Jones:** load that? It's expecting a VB reference file, so it's obviously some custom file. Some custom jobby. Anyway, the math functions, let's check out the math functions. Where are they? Where are they? Here we go. Here we go. Now, see, it showed up like, why not just keep the math there?

**Dave Jones:** I mean I don't get it. Alright, so if we go in there we can actually change it. There we go, plus, minus, multiply, divide, all the usual stuff. Nothing fancier than that. There's no integration. Once again, for a educational tool, especially one of this

**Dave Jones:** price point, I would have expected all of the math functions, like even the Rigol DS1054Z, right? 400 buck bench scope can do, you know, a ton more than this. That's just, nah, that is not good enough. That is not good enough. They need to

**Dave Jones:** work on their math. Yep, not happy with it. You've got to drag both at once. You can't drag one, oh yeah, you can drag one individually. Here we go. Yeah, there we go. So drag on the screen drags everything, that's kind of handy, and then if you want to drag one, it's over here.

**Dave Jones:** But too bad if it's behind it, you've got to drag that one first and then that one. Depends on which one you're focused on. Yeah, anyway. Alright. So math is barely what's there. That's about all I can give it. And our FFT is presumably, it's not done in hardware on the

**Dave Jones:** virtual bench, it's done in the software here. So let's we can break that panel out, actually. There we go. There we go. So let's move our FFT like that. Frequency per division. There we go. And we're going to be very coarse, actually, let's

**Dave Jones:** put the square wave in. There we go. It's very coarse, of course. The frequency resolution just isn't there, the binning resolution isn't there, because we've only got a couple of cycles on the screen. So that's absolutely useless. So let's go and fix that.

**Dave Jones:** And you'll notice that our resolution gets better and better and better. Let me there we go. There we go. Gets better and better and better. So I'll show you that getting worse now. Here we go. See? Until it's practically unusable. If you've only got a single cycle, that's a trap for young

**Dave Jones:** players. Students learn that very quickly. That's the advantage of, well, it's not just any scope you can do this on. You play off the time base. They think, oh, okay, I've got my square wave on the screen, let's see what the frequency components

**Dave Jones:** are. And then, wah, you get this ridiculous looking spectrum like this, which doesn't look anything like the lecturer said or what the textbook shows. And even this looks like, you know, some dick and balls. It's hopeless. Yeah, you've got to get more samples.

**Dave Jones:** Data. The algorithms don't work without data. Alright, they've got all the usual window culprits down here. Oh, regular and advanced. Oh, 7-term Blackman Harris for you Blackman Harris fanboys out there. Exact Blackman. Well, you don't want this 7-term rubbish, you want to be exact!

**Dave Jones:** Anyway, low side load. There you go, look at that. Where it's all hey, that's reasonable. The FFT functionality, you know, pretty basic. You know, we can do some vertical offset and stuff like that, but yeah, I mean, volts per division, 20, well, that's the

**Dave Jones:** other thing. Where's the scale? Where's the scale? Look, there should, where's the y vertical scale? That's just ridiculous. We need okay, it's over here, but if you didn't have that panel open, right? If you had this panel closed, oh no, there we go, 20 dB volts.

**Dave Jones:** Okay, I don't know, it would have been nice to scale it over here. Look at all that unused space on the screen there. It would have been nice. Anyway, cursors down here. Here we go, we can time, hang on, channel 1, ah, there we go, we can

**Dave Jones:** choose the FFT. Okay, it's going to change. Alright, there we go. It's a 1, but it doesn't, looks like you can't just skip to the peaks and things like that, there's no auto peak detection, it would have been nice if it detected all these frequency peaks and had a button down there

**Dave Jones:** that said enable peaks at some threshold value and auto detect peaks and things like that, but no, nothing. Once again, rudimentary scopes, rudimentary scope FFT functions have better functionality than this and they cost a lot less. So, you know, yeah, I think there's still

**Dave Jones:** I like the software, the software's quite good in terms of USB scopes I've seen, it's really quite good, but it's just, it's not good enough. I expect more, especially for the price. And if we go to the digital stuff down here, we can choose buses, we've got I2C,

**Dave Jones:** parallel and SPI, um, where is like RS-232? Where's serial? That's disappointing. Um, so yeah, there's our lines, so we can choose, what's that, enabled, okay so there we go, we're turning those on here, presumably we can drag, yeah we can drag those, it automatically rearranges, that's good.

**Dave Jones:** It's doing all the regular stuff. Our maximum sampling rate is one gig sample per second on the digital lines, and we can set our threshold voltage, it's all adjustable so it doesn't matter what logic family you're using, and that maximum digital buffer size

**Dave Jones:** one million transitions, there you go. So that's it. Um, so it must have sample compression, because it's doing uh, it enables you to select transitions instead of meg samples, it's got the sampling rate, and instead of setting a memory depth size, it's giving you

**Dave Jones:** you know, X number, 10,000 transitions, a million transitions, or whatever. So it's obviously doing sample compression, and that's very nice. I'm not sure, you'd have to check the spec sheet to know exactly how much sample memory it actually does have, but that's nice.

**Dave Jones:** It means that when you have a you have packets of data, that are spread, you know, by long period, long dead periods, you're not wasting all your sample memory taking all those dead periods, you only, it's only the transitions that are stored in memory, time stamped, and did it transition high, did it

**Dave Jones:** transition low, and then that makes more effective use of your memory. But you still need a lot of sample memory, um, you know the sampling compression like this is not magic. You've got to have a lot of memory to back it up, of course, because if one, if you've

**Dave Jones:** got 1,000 transitions in one packet, and you want to measure 10 packets and you've only got, you know, 1K of sample memory then it can only do 1,000 transitions, you're going to miss these other packets so, yeah. But I'm sure it does, I think it's got like

**Dave Jones:** megs or something worth of memory. And I just found a limitation with the bus trigger, and if we go into digital here, trying to set it up, like set up my SDA line, we can choose any one of the 16 digital channels, we can choose the digital IO

**Dave Jones:** but we can't choose the analog inputs, and that's what I was using. And here we go, check this out, I'll go in auto mode, here we go, we're now doing real-time I2C decoding, I've basically got the same signal, I've got data on channel 1 and clock on channel 2 here

**Dave Jones:** and same with D0 and D1 there, so they're actually back to front like that. So if we actually single-shot capture that, we should be able to oh, actually, sorry, I got that, got that back to front, there we go we should be able to capture that, like that, and if we zoom in

**Dave Jones:** we can see, oh that's not a good example, but single-shot capture that again, there we go, look at that, there we go, there's a whole I2C packet, very nice. Seems to have done the business, what's happening with that little, that pulse there? Oh, I don't know, I'm using a Tektronix

**Dave Jones:** demo board here, by the way, so I have no idea what signals it's actually generating, it may actually deliberately been putting in a false pulse there, perhaps. But that's the advantage of having your being able to view your waveform as well. So yeah, it's a bit disappointing that you can't actually

**Dave Jones:** trigger off the analog signal channels, because that's handy, to be able to view your signal to make sure your signal integrity is fine, but check out the rise time on that, that is poor as. But hey, we're getting data out of it, and it seems

**Dave Jones:** fairly quick, and it seems to be doing the business anyway. And we've just got some line termination probing type issues here, but no big deal. But it seems to be doing it. And I'm not sure if we can actually set the height on those digital channels, it'd be nice to actually expand those.

**Dave Jones:** I don't think you can. Like if you've only got two channels like this, actually expand the things. And the other thing that's a bit disappointing is I like the fact that they snap into place and then automatically move around. That's fine and dandy, but if you want to overlay that,

**Dave Jones:** now you can see that the digital and the analog are correlated there, okay? That's fine and dandy, but you can't leave it there. It just snaps back, and you'll notice that this is correlated down here as well. So that's obviously, you can see that pulse in here, that one

**Dave Jones:** that didn't go all the way up, but you saw anyway, it just didn't have the rise time actually. That's, yeah, that's what it is. We've just got a rise time issue on the I squared C lines, the pull-up resistor value is not high enough, so yeah, it's just not doing

**Dave Jones:** the business there. But anyway, it's still detecting that, because that will depend on our threshold value, which we can change. So let's actually give that a go. I just noticed that the threshold maximum digital threshold can only go to 2 volts. Huh? What the?

**Dave Jones:** And it hasn't got like an upper and lower threshold, so I don't know what's going on there. That's quite disappointing. Anyway, yeah, there we go. Did we get it? Yeah, we still got it. We still got it. And of course we can change that to

**Dave Jones:** binary there for you binary aficionados. None of that hex rubbish. But unfortunately, I can't see any way up here to trigger off the... like a pattern or anything like that. So there's nothing hardware. They've got all that hardware sitting in there. They've got that

**Dave Jones:** Zinc FPGA plus the Kintex FPGA. Huge beast, and they can't they haven't implemented I2C and SPI pattern triggering, for example. So it's quite limited. You've got to go in there and decode it, so you can't trigger on missing acknowledges and all that sort of jazz.

**Dave Jones:** So it's not really a protocol analyzer as such. So there we go. With the 1 meg sample memory we can capture the entire group of data here, and then we can zoom in. So that's okay. But that's standard on a deep-ish memory scope like this one with

**Dave Jones:** 1 meg. But yeah, you can't trigger, unfortunately, on anything. So you can't, you know, like a data word or something like that, which is very useful for debugging and things like that. But considering, I guess this is primarily targeted at the educational market, I think

**Dave Jones:** you know, it's okay. But still, yeah, it would have been nice to have that sort of stuff. So this is not a real tool for real world, you know, advanced troubleshooting and things like that. Certainly on I2C, you know, serial buses and the like.

**Dave Jones:** You can view them, you can capture them, but eh, the rest is up to you. And the other thing that I realized it's not here that I would have liked to see is some sort of automated, you know, programmable control over the digital I.O.

**Dave Jones:** down in the bottom corner here. But we can set them to inputs, set them to outputs, but we can't sequence them. You know, you can't like put a counter on there, for example. You know, basic sort of, you know, educational training stuff like that.

**Dave Jones:** You just can't do it. So like, yeah, that would have been nice. But granted, all this National Instruments hardware is fully configurable with either LabVIEW or LabWindows CVI, which is what I've used in the past for doing lots of National Instruments-based test systems.

**Dave Jones:** The LabWindows CVI stuff is quite nice. And you can, you know, they've got the libraries for all this, and I'm sure I have absolutely no doubt whatsoever, even though I'm not going to test it today. It requires too much time and effort. But

**Dave Jones:** you can actually, they have all the libraries there. You can program it using LabVIEW, LabWindows, whatever tool floats your boat. And yeah, it'll all work. That's the advantage of National Instruments, is that everything's integrated with all their tools and things like that, all their programming environments.

**Dave Jones:** So yeah, you can do that. But in the app here, nah, it's just, it's pretty basic. And I will not play with this today, but there's a networking option up here, because it's just going to work the same. I'm, you know, and I don't have an iPad, so I can't test

**Dave Jones:** the iPad app. But we can create a new wireless network here, and we can disable, right? So we can create a new wireless network and set it all up and everything. You know, and we can play around with the Ethernet as well and hook it up either way.

**Dave Jones:** But it works excellent via USB. No problems at all. In fact, as we saw at the start, it's fantastic with USB. You just plug it in, it's a drive, the software's on there, you just run it, boom! No software installation on your machine.

**Dave Jones:** Oh, it's beautiful. Why can't everyone do that for a USB scope? I don't know. And again, another disappointing aspect of this thing is the digital multimeter down here. Like, it's going to have good specs. I probably won't even insult National Instruments reputation by, you know, hooking up, you know, my reference generators

**Dave Jones:** to this and playing with it. It looks like it's fast. Updating 5.5 digit meter, but what can you do with it? It's just a multimeter. Where's, like, trend plotting and stuff like that? Like, you know, it's just not there. It's begging for it.

**Dave Jones:** It's absolutely begging to have a logging multimeter there to get trend plots and stuff. And it's just not there. Other stuff that is missing from here, did I mention it before? I don't know, this has been far too long. But where are the Bode plots, for example?

**Dave Jones:** No, not Bodey, Bode. That's how we pronounce it here. And, like, where's the Bode plot? Like, classic training stuff like that. It's got the function generator, it's got the DSO, it's got the multimeter, it's got the... everything's built in, right? But you can't

**Dave Jones:** log stuff. You can't do things like that. You can't get Bode plots. Like, how can we sweep the function generator? We can't sweep it, we can't modulate it, we can't do anything. Like, it's just really rudimentary stuff. And this is a six grand instrument.

**Dave Jones:** So I would have, you know, expected the software to have all the bells and whistles like that. You know, you can go buy your analog discovery thing for what is $150 or $200 or whatever it is. I think it's under $100 educational price, and it does those sorts of things.

**Dave Jones:** You know? And this thing doesn't do it. So, yeah, disappointed. Thumbs down, national instruments in terms of advanced functionality like that. But it gets a thumbs up in terms of basic functionality and implementation, but that's all it is. It's a basic implementation of stuff, and it's disappointing.

**Dave Jones:** Like the power supply, for example. We can't sequence the power supply. Where is the sequencing stuff? Tracking. Oh, we can set tracking the positive and negative, but that's it, right? Like, that's begging out. The power supply is begging out to be programmable. Where's the programmable functionality?

**Dave Jones:** Like I said, you can code this stuff yourself using whatever national instruments tool you like, but that's beside the point, right? An instrument of this price and grade and educational focus should have all this sort of you know, programmable functionality built in. So, yeah.

**Dave Jones:** Disappointed. Quite disappointed. Oh, alright, there it is. I've hooked up my multi-thousand dollar 10k precision resistor, and it's bang on. And I'll tell you what else would have been nice on this thing as well. Would have been nice to maybe have a K-type thermocouple probe on this thing as part of the

**Dave Jones:** multimeter, or maybe they could have like a Tate and K-type connector on the front panel, so you can hook up the, you know, regular temperature probes. Maybe two channels? That would have been really nice, wouldn't it? That would have added a huge amount, wouldn't have added anything in the scheme of things

**Dave Jones:** to the cost of the hardware, but they, you know, they didn't add that, you know, you could have done sequencing of your power supply with logging with your digital multimeter, logging the temperature as well while capturing scope signals, and this could have been

**Dave Jones:** a ridiculously powerful debugging tool that everyone would have used. Everyone, you know, if it had all that advanced functionality, and like the 350MHz version we're looking at, he is quite expensive, but the 300MHz dual channel one's not, you know, out of bounds for, you know, your hobbyist or your professional or something like that.

**Dave Jones:** And if it had all that advanced functionality, then, you know, maybe it would have been a lot more tempting for the individual to buy this thing, but nah, it's just got basic functionality. Alright, I'm going to try out some, just some loads here on

**Dave Jones:** the plus 25 volt channel. I've just got my DC electronic load here, my BK Precision load, and I've got it set for 22 watts, and which is constant power load, and it doesn't start up. It does not start up with that, whereas if I go switch it, hang on.

**Dave Jones:** There we go. There we go, I just went to switch that, and you'll notice that it came good. But if I turn that power off and on again, it won't restart. So I can't quite do the 25 volts 1 amp that it claims on there.

**Dave Jones:** So there must be, you know, there's some power envelope thing, I'm not sure if they have that in the manual or not. I don't think it's that, the specs of that are detailed. I don't remember seeing any power response graphs, so I'm just drawing a couple

**Dave Jones:** of watts from the second channel here, and you know, it's got excellent specs on the power supply, and you know, it reads back directly from the terminal. Everything's hunky-dory, but yeah, it can't quite deliver what it claims, that's all. But no big deal.

**Dave Jones:** So there you have it, that's a look at the 350 MHz National Instruments virtual bench. Thank you very much National Instruments for loaning this one so we can have a play around with it. And you probably already know my opinion of this thing.

**Dave Jones:** It's competent in what it does, the software's competent, there's no bugs, it's fast, it has all the basic functionality, but I can't help but be quite disappointed. Very disappointed especially at the price point for this 350 MHz one that doesn't have more programmable capability, the ArbGen, you know, like basic stuff.

**Dave Jones:** Power supply sequencing, multimeter logging, things like that. Why can't I do these sorts of things? Granted, it's software, they can add it, and I hope they take this on board and things like that, and actually improve the software. Because they can improve it, they can add stuff

**Dave Jones:** to the FPGAs and things like that. I'm not sure how they'd update them, but I'm sure they'd update the FPGAs in there, and I'm sure they've thought of that. Maybe you should be able to maybe get a tool to do that. And yeah, it really is some serious hardware

**Dave Jones:** at a serious price, and the software's competent but very quite basic. But much better than most USB oscilloscope software I've used is just crap. But as I said, there's some other good ones out there like the analog discovery and things like that, that do have a lot more functionality in there

**Dave Jones:** for a lot less price. But this does exactly what they wanted it to do, which would be for the all-in-one education market. So this is not really something that the individual would go out and buy necessarily. It's a very niche market for that.

**Dave Jones:** If you need the compact form factor, I love that everything is all in the one unit, that's fantastic. I can think of many times in the past where I would have killed to have such a small form factor thing from National Instruments. I've had to use multiple National Instruments cards in

**Dave Jones:** production test systems and things like that to automate all sorts of stuff. Or automate even benchtop systems, not necessarily production test systems, but they're on benches. And just to have one little box that does it all is brilliant. And I've had to have racks, 19-inch racks full of all

**Dave Jones:** the different individual gear to actually do stuff like this. And to have it all in one box is really quite neat. And the hardware quality and design is first rate. So you're definitely no issues there at all. You're getting your money's worth. And the software, it's competent

**Dave Jones:** but very basic. I just wish it was better. And I think that they could actually have quite a reasonable, bigger market out there for the thing if the software did more stuff. In terms of login and automation and stuff like that. I know it's all programmable, but out of the box I would have liked to see

**Dave Jones:** it do a lot more. I thought of, as I said, described like half a dozen different things that I was disappointed that the software didn't have. And I kind of expected it to have those sorts of things. At least half a dozen. If I sat here and thought about it, probably

**Dave Jones:** a dozen improvements I could make to the software to do that. But anyway, it's a nice bit of instrument. Gets a thumbs up. But yeah, it's not something that you'd go out and buy. You're paying for the bandwidth here. For 350 MHz there's much better value out there in benchtop scopes and things like that.

**Dave Jones:** This is not double the price of a 350 MHz scope. It might be. The retail price might be like a 350 Meg Rigol. No, they're about $4,000, something like that. This is about $6,000. Maybe the Siglent ones are a bit cheaper, but it's a different instrument

**Dave Jones:** for a different market. But it's all in one. The power supply, the digital I.O., the function gen. Yeah. And I haven't tried out the iPad-y app and things like that. So in theory you could sit this on your bench and have your iPad tablet just there

**Dave Jones:** and it's actually an incredibly small form factor thing. Or you could have a notebook or something like that. Wireless connection. All that sort of jazz. And it could be very good. But yeah, there's more powerful benchtop oscilloscopes out there. And if you're after a

**Dave Jones:** general purpose instrument, you wouldn't be buying this thing. You'd get a general purpose benchtop or something like that with maybe a USB logic analyzer added on just for logic analyzer and protocol analysis. Because the protocol analysis is very rudimentary on this thing and you can't trigger off staff and search.

**Dave Jones:** I haven't even gotten into all that sort of jazz of the logic analyzer functionality in the thing. It doesn't have any of that. So yeah, you wouldn't your average professional would not be buying this as their everyday tool. But for the education market, yeah, it's quite neat.

**Dave Jones:** You can hand a tablet around the classroom. People can play with it. It can be hooked up to all sorts of stuff and they can interact with it and play. And it's definitely quite neat. But if you do have that niche need for an all-in-one instrument,

**Dave Jones:** especially one that's programmable using LabView or LabWindow CVI or any other programming system, then to automate stuff and things like that, this could be the bomb. A real small form factor. And people might complain about the price. But from big companies that I've

**Dave Jones:** came from, it's nothing to spend $20-30 grand on a 19-inch rack full of rack-mount PC to automate stuff, and then all the separate instruments costing $5-10 grand a pop. It is not unreasonably priced in that respect. It's just a different market to what

**Dave Jones:** a hobbyist or a low-end professional might be used to. When you're spending your own money, it's quite a lot different. But for companies and educational institutions who would be getting a hefty discount on this thing, I'm sure when they buy them in $20-30, a couple of classroom or two at a time worth,

**Dave Jones:** then they'd be getting substantial discounts. But yeah, it has its market. So don't complain about the price. It is what it is. And I think it offers quite reasonable value for money if you're integrated all-in-one. I don't know another one that's as heavily integrated as

**Dave Jones:** this one. I'm not sure. I don't think there is. You know, there's a couple of like the bareboards, like the Analog Discovery and things like that, which are just not professional bench-level instruments like this one is. So yeah, it is what it is.

**Dave Jones:** And I like it. It's very nice. It worked out of the box. I've had no bugs, no crashes, and it was all seamless. And it's great. I like it. So that's it. I hope you enjoyed that not brief at all look at the new National Instruments Virtual

**Dave Jones:** Bench. Catch you next time. you know even at the full 270 bucks that's you know it's really quite decent
