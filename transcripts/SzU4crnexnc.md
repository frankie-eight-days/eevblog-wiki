---
video_id: SzU4crnexnc
title: Vegas Video Editing & Voukoder Encoding
url: https://www.youtube.com/watch?v=SzU4crnexnc
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 23, "3": 47, "4": 59, "5": 77, "6": 102, "7": 123, "8": 134, "9": 151, "10": 164, "11": 181, "12": 195, "13": 209, "14": 221, "15": 239, "16": 253, "17": 264, "18": 276, "19": 288, "20": 298, "21": 309, "22": 318, "23": 339, "24": 354, "25": 370, "26": 383, "27": 400, "28": 411, "29": 433, "30": 445, "31": 456, "32": 469, "33": 478, "34": 490, "35": 504, "36": 515, "37": 527, "38": 541, "39": 555, "40": 560, "41": 584, "42": 595, "43": 603, "44": 612, "45": 619, "46": 633, "47": 644, "48": 655, "49": 668, "50": 678, "51": 694, "52": 706, "53": 721, "54": 733, "55": 744, "56": 758, "57": 769, "58": 780, "59": 791, "60": 804, "61": 818, "62": 833, "63": 844, "64": 856, "65": 866, "66": 878, "67": 894, "68": 915, "69": 925, "70": 944, "71": 955, "72": 964, "73": 981, "74": 996, "75": 1008, "76": 1021, "77": 1038, "78": 1051}
---

**Dave Jones:** Hi, yes, it's Vegas video editing time again. I'm just [ __ ] around with it doing some trials comparison between version 17 and version 18 and in particular with a new encoder that I've found.

**Dave Jones:** So, before this I've been using of course Vegas for donkey's years now and yeah, don't get me started on other packages. Yes, I've tried them all. Yes, I've tried the Black Magics.

**Dave Jones:** Yes, I've tried everything. Okay, I use Vegas for reasons. All right, so anyway, what I normally do is use So, I've got Vegas 17 here and what I've done is I've set up a test project so that we can do a test render a 10-minute project here on the timeline which has a mix of different content because the rendering especially the not only the rendering time but the

**Dave Jones:** final file size will depend on the type of content that you're actually rendering out. In this particular case, I've got a mix of like you know, a talking head Dave in front of the camera.

**Dave Jones:** I've got a mix of bench stuff here which I normally do and then I've got a screen capture and screen captures because they're absolute static images. They basically, you know, my little head changes down here but like there's no little shaking in the camera which moves pixels like this.

**Dave Jones:** So, it's absolutely pixel perfect. So, that's really great for constant quality algorithms and and things like that and also rendering time. It renders much faster like a screen capture video is much faster and produces much smaller file sizes than it ordinarily ordinarily would unless you use constant bit rate and you really shouldn't be using constant bit rate for producing YouTube videos.

**Dave Jones:** You should be using variable bit rate or a constant quality which is what I would recommend. And so, over the years I've been using like variable bit rate. In recent times I've been using constant quality using the NVEnc encoder which is the Nvidia GPU hardware encoder supported inside Vegas and I show you that in a minute.

**Dave Jones:** But unfortunately, version 18, they've actually removed the constant quality format. I'll show you this. It's this is what really ticked me off and why I found a new encoder for this thing.

**Dave Jones:** Anyway, so we've got a 10-minute test video. So let's render this. I'm doing this on my solid state drive but it really makes no difference where your source materials are and where you're rendering to I found because like my network driver I normally have my videos from it doesn't impact the render times at all.

**Dave Jones:** So writing to reading or writing from a solid state disk makes no difference. But anyway, we will write to a solid state disk today. Hang on. What I'm going to do is I'm going to change the project.

**Dave Jones:** It's normally 60 frames per second. I'm going to change it to 30 frames per second because that's just going to work better with the mixed content here because my capture is only 30 frames per second and anyway, so we'll do that and we'll save that and we'll we'll now render a project.

**Dave Jones:** Now, what I would normally do is use 1080p 30 frames per second 8 megabits per second but it's constant quality so that doesn't matter. It's just a label. I'm using the Magix which is Magix Vegas.

**Dave Jones:** It was Sony Vegas. Now it's Magix Vegas. Anyway, the Magix AVC MP4 AAC MP4 encoder and this one actually supports You'll notice down here. Here it is. Here's the rub, right?

