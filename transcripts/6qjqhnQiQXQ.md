---
video_id: 6qjqhnQiQXQ
title: How to Measure Oscilloscope ADC Dynamic Range
url: https://www.youtube.com/watch?v=6qjqhnQiQXQ
source: youtube-asr
timestamps: {"0": 0, "1": 24, "2": 40, "3": 50, "4": 60, "5": 75, "6": 90, "7": 102, "8": 114, "9": 137, "10": 146, "11": 155, "12": 171, "13": 188, "14": 197, "15": 209, "16": 225, "17": 234, "18": 245, "19": 257, "20": 273, "21": 289, "22": 300, "23": 311, "24": 323, "25": 336, "26": 351, "27": 359, "28": 381, "29": 398, "30": 423, "31": 448, "32": 465, "33": 476, "34": 498, "35": 513, "36": 527, "37": 540, "38": 550, "39": 562, "40": 572, "41": 584, "42": 595, "43": 605, "44": 623, "45": 638, "46": 652, "47": 665, "48": 677, "49": 689, "50": 697, "51": 707, "52": 718}
---

**Dave Jones:** Hi, I'm going to show you how to measure the dynamic range of an oscilloscope. Now, this actually might be important because when you're analyzing, especially if you're a nerd on the EV blog forum like there are plenty of, um and you want to compare oscilloscopes and especially a 12-bit one like this new Rigol HDO 4000 series, then you know, if you're comparing like 12-bit scope and you want to compare the noise

**Dave Jones:** floor, you want to compare the effective number of bits and everything. Anyway, you know, you have to make sure you're doing apples to apples uh comparison. And one of the things you need to know is, well, what is the full-scale analog-to-digital converter range inside the scope?

**Dave Jones:** What's it actually, you know, doing? So, how do you measure that? Because most scopes, of course, will have like eight divisions vertically, but it could be uh more depending on the scope.

**Dave Jones:** This one actually has eight divisions. So, let's go down to 1 V per division here. You might think that the full-scale analog-to-digital converter range in this thing is those eight divisions.

**Dave Jones:** I.e., it's 1 V per division, so it's 8 V peak-to-peak full scale. But, that's not actually the case because as I showed in the unboxing and first play around with this video, you can see that actually um this is a triangle wave.

**Dave Jones:** You can see it's actually clipped at the top. And if I actually stop that and then go like this, you can see that it's not actually clipped. It's It does actually have some extra dynamic range, some extra sampling range outside of this window.

**Dave Jones:** But, how much more? Well, that's what we're going to find out here. So, the way you do this is you want to have a triangle wave. You can do it with a sine wave, but it's easier to see when waveforms are clipped with a triangle wave.

**Dave Jones:** So, what I've got here is my Rigol function generator. You can use Use the best function generator you've got, but I'm going to generate a 1 kHz signal. Doesn't matter about the frequency, really, but 1 kHz is just fine.

**Dave Jones:** Um and then we can actually set the uh peak-to-peak voltage here. Now, make sure you use the high uh Z or high impedance output. You don't want the 50 ohm termination cuz if you've used the 50 ohm termination, then uh you have to factor in uh the accuracy of the 50 ohm load termination and the actual divider and the 50 ohm output in this and all that sort of stuff.

**Dave Jones:** So, I prefer to use You can, but I prefer to use the high Z. We're not talking about anything high frequency here, so we don't have to worry about any of that um you know, signal integrity uh stuff.

**Dave Jones:** So, um high impedance output mode uh 1 kHz and I've actually got an 8.6 V peak-to-peak signal here. But, let's take this up to say 10 V peak-to-peak here, okay?

**Dave Jones:** And then if we view this over on the scope here, let's run it and then we'll go down here and we'll just verify that the that the accuracy is the same on this uh scope over here.

**Dave Jones:** There you go. The average volts peak-to-peak 10.0 1, right? So, it's pretty close to being spot on. So, we can you know, if both of these instruments are you know, roughly measure the same, then you can like we can get the accuracy spec of this thing and stuff like that.

**Dave Jones:** But, you know, if they both read the same, then well, that's good enough for Australia. Okay, so what we want to do now is actually uh we're with the 10 V signal, let's turn it back to 1 V per division.

