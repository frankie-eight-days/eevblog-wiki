---
video_id: Ferz6Dy73_I
title: EEVblog #1370 - Kindle Paperwhite REPAIR
url: https://www.youtube.com/watch?v=Ferz6Dy73_I
source: youtube-asr
---

**Dave Jones:** Hi, it's future editing Dave here doing a voiceover because well, Dave's dumbass uh cameraman forgot to plug the microphone in. So, I got like halfway through this video before realizing it wasn't plugged in. Yeah, duh. Anyway, so voiceover, this is my Amazon uh Kindle

**Dave Jones:** Paperwhite. It's I don't know, three, four, five years old or something. It's quite old now. And um I've been having issues with it for like months where uh the touchscreen would uh intermittently work and not work. And I of course

**Dave Jones:** without the touchscreen you can't use it. It's got no other uh controls on it. So, it's really annoying and no amount of resetting sort of uh fixed anything. So, I finally got jack of this thing. It's now just completely not working.

**Dave Jones:** And the other thing is is that uh it's not charging either. It's um yeah, so is the battery dead in it? I don't know. It's not doing anything. So, it looks like it might be a combination of faults

**Dave Jones:** or faults could be actually be related. We don't know until we play around with it. So, let's take it apart. And yeah, you can actually uh like press and hold the reset button to like reset the things like you hold it for 10 or like a

**Dave Jones:** minute and it's supposed to like completely reset the CPU and uh stuff like that. So, I've tried that. None of that uh seems to work. So, nothing left. Let's take it apart. I really had quite a bit of trouble actually getting my

**Dave Jones:** little plastic spudger. You don't want to use a metal spudger cuz then if it slips you can actually, you know, put a big mark across the uh screen. I had actually a lot of trouble trying to get this under and uh pry it out. But I

**Dave Jones:** found that uh if you do it from the power connector end, there's a bit more give under there which allowed me to get it under. I finally got it though. So, the front is just uh stuck on with some

**Dave Jones:** head adhesive and then you've got like a dozen screws to get this thing out. That's actually a lot of um screws to like that adds a lot of production cost to the unit. Somebody's actually got to screw all these screws in. Like it's an

**Dave Jones:** alloy uh frame. Don't know whether or not it's a magnesium alloy or not. And then the whole thing just start lifts out easily and you can see that there's a little RFID tag on the back cuz it doesn't actually connect to anything.

**Dave Jones:** It's not like a Wi-Fi or an antenna. It's that is the RFID tracker that they use when it goes through the conveyor belts on the production line and stuff. They have to identify these units and this is this is the way they do it at

**Dave Jones:** various production assembly steps. I'm not sure of the exact, you know, thing. It's all closely guarded Amazon secret, of course. But yeah, that just allows you to individually identify each unit with a remote sensor. So here's the completed assembly. Very

**Dave Jones:** nice. Everything's under a metal can, of course, and the battery there it is. Lithium polymer job 5 and 1/4 watt hours and it's easily replaceable. So, you know, hats off. They've made these things simple to easy to replace. I mean, it wasn't hard

**Dave Jones:** to get the front panel off and if you can just unscrew that, then any Joe Average replace the battery in their Kindle by the looks of it. And yeah, main piece of it everything's under the metal cans and unfortunately can't get

**Dave Jones:** those off. They seem to be soldered down. So, we're not going to see much at all. And there's our e-paper display driver and looks like we've got some charge pump caps there, but nothing else doing. There's nothing wrong with that.

**Dave Jones:** And here is where we might potentially have an issue. This is our touch screen connector there and our touch screen controller I believe it's like a capacitive touch screen. And yeah, so there could be like some connection issue in there perhaps, but I don't know

**Dave Jones:** until we solve the problem of well, I'm going to solve the battery charging problem first. I'm not going to jump into the touch screen controller. It's more likely to be a battery. When you're trying to solve a troubleshoot these

