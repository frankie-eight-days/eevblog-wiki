---
video_id: HLmty8KcOd4
title: EEVblog 1743 - Mechanical Vibration Detection with your Oscilloscope Probe
url: https://www.youtube.com/watch?v=HLmty8KcOd4
source: youtube-asr
---

**Dave Jones:** Hi, I want to show you something interesting with oscilloscope probes, but before we get to that, we're going to have a look at multi-layer ceramic capacitors, MLCCs. You've seen these before. They come in all shapes and sizes. I've got rather

**Dave Jones:** large ones here for a reason today. I've actually done quite a few videos. I'll link them in on multi-layer ceramic capacitors and what's called the piezoelectric effect with these capacitors where if you vibrate your board, like if you're got a capacitor in a physical

**Dave Jones:** product on a rigid PCB and it's vibrating, then that can actually generate a voltage across the capacitor. It's actually used as a piezoelectric microphone, basically. And this is a very well-known phenomenon and I've also done videos on where the MLCCs, they can

**Dave Jones:** actually crack internally and they can fail open circuit or short circuit and you've seen the magic smoke escaping uh previous videos. So, I'll link those in if you haven't seen them. The piezoelectric effect of ceramic capacitors actually works in both

**Dave Jones:** directions. Not only can it pick up vibrations, it can actually vibrate itself if you put a specific frequency on it and there's a physical mode how it's attached to the PCB and everything else. It's very dynamic thing. Doesn't happen all

**Dave Jones:** the time, but it can happen and I've demonstrated that in a previous video as well. And this is known as the singing capacitor phenomenon and you can actually hear um sometimes in rare circumstances, but it it does happen.

**Dave Jones:** You can actually hear ceramic capacitors actually emit a high-frequency sound. And other things that don't use the piezoelectric effect like inductors, wire wound inductors for example, they can also if you drive them at a certain resonant frequency that happens to meet

**Dave Jones:** up with the mechanical vibrational mode of the component and the PCB and the mounting system and everything else, then you can actually get um that high-frequency noise you might have heard from switching power supplies for example. And it can come from inductors,

**Dave Jones:** it can come from physical trans laminated transformers as well. So, we're going to look at multi-layer ceramic capacitors today, but we're also going to take a look at this bad boy which I will do a dedicated video on.

**Dave Jones:** Look at this. Thank you very much Cry Sound for sending this in. I'll link in they've got a Kickstarter for this. This is an acoustic imaging camera. So, it's got a little optical camera, but it's also got an array of microphones and it

**Dave Jones:** can pick up sounds from 2 kHz to 65 kHz and then map it over the actual image. And I'm actually driving a bunch of ceramic capacitors in parallel cuz I was trying to find capacitors that would actually do this. And

**Dave Jones:** Murphy's Law wasn't that good, but I'm going to be able to show you something today which is really cool. So, I'm driving that at 11.1 kHz, 20 V peak to peak. And if we put the acoustic imaging camera on there and I shut the hell up,

**Dave Jones:** this is our frequency spectrum here. Now, I'll be quiet and watch that dot. Those capacitors are actually emitting a sound. And I'll move it and we'll see if it follows it.

**Dave Jones:** It does. It's not massively accurate in in terms of positional, but it works. You can see that those capacitors are singing and you can see these very spikes in the frequency window there. We can change our frequency window. So, I've got it on a

**Dave Jones:** tripod now and you can see it. It's identified that middle capacitor there as emitting that sound and if we move it, you can see it does does a reasonable job of tracking that. Considering that I can't actually hear

**Dave Jones:** that, it's actually remarkable that it can do that. It can hear that capacitor emitting. It's really something. You can see it on the frequency spike there. You might have noticed that the peak is actually at about 22 kHz. It's actually

**Dave Jones:** double the frequency. So, it's actually a harmonic of the frequency that we're driving it at. Because we're driving it with a square wave. Now, watch what happens with this frequency here if I sweep it from 2 kHz to 20 kHz. Watch this.

