---
video_id: uMONqo-Ewug
title: EEVblog #526 - Bank Note Acceptor Followup
url: https://www.youtube.com/watch?v=uMONqo-Ewug
source: youtube-asr
timestamps: {"0": 1, "1": 14, "2": 32, "3": 43, "4": 58, "5": 71, "6": 84, "7": 101, "8": 113, "9": 123, "10": 137, "11": 152, "12": 168, "13": 185, "14": 201, "15": 215, "16": 230, "17": 241, "18": 255, "19": 271, "20": 287, "21": 306, "22": 322, "23": 340, "24": 353, "25": 369, "26": 380, "27": 394, "28": 403, "29": 416, "30": 427, "31": 440, "32": 454, "33": 465, "34": 476, "35": 498, "36": 513, "37": 528, "38": 539, "39": 555, "40": 570}
---

**Dave Jones:** Hi, just a quick followup on this note validator that I did in the last video. If you haven't seen it, this won't make any sense whatsoever. And the link, it will be linked right here. So, just click here and watch it. And uh a couple

**Dave Jones:** of people uh pointed out that um the LEDs used in here, which I um sort of assumed were uh maybe infrared uh leads are actually uh just a bike. It looks like a byolor lead. And sure enough, I've powered the thing up here and of

**Dave Jones:** course I should have checked the uh pins on the back and sure enough they do have three pins. They are a dual die uh lead. So they're at least red. One of the colors is red here. So, I've powered it

**Dave Jones:** up. So, there you go. Even though the um sensor, the photo diode in here is capable of going into the infrared range, as I said, from 1,400 400 nanome up to,00 nanometers. So, it certainly covers that infrared uh spectrum, but

**Dave Jones:** clearly they're just using red leads here for the three of them. And I've powered the thing up, and sure enough, I haven't seen any other uh color yet. So, I can turn the power off there, and we can watch it start up. And of course,

**Dave Jones:** it's probably not going to pass its power on self test because these leads aren't connected uh over to here. So, there's no, you know, feedback from these LEDs to the uh photo diodes in here. And I've put down

**Dave Jones:** some white paper just to maybe try and get some feedback cuz that optical uh path there with the uh light guide in there to feed back that signal. But anyway, we can uh power that up and uh there we go.

**Dave Jones:** No, it doesn't. Ah, there we go. I did get them to turn off. So, there you go. But I haven't been able to get it to actually detect a uh note or anything like that. So, clearly it hasn't um you

**Dave Jones:** know, it probably hasn't pass those S power on tests and things like that. But, um yeah, I might sort of whack that board back onto there so the sensors line up and uh see if we can still see

**Dave Jones:** the colors in there. And also, as many people uh pointed out, the $5 note I had, I didn't see it down there. There it is. Series 2006. So, apparently, they did drastically uh redesign the Note with uh some people have mentioned better

**Dave Jones:** security features in them. So, it's probably no surprise that a 2002 vintage firmware in this uh Note Acceptor I've got here won't accept these $5 bills. Now, just as a first guess, you might think it's a red green by color lead.

**Dave Jones:** And uh well, is it? I've hooked up an external uh coin cell battery via resistor here just to give it some current limiting. There's our red. And let's have a look. We get nothing out of the other one at all. Even though there's 8

**Dave Jones:** milliamps flowing through that other one, I don't see anything whatsoever. And if it was infrared, I thought it should show up on the camera. So maybe turn the lights down a bit. In fact, if we turn the lights down a lot. Bingo.

**Dave Jones:** There you go. I can turn that off and on. We can see that that is obviously on the uh low wavelength side because the camera sensor um or video camera sensors can easily pick up infrared or not easily, they're not very efficient, but

**Dave Jones:** they certainly can. And uh we can see that that is infrared, but I can't see that at all, of course, because my eye isn't uh uh tuned to infrared, but no, it looks like it is. So, it's combined

**Dave Jones:** red and infrared lead. Neat. And I'm assuming that the uh other one on the other board that matches that sensor is going to be uh identical. But uh we do also want to check these ones out here. Well, these are the photo diodes, of

**Dave Jones:** course, but the leads are on the other board. So, we'll uh check those out, power them up, and see if they're the same. They are also a byolor lead. They do have uh three pins on them, and they

**Dave Jones:** look like an identical lead. You can see the uh three pins down inside there. And if you really got this under a microscope, you'd see a bond wire going out there to each leg. And definitely a dual die, but uh is it the same

