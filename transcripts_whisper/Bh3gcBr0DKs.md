---
video_id: Bh3gcBr0DKs
title: How to do Lifecycle Testing
url: https://www.youtube.com/watch?v=Bh3gcBr0DKs
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 29, "2": 53, "3": 69, "4": 89, "5": 109, "6": 125, "7": 145, "8": 165, "9": 181, "10": 201, "11": 217, "12": 237, "13": 253, "14": 269, "15": 281, "16": 297, "17": 313, "18": 329, "19": 349, "20": 361, "21": 373, "22": 389, "23": 409, "24": 429, "25": 445, "26": 461, "27": 481, "28": 501, "29": 517, "30": 537, "31": 557}
---

**Dave Jones:** Mediswab, if you haven't seen them. They're not 100%, what are these, like 70% 70% isopropyl. Good enough for Australia. Cleaned up like a ballpoint, like there's still some gunk being pushed off those traces there, and once again the solder mask is worn off for that trace between the pads, but like, I don't

**Dave Jones:** think that's pretty good. Alright, so that is the 50,000 cycle test, and I betcha when I put this back together I betcha it measures just fine and dandy. I actually expected more wear than this, like I expected like contacts to be worn off the

**Dave Jones:** PCB and you know, like really ground down. The thing with this, right, is that if you want to do this properly, not only do we have to do a contact resistance measurement, you do it like maybe on an unpopulated board, but a production board nonetheless, or

**Dave Jones:** just cut the traces, but measure all of the contacts on there, every single one of them, in all the different ranges like, because there's multi-point contacts in there, it's a multi gang switch, so you've got to measure not only the contact resistance on there, but you would do some materials analysis

**Dave Jones:** as well. Just so I've got the second camera running. Let me start again. Yeah, if you want to do this properly, you really have to measure the contacts the multiple contacts on every single one of these ranges, it's a multi gang switch. So you've got to, as you saw, the multiple things in there, you'd have to

**Dave Jones:** cut the traces so there's nothing in parallel, you'd have to measure the resistance of each one, you'd have to design the jig and really qualify the jig to simulate fingers, and then you'd want to rotate the meter in different orientations, you know, and move it about during the cycle

**Dave Jones:** testing and all that sort of stuff, so it simulates sort of, you know, movement plus a hand and everything else. And not only that, but you'd want to do material analysis as well. So you would measure the thickness of the copper and the thickness of the copper and the gold traces on

**Dave Jones:** the PCB itself. You can get, yeah are they ultrasonic? Yeah, ultrasonic thickness gauges to measure the, however the PCB manufacturers measure the copper thickness, you can actually get quite accurate, you know, down to the micron or several tens of micron level or something of the thickness of the copper.

**Dave Jones:** So you measure them before, including the gold plating on the surface of the switches on the other side, which we can't see. So you would do that first, before the test, and then you'd do it, you know, maybe after 10,000 cycles or something like that, you might take it apart, you'd do the

**Dave Jones:** measurements all again, the thickness measurements all again, including microscope analysis of your contacts as well. And you'd have to do this on multiple meters across, you know, so that A, you can get some repeatability in the data, B, that you can use some as sacrificial to like

**Dave Jones:** cross-section the contacts and things like that so you can look at a site cross-sectional profile of how they're wearing down and, you know, all that sort of stuff. And there's this can take, if you were like, you know, a big ass, you know, if you were NASA

**Dave Jones:** designing this thing, or you were, you know, really serious about doing this sort of stuff, then that's what you would do. You know, you would have material scientists, material engineers, analyze the material and all that sort of jazz and do proper metrology measurements of the

**Dave Jones:** surface contact thickness of the range switch plus the contacts and everything else. So what we're doing here is just a bit how you're doing. You know, it's just for, well, no, like we get some real world data, right? Well, not real world, but we get some decent data.

**Dave Jones:** Anyway, if you wanted to do it properly, you can get, you do that over 10,000, maybe do it over 50, and then 100, you might get multiple stuff along the way, and you don't have to go, because it takes time. Especially if you're measuring the

