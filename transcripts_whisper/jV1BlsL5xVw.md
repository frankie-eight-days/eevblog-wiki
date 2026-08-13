---
video_id: jV1BlsL5xVw
title: EEVblog #698 - GPU Video Rendering
url: https://www.youtube.com/watch?v=jV1BlsL5xVw
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 24, "2": 43, "3": 63, "4": 85, "5": 103, "6": 122, "7": 147, "8": 160, "9": 178, "10": 196, "11": 211, "12": 227, "13": 249, "14": 263, "15": 284, "16": 309, "17": 324, "18": 344, "19": 359, "20": 387, "21": 403, "22": 423, "23": 442, "24": 459, "25": 484, "26": 506, "27": 521, "28": 541, "29": 568, "30": 586, "31": 606, "32": 631, "33": 655, "34": 672, "35": 693, "36": 712, "37": 737, "38": 761, "39": 779, "40": 803, "41": 827, "42": 845, "43": 862, "44": 881, "45": 900, "46": 918, "47": 933, "48": 951, "49": 966, "50": 997, "51": 1018, "52": 1038, "53": 1059, "54": 1077, "55": 1092, "56": 1108, "57": 1130, "58": 1147, "59": 1164, "60": 1181, "61": 1196, "62": 1214, "63": 1234, "64": 1257, "65": 1277, "66": 1292, "67": 1315, "68": 1332, "69": 1349, "70": 1369, "71": 1384, "72": 1402, "73": 1420, "74": 1443, "75": 1462, "76": 1481}
---

**Dave Jones:** Hi, this is hopefully going to be a relatively short video. I just wanted to test the video rendering performance of a new graphics card, a GTX 970, that I'm going to install in my video rendering machine here. Now, I've recently changed over to 50 and 60 frames per second video that I'm creating to upload to YouTube,

**Dave Jones:** but I haven't always done this. This is only fairly recent. I have actually always shot at 25 frames per second because the PAL video cameras here in Australia that you buy, they're 25 frames per second, not 30 frames per second. And it was very, very quick, even without GPU acceleration.

**Dave Jones:** Let me show you. Here's an old clip that I've got from my Canon HF G30 camera, and it's shot at 25 frames per second. You can see my project here is 25 frames per second, so I just want to show you what my rendering times used to be like here for doing my videos beforehand.

**Dave Jones:** It was very quick. So if I go in here and I set... Oh, sorry, wrong window. I was actually using, for the sake of rendering speed, the XD cam format. So I've got that down here. I've got it already set up for 25 frames per second and 35 megabits per second variable bit rate.

**Dave Jones:** Because I do a two-step video rendering process. I use Handbrake as a second step. But anyway, what I'm concerned with was getting a decent video rendering speed out of Sony Movie Studio, which is what I'm using. This is Sony Movie Studio Platinum 13.

**Dave Jones:** Really, there is essentially, I believe, no difference between Sony Vegas and Movie Studio, apart from some more professional features. But in terms of video rendering speed, it's exactly the same as Sony Vegas. So here we go. If I just do a test here, and I'm going to render this.

**Dave Jones:** It's a one-minute clip, precisely. And you'll notice that it is very quick. Look, it's churning this out. It's going to do it at about twice real-time. That's a metric used on video rendering. Is it real-time? So if I've got a one-minute clip here, if it takes one minute, that's generally regarded as pretty good.

**Dave Jones:** Now what I'm using here is an Intel Core i7 processor. I'll show you that in a second. But look, yeah, there you go. It is twice real-time. It took basically just over 30 seconds to render that video. 33 seconds, but let's just say twice real-time there.

**Dave Jones:** So it's pretty quick. So that's what I was used to. And then I do a second step in Handbrake to get the file size down before I upload to YouTube without dropping any video quality. Because the file I just rendered would be a very large video size.

**Dave Jones:** So I can't archive that and upload it to YouTube. It just takes too long, uses too much bandwidth. So, you know, it was very quick. I was used to twice real-time. And my projects, I can probably show you a detailed project later, but my projects are usually very simple.