**Dave Jones:** I support I render in high quality mode using the NV Nvidia encoder. The main concept that'll be like CPU encoding. The NV Enc will use the Nvidia GPU to actually do the encoding and I use constant QP mode.

**Dave Jones:** Look, there it is. Constant QP. That's constant quality mode which is what programs like HandBrake and things use. I still use HandBrake for my podcast 720p podcast version. I just I've got scripts which I just drag it in and it automatically generates a 720p podcast version for me.

**Dave Jones:** But anyway, I would normally use constant QP mode, right? So, I I don't think the variable bit rate actually matters here in the constant QP mode. But one thing about this is it doesn't actually let you set the quality factor of the video.

**Dave Jones:** So, what constant quality is is it analyzes each frame and chooses a bit rate based on the complexity or changes in frames between, you know, it's probably a block of frames or something.

**Dave Jones:** Not sure the exact mechanism, but it varies the bit rate all the time depend to give you a constant quality in your image. So, you know, it like X amount of loss or X amount of blockiness or whatever.

**Dave Jones:** Um and there's various, you know, settings like in HandBrake you might use a constant quality factor of 22 or 23, for example. What that number is it depends on the encoder.

**Dave Jones:** Don't worry about the actual number, but it's, you know, anyway, constant quality mode we can't adjust that, but I've been using that for quite some time now and it works well.

**Dave Jones:** So, here we go. I'm going to run a test. We'll render to C/video. So, we'll render. Go. Here it goes. There you go. My screen capture I've done this before and it doesn't really impact anything.

**Dave Jones:** So, don't worry about the screen capture there. So, you can see how it actually buffers. See the frame counter here? How it actually buffers and then pauses. It's filling the buffer with in this case 30, I believe.

**Dave Jones:** Yeah, it should be 30. Yeah, it's 30 frames. So, yeah, it's pulling in all the frames and doing its little processing and then pulling in the next one. So, anyway, this 10-minute video will take about Well, at the moment it's going to take 3:20, but that will speed up when we get to the video capture content.

**Dave Jones:** It'll just process it faster. So, I'll get back to you. Here you go. It looks like that is going to take 3 minutes and 30 38 seconds. 3:38. And there it is.

**Dave Jones:** Uh 226 meg. So, yeah, that's a combination. So, let's uh now try version 18, the new software I just got, and see if uh this new encoder that I've got actually makes a difference.

**Dave Jones:** Right. So, this is version 18 here, and let me show you. Okay. Magics AVC AAC. Okay. It's still it pulled in all my original uh ones here. And if we go into customize template, here we go.

**Dave Jones:** Down here, NVEnc, high quality, VBR. Where is the constant quality? They've actually removed the feature. I'm sure they have. Um and so, it's it's it's goneski. Like this was like the single thing that I used on Vegas.

**Dave Jones:** Yeah, I like I I can do VBR. Like if I'm doing a 1080p video, for example, uh then I might typically use an average bit rate bit rate of 8 megabits.

**Dave Jones:** Uh that's what YouTube recommend, I believe. But it depends on the content. If I'm shooting my lab content like this, like not much is moving, just my talking head is moving around or the products moving around in shot, it's nothing really that requires a high uh bit rate cuz the the more content you have moving frame to frame in your video, the higher bit rate you're going to need to keep the same

**Dave Jones:** compression and to stop it going all blocky and, you know, losing the quality and stuff like that. So, I typically uh I cuz my camera, I think at 1080p I'm shooting at 28 megabits per second, but I might have like a maximum of 20, so it'll peak.

**Dave Jones:** It'll change the variable bit rate and stuff like that. Um so, if I'm going to use VBR, oh well, actually, I I will do a VBR version of it and um and just compare the file size, actually.

**Dave Jones:** But if I'm doing a like one of my outdoors videos, for example, my one of my canyoning videos where there's you know like trees and things moving and the camera is shaking and doing everything else, I'm going to use much higher bit rates than what's here.

**Dave Jones:** So, you know, don't take this as you know, if you're outdoor shooting, you know, you don't want like an 8 megabit average video perhaps. Anyway, and of course if you go into 4K content, you would have higher.

**Dave Jones:** I've got different settings for 4K. Anyway, what I want to show you is a new encoder because this they've removed the constant quality encoding from NV Enc on version 18.

**Dave Jones:** Unbelievable. I'm going to need another encoder and thankfully some people over on the Vegas Creative Community Forum, they actually helped me out and they recommended this one which I've never heard of.

