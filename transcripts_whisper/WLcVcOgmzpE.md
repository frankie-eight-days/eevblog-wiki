---
video_id: WLcVcOgmzpE
title: Blackmagic Davinci Resolve CPU vs GPU Rendering
url: https://www.youtube.com/watch?v=WLcVcOgmzpE
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 33, "3": 57, "4": 73, "5": 85, "6": 101, "7": 117, "8": 129, "9": 145, "10": 157, "11": 177, "12": 193, "13": 209, "14": 233, "15": 245, "16": 261, "17": 273, "18": 289, "19": 305, "20": 325, "21": 345, "22": 361, "23": 381, "24": 393, "25": 413, "26": 429, "27": 445, "28": 461, "29": 477, "30": 493, "31": 513, "32": 525, "33": 541, "34": 565, "35": 577, "36": 593, "37": 609, "38": 625, "39": 645, "40": 665, "41": 681, "42": 697, "43": 717, "44": 733, "45": 757, "46": 773, "47": 789, "48": 805, "49": 825, "50": 845, "51": 869, "52": 893, "53": 905, "54": 933, "55": 949, "56": 965, "57": 981, "58": 1005, "59": 1021, "60": 1045, "61": 1057, "62": 1073, "63": 1089, "64": 1105, "65": 1125, "66": 1145, "67": 1165, "68": 1189, "69": 1201, "70": 1217, "71": 1233, "72": 1249, "73": 1265, "74": 1285}
---

**Dave Jones:** Hi, I'm excited. Look what just turned up. Thank you very much. Oh, I go full screen here. Thank you very much. Blackmagic Design, they sent me this DaVinci Resolve Speed Editor. Check it out. Oh, it's a Bobby Dazzler. I've been thinking about getting one of these, but yeah, I was talking

**Dave Jones:** about it on Twitter or something and they saw it and they said hey, do you want one? Yeah, beauty. Alright, so here it is. Oh, it's beautiful. Oh, I'll have to do like a separate video on this. So this won't be a video.

**Dave Jones:** Oh, that knob. Oh, that knob. Oh, just the feel and the weight in it and just the velocity of it. Oh, it's beautiful. Thing of beauty. And these keys are absolutely gorgeous. This is not feel-o-vision, unfortunately, but these keys feel absolutely first class, like 1980s IBM

**Dave Jones:** first class. Oh, it's beautiful. So anyway, this is supposed to speed up your editing, because if you don't know, I do my where is it? Ah, here you go. I use DaVinci Resolve. I switched I can't remember the exact date. Probably been using it for like a year now

**Dave Jones:** I think. I switched over from Magix Vegas, which used to be Sony Vegas, and then I've used other packages before that. And everyone was, yeah, I had problems. Everyone was raving about DaVinci Resolve and everything, so I tried it, and it suited my workflow.

**Dave Jones:** I really liked it. So I've been using that ever since. It only took me a couple of videos to get into it. Yeah, but I've been using DaVinci Resolve for all of my stuff. I even use it for like editing the Ampere occasionally, just doing audio editing, because

**Dave Jones:** it's just, I'm familiar with the workflow and stuff. Anyway, yeah, I've been using the free version up until now. I've been meaning to get the full version, but thankfully this one actually came with the license. So this video is not going to be about using this lovely speed

**Dave Jones:** editor, because I'll have to try that later, and I'll do a video on does this make, you know, how much of a difference does it make, just to someone who doesn't do like, I just do YouTube editing. I just join clips together, you know, put a couple of overlays

**Dave Jones:** in and Bob's your uncle kind of thing. Will that speed up my workflow? I don't know, because if you don't know, like, I think getting this like, I was looking at getting one of these, buying one of these, because it's only like, I think, maybe $100, $150 more than

**Dave Jones:** just buying the software license for DaVinci Resolve. So yeah, I thought, rather than just buy the license, I thought I might as well get one of these, for not much more. So anyway, check out, it depends on sales in your country and all sorts of things like that.

