---
video_id: Uemr8xaxcw0
title: EEVblog #239 - PCB Design For Manufacture Part 2
url: https://www.youtube.com/watch?v=Uemr8xaxcw0
source: youtube-asr
---

**Dave Jones:** Hi, as you know, my little microcurrent project has been very popular lately and I need to get some more manufactured because you know, there's been a pretty big demand for them and I've been selling this for quite a few years now

**Dave Jones:** and I've only got them made in small batches. I never originally designed this for high volume manufacture at all. So I've just been making you know, 50 was my first batch and then well, I made another 50, another 50 little small

**Dave Jones:** batches of of 50 or thereabouts, but I wanted I thought no, it's just not the right way to do it. I'm now actually selling quite a few of these things. So I thought might as well do it properly and rejig this thing

**Dave Jones:** for a bit more friendly for high volume manufacture. Now, I've done a whole video on this. It's DFM, what's called design for manufacturing and there's a link up here. So click on this if you haven't seen the previous video. It's a

**Dave Jones:** long one. Goes into all detail about how to panelize stuff for production and things like that, but that's all it was talk. I didn't actually give you a real world design example. So I thought I'd do just that.

**Dave Jones:** I'm going to rejig this thing for production. I'll make it more friendly for machine assembly and I thought I'd just actually show you what goes into that. It's not that hard, but should be interesting. So stick around. So here's

**Dave Jones:** the microcurrent as a bare board unit over here as a fully assembled PCB when I get it back from the manufacturer. This is what it looks like and this is the finished product tested and ready to ship. Now, let's take a look at what's

**Dave Jones:** involved with actually panelizing this as opposed to a loose version. Now, as you can see the PCB is designed into fit into this uh Jiffy box here and it's designed uh as a front panel. So, the appearance of these uh

**Dave Jones:** outside edges here is actually uh quite important in this particular product. So, you have to put a bit of thought into how you actually uh panelize this actual design because um currently, I get it manufactured like this. I get it

**Dave Jones:** manufactured from a company in China called PCBWay, but uh I'm going to drop them. I'm going to try and get it um locally manufactured or manufactured somewhere other than China. So, I'm going to give that a go um just to

**Dave Jones:** locally source it. Now, uh this is when you lay out the board in your uh CAD software, as we'll see later, it's just an individual board like this or what's called a loose board from the manufacturer. When you uh send

**Dave Jones:** your Gerber files away to be manufactured, you uh specify them either you want them panelized or you want them loose, supplied loose like this. And the way they do it is they will route these edges. They will They will actually

**Dave Jones:** panelize this on a larger board, but then they will actually uh route it out with a drill, and you'll get a beautifully finished board with a nice smooth routed edge, beautifully sharp corners on it, and it just looks really

**Dave Jones:** nice for a front panel. And that's great, but it's not very suitable for high-volume manufacture because if you've just got a single PCB like this, then uh when you stick it in a pick and place machine, especially one this

**Dave Jones:** small, then you're not full fully utilizing uh the available uh the available time on that pick and place machine cuz it can only pick and place one individual board, and then it's going to move through So, it moves through the

**Dave Jones:** conveyor belt like this under the pick and place machine. Pick and place machine's loaded. It loads all the components for one board, and boom, off it goes. And really, that is no good if you're just assembling one of these at a

**Dave Jones:** time because you've got it comes in and it places all the parts and goes through the reflow oven, and then it's just got to reflow that one individual board. And this board doesn't have any outside tooling strips around the outside of the

**Dave Jones:** board, as we'll see later, so that it can automatically get inserted and moved along the conveyor belt. Typically, if you get a loose board like this, they might have to design a like a custom jig for it where the board just sits in. It

**Dave Jones:** could be made of wood or you know, ABS or something else, but it's like a carrier board that sits in there and takes the board along. So, you're not using your pick and place machine very efficiently if you're just getting one

**Dave Jones:** board made at a time. So, what we want is to get multiple boards made at a time, let's say 10 at a time, and then you're really utilizing the time available on that pick and place machine. Because during high-volume

**Dave Jones:** assembly, what you'll pay for is you'll pay for the setup of the machine. You'll pay a fixed setup cost typically, and then you'll pay for the machine time itself, or how long that machine takes to assemble your particular board.

**Dave Jones:** That's in general. It It varies by the assembler, but generally, that's how it's going to work. So, if you can do 10 boards at once instead of one, you're going to go through that machine much quicker, and your assembly cost is going

**Dave Jones:** to be cheaper per board. Now, here's an example of a typical PCB manufacturing panel. It's exactly the same board, but it's duplicating this time In this case, three three vertical by four horizontal, 12 boards total. So, in the one

**Dave Jones:** manufacturing pass, you can do 12 boards at once. It's roughly an A4 size sheet, which is any good assembly machine should be able to handle that. If you want to go much larger than that, talk to your assembler first because you

**Dave Jones:** don't want to goof it up, manufacture this huge panel trying to fit 100 boards on there and oops, it doesn't fit into their automated machines. So, just check first, but A4 size like this generally pretty good. So, we want to get say

**Dave Jones:** multiple versions of this microcurrent on a panel like this. So, we should be able to fit say five across by two like that. So, 10 boards, that will be our aim, nice round number. I like it. Now, the other thing you have to consider is

**Dave Jones:** how you actually attach the board to the panel. You can, of course, just copy and paste your Gerber on there and get it manufactured as one big solid board, but that's pretty useless cuz then you'd have to have access to some sort of

**Dave Jones:** routing machine that could cut the board out after it's assembled and that's a pain in the butt. So, what you want to do is when you panelize a board like this, you want to add some routing paths like this and some little tab

**Dave Jones:** attachments in there to put the board in or you want to do what's called V-grooving which in this case, say this particular panel here, there's these score marks down the side and you can just snap the boards off. And, of

**Dave Jones:** course, you can actually do a combination of routing like this or a V-grooving like as an example on this board here. It's got one routing bit along here, one routing path along there to get. The reason you're putting a

