---
video_id: XAbeXAFpyh0
title: Here's How I SCREWED UP a Live Interview
url: https://www.youtube.com/watch?v=XAbeXAFpyh0
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 18, "2": 39, "3": 58, "4": 78, "5": 92, "6": 105, "7": 125, "8": 140, "9": 159, "10": 176, "11": 197, "12": 226, "13": 247, "14": 266, "15": 284, "16": 304, "17": 330, "18": 345, "19": 365, "20": 380, "21": 409, "22": 427, "23": 444, "24": 460, "25": 484, "26": 497, "27": 514, "28": 534, "29": 551, "30": 569, "31": 586, "32": 603, "33": 619, "34": 639, "35": 658, "36": 671, "37": 689, "38": 706, "39": 724, "40": 743, "41": 760, "42": 777, "43": 797, "44": 817, "45": 832, "46": 848, "47": 863, "48": 878, "49": 891, "50": 903, "51": 917, "52": 934, "53": 948, "54": 960, "55": 974, "56": 992, "57": 1005, "58": 1015, "59": 1027, "60": 1039, "61": 1054, "62": 1069, "63": 1084, "64": 1102, "65": 1115, "66": 1130, "67": 1145, "68": 1164, "69": 1182, "70": 1199, "71": 1217, "72": 1238, "73": 1255, "74": 1277, "75": 1299, "76": 1320, "77": 1334, "78": 1349, "79": 1366}
---

**Dave Jones:** Hi, I just wanted to show you a complete screw-up that I did with a live interview I did with Ron Demko from AVX, which you'll see in an upcoming video, a couple of videos actually. One is where I do the film capacitor teardown.

**Dave Jones:** Spoiler alert! Spoiler alert! I won't tell you what the issue is, but those failed caps, I did a teardown, I decided to check my assumptions and get on an expert, which Ron is. He's been at AVX for 40 years. Anyway, fantastic. We talked for an over, like an hour and 20 minutes or something.

**Dave Jones:** Fantastic discussion about failure in film caps and capacitors in general. Anyway, so I decided to use StreamYard for this because I wanted to like overlay, you know, slides and things like over there while we were actually talking. I wanted to sort of, you know, so that he could see what we're talking about,

**Dave Jones:** I could see what we're talking about, rather than just editing stuff later. And I'm going to show you how I completely screwed this up. Hopefully, I'll be able to explain it. It gets complicated, okay? So try and stick with me. But this is the kind of complications YouTubers have when we try and do these sorts of interviews.

**Dave Jones:** It's not just like, oh yeah, set up a Zoom call and just record it, right? No, if you want to like share material on the screen that you're talking about and stuff like that, you have to think about individual recordings, how you're going to actually present it later.

**Dave Jones:** Do you want both of you to be on screen at once and stuff like that. So I decided that I was happy to live produce it using StreamYard, which is what I use for my live shows. But in this case, I didn't stream it live.

**Dave Jones:** I recorded it locally, which it does no problems. And it's actually quite good. It will give you the video version. So once you've finished it, you can download the video version, which is this here, right? So here's my timeline in DaVinci Resolve, which I'm using now, right?

**Dave Jones:** So you've got the video contains mixed audio, right? So it's both of us. So you can't get the separate audio. So if you want to like do editing later and you want to adjust levels and stuff like that, or you want to mute someone, somebody's coughing or talking over somebody else,

**Dave Jones:** you might want to mute that out in a little fine edits and stuff like that. But it also gives you a mixed MP3 download as well. But it also gives you the two. It actually records the two audio channels separately. So I thought like I'm pretty safe, right?

**Dave Jones:** I can always download the two audio files, WAV files, right? WAV files, however you want to pronounce it. Download those two separately and Bob's your uncle, right? I'll be fine. But no, I was able to screw this up, okay? I originally thought it was a StreamYard problem.

**Dave Jones:** Then I realized, oh, no, it's something I did, right? So StreamYard, it's good for guests. Like we use StreamYard and Zencaster as well. Riverside FM is another one which I have used once because, you know, browser incompatibilities with guests. And so anyway, we're using StreamYard so it's easy.

