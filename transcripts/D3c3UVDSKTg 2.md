---
video_id: D3c3UVDSKTg
title: EEVblog 1664 - REPAIR with Junk Bin Parts! Keithley 2302
url: https://www.youtube.com/watch?v=D3c3UVDSKTg
source: youtube-asr
timestamps: {"0": 0, "1": 33, "2": 64, "3": 78, "4": 100, "5": 130, "6": 147, "7": 169, "8": 188, "9": 219, "10": 241, "11": 257, "12": 273, "13": 307, "14": 348, "15": 379, "16": 410, "17": 437, "18": 455, "19": 493, "20": 515, "21": 538, "22": 567, "23": 590, "24": 624, "25": 648, "26": 680, "27": 709, "28": 733, "29": 753, "30": 780, "31": 809, "32": 836, "33": 869, "34": 891, "35": 913, "36": 947, "37": 981, "38": 1011, "39": 1039, "40": 1064, "41": 1093, "42": 1114, "43": 1147, "44": 1170, "45": 1200, "46": 1232, "47": 1259, "48": 1297, "49": 1321, "50": 1339, "51": 1352, "52": 1368, "53": 1387, "54": 1413, "55": 1442, "56": 1455, "57": 1475, "58": 1505, "59": 1535, "60": 1563, "61": 1587}
---

**Dave Jones:** Hi, in a recent repair video, I got out a bit of kit that I haven't used for a long time, this Keithley 2302 battery simulator, and I was going to use it as part of that repair video, but um I went to use it, and well, the fan turns on, but So, it has failed. Now, if you haven't seen inside this thing, it's a very cool bit of kit. I'll link in the video. It's actually from 7 years ago. I did a teardown of this. So, I'll link that in

**Dave Jones:** if you haven't seen it, really interesting stuff. But, I looked at that video again, I noticed that yeah, it did work back then, but the vacuum fluorescent display in it was quite dim and hard to read. So, yeah, in that time it's gone skee. And sorry, I can't remember who it was, but I think somebody commented um that I'm paraphrasing a bit, but basically, if you don't take out your test equipment periodically and use them, they just die of loneliness. And well, I think that's what's happened here. So, yeah, let's

**Dave Jones:** take a look. There's two screws here, take those out, and uh I think it just slides. Does it just slide out, or has it got one screw on the bottom? Oh, yeah, it's got multiple screws on the bottom. Doh! All right, we have the screws out.

**Dave Jones:** It comes out nice and smooth. Look at that. There you go, glorious 4K resolution for those playing along at home. One massive board, but anyway, I won't go into it. We've looked at the teardown extensively before, but I'll just look look. Not sure if I did in 4K last time, but there you go, for those playing along at home.

**Dave Jones:** But, anyway, we have a separate display board here, but it's actually two boards. Looks like there's the actual display board, and then the vacuum fluorescent display board. Aha. That board also controls the front panel membrane keypad as well, just going on there but old school PLCC soldered down so let's get that out luckily there's a nice connector there which of course doesn't come out unless you remove this main board.

**Dave Jones:** But what? Are you kidding me? Hang on. How can I bend it? Don't want to break the blood seriously? Come on. Little cut out in there would have been nice just saying PCB designer. Now you see that's what happens when the PCB designer doesn't talk to like the housing person.

**Dave Jones:** They're they're not the same or at the design review meeting they just like didn't think about it and when somebody was you know they build up the first prototypes nobody complained and fed that back to the PCB designer for the next rev. Oh yeah, can you just add a cut out there please? But of course I'm just having a winge because you can't actually just do two at the same time. There you go.

**Dave Jones:** You can actually get this out so the little embedded threads in there are nice. And then that just pops out like that. Beautiful. And dual board construction there but you can see that in the teardown video and I like the big clunking switch which goes right to the back, does it? Yeah, it looks like it.

**Dave Jones:** Big shaft. I tell you I love a big plastic long plastic shaft like that. That's what she said. USA USA USA look at that. Keith Lee is that copyright 1999 there? So it's party like it's 1999. So oh I wonder what the extra connector there was for and you know some extra unpopulated stuff. I don't know. Was that like a maybe like some sort of serial interface that goes off via this like RJ11 thing?

**Dave Jones:** Without getting it out we can already see a part number in there. Oh is it going to be that easy? Do I just have to buy a new vacuum fluorescent board? These are usually pretty standard as you saw Um was a like a 16 by 2 dot matrix jobby. So, you know, it should be pretty standard. Metal threaded inserts.

