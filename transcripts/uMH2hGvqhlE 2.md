---
video_id: uMH2hGvqhlE
title: EEVblog #396 - Bode Plotting on Your Osciloscope
url: https://www.youtube.com/watch?v=uMH2hGvqhlE
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 36, "3": 53, "4": 68, "5": 86, "6": 103, "7": 113, "8": 128, "9": 140, "10": 157, "11": 172, "12": 186, "13": 201, "14": 216, "15": 231, "16": 244, "17": 260, "18": 281, "19": 298, "20": 311, "21": 324, "22": 336, "23": 353, "24": 367, "25": 381, "26": 399, "27": 414, "28": 427, "29": 444, "30": 463, "31": 480, "32": 500, "33": 516, "34": 535, "35": 549, "36": 566, "37": 578, "38": 592, "39": 608, "40": 625, "41": 642, "42": 659, "43": 671, "44": 690, "45": 708, "46": 729, "47": 746, "48": 759, "49": 776, "50": 789, "51": 809, "52": 821, "53": 837, "54": 853, "55": 866, "56": 877, "57": 894, "58": 914, "59": 929, "60": 949, "61": 967, "62": 988, "63": 1005, "64": 1021, "65": 1037, "66": 1049, "67": 1062, "68": 1075, "69": 1091, "70": 1104, "71": 1120, "72": 1138, "73": 1149, "74": 1162, "75": 1174, "76": 1189, "77": 1202}
---

**Dave Jones:** Hi, I was recently playing around with some filters and I wanted to get the frequency response plot of the actual filter, i.e. a Bode plot. Amplitude versus frequency and you've seen me do these in the videos before in

**Dave Jones:** simulations and various other things but I wanted to actually measure the response and well, as you do, I got to thinking, is it possible to get a frequency response or Bode plot on an oscilloscope? I think there's a way to do it. Let's

**Dave Jones:** have a go. Now, in a recent video which I'll link in here, I've showed how to do this with a spectrum analyzer with a tracking generator, very useful for getting a frequency characteristic or frequency response plot of a filter or

**Dave Jones:** something like that if you've got the tracking generator option. But all right, but these are a spectrum analyzers, they're only good for RF, i.e. 9 kHz up to 1.5 GHz. So, they're no good for like audio frequency or other

**Dave Jones:** lower frequency stuff. So, what would you use to measure lower frequencies? Well, traditionally you use a what's called a dynamic signal analyzer or one of these FFT analyzers and they had these have really fantastic dynamic range and a huge resolution ADCs

**Dave Jones:** in these things, excellent noise floor. They're really the bomb for doing you know, low frequency sound and vibration measurement and stuff like that. So, what do you do if you haven't got one of those? And well, yeah, you can use a

**Dave Jones:** sound card. A lot of people say that, you know, they've got a a reasonable you know, an audio type bandwidth and you can do the job with one of those. You can generate signals with the DAC on the

**Dave Jones:** card of course and um, measure it in with some audio inputs. So, well, we don't want to do that. So, how would you do this on this oscilloscope? Well, ordinarily, you cannot get an oscilloscope to display frequency on its

**Dave Jones:** horizontal axis, unless you do an FFT, which isn't really suitable in this case. So, the way you normally get a frequency response plot with an oscilloscope is, in fact, you don't even need an oscilloscope, you just need a

**Dave Jones:** multimeter and a function generator. You've seen me also do this before, manually measuring the frequency response of an amplifier, where you sweep the where you turn up the input frequency and you get a bit of paper and you write down values at spot

**Dave Jones:** frequencies. As you go up in frequency, you write down the amplitude, either from an oscilloscope or you can do it with a multimeter as well, if it's got sufficient bandwidth. So, that and then you enter those enter all those tables and numbers into

**Dave Jones:** your spreadsheet and you generate your frequency response graph, but we don't want that. We want to actually generate a Bode plot or a frequency response plot plot in real time on the screen. So, if I've got a low-pass filter, I want to

**Dave Jones:** see it go like this and then drop down like that. You might think it's impossible, but there's a neat trick that allows you to do this. So, quick recap on what a frequency response or Bode plot is is a

**Dave Jones:** graph of amplitude on the Y axis here versus frequency. And the way you normally get it is to sweep a signal through your filter over the desired frequency range like that and you will get response plot. In this case, we've

