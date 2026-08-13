---
video_id: r7Cw3GVXl44
title: Open Source Tesla Roadster Firmware?
url: https://www.youtube.com/watch?v=r7Cw3GVXl44
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 18, "2": 36, "3": 51, "4": 66, "5": 83, "6": 102, "7": 127, "8": 144, "9": 169, "10": 184, "11": 204, "12": 222, "13": 239, "14": 254, "15": 271, "16": 287, "17": 312, "18": 331, "19": 346, "20": 366, "21": 384, "22": 398, "23": 414, "24": 429}
---

**Dave Jones:** Hi, just a quick follow-up video to the Tesla Roadster open source video I did on my main channel. Sorry if I'm not talking correctly, it's because this side of my face is numb, and I can't feel my tongue or anything, I just got back from the dentist.

**Dave Jones:** So, yeah, if you see blood coming out, then you'll know I've bitten my tongue and I don't realize it. Okay, thank you very much for MeLoveScotch, I think it is, in the comments section of the previous video pointed out, because a lot of people pointed out, where's the source code, right?

**Dave Jones:** Like, where's the, you know, for the firmware and everything else? And they pointed out that it's on the GitHub, which is not linked on that Tesla page that I could actually find, that Roadster page that I could find. Anyway, Tesla's GitHub here, they do actually have it.

**Dave Jones:** They just released it the other day, updated it yesterday, I don't know if it's been there before, but yeah, you can actually go in here, and they've got, it just says diagnostic software, so, like, I don't know if it's actually the firmware for the, it seems like it's the firmware for the whole car.

**Dave Jones:** Anyway, they've got an ISO file here, so I've downloaded that, and it's, you know, it's a couple hundred meg, and here's all the stuff in the file here, okay? And it's got, it looks like all the previous versions, right? So this is really quite good.

**Dave Jones:** It's really difficult to talk. It's got the boots, I don't, you know, I'm not into this sort of stuff, so, I don't know, leave it down, you know, thoughts in the comments down below, I don't know what a pet file is. Help message, what is that, is there anything in that?

**Dave Jones:** Cannot open, no. I can open that with, can I open that? No, edit. Can I open? So it's got isolinux.bin, whatever that is. A puppy slacco. What's puppy slacco? I don't know. But anyway, it does have all the firmware versions here, so if we actually open the latest one, roads to 5.2.0,

**Dave Jones:** I presume this is, like, the software that you download to the car. Does the roads to have the big instrument, you know, the big tablet, phablet, the interface thing? I don't know, it's been so long. And here we go, it seems to have, like, the entire vehicle firmware.

**Dave Jones:** Firmware. Firmware? Like Jar Jar Binks, you know, when he gets his tongue zapped. This is ridiculous. Vehicle firmware. I can't say it. Vehicle firmware. So, yeah, it looks like that's all there, but that's not down to the circuit level, right? That's not that PIC processor, for example,

**Dave Jones:** that we saw in the previous video or anything like that. So it's got tools. What have we got? Perl. No idea what any of that does. Monitor. What does that do? No idea. Anyway, all the programmers will be leaving it in the comments down below,

**Dave Jones:** and then we can open the release notes. There you go. Bugs fixed. VMS. LG. Cells. I presume they're LG battery cell support. I changed hardware ID. I presume that's what that means. Does it arose to use LG cells? I thought it was Panasonic.

**Dave Jones:** But maybe there was an option for that. Don't know. Don't know. But that's what it seems like. Anyway, so, yeah, vehicle firmware. So there it is. There's Linux. Yeah, but this is only top level stuff. It's not the lower level thing. Like, we didn't get any of the lower level CAD files, of course.

**Dave Jones:** Some people mentioned that, well, one person mentioned in the comments that Tesla did not design a lot of the electronics that went into the Roadster, apparently, so they don't have the rights to it to actually release it open source, and that might be fair enough.

**Dave Jones:** I don't know. You know, do they have, like, the motor, the drive module? Did somebody else develop that and they just have to get their permission to release it as open source, even though maybe they paid for the development? I don't know. If you have any clue, leave it in the comments down below.

**Dave Jones:** But, yeah, so this is only the high level stuff. I mean, you know, it's got, like, firmware, but no, this is, I do believe, please correct me if I'm wrong, what's a shifter? I don't know. Are these different hex files? These look like different hex files for different, because, of course,

**Dave Jones:** when you update the firmware, there could be a processor on there that not only updates its own firmware, but then can actually remote program update all of the smaller modules and stuff like that, so it could actually be in there. But, yeah, so there's HVAC.

**Dave Jones:** Okay, so it looks like this is for different modules, CPLD, R3, whatever that is, BSM, is that some sort of battery thing? And the shifter is the, you know, is it manual? I don't know. I got no idea. Yeah, so maybe these are the firmware for the different modules and

**Dave Jones:** stuff like that, so maybe it does actually have, well, no, it's only got two, like, no, that's not source code, right? These are just the hex files, right? I mean, we can go further in here, vdsapp.bin, no? No, they're just image files. This is not firmware.

**Dave Jones:** So, no, I'm going to say nope on that. Nope for the source code, unless I'm missing it. Please leave it in the comments if I have missed it, but no, I don't see the source code, I just see various firmware image files for the

**Dave Jones:** main processor and maybe some auxiliary processors that it has access and the ability to update to. But I don't know, what is a puppy slacker? I mean, that's enormous. That's most of the file size here. SFS, sorry, not that type of programmer. I don't know what any of that is.

**Dave Jones:** So that's where the maybe is the source code in there? Don't know. But, like, to me, dummy programmer Dave, like, you know, I can just do basic C and assembler at the micro level. I'm not into, like, anything else is not my thing.

**Dave Jones:** So, yeah, I'm going to say that's yeah-nah. That's a yeah-nah, as we say here in Australia. That is not, I'm not seeing the source code, unless the only place I can see it is that it's buried away in there, because it certainly doesn't

**Dave Jones:** seem to be in the zip. It's just the hex and image files, the downloadables. So that ain't source code, I'm afraid. But there you go. So thank you for telling us about the GibHub. I didn't know that exists, and they didn't link it in on the main page.

**Dave Jones:** But there you go. So there's some additional stuff there. But, yeah, it's not all that low-level stuff. We didn't get the low-level schematics. We didn't get any, like, hardware CAD files for any parts, really. Was there? I don't know. Did I miss it?

**Dave Jones:** Please let me know if I did. But, yeah, no hard, no low-level CAD files, no low-level module schematics or anything like that. And no low-level source code. So, oh, well, I didn't expect it, but there you go. Quick update. Thanks. Catch you next time.
