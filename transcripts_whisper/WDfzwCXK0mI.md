---
video_id: WDfzwCXK0mI
title: WEIRD Blackmagic ATEM Mini Fault
url: https://www.youtube.com/watch?v=WDfzwCXK0mI
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 18, "2": 33, "3": 58, "4": 80, "5": 100, "6": 117, "7": 134, "8": 151, "9": 171, "10": 189, "11": 206, "12": 227, "13": 249, "14": 271, "15": 296, "16": 320, "17": 338, "18": 361, "19": 381, "20": 396, "21": 408, "22": 421, "23": 441, "24": 461, "25": 478, "26": 493, "27": 512, "28": 532, "29": 550, "30": 566, "31": 580, "32": 593, "33": 606, "34": 626, "35": 644, "36": 661, "37": 677, "38": 690, "39": 712, "40": 732, "41": 748, "42": 766, "43": 780, "44": 792, "45": 808, "46": 829, "47": 847, "48": 860, "49": 874, "50": 886, "51": 904, "52": 920, "53": 943, "54": 963, "55": 979, "56": 993, "57": 1011, "58": 1025, "59": 1040, "60": 1055, "61": 1074, "62": 1093, "63": 1111, "64": 1127, "65": 1149}
---

**Dave Jones:** Hi! Say hi to my live audience as well, um, because this is the Saturday morning live show, um, with Dave. And I've got a little hand puppet, he comes up and... No, um, Saturday morning live show, um, and I just discovered something really weird.

**Dave Jones:** I was just showing the live audience, um, this, uh, is this, um, scanner strip from that, uh, teardown I did, and the part salvaging video, right? And, watch this, right? It's got a nice little exposed die on here, right? It's really, it's really schmick.

**Dave Jones:** I'll put it back to auto-exposure. There you go. Right? Check it out, right? Nice colors, but watch this. Three, two, one, epilepsy warning. Look! Look! My, my, my camera's just going, my, this is my Tigano microscope. It's going berserk. Yep. There you are, look.

**Dave Jones:** Wow. There's, there's something. I've never seen this happen before. This is really weird. This is really, and look, I can make it go away. Three, two, one, stop. Three, two, one, go. There's, like, something to do with the exposure is causing that camera to go nuts.

**Dave Jones:** And if I go over here, will it happen over here? Three, two, one, not quite. But it happens when I'm viewing this die. Maybe not viewed in, maybe not zoomed, no, no, it doesn't seem to do it when I'm, unless I'm zoomed in.

**Dave Jones:** So maybe it's, yeah, yeah, look, right? It's happening, okay? If I zoom out and I'm not tilting the board, it goes away. So there's something wrong with my Tigano microscope when I zoom right in. Wow. I'm going to have to send this to them and go,

**Dave Jones:** hey, what's, what the heck's going on here? There's something weird. Once it overexposes like that, boom, it just, bleh. And yet, if I only do it, oh, look at that, that's beautiful. Light shining like that, right? And so I reckon I can make this go away

**Dave Jones:** if I turn the, if I turn the internal light off, right? So here it is, it's happening now. And if I turn off the internal light, it's not going to do it anymore. It's pretty, the footage is fairly grainy now because I don't have my overhead lights on.

**Dave Jones:** But, wow, okay? Now I'll turn the internal light on. It's a function of the internal light, like, ah! It's, well, it's a weird strobe-y thing, like, it's a weird exposure thing where it just causes, like, I can understand if it's an auto-exposure thing.

**Dave Jones:** I can set manual exposure, right? I've now got manual iris, so I can turn it down to F1, right, like that. And gain settings, right? I can set my gain like that. So if I set the gain right down, it's probably not going to happen.

**Dave Jones:** Yeah, no, no, it still happens, even with the manual gain, right? So even with manual, like, manual exposure mode and stuff, it still happens. Weird, huh? Something is causing that to overload the exposure system and it's just blanking, boom, boom. Like, I can understand, like,

**Dave Jones:** if it's just overexposes, that's fine, but it's, like, it's literally blanking the screen and causing these flashes, these blank flashes. Wow! Haha, weird, huh? There you go. So I'm going to have to send that to Mr. Togano and find out what the problem is.

**Dave Jones:** All right, looks like I have to apologize to Mr. Togano. I don't think it's the Togano at fault. I think it's the ATEM switcher that I'm going into because by popular demand on my live show, people wanted to see, most people thought it was the Togano microscope at fault.

