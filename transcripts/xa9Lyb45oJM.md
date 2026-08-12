---
video_id: xa9Lyb45oJM
title: EEVblog #258 - PSU Housing Design - Part 11
url: https://www.youtube.com/watch?v=xa9Lyb45oJM
source: youtube-asr
timestamps: {"0": 0, "1": 22, "2": 29, "3": 48, "4": 62, "5": 74, "6": 84, "7": 93, "8": 107, "9": 124, "10": 136, "11": 155, "12": 170, "13": 187, "14": 197, "15": 210, "16": 220, "17": 235, "18": 249, "19": 266, "20": 278, "21": 283, "22": 302, "23": 319, "24": 336, "25": 350, "26": 369, "27": 386, "28": 401, "29": 412, "30": 427, "31": 439, "32": 453, "33": 461, "34": 475, "35": 488, "36": 498, "37": 509, "38": 520, "39": 530, "40": 551, "41": 563, "42": 583, "43": 591, "44": 603, "45": 614, "46": 629, "47": 638, "48": 658, "49": 672, "50": 689, "51": 705, "52": 725, "53": 735, "54": 753, "55": 769, "56": 791, "57": 818, "58": 838, "59": 860, "60": 868, "61": 878}
---

**Dave Jones:** Hi, it's time for another installment in the power supply series and yes, it's another revision schematic. I've got some changes, not surprising because when you work on these projects long enough, one thing leads to another, you start thinking things and you start refining it and you get caught in that trap of well, maybe I can reduce the cost or maybe that idea I had at the start

**Dave Jones:** wasn't that great or I've changed my mind. I think this is more important now and well, one thing leads to another and you have a whole raft of changes.

**Dave Jones:** So, not only do I have rev C schematic here, I'll go through it in detail and all the changes to it, but I'll talk about the system engineering aspects to it as well, as well as revealing, I guess, the big secret to what my original intention for this lab power supply is.

**Dave Jones:** Let's go. Now, when it comes to lab power supplies like these, what do they all have in common? Well, they're all big, they sit on your bench like this and they have one of these, a power cord.

**Dave Jones:** They're tied to wherever they're tied to your bench just like a bench multimeter, for example, but I do a a lot of designs I'm working on, working on different part of the bench.

**Dave Jones:** I don't want to have to move my power supply somewhere else. I might be It might be something that's a portable. I might be working on the floor or could be working anywhere on a different bench on the other side of lab, whatever.

**Dave Jones:** So, I had no intention of just doing yet another bench lab power supply like this. They're a dime a dozen. You can buy them for next to nix on eBay.

**Dave Jones:** They're so cheap and so readily available. So, I thought I'd go for something that it was a bit more niche, was smaller and met a different requirement. Now, please excuse the crudity of the model.

**Dave Jones:** It's by no means finished. I haven't done the front panel. It's all just sort of hanging there. I haven't put in put the uh, the binding post on the front, but this is the case that I originally intended to house my power supply in, and I looks like I'm still going to do that.

**Dave Jones:** And what's the There's two cool things about this. One, it's very small. Look, it's only the size of my hand. It's tiny. So, it's very portable. You can take it to wherever you need the job.

**Dave Jones:** And what's the next big thing about it? I'm glad you asked. Well, tada! My original intention was to have it battery-powered. Lithium-ion batteries. I was going to have three 18650 lithium-ion batteries inside this thing.

**Dave Jones:** It's a rechargeable bench power supply. Is it a world first? Uh, I doubt it, but I don't know offhand of any other, uh, rechargeable just general-purpose lab power supply on the market.

**Dave Jones:** So, I thought it'd be quite unique to actually have a little battery-powered power supply like this, and hence why it people have always been asking from the first video why it's not 30 volts at 3 amps and 100 watts and all this sort of stuff.

**Dave Jones:** This is why. I wanted to be small, compact, battery-powered. For a good majority of the designs I work on these days, they're only drawing a watt or two, you know, tops.

**Dave Jones:** I don't need a 30-volt 3-amp power supply. And if I do, I've already got a bunch of those sitting on my bench. I just wanted this thing small, portable, battery-powered, rechargeable.

**Dave Jones:** Beautiful. So, the need to have this thing battery-powered from a couple of lithium-ion batteries in a small case is what drove most of the design decisions from the start.

**Dave Jones:** I started out by thinking, "Right, I want a battery-powered power supply." I went around, I want it small, house a couple of 18650 batteries, a small LCD, some, uh, you know, a couple of knobs, and a couple of switches, and that's about it.

