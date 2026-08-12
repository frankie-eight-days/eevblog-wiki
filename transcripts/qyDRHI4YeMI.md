---
video_id: qyDRHI4YeMI
title: EEVblog #415 - SMD Stencil Reflow Soldering Tutorial
url: https://www.youtube.com/watch?v=qyDRHI4YeMI
source: youtube-asr
timestamps: {"0": 1, "1": 17, "2": 36, "3": 51, "4": 66, "5": 81, "6": 100, "7": 115, "8": 130, "9": 143, "10": 156, "11": 173, "12": 183, "13": 196, "14": 207, "15": 217, "16": 229, "17": 239, "18": 250, "19": 267, "20": 285, "21": 302, "22": 315, "23": 329, "24": 343, "25": 361, "26": 374, "27": 394, "28": 411, "29": 425, "30": 439, "31": 455, "32": 468, "33": 485, "34": 502, "35": 513, "36": 544, "37": 563, "38": 581, "39": 595, "40": 606, "41": 621, "42": 637, "43": 649, "44": 663, "45": 676, "46": 688, "47": 703, "48": 715, "49": 729, "50": 742, "51": 754, "52": 765, "53": 775, "54": 785, "55": 798, "56": 809, "57": 822, "58": 832, "59": 846, "60": 863, "61": 877, "62": 891, "63": 911, "64": 925, "65": 943, "66": 972, "67": 982, "68": 999, "69": 1014, "70": 1029, "71": 1045, "72": 1061, "73": 1076, "74": 1088, "75": 1105, "76": 1123, "77": 1148, "78": 1159, "79": 1174, "80": 1187, "81": 1203, "82": 1213, "83": 1227, "84": 1240, "85": 1256, "86": 1270, "87": 1283, "88": 1296, "89": 1313, "90": 1329, "91": 1342, "92": 1354, "93": 1373, "94": 1394, "95": 1409, "96": 1431, "97": 1443, "98": 1455, "99": 1475, "100": 1494, "101": 1516, "102": 1537, "103": 1552, "104": 1568, "105": 1584, "106": 1598, "107": 1618, "108": 1635, "109": 1653, "110": 1669, "111": 1682, "112": 1696, "113": 1708, "114": 1722, "115": 1735, "116": 1749, "117": 1763, "118": 1779, "119": 1792, "120": 1805, "121": 1817, "122": 1834, "123": 1845}
---

**Dave Jones:** Hi, in this episode I'm going to show you how to do-it-yourself reflow stencil solder a PCB. And I got this one from the mailbag sometime back. If you haven't seen it, it's based on Vincent Himpe's book Mastering Surface Mount

**Dave Jones:** Technology. This is where they part of the Electrolab Works series. This is where the PCB comes from and it's a ring light for cameras. And we're going to reflow solder all of the parts on here using a solder paste stencil. This is a quite a

**Dave Jones:** high-quality stainless steel stencil. Now, you don't necessarily have to get a stainless steel one if you're doing it yourself. In fact, they're probably prohibitively expensive, but there's a lot of companies out there today that will laser cut you a

**Dave Jones:** a Mylar or a Kapton solder paste stencil direct from the file in your CAD package. It can generate the paste stencil. And that's a whole video in its own right, but I'm going to show you how to do that using some basic solder paste

**Dave Jones:** and a hot air reflow gun. And we're going to have a go at reflowing the parts on here after we apply the solder paste with a stencil. So, let's give it a go. And the solder paste I'm going to use today comes from

**Dave Jones:** Chemtools or Aim Solder here in Australia. And it's a 63% it's SN63, which stands for 63% tin and 37% lead. So, it's quite close to your regular 60/40 leaded solder. So, this is not lead-free solder. It's only 15 g, which

**Dave Jones:** doesn't sound like a lot, but you don't need much solder paste, as we'll see, to do one of these stencils on, you know, a fairly a fairly typical board like this. So, this one has been manufactured fairly recently. Now,

