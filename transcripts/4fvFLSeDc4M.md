---
video_id: 4fvFLSeDc4M
title: EEVblog #1306 (1 of 5): 3 Cent Micro - Open Source Programmer
url: https://www.youtube.com/watch?v=4fvFLSeDc4M
source: youtube-asr
timestamps: {"0": 0, "1": 19, "2": 35, "3": 48, "4": 59, "5": 75, "6": 93, "7": 104, "8": 114, "9": 132, "10": 143, "11": 162, "12": 174, "13": 198, "14": 213, "15": 233, "16": 243, "17": 258, "18": 271, "19": 285, "20": 307, "21": 321, "22": 330, "23": 341, "24": 351, "25": 365, "26": 373, "27": 387, "28": 399, "29": 415, "30": 427, "31": 445, "32": 453, "33": 468, "34": 482, "35": 493, "36": 508, "37": 519, "38": 529, "39": 538, "40": 555, "41": 567, "42": 581, "43": 594, "44": 618, "45": 630, "46": 638, "47": 652, "48": 661, "49": 680, "50": 692, "51": 707, "52": 718, "53": 731, "54": 742, "55": 758, "56": 770, "57": 782, "58": 795, "59": 802, "60": 822, "61": 834, "62": 859, "63": 870, "64": 881, "65": 889, "66": 900, "67": 914, "68": 924, "69": 946, "70": 956, "71": 970, "72": 980, "73": 993, "74": 1007, "75": 1017, "76": 1029, "77": 1055, "78": 1066, "79": 1078, "80": 1086, "81": 1103, "82": 1116, "83": 1124, "84": 1138, "85": 1146, "86": 1155, "87": 1168, "88": 1176, "89": 1192, "90": 1206, "91": 1218, "92": 1232, "93": 1244, "94": 1253, "95": 1266, "96": 1280, "97": 1288, "98": 1303, "99": 1320, "100": 1331, "101": 1340, "102": 1355, "103": 1363, "104": 1379, "105": 1395, "106": 1405, "107": 1416, "108": 1431, "109": 1442, "110": 1455, "111": 1472, "112": 1481, "113": 1494, "114": 1507, "115": 1517, "116": 1526, "117": 1536, "118": 1550, "119": 1560, "120": 1575, "121": 1589, "122": 1601, "123": 1610, "124": 1628, "125": 1639, "126": 1650, "127": 1662, "128": 1678, "129": 1690, "130": 1700, "131": 1713, "132": 1724, "133": 1737, "134": 1750, "135": 1758, "136": 1770, "137": 1778, "138": 1791, "139": 1799, "140": 1813, "141": 1830, "142": 1844, "143": 1851, "144": 1864, "145": 1873, "146": 1884, "147": 1895, "148": 1912, "149": 1924, "150": 1935, "151": 1955, "152": 1966, "153": 1975, "154": 1989, "155": 2000, "156": 2014, "157": 2033, "158": 2055, "159": 2084, "160": 2110, "161": 2132, "162": 2158, "163": 2182, "164": 2203, "165": 2213, "166": 2225, "167": 2241, "168": 2256, "169": 2266, "170": 2275, "171": 2283, "172": 2293, "173": 2303, "174": 2318, "175": 2328, "176": 2345, "177": 2352, "178": 2370, "179": 2387, "180": 2399, "181": 2411, "182": 2420, "183": 2437, "184": 2451}
---

**Dave Jones:** Hi, in some previous videos, which I'll link in down below at the end, if you haven't seen them, we've taken a look at these remarkable 3 cent microcontrollers from a Taiwanese, not Chinese, company called Padauk, and how we can actually program them with the supplied programmer and also emulate them as well.

**Dave Jones:** So, this particular programmer and emulator is well, it's not that expensive, it is actually quite difficult to actually get a hold of one of these. You've got to buy it from like some weird like Asian supplies you've almost certainly never dealt with before.

**Dave Jones:** It's not that simple. So, a bunch of users on the EEVblog forum have can't list them all, sorry, but anyway, there's been a whole bunch of threads like over the last year on the EEVblog forum.

**Dave Jones:** What they've done is actually not only reverse engineered the Padauk microcontrollers, but they've also released free it's called free PDK and it's on the GitHub here, which I'll link in down below.

**Dave Jones:** And what they've got is open source programmer hardware, open source programmer software, and they've added support for the SDCC or small device C compiler to support most of the Padauk microcontrollers because they do actually have a lot of micros.

**Dave Jones:** If you go to their website, you know, they've got different ones, ones with 12-bit ADCs and 8-bit ADCs, ones without them and and stuff like that. And they do actually start, if you go over to LCSC here, who's one of the official suppliers from, they do actually start from like under 3 cents, in fact, like 2.7 of sort of Yankee cents.

**Dave Jones:** I've rounded it up to 3 cents. Remarkable that you can get a 3 cent microcontroller. And yes, you can afford to buy like tubes of them like this cuz they're so cheap.

**Dave Jones:** Now, these are actually one-time programmable microcontrollers, these cheap ones. I do believe like they have one or two models that do actually have flash memory, but the whole point of this is that they're 3 cents or they start from 3 cents.

