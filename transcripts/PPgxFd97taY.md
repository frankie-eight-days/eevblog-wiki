---
video_id: PPgxFd97taY
title: EEVblog #652 - Oscilloscope & Function Generator Termination Demo
url: https://www.youtube.com/watch?v=PPgxFd97taY
source: youtube-asr
---

**Dave Jones:** Hi. Coincidentally, I've had two people recently contact me about a what is essentially the same problem to do with measuring things using coaxial cable like this. And the example was that they were trying to check the output signal

**Dave Jones:** level of their high-frequency function generator like this Rigol DG4162. It can go up to 160 megahertz. You know, a quite a nice function generator. And they're using their oscilloscope which had a better bandwidth than this, of course. In this

**Dave Jones:** case, it's the Rigol DS2000 series 200 megahertz. So, it's got enough bandwidth. Using a nice short piece of coaxial cable like this. You know, excellent capable of nice high performance RG58 coax. And they tried to measure the amplitude across the

**Dave Jones:** frequency. And look what happens. We'll start at 1 megahertz here, for example, and we'll notice that the peak-to-peak voltage over here is being displayed. And it's currently about 1.06 volts. And if we wind that frequency up 1 megahertz

**Dave Jones:** steps at a time here, then you'll see that it's, you know, it's pretty constant. We're at 28 megahertz now, but it's starting to drop a bit. 980 odd millivolts or thereabouts. And if we keep going up, we're back to a volt.

**Dave Jones:** Okay, you know, you don't expect it to be completely ruler flat over the frequency response, of course. And the specs will tell you that. But, if we keep going, for example, look. Now we're getting 960, 950. It's dropping. 920.

**Dave Jones:** Oh, look. We're under 900. What's going on here? Something strange at about 87 megahertz or thereabouts. 9 830. It's just Look. It's crazy. And if we go up in frequency, continue to go up 114 megahertz, our voltage is actually going

**Dave Jones:** back up. And it's going all over the place. And right up to 160 there. And you can see that if I sweep it quickly, it sort of goes it undulates up and down a little bit like that. Why is it so? And

**Dave Jones:** of course, you wouldn't expect there to be anything wrong here as well. If it was like loss from the coax cable, of course, if you look at the data sheet for a coax cable, you'll find that its loss does actually increase with

**Dave Jones:** frequency, of course, and fair enough. But in this case, we saw the signal actually like actually undulate go down and then undulate back up at a higher frequency. So, it wasn't like it was consistently rolling off or dropping in

**Dave Jones:** amplitude with frequency. So, there's something else at play here. And it gets even stranger. Let me show you something really weird. Look, I've got the same output here. I got a BNC T adapter here driving through exactly the same uh

**Dave Jones:** coax, exactly the same length. They're both RG58s going into both channels of our Rigol scope here. We're at 4 MHz, so a low frequency. And you can see that the two waveforms are identical there, okay? Now, watch what happens if we

**Dave Jones:** increase the frequency. Not only do we get that drastic drop again where but we're down to 600 and something millivolts now. By the way, I've been using that volts peak-to-peak. And the uh function gen should be stable 1 V peak-to-peak over

**Dave Jones:** the entire range. And you notice Look. Look at that. The signals are getting different. So, you can be forgiven for thinking that there's something wrong with the Rigol 2000 scope on that second channel, for example. But we're getting a whole bunch

**Dave Jones:** of issues here. We're getting output amplitude which seems to change over frequency. You expect it for a uh function gen. They're not ruler flat, but it It be nearly as much as what we saw there, not even close. Um and we're

**Dave Jones:** also getting amplitude differences between the two channels. Well, let's try another oscilloscope. Hopefully, we won't get any complaints about this one. 500 MHz Agilent 3000 series scope, an absolute beauty. Exactly the same setup. Both channels going in here. And as you

**Dave Jones:** can see, there we go. They're both the same amplitude. Let's wind the wick up and see what we get. Let's change the horizontal a bit there. 25 MHz. It's all looking good, but our amplitude has dropped to 600 mV

