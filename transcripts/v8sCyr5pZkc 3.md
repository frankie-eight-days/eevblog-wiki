---
video_id: v8sCyr5pZkc
title: EEVblog #1324 - Oscilloscope Reference Waveforms are USEFUL
url: https://www.youtube.com/watch?v=v8sCyr5pZkc
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 31, "3": 45, "4": 62, "5": 74, "6": 86, "7": 102, "8": 116, "9": 129, "10": 141, "11": 153, "12": 167, "13": 183, "14": 197, "15": 209, "16": 227, "17": 240, "18": 258, "19": 272, "20": 289, "21": 305, "22": 319, "23": 331, "24": 346, "25": 362, "26": 377, "27": 388, "28": 401, "29": 413, "30": 430, "31": 444, "32": 454, "33": 471, "34": 484, "35": 500, "36": 513, "37": 525, "38": 538, "39": 552, "40": 568, "41": 582, "42": 598, "43": 611, "44": 626, "45": 638}
---

**Dave Jones:** Hi, just a quick oscilloscope tip video. Now, modern digital scopes are of course very handy because they've got single shot capture capability and allows you to capture multiple waveforms and display them on the screen and of course get time correlated information of how

**Dave Jones:** they switch between one another like this and then you could go in there and look at the timing differences and count your divisions and use your cursors and do all sorts of other measurements and of course modern scopes I recommend like

**Dave Jones:** a four channel scope uh these days because well, even entry level ones like sub $400 scopes there, you can get like four channel ones. So, yeah, it's handy to be able to look at multiple signals, but the problem is modern electronics

**Dave Jones:** unfortunately is all this modern surface mount rubbish. Of course, the problem with that is if you want to say probe two signals at once, you've got to use one hand to hold both probes like this and hold your tongue at the right angle so

**Dave Jones:** that you've got the other hand free to operate the scope or you know, power the unit up or do whatever and of course, you can really slip and come a cropper and you can short things out and you

**Dave Jones:** know, generally ruin your day. Not to mention if you want to measure more than two signals. So, what do you do if you want to measure more than one signal and get the time correlation between them, but you've only got one hand to do it

**Dave Jones:** and you don't have like any ready access points to actually use your easy hook for example to get in there and like through and actually clip onto there so you've got one hand free like that and the other and bingo, now we can do it.

**Dave Jones:** What if you need to get in there with both of these points and uh tongue at the right angle? Well, now of course, you could actually get in there and like you know, solder a little wire up from whatever part that you

**Dave Jones:** wanted to measure whatever signal uh test point that you want to measure, but you know, it might be like a tiny pin on a little quad flat pack or a little 0402 component or something like that, you know, like just really annoying stuff

**Dave Jones:** and you might have to physically take the board out or bring your soldering iron over to it or, you know, whatever you need to do. That just can be like a really annoying solution and you might end up shorting things out or, you know,

**Dave Jones:** ruining your board or doing whatever. You just want to probe the damn thing, You just want to take a couple of seconds to probe it. So, how can you probe two signals with only one hand? Well, I got a tip for you. Huh. Get it?

**Dave Jones:** I'm here all week. Now, the first thing to do is find like a readily available reference waveform point that you can trigger off. Uh for example, if you're trying to like repower uh this product with the uh main switch under here, for

**Dave Jones:** example, then like a power supply can often be a good thing uh to hook hook onto. So, the 3.3 V uh digital power supply here, bingo. Look at these, we got through-hole caps up here, so we can actually uh clip onto

**Dave Jones:** the output voltage of the 3.3 V rail. No worries. So, in this case, we set up our scope for uh triggering off a channel one, you know, positive-going edge or that sort of stuff, so it's all happening. We're good

**Dave Jones:** to go. So, we now have a rising edge reference point, which will be our power supply that we can trigger off and then get time correlation uh between any other signals we want to probe. Now, of course, we can just probe them one at a

**Dave Jones:** time and do a single-shot capture like this, for example, and we get this waveform here, and then we do another one, and then we single-shot capture again, and then we probe another point here, okay? But, we can see those

**Dave Jones:** waveforms, but the problem is, of course, that we're not going to be able to see the time correlation between them because we have to trigger from the waveform under test. We don't have a like a separate reference that we can

**Dave Jones:** actually compare the two. Right, so if we take as channel one for example and trigger off our 3.3 V rail here, bingo, we now have a reference waveform on channel one that always triggers at the same point. So now we can use channel

**Dave Jones:** two to actually probe our two other signals. But how do we measure two signals with one channel? Aha, this is where a really useful feature of most modern scopes comes in and that's reference waveforms. So on this 1000 X

**Dave Jones:** series Keysight, we actually go into analyze up here and our features and bingo, we've got two reference waveforms. Some scopes might have like five or 10 reference waveforms or something like that, but two very handy. So we can actually choose our reference

