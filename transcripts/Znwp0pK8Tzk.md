---
video_id: Znwp0pK8Tzk
title: EEVblog #601 - Why Digital Oscilloscopes Appear Noisy
url: https://www.youtube.com/watch?v=Znwp0pK8Tzk
source: youtube-asr
timestamps: {"0": 1, "1": 22, "2": 40, "3": 54, "4": 66, "5": 77, "6": 89, "7": 103, "8": 115, "9": 129, "10": 140, "11": 150, "12": 158, "13": 171, "14": 184, "15": 196, "16": 208, "17": 222, "18": 248, "19": 270, "20": 283, "21": 304, "22": 321, "23": 349, "24": 364, "25": 373, "26": 388, "27": 401, "28": 422, "29": 435, "30": 462, "31": 470, "32": 479, "33": 487, "34": 497, "35": 512, "36": 541, "37": 563, "38": 579, "39": 587, "40": 602, "41": 615, "42": 627, "43": 641, "44": 651, "45": 669, "46": 695, "47": 707, "48": 721, "49": 732, "50": 744, "51": 764, "52": 773, "53": 783, "54": 794, "55": 806, "56": 826, "57": 838, "58": 849, "59": 868, "60": 880, "61": 894, "62": 931, "63": 941, "64": 957, "65": 973, "66": 985, "67": 1008, "68": 1022, "69": 1035, "70": 1047, "71": 1059, "72": 1072, "73": 1090, "74": 1098, "75": 1121, "76": 1132, "77": 1147, "78": 1163, "79": 1180, "80": 1192, "81": 1209, "82": 1220, "83": 1231, "84": 1240, "85": 1253, "86": 1271, "87": 1281, "88": 1297, "89": 1312, "90": 1342, "91": 1354, "92": 1378, "93": 1392, "94": 1408, "95": 1419, "96": 1431, "97": 1442, "98": 1456}
---

**Dave Jones:** Hi. Now, there's a myth regarding oscilloscopes that simply will not go away. And that is that digital scopes, be they ancient like this Tektronix TDS 210, sort of a bit more modern like this Rigol 1000 E series, or something like this, you know, really kickass high-end Tektronix 3000 series just released.

**Dave Jones:** And the myth is that your old traditional analog oscilloscopes, like this Tektronix 2225 or any analog oscilloscope, is, in {quote marks}, lower noise than a digital scope. And well, that's not actually true.

**Dave Jones:** And I want to explain it to you today. So, let's start off by taking a look at this Tektronix 2225. Nice analog oscilloscope, 50 MHz bandwidth, fairly typical analog scope.

**Dave Jones:** And look at that trace. Look at it. It's just beautiful. Look how fine that is. I've got no input connected to these scopes or any of these scopes, as we'll see.

**Dave Jones:** And they're all going to be, by the way, set to the same volts per division, 1 V per division in this case, and 1 ms time base, just so that we're consistent across all scopes.

**Dave Jones:** But look at that. You might think, "How beautiful is that? There's no noise on that whatsoever. These analog scopes are so massively low, they practically don't have any noise at all.

**Dave Jones:** They're brilliant." And then you go to something like this ancient TDS 220, 100 MHz bandwidth analog scope, one of the first real-time bandwidth scopes on the market. And well, take a look at the waveform.

**Dave Jones:** It's, you know, it's a bit fuzzy. Look at the noise on there. You You know, anyone would say that is noisier than that than that analog Tektronix 2225 we saw before.

**Dave Jones:** And then we've got this 6-7 year old Rigol DS1052E. It's still sold. It's almost obsolete, but once again, it's a even though it's a 50 MHz bandwidth, the firmware's been hacked.

**Dave Jones:** It is actually a 100 MHz bandwidth front end. And this is a pretty you know a good example of a modern low-cost, you know, bottom of the range DSO.

**Dave Jones:** And well, look at the waveform. Once again, all these time bases are identical. Volts per division are all identical. And look, and we're getting See See those little occasional blips in there?

**Dave Jones:** Look at that. That's you know a good four pixels high or something. All that noise. You would think, well, that one's actually slightly worse than the Tektronix TDS 220.

**Dave Jones:** And then we'll have a look at this brand spanking new Tektronix 3000 series scope. Very expensive scope, you know, over $10,000 worth. Just released. It's a quality Tektronix brand.

**Dave Jones:** You'd expect this to have, you know, be a really well-designed scope. And well, once again, same time base and same voltage setting, no input. Look at the waveform. Uh, it's all over the shop.

