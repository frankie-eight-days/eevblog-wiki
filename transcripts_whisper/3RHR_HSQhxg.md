---
video_id: 3RHR_HSQhxg
title: EEVblog #623 - See Through Thermal Camera Followup
url: https://www.youtube.com/watch?v=3RHR_HSQhxg
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 13, "2": 33, "3": 49, "4": 65, "5": 77, "6": 97, "7": 118, "8": 134, "9": 150, "10": 170, "11": 186, "12": 202, "13": 218, "14": 235, "15": 255, "16": 267, "17": 287, "18": 307, "19": 323, "20": 344, "21": 364, "22": 384, "23": 400, "24": 417, "25": 437, "26": 453, "27": 473, "28": 490, "29": 510, "30": 531, "31": 551, "32": 571, "33": 592, "34": 612, "35": 632, "36": 652, "37": 673, "38": 689}
---

**Dave Jones:** Hi. In a previous video, I showed how you could make your product effectively transparent to a thermal imaging camera, even when you have the lid on. And you can do that using cling wrap, because cling wrap is both visually transparent, obviously, as well as thermally transparent.

**Dave Jones:** That's why you can still see me through, on this thermal imaging camera, through this cling wrap. And that's really useful to be able to see the performance inside your product, the airflow, the thermal dynamics, and your components heating up and things like that, with the lid on,

**Dave Jones:** with the cling wrap. And that's really useful. But it seems kind of obvious that cling wrap is both visually and thermally transparent, because we always think in terms of visual. But that's not always the case. There are materials where you can see through them visually like this, but they're opaque

**Dave Jones:** to a thermal imaging camera like this. And I'll show you those in a minute. And vice versa, there are materials that are transparent thermally to this thermal imaging camera, but you can't see through them visually. And I'll demonstrate that now. Prepare to have your mind blown.

**Dave Jones:** Look at this. Just a regular plastic shopping bag from RS Components. I've been buying some components. Visually opaque. You can't see through this. If I put this bag on my head, which is probably an improvement, you won't be able to see me on my camcorder here visually.

**Dave Jones:** But watch the thermal imaging camera. Ha ha! Crikey! Look at that! You can see right through. You can see my head straight through this bag, because it is thermally transparent but visually opaque. Ha! Beauty! And then at the opposite end of the scale, you've got this glass.

**Dave Jones:** Obviously visually transparent, as you know. But watch the thermal imaging camera. Ta-da! It completely blacks me out. There's a few reflections on there, thermal reflections of my overhead light, and you can see those visually as well on my camera. But the thermal energy cannot get through

**Dave Jones:** this glass, regardless of how thin it is. It just doesn't work. The material is not designed to pass thermal energy. And that is why this FLIR E8 thermal imaging camera here doesn't use a glass lens like my camcorder here does, because it wouldn't let through

**Dave Jones:** the thermal energy. It'd just block it. So it actually uses a germanium lens, really expensive germanium lens, that is very transparent in that thermal IR range that this camera is designed to operate at. So how does all this magic happen? Well, you probably need a

**Dave Jones:** physicist to explain it properly, and I'm just, well, a humble electronics engineer. But it all has to do with bandgap energy levels. Certain materials have different bandgap energy levels in them, and different types of light, be they visual light or thermal light, which is lower in frequency, either be absorbed or let through depending

**Dave Jones:** on the bandgap energy level in the material. That's why you can visually see through this, but thermally can't. And you visually can't see through this, but thermally you can. And the cling wrap just happens to be really, really good at passing both. But some other type of energy

**Dave Jones:** it may not let through at all. So there you go. All has to do with physics. Love physics. Beauty. In my previous video, a lot of people mentioned the cling wrap I use could generate ESD, and that could damage electronics. Well, yes, it's possible.

**Dave Jones:** And yes, cling wrap, of course, does generate ESD. By the way, if you haven't seen the previous video, I'll link it in down below. So I thought I would just measure that and see what the values we actually get, and if it's really going to be

**Dave Jones:** a major issue. This is just Kohl's brand cling wrap. I have no idea what type of cling wrap it is. There are many different types. Apparently some of the older ones work on electrostatic build-up and charge. The newer ones have chemicals added to make them sticky and all sorts of stuff.

**Dave Jones:** So not entirely sure what this one's made of. Anyway, generic Kohl's brand. It could have been, you know, it's just rebadged. Anyway, I've got my surface DC voltmeter here, and this will tell me the charge in kilovolts at 1 inch. So I've got to try and keep the cling wrap

**Dave Jones:** 1 inch away from the sensor. It's going to be near enough. We're just looking at ballpark readings here. So I'll reset it, and here we go. I'll take the cling wrap off the roll. I've got to step around my camera here, it's really quite annoying.

**Dave Jones:** And yeah, we expect some build-up, of course. We expect, be very surprised if this doesn't generate any charge build-up. Here we go. Yeah, we saw it peak at 2000 there, something like that. Okay, so it does certainly build up a charge. And if we lay it

