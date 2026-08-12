---
video_id: lXvXBdTP7Tg
title: Haasoscope Pro - An Oscilloscope Space Oddity
url: https://www.youtube.com/watch?v=lXvXBdTP7Tg
source: youtube-asr
timestamps: {"0": 0, "1": 8, "2": 20, "3": 30, "4": 45, "5": 59, "6": 72, "7": 81, "8": 94, "9": 105, "10": 118, "11": 127, "12": 137, "13": 152, "14": 166, "15": 177, "16": 187, "17": 198, "18": 210, "19": 222, "20": 234, "21": 248, "22": 259, "23": 273, "24": 284, "25": 296, "26": 310, "27": 325, "28": 335, "29": 350, "30": 360, "31": 378, "32": 389, "33": 401, "34": 416, "35": 427, "36": 442, "37": 461, "38": 475, "39": 489, "40": 506, "41": 514, "42": 530, "43": 548, "44": 559, "45": 568}
---

**Dave Jones:** All right, I downloaded the software from the GitHubs and the GitHubs has uh yeah, all sorts of uh all sorts of stuff. It's fully documented. Everything else absolutely fantastic.

**Dave Jones:** Um and it's got ADC board or ADC firmware uh board firmware. ADC I guess he calls it the ADC board. Okay. It's it's the actual it's the main board.

**Dave Jones:** Um and the so it's got Python stuff. What is that? So it's got a Python version, does it? And anyway, I went into the distributions. It's got a Mac version by the looks of it and Windows.

**Dave Jones:** Um, that was only a couple of weeks ago. So, I downloaded that and I ran it and not only do we get this little uh command line um thing, but but here is the software and it is blindingly fast.

**Dave Jones:** Um, I haven't done anything with it yet. Um, this is just it immediately popped up like this. Um, and it's got voltage division voltage divisions. has one volt per division to like plus - 5 volts.

**Dave Jones:** It's like that doesn't seem right. It's almost as if like there's a bit there. It's like it's zoomed in or something displayed. What is that AC coupled? We got our 1 megga ohms.

**Dave Jones:** So, it's almost as if we're down in the noise there. I'm not sure what's going on. Uh so, trigger. So, we're running, right? And then we can we can single shot capture.

**Dave Jones:** No, we can't. Oh, yeah. Yeah. There we go. Okay. Right. There you go. But it's um it's super quick. Hang on. No. Run. Single. Run. There we go. You can fiddle the PLL clocks, can you?

**Dave Jones:** That's all grayed out. Maybe there's a have to go into a advanced menu or something to do that. Uh gain 160 molts per division. So gain is minus 6.

**Dave Jones:** Okay. So it does have well 20 molts per division. Okay. So we can go right down, but that's software. Not sure if that's hardware. I haven't looked yet. Not sure how we get the second channel up.

**Dave Jones:** We've got all our measurements and stuff, but we got some live measurements down the bottom here. Four split channel one, four switch clocks. Toggle PLL controls. Here you go.

**Dave Jones:** So, we can fiddle the PLL controls. Wow. If you want to like overclock overclock the ADC and stuff, go for it. Over sampling alignment. Uh, record to file. Update firmware.

**Dave Jones:** Do it via here. That's cool. Version 27.01. Jeez, had lots of lots of sucks of the sav at that. Um, so we got our grid. Okay, so we can turn off high- res, turn on or off high-res because this is a 12 bit.

**Dave Jones:** Got to remember this is 12 bits at 2 gig samples per second. It's a sorry, a 2 ghahz bandwidth at 3.2 gig samples per second. Like, okay. Oh, I've heard the fan come on.

**Dave Jones:** There's some rattling. There's some rattling. I put my hand on it and it vibrates less. But I've heard it come on. So maybe it does get hot. And I think probably a better thermal solution.

**Dave Jones:** That that fan is now annoying me. I'm not sure. You're probably not hearing it, but that's enough to annoy the heck out of me. So yeah. Um I think a better thermal solution.

**Dave Jones:** Um yeah, just um yeah, you got to couple it to the case, but as I said, you got the slide on case, so it's it's harder to get an effective um thermal solution there.

**Dave Jones:** Anyway, we've got our dual channels and the other channels doing that. Now, the channel one lead has turned from like white bluey to red. The channel 2 lead is white bluey, but it looks like they're doing the same thing.

**Dave Jones:** So, like it's one gig input impedance. I can short it out, but I suspect shorting it out, I get my little 50 ohm shorter plug, but I suspect that won't do anything.

**Dave Jones:** No, because it it it shouldn't have shouldn't have done anything. What's going on? Uh, do I have to calibrate it? No, that's just oversampling alignment. Didn't pop up with anything.