**Dave Jones:** But I cannot repeat this. I've got it plugged in directly into an external monitor now and I cannot get it to happen. So the HDMI, oh, no, hang on, I wasn't zoomed in. No, still not happening. It is, no, it's good. It's good, I'm going to deem that to be good.

**Dave Jones:** The Togano microscope is not at fault. So, Mr. ATEM, Grant Petty, I'll personally send it to Grant Petty and he's the CEO of Blackmagic. He was supposed to be on the Amp Hour, by the way. I'm going to follow up. And, yeah, it is not the HDMI output.

**Dave Jones:** There you go. It is the Blackmagic ATEM switcher, which I'm using to switch my live show. There's maximum exposure right there. Now, why the Blackmagic cares about what the HDMI signal is, I don't know. It's a switcher. You should just pass the information straight through.

**Dave Jones:** So if anyone's seen this with the Blackmagic ATEM, please let us know because it doesn't seem to be the Togano microscope at fault. I thought, like, yeah, the camera's overexposing and it's just, I don't know, chucking a wobbly or something, right? But it's not.

**Dave Jones:** Okay. So I'm going to go straight back. Haven't touched anything else. Yep. There we go. There we go. It's back. It's back. Wow. Wow. Who would have lost that bet? Everyone. Everyone. We have evidence in the chat. I am amazed. That is the ATEM.

**Dave Jones:** Try a different cable. It shouldn't matter. It's macro vision, copy protection. Could the picture-in-picture trigger the fault? No, because I'm also seeing it on, well, it shouldn't matter, right? If it does, then it's still a fault. But no, I'm also seeing it, because I've got a multi-view window here.

**Dave Jones:** This one here shows the picture-in-picture, okay? So this is the program output. You can see my VU meter here, right? So this is what's actually going live and or being recorded. I've also got this one, which is a live, which should be a live feed from the HDMI.

**Dave Jones:** And it does it on that one, too. It doesn't just do it on the mixed program output. If it did that, I would have noticed straight away. I would have noticed that, ooh, it's the ATEM. Obviously, some sort of processing artifact is doing that

**Dave Jones:** when it's doing the picture-in-picture thing and actually switching and processing. But that's taken from the live, well, it's not taken directly from the live input. It's got to sample it and, you know, process it and display it. But it's the same on both.

**Dave Jones:** It's definitely the transition. Once it's overexposed there, it's fine. But it's the transition to overexpose that gets it. That is, what are the odds of capturing that? I reckon I'm probably the first one to find that. I reckon that is so obscure that the guys at Blackmagic are going,

**Dave Jones:** no way, no way, no way. I bet you it's not our fault. It's got to be their fault. And shooting my live show here, you can see this is the output monitor from my ATEM switcher, which is down here. So I've got my HDMI input going here

**Dave Jones:** from my Togano microscope. So it goes into the second input here. I've got it selected. And that's the output there. So that's the live output, live in quote marks. That's a live output, the unprocessed output, or the unprocessed input, HDMI input. And then I've got my program output over here,

**Dave Jones:** which has a picture-in-picture. Sorry, it's got my VU meter. So all of this is processed and switched. It's got to do the picture-in-picture switching, heavy processing. It's got to overlay the VU meters and everything. Yet, it's not that. You'll notice, I can make this.

**Dave Jones:** It does it on both. It does it on both windows. So it's not just the internal picture-in-picture processing or something like that causing that. And it doesn't show up on the external monitor. There is something wrong with the ATEM switcher. It's just, for some reason, that obscure little transition

**Dave Jones:** between overexposed and overexposed is causing the input to blank out. And then that transfers to the output stream. Wow. Who would have thought? I'm stunned. I'm absolutely stunned. So if you've seen this on a Blackmagic ATEM, there's so many users out there. I can't believe, maybe I'm the only one

**Dave Jones:** who's found this obscure side, this obscure little issue with the ATEM. Who would have thought that it's doing any sort of processing like that? That it cares what you input. It should just switch it straight through. That's its job. So, yeah, weird. Let us know in the comments down below

**Dave Jones:** if you've seen something like this happen with the Blackmagic ATEM. Because it's definitely that. It's a poor old Togano microscope. Apologies to Togano. I thought everyone in the chat thought it was the Togano microscope at fault. That was the obvious reason. You wouldn't suspect the switcher.