**Dave Jones:** They've got, you know, not much in the way of editing and stuff. All I do is basically trim the start and the end of the video. And maybe there might be a text overlay or something like that. But there's no real graphics effects or anything like that in my videos.

**Dave Jones:** So very untaxing to a video editing software like Sony Movie Studio here. And for those wondering why I don't use Adobe or something like that, Sony Movie Studio works for me. It works for my workflow. I just like the way it works. I've benchmarked it.

**Dave Jones:** It was actually faster than Adobe. So, you know, I've been using it for a long time and it works well for me. Yes, I have tried Adobe and almost every video editing software out there. I don't like them. Yes, Sony has its drawbacks too, but it seems to be the best of the bunch in terms of...

**Dave Jones:** I might do a separate video on this, why that's the case and how I edit videos and things like that. Anyway, very, very quick. There you go. And for those wondering, yes, that was done without GPU acceleration, without using my video card. So just the CPU itself.

**Dave Jones:** Now, if I go over here and I do it again, I can't use that particular codec to do... to use GPU acceleration with that one. So I'll choose one that does. Everyone raves about GPU acceleration. That's what we're going to test today. Let me just do a very quick test here.

**Dave Jones:** Here we go. Render using GPU. Okay, so I'm going to render using my GPU over here. Yes, I've got... CUDA is available, so my NVIDIA card is all supported there. Everything's hunky-dory, so now I'm using the Sony AVC format. And once again, I've got high profile, CAVAC, all the requisite stuff at 25 frames per second here.

**Dave Jones:** And I'm doing that at, say, 16 megabits, which is typical back in the day, because I would shoot at 18 megabits, but now I shoot at a much higher data rate, because I'm using the 50 or 60 frames per second. Here we go.

**Dave Jones:** So we can just render that, and let's just run a test on that. And it's... Override existing file. Yep. And you'll notice that it is much, much slower. This is why I use the Sony XDCAM intermediate format. This one's going to take probably around about three times as long.

**Dave Jones:** I won't actually wait there for it to finish. This is going to be relatively accurate. Okay, so three times as long for exactly the same clip. And if I go in here and I do it again, and here we go. I do that without the GPU.

**Dave Jones:** Render using CPU only. Okay. Let's try that with just the CPU. Here we go. It's going to be actually slightly quicker. There you go. My CPU is actually rendering, doing video rendering, in my case, with my particular files, using this codec, the Sony AVC.

**Dave Jones:** It is actually faster to use my CPU than to use my video card. So why is the CPU faster than the GPU? Well, it's pretty easy, because my CPU is a pretty decent one. I built this machine maybe less than a year ago,

**Dave Jones:** and it's got an Intel Core i7-3770K working at 3.5 gig there. So, you know, it's got 16 gigs of memory, all the rest of it, right? So it's a pretty darn decent CPU for graphics rendering. Now, if we go over the graphics card, this is why I'm not getting huge performance using the GPU,

**Dave Jones:** because I've only got an NVIDIA GeForce GTX 650 graphics card, and this is what I wanted to update. You can see that a basic industry benchmark here for the 650 is only 1835, right? So that's really not terrific by modern standards. That's why the CPU is quicker.

**Dave Jones:** But if we go over to the new card I've got, I'm going to install, in a minute, a GTX 970. So this one has 8635 based on the same bench card, and it is one of the fastest graphics cards on the market at the moment.

**Dave Jones:** Not quite the best, but pretty darn good. So, really, we should get no complaints over that one at all. And if we compare the GTX 650, here we go, it's got 384 CUDA cores, and the 970 has 1664, plus it's got a boost clock mode,

**Dave Jones:** and it's got higher, you know, memory bandwidth, and memory clock is 7 gig compared to 5 gig, and it's got 4 gig of RAM, and it's got 224 gigabytes per second bandwidth compared to 80 gigabytes per second bandwidth. So, you know, a significantly faster graphics card.

