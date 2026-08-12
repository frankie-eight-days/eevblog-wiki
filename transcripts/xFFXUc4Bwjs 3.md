---
video_id: xFFXUc4Bwjs
title: EEVblog #669 - FLIR TG165 Thermal Imager Teardown
url: https://www.youtube.com/watch?v=xFFXUc4Bwjs
source: youtube-asr
timestamps: {"0": 0, "1": 18, "2": 32, "3": 48, "4": 63, "5": 78, "6": 95, "7": 109, "8": 123, "9": 139, "10": 155, "11": 173, "12": 187, "13": 200, "14": 215, "15": 228, "16": 242, "17": 259, "18": 269, "19": 281, "20": 294, "21": 311, "22": 324, "23": 339, "24": 355, "25": 369, "26": 385, "27": 398, "28": 412, "29": 428, "30": 441, "31": 453, "32": 466, "33": 487, "34": 501, "35": 517, "36": 536, "37": 549, "38": 562, "39": 578, "40": 590, "41": 605, "42": 619, "43": 634, "44": 650, "45": 664, "46": 682, "47": 696, "48": 715, "49": 726, "50": 736, "51": 753, "52": 768, "53": 790, "54": 804, "55": 816, "56": 829, "57": 842, "58": 859, "59": 874, "60": 886, "61": 897, "62": 912, "63": 933, "64": 951, "65": 970, "66": 986, "67": 1000, "68": 1014, "69": 1027, "70": 1046, "71": 1062, "72": 1076, "73": 1092, "74": 1107, "75": 1120, "76": 1135, "77": 1152, "78": 1169, "79": 1188, "80": 1203, "81": 1218, "82": 1238, "83": 1250, "84": 1265, "85": 1279, "86": 1295, "87": 1310, "88": 1324, "89": 1339, "90": 1355, "91": 1370, "92": 1383, "93": 1396, "94": 1408, "95": 1420, "96": 1434, "97": 1450, "98": 1465, "99": 1480, "100": 1493, "101": 1507, "102": 1523, "103": 1538, "104": 1552, "105": 1566, "106": 1583, "107": 1606, "108": 1622, "109": 1638, "110": 1653, "111": 1669, "112": 1684, "113": 1701, "114": 1719, "115": 1733, "116": 1747, "117": 1763, "118": 1778, "119": 1797, "120": 1816, "121": 1831, "122": 1846, "123": 1862, "124": 1878, "125": 1891, "126": 1905}
---

**Dave Jones:** Hi, welcome to Tear Down Tuesday. Today we're going to take a look at the brand spanking new Flur TG1 165 visual thermometer. No, it's not really a thermal imaging camera, although it does uh contain the new 80x60 thermal imaging

**Dave Jones:** leptton core. Exactly the same module. That's exactly the same as used in the new Flur one uh thermal imaging camera for the smartphones. But what this pe what this thing is, I showed it in the mailbag in the previous video and a lot

**Dave Jones:** of well some people seemed uh quite confused by exactly what it is. So under this large lens here on the front, it contains a traditional pyroctric uh passive infrared spot sensor. Exactly the same as what's used in, you know,

**Dave Jones:** these little cheap laser thermometers that you're used to. And this one has, of course, dual laser targeting as well to show you the size of the measurement aperture at the target that you're actually measuring. There's there'll be a Fresno lens in there somewhere behind

**Dave Jones:** that to actually uh focus that in. And it works exactly the same. But what they've done is they've added the new uh Flur Lepton core in here, the 80x60 thermal imager to give you a visual look at what's going on in there, what's

**Dave Jones:** going on at your target. But all of the measurement, the actual temperature measurement is still done via a traditional py pyroelectric sensor inside here. So your temperature reading here is not taken from the lepton sensor. It's taken from that uh pyro

**Dave Jones:** electric spot uh sensor in the front on that main window there. The leptton core is only there to provide this like a visual indication. And you'll notice that there's no temperature measurement on the side here. That's because this

**Dave Jones:** thing cannot get its temperature from that lepton core. It doesn't care. It doesn't need to be calibrated in any way to get that temperature cuz there is no scale like a traditional thermal camera. So, it it it looks like a thermal

