---
video_id: HiqtXdK1Dtk
title: EEVblog #879 - R&S HMO1202 Hacking Extended Version
url: https://www.youtube.com/watch?v=HiqtXdK1Dtk
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 0, "2": 30, "3": 59, "4": 59, "5": 89, "6": 89, "7": 119, "8": 149, "9": 149, "10": 179, "11": 209, "12": 209, "13": 269, "14": 299, "15": 359, "16": 419, "17": 479, "18": 539, "19": 599, "20": 659, "21": 719, "22": 719, "23": 719, "24": 779, "25": 779, "26": 779, "27": 839, "28": 899, "29": 959, "30": 959, "31": 959, "32": 989, "33": 1049, "34": 1079, "35": 1109, "36": 1109, "37": 1139, "38": 1199, "39": 1259, "40": 1319, "41": 1319, "42": 1319, "43": 1379, "44": 1379, "45": 1379, "46": 1439, "47": 1469, "48": 1469, "49": 1499, "50": 1499, "51": 1499, "52": 1529, "53": 1529, "54": 1559, "55": 1559, "56": 1589, "57": 1619, "58": 1649, "59": 1649, "60": 1699, "61": 1730, "62": 1750, "63": 1766, "64": 1784, "65": 1815, "66": 1827, "67": 1835, "68": 1853, "69": 1857, "70": 1881, "71": 1895, "72": 1911, "73": 1933, "74": 1947, "75": 1977, "76": 2017, "77": 2046, "78": 2073, "79": 2088, "80": 2099, "81": 2123, "82": 2138, "83": 2154, "84": 2173, "85": 2191, "86": 2217, "87": 2235, "88": 2248, "89": 2253, "90": 2261, "91": 2270, "92": 2278, "93": 2285, "94": 2291, "95": 2297, "96": 2303, "97": 2319, "98": 2325, "99": 2331, "100": 2347, "101": 2353, "102": 2359, "103": 2375, "104": 2381, "105": 2387, "106": 2393, "107": 2409, "108": 2415, "109": 2421, "110": 2437, "111": 2443, "112": 2449, "113": 2465, "114": 2471, "115": 2477, "116": 2483, "117": 2499, "118": 2505, "119": 2511, "120": 2527, "121": 2533, "122": 2539, "123": 2555, "124": 2561, "125": 2567, "126": 2573, "127": 2589, "128": 2595, "129": 2601, "130": 2617, "131": 2623, "132": 2629, "133": 2645, "134": 2651, "135": 2657, "136": 2663, "137": 2679, "138": 2685, "139": 2691, "140": 2707, "141": 2713, "142": 2719, "143": 2735, "144": 2741, "145": 2747, "146": 2753, "147": 2769, "148": 2775, "149": 2781, "150": 2797, "151": 2803, "152": 2809, "153": 2825, "154": 2831, "155": 2837, "156": 2843, "157": 2859, "158": 2865, "159": 2871, "160": 2887, "161": 2893, "162": 2899, "163": 2915, "164": 2921, "165": 2927, "166": 2933, "167": 2949, "168": 2955, "169": 2961, "170": 2977, "171": 2983, "172": 2989, "173": 3005, "174": 3011, "175": 3017, "176": 3023, "177": 3039, "178": 3045, "179": 3051, "180": 3067, "181": 3073}
---

**Dave Jones:** Hi. Now, you've seen this little baby in several previous videos, the Roden-Schwarz HMO 1202 series scopes, and click here if you want to have a look at the, I've done a teardown video of this thing. I've also done videos for comparing the FFT mode, which I really like on this thing, and things like that.

**Dave Jones:** It's a really nice little compact professional scope. So there's really a lot to love about this thing. It's whisper quiet, it's small and compact, one of the smallest scopes on the market, and it's great and responsive and fast and everything else, and it's fairly decent value for a, you know, a real top shelf brand like Roden-Schwarz.

**Dave Jones:** And it's a mixed signal scope, of course, and it, probably it's only major downside is that it's only two channels, but hey, you know, it's, for this sort of compact scope, it's just fine. So I love this little thing. And you'll notice that up the top here, it does not have a band

**Dave Jones:** width listed on it, which is quite unusual. And the reason they do that is because this is a software upgradeable band width scope, as many on the market are nowadays, probably the, you know, a good majority of them actually have the full band width inside them in the vertical amplifiers here.

