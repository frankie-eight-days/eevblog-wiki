---
video_id: bVxDibdosdI
title: EEVblog #1311 - Can Your Oscilloscope Zoom OUT?
url: https://www.youtube.com/watch?v=bVxDibdosdI
source: youtube-asr
timestamps: {"0": 0, "1": 16, "2": 29, "3": 41, "4": 54, "5": 65, "6": 77, "7": 93, "8": 110, "9": 123, "10": 136, "11": 151, "12": 170, "13": 185, "14": 199, "15": 213, "16": 226, "17": 239, "18": 256, "19": 268, "20": 287, "21": 302, "22": 317, "23": 335, "24": 355, "25": 371, "26": 383, "27": 395, "28": 408, "29": 422, "30": 437, "31": 449, "32": 463, "33": 478, "34": 492, "35": 506, "36": 524, "37": 538, "38": 552, "39": 567, "40": 585, "41": 602, "42": 617, "43": 629, "44": 640, "45": 651, "46": 665, "47": 677, "48": 690, "49": 702, "50": 719, "51": 731, "52": 747, "53": 763, "54": 778, "55": 792, "56": 806, "57": 823, "58": 836, "59": 848, "60": 861, "61": 873, "62": 884, "63": 897, "64": 910, "65": 924, "66": 936, "67": 953, "68": 971, "69": 987, "70": 1003, "71": 1020, "72": 1035, "73": 1052, "74": 1067, "75": 1082, "76": 1100, "77": 1111, "78": 1126, "79": 1139, "80": 1154, "81": 1169, "82": 1186, "83": 1204, "84": 1221, "85": 1234, "86": 1246, "87": 1259, "88": 1272, "89": 1284, "90": 1296}
---

**Dave Jones:** Hi, the humble oscilloscope. You're used to using it every day and if you're doing, say, troubleshooting a specific signal that you're trying to measure and seeing what's going on your circuit because it might be playing up, you're used to setting up your oscilloscope to

**Dave Jones:** capture a signal. You'll set your horizontal time base to what you want. You'll set your vertical time base to what you want. You'll set your trigger level to exactly what you want and then you it might single shot capture it, for

**Dave Jones:** example, or you might do a run stop and you might even set it to maximum memory depth here, for example, just in case you want to zoom in on the data and see extra detail. And when you hit single

**Dave Jones:** like this, bingo, you've captured your data. Fantastic. And you can zoom in, of course, to your heart's content because you've got a massive 200 meg of memory or whatever it is you've got these days. When I was a boy, jeez. But one thing

**Dave Jones:** you can't do is zoom out. We're at 5 microseconds per division. Take a look at this, of course. We can zoom in and we can see our data and everything. So, you can't see anything in there and you

**Dave Jones:** can't recapture. Let's just say it's a one-off like event, you know, a rare trigger event you're trying to trigger on. This isn't the best example. You've only got this one capture, but you want to see what happened off the screen over

**Dave Jones:** there or off the screen over here. You can't just move your horizontal like that because you've got no more data either side. And I put it that back in the middle and of course you can't zoom out because there's no more capture data

**Dave Jones:** either side of that. So, it's capturing just within the window in there to whatever memory depth you currently set. And you go, "Well, yeah, okay. Fair enough. That's just normal basic scope operation." But what if I said not all scopes

**Dave Jones:** operate this way. So, let's go over to this Keysight over here. Exactly the same signal, exactly the same horizontal, vertical. I've fixed the memory depth. Yes, you can actually do this in the latest stuff firmware upgrade. You can actually fix the memory

**Dave Jones:** depth in digitizer mode on the scope. So, but it doesn't matter whether it's in auto or not. I'm just, you know, having the same thing. And if we single shot capture that, it's exactly the same, right? 5 microseconds per

**Dave Jones:** division. We can zoom in on our data to see that, but we still can't see anything weird going on here. Once again, it'd be nice if we could actually zoom out on this captured data and see something. Well, check it out. We can do

**Dave Jones:** this on the Keysight. And look at this. Looky what we have here. We actually see something. There's a little glitchy in there, isn't there? There you go. A little runt pulse. Aha, got you. But if you didn't know,

