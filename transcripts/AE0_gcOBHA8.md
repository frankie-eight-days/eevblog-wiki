---
video_id: AE0_gcOBHA8
title: EEVblog #617 - Tektronix Oscilloscope Anomaly
url: https://www.youtube.com/watch?v=AE0_gcOBHA8
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 34, "3": 48, "4": 65, "5": 82, "6": 96, "7": 114, "8": 132, "9": 144, "10": 158, "11": 174, "12": 194, "13": 211, "14": 229, "15": 243, "16": 257, "17": 272, "18": 286, "19": 302, "20": 315, "21": 334, "22": 352, "23": 369, "24": 386, "25": 400, "26": 416, "27": 428, "28": 446, "29": 460, "30": 478, "31": 491, "32": 506, "33": 518, "34": 531, "35": 557, "36": 572, "37": 587, "38": 602, "39": 620, "40": 635, "41": 650, "42": 663, "43": 677, "44": 689, "45": 700, "46": 715, "47": 731, "48": 744, "49": 759, "50": 773, "51": 789, "52": 803, "53": 820, "54": 834, "55": 850, "56": 864, "57": 883, "58": 901, "59": 916, "60": 930, "61": 944, "62": 958, "63": 974, "64": 990, "65": 1005, "66": 1018, "67": 1032, "68": 1049, "69": 1061, "70": 1077, "71": 1091, "72": 1104, "73": 1120, "74": 1137, "75": 1149, "76": 1162, "77": 1176, "78": 1192, "79": 1205, "80": 1216, "81": 1227, "82": 1241, "83": 1254, "84": 1268, "85": 1282, "86": 1297, "87": 1309, "88": 1322, "89": 1338, "90": 1355, "91": 1372, "92": 1386, "93": 1402, "94": 1420, "95": 1437, "96": 1451, "97": 1465, "98": 1478, "99": 1493, "100": 1507}
---

**Dave Jones:** Hi, I thought I'd show you something interesting with Tektronix digital storage oscilloscopes and it is pretty specific to Tektronix scopes as far as I'm aware. I'm not aware of other brand scopes on the market that actually do this. Now, let's take a look at this MDO

**Dave Jones:** 3000 series scope. I'm feeding in just a a 2 MHz square wave here. Nothing fancy. It's all triggered. Everything's hunky-dory and I've got the output the trigger output of this connected up to my Rigol function generator up here. So, it's generating

**Dave Jones:** the 2 MHz signal as well as displaying effectively the waveform update rate of this oscilloscope. Now, I've talked about waveform update rates before in our previous video. So, I won't go over it again, but look, you know, it's a

**Dave Jones:** pretty good scope. We're getting 250 odd 250 kHz, which is means 250,000 waveform updates per second, right? It's a pretty you know, modern quick scope. And of course, that's with that the fast acquisition mode on, okay? So, if I turn

**Dave Jones:** fast acquisition mode off, then it drops down to, you know, 68 kHz, something like that, 70 odd kHz, but still, you know, quite a respectable update rate. And of course, you'd expect the waveform update rate to change with

**Dave Jones:** your record length. So, my record length is only 1,000 bytes at the moment. Like 1,000 samples, sorry, but I could change it to 10k and it drops a little bit. I change it to 100k points waveform memory. There you go. It's dropped down

**Dave Jones:** to 22 kHz there or thereabouts. 1 meg with 1 meg memory, we're talking, you know, 380 390 Hz waveform updates per second. Not much at all, but that's what happens when you get the deeper memory. And of course, if

**Dave Jones:** you turn fast acquisition mode back on, bingo, we're back up to 250,000 waveform updates per second. That's at 100 nanoseconds uh per division. But, watch this. Watch what happens if I change the trigger level. Okay, here's my trigger level, right? It's

**Dave Jones:** right in the middle here. Watch this. This is the interesting thing I wanted to show you. What happens if I raise the trigger point above that, so there is no longer any trigger, and it's got to go into auto trigger mode.