**Dave Jones:** peak-to-peak. That's way out of spec for this Rigol scope. Let's see if we get the amplitude difference between channels. We do. Look at that. Bingo. What's going on here? And look, we've just got two pieces of like pretty good performance

**Dave Jones:** coax. Coax should easily be able to do it. Short path or going in using BNCs. Everything's hunky-dory. And no, it has nothing to do with the 50-ohm output impedance mode, for example, here. Output impedance high impedance. No, look, makes no difference whatsoever, of

**Dave Jones:** course. So, what's going on here? So, pause the video and see if you can figure out what's going on here. I'll tell you after the break. Well, I hope you're able to figure it out. The answer is Well, the answer's

**Dave Jones:** actually really quite complex, but what it basically boils down to is the fact that this is the wrong technique for doing a simple measurement like this. You can't just use coax cable unterminated on the input here. And no, there's

**Dave Jones:** nothing wrong with this function generator. It is It meets its spec, and it is pretty ruler flat, you know, within 0.4 dB or something over the frequency range. To prove it, I'm going to disconnect my turn off channel two here. I'm going to

**Dave Jones:** use my Agilent 500 MHz probe here. We'll have to change the volts per division and I'm using a coax cable adapter on here like this. So, let's plug that in. Let's wind that up. And now amplitude, look, is gone

**Dave Jones:** back to 960 mV there. So, if we wind that over the right down, we're at 7 MHz now, right? So, we're looking at 1.06 V. So, if we now change it 1.07 18 MHz, we're still hovering around that 1 V mark and we're

**Dave Jones:** still within the spec I think it's about plus minus .1 V for a 1 V signal. 960, you know, it's not bad. It's going up 61 MHz. Everything, you know, 950 mV. So, it's gone back up to a volt. Okay, so

**Dave Jones:** it's certainly flat within that spec. A little bit over, maybe a small No, it's not. I think it's a you know, anyway, 160 MHz. As you can see, there was very little difference there. And that is the correct way to do

**Dave Jones:** it, not using an ordinary piece of coax like this. Well, you can, but you have to terminate them. Okay, to prove that, I'm back to my coax setup here. I'm going to set my input impedance to 50 ohms. And if your scope doesn't have

**Dave Jones:** that, you can just use a 50 ohm in-line terminator or or another T-piece like this with a 50 ohm terminator like that. Just hang it off it if you like. There we go. Both got 50 ohm inputs. So, let's

**Dave Jones:** now look at those. Okay, so we got both channels like that. That's at 1 MHz there. Okay, but of course we're going to be low in amplitude, okay, because we got the 50 ohm In fact, we're double 50

**Dave Jones:** ohm terminated here. So, normally it'll be half that 1 V that we're showing there. Or if we turn on our Where is it? Our 50 ohm output impedance. That just basically corrects the output amplitude on here so we can go to

**Dave Jones:** amplitude and we can go 1 V peak-to-peak and it ordinarily should give us 1 V peak-to-peak if we only had one output terminated like that and we do. There we go, 1 V peak-to-peak but because we're double terminating that,

**Dave Jones:** well, our amplitude's going to drop. But what I want to show you is the fact that uh this thing Here we go. Let's have a look. Okay, we've got both waveforms there. Okay, we've got 1 MHz. Let's wind the

**Dave Jones:** frequency up here and you'll notice that it's 675 mV and you'll notice that it's not going to change much and we're not going to see any of that amplitude difference between channels that we got before. There's a slight phase difference

**Dave Jones:** between channels. That's okay. But look, there's no amplitude difference as we go up like we saw before. So it's all about the terminate getting the correct termination when you're using these 50 ohm coax's and the reason we didn't get

**Dave Jones:** it when we were using this times 10 probe and I've done a video on oscilloscope probes before is because it's got that 9 meg input resistor there which effectively takes away the capacitance. Anyway, I won't go into the

**Dave Jones:** details but that is the correct method to use because it you don't need to terminate the other end in this case like you do with a direct coax cable here. And if you're curious to know why I said there's a phase difference was

**Dave Jones:** okay between the channels, it's because look, they're not actually the same length coax. They're slightly different, only a smidgen there but that makes a big difference on the scope. I'll show you how you can correct for that. Now

