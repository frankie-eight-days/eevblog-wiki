---
video_id: UDGsZcAWgL8
title: Rigol MSO5000 Bug Bonanza
url: https://www.youtube.com/watch?v=UDGsZcAWgL8
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 0, "2": 30, "3": 59, "4": 59, "5": 89, "6": 119, "7": 119, "8": 149, "9": 179, "10": 179, "11": 209, "12": 239, "13": 239, "14": 269, "15": 299, "16": 299, "17": 329, "18": 359, "19": 359, "20": 389, "21": 389, "22": 419, "23": 449, "24": 449, "25": 479, "26": 509, "27": 509, "28": 560, "29": 560, "30": 590, "31": 590, "32": 620, "33": 654, "34": 654, "35": 680, "36": 710, "37": 740, "38": 740, "39": 770, "40": 770, "41": 800, "42": 830, "43": 860, "44": 860, "45": 896, "46": 920, "47": 920, "48": 950, "49": 950, "50": 992, "51": 1010, "52": 1030, "53": 1052, "54": 1069, "55": 1078, "56": 1098, "57": 1112, "58": 1134, "59": 1154, "60": 1180, "61": 1198, "62": 1220, "63": 1236, "64": 1256, "65": 1272, "66": 1290, "67": 1308, "68": 1320, "69": 1336, "70": 1358, "71": 1380, "72": 1389, "73": 1413, "74": 1435, "75": 1451, "76": 1469, "77": 1487, "78": 1503, "79": 1516, "80": 1536, "81": 1554, "82": 1570, "83": 1588, "84": 1606, "85": 1626, "86": 1648, "87": 1665, "88": 1689, "89": 1703, "90": 1719, "91": 1745, "92": 1759, "93": 1775, "94": 1801, "95": 1826, "96": 1848, "97": 1868, "98": 1886, "99": 1912, "100": 1938, "101": 1958, "102": 1979, "103": 2001, "104": 2021, "105": 2043, "106": 2065, "107": 2083, "108": 2103, "109": 2132, "110": 2142, "111": 2162, "112": 2176, "113": 2188, "114": 2206, "115": 2226, "116": 2248, "117": 2265, "118": 2285, "119": 2303, "120": 2325, "121": 2341}
---

**Dave Jones:** Hi, just wanted to do another video just playing around with the new Rigol 5000 series scope and just maybe comparing it to some other scopes doing some serial decoding and just playing around with some of the features of it. And I found right off the bat here, I was just playing around with some SPI decoding and I don't know what's going on here.

**Dave Jones:** I really don't. I'm in just standard two channel mode. I'm feeding in two signals here and I'm just playing around with some SPI decoding. And you might think there's no signal there. They're both grounded, channel one and channel two. I've got my trigger point right in the middle here and it might actually come good while I'm actually saying this.

**Dave Jones:** But trust me, there's and it's refreshing. It's refreshing and it's not. There it is. There it is. I swear I didn't touch it. These signals I'm feeding in SPI signal and they just magically appear. Look, if I press run, stop, look, they're gone, right?

**Dave Jones:** Like I'm in, like you can't see it because like my, I've got my studio lights installed, my old ones anyway, get me up and running. But yeah, it's in run mode and I can do single shot. Single shot's fine. Single shot will capture it every time.

**Dave Jones:** My trigger point is smack in the middle of that data and it just cannot, it's 20 meg points at two gig samples a second. And it just runs stop mode. It's just nuts. It's almost as if there's no signal there and the volts per division doesn't actually matter.

**Dave Jones:** Look, it's vanishing. They're vanishing. What is, I swear it's just normal trigger, normal edge trigger, rise in, hold off, like what the hell is going on with this thing? I don't know. Now it's come good. Has it? It's going to make a fool out of me, but I cannot believe there's no signal there.

**Dave Jones:** I plug those same two signals into any other scope. It is fine. There's something up with this Rigol 5000 series. It's, it's just strange. And if I plug that exact same channel one signal over to here on the key site, 3000, there it is.

**Dave Jones:** Like you can see it coming up. It's like, you know, it's, it's there, there it is. And I'm decoding the SPI, but look, you know, when I run that, I actually see a signal. I see a signal on that. There it is, right?

