---
video_id: 588iV07nEdM
title: EEVblog #434 - SMD Thermal Pad & Drag Soldering Tutorial
url: https://www.youtube.com/watch?v=588iV07nEdM
source: youtube-asr
timestamps: {"0": 1, "1": 27, "2": 38, "3": 56, "4": 69, "5": 78, "6": 87, "7": 113, "8": 120, "9": 141, "10": 155, "11": 171, "12": 181, "13": 192, "14": 204, "15": 218, "16": 227, "17": 237, "18": 265, "19": 279, "20": 286, "21": 295, "22": 304, "23": 317, "24": 325, "25": 335, "26": 353, "27": 362, "28": 373, "29": 384, "30": 396, "31": 414, "32": 423, "33": 439, "34": 453, "35": 464, "36": 478, "37": 490, "38": 511, "39": 525, "40": 533, "41": 546, "42": 558, "43": 577, "44": 586, "45": 598, "46": 613, "47": 623, "48": 637, "49": 648, "50": 660, "51": 683, "52": 696, "53": 718, "54": 726, "55": 746, "56": 764, "57": 779, "58": 792, "59": 803, "60": 823, "61": 834, "62": 843, "63": 851, "64": 861, "65": 872, "66": 895, "67": 905, "68": 920, "69": 936, "70": 951, "71": 959, "72": 976, "73": 987, "74": 999, "75": 1008, "76": 1024, "77": 1038, "78": 1046, "79": 1055, "80": 1068, "81": 1076}
---

**Dave Jones:** Hi, just a quick video because I was just assembling my new micro supply prototype PCB that I got from PCBzone.net or Circuit Labs in New Zealand. And I was soldering the components on here and I thought, well, I've gotten to this little MSOP 8 package and I just thought I'd show you how I'm going to solder this onto here because it's not just a regular package.

**Dave Jones:** It's got a thermal pad on the bottom. So, let's go. Now, the chip I'm going to solder on here is this little one with a thermal pad on the bottom and it's an SC 4501 DC to DC converter.

**Dave Jones:** Now, as you can see, I've already soldered an MSOP package on here with a smaller pin pitch, actually, and I just did that using drag soldering. Just use my chisel chip tip soldering iron, put the solder on the bottom, and then just drag the solder off the pins.

**Dave Jones:** Done in a few seconds. You've seen me do that in previous videos, but uh I thought, well, I've got to solder this one onto here and we've actually got this thermal pad on the bottom.

**Dave Jones:** And I've shown you one way to do this before with solder paste and put it down on there and then use hot air, but I'm going to use a different technique today.

**Dave Jones:** So, I thought I'd show you that where I'm actually going to apply the heat from the bottom of the board and I specifically laid out my board so I could do this.

**Dave Jones:** Now, this is a 0.65 mm pin pitch MSOP. It doesn't matter what the pin pitch is. Really, what we're doing here is I'm going to show you how to get the thermal because you need solder under that pad down there to thermally bond it to the chip and then all of this copper around here, of course, is used as a heat sink to get the to get the heat out of the die

**Dave Jones:** inside the chip. And all those uh there, they all go down to the bottom layer, which um acts as a bigger heat sink as well. So, let's give this a go.

**Dave Jones:** Now, the key to doing this is actually um in the layout of the board. Of course, I've left the solder mask off there to uh attach to so that solder can attach to the uh bottom of the thermal pad on the chip, of course, but on the reverse side of the board, I've also added Here it is.

**Dave Jones:** a solder mask cut out as well, so I can apply a big chisel tip on there, and uh actually heat this chip up from the bottom. You need a a decent uh thermal capacity iron, so I'm going to use my uh JBC iron today with a fairly big uh chisel tip.

**Dave Jones:** And if we apply solder through the bottom like that, while that chip is sitting on top there, uh solder will actually flow through those vias there, and should contact our pad on the bottom, provided we use flux, of course.

**Dave Jones:** Now, you've seen me use my Electrolube uh flux pen before, but I'm not going to use that one today. I'm going to use my um flux gel. This is from um Aim Solder in uh Australia.

**Dave Jones:** You can get it from uh Wes Components and other places. This is an NC254 type uh flux gel. So, it's not like the liquid uh type flux, it's more of a gel type.

