---
video_id: mo4_5vG8bbU
title: EEVblog #1044 - LCD Technology Tutorial
url: https://www.youtube.com/watch?v=mo4_5vG8bbU
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 22, "3": 48, "4": 57, "5": 66, "6": 95, "7": 109, "8": 125, "9": 142, "10": 165, "11": 187, "12": 207, "13": 217, "14": 229, "15": 243, "16": 251, "17": 264, "18": 281, "19": 299, "20": 309, "21": 326, "22": 339, "23": 363, "24": 372, "25": 391, "26": 420, "27": 431, "28": 440, "29": 455, "30": 465, "31": 476, "32": 488, "33": 500, "34": 519, "35": 527, "36": 538, "37": 550, "38": 560, "39": 571, "40": 583, "41": 594, "42": 614, "43": 627, "44": 641, "45": 654, "46": 670, "47": 691, "48": 704, "49": 729, "50": 741, "51": 759, "52": 767, "53": 785, "54": 796, "55": 808, "56": 833, "57": 845, "58": 856, "59": 867, "60": 885, "61": 895, "62": 911, "63": 928, "64": 939, "65": 956, "66": 969, "67": 988, "68": 1001, "69": 1014, "70": 1027, "71": 1038, "72": 1053, "73": 1068, "74": 1083, "75": 1096, "76": 1108, "77": 1119, "78": 1133, "79": 1146, "80": 1161, "81": 1169, "82": 1183, "83": 1194, "84": 1210, "85": 1220, "86": 1232, "87": 1239, "88": 1251, "89": 1264, "90": 1280, "91": 1294, "92": 1305, "93": 1316, "94": 1332, "95": 1349, "96": 1369, "97": 1380, "98": 1390, "99": 1404, "100": 1414, "101": 1428, "102": 1447, "103": 1458, "104": 1479, "105": 1492, "106": 1519, "107": 1531, "108": 1544, "109": 1555, "110": 1566}
---

**Dave Jones:** Hi, this is the first video in a series of videos on LCD displays and more specifically how can you can go about getting or what steps are involved in designing and manufacturing your own custom LCD display.

**Dave Jones:** Hope you enjoy it. Let's take a look at it. Now LCDs come in all shapes and sizes as you can see here. This is just a some of them.

**Dave Jones:** You got your traditional low cost reflective static LCD display which will uh have a play around with in a minute so stick around and you've got your traditional 16 two line by 16 character LCD display module and you've got character based ones and graphical based ones and you've got ones that are on like you know mounted on PCBs as part of modules.

**Dave Jones:** You've got ones that are just a have a flat flex coming out of them. You've got ones that have got drivers on them. You've got ones that are low pin count serial interface ones.

**Dave Jones:** You've got seven segment 14 segment displays like this one we'll have a look at. You've got graphical display ones and all sorts of things. Let's take a closer look.

**Dave Jones:** Now of course you can buy fully custom modules like these which have all the driving circuitry and everything else on and you just talk through pin based interface be it a flat flex like this or just a your regular through hole type stuff and these are fairly inexpensive these days but you can actually do better cost than these which is what this video series is ultimately about is designing and manufacturing

**Dave Jones:** your own low cost custom LCD display. First of all we'll briefly cover how an LCD works and these images mostly images I'm going to show you in here are taken from the very excellent microchip application note AN658.

**Dave Jones:** So I'll link that in down below to check it out to get a bit more detail and you can actually a deep dive down the rabbit hole on how LCDs actually work at the you know the chemistry and physical level, but we'll just keep it very simple here.

**Dave Jones:** Now, let's take a look at the basic LCD components. There's a front polarizer on top, then there's the back plane electrode which is basically the for all intents and purposes like the negative common type terminal and then you've got the LCD fluid itself.

**Dave Jones:** It's actually just a like a pocket of liquid crystals and we'll take a look at electron microscope photo of that in a second. And then you've got the actual segments etched onto a glass layer and they go off via little conductive paths to the actual pins and there the shape of those how you design those determines what shape segments you get on your LCD.

