---
video_id: zoyaHOqp9gI
title: Rigol DHO800 Oscilloscope Fan Upgrade Experiment
url: https://www.youtube.com/watch?v=zoyaHOqp9gI
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 36, "3": 52, "4": 65, "5": 79, "6": 93, "7": 108, "8": 124, "9": 140, "10": 156, "11": 171, "12": 183, "13": 200, "14": 216, "15": 229, "16": 242, "17": 260, "18": 275, "19": 286, "20": 296, "21": 309, "22": 328, "23": 344, "24": 364, "25": 377, "26": 393, "27": 407, "28": 419, "29": 430, "30": 450, "31": 465, "32": 484, "33": 495, "34": 514, "35": 531, "36": 549, "37": 568, "38": 589, "39": 599, "40": 614, "41": 626, "42": 638, "43": 654, "44": 667, "45": 685, "46": 699, "47": 717, "48": 729, "49": 750, "50": 759, "51": 778, "52": 790, "53": 805, "54": 817, "55": 829, "56": 844, "57": 857, "58": 876, "59": 888, "60": 899, "61": 912, "62": 924}
---

**Dave Jones:** Hi, just a quick video looking at a potential fan upgrade for the Rigol DHO800 and 900 series scope cuz there's a lot of talk about the fan noise which might annoy some people. It's you know, you can hear it. Anyway, this is the fan

**Dave Jones:** that's used inside here. It's a tiny little thing and I thought basically 45 mm diameter frameless jobby very common on GP like old school GPUs and stuff like that. Anyway, and I've already done a second channel video on

**Dave Jones:** basically you need a fan on this thing. It'll overheat and it'll shut down even in room temperature like lab temperature things here. Anyway, I've got two Delta fans of course top quality fans. You can get the I got these off

**Dave Jones:** Digikey and they have them in stock. So let's have a squiz. So I'll put the model numbers and links down below for these but basically two different ones. This one's slightly bigger than this one. They're all 12 volt fans as is this

**Dave Jones:** one but as you saw in the previous thermal testing video on this this was running at 8 volts. I think it was. So they're actually derating that fan just to get it a bit quieter cuz they don't need the full

**Dave Jones:** air flow afforded by the 12 volts on there. These are both three wire jobbies but we can just use the two wire and ignore the taco output. Both of these do seem to physically fit but let's have a

**Dave Jones:** look. This is the nearest one is you can see that the fan blades are a bit thicker on this Delta one. So yeah, and and they're a bit more vertical. These are like it is a slimmer Oh, no, the overall thickness is

**Dave Jones:** basically the same there but the Delta actually has a bigger more vertical fan. So it's going to get I would presume greater air flow for a given a uh you know for a nominal RPM. So yeah, very similar but unfortunately

**Dave Jones:** they are this tri mount but they don't have it's hard to show you there but the footprints don't quite line up like that. The holes don't line up. The Delta ones the holes are further apart like that and both Delta fans I think have

**Dave Jones:** yep they've got the same pin out so to speak. Here is again this is much much thicker. Look at this right but it does still fit in the case. So yeah and I think I'll put up the rating

**Dave Jones:** of these two units. I think one's like 28 29 dB something like that at the full like 3000 full RPM. So we're not going to get the full RPM at a lower voltage but yeah even this bigger fatter one just has

**Dave Jones:** enough room to fit. So if you see if I mount the uh the fat one we'll call it okay the fat Delta in there. Yeah we can't screw into the existing things but look it's it's just there's just enough

**Dave Jones:** clearance on the heat sink here and it's not quite it's not absolutely perfectly centered. Let's just see if at the same like 8 volt nominal 8 volt output if this one is actually just lower noise. Just some simple bench test here at 8

**Dave Jones:** volts taking 70 milliamps here. I've got the fat Delta. Sure that's not next to the heat sink other obstacles but that I'm like I can hear it but jeez it's low. Okay I've got my microphone actually pointed towards it. There's not

**Dave Jones:** really any air flow there to disturb the mic. So that's a reference shut up and you'll get a reference for this fat Delta.

**Dave Jones:** There's the original Rygo one and I got to admit it's probably the same, I would say.

**Dave Jones:** Yes, I think as you'd expect, it's generating extra noise by like just the airflow being next to all these fins on here, and maybe some radiation, you know, some vibrational noise coming through as well because it's vibrating, but

**Dave Jones:** it's not much difference, but the thing is this thing, I think it's going to give greater airflow. It'd be tricky to set up airflow measurement stuff for this sort of thing, but we could potentially actually run this at a lower voltage anyway, but

