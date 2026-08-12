---
video_id: qyDRHI4YeMI
title: EEVblog #415 - SMD Stencil Reflow Soldering Tutorial
url: https://www.youtube.com/watch?v=qyDRHI4YeMI
source: youtube-asr
timestamps: {"0": 1, "1": 38, "2": 71, "3": 92, "4": 111, "5": 142, "6": 155, "7": 183, "8": 207, "9": 222, "10": 244, "11": 277, "12": 312, "13": 339, "14": 372, "15": 411, "16": 436, "17": 468, "18": 491, "19": 516, "20": 544, "21": 565, "22": 596, "23": 619, "24": 649, "25": 680, "26": 707, "27": 724, "28": 738, "29": 762, "30": 785, "31": 810, "32": 836, "33": 869, "34": 885, "35": 914, "36": 931, "37": 955, "38": 989, "39": 1021, "40": 1056, "41": 1085, "42": 1105, "43": 1127, "44": 1163, "45": 1179, "46": 1201, "47": 1227, "48": 1256, "49": 1273, "50": 1303, "51": 1336, "52": 1359, "53": 1380, "54": 1416, "55": 1449, "56": 1467, "57": 1489, "58": 1512, "59": 1540, "60": 1571, "61": 1599, "62": 1635, "63": 1669, "64": 1685, "65": 1713, "66": 1729, "67": 1749, "68": 1775, "69": 1804, "70": 1829, "71": 1847}
---

**Dave Jones:** Hi, in this episode I'm going to show you how to do-it-yourself reflow stencil solder a PCB. And I got this one from the mailbag sometime back. If you haven't seen it, it's based on Vincent Himpe's book Mastering Surface Mount Technology. This is where they part of the Electrolab Works series. This is where the PCB comes from and it's a ring light for cameras. And we're going to reflow solder all of the parts on here using a solder paste stencil. This is a quite a high-quality stainless steel stencil.

**Dave Jones:** Now, you don't necessarily have to get a stainless steel one if you're doing it yourself. In fact, they're probably prohibitively expensive, but there's a lot of companies out there today that will laser cut you a a Mylar or a Kapton solder paste stencil direct from the file in your CAD package. It can generate the paste stencil. And that's a whole video in its own right, but I'm going to show you how to do that using some basic solder paste and a hot air reflow gun. And we're going to have a go

**Dave Jones:** at reflowing the parts on here after we apply the solder paste with a stencil. So, let's give it a go. And the solder paste I'm going to use today comes from Chemtools or Aim Solder here in Australia. And it's a 63% it's SN63, which stands for 63% tin and 37% lead.

**Dave Jones:** So, it's quite close to your regular 60/40 leaded solder. So, this is not lead-free solder. It's only 15 g, which doesn't sound like a lot, but you don't need much solder paste, as we'll see, to do one of these stencils on, you know, a fairly a fairly typical board like this.

**Dave Jones:** So, this one has been manufactured fairly recently. Now, the solder paste has a couple of issues. The first one is that it does have a shelf life. If you try and use it beyond that, well, its performance is not guaranteed. I mean, this one might have, say, 6 months. And if you use it in 12 months' time, it's probably still going to work, but you know, the performance is not guaranteed at all. Now, this one's in a syringe format because it comes with a little tip like

**Dave Jones:** this, which you can plug it on. You can use it as a syringe, and you can individually put paste on each pad like that. And you can even do it manually with a syringe, or you can get an air pump, which dispenses a paste dispenser.

**Dave Jones:** You can buy them on eBay fairly cheaply these days, 100 bucks or so, I think. Solder paste dispenser, and you can go around and manually dispense solder paste on each pad. But hey, that's time-consuming. You end up missing the pads. It's much quicker and simpler to use the solder paste stencil like this. So, all we're going to do is apply our solder paste on there, then we go over it with a squeegee like this, and we're going to apply all of our solder paste in there. And we lift it

**Dave Jones:** off, and we should be left with an even amount of solder paste on each one of our pads here. That's the plan. And then we place the parts, and then we will reflow the solder. The other problem with solder paste, of course, is that it must be kept in a fridge as well. It must be kept airtight, so you got to put the nozzle back on it in a fridge. And then, even then, it still has a shelf life.