**Dave Jones:** Oh, Bobby dazzler. Looks like I've got some extra standoffs on the bottom there. But yeah, that's just going to flip out and there's the culprit. There you go. Looks like it's just a standard what a 16 pin inline interface there.

**Dave Jones:** Should be able to get a replacement for that even vacuum fluorescent or LCD. But of course bloody Murphy had to be soldered in, didn't it? Just my luck. All right, I got to actually do some hard work here.

**Dave Jones:** Uh my Rhino Tools Tools ZD-985 is kind of starting to suck and uh not in a good way. It's just all everything's loosey-goosey on it and uh it's it's never been it's been okay, but I think I'm in the market for a new sucker.

**Dave Jones:** So, there you have it. VFM 1602 SDAR8 made in China and that's a it's a Newhaven display jobby. There you go. Newhaven are one of the bigger LCD like suppliers. They were kind of like they'd be one of my handful of go-to ones that you know, if I'm looking for like displays and stuff. Yeah, they'd be it. But of course it's vacuum fluorescent displays. So, of course these things are famously yeah, just all the the vacuum escapes from it and once that happens yeah, she's no good anymore. So, who

**Dave Jones:** knows what's wrong with that thing, but it's almost certainly I would be 99.9% sure it's the vacuum fluorescent display that's failed rather than any electronics on there or any electronics on this driving board here. In fact, I wouldn't even bother measuring the signals going to this. I'd just order a new screen like this. But, yeah, but maybe we can just have a little poke see see if the signals are there. But, I'm pretty darn sure they are. You can see here what looks like a serial interface.

**Dave Jones:** They've got this silk screened on here, but they've also got the traces going to the other pins over here. So, I think this might be a combo series parallel. I'll actually get the data sheet for this and I'll whack it up and I think we'll find that. So, I don't know if it's operating in serial mode or parallel mode. So, let's just probe pin three there, the serial pin. Pin one's ground, pin three is serial. And just see if we get anything serial. If not, we move over to the parallel. Just a

**Dave Jones:** little pro tip here. When you're probing stuff like this, you don't want to like be accidentally shorting out pins. And if you've got, you know, your a big crocodile clip on your scope probe here, then that can be a problem. So, what I want to do is just find a more convenient ground point and sure enough the chassis there is connected. So, we can just connect our scope probe to the chassis ground like that. No worries.

**Dave Jones:** And because it's all mains earth reference scopes mains earth reference and so is this chassis. So, not a problem. Not the best signal integrity, but for just probing to see if the signal's there, you don't really care about signal integrity. All right. So, we're 1 V per division here and we're picking up some 50 Hz AC mains there.

**Dave Jones:** Triggered just above that. So, switch the power on. I'm probing pin three here. So, we're getting diddly-squat. So, either the processor or whatever else inside here has failed or it's using the parallel because on a parallel interface that pin three is not used for anything, I believe. So, let's go to a random one over here. Bingo. Hello. And we'll single-shot capture that. So, yeah, excellent. Data's there. And when I talk about signal integrity, by the way, look at that. What That's pretty good. I mean, the really piss-poor probing that

**Dave Jones:** we've got here, right? And this big antenna earth lead, we've got the big wire coming out here. It's picking up 50 hertz like there's no tomorrow. Um, it doesn't matter because we're not measuring When I talk about signal integrity, um, I'm talking about how the signal looks like. Is there any overshoot? Is there any undershoot? In this particular case, um, there's nothing. So, it's actually pretty good.

**Dave Jones:** So, yeah. So, you don't really have to worry about When you're just looking at signals like this, don't have to worry about that you've got, you know, in this particular case, like I've just I'm not even trying to probe it with this cuz you can accidentally short out pins with your easy hook, uh, on there. So, you just get like an extended, um, bit of wire coming out like that and just go to the chassis here with your ground and Bob's your uncle. No workers. So, the

**Dave Jones:** answer is that looks fine. It's continually updating the, uh, screen there. You jump to some other pins there. Yep. Yep. So, it's obviously a parallel interface like that. No problems whatsoever. So, yeah. Data's getting to there. That's That's some higher frequency, uh, stuff there. So, we can single-shot capture that and we can really go in on that. So, um, yeah, not not a problem. So, yes, this board, uh, still works. So, it's exactly what I originally, uh, suspected. But, of course, you know, it takes a couple of

**Dave Jones:** seconds to, you know, like a minute to hook your scope up and actually, uh, test this. So, trust and verify, but, you know, I was 99% sure it was the vac- failed vacuum fluorescent display. So, let's go have a squeeze, see if we can still get this or some sort of replacement. So, we type that number into the Google's, there's actually no hits, but it actually shows up as images. We've got a Newhaven display.