**Dave Jones:** wavelength? Well, let's find out. or at least close to. I mean, these could be very specialized uh leads, of course, uh specifically uh ordered from the manufacturer for a specific wavelength. We just don't know. And that looks like just the same red to

**Dave Jones:** me. Not a problem at all. And I expect, yeah, it is an identical uh infrared, but as I said, could potentially be slightly different uh specific wavelengths ordered from the manufacturer in terms of uh the infrared. The red looks the same, but

**Dave Jones:** yep, there we go. So, they're almost certainly identical leads. So, um basically four identical dual color red and infrared leads at four specific points on the Note. And now these two outer leads, uh with the purple color, which you I sort of assumed were um

**Dave Jones:** ultraviolet UV leads, they're also showing up on my camera. No problems at all. Look at that. I've got uh 8 milliamps flowing through that sucker and uh we can certainly see it. So, I wasn't aware that uh video camera video

**Dave Jones:** camera sensors could go into the uh UV range. So, that's either uh infrared or this camera can actually see some UV there. Nice. Sure enough, I did a quick check and yes, video cameras can see into the ultraviolet as well. So, uh,

**Dave Jones:** yeah, clearly, of course, you know, based on the, uh, purple color of that lead, you know, really, you know, high-end, uh, purple, but essentially going into the UV, considering that I know for a fact that they use UV

**Dave Jones:** detection in these note validators, then it's obviously a UV lead. So, we have ourselves four dual color uh, infrared and red leads and two ultraviolet ones on the outside edge of the note. when it comes down to it,

**Dave Jones:** there's not a huge amount of security that they're actually doing on this thing. I think they're they're probably just doing it more to just validate that, you know, just to check that the note is the proper currency. So, they're

**Dave Jones:** probably, you know, in the scheme of things, not hugely hard to uh fool. That's why they have the limit uh switches on the side. So, they limit, you know, what currency you can uh actually detect up to, you know, um

**Dave Jones:** it's up to the vendor. This one can only do up to $20. I mean, you know, why would you even bother checking the security on a $1 bill, for example? It's just, you know, it's just not worth it

**Dave Jones:** really in the scheme of things. So, I think it's uh, you know, this is a basic an old really, you know, probably a lowcost model. I'm not entirely sure. I'm just, you know, it's probably not even advanced for its day. So really,

**Dave Jones:** it's, you know, probably one of those ones where, yeah, in say a vending machine, you just, you know, no one's going to bother putting a, you know, a counterfeit bill in to get, you know, a couple of packets of chips or some

**Dave Jones:** chocolate or something like that or an icy cold can of Coke. So, what I might do is try and actually get myself a modern one, especially like an Australian one, for example, that uh can detect our polymer currencies. and and

**Dave Jones:** uh I I think we'll see you know a dramatic uh difference between the very quite simple uh you know sort of rudimentary level technology used in this one and uh and more advanced uh modern ones and also some people wanted

**Dave Jones:** to like you know get me to get the ROM dump and stuff like that and see if we can see the note images and you know the well the data that uh you know knows at what points but you probably have to do

**Dave Jones:** some serious disassembly like like that. it's not going to have their, you know, it's just not going to be obvious when you dump the data. So, I don't think it's worth the effort. And it's interesting that although these four

**Dave Jones:** leads here are the same, essentially the same uh dual color IR and red, the photo diodes are different. These two inner tracks of course angled 45° much larger uh sensor photo diar inside there to sense it whereas these other one these two outer ones are

**Dave Jones:** a smaller photo diode and you know presumably a different type even though essentially operating at the same uh wavelengths. They're obviously these two center lines are doing something subtly different to these two outer ones here. And some people have asked if I could

**Dave Jones:** maybe probe the uh sensor signals, photo diodes and stuff like that as the notes passing through. And yeah, you could do that and possibly correlate uh you know, you'd have to know the note of the well the position of the note. It goes

**Dave Jones:** through pretty quick. You'd have to know the position of the note and correlate that timing with the timing on the sensor. But unfortunately, once it's all assembled in place like this, you can't access those sensor boards. All you've

**Dave Jones:** got is um the outputs of the boards are presumably from you know the op amp but buffers which is probably good enough uh stuff like that. But unfortunately I put the thing back together and um um something something is uh wrong with

**Dave Jones:** this thing. It's just not detecting this at all. Anyway, I don't think you'd learn a huge amount by doing that. These things are pretty darn basic. So yeah, maybe I could have a probe around if I can get it going again, but it's not

**Dave Jones:** going to happen at the moment. Damn. Don't know why.