**Dave Jones:** They don't have to install any software. They could just, you just send them the link and it's all browser-based and it connects to their microphone and their camera, right? So no problems whatsoever, right? Except, and here's where the problems start, okay? Except if you're me and you're using a old Canon camcorder with a HDMI output

**Dave Jones:** that feeds into HDMI and AVerMedia, HDMI capture card, well, StreamYard and much other software doesn't support that as a direct input camera. So for me to get my audio here, like if I just use like a USB webcam, sweet, I would have connected in.

**Dave Jones:** I didn't, right? No problems whatsoever. But what I had to do because StreamYard would not accept, first problem, StreamYard would not accept my camera as a source, as a camera source, right? But it would accept the output from XSplit, which is my desktop recording software, right?

**Dave Jones:** So my XSplit, so I simply feed my camera in and I just, yeah, output. I'm using XSplit at the moment to actually desktop record this. And actually I'll turn the audio speakers off here, otherwise it'll blend through. There's another thing that we have to think about, right?

**Dave Jones:** I've screwed up entire recordings because I'm listening through my earbuds here, yet I had my speakers on and I didn't realize that it was feeding back through my microphone here, which is a Rode NTG1 or whatever it is. So yeah, anyway, I screwed up the audio in this.

**Dave Jones:** This is so complicated. Okay, so I was forced to use XSplit, okay, as my video source, as my video source. But StreamYard actually supports my Rode, I use a Focusrite, so the Rode microphone goes into a Focusrite mixer, Focusrite USB audio interface, and it accepts that just fine.

**Dave Jones:** Except I did a quick trial before I started this video, and I thought, ah, they're going to be out of sync, because it's getting the video through XSplit, which takes time to process, and it's getting the audio direct from here. So I did a quick test video before I joined with Ron,

**Dave Jones:** and sure enough, it was all out of sync. And I thought, I'm clever, I can fix this, right? I'm a pro YouTuber, I can fix this. So I selected in StreamYard the audio source coming from XSplit, okay? And XSplit, actually I can probably show you, I can put XSplit,

**Dave Jones:** ah, yeah, I can put XSplit on screen here, okay? Ready for inception, okay? So this is what I'm recording with at the moment. Now XSplit has my audio, you can see this bar graph here, right? This is my audio that I'm speaking with at the moment,

**Dave Jones:** but also has system audio, okay? And system audio is turned on. So it's also recording any system audio. What does the system audio have? It has Ron's voice that I'm listening through here. So it turns out that the recording that StreamYard was making for my channel,

**Dave Jones:** right, because it was recording mine and his separately, okay, mine and his separately, then it was getting, so my channel was getting my voice and his voice, but his channel was fine because he wasn't dicking around like this, right? He's just a guest, he doesn't have to dick around, that's the whole point.

**Dave Jones:** So, and it recorded. So what, here we go. Hopefully I can let you listen to what I recorded. So I'll mute. So here's the mixed audio of the two of us here, okay? So I'll mute Ron's channel and my channel, and I'll only enable, so this is when I downloaded it,

**Dave Jones:** and the look of horror on my face as I realized I've screwed up something in the audio, okay? So here it comes. Hopefully we can, yep, we can play it. Here we go. I see in here. My audio is fine. What do you think this problem is?

**Dave Jones:** Because you don't think that it is. When he starts talking. Moisture and higher resistance. So if we could blow this out. They might go .8 millimeters. Can you hear the echo? Other, just to put it in perspective, right? It's horrible, right? And I thought, right, that is unusable, right?

**Dave Jones:** Maybe if I had one snippet, if I needed just one snippet, I might be able to use that. But that is unfixable audio, right? That is completely corrupted. There's nothing I can do. And I thought, yeah, it was something weird in StreamYard going on.

**Dave Jones:** I at first blamed StreamYard for it. Sorry, StreamYard. It wasn't you. It was me. Because, yeah, and it wasn't his end either. Because we tried a couple of different microphones at his end to try and get the best audio quality and stuff. But, no, it had nothing to do with his end.

**Dave Jones:** It was the fact that within XSplit, which StreamYard was recording the audio from, it was, I forgot to turn off. I forgot to mute. I forgot the default, no, it's here. Where's system audio? They've changed it. They've changed the interface now. They've changed the interface.

