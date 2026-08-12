---
video_id: 2v5IvaWrPKk
title: EEVblog #1193 - KiCAD PCB 4 Layer Swapping & Stackup
url: https://www.youtube.com/watch?v=2v5IvaWrPKk
source: youtube-asr
timestamps: {"0": 0, "1": 18, "2": 26, "3": 40, "4": 54, "5": 74, "6": 92, "7": 106, "8": 118, "9": 127, "10": 140, "11": 147, "12": 166, "13": 176, "14": 188, "15": 196, "16": 210, "17": 222, "18": 232, "19": 243, "20": 254, "21": 267, "22": 278, "23": 289, "24": 304, "25": 316, "26": 328, "27": 342, "28": 360, "29": 374, "30": 383, "31": 396, "32": 409, "33": 432, "34": 445, "35": 457, "36": 473, "37": 482, "38": 500, "39": 507, "40": 518, "41": 530, "42": 544, "43": 553, "44": 576, "45": 584, "46": 595, "47": 614, "48": 626, "49": 654, "50": 666, "51": 675, "52": 692, "53": 706, "54": 721, "55": 746, "56": 768, "57": 777, "58": 793, "59": 811, "60": 820, "61": 833, "62": 844, "63": 853, "64": 865, "65": 877, "66": 890, "67": 903, "68": 922, "69": 934, "70": 945, "71": 958, "72": 976, "73": 988, "74": 1005, "75": 1017, "76": 1032, "77": 1055, "78": 1067, "79": 1084, "80": 1102, "81": 1116, "82": 1137, "83": 1150, "84": 1161, "85": 1171, "86": 1181, "87": 1198, "88": 1212, "89": 1222, "90": 1231, "91": 1242, "92": 1256, "93": 1266, "94": 1279, "95": 1292, "96": 1306, "97": 1321, "98": 1337, "99": 1350, "100": 1360, "101": 1380, "102": 1393, "103": 1403, "104": 1424, "105": 1436, "106": 1446, "107": 1462, "108": 1472, "109": 1483, "110": 1496, "111": 1509, "112": 1520, "113": 1529, "114": 1540, "115": 1554, "116": 1566, "117": 1576, "118": 1594, "119": 1608, "120": 1619, "121": 1632, "122": 1640, "123": 1653, "124": 1665, "125": 1683, "126": 1696, "127": 1706, "128": 1726, "129": 1742, "130": 1750, "131": 1760, "132": 1774, "133": 1783, "134": 1801, "135": 1813, "136": 1823, "137": 1835, "138": 1843, "139": 1850, "140": 1864, "141": 1878, "142": 1895, "143": 1908, "144": 1918, "145": 1929, "146": 1944, "147": 1956, "148": 1972, "149": 1987, "150": 2004, "151": 2018, "152": 2030, "153": 2043, "154": 2059, "155": 2069, "156": 2079, "157": 2092, "158": 2105, "159": 2115, "160": 2131, "161": 2146, "162": 2155, "163": 2161, "164": 2183, "165": 2198, "166": 2212, "167": 2224, "168": 2242, "169": 2255, "170": 2268, "171": 2276, "172": 2288, "173": 2305, "174": 2318, "175": 2330, "176": 2343, "177": 2356, "178": 2366, "179": 2379, "180": 2393, "181": 2408, "182": 2423, "183": 2434, "184": 2446, "185": 2462, "186": 2470, "187": 2488, "188": 2499, "189": 2511, "190": 2524, "191": 2540, "192": 2552, "193": 2560, "194": 2572, "195": 2583, "196": 2599, "197": 2610, "198": 2620, "199": 2630, "200": 2647, "201": 2657, "202": 2668, "203": 2678, "204": 2688, "205": 2701, "206": 2713, "207": 2725, "208": 2736, "209": 2748, "210": 2758, "211": 2773, "212": 2787, "213": 2798, "214": 2810, "215": 2826, "216": 2834, "217": 2848, "218": 2859, "219": 2865, "220": 2876, "221": 2884, "222": 2899, "223": 2910, "224": 2923, "225": 2937, "226": 2947, "227": 2959, "228": 2969, "229": 2980, "230": 2989, "231": 2999, "232": 3010, "233": 3023, "234": 3043, "235": 3063, "236": 3085, "237": 3103, "238": 3112, "239": 3121, "240": 3135, "241": 3145, "242": 3153, "243": 3164, "244": 3181, "245": 3192, "246": 3203, "247": 3240}
---

**Dave Jones:** Hi, yes we're back on the Gigatron PCB and doing some stuff in KiCad because if you saw my previous video which I'll link in if you haven't seen it where I compared the difference between a two layer and a four layer PCB for H or magnetic field radiated emissions and that was a very interesting video.

**Dave Jones:** A lot of people really liked that cuz no one had really taken the exact same design and showed the difference between a two layer and a four layer PCB before.

**Dave Jones:** And a lot of people asked like could I actually do the four layer PCB a bit different? I.E. Well, in this particular case, you'll notice that this is the four layer PCB I did.

**Dave Jones:** It has your traditional ground and power in the middle and the traces on the top and bottom. Can we zoom into that? Unfortunately, I don't think we can show the inner layers inside there.

**Dave Jones:** Anyway, and this is your traditional method because you say for surface mount parts, you want to route your traces on the top and bottom. You don't want to have your surface mount parts and then immediately drop down via vias down to the inner layers and then it just ruins your routing density and all that sort of stuff.

**Dave Jones:** But for through hole board like we've got here, there's no reason that the signal layers had to be on the top and the bottom. So a lot of people said, "Hey, what's the difference if we actually bury those layers those signal layers in the middle all these traces in here with all the loop area that's radiating everything.

**Dave Jones:** What if we buried them inside the copper plane? So have the ground and the power on the outside and the two signal layers on the inside. So hey, it's an interest it'll be an interesting experiment.

**Dave Jones:** So I'm going to do that now. So what I'm going to do is I've I created a duplicate version. I'm still running 5.00. I know there's a later version but I just want to use the same one I've already got installed.

**Dave Jones:** So, let's actually load this up. All right, so let's drag it over. And by the way, thank you to people on the uh KiCad uh forum because this is actually tricky.

**Dave Jones:** I couldn't figure out how to do this, and I'll explain in depth uh shortly. And a few and somebody I think basically had the right approach. Thank you EE Lick.