**Dave Jones:** camera, but it's really just a spot thermometer like this. And that's all it's doing is reading with inside that laser targeted window there. So, anyway, um I hope that's cleared that up. So, this thing is designed to fit into a

**Dave Jones:** well, I guess you could say a small niche between your traditional spot thermometers like this and your full-on uh thermal imaging camera which Flur do the E series, the lowcost E series which has the same resolution 80x60 but uh

**Dave Jones:** it's you know it actually takes the measurement from uh the thermal imaging core itself and doesn't have any of this uh pyroctric traditional pyrolectric uh focused lens focused sensor in there. So they're you know targeting a very specific market for this and if you're

**Dave Jones:** doing any comparisons that's what you have to uh consider with this thing. It's not a proper thermal imaging camera and it's not just a uh laser spot meter like this kind of combination of the both. Now uh there's been a few

**Dave Jones:** questions on the forum. Does this thing actually do any calibration of the lepton sensor? Is there a shutter inside and things like that? So, well, I guess we'll find out when we open it. But I reckon the chances are extremely high

**Dave Jones:** there is no shutter inside this thing because it doesn't need, as I said, doesn't need to calibrate this scale. It doesn't matter a rat's ass what it measures from the lepton core as long as it can get an image out of it. It

**Dave Jones:** doesn't care what this scale is here. So, there's no need to calibrate it. So unless they've got a higherend model in the works and that capability with the calibration shutter is deliberately built into this thing, then I don't

**Dave Jones:** think it's going to have it. But of course, there's only one true way to find out. Let's tear it apart. Beauty. Void the warranty on this sucker. So this looks like a pretty solid beast. It is designed for a 2 m drop. So yeah,

**Dave Jones:** it's pretty solid. I don't see any screws on it, but tada. Look at that. There is a rubber thing here. What's under that? Does that Yep. Hello. Hello. Two screws. There we go. So, I think that was It might be too

**Dave Jones:** easy. I don't know. Um because we want to see how easy it is to replace the uh built-in lithium battery on this thing, too. You know, this is going to last a long time. So, you don't want your

**Dave Jones:** lithium battery to go dead and then you have to toss it. So, um I'm I'm hoping that it will be easy to get apart uh by having the two screws down here and no visible screws anywhere else. I my guess

**Dave Jones:** would be that it's hinged up here. And of course, here's the line. So, this whole top part of the case will just lift off and the gut should just pull out of there like that. That's the plan. Oh, and by the way, um this thing

**Dave Jones:** people, someone did notice in my previous video that this thing did seem to stop and looks like it had a calibration shutter in there. And it does occasionally, very occasionally freeze, but it is certainly not periodic. And oh, there we go. It just

**Dave Jones:** froze for like less than a second there. But it's not I've I've had it go for like several minutes without doing it. So I, you know, I don't know what that is, whether it's a processing thing or whether it is actually a calibration

**Dave Jones:** shutter coming in. But as I said, I I'd be quite surprised if there's a calibration shutter in this because the reason for that is that uh if it did, and they did have an upmarket model uh that's not out yet, obviously um that

**Dave Jones:** did do some sensing from the Lepton, then uh a measurement from the Lepton. That's the only reason I think you would have a calibration shutter on there. There we go. Screws are out. But um anyway, that would eat into the Flur E4

**Dave Jones:** sales of course. So, and of the uh the Flur one that goes on the iPhone, that's just design, you know, that's designed to be a consumer price point sort of gimmicky. It's not designed for not gimmicky, but you know, it's not

**Dave Jones:** designed for uh commercial applications like this one. Okay, looks like we're going to have a few little uh um clasps in there, I guess. So, let me just gently prize this sucker open. So, I don't expect a calibration shutter.

**Dave Jones:** And I don't expect um it to have as high a processing as what you get uh higher power processing like you get in the flu one. I think it had like an Atmill ARM uh processor, you know, like a SAM

