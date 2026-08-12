---
video_id: UmD7F0--7Lc
title: EEVblog #437 - Removing SMD Parts with ChipQuik
url: https://www.youtube.com/watch?v=UmD7F0--7Lc
source: youtube-asr
---

**Dave Jones:** Hi, it's time for another soldering repair video. Now, ever since those LeCroy videos I did where I was trying to repair the LeCroy oscilloscope and I ripped off this huge quad flat pack ASIC rather brutally and medieval actually because I didn't need the chip

**Dave Jones:** again. And so, yeah, I just cut the pins and ripped the damn thing off. And a lot of people said, "Well, why don't you use Chip Quik?" And well, I don't have any Chip Quik. So, the makers of Chip Quik,

**Dave Jones:** they must have thought the same thing. They've sent me some. So, let's give it a go, this low melting point Chip Quik repair stuff. And it's supposed to be just that, low melting point solder that you can put on

**Dave Jones:** your chip so that you can heat up all the pins at once and safely remove the chip without using a special hot air attachment, which is the traditional method for getting off a large pin count quad flat pack. Is it

**Dave Jones:** any good? Hey, we'll find out. And here it is, it's the Chip Quik patented ooh SMD removal kit SMD 1. And well, it's about $16 or something like that. Might be more or less depending on where you get it from

**Dave Jones:** in what country. And what you get is a bit of flux in a little tube there, Chip Quik flux SMD 291 no clean paste flux. I don't think there's anything special with that flux. It's just a regular gel

**Dave Jones:** type flux. You could probably use any main type of flux you like. And there's some of the low melting point solder alloy, the special patented alloy, which is what gives this thing its magic apparently. And you get some 70% isopropyl alcohol

**Dave Jones:** wipes as well. No big deal, but that's the alloy you're paying for. And apparently, it's very expensive stuff if you want to buy a lot of it, um it's not cheap at all. So, um use sparingly. So, apparently this is enough to do like

**Dave Jones:** eight to 10 chips, they claim, depends on the size. And it's apparently really easy to use. You uh apply flux to all the leads, you melt the uh Chip Quick alloy on all the pins, and you uh heat

**Dave Jones:** it up and maintain that uh alloy in a molten state, so you can uh remove the chip and just take it off with a pick up tool. That's it. Mhm. Is it that easy? We'll find out. And if

**Dave Jones:** you want to get these 70% isopropyl wipes, pretty handy things to have around the lab for all sorts of purposes, not only uh cleaning boards, but for cleaning all sorts of stuff, then you can get them from your local

**Dave Jones:** chemist in that large boxes like this, um exactly the same stuff. They're for medical uses, cleaning down your skin and uh stuff like that before you um uh you know, inject yourself or do something like that. So, available

**Dave Jones:** cheaply at uh any chemist or drugstore for you Yanks. And here is up close a special Chip Quick patented uh low melting point alloy. How low? Well, they claim it's around 58° C. Crikey, that's like as hot as my old

**Dave Jones:** uh lab used to get in the middle of summer here. And uh here it is compared to regular uh 60/40 uh tin solder. It looks a bit uh shinier and brighter. And as you can see on the end there, it's

**Dave Jones:** actually broken off. It's pretty brittle this stuff. If you have a look at regular solder, it's uh not very brittle at all. Of course, you can bend it like that, all sorts of ways, and you know, it really takes some breaking. But this

**Dave Jones:** Chip Quick stuff, just whoop, that just broke straight off. Now, they're not actually telling you that I could find anyway what sort of alloy this is and uh why it's patented. I mean, I'm sure it's been done before. Um they also sell uh uh low

**Dave Jones:** melting point uh solder paste as well, but that's just regular um um 42% tin 58% uh bismuth paste that you can get from many different manufacturers, and that has a lower melting point, you know, 130 something degrees, 138

**Dave Jones:** degrees, I think, something like that. But, they claim this uh wire alloy does 58° C. Woo. So, it doesn't melt at a very low temperature. Well, let's find out. I've got my hot air gun here set to 100° C

**Dave Jones:** because all of my soldering irons only go down to a minimum of 200° C. So, here it is, around 100° on the hot air. Let's have a look.