**Dave Jones:** hmm, you might have never found this unless you have to recapture again. So, we're at 5 microseconds per division that we captured it at, but our Keysight allows us to go out to 10 microseconds, 20, 50, 100. And we will at 200

**Dave Jones:** microseconds. We will eventually get to a point where, oh, it's at its limit. Hmm. So, why does the Keysight allow us to zoom out and the Siglent doesn't? Well, before we try and answer that question, let's just take a look at how

**Dave Jones:** the Keysight is operating here, okay? We're at the 5 microseconds per division that we were before. And if you run it, yeah, we can see the runt pulse. So, I know this isn't the best example, but you know, just run with me. Let's assume

**Dave Jones:** you had some obscure, you know, thing that you're trying to find and you only had one capture. Then being able to actually stop this thing and zoom out like that on the captured data could actually be handy. But anyway, let's

**Dave Jones:** zoom out and see how far it lets us go. Aha, it only lets us go to 160 microseconds per division. It It actually goes really oddball. Don't worry about the demo mode there. I'm just using the demo mode to actually

**Dave Jones:** generate this run pulse signal. But, only in digitizer mode, okay, with the fixed four meg points, it knows that it can't actually display any more information outside of the screen. So, it's actually not going to let us go any

**Dave Jones:** further than that. It's smart enough, intelligent enough to know that well, I'm not going to show you blank space either side. What do you want to do that for? But, it will do that if you take off digitizer mode and it's just doing

**Dave Jones:** auto memory. That's 5 microseconds per division, and we stop it, okay? It'll go out and bingo, it'll start showing us the black either side. So, that's just an interesting difference. The Keysight scope operates differently in digitizer mode than it does in auto memory depth

**Dave Jones:** mode. And you'll also notice there is actually a difference in the amount of data it captures it in run stop mode as opposed to single mode. Once again, we're at 5 microseconds per division. Nothing peculiar about 5 microseconds. I

**Dave Jones:** just happen to be using that. If we actually press run stop, if we're at in stop mode at 50 microseconds per division, look, it starts showing the black. So, we're only capturing 50, 100, 150, 200, 250, 300, 350, 400

**Dave Jones:** microseconds worth of data. 400 microseconds before of data. Do the exact same thing, but press single. So, same time base setting, same everything. We're in auto memory mode. So, zoom out like this, and 100 microseconds per division. So,

**Dave Jones:** it's gone from 400 to 100, 200, 300, 400, 500, 600, 700, 800. It's doubled the amount of data that we've captured in single shot mode than it does in run mode. So, this is actually particular to the Keysight's scopes and

**Dave Jones:** the MegaZoom 4 ASIC and the capture architecture that they're using inside the scope cuz all scopes are designed differently. They implement capture algorithms differently, the way they use memory, and all things like that. So, scopes do vary in their

**Dave Jones:** operation. So, should you always use single shot capture mode instead of the run stop button if you want to freeze something on the display just in case, you know, you're just wandering into a random lab, start using a scope, and you

**Dave Jones:** don't know, you've never used it before, you have no idea whether or not it has extra memory in single shot capture mode. Which one should you use? Well, it's not as simple as that. Run stop mode actually exists for a reason. If

**Dave Jones:** you've got a very slow time base, like we're in 200 ms per division here, you can see it, right? A really slow updating waveform. If you actually press stop, here we go. If you see something, and then you just oh

**Dave Jones:** oh, saw something, and you press stop, then it actually just freezes it exactly in the middle of the sweep um sweep as in, you know, old school analog scope, but, you know, digitizing sweep, it stops it right then and there,

**Dave Jones:** and displays the existing memory that it already had in the buffer. But, a single shot capture mode, look, if we're part of the way through, you have to sit there and wait, and it'll give you a full acquisition like that. So, the

**Dave Jones:** single will wait for the next trigger point and then give you an entire capture in memory. So, there are different modes, and they exist for a reason. Each one has advantage depending on what you're actually trying to do.

**Dave Jones:** That's why every scope on the market will have a run stop mode and a single button. Now, Keysight actually call this the ping pong memory buffer. That's how they implement the memory inside their MegaZoom 4 ASIC, and I don't have

**Dave Jones:** particular details exactly how they do that. So, why did it actually run out of puff at 50 microseconds per division there? Well, this has to do of course with the amount of memory that we actually have and our sample rate and

