---
video_id: b9FC9fAlfQE
title: EEVblog #186 - Soldering Tutorial Part 3 - Surface Mount
url: https://www.youtube.com/watch?v=b9FC9fAlfQE
source: youtube-asr
timestamps: {"0": 0, "1": 30, "2": 45, "3": 83, "4": 99, "5": 136, "6": 172, "7": 194, "8": 210, "9": 242, "10": 261, "11": 297, "12": 327, "13": 356, "14": 385, "15": 410, "16": 441, "17": 479, "18": 511, "19": 544, "20": 582, "21": 602, "22": 627, "23": 656, "24": 689, "25": 718, "26": 750, "27": 782, "28": 814, "29": 844, "30": 860, "31": 890, "32": 913, "33": 929, "34": 956, "35": 986, "36": 1012, "37": 1038, "38": 1052, "39": 1089, "40": 1111, "41": 1140, "42": 1157, "43": 1172, "44": 1191, "45": 1211, "46": 1233, "47": 1248, "48": 1275, "49": 1295, "50": 1326, "51": 1351, "52": 1376, "53": 1391, "54": 1422, "55": 1459, "56": 1474, "57": 1505, "58": 1530, "59": 1552, "60": 1571, "61": 1586, "62": 1606, "63": 1620, "64": 1636, "65": 1667, "66": 1686, "67": 1715, "68": 1747, "69": 1784, "70": 1817, "71": 1842, "72": 1877, "73": 1897, "74": 1916, "75": 1941, "76": 1968, "77": 2001, "78": 2036, "79": 2050, "80": 2079, "81": 2107, "82": 2126, "83": 2157, "84": 2183, "85": 2215, "86": 2238, "87": 2261, "88": 2284, "89": 2314, "90": 2350, "91": 2369, "92": 2390}
---

**Dave Jones:** Hi, welcome to the AAVlog an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, it's surface mount soldering time part three in the hand soldering tutorial. And today we're going to do surface mount technology. We've looked at that the tools in the first part through hole components in the second part and surface mount a lot of people think it's a really hard but it's not.

**Dave Jones:** It's an absolute piece of cake. Use the basic techniques you did last time, few more little tricks and you can solder really first class stuff with not much experience at all and some very basic tools. Let's take a look at it.

**Dave Jones:** Let's start out by looking at some basic surface mount components here. Up here is your standard quarter watt through hole resistor everyone's familiar with. Now this is a 1206 size surface mount resistor. This is a 80805 surface mount ceramic capacitor. This is an the same size 0805 surface mount resistor. This is an 0603 surface mount resistor and this is an 0402 surface mount resistor. They do come even smaller than this tiny ones that are used in really ultra miniature mobile phones and things like that. Now the 1206 but these

**Dave Jones:** are the basic standard sizes that you'll deal with in terms of in terms of your basic resistors and capacitors, your basic passive components. Now the 1206 up here is an absolute monster. Stevie Wonder could solder this thing. It is so damn easy.

**Dave Jones:** Let me tell you now 0805s really very easy to do as as well. Once you get down to 0603 gets a little bit more touchy but I can easily do 0603 by eye. I don't need any magnification at all and you should yeah most people will generally be able to solder an 0603. So, if if you're designing your boards, especially for hand soldering, and even for surface mount soldering as well, try to avoid the 0402s. Now, I can do those by eye, just, but I much prefer to use

**Dave Jones:** to solder under either a times four or a times six magnification there, just so that I can, you know, just so that I can keep a much tighter control of how much solder I feed onto the the joint, and and just inspect the joint at the same time as I'm doing the component. So, if you're designing your own boards, I would stick to 0603 and up, because the once you get down to 0402, if if you're actually getting PCBs hand assembled prototype, they'll charge you a lot more for 0402s, cuz

**Dave Jones:** they will generally solder them under the microscope as well. Whereas, if you're getting some prototype board hand soldered, 0603 and up, they can do by eye. So, really, just put some thought into which components you use. Don't just jump right in and use 0402s. Now, for today's example, I am just going to solder an 0603 part.