**Dave Jones:** Is that starting to do anything? I don't know. Not sure. Doesn't uh No, 100° doesn't seem to be Oh, yeah. Look. Look. Look at that. There you go. That's only 100° C. Brilliant. Brilliant. And let's see how long it stays molten

**Dave Jones:** at 100 Look, it's still it's still, even after a couple of seconds, is still pretty molten. Wow. So, let's compare it with that regular 60/40 solder and see how long it uh stays molten at a higher uh well, a

**Dave Jones:** regular soldering temperature. So, I've got my JBC iron here set to 280°, which is uh you know, um a fairly average low temperature for a soldering iron. So, the top one is the quick chip, and the bottom one is regular 60/40 lead solder.

**Dave Jones:** So, let's melt molten Keep that molten. There we go. Let's leave it there for a few seconds, and as you can see, it stays molten for I don't know, for three or four seconds, something like that, without any uh you

**Dave Jones:** know, major thermal uh effects, maybe a little from the ground plane underneath there, but uh yeah, it doesn't stay molten very long. That means that uh on a big quad flat pack, you can't just heat up all four sides at once with your

**Dave Jones:** regular soldering iron and expect to be able to desolder it. By the time you get around all four sides, it's gone. So, let's compare that to the Chip Quik. Here we go. Look at that. So, let's heat that up,

**Dave Jones:** leave it there for a couple of seconds, and it is still molten three, four, five, six, seven. Uh you know, like you know, at least twice as long. And of course, the way this stuff works is if you combine it with regular

**Dave Jones:** solder, then it lowers the melting point of the whole alloy, of course, because you've effectively changed the alloy. You've added whatever alloy is in here to this alloy, and you've created a composite alloy. So, let's try that. Let's bring this over,

**Dave Jones:** and put that all in the So, we've added our Chip Quik to regular 60/40 stuff, and let's give that a go. And as you can see, it stays molten for longer. So, let me just add more to that.

**Dave Jones:** More Chip Quik in there. There we go. And so, we'll keep that all molten, and as you can see, still stays molten for Yeah, a fair amount of time, and then it starts to really go uh crystalline and stuff like that. So,

**Dave Jones:** what good is that? Well, let's say we wanted to remove, without damaging all the pads, this huge Spartan uh FPGA. It's an XC30S in a 208-pin quad flat pack. 52 pins per side. It's quite a large one. You know, you don't get too

**Dave Jones:** many uh bigger ones than that. So, it's not a bad example at all. How would Would normally remove this? Well, you would normally remove it with a um a specific hot air attachment that actually blew hot air over all four

**Dave Jones:** sides. And you usually, if you want to do it properly, you buy a hot air attachment that is designed for your specific size chip. So, if you got a hot air gun, you usually need a whole bunch of attachments for your specific chip,

**Dave Jones:** which is okay for a big company or something like that, you know, for a known product that you have to remove all the time. But, just one-off Well, how do you do it? It ain't easy unless you got this Chip Quik, or you go along,

**Dave Jones:** like I did in that previous video, and physically cut all the pins off like that. But, you got to be careful that you don't actually cause damage to the chip. But, with this Chip Quik, we should be able to put solder The idea

**Dave Jones:** is put solder on all four sides of this chip, and it'll stay molten long enough on all four sides to lift the chip off. That's the theory. All right. Now, let's give this a go. Now, we're going to need

**Dave Jones:** a pick up tool to, you know, a vacuum tool to extract this off once we melt all the pins. Now, if you don't have one, cheap and easy solution, some Blu Tack like this, whack it on the end of a

**Dave Jones:** screwdriver. It's nice and tacky. Very low cost. You can stick that in the middle of the chip like that, and you should be able to I mean, I can lift that whole board up. So, we should be able to easily lift that chip off. All

**Dave Jones:** right. Let's give it a go. It's supposed to be easy. Now, bear in mind, this is the very first time I've done this. I've never used Chip Quik before. I've haven't practiced. So, I'm doing it first time exactly as you would.

**Dave Jones:** Perhaps, I'd highly recommend if you get an important part, you practice. But, anyway, let's put the flux on all the pins there. And as I said, it probably doesn't matter what flux you use here. All right. So, we have the flux on all the

