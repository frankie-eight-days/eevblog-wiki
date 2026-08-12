---
video_id: LbqnHtNPt9Y
title: Siglent Oscilloscope - Function Gen USB Connection Test
url: https://www.youtube.com/watch?v=LbqnHtNPt9Y
source: youtube-asr
timestamps: {"0": 1, "1": 13, "2": 28, "3": 38, "4": 56, "5": 74, "6": 90, "7": 106, "8": 119, "9": 130, "10": 143, "11": 159, "12": 172, "13": 183, "14": 198, "15": 212, "16": 225, "17": 240, "18": 257, "19": 271, "20": 284, "21": 294, "22": 306, "23": 321, "24": 339, "25": 353, "26": 365, "27": 380, "28": 393, "29": 403, "30": 415, "31": 428, "32": 445, "33": 460}
---

**Dave Jones:** Hi, I just thought I'd show you something cool with uh Siglent uh gear here. You can probably do it with other uh manufacturers as well, but I think this is really cool. Now, it I didn't know that this was possible, but it only

**Dave Jones:** reoccurred to me after my uh Rohde & Schwarz MXO 4, the actually the uh frequency response analyzer, the FRA in that um actually the license for that expired, and I tried to use it, and of course it had expired. And also the

**Dave Jones:** arbitrary waveform generator license it it expired cuz I only had a demo. And I was in the middle of shooting a video, and I thought, "Oh, I'm going to need a different way to do this, but I needed a

**Dave Jones:** 100 MHz bandwidth frequency response analyzer." And I didn't I thought I didn't have one. Then it occurred to me, "Duh, Dave, um the Siglent gear can actually uh join uh an external uh function generator um to their oscilloscope." So, I thought I'd never

**Dave Jones:** tried it before, um but it just occurred to me that this is actually uh doable. So, what I've got is uh my um Siglent SDG gen, which is a 120 MHz bandwidth function generator. So, uh yeah, it's more than the 100 MHz that I

**Dave Jones:** needed, and uh I've got the um uh the Siglent SDS 2354X. It's a 350 MHz scope. It's got frequency response analyzer built in, as you can see. And also has an arbitrary waveform generator built in uh with the um output on the uh back

**Dave Jones:** there, but it's only uh 20 I think 20 or 25 MHz bandwidth uh function generator, as most scopes are. The Rohde & Schwarz is the only oscilloscope I've got that has a 100 MHz bandwidth function gen built in. So, um yeah, it's limiting. If

**Dave Jones:** you use the internal frequency response analyzer like this, you can and the internal function gen, you can only go up to 20 or 25 MHz or whatever it is. But, what I've done is hooked uh the USB onto this over to the Siglent function

**Dave Jones:** gen. You can either use Ethernet or uh USB, but I'll go in here. So, I'm in the uh frequency response um analyzer at the uh moment, and we can actually go into uh configuration up here, and you can

**Dave Jones:** see that the interface you can actually set that um to be uh the internal, which is the internal function gen, um or the uh USB, which I've got, or LAN as well. So, you connect it to USB, and I can

**Dave Jones:** press test, and it's successfully connected. Bingo. The scope can now control the function generator to do the external frequency uh sweeping. And so, what I've got is a little uh just a little 15 MHz um uh filter down here uh

**Dave Jones:** low-pass uh filter. So, the input's on uh channel one here, and the output's just go into channel two, and we measure the uh we can measure the frequency response of that. So, uh yeah. This actually works straight out of the box,

**Dave Jones:** even though I think like this is many years old. I can't remember how old this thing is. I don't think I've upgraded the firmware in a long uh time, but I thought, you know, I might have to upgrade the firmware so that it's a new

**Dave Jones:** model scope has to talk to this old one. No, it it just worked. So, whatever they've done's been available for uh donkey's years. So, um yeah. So, this is really cool. So, I've got it uh set for a 30 MHz uh sweep here. I don't like um

**Dave Jones:** the fact like how they set this thing up, and I can't set like a start frequency. So, it's pretty rudimentary unless I'm using it wrong or whatever. Sweep type simple. Uh we we've got variable level. We don't want that. But

