---
video_id: Dh0xYu8YvaE
title: EEVblog #662- How & Why to use Integration on an Oscilloscope
url: https://www.youtube.com/watch?v=Dh0xYu8YvaE
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 22, "2": 39, "3": 57, "4": 74, "5": 95, "6": 113, "7": 129, "8": 142, "9": 160, "10": 175, "11": 190, "12": 205, "13": 221, "14": 243, "15": 262, "16": 281, "17": 307, "18": 325, "19": 345, "20": 363, "21": 383, "22": 399, "23": 422, "24": 440, "25": 458, "26": 477, "27": 489, "28": 517, "29": 540, "30": 556, "31": 578, "32": 592, "33": 606, "34": 622, "35": 642, "36": 658, "37": 682, "38": 702, "39": 723, "40": 739, "41": 756, "42": 769, "43": 785, "44": 804, "45": 828, "46": 847, "47": 864, "48": 879, "49": 901, "50": 917, "51": 932, "52": 949, "53": 962, "54": 985, "55": 997, "56": 1013, "57": 1029, "58": 1043, "59": 1056, "60": 1068, "61": 1084, "62": 1101, "63": 1117, "64": 1129, "65": 1151, "66": 1170, "67": 1192}
---

**Dave Jones:** Hi. Modern digital scopes are wonderful tools and can have very powerful analysis and software capabilities. In particular, they have lots of math functions. Now, if we take a look at the math function over here, you'll notice that all of these transforms and operators, look at what we can do in one of these modern scopes.

**Dave Jones:** Add, subtract, multiply, divide, we can differentiate, and it shows you the data in real time. We can actually apply these operators and transforms to our captured data, not only in stop mode, but also in real time as well. And we can differentiate, integrate,

**Dave Jones:** we can do FFTs, you're likely familiar with FFTs, to get the frequency domain of your signal, or make it work like a spectrum analyzer, but we can square, square root, absolute value, we can do all sorts of logarithms, and we can even low-pass filter our signal,

**Dave Jones:** and do all sorts of weird and wonderful mathematical stuff for this. But you're probably thinking, well, what actual practical use is having something like an integral here? Why would you want to integrate your signal? Well, I'll show you a real practical example where this is very useful, and how you can use this and do it.

**Dave Jones:** Let's go. Now, a really good example of where integrals will come in handy is, for example, measuring the power consumption of a modern microcontroller like this EnergyMicro arm micro we have here. Now, I'm using my microcurrent here, and I've got it in series, a couple of jumpers in there,

**Dave Jones:** in series with the power supply of the microcontroller. I've set the range so that we're able to measure this on our multimeter, but in this case we're going to take it out to the oscilloscope and actually look at the waveform, and the microcontroller is actually going to sleep here, and then every second it's waking up

**Dave Jones:** and then, you know, changing the message on the LCD there. So we need to measure the total power consumption of this microcontroller. Let's see how integrals and the integral function helps us do this. So if we have a look in real time at the output from our microcurrent here,

**Dave Jones:** we can see our current waveform. You can see that every second it's popping up with, you might be able to capture it there, a current pulse when it wakes up and displays something on that microcontroller. Well, we can of course single-shot capture that.

**Dave Jones:** Bang, there it is, and there's our current waveform when it powers up. So we want to look at and calculate the total energy or current that's being used by our microcontroller over time. Now, our waveform's a little bit noisy there, so what we want to do in this sort of situation

**Dave Jones:** when you're looking to get high resolution and as much accuracy as possible, you basically want to go in and you want to turn on your boxcar averaging, your high-resolution mode here, and we should be able to get a nice, cleaner and higher-fidelity waveform in there.

**Dave Jones:** And now, bingo, we've captured that, and we can see our waveform in pretty good detail. And you can see how it powers up here, there's a little bit of, you know, weird stuff happening here when it powers up, and then it goes, got a few little wiggles in there.

**Dave Jones:** And we've got all of our data in there, and slowly charging up, that'll be due to, you know, the decoupling on the power supply, it's doing its operation, and then it's basically shutting back down, right down to the sleep current, right down the bottom, right there.