**Dave Jones:** Um here a lot of people said I can I'll show you in a minute that other techniques to do what I want to do to actually swap all these layers cuz I don't want to re-lay out the board.

**Dave Jones:** I want to keep everything absolutely identical. So, so let's actually load it up. So, I've created a duplicate board here. Okay, so we've got where if we take off the layers here, okay, we've got our top and bottom layers here and then our inner copper VCC and ground like this, okay?

**Dave Jones:** So, now what we want to do is swap these layers. And as it turns out like there is a layer swap tool. If you actually go in here and there's a move and swap layers.

**Dave Jones:** And you can actually go there and you can kind of sort of do it, but I found it didn't actually work. It didn't do exactly what I wanted. So, what I want to actually do this is trivial to do in Altium.

**Dave Jones:** I I used to do it all the time in Altium. And as it turns out it works the similar way here. It's just that I couldn't actually uh find it.

**Dave Jones:** So, I want to move all of these top layer traces here to the inner layer which is currently called VCC like that and I want to move the bottom layer ones to the inner layer here which is ground.

**Dave Jones:** So, if we go to our uh stack up here, we've got a four-layer board. Now, you can actually do this many different ways. You can create extra layers and then copy them the extra layers, but I don't think we have to actually do that.

**Dave Jones:** So, what I'm going to do is I'm first I'm going to change VCC uh and ground from power planes to signal planes cuz effectively we're doing polygon pours anyway.

**Dave Jones:** So, it makes, you know, it polygon or zones as they're called here, copper zones. So, it makes no difference. So, let's actually change those over to signal layers, okay?

**Dave Jones:** First of all, we'll just delete our plane here. I could probably drag it off or move or swap the layers and stuff like that. I I just don't want to.

**Dave Jones:** I will will just do it from scratch, shall we? Cuz if we go in here and then we select this layer here. Uh I don't think Yeah, I don't think we can actually swap the layer of that zone.

**Dave Jones:** So, we're going to have to place a new zone. Um maybe there is a way to do it or whatever, I don't know. But anyway, we'll delete our copper zones and you'll see all of our nets are now unconnected.

**Dave Jones:** All of our uh positive, uh which is called H. That's just the designers on the schematic chose the name H for high and L for low. They're actually VCC and ground, okay?

**Dave Jones:** So, all these nets are unconnected. That's what all these nets here mean. Now, if we go back into our top layer or FCU, [ __ ] you. Um sure, that's a running joke in the KiCad forum, isn't it?

**Dave Jones:** Anyway, what what we can do now is simply I'm still getting used to the got a hole down the middle thing. Anyway, let's select all of our items in here, but unfortunately it selects all the components.

**Dave Jones:** But, we can go in there and we can select and we can filter our selection. And by default, it's got everything. So, we don't want footprints, we do want tracks, we don't want vias cuz we can just leave them there.

**Dave Jones:** We're actually just swapping everything over and hopefully it because the vias need to go to a certain net. Hopefully, it won't screw up the nets and everything else. So, we want to turn everything off and all we get selected is our tracks, like that.

**Dave Jones:** Fantastic. Okay, so we've got just our traces now in there. So, we can actually go in and let's right-click and let's go into properties like this. And then, for the traces, unlike the zones, it gives you the ability to simply to change the layer that you're on.

**Dave Jones:** Now, I've tried to actually copy and paste to another layer. That doesn't seem to work. So, don't do that. Altium has an option when you paste, it's like paste on this layer.

**Dave Jones:** So, you can take something from another layer, highlight it, copy it, and then paste it to the current layer. It looks like that KiCad does not have that option.

**Dave Jones:** Anyway, we can simply just transfer the traces right over. Bingo, they're gone. And the vias, as you can see, are still all the same nets and everything like that because we're not changing anything else.

**Dave Jones:** And if we go into copper, uh sorry, if we go into VCC layer, bingo, our traces are now transferred into there. And we can go and do an identical thing to the bottom layer.

**Dave Jones:** It's too easy. We just highlight like that. And filter selection. And traces, that's it. Boom. Properties. Boom. Ground. Done. And bingo, we now have the VCC and ground layers, which we'll have to rename, of course, because they're no longer that.

**Dave Jones:** We can just go into Let's just call it inner top and inner bottom, like that. And we'll leave it FCU and PCU. It doesn't matter. And we don't have to change that back to power plane.

**Dave Jones:** Uh there's no uh reason for us to do that um because it's going to give us the positive I don't think it inverts it on the Gerbers. Anyway, we still have all these traces.

**Dave Jones:** So, now we have to go in and we have to to our copper. So, let's go to the uh bottom first. We'll pour our bottom copper. And we'll place a copper zone like this.

**Dave Jones:** And we don't want to go too near the edge. That's annoying. The board is actually off the grid, so I can't like put it in exact distance away. That's kind of annoying, isn't it?

**Dave Jones:** It's like half a grid. Maybe if if I change the grid size. 25 mils. There you go. Change the grid size. So, we're good to go. Let's uh we can scroll down to um what low L, or we can apply a filter and then we can just find it like that.

**Dave Jones:** That's probably easier. We're just going to leave it cuz I believe I used all the defaults last time, the thermal reliefs and everything. So, it's going to connect to the low.

**Dave Jones:** You see that low is unconnected at the moment with all those rats nest nets. So, let's go all the way with LBJ over here. I'm going to do something special on this board in a minute.

**Dave Jones:** I'm thinking about taking the copper all the way to the edge. But, I won't just for cleanliness. Just for, you know, good practice. I won't take it all the way with LBJ right to the edge.

**Dave Jones:** There you go. And I can actually complete that, I believe. Can you I think you can right click and close zone outline? Boom. Okay, we're in. Now, it's exactly the same as before.

**Dave Jones:** Yes, the copper before did not go through the pads. It's just the uh that was those clearances I chose in there. I'm going to leave that exactly the same.

**Dave Jones:** So, I did This is not technically best case because if you were like loop areas would be flowing around like this, you know, if you if you had a trace connected in here and the current and the return path had to get from this bit of copper over to here, then it would have to go right around here instead of going through the individual pin.

**Dave Jones:** So, this ground plane is not as good as it could be, but you saw the dramatic difference in the previous video of the radiated emissions between the two layer and the four layer.

