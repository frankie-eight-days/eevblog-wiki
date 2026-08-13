---
video_id: ty_sxMxUWeU
title: EEVblog #765 - LED Panel Lighting Switching Noise
url: https://www.youtube.com/watch?v=ty_sxMxUWeU
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 17, "2": 29, "3": 45, "4": 65, "5": 77, "6": 97, "7": 113, "8": 133, "9": 157, "10": 177, "11": 209, "12": 221, "13": 245, "14": 261, "15": 273, "16": 289, "17": 309, "18": 325, "19": 345, "20": 361}
---

**Dave Jones:** Hi, just a quick follow-up video to my previous LED ceiling light installation. Click here if you haven't seen it. Now, I was reminded that I actually forgot to do something which I was going to include in the video, a test. And that's to see if turning on the lights

**Dave Jones:** actually caused any, you know, common mode noise issues that can be picked up on, you know, when I'm measuring stuff here on the bench. And oh, yep, forgot to try it. So let's give it a go, compare the new lights to the old lights and see what the difference is.

**Dave Jones:** Now, what I've got here is my scope set to 5 millivolts per division. I've just got a BNC to banana plug, I'm just, you know, AC coupling, measuring the output noise of this power supply, like, you know, just something really simple, okay? And we can see that there's something there.

**Dave Jones:** Woo, look at that! That's, you can see that? That's my hand. There's noise, folks. Anyway, that's picking up the switching noise from the screen inside the scope, which is coupling in anyway. Let's not go there, I just noticed that. Now, I've done a whole separate video

**Dave Jones:** on common mode noise and actually trying to detect it and things like that, so click here if you haven't seen that one as well. So I won't go into explaining common mode noise and all the different types of noise and pick up and everything else.

**Dave Jones:** That's too confusing. I just want to see if these new lights actually do anything at all, okay? So I've actually got two switched on at the moment, and so let's have a look at my screen here. Okay, so here's the noise with just two of the nine of my new LED

**Dave Jones:** lights turned on. And you'll notice that there's a little spike there which I'm actually triggering. I won't touch the screen anymore, that's a bit bad. And we've got something happening in there. But let's go and turn the lights off and see if that goes away.

**Dave Jones:** Okay, I've got all my lights off in the lab, and nope! So those lights weren't causing that at all. It's got absolutely nothing to do with it. Okay, so I've got two of my lights on now, now I'll go up to my next level and I'll turn on, I think, three

**Dave Jones:** more. And there we go, still bugger all. And let's switch on the rest, here we go. And, oh, turn on. I've now got nine lights on, I've got all my lights on here, and as you can see sorry about a little bit of glare on the screen there, as you can see the new lights

**Dave Jones:** basically cause no noise whatsoever. Okay, I'm back to two lights here, two new lights. Now let's plug in three of my old lights down beside me here. Here we go, let's plug it in, and see what we get. Three LED light panels, whoa!

**Dave Jones:** Look at that! Whoa! That is an absolute shocker! The old ones were awful, look at that! Oh! And I disconnect, and it goes away. Reconnect, reconnect, bingo! There it is. Look, there's something seriously wrong with the switching converters, the crap one-hung low-brand switching converters in, to do with my

**Dave Jones:** old lights there, they were awful. Now actually I found a similar problem with these lights before, in that when I would switch them all on, I'd get extra noise. So I've actually narrowed it down to one particular switch-in plug pack here, and let me show you.

**Dave Jones:** So let's plug it in, and here we go. So we're getting all that shocking noise, but I'll disconnect the culprit. Here we go. Where is it? There we go. Gonski, look at that! So now we're back to where we were before. So it was one particular

**Dave Jones:** plug pack, it actually wasn't all of the existing lights you know, actually doing that. They will do it though, because the existing lights were capable of pulse-width modulation, i.e. dimming. I could actually, I had a remote control for the previous ones that I could actually

**Dave Jones:** dim. And if you dim them, yeah, you got some pretty horrible noise all around the place. But I always ran these on full brightness, so they weren't actually, you know, pulse-width modulating the lights. It was just, you know, constant current, like these new ones are.

**Dave Jones:** Just continuous constant current. So really, these new lights, no problems whatsoever. Dodgy one-hung low brand plug pack on the old one. Now I was actually powering that panel over there before, and now I've actually switched it over to this one, try and diagnose the problem.

**Dave Jones:** Now, this old one actually comes with two separate things. We've got the mains plug pack, which just gives a standard 24 volt DC output. And then we've got the actual constant current driver itself. And I've narrowed it down to this plug pack. So I've taken this

**Dave Jones:** good panel that wasn't giving any switching noise before, using its constant current regulator, and plugging it into this dodgy power adapter this one-hung low one, that came from literally one-hung low. Like there is no brand on that whatsoever. It's just made in China, thank you very much.

**Dave Jones:** This was the culprit. So this is actually, this plug pack is connected to the mains here, so if there's no load on it there's no problem whatsoever, there's no switching noise. But the second that we actually load this sucker down, woohoo! There we go.

**Dave Jones:** There's all our horrible switching noise. What a piece of shit that plug pack is. So there you go, these new lights, no problems whatsoever in terms of switching. Got a top quality plug pack there, as opposed to this piece of shit. And there's

**Dave Jones:** only one place for this. Catch you next time.