**Dave Jones:** you notice at 160 MHz there and if you zoom right in, okay, then uh can see the phase difference between there and that is just the length that that slight length difference like a centimeter or two between those cables.

**Dave Jones:** And this is actually why oscilloscopes have a probe skew function or a delay function or how whatever they want to call it. This is to correct and calibrate your uh probes for exactly the same delay time and it really matters

**Dave Jones:** when you get uh you know to really high frequencies ultra you know high frequency oscilloscopes you know in the many hundreds of megahertz as we see here or into the gigahertz range then your probe skew we've added minus 262

**Dave Jones:** picoseconds of skew there to correct for that difference. So we've basically got a length difference there of 262 picoseconds. Let's see if we can actually measure the exact difference and see that on the data sheet and actually get and see if that value

**Dave Jones:** actually calculates out. And there you go. That's the difference in our length about 45 mm. And the data sheet value for this I don't have the exact one but I uh it's going to be near enough. Let's take 5.05

**Dave Jones:** nanoseconds per meter propagation delay and at 45 mm uh differential uh in length there we're going to equal about 227 picoseconds uh delay difference between those two channels. And what do we get on the scope? We have to correct in round about

**Dave Jones:** 262 or thereabouts. So there you go. It works out. So with those two similar coaxials and if you don't terminate the inputs like on this uh Rigol scope here, look what happens. I mean we're at uh around about

**Dave Jones:** 35 megahertz and not only can the amplitude change but then the phase can drastically change as well and then they can swap over and do weird ass stuff like that at a particular frequency that is going to change with the uh

**Dave Jones:** uh impedance of the co-actual using the length of the coax and the reflect and the load being reflected as well. Yes, this is all transmission line stuff. So, when you start playing around with transmission lines, which coax cables

**Dave Jones:** are at what any any transmission line at high frequency and you don't terminate the things correctly, you can end up with all sorts of weird phase and amplitude adding and subtracting and standing waves, which we won't go a huge

**Dave Jones:** amount into, but look, even though we're not terminating these inputs here, there's no 50 ohm termination at all, so it's not a simple 50 ohm termination issue. If I disconnect channel two, look at look the amplitude of channel one

**Dave Jones:** actually dropped. And then, if I take another piece of coax like this and whack that in series with that one, so I've doubled the length of one of them. Whoa, dude, look at that. And it gets even more weird. Look at this,

**Dave Jones:** right? I'm now correctly terminating my scope in 50 ohms, there it is, so we get in our very nice, you know, 1 volt peak-to-peak exactly as we expect. And look what happens if I just whack on a piece of coax like this. There's nothing

**Dave Jones:** on the other end of it, there's nothing up my sleeve. Boom, it vanished. Our signal vanished. Whoa, and that's at 57 megahertz. Now, if I change the frequency, let's go back down to this frequency here. You'll notice it makes hardly any

**Dave Jones:** difference at all. That's because the the transmission line effects, the reflections are subtracting from going back, reflecting off this end, and then subtracting at the input here to the scope. So, your signal at your oscilloscope can actually vanish if

**Dave Jones:** you're not probing things properly and terminating things properly. Now, one way to demonstrate this is to instead of using sine wave, use a square wave. I'm just using the output of the Rigol function gen, so it's not incredibly

**Dave Jones:** sharp, but as you know, a square wave edge like that generates a whole bunch of uh you know, harmonic frequencies. So, watch what happens if we take the same coax cable. Look, you know, it's pretty nice edge there. It's all

**Dave Jones:** compensated very nicely cuz it's terminated in a 50-ohm impedance. Let's add on just this empty bit of coax like this and see what see what happens. Look at that. We've got what What is causing that? Well, all of the frequencies and

**Dave Jones:** the phase and depending on upon the length of the coax, the signal has been reflected from the unterminated end of this coax, reflected back along the coax, and it's subtracted from our signal here. So, it's been subtracted at

**Dave Jones:** the input of the oscilloscope at that particular frequency and phase. Whereas at this point here, it's actually added up. So, that can be the difference. And that's going to change if I change the length of the coax. And you'll notice