**Dave Jones:** It's, it's infrequent. Maybe that, you know, that's probably the problem. It does not like, for some reason, it does not like long periods between trigger when you get to a certain, no, no, it's gone. Like, where is it? That's just, that's just nuts.

**Dave Jones:** Is it like, like some ridiculously slow update rate or something that's hardly ever seen it? Doesn't feel like that. It feels like there's just, feels like there's something else going on. So it's actually a, seems to be a strange function of the, because we're in auto mode.

**Dave Jones:** We're not in normal mode. If you switch it into normal mode, let's go in here, have a look. Mode, normal. Okay. It pops up. And your data's fine, but, but if we put it in, a single shot's going to work, of course, but we put it in that auto mode and there we go.

**Dave Jones:** It's just, it might pop up occasionally, might not. So yeah, I, auto, I don't like it. Maybe it's just the particular frequency that I've got on this thing, but eh. And if we try it on the Keysight 3000, everything's hunky-dory. Doesn't matter what time base we set it to, like you'll eventually see something in auto mode there.

**Dave Jones:** And of course you put this one in normal and it's going to work fine and dandy too. But yeah, I, is it just a beat frequency thing with the auto refresh? I don't know. And even the Venerable 1054Z here is going to show it up more frequently.

**Dave Jones:** So, and you're just working in normal mode and you're fine. Yeah, I know that's a usage thing. It's just, like, it, it just got me. Like, I just thought it was weird. I thought, like, there's no signal on my screen at all. There was nothing.

**Dave Jones:** Couldn't see a thing. Yet any other scope I use, I at least see it periodically in auto mode. But, eh, anyway. More investigation required. Almost a bit depressing to use. Now, I've, I've set the same exposure here and I'll show you different scopes.

**Dave Jones:** I'm not sure if this will show up on camera or not, but the Roden Schwartz is the winner. It has the biggest and brightest screen out of the bunch. Much higher res too. This thing sticks on a stick. It's just beautiful. And even the old Rigol 1054Z has a, you know, a brighter screen on it.

**Dave Jones:** And yes, that screen is glarey, but putting it side to side with the Roden Schwartz, ah, it's, the Roden Schwartz is probably glareier. It's like crisper. Shows more detail. Love it. Should be in the spec sheet. You know, screen reflection, signal integrity. Anyway, I'm doing some SPI serial decoding here.

**Dave Jones:** So we go into the decoder. You've got four different decoders. We've got it set up for SPI. We've got mode with which is, ah, the timeout mode, um, which allows you to just have the clock and the, ah, MOSI data down here. So you've only got the two channels here.

**Dave Jones:** You can either have them come in from the analog or the digital source. No problems whatsoever. Um, so, and you can specify your, ah, timeout there. So that's nice. Or if you have your, ah, chip select, of course, you can choose your chip select on the, ah, third channel.

**Dave Jones:** So, um, but the good thing is you can do SPI decoding without chip select without sacrificing one of your analog channels. If you're using the analog channels, say you're using the 16 digitals already for other digital stuff, you can do a serial decoder in addition to that.

**Dave Jones:** So I'll set that the timeout. You can set up your sources. So you can set your, ah, threshold here, for example, and it shows you your individual, ah, thresholds down here. Yes, I don't have the scaling set for my times 10 probe. So no worries on the threshold, ah, display.

**Dave Jones:** We can actually, ah, choose, asky, hex, for example, we can go in there and it gives us our hex. I am not really a fan of having the D in here for data. I know it's data, but it's kind of annoying if we go out, ah, it's not going to show us.

**Dave Jones:** It did show us before, ah, because it won't show hex. If we actually go in and asky, ta-da, sorry, Rigol, but, ah, there's a Roden Schwartz advertisement in here because it just happens to have a pattern generator with SPI on it. Yeah, that's where I'm getting my signal source from, if you're wondering.

**Dave Jones:** Anyway, um, yeah, I, like, I don't like it showing the D in there. It's kind of like, you know, annoying. So if you zoom out like that, which, of course, we can see our, ah, both packets here, then, well, it's kind of, like, annoying to read.

