---
video_id: 2CDN8EQmOeo
title: EEVblog #1306 (3 of 5) : How to program an STM32 using DFU Bootloader
url: https://www.youtube.com/watch?v=2CDN8EQmOeo
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 17, "2": 31, "3": 47, "4": 67, "5": 84, "6": 98, "7": 116, "8": 132, "9": 150, "10": 170, "11": 186, "12": 205, "13": 226, "14": 245, "15": 257, "16": 271, "17": 290, "18": 300, "19": 308, "20": 316, "21": 324, "22": 332, "23": 340, "24": 348, "25": 356, "26": 364, "27": 372, "28": 380, "29": 388, "30": 396, "31": 404, "32": 412, "33": 420, "34": 428, "35": 436, "36": 444, "37": 452, "38": 460, "39": 468, "40": 476, "41": 484, "42": 492, "43": 500, "44": 508, "45": 516, "46": 524, "47": 532, "48": 540, "49": 548, "50": 556, "51": 564, "52": 572, "53": 580, "54": 588, "55": 596, "56": 604, "57": 612, "58": 620, "59": 628, "60": 636, "61": 644, "62": 652, "63": 660, "64": 668, "65": 676, "66": 684, "67": 692, "68": 700, "69": 708, "70": 716, "71": 724, "72": 732, "73": 740, "74": 748, "75": 756, "76": 764, "77": 772, "78": 780, "79": 788, "80": 796, "81": 804, "82": 812, "83": 820, "84": 828, "85": 836, "86": 844, "87": 852, "88": 860, "89": 868, "90": 876, "91": 884, "92": 892, "93": 900, "94": 908, "95": 916, "96": 924}
---

**Dave Jones:** Hi, welcome to part three in the Paduk 3-cent microcontroller programming series, where we build up open-source hardware and software to program these 3-cent microcontrollers. Now, in part two, we looked at actually assembling this PCB, but you plug it in, it doesn't do anything.

**Dave Jones:** It's dumb, because the Atmel processor on here is completely blank. So we have to program the firmware into this thing, but without using an Atmel programmer. We're going to use what's called DFU, or Device Firmware Upgrade, via the USB. And it sounds easy, but there's a few traps for young players.

**Dave Jones:** Let's go. Okay, we've got our board assembled, and yes, I do have a little SO8 SMD adapter for that. I actually did have one. You can see a little SO8 chip in there at the moment. I just happened to have one that was lying around.

**Dave Jones:** I forgot to order one, but I did actually have one. So, no wuckers. I could have just bodged in an SMD adapter board anyway. Anyway, doesn't matter. What we want to do now is actually program the STM32 Micro on this thing, which is an STM32F072C8T6, for those playing along at home.

**Dave Jones:** And if you actually plug this in, it's not going to do anything, because it's not programmed. There's no bloop in Windows to tell you that this thing's actually plugged in, because it's not. Well, it's not doing anything. So the first thing we want to do is actually measure the voltage regulator on here,

**Dave Jones:** because we do have a 3.3 volt voltage regulator. So we just want to measure across one of these bypass caps here, just, you know, surrounding the micro, just to make sure we get 3.3 volts. So I can't easily put this on screen, so you have to trust me.

**Dave Jones:** I'm probing it. Yep, minus 3.3 volts, because I had my probes backwards. But yeah, so we've got 3.3 volts. So there's 3.3 volts going to the micro. Now, we can't actually measure this other stuff down here, like 6.6 and 13 volts programming. These are the programming.

**Dave Jones:** So the VDD and the programming voltages down here that go off to the micro, because these need to be enabled and things like that. Now, program, I don't know, we could try, but it doesn't matter. We can do that later. All we care about is getting our micro working, 3.3 volts on there,

**Dave Jones:** and that our USB is connected here, and it's going through, and then it goes through, and it actually programs. Now, we're not actually going to use this header here to program. We actually could using the STM tools, but the good thing about the STM32 processors, and a lot of other processors,

**Dave Jones:** is that they have a built-in serial bootloader in them, which means you can just connect straight up to the USB and talk to the thing, and program that using programming software. It's called DFU, and DFU mode stands for Device Firmware Upgrade, and it supports like several different processes support the same thing.

**Dave Jones:** So the one DFU programming software can potentially support multiple different programmers. STM32 being one of them, because you saw I just plugged it in, and Windows didn't detect it at all, because there's nothing in there. What you have to do, and on here, I'll take off that SO8 adapter.

**Dave Jones:** There's a little button on here, which you have to press down, hold down, and then when you plug it in, hopefully, fingers crossed, we'll get the Windows. There it is. Hopefully, you heard that. If we go over to Device Manager, and there it is, other devices, STM32.

**Dave Jones:** Bootloader, winner, winner, chicken dinner. That means, oh, whoa, it's gone, aha, and that looks like it's Windows. That's gone over to here, rather than other devices. It's now, Windows probably just installed the driver-y thing for it, and now it's a universal serial bus controller, and it's the STM device in DFU mode.

**Dave Jones:** So Windows automatically knows about this. I don't know about Linux and Mac or whatever. I don't know. You're on your own, but STM device. So that means that our... Micro is soldered correctly, our 3.3-volt voltage regulator here, U2 is all working, and our resistance, you know, there's no shorts on the data lines.

**Dave Jones:** Our USB connector is soldered correctly, and, you know, because there's a lot of little, you know, tiny little joints in there. You can get a little, you know, hairline short or something like that between one of the data lines, and it just wouldn't do anything.

**Dave Jones:** And I was hoping that it wouldn't work, so I'd have to do some troubleshooting, but, yeah, can't always win them. Anyway, I hope yours doesn't work. I hope you've handled this up, or your next project doesn't work, so you have to troubleshoot it, because you learn a lot when things fail,

**Dave Jones:** and you have to troubleshoot them. If these work first go, okay, you've learned how to solder, but, you know, you haven't learned how to troubleshoot. Anyway, so this micro is now talking. So now we can download the DFU programmer software. So now if we go to the GitHub's software sources can be found,

**Dave Jones:** Easy PDK Programmer Software, and if we go into Firmware here, we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.

**Dave Jones:** So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here. So we can see that we've got a lot of stuff here.
