---
video_id: CqDUjskHIXc
title: EEVblog #155 - ITead Studio PCB Prototype Goof
url: https://www.youtube.com/watch?v=CqDUjskHIXc
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 19, "2": 48, "3": 59, "4": 81, "5": 97, "6": 107, "7": 135, "8": 151, "9": 170, "10": 189, "11": 207, "12": 227, "13": 249, "14": 268, "15": 290, "16": 304, "17": 320, "18": 337, "19": 357, "20": 380, "21": 402, "22": 417, "23": 434, "24": 449, "25": 473, "26": 486, "27": 506, "28": 523, "29": 537, "30": 550, "31": 578, "32": 588, "33": 608, "34": 631, "35": 644, "36": 667, "37": 678, "38": 695, "39": 717, "40": 743, "41": 762, "42": 781, "43": 799, "44": 818, "45": 837, "46": 853, "47": 873, "48": 888, "49": 899, "50": 922, "51": 939, "52": 958, "53": 977, "54": 996, "55": 1015}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, the other day on the Amp Hour, I mentioned these little prototype PCBs I got from a company called ITEAD Studios,

**Dave Jones:** I-T-E-A-D-Studio.com, and how I thought they were a real great value for money and almost game-changing. I was raving on about them. A 32mm x 32mm PCB, double-sided, solder mask both sides, silk screen both sides, plated through holes, 6-6 thou design rules, nice boards, and I got 10 of them for 16 Australian dollars delivered.

**Dave Jones:** You've got to be kidding me! I thought this was the greatest thing since sliced bread. Awesome! But, and I, and I tweeted that, oh, you know, they're pretty darn good value. A few little minor alignment issues with them, but not a big deal.

**Dave Jones:** Man, thought I'd struck gold with these things. And I posted a photo, and well, turns out I was a bit off the mark, because I had only given these a cursory glance before I started raving on about them. So, I went and built one up today,

**Dave Jones:** soldered on the components, powered it up, and it didn't work. And well, you know, Murphy's right, happens every time. Circuit never works first go, great, I get to do some troubleshooting, so let's go for it. And, well, no, I went through all the problems, and it turned out to be a

**Dave Jones:** problem with the PCB manufacturer. Let's take a look at it. So, let's go through the problem, shall we? I've got a little block diagram of the system that I was trying to get working. This is the PCB, this is my new little prototype circuit.

**Dave Jones:** It doesn't matter what it does, totally irrelevant, okay? But it's got a little AVR 80 mega micro on it, okay? And it's got a RS-232 type UART type interface, which goes to one of these little external FTDI, just, you know, I've got one of these SparkFun serial UART interface boards, right?

**Dave Jones:** Really quite neat, hooked up to the USB to the PC, and it's supposed to talk through to the AVR. And I was able to program, okay? I was able to program my AVR, okay, using the onboard in-circuit serial programming header, not a problem, okay?

**Dave Jones:** So everything was looking quite sweet, and I was quite happy with it, but it just wouldn't talk to the PC. And, oh, you know, I was scratching my head thinking, oh, I've screwed something up, maybe I've swapped the RX and the TX. Classic design mistake, which I still make these days.

**Dave Jones:** I still goof it up. Murphy gets me every time, but I double-checked, triple-checked, it wasn't that. And I started to look at, you know, the usual problems, oh, shorts on the board, you know, components in backwards, you know, incorrect components, whatever. I went through all that, not a problem at all.

**Dave Jones:** So I'd gone through pretty much everything I could without actually getting the scope out, and actually probing around. So that's what I did. I went and got my scope, it was just a little standard bench scope down here, and I hooked it up

**Dave Jones:** to a ground here. The board's got, like, another little pin interface on the side of it, like that. So I hooked that, that was rather convenient. So I hooked the oscilloscope probe, the ground point, up to the ground there, and I started probing around, but I didn't have to probe around very long

**Dave Jones:** because the thing just magically started to work. And then I went, oh, I know what that is, instantly. I knew it, I've seen it dozens of times before. It's a classic ground path problem, because once you hook an oscilloscope, well, there can be two things that happen when you hook up an oscilloscope,

**Dave Jones:** and your circuit suddenly magically works. Either, A, it's a ground problem because you hooked up the ground lead on there, and you've got some ground system thing happening, or it's actually loading, either capacitive or resistive loading, but usually capacitive loading on the point that

**Dave Jones:** you're actually measuring. But I knew it wasn't the latter. It wasn't the loading of any point that I was actually measuring. It was the ground problem. And that's just a classic error that I've seen time and time again. And I knew instantly that the ground pin between the FTDI UART interface here

**Dave Jones:** and this one over here was broken. Oh, and by the way, this board, this FTDI board, was actually supplying the plus 5 volts for this board under test, because the board didn't, you know, it doesn't consume much at all. So I was able to power it from the 5 volt interface directly on there.

