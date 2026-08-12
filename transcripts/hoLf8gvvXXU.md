---
video_id: hoLf8gvvXXU
title: EEVblog #997 - How To Solder Surface Mount Components
url: https://www.youtube.com/watch?v=hoLf8gvvXXU
source: youtube-asr
timestamps: {"0": 0, "1": 12, "2": 26, "3": 42, "4": 52, "5": 59, "6": 68, "7": 80, "8": 86, "9": 96, "10": 105, "11": 124, "12": 136, "13": 147, "14": 161, "15": 175, "16": 190, "17": 201, "18": 212, "19": 224, "20": 235, "21": 246, "22": 263, "23": 277, "24": 296, "25": 305, "26": 314, "27": 327, "28": 334, "29": 352, "30": 365, "31": 374, "32": 386, "33": 397, "34": 407, "35": 418, "36": 429, "37": 436, "38": 452, "39": 463, "40": 474, "41": 486, "42": 496, "43": 506, "44": 516, "45": 528, "46": 539, "47": 549, "48": 557, "49": 566, "50": 584, "51": 594, "52": 615, "53": 622, "54": 643, "55": 655, "56": 674, "57": 687, "58": 697, "59": 703, "60": 715, "61": 728, "62": 739, "63": 750, "64": 767, "65": 783, "66": 808, "67": 829, "68": 838, "69": 852, "70": 861, "71": 870, "72": 886, "73": 901, "74": 908, "75": 928, "76": 941, "77": 951, "78": 981, "79": 992, "80": 1004, "81": 1017, "82": 1029}
---

**Dave Jones:** Hi, time for another installment in the Nixie tube design video. We've received our PCBs from Elecrow. So, we'll just take a quick look at this before we actually assemble it.

**Dave Jones:** I got a 48-hour turnaround on these. I think they made it. I ordered them on the 1st and they packed them on the 2nd. So, I think they made them within 48 hours, but I don't think they actually shipped within the 48 hours.

**Dave Jones:** So, I'm not sure what the deal is. I think it was a day out or something like that. Anyway, they they did reasonably well, I guess. And considering that it was like 50 bucks or something and they sent me five, but I actually got about seven, I think.

**Dave Jones:** So, yeah, they just made a few more. And this is larger than your average little Arduino shield or something like that. What is it? Like three times, two and a half times the size of that?

**Dave Jones:** So, it's pretty darn good for the price. Just know the board is not warped. That's the camera on my That's the lens on my Takagi microscope at that particular zoom level.

**Dave Jones:** So, it looks Trust me, it is actually square. So, let's go in and take a look at it. The first thing is that yes, I ordered red solder mask.

**Dave Jones:** I got red solder mask. I didn't order gold plate, so that's why it's just solder um coat. And there there are no stupid manufacturer markings on the silk screen or anything like that.

**Dave Jones:** They haven't added their own code. I don't think there was an option to disable that. They just haven't done it and that's great. I hate manufacturers who actually do that.

**Dave Jones:** It's really freaking annoying. Well, let's have a look at the silk screen first. To my eye, it doesn't look like it's dot matrix printed, but of course it is.

**Dave Jones:** All your most of your low-cost services like that are and you can see the individual dots and it's quite good. I don't know about the alignment on that. It looks okay.

**Dave Jones:** Maybe that one doesn't slightly line up, so maybe there's a slight offset on the silk screen there, but for a prototype board, it's all fine and dandy. It's not a photo imageable solder mask, which is the other type, which is uh usually a bit more you know, you get on your more expensive boards and it's not not dot matrix printed.

**Dave Jones:** You just see like thick outlines like you would on the traces. So, if we have a look at the solder mask expansion here, I I'm not going to go in there with my microscope and actually measure it and all that sort of stuff.

**Dave Jones:** The alignment of the solder mask is pretty good around the pad there. You can see there's a slight offset there, but really no big idea. I can't remember what the solder mask expansion was.

**Dave Jones:** It's That's certainly more than acceptable for a prototype. No worries whatsoever, but they haven't expanded the solder mask, so you get it like a thin sliver through there. So, they've done That is fine and dandy.

