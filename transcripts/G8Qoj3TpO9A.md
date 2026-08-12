---
video_id: G8Qoj3TpO9A
title: EEVblog #1223 - Oscilloscope Standard Deviation Noise Measurement
url: https://www.youtube.com/watch?v=G8Qoj3TpO9A
source: youtube-asr
timestamps: {"0": 0, "1": 23, "2": 38, "3": 58, "4": 71, "5": 96, "6": 105, "7": 129, "8": 141, "9": 153, "10": 163, "11": 176, "12": 191, "13": 204, "14": 220, "15": 236, "16": 261, "17": 275, "18": 292, "19": 306, "20": 320, "21": 334, "22": 346, "23": 368, "24": 386, "25": 405, "26": 419, "27": 447, "28": 458, "29": 472, "30": 492, "31": 505, "32": 518, "33": 536, "34": 548, "35": 560, "36": 580, "37": 589, "38": 606, "39": 617, "40": 632, "41": 646, "42": 663, "43": 676, "44": 691, "45": 709, "46": 721, "47": 736, "48": 747, "49": 762, "50": 778, "51": 796, "52": 818, "53": 832, "54": 848, "55": 862, "56": 888, "57": 910, "58": 926, "59": 954, "60": 967, "61": 981, "62": 990, "63": 999, "64": 1016, "65": 1028}
---

**Dave Jones:** Hi, in my previous video reviewing this 1 GHz Siglent SDS5000 series oscilloscope, I made a little bit of an oopsy in the noise measurement compared to the Rohde & Schwarz one over here, which I was just comparing the input channel noise of the two and only a couple of people actually spotted the mistake.

**Dave Jones:** So, let's see if you can actually spot it. Now, of course, to measure noise on a waveform there's two ways you can specify. You can specify the peak-to-peak noise or the RMS noise and usually like most people will probably use the RMS noise.

**Dave Jones:** You could you know, it depends how you want to do it, but peak-to-peak you can see like all these little peaks in there and if we stop that you could actually potentially see like little tiny spikes in there that can contribute to the peak-to-peak noise and that really is not hugely relevant in a lot of cases.

**Dave Jones:** That's why often the RMS noise will be is a better measure when you're comparing like two different oscilloscopes in this particular case. And of course, the RMS value we've got the statistics here.

**Dave Jones:** I'll run that again. The mean value of our RMS is about 94 93 microvolts. So, you would say that the Siglent scope has an input noise of in on this particular range on the 1 mV range with a 2 meg of memory at 1 microsecond per division with the bandwidth, which is actually 200 MHz.

**Dave Jones:** It's not 1 GHz because on the lower 1 mV per division of 500 microvolts per division range, you don't get the full bandwidth out of it. It's a bit of a trap for young players.

**Dave Jones:** You only get a more limited bandwidth on this Siglent scope anyway. So, 200 MHz bandwidth, all those settings, about 94 microvolts, whereas the Rohde & Schwarz over here, if we go over and have a look, the same settings, I've got 1 mV per division, I've got 1 microsecond per division, I've got 2.5 gig samples, so roughly the same amount of memory, but our RMS noise is mean is about 323 microvolts.

**Dave Jones:** So, you might think this Rohde & Schwarz is much worse than the Siglent. Well, the Siglent's much better than the Rohde & Schwarz. But, that's not the case. I've made an oopsie here.

**Dave Jones:** And this is what happens when Dave doesn't engage his brain when he's shooting videos, and it it could easily happen. And I I knew this, but I just I goofed it in the video.

**Dave Jones:** So, let's look at it. So, pause the video now and see if you can figure out why the Rohde & Schwarz RMS noise is much higher than the Siglent.

**Dave Jones:** It is It's an important and subtle point that makes a huge difference. All right, did you guess it? Did you get it? Did you get it? Well, I'll tell you all about it.

**Dave Jones:** And looking here, you'll see that you can see C1, it means channel one, that is right in the center there, and that would be our ground point. And you can see that there's a slight little DC offset there.

