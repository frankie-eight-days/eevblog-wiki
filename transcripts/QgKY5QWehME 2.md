---
video_id: QgKY5QWehME
title: EEVblog #1037 - Solving Ceramic Capacitor Cracking
url: https://www.youtube.com/watch?v=QgKY5QWehME
source: youtube-asr
timestamps: {"0": 1, "1": 16, "2": 32, "3": 43, "4": 59, "5": 77, "6": 92, "7": 107, "8": 122, "9": 136, "10": 152, "11": 167, "12": 183, "13": 197, "14": 211, "15": 228, "16": 248, "17": 261, "18": 274, "19": 290, "20": 303, "21": 316, "22": 330, "23": 344, "24": 359, "25": 371, "26": 381, "27": 397, "28": 408, "29": 422, "30": 436, "31": 448, "32": 463, "33": 476, "34": 491, "35": 502, "36": 514, "37": 529, "38": 545, "39": 561, "40": 575, "41": 590, "42": 605, "43": 617, "44": 628, "45": 643, "46": 659, "47": 672, "48": 686, "49": 701, "50": 714, "51": 727, "52": 741, "53": 753, "54": 767, "55": 780, "56": 795, "57": 806, "58": 822, "59": 839, "60": 850, "61": 865, "62": 877, "63": 888, "64": 902, "65": 915, "66": 931, "67": 945, "68": 962, "69": 981, "70": 998, "71": 1012, "72": 1030, "73": 1047, "74": 1061, "75": 1074, "76": 1088, "77": 1104, "78": 1117, "79": 1132, "80": 1147, "81": 1162, "82": 1176, "83": 1187, "84": 1207, "85": 1222, "86": 1241, "87": 1260, "88": 1275, "89": 1292, "90": 1309, "91": 1321, "92": 1336, "93": 1349, "94": 1364, "95": 1376, "96": 1390, "97": 1403, "98": 1417, "99": 1432, "100": 1446, "101": 1462, "102": 1474, "103": 1490, "104": 1504, "105": 1518, "106": 1531, "107": 1548, "108": 1564, "109": 1581, "110": 1596, "111": 1609, "112": 1624, "113": 1638, "114": 1650, "115": 1667, "116": 1678, "117": 1690}
---

**Dave Jones:** Hi, in a previous video we took a look at a fire of a multi-layer ceramic capacitor inside a power supply module. And this is actually the second time this has happened to me as I pointed out in the previous video where the ceramic

**Dave Jones:** capacitors have actually failed short circuit and they've been across a high power source which has been able to deliver a lot of energy into that capacitor and they catch a light and needless to say that can ruin your day.

**Dave Jones:** Um in if you're designing a product like this. So quite a few people have asked and I thought it's quite worthy to do another video on this actually looking in more detail of exactly what's happening here and more importantly what

**Dave Jones:** you can do to either reduce your chances of this happening or basically eliminated almost entirely any issues in when you're designing a product cuz this is one of those more obscure things that you're not going to learn in school.

**Dave Jones:** This is like real manufacturing practicality stuff. So it's really fascinating. Let's take a look. So you can see in the photo here are the before and after. Before we had a multi-layer ceramic capacitor in there soldered between two pins and that was the

**Dave Jones:** mistake here. Pins that have big screw terminals on them. So when you screw in those terminals on the other side of the board you get transfer of mechanical stress onto these ceramic capacitors and ceramic is actually brittle so they tend

**Dave Jones:** to crack, get micro cracks in them and generally these can fail short circuit and that's exactly what happened here. The capacitor shorted, it dumped all the energy into that capacitor and it caught a light and well, it ain't there

**Dave Jones:** anymore. But there's actually another two ways at least that these capacitors can fail. The other one is by thermally stressing them. You could have one end on a big ground plane or both ends on a big ground plane, for example. On one

**Dave Jones:** end, can matter cuz when your board goes through the reflow oven, then the copper can retains the heat very well. So, if you've got one end of the capacitor, for example, hooked onto a large ground plane and the other one

**Dave Jones:** not, just going off on a tiny trace, that might impart differential thermal differentials, which can also crack your ceramic capacitor. So, it's not as common, but thermal stress is one thing. Mechanical stress, which is what we're going to look at in this video. And the

**Dave Jones:** other is just infant mortality manufacturing, you know, issues caused by the component manufacturer. You know, if you buy them from the Shenzhen market, you don't know what sort of quality you're getting. But even though that even the good quality

