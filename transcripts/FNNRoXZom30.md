---
video_id: FNNRoXZom30
title: EEVblog #558 - Beta Layout DIY SMD Thermal Reflow Oven
url: https://www.youtube.com/watch?v=FNNRoXZom30
source: youtube-asr
---

**Dave Jones:** Hi, everyone loves soldering stuff here on the EEVblog. They're some of my most popular videos, my soldering tutorials. Well, today we're going to take a look at and review, I guess, play around with a reflow oven controller kit from

**Dave Jones:** Beta Layout. They're a uh Oh, there it is. It comes in a huge box. They're a German company who started the PCB pool service almost 20 years ago now, where, you know, we take it for granted these days that you, you know,

**Dave Jones:** there's lots of companies out there that will take your files and put them on a shared panel, and that's how we get our low-cost PCB manufacture these days. Well, they started it 20-odd years ago with that PCB pool, they're one of the

**Dave Jones:** first companies to do it, and they're still going strong, and they offer this beautiful sort of, you know, all-in-one starter kit for SMD reflow because they, as part of their PCB pool service, PCB prototype service, they offer a free SMD stencil with every

**Dave Jones:** board, and they've provided me, and they also sell this all-in-one kit. So, we're going to check it out. Should be interesting. Let's go. Now, here's what I got in the box, and yes, my box cut does contain more than your usual box,

**Dave Jones:** but what is in the usual kit, just the reflow soldering kit itself, is No, it's not a toaster oven, it's a reflow oven. If you think it's a toaster oven, you're not thinking fourth-dimensionally. Um it's from Severin. I don't know, I've

**Dave Jones:** never heard of it. I don't even think you can buy it here in Australia. It's a European brand, I think. We'll take a look at that, but we've got ourselves a oven with a nice clear door, and that

**Dave Jones:** comes with the reflow kit, which we'll take a look at, which includes a multimeter and a whole bunch of stuff and the paste and things like that, and just that kit alone is 100 and uh sorry, um yes, 129 euros for that and or 178

**Dave Jones:** uh US dollars. Now, also for another 129 euro, I've got the re-flow oven controller kit, which uh turns this toaster oven into a re-flow oven, all controlled, which we'll get into. But, uh unfortunately, this is 240 volts only, so I don't believe they sell this

**Dave Jones:** in the US. Um so, if you're in a 112-volt 10-volt country, I think you are out of luck. It's not even on their American uh store. But, anyway, so they're 129 euros each. I don't know how that translates into various countries in the

**Dave Jones:** European Union and uh stuff like that in terms of uh value. But, yeah, you can probably get it. You can just buy this on its Sorry. You can just buy the re-flow kit on its own, which is uh 91 US dollars. I'm not

**Dave Jones:** sure uh what it is in uh euros, and you can buy your own toaster oven. There's nothing in particularly special about this uh toaster oven at all. You can pretty much use um anyone on the market cuz as we'll see, the re-flow controller

**Dave Jones:** has a learn button on it, which uh basically profile learns and profiles itself based on the thermal oven that you've got. Hello. You can see me. There you go. Um this Severin brand oven, I you can buy this separately if you want.

**Dave Jones:** So, you can just buy the re-flow uh kit basics kit and buy your own uh if you can get this cheaper than, you know, by all means do it. You don't necessarily have to uh buy it from Beetle Layout.

**Dave Jones:** And uh it is just your typical uh direct heat toaster oven. It is not a convection oven, so there's no fan inside to actually, you know, uh circulate the hot air. They are technically uh better cuz they give you

**Dave Jones:** a more even uh you know, a temperature distribution within side the thing, but this is a just a crumb uh tray on the bottom here, so you don't even need that. Two elements on the bottom, front and back

**Dave Jones:** there, and there's another two elements on the top up under there. So, there they are up under there. So, technically, you know, the issue with these reflow ovens is that technically you can get hot spots. Now, it's recommended that you have this

**Dave Jones:** in the center, of course, like this, but because there's no convection in there, there's no fan to blow the hot air around, technically it could get hot spots on your board, and that's not necessarily a good thing. So,

**Dave Jones:** this is just a normal oven, but hey, it's going to be good enough, especially when you put the reflow oven controller onto it. I probably wouldn't recommend a non-convection oven if you don't have a reflow controller, but hey, you know, everyone

**Dave Jones:** has their own experiences. I'm sure there people will be saying, "Yeah, I got no problems using my you know, non-convection oven without a controller, and it works just fine." But, the issue with the control the thing with the controller is

**Dave Jones:** that, you know, you don't have to manually time anything or anything like that, and, you know, it's going to give you a semi-professional sort of reflow profile. And control-wise, it's just a manual timer, which you're not going to use. And

**Dave Jones:** basically, whether or not you want the top elements, the bottom element, or dual elements. In this case, they recommend using the dual elements, top and bottom, so it heats it from the bottom of the board, and heats it from

**Dave Jones:** the top. Try and heat it evenly. And then, we've got our temperature, which goes from 100 up to 230, but basically, you want to just for operation, because it's got the external controller, you just want to set it to maximum, dual

**Dave Jones:** element, and Bob's your uncle, you then the reflow controller does everything. It's got a temperature probe in there, and it actually can control the heating elements externally. So, these reflow controller kits, they want you know, you really need one of these dumb ovens. I

**Dave Jones:** mean, it doesn't even have a, you know, it's got an off switch, but you know, you basically just want to leave the thing on. It's dumb, it's got no intelligent controller in it, so it can be, without being hacked at all, you can

**Dave Jones:** just put the controller in series with the mains plug, and it just switches the elements um off and on, and can use the PID control loop to control the temperature inside once you put a temperature sensor in there. But, as far