**Dave Jones:** I'm not a fan of that. Anyway, can we actually drag that signal there? Yep, it doesn't actually drag with you. though, but it, you know, it's, oh, look, it's, it stops decoding when you're doing the drag, of course. So, you know, it's not that responsive.

**Dave Jones:** I don't know if it's, ah, hardware or, ah, software decoding in the Rigol. I'll have to, ah, check up on that one. And we can set our ending in, of course, ah, most significant bit, least significant bit, no problems whatsoever. And, of course, if we do our least significant bit, we're not going to be happy with that anymore.

**Dave Jones:** Hang on. Our data seems to have vanished. Ah, Beulah? Beulah? What did I do? I was just moving it around. It's not decoding the data anymore. What the? What? Why? Have I screwed something up? What have I? I'm still in timeout mode. My sources are still set.

**Dave Jones:** So, what the, what? And, of course, we can set the position, but it, it, it stopped decoding. Why? It's, it's updating. Like, it's, you know, the data's actually updating there. Well, the signals are updating, sorry, but the data is not updating. It's going to show you the event table, but there's nothing damn well in it.

**Dave Jones:** Is this a pebcac? I'm just going to, like, disable decoding and simply enable it again. Where's our data gone? I don't get it. Is this a bug, or is this a pebcac? And I tried setting up a second, ah, decoder here, and no data either.

**Dave Jones:** Um, anyway, I wanted to show you this. If you try and position it further than that, you're going to get a bug. If you try and position it further than that, you don't get anything. So, I'm not sure whether or not, oh, yeah, you can't, actually, it's got nothing to do with channel one.

**Dave Jones:** You can't actually go below that. Why? Why can't I put it right down the bottom of the screen? That's just nuts. Look, you can go up there, that's fine. Why does that limitation exist? Let's look at the same data on the road in Schwartzy.

**Dave Jones:** I'll just plug it in. We're getting nothing at the moment. It's detecting the clock. And, bingo, pops up. Just love it how it's got all your frame information, and then it's just decoded down there for you, and then inside is very nice. I love that they put the secondary little clock and data there so that you don't have to view your actual signals up here if you don't want to.

**Dave Jones:** They're actually down there. That's a nice little touch. So, rather than just give you the decode, they give you the, ah, signals as well. So, that's pretty neat. Ah, couldn't have the font in there, but there you go. And check this out. I just wanted to show you this.

**Dave Jones:** It's decoding data in real time. I better not touch it. Decoding data, and I can press my touch lock to get rid of it. Anyway, watch this. Like, look at the lag. Look at the lag on that data compared to the, compared to the signal.

**Dave Jones:** That's just nuts. Ah, the decode. Let's go in and do our display, and we can do our event table, and event table on, and bingo. There it is. Format. Once again, we can do that in ASCII. There it is. Now, here's a little thing.

**Dave Jones:** Look, I can scroll that, but it doesn't stay scrolled. I'm turning the cursor knob. Something's happening there, but it's kind of like resetting to the top. I cannot... Like, I've got to stop it, then it'll do it. So, it's like it re-triggers it every time.

**Dave Jones:** I guess, like, it's supposed to, maybe? But you can argue that that's not... Well, it's kind of annoying. Like, I need to sort of, like, in nice view, fucking just override that. But I guess you could argue either way is correct. Anyway, we can then go into details like this, although we've got nothing there.

**Dave Jones:** And then the payload is just the raw data like that in the two packets that we've actually decoded there. And yes, we can just move this around the screen. So, menu off. There you go. Like, we can't dock anything or anything fancy like that.

**Dave Jones:** The screen real estate, there's just not enough screen real estate to, you know, do something like that. But you can move it around. It's kind of jazzy. So, that's at 100 kilobits. You'd expect it to decode that. No problems. 150 kilobits. See if it decodes that yet.

**Dave Jones:** Shorter. Yep. No problems. Let's go up to 1 megabit, which is the highest that Roden Schwartz can do. Yeah, there we go. Does that. No whackers. And as for UART data, handles it just fine. No problems whatsoever. This is 1 meg board and the data is asterisk IDN question mark with a line feed at the end of it.

