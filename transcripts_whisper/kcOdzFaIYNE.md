---
video_id: kcOdzFaIYNE
title: EEVblog #683 - Rigol DS1000Z & DS2000 Oscilloscope Jitter Problems
url: https://www.youtube.com/watch?v=kcOdzFaIYNE
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 17, "2": 37, "3": 53, "4": 69, "5": 85, "6": 109, "7": 129, "8": 149, "9": 173, "10": 189, "11": 205, "12": 221, "13": 237, "14": 265, "15": 281, "16": 301, "17": 317, "18": 337, "19": 353, "20": 369, "21": 385, "22": 401, "23": 417, "24": 433, "25": 453, "26": 469, "27": 485, "28": 501, "29": 525, "30": 541, "31": 561, "32": 577, "33": 597, "34": 625, "35": 641, "36": 661, "37": 681, "38": 697, "39": 717, "40": 741, "41": 761, "42": 781, "43": 797, "44": 813, "45": 833, "46": 853, "47": 873, "48": 893, "49": 913, "50": 933, "51": 949}
---

**Dave Jones:** Hi, I got an email from fellow video blogger Mads from the YouTube channel ECProjects. And if you haven't seen his channel, I'll link it in down below, check it out. Anyway, he emailed me with a problem that he found, and he posted a video on this which I'll also link in as well.

**Dave Jones:** He found a quite a serious problem in his Rigol 1104Z. And well, I've got the same one, essentially the same one, the DS1050. He has 1054Z here. So I thought we'd reproduce the problem. Now, rather than try and explain it all, I'll just do it.

**Dave Jones:** And see if I can reproduce it on mine. So what I've got here is just a function generator generating a square wave, 5 volt peak to peak, whatever, at 20 megahertz. And I'm feeding that into our scope and no problems whatsoever. I mean, it's exactly what you'd

**Dave Jones:** expect. You know, it's not terminated properly, doesn't matter. But there's no jitter in that signal whatsoever. I'm sure everyone can agree on that, and I've got no nothing turned on, I've got no high-res mode, no averaging, no nothing. So that's a very clean signal.

**Dave Jones:** It's triggered perfectly fine, everything's hunky-dory. And our trigger point is right in the middle there, and that's going to matter, I'll tell you why in a minute. We've got our hardware frequency counter there, 20 megahertz, no problem with no delay whatsoever because our trigger point's in the middle.

**Dave Jones:** Now, if I take that right out like this, and I adjust my horizontal and move my trigger point in this direction, and if we move it over by precisely 5 microseconds, and then we zoom in again, whoop, wrong control, dull, so the trigger point is now way off to that side,

**Dave Jones:** so it's now, we're displaying the waveform 5 microseconds after that trigger point. Look at this, we're getting a little bit of jitter here, and that's not too bad at all, but it is there. You can see that there's some jitter there. Now this isn't nearly as bad as the one

**Dave Jones:** that Mad saw on his one. I'll show you a shot of that, and look, it is absolutely shocking, right? And that's what he got with the exact same conditions on his 1104Z. Okay, so we've seen that. Now, watch this. We'll go out even further, we'll go, we'll double that time period

**Dave Jones:** to 10 microseconds. There it is. And we'll go right in, bingo! The jitter's gone. And you might be able to see where I'm going here. Let's move this trigger point even further over to, you guessed it, 15 microseconds. And we're going to be precise here, there we go, 15.000 microseconds.

**Dave Jones:** Ah, I hit the bloody vertical control again. Twit. Look, our jitter is back. And what do you think it's going to do at 20 microseconds? Well, let's find out. I think you've already guessed it. Bingo, it's vanished. Look at that. We're still, our signal is just fine.

**Dave Jones:** And of course we could, like, you know, scroll this thing right through and we'd eventually get there, but it's easier to zoom out like this. And if we go up to 25 microseconds, you guessed it, the jitter's back. And we can keep on

**Dave Jones:** going and going and going, and it alternates in those 5 microsecond time periods between jitter and not jitter. But as I said, mine isn't, so it's kind of confirmed, right, I've confirmed it on mine that there is some jitter there, but it's not nearly as bad as Mads has seen.

**Dave Jones:** And he seems to think, based on some of his viewers have been reporting in, that, yeah, it seems to possibly maybe after a certain manufacturing date, some units do it really bad, and mines might be an early unit or something, doesn't do it nearly as bad, but it's there.

**Dave Jones:** ... ... And for those playing along at home, I'm running software version 4.01.SP2, and I'm running hardware version 1.1. And if I jump back from 25 microseconds right back to 0, watch, it'll just vanish. Look at that. Gonski. And just to see if it's some sort of, you know,