**Dave Jones:** And then you've got a rear polarizer at the back. Now, it's these polarizers can be combined in various ways to get you a positive LCD, which is what we're going to look at now or a negative one, which is basically white segments with a black background or positive will be black segments that you're more familiar with on the white background.

**Dave Jones:** Now, light polarization is key to how LCDs work and I'll give you a crude demonstration with my watch and my polarized sunglasses here. If I put my sunglasses like that, you can see the LCD no problems at all, but if I twist it like that, you'll see it eventually vanish.

**Dave Jones:** There you go. And that's basically how the key concept behind how LCDs work. Now, the LCD we're going to talk about here is what's called a twisted pneumatic or TN type display.

**Dave Jones:** There are different technologies of how the actual liquid crystals themselves work. You don't have to concern yourself too much, but suffice to say that there are different states of these liquid crystals.

**Dave Jones:** So, Uh, most LCDs you're probably going to come across are of the twisted pneumatic type these days. And here's a really cool electron microscope photo of the liquid crystals and how they can line up under an electric field.

**Dave Jones:** And this is the key to how LCDs work. You've got the top and bottom electrodes there with the liquid crystal fluid in there, which is affected by an electric field.

**Dave Jones:** Not a not essentially not a current, it's just an electric field between the positive and negative plates. And that can change the orientation of the liquid crystals themselves. And let's have a look here.

**Dave Jones:** The LCD on the left there, the LCD orientation with no electric field, and you've got the twisted pneumatic liquid crystals in there. In this particular case, when there's no electric field applied, the light will pass through, reflect off the reflector at the bottom, and come straight back out.

**Dave Jones:** So, you effectively the light is not blocked at all. So, you essentially see that white or you know, silver type background, segments not on. But, on the right-hand side here, the when you've applied an electric field, all of the liquid crystals line up like this.

**Dave Jones:** It's a bit counterintuitive. They line up, so you would think that the light would pass back through. But, it's actually the opposite case because of the polarizers in this particular case.

**Dave Jones:** When when they all line up like that, the twisted pneumatic crystals in there aren't will not reorient the light, so the light is actually passes straight through, and then is blocked by the polarizers, and the segment appears to be on or black.

**Dave Jones:** And of course, you can as I said, you can change the polarizers around the configuration to get either white characters on a black background or black segments on a white background.

**Dave Jones:** And also, temperature can play a role in LCDs as well. The poor little liquid crystals actually get pretty lethargic if you drop them if you drop the temperature, and you can see this one here, I've actually had in the freezer for a little bit, and it's can see it a little bit lethargic compared to the other one.

**Dave Jones:** Just takes a little bit of time for those segments to decay, and that can take like, you know, hundreds of milliseconds if it gets cold enough. Once it gets towards 0° or below, can be very significantly affected.

**Dave Jones:** So, LCDs are not current driven, they're actually electric field driven, which essentially makes them zero power, apart from the capacitive nature of them, and you have to switch at a certain frequency to make it visible, and then you have to switch that capacitance.

**Dave Jones:** So, you do get some current through that capacitance. Basic reactant capacitive reactants formula there, but I can actually demonstrate this by not actually having any power at all. I can actually turn on these segments, and it's a bit higgledy-piggledy, but you can see that I'm just just the electric field picked up by my body, and then superimposed across, in this case I've got a ground hooked up to the common pin.

**Dave Jones:** It's going back to mains earth, and you'll see that we're able to get the segments to come on and stay on, and you can see that they do actually decay away like that.

**Dave Jones:** So, there can be a bit of charge build up in there on on the actual display, and then it can take time for them to fade out like that.

**Dave Jones:** Cool, huh? Now, you can actually drive LCDs with a DC voltage, but don't, because that is the incorrect way to do it. You'll ruin your LCD, it will destroy the liquid crystals in there, and it magic smoke will escape, and it won't work anymore.

**Dave Jones:** The only correct way to drive LCDs is with an AC voltage, and I'm actually uh driving it at the moment, as you can see, with a uh basically a DC voltage.