**Dave Jones:** Let's have a look at some of the via holes, shall we? Where That's good alignment of the hole based on the annular ring around there. It's almost perfect. And it's always hard to see the plating inside holes, but there it is.

**Dave Jones:** It does look uh quite reasonable. Yeah, no worries whatsoever on that. That looks like very smooth and consistent, but yeah, like you'd have to do a cross-sectional analysis. Of course, this is not a professional PCB.

**Dave Jones:** Usually uh the good manufacturers do send you a cross-sectional cut um through the vias and stuff like that, so you can see the plating uh consistency. But everything looks nice and clean.

**Dave Jones:** There's no There's no dag. There's no silk screen dags on there. There's no you know, contamination of the board or anything like that. It looks quite good. So, I'm happy with that.

**Dave Jones:** That is certainly a pass on the Elecrow board. No worries. All right, so let's start out by soldering. What you're going to want to do here is always solder your low-profile stuff first.

**Dave Jones:** So, all your surface-mount stuff, all your surface-mount chips, all your surface-mount regulators and capacitors and all sorts of stuff other stuff. These through hole ones don't put those in.

**Dave Jones:** Definitely don't put the sockets for the Nixie tube. Why? Because you can lay your board flat on the bench like this and it doesn't, you know, it doesn't rock because you got pins sticking out the bottom or anything like that.

**Dave Jones:** Big trap for young players. You're pretty you learn that pretty quickly that it's just nicer to solder all the surface mount stuff first and also you can get in there with your iron of course without these big components blocking access to pins and something like that.

**Dave Jones:** And certainly something like this where you've got a big, you know, axial resistor right next to a SO type package here. You would definitely want to do the SO package first so you can get in there and wipe across the pins and solder those pins on the chip.

**Dave Jones:** So yeah, definitely do all SMDs first. Golden rule. Just checking that my chip matches the footprint. Yep, very nice cuz we did actually goof that in the original layout and had to do a redo but I chose the narrow width SO package and this is the 7 1/2 mm wide one.

**Dave Jones:** So that's spot on. Let's go. And we're going to be using lead free stuff. Do they none of that lead rubbish? No, I am a lead fan boy solder.

**Dave Jones:** Anyway, it's important to use very fine stuff. I've got 0.38 mm stuff. You don't necessarily have to go this low but anything under 0.5 mm is what you got.

**Dave Jones:** It's got a five core flux genuine multicore brand the choice of champions. And so we'll give it a go. So that means the five core of course means it's actually got five cores of flux in there.

**Dave Jones:** If you got that under the microscope you might be able to see it. And the good thing about the fine solder is that it allows you to feed in a small amount of solder onto the joint.

**Dave Jones:** You don't want too much. That causes too many issues with soldering. A lot of people wonder why their soldering sucks when other people do it so well. It's because you use fine solder you control the amount of solder that you put onto the joint, and that's a big deal for surface mount stuff.

**Dave Jones:** You want the fine stuff, 0.5 mm or under, trust me. Next thing we're going to need is some flux. I've got this old Electrolube flux pen. I'm a big fan of the flux pen, so we'll just put some flux on there like that.

**Dave Jones:** We'll put some more over the top in a sec, but you just want a layer a base layer down like that, so it's under the pin. So, the first thing we're going to want to do is just tack down the corner pin.

**Dave Jones:** So, we just want to feed a bit of solder under that pin there, and then we can place it. So, there we go. And we can do the pin on the other side as well like that.

**Dave Jones:** So, the chip is held in place, so now we can do our drag soldering. So, we just put a little bit more flux there and there just to coat the pins.

**Dave Jones:** You can never have too much flux. Okay, now what I've got on my JBC iron here is a little well tip. You can see the little hole in the bottom, and there's actually we can put some solder on that.

**Dave Jones:** Now, normally you don't want to put solder onto your iron cuz you can see all the flux burning off there, right? That's normally a bad thing, but we've got additional flux on there, so it's going to be okay.

**Dave Jones:** And these well-based ones are designed for drag soldering like this cuz they sort of drag the solder back out like sort of suck it back out of the joint as you're putting it on.

**Dave Jones:** So, it's easier to control the amount of solder that goes onto the joint. Now, I haven't actually used this one before. This tip is brand new, and I haven't practiced with this.

