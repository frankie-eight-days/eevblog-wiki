---
video_id: W4twnd-YQQ4
title: EEVblog #1213 - The Oscilloscope Interpolation Trap!
url: https://www.youtube.com/watch?v=W4twnd-YQQ4
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 13, "2": 30, "3": 42, "4": 65, "5": 90, "6": 104, "7": 119, "8": 136, "9": 153, "10": 171, "11": 191, "12": 206, "13": 222, "14": 239, "15": 255, "16": 272, "17": 289, "18": 307, "19": 321, "20": 338, "21": 354, "22": 373, "23": 386, "24": 404, "25": 420, "26": 441, "27": 461, "28": 480, "29": 497, "30": 516, "31": 535, "32": 561, "33": 581, "34": 602, "35": 624, "36": 641, "37": 664, "38": 684, "39": 706, "40": 726, "41": 743, "42": 763, "43": 779, "44": 796, "45": 810, "46": 830, "47": 848, "48": 867, "49": 885, "50": 900, "51": 917, "52": 934, "53": 952, "54": 970, "55": 982}
---

**Dave Jones:** Hi, I wanted to show you a feature in modern digital scopes that can be a real trap for young players if you don't know what you're doing. And you may have actually seen this in the scope before but not really understood what it is.

**Dave Jones:** Let me show you here. A newfangled deep memory scope here. Obviously got a signal here and we can capture a ton of the signal and then zoom in later with our deep memory. Okay, so let's do our single shot capture here. Say we're on 50 milliseconds per division here.

**Dave Jones:** Let's single shot capture that and then we can go zoom in at our data and well, look at that. It looks like we've got a pulse there and it's got some ring in and you may be familiar with this sort of ring in

**Dave Jones:** as something that you'll get when you've got bad probing and things like that. Well, what signal are we actually measuring here? Well, let's single shot capture it again at this time base. That's the signal that's actually there. So, what's going on here? So, as you can see, what we're capturing is just a digital packet here and if we go out like this,

**Dave Jones:** you can see that there's several packets like that and it's actually a recurring packet of like serial data. But if we go out far enough, as I said, 50 milliseconds per division in this particular case and then we zoom in, we get, well, look, that actually looks like an absolute classic sine X on X signal.

**Dave Jones:** That's because of our sine X on X interpolation and this ring in type overshoot effect that we actually get from our sine X on X interpolation is actually known as the Gibbs effect or the Gibbs phenomenon and you can look that one up.

**Dave Jones:** That has its own history and mathematical relevance for all you math nerds. And I'll explain what interpolation is in a minute, but if we go in and go to the acquire menu like this, sync or sine C here, this is the interpolation. If we actually turn that off...

**Dave Jones:** If we turn that off, we can see that this is what it uses using what's called linear interpolation where it actually joins the samples like this. Because in this particular case, we're not going to have, because we're zoomed in, we're not going to have many sample points on this screen here.

**Dave Jones:** And we can see that if we actually go over to our display menu and choose instead of vectors, which it basically just joins the dots, so to speak, we can go dots here and you can maybe see, might be a bit hard. But you can see the individual sample dots in there.

**Dave Jones:** So how does it go from those dots to an interpreted display like that? Well, it's actually doing what's called interpolation or it's actually post-processing after it's sampled, which is the reason why that we can actually just modify this after we've actually captured it.

**Dave Jones:** Why is it actually doing that? What's the purpose of this sine X on X interpolation? But hopefully, as you can see, that can be a real trap for young players. That's our real signal there. And if you sample at a long enough time base with not enough memory,

**Dave Jones:** then you can come a gutser and think that there's a signal there, like some sort of weird thing happening when it's actually not. And if we go into our acquire menu, you see that our memory depth is only 1.25 meg points of memory.

**Dave Jones:** This one actually has up to 256 meg. So let's say we changed our memory depth so we get more dots across the screen. We get more samples. When we actually zoom in, you'll find there's our real signal, our live signal. Let's go up to, say, 125 meg.

**Dave Jones:** Now, if we go all the way back to our 50 milliseconds per division, it just happens to be 50 milliseconds for this particular signal that I'm using. Don't worry about that. If we now single-shot capture that and zoom in, ta-da! We don't get that problem anymore.

**Dave Jones:** Because if we go into dot mode, you'll see we have a lot more dots than what we had before. So the software, when it does that interpolation, that in this case it's using a sine-C filter, but it's basically, let's just say sine-x on x.

**Dave Jones:** That's what most scopes use and what it's generically called. It doesn't, it's already got enough sample dots in there that it can display our actual signal, pretty close to our exact signal. But it's only when you get fewer and fewer sample dots in there

**Dave Jones:** does this interpolation take over and try to interpret it as a sinusoidal signal. So why on earth would you want a scope to do this? Well, it basically makes your waveform look better and it's actually got a good reason behind it as we'll go into.