**Dave Jones:** So, thank you very much. It's called Vookoda, if I'm pronouncing the Vokoda, Vookoda. And look, it supports Adobe Premiere, Adobe Media Encoder, After Effects, Vegas Pro and VirtualDub too.

**Dave Jones:** And by the way, you have to download the core version here and also the plugin that you want for your thing. I just downloaded the plugin and it didn't work.

**Dave Jones:** I didn't know I had to download the actual core version. But yeah, this is a plugin for Vegas. So, this is absolutely fantastic and it supports H.264, X.264 constant quality just like HandBrake does.

**Dave Jones:** Absolutely fantastic. Now, you can actually integrate HandBrake and X.264 with Vegas and I've tried to do it, but I had like audio and video sync issues and it never worked properly and you had to use like a framing coder intermediate format thing.

**Dave Jones:** It was a real pain in the ass and I just gave up trying to do it cuz I love HandBrake, but I don't want to have to do a two-step process.

**Dave Jones:** I don't want to have to I used to do this many years ago for all of my YouTube videos. I used to render in super high quality, super bit rate from my from Vegas and then I would use HandBrake to then um, transcode that into a for, you know, a smaller file size, constant quality version that they not upload to YouTube or upload to my podcast uh,

**Dave Jones:** version in 720p, which I still do, by the way. So, I still use HandBrake for that, but so yeah, if we go back here, now because I've installed this, we've now got the Voukoder plugin and I've got this and let's have a look at the customized template.

**Dave Jones:** Now, you can't actually do much here cuz it's all inside the actual program, which I'll show in a second, but what it does is it actually takes your project settings.

**Dave Jones:** So, you have to go over to your file, project settings. Um, so yeah, so these project settings here are the ones that will render. You can't actually change it.

**Dave Jones:** You've got to change it in your project, which is different uh, to how you'd normally do it. But anyway, um, so let's go into here and we'll show you the dialogue box which pops up.

**Dave Jones:** Here it is. There we go. So, we can choose our codec H.264 and we can use the Nvidia card or can use the X.264 uh, which is just the uh, CPU doing it or you can choose, you know, any other whatever.

**Dave Jones:** But anyway, I'm going to use uh, Nvidia NVEnc. Um, and then the options here, I've got a GeForce uh, 1070 card for those playing along at home. And the quantizer value or constant quality factor is set to 23.

**Dave Jones:** What do they tell you? The encoding mode to use, choose constant bit rate, constant quantizer or or variable bit rate. So, we use it's called con- constant quantizer here.

**Dave Jones:** I've never heard that, but it's constant quality um, everywhere else I've uh, seen it. And the the quantizer value seems to be like the same as HandBrake cuz HandBrake uses X.264 uh, as well as the encoder.

**Dave Jones:** HandBrake's just a shell program around that. So, 23, this is a highly non-linear value. So, normally 22, 23 is a typical value you use. The lower the value, uh, the less lossy it is.

**Dave Jones:** Like if you once you get to like, you know, 19, 18, something like that, it's almost lossless. Um, it's, you know, but you'll get really huge file sizes. And if you go to like 25, you start getting, you know, pretty lossy, um, something like that.

**Dave Jones:** So, anyway, uh, 23 is the default value, so we're all going to stick with all the default values there. Uh, the audio is AAC, um, and the output uh, container MP4, you can get different, uh, containers for it, but we're going to use the MP4.

**Dave Jones:** Uh, there's nothing else there. And about Vookoda, Daniel uh, Stankewitz at uh, Lord Vook, thank you very much. Um, translation Bruno T and others. Um, yeah, fantastic. I'm going to uh, I might uh, donate to this.

**Dave Jones:** Yes, donate via PayPal. I'll do that. Um, and I highly recommend you do too if you use it. So, I don't you know, I definitely don't mind paying for software, um, even free software.

**Dave Jones:** I will uh, support them. So, anyway, let's give it a go. Okay, render test three, Vookoda, and we will now get a better uh, box. Version 18 has a better rendering box here.

**Dave Jones:** Um, so that's really good. And it shows you the rendering duration. So, that's not going to go down. So, already you can see it's fast. It was 3 minutes 38 before and it's saying it's going to do this in, well, you know, two and a half minutes, something like that.

