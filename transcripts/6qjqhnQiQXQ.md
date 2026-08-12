---
video_id: 6qjqhnQiQXQ
title: How to Measure Oscilloscope ADC Dynamic Range
url: https://www.youtube.com/watch?v=6qjqhnQiQXQ
source: youtube-asr
timestamps: {"0": 0, "1": 12, "2": 26, "3": 42, "4": 54, "5": 71, "6": 84, "7": 98, "8": 110, "9": 124, "10": 139, "11": 151, "12": 168, "13": 184, "14": 195, "15": 207, "16": 222, "17": 234, "18": 245, "19": 257, "20": 268, "21": 286, "22": 300, "23": 311, "24": 324, "25": 338, "26": 354, "27": 371, "28": 383, "29": 402, "30": 418, "31": 429, "32": 450, "33": 462, "34": 474, "35": 488, "36": 502, "37": 516, "38": 529, "39": 540, "40": 553, "41": 566, "42": 577, "43": 590, "44": 600, "45": 613, "46": 623, "47": 637, "48": 647, "49": 662, "50": 673, "51": 689, "52": 699, "53": 713}
---

**Dave Jones:** Hi, I'm going to show you how to measure the dynamic range of an oscilloscope. Now, this actually might be important because when you're analyzing, especially if you're a nerd on the EV blog forum like there are plenty of, um

**Dave Jones:** and you want to compare oscilloscopes and especially a 12-bit one like this new Rigol HDO 4000 series, then you know, if you're comparing like 12-bit scope and you want to compare the noise floor, you want to compare the effective

**Dave Jones:** number of bits and everything. Anyway, you know, you have to make sure you're doing apples to apples uh comparison. And one of the things you need to know is, well, what is the full-scale analog-to-digital converter range inside the scope? What's it actually, you know,

**Dave Jones:** doing? So, how do you measure that? Because most scopes, of course, will have like eight divisions vertically, but it could be uh more depending on the scope. This one actually has eight divisions. So, let's go down to 1 V per

**Dave Jones:** division here. You might think that the full-scale analog-to-digital converter range in this thing is those eight divisions. I.e., it's 1 V per division, so it's 8 V peak-to-peak full scale. But, that's not actually the case because as I showed in the unboxing and

**Dave Jones:** first play around with this video, you can see that actually um this is a triangle wave. You can see it's actually clipped at the top. And if I actually stop that and then go like this, you can see that it's not actually clipped. It's

**Dave Jones:** It does actually have some extra dynamic range, some extra sampling range outside of this window. But, how much more? Well, that's what we're going to find out here. So, the way you do this is you want to have a triangle wave. You can do

**Dave Jones:** it with a sine wave, but it's easier to see when waveforms are clipped with a triangle wave. So, what I've got here is my Rigol function generator. You can use Use the best function generator you've got, but I'm going to generate a 1 kHz

**Dave Jones:** signal. Doesn't matter about the frequency, really, but 1 kHz is just fine. Um and then we can actually set the uh peak-to-peak voltage here. Now, make sure you use the high uh Z or high impedance output. You don't want the 50

**Dave Jones:** ohm termination cuz if you've used the 50 ohm termination, then uh you have to factor in uh the accuracy of the 50 ohm load termination and the actual divider and the 50 ohm output in this and all that sort of stuff. So, I prefer to use

**Dave Jones:** You can, but I prefer to use the high Z. We're not talking about anything high frequency here, so we don't have to worry about any of that um you know, signal integrity uh stuff. So, um high impedance output mode uh 1 kHz and I've

**Dave Jones:** actually got an 8.6 V peak-to-peak signal here. But, let's take this up to say 10 V peak-to-peak here, okay? And then if we view this over on the scope here, let's run it and then we'll go down here and we'll just verify that the

**Dave Jones:** that the accuracy is the same on this uh scope over here. There you go. The average volts peak-to-peak 10.0 1, right? So, it's pretty close to being spot on. So, we can you know, if both of these instruments are you know, roughly

**Dave Jones:** measure the same, then you can like we can get the accuracy spec of this thing and stuff like that. But, you know, if they both read the same, then well, that's good enough for Australia. Okay, so what we want to do now is actually uh