**Dave Jones:** So, I went around searching for a case for that, and this one's pretty ideal, and I'll show you why in a minute. But, this also leads into uh why I've changed the design in uh rev C now, my third uh variation of this design.

**Dave Jones:** I've actually changed uh a few things. And the look and feel is going to be very similar, but uh the stuff like the heat sink on the back and the accessibility of the connectors and stuff like that really uh drove this uh rev C design decisions.

**Dave Jones:** Now, as for the case itself, it's a um Hammond {slash} well, it's actually a Rytek, but I think a Hammond actually uh redo these now, and it's an RM 2015M.

**Dave Jones:** And the good thing a couple of good things about it that I like, A, it's pretty low cost. It's only It's less than $4 uh in volume for this size.

**Dave Jones:** And uh the uh three things, actually. Low cost, uh and it has standard uh mounting holes on the top and bottom side of the case like this, so you can mount boards on both the top and the bottom of it.

**Dave Jones:** And I thought that was really good because I chose a heat sink, which is kind of low profile like that. And by the time you get that second one on, you've actually got some height there available to maybe put a couple of extra switches or something else along the top.

**Dave Jones:** And of course, my original intention was actually um to have these batteries actually uh mounted on a second board on the top here with its own battery charger. Hence why in my previous designs, I haven't included um any battery charging circuitry on the board.

**Dave Jones:** I just had this uh header connector over here, which I was going to connect up to the top uh battery board, which houses those batteries. But, I've uh changed my uh mind on that, so we'll go into that um at a later stage.

**Dave Jones:** So, you can mount dual PCBs on there, and by the way, they're exactly the same uh footprint. So, um one of the neat things is if this board mounts on here, there's my four mounting holes on there, not only can I mount it on Well, let's call this the bottom of the uh case.

**Dave Jones:** Yeah, it essentially is. Um but, I can actually flip it over like this and mount it on the top upside down like so. So, that the board, the main board's actually on the top and the knobs are on the top of the case.

**Dave Jones:** Why is that important? Well, I'm glad you asked because if you've got it down like this, it's a very compact case. I haven't got much room at all. And I was going The LCD takes up all this space over here cuz it's pretty big.

**Dave Jones:** I wanted to be able to see the LCD from the other side of the room or, you know, from a reasonable distance. So, I've got my uh binding posts up the top here, and that's a bit That's, you know, it's not that great.

**Dave Jones:** These knobs are on the bottom, and you've got to try and adjust the knob with your wires coming out from your binding post. Well, to solve that, you can just stick the board upside down in this case, and bingo, you've now got your binding posts on the bottom of the case like this.

**Dave Jones:** So, your wires come out, and your knobs and your switches are on top, so they don't get in your way of your wiring. It's pretty neat, versatile case. I really like it.

**Dave Jones:** And one of the things I really love about this case, in fact, Hammond cases in general, is that look at the data sheet. Here it is, the RM2015M, and check out the awesome interactive 3D model of the case, which you can download as well.

**Dave Jones:** Great if your uh CAD package, PCB CAD package, supports 3D models. You can import these, and you can see if your boards fit and things fit on your front panel.

**Dave Jones:** And it's just it's beautiful. I love it. And you can actually interact with the thing and not only rotate it around like this, which is brilliant, but you can actually select individual parts of it like this.

**Dave Jones:** And this is And you can do all sorts of other interactive stuff. And this is all within inside the PDF data sheet. Brilliant. Why can't every manufacturer do that?

**Dave Jones:** It really just makes you want to choose their cases just for the cool data sheet. But a third thing that makes this really cool is that this is a 50 mm high case.

**Dave Jones:** It's available in a shorter version, 30 mm high, 50, and also 70. And here And this is what it looks like. So, it's actually a bigger The holes are exactly the same.

**Dave Jones:** Footprints directly compatible like that. So, you can actually put it in a bigger beefier case like that. I love it. And then you don't have to change a PCB design.

**Dave Jones:** If you need more room in the case for something for some custom mod or something like that, you can put it in this case. But although this case I think is a bit too big.

**Dave Jones:** I mean, it just looks a bit, yeah, looks a bit tall and bulky and stuff like that. So, I think my goal is to get it into this smaller size case like this and try and get the LCD and the binding posts and everything in there plus all the connectors on the back and the ethernet and power and other stuff on the back.

**Dave Jones:** So, let's take a look at it. So, this is my Rev B board. As you've seen this before, I've done some troubleshooting on this thing. And I was thinking about it and looking at the big heat sink on the back.