**Dave Jones:** And if you're talking about automated pick and place assembly of your boards, when you're designing your boards, put a bit of thought into it. Once again, if you use 0402s, you might be in trouble, because there are basically two classes or two technologies of surface mount pick and place machines.

**Dave Jones:** Cheaper and older designs can only do 0603 and above components to to at least a reliable level. They might be able to do 0402, but their yield isn't as good. So, if you're getting your board assembled by a manufacturer, they may actually charge you more to use to place 0402 components, cuz they might have to use one of their more advanced machines. Uh the yield might not be as good and things like that. So, just put a bit of thought into it. It might cost you a bit more to go down there. So,

**Dave Jones:** don't make it an arbitrary choice to go to 0402s. Make sure you have a reason to do it. Now, here's our 0603 resistor that we're going to solder onto this board. And as you can see, it's going to be fairly easy because the pads are actually quite large in comparison to the component.

**Dave Jones:** They do actually extend out further, and this is great for hand soldering. Now, if you're going to if you're laying out your own boards like this, the IPC footprints, the international standard footprints, they actually come in three basic sizes. What's called normal, least, and most pad size. Now, I'd recommend using the normal or the most pad size. Most means it's got the largest pad size, and they're the ones that are suitable for getting your iron in in there to make contact with both the pad and the and the end cap on the

**Dave Jones:** component at the same time. And that's important. If you use the least pad size or even a custom pad size, some pads are really no bigger than the tiny little end cap on that resistor. And really, there's no way that you can actually get your iron in there to make contact with both. You could have put solder on the end and bring it over and maybe get under there and actually thermal or even thermally transfer the heat through the cap onto the pad, and it gets really nasty. So,

**Dave Jones:** just if you're actually designing your boards and you think that they may be reworked, hand soldered, or they're going to prototypes going to be assembled hand soldered, if if you can afford the room on your board, if it's not a super compact layout, highly recommend you go for a larger pad size so that you can get that thermal contact. Now, uh we're going to use a contact we're going to use a method today called the uh tack and reflow method uh for doing these components. And it you as you'll

**Dave Jones:** see later, it applies to other parts as well. It basically uh it it basically means that we're going to tack the component down first and then solder the uh other side. And if I'm doing a whole array of components like this, I would do it in like a batch process. Um as as you'll I'll do a single resistor here, but if I'm doing a whole bunch like this, uh I would go through and apply solder to I'll do one step, apply solder to all these pads first. And then I will

**Dave Jones:** go and place my resistor and then uh tack it down. Tack tack the resistor down onto each pad as a second uh batch step. And then I'll flip my board around to the other side. Or if you're left-handed, if you're am- ambidextrous, you can solder with both hands, you can then you go through and you complete the joint on the other side. So, that's a batch process, but I only show a single resistor today.

**Dave Jones:** Now, we aren't going to need any flux for this cuz there's uh flux built into this so- into the core of the solder here. So, let's actually just apply a small amount of solder, just a tiny amount onto that pad there, and that will allow us to tack down this component. So, if we grab it with the tweezers like this and we get in there. It's important to uh make sure the component doesn't flip up like that. It's hard on the camera. I can't get my tweezers down vertical. But

**Dave Jones:** if I get my resistor in there and I just reflow it like that. And really, we've soldered one side of the resistor there. Beautiful. And we just flip our board around like that. And we go in, grab our iron again, and get in there with our Once again, I'm using uh very fine solder, 0.46 mm solder, tiny stuff. I highly recommend you get that size or smaller for this kind of surface mount work. Forget using 0.7 or 1 mm solder. Really, you're going to do a horrible job. You're going to