**Dave Jones:** we're with the 10 V signal, let's turn it back to 1 V per division. And you can see how it I goes over scale here. So, what we want to do is we want to press stop like this and then go up a voltage

**Dave Jones:** range and you can see that it's actually clipped. So, somewhere between that 10 V and 8 V is where our actual uh dynamic range lies. So, what we have to do now is adjust the um output voltage on the

**Dave Jones:** uh scope to actually see at what point it doesn't clip. So, I've already done this. I know what it is, but uh let's set it to say 8.8 V uh peak-to-peak. So, we uh you know, you lower it down, lower

**Dave Jones:** it down. So, let's do 8.8 volts. Let's put it back to 1 volt per division here, and let's run it. Okay, and then we stop it, and then we can go down a range, and you can see, "Oh, is it clipped or not?"

**Dave Jones:** Well, we can actually zoom in like this. We can adjust our position, but we because it chops off the waveform here, not all the scopes will operate uh the same way here, but we can just uh put that back, and

**Dave Jones:** so, we can zoom in, just reset that. And No, we can go up a range. So, there we go. We can get it to there, and then let's just zoom back in, and then we change our horizontal time base, and you

**Dave Jones:** can see that, "Oh, it's just just clipped there. Just clipped." Now, unfortunately, we can't just leave it zoomed in like this, and then just uh tweak our value slightly down here, because if we actually run it, okay, you'll see that either we can't see our

**Dave Jones:** signal or it's uh changed because we've changed the offset, okay? So, when we uh redo this, every time we do it, we have to reset the offset like this. So, we have to reset it back to zero position

**Dave Jones:** like this. So, I forgot to show you that up front. You've got to have zero uh position like this, because then we've got a symmetrical waveform uh like this, because if you have an offset, okay, look, I'll I'll show you that we can

**Dave Jones:** actually I'll adjust this. So, I'll put in a 10-volt signal peak to peak, and you can see that it's absolutely clipped there. But, if we adjust it like this, then uh wait, the triggering's a problem. But, if we adjust it like this,

**Dave Jones:** and we run it, then it's not clipping anymore cuz we've adjusted that because it's not outside the positive uh range of the um essentially the analog-to-digital converter, if you assume that like it's in the middle, uh for example. So, yeah,

**Dave Jones:** you need to actually center that like that, and then and only then can you actually get a proper uh true peak-to-peak reading. So, anyway, I'll go to, uh, 8.75. You can see there, that's what I've dialed in, and it measures pretty close

**Dave Jones:** to that. And this one will not, if I turn it back to 1 V, and I stop it, and then I adjust like that. And we zoom in. And if I expand that, we'll find that, bingo, 8.75 V there, there's no clipping. We can't

**Dave Jones:** actually get the, uh, value anymore, cuz it it calculates that, uh, from the screen, and it can't actually doesn't have a full, uh, sample to actually gather that data from, so it's no good anymore. But anyway, somewhere between

**Dave Jones:** 8.75 V and 8.8 V, uh, peak-to-peak, is our full-scale range of our, uh, analog-to-digital converter, or maybe not. It could actually be just where the input amplifier clips. But you can't really know that, uh, the true range of the analog-to-digital

**Dave Jones:** converter, unless you're, unless the manufacturer tells you what it is, you know, you've got the schematic, and you can reverse engineer it, or potentially you can feed in like a one-bit signal, like a one, one-bit, uh, amplitude level signal,

**Dave Jones:** until you actually see like one-bit change or something like, uh, but then you're down in the noise, and it's horrible, and everything. So, we're just going to assume that the range is, um, in this particular case, 8.75 V

**Dave Jones:** peak-to-peak. So, if we get our confuser out here, 8.75 V peak-to-peak, divided by 4,096, cuz that's a 12-bit, uh, converter here, that will give us an individual bit of 2.14, or thereabouts, millivolts, uh, per bit. And that's how, um, we can calculate,

**Dave Jones:** and then you can use this information to then compare oscilloscopes, cuz I've been downloading, uh, raw binary waveform, uh, data in a standardized way, so that the EV blog forum nerds can actually, uh, compare it with uh the

