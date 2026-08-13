---
video_id: WI4xIJFl6to
title: EEVblog #120 - Renesas Devcon Day 4
url: https://www.youtube.com/watch?v=WI4xIJFl6to
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 38, "2": 57, "3": 73, "4": 95, "5": 108, "6": 122, "7": 151, "8": 168, "9": 184, "10": 196, "11": 208, "12": 225, "13": 239, "14": 260, "15": 277, "16": 291, "17": 307, "18": 327, "19": 341, "20": 357, "21": 378, "22": 397, "23": 419, "24": 438, "25": 458, "26": 492, "27": 519, "28": 535, "29": 557, "30": 572, "31": 591, "32": 612, "33": 631, "34": 651}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. It never ends. Back into it. There's Nicole! It's Thursday morning, the conference has kind of, sorta, officially ended, but there's still dozens and dozens of labs and lectures until about midday.

**Dave Jones:** This is the morning networking breakfast, so I'm going to go network and then maybe check out another lab or two and that'll be it. It'll be winding down, so let's go. And the labs are still going, it looks like. They're playing with the new RX board.

**Dave Jones:** How's the RX board going, guys? Oh, it's very fast. Very fast? Yeah, faster than we expected. Well said. Nah, it is a brilliant, it really looks like a brilliant board. And you just start mucking around with the Hue, are you? Yeah. With the development environment?

**Dave Jones:** Yeah, we're trying different options for performance measurement and getting it, each time it's a little bit faster. Fantastic. I found someone just hanging out in the lobby after one of the lectures. How you doing? Doing fine, thanks. Excellent. Who are you? My name is Alex Dean and I'm an associate professor at North Carolina State University.

**Dave Jones:** I teach classes with Renesas processors and I do research with them, too. Fantastic. How are you enjoying the conference? Oh, it's lots of fun. I'm getting a lot of good ideas. Excellent. And have you scored one of the new free RX kits yet?

**Dave Jones:** No, they ran out. They ran out? Completely ran out? It's that popular? It is, that's right. It does look pretty good. Yeah, I can't wait to play with it. Excellent. It looks nice and fast. I'll have to get one first. So you actually teach Renesas products in class?

**Dave Jones:** Yeah, we teach a couple of embedded systems courses, introductory and grad level and they both use M16C. Fantastic. And this is the same course material that Jim Conrad has been using as well. So Brian, what happened the other night? I heard you won the Wii at the conference.

**Dave Jones:** I did, but there's a story behind it. So I won the Wii, but actually I need to give it to somebody to keep good karma. Basically, I met a guy at dinner from Synopsys and we were talking to their dinner and then we got our tickets for the casino night.

**Dave Jones:** So we go and we play roulette. And we were just winning, winning, winning, winning. He ended up winning $20,000 and I won $14,000. So between the two of us, we have 34 tickets. And basically, he wasn't going to be here during the dinner, so he gave me the tickets and said, hey, just go ahead and if you win.

**Dave Jones:** And then we ended up playing Wii Bowling and he never played Wii Bowling before. So I said, you know what, I'm going to put all these in the Wii box and if I win the Wii, I'll send it to you. So I won the Wii.

**Dave Jones:** I won the Wii. Actually, one of the Renesas guys is going to take it with him back to the Bay Area and give it to the guy. Fantastic. It's good karma, right? It's good karma. It'll come back. Want to score one of the new free RX?

**Dave Jones:** Not yet. I need one. I heard they ran out. It's that comfortable. I've got contacts. I can get one. Good. Well, yeah, because he is... There he is, the designer. The only time you've seen me without a beer in my hand. Right. I can attest to that.

**Dave Jones:** Actually, I don't know if you noticed, but Kent started a new company. It's Kent Loman and Associates. Well, that's the other thing I didn't notice the whole festival is my badge is wrong. It's like my name is my company name and never even noticed.

**Dave Jones:** We decided that I am ubiquitous. So it's now Kent Loman Industries. And Associates. And Associates. And I'm pretty sure I'm just going to shorten it to Kent because, you know, if you're really big, you don't need two names. Bono, Madonna, Kent. But I'm sure you can't buy Kent.com, right?

**Dave Jones:** So you're screwed. You can't get the .com domain name. Without it, I'm nothing. Yeah, it's all over. It's all about Google ranking, right? It is. Good conference, though. I'll tell you, these guys really went all out. Here with Marcella. And she's headed off.

**Dave Jones:** How was the conference? It was a fabulous conference. And I'm headed back to Michigan today. So I'm hoping to work a lot more with Renesas over the years to come. And I enjoyed your presentation last night. It was great. Thank you very much.

