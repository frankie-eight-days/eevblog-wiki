---
video_id: xFFXUc4Bwjs
title: EEVblog #669 - FLIR TG165 Thermal Imager Teardown
url: https://www.youtube.com/watch?v=xFFXUc4Bwjs
source: youtube-asr
timestamps: {"0": 0, "1": 18, "2": 34, "3": 50, "4": 63, "5": 78, "6": 92, "7": 103, "8": 121, "9": 131, "10": 160, "11": 177, "12": 187, "13": 196, "14": 212, "15": 228, "16": 237, "17": 250, "18": 265, "19": 277, "20": 289, "21": 301, "22": 318, "23": 342, "24": 355, "25": 371, "26": 385, "27": 401, "28": 416, "29": 434, "30": 444, "31": 458, "32": 478, "33": 490, "34": 505, "35": 517, "36": 538, "37": 549, "38": 569, "39": 580, "40": 590, "41": 607, "42": 619, "43": 631, "44": 643, "45": 653, "46": 664, "47": 682, "48": 692, "49": 699, "50": 715, "51": 726, "52": 733, "53": 743, "54": 764, "55": 783, "56": 807, "57": 814, "58": 823, "59": 833, "60": 847, "61": 869, "62": 880, "63": 889, "64": 902, "65": 916, "66": 935, "67": 948, "68": 964, "69": 973, "70": 989, "71": 1000, "72": 1012, "73": 1023, "74": 1037, "75": 1051, "76": 1063, "77": 1076, "78": 1098, "79": 1109, "80": 1127, "81": 1143, "82": 1154, "83": 1169, "84": 1188, "85": 1200, "86": 1211, "87": 1231, "88": 1243, "89": 1253, "90": 1267, "91": 1279, "92": 1291, "93": 1303, "94": 1316, "95": 1327, "96": 1339, "97": 1353, "98": 1363, "99": 1375, "100": 1388, "101": 1398, "102": 1406, "103": 1415, "104": 1424, "105": 1436, "106": 1447, "107": 1462, "108": 1472, "109": 1486, "110": 1499, "111": 1508, "112": 1529, "113": 1548, "114": 1559, "115": 1572, "116": 1583, "117": 1597, "118": 1620, "119": 1630, "120": 1640, "121": 1655, "122": 1669, "123": 1684, "124": 1698, "125": 1726, "126": 1735, "127": 1747, "128": 1763, "129": 1781, "130": 1797, "131": 1816, "132": 1828, "133": 1841, "134": 1851, "135": 1862, "136": 1872, "137": 1883, "138": 1895, "139": 1909}
---

**Dave Jones:** Hi, welcome to Tear Down Tuesday. Today we're going to take a look at the brand spanking new Flur TG1 165 visual thermometer. No, it's not really a thermal imaging camera, although it does uh contain the new 80x60 thermal imaging leptton core.

**Dave Jones:** Exactly the same module. That's exactly the same as used in the new Flur one uh thermal imaging camera for the smartphones. But what this pe what this thing is, I showed it in the mailbag in the previous video and a lot of well some people seemed uh quite confused by exactly what it is.

**Dave Jones:** So under this large lens here on the front, it contains a traditional pyroctric uh passive infrared spot sensor. Exactly the same as what's used in, you know, these little cheap laser thermometers that you're used to.

**Dave Jones:** And this one has, of course, dual laser targeting as well to show you the size of the measurement aperture at the target that you're actually measuring. There's there'll be a Fresno lens in there somewhere behind that to actually uh focus that in.

**Dave Jones:** And it works exactly the same. But what they've done is they've added the new uh Flur Lepton core in here, the 80x60 thermal imager to give you a visual look at what's going on in there, what's going on at your target.

**Dave Jones:** But all of the measurement, the actual temperature measurement is still done via a traditional py pyroelectric sensor inside here. So your temperature reading here is not taken from the lepton sensor.

**Dave Jones:** It's taken from that uh pyro electric spot uh sensor in the front on that main window there. The leptton core is only there to provide this like a visual indication.