**Dave Jones:** that change even if I just add a little tiny barrel adapter like that to it. Look at that. You see? It goes It moves back at just a tiny smidgen. So, if we add another coax which is exactly the

**Dave Jones:** same length, about 2 ft or whatever, look at that. Bam! Everything changes because the length of a stub here. And I'll just give you a very quick whiteboard explanation of what's happening here. Now, you know that the a

**Dave Jones:** square wave by your Fourier uh theory is made up of or can be thought of or for practical purposes is made up of a fundamental frequency plus all of the odd harmonics at low at diminishing diminishing amplitudes. And when you add

**Dave Jones:** up all these uh sine waves, it gives you a square wave. So, a square wave has many different frequencies contained in it. And for a transmission line, that's a big deal. So, what we've got here is our signal generator. Okay, we're going

**Dave Jones:** through the first bit of coax, but it it doesn't matter. We're basically talking about the signal on the 50 ohm load at the oscilloscope. So, our oscilloscope is actually measuring these two points here, okay, across our load. But then

**Dave Jones:** we've got that extra bit of coax hanging off that stub. And because it's open, it's not terminated properly, we're going to get reflections back. Now, the signal here the got the square wave in red, okay? It's made up of all these

**Dave Jones:** different frequencies. So, if it's a 1 MHz signal, we're going to have all of the odd harmonics in there, 3 MHz, 5 MHz, 7 MHz, and so on down in diminishing amplitude. Now, when all of these frequencies travel along this coax

**Dave Jones:** and then get reflected back, some of them are going to be in phase, some of them are going to be out of phase, and they're going to have different delays. And this is uh known uh theory as group delay and phase

**Dave Jones:** delay. And I won't go into the details of it, but suffice it to say that pretty much any medium that your signal travels through, be it air, coax, or whatever, um these different frequencies are going to have slightly different or can have

**Dave Jones:** slightly different delays and phases uh based on the frequency content. So, take for example this 3 MHz, and let's just assume that that one is going to be fed back or reflected back in phase. And I've shown this here, and it is

**Dave Jones:** reflected back. And because it's in phase, it adds up. It adds to the existing amplitude signal at 1 MHz here. So, that is why in blue here your signal rises like that as we saw on the scope. But say your next harmonic or a

**Dave Jones:** different harmonic here at 5 MHz, that may come back out of phase due to phase delay and group delay and that's what the stuff and then if it's out of phase it can actually subtract from your existing signal there. So that's why you

**Dave Jones:** can end up with that little weird sort of you know pedestal thing on your waveform and so on and so on for all the different frequencies depending on your type of load, the coax, the length and the all sorts of properties of the coax.

**Dave Jones:** You can end up with all sorts of weird and wonderful waveforms reflected back like this. So that explains the square wave part of it but what's happening with the sine wave? Well, it's exactly the same thing because of group delay

**Dave Jones:** and phase delay even if you've got one pure sine wave at one frequency. So there's no other frequency content at all, no harmonics, you still that one signal can still get reflected back or it will be reflected back off the open end of the coax but it

**Dave Jones:** could come back at a different phase depending on the frequency and if it's big enough your signal can vanish which is what we saw on the scope before or practically vanish or it can double. It can actually increase or decrease in

**Dave Jones:** amplitude depending on the frequency and we saw that and we can see that there's another good example for that again I'll show you. Okay, now what I've got here is exactly the same coax we've been using before from the signal generator

**Dave Jones:** unterminated at the input here. Okay, so our signal that we're sending from the function gen is going to get reflected back because this isn't terminated properly back to here. And and you might think well, we should always get the

**Dave Jones:** same value out of the function generator output here cuz it's a nice low impedance, it's driving this coax. Why would the signal output here change? You can understand how it changes at the end here but watch this. So I'll get my uh

**Dave Jones:** oscilloscope probe, which is on channel two here, so that'll be the blue waveform, and we'll plug that in over here. So, now we can see the different waveforms, and let's wind up the frequency and see what we get here. So,