**Dave Jones:** ones, there's just a manufacturing bell curve thing. You will occasionally get some outliers that could fail short. And do a similar sort of thing. And I showed this table here of ceramic capacitor fires from NIC Components Corp. And it's a

**Dave Jones:** nice little summary of the different failure modes. Mechanical stress, as we're going to look at here. Thermal stress, as I said. And those intrinsic defects and how to mitigate them. So, that's just a useful table there. I'll have to link in the web page down below

**Dave Jones:** to that one. So, what's actually the problem here with mechanical stress? Well, this very handy graphic from the University of Maryland, their Center for Advanced Life Cycle Engineering. Once again, I'll link it in down below. Shows your multi-layer ceramic capacitor. And

**Dave Jones:** you can see the multi-layers. They Sometimes they can have dozens and dozens or a hundred layers in there inside. You know, especially your really high capacitance ones. Like, people take for granted the 10 microfarad or higher, even 100 microfarad multi-layer ceramic

**Dave Jones:** capacitors. They're very modern technology. And they rely on very tight manufacturing tolerances tolerances with all these different layers of the plates in there separated by the dielectric material. And they can be very fragile. They're encased in a ceramic dielectric

**Dave Jones:** material. And as I said, it can be quite brittle. So, in this case, it's exaggerated, but if you got your PCB and your capacitor's mounted on there, when it flexes like this and the flexion can be due to

**Dave Jones:** uh as we saw in the power supply that failed when you screw in the screw terminals on the thing that can impart not huge stress like that, but just enough. You don't need much. Tiny amount of stress at one end of the capacitor or

**Dave Jones:** both ends and crack um because ceramic is very brittle. And you can actually see the This is a micro cross-sectional photograph. 250 microns. You can see the size there, and you can see it's cracked right through the plates there. And that

**Dave Jones:** one's probably going to end up as an open capacitor, but they so very often fail as a short circuit. If they fail open, okay, your product might fail, but it's not going to catch a light and things like that. But if they fail short

**Dave Jones:** circuit and you've gotten to cross a power supply input or output that's capable of putting a lot of energy into that, it can catch a light. So, nasty. But yeah, this This is what actually happens inside there. And it's very

**Dave Jones:** difficult to actually detect these things. And there's various techniques to do it. you know, cross-sectional cut them. You can actually measure You can do an impedance analysis test like flying probe test on the board and things like that. So, you can get this

**Dave Jones:** board flexion from simply installing the board is one of them. You can get a drop. For example, if you're if you've got a mounting post here and here and your product is dropped, you'll get a little bit of flexion like that,

**Dave Jones:** especially if you got heavy components like a transformer on there or something. Your board might do a flex like that and bingo, you can crack your ceramic capacitors. Nasty. You could also have board plugging connectors, for example. You've got your mounting post here.

**Dave Jones:** You've got your nice big Phoenix contact plugs or whatever. You plug them in after you've installed your board and you can get tiny little flexion on there. You've no doubt seen this on you know, computer motherboards and things

**Dave Jones:** like that when you're pressing the RAM into the thing. You've got to you know, squeeze it. That's putting stress on the board and you can really come a cropper with that. Another way to crack them that you might not think of after you've

**Dave Jones:** had them machine assembled. You may not do this yourself. It might just happen at the assembly factory. When you panelize boards like this, I've done a whole separate video on panelize couple of videos on panelizing boards with routes and slots and V scores and things

**Dave Jones:** like that. If you've got say V score boards and you snap them, snap the boards like out there, you know, you've already assembled them or you can components are assembled on there. Then you go snap the boards off.

**Dave Jones:** That can ruin your day as well. You can actually impart flexion in your board and crack your ceramic capacitors. So, if you've got the slotted out boards like this, trying to push them out with your thumbs, for example, if you've got those

**Dave Jones:** breakout tabs, once again, imparting force. So, that's why it's recommended to actually get the side cutters in there and actually cut out the boards from the panel so that you're reducing the stress on the board. So, let's take

**Dave Jones:** a look at the PCB layout level and see how you can mitigate these sort of problems. And these things might seem obvious, but it's very simple to overlook these when you're designing boards and designing products. Please excuse the crudity of the model. Didn't

**Dave Jones:** have time to build to scale or to paint it. We've got one capacitor on here and a connector and we've got our four mounting posts here. And obviously, if you press the connector on there, that board is going to just flex a tiny