**Dave Jones:** And one of the things I did when I was troubleshooting this thing, before I hooked up the oscilloscope, of course, I measured that I was getting 5 volts there, and I was, and I measured it directly on the pins, and it was no problem at all.

**Dave Jones:** But I didn't think to actually probe any other point. So I knew this was one of those classic system ground problems, because I didn't even have to, uh, probe the circuit at all. All I had to do was hook up the ground on there, and all of a sudden it started

**Dave Jones:** working. It talked, no problems at all. I was talking to my AVR from the PC, excellent, not a problem. Take the ground, the oscilloscope ground clip off this pin here, take it off, and it stops working. It just dies. So I knew I didn't have connectivity on the board between this ground point coming in

**Dave Jones:** here and this one over here, because an oscilloscope is actually grounded like that. A bench oscilloscope, okay, is, unless you've got one of those, uh, fancy isolated ones, uh, you know, Tektronix and many other ones, or you're using an isolated probe, the BNC connector on your, the BNC input connector on your

**Dave Jones:** oscilloscope is actually connected through to mains, um, earth. That's, that's a ground symbol. I should probably do the, uh, earth symbol like that. And because I had it hooked up to a PC, as in a desktop PC, they also are mains, earth, and the USB connector, and the other connectors on there,

**Dave Jones:** the shell of that, and the ground, and the circuit ground inside the PC, is connected to mains, uh, earth as well. So instantly, you've got that connection going back through your power point, through to your power board, and coming back in, if you've got them on different circuits,

**Dave Jones:** it might actually go all the way, you know, if you've got a house here, draw a little chimney on that, it's not a very good house, but anyway, it can go all the way through your house, but it will eventually join back down to your, uh, common earth point down here, but they will actually

**Dave Jones:** connect up like that, and that provided the, uh, ground path needed to complete the circuit, and that's why it instantly started to work. The signal integrity is going to be complete and out of crap, because it's got to go all the way through your power board and back out.

**Dave Jones:** It's going to be awful, but because this isn't, you know, UART interface isn't particularly high speed, it was able to work no problems at all. So I was asking myself, how could this be? Because I know I did a DRC, a design rule check, on this board before I sent it out, and there were no breaks

**Dave Jones:** in the ground at all, so I knew I hadn't goofed up my PCB layout, I knew I didn't even have to go back and check that, because, you know, DRC, it, you know, you rely on it, and it works, okay? So I knew

**Dave Jones:** they were connected, so I thought, there must be a PCB manufacturing issue, and I thought, okay, one of the V's is, you know, has got a problem, and it didn't connect through, okay, it happens. Now, it's one interesting thing to note here, is that I was using a desktop PC, which is, uh, they're

**Dave Jones:** all mains earth reference, but if I was using my notebook, notebook, uh, PC, then it wouldn't have shown up instantly when I connected the ground probe over here, because notebooks aren't mains earth reference. They're powered from isolated plug packs, and if you're powering them from batteries,

**Dave Jones:** uh, as well, then it's going to be absolutely, completely isolated, no doubt about it. So it wouldn't have shown up, like that eureka moment, as soon as I connect up the, uh, ground point, I wouldn't have seen, I would have had to start probing around more, and, you know, it just would

**Dave Jones:** have led to some weird effects that, uh, weren't instantly recognizable when I hooked, when I actually completed the ground here with this circular, uh, system ground loop. So, just something to watch out for. It's always a trap with young players. Don't ever forget to check your grounds.

**Dave Jones:** I decided to put the board under the microscope, and here's what I found. So here's a microscope photo of the actual IT board that I got delivered down the bottom here, and on the top is exactly the same part of the board in the original Gerber file that I actually sent, uh, to them to manufacture the

**Dave Jones:** board. Now normally, they would take that Gerber file, and they wouldn't alter it at all, assuming unless there's something wrong with it, they wouldn't touch it. They would just use that to manufacture the board. Now, um, just some basics about, uh, Gerbers like this.

**Dave Jones:** You'll notice that there's no holes up here in, inside the actual pad like that. Now that's, uh, that's common. You will not find holes in the Gerber files themselves, because they're specified in a separate NC drill file. That's why this, uh, via over here like this, um, is not, you know, you can't actually see it up there.

**Dave Jones:** It's not that it wasn't in the Gerber file, it's just that it's specified, uh, in the NC drill file instead. Now, uh, now the real problem here, okay, as you can see, there is, uh, copper in, in my Gerber file. There's copper going

**Dave Jones:** between these pads. This is what's called a flood fill. I've, it's, it's actually connected to ground, and I've flood filled all of my board with this, uh, grounded copper, and it snakes its way through all these pads, and up through the vias, and all over the board, okay.

**Dave Jones:** And that helps, um, actually get the ground connectivity on the board, because, um, now this ground point down here, okay, this one down here is actually the one that I hooked at my, hooked my oscilloscope probe up to, and that I mentioned, okay.

