---
video_id: vDe_BHvRpks
title: EEVblog 1521 - Common Mode Rejection Ratio (CMRR) Explained & Measured
url: https://www.youtube.com/watch?v=vDe_BHvRpks
source: youtube-asr
timestamps: {"0": 0, "1": 12, "2": 28, "3": 44, "4": 61, "5": 75, "6": 90, "7": 106, "8": 120, "9": 138, "10": 153, "11": 170, "12": 183, "13": 198, "14": 210, "15": 225, "16": 240, "17": 253, "18": 267, "19": 280, "20": 293, "21": 308, "22": 319, "23": 331, "24": 345, "25": 355, "26": 367, "27": 383, "28": 401, "29": 416, "30": 431, "31": 442, "32": 456, "33": 473, "34": 486, "35": 501, "36": 514, "37": 529, "38": 540, "39": 554, "40": 567, "41": 580, "42": 592, "43": 604, "44": 614, "45": 624, "46": 636, "47": 647, "48": 657, "49": 667, "50": 678, "51": 690, "52": 703, "53": 718, "54": 733, "55": 746, "56": 761, "57": 773, "58": 787, "59": 804, "60": 821, "61": 839, "62": 858, "63": 871, "64": 885, "65": 901, "66": 916, "67": 932, "68": 953, "69": 969, "70": 981, "71": 998, "72": 1011, "73": 1028, "74": 1041, "75": 1056, "76": 1071, "77": 1082, "78": 1098, "79": 1111, "80": 1125, "81": 1143, "82": 1154, "83": 1165, "84": 1178}
---

**Dave Jones:** Hi, in this video I'm going to explain what common mode rejection ratio is and actually how to measure it in this particular case of a high voltage differential probe here, but it doesn't have to be a high voltage differential

**Dave Jones:** probe available on the EVblog store by the way. Discount coupon code down below. Any differential amplifier circuit be an op amp or a discrete transistor one, it will have a common mode rejection ratio. So, let's have a look at it. We're going to measure it

**Dave Jones:** with a brand spanking new Rohde & Schwarz a four MSO four series scope here, 12-bit jobby because why not? It's beautiful. So, the common mode rejection ratio of a differential amplifier, in this case a differential probe, as the name suggests, is just the

**Dave Jones:** ratio of the differential gain of the amplifier divided by the common mode gain of the amplifier. And what is differential and what is common mode? Well, a differential amplifier measures the difference between two inputs here. Their base is essentially is no ground

**Dave Jones:** reference. It is a differential signal and a differential amplifier will have a a gain of that differential signal. That's its job. If your differential amplifier has a gain of 10 and you put one volt differential across here, it

**Dave Jones:** doesn't matter where it is in the circuit, it's a differential voltage, doesn't matter about the ground reference, it'll multiply that by 10 and that's its differential gain. Now, you divide that by the common mode gain. Now, what is the common mode gain? Well,

**Dave Jones:** instead of the differential voltage across here, it is an external voltage applied to both of them at the same time. So, in this particular case, okay, we've got these long leads here and we could have like external either capacitive coupling or EMI

**Dave Jones:** coupling into the probe like this. So, they're basically getting onto the probes in the same way. And this is why the wires are twisted like this. And if you're measuring a differential signal, it means any external noise or

**Dave Jones:** interference in should in theory apply to both wires at the same time. So, it's an external reference. In this particular case, referenced to the grounded output of our differential probe. So, the job of a differential amplifier is to

**Dave Jones:** amplify the difference between its positive and negative input while rejecting all of the signal or much of the signal as it can that is applied commonly to both of these wires. So, that's why it's a common mode rejection

**Dave Jones:** ratio. So, in theory, your differential amplifier should have an infinite common mode rejection ratio. It just measures difference here and rejects everything else. It has no gain at all of any common mode signal being picked up by both wires. But in practice,

