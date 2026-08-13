---
video_id: omtmtJelm9M
title: EEVblog #274 - Makerbot Tweaking & First Print
url: https://www.youtube.com/watch?v=omtmtJelm9M
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 17, "2": 31, "3": 101, "4": 125, "5": 147, "6": 173, "7": 193, "8": 213, "9": 235, "10": 253, "11": 274, "12": 293, "13": 312, "14": 338, "15": 357, "16": 396, "17": 423, "18": 443, "19": 463, "20": 483, "21": 501, "22": 518, "23": 530, "24": 547, "25": 570, "26": 586, "27": 608, "28": 630, "29": 650, "30": 676, "31": 692, "32": 708, "33": 720, "34": 744, "35": 764, "36": 784, "37": 808, "38": 824}
---

**Dave Jones:** Hi, I've been having a few issues with my MakerBot. So, I wanted to print directly from the SD card, and I've been using a crappy old computer, and I've been getting all sorts of slip and step issues with my stepper motors, so I'm looking to fixing that.

**Dave Jones:** But, I thought I'd build the Gen 4 interface board, the little external keypad, so you can operate the MakerBot directly from the keypad. You don't need a computer, you can print directly from SD card. So, here we go. I'm going to build the thing up,

**Dave Jones:** and hopefully fix the stepper motor issues as well. We'll see. Anyway, let's build it. Now we have to get inside our MakerBot here, so we've got to take the damn thing apart. And, it's an absolute mess in here. We've got to plug this thing into our interface connector,

**Dave Jones:** which is all the way in here. Oops, so he's pulled out a cable. Lovely. Oops. Excellent. What did I pull out? That thing? Don't know how. Should have had a clip on that. Anyway, we've got to wedge it all back together. And, ah, this is messy.

**Dave Jones:** And there we have it. We now have our Gen 4 interface board. So, we should be able to operate this thing without the computer. Here we go. Oh, blinking. That's good. Might have to adjust the contrast. I assume that's what the pot's for.

**Dave Jones:** Get out my Swiss Army knife. Tweak it. There we go. Well, there is no text. Might have to read the instructions. Well, I'm getting absolutely nothing. It's just flashing the debug here and pressing the reset button. And, I don't know, it says I need version 2.8 firmware

**Dave Jones:** or later in my MakerBot, I'm pretty sure I upgraded to the latest firmware when I built the thing. So, beats me. Yeah, debug time, alright. And I checked. There it is. Motherboard version firmware 3.1. So, it should support this LCD. So, don't know why the damn thing is flashing debug.

**Dave Jones:** Back to the instructions. Ta-da! Finally got it. There we go. It looks like it was something to do, maybe the ribbon cable crimp or something like that. I went in there and sort of re-crimped it and fiddled around with it. Gave it the old percussive maintenance and seems to have come good.

**Dave Jones:** So, looks like we have a winner. Now if you have a look at a microscope adapter I'm trying to print for my Olympus microscope, you'll see it's supposed to be a cylinder, basically. And it's not. It's stepping out the edges like that. There seems to be some slippage in my MakerBot.

**Dave Jones:** And everyone has said something different. Oh, there's not enough drive current going to the stepper motors, the belts are slipping, there's backlash and that sort of stuff. Some people have said that it's the fact that I'm printing from the USB instead of from the SD card.

**Dave Jones:** There's, you know, a buffer problem sending via USB, which I find hard to believe. But anyway, first thing I'm going to do is just try and build the same thing again, but from the SD card using my Gen 4 interface controller. Okay, what I've done is generated the necessary file for my adapter here,

**Dave Jones:** and I'm going to go build from SD card. Microscope adapter 2, that's the only file on the card, excellent. So I'll select that, and there goes my MakerBot, it's starting. And you can see it's starting to ramp up the temperature there as it actually moves the platform, so it's got a target of 225.

**Dave Jones:** And we'll see what happens. That'll take some time to warm up. Oh, it looks like I screwed this connector that came out that goes to the heated build platform, and that's why the heated build platform was showing the incorrect temperature. It doesn't plug into this connector here,

**Dave Jones:** even though it's the mating connector with the lock in everything. That's the quadrature output, it's got to plug into this header over here. Ridiculous! Alright, let's try that again, monitor mode. 20 degrees, there we go, much better. Alright, so we'll start our build again, build from SD card.

**Dave Jones:** And I think that's why it didn't go ahead, because it was waiting for the platform to build up to temperature, and it never did, so we'll go, yep, there we go. Alright, the target temperature's 100, so it should start, there we go, it's jumping up, and the target temperature for the tool head is 225 degrees C.

**Dave Jones:** So once it reaches those temperatures, it should start the build. No, I think I'm just going to stop there because, ah, cancel the build. I can see some step in the pattern on the Y mode, so let me just go into jog mode here,

**Dave Jones:** and I like this control panel, I can just manually tweak things up. Take it out, and yep, a problem on my Y. I'll show you that up close. And you should be able to see that stepped pattern over, under my finger there. So it's definitely way off on the Y axis.

