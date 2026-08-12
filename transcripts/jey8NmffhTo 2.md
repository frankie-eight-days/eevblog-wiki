---
video_id: jey8NmffhTo
title: EEVblog #1158 - How To Create PCB Mod Boards
url: https://www.youtube.com/watch?v=jey8NmffhTo
source: youtube-asr
timestamps: {"0": 1, "1": 15, "2": 32, "3": 51, "4": 65, "5": 78, "6": 93, "7": 105, "8": 125, "9": 137, "10": 153, "11": 167, "12": 181, "13": 198, "14": 211, "15": 222, "16": 236, "17": 247, "18": 262, "19": 275, "20": 293, "21": 307, "22": 321, "23": 333, "24": 345, "25": 360, "26": 372, "27": 384, "28": 397, "29": 410, "30": 424, "31": 435, "32": 450, "33": 465, "34": 481, "35": 493, "36": 507, "37": 519, "38": 531, "39": 542, "40": 556, "41": 570, "42": 583, "43": 595, "44": 610, "45": 623, "46": 633, "47": 647, "48": 660, "49": 677, "50": 692, "51": 706, "52": 716, "53": 730, "54": 744, "55": 755, "56": 771, "57": 786, "58": 808, "59": 822, "60": 833, "61": 847, "62": 862, "63": 873, "64": 887, "65": 900, "66": 913, "67": 928, "68": 942, "69": 956, "70": 968, "71": 979, "72": 993, "73": 1002}
---

**Dave Jones:** Hi, quite often in product design, product manufacture, production, repair, you might have to upgrade things in the field, you might find a fault in your product after you released it, or you might want to upgrade its performance, you want to make some changes, things

**Dave Jones:** like that. There's plenty of reasons why you might actually want to modify an existing populated PCB. Not always can you just re-spin the board as it's called, re-lay it out to add a new component, add a different component, something like

**Dave Jones:** that. This is actually very common in the industry, and I've actually worked in large companies, uh defense companies in particular, where they'll actually have specific component obsolescence engineers, where you have to maintain this military equipment, very expensive equipment, existing boards out there

**Dave Jones:** that have already been manufactured, you want to do upgrades to them, or a component becomes obsolete, for example, and you have to replace it, but you can't just re-spin the board and re-manufacture these things. The boards cost can cost, you know, tens of

**Dave Jones:** thousands of dollars in many cases, and you just don't want to re-spin those, or they're fitted to existing equipment, they've already been qualified and stuff like that. You just want to make a small little change or upgrade, or replace a

**Dave Jones:** component to a different package, for example, very common that components in certain packages go obsolete over years, or they might discontinue some sort of a programmable part, you have to replace it with another programmable part that only comes in a different footprint, and

**Dave Jones:** things like that. So, you want to actually upgrade these boards. How do you do it? So, I thought we'd take a look at it, because let's take this board as an example. It's a ridiculously complicated board, and would be

**Dave Jones:** seriously expensive to actually, um, not only, manufacture the board from scratch, but if you've got a big stock of these blank PCBs, for example, just a blank PCB can be seriously expensive. So, often it makes economic sense to do

**Dave Jones:** what's called a a mod board, a daughter board. There might be many other different names for it. Let us know in the comments if you work at companies that call it different things, but we'll just call it a mod board. So, it makes

**Dave Jones:** sense just to modify these boards with a little mod board. And of course, you might have to modify boards of any complexity just to attest that your new modification works. So, typically you'll, you know, you'll hand solder that. There'll be little mod wires going

**Dave Jones:** everywhere. It'll be really ugly, but you don't necessarily want to do that in a production environment. You know, if you've got a thousand boards you're manufacturing a new production, 10,000, 100,000, or if you've got boards out in the field, you don't want to the repair

**Dave Jones:** techs to go out there and have to put in mod wires, cut and strip wires, and individual parts, and bend them over, and put electrical tape in there, and just all sorts of dodgy stuff like that. So, you want to do a nice simple mod

**Dave Jones:** board, like a professional solution for modifying a doesn't have to be this complex. Even relatively cheap and simple boards, they can be lots of economical or other sort of logistical issues why it's better to actually do a mod board. So, I think

