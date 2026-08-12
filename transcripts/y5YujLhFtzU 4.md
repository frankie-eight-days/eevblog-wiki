---
video_id: y5YujLhFtzU
title: EEVblog 1610 - Deye 5kW Hybrid Solar Inverter
url: https://www.youtube.com/watch?v=y5YujLhFtzU
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 30, "3": 38, "4": 50, "5": 63, "6": 75, "7": 87, "8": 99, "9": 110, "10": 125, "11": 136, "12": 145, "13": 161, "14": 171, "15": 182, "16": 198, "17": 205, "18": 216, "19": 227, "20": 237, "21": 250, "22": 263, "23": 273, "24": 281, "25": 294, "26": 307, "27": 318, "28": 334, "29": 345, "30": 358, "31": 369, "32": 380, "33": 395, "34": 401, "35": 411, "36": 422, "37": 434, "38": 447, "39": 460, "40": 471, "41": 481, "42": 495, "43": 505, "44": 516, "45": 524, "46": 534, "47": 546, "48": 564, "49": 576, "50": 593, "51": 608, "52": 628, "53": 644, "54": 656, "55": 669, "56": 681, "57": 693, "58": 700, "59": 720, "60": 734, "61": 744, "62": 753, "63": 762, "64": 778, "65": 789, "66": 800, "67": 809, "68": 820, "69": 829, "70": 844, "71": 858, "72": 872, "73": 884, "74": 894, "75": 905, "76": 915, "77": 929, "78": 941, "79": 951, "80": 967, "81": 990, "82": 1003, "83": 1015, "84": 1024, "85": 1031, "86": 1050, "87": 1073, "88": 1087, "89": 1097, "90": 1106, "91": 1129, "92": 1139, "93": 1155, "94": 1168, "95": 1182, "96": 1190, "97": 1209, "98": 1221, "99": 1234, "100": 1244, "101": 1258}
---

**Dave Jones:** Hi, welcome to an exciting teardown. We've got a solar inverter for you. This is a DIY inverter. It's a Sun 5 K SG04LP1A AU, the Australian model for those playing along at home.

**Dave Jones:** It's a 5 kW hybrid inverter. Yes, I'm going to upgrade my original 3 kW Sunny Boy inverter at home. So, stay tuned for future videos on that. But, before this gets installed next week, I just wanted to do a teardown.

**Dave Jones:** Let's go. This should be exciting. Look at this bad boy. It's a bit of a beast. We've got giant heat sinks on it. So, this is We'll show you the specs.

**Dave Jones:** And you'll have to read the specs sideways if you're really interested. Anyway, a hybrid inverter IP 65. So, you know, good enough for, you know, outdoor mounting and rain and whatnot.

**Dave Jones:** It's a nominal 5 kW inverter, but it can actually do 65 100 W 6.5 kW peak. And the reason I picked this DIY inverter is cuz it supports a ton of different batteries.

**Dave Jones:** So, there's no vendor lock-in on your batteries. Anyway, that'll be the subject of a future videos. But, it supports a 5 kW charge and discharge from the battery as well.

**Dave Jones:** And also 5 kW into the grid. But, as I said, 6 and 1/2 kW peak PV solar input. And also, it's got an emergency backup load on it as well, which I'm going to utilize.

**Dave Jones:** Now, unfortunately, I might have guessed the sizing because I It says here the PV input power per string is 3250 W. I've actually got 3.33, I think it is.

**Dave Jones:** So, I might have to remove a panel from each of my strings. Anyway, oops. And the IO here, we've got our two PV strings, standard MC4 connectors on the input here.

**Dave Jones:** That's nice. Battery input plus and minus, I think it's 35 sq mm copper as its rating. It's got two com ports for the RS485 and CAN for the any battery and other coms.

**Dave Jones:** It's got like four different cables, so you can basically have four weather proof cables coming out of there. So it does actually come with a Wi-Fi dongle that just plugs into a D9 connector in there and has an antenna sticking out the bottom.

**Dave Jones:** I'll actually show you that today. And one of the most interesting things about this inverter is it's got a generator input. So not you know like a diesel generator input but that also supports inverters.