**Dave Jones:** So, I'm going to apply that um on there, and on the bottom of the chip as well. It's important to apply it to uh both surfaces, and then we'll see if we can reflow this thing from the bottom.

**Dave Jones:** It's not the easiest It's not as easy as the uh liquid stuff to apply this gel type one, but we'll put it That will probably be enough, and we'll smooth that around the bottom.

**Dave Jones:** We'll smooth that around there. In fact, we can do that with our chip. So, I don't actually have to apply it. If I was using my flux pen, I would have applied it to both sides of the chip.

**Dave Jones:** Hang on, I'm trying to get the bloody chip here with the tweezers. Real pain in the ass, but uh uh we should be able to Let's, in fact, make sure I'm getting pin one in the right orientation.

**Dave Jones:** You can see the dot up in the corner of the chip. There's my pin one up there with the square pad and the indentation up there. So, really what we want to do is uh you can see that that's really is very It is very much a gel, very sticky kind of uh gel, certainly different, much different to the uh to the liquid type one you get

**Dave Jones:** in a pen. So, if we get our chip on there, and we put it down in place, we don't have to hold it exactly cuz our chip should self-center on there, but we've applied our liquid flux on the bottom.

**Dave Jones:** The chip is around the right way, I hope, and uh we should be able to heat this thing from the bottom, and we should be able to reflow it.

**Dave Jones:** Let's give it a go. Now, for this, I'm going to use my JBC soldering iron cuz it has a much bigger thermal capacity than my Hakko uh FX triple eight here.

**Dave Jones:** So, I'm definitely going to give this a go. It's got a, you know, a fairly wide uh chisel point on there. I'm currently soldering it at about uh 310.

**Dave Jones:** Probably want to bump that up a little bit because there's a lot of thermal mass on the bottom of that. I don't know. Let's go 330, something like that, but it shouldn't have to maybe set it this high.

**Dave Jones:** Um I'm still not intimately familiar with this JBC. It'll probably do it at uh 300, no problems, but uh you just want to compensate a bit, not taking any chances.

**Dave Jones:** Let's whack it up to 330. Shouldn't need to keep it there very long. Large thermal mass soldering iron, large thermal mass tip. I won't touch it cuz that's the hot pointy end, folks.

**Dave Jones:** And uh the idea is I apply solder to the uh to the chisel chip down here, and I just get up under the bottom there, heat that bottom pad, and that chip, the solder should uh flow through the pins in that, and it should just self-center and attach to the bottom of the chip.

**Dave Jones:** That's the plan. So, here we go. I've got a large uh dollop of solder on my iron tip, and I'm going to apply it to the bottom down here.

**Dave Jones:** Now, I'll have to uh go off-camera because I I've got to see visually where I'm putting this thing, so let me give it a go. But, we apply that there.

**Dave Jones:** Yep, you see it? Bang. And that should now be soldered to that thermal pad. Too easy. Probably didn't even need to turn that up to 330. We go in there.

**Dave Jones:** It'll still be hot, by the way. And this chip, uh bugger. It has moved. I thought it self-centered, but it didn't. There you go. All right. Well, let's give that another go.

**Dave Jones:** I've applied some liquid flux this time cuz I haven't used that uh particular gel type one before. It was an experiment. So, maybe that's it, but let's uh let's reheat the sucker up and uh see if we can get that to float.

**Dave Jones:** Oh, there we go. You saw it just drag it back into place. Look at that. It's even soldering the pads for us now. Beautiful. Look at that. All right.

**Dave Jones:** I think that, folks, is a winner. There uh solder flowed through, and it even reflowed some of the what looks like maybe attempted to do some of the pins there.

**Dave Jones:** But, uh it's definitely flowing through, and I think if that cools down, cuz there will be still a lot of heat left in that. So, but that should be in place, folks, and that is well and truly stuck.

**Dave Jones:** Bingo. We now have our chip soldered onto that thermal pad down in there. Now, let's watch this again in slow motion, shall we? And you'll be able to see the chip self-center.

**Dave Jones:** Here it goes. Bang. That is actually the surface tension of the solder pulling that uh chip back into the center of the solder mask exposed pad under there. Now, let's take a look at the solder reflowing on these pins.

**Dave Jones:** Now, this is not solder actually coming from the soldering iron up through the vias up under the board. It's actually the pins themselves. When you buy these chips, the pins are already coated in solder.

