---
video_id: 9pFal1lgFl0
title: EEVblog #245 - PSU Design Part 10 - PCB Layout Editing
url: https://www.youtube.com/watch?v=9pFal1lgFl0
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 24, "3": 37, "4": 64, "5": 74, "6": 89, "7": 103, "8": 116, "9": 128, "10": 142, "11": 164, "12": 181, "13": 192, "14": 215, "15": 225, "16": 235, "17": 254, "18": 277, "19": 289, "20": 303, "21": 315, "22": 326, "23": 339, "24": 350, "25": 363, "26": 375, "27": 402, "28": 413, "29": 426, "30": 441, "31": 451, "32": 463, "33": 473, "34": 486, "35": 500, "36": 508, "37": 521, "38": 529, "39": 543, "40": 554, "41": 567, "42": 583, "43": 593, "44": 606, "45": 627, "46": 646, "47": 656, "48": 676, "49": 682, "50": 698, "51": 710, "52": 720, "53": 737, "54": 750, "55": 771, "56": 793, "57": 807, "58": 822, "59": 830, "60": 845, "61": 859, "62": 869, "63": 882, "64": 899, "65": 910, "66": 920, "67": 930, "68": 943, "69": 957, "70": 978, "71": 992, "72": 1018, "73": 1028, "74": 1043, "75": 1052, "76": 1062, "77": 1081, "78": 1089, "79": 1096, "80": 1119, "81": 1130, "82": 1147, "83": 1161, "84": 1172, "85": 1183, "86": 1192, "87": 1208, "88": 1228, "89": 1236, "90": 1250, "91": 1261, "92": 1273, "93": 1282, "94": 1292, "95": 1310, "96": 1320, "97": 1332, "98": 1352, "99": 1368, "100": 1378, "101": 1389, "102": 1398, "103": 1410, "104": 1422, "105": 1437, "106": 1447, "107": 1458, "108": 1471, "109": 1479, "110": 1489, "111": 1504, "112": 1516, "113": 1533, "114": 1546, "115": 1563, "116": 1578, "117": 1593, "118": 1600, "119": 1609, "120": 1622, "121": 1640, "122": 1651, "123": 1663, "124": 1675, "125": 1686, "126": 1695, "127": 1705}
---

**Dave Jones:** Hi. In the last video, I showed how I laid out my Rev A power supply board and what went into that. Well, I said I'd do another video showing you how I laid out the Rev B revision of the board.

**Dave Jones:** In this case, I took the existing Rev A board I've got here, as you saw last time, and basically changed it a little bit, added a few components on here for Rev B.

**Dave Jones:** And it doesn't look like there's a huge amount of difference. There's Rev A. It's down in the bottom right corner here. There's not too many components, for example, and I've added those I squared C chips over here.

**Dave Jones:** And it's a little quite a bit more dense layout in terms of component density and things like that. So, but there weren't a huge number of changes, but surprisingly, as you might find out, it does actually take a almost same amount of effort really to uh make some small changes to an existing board as it does to layout an existing board from scratch.

**Dave Jones:** That's not always the case, but in this case, it it probably wasn't too far off. So, what I'll do is I played back the existing Rev A one at times 10 speed.

**Dave Jones:** I didn't want to make this video as long as the last one, so I'll do this as times 20 speed. So, you can figure out how long I did based on the amount of time multiplied by 20.

**Dave Jones:** Let's start out by having a look at the schematic here. And here's the existing one. I've shown this before. I squeezed it all onto the one A4 page, and it looks quite dense, but I was I was happy that it was all on one page.

**Dave Jones:** So, I did keep it all on one page for Rev B, but I actually modularized the thing and changed it to an A3 size sheet like this. And of course, I added these I squared C uh chips down here.

**Dave Jones:** They're two 18-pin DIP packages. So, they're fairly, um you know, large uh devices to fit onto an existing populated uh board. It's not like they're little surface-mount jobs or something like that.

**Dave Jones:** Um what I I expanded the LCD connector down here with the RGB LED interface. I uh increased the um the serial uh header IO to make it FTDI uh compatible.

**Dave Jones:** So, I increased uh the number of pins on there to break out the things. I added another serial um IO connector for um well, not serial IO, sorry. Uh that's labeled incorrectly, but another IO connector for the uh switch um IO chip down here, just in case you wanted to add like a keypad interface or something like that.

**Dave Jones:** And uh that was that was really the main uh change. Of course, there are a couple of uh things around the um AVR microcontroller, like the uh like the 8-MHz resonator here and a couple of pin changes and and stuff like that.

