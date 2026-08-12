---
video_id: ESdqWYlLPbI
title: EEVblog #325 - Rigol DG4162 Voice
url: https://www.youtube.com/watch?v=ESdqWYlLPbI
source: youtube-asr
timestamps: {"0": 0, "1": 31, "2": 63, "3": 75, "4": 104, "5": 118, "6": 143, "7": 172, "8": 203, "9": 268, "10": 279, "11": 298, "12": 331, "13": 353, "14": 378, "15": 400, "16": 421, "17": 458, "18": 488, "19": 529, "20": 558, "21": 597, "22": 630, "23": 652, "24": 673}
---

**Dave Jones:** Hi. All right, I've had so many damn complaints about that I didn't test the voice arbitrary capability of this Rigol DG4162. Fine, here it is. I'll do a quick video. Geez, hope it keeps everyone happy. All right, if you didn't know in the arb capability here, if you go into arb and then you go into select waveform, it's one of the built-in waveforms. So, built-in, there's a whole bunch of them, but it's in the engine one, go figure.

**Dave Jones:** It's one of these ones over here. You can see the little dot. It's in there with, you know, Butterworth and Chebyshev and all that sort of stuff. So, let's go into voice and you've got a look, check this out, right? There's a select thing here on the second menu, but it's not on all the menu It's not on that menu. So, like, it's just it's stupid, really. So, you've got to like, you know, you press enter over here to select it, which is part of this menu,

**Dave Jones:** which is part of this numeric keypad here. It's just it's just stupid. I don't know. It It doesn't seem to make sense. Anyway, getting into a mini review rant here, but there it is. Select voice. Let's go back.

**Dave Jones:** And there's the waveform. That's pretty much exactly what it looks like. So, it looks like there's two syllables there at least and I I originally had it at 1 kHz. I just played it and well, I just looked at it on the scope first and of course, it was massively too fast. It was just, you know, it was repeating every, you know, every millisecond or something. So, it was just crazy. So, I've had to lower it down to 2 Hz here. Okay, 5 V peak-to-peak output. I've got it hooked

**Dave Jones:** up to my speaker here. Yes, it can drive an 8 ohm speaker directly. So, let's give it a go. Here we go. I found 2 Hz is roughly the optimal spot. Here Here go. I'll put my mic up to it.

**Dave Jones:** Remo Remo Remo Remo There you go. That's clearly saying Rigol or Rigol. You know, I I pronounce it Rigol, but Rigol, it's the voice is clearly saying Rigol, Rigol, Rigol. And I haven't figured out how to extend that.

**Dave Jones:** Like actually extend the pause between each one. Not even sure if it's possible. You might have to just go in and edit the arbitrary waveform itself to actually do that cuz it is annoying. It actually repeats too quickly. But there you go. It's saying Rigol. I'm pretty sure. Now, there's one annoying aspect with this is that the frequency selection. You'll notice that it's highlighted green there when, you know, you press frequency or you press amplitude, it highlights the other one.

**Dave Jones:** Not sure how good that looks on camera, but it looks good in real life. And you want to adjust the frequency. Fine. Okay, but look at which digit you're adjusting. There's that tiny little Once again, that stupid little yellow dot in there like they had for the waveform selection. I don't know what idiot thought that that was a good selection idea. And of course, if you move and if you use the buttons over here under the knob, it sure enough, it selects which digit you want. But look,

**Dave Jones:** it's just it's tiny. Tiny that little yellow dot. So, if I want to adjust, you know, in 100 mHz increments, there you go. That's fine. But yeah, it's just man, it's just Really, that's a horrible feature. I just tiny dot. Why not just, you know, make it a different color, highlight it red or, you know, something like that. I don't know. Anything but that silly yellow dot. And we'll play with the frequency just a little bit.

**Dave Jones:** So there you go. I think the you know, the optimum spots maybe you know, 2.2 2.3 hertz or something like that.

**Dave Jones:** And I'll try and edit that waveform to add in an extra pause after that. So let's go down to edit waveform here. I haven't tried this before so uh cycle period. Ah, here we go. So let's change the uh let's change the cycle period, shall we?

**Dave Jones:** Let's increase that to you know, a couple of seconds. And let's try that. So how do we save? There we go. Once again, you got to go down to another menu. So let's save it. Oh, here we go. We're saving it to the internal memory. Let's save it to How do you jump across? Oh man, trying to use this thing. Ah, there we go. It's obvious. Browser and we're in the directory thing. We need to go to file there. And once again, we got a little

