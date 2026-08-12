---
video_id: zoyaHOqp9gI
title: Rigol DHO800 Oscilloscope Fan Upgrade Experiment
url: https://www.youtube.com/watch?v=zoyaHOqp9gI
source: youtube-asr
timestamps: {"0": 0, "1": 11, "2": 31, "3": 43, "4": 55, "5": 71, "6": 82, "7": 93, "8": 104, "9": 122, "10": 133, "11": 143, "12": 156, "13": 171, "14": 189, "15": 200, "16": 214, "17": 242, "18": 266, "19": 275, "20": 289, "21": 303, "22": 317, "23": 329, "24": 344, "25": 361, "26": 370, "27": 379, "28": 396, "29": 407, "30": 414, "31": 434, "32": 450, "33": 460, "34": 478, "35": 490, "36": 499, "37": 516, "38": 534, "39": 551, "40": 568, "41": 583, "42": 593, "43": 604, "44": 618, "45": 626, "46": 636, "47": 644, "48": 667, "49": 683, "50": 695, "51": 704, "52": 725, "53": 738, "54": 759, "55": 790, "56": 810, "57": 817, "58": 827, "59": 841, "60": 850, "61": 871, "62": 880, "63": 895, "64": 910}
---

**Dave Jones:** Hi, just a quick video looking at a potential fan upgrade for the Rigol DHO800 and 900 series scope cuz there's a lot of talk about the fan noise which might annoy some people.

**Dave Jones:** It's you know, you can hear it. Anyway, this is the fan that's used inside here. It's a tiny little thing and I thought basically 45 mm diameter frameless jobby very common on GP like old school GPUs and stuff like that.

**Dave Jones:** Anyway, and I've already done a second channel video on basically you need a fan on this thing. It'll overheat and it'll shut down even in room temperature like lab temperature things here.

**Dave Jones:** Anyway, I've got two Delta fans of course top quality fans. You can get the I got these off Digikey and they have them in stock. So let's have a squiz.

**Dave Jones:** So I'll put the model numbers and links down below for these but basically two different ones. This one's slightly bigger than this one. They're all 12 volt fans as is this one but as you saw in the previous thermal testing video on this this was running at 8 volts.

**Dave Jones:** I think it was. So they're actually derating that fan just to get it a bit quieter cuz they don't need the full air flow afforded by the 12 volts on there.

**Dave Jones:** These are both three wire jobbies but we can just use the two wire and ignore the taco output. Both of these do seem to physically fit but let's have a look.

**Dave Jones:** This is the nearest one is you can see that the fan blades are a bit thicker on this Delta one. So yeah, and and they're a bit more vertical.

**Dave Jones:** These are like it is a slimmer Oh, no, the overall thickness is basically the same there but the Delta actually has a bigger more vertical fan. So it's going to get I would presume greater air flow for a given a uh you know for a nominal RPM.

**Dave Jones:** So yeah, very similar but unfortunately they are this tri mount but they don't have it's hard to show you there but the footprints don't quite line up like that.

**Dave Jones:** The holes don't line up. The Delta ones the holes are further apart like that and both Delta fans I think have yep they've got the same pin out so to speak.

**Dave Jones:** Here is again this is much much thicker. Look at this right but it does still fit in the case. So yeah and I think I'll put up the rating of these two units.

**Dave Jones:** I think one's like 28 29 dB something like that at the full like 3000 full RPM. So we're not going to get the full RPM at a lower voltage but yeah even this bigger fatter one just has enough room to fit.

**Dave Jones:** So if you see if I mount the uh the fat one we'll call it okay the fat Delta in there. Yeah we can't screw into the existing things but look it's it's just there's just enough clearance on the heat sink here and it's not quite it's not absolutely perfectly centered.

**Dave Jones:** Let's just see if at the same like 8 volt nominal 8 volt output if this one is actually just lower noise. Just some simple bench test here at 8 volts taking 70 milliamps here.

**Dave Jones:** I've got the fat Delta. Sure that's not next to the heat sink other obstacles but that I'm like I can hear it but jeez it's low. Okay I've got my microphone actually pointed towards it.

**Dave Jones:** There's not really any air flow there to disturb the mic. So that's a reference shut up and you'll get a reference for this fat Delta. There's the original Rygo one and I got to admit it's probably the same, I would say.

**Dave Jones:** Yes, I think as you'd expect, it's generating extra noise by like just the airflow being next to all these fins on here, and maybe some radiation, you know, some vibrational noise coming through as well because it's vibrating, but it's not much difference, but the thing is this thing, I think it's going to give greater airflow.