**Dave Jones:** A few an AREF change and a reset pin change and a couple of other things. But, so not a huge amount of difference, really, uh compared to the two uh the two schematics here.

**Dave Jones:** The LED, of course, um on the reset pin. That was one of the things that we talked about changing. So, one of the first things you want to do once you've got When you want to update a board like this, once you've done your uh your new schematic like this and you've got your footprints attached to each component, you know, so if I double-click on that component, it pops

**Dave Jones:** up and and it's the correct package I want, DIP 18, and uh all that sort of stuff, then what you do is you push this information through to the schematic.

**Dave Jones:** And I won't you know, I won't tell you how to use Altium Designer here to actually do that. But, um it's actually off the screen capture here. You can't see it, but it's update PCB document.

**Dave Jones:** And when you push through all of these uh changes to an existing board, then what you end up with is a board with uh what you end up with is your rev A PCB like this, but it'll have all of your additional components over on one side here.

**Dave Jones:** At least, that's how Altium does it. Other packages will vary, but anyway, so you import all of your extra components, and you'll end up with a whole bunch of components over here with all the rats nest going uh over, all the net connections going over, and you've got to rip up your existing design or try and put them fit it onto your existing rev A board.

**Dave Jones:** So, let's actually try and do that live here. What I'm going to do is I'm going to push through my new rev B schematic. Uh I'm going to push that through to my rev A PCB.

**Dave Jones:** And update component links, yes. Uh yes. And continue. And bang, it's going to execute. It's going to make all these changes here, all these nets. It's going to add in all these components, all that sort of stuff.

**Dave Jones:** So, let's execute all that. It goes through. This is just an Altium Designer specific thing. There might be a few errors in here if you haven't got footprints correct and stuff like that, but generally, what you're going to end up with is bingo.

**Dave Jones:** Here it is. You're going to end up with this In the In this case, it's actually a room Altium Designer. Um puts it in a room for you. I don't like that.

**Dave Jones:** So, what we've got is we've got these two 18-pin uh I squared C uh interface DIP chips. We've got the new uh serial connector up here, or it's actually replaced it.

**Dave Jones:** Um you'll notice that down in here the LCD LCD connector down in there is now got these three extra pins there, One, two, three, and you see they're overlapping.

**Dave Jones:** So, it it took that existing eight-pin or seven-pin connector or whatever it was and added three extra pins. And you can see that they're conflicting with the existing vias there and traces and ground plane underneath and things like that.

**Dave Jones:** So, that's what happens if you change your footprint. And likewise, the serial connector over here, which was only a five way one down here or there abouts. It's It's added the extra pins on there.

**Dave Jones:** So, we're going to have to end up moving that. And I'm not going to clearly do that now because I've already done that. And I'll play that back. I'll play back all these edits at times 20 speed so you can see just how much work is involved in shuffling things because you've got to fit all of these components here onto somehow, you know, down in here.

**Dave Jones:** I've got to get these DIP packages down in here like this. I've got to somehow get a serial connector on the board. And you'll see in the final layout that I end up adding it around about up here somewhere.

**Dave Jones:** And there's another connector down here. There's and all these resistors around here. And and it you know, it's it looks a bit daunting when you first actually do it.

**Dave Jones:** And well, and and it pretty much is. And that's why it takes a lot of little edits and shuffling tracks here and there and ripping things up and moving and re-trying stuff and finding out that the last component just didn't fit.

**Dave Jones:** And then I'm going to have to move this whole section over. And then it all gets quite complicated. So, that's why an edit of an existing board, even a fairly simple edit.

**Dave Jones:** I mean, there's not that many components we're trying to add here. There's two chips, a couple of connectors, and a you know, a dozen dozen resistors or so. But yeah, it can take almost as long as the existing board.

**Dave Jones:** You'll find it's actually quite remarkable how long it can actually take. And uh once again, that depends on the complexity of the board. Some it won't matter, you know, it'll be very quick and easy.

**Dave Jones:** Others will take could take five times longer than the original uh layout. It could be really bad. You might have to rip up the whole thing. But as you'll see hopefully in this uh time-lapse video that uh I won't make too many changes.

**Dave Jones:** Like the main um the main AVR microcontroller here, I I don't actually uh end up moving that, I don't think. Maybe I shuffle it a you know, a couple of millimeters here or there or something like that.

