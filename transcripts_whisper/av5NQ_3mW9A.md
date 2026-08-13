---
video_id: av5NQ_3mW9A
title: EEVblog #32 - Tandy 1000 Retro Computer time!
url: https://www.youtube.com/watch?v=av5NQ_3mW9A
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 21, "2": 38, "3": 56, "4": 82, "5": 109, "6": 127, "7": 139, "8": 161, "9": 202, "10": 227, "11": 252, "12": 268, "13": 287, "14": 307, "15": 322, "16": 333, "17": 352, "18": 371, "19": 389, "20": 412, "21": 437, "22": 451, "23": 474, "24": 489, "25": 507, "26": 531, "27": 552, "28": 571, "29": 584}
---

**Dave Jones:** Hi, I hope you like the new intro. We're up to blog number 32, so I figured I'd make this thing look a bit more professional and do some kind of lame intro like all the other cool blogs have. If it's any good, let me know.

**Dave Jones:** In case you're wondering what that board is, it's a board I designed some time ago. It's a development board. It's got a real expensive top-of-the-line Vertex 5 FPGA on it, a real expensive chip. It's like $800 or something like that. And it's got gigabit Ethernet.

**Dave Jones:** It's got high-speed Rocket IO. It's got SATA. It's got power over Ethernet. And it's a really cool little board. It's quite high-tech. So, that got me to thinking, well, what can I do for this blog? I know, let's go low-tech retro. Look what I found.

**Dave Jones:** My old Tandy 1000 PC. Wow, check it out. Ancient. Absolutely ancient. It's 1984 vintage, I think it is. That's probably before a lot of you guys were even born, before you were itching your daddy's pants. Unbelievable. Cool bit of retro machinery here. And this was my first real computer that I got.

**Dave Jones:** Well, first real one that did any useful work anyway. And it's a classic. It's the original Tandy 1000. It's serial number 5841, so it's one of the first sort of batches. And I thought, wouldn't it be really cool to see if this thing powers up again?

**Dave Jones:** I haven't touched this thing in, oh, I don't know, it's got to be at least 15 years. And check it out, I'm wearing my fire is not an option T-shirt. So, we're going to get this sucker to power up by hook or by crook.

**Dave Jones:** Hopefully, it'll go first go. What are you betting? All right, here we go, the moment of truth. I had to bring it inside and hook it up to the Sony LCD because I don't have the original composite monochrome monitor I had with it anymore.

**Dave Jones:** I tossed that out many years ago. But let's see if this sucker powers up. I've got it plugged into the composite video output and that's it. And it may actually go poof, because the power supply, who knows? It's just been sitting there for 15 years.

**Dave Jones:** So, here we go. Building the suspense, flip the power switch and run for my life. Oh no, no, it doesn't work. Oh, what a loser. Unbelievable. Hit the reset button. Oh, massively disappointing. What a letdown. Unbelievable. All right, after that massive disappointment, I've taken the cover off and we'll inspect this sucker later.

**Dave Jones:** But I just want to see if everything's still in place in there. And it looks like it is. So, I don't know, let's try it again. Maybe it just needed a kick in the pants. Here we go. Got it, got it. There it is.

**Dave Jones:** Copyright 1994 Tandy Corp. All rights reserved. Insert system diskette. We have a winner. It lives. That is just awesome. Wow, obviously the power supply just needed a little bit of a kick in the pants, but yeah, there it is. Bang, 128k. Actually, it should have more than that, because

**Dave Jones:** I believe that's the extra 256k expansion board. So, obviously that's not working. I'm not sure why. That's not the one I originally was using the last time I had it. I actually had a bigger board, which is why I've actually cut the chassis out here.

**Dave Jones:** I actually had a bigger board which came out the front. Because the Tandy 1000, one of its classic problems was that it wasn't a full-length PC. And almost from day one, I don't think I ever put the cover back on this thing. I always