**Dave Jones:** And of course, it is in auto uh trigger mode, so we can actually go in there. And there it is. Yep, auto trigger mode. Okay. So, if I had just adjust that level there, watch what happens.

**Dave Jones:** Look at that. Look at that. And our trigger frequency has dropped down the bugger all here, but look at what And you'll probably already noticed on the screen there that it's not very quick at all. And well, that's confirmed up here.

**Dave Jones:** Look, it's got a wave drop down to a waveform update rate of like 19 hertz. Hertz, 19 waveform updates per second in that free running auto trigger mode. When there's no trigger, Tektronix oscilloscopes drop down to an incredibly low value of

**Dave Jones:** waveform updates per second. Very interesting. And of course, it'll do exactly the same thing if I simply remove the input signal here. So, there we go. 250,000 waveform updates per second, and boom, we drop down to, you know, 10 or 20

**Dave Jones:** hertz or thereabouts. Unbelievable. And you can really see that on the screen there, too, in terms of the waveform and how it's you know, a really slow waveform update rate. And that is actually a true, you know, 10 or 20 hertz waveform update

**Dave Jones:** rate. It's very, very slow. Now, because that Rigol frequency counter in that DG4000 series is a little bit dicky, I will actually look at the waveform. So, I've got it on my Agilent 3000 series here. And no, you

**Dave Jones:** can't do it on the other on the actual Tektronix scope itself cuz then you'd have to trigger off the second channel import, so then you're not in that untriggered mode anymore. So, that's just the way it works. You need a second

**Dave Jones:** oscilloscope here. You can see it's pretty stable there it is. Um you know, 19.9 Hz is basically 20 Hz. And then of course, if I plug my signal back in, bingo, look at that. There we go. We're way back in there and then we get that

**Dave Jones:** super fast update rate. It does jump around a little bit cuz there's trigger jitter stuff like that, but there you go. It's jumped up to the 250 odd kHz that we're at before. So, there we go. We have a quite a bit of jitter

**Dave Jones:** on that probably due to the processing. Let's actually turn on the fast acquisition. You'll see it's like I can stop that and we're looking at you know, 70 odd kHz or thereabouts. Let's turn fast acquisition mode on again. And bingo, look at that. It

**Dave Jones:** becomes much more stable in that fast acquisition mode, but there are periods there where it actually blanks out. Now, let's see if we can actually capture that and measure that value of that blanking period. And there you go. Set

**Dave Jones:** up the cursors there and what do you know? Precisely precisely bang on 25 Hz. So, there you go. It's you know, fine down in there at that in fast acquisition mode. It's pretty stable at that 250 K mark or

**Dave Jones:** thereabouts. Yeah, what is it? Yeah, there we go. 250 kHz. 250,000 waveform updates per second, but it adds in that blanking period. There it's doing something there. Some sort of processing where it stops that triggering and stops that waveform

**Dave Jones:** stops the waveform update rate every 40 milliseconds or so. And there you go, it has a dead time of 873 microseconds. So there you go, that is interesting. When there's no trigger in that free running auto mode, bang, it drops down

**Dave Jones:** to a ridiculously low waveform updates per second. Now, I've got to say there's nothing inherently wrong cuz it's always sitting there waiting for that trigger to actually happen in the background and the glitch capture and everything else. So it's everything's just fine there. So

**Dave Jones:** in terms of this scope it's just that visually you know it's just a bit disconcerting I think. And the other thing that makes it interesting is that other oscilloscopes don't seem to have this. Let's try the same thing on the Agilent. So there's a

**Dave Jones:** signal on our Agilent once again 100 nanoseconds per division measuring that 2 megahertz signal and no my hold off is set to absolute minimum. So there is no hold off there. That's the way in triggered mode that you can actually reduce the

**Dave Jones:** waveform update rates per second and I might show you that in a minute but let's take a look at what the the here's the trigger output of the Agilent scope. So we're going to you know it's jumping around a bit there. So