**Dave Jones:** I think it's on the small side, but I'm going to give it a go. So, this could end very badly. So, I've got our solder on there. And we just want to literally drag it across like that.

**Dave Jones:** And that ended badly on the first couple of pins, but we can just get that off there, clean it up a bit, and we should find maybe that second last one hasn't got much on there.

**Dave Jones:** So, we'll just add a bit more solder. You see how the solder just flowed onto there? That one's got a bit bit too much. It's a bit how you doing.

**Dave Jones:** But our well base tip will be able to suck that back out. But ordinarily, you know, once you get this right, then you just literally just one drag across should do the trick.

**Dave Jones:** And just to show you that you don't need one of those well base tips. So, I've got my huge, which is my general purpose uh iron that I use pretty much for everything.

**Dave Jones:** A big chisel is one of my big recommendations for soldering, even for surface mount, believe it or not. So, let's try and do drag soldering like this. Just put some solder on there.

**Dave Jones:** I'll put some flux back on the pins, of course. I've tacked down the two corner pins. I've got some solder on the bottom there. Probably should put a bit more, but let's let's give this a whirl, shall we?

**Dave Jones:** See? Drag it across like that. And Bob's your uncle. There's a little bit of a dag in there. Yeah, you don't need a well base tip. And by the way, that ugly stuff you can see, that's just all gunk and flux residue.

**Dave Jones:** That'll clean up in the wash. Jeez, the alignment of that chip's a bit how you doing, isn't it? Well, let's uh not worry about that. Drag along and we can do this.

**Dave Jones:** I'm doing it a bit slower. You can do it fast, of course. Look at that. Beautiful. Well, you know, a couple of little solder dags in there, but you know, you tidy them up if you want.

**Dave Jones:** But generally, you don't have to. They're not going to short out anything. And if you're not a fan of drag soldering, that's all right. You don't have to do drag soldering.

**Dave Jones:** You've already seen me do this before. It's the I don't know whether or not has an official name, but it's the dab method. And I I rather like this is cuz it's very controlled.

**Dave Jones:** You don't you can't accidentally put any excess force on the pins, really. And the solder just flows into each individual pin like that off the tip of the iron, and just the right amount that you happen to need to do a nice fillet.

**Dave Jones:** It's not hard to do uh good SMD soldering at all. So, there's the result of that dab method there, and that is beautiful. Just enough solder to form a very nice fillet on those pads there.

**Dave Jones:** So, let's do one in real time, shall we? Put some flux down there. Put our tin our pad there. Whack our chip on. Make sure you've got it around the right way.

**Dave Jones:** You can use tweezers for this, or do it by hand. It doesn't matter. Ah, put a bit too much solder in I solder on there. It's a bit how you doing, isn't it?

**Dave Jones:** The alignment's not terrific on that. But, we'll run with dab. There we go. And now we're ready Oh. Sorry. Just to make it easier, because these chips, especially older ones, they got oxide oxidization on the pins and everything.

**Dave Jones:** So, that's what the flux is really good for. It just gets right through that rubbish, and uh All right. And then we I won't do drag. I'll just go dab dab dab dab.

**Dave Jones:** Look at this. Beautiful. Thing of beauty joy forever. I deliberately missed that one, so cuz I knew the solder would wick down there. But, there you go. We're getting there.

**Dave Jones:** We could do once again, we could save a few seconds by doing uh True. Ah, just I didn't I haven't got my fume extractor, because it will uh cause too much noise here.

**Dave Jones:** So, but look at this. All right, I'm using like what is it? That's a 2 1/2 mm tip or whatever. No worries, beautiful. How long did that take? Anyone timing?

**Dave Jones:** Now, it's just a little tip. What I would do here just to be more efficient when you got a lot of chips like this is to sort of batch the process.

**Dave Jones:** So, I've like gone and fluxed all of those pins and then I've gone and dabbed some solder on to the corner pin there and then I'll go put them in place.

**Dave Jones:** So, I'll get multiple chips go bang bang bang bang bang and then I'll go drag solder the whole lot and it ends up being a little bit more efficient and quicker.