**Dave Jones:** A more capable one with, you know, that might have some hardware UARTs and like ADCs and things like that might be in the order of 10 cents. But still, these are like three, four, five times cheaper than your other mainstream brand microcontrollers.

**Dave Jones:** And the problem with the Padauk microcontrollers not only the kind of difficult to get programmer / emulator for it is also the C compiler that they had available for it.

**Dave Jones:** It's I believe it's called mini C and it's not really properly ANSI C compatible. It's sort of Padauk's mini C quasi C, whatever you want to call it. So, you know, for those used to a programming in C, it's not really the best environment.

**Dave Jones:** But the fantastic thing about this is that quite a few smart cookies have reverse engineered this and actually there is now full open source hardware and software for programming, emulating as well.

**Dave Jones:** There's like they've got emulators which can put in VHDL and all sorts of stuff. And there's all sorts of examples. So, I thought we'd actually build up the open source programmer hardware and install the open source programmer software over a series of videos because I've already shot the videos and trust me, there's a lot of traps for young players in there and we come across them.

**Dave Jones:** So, it's sort of like, you know, play along with Dave as I attempt to build up because I've already built one, open source hardware and program these Padauk microcontrollers with proper open source, you know, like ANSI C compatible compilers.

**Dave Jones:** This is absolutely fantastic. So, hats off to everyone who's actually worked on this. And now it's completely opened up these remarkably cheap microcontrollers. So, it's gotten to a point now where, you might be able to feel confident about using these ridiculously cheap 3 cent microcontrollers in a commercial product.

**Dave Jones:** And that's the whole idea behind this is that they're remarkably low cost, but you know, it gave you the bit of heebie-jeebies before, but now with full open source support, let's see what we can do.

**Dave Jones:** So, rather than just shoot one concise video, what I thought I'd do is do sort of like a play along with Dave as I try and not only build the hardware, but also install the software and figure out how it all works.

**Dave Jones:** And then, you know, so you sort of sitting over my shoulder as I'm doing this over a series of five videos all linked in to a playlist somewhere up here where we actually go through step by step.

**Dave Jones:** So, unfortunately, if you're after a really short concise tutorial video on how to get these PSoC micros up and running, this video series might not be for you. It's like going through all the steps, warts and all, problems, solving things along the way, but hopefully that's more fun.

**Dave Jones:** So, anyway, this particular video I thought would be about actually it could really apply. It's not really for the PSoC one here. It's if you happen to see a project and it's available on say GitHub like an open source project, but nobody sells a kit or the finished product, and you want to build it, how do you go about it?

**Dave Jones:** In this video, we're going to part one, we're actually going to take a look at actually looking at the programmer hardware down here, going in there, and looking at how to order all the parts, how to order the PCBs, and that sort of jazz.

**Dave Jones:** Let's get to it. Right, so here we are. We're in the GitHub of our project that we want to manufacture, and we go down here easy PDK programmer hardware.

**Dave Jones:** So, we click on that, and we have a look at what's available. Maybe the readme has something. Probably want to do that, but this is the hardware that we want to build down here.

**Dave Jones:** There you go. Now, they actually come on a panel of four like this, but really I only wanted to order one. So, we'll go through the process of doing that.

**Dave Jones:** So, So, up here it looks like we have our schematic and we can check that. That's available as a PDF, very nice. I always appreciate when people produce the PDF, nice single sheet.

**Dave Jones:** There you go, it's laid out quite well. It's got all the stuff you need. So, beauty. You want to print that one out. Have it on your desk. So, you have easy reference.

**Dave Jones:** And here we go, we've got our bomb file down in here. We've got an assembled JPEG assembled JPEG, we've seen that before. And our bomb and our bomb for LCSC, which is where I'm going to actually order the parts from.

**Dave Jones:** Now, they didn't originally have this I I actually requested way back that I was having trouble importing their bomb in their original bomb, their CSV bomb here into LCSC.

**Dave Jones:** So, it was really nice of them to actually add this to the git. Because if you don't know, whether it's Mouser, Digi-Key, or LCSC, or any of the other component suppliers, most of them will have a Look, this one's it's right up the top here.

**Dave Jones:** It's got a bomb tool where you can import your bomb or bill of materials of all your parts. So, rather than having to like actually print out like you can just print it out, okay?

**Dave Jones:** The The traditional way to do this, here it is, right? So, they've got the manufacturer's part number. So, you can actually go here like this and let's say we wanted this STMicro like this, you could actually just go over here to like LCSC or Digi-Key or anyone like that and you can search for that.

**Dave Jones:** There it is, okay? And they've only got one. In some cases, there might be more variants. So, if we go over to Digi-Key, for example, and we search for that.

**Dave Jones:** There Oh, no, it's pretty That's part number's pretty specific. I think that's going to include the package. Okay, so what these variants are here, you can tell this is the specific part number like this, but this one is the same part number but has TR on the end.