**Dave Jones:** Now, when you go to use it like this, make sure you sit it in room temperature for a couple of hours. You don't want to apply it cold. It's not an issue that it's going to reflow incorrectly. It's just that it won't apply through the solder paste stencil very nicely.

**Dave Jones:** So, you really have to let it warm up to room temperature for a couple of hours first before you can use it. And when you done with it, make sure you put it airtight and put it back in the fridge. So, solder paste can be a bit annoying if you and a quite an expensive way to do it if you're just, you know, you want to do a one-off board, you're doing one or two boards a year, uh solder paste, you know, it may not be

**Dave Jones:** worth your while, but anyway, um we are going to give it a go. Now, the first thing you want to do is just inspect your solder paste stencil to make sure all of the holes are cut out. Now, it just so happens that this one here um hasn't. You can see that there's still one there that didn't punch out correctly. So, we're now left with all of our precisely cut pad-shaped holes there for the solder paste. Now, if you're really um you know, into high-volume uh manufacture mobile phones

**Dave Jones:** or something really high-density parts, very critical, very dense uh spacing, then the type of stencil you use, the thickness of your stencil, the uh exact type of solder paste, the exact angle that you apply the solder paste at, and uh the size of your paste pad uh holes and everything like that can become quite critical to um your final yield in volume production, but just for do-it-yourself stuff, uh it doesn't matter. This is a stainless steel stencil, more than good enough. It's about 150 microns uh thick. Doesn't

**Dave Jones:** matter. It's going to work whether you use like a you know, you just get one of those cheap laser-cut Mylar um or uh Kapton sheets or something like that. And next up, you're going to require uh a couple of PCBs the exact same thickness as the board you're doing. Of course, this is like a standard 1.6 mm board, so we've got two other 1.6 mm boards. This will hold this board in place and ensure that it just doesn't move around on the bench like that. So,

**Dave Jones:** we're going to put it down there. We're going to get some sticky tape. And you don't want any tape on the board itself on the board you're doing, especially if there isn't much room around the outside of the panel here because then when you apply your stencil on there, it may not sit very flat if there's some tape very close to the individual pads that you're doing. And next up, we're going to have to align our stencil over these pads. As you can see, it's uh

**Dave Jones:** it's fairly critical. There's not much movement in my fingers there. You can see how critical this would be if you were doing you know, a real you know, like a mobile phone with little 0201 components or something like that, real ultra-dense stuff, then the alignment of these stencils becomes a big deal. So, I'm going to I think that's right, so I'm going to apply some sticky tape on the outside of that, either side, and it's it's sitting fairly flat. The thing you don't want to do is have this warp

**Dave Jones:** during your paste application. For a do-it-yourself application like this though, it's really not that critical. You know, if you get a little bit of warpage in there, it's not a problem. Now, what we've got is a spatula here or it's sometimes called a squeegee or you know, it goes under various names in the industry. This one is not designed for this purpose. This is just one designed for cake mixing and things like that.

**Dave Jones:** It's a silicone rubber one and you know, it's it's not ideal for the purpose, but for just a do-it-yourself one-off like this, it's going to work just fine, I think. Ideally, you'd want a proper stainless steel spatula to apply. Now, the angle that you use on this can be reasonably critical. It may not matter just on a simple do-it-yourself one like this, but you know, if you use too shallow an angle like that, it can or too sharp an angle like that, then it can actually uh

**Dave Jones:** rip some of the solder paste back out of it. All right, now let's give it a go. Now, we shouldn't need a huge amount of solder paste at all. Let's just maybe put that much on there, perhaps. There we go, a little bit more. Now, let's get our squeegee in here and move it drag it across.

**Dave Jones:** Now, stencil like that, and make sure you get the right angle. Make sure there's no retraction in there. The sol- Oh, you can see that one. I think you can see that one just there. You can see some of the paste has retracted out of that one. Normally, you only have to like, you know, do this in one pass, usually. Don't be afraid to go back over existing pads.

**Dave Jones:** You can certainly do that. And I really, you know, this uh is not the best spatula at all, folks. I'm not happy with this. Um at all. I didn't have a metal one, so I've had to make do here.