**Dave Jones:** And of course, if you don't have a flux pen, then you can always get in there and do it the old-fashioned way and use the multi-core inside your solder like that.

**Dave Jones:** So, just apply your iron down there and apply the solder to the joint. This is where your 0.38 mm solder comes in real handy. Try doing that with 1 mm solder and see how you get on.

**Dave Jones:** Something like this sot223, I would uh get in there and once again, solder the pin first just to put it in place. So, I put that in place and I don't have to use flux for this one.

**Dave Jones:** Doesn't matter because we can get in there with our individual with our Whoop. Hello. Yep, that's what you get when you look at the screen. You don't get that three-dimensional view of what's happening there.

**Dave Jones:** Viewing the screen instead of viewing the object. And then we go in and solder our tag. Thank you very much. There we go. Nicely done. And with surface mount passives, of course, you want to just dab one pad like that and Whoop.

**Dave Jones:** Dip it in place. Yes, it is the wrong size. I'm you I'm putting an 0603 on an 0805 pad, but meh, she'll be right. By the way, when you're trimming component legs, don't go in there flush, like like completely flat with the board like that, because you just put uh likely stress on the solder joint.

**Dave Jones:** Haven't got much of a fillet on here, but generally just go in there and then just tilt it. Just a just a wee tad like that, and Bob's your uncle.

**Dave Jones:** And it doesn't matter how good a digital microscope you have, multi-thousand-dollar Tagarno one, uh-uh, nothing beats a good uh stereoscopic uh microscope like the Mantis here. You can get in there for visual inspection.

**Dave Jones:** Fantastic. Can't be beat. Now, as for the Nixie tubes here, I'm not going to just solder them uh straight in. That's a bad idea, because these things are uh you know, you might want to replace them.

**Dave Jones:** Uh they're fragile, etc., etc. So, you know, the best thing to do is use these sockets. I just bought these on eBay. They are specifically designed for Nixie tube sockets.

**Dave Jones:** I some Nixie tube store that sells all Nixie tube parts. Fantastic. They cost uh a bugger all, and uh they've got two levels. Okay, there's our pin. You can either have like the thin pin that go like that and just stop, but I actually drilled the hole.

**Dave Jones:** Let's try it. DOES IT FIT? AH! BEAUTIFUL. LOOK AT THAT. There's hardly any wiggle in that at all. So, I've got the drill size right, and so you can sit it in like that, or you can leave it off like that.

**Dave Jones:** If you drill a smaller hole, it'll just stop there, but of course, then you're probably going to get a little bit more wiggle on that. It's better to stick it straight in.

**Dave Jones:** So, that's really very nice. So, I'll just go around and solder all those in. Beauty. And just a little uh trap for young players, by the way, if you've got a mat that is um uh you know, that can easily burn, You shouldn't you know, cuz this one is one of these proper rubberized ones designed for taking heat on it.

**Dave Jones:** Of course, the heat will transfer these pins through these pins very easily when you actually go to solder them. So you know, the other end will instantly get almost as hot as what the joint is.

**Dave Jones:** So just be careful that anything under anything under the bottom doesn't burn. And of course, if you don't want the wretched things to fall out, you can just solder them under the top.

**Dave Jones:** Look at that. No worries. Check it out. Starting to look pretty schmick, isn't it? Yep. Look at that. Beautiful. And behold the completed module. Check it out. Isn't it beautiful?

**Dave Jones:** We've got our WeMos D1 module on the back, our pile of poo high voltage module, and yes, I have actually powered it up and it does do the business.

**Dave Jones:** But I've got to program the thing. So yeah, I can power it up, but it doesn't display anything, but it regulates and everything's hunky-dory. It generates the 160 volts on the tubes.

**Dave Jones:** Yes, I know that might have been a bit boring, but hopefully you learned something. I added a bit in there on SMD assembly and stuff like that soldering. So yeah, it's soldering a board together.

**Dave Jones:** It's just another part of the video step by step for this thing. And yes, so we'll have to do a future video on powering that up, programming the module, and getting it working into its final application.

**Dave Jones:** So if you liked it, please give it a big thumbs up. And as always, discuss down below. Catch you next time.