**Dave Jones:** little bit and your capacitor is going to do the same because it's mounted in the middle. What can you do about this? Well, there's several things you can do about this. One is to uh have another mounting hole, for

**Dave Jones:** example. Whoop. There we go. You know, you can have another mounting hole there and it takes the mechanical stress away. So, the first thing is just to stop the flexion happening uh if at all possible, which means extra mounting uh

**Dave Jones:** posts and you know, things like that. Putting mechanical connectors, you can move the connector over to here so that it's near some mounting holes if you didn't want to, you know, have an extra one in here. If you got the flexibility

**Dave Jones:** to do that sort of thing, then that can greatly reduce the uh stress or eliminate the stress on the capacitor. But, let's uh say that you just had it like this. What's another thing you can do? Well, you can simply, like if you

**Dave Jones:** have a look at the uh board here, that's the three-dimensional so that when you you can see that when you plug the connector in there, the board's going to flex a little bit like that when you plug it in and your capacitor is on the

**Dave Jones:** axis like that and that is the most uh you saw in the uh stress photo here, the stress fracture. They happen on the axis like that. So, when the capacitor goes down like that. So, what can you do?

**Dave Jones:** It's easy. You can simply to reduce the stress on the capacitor, rotate it. Like that. So, then you're not on that axis where it's where the solder points are like that and when it flexes like that, if you know what I mean. Uh if you

**Dave Jones:** rotate the capacitor like that, you're not going to get nearly the same sort of longitudinal stress, if I'm calling it the correct uh term, uh on the ceramic substrate. So, it's not going to crack like that. You're just

**Dave Jones:** Sim- by simply rotating that component, you've already greatly reduced the stress on that. So, if there are stress points on your PCB and you can't uh eliminate them for system design reasons or whatever, um you can't put in extra

**Dave Jones:** mounting posts or whatever it is, then simply uh rotating your components can make a huge difference and probably eliminate the issue entirely. So, let's take the uh connector out of the uh equation here for a second and say that you want to

**Dave Jones:** reduce the stress from the mechanical standoffs. You know, when you screw them in and things like that, that could be causing an issue and your capacitor uh for layout reasons has to be right close to your mechanical standoff there.

**Dave Jones:** Well, what can you do about it? There's a simple trick. One way to do it is to add uh mechanical stress-relieving slots into your board like this. So, if we have a look at the uh 3D view, you can

**Dave Jones:** see that we've just routed out a slot in there. Don't worry about the uh little artifact there. Um a slot around your mounting holes like that so that uh less mechanical stress is transferred through the board uh to your components surrounding it, but

**Dave Jones:** it's still provides the mechanical rigidity. And by the way, multi-layer ceramic capacitors aren't the only uh electronic components to be susceptible to stress. If you get a really high-precision voltage reference, uh you'll find that they are um it's quite

**Dave Jones:** common to find them actually surrounded by an isolation slot like this around the chip. They might come in an SO8 package like that. And if you see a slot routed around like that, it means that they're actually uh trying to isolate

**Dave Jones:** any stress, any flexion on the board like that into the chip because uh the mechanical stress can couple into the voltage reference and it can drift and do all sorts of, you know, really subtle things. It's not going to ruin uh the chip or anything,

**Dave Jones:** but it, you know, accurate voltages references like this, thermal expansion of the board can do this, not only isolating mechanical stress, but thermal expansion of the board. The uh FR4 material will have a certain uh value for its thermal expansion. Uh

**Dave Jones:** for example, you can get different PCB materials with different thermal expansion coefficients, and that's a way to isolate our components, but that's got nothing to do with the ceramic cracking and things like that, but you could, if you had to, uh isolate your

**Dave Jones:** capacitor with a slot like that, but that's Yeah, that's pretty extreme. Generally, you want to reduce it using some other technique. So, PCB techniques are pretty simple. One is to stop the stress happening at all, not only in the

**Dave Jones:** PCB handling phase, but also in the product phase. If you've got connectors and screw terminals and other types of things, uh just avoid that happening, or you can reduce the effect by uh mounting holes and just being aware of

**Dave Jones:** where the stress points are in your board. And third is to add uh isolation uh mechanical stress isolation slots where appropriate on your board. And speaking of thermal expansion of the PCB, this can be a real problem on, say,

**Dave Jones:** if you're designing a uh LED board, for example, LEDs on there, um you might have an aluminum or other high-power components. A lot of uh common thing to do these days is to have an aluminum-backed board, uh so that it

