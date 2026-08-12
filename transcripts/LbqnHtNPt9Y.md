---
video_id: LbqnHtNPt9Y
title: Siglent Oscilloscope - Function Gen USB Connection Test
url: https://www.youtube.com/watch?v=LbqnHtNPt9Y
source: youtube-asr
timestamps: {"0": 1, "1": 9, "2": 26, "3": 44, "4": 60, "5": 77, "6": 96, "7": 114, "8": 121, "9": 141, "10": 151, "11": 168, "12": 185, "13": 194, "14": 207, "15": 218, "16": 227, "17": 238, "18": 255, "19": 266, "20": 273, "21": 284, "22": 294, "23": 306, "24": 323, "25": 336, "26": 354, "27": 362, "28": 375, "29": 389, "30": 404, "31": 421, "32": 430, "33": 440, "34": 451, "35": 463}
---

**Dave Jones:** Hi, I just thought I'd show you something cool with uh Siglent uh gear here. You can probably do it with other uh manufacturers as well, but I think this is really cool.

**Dave Jones:** Now, it I didn't know that this was possible, but it only reoccurred to me after my uh Rohde & Schwarz MXO 4, the actually the uh frequency response analyzer, the FRA in that um actually the license for that expired, and I tried to use it, and of course it had expired.

**Dave Jones:** And also the arbitrary waveform generator license it it expired cuz I only had a demo. And I was in the middle of shooting a video, and I thought, "Oh, I'm going to need a different way to do this, but I needed a 100 MHz bandwidth frequency response analyzer." And I didn't I thought I didn't have one.

**Dave Jones:** Then it occurred to me, "Duh, Dave, um the Siglent gear can actually uh join uh an external uh function generator um to their oscilloscope." So, I thought I'd never tried it before, um but it just occurred to me that this is actually uh doable.

**Dave Jones:** So, what I've got is uh my um Siglent SDG gen, which is a 120 MHz bandwidth function generator. So, uh yeah, it's more than the 100 MHz that I needed, and uh I've got the um uh the Siglent SDS 2354X.

**Dave Jones:** It's a 350 MHz scope. It's got frequency response analyzer built in, as you can see. And also has an arbitrary waveform generator built in uh with the um output on the uh back there, but it's only uh 20 I think 20 or 25 MHz bandwidth uh function generator, as most scopes are.

**Dave Jones:** The Rohde & Schwarz is the only oscilloscope I've got that has a 100 MHz bandwidth function gen built in. So, um yeah, it's limiting. If you use the internal frequency response analyzer like this, you can and the internal function gen, you can only go up to 20 or 25 MHz or whatever it is.

**Dave Jones:** But, what I've done is hooked uh the USB onto this over to the Siglent function gen. You can either use Ethernet or uh USB, but I'll go in here.

**Dave Jones:** So, I'm in the uh frequency response um analyzer at the uh moment, and we can actually go into uh configuration up here, and you can see that the interface you can actually set that um to be uh the internal, which is the internal function gen, um or the uh USB, which I've got, or LAN as well.

**Dave Jones:** So, you connect it to USB, and I can press test, and it's successfully connected. Bingo. The scope can now control the function generator to do the external frequency uh sweeping.

**Dave Jones:** And so, what I've got is a little uh just a little 15 MHz um uh filter down here uh low-pass uh filter. So, the input's on uh channel one here, and the output's just go into channel two, and we measure the uh we can measure the frequency response of that.

**Dave Jones:** So, uh yeah. This actually works straight out of the box, even though I think like this is many years old. I can't remember how old this thing is. I don't think I've upgraded the firmware in a long uh time, but I thought, you know, I might have to upgrade the firmware so that it's a new model scope has to talk to this old one.

**Dave Jones:** No, it it just worked. So, whatever they've done's been available for uh donkey's years. So, um yeah. So, this is really cool. So, I've got it uh set for a 30 MHz uh sweep here.

**Dave Jones:** I don't like um the fact like how they set this thing up, and I can't set like a start frequency. So, it's pretty rudimentary unless I'm using it wrong or whatever.

