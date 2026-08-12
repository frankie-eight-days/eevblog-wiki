---
video_id: ta096oBzSac
title: EEVblog #159 - Oscilloscope Trigger Holdoff Tutorial
url: https://www.youtube.com/watch?v=ta096oBzSac
source: youtube-asr
timestamps: {"0": 0, "1": 16, "2": 32, "3": 47, "4": 63, "5": 80, "6": 95, "7": 111, "8": 129, "9": 146, "10": 162, "11": 178, "12": 193, "13": 206, "14": 223, "15": 241, "16": 254, "17": 271, "18": 286, "19": 305, "20": 319, "21": 335, "22": 349, "23": 365, "24": 380, "25": 395, "26": 410, "27": 424, "28": 438, "29": 450, "30": 464, "31": 476, "32": 490, "33": 504, "34": 518, "35": 530, "36": 545, "37": 560, "38": 576, "39": 589, "40": 603, "41": 614, "42": 628, "43": 639, "44": 650, "45": 662, "46": 676, "47": 688, "48": 704, "49": 722, "50": 737, "51": 749, "52": 765, "53": 777, "54": 792, "55": 809, "56": 820, "57": 838, "58": 854, "59": 869, "60": 884, "61": 896, "62": 910, "63": 922, "64": 938, "65": 952, "66": 970, "67": 984, "68": 998, "69": 1011, "70": 1023, "71": 1037, "72": 1053, "73": 1067, "74": 1083, "75": 1095, "76": 1110, "77": 1127, "78": 1140, "79": 1157, "80": 1171, "81": 1185, "82": 1201, "83": 1211, "84": 1226, "85": 1239}
---

**Dave Jones:** Hi, welcome to the AEV blog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, it's quick oscilloscope tutorial time. Now, I'm going to take a look at one particular feature of the

**Dave Jones:** oscilloscope that a lot of people really don't have much idea about. They find it a bit mysterious. In fact, a lot of people have never used it and well, quite frankly, they don't know what it does. And it can be found as a dedicated

**Dave Jones:** knob on many higher-end, in fact, most higher-end, older analog oscilloscopes, but especially on new digital scopes, they will have this option that a lot of people go, "Well, what's that?" I'm not really sure. They might twiddle it, but

**Dave Jones:** they don't really understand what it does. What is it? It's trigger holdoff. Let's take a look at it. First up, a bit of a background refresher on oscilloscope triggering. Now, this is going to be in reference to the old-fashioned analog oscilloscope,

**Dave Jones:** the old CRT cathode ray oscilloscope, because the concept starts there and it it carries on over to digital scopes, which are effectively the same thing. The concept's the same, but it just the background works better with the analog scope, cuz that's where it comes

**Dave Jones:** from. Now, as you we've got an analog CRT display here, which draws a waveform on the display. Now, the triggering system, which I might have to do another blog on just just general triggering, but all we're interested in is the trigger

**Dave Jones:** holdoff control this time, but the trigger point, what it does is that the the beam inside the CRT sweeps across the display, which we'll look at down here. It sweeps across from left to right and it draws the waveform on the

**Dave Jones:** display. Now, your vertical amplifier, the input channel to your oscilloscope, is the one that causes the vertical or Y deflection like that. But, the X axis or the horizontal time base is based on a fixed ramp. Basically, it's based on a linear

**Dave Jones:** It's an integrated sawtooth ramp like this. So, it's a linear sweep It's also called the sweep, okay? It's the horizontal deflection sweep or it's the voltage that's applied to the horizontal deflection plates, which causes the beam to sweep across the display. And that's

**Dave Jones:** a sawtooth waveform like this. So, once the oscilloscope triggers, okay, at this point, if you set your trigger level to say this Y value here on the positive edge like this, then the Once that trigger is received, then it will start

**Dave Jones:** sweeping this voltage will increase and the beam will sweep across the display like that, drawing your waveform. Now, when it gets to the end over here like this, okay, it's got to somehow get the beam back to here. It's got a what's called a

**Dave Jones:** retrace. So, it retrace its step all the way back here and it does that very quickly. Hence, the very quick ramp down like that. I've exaggerated the time period there and you don't want that to be displayed when it's retrace that beam

**Dave Jones:** back. Otherwise, you'd get a horizontal line on your display and that's no good. So, what they do is they blanket like this when it's retrace it and then it arms then the trigger circuitry arms again and it's ready for the next sweep

**Dave Jones:** and it does that again and again and again for your repeating signal. But, what happens is there is actually an extra hold off time here and that's what that analog hold off control on your analog oscilloscope does. It actually

**Dave Jones:** increases this time period up to a certain point. Each oscilloscope is different. Some will be calibrated, others will be like in actual time units. So, um you'll be able to actually set an exact hold off time. Others will just be a