**Dave Jones:** So, I'm going to leave it exactly the same. Now, the top layer we can do the same. Now, I said that I wanted to do something special on the top layer and I'll explain in a minute.

**Dave Jones:** I'm going to actually take this back a significant margin here. Let's just say center of that. H apply filter. Still not used to using KiCad, but it really doesn't take much um doesn't take much doing to learn it.

**Dave Jones:** It's pretty good. So, is that the yeah. Yeah, I'll just take it in the center of those pads just because and I'll explain what I'm going to do in a minute.

**Dave Jones:** I have a devious plan. Why didn't we get Why didn't we get it connected? Oops. Uh once again, I placed I didn't have it selected. That's really annoying. I didn't have the layer selected even though it's disconnect like How can you work on a non-displayed layer?

**Dave Jones:** I reckon that's wrong. Oh, I did Anyway, I'm selecting it with the blue thing here. Maybe if I was in single layer display mode would have been anyway, whatever.

**Dave Jones:** Okay, let's do that again. I like how it centers when you like center you move your mouse pointer and then when you zoom in with the inner mouse wheel it centers on that.

**Dave Jones:** That's really quite nice. Close zone outline. Bingo. There we go. So, now you'll notice that all the rats nests are gone because our Yeah, there it is H has been connected and if you go through to the bottom layer, you'll see that all the L's are being H?

**Dave Jones:** What? Did I screw the pooch? Have they both got a H? Uh yeah, I've created that. Don't send that out for manufacture. Your ground planes are short. What have I done?

**Dave Jones:** Probably screaming at me. I don't like that you can't click in the middle of that layer. I find that really annoying. Copper. Bottom copper is L. Yeah, I think I I completely screwed that.

**Dave Jones:** There we go. Top is now connected to Just testing you. Making sure you notice. Okay, so our top layer but then you'll notice that our top layer is pulled back from the edge like this cuz the What I want to do is also not only do I want to see if there's a difference between having the grounds on the outside and ground and power on the outside versus the inner layers and

**Dave Jones:** there will be. It's just a matter of how much really. Uh in terms of field emissions, far field emissions once again. And when I have these three boards different types, the two layer one, the four layer with the grounds and power in the middle, the four layer with ground and power on the outside, this will give me some fantastic references to do some far field measurements perhaps in an outside

**Dave Jones:** an open area outdoor test site even in my own lab or at a fully at a full compliance EMC test house. That'd be really cool if I can swing that.

**Dave Jones:** Anyway, Uh so the H Oh, we've got a got a net over here. Hello. Hello. Why aren't you connected? What's What's wrong with you? You're connected. Look at that.

**Dave Jones:** There's a What's going on? Got two perfectly good um thermal reliefs going in there. There's nothing wrong with that at all. That's bull dust. Anyway, top silk, I change that DaveCad four layer outer.

**Dave Jones:** Have you got an inner or an outer? Four layer outer. There you go. What I want to do is actually see if it makes any difference if you put copper tape around the outer edges.

**Dave Jones:** Now, of course, you wouldn't do this in production, of course, but a lot of boards like specially RF ones and things like that might have the edges actually gold plated as well and they're connected to the ground plane.

**Dave Jones:** Sort of like to uh form like a shielded box around everything. So, all your signal layers are enclosed inside, so it can't like radiate out the sides and stuff like that.

**Dave Jones:** So, what I want to do is add some extra copper on this top layer here, but it's got to be connected to ground. I can't have the power there.

**Dave Jones:** So, I'll add in some extra uh copper fills in here. Some extra zones. Non-copper zone properties. No. Ah, cuz I've right. There you go. Cuz I've got the bloody silk selected.

**Dave Jones:** There we go. All right, still getting used to this. Here we go. Right, so I want it connected to L, which is my ground. Okay, yeah, happy. Can I create a polygon that No.

**Dave Jones:** No, I'll I'll just create four by four overlapping polygons. Thank you very much. Oh, no, I I could do it as two overlapping polygons. Look. Here we go. Look, I'll be I'll be fancy pantsy.

**Dave Jones:** Look. All right, I'll go over to here. Here. Here like this. We'll pull it back. Okay, so I don't want it to be touching the other ground. Uh the other the positive one there.

**Dave Jones:** And we'll go like this. And we'll go up here. And we can close zone outline. And that, unfortunately, because there's nothing to connect to, if the zone is there, but it hasn't um created like it hasn't connected through to copper.

**Dave Jones:** So, what we'll do, copy a via Oh, hello. That's a What's wrong with that trace? That trace sucks. Look at that. That's terrible, Muriel. I I I could place a via, but I want it to be exactly the same.

**Dave Jones:** Like, and I don't know what the current settings and all that sort of stuff are. Paste, and then I'll change it. There shall we? Through net L Boom. Like that.

**Dave Jones:** And if we repour How do we repour our copper? Can we just hit okay? Will that Yep, there we go. So, it's now it's decided to lay that copper down there cuz we've got the one via.

**Dave Jones:** So, I'll I'm going to put a bunch of vias around here. It's Oh, yeah, look, it's split it down here. There you go. So, I'll also put the extra one around the outside, and that'll be connected to ground, and then we have to expose the solder mask as well, top and bottom so that we can see this.

**Dave Jones:** I'll spare you the details. I'll go to the finished product. Well, that's annoying. I just copied this uh via here, and it did not automatically copy the net as well.

**Dave Jones:** So, there you go. That's a thing. But, I find that if I now paste another via in there should connect. No, it doesn't. Doesn't automatically connect. Is there an option That is really annoying.

**Dave Jones:** Wow. Use net class net design Yeah, that's that's really annoying. Maybe there is a way. I'm not going to say there's not, but that means I can't bulk copy.

**Dave Jones:** I can't just paste them and have it I got to go in and manually change it. Really? That's annoying. I'm sure all the KiCad experts will tell me, "No, no, there's a way to do that."

**Dave Jones:** No, there probably is, but if there's not there damn well should be. So, I don't care if these are exactly Heh. If I was laying out a board for real, I would uh make sure that these are all evenly spaced or whatnot, but you'll see this all the time where where just by placing the multiple vias here, we're just lowering the inductance of uh around the out outer edge.