**Dave Jones:** operated it with the cover off. And you can see a couple of my custom mods here. I've got a volume control, which it never had. I've got a mono and colour switch. It's the only Tandy 1000 in the world that actually had a turbo mode, because I designed a custom turbo board for this thing.

**Dave Jones:** And there it is there. If I zoom in on it, you can see it's a little, an old piece of Vero board with the original timing chip here. It's got a new crystal. It's got a couple of other chips, which I'll probably explain later.

**Dave Jones:** And it's designed to plug into the existing socket on there, and it fits between these two boards. So the really cool thing about it is that the boards would still fit in here, and the turbo board just neatly goes in there like that.

**Dave Jones:** And it's got all these wire mods around, as you can see. And I really modified this sucker a lot. I know what you're thinking. This is an electronics engineering video blog. We can't have this episode being some geeky PC retro loving. So let's have a look at some electronics, shall we?

**Dave Jones:** I mentioned before that my Tandy 1000 had a turbo board, which I custom designed. And this was way back in the early days. I had the technical reference manual, and it just wasn't fast enough. It only operated at 4.77 megahertz. And I put in a V20 processor, because back then you could get a V20.

**Dave Jones:** It was a pin compatible processor for the 8088. It sped up your machine, but that wasn't good enough. I wanted a turbo button. All these other machines out there had a turbo button, so I wanted my own. So I designed it. So this is how I did it.

**Dave Jones:** The Tandy 1000 had an 8245A timing chip, and this was specifically designed for sending the required clock signals out to an 8088 processor. Now, I pulled over the data sheets for this thing back in the day, figuring out how I could add a turbo functionality.

**Dave Jones:** And what I found is that it had an internal oscillator, and that wasn't being used. I actually used an external oscillator, and it already had an internal switch to switch between the external clock and this internal oscillator. Aha! Brilliant! Right, but then I found, I read the more, I looked the circuits more in

**Dave Jones:** depth, and I found that the DMA memory processing still required a fixed 4.77 at 33% duty cycle, otherwise it wouldn't work. And I experimented with that, and sure enough, the machine crashed. So I had to generate that signal, regardless of the turbo mode.

**Dave Jones:** And also, the timer chip, the real-time clock, actually required, I think it was a real-time clock, it required a 2.38 MHz. signal fixed. So my turbo board had to come up with both of these signals, regardless of what the actual processor clock speed was.

**Dave Jones:** And what did you do back in the old days? You wanted to design the most elegant, simplistic circuit you could. So I channeled my inner Woz, my inner Wozniak, and I came up with this sucker. And I thought it was very clever at the time.

**Dave Jones:** Well, you know, it's not too bad anyway. I was only young, so you know, I was impressed by it. And what I had was a three-stage shift register with feedback, and that was fed from the existing 14.318 MHz clock. And sure enough, that's a divide by six.

**Dave Jones:** So the output gave me my fixed 2.38 MHz I needed. Great! Okay, but where did this 4.77 at precisely a 33% duty cycle come from? Well, I figured out, I looked at the mappings for this thing, and I figured out that this shifting clock going through

**Dave Jones:** here, this shifting one that was shifting through here, could actually be decoded and give me my required 33% duty cycle. So I figured out that if I tapped it off with an exclusive OR gate, bang! It gave me, I tapped the inner signals, and it would give me this exact signal I needed.

**Dave Jones:** It was elegantly simplistic. It was fantastic. So that went off to a different wire, and then the thing had the building switch, and you flicked the switch, and this was a, I think, I don't know, 20 MHz crystal or something, and bingo! I could turn off and on the turbo mode

**Dave Jones:** here without affecting any of the other signals that the machine needed. And I thought this was the coolest thing ever, and it was one of my first few published circuits I got published, and anyway, I thought it was pretty cool at the time.

**Dave Jones:** Sadly, those days of elegant simplicity in circuit design, they're pretty much gone. There's so much waste these days.
