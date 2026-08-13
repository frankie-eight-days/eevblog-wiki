---
video_id: bTDuOUipjhg
title: EEVblog #8 Part 1 of 2 - Graphical LCD Displays & PIC Micro Demo Boards
url: https://www.youtube.com/watch?v=bTDuOUipjhg
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 19, "2": 40, "3": 70, "4": 86, "5": 110, "6": 125, "7": 146, "8": 168, "9": 186, "10": 204, "11": 227, "12": 255, "13": 270, "14": 290, "15": 312, "16": 332, "17": 346, "18": 362, "19": 381, "20": 398}
---

**Dave Jones:** EEVblog. I'm your host, Dave Jones, and this is episode number 8. I've been playing with a little LCD display recently. It's for a new project I'm working on. It's actually my Mark II microwatch, the Mark II Scientific Calculator watch I've decided to have a go at.

**Dave Jones:** Now, this is a little New Haven 128 by 64 pixel LCD display I'm going to use in the new watch. And I've been trying to get it up and running and I've got a couple of stories to relate. Now, the first story is, do you use serial or do you use a parallel interface?

**Dave Jones:** Now, this little LCD actually is quite cool. It has both an SPI serial interface as well as a more traditional 8-bit parallel interface. Now, an interesting question with this is, do you use serial SPI mode or do you use parallel mode? Now, I started, I wired this up to use parallel mode because I wanted increased transfer speed, which is quite important.

**Dave Jones:** So, I set up my little, I just prototyped this up just so I could use it. It's got a little flat flex cable in there, 0.5 mil pitch. So, it's really quite small and, you know, it's really fiddly, so I wired up a header connector on it.

**Dave Jones:** Now, the really annoying thing about LCD display development is that you don't really get any feedback on where you are in the development cycle. It either works or it doesn't. You either get something on the display or you get nothing. And, of course, you know, Murphy's Law of Development says that when you first write your code and hook it up and fire it up,

**Dave Jones:** it just won't work. You'll get nothing on your display. And, of course, that's what happened to me this time. Now, if you use parallel mode, like I did, and it doesn't work at first, you've got a lot of lines. In this case, I was like, you know, 16 lines.

**Dave Jones:** I had to probe and check and debug to see if it was either a hardware wiring issue or whether or not it was my code. I wrote my own driver for this. Unfortunately, I had left my logic analyzer at work, and so I only had my scope, my two-channel scope, to actually debug this thing with.

**Dave Jones:** And parallel mode, it was really quite annoying trying to debug this with just the two-channel scope. So, in the end, I got really fed up with it. I was following the data sheet. It's really quite comprehensive. There's lots of hoops you've got to jump through with this thing, and I wasn't sure if it was a hardware timing issue

**Dave Jones:** or whether or not I just wasn't feeding it the right codes in my driver. So, in the end, I just went, bugger this, and I rewired it for serial mode. And, sure enough, that was much easier to debug, and I could see it on my screen.

**Dave Jones:** I could see it on my scope that the timing was perfect, and there was nothing wrong with it, and it wasn't a hardware issue. So, it had to be in my driver code. And, sure enough, once I dug deep enough, I eventually found that I was missing one code that I wasn't feeding the screen,

**Dave Jones:** and bingo, it lit up like a Christmas tree as soon as I added that code. So, it really took going to serial mode in order for me to be confident that it wasn't my hardware. It was actually my software. Now, even if I did have my logic analyzer with me, probing 16 channels is just a pain in the butt, and you don't really want that hassle.

**Dave Jones:** So, next time, if you have a choice between serial or parallel mode, and you need to do your development fast with the least amount of hassles, I'd recommend using serial mode. Now, my second issue I had with developing this screen is that I decided to use a microchip, a PIC24F standard development board.

**Dave Jones:** I thought about wiring a chip directly up on my board and controlling the display that way, but I was feeling a bit lazy, and I had this thing lying around, I haven't used it before, so I thought, oh yeah, I'll just use this, and it'll shorten my development cycle.

**Dave Jones:** Wah, not wrong. I had issues with this, it was a real pain in the butt. Now, this one is a PIC24F starter board, and on the back here, it's got really nice silkscreen labels of all of the pins on the header connector here.

**Dave Jones:** They're all labeled, you know, RB0, RB1, and I thought, great, I don't need to read the documentation for this, it's already there for me. So I hooked it up, and lo and behold, it didn't work. The reason it didn't work is because even though the pins are labeled right, they actually share functions which aren't labeled on here.

**Dave Jones:** So some of the IO pins on this header connector I was using are actually shared with the debug lines, and they're actually connected to other things on the board, and it was really annoying when I hooked my scope up, and I found that my signal was shorted to something else.

**Dave Jones:** And that's why I was having so many problems. So it was a double whammy, I was having software issues and these hardware issues, because I didn't look at the schematic for this board before I used it. Yeah, I know, it's my own stupid fault.

**Dave Jones:** I should have checked the schematic first before using this thing and trusting that the outputs were exactly as labeled. But, you know, I was feeling a bit confident in it, and I thought I'd give it a go, and it just came back to bite me.

**Dave Jones:** Really annoying. So next time you're using these development boards, check out the schematic first to make sure the pins aren't being used for something else as well. Now I'm probably exaggerating about all the problems I had getting this LCD to talk, because all these issues were only over the span of a couple of hours.

**Dave Jones:** It's not like it took me days or weeks or anything like that to figure it all out. But really, sometimes you've only got... I've worked on projects at work where I've only had hours to get something up and running, and you just don't need these sort of hassles.

**Dave Jones:** So, you know, just be wary of it next time.