**Dave Jones:** And you'll notice that there's no temperature measurement on the side here. That's because this thing cannot get its temperature from that lepton core. It doesn't care. It doesn't need to be calibrated in any way to get that temperature cuz there is no scale like a traditional thermal camera.

**Dave Jones:** So, it it it looks like a thermal camera, but it's really just a spot thermometer like this. And that's all it's doing is reading with inside that laser targeted window there.

**Dave Jones:** So, anyway, um I hope that's cleared that up. So, this thing is designed to fit into a well, I guess you could say a small niche between your traditional spot thermometers like this and your full-on uh thermal imaging camera which Flur do the E series, the lowcost E series which has the same resolution 80x60 but uh it's you know it actually takes the measurement from uh the thermal imaging

**Dave Jones:** core itself and doesn't have any of this uh pyroctric traditional pyrolectric uh focused lens focused sensor in there. So they're you know targeting a very specific market for this and if you're doing any comparisons that's what you have to uh consider with this thing.

**Dave Jones:** It's not a proper thermal imaging camera and it's not just a uh laser spot meter like this kind of combination of the both. Now uh there's been a few questions on the forum.

**Dave Jones:** Does this thing actually do any calibration of the lepton sensor? Is there a shutter inside and things like that? So, well, I guess we'll find out when we open it.

**Dave Jones:** But I reckon the chances are extremely high there is no shutter inside this thing because it doesn't need, as I said, doesn't need to calibrate this scale. It doesn't matter a rat's ass what it measures from the lepton core as long as it can get an image out of it.

**Dave Jones:** It doesn't care what this scale is here. So, there's no need to calibrate it. So unless they've got a higherend model in the works and that capability with the calibration shutter is deliberately built into this thing, then I don't think it's going to have it.

**Dave Jones:** But of course, there's only one true way to find out. Let's tear it apart. Beauty. Void the warranty on this sucker. So this looks like a pretty solid beast.

**Dave Jones:** It is designed for a 2 m drop. So yeah, it's pretty solid. I don't see any screws on it, but tada. Look at that. There is a rubber thing here.

**Dave Jones:** What's under that? Does that Yep. Hello. Hello. Two screws. There we go. So, I think that was It might be too easy. I don't know. Um because we want to see how easy it is to replace the uh built-in lithium battery on this thing, too.

**Dave Jones:** You know, this is going to last a long time. So, you don't want your lithium battery to go dead and then you have to toss it. So, um I'm I'm hoping that it will be easy to get apart uh by having the two screws down here and no visible screws anywhere else.

**Dave Jones:** I my guess would be that it's hinged up here. And of course, here's the line. So, this whole top part of the case will just lift off and the gut should just pull out of there like that.

**Dave Jones:** That's the plan. Oh, and by the way, um this thing people, someone did notice in my previous video that this thing did seem to stop and looks like it had a calibration shutter in there.

**Dave Jones:** And it does occasionally, very occasionally freeze, but it is certainly not periodic. And oh, there we go. It just froze for like less than a second there. But it's not I've I've had it go for like several minutes without doing it.

**Dave Jones:** So I, you know, I don't know what that is, whether it's a processing thing or whether it is actually a calibration shutter coming in. But as I said, I I'd be quite surprised if there's a calibration shutter in this because the reason for that is that uh if it did, and they did have an upmarket model uh that's not out yet, obviously um that did do some sensing from the Lepton,

**Dave Jones:** then uh a measurement from the Lepton. That's the only reason I think you would have a calibration shutter on there. There we go. Screws are out. But um anyway, that would eat into the Flur E4 sales of course.

**Dave Jones:** So, and of the uh the Flur one that goes on the iPhone, that's just design, you know, that's designed to be a consumer price point sort of gimmicky. It's not designed for not gimmicky, but you know, it's not designed for uh commercial applications like this one.

**Dave Jones:** Okay, looks like we're going to have a few little uh um clasps in there, I guess. So, let me just gently prize this sucker open. So, I don't expect a calibration shutter.

**Dave Jones:** And I don't expect um it to have as high a processing as what you get uh higher power processing like you get in the flu one. I think it had like an Atmill ARM uh processor, you know, like a SAM series processor in that uh Flur one.