**Dave Jones:** as uh toaster ovens go, I don't mind the feel of this. It seems to be, you know, reasonable quality. Now, what you want in a good uh thermal uh reflow oven like this, nice big clear glass window, so you can

**Dave Jones:** see exactly what's uh going on there. Absolutely essential for uh reflow work. It's got nice feet on the bottom of to lift it up above your bench, and it feels like a reasonable quality unit, you know, it's not high-priced. It's

**Dave Jones:** probably like 50 bucks retail or something, but yeah, it does uh feel decent quality. And it's got a total internal uh space of 300 mm across there. Easily fits my microcurrent channel, as you can see, and depth, a

**Dave Jones:** good 300. So, we're talking 300 by 300 mm boards. So, that's a pretty decent capability. You probably, in most cases, don't want to do panels any bigger than that. And in our reflow starter kit here, which you can buy uh separately,

**Dave Jones:** as I said, or you can buy the individual parts separately if you just need them. Um but, this is all convenient in one box. It's got just a 3M Scotch masking tape here to hold down the boards. We've

**Dave Jones:** got a a power adapter, a uh looks like a UK to um EU power adapter or something like that. We've got ourselves our lead-free uh solder paste. This is about uh 20 bucks retail or uh something like that. So,

**Dave Jones:** that's 100 g worth, so that's going to do a decent number of boards there. Lead-free. And uh we've got ourselves a spatula, metal spatula, that's going to work really well. Um we've got ourselves a cheap-ass PicTech multimeter. Look at

**Dave Jones:** this pile of garbage. But uh you know, they just throw this in just in case Oh, something just fell ON MY TOE. OH, THAT HURT. THAT HURT. MAN, DON'T know what it was. Anyway, PicTech multimeter manual range thing. They just

**Dave Jones:** throw this in. Oh, look, they've even got their own beta layout sticker on there. Look at that. And just some crap multimeter leads. That is a temperature probe uh just in case you didn't have one, but there's also a temperature

**Dave Jones:** probe with the uh reflow oven uh kit, which we'll take a look at. And inside, then we've just got some uh boards. We've got a training stainless steel uh stencil so that you can do some um uh trial stuff on there. And then we've

**Dave Jones:** got uh various uh just uh blank boards, which are put down templates that you can just slide your board into and hold it in place with these angle pieces as we'll see. Oops, I left these out of the box, but they do

**Dave Jones:** come with it. Last but certainly not least, they've got some uh example components. So, various sizes, 1206 down to 0603, SO-23s, and SO-8 to match your uh training board, and some very nice-looking uh Vetus brand Swiss um SMD tweezers.

**Dave Jones:** Awesome. But this is where the real magic happens, the uh reflow oven controller kit. So, you just plug it in series with uh either this toaster oven or any toaster oven, and it turns it into an intelligent uh profile

**Dave Jones:** temperature profile SMD thermal oven. Comes from Ireland. Awesome. So, this one is, as I said, 129 euros, and it looks really good. Here's the temperature probe, which plugs into the front of this thing. Let's have a look, and this looks really

**Dave Jones:** top quality. You know, that's just a really nicely done. I like that. It's got various preheat, soak, reflow modes, dwell, and a learn mode. As I said, you just press the learn button, as we'll see, and it learns the profile of your

**Dave Jones:** oven. Sets it all up, and you plug plug your temperature probe in there, and mains power in 240 volts only, as I said, mains power out, which then goes in series with the oven, and it's got RS232 interface as well. And they did

**Dave Jones:** send me Where is it? A USB RS232 converter, which I don't think comes with it. I think you have to buy that separately, or you can buy that from anywhere on eBay or anywhere else. And I thought I'd

**Dave Jones:** have to hack the weird ass European plug on the toaster oven, but I don't. It comes with a nice adapter, which then just plugs into the back, and plug that straight into your toaster oven. Brilliant. And it looks

**Dave Jones:** like, assuming the serial number is sequential, they've made quite a few of these. 4,296. 1,500 watts max. This particular toaster oven is, coincidentally, 1,500 watts. And as I said, 230 volts only. So, I don't believe they have a model yet.

**Dave Jones:** Maybe there's one in the works for the US market. But, yeah, if you want 110 volts, sorry, this one's not going to do the business for you. And you know what we say here on the EV blog, don't turn

**Dave Jones:** it on. Take it apart. If I can get it apart, let's see what this puppy has to offer inside. There we go. Oh, that's pretty neat. Nice little controller board. Looks like we have ourselves a big ass Yeah, we've got ourselves a big ass

**Dave Jones:** solid state relay down there from Sharp, by the looks of it. We have a good look at that. Nice little PCB mount transformer there from Gurth, by the looks of it. It's a fused. Everything's hunky-dory. It's got an

**Dave Jones:** external fuse here, and that really looks uh quite neat. I rather like that. So, yes, that is a Sharp a 16-amp solid state relay, S216S02, 4 kV isolation, mounted on a nice little heatsink there. That really is implemented quite nice. I rather like

**Dave Jones:** that. They've got a small HRC fuse down in here for that. And, you know, it's just all nicely integrated, completely safe, not a problem. And we've got ourselves an ATmega32 there, RS232 interface chip, and a thermocouple amp. And that's all she

**Dave Jones:** wrote, just down the bottom. Just we've got a a SO8 voltage reg there, and just the rectified AC input from the transformer. Too easy. And they also sent me an example of my latest microcurrent design board. They actually panelized this for

**Dave Jones:** me in a 2x2 format as an example of their PCB pool service. And the whole idea about the PCB pool service is that it comes with a free stainless steel stencil. So, you get your board made, and you get your free stencil. Not a

**Dave Jones:** crappy Mylar one, but a proper stainless steel one, like you get from a professional professional you know, SMD manufacturer for professional production. So, that'll last for thousands and thousands of boards. Excellent. I love it. And yeah, their board quality looks quite good.

