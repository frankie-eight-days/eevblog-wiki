---
video_id: 6vbI-r5aXJI
title: EEVblog #1080 - Gigatron TTL RISC Kit Computer Review
url: https://www.youtube.com/watch?v=6vbI-r5aXJI
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 17, "2": 43, "3": 62, "4": 80, "5": 99, "6": 118, "7": 134, "8": 153, "9": 173, "10": 194, "11": 207, "12": 227, "13": 243, "14": 257, "15": 299, "16": 315, "17": 333, "18": 352, "19": 370, "20": 389, "21": 403, "22": 415, "23": 435, "24": 457, "25": 475, "26": 491, "27": 507, "28": 530, "29": 548, "30": 567, "31": 583, "32": 599, "33": 618, "34": 637, "35": 656, "36": 675, "37": 692, "38": 712, "39": 729, "40": 748, "41": 768, "42": 786, "43": 806, "44": 823, "45": 841, "46": 860, "47": 877, "48": 897, "49": 917, "50": 936, "51": 951, "52": 967, "53": 982, "54": 997, "55": 1010, "56": 1025, "57": 1040, "58": 1056}
---

**Dave Jones:** Hi! We love vintage computers here on the EEVblog, but it gets better. This really isn't a vintage computer, but it's a do-it-yourself, TTL-based microcomputer called the Gigatron. And we're going to check it out. We're going to assemble this thing. It is a kit, and look at this.

**Dave Jones:** It's beautiful. All the individual chips soldered onto the board. And yes, there is no microprocessor on this thing. There is simply the ROM. Where's our ROM? Check it out. There it is. We've got a ROM, and we've got a 62256 RAM. Absolute classic, but everything else is TTL.

**Dave Jones:** Oh, I'm going to love building this. So thank you very much, Walter and Marcel, who designed this thing. And look at this comprehensive manual we get with it. I'll link it in down below if you want one of your own. And they've developed this thing from scratch.

**Dave Jones:** Something like that. Talk about the WOS. Famously built the Breakout arcade game with 44 off-the-shelf chips. There's Marcel and Walter. Good on you guys. This is fantastic. I love the manual. Check this out. How to use this manual. Crash course in electronics. How to read your resistor color codes.

**Dave Jones:** How to identify all your symbols and your caps and your ICs and everything else. They've gone to an awful lot of trouble. So this would make an awesome beginner kit. It is so comprehensive. Unbelievable. Like a through-hole soldering beginner's kit. They teach you how to solder and do everything else.

**Dave Jones:** Bend the leads. There you go. I had the old-fashioned squeezy. I've probably still got it somewhere since when I was a kid. The old-fashioned squeezy thing to dill. Squeeze. Dill pin aligner thing. Because when you buy the chips they come with the splayed leads like that.

**Dave Jones:** Now I just roll them on the thing. Hold your tongue at the right angle. Roll it on the bench and she'll be right. But yeah, I had one of those. And here we go. Step by step. Assembly instructions. This is absolutely brilliant. Hats off.

**Dave Jones:** This is one of the most comprehensive instruction assembly guides I've seen. And I believe it is all open source hardware. I don't know about the license for it. But anyway, check it out down below. We've got the full schematics. Fantastic. Oh, is that the original?

**Dave Jones:** Is that the original prototype on breadboard? Oh yes. You win the internet. Fantastic. And then we've got some major... is that wire wrap? That must have been a wire wrap version. Wow. This is great. Look, they've even put in the audio line level stuff.

**Dave Jones:** Interesting. Anyway, simulator. It doesn't get any better. Anyway, let's go build this puppy. I absolutely love the case it comes in. Look at this. Nice... yeah, that's... yeah. It's a nice wooden case. And then we've got the see-through cover on the top, so you can see all the circuitry.

**Dave Jones:** I'm sure it's got some blinky LEDs in there as well. And it even comes with an old school... what is this? One of those Nintendo controller-y things. So we can play games. Yes, because it does have a whole bunch of stuff built in.

**Dave Jones:** So it should just power up and play games. They all should be programmed into the ROM. The operating system, in quote marks, whatever that is, I'm sure they've got detailed info and all that sort of stuff. But basically, we're building a microprocessor just out of 7.4 series logic.

**Dave Jones:** Brilliant. I tell you what, I like the layout too. That's actually quite efficient. You can see, like, mostly vertical routing on the top side here. This is only a double-sided board, so, you know, laying out this one, if you want to task, maybe they've got the...

**Dave Jones:** what did they use, Eagle or something? If they've got the files, try and route something like this yourself. It'd be an interesting exercise in optimization. Most of the routing on the bottom there, that's a very... and the flood field, the rest. Anyway, I like this.

**Dave Jones:** A lot. Let's go build it. So there's our fully built Gigatron TTL microcomputer. Look at it. Isn't it brilliant? I love the case. Fantastic. It took me probably two and a half to three hours to assemble this, but I was actually doing it live with an audience,

**Dave Jones:** so interacting and chatting. It'd probably take you probably under two hours for anyone to solder a board like that. And it went together a treat. No problems at all. So let's apply power to it here. I've plugged in a VGA monitor and the game controller.