**Dave Jones:** series processor in that uh Flur one. wouldn't expect that because this one doesn't have to do any MSX uh technology or anything like that. This is certainly proving a real dog to be get apart. There's a look, there's a uh a recess in

**Dave Jones:** there with overlapping molding that goes into that. But ah man, there it must be clips further up here. It's a real mongrel, let me tell you. Well, I really am having no luck with this thing. I've tried all sorts of ways

**Dave Jones:** to I managed to get the uh end piece out of that with the tripod mount on it. That was no problem. And I can prize it out, but there seems to be a stuck point in here. Um like there are screws in

**Dave Jones:** here somehow, but I can't see how like the rubber peels back. I can't see how you could get that screen out to access any screws there. So, I can only preserve and and they're not clips because I've tried all sorts of tools to

**Dave Jones:** try and lever them out and, you know, uncip it in various uh ways and it just hasn't budged at all. So, I reckon there's got to be screws in here and I can't see how that trigger is going to

**Dave Jones:** come out. Um, so by deduction based on the angle of everything, I would say you got to somehow prize this front off. Either the bezel around there or this entire thing. And there's probably some screws in there. Deep ones holding on

**Dave Jones:** the back of that. That would be my guess. H going to have a hack on the front now. So, let's get in there with the knife. And it looks like there is a gap under there. Aha. Tada. That's actually coming off ridiculously

**Dave Jones:** easy, actually. Does that just Is it just It's just adhesive held in there. Aha. Yeah, I think I see a screw. Yep. Yep. I think we have it. I think we have it, folks. That's the key. Yeah, it's just Yep.

**Dave Jones:** Just glued in place. There we go. And Oh, no. No, they aren't screws. What? But I'll tell you what, I can get my knife in there and prize that open. You might not be able to see that well,

**Dave Jones:** but yeah, that looks like it might actually pop. That whole front might actually pop out. Yeah, probably hard bit hard to do without a damage. Might have to get some plastic tools for that. And for those curious, no, there is

**Dave Jones:** nothing under the sticker there. I've checked. And you can usually feel those uh without having to peel them off, but I peeled it off just for good measure. There's nothing under there. Well, this thing's proving next to impossible, but

**Dave Jones:** I have managed to figure out that I can maybe lift this rubber off. So, yeah, if I maybe I prize that off, maybe the front will lift out. But I've been trying to prize all this top part open either at

**Dave Jones:** this point, this point, or this point is proved hopeless. I've had quite a lot of hacks around here. It is getting vicious, folks. Um, I'm getting medieval on its ass. I really am. I think I figured it out what's happening, though.

**Dave Jones:** I think this front plastic cover is glued in place or adhesived in place or something like that. And I need to get under there and pry that out like that because I reckon that the screws are in that that there's a couple of screws

**Dave Jones:** under here which go all the way through. Well, I'm in like Flynn, but what a bastard. And I've pretty much uh well, they're probably still functional, but I pretty much uh destroyed the front as you might have noticed in the previous

**Dave Jones:** clip. I didn't realize that when I was pressing uh uh play there that well record that I did actually crack trying to sort of prize that out. I did actually crack the IR lens on that thing. So, oops. Um and look, we've got

**Dave Jones:** three. There were actually three screws from the rear side holding this on. So, that was completely wrong. You had to get through there. So, I can't I think I can see some screws right down in there, but oh, what a I don't know. I don't

**Dave Jones:** know how this bloody thing comes apart. I could have sworn that this would have come off and then would have been screws back in there holding this back on because I can't pry any of this off regardless of what tool I use or what

**Dave Jones:** technique I use. So, yeah, there's a few Yep. Oops. Hm. There goes my uh lucky I've got a Flur E8. Um yeah, so even with that filter gone on the front and we've just got our leptton sensor there.

**Dave Jones:** That's it. It's in it. It's just in a little uh cage being held on there, it still works a treat. Anyway, we have cleared up the thing about the shutter. There is no shutter. If there was going to be it, it would be in here and it

**Dave Jones:** would move up and down in front of the lepton sensor there. So definitely no shutter folks. And tada we have out the uh purse sensor there with its uh lens assembly. And it is uh quite uh quite elaborate for one of these things.

