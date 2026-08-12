---
video_id: 4XGwveNyLJo
title: EEVblog #1354 - Compaq Portable Repair - Part 2
url: https://www.youtube.com/watch?v=4XGwveNyLJo
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 35, "3": 58, "4": 73, "5": 84, "6": 107, "7": 122, "8": 135, "9": 149, "10": 156, "11": 184, "12": 196, "13": 209, "14": 219, "15": 237, "16": 247, "17": 258, "18": 269, "19": 280, "20": 294, "21": 309, "22": 323, "23": 340, "24": 349, "25": 362, "26": 385, "27": 401, "28": 414, "29": 433, "30": 447, "31": 459, "32": 474, "33": 485, "34": 494, "35": 513, "36": 530, "37": 542, "38": 559, "39": 568, "40": 579, "41": 609, "42": 625, "43": 637, "44": 648, "45": 667, "46": 681, "47": 696, "48": 712, "49": 726, "50": 733, "51": 748, "52": 766, "53": 779, "54": 791, "55": 804, "56": 820, "57": 831, "58": 846, "59": 862, "60": 877, "61": 898, "62": 906, "63": 922, "64": 940, "65": 956, "66": 972, "67": 989, "68": 1003, "69": 1018, "70": 1030, "71": 1044, "72": 1057, "73": 1070, "74": 1081, "75": 1095, "76": 1106, "77": 1124, "78": 1149, "79": 1164, "80": 1182, "81": 1194, "82": 1210, "83": 1235, "84": 1256, "85": 1268, "86": 1279, "87": 1290, "88": 1304, "89": 1324, "90": 1339, "91": 1352, "92": 1364, "93": 1374}
---

**Dave Jones:** Hi, it's part two, repair time here of this Compaq IBM well, the world's first IBM PC compatible machine. It's the Compaq portable dates from 1984 and I'll link in the video up here somewhere and down below and at the end if you haven't seen it.

**Dave Jones:** Anyway, we were debugging this thing and we got down to the point where the processor was actually reset. So, we actually traced the problem down to the basically the 8088 processor was permanently in reset and the reset comes from the 8284 clock driver chip here.

**Dave Jones:** This is the main 14.31818 megahertz clock that is divided by this to give you the 4.77 meg in here as well as other stuff and the reset comes from here and the reset pin that one there actually came from the power good signal from the power supply over here which is in the bottom of the case.

**Dave Jones:** So, that's what's stopping the processor from powering up. The rails, the 5 volt rail, 12 volt rail seemed okay, but apparently there is a power good signal coming from it was the second pin here on the power supply connector.

**Dave Jones:** It was coming from in here. So, let's get this power supply board out and have a squeeze now. It uses just these I have to take the mains input out here.

**Dave Jones:** That's actually welded soldered shut actually that thing. So, it's probably just got a filter in it or something like that. Hopefully no refer caps that have blown up, but anyway, mains does get in and it does have these little clips here which then could the board can slide out, but it can only do that if you actually take off not sure if you're going to be able

**Dave Jones:** to see it in there. Right down the bottom there in that corner. Focus you bastard. There it is. This little metal springy clip that I had to undo, which like it's like a locking pin or something like that that locks the whole power supply in place.

**Dave Jones:** It's rather, you know, it's a clever and nice, but bloody annoying. Anyway, we should now be able to slide this supply out. These connectors, I can't damn well get them off.

**Dave Jones:** They're really hard, but anyway, that's the plan cuz everything else in this machine sort of slid out. Everything's designed to be modular in this machine, but they kind of like didn't implement it very well.

**Dave Jones:** Everything I tried to get out of this had some kludge to it, and it was clunky to get out, and I didn't like it. Anyway, I'll get back to you.

**Dave Jones:** It does come out somehow. There we have it. There's our boards still attached to the umbilicals, but at least we can get in here and have a visual inspection cuz the first thing you want to do, well, first thing you want to do is smell it, of course, but visual inspection, make sure any of the caps aren't failed because tag tantalums like these ones here and these ones here, these are all tag

**Dave Jones:** tantalums down down here as well, absolutely famous for catching on fire, and one of them actually did when I switched this on. It blew up. I'll see the previous video for that, but not on this power supply did it.