**Dave Jones:** So my next step is to check the voltage, or the drive going, the current drive, which you measure by measuring voltage on test points here on the board. This is the Y stepper motor controller, and I've, the instructions say it should be 0.6 volts for ref.

**Dave Jones:** And it certainly is, there it is, 0.6. So let's check the other ones and see what they are. And I think I've got it figured. There are different voltages here for the different types of stepper motors, either the MakerBot NEMA 17 or the Moons brand NEMA 17.

**Dave Jones:** And if we look inside my MakerBot here, you'll see I've got a Moons brand, if you can read that, Moons brand motor. So that's why I've got it wrong. I've got these set up to the MakerBot stepper motor. So I have to adjust these, and there is a fairly huge voltage here.

**Dave Jones:** There's a, it's currently set to ref is 0.6. It should be the Moons motor on the XY axis set to 1.68. It's getting nowhere near enough current. Oh! Well, that certainly sounds different now. Now it sounds like it does actually have more grunt in there in each step.

**Dave Jones:** It certainly sounds louder, so I'll let this go for a while. It's got, I think, a 60 minute build time on my microscope adapter, and we'll see how it goes. By the way, this controller's actually got some hooks on the back. It allows you to just hook it up on the top of the unit like that,

**Dave Jones:** which is rather neat, because it does slide around. It's got no rubber feet on it. If you try and use it on the desk and you push the buttons, it just slides across the desk, hopeless. And it does seem to be working very nicely.

**Dave Jones:** I see no issues in the X or Y direction. I think we might have a winner! And you can see it just about to fill in my second layer there, so it's got the crosshatch underneath it, and now it's gone for the solid next layer.

**Dave Jones:** Ooh, yeah, it didn't quite fill it all in. Maybe it fell through, but it should eventually, well, hopefully, eventually will fill in that gap there. I guess it will put like a small solid section between, there we go. I love the sounds. There we go, if we go in this direction, we might,

**Dave Jones:** yeah, there we go, it's building up the platform there, you can see it. And this is building up the next level, which you'll have, because it's not just a, it's not just a single cylinder, there is a stepped aspect to this. But there you go.

**Dave Jones:** And there it is, my first ever make-it-your-useful MakerBot print, and it looks absolutely spot-on in the X axis, and more importantly, the thing I was having a problem with was the Y axis. And there it is, it looks absolutely perfect. Just like I bought one.

**Dave Jones:** I'm sure there's an art to ripping off these rafts on the bottom. And yeah, I might have to get a knife in there and slice that out. I just realised I don't really have to take the raft off that, because it does seem very difficult, even trying to get the knife in there.

**Dave Jones:** So I guess the idea is not to print rafts, but I don't need, I don't need to remove the raft, because this will sit on the bottom of the microscope adapter, and you won't, it'll be, it is the bottom of it, and you won't, you won't really see it, so all I've got to do is

**Dave Jones:** clean the edges up a bit, and make sure it's not fouling the inside there, and that should be right. Now unfortunately, it turned out perfectly, but it doesn't fit, it's too small. And it doesn't fit my camera either, and the idea was to fit my old blogging camera,

**Dave Jones:** this is the old camera I used to use for the blog, and the whole idea was for it to sit in there like that, and for that to go on my microscope, but the inner diameters are too small, and I did allow half a millimeter bigger,

**Dave Jones:** but obviously that's not enough, the, I guess when it's squared to the plastic it oozed out and made a smaller diameter hole, so yeah, bummer. It's a perfect print. Other than that, I love it, but just, well, I learned something, it doesn't fit.

**Dave Jones:** You've got to accommodate that, so what I'll do is I'll print a couple of test rings at various diameters, just to get the exact fit on my camera and on the microscope, and when I've got that, then I'll print the final thing, and hopefully it should be good.

**Dave Jones:** I mean, I could try and file it out or something like that, but I think I'll just experiment some more with the software. So there's a couple of flat spots on it, very, very small flat spots. You'd really be, you know, so you can probably see a flat spot up the top and

**Dave Jones:** bottom there, but apart from that, it's pretty darn impressive. I'm, I like that a lot. I mean, considering that, how many tens of thousands of little micro steps did it have to do, and considering that this is an open loop system, the MakerBot's an open loop control system,

**Dave Jones:** and there is no absolute positional feedback, and doing tens of thousands of little micro steps, and after it built up all of this, and to be pretty darn close to spot on like that, I think is awesome. So there you go. I had a hard time getting the raft off the bottom, so I probably shouldn't

**Dave Jones:** print the raft on future ones I think, but that's a really nice first useful print. Check this out, I decided to print a spool holder to replace my bodgy cardboard spool holder on the back there that I've got, so that should mount on the top here, and I should be able to have my spool

**Dave Jones:** on the top. Awesome. Let's break it off and give it a try. Well, that was a waste of filament, unfortunately. It fits, it was a very tight fit in there, but the damn thing doesn't rotate. I've got to put a lot of force onto that to make the thing

**Dave Jones:** rotate. It needs to be loose. It's crazy. It doesn't work at all. Grrr.