**Dave Jones:** And as you can see, it does go through, it is plated through, and goes through to the other side, same with this one next to it. But, uh, because this board's particularly, uh, dense on the other side, it's very densely routed, there wasn't room to actually connect that ground through to somewhere else.

**Dave Jones:** So I've actually got to rely on the fact that, um, I'm using the flood fill. It's got to go around here like this, it's got to go up, it's got to go through here, and up through this little narrow part here, around here, and through this, uh, via here, onto the other side, and then to the rest of my circuit.

**Dave Jones:** Now, um, so I'm pretty much reliant upon this part actually going through here, and this part going through here. Now, um, I've, this, the amount of copper going between these pads is actually quite large, it's actually, um, 8 thou, which is quite, quite a wide amount of copper.

**Dave Jones:** Now, the, um, because that's what, 8 thou is what was left over after I used the IT Studio, uh, design rules, which were 6-6, which means that, um, I can do a 6 thou trace and a 6 thou space. Now, this trace down here is actually 6 thou

**Dave Jones:** wide, as you can see, and they've produced it, they haven't touched it at all. And the clearance around the pads here is also 6 thou, so I met the design rules, so they shouldn't have to touch this, uh, copper at all. They shouldn't have to alter the Gerber files in any way, they should just

**Dave Jones:** actually produce the mask and, and produce the board, and that's it. But somebody at IT has decided, no, we're going to take, um, all of the ground plane and we're going to expand it. We're going to expand the, uh, you know, this, the spacing around between the, um, pad or the via and the ground

**Dave Jones:** plane isn't enough, we're going to expand it even further. And look, down the bottom here, look at this, you can see this, and there's actually a break in the copper there, and it's left what's called, uh, dead copper. So that this is, here is an example of dead copper, okay, it goes through like this,

**Dave Jones:** and it's just floating. Now, um, it's not connected to any other part of the circuit, that's why they call it dead copper. Now, you know, that's not usually a big deal unless you're talking really critical, um, circuit design. Uh, but in this case, I was reliant upon my ground going from my ground

**Dave Jones:** in all the way through here, up through here, up in, into this, uh, via up here. But look, right, there, here's the break, there it is, right there, and that is what, uh, stopped my circuit from working, because there was no electrical connection between the input, this is my UART,

**Dave Jones:** um, input here, the, the ground and the five volts and, and the transmit and receive come through here, and it, and the ground, the, the five volts and the transmit and receive went through to the rest of the circuit, but the, but the ground didn't, because there's a huge break down here.

**Dave Jones:** Now, why they've done that, why they've decided to expand that, um, copper around the pads and the vias, I have no idea, it's crazy. Anyway, they decided to do it, and it screwed up my ground plane. Now, um, my ground, uh, connection. Now, if these pads down the bottom here, if they actually

**Dave Jones:** connected through to ground on the other side and was routed off somebody else, somewhere else, I might not have noticed, um, that, you know, a problem at all, it would have just worked, and unless I went through and actually visually inspected it, I wouldn't have known

**Dave Jones:** that there was this break here and there was this, uh, large, um, clearance around the pads. Ah, it's just crazy. It's something to watch out for, and, um, yeah, I didn't do a thorough inspection of these boards before I assembled them, just gave them a quick glance, and they look pretty good.

**Dave Jones:** I think I was, uh, carried away by the super low cost of these at $1.60 each, including tooling, which is incredible. I got carried away and, well, I didn't look at this, and there and up. But it's a major, major problem, which can cause real headaches and screw up your design completely.

**Dave Jones:** Even if these, uh, pads down here were connected on the other side, there could have been a reason that I wanted the, uh, current going through this way as well, and then you can get all sorts of, um, subtle ground problems if only, you know, if the current's not going where you expect it

**Dave Jones:** on the board or it's being routed somewhere else. So, definitely something to watch out for, A, when you're laying out boards, and B, when you're getting them manufactured like this. So, there you have it. The problem was with these IT Studio boards. Someone there decided

**Dave Jones:** to modify my Gerber files and actually expand the ground plane around those pads to the point where they went from an eighth thou, uh, trace between there, which I was relying on, to nothing. A break! It's crazy! I, you know, I can understand maybe a thou or something like that, but to

**Dave Jones:** totally eat away an eighth thou trace going through there is just insane! God! Unbelievable! So, if you're going to get these boards from IT Studios, they're dirt cheap, great value for money, if you don't get problems like this. And they shouldn't. I'm going to have to ask them why,

**Dave Jones:** on Earth, they're actually expanding their ground plane. I already had the sixth thou clearance they required. The spec is sixth thou trace width and sixth thou clearance between, well, copper and one, any copper and any other copper. So, the ground plane and a pad or a

**Dave Jones:** via or something like that. So, it was already in place. They didn't have to expand the power plane on there. I don't know why they've done it, and it screwed up my board, and it was a pain in the arse! Catch you next time!