**Dave Jones:** things, you want to do the easiest stuff work. You don't want to go down the rabbit hole of the touch screen controller and all the dicky little connections in there and things like that. Um yeah, solve the charging issue

**Dave Jones:** first and you might find that the touchscreen controller issue was related to the battery. I mean, the battery's easy to solve. We can just take it out. So, the battery just uh lifts out here and then it's just got some uh spring

**Dave Jones:** contacts onto a a PC board in there and that's going to have some uh battery protection as well. But, have a look at the contacts though. There's actually four pins and it's not like a temperature uh sensing pin for like

**Dave Jones:** overcharge and stuff like that. No, they're SDA and S CL. So, that's an I squared C interface that no doubt has an annoying um like ID chip in it and the software they've protected these things. So, if you put in an aftermarket battery

**Dave Jones:** that doesn't have the correct ID in it, hasn't spoofed the ID, then it's going to pop up with an error message, you know, probably saying, you know, "Invalid battery" or something, you know, "Not authorized by Amazon by your

**Dave Jones:** Amazon overlords." And uh yes, please buy a genuine one. And uh bugger off. But, the good thing is though that that ID chip should be on the protection uh PCB in there. So, we should just be able to If there's anything wrong with the

**Dave Jones:** battery, we should just be able to replace the uh cell inside there but keep the PCB. So, it has the genuine chip in there, so it'll think it's a genuine battery, but we've just replaced the cell. And that's how you can get

**Dave Jones:** around this. So, let's see if this has any juice left in it. 2.86 volts. Well, no, that's not good enough. That's usually below uh the operating voltage of um like a device with a lithium uh polymer lithium ion battery like this. Uh but,

**Dave Jones:** it is above the like typical uh dead cell uh protection voltage of like, you know, 2.4, 2.5 volts, something like that to actually protect the cell from over discharge. So, it's somewhere in there, but it's not good enough to

**Dave Jones:** operate it, clearly. All right, so let's do a uh charge test on this thing to see if it actually charges or not. Uh so, we're going to it's uh normal 3.7 volts, but uh these uh charge up to 4.2 volts,

**Dave Jones:** so that's that's the maximum compliant voltage you want to set and the current you want to set uh typically like for something like this you don't want to charge it at 1C. So it's 1400 milliamp hours you don't want

**Dave Jones:** to charge it at 1.4 amps which you would be 1C. So we're going to go on order magnitude less than that to be safe 140 milliamps. I don't know what the actual charge rate is for the Kindle but you

**Dave Jones:** know this will be nice and safe. So let's give it a go. So how do we make contact with this? Well using the awesome PCB system. I love these things I've done a video on the second channel and on the

**Dave Jones:** mail bag actually reviewing this and they're just pressure point contacts which are just under their own weight make contact very handy and they got the magnetic base and everything. Fantastic. All right so let's switch it on and it's

**Dave Jones:** instantly gone up to 3.8 3.9 volts. Wow that's a significant jump up. I wouldn't uh have expected that perhaps but anyway I'm yeah it's it's doing there's 140 milliamps going into it but whether or not it retains it that's the trick. And

**Dave Jones:** it does seem to be like jumping all around the place. So doesn't seem to be doing the normal charge curve. I think we've got one sick puppy here. Back to my internal mic now. Don't. Anyway I'm the voltage is rising so that

**Dave Jones:** indicates that it's a charging curve. So it indicates that it is accepting the charge which causes the voltage to rise up. So it's doing something. But whether or not it holds it I don't know. Okay I pushed it up to 250

**Dave Jones:** milliamps cuz I'm a rebel and it seems to be holding. I can just just can't wait. I'm going to going to disconnect it and see what happens. 3.8 well yeah I would have expected it to drop back. I

**Dave Jones:** could put a reasonable load on that of course and and see if it drops but all right let's do that. So let's hook that up to a load well constant current let's just draw a small current. Let's just