**Dave Jones:** Uh 6 V peak-to-peak uh with a 3 V offset. So, that's basically a 6 V TTL type, you know, digital signal at uh 0.1 Hz. So, it actually flashes off and on.

**Dave Jones:** So, you can technically do that, but don't. What you actually want to do is have a proper AC signal like that, so there's no offset. So, I've just got a 6 V peak-to-peak AC signal.

**Dave Jones:** So, you can see in the middle there, it's going positive, negative, positive, negative. So, the DC the average DC value is zero, and that's what you want when you're driving an LCD.

**Dave Jones:** Uh you want an average DC value of zero. Otherwise, you'll eventually kill it. Now, I'm actually driving this segment at uh 6 V peak-to-peak AC with 100 Hz. This data sheet actually says to uh do 5 V, but it doesn't specify RMS or peak-to-peak.

**Dave Jones:** Now, we can actually uh uh just the amplitude here. I'm going down. If I do it at 5 V, you can see that it starts to affect the contrast, and that's 4 and 1/2.

**Dave Jones:** It's basically almost vanished, and at 4 V, it's goneski. 4 V peak-to-peak for this particular one is not enough. A common drive voltage might be, you know, at least 3 V or something like this.

**Dave Jones:** And this one needs at least 6 V peak-to-peak to be dark. And of course, you can go up, and that might increase the contrast, but don't go too high, otherwise you can get uh ghosting between segments.

**Dave Jones:** Now, I'm actually driving this at 100 Hz at the moment, but you can't just say switch down to 1 Hz, because if I do that, you'll see it's still basically on.

**Dave Jones:** Trust me, I've got that at 1 Hz. Now, if I drive this at uh 0.1 Hz, you can see it's sort of fading out like that. That's not the correct way to do it.

**Dave Jones:** The proper way to actually drive it is to apply your frequency or not. So, that that's 100 Hz and you can drive it, you know, you don't have to drive it any lower than that.

**Dave Jones:** That's just, you know, so it doesn't flicker or anything like that. So, we're driving that at 100 Hz and on off on off on off. That's it. But, you definitely don't want any DC bias.

**Dave Jones:** If you want to go off, you actually just tristate your pin, your driver pin like that. Now, this is your most basic type of LCD. You've basically just got your raw LCD glass and the pins like that.

**Dave Jones:** There's no additional circuitry. Now, these actually come in two types. One is with the through-hole pins like that, which just clamp top and bottom basically like that. Or, you can just specify the exact same LCD but without the pins.

**Dave Jones:** It's exactly the same glass, but if you order them without the pins, then you need to use them with what's called an elastomeric connector, otherwise known as a zebra strip, which is basically Ah, if we can get that off there.

**Dave Jones:** It's a conductive rubber strip like that, which just connects through to the glass. You might be able to see the actual contacts on the bottom of the glass down there.

**Dave Jones:** So, you can either tell the manufacturer to just give you the raw glass like that and no worries, I'll use an elastomeric or zebra strip. Or, you can ask them to provide a strip to your specification, or you can just order it with the through-hole pins attached.

**Dave Jones:** Now, the next step up from your just your basic glass either pin or elastomeric connector, zebra strip connector, is a flat flex connector. Once again, it's exactly the same glass, but you can get them to use a conductive glue that basically sticks the flat flex cable onto there and it goes straight out to pins like this.

**Dave Jones:** You're not actually reducing the number of pins in any way. You're just merely they're the just three different types of interfaces that you can get to a regular LCD glass like that.

**Dave Jones:** And the thing with any of those three interconnect solutions, you've basically just got your LCD glass and you need a separate driver. So, you need all the driver circuitry on the bottom there, either a microcontroller which has the built-in LCD a controller which we'll go into in a future video or whether or not you use a dedicated LCD driver chip or you can budge your own driver circuitry.

**Dave Jones:** We might go into that, but you need some sort of AC drive circuitry for the display cuz these things don't drive themselves. You can't just hook these up to a microcontroller and expect them to work.