**Dave Jones:** So let's see if it makes a huge difference. But what now I want to do is show you how slow my machine has become now that I'm rendering 50 and 60 frames per second video. So here is my latest mailbag video, and here's a clip from it.

**Dave Jones:** Once again, precisely one minute long, so we've got a decent benchmark, and it was shot at 59.94 frames per second at, I think it's 35 megabits or something like that. So it's a much higher bitrate as well than my previous videos. They were all shot at 17 megabits per second, my previous ones.

**Dave Jones:** So if I go here, I actually can't use the AVCHD or the XDCAM format anymore because it doesn't support 60 frames per second. Hang on. No, yes it does. Sorry, I got confused. It does, but only at 1280x720. There you go. So I've had to ditch that, and I've now had to go to this Sony AVC codec,

**Dave Jones:** and by the way, no, the main concept codec is even slower than the Sony codec. But hey, it might not be when I install the new card, but the Sony one supports the NVIDIA CUDA cores. So let's go in here. So I'm now getting a 60 frames per second project.

**Dave Jones:** So there we go. And I'm outputting at a higher bitrate, it's 26 megabits, but it's all essentially the same. So here we go. Let's render the same video here at, well, the same length, one minute, but it's at 60 frames per second at 26 megabits, CPU only,

**Dave Jones:** so I'm not actually using my graphics card, because we've already established that the graphics card, the CPU is faster than the graphics card, okay? So let's go render. And my one minute video took 30 seconds to render before, and now it's going to take, hmm, around about three minutes to do.

**Dave Jones:** Wow, so that is six times slower, just because I've switched to 60 frames per second, and I've been forced to change my codec. Killer. And if you don't believe me that the GPU doesn't accelerate that, then we've got our GPU, let's render. It should take a little bit more, a little bit longer than three minutes

**Dave Jones:** to actually render that one minute clip. Now, yep, see, it's gone up. It's only slightly slower, but basically, you know, pretty much on par with the CPU, very similar to what we saw before. And here we go. Just as an absolute benchmark, I'll reuse this project

**Dave Jones:** when I install my video card, but this was using GPU acceleration, and it took three minutes and 27 seconds to render that one minute video with no fancy editing stuff, no fancy transitions, or anything else, just raw video from the camera. Let's see how the new video card does.

**Dave Jones:** So here we go. I've got the new graphics card installed. That wasn't too painful at all. Just downloaded the latest driver, installed that, and everything's working just fine. Here it is, the NVIDIA GeForce GTX 970 with 4GB of RAM. So let's give this a burl and see if it makes a difference.

**Dave Jones:** Remember it was like three minutes 30 or something last time? So let's try it. We've got exactly the same project, exactly the same configuration. We're using the GPU. Here we go. So let's turn it on, 60 frames per second. Yep. Let's go. Render, and here we go.

**Dave Jones:** It's not looking great, is it? Nope. Look at that. Three minutes. Three minutes. No, that is a complete fail. That is a $500, one of the highest-end video cards you can get. Not quite there, but geez, it's pretty darn near the top. It is like five times at least,

**Dave Jones:** I think it's about four or five times quicker than my previous GTX card, and that does not work at all. Is there something wrong in my settings? I don't like that at all. That's taking forever. And yeah, there you go. That makes sense.

**Dave Jones:** Check GPU, no GPU available, even though if I go up into the preferences, it will, look, it's there, GTX 970. But it doesn't let me. Maybe I have to repower it. Let me try that. Well, there you go. As it turns out, this top-of-the-line NVIDIA graphics card

**Dave Jones:** has been a complete waste of time and money. Now, I just cannot get this thing to work. Well, kind of, okay? I originally thought it was the graphics card, and I searched all the drivers, and I searched the net, and everyone seemed to be having problems with this new Maxwell chipset,

**Dave Jones:** which is in the 970 and the 980 chipsets, and also in the GTX 750, but these specific 970 and 980 chipsets are so new. Oh, they need special drivers, all that sort of stuff, and I tried various different drivers, the one that came in the box,