**Dave Jones:** draw like 50 don't want 50 amps. 05 enter. Okay, 50 milliamps constant current, so I'll turn that on. Let's, you know, expect it to drop a little bit. Let's see if it like dramatically plummets. And yeah, it dropped right

**Dave Jones:** down to 3.03. So, it can't even sustain a like 50 milliamp current. So, yeah, that battery is all show and no capacity. So, yeah, there's something something wrong with that. And look, it's just No, it's going up. It's it's

**Dave Jones:** jumping all over the place, actually. It's a bit jet rabbity. Yeah, something very wrong with that battery. Try 10 milliamps. Series resistance is is very high. That indicates that yeah, it's going the way of the dodo. Let's just

**Dave Jones:** wind that up and see at what point it just dies. 20 milliamps, come on. Yeah, a battery like that that can't deliver 20 milliamps, 30 milliamps is just yeah, hopeless. It's not even going to get to 100 milliamps before it's just Yeah,

**Dave Jones:** it's it's toast. That will work very nicely. Thank you very much. So, I've got the probes on the back like that. All right, so let's give this a whirl. I've got it 3.7 volts, which is, you know, nominal for a lithium polymer.

**Dave Jones:** Half an amp because well, it might turn on the Wi-Fi or something like that. So, push this. This button's a bit tricky. 170 milliamps, it's working. It's booting. It's booting. Woohoo! Your Kindle nee- needs repair. It is. Yeah,

**Dave Jones:** yeah, here's the catch. There you go, upside down. All the electrons are going to fall out. Repair needed. Your Kindle needs repair. Please contact Kindle customer service. Battery invalid. -1. Bastards. Now, unfortunately, that's not going to let me test

**Dave Jones:** the touchscreen. So, that's really annoying. We should be able to prize this out. You can see the two terminals in there. So, I'll cut those and then should be safe to actually sell. The pouch should just be like stuck in the

**Dave Jones:** bottom with some double-sided tape or adhesive stuff. See if I can pry that battery out. Got to be careful. You don't want to uh actually pierce the pouch. I can feel it breaking. It's breaking. As in the adhesive. That's a metal

**Dave Jones:** backing. I thought that was all plastic. It's not. Came out of the frame, the plastic frame like that. That's interesting. Wow. It's kind of annoying actually. So, I have actually cut both of those tabs on top. And the one

**Dave Jones:** down in there does seem to go down to the PCB down in there. Some sort of poly switch. Cuz I want to keep the PCB intact and then potentially like just mount a much smaller battery in there and then just wire it on. It should

**Dave Jones:** work. So, it's just a matter of separating the adhesive in there. I'll get it eventually. Outski, you want to dispose of that? DuPont DuPont Nomex. That looks like it's damaged, but that's actually not um the internal cell. That's just the outer

**Dave Jones:** uh wrap. So, no, I haven't bent, haven't damaged, haven't pierced that. And uh it's a bit how you doing. If anyone knows why they use a metal backing on that instead of a like a whole plastic carrier, uh please leave it in the

**Dave Jones:** comments. So, there's our main board. Is that our main charge controller or is that a mosfety? That looks for all the world like a mosfety pinout, doesn't it? I think we've got an external fit there. The controller is likely that little

**Dave Jones:** sucker down there. There we go. Is that our poly switch? Yes, I do actually have a drawer for this. And yes, it is labeled. There you go. That looks all right. That looks not all That one looks a bit fatty. Yeah, 1,000 mA hour. Woah,

**Dave Jones:** might be a bit too thick. So, apart from this little itty-bitty thin thing, can't remember where I got that from. Obviously, I pulled it out of something. I thought, "Oh, that really thin one could be useful for something." Oh, if

**Dave Jones:** you squint, it makes it. And shoving it back in here, yeah, that's really bulgy. Not much uh thickness left in that to like dig out a a pouch or anything. Although technically this actually does have bit milled out of it. You can see