**Dave Jones:** The spot's going to jump around. You'll notice those peaks are sweeping. That was a 30-second time period. I'll lower that. Okay, I've now got a 10-second sweep. Look at that.

**Dave Jones:** Cool, huh? And you can see those harmonics extend right up into the high frequencies as well. So, anyway, that's a cool bit of kit. I'll definitely do a future video, like a more detailed video on that, but I'll

**Dave Jones:** link the Kickstarter down below. It's awesome. I cannot hear that, but it the microphone array can pick that up. I am super impressed. >> [bell] >> So, that's really cool, but what I want to show you today is that you can use a

**Dave Jones:** times 10 oscilloscope probe. This one's a switchable one times one times 10 like this. Oops. And I've done videos on this before. These contain a certain multi-layer ceramic capacitor in them which, as we've seen, can be used as

**Dave Jones:** like a microphone. So, if I tap that, I've got that single shot captured and bang on the bench, we're actually picking up that signal. Look how massive it is. And as I've shown in many previous videos as well, it the same

**Dave Jones:** thing also happens to the front end of amplifiers. They have the ceramic capacitor. So, if I go like that, bang. Look at that massive spike in there. All oscilloscopes are susceptible to it. So, you can actually use your times 10

**Dave Jones:** oscilloscope probe as a poor man's acoustic imager, so to speak. It's not really It doesn't do a full image, but like a spot checker. And we're going to actually put this on here and we're going to have a look at trying to pick

**Dave Jones:** up the vibration signal from coming from that ceramic capacitor. Let's give it a go. But, of course, we want to shield it because well, we're just picking up right we're we're just picking up that what is it? 11.1 kHz signal there. So,

**Dave Jones:** I've got my trusty little shorting plug here which will allow us to boom short that out hope hopefully if it makes bloody contact. And yeah, we're not picking that up anymore. Cool bananas. So, we can actually use this

**Dave Jones:** probe to actually pick up the vibrational mode of this PCB here. So, it's shielded. It's not capacitively picking up this, but let's see if I can place the probe on there and get this to work. Whoa, hello. We've got something small.

**Dave Jones:** Trigger's not set. Trigger's not set. What have we got? We've got Look at that. Look at that. It's picking it up at 11 kHz, 11.1 kHz, exactly what we've got set over here. And that's picking up the vibrational component of that not just

**Dave Jones:** the capacitor, but the entire structure of the PCB it's mounted on. And I experimented with quite a few different ones here and you know, it was hard to actually get a good one. Bloody Murphy's Law. But isn't that cool? You can actually use your

**Dave Jones:** oscilloscope probe as like a poor man's vibrational probe. And if we change frequency, we can see that I'm I'm lowering that and you can see that that is going to actually change based on the frequency. Isn't that cool?

**Dave Jones:** >> [laughter] >> You can actually pick up vibrational modes of PCBs with your times 10 oscilloscope probe. Love it. Neat little hack. Definitely give that a go yourself. Of course, you've got to short the input. It's you know, cuz otherwise,

**Dave Jones:** if we take that damn thing off and then we capacitively, you know, it's just going to capacitively couple that whatever signal we've got in our PCB like all day long. So, yeah, don't want to do that. But yeah, short it out.

**Dave Jones:** Bob's your uncle. So, I hope you like that little tip. Definitely give it a try with your own times 10 oscilloscope probe, especially on like switch mode power supplies and stuff like that. Take safety into account, of course. Don't go

**Dave Jones:** just touching stuff, especially if it's mains, you know, switch mode power supply. So, have a probe around. I'm here all week cuz it's a probe except you're not electrically probing it. You're mechanically probing it. How cool is that? Anyway, if you like that little

**Dave Jones:** tip and found it useful, give it a big thumbs up. As always, discuss down below. Catch you next time.

**Dave Jones:** >> [music]
