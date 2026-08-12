---
video_id: 41gK3lYejgE
title: Microsoft Just Open Sourced GWBASIC !
url: https://www.youtube.com/watch?v=41gK3lYejgE
source: youtube-asr
timestamps: {"0": 0, "1": 27, "2": 61, "3": 82, "4": 96, "5": 128, "6": 149, "7": 173, "8": 196, "9": 227, "10": 261, "11": 281, "12": 307, "13": 333, "14": 355, "15": 372, "16": 396, "17": 422, "18": 452, "19": 471, "20": 498, "21": 520, "22": 553, "23": 567, "24": 602, "25": 624, "26": 662, "27": 688, "28": 704, "29": 732, "30": 771, "31": 787, "32": 800, "33": 826, "34": 848, "35": 877, "36": 895, "37": 926, "38": 954, "39": 982, "40": 1014, "41": 1040, "42": 1066, "43": 1089}
---

**Dave Jones:** Hi, this is going to be an interesting one. Well, interesting from a historical perspective for me anyway. Microsoft have just announced that they've open-sourced the original GW-BASIC from 1983. I'm not sure which version it Actually, did GW-BASIC even have versions back then? I can't I can't remember. It's been so long ago. But, they just open-sourced it. Absolutely fantastic.

**Dave Jones:** So, it's on the GitHub's over here. And let's have a look. I thought we just open some of this source code and have a look at the original source code because I That's where I got my start using GW-BASIC in terms of programming. And of course, then I I went on to QuickBASIC and QuickBASIC 4.5. I wrote a ton of stuff including commercial software with QuickBASIC 4.5. And then I went on to Microsoft BASIC Professional Development System PDS 7.1.

**Dave Jones:** Hands up if you remember Microsoft BASIC PDS 7.1 which included all sorts of libraries for like window like kind of like text-based window user interfaces and all sorts of stuff like that. So, leave it in the comments if you were a BASIC PDS fanboy like I was.

**Dave Jones:** I sold a couple of commercial products. And then I kind of went off BASIC. I moved into Borland Pascal for DOS. And then I And then I moved on to then when Windows was a thing, I moved on to Delphi for Windows.

**Dave Jones:** And yeah, it's a fascinating. And if you don't know Altium who I used to work for, that was originally written in Borland Pascal as well. And then when they released the Windows versions, they moved over to Delphi. And for many years they had a lot of issues because of the Delphi environment. I believe they ported most of it over anyway. That's just a little um Altium historical uh perspective there. But yeah, anyway, um it's in 8088 uh assembly language. Little historical uh context, there you go. And Men at

**Dave Jones:** Work topped the US uh charts with Down Under. Dustin Hoffman was in Tootsie. Um Return of the Jedi came out. WarGames. Fantastic uh '83. And uh Chris Hemsworth was born that Ronald Reagan was president. Margaret Thatcher, the Iron Lady, was UK's prime minister. This is absolutely fantastic.

**Dave Jones:** Anyway, um where's the source code? Uh this It's 100% assembly language. Why assembly? Why didn't they use? When developing on the mainframe computer, developers sometimes I would use high-level languages like Fortran, Lisp, Cobol, blah blah blah. But compilers were often hugely expensively expensive, rarely generated efficient code, and were generally unavailable for the space or performance constraints.

**Dave Jones:** Um was this source translated? This source was translated. Each of the assembly source files contains a header statement. This was translated since the instruction set ISA of the early processors using home and personal computers weren't spectacularly different from one another, Microsoft was able to generate a substantial amount of code for a port from the sources of a master implementation.

**Dave Jones:** Okay. So that's interesting. So they didn't So they had a translation program to generate this assembly code? Hm, if you know more details about that, please post it in the comments uh down below. But anyway, um this won't be an analysis because I haven't done uh 8088 assembly language uh for like 30 years. I did a bit of it and I I forget all of it. So yeah. Anyway, um I've downloaded it from the GitHub here.