**Dave Jones:** And there's a very good close-up of some uh solder retraction there. So, I'm just going to put a little bit more paste in there. And uh this uh paste I I may not have may still be a bit cold. I may not have let it uh warm up enough.

**Dave Jones:** Now, this isn't the world's best job, I'm afraid, cuz I usually don't uh do this. I'm I'm using uh new solder paste I haven't used before. I'm using a new spatula I haven't used before, so you know, really and I and I haven't um done any practice at all. So, this one this particular job is a little bit hit and miss, I'm afraid, but you get the idea. So, ordinarily, you know, if you've got your uh technique down uh pat, then you should be able to in

**Dave Jones:** theory uh do this in one pass of the uh spatula or the uh squeegee. If you got a super wide one, it can go right across the board, but um anyway, we just want to inspect. Make sure you inspect like the big ones are really obvious for the LEDs, but just inspect those little uh ones in there just to make sure that they're uh make sure that they're covered very carefully.

**Dave Jones:** Peel it off. And don't touch it and you should be left with a board with tada, solder paste on it. And there you have it. You can see the solder paste on the individual pads there. And of course, if you have a look in here, you can see some what looks like, you know, I like the solder paste has gotten between the pads, but don't worry about that. Your solder mask, that green stuff on your board there, is going to take care of that when that

**Dave Jones:** reflows. So, when you uh reflow that solder with the uh hot air gun, that they will not uh stay together and short. The solder will just start reflow into the well on the pad. Uh and uh it won't stick to the solder mask, so it shouldn't be a problem. If you actually miss one of the pads and it doesn't uh reflow, then well, really, that can ruin your day. So, it's worth spending 5 minutes just under a uh under a magnifying lamp going around inspecting everything. Now, as for placing parts,

**Dave Jones:** there is a uh couple of ways to do it. Of course, the fully automated way to do it is to use a pick and place machine, but we don't have one of those and you don't either, I'm sure, because that's why you're watching this video. So, the traditional way to do it is just a pair of surface mount tweezers, non-magnetic type. Make it Make sure you get a good high-quality pair, and you can individually place them one by one down like that. And the other way to do it is

**Dave Jones:** with one of these vacuum pick up tools. You can pick these up for, you know, 5 or 10 bucks, very cheap. They come with different width um uh heads on them for different parts. So, you just press the button on this thing.

**Dave Jones:** Put the suction cup on top, let it go, and bingo, we've picked up our part, and we can move it over. But, as you can see, you don't get it right, uh it falls off, and uh it can ruin your day. These are a pain in the ass. I find tweezers much easier.

**Dave Jones:** But, uh the these particular just hand ones like this, these are, you know, these are pretty crap and crusty. You can get uh much better uh vacuum ones which actually have a proper mains power vacuum pump, and then there's a foot pump on the floor, so that uh you know, you operate with your foot, and it picks up your part and moves it over. And they have much better and more consistent uh vacuum in them than just these hand ones. Now, if you do get your

**Dave Jones:** parts in tape form uh like this, and you've got a lot of them to do, it can be worth actually uh labeling them on the bench, you know, put a little uh label next to them. Get some uh sticky tape, actually uh you know, hold down the start and the end of it, and then you can, if you have a vacuum tool, then you can just go along and pick them out like that. And you can actually be, you know, quite efficient if you've got a proper vacuum

**Dave Jones:** tool, and it's right near it. You don't even have to raise your hand. Boop. Boop. Boop. Almost like a human pick and place machine. Almost. Once you, you know, if you get your uh technique down right. But, of course, we can't take too long doing this, cuz as I said at the start, this solder paste has a not only a 6-month uh shelf life or a a shelf life, but after you've uh taken it of the fridge, let it warm down, you've applied it here, you've only got a

**Dave Jones:** couple of hours before the solder paste isn't going to work that well, and you know, so maybe like 2 hours is usually the recommended figure, but yeah, you've probably got, you know, four or five for a simple do-it-yourself one like this, but you certainly don't want to apply the paste and then come back the next day. It's just not going to work. So, make sure you got all your stuff sorted, ready to go after you've applied your paste. Now, if there's one thing that will really ruin your day, and Murphy