**Dave Jones:** our particular time base that we happen to be capturing at. And you'll notice that we're uh sampling at 5 gig samples per second and we're in auto memory depth so we don't the Keysight uh the ASIC is uh quite smart and it'll

**Dave Jones:** use the maximum amount of memory of its 4 meg sample memory maximum that it can uh based on whatever mode and time base and all, you know, everything else you're in. So, let's actually wind this time base back a bit. 10 microseconds,

**Dave Jones:** 20. Watch this gig samples per second. 50. Aha, 50 microseconds per division. We've dropped Well, bloody touch screens. We've dropped down to 2.5 gig samples per second and at a 100, 1.25 gig. You'll notice that it's dropping because uh this thing's only got 4 meg

**Dave Jones:** of memory. So, it has to drop that sample rate because it can't get the maximum 5 gig sample uh per second sample rate at 1 millisecond per division. It just does not have the memory to do it. If this thing had 400

**Dave Jones:** meg of memory, yeah, we could actually probably still go to 100 milli 1 millisecond per division and still get 5 gig samples per second. So, let's go to Dave Cow here at 5 microseconds per division, we get 5 gig samples per

**Dave Jones:** second and we want to work out how much time uh between each sample. So, you just invert your sample rate, 5 gig samples per second. That gives you 200 puff seconds, 200 picoseconds per sample. And if we uh multiply 200

**Dave Jones:** picoseconds by our 4 meg our maximum 4 meg memory depth of this scope, that gives us 800 microseconds. Is that sounding familiar? And also, 200 picoseconds * 2 meg of sample memory is 400 microseconds. Bingo, that's exactly how many divisions we were getting in

**Dave Jones:** this case in uh stop mode. Here, if we go out at 50 microseconds per division, we had 400 microseconds. And as before, in single shot mode, when we go out, we've got eight divisions there * 100, that's our 800 microseconds. So, that's

**Dave Jones:** why we can't get any data outside of there because it we've only got four meg sample four meg sample memory. And this scope just happens to have two different modes uh where you have run stop and single have different memory depths in

**Dave Jones:** auto mode. But Dave, why does the Keysight scope have different memory depths in run stop and single mode? Well, this has to do with as I said this ping pong buffer, which basically they split the memory in two. They've got two

**Dave Jones:** meg up here and two meg down here. This is how they get their fast update rate. They uh fill up uh the top two meg of memory, and then while they're filling up the bottom two meg, they're actually

**Dave Jones:** reading out the top two meg and displaying that on the screen. That's why Keysight is one of the fastest, you know, million waveform updates per second, blah blah blah. A lot of other scopes choose not to do that, so they're

**Dave Jones:** in inherently slower updating. There's other architectural things behind the fast updating as well. And the software is smart enough to know that, well, if you if you're choosing you're the user, if the user chooses to go single shot,

**Dave Jones:** then obviously they've set up all their triggering and their time base and everything's all set up nicely, and they're going to press single. They know exactly User knows exactly what they're doing. So, aha, I don't need the ping

**Dave Jones:** pong memory anymore. I'm just going to give all the memory. So, you'll get in this case the trigger at points in the middle, of course, and you'll get 50% pre and 50% post trigger data. So, it'll switch off, disable the ping pong

**Dave Jones:** memory, and use the entire It's actually quite clever. So, even on the key site that has this ability, it depends on the horizontal time base and the 4 meg of memory we've got in here. If we're on 10

**Dave Jones:** milliseconds per division, we can stop that, but then we can't do anything. Like, it is just limited to the screen length because all of the 4 meg is being used on the screen. There's nothing left to go outside. Even if we go down right

**Dave Jones:** down to 1 nanosecond per division, as fast as this scope will go, and we press stop, we get all that data. We can go actually go all the way out 10 20 We have to get to 50 microseconds per

**Dave Jones:** division before we start coming to guts there because once again, it's the 5 gig samples per second. But, another scope like this Siglent just won't do it because it uses a different architecture, and it's actually plainly visible on the screen. Look, even if we

**Dave Jones:** set this to 200 meg points, right? We've got a huge massive amount of memory here. Have a look down the bottom on the time base, 20K points. Even though it's set to the maximum, you know, this is not auto