**Dave Jones:** And some people go insane. They actually stitch like vias all the way around and create like a Faraday cage. They don't want anything seeping out. But because we're going to put the copper tape, um it it doesn't It literally doesn't matter.

**Dave Jones:** So, Oh, actually, I've run into a problem. I tried to go into the uh 3D viewer, and it really does not like this. Unable to find the next graphic segment endpoint edit graphics making the continuous polygons each cannot determine the board outline.

**Dave Jones:** Anyway, see, we've got solder mask over our What the hell? What What the hell has happened to all our pads? Uh that's um silkscreen. What looks funky. Something has gone horribly wrong with this 3D viewer.

**Dave Jones:** Wow. That looks funky. Kind of like that font. Maybe we should trademark that font. That looks pretty groovy. Heavy metal or something. Call it the heavy copper font. I'll get back to you.

**Dave Jones:** I have no idea why this 3D view has done this. Wow. Let's go down to We can do this by going down to our front mask here, and then once again, uh placing a zone, or do we have to do a keep out area?

**Dave Jones:** I'm not sure. Oh, and our Our 3D viewer's back. Okay. Look, our three Our pads are fine now. It's come good. It doesn't like the board size. For some reason, the board size has been screwed.

**Dave Jones:** Once again, like this is like the first time I'm using KiCad, so please bear with me. Oh, I think a zone was the wrong thing to do. You don't want to do a zone.

**Dave Jones:** That's uh I'm going to kill that zone. I think we need to place Jeez, that that's taking a while. Not Not Not responding. I saved it, didn't I? Oh, there we go.

**Dave Jones:** Okay. Place. No, what we want we want to place a polygon. Sorry. I screwed the pooch. Front mask. Okay, here we go. Now we can Now we can do this.

**Dave Jones:** Watch this. Watch this. I'm going to this one and then way up. Boom and end. Oh, well we can't There. Like that. There we go. Once again, it's taking a while.

**Dave Jones:** I think we've got an error there. I've introduced some sort of issue. Let's go into 3D viewer again. Bingo. Our solder mask has been removed. So now, we've got this copper exposed copper all around.

**Dave Jones:** I've got to do the same on the other edges plus on the bottom as well. And then I'll have these exposed um if I get a gold plated, probably yeah.

**Dave Jones:** Probably will. Um then they'll have the nice gold plated things and I'll be able to actually put some copper tape over around the outside if I want to do that thing where I seal it up.

**Dave Jones:** It's just It's just a maybe. It's you know, once again, I wouldn't bother fixing that pad either. Like I just you know This is just a board for experimentation purposes.

**Dave Jones:** I'm not going to dick around much. Aha! Is that our furphy down there? Ah, okay. I think that's been moved. There you go. That's what was causing that issue there, I think.

**Dave Jones:** There you go. So I fixed the edge cuts, which is the board outline, and you can see that our solder mask There's no solder mask on the corners or anything like that.

**Dave Jones:** So, we've got exposed grounded copper all around the edge like that. That's just so that maybe if I want to, I can do an experiment. But, once again, I still haven't done the bottom side there.

**Dave Jones:** I'll finish that now. There you go. That's the bottom layer. And for those curious, uh yes, you can actually take uh mask uh solder mask directly to the edge.

**Dave Jones:** Um unlike copper, which creates copper burs and stuff like that, especially um when you're uh removing solder mask like this one. So, if we go up in in our 3D viewer, you can see that now will be complete.

**Dave Jones:** There's no problems taking that directly to the edge. That's top and bottom. Oh, we got our stupid pads again. Got our stupid pads. Anyway, we've got our copper I don't I have no idea what the hell's going on there.

**Dave Jones:** Wow. Just wow. It's just rendering all those pads wrong. All right. Because some people are going to ask, "How do you get your board to have these gold-plated edges like this?"

**Dave Jones:** Well, this is called edge plating. It might be called, you know, something different at some other fab. But, um any fab should know what edge plating means. So, what you want to If you wanted to do that, then obviously, here's your like Here's the side of the board here.

**Dave Jones:** You don't We can see that in uh Let's turn off our contrast mode. There you go. So, we've got Let's just turn on our edge cuts and our top layer.

**Dave Jones:** So, what you'd want to do is actually take your copper right to the edge like this. And then, somewhere on your fabrication drawing down here, for example, you might uh This one doesn't have any fabrication uh notes, but sometimes you would have like a fabrication layer.

**Dave Jones:** Yeah, I don't think we have any don't think we have any drawings use that now. But often you'll put all of your fabrication notes on your board like this and you'll have all your specifications.

**Dave Jones:** I want FR4, I want Rogers PCB material and put the the particular part number you want and I want this tolerance you know, I want 4 thou 4 thou tolerance.

**Dave Jones:** I want gold plated you know, immersion gold for example and I want edge plating please. You will specify that either on your drawings or you can just simply do it in the email to them or it might even be an option on an online PCB manufacturing tool when you upload your Gerber's for example there might be an option for edge plating.

**Dave Jones:** I don't know. So but generally I've just done it manually in the past. Just tell them I want edge plating and they will do that as a separate process for you and if you don't take the copper to the edge maybe they might do it for you.

**Dave Jones:** They might expand the copper out until right to the end. So do whatever they have to to give you that edge plating and you know, usually you want it connected to the ground.

**Dave Jones:** Usually almost always is ground and then connect top and bottom like that. You can get just the edge plating without it being connected to everything anything. It can just be floating there but really apart from looks there's no other real there's no electrical reason to do that.

**Dave Jones:** But in this particular case I don't want to do that because I want the option to be able to measure this with no edge plating cuz that's like a standard board would be would to have no edge plating on it.

**Dave Jones:** So that's why I've peeled it back from the edge like that. Okay, so we're actually good to go now. Let's go into our 3D viewer. That's what our board is going to look like.

**Dave Jones:** We got no I I don't think there's any way to show edge plating in the 3D view. So yeah, it's just like you just have to specify that manually but that's look that's all right.

**Dave Jones:** And we've got our exposed copper around the edges, which is ground, top and bottom, good. So, I have the option. So, that looks that looks all good to go.

**Dave Jones:** That's looking pretty groovy, isn't it? I like that. So, yeah, I don't know where the bug is where that causes all the the funky copper font and everything else, but anyway, so we're good to go.