**Dave Jones:** Anyway, I forgot to turn off the, yeah, they've changed it. It used to be mute, unmute mic, and mute unmutes default speakers. Yeah, that's system audio. So now system audio is off. So now you shouldn't be able to hear. If I play it, you shouldn't be able to hear anything.

**Dave Jones:** Right? Here we go. I'll play it. There we go. You shouldn't be able to hear anything in the background. Right? So, yeah, I'm pretty sure that's the case. Right? So I had that enabled. So my feed, so if we just listen to my feed, right, so if we mute that

**Dave Jones:** and just listen to what StreamYard recorded just for me, this is it. Ready? Here it is. Right. Okay. So this is fine. See? Would these be made to order? This was supposed to be just my audio, just from my mic, but it's not.

**Dave Jones:** It's both of us mixed. So I do actually have a nice clean mixed version of this. That's 0.1 microfarads. But, of course, see, we're both, you know, if I need to edit, well, normally I would edit this video, right? So if we accidentally, like, talk over each other, one of us coughs

**Dave Jones:** or does, you know, something like that, then, yeah, I can, like, microedit that kind of thing out if I've got the two separate audio streams. Right? So we've got a bit. So I do have a good clean mixed version. But he's quite low.

**Dave Jones:** His levels, you know, they're not mixed. So you can hear it. It's, you know, it's quite low, and then I'll come in and mine's much louder. And it's just, like, you know, if, like, I could use that because I wanted to make potentially an Ampower, like, audio podcast version of this as well

**Dave Jones:** because, you know, it's over an hour long. Great for the podcast. But, yeah, in theory, I could just use that mix because the levels are all out, and you can't fix that, right? You can't really microedit. You can't microedit a mixed audio like that.

**Dave Jones:** You can, but then if you're talking over each other, then it's going to sound really choppy if you try and do that. It's better if you have the two separate audios. Right? So, and, of course, we've got his one. His audio is great, right?

**Dave Jones:** So. 75 kV. No problem. Massive amounts of energy. Of course, you can work with energy. No problems whatsoever. Right? So shoot. So now I've got a choice. Well, there's two choices. I can just either run with just the mixed audio like this, and then I don't have

**Dave Jones:** to do any editing apart from, I don't know, taking out pauses or any unwanted information or something like that. Or I can go to the effort to switch between. I've got to then, like, edit between this version up here, which is okay for my

**Dave Jones:** voice. Right? I'll put it up here. See? My voice is okay. There's not much shoepage on the side, really. Right. So my. And that screws up your circuit. My audio sounds okay. It's a little bit echoey. It's a little bit echoey, but it sounds okay.

**Dave Jones:** So I could potentially, like, mix between the mixed audio and Ron's audio. So if Ron's doing a lengthy talk, you know, I could, like, you know, switch over to him and mute this channel. It's harder. I can't just go mute like that. I've got to.

**Dave Jones:** Because that mutes the whole channel. I've got to do little micro-edits in there. So this is over an hour long. So I'm going to do little micro-edits and switch between audios. But I don't. There's no clean solution here. There's no clean solution, really, because this channel down here is mixed.

**Dave Jones:** Okay. So. Actually, well, no. I would swap between these two. I'd swap between this one, which is Ron's clean audio, nice clean audio, and the mixed version. So I've got to sort of, like, alternate between those. If I'm talking, I'm probably going to have to.

**Dave Jones:** Got it. So the. See. So when. I sound pretty good there, right? So I sound good. Ship my boat. But then I will. But then if he talks. See. If he talks. So the best quality audio of mine is this mixed one down here where if I talk,

**Dave Jones:** it's fine. But if Ron talks over me, we're going to get the echo. Okay. So it's not good. So I can. Like the one up here, the system, the system audio up here is, once again, I sound okay. Well, actually, it's the same problem with both.

**Dave Jones:** Regardless. When they potted, is that what they're trying to do? Is that. If Ron talks at all. As best they can. Yes, that's correct. Then we get. Most likely. Okay. So if the potting's poor. There we go. If we're both talking at the same time, we get the.

