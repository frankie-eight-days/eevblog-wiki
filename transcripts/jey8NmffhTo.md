---
video_id: jey8NmffhTo
title: EEVblog #1158 - How To Create PCB Mod Boards
url: https://www.youtube.com/watch?v=jey8NmffhTo
source: youtube-asr
timestamps: {"0": 1, "1": 15, "2": 32, "3": 59, "4": 73, "5": 93, "6": 100, "7": 122, "8": 134, "9": 148, "10": 158, "11": 178, "12": 196, "13": 213, "14": 222, "15": 235, "16": 247, "17": 257, "18": 268, "19": 281, "20": 297, "21": 309, "22": 327, "23": 352, "24": 368, "25": 380, "26": 390, "27": 402, "28": 424, "29": 433, "30": 448, "31": 465, "32": 479, "33": 495, "34": 512, "35": 527, "36": 536, "37": 547, "38": 558, "39": 570, "40": 587, "41": 602, "42": 617, "43": 630, "44": 643, "45": 653, "46": 663, "47": 683, "48": 698, "49": 717, "50": 735, "51": 746, "52": 754, "53": 765, "54": 795, "55": 803, "56": 820, "57": 825, "58": 837, "59": 847, "60": 858, "61": 878, "62": 900, "63": 909, "64": 921, "65": 936, "66": 951, "67": 963, "68": 971, "69": 977, "70": 991, "71": 998, "72": 1010}
---

**Dave Jones:** Hi, quite often in product design, product manufacture, production, repair, you might have to upgrade things in the field, you might find a fault in your product after you released it, or you might want to upgrade its performance, you want to make some changes, things like that.

**Dave Jones:** There's plenty of reasons why you might actually want to modify an existing populated PCB. Not always can you just re-spin the board as it's called, re-lay it out to add a new component, add a different component, something like that.

**Dave Jones:** This is actually very common in the industry, and I've actually worked in large companies, uh defense companies in particular, where they'll actually have specific component obsolescence engineers, where you have to maintain this military equipment, very expensive equipment, existing boards out there that have already been manufactured, you want to do upgrades to them, or a component becomes obsolete, for example, and you have to replace it, but you

**Dave Jones:** can't just re-spin the board and re-manufacture these things. The boards cost can cost, you know, tens of thousands of dollars in many cases, and you just don't want to re-spin those, or they're fitted to existing equipment, they've already been qualified and stuff like that.

**Dave Jones:** You just want to make a small little change or upgrade, or replace a component to a different package, for example, very common that components in certain packages go obsolete over years, or they might discontinue some sort of a programmable part, you have to replace it with another programmable part that only comes in a different footprint, and things like that.

**Dave Jones:** So, you want to actually upgrade these boards. How do you do it? So, I thought we'd take a look at it, because let's take this board as an example.

**Dave Jones:** It's a ridiculously complicated board, and would be seriously expensive to actually, um, not only, manufacture the board from scratch, but if you've got a big stock of these blank PCBs, for example, just a blank PCB can be seriously expensive.

**Dave Jones:** So, often it makes economic sense to do what's called a a mod board, a daughter board. There might be many other different names for it. Let us know in the comments if you work at companies that call it different things, but we'll just call it a mod board.

**Dave Jones:** So, it makes sense just to modify these boards with a little mod board. And of course, you might have to modify boards of any complexity just to attest that your new modification works.

**Dave Jones:** So, typically you'll, you know, you'll hand solder that. There'll be little mod wires going everywhere. It'll be really ugly, but you don't necessarily want to do that in a production environment.

**Dave Jones:** You know, if you've got a thousand boards you're manufacturing a new production, 10,000, 100,000, or if you've got boards out in the field, you don't want to the repair techs to go out there and have to put in mod wires, cut and strip wires, and individual parts, and bend them over, and put electrical tape in there, and just all sorts of dodgy stuff like that.

**Dave Jones:** So, you want to do a nice simple mod board, like a professional solution for modifying a doesn't have to be this complex. Even relatively cheap and simple boards, they can be lots of economical or other sort of logistical issues why it's better to actually do a mod board.