**Dave Jones:** can be used as a heat sink uh substrate. Well, aluminum has a thermal expansion constant, and you can get thermal expansion issues on a uh aluminum-backed board like that. So, you've got to be careful with the the thermal stresses.

**Dave Jones:** They're a much higher coefficient than a fiberglass FR4 PCB that you're used to. So, just be careful there. And just some other uh microphotographs here of some uh cracking. In this case, an 1812 multilayer ceramic capacitor. You can

**Dave Jones:** get the cracks running all the way through like that. I just love these. They're beautiful how they can get these photos. They can also show up on um X-rays as well. You don't have to uh cut them in half to actually uh see this,

**Dave Jones:** but you know, you can get pretty horrific stuff inside these brittle ceramic capacitors. The other risk mitigation technique you can do, I mentioned this in uh the video, is that you can put two capacitors in series. Yes, you halve your capacitance, but uh

**Dave Jones:** this increases your liability because if one that does fail short, then uh the other one, the other capacitor is there to take up the slack uh basically. And yes, uh it'll halve capacitance when you put them in series, but then if one fails

**Dave Jones:** short uh in your product, it will still continue to work as long as it can handle the double capacitance cuz you're getting rid of one, so you uh double the capacitance there. So, this is actually a very common technique for high

**Dave Jones:** reliability products, especially if your product if your capacitors are going directly across a power source input or output as we've uh mentioned, but unfortunately, this doesn't help you uh in the case of the capacitors failing open circuit, which they uh most

**Dave Jones:** certainly can. If either of those capacitors fail open circuit due to any of the mechanical or thermal stresses or whatnot, uh or the intrinsic failure of the capacitor, then that's not going to help you. Your capacitance is going to

**Dave Jones:** vanish, but at least your product is not going to catch on fire. So, the way to mitigate that, of course, would be to have two of them and then another two in parallel with that. But that's getting pretty extreme. And another technique is

**Dave Jones:** to simply use smaller size capacitors. The smaller you go, the less uh flexion overall you're going to get for a given unit length. So, you know, some people might have a blanket rule, I'm not going to be use bigger than 0805 ceramic

**Dave Jones:** capacitors, multi-layer ones for example, because um of the extra risk. The larger the component goes, you go to 1206 and then bigger ones, you get some of the real monster-size ones, um then it doesn't take much uh flexion at all

**Dave Jones:** to actually uh crack those. So, the smaller ones, you know, they could be a valid reason for going for those 0402s. Now, of course, another obvious uh technique to eliminate this sort of multi-layer ceramic capacitor shorting problem is to simply not use multi-layer

**Dave Jones:** ceramic capacitors. And sometimes that's an option. You might use a film type. You might use a tantalum or, you know, something else. But multi-layer ceramic capacitors are very popular for the reason that they're A, they're incredibly the volumetric capacitance

**Dave Jones:** per unit volume is incredibly high and they're cheap. They're surface-mountable, everything else. Yeah, they've got downsides. They're microphonic as I've done videos on and they're susceptible to cracking and stuff like this. But they're used for, you know, very legitimate reasons. But

**Dave Jones:** you could in high-reliability products, like directly across the mains, for example, you might use a film type capacitor, you know, your X 2-rated caps, for example. But there is another option. There are companies that actually manufacture multi-layer ceramic capacitors that are

**Dave Jones:** intrinsically safe and certified. Cyfer is one example here. They've got a FlexiCap thing. They're certified for, you know, your X X and Y capacitors go directly across the mains. Once again, they're a high a mains is an incredibly

**Dave Jones:** high energy source, so you want certified capacitors go across there. And they actually offer a range of these certified, you know, they're tested by approved by UL and TUV and everyone else under the sun, rated for directly across these

**Dave Jones:** supplies. And they are multi-layer ceramic capacitors. And they use this using FlexiCap technology. And there's other companies that actually AVX, Kemet, there's a whole range of, you know, almost every legitimate capacitor manufacturer on the planet is going to

**Dave Jones:** offer specific multi-layer ceramic capacitors that solve this very specific problem. So, let's have a look at uh TDK here. They're another manufacturer of uh components that have, you know, this flexy type of technology that can uh help reduce or practically eliminate the

**Dave Jones:** issue here. Now, if we have a look at this, um they've got these uh they put the multilayer ceramic capacitors on what's called a mega cap. They're the lead frames, and I showed this in a previous video. Um and the lead frames on there,