**Dave Jones:** no, that's not going to happen. Just the design of the amplifier itself and most importantly the matching of the input resistor network in here and I've done a teardown of a high voltage differential probe down like this. I'll link it in up here

**Dave Jones:** and down below if you haven't seen it. And just the matching between the resistors on here is like pretty much determines the common mode rejection ratio of this probe. Because usually like the op-amps used inside here, they're usually pretty good. They're

**Dave Jones:** going to have like a rejection ratio of like, you know, over 100 dB or something. Whereas the resistor divider drops that down to like 40 or even less. Now, a product like this HVP 70 differential probe, it'll typically have

**Dave Jones:** a common mode rejection ratio figure measured at various spot frequencies. Maybe if you're lucky, you might get like a response curve of common mode rejection ratio because it's going to vary depending on the frequency. So, it's going to change. So, they typically

**Dave Jones:** here's the values for this HVP 70 and it gives us four spot values there. And the ratio, you can see is, you know, like at 10 MHz, minus 40 dB. And it is usually given in a dB figure, but it doesn't

**Dave Jones:** have to be because it's just a ratio. So, you could just use the ratio figure. And the interesting thing about this is that the common mode rejection ratio is, as I said, the differential gain divided by the common mode gain. And that

**Dave Jones:** actually comes out at a positive value. But so, why is the data sheet negative? Well, it's kind of there's no like standard for this kind of thing. So, you just sort of have to like understand that when you're talking a negative

**Dave Jones:** number, in this particular case, minus 60 dB, uh common mode rejection would be better than minus 40 dB. But if you had it if you specify it as a positive one, as you might get on, say, a uh op-amp

**Dave Jones:** data sheet, here's an example, uh you would get a the higher the value is going to be better. So, that positive or negative thing, just a little trap for you young players, just be aware of it. Right, so how do we measure the common

**Dave Jones:** mode rejection ratio and verify the common mode rejection ratio of this probe? First thing you want to do is, as I said, you want to twist the wires like this so that any uh external noise is equally picked up on both. And then, you

**Dave Jones:** need a signal generator. In this particular case, this uh new Rohde & Schwarz MXO 4 can go up to 100 MHz, so very nice. And then, we want to feed the output of the sig gen into a 50-ohm

**Dave Jones:** terminated load so that uh we don't have any transmission line issues whatsoever, no reflections causing problems. I've done videos on that and how you can goof that up in noise measurements and stuff like that. So, I'll link in that video

**Dave Jones:** up here and down below if you uh haven't seen it. So, here I'm using an external 50-ohm uh 2-watt termination, a series termination, even though the scope has a built-in. If you look down here, you could actually come a gutser because

**Dave Jones:** this is only like got a half watt radiant. It's less than 5 volts RMS. Just, you know, you don't want to blow up your scope when you do something like this cuz you want to use a high as high

**Dave Jones:** a voltage as possible. But in this particular case, I'm just showing you it's better to use a high rated external terminator just so you don't blow up your really expensive, beautiful, shiny scope. And then we just start tapping

**Dave Jones:** off right across this 50 ohm terminator load here. So, here's the negative terminal and here's the positive terminal. So, what we want to do is connect both of these inputs together, short them together, and connect to the positive input like this. Why the

**Dave Jones:** positive input? Because it means that we're applying a voltage relative to the output here cuz the output is ground reference like this. So, we're actually referencing it to the output. So, we're effectively feeding that signal generator voltage into both of these

**Dave Jones:** leads, i.e. a common mode signal relative to the grounded output. Because if you remember, all the grounds on your scope are all common. So, this is the input signal and the output and they're effectively joined. They're common. So,

**Dave Jones:** what happens if I just connect one of these to here? Well, you saw it. The green signal's our output. The yellow is our input there and our green signal, it gives us a nice, clean output like that, okay? So, our

**Dave Jones:** differential probe is cuz this one's just flapping around in the breeze, right? Doing nothing and you'll see that just jump all over the place there. And if I touch it, look at that. Like we're picking up all sorts of crap. And you'll

