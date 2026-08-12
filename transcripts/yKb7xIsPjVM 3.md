---
video_id: yKb7xIsPjVM
title: EEVblog 1379 - What's all this NPLC Stuff Anyhow?
url: https://www.youtube.com/watch?v=yKb7xIsPjVM
source: youtube-asr
timestamps: {"0": 0, "1": 9, "2": 28, "3": 38, "4": 59, "5": 85, "6": 98, "7": 114, "8": 123, "9": 136, "10": 153, "11": 163, "12": 176, "13": 187, "14": 201, "15": 212, "16": 224, "17": 237, "18": 257, "19": 270, "20": 277, "21": 290, "22": 308, "23": 321, "24": 333, "25": 343, "26": 361, "27": 376, "28": 387, "29": 400, "30": 414, "31": 422, "32": 438, "33": 454, "34": 468, "35": 479, "36": 491, "37": 506, "38": 515, "39": 542, "40": 551, "41": 564, "42": 578, "43": 590, "44": 603, "45": 621, "46": 630, "47": 640, "48": 652, "49": 664, "50": 671, "51": 684, "52": 698, "53": 721, "54": 730, "55": 747, "56": 756, "57": 765, "58": 776, "59": 802, "60": 812, "61": 824, "62": 837, "63": 852, "64": 869, "65": 882, "66": 899, "67": 910, "68": 930, "69": 940, "70": 966, "71": 975, "72": 986, "73": 1007, "74": 1021, "75": 1037, "76": 1052, "77": 1063, "78": 1074}
---

**Dave Jones:** Hi, this is your humble multimeter and you used to it just on DC volts here reading zero volts when you're just got your probes sitting there on the bench.

**Dave Jones:** It's reading nothing and you might be familiar of course. You switch it over to millivolts, you know, it might pick up a little bit of noise there and if you put your hands on there, you know, you might get a few like tens or even hundreds of millivolts noise, but generally it's around about, you know, zero volts, something like that, especially if you put it on the voltage

**Dave Jones:** range like this. Well, what happens if you take the same leads and you plug them into like a high-end six and a half digit or seven and a half digit multimeter like this?

**Dave Jones:** Well, uh Bueller? Bueller? That's um one and a half volts. What's going on there? Something's a bit weird. Why are we getting like a volt and a half? Well, let's go over to the Keysight meter up here and let's plug in the exact same leads.

**Dave Jones:** Oh, we're still getting a volt. I can hear you saying, "Dave, I know what's going on here. Bench meters are famous for having like a high input impedance on like the millivolt range and even up into uh several over one or several of the voltage ranges." Well, if we go into there, you'll see that no, we're 10 megaohms input impedance and if we go auto, um input said, "Yeah, it goes a bit higher

**Dave Jones:** and stuff like that and it might charge up because you've effectively got uh infinite input impedance, but um and if we like manually range it like this, look, on the one volt range, we're getting overload, overload, overload.

**Dave Jones:** What? What's going on? And let's try an older school uh bench meter, in this case a um old Philips uh six and a half digit jobby and if you listen very carefully, you might be able to hear something.

**Dave Jones:** You You hear a relay in there Relays switching because it's just going crazy. It doesn't know whether it's volts, millivolts, or whatever. You can see the M flash up there very briefly.

**Dave Jones:** It's just going berserk. And this is actually a very real stuff. Look, if we go into the trend chart over here, we can see Look at that. I mean, that's we can auto scale that.

**Dave Jones:** Look at that. I mean, there's real stuff on there at like almost 2 volts plus minus 2 volts peak to peak. Thomas, why? As I said, we've got 10 megaohms input impedance, exactly the same as your regular multimeter.

**Dave Jones:** What's going on? Why does this show zero and these higher-end meters show like a couple of volts? And we can even choose to like like slowly data log this as well.

**Dave Jones:** Look at this. I'm I'm doing like one sample per second. One It's like minus 1 volt. It's all over the place. Look. But you might see it is actually counting down.

**Dave Jones:** That's interesting. And if we do a trend chart of this slow one's once per second data logging, hmm. There you go. I left it for a bit, and this is what we're getting.

**Dave Jones:** It's kind of sort of sinusoidal, not really. But something's going on. Look at that. Oh, there's a bit of a bit of wiggle wiggle wiggle yeah going on down the bottom there, and it'll probably go back up shortly.