**Dave Jones:** But basically all modern scopes by default have sine-x on x interpolation and it's enabled by default. So you have to actually know, under what circumstances you should leave it enabled and under what circumstances you should disable it. And of course, you've already noticed that at very long time bases like this,

**Dave Jones:** when you do that, that is when you can get a real problem and come a gutter depending on how much memory depth you've got on your scope and how much memory depth you've got enabled. Which is why some scopes like this Keysight 3000 here

**Dave Jones:** are smart enough to know this is a problem and actually disables it for you by default. It's smart enough to know that. In fact, with the Keysight InfiniiVision scopes, you cannot enable or disable the sine-x on x interpolation. It takes care of it for you.

**Dave Jones:** So let's single shot capture that at the same 50 milliseconds. It's exactly the same signal. This only has 4 meg of memory maximum, doesn't have a lot. But you'll notice that there is no sine-x on x interpolation. It hasn't tried to, you know, fill in the dots with any sinusoidal signal.

**Dave Jones:** It's using linear interpolation, which is what you get. If you turn off your sine-x on x. Some scopes will call it linear interpolation, others will just say off. So to demonstrate why they add interpolation to oscilloscopes, in particular, sinusoidal or sine-x on x interpolation,

**Dave Jones:** we need a lower, well, we can do it with any scope, but hey, you can try this at home if you've got the suitable gear, where we'll go down to a 200 megahertz bandwidth scope and we'll feed in a 200 megahertz sine wave.

**Dave Jones:** And believe it or not, ta-da! That's what I'm feeding in there. That is a 200 megahertz. That's a perfect from an RF signal generator. And it's kinda sorta sinusoidal, but look at it, it's all jaggy. Why? Well, it's obvious because the sample rate here is only 1 gig sample per second,

**Dave Jones:** which is only 5 times the bandwidth in sample rate. So we're only getting 5 samples or 5 dots per cycle of the sine wave. And obviously, you can see it, 1, 2, 3, 4, 5. You're only getting those 5 dots. That's why it looks jaggy.

**Dave Jones:** And as you should know, often with these scopes, when you enable the second channel, that sample rate will halve. So in this particular case, it drops down to 500 meg samples per second. And we're trying to sample a 200 megahertz signal with a 500 meg sample per second scope.

**Dave Jones:** And of course, it looks worse because you've only got 2.5 samples per cycle. It's absolutely awful, that's useless. What is that, a triangle wave? Sawtooth? So if we turn on our interpolation, let's go down here like this. And interpolation, sine x on x, look at that.

**Dave Jones:** We've got a sine, it looks like a sinusoidal wave, which is actually what we're feeding in here. And it's only 500 meg samples per second. It's barely above what's called the Nyquist frequency limit, which you may have heard of, which is, basically, half of the sample rate.

**Dave Jones:** So 200 megahertz, in theory, to meet our Nyquist requirement, we need 400 meg samples per second. And we're just meeting that here with our 500 meg samples per second. And if we go turn off our channel 2 and do it again, we're back up to 1 gig sample per second.

**Dave Jones:** So now we're basically five times our sample rate. And bingo, we get a nice, beautiful sine wave, look at that. That's fantastic. But of course, it's all smoke and mirrors. If we go into display here and turn on dots, you can see there's our dots there.

**Dave Jones:** Look, little itty bitty dots. Like it doesn't look like much, does it? It kind of looks like just a random array of dots in there. But when you turn on the interpolation, it gives you a beautiful sine wave. So what's going on here?

**Dave Jones:** Is this cheating? Well. Yes and no. This actually is, can be mathematically completely valid. So basically interpolation is just a way to mathematically fill in and predict what the other points would be. And it's, it can be mathematically valid because remember, the analog bandwidth of the oscilloscope on the connector here is only 200 megahertz.

**Dave Jones:** So any frequency, it's not a brick wall filter. It does actually roll off, it doesn't just magically stop and not allow any other frequencies beyond 200 megahertz. But remember, like it's starting to roll off at that frequency. So really, if we fit in a 200 megahertz square wave into the input here,

**Dave Jones:** what's going into the analog to digital converter is not actually that square wave. It's the rolled off 200 megahertz bandwidth limited signal into the ADC. So all of those higher frequencies caused by the sharp rise and fall times of your square wave, they're actually filtered out.

**Dave Jones:** So the ADC is really seeing more of a sine wave. And you can actually sort of mathematically guarantee that for a certain type of input bandwidth filter, then sine x on x interpolation is a completely valid mathematical technique for reconstructing the waveform that's actually

**Dave Jones:** seen by the analog to digital converter inside the scope, or it would be. So these points in here are actually valid. And the interesting thing about this is it actually gives you a higher, what's called, effective sample rate. Even though we've only got one gig sample per second,