**Dave Jones:** the solder paste has a couple of issues. The first one is that it does have a shelf life. If you try and use it beyond that, well, its performance is not guaranteed. I mean, this one might have, say, 6 months. And if you use it in 12

**Dave Jones:** months' time, it's probably still going to work, but you know, the performance is not guaranteed at all. Now, this one's in a syringe format because it comes with a little tip like this, which you can plug it on. You can

**Dave Jones:** use it as a syringe, and you can individually put paste on each pad like that. And you can even do it manually with a syringe, or you can get an air pump, which dispenses a paste dispenser. You can buy them on eBay fairly cheaply

**Dave Jones:** these days, 100 bucks or so, I think. Solder paste dispenser, and you can go around and manually dispense solder paste on each pad. But hey, that's time-consuming. You end up missing the pads. It's much quicker and simpler to use the solder paste stencil

**Dave Jones:** like this. So, all we're going to do is apply our solder paste on there, then we go over it with a squeegee like this, and we're going to apply all of our solder paste in there. And we lift it

**Dave Jones:** off, and we should be left with an even amount of solder paste on each one of our pads here. That's the plan. And then we place the parts, and then we will reflow the solder. The other problem with

**Dave Jones:** solder paste, of course, is that it must be kept in a fridge as well. It must be kept airtight, so you got to put the nozzle back on it in a fridge. And then, even then, it still has a shelf life.

**Dave Jones:** Now, when you go to use it like this, make sure you sit it in room temperature for a couple of hours. You don't want to apply it cold. It's not an issue that it's going to reflow incorrectly. It's

**Dave Jones:** just that it won't apply through the solder paste stencil very nicely. So, you really have to let it warm up to room temperature for a couple of hours first before you can use it. And when you done with it, make sure you

**Dave Jones:** put it airtight and put it back in the fridge. So, solder paste can be a bit annoying if you and a quite an expensive way to do it if you're just, you know, you want to do a one-off board, you're

**Dave Jones:** doing one or two boards a year, uh solder paste, you know, it may not be worth your while, but anyway, um we are going to give it a go. Now, the first thing you want to do is just inspect

**Dave Jones:** your solder paste stencil to make sure all of the holes are cut out. Now, it just so happens that this one here um hasn't. You can see that there's still one there that didn't punch out correctly. So, we're now left with all

**Dave Jones:** of our precisely cut pad-shaped holes there for the solder paste. Now, if you're really um you know, into high-volume uh manufacture mobile phones or something really high-density parts, very critical, very dense uh spacing, then the type of stencil you use, the

**Dave Jones:** thickness of your stencil, the uh exact type of solder paste, the exact angle that you apply the solder paste at, and uh the size of your paste pad uh holes and everything like that can become quite critical to um your final yield in

**Dave Jones:** volume production, but just for do-it-yourself stuff, uh it doesn't matter. This is a stainless steel stencil, more than good enough. It's about 150 microns uh thick. Doesn't matter. It's going to work whether you use like a you know, you just get one of

**Dave Jones:** those cheap laser-cut Mylar um or uh Kapton sheets or something like that. And next up, you're going to require uh a couple of PCBs the exact same thickness as the board you're doing. Of course, this is like a standard 1.6 mm

**Dave Jones:** board, so we've got two other 1.6 mm boards. This will hold this board in place and ensure that it just doesn't move around on the bench like that. So, we're going to put it down there. We're going to get some

**Dave Jones:** sticky tape. And you don't want any tape on the board itself on the board you're doing, especially if there isn't much room around the outside of the panel here because then when you apply your stencil on there, it

**Dave Jones:** may not sit very flat if there's some tape very close to the individual pads that you're doing. And next up, we're going to have to align our stencil over these pads. As you can see, it's uh it's fairly critical. There's not much