**Dave Jones:** it's an important skill to have. Not only know that mod boards like this, and this is a very simple example, but even more complicated ones, like you might be familiar, for example, if you're into like gaming consoles, a lot of those

**Dave Jones:** illegal mod boards and things like that you can buy. A lot of people fitted them themselves. So, you buy them as a kit. They might come on a little board that's sort of, you know, a weird-looking board that's convoluted shape or whatever to

**Dave Jones:** fit around existing components. That's a classic example of a mod board to an existing product that really there was no other choice to do it. and you want a professional solution that's easy to use so that people can install it. They

**Dave Jones:** don't want to have to run wires and strip wires everywhere. It's better if it's a professional solution on a board, something like this. So, it's really important to know that A, you can do this sort of thing and that this is a

**Dave Jones:** professional solution. So, a really important topic. I've actually got a mod board here, which we'll take a look at. And this is for the 121GW multimeter. We upgrade one of the parts in it. So, I thought, "Yeah, this is a good excuse to do a

**Dave Jones:** video on this." So, we'll take a quick look at this and maybe another example of a production mod to a real expensive bit of gear. Let's go. Now, here's an example of a mod board on a real expensive board. This is from one of the

**Dave Jones:** Lecroy oscilloscopes. You remember I did a couple of videos trying to repair this thing, but it was unfortunately BR, beyond economical repair. And can you spot spot the mod board? Where's Wally? There's somewhere. If you're watching in 4K, I'm sure you

**Dave Jones:** can spot it. Yep, there it is down there, right on the front end like that. You can see they've got this board with a whole bunch of components and they've even like double stacked the melts. You know I'm a melt fanboy. So,

**Dave Jones:** I'm really excited about the melts double stacking there. But a little mod board that they've obviously put on this board. Now, whether or not this was done at the production stage or whether or not it was like an upgrade or

**Dave Jones:** you know, something like that or they released it and they found an issue out there and they wanted to you know, fix it or whatever. If you do know the details of this particular mod, then please leave it down below. But

**Dave Jones:** anyway, fact is that they have actually modded that front end. You can see that they've got a little board here, obviously snapped off from a panel, which we'll go into detail a minute and also we'll go into detail of of little

**Dave Jones:** uh on the side here of the board where they've actually soldered it down to uh like existing components. You see they've already got an existing component there. They just soldered that over. And here's the blank space where it actually uh went. And uh this

**Dave Jones:** wouldn't have been uh designed at the production stage cuz if they were laying out this board and and clearing that space in there, um they would have just put the parts in there. So, obviously post-production kind of thing or some

**Dave Jones:** sort of upgrade or something like that cuz this is a real huge expensive board. And as I said, even if you got the blank board stock can be very expensive, but let alone a populated board. You don't want to scrap a populated board. Uh

**Dave Jones:** it can cost thousands and thousands of dollars. Or even as I said, some of the stuff I've worked on, many tens of thousands of dollars. Um even into the six-digit category for a board is not unheard of. So, they obviously like got

**Dave Jones:** a little bit lucky because if there was some space available, they can always put it on top of the components really. And the fact that it was a square board, um that fitted in there quite nicely. So, yeah, um sometimes you get lucky.

**Dave Jones:** Other times as I said, you know, if you need to connect, say, you know, this spot here over to like over to here, you might need some convoluted board that sort of runs around this chip here cuz it's got this uh tie down uh point here.

**Dave Jones:** So, you might need, you know, and you don't want to you want access to the pots. So, you might have to do some weird thing. You might even have to do some flex uh solution or something like that. But, yeah, you can see how you

**Dave Jones:** just tie a mod board into existing components like that. It's nice and simple, professional, and it allows uh repair techs in the field to actually upgrade these things, which is important, or just easily solder them down in production. Or as we'll see in a

**Dave Jones:** minute, actually uh treating them as a pick-and-place component and reflow soldering them. So, here's an example of a mod board uh panel. In this case, it's for the 121GW multimeter where we wanted to upgrade an existing uh part on a some