**Dave Jones:** They sent me a green. That's their standard finish. They can do other colors and stuff like that to order, but they wanted to give me an example of their actual production, their regular production process. And as you can see,

**Dave Jones:** because I only gave them a single board file, they didn't know how to panelize this. I didn't tell them how to panelize it. So, here's a just a quick trap when you let a PCB manufacturer panelize your files for you. Now, if you compare it

**Dave Jones:** with the one that I did myself, you notice that they're in the corner like that. Because this is a front panel board, I deliberately specified in that so when you cut it out with the side cutters, you get a nice clean and all

**Dave Jones:** your edges are nice and clean and everything. But because I didn't tell them how to panelize it, just by default, they just whacked them anywhere. So they've put them in for me as as this being a front panel in the

**Dave Jones:** most inconvenient uh location possible, which is on the side. So when you go and cut these things out, you're left with like a horrible looking side on them. And that's a lot worse than doing it on the corners. Now, you know, if you're doing

**Dave Jones:** a front panel like I am, that's really important. But if you're just doing a regular production board regular board that, you know, goes inside a box and no one's ever going to see it, doesn't matter, of course. But I just wanted to

**Dave Jones:** point that out. That is a trap for young players about letting the PCB manufacturer panelize your board. And I talked about this on uh this morning's Amp Hour that I just recorded. So check that out. Now, normally I'm not a fan of

**Dave Jones:** green boards, but I actually really like it. It's more like an olive color when you've got the of course I've got a ground plane on top there. So, you know, here's the regular green cuz there's no copper under it. But you put that copper

**Dave Jones:** under it and it just goes this nice olive color. And I actually really really like the um the standard green with the copper under it. That's just a beautiful color on it. And um I can't find any manufacturing uh faults with

**Dave Jones:** this uh board at all. Take a look. I'll get the macro lens out. Take a look in more detail. There's the bottom flip side of that. They've just got it all right. We'll have a look at the um

**Dave Jones:** via hole alignment and uh stuff like that. Let's go to the macro lens. Now, the first thing you notice is that it this is clearly not a photo imageable um overlay uh component overlay white component overlay. It's all uh you know,

**Dave Jones:** dot matrix uh printed. And you know, you can see that yeah, you can see the lines in there and it just doesn't look nearly as good. You can see that you know, the text doesn't turn out that great. So, I

**Dave Jones:** certainly wouldn't use this as a production board. That's for sure this particular process. So, if you compare this which I got from project PCB, this is going to be my production panel. The quality of that is, you know, even

**Dave Jones:** though it is still that dot matrix technique, it's not photo imageable. It still, you know, is much better than the PCB pool one unfortunately which didn't turn out that great. So, bit for prototypes, eh, it's adequate. I don't

**Dave Jones:** really see any misalignment on those via holes either. So, I think they're 0.4 mm on a 0.8 mm pad. Not a problem. And no problems on the really thin sliver of solder mask. I think that's like 4 thou

**Dave Jones:** or something going through there. Not an issue at all. So, these PCB pool PCBs are perfect. They're adequate for prototype stuff, but the yeah, the quality their overlay does let them down significantly, I think. I'm not not entirely happy with that. For

**Dave Jones:** prototypes, fine. Wouldn't touch them for production though. And a stainless steel stencil lines up perfectly as you'd expect. Yeah, that's just me around there. Unfortunately, they only gave me the stencil for a single board. They didn't didn't give me

**Dave Jones:** the stencil for the entire four board panel. I'm not sure if that's a usual or just that's a quirk of the one they sent me. So, the issue with that, of course, is I can't reflow well, I can't assemble all of these

**Dave Jones:** boards and apply the paste like this because if I Sure, I can line that up, use the squeegee, apply my paste on those pads, but then if I move it over to this one, it's just going to ruin, squish all the

**Dave Jones:** paste there. So, what I'm going to have to do is break out the individual boards and just do them one by one. That's a bit of a bummer. I would have preferred to get the full stainless steel stencil

**Dave Jones:** for my entire panel. And by the way, it comes with an instruction manual on disk as well, so you can read this explaining how to do this and how to use the reflow oven controller. Now, what I've done

**Dave Jones:** here is uh we're going to apply the solder paste. Let's get right into it. And uh basically this right angle board acts as a template. So, you just start stick that down there like as as a template retainer. So, you just stick

**Dave Jones:** that down in place like that. And then your board, which can just sit in there just sits in the corner like that. And then you get one of these corner pieces and you tape it down. So, when you're

**Dave Jones:** applying the squeegee across the top of that, once we put our stencil on, your board doesn't move. That's just the whole idea behind that. Now, we want to put our stainless steel stencil on there and there we go. It lines up perfectly. If

**Dave Jones:** you take a look at that. Beautiful. There's a bit of art in getting these things uh lined up. But uh generally good enough by all right. Like that. And we only want to put one strip of uh tape along

**Dave Jones:** this edge here. So, that when we're done when we're done with the squeegee, we just want to lift the flap up like that. So, we don't, you know, dick around with it and uh disturb our nicely placed solder paste. So, let's get ready to go.

**Dave Jones:** And let's have a look at the solder paste we're going to use here. It is which are one of the top uh brands in the industry. No clean, lead-free, tin-based solder paste. And it's important to get the no clean stuff. It

**Dave Jones:** means it doesn't leave behind any crappy residue that you got to clean up on your board as a uh post reflow process. So, that's really good. Anyway, this is type uh NC254. That's the model number. SAC305. Don't confuse it with the NC254,

**Dave Jones:** which is you can get in a lead leaded version. This is the lead-free stuff. Looks like we got a fair bit left on the expiry date there. This stuff uh data sheet says it has has life of uh 9

