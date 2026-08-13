---
video_id: yKflC-fmSX8
title: CPU Thermal Ghost
url: https://www.youtube.com/watch?v=yKflC-fmSX8
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 16, "2": 43, "3": 69, "4": 90, "5": 106, "6": 127, "7": 146, "8": 167, "9": 183, "10": 200, "11": 222, "12": 249, "13": 275, "14": 299, "15": 316, "16": 333, "17": 350, "18": 376, "19": 399, "20": 417, "21": 439, "22": 457, "23": 470, "24": 486, "25": 503, "26": 519, "27": 532, "28": 550, "29": 565, "30": 581, "31": 599, "32": 624, "33": 642, "34": 663, "35": 685, "36": 703, "37": 725, "38": 739, "39": 760, "40": 777, "41": 800, "42": 817, "43": 835, "44": 852, "45": 868, "46": 886, "47": 902, "48": 921, "49": 938, "50": 959, "51": 974, "52": 990, "53": 1004, "54": 1020, "55": 1037, "56": 1061, "57": 1079, "58": 1095, "59": 1117, "60": 1136}
---

**Dave Jones:** Hi, I've got a bit of a problem with my main machine here that I do my video editing and rendering on. It's shutting down on me due to a thermal problem by the looks of it when I do CPU rendering. Anyway, I've got an AMD Ryzen 9 5900X.

**Dave Jones:** It's a 12-core jobby running at 4.2 gig. I've had it for quite a few years now, and it's quite a beastie processor for rendering and stuff. Anyway, I thought that I'd just have a look and investigate why it's doing this. What I've got is I've got batch files here, and these are what I do my transcoding with.

**Dave Jones:** So this uses Handbrake, so I've got a little script there, it's just a batch file. And let me drag in a 4K video, and we'll do x265 conversion, and see if we can make this fail. So there's my script there, it's running, it's running, and CPU, you can see that the CPU is going up.

**Dave Jones:** It's not quite 100% though, so I'm not exactly maxing it out, but the CPU package is now at 80 degrees. Now CPU is 72, it's saying, it's jumped up 73. I did set the bias to ignore, but it still did it anyway. But it's probably not, I bet you it's not going to do it, the bastard.

**Dave Jones:** Because I have been on flat out 100%, so maybe this is not the best file to work from. Should have shut down the whole machine, like the whole machine just shuts down. Whole machine just reboots. But I do believe the CPU maximum is 90, or it's supposed to be or something.

**Dave Jones:** So all the voltages and everything else is fine, and yeah, go in the comments down below, go! Just like, everyone's going to be an expert in the comments down below, knock yourself out, go! Hey, there it goes! There you go. Anyway, yeah, so I will eventually on this machine here, it will reboot.

**Dave Jones:** And I will get a, I've got a Zeus A580, oh no, no, it's booted. No, it's doing the Windows thing. Oh, usually it gives me an error message saying CPU over temp. Put up a screen, I'll insert a screenshot here, because I did actually take a photo of it, I put it on Twitter.

**Dave Jones:** And yeah, it's okay, Windows is booted again. But it shuts down. So obviously, there's something wrong with this stupid thing. And I have noticed the error message, like the bias boot message, very occasionally just saying CPU over temp. But that's because it was set to like 80 degrees, and it had just like, it always worked fine.

**Dave Jones:** So this has only happened recently. I've always flogged the CPU at 100% doing rendering, hasn't been a problem. So, I suspect that, um, yeah, either something's come up, like a fan, well the fan seems to be operating at normal speed, 1300 RPM or something, the bias says.

**Dave Jones:** I should, CPU fan, 1300, um, yeah, go on, crap all about my bias. Crap on, all about all your technical doodads, it's not set up correctly. Oh, your envelope's not set up correctly for your fan control, everyone on Twitter told me all about it.

**Dave Jones:** Yeah, yeah, yeah, go on, go on, um, knock yourself out, really. Um, anyway, so I did set it to ignore, but it still doesn't. So obviously, I think, like I have seen it, like when it boots up, it pops up with, you know, CPU over temperature error, press F1 to continue or something like that.

