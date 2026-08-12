---
video_id: L9q5vwCESEQ
title: EEVblog #317 - PCB Tinning Myth Busting
url: https://www.youtube.com/watch?v=L9q5vwCESEQ
source: youtube-asr
timestamps: {"0": 0, "1": 20, "2": 34, "3": 47, "4": 62, "5": 75, "6": 91, "7": 103, "8": 115, "9": 133, "10": 158, "11": 170, "12": 190, "13": 206, "14": 230, "15": 241, "16": 249, "17": 266, "18": 289, "19": 306, "20": 318, "21": 334, "22": 346, "23": 365, "24": 385, "25": 399, "26": 408, "27": 423, "28": 438, "29": 452, "30": 472, "31": 498, "32": 525, "33": 542, "34": 559, "35": 570, "36": 582, "37": 594, "38": 609, "39": 625, "40": 643, "41": 663, "42": 690, "43": 706, "44": 714, "45": 734, "46": 757, "47": 768, "48": 785, "49": 805, "50": 812, "51": 828}
---

**Dave Jones:** Hi, in a recent, uh, teardown power supply teardown I mentioned, um, that a cheap, simple, and very common way to, um, decrease the resistance and increase the current handling capability of PCB traces is to leave the solder mask off and, uh, let the wave solder apply extra solder to the trace like this.

**Dave Jones:** And, uh, there were quite a few, uh, people who said, "Well, that's really not going to make a huge difference at all. Um, if anything." Well, and, uh, I I I think they're wrong.

**Dave Jones:** It's a common technique that's been used for a long time. But, you know, I don't know if anyone's actually done the numbers on it. So, I thought I'd do a video actually, uh, trying to measure the difference.

**Dave Jones:** Unfortunately, Mike at Mike's Electric Stuff has beat me to it. He's already done a video, uh, checking just this. He, uh, did some measurements, uh, before and after he took off, um, the solder, actually solder wicked it off, and, uh, did some measurements.

**Dave Jones:** So, I think he got a figure of like, uh, 40 to 50, uh, percent, um, decrease in the, uh, resistance of the, uh, trace due to the, uh, solder on there, which is quite significant.

**Dave Jones:** Um, you know, so, it it definitely does make a difference as you'd expect. Uh, but, I, uh, noticed an issue with, uh, Mike's video in that, obviously, um, he started with a board like this which already had the, uh, solder on it.

**Dave Jones:** And, as you can see, it's it's can be quite inconsistent this process. Um, you know, some like in some areas it'll be big and lumpy, others will be very thinly coated like that.

**Dave Jones:** So, you know, it's a very hit-and-miss, uh, thing, but it is a cheap and simple way to do it. Anyway, Mike, uh, started with a board like this with the solder already on it, and then went to wick it off and remove it all.

**Dave Jones:** And, um, I think that's, you know, a back-to-front way to do it and can incre- and can probably, um, have significant, um, error involved in there cuz I don't think there's any way you can possibly solder wick off all of the, uh, solder on there and be left with your original copper.

**Dave Jones:** Because copper is only standard copper on a board like this is only, uh, 1 oz, uh, copper and, uh, that is 35 microns thick. It's very, very thin. So, I thought the correct way to do it is to, uh, or a more accurate, uh, way so we can get some more measurement data is to start off with a standard 1 oz copper-clad board with a single trace of

**Dave Jones:** a known, uh, thickness like this and, uh, then take some measurements of that, of course, and then add the solder to it and see what the change is. And that should give us, um, more accurate, uh, readings than what Mike got.

**Dave Jones:** So, let's give it a go. I've got some, uh, final uh, Veroboard here and it's, uh, part number 147899 and I had to look up the, uh, MSDS, actually, material safety data sheet to get the thickness, but it is standard 1 oz 35-micron copper.

**Dave Jones:** So, let's give it a go. And as I mentioned in, uh, my power supply video and, uh, Mike mentioned as well, there are other ways, uh, to do it apart from, uh, add solder to the traces and how to get increased current handling capability, um, in your traces.