**Dave Jones:** Right? That is the worst of these four scopes. It looks like they got progressively worse or digital scopes have got progressively worse as time has gone on. Well, is that fact or fiction?

**Dave Jones:** So clearly, I know what you're thinking. Dave, you're talking rubbish. I can see it with my own eyes. This one analog scope, traditional analog scope, is definitely the lowest noise scope.

**Dave Jones:** This one is the next best, the ancient digital, then the slightly more modern digital is probably better again. And this latest modern one is just absolutely hopeless. I can see it with my own eyes.

**Dave Jones:** Well, I'm here to tell you that your eyes aren't deceiving you. Yes, this is better, but you're not seeing the whole picture. You're not thinking fourth dimensionally. Now, a thing you must remember with a traditional analog scope is, obviously, it has no storage capability, and the brightness of the image on the screen is going to be determined by how long the trace spends in that position.

**Dave Jones:** So, if we had just had a little tiny runt pulse that went boom up there like that, and it happened one in a million times, you're never going to see it on an analog scope because in each sweep, assuming that the trigger actually, uh, uh, you know, it was actually able to be displayed, it'd only be displayed one in those million sweeps or whatever.

**Dave Jones:** So, you wouldn't see it. It wouldn't be there long enough to produce a bright image on the screen like we're seeing with that trace there. And yes, I can make that trace fatter by turning up the brightness.

**Dave Jones:** Now, that is like a blooming effect on the scope, but it's not just that. It's also displaying more information when you make it brighter. And I've shown that in my previous video, as I mentioned, which I'll link in down below, how your analog oscilloscope can be hiding the true signal.

**Dave Jones:** So, in this respect, analog scopes aren't nearly as good as digital scopes for capturing the actual hidden data in there, the hidden signal in there. So, somewhat confusing, but a lot of people make that mistake thinking analog scopes display the signal better.

**Dave Jones:** Not necessarily so. Watch the other video, and you'll find out why. So, the bottom line is any noise on the analog amplifier input down here or on the signal that you're feeding in, any noise which is uncorrelated to your sweep speed or your trigger, i.e., it's just randomly appears, it's not synchronized with the sweep, then it's going to appear quite dim or non-existent because it's not going to

**Dave Jones:** show up all the time. And that is why an analog scope will always show this beautiful clean signal like that. Effectively, what it's doing is averaging your signal by way of brightness.

**Dave Jones:** But let's take a look at the first example of our digital scope here, ancient Tektronix TDS 220. But as you should know, a digital scope actually samples the signal then displays it.

**Dave Jones:** So any noise or anything else in there is going to get captured in that data acquisition and displayed. Now, in this case, this signal looks relatively clean. You can see little noise artifacts on there.

**Dave Jones:** You can see it. Right? But it's not that bad. You would think that's not too bad at all, especially compared to the Rigol one above it. But here's the first fact you need to know about digital scopes.

**Dave Jones:** The amount of information you're seeing displayed on that screen there is going to be determined by the sample memory depth. And with this ancient scope here, the 200 series TDS, it's only got 2.5 K of sample memory, practically bugger all.

**Dave Jones:** And that is why we're getting a nice clean signal there. So that's fact number one. And I can demonstrate that on this Rigol here. Now, you can see that it looks a little bit worse than the Tektronix one, okay?

**Dave Jones:** 100 MHz bandwidth, same time base, same voltage, no input, all those spikes, but this Rigol DS1052E has 1 meg of sample memory. So for any given time base, in this case 1 ms per division, then it can capture much more high frequency noise and actually display it on the screen.

**Dave Jones:** And that's exactly what it's doing. And I'll show you that. If we go into the acquire menu here, if I it's on long memory at the moment, so it's got that one meg points.

**Dave Jones:** It's using that one one meg points of memory. But watch what happens to this signal if I drop it down to short memory. I think it's only a couple of K.

**Dave Jones:** It might be 10 K on this scope, but we'll see a difference. It's going to clean it up. Not by a huge amount, but it will. You'll be able to see it.

**Dave Jones:** Watch. See? It dropped. Whoop. The scope's memory depth is 8 K or 16 K in normal mode and will be 512 or 1 meg in long memory mode. There you go.

**Dave Jones:** It answered that for us. So, you can see that difference there. It's going It's dropping at least a whole line of pixels there. It's thinner by at least one pixel one least significant bit if it's displaying 256 for example.

