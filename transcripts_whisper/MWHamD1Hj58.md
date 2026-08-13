---
video_id: MWHamD1Hj58
title: Adventures in AVR ISP Programming
url: https://www.youtube.com/watch?v=MWHamD1Hj58
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 23, "2": 38, "3": 67, "4": 85, "5": 98, "6": 114, "7": 132, "8": 152, "9": 172, "10": 199, "11": 220, "12": 250, "13": 276, "14": 295, "15": 312, "16": 339, "17": 361, "18": 377, "19": 395, "20": 413, "21": 444, "22": 457, "23": 479, "24": 495, "25": 512, "26": 536, "27": 551, "28": 570, "29": 594, "30": 612, "31": 631, "32": 653, "33": 670, "34": 694, "35": 725, "36": 749, "37": 773, "38": 796, "39": 824, "40": 842, "41": 864, "42": 884, "43": 902, "44": 924, "45": 941, "46": 963, "47": 982, "48": 1006, "49": 1031, "50": 1052, "51": 1077, "52": 1093, "53": 1111}
---

**Dave Jones:** Hi, do you remember the micro-red monitor radiation network thing that I got in the mail bag quite a few years ago from Radu Motisan? Well, I used to have it hooked up to my network here and I was monitoring everything else, but I think he changed the system, I don't know, something happened, because I got like an early

**Dave Jones:** BD unit or something like that, and I was supposed to, and it just stopped working one day and he sent me some new firmware, and this was quite a long time ago, but I never got around to updating that firmware, so I just thought I'd actually do that now.

**Dave Jones:** It's an ATmega328, I think it is, inside this thing. And Radu's got this nice firmware upgrade guide page, so I thought I'd just do this. I've got my AVR Mark II programmer, so hopefully that will work, it's a 3.3 volt compatible unit, so he sent me a hex file, it has to be individually programmed hex file for each unit,

**Dave Jones:** and so I've got that, and presumably it will work again if I flash that. So I've got to do the AVR, well, I was going to, well, he's a suggested AVR dude here, but I thought, oh no, look, I'll install Atmel Studio 7, I haven't installed it for a long,

**Dave Jones:** Atmel Studio for a long time, I think, you know, 5 or 6 was the last one I used before they got bought out by Microchip. Anyway, I've been sitting here trying to install this heap of crap for like 10, 15 minutes, and it's just been spinning its wheels.

**Dave Jones:** Most of the time it spent, this was all the way over here, now it says it's caching something, it's just a worst installer I've ever seen, it just sits there giving you no information at all. Absolutely ridiculous. Anyway, not happy with that at all.

**Dave Jones:** So I think I'll go down the AVR dude route, and we'll give that a try. I've never used AVR dude before, so we'll give that a go. Anyway, we'll go into WinAVR, I believe, contains AVR dude and everything else, so I'll download and install the latest version of that.

**Dave Jones:** Let's go. So we'll just install that, English, thank you very much, install that, and give it a burl. Ah, it's on my other screen and I can't drag it. Hang on, yes I can. Yeah, I agree, whatever, sign my life away. Oh, it's just going to put it in my C drive, oh yeah, whatever, it's only small.

**Dave Jones:** Let's go! Install programmers notepad, I don't want that. So that's installed, that was quick and painless, unlike the bloody Atmel Studio thing. Unbelievable, thank you very much Eric B. Weddington, who maintains this. Open source, WinAVR is like an open source, well it's a suite of executable open source software.

**Dave Jones:** Fantastic, and yes, it contains AVR dude down here, 5.8 cv, open source programmer software, there's user extensible, so there you go. Now I presume I've got to plug in my AVR ISP Mark 2 programmer. Hopefully this works, we'll find out. I'll plug it in, and it's installing device driver, here we go, driver not found.

**Dave Jones:** Ah, terrific, first hurdle. I mean, I haven't done AVR programming on this machine for a long time, and well, may not have even originally been in this machine, so yeah, let's like, give me a break. Argh, I hate bloody tools like this. I just want to program one chip, that's it.

