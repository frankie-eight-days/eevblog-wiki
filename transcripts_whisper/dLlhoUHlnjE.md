---
video_id: dLlhoUHlnjE
title: LED Flicker 3 - More Electric Boogaloo
url: https://www.youtube.com/watch?v=dLlhoUHlnjE
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 20, "2": 39, "3": 59, "4": 76, "5": 93, "6": 109, "7": 129, "8": 145, "9": 169, "10": 181, "11": 201, "12": 221, "13": 241, "14": 257, "15": 281, "16": 301, "17": 321, "18": 333, "19": 357, "20": 373, "21": 389, "22": 405, "23": 421, "24": 445, "25": 465, "26": 481}
---

**Dave Jones:** Hi, just a quick follow-up video to this one-hung low LED driver flishy-flashy problem that I had. No point putting this on the main channel again. So I've got myself, I'll link those in down below if you haven't seen those videos. Anyway, I got myself some new LED drivers

**Dave Jones:** because it just wasn't worth hacking these things. It's just silly. Anyway, lots of, you know, almost 100% flicker or poor power factor, take your pick. And some people said, oh, I should just lower the input cap value and stuff like that and then you'll get better power factor.

**Dave Jones:** But it's still a power factor ripple and hence flicker. Trade-off. Anyway, so I got myself some new ones. These are flicker-free versions. Does it say flicker-free on here? Anyway, they are supposed to be. They're a Lifford brand. I believe I've shown these before and have used them before.

**Dave Jones:** And they're nothing special, but they are, you know, at least a reputable kind of brand, Chinese one. And they're pretty cheap. Got them from a local supplier. I got both a 700 milliamp and 500 milliamp versions. Anyway, these are supposed to be flicker-free.

**Dave Jones:** I do actually like the way they've done these cable clamps here. Check this out. They've got, of course, the little toothy thing there which clamps into the insulation on the wire, of course. And then they've got these little I don't know what you call those.

**Dave Jones:** Anyway, that slot in down the side. So when you push that in, it can't come back out. And it clamps the cable in. I reckon that's a pretty neat sort of cable clamping mechanism for this sort of product. Anyway, let's have a look inside these things.

**Dave Jones:** I was actually quite surprised. Definitely power turned off, yes. Now, I was expecting more because we saw the... do I still have it? No, I think I put it back together. Anyway, watch the previous video if you haven't seen the difference between a cheap-ass

**Dave Jones:** one like this with no second-stage output regulation at all, and hence why it's getting all the flicker. I expected this one to be a two-stage and have output regulation as well, but you can see that on the secondary side here, there's not much.

**Dave Jones:** We've got an output cap, and on the bottom side, there's even less. We've got ourselves some diodees there. I don't have my other pointer. Anyway, we've got some diodees, and that's it. There is no secondary side, second-stage output constant current regulation here. Once again, it's done on the

**Dave Jones:** primary side. And I won't be able to pull a part number off that little six-pin jobby, I'm sure, so I'm not sure which one that is. I won't even bother changing my macro lens, because then I'll have to edit this damn thing, and I don't want to do that.

**Dave Jones:** Anyway, so it's a very simplistic design just like this cheapy one here, but it's supposed to be flicker-free, and, you know, it's supposed to be decent. Anyway, it does have better input filter cap than before. It's a CapZon, so yeah, what do you expect?

**Dave Jones:** It's a cheap price. Anyway, it does have 12 mics at 450 volts. Is that 100 and... that's 105. Oh yeah, okay. It's doing the business. Anyway, so it does have a decent amount of input capacitance there, so that's definitely going to help, but it's basically exactly the same topology.

**Dave Jones:** We've got the full-wave bridge rectifier going directly across the filter cap of course, that's why the cap's 450 volts. And then we've got our, no doubt, it's similar to the chip that we... what was it? Onbright or whatever? Chip that we used here, but it could be another manufacturer.

**Dave Jones:** Don't know if it's the same one. But it's a similar topology, but they're getting much better... well, they're supposed to get much better power factor out of this. And ripple, flicker-free. So let's try it, let's power it up. Alright, got my current clamp probe on there.

**Dave Jones:** Power it on. And let's have a look at the scope of dope. There it is. Still got the same 200 milliamp... oh, 100 milliamp per division. 100, 200, 300, 400, so we're just over 400 odd milliamps there. And look at it. Naffle ripple.

**Dave Jones:** Very, very nice. And I can't see any flicker on the camera on the panel of this thing. And as for power factor, well, don't know if you can see that. I think you can. That is 0.94 power factor. And that's at, or near,

**Dave Jones:** 30 watts. So that's pretty darn impressive for just this, like, you know, single-stage converter like this. So I'm quite surprised, but obviously it's a better chip, they've got more input capacitance, they're doing some sort of right thing. Oh, let me turn that off now.

**Dave Jones:** I really like the look of the transformer. Doesn't that look like it's doing the business? I know this is a... well, it's a little bit higher power than this one, but look at that pokey little thing there. Look at this Bobby Dazzler. Ah, it's a thing of beauty.

**Dave Jones:** Joy forever. Anyway, and the bigger, look, external switching trennies there. So they're very, very nice. And they've got two of them. So I'm not sure of the exact topology, but it is, once again, a still, a primary side constant current regulation thing. Because there's no converter on the, no constant current regulator on the

**Dave Jones:** second side. So there you go. That's, you can, it shows that you can do a decent, low-ish cost. It's not going to be as low a cost as this one. They've really cut costs there. But it shows that you can actually do it with a primary side only

**Dave Jones:** regulation. That's great. Power factor, anything over 0.95 is pretty fine. And that ripple is, you know, it's not zero, but it's almost non-existent. Now for all practical purposes, this thing is not going to flicker at all. So that really is quite sweet. That's the Lifford

**Dave Jones:** 1. So if you want a trade-off of, you know, and like, once again, decent size transformer. The switching transistors don't need any heat sink on them. They are just flapping around in the breeze there. But anyway, if it, but these things aren't subject to vibration

**Dave Jones:** usually. And you know, decent amount of input filtering and it's got all the requisite and got common mode chokes on the input and everything else. Although I don't see a fuse. We've got an input. But I got a resistor there. But yeah, I don't see any.

**Dave Jones:** Is there any input fusing on that? That's a choke. Hmm. Anyway. Might have been cutting corners there. But oh, anyone want to see the trannies? There you go, I can't read that on the camcorder screen, so knock yourself out there. But for you switching transistor aficionados, there you go.

**Dave Jones:** But yeah, you know, this looks like a pretty decent trade-off between ripple and cost. So I think these were like $8? No. What were they? Oh, I don't know, I can't remember. Anyway, you know, around about like $10 a pop or something. So,

**Dave Jones:** just over I think, $12 a pop or something like that. Anyway, they are decent, looks like fairly decent drivers. Doing primary side regulation only and getting away with it. So there you go. Let me know your thoughts in the comments down below, and as always, give it a

**Dave Jones:** big thumbs up. Oh, and if you liked it, catch you next time.