**Dave Jones:** So, I think it's an important skill to have. Not only know that mod boards like this, and this is a very simple example, but even more complicated ones, like you might be familiar, for example, if you're into like gaming consoles, a lot of those illegal mod boards and things like that you can buy.

**Dave Jones:** A lot of people fitted them themselves. So, you buy them as a kit. They might come on a little board that's sort of, you know, a weird-looking board that's convoluted shape or whatever to fit around existing components.

**Dave Jones:** That's a classic example of a mod board to an existing product that really there was no other choice to do it. and you want a professional solution that's easy to use so that people can install it.

**Dave Jones:** They don't want to have to run wires and strip wires everywhere. It's better if it's a professional solution on a board, something like this. So, it's really important to know that A, you can do this sort of thing and that this is a professional solution.

**Dave Jones:** So, a really important topic. I've actually got a mod board here, which we'll take a look at. And this is for the 121GW multimeter. We upgrade one of the parts in it.

**Dave Jones:** So, I thought, "Yeah, this is a good excuse to do a video on this." So, we'll take a quick look at this and maybe another example of a production mod to a real expensive bit of gear.

**Dave Jones:** Let's go. Now, here's an example of a mod board on a real expensive board. This is from one of the Lecroy oscilloscopes. You remember I did a couple of videos trying to repair this thing, but it was unfortunately BR, beyond economical repair.

**Dave Jones:** And can you spot spot the mod board? Where's Wally? There's somewhere. If you're watching in 4K, I'm sure you can spot it. Yep, there it is down there, right on the front end like that.

**Dave Jones:** You can see they've got this board with a whole bunch of components and they've even like double stacked the melts. You know I'm a melt fanboy. So, I'm really excited about the melts double stacking there.

**Dave Jones:** But a little mod board that they've obviously put on this board. Now, whether or not this was done at the production stage or whether or not it was like an upgrade or you know, something like that or they released it and they found an issue out there and they wanted to you know, fix it or whatever.

**Dave Jones:** If you do know the details of this particular mod, then please leave it down below. But anyway, fact is that they have actually modded that front end. You can see that they've got a little board here, obviously snapped off from a panel, which we'll go into detail a minute and also we'll go into detail of of little uh on the side here of the board where they've actually soldered it down to uh

**Dave Jones:** like existing components. You see they've already got an existing component there. They just soldered that over. And here's the blank space where it actually uh went. And uh this wouldn't have been uh designed at the production stage cuz if they were laying out this board and and clearing that space in there, um they would have just put the parts in there.

**Dave Jones:** So, obviously post-production kind of thing or some sort of upgrade or something like that cuz this is a real huge expensive board. And as I said, even if you got the blank board stock can be very expensive, but let alone a populated board.

**Dave Jones:** You don't want to scrap a populated board. Uh it can cost thousands and thousands of dollars. Or even as I said, some of the stuff I've worked on, many tens of thousands of dollars.

**Dave Jones:** Um even into the six-digit category for a board is not unheard of. So, they obviously like got a little bit lucky because if there was some space available, they can always put it on top of the components really.

**Dave Jones:** And the fact that it was a square board, um that fitted in there quite nicely. So, yeah, um sometimes you get lucky. Other times as I said, you know, if you need to connect, say, you know, this spot here over to like over to here, you might need some convoluted board that sort of runs around this chip here cuz it's got this uh tie down uh point here.

**Dave Jones:** So, you might need, you know, and you don't want to you want access to the pots. So, you might have to do some weird thing. You might even have to do some flex uh solution or something like that.

**Dave Jones:** But, yeah, you can see how you just tie a mod board into existing components like that. It's nice and simple, professional, and it allows uh repair techs in the field to actually upgrade these things, which is important, or just easily solder them down in production.

**Dave Jones:** Or as we'll see in a minute, actually uh treating them as a pick-and-place component and reflow soldering them. So, here's an example of a mod board uh panel. In this case, it's for the 121GW multimeter where we wanted to upgrade an existing uh part on a some already populated boards.