**Dave Jones:** feed too much solder in there. It'll It'll just look very amateurish. It'll be horrible. Trust me. Spend good money, get good quality fine solder. And we go in there and we just There we go. We just tack down the solder the other side of that component. And bingo, we've soldered an 0603 surface mount resistor. And it's the same for a capacitor. It's the same for 0402 size, 1206, 0805, whatever. Or it's also very similar for other components like a SO-23 and things like that. So, it's really

**Dave Jones:** quite easy to solder these components. Give it a try. Piece of cake. And after you solder small parts like this, you just want to get in there with your jeweler's loop, one of these, or pure inspection microscope or something like that, and just check that that the resistors are soldered nicely. Just be And once again, it as with any solder joint, should be nice, shiny, very nice, shiny, and smooth finish. And it should have a very nice fillet there on either side of the resistor. That one there is slightly

**Dave Jones:** crooked, little bit off-center, but generally, that's not a bad job at all. Okay, now let's try and solder this very typical eight-pin SO package IC here. Very easy to do by hand, even if you're not even if you haven't done SMD soldering at all, because the pin pitch is reasonably large. It's half that of a standard DIP-based IC. Instead of 0.1 in, it's 0.05 in or 1.27 mm pin pitch in the metric scale. And that's actually quite large, and you can get in and with your soldering iron and actually

**Dave Jones:** individual and solder very fine solder and solder each individual pin. This is one way to do it do it. There are other methods, as we'll see, which better used on smaller pin pitch parts, but these SO packages I like to just solder each individual pin by hand with my iron.

**Dave Jones:** And how we going to do this is we're going to use the reflow the tack and reflow soldering method. So, I'm going to put my iron on there, and I'm going to just tin that little pad there. It It needs to be sort of you know, a a small size lump of solder on there. It's You don't want to tin it completely flat cuz then there won't be enough solder on there to actually tack down your component.

**Dave Jones:** And the whole idea is that we want to bring in our component. This is where our our tweezers can come in handy, and we want to actually tack that pin down on there like so. And that holds our chip in place, and we can solder the other pins. Flip that around to the other side, and we just want to solder the diagonally opposite pin. So, get your iron in that chisel tip, which heats up the pin and the pad at the same time, and just apply

**Dave Jones:** a small amount of solder in there, and it will You can it'll it'll just flow onto both the pin and the pad, and you should get a nice a very nice fillet in there. It's hard to get I can't really zoom in that much more than that, but you should get a really nice shiny finish as well with no burs and no things sticking out, no shorts to other pins. Because we've got the solder mask on these boards, solder mask is vital for surface mount soldering

**Dave Jones:** work. This is the red material that you see on the board, but it also comes in um other colors. You've seen uh green and there's uh blue and there's black and there's yellow and there's white and there's all sorts of colors that you can get, but solder mask is vital because the solder mask will actually go between each individual pad like that and it will prevent it will help prevent, unless you're really bad at soldering, prevent uh shorts between the individual pins and that's really important as

**Dave Jones:** we'll see on the much finer pin pitch uh components, but as you'll see, I can sort of, you know, solder all I want on trying to attempt to put solder onto this this solder mask, it'll blacken, but it will never ever take and uh by having the solder mask in between the individual pins like that on a board, it just um helps keep the solder out um because it's not uh sticky at all. The solder will uh just naturally want to flow into the individual pins and not

**Dave Jones:** get stuck between the pins. Place our iron there once again for a second or two just like uh through-hole work and apply the solder not to the iron itself, although it's hard when you're at this sort of um pin pitch, but uh apply it to the pin or the pad if you can get access to the pad and uh it will flow onto the joint like that. Bingo, we have one side nicely soldered and with uh practice, you can do this incredibly quickly um just as quick or even quicker

**Dave Jones:** than uh through-hole work. And then we'll get in there with our jeweler's loupe and we'll just have a look uh to make sure the uh solder joints are good and we can actually um see that there's no shorts in there. And as you can see, I got a little bit of um solder splash onto this pad here. You got to be careful not to do that. Um it's because I'm working under the camera here and I have to use a shallower uh angle soldering iron at the