**Dave Jones:** movement in my fingers there. You can see how critical this would be if you were doing you know, a real you know, like a mobile phone with little 0201 components or something like that, real ultra-dense stuff, then the alignment of

**Dave Jones:** these stencils becomes a big deal. So, I'm going to I think that's right, so I'm going to apply some sticky tape on the outside of that, either side, and it's it's sitting fairly flat. The thing you don't want to do is have this warp

**Dave Jones:** during your paste application. For a do-it-yourself application like this though, it's really not that critical. You know, if you get a little bit of warpage in there, it's not a problem. Now, what we've got is a spatula here or

**Dave Jones:** it's sometimes called a squeegee or you know, it goes under various names in the industry. This one is not designed for this purpose. This is just one designed for cake mixing and things like that. It's a silicone rubber

**Dave Jones:** one and you know, it's it's not ideal for the purpose, but for just a do-it-yourself one-off like this, it's going to work just fine, I think. Ideally, you'd want a proper stainless steel spatula to apply. Now, the angle that

**Dave Jones:** you use on this can be reasonably critical. It may not matter just on a simple do-it-yourself one like this, but you know, if you use too shallow an angle like that, it can or too sharp an angle like that, then it can actually uh

**Dave Jones:** rip some of the solder paste back out of it. All right, now let's give it a go. Now, we shouldn't need a huge amount of solder paste at all. Let's just maybe put that much on there, perhaps. There we go, a little

**Dave Jones:** bit more. Now, let's get our squeegee in here and move it drag it across. Now, stencil like that, and make sure you get the right angle. Make sure there's no retraction in there. The sol- Oh, you can see that one.

**Dave Jones:** I think you can see that one just there. You can see some of the paste has retracted out of that one. Normally, you only have to like, you know, do this in one pass, usually. Don't be afraid to go

**Dave Jones:** back over existing pads. You can certainly do that. And I really, you know, this uh is not the best spatula at all, folks. I'm not happy with this. Um at all. I didn't have a metal one, so I've had to make do here.

**Dave Jones:** And there's a very good close-up of some uh solder retraction there. So, I'm just going to put a little bit more paste in there. And uh this uh paste I I may not have may still be a bit cold. I may not have let it uh

**Dave Jones:** warm up enough. Now, this isn't the world's best job, I'm afraid, cuz I usually don't uh do this. I'm I'm using uh new solder paste I haven't used before. I'm using a new spatula I haven't used before, so

**Dave Jones:** you know, really and I and I haven't um done any practice at all. So, this one this particular job is a little bit hit and miss, I'm afraid, but you get the idea. So, ordinarily, you know, if you've got your uh technique down uh

**Dave Jones:** pat, then you should be able to in theory uh do this in one pass of the uh spatula or the uh squeegee. If you got a super wide one, it can go right across the board, but um anyway, we just want

**Dave Jones:** to inspect. Make sure you inspect like the big ones are really obvious for the LEDs, but just inspect those little uh ones in there just to make sure that they're uh make sure that they're covered very carefully. Peel it

**Dave Jones:** off. And don't touch it and you should be left with a board with tada, solder paste on it. And there you have it. You can see the solder paste on the individual pads there. And of course, if you have a look

**Dave Jones:** in here, you can see some what looks like, you know, I like the solder paste has gotten between the pads, but don't worry about that. Your solder mask, that green stuff on your board there, is going to take care of that when that

**Dave Jones:** reflows. So, when you uh reflow that solder with the uh hot air gun, that they will not uh stay together and short. The solder will just start reflow into the well on the pad. Uh and uh it won't stick to the solder

**Dave Jones:** mask, so it shouldn't be a problem. If you actually miss one of the pads and it doesn't uh reflow, then well, really, that can ruin your day. So, it's worth spending 5 minutes just under a uh under a magnifying lamp going around

**Dave Jones:** inspecting everything. Now, as for placing parts, there is a uh couple of ways to do it. Of course, the fully automated way to do it is to use a pick and place machine, but we don't have one of those and you