**Dave Jones:** they can actually take the stress. And you can actually see here that uh compared to a regular capacitor, this is the flex amount in the board here, and I'll show you the standard for that in a minute. The flex amount in millimeters

**Dave Jones:** compared to uh the cracking in the thing. And it needs like they start cracking at like 4 mm uh flexing and things like that, whereas using this technology here with these just these adding these little lead frame uh things

**Dave Jones:** in, then you can basically get up to 10 mm of flex in the board with no cracking whatsoever. However, and there's actually a uh standard for this. It's um AEC uh standards, an automotive electronics uh council Q200 005 is the

**Dave Jones:** specific one for flexion of the board here. And they like the supports like this are 45 mm out. This is the standard when they talk about flex uh generally that it can survive, this is what they're talking about here. So, you

**Dave Jones:** know, a little weight comes down on the supports and how much they flex by. And that's um how much they can actually uh survive flexing. So, just mounting that alone can practically eliminate all of your issues here. And here you go, the mega

**Dave Jones:** cap features exorb stress of the board flexure by its unique metal frames, can be mounted on aluminum circuit boards, beauty, uh provided with metal caps uh that exorbs the stress caused by mechanical shocks and uh flexure. It's not just uh shock. Also features

**Dave Jones:** improved vibration resistance as well. Um they can So, they're that's talking about microphonics there. They might be able to reduce or change the resonant mode of the microphonics if that's a problem. And you can get more capacitance because you

**Dave Jones:** can physically stack them with these lead frames and they got lower ESR and ESL etc. But yeah, there you go. So very common in automotive applications. And another type if you don't want to use those lead frame types cuz that's extra

**Dave Jones:** process that might cost money whatever you might might not be able to afford the height whatever. Um, is to use these soft terminations. You can see in this particular case all the manufacturers will have their own technology and ways

**Dave Jones:** of implementing this but they actually have a a conductive resin layer inside there. So that actually takes the stress decouples the stress from the mechanical end caps to the ceramic dielectric. Yet it still allows the conduction through. So it is really quite neat there. And

**Dave Jones:** you can see once again they can flex up to 10 mm with these soft termination technology. It's not going to cause a problem. Beauty. And you can actually see here it doesn't stop these things cracking but what it does you can see on the left

**Dave Jones:** hand side here is your traditional multi-layer ceramic capacitor and you can see that there's a big stress crack right through there. It's horrible. The soft termination ones can still crack but they don't crack the ceramic dielectric inside. Yeah, it might peel off a little bit but

**Dave Jones:** you still got that conductive epoxy type stuff in there to go through. So there you go. Just terrific technology. And this is such a serious problem that the manufacturers have had to develop very specific manufacturing component manufacturing techniques to

**Dave Jones:** reduce and eliminate this sort of problem. It's a big deal. But in this particular uh for this soft termination TDK technology You can see that there. Um basically the main main disadvantage apart from probably extra cost to manufacture these things is, you know, a

**Dave Jones:** 12.5% decrease in nominal uh capacitance volumetric uh capacitance or whatnot. But, um that's a small price to pay for having a reliable product. And some markets like the automotive and other high vibration high stress environments demand this sort of reliability. And

**Dave Jones:** this is an interesting graph here uh using this uh soft termination technology. Um the amount of uh cracks um issues per number of times dropped. Look at you know, the regular multilayer ceramic caps just go up and up and up the more times you drop them.

**Dave Jones:** Um that mechanical stress can add up to a point where you know, you might start with a little micro crack doesn't damage your product. But, then that can get bigger and that can provide a crack point to make it bigger. So, every

**Dave Jones:** time the product is dropped can cause an issue. And well, if you get your capacitors from the One Hung Low company uh their stall at the Shenzhen market, you know, and need a reliable product, well, that can cause a big issue. So, but if

**Dave Jones:** you spend the money, you can buy the capacitors that are super reliable like this. And the other way to do it is you can actually uh TDK sell these capacitors that are effectively two capacitors in series in the one case.

**Dave Jones:** The way they've arranged the layers in there, as you can see, um it's a basically a an arrangement of two serial uh capacitors in there. So, you get the volumetric uh size, it's probably going to be decreased. The capacitance is

**Dave Jones:** going to be decreased. But, you don't have to have two physical components which take up more size when you got the footprints and everything else uh associated with them. But, once again, if uh these things don't have the soft uh