**Dave Jones:** get the same exactly the same thing if you connect the negative up like that, right? The exact same thing will happen cuz this is a differential amplifier. It it doesn't care. Um it just you're just unbalancing that input. But if you

**Dave Jones:** connect both of them on like that to the same point, then bingo, we've got a really small signal. So, this probe isn't perfect. It's got a common mode rejection ratio. So, there you go. It's There's a signal being amplified even

**Dave Jones:** though that input is completely shorted. And you'll notice that goes away if we don't connect up to that. Okay? There's our ground there, so we've just got like the inherent noise of that amplifier. It doesn't matter what I do to the probes

**Dave Jones:** here, but this one, if we hook it back up, you'll notice that if I start playing with those probes, things start happening. Okay? It starts like being influenced because like we've got these long leads here. That's why a

**Dave Jones:** differential probe with like like really shorter leads is better, but these have them Most probes have them built in though, unfortunately. So, what happens if I untwist those leads like this? We're going to get the same signal, but

**Dave Jones:** we potentially have more variation. Check it out. You actually get huge differences. Like if I like take my hand away from that, right? You can get large differences like that. So, if you don't twist the leads and keep that common

**Dave Jones:** mode signal, right? You can completely screw up and come a gutser on your measurement. Now that I've explained what we're doing and I've shown you the setup here, there's no reason to look at this anymore. So, I'm going to actually

**Dave Jones:** go over to a remote desktop view and we'll do a direct screen capture of this. It'll be just be nicer and because I can. Ah, isn't this schmick? Look at this. Ethernet remote control. It's got a building web browser, so we can just go

**Dave Jones:** to the IP address and bam, we're in. So, we can actually we can do some like configuration and file manager stuff, but let's just go to full screen here. So, channel one, the yellow one, that's our sig gen there. We've got 1 V per

**Dave Jones:** division, 50 MHz bandwidth cuz you do want to bandwidth limit. And this scope actually has some cool software bandwidth limiting options in it, um, might see later. And, uh, one one big ohm input, DC coupled, DC or AC, it

**Dave Jones:** doesn't matter. And channel two also the same, uh, 50 MHz, uh, bandwidth here. Leave it on, uh, 2 mV there, shall we? Now, you can see we've got a real fuzzy wuzzy waveform here. Now, of course, this is a, uh, 12-bit scope. You don't

**Dave Jones:** necessarily need a 12-bit scope for, you know, this particular application that we're doing, uh, right here. But, 10 or 12 bits, more betterer. But, we can actually go more than this. So, you can actually see up here, up the top, it's

**Dave Jones:** telling us start to just that's the basic 12-bit. Uh, but we can go higher, because if I get my ugly mug out of here, we can see that got a HD mode down here, a high definition, uh, mode. And

**Dave Jones:** we can actually set that on, whoop, oh, there we go. We instantly set it on. And you'll notice that our 12 bits went to 16 bits up here. But, before we go ahead with that, I'll just mention the, uh,

**Dave Jones:** signal gen here. Now, uh, you want this to be as higher amplitude as possible, because the output signal that you're actually trying to measure, um, that common mode signal is really low. So, the higher the input signal, the better.

**Dave Jones:** So, I've gone up to the maximum, uh, amplitude here of, uh, 5 V peak to peak here. And, uh, we've got a frequency of 10 MHz, because that's just the, uh, you know, a typical figure we've got in

**Dave Jones:** the data sheet, which we want to try and, uh, verify. So, we want to clean this up a bit more. So, let's do some averaging. So, we'll go up to the, uh, acquisition up here, and we're actually, uh, in sample mode. So, we'll go down

**Dave Jones:** here to average mode, and then, boom, we can do like 40 averages, something like that. We can take the, uh, time base out a bit like that. So, we've got a decent number of signals. You can see that our

**Dave Jones:** average there, we've got 40 averages there, and, uh, that's just cleaned that up a tad. But, you can see how we are dealing with the wobbly's down here. Cuz as I said, the test setup is everything. So, if you can shield it and keep the