**Dave Jones:** It's just 800 meg any alias. Nice. Okay, so that changed it a bit. So, the problem is we don't have our traditional um oscilloscope uh controls here. Like where's the time base?

**Dave Jones:** Okay, we got time nanconds here, but like is that like that's not like nanconds per division. It's interesting that it has a frame counter. It's doing 300 like 90.

**Dave Jones:** It's almost pushing 400 frames per second. 46,000 events at 81 hertz at 08 megabits per second. Uh sorry, yeah megabytes per second. And okay, um this is not yet.

**Dave Jones:** This is not like it's starting sound. It's not working like a traditional oscilloscope interface with your trigger in your m in the middle. Well, maybe that that is the trigger point.

**Dave Jones:** I can't Oh. Oh, I can drag it. Okay. Uh axis plot options. Oh, okay. Oh. Oh. Oh, fancy pancy. Okay. So, we can do our power spectrum now. We can do a ton of stuff.

**Dave Jones:** Okay. All right. And we can do log average. Oh my god. Okay. Right. Pretty advanced. We can export stuff. So, it's Y is okay. Y is like Yeah, it's zoomed in.

**Dave Jones:** That's what it seems to be. Like it's zoomed into the couple of bits there. But look, I go to like manual axes, right? So, let's just go minus2 to + two, right?

**Dave Jones:** Minus2 to plus two. Okay, there we go. So, we've adjusted that, but that's in volts, right? That's in volts. And where is like we're like jumping to full scale here.

**Dave Jones:** I don't know. Did I do something to it in the tear down? I shouldn't have AC coupled. Okay. Whoa. Hello. Whoa. That's changed dramatically. What's going on? One megga input impedance.

**Dave Jones:** I can hear the relay click for the 50 ohm. Okay. But no, we've got a 50 ohm input impedance. We should be getting a flat line there. What the heck's going on?

**Dave Jones:** I don't get it. Show FFT. Boom. Okay. But yeah, no, we can't see anything because we got no input signal. Um, no board zero. Okay, because we've only got one board and channel one, two.

**Dave Jones:** Okay, that's just changed the color. Is it trigger threshold? There you go. We can adjust our trigger threshold, but that's not helping me. What the heck? What the heck's going on?

**Dave Jones:** Trigger time faster or slower. There's no ability like I can change my time like X-ax is right. I can go manual but that's not what I want. Like I I expected a traditional oscilloscope.

**Dave Jones:** Um I would not call it an oscilloscope. I'd call it a sampling system or something like that. Um because it hasn't got your traditional oscilloscope interfaces. Like it starts at zero over here and then just displays zero to 1200 nconds.

**Dave Jones:** I mean we can adjust that of course. Let's Let's adjust that to like we can't even set Oh, okay. The fan stopped rattling now. Oh, no. No, it's back.

**Dave Jones:** Oh, that fan's dodgy as Oh, change the fan, please. Yeah, better thermal solution required. Um, auto 100%. Okay, so manual. Okay, so let's go from minus I don't know 100 to plus 100.

**Dave Jones:** 100 what? What are the units for the x- axis? Like nanconds. They're all in nanconds. It can't do anything else. Like, I don't get it. Am I missing something?

**Dave Jones:** What am I missing? And it can't do any pre-trigger, right? Can't do any pre-trigger stuff. We set our threshold here. There's no ability to do pre-trigger information or like see any pre-trigger stuff.

**Dave Jones:** That's just I don't get it. Anyway, our ADC board's only at 30 degrees. It's not like it's getting hot there. I don't get what's going on here. I might have to email Andy.

**Dave Jones:** Like I've I'm probably headed to the gym in 15 minutes. So, I'm probably stop this. I might upload this as a second channel video, a quick second channel video maybe, and contact Andy and go, "Well, what what's going on?"

**Dave Jones:** Um, got external trigger. Okay. So, now it's going back to like an a slower auto trigger. It's kind of what you'd expect. Okay. What's to t? I don't know.

**Dave Jones:** Uh, delta delta what? Some difference in trigger threshold or something. I I don't get it. And to change our offset, we've got to go like here. We can't uh 0.5.

**Dave Jones:** We can't like No, didn't even do that. Offset five. No. Ah, mill volts there. Okay. No, I'm not getting it. I don't understand this at all. It's almost as if something's something's wrong with the hardware.

**Dave Jones:** I don't like we we should get a flight. Like I can understand. Okay. If it's always doing it's not doing the regular time per division. It's only going from zero nonds to, you know, it's just re-triggering.

**Dave Jones:** There's no pre-trigger information, etc. Right. I Okay, I can understand that. What I don't understand is why the data is doing this. Do I have to feed in a signal?

**Dave Jones:** I shouldn't have to feed in a signal. No, I'm going to have to get back to you on that.
