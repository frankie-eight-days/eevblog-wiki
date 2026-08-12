---
video_id: Fk9T1FDNAk4
title: New Agilent 3000X Oscilloscope Firmware - EEVblog #209
url: https://www.youtube.com/watch?v=Fk9T1FDNAk4
source: youtube-asr
timestamps: {"0": 0, "1": 11, "2": 21, "3": 32, "4": 44, "5": 58, "6": 71, "7": 87, "8": 98, "9": 113, "10": 129, "11": 142, "12": 152, "13": 166, "14": 176, "15": 190, "16": 207, "17": 222, "18": 234, "19": 245, "20": 261, "21": 274, "22": 286, "23": 299, "24": 317, "25": 327, "26": 342, "27": 353, "28": 368, "29": 378, "30": 390, "31": 409, "32": 419, "33": 434, "34": 451, "35": 461, "36": 481, "37": 502, "38": 512, "39": 522, "40": 531, "41": 546, "42": 563, "43": 579, "44": 589, "45": 614, "46": 633, "47": 648, "48": 672, "49": 692, "50": 701, "51": 722, "52": 752, "53": 768, "54": 782, "55": 796, "56": 810, "57": 825, "58": 839, "59": 855, "60": 868, "61": 884, "62": 900, "63": 917, "64": 929, "65": 942, "66": 954, "67": 969, "68": 977, "69": 996, "70": 1010, "71": 1020, "72": 1037, "73": 1047, "74": 1056, "75": 1073, "76": 1085, "77": 1103, "78": 1119}
---

**Dave Jones:** Hi, you know how I reviewed the new Agilent 3000 series scopes about 7 months ago when they first came out? Well, it turns out as of today, October 18th, Agilent have just upgraded them.

**Dave Jones:** Not the physical scope, but the firmware. They've got a new release uh firmware code named, yes, it's got a code name, code name Dingo, and version 2.0 firmware for the 3000.

**Dave Jones:** I thought we'd take a look at it. It's got some cool new features. One of the killer new features for this new firmware is something that I complained about when I first originally reviewed the scope.

**Dave Jones:** And I think I'm going to take credit for this one because back when I reviewed it, I said, "Well, the function generator in there is great. Excellent idea to stick a function generator in a scope.

**Dave Jones:** Allows you to do lots of cool stuff." But it was clear that they were actually using an arbitrary uh waveform generator internally to actually generate uh the waveforms that it could do.

**Dave Jones:** And I said at the time, "Why don't Why doesn't it include arbitrary capability? Why can't you capture the waveforms with the analog input and then store edit them and store them and then output them on the function generator?"

**Dave Jones:** And well, at the time, Agilent said, "Well, you know, they didn't want it They It was a bit competitive internally, you know, their function generator group would be all up in arms cuz they'd lose sales of their function generator, etc., etc." And well, I don't know.

**Dave Jones:** I thought it was a bit lame that it didn't have uh arbitrary capability, but I understood it from an internal political point of view. But as it turns out, they've decided to offer free arbitrary capability on the 3000.

**Dave Jones:** And I find that rather surprising now. Um I expected it uh to come up eventually if uh like a competitor came out and they had a function generator in their scope and Agilent had to compete, they'd put it in there.

**Dave Jones:** But I thought No, other than that, they wouldn't do it. But turns out they have. So, this sucker now has arbitrary waveform capability. And if you've got one of these scopes with the waveform generator option, you can download the firmware, bingo, you'll have it, too.

**Dave Jones:** Beauty. All right, I've updated the firmware, which is pretty painless process. You put it on a USB stick, and I should have the new version 2.0 firmware installed. So, let's check it out.

**Dave Jones:** It's booting, booting, booting. Same splash screen, but I rather like that splash screen. So, I'm glad they kept it, actually. And if we go into the about screen here, there we go, version 2.00.

**Dave Jones:** Warning, unreleased software, only cuz I got it before most other people. Okay, I don't have any manuals for how any of this works. So, we're going to have to suck it and see, but as it turns out, that's one of the best ways to see if features are user-friendly.

**Dave Jones:** So, let's try and capture a waveform input and then save it and generate it through the arbitrary function capability. I've got my probe here set up for single shot capture.