**Dave Jones:** all the milling marks and everything. So if I take out the metal that might do the you know it's like point one millimeters. Everything counts. Yep, I reckon I can do that. I'm going to go ahead and use that puppy. So I'll solder

**Dave Jones:** it in now. If you sit it flat little bit of wobble wobble yeah, but uh it's good enough for Australia. Check this out. This is very weird. If I take the battery on there which of course measures 3.8 volts. No worries. It

**Dave Jones:** doesn't come through. Why? It's like the low side MOSFET is off. If I buzz this out the positive actually goes through to here. No worries. And the low side goes through to the test point here on the one side of the MOSFET. And then on

**Dave Jones:** the other side which is the actual battery negative terminal. No, that's now positive. What? What? That's now direct continuity. What? So if I take that back I should be getting Wow, there's a there's a dicky contact in there

**Dave Jones:** somewhere. I'm going to have to solder that properly. Yeah, so what I've done there is I've just actually removed this metal cap that they had on there. And I've also removed tag going over to here. And solder does readily take to

**Dave Jones:** that side of the fuse. So yeah, I the tabs just don't work. So I might like put the battery over here and just put some little wires over. That's probably easier. There we go. That's much better. Before I cover it up.

**Dave Jones:** Ta-da! 3.8 volts. No wackers. And that'll be good enough for Australia. Well, it's done something. We're back to that screen. Beauty. So let's plug that in. See if it'll accept charge. Our LED's on. Don't know if it's Oh, yep.

**Dave Jones:** Yep. Yep. WE GOT A WINNER. Chicken dinner I suspect. Okay, well it's just done that. I can't remember if you should be able to power these while they're charging right? Or maybe I don't know, maybe I have to reset the thing or

**Dave Jones:** something. No, it's Is it still in its original state? I mean, that it shouldn't be showing that low a battery. I didn't load that battery down, but I you know, surely Murphy wouldn't have let me put in another Cactus one. Oh,

**Dave Jones:** no, no, no. Oh, was that my imagination or did that go up? I think it moved up by a pixel. No, it's not really increasing, unfortunately. Nothing really else around to measure, is there? It's all under the damn cans. So yeah,

**Dave Jones:** unfortunately, I can't get it to do anything. If I hold down the button for 10 seconds, it the LED will switch off and stay off, and then when I release the button, it'll come back on. So the processor and stuff is being powered,

**Dave Jones:** but I don't know, maybe I have to wait longer, but it's it's not going up. I waited like half an hour already. It's doing nothing. So what I've been able to do is hold down the reset button for

**Dave Jones:** like a minute, and like the LED here flashes green briefly, and eventually when I release that, it clears the screen and puts the charge symbol back on. So the like the processor and everything's working, it's getting voltage from the battery, and every like

**Dave Jones:** it's doing everything, it's driving the screen, and hunky-dory, but it refuses to charge, by the looks of it, anyway. And if I have a look at the current monitor, look at this, it starts out drawing about 70 milliamps, but now it's

**Dave Jones:** drawing 460 milliamps. That's not going into the processor, cuz the Kindle is ridiculously low power. That's constant, like it's charging the battery. Yet, there's no indication that it's charging. Possibly, like a secondary fault with the charging chip, cuz the

**Dave Jones:** battery was definitely faulty. Oh, yeah, there we go, green. Oh, hang on. No, it's doing something. Oh, no. Oh, there we go, it's back. Oh, so either like it's reporting the state of the battery is too low, and it's just switching

**Dave Jones:** itself off when there's clearly current going into the battery. I mean, you know, I don't want to have to get out and dick around and try and get like pros out of there and, you know, try and probe the damn thing while it's charging

**Dave Jones:** and stuff like that. I mean, jeez, I've already gone down enough bloody rabbit holes. It's doing something. Flash, flash, flash. What does that mean? Woohoo! Hang on, it's finally come good. By the looks of it, I just left it here