**Dave Jones:** routing path instead of a V-grooving is to get a nice smooth edge like I talked about. You want a nice smooth edge. If you want a nice smooth edge say on this side for some particular reason because it's visible inside your product, then

**Dave Jones:** you would route it out like that. But, if you don't care about the other edges, then you just put specify V-grooving which puts a score mark in there and then you can come along later and then just snap this board out. Now, of

**Dave Jones:** course, if I I the microcurrent board like this with these little tabs in there that you have to cut out with the sear pair of side cutters afterwards and it typically leaves a really ugly looking dag on on the corner like that

**Dave Jones:** or you can put them in the middle like here if you want but that's even uglier cuz you got to put in a little sort of bit of cut out in there and I won't go into details but when you cut out it

**Dave Jones:** looks ugly and that's okay if your board's inside your product and people aren't going to see it but when it's actually a front panel like this then the edges can actually be quite important the visible edges like that.

**Dave Jones:** So ideally we want as much as these edges routed as much as possible. So for this microcurrent I figure that these longer edges here are you know quite prominent and visible so I would prefer to have those edges down there fully

**Dave Jones:** routed so they're nice and smooth and then just say V groove the top like that because I don't want daggy edges in there with the tabs. I think I'll rule out tabs completely and I'll go with just a routing path down the side of the

**Dave Jones:** board like this the long side and then the top side I will do V grooving like that just like on this particular board here I've done V grooving uh sorry routing down the side just imagine this is my microcurrent board I want to do

**Dave Jones:** routing down the side like that so I get nice smooth edges and then that V groove that scored V groove mark along the top like that. And as I've explained in the previous video I'll just mention it again there's a bit of an art to

**Dave Jones:** choosing you know how to strengthen these particular tabs and things like that cuz when the pick and place machine comes along and then pushes down your component down onto the board the board can warp particularly if you've got very

**Dave Jones:** thin PCB this is standard 1.6 mm that I'm using here, but you might use a 0.8 mm board or even thinner like that and they're very, very flexible. So, there's a bit of an art which goes into that,

**Dave Jones:** but if you just do V-grooving, V-grooving is you know, usually you know, is really strong enough for almost anything. They've The PCB manufacturers have got the V-grooving down to an art where you know, it just works. You can

**Dave Jones:** easily snap it out, but it's more than strong enough. There's more than enough fibers inside that V-grooving there to actually hold the board in place. No problems at all with a lot of force. And the other thing we're going to want are

**Dave Jones:** tooling strips top and bottom of our board like this so that these and you've got tooling holes like that typically 3.2 mm in diameter would be a typical tooling hole and you want these fiducial marks as well. A fiducial

**Dave Jones:** mark would be a typical 1 mm diameter circle or thereabouts with the solder mask removed around it. So, that's a vision identification alignment point for the pick and place machine. And you want to put those on the outside of the

**Dave Jones:** board and you'll see that the entire panel like this has typically four tooling holes in the corners like that and it will have a usually three fiducial marks like that top and bottom. So, you want them on the bottom side as

**Dave Jones:** well and especially for this microcurrent considering there's no point having fiducial marks on the top side of the board because all my components are mounted on the bottom. So, when they put this machine through when they put this board through the

**Dave Jones:** pick and place machine, it's going to be facing up this way. So, and your camera your fiducial camera is going to be typically on the top here. So, if your fiducial marks on the bottom, that's no good to you. So, you want to make sure

**Dave Jones:** your fiducial mark is on the side of the board that your components are. Don't get confused. Now, as you can see, there really aren't a lot of components on this board, so you can argue that well, you know, I can if I'm only making you

**Dave Jones:** know, 50 or 100 or maybe even 200, you could actually hand assemble these and I do actually currently get these hand assembled by a guy in Melbourne. Uh his name's Vultronics. So um and he just hand assembles these individual boards

**Dave Jones:** and that's okay for a run of 50 because when you're doing machine pick and place assembly, you're going to pay quite a larger setup cost actually tool up for that and as we'll talk about in a minute, you've got

**Dave Jones:** to buy reels of components instead of individual ones. So if you're only going to get 50 of some board manufactured, it's really not worth panelizing them. But now I think I'm going to go to the trouble to do it cuz that's

**Dave Jones:** professional. It's the proper way to do it and if I sell more of these in the future, it's going to be better. Might be a bit of upfront cost now to get it set up and panelized. I can loose the

**Dave Jones:** components in terms of like I might have to buy 500 of one component even though I'm going to make 100 boards, but in the end hopefully if I sell enough, I should recoup the cost and it should be lower cost to get this

**Dave Jones:** machine assembled instead of hand assembled. And of course the other thing to watch out for is how many different types of components you got on the board. Thankfully, this is only a very simple board. As you can see there's

**Dave Jones:** only three ICs, there's 12 you know, dozen resistors or so, three caps, you know, a couple of ICs and this surface mount battery battery connector and that's about it. So uh really I'm not going to even if these all the resistors were all

**Dave Jones:** different values, I'm not going to exceed the maximum number of reels available on the machine because um I don't want my board to have to go through the pick and place machine twice. Let's say the pick and place

**Dave Jones:** machine at your particular assembler only supports 20 different reels of components. That means well, you're limited to having a maximum of 20 different types of components, not 20 components total, but different types on your particular design. So, um if you've

**Dave Jones:** got more than that what your assembler is capable of, you may have to rejig your design and consolidate some of your components. Like uh you might go around and consolidate some of your resistor values or something like that so that

**Dave Jones:** you can actually um get this board in a single run through the pick and place machine because that will be cheaper. So, what happens at the moment? Well, I order 50 loose PCBs like this from uh PCB cart in China. They're

**Dave Jones:** very cheap. I get 50 of these. Then I order 50 of all my required components from Digi-Key and they come all loose like this and you know these there's the battery connector. It comes in a non-machine-friendly uh you know thing like this holder like