**Dave Jones:** will ensure it probably happens, is you place your components back to front. Now, take this LED I'm using here, for example. How do Where are the markings on this to indicate which is the anode and which is the cathode? So, make sure you physically test these things before you put them on for these critical parts, and or you're reading the correct data sheet. Trap for young players. Nothing worse than going placing a hun- hundred leads or something, then finding you got them all back to front.

**Dave Jones:** And they've thoughtfully provided in the book identification for the LED here, but look at this. This is a much larger cutout. They've actually supplied a different type of LED, and guess what? The supplied one is actually the opposite polarity to what's shown here.

**Dave Jones:** It's shown that the cathode here is the one with the notch in it. Well, it's not on the ones I've got, the notch is the anode. Bastard. Let's have a good look at placing that one manually. You can see that not all the solder paste applied to that bottom pad there, so Let's place our LED on there, and push it down into place.

**Dave Jones:** But, even though all our solder paste didn't go on there, that will be enough to reflow that LED. And if we find it fails later, we can always add a bit more solder manually, but not really a big deal. And I'm finding these LEDs incredibly annoying, actually.

**Dave Jones:** Because trying to get them out of the tape and keep the orientation, they keep flipping around and it's just it's really is pretty awful when you use these components which have virtually no visual identifiers on them.

**Dave Jones:** Tediously trying to get my very fine point tweezers inside the tape there and pick it out. And I didn't have much luck with the handheld vacuum pump. That's just garbage. So, really, anyway, it's done. I mean, you know, in the end it only took me a few minutes, but if you really had a lot of these to do, you know, efficiency in this sort of thing matters. Now, it's not hugely critical that you'll actually get the uh chip and parts, you know, really bang center on those uh pads

**Dave Jones:** because when this solder reflows, there will be surface tension on there and it will actually pull the chip directly into the center. Now, I was going to say that this is this project is probably not a good example of um you know, just being able to easily place parts on a board like this, but well, I guess the whole idea is to show a practical uh circuit and this is a practical circuit. These are practical parts. These LEDs, pain in the ass, they've got no visual identifiers. This

**Dave Jones:** tiny little um six-pin SOT23 here, you can just see the tiny little uh pin one marker on there. I can barely see that with my eye. It's much clear It's much clearer on the screen here. So, I was going to complain that it's really a pain in the butt. I was hoping to have a real quick video just showing this sort of stuff, but this is This is more real world. There is our tiny little six-pin sot-23. You'll notice that the uh solder paste is now, you know, it's it's

**Dave Jones:** all over the shop there really, but the thing is that will reflow quite nicely and the solder mask it should reflow just fine and we shouldn't get any shorts at all. And you'll notice I've got it the right way around. Pin one marker there, the little dot on the chip with the white notch on the top. And when you peeling the tape back on these things, just be careful. These if you fling these, these little capacitors will go everywhere and if you drop one of the

**Dave Jones:** There we go, one just popped out. And if you drop these on your carpet, you you'll never find them again. They're just completely gone. And these are 0603s, you know, if you're using 0402s or something, oh man, forget it.

**Dave Jones:** Just be careful you don't bump the ones next to them. That's why you really need a fine pair of tweezers like I'm using here rather than ones with big fat stumpy ends on them. Uh should try and self-center themselves when they reflow.

**Dave Jones:** There we go. That will be the end of the most tedious part of all this which is uh placing the components. Dave robot pick and place machine is complete. All our parts are done. Woohoo! Time to actually reflow this thing. Now, ideally uh we would use a reflow oven to do this or one of those modified uh toaster ovens which are all the vogue these days, but I don't have one and as it so happened I wanted to show that you can do it just using a hot air

**Dave Jones:** gun like this because any well-equipped lab lab for surface mount work should have a basic hot air gun like this 858D. Plus, I mean, real cheap on eBay, you know, like $60, I've done a review on this and good enough for this purpose.

**Dave Jones:** Now, there's one thing you should do if you want to take this reflow soldering business seriously, look up the manufacturer of your particular solder paste and I've done that just here. Look at their data sheet for it and you'll get a reflow thermal profile for it and this is typically what you would program into your reflow oven or toaster oven.