**Dave Jones:** wouldn't expect that because this one doesn't have to do any MSX uh technology or anything like that. This is certainly proving a real dog to be get apart. There's a look, there's a uh a recess in there with overlapping molding that goes into that.

**Dave Jones:** But ah man, there it must be clips further up here. It's a real mongrel, let me tell you. Well, I really am having no luck with this thing. I've tried all sorts of ways to I managed to get the uh end piece out of that with the tripod mount on it.

**Dave Jones:** That was no problem. And I can prize it out, but there seems to be a stuck point in here. Um like there are screws in here somehow, but I can't see how like the rubber peels back.

**Dave Jones:** I can't see how you could get that screen out to access any screws there. So, I can only preserve and and they're not clips because I've tried all sorts of tools to try and lever them out and, you know, uncip it in various uh ways and it just hasn't budged at all.

**Dave Jones:** So, I reckon there's got to be screws in here and I can't see how that trigger is going to come out. Um, so by deduction based on the angle of everything, I would say you got to somehow prize this front off.

**Dave Jones:** Either the bezel around there or this entire thing. And there's probably some screws in there. Deep ones holding on the back of that. That would be my guess. H going to have a hack on the front now.

**Dave Jones:** So, let's get in there with the knife. And it looks like there is a gap under there. Aha. Tada. That's actually coming off ridiculously easy, actually. Does that just Is it just It's just adhesive held in there.

**Dave Jones:** Aha. Yeah, I think I see a screw. Yep. Yep. I think we have it. I think we have it, folks. That's the key. Yeah, it's just Yep. Just glued in place.

**Dave Jones:** There we go. And Oh, no. No, they aren't screws. What? But I'll tell you what, I can get my knife in there and prize that open. You might not be able to see that well, but yeah, that looks like it might actually pop.

**Dave Jones:** That whole front might actually pop out. Yeah, probably hard bit hard to do without a damage. Might have to get some plastic tools for that. And for those curious, no, there is nothing under the sticker there.

**Dave Jones:** I've checked. And you can usually feel those uh without having to peel them off, but I peeled it off just for good measure. There's nothing under there. Well, this thing's proving next to impossible, but I have managed to figure out that I can maybe lift this rubber off.

**Dave Jones:** So, yeah, if I maybe I prize that off, maybe the front will lift out. But I've been trying to prize all this top part open either at this point, this point, or this point is proved hopeless.

**Dave Jones:** I've had quite a lot of hacks around here. It is getting vicious, folks. Um, I'm getting medieval on its ass. I really am. I think I figured it out what's happening, though.

**Dave Jones:** I think this front plastic cover is glued in place or adhesived in place or something like that. And I need to get under there and pry that out like that because I reckon that the screws are in that that there's a couple of screws under here which go all the way through.

**Dave Jones:** Well, I'm in like Flynn, but what a bastard. And I've pretty much uh well, they're probably still functional, but I pretty much uh destroyed the front as you might have noticed in the previous clip.

**Dave Jones:** I didn't realize that when I was pressing uh uh play there that well record that I did actually crack trying to sort of prize that out. I did actually crack the IR lens on that thing.

**Dave Jones:** So, oops. Um and look, we've got three. There were actually three screws from the rear side holding this on. So, that was completely wrong. You had to get through there.

**Dave Jones:** So, I can't I think I can see some screws right down in there, but oh, what a I don't know. I don't know how this bloody thing comes apart.

**Dave Jones:** I could have sworn that this would have come off and then would have been screws back in there holding this back on because I can't pry any of this off regardless of what tool I use or what technique I use.

**Dave Jones:** So, yeah, there's a few Yep. Oops. Hm. There goes my uh lucky I've got a Flur E8. Um yeah, so even with that filter gone on the front and we've just got our leptton sensor there.

**Dave Jones:** That's it. It's in it. It's just in a little uh cage being held on there, it still works a treat. Anyway, we have cleared up the thing about the shutter.

**Dave Jones:** There is no shutter. If there was going to be it, it would be in here and it would move up and down in front of the lepton sensor there.

**Dave Jones:** So definitely no shutter folks. And tada we have out the uh purse sensor there with its uh lens assembly. And it is uh quite uh quite elaborate for one of these things.