**Dave Jones:** Um, but it's never been a problem, it's never shut down, but I've seen it happen maybe less than a handful of times over the last six months. Um, but this is the first time that it's shut down using, like, handbrake transcoding. So, yeah, I assume that either something's happened, um, or, you know, like, you know, in terms, like, physically, um, the thermal paste has dried out, I don't know, the heatsink's come loose, I don't know.

**Dave Jones:** So, anyway, I'm going to pop her open now, but, uh, yeah, it didn't come up the message because the CPU's only at 54 now, but it definitely shut off, so let's open this stupid thing. Headlamp time. So, yeah, I think the most likely problem here is that something's physically failed, like it's aged, the thermal paste has aged, or, you know, something like that might have even come loose because they're spring-loaded heatsinks, aren't they?

**Dave Jones:** I don't know how this one connects, jeez, I really need to vacuum under here. It's terrible, Muriel. Fan's definitely working, the rear fan's working, everything's working. So, it is, like, physically on its side like that, so maybe, I don't know, I think I'm going to have to shut it off and, uh, take the heatsink out.

**Dave Jones:** I don't even remember how the damn thing comes out, so I can confirm that it's upright, and it doesn't, it doesn't feel loose. I can give it a wiggle wiggle wiggle yeah in there, but, yeah, it's not, it's not loose, oh yeah, that's, there's a clip on this side here.

**Dave Jones:** Sorry, I'm not going to bother framing this video at all, everyone's just going to bitch in the comments and everyone's going to have a different opinion, and I'm just going to ignore everyone. So, no worries. Tongue at the right angle, come on, there's a clip under there.

**Dave Jones:** Got it, got it, got it, got it, got it, got it. Yeah, that is, yeah, dry as a dead dingo's donger. Um, that is crusty burger. Well, wasn't as good as when it went on anyway, that's for sure. So, yeah, there it is down there.

**Dave Jones:** It doesn't look too terrific, does it, I guess? But, eh, anyway, um, get some freshie. Um, yeah, I'd say I've run out. Oops. So, there it is, I'm no expert on paste, but I'm guessing that, uh, yeah, like aged paste, but I'm guessing that, um, is too high a thermal resistance and maybe it's going to thermal, um, you know, cut out.

**Dave Jones:** And it's just, yeah, it's just dried out. It's gotten progressively worse, because that's kind of the symptoms, I guess, maybe? But, yeah, anyway, so I'm going to clean that off with some isopropyl. And, uh, we get some new stuff. Now, I was going to get the absolute cheapest heap of crap that the local computer store, uh, had, just to trigger everyone in the comments.

**Dave Jones:** And this is what everyone, this is what the majority wanted. Here's the poll for yourself. Okay, unfortunately, just went to the computer shop. This is the Cooler Master High Performance Thermal Compound stuff. Is the best, um, well, is the only one that they had.

**Dave Jones:** So, I didn't have a choice. So, I had to, yeah, Cooler Master High Performance Thermal Compound. So, it is not Arctic Nano Graphene Wank, um, stuff. It is, um, just whatever they had. HTK-002, or whatever. And for those who think that this was applicated, ink-applicated?

**Dave Jones:** Is that a word? I don't know. Anyway, leave it in the comments. Um, the application of this, um, was not proper. Because, oh, you obviously didn't do your little P dot in there, and let it spread, and all that sort of crap. This is how Cooler Master recommended it.

**Dave Jones:** Here's the guide, and they actually even give you an applicator. To actually, and a template, by the looks of it, that you stick on top of your CPU. It looks like it's got a cutout in there. So, it looks like, I guess, you peel that out, you get that out.

**Dave Jones:** And then you apply with your applicator, um, and a big square of paste in there. And that's what they, that's what they recommend. Because I would presume that it's, um, it has to, maybe for this, um, well, I don't know. Are all Cooler Master heatsinks like this?

**Dave Jones:** But, anyway, let me rub this off, and I'll show you. Okay, so I've cleaned that off, and you can see that it uses these four copper busbars here. And, it's, if you try and feel that, this is not feel-o-vision, but trust me. There are, that is not perfectly machined, absolutely perfectly flat.

**Dave Jones:** So, I would presume that if you put a little dot of thermal paste in the middle. You know, everyone's, ugh, put a pea-sized amount of, you know, thermal paste. And then it, and then it's supposed to spread out. Well, no, you could actually end up, if there's slight imperfections, this isn't perfectly machined.

