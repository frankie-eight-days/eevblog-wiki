---
video_id: y5YujLhFtzU
title: EEVblog 1610 - Deye 5kW Hybrid Solar Inverter
url: https://www.youtube.com/watch?v=y5YujLhFtzU
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 33, "3": 47, "4": 65, "5": 82, "6": 95, "7": 111, "8": 129, "9": 139, "10": 155, "11": 168, "12": 180, "13": 193, "14": 203, "15": 216, "16": 229, "17": 245, "18": 256, "19": 269, "20": 281, "21": 294, "22": 307, "23": 324, "24": 339, "25": 350, "26": 365, "27": 378, "28": 395, "29": 406, "30": 419, "31": 437, "32": 449, "33": 463, "34": 477, "35": 490, "36": 503, "37": 516, "38": 529, "39": 543, "40": 564, "41": 582, "42": 599, "43": 615, "44": 635, "45": 653, "46": 669, "47": 686, "48": 697, "49": 711, "50": 725, "51": 741, "52": 753, "53": 766, "54": 780, "55": 794, "56": 806, "57": 816, "58": 826, "59": 844, "60": 862, "61": 876, "62": 888, "63": 903, "64": 915, "65": 926, "66": 941, "67": 956, "68": 978, "69": 993, "70": 1007, "71": 1019, "72": 1031, "73": 1046, "74": 1061, "75": 1076, "76": 1092, "77": 1106, "78": 1121, "79": 1135, "80": 1151, "81": 1165, "82": 1180, "83": 1190, "84": 1209, "85": 1219, "86": 1233, "87": 1249}
---

**Dave Jones:** Hi, welcome to an exciting teardown. We've got a solar inverter for you. This is a DIY inverter. It's a Sun 5 K SG04LP1A AU, the Australian model for those playing along at home. It's a 5 kW hybrid inverter. Yes, I'm going to

**Dave Jones:** upgrade my original 3 kW Sunny Boy inverter at home. So, stay tuned for future videos on that. But, before this gets installed next week, I just wanted to do a teardown. Let's go. This should be exciting. Look at this bad boy. It's a

**Dave Jones:** bit of a beast. We've got giant heat sinks on it. So, this is We'll show you the specs. And you'll have to read the specs sideways if you're really interested. Anyway, a hybrid inverter IP 65. So, you know, good enough for, you

**Dave Jones:** know, outdoor mounting and rain and whatnot. It's a nominal 5 kW inverter, but it can actually do 65 100 W 6.5 kW peak. And the reason I picked this DIY inverter is cuz it supports a ton of different batteries. So, there's no

**Dave Jones:** vendor lock-in on your batteries. Anyway, that'll be the subject of a future videos. But, it supports a 5 kW charge and discharge from the battery as well. And also 5 kW into the grid. But, as I said, 6 and 1/2 kW peak PV solar

**Dave Jones:** input. And also, it's got an emergency backup load on it as well, which I'm going to utilize. Now, unfortunately, I might have guessed the sizing because I It says here the PV input power per string is 3250 W.

**Dave Jones:** I've actually got 3.33, I think it is. So, I might have to remove a panel from each of my strings. Anyway, oops. And the IO here, we've got our two PV strings, standard MC4 connectors on the input here. That's

**Dave Jones:** nice. Battery input plus and minus, I think it's 35 sq mm copper as its rating. It's got two com ports for the RS485 and CAN for the any battery and other coms. It's got like four different cables, so you can basically have four

**Dave Jones:** weather proof cables coming out of there. So it does actually come with a Wi-Fi dongle that just plugs into a D9 connector in there and has an antenna sticking out the bottom. I'll actually show you that today. And one of the most

**Dave Jones:** interesting things about this inverter is it's got a generator input. So not you know like a diesel generator input but that also supports inverters. So microinverters. So in theory, I could actually put all of my Nphase microinverter system into here. But

**Dave Jones:** unfortunately, I can't do that in a practical sense because I've already got 5 kW maximum over here and it's a 5 kW max inverter. But you can actually put microinverters into the generator input. That is really cool. I haven't seen

