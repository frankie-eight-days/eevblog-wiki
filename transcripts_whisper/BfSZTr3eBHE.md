---
video_id: BfSZTr3eBHE
title: GCC Embedded Linker Issue Stops uSupply Development
url: https://www.youtube.com/watch?v=BfSZTr3eBHE
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 13, "2": 45, "3": 67, "4": 85, "5": 106, "6": 135, "7": 153, "8": 176, "9": 204, "10": 239, "11": 252, "12": 274, "13": 294}
---

**Dave Jones:** Okay, so I've been working on the firmware for the microsupply and I've come across a link error. You know it's a link error when it gives you no explanation about what was wrong, and here you have literally no explanation. It just says, LD returned 253 exit status.

**Dave Jones:** Oh okay, that sounds like something that would be documented, right? No, no, not at all. So, all you have to do is search here, and you just get my results, which aren't helpful because, you know, and no one really had an idea what was wrong,

**Dave Jones:** other than maybe just giving me the advice that this is a bug because the linker should succeed the linker should succeed or fail with a diagnostic message, otherwise it is a bug. Okay, fair enough. The best thing to do is to go report it to the authors of the tool, right?

**Dave Jones:** Okay, so in I go, and if you read the things that they tell you to do when you post here, they say dump all the things, so that's why there's a giant dump of all the log. Okay, anyway, so I dump all the information, give some explanations about what I've done, blah, blah,

**Dave Jones:** blah, blah, then they say, okay, it sounds like a resource issue. I suspect the linker is running out of memory or maybe stack space and crashing. Okay, I agree. I agree, it does sound like that. So, I give you some instructions, I tried some flags to reduce memory usage,

**Dave Jones:** nothing changed. I tried running it through a debugger, which produces an interesting result. So, I set up a debugger in Visual Studio and, whoop, might as well stop that. I set up the debugger in Visual Studio to run LD and I have this enormous linker, this enormous command,

**Dave Jones:** which runs the linker, because usually this is generated, but not today. I have to manually run it. I can't run G++, I have to run LD. So, great. So, then all I have to do is run the debugger. Loading symbols, that's great. We want those.

**Dave Jones:** Hopefully, it makes it debuggable. Oh, dear. So, it is a stack overflow. Okay, so let's look at the stack frames. Oh, no, there's no debugging information at all. We only care about the latest stack frame, that's this one here. And this one looks extremely suspect to me, but I'm just going to ignore that for now.

**Dave Jones:** And we only care about that. And, oh, no, there's no symbol information. Or at least maybe Visual Studio couldn't find it. So, okay. Yeah, that looks like no symbol information. Anything? Anywhere? So, maybe there's some other things you can try. Maybe there's another linker.

**Dave Jones:** Well, there's one called LLD used by the Clang tool chain. And there's another one, the Microsoft Visual C linker, mlink.exe or something. And there's also one called LD gold. That's one that will eventually replace LD.exe probably. Only one problem. None of them can link for arm m0.

**Dave Jones:** So, this is where I am. This is where I'm stuck. And these kind of issues. I'm kind of at the whim of the linker developer, unfortunately. So, usually they're quite good at fixing things like this. But there's no guarantee they'll be able to fix it.

**Dave Jones:** I've posted exactly what happened, but that may not even help them at all. So, great. Anyway, I've gotten stuck. And if anyone has ideas how to fix this, it would be very helpful. Because I'm still stuck. So, there is an update coming. The quarter 4 2018 GCC update.

**Dave Jones:** That very likely has some information which might be able to fix this. And I'm looking forward to that. But there is the potential it won't. And I may have to do some radical changes to the code to make it behave very differently so that I don't get this issue.

**Dave Jones:** That's all I have to say. Have a good day.