**Dave Jones:** I can imagine, this is my guess, that it's not, it could get trapped in like these things here. And it won't spread out to these outer parts. It might just sort of like ooze out along there, for example, if you put it in the middle.

**Dave Jones:** It might not make it out here. So I guess, that's why they recommend to actually, um, you know, use this square template. And put a square amount of, uh, solder paste, solder paste. Have I been saying solder paste this whole time? Thermal paste, thermal compound, um, on there.

**Dave Jones:** Because it, it's just totally consistent. There's no, like, guessing what size of the thing you have. Because you've got the thickness of this. So you just rub it like that. It's like applying actual solder paste, really. Um, you know, how you have a solder paste, uh, template.

**Dave Jones:** And, you know, stainless steel one. And you, and you apply your solder paste. It applies a perfectly even amount of solder paste. So, yeah, that is my guess. So no bloody complaints in the comments that I'm applying the solder paste wrong. This is the recommended method by Cooler Master.

**Dave Jones:** So suck it. So it turns out those templates are kind of dumb. So I'm just going to go ahead and spread it. I don't know how much is required. It's probably too much, is it? I don't know. I probably should have put a few more dots or whatever on there.

**Dave Jones:** But I'm going for the full coverage method. As they call it, I believe. I don't know. Leave it in the comments down below. Because everyone's an expert. So, yep, I'm absolutely doing it wrong. And that's just fine. Because I love the triggering in the comments.

**Dave Jones:** It's hard to say. Is that enough or not? I'm tempted to think it's probably not enough. Don't want too much, of course. But as I said, there are gaps in that heat sink. So there you go. I reckon that's a nice, that's a nice full coverage.

**Dave Jones:** That'll do. That's good enough for Australia. And yes, I know the fan's pointed the wrong way. Relax, okay? It's the fan, it's the one that I had, and I wasn't going to change it. So whatever. It is good enough for Australia, I'm telling you.

**Dave Jones:** So give it a little wiggle, wiggle, wiggle, yeah. That feels like it went down nicely. Clip that down. So, yep, no worries. All right. Turn it back on. That's re-applicated. Everyone's going, weee, weee, weee, weee, in the comments. Go for it. Go for it.

**Dave Jones:** Knock yourself out. I can't actually remember what the ambient temperature was before, but we're talking CPU is reporting 45, 46. It's going up. I'm just idling. I'm not doing anything, you know. I've got my browser open with my 50 tabs. But apart from that, I'm not doing anything at all.

**Dave Jones:** And I don't know. Anyway, the motherboard, I guess, down here, it weighted 44 degrees. I don't know. It's slightly different. This one gives greater resolution up here coming from the CPU, I'm guessing. So x265 at, let's go, 23 quality here. 50, yeah, it's jumped up 60 degrees.

**Dave Jones:** But that's a lot better than what it was, right? Yeah, we're not quite flogging this 100%. I'll have to find a thing that actually flogs it 100%. It's just, I don't know, I guess the file that I'm using at the moment is not doing that.

**Dave Jones:** But, okay, this is 4K directly from my card, x265. Yeah, it's hovering around that 80% CPU usage mark. So anyway, I think the temperatures are much better. I don't remember. I don't recall because it is the next day now. So I'll look at this in the edit.

**Dave Jones:** But there you go. I'd be surprised if I didn't solve the problem. I think it was just crusty thermal paste. You know, it could be something else. It could be like power supply, you know, dropping out or something. But, you know, you go down to the power supply voltages here

**Dave Jones:** and they're all fine. You know, it's not like they're dipping. 3.36, 5.06, 3.32. I guess that all seems fine. So, yeah, no worries. I don't think it's power supply. I think it was just crusty thermal paste. Anyway, I'm sure everyone will have their expert opinion in the comments down below.

**Dave Jones:** Catch you next time. And wouldn't you believe it? Murphy says it doesn't work. I still get this dropping out. Unbelievable. So I don't think it's the thermal. So I'm going to have to run this test here. And I'm just going to have to look at these parameters.

**Dave Jones:** Like 60 to the 70 CPU package is 74. I don't know, is that normal? 75, 63, I'm not sure. Hopefully you can see this. But anyway, I'm rendering in the background. Geez, I don't know. So, like, the voltages, I don't know. I'd have to wait until this drops out and see if, you know,