**Dave Jones:** let's zoom let's freeze that. There we go. We're looking at 333 kilohertz or thereabouts. So you know 333,000 waveform updates per second. There's the odd skipped one and stuff like that but you know as you know the Agilent is the fastest

**Dave Jones:** updating scope in the industry. So we can actually change that. So let's run it back and let's up the time base on the Agilent here and we can go right in let's go right up and you'll notice that

**Dave Jones:** at the higher time base we should get close to our theoretical 1 million waveform updates rates per second. There we go. 1.01 MHz. So, super quick, but once again, it's not absolutely consistent in there, but very very quick. Now, at this fast time base, it

**Dave Jones:** doesn't look like there's any dead spots in there, but let's wind the wick right out and aha, bingo. There we go. We've captured them just like we got on the Tektronix. So, the Agilent also has these dead time periods. Let's see if

**Dave Jones:** it's the same. And I've got the cursors set up here and the period of that seems to be about 16.6 ms or around about 65 Hz or thereabouts. So, not that exact round figure like we got on the Tek. So,

**Dave Jones:** the Agilent is certainly also got some waveform processing dead spots in there just like the Tek did. And we're looking at a dead time there of about 230 microseconds total. Now, of course, here's the big test. What happens if we

**Dave Jones:** disconnect our input signal and the Agilent goes into free running trigger mode just like the Tek scope. Well, let's try it. Here's our waveform update rates per second. Let's pull it out. Look, it's basically the same. It is

**Dave Jones:** still very very quick. It's still 340,000 waveform update rates per second. Totally different to the way this Tektronix scope actually works. They're entirely different beasts. The Agilent, it's waveform update rates per second is basically the same regardless of whether or not you're

**Dave Jones:** triggering on a signal. But, for some reason, the Tektronix, if there's no trigger signal, it sits around, twiddles its thumbs, and waits, and has a timeout in there of you know, that sort of like 50 ms, 60 ms

**Dave Jones:** kind of value. And well, why? Well, I asked Tektronix and they said, "Well, that's just the way Tektronix scopes work. That's the way it's always been." So, I've got another Tektronix scope here, much older model. It's a TDS 3000

**Dave Jones:** series, 500 MHz, got DPO technology. Once again, it's a pretty uh fast updating rate scope for its guy day. And as you can see, I'm in Let's zoom into the waveform there, and you can really see that's updating very quick.

**Dave Jones:** Unfortunately, this scope does not have a trigger out to readily measure the waveform update um rate. So, we're going to have to just look at the waveform. Now, let me discon- uh disconnect the input and watch it. Ready? There it goes. You can see that

**Dave Jones:** it's dropping down to a almost certainly exactly the same rate like it does on the new MDO 3000. Tektronix are continuing to operate this exactly the same way, and I'm told that's how all their digital scopes have always worked.

**Dave Jones:** And what about this Rigol DS2000 series? Well, once again, exactly the same, 100 ns per division measuring this 2-MHz waveform, uh the lowest memory rate possible. So, let's go into the acquire menu. Sample mode, memory depth is auto,

**Dave Jones:** but I can set it down to the absolute uh minimum 14K points, but it makes absolutely no difference. And what update rate frequency do we get? Yes, this one has a trigger out, so we're able to have a look at that. And there

**Dave Jones:** we go, about 23 and 1/2 kHz. 23,000 waveform updates per second. Now, exactly the same test again. What happens if I disconnect my input signal down here? Well, let's have a look. 23 and 1/2 kHz, disconnected, it's exactly

**Dave Jones:** the same. In fact, it's gone up a little bit to 24 kHz. Oh, I promised to show you how the uh trigger hold-off can slow down the waveform update rates per second. I've probably showed you this before, but let's go in there. Here we

**Dave Jones:** go, trigger hold-off. It's down at 100 ns at the moment. If we increase that, I have to increase it a fair amount before it's going to become a percentage, but here it is. Look at that. There we go.

