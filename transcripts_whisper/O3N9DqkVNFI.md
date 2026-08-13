---
video_id: O3N9DqkVNFI
title: EEVblog #925 - Panasonic CF-U1 ToughBook Teardown
url: https://www.youtube.com/watch?v=O3N9DqkVNFI
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 17, "2": 48, "3": 74, "4": 85, "5": 110, "6": 131, "7": 151, "8": 170, "9": 189, "10": 206, "11": 223, "12": 242, "13": 261, "14": 274, "15": 292, "16": 310, "17": 325, "18": 341, "19": 356, "20": 373, "21": 391, "22": 407, "23": 427, "24": 454, "25": 473, "26": 494, "27": 511, "28": 525, "29": 544, "30": 565, "31": 585, "32": 604, "33": 623, "34": 638, "35": 654, "36": 672, "37": 688, "38": 706, "39": 720, "40": 738, "41": 752, "42": 774, "43": 788, "44": 806, "45": 826, "46": 848, "47": 864, "48": 884, "49": 904, "50": 924, "51": 942, "52": 962, "53": 984, "54": 1000, "55": 1028, "56": 1048, "57": 1070, "58": 1086, "59": 1106, "60": 1122, "61": 1136, "62": 1154, "63": 1174, "64": 1188, "65": 1204, "66": 1222, "67": 1238, "68": 1252, "69": 1268}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. We've got the Panasonic CF-U1 Toughbook for you. And, well, it wasn't as tough as it sounds because it's had the absolute crap beaten out of it and has seen better days. Look at that. This was sent in in the mailbag segment.

**Dave Jones:** Thank you for sending this one in. It is an industrial Windows-based computer. This is a reasonably recent model, not designed for consumer use, designed for industrial and professional use. It's got a built-in barcode, laser barcode scanner in it, so designed for, like, inventory warehouse management, going around scanning stuff, delivery drivers, you know, things like that.

**Dave Jones:** So, complete Windows platform in a rugged... well, it was apparently pretty rugged, but this one has just absolutely been butchered. So, look at the marks on it. Unbelievable. And it looks like it's got some sort of IP-rated waterproof... not waterproof, but, you know, water-resistant connector, things which don't stay in place anyway.

**Dave Jones:** Look, there's screws missing, so I don't know what the hell has gone wrong with this thing. Anyway, it comes with dual batteries in the thing so that you can keep it running and swap out the batteries. Very, very clever. I'm not sure what they do.

**Dave Jones:** They're some sort of... you know, they could play games with that. I don't know. Something to do with the battery, perhaps? Anyway, yeah, very professional solution, professional interface, and, no doubt, charging dock through that. So, you know, they would sell the professional base stations with this, so it'd plug in and all that sort of jazz.

**Dave Jones:** So, anyway, let's tear this puppy down and see what makes this so tough, when the going gets tough. And this one's so recent, it runs Windows 7 Pro. Beauty. And it's made in Japan. All the best stuff's made in Japan. Looks like it had a spot for a stylus, too, so that you could, no doubt, touch that.

**Dave Jones:** Hmm. Until it shattered. Like, why use glass like that? I thought it would have been some sort of polycarb. Hmm. And it's got room for a solid-state drive as well, using some weird-ass custom connector down in there. No doubt you buy that at considerable expense from Panasonic.

**Dave Jones:** We've got our first little peek of what's inside. We've got a bunch of flat-flex cables in here. This was under this cover here. And an unpopulated flat-flex, presumably for whatever plugs in here. Is that like some sort of wireless option or something like that?

**Dave Jones:** Anyway, we've got a two-way header. What is that for? I don't know. Anyway, it's like a four-way header. Tiny things. I don't know. But they decided these need to be accessible. And of course, this has to have 3G SIM capability, so that's going to go in there.

**Dave Jones:** Alright, here we go. I'm going to lift the kilt on this thing. And... ta-da! We're in like Flynn. Check it out. Aha, we found out what those connectors were for. There you go. Speaker, that would have been the 2-pin one. And the 4-pin one goes off to the two little trigger buttons.

**Dave Jones:** And no surprises for finding full rubber O-ring seal. Oh, that's not going to come out of there in a hurry. It's been in there too long. Oh, crusty as. But yeah, complete O-ring seal right around. So this would be a pretty decent IP rating on the thing.

**Dave Jones:** I'm not actually sure what the IP rating is. Anyway, there's our laser barcode scanner. And got a USB port on there. And right here is our GPS. That's our GPS antenna right on the top side there. And it's got a little coax going over, so there you go.