**Dave Jones:** months if kept between 4 to 10° C or 4 months if left at uh room temperature. But, for you know, just prototype around like, you know, where we're doing here, you can probably keep this for 12 months at uh shelf uh

**Dave Jones:** temperature. It's probably still going to be usable. You just mix it up a bit. It's just that the uh uh you know, the uh volatile chemicals inside the solder flux in there just, you know, over time just leak out or do

**Dave Jones:** whatever. They're just, you know, but you can mix in some flux uh afterwards if it is like dried out a bit. But, anyway, let's not go into that. So, uh 100 g worth, it'll do a decent amount of

**Dave Jones:** stuff. So, this is what it looks like inside. There we go. 100 g of solder paste. Tight asses, they can't give you a full tub, can they? Anyway, um this comes in various uh type sizes uh from T3 to T5. T5 have smaller

**Dave Jones:** solder balls than T3. Comes in T3, T4, T5 industry standard sizes. I don't see any T marking on there, so I'm not sure what size uh solder balls that this particular one is. And here's the data sheet, which I'll link in down below,

**Dave Jones:** and it extols the virtues of this wonderful solder paste a broad printing process window and uh reduces avoiding under micro BGAs. And there we go. This is important. 12 to 14-hour tack time. So, when we apply our solder paste here

**Dave Jones:** to our stencil, we've got basically half a day to of good working time to apply our components to the board, maybe 24 hours on the stencil. So, you know, anyway, it's you know, you've in no hurry essentially to place all your

**Dave Jones:** components down. So, that's really good when you're hand placing stuff. There's all sorts of printing recommendations here. Look at this, the squeegee pressure, stuff like that. But, you know, when you're doing it by hand with your squeegee like this, I mean,

**Dave Jones:** obviously, you know, not really controllable. But, when you've got, as I showed in a previous video which I'll link in, when you've got automated squeegee machines, um you can actually set and program all this uh sort of pressure and stroke speed into your

**Dave Jones:** machine. So, you want to you know, there's all different types of solder pastes. More on the market than you can poke a stick at and you have to set up uh your solder paste machine in production to match the exact type of

**Dave Jones:** type of solder paste you're using. And there we go, there's all sorts of you know, the snap off distance of your um stencil and you know, separation distance. Uh all sorts of stuff. They really go to town on how to use this

**Dave Jones:** stuff. And here's our all important uh temperature reflow profile. And basically, the reason it looks funky like this is cuz they're basically the windows you have to operate in. So, you've got to keep your temperature at each particular

**Dave Jones:** time point somewhere within side this window. You know, it's very broad down here with the preheat kind of stuff. Doesn't really matter. But once it gets up to this critical region, you know, you've got to keep it within inside

**Dave Jones:** window to get optimum reflow solder and then the cooling period. And that's why it's you know, it's best to get one of these reflow oven controllers. At least it's going to be repeatable and attempt to get a profile even though we don't

**Dave Jones:** have a proper convection oven or a you know, proper IR oven or something like that. We've only got a toaster oven here for goodness sake. But combine it with a reflow controller and we can get something that looks like one of these

**Dave Jones:** profiles. They've got one for low density boards and another profile for high density boards as well. And you'll notice that the temperature There we go, you know, it peaks around that 230 mark. And as you saw on the oven, this

**Dave Jones:** particular oven's only capable of 230. But it's going to do the job. That's just enough. And we have a visitor. Who is it? It's Sagan and she who must be obeyed. Sagan wants to come in and play with the

**Dave Jones:** reflow oven. He's more interested in the MakerBot than the reflow controller. And there we go. There's the micron sizes for the little balls for the different types there and you've got all the technical details you could possibly imagine surface insulation resistance

**Dave Jones:** and uh more sorts of stuff than you can poke a stick at. Uh look at tack test test results and stuff like that. They've got various IPC standards for this sort of thing. And well, surface mount reflow soldering is not

**Dave Jones:** easy, folks. It's almost rocket science. And of course, all these are thermal profiles. These aren't, you know, absolute values. These can change depending on your type of components, your board, and things like that. Because if you got some real critical components, you you

**Dave Jones:** know, you got to watch out and make sure that your thermal profile is going to match those critical components as well. So, here we go. I've got my stainless steel stencil just set there as a flat like that. So, as I said, we can peel it

**Dave Jones:** off at the end and we shouldn't disturb our solder. Now, let's get our paste out. We'll put a little bit on here. You've got to mix it after you get it in and this can be tricky business. We won't need much.

**Dave Jones:** I only need a tiny little bit today. So, let's just put a little bit on there and then we just want to have a play around with that. Just give it a bit of a mix. There are better ways

**Dave Jones:** to mix it than this. Now, if you're taking it out of the fridge, you do want to let it cool down to the room sorry, warm up to room temperature. But anyway, let's take that now and let's give it a go, shall we? We'll start like

**Dave Jones:** that and just move across like that. There we go. We've got some in there. And whoop. There we go. I probably should have done some more mixing than that. Probably a few people screaming at me at the moment

**Dave Jones:** that it's not optimum, but you want to get a bit of an angle on that. And I could have got that in one stroke if I knew what I was doing.

**Dave Jones:** Anyway, that looks pretty good. Well, good enough, anyway. We'll just peel that back like that, and we should be left with a nice amount of paste on each pad. Let's go get a close-in look. There's our 0805 pads. Not

**Dave Jones:** absolutely perfect, but certainly good enough, and you can see the paste applied. There's our SO-23s, our 1206s. 1206s, ah man, they're as big as houses. SO-8, massive. No problems there at all, but uh There we go. We should be able to And of

**Dave Jones:** course our little 0603s. Ah, that one down there is a bit of a bit of a loser, but that's got more than enough paste on there to do the job anyway. So, that's just going to work fine. There you go.