**Dave Jones:** memory depth mode. This is manually set to 200 meg. The scope simply will not use that 200 meg. It's only going to use 20K points. So, of course, we're only going to get 20,000 points on that visible area. If we zoom out, you're not

**Dave Jones:** going to get any extra data. You've only got the 20K points in there, even though we have 200 meg of memory. And this one can go right down to 500 picoseconds per division, right? And but we only get 10

**Dave Jones:** points down there. 10, not 10K points, only 10 points whatsoever, even though we're in 200 meg memory depth. To get our 200 meg points, we have to go all the way up to 10 milliseconds per division there. But, of course, if we

**Dave Jones:** stop that, it's only in the visible window. So, why do Siglent and other scope manufacturers do this uh and Keysight do it differently? Well, uh your guess is as good as mine, really. They just implemented their architecture differently, I guess. This hasn't got an

**Dave Jones:** ASIC uh in it. It's got FPGA. There's no reason why they couldn't even like change this in firmware or update the FPGA hardware or or something like that cuz FPGAs are reconfigurable or field programmable gate array. There's no

**Dave Jones:** reason why they couldn't change it to actually um do the same thing cuz you've got 200 meg of memory depth. Surely you can get in the fast updating. But, Keysight can do it. They've got the best of both worlds. They can have the fast

**Dave Jones:** updating and also have capture the data outside of the screen area. But, yeah, only uh the likes of Siglent and other manufacturers would have to get back to us and say, "No, the reason we don't do this is because X." And I'm sure there's

**Dave Jones:** uh some reason. Or if they say, "Oh, yeah, okay. That's kind of sort of useless." Or because this is not a feature that you would actually uh rely upon all the time. It's nice if your particular scope has it, of course, but

**Dave Jones:** how you regularly use a scope is based on what's on the screen. As I said, you set up your time base, your vertical, you set up your trigger level, trigger pattern, whatever you want to uh do. You set it up and then you capture your

**Dave Jones:** data. And usually in most cases, if you want to see what's outside of uh that screen, then you recapture at a uh longer time base. It's no big deal. That's how people have been using scopes for generations. So, you know, it like

**Dave Jones:** this is just a little interesting tidbit. So, it's not a showstopper. Like, you wouldn't not buy a scope because it doesn't have this feature. Anyway, there's much about this uh there's much debated about this over on the EEVblog forum, which is course a

**Dave Jones:** test equipment central on the internet. There's just lots of test equipment nerds over there uh getting into the intricacies of all this, and it's quite fascinating. But, Keysight aren't the only ones that do it this way. Tecktronix do it as well. I don't know

**Dave Jones:** about in all models. Somebody on the forum said that they didn't, but you know, the same signal run signal again 4 microseconds cuz they do 1 2 4 sequence instead of 1 2 5. If we stop that, we

**Dave Jones:** can zoom out 10 microseconds, 20, 40, 100, 200 microseconds per division. Bingo. And we're running 10 meg points here. And if we run the numbers here, 2.5 gig samples per second, 400 pico times 10 meg is 4 milliseconds. So, in

**Dave Jones:** theory, we should get 4 milliseconds worth of data if they're not doing some ping-pongy type thing, but we don't. Five divisions times 400 microseconds, that's 2 milliseconds instead of 4 milliseconds. So, Tecktronix must be doing the same ping-pongy type thing for

**Dave Jones:** the acquisition. But unfortunately, their update rate is just atrocious. So, yeah, they're famous for it. So, if we go all the way down to 400 picoseconds per division, and we press stop, you should be able to go right up.

**Dave Jones:** Yep, look at that. Use our full 10 meg points till we eventually get to our black. And Rohde & Schwarz use the Schwarz look. 2.5 gig samples per second, 5 microseconds, same signal. Stop. Change the horizontal time base.

**Dave Jones:** Nope, Rohde & Schwarz don't do it either. We'll just do single shot capture on that. And nope. But that's on auto record length. 150.15 K samples per second. Anyway, let's go to the full 20 meg samples per second.

**Dave Jones:** Stop. Go out. Ta-da! If you fix it, it does. So, depends on what scope you've got. Some scopes won't do it on auto mode. The Keysight does it on auto mode, but ones like the Rohde & Schwarz, this is