**Dave Jones:** beat thing against, like, the input frequency versus the input sampling clock, which it shouldn't be, because like, it's got nothing to do with the period, it's all to do with the, you know, the transition time of this thing. But anyway, just for kicks, I set it to

**Dave Jones:** 1.21 megahertz here, and yes, I've delayed it by 5 microseconds, and you can see that we are getting some jitter there. Look at that. Here we go. And I'll instantly switch it right back to 0. There we go. Look. And there you go, at practically 10 microseconds, I've just

**Dave Jones:** moved it so you can see it a bit, no problems whatsoever. But you guessed it, at around about 15 microseconds, it's back! And I've now got an 11.1 megahertz signal just for kicks, 5 microseconds out, look at that jitter, I'll reset that back to 0,

**Dave Jones:** no problems whatsoever. And at 10 microseconds, yep, basically nothing there. Back to 5 microseconds again, there it is, I'll switch it back to 0. So that is weird, there's something happening it's like there's, like some frequency modulation jitter thing happening at those 5 microsecond

**Dave Jones:** time intervals, like that. It just alternates jitter, no jitter, jitter, no jitter. So it's like there's, you know, it's got to be it's not the external signal, okay? I'm using a very clean external signal verified on another scope, not a problem whatsoever, I'll show you that in a second

**Dave Jones:** and as other, do other scopes do it or not? Or is it just the Rigol 1000? But anyway, it's not the external signal, so it's internal to the Rigol DS1000Z series, they're all the same of course, so any model in the series might

**Dave Jones:** have this to some extent. Mine's not that bad, Mads' one's really awful, so I'm not sure what's going on here. It's maybe a combination of bad clock jitter of the main reference clock in here, but I think it more has to do with

**Dave Jones:** the, maybe it's introduced, it's trigger jitter of course, so not just the clock, but maybe a combination of that might have a little bit to do with it. Or something maybe to do with the trigger hardware and how they're implementing that, possibly in one of the FPGAs or something like that

**Dave Jones:** is just causing it to, causing it to muck up and give that jitter but right on there, it's clean and then every 10 microsecond time period it's clean, and if you actually scrolled it through, you'd be able to if you were patient enough, you'd be able to see it get progressively worse

**Dave Jones:** and then better, and then worse, and then better. Some sort of modulation, jitter modulation happening there. And does the venerable old Rygold DS1052E do it? Well, that's at no offset and look, it looks pretty clean, no problems whatsoever. And if we go out by

**Dave Jones:** exactly 5 microseconds there, nope. No jitter at all. And does the Rygold DS2000 series scope do it? Well, look at that, that's at no offset whatsoever, beautifully clean. And that's at 5 microseconds offset, beautifully clean and sharp again, no problems at all on the DS2000 series.

**Dave Jones:** Okay, so we have a potentially very serious trigger jitter issue there, and Rygold really need to look into that. So anyway, I can't do any, I haven't got time to do any more experiments on that, but I just wanted to show you something even

**Dave Jones:** potentially a hell of a lot worse that I discovered while I was having a quick play around with this before. Here we go, we've got the same 20 MHz signal we've got no delay whatsoever, so it's all beautifully sharp, everyone's hunky-dory. But if we go into the trigger menu, and we go down to settings

**Dave Jones:** down here, we're at DC coupling at the moment, and all the other scopes have been DC coupled as well for the triggering. What happens if we switch that to AC? Watch this! Crikey! Look at that! What's going on? You've got to be shitting me!

**Dave Jones:** What is this massive amount of jitter? And you know, no, it's not the trigger point, there's nothing weird going on, we're going to set that to mid-point. There's nothing else weird going on there at all. There's no filters on, right? It's just your pure AC

**Dave Jones:** coupling. And I thought, this has got to be a pebcac, right? It's got to be, I'm just doing something incredibly dumb. But no! I've double-checked! This is just basic from AC to DC coupling. It goes from perfectly triggered to this massive amount of trigger jitter.

**Dave Jones:** What the? And you'd think it's just a square wave or something. No, sine wave at frequency. Let's go down to 1 MHz, shall we? Here we go. It looks like okay, but square wave, look at that. We're still getting it. Look at that.

**Dave Jones:** And we can even go down to 1 kHz. There we go, we're right down now to 1 kHz, of course we're a square wave, so we've got a rapid rise time still there. Look at that trigger jitter! And there's nothing I can do to get rid of that.

**Dave Jones:** Absolutely nothing. It's just, it's inherent in the AC coupling mode of this scope. Unbelievable, that is awful! I can't believe, well, I haven't played with this one much, but I never saw it, and well, let's go see if our other scopes do it.

**Dave Jones:** Here we go, the venerable DS1052E setup, DC coupling, let's switch it to AC. Nope, no problems whatsoever. Works a treat. Look at that, perfectly triggered. Okay, the DS2000 series scope, let's go into the trigger menu here, go into settings, AC coupling. Whoa! Look at that!