**Dave Jones:** back down on the ESD mat here, and whoop, yeah, it's gone back down. Let's reset, let's reset it again. And if you bring it back up, yeah, it does build up that charge back up again. So there you go. So yes, it could be an issue if you're going to get these near your boards.

**Dave Jones:** I mean, obviously you wouldn't recommend wrapping your boards in it, but for putting it as a case over a product, eh, not a huge deal. Now of course, those sort of levels, you can generate more yourself. So you know, with your clothing and other stuff, walking across the carpet and other

**Dave Jones:** traditional methods of building up static. So really, yes, cling wrap could potentially be dangerous ESD-wise, but then so are you if you're not taking proper ESD precautions and everything else. So, you know, really, let's also test what happens if we roll it back onto this

**Dave Jones:** roll, and then unroll it again. Does it build up the same charge? Ta-da! No, it doesn't. Look at that. So if you want to minimise the charge on your cling wrap, just wrap it back up and then re-deploy it. Like that. And it's not a huge deal at all.

**Dave Jones:** It's not nearly the same as when you take the brand new stuff off the roll. And let's have a look, if I do the brand new stuff again. Here we go. Yeah, there we go. So that brand new stuff certainly builds up a charge.

**Dave Jones:** So is it a problem if we put it over a product as a lid? So let's take this PC as an example, and let's unfurl our cling wrap, and bring it in like this. Sorry. Yeah, it's generally, I've got to make sure it doesn't touch.

**Dave Jones:** There we go. I mean, you know, we're only talking a couple of hundred volts there. It's not a huge amount. It's not a huge, oh there we go, 500 at that point. But it hasn't, no, there we go, that could just be, nah, the movement of the thing.

**Dave Jones:** But anyway, it's not a huge, it's not as big a deal as you might think once it's on a grounded product like that. And if I do that again by rolling out the cling wrap from its already rolled out state, there we go.

**Dave Jones:** Not a huge deal. That's not a big deal, it's practically going down to zero there. So there you go, you do certainly need to be careful with cling wrap because it can build up a charge, and that is totally expected. So pros and cons of using cling wrap.

**Dave Jones:** Of course, the beautiful thing about cling wrap is that A, it's cheap and readily available from anywhere, and also that it's super thin and very thermally transparent. So if you want the utmost in thermal transparency, cling wrap is an awesome way to do it.

**Dave Jones:** Yeah, just be careful though. Although there are ways to mitigate that with the cling wrap. You can actually wash the cling wrap and actually remove the static charge as well. But if you are really concerned about ESD for your particular scenario using that thermal camera, there's other materials you can use.

**Dave Jones:** And you guessed it, these pink ESD bags of course. These also work a treat and are thermally transparent. Now these are made of polyethylene usually, but also polyethylene material as well. You can get these and they are fully thermally transparent. Not as good as the cling wrap, we'll test that in a minute.

**Dave Jones:** But yes, they do work. And look, they build up absolutely no charge at all. That's the whole idea of anti-static bags. They do not build up a charge. And I've done a video on that which I'll link in down below, how they technically do not fully protect your

**Dave Jones:** devices. They're just designed from ESD discharge. You can actually kill devices through these bags. But anyway, that's a different video. But yes, they are thermally transparent. Here we go, I'll prove it. Here's my hand, and I'll stick it in one of these pink ESD bags, and you can still

**Dave Jones:** see my hand. Look at that. Ta-da! And of course this one, they're both visually see-through and visually transparent as well, but also totally thermally, or not totally, but they are thermally transparent and they don't build up a charge. Beauty! And for those who will almost certainly

**Dave Jones:** ask, no, these metallized static shielding bags are not thermally transparent. Let's have a look in there. Oh no, that was my hand print. There we go, I can leave my hand print on there. Maybe I can flip it over and like that. But no, I can't stick my hand in there, those

**Dave Jones:** are not thermally transparent. Sorry! So is this pink ESD bag thermally as transparent as the cling wrap? Well, let's try it. I've cut it into a single piece, so it's not a bag anymore, it's just a single piece. And here we go, I will overlay it, and you can see it come in

**Dave Jones:** there, and it really, oh sorry, that was calibrated. It really does blur stuff out, and yeah, it's not nearly as good. You can see the maximum temperature go from 78 degrees here. You can watch that go down to yeah, drops down a lot, down to 63.

**Dave Jones:** So not that great. Now we'll do exactly the same thing with cling wrap. Here we go. Here goes the cling wrap, 78. And as you can see, it only dropped down to 73, and you can see more detail in there, definitely. So cling wrap does work better.

**Dave Jones:** And for those who want just the thermal image mode, okay, here we go, we'll go with the cling wrap again, and oop, it's a bit, here we go. There we go, it really doesn't change that thermal image at all. It really is very

**Dave Jones:** thermally transparent. That's why I love the cling wrap for this purpose, even though it might have a bit of ESD danger. And back to the ESD bag, here we go, it's coming across, coming across. And you can see that temperature drop a fair bit, and

**Dave Jones:** yeah, the detail's there, but the camera, because we were using the MSX technology before, so the detail is still there, but really, yep, you've got a lot more loss through that anti-static bag.