**Dave Jones:** I'm just going to bang it on the bench here, and that will generate a shock impulse response. Here we go. Well, it will. There we go, eventually. So, if we hit that there, it's Let's get that on the screen.

**Dave Jones:** Let's do it again. Bang, there we go. That looks like a nice waveform. Let's try and save that into our arb generator. Okay, I'm going to assume that it's going to be sensibly I'd put it under the save recall file thing under save here format.

**Dave Jones:** Bingo. Look at that, arbitrary waveform data. I I don't think we had that before, and power harmonics data. That's for the new power module, possibly, that's in there. But, that's the new arbitrary waveform data.

**Dave Jones:** So, let's select that, and location /arb. It's already put that in there. It looks like Well, I guess you You store as many as you want, but let's Well, let's choose one of those.

**Dave Jones:** Let's store it in arb zero. Press to save. And it's done. It's saved. All right, let's go into our wave generator here and our waveform. Hey, bingo. There we go.

**Dave Jones:** We've now got an arbitrary capability there as well as if you didn't know some of the new There's a couple of extra wave shapes added to the previous new firmware exponential exponential rise and fall cardiac Gaussian pulse stuff.

**Dave Jones:** So, we go up here to arbitrary and it looks like we've got edit waveform. Bingo. That's a new option. Okay, let's go into settings here and it looks like there's a noise capability here.

**Dave Jones:** Check it out. It's got arbitrary plus noise. So, it looks like you can add from anywhere to from no noise just arbitrary up to What is it? What? 100% noise.

**Dave Jones:** There we go. That's a handy feature. I rather like that, but I haven't figured out yet how to gen actually load that waveform in. There's the default wave gen, but we don't want that.

**Dave Jones:** We want edit waveform. And source is There we go. Channel one. Okay. Our source is coming from channel one. Store source to arb. And Bingo. There it is. So, we didn't even I don't think we even had to save that to the file.

**Dave Jones:** I I think that was totally optional. Um so, let's actually try that again. Actually, let's go back to our single shot capture here. Get out of our edit menu.

**Dave Jones:** Let's capture that again. There we go. And let's see if we can edit waveform and source is one and store source to arb. Yep, it changed it. There you go.

**Dave Jones:** So, you don't have to save it to file. You can just uh capture it on any of the channels and store it straight in. I like it. Or you can take it from the math as well or any of the reference waveforms.

**Dave Jones:** Beautiful. Okay, now what it looks like it's done here with the waveform is it's automatically looks like it's automatically scaled cuz you saw that waveform wasn't uh full scale on the screen, but it has actually scaled it full scale inside there.

**Dave Jones:** So, that's that is really quite nice. I like that. So, I presume that you get the full uh what is it? 10 or uh 12-bits uh capability? I'd have to check.

**Dave Jones:** Don't remember off the top of my head, but you then you get the full capability of uh that your full you get the full resolution of the uh DAC in there based on your current waveform.

**Dave Jones:** I like it. That's neat. And it looks like they've got this window here. This window obviously uh that uh orange uh window there obviously correlates to this zoomed window down here and they've automatically scaled these figures based on those maximum positive and negative values.

**Dave Jones:** That's rather neat. And they've got an interpolate function there just to uh smooth it out so it's uh not as jagged. And let's go into edit existing, shall we?

**Dave Jones:** Point number one. You can insert points and you can remove points. Okay, so it's obvious that that you set your voltage here. You set you set the voltage you want like that.

**Dave Jones:** Oh, yeah, I can see that point. Can see that point going up there. So, if I go into here and point number There There you go. I'm jumping along each data point, each sample, which will be output to the DAC.

**Dave Jones:** Or actually Oh, sorry. Point number 161. No, you have to go into find if you want to do each individual little bit, but then you can set the voltage and bingo.

**Dave Jones:** Actually, there you go. If you just hit insert point, then you just keep inserting that voltage there. So, if I put the voltage adjust here, fine, and I just hit keep hitting insert point, I can just sort of manually you can you probably can't see it.

**Dave Jones:** Let's take that to up. Hang on. Let's take that to coarse voltage, and then you can insert the point, and you can see me manually drawing that waveform. So, I can draw in effectively draw in a uh like a rough sort of sine or triangle wave or any wave shape I like.

**Dave Jones:** Oh, there's a bit of lag there though. You see how it's still going? It's capturing It's uh actually capturing uh actually trying to catch up to where I had it.