**Dave Jones:** termination technology or the lead frame technology, they're just simply a lower cost more reliable version that prevent the shorting capacitor problem. These things effectively will fail open if they're going to fail. And another way you can guarantee in it from a

**Dave Jones:** manufacturing point of view that you can get these to guarantee to fail open is that you can actually extend the length of the materials inside. So this is all part of the manufacturing thing. Once again, the data sheets will probably I

**Dave Jones:** don't know if they guarantee it, but they will say, you know, like it's almost guaranteed to fail open. The risk of it failing short cuz the cracks usually happen at the end terminations as we've seen in there. So if you

**Dave Jones:** move the plates back from the edges where the cracks typically happen, then you practically eliminate the possibility of a short because it just, you know, it physically can't happen. You can see down here this crack goes down here. A regular one can actually

**Dave Jones:** short out the plates, but this one can't because they don't overlap until they get further within the chip. So that's pretty neat. So here's a nice little summary of TDK's four different You know, one technique is not perfect.

**Dave Jones:** So they need four different techniques to mitigate the problem of flex causing cracks in issues and shorts in model A ceramic caps. So the mega cap is soft termination. I'll let you read that, but you know, cost obviously the higher the

**Dave Jones:** open mode ones are the highest cost. Look at that. I wouldn't have uh thought so, but obviously they need larger ceramic material to actually uh do that and they're going to be physically larger on the board as well

**Dave Jones:** for a given volumetric efficiency and stuff like that. So the obviously the cost, the smallest one is simply the lead frame cuz they just take their existing capacitors which are already manufacturing in the good billions and they just solder on some little lead

**Dave Jones:** frames on the end. The other ones are soft termination and the series design. I'm surprised the soft termination is actually you know isn't right up there in the highest cost but I guess they've perfected the technology that's it's not

**Dave Jones:** too bad. So we'll just have a very brief look here at the end of this TDK soft termination technology. Look at this, it shows you a very nice little diagram of how they actually do that the conductive resin layer and everything else.

**Dave Jones:** So I was just wondering how much what's the cost difference here between these and regular ones. Let's take a quick look. Now if we go on Mouser here and actually have a look at a specific TDK part number for a one microfarad 0402

**Dave Jones:** model a ceramic capacitor with soft termination technology. Here we go 2.8 cents in a in 10,000 quantity. So if we go over here and just find an equivalent just a generic one. But check this out. This is interesting. The Mouser

**Dave Jones:** parametric search actually has the termination type a specific soft flexible termination. And of course if you choose that then only the TDK parts will show up because that's a specific TDK thing and they've put that into the parametric search but that's really

**Dave Jones:** quite useful, isn't it? I like it. But anyway, if we search for all the catalog for one microfarad 0402 capacitors sort by price we're looking at 1.3 cents there. So basically half the price. So basically it doubles the

**Dave Jones:** price for that in volume. 10,000 is a reasonable volume in for that soft termination technology. So there you go. And if you use some of the other ones they're more expensive again. But yeah, that's you know double your cost. But if you got a lot

**Dave Jones:** of caps on your board, that can really ruin your bomb cost and and ruin your day. But something like a you know an automotive product reliability is the number one thing. So they're not going to skimp on cost. They're going to

**Dave Jones:** specify that specific part number for example, it must be that no substitutions. Um and that's it, right? You know, they must buy it and they buy it from the original, uh you know, a reputable certified source. So, make sure they

**Dave Jones:** don't get any, you know, no substituted crap quality parts somewhere in the supply chain or something like that. But and they would pay double or even more um for these, especially if you got big uh ones that are, you know, like

**Dave Jones:** equivalent to like the film capacitors is the X1, the Y1 uh kind of ones that go directly across the mains. They could uh cost a lot more or whatnot. If you wanted the volumetric efficie- efficiency of the multi-layer ceramic

**Dave Jones:** capacitors, but you wanted that reliability and guaranteed certification, you'll pay for that. Anyway, there you go. I've waffled on long enough about uh cracks and microcracks and shorting and how to reduce those in multi-layer product design for multi-layer ceramic

**Dave Jones:** capacitors. It really is a big issue that all the major manufacturers out there have solutions to solve this specific problem. So, I hope you found that interesting. If you did, please give it a big thumbs up and I'm sure

**Dave Jones:** I've missed some things. There's other techniques you can do as well, you know, it's probably not uh entirely comprehensive. But anyway, hope you found it useful and as always discuss down below and there'll be links to various uh

**Dave Jones:** application notes and data sheets down below. Catch you next time.