**Dave Jones:** You can see that up close there. The tiny You can see see if you're watching this in HD, you can probably see the tiny little balls in that solder paste. And there's that little slightly failed 0603. We just uh SO-8 over here, you'll

**Dave Jones:** find that there's a solder mask between pads. All right, we'll place some parts. I've got some five SO-T 23s here. We'll use the uh SMD uh uh tweezers that came with it. Personally, I don't like the hook uh

**Dave Jones:** type like this, but eh each to their own. We'll give it a go. And hand place it. I don't have to get the alignment too spot-on. Ah, they're all upside down, of course. And don't have to get the alignment too spot

**Dave Jones:** on because the component will when the solder paste reflows, they will self-center into the pads, and that's the beauty of SMD. You just got to get them near enough, and uh although it does vary with component. I'll place our 1206s here. These are, as

**Dave Jones:** I said, 1206s. Big as houses, these things are absolutely enormous. Anyone who can't SMD solder using uh uh by hand using 1206 components really um needs to get their eyes checked because Stevie Wonder could uh salt hand solder

**Dave Jones:** 1206 parts. You want to give them just maybe a little push down there to get them onto the pads, and uh well, I'll finish the rest of them. Now, I don't care how good you claim to be, 0603

**Dave Jones:** starts getting down into the territory of being a little bit annoying for hand soldering and hand placement. Um certainly when we're talking hand soldering, I mean, I can I think I you know, I can solder 0603s not a problem by hand without any uh

**Dave Jones:** without any uh magnification, but then when you get to 0402, I find I really need magnification. It really helps, but 0603 generally pretty darn annoying, but that's what I got on my Micro Current. Wasn't designed for hand assembly. If

**Dave Jones:** I'm designing stuff for hand assembly, I'm going to stick to 05 um I'm going to stick to 0805 and SO packages and SOT-23s. Now, I've got my reflow controller hooked up in series with the oven here, and the soak

**Dave Jones:** LED is flashing there. That means that the we haven't plugged in our temperature sensor. Now, with the thermocouple here, we need a dummy board inside this chamber to get the heat from. Now, it should be a similar material, similar type to what you

**Dave Jones:** intend to solder. So, I've just got a standard 1.6 mm FR4 board here. I've just thread the thermocouple wire through here just to give it some stability so it doesn't shake loose. And then I've just Of course, you don't

**Dave Jones:** solder it in one of those holes. I've just you know, placed it down in one of those holes. So, we'll place this in the middle of our oven and that will be our control board where this thermal reflow

**Dave Jones:** controller will learn the temperature from. So, there we go. There's our board in the center of the rack. Now, ordinarily, I'd have this rack up one a bit more in the center, but there's actually not an exact center point in

**Dave Jones:** here. But because I want to get some video, I need to have my board near the front of the edge down a bit. So, I want to get some video through the glass here. So, you know, for for production,

**Dave Jones:** you would want to put it in the center, but I'm going to do it over here. Anyway, it's hooked up. It's got it coming out the door. Now, this is, you know, just a kludge at the moment. I

**Dave Jones:** might actually take the covers off this thing and see if I can feed in for a more permanent setup the thermocouple probe through the inner wall or something like that and then have the board sort of, you know,

**Dave Jones:** semi-permanently set up in there. Now, it's flashing the learn that LED is now flashing. That means that this box comes, well, a dumb. It hasn't learned this oven. So, we've got to put it into learn mode now and it will just heat up the

**Dave Jones:** oven and it will learn. This is one of one of the things I really like about this oven. It'll check out the profile and set it up for any oven you choose. Really simple. I like it. Assuming it

**Dave Jones:** works. All right, let's turn this thing on. Just goes through a sequence there, and the learning lead is flashing. So, what we're going to I've got my Fluke hooked up as well with a thermocouple. Now, this thing should heat up the in

**Dave Jones:** learn mode should heat up the oven to 100° C, so I can get a reference point and then stop. So, let's press the learn button. And there we go. It's on. The light doesn't seem to come on, so I don't know Is it?

**Dave Jones:** Oh, yeah. No, sorry. It's on. You just can't see it. It's quite uh it's quite dim. Oh, I can see some smoke coming out. So, uh this thing is uh probably to be expected being used for the first time.

**Dave Jones:** Geez, I hope it doesn't set off the smoke alarm here in the building. That'd be embarrassing. And my um my Fluke thermocouple isn't exactly on the board, so I expect some error uh there certainly. Uh all the uh all

**Dave Jones:** the residual smoke seems to have gone. Not a problem. Oh, there we go. There we go. So, according to the Fluke, it overshot a bit, but as I said, that's not mounted on the board. It's not exactly uh going

**Dave Jones:** to be spot-on there, but uh yep, that is uh done. It's finished. So, now it's learned. The it's not uh blinking anymore, so now we should just be able to run the soldering process. That should work a treat. Now, you can

**Dave Jones:** see that the uh reflow lead is flashing here, and what that indicates that inside the oven is still greater than 50° C, and it won't let you start a new soldering process until the oven gets down below 50°. So, that's one of the

**Dave Jones:** disadvantages with this thing is that uh you do have to wait if you're doing uh if you're doing boards, you know, big batches of boards in sort of, you know, a small-scale production process. You got to let the oven cool down to less

**Dave Jones:** than 50° before you do your next board. So, yeah, the uh rule of thumb is jam as many boards in there in one go as you can and reflow them all at once, cuz this could take some time to cool down.

**Dave Jones:** And of course, one of the uh reasons for the discrepancy on the Fluke uh meter there is because the um thermocouple of the Fluke temperature probe there was just sitting in free air. So, it didn't have like the thermal mass attached to

**Dave Jones:** the board like I've got for the other one in there. So, you'd expect the Fluke to actually go a bit higher than the 100 degrees C that the reflow controller was expecting. We're ready to go. So, let's stick our

