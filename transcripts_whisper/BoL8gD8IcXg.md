---
video_id: BoL8gD8IcXg
title: Mantis Elite Cam & LattePanda Project FAIL
url: https://www.youtube.com/watch?v=BoL8gD8IcXg
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 42, "2": 55, "3": 68, "4": 79, "5": 85, "6": 91, "7": 97, "8": 103, "9": 111, "10": 117, "11": 124, "12": 130, "13": 136, "14": 137, "15": 167, "16": 167, "17": 197, "18": 197, "19": 232, "20": 258, "21": 276, "22": 287, "23": 302, "24": 327, "25": 341, "26": 354, "27": 360, "28": 390, "29": 410, "30": 420, "31": 449}
---

**Dave Jones:** Hi, this is just going to be a single-take, second-channel video. What you're seeing here is through one of the ocular ports of my Mantis Elite cam microscope. I'll link in a video I've done down below for this thing. And I thought that, like I was doing this the other day, I was shooting a teardown video, and I thought that it'd be great if I could just have this cam hooked up to a little Raspberry Pi or other little, you know, computing thing hooked up to a Dropbox so that I can just hook up a button, push a single button, and it'll take a screen capture through my Mantis Elite microscope and save the image to my Dropbox.

**Dave Jones:** So when I go back to my office and edit the video, I don't edit the videos here in the lab anymore. I take a screenshot. I take the SD cards and other stuff back. I thought I'd, you know, be able to have that image file already there, ready to go, so I can just capture stuff through the Mantis Elite.

**Dave Jones:** Because the Mantis Elite has these awesome optics. So I'll zoom in. So I've got my camcorder, like, you know, four or five inches away from the hood of this thing. And you can see down on this board here, and it's just, it is absolutely brilliant.

**Dave Jones:** I can bring in, like, more zoom. I've got a x4 lens on the Mantis Elite now. And it's just, like, superb image, optical image. It's just, like, superb image, optical image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image.

**Dave Jones:** And it's just, like, superb image, optical image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image.

**Dave Jones:** And it's just, like, superb image, optical image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image. And it's just, like, superb image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image.

**Dave Jones:** And it's just, like, superb image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image.

**Dave Jones:** And it's just, like, superb image, optical image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image.

**Dave Jones:** And it's just, like, superb image, optical image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image.

**Dave Jones:** And it's just, like, superb image, optical image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image.

**Dave Jones:** And it's just, like, superb image, optical image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image.

**Dave Jones:** And it's just, like, superb image, optical image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image.

**Dave Jones:** And it's just, like, superb image, optical image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image. And it's just, like, superb image, optical image.

**Dave Jones:** And it's just, like, superb image, optical image. built inside the Mantis Elite Cam, and I actually forgot how crap this camera is. They've got, they built one of the world's best stereo optical microscopes here with, you know, some of the world's best optics in it, and then just put a shitty HD webcam in it.

**Dave Jones:** And, like, the quality is just, like, everything's overexposed, and it's cropped. It's not near, like, there's good, lot of it cropped. You'll have to look at the, uh, LinkedIn video to see how much this is cropped. But it's, all the highlights are blown out.

**Dave Jones:** This has got gain boost on. There's some, there's noise on the image. It's pretty terrible. Anyway, um, what David did, David 2, um, he, uh, what we did is had this, uh, Latte Panda here that you've seen in a, uh, previous video. It's a Windows 10, uh, computer.

**Dave Jones:** It was one of the first Windows 10 single board, uh, computers available. And, uh, it's just got an Intel Atom, uh, processor in it. And I thought, you know, we'd use that, because it's easy to use. It's easy to hook up to Dropbox and everything else.

**Dave Jones:** And, uh, so, uh, David wrote a nice little, um, app here. And I'll show you the source code in a minute. But, uh, basically, yeah, we've, we've got this button here. And hopefully, um, so he wrote this application, which, uh, talks to, because there's actually a Raspberry Pi on, uh, sorry, there's an Arduino on here.

