---
video_id: c0evM3-GTAw
title: Weird Uni-T UDP6731 PSU Fault FIXED. I got a DUD?
url: https://www.youtube.com/watch?v=c0evM3-GTAw
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 28, "3": 41, "4": 53, "5": 68, "6": 84, "7": 98, "8": 112, "9": 129, "10": 145, "11": 161, "12": 174, "13": 186, "14": 207, "15": 220, "16": 238, "17": 250, "18": 260, "19": 270, "20": 288, "21": 302, "22": 320, "23": 333, "24": 352, "25": 365, "26": 380, "27": 393, "28": 409, "29": 422, "30": 434, "31": 449, "32": 462, "33": 475, "34": 487, "35": 500, "36": 517, "37": 531}
---

**Dave Jones:** Hi, just a quick follow-up video on this UT UDP 6731 power supply. The review I did a full review of that. It was quite popular. But there was one issue with it and that was the Lister mode here. So we've got

**Dave Jones:** the regular voltage mode and then we've got the delay mode and then we've got the Lister mode which allows you to program in different voltage steps and like a time delay between each one so that you can step your waveform up and I

**Dave Jones:** just did a simple thing and in that video I just programmed in a simple 1 V step. So 1 V, 2 V, 3 V, 4 V, 5 V. So five counts total and it cycles through one time. So it just does all those

**Dave Jones:** steps through that five those five steps one time. And there's one second delay between each one. Current limit doesn't matter. Just set it to like a 2 amps and we had a problem with it. So let's see if we

**Dave Jones:** can recreate that. Now I've got the exact same conditions that we had in the video. So let me run that. Hold down enter. I've got single shot trigger, 1 second per division. So you can see it's cycling through there and it's now

**Dave Jones:** stopped and take a few more seconds. Bingo. And that's exactly the same fault that we saw in the fault in quote marks. We will get in these little little pulses like halfway up these ramps here. Like what the heck? These little wiggle

**Dave Jones:** wiggle wiggle. Yes. And I told you need to be about this and they went hey, it's not supposed to do that. We think you might have a faulty unit. So we'll ship you another one. Offhand I can't think what fault would

**Dave Jones:** sort of like give that issue. But anyway, thank you very much UT. They did send me a brand spanking new one. So I've written new on the top there. So I can differentiate it. So I've programmed that I did I do believe I've programmed

**Dave Jones:** that identically. Let's have a look um the voltage mode out here doesn't actually matter. Well, I I set it the same like every everything's the same, okay? So, list the mode is the same here. So, let's plug that in and run that. So, let's

**Dave Jones:** switch that over, plug it in, single shot capture again, and let's run that and see if it's any different. I have not tried this Oh. Oh, yeah? I have not tried this yet, so let's have a look. Let's have a look. They claim

**Dave Jones:** they fixed it. They have. They have fixed it. Look at that. It's a beautiful, absolutely beautiful. Brings a tear to the eye, joy forever. Um absolute beautiful ramp up there. It's even got some nice rounding on there. So,

**Dave Jones:** what have they done? What have they done? I don't know. Um I'm going to check the firmware version just to make sure they haven't tweaked the firmware, but they I'm sure they would have told me that was the case. They said, "It looks like

**Dave Jones:** you got a faulty unit, but I don't know how. If you got any idea, what would actually cause that, um leave in the comments down below." Some sort of loop response thing as it like jumps out, but that's more like

**Dave Jones:** Oh, no, that that you know, it could be hardware, but you know, anyway, it depends on how they've implemented, but anyway, let's go down to about and version 1.1 and version 1.1. So, yeah, fair enough. They have not changed the software at all.

**Dave Jones:** So, there you go. It is fixed. Into whether or not or you know, like the first maybe I got a first batch or something and then it does that and they've tweaked the hardware or whether or not it's faulty, but I can't

**Dave Jones:** understand it. Like is a part missing, desoldered? I don't know I don't know. Let's compare the PCBs. I've already got my previous teardown photos from the old unit and the new unit. I just took two identical hopefully identical photos that we can

**Dave Jones:** compare. So, this is the back of the PCB. Couldn't see any issues on the top of the PCB or the through-hole stuff, but you wouldn't expect any of that to change. If anything, there'd be something maybe subtle in

