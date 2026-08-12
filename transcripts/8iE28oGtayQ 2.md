---
video_id: 8iE28oGtayQ
title: EEVblog #1226 - Get Better Accuracy On Your Oscilloscope
url: https://www.youtube.com/watch?v=8iE28oGtayQ
source: youtube-asr
timestamps: {"0": 0, "1": 31, "2": 58, "3": 69, "4": 84, "5": 112, "6": 143, "7": 173, "8": 205, "9": 221, "10": 253, "11": 278, "12": 298, "13": 324, "14": 345, "15": 361, "16": 384, "17": 418, "18": 432, "19": 458, "20": 470, "21": 508, "22": 525, "23": 561, "24": 592, "25": 627, "26": 648, "27": 683, "28": 697, "29": 712, "30": 734, "31": 767, "32": 786, "33": 819, "34": 836, "35": 852}
---

**Dave Jones:** Hi, there's a control on your oscilloscope that you're almost certainly familiar with, but you may not know two advantages to actually using it. And it's what's called a fine vernier control on your vertical channel, and you'll see that it says push for fine here. And most modern oscilloscopes will have a pushable controls, not only pushable on the position adjust so that you push it and the waveform goes to the center of the screen like this. Or you can push your volts per division control like this,

**Dave Jones:** and you'll see channel one scale is now fine. And you can adjust it in much finer steps. But why is that useful? So you're familiar with your volts per division control, you can see it up here, one volt per division. It's usually in a one two five sequence. It that can vary depending on the manufacturer, so you'll get like one volt per division, two volts, five volts. You get one millivolt, two millivolts, five millivolts, 10, 20, 50, 100, 200, 500, and so on. So you adjust

**Dave Jones:** it in large steps. But as you can see, sometimes the waveform can get too large. And if you if we just center that there like this, okay, it's taking up a good lot of the screen here like this.

**Dave Jones:** But let's just get rid of that. But if we go up there, sorry, it's off the screen. So if we push that, we can get a fine vertical adjust like this so that we can make it any size we want. Well, what's the point of that? You might ask.

**Dave Jones:** Well, there's actually two advantages to this. The first advantage is in comparing waveforms. Let me center both of these waveforms here. I'll push the center and you can see that they're not the same voltage, but they're both 1 kHz sine waves, and they look pretty identical. And if you make it bigger like that, we can make this one a bit bigger. They look pretty identical, don't they? But well, let's go in there and have a look. Are they identical? But let's push our fine vernier control and

**Dave Jones:** actually adjust channel one until it matches channel two like this. And if we go in like that, we can see that there's little subtle differences in there between the two two channels. They're not quite the same, are they? And that's the first advantage of your fine vernier control. So, you won't be able to see it if it's like that or like that, for example. You can't see it, but when you make them even, that makes a big difference. So, that's very useful, but you might be familiar with that. Let's

**Dave Jones:** go to the second reason. And the second reason you might want to use your vernier control is the subject of this video, how to make your measurements on your oscilloscope. That's just one of the advantages of digital oscilloscopes is that you can actually take measurements of the waveform. There have been some analog oscilloscopes in the past that could do measurements and stuff like that, but they're usually cursor-based. When you've got stuff in the digital domain, you can measure things accurately. Anyway, let's take a look. We've just got a 1 kHz sine wave

**Dave Jones:** here, 4 V peak-to-peak. And because we've only got eight divisions total vertical here, you can see that it is basically using up all of the screen. But, if we go into measure here and we actually try and measure the peak-to-peak voltage, we can get rid of those statistics. There we go. You'll notice that it's not actually calculating anything here. It's not able to because the waveform is just a couple of samples, couple of pixels outside of the window. So, it can't measure that.

**Dave Jones:** It can't Trust me, that is actually real-time updating there. So, it can kind of give you the value down here, but you're not going to be able to get any of your statistics. You're not going to be able to get your mean value and see your standard deviation. Um Siglent is ridiculous, by the way. Look at this.

**Dave Jones:** 0.0 picovolts. Give me a break. You usually won't see that kind of stuff on a bigger brand instrument. The software should know that that is a ridiculous value, and it shouldn't even display it. Unbelievable. Anyway, so what we have to do of course is change our range down like this to 1 V per division. And now it can actually start measuring. I'll restart that just in case. Always restart your statistics after you change ranges, time bases, anything like that because there might be some accumulated error there or