**Dave Jones:** Now my cursor's frozen, what the hell's going on? Stupid mouse. Logitech M215. No, no, disconnect the programmer. No, bloody cursor's frozen. Alright, now I remember, yeah, you had to install the AVR ISP drivers separately, and that installer didn't do it, so let's, here it is, libusb blah blah blah blah blah,

**Dave Jones:** so we can actually go in here, in the winavr stuff it installed, and we'll have to do that on our own. It looks like it might be in utils, libusb, bin, obviously. Is that where the install info wizard? Oh, I don't know. libusb, yep, libusb, that's what we want, so let's, I guess, try and run that.

**Dave Jones:** This program will create an imp file for your device before clicking, oh yeah? Here we go. What have we got? No? Select the device. Okay, I've got to plug it in. Hang on. Here we go. Oh, so much fun. Fun for the whole family.

**Dave Jones:** Sorry, it keeps going back to the other screen. I capture on a specific screen, because I've got a full HD screen, a 1920x1080 screen that I capture on, and it's not my main screen, so it's, that's just the way it is. Anyway, info.

**Dave Jones:** Aha! There it is. Next. I assume, insert manufacturer name. Atmel? Or is it microchip now? I guess, I don't know. I haven't done this before. Your file. Okay. Oh, okay, can I load that? So it's saving. Okay, we'll just save it as your file.

**Dave Jones:** Hmm, okay. AVR-ISP2-INF. That's the, there's that like a Windows setup thingamabob, is it? I don't know. I don't know enough about this crap. Alright, now we're talking. I went into device manager. Here we go. Yeah, I went into device manager, AVR-ISP, did all the manual stuff.

**Dave Jones:** Windows can't verify and install this driver or software anyway. You bet. Come on, let's go. Ah, all this manual stuff, like it probably would have worked if I installed the, went through the pain of installing the Atmel studio thing, if it ever bloody well downloaded.

**Dave Jones:** Anyway, has it countered a problem? Of course it has. I think I remember this before, and I've probably even done a video on it, but I can't bloody well remember. Ah, close kernel digitally signed driver, blow it out your ass. Ah, God, why can't tools just work?

**Dave Jones:** Ah, man. Woohoo, it may have actually worked. Look, there it is, libUSB, Win32 drivers, AVR-ISP, Mark II. It's no longer in the other devices. So why did it tell me that whatever, it didn't work? Anyway, um, okay. We might be cooking with gas.

**Dave Jones:** Let's give it a bell. Alright, I'm in my command prompt here. Good old, back to the days of DOS. Jeez, unbelievable. Anyway, there's my micro red monitor hex file that Radu's prepared for me. And, um, AVR, dude, there it is. It's accessed. Now, I like, my AVR-ISP Mark II programmer, the orange light on the top is flashing,

**Dave Jones:** so I don't, I can't recall if that's normal or not. I'm surprised that, you know, I wouldn't be surprised if there's some sort of firmware incompatibility issue, because I've had to update the firmware on the AVR-ISP Mark II several times in the past,

**Dave Jones:** and it's been a whole pain in the ass, it really has. Um, so let's, what do we have to do? Here we go. We've got a command here. AVR, dude. So we should be able to, can we copy that? Anyway, so there's my AVR-ISP Mark II hacked version,

**Dave Jones:** you might remember that I did a video on how to hack that to make it 3.3 volt compatible, and I can't remember if that's normal, I don't know. It's doing something. Anyway, time to hook it up to the DUT, the poor old DUT.

**Dave Jones:** So, here's inside my little micro red monitor. Sorry about the focus, this C920 webcam seems to have a hard time focusing on stuff, I'm not exactly sure why. Anyway, let's just make sure we get pin 1 correct. I've oriented it as per the photo.