**Dave Jones:** Our waveform update rate has dropped to basically the uh trigger hold-off value. So, there we go. That's 100 microseconds uh hold-off there, and we're getting basically almost 10 kHz there. So, there you go. That's a way to slow down the

**Dave Jones:** waveform update rate of your oscilloscope if you need to. Now, I've also got this GW Instek GDS-2000A series, and it's a fast updating rate uh scope as well. Nominal uh maximum rate of about 80,000 waveform updates per second. It's got

**Dave Jones:** the VPO technology. It's got demo signal outputs here, and one of the demos can actually be set to the trigger output here, so I can select that. So, we can actually get the trigger output frequency, but it doesn't seem to be

**Dave Jones:** working. So, it's actually rather strange. We're getting what uh we would expect for a trigger pulse out of the thing, but it's only at 100 Hz, 99.9 Hz, basically 100. We've got the same 2 MHz signal going in here. We know it's

**Dave Jones:** capable of 80,000 waveform updates per second. It certainly looks very fast uh as well, but for some reason its trigger output is not giving us what we expect. And the time per division makes no difference. If I increase that right up

**Dave Jones:** to 10 nano uh seconds per division, then we expect it to be, you know, maximum waveform update rate, but it's not. It makes no difference whatsoever. If we go down, then we then we can actually get this to change. So, it seems to be doing

**Dave Jones:** that, but it's more like it's the display update instead of the actual waveform acquisition or something like that. Anyway, it does it change if we take the uh turn off the input. No, it's exactly the same because I think it's

**Dave Jones:** just the display update rate. So, the waveform updates per second, we can actually go in here and and have a look at that. And really I can't see any difference. I'll disconnect the signal and the waveform update rate looks basically

**Dave Jones:** the same. It looks very quick with and without that signal. And of course I can adjust the trigger level up here and I can go out of that. And I don't know. So, it's hard to tell, but I get the impression that it's operating

**Dave Jones:** exactly the same as the Agilent and the Rigol unit. I.e. it's going into a true free running uh trigger mode when there's no trigger or no input signal. Now, here's an interesting little aside I just discovered. Something really

**Dave Jones:** weird. I can't really explain what it's doing here. Totally unrelated to this, but look, I've got a 100 MHz triangle wave, but it's spread spectrum, okay? So, it's going to be jittery all over the place, okay? So, there it is. It's

**Dave Jones:** being triggered, find the trigger levels, you know, there, and everything's hunky-dory. Fast acquisition mode is off. Now, watch what happens if I turn fast acquisition mode on. Look at that. It turns it into some bizarre sort of point-based. It's like individual dots

**Dave Jones:** and then showing the difference in the dots. Now, that's got to be intentional. And of course you can change the waveform palette on that. There's the spectral response showing the different colors for the different intensity. So, that's really rather interesting. I'm I'm not

**Dave Jones:** sure if I'm impressed by that or whether or not I'm I'm a little bit scared at how that's actually displaying that. It's got to be a feature. Hmm. So, anyway, I've got fast acquisition mode turned off and there we go. Our waveform

**Dave Jones:** is updating, everything's hunky-dory. It's probably doing that 250,000 times per second. And let's take the trigger level up so it doesn't trigger any anymore. And there we go. We get that, you know, like 19-20 Hz update rate. It

**Dave Jones:** looks pretty awful, but you can actually see the waveform. So, that's You could argue that's actually useful, and that's different to how the Agilent operates. Let me show you. Okay, the exact same signal on the Agilent, and adjust our

**Dave Jones:** trigger level up, and boom, look at that, free running. You can't see that signal at all. But of course, if you press stop, boom, we're straight in. You can see you instantly capture. Run, stop, run, stop. And that brings up

**Dave Jones:** another difference between these scopes in terms of how they operate. Let's take that trigger level up, so it's not triggering at all, and it's just free running. Although it's not true auto update triggering as the Agilent is. Press stop, and you get all those