**Dave Jones:** On the disk controller card. But anyway, we've got electrolytic caps, and they all look really good. They've got the vents on top. None of those are bulging. Nothing fancy going on there at all.

**Dave Jones:** I mean, you know, could be a ripple thing or something like that. They could have certainly dried out and have not died yet, but so they're mark 'em jobs.

**Dave Jones:** The orange ones, not sure, but the silver ones are Sprague, made in USA. They'll be fine. But no, of course, if you were actually refurbishing this thing and you were serious about, you know, having this thing work for any sort of extended period of time, you would recap absolutely everything.

**Dave Jones:** All the electros, all the tag channels. And I didn't actually notice that before. The silk screen would have been handy if they put on the other side, but the silk screen's buried under here.

**Dave Jones:** Sure enough that second pin is PG or power good and that's the one that's low. It's active low and that's what's causing our processor to reset. But there's other rails.

**Dave Jones:** I've only remeasured the plus five and plus 12 which are fine, but we've also got minus five as well and minus 12. But they're not needed for the processor.

**Dave Jones:** But if the power supply of course has any sort of you know, sensing stuff it likely does to check the power rails. So even if the negative five volt is buggered, then it's going to just reset the processor.

**Dave Jones:** Even though the processor doesn't need the negative five volts. So, you know, better safe than sorry I guess. It's just really annoying. I mean, we can override that. We could simply lift the pin, the second pin on there and power this thing up and see if it boots I guess.

**Dave Jones:** There's the back side of the board there. It's a little bit crusty. So, I'll get in there with some high so propyl and uh clean that up. But you know, you might look for dry joints, you know, thermal cracked joints.

**Dave Jones:** Actually, you know, thermal expansion of the parts as they power off and on over the years and that can cause problems particularly on like things like you know, the TO3 power transistors and stuff like that.

**Dave Jones:** So, you want to get in there with a little jeweler's loop or a microscope and just uh inspect all those. And if you're wondering what I use to have a look at things like this that I can't take over to say my Mantis or my Tagarno microscope, I just use my times 10 macro lens.

**Dave Jones:** This is an Opteka. This is what all my close up shots that you see, I just screw this on the front of my camera and bingo, it gives me my close-up shots like that.

**Dave Jones:** But, you can actually just hold this near it and you can actually get Look, you can get like really good close-ups like that. It's You know, it's it's really quite nice.

**Dave Jones:** Highly recommend it. And sure enough, you can see what looks like possibly a cracked joint there. It's like on the nut that holds the TO3 in place. And the other one up there looks like it's maybe something similar, but I actually measured those and they seem fine, but that could be a potential intermittent source.

**Dave Jones:** Uh so, you'd want to resolder those as a minimum. So, I just powered it back up and of course the 5 and 12 V rails work, but sure enough, 1 2 3 4 5 pin number five or fifth one from the end, that's supposed to be -5 V and -12 V is not there either.

**Dave Jones:** So, yeah, both negative rails gonski. Um and that's why power good is not coming on. So, we have to look at the negative rails and here's where it gets like really annoying.

**Dave Jones:** Um they're in here. Um so, and it's like just populated with all these physically tall and dense parts. These are probably the output filter caps for it. The LM338 there, that is a positive voltage regulator.

**Dave Jones:** So, that's almost certainly not the negative rail there, but yeah, little switching jobby in there perhaps for the negative rail. So, it's just really annoying from an access point of view.

**Dave Jones:** And as always with Murphy, if you have a look, the fifth pin down there, that's actually the -5 V which I'm trying to trace. And of course, it doesn't go on the neck bottom, does it?

**Dave Jones:** So, you can't see where it's going to and I can barely see down in there. So, actually before I muck around on the power supply, I thought I'd actually power this board up with the bench supply and then just start change the reset pin.

**Dave Jones:** So, I've got it hooked up to the bench supply here. I'm only generating the 5 volts and 12 volts. In fact, probably don't even need to generate 12 volts and by looks of this, I've turned it's on at the moment.