**Dave Jones:** I don't actually remember, but you'll find that a good lot of it is still in the ex- existing location. But of course, um some of this silkscreen, I've got to move that sort of stuff.

**Dave Jones:** The platypus is probably going to move and uh all sorts of things. One of the first things you're going to want to do uh is get rid of that ground plane because it's going to be a pain in the butt.

**Dave Jones:** Now, I Now, you don't actually go and actually delete the ground plane. So, what you can do is just go in there and you can actually uh uh hide.

**Dave Jones:** If you go into polygon actions, you can actually shelve all of the polygons. So, bang, I've now got all the bottom layer available for um for all of my uh routing and things like that so nothing conflicts.

**Dave Jones:** And you'll find that if I go in and do a design rule check now, there'll be probably, you know, there could be dozens or hundreds of errors or something like that because all things are shorted out and not connected and various things.

**Dave Jones:** But as you can see, all of those uh nets, all of those rats' nests, those from-tos as they're called in the uh Altium world, they're um they're all the unrouted connections.

**Dave Jones:** So, we've still got to make all of those all of those connections. So, we'll go through the uh times 20 time-lapse. Now, um unfortunately, the first part of the time lapse was was actually corrupted somehow, so I didn't actually capture that.

**Dave Jones:** So, you it'll start actually part way through the process where I I believe I have a couple of the chips down in here and I've already shuffled a few things around.

**Dave Jones:** So, sorry about that, but after that, I think I captured most of it. So, I'll add some commentary on top of the times 20 time lapse. Let's go. And here we go.

**Dave Jones:** As you can see, I've got already a bunch of resistors there in place. They're the pull-up resistors, I believe, for the I squared C chip, which doesn't actually need because it's got internal active active software pull-ups you can define within the chip, but anyway, I thought I'd add some external ones in there.

**Dave Jones:** I might remove them on the next version, perhaps, cuz they do take up some room. But anyway, let's take a look. I'm trying to shuffle in the chip there and you'll notice that right next to it I'm now dragging it out and dragging it around trying to figure out the best orientation for it and how it's going to work out it's going to wire into the other parts of it.

**Dave Jones:** And I've decided to actually move that Oh, no, there we go. I moved it back and I've looks like I've settled on that orientation at least for now. I've dragged in the other chip.

**Dave Jones:** I'm checking something on the schematic there. Mucking around with a bypass cap there and you'll notice that I've got the connector the expansion connector right next to the chip because that's where it should be because you wire it if you actually look at that little circuit it wires for that for those pull-up resistors in that expansion connector.

**Dave Jones:** They're right next to each other. So, it makes sense to put it right there. It doesn't make sense to put it on the edge of the board or somewhere else.

**Dave Jones:** It's silly. You'd have to wire eight traces right across. But anyway, now I'm mucking around with uh the odd resistor up the top there, moving some traces. Not sure, putting in a via there, jumping through to the bottom layer because I couldn't get around.

**Dave Jones:** So, I'm um uh there's a uh a TO-92 package there I'm shuffling around. I'm moving a few things up here. I'm not exactly uh sure why I's doing that.

**Dave Jones:** I'm I'm obviously trying to gain room. Anything that I move within uh doing this board, um you'll have to forgive me. It's been a couple of weeks since I've actually uh laid this thing out.

**Dave Jones:** Uh now I'm doing the commentary, so I've got to remember what I actually did. I'm playing around with the schematic, checking something. I've got another um I've got the bunch of uh 10 I've got another bunch of 10 resistors there, and I'm uh I've put those in somewhere, but I haven't uh been too concerned with those.

**Dave Jones:** I lost interest in that and decided to go on to something else. Now I'm looks like I'm tackling the um getting room for the serial connector. So, you'll notice that I'm uh around the AVR chip here.

**Dave Jones:** This is going quite fast. This is hard to do. But, I've pretty much decided, I think, at this point that I'm going to put that uh serial expansion connector right next to the chip because it makes sense because most of the um signals uh not only duplicated from that um uh in-circuit programming connector that I've got next to the chip there, the AVR that's labeled AVR ISP.

**Dave Jones:** So, it makes sense to put the connector, whereas before I had it in the top left uh corner, but I've I decided that uh that I really had to compromise there, and I just put it smack in the middle of the board right next to the chip because getting um those 10 traces all the way over to the other side of the board, it would have required me to rip up a whole ton of

**Dave Jones:** stuff, probably half the layout on in that top uh left corner or most of it. It would have been really ugly. So, I've decided to put um the serial connector, which I'll move it in there later, but I think I'm just uh making room for that now.