**Dave Jones:** just a simple analog control which allow you to increase that time. Now, the hold off time will be in addition to that retrace period. So, when your beam sweeps across like this and gets to the end of the waveform, instead of just

**Dave Jones:** immediately retrace back like that, what it does well, it still retrace back, but instead of rearming straight away, rearming that trigger circuitry ready for the next trace, it just holds off. And that's why it's called trigger hold off because it effectively disables

**Dave Jones:** your trigger signal again for a fixed period of time. Now, of course, that hold off time must at least be as long as the retrace period to sweep that back and plus a little bit extra for it to settle before

**Dave Jones:** that trigger circuitry resets. But, you can actually extend that. But, why would you want to do that? Isn't update rate important? Why would you want to sit there doing nothing, displaying nothing on your CRT screen, potentially missing information, missing data when you can

**Dave Jones:** just rearm it and go straight away? Well, there's a good reason to it and there's some important benefits. That's why trigger hold off is an important concept that you should understand to really know your oscilloscope. So, let's take a

**Dave Jones:** look at it. One more thing, if you're talking about digital oscilloscopes, then it's effectively the same thing. It really it operates exactly the same except there is no retrace cuz it doesn't need to physically fly back the beam back to the

**Dave Jones:** left side of the CRT like that. So, really there is no retrace period, but there might be a processing time and stuff like that before it can actually trigger. And of course, a a one of the benefits of a digital oscilloscope is

**Dave Jones:** that you get pre and post trigger. So, it will typically trigger trigger in the middle like this, but really the hold off concept is exactly the same. After it's finished capturing the data, it will hold off triggering again for a certain

**Dave Jones:** predetermined amount of time. And the real benefit with digital scopes is that they all have really high resolution digital control for the hold off time. It allows you to set a precise value. Now, let's take a look at an analog

**Dave Jones:** oscilloscope here. Now, unfortunately, this isn't the best example cuz this is an analog digital combi scope. So, it's a bit complicated on the display here, but what we're interested in is the dedicated control down here. Now, it says delay position, but that's only for

**Dave Jones:** the delayed time base. If I turn it on, there we go. It's actually the hold off control. In regular mode of operation, it's hold off. Now, it's got a dedicated button. So, you think it's a pretty darn important control, and it is. So, let's

**Dave Jones:** take a look at the screen here when we operate the delay control. Now, if you remember that sweep waveform we had before, okay? I've got it set to a very fast sweep speed, so you can't see it retrace or anything like that. Hold off

**Dave Jones:** is off. It's set to or or it's set to the minimum. Often, they won't have an off. They'll just have minimum. Okay, but let's turn the time base down. Let's slow it down until we can physically see that dot sweep across the display like

**Dave Jones:** that. Okay? Now, if I now turn on this Well, first of all, you will notice that as soon as it gets to the end, bang, it retraces straight back like that. And it it actually goes slightly further than

**Dave Jones:** the screen. That's why there is a slight actual delay there, but let's now turn off this hold off. Now, you can't notice much at the moment. It looks pretty similar, but if I really turn that up, okay, I adjusted it all the way up.

**Dave Jones:** Look. Bang, it waits 1 2 3 and then it starts again. You see? That's probably the maximum for this control cuz it it's not really a fancy hold-off control at all, but you can see it sweeps across and

**Dave Jones:** there's an extra delay before it re-arms because I've got this in auto sweep mode, okay, which means it doesn't actually need a trigger input. It doesn't need a waveform to actually trigger it, but the concept is the same

**Dave Jones:** if you've got a waveform fed into it. And just to prove that's the case, let's actually get a real waveform on here, okay? Now we're actually going to switch it to normal mode here. So it's normal triggering. So if the trigger isn't

**Dave Jones:** there, there's no display at all. There's no trigger. There's no sweep. Nothing happens, but if we allow it to trigger, we can't actually This is an analog scope, so we can't actually physically see the trigger level here. Actually, we can if I turn the readout

**Dave Jones:** on. There you go. See how the trigger goes above? Once it Once that trigger point there goes above the waveform, the peak of the waveform, you don't get anything at all. And as you can see, it's come down and down and

**Dave Jones:** down and because we're triggering on the positive slope, then it starts to trigger and it on the positive edge of the waveform like that. But anyway, let's turn this hold-off control so you can see it does exactly the same thing here.

**Dave Jones:** Let me turn that readout down a bit. It's a bit distracting. And let's turn this hold-off up. And notice I'm not changing the time base and bingo, there it is. After it's finished, bang, it's got to wait. It's got that hold-off time and it

**Dave Jones:** must wait before it gets the next trigger. I know what you're thinking. Whoop-de-doo. What's the point of trigger hold-off? That didn't show us anything. It just delayed the sweep. What point is that? Well, there is really no point for simple repetitive