**Dave Jones:** Anyway, um yeah, once again a flat flex cable. Was able to get there were four screws holding that down to a a holder, another plastic holder down inside. So I can get that off and take all that out.

**Dave Jones:** So and then we got our laser diodes on the side of course. So, I can uh unscrew all that and probably have a look at what sensor they used in there. And there we go. You can see down in there

**Dave Jones:** there is another another holder down there, that standoff. So, another couple of screws that get rid of that plastic standoff. But oh, hey, what's that? I'm going to be pissed off if that's a clip. Oh, I tell you what.

**Dave Jones:** And some people have wondered how those laser dodes actually formed the two dots which sort of you know rotated like that as we uh saw at the start and in the previous video. Well, it's to do with the slight angles on they're going to be

**Dave Jones:** angled in two axes slightly. So you might see that that one is slightly tilted that way I think and the other one is is it slightly tilted. Anyway, we're going to have slight tilts in these things. So, they're going to be

**Dave Jones:** perfectly aligned in there to give a to be basically uh vertical at the set distance where it's going to focus and then rotate in one direction when you get closer and rotate in the other direction and get bigger and further

**Dave Jones:** apart as you um get further away from the object. So, that's how it does that. No big deal. Nothing fancy, but it is quite clever. And just for kicks, I thought I would power the thing up without the leptton sensor in it. So,

**Dave Jones:** I've got nothing. I've taken out the plastic block and everything now and it's just sitting on that boot screen there. There's, you know, there's absolutely nothing happening there. I could maybe power up try some combinations. I haven't uh tried the

**Dave Jones:** power up key combinations yet actually to see if there's any debug mode or factory mode or something like that. But obviously, it's um not getting any data from the lepton sensor. So, it's just sitting there. And by the way, I can, if

**Dave Jones:** I don't get the rest of the case open, I can actually confirm that it is a an ARM STM 32 processor down in there. So, it's not the um it's not the ATM SAM. So, yep, different beast. And here you go.

**Dave Jones:** If you hold down the down arrow key and power it on, you actually get, tada, upgrade firmware, initialize SD card. So, it's clearly not happy that we don't have the firmware on the card. That's the firmware upgrade mode. And yep, it's

**Dave Jones:** just doing a dummy spit. So, as for getting this stupid thing apart, I've taken out all the screws down in the board. They're all gone. And all we got are these uh four shafts are running all the way up here. This goes into the

**Dave Jones:** molding at the back there. Of course, it just dead ends into the molding. But, we had some screws on the front of the board here. So, it's not like there could be screw on the top of that board

**Dave Jones:** there. So, that's probably just the board's probably just resting on that. But, there are two other shafts. You probably can't see them, but they're deep right down in there. And I believe there's two screws in there like that.

**Dave Jones:** But like, yeah, like accessed from this side here. Unbelievable. And yep, my hunch was right. There is two plastic clips in there at least. So, I've now I can prize these plastic clips open. But yeah, I had no chance of

**Dave Jones:** getting those from this side at all. They're designed to be like to go in once and that's that's pretty much it. Bastards. But I'm telling you what, even with this clip I know is out. I've actually broken it off inside. Basically prized it off.

**Dave Jones:** I still cannot attempt to even wedge these two part things apart. Like, you know, here down the bottom, it comes out like that fairly easily. And you see that it just sticks there. And I've taken that clip out up there. Then, I can only presume

**Dave Jones:** there's another one down in there. But I can't even like, you know, get in there and prize that open at all. Zip. Nothing. Unbelievable. Well, as you've probably guessed by now, and uh as I was beginning to uh guess as well, there was

**Dave Jones:** only one thing that this thing could be. This is all over molded rubber. The screws are in here like this under the screen. And this is all over molded. I had no chance in hell. Look, you can see

**Dave Jones:** the screw. There it is. I had to get along here and break this off with progressively bigger flathead screwdrivers. It's the only way I could do it. Um, is to, you know, break out those screws. And I'm still stuck

