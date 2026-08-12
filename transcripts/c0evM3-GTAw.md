---
video_id: c0evM3-GTAw
title: Weird Uni-T UDP6731 PSU Fault FIXED. I got a DUD?
url: https://www.youtube.com/watch?v=c0evM3-GTAw
source: youtube-asr
timestamps: {"0": 0, "1": 12, "2": 32, "3": 44, "4": 53, "5": 63, "6": 77, "7": 88, "8": 100, "9": 114, "10": 124, "11": 136, "12": 145, "13": 160, "14": 172, "15": 195, "16": 220, "17": 233, "18": 246, "19": 258, "20": 266, "21": 285, "22": 298, "23": 310, "24": 332, "25": 346, "26": 358, "27": 367, "28": 380, "29": 390, "30": 401, "31": 412, "32": 432, "33": 439, "34": 454, "35": 462, "36": 469, "37": 482, "38": 493, "39": 503, "40": 517, "41": 531}
---

**Dave Jones:** Hi, just a quick follow-up video on this UT UDP 6731 power supply. The review I did a full review of that. It was quite popular. But there was one issue with it and that was the Lister mode here.

**Dave Jones:** So we've got the regular voltage mode and then we've got the delay mode and then we've got the Lister mode which allows you to program in different voltage steps and like a time delay between each one so that you can step your waveform up and I just did a simple thing and in that video I just programmed in a simple 1 V step.

**Dave Jones:** So 1 V, 2 V, 3 V, 4 V, 5 V. So five counts total and it cycles through one time. So it just does all those steps through that five those five steps one time.

**Dave Jones:** And there's one second delay between each one. Current limit doesn't matter. Just set it to like a 2 amps and we had a problem with it. So let's see if we can recreate that.

**Dave Jones:** Now I've got the exact same conditions that we had in the video. So let me run that. Hold down enter. I've got single shot trigger, 1 second per division.

**Dave Jones:** So you can see it's cycling through there and it's now stopped and take a few more seconds. Bingo. And that's exactly the same fault that we saw in the fault in quote marks.

**Dave Jones:** We will get in these little little pulses like halfway up these ramps here. Like what the heck? These little wiggle wiggle wiggle. Yes. And I told you need to be about this and they went hey, it's not supposed to do that.

**Dave Jones:** We think you might have a faulty unit. So we'll ship you another one. Offhand I can't think what fault would sort of like give that issue. But anyway, thank you very much UT.

**Dave Jones:** They did send me a brand spanking new one. So I've written new on the top there. So I can differentiate it. So I've programmed that I did I do believe I've programmed that identically.

**Dave Jones:** Let's have a look um the voltage mode out here doesn't actually matter. Well, I I set it the same like every everything's the same, okay? So, list the mode is the same here.

**Dave Jones:** So, let's plug that in and run that. So, let's switch that over, plug it in, single shot capture again, and let's run that and see if it's any different.

**Dave Jones:** I have not tried this Oh. Oh, yeah? I have not tried this yet, so let's have a look. Let's have a look. They claim they fixed it. They have.

**Dave Jones:** They have fixed it. Look at that. It's a beautiful, absolutely beautiful. Brings a tear to the eye, joy forever. Um absolute beautiful ramp up there. It's even got some nice rounding on there.

**Dave Jones:** So, what have they done? What have they done? I don't know. Um I'm going to check the firmware version just to make sure they haven't tweaked the firmware, but they I'm sure they would have told me that was the case.

**Dave Jones:** They said, "It looks like you got a faulty unit, but I don't know how. If you got any idea, what would actually cause that, um leave in the comments down below." Some sort of loop response thing as it like jumps out, but that's more like Oh, no, that that you know, it could be hardware, but you know, anyway, it depends on how they've implemented, but anyway, let's go down to about

**Dave Jones:** and version 1.1 and version 1.1. So, yeah, fair enough. They have not changed the software at all. So, there you go. It is fixed. Into whether or not or you know, like the first maybe I got a first batch or something and then it does that and they've tweaked the hardware or whether or not it's faulty, but I can't understand it.

**Dave Jones:** Like is a part missing, desoldered? I don't know I don't know. Let's compare the PCBs. I've already got my previous teardown photos from the old unit and the new unit.

**Dave Jones:** I just took two identical hopefully identical photos that we can compare. So, this is the back of the PCB. Couldn't see any issues on the top of the PCB or the through-hole stuff, but you wouldn't expect any of that to change.