**Dave Jones:** Anyway, um yeah, once again a flat flex cable. Was able to get there were four screws holding that down to a a holder, another plastic holder down inside. So I can get that off and take all that out.

**Dave Jones:** So and then we got our laser diodes on the side of course. So, I can uh unscrew all that and probably have a look at what sensor they used in there.

**Dave Jones:** And there we go. You can see down in there there is another another holder down there, that standoff. So, another couple of screws that get rid of that plastic standoff.

**Dave Jones:** But oh, hey, what's that? I'm going to be pissed off if that's a clip. Oh, I tell you what. And some people have wondered how those laser dodes actually formed the two dots which sort of you know rotated like that as we uh saw at the start and in the previous video.

**Dave Jones:** Well, it's to do with the slight angles on they're going to be angled in two axes slightly. So you might see that that one is slightly tilted that way I think and the other one is is it slightly tilted.

**Dave Jones:** Anyway, we're going to have slight tilts in these things. So, they're going to be perfectly aligned in there to give a to be basically uh vertical at the set distance where it's going to focus and then rotate in one direction when you get closer and rotate in the other direction and get bigger and further apart as you um get further away from the object.

**Dave Jones:** So, that's how it does that. No big deal. Nothing fancy, but it is quite clever. And just for kicks, I thought I would power the thing up without the leptton sensor in it.

**Dave Jones:** So, I've got nothing. I've taken out the plastic block and everything now and it's just sitting on that boot screen there. There's, you know, there's absolutely nothing happening there.

**Dave Jones:** I could maybe power up try some combinations. I haven't uh tried the power up key combinations yet actually to see if there's any debug mode or factory mode or something like that.

**Dave Jones:** But obviously, it's um not getting any data from the lepton sensor. So, it's just sitting there. And by the way, I can, if I don't get the rest of the case open, I can actually confirm that it is a an ARM STM 32 processor down in there.

**Dave Jones:** So, it's not the um it's not the ATM SAM. So, yep, different beast. And here you go. If you hold down the down arrow key and power it on, you actually get, tada, upgrade firmware, initialize SD card.

**Dave Jones:** So, it's clearly not happy that we don't have the firmware on the card. That's the firmware upgrade mode. And yep, it's just doing a dummy spit. So, as for getting this stupid thing apart, I've taken out all the screws down in the board.

**Dave Jones:** They're all gone. And all we got are these uh four shafts are running all the way up here. This goes into the molding at the back there. Of course, it just dead ends into the molding.

**Dave Jones:** But, we had some screws on the front of the board here. So, it's not like there could be screw on the top of that board there. So, that's probably just the board's probably just resting on that.

**Dave Jones:** But, there are two other shafts. You probably can't see them, but they're deep right down in there. And I believe there's two screws in there like that. But like, yeah, like accessed from this side here.

**Dave Jones:** Unbelievable. And yep, my hunch was right. There is two plastic clips in there at least. So, I've now I can prize these plastic clips open. But yeah, I had no chance of getting those from this side at all.

**Dave Jones:** They're designed to be like to go in once and that's that's pretty much it. Bastards. But I'm telling you what, even with this clip I know is out. I've actually broken it off inside.

**Dave Jones:** Basically prized it off. I still cannot attempt to even wedge these two part things apart. Like, you know, here down the bottom, it comes out like that fairly easily.

**Dave Jones:** And you see that it just sticks there. And I've taken that clip out up there. Then, I can only presume there's another one down in there. But I can't even like, you know, get in there and prize that open at all.

**Dave Jones:** Zip. Nothing. Unbelievable. Well, as you've probably guessed by now, and uh as I was beginning to uh guess as well, there was only one thing that this thing could be.

**Dave Jones:** This is all over molded rubber. The screws are in here like this under the screen. And this is all over molded. I had no chance in hell. Look, you can see the screw.

**Dave Jones:** There it is. I had to get along here and break this off with progressively bigger flathead screwdrivers. It's the only way I could do it. Um, is to, you know, break out those screws.

**Dave Jones:** And I'm still stuck because if I break them out anymore, if I try and break this top half off, I might break my SD card there and maybe my um USB micro connector down there.