**Dave Jones:** because if I break them out anymore, if I try and break this top half off, I might break my SD card there and maybe my um USB micro connector down there. And ah, this is an evil piece of [ __ ]

**Dave Jones:** It really is. I mean, fan, by the way, all O-ring sealed all the way around here. Fantastic. uh you know, and O-ring sealed around the top here. Fantastic, but completely unserviceable. And the battery, by the way, um standard 18 650. There you go.

**Dave Jones:** With a a uh little connector on it, and that's it. But yeah, so that's screwed. There's no way that you could possibly replace this battery without destroying your unit. It is just it's a joke. And no, I can't like peel the rubber off or

**Dave Jones:** anything like that and get that screen out nicely. You got to destroy the whole lot, bastard. And there it is. Finally, after I don't know, bloody hell, an hour or something of trying to, you know, get it apart in way at least reasonably in

**Dave Jones:** one piece, I didn't stand a chance. This thing is just not designed to be open. And they have purposely designed this to be uh completely unserviceable and unopenable almost to the point that they, you know, they want to stop

**Dave Jones:** people, you know, maybe reverse engineering the thing, which is stupid because you just buy it and open it up. It's only 500 bucks, right? And, you know, it's nothing for somebody who wants to do that. And um but it's I

**Dave Jones:** didn't stand a chance at all. That is just pure evil. It really is. Whoever did this should be hung, drawn, and bloody quartered. Look, here are the standoffs. Here are the screws. Okay, there are the four screws there. I had

**Dave Jones:** to break those off that were down there, there in those board cutouts there in those little cutouts. So, that was behind there. So, the four screws are behind all this over molded rubber, which you cannot get off. It's

**Dave Jones:** completely uh fused on there and you can't get the and you can't get under there to peel to take any of that off either. It's just insane. But the good news is it still works. Look at that. There we go. I've got the

**Dave Jones:** got it all connected back up and it's still hunky dory. It just had stood absolutely no chance whatsoever. And hello. There's my camera. There we go. Ta. Hey, there we go. I can see my camera. Can see myself. There you go.

**Dave Jones:** Hello. Yep. Works fine. There's my LCD. And yeah, and we get our temperature, of course. There we go. 34. Yep. Good enough. Still works. So, after what, bloody 20 minutes of video or something, we can finally get to see the guts in

**Dave Jones:** this thing. Probably, as I said before, STM 32F103. That's a um ARM Cortex M3. Pretty beefy. Uh 72meg maximum speed. You know, it's got 1meg built-in flash. It's got USB. It's got 16K of S RAM. It does, you

**Dave Jones:** know, does all the business. Exactly what you'd expect in this, but uh curiously different to the one that's used in the Flur one, which was, as I said, an ATM uh SAM 9, I think. Uh once again an ARM processor but you know

**Dave Jones:** totally different manufacturer, different um uh different device targeted and inside the the upmarket Flur E4 is a free scale um MX257. So completely different again. And the E4 also has an FPGA as well a Cyclone uh 4 inside it. So you know they they've

**Dave Jones:** tailored this. They haven't just reused what they had in the ARM one or anything like that. So, um I don't maybe they got nothing on the bottom. I got to get that board out and check the uh bottom side,

**Dave Jones:** of course, but there's not a huge amount extra in there. What's this thing working at? There you go. That looks like the main oscillator only 8 megahertz. But that's kind of what you'd expect because uh they wouldn't, you

**Dave Jones:** know, I mean, this thing's just got to read the serial interface from it. It's either got to read the SPI or more more likely the Mippy interface from the Lepton sensor over here and then uh display it on the LCD. And that's

**Dave Jones:** basically it. There's not a huge amount else. Everything else is just uh support stuff. Here's our SD card. Here's our uh micro USB up here. We've got some um input protection there. Some more input protection going on down here. Some

**Dave Jones:** unpopulated parts around here. There's another two pin connector over here. So, I'm not sure what they uh designed that one for. Two pins is usually like power and based on the power traces there. It is some sort of power connector. So, I

**Dave Jones:** don't know. Maybe during uh development or something like that, but why you wouldn't use the the you know, the one they had over there. I I don't know. So, but as you can see, um couple of sort 23s not populated. And you know, there's

