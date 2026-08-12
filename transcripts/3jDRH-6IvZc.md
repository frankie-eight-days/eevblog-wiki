---
video_id: 3jDRH-6IvZc
title: Analog VS Digital Scopes for Glitch Captue
url: https://www.youtube.com/watch?v=3jDRH-6IvZc
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 23, "3": 41, "4": 51, "5": 64, "6": 73, "7": 86, "8": 96, "9": 106, "10": 118, "11": 135, "12": 147, "13": 158, "14": 177, "15": 199, "16": 209, "17": 222, "18": 233, "19": 245, "20": 253, "21": 264, "22": 276, "23": 294, "24": 314, "25": 331, "26": 342, "27": 351, "28": 372, "29": 392, "30": 411, "31": 427, "32": 433, "33": 443, "34": 450, "35": 463, "36": 471, "37": 483, "38": 490, "39": 505, "40": 516, "41": 528, "42": 548, "43": 557, "44": 572, "45": 596, "46": 608, "47": 616, "48": 629, "49": 641, "50": 653, "51": 668}
---

**Dave Jones:** Hi, in a previous main channel video, we took a look at waveform update rates on the new Tektronix 2 series scope and compared it with various other brands. And as it turns out, the 2 series scope is well, he's just captured one then.

**Dave Jones:** The 2 series scope is not that great. It's actually very poor in its waveform updates per second. This is why we're up to heart Oh, there we go. Just got it.

**Dave Jones:** What we've got is we're feeding in a signal that has a glitch there on it and you can see it pop up occasionally. And this is basically based on the statistical chance of it happening because it's got the number of waveforms per second that it's actually capturing up here and you can see it's probably doing 200, 300, 500.

**Dave Jones:** It's probably doing, you know, a couple of hundred waveforms per second. So, it's set at this particular time base, this particular memory depth that varies. Currently doing a couple of hundred samples per second.

**Dave Jones:** And we've got a signal that has a what's called a frequent glitch. I'm actually using Tektronix's own demo board and it's got frequent anomaly. It's actually called on there frequent anomaly.

**Dave Jones:** We can switch it over to the rare anomaly. I don't actually know how frequently it actually happens. But, anyway, I might be able to get some Is there a data sheet for that board?

**Dave Jones:** I don't think so. But, anyway, we've got an anomaly on here and it pops up occasionally. If you use another scope like this Keysight with the MegaZoom for ASIC, it just shows up all the time, right?

**Dave Jones:** Our glitch is there. It's just going to capture it cuz this does a million waveform updates per second or less at this particular time base. But, anyway, it's like orders of magnitude higher than the tech scope.

**Dave Jones:** So, it shows up all the time. Anyway, thank you to Steve Hurcomb on Twitter for asking this which prompted this video. Can I actually do this test on an analog oscilloscope?

**Dave Jones:** Well, you bet I can. I've got the Fluke combiscope here. This is actually analog and digital, but we're currently in analog See, there's digital mode there. We're currently in analog mode, so it's an analog scope, okay?

**Dave Jones:** Really nice analog scope. And we can plug this in, and like, can we see it? And the answer is uh not really. And why is that the case? It's like analog oscilloscopes are famous for showing the real waveform.

**Dave Jones:** And so, you know, you would think that we can actually see this thing cuz it's sampling all the time. Well, there's a brief period where it sweeps, where the trace actually sweeps back like this, but generally, it's just rewriting that screen all the time.

**Dave Jones:** We should be able to see it, right? Unfortunately, or fortunately perhaps, um this is the one example that actually shows up the benefits of digital oscilloscopes over analog scopes.

**Dave Jones:** And one of this frequent or infrequent glitching um stuff is going to do it. Because on an analog uh scope, the intensity of the display here depends on how many times uh the photons actually hit the front surface and actually emit light out of it.

**Dave Jones:** So, if you've got a very infrequent glitch that's only happening one in a thousand, one in ten thousand sweeps uh across for example, yeah, it's going to capture it, and it's going to put it on the screen, but if it doesn't stay there long enough or happen frequently enough um in order to excite the phosphors that you can actually see, then well, you're just not going to see it.

**Dave Jones:** And if I turn the trace intensity right up, right up, don't know if you can see that. Don't know if it's going to show up on the camera, but I can see just something in there.

**Dave Jones:** Maybe I'll turn out the lights. Hang on. Oh, can we see that now? Maybe? There, you can just see the little runt pulse in there. But, oh jeez, like it no, you would totally miss this in normal operation.

**Dave Jones:** You just wouldn't see anything. Now, if we put this back on the Tek Series II scope, there is actually a way that we can actually show this more frequently, and that's to turn persistence mode on.

**Dave Jones:** Okay, peak detect, we can do that. There we go. It might show it more frequently. There you go, peak detect. Oh, no. No, no, that was just a coincidence.

**Dave Jones:** Peak detect is still not going to do it. We need persistence. Where is it? It took me a while to find this. It's you double tap on there and we get waveform view.

**Dave Jones:** Anyway, now we can set persistence. At the moment, it's you can see it's set to auto. So, uh this what I discussed in the other video in that um what happens, right?

**Dave Jones:** If you have let's say your oscilloscope has a million waveform updates per second, like that one down there, right? That doesn't mean that your waveform on the screen that doesn't mean your screen is updating a million times per second.

**Dave Jones:** It's it's clearly not, okay? It's I don't know how frequently a screen refreshes on these scopes cuz that's not a spec that they actually uh tell you, but what they do is uh they take the million waveforms per second and then they sort of like combine those together to give you a screen update.

**Dave Jones:** That's why even though that glitch might only appear one in every thousand uh san- waveform captures, it's going to display it there for a brief period of time just so that you can see it, but you can actually override this by having either variable uh persistence where you can set a time period or you can have infinite.