**Dave Jones:** So most of the time is going to be spent in sleep mode, of course, and you can see in this case, five minutes, per division, it powers up every two seconds, basically, and updates the LCD. So we want to get the total current consumption over that time.

**Dave Jones:** How do we do it? Well, the integral is the key. So when you're talking about power consumption, when you have effectively a current draw graph like this, the area under the curve represents the total current consumption of your product. And of course, if you zoom right out, and you get it over time, for example,

**Dave Jones:** then you're only drawing very small current peaks like that, with lots of, you know, dead period like this, where there is still current drawing there, but you've got to add it all up over time, over one full cycle, so that you can get a true measured value of the total current consumption.

**Dave Jones:** And the way to do that, the way to find out what the area under that curve is, is with an integral. So just what is an integral? Well, if you're familiar with integral calculus, or if you're not, I'll tell you now, well, it can be a relatively complex mathematical subject,

**Dave Jones:** but what it comes down to is an integral is essentially, the integral function is the area under any particular curve. So we've got our yellow data waveform here, so all of that in there, all that area under the curve there, is the integral of that particular waveform.

**Dave Jones:** And the purple waveform we've got here is basically just adding up, each little bit of that as we go along, and then increasing, increasing, all the way up, until we get a total figure right at the end. So over a particular time period, it'll always, it'll rise like this,

**Dave Jones:** representing the maximum value of all the, each individual segment, if you want to visualize it all broken up into little segments, adding those all up until you get to a final value. Sorry, the colors aren't working out very well, but basically, that green area in there, that total area,

**Dave Jones:** is going to be representative of the total area under that yellow curve there. So we end up with a final figure up here, from the bottom to here, when we turn on our measurement function of our total area under the curve. And that's how integrals can be done.

**Dave Jones:** So what we get here, when we select the integrate function here, we can select our source, of course, our source is coming from channel 1, the yellow waveform, and then we get different scales, and there's two other controls on the oscilloscope, that then operate the scale of that integral calculation waveform,

**Dave Jones:** just like you have another vertical scale there. So we set it so it's on screen like that, and we can also offset that like that, so we can put it down and line it up with a graticule like that, and then we can, you know, take measurements from there like that if we want.

**Dave Jones:** And of course, being an integral, it's going to be over time, so rather than just being a voltage, it's going to be voltage with respect to time. So we've got different units here of 100 microvolts seconds. So it's 100 microvolts over time, so it's 100 microvolts over 1 second total value,

**Dave Jones:** peak value there over a 1 second period, but of course we don't have 1 second on the screen, they're just the units. Okay, what we want to do first is pretty much get the area under this entire curve here, so I've expanded it out so that, you know, it pretty much is decayed away back down to 0 here.

**Dave Jones:** We care about all the energy content under that, and you can see how the waveform is slowly tapering out until it's pretty much flat. So, you know, that's going to be good enough. Let's get the area under that current pulse peak there. So we can of course just, you know, move that up manually and just count the number of there

**Dave Jones:** until we get to that maximum value we want there, but hey, this is a modern scope. We can turn on cursors, and we can go into Y here, and we can set our Y cursor right down to the bottom there. That's where it starts, and then we want the peak value right up the top here.

**Dave Jones:** So Y2, there's our second cursor value, so we want it over that particular time period there. We don't have to worry about the X1 and X2 cursors, that just gets us the difference there. But here is our value, delta Y, between those two values, i.e.

**Dave Jones:** that peak value up there. 697.9 microvolt-seconds. Hey, let's round it up to 700 microvolt-seconds, shall we? Now if we actually expand this out, and readjust our scale for our math function, for our integral, you can see that we can see the accumulation of the value over time.

**Dave Jones:** So we can actually measure it directly from here. If our oscilloscope had the correct, you know, enough dynamic range, i.e., you know, a big enough, high-order enough analog-to-digital converter to actually accurately measure this small sleep current down in here, you know, in the same range as our big peaks here at every two-second mark.

**Dave Jones:** But you can see the accumulation, and you can see the small step function in there. You can see how it sort of just steps up a little bit at each pulse, and then it accumulates all of this sleep current here, and you get a final value.

