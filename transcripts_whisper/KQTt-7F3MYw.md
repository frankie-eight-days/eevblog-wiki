---
video_id: KQTt-7F3MYw
title: Focusrite Scarlett Solo Issues
url: https://www.youtube.com/watch?v=KQTt-7F3MYw
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 17, "2": 37, "3": 53, "4": 73, "5": 89, "6": 109, "7": 121, "8": 145, "9": 165, "10": 181, "11": 201, "12": 225, "13": 241, "14": 265, "15": 285, "16": 313, "17": 341, "18": 381, "19": 401, "20": 413, "21": 429, "22": 449, "23": 473, "24": 493, "25": 513, "26": 533, "27": 549, "28": 565, "29": 581, "30": 597, "31": 613, "32": 629, "33": 645, "34": 669, "35": 685, "36": 697, "37": 713, "38": 725, "39": 741, "40": 757, "41": 769}
---

**Dave Jones:** Hi, if you've been following me on Twitter and maybe the Amp Hour, you would have probably heard me mention my Rode AI1 USB audio interface that I've been using for quite a few years now. You know, I've had it for a long time.

**Dave Jones:** I never had any issue with it. I thought it was great. But in recent times, as in like the last six months a year maybe, I've had problems. What this thing does is the USB-C interface, it gives me line out which goes to my focal studio monitor

**Dave Jones:** speakers, and I've got a microphone input, 48 volt phantom power which goes to my Rode voiceover microphone that I use if I'm, you know, doing the Amp Hour podcast or I'm doing any voiceover work for my videos or whatnot. And then it's got a volume control, it's got

**Dave Jones:** headphones as well. I use the headphones for when I'm recording the Amp Hour and that's all it does is just microphone input, line output, and USB, and then it converts to like, you know, a Windows compatible USB interface but I've had problems with it where like just in the middle of recording

**Dave Jones:** something, the microphone input will just completely drop or whatever, right? And I don't think it's the actual you know, it's not like the microphone input part of it. I don't think it's battery failing. I think it's some sort of like, you know, USB driver

**Dave Jones:** problem. Resetting the USB, like, fixes it. Now the problem started with using Zemcaster for the Amp Hour which is a web-based, you know, or like a recording collaboration interview tool that we actually use for recording both ourselves and our guests for the Amp Hour, and

**Dave Jones:** like, it used to work just fine, but then all of a sudden this Rode interface unit was not compatible with it, wouldn't detect it properly and stuff like that, even though Windows would detect it and other programs would work just fine, and so, like, it was really annoying.

**Dave Jones:** I had to revert in a lot of cases to using my old Samson CO1 USB microphone just for the Amp Hour, but also in recent times, I've had this actually using XSplit, I've had this actually drop out during recording, like, you know, screen capture videos and stuff like that, and I've

**Dave Jones:** wasted, like, they've been actually ruined. I've had to reshoot entire, like, voiceover screen capture videos, because this thing just failed somewhere, like in the process, and I'm not sure what. And no, it's not just the XSplit recording software, it's actually, it happens with OBS and other

**Dave Jones:** recording software as well, so there's something to do with, like, the USB interface the driver, even though it's supposed to have, like, a generic Windows driver and stuff like that I've updated the firmware in it. Anyway, I've got completely jack of it. So I asked on Twitter what is the best replacement, and a lot of people

**Dave Jones:** recommended the Focusrite. There's, like, a two-input version, but this is, like, the cheaper one, which matches the Rode IR1. This is the Scarlett, the Focusrite Scarlett Solo, and it does exactly the same thing. Microphone input 48 volt phantom power, it's got an instrument mic input

**Dave Jones:** as well, you know, if you're mixing your guitar or your whatnot. And it's got the monitor, headphone out, volume control, and just the 6.5mm quarter-inch TRS jacks out, and USB-C in. So it's practically identical functionality to the Rode mic. But do you think that Murphy would actually let me get away with simply

**Dave Jones:** replacing this with this and not have any issues? No. Of course not. So let's have a look at it. Bloody hell. Right, so let's try the Rode AI1 here. Right, it's connected up to my, here's my editing window, and it's connected up to

**Dave Jones:** my focal CMS40 studio monitor speakers right? And they use a balanced 6.5mm quarter-inch TRS jack to a balanced XLR input over there, and I play video, and it works just fine, as you can hear. And if I stop that, I've actually got my monitor speakers actually turned up to absolute

**Dave Jones:** maximum here, and well, it doesn't matter about the volume I can turn the volume right up there, and I can't hear a thing I put the microphone closer, can't hear a thing. So let's simply replace this with the Focusrite once again, it's completely Windows compatible, didn't have to plug in any drivers

**Dave Jones:** or anything like that, it just works. And it'll auto switch over, and here we go, there we go, I've plugged it in, audio about there, like, there we go. So it works just fine, everything's hunky-dory. Except when I stop it. You probably can't hear that, but let me put the microphone

**Dave Jones:** closer. Listen to this. Hopefully you can hear it. Static. Really annoying static. And it's not just random static like that, it's actually correlated to what my CPU's doing in my computer. Let me show you. Alright, so I'll keep the microphone up to the speaker here, so you can hear the static now, listen.

**Dave Jones:** Okay? Now watch this scrubber bar. You can hear me scrubbing across there like that. And if I render listen to the difference. Listen to this. Can you hear that? And let me cancel it. And it goes back to normal. There you go. It is correlated, the noise is correlated to