**Dave Jones:** That's to use thicker copper, either 2 oz or, uh, even 4 oz, uh, copper. But, the issue with that is, A, it's very expensive to do and, uh, B, uh, if you've got a mix of very high-power power supply stuff on one part of your board and very, uh, dense stuff on another part of your board, say you've got a BGA or a, you know, very fine pitch quad flat pack or

**Dave Jones:** something like that, Um, then etching away 4 oz copper, um, you know, to those sort of tolerances required for very fine traces can be very, uh, difficult if not impossible.

**Dave Jones:** So, you can't sort of mix and match high-power stuff with high-density stuff using that thick copper. So, this is a real cheap and, uh, simple way to do it.

**Dave Jones:** And of course, that's the reason most manufacturers will do this, very common in power supplies, is because it's cheap, simple, and you effectively get it for free. Now, of course, to do these measurements properly, you've got to use what's called four-wire resistance measurement.

**Dave Jones:** Um, and I've, uh, done this in previous videos. You've seen it. And, uh, we'll do, uh, two different, uh, methods of four-wire. We'll use my, uh, HP 3478A, and then we'll also, um, do the manual method of, uh, passing a constant current through and measuring the voltage drop with a multimeter just to get, you know, two different measurements to make sure we're consistent.

**Dave Jones:** So, a four-wire measurement basically means that, uh, you have a drive wire, which is this one, and then you have a sense wire as well. So, that, um, when it's driving current through these leads, you're going to get a voltage drop and an error along these leads.

**Dave Jones:** But, if you have this sense wire, which is tapped right at the same point like that, then you're measuring the voltage directly off there. And because there's no current, you've got a high-impedance multimeter measuring this, there's no voltage drop along this wire.

**Dave Jones:** It measures the exact uh, resi- the exact voltage drop across your trace like that. So, it is the most accurate way to measure resistance like this. And of course, we've got that on both ends of the board like that.

**Dave Jones:** So, we've got one at that end and one at this end, four wires. We can drive it with a constant, uh, current or with a, uh, a four-wire multimeter like a HP 3478A.

**Dave Jones:** So, we've got two drive wires and two sense wires. Let's give it a go. And just for the record, the length here from uh sense point to sense point is uh 358 mm or thereabouts.

**Dave Jones:** The uh thickness is approximately 4.2 mm. And for those curious to know the difference between four-wire and two-wire mode, if we switch to two-wire, we get much higher 220 uh 212 mΩ because all of the uh it's measuring all this wire in series with it.

**Dave Jones:** But, you switch to four-wire and it effectively cancels out any resistance in these wires and the contacts and things like that. Actually, that's come down a bit maybe due to uh you know, it was still a bit warm from the soldering, perhaps.

**Dave Jones:** Anyway, 51 mΩ. And what I've got here, I'm now passing a constant current of 1 amp through this uh trace and I'm measuring the voltage drop from the sense wires.

**Dave Jones:** And as you can see, 51 mV for 1 amp. Use Ohm's law, that's 51 mΩ. It's spot-on to our HP 3478A meter uh four-wire terminal resistance measurement. So, we've got two different uh measurements confirmed.

**Dave Jones:** This trace is definitely 51 mΩ. Now, we can add some solder, see what the difference is. And the solder I'm using today will be standard Multicore brand 60/40. None of this lead-free rubbish, just your traditional 60/40.

**Dave Jones:** So, let's give it a go. Um I'm not going to go all the way right to the end right to the tip there because I don't want to, you know, upset my uh uh measurement um upset my connection there.

**Dave Jones:** So, I'll go most of the way and I'll put a very thin coat on to begin with. So, let's give it a go. This will be a probably, you know, a thin and then I'll spread it along and you'll see the resistance jump all over the place due to once this copper heats up, it changes its resistance, of course, and so does the solder.

**Dave Jones:** So, really we need to let it settle down, but we've got 51 milliohms there, so let's let's give it a go. Well, that's rather surprising. It's not uh nearly as much as I thought it would be.

**Dave Jones:** It's a relatively thin coating on here, but I get a basically it's dropped to 43.2 43.3 milliohms and I calculate that as basically a 15% decrease in resistance and uh uh or a 17% increase if you want to uh do the way Mike did and then I checked Mike's numbers again and he got a 40% increase.