**Dave Jones:** What TR stands for is tape and reel. So, if you're ordering a whole reel of them, then i.e. you're going to get your uh product uh machine assembled, you're going to get it pick and place assembled, then you want your chips on a reel.

**Dave Jones:** You don't want to just like loose in a bag or whatever because your assembler is not going to be happy with you and they're going to charge you a fortune to actually hand assemble those things on.

**Dave Jones:** So, if we actually go inside there, we can see that these are available on a available in a tray like this. So, once again, pick and place machines can actually pick and pick them from a tray, but generally I found that most assemblers would prefer tape and reel uh parts than uh trays.

**Dave Jones:** So, only get the trays if you absolutely have to uh or cut tape, which is if you just want to buy five of them cuz you're going to build five boards yourself and you're going to hand assemble them, you just get the cut tape.

**Dave Jones:** So, they just take a they just cut a bit off the tape or you can get a Digi-Reels, which is order as many as you want and they will re-reel, put them on a specific reel for you.

**Dave Jones:** They'll get their re-reeling machine out, they'll cut and take the cut tape, and they'll put it on a reel and they charge like $8. I think there's an $8 charge or something like that for the Digi-Reel.

**Dave Jones:** Anyway, um so, you can do that and then you can repeat ad nauseam. The good thing about this BOM is that it does actually have the part numbers. A lot of uh like projects out there, GitHub or otherwise, they won't bother with the manufacturer's part number, they'll just go, "Oh, it's a 47 microfarad cap.

**Dave Jones:** Why should I bother with the part number?" But, they've actually given you specific part numbers. But, for things like these uh like a 47 microfarad 1206 capacitor, for example, it the part number does not matter.

**Dave Jones:** It is not critical at all. As long as it's the same value and the same footprint, the the dielectric material of it's XR7 or it's Wi-Fi view or whatever it is, um it it's not going to matter a rat's ass, basically.

**Dave Jones:** Um unless you have some really specific uh niche application, in which case they really will uh specify and they should put a like a uh little asterisk on the schematic and annotate that saying it must be this part because reason.

**Dave Jones:** You know, so if you that's a little tip, if you're designing uh products, annotate your schematics with useful information like that. Anyway, so you can go, the point is you can actually go down and you know, copy all these one by one into your Digi-Keys or your Mousers or your LCSC's or whatever, and then you add them to your shopping cart up, you choose how many you want, you add them to your shopping

**Dave Jones:** cart, and it's tiresome. So, they have these bomb tools, which you can actually import bill of materials. And unfortunately, oops, they're out of stock of that microcontroller. Wah, wah, wah, wah.

**Dave Jones:** Good thing I don't have to order them now because I'm shooting this video quite some time after I've already received these things. I'm sort of back shooting. Is that a term?

**Dave Jones:** Uh it is now. And what you can do is you can just drag the uh XLS file in here, and often they will provide you a template of what format all the cells and things must be in.

**Dave Jones:** So, if you have a look over here, like uh they you know, usually have a format that these things have to be formatted uh into. So, you can select the file or just drag it in.

**Dave Jones:** And yes, I did this uh quite some time back. I had my parts sitting around for quite some time. Anyway, so I ordered 29 parts, and of course, if you don't know how to use you know, if you don't actually use Git, you can actually just uh download the zip here for the entire project, and this is what you do before you start.

**Dave Jones:** You just download the whole blinking lot. All right, so let me show you what happens if you just import the incorrect uh well, the just the regular CSV. Import the CSV like this.

**Dave Jones:** Boom. And here it is. Okay, it's imported it, but you have to like manually select like what things are what. And you know, it does work and it and it does actually have the the supplier is LCSC for all of these in their original bomb.

**Dave Jones:** And it does have the specific supplier part number LCSC part number. So, and then you've got to go over here. Well, yeah, no, you just ignore that. It's just a value.

**Dave Jones:** Then we've got quantity here, manufacturer part number, manufacturer. That'll be a package. Just put description for that. And then that we don't really need that. We can't just ignore that field.

**Dave Jones:** So, I don't know. We'll just put customer part number or whatever. So, we've now this is if we want to import like just a CSV into this tool. The bomb is in process.

**Dave Jones:** Boom. And now we have our entire bomb imported from the CSV. But of course, we could have just downloaded the specific bomb the bomb LCSC in LCSC format specifically.

**Dave Jones:** And you see, it wasn't that hard to actually do this. I think when I did it, there was some issue which made me uh I have to do the LC get into do the LCSC LCSC version.

**Dave Jones:** It wasn't this easy if I remember right. Anyway, here's all the parts. And you might have and it's got the quantity over here the purchase quantity. Let me Can I make my Maybe I'll make myself a bit smaller.

**Dave Jones:** Here you go. So, we've got the purchase quantities like this. And yeah, you might need two, but it says you need a minimum of 10 cuz they just won't sell you onesies, twosies, or one one two cent, right?

**Dave Jones:** So, and it tells you they come on cut tape and things like that. So, you notice that you know, tells you some are out of stock and things like that, which is really great.