**Dave Jones:** leads short, and, uh, make sure that they're twisted and everything else, it's going to be, uh, better. So, what we need now is to compare the input signal to the output signal. That'll give us our common mode rejection ratio.

**Dave Jones:** In this particular case, that it's actually negative here. So, at 10 MHz, it's minus 40 dB here. So, we want to flip that around here to give the output divided by the input. Now, to measure this uh ratio between input and output,

**Dave Jones:** we can either measure the uh peak to peak value or the RMS value. Doesn't matter. RMS is, you know, it's better. It's more accurate. But, you might think that we use this RMS value here. And uh what's that 1.4 mV like that. But, I've

**Dave Jones:** done a video on this where that RMS value, that includes any DC offset component. So, that's not quite what you want. So, let's go into the measurement uh menu here. Unfortunately, they don't have it in the basic category. You've

**Dave Jones:** got to go down to vertical there. There you go. Standard deviation AC RMS. I've done an entire video on that. So, we want uh channel uh one. But, I can actually uh go in here like this. I can

**Dave Jones:** double-click on that, and I can choose specific type AC RMS like that. So, let's actually get a few waveforms on screen here. So, it's a bit more accurate. And uh once again, we can turn the statistics on there. Come on. Can't

**Dave Jones:** double-click to get into the menu. Oops, I had the uh wrong bandwidth there. So, we have to use the 50-MHz uh bandwidth here cuz we're measuring at 10 meg. 20 meg is a bit close to the frequency. You want to be a bit more

**Dave Jones:** than double above like that. So, you know, 50 is 50 is not a bad value. So, we get our confuser out here, and we look at the RMS value here. Don't be confused by Remember how I mentioned standard deviation before? You got to

**Dave Jones:** watch my standard deviation video. The standard deviation here is not referring to the AC RMS. It's referring to the standard deviation of the standard deviation AC RMS signal. So, it's like it is very confusing. So, yeah, don't come a guster there. So, we

**Dave Jones:** need to uh get our confuser out and uh 883 microvolts. So, microvolts, we won't get any more precision than that. Uh divided by our input because we want a negative uh number. So, 1.75 V. Then, we want to take the log of that uh

**Dave Jones:** and then multiply that by 20, not 10, cuz this is a voltage. So, we get minus 65 uh minus 66, basically. Hmm. That doesn't sound right. Cuz our spec over here says minus 40 at 10 MHz. Why is it way,

**Dave Jones:** way better? Way, way betterer. Hmm. Because this CMRR is what's called input referred. It's referring to the input of the actual uh amplifier in this case inside the uh probe here before it gets gained up by the amplifier. Now, if you

**Dave Jones:** noticed in the video before, we're in the uh 10:1 division ratio setting. So, there's a gain of 10 in there. So, we have to account for that uh gain of 10 in here in our DB figure. Now, you know,

**Dave Jones:** a good data sheet, they should actually specify that and tell you exactly what it is. Now, this is a good marketing trick because marketing can make the common mode rejection figure sound a lot better just by saying, "Oh, that's input

**Dave Jones:** referred." instead of like output referred. So, in this particular case, uh our times 10 uh probe over there, times 10, of course, in DBs is 20 DB. And times 100 would be 40 DB. Times 1,000 would be 60 DB. It goes up 20 DB

**Dave Jones:** for each order of magnitude step. So, we have to actually add on uh 20 DB to that. Minus 66 DB becomes minus 46 DB. So, yes, it does actually meet that specification. So, it beats it by 6 DB.

**Dave Jones:** Not too shabby. So, let's repeat this at 1 MHz. So, So should get better by about uh 10 dB. So it's got this 46 here. Maybe we'll get 56, will we? So there you go, 423 microvolts divided by 1.8

