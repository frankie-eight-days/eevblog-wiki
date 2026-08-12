---
video_id: e4wvxWWMla0
title: Rohde & Schwarz HMO1202 - Like a Bought One
url: https://www.youtube.com/watch?v=e4wvxWWMla0
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 25, "3": 35, "4": 52, "5": 67, "6": 83, "7": 99, "8": 110, "9": 125, "10": 139, "11": 152, "12": 165, "13": 176, "14": 190, "15": 206, "16": 219, "17": 233, "18": 247, "19": 260, "20": 274, "21": 286, "22": 305, "23": 323, "24": 338, "25": 346, "26": 360, "27": 373}
---

**Dave Jones:** Hi, you saw in a previous video how dumb-ass Dave left the uh shielding can off this Rohde & Schwarz HMO 1202 series scope when I did a um hack-in video on the uh SPI bus uh for the front end to

**Dave Jones:** hack around with the uh bandwidth and stuff like that. And yes, it is uh possible if you tap in uh to the SPI bus cuz the uh software bandwidth is uh defined by the front end chip and you

**Dave Jones:** send commands to it and the bandwidth limits it. So, anyway, um yeah, I forgot to put the metal can back, and of course it's picking up the 50 Hz. And I'll show you, if I actually pick this up, you'll

**Dave Jones:** see that's coming from my ESD mat. The closer it gets, it picks it up. Boom, look at that. And of course, uh it's not supposed to be doing that um if this anti-static mat was actually grounded, and it was supposed

**Dave Jones:** to be, but doll, I just uh checked and yeah, my grounding point uh must have been shuffling my power points or whatever, and yeah, it wasn't um it plugged back in. So, let me go plug it back in, and I'll show you. Hang on.

**Dave Jones:** Hang on. Ready? Ready? Boom, look at that. The anti-static mat is now grounded. Of course, um it is still a problem with the scope uh of course that it's not shielded. It's just that the uh ESD mat mat is acting

**Dave Jones:** as a really nice uh 50 Hz picker-upper, and um yeah, it's a bit still, there you go. So, I'm going to leave it ungrounded so we have a nice 50 Hz uh source under the scope, and I'm going to put in a new metal can. And I

**Dave Jones:** can show you that here. Let's actually hook my ESD mat up, and let's ground it here to the scope, which is of course is grounded, and there you go. It uh it still still comes through. You can still

**Dave Jones:** see a bit of the 50 Hz on there. But you can see, when your mat's uh floating, then you know, it's a pretty effective coupling, capacitive coupling of course, through the scope. So, it picks all that 50 Hz crap up and yeah, in it goes,

**Dave Jones:** straight into the front end if you're not shielded. Anyway, I'll leave that open and I'll get Well, here it is. I've already found one. I've got a metal shield. So, where did I get this shield from? Well, it pays to keep your old dumpster

**Dave Jones:** teardowns. Looks one like one of these audio video things. We've got component video here. We've got HDMI and we've got our RF can. And this is where I got it from. The RF can and then I just bent

**Dave Jones:** the sides up like that. It was a 30 mm width can and this one's it's pretty close to that, like near enough. This side here, unfortunately, is a little bit short like that, but this side will go in

**Dave Jones:** there perfectly. And I just bend up the ends so that it doesn't short out the components on either end. And it's not quite as long as I need, but it's near enough. It really needed to be like a

**Dave Jones:** millimeter wider or something like that. So, this actually this goes into the clips nicely in the board as I show you in a second, but the other side yeah, it sits on the inside, but it still just touches. So, it's almost perfect. So,

**Dave Jones:** you can see here we've got the clips here, here, here and here. This one unfortunately has lifted when I was desoldering that cuz these actually were soldered in. Yeah, the little bit of lift there, but it's no problem. I don't even have to really

**Dave Jones:** repair that. So, what I'm going to do is I'm going to put this one on this side in here like this and that hang on. I've got it cuz you don't want it to short out. See, I want it

**Dave Jones:** just to be short of the BNC in there. Not sure if you can see that. So, there you go. And you can see that it it's just on the inside there of those. But what I can do is just um you

**Dave Jones:** know, tack solder that on that light there. No worries. And um yeah, that's almost bang on. Now, you'll notice um that they covers the relays in here, and they do actually use some magnetic uh shielding tape on top here, but this is

**Dave Jones:** not a magnetic field problem. This is an electric uh field problem picking up uh the 50 Hz. So, the metal can should totally eliminate that. So, I'm going to do a uh quick test with this. Uh just, you know, I'm not soldering it

**Dave Jones:** um down or anything. It's just sitting there like that. So, let's check it out. Okay, let's power it up. Good thing is, this scope boots up nice and quickly, and there it is. Winner, winner, chicken dinner. That is

**Dave Jones:** pretty close. Can you still see? I can still see some 50 Hz on there, but there's basically naff all in it. I mean, that's just nuts. Let's turn on the quick view here. Okay, so what do we get on channel one, which is our good

**Dave Jones:** channel? Peak-to-peak, 400, 440 microvolts, something like that. The RMS, it's down around uh 130. It just can't do that. Yeah, 140. Just can't do it. Channel two, which is our unshielded one, 440 microvolts. Yeah, the RMS looks like

**Dave Jones:** it might be a smidge higher. Maybe a smidge, but there's There's not much in it, is there? I mean, jeez. That's our That's 10 milliseconds per division, 20. There you go. Oh. Nah, look, it's it's absolutely identical, really. 44 440 peak-to-peak,

**Dave Jones:** 220 odd RMS on channel one, channel two, to like there's not There's There's nothing in it. You really can't pick that at all. So, that works fine. So, yeah, I'll just uh tack solder one side of that down, so you can cuz you don't

**Dave Jones:** want to drop it off in the bottom of the case. That could really uh ruin your day. So, yeah, you want to tack solder it in there uh to make sure any vibration or knocks isn't going to uh

**Dave Jones:** make it fall out, and Bob's your uncle. So, I've just tack soldered down just one side of that. Still warm. And that should be good to go. That's not going to fall out. And yeah, it doesn't quite, you know, I could like could argue I

**Dave Jones:** should bend over the flat here. No, doesn't matter. Like the fact that it's covered and it's not picking up the 50 hertz, that is going to do the business, as you saw. No worries. And that was the previous test was, by the way, with the

**Dave Jones:** ESD mat disconnected. So, with the mat connected, there's just there's going to be no pick up at all. So, there you go. I'm fixed. No worries. Catch you next time.