**Dave Jones:** this and really you can't put this into an automated pick and place machine and and place the damn things. They're only good for hand soldering. And each individual component comes in the individual little bags like that. They're cut off from the reel. As you

**Dave Jones:** can see, they're just chopped off like that. And they're that's only good for hand solder. So, my assembler, Vultronics, he's got to sit there and take them all out of their individual things and place them down with tweezers

**Dave Jones:** and solder them. And does a pretty good job and does it really quick, which is excellent. But that's really only good for low volume stuff. If you when you start talking 100 or 200 or more like 1,000 boards, perhaps not that I'm going

**Dave Jones:** to make 1,000, but a couple of 100 of these things, then you really want to look into uh pick and place, actually buying your components that are machine-friendly. If you went to a machine assembler, even if you've got your lovely panelized board like

**Dave Jones:** this, you send them your lovely you know you've done all the work to panelize the thing and you send them a bunch of parts like this, they're going to laugh at you. Uh well, secretly laugh at you behind their back because then they're

**Dave Jones:** going to have to take all these out and then individually um individually wind these onto their own reels, and they'll charge you a fortune for that, an absolute fortune. So, what we want to do is we don't want to buy

**Dave Jones:** them loose like this. Forget that, that's hopeless. So, we want to ditch all that rubbish, and we only want things on reels or in uh tubes of components. Usually, the manufacturers prefer reels like this. They don't uh in

**Dave Jones:** particular like uh tubes anymore. They're not as good or trays of components. So, really, say these um uh surface mount battery holders, you can actually get them in uh trays, and they supply them as one big tray like that,

**Dave Jones:** and they can sort of load those into some pick and place machines and pick them from trays, but not nearly as good as buying them on a reel. So, you can actually buy these on a reel like this.

**Dave Jones:** It's a really thick reel like that. It's going to be about that thick, and it might have, say, 500 of these on the one particular reel, and they can load those in to their pick and place machine on

**Dave Jones:** their reels like this. It might hold 20, 30, or 50 reels of components, and bingo, the tape goes into the machine like this, and it actually uh assembles those really quickly and really efficiently with the minimum amount of

**Dave Jones:** handling. So, every single component, I've got to go through my bill of materials, I've got to go back to Digi-Key, and I've got to look at buying each part on a reel. Now, if you're buying a capacitor or a resistor, uh you

**Dave Jones:** know, 0.1 cents each, they're really cheap. You buy a reel like this, it's only 10, 15, 20 bucks, not a problem. Even if you only want to make a couple hundred boards, you can waste you can afford to waste a couple of thousand uh,

**Dave Jones:** components. Because each reel might have four or five thousand resistors or four or five thousand capacitors on it. That's not a problem, but some of the ICs, um, uh, could be, uh, quite expensive. So, uh, companies like, uh, Digi-Key and

**Dave Jones:** Mouser, they offer a re-reeling service. So, instead of buying a full reel, and let's say I've got to buy the, uh, the Max, um, IC on here. Very, you know, it's the most expensive part on the board. It's like a dollar or a dollar

**Dave Jones:** fifty or something like that. You don't want to buy a couple of thousand of them on a reel like this, a full reel, what's called a full reel, if you only want to make a couple of hundred boards. That's

**Dave Jones:** so you can actually, um, this isn't This is a reasonable example of what you'll get. It's actually a mini reel. Um, it's a brand name. I think this is a Farnell one, but the Digi-Key one, or this comes

**Dave Jones:** from the manufacturer, actually. But, Digi-Key, they'll offer a re-reeling service where they take all of these components off a larger reel, and they put it onto a smaller reel. So, if you only want 200, they'll take 200 off this reel like this, and

**Dave Jones:** they'll rewind it onto a smaller reel, and you only have to pay for those 200 parts, plus, like, you might pay eight or ten dollars for, uh, a a re-reeling fee, but that's okay. Then you don't get a huge amount of wastage. But, once

**Dave Jones:** you've got these, you can ship those to your, uh, uh, PCB assembler, and they'll be happy as Larry that you've given them all the components perfectly on reel like this, and they'll love you, and they won't charge you a premium. Now, the other

**Dave Jones:** thing is, uh, you will lose some of the components off these reels. So, don't go giving your manufacturer exactly the right amount of components that they need. If you're getting 200 boards manufactured, do not go and give them

**Dave Jones:** exactly 200 devices on this reel. Make sure you have some extra because they will actually lose some components and they have to add some leader tape on there as well. So they they will actually add some tape on top of that,

**Dave Jones:** some extra length so that it can actually be fed into their machine wound on first before it gets to the components. But if your components start right here, they can't just stick that into their machine cuz it's going to get

**Dave Jones:** wound through and you're going to waste the first you know 50 components or something like that. So it's very common. So you have to have some overrun on your reels. Just make sure you order you know 10% more or you know 50 components more

**Dave Jones:** for resistors or capacitors or something like that. Don't do an exact number. And of course unfortunately the microcurrent board isn't all surface mount. It's got a couple of through-hole switches on the top here plus these binding posts and

**Dave Jones:** these 4 mm banana plugs here and they still have to be hand soldered. So um really you know there's they could actually selectively wave solder these switches but I doubt they would actually go to the effort to really do that. So

**Dave Jones:** considering they have to hand solder other stuff, they'll hand solder those switches as well. So you got to factor that into the cost you'll pay you know a fair bit extra for that individual hand solder process but hopefully we should

**Dave Jones:** be able to save um quite a bit of cost even even if we manufacture a couple hundred of these boards, should be able to save enough cost to compensate for the fact that we're going to have to hand solder a few

**Dave Jones:** extras but I think we can save some money. Maybe the you know the price benefit might start at maybe 100 boards or 200 but after that it would really kick in to play and save you a big cost.