**Dave Jones:** don't either, I'm sure, because that's why you're watching this video. So, the traditional way to do it is just a pair of surface mount tweezers, non-magnetic type. Make it Make sure you get a good high-quality pair, and you can

**Dave Jones:** individually place them one by one down like that. And the other way to do it is with one of these vacuum pick up tools. You can pick these up for, you know, 5 or 10 bucks, very cheap. They come with

**Dave Jones:** different width um uh heads on them for different parts. So, you just press the button on this thing. Put the suction cup on top, let it go, and bingo, we've picked up our part, and we can move it over. But, as you can

**Dave Jones:** see, you don't get it right, uh it falls off, and uh it can ruin your day. These are a pain in the ass. I find tweezers much easier. But, uh the these particular just hand ones like this, these are, you know,

**Dave Jones:** these are pretty crap and crusty. You can get uh much better uh vacuum ones which actually have a proper mains power vacuum pump, and then there's a foot pump on the floor, so that uh you know, you operate with your foot,

**Dave Jones:** and it picks up your part and moves it over. And they have much better and more consistent uh vacuum in them than just these hand ones. Now, if you do get your parts in tape form uh like this, and

**Dave Jones:** you've got a lot of them to do, it can be worth actually uh labeling them on the bench, you know, put a little uh label next to them. Get some uh sticky tape, actually uh you know, hold down the start and the

**Dave Jones:** end of it, and then you can, if you have a vacuum tool, then you can just go along and pick them out like that. And you can actually be, you know, quite efficient if you've got a proper vacuum

**Dave Jones:** tool, and it's right near it. You don't even have to raise your hand. Boop. Boop. Boop. Almost like a human pick and place machine. Almost. Once you, you know, if you get your uh technique down right. But, of course, we can't take too

**Dave Jones:** long doing this, cuz as I said at the start, this solder paste has a not only a 6-month uh shelf life or a a shelf life, but after you've uh taken it of the fridge, let it warm down, you've

**Dave Jones:** applied it here, you've only got a couple of hours before the solder paste isn't going to work that well, and you know, so maybe like 2 hours is usually the recommended figure, but yeah, you've probably got, you know, four or five for

**Dave Jones:** a simple do-it-yourself one like this, but you certainly don't want to apply the paste and then come back the next day. It's just not going to work. So, make sure you got all your stuff sorted, ready to go after you've applied your

**Dave Jones:** paste. Now, if there's one thing that will really ruin your day, and Murphy will ensure it probably happens, is you place your components back to front. Now, take this LED I'm using here, for example. How do Where are the markings

**Dave Jones:** on this to indicate which is the anode and which is the cathode? So, make sure you physically test these things before you put them on for these critical parts, and or you're reading the correct data sheet. Trap for young players. Nothing

**Dave Jones:** worse than going placing a hun- hundred leads or something, then finding you got them all back to front. And they've thoughtfully provided in the book identification for the LED here, but look at this. This is a much larger

**Dave Jones:** cutout. They've actually supplied a different type of LED, and guess what? The supplied one is actually the opposite polarity to what's shown here. It's shown that the cathode here is the one with the notch in it. Well, it's not

**Dave Jones:** on the ones I've got, the notch is the anode. Bastard. Let's have a good look at placing that one manually. You can see that not all the solder paste applied to that bottom pad there, so Let's place our LED on there, and

**Dave Jones:** push it down into place. But, even though all our solder paste didn't go on there, that will be enough to reflow that LED. And if we find it fails later, we can always add a bit more solder manually, but not really a

**Dave Jones:** big deal. And I'm finding these LEDs incredibly annoying, actually. Because trying to get them out of the tape and keep the orientation, they keep flipping around and it's just it's really is pretty awful when you use these components which have

**Dave Jones:** virtually no visual identifiers on them. Tediously trying to get my very fine point tweezers inside the tape there and pick it out. And I didn't have much luck with the handheld vacuum pump. That's just garbage. So, really, anyway, it's done. I mean,

