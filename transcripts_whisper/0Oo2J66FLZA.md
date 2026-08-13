---
video_id: 0Oo2J66FLZA
title: BM786 Firmware Update Test
url: https://www.youtube.com/watch?v=0Oo2J66FLZA
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 41, "3": 65, "4": 85, "5": 105, "6": 126, "7": 142, "8": 162, "9": 178, "10": 195, "11": 211, "12": 231, "13": 251, "14": 275, "15": 291, "16": 312, "17": 328, "18": 356, "19": 398, "20": 418, "21": 438, "22": 459, "23": 475, "24": 495, "25": 511}
---

**Dave Jones:** Hi, just a quick second channel video to show you something on the EEVblog BM786, which is Bryman, of course. You can only get the 786 model from me, the EEVblog. Unlike, I believe, all Bryman meters, please correct me if I'm wrong down below, but they have used

**Dave Jones:** one-time programmable microcontrollers. You can't upgrade the firmware in them, but the BM780 has a BM780 series is different. You can't actually upgrade the firmware. And this is my original one which they sent me, the development version. If you hold down the delta key, when you power it on,

**Dave Jones:** it'll show you the firmware number. There it is, 78601. I'm deliberately tilting the meter like this so you don't see the programmer, which I've got for this thing, because you can't actually reprogram it, and as anyone who's taken the battery cover off this would know, there's the three

**Dave Jones:** AAA battery holders. It's got sort of a uniquely different system for, like, a uniquely different battery holder in the 780 series. I've grown quite fond of it. I thought, I don't know, it's a bit weird at first, but anyway, yeah, it just slots in the back

**Dave Jones:** like that. And if you take it off, you can see that there's a header. Header up there. Little, what is it? Six pin, is it? Little six pin header. And obviously, that is the programming port, as a lot of people, well, it's obvious.

**Dave Jones:** It's a programming port. So this actually does have a flash reprogrammable microcontroller in it. And if you've seen Joe Smith's videos, he's actually been, you know, playing around with these meters, actually reviewing them, including the 789, and he's actually sent him a new microcontroller when

**Dave Jones:** they've upgraded the firmware, and he's had to desolder it and put it back on. Now that's not actually, you don't actually have to do that. Because you can actually reprogram it via this header, which is what I'm going to try now. And I haven't done this before, so this is just an

**Dave Jones:** experiment to see if it works. Now, unfortunately, please, do not ask. I am not going to tell you what the programmer is, or what flash microcontroller is used inside this. I'm under NDA, sorry. As a dealer of this meter, I have access to the

**Dave Jones:** programmer for this thing, for obvious logistical purposes. And yeah, I cannot, I'm under NDA, I cannot tell you, I will not tell you what microcontroller is in this, nor show you the programmer, which is sitting on top of my camera at the moment,

**Dave Jones:** that's why I have to tilt it down like that, otherwise you'll see it in the reflection of the screen. So, what I'm going to do now, so this is version 78601, this is the very first, like, you know, alpha production version. This is a pre-release version, so this is the pre-release

**Dave Jones:** meter that they sent me. Still good, I haven't noticed any difference whatsoever. The release version was version 5, so 78605, and I've currently got 78607 as the latest ones that I ship, and there's very little minor things you'd almost never certainly notice in the firmware update.

**Dave Jones:** So it's not really a big deal, just like the BM235, for example, went through like 5 firmware revisions since I've been selling it, I think, and nobody notices. It's just like, I just shipped the latest version, but that's not a firmware updatable, uses an OTP part, a one-time programmable part.

**Dave Jones:** So, anyway, what I'm going to do is I'm going to plug in the, hang on, excuse me, I've got to plug this in here, I've got to make sure it goes correctly, and because it shares the battery compartment like that, it obviously needs to power it through there.

**Dave Jones:** You can see that it does actually power on, it's got the dash dash dash dash dash in there, right? And if I actually press the button on the programmer, there's an information thing, an information button, so I'm going to press that, and program

**Dave Jones:** and I press that, and it has detected the chip, and it actually rebooted the thing there. Anyway, so, there's two ways to program this, one is to hook it up, the programmer up to the PC and do it that way, but I've actually

**Dave Jones:** programmed the firmware into the programmer itself, so I can work standalone. So all I have to do, apparently, is push the program button on the front. So, yeah, this actually powers the meter, and it powers the meter in off, the meter is currently switched to off, so it powers it in the off position.

**Dave Jones:** And if I actually switch it on, yeah, the meter still seems to work, I haven't tried to operate it, but yeah, it's still there you go, it still seems to work, but you switch it, I presume, you leave it in the off position, and you've got dash dash dash

**Dave Jones:** dash dash, like that, it's being programmed through the programming port. So here we go, I am going to program this sucker, and let's see if we can, let's see what happens. I'm going to push it. Here we go. Busy. It's erasing. It's a good sign.

**Dave Jones:** Could actually take a while. Programming. Sorry, cable's only short, I can't put it further. Program, okay, check some and we're back to there. Beauty. What a bobby dazzler. That seems to have worked. So, I'll put my battery pack back in here. And switch it on by holding down the delta key.

**Dave Jones:** 78607, it worked. Winner winner, chicken dinner. So there you go, it is possible for dealers, only dealers, to upgrade the firmware in their meter. So please don't ask, at this stage I have absolutely no plans for offering a like a programming service if you want to return your meter or something like that.

**Dave Jones:** Just the cost of returning it and everything else is just, it's just, and then reshipping and everything, it's just silly. So, yeah. So this is for firmware updating only for logistical purposes. Obviously if, you know, there's some gross bug found and I've got stocks of hundreds of meters, I can actually upgrade

**Dave Jones:** the firmware in them. So there you go. Does work. Fantastic. Sorry, I can't give you any more details. I'm just under NDA. Sorry. But yeah, it does work. There you go. So that's cool. My meter is now upgraded. And by the way, you do not have to recalibrate after upgrading the firmware.

**Dave Jones:** Unlike Joe, unlike there's, they've advised Joe Smith that when they sent him the new chip, he, it may be slightly out of calibration. And the reason for that is because the microcontroller has a built-in sigma-delta converter in there, the main converter's in there.

**Dave Jones:** So obviously, when you actually calibrate the meter, it's going to have little, you know, the calibration's going to include the analog-to-digital converter and the reference and everything else. So if you change the micro, the physical micro itself, then yes, your readings might be slightly out because

**Dave Jones:** of the, because the calibration is obviously going to take into account any errors in the analog-to-digital converter. So yeah, if you change the chip, obviously, yeah, it might be slightly out. But if you just upgrade the firmware, I am told that no, you don't have

**Dave Jones:** to recalibrate them. So there you go. Winner winner. Chicken dinner. Does work. It's possible. Catch you next time.