**Dave Jones:** So, now really we want to do our ERC thing. I'm still don't know what's causing this. Like, why is that still showing that as a net? I don't know.

**Dave Jones:** Anyway, so now we want to do our DRC before we do our Gerbers, because you want to make sure that you haven't screwed the pooch. So, design rules checker, we want that in there.

**Dave Jones:** Let's list Um uh once again, you can put in your tolerances and stuff like that here. There's options to like refill all your zones before performing DRC. Unless you've got a special circumstance, I wouldn't recommend doing that, cuz you can screw the pooch.

**Dave Jones:** Um because there's steps here. You go in we've done our layout board, we've verified it in 3D mode. 3D mode is brilliant for it's what you see is what you get.

**Dave Jones:** So, you use that as an inspection tool. We've done that. You lock everything down. Then we'll do our final You can do that after your DRC, but we'll just in this particular case, we'll do our DRC.

**Dave Jones:** We might find one or two little errors, we'll fix it. We'll do the 3D view again and lock it all down, and then we're good to go. So, you wouldn't want to refill all the zones and do the DRC and then just generate the Gerbers, cuz refilling the zones you might have changed your clearances, your tolerances, you know, and all that sort of stuff in your zone.

**Dave Jones:** You may not get like copper through here, for example. You wanted copper through there, but you accidentally didn't realize that you changed the clearances in there the for the copper zones and stuff like that for the copper pours.

**Dave Jones:** So, you could find that it was working before when you last viewed it, but now all your copper's broken in here and stuff like that. So, really, you know, just be careful when you're refilling zones.

**Dave Jones:** Report all errors for tracks. Check footprint uh courtyard overlap. Uh where that's like if you the footprints, you can specify a courtyard of components whether any any components are overlapping.

**Dave Jones:** If you got a chip here and a chip here and they're overlapping like that, then it'll flag that as an error. It's a it's a mechanical DRC error essentially.

**Dave Jones:** But if you don't haven't generated courtyards for your it'll be called different things in different tools. In KiCad it's called a courtyard. Uh if you haven't specified a courtyard for your component, then you won't have that feature.

**Dave Jones:** Anyway, we can like just go list unconnected. Here we go. We've got a two unconnected items. Pad one on [ __ ] you. And yeah, look, there it is.

**Dave Jones:** Yeah. Like why is that unconnected? Why the If we generate that Gerber, th- this this copper will be here. Our board will come back. It'll be fine. So, there's something something that's wrong with um we can just go edit.

**Dave Jones:** Can we just edit the properties of that? I I don't know why these pads are weird like that. I mean, the when we've poured that copper zone, we've poured that copper and the software knows that it connected to this pad.

**Dave Jones:** Otherwise, it would just leave the gap right around like that. So, it knows to put in those thermal reliefs. It knows to connect it. It knows to connect it up here cuz it's putting these thermal reliefs.

**Dave Jones:** So, why that is showing up as an error? I Th- There's got to be something subtle in there or it's some sort of bug. So, I don't know. So, it's not uncommon unless you're following very strict procedures where you have to have zero errors.

**Dave Jones:** Like you you know, you're at the design review meeting before your board gets manufactured. If you've got a ridiculously complex board, like one of these things, you know, if you've got Right, if you've got something like this, you've you've designed this board here, for example, right?

**Dave Jones:** You've designed this board or it's some other huge PC motherboard or something. It's taken you a month to lay out this board, which is not uncommon, by the way.

**Dave Jones:** I've had boards that have taken me a month or two to lay out, right? They're absolutely like, you know, and this one's not enormously complex, but this is a pretty advanced board.

**Dave Jones:** This is going to be like an eight or 10 layer job or something with all these huge thousand pin count BGAs, right? There's a lot of work that goes into that and it's probably an expensive board to get that manufactured, especially when you got to solder the chips on and everything else, right?

**Dave Jones:** You don't want to goof this up, right? So, there's probably going to be a design review meeting. Foo. There's going to be a design review meeting for this board.

**Dave Jones:** So, they're going to say, "Well, show us your DRC report, for example." And there's ways to fudge, of course, you can fudge your DRC report, but if you've got something someone cluey in the uh design review meeting who goes, "Well, show us the constraints that you used for your DRC."

**Dave Jones:** That's what I'd be asking for. "Show us your constraints to see if you're fudging uh the DRCs cuz anyone can make You can have a board riddled with errors and get your DRC errors down to zero.

**Dave Jones:** So, they can produce your report and go, "Here it is, there's no errors." But, it's riddled with problems. So, it's all about the constraints that you set up when you do your uh design rule checking and your ERC.

**Dave Jones:** Uh your electrical rules checking. ERC is for schematics electrical rule checking and then DRC is for design rule checking, which is for PCBs. And in this particular case, we could ignore that.

**Dave Jones:** I'm absolutely confident and we can check out verify our Gerbers that this would be fine. So, I could go, "Look, I just want to send this board out to one-off.

**Dave Jones:** Doesn't matter." I could just ignore that. So, um I don't know. It's probably easy, but I I don't know why it's doing that. Aha! I found it. Look at this.

**Dave Jones:** I'm on the bottom copper layer at the moment, and look, L and H nets are shorted together. Um yeah, L and H. So, why it's only giving me that one error?

**Dave Jones:** Maybe it's suppressed all the rest. So, oops, did I forget to repour a poly, did I? Let's repour poly. Put the kettle on. Nope. Look at that. That's interesting.

**Dave Jones:** The only thing that we're going to The only net we're going to connect to is L. We repour that, and it goes over the H net. WHAT THE OH!

**Dave Jones:** I've poured multiple ones. I've done multiples. Look. It's got a H. Yep, that's when I I goofed it up before. Oops. Sorry. Get rid of that. Move that one back.

**Dave Jones:** There we go. Is that it? I have to redraw that. You think it'll redraw after moving, wouldn't you? Okay, now we're good. And then I've got to go back to the top.

**Dave Jones:** H and now H. And if we run the DRC again, I think we'll find we're good. So, there you go. That's interesting that it didn't like it didn't flag like hundreds and hundreds.

**Dave Jones:** There should have been hundreds of you know, dozen at least dozens of shorted connections there. Oh, it's Well, why it listed them as unconnected? That's the other thing. So, let's just anyway, let's just run that design rule check.

