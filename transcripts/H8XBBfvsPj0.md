---
video_id: H8XBBfvsPj0
title: EEVblog #1282 - Design Your Own Membrane Keypad! (µSupply Part 20)
url: https://www.youtube.com/watch?v=H8XBBfvsPj0
source: youtube-asr
---

**Dave Jones:** Hi, if you've got a sexy new product idea you're developing or heck even if you've just got a prototype or a short run production run that you want to do and you want to make it sort of like customy

**Dave Jones:** and more professional. In this case we've got the new micro supply here and I've done videos on actually designing custom LCDs like this as well as custom heat sinks that are inside this thing and I'll link those videos at the end and down below

**Dave Jones:** if you haven't seen them. But in this video we're going to take a look at doing custom keypads like this because doesn't that really make the product look like you know, really sexy and professional. Nice splash of color, low

**Dave Jones:** profile and it just looks and feels gorgeous. And you might think that a custom keypad like this is like super hard to do and expensive and you don't know where to start. Well, in this video I'll show you that it's actually really

**Dave Jones:** very simple to do and relatively cheap and easy these days. By cheap I mean for as little as a couple of hundred US dollars you can get like a handful of these prototyped and in volume like they're only like a dollar or two or

**Dave Jones:** even sub one dollar depending on your particular requirements and the particular technology that you've got used in these things. Of course the price does scale with the size of it. This one's only like 58 mm by 45. Of

**Dave Jones:** course if you want a large one that goes over your entire product with clear LCD windows and all sorts of stuff like that. You pay more for the material size and it's got the good stuff or the genuine 3M material. Hang on, let me

**Dave Jones:** have a sniff. Oh yeah, that's the good stuff. So these are completely custom designed in this case to the requirements we had for the micro supply, the key layout, the key shape, the colors, even the pressure of the contacts as we'll go into, the type

**Dave Jones:** of contacts, the pitch of the connector, the length, the placement, and everything about this is entirely custom, and it's really easy to do. So, as we say here on the EE blog, don't turn it on, take it apart, and here it

**Dave Jones:** is inside. Let's show you what's actually inside one of these ones. Well, that's still sticky. What we've got here, there's basically three parts to this. The first one is this flex uh PCB. And this is just like any other flex

**Dave Jones:** PCB. I've done a video on how to get flex PCBs manufactured. As you can see, this one's actually a double-sided one. These traces here, these copper traces are on one side, and you flip it over, and there's the copper traces on the

**Dave Jones:** other side there, and they all go down to the connector at the bottom. It's got a bit of stiffening piece on the connector there. I'll show you that up close. And they will usually add that because it just adds a bit of rigidity

**Dave Jones:** when you're putting this into the flat flex connector on your PCBs. There's absolutely nothing special about this, and yes, you can actually get these just manufactured yourself. You can lay this out in your favorite CAD program, and just send it away to a PCB manufacturer.

**Dave Jones:** And you could do that if you had some special requirement, or you wanted to reduce costs, or, you know, do something weird that your particular favorite manufacturer of keypads can't do. For example, you might want to get this made

**Dave Jones:** yourself. And that brings us to the second part here, which is the vinyl decal. Now, this is a poly put the kettle on type material. They generally come in two types. Either a polycarbonate is the most common, or a

**Dave Jones:** polyethylene type. And whether or not this material is polyester type, or a polycarbonate type, really depends upon your requirements. And really, if you've got specific requirements, talk to your specific manufacturer to see what is the best one they recommend cuz there could

**Dave Jones:** be, you know, differences between manufacturers. But in general, if you're after super low cost, your polycarbonate is probably going to be the cheaper material, but your polyester type material is going to have a much longer wear life, especially on the non-tactile

**Dave Jones:** versions. As we'll take a look at, this is a tactile one, but non-tactiles, you know, you get up to like 100 million operations or something insane on those. If you're talking about ESD susceptibility, like through the keypads, people rubbing their shoes,

**Dave Jones:** walking up to some terminal or something going zap, then polycarbonate, well, polyester's technically better, but I think polycarbonate's available in like thicker sheets and stuff like that. So, you know, technically you can get it to a higher voltage ESD voltage rating

**Dave Jones:** in polycarbonate, perhaps. And in terms of you know, physical abuse and wear and things like that, polycarbonate might have the edge depending on, you know, the type of finish and all that sort of stuff. So, you know, it it varies a lot,