**Dave Jones:** You can take those off. Very common. And it's got a lead tech LR9101 chipset. And that just pops straight off. There you go. For those playing along at home, got ourselves the good old Surf chipset. No worries. And of course the Panasonic engineers aren't going to go to the trouble

**Dave Jones:** to design their own GPS and everything else. They're just going to buy, like, off-the-shelf module. Leave it to people who've already done that, and then just whack it in there. There you go. You can see the little castellations, they're called, on the edge of the board.

**Dave Jones:** They're the little half-moon ones. They basically put a pad on the side of the board, and then you just specify to the PCB manufacturer that you want to route straight through the center like that. Very common technique for PCB modules like that. And you can just nicely mount them on the board,

**Dave Jones:** and you get a nice little fillet into the half-moon castellation there. Very common. And for you GPS antenna aficionados, I know you want to see it. What's a glade? I assume it's a... Hmm. This little board here, they've gone to all the effort to put tape on top of there

**Dave Jones:** to stop that cable coming out from the flat-flex connector. Nice attention to detail. And they're serious about having the ground strapping go over to that board from that flat-flex. Look at that. Wow. Oh, and of course, they've gone to the effort to LED backlight

**Dave Jones:** those two buttons on the back via those flat-flexes. So they've had to, you know, build that into the... Well, not the mold, but all the... Well, this looks like magnesium alloy bracket here, so that's pretty good. And yeah, they've got those on the flat-flex to light up those LEDs.

**Dave Jones:** Now, I don't know what this inner... This board here, it says IFPCB. That's IF, obviously stands for interface. So I don't know what's doing there. A couple of level translators, maybe. I don't know, I'm not going to go in and look at the part numbers down there.

**Dave Jones:** But it doesn't seem to do anything else. It goes down to the board, right down the bottom down there, and then connects to all the, you know, the buttons and everything over here. They could just be dedicated button detection chips. I don't necessarily know.

**Dave Jones:** Anyway, that's just all for the speaker and other stuff, the LEDs and the buttons and things like that. We've got ourselves a sneaky little Wi-Fi antenna in there. I can't get the screw out yet, so obviously this entire module lifts out, and that coax snakes its way around there,

**Dave Jones:** down onto... is it that one or that one? I don't know. It goes off somewhere. There's more for the antenna aficionados. Oh, wiggle, wiggle, wiggle, wiggle, wiggle, yeah. Oh, and we found the other one. There you go. That's going to be the Bluetooth-y, would be my guess.

**Dave Jones:** Check it out, they even went to some trouble to put some cable management down there on the board. How sweet is that? Beautiful. Thumbs up, engineer who did that. Lift the RS shielding can, and bingo, we're in like Flynn. There is our... We've got bloody cables running off everywhere.

**Dave Jones:** We've got another antenna over here! What? Is that another... There you go, another Wi-Fi antenna. What? We've got two of them? Wow. Anyway, got ourselves an Ericsson F... 5521GW, for those plain looking at home. Aha! Now, here's our two antenna modules coming from here.

**Dave Jones:** One goes direct, that's the black one, goes directly into here. The other one goes here, into that board, and then maybe it goes out, they've got like just using that board as an interconnect. Anyway, there's our two antennas. So wireless WAN, main W-WAN,

**Dave Jones:** WAN10, I assume that's what it stands for, U1, CFU1, Mark II, but they are significantly different from an antenna point of view, so obviously for different bands. Tell you what, whoever specified this tape really went to town, because this stuff is impossible to get off.

**Dave Jones:** Wow. They earned their money. Oh, jeez, what is that? You'll note that where that cable went in before from here to here, and then out here to the antenna, look, smack in the middle of that is this switch here, another one over there,

**Dave Jones:** that's got to be an antenna switch. So you can start to see the modularity of this thing now, and this is where it's so impressive from a system engineering point of view. Looks like we've got a big-ass inductor and a tent under there, so that'd be

**Dave Jones:** localized power supply just for the RF module. And yeah, as I said, this looks like a magnesium alloy frame here, very nice, they haven't cut corners there, they've gilded the lily, and, oh man, that tape's incredible. But yeah, lots of flat flecks everywhere,

**Dave Jones:** incredible system engineering, very little wasted space inside this thing, and it's looking really nice. And of course, that is going to be conductive, and look at the big earth strap they've got going over there from some other part of that, and sure enough, ta-da!

**Dave Jones:** Check this out, I wonder if they've gone to the effort to add a blue cable for the Bluetooth antenna. It is, oh look, it's got blue cable. Ah, now we understand, it's actually, they've silkscreened on the assembly instructions. That is a nice bit of engineering