**Dave Jones:** List unconnected. It still thinks that they're unconnected. What what what? Have I done the same thing on the top? Nope, there's no other hidden uh polygon under there. So, no.

**Dave Jones:** So, that's interesting why it actually like that was a massive error. I had those ground plane shorted together. And if we got that board manufactured, if I ignored that, oh, there's only one unconnected pad, but I hadn't done the DRC yet.

**Dave Jones:** But like once again, let's go up here. Design rule check. We'll start the DRC. Okay? Boom. That's it. So, maybe it would have given hundreds of errors before or something.

**Dave Jones:** I should have checked that. Track near via. Oh, look, there's our little red arrow. What's What's wrong with that? There's nothing wrong with that. Aha, I was wrong. It is only reporting the first error cuz I didn't have this tech checkbox ticked.

**Dave Jones:** Uh here we go. Report all errors. Uh this can be slow. If unselected, only the first DRC violation will be displayed. So, yep. There we go. So, start DRC again.

**Dave Jones:** And two two track ends too close. Track near via. Okay. So, now there you go. Trap for young players. Young KiCad players. So, these are all my DRCs with this board.

**Dave Jones:** So, track ends too close. Track near via, we know about. Okay. What's track ends too close? Why are the track ends I They're not tracks. There are no tracks there.

**Dave Jones:** So, here's how where we have to go into the detail. Net bus 7 16 on layer inner top. Oh. Oops. Doll. Yep. Inner top. Here we go. Silly me.

**Dave Jones:** Have I Yep. Yep. There you go. There you go. I placed those vias without any thought for the tracks on the inner layers. Oh, that was dumb, wasn't it?

**Dave Jones:** And I didn't have like any like online DRC to to tell me that I was being uh that I was being naughty. Here you go. So, that is that is correct.

**Dave Jones:** All right. No worries. Why do they have like six markers or whatever? Anyway, yeah, have I screwed the I thought that I was away thought I was nowhere near them, but yeah, there's a couple down there.

**Dave Jones:** So, let's run that design rule checker again. Bingo. None. We're done. That's it. They were all our DRC errors. So, we've got yep, all tracks. So, we're searching all tracks.

**Dave Jones:** We're using minimum track They're the specs. So, minimum track width 0.2, minimum via size 0.4, minimum micro via size We don't have any micro vias. Uh so, we're good.

**Dave Jones:** List unconnected. The only issue we still have non-copper of C6. I I still don't get it. Is that it? That It's got to be that. And you want to make use of the high contrast mode here.

**Dave Jones:** You can just go H, which is quite nice, and then flick through the layers, but like why how that's a thing That's nuts. Could the you know, like there's nothing extra like sometimes you might have something extra hidden under there, but there's not.

**Dave Jones:** Like if you click here So, if we go here, for example, like you you needs to clarify the selection cuz it knows there's a both a pad there and a track there.

**Dave Jones:** It asks you what one. So, if we, you know, go over here like this, it it just knows that's a pad. There's nothing else hidden under there. All right.

**Dave Jones:** So, I think we're done. All of our traces, our inner layers, our top That's our top copper. We've got the ground around the outside. It's exposed. We've got the and then the VCC plane, and we've got the inner uh top layer uh We'll call that layer two, and layer three, which is the inner bottom.

**Dave Jones:** They're all our traces, and uh B, bottom copper. Um, that's our ground plane. So, I think we're good to go. I mean, we can, you know, turn on the silk and have a look at stuff like that.

**Dave Jones:** If you're really that keen. Front silk, there you go. And I'm not going to fuss about any more details. Solder mask. Solder mask, I think we're good. I think we're good to go.

**Dave Jones:** We're going to generate our Gerbers now. So, I'm just going to ignore that error. Seriously, I I just pretty confident that's not going to be a problem. I could come and get you.

**Dave Jones:** Also, we could actually run the cleanup. Delete track segments conflicting with different nets, delete redundant vias, merge overlapping segments, delete dangling tracks. Don't want any dangling tracks. We can do that, but I don't think we had anything because our DRC didn't like unconnected nets.

**Dave Jones:** There was only that one up there. Is that gone now? Let's say, out of curiosity. Curiosity. What, and which, how, or why? For you Aussies, you'll know what I'm talking about.

**Dave Jones:** List unconnected. Nah, still there. Anyway, there's our 3D view. So, you want to go through your 3D view, like go in, check it all out, you know, like the simple stuff like silk screen over pads and things like that.

**Dave Jones:** And the great thing about this is that it is rendered in what you see is what you get. But, sometimes you might not want silk screen over your vias or something.

**Dave Jones:** If it's a nice important silk screen, you know, you might go in and shuffle your tracks on a pro board, uh, for example, if you're really, you know, caring about that sort of stuff, but uh, generally, I think we're good.

**Dave Jones:** I think we're good to go. The blinking lights. So, we're going to want a drill file. Postscript, excellent. Drill units. You want millimeters, decimal format. Generate generate drill files.

**Dave Jones:** Yep. Now it's our plated through holes, non-plated through holes. Uh separate them and the manufacturers can deal with that. No problem. We want to plot our Gerbers. Output directory, Gerbers.

**Dave Jones:** We want the front copper, the bottom copper. We want the top silk screen, the bottom silk screen we don't need. There's no silk screen on the bottom. Uh the front solder mask, the bottom solder mask, the edge cuts.

**Dave Jones:** We don't have any more. We don't have like fabrication drawing info or anything like that. So, let's not worry about that. Uh coordinate format, that's fine. Use Protel file name extensions, no.

**Dave Jones:** Uh check zone fills before plotting. Exclude pads from silk screens. Exclude piece of inches. Force plotting. Do not tent vias. Uh yeah, we don't want to tent them. Tenting, of course, means to put the solder mask over the vias.

**Dave Jones:** You can get to do that at the You can even do it at the via stage. You can edit I think you can edit your via. Can you do that in KiCad?

**Dave Jones:** No. There you go. You can't tent. Really? You can't tent an individual via. Wow, that's a bit of a limitation cuz sometimes you might want to tent individual ones and not board wide.

**Dave Jones:** Is that a thing in KiCad, really? Wow, that's that's pretty limiting. Many, many times I've wanted I've done boards where I've had to uh tent some vias and not others.