**Dave Jones:** There was only, like, one person, I think, who suspected the switcher. But there you go. I'd at least have to put more investigation to figure out, you know, to actually get under it. Like, I could maybe use a different example to replicate it.

**Dave Jones:** Somebody mentioned a CD or something to put under there because that actually reflects light and can give large exposure changes and stuff. Does anyone think the HDMI cable is going to be the problem? Yeah, I agree. It's got to be the HDMI capture.

**Dave Jones:** I totally agree, Mike. I can't see it being the cable. Yes, people saying it could be this. Some people saying it could be the cable. Others saying, nah, definitely not. I'm on the side of definitely not. But then again, I was on the side of definitely not.

**Dave Jones:** Definitely not ATEM. It was the Togano. It's the HDMI capture. Blackmagic will know. I reckon, I reckon Blackmagic don't know about this. I reckon I'm the first. I betcha. Because, like, this is the, like, it's not some obscure feature. This is a fundamental feature of a video switcher

**Dave Jones:** is to switch the video, is to take the video from the input, switch it to the output without it getting all the heebie-jeebies, right? So, like, if anyone else saw this, I'm sure they would have reported it. It'd be number one priority. It'd be number one.

**Dave Jones:** Seriously, if I was on the team for the ATEM, anything to do with video capture, video processing, would be number one priority. That's its job. You agree, Rob. It's a unique application which is unlikely to be tested. Yeah, I reckon, oh, you search Google already, BatTube?

**Dave Jones:** Okay, BatTube, search Google. Can't find a relatable issue. Someone, Das Breaker, has bet on limited RGB color 0 to 235. Try a different ATEM input. Could be a hardware fault. Oh, well, that's easy enough to do. But I doubt it. I'd be stunned.

**Dave Jones:** Not still doing it. But then again, is it a dual chip? I can't remember the teardown of this. Is there, like, a dual, is there one chip handling, like, two inputs or something? I can't remember if it was. I just switched it to the chip next.

**Dave Jones:** So you'd have to test all stuff like that. You would have to go through and systematically, like, you know, trial this. It's probably not supporting all the color space options. Okay. Interesting. High-speed HDMI cable. It's another cheapie. Sorry. Like, but I think everyone would be happy with just a physically

**Dave Jones:** a separate. Ta-da. It ain't the cable. Sorry. Doing exactly the same fault under the exact same circumstances. It ain't the cable. Might be an issue with the video alignment because the image jumps around like crazy. It is the fast color exposer. Exposer? Exposer.

**Dave Jones:** Processing glitch. Somehow the processing is delayed so he's not buffered fast enough to process the image in time properly. Yeah, but why? But a switcher. I can understand the camera. That's why I and everyone else thought it was the camera. Because the camera does exposure.

**Dave Jones:** Right? That's one of its jobs. A HDMI switcher should not do any exposure processing at all. It should simply pass the HDMI signal straight through. Well, you know, it captures it and then sends it out, I guess. Oh, but no, it uses the HDMI receiver chip.

**Dave Jones:** See, here's the, like, if I was to do a proper main channel video, here's the, you know, the rabbit hole I would go down. I'd go back to my teardown of this, find out which chip. It's in analog devices, I think, HDMI processor receiver chip.

**Dave Jones:** You'd go in there and you'd check the HDMI receiver chip. And you'd do all that sort of stuff. Right? So if I was to do, if I was to put like a, you know, half a day or a day's work into it. Like, do a, do a proper video.

**Dave Jones:** I would go down that rabbit hole. Having rapidly vary in the image or video stream should be part of EMC testing the ATEM? Yeah, you'd think so. Yeah, I could, you know, you could generate, if you wanted to test this properly, yeah. You would, you'd have to do an extensive test rig that generated,

**Dave Jones:** you know, some sort of video pattern generator that could. Do ATEM have any settings for contrast enhancement? Not that I'm aware of. There might be something there, Mike. Somebody says, bingo. Could be one of those weird things to do with HDMI. Black level being 0 to 255 full instead of 16 to 235 limited.

**Dave Jones:** But usually that just makes the black, blacks crushed, bloomed if it's wrong. Interesting. You're speaking from experience there, I'm sure. Um, yeah. That's interesting. So here's, here's, here's the Tigano channel, for example. Lift. We can do gamma correction. We can do gain correction.