**Dave Jones:** something like that just to be sure. And we should eventually get a standard deviation value. You can see the mean value 4.12 V. It's got two decimal places of resolution there and I don't know why it doesn't give us a standard deviation value straight away. Other scopes I've got here, they all give it to you straight away but the Siglent TAKES TIME. 0.01 PEAK OF VOLTS.

**Dave Jones:** UNBELIEVABLE. OH, actually this 0.02. This was working before. Trust me. Have I found a bug? I don't think I'm using the latest firmware. In fact, I'm pretty sure I'm not. Let me just upgrade the firmware here. I'll get back to you. No, unfortunately the new firmware doesn't make this work.

**Dave Jones:** We still have the same problem. God, I swear it was working before. I did a quick test before this video just to make sure it was going to do the business and no. What the Okay, I changed it 2 V per division and it's working now. So if we turn the statistics off and I'm effectively resetting them, give it a couple of counts and doesn't or two and it should There we go. We We now have a mean value 4.24 V. We're measuring the peak to peak

**Dave Jones:** voltage and a standard deviation. So this is like the like the spread of the values that it's actually getting cuz there's noise and and sampling error and other stuff on the signal, okay? So effectively 25 mV is the spread of the measurements that it's getting. Not still not working. Damn annoying.

**Dave Jones:** Anyway, I can still show you what I'm talking about. So, remember that figure, 25 mV standard deviation and two decimal places here, okay? So, let's go up. So, as I showed before, if we change the time base to 500 mV per division, it's just outside. It can't measure it. Okay?

**Dave Jones:** So, this is where our vernier can come in. We can push, hence it says variable there. We can go in and just get it under until it starts displaying our value. And bingo, what do you know? Look at the standard deviation there. It is smaller than what we had before. Let's reset that. Look at that. Nine odd millivolts.

**Dave Jones:** Effectively, we have a more accurate measurement. Even though on this particular signal scope, it hasn't given us any extra resolution here, but on other scopes, it will. And the reason it's going to give you a smaller standard deviation here or smaller error. And you can think of the standard deviation as the uncertainty in your signal. Basically, the reason that it's smaller, which is better, it's it's more accurate in quote marks, is that it has more bits from your ADC to work with than it did when the signal's

**Dave Jones:** down here like this. You remember? We've only got an 8-bit analog-to-digital converter. So, if your signal's right down here like this, let's let's go down to 5 V per division, shall we? And ah, it doesn't work down there either.

**Dave Jones:** Ridiculous. Given up on this signal scope. All right, let's check out the Rohde & Schwarz scope. This one actually uses a 10-bit ADC, as you've heard about before, which is better than the 8-bit ADC used in most other scopes. I've changed because we have 10 divisions here. I've changed it to 5.2 V peak-to-peak. So, you'll see the tips of the waveform there, top and bottom, just outside the range. So, you'll notice it can't measure the peak-to-peak voltage.

**Dave Jones:** It says it's clipping. I love that it actually says clipping there, plus minus. That's That's very nice. If we actually change our vertical scale here, this is the best scale that we can get uh that actually has it all on screen.

**Dave Jones:** That's going to give us a reading. We'll reset the stats there. And look at this. I mean, we're getting four decimal places on the standard deviation, four decimal places on the the current That's not current current as in amps. That's current value and the mean value. So, 9.6 standard deviation, okay? Let's go down a range, reset. Bingo! 15 mV standard deviation. It's got more error. Even though it's got that gorgeous big 10-bit analog-to-digital converter, it's still going to give you a a greater error, a greater variance in

**Dave Jones:** uh your values. And we'll go down again. Look at that. 60 mV. Reset that there. There we go. So, you can see how that changing the range actually upset that value. It's upset the apple cart there. So, you got to reset your stats. Is that Could that be a bug? Yeah.