**Dave Jones:** You might recognize that. And there you go. It's got the stop bits. This is actually 8 data bits, 2 stop bits and odd parity. And at 1 meg board, handles it fine. As I said, like, it's a bit slow. But it's certainly not unusable, that's for sure.

**Dave Jones:** What's FS? Hang on. I just noticed that the data can get a bit screwy here. I was playing around with it. You might have seen it back then. I don't know what the deal was. But I, yeah, look. Look. There we go. Our data's screwed up, you know.

**Dave Jones:** Our data's screwed up. It doesn't like that at all. We've got to go out. It's probably because it doesn't have the whole packet in memory. The whole thing in memory. Perhaps. But it's a bit odd. IDN. No, it works like that. We're in normal triggering mode.

**Dave Jones:** But you saw it. I was able to get some data that wasn't supposed to be there. That was weird. Oh, yeah, look. Data S-O-N. Like, that's just wrong. That's wrong. So, what's going on there? But it comes good when I go out like that.

**Dave Jones:** So, okay. IDN. Maybe some more investigation required. But, yeah. It does work, though. IDN. I didn't have the logic probes last time, but John South at Imona's kindly sent me the Rigol probes for this thing. What are they? PLA-216 or something they're called?

**Dave Jones:** $399 Yankee bucks for the probe. IDN. And that's pretty darn pricey. But, hey, let's take a look at it and some other aspects. This won't be a full review. I've actually got to send this back in a couple of hours. So, actually send the scope back.

**Dave Jones:** So, I won't have it any longer, unfortunately. It has to be sent to Silicon Chip because they want to review it, apparently. So, anyway. Or it's going off somewhere else. They might have another unit for them. Anyway, yeah, these new Rigol probes, they seem quite nice.

**Dave Jones:** They don't have any problems. IDN. I don't actually want to be, of course, for $400 Yankee bucks. But, anyway, I can't, unfortunately, I cannot open them. They're, like, you know, welded shut or whatever. I'd have to get the Dremel to that and damage them and I'd have to give them back.

**Dave Jones:** So, unfortunately, I can't do a thing. Anyway, one of the first interesting things is that this is the one that goes into the scope and you can see that they're not the same pin count. So, they've got their standard .1 inch header, of course.

**Dave Jones:** So, you could, in theory, make your own probes up. I don't think there's going to be much else in there apart, like, I don't think there's any differential drivers or anything like that. But don't quote me on that. I think it's just these are a nominal

**Dave Jones:** 100k. You can see it there. A nominal input impedance of 100k with 8 puff there, 8 picofarads. So, yeah, a pretty standard logic analyzer probe. So, in theory, you could make your own. So, they've probably just got the 100k resistors in there. And if you actually plug the thing in,

**Dave Jones:** it does actually auto-detect and it connected logic analyzer probe and it enables your logic analyzer. And when you get the logic analyzer up, you get various options. Let's have a look. You can actually select a waveform no big deal. You can turn various groups

**Dave Jones:** off and on. But then you can actually go in and turn individual traces off and on. So, I've only got the first four channels turned on for my experiments here. You've got a position control, which you can then invalid configuration. So, it looks like you can only move them

**Dave Jones:** in groups, I believe. So, you can't move individual waveforms. So, I personally, I've got some waveform data there you can see. I personally think they're very close together. Sort of, you know, I'd like to see a larger differentiation than that. And I've got it set to the large size, as you'll see.

**Dave Jones:** So, but you can group. So, you've got a position control, which you can then, oh, invalid configuration. So, you can have up to four different groups on this thing. Let's have a look. Sorry about the reflection on the screen and everything else. It's not good for videoing.

**Dave Jones:** And it's not the best screen to look at either. So, yeah. Anyway, we've got large, medium, small is really small. But I guess if you're trying to cram everything on the screen like, you know, four analog waveforms and you've got a bunch of digitals

**Dave Jones:** then, you know, you might want to... use small, medium and large. Unfortunately, the gap between the waveforms does not change. And as I said, I don't think there's a way to change that. Which is kind of annoying. You can actually label them, which is quite nice.