**Dave Jones:** So microinverters. So in theory, I could actually put all of my Nphase microinverter system into here. But unfortunately, I can't do that in a practical sense because I've already got 5 kW maximum over here and it's a 5 kW max inverter.

**Dave Jones:** But you can actually put microinverters into the generator input. That is really cool. I haven't seen another I don't know. Leave it in the comments if you've seen another inverter that you've seen can do that.

**Dave Jones:** Now, this is the emergency load output. I will be powering my fridges off this and some emergency power points and and things. But some people power their entire homes from the emergency off-grid backup.

**Dave Jones:** So it's like it automatically switches over. So if you're in an off-grid property for example, you would plug it into here cuz you don't have a grid connection. So you plug your whole home into here and well, you couldn't you can plug your grid in as well if you have it.

**Dave Jones:** But your whole house load if you if you want to if you had a big enough inverter. And I believe you can have up to 16 of these inverters in parallel.

**Dave Jones:** So that's really cool. So you can actually power your entire house from there. But I won't be doing that for practical reasons cuz I've also got my 5 kW Nphase system as well which is on the grid.

**Dave Jones:** So yeah, and this is only a 5 kW total inverter. So anyway, yeah, very cool. The flexibility on this thing is incredible. That's why I bought it. Big clunking PV switch there.

**Dave Jones:** That'll be in series with the panel. So you don't need an external box. Very nice. Um and a big nice like elevator type on off button. That's really sweet.

**Dave Jones:** And as you can see, it's all undercut here and it's just all heat sink on the back here. And we can check that out. Wow, look at that. So, that's our mounting uh bracket that goes on the wall and then you just lift it and hook it in place.

**Dave Jones:** But yeah, this looks like two different heat sinks here. One down here, which is one big solid array in there. That'd be like for where your big MOSFETs are mounted to and just a more general purpose one.

**Dave Jones:** I don't know. Might have one might be for the inverter, one might be for the battery type system. I don't know. That's why we're going to hopefully tear it apart.

**Dave Jones:** So, fingers crossed I can actually do it without damaging it. And that's what it looks like on the front. There's a nice big weatherproof access panel here with a big O-ring seal.

**Dave Jones:** Have a look at that. And a big color LCD graphical LCD display on here. So, it's very nice from a display point of view and some indicators for your DC string, your AC, your normal.

**Dave Jones:** And there's a ton of different configurations you can put this thing in. It's absolutely amazing. I've never seen an inverter like it. Anyway, I won't go through it in detail, but it has all different configuration modes where, you know, a basic mode like this, a basic mode with backup.

**Dave Jones:** That's how I'll be using this thing even I don't have a diesel generator. I do actually have the ability to put like extra microinverter. Maybe that 3 miles one.

**Dave Jones:** I might actually experiment with that and put in. So, you can have a smart load configurations. Then you can have on generator plus AC couple configurations, on load plus AC couple configurations, on grid plus AC couple configurations.

**Dave Jones:** And there's lots of other little tweaks and stuff you can do it. Anyway, you can do a ton of stuff with this. It's just absolutely incredible. It even had something for wind turbines up here.

**Dave Jones:** Look at that. There's some connection diagrams, but it does have an installation manual. Didn't come with it though, which is a bit disappointing. Anyway, this one cost me 1,600 Aussie dollaridoos from the local supplier Dual Power.

**Dave Jones:** So, I'll link them and link them in down below if you want one of these bad boys. So, this is incredibly cheap. I got to say this is probably the best bang for buck inverter on the market.

**Dave Jones:** Yes, it is made in China, but DIY pretty big. I'll put in some photos of their factories and whatnot. And they're a, you know, a pretty big player, but they're not one of the more well-known brands.

**Dave Jones:** But, just the ability of this to run like tons of different different chemistry and type batteries. I'm not locked into any battery configuration. I can even run old 12-V, you know, lead-acid batteries if I want.

**Dave Jones:** Now, there seems to be some confusion over the name. I call it DIY because I think there's a capital D and there's an I in there with the dot.

**Dave Jones:** So, I think they want us to pronounce it DIY, but I've heard it pronounced day-e, day-a, all sorts of things like that. But, I'm going to call it DIY.

**Dave Jones:** I think it's correct, but I don't know. Company official, correct me down below. Warranty void if seal broken, huh? Well, let's see if we can uh get that out.