**Dave Jones:** And you can see how it I goes over scale here. So, what we want to do is we want to press stop like this and then go up a voltage range and you can see that it's actually clipped.

**Dave Jones:** So, somewhere between that 10 V and 8 V is where our actual uh dynamic range lies. So, what we have to do now is adjust the um output voltage on the uh scope to actually see at what point it doesn't clip.

**Dave Jones:** So, I've already done this. I know what it is, but uh let's set it to say 8.8 V uh peak-to-peak. So, we uh you know, you lower it down, lower it down.

**Dave Jones:** So, let's do 8.8 volts. Let's put it back to 1 volt per division here, and let's run it. Okay, and then we stop it, and then we can go down a range, and you can see, "Oh, is it clipped or not?"

**Dave Jones:** Well, we can actually zoom in like this. We can adjust our position, but we because it chops off the waveform here, not all the scopes will operate uh the same way here, but we can just uh put that back, and so, we can zoom in, just reset that.

**Dave Jones:** And No, we can go up a range. So, there we go. We can get it to there, and then let's just zoom back in, and then we change our horizontal time base, and you can see that, "Oh, it's just just clipped there.

**Dave Jones:** Just clipped." Now, unfortunately, we can't just leave it zoomed in like this, and then just uh tweak our value slightly down here, because if we actually run it, okay, you'll see that either we can't see our signal or it's uh changed because we've changed the offset, okay?

**Dave Jones:** So, when we uh redo this, every time we do it, we have to reset the offset like this. So, we have to reset it back to zero position like this.

**Dave Jones:** So, I forgot to show you that up front. You've got to have zero uh position like this, because then we've got a symmetrical waveform uh like this, because if you have an offset, okay, look, I'll I'll show you that we can actually I'll adjust this.

**Dave Jones:** So, I'll put in a 10-volt signal peak to peak, and you can see that it's absolutely clipped there. But, if we adjust it like this, then uh wait, the triggering's a problem.

**Dave Jones:** But, if we adjust it like this, and we run it, then it's not clipping anymore cuz we've adjusted that because it's not outside the positive uh range of the um essentially the analog-to-digital converter, if you assume that like it's in the middle, uh for example.

**Dave Jones:** So, yeah, you need to actually center that like that, and then and only then can you actually get a proper uh true peak-to-peak reading. So, anyway, I'll go to, uh, 8.75.

**Dave Jones:** You can see there, that's what I've dialed in, and it measures pretty close to that. And this one will not, if I turn it back to 1 V, and I stop it, and then I adjust like that.

**Dave Jones:** And we zoom in. And if I expand that, we'll find that, bingo, 8.75 V there, there's no clipping. We can't actually get the, uh, value anymore, cuz it it calculates that, uh, from the screen, and it can't actually doesn't have a full, uh, sample to actually gather that data from, so it's no good anymore.

**Dave Jones:** But anyway, somewhere between 8.75 V and 8.8 V, uh, peak-to-peak, is our full-scale range of our, uh, analog-to-digital converter, or maybe not. It could actually be just where the input amplifier clips.

**Dave Jones:** But you can't really know that, uh, the true range of the analog-to-digital converter, unless you're, unless the manufacturer tells you what it is, you know, you've got the schematic, and you can reverse engineer it, or potentially you can feed in like a one-bit signal, like a one, one-bit, uh, amplitude level signal, until you actually see like one-bit change or something like, uh, but then you're down in the noise, and it's

**Dave Jones:** horrible, and everything. So, we're just going to assume that the range is, um, in this particular case, 8.75 V peak-to-peak. So, if we get our confuser out here, 8.75 V peak-to-peak, divided by 4,096, cuz that's a 12-bit, uh, converter here, that will give us an individual bit of 2.14, or thereabouts, millivolts, uh, per bit.

**Dave Jones:** And that's how, um, we can calculate, and then you can use this information to then compare oscilloscopes, cuz I've been downloading, uh, raw binary waveform, uh, data in a standardized way, so that the EV blog forum nerds can actually, uh, compare it with uh the equivalent Siglent uh 12-bit scope and stuff like that.