**Dave Jones:** So, what we're going to see here, as you can see on the left-hand side there, the pins, as the heat flows up through the die, through the bond wire onto the individual legs, you can actually see the solder start to flow, what looks like flowing from inside the chip outwards, but that's not That's just the heat radiating up that bond wire through the leg, and then it down eventually to

**Dave Jones:** the pad. So, obviously, once you start seeing that uh solder reflowing on the pins themselves, you know that that heat has transferred through that thermal pad on the bottom of the chip, and actually got up into the bond wires, and yeah, it's really attached.

**Dave Jones:** So, don't wait for the mold to reflow. You know that thermal pad is definitely stuck. Get back in there. So, maybe it was that uh gel flux. I'm not uh sure.

**Dave Jones:** Maybe the liquid uh flux I've got is better. But, let's just start drag solder these pins. I've got a little bit of solder on the bottom of my chisel tip down in there.

**Dave Jones:** And just get in there and go boing. And just drag those pins back out. Up. Got a short on that one. We can fix that up later. Not a problem.

**Dave Jones:** Some solder wick, and it's really hard to do this under the camera. I keep saying that, folks. It really is. Trying to solder under the camera is infinitely harder than doing it with the correct angle, seated, standing up.

**Dave Jones:** But, just drag those pins back, bang, and we solder like that. Not a problem. So, with that shorter pin there, we can just get in there with a bit of solder wick and wick that off.

**Dave Jones:** Or you can try and drag it off with the pin as well. It's It could work either way, but uh this is real world example, folks. This is not one of these perfect soldering tutorials.

**Dave Jones:** Of course, you have these little issues when you solder these things in the real world. Let's just wick There we go. Wick that little bit of solder left, and you can probably retouch that back up, but shouldn't need to.

**Dave Jones:** And yeah, it looks a bit messy. There's a bit of flux residue there, but we can just clean that up. And we'll have a perfectly soldered uh thermal uh MSOP-8 chip.

**Dave Jones:** Beautiful. And to clean that up, we'll just use some of this Electrolube Flux Clean, which uh somebody sent me in the mailbag. So, thank you very much. Otherwise, I'd just use my isopropanol alcohol version.

**Dave Jones:** So, here we go. We'll just squirt a little bit of that down. Rub it around with the brush. Or you can You should have one of these conductive brushes as well.

**Dave Jones:** These are quite neat. Little bit harsher. They've got conductive uh bristles. So, it doesn't generate any static charge. Really quite nice. And you can clean your board up, and that will be now beautiful.

**Dave Jones:** And there you have it, folks. There is our beautifully soldered MSOP-8 .65 mm pin pitch chip with the thermal pad on the bottom. And of course, the key to that is just leaving your solder mask off the bottom like that, so you can apply the heat from the bottom and the solder flows through those vias on the thermal pad and bonds your chip in place.

**Dave Jones:** So, beautiful. Just like a bought one. And of Of when you're doing boards like this, you can see these 0805 components around them. You don't want to solder those on first.

**Dave Jones:** Go in and solder all of your fine pitch chips first and then do your passives around them cuz if you got your passives in there, especially if they're very close like that, being able to drag solder out either whether you do drag solder out or drag solder across the pins like that, really annoying when you try and get it if you already got these passives in place and large components

**Dave Jones:** like there's going to be a big huge inductor here and you know, you might not be able to get your soldering iron in. So, make sure you just do these chips first, but there you go.

**Dave Jones:** That is almost trivial to do. As you see, I used a a gel type flux I've never used before. It didn't quite take on the first go, but then I applied some more a flux from my flux pen which is a which is a liquid type flux and it worked no problems whatsoever on the second pass, very quick.

**Dave Jones:** If you got a decent thermal mass soldering iron and a chisel tip. And you can see we got a bit of residual solder on various pads around here, but you know, that's not really an issue that, but that's going to happen, you know, if you're doing some drag soldering around here, you're just going to get some solder dags on these pads, but not a problem.

**Dave Jones:** You need to apply solder to those anyway to hand solder those passive components on later. And as you can see, I've already soldered my ATmega on there and what I'll do now is just solder this TSOP package.

**Dave Jones:** Once again, 0.65 mm pin pitch just as a bonus, we'll just do some drag soldering onto here. Let's go. Again, always flux is key to this. So, just apply some There we go.