**Dave Jones:** And that is a problem because if you're measuring RMS with a DC offset, by definition, root mean squared does not take out that DC offset. It's going to include that DC offset value.

**Dave Jones:** So, that's why there's a small amount of DC offset. Look, it's 1 mV per division, it's only a couple hundred microvolts, right? It's it's down it's almost bugger all, but it makes going to make a huge difference, and it's going to add on and contribute to that mean value.

**Dave Jones:** And you might think, "Aha, Dave, dummy, it's because you've got DC coupling of your input." Well, let's go in to AC coupling. Turn my channel off. Let's go into Come on, give me my menu.

**Dave Jones:** There you go. AC coupling, the statistics have reset themselves, but it's still there. It hasn't removed that DC offset cuz that DC offset is actually after the input AC coupling cap, which is when you select AC mode here, there's a relay in there, either a mechanical or electronic relay that will switch in an AC coupling capacitor.

**Dave Jones:** So, the DC offset is actually after that AC coupling cap. It's residual within the input amplifiers and it'll vary with temperature and time and everything else. So, if we made wait another hour or something, that DC offset might drift up.

**Dave Jones:** And you can see that the signal over here just so happens to have at this particular time, it could drift, I don't know, hardly any DC offset, maybe and maybe a a width of a [ __ ] paper over ground there.

**Dave Jones:** So, this one has a slight probably a slight DC offset value, but it's not really contributing to that noise, not nearly as much as a Rohde & Schwarz. So, that's why, aha, we're getting that high mean value.

**Dave Jones:** But, there's actually a measurement on these oscilloscopes that we should use instead of RMS. Let's have a look. All right, so our AC coupling didn't fix it, but we actually have a different type of measurement from RMS.

**Dave Jones:** It's still RMS, but it's not RMS. I'll get into it. Let's press the measurement button and go up and have a look. And of course, we can we've got a volts peak to peak at the moment and RMS, and we can choose in many different types.

**Dave Jones:** So, let's get a third measurement here and we can choose the type here and we can go in and have a look. At the moment, we're using peak to peak and we're using RMS, but there's one called standard deviation.

**Dave Jones:** And you can I love the rodent Schwartzy cuz it actually shows you the actual formula. And in this particular case, you can see that this standard deviation formula is almost identical to this the formula that we get for RMS here, root mean squared, which is the square root one on N the sum from one to N and square of the values.

**Dave Jones:** Anyway, this is not going to be a math lesson. Anyway, let's standard deviation is very similar. Okay, except it's one on N minus one. It's the same range, so you're summing the same values, except it's instead of XK here, it's XK minus the mean value of X.

**Dave Jones:** And it's got the square in there as well. So, it's actually subtracting out effectively the DC value. So, what this standard deviation measurement is is not to be confused with a graph of standard deviation, you know, the bell curve and all that uh sort of stuff.

**Dave Jones:** It Let's not go into it. This formula here is actually what's called a sample standard deviation. Uh not to be confused with a population standard deviation. And I won't go into the differences cuz then we have to get into a whole math lesson, and I really hate math.

**Dave Jones:** It's Anyway, this standard deviation is also called AC RMS. So, it's exactly the same as the RMS, but instead of including DC values, it actually simply removes any You can think of it as removing the DC offset or having an AC coupled RMS value, but instead of physically decoupling with an AC capacitor in here, it does it in the formula.

**Dave Jones:** It does it in the software. It removes that DC value. So, if we select our standard deviation, bingo. We're going to Well, let's reset our stats. There we go.

**Dave Jones:** And bingo, we now have our mean value of about of the standard deviation, and the standard deviation is actually a square root of the variance. But, once again, all you math nerds go go for broke down in the comments.

**Dave Jones:** I won't I won't try and explain it. But, the mean value is now 96 microvolts. Practically identical to the Siglent. In fact, because this is a higher bandwidth scope, this is actually 350 MHz, cuz you do actually on the 1 mV per division range on the Rohde & Schwarz, you get the full 350 MHz bandwidth.