**Dave Jones:** The 12 volts is drawing nothing. So, like the minus 5 and stuff like that is not really needed for just getting the processor and stuff like that working, I believe.

**Dave Jones:** Anyway, it is drawing 1.6 amps here and if I actually reset it, put that to ground, 1.519 and switch it on, 1.577. So, it draws a little bit more power when it's going, but anyway, let's measure some clock, shall we?

**Dave Jones:** There's a reset pin. It's low. There's our clock pin. That's uh that'll be 4. Yeah, 4.77 megahertz. There it is. Yeah, no wuckers. And let's look at some bus activity, shall we?

**Dave Jones:** It's just randomly, yep. That looks like bus activity. Bus activity. More bus activity. Uh whatever that pin is. Sorry, I can't remember all the pin outs off the top of my head.

**Dave Jones:** But yeah, this looks like classic bus activity. So, it's certainly doing something. So, what I'm going to do now is plug in the video card in here cuz it shouldn't Well, the video card might need the positive and negative rails.

**Dave Jones:** Anyway, let's just plug it in and see what's what. All right, there we go. I've plugged it in. Haven't hooked up monitor yet, but we're getting significantly more current draw.

**Dave Jones:** Look at that. The video card's drawing huge amounts. I mean, I like we're now 4 amps. Uh that's just nuts. Drawing a lot more than the processor is, and we're drawing something on the 12 volts.

**Dave Jones:** And I'll switch it on. And getting an absolutely nothing on the video output there. So, zippity-doo-dah. Okay, we're still getting bus activity there. That's a processor bus activity. So, it's not like it's being loaded down or anything like that, but we're certainly getting nothing on the video out, but I don't have those other rails, so that could be it.

**Dave Jones:** Okay, I've got uh minus five here. And minus five's drawing nothing. Zip. Okay, I got uh minus 12 as well, so I've got all four rails there. Just set them to nominal like half amp current limit, whatever.

**Dave Jones:** So, whoa. Now we're going in the current limit. Negative rail there. Oh, no. No, there we go. No, it's good. Maybe that was just a power on thing. So, reset it.

**Dave Jones:** Cuz I don't have a power on reset. So, they're both drawing zero. Negative five and negative 12, so and I'm getting nothing on the video, so that's still not going to help me.

**Dave Jones:** Even if I fix my main power supply, um it's pointless because um this thing, while the processor's working, the video's not. So, once again, like as I said, uh I'm not sure if you have to make me set some jumpers or something to get a composite video out.

**Dave Jones:** Maybe I can check uh some of the RGB uh out here, perhaps. Okay, I've no idea which pin's what. Hello. That looks like a sync. That's definitely synchy. There we go.

**Dave Jones:** Yep. Whoa. That's 50 hertz. Yeah, getting stuff. There you go. 18 18 and 1/2 kilohertz. That certainly looks like the horizontal. Okay, it looks like we are getting horizontal and vertical sync there.

**Dave Jones:** There we go. We're getting something in there. That looks maybe like some video data. Probably only one color because that's all you need. When you boot up, you probably just getting like a text, you know, a monochrome like one color text image.

**Dave Jones:** So, that sort of makes sense. So, it looks like that works. So, this uh I think this machine's working. Um and if we actually hooked up the CRT, but I've got to put all the boards back in, I think, to get all the CRT working again.

**Dave Jones:** It'd be a mess to try and do that outside of the case, I think. So, yeah, that's a bit tricky. I wish I could get that damn composite working.

**Dave Jones:** And by the way, kids, don't try this at home. I'm a professional. Now, apparently, uh DIP switch five and six on the main board here, these actually set the uh startup video mode.

**Dave Jones:** And it's currently set to uh CGA 80-column mode. So, that's interesting. I might try MDA, which is both of them off. So, I will do that and repower. Okay, I'm getting the same horizontal and vertical there.

**Dave Jones:** So, 18 and 1/2 K, but that data does look significantly different. It was less populated before, but I'm still getting no composite output signal at all. Now, here's something interesting.

**Dave Jones:** I was just playing around with measuring the signals again because I've got a uh capture card, which we'll talk about in a minute. But, I'm using the case of the uh composite output connector here as ground.