**Dave Jones:** it still remains to be seen. The proof is when you put it in the unit itself and actually put the back on. That takes the same current, by the way. And that's the slim Delta one, and yeah, you

**Dave Jones:** definitely don't want to use that one. That is noticeably louder than the other two. Wow.

**Dave Jones:** And it is drawing significantly more current, too. So, maybe it's just going faster. I mean, they're all going to have different characteristics, some RPM for a given voltage. All right, I got some double-sided tape on that, so that

**Dave Jones:** fits. Very slim double-sided tape, so hopefully it still it still actually fits in here. Okay, only one way to find out. Let's power it up. Ah. No, it just got caught. So, yeah, no, it must be touching. It's probably the double-sided tape.

**Dave Jones:** There we go. Ah. No, that's pretty whiny. I'd say potentially more whiny when it's next to the fins there, so I don't think that even if that fits, it's not going to deaden it, so wah wah wah wah.

**Dave Jones:** I think. But anyway, as I said, uh increased air flow, I believe. So, we could uh potentially drop that voltage down and run to slower speed. Aha, I just noticed that there's some raised bits in here. Look at this. Um that are right

**Dave Jones:** over the fan. Uh bugger. So, I reckon if I shave those down, can cut them off with a pair of side cutters, I guess. Don't have to Dremel it and get all medieval on its ass. Um Yeah, I reckon we can uh make

**Dave Jones:** room for that. Nothing you can't fix with a pair of side cutters. No wuckers. And sure enough, that fits and works. Just shave off some part of the parts up the top. Here, it's not directly in the center. Um but right off the bat, I can

**Dave Jones:** tell you that is louder than the original, unfortunately. But, at the same voltage. Once again, I think the air flow is significantly higher. All right, I went to a lot of effort to find my anemometer. You won't believe where I

**Dave Jones:** found it. Here's a photo of it. Um yeah. Anyway, okay, so I'm going to do some crude measurements here. I've got the uh fat Delta in here um a blaring away. And for some reason, this stupid thing won't

**Dave Jones:** let me change it to like meters per second or whatever. It's kilometers an hour. Anyway, there you go. So, I put it like directly over the fan there just to get sort of like the inlet um you know,

**Dave Jones:** whatever vortex thing is happening, whatever flow is happening there. Anyway, I'm just going to put it into some street strategic locations for comparison. So, yeah, 31 kilometers an hour. Does that change if we Yeah, that's uh Oh, actually, that really changes a lot.

**Dave Jones:** That really You have to get it You have to get it right over the top. That is sensitive, isn't it? Okay. No, that's that's that's fairly repeatable, though. 31, okay. Can we get anything at all down there? I've got it

**Dave Jones:** right up against the end stop here, the foot. So, 1.3. Oh, I killed it. Luckily, I ordered two of them. Yeah, no, I think I'm going to have to really you need to hold this in place. So, I think I'm going to have to go to

**Dave Jones:** the effort to just drill a couple of small mounting holes in there cuz it's the same angles and everything. It's just that the mounting holes are off. So, yeah, I think I'm going to have to go to that

**Dave Jones:** effort. Okay, I've put the original fan back in and you can see roughly the same, isn't it? But, regardless of what I do, I can't get any airflow out the bottom here. Nothing. So, uh yeah, I don't know. Inlet is kind of

**Dave Jones:** like similar, but I don't know. There's too much variability in this sort of test. All right, I've got the Delta skinny in there and yeah, we're getting about 35. So, that's technically the highest out of them, but it is the loudest

**Dave Jones:** because for a given well, doing an extra RPM, it's just it's just noisy. There we go. I'm able to get it. Yeah, one one 1.2 So, 1.3. So, that seems to be the bestest fan, but you'd expect that

**Dave Jones:** cuz it I think it's uh operating at a higher RPM. Yeah, I found a much better metric. Just stand it up vertically, sit the anemometer on top, and 3.3 3.4 3.5 km/h. This is with the Delta skinny. This is the original fan.

**Dave Jones:** 2.7 km/h. So, yeah, it's the noise kind of is proportional to the amount of air flow pretty much. All right, I've got the fat Delta in there. I've actually screwed it down. I just cut down rather than drill the holes in the little arms.

**Dave Jones:** I just cut them down until it just like fitted on the ends and then the screws are sort of holding that in. And I've screwed the case in. So it does actually it does actually fit. Although this is