**Dave Jones:** You can apply some liquid flux. You can never have too much flux onto my pins there using my flux pen. Not going to use that gel type again. Not that it's not any good.

**Dave Jones:** It's just that uh I've got my flux pen. And we will apply our chip on there. This is where you Yeah, 0.65 mm. You don't really need to work under a microscope, but like a nice little times four magnification or something really kind of helps.

**Dave Jones:** Um I'm just doing this one under the camera. And yeah, pin one pin one, not a problem. So, let's go in there, do some drag soldering. Now, I just found something a little bit annoying with my JBC iron here.

**Dave Jones:** Um I had it in here and well, I had it in the It goes to sleep when you put it in the stand uh like this. There it is in the stand there.

**Dave Jones:** You whack it in Yeah, it's got a sensor in there and it can detect when you put it in and it instantly heats up. Really quite neat. Um but I tried to uh change the temperature.

**Dave Jones:** Hold the tool, change the temperature. You can't change it when it's in the stand. Hopeless. And you So, you've got to hold it, but I'm holding it. And it still doesn't Look.

**Dave Jones:** There's some timeout thing. All right, there we go. You've got to press menu, enter. Oh, bloody hell. Hopeless. We only need this on 300. Really a good thermal mass soldering iron.

**Dave Jones:** Now, as I said before, large chisel tip soldering iron like this, we'll apply a little bit of solder to the bottom of that. Now, ordinarily um I'd recommend uh just tacking down one pin there on the corner, but if your um flux is actually uh tacky enough, it's going to hold the chip in place anyway.

**Dave Jones:** So, I'm just going to go for broke here and uh get in there and drag solder. No, there we go. The chip did actually move a little bit. Bit of a fail there.

**Dave Jones:** So, let's But, the good thing is that effectively allowed me to tack one of the pins in place there. So, there we go. And then I can just drag solder the rest of these pins.

**Dave Jones:** Look at that. Done. One side complete. And let's try the other side here. I've put a little bit more solder on my tip again, and we get in there and drag it back.

**Dave Jones:** And if some A lot of people ask, why do I shake when I solder? I normally don't. Usually I'm extremely good at that, but I am standing up here, leaning over my camera, getting in at the wrong angle.

**Dave Jones:** Uh, it all has to do with uh doing this on camera. Maybe that second pin up there, I haven't looked at that. Maybe that just needs another go there.

**Dave Jones:** There we go. Look at that. Perfectly soldered a uh 0.65 mm pin pitch um TSOP package in, you know, seconds, really. Too easy. And of course, you use exactly the same uh drag soldering technique on a quad flat pack like this ATmega here.

**Dave Jones:** No difference whatsoever. It doesn't matter about the pin pitch, whatever. You can do it on SO8 parts. Doesn't matter. Um usually I prefer to drag outwards like that rather than along the pins.

**Dave Jones:** Um well, I do do it both ways depending on the circumstances, but I just find it's a little bit more controlled if you just pull the iron out from the pins like that.

**Dave Jones:** Um but you can certainly just go along, bang, drag it right along the pins like that. Not a problem. And the key, of course, is the solder mask between the pins.

**Dave Jones:** And hopefully you can see that in there. You can see the solder mask just go at the little slither of solder mask going between the individual pads there. And that's the key to prevent uh solder bridges on these sorts of pads when you do drag soldering along the pins like that.

**Dave Jones:** So, if you're doing a very fine pitch part, this one's a 0.65 mm, which you know, isn't too bad. You can easily, even a cheaper PCB manufacturer, you can get the solder mask between the pads on there.

**Dave Jones:** But say if you got a 0.5 mm or something, you may actually not be able to your cheap manufacturer of your board may not be able to get that solder mask between pins.

**Dave Jones:** In that case, then you do want to do that drag soldering out, the technique I just showed there, dragging out from the pins like that instead of dragging along like that.

**Dave Jones:** It just start prevents, helps prevent individual shorts between the pins. So there you have it, there's our beautifully soldered chip. Piece of cake, you can do it with any normal soldering iron whatsoever.

**Dave Jones:** Just a decent chisel tip. So if you like these soldering videos, please give them a big thumbs up. If you want to discuss it, jump on over to the EVBlog forum.

**Dave Jones:** Catch you next time.