**Dave Jones:** waveforms like that sine wave use. So, let's take a look at another example where it's actually going to be of great value. Now, let's take the case of a digital signal here, but it doesn't have to be digital. It could easily be some

**Dave Jones:** complex analog signal or something like that, but this is a much easier example to work with than the one I'll show you on the display. Now, let's say you've got a burst of data like this separated by a long period of of nothing, really,

**Dave Jones:** and then there's another burst of data. And it might be the same burst or it might be the data that you want to look at. Now, if you don't have the hold off set at all, okay? If you've just got the

**Dave Jones:** trigger set, positive edge trigger, set in the middle like that, well, it can trigger off this point, this point, this point, this point, this point. It doesn't really know where to trigger. It's got no idea at all. The scope

**Dave Jones:** hasn't got a clue. This edge over here or this one in the middle of the waveform is exactly the same as this one here. It It doesn't know. So, with no hold off at all, what you get on your

**Dave Jones:** display, you've probably seen it before when you probe digital signals, it's just garbage, really. You can see the positive and the negative level and you can see a couple of traces in there. If you zoom in, you can see some edges and

**Dave Jones:** stuff, but it just jumps around and gives you a completely jumbled display. And you don't want that. You want to actually trigger off a fixed pattern like that and you want to see the gaps in between here and you want to do all

**Dave Jones:** that sort of stuff. Well, that's what trigger hold off can do. If you increase that hold off time from the minimum or from zero, you switch it on, and let's say the time period from here from here to here is say 100 microseconds, and you

**Dave Jones:** know it's 100 microseconds. You don't have to know. You can just in kick keep increasing the hold off time until you get the display you want. But let's say you did know that that dead time in there was 100 microseconds, well, you

**Dave Jones:** might set your hold off time to you slightly less than that, 90 microseconds, 95 microseconds. And what that does to the display uh what that does to the scope is that it the trigger will only trigger if there's 95 a

**Dave Jones:** minimum of 95 um uh microseconds of hold time of of dead time before that. Otherwise, it just ignores those trigger points. So, what it's going to do is it's going to capture that first trigger point after that hold off time. And the result is

**Dave Jones:** bingo, a magically stable display where you're actually able to see not only the individual uh packet down here, but the but the entire waveform display if you turn the horizontal out far enough, and you get a stable display. Magic. Let's

**Dave Jones:** take a look at a real example where it does exactly that. Now, what I've got on the analog scope here is this uh same a very similar digital burst signal. It's actually a bit more complicated, but as you can

**Dave Jones:** see, um if I adjust the time base here, then really um it's just, you know, it's just digital data. It's just really digital uh you know, garbage, really. You can't see much at all. You can see it's transitioning and

**Dave Jones:** all that sort of stuff, and everything's just fine, but really you can't make out that there's actually uh packets there. So, that's no of no use at all. So, what what we want to do is we want to use the

**Dave Jones:** hold off control here. So, let's turn the hold off controller. I don't know exactly what the time period is, but you can see the display kind of shifting there. And wait, bingo. There it is. We eventually hit a hold off time. If I go

**Dave Jones:** further than that, boom, it's gone again. So, there will be that window there where it it just delayed enough that we could see the difference in those packets. There's the There's the individual packet there. Magic. We've now stably triggered on that packet of

**Dave Jones:** data and you can do the same thing on a complex analog waveform as well. Now, there's actually one side effect of the holdoff control that is a bit hard to get on the display, but I'll see if I

**Dave Jones:** can do it. Um because when you when you add trigger holdoff, then it is then the display is not re-tracing as often and as fast on an analog scope. So, the intensity of your display is actually going to dim. So, I've got no holdoff or

**Dave Jones:** minimum at the moment. Now, actually see if you can remember that trace brightness and see if it dims when I turn up There we go. It actually dims when because there's not as many re-traces on the display. Now, let's feed the exact same signal

**Dave Jones:** into a modern digital oscilloscope like this Rigol DS1052E here. It's only a low-cost scope, but it'll give you an idea the even the high-end ones will have exactly the same functionality. As you can see, the same signal. It doesn't know where to trigger

**Dave Jones:** from cuz we if we go into the trigger menu over here, we're only triggering off regular uh positive slope edge triggering. It's an auto sweep and it's just it's not really doing anything at all. It's quite boring. So, um really

**Dave Jones:** it's it's not doing much at all. Now, if we change the time base here, the horizontal, we can get to a point where we can see start to see that there is some sort of packet type information in there. You can see

**Dave Jones:** those dead periods, but certainly can't trigger off it. Now, I know what you're thinking. There's this magic button up here. It's the auto button. Can't you just hit that and it auto scales everything and it should trigger, set up

**Dave Jones:** your trigger, and the whole works. Well, let's give it a try, shall we? Here we go. It's trying to figure itself out and bingo. Okay, it's set it up. It's triggered. Now, like if we we could have gone like that and let's let's hit