**Dave Jones:** Bloody audio. Yeah. The. That echoey audio. And it all has to do with the fact that I thought I was being clever. By taking the audio feed from XLIT. And then I just simply forgot. In XLIT, it was mixing in the system audio.

**Dave Jones:** And I didn't hear this. Once this show is going. Okay. I like. I didn't hear a thing. Like, it all sounded fantastic to me. It's just the back end. In StreamYard. That was doing the recording. And I. You know. And when you've got a guest on like this.

**Dave Jones:** You know. Their time's valuable. You know. You don't want to dick around. And stuff. So it's not like I can do. Oh, let's. Let's do a test. You know. Thing. And then. Oh, just wait five minutes. While I go and. You know. Download it.

**Dave Jones:** You know. And we would have had to stop the. Stream. I would have had to have downloaded it. And then. I would have had to go and. Download it. And then. Check that. You know. Everything's right. And all the audio is fine. And everything else.

**Dave Jones:** And then. I'd have to start the stream again. Send him. Email him a new link. For a new stream. Because you can't restart. The stream in StreamYard. You can't like restart. An existing scheduled thing. Once you've done it. You've done it. You know.

**Dave Jones:** You have to start up a new one. And I. You know. You don't want to hassle. Like guests. Like that. And it's something that. You know. You wouldn't think of. As the video audio. The mix. And the two individual channels. Right. So I thought.

**Dave Jones:** Yeah. I'm pretty safe. And you can say. Yeah. I should have recorded locally. As well. But. But I'm using. The thing I normally do. The recording with. Would be XSplit. And I'm using XSplit. To do the thing. So I. Yeah. But I. Yeah.

**Dave Jones:** I could have started up. Maybe another instance of OBS. Or something. Which would have. Captured the audio. But yeah. Like I didn't think. It's a problem. It just didn't even. You know. Didn't. I didn't even think. That this was actually possible. But yeah.

**Dave Jones:** It's possible to screw this up. And I did it. And this is the problem. That YouTubers have. When they try and. You know. This sort of stuff. Is not easy to do. You're used to. You know. If you're not creating content. Like this.

**Dave Jones:** You hop on your Zoom call. Bob's your uncle. Right. But when you're trying to actually record. Things. It can get. Really complicated. Because you're also thinking about. The process of editing. Later. You know. You might want. Different audio streams. And you might want.

**Dave Jones:** Different video streams. That's even harder. Again. You know. If I want to. Like. Put someone. Have a look at the. Show I did with. Mehdi. Where I put. It's an amp hour one. Where I. I had to. Individually. Cut out. Our. Our separate video.

**Dave Jones:** Feeds. Because I wanted to make him bigger. Because he was the guest. So. You know. He was like bigger. And I was like. It was too big. So I put it in. And redone it. And stuff like that. I did some. Fancy editing.

**Dave Jones:** And stuff like that and you have to think about how. You're going to capture. All of this stuff. As a content. Creator when you're doing. Live shows. Like this and especially. It's even more. Difficult if you want to like. Include like overlay overlay.

**Dave Jones:** Material and stuff. Like you know slides and. Other stuff which you're. Actually discussing because the. Guest has to see it as. Well you can't go. Oh. Yeah. Let's talk about this. And then you know. Not show the guest. And then have them talk about it.

**Dave Jones:** And then you edit in the picture later that. That doesn't work for the guest right. The guest has got nothing to look at. I like a look at it on my screen. Or maybe if we could coordinate stuff beforehand. Look at slide X.

**Dave Jones:** And then he could call it up. But then he would need multiple monitors right. Which you can't assume that a guest is going to have. Like they're not. You know it's. It's just. It's nuts. So that's how I screwed up. The audio. In this.

**Dave Jones:** Probably I wouldn't have screwed up. Because normally. It went. When I'm doing StreamYard. I would just record. The audio. Well I usually do it on the other machine. Which has a webcam. Which doesn't have this issue. So and I feed the audio through a separate device on the.

**Dave Jones:** When I'm doing my weekly live show over there. Using StreamYard. But yeah. Here we go. I'm on my desktop. PC at the moment. You know. This is my editing. PC. And. Which is where I do all my screen recordings and stuff. And where I do interviews like this.