**Dave Jones:** another I don't know. Leave it in the comments if you've seen another inverter that you've seen can do that. Now, this is the emergency load output. I will be powering my fridges off this and some emergency power points and and things.

**Dave Jones:** But some people power their entire homes from the emergency off-grid backup. So it's like it automatically switches over. So if you're in an off-grid property for example, you would plug it into here cuz you don't have a grid

**Dave Jones:** connection. So you plug your whole home into here and well, you couldn't you can plug your grid in as well if you have it. But your whole house load if you if you want to if you had a big enough inverter. And I

**Dave Jones:** believe you can have up to 16 of these inverters in parallel. So that's really cool. So you can actually power your entire house from there. But I won't be doing that for practical reasons cuz I've also got my 5 kW Nphase system as

**Dave Jones:** well which is on the grid. So yeah, and this is only a 5 kW total inverter. So anyway, yeah, very cool. The flexibility on this thing is incredible. That's why I bought it. Big clunking PV switch there. That'll be in series with the

**Dave Jones:** panel. So you don't need an external box. Very nice. Um and a big nice like elevator type on off button. That's really sweet. And as you can see, it's all undercut here and it's just all heat sink on the back here. And we can check

**Dave Jones:** that out. Wow, look at that. So, that's our mounting uh bracket that goes on the wall and then you just lift it and hook it in place. But yeah, this looks like two different heat sinks here. One down

**Dave Jones:** here, which is one big solid array in there. That'd be like for where your big MOSFETs are mounted to and just a more general purpose one. I don't know. Might have one might be for the inverter, one might be for the

**Dave Jones:** battery type system. I don't know. That's why we're going to hopefully tear it apart. So, fingers crossed I can actually do it without damaging it. And that's what it looks like on the front. There's a nice big weatherproof access

**Dave Jones:** panel here with a big O-ring seal. Have a look at that. And a big color LCD graphical LCD display on here. So, it's very nice from a display point of view and some indicators for your DC string, your AC,

**Dave Jones:** your normal. And there's a ton of different configurations you can put this thing in. It's absolutely amazing. I've never seen an inverter like it. Anyway, I won't go through it in detail, but it has all different configuration modes where, you know, a basic mode like

**Dave Jones:** this, a basic mode with backup. That's how I'll be using this thing even I don't have a diesel generator. I do actually have the ability to put like extra microinverter. Maybe that 3 miles one. I might actually experiment with that and put in. So, you

**Dave Jones:** can have a smart load configurations. Then you can have on generator plus AC couple configurations, on load plus AC couple configurations, on grid plus AC couple configurations. And there's lots of other little tweaks and stuff you can do it.

**Dave Jones:** Anyway, you can do a ton of stuff with this. It's just absolutely incredible. It even had something for wind turbines up here. Look at that. There's some connection diagrams, but it does have an installation manual. Didn't come with it

**Dave Jones:** though, which is a bit disappointing. Anyway, this one cost me 1,600 Aussie dollaridoos from the local supplier Dual Power. So, I'll link them and link them in down below if you want one of these bad boys. So, this is incredibly cheap.

**Dave Jones:** I got to say this is probably the best bang for buck inverter on the market. Yes, it is made in China, but DIY pretty big. I'll put in some photos of their factories and whatnot. And they're a, you know, a pretty big player, but

**Dave Jones:** they're not one of the more well-known brands. But, just the ability of this to run like tons of different different chemistry and type batteries. I'm not locked into any battery configuration. I can even run old 12-V, you know, lead-acid batteries if I want.

**Dave Jones:** Now, there seems to be some confusion over the name. I call it DIY because I think there's a capital D and there's an I in there with the dot. So, I think they want us to pronounce it DIY, but

**Dave Jones:** I've heard it pronounced day-e, day-a, all sorts of things like that. But, I'm going to call it DIY. I think it's correct, but I don't know. Company official, correct me down below. Warranty void if seal broken, huh? Well,

**Dave Jones:** let's see if we can uh get that out. Get a I've done a video Oh, no, void. There you go. No, I think I voided it. That hasn't worked. My technique of the No, no, that's That's pretty good void sticker. Oops.