**Dave Jones:** You watch. Come on. Come on. I'm betting it will. You bet you. There you go. Go, you little beauty. Up it goes. All the way. You can do it.

**Dave Jones:** Oh, had a little jaggy there. But you can see this is like real interesting stuff. This is real logged data, once again, with the probe sitting in exactly the same position we had for the other meters.

**Dave Jones:** It's interesting. It's picking up something. But of Of everyone knows what it's picking up. He's just picking up mains and crap, right? And sure enough, if we short the probes, it is zero.

**Dave Jones:** And we can go back to our uh number display there, and zero volts. And we take our hand off that, and there we go. It's going up. .3 .5 .7 Once again, this is 10 megaohms input impedance, exactly the same as our 10 megaohm input impedance multimeter here.

**Dave Jones:** So, why the difference? Well, I'm glad you asked. It has to do with the number of power line cycles or the integration time of the multimeter. Yeah, typical handheld multimeters are like these.

**Dave Jones:** These are relatively uh slow. You used to, you know, like a really fast one will get five or even some on the market might do like seven times a second or something like that.

**Dave Jones:** They're really quite slow. But, these actually have built-in 50 {slash} uh 60 hertz. Sometimes it's selectable, sometimes it's not. Um filters in them. Uh so, they're actually filtering out out the power line frequencies.

**Dave Jones:** Because in any sort of uh lab or environment uh where you're measuring stuff, uh 50 hertz is going to be or 60 hertz for you Yanks um is going to be like one of the predominant um interference sources in a typical uh environment, office, or lab environment.

**Dave Jones:** So, your handheld multimeters are being very nice to you, and they actually have that uh integration time set so that it takes samples long enough that it actually effectively filters out 50 hertz or 60 hertz uh interference frequencies.

**Dave Jones:** But, your higher-end multimeters like this, uh they may or may not do it by default. You've actually got to go into the menu and check out the number of power line cycles.

**Dave Jones:** So, if we go into DC volts here, you'll see I'm at 0.2 PLC or power line cycles. Right, so I'll just stop my data logging here, and we'll go back to a continuous uh display, right?

**Dave Jones:** And there we go. We're in volts, and number power line cycles. This actually determines the accuracy of your meter as well. So, NPLC is the acronym for it. And you can also do time as well in milliseconds.

**Dave Jones:** They're effectively like essentially the same thing. The number of power line cycles means it'll do an integration measurement over 1 50 or 60 hertz power line cycle. So, if NPLC is set to 1, and then you can do that in milliseconds as well.

**Dave Jones:** I mean, you know, 50 hertz would be 20 milliseconds, of course. So, you can see if I've actually got that value very low, I don't get many significant digits there, and I also get quite a lot of noise here.

**Dave Jones:** And if I go into 0.02 power line cycles, 0.06, we're still getting you know, like volts of noise, right? And 0.2, we're still getting quite a lot of noise.

**Dave Jones:** But watch what happens when I go to one power line cycle. Tada! It's magically vanished because it's doing at least one full integration of the 50 or 60 hertz power line cycle.

**Dave Jones:** So, you're reducing the noise. And you can see, of course, that we've got more significant digits now. So, if we go back, of course, we still have the same number of significant digits there.

**Dave Jones:** It hasn't changed, but because the integration time is not long enough to do any effectively like averaging, so to speak, even though it's integration. I won't go into the differences, but but anyway, if we go to there, and then if we go to 10 power line cycles, watch.

**Dave Jones:** Tada! We get an extra digit of resolution here, and of course, we're getting our zero volts there. Once again, if I touch those leads, right, yeah, I can get, you know, tens of millivolts, basically, equivalent to what we get on our handheld multimeter here.

**Dave Jones:** And I can show you how the smoothing, you know, average mathematical averaging doesn't do the same thing. It's actually to do with the measurement integration, not the post measurement smoothing or something like that.

**Dave Jones:** So, let's go down to say 0.2 power line cycles here, and then we'll go into math up here, and where are we? We got smoothing filter. There we go.

**Dave Jones:** If we turn the smoothing filter on, ah, it doesn't really do anything. So, it's doing and the response also, you know, 10 readings, 50 readings of smoothing, it doesn't help.

**Dave Jones:** So, doing post sample averaging and smoothing does not help the situation. It's all to do with the how the ADC works, and these are integrating ADCs. You might have heard of dual slope integration.