**Dave Jones:** not a huge amount extra. That's Look at that. That's interesting. That almost looks like it's been photoshopped on there, but it's not. It looks like there's a little sticker or it's it's had that changed. I'm going to get a

**Dave Jones:** closer look at that. Ah, look. There you go. What is that little two pin device? We got some Got some caps on there. Is that another Is that another crystal? It looks bizarre. Um, they've got to have a

**Dave Jones:** real-time clock crystal in here cuz this thing does have a uh realtime clock in it. So, is that what it is? Five pin 23s. Nothing fancy. There's really nothing else interesting. The button of course is the uh trigger, the front

**Dave Jones:** front panel trigger, but uh this would just be uh US can't make out the number on that from the screen here, but that would just be uh USB. Um yeah, that would just be the charging uh circuitry dead giveaway by its placement there.

**Dave Jones:** And yeah, there was really there's not much else. There's not much else at all. Wow. Yeah, it's very minimalist, but this is pretty much what I expected cuz as I said, all it's got to do is read out the data from our lepton sensor

**Dave Jones:** there, which is just a serial interface. Doesn't have to do it quick. It's only got to update, you know, I don't know how often this updates, you know, three, four times a second or something. Not much. I don't even think it does the

**Dave Jones:** full nine. Um, so it, um, which is limited by the, uh, international regulations and all that sort of crap. I don't even think it goes that fast. It doesn't need to. So, um, all it's got to do is read that serial data in and then

**Dave Jones:** update the display. And that's and handle the user interface. So, not a huge amount at all. We've got ourselves a small ATM external ES squared PROM there. I haven't checked whether or not this has any uh, nonvolatile memory

**Dave Jones:** apart from the uh, regular program flash built in. So maybe they're using that to hold the settings. And uh not a huge amount more. Got a couple of test points around there. We got one test point here. I don't see

**Dave Jones:** another one over here. Over here that's a ground. I don't see like any JTAG test points easily accessible on the top. So might have to get those from the bottom side if you want to muck around with that. And no surprises on the back

**Dave Jones:** that we've just got ourselves the LCD, a couple of tactile dome switches for the uh user interface. And I don't think there's anything under that. I might have a squeeze. And no, nothing on the back. Just a hot bar flat flex connector

**Dave Jones:** holding the uh LCD on. For those playing along at home, you can turn your monitor upside down and uh check out that part number in high definition there. or you can always look at the uh high-res tearown photos I've got on evbblog.com.

**Dave Jones:** But yeah, nothing else on there. So, the only thing it's I mean, incredibly simple. It all happens in that STM32. There's the flash built in. There's no external memory. There's just an external uh E squared PROM for some

**Dave Jones:** small E squared PROM for some nonvolatile stuff. Uh battery uh charging up here from the USB and just some miscellaneous stuff. And that's it. And well, that's pretty much all you'd expect. So, any theory anyone had about this having some secret capability built

**Dave Jones:** in cuz they had, you know, an upgraded model they haven't actually released yet and they'll just software limiting stuff. Well, no. you're limited by the lepton sensor, which unless there's a well-kept hidden secret that this thing's capable of better than um 80

**Dave Jones:** than the claimed 80x60 resolution, then um you're not going to be able to hack this thing to get anything worthwhile out of it really. Unless you want to rewrite the firmware to try and uh get some absolute value

**Dave Jones:** out of the Lepton sensor, but then you don't have a shutter, a calibration shutter on the thing to really make use of that. So, it's purpose-designed for the task. And as far as an actual product goes, it is actually extremely

**Dave Jones:** well engineered. I like it. Apart from it being absolutely freaking evil. So, there is our pyro electric spot sensor. Uh that's a four pin uh package that's on the back there. No, there's no extra uh temperature sensing on that

**Dave Jones:** board or anything like that. if you're wondering about um anything like that like the big uh ground plane around here it's not being temperature sensed or anything. So unless there's something internal but uh they don't need that sort of thing. So that is HCA60560