**Dave Jones:** Okay, if we have a look in the access panel here and you can see the nice rubber baby buggy bunker seal around the uh window there. Have to keep this thing tilted. Um it's a little bit hard, but

**Dave Jones:** there you go. You've got all your basic wiring. There's that PV switch on the side. So, these are your MC4 string wiring coming in and then just going out the bottom there. And then that's our power clunk and power switch on the

**Dave Jones:** side. Got a ferrite down there, and those two gigantic screw terminals down there are your battery. So, your battery your wiring just comes in there, and you screw them down. As I said, I think the spec is 35 square mil or something like

**Dave Jones:** that. Then you've got all your various interfaces down here. There's an earth screw terminal block, nice. So, you've got your grid, your load, your generator. Then there's various RJ45s around here. So, they're the like there's an external meter if you want

**Dave Jones:** it. RS485, CAN, and and then we've got some little screw terminals here. They're like you can get a temp sensor. In fact, it comes with a temp temp sensor that goes into 12-V lead-acid battery. So, if you want to

**Dave Jones:** hook those directly on, it all comes with that. Couple of dip switches for various mode and country settings and things like that, I guess. And there's a couple of relays down there associated with that. So, can't see a huge amount.

**Dave Jones:** That looks like a cutout circuit breaker. That like looks like it'll pop up. No, that don't that isn't like an anti-tamper thing on the front. It's too low down for that. Gigantic varistor down there, and can see some big current

**Dave Jones:** shunt links down behind that, but can't see a huge amount more. Let's try and open the rest of it. Okay, it looks like this heatsink is screwed internally to this larger heatsink. So, I think if I get the outside screws here, I'm hoping

**Dave Jones:** this whole thing will just lift off in one side. That's my guess. So, anyway, comically long screwdriver time, and uh let's go. So, if there is this is designed well, I shouldn't you know break any thermal you know, heatsink uh

**Dave Jones:** connections or anything. It should just hold the case on it. It should pivot out. That's the plan. But, I'm assuming that the designers have designed it for a little bit of serviceability if not assembly. So, we'll see what happens. Anyway, if this

**Dave Jones:** does fail and they don't honor the warranty, then uh Um definitely thumbs up uh and comment down below and share this video cuz I I might need the ad revenue. Um And I don't buy the merch on my store.

**Dave Jones:** Buy a multimeter from me, please. evblog.store They put an access hole here for this screw. That's nice. Okay, I think I got them all out. No, it doesn't doesn't want to pop out off. Oh, no, unfortunately, it's not going to

**Dave Jones:** come off because Look, this seems to be screwed. As I said, this heatsink here is screwed from the inside, and yet I can't access the inside, so uh cuz there's no front panel. It's like one big It's one big case. So,

**Dave Jones:** I'm not Damn, I voided my warranty sticker for no reason. Um I may not be able to get this apart. Um yeah, cuz I got like this thing needs to be installed um very shortly. I don't want to have to

**Dave Jones:** damage it. I'm not sure what the the deal is. I can get this plastic case off here, but that doesn't help much. Maybe I need to like I'd have to take out all the boards in here to potentially get it

**Dave Jones:** something else. I can see another bracket in there, and it's got some screws going in that direction, so might have to get like This is not designed for serviceability. Um oops. Sorry. Um This might be as big a teardown as we

**Dave Jones:** get, uh which is not really a teardown cuz I haven't really torn it apart at all, but I've destroyed my warranty void if seal broken sticker. I don't think so. Um I don't want to have to start taking out

**Dave Jones:** everything internally and then trying to figure out how to get that off. There's no other screws. It's one big metal case, but it doesn't seem to lever off the back. Well, it turns out my spidey sense about tearing this thing down was right. I

**Dave Jones:** could sort of feel that I had to disconnect all of the cables and things and all the boards in that front uh section before I could actually pull the whole thing out. So, yeah, sorry. I just I'm not going to do that for an inverter