**Dave Jones:** The band width is actually there, but then they software limit you via license keys and everything else to various band widths. Now this one is available in 100 megahertz as the base band width. That's about, goes current price is about 1300 US dollars for that one.

**Dave Jones:** And there's also a 200 megahertz version and my one here is the 300 megahertz version, but you shouldn't, wouldn't know it by looking at the front panel because you've got, it's just a license key inside which upgrades the bandwidth. So even the base model 100 megahertz unit you buy for, you know, 12, 1300 bucks or something like that is, has the full 300 megahertz bandwidth in here.

**Dave Jones:** So I thought just for educational purposes, we will crack this thing open yet again and we'll have a look at the front end here yet again and see what chip it's using, what topology it's using, and see if there's any little tweaks that we can make to potentially get greater bandwidth out of the base model unit.

**Dave Jones:** Unfortunately, I've actually got, unfortunately, in quote marks, I've got the 300 megahertz license keys already installed for this one, but it's full bandwidth, but we should be able to probe some things and have a look at how they're actually doing that. Should be fun.

**Dave Jones:** Let's go. And the only thing that tells me this is a 300 megahertz version is just this sticker on the back they've got here. So they've obviously, this is done at the factory, they've whacked the sticker on, but you can actually buy the license upgrade later.

**Dave Jones:** So here's inside the unit as we've seen in the previous teardown video. I've got metal cans on the top here for our two analog channels and unfortunately metal cans on the bottom, which are even more unfortunately soldered in place, but there's only one point there.

**Dave Jones:** One solder point. So I can desolder that and lift this can off without having to take the board out. So yeah, okay, small win. Now if we have a look at the front end here, I've got that bottom side can off, then there's our BNC, we've got some attenuation switching relays, and these transistors down in here, they're probably, well, those S-SOT23 packages, they're likely transistors, they're probably the JFET

**Dave Jones:** and the BJT or something like that. And apart from that, and I've got, here's a photo of the other side of the board, I won't bother taking the other side of the board, I think you have to get the whole board out to get that out.

**Dave Jones:** But yeah, I've got a photo of that side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here.

**Dave Jones:** And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there.

**Dave Jones:** The part we are interested in is, however, right here. And apart from that, and I've got a photo of the other side, and there's nothing terribly interesting there. The part we are interested in is, however, right here. that's basically the only thing that we capture there.

**Dave Jones:** And it's got this one here, and it's got this one here. Now this one here is 24 bits long, is exactly what it shows in the datasheet. So if we have a look here at the write operation, you can see that this is a single access cycle, and the chip select is supposed to go low of course, but it doesn't, so we're not sure what's going on there.

**Dave Jones:** And this shows that the data bits are sampled on the positive going edge of S-clock here, and it shows that there's 24 bits total in there. So that's exactly what I counted in there. So there's a command field of 8 bits, so there's 8 bits command and 16 bits data.

**Dave Jones:** And here is that 16 bit data field, and you can see D6, D7, D8 here, see table 6, and this is the bit that should change. So I'd expect a D6 to change from 20 to This bit to change from 20 to 350, so D8 and D6, I'd expect those to toggle on the different write operations when we toggle that bandwidth limit button off and on.

**Dave Jones:** Or at least go between 1 and 0 here, between 20 and full for example. So yeah, but we're not seeing that. We're seeing no data change at all. It's weird. Now there's something very, very strange going on here. I just know that chip select line must be positive.

**Dave Jones:** So what I've done is I've hooked up a second scope here, and sure enough, to the chip select line, look, there it is. I can re-trigger, here we go, I'll show you in the one shot, I'll re-trigger this thing, oh here we go, single shot capture, okay, and I press the bandwidth limit button, bingo, there's the chip select line.

**Dave Jones:** I'm probing it, and I'm probing the exact same line on the Rodenschwartz scope itself, and I've got a And it's just, like, it's not, it's not doing anything. It's not doing anything. Look, type, trigger, edge, no worries, source, channel 1, we're in channel 1, negative slope, positive negative slope doesn't matter, it should capture something, and it's not capturing a damn thing.

**Dave Jones:** It doesn't help that the single mode works back to front, it's really weird. Anyway, auto normal thing, like, it just, it stays high. That's it, what the hell? I've changed probes to the genuine Haymeg slash Rodenschwartz one, and it's the same thing, but this is the data line now, I was getting the same thing on chip select, just wasn't there, and now I'm getting this on the data line, which coincidentally is just continuously triggering now.