**Dave Jones:** They're just a raw glass. They need that AC signal and they're going to be a summer often multiplexed displays. So, they're very complicated to actually drive these things. You need a dedicated driver chip basically.

**Dave Jones:** So, basically the next step up from your raw glass is of course these dedicated modules which have all the driver circuitry and everything built in, but that's quite expensive.

**Dave Jones:** You've got a PCB, you've got you know components and all sorts of stuff on there. You know, it's a like you can get these reasonably cheap, but if you're talking really high volume, you know, it's not that terrific and the height form factor with the PCB and everything else can impact your design.

**Dave Jones:** You can't do like really ultra tiny designs and things like that. So, your next step up from that is to get your driver chip built onto here. Can you see it?

**Dave Jones:** You see it? That's it down in there. Now, this is actually called a chip on glass or COG solution and that's actually the driver chip built into there. So, you can see this is actually hasn't got many pins at all.

**Dave Jones:** This is actually 132 by 32 dot matrix graphic LCD display. So, the LCD display is all multiplexed and everything. It's got a lot of lines on there, a lot of contacts, and they go into the embedded chip which they mount on the glass on there, hence why it's called chip on glass cuz the glass actually extends right out to the edge here, and then they've only got like a

**Dave Jones:** simple serial interface. So, it takes all the headache out of driving this LCD. This one's, you know, nice and thick cuz it has like a huge backlight and things in there, but if you actually take that module out without the backlight, it's pretty thin.

**Dave Jones:** The chip is just on the glass. And another variation of that one, here we go. This one's also got a backlight, but the backlight just pops off like that.

**Dave Jones:** There you go. And that is like just the same really as our glass that we had before, but it's got the driver chip built onto it, the chip on glass.

**Dave Jones:** This one's not a serial interface. This is like a parallel interface one just like like it actually might simulate the interface on your standard 16 by 2 LCD. I think this one is a 16 by 2 LCD dot matrix actually, and it's got your standard interface, but all the driver circuitry is built on there.

**Dave Jones:** Look how thin that is. Awesome. Or if you're not a fan of chip on glass COG, you can actually this one before I lied. This wasn't just the flat flex coming out.

**Dave Jones:** If you look at the there's a little bulge in there. That's actually what's called chip on flex. So, this one actually has the driver chip once again a standard you know, Hitachi LCD driver interface, but the driver chip is built onto the flat flex like that.

**Dave Jones:** And that you may prefer that for some system interconnect reason or something like that rather than a pin base one like this. But just be aware the the result is exactly the same whether or not the driver chip is mounted on a flex like this or as mounted directly on the glass.

**Dave Jones:** When you're getting a custom LCD made like this, you can just specify I want COG, please. I want chip on glass, and they will just extend the glass out for you.

**Dave Jones:** They'll put the chip on there like a standard Hitachi chipset or whatever it is, whichever uh type of interface you specify, and they will give you that for like, I don't know, like 50 cents extra, a dollar extra um per display or something like that in, you know, reasonable like thousand, you know, thousand odd volume or something like that.

**Dave Jones:** So, it's not necessarily a hugely um expensive solution, but it can actually be ultimately cheaper, as we'll go into in a future video, to just get the raw glass and use an external driver chip uh that way.

**Dave Jones:** This And so, these aren't too expensive, but if, you know, you're counting every single cent, then this may be more solution than this plus a driver chip. Now, to confuse the issue even more, LCDs, um all different types, come in three different varieties.

**Dave Jones:** Um in addition to those uh three different solutions we saw for the interconnect, this one has to do with the uh optical uh properties of the LCD glass in the module uh itself.

**Dave Jones:** The first one is reflective, the next one is transflective, and the third one is transmissive. Oh, goodness. Now, this particular one here, for those playing along at home, there's the Digi-Key part number.

**Dave Jones:** This is a reflective LCD display. And what that means is that uh it is not compatible with a backlight. You might be able to edge light the thing or something, but it's basically not compatible with a backlight.