**Dave Jones:** but generally, if you want embossed buttons, as we'll go into, the raised ones, which you will, as we'll have a look at, then polyester's, you know, probably the go cuz it's going to be less brittle. So, it's going to have a

**Dave Jones:** longer life with embossed buttons, generally speaking. But yeah, it's basically a decal and the more colors you have, generally when you as we'll see shortly when you go to quote for these things, you'll pay for however many colors your overlay has. In this

**Dave Jones:** case, we've got white, which will be a color, black, we've got blue, we've got gray, and yeah, that's it, four colors. Now, membrane keypads like this come in two different types, either tactile type or non-tactile. These are tactile type

**Dave Jones:** because as you can see in here, these are little tactile metal domes in there. And you can actually buy these separate. In fact, I have a whole bunch of them. Now, these here actually come from a company called Snaptron, and they're one

**Dave Jones:** of the industry leaders in these little tactile domes. You can see they come in various sizes. This is like 0.22 in. Two things you're after is the size, i.e. the diameter, but they're not always round, the shape, and the trip force.

**Dave Jones:** This is 170 g. So, it requires 170 g to push down on that using a point source, or your finger, or however they specified. I believe Snaptron specify it with like a 1 and 1/2 mm diameter and run rod or something like that. And they

**Dave Jones:** come in various shapes like this. This one This one here is quite similar to what we've got in the micro supply keypad. There's a little, you know, three-sided thing. That's another four-pointed arrangement. Another one there. Then we get over to these absolute tiny ones

**Dave Jones:** here. Look at this 0.15 in diameter circular one. That's really absolutely tiny. And I got these when I was developing my micro watch. These are various samples so I could, you know, just have a look and see how small I

**Dave Jones:** could make a keypad. And I think at the time this was like the smallest one they offered, I think. So, you know, really tiny stuff. But they're all little tactile domes that just snap down. So, here's the one inside the micro supply.

**Dave Jones:** I've taken it out and flipped it over cuz they're usually flipped up the other way. And you notice that'll just go snap like that. Just snap down. It's really quite satisfying. It's brilliant. And they snap back. Just want to see that up

**Dave Jones:** close. Look at that. There we go. They snap down like that. And you'll notice that these side bits actually do pop up. Now, these actually can be a PCB reflow soldered onto a front panel or something like that. They don't have to

**Dave Jones:** be integrated into these poly put the kettle on type deco systems like this. You can actually get them in specific manufactured like a strips to your orientation like your spacing and key layout and things like that that you put

**Dave Jones:** over your PCB. But this is the most common technique is just to have them inside a little cap out there. So this is what's called a tactile membrane keypad because these are tactile domes. So you would choose one of these tactile

**Dave Jones:** dome keypads when you want a positive click that gives like a sensory feedback directly to the person. So you know if that if you push down on that and you can feel and hear the click in it, then

**Dave Jones:** you know that you've made contact in there. So you know, you don't need any visual or audible feedback in terms of like a beep beep. These ones have what's called embossed keys. Once again, I'll get the macro lens out and show you that

**Dave Jones:** these are all slightly raised up. This is probably going to be hard to show cuz this one is only very slightly embossed upwards. But yeah, we need feel a vision. When somebody going to invent that? Anyway, yeah, they

**Dave Jones:** are very slightly raised because you obviously have to have room in there for that little low profile tactile dome to go. Now you don't have to get embossing. You can actually just put the deco directly over the tactile domes and have

**Dave Jones:** it flat and that will actually be a cheaper solution. And in some cases that's better to go with, but it it's just much sexier to have this embossing cuz you can feel it. Once again, it's not feel a vision, but you can feel all

**Dave Jones:** those keys are raised up and it's just uh it's really quite nice. So as I said, the The you want to specify with these keypads is the force required to actually push these buttons down and that's always specified in grams. None

**Dave Jones:** of that non-metricated Yankee rubbish. And there are countless permutations and combinations of this sort of membrane technology and one of them is to not have the tactile domes actually embedded inside here, but actually have them on the PCB of your product. You've seen

**Dave Jones:** this product in the mailbag before. It's a data logger type type thing. It's got one big I guess you don't call this a membrane keypad, but you would get it from the same manufacturer who does the same thing. We've got a key embossing

**Dave Jones:** here this so you can physically feel those keys which highly recommended. It just you know it it just adds to the professional feel. It's got a clear window on it for the display. It's got you know transparent windows up here for