**Dave Jones:** that's being installed in very shortly. But, full credit to uh um Alubi maintenance center if I'm pronouncing that correctly. So, I'll link that in down below. Um he's done a teardown video on uh the 03 LP 1. This

**Dave Jones:** is mine is the 04, but it looks almost identical. So, yeah, you can see the heat This heatsink on the back is a little bit uh different. Mine is like a different uh molding for that, but all the screws are all in exactly the same

**Dave Jones:** place. The case is exactly the same inside looks exactly the same. So, he's doing a repair on this. So, he's got to tear the entire thing down to the board uh level. And he actually uh confirms in this video, there's no voice, but with

**Dave Jones:** overlays that yeah, it's really tricky to tear this thing down. You have to uh really, you know, uncable manage all of So, he's taken out like uh the power switch and all the cabling all all hooked up to there. So, he's had to take

**Dave Jones:** all this out before he could actually get in there. And he had to See, he had to get that board out and everything before he actually uh took was able Look, he's in line. And then that board has to be shoved under. Right? So, yeah,

**Dave Jones:** sorry. This is the reason that I didn't uh tear this thing down. Yeah, my my spidey sense told me this was not good. Anyway, um it's starting to look very good inside. So, I'll I'll link in the full video down below. So, there it is.

**Dave Jones:** Yeah, confirmed. Seems hard to disassemble this inverter for the first time. Yeah, it's it's just you got to take apart all of the stuff on the all the wiring on the front end and everything else. Anyway, um I'll I'll

**Dave Jones:** link in the video, so please watch it if you want to watch the uh full thing. But, uh what what we want to see is like like all the like all the cables are labeled, they're heat shrunk, they're uh

**Dave Jones:** terminal um you know, screwed terminal all very nicely. Everything looks very good. But, everyone wants to know what the caps are. Nichicons, CHECK IT OUT. JAPANESE CAPS, ABSOLUTELY FANTASTIC. What do you mean, doc? All the best stuff is made in Japan.

**Dave Jones:** Unbelievable. Yep, yeah, top quality build and construction inside this thing. Nichicon caps, that's the main uh DC um filter cap there. And yeah, look, um like bus bar systems installed in here and everything. And look, there's all everything's routed out nicely.

**Dave Jones:** Everything's Everything's very good. I'm very impressed with the design and construction quality of this thing. Look, everything's cable tied, everything's uh sleeved, all the cables are uh sleeved going over here. Yeah, a lot of attention to detail in this. And

**Dave Jones:** this is one of the local lowest cost inverters on the market. Really is quite something. So, thank you very much, LUB uh maintenance center, for doing this. And he's got a whole bunch of other videos. Look, there's um some MOSFETs on

**Dave Jones:** the back. Oh, that's an interesting package, isn't it? Wow, look at that. Uh That's like a a jewel. Like package. Wow. If you If you know what MOSFET that is or what MOSFET pair that is, then I assume they're like a

**Dave Jones:** switching like you've got an integral switching pair and integral package. I don't think I've seen that before, but yeah, anyway, um I'll link in his video down below. Um excellent, he's got a whole bunch of them on his uh channel.

**Dave Jones:** So, thank you very much for that. So, if I watched this, I could have kept my warranty void uh sticker, but I Yeah, yeah, anyway. Trappy young players. This top end uh actually leaves off and look, you can

**Dave Jones:** see very nice attention to detail here. They've got sheets covering all the wiring going down here, but and you can see a whole bunch of whole bunch of caps in there and on one huge board and it's got

**Dave Jones:** standoffs. You know, the bottom half doesn't want to come off. It's It's It's not good. There's a trick to this. There's a trick to it unfortunately, which I do not have. So much for the teardown. Yeah, what what what what. So

**Dave Jones:** unfortunately, I don't want to incur the wrath of the Murphy God in in doing this just days before I have to get this installed. That would really ruin my installation. So, unfortunately, we tried, but it wasn't that easy to get. So, that's an

**Dave Jones:** embarrassing wimp out attempt at tearing down this thing. I was hoping that it would just like fall off easy and all the wiring would be on one side and it would just like leave her open like that for example. And yeah, no, there seems

