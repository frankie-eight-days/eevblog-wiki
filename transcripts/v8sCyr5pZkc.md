---
video_id: v8sCyr5pZkc
title: EEVblog #1324 - Oscilloscope Reference Waveforms are USEFUL
url: https://www.youtube.com/watch?v=v8sCyr5pZkc
source: youtube-asr
timestamps: {"0": 0, "1": 27, "2": 38, "3": 64, "4": 74, "5": 97, "6": 107, "7": 131, "8": 143, "9": 149, "10": 160, "11": 173, "12": 184, "13": 194, "14": 206, "15": 224, "16": 235, "17": 255, "18": 269, "19": 287, "20": 298, "21": 309, "22": 319, "23": 334, "24": 343, "25": 359, "26": 372, "27": 383, "28": 399, "29": 419, "30": 432, "31": 441, "32": 461, "33": 471, "34": 482, "35": 493, "36": 506, "37": 521, "38": 533, "39": 550, "40": 561, "41": 575, "42": 600, "43": 620, "44": 636}
---

**Dave Jones:** Hi, just a quick oscilloscope tip video. Now, modern digital scopes are of course very handy because they've got single shot capture capability and allows you to capture multiple waveforms and display them on the screen and of course get time correlated information of how they switch between one another like this and then you could go in there and look at the timing differences and count your divisions and use your cursors and

**Dave Jones:** do all sorts of other measurements and of course modern scopes I recommend like a four channel scope uh these days because well, even entry level ones like sub $400 scopes there, you can get like four channel ones.

**Dave Jones:** So, yeah, it's handy to be able to look at multiple signals, but the problem is modern electronics unfortunately is all this modern surface mount rubbish. Of course, the problem with that is if you want to say probe two signals at once, you've got to use one hand to hold both probes like this and hold your tongue at the right angle so that you've got the other hand free to

**Dave Jones:** operate the scope or you know, power the unit up or do whatever and of course, you can really slip and come a cropper and you can short things out and you know, generally ruin your day.

**Dave Jones:** Not to mention if you want to measure more than two signals. So, what do you do if you want to measure more than one signal and get the time correlation between them, but you've only got one hand to do it and you don't have like any ready access points to actually use your easy hook for example to get in there and like through and actually clip onto there so

**Dave Jones:** you've got one hand free like that and the other and bingo, now we can do it. What if you need to get in there with both of these points and uh tongue at the right angle?

**Dave Jones:** Well, now of course, you could actually get in there and like you know, solder a little wire up from whatever part that you wanted to measure whatever signal uh test point that you want to measure, but you know, it might be like a tiny pin on a little quad flat pack or a little 0402 component or something like that, you know, like just really annoying stuff and you might have to physically take

**Dave Jones:** the board out or bring your soldering iron over to it or, you know, whatever you need to do. That just can be like a really annoying solution and you might end up shorting things out or, you know, ruining your board or doing whatever.

**Dave Jones:** You just want to probe the damn thing, You just want to take a couple of seconds to probe it. So, how can you probe two signals with only one hand?

**Dave Jones:** Well, I got a tip for you. Huh. Get it? I'm here all week. Now, the first thing to do is find like a readily available reference waveform point that you can trigger off.

**Dave Jones:** Uh for example, if you're trying to like repower uh this product with the uh main switch under here, for example, then like a power supply can often be a good thing uh to hook hook onto.

**Dave Jones:** So, the 3.3 V uh digital power supply here, bingo. Look at these, we got through-hole caps up here, so we can actually uh clip onto the output voltage of the 3.3 V rail.

**Dave Jones:** No worries. So, in this case, we set up our scope for uh triggering off a channel one, you know, positive-going edge or that sort of stuff, so it's all happening.

**Dave Jones:** We're good to go. So, we now have a rising edge reference point, which will be our power supply that we can trigger off and then get time correlation uh between any other signals we want to probe.

**Dave Jones:** Now, of course, we can just probe them one at a time and do a single-shot capture like this, for example, and we get this waveform here, and then we do another one, and then we single-shot capture again, and then we probe another point here, okay?

**Dave Jones:** But, we can see those waveforms, but the problem is, of course, that we're not going to be able to see the time correlation between them because we have to trigger from the waveform under test.

**Dave Jones:** We don't have a like a separate reference that we can actually compare the two. Right, so if we take as channel one for example and trigger off our 3.3 V rail here, bingo, we now have a reference waveform on channel one that always triggers at the same point.

**Dave Jones:** So now we can use channel two to actually probe our two other signals. But how do we measure two signals with one channel? Aha, this is where a really useful feature of most modern scopes comes in and that's reference waveforms.

**Dave Jones:** So on this 1000 X series Keysight, we actually go into analyze up here and our features and bingo, we've got two reference waveforms. Some scopes might have like five or 10 reference waveforms or something like that, but two very handy.