**Dave Jones:** the LEDs for example, but this doesn't have a tactile dome in it. You can hear that click. But that's not inside the membrane. It's just on the back of the PCB that a regular tactile dome switch that just

**Dave Jones:** happens you engineer you know your standoffs and everything to be exactly the same height and you just integrate that into your product. So you know there's more than one way to skin this cat. So the way these work is pretty

**Dave Jones:** obvious. It's just a your regular matrix keypad array and then the tactile dome just sits on the top there. There's those two contacts the outer one and the inner one and they each go to a different part of the array and then

**Dave Jones:** when you click down on that it whoop makes contact between the outer pads and the inner pad. So this is very similar to how like calculator keypads I've done a ton of tear downs of those. They will work either with in really good quality

**Dave Jones:** calculators they might use a tactile dome, but that's fairly rare. Generally they will use a rubber button with a backing of like conductive carbon on it and then the the will come down and press on those pads, but they wouldn't

**Dave Jones:** have this arrangement. They generally have like lots of crisscrossed lines like that intertwined. But because we do actually have a specific point in the center of that dome that will actually go down and contact that center bit. So

**Dave Jones:** that's how your tactile dome switches work and they're quite nice. They're not as reliable however as the other method. They don't have an infinite life. They will have a rated cycle because you are flexing These are generally like

**Dave Jones:** stainless steel. Half a million, a million operations, you know, the really good ones will have it like be rated for a couple of million operations, but they will eventually wear out. And by the way, the characteristics of these will

**Dave Jones:** be different if you have them reflow soldered onto your PCB because you can see when I press that, then those little corners actually flip up. But if you've got these four corners, these four pads here soldered down to a PCB, then

**Dave Jones:** there's going to be less Well, there's going to be no give in that. The tactile response to these can be quite different. So the life of these can be quite different whether or not you've got them reflow soldered to a PCB or

**Dave Jones:** whether or not you've got them just you know, loosey-goosey in there inserted inside this where it's upside down or the electrons are going to fall out where it's actually just free in there to be able to like move those little

**Dave Jones:** outer arms like that. So yeah, this one's probably going to have a longer life. But in any case, these tactile domes will not have as good a life as the next type which is a non-tactile type. Yes, copyright 1980. We have to go

**Dave Jones:** back to the future 40 years back to find an example here in the lab of the next type which is a non-tactile keyboard. This is the classic Sir Clive Sinclair ZX81 although it's the rebased Timex Sinclair 1000. And if it's good

**Dave Jones:** enough for Sir Clive Sinclair, it's good enough for you. Or if it's cheap enough for supply of Sinclairs cheap enough for you, um this is a mem- this is a non-tactile membrane technology, and you've seen these in teardowns before.

**Dave Jones:** So, what it is is just two flat flex PCBs like this, the traces on one side, traces on the other, and then they just sandwich together like that. There is no, trust me, feel the vision, there is no tactile feel in that. All you can

**Dave Jones:** feel is a tiny little hole in the middle of it. When you depress it, you can feel that you're sort of like going into a depression. There is no give on that at all though. It's it's absolutely horrible these things, but they are dirt

**Dave Jones:** cheap cuz they're literally just two flat flex mylar uh type sheets like that, and then you just got the contact on the top and bottom, and then when you there's a like a tiny little gap between them due to the thickness of the

**Dave Jones:** material, and when you depress it on a hard surface like that, it makes contact. And these are ridiculously reliable. So, if it's reliability you're after, you want uh a non-tactile one like this over uh your tactile dome ones

**Dave Jones:** cuz the domes will eventually wear out, but there's no nice feel in these. So, you need uh often use a feedback in terms of a beep or uh you know, a LED turning on or flashing or something on

**Dave Jones:** the screen or something like that to tell you that you've actually pressed a button. Otherwise, you just wouldn't know it. There's actually um two ways to do this. One is like I've shown here. You have a top and a bottom sheet like

**Dave Jones:** this with contacts top and bottom, but you can actually do it um just like this with the one membrane sheet like this, and you once again, you wouldn't use this uh land pattern here, this pad pattern. You would use like a uh

**Dave Jones:** an interconnected uh one like that, but you can actually have on top of your sheet up here, you can have a conductive material be it like, you know, silver or carbon or something like that conductive on top so that when you press down on

**Dave Jones:** it, it just presses down on the two contacts. And that's common in you know, pocket calculators and things like that. Even these things, as I said, quite cheap. Anyway, let's go to the videotape and see how cheap and how you actually