**Dave Jones:** And ah, this is an evil piece of [ __ ] It really is. I mean, fan, by the way, all O-ring sealed all the way around here. Fantastic. uh you know, and O-ring sealed around the top here.

**Dave Jones:** Fantastic, but completely unserviceable. And the battery, by the way, um standard 18 650. There you go. With a a uh little connector on it, and that's it. But yeah, so that's screwed.

**Dave Jones:** There's no way that you could possibly replace this battery without destroying your unit. It is just it's a joke. And no, I can't like peel the rubber off or anything like that and get that screen out nicely.

**Dave Jones:** You got to destroy the whole lot, bastard. And there it is. Finally, after I don't know, bloody hell, an hour or something of trying to, you know, get it apart in way at least reasonably in one piece, I didn't stand a chance.

**Dave Jones:** This thing is just not designed to be open. And they have purposely designed this to be uh completely unserviceable and unopenable almost to the point that they, you know, they want to stop people, you know, maybe reverse engineering the thing, which is stupid because you just buy it and open it up.

**Dave Jones:** It's only 500 bucks, right? And, you know, it's nothing for somebody who wants to do that. And um but it's I didn't stand a chance at all. That is just pure evil.

**Dave Jones:** It really is. Whoever did this should be hung, drawn, and bloody quartered. Look, here are the standoffs. Here are the screws. Okay, there are the four screws there. I had to break those off that were down there, there in those board cutouts there in those little cutouts.

**Dave Jones:** So, that was behind there. So, the four screws are behind all this over molded rubber, which you cannot get off. It's completely uh fused on there and you can't get the and you can't get under there to peel to take any of that off either.

**Dave Jones:** It's just insane. But the good news is it still works. Look at that. There we go. I've got the got it all connected back up and it's still hunky dory.

**Dave Jones:** It just had stood absolutely no chance whatsoever. And hello. There's my camera. There we go. Ta. Hey, there we go. I can see my camera. Can see myself. There you go.

**Dave Jones:** Hello. Yep. Works fine. There's my LCD. And yeah, and we get our temperature, of course. There we go. 34. Yep. Good enough. Still works. So, after what, bloody 20 minutes of video or something, we can finally get to see the guts in this thing.

**Dave Jones:** Probably, as I said before, STM 32F103. That's a um ARM Cortex M3. Pretty beefy. Uh 72meg maximum speed. You know, it's got 1meg built-in flash. It's got USB. It's got 16K of S RAM.

**Dave Jones:** It does, you know, does all the business. Exactly what you'd expect in this, but uh curiously different to the one that's used in the Flur one, which was, as I said, an ATM uh SAM 9, I think.

**Dave Jones:** Uh once again an ARM processor but you know totally different manufacturer, different um uh different device targeted and inside the the upmarket Flur E4 is a free scale um MX257.

**Dave Jones:** So completely different again. And the E4 also has an FPGA as well a Cyclone uh 4 inside it. So you know they they've tailored this. They haven't just reused what they had in the ARM one or anything like that.

**Dave Jones:** So, um I don't maybe they got nothing on the bottom. I got to get that board out and check the uh bottom side, of course, but there's not a huge amount extra in there.

**Dave Jones:** What's this thing working at? There you go. That looks like the main oscillator only 8 megahertz. But that's kind of what you'd expect because uh they wouldn't, you know, I mean, this thing's just got to read the serial interface from it.

**Dave Jones:** It's either got to read the SPI or more more likely the Mippy interface from the Lepton sensor over here and then uh display it on the LCD. And that's basically it.

**Dave Jones:** There's not a huge amount else. Everything else is just uh support stuff. Here's our SD card. Here's our uh micro USB up here. We've got some um input protection there.

**Dave Jones:** Some more input protection going on down here. Some unpopulated parts around here. There's another two pin connector over here. So, I'm not sure what they uh designed that one for.

**Dave Jones:** Two pins is usually like power and based on the power traces there. It is some sort of power connector. So, I don't know. Maybe during uh development or something like that, but why you wouldn't use the the you know, the one they had over there.