**Dave Jones:** You would program in this profile here where it ramps up, you know, ramps up to maximum temperature at about 180 seconds there. So, you put your entire board in and boom, it ramps up. It's going to be, you know, it needs to be within these margins. That's why it's got two curves up and low. It should be somewhere smack in the middle of that and then reaches a peak at around 180 seconds and taper off, but this will vary depending on the type of solder paste and it'll also vary

**Dave Jones:** depending on the type upon the layout of your board as well because if you've got a board with you know, lots of ground planes on there, not enough thermal relief and this is where the design of your PCB comes into it because your components can tombstone. They can one end of a component can reflow quicker than the other end and your component can tombstone and lift up like that and that's bad news and well, I don't know, it might happen today, but a lot of that

**Dave Jones:** is a lot of art in PCB design and designing thermal thermal reliefs on your pads and things like that. So, but that's a whole video in its own right because we don't have a reflow oven here, we can't set a temperature profile. We don't have a board preheater or anything like that.

**Dave Jones:** I'm just showing you how you can do it quick and dirty using, you know, a non-optimal tool like a hot air gun, but it can work. So, really what we want is our maximum temperature there is, you know, 220 or something like that. Uh for one of these um hot air guns, you probably want to go and uh set it maybe 40 50° above that. So, sort of like 250 is probably not a bad temperature to set it at. Sort of 250 260. You probably wouldn't want to go above that. To make

**Dave Jones:** it even more difficult, we have um quite uh temperature-dependent components on here. These LEDs are notorious for not surviving high temperatures. So, you really got to solder them quick and you know, really keep that temperature down to an absolute minimum. Otherwise, your LEDs can be ruined. So, there you go. I've got it set to around about 250. And I'm going to try a wide I actually don't have the nozzle the wide nozzle. So, I'm just going to use the direct output.

**Dave Jones:** Usually, you'd use a wider nozzle for this purpose. Otherwise, you'd get a smaller nozzle like that if you want just wanted to get in there and do more you know, more direct work. And you want it set to a reasonably low level on your air flow as well because you don't want to blow your components off the board cuz there's not much adhesion on those components. All right.

**Dave Jones:** Now, I'm just going to experiment with a couple of components on the outside here. And we start out by bringing it down swirling motion around there until we can see the solder paste reflow.

**Dave Jones:** And there we go. You can see that capacitor moving into place there and we reflowed the LED. Beautiful. Now, here's an example on this capacitor here where it has reflowed, but you can see because it's a big 10 microfarad capacitor 0603, very thick one. So, it's you know, the height of there it's the solder fill up is only on the bottom of the capacitor down in there, but you can see it is actually quite uh quite clean. I rather like that. You can see that LED there reflowed very nicely

**Dave Jones:** as well. All right, let's try the same thing on this SO8 and these resistors down here. Circular motion on your hot air gun there and it will take a little bit because there is a a thermal mass in the board that you'll have to heat up. You do have to experiment with this. It's all a matter of getting the correct amount of air flow and temperature. This is why a proper thermal oven is much better. It just does it all in one hit and it correctly

**Dave Jones:** matches the manufacturer's thermal profile for the paste and minimizes damage to parts and stuff like that. And here we go. We're starting to go. And you can see the solder that There we go. You can see the solder mask working perfectly.

**Dave Jones:** Brilliant. Look at that. No more No solder bridges. No nothing. Fantastic. That's the magic of solder mask here is that Look at there's no shorts between any of those pins at all and each pin is perfectly soldered. Brilliant. And here goes our six-pin SOT23.

**Dave Jones:** Wham! Look at that. Oh, yeah, there we go. Our solder bridge went away. All that solder reflowed nicely. Oh, beautiful. Now, I've actually uh uh turned up the temperature to about uh 265 or thereabouts, and that seems to be reflowing these leads rather quickly.

**Dave Jones:** You probably can't uh see that, but So, yes, it's all a matter of getting the right temperature, the right air flow, and uh you can reflow these quite quickly. I've got it set to about 265. I don't know how good that is on uh this particular unit, how well regulated, but uh anyway, I've got it like a uh air speed of four, I think.