**Dave Jones:** And also with machine assembly of the components there's less chance of it going wrong and your soldering quality is going to be more consistent as well. Not that my hand solder of Vutronix does a bad job. Does an excellent job in fact. And of course

**Dave Jones:** the other thing that the manufacturer is going to charge you for unless you supply it yourself. I wouldn't recommend you supply it yourself. Usually you leave it up to the manufacturer is the solder paste stencil and that will be

**Dave Jones:** usually a stainless steel one for high volume manufacture with all the cutouts of all the pads so that they can apply the solder paste on there and that might be absorbed into the setup fee or something like that or they

**Dave Jones:** could even charge you extra for that. But once again, that's only a one-off cost for that stainless steel stencil. And they do wear out. So if you're manufacturing a million boards or something, you know, they're eventually going to wear out. But when you're, you

**Dave Jones:** know, assembling this sort of quantities I'm after the hundreds or even the thousands, you know, it's really not going to be a problem. So just leave it up to the manufacturer. All right, so let's actually take a look at how we do

**Dave Jones:** this in the PCB package. Now before anyone asks, this is Altium Designer, okay? Don't ask how to do it in any other package because well, that's up to you to figure out, okay? This is just how I'm going to do it in Altium

**Dave Jones:** Designer. Now this is my existing micro current board and I've actually tweaked the I've taken the opportunity to tweak the uh silk screen on the front here. I've increased the size of the micro current font, added EEVblog there cuz this

**Dave Jones:** design was from before I was actually started the EEVblog. So I didn't put it on there. But I thought I'd just take the opportunity seeing as that I am actually paying for a retooling of this PCB because I used to get it supplied in

**Dave Jones:** this individual thing like this. So you have to which means if I want to panelize it, I'm going to have to pay a new uh tooling charge. So, you may as well add in any other changes. There's no circuit changes, so I'm happy with

**Dave Jones:** that. I'm just going to change this silk screen on the front. So, this is how I supplied the board uh previously is just the Gerbers for this one individual file. And if we actually go in there and we can actually generate

**Dave Jones:** the uh Gerbers for those now. Let's actually do that. As I I won't go into inches and millimeters and all that sort of stuff. Let's just generate the Gerbers, shall we? And uh have a look at bang! There it is. There's the Gerbers.

**Dave Jones:** And if we take a look here, we can actually see the individual uh Gerber layers like that. That's the bottom layer, hence GBL. That's the bottom overlay like that, the bottom solder mask, the bottom mechanical layer. As you can see, I define the outline of my

**Dave Jones:** board. Actually, don't worry about the switches. That was just part of a model for that component, but I define the outline of my board based on a separate mechanical layer. So, when the manufacturer imports all of these uh

**Dave Jones:** layers, they will all match up and overlay, and they know exactly, because they're based on the same origin down in the uh bottom corner down here, they will know that uh that is the dimensions of my board that I want. And because I

**Dave Jones:** haven't specified any panel information or anything else, they're just going to supply that board loose. Like um uh just uh like we talked about. So, there's the overlay. So, let's actually look at getting this thing panelized. So, in my

**Dave Jones:** project here over the left-hand side, what I've got is my schematic, of course, and then I've got my individual PCB here. I've generated this that's exactly the same as before, but then I've created a new uh PCB inside this um

**Dave Jones:** PCB thing. And this is inside my PCB project. And there is my completed panel. I've already done it, of course. Here's one I prepared earlier, and I'll go through the steps and explain exactly what I've done here. Okay, so the first

**Dave Jones:** thing you want going to want to do is just create a blank panel size that's big enough for the amount of boards that you want. In the case of the micro current, it's 79 mm high by 50 mm wide.

**Dave Jones:** That's the individual board. So, I can calculate, simple math, how big my panel needs to be, but you can tweak it like that. You can drag the corners in and tweak the sizes, but you create a blank panel like that, and then you start

**Dave Jones:** laying down your individual PCBs into the panel board. Now, of course, the old-school way to do this is just to cut and paste your entire board. So, you go into your individual board, and then you actually uh make sure all of the layers

**Dave Jones:** you want are actually selected, that they're all there. You can go used all on or whatever. So, all your layers are there, and you can just highlight everything or select all, and then you just copy it. Make sure you choose the

**Dave Jones:** bottom uh corner down here, for example, and then bang, I've copied that, and I go into my panel, and I can then paste in my individual board. And you can see the actual size of it there, and bang, you

**Dave Jones:** can paste there, rebuild the polygons. You typically do not want to rebuild your polygons, and then you can paste individual boards. You can actually go in there and make sure set your default grid and things like that just to make

**Dave Jones:** sure that you actually get it um accurate like that. But that's really um that's really the old-school way to do it. And you've got to be careful that um it doesn't duplicate, uh for example, doesn't duplicate your silkscreen

**Dave Jones:** designators and things like that. Some packages will automatically, see, it has. Altium Designer, if we go in here, see that uh it's back to front mirror image there, but if we go in, see it's actually relabeled those silk screens.

**Dave Jones:** That's just the individual component designators. It's relabeled those. So, that's a bit of a trap for young players when you're doing it manual like this. There is an option somewhere in Altium Designer to disable that sort of thing.

**Dave Jones:** It's increment designators on paste or something like that. But, uh um so, some packages without a penalization feature, you are going to have to do it manually like that. But, thankfully, Altium Designer has a penalization feature, so we're going to

**Dave Jones:** use that instead. So, let's use this penalization feature. So, let's go into uh uh place and then embedded board array panelize like this. And you can set up your uh individual distances between boards. Now, I know my board is uh you

**Dave Jones:** know, I can actually tweak these uh figures later, but it's 55 mm um in the X direction to the next board and then 90 mm vertical to the board after that. And then you can specify which uh PCB

**Dave Jones:** file you want want. In this case, we've only got one, which is the microcurrent. The the column count, the row count, and bingo, if we do that, look what we've got. We've instantly got our panel there, which we can place on our board.