**Dave Jones:** contact resistance in each one of these positions like this, right? You know, then you'd have to wait for it to settle, you know, move the jig away, you'd probably like, the jig would probably come down, move it, go out, so it didn't put

**Dave Jones:** any force on it, move it, go out, like that, come back in, boop, boop, boop, and then after, then your contact resistance has to settle, and that takes a lot of time. Somebody commented on this the other night on the thread here, it's probably back in the comments on this video,

**Dave Jones:** that, oh, you know, Bell Labs do 3 million cycles, well good luck to you! Go try and do 3 million cycles on this and see how long it takes you. So you might do, say, 10,000 cycles, then, as I said, you get metrology measurements of the

**Dave Jones:** thickness of the contacts and all that and you can calculate how much they're wearing down. And then, you know, if you get some you might be able to get 4 or 5 data points or something, you might see that they're wearing down by 10 microns per 10,000 revolution per

**Dave Jones:** 10,000 cycles or something like that. And then, you can, from that you can, you know, calculate and publish a 2 million cycle lifetime, or 100,000 guaranteed at this resistance or something like that. So yeah, there's a lot of there's a lot of engineering and science that can go behind

**Dave Jones:** testing a rain switch like this. It really is quite remarkable if you want to really do it properly. If you want to go to town, so what we're doing here yeah, a little bit of how you're doing. But still, we get good data

**Dave Jones:** out of it. You know, usable data. We get usable you know, we didn't, we really, I mean, because we're under time pressure here to try and fix this thing before, you know, to get the Kickstarter stuff out and, you know, things like that.

**Dave Jones:** So, you know it's not like we have a month to qualify our test jig, and it's not like we have 20 multimeters to sacrifice either. Actual production meters we've got quite a few here. I've probably got 10 yeah, I've put those screws in, yep.

**Dave Jones:** 10 meters here. But they're all like pre, most are pre-production. We've only got the two which we've, both have now been cycled for 50,000 times. So we've got no more virgin meters left to I guess I could maybe see if UEI have some

**Dave Jones:** but yeah, it's not like we had, you know, months to perfect a jig, because that's what it'd take, you know, it'd take it could easily take a month. Easily, it's only four weeks, geez, to qualify a rig like this. Gee, it'd take months, months and months.

**Dave Jones:** Geez, if you did it in a month you were doing really well. Like if you were really serious about qualifying something like this. There's a lot of art and science that goes into cycle and life cycle testing of components, not only mechanical but

**Dave Jones:** electrical as well. So you know, especially like if you're getting that dust in there and stuff like that, building up crud and whatnot, it's not good. Happens to all you know, you've got your hermetically sealed ones that are designed for 10 million life cycles and stuff like that.

**Dave Jones:** Somebody was arguing last night in this same thread here, that you know, switches should last a million, three million cycles or something. Well I actually posted a link to a digikey, you know, I searched for digikey parts for rotary encoders for example. The contact rotary encoders.

**Dave Jones:** They actually, they're not optical encoders. They're not the optical ones, they're the ones with the wiping contacts. And you go pull, you know, from any of the big manufacturers, C&K, Panasonic, all those sort of ones, CUI, they've all got, if you look at the data sheets, there's a good lot of them.

**Dave Jones:** There are some in the millions, but a good lot of the majority ones, even ones costing like $5 a pop, will only have like 30, 50,000 cycles. Tops, guaranteed, right? Before they're out. Those, you know, the rotary encoders that you spin all the time, which will get

**Dave Jones:** much less use than a multimeter switch, for example. So those, you know, rotary encoders don't, you can get good ones that are designed to last a long time, but there were like 400 different types on digikey that had under 100,000 cycles. You know, people who think that 50,000 is not a lot

**Dave Jones:** for a range switch, you know, are just wrong. Because these are mechanically much different beasts to a simple rotary encoder or a toggle switch or something like that. They're vastly different beasts. Huge multi-gang things over big surface areas with, you know, different pressure

**Dave Jones:** on the switch and the contacts as they spread across, you know, this much, you know, 2 inches of surface area or whatever. It's a big difference. So I think I've heard, well, heard that Breiman specified their meters to 25,000.