**Dave Jones:** And you apply power, and you get some blinkin' lights here. Power LED and scanning back and forth, and what do you know? We're in like Flynn. Check it out. And it's amazing that we can actually get this sort of output with just a couple of handfuls of TTL chips,

**Dave Jones:** some RAM, and some ROM-based instructions to make our own RISC processor. Now, you might notice that there's scan lines missing on here, these black lines. Well, that's actually very deliberate. You can actually get rid of that and make it solid by pressing the Select button like that,

**Dave Jones:** and what that does is actually, because there is no video processing hardware on this thing, there's no hardware to actually generate the video, it's all done in the software via the TTL processor itself, then it's got to take time to generate all this graphics.

**Dave Jones:** And that's the limitation of not having any, well, what we'd call a graphics card these days, but back in the times of the 8-bit computers, you'd have a 6845, for example, which was a graphics controller chip, which would handle the graphics. So by making it solid like that, it actually works slower.

**Dave Jones:** So we'll see that in a minute, but yeah. So it just leaves out a scan line, so during the black periods there where it's not displaying anything, it has more time to do processing of your actual program. And if we want to reset the PC,

**Dave Jones:** we can just hold down Start at any point like that, and it will actually get us back to the screen. So if you're in the middle of the program, you can just exit back at any point. So what we'll do is we'll select some photos here.

**Dave Jones:** So let's go in and select our pictures. There we go, and it's going to start drawing a picture from the right-hand side. But it's going to do it very, very slowly, and it's got 64 colors because it's got two bits per, you can see that on the resistors down there,

**Dave Jones:** it's two bits per red, green, and blue. So four colors, four colors, four colors, 4x4x4 is 64 colors. So that's what gives us our total palette on here. And the screen resolution is 160x120, but that can actually go up to a 160x480, but I'm not sure how it actually does that.

**Dave Jones:** And you'll notice that if we actually press the Select now, it should actually draw that a lot quicker. Look at that, there you go. So that was the difference between having it solid like that and very little time to do the actual processing.

**Dave Jones:** It's prioritizing the video or prioritizing process like that, but it still does a pretty good job like that. See, that's not too shabby at all. The color's actually quite nice. I mean, you stand right back and it looks pretty good. Beautiful, look at that.

**Dave Jones:** Great stuff, a bunch of TTL chips. And this Mandelbrot set is really cool, but you can see it's taking almost 20 minutes in fast mode to actually do that, and I can switch into the slower mode, which fills in the extra scan line there.

**Dave Jones:** Yeah, it's slow, because it's got to run that interpreter on top. And then we've got a racing game if we go in here to Racer, and here we go. Assume we go Start. You can see the difference in the count up there when I select Solid Graphics as opposed to the faster processing.

**Dave Jones:** So we basically just have to keep the car on the track. Come on, you can do it. Press Select. See, it's pretty slow when we go to Solid. And we can play Snake as well, so meh. But unfortunately, that's pretty much where the fun ends

**Dave Jones:** with this Gigatron computer. You can just, yeah, you play some games. Like, it's very impressive, the stuff they've written for this thing to get it working on just a basic bare-bones TTL wrist computer, but the only other option we've got is a loader.

**Dave Jones:** We can't actually, like it doesn't have a basic interpreter or anything else in there, so what it's actually doing at the moment is it's just scanning the game port over here, and you can hook an Arduino microcontroller onto there. I'm not going to go to the trouble to do it,

**Dave Jones:** but apparently an Arduino microcontroller in there, you can bitbang some new, like, some programs in there. It's like you're loading, like, from tape, like old-school cassette tape or something like that. Of course, you would have to actually reprogram the ROM if you wanted them actually built in

**Dave Jones:** and actually save when you turn the power off. So this is like, you know, the old-school tape program from the old microcontrollers, but basically, like, that's it. So it's quite disappointing, and that's basically all you can do with it. Like, you can't hook up a keyboard,

**Dave Jones:** you can't, you know, there's no basic interpreter, there's no even just, like, a ROM, like, a assembly-level monitor or something like that. You basically can't really do anything with it unless you want to hook up an Arduino and dick around that way, and I don't know.

**Dave Jones:** That just takes all the fun out of it. So therein lies the problem. Whilst it does live up to its reputation as a TTL microcomputer, that's basically all you've built is a microcomputer. You haven't, unfortunately, built a personal computer. So if you do want to write your own programs

**Dave Jones:** and upload them via the Arduino serial interface, then you can use what's called the Gigatron Control Language, GCL. It's actually an interpreter. So they effectively have an interpreter running on the CPU, and then it can execute the programs. Of course, just like any sort of basic interpreter,

**Dave Jones:** these are probably going to run pretty darn slow, so it's not like writing in assembly language and executing from the ROM in there. And there's an example program. So they've got their own syntax and everything like that. So if you want to do it,

**Dave Jones:** you've got to learn the Gigatron Control Language. I don't see the point. Like, yeah, it's cute, okay, but, yeah, I don't know. Well, I guess it's fun if you're into that sort of thing. I'm not judging. And if you're wondering why the Mandelbrot was so slow, for example,