**Dave Jones:** So, let's just do infinite like this and you'll see that it'll just stay there like that, okay? So, if we refresh that we have to wait for it to happen wait for it to happen wait for it to happen, but if it happens once, boom, there we go and it stays there and your waveforms will build up.

**Dave Jones:** So, uh using persistence mode, I might have done a video on this, have I? I don't know. Haha. Maybe this video is the persistence mode video. Um but here's where you can use persistent mode.

**Dave Jones:** If you think there's something happening with your signal now, you can see we've captured a bit of jitter on here, but this could be just a trigger jitter or something like that, right?

**Dave Jones:** So, this is just going to slowly build up and it won't override the screen unless you manually reset it or you change the scale or something like that. And this is a valuable way that even if you've got a slow waveform updating scope like this Tektronix 2 Series, even if, you know, the number of waveforms per second is slow, you can still turn on that persistence mode and

**Dave Jones:** just sit there and twiddle your thumbs and wait and wait and wait and see if something happens. But like I said before, it is a statistical thing. If you've got a if this one's only capturing a couple of hundred waveforms per second and another scope's capturing a couple of hundred thousand waveforms per second, you stand a better statistical chance of finding that waveform.

**Dave Jones:** So, you can think of this as like two levels here. One is the the waveform updates per second is important because you want to capture that signal. If you've got a slow enough update rate, then you may never capture or could take a huge long period of time that you might wait for a while and then you know, I don't see anything.

**Dave Jones:** So, you know, there's nothing wrong there. But it's the problem is you're don't have a fast enough waveform update rate to actually capture that. And then the next separate layer to that is really how the scope actually takes those waveform captures cuz it captures this is like there it is there.

**Dave Jones:** You can see it counting up there, right? It's a couple of hundred waveforms per second, okay? And it could be a couple This one has a maximum of 1,400.

**Dave Jones:** I actually measured it on the previous one, but it has a burst rate of up to 18,000 waveforms per second, but there's lots of dead periods. You have to watch the previous video for that.

**Dave Jones:** Won't go over it again. But if your scope doesn't have a fast enough waveform capture rate to actually capture the signal to begin with, you're never going to see it on the screen.

**Dave Jones:** But there is that second layer where you can include persistence on there or either infinite or variable. And if we actually take it back to variable, we can actually see that at 500 milliseconds.

**Dave Jones:** Let's set it for say, I don't know, 10 seconds, something like that. I've got to do seconds. How do I do 10 seconds? There we go. And bingo, right?

**Dave Jones:** So, we'll we'll capture that and it'll stay there for 10 seconds and I got to keep talking for 10 seconds and then it will eventually clear and then start again.

**Dave Jones:** Um 10 seconds is too long. Oh, come on, Dave. What did you pick that for? Come on, it should go. Should go. I've been talking for longer than 10 seconds.

**Dave Jones:** Hey, why isn't that working? That should bugger off. That should bugger off after 10 seconds. Why doesn't that work? Let's try 2 seconds, variable persistence. Okay? It should It should play Yeah, there we go.

**Dave Jones:** It just cleared itself. Yep, it just cleared itself after two. So, I don't know what it was happening with the 10 seconds there. But yeah, see, it clears itself and then it stays on there long enough so that you can capture it.

**Dave Jones:** So, that's a valuable technique. It's just to set, you know, not necessarily infinite's really good cuz if you're like you can leave the thing running overnight. I've done this many times to capture intermittent faults.

**Dave Jones:** You leave your scope hooked up running overnight. You know something's wrong there, you know, you got the heebie-jeebies. You know something's going to happen, but it's so infrequent. You leave your scope running overnight and then you come back the next morning and if you've got infinite persistence, bing, you're going to see your runt pulse or whatever glitch or whatever problem that you actually or your clock missed

**Dave Jones:** or something, you know, and you can actually see that by using infinite persistence on there. So, you can just leave it running for days, weeks, months if you want to find an intermittent problem.

**Dave Jones:** But the faster the update rate, the more possibility every second you have to capture that glitch. If If you've only got 100 waveforms per second capture and then another scope has, you know, 100,000, then you stand a better chance of getting it.

**Dave Jones:** Better statistical probability of capturing it with the 100,000 waveforms per second. So, there you go. And this is something that we can't do on an analog oscilloscope because analog oscilloscopes have a natural persistence, so to speak, in that you know, you light up the phosphor, you know, you shoot the electron beam shoots and lights up the phosphor, and then it does actually stay there for a period of time before it

**Dave Jones:** decays. But, if you've got like a really infrequent glitch like we've got here, then you know, it it only pops up like one in every thousand sweeps, and it's it's there for a millisecond.

**Dave Jones:** You you know, you're barely going to see it. And as you saw here, we could barely see that thing, right? And I've got to turn the trace up. I'm burning my screen.

**Dave Jones:** I can barely barely see that sucker down in there. There it is, but you know, you would you would totally miss that. When the only reason I'm looking for it is cuz I know it's there.

**Dave Jones:** But, yeah, there's nothing you can do better than that on an analog scope except turn up your intensity like this, which effectively increases your persistence time, but there's a certain limit to how much you can do that.

**Dave Jones:** So, yeah, that's the huge advantage of digital scopes, even slow ones in quote marks like this Tektronix 2 series. It's not slow in operation, as I said, it's just slow in the number of waveform updates per second.

**Dave Jones:** But, even in this particular case, no, this is an infinitely better tool than our analog scope. And that's a really good example. So, thanks for recommending that. If you liked that video, please give it a big thumbs up, and as always, discuss down below.

**Dave Jones:** Catch you next time.