**Dave Jones:** design one of these and send the files to the manufacturer. So, how do you design one of these? Well, turns out it's really easy. You can use practically any package you like. Oh, you don't even have to use a

**Dave Jones:** CAD package. You can just do it on like a napkin sketch and take a photo off your phone and send that to them and they'll pretty much take anything as long as they can get the general gist of

**Dave Jones:** what you want. So, in this particular case, we've used Inkscape here, but really it can be anything. They accept it in like a one-to-one PDF drawing, DXF and like any sort of like format almost that you'll give them. We'll have

**Dave Jones:** a look at that in a minute. You do it in You just have to get across your intention. Now, in this particular case, you don't have to go to this sort of detail, but we've basically got panel down the side here. It says our

**Dave Jones:** dimensions, what type of tactile switch we want. Now, we could actually specify a particular Snaptouch dome or other brand dome or something like that. But in this particular case, we weren't that fussy. We just like give us whatever

**Dave Jones:** dome you've got cuz that'll be lower cost. A lot of manufacturers, they might only supply their own domes, but the good ones will be able to source and use a particular dome that you like. Now, pillow embossing means that you've got

**Dave Jones:** the nice rounded edges like this up here on the keys and they'll actually emboss it rather than just like a square and then print the round because they can print whatever you want, of course, and that's no extra cost. But to actually do

**Dave Jones:** the round embossing may actually cost more. It did a little bit more. It depends on the manufacturer really, but and then the back in it can be a particular type of particular 3M model number as we'll look at shortly or just

**Dave Jones:** leave it up to them. It doesn't matter. Yeah, we want to tactile dome or we want polyester and a matte finish. You can get either matte or gloss. I don't like gloss anything. Gloss PCB solder mask. And you don't need to put operational

**Dave Jones:** temperature range and stuff like that. And the connection method we've got we specifying a 0.5 mm pitch. And then we've got some expanded detail here of exactly how to manufacture this and you'll generally get this from the data

**Dave Jones:** sheet of your particular surface mount flex connector that you're actually using. You know, the thickening of the back in stiffener here 0.3 mm. But you don't really have to know like any of this stuff. You just get it from like

**Dave Jones:** choose a connector, get it from the data sheet or simply leave it up to them. Or if it's 1 mm pitch flat flex connector, almost any 1 mm pitch flat flex PCB connector is going to work. Yeah, you

**Dave Jones:** can leave it up to them or you can specify down to the most minute detail. And if you're you know, designing an fruity Apple gadget or something, yeah, you're going to want to do that. And we've got you know, pretty exacting look

**Dave Jones:** and feel here of exactly what we want. And really they might take it from this drawing or they'll simply redo it in whatever local CAD package they've got. And then we've got just the key spacing detail and the dimensions and you know,

**Dave Jones:** like the real actual look and colors. Although we have specified the actual Pantone colors down here. 3005C is the official EEVblog blue by the way for those wondering. And it just helps. You don't have to include a schematic like

**Dave Jones:** this, but you got to include some sort of pinout otherwise they can you can just tell them like randomly do it and then give me the details. You can potentially put series resistors on here. Now I haven't done a video on

**Dave Jones:** carbon printed resistors on PCBs. You can get those on flex materials as well. And there could be various reasons you might want to print resistors on there and one of them might be because you don't have the number of pins over here

**Dave Jones:** to actually do it. You might only have a single pin on your microcontroller. In that case, you can actually do the array matrix using an analog-to-digital converter. A single ADC pin on your micro, you can have different value

**Dave Jones:** printed resistors depending on which key you press. It'll give you a different resistor divider and from that you can work out the voltage and you can have a mapping in software and things like that. We won't go into details. Do a

**Dave Jones:** video on that one day. Our resistors are in here but we didn't actually get them carbon printed. So that's it from the design point of view. I mean, you don't even have to go to this sort of detail

**Dave Jones:** but this is kind of, you know, professional and what you'd expect. If you're working for a company, you'd have to develop, you know, at least some sort of like data sheet like this. Effectively, what you are making is a

**Dave Jones:** manufacturing data sheet. So if you've got a manufacturer in mind as we'll check out in a second, then you can actually steal all the information of what type of 3M material to use and what type of embossing and all that sort of

**Dave Jones:** jazz. Just steal it from the website and incorporate it into your drawing. So the company we got ours manufactured from is not this one but I just found this website and I think it's cool because it's like getting a shopping