**Dave Jones:** anyway, 15 MHz uh center, which is our target uh frequency we uh want here, and we can control the amplitude of the function gen from here. So, uh 2 V amplitude, not that it matters, volts peak to peak, and 50 ohm uh load and

**Dave Jones:** whatnot, and the offsets. Um and I've got 150 uh points here. So, we can just uh now uh go in here and we can just go operation on. So, we can start that now and it will give Oh, yep, there it goes. And you see it

**Dave Jones:** flashy flash even though these aren't very bright. It'll start flashy flashing in a minute. And yep, there it goes between 1 and 4 and you see that the function gen here, it's controlling that frequency no problem. So, it's generating that sweep

**Dave Jones:** here and here is our response. This isn't the best frequency response analyzer I've used, but you know, it's good enough for Australia. Does the job. So, I've set the reference up there to 0 dB at the top, 10 dB per

**Dave Jones:** division down here. So, we should see it roll off at about 15 MHz. And I've got it set up to manually find the three minus 3 dB point of the sweep, which is a really cool function actually. So,

**Dave Jones:** it'll automatically find that. I don't know if it'll pop up yet cuz I haven't done it. No, it didn't No, I think it's got to wait until the end cuz it don't doesn't know where the it doesn't probably do that calculate automatic

**Dave Jones:** calculation until the end. But you can see at 15 MHz start to roll off there. The purple one is the phase, so green is the magnitude, purple's the phase. You can switch those off and phase is going all over the place, not that it matters.

**Dave Jones:** And there you go. But we're at like we're really down like, you know, minus 60 dB down here. So, isn't that There we go. There we go. And we'll Yeah, our frequency our minus 3 dB point it's automatically measured that at

**Dave Jones:** 15.74 MHz. So, that's really quite cool. So, that's in the display No, is that in the measure menu here? So, yeah, you can set up position P1 for the upper cutoff frequency. I like how they've got the little

**Dave Jones:** you know, diagram here of how that actually works. And you can get like the bandwidth and stuff like that. So, if you've got like a band pass filter, for example, you can get the upper cutoff and lower cutoff automatically done so

**Dave Jones:** that you don't actually have to measure that. And so, you can get up, you know, a couple of different things set up. It does actually do cursors as well. No, you're going to go into display for cursors. You can actually turn cursors

**Dave Jones:** on here, and then you can fiddle around with the cursors like that. So, you go over there -3 dB point. Yeah, that's about, you know, 15.6 15.7 exactly what it measured. There it Yes, - -3 dB precisely. So, yeah. Um so, it's got

**Dave Jones:** that automatic measurement. So, that's kind of cool. So, there you go. I just thought I'd um show you that that you can actually uh um you know, the Siglent. Leave it in comments down below if you know other gear that

**Dave Jones:** controls it via USB, which is handy. I didn't have to I thought, "Oh, I've got to set up another" cuz I Well, I do have two Ethernet ports here, but, you know, my but I don't think it's wired into my

**Dave Jones:** router, so I might have to dig around everything. And I thought, "Oh, I'll try the USB." Plugged it in, just worked. Bob's your uncle. Um so, yeah. Hats off to Siglent. I'm very happy with that. That is a very cool feature just to be

**Dave Jones:** able to control an external uh function gen cuz you're not limited by the internal function gen in here anymore. You can just use the external function gen. And of course, other manufacturers will do it if you network them and write scripts and things like

**Dave Jones:** that, but I'm not sure offhand. I'm sure there is, but offhand I don't know of another scope that will just automatically uh do that via USB like that. So, very simple, very handy. I like it. One thing I don't like is that like while you're

**Dave Jones:** in the frequency response analyzer, you can't adjust your channel one or your channel two. Um you can't do anything there. So, that's really annoying. You're going to have to exit completely exit the frequency response analyzer, change those, and then go back in. So,

**Dave Jones:** I don't know. Anyway, pretty cool. Catch you next time.