**Dave Jones:** Looks like you've got a library of, you know, all your yep, of all your basic stuff and things like that. So, you don't have to type min. But because this is a touchscreen we can label D0EEV log. There we go. How do we accept?

**Dave Jones:** Okay. The okay is not highlighted. What? Um, yeah. Okay. What? How? How? I want to call it EEEV log. Why doesn't it let me? What's going on? What? That's ridiculous. I think you might have to actually turn the labels on first, which is pretty dumb.

**Dave Jones:** So, EE. V blog. No. Still can't do it. Okay. I selected it from the library address down here. I think I had to did I have it selected there before? No. It's still not going to let me. It looks like you've got to erase that first and then EE

**Dave Jones:** V blog. And then you've got to click on that and now we've got EEV blog. Okay. Whatever. I got it. Okay. What else can we do in here? We can groups and we can change our color of our high, low, and edge as well.

**Dave Jones:** So, if you want. What? Is that it? That's that can't be the selection. I thought you'd be able to change it from a palette. Nope. Unbelievable. What? They're the selections. Why even bother having that at all if that's your selection? That's just crazy.

**Dave Jones:** Ah, you may as well not even have that function. Unbelievable. And then you can set up your groups in there, but that's about it for the, yep, that's it. For the logic analyzer functionality. Alright. I'm actually generating a pattern here. So, we can actually run this.

**Dave Jones:** I'm generating a 1 MHz counting pattern and I've noticed a few things already. A few issues. Let's check it out. So, the first one is we'll single shot capture that and we'll zoom in. Here's the weird thing. Right? This is so hard to see this

**Dave Jones:** on the camera camcorder screen. The trigger point is here. It's right on D0 there or the EEV blog channel. I don't know why they still call it. Well, okay, you can argue that D0, you can still do that. Can we move that channel

**Dave Jones:** by the way? We can select it, but we can't move channels. That's a bit disappointing. You know, what's the point of having a touchscreen if you can't do that? You can't unselect it either by double clicking. Anyway, look, my waveform is right in the middle.

**Dave Jones:** Sorry if you can't see that. I have a hard time seeing that with my eyes too when it's red and highlighted. Anyway, the trigger point, I am actually triggering off, if we go into the trigger menu here, I'm actually triggering off edge triggering.

**Dave Jones:** D0, okay, it doesn't put up the label EEV blog by the way. It just puts D0, so why, like, labeling is just an on-screen thing. It'd be nice, you know, I want to, when I go trigger, I want to be able to select

**Dave Jones:** oh, I want the clock line or I want something else. You know, I want my labels to show up there, so, like, it's almost, why even bother labeling them? I know for printouts and screen captures and stuff. Anyway, I've got right, let's go, rising edge, like that.

**Dave Jones:** Anyway, it was set up to either, so let's single shot capture that. Look, every time I capture that, D0, there's my trigger point. It is not there. It is not there. It is not triggering. And now, look, it decided to there, but when I do, look, I'll take out my time

**Dave Jones:** base a bit further, right, that looks like it's triggered. But when I go in, look, it shifted the waveform. What? It shifted it. My trigger point has not changed. Yet, somehow, this waveform, somehow, this display, the displayed algorithm or whatever, has decided that

**Dave Jones:** it's going to put it in the middle. What on earth is going on there? That's just crazy. So, I, like, it looks like it's below, above a certain time base, it looks okay. But when I get down below, like that, oops, jump back.

**Dave Jones:** Now, it's not. Like, no, there's something wrong there. I want my trigger point to be exactly where I tell it. So, I've changed my trigger to D3 up here, channel 3. It's doing exactly the same thing. Look at that. It just does not trigger at the correct point.

**Dave Jones:** That, it's just inexcusable. Anyway, if I keep single shot capturing that, it seems to be consistent. So, that's good. You'd expect it to be consistent. I'm putting in a consistent counting 4-bit counter. Now, if I actually go up to a 10 MHz counter, we