**Dave Jones:** got a band-pass filter here, because as you can see, it passes frequencies in this band here and then it drops off on either side. And of course, you know, we've got a traditional band-pass op-amp filter there and you can get different

**Dave Jones:** responses in terms of like a low pass, high pass, and the band pass. And you can also get band stop filters as well. So, we I got to try and see if we can get this response on our oscilloscope.

**Dave Jones:** Now, ordinarily you wouldn't be able to do this because an oscilloscope does not display anything versus frequency. It displays it versus time. And of course we've got different types of axes as well. You can have a logarithmic dB

**Dave Jones:** vertical amplitude axes here and you can also have a decade or logarithmic or octave or linear axes for the frequency. So, we're going to see if we can get linear for for starters and then possibly get a logarithmic one as well. Then you might

**Dave Jones:** be thinking, well the oscilloscope has FFT built in. Well, that's not going to really do the job in this case. So, we're going to actually trick the oscilloscope into displaying frequency on its horizontal axes. It's a lot easier than you think. Let's

**Dave Jones:** go. Now, what I've got here is my Rigol function generator. I've got it set to do a sine frequency sweep. So, it's in sine wave mode, it's in sweep mode, and I've got it set here for a 1 second

**Dave Jones:** sweep. So, it takes 1 second to do the entire frequency sweep and it starts at 1 hertz and goes to 100 kilohertz. So, I mean these are just round numbers I've picked. You can do it for, you know,

**Dave Jones:** almost any frequency range you desire. So, we've got a 1 second sweep. So, if we go and look at that signal, this is what it's generating. I mean it starts out at 1 hertz and it goes all the way

**Dave Jones:** up to 100 kilohertz there. Now, if we hook this up to a filter, which I will do right here, I'll insert a filter and you can see it actually changing. We can actually see that there. It's starting off, and it's going down like that. And

**Dave Jones:** you can sort of start to see a response plot on this. And it's it's kind of sort of there. It's kind of sort of doing it, but we're going to make it much nicer. How are we going to do that? Well, we're

**Dave Jones:** going to do that by something I've mentioned before, the sync or trigger output on the function generator. So, what I've got that hooked up to is channel two on the scope here. Here we go, and we'll turn on channel

**Dave Jones:** two, and it generates a sync pulse when it starts at frequency sweep and when it ends. Like that. During that whole period one complete cycle of that trigger pulse, that is our entire frequency range. So, from there it starts out at 1

**Dave Jones:** Hz in this case that I've programmed in, goes up to 100 kHz. So, that's our entire frequency range there, and you can see that we have a response in there. And that is a real linear amplitude response of the

**Dave Jones:** filter I've got put in here. And if I turn the filter off there we go, we get a straight line, of course, because the amplitude from the function generator is flat across the frequency range. So, what we want to do

**Dave Jones:** is at the moment we're triggering off our channel one signal up there. We don't want to do that triggering off our actual signal. We want to want to trigger off this nice clean perfect trigger or gating pulse down here. So, we go into trigger,

**Dave Jones:** we'll trigger off channel two. Thank you very much. Positive sloping edge, and bingo, we'll now find that we have a signal, let's that is triggered every single time. It starts here, you can see the triangle up there, and it's repetitive, and we can

**Dave Jones:** get our frequency response plot on the scope like that. So, but really we want to actually get the largest dynamic range possible, and also um measure over and you know get it sort of like full screen there. So, we're just

**Dave Jones:** going to change our vertical down to here like this. So, the ground point is just right the bottom there. Bang. There it is right there, and we'll change our horizontal. And because we're set it for 1 second, it's going to be an exact multiple. So,

**Dave Jones:** it starts rising here, goes there, and it rises just there again. So, as it turns out, it we can maximize because we've chosen that nice round value which fits on our screen of 1 second period at 100 milliseconds per division. We've got

**Dave Jones:** 10 divisions on the screen. Um that is our complete frequency sweep from 1 hertz up to 100 kilohertz, and bingo. Look, we've got our frequency response plot. Because half of the waveform is below, we we don't want that. We want that set below the ADC

**Dave Jones:** range, and now we're maximizing the full use of our ADC. Now, what I've got here is a very simple RC filter for starters. I've got a 2.2 nanofarad cap. It's just what I had handy, and I've got my decade

**Dave Jones:** resistance box here. Got it set to 10 K, and we'll be able to double-check these values with the simulator and see if we get exactly the same response plot. So, let's go up here and have a look at our response with those