**Dave Jones:** the control circuitry or with the control board, which is different to this one. This is just the main board. If anything, I probably would have expect on the control side cuz that's where like the control loops are. But

**Dave Jones:** anyway, so this is the back side of the PCB and you can see in the file name here, this is the old. So, this is the back of the PCB. So, this is the old and this is the new one.

**Dave Jones:** And I can just toggle between these. So, the new one is the brighter one. So, I've lined these I've rotated and lined these up and hopefully leave it in the comments down below, but I cannot see any difference at all. There's no bodge

**Dave Jones:** wires on either of these boards. So, they haven't bodged anything. There's no As far as I know, like I'm not going to go in and check every component detail, but I can't see any difference. Like, you know, there's little components down

**Dave Jones:** there, for example, that one is is changed from 000 to 0, but they're both 0 ohm jumper links, but there's no value changes. These unpopulated parts here remain unpopulated, for example, and I'm I'm just not seeing any difference whatsoever.

**Dave Jones:** So, as I said, I haven't checked every component value because the rotations have changed on some of the components, a lot of the components between but on both of these boards, but yeah, I'm not I'm not seeing. There's no additional

**Dave Jones:** components. There's no bodges. There's no components left off that were on before. The chip The chips look the same. And yeah, I'm just I'm I'm not seeing it. So, that's the bottom side, but as I said, I would not expect

**Dave Jones:** the main piece to be If anything, I'd expect this one. This is the control PCB. There's no components on the backside. And this is the old one, so with the bent wire, sorry. I've just got the old photo of the bent wire over there, but

**Dave Jones:** yeah, it's Let's just assume that the issue is not under there. And it looks like like I couldn't get the I haven't tilt corrected this one, so sorry. The bottom of the board's a bit out, but once again, I'm not seeing it.

**Dave Jones:** The the chips are all the same. They're all the same. Uh They've made no differences to the chips at all. Both of like had this like testing mark over here. This is what this red mark could be here. Somebody's

**Dave Jones:** actually actually tested the biggest this is a plug-in PCB. This is the control PCB that has all the control loops on it. And this is what This is where you'd expect this sort of issue to come up. Although, I don't know how

**Dave Jones:** halfway up a step it's going It's wiggling. I don't know. Leave it in the comments down below if you got any good theories on that. But yeah, I'm I'm not seeing any difference. So, yeah, this board would have been like they

**Dave Jones:** would have a production test jig and you can see it's got the right angle pin headers on the bottom here and that that would just plug into a board and they'd have an automated test system that that test this board. So, each one of these

**Dave Jones:** boards would have been thoroughly tested. And again, this is the old one with the bent wire and the new one has the straight one. And I'm I'm I'm not seeing it. So, I think they're probably right that there's some sort of fault on this

**Dave Jones:** board. Maybe there's a dodgy solder joint on this old board here somewhere. I don't know if you can see it, leave it in the comments, but all the unpopulated parts are still unpopulated. There's no bodge wires. There's nothing on the back

**Dave Jones:** of this board whatsoever. It's only a a a top side load. In fact, there's no traces on the bottom. It's just one big ground plane. Um so, yeah, I'm I am not seeing it. This can't see any difference whatsoever. So,

**Dave Jones:** they haven't bodged it and they haven't updated the firmware. So, I guess they're right in that yeah, this was just just faulty somehow. I can only presume some dodgy solder joint. But as I said, this board would have been production

**Dave Jones:** tested. Maybe it could have been maybe it's an intermittent solder joint or something like that that uh is causing the issue. But I didn't see any sort of like wiggle wiggle wiggle yeah problems um in any of the other testing. It was

**Dave Jones:** only in Lister mode, which is it uses the same control loops. So, I yeah, I don't I don't understand it why it would happen only in Lister mode, which is really weird. But anyway, there you go. So, that's an interesting

**Dave Jones:** comparison. Thank you, Unity, for acting on that very quickly and sending me a new one and confirming that yeah, maybe it looks like somehow I've got a faulty unit there that doesn't show up in any other modes except Lister mode.

**Dave Jones:** Weird. Anyway, thoughts and comments down below. Catch you next time.