**Dave Jones:** I'm putting in a couple of other uh looks like I'm shuffling my this is my microcurrent part of the circuit. I changed the odd resistor there. So there were a few missing resistors there and I've decided to shuffle that over because I need to get those multiple traces.

**Dave Jones:** You can see like running sort of like a bus there. I need to get those through and I know I'm going to need some more room in there as well.

**Dave Jones:** So I'm uh ripping up that sort of stuff over rerouted the power there for the microcurrent Maxim chip and I'm playing around with that bus there deciding because the pinouts on my chip have changed by the way my AVR microcontroller.

**Dave Jones:** So I'm trying to actually uh trying to get the trace on probably have to rip up half the traces to the microcontroller and then rewire them straight through like that.

**Dave Jones:** That's what I'm trying to do putting a few more resistors there. Uh dragged them in. I've decided now I want to shuffle them over to the left of those couple of pins.

**Dave Jones:** So unless I actually was commentating while laying out this video, it's hard to explain exactly what I'm thinking at this point because I'm taking into account a whole bunch of net connections and things like that and where they go and I can see them.

**Dave Jones:** You might not be able to see them there but I I've got the schematic in my head and I've also got the the rats nest lines there of where things going to go and I'm building up a map of all this stuff in my head pretty almost subconsciously kind of thing.

**Dave Jones:** So I kind of know that I'm going to need at least another two traces through there or through these two pins. So I better move those couple of resistors over and things like that.

**Dave Jones:** So looks like I I just highlighted the power net there. So I was obviously playing around with that. And I'm looks like I'm freeing up more room there for the serial lines.

**Dave Jones:** Here we go. I just dragged all those back. I've got uh I dragged in another capacitor there. That's all That's part of the reset circuit, I think, that changed between the two revisions.

**Dave Jones:** So, actually I'm Yeah, I'm going to have to move a lot more stuff in there to put in that serial connector. I'm mucking around with a few of the really just slightly tweaking the locations of those switches.

**Dave Jones:** I'm not sure why I did that. Probably I'm just a freeing up a few just a little bit of space here and there, a few few millimeters, things like that.

**Dave Jones:** Oh, that's right. I think they were placed on a different grid. So, I probably redid them on a metric grid or something like that, perhaps. So, once again, I'm probably using like a 50-mil grid here or a 25-mil routing grid with a 50-mil component or a half a millimeter component move grid.

**Dave Jones:** So, the component grid will be in a will actually be in metric and the routing grid will be in imperial, be 50 or 25-mil. I might switch to between those depending on the work down there.

**Dave Jones:** And here I am back at the I2C chip. And if you can see the the serial expand the this switch expansion connector in there, that 10-pin connector, it takes up no room at all because those traces go directly from the I2C chip right up through the resistors, through the connector, and it's it's all very efficient down there around that I2C chip.

**Dave Jones:** I really like that. So, if you're not fussy about where expansion connector goes, you can really save a lot of PCB space. And there we go. I'm Now I'm moving in my serial connector.

**Dave Jones:** Here it comes. I've Looks like I've shuffled up a few of Looks like I've shuffled up that back uh that protection uh diode there and I'm playing around with a few with the space up there and it's getting quite tight.

**Dave Jones:** There we go. I've moved moved the diodes again, the TVS there, and I'm shuffling Oh, there we go. Bang! I've got room for my serial expansion connector right next to the chip.

**Dave Jones:** Magic. I've shuffled in I'm not sure how long I am into the process now, but there you go. I'm re-routing a few of those traces there just so I can eliminate using any uh vias at all.

**Dave Jones:** I can wire those straight through and you can see how short some of those traces were. You you got a glimpse of that uh going directly from the AVR ISP connector through to the micro through to that um CN3 there, the IO expansion connector.

**Dave Jones:** And if you had that expansion connector right on the other side of the board, as I did before, then uh you would have to route all those traces from one side to the other.

**Dave Jones:** And on a double-sided layout like this, that could completely ruin your entire design. It'd be horrible and you'd have no ground plane on the bottom, be all ripped up.

**Dave Jones:** Or you'd have to restart the design from scratch. But now I'm left with all these uh traces there, which I've got to cut back. I've got to rip those up and uh um think about how to re-route those uh through the best uh through the best way to get those back to the microcontroller cuz the pinouts uh from my microcontroller have all changed.