**Dave Jones:** It'd be tricky to set up airflow measurement stuff for this sort of thing, but we could potentially actually run this at a lower voltage anyway, but it still remains to be seen.

**Dave Jones:** The proof is when you put it in the unit itself and actually put the back on. That takes the same current, by the way. And that's the slim Delta one, and yeah, you definitely don't want to use that one.

**Dave Jones:** That is noticeably louder than the other two. Wow. And it is drawing significantly more current, too. So, maybe it's just going faster. I mean, they're all going to have different characteristics, some RPM for a given voltage.

**Dave Jones:** All right, I got some double-sided tape on that, so that fits. Very slim double-sided tape, so hopefully it still it still actually fits in here. Okay, only one way to find out.

**Dave Jones:** Let's power it up. Ah. No, it just got caught. So, yeah, no, it must be touching. It's probably the double-sided tape. There we go. Ah. No, that's pretty whiny.

**Dave Jones:** I'd say potentially more whiny when it's next to the fins there, so I don't think that even if that fits, it's not going to deaden it, so wah wah wah wah.

**Dave Jones:** I think. But anyway, as I said, uh increased air flow, I believe. So, we could uh potentially drop that voltage down and run to slower speed. Aha, I just noticed that there's some raised bits in here.

**Dave Jones:** Look at this. Um that are right over the fan. Uh bugger. So, I reckon if I shave those down, can cut them off with a pair of side cutters, I guess.

**Dave Jones:** Don't have to Dremel it and get all medieval on its ass. Um Yeah, I reckon we can uh make room for that. Nothing you can't fix with a pair of side cutters.

**Dave Jones:** No wuckers. And sure enough, that fits and works. Just shave off some part of the parts up the top. Here, it's not directly in the center. Um but right off the bat, I can tell you that is louder than the original, unfortunately.

**Dave Jones:** But, at the same voltage. Once again, I think the air flow is significantly higher. All right, I went to a lot of effort to find my anemometer. You won't believe where I found it.

**Dave Jones:** Here's a photo of it. Um yeah. Anyway, okay, so I'm going to do some crude measurements here. I've got the uh fat Delta in here um a blaring away.

**Dave Jones:** And for some reason, this stupid thing won't let me change it to like meters per second or whatever. It's kilometers an hour. Anyway, there you go. So, I put it like directly over the fan there just to get sort of like the inlet um you know, whatever vortex thing is happening, whatever flow is happening there.

**Dave Jones:** Anyway, I'm just going to put it into some street strategic locations for comparison. So, yeah, 31 kilometers an hour. Does that change if we Yeah, that's uh Oh, actually, that really changes a lot.

**Dave Jones:** That really You have to get it You have to get it right over the top. That is sensitive, isn't it? Okay. No, that's that's that's fairly repeatable, though. 31, okay.

**Dave Jones:** Can we get anything at all down there? I've got it right up against the end stop here, the foot. So, 1.3. Oh, I killed it. Luckily, I ordered two of them.

**Dave Jones:** Yeah, no, I think I'm going to have to really you need to hold this in place. So, I think I'm going to have to go to the effort to just drill a couple of small mounting holes in there cuz it's the same angles and everything.

**Dave Jones:** It's just that the mounting holes are off. So, yeah, I think I'm going to have to go to that effort. Okay, I've put the original fan back in and you can see roughly the same, isn't it?

**Dave Jones:** But, regardless of what I do, I can't get any airflow out the bottom here. Nothing. So, uh yeah, I don't know. Inlet is kind of like similar, but I don't know.

**Dave Jones:** There's too much variability in this sort of test. All right, I've got the Delta skinny in there and yeah, we're getting about 35. So, that's technically the highest out of them, but it is the loudest because for a given well, doing an extra RPM, it's just it's just noisy.

**Dave Jones:** There we go. I'm able to get it. Yeah, one one 1.2 So, 1.3. So, that seems to be the bestest fan, but you'd expect that cuz it I think it's uh operating at a higher RPM.

**Dave Jones:** Yeah, I found a much better metric. Just stand it up vertically, sit the anemometer on top, and 3.3 3.4 3.5 km/h. This is with the Delta skinny. This is the original fan.

**Dave Jones:** 2.7 km/h. So, yeah, it's the noise kind of is proportional to the amount of air flow pretty much. All right, I've got the fat Delta in there. I've actually screwed it down.

**Dave Jones:** I just cut down rather than drill the holes in the little arms. I just cut them down until it just like fitted on the ends and then the screws are sort of holding that in.

