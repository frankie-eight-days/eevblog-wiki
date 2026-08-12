---
video_id: fvTfBwRzpdo
title: EEVblog #1109 - Spectrum Analyser Design Walk-through
url: https://www.youtube.com/watch?v=fvTfBwRzpdo
source: youtube-asr
timestamps: {"0": 13, "1": 23, "2": 36, "3": 51, "4": 68, "5": 82, "6": 96, "7": 111, "8": 124, "9": 137, "10": 150, "11": 160, "12": 175, "13": 191, "14": 207, "15": 220, "16": 233, "17": 243, "18": 256, "19": 267, "20": 280, "21": 294, "22": 308, "23": 322, "24": 334, "25": 347, "26": 360, "27": 373, "28": 390, "29": 403, "30": 417, "31": 430, "32": 447, "33": 457, "34": 473, "35": 485, "36": 499, "37": 514, "38": 529, "39": 544, "40": 559, "41": 571, "42": 587, "43": 598, "44": 612, "45": 623, "46": 640, "47": 654, "48": 666, "49": 680, "50": 695, "51": 710, "52": 721, "53": 738, "54": 754, "55": 769, "56": 786, "57": 801, "58": 815, "59": 831, "60": 846, "61": 861, "62": 877, "63": 893, "64": 907, "65": 919, "66": 934, "67": 949, "68": 963, "69": 980, "70": 996, "71": 1011, "72": 1025, "73": 1039, "74": 1053, "75": 1066, "76": 1080, "77": 1094, "78": 1108, "79": 1127, "80": 1146, "81": 1163, "82": 1182, "83": 1194, "84": 1205, "85": 1221, "86": 1239, "87": 1258, "88": 1273, "89": 1287, "90": 1301, "91": 1317, "92": 1334, "93": 1354, "94": 1370, "95": 1384, "96": 1399, "97": 1416, "98": 1428, "99": 1443, "100": 1456, "101": 1470, "102": 1482, "103": 1494, "104": 1507}
---

**Dave Jones:** So, let's take a detailed look at the main board here, and uh we're only going to be concerned with the top side here because if you have a look at the bottom side here, there's just nothing of interest there. It's just all passives,

**Dave Jones:** bypassing, and some regulation, maybe things like that. So, nothing special at all. Now, it might look daunting at first with all these distributed element filters and everything else, but as we've seen before, you can see that's pretty much a modular block approach,

**Dave Jones:** and I've done a handy little overlay here that will uh attempt to hopefully explain all the different functional blocks and the signal flow on the board. So, let's get to it. So, let's start by taking a look at the RF input in the top left corner.

**Dave Jones:** This section here, of course, contains the 50-ohm input impedance, but that little SOT23-6 package, you'll see four of these here. These are actually single-pole double-throw switches, so they can actually switch in the 50-ohm load and various other stuff. So, we'll

**Dave Jones:** go to a higher-res photo for this and then zoom in on the RF section here, and we can see that the input is AC coupled there through C10, and then that goes into U1, which is a 955C as all the other ones here, these

**Dave Jones:** SOT23-6 parts there, some form of single-pole double-throw switch, which I can't find the data sheet for. If I can, I'll link it in down below. But, you can see that one side of the switch there, I believe pin one there, switches in

**Dave Jones:** C9 and R1, which is the 50-ohm load there. So, it's not a permanent 50-ohm load input. And you'll notice that there's actually four diodes unpopulated there, so there's a distinct lack of input protection here. So, unless there's something inside that little

**Dave Jones:** wimpy U1 switch there, there's, you know, not much here at all. There's basically nothing on the other side. There is a tiny little diode D7 there, but jeez, it's wimpy. And if we scroll down here, we've got a couple of

**Dave Jones:** more of these uh switches here. And there's some diodes, four diodes there. So, I'm not exactly sure what's uh doing there, but that looks like some uh power supply clamping protection there. At least they start to have something now.

**Dave Jones:** And if we have a look at uh pin one of U2 there, you can see that there's a controlled impedance uh trace coming into that. Obviously, this is an input path where they can switch in some sort of uh you know, a system test signal,