**Dave Jones:** So, I've got to rip them up and then uh figure out the best routing scheme to get back to them there. And this is going quite fast and as you can see, I'm jumping back and forth between my schematic uh a lot.

**Dave Jones:** And that happens. I might even change a few nets there. Um I may have even uh pushed. Yeah, I think Yes, I did. There you go. I pushed through a uh change from my schematic through to my PCB because I thought that uh that would give me an easier uh routing path.

**Dave Jones:** So, I swapped a couple of pins. And that's pin swapping. You can do that using back annotation techniques uh depending on how your software works with that, but you can actually make changes in the PCB and then what's called back annotate that into your schematic.

**Dave Jones:** So, it'll automatically make schematic changes. I'm that works um sometimes, but I'm I'm a fan if it's just a simple edit like I'm just swapping two pins on a simple design like this.

**Dave Jones:** I won't use the back annotation feature. I'll just change it on the schematic and then forward forward annotation, push it through to the um through to the PCB. There we go.

**Dave Jones:** I couldn't get those two traces through. I had to shuffle the power uh trace up there, but I'm dragging those two traces at a time. Somebody asked that in the last video what I'm doing there.

**Dave Jones:** They aren't a differential pair. I'm just actually uh highlighting and dragging both traces at the time because I know they're going to the same side of the board. So, I may as well drag them um at the same time and keep them together and the software handles the spacing for that.

**Dave Jones:** They So, they would have been 10 thou uh space to meet my 10 10 uh rules and everything works fine. So, I'm back down to my uh I squared C devices down here and I'm shuffling a few traces there back and forth, figuring out the best route, and uh there you go.

**Dave Jones:** That's um and whoop, I'm back up to the Oh, there we go. I've decided I need more room. I just moved my platypus there, shuffled the serial connector again.

**Dave Jones:** I decided I needed it down one. I'm not sure the reason for that. Ah, I need more traces out of there. There you go. I needed a third trace to go from the bottom right corner of the board to the top left part of the board.

**Dave Jones:** So, instead of doing that on the bottom, which would cut through all of your uh ground plane, that'd be ridiculous. I decided to shuffle um couple of the power tracks and those diodes, those big diodes at the top, gain extra room for that one trace.

**Dave Jones:** Um it's a fair bit of work just to add uh when you get to the end of the layout, you might find, "Oh, I've got to get one trace left from one side of the board to the other." And then you might have to move 10 components.

**Dave Jones:** You might have to shuffle uh 10 components by, you know, 50 thou or something like that to get from one side of the board to the other. And it can be crazy.

**Dave Jones:** So, uh those Oh, there we go. I'm mucking Oh, looks like I've done most of it. I'm mucking around with some silk screen now. Looks like my routing is pretty much finished.

**Dave Jones:** I see a few resistors down the bottom. But, uh No, there we go. I've still got some traces. I did Maybe I was a bit bored there with the uh routing the traces, so I decided to do some uh therapy and go and move some of the silk screen for a while just to clear my head perhaps.

**Dave Jones:** Uh that happens. You can It's a complex process. There's one hell of a snaking trace that went from the bottom right uh bottom right corner of the board right around through to the micron.

**Dave Jones:** I ended up having to use a via. So, I'm really getting down to the nasty end of it now where um if you've got any traces left that need to go any significant distances, it can be a real real pain in the butt.

**Dave Jones:** And those four resistors down the bottom, they're um for the USB connector. So, I'm thinking I'm leaving those because they're not important. They're not um electrically important or anything like that because they're they're just setting the DC level on the USB port.

**Dave Jones:** So, I figured I'd put those in last. And if push came to shove, I could even possibly leave those off if I was absolutely desperate for room. If I had to leave some components off this board, it'd probably be those USB those resistors for the USB connector.

**Dave Jones:** Um cuz they're not essential. It's just a nicety. So, uh in effect, I'm um hedging my bet here that if I do run out of room, ah well, I can drop a feature.

**Dave Jones:** It's not unusual to actually uh do that on a project like this, where I'm changing my mind all the time with things. So, it doesn't, you know, it's not a huge deal if I figure out, "Oh, I don't have the space.

**Dave Jones:** I'll just drop that feature, or I'll change that feature, or modify it, or something like that." So, um here we go. I'm trying to get a trace right around the bottom edge of the board there.

**Dave Jones:** So, it looks like I shuffled up those switches just a just a tiny tad to get room for that second trace around the bottom, perhaps. Working on my power trace again there.

**Dave Jones:** And where are we up to now? Looks like we're still mucking around with the uh I squared C stuff down in I'm back on my microcurrent. Here we go.