**Dave Jones:** Anyway, I do have, so this video is going to be me testing out the new licensed version, which actually supports GPU rendering. Because all the stuff I do, the only real major difference between the, at least for my use anyway, for the free version

**Dave Jones:** as opposed to the paid version of DaVinci Resolve editor, is that it supports, the paid version supports GPU rendering. So all my rendering and everything else, and also I believe just actually playing the video like this and stuff, does not go through the GPU.

**Dave Jones:** So those who are curious to know what machine I run here, I'm running an AMD Ryzen 9 5900X. So it's actually quite a beastie processor. In terms of, it's really pretty good. I think it's got a pass mark of 36,000 or something, 40,000 or 36,000, something like that.

**Dave Jones:** Anyway, it's quite a beastie processor. And my graphics card, I've just recently upgraded to this. I've got an RTX 2060. None of that new, modern, fangled 3060 rubbish. I've got an RTX 2060. So I thought, you know, it does make a difference when I'm using Handbrake, my X and X264

**Dave Jones:** which is what Handbrake's like, the shell around it. So I use that for transcoding. Now I actually, when I get my videos on my card, I do actually transcode them now. I never used to, but it was taking up too much space for the raw footage, which I keep all my raw footage.

**Dave Jones:** So I actually, so I transcode those with Handbrake. I've got a script which actually does all that for me. It's dragged the files in, boom, and 10 minutes later it's all transcoded. So I work on those. So anyway, will an RTX 2060 make any difference to my rendering?

**Dave Jones:** Now, rendering is not a big deal for someone like me. Once I've edited my thing, it's all about the editing. Once I've edited it, I just set it to render, and who cares? You know, it's relatively quick. Who cares if it takes an hour to render?

**Dave Jones:** I go off and do something else. It's not a big deal, right? Now, when with just the CPU that I'm doing at the moment, I think, don't quote me on this, it depends on the type of footage that you're actually rendering, but most of my videos are 1080p, okay?

**Dave Jones:** So I shoot them in camera at 1080p. Unless I'm doing a teardown like this one, which the teardowns I shoot in 4K. I'm shooting this one, actually, in oddball. I'm screen capturing this at 2K. So this is gonna, I can't remember the last time I did a 2K video.

**Dave Jones:** Anyway, I'm gonna edit this in DaVinci Resolve after this. Anyway, I'm waffling too much. DaVinci Resolve using CPU only, rendering 1080p footage, it renders it 5 times real speed or more. It's really quick. So if I've got a, you know, 30 minute video, it renders it in 5 minutes.

**Dave Jones:** Like, it's really quick. The only thing it's really slow on is 4K footage, which this particular one, that's why I've got this project open here. I'm gonna do a test render with CPU. I'm gonna time it doing CPU only. Then I'm gonna install the new

**Dave Jones:** DaVinci Resolve software that I've got. Thank you very much. And I'm going to, hopefully, I assume it just magically enables the GPU, and I'm gonna render the exact same footage using GPU to see what the speed improvement. Now on the CPU, 4K footage, it generally renders about real time.

**Dave Jones:** So a 30 minute 4K video will take about 25 to 30 minutes to render. I think it's slightly faster with the GPU. But as I said, it's not a big deal, but it's handy, right? So that's the only, really, I think the only major improvement I'm gonna get out of having the licensed

**Dave Jones:** software. But I was gonna buy it anyway, because I wanted, you know, why? It's better. And I use it. I want to pay for the software that I use. I've been using this free version for far too long. So, anyway, yeah. Ironically, they gave me a free version of this.

**Dave Jones:** So, thank you very much, DaVinci. Anyway, yeah. So this is a, actually this is a mix. This project is a mix of, it's, how long is it? Okay, 1946. So 20 minutes long, right? So this is a 20 minute 4K, but it actually has a mix of

**Dave Jones:** I believe this footage here I shot is 1080p. So the talking head stuff, but all the teardown stuff is in 4K. So it's a mix of source material here. So, yeah, that'll be an interesting thing. I will render it using my normal thing.