**Dave Jones:** I've probably done a video on dual slope or multi slope integration. The Keysight have their multi slope integration, and there's dual slope, and there's single slope, and all sorts of things.

**Dave Jones:** But, that's basically how your high-end multimeters, well, even your handheld multimeters as well. Like, even your low-end ones, they use like dual slope integration. So, it's, if you don't have your integration time of your measurement set to actually take into account and average out in the measurement the 50 or 60 hertz noise pickup, then yeah, you're going to come a cropper like this, and you're going to

**Dave Jones:** measure volts, and you can get the meter to do weird auto ranging stuff. We saw on that Philips one. And the Keithley one down here, exactly the same thing.

**Dave Jones:** Like, I've got the smooth That smoothing filter is actually on, right? The smoothing filter doesn't do anything. It doesn't help your cause at all. And check it out. It's just going auto ranging.

**Dave Jones:** And then, oh, look, it's even going like like 10 volts, 1 volt, right? It it just doesn't know what to do. It's just absolutely nuts. And you turn on the smoothing filter, and well, it's still it's a little bit slower, of course, but the those high voltages are still there.

**Dave Jones:** It's not getting rid of them. And once again, we're still 10 megaohms input impedance. But you'll see that we're 0.1 power line cycles. So, I'll turn off the filter here, and we'll change that to one power line cycle.

**Dave Jones:** Bingo, it's gone away cuz we're doing at least one integration over one full 50 or 60 hertz power line cycle. Nice. And as I said, uh meters will typically have like a setup in there for 50 or 60 hertz.

**Dave Jones:** And just to show you the actual waveform that we are picking up here, what I've got is I've replaced the multimeter leads with just uh some banana plug leads flapping around in the breeze there, and I've got a uh 10:1 uh probe directly coax connected across there.

**Dave Jones:** So, we've effectively got a 5 megaohm uh input impedance now uh total, but we're going to be, you know, that's still quite high enough to pick up uh the noise and stuff.

**Dave Jones:** So, if we go in here and we have a look at our trend chart, you can see that we're getting like plus minus a volt there. Does that correlate with the oscilloscope?

**Dave Jones:** Yep, it does. Check it out. There you go. Plus minus a volt there. So, yeah, no worries. And I was getting before, but I'm not now. Unfortunately, I was getting like large um spikes on there.

**Dave Jones:** So, something was switching in here. I don't know what it's gone now, of course it is. As soon as I hit record, white coat syndrome. And of course, if I touch those leads there, you can see yeah, it just changes.

**Dave Jones:** If you twist them, it's going to change. If you, you know, it depends where you got this. It'll change from lab to lab, whether or not you're holding them.

**Dave Jones:** It'll change from one part of your lab to another. It'll like just vary all the time because you've got such a large input impedance. You can see that change that I just played around with there on the uh trend chart there, and we can probably do that again.

**Dave Jones:** Let me get the leads, and I'll actually twist them. Okay, so what I've gone and done now is actually uh twisted the leads like that and you can see that that is significantly reduced the pick up there.

**Dave Jones:** But of course it all has to do with the number of power line cycles. So, when you're uh playing around with your multimeter, especially these bench ones, um that can do a really fast integration uh times and stuff like that, you need to know about your number of power line cycles and how not only how it can influence uh the display resolution um but also can influence

**Dave Jones:** your noise pick up. There it is, just magically vanished. And if you want the most accurate readings, like you're going to put it on like a 100 power line uh cycles.

**Dave Jones:** And to give you an example of this, I'm actually feeding in 5 V DC superimposed with a 1 V peak-to-peak 50 Hz uh sine wave and you can see that it's bang on 5 V because we've got the number of power line cycles equal to one.

**Dave Jones:** And if we go to point two, you know, there we go. jumping around like a jack rabbit. Point 02, point 06, there you go. It's jumping around like crazy.

**Dave Jones:** But if we go to the number of power line cycles at least equal to one, it magically vanishes. And we can see that perfectly on the uh trend chart here.

**Dave Jones:** You'll notice it's precisely uh plus minus point five of a volt there. One volt peak-to-peak, that's exactly what we're uh seeing. And if we actually extracted that data and looked in, hopefully we can see a sine wave.

