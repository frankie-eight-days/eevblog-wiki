---
video_id: vwAhHz7Zpzk
title: Guest Video - Karl Adams - Audio Distortion Measurement
url: https://www.youtube.com/watch?v=vwAhHz7Zpzk
source: youtube-asr
timestamps: {"0": 0, "1": 10, "2": 21, "3": 34, "4": 45, "5": 62, "6": 73, "7": 89, "8": 108, "9": 121, "10": 139, "11": 169, "12": 185, "13": 202, "14": 226, "15": 241, "16": 261, "17": 278, "18": 297, "19": 307, "20": 322, "21": 333, "22": 344, "23": 362, "24": 380, "25": 404, "26": 421, "27": 436, "28": 454, "29": 470, "30": 486, "31": 500, "32": 515, "33": 536, "34": 569, "35": 587, "36": 598, "37": 622, "38": 643, "39": 655}
---

**Dave Jones:** Good day. I'm Carl Adams, and I'm here because of Dave's incredible generosity in sharing this channel with folks like me. So, if you're not familiar with my channel and its content, audio is my thing.

**Dave Jones:** Do a lot of audio projects. I'm a bit of a nostalgia tragic. Um you'll see that in my choice of test equipment. And I've got the sort of leaning towards analog techniques that you'd expect from someone whose day job is as a software engineer.

**Dave Jones:** So, enjoy. So, today I thought I'd I'd look at some techniques for measuring distortion in audio amplifier. Um particularly techniques for trying to measure very low levels of distortion.

**Dave Jones:** Um I've got a little project underway. The amplifier based on the um LM8375, but um in a compound configuration um with it inside the feedback loop of another op amp.

**Dave Jones:** Um which promises to give some impressively uh good distortion numbers. But that then is challenging to measure on an instrument um like the uh 3562A, uh which has 75, maybe 80 dB dynamic range tops.

**Dave Jones:** So, I was going to experiment with using an old-fashioned analog distortion meter as a a notch filter, basically, as the front end prior to uh putting the signal into the uh DSA.

**Dave Jones:** Let's give it a go. So, one of the issues with trying to do um accurate distortion measurements on an instrument like the 3562A is that we can't really use the internal source uh of the 3562A because it's not quite clean enough for our purposes.

**Dave Jones:** So, what I've gone with is uh this little unit here, which it looks like I made it myself, but truth is I didn't. I actually bought the board off uh eBay um a few years ago from a chap in Latvia, I believe, um who made some very fine um oscillator boards.

**Dave Jones:** Um I forget exactly um how good the um performance in terms of distortion these things are supposed to have, but uh uh there's a lot of zeros involved, I know that much.

**Dave Jones:** So, it's certainly going to be uh better than our ability to measure, so um that should be fine. And just as a initial test, I've just uh led that straight into the 3562A to see whether we can see any trace of any harmonics at all.

**Dave Jones:** So, we're doing a um harmonic distortion measurement of our source um just straight into the 3562A and we're covering a frequency span from 100 Hz to 5.1 K. And uh we've set the fundamental to 996 Hz because that's what our source is actually putting out uh as we need to make sure that the analyzer does actually correctly identify the harmonics.

**Dave Jones:** But uh even uh with some averaging on pretty much all of the harmonics are right down there in the grass. There's There's basically nothing to be seen there. So, we're seeing 86 87 dB.

**Dave Jones:** Uh basically, that's just the limitation of the instrument. Um we're not able to measure really any harmonics at all. So, I'm going to try something a little different. So, what we've done here is we've now led the output of our source into the distortion meter.

**Dave Jones:** So, this is a uh Leader brand distortion meter from the mid-1980s, I would believe. Um I previously actually had the model before this, the LDM-170, which uh unfortunately didn't have the the automatic uh nulling mode that this one does.

**Dave Jones:** And certainly trying to use that in its originally intended purpose was most frustrating as uh attempting to get the notch filter properly nulled and keep it that way was very tricky indeed.

**Dave Jones:** Anyway, so our output is going to be approximately 1 volt RMS and we enter level setting mode and we'll just adjust the level set to try and get that Try and do that without sticking your head in front of the camera probably would be good.

**Dave Jones:** There we go. Okay. So, we now have uh the level set and we can start adjusting. This is actually pretty good. So, um frequency is set pretty close where it should be.