**Dave Jones:** charging again. Yeah, it's still charging at 460 odd milliamps. Because it doesn't take that just actively takes nothing when it's cuz the e-ink displays, of course, take nothing. They just they don't need any power to actually keep them going. So, this thing

**Dave Jones:** just sleeps all the time scanning the touchscreen and then if you touch it, it wakes up and it changes the page or whatever and it goes to sleep again. So, it needs no power. So, all that charging at 460 milliamps, that's all going into

**Dave Jones:** the battery at the moment. But, it's obviously that like minute-long reset or a couple of cycles of that obviously got the thing working. It was really locked up. Oh, yeah, yeah, there we go. We're in. And there you have it. It's charging

**Dave Jones:** up there. Indicator looks like Oh, but my hang on, my my my touchscreen works. Yep, that seems to be working fine. So, uh ignore the noise and the jackhammering in the background. There's some fit out work going on in the office next door.

**Dave Jones:** Um yeah, it works and we got the little LEDs down here. Fantastic. Winner, winner, chicken dinner. I'm going to put it back together. No! Bloody Murphy. Look, I put the front panel back on. The touchscreen doesn't work. Maybe there's

**Dave Jones:** some alignment issue and it thinks the plastic is touching it, but it should be like a capacitive touch, I think. Okay, this is ridiculous. I can't get this to do anything now. Touch Oh, no, now now it's it's done it.

**Dave Jones:** Oh, this Oh, no, it's resetting. This is cursed by Murphy, this one. Anyway, that is the that is the reboot screen. so I'll get back to you when it's done. Okay, it's going through its full on. Maybe it just needed another kick in the

**Dave Jones:** pants to give it like a complete system restart. So, we might be dealing with software lock-up issues instead of hardware here. Seems to be stuck there. Bloody non-linear bar graphs. Okay, it seems to be back. Yeah, the touchscreen's

**Dave Jones:** working. It's showing the battery's only very low. Plug that back in and charge it. So, it's obviously, you know, it's doing the charging thing. No, I don't think there's anything physically wrong with the touchscreen. I think we're just

**Dave Jones:** dealing with software issues because like this was my major issue with this. It didn't seem like the battery was failing. It seemed like you know, the touchscreen was the thing that was failing. It was annoying me for like a

**Dave Jones:** month. It would work occasionally, then it wouldn't work, and it was just It was just really annoying. So, seems to work. So, carefully, you saw it. It's working. Let's put this front cover back on. Please work. It works.

**Dave Jones:** I think that there's just like really like software lock-up issues with this thing. Please, if you've had experience with this, you know of happened to you, you know of others that this has happened to, please leave it in the comments down

**Dave Jones:** below. But yeah, it looks like yeah, we just had a failed battery that probably led to weird lock software lock-up issues and stuff like that. I could never get it. You know, I was trying the reset thing and stuff, and that never actually

**Dave Jones:** worked. So, looks like I had to fix the battery problem and then fix the lock-up software problems. It looks like it just went through a hard reboot then. Yep, I think we're good. I'm pretty sure that's going to charge, so I'm going to call

**Dave Jones:** that a winner, and I can use my Kindle again. Thank goodness. Oh, what a drama. I know that ended up being like essentially just a simple battery repair, but you know, there's just more to it than that. You could have like gone down the

**Dave Jones:** rabbit hole thinking, "Oh, there's something wrong with the touch screen." And something like that because everything else seemed to be working, so you could have like uh chased a red herring down that rabbit hole. And no, so anyway, there you go.

**Dave Jones:** That is a Kindle repaired, finally. Oh goodness, what a drama. And the bloody microphone thing, goodness. Can't win. So anyway, if you like that and if you like the struggle, please give it a thumbs up. As always, discuss down below. You know what to do.

**Dave Jones:** Catch you next time.