**Dave Jones:** And what that does is it actually it it really it doesn't actually place the individual tracks um on that board. Is that a bug? There, that's some sort of bug in Altium Designer. What a load of crap. Anyway, um

**Dave Jones:** it doesn't actually place down the actual tracks and the silk screen and everything else. It just place places down the information placement information for them, so that when you generate the Gerber files later, it will actually generate the full panel, which

**Dave Jones:** is really quite a neat way to do it. I like it, but there you go. That's how easy it was. Okay, so what we've got now, we've actually placed our individual border ray like this and I've set the

**Dave Jones:** dimensions, the distance between one board and the next to be precisely 2.4 mm wider than than the board itself. So that width in there is 2.4 mm wide. I've done that is because 2.4 mm is a standard routing

**Dave Jones:** bit width. So what the manufacturer can do is just route out bang that um they can route out that slot straight up there with one pass of the routing bit. They can route any size you want. But they you know, it's just nice if they

**Dave Jones:** can do it just in one routing path like that. So that's what I'm going to do. So we'll have to specify the routing path later, but basically as you can see, I've created my panel there. Now let's take a

**Dave Jones:** look at that in the 3D mode like this and bang, there it is. There's my actual board and if we uh we can actually play around with that and uh there we go. That's what our board is actually going to look like well our

**Dave Jones:** final panel is going to look like as opposed to our individual board. And as you can see, there's no because it's not easy to show the routed slots on here. You have to use your imagination a bit. But what we've done there is we've

**Dave Jones:** created one big panel with 10 individual microcurrent boards. Now you know how I said there were no circuit changes? Well, I kind of lied there because there actually are and what they are is let me go down to the bottom layer here. Now in

**Dave Jones:** the previous version of the board, I won't bother opening it, but this blue trace up here was actually much closer to the edge of the board up here and that's usually not a problem if you're actually cleanly routing those boards.

**Dave Jones:** But because we want to V groove the top uh edge and the bottom edge of the board and it was the same down the bottom here as well. This trace was actually down near the bottom of the board down there.

**Dave Jones:** So what we've had to do is peel that back a bit move that trace down a bit so it's so there is some clearance a decent amount of clearance between the top of the board there and I've left about 1

**Dave Jones:** and 1/2 mm I think by looks of that and that should be enough for the V groove to go along because what the V groove or V scoring does is it gets a little drill bit and it goes

**Dave Jones:** and it routes a a groove or a V groove funny that it routes a V groove right along there so you actually cut into some of this board here. So you're also going to cut into some of the solder mask and if you have

**Dave Jones:** traces near the edge of the board it's going to cut into them and it's going to ruin your day. So anyway you're doing V scoring like that just make sure you peel back the copper from the edges especially if you're

**Dave Jones:** doing copper fills and stuff like that like I've done on the top layer here has the copper pour on there or the polygon pour it's a millimeter back from the edge which should be more than enough for the V

**Dave Jones:** scoring. So that's just something that you need to watch out for when you're panelizing boards like this and what we want on the bottom of the board here is a tooling strip top and bottom it needs to be wide

**Dave Jones:** enough to handle you know handle the sliders on the automated machine and I've made it 20 mm thick here and that should be more than enough and I as you can see I've added a 3.2 mm tooling hole

**Dave Jones:** like that and I've added my fiducial here which will be a two-sided fiducial and there's no hole of course and it's a 1 mm size pad there with solder mask expansion on it. So, if we go to 3D mode

**Dave Jones:** there and we actually zoom in on that, you can see that we've got the gold, which is the copper, like that, and the solder mask expanded it expanded around like that. And that will actually be the same on the bottom side as well

**Dave Jones:** on the bottom side as well. There you go. Because all my components are mounted on the bottom, these fiducials really only need to be on the bottom, but put it on the top as well. So, now we have to add in some panelization

**Dave Jones:** information. That's one of the common terms used to specify that we want V-grooving and where we want our routing. So, I've prepared that earlier and here it is. It's just on the mechanical layer. So, if I only show you

**Dave Jones:** the mechanical layer, sorry, I can't get rid of the hide the panel at the moment, but as you can see, I've added in these this routing path here. I've actually done the outline of the routing path. It's 2.4 mm wide and I've just

**Dave Jones:** specified it to go like that. And I've specified There it is. Route out. So, I'm telling the manufacturer, I giving them specific information to route out that particular path there. And I've added in a little pointer here, which says V-grooving, to

**Dave Jones:** which means if it matches up with the one on the other side, it means V-groove or V-score that board all the way along like that. So, the top edge of the board, likewise the bottom edge of the board, and that one, and that one down

**Dave Jones:** there. So, that's all the information that I need to provide on that panel, and the manufacturer will interpret that. They the bare board PCB manufacturer will interpret that and they will know to actually route out the path between the boards and V-score top

**Dave Jones:** and bottom. And if they have any uh questions, then they'll ask you about things like this, but they will actually handle the fine details of then programming those route paths and the V-scoring into their um into their PCB

**Dave Jones:** manufacturing machines and the software to actually do that. So, you don't have to worry about what software they're using or what system they're using to actually do that. They will manually take the information you provide on your mechanical layer here, and and they

**Dave Jones:** their their knowledge and smart enough to know exactly what you mean by V-grooving and routing. And maybe, just to be on the safe side here, we might actually drag out this individual uh thing past a bit past the end of the

**Dave Jones:** board like that, just so you end so that you do actually genuinely get a nice sharp uh corner. So, what we're going to do is we're going to uh just place some lines in there like that, and just

**Dave Jones:** extend it past there so that they know to actually go so that they will tell their drill to actually go all the way past the edge of the board, and you just guarantee that nice clean sharp edge down in there. And there you go, that's

**Dave Jones:** our completed uh panel, and that's really all there is to it. It's not that hard at all. It's not uh much work even if you have to use even if your package requires you to do individual cut and uh