**Dave Jones:** There's no limitation like there is on the Siglent. So, this is actually a better result because, as a rule, for the higher bandwidth you have, the more inherent noise you're going to get.

**Dave Jones:** It's It's just a function. Once again, there's lots of advanced math behind that and and theory, and we won't go into it. But, a wider bandwidth. So, technically, this is a lower noise scope for a given bandwidth than the Siglent.

**Dave Jones:** There you go. I simply forgot that there was this DC offset up there. I didn't notice it. Oh, and and I should have, cuz it's really obvious. And also, I should have known, if I was engaging my brain, that 330 microvolts, well, look at the Look at the actual level.

**Dave Jones:** Just, you know, mark what Use your mark one eyeball and compare the thickness of that line to the one over here on the Siglent, and you can see that they're You know, they're they're practically identical, really.

**Dave Jones:** In fact, the Siglent might look a bit thicker, but you know, it's like slightly There's nothing in it. So, I Yeah, if I was thinking, I would have gone, "Well, it's obviously 337 microvolts can't be correct value for the RMS.

**Dave Jones:** So, oh, oops, there's a DC offset in there. Ah, I should be using the standard deviation or AC RMS." So, let that be a lesson to you. You should be using AC RMS when you're doing these types of noise measurements, where you need to remove any residual DC offset.

**Dave Jones:** So, let's go back to the Siglent here and see if the Siglent has the AC RMS, as it's often called. Sometimes it's not called standard deviation. It'll just be called AC RMS.

**Dave Jones:** So, let's go into the type here, and yes, it does standard deviation. There it is. It's also for both the RMS value here and for the standard deviation value, they have also what's called cycle RMS and cycle standard deviation.

**Dave Jones:** That's if you want to measure it over the one cycle on your screen. But, of course, we don't have a cycle here. We're not inputting a sinusoidal or other repetitive waveform.

**Dave Jones:** We're measuring noise. So, the cycle standard deviation and cycle RMS just won't work. It just won't give you anything. So, we can put standard deviation. So, if we get rid of that, bingo, we now have our standard deviation here, and it's actually smaller.

**Dave Jones:** So, there you go. If we're doing it, now we're doing an AB, a true AB comparison. The mean is about 65 microvolts. So, the Siglent is actually lower, but as I said, the Rohde & Schwarz is higher bandwidth.

**Dave Jones:** So, you could probably run the numbers there and kind of let's just call them pretty equivalent in terms of noise floor. But, if you really want to do it properly, well, let's go into our channel menu here and let's get we can set the bandwidth on both of them to 20 meg.

**Dave Jones:** Okay, so now I've got 20 megahertz bandwidth, and you can see that it's much lower noise. The mean is now 38 microvolts on the Siglent, and and the Rohde & Schwarz, what have we got?

**Dave Jones:** 44 microvolts. There you go. So, actually, the Rohde & Schwarz is a bit higher noise for the 20 for the fixed 20 megahertz bandwidth there. And curiously, of course, you've got the standard deviation of the standard deviation there.

**Dave Jones:** That's confusing and we won't go into the details anyway, but just remember the standard deviation you'll find in the measurement menu like this. So, you press measurement and bingo and you can go into the type and the type of measurement that thing if it says standard deviation on your particular scope, just remember it's AC RMS.

**Dave Jones:** That's the best way to remember it because it's functionally what it is. So, the best way to think of that is a standard deviation is basically the spread in the numbers of the AC RMS value.

**Dave Jones:** If that makes sense. Maybe you know, if you got a better way to explain it, leave it in the comments down below, please. Okay, so a better example of this is if we actually put in a real signal.

**Dave Jones:** In this case, I've got a 1 MHz sine wave here. I'm on 1 V peak-to-peak and I'm actually feeding in from my generator up here. You can see on my generator there, 2 V RMS and we've got a 2 V DC offset.