**Dave Jones:** With guys like Rod. And yeah. I. I just. Yep. Yep. It's not something that I thought of. So. I. Yeah. There's many convoluted ways. To screw up. Recordings. And it happens with. Chris Gamble. And myself. Doing the amp hour all the time. He's done it with guests.

**Dave Jones:** We've done it. When we've had guests on. And stuff like that. And. Especially if we try and do. Just audio is hard enough. But when you're trying to include. The video. Functionality. As well. And trying to capture it all. Works. And make sure there's no.

**Dave Jones:** Audio source screw ups. In the recording. To make sure you've got backups. And stuff like that. I was just complaining. Like. A couple of weeks back. A month ago. One of my amp hour recordings. Was almost. Almost. Destroyed. When. Zencastr. That we used.

**Dave Jones:** Actually screwed up. Zencastr. Did something. That screwed up. The guests. Side audio. And. Yeah. And it was just. It was. Like I had people on Twitter. Trying to fix it for me. But it was just like. This stuttering thing. So it would be like.

**Dave Jones:** Everything said. Twice. Twice. Twice. Twice. Twice. And it was like. It was. Like. Completely chopped up. It screwed up. Completely. The original wave recording. That was supposed to happen. On the. Guests. Local machine. And that's what we rely on. We've done hundreds of episodes.

**Dave Jones:** Of the amp hour. With Zencastr. No problems. But. This one case. Where I had a guest on. It completely screwed it up. And it was. Backup. Readily available. And it couldn't be recovered. But luckily. Zencastr. Were. The Zencastr. Servers. Do actually record. They don't tell you this.

**Dave Jones:** But they do actually record. The. The. Voip. The Voip. The Voip. Version. Which is what you actually. Listen to. You're listening to a Voip. Version. It's different to the recorded. Version. Which records locally. On each end. Using the browser. And it was probably the browser.

**Dave Jones:** That screwed it up. Actually. It was the browser. That. You know. That uses like. The operating system. Audio. Capabilities. To record. Audio. From the browser. Directly. And saves it locally. And then it straight. Then uploads it. At the end. So you get higher quality.

**Dave Jones:** Local. Audio. Right. And that's why we use. Zencastr. For our. Podcast. Because we want the highest quality audio. Possible. And. It. Yeah. So I got in contact with. Zencastr. And. Yeah. They were able to. Contact me. They were able to. Get. The Voip.

**Dave Jones:** Which. They don't keep forever. Like they were lucky. I contact them within. You know. 48 hours. Or something. Otherwise. It would have been gone. Yeah. They were able to get. The Voip. Copy. Of that. And then we were able to do. The. Yeah.

**Dave Jones:** Well. That podcast. Was saved. Yeah. So. I've got. Yeah. So when I do guest. Things like this. It depends on what I'm trying to do. In this case. I wanted to do like. Overlays. And. Stuff. So. Yeah. I. Like. Like. Yeah. We're talking about all these slides.

**Dave Jones:** And it's great. Right. It's absolutely fantastic. And Ron was. So. Knowledgeable. Right. It's. It's. Gonna. Be. A bit. Weird. And you can't figure out why. Well. This is why. Because I. Screwed it up. And. Yeah. There was just like. I could have used.

**Dave Jones:** Zencastr. Because it records. Videos as well. But I don't think I can. Actually overlay. Live. You know. Slides. Like this. So then. You know. Myself and Ron. Couldn't like. Talk about. The. Slides. And things. So. There's the other one. I talked about. As well.

**Dave Jones:** That's why I've used once. But you know. I don't want to use. Something I've used once. In. At a pinch. For. You know. So I use Streamyard. Which is what I knew. And. I thought Streamyard screwed up. But it wasn't. It was me.

**Dave Jones:** Because I selected an audio source. That had system audio included. So there you go. Wow. There you go. I've waffled on enough. That's my. Screw up. I just wanted to share that. And. So I just. And. I want to thank. You guys. For.

**Dave Jones:** Alfred. Is saying. To. You know. He's telling all this. Bruce Wayne. All this. Technical stuff. And Bruce. Wayne says. Why do I need to know? Any of that? And he says. You don't. I just wanted to tell. You how hard it is. And that's basically.

**Dave Jones:** What I'm doing. Here.