**Dave Jones:** shallowest a shallower angle than I normally would, but as you can see those joints have turned out quite nice because I've used 0.46 mm solder. I've used a nice chisel point soldering iron which allowed me to hit the pin and the pad at the same time. I was able to get in there nice and quick and that is a nicely soldered surface mount chip and it really is easy. Give it a go. Now, let's try and solder a much smaller pin pitch of 0.65 mm pitch device. Let's see

**Dave Jones:** how we go and remember it's got the solder mask in between the pads. Let's start out by tinning one of the pads, shall we?

**Dave Jones:** There we go. And this will allow us to reflow what's called reflow our part into position because this is the reflow soldering process because there's already solder on the pad itself and all we do is heat it up, be it with a soldering iron or with an infrared reflow oven or a toaster oven as you may be familiar with. A lot of people use those and this is how they mass assemble boards after they pick and place them using the reflow process.

**Dave Jones:** We've done a very similar thing here or an identical thing, but we've just used a hand soldering iron. And with this pin pitch I'm not actually using any visual magnification at all. I'm viewing this on the camcorder screen here, but I can solder these by eye. Okay, let's try and tack down the other corner here, shall we? If we can get in there.

**Dave Jones:** There we go. I think we've tacked down the other pin, so that chip can't move anymore. It's secured in place and we can to the other pins. Even if my alignment's a bit off there, I may need to uh reflow that and just shift it slightly.

**Dave Jones:** So, there we go. Just reflow that and just move the chip gently into place until those pins line up. Perfect. Now, there's one thing I forgot to use here and this is was the flux pin. I probably should have. With these surface mount parts, these surface mount ICs like this, I probably should have just pasted on a bit of a layer of a flux before onto all the pads before I soldered that chip into place.

**Dave Jones:** But, I'm just going to apply some just after the fact here. I'm just going to wet that a little bit on there so to help the solder take to that when I drag it right across with my well-based tip. And there you can actually see the residue the flux residue all around there like that. I sort of overdid it a bit there, but you can actually see it's in place. Too bad it's not actually under the pins, but it could actually flow back under and that will be good

**Dave Jones:** enough. Should be good enough. Okay, here we go. Let's feed some solder into the well here until we've got just enough to sort of make it sort of just swell out the bottom and let's see if we can do this.

**Dave Jones:** Bingo. Look at that. Magic. And there you go. That's almost a near perfect solder joint on each and every one of those pins. And all I did was drag the soldering iron across. I actually dragged it across a couple of times cuz I didn't get it first go. It's a bit harder under the camera and I haven't practiced today which is something that you should do before you start out on an important board. Just even no matter how experienced you are, just do a little practice run. Now,

**Dave Jones:** as you can see, we do have a tiny little bit uh two pins shorted together there, but we can get our trusty solder wick. This is the really thick stuff. This is where the super fine stuff would come in, and we'll just wick that away.

**Dave Jones:** Bingo, gone. And we have a perfectly soldered 0.65 mm pin pitch. And I don't know if you heard that on the camera, uh but there was a lot of uh sizzle there as well as the uh flux uh burned. And the the flux is really the key to doing this. I'll try and do exactly the same thing on the other side, okay, but I won't use any flux, and let's see what happens.

**Dave Jones:** Now, that one turned out uh okay. There's one little solder bridge there uh which I can fix up with either the uh solder wick, or I can just come back in with my wicking tip, okay? And just that will just uh suck that should, if I can get in there, suck that away like that. Now, that turned out all right, but uh it took a few uh swipes.

**Dave Jones:** It it didn't seem as clean to me um because the other side that had the flux on it just seemed to reflow much better. I just much preferred that. So, the flux can be really handy unless you got like a brand spanking new board fully clean, you've got a uh a brand spanking new component, and um you know, no oxidization, then you can do without the flux, but flux really helps. But there you go. That's how you can solder a 0.65 mm pin pitch. Uh you'd have a hard time