**Dave Jones:** So, mine's only 17%. He got 40, so he must have had a lot more solder on there, I can only presume. Or he got a 28% decrease. I'm getting a 17 15% decrease, but it's still it's relatively significant considering that you get it for free.

**Dave Jones:** Like you don't actually, you know, you have to all you have to do is leave your solder mask off and it's you certainly wouldn't rely on the fact uh cuz it wouldn't be consistent, but anyway, I think what I'm going to do is put another layer on, make it really thick and globby and see what we get.

**Dave Jones:** And it's it's it's actually cooled down. By the way, it's as you can see, it's pretty stable. It took about, you know, a few minutes to cool down at least, so let's apply some more solder.

**Dave Jones:** And you can see my coating there. It is relatively uh thin. It prob- maybe looks a bit thicker than what I on camera perhaps, but yeah, I let's let's add it.

**Dave Jones:** Let's go much clumpier like down here. So, I started to add some. Let's do some more even clumpier than that, I think. All right, now we're talking 26.2 miliohms.

**Dave Jones:** So, we've basically that's like a 94% uh increase in the resistance if you're talking in the way Mike did it or a 48% uh decrease in resistance. Uh practically, you know, double and half.

**Dave Jones:** So, and really I don't think my solder is as thick as I'm not sure how that looks on camera, but really I'm not sure it's nearly as thick as what, you know, has accumulated on this board after the wave soldering process.

**Dave Jones:** And, you know, that's that's fairly typical of a board after it's you know, been uh uh wave soldered like that in tin. So, you know, I think yeah, it's basically um we're talking, you know, you halve the resistance um pretty much.

**Dave Jones:** So, that's a better result than what Mike got, much better. He only got a a 40% increase in resistance or a 28% decrease. I'm getting a 50% decrease. And I know what you're thinking, can we get it back to normal and do what Mike did and remove all the solder and get it back to 51 miliohms?

**Dave Jones:** Well, let's give it a try. And that's basically what's left after trying to wick it all off. I could probably get a little bit better than that, but gee, you know, you could do this thing until the cows come home, but there's yeah, trust me, there's really not much uh solder left on that at all in terms of physical height anyway.

**Dave Jones:** Okay, I've done my darndest to uh suck all that solder off the strip and we're back to 52 milliohms or thereabouts. Going to be a little bit of error in there, but I and I may have even you know because I physically scraped along with the stuff.

**Dave Jones:** So maybe it actually takes off you know a little bit of copper in there or something. You know, maybe it even leaches it out. Maybe it even leaches a bit of copper out.

**Dave Jones:** I don't know the chemical process precisely, but anyway, we're basically back to where we were. So that pretty much validates Mike's technique of starting out and removing the solder as well, but I think our one was a little bit more accurate because we did start off with the known quantity with the 1 oz copper.

**Dave Jones:** So there you have it. Tinning a PCB trace. We've done some I think reasonably controlled measurements here. So you can be pretty confident of these results. We got anywhere from a 15% to a 50% decrease, a halving of the resistance by just tinning the trace with 60/40 lead solder.

**Dave Jones:** It It'll differ with the tin stuff, but that's a nice ballpark. That 50% figure Mike got a figure of 28% decrease in resistance. We were able to get better than that.

**Dave Jones:** So there you go. It's going to be somewhere within that range. So it does actually make a difference and considering that you can do this for free by just removing the solder mask and getting the solder you know put on there by the wave soldering process, it's you know, it's not a bad technique.

**Dave Jones:** It's and that's why people have used it for a long time. It's cheap. Well, it's effectively free. So and it does work, but you can't rely on it though because as you see there is a quite a big spread in there and even if you leave a very thin coat of solder on there, it it really doesn't do much at all.

**Dave Jones:** You've got to have at least a, you know, a reasonable amount on there. When you try to suck it all off, it basically goes back to the same as the copper.

**Dave Jones:** But, that's very interesting result. I don't know if anyone's actually done that before. So, it's pretty much confirms Mike's results as well. So, there you have it. Some conclusive results and a bit of an industry rule of thumb there.

**Dave Jones:** I like it. If you want to discuss it, jump on over to the EEVblog forum. And if you liked it, please give it a thumbs up. Catch you next time.