**Dave Jones:** pins. Let's get my iron chisel tip, of course. And I've set it. You don't want it too high. I've set it for about 280° or thereabouts, Celsius by the way. Everything I say is in Celsius because you don't want to get it too hot and

**Dave Jones:** lift off the pad. So, it's a bit of a compromise between how hot you get it to how long it stays molten to, you know, risk of lifting those pads. So, anyway, here we go. Let's give it a go. I expect

**Dave Jones:** a lot of fuming for the uh all the flux in there. But, we really need to use a fair bit of this to get on every pin along there. So, and be careful you don't put too much pressure

**Dave Jones:** on this, by the way. Blow that those fumes away because you don't want to uh lift any of your pads or your pins. So, just don't put much any pressure at all, really, on your iron. You're just trying

**Dave Jones:** to add solder to those pins. So, oops, I just broke it off. It's very brittle stuff. Let me go around and add solder to all these pins, and we might come back. And then we'll go around and reheat this

**Dave Jones:** stuff and see if that chip just lifts off. And here we go, the moment of truth. Once again, my iron set to 280°. So, I'll go around and heat up all these pins. Once again, being very careful not to

**Dave Jones:** put pressure on those pins at all. And going around, keeping it all molten while supposedly I don't feel it coming yet.

**Dave Jones:** No. It's not coming yet. It seems to be staying molten on all sides, but uh No, maybe I need to give my chip a good week There we go, it's coming off. Woohoo! Look at that. Beautiful.

**Dave Jones:** Now that And you can see the solder is still molten there. Quite a few Look at that. Jiggle, jiggle, jiggle. Uh quite a long time after the fact cuz there's still a lot of thermal mass. I mean, that's

**Dave Jones:** Look at that. Wow. I could probably get rid of those balls, actually. But anyway, you don't want to do that. Uh I don't care about this board, but if you wanted to, you wouldn't do that. You'd get it all over your board. Look

**Dave Jones:** at that. But that stayed molten for an awful long time there. And look, even on the chip here, it's still molten. But So, that's, you know, like 30 seconds later or something like that, easily. Like So, getting it up to 280°

**Dave Jones:** probably didn't need 280°, uh of course. So, we probably could have done that with a lower temp just to avoid uh damaging the chip, especially if you wanted to reuse the chip as or something like that. You probably could,

**Dave Jones:** um you know, clean up those pins perhaps and reuse it. But jeez, anyway, the whole idea is to get the chip off so that you can clean up the pads, solder on a new one. That's a win. Now, to clean up these pads, uh Chip

**Dave Jones:** Quik recommend going around with a um a cotton swab and uh actually a low um uh, temperature iron and uh clean them and them up dead isopropyl alcohol, clean them up that way. Uh, they don't recommend solder wick, but I'm going to

**Dave Jones:** use solder wick iron. I've got it set lower to, uh, 250° C. So, some of this I mean, we can just get rid of the big balls like that easily. And because it's still Look look look at that. It's just

**Dave Jones:** beautiful, this stuff. Look. So, you don't actually have to use your solder wick to clean that up. Just blob it all together like that. And then you can just peel that off. Let Let your solder mask do the work there. But,

**Dave Jones:** uh, then you want to go around, clean your pads. Do it using solder wick. The regular rules apply to, uh, very low temperature, of course, to, uh, ensure you don't damage any pads. I think we may have had one little pad damage down

**Dave Jones:** there. Ah, well. Maybe it's a bit high. Uh, maybe I was, uh, accidentally, uh, uh, moved it with the iron, you know, actually accidentally hit that pin with the iron or something like that. But, anyway, it's the first time I've ever

**Dave Jones:** used this stuff. It worked well. So, as you can see, yes, one little tiny pin in there is, uh, bent. So, maybe I was, you know, my iron accidentally touched that. Once again, doing this under the camera wasn't probably optimal angle. I wasn't

**Dave Jones:** spinning my board around and stuff like that to get the optimum iron angle. But, apart from that, there are no other pins lifted. So, I declare that, folks, to be a win. Just have to clean up some of the pads

**Dave Jones:** because, uh, one of the keys of, uh, reworking stuff like this is you need to get all the solder off those pads because, uh, you need it, uh, completely flat or as flat as you can get it when