**Dave Jones:** well, it's an interpreted GCL program as well. So you can actually just download the source code for that. So there you go. There's the Mandelbrot function for those playing along at home. Go for it. I'm sure you can optimize it. And the other thing, whilst this is probably the best,

**Dave Jones:** if not the best assembly manual I've ever seen, it's fantastic, it's basically all you're doing here is you're building a kit. And that's all the instructions basically do. Yeah, you do get the schematics, of course, and then you get the simulator code, which is very cool

**Dave Jones:** if you want to, you know, run that. But there's basically nothing else that explains, like, yeah, we've got the architecture block diagram, but there's no real, like, detailed tutorial on what you've actually built here, how the computer works, how it corresponds to, you know,

**Dave Jones:** the different circuitry on here, and how the instructions flow and are processed, and how the computer actually works. So it's really, it's just a through-hole assembly kit, and it just happens to be a non-personal computer at the end of it, which is really cool, but yeah,

**Dave Jones:** it's an expensive amount of cool just for a do-it-yourself through-hole kit, basically. And as for the RISC processor itself, well, it really is a reduced instruction set, so much so it's only got eight instructions, and here's the instruction set, and you can't really, you know, there's not much variety in there

**Dave Jones:** to, you know, do creative things and stuff like that. Sure, you can do your Mandelbrot, and you can draw your pictures and do everything else, brute force, but yeah, and it's not, basically not compatible, that I'm aware of, with any other RISC processor that's been produced.

**Dave Jones:** It basically is its own architecture, and it uses its own programming language as well. So I just found this presentation that they did at a conference, and you can watch the actual presentation video online as well. There's the Woz with his Nixie tube watch,

**Dave Jones:** and that's the original Breakout arcade game, just using TTL logic and the Apple One, of course. And there's their original prototypes, and they actually, this is quite good. They actually go through and explain the different sections with the different chips, and the instructions,

**Dave Jones:** and the difference between CISC and RISC, and all that sort of stuff. So this is actually quite detailed. Go in and actually check this out. So they probably should have included something like this in the kit, maybe in a simpler form. This is obviously a technical presentation

**Dave Jones:** to a reasonably technical audience here, but yeah, all this sort of stuff should have been included as educational material in the kit, I think. Anyway, it's just hidden away on the website. And unfortunately, here's the sad news, it's expensive. This thing is 150 euros plus,

**Dave Jones:** unless you're in the Netherlands, is 25 euros or 30 euros postage. So that's equivalent to, at current exchange rate, 210 US dollars delivered, or 280 Australian dollars delivered. Jeez, you can buy like a low-end laptop for that. Sure, you can't assemble it, it's not nearly as much fun,

**Dave Jones:** but ultimately, once you build this, I don't know, it's a struggle to do anything with it, unfortunately. And it's 6.25 megahertz, which it does actually execute one 8-bit instruction every cycle, so it's reasonably powerful in that respect, but the fact that it doesn't have any video or audio processing,

**Dave Jones:** that's all got to be done in the software itself, well, that slows it down drastically. So yeah, it's not exactly a speed deemer. You're not going to be crunching any bitcoin on this anytime soon. So there you have it, that's the Gigatron TTL microcomputer.

**Dave Jones:** Thank you very much, guys, for sending that one in. I did enjoy building this thing and doing it live stream. I'll link in the video at the end of this for the live stream of that. It should be finished processing soon. And you can watch the whole four-hour live build of this thing.

**Dave Jones:** I talk about, you know, various soldering techniques and traps for young players and all sorts of stuff. And no, I didn't follow the assembly manual, I just followed my nose, because I thought the assembly manual was actually, they said do all the capacitors first.

**Dave Jones:** I think that's wrong. Should have done the chips first in terms of height of components off the PCB and things like that. Just little things, but it doesn't really matter. Just nitpicking. Just be aware, if you're getting this thing and you're expecting like a fully-fledged computer,

**Dave Jones:** you can hook a keyboard up to and actually program, nah, it's going to be ultimately a bit disappointing for you. But it was a fun kit to build. So yeah, I think there are quite a few of these kit computers out there these days, aren't they?

**Dave Jones:** They've gone through a bit of a revival in terms of retro, you know, TTL computers and kits and things like that. Somebody's done, yes, I'm aware of the Monster 6502. I'm not sure if you can buy that as a kit, but it's a giant 6502 processor.

**Dave Jones:** Would have been nice to like see some LEDs on here and like you could shift all the data through and use it as like a learning tool to watch data shift through the various registers and stuff like that. And you know, maybe some manual clocking buttons

**Dave Jones:** or something like that to, you know, clock it through. So it's more of an educational tool. At this point, it's basically just a through-hole assembly kit with a fun little, you know, novel little computer at the end of it. So anyway, I hope you enjoyed that video.

**Dave Jones:** If you did, please give it a big thumbs up. As always, comment down below. And if you want one of these Gigatrons, they still do have them available, so I'll link it in down below. Catch you next time. ♪♪