**Dave Jones:** And it requests multiple of a because this is like a 20 ohm resistor. They're not going to cut off like three 20-ohm resistors. So, you've got to order 100, but the good thing about ordering because they're so cheap, and the good thing about the minimum order quantities like this is you'll be left over with leftover stock and you can use those to stock up your parts bin, which is absolutely fantastic.

**Dave Jones:** So, yeah, minimum of 20 of these little pin headers for example, you only need one. So, bingo, you've now got a whole bunch of pin headers, which can go in your parts drawer.

**Dave Jones:** Fantastic. So, anyway, after you're done all that, you'll notice that they're all ticked here, and you can add estimated total $7.90 once you've done all that. But anyway, so you can add to cart * 1, and bingo, we now have 28 items in our shopping cart, and we can just check out, and I think it has actually added minimum quantities.

**Dave Jones:** I think it has changed them all to minimum quantities like this. So, this is the minimum that you're going to get away with like this. So, how how what's our total?

**Dave Jones:** So, there's a few ones which are requested a quote and things like that. So, you might have to go for another 6.8 micro Henry inductor. It's not going to matter that much about the specs for that.

**Dave Jones:** It's just for a DC, you know, a fairly jelly bean DC to DC converter they need in here for the programming voltage. So, not not really a huge deal.

**Dave Jones:** Just pretty much choose any sort of similar footprint 6.8 micro Henry and you'll be right. No wackers. And it's not going to give us a subtotal, but anyway, there you go.

**Dave Jones:** That's a loading into the shopping cart, and you can whack some extra product. Always whack some extra products on there, including some micros to actually play around with. Beauty.

**Dave Jones:** So, anyway, yep, I've already ordered those before, so I'm not going to order those again. So, that is all the shopping cart experience. So, now, what we want to do is order the blank PCBs, of course.

**Dave Jones:** So, what we're going to do here is go into our PCB and what have we got? Gerbers no silk Here you go. And this is another one where I had to get them to actually add a specific single PCB in there because the files were only available on Easy-EDA.

**Dave Jones:** Well, they're available on Easy-EDA, that's right. I think they had the Easy-EDA project up here. So, I don't use the Easy-EDA but if you do, there you go. You might be able to load in your project.

**Dave Jones:** But, of course, like it could be available in KiCad format or Eagle or Altium or whatever format that they happen to use in that particular. So, they've got some adapter PCBs if you actually want the little adapters.

**Dave Jones:** But, these little adapters here I I actually just bought a bunch of these. They actually came with my EPROM programmer. I don't have it here. But, anyway, yeah, I bought these for my TL What is it?

**Dave Jones:** TL866 EPROM programmer. So, I already had a bunch of these little SO8 little adapter things. So, I didn't need to manufacture those. But, if you do, you might have to get those PCBs manufactured as well.

**Dave Jones:** So, let's go into PCB here. So, in here they've got a they've got a the zip file for the Gerbers and also a subdirectory for the Gerbers with no silk means no overlay, no silk screen overlay.

**Dave Jones:** As these actually these boards will actually come and I'll talk about that in the next video. But, it looks like it's got everything here. It's got the board outline layer.

**Dave Jones:** That'll be the mechanical outline layer. It's got the bottom copper layer. It's got the bottom solder mask layer. It's got the through hole. That's what PTH stands for. That's through hole drill stuff.

**Dave Jones:** It's got the top layer copper. It's got the top uh power paste mask layer, which we don't need because we're not getting a paste mask stencil uh made. But if you do, if you want to get it or if your PCB supplier supplies a free uh like stainless steel or even a Mylar um paste mask and you like using solder paste and stuff like that, um then you

**Dave Jones:** might want to uh supply that. That might have to be supplied separately, but we're not going to worry about that. And the top solder mask layer. Um as uh it says in the title, there is no silk screen layer.

**Dave Jones:** But all of those files should come in the um silk here. Now, there is that panelized version we saw before that had four boards. I don't know why you'd want to build up four of these programmers.

**Dave Jones:** Usually, you only want uh one. I would prefer to do that. And then if you get that panel made, then uh if you want to be able to snap them off easily, you got to have V-scoring.

**Dave Jones:** And if you're getting one of the cheap uh prototype PCB services, you can't just do that. You can't just go, "Okay, I want my board, but it's it's only this big, but I also want four V- uh scoring grooves in there so I can snap them off." It doesn't work like that cuz V-scoring has to be done on a an entire panel basis.

**Dave Jones:** They can't just go in selectively like V-score your individual board. It it has to go through I've done a video on this showing you machine. They put the whole panel in like that.

**Dave Jones:** So you're going to share these panels. This is why they're so cheap. You share the panels with, you know, 100 other people. There's 100 other boards on the same panel that's being manufactured.

**Dave Jones:** And if you uh you pain in the ass you want your little V-score for the panel, they they're going to say, "No. We can manufacture the panel for you, but it's going to cost you a lot more because it has to go through its own separate process." So, yeah, don't do that.

**Dave Jones:** You can order four of them, but just say, "I don't want silk screen." And then but then they get all confused. But then they come back to you with questions.