**Dave Jones:** something like that. I I don't know where that comes from, what that would be, maybe part of the self-test or or calibration or something like that. So, yeah, that's coming from somewhere. But normally, that wouldn't be part of the

**Dave Jones:** measurement system. Just allows them to switch stuff in. And a bit further down here, you can see that uh VR1 there, it's got 20 written on it. And that's a 20 dB uh attenuator there. And you can see that's basically switching in uh C16

**Dave Jones:** that uh that straight controlled impedance line there. So, it's basically it's selecting either straight through or a 20 dB attenuator here. Next up, we go down into a HMC. Once again, Hittite, they're everywhere. They've got the entire solution for this thing. Uh the

**Dave Jones:** HMC307. And this is the digital attenuator. So, when you go into the spectrum analyzer and you set the input attenuation, you can set it in 1 dB steps um up to uh 31 dB over and above the 20 dB input

**Dave Jones:** attenuator. And that's exactly what this chip does. So, the software is limited by the capabilities of this chip. But yeah, nice device. DC to 4 gig. DC to daylight. And I really like the way the designers have laid out this chip. Look at this,

**Dave Jones:** there's the input pin, and then there's the uh two ground pins right there. So, you can see all that uh via stitching to separate the input and output. So, there's no uh coupling there. And then the pin below that is the output. So,

**Dave Jones:** from a layout point of view, it allows you to lay it out with a minimum amount of coupling. Nice. But, we're not done with our input section yet. If we scroll down a little bit more, we'll see uh the

**Dave Jones:** signal flow down into our next section, which is of course the preamp. This thing has, I believe it's a 10 dB uh preamp gain on it. Once again, selectable, so we expect to see the digital switches there, and that's

**Dave Jones:** exactly what we get. So, I can either bypass the uh preamp or switch in the preamp. But, in this case, you'll notice that the switches are bigger. They're a different package, and we can actually get the data sheet. Surprise, surprise,

**Dave Jones:** it's another Hittite uh part. It's a single pole double throw. Uh it's a non-reflective switch up DC to not quite daylight this time, 3.5 gig. Uh it's a non-reflective switch. You can see the internal diagram there. It's actually

**Dave Jones:** got internal 50 ohm uh termination resistors in there. But, uh basically, it's just a switch. It allows us to say they use a combination of two of them. You can switch in your preamp or switch it out. Easy. Now, that's all bread and

**Dave Jones:** butter stuff, but look at all these other blocks in here, and this is the complex operation of a spectrum analyzer. Not all spectrum analyzers operate the same, uh but they use very similar uh techniques. So, what we're going to do is take a look at

**Dave Jones:** a basic uh block diagram here. So, we've looked at basically just one block here, the RF input attenuator in near the signal input there, and that includes the switching and the preamp and everything else. Now, we expect to see a

**Dave Jones:** low-pass filter in here, and that's what we'll see in a second. And then, that goes into a mixer, which then uh uses a local oscillator, mixes the two signals together, generates a higher frequency called the intermediate frequency, and

**Dave Jones:** then we expect to see a gain stage there. There's that gray uh uh amplifier block there. Uh attenuator, we won't see this in this one, but it doesn't matter. Um that IF then goes into an IF filter. We'll definitely see

**Dave Jones:** that, and then goes into a log amp and envelope detector, video filter, and display, but that's not quite how this one works. We need to look at another block diagram for that. And as it says here, most spectrum

**Dave Jones:** analyzers use two or four mixing steps to reach the final intermediate frequency that we can then in this case all do all digital processing and actually display that cuz this is an all digital IF system instead of a

**Dave Jones:** traditional analog spectrum analyzer. Anyway, so this we're going to see several steps here. By the way, these diagrams come from the Keysight application note AN 150. I'll link it in down below. Highly recommend it's one of the best reads on how spectrum analyzers

**Dave Jones:** work and everything else. So we expect to see in well in this case what we're going to see is two local oscillators. The first one goes in the first mixer and then the second one that goes into the second mixer here. If we take a look