**Dave Jones:** I I don't know. So, but as you can see, um couple of sort 23s not populated. And you know, there's not a huge amount extra. That's Look at that.

**Dave Jones:** That's interesting. That almost looks like it's been photoshopped on there, but it's not. It looks like there's a little sticker or it's it's had that changed. I'm going to get a closer look at that.

**Dave Jones:** Ah, look. There you go. What is that little two pin device? We got some Got some caps on there. Is that another Is that another crystal? It looks bizarre.

**Dave Jones:** Um, they've got to have a real-time clock crystal in here cuz this thing does have a uh realtime clock in it. So, is that what it is? Five pin 23s.

**Dave Jones:** Nothing fancy. There's really nothing else interesting. The button of course is the uh trigger, the front front panel trigger, but uh this would just be uh US can't make out the number on that from the screen here, but that would just be uh USB.

**Dave Jones:** Um yeah, that would just be the charging uh circuitry dead giveaway by its placement there. And yeah, there was really there's not much else. There's not much else at all.

**Dave Jones:** Wow. Yeah, it's very minimalist, but this is pretty much what I expected cuz as I said, all it's got to do is read out the data from our lepton sensor there, which is just a serial interface.

**Dave Jones:** Doesn't have to do it quick. It's only got to update, you know, I don't know how often this updates, you know, three, four times a second or something. Not much.

**Dave Jones:** I don't even think it does the full nine. Um, so it, um, which is limited by the, uh, international regulations and all that sort of crap. I don't even think it goes that fast.

**Dave Jones:** It doesn't need to. So, um, all it's got to do is read that serial data in and then update the display. And that's and handle the user interface. So, not a huge amount at all.

**Dave Jones:** We've got ourselves a small ATM external ES squared PROM there. I haven't checked whether or not this has any uh, nonvolatile memory apart from the uh, regular program flash built in.

**Dave Jones:** So maybe they're using that to hold the settings. And uh not a huge amount more. Got a couple of test points around there. We got one test point here.

**Dave Jones:** I don't see another one over here. Over here that's a ground. I don't see like any JTAG test points easily accessible on the top. So might have to get those from the bottom side if you want to muck around with that.

**Dave Jones:** And no surprises on the back that we've just got ourselves the LCD, a couple of tactile dome switches for the uh user interface. And I don't think there's anything under that.

**Dave Jones:** I might have a squeeze. And no, nothing on the back. Just a hot bar flat flex connector holding the uh LCD on. For those playing along at home, you can turn your monitor upside down and uh check out that part number in high definition there.

**Dave Jones:** or you can always look at the uh high-res tearown photos I've got on evbblog.com. But yeah, nothing else on there. So, the only thing it's I mean, incredibly simple.

**Dave Jones:** It all happens in that STM32. There's the flash built in. There's no external memory. There's just an external uh E squared PROM for some small E squared PROM for some nonvolatile stuff.

**Dave Jones:** Uh battery uh charging up here from the USB and just some miscellaneous stuff. And that's it. And well, that's pretty much all you'd expect. So, any theory anyone had about this having some secret capability built in cuz they had, you know, an upgraded model they haven't actually released yet and they'll just software limiting stuff.

**Dave Jones:** Well, no. you're limited by the lepton sensor, which unless there's a well-kept hidden secret that this thing's capable of better than um 80 than the claimed 80x60 resolution, then um you're not going to be able to hack this thing to get anything worthwhile out of it really.

**Dave Jones:** Unless you want to rewrite the firmware to try and uh get some absolute value out of the Lepton sensor, but then you don't have a shutter, a calibration shutter on the thing to really make use of that.

**Dave Jones:** So, it's purpose-designed for the task. And as far as an actual product goes, it is actually extremely well engineered. I like it. Apart from it being absolutely freaking evil.

**Dave Jones:** So, there is our pyro electric spot sensor. Uh that's a four pin uh package that's on the back there. No, there's no extra uh temperature sensing on that board or anything like that.

**Dave Jones:** if you're wondering about um anything like that like the big uh ground plane around here it's not being temperature sensed or anything. So unless there's something internal but uh they don't need that sort of thing.