**Dave Jones:** start to see a few issues here. Look at this. That's a problem. We've got some extra pulses there. By the way, I'm generating this with, and probing, with the, just the Roden Schwartz to generate a pattern signal on there. And I'm using the supplied probes, by the way.

**Dave Jones:** You get with them you get a whole bunch of ground leads like that, with little ground flags on them. You get two packets of easy hooks, which are, you know, your regular easy hooks. They're fine and dandy. And all your little cables, which are very thin and nice.

**Dave Jones:** They feel very nice. I like the outer coating on that. It's not just really, like it feels like a, more like a woven fabric kind of outer, you know, thing, if you know what I'm talking about. Anyway, they come with these little molded flags.

**Dave Jones:** Obviously, there's no point putting them on here, like this. Obviously, they're designed to go on this end. And, you know, you stick them in there like that, and they're little identifiers. So they're kind of nice, you know. I don't mind that at all.

**Dave Jones:** So, that's pretty good. But, you know, I don't want to be decent for your 400 Yankee bucks, anyway. And that's one of the things, like you pay 400 US dollars for the probes, you can buy a very nice USB logic analyzer for 400.

**Dave Jones:** You know, a complete stand-alone system with much more comprehensive you know, software and everything else, and more like better capabilities and stuff. So, yeah, you know, you'd really want the mixed signal capability. Granted, like, nothing beats a mixed signal scope. By mixed signal, I mean when you've got logic analyzer

**Dave Jones:** and all of your analog stuff, especially 4-channel like this, all intermixed and triggered together. That's very nice. For many applications, that is like a series seriously powerful tool, except when it doesn't trigger on the correct location. Unbelievable. Anyway, yeah, mixed signal scopes I've done.

**Dave Jones:** Have I done a video on the advantages of mixed signal scopes? I think I have. I'll have to link it in at the end. Anyway, look at these little glitches on here. This isn't nice. And I've set up my threshold, by the way.

**Dave Jones:** Let's set up the threshold here. You can do group thresholds. This is done inside the scope. It would not, the threshold would not be done inside the probe. I'm absolutely sure of that. So, I've got it set to like regular CMOS, like, you know,

**Dave Jones:** 3.3, which is 1.5 volt, 1.65 volt threshold. You know, I could change it down to maybe, you know, let's change it down to 900 millivolts. See if that makes a difference. A little bit. But look at this. We're getting glitches. Right in the middle.

**Dave Jones:** In the middle of that. Wow. That's not terrific, is it? That's terrible, Muriel. Whoa. That moved. Why did that not expand? Look. There's something wrong with this scope. I swear. I'm moving the position here like this. I want to zoom in on that.

**Dave Jones:** Right? When you zoom in, you expect the window to expand around the center point. And it is not doing that. Look. It's just, it's just vanished. What on earth is going on there? Look. When you move in like that, but when you move

**Dave Jones:** out past a certain threshold, it's gone. It's gone. Is that the same point? I can't tell because it's all like, uh, just similar sequential... No. Look. There's that. It's almost as if it's vanished. Look. I'm seeing stuff there. That's got to be the same point.

**Dave Jones:** Surely. And there's no data showing in there. Is that some software artifact? Is that some sort of bug? Oh, no. It's back. Look. It's back. So at this time-based setting, it's there. That time-based setting, it's not there. Go in again. It's there. But it's not, it hasn't shifted

**Dave Jones:** properly. Like, I'm putting that in the center. Okay? So it should expand around that. And it's moved it again. There's something seriously wrong with this. Anyway, I'm not sure why I'm getting those pulses. You know, granted, okay, we're using fairly long, uh, probes here.

**Dave Jones:** But, you know, they're the supplied probes. They are, you know, fairly long. But they're standard for, like, logic analyzers and stuff. And it's not particularly quick. Okay, change it back to 1 MHz. And it's not like it changes the, uh, frequency changes the edge rate.

**Dave Jones:** Um, oh, look. See? Even at 1 MHz. That's 1 MHz. We're getting these runty pulses in here. Pinch and zoom to expand. That even doesn't seem to work reliably. Pinch and zoom. Ugh. Right, so what I'm gonna do is, uh, try my Keysight 3000