**Dave Jones:** Sure enough, there's more images, but no, there's no like text results for this link results at all. So, this not quite the same number, but if you jump over to it, and this is Octopart, which is an aggregator of different suppliers here, you can see that the 16 is stocked at onlinecomponents.com. I've used them before for parts for my micro current and other projects. Mouser.com, Mouser Electronics, and Zero at Hawk. So, yeah, if we jump over to Mouser over here, sure enough, vacuum fluorescent display VFD 2 by 16, and we've got a

**Dave Jones:** data sheet, but it's not quite the same number. So, I don't know how it correlated that number there, because if you search this page for the actual um thing, like there's no other information, like there's an alternate part number down here, but that's not it. So, I guess Google determined that that's the nearest hit, and I don't know. But anyway, we have a data sheet.

**Dave Jones:** If you search the Newhaven display website, you don't get anything for that part number at all. But granted, this is 25 years old. So, yeah, it could be a well discontinued model. So, this one initial release is 2011. So, this is way after. So, yeah, maybe this is just the new model for it, but yeah, without any identical like you know, part references, or with a data sheet for the original one, I can't tell if it's going to be exactly the same. But that looks like a 84 by 44,

**Dave Jones:** that looks correct. Yeah. 84 by 44. Yep, holes are in the right location. It's important to get your holes in the right location. And sure enough, it is parallel and serial interface, exactly the same pinout, VSS, which is ground on pin one, pin two is VDD, pin three is that serial input output, which we which we didn't get a signal on, and up here, because we know we're operating in parallel mode, yeah, it's NC, not connected, or it could be slash reset.

**Dave Jones:** In this case, it's not connected. So, if you see that 50 hertz main sound like we did on the scope there, then you know that the signal is basically open, and it's picking up just the 50 hertz from the air because it's a high impedance input on the scope. Whereas, if you once you if you connect that to a digital signal, even if that digital signal is low, that's a low impedance drive signal. It's a low impedance signal, so that 50 hertz is is going to be vanished

**Dave Jones:** because you've got a low impedance drive there. So, we knew that that pin was open. So, it is actually not connected. There you go, it's got different jumper settings, which you can set parallel M68, default parallel I80. That's an Intel 8080 interface. So, which one the Keithley's actually implementing? I don't actually know.

**Dave Jones:** Might have to look through my original teardown video to see what processor it was using, maybe. Hmm. Anyway, the M68, that would be the 6800 processor. So, you know, Intel and Motorola competition there for their interface settings. So, so yeah, without knowing anything about this original jobbie, you have to assume that this is like the closest we're going to get, I guess.

**Dave Jones:** Like, you know, I could go in there, you could hook your logic analyzer up, and you could get the signals to know exactly which interface it is, but you know, that's like a lot of time and effort. It's easier just to cross your fingers, hope to Murphy that your LCD replacement that you're going to get is going to fit. Now, we can probably get an LCD replacement for that instead of with the same interface and the same protocol and everything as a vacuum fluorescent, but given that we don't have any information

**Dave Jones:** on this original one, and I don't really want to spend the time going in and double-checking the signals, I'm better off just ordering this from Mouser. What is it 66 Aussie bucks? You know, it's a bit pricey, but hey, it gets a very expensive bit of kit up and running with probably the best chance that we're going to have without putting a lot of time and effort into this. Time and effort cost money. As interesting as it might be to go down that rabbit hole.

**Dave Jones:** Now, I'm just going to have a look at the vacuum fluorescent displays on here. Seven segment displays, dot matrix displays, or VFD modules. That's the that that's the one the 162 SD-A-R-8. Yeah, it's current one. 67 that'll be Yankee bucks, so looks like I'm getting it pretty cheap, actually. Oh, there's an SD and there's an MD. One is a 5x8 and one is a 5x7. Yeah, I definitely count eight there and this one is physically different to this one over here. So, this is all my like this is as

**Dave Jones:** I said without any data, this is the best bet we've got. And we'll whack this into Fine Chips as well just to see. Digi-Key have zero stock. Minimum quantity 1,000. No, thanks. Verical $41. Mouser, yeah, it looks like Mouser is the best bet. Online Components are 31 bucks, but that's a thousand off price.

**Dave Jones:** So, but they've only got 16 in stock. So, yeah, I do have an account with Online so we can actually see. Oh, no, they want 59 bucks. There you go, each. So, it looks like Mouser is the go. Now, I asked Rock and it did come up with a potentially alternative part number here, which is KH6162 SD01.