**Dave Jones:** Look, it's changed our scale a bit to millivolt-seconds here, but it's showing 12.16 millivolt-seconds, which, of course, because of the microcurrent, we can translate that to 12.1 milliamps average over an entire second. But I think it's reading a bit high, because this noise down in here,

**Dave Jones:** it's going to have too much noise down in there, which, you know, it's just that may not be the device under test. So you just have to be careful when you're doing these sorts of measurements to, you know, if you want to do this period here,

**Dave Jones:** you would have to sample that separately and add it up. But we're going to use just the multimeter to get our average figure right down at that value. And then, so we're only using our oscilloscope to get these current pulses here. So there's, you know, several different ways to do it.

**Dave Jones:** You've just got to be careful that you're not being trapped into reading that directly, because you could find that there, well, we will find that that value is much higher than what it realistically would be. So we can use our multimeter here just to get, like, an average figure,

**Dave Jones:** and, like, over the macroscopic timescale, and we can set, like, min-max if we really wanted to, and then we could, like, take the average value, 4.7, something like that. We could maybe round it up to 5 millivolts, for example, over the macro time period, because we're talking about a very large difference

**Dave Jones:** between that very short current pulse and the rest of it. So let's just say it's 5 millivolts. And, of course, the microcurrent here is set to 1 millivolt per microamp, so that translates to 4.6, or let's, as we said, round it up to 5 microamps,

**Dave Jones:** just, you know, generic sleep power consumption. And, by the way, with these integral units of volt-seconds, or, in this case, micro-volt-seconds, don't confuse that with volts-per-second. They are actually different. Volts-per-second means a rate of change, you know, a differential dvdt, you know, a capacitor or charging or something like that.

**Dave Jones:** A volt-second, like we're talking about here, is entirely different. It's, we're talking about accumulated energy over time. That's basically what it is. Entirely different to a rate of change over time, volts-per-second. So just don't confuse them. Be careful. Again, you know, it's very easy to mix the two up.

**Dave Jones:** So with a value of 700 micro-volt-seconds, what that basically means, if we spread all of the energy under that curve there, which we're getting in 4 milliseconds, if we spread that over 1 second, 1 full second, it would average a value of 700 micro-volts for that 1 second.

**Dave Jones:** Now, because we've got units of micro-volt-seconds there, well, we've got our unit of time, 1 second. So it makes sense to deal with 1 second from here on in as our defined time period for calculating our total current. So that's what we'll do now.

**Dave Jones:** You could convert over other time periods, but it just makes sense to go over a second. So that's what we'll do now. So at this point, all we're doing is looking at the total value there, effectively the peak value, which is the accumulation of all that area over time.

**Dave Jones:** So it doesn't actually matter if we choose a longer time period, assuming that this thing flattens out. It doesn't matter. We're only talking about that peak value there. We could go a bit longer. You can see it's still trying to ramp up a bit,

**Dave Jones:** but we're pretty close. Just for argument's sake today, we'll say that we've got our 700 micro-volt-second mark. So that's all the energy in our pulse. So now all we have to do is add that energy to the energy that we measured average with the multimeter

**Dave Jones:** over the rest of the time period, and bingo, we can get our total current consumption. So what have we got here? We've got 700 micro-volt-seconds, and because we're using the micro-current, it's equivalent and translates to micro-amps because we're using the one millivolt per micro-amp range.

**Dave Jones:** So 700 micro-volt-second is equivalent to 700 nano-amp-seconds, or an average figure of 700 nano-amps. That energy we saw is spread over an entire second. So what we can do is now draw a graph, because our microcontroller only wakes up every two seconds, as we saw, then effectively we measured the average current

**Dave Jones:** around about five micro-amps there. We could measure it more accurately and get more fussy and stuff like that, but let's just say, for argument's sake, five micro-seconds average current over that time, then during that one second, then assuming a one-second period, we've got to add on that 700 nano-amps

**Dave Jones:** that we got from the energy consumed during that big pulse when the microcontroller started up. So you can see it's not a very large percentage, but it's a reasonable error if you didn't take that into account. And you can see that's over one second,

**Dave Jones:** and then for the next second, just for argument's sake, there was no pulse, we're not accounting for the pulse there, so we only get our five micro-amps. It's just a way to look at it, it's just like a visualization tool, there's different ways to do this.

