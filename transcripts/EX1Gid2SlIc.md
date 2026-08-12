---
video_id: EX1Gid2SlIc
title: EEVblog 1607 - PSU Switching Noise Reduction via Vibration
url: https://www.youtube.com/watch?v=EX1Gid2SlIc
source: youtube-asr
timestamps: {"0": 0, "1": 16, "2": 28, "3": 49, "4": 65, "5": 80, "6": 100, "7": 111, "8": 129, "9": 146, "10": 158, "11": 172, "12": 186, "13": 196, "14": 222, "15": 234, "16": 252, "17": 268, "18": 282, "19": 299, "20": 314, "21": 336, "22": 350, "23": 368, "24": 379, "25": 394, "26": 410, "27": 421, "28": 433, "29": 445}
---

**Dave Jones:** Hi, just a quick but very interesting video showing you an interesting phenomenon here which came about cuz I was testing this little Alienware DP 100 power supply here. I'll link that in video if you haven't seen it down below.

**Dave Jones:** And while I was measuring the noise for this thing, it got me thinking about something that I read probably decades ago now and I can't find it, but please leave it in the comments down below if you have any

**Dave Jones:** reference to this. And this is where potentially physical vibration, hence why this thing's moving, physical vibration in switching components like multi-layer ceramic capacitors and your inductors and stuff like that can actually be impacted by physical vibration. And I

**Dave Jones:** read that you could potentially lower switching component noise by actually hitting a certain mechanical vibration or subharmonic of the vibration here. And you know I've done quite a few videos linked in up here and down below if you haven't seen them where I discuss

**Dave Jones:** the impact of shock and vibration on multi-layer ceramic capacitors and how capacitors can actually sing. It's a phenomenon in the industry called singing capacitors. And like and I've done videos on shock response of capacitors and stuff like that. So physical vibration can actually

**Dave Jones:** have a real impact. And I did an interesting video also linked this in where Tesla when they were developing their compute module for their AI you know learning systems, they actually had a very interesting MEMS oscillator that was impacted by nearby multi-layer

**Dave Jones:** ceramic capacitors in the switching power supply. So I'll link in that video down below. It physically broke them. It took them ages to figure out where the source of the problem was. Anyway, it's a very well-known effect where

**Dave Jones:** components like inductors and capacitors can actually be impacted by vibration. And you might have actually heard a power supply like a squeal, you know, like like this high-pitched squeal sound. That can come from the inductors and or capacitors in the power supply. So,

**Dave Jones:** anyway, I thought we'd look at the noise here. So, I've got my same setup as before. I'm high frequency probing my this output here, and I've got the output going over to my electronic load over here. I'm drawing 3 amps, but I'm also using my

**Dave Jones:** little vibration motor here, and you've seen this in previous videos where I'll link those in as well. Tons of videos linked in, AND I'VE GOT THAT going through this power amplifier up here, okay? So, I'm just actually driving this

**Dave Jones:** at the moment with the signal gen from the scope. I'm just driving at 8 1/2 hertz here, and you can see it physically vibrating, and I can Whoa, it's going to bottom out there. I don't want it to bottom out. So,

**Dave Jones:** lower that back down. But, let's see if we can actually find a sub resonant point. We won't be able to go to multiple resonances cuz the switching frequency of this is 246 kilohertz, right? So, you can see that

**Dave Jones:** there is the main switching frequency. So, this is at 3 amps here. Now, I'm going to see if I can actually wind up this frequency, and we'll see if we can get any impact on that at all. Get rid

**Dave Jones:** of that, and I'll adjust it here, and let's let's go. Okay. So, where are we? Whoa, 16 hertz. Nothing. Nothing. Nothing. Whoa. Is it going to survive? Nothing. Let's go up. Let's keep going. Let's go Whoa, whoa, whoa. Wait, hang

**Dave Jones:** on. My probe came out. Don't you hate that? That's what she said. Hang on, I'll tape that up. All right, there you go. Hopefully, that won't come out now. Now, also, I've got the peak-to-peak and the standard deviation. So, 110

**Dave Jones:** microvolts here and 2.5 millivolts peak there. That's so RMS noise and peak-to-peak. So, we're looking really it's probably going to be impacted more on the peak-to-peak aspect if this if we can actually get the resonant frequency for this or sub resonant frequency. So,

**Dave Jones:** I'm going to take that up. I'm going to wind that wick up. And so we're looking at 246 kHz. So, maybe at 200 something hertz perhaps. I don't know. I'm going to wind it up. Now, you won't fit. Trust

**Dave Jones:** me, that's vibrating. I'm not sure if you can even hear you probably can't hear that, but that is still Oh, yeah. Yeah, you should be able to hear that. Whoa, hello. Hello. I can hear that. Hear it? Actually, I'll turn my

**Dave Jones:** microphone around. So, there you go. I've got my microphone a bit closer now. Now, let's see if we can get near a harmonica this thing. So, 246 kHz. So, we're looking at about 2 50 something like that. And

**Dave Jones:** check that out. Look at that. Wow. And if we go above that No, no, it's back to it's back to normal. Wow, that's really bad. Okay, don't want to go higher than that. So, let's wind that wick back down again and

**Dave Jones:** see if we can reproduce that. Look at that. Wow. And around around about that 250 or so mark. So, there's way lower there. We're talking like 1.3 millivolts peak-to-peak there. That is really quite something. Wow.

**Dave Jones:** And if we lower it back down we get 180. And we don't seem to get it at the like 25 hertz or whatever, but at 250 Yeah, we don't seem to get it. Whoa, which Yeah, we don't seem to get it at like

**Dave Jones:** the 24 25 hertz mark. That's too much of a sub multiple. But anyway, you saw that around about 250. So, that is interesting, is it not? The physical vibration of this unit. But it has to do with the construction and it's like

**Dave Jones:** there's nothing wrong with this unit. I I think this will it'll happen but it depends on the specific components. So, it could happen on any design. Uh please leave it in the comments down below if you've actually uh seen experienced

**Dave Jones:** this. I've experienced the other way where physical vibration of the capacitors uh causes a problem or the inductors causes a problem elsewhere. Now, I've seen all sorts of vibration effects in electronics, but I've never seen it lower the system noise like

**Dave Jones:** that. And I don't really understand the exact mechanism behind this. So, I I don't know. I'm going to open it up. Leave it in the comments down below if you have any idea why it would lower system noise like that at a subharmonic

**Dave Jones:** multiple of the switching frequency. Cuz I'm at a bit of a loss to actually explain that. You saw saw it there. It did actually work. So, please leave it in the comments down below. It's an interesting phenomenon. You can lower

**Dave Jones:** your system noise when you're at a subharmonic frequency. I don't think it's going to work at the much higher frequency cuz you're not going to be able to vibrate at in the megahertz region, right? So, you're not going to

**Dave Jones:** be able to physically vibrate in the megahertz. But you can do it with a sub multiple and you saw it at 250 hertz. That dropped the system noise quite substantially. Anyway, if you enjoyed that video, please give it a big thumbs

**Dave Jones:** up. And as always, discuss down below. Fascinating, huh? Catch you next time.