**Dave Jones:** So, let's just reset the statistics there. The statistics for I can talk. Hardly. So, you can see our ground point over here is actually shifted up where 1 V per division.

**Dave Jones:** So, 1 V 2 V, you can see there's a 2 V DC offset here. The waveform has been shifted up that DC by 2 V DC there. And if you have a look at the RMS value here, then let's reset our statistics to make sure I've got it right and look at the mean value.

**Dave Jones:** It's 2.81 V RMS. So, of course we know we're only feeding in 2 V RMS from our signal generator. It's giving us an error. Well, in this particular case, it's not an error because we've chosen the RMS measurement which by definition of RMS includes the DC component.

**Dave Jones:** But you can see if we choose our standard deviation measurement which is, as I said, AC RMS, it removes that DC offset there without having to AC couple. Remember, we're still DC coupled on our input, so we're seeing our offset like that, but we're effectively AC coupling the signal in software.

**Dave Jones:** So, it gives us almost precisely our two part our 2 V RMS there, 1.98 V. Near enough, well within spec. By the way, you can often now remove these residual DC offsets by actually self-calibrating the oscilloscope.

**Dave Jones:** And I'm just running through the self-alignment process at the moment with the Rohde & Schwarz here. So, like if you move your scope to say like a much different temperature environment or something like that, you know, you go from a 20° lab and then you go use it outside at 0°.

**Dave Jones:** You know, if you really want the best accuracy, you should probably do a re-self calibration. And bingo, sure enough, after the calibration, the RMS value now is 84 microvolts.

**Dave Jones:** You can see that there's basically no DC offset anymore. So, yeah, I just hadn't self-calibrated the scope. Self-calibrate yours, it's worth it. And if we actually compare this to our multimeter here and we're on regular AC mode, I have had to reduce the frequency down to 1 kHz for the bandwidth of the meter here, but you can see that we're at precisely 2 V RMS because the AC on

**Dave Jones:** your multimeter actually physically does AC coupling. So, it removes that DC offset and you only get that standard effectively it's doing that standard deviation measurement. And if you want to include like a RMS measurement, that's not true RMS, that's actually what's called AC plus DC mode.

**Dave Jones:** So, DC plus AC, if you do that, bingo, 2.8. So, you can see it's identical, 2.8 there and the standard deviation. And let's go back. If we actually go to DC, it'll be 2 volts like that because that is the DC offset.

**Dave Jones:** It's measuring the DC offset. So, there you go. That's just a comparison with the multimeter. Multimeter can do the same thing, but don't confuse DC plus AC mode with true RMS because true RMS means it's just measuring the RMS value will be correct for any wave shape, be it a triangle wave or whatever or some weird convoluted waveform depending on the crest factor, but let's not go into that.

**Dave Jones:** True RMS means it's valid for the RMS values are valid for any wave shape, any waveform shape, not just sinusoidal. But, you want DC plus AC if you want to include that DC offset.

**Dave Jones:** So, which one is more relevant? The RMS that includes the DC value, DC plus AC, or your AC RMS value? Well, it depends on your particular application. There's no right or wrong.

**Dave Jones:** They're both valid. It's just depends on what what your application is, really. So, there you go. That's a bit of a little trap for young players, and it's important to realize the difference between AC RMS and RMS.

**Dave Jones:** So, have a play around with your scope. Let us know what your particular scope is cuz as I said, it may not be called standard deviation. It could be called AC RMS.

**Dave Jones:** And usually and often they won't call the like say DC RMS. They'll just call it RMS because by definition of the formula, it's going to include DC. But, standard deviation could be called AC RMS on your particular scope or it let us know if your scope doesn't have it at all.

**Dave Jones:** So, anyway, I hope you found that interesting. If you did, please give it a big thumbs up. And as always, discuss in the comments down below or over in the EV blog forum.

**Dave Jones:** Catch you next time. Mhm.