**Dave Jones:** already populated boards. So, it it was an SMB part that we upgraded to two 23 parts like this. So, how do you do it? Well, let's take a look at the details cuz this is just one example. There's many ways to do it, but there's

**Dave Jones:** lots of issues which go into making a board like this. Unfortunately, this is not the full panel. As you can see, it's been broken off here and as you can tell by the fiducial marks up here and the

**Dave Jones:** rounded and the tooling holes here, the panel is actually this width here. It's not hugely big, but it obviously extended down here like this. And this is how you want to do it. You want to manufacture these in panels like this

**Dave Jones:** with either break-off tabs or V-scoring or something like that so you can easily cut them out at a later stage. Cuz the last thing you want to do is get a tiny little board like that and give that to

**Dave Jones:** your pick and place assembler and go, "Assemble that board, please." They'll just roll their eyes and charge you a fortune and probably just end up hand-soldering anyway. So, how do you make a nice panel like this one? Well,

**Dave Jones:** I've done a whole panelization video, which is very popular. I'll link that in at the end and down below if you haven't seen that. Highly recommended. Lots of detail on how to do routing and V-scoring. And that's what

**Dave Jones:** we've got here. We've got a combination of routing and V-scoring. So, let's have a look. You can see that obviously they've got they've routed out this board like you didn't have to add this little like chamfer in here like this.

**Dave Jones:** It's not necessarily important to do that. They've just decided to do that. No problems whatsoever. But anyway, you just route like that like a 2.4 mm routing tool might be like a standard diameter. As I said, look at that

**Dave Jones:** panelization video I've done. And we've got a combination of V-scoring like that. And I'll show you up close. But as per regular panels, of course, you want your fiducial uh alignment marks. You want your tooling holes on your outer

**Dave Jones:** strip like this so that it can go through the conveyor machine in the pick and place. So, they'll have a rail up here and another rail down here, and your board passes through the passes into the pick and place machine, gets

**Dave Jones:** picked and placed, and then it goes out on those rails out in a via these tooling holes, which move it along, and it goes out to the reflow oven. So, you want to automate that sort of process. Now, you can see that all the copper

**Dave Jones:** fill has been left on here. It's not on the bottom of the board because we don't actually want copper underneath here. There's just no reason to have it, but like there's been copper in fill like this, just floating copper like that.

**Dave Jones:** The reason to do that is just so it's nice for the PCB manufacturer so that they don't have to etch away all the copper. So, you might as well just leave the you know, leave the copper on there

**Dave Jones:** to make the etching nice and easy. We've got a combination of routing slots, V grooving top and bottom, or V scoring as it's called going across the panel here. You might be able to see the detail in there. I'll show you in a sec. And also,

**Dave Jones:** we've actually got what's what are called castellations or half-moon pads going right across the scoring here. That not only allows for the boards to be individually snapped and cut out of the panel easily, but then it allows you

**Dave Jones:** to actually solder these down as a surface mount component. Because as I said, in this case, this little mod board here is actually replacing an SMB footprint part with two in this case, two SOT-23 transistors. Now, you can

**Dave Jones:** make this panel as large as you want, of course, subject to your assembler and how it fits in their machine and whatnot. Now, this is a 0.8 mm PCB, so that's pretty thin. There's no real need to have it uh 0.8 mm in this particular

**Dave Jones:** case, but you can see that it's actually going to be quite flexible like that in both directions. You don't want to do it too far in that direction cuz you're going to snap off the uh V-scoring uh along those boards. But uh the

**Dave Jones:** problem is is that if you have one big panel like this and you stick it in your pick and place machine and it's only held with the rails at the top and bottom, when you put it in like this and

**Dave Jones:** the pick and place head comes down to place parts, whoops, it's going to it's going to warp in the middle like that. So, uh boards like this um it's quite common for your assembler to actually uh manufacture a custom uh tray that

**Dave Jones:** actually this board just sits snugly inside the tray and it's fully supported over the entire area like that. So, yeah, but but your manufacturer will um advise on that sort of stuff and um often just handle that for you. They