**Dave Jones:** "Oh, do you really want V-scoring? If you do, and then like how do Do you want us to route it out? But they're too close to route at at routing paths and stuff like ah, it's just no.

**Dave Jones:** Get get your individual one-off boards made. So, there we go. That just has all the same stuff. We just want our one board. So, we can upload that. So, let's just go into JLCPCB, no recommendation.

**Dave Jones:** I just happen to use them and this is where I got my ones from. You may want to use your favorite PCB supplier, it doesn't matter. It rats really who you use to get these.

**Dave Jones:** So, anyway, uh two layers, 1.6 mm anyway. Let's just go into the quote tool and then we can dick around with it in there. Here you go. Oh, and we could have used any Gerber viewer to import and like look at those Gerber files, but JLCPCB have a Gerber viewer as well.

**Dave Jones:** A lot of the online ones have Gerber viewers, so we'll be able to see what it looks like before we get it made. You shouldn't have to make any tweaks yourself, but if you do, of course, you're probably better off doing that on the P original PCB file, which in this case I think's EasyEDA.

**Dave Jones:** Okay, this is 63 by 22 mm. And if you didn't have one to hand, you would have had to load that up in Gerber program and actually get your measurements there.

**Dave Jones:** 1.6 mm red because red goes faster, trust me. Surface finish, we don't want any of the ENIG, which is immersion nickel gold. We we don't want that fancy pancy gold rubbish.

**Dave Jones:** We'll just go with HASL, which is hot air surface leveling or with with lead. No, we'll just go to lead lead free. Oh, change red to there are very few people choose below combination.

**Dave Jones:** Okay. Oh, this is new. I've never seen this message before. Wow. There you go. Ex- extra $16 for the special process. This probably has to do with all their backlog and and stuff like that.

**Dave Jones:** The recent shutdowns and everything. I I've never I got mine made red. So, yeah. Sorry, yeah, I never got that message before. So, anyway, change red to green. Okay, we'll have green.

**Dave Jones:** Thank you very much. Um it never used to cost any difference. So, 1 oz copper is fine cuz there's no heavy currents on this thing. Gold fingers, no. Standard FR4 panel, no, we do not want a panel.

**Dave Jones:** Flying test, don't bother. I For a board like this, I wouldn't even bother to flying probe test. I just don't like wasting their time when it's like a nothing burger.

**Dave Jones:** But, you know, if you're like I think it Does it come for free? I think it comes I think Yeah, I think probe testing comes for free. It's like You know, they they might do it anyway cuz they manufacture it a whole panel.

**Dave Jones:** Cast related holes, no, they're the holes on the side of the board. No, we don't want those. Different designs, we've already got one design. Remove order number, yes. Yeah, yes, because otherwise they will put your order number on the board and that's really Do they charge you extra for that?

**Dave Jones:** They charge you extra to remove the order number. All right, we'll leave it on there. Cuz this is not, you know, a front panel board. It's not, you know, an important thing.

**Dave Jones:** So, yeah, they'll put their own custom order number on there. And the reason that they're charging you more for that is because I it's a manual process that they have to manually do it.

**Dave Jones:** But, then also when they get the big panel huge giant panel like this manufactured, then they need an individual order number on there so that they can track who that But, when they snap it out of the panel, they know who that's going to.

**Dave Jones:** So, they just have to manually check and that's an extra process that costs extra labor. So, they're going to charge you an extra what, buck or something for that, buck 50 or something.

**Dave Jones:** Anyway, we don't care about any advanced options. Four wire Kelvin test, no. Paper between PCBs, no. We don't care about any of that. Free SMT Free SMT assembly. Wow, really?

**Dave Jones:** Oh, there's a coupon for free SMT assembly. Jeez, anyway, no, we don't want that because we're going to assemble it ourselves. That's the whole point. Anyway, stencil all together with the PCB and you know, and yeah, look, if you want a stencil framework, no, we don't want fancy framework.

**Dave Jones:** Electropolishing, no fiducial, all that. No, we we we don't want a stencil. We just want our boards, thank you very much cuz we're going to hand solder all these.

**Dave Jones:** Anyway, let's add our Gerber file, okay? And you can actually just specify the zip file, so I will off screen here I'll specify the zip file and it just processes all the Gerber files and we shouldn't have any problems.

**Dave Jones:** It's pretty uh plain vanilla stuff that we're importing here. Come on, you can do it. You can do it. You can do it. Are you done yet? Uh it's stuck on 96%.

**Dave Jones:** What's going on? Your files have been successfully uploaded and it may take a few minutes to generate preview. It never used to take a few minutes. So, yeah, they've they've changed things since I last used it.

**Dave Jones:** Anyway, in the meantime, I thought I'd just um find a random online Gerber viewer. Here we go, um online Gerber viewer. New viewer, I don't know. Let's have a Let's have a go.

**Dave Jones:** Start viewer. Okay. Uh we got to log in. Bugger that. Online Gerber viewer, looks like PCB have one. PCB GoGo Gerber viewer, uh EasyEDA have one. Like yeah, there's lots of online Gerber viewers these days.