**Dave Jones:** and the latest one I downloaded, and all sorts of things. Tried to install all sorts of CUDA stuff, and it made absolutely no difference at all. Now, I was eventually able to go in here under the main concept codec, and actually get it to get,

**Dave Jones:** CUDA is available here, but I could not get it, I could not get the CUDA availability on the Sony AVC codec that I want to use. It's just not possible. It's either Sony doesn't support it, or some sort of combination of the new CUDA drivers

**Dave Jones:** in the NVIDIA driver set aren't compatible, you know, backward compatible with the existing support that's in Sony. And yes, you look at the official list for Sony and what cards it supports, and it just says basically anything CUDA supported greater than some old

**Dave Jones:** GTX 400 series. It just says anything greater than that should work just fine. And well, no, it ain't that easy, I'm here to tell you. This is, you know, basically potluck. I've had no end of problems with stuff like this. Anyway, what I've done is I've ditched that card,

**Dave Jones:** okay, it was, I couldn't get the CUDA support, so really, it was a complete waste of time. So what I've done is I've gone back and I've actually installed an old 80, well, it's not all that old, but it's a Radeon HD 7850.

**Dave Jones:** And it's not a bad graphic card at all. It's got, look, it's got a benchmark of about 3700, so it's like more than twice as quick as the previous GTX 650 I had in there. And I originally had this graphics card installed in my machine,

**Dave Jones:** but I was getting all sorts of, like, video tearing up the top, and there were all sorts of issues, and it was just a pain in the arse, so I ditched it. And, well, now I'm back, I've got the latest drivers available, and if we check it out, if we go in here,

**Dave Jones:** we'll see that we've actually got it available in, but not as CUDA. We will have it available as, here we go, render using GPU and system. It actually uses the OpenCL GPU interface instead of the CUDA, because CUDA is NVIDIA-specific, but I believe that you saw it before,

**Dave Jones:** that it does offer CUDA when you accept the main concept, choose the main concept codec, so it's rather unusual. Anyway, we now have OpenCL available, and I can actually run this thing. So let's go, let's run it, and bingo, that's looking reasonably quick there,

**Dave Jones:** that update rate. There we go, but ultimately, ultimately not much quicker than the GTX 650 that we had before. So really, that's going to take, like, two and a half minutes. Not that great. You'll probably see, if we cancel that, it's probably going to,

**Dave Jones:** well, we've seen it before, it's going to be pretty much identical with the CPU version of the driver. So, you know, look, it's not helping at all, even with that sort of mid-range graphics card with, as I said, like a pass mark of like 3700,

**Dave Jones:** which, you know, is sort of like mid-range, but here's the one we tried, this GTX 970 right up here with 8600. It's a shame we couldn't get the damn thing working, but it just goes to show you that this, you know, video rendering stuff is tricky business.

**Dave Jones:** Depends on the card you've got, the driver, the OS, it's going to, what version of driver you've got, what type of, whether you're using CUDA or OpenCL, what video editing software you're using here, what codec you're going to be choosing in the thing,

**Dave Jones:** and all sorts of paraphernalia. So people make it out that, you know, this sort of thing is, oh, it's just trivial, just whack in a high-end video card and Bob's your uncle, she'll be right. You know, you'll scream along, your video editing, no,

**Dave Jones:** and it's your source material as well, what frame rate you're outputting to, whether or not you're doing any resampling, any resampling of your video, all sorts of stuff, let alone the effects and everything else. So, and yes, by the way, I did actually try Adobe Premiere,

**Dave Jones:** I do have it installed on this machine, and I tried it with that card, and it was, it's still slower than my original thing, than my original setup. So it's not any quicker at all. So, you know, please Adobe fanboys, don't come in and say,

**Dave Jones:** oh, I just switched to Adobe Premiere, it screams on my machine. Yeah, well, your machine's not my machine, and your requirements aren't my requirements. So it's entirely specific, as we saw. Anyway, I was hoping that this would work, but it turned into a complete fail,

**Dave Jones:** so what's that, I don't know, a 10 or 15 minute video of me waffling on, looking at video editing, and I was hoping I'd fix my issue by putting in a top-of-the-line video card, and nah, wah, wah, wah, wah, fail. Anyway, there you go,