**Dave Jones:** paste instead of having some automated panel function like this, it's it's no drama at all. So, once we're finished with that and we're happy with it, we just generate our uh Gerber files. So, that's uh fabrication outputs. Let's generate

**Dave Jones:** our Gerber files. We're happy, we want those layers. Let yada yada yada, but we're going to have to include, look, the paste layer, okay? Because we GTP here, the top paste layer. And well, actually, we don't need the top paste

**Dave Jones:** layer, but we'll do it anyway, but the bottom paste layer is important cuz that's where all of our components are and I've never had to generate or supply that before when I was getting them hand assembled because there is no solder

**Dave Jones:** paste stainless steel stencil that's used by the machines to actually put the paste down onto the individual pads. But because we're getting this machine assembled designed for manufacture, we have to supply that bottom and top paste overlay or in this case really only the

**Dave Jones:** bottom paste overlay because we've only got components on the bottom. But that's what we want to generate. So let's actually go into that and generate our Gerber's for that and it'll take a bit longer than usual because it's got a

**Dave Jones:** larger panel, but bang, there it is. There's our And if we go into the individual generated files down here, here they are. Microcurrent panel rev two bottom layer. There it is. There's the Gerber information for the entire panelized thing. The bottom overlay.

**Dave Jones:** It's zoomed in there. So but there it is. There's the bottom overlay, the bottom paste. So there's our paste layer that might be hard to see. It's in a hard to see color there, but that's the paste mask that they'll use to generate

**Dave Jones:** the stainless steel stencil for the paste and the solder paste will only go into those particular areas on the pads. So and there won't be any solder anywhere else on the board. So that's how they get the reflow soldering process.

**Dave Jones:** They'll put the They'll use a stencil, apply the paste which applies solder paste to the pads. They'll then pick and place the components and it goes into the reflow oven and the solder melts and bingo, magic happens and you get your

**Dave Jones:** board. And there's our solder mask and there's our mechanical layer with all of our uh, and uh, information. There it is. We've got our V-groove, we've got our routing paths, and the manufacturer should know that we want that size board, the outer size

**Dave Jones:** board manufactured, and the V-grooving and the routing. And it's all there for them. And then we've got the top layer, of course, and uh, top overlay. Let's have a look at that. That's got lots of information. It takes a while to load

**Dave Jones:** because it renders because Gerbers actually render um, all these things as um, individual uh, tracks. So, it's, you know, they don't actually render uh, fonts. So, that's how Gerbers actually work. And top paste layer, as you can see, I've got no components there, so

**Dave Jones:** there is no top paste layer. It just It generated it, but it's blank. And that's uh, what we have to send to our um, PCB manufacturer. Actually, we don't have to send the paste layer to the manufacturer. The manufact- bare board

**Dave Jones:** PCB manufacturer, it doesn't care about the solder paste. They'll just ignore it. Um, but our assembler will need that file to generate the stencil. And we're not done yet. We have to generate our uh, pick and place files and our NC

**Dave Jones:** drill files. So, we go into our NC drill file, so our bare board manufacturer knows that where to uh, drill the holes and what size. And bingo, there's our hole information. And if if you actually zoom right in there,

**Dave Jones:** there's all the individual holes, but it will generate a text file uh, basically that has all that drill information. So, you're going to want to supply that to the bare board manufacturer. If you want to know what those drill files actually

**Dave Jones:** look like, here they are. It's uh, the Micro Current Panel Rev 2. Uh, it's generated Altium's generated two files, one for round holes and one for slots. And there is all the uh, Gerber um, the sorry, the NC uh, drill information that

**Dave Jones:** they need. It specifies the um the drill uh sizes and the um and the actual uh locations of where to drill the holes. And same for the slots. I've got some slots in the board, and they will know exactly where to do

**Dave Jones:** that. And there's my drill report file with the uh different tools. Uh they call them uh tools for each uh particular drill that's required and the hole sizes uh required the drill sizes actually required. And then uh the NC

**Dave Jones:** drill files just use that tool information to tell them where to actually put. And uh NPTH is non-plated through, and the other ones are plated through holes. And of course, all this uh Gerber and NC drill stuff is exactly

**Dave Jones:** the same regardless of where we whether we get an individual board manufactured or a panel. There is no difference. The bare board manufacturer doesn't care. Um actually, you don't have to do this panelization step. You can actually get

**Dave Jones:** your uh bare board manufacturer to do the panelization and add all the tooling stuff and the routing and things for you. But by the time you specify exactly what you want, you're better off doing it yourself. Really, you're better off

**Dave Jones:** specifying and laying out your own panel just so there is no confusion. You know exactly what you're going to get um that's going to go to your assembler. Otherwise, there's too much to-ing and fro-ing between you and the uh bare

**Dave Jones:** board manufacturer. It's just not worth it. Just do the panelization yourself. As you see, it's very simple. Takes no time at all. And one more step which we're going to need for our PCB assembler uh the pick and place files.

**Dave Jones:** So, we want to go into assembly outputs, generate pick and place files. And uh you can do that as a text or a uh CSV format or both. Then we'll do that. And bang. And there are various uh file

**Dave Jones:** formats available for this, but uh they should be able to all all the uh assemblers should be able to accept a basic uh CSV uh file like this and here you go. It's, you know, C1 there and it

**Dave Jones:** tells you exactly where to place that component and what uh orientation to place that component on the board. Usually, it's the center of the component, but um in general, the uh assembler will have to do a lot of

**Dave Jones:** tweaking to this file to, you know, tidy it up and make it suitable for their particular uh assembly machine and their assembly pick and place uh software cuz they're all not the same from different manufacturers and they have different

**Dave Jones:** internal methods to do stuff. Uh but that will be all part of your uh tooling charge that you'll pay for um uh doing um uh to actually set up uh the assembly of your board, but that's usually only a one-off fee. So, you pay

**Dave Jones:** it once and then you can run a million boards through. And that's all there is to the PCB side of it. I've completely panelized my microcurrent design now. Should have done it right back at the start, but uh I thought it was only