**Dave Jones:** cart type thing process like you used to for your PCBs and I've done many videos on that. Often there's not much difference in price between getting five made and 500 for example cuz most of the cost in that is like the tooling or NRE

**Dave Jones:** or non-recurring engineering charges as they say in the biz. Anyway, this company, I haven't used it before. I just found them and I thought it was cool because it's the first time I've seen a shopping cart system. They've

**Dave Jones:** probably been around for years. There's probably lots of companies that do this. So let's actually go into the quote for membrane switches, shall we? So you're probably very familiar with this for getting your PCBs manufactured. You can basically do the same thing for overlay

**Dave Jones:** graphics, membrane switch keypads. Absolutely great and they give you a real-time costing. If you're aware of other websites that do this, I haven't even bothered to look. We want a 50 mm by 50 mm keypad that's close to what

**Dave Jones:** we've got in here. Oh, yeah, let's go. Millimeters, none of that inches rubbish. And we only want five of them, for example, but they'll go up to 3,000. You can just get one, but let's get like five. Now, material, uh PC polycarbonate

**Dave Jones:** or uh PET, that's your polyester type. And the good thing is they've got little uh pop-up help things here. So, we'll choose uh the polyester, none of that glossy surface rubbish. No, uh evil. Should be eradicated from the planet. Um

**Dave Jones:** all of the different specific 3M model number types, and you can probably go look up the data sheets on the 3M website. It's got you know, different uh temperature, transparent, white, translucent, transparent, blah blah blah. Uh you can choose an IP66 rating.

**Dave Jones:** Um that'll have like a better ingress uh protection in the uh glue, the backing glue, and things like that. Uh material thickness, it looks like they don't have a choice there. Uh once again, this is a company that just manufactures,

**Dave Jones:** specializes in manufacturing prototypes. You probably can go to them with your data sheet. Um they might be able to do more custom stuff for you, but you have to ask. Total thickness, about 0.9 to 1.3. Like, yeah, these are prototypes,

**Dave Jones:** you know, not exacting requirements. So, if you're manufacturing your fruity Apple gadget, then uh yeah. Color, let's say we've got four colors quantity here. Um top embossing. Now, one of the other things is look, this company offers um

**Dave Jones:** integrated LEDs inside the membrane switch. And as I said before, because this is a a flex PCB, you can do almost anything with it. You can get uh surface mount components actually laid and embedded on these things, and then the

**Dave Jones:** graphic goes out with a little cutout in the graphic to go over your components. So, they're all embedded inside there, so you can embed LEDs in there, you can embed uh components, chips even, uh caps, and all sorts of stuff. You could

**Dave Jones:** potentially have your entire product embedded into the circuitry of the flat flex keypad. If your product is like one of those little credit card thin pocket calculators or something, you could have everything embedded in there. Like a Now, the key type here, they call it die

**Dave Jones:** pressing. But that's basically non-tactile. So we got 20 because you'll pay per key. They're not free. Do we want an LCD window or not? And once again, you can get various treatments for the LCD window. Like they can do an

**Dave Jones:** extra process on it where it like really makes it translucent and things like that. But no, we don't have one. So we can have a look at how all this sort of stuff affects the cost. Now we can

**Dave Jones:** choose laser cutting or mold cutting. Laser cutting's going to be cheaper because they don't have to do a mold to stamp them out. But a mold will be more accurate. So and it'll be a cleaner thing and stuff like that. Gloss window

**Dave Jones:** with a matte surface for example. So you can have a glossy overlay which I don't recommend and with a matte finish LCD. So they combine these things. This is great for like just prototyping. They offer all this sort of stuff. It's fantastic. And a

**Dave Jones:** light color background. Not exactly sure what they're getting at there. There's a like an info panel. You There you go. They've got 20% gray, 10% gray, that sort of stuff. And then you can also add an electrostatic shield for ESD and

**Dave Jones:** stuff like that. So they'll put that in as an extra ground layer and typically connect that through to a pad. But if you wanted that, you'd typically specify that on your engineering drawing. Tell us the price, son. All right. 254 Yankee

**Dave Jones:** bucks to the production type. That's like the tooling in the non-recurring engineering. The mold cost for $30 for the embossing. But the actual units themselves, five of them, only cost $16. So and film cost as well. That's just

**Dave Jones:** yeah, like negatives. It doesn't cost much. They come out of a big laser Uh uh machine. It's dirt cheap. Man, when I was a boy, ah unbelievable. And they'll do this in 48 hours turn time, unless it's the, you know, Chinese uh New Year