**Dave Jones:** 9. Google that one. So that's a sensor. But what we really want to also know is what's going on here with this lens. Cuz ordinarily on these you would see a Fresno lens. I'll show you that on the

**Dave Jones:** uh Fluke unit. And there it is down in there. You can see the Fresno arrangement of the all this staggered uh layers there. So yeah, and there isn't anything down in there. Just a tiny little pinhole down the bottom. Now, I'd

**Dave Jones:** love to get in there, but I've taken the screw off there and there. And well, it's all I think. Well, is that glued? No, I don't know. But I can't get it I can't get the thing apart at all. It's

**Dave Jones:** not going to budge and I don't want to ruin it. There's nothing hugely fascinating in there, I suspect. And uh there obviously it needs to be a certain length to get the uh 24 to1 uh spotto distance ratio they've got on this

**Dave Jones:** thing. Um but yeah, sorry. I don't want to don't want to smash it open, which is what it looks like I'll have to do. I think it's I don't know why they got the screws in there cuz this thing is seems to be

**Dave Jones:** glued shut. Anyway, you can tell from the glue on there that uh this whole laser arrangement sits in there and of course can rotate around like that. And somebody has lined it up in some sort of jig and then glued it in place. I assume

**Dave Jones:** that's a manual uh step after that's done. And it can probably of course go in and out like that as well. And both of those have been uh manually tweaked with the right tongue angle of course and glued in place to get that uh novel

**Dave Jones:** effect with the lasers that uh you know expands and rotates with the certain distance to match the Fresno lensing inside here. So the only thing I can presume that's going on here is this is an IR filter on the front and that's got

**Dave Jones:** to have just the uh Fresno lens in behind there. And that's you know pretty much all she wrote. And if you're curious to see that leptton sensor up close, there it is. Well, lepton module. It's all they've got a a ceramic uh base

**Dave Jones:** on that. It is all in one. It's a leadless chip carrier. And and there's the tiny little window on top down into the sensor array right down in there. Sorry, I'm not going to do a destructive tear down on my leptton sensor unless

**Dave Jones:** people want me to. H that's just around the outside of that edge. You could actually looks like you can take that clip off. That plastic top on there can just clip off. And you might be able to see a little bit more, but I'm not that

**Dave Jones:** daring for today. And we got something. Got a co. Is that a coil? And yes, that is most certainly a coil. Look at that. That's interesting. Anyone know what that's doing? And of course, that just plugs nicely into its leadless

**Dave Jones:** chip carrier socket like that. Please excuse my fingers in the way, but uh yeah, just sits in the socket nicely. Love it. Beautiful design. All right, it's back together. Look at this. Beautiful. Let's see if she still works.

**Dave Jones:** Come on, boot up. Oh, look at that. like I bought one. Fantastic. And if you have a look at my lead lights up on the roof, you can see these two red spots there and there. They're just the

**Dave Jones:** transformers for the lead lights just sitting on top of the panel up there. Can see right through it. No problems whatsoever. And I got my train set here. Sean was here playing before. And there we go. You can see that my power supply.

**Dave Jones:** You can still see the uh transformer inside. little bit warm. So, there you have it. I hope you enjoyed the tear down of the Flur TG1 165, I guess, visual thermometer or visual spot thermometer or infrared spot thermometer, whatever you want to call

**Dave Jones:** it. Sort of halfway between a a proper thermal imaging camera and uh one of those uh laser spot thermometers. So, that was a real pain in the ass to get into. And unfortunately, it's now pretty much ruined. And that was the timeout.

**Dave Jones:** Come on, boot up. Flur. There we go. Thank you very much. And anyway, I hope you enjoyed it. Was interesting. And yes, I've basically got a screwed unit. I'm going to keep it like that. It works. It's fine. No problems

**Dave Jones:** whatsoever. And if you want to see the high-res tearown photos of this, check the links down below. Evblog.com. There we go. Down below there. And if you want to discuss it, also links to the forum are down below or leave a

**Dave Jones:** YouTube comment. And don't forget to give it a big thumbs up if you like it because that helps a lot. Catch you next time.
