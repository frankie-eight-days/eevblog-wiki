---
video_id: NCeSgpPWnsc
title: EEVblog #11 Part 2 of 2 - More on DIY product design
url: https://www.youtube.com/watch?v=NCeSgpPWnsc
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 21, "2": 44, "3": 70, "4": 89, "5": 108, "6": 136, "7": 154, "8": 170, "9": 187, "10": 206, "11": 220, "12": 238, "13": 254, "14": 271, "15": 290, "16": 309, "17": 331, "18": 349, "19": 367, "20": 383}
---

**Dave Jones:** Now, because this was a low-cost, do-it-yourself type project, I didn't want to limit my board to the requirement of a professional pick-and-place machine. But that's, as I found out, that's what you really need if you use surface mount switches, because they all have to be lined up perfectly.

**Dave Jones:** There's nothing worse than having keys that are misaligned and they won't protrude through your front panel and things like that. So, really, surface mount switches, you can't really assemble them yourself and get a really accurate alignment. It's a pain in the butt, and if you space them close together too, you just don't have room to physically get your soldering iron in there.

**Dave Jones:** So, surface mount switches didn't really work for a practical do-it-yourself application. So, I decided to go to through-hole switches, and I got these little tact switches, which are really cool. They've got a nice profile, a 6mm by 3.5mm profile, and they've got a nice, soft, tactile click that you can actually press with your finger.

**Dave Jones:** And, really, there were only one or two choices on the market when it came down to it. You go to the catalogue, you go to Digi-Key or something, and there's 10,000 tact switches to choose from. But, in the end, you whittle down your design criteria, and really, in the end, there's only one or two practical choices.

**Dave Jones:** It really is quite amazing. So, I changed the board to through-hole. This one uses the through-hole switches, and that means that you can actually hand-assemble these. And you can put them on, and the holes in the board line up the switches for you.

**Dave Jones:** So, you can do a hand-solder job, and really get a nice, professional finish with nicely spaced keys, and it all works really well. The only disadvantage to through-hole, of course, is that you lose surface area on both sides of your board. So, I had to scrap my idea of using a surface-mount battery holder on the bottom of the board, because I didn't have room anymore.

**Dave Jones:** So, that pushed me in the area of having a battery that was mounted off the board. So, now that I had a battery that was mounted off the board, on free wires, really, that meant that I had to have some sort of case.

**Dave Jones:** So, I had to reinvestigate the case, and I got the idea of, well, you know, instead of having a full case, a full custom case, why don't I just have a little case for the bottom? So, I went through the standard catalogs, and I found a little Serpac brand case.

**Dave Jones:** And I, you know, it comes with a top half, but I didn't need that. I just used the bottom half, and it just so happened to be, I found one that was the perfect inside depth, and dimensions that I could mount a coin cell battery holder, or in this case, two coin cell battery holders.

**Dave Jones:** And then there were more trade-offs with the case as well, because you have to secure the case to the watch somehow. And this one happened to have a screw hole in the center, which was really handy. So, that meant that I could put a hole in the center of my board, here, and line it up.

**Dave Jones:** And I could put the board on the bottom, and I could glue a nut on the top, and then a single screw in the back, and bingo, the case holds on. So, I've got a little battery holder, sort of a, you know, a semi-custom battery holder,

**Dave Jones:** that uses all off-the-shelf parts, and it was really quite a nice solution. Now, the next problem I had to solve is, I've got a keypad, okay, no worries. But what do I do for a front panel? And I went through all sorts of designs and things, and I thought I'd use, like, a membrane overlay,

**Dave Jones:** or something like that, a printed overlay. And then I thought, oh no, it's, you know, this is a do-it-yourself, simple type project. Sort of, you know, using off-the-shelf stuff. If I used a custom, you know, plastic overlay or something like that, it was a bit of a cop-out.

**Dave Jones:** And because the watch wasn't in a case, there was really no way to actually mount that. So, I went back to an idea I've used many times in the past, because I'm, you know, I'm an actual PCB designer, and, you know, I know how to design boards,

**Dave Jones:** and boards are real easy and cheap to get custom made. So I thought, why not do a front overlay, a front keypad overlay, using a PCB. And that turned out to be fantastic. Because I was familiar with PCB design tools, this is, you know, this is a piece of cake.

**Dave Jones:** I thought, I'll lash this up in five minutes. And you can have a professionally produced front panel, made out of FR4 fiberglass, and you can get these made cheap and simple. And you can get a range of colors. I could have had, you know, a green, or a blue, or a red, or, you know,

**Dave Jones:** but I chose black, because it matched the rest of the watch. So I got a black gloss solder mask, and white silkscreen, of course, and, yeah, it worked out really well. And because the keys were actually, they only had a very limited height on the actual key switch,

**Dave Jones:** I had to make it as thin as possible. So I used a 0.5 millimeter PCB, it's really thin, and that just slips straight over there like that, and you can still push the button through there. And, you know, that's what it turned out like.

**Dave Jones:** Okay, so I've got my LCD, I've got my PCB, I've got my watch band attachment idea, I've got my key switches, I've got my keypad overlay, and what happens when you put all those together? Oh, and I've got my battery compartment with my bottom case.

**Dave Jones:** You put all those things together, and what do you get? You get, bingo, it magically pops out the end, a scientific calculator watch, the world's first. And really, it's, you know, it was a piece of cake. So in the end, there wasn't really anything, you know,

**Dave Jones:** magical or, you know, fantastically innovative about this, it just used a bunch of practical techniques that really led one to the other, and, you know, it started out with an idea, and it just popped out the other end.