**Dave Jones:** multiple waveforms on the screen like that. I don't like that. When I press stop, to see a single capture, single waveform. Uh, I don't know. Agilent uh Tek must have their reason for doing that. And then of course, it fixes it as

**Dave Jones:** soon as you move the horizontal position, or you change the scale like that, and you're instantly replaying the memory. It doesn't have that uh displayed value, or that sort of, you know, that uh persistence information that it's showing like it does when you

**Dave Jones:** just press stop. So, how does the Rigol operate? Well, in one way, exactly like the Agilent. Let's take a look. Here's the level, signal level, boom, stops. Look at that. There we go. It goes into true free running mode. You can't see a

**Dave Jones:** waveform, but it's pretty Soon as you press stop, it acts exactly like the Tektronix one. So, it's sort of like a blend of both modes. And once again, if you move the position, or you move the uh time base, then you get the captured

**Dave Jones:** waveform. Uh, and how does the GW Instek operate? Well, let's try that. Let's take the trigger level up and it free runs like that, but it's not nearly as fast as what it should be. It claims 80,000 waveform updates per second, but I don't

**Dave Jones:** know. I'm sort of beginning to doubt this. It's really weird. It doesn't operate like all the other scopes in that regard. So, I'm not sure what they're doing with the acquisition there and with the acquisition engine there and how they're claiming those 80,000

**Dave Jones:** waveform updates per second. Need more investigation there. Anyway, if you stop that, boom, it instantly operates like the Agilent one and displays your captured waveform single shot instead of the displayed waveform it had before. So, there you go. That just goes to show

**Dave Jones:** you a couple of operational differences. I know this sort of led us astray from what this video kind of started at with just showing that little quirk in how the Tektronix operates, but anyway, you know, I like to waffle on

**Dave Jones:** here and I find these things as I play with them and I like to show you some operational differences between scopes and really none of them are right or wrong. You could argue either way about how you actually prefer it and the pros

**Dave Jones:** and cons of both approaches with these scopes, but anyway, they all certainly do operate differently or a combination of others depending on how you want to look at it. It's interesting. And here's another interesting waveform, just another aspect of scope differences I'm

**Dave Jones:** going to look at here. I've got a kind of a complicated sort of amplitude modulated pulse waveform here. Let's have a look at it. If it's got enough memory, yeah, it's like a pulse waveform like that. Okay, that's in Yeah, that's running and then

**Dave Jones:** it's then it's amplitude modulated. So, it is really quite a complex waveform for a scope to trigger on and it's also going to test memory depth as well. Now, if we have a look at the Tektronix, its memory

**Dave Jones:** depth at the moment is only set to 1,000 uh samples there. And of course, you get, you know, it's just garbage. You get all sorts of these artifacts because of the sam- of because of the memory depth there. And if we increase that to

**Dave Jones:** 10K, we're almost there. 100K, we sort of start seeing the waveform. And really, we've got to get to a meg before we start seeing it like we're seeing it on the Agilent here, although it's still not as good. And the waveform update

**Dave Jones:** rate isn't nearly as quick. So, in terms of being able to simply drive your oscilloscope on a day-to-day basis, I much prefer the Agilent where it's got no memory depth setting. It has no fast acquisition mode. It just, you know, it

**Dave Jones:** optimizes everything for you and displays the waveform as best it can. It does a best job. But something like the Tek here, you've actually got to, know how to use it and know what mode you're currently in, what memory depth you've

**Dave Jones:** got it set to, and all that sort of stuff. Otherwise, you can get tricked into thinking that your waveform something that it's not unless you go in there and start analyzing it. So, we really need the Tek set to its

**Dave Jones:** deepest memory there, 5 or 10 meg, before we start getting sort of an equivalent waveform to the Agilent up here. But you're usually not going to operate the Tek on a day-to-day basis at that kind of memory depth usually

**Dave Jones:** because it's so slow. Usually, you want a fast updating scope. And if we try and go into fast acquisition mode here, well, it For some reason, it jumps to 10 microseconds per division from 10 milliseconds per division. For starters,

