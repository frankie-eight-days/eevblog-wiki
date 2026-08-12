---
video_id: cm1HFKOOCgo
title: RTX4060 AV1 vs H.265 Encoder Using Handbrake
url: https://www.youtube.com/watch?v=cm1HFKOOCgo
source: youtube-asr
timestamps: {"0": 2, "1": 18, "2": 34, "3": 45, "4": 60, "5": 71, "6": 85, "7": 95, "8": 112, "9": 126, "10": 140, "11": 154, "12": 162, "13": 172, "14": 185, "15": 191, "16": 204, "17": 217, "18": 230, "19": 246, "20": 258, "21": 272, "22": 285, "23": 303, "24": 318, "25": 329, "26": 349, "27": 364, "28": 374, "29": 390, "30": 404, "31": 420, "32": 431, "33": 443, "34": 457, "35": 471, "36": 482, "37": 497, "38": 508, "39": 526, "40": 539, "41": 551, "42": 565, "43": 580, "44": 591}
---

**Dave Jones:** Hi, yet another video on a GPU rendering. I got myself a cheapest chips, the cheapest Nvidia RTX 4060 board that I could find. What is it is a Hang on.

**Dave Jones:** It's a It's a PNY card. It was absolutely cheapest cuz what I wanted cuz I don't know I'm not a gaming kitty. I don't do any gaming. What I wanted is the 4060 the new 4060 chip set that supposedly has the AV1 codec encoder in it cuz I wanted to try that.

**Dave Jones:** Everyone was raving about this AV1 codec and how file sizes are much smaller and it's better quality blah blah blah blah blah, right? A file smaller file size is always better, right?

**Dave Jones:** More betterer. Uh because now these days like I do keep all my raw video files uh by the way and so I drag them so I used to just copy them straight from the SD card straight onto my NAS array and then edit it straight from those.

**Dave Jones:** But now I actually transcode the files first from H.264 which is what I get on the camera to H.265 and I save quite a significant amount of our file size doing that.

**Dave Jones:** And I've got some HandBrake scripts to do that. You've seen this in plenty of previous videos. Anyway, so I've upgraded from the RTX what what is it? 2060 to the 4060.

**Dave Jones:** It's an 8 gig card and it doesn't I don't need any of the I don't need the full 8 gig as I'll show you. GPU temperature 44° C. There you go.

**Dave Jones:** 19% at the moment because I'm doing screen capture. My screen capture is uh using GPU using XSplit. So anyway, yeah, I I've tried it and sorry but AV1 uh at least for my purposes.

**Dave Jones:** Now Um, get support for this I had to actually install the latest nightly build of HandBrake here, right? So, uh yes, I did this snapshot, the latest update from 4 days ago or whatever, right?

**Dave Jones:** So, I've now got that and um here it is. I now actually have file support. Give me 1 second. I now have uh file support and codec support for an AV1.

**Dave Jones:** Now, the release build of HandBrake still does not support the AV1 codec on the NVEnc, which is the Nvidia encoder. It only supports these first two options here, which is SVT.

**Dave Jones:** I believe that's the Intel one. So, you got to have one of those Intel uh GPU cards to actually get that, I believe. So, anyway, I I did try that.

**Dave Jones:** It Well, it Actually, you don't need that. I tried it and it doesn't work. Like, well, it it works, but it's dog slow. I'm talking like four frames per second.

**Dave Jones:** And and I got a pretty grunty um CPU, so, you know, it's like Like, uh for those who want to know, my um CPU um is a Ryzen 9 5900X, right?

**Dave Jones:** 12-core jobby. So, you know, it's it's not too shabby at all as far as uh you know, as far as CPU goes. And it was like three Like, it was nothing.

**Dave Jones:** It was totally two frames per second. I don't It wasn't like it didn't work. Anyway, so, with the uh new daily build, they do support AV1 NVEnc and it does actually uh work.

**Dave Jones:** Now, by default, the constant quality uh codec here is uh 30, whereas I used to use 26 on my HandBrake My HandBrake uh script that I've got, I've got the quality set to 26, which is what I use for 4K.

**Dave Jones:** And it's that's a little bit high uh for 1080p, but I don't notice a difference with my uh sort of content. Anyway, I do have another script which does it at uh 23 uh for 1080 uh P content.

**Dave Jones:** So, if I've got uh, if I'm shooting in only 1080p on the card, I drag it into the 23 quality factor um, transcode of a H.265, right? So, um, I normally I don't use the GUI interface like this, but I'm just showing you that it is now available.

**Dave Jones:** So, um, my other one uses the H.265 NVENC um, encoder. And I've dragged in a file um, here, right? That's not what I This is part of this uh, shoot here.