**Dave Jones:** you put your, uh, chip down again, especially for large pin count fine, uh, pitch devices like, uh, this one. So, and of course, this, uh, Chip Quik stuff is probably not ideal if you're doing, a you know mill spec or a NASA spec

**Dave Jones:** soldering or something like that cuz you've added this alloy. Uh check out that. It's sort of like a frosted sort of Look look at that. So you've added this uh unknown alloy to your uh solder which is then going to be mixed on these pads

**Dave Jones:** even if you clean it off. There's still going to be some left on there of the So now you've even when you apply fresh uh solder uh flux and put the chip back on, you've still got some of that alloy is

**Dave Jones:** left in your joints and does that make them brittle? What does it do for you know um long life tin whiskers, all that sort of thing. So you know but um you don't really have to worry about that

**Dave Jones:** for you know uh sort of you know hobbyist or a one-off type stuff. It's only if you really take your soldering extremely seriously. And if you are using solder wick like this, don't make the common mistake of putting your soldering iron on and then

**Dave Jones:** dragging the thing across. That's bad. You're just going to lift the pads. You should go through and just dab each one like that and then move along. Move along. Yeah, it takes longer but you're not going to lift those pins off because

**Dave Jones:** if you drag that abrasive solder wick across your pins, you're just going to lift them. Really. Even if you've got a relatively low temperature on your iron. Don't do it. Even though I don't have a new chip to solder on.

**Dave Jones:** Sorry, I've already done uh soldering videos on uh a couple of different methods to do uh quad solder quad flat packs like this using uh drag soldering also paste uh reflow method as well. So I'll have to link those in if you want

**Dave Jones:** to see them. But apart from that there we go, folks. We are almost clean. There was a little bridge in there anyway. Let's not fuss. And to clean all that uh flux residue off there, you can get in there with

**Dave Jones:** your isopropyl alcohol pad and wipe it off, but these aren't the best things. I'd highly recommend getting your isopropyl PCB cleaning uh spray. You can just buy it. It's the same stuff. It's isopropyl alcohol or you can get the flux clean

**Dave Jones:** brand stuff and things like that. Clean it all up and there's our leftover chip and as you can see no pins damaged at all. You could you know there's a few pins pushed to the side or something like

**Dave Jones:** that, but in theory you could just get rid of that solder, wick that off and probably reuse that chip if you really needed to. All right, now I've got a little bit of practice on that. Let's try it again in real time. Little tiny

**Dave Jones:** quad flat pack here. Bit of flux on the pins. We'll do this in real time. See how easy it is. And it's a much smaller chip, so the thermal mass is uh much smaller that we have to keep

**Dave Jones:** molten. So, let's go in there. Apply our solder on all sides. Whoop. There we go. Be careful if you've got nearby passives, of course. You don't want to uh don't want to lift those or cause an issue there.

**Dave Jones:** And where's my tool to lift up? There we go. Gone. And the good thing is we can just lift the excess stuff off those pads. No problem at all and that was far too easy, man. Instant. I like this stuff.

**Dave Jones:** It works. And as you can see I don't have much left after doing that quad that large 208 pin quad flat pack or the end the uh smaller one. So, you know, it doesn't go very far at all. And uh really, you

**Dave Jones:** know, it's not cheap uh stuff, but it works absolutely perfectly. There's no damage to those chips. Trivial to remove them. And that was not some practice perfect soldering tutorial there, folks. That was the first time I've ever used

**Dave Jones:** it on large 208 pin quad flat pack. I didn't know what I was doing, and it worked a treat. So, certainly well worth having some of this stuff in your kit. Definitely. Um I'm going to buy some uh

**Dave Jones:** I've got some left, but uh I'll probably buy some more to uh keep in the kit just for those emergencies when you have to remove these chips types of chips and do it properly. Highly recommended. So, I hope you enjoyed that. Uh if you want to

**Dave Jones:** discuss it, jump on over to the EEVblog forum. And if you like these types of videos, please give them a big thumbs up. And uh I'll link in some of my other uh soldering videos as well. There'll be

**Dave Jones:** a playlist there. And I've got a whole bunch of them. Catch you next time.