**Dave Jones:** It's 10 * 100 around about 1 kHz and we can just tweak the balance the It's probably quite close. I often use this at a similar sort of frequency, so we can start making our way down the line.

**Dave Jones:** It's looking pretty good. Fine frequency adjustment's not really changing anything at that point. We should probably leave it alone. There we go. Just playing with the coarse balance at that point.

**Dave Jones:** I just touch that and see if that can get better. Oh, can it what? There we go. Okay, that's good. Keep making your way down. Uh-huh. Dare I touch the coarse adjustment?

**Dave Jones:** Yeah, we're still good. Oh, look at that. Now, this I don't really want to try touching that now, I don't think. We'll try that one. Not really doing anything.

**Dave Jones:** All right, let's go to there. And that's in manual mode. I don't want to start out in auto. See if I can do any better. Now, that's right at the limit anyway.

**Dave Jones:** I don't like. Oh. All right. Oh, and I've made it worse. Here we go. Uh yeah. Oh. Probably shouldn't touch that, but we'll go near it. See what happens.

**Dave Jones:** Oh, that's good. All right, here we go. Yeah, looks good. All right, now I'll whack it in auto. Okay. So, we're currently um in a mode where uh 1% distortion is uh full scale.

**Dave Jones:** So, if you're not familiar with these instruments, basically they're um a notch filter um followed by um amplifier and an AC millivolt meter. Um So, basically anything that's left over um after the notch filter is considered to be uh the THD plus N.

**Dave Jones:** Um Now, the thing about this is that the limiting factor for these things is always the depth of the notch. Um So, I mean, this thing's best measurement range is 0.1% full scale.

**Dave Jones:** Um and I think it's um .015 or something like that is about the minimum reading you'll ever get off of it. Um but that's not because it's .015% distortion um inside the machine.

**Dave Jones:** Simply that it cannot suppress the fundamental any more than that. Now, with our dynamic signal analyzer, our limiting factor there is that it has um a 14-bit analog-to-digital converter.

**Dave Jones:** So, although the the DSA has uh enormous dynamic range in terms of being able to deal with input signals of different magnitudes, in terms of dealing with uh signals uh that are occurring at the same time, uh it's limited by the number of bits in the ADC.

**Dave Jones:** So, that's the reason why we can't measure vanishingly small amounts of distortion. However, because we have output terminals on here, we can actually look at the signal that's coming after the notch filter.

**Dave Jones:** So, by using this notch filter to remove um the by far the largest part of the the input signal, uh we can make the uh the job of the DSA much easier.

**Dave Jones:** Not only that, because the uh the DSA allows us to not just uh measure the um the THD um in terms of measuring the harmonics in proportion to the fundamental, it also has a mode that can measure harmonic power.

**Dave Jones:** And by using that mode instead, we can actually uh directly read um THD in conjunction uh with the uh the settings here. So, Okay. So, we're currently in the minus 40 dB range.

**Dave Jones:** So, we would expect that uh full scale, which is 1 V RMS, uh would correspond to minus 40 dB. Now, if we now just flick the lights out and have a look at what's happening on the display on the signal analyzer, you'll see that we are getting a harmonic power of minus 66.6.7 dB.

**Dave Jones:** So, what we need to do is take another 40 dB from that. So, that's around about minus 106.7. In this case we're measuring THD over the first first five harmonics.

**Dave Jones:** Just we're just looking at a small part of the spectrum there. We could look a little bit further but it doesn't really matter. I just wanted that to be nice and clear on the screen.

**Dave Jones:** As you can see the noise floor starts to rise so we do have some issues there. You might think with a um a device that can measure down to minus 80 dB notch filtering into a device that can also measure down minus 80 dB that you'd get some whiz-bang minus 160 dB of dynamic range but it doesn't work that way.

**Dave Jones:** The noise floor and probably the residual distortion the analog distortion meter start to rear their ugly head. Nevertheless, we're we're looking um much more deeply into the uh the distortion spectrum of our source and that's looking quite promising.

**Dave Jones:** So I think that illustrates how we could perform the same thing on our device under test. I hope you enjoyed this little demonstration how with some inexpensive equipment and a bit of imagination you can improve your distortion measurements by about a factor of 10.

**Dave Jones:** Thanks for watching.
