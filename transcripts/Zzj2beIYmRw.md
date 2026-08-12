---
video_id: Zzj2beIYmRw
title: CH7 Sydney 300W NEC TV Transmitter Teardown
url: https://www.youtube.com/watch?v=Zzj2beIYmRw
source: youtube-asr
timestamps: {"0": 0, "1": 12, "2": 31, "3": 45, "4": 58, "5": 70, "6": 84, "7": 106, "8": 116, "9": 132, "10": 147, "11": 161, "12": 174, "13": 185, "14": 200}
---

**Dave Jones:** future. Now, everyone loves teardowns on the EV blog and I got something special. Let's check it out. Woohoo! You might have seen this on a previous video, which I'll link in down below where I did the Channel 7 TV transmitter teardown.

**Dave Jones:** This is the 300 W amplifier that transmitted the analog TV signal in Sydney for about 20 years. This one 300 W as I said, this one was the preamplifier 300 W preamplifier for the video signal and also they used the same one might have even been this one for the audio.

**Dave Jones:** So, the audio went out at 300 W, the video went out at several hundred kilowatts. It's got a phase shift input here so that you can parallel these things up and tweak them for the same phase so that they load equally.

**Dave Jones:** But, there's just an input, output, and overload indicator. So, let's take a look inside this baby. And yes, we have the schematics. You ready for it? Oh, yeah. The RF aficionados are wetting their pants right now.

**Dave Jones:** Look at this thing. Oh, oh, I have to do a detailed teardown. This will be very short, but look at all the rigid coax lines here. Look at that little stargates inside.

**Dave Jones:** Look. Look little rigid coax penetrators. Here's the power supply. It operates off 28 V DC system supply. And let's take a look at the topology used in this thing, shall we?

**Dave Jones:** And I'll take you briefly through. Oh, by the way, I do have the schematic. I'll link it down below for those playing along at home. Now, the input signal comes in down here and it goes into a limiter circuit cuz you don't want some feeding in some input signal that then blows up your amplifier and a you know, a couple of million people in Sydney can't watch

**Dave Jones:** their TV signal. So, it just clips and limits the input signal so it doesn't damage anything else. And there's a phase adjust. Now, it goes into a circulator, which I'll uh shortly.

**Dave Jones:** And then there's a couple of preamplifier uh transistors over here. And then that leads up into another uh circulator, which then uh goes into two circulators uh which basically split the signal out like this into two separate channels.

**Dave Jones:** So, there's actually two power amplifiers in here, two complete separate stages like this. I believe they do this for redundancy. Um so, that if one blows, the other one still goes, and they can't affect each other.

**Dave Jones:** It recombines in a circulator and then comes out down here. That's tapped off for an overload indicator display like that. Beautiful. Now, I promised to briefly mention circulators. So, let's give that a go.

**Dave Jones:** Let's have a look at these circulators down here. What a circulator does, it's a passive device that uses ferrites, and it basically um does uh RF power protection. So, it basically circulates the power through to a dummy load here.

**Dave Jones:** So, if some idiot shorts the output of the antenna here, then what it will do is automatically dump all the energy into the load like this. The load is internal.

**Dave Jones:** Uh well, no, that's might be external. But it uh it dumps it into the load instead of blowing up your transistors over here. Very, very nice. And you can probably see the power resistors going to be under there near the output circulators for combining.

**Dave Jones:** There you go. That is very, very nice bit of kit, and I'll have to do a more detailed teardown on that. So, I hope you enjoyed that.