**Dave Jones:** board in. Once again, it shouldn't be at the front like this. I'm just doing this so that I can possibly get some video. So, this is not ideal location because it's right under one of the elements here. Not that

**Dave Jones:** great a thing to do, but anyway, for the purposes of today's experiment and being on video, then that's what we're going to do. All right, we are ready to go. So, let's run this thing. I'm trying to get a shot.

**Dave Jones:** I've only got the 0805s in shot here cuz I want to try and get the close-up. We should be able to see those resistors self-center though. So, here we go. I'm going to press the solder button and well, hopefully, this sucker's going to

**Dave Jones:** work. Here we go. We're in our preheat phase. So, this will take a bit. And this is designed to heat up the board slowly and evenly so that things don't crack and the components so that things don't crack and

**Dave Jones:** do all sorts of nasty little mechanical issues. So, we'll start out with the preheat and then we'll go into the soaking phase which is designed to activate the flux inside the solder paste so that all the volatile chemicals inside the flux, they

**Dave Jones:** all burn out and then you hit the reflow phase. Wham, that just peaks it up and reflows that solder. And then after that, we've got the dwell time which is the the actual decay of the temperature. So, all these things by the way in this

**Dave Jones:** reflow controller, all these all these various parameters, they are settable. So, you can actually program this all via the serial port. There's various serial port commands to do this, but I'm just using this straight out of the box using its default values. So, uh

**Dave Jones:** who knows what's going to happen? But, uh Okay, we're up to 1 minute 10 and we're still preheating. There we go. We've just switched into the soak phase. My fluke says that was 118°.

**Dave Jones:** And I can see that the element is switching off and on. It's switching the element off and on at about once per second according to the blinking light on the front of the oven there. Sort of uh maybe, you know, half second

**Dave Jones:** on, half second off uh cycle time for that. So, temperature slowly going up. It's still only 125° according to my fluke. And there we go. We're into the reflow process at well, 153 it's saying according to my fluke there. And

**Dave Jones:** according to the oven light, it's uh the element is continuously on now. So, we should see the temperature ramp up a bit quicker now. And the good thing about having one of these reflow controllers is that it does

**Dave Jones:** ramp up the temperature gently rather than just uh you know, getting the regular toaster oven just switching on the elements and you know, baking your board. This one at least has a modicum of control about it.

**Dave Jones:** Here we go. You can see the solder starting to melt. And a couple of those, the ones on the uh left-hand side there, they've almost reflowed, but the ones on the right there haven't done so. They're about to. I think I can notice

**Dave Jones:** something happening there. So, you can as you can see, not an even temperature spread across that board. And there we go, we've switched into our dwell cycle. And uh well, we haven't had reflow of uh three of our

**Dave Jones:** resistors there. I can't quite see the other components, but I don't think they've fully reflowed, either. So, I'm not sure what the go is there. Anyway, it's still going. And we're back to a flashing reflow LED. Um I don't know. I might have to go read

**Dave Jones:** the manual on that one. What's going on? No, well, that um according to the manual as before, it's um it's finished. But it didn't reflow all of our parts in there. Ah, it's terribly disappointing, and it didn't really uh pull them in place

**Dave Jones:** very well, either. So, this could be a fail, folks. So, that is terribly disappointing, and of course uh I'm not going to touch it. It's still uh it's still quite warm. In fact, uh these boards, as I've said in previous video,

**Dave Jones:** can retain their heat, especially if they got lots of uh ground plane copper in the mar This board doesn't, but uh still, it can uh retain heat for a significant amount of time, but we have a fail. I mean, these components, some

**Dave Jones:** of these components just have not reflowed. I'll show you this when we take the board out, but yeah. What? This is supposed to work out of the box, and it doesn't. Disappointed. And as you can see, those sot 23s

**Dave Jones:** haven't reflowed. I mean, some of the pins have there, but that's pretty much Well, it's certainly a fail. Um and the 0805s, as I said, a couple of them have reflowed and they look okay. The 0603s have reflowed, not a problem there.

**Dave Jones:** And the 1206s, not now, only a couple of them have reflowed and our SO8 hasn't reflowed at all. And I just noticed something very dumb. I put the reflow controller up on the top of the oven here just for convenience for

**Dave Jones:** shooting this video. And of course, the top of that oven is very hot and consequently, the bottom of that box is very hot as well. So, I'm thinking that may have possibly affected the accuracy, perhaps, of the built-in

**Dave Jones:** thermocouple, and perhaps. So, that's probably not the best. You really don't want to be sitting this thing on the top of this reflow oven. D'oh! Trap for young players. All right, let me try that again. I'm going to run through the

**Dave Jones:** learn process again and then run it through the complete cycle again with the board in the center. And this is the real advantage of the really smart learn mode on this thing. You can just, you know, quickly just

**Dave Jones:** readjust it, recalibrate it for any position inside your oven. I, you know, I changing ovens and things like that. I really quite like that. That works really well. And I started reflow soldering again. Sorry, I can't get any video of this.

**Dave Jones:** The board is like sitting smack bang in the middle of the oven and it's dark in there. So, it doesn't really work getting a shot for these things. Quite difficult, but I can certainly see it by eye, but yeah, the camera's not that

**Dave Jones:** great. All right, we're in the soak phase now. What we're looking for here is to at least on our Fluke here for the internal temperature that oven to get at least to 225 or or degrees or thereabouts, which puts

**Dave Jones:** it within sight of that reflow window there. Whoop, and we're into the reflow process now. And by the way, this LED on the front does actually match the heater element. So, when that's on, it means the heater element's on and the

**Dave Jones:** light on the front of the oven actually duplicates that. So, if we don't see this get to at least like 220, 225, 230° C, then well, something's you know out of whack cuz I'm assuming that my you know good Fluke temperature probe is