**Dave Jones:** Four and a half, something like that. So, I had to uh increase it where I started off having it because this is pretty much uh experimentation. It's going to vary greatly. There goes the capacitor. It's going to vary greatly uh between individual units and uh the type of board you have. As as I said with uh how many thermal reliefs it has, how much copper it's got on there, what all the thermal mass, thermal mass of the parts, all sorts of stuff.

**Dave Jones:** It's all uh it's all a big gamble, and it is uh trial and error. And by the way, just be careful what surface you do this on. I'm doing it on this uh high temperature uh rubber uh ESD mat, which is designed to uh uh not burn through with solder, and uh it is done. I forgot to load the components on that board, by the way. If you're um that's actually a double-sided load board. So, what I'm actually going to do Actually, what I'll do is I'll

**Dave Jones:** just reflow Now, before I hand solder uh a a of uh components left, we'll just uh cut this out of the panel here. Use a uh your crap pair of side cutters. Have a good pair for uh good work and a crap pair for something like this and get in there the flat side. If it's a round board like that, you want the flat side of your side cutters in there and bang.

**Dave Jones:** All right, we have our nicely assembled board. Moment of truth, plug in my 5-V power supply and ta-da! Look at that. All LEDs work. I got them around the right way, regardless of uh yeah, the uh instructions being slightly wrong. Pays not to follow the instructions sometimes, but look at that. We have a ring light. If we go up, we can see it hopefully increasing brightness. It looks like Oh, yeah, you can hold it down. Bang, bang, bang. And ooh!

**Dave Jones:** Full brightness. It's pretty darn bright. You don't want to look look at the thing, that's for sure. Very nice. And you wouldn't believe it. Look at this. It doesn't fit over the uh focus ring on my Canon HFG10, which is my main camera I shoot the blog with. Ah, well.

**Dave Jones:** I've I've got to admit, I normally wouldn't uh do a reflow soldering on a board like this. I'd just get down with my soldering iron and my 0.5 mm solder and I just manually solder all of the leads and all of the components cuz there's not that many because it is actually quite a hassle to do uh reflow soldering uh with uh stencil reflow soldering. And you've essentially got to have a very good reason to do it. One of the best uh reasons, of course, essential reason is

**Dave Jones:** if you've got like a BGA component, for example, that you can't do with the manual method. You've got to use a stencil and paste and then uh reflow underneath the BGA. And you can just see the consistency on all of those solder joints. there. It is very, very nice.

**Dave Jones:** You can tell it's been reflow soldered. Uh the other thing is uh you know, there's no flux residue, sorry, left around from the rosin core solder. Uh so, it looks very clean and very professional like it was machine assembled. And well, it you know, it almost is. The only difference is you place the parts instead of a machine.

**Dave Jones:** So, really to do reflow soldering properly, you should have a proper thermal uh oven I converted uh toaster oven or a proper reflow oven. Then you can program in the temperature profile and you can follow the manufacturer's instructions precisely. You minimize risk to all your components and it's just going to work a lot quicker as well. But, as you saw, we just used basic uh tools here today. We didn't even use the right type of uh spatula.

**Dave Jones:** We used just a uh hot air uh reflow gun and we were able to do it no problems whatsoever. We reflowed all our parts, lots of delicate LEDs, didn't damage one of them. But, you have to be very careful if you're using one of these hot air guns just to experiment and make sure you've got it right on non-critical components first before you trust it on, you know, a a real uh you know, critical board with a BGA and everything else that you can't afford to get wrong. And

**Dave Jones:** of course, you got to design your boards properly for a thermal layout as well. That's a whole 'nother video. So, I guess you could argue it's a bit of a toss-up with on a board like this whether or not it's quicker just to hand solder the thing and be done with it or whether or not you muck around with a stencil and a reflow oven or a hot air gun. But, certainly, the results are first class and you can easily do it yourself using uh very cheap uh laser

**Dave Jones:** cut Mylar or uh uh other stencil. And in fact, some PCB uh suppliers even provide you a free stencil now. Yeah, give it a try. It's not as hard as you think. Hope you found that interesting and if you want to discuss it, jump on over to the EV blog forum.

**Dave Jones:** Catch you next time.