**Dave Jones:** So that looks, uh, that looks correct. Come on. Get on there. Oh, d'oh! You're not gonna believe it! This is a 10-pin header! I've only got the 6-pin! I've only got the 6-pin header! Shit like this! That just, like, it just sucks your time away.

**Dave Jones:** It really does, when you've got to do something like this just once. Like, you know, like, ordinarily I haven't programmed ATMO AVR stuff for years. Don't have the software, don't have the, you know, I'm not doing, it's not something I'm doing every day, and just, uh, like,

**Dave Jones:** I should have checked, but I didn't. And, of course, it doesn't fit. And, of course, I'm not in my lab. I'm actually at my, uh, editing office here doing this, and I don't have the little jumper cables to go over. Ah. It's, yeah, hang on.

**Dave Jones:** Yep. Typical Friday. And there it is. There's the two different 6-pin and 10-pin AVR ISP headers. Ugh! Alright, so I've got all the wires bodged in, converting, because it's not the same, uh, pin-out. It's, you know, like, it's obviously got the same connections,

**Dave Jones:** but, uh, the actual pin-out is, apart from VCC, I think, is the only, and maybe, yeah, an equivalent, uh, ground on pin 6 there is basically the only one that's, uh, the same. So it's, yeah, just rather annoying. Ugh, I hate multiple ISP programming things.

**Dave Jones:** Anyway, 3.3 volts. Um, I don't believe we need to apply power, uh, to this. It should power it through the, uh, ISP. So let's switch it on and see what happens. I believe it's supposed to... Hey, hello. There's a LED under there. Oh, green.

**Dave Jones:** Green! Yes! We got it! I presume that's, uh, all hunky-dory. Let's try our command now. Ho-ho, we might be on a winner. All right, now we're supposed to put in, um, this command here to do the AVR-DUDE program, but C is to specify the actual, uh, programmer itself.

**Dave Jones:** Now, I'm not sure of the ID name. Obviously it's not the USB-ASP. Well, I don't think. It could be. Um, but apparently you can type in the command AVR-DUDE, uh, dash C A-S-D-F, and that's supposed to put in the supported programmers. Oh, there we go.

**Dave Jones:** A-V-R-I-S-P M-K-2? Okay, you can put either one. Okay, so it's all lowercase A-V-R-I-S-P M-K-I-I. Let's try that. Cool. All right, I'm going for broke here. Here we go. Hopefully I've got that command right. A-V-R-DUDE, I've replaced the A-V-R-I-S-P mark 2. I've put in my filename.

**Dave Jones:** Exactly, colon I on the end. Here we go. Fingers crossed. In shot. It's doing something. Come on. What's it? No, no, that doesn't look promising. Oh, no, here we go. Receive timeout. Nah, S-T-K-5-H-U-N-D-E-D 2? No, it's not talking to the programmer. Ah, great.

**Dave Jones:** I knew this would happen, like Murphy. It was guaranteed. It was guaranteed not to work. Okay, let's try changing the programmer name A-V-R-I-S-P 2. Let's try that. Give that a burl. And no, I'd expect it to instantly connect. So, wah, wah, wah, wah.

**Dave Jones:** And I think I might know what's wrong. What's wrong? Look, it's got the little warning thing next to it. It didn't have that before. So, yeah, it's obviously not talking to that anymore. So, what's going on? Hmm. Alright, so I just installed, like, another random driver off the interwebs.

**Dave Jones:** And it seems to have done the trick. There you go. It seems to have done the trick. So now it's, well, device manager says it's all hunky-dory. But I'm sure it said that last time, didn't it? Alrighty, let's try that again. Glutton for punishment.

**Dave Jones:** No, I would have expected it to talk straight away, surely. No, no, I think it's going to do the same thing. No, yeah, time out. There you go. And it still says it's installed. So, yep. But why it's looking for the STK 502, well, maybe that's sort of the driver it's kind of using.