**Dave Jones:** So, do 151 bucks. And sure enough, it pulls up that Newhaven one there as well. So, that's interesting uh display tech um ooh, okay. Carry Digikey Australia, okay. So, there is one and that looks like it's sort of like Alibaba AliExpress kind of thing. Okay, it's available from uh kinghigh.com um yeah, made-in-china.com ooh, and eBay as well. Yeah, no, that doesn't look like uh it's compatible, does it? Nope.

**Dave Jones:** Um that one looks like it might be. Anyway, like got 314 in stock at uh 27. Is that Aussie bucks or Yankee bucks? It's the Aussie flag up there. So, that is a potential cheaper LCD replacement, perhaps. No, but see like that's going to have like pin three as the operating voltage for the LCD and this is doesn't have like the serial interface compatibility that the other one has that the original has. So, it yeah, no, look, I think you you could probably get almost certainly

**Dave Jones:** I don't know get an LCD working um here, but yeah, as I said like the time and effort required to sort of like make sure you got the right one um is just it's worth a lot more than paying the 60 bucks just to get the replacement and you know, 80% confident it's going to work kind of thing. If I hold up that board there and you can check out that it it's pretty identical, isn't it? The layout of all the resistors and everything is absolutely all the jumper

**Dave Jones:** links and and the boost converter circuit there. Like it's it is identical. So, yeah, confidence is high. I repeat, confidence is high. Confidence is high. I repeat, confidence is high. And the part number at the end the 162 SD A8 is exactly the same. So, it looks like they just changed it from the VFM that's here to that new part number, but they haven't changed layout like at all.

**Dave Jones:** So, yeah, we got pretty lucky there that Newhaven display. And that's one of the advantages of going with one of these major manufacturers is they'll usually keep uh compatibility with legacy products like this. It would have been nice to like have on the data sheet or on the website that yeah, this is compatible with the old one. I'm presuming it is still fully compatible cuz yeah, it looks the same, but I think we found a winner and I can get that for 60 Aussie bucks with free FedEx

**Dave Jones:** delivery. Beauty. All right, I thought I'd have a look in my LCD tubs where I just keep a whole bunch of uh displays, both um actually quite a few vacuum fluorescents and also uh LCDs as well. I didn't have any direct 16 by 2 vacuum fluorescents like uh this Newhaven one, but uh and of course, you know, I got a bunch of these, but uh that is a totally different physical form factor um in terms of the pinout, but I did find this LCD here which is

**Dave Jones:** basically absolutely identical footprint. They were actually uh similar part numbers. This is JHD162D and this is also a 162 uh SD. So, they're not too far off, but yeah, you'd have to go into the uh minutia of the data sheet, I'm afraid.

**Dave Jones:** But you have to be careful with this. Can you spot the difference between these two boards? Uh yeah, leave it in the comments down below before we continue. Can you spot it? Can you spot it? I'll put you out of your misery if you couldn't. Um yeah, this one has 16 pins, this one has 14 and you notice how the pin number here goes 15, 16 and then one. So, one to 14 actually matches these ones here like this. It physically matches like that, but they've got the two extra pins over

**Dave Jones:** here and that goes off to the uh well, usually yeah, to the LED backlight. There it is down in there. Yeah, so you've got to be careful with that. We've got to actually shift it over by two and start it from there, not from there. So, we'll do that and we shouldn't have to solder it in. Uh, we should just be able to physically hold that in place, probably.

**Dave Jones:** Put a bit of pressure on it, like angular pressure, and those pins should hold in there like that. So, let's start that up and see if we get it and see if we get lucky. No, we don't. It's a bit of a bummer. But you remember how we said that pin three there wasn't going to anywhere and sure enough, I've had a squeeze and there seems to be no trace going off pin three there. So, that was uh floating. So, you can actually measure that, measure that

**Dave Jones:** compared to ground and sure enough, it's not going off floating and you know, like you do any of the other pins and they're obviously connected to some sort of like semiconductor. So, pin three is floating. And what's pin three on this? Well, that's the LCD contrast voltage. So, that you know, leaving that floating, uh that might uh the display might be working, but it may not have the correct uh contrast voltage on there. Hmm. Okay, so what I've done is just uh grounded pin three there. Um and we'll see if

**Dave Jones:** that makes a difference, shall we? All right, let's put pressure on that again and let's power that up. Whoa, hello. We have Uh, we have a flashing cursor. Oh, look. Look. Win- winner, winner, chicken dinner. Look at that. Works a treat. Oh, I knew that grounding it would uh usually that's, you know, the like the right contrast voltage. I mean, you can put a pot on there, but uh yeah.