**Dave Jones:** I'm not sure why it does that. But then we can certainly go up there back to our 10 milliseconds per division. But because in fast acquisition mode, we don't have the memory, you can kind of sort of see its amplitude modulated. But

**Dave Jones:** here's where the fast acquisition mode is really, really nice. And the And the color grade different palettes and color temperature grading you can get that you don't get on the Agilent. So, let's zoom right in, for example, and let's have a

**Dave Jones:** look at There we go. We're at 200 Let's go to 200 ns per division. Let's wind this one down to 200 ns as well. There we go. Look at that. Similar sort of The way the Agilent is updating

**Dave Jones:** really, really fast. You can Oh, jeez, that could cause seizures or something like that. But, look, if we change our waveform palette here, this is, you know, really nice. You can see the spectral intensity of the waveform down

**Dave Jones:** here, and this is really nice stuff. I do like this. Look at that, the color temperature. So, you can see that the red is more frequent in the center around there. Really, really very nice, and you don't get that on the Agilent.

**Dave Jones:** So, that's one of the advantages. Even that inverted mode is kind of novel. And how does the Rigol operate? Well, once again, we're back to our 10 ms per division. And look at that. I think that is just beautiful. That is a gorgeous

**Dave Jones:** intensity graded display. And I've said it before, and I've shown a video on this. I think the Rigol has the best intensity graded monochrome display out there. That analog lights just thing of beauty. So, it operates just like the Agilent, and then we can stop

**Dave Jones:** that, and we can zoom right in, because it's operating on that deep memory. If we go into acquire there, memory depth it's auto It's set to auto there, so it's choosing that real deep memory, and it's working really, really nicely. And at 200 ns per

**Dave Jones:** division, well, yeah, very, very similar to the Agilent. If you put them side by side, I'll try and get them in the same shot. There we go. Yeah, very nice. The Rigol and Agilent do operate very similar. The tech is is

**Dave Jones:** significantly different. So, on an everyday signal like this SPI line here, for example, they're both triggered like this. If I take the Agilent out of trigger like that, yeah, there goes all the data. do do do do. And I can do the

**Dave Jones:** same thing for the tech. And yeah, it's just that slower updating. Whether I don't know. I I just prefer the Agilent really. There There might be some advantage to the slower updating rate of the tech. So, there could be method in

**Dave Jones:** their madness there by not having a true auto rolling function. But each to their own. So, there you have it. That's an interesting little quirk with Tektronix digital scopes that others on the market don't seem to have. Yeah, I haven't tried all of them on the

**Dave Jones:** market, but hey, these ones here good representative sample. So, it seems to be pretty unique to tech, I think. If you know otherwise, please leave it in the comments. Now, tech have explained that the acquisition engine waveform capture and acquisition engine is dri-

**Dave Jones:** driven by the triggering system. And that's exactly what With no trigger, there's nothing for it to actually acquire. And I guess tech figure, well, if you're not triggering on a signal, what's the point of actually being able to see it? And well,

**Dave Jones:** okay, arguments are for and against that, but I personally find a little bit disconcerting watching that waveform update rate just drop to bugger all. And obviously, if there's no trigger, then they give you a timeout because people expect that's how

**Dave Jones:** oscilloscopes work. They expect continuous update rate on the screen. So, it's not like in normal mode, for example, you can put in normal mode where it just won't update at all. But in that auto mode, you sort of expect it

**Dave Jones:** to be auto. You expect it to update all the time in in an abs- even with an absence of input or otherwise or any other trigger signal, be it internal or external. And that's what these other scopes here do. And but the tech

**Dave Jones:** doesn't. It's just different. Hmm. So, there you go. That's an interesting little tidbit. I hope you like that. And if you want to discuss it, jump on over to the EV blog forum. And yes, here's the new t-shirt. Warranty void if not

**Dave Jones:** removed. Beautiful. Catch you next time.
