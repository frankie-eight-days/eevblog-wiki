---
video_id: wLcdZjFuho0
title: EEVblog #1312 - Siglent Oscilloscopes CRIPPLING History Mode!
url: https://www.youtube.com/watch?v=wLcdZjFuho0
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 32, "3": 45, "4": 59, "5": 75, "6": 92, "7": 106, "8": 118, "9": 131, "10": 144, "11": 157, "12": 173, "13": 189, "14": 207, "15": 221, "16": 234, "17": 247, "18": 262, "19": 274, "20": 290, "21": 304, "22": 317, "23": 332, "24": 346, "25": 361, "26": 375, "27": 391, "28": 404, "29": 419, "30": 430, "31": 446, "32": 459, "33": 473, "34": 488, "35": 500, "36": 512, "37": 525, "38": 544}
---

**Dave Jones:** Hi, this is just a quick follow-up video to my main channel video on the oscilloscope zoom out feature, I guess, which is on most scopes, but it's not on siglant scopes, and I believe Lacroy scopes work the same way as well, but I

**Dave Jones:** don't uh have one. So, and when you press uh stop here, if you zoom out on the time base, of course, there's no there's actually no data captured either side of that. So uh it seems fairly particular to sign scopes. I think Pico

**Dave Jones:** Scope might do it as well. Someone mentioned that on the forum, but like most other scopes on the market will actually uh use the full memory depth and capture. But you can see down here, even though we've got 200 meg memory

**Dave Jones:** depth set, which is absolutely fantastic to have 200 meg, it's only 200k points down here. And to go to the uh 200 meg, I've really got to go all the way down to where is it? There you go. Got it all

**Dave Jones:** at 20 milliseconds per division before it'll uh use all 200 megp points there. So you got this 200 megpoint scope, which is fantastic. But at say which is what I was using uh here as an example, five microsconds per division, you only

**Dave Jones:** get 100k points. So, if it's got 200 mega memory, why is it only giving and why is it only using 100k points? And it does exactly the same thing in singleshot uh mode as well. You would think that oh, if you press single shot,

**Dave Jones:** it should use all the full 200 meg, but it doesn't. And I've I've realized what Sigant are actually doing here. This is actually a deliberate tradeoff they've made with the history function down here. Here there's a history button here

**Dave Jones:** and you'll notice that it's off. And the history is a feature where it captures multiple frames of waveform. So each uh trigger cycle will capture a frame put in memory so that you can actually replay frames. It's a really handy

**Dave Jones:** feature on modern uh scopes. Absolutely fantastic. Siglin's got it. Most other modern scopes have a history feature. Nothing unusual about that at all. But what Siglin have done is determined that it's so important that they have to use

**Dave Jones:** it all the time, even when you've got it switched off. Look phys like I can physically switch it on. History mode on. Okay. And you can see that it's automatically uh stopped here. It's automatically gone into stop mode. And

**Dave Jones:** then we can actually go through the different frames. You can see that it's got, you know, n you know 2,000 almost 2,000 different frames. And that's what history mode does. Once again, nothing uh, you know, unusual about this. This

**Dave Jones:** is how it works on every scope. But even if I turn history mode off, this is off here. It's still in history mode. Watch this. If I go stop like that, we can actually still go into even though

**Dave Jones:** history mode is off here, we can still actually turn on history mode and it's still captured that data. Yes, that data is actually really there because if I uh do this and I Yep. and I go stop like

**Dave Jones:** that and then we go into history and turn it on. You'll notice like that wasn't residual data from last time. That's really data that it's so it's using uh history mode continuously. Cichl have determined and or LCROY determined because Siglant actually make

**Dave Jones:** uh manufacturer. They're the OEM for a lot of uh for LCROY's like lowerend uh scopes. But anyway, they've determined that history mode's so important. you, we're going to sacrifice that 200 meg sample memory, that fantastic 200 meg of

**Dave Jones:** memory, and we're going to use it all the time. And you're only allowed 100k points at five microsconds per division. It changes. And if you go, of course, all the way, look, 400 points down here at 20 nconds per to 200 points. where if

**Dave Jones:** you use something like the uh keysite that we saw over here, it's only got a lousy 4meg of memory, which is, you know, not much these not a huge amount these days, especially for the price, but it uses the full uh 4meg like down

**Dave Jones:** at these time bases, whereas the seat slot will only use 400 points. It'll actually go down to like 10 points, right? At 500 pics per you, you only get 10 samples on there. It looks like there's more because it's not in uh dot

