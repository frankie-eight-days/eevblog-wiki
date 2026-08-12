---
video_id: RlwcdUnRw6w
title: EEVblog 1478 - Waveform Update Rate Shootout - Tek 2 Series vs Others
url: https://www.youtube.com/watch?v=RlwcdUnRw6w
source: youtube-asr
timestamps: {"0": 0, "1": 10, "2": 23, "3": 34, "4": 47, "5": 60, "6": 76, "7": 98, "8": 111, "9": 124, "10": 142, "11": 149, "12": 160, "13": 176, "14": 186, "15": 205, "16": 219, "17": 234, "18": 244, "19": 262, "20": 276, "21": 289, "22": 300, "23": 313, "24": 327, "25": 338, "26": 353, "27": 370, "28": 383, "29": 396, "30": 407, "31": 417, "32": 431, "33": 445, "34": 461, "35": 480, "36": 497, "37": 510, "38": 526, "39": 541, "40": 550, "41": 567, "42": 579, "43": 594, "44": 604, "45": 616, "46": 635, "47": 653, "48": 663, "49": 676, "50": 696, "51": 707, "52": 716, "53": 727, "54": 737, "55": 748, "56": 757, "57": 770, "58": 776, "59": 799, "60": 813, "61": 824, "62": 837, "63": 852, "64": 863, "65": 875, "66": 886, "67": 896, "68": 912, "69": 922, "70": 933, "71": 944, "72": 952, "73": 961, "74": 973, "75": 988, "76": 997, "77": 1014, "78": 1024, "79": 1031, "80": 1040, "81": 1052, "82": 1065, "83": 1074, "84": 1087, "85": 1100, "86": 1118, "87": 1127, "88": 1141, "89": 1154, "90": 1172, "91": 1185, "92": 1203, "93": 1215, "94": 1225, "95": 1236, "96": 1254, "97": 1276, "98": 1290, "99": 1299, "100": 1311, "101": 1332}
---

**Dave Jones:** Hi, just a quick video on the new Tektronix 2 series scope. Sorry, I haven't finished a full review. That'll actually but take some time. Leave in the comments down below if you want the full review.

**Dave Jones:** That's my plan. I just yeah, things didn't pan out unfortunately, but I've got the teardown video of course and I was going to throw this on the second channel as just a quick video over on EVblog 2 as I often do.

**Dave Jones:** You should be subscribed over there if you're not. Past 100,000 subscribers is where I put lots of secondary content, but hi. Everyone on Twitter the majority said that they wanted to see this on the main channel, so here it is.

**Dave Jones:** Main channel video. So this is not a review of the new Tektronix 2 series. It's just looking at waveform update rate for this thing and we're going to compare it with some other brands and I'm going to show you how to measure waveform updating.

**Dave Jones:** Let's go. Okay, let's measure the waveform update rate for this. Now I already know it's supposedly not that great according to Andy Ted in one of my second channel videos, but let's actually measure it cuz it's not on the data sheet.

**Dave Jones:** Unlike the series 3, which is here is the spec sheet for it 200 up to 280,000 waveforms per second, which is not too shabby. So what I've done is I've set the auxiliary output here to trigger and I'm feeding in a 1 MHz square wave like this.

**Dave Jones:** I've got nothing else turned on, so it's doing absolutely a bare-bones and we can actually measure the output. Here it is here. So this is the trigger output, so this is our waveform update rate in waveforms per second and you can see we're getting 1.9 K waveforms per second, but you'll notice that it's very bursty like that, right?

**Dave Jones:** Is that a word bursty? So in here we're getting all of our sample updates and I can freeze that and we can actually have a look and you know, we're getting like a dozen or more like updates.

**Dave Jones:** Each each one of those is a trigger and you can't see it Uh, cuz I don't have enough memory depth, but trust me, it's capturing that, uh, properly. So, anyway, we can redo that, and I'll show you that it That That is actually a very small pulse in there.

**Dave Jones:** So, it's not very consistent. It jumps around all the time, and this is, uh, consistent with like other like low-end scopes on the market, um, that don't have something like the Keysight Mega Zoom 4 ASIC, of course, which, uh, has phenomenal update rate.

**Dave Jones:** And well, we might actually do a comparison in a minute. Actually, uh, show you. So, we get like, uh, 20 or something, uh, waveform updates in there. Then we have to wait, what?

**Dave Jones:** Uh, 20, you know, 30 milliseconds, something like that, before we actually get another one. But there's other periods over here where it's much bigger. But as you can see, it's, uh, quite random.