**Dave Jones:** doing those uh individually with each pin. You'd probably have to do it under a microscope to get a good result. But with one of these uh well based um tips, these things that actually have the well in them that wick the solder away. These wicking tips, they're great.

**Dave Jones:** Now, what we're going to have a go at is uh soldering this PIC24FJ. Not that it matters, it could be any uh chip, but it's a PIC24F uh 0.5 mm pitch quad flat pack. Let's see how we go.

**Dave Jones:** First thing we're going to do is just put some flux on these uh pads. Now, you can use a liquid uh base flux if you want. And uh really, because we've got the gold flash uh pads here, you don't necessarily um have to use flux like this, but uh I'm going to anyway, because flux is always a good thing.

**Dave Jones:** Trust me, it's the key to good surface mount soldering like this. And we're going to use our tack and reflow method here, so I'm just going to put a little bit of solder on that uh second pin there, cuz I didn't have to worry about getting it on the first one there, and we're going to tack that component in place in at least two corners.

**Dave Jones:** And we'll just reflow that pin there. There we go. And we'll just tack and we'll just tack solder a second pin there. We can clean that up later, it doesn't matter if we've got a short there. And just to be sure, we'll add some more flux along there, because you can never have too much.

**Dave Jones:** Now, the technique we've been using here is called drag soldering. As you've seen, we drag the soldering iron over the pins. And I've showed you it with a well-based uh tip, but you don't have to have a well-based tip. You can have a standard chisel like we've been using.

**Dave Jones:** And now, what you can In fact, some people will say it's better to use a chisel, but well, I don't know. Um take your pick, really. But we can do drag-based soldering with a well with a regular chisel tip as well. Let's give it a go. Here we go. We've got a 0.5 mm pin pitch part. This is quite a very small part, pretty much as small as they get. So, we've got some solder on the back side of that. Let's give it a go.

**Dave Jones:** There we go. It's not necessarily the cleanest result there um because there's a probably a bit too much uh solder got on the on the pins, but we can actually clean that up. You can actually drag the iron back out like that and get the solder off those pins, no problems at all.

**Dave Jones:** But, look at that. We have created We've soldered easily soldered a 0.5 mm pin pitch part. And granted it's really easy if you've got uh these larger longer pads that you can actually get the iron onto. So, if you're laying out your board like this for these 0.5 mm quad flat packs, it doesn't matter what size. This can be a big two or 300 pin quad flat pack and you'll solder it just as easily and just as quickly.

**Dave Jones:** And to finish off this chip, you would just do exactly the same thing on all four sides. And uh clean it up with a little bit of solder wick if you have to or as I showed just dragging the iron back away from the pins. Now, this one really helps because it's got really long It's a prototype board, so it's got really long uh pads like this. And uh I don't recommend you when you're laying out footprints to make them this long, but something like these pads over

**Dave Jones:** here is would be a really nice size exposed pad there so that you can get your uh chisel tip iron or the solder the molten solder the ball of solder either in your well or on your chisel tip um so that it actually makes decent uh contact thermal contact with the pad itself as well as the pin and then with the flux, it all just flows beautifully.

**Dave Jones:** And it all has to do with the surface tension of the solder because you know, some people look at this and they think it's just amazing how you can solder a 0.5 mm pin pitch part with a couple of millimeter diameter chisel tip like this. You would think it's impossible.

**Dave Jones:** Well, it's not. It's because of the surface tension of the solder. It just wants to stay on the iron either or stay in the well tip or the chisel tip and it doesn't as we showed it doesn't want to stick to the solder mask, the red solder mask material which is between the pads and it wants to actually just reflow onto the pads itself and with the flux there to help clean it. So, really it's it is almost like magic and there's no trick to it at

**Dave Jones:** all. It really is that easy. And if you don't feel comfortable actually dragging your iron all the way along these pins, especially the very large packages, you don't have to actually drag it along. You can actually just drag the individual pins backwards as we saw like this. You can actually just get them like that and just touch it in like that. If that's another technique you can use. It's not as quick and efficient, but you can actually say that it is a bit it's a bit more precise than the