**Dave Jones:** I don't think I've finished my microcurrent. And yeah, a few of the oddball resistor around there. Um these I haven't finished the connection for these resistors. I've shuffled part of the um part of the microcurrent circuit around there.

**Dave Jones:** And I've got the odd trace left. And I From memory, it's starting to get a little bit frustrating now. I've got a couple of oddball ones left. And it's getting quite tight.

**Dave Jones:** And and it's getting annoying. Now I'm thinking about my USB resistors. There we go. They just squeeze in there with a little bit of silkscreen overlap. Oh, well. You can't have everything.

**Dave Jones:** So, um maybe I shuffle tidy that up later. The last thing I'm worried about is a little bit of um silkscreen over silkscreen. That's no big deal at all for a board like this.

**Dave Jones:** And I thought I was up to my LCD connector here, but uh the RGB um extra pins. But I've already done those. I must have missed those somewhere within all this times 20 speed.

**Dave Jones:** This is phenomenal trying to keep up with this. But uh I think we're always done. Oh, look. There's a Yeah, a little pain in the butt trying to figure out the best way to route a few traces there.

**Dave Jones:** It's I ripped up, retry, try to via, try to eliminate any uh vias and traces on the underside if I can, things like that, even if the traces have to go snaking around the board um when you're down to the last couple.

**Dave Jones:** Because generally when you're laying out uh a board like this, you try and keep the traces the minimal length. That's the key. It's only at the end where you're so desperate to get uh you know, traces um that are finished.

**Dave Jones:** That's why you want to try and mount things uh route things as a modular type uh thing as I explained in the last video. Um Now, because then you can uh keep all the modular things and then you only have to join power and a few data connections usually between the modules.

**Dave Jones:** Depends on your design, of course, but um looks like I've still got a few traces up there. I've got uh some bypass caps up the top. I'm route trying to route my 5-V power around down to the bottom resistors.

**Dave Jones:** I've I mass moved a few of those resistors just to get a uh shuffled them over a bit just to get my 5-V power around. Now, this can be tricky because I've Look, I had to snake that five I had to um make that 5-V I had to neck down what what's called neck down the 5-V uh power trace.

**Dave Jones:** I probably used like a 100-mil width and I had to neck down to 80 or thin it down to try and get under those uh uh pots at the bottom uh cuz those pots have to be a certain distance from the edge of the board.

**Dave Jones:** So, I don't have much leverage in uh much uh uh spare room in moving those. So, I had to neck down the power, but I used 100-mil most of the way and looks like I'm trying to I'm rotating my platypus a few times.

**Dave Jones:** You know, it takes a bit of while to work out the best location for the platypus, but looks like it was the same as last time, just shuffled over a bit.

**Dave Jones:** Mucking around with the silkscreen and Jeez, I think we're almost done. I'm looking for my micro supply there. There we go. I think we're done. We're going to do a DRC check.

**Dave Jones:** There we go. There's our DRC And uh looks like we've got a few errors. Tidying those up. Looks like just a few uh clearance errors. Probably doesn't meet the 10 thou uh clearance.

**Dave Jones:** And it looks like I'm shuffling I changed my ground plane there. I'm changing my polygon. It's part of the ground plane. I've just decided to shuffle that there cuz there probably wasn't enough room there to get the uh the polygon was a bit thin there even though on the left-hand side even though it didn't carry any significant current on the left-hand side.

**Dave Jones:** Um just as good practice I decided to And there we go. Oh, you missed it. I just uh joined the polygon at the start point down in the bottom left corner.

**Dave Jones:** And now I'm mucking around. I'm in the whole size editor now. So, I'm just tidying up a few uh I think I'm in the whole size editor there. I'm just uh checking a few things and boom, that's it.

**Dave Jones:** Is that it? That's all we got? It's all over. So, there you go. There's our completed board. And yeah, that took probably um not as long as the original layout but uh not that far off it.

**Dave Jones:** And there was a lot more uh involved in there. A lot of thinking, a lot of rip up, retry for a lot of things. And but as you can see, I didn't rip up and retry a lot of components.

**Dave Jones:** So, just the act that you've got to do a dozen or so components even on a fairly simple, rudimentary double-sided design like this can take a fair amount of time.

**Dave Jones:** So, there you go. Uh I hope you've given that's given you a bit of insight into uh not just laying out a board from scratch but actually making changes to an existing board.

**Dave Jones:** I'll catch you next time.