**Dave Jones:** to be something stuck up here perhaps and there may be like maybe no easy way to get this apart or there could be a simple trick, but I don't can't seem to find it. So, unfortunately, that's the best I can do

**Dave Jones:** all right now. Yeah, I'm going to officially wimp out on that. Bummer. Cuz I want to see the quality of the caps in there. I don't know. I'll see if I can get a torch under there maybe. Hang on.

**Dave Jones:** I thought this was fanless, but don't know if you can see it, but I see a fan. I see a fan down in there like on an angle, which is kind of weird. I'm not sure what's going on there. There

**Dave Jones:** doesn't seem to be any vents. So, yeah, that's that's strange, but there is actually there's actually a tiny little fan in there. I thought this was a passive jobbie. Anyway, I've taken off the plastic here and then we can see

**Dave Jones:** uh more of the wiring inside there and we can see the gen. Ah, I thought they were current shunts, but they're not. They're actually just um extra load current carrying capacity cuz they couldn't get enough copper on the PCB there. So,

**Dave Jones:** they're putting the massive jumper links in there um to increase the current carrying capacity instead of going to like 12 oz copper or something absolutely enormous like that, um they just put in these big links. That's nice, really nice attention to

**Dave Jones:** detail there. So, anyway, that goes down to a lower board down there and everything looks really neat and tidy and professional. So, quite happy with that. There's a current transformer down there. Is that the grid transformer? It has an external

**Dave Jones:** connection for a grid transformer. So, I'm not not sure what's going on down there. Yeah, there you go. You should be able to make out the part number on that jobbie there. So, little current transformer, that's yeah. Um that looks to be the grid side of

**Dave Jones:** things. Another couple of big-ass relays in there. Another big ferrite under there for the gen and the load. You know, like all really nice attention to detail in terms of like heat shrink tubing all over all of these ribbon

**Dave Jones:** cables so that they don't accidentally during the assembly process uh get you know, little burrs on the metal work here. They they don't cut through the cables. So, you know, there's really quite a lot of attention to detail in

**Dave Jones:** here. I'm liking the build quality. I really like what I'm seeing from what I can see anyway so far. So, pretty impressed. It's a BC55040. It's all It's got all the requisite ratings and everything and approvals and stuff. So, yeah, that's an overload uh

**Dave Jones:** there. So, it'll just uh pop up and allows you to reset it there if you really want to. But, yeah, I'm really liking uh what I'm seeing in this. It's uh really quite nice. Um and yeah, you can see the uh D9 interface uh down in

**Dave Jones:** there for the uh Wi-Fi and um external uh comms as well to plug in. Anyway, um that's barely not even a teardown, half-assed teardown on the DI uh Sun whatever bunch of numbers um inverter and they come in different

**Dave Jones:** and this is uh the official imported uh Australian version. You can buy them on AliExpress. I think you can import them direct, I think I don't know. You probably don't have to change the dip switches, but don't quote me on that.

**Dave Jones:** So, yeah, $1,600 5 kW hybrid inverter with uh like external generator which supports microinverters and all the different on-grid, off-grid uh modes and a ton of stuff. Um absolutely uh incredible and so, I don't know of a similar hybrid inverter with all these

**Dave Jones:** uh features on it. So, it's you know, it's really is quite uh something. So, anyway, um the proof will be in the pudding after I install it and uh set it up and have it running for a couple of

**Dave Jones:** years, but anyway, future videos uh to come on that. So, yeah, I'm completely replacing me old uh 3 kW Sunny Boy system with those uh 250 W uh panels. Got all new uh panels and uh yeah, it's all going to be remounted along with the

**Dave Jones:** uh Enphase uh system. I'll still be having the two split systems and apparently it has some app which is Solarman pv.com pro.solarmanpv.com and that's where you can upload your data to and whatnot. Um I don't know, but uh yeah, it it looks like a pretty

**Dave Jones:** cool bang for buck inverter. So, I hope it goes well, fingers crossed and uh we'll see this in future videos. Anyway, if you liked that half-assed half-assed teardown, give it a thumb sideways and as always, comment down below. Catch you next time.