**Dave Jones:** waveform like that and this is our feature. We enable that and then we can save and clear waveforms that we actually capture. See I've got one there previously. So let's clear any existing reference waveforms there and now we're

**Dave Jones:** ready to probe with our second channel our first signal that we want to capture. All right, I've probed my first tricky point down there and I've still got one hand free and I'm not going to accidentally short anything out. Let's

**Dave Jones:** go single shot capture. Let's power it on and you'll see that bingo, and you'll see that we have triggered off our channel one here, which is the 3.3 V rail and you can see that the signal that we've actually

**Dave Jones:** measured immediately went high like that. Although you can of course zoom into that and actually see you can just go zero like that. Zoom in and see yep, they did actually ramp up at the same time. So we want to actually

**Dave Jones:** select the source now that we want to save. We want to save channel two and bingo, we just gave a save to one like that and you'll notice that's changed color up there and our reference waveform has now been stored. So, what

**Dave Jones:** we can then do is simply move our waveform up here and we can capture another one. Let's do it again. So, this reference waveform here will stay there even if we go single shot. Capture again. It's going to stay there as our

**Dave Jones:** reference as long as you don't touch the time base or anything else. Now, we can probe and capture the second signal. Now, let's probe the second signal. It looks like the same spot, but it's actually not. It's like one or two

**Dave Jones:** millimeters apart. Um that's what makes it really tricky to probe both of these points at the same time with one scope probe, especially when you've got like everything in the way like heat sink and crystal here. There there are This is

**Dave Jones:** actually a real genuine example. I tried to troubleshoot these two signals actually repairing this uh speaker and I wanted to do this. I can't like hold both of the probes in there at the same time, uh not short anything out, not

**Dave Jones:** slip, and you know, be able to operate the scope and the uh power switch at the same time. So, yeah, this is really handy. So, anyway, we're probing that and let's switch it back on again. Here we go.

**Dave Jones:** And bingo, that Trust me, that is a different point. I I know I probably could have chosen a better example uh than this, but trust me, these are two different signals even though they're doing exactly the same thing. Um so, you

**Dave Jones:** have to watch my previous video to know, but trust me, if this signal was different, uh then you'd be able to see Let let's say it went uh high here, for example, then you'd be able to see that

**Dave Jones:** it went high like, you know, 250 or 300 milliseconds like before this one did. But, this is helpful because in this particular case, I've actually determined that these signals are match. They do the same thing even though this

**Dave Jones:** is two separate signal points. So this actually, even though they look identical, this actually gives me valuable troubleshooting information about what's happening in my circuit. They don't have to be different. They could be the same. That could be the

**Dave Jones:** result that you're interested in. And just to show you that they are actually different, we can actually go over to here and we can see a subtle difference in timing between them. If we zoom in like that, aha, look. This one is doing

**Dave Jones:** some sort of like analoggy ramp up funny business back down and then back up. Whereas the other signal we were measuring is more digitally. So you can see well this is actually occurring, you know, millisecond or two milliseconds

**Dave Jones:** before the other one. So they seem similar on the surface by looking at them, but we can actually go in there and see subtle differences between timings. And this is not the best example, of course. Or we can measure

**Dave Jones:** another signal here and then we can see, aha, well if you zoom right in there, you can see, aha, this one is doing something there. So we can go in and actually zoom in and take a look what's

**Dave Jones:** going on there. So you can see that something happened there. Woah, we don't unfortunately our memory depth here is just not we can see something happened there at, you know, at what 5 microseconds or something like that. But there's

**Dave Jones:** obviously a little pulse in there before this thing happens. So this allows us to really like troubleshoot differences between signals. And of course we can use multiple reference waveforms. This scope has two. And of course we could actually save that up.

**Dave Jones:** Ah, pushed the wrong button. I was going to say say we could I should have actually changed that to reference waveform two. Anyway, we could change that to another reference there and we could have multiple references on the screen and

**Dave Jones:** you can do this for multiple signals. So, even though we've got our four channel scope here, which is more than capable of like viewing in this particular case three signals at the a correlation between three separate signals, the fact that we've got all

**Dave Jones:** this surface mount stuff down here that's really difficult to probe and hold the probes on, reference waveforms can just be a really handy way to actually do that. So, yes, I know there's ways you can get like these big

**Dave Jones:** things to like hold your probes at certain points and stuff like that, but as you can see, don't really have room to do that and it gets like really messy. So, this is just a quick and easy method using reference waveforms just to

**Dave Jones:** get yourself out of a trouble and not have to go in there and solder stuff onto your board cuz you might have to like to do that, you might have to disassemble it or you know, something like that. So, anyway, I hope you found

**Dave Jones:** that tip useful and if you did, please give it a big thumbs up and as always discuss down below. Catch you next time.