**Dave Jones:** So this is my finished project. I uploaded this video, so I'm gonna render it again. So let's go ahead and do that. Okay, so I'm gonna render this to my solid state drive. All the source files are coming from my NAS, which is downstairs.

**Dave Jones:** But trust me, the source material, it makes no difference to the rendering speed that the source material comes from my NAS. Trust me, I've tested this, okay? And it really makes no difference that I'm writing to a solid state drive. I've also tested that.

**Dave Jones:** But, for those people who like to bitch about it, I'm writing to my solid state drive, okay? So I'm gonna, so this is CPU rendering, okay? I normally this is how I'd normally render. I'd usually use MP4. I'm gonna use H.264. I might do H.265 as well, so I might

**Dave Jones:** run this process twice. I think I'm gonna start to go to H.265 now, because it is slightly smaller file size and supposedly higher quality. I don't see it in the videos that I do. Just the talking head videos and the screen capture videos, they compress perfectly.

**Dave Jones:** Like, I just don't see it. So all that, you know, it really doesn't make much of a difference to my content. Anyway, 4K footage, okay? 3840x2160, 29.97 frames per second. I never use best. As I said, I can do least, okay? With my footage, it makes no difference whether I render with

**Dave Jones:** best video quality or least. You won't see a difference for my content, for the talking head stuff, or for, you know, but if I'm doing like an outdoors video, I just rendered one a couple of months ago where I was doing downhill mountain biking and stuff, right?

**Dave Jones:** That matters, okay? It really matters a lot to get the right quality and all that sort of jazz. Anyway, I will typically go low, okay? Like this. So I will typically go low like that for my 4K, okay? So I'm going to start this now and we'll time it.

**Dave Jones:** I will put it over here and I will render, okay? Go. Go, go. Go, you little beauty. You can see that it may be a bit slower because I'm doing screen capture in the background. I don't know how that impacts it. You can see, like, it's getting down to about 22 minutes there.

**Dave Jones:** Right, 20, right? So it's already rendering faster than real time. Okay, 17 minutes. Oh no, but this is rendering no, at the moment it knows it's rendering the 1080p footage so it's going to get slower later when it switches to the 4K footage.

**Dave Jones:** Anyway, I'll get back to it. And here we go, it's about to finish. 99% in 16 minutes and 21 seconds. And you can see before, it actually did it in 18.45, so I don't know what the change is. Maybe I was doing something else

**Dave Jones:** in the background. I could have been watching videos, doing whatever, maybe, and it was sucking the CPU. Now I'm going to do H.265. I've changed the file name low here. Let's add to render queue and let's go. Should be a little bit slower.

**Dave Jones:** It takes, you know, a bit more resources to encode H.265, I believe. So there you go, that was 18 minutes and 14 seconds, so it took a couple of minutes longer. So we've got a reference there. If you are curious about the file sizes, the H.264 was 2.57

**Dave Jones:** gig, and the H.265 was 1.93 gig. So smaller file size, both on the low quality setting, which trust me is not low for my content. And I'll do a 1080p screen capture video here, just for the other extreme. So this is super quick, you can see before it did it in

**Dave Jones:** 4 minutes and 50 seconds, and this is a almost 30, 29 minute long video. So let's try that again. So H.264 low, let's go. What? There it goes. No, it won't take 1 hour and 40, and 2 hours and, no, 20 minutes. 11 minutes.

**Dave Jones:** Would you believe 9 minutes? Would you believe 7? It'll come down. Yeah, 6 5, yeah, yeah. It's only going to take like 4 minutes. So as I said, like even with the CPU version, the free version of DaVinci Resolve for 1080p content, and it's a bit faster because this is

**Dave Jones:** screen capture stuff, so everything's pixel perfect, so pixels don't change from scene to scene except for my talking head and whatever's happening there with the cursor or whatever. So yeah, it's but my regular 1080p content, as I said, is like 5 times real time

**Dave Jones:** or something. It's very quick. So yeah, I don't have a speed problem with the free version on 1080p. It's really for 4k stuff that I'm really looking forward to. 7 minutes, 7 seconds for H.265 compared to 4 minutes 28 for H.264 there. If you're concerned about the file size,

