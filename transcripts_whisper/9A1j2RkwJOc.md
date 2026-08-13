---
video_id: 9A1j2RkwJOc
title: EEVblog #12 Part 1 of 2 - Shanghai Special - PCB Assembly Factory Tour
url: https://www.youtube.com/watch?v=9A1j2RkwJOc
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 22, "2": 44, "3": 67, "4": 97, "5": 148, "6": 204, "7": 224, "8": 264, "9": 286, "10": 335, "11": 355, "12": 373, "13": 389, "14": 404, "15": 424, "16": 441, "17": 460, "18": 481, "19": 502, "20": 519, "21": 544, "22": 564, "23": 586}
---

**Dave Jones:** Hi, welcome to the EEVblog. I'm your host, Dave Jones, and this is episode number 12. I just got back from a rather interesting trip to Shanghai in China, of all places. And I was there for work and I visited a rather typical surface mount and through-hole PCB assembly factory.

**Dave Jones:** And I thought it'd make a real interesting blog entry for those who haven't seen what happens inside one of these PCB assembly factories. So, here it goes. This week it's the Shanghai special. The first thing I'm going to show you is a guided trip of a typical surface mount assembly line.

**Dave Jones:** Where your blank boards go in one end and, bingo, out pops a magically soldered, fully assembled board at the other end. So, here it goes. Okay, we're on the surface mount soldering line here and I'll take you through all the different items. This is the solder paste dispensing machine where they put the stainless steel stencil in there.

**Dave Jones:** And it applies the solder paste and they have a little conveyor belt in there which then takes it out of here once the solder paste is applied. It comes out to a vision inspection system. Ah, well, it's not an automated vision inspection system.

**Dave Jones:** They've got those somewhere else. But that's a manual. Then it comes into the first pick-and-place machine. And you'll notice I'm wearing a daggy anti-static cap and a coat and anti-static shoes. And this is a pick-and-place. This is the first pick-and-place machine. This is the first pick-and-place machine.

**Dave Jones:** And just in case they can't fit the number of reels, then it'll go into the second pick-and-place machine. And then just in case they still, your board's got too many components, it'll go into the third pick-and-place machine. And then it'll pop out another, just a manual visual inspection.

**Dave Jones:** And then it goes into the reflow soldering oven. And you'll see the thermal profile here. Each board will have a different thermal profile set. So this one is, I'm not sure if this is actually for our board, but our board will have its own individual thermal profile.

**Dave Jones:** And then magic happens in the reflow soldering machine and it pops out the other end. Just grab that and it comes out on the conveyor at the other end. And bingo, you've got a soldered board. Now after the board comes out of the reflow oven, it actually usually goes to an automated visual inspection system.

**Dave Jones:** Now these things are really cool. They actually take the assembled board and they compare it against a reference board, a golden board. And they check for missing components and the camera zooms around and it actually inspects each component on the board and compares it with a library reference it's had stored in there.

**Dave Jones:** So it's a really good indication of whether or not a board is actually assembled correctly. And this is how it works. Now that's the line for the surface mount assembly system, but they've also got a typical old fashioned through hole wave soldering machine.

**Dave Jones:** And I'll take you on a short guided tour of that line as well. Here we go. Okay, so here we are. We're on the DIP through hole assembly system. Now these girls are sitting at a bunch of benches with, as you can see, bins containing the through hole components.

**Dave Jones:** And they're each dedicated to a task of inserting a particular bunch of components. Now the components do move automatically along a conveyor belt, or they can, but in this case they're manually pushed until they get into the machine here where they do actually automatically go in.

**Dave Jones:** And you can see a couple of boards automatically being fed into the machine there. That's a look back along the line. As you can see they're all ESD set up with their wrist straps. Now this is the control software for the actual machine.

**Dave Jones:** And it's a lead free system as you can see there. It's actually a Sun East brand machine. Now let's take a look inside where the magic happens. This is the solder bath as you can see here. It'll come clearer in a second as I've lifted the lid on it.

**Dave Jones:** Now this is actually quite dangerous because the solder can actually splash. But you can see the board going over the solder wave here and that solders all of the through hole components. Now as you can see the board actually contains a mixture of previously assembled surface mount parts.

**Dave Jones:** So you do the surface mount parts first and then you put it through the through hole wave system. Now there's a board actually emerging. That's a completely soldered board. And then it goes down the conveyor belt here and along the next assembly bench which we see here.

**Dave Jones:** There's more components and these are mainly either hand assembled components or their connectors or some other system which are hand assembled. And it actually goes along an automatic conveyor belt there which is quite slow. Now this is the automatic bed of nails tester.

**Dave Jones:** It's fully custom and set up for this individual board. And as you can see it's a very quick test. And it's fully automated and the board is passed and it goes into final inspection here. As you can see the girl is actually inspecting the board for any missing components and things like that.

**Dave Jones:** And you can see the reference template she's got there which compares the colour of connectors. Now that's quite a neat system to ensure easy visual identification. So that's it. That's the DIP assembly line. Okay, now what we're actually taking a look at is an x-ray machine.

**Dave Jones:** We're taking an x-ray of a 676 pin BGA device as you can see on the board in there. And the x-ray machine is actually really quite neat. You can pan and zoom around in real time and you can see it fade in and out there.

**Dave Jones:** Now the idea is to actually fade the image in and out and look for any shorts between the balls and any sort of discrepancy in the colour between the balls which could indicate a dry joint. Now we actually, this is an FPGA on one of our boards which we had a problem with.

**Dave Jones:** Here you can actually see an SD card. That shadow outlined which they're pointing out now is actually an SD card on the opposite side of the board. Now it's a really neat system. And now we didn't actually find any fault with the actual BGA on the x-ray machine

**Dave Jones:** but it turned out when you apply actual pressure, physical pressure to the BGA it did actually have a dry joint. So these x-ray systems are not infallible but they're a really neat tool and most good assembly houses will have one. I hope you enjoyed that short tour of a typical PCB assembly factory in China.

**Dave Jones:** So let's go on to something else shall we, something that ticks me off again.