**Dave Jones:** maybe there is a, if it is like a power supply dropping out or something like that. Maybe I might be able to see something. Yeah, so this is interesting. Once again, like, I haven't changed anything. Nothing's changed in the BIOS. This machine's been working fine for years.

**Dave Jones:** And the voltages look okay. So unless, like, there's some thermal issue in the power supply and that it's dipping and vroom, the whole motherboard goes down. But the thing is, it only does it for CPU rendering. It doesn't do it if I do GPU.

**Dave Jones:** I can do 100% GPU. I can be flogging that RTX 2060 card like the clappers. And it doesn't do it. This is only when the CPU gets to, like, you know, is like highly taxed for at least, you know, it's like 80% or whatever taxed.

**Dave Jones:** And for at least a few minutes, a significant amount of time. Probably won't do it now. You watch. But anyway, I did go to lunch. I came back and the thing had reset. It's not thermal. So I'm not going to say that was a waste of time.

**Dave Jones:** Thermal paste was a bit crusty. So I don't know. I've renewed my thermal paste. That's good. But otherwise, wah, wah, wah, wah. Come on. Oh, you bastard. Whoa, yes. Blue screen of death. What I did is I just rendered. I just started a render.

**Dave Jones:** It can't be a coincidence. Just started a render of a second video at the same time. I often do that multiple ones. I've done this. I've shown screenshots before of me transcoding like 10 different videos all at once. I did a second one which took the CPU to 100%.

**Dave Jones:** And bingo, it just reset itself. Because I was already waiting here five minutes and it didn't do it. So there you go. There's something. There's something about Mary. I'm going to leave it for this video. I do have a workaround, of course. Because I know using the GPU rendering with Handbrake

**Dave Jones:** is fine. So it's not a problem at all. I've flogged it to death using GPU rendering. The problem with GPU rendering is that it's a bigger file size and the quality isn't quite as good as CPU. So if you've got a choice, CPU rendering, it takes longer.

**Dave Jones:** A little bit longer. Not a huge amount. But yeah, but you do get better file size, smaller file size, and better quality. So I don't know. Leave it in the comments down below. I'm going to have to look back at those numbers. But yeah, you saw there was a blue screen of death there.

**Dave Jones:** I hadn't seen that before. But you couldn't capture the whole thing. I'm not sure what the message was. But there was a blue screen of death. And it just rebooted. There's so many things you can experiment with here. I could be spending bloody weeks just experimenting,

**Dave Jones:** trying to find what this problem is. But I've got to get on with work. And the machine works fine. I can flog it to death. And video rendering is not, like, using DaVinci Resolve is not a problem. Playing back video is not a problem.

**Dave Jones:** But handbrake CPU rendering, yeah, I just took it to 100% and it just failed. In fact, I might try that once more and capture that blue screen of death. So here you go. I've got one video rendering. I'm going to drag in a second one.

**Dave Jones:** And that should take the CPU to 100%. And performance, yeah, yeah, right. It's now hovering around that 100% mark. I don't have a browser open, so it's doing nothing else on this machine. It happened, like, seconds after I started the second video. Maybe I can tax it even more.

**Dave Jones:** I can do a third one. Let's go for broke. Let's tax this machine out. Come on. Yeah, it goes much slower now. It never used to do that. That's only a recent thing. I think since I changed my video card for some reason it's done that.

**Dave Jones:** Not sure what the reason, not sure what that is. But that is, that is flat chat. Almost 100%, you know, that is 100%, 99% utilization on the processor. But she ain't dead yet. Come on, I want to see what that blue screen of death message is.

**Dave Jones:** I'm still erring towards the most likely thing is, like, a processor-y, thermal-y thing. Right? Because when I stress it, it doesn't do anything unless I stress the CPU. Granted, I haven't stressed the CPU. I'll have to use, like, CPU-Z or something to run, like, a little benchmark-y thing

**Dave Jones:** and just stress the CPU. So that's another test that I have to do. I won't do that in this video. But I just want to, oh, yep, no blue screen of death. Wouldn't you know it? Unbelievable. I mean, come on. Seriously? Anyway, that's enough.

**Dave Jones:** Thoughts and comments down below. Catch you next time.