**Dave Jones:** Get a I've done a video Oh, no, void. There you go. No, I think I voided it. That hasn't worked. My technique of the No, no, that's That's pretty good void sticker.

**Dave Jones:** Oops. Okay, if we have a look in the access panel here and you can see the nice rubber baby buggy bunker seal around the uh window there. Have to keep this thing tilted.

**Dave Jones:** Um it's a little bit hard, but there you go. You've got all your basic wiring. There's that PV switch on the side. So, these are your MC4 string wiring coming in and then just going out the bottom there.

**Dave Jones:** And then that's our power clunk and power switch on the side. Got a ferrite down there, and those two gigantic screw terminals down there are your battery. So, your battery your wiring just comes in there, and you screw them down.

**Dave Jones:** As I said, I think the spec is 35 square mil or something like that. Then you've got all your various interfaces down here. There's an earth screw terminal block, nice.

**Dave Jones:** So, you've got your grid, your load, your generator. Then there's various RJ45s around here. So, they're the like there's an external meter if you want it. RS485, CAN, and and then we've got some little screw terminals here.

**Dave Jones:** They're like you can get a temp sensor. In fact, it comes with a temp temp sensor that goes into 12-V lead-acid battery. So, if you want to hook those directly on, it all comes with that.

**Dave Jones:** Couple of dip switches for various mode and country settings and things like that, I guess. And there's a couple of relays down there associated with that. So, can't see a huge amount.

**Dave Jones:** That looks like a cutout circuit breaker. That like looks like it'll pop up. No, that don't that isn't like an anti-tamper thing on the front. It's too low down for that.

**Dave Jones:** Gigantic varistor down there, and can see some big current shunt links down behind that, but can't see a huge amount more. Let's try and open the rest of it.

**Dave Jones:** Okay, it looks like this heatsink is screwed internally to this larger heatsink. So, I think if I get the outside screws here, I'm hoping this whole thing will just lift off in one side.

**Dave Jones:** That's my guess. So, anyway, comically long screwdriver time, and uh let's go. So, if there is this is designed well, I shouldn't you know break any thermal you know, heatsink uh connections or anything.

**Dave Jones:** It should just hold the case on it. It should pivot out. That's the plan. But, I'm assuming that the designers have designed it for a little bit of serviceability if not assembly.

**Dave Jones:** So, we'll see what happens. Anyway, if this does fail and they don't honor the warranty, then uh Um definitely thumbs up uh and comment down below and share this video cuz I I might need the ad revenue.

**Dave Jones:** Um And I don't buy the merch on my store. Buy a multimeter from me, please. evblog.store They put an access hole here for this screw. That's nice. Okay, I think I got them all out.

**Dave Jones:** No, it doesn't doesn't want to pop out off. Oh, no, unfortunately, it's not going to come off because Look, this seems to be screwed. As I said, this heatsink here is screwed from the inside, and yet I can't access the inside, so uh cuz there's no front panel.

**Dave Jones:** It's like one big It's one big case. So, I'm not Damn, I voided my warranty sticker for no reason. Um I may not be able to get this apart.

**Dave Jones:** Um yeah, cuz I got like this thing needs to be installed um very shortly. I don't want to have to damage it. I'm not sure what the the deal is.

**Dave Jones:** I can get this plastic case off here, but that doesn't help much. Maybe I need to like I'd have to take out all the boards in here to potentially get it something else.

**Dave Jones:** I can see another bracket in there, and it's got some screws going in that direction, so might have to get like This is not designed for serviceability. Um oops.

**Dave Jones:** Sorry. Um This might be as big a teardown as we get, uh which is not really a teardown cuz I haven't really torn it apart at all, but I've destroyed my warranty void if seal broken sticker.

**Dave Jones:** I don't think so. Um I don't want to have to start taking out everything internally and then trying to figure out how to get that off. There's no other screws.

**Dave Jones:** It's one big metal case, but it doesn't seem to lever off the back. Well, it turns out my spidey sense about tearing this thing down was right. I could sort of feel that I had to disconnect all of the cables and things and all the boards in that front uh section before I could actually pull the whole thing out.