**Dave Jones:** two values in there. And look at that. It's Remember, this is a linear range on the bottom here. So, this is a linear scale, and also the amplitude is linear as well. But we'll be able to do log

**Dave Jones:** frequency scale in a minute. So, as you can see, we get a response here that drops off and then levels out like that. Now, to get the full maximum use of the screen here and the ADC, remember the

**Dave Jones:** scope's only got a lousy 8-bit ADC in it. So, it's not nearly as good as a real, you know, a dynamic signal analyzer or FFT analyzer with a much higher dynamic range ADC in it. But, we can get our frequency response plot like

**Dave Jones:** that. No problems at all. And if I adjust the fine vertical scale there just so it, you know, I could I could tweak the function gen value as well, but I think that's pretty close to the maximum value there. So, we're getting the full

**Dave Jones:** screen in there and it's going down to, you know, uh you know, maybe 7% of the full value up there, maybe 8% of the full scale value at 100 kHz. Now, let's see if we get that identical response plot on our

**Dave Jones:** simulation. All right, I'm running LTSpice here. I've got the same values, 10K and 2.2 nF there. I've got my um uh source set up to uh sweep. So, let's go into edit simulation command. I'm doing AC analysis, which is going to give our

**Dave Jones:** bode plot. The type of sweep we want is linear because that's what we're doing with our function generator. We're doing a linear sweep and the start frequency is 1 Hz and the stop frequency is 100 kHz, exactly the same as how we've set

**Dave Jones:** up on our function generator. So, let's give that a go and we'll be able to get our bode plot if we run it. There it is. Let's actually go into full screen there and bingo, look at that. We get exactly the same response.

**Dave Jones:** Actually, let's go fit this to manual limits here. Let's say 1 V 100 mV. Uh this we're setting up the just the vertical axis here. Vertical axis is linear, exactly like it is on the scope. And look at that. That is exactly if you

**Dave Jones:** actually scale that to the correct uh dimensions and you overlaid that over the that oscilloscope screen response, you would get exactly the same response. Bingo. Perfect. And once again, down here this value down in this uh bottom right corner around here at 100

**Dave Jones:** kHz is there there it is. It's around about six or seven or so uh percent of the full scale value. It's exactly the same. So, our little trick works. We're able to get frequency response or Bode plots on an oscilloscope.

**Dave Jones:** Piece of cake. But what happens if we want to get a log response and our frequency here? Well, let's have a look at what it will look like on the simulator here. We'll just uh manual limits again and we go

**Dave Jones:** logarithmic horizontal axis here. And bingo, it looks like that because it starts to roll off at around about here, you know, 0.707. And it goes down to the same value at 100 kHz of course, but it looks different. It's exactly the same

**Dave Jones:** response, but it's plotted on a logarithmic axis. Can we get that on our scope? You bet we can. All we have to do for that is go into our sweep menu here and sweep type linear. We don't want linear, we want

**Dave Jones:** log. And ta-da! Look at what we've suddenly got here on our scope. Magic. And once again, if you overlay the two, scale them correctly, you would get exactly the same response. Look at that. And obviously down at the, low end

**Dave Jones:** down here, of course, you know, it's you've just got to use your imagination to extend it down at that, uh, low frequency with this logarithmic axis, but there you go. Now, of course, we have to assume that the line is, you

**Dave Jones:** know, the peak of the waveform here. If you wanted to actually get an actual line like that, you would have to have some sort of, uh, peak detector or RMS, uh, converter or something like that on the input to your scope so that instead

**Dave Jones:** of showing the actual waveform, it shows the peak or the RMS value. And then, you would actually get a line just like you do on the, um, simulators. So, although this works a treat, I thought we'd, just for kicks, do a, uh, bandpass filter as

**Dave Jones:** well. So, I'm going to lash up this little thing. It should be centered around about 50 kHz or so, uh, with like a 10 kHz, um, passband or thereabouts. So, you know, that will should be without anything on

**Dave Jones:** our scope, it should be smack in the middle somewhere there. The tolerances will be a bit off, may not have the exact values, but we'll get the idea. And here we go, lashed up on the breadboard. I took a few liberties with

**Dave Jones:** the, uh, values, but, uh, we're still going to get a bandpass response somewhere within that range. Let's check it out. Tada! And here it is. Beautiful. Look at that. It's, um, happens to be around about, uh, I don't