**Dave Jones:** technique of dragging them actually across the chip like that. So, you can drag back. It might take you a little bit more, but you can actually get a bit more a bit more precise feel and there you go. It's just that simple application of the iron.

**Dave Jones:** We have pretty much perfectly soldered one side of that quad flat pack. And as with any solder joint, each one has to be a really nice shiny joint with a a really nice fillet. It's it's really hard to get. Sorry, I can't actually zoom any closer like this under the camera, but you can see that really uh, only took me a couple of seconds and each joint is pretty much almost perfectly formed.

**Dave Jones:** And as I mentioned in the first part of the tutorial, my soldering iron there is set to about 350°. You certainly wouldn't want, uh, any higher than that. Anywhere from 300 to 350 is is really going to do the trick for, uh, uh, for fine surface mount work like this because if you make it too hot, you can actually lift the pads. You have to be careful. And especially if you apply too much pressure. If with your iron, if you come across here and actually apply

**Dave Jones:** a lot of pressure as you're sweeping across like that, uh, you can actually lift the pads. So, just be careful that you apply very light pressure. And in and in the case of the, uh, well, uh, base tip, you really shouldn't even need to touch it. As long as the, uh, the molten ball of solder actually makes, uh, contact, thermal contact with the pin and the pad, it's going to reflow.

**Dave Jones:** So, really, you should shouldn't be having any pressure at all on there. If you are, just very, very light. There's another technique that some people like, uh, to use and, uh, you can actually use, uh, solder paste. This is, uh, just some basic, uh, solder paste with a little, um, in a in a syringe like this.

**Dave Jones:** And, uh, you can actually just apply a small amount of, uh, solder paste either either before you lay the chip, uh, down or or you can even do it after, which, uh, I'll show an example of here, but you really have to get just the right amount of, uh, paste on there.

**Dave Jones:** Otherwise, you end up with too much and then you've got to clean it off. But anyway, let's give it a go. Let's see if we can apply a small amount of paste across here. It's got, uh, uh, it's quite hard under the camera here, but anyway, let's give that a go and see what happens.

**Dave Jones:** And you can likely hear that I've got my, um, uh, hot air gun here. Once again, set to about 350° and with a reasonable air flow on there and let's heat up this and see if we can do it.

**Dave Jones:** Normally I'd get this right down vertical, but uh I can't do that with the camera in the way, unfortunately. Go on this, but it should There we go. There we go. It's finally reflowing. Bingo.

**Dave Jones:** And that's not a bad result. I'd say I've used slightly too much uh solder paste there. As you can see, it's actually quite hard to dispense the correct amount of paste and of course this way this is where you get into uh solder stencils and proper reflow soldering with a thermal oven, which won't be in this tutorial cuz this is about uh hand soldering. It's not about um doing a solder paste uh stencil, but um there there you go. You can actually use a syringe-based uh paste and once

**Dave Jones:** again, you can go along with your iron or your wick later and you can actually clean up that um generally you're going to end up you're usually going to end up with uh more solder than uh not. Generally it's it's hard to put a very tiny amount on there unless you've got a specific uh paste dispenser. You can get um automated uh pump-based dispensers.

**Dave Jones:** They only dispense a certain amount of paste and you can go along and and actually apply it to each pad and go along and go bang bang bang bang on each pad like a little drop just before you place the chip down, but jeez, if you got to do that, well, probably may as well do the um stencil as well, but there are some cases where you actually want to rework uh boards with the components all around where you can't actually get in there and do a so- or it's not as easy to use

**Dave Jones:** one of those uh solder paste uh stencils. So, you may have to use one of those um pump solder paste uh solder paste-based dispensers to just dispense the correct amount of paste on each sharp pad. And you can actually get machines to do that as well. And I've got another video which I'll link to here which actually shows you a very expensive high-end machine that can actually dispense paste onto individual pads in a fully automated type process. And that's good for reworking VGA components and things like