**Dave Jones:** that's the intricacies of all this sort of stuff. One thing I haven't actually mentioned yet is that the figures that we've seen here while I'm doing this aren't quite as fast as they can be, because I'm screen capturing this in the background, so it's got to do two things.

**Dave Jones:** It's got to do all that video rendering, which is massively processing intensive, and so is this video capture as well, and I'm using Debu video capture software from NCH, if you're wondering, that's an Australian company, works really well, and it's pretty cheap. This is what I use to screen capture stuff,

**Dave Jones:** and it's doing it at 30 frames per second. So I've actually done some tests on this with the AMD HD 7850, and it turns out it's a little bit slower, like with the capture turned off, it's a little bit slower with the OpenCL GPU enabled.

**Dave Jones:** Once again, the CPU rendering is actually slightly quicker for this particular test video using this particular source, etc., etc. So there you go. Yep, I just can't win with these graphics cards. I don't want to fork out for another high-end Radeon now. Jeez, it's getting ridiculous.

**Dave Jones:** So it goes to show the sort of complex requirements from a professional video blogger like myself who does this daily. I'm editing, I'm producing several videos a week, so all sorts of render time and productivity and workflow and everything else really matters, and I'll have to do some separate videos on this

**Dave Jones:** to show you exactly how I edit things and then render and then transcode and do that sort of stuff, how my workflow actually works for that. But just changing from 250 frames per second made a hell of a difference, but it's not just 50 frames per second.

**Dave Jones:** I'm now using a combination of two cameras. One does 50, one does 60, just because they're the particular cameras that I've got. One's saving in MPEG-4 format, one's saving in AVCHD. Slightly different flavors there. They're going to render in different bit rates and all sorts of stuff can get really, really complex.

**Dave Jones:** And by the way, for those wondering, no, the hard drives don't make any difference whatsoever. That's another myth that goes around just for general editing like this. The bit rates are not high enough for the hard drives to have an impact. So just switching to solid state hard drives

**Dave Jones:** is not going to increase your throughput at all. It's all about the bit rate, and what we've got here is you're rendering at, say, a high bit rate, like 25 megabits per second, for example. That's megabits, that's not megabytes. And modern hard drives, the SATA interfaces,

**Dave Jones:** the read and write speeds, more than fast enough to keep up with rendering in real time on a machine like this. No problems whatsoever. And trust me, I've actually tried it. I've tried writing to solid state drives, reading from regular hard drives, or reading and writing from the same hard drive.

**Dave Jones:** It makes no difference to the render time whatsoever. So unless you're doing really extreme stuff, solid state hard drives aren't going to increase your performance. But yes, I do have a solid state hard drive on this machine for my boot drive, but I do all of my video rendering

**Dave Jones:** on a regular 7200 secondary drive. But even like on a 5200 speed, like a really bottom-end consumer grade hard drive these days, more than good enough to keep up with these sort of bit rates at 20, 30 megabits per second. No problems whatsoever.

**Dave Jones:** And there's no doubt going to be some people out there that are going to say, well, I'm completely wasting my time trying to do GPU rendering anyway because it's a complete pile of garbage and it produces actually inferior quality video. And well, I can neither confirm or deny that really,

**Dave Jones:** because I haven't bothered to actually critically review the video quality footage from a GPU rendered output as compared to a CPU rendered output. But some people claim there is significant differences. I know, I'm pretty sure there is with Intel QuickSync, for example, which can be really, really fast at rendering,

**Dave Jones:** but apparently, yeah, the video quality is not that great on that. So anyway, these are the trials and tribulations of trying to do GPU rendering. It's not as, yeah, it may work for some people, and well, good on you, but it's never worked for me,

**Dave Jones:** and even when I bought a high-end card, it's still not working. Murphy's going to get me every time. So looks like I'm just going to have to go back and rely on CPU rendering. Oh well, can't win them all. Catch you next time.

**Dave Jones:** Thanks for watching.