**Dave Jones:** looks like can be an advantage to setting fixed memory size. Does GW Instek do it? Let's go. Yep, it does. Look at that. Nice. We're at uh 2 gig sample per second there. And where's the memory depth? Is that

**Dave Jones:** displayed there? I don't think it is. That's a bummer. But we go into the acquire menu there. There you go. It worked It does that. No worries in auto memory depth. It doesn't have anything else. But it doesn't. How about Rigol's new

**Dave Jones:** bad boy with their uh custom ASIC? Once again, exactly the same 5 microseconds per division. We're in auto memory depth here. Stop. Nope, doesn't do it in auto. Let's fix it. You can't actually change that unless you're running, which is pretty dumb. So

**Dave Jones:** we're in 100 meg now. Let's stop it. And yep, it'll do it. Once again, fixed memory depth. So that's a pretty handy reason to fix that memory depth. And of course, you might trade off uh update rate, of course, for the ability

**Dave Jones:** to have to be able to zoom out like this. I don't know what do you call it? The zoom out feature, I guess. Zoom out on stop or something. But anyway, yeah, that's a reason to set your memory depth

**Dave Jones:** fixed. How about Uni-T? 4 microseconds per division. They got the 1 2 4 sequence again. Where's our stop button? And nope, not on auto memory depth. But hey, we can we can change that. Let's go to the full 70.

**Dave Jones:** Function is disabled. What? Can I have 7 meg, please? Function is disabled. Do I have to be running it? Yeah, you've got to be running it before you can do that. And you saw just then when we switched

**Dave Jones:** to um 7 to 70, the update rate actually changed on this sucker. Of course, that's the trade-off. But on, once again, the fixed memory, no wackers whatsoever. And you can see all the little ramp pulses in there. Neat. And 01 here exactly the same 1 gig

**Dave Jones:** sample per second 1 meg memory depth stop and no problem whatsoever. And 01 doesn't seem to have an auto memory depth. It's just fixed only. Now, I've also heard that Lecroy don't do this as well. It works exactly the same as the Siglent.

**Dave Jones:** Probably not surprising considering that Siglent actually manufacture low-end scopes for Lecroy. So, maybe there's some, you know, shared technology there or something like that. But, even in fixed memory depth it doesn't actually have an auto mode. You stop it and you can you do not

**Dave Jones:** get any information outside the screen. So, it does operate quite significantly different in fixed memory capture mode to probably the majority of other scopes out there. So, it's really interesting. Anyway, I hope you found that video useful. If you did, please give it a big

**Dave Jones:** thumbs up. And as always, discuss down below. I'll actually link over to the existing EEVblog forum thread on this one cuz that's where this particular feature feature in quote marks is being discussed. With much excitement, by the way. So, anyway, yeah, it's just an

**Dave Jones:** interesting little aspect of using your scope. So, you really should get to know your scope in terms of what it's capable of and whether or not it does this in auto mode, what what difference is between auto mode and manual memory

**Dave Jones:** mode, and things like that. And it might just save your bacon one day knowing that you can just Well, in this case you can't, but knowing that you can just zoom out. As I said, in probably the majority of usage cases it doesn't

**Dave Jones:** matter. You just retrigger again at a slower time base. You know, you just go over here and you just go, "Oh, well, stop it." and then zoom in. I've got 200 meg of memory. No worries, right? But, you know, there might occasionally be

**Dave Jones:** the case where you're working on some obscure glitch or something. You finally capture it. Like you see something in here and you go, "Oh, jeez, I wonder what happened out side the screen here." And if you can't see it and you can't

**Dave Jones:** readily recapture it at a slower time base, then yeah, that could potentially be a useful feature. So, leave it in the comments down below. Does your scope actually have this feature or not in auto mode or fixed memory mode or both

**Dave Jones:** it doesn't or your scope doesn't have auto memory mode and it's only got manual or vice versa. And it may not be specific to a manufacturers there could very well be different models from the same manufacturer that operate uh

**Dave Jones:** differently, especially like older models, newer eye capture architecture and all that uh sort of stuff. So, yeah, it's a little fascinating uh quirk of scopes. So, anyway, I hope you learned something there and you found it useful. Catch you next time.