**Dave Jones:** But yeah, it's getting time out. So it's obviously clearly not working. It's not talking to the programmer. Woo-hoo! I got it! Hang on! Here we go! I'll tell you in a second. I forgot to hit record. Okay, what I did, whoa! We're done!

**Dave Jones:** Safe mode, fuses okay, flash verified. Thank you. Thank you very much, AVR dude. Done. What I did is, I'll go back in here. Here we go. I put in the uppercase P as opposed to lowercase P, which is program. I put in the uppercase P, which is port, and then USB.

**Dave Jones:** Yeah, the dash P, USB, uppercase P, port. So apparently it's supposed to, the drivers are supposed to just do USB by default or something. But, hey, it couldn't find it, so that's all it was. And everyone's probably screaming at me going, Dave, that's obvious, I know about that.

**Dave Jones:** Well, of course you do, right? It's either worked perfectly for you before, or you followed instructions that worked perfectly, or you've been using it forever. But when you come, you know, to something like this, like once in a couple of years, you just want to, you know, dig out your old programmer and just program a header,

**Dave Jones:** then, well, anyway, we're done. So I'm happy, hopefully. Now I'll plug, so this is re-flashed, reprogrammed, so I'll put it back in the case. I'll hook it up to the USB. Apparently it takes a while to connect to the micro-RAD system or whatever.

**Dave Jones:** So I can't exactly remember if it, like, it pops up. It should auto-pop up my location if memory serves me correctly, because my one's programmed with my location. So it should automatically identify on the network. So anyway, there you go. That was just, that took me a little bit.

**Dave Jones:** I'm not sure, you know, how long that took me all up, like an hour and something. Plus, you know, going back to get the cables from the other lab. So there you go. I hope you enjoyed that. Well, there's nothing to enjoy. I just wanted to share with you the, ultimately, what I knew would be a little bit of pain in getting this working.

**Dave Jones:** I knew this sucker would not work first go. I don't think it ever has, the AVR-ISP Mark II. I've had so many issues with it and compatibility with various AVR tools that I've used over the years. Pain in the butt. But anyway, yeah, it's like driver issues and whatnot.

**Dave Jones:** But I'm surprised I didn't have to update the firmware in this again. But yeah, mine's like a 2009 vintage unit or something. It's pretty old. So yeah, anyway, hopefully I'll get this working. It looks like we've got one! Look, it wasn't live in Sydney before, but check it out.

**Dave Jones:** Unfortunately, it's got to be mine. Unit, yep, 111000B in Cremorne. Military Row, Cremorne. I do not live anywhere near Cremorne. For those who want to know, for those who haven't been to Sydney before, let's have a look at the map. Here is the Sydney Central Business District, the Sydney CBD.

**Dave Jones:** And the iconic Opera House is right in there. There's the Harbour Bridge. Then you've got the Harbour Tunnel. Nobody likes the Harbour Tunnel, but it's functional. Yeah, it works. And I used to work at the Garden Island Naval Base there for Australian Defence Industries.

**Dave Jones:** Jeez, that was in a galaxy far, far away. And yeah, so that's Sydney CBD. But Sydney actually extends basically all of this white stuff. Well, it doesn't extend down that far, pretty much. It stops down at Camden there, pretty much. And Penrith at the base of the Blue Mountains here, that's where it stops.

**Dave Jones:** And that, all of that, that's about 50km from Sydney right out to the base of the mountains there. So Sydney's a pretty darn big place. And I'm, like, out in the Hills District, somewhere around here. Somewhere around there. So there you have it.

**Dave Jones:** I'm back on the grid, and I'm currently the only operational one in Sydney. I don't know if these other four other people have got them, whether or not they've had, like, that firmware, like, early units and then firmware, old firmware not being compatible with some upgrade or something like that.

**Dave Jones:** But anyway, mine is working. What am I getting? What sort of dose am I getting? Microsevits per hour? 0.15? 0.18? Aww. Should go to the bunker, I think. Anyway, I hope you liked it. Catch you next time. Thanks for watching.