**Dave Jones:** So and here it is. Let's load her up. So we've got ASM source files. Uh probably some header file Yeah, header files. What else we got? Security MD, no idea what that is. Let's sort by type. All the ASM and headers. So, here it is. Here we go. Um I assume that GW-MAIN is the main one. So, let's go. By the way, yeah, I am not a like Programming's not my thing. Um so, yeah, I'm just bumming around here for old time's kicks. Here it is. This

**Dave Jones:** translation created 10th of February 1983 version by version for That's what they were talking about. Radix 8 uh to be safe, I have no idea. Segment public um include bin trap, I assume that is {dot}h. Um GW-MAIN copied from {dot}mac.

**Dave Jones:** So, is {dot}mac Is that where what they were make like a higher That's a higher-level thing that they were doing? And then they were kind of uh recompile in that cuz of course they released um a basic for many different um operating systems. Look at this. I love it. Copyright 1975 by Bill Gates and Paul Allen. Originally written on the PDP-10 from February 9th to April 9th, 1975.

**Dave Jones:** Bill Gates wrote a lot of stuff. Paul Allen wrote a lot of other stuff and fast code. Monte Davidoff, for those who are unaware, he's the uh one of the original uh founders of Microsoft and he sold his I can't remember what uh percentage he had in Microsoft at the time, but uh yeah, he um sold out uh really early. I believe Oh, was he No.

**Dave Jones:** No, I'm Might be thinking of the Apple story. Anyway, Monte Davidoff is certainly he famously um although obscurely famously um yes, he wrote the math package uh for GW-BASIC because apparently um Bill and Paul were like too busy uh writing stuff. This is felt like the original Altair, like was it the Altair stuff?

**Dave Jones:** And, uh, which they started of course they didn't start with GW BASIC. It was originally, um, Altair was their first one. So, a lot of this code would have, uh, come from there and been, uh, ported over. But, yeah, anyway, they didn't have time to write the floating point math package. Um, maths.

**Dave Jones:** Australian, not that American math rubbish. I kind of in the habit of saying math these days. Don't know why. Maths. Monte Davidoff wrote the maths package, um, f4i.mac. There you go. So, anyway, yeah, but he he wasn't around after that in, uh, Microsoft that I'm aware of. But, anyway, um, here we go. X list, don't know what these are.

**Dave Jones:** The 4 FE extended tokens. I Zenith 8086. Um, no, we're not on a Zenith. We're not what a Tetra. What's that? CPM 86. Hell. The hell 9000. This is great. Toshiba. That's got to be Toshiba. So, I'm assuming that these are different target platforms. Number of text pages.

**Dave Jones:** Anyway, interesting. There's not comments on everything. So, okay, we've got externals. And there's no comments on any of those. The following block of externals was added on December 19th, 1982 when bin trap was split up after the freeze of GW BASIC version 1. This split up was not reflected in the blah. See See Tom Corbett. Leave it in the comments if you know who Tom Corbett is. See Tom Corbett if you have any questions. Maybe we can still find Tom and we can ask him. Good

**Dave Jones:** on you, Tom. Following externs are defined. Uh, the reserved word table are in another module. Consequently, many things must be declared external. Uh, all of these things are in code segments, so I guess they couldn't make it as as modular as they wanted. They just external everything. She'll be right. No worries.

**Dave Jones:** Uh since the dispatcher was no longer been trapped, maybe addressed. I like the comments are the interesting stuff. I don't care about the code. Like I do not remember um assembly 8086 assembly. I used to do a bit of it, and I just don't remember a damn thing. Um it's been way too long. 8086 versions for stack entries to be an even length, so stack accesses won't cross word boundaries. Yes, 8086 would be different to the 8088. Although I thought the 8088 I thought they were the same except the

**Dave Jones:** 8088 had an ex- 8-bit external interface. Um but what that wouldn't change the stack access, would it? Hmm, leave it in the comments down below if you know. I like I thought it was just like I don't know like external access. The actual um assembly for them shouldn't be any different.