**Dave Jones:** it again, change the time base, boom, right? And it will auto scale like that. But, has it triggered off those packets? No, because it's not smart enough to do it. It just doesn't realize. But, if we go into the trigger menu here, and we go

**Dave Jones:** to set up, it will have, as all modern digital scopes do, they will have a hold off option. Now, if you reset it, which is the default value when you're using the oscilloscope normally, the hold value, in this case, is 500 nanoseconds

**Dave Jones:** minimum. Now, let's increase that, shall we? Let's select that, and let's turn it up. And I happen to know that that if we put in about 45 odd microseconds, that should allow us to trigger off this sucker, because that's what that dead

**Dave Jones:** time is. So, well, we're getting about No, we're getting there. So, let's Let's go up. Well, bingo. There we go, about 40 microseconds. And there, bingo. Our trigger hold off has worked perfectly, and we're actually triggering off that.

**Dave Jones:** So, you can that live display like that is incredibly valuable, so that you can actually see if there's any glitches in there in real time, and stuff like that. And of course, you can stop it, and then zoom

**Dave Jones:** into your data, of course, and then you can analyze it. But, that's just a way that you can get triggering on a complex waveform using trigger hold off. It's brilliant, and that's what it's for. And just to show that hold off again on

**Dave Jones:** the digital scope, or the effect of it, I've just got some noise I'm just measuring a noise signal here, so you can see the updating on the display going flash flash flash flash flash, because I've got the minimum hold time.

**Dave Jones:** Now, let's change that hold off time to Let's change it, say Let's go massive. Let's go up to a second, and you'll see it Well, there we go, about a second. One spot on a second, actually. And bingo,

**Dave Jones:** one, two, three, four, five. Because it's not triggering. It's only going to trigger Well, in this case, because it's very quick, um it's effectively once per second. Bang. Bang. Bang. Like that. It's holding off the trigger for that 1

**Dave Jones:** second. Just for kicks, let's try that on a more upmarket digital scope. In this case, the brand new Agilent InfiniiVision 2000 series. Now, I've already set that hold off time, so we're getting our packets, no problems at all. We're seeing that

**Dave Jones:** data, and it's just brilliant. Not a problem. But, let's try that magic auto scale button, shall we? That everyone thinks is so wonderful. Let's try it on this scope and see if it does anything. Here we go. There you go. It's It's hopeless. It

**Dave Jones:** doesn't know what to do, either. And it's not surprising, really. It just did the same as the Rigol. So, what we've got to do is we've got to go into Of course, we've got to go into our trigger

**Dave Jones:** mode, and the minimum hold off time, there it is, 40 nanoseconds. And we've got to adjust that. Now, it's a bit touchy, this one. It can jump around the place if you uh turn it too fast, so But, if we get to 40, there we go.

**Dave Jones:** Bingo. There it is. We've got our stable display using our hold off control. Magic. Now, just to clarify that one bit further, what hold time will actually work is uh actually the period of the entire repetitive cycle that you're

**Dave Jones:** trying to actually capture. And that window in there is the value that will actually work. So, I've set up the vertical cursors here. I've set one right at the start of the packet which I want to measure. And let's go Let's move

**Dave Jones:** the other cursor here. And as you can see, it should The hold off should work anywhere from about 40 microseconds up to just before about 47 microseconds, or thereabouts. So, any hold-off time in that period should give you a nice

**Dave Jones:** stable triggered display like we're seeing here. And this is actually a live display. It's not actually That's actually captured, okay? And that's actually live. So, let's try that and see if it works. And here we go. Let's try and prove that

**Dave Jones:** the hold-off time 37 microseconds. So, all all before 37 microseconds it doesn't work, but after we should hit about 40 or or hey, bingo. There we go. 39.6 is near enough cuz we didn't measure that absolutely precisely. And

**Dave Jones:** it should work up to about 47 or thereabouts, maybe with a bit of errors, but it's still going. No, it's still going. But there we go. Hey, it's starting to starting to jump around there because we're getting a couple of other edges it's triggering

**Dave Jones:** off. And then 50 it's lost the plot completely. And after that it's just not going to work at all. And then of course we're able to capture that and zoom into our heart's content. And we've got a nice

**Dave Jones:** beautifully triggered uh complex waveform. So, next time you're playing around with complex waveforms like this, be it digital or analog, just have a play around with the trigger hold-off. There's no need to put up with that crap uh display which just

**Dave Jones:** goes all over the place. Sure, we can just start-stop that and capture the data, but it's good to have your live uh you know, if if you've got enough if you got a digital storage scope with enough memory, sure you can just capture it

**Dave Jones:** like that and everything's fine. But really uh you you can't beat having that stable triggered display for live viewing. So, just play around with the hold-off control next time you're using the scope. I hope that was worthwhile. See you.