**Dave Jones:** going to make a tiny batch of them. It was just easier to do it uh loose as a one-off board and get it hand assembled. But anyway, I've done the little bit of extra effort now. It's panelized. I pay

**Dave Jones:** another tooling charge uh to get this board done instead of paying no tooling charge just to reorder the loose board, but the tooling charge isn't huge and uh bingo, I've now got 10 boards and I don't actually have to get this machine

**Dave Jones:** assembled if I don't want to. If I want to continue with my hand assembly, you can do that on the panel as well. In fact, it could be nicer the um if uh somebody's hand assembling this for you, they may actually prefer on a large

**Dave Jones:** panel like this. It just makes handling and things like that easier and it can speed things up cuz they can do uh 10 boards at a time. They can place the one component bang bang bang bang on all the

**Dave Jones:** different boards depending on their preferred method. So, even if you are going to use pick and place, panelizing like this is not a a way to go. So, now we go on to our next step in the uh

**Dave Jones:** design for manufacture step, and this one can take a hell of a lot of work, a lot more than just panelizing your board. I've said it before, you can spend 80 or 90% of your time actually doing the stuff we're going to do now.

**Dave Jones:** So, what we have to do is go through our um in our bill of materials for the microcurrent part by part, every single one of them. And if you've got a board that's got 500 parts on it, then you'll

**Dave Jones:** have to do this 500 times. But, I'll show you one. So, let's go for the max 4239. Go to a good website like Digikey, and let's max 4239, and uh let's or 30 38, sorry. Max 4238, and let's take a look at

**Dave Jones:** what we've got here. We've got the different packages. The one we need is the uh SO8 uh package down here. There it is, the max 4238 ASA plus, and uh the plus indicates it's uh lead-free. Yeah. And if we scroll across, if we take a look

**Dave Jones:** at this, it is bang, it tells us it's an it's an SO um eight-pin SOIC, which is exactly what we need, but it's in a tube. Now, um some of the assemblers prefer not to have tube uh tubes. They can be a bit uh

**Dave Jones:** troublesome, but Digikey do have 1,507 of those in stock. Uh they're available one off, but we would buy them in tube uh quantities. So, we would So, if we click on that, and we'll go into there and have a look at the individual part. Now,

**Dave Jones:** it doesn't uh if you scroll down here, it should tell you how many are in a tube. Tube quantity, and standard package, there it is, 100 up there. So, there's 100 that that standard package means that there's 100 of these devices

**Dave Jones:** per tube. So, if we wanted to buy if we wanted to assemble 200 of these, for example, then we would buy two tubes worth. Um otherwise, they're going to give you a partial uh tube. And that might not be so bad, but uh other times

**Dave Jones:** it it you know, it might be an issue. They may supply the extra chips outside of the tube. You don't know. They may actually repackage them. So, let's actually if we can avoid uh tube, we probably uh would like to um because

**Dave Jones:** most manufacturers assemblers these days will prefer the uh tape and reel. So, let's go down to the bottom here and look at this one down here, the MAX14238ASA+ it's exactly the same, but it's got a T on the end of it, which uh to me

**Dave Jones:** indicates tape and or tape and reel. And if we scroll scroll across, here it is, 8-pin SOIC in tape and reel packaging. But, uh unfortunately, um it's a non-stock item. So, they don't actually have it in stock. We'd have to

**Dave Jones:** get it in. It's 2,500 minimum. So, if we actually click on that, then they're only going to you aren't you have to buy 2,500 of them. But, and it gives you an alternative. So, really, that's ruled out. I mean, I'm not going to buy 2 1/2

**Dave Jones:** thousand of them and uh not get them in stock and have to wait forever to get them. Bugger that. So, it actually gives you alternative packages down here and it tells us, well, the tube. Duh, we've already looked at that, okay?

**Dave Jones:** But, at least it's there. It tells you what alternatives are available. So, it looks like at least from Digi-Key, um we have no option but to do uh the tube. But, um an equivalent part is actually the MAX4239.

**Dave Jones:** So, let's have a look at that. They're exactly the same chip, except they have a different minimum uh gain and a slightly different bandwidth. But, we can actually use either in this design, as it turns out. Now, here it is, the

**Dave Jones:** MAX4239 ASA plus with the tape in the tape and reel. Bang, no stock either. And it looks like the 4239, they've only in the tube, they've only got 41 stock anyway. That's useless. We'll use the 4238. And it looks like we're stuck with the

**Dave Jones:** tubes at least for this device. I hope the assembler doesn't mind. I'm sure they won't. All right, let's go on to our next part, the battery holder, the surface mount 2032 battery holder. The part number is 1060K. So, let's type

**Dave Jones:** that into Digi-Key and away we go. And here it is, battery holders. I've been there before, clearly. And there's two types available. Aha, once again, it's got the 1060TR. That stands for tape and reel and the regular 1060, which I've been buying up

**Dave Jones:** until now. Oh, look, both of them, they got a huge amount in stock, 11,000, 12,000. No worries. Man, I'd be over the moon if I saw all that many microcurrants, that'd be awesome. Now, as you can see, the minimum quantity for

**Dave Jones:** the non-tape and reel part, the individual, is one. I can just buy one of those for $1.83. Thank you very much, Digi-Key. That's awesome. But, I'm trying to design for manufacture here. So, um I've I've bought these ones before,

**Dave Jones:** but they have, you know, they actually provide them in a tray. And that's really no good for pick and place. It's not a proper pick and place tray. It's just a a storage and shipment tray. So, it's not really designed for pick and

**Dave Jones:** place. So, we're really going to have to go for the tape and reel option here. And as it turns out, I'm going to have to buy 500 minimum. Because if you scroll down, the standard package there is 500. So, we have to buy a reel

**Dave Jones:** of 500 of these things at $1.25 each. But, that's the price you got to pay. And if you want to only assemble 200 of these, well, they don't give you the digi-reel option, the re-reeling option, which we'll see later like they do for