**Dave Jones:** Man, that's like potentially worse than the Rygo 1000 series. Look at that, that is just shocking. Now once again, I've got like 50% level set, I just reset the trigger level, all I'm doing is going from AC to DC coupling. That's it. Perfectly triggered.

**Dave Jones:** Garbage! What the hell is that? And once again, likewise, you'll see it at 1 kHz for example. So we can go down to 1 kHz and get out a bit, there we go. That's a 1 kHz signal. Look at that trigger jitter. Just due to AC and DC, absolutely perfect.

**Dave Jones:** AC, garbage. I can't believe I've never noticed this on the Rygo DS2000. I don't believe there's any other reports out there, I'm not aware of any, there might be, but AC coupling mode? It basically does not work, look at the trigger jitter on that!

**Dave Jones:** It's ridiculous. And I think we need a couple more scopes to verify this. This ought to do it. And what about our Agilent 3000X series? We've got DC coupling on at the moment, let's switch it to AC. Heh, of course it works. And how does the Agilent go

**Dave Jones:** at that offset issue again? Well, let's try it. Okay, we're now 5 microseconds delayed there. Let's go in, yep, no problems whatsoever, exactly the same as bingo, we've gone back to 0 there, no problems. And what about a GW Instec GDS2304 300MHz scope?

**Dave Jones:** There's our 0 delay signal, no problems whatsoever, it's just beautiful. And 5 microseconds offset there, beautiful, no problems. We've got DC coupled at the moment, what happens if we go to AC coupled? Heh, of course it works. And what about our Tektronix MDO3000 scope?

**Dave Jones:** Look at that, nice and steady, rock solid at 0 delay. We've got ourselves 5 microseconds delay there. And as you'd expect, works a treat. And trigger coupling, we've got DC at the moment, let's switch to AC. Not a problem! And it still does it of course, it doesn't matter

**Dave Jones:** whether you're positive or negative slope or whether you get it in both directions like that, it's still doing it. It's just unbelievable, what the hell is going on with this? It's just ridiculous, that one's actually not even going in both that's not even going in both directions, there we go, center it, no

**Dave Jones:** no, can't even do that, can't even get the dual slope, the positive and negative edge slope. What the? Actually, is that another thing wrong with the DS2000? I've turned it back to DC coupling, I've got the dual slope, like both edges here, triggering, and it's not doing it.

**Dave Jones:** It works fine on the 1000Z, apart from the ridiculous amount of trigger jitter, look at that! But, what the, oh, is that 3 problems? Gee, I don't know, I just found that one then. I, look, oh, I'm going to have a brain aneurysm here.

**Dave Jones:** Anyway, Rigol has some serious explaining to do with, A, that frequency modulated trigger jitter that Mads found, and yeah, what the hell is going on there? It doesn't do it on the old 1052E, not a problem at all. It does it on both the

**Dave Jones:** 2000 and the 1000Z series, because they're both new architecture scopes. Maybe there's something inherently wrong with that. But a huge deal is the damn AC coupling! What's going on there? Unbelievable. So yeah, that's all I've got time for. Sorry, I don't have time

**Dave Jones:** to actually investigate this, I'm just throwing this out there. This is what I've found, this is what Mads found, and yeah, there's something like going on here. If you, if anyone out there has these Rigol scopes, please confirm what sort of modulated trigger jitter you get with that 5 microsecond offset,

**Dave Jones:** a few people are calling it the 5 microsecond jitter issue. Which is, yep, a reasonable name for it. And the AC coupling! That's just ridiculous! Anyway, Rigol, please look into it, something's seriously wrong here with the, I mean, these are, were kick-ass scopes, or they still are, apart from this issue.

**Dave Jones:** I mean, I was just doing the review on this, I've already uploaded an hour and 15 minute review saying how wonderful this thing is, but I haven't done my second summary video yet, and I hadn't done my performance tests on it either. Whether or not I would have detected that in the performance

**Dave Jones:** tests, I don't know. Whether or not I lucked out and maybe, you know, tested the AC trigger coupling, I would have found that, because that sticks out like dog's hind leg, it's ridiculous! Anyway, I've had enough. So yeah, please links down below to discuss this, and yeah, Rigol, I'm sure

**Dave Jones:** they'll look into it and they'll get back to us in due course. They bloody well want to because I can't recommend this yet until such time as this sticks. Is it a hardware issue? Is it a, like a software, like a firmware FPGA trigger issue or something like that?

**Dave Jones:** Don't know. That they can fix in with the software patch, so, I don't know. Anyway, if you liked the video, please give it a big thumbs up, and give these Rigol scopes a thumbs down for this jitter problem. Anyway, catch you next time.