**Dave Jones:** you know, in the end it only took me a few minutes, but if you really had a lot of these to do, you know, efficiency in this sort of thing matters. Now, it's not hugely critical that you'll actually

**Dave Jones:** get the uh chip and parts, you know, really bang center on those uh pads because when this solder reflows, there will be surface tension on there and it will actually pull the chip directly into the center. Now, I was going to say

**Dave Jones:** that this is this project is probably not a good example of um you know, just being able to easily place parts on a board like this, but well, I guess the whole idea is to show a practical uh circuit and this is a

**Dave Jones:** practical circuit. These are practical parts. These LEDs, pain in the ass, they've got no visual identifiers. This tiny little um six-pin SOT23 here, you can just see the tiny little uh pin one marker on there. I can barely see that

**Dave Jones:** with my eye. It's much clear It's much clearer on the screen here. So, I was going to complain that it's really a pain in the butt. I was hoping to have a real quick video just showing this sort of stuff, but this is

**Dave Jones:** This is more real world. There is our tiny little six-pin sot-23. You'll notice that the uh solder paste is now, you know, it's it's all over the shop there really, but the thing is that will reflow quite nicely

**Dave Jones:** and the solder mask it should reflow just fine and we shouldn't get any shorts at all. And you'll notice I've got it the right way around. Pin one marker there, the little dot on the chip with the white notch on the top. And when you

**Dave Jones:** peeling the tape back on these things, just be careful. These if you fling these, these little capacitors will go everywhere and if you drop one of the There we go, one just popped out. And if you drop these on your carpet, you

**Dave Jones:** you'll never find them again. They're just completely gone. And these are 0603s, you know, if you're using 0402s or something, oh man, forget it.

**Dave Jones:** Just be careful you don't bump the ones next to them. That's why you really need a fine pair of tweezers like I'm using here rather than ones with big fat stumpy ends on them. Uh should try and self-center themselves

**Dave Jones:** when they reflow. There we go. That will be the end of the most tedious part of all this which is uh placing the components. Dave robot pick and place machine is complete. All our parts are done. Woohoo! Time to actually reflow this

**Dave Jones:** thing. Now, ideally uh we would use a reflow oven to do this or one of those modified uh toaster ovens which are all the vogue these days, but I don't have one and as it so happened I wanted to

**Dave Jones:** show that you can do it just using a hot air gun like this because any well-equipped lab lab for surface mount work should have a basic hot air gun like this 858D. Plus, I mean, real cheap on eBay, you

**Dave Jones:** know, like $60, I've done a review on this and good enough for this purpose. Now, there's one thing you should do if you want to take this reflow soldering business seriously, look up the manufacturer of your particular solder

**Dave Jones:** paste and I've done that just here. Look at their data sheet for it and you'll get a reflow thermal profile for it and this is typically what you would program into your reflow oven or toaster oven. You would program in this profile here

**Dave Jones:** where it ramps up, you know, ramps up to maximum temperature at about 180 seconds there. So, you put your entire board in and boom, it ramps up. It's going to be, you know, it needs to be within these

**Dave Jones:** margins. That's why it's got two curves up and low. It should be somewhere smack in the middle of that and then reaches a peak at around 180 seconds and taper off, but this will vary depending on the type of solder paste and it'll also vary

**Dave Jones:** depending on the type upon the layout of your board as well because if you've got a board with you know, lots of ground planes on there, not enough thermal relief and this is where the design of your PCB comes into it because your

**Dave Jones:** components can tombstone. They can one end of a component can reflow quicker than the other end and your component can tombstone and lift up like that and that's bad news and well, I don't know, it might happen today, but a lot of that

**Dave Jones:** is a lot of art in PCB design and designing thermal thermal reliefs on your pads and things like that. So, but that's a whole video in its own right because we don't have a reflow oven here, we can't set a