**Dave Jones:** If anything, there'd be something maybe subtle in the control circuitry or with the control board, which is different to this one. This is just the main board. If anything, I probably would have expect on the control side cuz that's where like the control loops are.

**Dave Jones:** But anyway, so this is the back side of the PCB and you can see in the file name here, this is the old. So, this is the back of the PCB.

**Dave Jones:** So, this is the old and this is the new one. And I can just toggle between these. So, the new one is the brighter one. So, I've lined these I've rotated and lined these up and hopefully leave it in the comments down below, but I cannot see any difference at all.

**Dave Jones:** There's no bodge wires on either of these boards. So, they haven't bodged anything. There's no As far as I know, like I'm not going to go in and check every component detail, but I can't see any difference.

**Dave Jones:** Like, you know, there's little components down there, for example, that one is is changed from 000 to 0, but they're both 0 ohm jumper links, but there's no value changes.

**Dave Jones:** These unpopulated parts here remain unpopulated, for example, and I'm I'm just not seeing any difference whatsoever. So, as I said, I haven't checked every component value because the rotations have changed on some of the components, a lot of the components between but on both of these boards, but yeah, I'm not I'm not seeing.

**Dave Jones:** There's no additional components. There's no bodges. There's no components left off that were on before. The chip The chips look the same. And yeah, I'm just I'm I'm not seeing it.

**Dave Jones:** So, that's the bottom side, but as I said, I would not expect the main piece to be If anything, I'd expect this one. This is the control PCB. There's no components on the backside.

**Dave Jones:** And this is the old one, so with the bent wire, sorry. I've just got the old photo of the bent wire over there, but yeah, it's Let's just assume that the issue is not under there.

**Dave Jones:** And it looks like like I couldn't get the I haven't tilt corrected this one, so sorry. The bottom of the board's a bit out, but once again, I'm not seeing it.

**Dave Jones:** The the chips are all the same. They're all the same. Uh They've made no differences to the chips at all. Both of like had this like testing mark over here.

**Dave Jones:** This is what this red mark could be here. Somebody's actually actually tested the biggest this is a plug-in PCB. This is the control PCB that has all the control loops on it.

**Dave Jones:** And this is what This is where you'd expect this sort of issue to come up. Although, I don't know how halfway up a step it's going It's wiggling. I don't know.

**Dave Jones:** Leave it in the comments down below if you got any good theories on that. But yeah, I'm I'm not seeing any difference. So, yeah, this board would have been like they would have a production test jig and you can see it's got the right angle pin headers on the bottom here and that that would just plug into a board and they'd have an automated test system that that

**Dave Jones:** test this board. So, each one of these boards would have been thoroughly tested. And again, this is the old one with the bent wire and the new one has the straight one.

**Dave Jones:** And I'm I'm I'm not seeing it. So, I think they're probably right that there's some sort of fault on this board. Maybe there's a dodgy solder joint on this old board here somewhere.

**Dave Jones:** I don't know if you can see it, leave it in the comments, but all the unpopulated parts are still unpopulated. There's no bodge wires. There's nothing on the back of this board whatsoever.

**Dave Jones:** It's only a a a top side load. In fact, there's no traces on the bottom. It's just one big ground plane. Um so, yeah, I'm I am not seeing it.

**Dave Jones:** This can't see any difference whatsoever. So, they haven't bodged it and they haven't updated the firmware. So, I guess they're right in that yeah, this was just just faulty somehow.

**Dave Jones:** I can only presume some dodgy solder joint. But as I said, this board would have been production tested. Maybe it could have been maybe it's an intermittent solder joint or something like that that uh is causing the issue.

**Dave Jones:** But I didn't see any sort of like wiggle wiggle wiggle yeah problems um in any of the other testing. It was only in Lister mode, which is it uses the same control loops.

**Dave Jones:** So, I yeah, I don't I don't understand it why it would happen only in Lister mode, which is really weird. But anyway, there you go. So, that's an interesting comparison.

**Dave Jones:** Thank you, Unity, for acting on that very quickly and sending me a new one and confirming that yeah, maybe it looks like somehow I've got a faulty unit there that doesn't show up in any other modes except Lister mode.

**Dave Jones:** Weird. Anyway, thoughts and comments down below. Catch you next time.