**Dave Jones:** scope over here. And with the Keysight's, uh, logic probes, which are these little, uh, jobbies here. Very similar length, uh, probes and everything. Everything else, exactly the same test point. So I've got both hooked on there. And let's see if we get these little runt pulses.

**Dave Jones:** Again, we're at, uh, 1 MHz. We're only at 1 MHz frequency. And let's go over here to the Keysight. And here we go. Let's single-shot capture that. You can see that there's absolutely no issues there whatsoever. So I'll set the thresholds up the same.

**Dave Jones:** So I've got that set to, uh, standard 1.4 volts TTL. I'll do the same on the Rigol. There we go. At the same 1.4 volts there. And let's see if we get our spurious data. It hasn't come back. But I have seen it at 1.4 volts before

**Dave Jones:** on 1 MHz. Let's go to 10. 10 MHz. Okay. Seems to have come good. I'm not seeing that anymore. Is that because of the extra probing on there? But we are seeing, look, these little, these little pulses here. And once again, if we go in there and try and expand that,

**Dave Jones:** dah! Whereas if we do the exact same thing over here on the Keysight, I'm triggering off, uh, channel 3 up here, D3, and like, it expands exactly how you'd expect it to expand. No problems whatsoever. And there's no multiple pulses on there at all.

**Dave Jones:** I'm just not seeing it. We're probing the exact same point, and the Rigol shows it was same threshold level. The Rigol's showing, uh, multiple pulses on the edge. So there's some sort of signal fidelity thing wrong with the Rigol. The probe, like the

**Dave Jones:** actual probes themselves, the input of the, the input circuitry of the Rigol, I don't know what's going on. But something's giving multiple pulses there, which are definitely not there, and I'm not, just not seeing that. Let's go up all the way with LBJ, up to maximum

**Dave Jones:** 50 MHz now. There we go. That's 50 MHz. Count rate. No problems, no multiple pulses, no nothing. There's a bit of, you know, timing issue between channels, which you'd expect. Little bit of variation there. Let's go over to the Rigol. Exact same signal.

**Dave Jones:** Multiple pulses. Look at that. Multiple pulses on two different channels. The same threshold voltage. 1.4 volts. At least it's consistent. That seems, that seems, it does seem consistent. Wow. But I wouldn't trust this thing at all. That's just, you know, okay, if you see multiple pulses,

**Dave Jones:** that's fine. It could, could be a probing and all sorts of stuff like that. But two identical logic analyzers with the same threshold and the same probe length and the same probing technique, one showing multiple pulses, the other isn't. Yeah. Sutton's up. And again, and watch

**Dave Jones:** this David Copperfield magic. We've got pulses there, pulses there. Expand the time base. Pulses are still there. Pulses are gone over here. That is just incredible. Look, here, like they're gone at this time base. They're still here. They're still here, but it's shifted.

**Dave Jones:** Okay, so here and here, on the rising edge. Now the, what? The falling edge? Oh no, it's shifted again. What? Ah, 'cause the waveform shifted. Ah, I give up. For reference, ah, hardware version 1.00.000. That's kinda disturbing. Didn't the teardown show a, a bigger number than that?

**Dave Jones:** Ah, reference my video. I think you'll find it might. Anyway, firmware version 1.01.02.03. I have an update. Let's update the firmware. See if it makes a difference. Let's just check out the, ah, firmware update. It's reading the disk. So, everything's hunky dory. Let's go into utility.

**Dave Jones:** Where is it? System. More. Unlock quick setting. No. About. How do I update? Bueller. Bueller. How do I update the firmware? Oh, by the way, I also got the, ah, 200 meg, um, option install. Here we go. Invalid license. What? Wah, wah, wah, wah.

**Dave Jones:** Um, I, anyway. Oh, retry left. Seven, what? Seven retries before it, what, locks me out? It's gonna, invalid license. It's gonna lock me out. So there you go. Is that some sort of protection? Hacking protection thing to, you've only got so many shots at installing a license.

**Dave Jones:** Um, I gave them my serial number. And they gave me a license file back. And it was supposed to enable the, ah, enable the 200 meg, um, option. But, anyway. Um, so yeah, the 200 meg points, which for some reason isn't installed. Why you bother?