**Dave Jones:** temperature profile. We don't have a board preheater or anything like that. I'm just showing you how you can do it quick and dirty using, you know, a non-optimal tool like a hot air gun, but it can work. So, really what we want is

**Dave Jones:** our maximum temperature there is, you know, 220 or something like that. Uh for one of these um hot air guns, you probably want to go and uh set it maybe 40 50° above that. So, sort of like 250

**Dave Jones:** is probably not a bad temperature to set it at. Sort of 250 260. You probably wouldn't want to go above that. To make it even more difficult, we have um quite uh temperature-dependent components on here. These LEDs are

**Dave Jones:** notorious for not surviving high temperatures. So, you really got to solder them quick and you know, really keep that temperature down to an absolute minimum. Otherwise, your LEDs can be ruined. So, there you go. I've got it set to around about 250. And I'm

**Dave Jones:** going to try a wide I actually don't have the nozzle the wide nozzle. So, I'm just going to use the direct output. Usually, you'd use a wider nozzle for this purpose. Otherwise, you'd get a smaller nozzle like that if you want

**Dave Jones:** just wanted to get in there and do more you know, more direct work. And you want it set to a reasonably low level on your air flow as well because you don't want to blow your components off the board

**Dave Jones:** cuz there's not much adhesion on those components. All right. Now, I'm just going to experiment with a couple of components on the outside here. And we start out by bringing it down swirling motion around there until we can see

**Dave Jones:** the solder paste reflow. And there we go. You can see that capacitor moving into place there and we reflowed the LED. Beautiful. Now, here's an example on this capacitor here where it has reflowed, but you can see because it's a

**Dave Jones:** big 10 microfarad capacitor 0603, very thick one. So, it's you know, the height of there it's the solder fill up is only on the bottom of the capacitor down in there, but you can see it is actually quite uh

**Dave Jones:** quite clean. I rather like that. You can see that LED there reflowed very nicely as well. All right, let's try the same thing on this SO8 and these resistors down here. Circular motion on your hot air gun there and it will

**Dave Jones:** take a little bit because there is a a thermal mass in the board that you'll have to heat up. You do have to experiment with this. It's all a matter of getting the correct amount of air flow and

**Dave Jones:** temperature. This is why a proper thermal oven is much better. It just does it all in one hit and it correctly matches the manufacturer's thermal profile for the paste and minimizes damage to parts and stuff like that. And

**Dave Jones:** here we go. We're starting to go. And you can see the solder that There we go. You can see the solder mask working perfectly. Brilliant. Look at that. No more No solder bridges. No nothing. Fantastic. That's the magic of solder mask here is

**Dave Jones:** that Look at there's no shorts between any of those pins at all and each pin is perfectly soldered. Brilliant. And here goes our six-pin SOT23. Wham! Look at that. Oh, yeah, there we go. Our solder bridge went away. All

**Dave Jones:** that solder reflowed nicely. Oh, beautiful. Now, I've actually uh uh turned up the temperature to about uh 265 or thereabouts, and that seems to be reflowing these leads rather quickly. You probably can't uh see that, but So, yes, it's all a matter of getting the

**Dave Jones:** right temperature, the right air flow, and uh you can reflow these quite quickly. I've got it set to about 265. I don't know how good that is on uh this particular unit, how well regulated, but uh anyway, I've got it like a uh

**Dave Jones:** air speed of four, I think. Four and a half, something like that. So, I had to uh increase it where I started off having it because this is pretty much uh experimentation. It's going to vary greatly. There goes the capacitor.

**Dave Jones:** It's going to vary greatly uh between individual units and uh the type of board you have. As as I said with uh how many thermal reliefs it has, how much copper it's got on there, what all the thermal mass, thermal mass of the

**Dave Jones:** parts, all sorts of stuff. It's all uh it's all a big gamble, and it is uh trial and error. And by the way, just be careful what surface you do this on. I'm doing it on this uh high temperature uh