**Dave Jones:** So, yeah, go figure, but you put it in, let's go over to channel 1 here, it still triggers, let's go into... I don't know, another menu, it's still automatically triggering, whereas we weren't seeing that before, but something's weird going on, this thing just will not probe the chip select line for some bizarre reason.

**Dave Jones:** And here's this average trap that I did in a previous video just recently, if I actually trigger this thing, here we go, this is my chip select line, and you'll think, oh, something's weird, something weird's happened to the chip select line, but it's not.

**Dave Jones:** I guarantee you, if I go over here, silly me. It's still got average in mode on, I was just playing around with that this morning, somebody asked if I could do that. Anyway, here we go, there we go, there's our chip select line, I'm just, it's not, the chip select line is not continuously triggering, okay?

**Dave Jones:** So, you'll see it's not updating there at all, but if I press the bandwidth limit button, bingo, it updates, and then it just updated again, and, you know, so it's like, but... That data, on the data line, just keeps coming out. So this has got to be a peb cac, I'm just trying to sanity check to figure out what's going on here, sorry about all this, this is like real time, you know, this is a real problem I'm encountering here, so I'm gonna show it.

**Dave Jones:** Um, and, look, I'm probing the data line on both of them, so it's like, it's auto updating, no problems whatsoever, right, everything's, everything's fine, for whatever reason it's auto updating at the moment, or sending data on that line, although there's no chip select line, so it's fine.

**Dave Jones:** So I've got both probes on exactly the same point with two scopes, let me now change, do that exact same thing, but move the probes to the chip select line. I'm pressing the bandwidth limit button there, okay, I've got both scopes set to normal mode, so it will only, um, trigger, you'll notice there's, there's small changes in the width of that, but I, I'm getting nothing there, I swear, I swear I'm probing exactly the same damn point, down there.

**Dave Jones:** I'm pressing the bandwidth limit button there, okay, I've got both scopes set to normal mode, so it will only, um, trigger, you'll notice there's, there's small changes in the width of that, but I, I'm getting nothing there, I swear, I swear I'm probing exactly the same damn point, down there.

**Dave Jones:** I'm pressing the bandwidth limit button there, okay, I've got both scopes set to normal mode, so it will only, um, trigger, you'll notice there's, there's small changes in the width of that, but I, I'm getting nothing there, I swear I'm probing exactly the same damn point, down there.

**Dave Jones:** There's the probes, look, probing exactly the same point, and, like, what? What? That is one of the weirdest things that I've ever seen, it's not like this scope is incapable of probing itself, the analog front end does not matter, it should not matter, it can't matter where it's hooked up to, as long as, you know, you don't short anything out with ground issues or anything like that.

**Dave Jones:** I'm going to the chassis ground, it shouldn't care where the signal's coming from, it's relative to that ground, it's exactly the same point, it, it should work, and it works for one of the lines on the SPA boss, but it doesn't work for, on the other.

**Dave Jones:** What? There's gotta be some sort of pep cack with this thing, it, it's gotta be me, what the hell am I doing? I've resorted to the manual, this is bad, it really is, I don't know what's going on with this scope. No, I'm at a loss.

**Dave Jones:** I'm at a loss here, look, I'm, I've got the correct type, I've got edge triggering, I'm at the correct source, channel one, which is what I'm using, the slope, positive, negative, both, it makes absolutely no difference to what happens, and then the filter, we're on DC, so we can set our level here, okay?

**Dave Jones:** And here is the thing, right, we put it in auto mode, okay, so here's our level, it's positive, trigger level is smack in the middle, right, here's our ground point down here, everything's hunky-dory, this should work, you put it in normal mode, okay?

**Dave Jones:** The trigger goes like this, and if I go to channel two, here, and change the bandwidth, look, it triggered, it triggered, but it didn't capture and display any data. What the hell? What is going on? Yet, if I go over to my keysight scope here, and I do the same normal mode, and I press that bandwidth limit button, it's capturing that, the probes are on the exact same point.

**Dave Jones:** There is something seriously wrong with this scope, and I don't know what. Have I got some sort of weird software bug? If I have, it's bloody well major. People are probably screaming at me right now, it's obvious. But unbelievable. Okay, so it's clearly, this trigger thing here is resetting, whenever I push this bandwidth limit, I can actually disconnect my input here, right, we just triggered, and I can push this bandwidth limit, and it resets that, and there's no triggered light here, which is like a latched, you know, a pulse-stretched triggered light, so it's obvious.