**Dave Jones:** 419 meg for H.264 and 344 meg for H.265. Now I'm going to install my new license and hopefully it just auto magically works and does faster GPU rendering. I'm not sure if I have to put it into settings or whatnot. I don't think so.

**Dave Jones:** Yes, you can see here that the NVIDIA GeForce is it detects it, but it's not enabled or whatever so I've got to find a way to put in my code Okay, for some reason, after all this, my camera has died. My AVerMedia HDMI capture card, I don't know

**Dave Jones:** I'm going to have to sort that out later, so sorry, you can't see my ugly mug anymore. Anyway, I couldn't figure out how to install the serial number and the registration code. I don't think it's actually possible. So I had to, like in the free version, so I had to

**Dave Jones:** actually uninstall it and then reinstall the complete one from scratch and go through the website and register and all that sort of jazz. It kept all my projects, even though I did back them up, it seemed to have kept them just fine. So I don't know, yeah, excellent.

**Dave Jones:** Alright, so, I'm assuming, there's some new stuff over here as you might see. So H.264, I'm going to call it GPU low, I'm not going to touch any of that stuff. I'm sure that stuff's new, right? It wasn't there before, am I imagining that?

**Dave Jones:** Anyway, add to render queue, okay. Yeah, let's go. Alright, render. And render in progress. I assume it's just going to automatically use the GPU. 12 minutes. 10 minutes. Oh yeah, now we're talking. There you go. No, because it's doing the 1080p stuff at the moment.

**Dave Jones:** I will reserve judgement until it's done. It took 18 minutes before. But anyway, I'll get back to you. Alright, it's about to finish. Look, 13 minutes. How do I get rid of this? Anyway, you saw it, 13 minutes and 12 seconds. I'm very disappointed in that.

**Dave Jones:** Okay, it's quicker, and it was using 100%. I'll bring this in here. But it was actually using, I'll put up a screenshot, you can see, it was using 100% of the GPU here. But it was using some shared GPU memory. So my RTX 2060 only has 6GB of memory.

**Dave Jones:** That's the reason. The RTX 2060 sucks. You've got to get a 3060. Right? God, I expected better. Okay. Because it's using a couple, it was using like 2GB or something, or 3GB of shared GPU memory there. So I did actually switch off my screen capture, because my screen capture, my

**Dave Jones:** XSplit software does actually use the GPU, it tells me. It's currently using, in recording this, about 17% of the GPU. Well, you can see it there. You can see it's using that 17% there. So I did actually switch it off during this. So it wasn't that.

**Dave Jones:** And it wasn't doing anything else. It was like, just like, what? Okay, 13 minutes. Okay, it's quicker. Great. But not radically different. Okay. I'll try X265. See if that makes a difference. There it is, running there. It's almost done. I just fired XSplit back up, and it's

**Dave Jones:** once again, like 17% of that GPU will be taken by the video capture. But anyway, there you go. It looks like it's finished. Yep, it's finished. There you go. So it definitely does. It is using GPU rendering now, because before it was using no GPU, and it was

**Dave Jones:** using like, you know, 90% CPU, or whatever. Now it's using a couple of percent CPU, and all GPU. So it's definitely doing the business. But yeah, I don't know whether or not that's because I've got a RTX 2060. Yeah, there's a 2040 now.

**Dave Jones:** Sorry, a 4060 or whatever is the latest. Is it? I don't know. Is it because I don't have enough dedicated GPU memory, and it then has to go outside? Or is that I don't know. It's using some of that shared, because that's doing the

**Dave Jones:** decoding, or the other screen updating. I don't know what. But yeah, anyway, so I'm disappointed. That took 14 minutes and 44 seconds, compared to 18 minutes and 14 before, and 16.21. You can see the times up there. So really, that's disappointing. I expected better from a, you know, a 2060 to me

**Dave Jones:** is still a fine cut. Okay, I just got it second hand on eBay. Got it cheap. But jeez, you know, like I expected better. Sure, okay, it's not the latest whiz-bang 4060 or whatever, with you know, 16 gigs of memory. But yeah, I expected better.