**Dave Jones:** And if I do anything on the scope over here, you'll notice that if I try and move a waveform, it completely stops. Okay? There's no more updating there. And if I pinch and zoom that, boom, it is not updating.

**Dave Jones:** And of course, you can see it on the screen over here. It is just not updating. And well, you know, that's fair enough, cuz you're interacting with it. And if I drag the trigger level here, yeah, trigger level, same thing.

**Dave Jones:** No updating. And the absolute best waveform updating rate I'm able to get on this thing is 18.8k waveforms per second. And that's at, uh, like a real fast time base, like 10 nanoseconds per division, 250 points memory, um, and I'm also, uh, in normal, uh, trigger mode on this on the scope.

**Dave Jones:** So, I cannot get better than that. And if I slow down the time base, you'll notice this is still the same until I hit 100 nanoseconds per division here, which gives us, uh, 7 and 1/2 K waveforms per second.

**Dave Jones:** Then it jumps to 3.8 kHz here. And then if I go down lower than that, I've got to change my time base down 1.9 kHz at 400 nanoseconds. At 1 microsecond per division, we're now down to 760 hertz.

**Dave Jones:** So, yeah, it's it's not that great. But, uh we are getting increased memory here. Oh, one incredibly annoying thing. Check this out. If I want to set my manual memory depth, okay?

**Dave Jones:** I can go in the horizontal mode, manual, record length 25k. Okay? You think if I go up it'd go to 50k or something. Nope, goes to 26, 27, and then it adjust the micro time base over here.

**Dave Jones:** It adjust My horizontal scale is now 1.24 microseconds per division. Why? Why? I don't want that rubbish. And if I go in here like this and I want to update the uh K points per second, then let's just say I wanted like uh you know, a low like 1,000 points.

**Dave Jones:** It's actually K points. I've got to go no for to change the scale over here and enter. Okay? So, we're now 1K point. But, the annoying thing is is that it doesn't matter what I do.

**Dave Jones:** I can't seem to have a fixed record length of 1K points. Um it doesn't matter whether or not I have the sample rate changes affect horizontal scale or record length.

**Dave Jones:** Watch this. If I change my time base, okay? It's changing my K points. Right? I've told it no. I only want 1K point. So, I've got to This is manual mode.

**Dave Jones:** Okay? Why? Why? This is just ridiculous. Check this out. This is crazy. I'm at 1 microsecond per division, okay? And I want to change my record length. I want to actually I I I I don't want 25.

**Dave Jones:** I only want 1K. Thank you very much, right? And I put 1K in and it's changed me back to 40 nanoseconds per division because I've got this sample rate changes affect horizontal scale.

**Dave Jones:** I can change this to record length. I can change this back to uh 1 microsecond per division. I can go back in here and I can go one K points like that and it's taken me back to 40 nanoseconds per division.

**Dave Jones:** I can't set a manual bloody memory depth on this thing and then change horizontal ranges. It's ridiculous. Now, just remember when we measured that frequency there to calculate the effective number of waveforms per second, that doesn't include the dead time.

**Dave Jones:** That's just what it's capable of if there was no dead time, but thankfully the Tektronix actually gives us a display of the wave for effective waveforms per second. Here it is.

**Dave Jones:** It gives us the number of acquisitions, which is an acquisition is a complete waveform acquisition. So, this is the number of waveforms per second and you can see it counting up 3,000, 4,000, 5,000.

**Dave Jones:** So, that's probably about 2,000 odd waveforms per second. And this is at the maximum time base Well, this is 10 nanoseconds. And you'll notice that it resets every time I change the horizontal time base.

**Dave Jones:** So, we can actually get a stopwatch out and at the different time bases. So, this is 40 nanoseconds per division. Sorry, it's off the screen. You can't see it.

**Dave Jones:** There's 100 nanoseconds per division and as we saw before, we go to one microsecond per division. There we There we go. Ready? Let's start again. There you go. So, you can probably use your own stopwatch and count those yourself the number of waveforms per second.

**Dave Jones:** It's not many. We're talking about 1,000 and that took like 10 seconds or something. Okay, so I can get a stopwatch here and let me try this at 10 nanoseconds per division and go.

**Dave Jones:** And then we can actually get a figure for the real the maximum number of waveforms per second. So, let's give that say 30 seconds and I'm going to say 30 seconds is about now, 43,000 acquisitions in 30 seconds.