**Dave Jones:** stupid blue dot this time. Crazy. Okay, let's save it in Oh, that's very laggy. I don't know. There we go. All right, save. I'm I'm to save it to arb one. Uh, file name. Geez. Do we care? Let's just call it one.

**Dave Jones:** Hello, I'm pressing uh, see, the enter button over there doesn't work. I've got to use the select button. Let's just call it that. That'll do. Saving arb wave data. Bang. We're in. Okay. So, now we should be able to recall this with a Let's have a look down here.

**Dave Jones:** Select waveform. Save stored waveforms. There we go. And then we can go in here to select the file read. Bang. I assume arb data have been changed. Okay, beautiful. Now it should output.

**Dave Jones:** No. All right. No, that's no good. We're obviously not we extended the whole thing. Clearly. That's no good. And for those who are curious to see the actual waveform, well, we'll single shot capture that and we'll zoom in.

**Dave Jones:** And there there is your waveform. It's very uh, it's very stepped, of course. It's like it's uh, it's like it's not even eight bit. It's very, very coarse. Look at that. Extremely coarse. What is that, you know, six bits or something? It's uh, it's pretty terrible. Seems like they've just used some, you know, computer crap computer generated voice to generate, you know, a a crude uh, wave file and then stick it in there as one of the arbitrary waveforms. They didn't even bother like sampling a real

**Dave Jones:** human voice in high fidelity, which this thing's capable of. What is it, 14 bits, um, you know, DAC in the thing? It's capable of, you know, extremely good voice reproduction. And a quick one for those who want to see the hardware counter capabilities. So, you switch on the hardware counter, which is weird to have a hardware frequency counter on a on a function gen like this. So, I've just got my scope probe hooked up to the back input and let's have a look.

**Dave Jones:** And there we go. Bang. It's um clearly got a clearly automatically selects a reciprocal counting function because it gives you the, you know, the huge number of decimal places, the huge resolution on low frequencies like that. So, it's doing reciprocal frequency counting. You know, on some older well, a lot of older frequency counters, you they either didn't have this capability at all or you had to manually select it, but it's clearly automatically knows that it's a low frequency. Bang, I need to use reciprocal counting. So,

**Dave Jones:** there you go. And there's it measuring a 1 kHz 1 V peak-to-peak sine wave from my Agilent 3000 series built-in waveform generator. And let me uh drop that frequency down a tad. Actually, I completely take that back. I think it's absolute because this reciprocal I don't think it's using reciprocal counting at all.

**Dave Jones:** It seemed to work okay at 50 Hz, seemed to be doing the business with a bit of noise, but I just I'm generating now 18, let's say 20 Hz on my Rigol sorry, my Agilent waveform gen 1 V peak-to-peak 20 Hz and it's just jumping all over the place, and it wouldn't do that if it was a true reciprocal uh frequency counter. And if I drop it lower in if I drop it lower like 12 hertz, it's completely stopped. It's just completely stopped updating. So, obviously, there is a lower frequency

**Dave Jones:** limit there, and all those digits are just complete really. It's not a true I assume it's not a true reciprocal frequency counter, because if it was, um then, you know, it'd be easily able to do, you know, 10 hertz or 1 hertz just as easily as it can do 50 hertz. And of course, you know, it tries to do 20 hertz, and bang, it's just it's just crap. Have to read the manual. No, there you go. I flew off the handle. I had to go in and change the gate time. So, you

**Dave Jones:** go into counter here, and well, you turn on the counter. Uh where was it? It was uh gate time here, and it didn't automatically adjust the gate time. So, now I'm feeding in my 24 hertz signal, and it's uh it's rock solid. So, let's uh turn it down to and it should update. There we go.

**Dave Jones:** All right. Much, much better. Much, much better. I like it. And I checked the manual, and yes, it uh goes down to uh a 100 microhertz or something like that. It's, you know, it can go and measure incredibly low uh frequencies. So, yeah, that was all uh just a red herring. Auto, here we go.

**Dave Jones:** Let's try auto. And the auto function didn't really work there, so I'm not sure what that's doing. Got to read the manual again, but uh I was able I'm able to measure 100 millihertz, no problems at all if I've got my uh gate time set slow enough. And there's the 50 hertz from my finger updating once per second. So, there we go. It's a bit better now than the high gate time we were using before.