**Dave Jones:** at the first mixer on the left-hand side there, that's the green circle with the X there, we need this because we need to generate a higher frequency than our frequency range of interest. In this case, our spectrum analyzer can go up to

**Dave Jones:** 3.2 gig. So we have to generate an intermediate frequency higher than that because if we don't do that, then there will be dead bands within the measurement window that just won't work. So we have to actually mix that with a

**Dave Jones:** high mix our input frequency with a higher frequency to generate an intermediate frequency above our maximum 3.2 gig input range. And if we go back to our original block diagram here, what we expect after our input stuff is a low-pass filter and

**Dave Jones:** then a mixer with a local oscillator feeding into that mixer. Do we get that? Well, let's take a look. Yes, of course we do. You can see the preamp there on the left that we looked at before. It

**Dave Jones:** then feeds into a down into that uh low-pass filter, which is again a distributed element uh filter there with the various L's and C's, and then that goes into a mixer IC there, which then uh accepts the signal from above it

**Dave Jones:** there from that nice-looking uh bowtie distributed element low-pass filter, and that will come from the local oscillator, as we'll see. But, it's a bit more complex. It's not like the local oscillator feeds straight in. We're doing some tricks with our local

**Dave Jones:** oscillator in this particular case. But, anyway, the output from the mixer then goes into that uh amplifier gain stage, as we saw on the block diagram. And, if we take a look at a high-res photo of the mixer and that uh amplifier IF

**Dave Jones:** amplifier uh stage, once again, we've got two Hittite parts yet again, the uh HMC488 mixer there on the left and the HMC716 uh amplifier. Let's take a look at the data sheets. And, this mixer can go from 4 to 7 gig, which is exactly what we

**Dave Jones:** want. It's above our operational uh frequency range of our amplifier. And, if we have a look at uh the specs here, then our uh intermediate uh frequency range DC to 2.5 gig. And then, our IF amplifier chip, the HMC716,

**Dave Jones:** it's exactly what you expect. It's a In this case, it's an 18 dB gain uh amplifier, but it's got uh the bandwidth of 3.1 to 3.9 gig. So, it's designed to operate within that range, which is above basically our 3.2 gig maximum

**Dave Jones:** operational frequency range, and that's where our IF frequency is going to sit somewhere above 3.2 gig. The exact value uh we don't actually know unless we do more investigation or some measurements. But, before we follow that intermediate frequency out, we want to see our local

**Dave Jones:** oscillator, cuz as I said before, it wasn't as simple as just a local oscillator feeding into the mixer as it shows on the uh block diagrams for spectrum analyzers. So, if we zoom in here, we can find our uh first local

**Dave Jones:** oscillator our main uh voltage-controlled oscillator. And, this one uses a Z-Comm uh part there for the VCO, the voltage controlled oscillator, and which is the big metal can there, and another Hittite PLL there to form our local oscillator.

**Dave Jones:** Now, this is made by a company called Z Communications, and they make a ton of different variants of these with different ranges and things like that. And this one is going to cover the frequency range that we need. If you

**Dave Jones:** have a look at the tuning voltage here, it goes from 1,800 to 4,200 MHz, or 1.8 to 4.2 gig. It's pretty much exactly the range we need here. And this is our sweep generator we saw in the block

**Dave Jones:** diagram on the bottom left there. The red sweep generator feeds into the local oscillator, and then feeds into the mixer. But, as I said, there's a few more steps after our local oscillator before we get to the mixer in this

**Dave Jones:** particular analyzer. But, as part of that local oscillator, we've got a Hittite HMC703 fractional synthesizer, which forms part of the ultimate PLL local oscillator loop. And we can see that here. If we take a look at the demo board you can actually get for this

**Dave Jones:** chip, it shows that there's a VCO integrated as part of the system here, in this case a Hittite HMC508. But, in the case of the Siglent spectrum analyzer here, we're using a VCO from Z Communications. And if you believe the

**Dave Jones:** sales blurb here, check it out. This platform has the best phase noise and spurious performance in the industry. Yes, thank you very much. But, once again, you know, decent choice has been made here to enable a pretty decent