**Dave Jones:** This one didn't work. Don't like that one. Uh Upload Let's have a look. Let's actually do a little mini shootout of Gerber viewers, shall we? Online Gerber viewers, here we go.

**Dave Jones:** Passing. Oh, that was quick. Upload Oh, PCB Go That looks identical. No? No, it's not. Could be. Let me Yeah, that's I I think that's Is that the same?

**Dave Jones:** Uh uh please go to JLCPCB okay to view the Gerber. Do JLCPCB actually have an online Gerber viewer? No, they didn't. No, they don't have a Gerber viewer. It's only as part of the um ordering system.

**Dave Jones:** Anyway, here you go. Uh the PCB way one uh free PDK. There you go. There we just imported that. That looks fantastic, right? Here Here's the different uh layers.

**Dave Jones:** There you go. You can turn them off and on. Oh, wow, like that. That looks really good. Yep. Top Top of the board looks like they're all lined up.

**Dave Jones:** You know, nobody goofed the offsets or anything like that. Everything looks fine. There's no silkscreen. As I said, this text here is not silkscreen. That's actually embedded because look, you can see the gold color.

**Dave Jones:** It's not done as like white or, you know, some other silkscreen uh color. That's actually uh copper on the board. And that will um in our case, we're not ordering a gold flash uh PCB in immersion gold uh PCB.

**Dave Jones:** So, it won't come It'll come up silver instead of gold. It'll get, you know, that silvery uh lead-free rubbish color. And same with the uh text over here. But anyway, that's a good Gerber viewer.

**Dave Jones:** I like that. Oh, yeah. Nice. Nice. Anyway, you can see the the solder mask slither there. The expansion is quite large, I think. My board had more slither than Have they automatically expanded that?

**Dave Jones:** You can see the line going between the tight I mean, that that won't be manufacturable, right? I I I guarantee you, if they tried to manufacture I don't know the like that looks like a couple of thou um a couple of mil.

**Dave Jones:** A couple of thou A couple of thousands of an inch uh thickness. That's just not going to get manufactured. So, if they tried to do that um because some manufacturers I've done a video on this in the past, they will actually touch your Gerbers.

**Dave Jones:** I've got a I used to have a T-shirt, don't touch my Gerbers. Um and they will actually do the solder mask expansion around your pads. And I hate that.

**Dave Jones:** Hate that. Stop it. Anyway, the ones I got, I'm pretty sure, and as you'll see in my second video, the assembly video, the board I got, uh you can't see it here, but you'll see it in the second video, is that uh from JLCPCB, is that they didn't do the solder mask expansion.

**Dave Jones:** Anyway, I believe we are good. Our Our file's been uploaded. Didn't take that long. Uh you can just been saved to your file manager. And here it is. There we go.

**Dave Jones:** Can we go in and have a look at that? So, we click on our Gerber viewer there. It's got analysis. Uh minimum trace width is greater than 10 mil, minimum trace spacing is greater than 10 mil, minimum drill size.

**Dave Jones:** So, we're looking looking sweet. To get it manufactured. There we go. You can zoom in. Look, this has done the same thing. This Gerber viewer This is This is curious.

**Dave Jones:** It's done the same thing as what PCBWay showed, but as you'll see in the second video Oh. Solder mask doesn't look like that. So, it's much thicker. As you'll see.

**Dave Jones:** So, I I don't know what the deal is there. I don't know if they've changed something since I got my boards made or what, but uh that's interesting. Anyway, all we care about with the Gerber viewer here is that everything looks right.

**Dave Jones:** It looks like the final board which they show you over here. If you go over here, they will actually show you There you go. That's what it looks like.

**Dave Jones:** Um and that it looks exactly like that on the preview. So, what you see is what you get pretty much these days. So, I'm happy with that. So, we should just be able to uh like save that to our shopping cart.

**Dave Jones:** Anyway, look at this. I mean, crazy, right? Engineering fee four bucks. I mean, remove order number a dollar 50. It's still got the remove order under there. Remove order.

**Dave Jones:** No. I mean, like under 10 bucks. Like and it's like it's $18 $19 for DHL Express Priority Australia. Even that's cheap because, you know, it's it's tiny. It weighs absolutely nothing.

**Dave Jones:** But DHL Express Priority. Oh boy. Anyway, when I was a boy so we got five so we'll get five boards for our 10 bucks. Absolutely incredible. Plus plus the delivery's more expensive.

**Dave Jones:** Anyway, it's nuts. So that's what you have to go through to get your board uh manufactured. Now, of course, we could do uh let me show you the other one.

**Dave Jones:** Where was the good online viewer that we have? I really like this one. Let me choose the if you got the panel version of it. Let's upload the panel Whoa.

**Dave Jones:** Yeah, it didn't like that. There you go. Yeah, this is the issue that I had is that the panelized version that they had was not actually the full panelized Gerber.

**Dave Jones:** It was the one board like this and they didn't actually copy it on the Gerbers. Like so it like the data is physically not in the Gerber file for these other boards.