**Dave Jones:** So, it it was an SMB part that we upgraded to two 23 parts like this. So, how do you do it? Well, let's take a look at the details cuz this is just one example.

**Dave Jones:** There's many ways to do it, but there's lots of issues which go into making a board like this. Unfortunately, this is not the full panel. As you can see, it's been broken off here and as you can tell by the fiducial marks up here and the rounded and the tooling holes here, the panel is actually this width here.

**Dave Jones:** It's not hugely big, but it obviously extended down here like this. And this is how you want to do it. You want to manufacture these in panels like this with either break-off tabs or V-scoring or something like that so you can easily cut them out at a later stage.

**Dave Jones:** Cuz the last thing you want to do is get a tiny little board like that and give that to your pick and place assembler and go, "Assemble that board, please." They'll just roll their eyes and charge you a fortune and probably just end up hand-soldering anyway.

**Dave Jones:** So, how do you make a nice panel like this one? Well, I've done a whole panelization video, which is very popular. I'll link that in at the end and down below if you haven't seen that.

**Dave Jones:** Highly recommended. Lots of detail on how to do routing and V-scoring. And that's what we've got here. We've got a combination of routing and V-scoring. So, let's have a look.

**Dave Jones:** You can see that obviously they've got they've routed out this board like you didn't have to add this little like chamfer in here like this. It's not necessarily important to do that.

**Dave Jones:** They've just decided to do that. No problems whatsoever. But anyway, you just route like that like a 2.4 mm routing tool might be like a standard diameter. As I said, look at that panelization video I've done.

**Dave Jones:** And we've got a combination of V-scoring like that. And I'll show you up close. But as per regular panels, of course, you want your fiducial uh alignment marks. You want your tooling holes on your outer strip like this so that it can go through the conveyor machine in the pick and place.

**Dave Jones:** So, they'll have a rail up here and another rail down here, and your board passes through the passes into the pick and place machine, gets picked and placed, and then it goes out on those rails out in a via these tooling holes, which move it along, and it goes out to the reflow oven.

**Dave Jones:** So, you want to automate that sort of process. Now, you can see that all the copper fill has been left on here. It's not on the bottom of the board because we don't actually want copper underneath here.

**Dave Jones:** There's just no reason to have it, but like there's been copper in fill like this, just floating copper like that. The reason to do that is just so it's nice for the PCB manufacturer so that they don't have to etch away all the copper.

**Dave Jones:** So, you might as well just leave the you know, leave the copper on there to make the etching nice and easy. We've got a combination of routing slots, V grooving top and bottom, or V scoring as it's called going across the panel here.

**Dave Jones:** You might be able to see the detail in there. I'll show you in a sec. And also, we've actually got what's what are called castellations or half-moon pads going right across the scoring here.

**Dave Jones:** That not only allows for the boards to be individually snapped and cut out of the panel easily, but then it allows you to actually solder these down as a surface mount component.

**Dave Jones:** Because as I said, in this case, this little mod board here is actually replacing an SMB footprint part with two in this case, two SOT-23 transistors. Now, you can make this panel as large as you want, of course, subject to your assembler and how it fits in their machine and whatnot.

**Dave Jones:** Now, this is a 0.8 mm PCB, so that's pretty thin. There's no real need to have it uh 0.8 mm in this particular case, but you can see that it's actually going to be quite flexible like that in both directions.

**Dave Jones:** You don't want to do it too far in that direction cuz you're going to snap off the uh V-scoring uh along those boards. But uh the problem is is that if you have one big panel like this and you stick it in your pick and place machine and it's only held with the rails at the top and bottom, when you put it in like this and the pick and place head comes down to

**Dave Jones:** place parts, whoops, it's going to it's going to warp in the middle like that. So, uh boards like this um it's quite common for your assembler to actually uh manufacture a custom uh tray that actually this board just sits snugly inside the tray and it's fully supported over the entire area like that.

**Dave Jones:** So, yeah, but but your manufacturer will um advise on that sort of stuff and um often just handle that for you. They might do that without even telling you.