**Dave Jones:** the one blade missing jobby still so it's probably a bit louder than what it should be. Keep it. Talking 3.2 there. So yeah, we can we can drop that. We can drop the voltage on that so I can

**Dave Jones:** put my replacement good good fan fat Delta in there. I can drop it. Oh jeez, you can feel the wobble. You can feel the imbalance the the vibration. Oh my god, I wonder if we can pick that up.

**Dave Jones:** I don't think we're going to be able to pick that up on the microphonics of the input capacitor. I mean that's that's really down in the noise there. So I doubt it. I'm not going to go to the

**Dave Jones:** bother of that FFT that. All right, let's just crudely experiment here. I've got the fat Delta in here the one with the all the blades this time. So yeah, we're getting 3.0 I saw 3.6 before 3.5 thereabouts. So we're feeding that.

**Dave Jones:** Let's just try whacking a 100 ohm in series. That does make it quieter. Really changes the whine.

**Dave Jones:** You're probably not hearing that but we're dropping down to uh 2.2 2.1 now two two it's going to go under is it? Yeah. Yeah, 1.8. Yeah, it's just it's not much anymore, is it? Whether or not that's enough air

**Dave Jones:** flow you'd have to do thermal test but that I mean noise is still there but it's not really as annoying as the original. Yeah, I don't think you'd want to go below that. Like if we go to 200,

**Dave Jones:** we're probably Are we going to Are we going to stop the thing? No. No, it's still going. Barely. Barely. Barely. Oh god, it's halved. Yeah. Yeah, nah. I think that's that's not going to do the business uh at all. But anyway, we

**Dave Jones:** can put that back to zero, and we can adjust the voltage somewhere between 4 and 5, maybe 4 and 1/2 there is where we had it before. Well, I can tell by the airflow, really. So, we're on two

**Dave Jones:** at the moment. 1.9. So, you know, if if you drop the eight down to say five, um then yeah, you're you're pretty much on target. So, just below five there or thereabouts. Anyway, five is significant.

**Dave Jones:** I'm going to put my mic close to that, and uh this is at eight volts, and we'll lower that.

**Dave Jones:** There you go, that's at five. And that's at eight. It's quite a significant difference.

**Dave Jones:** So, what's left to do? I guess is I'm probably going to stick my probe back up its clacker, and uh just see what uh the temperature gets, uh cuz I do have a reference in that video I uploaded uh

**Dave Jones:** the other week. But in any case, I certainly wouldn't call that like silent. It's definitely a lot better, but probably not you know, I mean, a lot of people want, you know, like, "Oh, I want a silent fan." And I just don't

**Dave Jones:** think you're going to get that with these um just these small-ass fans like this. I think you're going to have to go for the 100 mm jobby on the back. And then yeah, it will be completely silent, but you know, it changes the form factor

**Dave Jones:** a bit on the back. And uh then if you want to mount the VESA mount as well, then um like a VESA arm on the thing, then yeah, it becomes a bit troublesome, but yeah, possible. All right, I'm doing

**Dave Jones:** the same test I did uh last time. Got uh two thermal uh probes in here. One's 41.5, the other's 42.1. We were getting uh 39.5 before. So, we're getting a couple of degrees C increase. Uh the ambient temp

**Dave Jones:** according to my aircon is the same as 25 degrees uh C in here. So, this is at uh 5 V there. So, I've had it on for like an hour. I could leave it on longer, but I think it's probably thermally

**Dave Jones:** equalized uh now. So, yeah, what we're talking 2.5 degrees, maybe 2 degrees C increase, which is not a lot from dropping it um from 8 V down to 5 V drive. So, it's certainly possible. And that is with the fat uh

**Dave Jones:** Delta fan. I don't think you're going to get the same noise with that uh little skinny uh Delta jobby. So, yeah, um you just have to uh mounting's a little bit dodgy. I mean, but I managed to uh just

**Dave Jones:** cut off the ends of uh these here. And um yeah, so cut them to the right length and the screws just like go over the uh ends of that. So, that should be good enough for Australia. And I you could

**Dave Jones:** potentially glue it down, but that would eventually come off uh with the vibration, I think. Um double-sided tape, I probably not going to get stuff thin enough cuz it's a real tight fit in there, I think. Anyway, you might be

**Dave Jones:** able to uh get away with that. So, you're only going to get a couple of degrees C increase there, but it's working. Um so, yeah, I wouldn't have a problem with a couple of degrees C increase, so it looks like

**Dave Jones:** it's possible you can, you know, lower and change the spectrum of the fan noise by putting in that fat delta jobbie.