**Dave Jones:** know, 18 kHz or thereabouts. So, look at that, beautiful response. And, uh, of course, we could, uh, let's adjust our frequency range on this thing. So, let's go into our end frequency, for example. There it is, it's highlighted. Let's go to, uh,

**Dave Jones:** well, let's just, uh, go to 40K, for example. There we go. And tada! We're back. So, there you go. We're now from uh, 1 Hz to 40 kHz. So, we're because we're doing a linear sweep again, we've got

**Dave Jones:** off log. So, we're doing 4 kHz per division here. So, 4 8 12 16 Yeah, you know, it was around about that 18 that we guessed before. Haha, love it. All right. Now, let's say we wanted to zoom in on that. I mean, we can do that

**Dave Jones:** with the horizontal, of course, but the proper way to do it is to adjust our sweep frequency range. Instead of going from 1 Hz to 40 kHz we've got at the moment, i.e. 4 kHz per division, let's go from say 8 up to I don't know 28 or

**Dave Jones:** something like that. So, we jump on over here. We can just go from the start from 8 kHz to end frequency 28 kHz and tada! There it is. We've swept over a different frequency range. And of course, once again, we

**Dave Jones:** would scale our we would use our vertical vernier here and scale that peak to full scale so that we can get a So, you know, so that that's our reference point and then we can measure various amplitudes reference to the full

**Dave Jones:** scale using the graticule and all the cursors. Brilliant. And of course, if we zoom that out like that, we can actually get the multiple responses like that. But of course, you're just wasting your horizontal screen real estate there. So,

**Dave Jones:** you really want to just make sure you choose that exact time period to fit your 10 horizontal divisions and you can divide nicely and just remember to keep the vertical adjusted with your vernier. That's what your vernier is good for.

**Dave Jones:** Two full scale or you can adjust the amplitude on the function gen as well. And of course if we try to get this response the old fashioned way by just sweeping our function gen here through the entire range and then manually

**Dave Jones:** recording down on a bit of paper, you know, each value at each specific frequency and then you know, you might get you know, 10 or 20 points or even more 50 points or something like that. Then you could get your frequency

**Dave Jones:** response and it would look you plot it on Excel or whatever you get exactly the same thing. So there you go, a poor man's bode plotter using your oscilloscope. I like it. It's neat. But yeah, there's going to be some

**Dave Jones:** limitations, but look, we are getting a response we can capture that you know, to JPEG or whatever and we can label the axes and do everything and that would be a perfectly adequate waveform to put in your report or

**Dave Jones:** something like that. So you know, it is certainly doable and it's real time. That's the thing. I mean, I can go in there and touch Let me sort of touch some caps or something like that. Let's have a

**Dave Jones:** play around. Can I do that? Yeah, there we go. And we can see it all changing in real time, which is fantastic. I like it. So it does actually work, but yes, there's going to be some limitations. I mean, the main

**Dave Jones:** one of course, you know, we're only talking about an eight put eight bit ADC in this thing. So we don't have a huge dynamic range and no, you can't really use the high dynamic range functions, the boxcar averaging function of this thing. I

**Dave Jones:** mean, if we go in there and we turn that on, we're really going to screw that up with the high resolution mode on this thing. It's not going to work that well at all. And of course you can still turn

**Dave Jones:** on that peak detect and capture uh and things like that. And uh so it it does actually um work. Just keep it in normal mode. You'll be able to do this on your analog uh scope as well. Don't

**Dave Jones:** necessarily have to do it on a digital. We're using nothing fancy, just a regular oscilloscope. And of course the good thing with this is that you can use it over a fairly wide frequency range. Depends on what your sweep generator is

**Dave Jones:** capable of and um the bandwidth of your oscilloscope. But if you know, don't go near the you know, the upper frequency of it. Don't go near the uh maximum sample rate of your oscilloscope cuz you're going to start aliasing. So, you

**Dave Jones:** don't want that to happen, but there you go. I think this is a neat little um it's not really a hack. It's just a neat little um alternate use for your oscilloscope. I like it. So, if you want

**Dave Jones:** to discuss it, jump on over to the EEVblog forum. And remember, if you like it, please give it a big thumbs up. And don't forget, follow me on Twitter cuz that's where I rant a lot. Catch you next time.