**Dave Jones:** Uh so, that's from my memory anyway. Uh this routine is called to reset the stack if basic is externally stopped and then restarted. Right. Illegal file name. Okay, so here's some uh no. Okay, yes, so here's a der- der mac. I have no idea what that is. Um so, they I assume like these are links to some of the uh strings that they would have had. So, of course, you know, when GW BASIC responds with something, it has that's text string stored somewhere.

**Dave Jones:** Wow, there's a like Look at this guy like there is a lot of code. There is a lot of wow, I didn't realize that GW BASIC had so much code. What was the like the uh binary file size of GW BASIC?

**Dave Jones:** Don't don't remember. Don't remember, but uh like some of like some of the original basics, they were very lean and mean. So, anyway, yeah, um as to uh like Paul Allen writing the fast other stuff and fast code. But, um of course, Bill is famous for writing fast code. In fact, for many decades, I do believe he held the record for the fastest sort routine or something like that. Please correct me down below if I'm wrong. But, yeah, he he came up when he was at Harvard or

**Dave Jones:** wherever. Yeah, I think he came up with a a routine that was um still like the fastest routine decades later or something. It was some sort of sort some sort of sort based problem or something like that. So, yeah, Bill can certainly write fast code if he wants to. But, look at it all. Look at it all.

**Dave Jones:** Wow. This is a huge amount of assembly code. Wow, how much pizza was consumed to write this? So, so this was generated code? Would it have come with the comments have been copied over from the original whatever higher level stuff that they did or whatever? I'm not not sure what the deal is. But, look there there like you know, it was obvious. Oh, yeah, it's obvious what exchange does here. But, coerce the final value there really as well as double precision gives strings a type mismatch.

**Dave Jones:** You know, there's lots of like they're commenting almost every line there. Which which you have to do in assembly because it's like like some things are obvious. But, if you're fluent in in assembly, then some things are obvious. But, yeah, this is why you get like comments per line and stuff like that. Some of the stuff at the top didn't. But, once you get into the nitty-gritty of it, possible on go subs.

**Dave Jones:** Go sub, those were the days. Octal constant, hexa constants. Anyway, look, I I'm not going to go through all the code cuz this is just insane. But, wow. So, this is just the main routine. This would be the disk routine, would it?

**Dave Jones:** Uh common routines for disk basics. Uh yep, any I'm I'm I'm after the comments. The comments are the most fascinating things in stuff like this. So, 50 handles the while wind uh 80 80 80 stack is used to put an entry. Format is as follows. There you go. An even length, yeah. Okay. Maybe that's what they're talking about, 8086. They're not talking Maybe they're talking about the difference between the 8080 and the 8086/8088.

**Dave Jones:** Maybe that's the difference. IBM res.h. So, these are all the if defines. Gee, yeah. Oh, Tom Corbett, here you go. Here's Tom again. Early employee, Microsoft. It's been strapped. So, here's the math routine written by Monty Davidoff. Doesn't say he wrote it. Once again, like comment virtually every line because you have to. Otherwise, if you go back in there, you'd have have no clue, really. It's It's much more difficult to even somebody fluent in assembly could go back in here. Like I look at my old

**Dave Jones:** assembly code. I did it in like my 1K video, my video number 1,000. And I Or was it 1,024? Yeah, it was 1,024 where I looked at some old original PIC assembly language code. So, I'll link that one in.

**Dave Jones:** Uh if you haven't seen it, I I I don't know. I can't go in and recall PIC assembly language. Like I used to be good at it. Now, it's like it's It's just Klingon. Talking about the mantissa. Good on you, Monty.

**Dave Jones:** Looks like he writes Looks like Monty writes good code. I wonder know doing these days. Screen driver. So, they're just like all the That's just like scrolling routines and stuff. Wow. Line feed terminating line terminator. That's to do with the RAM keyboard support. Why is there keyboard support variables in RAM and stuff like that? Don't know what DB is.