**Dave Jones:** I don't rather like that. I'd rather that be uh instant, but oh, it's stopped for some reason. What's going on? Why is it stopped? Selection is not available anymore.

**Dave Jones:** Oops. Something's gone wrong. Anyway, I can remove points, and I don't know. It just seems to work quite well. It's fairly intuitive, and it's transparent. You can see That's nice.

**Dave Jones:** It gets rid of the menu so that you can see your waveform behind it. Excellent. All right. Well, let's go back. I don't want that extra little uh jagged stuff I edited over there.

**Dave Jones:** And whoops, store to arb. Yeah, okay. Yes, we're back. So, if I go back into my wave gen here, it looks like it's automatically selected the amplitude for me, 635 mV peak to peak, because the peak to peak that it was doing here was 640 mV.

**Dave Jones:** That's my waveform that I uh captured, but it's set the arb gen to that. It set the frequency to 200 Hz. Okay. So, what I've done now is I've uh stored that uh signal that we captured as one of the uh reference waveforms over here.

**Dave Jones:** So, we can keep that permanently on the screen. Now, let's have a look at what happens when we get the arb gen to generate this signal. And bingo, there it is.

**Dave Jones:** It's repetitive. It's uh generated that signal as a repetitive signal. And that's at the 200-Hz repetition frequency we set in here. So, we can change that, obviously. There's our arb gen, and we can change the repetition rate of that particular waveform, that arbitrary waveform, which we generated.

**Dave Jones:** Nice. Works exactly as you'd expect. But, of course, if you change that repetition frequency there, then you'll find that the um frequency of the waveform itself, not just the repetition rate, uh changes.

**Dave Jones:** So, just be careful when you do that sort of thing. Remember, there's our reference waveform. So, as you can see, it's actually uh changing frequency based on the uh based on the record uh the sample record length inside the arbitrary waveform generator.

**Dave Jones:** And, of course, it's not magic. It can't go up to any arbitrarily high frequency, no pun intended. So, um we're adjusting our our repetition frequency down here. And once it gets to 1 MHz, bingo, you'll see the amplitude start to drop on that waveform until, well, there's not much left.

**Dave Jones:** And let's try that noise function and see how it works. Setting add noise, and bingo, look at that. I I like that. That's nice. Now, there's one thing I haven't been able to find in this arb generator is the ability to generate a single shot waveform.

**Dave Jones:** If I just want to generate that bang once and then stop, I don't know how to do it. I It'd be silly if you can't do it, but I'm buggered if I can find it.

**Dave Jones:** Maybe that's one of the limitations with uh a built-in arb gen like this that they're just Well, now effectively uh giving away, although you do have to pay for the wave gen option, but maybe they don't want to add uh stuff like that to actually compete with the um you know, a full-on proper uh separate bench function generator.

**Dave Jones:** Because one of the things this um it still does not have is external modulation capability. And I'm just wondering is it possible to um uh use one of the spare analog channels here to feed in your modulation signal into that and then modulate the your arbitrary or some other uh waveform some one of the other uh predetermined uh waveforms, be it sine or whatever, um actually modulate

**Dave Jones:** that with it. One of the analog inputs. I wonder if the hardware is actually capable of that. If it was, that'd be really cool. Now, another thing they've added is uh an optional module for the if you've got the advanced math uh option module, then they've added all these other cool stuff.

**Dave Jones:** All these uh you've got uh filters, you've got squares, square root, absolute logs, natural logs, exponentials, and low pass and high pass filter, measurement trends, and uh all sorts of stuff.

**Dave Jones:** I like it. But, of course, if you don't have that module, you don't get it. So, you got to pay for it. Okay, let's just have a quick play around with that low pass filter there and we can adjust the bandwidth here and uh the purple waveform there is our math uh one.

**Dave Jones:** This is still our live input, obviously. See, it's uh live if you disconnect it, it totally goes away. So, where our math is being updated in real time there, and uh let's adjust our bandwidth here.

**Dave Jones:** For uh let's lower that down, and we should see the amplitude uh drop. There we go. Bingo, cuz we've put in that uh low-pass filter. So, that's a neat tool.

**Dave Jones:** It just allows you to uh experiment in uh real time inside your scope with um your actual uh waveform. So, you can see it actually smooth out um all of those high-frequency high-frequency components.