**Dave Jones:** It's supposed to be one, two, three, four. But there's only one board there. So that hasn't been rendered from EasyEDA or whatever package they used to do this in.

**Dave Jones:** Um it it just hasn't been done and they haven't produced those Gerbers right. So that's useless. So you don't want to get that manufactured. This is why don't touch panel manufacturing panels like this if you're just trying to get, you know, if you're just making your one-off board.

**Dave Jones:** Just, you know, it it's more hassle than it's worth. And as I said, even if this was imported properly and did actually copy over, then uh you would still have the issue of them questioning, "Oh, this looks like a panel." Cuz they're experts at doing this.

**Dave Jones:** They do it 100 times a day. And they'll go, "Oh, this looks like a panel. You want us to make a panel? Oh, do you want V-scoring or do you want uh routing in here?" And I believe this one um it didn't have enough room for the routing in there.

**Dave Jones:** So, it's got to be V-scored and things like that and then they won't do that on the prototype panel, as I said. And there is just a whole end of problem.

**Dave Jones:** So, just don't do it. Just don't muck around with the panels. So, hopefully, um, the GitHub project that you have will have individual files like and most of them will.

**Dave Jones:** I don't know why they bothered, um, like having a panel like this. And the original GitHub, that's all they had is they had the panels for this. And you can see the V-scoring in there, actually.

**Dave Jones:** There you go. You can see how that's actually V-scored all the way along there. So, these big cutting wheels come down and go And you can't do that on a panel that you share with other people.

**Dave Jones:** And just for kicks, uh, because they have an easy EDA project, I'm actually going to, I thought it was a browser-based thing. It's an online PCB tool, but you've got to download it.

**Dave Jones:** So, anyway, um, and easy easy it's all part of LCSC. They're the ones who do easy EDA and it's all integrated. So, in theory, um, you should be able to, uh, use LCSC for everything here, like designing the board, importing the bill of materials.

**Dave Jones:** They sell you the parts and they'll even assemble it, uh, for you. So, you know, if if somebody wanted, uh, they could be a complete turnkey solution here for using LCSC to get these, uh, manufactured.

**Dave Jones:** So, if somebody wanted to go, "Right, uh, yeah, I'd love I'd love to be able to sell these boards or whatever." So, even whether that's for profit or not for profit, whether you wanted to make these just make these boards available so people didn't have to build them up.

**Dave Jones:** If you wanted to promote these Peduq Micros and just make so people just buy the ready-made, uh, thing, uh, the ready-made programmer board here instead of, you know, and the firmware's already programmed instead of around with multiple videos, as you're going to, uh, see in this series of how much, um, you know, just little traps involved in not only hand-building the board.

**Dave Jones:** It takes, you know, hours to build it up. Then the microcontrollers blank, so you got to program that using DFU, and there's a few traps for young players in setting that thing up, as you'll see in in the coming videos and stuff like that.

**Dave Jones:** Anyway, I might I might say just for kicks, I might just download that and see if it loads in. See if the project loads in. There's nothing like pattern out a video.

**Dave Jones:** Next. Okay, it's installing. Run mode setting. Guess this is a little review of EasyEDA, is it? Teamwork, projects are stored on cloud server, work anywhere. Projects are stored on your own computer.

**Dave Jones:** That's yeah, teamwork is that and full offline, I think yeah, you probably have to pay for that cuz this is a free thing. Anyway, apply. Yeah, whatever. Happy to put on my C drive.

**Dave Jones:** Orlando Flynn, skip. User management area, we don't care. There you go. So, here's all the parts and these are all linked to their supply part numbers as well. So, I presume that like all of these part will have like Oh, no, LCSC parts.

**Dave Jones:** Here you go. And JLCPCB, no, they just link you over to the page, but anyway. Libraries, here you go. EasyEDA types, JLCPCB assembled. Ooh, okay. So, yeah, these are all the parts that presumably you can get as part of their assembly service.

**Dave Jones:** So, if you were looking for a turnkey solution for this, this is where you might want to modify. If you went right, you know, I I love these little pedook micros and I you know, I love to actually sell these little things made up and maybe in a nice little case, you might customize it or something like that and you program the micro for people so that you know, you can make a

**Dave Jones:** little little Midnight Engineering business selling these little pedook microcontroller boards. If you wanted to do that, if you wanted to and you wanted a turnkey solution, then you might want to modify the project and the bill of materials to use like specific you know parts like these caps for example that they actually yeah here we go capacitor arrays aluminium electrodes don't have any but multi-layer ceramic capacitors these are all the ones that

**Dave Jones:** they will you know we had we're talking about the 1206 one before I think we didn't we need like a 47 microfarad or something like that we probably don't need 47 microfarad like it doesn't matter so you might go oh let's just use a 4.7 microfarad so there it is so you might want to you know anyway hours and hours and hours involved in a tutorial of how to like modify a project

**Dave Jones:** like that but anyway what I want to do is I want to open a project open here we go and oh they can open Altium files Eagle files and KeyCAD files as well that's nice anyway we do have the file in here what where is it oh I'm in the wrong I'm in the wrong subdirectory right EasyEDA project here we go EasyEDA oh it's a zip I don't think I