**Dave Jones:** that. Now, you'll notice that I've been using a gold-plated or gold-flashed prototyping board here. Now, if you're going to do really high-density fine surface mount work, I highly recommend that you get your boards manufactured with these gold flashed pads because it is just A, it's easier to solder to, everything takes better, the flux takes, you don't have to use as much flux. It's just nicer, it doesn't doesn't corrode as much. And it's just And the other thing is that it is a much flatter surface. And that's quite

**Dave Jones:** important when you get down to quite fine pin pitches. You can get finer stuff than this. And if you get BGAs, it's actually quite important that you that that the chip actually sits on all the pads quite flat. Now, if you compare that with a what's called a hot air level solder finished board, here's a typical one. It's it's not it's not the gold flash. It's just a solder a tin plate solder finish on the pads here. And you probably can't see it under the camera

**Dave Jones:** there, but the finish is it is lumpier. And and the chip doesn't sit as flash flush as flat to the board. And if you've got like a BGA or something like that with the little balls in there, if you just get one pad that's got a bit of excess solder on it, then you're going to get a horrible result. So, really it doesn't cost all that much more.

**Dave Jones:** You know, it might even cost a few cents uh per board really to get the the gold flash pads. I highly recommend it. Now, let's try and solder on this a higher thermal capacity D pack here. The others have been really easy because our soldering iron hasn't sweated the smaller stuff at all. But as you can see this large rather large device has a huge pad on the bottom and a matching pad here which is connected to a well, it's a reasonably large little heat sink here. A sort of a heat sink

**Dave Jones:** ground plane. So, let's solder that in place and see if we can do that at the same soldering temperature we used before 350° C with the same chip our our chisel tip we used before and see how we go on that. See how long it takes to solder something of this thermal capacity.

**Dave Jones:** And of course we're going to want to have to tack this in place as well. So, we'll just put a bit of solder on that pad there and we'll just bring our device in and we'll reflow that in place.

**Dave Jones:** No problems. Do the other pad. Now, as you can see we don't actually have any pad area there to actually apply our solder to. Our well, our iron to. So, we really have to apply put the iron on top of the leg, apply pressure and feed in solder from the bottom like that and it reflows onto the pad and then onto the leg as well.

**Dave Jones:** Now, I'm going to use my standard chisel medium size chisel tip here. I've still got my iron set to 350° as we've been using up until now, but I've got this large amount of copper. Let's Let's see how it goes. Now, one method to actually do even well, larger devices like this and this is actually quite a small device a D pack. You know, if you've got a large TO220 and you're trying to solder to the tab or something like that you may actually want to

**Dave Jones:** preheat it what's called a preheating process where you would that's where your hot air gun might come in handy. You would actually heat up all of the surrounding copper in the pad and the component first and then you can get in there with your solder and require less time. Anyway, let's let's not discuss that today. Let's actually get our iron in there. Try and get it on the pad and the device as well at the same time and let's try and get our solder in there. Now at the moment you know, we're

**Dave Jones:** trying to apply it to the pad and that's really not working that well. This is where okay, we're going to have to put some solder onto our under our tip like that so that we're we can actually better thermally couple onto both the pad and the device. So we've now got solder on there and you can see it already starting to flow onto the pad and there we go. Bang. Starting to flow along and it's starting to heat up both.

**Dave Jones:** But as you can see it's taking a bit of it's taking a bit of effort. You can actually see parts of it cool while the others actually heated actually heating up and is molten. The other end of it just instantly cools and solidifies.

**Dave Jones:** Look at that. But there you go. We've actually now completed that. But this is actually this isn't ideal because it's only actually attached to the top. We haven't actually reflowed any under the bottom. This is where some thermal paste would come in handy to actually put some paste on the bottom of that device and then you would actually reflow that with your hot air gun on top. But anyway, that's that's not that's okay for just a simple art prototype.

