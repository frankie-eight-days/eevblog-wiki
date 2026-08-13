---
video_id: C9pw5z6jI0U
title: RTX4060 AV1 vs H265 Davinci Resolve Rendering Test
url: https://www.youtube.com/watch?v=C9pw5z6jI0U
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 25, "2": 50, "3": 75, "4": 95, "5": 112, "6": 128, "7": 144, "8": 161, "9": 177, "10": 194, "11": 216, "12": 238, "13": 262, "14": 280, "15": 295, "16": 319, "17": 337, "18": 359, "19": 376, "20": 393, "21": 414, "22": 436, "23": 453, "24": 478, "25": 495, "26": 511, "27": 533, "28": 552, "29": 566}
---

**Dave Jones:** Hi, just another quick video on this new RTX 4060 card that I've got and the AV1 codec, which it has a hardware AV1 encoder on it. Just a follow-up video, I just used DaVinci Resolve, first time since I've installed this card, and what do you know?

**Dave Jones:** Bingo, check it out, it pops up with, ta-da, AV1. So AV1 is now an option. There is no CPU option with AV1, it's just using the NVENC core on the NVIDIA card. So that is now an option, pretty groovy. So I won't waste any time, I've actually rendered just this video which I'm about to release now,

**Dave Jones:** which is a 15 minute long, 15 and a half minute long video, just typical bench content, you know, moving stuff around on the bench and, you know, things like that. So let me give you the results here. So what I've done is I've rendered both using AV1 and H.265, which is what I'm normally using now.

**Dave Jones:** I used to use H.264, but pretty much standardized on H.265 now. And of course, when you do H.265, you get a choice of the, you can use the NVENC core, so GPU encoding, or you can use native, native means CPU encoding. So I've done all that, and then we can set the quality here from least to best.

**Dave Jones:** When I render my videos, the type of content that I do, if I'm just doing my regular bench stuff or talking head stuff or something like that, I just set low quality here. Because, you know, unless, like, I would choose something different, if I'm doing, I'd choose a higher quality thing.

**Dave Jones:** If I'm doing downhill mountain biking videos or something like that, you know, outdoor content with lots of complex stuff in there, you know, I wouldn't be using low. But that's a totally different thing. For almost all my content, I cannot pick the difference between low and best.

**Dave Jones:** There's no difference whatsoever. If I'm just waving my hands around, talking head, you know, whiteboard or bench or something like, low is fine. And for those on the previous video, those who said, oh yeah, it's because the constant quality factor varies by codec.

**Dave Jones:** Yes, it does. It's going to vary by codec. So once again, I don't know what this is, right? I'm going to choose automatic. Look, I can restrict to a bitrate, but that's not something that I want to do. As a content creator, I want to pretty much get, like, consistent quality regardless.

**Dave Jones:** So I don't want to have to think about what type of content that I've shot and to set, like, a target bitrate or something like that. I don't want to have, like, complex video information, which then if I chose a target bitrate, which is, no, it's just no, right?

**Dave Jones:** I just don't want to think about it. So I do, that's why in handbrake transcoding, I use constant quality. I don't use constant bitrate. And so yeah, you can tweak the constant quality and then you can start pixel peeping and to figure out what the optimum constant quality is for which codec and stuff like that.

**Dave Jones:** You know, okay, that's a huge rabbit hole, right? You can spend a whole week just in full time just testing that sort of crap. Anyway, so I'm just going to use automatic quality here. All these settings are the same down here. Everything else is, this is just 1080p content, 30 frames per second, and these are results I got.

**Dave Jones:** So this is it. I won't bore you with any more details. So the AV1 codec on low quality factor for the 15.5 minute video, 634 meg there. And the CPU on low, so on H.265 CPU, is half that, basically. Yeah, almost half that.

**Dave Jones:** 349 meg there. And H.265 on medium, so the difference between low and medium for CPU encoding using my Ryzen 9. Because CPU encoding, everyone says that, everyone pretty much, all the experts pretty much agree that CPU encoding is technically better quality than GPU encoding.

**Dave Jones:** So better quality for a given file size, but it's slower. So, you know, that's sort of like the trade-off thing. So low and medium, yeah, there's a significant file size difference there, but I can't spot any quality difference at all between all of these options.