**Dave Jones:** It is not triggering, right, so okay, it's not triggering. That's why our data is not coming up. Okay, fair enough, but why the hell is it not triggering? That signal is there. Look, I'll, here we go, look, I'll plug this same thing over to here, okay, and let's do the bandwidth thing, there we go, there we go, look at that.

**Dave Jones:** Okay, so that needs compensation, obviously, that's, you know, it's poorly compensated. But it works, yet I plug it on this scope, and it doesn't. And the exact same thing happens on channel two, when I set the source to there, and I've set it up, and look, if I actually plug in a signal here, there we go, I'm plugging in like a one mega square wave, it triggers.

**Dave Jones:** No problems at all. And, like, if I go back to channel one, it's the same thing. If I go back to channel one, it's there. So bugger it, I've had enough of using this thing to probe its own clacker. Let's have a look now at hooking up the SPI line here.

**Dave Jones:** So I've got all three channels coming in. By the way, it is not a true SPI as you know it, because SPI, if we go in here, is normally a four-wire thing. We've got our clock, our, whoop, bloody touchscreen, our MOSI, and our MISO, i.e.

**Dave Jones:** input. And output data signals and chip select. But in this case, it's actually a three-wire SPI interface. It's still SPI, but it's three-wire. So it shares, it's bi-directional here. So it's not as great a throughput. It goes tri-state and everything else. So anyway, we don't actually have specific support for that.

**Dave Jones:** So I've just set it up here. I haven't set up the bits yet, but let's just trigger this thing and have a look. I'll press the bandwidth button. And there we go. Look at this. We've got our clock. We've got our data. And now we have our chip select.

**Dave Jones:** Yay. Now the most interesting thing about this is, look, we're getting our 24 clocks. Exactly what we expect before. And if I zoom right out, okay, just what we were doing way, way back, and I press it. Look, we're getting none of that double rubbish that we were getting before.

**Dave Jones:** You remember the one that had the 50 or 60 clocks or whatever? We're getting exactly what we expect as per the data sheet. So it's bizarre. I've got no idea. This is exactly what we expect. And let's just have a look to see if this data now here changes.

**Dave Jones:** I haven't tried it. Okay. So we're in, let's go to normal mode. So we're in normal mode. Let's see. Normal mode. So let's go to a quiet, yeah, we're in normal mode. Okay. So we're going to run it. Here we go. So I press it.

**Dave Jones:** Let's press it again. Look. Bingo. There we go. Wow. I could have saved like half an hour of video or something. Look. That's it. The bit is shifting exactly what I expected from the get go. And, like, why we could, why? That's a problem with the Roden Schwartz measuring its own clacker.

**Dave Jones:** I don't know. I honestly do not know. So now we can get in there and actually decode the bit. That's exactly what I expect. It's exactly as per the data sheet. Here it is. It's exactly what we expected with the 24 bits or whatever.

**Dave Jones:** Here we go. Write operation. There we go. It's supposed to send 24 bits. The command and then the data field. And we have the data for that. And we can see the bit changing. Yeah. It's somewhere over here. Yep. If you correlate it, look.

**Dave Jones:** It looks to be in the right spot to have the D6, D7 and D8, which is our filter selection field. All right. So let's just have a look at the first section, which is the command section here. And we'll just expand that out.

**Dave Jones:** And here's where it starts here. And the command to write is here. And here's where it starts here. And here's where it starts here. And here's where it starts here. And here's where it starts here. And here's where it starts here. And here's where it starts here.

**Dave Jones:** And here's where it starts here. All right. And here's where it starts here. And here's where it starts here. And here's where it starts here. And here's where it starts here. And here's where it starts here. And here's where it starts here. And here's where it starts here.

**Dave Jones:** And here's where it starts here. And here's where it starts here. And here's where it starts here. And here's where it starts here. And here's where it starts here. And here's where it starts here. And here's where it starts here. And here's where it starts here.

**Dave Jones:** And here's where it starts here. And here's where it starts here. And here's where it starts here. And here's where it starts here. And here's where it starts here. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.

**Dave Jones:** And the command to write is a 0. And the command to write is a 0. And the command to write is a 0. And the command to write is a 0.