**Dave Jones:** But of course, I'm not entirely happy with that look. It's it's it's all lumpy and it doesn't, you know, it's all craggy. I don't like it. It's not as shiny as it should be. So, let's get our iron back on there, shall we? Try and we we try and get this one flat to apply a much much more even heat. So, we'll leave it there for 5 seconds or so and we can heat up both the pad and the device. And this is where we might want to turn our

**Dave Jones:** temperature up a tad. Um but as you can see, we're already starting to get a much better uh a much better wetting between both surfaces there. And we've probably got a little bit too much solder there, actually. Um so, it's not going to look perfect, but that is better than what we had before.

**Dave Jones:** And there you go. That is quite a nice uh shiny, smooth result there. And that device is still hot. Um it's still very hot after the process. But these larger components can actually uh take more of the heat like this and they will actually uh trap the heat for longer. So, just uh be careful not to touch them cuz um after you've soldered them cuz they will still be hot, retaining that heat as part of their thermal capacity. That's their job. Now, with these uh small components like

**Dave Jones:** this, these passive components, they can be uh quite easily damaged by excess heat. You have to be very careful with them. Um it could be because there's no thermal capacity in there at all. So, uh so, all most of the temperature of your iron is going to go straight into that component very quickly. Uh multi-layer ceramic ceramic capacitors are one example of components that can be really damaged very easily with excess heat.

**Dave Jones:** So, you want to be very quick and and want to use as lower temperature as you can get away with with these devices. Um otherwise, you can lift the end caps off them and and your boards as well, your FR4 PCB material. You can get different temperature grades, which will handle heat better than some will handle heat better than others. But if you've got a poor quality FR4 material that uses poor poor quality glue and resins and things like that to actually stick the copper down

**Dave Jones:** to the FR4 for material, then really you um these pads can actually lift straight off the board if you have excess heat or leave it there for too long. So, just be aware of that. Let's actually see if we can do that. I've turned the soldering iron up to 450° C and I'm going to heat up this pad here.

**Dave Jones:** Now, it could take a little bit and especially it it it does it a lot when you when you're doing rework and stuff like that. If you have to rework several devices, but there we go. Bingo, it's gone. There we go. We've lifted Check it out. We've totally lifted that pin up. It's buggered. Look at it.

**Dave Jones:** See? It's just totally floating and hanging on to to the trace like that. Thank goodness that that the copper actually still hangs on there. So, you can actually if you're very careful, you can actually push push those back into place. If you do lift them, can push it back into place and then still solder your IC on top. But you got to be careful of that.

**Dave Jones:** That's what can happen with too high a temperature. I told you it was easy. Look at that. 0.5 mm pin pitch parts. Why be scared of it? You can do it in a couple of seconds with just very basic tools and hardly any experience at all. It's unbelievably simple. Now, we didn't cover solder stenciling, which is a different technique and put it in in the reflow oven and things like that. Maybe we'll cover that sometime in the future, but this is just hand soldering, and you

**Dave Jones:** need good hand soldering skills, even if you're going to stencil and reflow your own boards, cuz sooner or later, you're going to have to rework parts and rework soldering techniques are slightly different as well, especially removing parts. Maybe we'll do another tutorial on just reworking parts, but hand soldering skills, very important, and there's no need to be scared of any components like this. Surface mount components are easy to do. Basic chisel tip soldering iron, some fine solder, a well-designed board with well-designed pads, and the solder mask, make sure you get the

**Dave Jones:** solder mask between the pins when you're laying out the board. Watch for solder mask expansion. Go Google that. To I think I've probably done that in a previous tutorial. Solder mask expansion is important to get that right. But if you get those things right, you can solder all these boards yourself at home very quickly, very professionally.

**Dave Jones:** Simple, basic tools. So there you go. I hope you learned something, and go out there. Don't be afraid of surface mount parts. They're a piece of cake. See you next time.

**Dave Jones:** And don't forget your flux. Flux is everything.