**Dave Jones:** I just, I just can't see it. Maybe if I go in there and still frame and pixel peep in a motion part of it, maybe? Like, you know, but no, no, I just can't see it for my type of content. Anyway, I just thought this is interesting.

**Dave Jones:** And then H.265 using the NVENC NVIDIA GPU are 404, and that's on low. So CPU versus, you can see that CPU is a slightly lower file size, and technically a lot of people say it's better quality. But I don't know, because I don't know, how does DaVinci Resolve implement this?

**Dave Jones:** I assume like it's a constant quality thing, right? You're choosing a quality. Well, it is, right? That's essentially what it's telling you there. It's a constant quality. But however they implement that, how the codec, how the GPU decides to, the algorithm for the GPU decides to do that quality thing

**Dave Jones:** as opposed to the CPU algorithm, they're differently implemented, eh, gets all complex. But there you go. Anyway, so low and medium from 404 almost doubles there, not quite. From low to medium there, but as I said, I can't pick the difference. And AV1, low, medium, 634, 2, 1 gig there.

**Dave Jones:** So really, the constant quality, I'm seeing a similar sort of result here, as I did on handbrake for the constant quality. Like I can't tweak the value, like I can't tweak a number in there, as far as I'm aware. Like, you know, I can go down here, I don't know,

**Dave Jones:** because this automatic, right, low, it hasn't greyed out this stuff, so I can still, oh no, constant QP. There you go. Okay, rate control. Okay, I've just always left it on the default, which is variable bitrate. So I don't, yeah, it looks like, yeah, I can tweak with that as well.

**Dave Jones:** So, oh God. It's all too hard. It's all too hard. Anyway, for those curious, there's just some results in DaVinci Resolve. I don't plan on using AV1, I'm just going to stake with H.265. By the way, I did use H.264 using NVENC. I didn't go any further, but compared, so that one and that one,

**Dave Jones:** if you compare those two, yeah, the H.264, 889 meg, as opposed to 759 for exactly the same encoder. So H.265's a bit more better, you know. So, yeah, I just use H.265, it's a standard now. Yeah, YouTube support AV1, and yes, I know about all the streaming thing.

**Dave Jones:** I'm not a streamer, so, you know, it doesn't really matter. So, yeah, there you go. I've got a similar result under DaVinci Resolve. Maybe I could play around with this rate control thing down here, perhaps. And then you can do, like, and then you can experiment with 2-pass, right?

**Dave Jones:** And then tune in, low latency, I've got high quality, and then 2-pass, whether you want 2-pass encoding and stuff like that. So if you really, absolutely wanted to get the best quality, the absolute lowest quality, sorry, what am I thinking? If you wanted to get the absolute best quality you could for a given file size,

**Dave Jones:** yeah, you'd put on, like, two, and you didn't care how long it took. You'd use CPU encoding, and you'd do, like, 2-pass encoding, and, you know, stuff like that. And you'd probably do constant quality, unless you knew exactly what the content was, and then you could tweak the optimum bitrate,

**Dave Jones:** and, you know, it's complex stuff, right? It's just, but my render, like, I don't really care how long my renders in DaVinci Resolve take. It's not really a problem. I finish my project, I hit render, and, like, you know, this is done, oh, by the way, speeds.

**Dave Jones:** I can show you the speeds. Here you go. Speeds for reference. Ta-da! There they are. So, 1 minute 12, that was for the AV1. There was no difference in speed between the AV1 medium and low. And then the CPU low here, CPU medium took 2 and a half minutes.

**Dave Jones:** Okay, so you can see CPU is, like, significantly slower. And then the NVENC took a minute 5, so a smidge faster than the AV1, 5 seconds faster than the AV1, no real difference there, really. So, yeah, there you go. I'm just going to stick with H.265, I think.

**Dave Jones:** But it's good to know that, because the AV1's kind of new, and a lot of people are saying, well, some people are saying, like, oh, yeah, just avoid it, wait a couple of years. But it's good to know I've now got a video card that supports hardware AV1 encoding

**Dave Jones:** if I need it in the future. Anyway, catch you next time.