**Dave Jones:** might do that without even telling you. You'd just say, "Assemble my panel, please." and they'll go, "Okay." And they'll have like as part of the tooling charge will be manufacturing a uh holder for this particular board. Now, you can

**Dave Jones:** see the V-grooving across there. This isn't a particularly deep V-groove. If you have a look down there, it's uh in fact, bottom seems to have a different depth. I wonder if that's actually uh consistent across the board. Yeah, it seems to be.

**Dave Jones:** I think they've got possibly a uh sharper V-groove on the bottom. Did I'm not sure if that's on purpose or whether or not that's just the way that the you know, tolerancing how the uh the machine the V-groove wheel was actually uh set on

**Dave Jones:** the thing. And there's the bottom of the board and this V-grooving needs to be controlled, you know, fairly accurately at the factory, especially for a like a 0.8 mm uh PCB like this one. The thinner your PCB gets, the uh you know, the more

**Dave Jones:** critical your tolerance gets on that uh V-groove cutting wheel. But, in either case, there's more than enough uh fiberglass left in there to hold this uh board together during that handling and whatnot, but it allows easy snap-off. So, as you can see, when you snap it

**Dave Jones:** off, you might be left with a few dags and things like that in there, but uh this is fairly common. It's not generally going to be an issue. So, you're left with a half-moon castellation like that, and which allows

**Dave Jones:** you to just easily solder that onto a like existing pads onto the board. And then, when you snap it off, you're left with a tiny little uh board like that, and you can see that how that is basically becomes a little uh

**Dave Jones:** surface-mount component. There's other ways you can do the uh castellations and uh you know, stuff like that if you really want to get all fancy-pantsy about it, but you know, those half-moon castellations work well. Then, you simply solder that as a component. In

**Dave Jones:** this case, you would hand-solder it, but you could actually reflow it, but because this is a retrofit, generally a retrofit to an existing uh board, although it doesn't have to be if it's a like an obsolescence uh component

**Dave Jones:** replacement or something like that, you can actually get this actually placed by the pick-and-place machine and reflow it. But, of course, like you wouldn't have it on any um production reel or production tape or anything like that. So, you might put it may maybe you might

**Dave Jones:** do it if you're like really keen, you might do a a specialized uh production tray for it or something like that that held it uh as a tray-based component in the pick-and-place machine, which could then uh pick it up just, you know, using

**Dave Jones:** your existing nozzles onto the existing uh component, and then lift it onto the board, and actually place it and have it reflowed. And of course, this is a real simple example. There's only uh two transistors in there replacing a single

**Dave Jones:** uh surface-mount part, but like you can make these as weird and wonderful and convoluted as you like. That could like spread out over in entire board. You can even do this as a flex circuit as well. But the problem with a flex board is

**Dave Jones:** that you don't get the same kind of castellation hole on the end that you would on a fiberglass PCB like this. But yeah, you can have pads either on the top or bottom or whatnot and then just start solder bridge those

**Dave Jones:** on. No problems whatsoever. Both are valid techniques. So in this particular case, we wanted to do replace an SMB component with two SOT-23 parts. As you can see, doesn't quite fit on there. You could sort of like stagger

**Dave Jones:** them a little bit. So like this one went behind there if you had the width like this which we didn't really have. But because we actually had two of them there and had an adjacent pad. Sorry, you can't see under there, but normally

**Dave Jones:** there's a pad there and a pad there. Then we can just have it going from that pad to that pad. No problems whatsoever. And this is just a real simple example. But it gets the point across. So it's

**Dave Jones:** just real neat and tidy and it simply becomes just it looks like yet another part. In fact, you know, if you zoom out of this like you you're really like hard pressed to tell that you know, that's actually a mod board in there really. So

**Dave Jones:** I hope you found that video useful and if you did, please give it a big thumb up. And as always, you can discuss down below or over in the EV blog forum. And if you like my content, you can always

**Dave Jones:** support me on Patreon. Links down below and I accept cryptocurrency donation or what sort of jazz. And as much on my store. You know the deal. Catch you next time.