**Dave Jones:** performance at a low price point. Well done, Siglent. But, even with all that magic, the output of the first main local oscillator here is not high enough in frequency. So, it goes into a frequency doubler there, and this is

**Dave Jones:** designed for a two two to four gig input, so doubles that anywhere from four up to eight gig. But, once again, the exact bandwidth frequency range we're talking about here, we don't exactly know unless we did further investigations or measurement. And the

**Dave Jones:** frequency doubler being used again, a Hittite HMC189 here, 2 to 4 gig input as I said, so 4 to 8 gig output. Uh it's designed for exactly this job. And this particular part isn't obsolete. Unlike uh if you

**Dave Jones:** were very keen you would have noticed uh plastered over the data sheets for a couple of chips before, we would have seen that they're actually obsolete. So, yeah, why they're still using them but I don't know. Maybe there's nothing better

**Dave Jones:** at the price point. But we're not done yet. No siree Bob. The output of the frequency doubler here for our local oscillator uh goes into uh two single-pole double-throw switches which then can select one of three band-pass filters. In this case uh the this

**Dave Jones:** particular uh physical arrangement and the distributed element uh filter is called an interdigital band-pass filter. So, three different frequencies. You can actually see that they're different uh geometries there which actually selects the bandwidth and the response. And then

**Dave Jones:** there's three uh single-pole double-throw switches on the other side. So, the software can select one of three band-pass filters on our local oscillator. And these switches are different to what we've seen before. These are uh VSWAT2-63 blah blah blah blah blah. And these are

**Dave Jones:** about high isolation absorptive uh single-pole double-throw switches with integrated CMOS drivers and all sorts of weird and wonderful stuff. And we don't care about the quiescent current really. Um and 500 uh to 6 500 meg to 6 gig uh

**Dave Jones:** bandwidth. Pretty decent. And we're almost there. I've mentioned this before. You can see the output of that um one that selectable band-pass filter there then uh goes through just a little bit more stuff there and goes through another uh bow-tie low-pass filter. It's

**Dave Jones:** called a bow-tie low-pass filter because it looks like a bow bow That's where it gets its uh name from and then that finally goes into the mixer. So, that block diagram we saw before and you see for all spectrum analyzers, the local

**Dave Jones:** oscillator goes straight into the mixer. Well, as you've seen, it's a bit more complicated than that for various performance reasons. But, if you're keen eye, you would have noticed something in between there, the output from the interdigital filter after the switching

**Dave Jones:** and uh probably some little buffering there or something. Uh then goes into this odd-looking arrangement here on the board, which is coupling um the signal to go over, if you follow the trace on the other side. It's coupling over to go up to the tracking

**Dave Jones:** generator local oscillator SMA connector and that jumps on over to the uh tracking generator module we saw before. So, finally out of our mixer and then through our IF gain stage, which we've looked at, uh we expect to find an IF

**Dave Jones:** filter and well, you betcha. Look at the output of the amp the 18 dB IF amplifier down here. Bingo, it goes into another bandpass filter, another interdigital uh type. Once again, different geometry in there uh to give you a different uh

**Dave Jones:** range and response of the thing. And then that's followed by another uh cute-looking bow tie uh low-pass filter as well. Once again, just to take the upper edge off something. And if you're curious about how these interdigital uh bandpass filters

**Dave Jones:** actually work, when you can clearly see that both uh like the input signal comes in and then it basically goes down to ground with a trace sticking up and then the other then the trace on the right-hand side next to that uh goes up

**Dave Jones:** to ground at the top side and then the next one goes down to uh ground. So, how does this actually work? Well, it's because we're at high frequencies here. These work at, you know, several hundred megahertz up to, you know, several

**Dave Jones:** gigahertz or something like that. They're basically uh a coupled resonators, but they're also known as interdigitated coupled resonators. So, yeah, they resonate between the two, and then it propagates along and resonates. And that's why you might see different

**Dave Jones:** spacing in there is to give a different passband characteristic for this thing. Anyway, you have to get into real complex RF microstrip type theory to, you know, figure out exactly how this works. And there's a ton of math into it. And I'm