**Dave Jones:** And I was using that uh before to actually probe. But, now, if I actually probe these signals, let me just do a a resetty. Let's actually probe these signals again.

**Dave Jones:** Look at this. See how it's just dropping down there? It's got some 50 hertz crap, all sorts of stuff on there. Right? Look at that. You see? And then it's just it's just dropping down and down and here's a sync.

**Dave Jones:** See? Look at that. It's just going down and down and down and down. Now, what when you see a signal like that and look it's just rising up. When you see a signal like that, that's indicative that the ground is actually doing nothing.

**Dave Jones:** So, if I disconnect the ground and measure that again, you'll see it's doing the same thing, right? So, our ground is Why is that no longer grounded? Uh Beulah?

**Dave Jones:** Beulah? So, if I actually measure that compared to what I know is a ground pin here, it it's just not connected. It is not connected at all. That is like what?

**Dave Jones:** What the? It what I I swear it was before. That's why I used it. I would have measured it. It's actually been some quite some time since I shot this video because I just acquired a um CGA uh to V VGA uh converter card and I was just about to hook up all the signals.

**Dave Jones:** I was determining where the signals were and I what? And sure enough, if I measure it um this bracket and of course which is electrically connected uh to the ground of the composite connector and also to the shell of the uh CGA output connector, then uh yeah, I'm getting like um nothing.

**Dave Jones:** It's just like like 40, 50 meg, something like that and then it is sort of like goes open compared to ground. So, I have no idea how I was measuring those signals before.

**Dave Jones:** Has been a couple of weeks, but I got like I don't know. Um I scratching my head. Anyway, um what I did is went and ordered a uh CGA and EGA and YUV to VGA converter and this is actually uh quite nice.

**Dave Jones:** It's got the VGA in, it's got uh the component in as well, and it should be able to do the CGA, hopefully. Um and and it's got a very came with a very nice little cable, which then I've uh connected up to uh pin headers here, so I can just slide these on.

**Dave Jones:** Got to uh find which pins is what again. I know that that one's ground as in 5-V ground. I've buzzed that one out. Um uh so I'll just uh remeasure that now using that as the ground pin, and uh anyway, yeah, we'll get these signals and we'll see if we can get a uh CGA output signal from this thing.

**Dave Jones:** Actually, it's a really quite frustrating that there's no really easy ground points on this thing that you can just hook your scope probe up to, um you know, without danger of you know, you can go on to maybe one of the pins of a tag tent or something like that.

**Dave Jones:** You know, that's why um you know, you generally like pick a uh ground connector like a you know, a a bracket like that. So, when you're designing boards like this, just make sure you include like a a nice handy ground reference loop or pin or something.

**Dave Jones:** Er. Unfortunately, I'm getting zippity-do-dar on this. No signal. Um so, I've got to muck around with this thing, but the menu um yeah, I can't make heads or tails out of that.

**Dave Jones:** I might need a cheat sheet, so we'll see. Um there is an auto button. Maybe I can press and hold auto or something. I don't know. I I am getting I'm getting horizontal sync, vertical sync, and I'm getting something on the green signal.

**Dave Jones:** So, yeah, I don't know. There's some adjustment pots in there, maybe. Bugger, I just read the manual for this thing um or the specs on the eBay or whatever, and it tells me that it's only 14 and 1/2 kHz to 16 and 1/2 kHz.

**Dave Jones:** We've got 18 and 1/2 kHz here. D'oh! Winner, winner, chicken dinner, green screen, and oh, I had to change the mode of the board to RGB-S. Um, and that worked a treat.

**Dave Jones:** So, there it is. Um, I don't know what these are okay. I assume they're Erica's 301, 401, 601. Um, you know, we've got nothing and course there's diskette error, but this thing works.

**Dave Jones:** There you go. It boots. Woohoo! Winner, winner, chicken dinner. Um, that well, as you'd expect because we were seeing video signals there. So, yeah, no worries. But, hold on to your hat.

**Dave Jones:** If I use the ground down on this board and I probe our composite output we now have a signal. Why weren't we getting a composite signal before? Look at that.