**Dave Jones:** right there, to actually, at the PCB design stage, know what cable, what colour cable that they're actually going to put in there, and put that on the silkscreen as an instruction to the assembly operators. Wow, that's some real systems thinking. Ta-da! Out pops

**Dave Jones:** our self-contained laser module! Look at that! Wow! All in one! Geez, and obviously Panasonic wouldn't have done this. Oh, there we go. Part number for those playing along at home. Aha, is that a symbol tech? I think I've torn down a single tech

**Dave Jones:** barcode reader before, haven't I? If memory serves me correctly, I don't know. Done way too many videos. Anyway, that's all it takes. It's already engineered for you. And they stuck this down, it's all one big flat flex, but they did put a rigid

**Dave Jones:** fibreglass backing on that. And they actually went to the trouble I've taken the screw out there, went to the trouble to actually earth these as well, which screw into the, or go into well, is it part of that? I don't know, I haven't actually seen

**Dave Jones:** the base station. But they've gone to the effort to earth those, have those all going right around. Very nice. They obviously had to do that for you know, system grounding RFI reasons. And ta-da! We're in like Flynn in terms of the screen. And you can see

**Dave Jones:** all the glass is shattered. It's obviously got the polycarbonate, I think I've got some glass shards in my fingers anyway. This is real nasty. They actually went for glass in there, I'm not sure what type of glass it is, plate glass or whatever, does it

**Dave Jones:** shatter like that? I don't know, I'm no glass expert. But yeah, they obviously did that. I mean, here's our touch screen on the front, but why they went with glass to wedge that in? I don't know, in such a tough book, they know

**Dave Jones:** people are going to drop this thing, it's going to be used out in the field, ruggedised. Why would you go with that? I don't know, if anyone's has the, or used these in the past, serviced them or whatever, or worked for a company that used them, did you have

**Dave Jones:** a big history of the glass shattering? Or was it so tough that they actually designed it like just flicked out? Hmm. Anyway, I don't see any real shock absorption on there in terms of like the case going into the glass, it just seems to be rigidly

**Dave Jones:** coupled by the plastic. I mean, the plastic's going to have some give as well. I'm sure they, you know, Panasonic would have done their vibration and shock testing on these, would have been extensive. So I'm sure they know what they're doing. This is

**Dave Jones:** not a one hung low brand, they would really know what they're doing. But anyway, this one did shatter, for whatever reason, and well, yeah. That's very nicely integrated into one, well, two-sided magnesium alloy package. That's really very sexy, I like that. Glass bloody shards everywhere,

**Dave Jones:** it's awful. I stick it into my fingers and they're bleh! Maybe you can see it in HD. If we separate those two halves, you can see that flat flex going off to the solid state drive there, that's obviously some sort of serial interface, I don't

**Dave Jones:** see... well, there's I don't know, maybe there's 15 lines on there or something. Anyway, I'm not sure what interface that they've used there. These are the battery connectors, look at that! You've got obviously the big-ass flat flex contacts, you know, half a dozen pins or whatever,

**Dave Jones:** for each power contact. No wuckers, and we've got an insulating sheet, ta-da! We're in. We don't see a processor yet, but here we go, here's more RF goodness. This thing's just chocka with RF. Here's our Wi-Fi module, dual antenna. Thank you very much for playing.

**Dave Jones:** ZooWare. There you go. 80211 ABGN. Mini PCI Express. Awesome. It should be lead-free, thank you very much. None of this lead rubbish. Looks like we've got our main system memory there. I don't know how much memory this thing had, I don't know, a couple of gigs

**Dave Jones:** or something like that, running Windows 7. There's going to be ah, yeah, probably something under there. Massive amount of bypassing under there, but that's not your typical BGA type pinout. Anyway, there's going to be a processor and a system ASIC. I haven't even looked at the specs

**Dave Jones:** of this thing, so I have no idea what processor it uses. We've got ourselves a battery backup in there. Thank you very much. Is that a rechargeable or a primary? Not sure. Anyway, screw there. Let's try and get this puppy out. And apart, shall we?

**Dave Jones:** What is that connector? That's our main DC power connector. Ta-da! There you go. Was that holding it in? Oh, there we go, we've got ourselves a thermal pad, and no wonder they're using the magnesium alloy. They're using that as the heatsink inside, because this is completely fanless, of course.

**Dave Jones:** Um, it's awesome to run Windows 7 fanless. Oh, bloody hell. Taped everywhere. They really didn't want this coming apart. Like, due to vibration and everything else, and ta-da! Now we're certainly in like Flynn. Look at this. Beautiful. For our system memory on the top here,

