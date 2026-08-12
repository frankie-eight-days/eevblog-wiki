---
video_id: VTHcxTst_RA
title: Rohde & Schwarz MXO3 3 Phase Power Measurement
url: https://www.youtube.com/watch?v=VTHcxTst_RA
source: youtube-asr
---

**Dave Jones:** All right, I'm here at the Rohde & Schwarz stand, and we've got a pretty impressive demo set up with the new MXO 3 series, the eight-channel jobbie. And I'm here with Tristan. You've seen Tristan on the channel before from Rohde

**Dave Jones:** & Schwarz. He's going to give us a demo. >> Yes. >> Tell us what we've got here. >> So, what we've got here is the new 3000 series, our little baby with eight channels. So, for a lot of scoping the

**Dave Jones:** market, you see only four channels. And now we have a eight channels that perfectly fit into a lot of power customer for motor drive, AI data center, that they require different power rail testing using more than a eight-channel scope. Okay? So,

**Dave Jones:** this setup is a BLDC motor from MXP with a gate driver. So, what it does is actually it's taking in a um 240, convert to 10 12-V DC, and the gate driver will actually do a PWM to regulate a AC to drive the motor. Okay?

**Dave Jones:** So, yep, um it's pretty messy when you see this screen, but uh we can look at the the eight channel. So, for most of the power customer, so when they look at a three-phase measurement, it's going to fill up the

**Dave Jones:** screen with a lot of waveform, current measurement, and some calculation to get the best accuracy that you want. Okay? So, yep, this is what you you can see from the bottom. We have all the channel. We can actually drag and drop

**Dave Jones:** Okay, each channel to show you phase one. So, this phase is coming from our single phase, the A phase, which is the PWM voltage plus the the channel two current. Okay? Manually, you can actually move all these to different grid, which our scope

**Dave Jones:** allows customer to play around with this very smart high-resolution display. Okay? I can actually bring this reading visually.

**Dave Jones:** Okay? >> That's a bit tricky. >> Yeah. There we go. You [laughter] know Yeah. >> That's better. >> Yeah. I just want to fit them into the same screen. Okay. So, we have all the channels.

**Dave Jones:** And when you want to perform measurements, you can actually look at every individual channel by manually going to our measurements that you add amplitude. You can add cycle to cycle RMS. Okay? You can add all the individual channels

**Dave Jones:** onto our oscilloscope. Think about when you want to do power as well, you have to multiply the phase. Okay? But now, Rohde & Schwarz have come up with this K 133 or K333 options. And this is our new

**Dave Jones:** apps on the three-phase power. Okay? And we can add in power quality or harmonics. And what this does is okay, it can provide you with a quick quick measurements for this three-phase motor. Okay? And when I get this activated, you

**Dave Jones:** see them onto the screen. >> Is is that three-phase module available on all the series scopes? >> That is correct. This is a new options that we have complete on our MXO series 345. Okay? And this allows you to look at all

**Dave Jones:** the three-phase measurement. And the bottom part you get to see the frequency. Okay? And we can tweak this to optimize all the crest factor, active factor, as well. As a scope, you know, we do have 1 to probably 4% error. Okay? The way to

**Dave Jones:** improve this cycle-to-cycle measurement, okay, first you need to find out, you know, where are we triggering it. So, the frequency on the PWM are pretty messy. Okay? I can change my trigger. I can look at my current because my current channel on channel

**Dave Jones:** two. Okay, which is this green area here. Okay, it's still fluctuating. I can use my digital trigger to increase my hysteresis.

**Dave Jones:** Okay, we can put in absolute or relative where we increase the um the sensitivity.

**Dave Jones:** Which you're going to see from here. So, this is our hysteresis that you can see from here and I can bring it up, okay, to get a much more stable trigger on I on my three-phase power. So, that's

**Dave Jones:** one part to stabilize my three-phase measurement. And next step is uh when I go into my power we can go deep dive into the setup. Okay? So, you can actually look at the fundamental frequency. So, we need to be close to the