**Dave Jones:** It's Arduino compatible inside. So he's talking through the serial port of the, the Arduino serial port, um, to interface with that. up, and we can store a-- here we go, if we press it, hopefully, there we go. It's stored a PNG into our Dropbox.

**Dave Jones:** Fantastic. And of course the-- well, I don't know what image program I've got installed here. Whatever. Anyway, so it all works, hunky-dory, but the problem is, it's basically a useless tool because the-- I don't know what it is, but the problem is, it's basically a useless tool because the HD camera inside this thing is

**Dave Jones:** just garbage. Utter garbage. Not the same field of view. There's not enough light from the regular thing to get any decent thing, and the light, it's a different angle, so you can't see the chip numbers the same, and it's just-- crap. Anyway, so that is a real

**Dave Jones:** shame. So it's a useless tool. I might as well just put my camcorder up to here, and then I'll be done. Subtitles by the Amara.org community and just, you know, spend 30 seconds just getting it all lined up, and take a screen capture that way.

**Dave Jones:** So, there goes my idea of just having like a nice little, you know, embedded PC always there, just maybe doing some boink processing in the background. And when I want to come over, I just had a button and a LED, it does a buzzer sound when it

**Dave Jones:** is captured the PNG, and uploaded to Dropbox. Anyway, that's just-- like, so, yeah. We only realized how crap we were doing. Oh, crap, it wasn't until he started doing it, unfortunately. So he actually wrote this on Visual Studio. So he actually had Visual Studio running in the-- actually installed Visual Studio on this Latte Panda, which was a pain in the arse, wasn't it, David?

**Dave Jones:** Yeah. Yeah. I think it's slow. I think he's traumatized by the Intel Atom processor. Anyway, there's the code for those playing along at home. It interfaces to the MicroEye software, which is a software that comes with the Mantis Elite camera. And it's actually got drivers.

**Dave Jones:** So it's through the API, is it, David? Yeah, and to be clear, this is actually one of the first steps that they recommend you follow. Install Visual Studio on the, you know, the Latte Panda. That's what they tell you to do. What? Really?

**Dave Jones:** They tell you to install Visual Studio, and it's traumatic. So I was just like, "Okay, I'll do that." Uh, alright. Anyway, so we've got, like, gain-- like, auto-- auto gain-- gain boost and white balance and every-- like, everything auto gain set up. So, like, and they're just-- the color's not nearly the same as what you get through the optical port, and it's a shame.

**Dave Jones:** Anyway, so there's his code, um, for those playing along at home. It didn't take him long at all, 'cause he's a software wizard. Um, and, yeah, that was just-- oh-- oh, oh, my Mantis Elite cam just fell. It just fell. Oh, lucky I've got my protector on there.

**Dave Jones:** Oh, just the weight of that. Oh, anyway, the benches are properly set up at the moment. Um, so I've got the desoldering gun anywhere. Um, there-- yeah, there's, like, a tension bar in the back that allows you to, you know, um, set the exact, um, you know, offset the weight of the head and stuff like that.

**Dave Jones:** So, yeah, unfortunately, that was a failed project. Um, but, yeah, it worked. But, nah, it's just much-- better. Much easier to simply dick around, get the camera close enough like that, and go in. So, if you see, uh, you know, really bright and colorful, uh, screen captures like that in future videos, you'll know where it comes from.

**Dave Jones:** It's just me putting the camcorder up to one of the optical eyepieces on that. Um, of course, I can use my Tagano microscope as well, which is, uh, fantastic. Um, and-- but I usually only do that for, like, video, uh, type stuff. So-- and-- and this is better for viewing, uh, chip numbers and stuff like that.

**Dave Jones:** than the, uh, Tagano. So, anyway, thought I'd show you that failed project. Eh. Catch you next time.
