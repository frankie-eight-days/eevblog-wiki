---
video_id: ImyUB3_n9fw
title: EEVblog #442 - Analog Vs Digital Oscilloscope Noise
url: https://www.youtube.com/watch?v=ImyUB3_n9fw
source: youtube-asr
timestamps: {"0": 10, "1": 33, "2": 65, "3": 96, "4": 128, "5": 159, "6": 198, "7": 222, "8": 241, "9": 275}
---

**Dave Jones:** Now digital scopes have this uh reputation of being higher in noise than analog scopes, for example, but that's not necessarily uh the case. It's just that with their update uh rate and capture, they're actually capable of displaying more of the noise than a traditional analog scope. And you might think, "Well, our problem is going to disappear if we use an analog scope." But no, it's not. Check it out. Let's have a look here. It's hard to get this.

**Dave Jones:** I'm going to have to set the exposure, but you can see the switching uh You can see, look, we're still got switching noise in there. We're still got common mode noise even on our analog scope. It's nothing to do with the scope at all. It's inherent. It's common mode noise being picked up through the mains input between uh the earth and the neutral. There we go. I turned down the contrast on my camera, and you can see the switching noise in there. It's actually quite significant. Now that's 5

**Dave Jones:** ms per division with no uh times 10 amplifier in there, and it's really it's going to be hard to see on camera, but you can actually see the switching noise in there. It's actually quite significant. Exactly what we're seeing on the digital scope, except the digital scope picks it up better by virtue of its uh sampling and um greater persistence, effectively, especially on the cheaper scopes. But you can see that switching noise in there. So, this is where digital scopes actually have an inherent advantage. You're being fooled

**Dave Jones:** You're effectively being fooled by your analog scope thinking that there's no, you know, you turn the intensity down. There we go. And you might think, "Oh, well, you know, it's just that looks clean as a whistle, you know, not a problem at all." But you're actually getting that common mode noise on there, which you normally wouldn't see. Now, if I actually go, turn the time base right up here, and move my horizontal position, and turn that up, look, there it is. You can actually Let's turn the

**Dave Jones:** There we go. You can see it. There it is. You can see that switching noise there, that common mode switching noise. You can't necessarily see it when it comes in here. You see it It's sort of, you know, it just vanishes because, you know, it's the analog scope is not really capable of the persistence that a digital scope is capable of. But look, that's 5 mV 5 mV per division. There it is. I've got my times 10 gain not in, and you can see Look at

**Dave Jones:** that switching noise. It's exactly the same amplitude we get on our digital scope. And look, I'll do it in a single shot. I'll take it over. We're 5 mV per division there, and there we go. It's the same thing. If we stop it, and look, we can see that amplitude is exactly exactly the same. But our digital scope, because of the greater Well, effectively, because digital scopes aren't as good, in {quote} marks, as our analog scopes, the slower your updating scope, the greater you're going to actually see this noise.

**Dave Jones:** So, if you've got a really super fast updating scope with persistent variable persistence and all that sort of magic, then you're going to see it less than you would on a lower-end digital scope, which shows all this stuff up. And you can see precisely that on this Rigol scope. It's going to be very similar to this analog scope. I've turned my intensity knob Here's my intensity knob.

**Dave Jones:** I've turned it all the way down to the bottom, like this. And you might think, "See, we're getting that nice flat line." You can just see some switching components in there, okay? And of course, when you turn the horizontal knob, it stops picking it stops refreshing and you can momentarily see the noise on there.

**Dave Jones:** Let's turn it back and if we turn up our intensity, look, all that noise has magically appeared again. So, it's not that these digital scopes are inherently noisier than analog scopes. It's not the case. It's just that they're better off the sampling nature of the digital scope and the greater effective persistence on the screen is better at picking up these noises. So, really, you know, be careful when you claim that analog scopes you know, they're they're much lower noise than digital scopes.

**Dave Jones:** Not only is that not necessarily true, it can be in some circumstances, but not necessarily true, but the fact is you can miss a lot of stuff like this common mode noise that you wouldn't normally get on this on that you could easily pick up with a digital scope. So, just be careful when you're talking about noise in systems like this.