**Dave Jones:** That's because in long memory mode, it is capturing more of that high frequency band that high frequency noise, and it's and it's putting it on the screen. So, it's showing you more of a true representation of the signal than the analog scope is because this this that high frequency data in long memory mode wouldn't be displayed on an analog scope because it wouldn't be it wouldn't be visible.

**Dave Jones:** It wouldn't be on the screen long enough to light up those phosphors, and that's why an analog scope appears to have less noise, but it actually doesn't. And fact number two that you should know about digital scopes or any scope, even analog ones, the higher the bandwidth, the greater the inherent noise of the amplifier and other front-end circuitry.

**Dave Jones:** So, in this case, we can see this by turning our bandwidth limit off and on. At the moment, this Rigol scope is a 100 MHz bandwidth, but I if I turn this bandwidth limit on, it'll drop down to 20 MHz bandwidth, and we should see this noise drop a little bit more.

**Dave Jones:** You won't see it a huge amount on this, but we'll be able to see it on our high-end Tektronix in a second, but I'll show you. There we go.

**Dave Jones:** There's slightly less. You can see just on the bottom of the waveform there, there's little pixel chunks taken out, so it's slightly less noise. Look at that. Hey, fact number two.

**Dave Jones:** Now, on our brand new Tektronix MDO 3000, we'll be able to see both of these things much better than we could on the previous one. Now, as before, exactly the same time base, exactly the same voltage input, and the noise looks pretty horrible.

**Dave Jones:** Look at that. But, if I call up channel one here, look, the bandwidth is full, and the bandwidth of this scope is 1 GHz. Got a massive bandwidth. So, the first thing we can do is change this 250 MHz.

**Dave Jones:** We'll see the noise maybe drop by a smidge, and it might be hard, but we'll give it a go. Here we go. 250. Yep, slightly. You can see that grow just a little bit there and 250.

**Dave Jones:** We drop it down to 20, same as we did on the Rigol. It's less noise again. Look at that. So, I'll put that back to its full 1 GHz bandwidth.

**Dave Jones:** We'll go to the acquire menu, and we'll now muck around with the record length. Look, it's 10K at the moment, okay? So, not a huge amount, okay? Now, if we vary this, let's drop it down to 1,000, just like we had on that ancient Tektronix TDS 200 series.

**Dave Jones:** Watch the noise on the waveform. Bingo. Look at that, it's dropped significantly. And once again, if we uh drop the bandwidth down to 20 MHz, look at that, our line is exactly almost exactly identical to what we were getting on the ancient TDS 220, because our uh those two rules, the bandwidth makes a difference, and also the amount of the sample rate showing that high frequency content.

**Dave Jones:** But we've dropped both of those down, and bingo, our noise has magically vanished. Look at that. I'll turn it back. Now, watch this. So, we're back to our 1 gig bandwidth.

**Dave Jones:** So, we're now on 10 K. Let's go out to 100 K. Look at that, the line gets thicker. 1 meg, line gets thicker again. 5 meg, all you probably Yeah, you won't see might not see much difference there, but 10 meg that is as thick as it's going to get.

**Dave Jones:** Look at that. We're on 1 V per division with no input whatsoever and a 1 GHz bandwidth. You would think this is the worst scope in history, but it's not.

**Dave Jones:** It's actually showing you real data. So, there you go. There's nothing inherently wrong with digital scopes. You've just got to understand those two reasons why they can show more noise in {quote} marks.

**Dave Jones:** It's not really noise. It's actually real data that's there, which is ordinarily being hidden on an analog scope, because that analog scope just averages out over its screen. So, in that respect, digital can actually be better, cuz you can easily capture that high frequency data that's really there.

**Dave Jones:** Now, if we go into the acquire menu again, I can demonstrate that. Let's go into high-res mode, which puts on boxcar averaging. So, it's averaging out some of that high frequency content.

**Dave Jones:** Boom! Look at that. And then, if we go into normal averaging mode, we can do that as well. But that is what happens when it averages out that content.

**Dave Jones:** And then, we can, of course, combine our memory depth, so we can do our boxcar averaging, our memory depth, go right down to 1,000 points. Oh, let's be reasonable.

**Dave Jones:** Let's go down to 10 K, get a decent amount of memory. But look at how thin that line is now, because we've turned on that boxcar averaging over time to filter out effectively that high frequency content.