**Dave Jones:** So, get the confuser out. That works out to about 1,400 waveforms per second. That's the maximum this thing can Well, actually does in practice with the sort of like de facto reference standard at 10 MHz input with 10 nanoseconds per division at 250 points down there.

**Dave Jones:** So, yeah, it's not great, is it? Anyway, we've got our 18K waveform updates per second. So, we've got our maximum. Okay, so I'll leave it about there. Well, actually I'll dial it one back like this and we'll be able to see as we do various things on the screen.

**Dave Jones:** Now, if I turn on the other channels, let's go to three. Whoa, look at that. Extra channels really slows it. So, yeah, even if I turn channel four on here, it it does that.

**Dave Jones:** So, let's turn channel four off and bingo, yeah, we do if we have a single channel, we do actually get not faster waveform updates per second, but less of a dead period a dead time actually between bursts of acquisitions.

**Dave Jones:** Anyway, let's turn our cursors on, shall we? So, we'll go up here. Cursors on. Yeah, that adds a little bit of dead time. Turn our cursors back off. And we'll do some measuring as well.

**Dave Jones:** Let's measure, you know, RMS and peak to peak and stuff like that. And uh hasn't slowed it down it No, it hasn't slowed it down a huge amount, but there is some extra dead time there.

**Dave Jones:** Then, if we turn on, say FFT, cuz that's always a good example of like some really advanced stuff. And whoa, there we go. It slows down for a bit while it's actually thinking about it and doing something internally to change into FFT mode and set it up and everything.

**Dave Jones:** But once it you know, once it actually turns on the FFT, it does actually get back to while not as good as not having all these things on. It's actually still not hugely bad.

**Dave Jones:** Now, of course, the update rate really doesn't have anything to do with like how responsive the scope is in actual use. In actual use, it's actually um you know, it's it's a fairly responsive scope even with FFT and cursors and measurements and everything else on.

**Dave Jones:** So, it's actually it's not too bad. But, yeah, for a new architecture that um well, what has been 15 years since the last tech arc in like low-end tech architecture?

**Dave Jones:** I believe around about that sort of uh period for the MSO 2000 series. Um but, yeah, this new Lexington architecture with the Xilinx Zynq processor, it's just it's quite frankly uh rather disappointing.

**Dave Jones:** Um I just didn't really expect it to be that poor. I expected new scope to have, you know, a decently fast update rate. It's a shame because the 3 series, even though I don't have one, um and I've never measured it on it, um apparently has up to 280,000 waveform updates per second.

**Dave Jones:** And this new one Yeah, it's cheaper, but this low-end Keysight 1000 series has 200,000 per second. So, uh And interestingly, even with FFT and cursors and everything else happening here, we do actually get more updates in an actual burst like this.

**Dave Jones:** So, you know, then we'll get in, you know, like 20 odd before or something like that. So, yeah, that's curious. But, you can see that we're 50 milliseconds per division.

**Dave Jones:** So, we're getting like 150 milliseconds or something, you know, dead time where it's not acquiring anything at all. Okay, just to show you the difference here, I'll compare the new 2 series with my Keysight 1000 series.

**Dave Jones:** I believe this is now 200,000 waveforms updates per second, but the one I've got here is only 50,000 because the MegaZoom 4 in here is capable of 1 million per second, but you they don't enable that unless you spend more and more money as all the manufacturers do.

**Dave Jones:** It's not just tech. Anyway, so this one will definitely do a million per second, but I'll just show you this little puppy here, which is you know, the low end of the Keysight range.

**Dave Jones:** And we'll compare the difference. So I've still got the tech 2 series out here and there you go. That's what we get in. That's 100 milliseconds per division. We're getting our little burst there.

**Dave Jones:** And so we can go in and we can measure our burst the frequency is now up here. So that was the you probably just saw it. I can freeze that and that's the 18 kHz that we get there.

**Dave Jones:** Okay, so we go back to 100 milliseconds per division. So let me now change this over and I won't touch anything else here. So auxiliary out. I've actually set my function generator output on here to trigger output.

**Dave Jones:** That's a software feature in here. Not all scopes by the way have the ability to output a trigger signal. So if your one can't, then it's more difficult to like measure the waveform update rate.

**Dave Jones:** You have to do it in roundabout ways. Um, but anyway, let's now plug that in and boom! Look what's happened. Look at this. There's hardly any dead time. There's just this little boop boop.

**Dave Jones:** This is all This is all Look at this. Here it is. And there it is. 50,000 50k samples per second. There it is, right? So 50,000 waveform updates per second.