**Dave Jones:** volts there. Uh and log * 20 = -72. Yep, add 20 dB to that. So it's -52. So there you go, the typical spec is -50, we're getting -52. Yeah. Comes out. But if we try and measure it down at 50

**Dave Jones:** Hz here, which is supposed to be -80 dB, so again like it it's 20 dB increase over 20 kHz, you can see that yeah, it's it's gone to nothing. Again here, 500 microvolts per division, and there's nothing There's nothing there. I mean,

**Dave Jones:** we can take that figure and punch it into the calculator, but like there's just nothing there. We're basically measuring the RMS value of the noise at this point. Anyway, you can see the process there. That's how we can

**Dave Jones:** measure the spot frequency. Now, how can we get a plot over frequency? I'm glad you asked. We can do this using If we go into apps here, FFRA or frequency response analyzer. So, let's open this bad boy up. Yeah, we can get a plot of

**Dave Jones:** this over frequency. We can also get phase as well. So we're going to put our stop frequency in here of 10 MHz, and start frequency. Yeah, we can actually start down at that 50 Hz. So we set up

**Dave Jones:** our input as channel one, our output is channel two, 50 Hz to 10 MHz. Amplitude as you Once again, you want the maximum amplitude. Run on this. Now watch down in the bottom corner down here. As it's adjusted, it's set to AC,

**Dave Jones:** and then it's adjusting the range, all in real time. And you can see it's slowly pro plotting here. It's only a small It's got a table and a thing we could we could zoom that later if we really wanted to. 50 hertz, 100

**Dave Jones:** hertz, right? It's down in the noise. Starting to get out of the noise there. We can adjust the range in a minute to actually see that. And boom, we are done. Now, I don't think there's anything in here that allows us to set

**Dave Jones:** the offset there. Just remember that we have to add 20 dB onto these figures here. So, you can see that you know, around about 5 megahertz there, it does really you know, it starts to gets worse the higher that is the worse it is. And you

**Dave Jones:** can see that the the red plot here is the gain. We're not too that doesn't matter for our common mode rejection ratio. But if we actually extend the bandwidth on that, we should be able to actually see a phase reversal. So, at 10

**Dave Jones:** megahertz here, you can see minus 64, which is minus 44. The 1 megahertz figure it's minus 71 is minus 51 dB there. So, yeah, that meets the spec. So, if I go up to the full bandwidth here, 70 megahertz of this probe, let's

**Dave Jones:** rerun that again. I'm not going to go low frequency this time. So, it's auto ranging each time it actually takes these samples, which is really quite nice. So, it's maximizing its dynamic range there. And it's also adjusting its

**Dave Jones:** bandwidth as well. You'll see that the yeah, it just jumped from 1 to 2 megahertz, 3 megahertz, see? So, it's actually it's software adjusting that bandwidth. This is really cool. This is a very good frequency response analyzer. So, we're looking for the phase response

**Dave Jones:** to actually reverse here. Oh, yep. There it is. There it is. That's totally expected. Not just a differential amplifier, it's normal amplifier behavior. But once again, phase doesn't mean anything here. Right up to 70 megahertz, it's minus 41, which is minus 21 dB. So, it's

**Dave Jones:** a fairly sharp rise. It's once you get above that 10 megahertz, that's why they don't give you a figure up at 50 meg or 70 meg. They Once again, marketing just does, know, stop at 10 MHz. There you

**Dave Jones:** go. Common mode rejection ratio. If you enjoyed it, give it a big thumbs up. As always, discuss it down below and subscribe to EE Vblog 2 and my Odyssey channel where there's exclusive videos over there. If you want to see a couple

**Dave Jones:** of these I think I've got two exclusive videos of the Rohde & Schwarz oscilloscope why it's actually been delayed cuz we had to actually swap it. Yeah, this is really sweet scope. So, yeah. Leave Leave it in the comments. Do you

**Dave Jones:** want to see a teardown or want to see a feature review? It's got so many features, but I can show you some of the really cool stuff in this. It's going to be good. So, anyway, catch you next time.