**Dave Jones:** And if I go into the analyze menu here, then I've got the new uh video um option uh installed as well. You've got to uh pay more for that, of course, but it can do uh all of HD TV stuff and all that sort of thing.

**Dave Jones:** Beautiful. And here's a new module which they've got in the 2.0 firmware which you can buy, which is the power application one. I'm very excited. I've got it, and uh let's switch it on and uh look at some of the stuff we can do, cuz it's very cool.

**Dave Jones:** Some of the stuff we can analyze here for uh you know, DC-to-DC converters, power applications, current harmonics, efficiency, inrush current, modulation, power quality, switching loss, transient response, turn-on turn-off time, output ripple, uh PSRR, slew rate.

**Dave Jones:** It's fantastic. Everything you need for designing power supply circuitry. And the good thing about this, okay, is we if you actually uh go in there, let's say we want to do um uh let's say efficiency, okay?

**Dave Jones:** Let's go into signals. Look at this. It uh tells you how to actually uh set up your voltage probe, your current probe, voltage and current probe. And the good thing about having a four-channel scope is that you can have uh measure input and output power at the same time.

**Dave Jones:** You can have voltage and current on uh one and two, and uh the output uh voltage and current on three and four. And it gives you a little connection diagram right there, and it shows you how to do that.

**Dave Jones:** You've got the voltage you you've got your differential uh voltage probe there. Usually, you're going to use differential uh probes for something like this. Um unless you're working on a totally common uh ground system or something.

**Dave Jones:** And your current probe on channel two, your other differential probe measuring your input, and it shows you how to set it up. It's just nice that you've actually got um output ripple um actually written here, and you've got output ripple over here.

**Dave Jones:** And that's good when you do screen captures and you put them in test reports and stuff like that. And if you haven't actually um analyzed uh power supplies before or you're a bit rusty, you know, you haven't done it for 5 years or something, this uh it's just nice being able to go in here.

**Dave Jones:** Okay, I need to measure the switching loss of this thing. And you go in there, and it tells you how to set it all up to measure the switching loss.

**Dave Jones:** I love it. One of the other things they've actually uh included with this update, even though they haven't actually done anything, but they've actually uh specified it. There is now a 2-year calibration interval standard with these uh scopes, and that applies to all existing scopes manufactured as well as new ones.

**Dave Jones:** Because Agilent, well, they actually have done some work on it, I guess. They've actually uh analyzed it and found that these scopes uh should be stable, and they're um confident that um you can the uh the recommended factory calibration interval is now 2 years.

**Dave Jones:** And that can be a big deal um for people who have to get these sort of things calibrated and who don't have their own internal standards, but they follow the manufacturer's recommended interval.

**Dave Jones:** So, they've upped it from 12 months to 2 years. Beauty. Now, the specs for this built-in arb gen aren't exactly going to set the world on fire. We're only talking uh 10 bits vertical resolution, 100 megasamples, and uh 8K sample memory.

**Dave Jones:** But hey, consider this built-in a scope, it's it's not bad at all. It's certainly quite useful. So, I don't think Agilent's function generator group are, you know, really shaking in their boots at this stage.

**Dave Jones:** You know, they might lose the occasional sale, but really, if you want a, you know, a decent high-performance arb generator, you've got to get a dedicated instrument. So, there you have it.

**Dave Jones:** It's a rather neat little implementation of an internal arb generator, and I don't mind it at all. Works quite well. It's fairly intuitive. Um single shot capability would be nice, but it's not It's not a full-featured arb generator.

**Dave Jones:** You can't do, you know, a function generator. It's just They've just added some basic arb capability, and it's especially considering it's a free download, it's very worthwhile getting if you've already paid for the function generator.

**Dave Jones:** Definitely get it. Now, it does have the capability to interface to some PC software as well for editing and downloading, uploading, downloading the waveforms. I'm I'm assuming that is the Agilent BenchLink software, but I didn't get any pre-release information on that.

**Dave Jones:** Normally, you've got to pay extra for the BenchLink software, so I'm not sure, but I'm sure details will come to light today. So, there you go. If you've got an Agilent 3000 series, and you've probably been maybe deciding if you want to buy the function generator or not, well, now you've got arb capability.

**Dave Jones:** And if you've already got it, download it quick smart. Catch you next time.