**Dave Jones:** accurate. And even the chart that comes with the Beta reflow kit, you know, it's showing a peak at 250. This is for its supplied no clean lead free solder paste. So, in this reflow process, it says 2° C per second ramp up. And are

**Dave Jones:** we? 2° C per second? Oh, not quite. Anyway, we're getting close to our temperature now. So, this is pretty good. This looks like it's going to do the business. 220 is close enough. So, I think we're uh uh we're going to be in the ballpark and

**Dave Jones:** that board should have reflowed. It'd be nice if there was a light in there. Geez, that'd be neat. But it's still in the reflow phase. It's coming back down because it hasn't uh hasn't switched the heater on there for

**Dave Jones:** a bit. But it you know, it basically according to our solder paste uh our actual solder paste data sheet there, you know, it got to 220. So, it you know, near it's pretty darn close to bloody Fluke switched off. That's

**Dave Jones:** hopeless. And now, there we go. It's just switching it on again. So, there we go. Oh, there we go. And we're in dwell now, but it's still uh switching that element on.

**Dave Jones:** But, anyway, that should have reflowed. So, I'm going to I'm going to claim that's, you know, near enough in terms of uh temperature. I'll probably get a second multimeter and a separate uh a second thermometer in there as well,

**Dave Jones:** just to check that out. But, once again, um but that's not the thermal mass though. Remember, this uh Fluke temperature probe is actually um just hanging in free air in there. So, um technically, that actually should be a

**Dave Jones:** higher temperature than what uh the oven is. But, anyway, that is done. It is done and dusted. It is finished. So, what did it peak at there? At about uh just over 220 or something like that. And the thing is, you can get in there

**Dave Jones:** with the serial commands, and you can actually calibrate the thermocouple that uh comes with this thing. But, it says in the manual, ordinarily, you shouldn't need to do that. But, there is a manual mode where you can go in and actually uh

**Dave Jones:** actually calibrate its temperature and uh pre-program it into here. There you go. That looks like it's done the job. If we have a look there, there seems to be some sort of like residual flux left over or something like that. So,

**Dave Jones:** um I don't know whether or not it's I mean, surely it's fully activated. I mean, you I mean, you're not going to get the uh the solder reflowing unless it's fully activated. But, I don't uh know this particular type of paste

**Dave Jones:** offhand of what it looks like after it's uh reflowed. But, it barely got to temperature there. Um and well, yeah. I don't know. It looks like it's done the business. Although, I think we are running a little bit under

**Dave Jones:** temperature there on our oven, I think. I don't think it's getting up to exactly what it should be. So, what I'm actually going to do, because I'm a bit concerned that this thing's a bit under temperature, I'm going to recalibrate

**Dave Jones:** the thermocouple in this thing. Now, there's two ways to do it. One is to hook it up to a PC and do it that way or it's built in to the firmware in here and you can do it just do it like that

**Dave Jones:** and I'll show you how to do it. I've got two other thermocouples that you let and fluke in there. As you can see, they're reading slightly different, so I'll just like split the difference or something. Temperature-wise, I think I'll probably,

**Dave Jones:** you know, we're getting up to like just barely 220 before. I'm going to set it maybe for 240 or thereabouts. All right, so the way I do this is I press the learn button and as soon as the on-off

**Dave Jones:** button comes on a LED comes on, I press the solder button and then it'll turn the oven on full power. As soon as these two reach 240, I press off and it should store the value in there. So, here we

**Dave Jones:** go. Learn and solder. There we go. Hello. Hello, McFly. It's not heating up. Hmm. What's going on? And looky here, the two thermometers are eventually settled down pretty darn close to each other, so I'm pretty confident in that. What I've decided to

**Dave Jones:** do is hook on the serial port onto here and actually check, cuz it's got to come on to check what the temperature's reading. So, if we go into 28 um to see if it matches 28. Here I am in

**Dave Jones:** the serial console for this thing. So, if we type temp show, we expect to see Ah, look. See? 36° C. It's way out. No wonder it's reading No wonder this thing was under. So, this thing it it calib

**Dave Jones:** You know, out the box was 36° C. That's hopeless. That was why our board didn't reflow properly. It was too low in temperature because it thinks it's higher um if it's, you know, if that was lower then it would go over temp, but it's

**Dave Jones:** not. It's higher than what it actually is in there and well, no wonder. And if we actually type the show all command, it should give us all of the current parameters for this thing and you can see that's, you know, the

**Dave Jones:** preheat uh temperature, preheat time, preheat power, so temperatures are all this stuff we can adjust manually if we want. Anyway, what we want to do is because that's uh 35°. It was 36 before and it's 28 in there. We're basically

**Dave Jones:** out by 7° and uh if we go temp uh offset, then you can see that there's no offset programmed in, but we can uh temp Whoop. Offset and we can put in minus seven. There we go. We've now adjusted that and

**Dave Jones:** if we go temp show, it should give us 28°. There we go. Spot on. Recalibrated. No worries. And I guess, folks, that is why they give you a multimeter and a separate thermometer with this thing, but how accurate it is, I don't know. I

**Dave Jones:** don't think it's going to be as good as my Fluke and my Agilent one. Well, let's try this cheap ass multimeter. Shall we see what it tells us? Eh, 26. Not too bad. Only 1° C resolution though. All right, I've let it all

**Dave Jones:** settle down and I've come back what, the next day? Actually, it's the next morning and uh 25 26° C. So, it's pretty darn close and my Fluke and my Agilent uh probes are bang on to within 0.1°. So, I'm pretty confident with that. Um

**Dave Jones:** so, what I'm now I'm to do is ramp up the temperature in the uh learning mode and just see if the uh temperature at a higher temperature thermocouple in there matches the multimeter. So, let's give that a go.