**Dave Jones:** That's a massive limitation if that's legit. Anyway, plot sheet references on all layers. Plot footprint values. I think we're good. Plot. I It's good that we can run a DRC and we can generate the drill files from here.

**Dave Jones:** Generate our Gerbers. Because um some manufacturers will accept KiCad files, but no, you want the Gerbers. And I will find the next boundary. Bite me. Okay, where are our files?

**Dave Jones:** It's not in the Gerbers cuz they're the old ones. Because it's not four-layer outer is the name OF MY PROJECT. OH, I think it's not generating the Gerbers because of this error.

**Dave Jones:** Cannot determine the board outline. Wow, I don't think it'll even generate them. There's no files in there. It doesn't even generate any Gerbers at all, any layer with that bug.

**Dave Jones:** So, I've got to fix that. Damn. It's a bit limiting. I'll get back to you. Maybe I can disable the check zone fills before plotting, perhaps. Let's give that a whirl.

**Dave Jones:** There we go. Yep. Yep. All right, so I just ignored the zone fills and we're good. Do I have to like is there a like a refresh and a refresh?

**Dave Jones:** Refresh project tree. There you go. Tada! There you go. That's our front copper Gerber. That looks good. No wackers. There's no daggies outside that Oh, it's still got the it generated the frame in there.

**Dave Jones:** It doesn't matter like the manufacturer will get rid of that. It's not a problem. Like the manufacturer will just ignore that. It's not a problem. Uh So, bottom copper.

**Dave Jones:** That looks good. Yep, happy with that. Our mask Uh it won't open up in the same window. Yep, that looks good. And the edge cuts will just be as the name suggests, around the outside.

**Dave Jones:** Front mask. Front mask looks good. No wackers. And last but not least, the front silkscreen. And always check your Gerbers. To Oh, no, I was going to do the T-shirt.

**Dave Jones:** Don't don't touch my Gerbers. Cuz some manufacturers will. I've done a video on that. I might try and link it in how a manufacturer modified my Gerber's to expand the copper around the pads.

**Dave Jones:** It was It was just ridiculous. And then I had breakouts and my ground plane was broken. It was just It's just insane. The manufacturer should not touch your Gerber's without your express written permission.

**Dave Jones:** It's ridiculous. Anyway, so those Gerber's look good. So we're good to go. So we'll package up those Gerber's and the drill files in a zip file and we'll get this board made.

**Dave Jones:** Now of course if this was a professional PCB and a lot of money like as I said like one of these boards here or something like that there'd be a lot more involved in checking this than just a cursory glance.

**Dave Jones:** Yeah, you know, she'll be right. No worries, mate. In this sort of board like a four-layer board like this is pretty simple. As long as you don't screw up your ground planes and all that sort of stuff and it passes DRC and everything's fine.

**Dave Jones:** You don't care too much about all the not fussing over the little details. You just want something to work um electrically then uh yeah, no worries. But sometimes you can you can take a day or two just just to check everything, double check, triple check everything before you send it out for manufacture.

**Dave Jones:** Cuz like I said like if you're populating a huge board like that, right? You get your board manufactured and then yeah, it might be 100% electrical tested at the factory which it would be, right?

**Dave Jones:** Everyone does that nowadays. Used to cost you extra. Now it doesn't. But if you got a board like that electrically tested so oh yeah, it passes electrical test. It must be okay.

**Dave Jones:** You go put some of those FPGAs are thousands of dollars each, right? Getting one board I've had boards that cost like tens of thousands of dollars just in parts on the boards.

**Dave Jones:** So it like and if you and if there's something wrong with that board and you put all the load all the things on and you find that I don't know your ground planes are short or one ground plane's not connected because of something or other that like it could be a real expensive mistake.

**Dave Jones:** Now, I'm in JLCPCB here at the moment. Don't necessarily recommend them, but I don't not. So, you know, it's not an endorsement or anything like that. It's just happened to I use at the moment, so I'll load the Gerbers up.

**Dave Jones:** Okay, we're uploading our zip file now. Good thing is it can like it when I was a boy, not that long ago really, uh these online what you see is what you get things were just not available.

**Dave Jones:** You sent your by email. You didn't even upload it via web. You sent it by email to your PCB manufacturer and they'll, you know, like you wouldn't even get previews back.

**Dave Jones:** You just crossed your fingers and hope you'd done it right. And here it is, detected two-layer board. Oops. We had this problem the other day getting the micro supply PCB.

**Dave Jones:** There's a new one I've shown a video shown a video to my supporters. That's the new micro supply PCB. And we had troubles actually uploading this to JLC. It wouldn't detect the four layers.

**Dave Jones:** It had a problem with the way that Altium did power planes. It would actually invert them, of course, and it then the software couldn't handle that and anyway, I finally got it working.

**Dave Jones:** But like it took like a day of effort. That was of course a test. I was testing everyone to make sure you were paying attention there when I plotted I forgot the inner top and the inner bottom.

**Dave Jones:** No, I didn't. It was a test. It's taking a while generate those. All the Gerber the ones with all the polygons. Unable. Yeah, bugger off. We'll try that again.

**Dave Jones:** See if it likes it. I don't know how it identifies whether or not which order the stack up goes though. So, you might want to watch that if that's important to you.

**Dave Jones:** Detected four-layer board. There we go. Why does it only show it only shows top and bottom? I think that's normal. Okay, but that looks good, right? Shows all the silk.

**Dave Jones:** They're like the the dimensions are right, everything's yep. So, let's go into the Gerber viewer. It's for reference purposes only and may differ. Bottom. Cuz it only does the top and the bottom.

**Dave Jones:** It does not have the inner layers. Oh, we're unselecting. There you go. We're unselecting. Got it. Yep. Right, that makes sense now. Okay, but it's only top and bottom.

**Dave Jones:** Yeah, if we go into analyze analysis results, it tells us that inner bottom and inner top Don't know why it's got null there. Maybe cuz it's it's done nothing with it, I presume.

**Dave Jones:** Generic Gerber file like it's Gerber file with board outline generic. No, the others are just generic Gerber files. So, it's not showing us the four layer. Did it show us before?

**Dave Jones:** No, I've uploaded the old four layer one that I got manufactured and it's once again, it's exactly the same. So, I think it only displays top and bottom. I think the JLCPCB Gerber viewer doesn't let us view the inner layers, which is what a pain.