**Dave Jones:** So, um yeah, if you want to know what I've been doing, I've been basically uh to get um the raw data on this, I'll show you what I've uh I've well, that I've standardized on I've standardized on.

**Dave Jones:** Anyway, so what I've done is I've disconnected it like this and I've uh set it um well, I've done it with 1 meg samples and I've also done it with uh the full 250 meg and that's where you'll get the most uh data as well and I set the time base to 1 millisecond like this uh for example and I've got um and I've done it with both

**Dave Jones:** 50 ohm input termination on and also just 1 meg input termination, so just leaving it flapping around in the breeze and I've also done it with the full 200 MHz bandwidth and the 20 MHz bandwidth and then I save the binary data, the raw binary data to a USB uh stick.

**Dave Jones:** You can also save it as a uh CSV uh file as well. But, the forum nerds uh requested a binary file, so I've provided a binary file and yes, it does actually take a long time to save the data.

**Dave Jones:** Takes several minutes to save the full 250 itself. I stopped this, okay? There's 200 at 4 gig sample and you have to know the sample rate as well and that changes to 50 meg samples per second if you go to the 1 meg memory depth.

**Dave Jones:** So, you have to know that as well and ooh, is that a bug? Is that a bug? Cuz we're stopped. That should be 50 meg sample We're in stop mode at the moment.

**Dave Jones:** Will it Come Yeah, it changed back. There you go. There's a There's a little bug. Um it was showing it didn't automatically change that meg samples until I actually pressed start.

**Dave Jones:** I guess that's all right cuz it still had Oh, no, that's probably not a bug cuz it's it had it still had that existing data in memory cuz it was in stop mode.

**Dave Jones:** So, you don't I know, I'm going to No, I take that back. Sorry, Rigol. I don't think that's a bug. I think that's a feature in that the memory was still the data was still in the memory, so it should display should match the memory.

**Dave Jones:** So, yeah. I think it No, I'm going to take that back. Take it back. I won't edit that part out cuz that's interesting. Um but yeah, this you need to know the sample rate as well if you know if you're calculating all sorts of stuff.

**Dave Jones:** You can get the effective number of bits. As I said uh in the uh first impressions of this Rigol, only say it's greater than eight bits effective number of bits for 12-bit converter um scope.

**Dave Jones:** They don't give you any more information than that. So, anyway, um the forum nerds will be added. So, someone on the forum who's got the uh 12-bit uh Rigol um HD scope, then uh yeah, they can get the same measurements and then we've got the raw binary data and you can compare the two and argue until the cows come home about which one's better.

**Dave Jones:** Anyway, that is an interesting way to measure the uh dynamic range of the scope. So, you can do this on your um scope. Find out like like especially on an 8-bit converter, how many bits is it uh pissing away outside of the screen you're not capturing?

**Dave Jones:** Sometimes that's good. You want that, you know, because uh you want to like zoom into detail, but then you want to zoom out and capture data later. In this particular case, it would've been nice to I don't know select it or something, have a selection for like how much dynamic range you want.

**Dave Jones:** I don't know. Does any scope have that feature actually that allows you to adjust the uh dynamic range of the scope? Of course, on an 8-bit converter, it's like uh you you haven't you haven't got much to spare outside of the uh windows.

**Dave Jones:** In fact, you've only got 256 uh samples and your screen is going to be more than 256 pixels. So, like you don't even have a sample per pixel already, let alone outside.

**Dave Jones:** But when you got like a 12-bit converter like this one, you know, you got 4,096 bits to uh play with and uh and this is only a 800 um pixel screen from top to bottom.

**Dave Jones:** So, you know, you've got greater than one pixel per thing. Anyway, it'd be nice to be able to um adjust something like that. Let us know in the comments if you know a scope that's got that.

**Dave Jones:** But anyway, that's how you measure um the in theory the ADC dynamic range of a scope. Just put in a triangle wave is easy and just see where it clips.

**Dave Jones:** So, I hope you found that useful. If you did, give it a big thumbs up. As always, discuss down below and I'll link to the EVBlog forum thread where people are discussing, measuring, and comparing the noise floor of this thing.

**Dave Jones:** Catch you next time.