**Dave Jones:** 36 mV, but if we hit our vernier, go all the way with LBJ, let's go until it's just lower than that. Bingo! Reset. Our error standard deviation is now 5.7. We're getting a more accurate reading. Brilliant. And watch this. You see how we got four decimal places at the moment. But if we change it to a smaller one, it Bingo! We drop back to two decimal places on our current value. It's still showing the mean as four decimal places because you can get a mathematically higher thing.

**Dave Jones:** But the scope's smart enough to know, I'm not going to give you these BS extra digits in there There's four digits when I know very well that I can't do that. That's the scope saying that. So, it only gives you the two decimal places. Very nice. So, there you go. That's a neat way using your vernier to maximize the accuracy of your scope. Now, of course, it must be said that oscilloscopes are inherently not that absolute accurate. Go and check out the specs for the scopes. I don't know what

**Dave Jones:** the Rohde & Schwarz is offhand, but they're in the order of like 1% absolute error, half a percent, you know, like even a couple of percent absolute error. So, they're not the best things in the business for measuring absolute values, but hey, if you're measuring difference between signals and things like that, all that extra resolution matters. And let's use our a Keysight 3000 T-series. I couldn't use the low-end 1000 1200X series cuz it doesn't have the statistics measurements. And you can see that our standard deviation 1.3 mV.

**Dave Jones:** If we go down like that, let's reset our stats again. 3.7. Look at this. You can see our error increasing eight. But, if we turn on our vernier and go right near the top there and reset. 1.2 mV standard deviation. Beautiful.

**Dave Jones:** And just like the Rohde & Schwarz, we've got four decimal places there and it's smart enough to know that if we actually go down, bingo, we drop a decimal place because, well, anything else is just BS. And the new Rigol 7000 series, let's reset our statistics there and we're looking at 15 mV standard deviation, 13, something like that. And if we go down, it's reset it, but we'll reset it anyway. Bingo, look at that. It's more than doubled, 35 mV. And go right down, 84 mV. Horrible, but if we turn our

**Dave Jones:** vernier on give that a bit of a clicky and oh, you can see, this is a good example. It hasn't updated. You can see how many bits it's got to play with here. Not many. Uh Um yeah, this Rigol scope is just slow.

**Dave Jones:** It's not updating as I turn that thing. But that that actually gives you Hey, that's you know, it's really quite neat. It gives you a representation of how many bits it's playing with there. Not many is the answer. So that's why standard deviation the error is larger.

**Dave Jones:** And right down here, 11 mV. No, eight, seven, six, dropping a little bit, five. So there you go. You can get extra resolution on your waveform on practically any oscilloscope that does these sorts of measurements. And by the way, you don't necessarily have to have these standard like these statistic measurements here.

**Dave Jones:** Just know that the just be confident that when your scope you use that vernier control to adjust it to a like near enough to full scale like that without clipping, your regular just your regular without the statistics Let's turn the statistics off. Even without that, you know, you can be fairly confident that your figure down here for your peak-to-peak measurement or whatever measurement you're doing is going to be more precise, so to speak. And just be aware the similar thing can happen on horizontal measurements as well. In this

**Dave Jones:** case, we're measuring the frequency. We're doing this via the samples. We're not using the hardware frequency counter. Actually only running with 10K sample points at the moment. So not many sample points. This is just to show you that it does actually work. And you can see that 1 kHz we're like one decimal place there on the frequency.

**Dave Jones:** And we're one decimal place on the standard deviation. So that's 54. So let's actually change and increase our time base so that we get more stuff. Bingo. We've got two decimal places there on our standard deviation. But in the case of the horizontal, the standard deviation actually works in the opposite way. If we go one waveform at like you know just basically one and a bit cycles or two cycles on the screen or whatever, you can see that our standard deviation is quite high. But if we get more

**Dave Jones:** waveforms on the screen, our standard deviation goes down. So it actually works opposite to how it does on the vertical. But then you can get extra digits over here by zooming in like that. So it depends on how you want it.

**Dave Jones:** Yeah. But with today's deep memory scopes and things like that, the main advantage isn't on any horizontal stuff with the horizontal vernier, but you can really get some advantages in measurement accuracy with your vertical vernier. So there you go.

**Dave Jones:** I hope you learned something there and you found that interesting. If you did, please give it a big thumbs up. And as always, discuss down below. Catch you next time.