**Dave Jones:** But anyway, so that 700 nano-amps is going to average to half that value, or 350 nano-amps over the two-second period before that pulse starts again. So our total current consumption of our microcontroller, we can say, is 5.35 micro-amps. So you can see that that rather large pulse

**Dave Jones:** really didn't have a huge effect in the power consumption, in the average total power consumption of our device. So I guess this wasn't the best example, because our pulse, you know, we didn't, we could measure it as accurately as we wanted, we used the integration method,

**Dave Jones:** which gets us the total area under the curve, and it turns out to be, you know, a relatively small percentage of our overall power consumption, but hey, you know, this is just the technique used, and this is the proper way to do it

**Dave Jones:** if you want to measure your total power consumption for your product like this that uses these types of pulses. Now I was showing you how to do this using the integration function, math function here, but as it turns out, this Agilent X-Series actually has a measurement function,

**Dave Jones:** not a math function, but a measurement function. If we go in there, and you're used to all these, you know, you can measure your peak-to-peak, maximum, amplitude, you know, average, blah, blah, blah, RMS, all that sort of jazz. If you go right down here, check this out.

**Dave Jones:** Look, area over the full screen. Look at that, area over number of cycles, or area over full screen. So area over the number of cycles would basically give you an instant readout of your microcontroller, of the total power consumption in your microcontroller if you had the dynamic range,

**Dave Jones:** as I said. So we can go in there, and we can choose, well, let's go in there and go full screen, but then we can actually choose the value that we actually want. And there you go. At the moment, it's giving us a readout

**Dave Jones:** of 525 microvolt seconds there, and of course we can expand the time base and actually get the full figure, just like we got before. Actually, there's another neat thing. We can go into the zoom function here, and then we can expand that window,

**Dave Jones:** because we've selected measure over the full window. So then we can go in there and choose our window, and if you wanted to, you can press that and go into your Vernier and actually get exactly the time period that you wanted to, so over the full screen.

**Dave Jones:** So you can adjust that just, you know, rather finely. Say if you wanted the pulse, you know, from there to there or whatever, you could go in and actually tweak that and get a full value there, and there you go. It might be, you know, 400 and something,

**Dave Jones:** but it does exactly the same thing that we did before. So as you can see, we've got our math functions completely turned off, so it's not getting the integral, it's actually calculating the area under the curve, and it knows how I do that.

**Dave Jones:** It's a very similar time period to what we had before, I think, and look, we're getting very similar to the accumulated value we got before. It's 663. There might be a bit error because I haven't exactly got the same period or something like that,

**Dave Jones:** but there you go. You can get exactly, pretty much, well, you can get exactly the same reading using that area under the curve measurement function if your scope supports that. This one happens to, but not all do that. So although we had a relatively large current spike here

**Dave Jones:** of, in this case, around about 1.4 milliamps, which is actually quite large for the microcontroller to start up, do that sort of processing, compared to our average, you know, value, which is down in the noise here, of 5 microamps, which we measured on our multimeter,

**Dave Jones:** and that current pulse there is relatively high, but it overall, over the span of that two seconds, doesn't really add a huge amount to the overall current consumption of the thing. And yes, with the calculations I just did, technically I should have subtracted the time

**Dave Jones:** taken from that, but we were like, you know, the pulse that was only 4 milliseconds is like a couple of orders magnitude less than the total time period, so, you know, you wouldn't bother adding that sort of stuff in. So there you go.

**Dave Jones:** That's some reasonably accurate calculations of total power consumption of a microcontroller. So I hope you found that useful, and then you can, you know, play around with these integration functions. They're not just there for looks. They actually have, these sorts of mathematical operators

**Dave Jones:** can really have some useful practical applications like this, and other ones you might get, like the half power point in a communications system or something like that. There's various other uses for the integration method which I won't go into, but this is one particularly nice example.

**Dave Jones:** So I hope you enjoyed that, and if you want to discuss it, there will be the EEVblog forum link down below, or leave it in the comments. And if you liked the video, please give it a big thumbs up. Catch you next time.

**Dave Jones:** .