**Dave Jones:** That is going to work a treat. So, if I hook this monitor back up to the composite out, I have no doubt that it'll work. What the Whoa! Glitch in the matrix there.

**Dave Jones:** So, I just change this back to AV here and let's see if we Oh, yeah, it's not as good, is it? It really doesn't like that. Uh, that's yucky.

**Dave Jones:** Yucky, yucky. Um, so, yeah, modern monitors, they're probably not very good at this sort of thing. Meh, who knows? But, uh, yeah, that's working a treat. And as we, uh, saw before, it doesn't take any power on the, uh, minus five and minus 12 volt rails.

**Dave Jones:** So, really, to get this thing to boot, um, I don't even need to fix that power supply, uh, in this thing. All I need to do is force that or break into that line, force it, uh, high, and that power good line, force it high, and assuming that all the CRT circuitry and everything works, it'll it should just work a treat or at least the composite output will work and we'll be able to

**Dave Jones:** see that. At least we can read it, I guess. Okay, I think the reason that the composite is working now is because I have been mucking around with these dip switch settings and I which changes the graphics modes and I think there's only one that seems to work.

**Dave Jones:** Oh, okay. It just takes some time to boot. Let me uh Let me show you that. Go like that and there's no composite output for quite some time at time this puppy.

**Dave Jones:** Come on. You can do it and it will eventually get there. I believe or it did last time. So, come on. So, maybe I was a bit too impatient before about checking for video signals.

**Dave Jones:** There we go. Yeah, it eventually just pops up. Yep. So, I you know, it's going through memory checks or something like that before it displays any before it even enables like the video signal's not even enabled until literally the text pops up.

**Dave Jones:** So, there's no sync there. There's no nothing. Okay, I've confirmed that the only mode that actually seems to work is dip switch five off and six on which is I believe CGA 40 column mode and that's the only one that will give me the composite output and work with this CGA to VGA converter card as well.

**Dave Jones:** So, anyway, I'm going to leave it set to that. So, that at least gives me a baseline to get this puppy up and running from now on. But really, I didn't have any doubt that the board would have worked cuz I found with these vintage computers like just you know, when you're talking about like TTL stuff unless you have an exploded tantalum cap like we had in the first

**Dave Jones:** video, something like that. Really, the you know, the silicon's actually quite robust and you know, even after all this time the mask ROM uh still works. You know, that's all just fine and everything's hunky-dory.

**Dave Jones:** The RAM in it still works and everything's hunky-dory. So, um yeah, I might have to look at I'll look up those codes, but anyway, like the thing works, the processor works, everything all the video card works.

**Dave Jones:** And yeah, everything's sweet. So, no real surprise. I knew I I was pretty confident. You know, I was like 90% confident when I get this board out and power it up from a bench supply, it'll probably boot.

**Dave Jones:** And sure enough. So, there you go. I'm going to leave this video at that cuz I've run out of time today. I will do the power supply troubleshooting another day, but we at least got this puppy up and running using the external um monitor output here.

**Dave Jones:** And I have checked there are signals on the CJ monitor CJ connector as well. So, I should be able to you know, if I assemble the thing and the CRT doesn't work and I can't get that working or I don't want to get it working, I can at least hook on an external monitor without having to you know, hack into the internal header connector here, but there you go.

**Dave Jones:** I hope you like that. Um so, yeah, I've got so two more unknowns as well. I definitely know the power supply is faulty. So, I need to fix the power supply, but as I said, like the minus 5-V and minus 12-V rails on here draw absolutely nothing.

**Dave Jones:** So, in terms of getting this thing working, unless you want to use like a serial port or something like that, maybe where it might use that those voltages. I don't you know, all of the disk drives and stuff like that.

**Dave Jones:** Uh possibly and also the CRT as well. They may only be for the CRT. So, you know, who knows, but yeah, so to get the So, probably to test the CRT, I reckon I'm probably going to need to fix the power supply first.

**Dave Jones:** So, that needs to be the next step and then check to see if the CRT works and get this whole thing restored eventually. It's one of those time things.

**Dave Jones:** Anyway, that's it for today. So, if you liked it, please give it a big thumbs up. As always, discuss down below. Catch you next time.