**Dave Jones:** Almost exactly like the analog scope does, except the analog scope does it using persistence of vision on your phosphor-based screen. And then, of course, you have other modes like your peak detect mode, which can show which captures those peaks and stores them better than your full memory depth.

**Dave Jones:** Even with a record length of a thousand here, we can still get it to display all of that high frequency data cuz it captures it. It's got that peak detect mode in the ADC.

**Dave Jones:** And likewise, envelope mode, of course, you can with infinite persistence, you can capture that and it just fills it up. Fills up the screen like that. That's something you can't get on an analog scope.

**Dave Jones:** But that's a real information there over time you'll never see on an analog. Now, there are two types of digital scopes, and this will make a difference. One is like your Rigol 1000 series scope without what's called an intensity graded display or variable persistence display.

**Dave Jones:** Goes under all sorts of names like that or analog-like display. But something like this Tektronix 3000 series does have that, and that's what this intensity button over here actually does.

**Dave Jones:** If we hit that, it's at 100% at the moment. That's why this waveform looks exactly like it will on a Rigol 1000 series. It's all chunky, you know, and there's there's no sort of a variable intensity in that at all.

**Dave Jones:** But if we drop that down, you'll notice that the real signal going down, going down, going down. Look, the real signal and the real line in there is actually thinner than that, and there's high frequency noise superimposed on top of that, which you which you'll see clearly if you have a an oscilloscope like the Rigol 1000 that doesn't have this intensity graded display, you'll always see all of that high frequency noise.

**Dave Jones:** There is no way for the oscilloscope to tell you the difference between ones that are that appear there all the time and just noise that just appears there periodically.

**Dave Jones:** And that's one of the advantages of the analog oscilloscope, of course, because it shows you that intensity graded display just like these modern modern digital scopes. And that's what these modern digital scopes try to do.

**Dave Jones:** They try to replicate that sort of thing. So, if I show you that waveform with 100% waveform intensity, it operates just like that cheap low-end Rigol one or any of those low-end scopes without this intensity graded display.

**Dave Jones:** Look, if I turn it down, then it operates more like an analog one, and you can see I've got 1 mega sample memory now, so it's showing lots of high frequency detail in that waveform.

**Dave Jones:** But you turn it down, you turn it down, and you start to see that the true line actually gets thinner and thinner. Take a look at that because that high frequency information isn't displayed or captured nearly as often, and that's why the that's why these digital scopes offer this intensity graded display cuz it tries to simulate the analog scope in that respect.

**Dave Jones:** But in my opinion, they're actually better. Digital scope is better than an analog scope because you can actually pick up that information, especially one with these intensity graded displays, really.

**Dave Jones:** Fantastic. Look at that. See? It's almost all gone. And there's the tiny amount the tiny waveform. That's the one that's there all the time, and the rest of that information is just more uncorrelated noise around that.

**Dave Jones:** And you'll really see that here because I've added 30% noise to this signal. So, if we turn it right up to a 100% there we go. Look at that, right?

**Dave Jones:** There's a ton of noise. That is deliberately added on that waveform cuz this scope allows me to do that. You can see if I turn that intensity right down, because that noise is effectively uncorrelated, it goes away like that.

**Dave Jones:** And you can see that the noise is uncorrelated cuz if I go into my acquire mode and choose average down here, bam, it disappears. So, that noise was actually superimposed on that signal.

**Dave Jones:** Now, if I turn on the fast acquisition mode, which this Tektronix 3000 has, I can select different variable intensity display modes. Now, the normal one we had before down here was showing up yellow, but if I set it to temperature mode here, check this out.

**Dave Jones:** We'll see what it does. Change the waveform intensity. Got it set to 100% so it looks just like it would on that uh you know cheap low-end ring gear without any waveform intensity.

**Dave Jones:** But, we turn it down, you'll notice that the waveform changes color. And outside there, the ones on the outside like the little hints of blue and green out in there, they're a they're signal anomalies or noise or whatever it is on your signal that is occurring less frequently than that red line in the middle.

**Dave Jones:** Just like the color temperature gradient in light uh for example. Same sort of thing. So, it's that red part in the middle there, which is your main signal, which is showing up all the time.

**Dave Jones:** That's your baseband signal with all the less frequent noise, or it could be, you know, some other part of your signal. Can It's real information there that's ordinarily hidden on an analog scope, but shows up here as, you know, infrequent blue and green data.