**Dave Jones:** Initialize the jump vector for exit to MS-DOS. Requires that exit is made through the segment prefix table. I'm sure it's bringing This is bringing back a lot of memories for a lot of people. The following code scans a CPM command line for basic. Wow. Yeah, so it's obviously, you know, ported over from other other platforms. That's interesting.

**Dave Jones:** There's a routine called it's a 86. So, what are they Are they detecting that it's an 8086 resident initialization for Intel 8086? And it gets discarded. Love it. So, they have to detect what processor type they're using and oh, that's it. This is the keyboard routine. Check this out. They got a nice little text flowchart here to describe the operation of this thing.

**Dave Jones:** Very nice commenting. Love it. So, yeah, I can't go through all the code, but some of the comments I'm sure there's like some classic comments in here. If you can find them, please leave it in the comments down below. But yeah, classic from 1975 by Bill Gates and Paul Allen.

**Dave Jones:** And don't forget David off. He wrote the maths package. And they of course famously had to write this on the PDP-11. They had to simulate it. They had to simulate the 8080 because that was used in the Altair computer. And of course, they phoned up Ed Roberts who designed the Altair. And and they said, "Oh, look, we've we've got a basic for that runs on the Altair." And they didn't have it. Of course, they were just, you know, they knew they could probably write one, but they were just,

**Dave Jones:** you know, I'm spinning a yarn saying, "Oh, yeah, we've got this." And then he said, "Oh, yeah, come down." Okay, so they they started writing the damn thing. And of course, they famously couldn't They didn't have a machine to run it on, so they had to simulate it, and they didn't know on on the PDP-10 mainframe, and they didn't know if it would actually work on the real hardware, cuz they didn't have the real hardware. And then when they I Paul flew down there because Bill he

**Dave Jones:** was like the older, more mature-looking of the two, and he flew down to Albuquerque where MITS was, who designed the Altair and made it, and uh so he flew down there with the paper tape to load in the BASIC. And of course, they forgot the bootloader routine. So Paul Allen had to write the bootloader routine on the plane. So when he turned up and they put the paper tape in, and amazingly, it actually worked.

**Dave Jones:** And of course, they got the deal. Um I think Paul Allen was technically an employee of MITS, but Bill Gates claims he never was an an employee of MITS. So yeah, they were anyway Microsoft, and that's how they got their start, of course. The paper tape. And of course, Bill Gates published the famous I can't forget I forget the publication it was in, but the famous open letter to hobbyists where he basically said, "Look, don't steal our paper tape. You know, we put thousands" even though they got the computer time

**Dave Jones:** for free cuz it was at the university. They said, "Look, we put, you know, thousands All this computer time cost money" cuz back then mainframe computer time cost a lot of money. So they put, you know, tens of thousands, however many or hundreds of thousands of dollars worth of computer time he claimed into this thing, and everyone was just at the at the computer meetups and stuff. They were just handing out copies of the paper tape of Microsoft BASIC and things like that. So, yeah, the famous open

**Dave Jones:** letter to hobbyists. Um that's a classic. Go and look that one up. But anyway, yeah, that's uh that's fascinating. I knew they actually wrote it in a high-level thing and then sort of like targeted it down. Um so, if you got more details on that, uh please leave it in the comments down below. I'd like to know the details. But anyway, I I just love that. Good on Microsoft for uh releasing the uh for open, you know, open-sourcing. I I I don't think it's for I'm not sure what the license I

**Dave Jones:** think he mentioned something in the article about the license or something. Anyway, um anyway, they've released the source code. It's on the GitHubs. Absolutely fantastic. The original GW-BASIC. I wonder if they'll ever release QuickBASIC or BASIC PDS. Um that'd be fantastic, but yeah. Anyway, Bill Gates and Paul Allen, legends. And Monte Davidoff, come on.

**Dave Jones:** Let's not forget poor old Monte. Anyway, catch you next time.