**Dave Jones:** what my CPU is doing. And my Rode AI1 doesn't do this at all. It's like, if I turn my studio monitors completely up like I've got now, I can just faintly hear the Rode one doing it. But this one, focus right, at normal volume levels is so loud, it's incredibly annoying.

**Dave Jones:** It may not show up on camera, but I can't sit here with my volume control sitting there doing nothing, and then just like have that amount of noise. But if there's audio going through it, you know, it sort of like swamps it all out.

**Dave Jones:** But no, I can't sit there, it's annoying. And no, it's got nothing to do with the actual setting of the volume control. It makes no difference. The microphone line inputs make no difference. Turning on phantom power makes no difference. It has to be coupled from

**Dave Jones:** the USB input here. Now, I've actually tried the same thing. I actually swapped USB ports here. So I used an entirely different one. It does exactly the same thing. I've tried ferrite clamps on the cables. It does exactly the same thing. I've tried using a common mode choke on the mains

**Dave Jones:** input for my speakers. Makes no difference. And then I discovered Oh! Dave! You dumbass! That's right. You're using unbalanced quarter inch TRS jacks here. Because there's only the two pins. So that's converting. Both the focus right and the Rode have balanced outputs. So you're actually converting

**Dave Jones:** the nice balanced outputs here. So I've got these cables are quarter inch to XLR inputs and the XLR inputs on the studio monitors, they're balanced. So that's gotta be the problem. And yep, of course if I put in a proper balanced lead, as you can see here, I've got the

**Dave Jones:** three pins there. So you've got the ground and then the two balanced outputs like that. It works just fine. I don't get any of the conducted mode noise at all. But I'll just demonstrate what happens when you unbalance it like this. So what I've got on there is just a 3.5mm converter

**Dave Jones:** jack on there. That just extends the ground out. So what I can do is ground either of these balanced outputs. Have a listen. There you go. So that's the tip. Get the same conducted mode noise we did before. And if I ground the other side of the balanced

**Dave Jones:** you get exactly the same thing. And of course, that's what you're doing with that mono one I had before. It was shorting these two out. So it was shorting that balanced output there to ground. And as you can see, if you short either of those to ground

**Dave Jones:** that's what causes the problem. And if you short ground to ground, that's not an issue. But of course that doesn't actually explain why the Focusrite does this and the Rode doesn't. Now, to be fair, I was actually using times 10dB gain. There's a switch on the back of my focal monitors.

**Dave Jones:** I was actually using the highest gain. Plus 10dB gain on there. And when I had my volume at 3 quarters, that's where I've always operated them at. Just because. I don't know. It seemed to work just fine. And well, the Focusrite has this conducted

**Dave Jones:** mode USB noise problem. But the Rode didn't. Under exactly the same configurations. Now, to get to the bottom of that, of course, you'd have to reverse engineer the schematic, have the schematic, have the PCB analyze the PCB layout, everything, to try and figure out why

**Dave Jones:** we're getting conducted mode noise through the USB and then that's making it. If you unbalance one of the outputs, why that comes through and things like that. So, to be fair though, if I actually switch this switch on the back here to 0dB

**Dave Jones:** which is actually a minus 10 as well. If I switch it to 0dB and then I turn the volume down to about halfway something like that, then you can't hear it. So, even if you unbalance it. So, it's not a problem. So, well, you know.

**Dave Jones:** But you should be using proper balanced leads. I just never was because, well, I didn't need to. I should have but I didn't have them at the time when I had my Rode. So, yeah. But now I've got balanced leads for it and that just solves the problem.

**Dave Jones:** So, no worries whatsoever. But it is actually does have an issue on the focus right compared to the Rode in that respect on unbalanced outputs. But! Unbelievable! This thing is actually not suitable for my purposes. I just discovered, I didn't know this, but I just discovered that if you plug the headphones in

**Dave Jones:** to here, it does not mute the monitor outputs. It just, like, whereas the Rode did that. The Rode did that. It muted it. And, of course, that's what you want when you're, like, recording a podcast. You're doing a Zoom call. You're doing whatever.

**Dave Jones:** Right? I'm recording my amp hour radio show. When I plug my headphones in here, the reason I plug my headphones in is not to hear myself. It's got nothing to do with the direct monitor thing which brings the mic through to that. I never use that.

**Dave Jones:** I hate hearing my own voice from the microphone in my own headphones. It's to hear the other person without their voice coming through the speakers and then feeding back to the microphone which causes all sorts of issues. You want this to automatically mute

**Dave Jones:** the output. So the focus right doesn't do it. So in this respect, it is not a direct replacement for the Rode AI1. Now, I can probably understand why you want to do this. You know, this is designed for, like, instrument recording. You plug your guitar into here.

**Dave Jones:** You know, you turn on this button for your air. You know, if you're using an air guitar. Anyway. You're awake. And you plug your mic in and then you want it to come through the speakers but you also want it to, like, come into your headphones so you're, I don't know,

**Dave Jones:** you're listening to the exact mix but it's coming through the speakers at the same time so someone else can hear it. But I have no, absolute no use for that. So for my needs, the focus right is absolutely useless. I have to turn off my speakers manually

**Dave Jones:** every time I want to plug in the headphones just to mute the speakers out. So that's, unless there's some ability to reprogram this in, you know, I don't know, via the USB or something, then I don't know. If you do know about that, leave the comments down below.

**Dave Jones:** Otherwise, this thing is absolutely useless for my needs. Unbelievable. Catch you next time.