**Dave Jones:** So that is HCA60560 9. Google that one. So that's a sensor. But what we really want to also know is what's going on here with this lens. Cuz ordinarily on these you would see a Fresno lens.

**Dave Jones:** I'll show you that on the uh Fluke unit. And there it is down in there. You can see the Fresno arrangement of the all this staggered uh layers there.

**Dave Jones:** So yeah, and there isn't anything down in there. Just a tiny little pinhole down the bottom. Now, I'd love to get in there, but I've taken the screw off there and there.

**Dave Jones:** And well, it's all I think. Well, is that glued? No, I don't know. But I can't get it I can't get the thing apart at all. It's not going to budge and I don't want to ruin it.

**Dave Jones:** There's nothing hugely fascinating in there, I suspect. And uh there obviously it needs to be a certain length to get the uh 24 to1 uh spotto distance ratio they've got on this thing.

**Dave Jones:** Um but yeah, sorry. I don't want to don't want to smash it open, which is what it looks like I'll have to do. I think it's I don't know why they got the screws in there cuz this thing is seems to be glued shut.

**Dave Jones:** Anyway, you can tell from the glue on there that uh this whole laser arrangement sits in there and of course can rotate around like that. And somebody has lined it up in some sort of jig and then glued it in place.

**Dave Jones:** I assume that's a manual uh step after that's done. And it can probably of course go in and out like that as well. And both of those have been uh manually tweaked with the right tongue angle of course and glued in place to get that uh novel effect with the lasers that uh you know expands and rotates with the certain distance to match the Fresno lensing inside here.

**Dave Jones:** So the only thing I can presume that's going on here is this is an IR filter on the front and that's got to have just the uh Fresno lens in behind there.

**Dave Jones:** And that's you know pretty much all she wrote. And if you're curious to see that leptton sensor up close, there it is. Well, lepton module. It's all they've got a a ceramic uh base on that.

**Dave Jones:** It is all in one. It's a leadless chip carrier. And and there's the tiny little window on top down into the sensor array right down in there. Sorry, I'm not going to do a destructive tear down on my leptton sensor unless people want me to.

**Dave Jones:** H that's just around the outside of that edge. You could actually looks like you can take that clip off. That plastic top on there can just clip off. And you might be able to see a little bit more, but I'm not that daring for today.

**Dave Jones:** And we got something. Got a co. Is that a coil? And yes, that is most certainly a coil. Look at that. That's interesting. Anyone know what that's doing? And of course, that just plugs nicely into its leadless chip carrier socket like that.

**Dave Jones:** Please excuse my fingers in the way, but uh yeah, just sits in the socket nicely. Love it. Beautiful design. All right, it's back together. Look at this. Beautiful. Let's see if she still works.

**Dave Jones:** Come on, boot up. Oh, look at that. like I bought one. Fantastic. And if you have a look at my lead lights up on the roof, you can see these two red spots there and there.

**Dave Jones:** They're just the transformers for the lead lights just sitting on top of the panel up there. Can see right through it. No problems whatsoever. And I got my train set here.

**Dave Jones:** Sean was here playing before. And there we go. You can see that my power supply. You can still see the uh transformer inside. little bit warm. So, there you have it.

**Dave Jones:** I hope you enjoyed the tear down of the Flur TG1 165, I guess, visual thermometer or visual spot thermometer or infrared spot thermometer, whatever you want to call it.

**Dave Jones:** Sort of halfway between a a proper thermal imaging camera and uh one of those uh laser spot thermometers. So, that was a real pain in the ass to get into.

**Dave Jones:** And unfortunately, it's now pretty much ruined. And that was the timeout. Come on, boot up. Flur. There we go. Thank you very much. And anyway, I hope you enjoyed it.

**Dave Jones:** Was interesting. And yes, I've basically got a screwed unit. I'm going to keep it like that. It works. It's fine. No problems whatsoever. And if you want to see the high-res tearown photos of this, check the links down below.

**Dave Jones:** Evblog.com. There we go. Down below there. And if you want to discuss it, also links to the forum are down below or leave a YouTube comment. And don't forget to give it a big thumbs up if you like it because that helps a lot.

**Dave Jones:** Catch you next time.