**Dave Jones:** Got some Kapton tape there and I've got my uh Agilent thermocouple probe taped into uh a hole next to so they're both making contact uh into holes next to each other on the board. So, basically the same thermal mass. So, we should be able to

**Dave Jones:** now track the temperature more accurately with our reference board in the oven with our Agilent meter. And you can see they're basically tracking pretty precisely now. I really like it. So, I've got pretty darn good confidence with this thing now in terms of being

**Dave Jones:** able to actually track the real temperature. And also what I've got is the Bluetooth module connected to my Agilent meter here and the data logging app. So, we'll be able to actually see profiles and stuff with our reference

**Dave Jones:** temperature thermometer. Beauty. So, now what I'm doing is uh logging the temperature in learn mode. So, we should see it go up to 100° uh C here cuz that's what learn mode does. Goes to 100°. It follows the ramp, it times it,

**Dave Jones:** and all that sort of stuff. And uh it should switch off. We were well off before because we weren't connected to the same thermal mass. So, here we go. So, it got up to 135° in learn mode and switched it off and as

**Dave Jones:** you can see it is uh slowly starting to just uh ramp back down now. Cuz the element's off. So, there we go. We can actually see the ramp on that thing and uh look at that. It's a really nice

**Dave Jones:** curve. I like that. Uh I just read the instructions for this uh learn mode and what it does is it uh once it reaches 100° C, it actually switches off the uh element and then what it does is it

**Dave Jones:** continues to track uh you know, and and learn uh how long how long it overshoots basically over that 110° or 100° uh C. So, that's what's it it's effectively learning there how much it overshoots when it switches the element off. So,

**Dave Jones:** there's 100 Where is it? There's 100° there. So, it switched it off at that point, would have switched off the element there, and you can see that it's overshoot. Oh, like that. Oh, I've zoomed in. There we go. But, uh so, it

**Dave Jones:** and so, it looks at that part of the curve there, and now it knows how much it overshoots. So, I don't know. It applies it to some sort of intelligent algorithm so it can now control the oven presumably safely. So, let's try this

**Dave Jones:** again in reflow mode. All right, I'm going to start it again. I'm going to do the full temperature profile, and we'll see what we get cuz all we care about is what's actually on the meter. So, push the solder button, and uh

**Dave Jones:** here we go. Okay, so what I've done is I've set my uh reflow temperature to 230° uh here. I've actually programmed in that. So, we should expect to get a maximum of 230° C on here. So, we're looking and I can

**Dave Jones:** log the data with the serial command here as well. So, I'll go What I'll do is I'll go temp show, and then 1 second, and what it does is it will every second it will just display new temperature

**Dave Jones:** there. So, we can uh keep that running, and I'll start my uh login on the multimeter, and I'll do on the uh login app, and I'll press solder, and away we go.

**Dave Jones:** Now, as you can see, we've reached 240 241 there even though it's set to 230. So, we have you know, as you know, a significant amount of overshoot there. Not dangerous by any stretch. It's still within the you know, the thermal reflow recommended

**Dave Jones:** profile of this thing. So, that's not too bad actually, especially given that you know, this is a very small thermal mass board. So, I'd be tempted to actually leave it at that because you know, like a a component in

**Dave Jones:** my micro current for example are maximum recommended 250°. So, it's certainly under that. And when you put larger thermal mass boards in there, you'd expect a slightly lower temp. So, I think that's pretty much ideal. Now, it's it's still in the reflow stage. And

**Dave Jones:** it's still uh got the heater switched on. But, what? No. There we go. It's just switching off and on now and we're into dwell mode now and we're continuing this thing. But, yeah. I I think that's that's pretty optimum. It didn't It's not over

**Dave Jones:** shooting to dangerous levels. That's really all you care about and one of the real dangers of not having a proper reflow controller on your oven. If you're just using the regular oven for be careful. You can see the profile there and you

**Dave Jones:** can see the three stage step there and that's exactly what they intended to do and that's exactly what you need for the profile. So, it's not bad at all. Now, we're up to the 10-minute mark here now and that is taking a long time to ramp

**Dave Jones:** down. So, I haven't opened the door. So, at this stage we probably want to well, when it's actually done and goes beep, you probably want to open the door to ramp it down much quicker than that because if you have a look at

**Dave Jones:** the recommended profile for the paste. I mean, you know, there's no way our little piss ant oven here can A ramp up that quick and B ramp down that quick as well. I mean, we're only talking, you know, 300 seconds there.

**Dave Jones:** So, you know, really probably best to just open the door at this point. So, there you have it. There's the beta layout reflow oven kit and I really do like this controller. It works quite well. So, I'm pretty happy with it. Very

**Dave Jones:** confident now with that thermal profile that the boards I whack in here will work and no doubt you'll see future videos on this where I assemble the micro current and other boards as well. Oh, look, it's Dick Cheney.

**Dave Jones:** Sorry, Australian joke. So, you can get by with just a regular oven setting it at 230 doing timing. You can do similar thermal profiles to this to make sure it works and stuff like that, but I really like this controller. I think it's

**Dave Jones:** probably worth every cent. There's lots of other controllers on the market too. There's open source hardware ones and things like that, but yeah, this is quite neat. So, pretty darn happy with this. I'll make a little dedicated location for this and I've got myself a

**Dave Jones:** pretty useful thermal reflow oven now, which is, you know, pretty darn good. I mean, you know, it's not professional grade, but hey, you know, it can still do pretty decent quality boards in it without damaging components cuz now I've thermally

**Dave Jones:** profiled it, know exactly what it's capable of. It's not going to go over temperature. It's not going to damage my parts. Can be pretty damn confident in it. Beauty.

**Dave Jones:** Catch you next time.