**Dave Jones:** And you can see that there's just a little bit of we're triggering on the one, but there's a little bit of like jittering in there cuz the ASIC's doing, you know, whatever.

**Dave Jones:** But look, that is the difference, right? So it's almost always sampling, right? Look, just all the time. There's no dead periods. And sure if I, you know, tweak the vertical and stuff like that, it's still, you know, there is some extra dead time in there to do, you know, stuff like that, change the vertical divisions and change the horizontal and stuff like right.

**Dave Jones:** I get little bits of dead time in there, but it's basically it's pretty much sampling, especially when you're not touching it. It's sampling all the time. And I've turned on my measurements down here, and I can turn my cursors on as well, and I can fiddle fiddle with the cursors.

**Dave Jones:** And even when I'm fiddling with the cursors, right, moving the cursors around in that waveform, there's like there's really no difference in the waveform there. Let's see if there's a little bit of difference in the jitter.

**Dave Jones:** No. See, there's no I'm I'm moving that cursor across there, doing that. It's only if I start Well, no, actually you can't even see that because there's so little Oh, yeah, yeah, we got we got one.

**Dave Jones:** There's so little dead time in this thing that yeah, you just you really don't notice it unless you're, you know, really changing ranges very fast. But even then, it's this like orders of magnitude better than the new architecture Tektronix.

**Dave Jones:** And this is a 12 13, I think it's now. I think the MegaZoom 4 ASIC in this is now 13 years old. Come on, uh Keysight. When are you going to I'm doing Agilent.

**Dave Jones:** Come on, Agilent. When are you going to release the MegaZoom 5? But yeah, um there you have it. So, this will only slow down if we go at slower time bases cuz it's got to fill the it's going to take time to fill the memory up.

**Dave Jones:** And the uh Keysight uses automatic uh memory. So, you know, we don't know exactly how much it's using. But anyway, I'm at 100 microseconds per division. Sorry, I can't show you this and show you the detail on the frequency there.

**Dave Jones:** But uh trust me. And if I go up to the fastest speed, that's uh 2 nanoseconds per division, it's still the same 52 kHz signal. So, if I slow it down 200 ns, 500, right?

**Dave Jones:** It starts getting a bit slower. And we can whoop do that. There you go. So, at 2 microseconds, that's 22.7 kHz. And let's go to 50 microseconds. We'll have to single shot capture that.

**Dave Jones:** 1.8 uh kHz. So, you know, the slower it gets because we've got uh slower time base on here means it's got to fill up the memory, and it's got to take that amount of time.

**Dave Jones:** It just, you know, it's all scopes are going to slow down. And the the million waveform updates uh per second on these Keysight scopes means nothing if you're using it at a slow time base, and it's got to fill all that memory.

**Dave Jones:** It's you know, can't beat the laws of physics, Captain. Just to show you that in the real world, I've got a Tek's own demo board actually, uh the MDO demo board.

**Dave Jones:** I've got the rare anomaly uh setting, so I'm not sure of the exact details of that. You can probably go and look up uh info somewhere. But anyway, there you go.

**Dave Jones:** I've got a hold off in there of uh 2.2 microseconds to try and to get the display stable, and hopefully you can see all that Well, well, yep. Oh, yep.

**Dave Jones:** Yep. Yep. There should be like a runty pulse, an anomaly. Whoop, yep. See it? See it? This is the fast update rate of the Keysight. Anyway, so you can see Yep.

**Dave Jones:** Yep. Saw another one. Yep. Got one there. Right, so you can see that. Now, I'll do the same signal on the Tek. There you go. Exactly the same uh settings, 2.2 microseconds uh hold off time uh so that you know, so that it doesn't otherwise you get jittery trigger and stuff like that.

**Dave Jones:** So, you got to hold off on uh complex waveforms like this. But yeah, I'm waiting for the cows come home. Um I'm not I'm not seeing anything. Not seeing any jitteries.

**Dave Jones:** Not seeing any runt pulses. Nothing. Not a sausage. And that's due to the uh small number of uh waveform updates. But wait. No, I think I got one. I think I might I think I might have captured one there.

**Dave Jones:** But yeah, wow. You got to wait a while. Um and yeah, it's a purely a uh percentage chance of it happening based on the Well, did I see something there?

**Dave Jones:** I was too busy looking at the camcorder. I thought I saw it out the corner of my eye. But yeah, it's a basically a percentage chance of capturing something.

**Dave Jones:** Uh whoop. Maybe. Maybe. But yeah, you can see the real difference there. And I swapped it over to the frequent anomaly and you can see it's picking up I mean sorry, yeah.