**Dave Jones:** That's that's fantastic. We have a winner from the junk bin. Oh. Whoop. Well, what's that? That's what happens when you don't solder it on. Oops. So, I soldered that back on and ta-da, it does take a bit to boot up, but flashing cursor, flashing cursor, and I'm actually happy with that. That's actually a really nice display. And look, it's even still got the protective film on it. And I just happen to have uh three of these displays in my literal display uh junk bin that labeled displays. I'm very

**Dave Jones:** happy with that. Um you know, I kind of like a vacuum fluorescent as much as anyone, but you know, like that gets me out of trouble, no problems whatsoever. And I could like um power on the backlight. I could just solder in the backlight if I really wanted a backlit uh version as well, but I I really like that. That's just nice. So, I'm I'm just going to stick with that. I'm going to call that a win from the junk bin.

**Dave Jones:** Fantastic. So, let that be a lesson to you. It pays to keep a junk bin full of uh parts like this. So, it's not often that I get a uh win like that, but uh Murphy must be sleeping today. I'll take it. Whoa, hang on. I put it back together and um what's uh what's going on?

**Dave Jones:** And did I miss that it had like a That looks like a dark like a filter or something on there. Ah, yeah, I didn't even think about that. Oops. Yeah, that has like a really Is that a polarizing filter?

**Dave Jones:** Or is that just really dark? That wouldn't that be Wouldn't that be Wouldn't that be just my luck that it has the polarizing filter opposite to the um polarizing filter inside the LCD here? That'd be hilarious. So, check it out. It works just fine.

**Dave Jones:** And if I put the screen over it, yeah, it filters it out. What if I turn it 90°? No, still can't see it. Um so, yeah, I uh what? That's annoying, isn't it? Do I need the vacuum fluorescent like if I had a backlight to it?

**Dave Jones:** Is that going to be enough? I don't know because these are black. So, um yeah. Damn, I think I've come a gutser at the last minute by the bloody filter on the front. Are you kidding me? And that's I can't just remove that. Well, I can cut it out.

**Dave Jones:** I can cut it out, but that is integral with the um with the decal on the front. Are you kidding me? After that win, that solid epic win, I'm going to have to have an actual radiative display I like an actual emitting display like a like the vacuum fluorescent. I might have to order the vacuum fluorescent cuz I don't really want to butcher the front like that, but oh man.

**Dave Jones:** Unbelievable. What are the odds? Yeah, yeah, that's the EV blogging a nutshell. Bloody Murphy. Unbelievable. Come on, but at least give me credit for that win. All right, I turned the backlight on. There you go. Just added a couple of jumper links down the bottom there.

**Dave Jones:** There you go. That's a Bobby dazzler, isn't it? Oh, look. Oh, kind of sort of works. Kind of sort of. Oh my goodness, I'm going to take that for a win for now um until I can get maybe a vacuum fluorescent display replacement. Oh, but jeez, unbelievable. All right, watch this bad boy in action.

**Dave Jones:** Look at that. Come on. You can do it. Flashy flash. And tada. Excellent. And now we can yeah, we can go display type one and of course it's all going to work cuz the only issue was the actual display. Yeah, that's not a great display because of that filter on there, but it actually up it it does work. So, with the backlight, but I might order the vacuum fluorescent display anyway just to give it its original look and feel, but yeah, there you go. I hope you

**Dave Jones:** like that thing. Can you see that on the screen? I think you can. It's well, it's actually kind of like more readable than it actually was originally with the faded vacuum fluorescent display. So, that's definitely a winner winner chicken dinner, but I had to earn my dinner this time by raiding my junk bin to find the exact replacement and then to be thwarted by the first jumper link required which was for the LCD contrast voltage. So, we had to pull that pin down to zero to actually get that thing

**Dave Jones:** working and then foiled by the the actual display filter thing on it which is completely black. Couldn't see a damn thing. And well, the backlight works, but yeah, yeah, I'll get the new vacuum fluorescent display and make it look all better, but I won't do a follow-up video on that, but you know, follow me on X on the Twitters and I'll post a photo of that when that comes in and I replace that, but I got to go and desolder the whole bloody thing again.

**Dave Jones:** Anyway, so anyway, that was a rather interesting repair video. I hope you agree. If you liked it, please give it a big thumbs up and as always discuss it down below and check out the EV blog.store because you can get the new BM2257 with the Well, look at that orange backlight on it. Bobby Dazzler. BM2257 are available over on evblog.store.

**Dave Jones:** Catch you next time.