**Dave Jones:** So that's kind of disappointing. Still, it is better than what I had. So yeah, okay, thumbs up. Okay, I'm going to try the Karno MAP-1 again, H.264. So this is a 1080p screen capture, so this is as easy-peasy as it gets. So we've got 4 minutes 28 to beat, and

**Dave Jones:** 240, 230. This, so my content in this one doesn't change. So it looks like, yeah, it looks like it's going to do this in half the time. Yeah, I don't think, you know, there's the odd overlay in this, but like, odd text like you just saw

**Dave Jones:** there, but pretty much nothing else. So, and by the way, like, I don't do any color rendering, I don't do any of that you know, fancy whiz-bang editing stuff. I simply join clips together, you know, maybe tweak some audio levels here or there.

**Dave Jones:** I add a couple of text overlays or image overlays and that's it. I don't do anything fancy at all. Ah, I just discovered over here there's a drop-down box that was set to auto. The encoder used was auto, not NVIDIA. So that is interesting.

**Dave Jones:** So it uses the, so I presume that in the native, like the auto mode, which would have got native, right? Or was it native? I can't remember. Anyway, the native mode, it's using the DaVinci Resolve one, but it's doing it on the GPU.

**Dave Jones:** But in this case, the NVIDIA, it was, but there is an encoder core inside the NVIDIA chipset. But you saw that on the usage graph, that it was actually using the encoder built in. So it's interesting. Anyway, I just did the CardioMap one in 2 minutes

**Dave Jones:** 30 seconds for the H.265 using that NVIDIA one. So now I'm going to go back to the 4K one and do that again, see if it makes a difference using the NVIDIA encoder option. Okay, so H.264 encoder NVIDIA like this. Let's choose our low quality

**Dave Jones:** down here. I won't change anything else. I've got NVIDIA in the file name. And let's run that again. 13 minutes 59 seconds. Well, that's interesting. That's actually more than the 13 minutes and 12 seconds using that non-NVIDIA, like the native option or whatever.

**Dave Jones:** So yeah, there you go. That made actually no difference. Surprising, huh? And it looks like the H.265 is not going to be any quicker on that, unfortunately. So there you have it. I mean, we're talking, yeah, there's been an improvement with this registered version with GPU rendering, you know, like

**Dave Jones:** 25% or something like that. Although, with the H.264 what was it? Double or something. It was twice as fast. So it halved the speed. But yeah, as far as the 4K stuff, which is the one I had trouble with. So yeah, not a massive improvement, but worthwhile.

**Dave Jones:** But once again, if you got a bigger, beefier graphics card, more modern than my RTX 2060 with 6 gigs of RAM, then maybe, yeah, you're going to get a better improvement. One thing I want to test, though, is can it actually play things quicker?

**Dave Jones:** Because it was like stuttered and things like that. It was kind of annoying. It was really hard to reproduce, actually. In fact, it's still the same thing. Oh no, there we go. I'm just pressing my spacebar to start, stop. Nah, it's got a similar thing.

**Dave Jones:** I was hoping this would be quicker. Anyway, I won't be able to tell you that until I actually do a full edit on the thing. Yeah, but it was editing 4K was rather, like, sometimes it was smooth as silk. Others, it was jerky.

**Dave Jones:** And really frustrated me and stuff like that. And I've tweeted about that a few times. So I presume that the GPU stuff will fix that, because it'll do, like, the GPU everything on the screen, like the preview and all that's all happening in the GPU.

**Dave Jones:** So yeah, anyway, so that remains to be seen. But anyway, so if I call up, like, with overlay text, there it is. Boom. No problem. So yeah, it comes on. Anyway, there you go. So not a massive improvement with the H264. I'm sorry my camera

**Dave Jones:** fails and you can't see my ugly mug anymore. But anyway, there you go. Thoughts and comments down below. It's an improvement but yeah, I guess I need a more better graphics card. Catch you next time.