**Dave Jones:** So, yeah, sorry. I just I'm not going to do that for an inverter that's being installed in very shortly. But, full credit to uh um Alubi maintenance center if I'm pronouncing that correctly.

**Dave Jones:** So, I'll link that in down below. Um he's done a teardown video on uh the 03 LP 1. This is mine is the 04, but it looks almost identical.

**Dave Jones:** So, yeah, you can see the heat This heatsink on the back is a little bit uh different. Mine is like a different uh molding for that, but all the screws are all in exactly the same place.

**Dave Jones:** The case is exactly the same inside looks exactly the same. So, he's doing a repair on this. So, he's got to tear the entire thing down to the board uh level.

**Dave Jones:** And he actually uh confirms in this video, there's no voice, but with overlays that yeah, it's really tricky to tear this thing down. You have to uh really, you know, uncable manage all of So, he's taken out like uh the power switch and all the cabling all all hooked up to there.

**Dave Jones:** So, he's had to take all this out before he could actually get in there. And he had to See, he had to get that board out and everything before he actually uh took was able Look, he's in line.

**Dave Jones:** And then that board has to be shoved under. Right? So, yeah, sorry. This is the reason that I didn't uh tear this thing down. Yeah, my my spidey sense told me this was not good.

**Dave Jones:** Anyway, um it's starting to look very good inside. So, I'll I'll link in the full video down below. So, there it is. Yeah, confirmed. Seems hard to disassemble this inverter for the first time.

**Dave Jones:** Yeah, it's it's just you got to take apart all of the stuff on the all the wiring on the front end and everything else. Anyway, um I'll I'll link in the video, so please watch it if you want to watch the uh full thing.

**Dave Jones:** But, uh what what we want to see is like like all the like all the cables are labeled, they're heat shrunk, they're uh terminal um you know, screwed terminal all very nicely.

**Dave Jones:** Everything looks very good. But, everyone wants to know what the caps are. Nichicons, CHECK IT OUT. JAPANESE CAPS, ABSOLUTELY FANTASTIC. What do you mean, doc? All the best stuff is made in Japan.

**Dave Jones:** Unbelievable. Yep, yeah, top quality build and construction inside this thing. Nichicon caps, that's the main uh DC um filter cap there. And yeah, look, um like bus bar systems installed in here and everything.

**Dave Jones:** And look, there's all everything's routed out nicely. Everything's Everything's very good. I'm very impressed with the design and construction quality of this thing. Look, everything's cable tied, everything's uh sleeved, all the cables are uh sleeved going over here.

**Dave Jones:** Yeah, a lot of attention to detail in this. And this is one of the local lowest cost inverters on the market. Really is quite something. So, thank you very much, LUB uh maintenance center, for doing this.

**Dave Jones:** And he's got a whole bunch of other videos. Look, there's um some MOSFETs on the back. Oh, that's an interesting package, isn't it? Wow, look at that. Uh That's like a a jewel.

**Dave Jones:** Like package. Wow. If you If you know what MOSFET that is or what MOSFET pair that is, then I assume they're like a switching like you've got an integral switching pair and integral package.

**Dave Jones:** I don't think I've seen that before, but yeah, anyway, um I'll link in his video down below. Um excellent, he's got a whole bunch of them on his uh channel.

**Dave Jones:** So, thank you very much for that. So, if I watched this, I could have kept my warranty void uh sticker, but I Yeah, yeah, anyway. Trappy young players. This top end uh actually leaves off and look, you can see very nice attention to detail here.

**Dave Jones:** They've got sheets covering all the wiring going down here, but and you can see a whole bunch of whole bunch of caps in there and on one huge board and it's got standoffs.

**Dave Jones:** You know, the bottom half doesn't want to come off. It's It's It's not good. There's a trick to this. There's a trick to it unfortunately, which I do not have.

**Dave Jones:** So much for the teardown. Yeah, what what what what. So unfortunately, I don't want to incur the wrath of the Murphy God in in doing this just days before I have to get this installed.

**Dave Jones:** That would really ruin my installation. So, unfortunately, we tried, but it wasn't that easy to get. So, that's an embarrassing wimp out attempt at tearing down this thing. I was hoping that it would just like fall off easy and all the wiring would be on one side and it would just like leave her open like that for example.