**Dave Jones:** It's got a mirror reflector um embedded on the back in there, and you basically have to shine the light from externally through the glass, and then it reflects back out.

**Dave Jones:** Now, these reflective types, in my opinion, have by far the best contrast and view angle and stuff like that, although that varies with process technology and other things. So, but basically, if you want the ultimate contrast in LCD, you'll want a reflective type.

**Dave Jones:** But, the disadvantage is they're no good in low light because you've got no backlight. Once you're, you know, in like dark conditions, you're screwed. But, the reflective type basically, once you got good external light, it's the holy grail of display quality.

**Dave Jones:** So, your next type is what's called transflective, and that's what this one here is. And it's hard to sort of, you know, tell the difference. One has like a white background and one has this kind of, you know, a silvery type, or it could be, you know, some other type of backing on it.

**Dave Jones:** And transflective tries to get the best of both worlds, tries to get the optical properties of the reflective one while still allowing light to shine through from the back here and actually give you low lighting conditions.

**Dave Jones:** And you can see this one has the backlight. You can see the two PCB mount pins here. This is just the LED on here that allows you to have your backlight like that, and it shines through.

**Dave Jones:** So, you can use it with or without the backlight. But, the disadvantage is transflective isn't quite as good at optical contrast quality as you'll get on a pure reflective like this.

**Dave Jones:** But, it's probably the best overall solution if you want to use your display in all sorts of lighting conditions. You simply choose to turn the backlight off or on, just like, you know, you're used to your multimeter.

**Dave Jones:** Most good multimeters will have a backlight on it. They're using transflective displays. And the third type is what's called transmissive, and I didn't actually have an example here in the lab of that, but it basically here's a graphic about it.

**Dave Jones:** You basically must have the backlight on it Uh, there make it work at all. There is no reflective or semi-reflective uh, back in on it. It's purely relying on the light source coming from the back instead of coming from the front.

**Dave Jones:** And that's great if you're uh, always want a back light and you want it to work in all conditions. It can, but then the back light is always drawing power.

**Dave Jones:** You don't have the option to turn that back light off. It'll basically come unreadable if you remove that light source from the rear. Now, transmissive uh, displays are very uh, common like your TV uh, for example, we use a transmissive uh, display.

**Dave Jones:** It's always on. It requires that back light, but if you want to use them outside, then you've got to have a really bright back light on it uh, continuously to overcome the external ambient uh, sunlight.

**Dave Jones:** And that can be really difficult for outdoor uh, type displays or more to the point very power hungry. But in small displays like this, you won't often find uh, like a small you know, that you'd use in a product like this um, transmissive isn't all that common.

**Dave Jones:** You usually get the uh, transflective type or the fully reflective type. So, your standard reflective uh, display like this one is your cheapest and your simplest because it doesn't need a back light.

**Dave Jones:** It's going to be the thinnest, whereas your uh, transmissive one actually you know, you're going to have to need the back light on the back of it cuz you wouldn't want to use a transmissive one without the back light.

**Dave Jones:** If you know you're not going to use the back light and you're not even going to integrate it into your product, it'll still work, but yeah, not as good as a reflective one.

**Dave Jones:** So, you've got to decide up front whether your product is going to have back lighting or not. But uh, there we go. I can get I can generate numbers.

**Dave Jones:** Beautiful. Anyway, we're going to drive in them uh, in a future episode, but there are uh, basically two different uh, types of LCD. This one that we've got here is a static type.

**Dave Jones:** If you take a look at the data sheet, it's what's called a uh, static or a non multiplexed LCD display. So, what that means is that it's got one common pin down here, and then a pin for each particular segment on the display here.

**Dave Jones:** And basically, there's no need to multiplex anything. You're still AC driving the pin, but you don't actually need to multiplex different segments. And this is common for like a display like this, which doesn't have many segments on it.

**Dave Jones:** In this case, it's just a seven-segment display like that. And you know, we have X number of pins. This one actually has two pins per segment. So, you don't need that many pins.