**Dave Jones:** See? So, this is picking up the frequent anomaly there. You know, it's once every couple of seconds, maybe 5 seconds. This one's going up. There we go. There we go.

**Dave Jones:** Right. And we'll do the same on Keysight. Swap it over. Haven't changed anything and we get it all the time. It's like it's constantly there. It is constantly there.

**Dave Jones:** So, then you can go, "Aha, I got you, you little mongrel." And then you can set up a runt pulse trigger or some other triggering to actually capture that sort of thing.

**Dave Jones:** Yeah, so that really illustrates the difference that waveform updates can make. And yeah, I'm just disappointed in the new tech architecture. I you know, I jeez. Yeah, I expected better.

**Dave Jones:** And even if you compare it with this Siglent SDS 1104 XE, you know, nothing special like low-end scope and look, you can readily readily see it. No problems whatsoever.

**Dave Jones:** Because it's got a better update capture rate than the new Teledyne LeCroy architecture. Whiz bang two series. Disappointing. And the old firmware 50k waveform version of the 1000 X series, you see that frequent anomaly is just it's showing up all the time.

**Dave Jones:** Whereas we were waiting, you know, up to like 5 seconds at one point. I you know, it's 3 5 seconds or something on the two series tech to even see anything.

**Dave Jones:** And this is like multiple times per second. Boom. It's just so easy to detect here. Look, it's nuts. And this old Rigol DS2000 series, don't know how old it is now, but jeez, can't remember last time I did a video on this.

**Dave Jones:** And there you go. Heaps. But here's the thing, right? Once you include once you increase your memory points, okay, it's going to go down. So, we're on fixed 14k point memory there, which is heaps for just general use and screen.

**Dave Jones:** So, really when you're operating your scope, pro tip is that, you know, you should choose the lowest amount of memory for the fastest update rate possible for a given time base, and that'll help you detect infrequent stuff like this, which is going to rely on sheer statistics of whether or not it's actually picked up in the acquisition or not.

**Dave Jones:** Of course, if you got a scope that has zero dead time, it's just acquired it all the time, and it's going to present that information to the screen. It actually decimates it because you can't, even on the Keysight over here, right?

**Dave Jones:** You know, million waveform updates per second, you're not actually updating, refreshing the screen a million times a second, that's just ridiculous. So, what it does is actually takes those samples and effectively like combines them into like a displayed version of that waveform periodically.

**Dave Jones:** So, I don't know how often it actually, you know, it does that, but then it's able to pick up stuff like that and actually display it. So, we change that to 140K points here, and you're still seeing it, okay?

**Dave Jones:** Let's go to 1.4 meg points, and there you go, less frequent because the update rate is going to drop based on the amount of memory it's got to process.

**Dave Jones:** 14 meg points, uh, whoa, whoa, whoa, did we get one there? I don't know. You're going to have a hard time seeing it now, so don't always, oh, well, there we go.

**Dave Jones:** Don't always think it's the best thing to actually set your scope to the maximum memory depth. It's not always good. Anyway, I hope you enjoyed that little comparison of waveform update rates and how to actually measure them, and it's, yeah, just a tad disappointing from the new architecture Tech 2 Series.

**Dave Jones:** Like, I don't know, why is it a hardware limitation? I mean, I can't understand how it would be a marketing position thing to actually deliberately that. I don't know, Tech will have to tell us because the next one up in the series, three series as I said, has a maximum of supposedly maximum of 280 thousand per second.

**Dave Jones:** So, yeah, that's like that's like really good and modern. But the new two series for that aspect it yeah, it gets a thumbs down. It's disappointing. But as I said, it's actually a reasonably responsive scope.

**Dave Jones:** And when you turn things on it doesn't really slow it down all that much. So, as I said, waveform update rates doesn't actually correlate into a slower slower user interface experience.

**Dave Jones:** It just means more dead time. Cuz it depends on how you prioritize the thing in the design of the user interface in the acquisition engine whether or not you're going to prioritize the user interface which you should.

**Dave Jones:** You don't want a slow operating scope. But then also you want the fast update. But that's why something like the Keysight does it all in an ASIC so that it you know, it doesn't matter what you turn on FFTs or any of the other cursors and measurements and all the other processing functions, it it doesn't matter because the main processor is not handling that sort of stuff.

**Dave Jones:** But you saw the dead time on the Tech here. It was quite substantial. But you know, it is still a fairly responsive scope. You've just got to live with the dead time.