**Dave Jones:** can open a zip no all right I just unzipped that so let's do that again one more time for the dummies there you go read me PCB JSON and schematic JSON files all right see we can open both at once can we you bet you yep it's loading in here you go here you go beauty all right space or R to rotate no wackers so there's there's our schematic

**Dave Jones:** so if you wanted to modify something so as I said like let's just go in and say as we said before oh no it wasn't it was 4.7 Mike wasn't 47 Mike was 4.7 but just say we wanted to change can we no you can't you can't double click ah here's the attributes over here here you go supplier LCSC Digi-Key Mouser element 4 wow that's nice okay supplier part

**Dave Jones:** number wow excellent so if you didn't have that sort of stuff in there, if you had a project that you wanted to get turnkey manufactured from say JLCPCB or you know, you can use others, but if you want to get it manufactured from them and they had the schematic file, then you can import like a KeyCAD schematic file, you can import that and then you can go through and you'd have to do each

**Dave Jones:** one, you know, you'd have to do each part, you'd have to go and then like find the specific part number and do all that sort of stuff, but anyway, oh, can we view data sheet for that, really?

**Dave Jones:** Yep, there you go. Takes you over to here and takes you over to the that's that's nice. Easy EDA actually pretty comprehensive. Must say I like that aspect of it.

**Dave Jones:** Anyway, here's our PCB, tada. So, if you wanted to make a few changes on here, you most certainly could. Oh, there you go. They've got live by default we've got live net view, net highlighting both and on both layers cuz we're not in presumably not in single layer mode if it's got that.

**Dave Jones:** Yeah, cuz sometimes you just want to work on a single layer. You don't want the other you want to view the other layers, you want them in the background there, but you don't want to be, you know, you don't want it to highlight this bloody one that's on the bottom layer there cuz you know, it's yeah, you don't want to dick around with that.

**Dave Jones:** Anyway, so Easy EDA, yeah, I've heard good things about it. If you want a turnkey solution and all their parts are in their inventory and stuff like that for simple, you know, you're not going to do hugely complex projects with it.

**Dave Jones:** I wouldn't recommend it. I'd recommend going to KeyCAD or Altium or something like that, you know, if you're really serious about, you know, doing high-level designs and things like that.

**Dave Jones:** I'm sure you could do it in Easy EDA, I don't know. Anyway, this is not going to be shooting CAD tool shootout, but there you go. It does load in.

**Dave Jones:** So, that's pretty cool. So, we could could have modified that and then how do we generate our Gerbers? I presume we can just go generate PCB Gerbers. There you go.

**Dave Jones:** PCB fabrication files, Gerbers. So, we if we did make our modifications, please save your file. Yeah, we can just go in there, generate the Gerbers and then upload them the same as what we saw before.

**Dave Jones:** So, there you go. That is just nice that that they make the project file like that available in the GitHubs. So, yeah. Easy EDA, neat. Once again, I don't know why they didn't do the uh silk screen on the thing cuz silk screen like comes for free these days.

**Dave Jones:** You get them on these uh panels and whatnot. And as you'll see in the assembly uh video of this board, um yeah, I would like the silk screen probably would have saved some time.

**Dave Jones:** Would have helped, but doesn't matter in the end. Anyway, so there you have it. That's a um a little bumble in look through uh getting a project, a PCB, and parts uh on ordered from a GitHub project like this.

**Dave Jones:** And it can be any project. It doesn't have to be this particular one, but this is what this uh series is about is building up this board. So, anyway, I have another four videos.

**Dave Jones:** The next one is building up this board. Then the video after that is uh programming the blank Atmel micro on here, not using an Atmel programmer, but actually using the USB port, using the uh serial boot USB serial bootloader that's uh automatically included.

**Dave Jones:** That's burnt into the silicon of the Atmel microcontroller. It's called DFU or device firmware update uh mode. So, and we had a few issues with that. And then we get into uh the SDCC, the small device C compiler uh that now supports these PSoC microcontrollers.

**Dave Jones:** And then I've got another one uh testing. Anyway, there's five videos. And And we had like a weird hardware issue in the last video. So, you want to It's spooky action at a distance.

**Dave Jones:** You'll want to see that one. So, there you go. Um I hope you like this. If you did like this If you do like this series and this video, please give it a big thumbs up and leave it in the comments down below.

**Dave Jones:** Uh as I said in my I think my final video of this series is that like this isn't just follow along with Dave as Dave goes through and installs these things for the first time.

**Dave Jones:** And hopefully, the whole idea behind that is that you learn a lot of stuff and learn about the hurdles on the way. Cuz yes, I could just produce a 10-20 minute polished video where nothing goes wrong and showing you how to actually, you know, in 10 easy steps, how to get this thing up and running and programming a part.

**Dave Jones:** But, you know, it's good learning process to see the fails along the way. And hopefully, that's what this series is going to do. So, there you go. Five video series all linked somewhere.

**Dave Jones:** Yeah, you know what to do. Catch you next time.