**Dave Jones:** And you know, maybe like a 3 1/2 digit multimeter, you know, one of those real old cheapo ones, they might be static as well cuz you can get away with like 40 pins or whatever.

**Dave Jones:** And you can drive those statically. There's no need to multiplex. But once you get into a more complex LCD, which is what we're going to actually design in this series of videos and actually get manufactured, you'll see that in the next video, is that you need to multiplex the pins.

**Dave Jones:** You need to have more than one common pin on here, and then you need to multiplex the segments. Otherwise, you'd end up with hundreds and hundreds of pins. And you obviously don't want that because it's logistically very difficult to drive.

**Dave Jones:** You need a multi-hundred pin LCD driver chip and everything like that. And of course, it goes without saying that your graphical ones like these or you you know, even your text-based graphical dot matrix ones, you This is an eight character by two line, and this one here is a a 16 character by two line LCD that you're familiar with.

**Dave Jones:** They're actually dot matrix, and because there's just so many dots on there, these ones are by default, they have to be multiplexed. There's just no other way to do that with the sheer number of dots.

**Dave Jones:** But if you've got one like this one, which is an 8-digit 14-segment, look at this puppy. Um it's one of these uh starburst displays. I love these uh classic old school school starburst, right?

**Dave Jones:** This has, if you count up the number of segments on there, it's 8 by 14 segments. Clearly, we don't have that number of uh pins. So, what this one is got is it's actually got four commons.

**Dave Jones:** Uh what's called four common pins instead of this one here which just had the one common pin. And then you have to actually multiplex. If you want to turn, like in theory, your product could turn all these segments on at once.

**Dave Jones:** And if you want to do that, of course, then you have no choice but to multiplex the display using those four different uh commons just uh to like reduce the number of uh driver pins that you've got on there.

**Dave Jones:** Oh, it's sorry. I love these. I just love them. Starburst. Brilliant old school stuff. Um if you don't know about the starburst, it's just a uh a way to uh allow you to display alphanumeric characters in a standard uh like seven-segment type uh format, but it uses uh 14.

**Dave Jones:** And you can also get 16 uh segment ones as well. But, they're very cool. And you'll find that most LCD uh driver chips built into microcontrollers will typically have a maximum of four commons.

**Dave Jones:** But, we'll go into this in the uh design video in the next one. So, there you go. That's just an example of a multi-common multiplex display. But, the problem with your multiple common displays like this is that they require, the more commons you have, the uh more bias voltages that you actually require to uh bias uh the various commons.

**Dave Jones:** And And that's probably a video in its own right. But, suffice it to say, they're a bit more complicated to drive uh than your just your general um static display or non-multiplex display like this one, which has basically one common.

**Dave Jones:** So, you really do need a dedicated uh driver chip that handles the multiple uh bias voltage levels uh for these multi-common displays. So, there you go. That's a look at uh basically the three different interconnect uh type solutions for uh custom LCDs and also the three different uh type optical properties of LCDs like this and you can get them all in any weird and wonderful combination that you

**Dave Jones:** like. So, in the next video, we're actually going to look at actually designing your own custom LCD display and ultimately in future videos actually getting that manufactured and then uh driving that for our custom product.

**Dave Jones:** So, stay tuned for that one. So, I hope you enjoyed that and if you did, please give it a big thumbs up cuz that always helps a lot and as always discuss down below in the comments or on the EVblog forum.

**Dave Jones:** And don't forget to subscribe and you know, do that bell icon so you get email notified and all that stuff YouTube has to you know, YouTubers say. And yes, thank you to my uh patrons over on patreon.com.

**Dave Jones:** I've had a Patreon page for ages where people uh support me directly uh because of the adpocalypse these days. I'm I'm not losing a huge amount of money on videos, but I'm getting more and more videos demonetized.

**Dave Jones:** So, a lot of YouTubers like myself are moving over to uh direct sponsorship uh from the viewers on places like Patreon. Really appreciate it. Catch you next time.