**Dave Jones:** mode. Uh, if we go into dots, you can see, yeah, they're the physical. Why do they look like that? Oh, because it's it's it's re-triggering. If we stop it, you'll only see Oh, I don't know if you can see that, but yeah, you've only got

**Dave Jones:** 20 samples in there. So, yeah. Um, this is just like [laughter] they've decided that we've got all that memory, but no, no, we can't use it. That's what they've done. They've made the trade-off. This history mode is always on, and as far as I'm aware,

**Dave Jones:** please correct me in the comments down below. if I'm uh wrong and I've looked at the manual and it's not really clear that it does actually say that like history it does imply that history mode's always there but it's it's not really clear and

**Dave Jones:** they're certainly not clear that you're trading off that 200 meg of memory um they're pretty exclusively for you know these signant scopes on the market not sure about all models but I think it's like this is a Sigant thing and a LCROY

**Dave Jones:** thing so yeah they're making that tradeoff it's just Ah, you're giving away all that 200meg memory depth. And and by the way, it you would think that for run stop mode. Okay, fair enough. I can actually think, okay, this is

**Dave Jones:** probably not an unreasonable choice. It's actually could be very helpful to have it always on, right? So, when you do run stop, okay, no worries, right? You got all the frames in there. But when you decide that you set up your

**Dave Jones:** horizontal trigger, your vertical uh horizontal trigger, set up your horizontal, you set up your trigger, you set up your vertical, everything else, you're ready to capture your signal and you do your singleshot capture. It should switch out of this, you know, 40k

**Dave Jones:** points here or 100k points or whatever it is based on the time base and give you your full 200 meg, which we actually have set. I've deliberately set the 200 meg, but even in singleshot capture mode, it will not do it. Like because we

**Dave Jones:** just hit single shot capture, right? Let's do it again. There we go. Right. Single shot capture. No, it it actually disables it in single stop mode, but doesn't then give you the advantage of the extra deep memory. Why? That's an

**Dave Jones:** insane choice. Why would you do that? I don't get it. Please, somebody [laughter] at Sigland who designed this thing, please tell me why you would make that choice. I fair enough. I'm going to I'm going to give it to him in run stop

**Dave Jones:** mode. Okay. Automatic history mode. You can Some people might even say that's kind of cool, but when you hit single shot mode, no. Damn it. I I would want my full 200 meg of memory or whatever memory depth I've chosen there. I I

**Dave Jones:** can't see a reason why you wouldn't do that. And a couple of people asked about the uh acquisition mode here. Does that have any effect? The fast isn't because we've only got the limited memory because we're on fast mode. Well, no.

**Dave Jones:** The slow mode actually makes no difference at all. We can, you know, stop that and it works exactly uh the same way. We can single shot capture that. It works exactly the same way. The fact the slow mode seems to like do

**Dave Jones:** nothing else apart from just slow down the updating. you don't get any extra benefit in terms of memory or anything else. The uh the history mode and everything works exactly the same in slow or fast mode. And it basically uh

**Dave Jones:** implies that in the manual as well. Anyway, rant over, please. But at least we know now why um they don't do the zoom out thing, of course. And and by the way, yes, if you um if you go into

**Dave Jones:** history mode and deliberately like have it on and no, it turns off. See, it it's confusing. Like you go into here, it's off. You would think that the history features off, but it's not. It's still continuously s they're using up all that

**Dave Jones:** 200 mega memory to capture all those different frames in there continuously. Bam, bam, bam, bam, bam, bam, bam, and it fills it up. And when you stop it, bingo. The uh frames are wh you got to hit the history button. The frames are

**Dave Jones:** instantly there in the 200. So they are using the 200 mega memory just not in the way you want them to in [laughter] most cases. So and and no you can't there there is no data. There's only the

**Dave Jones:** uh uh in this particular case based on this time base 100,000 points in there for every frame. So the whole 200 they're using the whole 200 meg but they're using you know taking frames of this 100k 100k 100k 100k and just

**Dave Jones:** filling up with uh you know 1,987 frames there. So, uh, yeah. Anyway, that's the tradeoff you get with the Siglin and I believe the Lacroy as well, but please correct me down below. Anyway, there you go. I I Yeah. No, no, especially in

**Dave Jones:** single shot mode. H, I'll shut up now. Catch you next time. [music]
