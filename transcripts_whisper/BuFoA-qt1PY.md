---
video_id: BuFoA-qt1PY
title: Brymen BM2257 Intelligent Auto Power Off (iAPO) tested
url: https://www.youtube.com/watch?v=BuFoA-qt1PY
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 19, "2": 43, "3": 59, "4": 75, "5": 91, "6": 107, "7": 123, "8": 135, "9": 151, "10": 173, "11": 193, "12": 243, "13": 263, "14": 283, "15": 307}
---

**Dave Jones:** Hi, just a quick video testing the new BM-2257 multimeter, available at EEVblog.store, by the way, which is pretty much an upgrade to the old BM-235, still a venerable meter, still available. It's a few dollars more, won't go into the details. Full review video coming soon.

**Dave Jones:** And also the BM-786 here, because the BM-2257 has a new feature called Intelligent Auto Power Off. And so, I'll try and overlay something here. So it's designed to reset the power off, the auto power off timer when you actually take a measurement. Now, that didn't happen on the 786,

**Dave Jones:** I don't, well, the 786, it didn't happen. Somebody actually reported this on the forum, and it just turned off after 30 minutes or whatever. So I thought I'd actually test that. So this has a new Intelligent Auto Power Off. It'll automatically turn off in capture mode as well.

**Dave Jones:** So if you put it in, sorry, if you put it in min-max average mode, apparently it'll switch that off, but I won't test that. I just want to test a periodic measurement. Will it actually continue to reset that sleep timer? So what I've got set up here is a

**Dave Jones:** 100 millihertz signal, so basically once every 10 seconds, 10% duty cycle. And you can see it, it's going from 0 to 5 volts here, and you'll see them all tick over. There we go, it goes to 5. I think this has a slightly better update rate, which is why it stays

**Dave Jones:** there at 5, gets to 5 quicker than the 235 does. Of course the BM786 has an extra digit of resolution there. It went to 2.5 volts interim there, but that's because the waveform just happened to be in the point in the sample period where it actually sampled that.

**Dave Jones:** So it's neither here nor there. But anyway, so I've got a timer here, so I'm going to reset all these. So I'm just going to leave this, it'll just put in a small pulse, a 1 second pulse every 10 seconds, so it'll continually

**Dave Jones:** update the meters, alright? So what I'm going to do is I'm going to turn them all off, and then I'll do a time lapse of this thing. So I will start the timer now. There we go. And we'll turn it back to DC volts.

**Dave Jones:** And of course you can manually switch the auto power feature off, but I won't actually do that bit of glare on the screen there. So there you go. I will leave this running for an hour. I'm going to the gym now, so probably an hour

**Dave Jones:** and a half. And I'll come back and then I'll time lapse edit this and we'll see what happens. Hopefully we can see it, we can see the timer on the screen. Yeah, good to go. I'll get back to you. Oh, just before I leave, I thought I'd whack in another

**Dave Jones:** BM2257 and actually put it in the recording mode. So let's switch that on so there's no auto power off thing. And recording mode, okay, I won't feed a signal into that. So yeah, we'll just see if that doesn't switch off, because it's not supposed to when it's in

**Dave Jones:** recording, min-max recording mode. recording mode And I'm back, and as predicted the 786 turned off. It's been a long time since I looked at the BM235 manual. Does it have the intelligent auto off? I thought it was or maybe they didn't advertise it as such, but it

**Dave Jones:** looks like it resets itself. And the min-max hasn't turned off at all. So what's it been, an hour? Yeah, hour and 41 minutes there. And of course the 7857 with the intelligent auto off hasn't switched off either. And yep, sure enough, I had completely forgotten that the BM235

**Dave Jones:** even though it dates back, what, a decade now, yes it still has intelligent auto off. Why they didn't add that to the BM786, which is a relatively new model in the scheme of things, why they didn't add that, I don't know. So that just seems

**Dave Jones:** I don't know, maybe it's a processor architecture thing? But I know that on the BM235 they do have extremely limited memory space inside the micro, inside this thing. So yeah, I've said over the years, can you add this feature and this feature, and they go, no, not really, we don't really have the space for it.

**Dave Jones:** So yeah, 786 though, it's interesting, huh? Anyway, the intelligent auto off works fine and it's the same on the old school BM235. Anyway cool bananas. Catch you next time.