**Dave Jones:** when you turn on your interpolation down here, when it's filled in the dots, look, we can go in there and more accurately measure with our cursors. A, what's effectively a much higher sample rate. In fact, we can go up in increments here. Look at this, x1, x2 of 20 picosecond steps there, wow.

**Dave Jones:** And if you get your confuser out and do 20 picoseconds, and you invert that on the calculator, what do you get, 50 gig. So we've effectively turned our 1 gig sample per second sample rate into an effective, I'm gonna use the quote marks, effective sample rate.

**Dave Jones:** Of 50 gig samples per second. And particularly on very high end scopes, you will actually see them advertise this effective, or sometimes called interpolated sample rate, of much higher than what the actual ADC sample rate is. And it can actually be, depending on your input signal,

**Dave Jones:** can actually be a very valid, mathematically valid method of recreating your signal and actually measuring it. At a higher sample rate. Cool, huh? So all that extra data there coming from just implementing a mathematical filter or what's called a convolution filter on the input data.

**Dave Jones:** And there's a couple of different ways to do it, but sine x on x is the most popular method for that. But of course, the sine x on x, or sometimes simply called a sine x or a sine c filter, is only valid if you meet that Nyquist requirement.

**Dave Jones:** So you've gotta have at least twice the analog bandwidth in sample rate. But as I said, that's gonna be reliant upon what type of roll-off you've got in your oscilloscope. So that 200 megahertz bandwidth roll-off on your front end here, if it's like a different type of response, you will have a different resultant waveform

**Dave Jones:** when you actually turn on your interpolation here. So if it's got a Gaussian response filter, that response can actually make a difference in how the signal is actually interpreted. So as we see, if we have our sample rate again, let's do that one more time,

**Dave Jones:** you'll notice that it didn't give us quite the valid response that we got last time because we've halved our sample rate. We're only two and a half times more than the actual bandwidth. And because there's higher frequency components, when it rolls off, they still sneak through, then you get little artifacts.

**Dave Jones:** And it's not as an accurate recreation of that. And also, sine x on x interpolation is only valid if you get a very high frequency. If you meet that Nyquist requirement. If you've got a 200 megahertz bandwidth and only a 200 megahertz sample rate,

**Dave Jones:** sine x on x interpolation is completely mathematically invalid. Doesn't work. So interpolation is great when you're near the maximum time base like this and you're looking at more like analog sinusoidal or, you know, analog-y type signals. But if you're way up in the time base, as we saw right at the start of this thing,

**Dave Jones:** looking at digital signals, for example, you can really come a-gutser. As we saw at the start, this can happen right at effectively very low frequencies if you run out of samples. You can really come a-gutser like that when it should look like that.

**Dave Jones:** And it's just the memory depth of that. When it just has so few samples and you're looking at a different signal, you're looking at a square wave, in this particular case, nothing high frequency. It's got nothing to do with the bandwidth. You can reduce the bandwidth here to 20 meg and it's not going to make a difference.

**Dave Jones:** You still go into it. You see there was very little difference in that data between the full 200 meg bandwidth. And if we do that again, we're still screwed because we don't have enough samples because we've only got 14k points. Whereas if we go up to enough memory or we choose a lower horizontal value,

**Dave Jones:** let's do 1 millisecond instead of 50, we might get away with that. Yep, we can see. We've got digital data there. So just be aware of that. It can be a real trap when you're looking at it. You might think there's some other problem there.

**Dave Jones:** You might think, "Oh, I've got a probing problem. Oh, no, I'm screwed." So you trace a red herring down a rabbit hole because you think that you've got something weird probing thing or something happening when, nope, you're just using your scope wrong. And it's pretty easy to make this mistake.

**Dave Jones:** You're using your scope and you're not really keeping in your head, well, how many memory points, am I using? And when you do your capture like this and you zoom in, you're not really thinking, like doing the mental calculation that, oh, okay, how many meg points, how many data points

**Dave Jones:** and things like that. If you can't see them and you get a nice looking waveform like that, well, it's very easy to come to the conclusion that that's what's really there when it's nothing of the sort. So there you go. Just be aware of interpolation that your scope almost always is going to have on by default.

**Dave Jones:** Next time you're using it, just look at the waveforms that you're measuring, your memory depth, your sample rate, all sorts of things, and don't get tricked into thinking that there's something weird going on when it's, no, it's not the scope. It's you. Anyway, I hope you found that interesting.

**Dave Jones:** If you did, please give it a big thumbs up. And as always, discuss down below in the comments or over on the EUVblog forum. And I'm sure all the math nerds will, of course, go to town because this is like a real, like,

**Dave Jones:** quite a mathematically involved subject if you really get into this sort of thing. And yes, the 10 year old in me sees dick and balls. Catch you next time. Bye.