**Dave Jones:** Did you have one of the presenters? I did yesterday. I talked about my hardware in the loop system. What is it? Hardware in the loop. Oh, hardware in the loop. I'm from Boston, so I often drop my R's. Right, okay. Well, I sleep with my R's.

**Dave Jones:** So you should. Tell us about that. So the hardware in the loop allows you to test your control systems without having the plant. We call the plant, which is essentially the vehicle or the medical system, whatever you're going to be controlling. You don't have to have the real one.

**Dave Jones:** We do deterministic hardware in the loop testing, and it allows you to run it as though it's in the vehicle that it will be in eventually. So it's great business and a lot of fun. Here with Cindy from Total Phase. How was the conference?

**Dave Jones:** It was a great show. I really enjoyed it. It was really well organized. I was very impressed by the level of effort and time that people really obviously put into the conference. Were you the only female here? I was almost. Almost? Maybe there were four other ones in the room.

**Dave Jones:** Overwhelmed? Ah, it was great. By the amount of nerdity here? No, it was inspiring. Edit in. Well, it's all over. That's Renesas DEVCON. I've got to say, I am massively impressed. I went into this thinking, you know, it's going to be a bit lame.

**Dave Jones:** As most of these conferences are, I've been to quite a few of them, and this one was far from it. The best put together conference I've ever been to. Unbelievable. The amount of effort and the lectures were out of this world. Outstanding quality lectures and hardware labs.

**Dave Jones:** Thoroughly well put together. And the Renesas products actually look really good. The new RX devices. I'm surprised. Hardly anyone's ever heard of Renesas. But hey, you know, number three semiconductor in the world. Number one in micros. Jeez, nobody knows about it. Tell you what, they will after this, I think.

**Dave Jones:** They're dismantling the sign. There it goes in the entry for you. DEVCON's over. I almost forgot. You know what we say here on the EEVblog. Don't turn it on. Take it apart. Let's crack open the Pokin. Here it is. Little USB Pokin tag.

**Dave Jones:** And let's crack it open. Now, kiddies, let me tell you, if you go into one of these conferences, always bring your tools. Okay? Get your, you should have a knife. A Swiss Army knife. A multimeter. Got my little pocket multimeter. No worries. And we're going to crack this sucker open and see what's inside.

**Dave Jones:** Here we go. Now, it's supposedly got an RFID tag or something like that in it. So it looks like you can actually get in here. And with a knife. And actually. There we go. There we go. It's popping open. No problems. Piece of cake.

**Dave Jones:** There we go. Ta-da. There's the Pokin. That's what's inside. Little lithium coin cell battery. No surprise there. That's a CR1632. And let's take a look at the board. As you'd expect, it's just a, um, as you'd expect, it's just a single, um, a single board solution with the contacts directly on the board.

**Dave Jones:** That's very common. This is actually a button on the front. It's actually an LED and a button. So, um, now I know. We've got some heat stakes. Check out the little heat stakes here. So I have to shave those off. Okay, I've shaved the heat stakes off that.

**Dave Jones:** And let's take a look inside, shall we? Ta-da. There it is. That's inside the Pokin. Check it out. There's the inductive loop coil. It's actually, it's probably not, it's not an RFID tag. It looks like it's just a close proximity inductive loop of some kind.

**Dave Jones:** So they must, um, that's why they only work when they get within sight a certain coupling range on that face. They, if you put them back to back, they wouldn't actually work. So you had to put them face to face. And that's why, because they're, they work on an inductive coupling loop.

**Dave Jones:** So, obviously, uh, the battery must, um, pulse this loop like once per second or something like that. Very quick, uh, fast pulse into that just to detect other, um, other devices which are close. It just continuously detects whether or not a device is there.

**Dave Jones:** Now, let's take a look at the, uh, uh, microcontroller. Let's hope it's a Renesas part. It could very well be, be in the number one microcontroller manufacturer in the world. Let me have a close look at that. It's a HA1561. I don't recognize it, and the symbol is a bit, bit hard to see.

**Dave Jones:** Um, motor, uh, HA, that could be like an old Mitsubishi, um, one, which is now a Renesas, of course. But, um, yeah, I, I don't recognize it off the top of my head. So there you go, a HA1561 micro. And it's just a couple of passive, there's some LEDs in there,

**Dave Jones:** a couple of other passive parts. But it looks like it's not, um, not your traditional RFID, uh, tag. It's, you know, it's, it's effectively the same system. It's a, it's a coiled loop with a, with a little, uh, micro in there. But, um, it, it doesn't use an off-the-shelf RFID solution.

**Dave Jones:** It's just a completely, um, uh, custom, uh, loop with a, with a, with a micro hanging off it. Nothing too exciting, exactly what I expected, really. It's been one hell of a conference, but time to head out of here. See ya! Almost forgot the video camera!