**Dave Jones:** And I've screwed the case in. So it does actually it does actually fit. Although this is the one blade missing jobby still so it's probably a bit louder than what it should be.

**Dave Jones:** Keep it. Talking 3.2 there. So yeah, we can we can drop that. We can drop the voltage on that so I can put my replacement good good fan fat Delta in there.

**Dave Jones:** I can drop it. Oh jeez, you can feel the wobble. You can feel the imbalance the the vibration. Oh my god, I wonder if we can pick that up.

**Dave Jones:** I don't think we're going to be able to pick that up on the microphonics of the input capacitor. I mean that's that's really down in the noise there. So I doubt it.

**Dave Jones:** I'm not going to go to the bother of that FFT that. All right, let's just crudely experiment here. I've got the fat Delta in here the one with the all the blades this time.

**Dave Jones:** So yeah, we're getting 3.0 I saw 3.6 before 3.5 thereabouts. So we're feeding that. Let's just try whacking a 100 ohm in series. That does make it quieter. Really changes the whine.

**Dave Jones:** You're probably not hearing that but we're dropping down to uh 2.2 2.1 now two two it's going to go under is it? Yeah. Yeah, 1.8. Yeah, it's just it's not much anymore, is it?

**Dave Jones:** Whether or not that's enough air flow you'd have to do thermal test but that I mean noise is still there but it's not really as annoying as the original.

**Dave Jones:** Yeah, I don't think you'd want to go below that. Like if we go to 200, we're probably Are we going to Are we going to stop the thing? No.

**Dave Jones:** No, it's still going. Barely. Barely. Barely. Oh god, it's halved. Yeah. Yeah, nah. I think that's that's not going to do the business uh at all. But anyway, we can put that back to zero, and we can adjust the voltage somewhere between 4 and 5, maybe 4 and 1/2 there is where we had it before.

**Dave Jones:** Well, I can tell by the airflow, really. So, we're on two at the moment. 1.9. So, you know, if if you drop the eight down to say five, um then yeah, you're you're pretty much on target.

**Dave Jones:** So, just below five there or thereabouts. Anyway, five is significant. I'm going to put my mic close to that, and uh this is at eight volts, and we'll lower that.

**Dave Jones:** There you go, that's at five. And that's at eight. It's quite a significant difference. So, what's left to do? I guess is I'm probably going to stick my probe back up its clacker, and uh just see what uh the temperature gets, uh cuz I do have a reference in that video I uploaded uh the other week.

**Dave Jones:** But in any case, I certainly wouldn't call that like silent. It's definitely a lot better, but probably not you know, I mean, a lot of people want, you know, like, "Oh, I want a silent fan." And I just don't think you're going to get that with these um just these small-ass fans like this.

**Dave Jones:** I think you're going to have to go for the 100 mm jobby on the back. And then yeah, it will be completely silent, but you know, it changes the form factor a bit on the back.

**Dave Jones:** And uh then if you want to mount the VESA mount as well, then um like a VESA arm on the thing, then yeah, it becomes a bit troublesome, but yeah, possible.

**Dave Jones:** All right, I'm doing the same test I did uh last time. Got uh two thermal uh probes in here. One's 41.5, the other's 42.1. We were getting uh 39.5 before.

**Dave Jones:** So, we're getting a couple of degrees C increase. Uh the ambient temp according to my aircon is the same as 25 degrees uh C in here. So, this is at uh 5 V there.

**Dave Jones:** So, I've had it on for like an hour. I could leave it on longer, but I think it's probably thermally equalized uh now. So, yeah, what we're talking 2.5 degrees, maybe 2 degrees C increase, which is not a lot from dropping it um from 8 V down to 5 V drive.

**Dave Jones:** So, it's certainly possible. And that is with the fat uh Delta fan. I don't think you're going to get the same noise with that uh little skinny uh Delta jobby.

**Dave Jones:** So, yeah, um you just have to uh mounting's a little bit dodgy. I mean, but I managed to uh just cut off the ends of uh these here. And um yeah, so cut them to the right length and the screws just like go over the uh ends of that.

**Dave Jones:** So, that should be good enough for Australia. And I you could potentially glue it down, but that would eventually come off uh with the vibration, I think. Um double-sided tape, I probably not going to get stuff thin enough cuz it's a real tight fit in there, I think.

**Dave Jones:** Anyway, you might be able to uh get away with that. So, you're only going to get a couple of degrees C increase there, but it's working. Um so, yeah, I wouldn't have a problem with a couple of degrees C increase, so it looks like it's possible you can, you know, lower and change the spectrum of the fan noise by putting in that fat delta jobbie.