**Dave Jones:** some other parts. So, really you are stuck with buying those 500 items if you want them on the tape and reel, at least from Digi-Key. You might have to go somewhere else if that, you know, if you only want to make 100 or 200 boards and

**Dave Jones:** you can't justify spending, you can't absorb that extra uh cost of those 300 um parts which you may not use. So, you know, you've got to weigh up these and you've got to weigh this up for each individual component in your design. It

**Dave Jones:** can get crazy. So, now let's go and look at another part, our Texas Instruments voltage monitor here, and let's see what we get. There's quite a few of them here, and uh what we want is to scroll over. We want uh cut tape, which is how

**Dave Jones:** I normally buy them. Cut tape means that you like they're minimum of one. So, you know, the person at the Digi-Key factory, the Oompa Loompas there, will just cut off your one little SOT-23 chip and put it in a little baggy for you and

**Dave Jones:** send it to you if you want, and it'll cost you a whopping uh dollar for that one part, and they've got 3,000 in stock. Not a problem, but it tells you alternative package is available, and it's available in tape and reel, and

**Dave Jones:** it's available in a digi-reel. Awesome. Now, the difference is, as you can see, the uh tape and reel here is uh that is a very low minimum quantity of 250 for the tape and reel. I was expecting that like minimum to be like, well, up

**Dave Jones:** the top here, 3,000. There it is. There's a tape and reel option. Looks like there's two tapes and reel options for this one. The one at the top here, take a look at this. Minimum quantity of 3,000, you pay 28 cents each cuz they're

**Dave Jones:** in volume, and it's tape and reel. Uh but it looks like the minimum is 3,000 on that one reel. So, this one tape and reel down here is rather interesting in that you can get 250 of them for $0.53. I

**Dave Jones:** I don't know what's going on there. And they offer you the Digi-Key the Digi-Reel as well, which is the re-reeling service. And this is incredibly flexible. So, they're giving you like four different options here to purchase your products. And this this is

**Dave Jones:** the advantages of buying through uh someone like Digi-Key. You're going to pay you know, you might pay for more for it, but you can really kit up easily for your projects doing this. Now, as you can see, it's uh all these

**Dave Jones:** alternate packages here are available and the minimum uh quantities and it looks like the standard package is 250. And it says tape and reel, so I guess that probably comes from the manufacturer TI themselves on a little mini reel. But, uh let's say you needed

**Dave Jones:** a thousand of them, um you could buy multiple mini reels and you could buy multiple four of these reels or you could go for the uh Digi-Reel. Where was it? Let's have a look at the Digi-Reel. Let's go back and there it is. Here's

**Dave Jones:** the Digi-Reel one and let's take a look at this cuz this is interesting. They give you an extra, let's say we wanted our thousand, they give you an extra box and you can calculate the price uh for the thing. And they tell you a $7

**Dave Jones:** reeling fee will be applied to each reel ordered. So, um and they're non-returnable of course cuz they've done something custom for you. And then you can calculate the price for a thousand and they'll then put a thousand of these devices on a reel just for you.

**Dave Jones:** So, that's a trade-off between buying the full reel from the manufacturer of 3,000 and four of those smaller reels because then the manufacturer uh the PCB assembler, if you've only got the little reel of 250, and you want to put 1,000

**Dave Jones:** boards through in one run, then they're going to have to stop the machine and change it change that reel at 250, and that stops the line, and costs you more time, and they're going to charge you more for that. So, if you know you're

**Dave Jones:** going to manufacture 1,000 boards, it's better to actually get 1,000 of these on the reel. But, remember, as I said, uh earlier, you there might be some loss in this. So, you know, if you were going to manufacture 1,000 boards, you might

**Dave Jones:** want, say, 1,100 or something like that. And, if they're real expensive devices, and you can't afford to lose any, you better tell the manu- the assembler that they're uh really expensive parts, and try not to waste them, please, and

**Dave Jones:** they'll handle them more carefully, and they'll put extended tapes on, and uh things like that to ensure um that there's less loss or zero loss. But, generally, they throw comp- these components away like they're jelly beans. So, uh just be prepared for some wastage.

**Dave Jones:** And there it is, quantity 1,100, 35 cents each, $386. If you want to manufacture 1,000 boards, that's what you'd get. Awesome. And I would do exactly the same step for every item in my bomb. But, thankfully, the Microcurrent doesn't have many parts in

**Dave Jones:** the bomb, so it shouldn't take me too long to do this. But, I've got to go through and order all these things on reels or tubes, if that's good enough. Preferably, uh reels for everything. Every one of these items, I might have

**Dave Jones:** to buy more than what I need, so I've got to try and absorb that cost, hopefully sell enough um units in the end to actually, um you know, cover that extra cost, which I've paid for possibly extra components,

**Dave Jones:** which I'm not going to use. So, that's the trade-off with um machine assembling, pick and place assembling um your boards like this. Whereas, previously, I'd order 50 parts, 50 boards, there'd be practically zero wastage from my hand assembler Vutronix,

**Dave Jones:** and you know, everything was easy and sweet. Now, it's a bit more of a gamble. You've got to put more effort into it. But hopefully the quality should be really, you know, 100% very repeatable, and it should in the

**Dave Jones:** long run be cheaper. But there you go, that's the design for manufacturing, just a basic product like this microcurrent. There's a fair bit of work into it, but it's it's worthwhile in the end. And if you're designing a really

**Dave Jones:** high volume product, this sort of stuff is absolutely essential. So I'll keep you updated on where the micro current is, and I'll show you the board when I get it back, the finished panel and things like that, and uh

**Dave Jones:** yeah, if you want to sign up for one, then there's a form on the website. You can sign up and register your interest for one so that I actually know how many people want one, and how many I've got

**Dave Jones:** to get manufactured. So I hope you enjoyed that. Catch you next time.