**Dave Jones:** Like, it's a 100 meg point, um, scope. Why? Like, just give people the full 200 meg instead of the 100 meg. It's, it's ridiculous. Anyway. Okay, so I'm gonna assume that the, ah, way you load the firmware is to simply go into the, ah, storage.

**Dave Jones:** Load setup. Disk. Here we go. Drive D. Aha! License gel. There we go. So let's install that. That would, no. Rename. Delete. New folder. No. No. Well, how do you install the new firmware? Aw. Sadly, John just came to pick up the Rigol 5000.

**Dave Jones:** So, that's the end of that. I will eventually ah, get it back, I think. But, yeah, it's gotta go to Silicon Chip plus some other people. Ah, I want it. I think it might still be the only one in the country, is it?

**Dave Jones:** Anyway, I thought I'd try out the, ah, 7000 series Rigol, which I've still got. And I've got the Logic probes for it. They are nicer. It is a different, ah, interface. It's got that, ah, PCI interface on it. It is much nicer. It does, these probes instill a lot more confidence

**Dave Jones:** in me. So it's got these extenders, and I assume that they just, ah, feed ah, straight through. What these are good for is if you wanna keep your, ah, probes permanently attached to your, your circuit and all that sort of stuff, you know, without

**Dave Jones:** having to, 'cause it takes a lot of time to, you know, probe like 16 channels and set it all up and all that, ah, sort of jazz. So you can leave it attached to this, and then you can just disconnect this part of it and take your scope or, you know, or take your lead or go,

**Dave Jones:** ah, somewhere else. So, I guess that's kinda handy. Anyway, so I'm probing, doing exactly the same thing. Probing these, ah, the wires that you actually, or the leads you actually get with the, ah, 7000. They just, ah, they feel better. They feel better than the 5000, so it instills, ah, more confidence in you.

**Dave Jones:** Anyway, I'm generating the 50 megahertz, ah, the same 50 megahertz counting signal, and this one works a treat. Here we go. Single-shot capture. Run, and this one is just fine and dandy. And look, when you expand the time base, I'm triggering off, ah, D3 there.

**Dave Jones:** When you expand the time base, it works. Exactly as you expect. It's the same as what we, ah, see on the Keysight one. There's a little bit of, ah, jitter there. That's, ah, that's normal at 50 megahertz. That's probably some, ah, sample, ah, just some timing jitter, whether or not it's coming from the Roden-Schwarz

**Dave Jones:** generator or whether or not it's, ah, like a sample. It looks, it's jumping in quantized steps there. So I'd like to think that that's just, you know, um, ah, asynchronous because we're in, ah, timing mode. We're not in state analysis mode. State would be different if we were synchronizing something to an external clock.

**Dave Jones:** We're not. We're in timing analysis mode. So that is a good example actually of the single, um, sample rate, ah, you know, inherent, um, jitter you could potentially get in a, ah, asynchronous timing, ah, logic, by using, by timing I mean timing analysis of a logic analyzer.

**Dave Jones:** I'm sure I've done a video on that somewhere. Anyway, um, it works fine. It zooms in. There's no extra glitches. I've got the, ah, ah, the thresholds, um, set to the same, 1.4 volts. Everything's, everything's hunky dory, so there you go. Um, the Rigol 7000 works fine.

**Dave Jones:** There's something up with the Rigol 5000, but I do have an early possibly pre-production unit and pre-production software. Still couldn't figure out how to do that, um, firmware upgrade. Ah, John didn't know offhand, so yeah, um, and he, I thinks he, thinks he may have

**Dave Jones:** generated that license file incorrectly, so anyway, there you go. Um, yeah, Rigol 5000 has issues. I'm sure they'll, you know, eventually, ah, sort them out, but that's, that, ah, logic analyzer one, that was, yeah, it's really kind of nasty, so Rigol need to look into that one.

**Dave Jones:** Anyway, if, ah, you've got one of those Rigol 5000s and you can duplicate, ah, that, please let us know down below. Catch ya next time.