**Dave Jones:** Like they go to all the effort to do all these Gerber rendering and viewing and everything else, yet can't show us the inner layers by the looks of it.

**Dave Jones:** So, that's it's kind of frustrating. But anyway, let's go through with it. It's detected a four layer board. There's an issue, I'm sure they'll come back to us. All right, stupid bloody screen capture didn't capture my final thing here.

**Dave Jones:** I was just showed you the whole process for 10 minutes, didn't capture it. So, I got to Uh, here we go again. Anyway, here we go. Four layer board.

**Dave Jones:** Uh, we can only get a minimum quantity of five. I can't order one, which is pretty wasteful. If I only want one and it's a one-off, like they're going to make five.

**Dave Jones:** Anyway, it's got to expend all the fuel coming here on the DHL jet and everything else. So, you know, whatever. Anyway, the interesting thing is is that there's no price difference here.

**Dave Jones:** Look look at the insane price. 32 bucks is the tooling fee. When I was a boy, don't even get me started. 19 bucks for five boards. These are large.

**Dave Jones:** This is 160 by 230 mm. Like it's just crazy. Anyway, um you get no price penalty for the other sizes like a point eights the next nearest sort of like standard size which is half the thickness.

**Dave Jones:** There's no price penalty for that and there's no price penalty for any of the ones in between. Look at it even changes the weight. Uh does not support 0.6 mm.

**Dave Jones:** Choose another option. Thank you very much. And and 0.4 but 0.4 is a price difference and two is a price difference again. So anyway, 1.6 so we don't need impedance control and there's no price penalty for red either.

**Dave Jones:** Green or red. It's exactly the same price. Terrific. We might as well go red. Makes the electrons go faster. And there is a difference of course if you get gold plating a hassle which is hot air surface leveling with lead.

**Dave Jones:** This is lead base. I don't know why they I mean some people still want lead I guess. You pay do pay a little bit extra. You pay like an extra six bucks or something for lead free hot air solder.

**Dave Jones:** Uh hot air surface leveling. You can think of it as hot air solder leveling if you want. ENIG which is immersion nickel gold. That's what that stands for. A layer of nickel and then a layer of gold on top.

**Dave Jones:** So that's your traditional gold plated board. You pay Look at this. Do we Oh, look it's an extra It's an extra 30 uh 15 bucks for the surface finish.

**Dave Jones:** Extra fee. It's got to be worth it. It's got to be worth it for the wankery. Come on. You know, gold plating is absolutely worth it. 1 oz you do pay a lot for the 2 oz copper.

**Dave Jones:** You'll pay There you go. There's the price difference. We only want 1 oz copper. 2 oz copper is 70 microns thickness compared to 35 microns thickness for your 1 oz the a copper.

**Dave Jones:** So 2 oz copper is what you want if you're doing real heavy current, you know, switching power supplies and stuff like that. You just double your copper weight, you halve your resistance, really.

**Dave Jones:** And uh it's Yeah, it's good stuff. We don't want any gold fingers. We've got like card edge card edge connectors with the 45 chamfer on the edge. We don't have any of that rubbish.

**Dave Jones:** Uh we don't want a panel uh flying probe. You can only get it fully tested. You can't even specify. No, don't bother testing. Don't waste your time. Castellated holes, no, which is the half cut the half moon holes on the edge of the board.

**Dave Jones:** Uh one different design. Remarks, that's possibly where you could put in the remarks for I want the gold plated edges. I want edge plating on there or something like that because JLC um unlike some of the others that I showed previously in the video further back, this one doesn't have like a check box or whatever to select the edge plating.

**Dave Jones:** So, there you go. We don't want our laser stencil, anything like that. So, we're good to go. I'm going to order that. And I will get those in a week or so, then I'll build them up at my leisure, and then I'll be able to do a follow-up video doing the H local H field measurements here in the lab comparing it with the other board, and then I'll do a separate video,

**Dave Jones:** hopefully, uh with some far field measurements E and H field when they combine, you know, I've done that video where they they combine like that and then um at a certain distance they a certain wavelength distance they actually electric and magnetic fields combine to create your electromagnetic radiation which is what you measure in the far field, and that's what you get measured at a test house when you go for EMC

**Dave Jones:** compliance testing. You're measuring the far field, basically. So, I need like an outdoor area uh test site an oats test site for that or maybe a EMC test house if I can get it or, you know, I could even do it myself here in the lab with a, you know, couple of rabbit ears rabbit ear antennas, you know, something like that.

**Dave Jones:** And like just budget, but it's not great. Anyway, hope you found that video useful. There was lots of information in there, hopefully. It's a long laborious process to do this.

**Dave Jones:** It would have gone, of course, this would have taken me much quicker if I wasn't shooting a video. It's like a half hour job or something to do this and boom, it's done.

**Dave Jones:** Kind of thing. And as I said, designing and getting a more professional board manufactured, I'd go through a lot more checks than this. But I don't care. I'm pretty confident this board is just going to work near it to electrically work and that's pretty much it.

**Dave Jones:** And I'm not going to look into the stack up of the PCB. It doesn't have I'm sure JLC on their site somewhere tell you what the stack up of the board is.

**Dave Jones:** So, the various layers in there. And of course, that's going to make a difference for your EMC. So, if you want uh the least emissions possible, you want to keep the layers.

**Dave Jones:** So, if you've got a board like this and you've got a layer on the top, then you've got your two inner layers, you want the inner layer as close to the top ground and the bottom and you know, you want it as close to the power plane.

**Dave Jones:** Ground and VCC are effectively the same. The bypass capacitors ensure that. Um then you want it as close as possible to the plane. So, you want the inner core to be thick and then the outer planes and then the outer signal layers to be as close as possible and tiny little thin prepregs next to the layer.

**Dave Jones:** And they don't give you the option here. There's a controlled impedance option. Yes, but that just tells you the standard We could go look that up. But I'm just going to go for their standard stack up.

**Dave Jones:** I'm not too fussed. I just want to see if there's any sort of dramatic difference between having the layers on the top or having them on the inside in terms of H field and eventually far field measurements.

**Dave Jones:** So, that's the plan anyway. So, I hope you enjoyed that video. If you did, please give it a big thumbs up and as always, discuss down below. Catch you next time.

**Dave Jones:** Mhm.