**Dave Jones:** So we can actually choose our reference waveform like that and this is our feature. We enable that and then we can save and clear waveforms that we actually capture.

**Dave Jones:** See I've got one there previously. So let's clear any existing reference waveforms there and now we're ready to probe with our second channel our first signal that we want to capture.

**Dave Jones:** All right, I've probed my first tricky point down there and I've still got one hand free and I'm not going to accidentally short anything out. Let's go single shot capture.

**Dave Jones:** Let's power it on and you'll see that bingo, and you'll see that we have triggered off our channel one here, which is the 3.3 V rail and you can see that the signal that we've actually measured immediately went high like that.

**Dave Jones:** Although you can of course zoom into that and actually see you can just go zero like that. Zoom in and see yep, they did actually ramp up at the same time.

**Dave Jones:** So we want to actually select the source now that we want to save. We want to save channel two and bingo, we just gave a save to one like that and you'll notice that's changed color up there and our reference waveform has now been stored.

**Dave Jones:** So, what we can then do is simply move our waveform up here and we can capture another one. Let's do it again. So, this reference waveform here will stay there even if we go single shot.

**Dave Jones:** Capture again. It's going to stay there as our reference as long as you don't touch the time base or anything else. Now, we can probe and capture the second signal.

**Dave Jones:** Now, let's probe the second signal. It looks like the same spot, but it's actually not. It's like one or two millimeters apart. Um that's what makes it really tricky to probe both of these points at the same time with one scope probe, especially when you've got like everything in the way like heat sink and crystal here.

**Dave Jones:** There there are This is actually a real genuine example. I tried to troubleshoot these two signals actually repairing this uh speaker and I wanted to do this. I can't like hold both of the probes in there at the same time, uh not short anything out, not slip, and you know, be able to operate the scope and the uh power switch at the same time.

**Dave Jones:** So, yeah, this is really handy. So, anyway, we're probing that and let's switch it back on again. Here we go. And bingo, that Trust me, that is a different point.

**Dave Jones:** I I know I probably could have chosen a better example uh than this, but trust me, these are two different signals even though they're doing exactly the same thing.

**Dave Jones:** Um so, you have to watch my previous video to know, but trust me, if this signal was different, uh then you'd be able to see Let let's say it went uh high here, for example, then you'd be able to see that it went high like, you know, 250 or 300 milliseconds like before this one did.

**Dave Jones:** But, this is helpful because in this particular case, I've actually determined that these signals are match. They do the same thing even though this is two separate signal points.

**Dave Jones:** So this actually, even though they look identical, this actually gives me valuable troubleshooting information about what's happening in my circuit. They don't have to be different. They could be the same.

**Dave Jones:** That could be the result that you're interested in. And just to show you that they are actually different, we can actually go over to here and we can see a subtle difference in timing between them.

**Dave Jones:** If we zoom in like that, aha, look. This one is doing some sort of like analoggy ramp up funny business back down and then back up. Whereas the other signal we were measuring is more digitally.

**Dave Jones:** So you can see well this is actually occurring, you know, millisecond or two milliseconds before the other one. So they seem similar on the surface by looking at them, but we can actually go in there and see subtle differences between timings.

**Dave Jones:** And this is not the best example, of course. Or we can measure another signal here and then we can see, aha, well if you zoom right in there, you can see, aha, this one is doing something there.

**Dave Jones:** So we can go in and actually zoom in and take a look what's going on there. So you can see that something happened there. Woah, we don't unfortunately our memory depth here is just not we can see something happened there at, you know, at what 5 microseconds or something like that.

**Dave Jones:** But there's obviously a little pulse in there before this thing happens. So this allows us to really like troubleshoot differences between signals. And of course we can use multiple reference waveforms.

**Dave Jones:** This scope has two. And of course we could actually save that up. Ah, pushed the wrong button. I was going to say say we could I should have actually changed that to reference waveform two.

**Dave Jones:** Anyway, we could change that to another reference there and we could have multiple references on the screen and you can do this for multiple signals. So, even though we've got our four channel scope here, which is more than capable of like viewing in this particular case three signals at the a correlation between three separate signals, the fact that we've got all this surface mount stuff down here

**Dave Jones:** that's really difficult to probe and hold the probes on, reference waveforms can just be a really handy way to actually do that. So, yes, I know there's ways you can get like these big things to like hold your probes at certain points and stuff like that, but as you can see, don't really have room to do that and it gets like really messy.

**Dave Jones:** So, this is just a quick and easy method using reference waveforms just to get yourself out of a trouble and not have to go in there and solder stuff onto your board cuz you might have to like to do that, you might have to disassemble it or you know, something like that.

**Dave Jones:** So, anyway, I hope you found that tip useful and if you did, please give it a big thumbs up and as always discuss down below. Catch you next time.