**Dave Jones:** fundamental in order to get a good crest factor measurement or power factor. So, you can look at the the hertz. And Australia is actually 50 hertz. I can select my fundamental frequency to 50. Okay, that will improve all the

**Dave Jones:** measurement. And um when I go to my sources, okay, we do support not only the three-wire measurement, we support two wires as well. You can have a four-wire a four-channel to look at two-wire measurement. The this uh uh BLDC motor that we have doesn't

**Dave Jones:** have a neutral. So, by default we have selected a three-volt neutral three amp. Okay, all I need to do is switch this over to this configuration. Three current and three voltage on each phases. Okay, that will help us to

**Dave Jones:** optimize the three-phase measurement. And when we go further down the configuration yeah, you are able to change the channel. So, for my setup I I put it as phase one voltage current on channel one and two. Channel three and four will be phase

**Dave Jones:** two. This will assign our channel for the power calculation. So, we have a uniform bandwidth filter as well. For most power customer, you don't have you probably do not require 500 MHz in order to increase the sensitivity or the

**Dave Jones:** range. Okay, we can actually bring it down to Yeah, this is around 20 MHz. You can see that my frequency cycle is around 45 Hz. So, this 20 MHz will be good enough that I can apply a filters to all my channels.

**Dave Jones:** Okay. And we can actually select the cycle source. Cycle source is important as well. When you look at measurement, we do want to capture and calculate based on cycle by cycle RMS value. Okay, rather than having this free run that we

**Dave Jones:** do not know where to get where to measure our power. Okay, we can use this to select like channel two. Channel two is a current waveform which is like running around 30 40 Hz. I can apply another cut-off frequency.

**Dave Jones:** Okay, this is a low-pass filter that I can actually use this to filter maybe up to 100 kHz.

**Dave Jones:** Okay, this will help you guys to improve the measurement. And most of our customer that wants to on power power efficiency is important these days. You know, we are looking at more than 80% or 90 95% data center EV power

**Dave Jones:** converters. And we can actually use these to work with our We have another sister company called ZES Zima. So, this is a German company that produce power quality analyzer. So, that accuracy go down to 0.025 or better. Okay? You can

**Dave Jones:** use this to correlate to the efficiency based on the IEEE or ANSI standard. Okay? The last bit is once I optimize everything, we get a very stable measurement. We get to see the phase value as well. We do have these um

**Dave Jones:** extra features that we can actually bring out the uh Yep, the vector plot. >> Oh, very nice. >> Yep. So, you can have a vector plot that coincide with the power power waveform. Okay? So, this is a new features that we

**Dave Jones:** put up. There's another features that if you want to look at power harmonics, we have built in the power harmonics as well. Yep, compare we can see a lot of power harmonics because of the bandwidth that we can extend out to 1 gig

**Dave Jones:** bandwidth. >> And that vector plot is part of the app. It's part of the >> You are correct. >> power app. >> Vector plots, the power waveform, the entire setup is actually part of the 223 options. >> Very cool.

**Dave Jones:** >> Yep. >> And we didn't point out that the MXO 3 series starts at 100 MHz. So, as as you can see, if you if you don't need the bandwidth, which you usually don't for these sort of motor

**Dave Jones:** applications, then 100 meg you can get your eight channels. >> Yes. >> So, what's the starting price of the eight channel 100 meg? >> So, if I look at the Australian dollars, you know, you you can get one with you know,

**Dave Jones:** without probes and options around $10,000. Because this is one of our entry level for performance oscilloscope. And for most customer who want to get a complete power package, it can it can actually add in all these option and probes. And

**Dave Jones:** typically, we looking around like 50K or slightly more. >> Excellent. So, these are the wideband with current probes. These are 100 MHz current probes. Yep. And high voltage differential probe. >> Yep. We have three sets of high voltage

**Dave Jones:** differential probe. And then we have three of the current clamp as well. They are all from Rohde & Schwarz. >> Excellent. Thank you very much, Tristan.