**Dave Jones:** This is really handy, very powerful feature of digital scopes, and especially this one with that color temperature graded display. And it also has an inverted mode here, which actually does exactly as the name says.

**Dave Jones:** It actually inverts the waveform, so the least frequent stuff, the glitchy stuff, all that noise, shows up brighter than your main waveform. So, we go up to 100% or else it's all there, and your main waveform in the middle vanishes.

**Dave Jones:** That's just a neat little different way to view your data on this MDO3000. But, that's the same noisy signal, 30% noise added, and can we see it on our analog scope?

**Dave Jones:** Well, not really. It's very difficult. Look, it looks like a very clean sine wave, but there's actually I've added all that noise to it. You can't see it because it's uncorrelated to the sweep signal, and it's only showing up a very briefly there, but we should be able to capture that with the camera.

**Dave Jones:** Now, I'll attempt to demonstrate that this analog scope can actually display that high-frequency content. Because it's so short, it doesn't light up the phosphors much, and your eyes can't see it.

**Dave Jones:** Well, we can try and attempt to capture that by using a long exposure on our camera here. So, that's what I've got here. I'll put what they used to use back in the old days as camera hoods.

**Dave Jones:** You could buy That's what these ridges around here were for on these analog scopes. You'd buy these hoods, you'd hook your film camera back then up to it, and you could get long exposures.

**Dave Jones:** Well, I'm going to do that. I'm going to whack some uh t-shirt over the top like that, and uh I'll turn out the lights here, try and get as dark as possible, and I'll see if I can capture the noise on a couple of typical signals.

**Dave Jones:** First, a flatline with no input, and then a two be the control, so there shouldn't be much noise on that. And then, a 1 kHz analog signal that will have noise on a digital scope, but you won't see it on the analog unless we do this.

**Dave Jones:** And here's what I shot with the camera at different shutter speeds. Now, the signal was barely visible. That's 1/20th of a second, and you'll notice that it does get a little bit thicker there, and now it sort of pretty much stops.

**Dave Jones:** So, that is the real signal there, bit of blooming, but basically, there was a difference between the signal as originally that I could see with the eye, and then what we recorded with the camera got a little bit thicker.

**Dave Jones:** And here's that noisy signal. As you can see, barely visible at the low shutter speed, and that's what it looked like to my eye. But as you increase that shutter speed, you start seeing all that dim phosphor you couldn't see with your eye, and you can now see the noise superimposed on the waveform.

**Dave Jones:** Brilliant. So, there you go. I hope that's cleared up the myth that digital scopes are noisier than analog scopes, because they're not. They're just better, and they work differently, and hence they're showing up all that high frequency stuff that your analog scope has pretty much been hiding from you all these decades by way of the the phosphor persistence on there, and it having that uncorrelated noise or signal

**Dave Jones:** just not being bright enough. Back in the old days, when we didn't have digital scopes, you had to turn the brightness right up on this sucker to sort of, you know, see all that I think there's something hidden in there.

**Dave Jones:** Is it? Oh, I don't know. Sometimes you might have to get your camera and hook it up to actually saw it as I demonstrated there. It wasn't a totally thorough demonstration for the camera, but it did at least show the difference that when I've got it low intensity like that, there is actually more information there that my eyes just aren't picking up because they aren't displayed as frequently.

**Dave Jones:** But the exact same signal on a digital scope, especially one that doesn't have variable persistence like this Rigol or this ancient Tektronix one, it shows up and that's why the waveform looks thick or noisy, but it's not.

**Dave Jones:** Yeah, there might be subtle differences between analog front ends, but it's not like this modern Tektronix 3000 series scope just released is going to have a noisier analog front end than this ancient analog Tektronix scope.

**Dave Jones:** No, it's not the case. And there's a little bit involved in terms of the 8-bit digital sampling and things like that, but in the end what it comes down to is, as I said, the memory depth of the scope.

**Dave Jones:** The more memory depth, the more you're going to pick up all that high frequency content. The greater your bandwidth, the more noise you're going to see and that's inherent in analog scopes as well, not just digital.

**Dave Jones:** And of course, your variable intensity displays. If you've got something like the old Rigol or the old Tektronix here that doesn't have variable intensity, well, you just got to capture everything.

**Dave Jones:** And sometimes, as I showed in the previous video, that can be a good thing. So, there you go. Don't rag on digital scopes. They're not that bad. They can actually be better.

**Dave Jones:** Sorry for all you analog graybeards out there. Catch you next time.