**Dave Jones:** And yeah, no, there seems to be something stuck up here perhaps and there may be like maybe no easy way to get this apart or there could be a simple trick, but I don't can't seem to find it.

**Dave Jones:** So, unfortunately, that's the best I can do all right now. Yeah, I'm going to officially wimp out on that. Bummer. Cuz I want to see the quality of the caps in there.

**Dave Jones:** I don't know. I'll see if I can get a torch under there maybe. Hang on. I thought this was fanless, but don't know if you can see it, but I see a fan.

**Dave Jones:** I see a fan down in there like on an angle, which is kind of weird. I'm not sure what's going on there. There doesn't seem to be any vents.

**Dave Jones:** So, yeah, that's that's strange, but there is actually there's actually a tiny little fan in there. I thought this was a passive jobbie. Anyway, I've taken off the plastic here and then we can see uh more of the wiring inside there and we can see the gen.

**Dave Jones:** Ah, I thought they were current shunts, but they're not. They're actually just um extra load current carrying capacity cuz they couldn't get enough copper on the PCB there. So, they're putting the massive jumper links in there um to increase the current carrying capacity instead of going to like 12 oz copper or something absolutely enormous like that, um they just put in these big links.

**Dave Jones:** That's nice, really nice attention to detail there. So, anyway, that goes down to a lower board down there and everything looks really neat and tidy and professional. So, quite happy with that.

**Dave Jones:** There's a current transformer down there. Is that the grid transformer? It has an external connection for a grid transformer. So, I'm not not sure what's going on down there.

**Dave Jones:** Yeah, there you go. You should be able to make out the part number on that jobbie there. So, little current transformer, that's yeah. Um that looks to be the grid side of things.

**Dave Jones:** Another couple of big-ass relays in there. Another big ferrite under there for the gen and the load. You know, like all really nice attention to detail in terms of like heat shrink tubing all over all of these ribbon cables so that they don't accidentally during the assembly process uh get you know, little burrs on the metal work here.

**Dave Jones:** They they don't cut through the cables. So, you know, there's really quite a lot of attention to detail in here. I'm liking the build quality. I really like what I'm seeing from what I can see anyway so far.

**Dave Jones:** So, pretty impressed. It's a BC55040. It's all It's got all the requisite ratings and everything and approvals and stuff. So, yeah, that's an overload uh there. So, it'll just uh pop up and allows you to reset it there if you really want to.

**Dave Jones:** But, yeah, I'm really liking uh what I'm seeing in this. It's uh really quite nice. Um and yeah, you can see the uh D9 interface uh down in there for the uh Wi-Fi and um external uh comms as well to plug in.

**Dave Jones:** Anyway, um that's barely not even a teardown, half-assed teardown on the DI uh Sun whatever bunch of numbers um inverter and they come in different and this is uh the official imported uh Australian version.

**Dave Jones:** You can buy them on AliExpress. I think you can import them direct, I think I don't know. You probably don't have to change the dip switches, but don't quote me on that.

**Dave Jones:** So, yeah, $1,600 5 kW hybrid inverter with uh like external generator which supports microinverters and all the different on-grid, off-grid uh modes and a ton of stuff. Um absolutely uh incredible and so, I don't know of a similar hybrid inverter with all these uh features on it.

**Dave Jones:** So, it's you know, it's really is quite uh something. So, anyway, um the proof will be in the pudding after I install it and uh set it up and have it running for a couple of years, but anyway, future videos uh to come on that.

**Dave Jones:** So, yeah, I'm completely replacing me old uh 3 kW Sunny Boy system with those uh 250 W uh panels. Got all new uh panels and uh yeah, it's all going to be remounted along with the uh Enphase uh system.

**Dave Jones:** I'll still be having the two split systems and apparently it has some app which is Solarman pv.com pro.solarmanpv.com and that's where you can upload your data to and whatnot.

**Dave Jones:** Um I don't know, but uh yeah, it it looks like a pretty cool bang for buck inverter. So, I hope it goes well, fingers crossed and uh we'll see this in future videos.

**Dave Jones:** Anyway, if you liked that half-assed half-assed teardown, give it a thumb sideways and as always, comment down below. Catch you next time.