**Dave Jones:** You'd just say, "Assemble my panel, please." and they'll go, "Okay." And they'll have like as part of the tooling charge will be manufacturing a uh holder for this particular board.

**Dave Jones:** Now, you can see the V-grooving across there. This isn't a particularly deep V-groove. If you have a look down there, it's uh in fact, bottom seems to have a different depth.

**Dave Jones:** I wonder if that's actually uh consistent across the board. Yeah, it seems to be. I think they've got possibly a uh sharper V-groove on the bottom. Did I'm not sure if that's on purpose or whether or not that's just the way that the you know, tolerancing how the uh the machine the V-groove wheel was actually uh set on the thing.

**Dave Jones:** And there's the bottom of the board and this V-grooving needs to be controlled, you know, fairly accurately at the factory, especially for a like a 0.8 mm uh PCB like this one.

**Dave Jones:** The thinner your PCB gets, the uh you know, the more critical your tolerance gets on that uh V-groove cutting wheel. But, in either case, there's more than enough uh fiberglass left in there to hold this uh board together during that handling and whatnot, but it allows easy snap-off.

**Dave Jones:** So, as you can see, when you snap it off, you might be left with a few dags and things like that in there, but uh this is fairly common.

**Dave Jones:** It's not generally going to be an issue. So, you're left with a half-moon castellation like that, and which allows you to just easily solder that onto a like existing pads onto the board.

**Dave Jones:** And then, when you snap it off, you're left with a tiny little uh board like that, and you can see that how that is basically becomes a little uh surface-mount component.

**Dave Jones:** There's other ways you can do the uh castellations and uh you know, stuff like that if you really want to get all fancy-pantsy about it, but you know, those half-moon castellations work well.

**Dave Jones:** Then, you simply solder that as a component. In this case, you would hand-solder it, but you could actually reflow it, but because this is a retrofit, generally a retrofit to an existing uh board, although it doesn't have to be if it's a like an obsolescence uh component replacement or something like that, you can actually get this actually placed by the pick-and-place machine and reflow it.

**Dave Jones:** But, of course, like you wouldn't have it on any um production reel or production tape or anything like that. So, you might put it may maybe you might do it if you're like really keen, you might do a a specialized uh production tray for it or something like that that held it uh as a tray-based component in the pick-and-place machine, which could then uh pick it up just, you know, using

**Dave Jones:** your existing nozzles onto the existing uh component, and then lift it onto the board, and actually place it and have it reflowed. And of course, this is a real simple example.

**Dave Jones:** There's only uh two transistors in there replacing a single uh surface-mount part, but like you can make these as weird and wonderful and convoluted as you like. That could like spread out over in entire board.

**Dave Jones:** You can even do this as a flex circuit as well. But the problem with a flex board is that you don't get the same kind of castellation hole on the end that you would on a fiberglass PCB like this.

**Dave Jones:** But yeah, you can have pads either on the top or bottom or whatnot and then just start solder bridge those on. No problems whatsoever. Both are valid techniques. So in this particular case, we wanted to do replace an SMB component with two SOT-23 parts.

**Dave Jones:** As you can see, doesn't quite fit on there. You could sort of like stagger them a little bit. So like this one went behind there if you had the width like this which we didn't really have.

**Dave Jones:** But because we actually had two of them there and had an adjacent pad. Sorry, you can't see under there, but normally there's a pad there and a pad there.

**Dave Jones:** Then we can just have it going from that pad to that pad. No problems whatsoever. And this is just a real simple example. But it gets the point across.

**Dave Jones:** So it's just real neat and tidy and it simply becomes just it looks like yet another part. In fact, you know, if you zoom out of this like you you're really like hard pressed to tell that you know, that's actually a mod board in there really.

**Dave Jones:** So I hope you found that video useful and if you did, please give it a big thumb up. And as always, you can discuss down below or over in the EV blog forum.

**Dave Jones:** And if you like my content, you can always support me on Patreon. Links down below and I accept cryptocurrency donation or what sort of jazz. And as much on my store.

**Dave Jones:** You know the deal. Catch you next time.