**Dave Jones:** So, it is faster than NVEnc. And I just uh, rendered my mailbag video with it and yes, it was much faster. And you'll see, oh, there's a no, there's basically no buffering there anymore.

**Dave Jones:** Look how fast that's going. So, as you can see, yeah, there's no buffering, it's much faster, it's faster than real time. So, this is a 10-minute video and it's going to do it in 2 minutes, under two and a half minutes.

**Dave Jones:** My uh, for a reference, my 50 latest 52-minute mailbag video, I rendered it with this, these exact settings, and it took uh, 14 minutes, um, and 20 seconds or something to render a 52-minute mailbag.

**Dave Jones:** So, that's pretty schmick. Yeah, 2 minutes 34. Sweet. So, that's that's a more than a full that's more than a minute quicker. Wow, that's like a third quicker. That's that's fantastic.

**Dave Jones:** Wow, just there, it's worth uh, using. Anyway, so let's have a look at the file size. Let's see what we got. Aha, unfortunately, it is yeah, I noticed this with my mailbag and I mentioned this on the forum as well.

**Dave Jones:** It is much higher in file size. 360 meg. So, we can actually tweak that though with that QF value, that constant quality value. You can actually tweak it cuz obviously we weren't able to tweak that value in version 17.

**Dave Jones:** So, it's obviously using a more aggressive compression there which I I can play these videos, but look, I I've had a look at these before and you really can't pick a difference between it.

**Dave Jones:** So, I might actually experiment with the quality factor there. I think I'd be surprised if I can't go to a value of 24 there actually. So, yeah, there you go.

**Dave Jones:** But, that's quicker and just for completeness, I will re-render that using a variable bit rate. There you go. High quality variable bit rate. VBR, boom. And here we go.

**Dave Jones:** We're going variable bit rate and that's going to take longer than the constant quality. And constant quality's better than the variable bit rate. So, yeah, why you wouldn't use the constant quality, I don't know.

**Dave Jones:** Yeah, it's now it's going to take 3 minutes 20. But, what I'm really interested in is the file size. And there you have it. 3 minutes 11. So, that's significantly slower than the constant quality and and that's curious, isn't it?

**Dave Jones:** It's almost precisely only 1 kilobyte difference between the constant quality and the VBR version. It's just sheer coincidence, I'm sure. Anyway, yeah, I need to tweak the V coder one, I think to just to get the file size down.

**Dave Jones:** I don't want it to be smaller. Like I was happy, super happy with the quality that I was getting. There was no degradation in the constant quality I was getting from the version 17 Vegas and NVEnc encoder.

**Dave Jones:** So, you know, there's no reason to sacrifice larger file size if it's not actually necessary. So, anyway, I experimented that like I could actually play them now, but you know, trust me, you're you're not going to you're not going to pick the difference.

**Dave Jones:** Like the quality is going to be like you know, like there's the right you've got a different screen. There it is, right? You are not going to pick the difference.

**Dave Jones:** I guarantee it. Yep. I I guarantee you're not going to see it. You're not going to see the difference. So, that's the V coder one and this is the version 17.

**Dave Jones:** Yeah, you're not going to see it. This is not a polished edit. Where am I holding stuff up to the camera? There we go. Yeah, no, it's like you're not going to pick the difference.

**Dave Jones:** There it is. Yeah, the screen capture, pixel perfect, absolutely pixel perfect. No no problems with whatsoever. So, yeah, there's no point like pissing away an extra like 100 and you know, 40 megabytes there.

**Dave Jones:** Like you know, it's like increased by like a third file size. So, yeah, there's no point, but I like the V coder thing. So, thank you very much to those on the Vegas Creative Forum for pointing that one out.

**Dave Jones:** That's I'm going to use that even though the bastards at Magix seem to have removed the constant quality encoding from version 18. Unbelievable. Don't know why. If you know why, leave it in the comments down below, please.

**Dave Jones:** But yeah, anyway, and I had crashes with this, but I've I've done a few tweaks to it and it's it doesn't seem to crash now and the encoder seems rock solid and pretty darn happy cuz it's using the x264, which is what encoder I believe, which is what HandBrake uses and I'm super confident in that.

**Dave Jones:** So, yeah, looks like I really got a good solution now with version Vegas version 18 and I've even got even faster encoding. So, rendering, as I call it. So, absolutely fantastic.

**Dave Jones:** Winner winner, chicken dinner. Catch you next time.