**Dave Jones:** sure you could Google really interested. But yeah, even though it goes down to ground there, it gets through. But we said here before that uh this particular spectrum analyzer arrangement uses uh two mixing uh techniques. And so, we

**Dave Jones:** need to find that second mixer and the second local oscillator as well. And if we pan across here, bingo, the output of our filter there goes into another mixer uh the 422 488 exactly as we had before. But just like on the block diagram here,

**Dave Jones:** you'll notice that the output of the second mixer is a much lower frequency. It's within way under, way within uh the passband of our spectrum analyzer in this block diagram, 322 MHz. But in the case of uh this particular one here,

**Dave Jones:** it's actually at 810 MHz. And the reason we know that is because, hey, look, we can look at the um filters on the output of the mixer, and we can see that there are SAW filters or surface acoustic wave filters. And we

**Dave Jones:** can have a look at the data sheet for this particular uh one. They're available in all different frequencies. This one happens to be an 810 MHz SAW filter. So, we know that's the output uh frequency of the second mixer.

**Dave Jones:** But this isn't low enough uh frequency for now us to do digital IF uh sampling on. So, what we want to do is feed it into another third mixer, just like what's uh shown here, to actually down-convert it to a frequency that we a

**Dave Jones:** baseband frequency that we can actually sample with like a Joe Blog's uh you know, 16-bit analog-to-digital converter. And we can see that here, the output of the saw filter goes into this little white block here, which is a

**Dave Jones:** Mini-Circuits. Yes, we finally get a Mini-Circuits win in the design here. It's not all Hittite. Mi- Mini-Circuits one of the biggest uh providers of uh these sorts of uh mixers. And so, this will go in and we can take a look at the

**Dave Jones:** data sheet for this Mini-Circuits mixer as well. But, there's nothing terribly exciting to see here. It's just a you know, basically 5 MHz to 1 gig mixer designed for this sort of uh application. Uh down-conversion uh to a

**Dave Jones:** baseband signal. But, wait. We're not finished with the mixer. Every mixer's got to have a local oscillator input. Where's that coming from? Well, it it is coming from the second local oscillator, but we need a much lower frequency. So,

**Dave Jones:** you'll notice that the second local oscillator here uh as like feeding the second mixer across to the left there, it also goes up and that same signal feeds a uh is divided by four and then that gets fed into the third mixer,

**Dave Jones:** which does the down-conversion. So, we've got our final RF uh frequency bandwidth here and this goes into a curiously a single-pole four-throw switch and that's what the IC is. So, I'm not exactly sure what it's selecting there. You know, there's

**Dave Jones:** some sort of different uh filtering options that it's doing there. I'm not exactly sure what. Anyway, that then goes over into another single-pole four-throw switch here, which has only half the stuff populated. So, that's quite unusual. Why did they leave that

**Dave Jones:** out? Now, as a user by the name of uh Goozu, if I'm pronouncing that correctly on the EEVblog forum postulated for this one. It I It certainly looks like another band pass filter in there with inductors and the caps in there. And that would be

**Dave Jones:** one of going into presumably one of the channels of U85 on the left-hand side there the single pole full throw switch and presumably there would be a software option for this to have another additional band pass filter on the final IF before it goes into the

**Dave Jones:** sampler. So, maybe there's even a secret menu option for it if you could hack the firmware or whatever. Or maybe, you know, they had an early version of firmware they decided they didn't want it. I don't know. It could still be

**Dave Jones:** there. Who knows? Could be interesting. But, yeah, I don't know. If you could find it, you might be able to hack in your own band pass filter in there for some additional functionality. And the good thing about an experimental hack

**Dave Jones:** like that is that you're not really, you know, damaging anything. You're populating existing footprints in there with an existing digital switch that's only affected if you enable a software option in the firmware to actually flick that switch and in, you know, put that

**Dave Jones:** filter in series with the final IF there. So, you know, you can play around if your heart's content without really risking damaging anything. So, that's it. We're finally through our complete block diagram here. But, this envelope detector, we don't have that cuz as I said before,