**Dave Jones:** watch this. If we go start at 1 MHz, everything's fine, right? Both waveforms, they're all nice nicely in phase there, not a problem. Okay, and exactly the same amplitude, exactly what you'd expect. But, you wind that frequency up, and

**Dave Jones:** let's see what happens here. Look, it starts to get out of phase. This reflected signal back from the coax like this is now arriving back here out of phase, and you can see the amplitude is changing. So, if we increase that, you can see the

**Dave Jones:** amplitude goes down on this reflected signal here, that blue signal there, and it's out of phase. And if we get to we're up to 42 MHz at the moment. Hey, that's a good number. I like that, but look, we get to there, and that's about

**Dave Jones:** 47 MHz. Just so happens to be the frequency where the minimum value, we hit a minimum value at our input over here. So, and if we keep going up in frequency, you'll notice that it goes back up, and it

**Dave Jones:** comes back in phase, but look at that. So, that's a great example of how your signal gets reflected back from the coax and can actually cancel right at the output of your function generator here. So, getting back to the

**Dave Jones:** original question and point of this video, why does that waveform there change in amplitude that we measure on the scope here from the output of the function generator change in amplitude when we change the frequency like this? Well, you'll notice that the yellow one

**Dave Jones:** is increasing in amplitude as the blue waveform, that reflected waveform, is uh getting getting to a minimum. So, you'll notice that the yellow one reaches a peak there when the blue one is the lowest. And that is because the

**Dave Jones:** signal is uh being reflected back off this unterminated input here, coming all the way back, add into that, and it's going to continue to reflect back and forth like this, and it's basically at the input here that we're measuring with

**Dave Jones:** the scope that is going to get added when the when we have the most amount of reflection. So, when there's the most amount of reflection here, you're going to get the maximum value, i.e., that blue waveform is a minimum. Where was

**Dave Jones:** that frequency? At 47 MHz or something? When that blue waveform is a minimum, the yellow one measured here, the input to the oscilloscope, will be at its maximum value. And that is why using a piece of coax is the wrong way to do it

**Dave Jones:** unless you actually terminate it or you actually use a high-frequency uh times 10 oscilloscope probe and plug that straight in because you're not going to get any transmission line reflection issues. So, by using this times 10 probe or using a properly

**Dave Jones:** terminated 50-ohm coax here, you're going to be able to measure, that is the correct way to measure, the true output amplitude over frequency of your function generator here or anything else. So, anyway, that was longer than I wanted it to be, but I hope you found

**Dave Jones:** that interesting and why simply connecting uh your function generator to your oscilloscope with a piece of coax, you might think that's a good thing, you're doing the right thing, but you're not, technically. And, you know, if you want

**Dave Jones:** to anything at any sort of high frequency where the wavelength is a good fraction of the length of the coax, you're going to get problems like this. You're going to get group delay and phase delay and reflections and all

**Dave Jones:** sorts of things. So, if you're doing this sort of thing, make sure you use your proper times 10 probe. A times one probe isn't going to do it. You need a times 10 probe that is designed to actually uh measure that so that you

**Dave Jones:** don't need to re-terminate uh your input here or you terminate the scope properly. In the case of the Rigol uh DG4000 series here and similar other function gens, it's output amplitude specification specified into 50 ohm load. So, you have to actually terminate

**Dave Jones:** in 50 load truly to meet the spec. But, in this case, if you do actually want to measure its open uh load uh flatness output voltage, then you've got to use this times 10 probe. So, there you go. Hope you found that

**Dave Jones:** very interesting. And it's fun to play around with this sort of stuff. You can get lots of weird and wonderful things. So, if you like that video, please give it a big thumbs up on YouTube. That helps a lot as always with the uh

**Dave Jones:** engagement of the video and the stats. Some people have asked about that. Yes, um when you comment on a YouTube video and you give it a thumbs up or a thumbs down, um that it it contributes to the

**Dave Jones:** engagement of the video and helps rank the video on the YouTube uh search engine. It's all very important stuff to get the video more popular and to be seen by more people. And as always, if you want to discuss it, you can leave

**Dave Jones:** comments on eevblog.com or you can jump over to the eevblog forum. Catch you next time.