**Dave Jones:** there's our processor. And there's not much else. No, we've been ripped off. We haven't found the processor yet. This is the Intel System Hub. I'll show you that up close, because that's got the graphics media controller, so the graphics video and everything else, and there's

**Dave Jones:** something else under there. Come on. Come out of there. There we go. What's that baby? It's too small to be the processor. There it is. The AF82US15W. Yes, know it very well. Not. Um, anyway, yeah, system controller, graphics, and PCI Express, and everything

**Dave Jones:** else under the sun. Check it out. They've got some gluski under there. And hello, McFly. That is the processor. I thought it was too small. This is an Intel Atom. The AC9566 points towards the Intel Atom processor, the Z500 series. So I'll link in the data sheet for

**Dave Jones:** that, and try and get some more info on that. But there you go. Tiny little Atom processor. Look at the longitudinal die on that, compared to the big-ass system. The die up there has got more than the actual processor. Anyway, that's all she wrote.

**Dave Jones:** And is that a H8S processor? They've got that separate. We saw that in another teardown. What did we do recently? Tore down another embedded, the Sony embedded computer. Didn't we see a H8S in that? Anyway, what's that? Chrontel? Hmm. Check that out. And nothing else hugely

**Dave Jones:** interesting around there. There's our Alps clock. Main clock, I don't know. Then we get into the, oh, wind bond. There we go. And then we get into power stuff around here. Yeah. I'll spare you the details. They weren't mucking around on their PCB mount fuses there.

**Dave Jones:** Look at them. Four of the babies. You know how I was talking about rubberised shock mount on the screen before? Well, not on the glass, but certainly big rubber baby buggy bumper around the main LCD here. Check it out. There you go. That would have taken some out on the LCD

**Dave Jones:** as well. Sorry, on the glass. But the glass is still rigidly coupled in. Oh, and there you go. For all you Sanyo. We're going to install the Sanyo controller down in there, and I don't know, decode that part number for you LCD fanboys.

**Dave Jones:** And there you have it. That's inside the Panasonic Toughbook CFU-1. Very interesting bit of kit. As you can see, just tons of system integration. Everything has to be designed. Not only the main board, but every little mechanical, and this one goes RF to the hilt, but as I said before,

**Dave Jones:** Panasonic didn't roll their own in that sort of case. Maybe they did their own antenna boards and stuff like that, but everything uses off-the-shelf compliant modules, so they wouldn't have to worry about that. Someone's gone to town on that, and really this is not built down to a price.

**Dave Jones:** This is a professional product for the professional market. Price point wouldn't really have mattered. They spared no expense on this thing. I don't know what volumes would have been on these. You know, maybe the hundreds of thousands in the end? I don't know.

**Dave Jones:** Maybe it wasn't that much? Maybe in the tens of thousands? Something like that. You know, even like if you've got a large customer like UPS or the United States Postal Service or someone like that might order these with the scanning module and everything else, which may have been

**Dave Jones:** optional, but they designed it in there from the get-go. There's the little scanning module, and they could easily sell 10,000, 20,000 of those to all the courier drivers and everyone else in there, warehouse inventory scanning and management and things like that. So real interesting bit of kit.

**Dave Jones:** An Intel Atom processor. More than enough grunt just to run something like this. Windows 7 bare bones. You know, you're not going to be playing Doom on this thing. Or what is it these days? Bloody Crysis everyone keeps talking about. I don't know.

**Dave Jones:** Not up with this sort of newfangled games. Anyway, you're not going to be playing and doing anything serious on this. It's just, you know, you're going to be running a customised app and that's basically it. If some user was sufficiently clever, they might be able to

**Dave Jones:** play Solitaire on it or something. I don't know. Anyway. Hope you found that really interesting. These teardowns are always fascinating, these industrial bits of kit. Spared no expense, but yeah, glass. It's obviously one of the weak points. And I expected a bit more.

**Dave Jones:** I mean, obviously, the plastics inside this are going to be top quality. Like, you know, plastics have not broken. This thing's obviously been absolutely abused to hell and back. And dropped how many times? I don't know. It's just ridiculous. And the plastics have not broken.

**Dave Jones:** So these would be top quality thermoplastics. I'd be paying an absolute fortune for those. Not just, oh, whatever plastic mix came in the One Hung Loaf Factory this week. They would have gotten, you know, they would have specified that and characterised this thing.

**Dave Jones:** Shock and vibration testing to the hilt. IP testing. Everything else. And probably meets all sorts of industrial certifications and requirements and whatnot. And probably cost a fortune. I don't know if you know what these things cost back in the day. Sure it was more than

**Dave Jones:** an ordinary PC. I guarantee it. Anyway, if you liked that video, please give it a big thumbs up. Catch you next time.