**Dave Jones:** this uh spectrum analyzer uses what's called an all-digital IF filter. So, it does everything after the IF stage, the intermediate frequency stage. It just samples that directly with a high resolution high sample rate analog-to-digital converter and then does everything in software. As we see

**Dave Jones:** in this Keysight application note here, here is how the Keysight X-Series signal analyzers do an all-digital IF. They've got an ADC in there with a gain and the alias filter, everything else. But, it goes into then a custom IC, which in this

**Dave Jones:** case would be that uh, Spartan-6 FPGA we saw is doing a Hilbert transform and then it's doing some filtering and then it can do the video bandwidth in there and does logs and powers and all sorts of and uh, the detector, all sorts of

**Dave Jones:** stuff, all within side uh, that'll be happening inside that Spartan-6 FPGA, no doubt. And then that goes into the pro and probably it'll be doing the FFT in there as well. Um, and then that just goes out to the display applications

**Dave Jones:** processor, which we saw earlier. So, now we have to go full circle right back to the main PCB under that uh, block where we found our main reference oscillator before. And what do we find? Surprise, surprise, an ADC driver

**Dave Jones:** designed specifically for IF baseband processing. In this case, it's the uh, National Semiconductor, not this Texas Instruments rubbish, LMH 6517. It's designed exactly for this for a 16-bit ADC. And there's the block diagram down the bottom. So, no

**Dave Jones:** surprises to find what's down below this. I'll give you a one guess. And congratulations, you win a brass razoo. It's an analog-to-digital converter. It's the Analog Devices uh, AD9235. Actually, 12-bit, surprise, surprise. Not this 16-bit rubbish, I guess. For

**Dave Jones:** Siglent, no. 12-bit will do the job just fine. And uh, yeah, it's designed for ultrasound equipment or low-cost digital oscilloscopes. There we go. Winner, winner, chicken dinner. And you'll notice that we've got the uh, dash 40 part there, uh, which it means

**Dave Jones:** 40 megasamples per second. This part's available from 20 up to 65 megasamples per second. So, at 40 megasamples per second, we know that our uh, IF baseband frequency has to be somewhere below 20 cuz you know, all that Nyquist stuff,

**Dave Jones:** really annoying. Yeah, so it's got to be at at most half of that sample rate. So, I hope you enjoyed that sort of building block walk-through of a spectrum analyzer, in this case the Siglent SSA 3000. I did do this video a couple of

**Dave Jones:** years back, but it was embedded in the teardown, and it was a new style of edit I wanted to try where I took my high-res photos and actually then just in my editor actually did the voice commentary with my mic here, and

**Dave Jones:** do that over the top and then, you know, zoom in and pan and do all that sort of stuff. So, that was I was quite proud of that, and it was kind of like, you know, just tucked away in this

**Dave Jones:** teardown. So, I thought I'd just take that out and move it on over to a separate video, and I've got a new monitor setup here I just wanted to try edit some video. So, I hope you found that useful. And if you like that style

**Dave Jones:** of teardown video, please let me know. It does take bit more work than just my usual thing where I just literally like opened up and I stand behind the camera, I've got my little poker in there, and I just

**Dave Jones:** like poke at stuff and then, you know, zoom. Basically, the zoom in I do is zoom in on the camera or changing the macro lens or whatever, and just, you know, waffling on. Just press record and figure out something to say. I do the

**Dave Jones:** same thing here. It's not like I have a script or anything. It's I still do sort of like the off-the-cuff commentary and stuff like that, but it's done at the editing stage, which is a different style of video to what I

**Dave Jones:** normally do. So, anyway, if you liked it, please give it a big thumbs up. Let me know down below. I won't do this kind of style of video for all teardowns, cuz sometimes it's not appropriate. Sometimes it's just

**Dave Jones:** easier and quicker to do it just standing behind the camera and just do it off the cuff just poking, you know, straight at the thing. This is still off the cuff, but it requires a lot more editing magic, and I'm not really the

**Dave Jones:** world's best editor, but hey, it worked, I think. Anyway, catch you next time.