**Dave Jones:** equivalent Siglent uh 12-bit scope and stuff like that. So, um yeah, if you want to know what I've been doing, I've been basically uh to get um the raw data on this, I'll show you what I've uh I've

**Dave Jones:** well, that I've standardized on I've standardized on. Anyway, so what I've done is I've disconnected it like this and I've uh set it um well, I've done it with 1 meg samples and I've also done it with uh the full 250 meg and that's

**Dave Jones:** where you'll get the most uh data as well and I set the time base to 1 millisecond like this uh for example and I've got um and I've done it with both 50 ohm input termination on and also

**Dave Jones:** just 1 meg input termination, so just leaving it flapping around in the breeze and I've also done it with the full 200 MHz bandwidth and the 20 MHz bandwidth and then I save the binary data, the raw binary data to a USB uh stick. You can

**Dave Jones:** also save it as a uh CSV uh file as well. But, the forum nerds uh requested a binary file, so I've provided a binary file and yes, it does actually take a long time to save the data. Takes

**Dave Jones:** several minutes to save the full 250 itself. I stopped this, okay? There's 200 at 4 gig sample and you have to know the sample rate as well and that changes to 50 meg samples per second if you go

**Dave Jones:** to the 1 meg memory depth. So, you have to know that as well and ooh, is that a bug? Is that a bug? Cuz we're stopped. That should be 50 meg sample We're in stop mode at the moment. Will it

**Dave Jones:** Come Yeah, it changed back. There you go. There's a There's a little bug. Um it was showing it didn't automatically change that meg samples until I actually pressed start. I guess that's all right cuz it still had Oh, no, that's probably

**Dave Jones:** not a bug cuz it's it had it still had that existing data in memory cuz it was in stop mode. So, you don't I know, I'm going to No, I take that back. Sorry, Rigol. I don't think that's a bug. I

**Dave Jones:** think that's a feature in that the memory was still the data was still in the memory, so it should display should match the memory. So, yeah. I think it No, I'm going to take that back. Take it back. I won't edit that part out cuz

**Dave Jones:** that's interesting. Um but yeah, this you need to know the sample rate as well if you know if you're calculating all sorts of stuff. You can get the effective number of bits. As I said uh in the uh first impressions of this

**Dave Jones:** Rigol, only say it's greater than eight bits effective number of bits for 12-bit converter um scope. They don't give you any more information than that. So, anyway, um the forum nerds will be added. So, someone on the forum who's

**Dave Jones:** got the uh 12-bit uh Rigol um HD scope, then uh yeah, they can get the same measurements and then we've got the raw binary data and you can compare the two and argue until the cows come home about

**Dave Jones:** which one's better. Anyway, that is an interesting way to measure the uh dynamic range of the scope. So, you can do this on your um scope. Find out like like especially on an 8-bit converter, how many bits is it uh pissing away

**Dave Jones:** outside of the screen you're not capturing? Sometimes that's good. You want that, you know, because uh you want to like zoom into detail, but then you want to zoom out and capture data later. In this particular case, it would've

**Dave Jones:** been nice to I don't know select it or something, have a selection for like how much dynamic range you want. I don't know. Does any scope have that feature actually that allows you to adjust the uh dynamic range of the scope? Of

**Dave Jones:** course, on an 8-bit converter, it's like uh you you haven't you haven't got much to spare outside of the uh windows. In fact, you've only got 256 uh samples and your screen is going to be more than 256

**Dave Jones:** pixels. So, like you don't even have a sample per pixel already, let alone outside. But when you got like a 12-bit converter like this one, you know, you got 4,096 bits to uh play with and uh and this is only a 800 um pixel screen

**Dave Jones:** from top to bottom. So, you know, you've got greater than one pixel per thing. Anyway, it'd be nice to be able to um adjust something like that. Let us know in the comments if you know a scope that's got that. But anyway, that's how

**Dave Jones:** you measure um the in theory the ADC dynamic range of a scope. Just put in a triangle wave is easy and just see where it clips. So, I hope you found that useful. If you did, give it a big thumbs up. As always,

**Dave Jones:** discuss down below and I'll link to the EVBlog forum thread where people are discussing, measuring, and comparing the noise floor of this thing. Catch you next time.