**Dave Jones:** and um the coronavirus and all that sort of stuff and delaying things. I don't know where they're based. Play around. Uh does glossy surface cost any more? 251. Matte surface costs a couple of bucks more for a matte. Is polycarbonate

**Dave Jones:** any cheaper? Polycarbonate's a little bit cheaper but as I said, like when and when you're talking about really, you know, Apple fruity type product volumes, um like polycarb's going to be uh generally much uh cheaper. Um so, there's trade-offs there. Couple of

**Dave Jones:** bucks extra for your IP66. Material thickness, does that change anything? No. Uh color embossing, let's go let's say we had 10 colors or something. We want the original Apple logo uh to show up, then 458 bucks, right? Like you're

**Dave Jones:** almost doubling your price for the color quantity. Let's go down to one. How does that change it? 200 bucks. There you go. And don't put like 256 colors or something. So, do they even allow that? No. 25 different colors.

**Dave Jones:** No, bugger off again. 15 different colors. Yeah, they'll do 15 cuz it's a different process manufacturing process for each one. So, yeah, like there's a limit how long you can tie up their production line. If we don't do embossing, you

**Dave Jones:** know, it's not a huge amount extra for embossing uh really. Let's say we had 10 different LEDs on there. 339, so that increases it quite substantially. And if we remove our metal domes here, it's not much extra cuz we've already uh done the

**Dave Jones:** embossing of the keys. Cuz you can have embossing of the keys with no uh snap dome under them if you want. And if we go from 20 keys, we've got a big keyboard, we've got 50. It it's not a

**Dave Jones:** huge amount extra. They're not charging so they're they're getting those um tactile domes for cents each. But if you want the good quality, you know, like the proper specified Snaptron domes or something, they can actually be quite expensive and add up if you've got a

**Dave Jones:** large keypad. But, if you want a specific guaranteed look and feel and things like that rather than just whatever one they provide, they might be able to provide a data sheet for their particular one. Don't know. Do we want a

**Dave Jones:** window? Yep, looks like it's an extra like 20 bucks for a window there. Mold cut in. Oh, yeah, okay. So, you're paying for your mold extra 90 for your mold. But, if you want a cleaner more accurate cut, then yeah, it's not a huge

**Dave Jones:** amount extra. Add the electrostatic shield, uh, an extra 50 bucks for your electrostatic shield. Presume we have to go to a four-layer flex. So, there you go. That is very cool. And as I said before, if your switches are mounted on

**Dave Jones:** your board for example, you can just do like a graphic overlay. Uh, you don't actually have to have a membrane uh, keypad. And they do acrylic panels as well, which is uh, really neat. Wow, it's fantastic. Once again, when I was a

**Dave Jones:** boy, and just out of interest sake, uh, here's their manufacturing acceptable uh, files and things like that. They're a prototype manufacturer, whereas like your larger key switch manufacturers, they'll do absolutely anything you ask them to do. They'll bend over backwards.

**Dave Jones:** Uh, CAD, CDR, AI, and PDF formats. PDF is one-to-one as I said. They'll accept uh, CorelDRAW, uh, AutoCAD, Adobe Illustrator, you know, things like that. Or as I said, like a napkin sketch. They'll they'll happily take that. Uh,

**Dave Jones:** they actually suggest a Pantone Pantone colors, uh, things like that. And look, they give you nice detailed uh, requirements of So, there you go. We'll leave it there. This video's been long enough as it is. And you can see

**Dave Jones:** how easy and relatively cheap it is to manufacture your own membrane switch keypads. And hopefully this video's given you the confidence that this is, you know, a a normal thing, just like getting a PCB made. Whereas, you know,

**Dave Jones:** 20 years ago getting your own like custom PCB made was uh, like a big deal. Now it's like your grandmothers doing it. And the same thing with their custom membrane uh keypads. So, even if you're doing short-run prototype uh

**Dave Jones:** proof-of-concept, you've got a startup and you want like like a really cheap uh you know, proof-of-concept prototype to show off to the investors, or you got you know, you just want to do short-run uh stuff and sell them

**Dave Jones:** yourself. I've done a video on selling your own hardware and things like How many videos do I have to link into this one? Unbelievable. Anyway, hope you found that useful. If you did, please give it a big uh thumbs up. And, as

**Dave Jones:** always, you can discuss down below and check out my uh library channel at eevblog.tv. Catch you next time.