**Dave Jones:** But if we change our number of power line cycles, instantly go up to one, bingo, it's stopped. We're actually getting a flat line there now. And we can go back to point two power line cycles and you can see at point two, it's getting a bit We probably won't If we actually looked at the data and zoomed in, we probably wouldn't see a perfect uh sine wave there, but the lower that

**Dave Jones:** we go, the more solid you see that's going to get. Right, so what I've done is I've pulled the uh the data from the multimeter, put it in your spreadsheet here, and we can graph it.

**Dave Jones:** And I'm changing the modes in the power line cycles, and you can see like four distinct modes here. Now, this flat one over here, this is 5 V, where of course feeding in 5 V plus minus half a volt 50 Hz uh signal on there.

**Dave Jones:** And we're completely flatlining here, and you may have guessed this is one power line cycle. So, that's 20 ms cycle time or aperture time as it's called, or sampling time.

**Dave Jones:** They're all basically the same thing. It's just different uh terminology. Some manufacturers might use a different uh term, but basically an aperture time there of 20 ms. So, that allows us to get at 50 Hz signal.

**Dave Jones:** This would be different for 60, but at 50 Hz we get one complete mains cycle, so it averages out, and that's why we get a flat line. And it's not averaging out mathematically later as we just uh store, it's actually doing it in the integration or sampling time of the analog-to-digital converter.

**Dave Jones:** The If if it takes this much time to uh sample it, in that time the 50 Hz noise has gone exactly one complete cycle, and it's just averaged itself out, and we get 5 V.

**Dave Jones:** Magic. But at this point here, I then switch to 0.2 power line cycles, or four and now which is 4 ms aperture or uh sample time. And as you can see, we start to see I you know, I up to like we start to see the peak there that 1 V peak-to-peak signal there.

**Dave Jones:** But you might have noticed this, it's kind of like modulated. You might have seen this before in your oscilloscope. This looks like classic aliasing. This is all to do with your Nyquist stuff, right?

**Dave Jones:** Where you need at least twice the sample rate, otherwise you get aliasing. So, we're I clearly getting sampling artifacts here of our 50 Hz um signal, and it's it's not good enough because we're only sampling at with an aperture time of 4 milliseconds or 0.2 power line cycles.

**Dave Jones:** Now, at this point here I switched over to 0.06 power line cycles or 1.2 milliseconds um aperture time and as you can see we really start to get a pretty decent signal.

**Dave Jones:** It's still not absolutely perfect because our sample rate's not very high and at this point over here I switched to 0.02 power line cycles or 0.4 milliseconds uh aperture time and as you can see we get pretty much a perfect sine wave there and you can see how it's effectively changed what looks like changing frequencies there at at each point because we're taking more samples each time we set or each time we change

**Dave Jones:** that number of power line cycles. It's changing our sample rate effectively. So, there you go. We get sampling artifacts just like you would on an oscilloscope or a data logger or anything.

**Dave Jones:** A bench multimeter is no different. It's just a sampling system. That's it. It's not rocket science. Just how these things work. And of course it all has to do with the input impedance.

**Dave Jones:** That 10 megaohms is actually quite high and it it picks it all up and if you put go whack a 1K resistor in parallel with it it's going to knock it on the head and and if you go and measure like a low impedance voltage source like a battery cuz it's got like milliohms output well a source impedance and you measure that, that's why we can get just the probes

**Dave Jones:** there we can get like a volt of noise. Yet when we measure a battery like that, we will get 1.30254 and we'll only get the noise will only be a couple of least significant digits like that.

**Dave Jones:** So, that's all to do with the impedance of your measurement source. In this case, the impedance of our measurement source is 10 meg and it's just picking and we've got these big antenna leads on here picking up the 50 hertz which is like plus minus a volt.

**Dave Jones:** So, there you go. Very interesting stuff. Number of power line cycles that has to do with the integration time, which is different to any sort of smoothing or averaging mode which the meter might do after that because you're doing that after the measurement and not before.

**Dave Jones:** So, it's all to do with the measurement time of the analog to digital converter. And of course, it's going to slow down your measurement the more number of power line cycles you have, but you get increased accuracy and rejection of 50 60 hertz noise.

**Dave Jones:** So, hope you found that interesting. If you did, please give it a big thumbs up. As always, discuss it down below and check out my alternative platforms like Odyssey.

**Dave Jones:** I think I'm close to 60,000 subscribers on Odyssey now. Winner, winner, chicken dinner. Catch you next time.