**Dave Jones:** There are a couple of things I was looking at. A, the big heat sink on the back meant I couldn't access ethernet. I'd have to If I wanted that ethernet module which I was talking about, sticking it in the middle of the board here somewhere or having it um somewhere else in the board, maybe on the top uh board of the case then, really there's nowhere to put

**Dave Jones:** it cuz it's failing with one of the mounting holes there. It's not nice. I can move it over, but then there's no room for the DC input uh charging jack.

**Dave Jones:** Or originally, I was going to have a USB uh charging jack and it actually uh charge up from either a DC jack or a 5-V USB as well. But, I think I'll just start stick with the standard jack, which will go into.

**Dave Jones:** Now, so I thought, uh you know, there's a big heatsink on the back and it costs about four bucks or something in volume. The heatsink is not cheap. So, I was looking at, you know, the price was creeping up.

**Dave Jones:** I was looking at maybe trying to shave some cost off and I thought, well, uh gee, a couple of things led to it, okay? One was the price of the uh heatsink and the size and the accessibility of the connectors on the back.

**Dave Jones:** So, if I could get rid of that heatsink, then well, I can save some cost and get room for the ethernet uh module there and and other stuff on the back.

**Dave Jones:** So, that'd be really nice. Save some cost, get some room. Beautiful. But, I'd have to change it to a switch mode design, which we'll go into, but I decided, nope, I'll just keep my um LT uh 3080 as we've got and the other thing um is I was going to charge it from three 18650 lithium ion batteries.

**Dave Jones:** And once you go to three of these or four even, the uh charging solutions for those become more complex and more expensive and more difficult and things like that.

**Dave Jones:** So, and really, it was taking up a fair bit of uh room inside this thing. I couldn't mount them in the other uh orientation if I wanted to. And really, with a linear power supply I was using here, you're really pissing away a lot of your capacity in your battery due to your linear uh voltage regulator.

**Dave Jones:** So, you know, if you've got uh 12 volts coming from your uh uh batteries, for example, then well, and you're only putting 3.3 volts um out, uh which might be a typical uh power for a project or something like that, there's a lot of power wastage in your heat sink.

**Dave Jones:** You're just throwing it away down the drain. Can't have that. So, I decided to go to two uh lithium ion 18650 batteries. I can mount them in other orientations, ditch the top board on the top, uh put in the battery charging circuitry onto the main board.

**Dave Jones:** So, all I've got to do is have a connector coming off, going to the battery pack, and getting rid of the heat sink by actually having a switching pre-regulator.

**Dave Jones:** Beautiful. And the other thing was the LCD. I was originally going to have like a ribbon cable, and there's my LCD connector there. I was actually going to have it um you know, a ribbon cable coming out to the front of the board, and really, you know, it's There there's no way to mount this um on the front panel.

**Dave Jones:** It'd have to be glued in place or something ugly like that. So, I decided, well, I'm redesigning the board anyway, so why not actually, because this is a PCB mount um uh LCD, it's got the uh RGB LEDs on the side, plus the pins there.

**Dave Jones:** It'll mount directly on a board. I might as well go back to the original intention I had before I got the ribbon cable uh before I sort of uh relented and went for a ribbon cable is to have just a vertical PCB coming out of here, like this, and and that would actually hold the LCD in place just in front of the front panel.

**Dave Jones:** But, to do that, of course, I didn't have room for it before because I had the 5-volt USB on the front. But, aha, if I was getting rid of this heat sink on the back, then I couldn't have this uh couldn't really have this 5-V voltage regulator anymore, so I decided, uh, bugger that, I'll just get rid of the 5-V output completely, and that gives me room just behind the switches on the

**Dave Jones:** front panel there to actually put a vertical riser board to hold my LCD in place. So, I think that's a a more elegant design. I've dropped the 5 V, but I think I've gained it in terms of, uh, just nice, um, build functionality and mounting the LCD.

**Dave Jones:** And if you're wondering what the deal is here with the, uh, heat sink sticking out the back like this, and I've actually designed my board to poke out the back like that, it's done so that the back panel here would slide just behind, it'd have actual, uh, cutouts for the two voltage regulators, and that back panel there would just slide directly out there, so it just isolates

**Dave Jones:** the heat from the inside and keeps it on the outside like that. Well, you got the plastic rear panel that just slides into those slots over there like that.

**Dave Jones:** So, I'm going to replace, uh, that because I'm getting rid of this. I still need some heat sinking, uh, even though we're going to have a switching pre-regulator on this thing.

**Dave Jones:** I'm just going to have the LT3080 directly on an aluminium, a flat aluminium back panel. Easy.