**Dave Jones:** And um, I've These These are the results here. Let me up. Get rid of that. And yeah, up I Everyone raved about this AV1 being for a smaller file size.

**Dave Jones:** It's not, okay? Here's my H.265 at 26 quality factor, okay? Which is better quality than 30. Uh, the lower that number, the better the constant quality of your video is going to be.

**Dave Jones:** And that's 674 uh, meg for a um, oh, what's the I'm going to have to I can tell you what the up Hang on. Uh, I'll get there in a sec.

**Dave Jones:** Give me a second. Da da da. I'm not going to edit this video. Sorry. Um, it is uh, uh, it is 1.85 gig. So, the raw video file is 1.85 gig, okay?

**Dave Jones:** And it goes down to That's H.264 uh, and it goes down to I can show you that actually. Properties. There it is there. Okay, there's the file that I transcoded.

**Dave Jones:** Uh, you know, 4K uh, 3840 by 2160. Um, and yeah, just a standard uh, camera H.264. I did it to H.265 with 26 quality factor. I got 674. Exactly the same quality factor with AV1 using the NVENC encoder.

**Dave Jones:** So, the new AV1 core in there, 1 gig. 1 gig. Why? Why would I Why would I use it? I don't know. Leave it in the comments down below, but I Everyone was raving about this AV1 codec.

**Dave Jones:** Maybe the NVENC implementation is not as good as the Intel implementation. Uh-huh. I'm not going to go bloody buy another Intel Intel card just to do that. Anyway, um yeah, disappointing.

**Dave Jones:** So, and once I change it to 30 quality factor, it's 951. It's still not as good. Worse quality factor than the than the H265. So, AV1 compared to H265 it's no contest.

**Dave Jones:** I'm still going to use H 265 and and I can actually run it here starting code same as source. So, NVENC encoder. Yeah, yep, NVENC encoder. We're all good.

**Dave Jones:** Yeah, I think we're all good. I can start that encoder. And I was getting about 100 Well, with my script, I was getting about I'm now getting with 4K I'm getting about 125 frames per second.

**Dave Jones:** This one's doing 137. So, it's pretty good. It might be faster, but let me Okay, so like an average frames per second 132. There you go. So, I can stop that now.

**Dave Jones:** Are you sure? Yes. And then I can change it over to H265 also on the new using NVENC on the new 4060 card and I can start that. Everything's exactly the same.

**Dave Jones:** Okay, so all exactly the same settings. And yes, already exist. Overwrite. So, what was that? 132 or something? Let's compare it. Simple speed comparison here. There's not much in it.

**Dave Jones:** It's It's the same average, right? So, it looks like the NVENC is the same either way. By the way, GPU video and code it does H.265 shows 100% here for that.

**Dave Jones:** But as I said, I'm screen capturing here. So are you willing to stop? Yes. Let's change it back to AV1 NVidia Inc. Let's start the encode again. Yes. Boom.

**Dave Jones:** And I found that the AV1 did not go to 100%. Which was It It probably will now because I'm doing the screen capture in the background. But I found I find that it went to like 70% or something like that.

**Dave Jones:** So anyway, yeah, it's only using 2 gig of the 8 gig dedicated memory on the card. So like there's no difference. If you just want to do encoding like this, just get the cheapest shittiest card.

**Dave Jones:** It makes no no difference between the 4060 or the 4060 Ti. I don't believe there's any difference because it's the rendering core in the chip. Yeah, if you're doing any of your other graphics, you're a gamer kitty and doing your other graphics, yes, it's got more cores for other things, but that doesn't matter for the encoding.

**Dave Jones:** The encoding engine's actually the same there. So Yeah, GPU only gets to 55. Oh, no. No, it's peaking. It's cooling down a bit, isn't it? I can't hear it.

**Dave Jones:** So at 51. Right? Oh, no. No, it just finished cuz it just finished. There you go. So anyway, there you go. No AV1. Everyone's raving about it. Nope. Nope.

**Dave Jones:** I'm going to stick with H.265 encoding. Thank you very much. Anyway, yeah, it's I got it quite a significant boost going from the 2060 to the 4060 in terms of HandBrake transcoding.

**Dave Jones:** 4K is my 1080p stuff is about 480 frames per second, which is really quick. I think I was only getting 330 350 before or something like that. So, it's significantly faster with the 4060 compared to the 2060.

**Dave Jones:** And 4K is now 100, you know, 30 odd frames per second there. And I used to get like, I don't know, 80, 100, something like that for the my 4K with the older card.

**Dave Jones:** So, it's a decent improvement for the 4060. There you go. Yeah, AV1, no. As far as I'm concerned, it's a loser, but you know, your mileage may vary. Catch you next time.