**Dave Jones:** Sweep type simple. Uh we we've got variable level. We don't want that. But anyway, 15 MHz uh center, which is our target uh frequency we uh want here, and we can control the amplitude of the function gen from here.

**Dave Jones:** So, uh 2 V amplitude, not that it matters, volts peak to peak, and 50 ohm uh load and whatnot, and the offsets. Um and I've got 150 uh points here.

**Dave Jones:** So, we can just uh now uh go in here and we can just go operation on. So, we can start that now and it will give Oh, yep, there it goes.

**Dave Jones:** And you see it flashy flash even though these aren't very bright. It'll start flashy flashing in a minute. And yep, there it goes between 1 and 4 and you see that the function gen here, it's controlling that frequency no problem.

**Dave Jones:** So, it's generating that sweep here and here is our response. This isn't the best frequency response analyzer I've used, but you know, it's good enough for Australia. Does the job.

**Dave Jones:** So, I've set the reference up there to 0 dB at the top, 10 dB per division down here. So, we should see it roll off at about 15 MHz.

**Dave Jones:** And I've got it set up to manually find the three minus 3 dB point of the sweep, which is a really cool function actually. So, it'll automatically find that.

**Dave Jones:** I don't know if it'll pop up yet cuz I haven't done it. No, it didn't No, I think it's got to wait until the end cuz it don't doesn't know where the it doesn't probably do that calculate automatic calculation until the end.

**Dave Jones:** But you can see at 15 MHz start to roll off there. The purple one is the phase, so green is the magnitude, purple's the phase. You can switch those off and phase is going all over the place, not that it matters.

**Dave Jones:** And there you go. But we're at like we're really down like, you know, minus 60 dB down here. So, isn't that There we go. There we go. And we'll Yeah, our frequency our minus 3 dB point it's automatically measured that at 15.74 MHz.

**Dave Jones:** So, that's really quite cool. So, that's in the display No, is that in the measure menu here? So, yeah, you can set up position P1 for the upper cutoff frequency.

**Dave Jones:** I like how they've got the little you know, diagram here of how that actually works. And you can get like the bandwidth and stuff like that. So, if you've got like a band pass filter, for example, you can get the upper cutoff and lower cutoff automatically done so that you don't actually have to measure that.

**Dave Jones:** And so, you can get up, you know, a couple of different things set up. It does actually do cursors as well. No, you're going to go into display for cursors.

**Dave Jones:** You can actually turn cursors on here, and then you can fiddle around with the cursors like that. So, you go over there -3 dB point. Yeah, that's about, you know, 15.6 15.7 exactly what it measured.

**Dave Jones:** There it Yes, - -3 dB precisely. So, yeah. Um so, it's got that automatic measurement. So, that's kind of cool. So, there you go. I just thought I'd um show you that that you can actually uh um you know, the Siglent.

**Dave Jones:** Leave it in comments down below if you know other gear that controls it via USB, which is handy. I didn't have to I thought, "Oh, I've got to set up another" cuz I Well, I do have two Ethernet ports here, but, you know, my but I don't think it's wired into my router, so I might have to dig around everything.

**Dave Jones:** And I thought, "Oh, I'll try the USB." Plugged it in, just worked. Bob's your uncle. Um so, yeah. Hats off to Siglent. I'm very happy with that. That is a very cool feature just to be able to control an external uh function gen cuz you're not limited by the internal function gen in here anymore.

**Dave Jones:** You can just use the external function gen. And of course, other manufacturers will do it if you network them and write scripts and things like that, but I'm not sure offhand.

**Dave Jones:** I'm sure there is, but offhand I don't know of another scope that will just automatically uh do that via USB like that. So, very simple, very handy. I like it.

**Dave Jones:** One thing I don't like is that like while you're in the frequency response analyzer, you can't adjust your channel one or your channel two. Um you can't do anything there.

**Dave Jones:** So, that's really annoying. You're going to have to exit completely exit the frequency response analyzer, change those, and then go back in. So, I don't know. Anyway, pretty cool.

**Dave Jones:** Catch you next time.