**Dave Jones:** rubber uh ESD mat, which is designed to uh uh not burn through with solder, and uh it is done. I forgot to load the components on that board, by the way. If you're um that's actually a double-sided load board. So, what I'm actually going

**Dave Jones:** to do Actually, what I'll do is I'll just reflow Now, before I hand solder uh a a of uh components left, we'll just uh cut this out of the panel here. Use a uh your crap pair of side cutters. Have a

**Dave Jones:** good pair for uh good work and a crap pair for something like this and get in there the flat side. If it's a round board like that, you want the flat side of your side cutters in there and bang.

**Dave Jones:** All right, we have our nicely assembled board. Moment of truth, plug in my 5-V power supply and ta-da! Look at that. All LEDs work. I got them around the right way, regardless of uh yeah, the uh instructions being slightly

**Dave Jones:** wrong. Pays not to follow the instructions sometimes, but look at that. We have a ring light. If we go up, we can see it hopefully increasing brightness. It looks like Oh, yeah, you can hold it down. Bang, bang, bang. And ooh!

**Dave Jones:** Full brightness. It's pretty darn bright. You don't want to look look at the thing, that's for sure. Very nice. And you wouldn't believe it. Look at this. It doesn't fit over the uh focus ring on my Canon HFG10, which is my main

**Dave Jones:** camera I shoot the blog with. Ah, well. I've I've got to admit, I normally wouldn't uh do a reflow soldering on a board like this. I'd just get down with my soldering iron and my 0.5 mm solder and I just manually solder

**Dave Jones:** all of the leads and all of the components cuz there's not that many because it is actually quite a hassle to do uh reflow soldering uh with uh stencil reflow soldering. And you've essentially got to have a very good

**Dave Jones:** reason to do it. One of the best uh reasons, of course, essential reason is if you've got like a BGA component, for example, that you can't do with the manual method. You've got to use a stencil and paste and then uh reflow

**Dave Jones:** underneath the BGA. And you can just see the consistency on all of those solder joints. there. It is very, very nice. You can tell it's been reflow soldered. Uh the other thing is uh you know, there's no flux residue, sorry, left

**Dave Jones:** around from the rosin core solder. Uh so, it looks very clean and very professional like it was machine assembled. And well, it you know, it almost is. The only difference is you place the parts instead of a machine.

**Dave Jones:** So, really to do reflow soldering properly, you should have a proper thermal uh oven I converted uh toaster oven or a proper reflow oven. Then you can program in the temperature profile and you can follow the manufacturer's instructions precisely. You minimize

**Dave Jones:** risk to all your components and it's just going to work a lot quicker as well. But, as you saw, we just used basic uh tools here today. We didn't even use the right type of uh spatula. We used just a uh hot air uh reflow gun

**Dave Jones:** and we were able to do it no problems whatsoever. We reflowed all our parts, lots of delicate LEDs, didn't damage one of them. But, you have to be very careful if you're using one of these hot air guns just to experiment and make

**Dave Jones:** sure you've got it right on non-critical components first before you trust it on, you know, a a real uh you know, critical board with a BGA and everything else that you can't afford to get wrong. And of course, you got to design your boards

**Dave Jones:** properly for a thermal layout as well. That's a whole 'nother video. So, I guess you could argue it's a bit of a toss-up with on a board like this whether or not it's quicker just to hand solder the thing and be done with it or

**Dave Jones:** whether or not you muck around with a stencil and a reflow oven or a hot air gun. But, certainly, the results are first class and you can easily do it yourself using uh very cheap uh laser cut Mylar or uh uh other stencil. And in

**Dave Jones:** fact, some PCB uh suppliers even provide you a free stencil now. Yeah, give it a try. It's not as hard as you think. Hope you found that interesting and if you want to discuss it, jump on over to the

**Dave Jones:** EV blog forum. Catch you next time.