**Dave Jones:** So it does all this. It can, it can do all this magic. It does it all in the FPGA, I think. But yeah, it's got gain, gamma, lift. It's got color balancing. It's, we can do all that. We can do all that processing.

**Dave Jones:** There's a hell of a lot of processing involved in there. But why it would blank out? Like, why it would blank out? That's really weird. I just got here. I've got no idea, but it's the most expensive part of the thing is usually the issue.

**Dave Jones:** Okay, it's the FPGA chip. We were just talking about that. It's the FPGA chip. It's the most expensive thing in this. So it's got to be that. It's got to be that at fault. It can't be the HDMI receiver chip. The analog device is HDMI receiver.

**Dave Jones:** HDCP protected signal. They do actually have HD, different HDMI receivers in here for different channels. So, you know, this is all part of the process of, like, nailing this down. Because you can only, I think, I don't, does it only support 4K on four of them or something?

**Dave Jones:** Or it only supports something on four of them instead of eight inputs? Or, you know, it physically uses, if you have a look at my Teardown video, it physically uses a different HDMI receiver chip. Yeah, see, there's another thing you could try. Like, just try a different microscope.

**Dave Jones:** You know, it could still be the Togano, right? It still could be the Togano outputting some non-standard-y kind of thing. Like, I don't know my HDMI standard, right? So it could be, like, it could be, like, non-compliant in some way. Um, I do know, see that?

**Dave Jones:** This is the original cable supplied with the Togano. This is the original HDMI cable. And it actually has Togano on it. It actually has Togano labeled on it. Because I think they did have an issue. I think Togano did have an issue with the HDMI.

**Dave Jones:** That they had to say, no, you have to use our cable. So, eh, you know, eh. But then again, right, why the monitor handled it and the ATEM didn't, right? The ATEM did not handle it. So, you know, it could be both at fault.

**Dave Jones:** I would say, yeah, the ATEM is not, at the very least, the ATEM is not robust enough like the, like the, we saw it on the screen, right? So that monitor, whatever HDMI receiver that used it, and whatever processing it's doing, it worked fine.

**Dave Jones:** Lewis Rossman had an issue with HDMI capture card microscope camera. I think it may have been Blackmagic and they told him that medical cameras were not supported. Yeah, I reckon, I reckon the ATEM is just not as robust. It's not as robust as that LCD monitor we used, which had no problems.

**Dave Jones:** You know, okay, the Togano might be slightly non-compliant or something, but the Blackmagic should handle it. It shouldn't blank out like that. I think that's a pretty bad value mode. The problem seems to be in transition between colors. That makes sense from a video compression point of view.

**Dave Jones:** Too many pixels are changing too rapidly. I reckon I'm going to send, this video is going to send the ATEM team into a loop. I reckon they're going to, I reckon they're going to be chasing their tail for weeks. ATEM tries to convert all inputs to match cam 1 in,

**Dave Jones:** so it is probably a conversion codec. Can I get something to pre-process the video so ATEM will receive a different signal? See, once again, that is another interesting test that would have been part of if I did a full video investigation on this.

**Dave Jones:** Ah, see, that's interesting. I wonder if you can record the Togano output video. I can. And play it back through the ATEM. I can. Blackmagic gear historically has various limitations, but it also costs like one-fifth of the name brand stuff. Yeah, yeah. You get what you pay for, I guess.

**Dave Jones:** No, no, the recording's not the actual HDMI signal, but we're talking about the, we're talking about like the transition between, like the sudden transition between like colours and things. But yeah, no, I think it's more, I would bet money, I would bet serious money that if we recorded the output and played it back through,

**Dave Jones:** you wouldn't get the problem. I think the problem is the HDMI source, and potentially not 100% compatible HDMI source, don't know, or maybe it's just on the margin of something somewhere, and the Blackmagic can't handle it. I'd be surprised if they couldn't fix it in firmware.

**Dave Jones:** Yeah, totally. But the problem is nailing and reproducing the problem. It may only be that it can be reproduced here, with this board, on this microscope, with this microscope source, into like, I wouldn't surprise me if they came back to me and said,

**Dave Jones:** hey, we can't reproduce this. You know, they send somebody over here to try and write. That'd make for a great video. Imagine if Blackmagic sent Grant Petty himself, the CEO, Grant Petty comes to the EEVLOG lab and tries to troubleshoot the, troubleshoots the FPGA in the bloody ATEM switcher.

**Dave Jones:** That'd be great.
