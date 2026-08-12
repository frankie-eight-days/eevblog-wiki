---
video_id: ggeCYry3gTw
title: EEVblog #1374 - DIY Trezor Crypto Hardware Wallet - Part 1
url: https://www.youtube.com/watch?v=ggeCYry3gTw
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 24, "2": 33, "3": 54, "4": 77, "5": 94, "6": 114, "7": 144, "8": 162, "9": 176, "10": 188, "11": 201, "12": 215, "13": 227, "14": 241, "15": 255, "16": 272, "17": 287, "18": 299, "19": 316, "20": 331, "21": 348, "22": 365, "23": 379, "24": 391, "25": 404, "26": 422, "27": 443, "28": 466, "29": 485, "30": 496, "31": 509, "32": 523, "33": 536, "34": 553, "35": 570, "36": 592, "37": 617, "38": 635, "39": 647, "40": 663, "41": 678, "42": 691, "43": 706, "44": 720, "45": 737, "46": 754, "47": 769, "48": 783, "49": 797, "50": 809, "51": 824, "52": 837, "53": 853, "54": 866, "55": 880, "56": 894, "57": 906, "58": 920, "59": 935, "60": 950, "61": 966, "62": 982, "63": 997, "64": 1017, "65": 1032, "66": 1047, "67": 1061, "68": 1080, "69": 1099, "70": 1114, "71": 1129, "72": 1146, "73": 1166, "74": 1181, "75": 1200, "76": 1215, "77": 1229, "78": 1244, "79": 1255, "80": 1267, "81": 1284, "82": 1304, "83": 1325, "84": 1338, "85": 1348, "86": 1364, "87": 1381, "88": 1397, "89": 1414, "90": 1433, "91": 1451, "92": 1465, "93": 1479, "94": 1494, "95": 1511, "96": 1528, "97": 1541, "98": 1556, "99": 1571, "100": 1587, "101": 1604, "102": 1620, "103": 1635, "104": 1653, "105": 1667, "106": 1683, "107": 1701, "108": 1716, "109": 1728, "110": 1743}
---

**Dave Jones:** Hi, this is the Trezor Model T crypto hardware wallet. I'm sure I've done videos on these before and you should have a crypto hardware wallet if you're into crypto because if you don't hold the keys, then you don't own it. If you're relying on some software wallet or exchange wallet or something like that where you don't own, hold the private keys yourself, then yeah, you might come a gutter.

**Dave Jones:** So, I use crypto hardware wallets. Trezor is the one I use, the one I like. I've got quite a few of them, but I just like the Trezor system. It works. And I've got a couple of these Model T units. I've got the Model 1 as well, but I like the Model T.

**Dave Jones:** It's got the touchy-feely screen. But one of the good things I like about this is that it's actually open source. Not only open source software and firmware like the ecosystem, the application and the firmware that goes into its open source, but it's open source hardware.

**Dave Jones:** So, in theory, you can build one of these yourself without having to rely on the supply chain and potentially get hit by supply chain man-in-the-middle attacks. Because if you aren't aware, simply do not buy a crypto hardware wallet anywhere but the official manufacturer or one of their official authorized dealers.

**Dave Jones:** Because if you do, you can get hit with like a supply chain or man-in-the-middle attack. And the way these things work is that... When they ship you... Well, there's a couple of methods that works. One of them is that they can buy these and then pretend to be a deal authorized dealer and sell them.

**Dave Jones:** And then they can install custom firmware on here, which then can report back and steal your crypto some way like that. Or another way to do it is to supply you an authentic-looking keyword seed sheet with the unit. And then you think, oh, this is my super secret key.

**Dave Jones:** And everything. But no, you do not do that. If your crypto hardware wallet, doesn't matter what brand it is, is supplied with a pre-existing seed key, private key, then you're being scammed. Because you're supposed to generate it on the unit itself secretly and ideally on an isolated, non-internet connected machine, like a clean machine, so that nobody but you has the seed key for this.

**Dave Jones:** The thing with your keyword seed recovery sheet is that you should treat this like cash. Because if anyone has that, then they don't need your Trezor. They don't need your hardware wallet. They can simply use that and recover either onto another hardware wallet they buy or just a software wallet.

**Dave Jones:** They can simply recover that in minutes and steal all of your crypto. So you want to store that in, like, your safe deposit box, bury it in your backyard, although it's paper. So, yeah, maybe something more durable than that. But, yeah, treat it like cash.

**Dave Jones:** Because if somebody has that, they can steal everything. So you can talk about all the security aspects of hardware wallets until the cows come home. But the fact is, they don't need this. They can just get your seed sheet. So, yeah, keep that secret squirrel.

**Dave Jones:** So here's the Model T. And one of the things I don't like about it is the tiny little screen on it. Now, I do not have big fingers. But it's, like, it's really hard to get in there and push these buttons. It's really quite annoying.

**Dave Jones:** So I've always wanted to... try and build my own Trezor Model T and potentially, like, improve it by maybe putting on, like, a bigger, building a bigger compatible screen into it. Because I don't want to have to, like, rewrite the firmware or anything like that.

**Dave Jones:** I want it to be completely firmware compatible, but have a nice bigger touchscreen. So maybe there's a compatible one that works exactly the same with the existing firmware and everything. And then I could mount it in maybe, like, a nice machine down your minimum case.

**Dave Jones:** I could pod it. And I could put on multiple USB connectors and things like that. Because if you're USB, port on this goes bust, then, well, you haven't lost your crypto, but it's just really annoying because then you've got to get your seed recovery sheet

**Dave Jones:** and then set up a new one from scratch. And that's a lot of time and effort. It's really annoying. So, I don't know, you might put on multiple USB ports. I even had ideas of maybe adding, like, a second little memory LCD on there.

**Dave Jones:** Or a E-Ink LCD. And potentially having, like, a power-up counter on there. So, like, you can secretly know if anyone's been trying to hack into your little crypto hardware wallet. So then you'll be able to know if anyone's tried to secretly hack into your hardware wallet

**Dave Jones:** without knowing because then it increments a counter on there. You'll know how many power-ups it's done and things like that. Although they could probably implement that in the firmware as well. So, Trezor, if you're listening, I tweeted to this years ago. But anyway, yeah, that'd be a nice feature.

**Dave Jones:** Like, you know, it's been powered up X amount of times. So, yeah, you never know when you might want to know how many times this has been, you know, powered up. So, yeah, that's one of the cool things about this is that it's completely open-source hardware and software

**Dave Jones:** so that you can potentially, in theory, make your own and then bypass the supply chain entirely so that you're not trusting anyone. So, anyway, let's take a look at their website because when they first released this, I was disappointed that they didn't actually have the hardware files,

**Dave Jones:** the hardware, they didn't release the hardware files for it. And they have actually since released it. It's been a while, but haven't gotten around. So, let's take a look. This is their GitHub page. So, they've got the Trezor firmware here, the Trezor Suite, which is the software.

**Dave Jones:** They transitioned from, like, a web-based user interface to an application-based user interface. And I like it much better. Although, the web one, of course, you didn't have to install any software. It just worked from the interwebs. But, yeah, that's it. So, the application is open-source.

**Dave Jones:** I think it might be multiple. I use Windows, but it might be available on multiple platforms. Then they've got Kinect. Easy integration into third-party services. Account balance backend. They've got a communications daemon written in Go. I don't know. But, yeah, like, there's a very cool ecosystem surrounding the Trezor here.

**Dave Jones:** And in terms of, like, being able to integrate it into other products and stuff like that, which is really cool. All right, so let's take a look at the GitHub repository. We've got the Trezor Suite Mono Repo. I don't know what that means.

**Dave Jones:** Look, I don't know. Like, I don't use GitHub, so if I use all the terminology wrong, I just don't know what I'm freaking doing. It's like, I do have a GitHub account, and I've got some stuff on there, including DaveCad, but I just, no, I'm not a GitHub person.

**Dave Jones:** Trezor Firmware. We're not really going to touch the firmware, but because, you know, I want to build up one of these from scratch, design and build, yeah, we're going to have to get the firmware. I don't want to have to compile it and everything,

**Dave Jones:** but I want, like, the image that I can download to my micro when I plug it on there. So, that could be an adventure in its own right. So, we won't go into the... Trezor. So, we won't go into the firmware. Blockbook. Sithon HID API.

**Dave Jones:** I have no... Python wrapper for the HID. I got no idea. MicroPython Connect. Wallet data. Data, there you go. Blockchain. Yeah, we want hardware. We want hardware. Trezor Common. Don't post issues. Trezor UTXO Lib. Android. That's nice. Link. Test scenarios. Password. Open Manager.

**Dave Jones:** HD Wallet. No. In Java. No. Trezor Wallet. Obsolete. Do not use. Address Validator. Trezor Hardware. There we go. Trezor Crypto. Fido 2 Test. Stellar Account Viewer. Okay. Anyway, there we go. We're in the hardware. It's C. It's AGPL 3.0 License for those playing along at home.

**Dave Jones:** Let's go into the Trezor Hardware, shall we? And they've got... That's it. They've got the case, the electronics, and a production test, self-test thing, something like that. We're not really concerned with that. Doc make file, Trezor, test Trezor. Yeah. It's just some sort of production testing.

**Dave Jones:** Not too fussed about that. Although you might have to use it if you build it up. Probably not. Should just be able to... In theory, you should just have to take the Gerber files that they should provide and then send it to the manufacturer,

**Dave Jones:** get it made, buy the parts based on the BOM, and then you burn the firmware. I think it's an ST-ARM micro in here. So you just burn the firmware. You use an ST programmer and Bob's your uncle. That's the theory anyway. So the case, let's have a look at the case.

**Dave Jones:** There are two different ones. One's the model one. It's the older one. But if you're going to get a Trezor, I recommend the model T. It's just got the nice touchy-feely in a bigger touchscreen. It's just more better. So that's version three of the Trezor one,

**Dave Jones:** but really model T. So you might have to use this as a baseline to design like a custom case or something. It's got top and bottom STL files. That's it. Okay, last update, 11 months. 11 months ago. Electronics, this is what we want.

**Dave Jones:** Ta-da! Let's have a look at the older model one, and it's got like the board JPEG and stuff. Oh, yeah, there it is. That's the model one. I've done a teardown of that. Programmer.board, that looks like .sketch. They look like Eagle files. Raspi?

**Dave Jones:** What's Raspi? Oh, is that a programmer? Oh, is that a Raspberry Pi programmer? Oh, I think that's a Raspberry Pi programmer, is it? I guess so. That's part of their programming system, I would presume. They've got a bomb. That's for the old one.

**Dave Jones:** Anyway, we want the new one, because I want to make this like a multi-part series, actually designing and potentially improving the Trezor, because it's all open-source hardware, which is cool. So we'll go in the model T. That's it. That's it. The board and the schematic file.

**Dave Jones:** Really? Where's the project file, the bomb? Where's the... It'd be nice if you had a PDF of the schematic and images. Where's everything? Last input five months ago. Geez, they haven't really updated anything, have they? So these look like Eagle files. We're in, yep, Eagle version 7.7 of Eagle.

**Dave Jones:** It's the XML. No wuckers. Board file is also done with Eagle 7.70. So that's it. Well, that's disappointing. That's not really... I mean, it's open hardware in terms of, well, you can get the board and the schematic, so we can load those into Eagle,

**Dave Jones:** although we can import them into KeyCab, which I'll try and do here, or we can import them into Altium, whatever your favorite package is, you should be able to import that and then get the board manufactured. But where are the Gerbers? Where are the Gerbers?

**Dave Jones:** The whole idea, the cool thing about this, is that you should just be able to grab the Gerbers, upload them to whatever $2 PCB manufacturer you want, and get the boards delivered for like $5 delivered or something, whatever the ridiculously low price is this week,

**Dave Jones:** and make your own. And then just, and where's the bomb? Where's the bill of materials? The bill of materials is going to be very different for this than it is from the, well, maybe it's like built into the schematic, but no, that's, no, no, that's a thumbs down.

**Dave Jones:** That's a thumbs down right off the bat for not having, like, a bill of materials, and... and other stuff. And there's, there's, uh, uh, Pavel. Good on you, Pavel. Look at that beard. Looks like a happy guy. All around hacker working on Trezor,

**Dave Jones:** Tropic Square, NixOS, another open source project in Prague in the Czech Republic. Hi to all my Czech viewers. Um, so, yeah, please, um, you've got more stuff there. Please just dump it in here. I'm sure it's not hard. Anyway, I'll download those and see what we get.

**Dave Jones:** Now, one of the annoying things about GitHub and a trap for young players is you can't just go save link as like that. Because then it'll download the HTML instead of the real file. So, even though it'll, it'll actually save it as the .brd file,

**Dave Jones:** it's actually HTML, and it won't work. So, yeah, you've got to, like, download the Git thing. I don't know. Yeah, and, like, that's another annoying thing. Like, I don't even think you can, like, download. Can you? Like, you can't download this particular, there's no, like, there's goto file,

**Dave Jones:** but there's no, like, download zip or whatever. It's just, it's stupid. I know you're supposed to, like, do the command line, git pull or some rubbish like that, I don't know, but, yeah, anyway, here we go. We can download zip. Okay, so I've got the latest version of EagleEat 9.6.2.

**Dave Jones:** It should be able to open the old ones. I don't know, I don't use Eagle, but, yeah, let's go. And we're in like Flynn, look at that. Beautiful. There you go, there's our, it doesn't, oh, I didn't know Eagle opened up different windows

**Dave Jones:** for the schematic, I don't know. It's been a long time since I've used it. But there you go. And it looks like, see, we can get our bomb from here potentially. Like, I don't know how the Eagle thing works. It device, if they got, like, footprints,

**Dave Jones:** but they don't have, like, links to anything, do they? Like, they don't have, like, digi-key links or something like that. See, it'd be nice to have a bomb for this thing. Like, all your generic parts and things like that, that's all, like, hunky-dory.

**Dave Jones:** Like, all your, you know, your LCs and Rs and stuff. No wuckers, you can just sort of get anything. But, you know, things like the LCD and stuff like that, you've got to get very specific ones. There it is, okay. So that looks like at least they've got

**Dave Jones:** the very specific part number. No, that might be the connector. See, that might be the connector. I'll have to Google that one. But that could very well be the connector, not the actual LCD. And that, well, kind of makes sense on the schematic side of things.

**Dave Jones:** But that, that's incredibly annoying. Most other things are being okay. Like, because that's one of the things I want, is, hey, what LCD? What LCD do they use in there? Have I done it? No, I don't think I've done a teardown of the Trezor Model T.

**Dave Jones:** I'm sure you could get the info somewhere. Someone's probably done a teardown. Get this thing made. So, ideally, maybe at the end of this video series, I'll have, like, a, a bomb, like, either a digi-key or a mouser bomb or a JLC, like, bomb or something like that,

**Dave Jones:** and then the board. And you can just potentially just turn-key it. That'd be nice. If you can just, you know, hit one of those auto-buttons, you might even be able to get, maybe, this could be, leave a thumbs-up in the comments. Leave a comment down below if you want to see this.

**Dave Jones:** Maybe I could potentially use one of those, like, turn-key services, perhaps, so that, and then you can make it publicly available, because this is all open-source hardware, so if I do anything with this, I've got to re-release it as open-source hardware as well.

**Dave Jones:** I can make it publicly available, so anyone, in theory, can just push a button, and they, then you get an assembled board, but then you've got to trust the manufacturer, don't you? You've got to trust that they haven't done anything to make this a sneaky bugger.

**Dave Jones:** Like, but then again, once you get the hardware, you can just, like, re-flash it yourself, so that's not, you know, you don't have to get it programmed. You can just nuke it. So that's fine. So that's pretty safe. But, yeah, let us know if you want me to do that.

**Dave Jones:** Maybe that should be the goal of this little series. Yeah, these clamps up here, you know, we've got part numbers, we've got part numbers for, like, the fuse here and stuff, and, you know, so that's okay, but it's just not the same as having a proper bomb.

**Dave Jones:** Please, Trezor. So on the... V-Blog open-source hardware logo thing, which is still a thing. A lot of people use this, and I think it's great. They do provide the schematics and the PCB, and they do have the mechanical CAD files, firmware, software, but they don't have any...

**Dave Jones:** There's no... Well, there might be design documentation. I have a... Well, they don't have a bill of materials, so it fails at that. License start use does not restrict commercial use, so commercial use is fine, I believe. Yeah, so it's, like, bill of materials is, like, really annoying.

**Dave Jones:** And then there's arguments over, well, yeah, you get the PCB, the original file, but you don't get the Gerbers. So it's, like, maybe I should have added, like, another one saying manufacturability or something like that. Anyway, let's open up the PCB. Board. .board file.

**Dave Jones:** And bingo, we're in. No wuckers. Like, these are all big, fat dots. What's going on there? I don't... Once again, I don't use Eagle. Is that, like, an Eagle thing, or is it... And they're all, like... They don't line up, so I'm not sure what the deal is.

**Dave Jones:** It's not like one is the board outline, because here's your board outline. I so don't know how to use Eagle. Yeah, so we've got... Yellow is our board outline. No wuckers. So I don't know what the deal is with the other thing. Is that an Eagle thing,

**Dave Jones:** or is it just something that they've done? I don't... I don't know what the deal is. Anyway, yeah, there you go. Oh, it's a four-layer board. Okay. Oh, I didn't think that the free version... The free version supports a four-layer board. I'm pretty sure it doesn't.

**Dave Jones:** No, it doesn't. Two schematic sheets, two signal layers. There you go. And, of course, it's a tiny board, so it fits in the area, but it only supports two signal layers. So the free version does not support... You cannot get this thing... In theory, like, we should not even be able

**Dave Jones:** to generate the Gerbers, I guess, from this. So that's pretty useless. So, yeah, I might try and do the import thing. I might import it. I might import it into KiCad. I was going to do that anyway, because I don't want to use Eagle,

**Dave Jones:** because KiCad, of course, is open source, so it's more fitting to use KiCad for, like, an open source project like this. Whatever. Anyway, it loads. Okay, so I've got the latest version of KiCad, although there is, like, a version 6 beta or something.

**Dave Jones:** Meh, whatever. Let's see if we can import an EagleCAD. Electronics, Model T. Can we do... No, we can only just do the board. Import. Okay. Oh, hang on. We did get an error message. Unsupported Eagle layer T-test. 37 converted to drawings user layer.

**Dave Jones:** Okay. I don't know. Restrict drill legend measures. Okay, so there were issues importing this, but we did get it. There you go. So we do have the layer details. That's nice. Don't like the blue on black. There you go. They've done their layer stack up.

**Dave Jones:** Very nice. It's a 1mm. PCB. Okay, there you go. Didn't know. Oh, yeah, that makes sense in a tiny little, you know, thin thing like that. Might not be able to fit 1. Because you've got to get the touchscreen and the whatnot in there.

**Dave Jones:** So 1mm already, that's a bit odd. But, you know, I might go for, like, 0.8. Or because I'm going to design my own, like, you know, improved version of it, bigger potentially, then, well, it can be 1.6, standard 1.6. Or, you know, you typically go with a 0.8.

**Dave Jones:** You wouldn't normally go with a 1, unless you had to, because it's just less common. Vertaki plan. I have no idea what that is. Jeez, that's going back, isn't it? 24th of the 7th, 2018. Wow, is it that old? Really? Okay, now it's mixing sheets.

**Dave Jones:** So the brown in the background there, that is the generated template for KiCad. And the blue one is for EagleCad. So that's, yeah, that's kind of annoying, isn't it? Anyway, it looks like, yeah, this has not gone well. Um, it's, it's got, like, broken nets and,

**Dave Jones:** well, it's showing broken nets and stuff, but I guess if you, because it's a four layer, we've got a ground and power, and it's just, it's not doing terrific. So, yeah, that's not, you know, it's not trivial to import these and to convert between one package and another.

**Dave Jones:** Once again, you know, if you've got more experience in, like, importing Eagle files into KiCad, like, I, I really am a complete noob at KiCad, uh, let alone, importing Eagle into KiCad, so, yeah. Um, and Soldermask expansion. Look at that. No, I mean, it's just, it's just none.

**Dave Jones:** Look, it's just complete under, under the part, under the entire part, not around the pad. Oh, that's terrible, Muriel. But those pads seem to be okay, but, yeah, no. So you've got to fix, like, the Soldermask expansion. So you can't just, like, import this

**Dave Jones:** and then just hit Generate Gerber and get it manufactured. You know, it's going to be an absolute mess um, let alone what's happening with all these nets. I mean, ground, you might have to assign, you know, the, the power planes probably weren't imported properly.

**Dave Jones:** I don't, you know, I, like, I, I still don't know what all this deal up here is. Like, this converted these into lines. Yeah, that's, it's going to require a lot of cleanup. This is many hours of me to, A, figure out what's going on here,

**Dave Jones:** and then, B, clean it up. So, I won't be doing that in this video. This is just making, see, seeing, in part one, seeing if I can I can import and see what was what. Very disappointed that we couldn't just get the Gerbers

**Dave Jones:** and just get it manufactured, because I might have done that. I might have just got the, got the Gerbers and then boom. Um, so, yeah, but I can still do that. I can generate them from Eagle, I guess. Um, but, yeah, can't just, you don't want to be, just be pushing

**Dave Jones:** Generate Gerber on this, that's, that's just a mess. Um, so, I'm not sure what's happening with the ground and power planes and stuff. Um, so they're obviously the only not net connected things. So they're all ground. What's, like, P$1? Um, like, I don't, I don't get it.

**Dave Jones:** Anyway, uh, these do have nets, I see too, Pat. Like, it just doesn't know what it's doing. So, yeah, but that's common with imports. So, yeah. Some work required. Generated a .pretty. I don't know what a .pretty is. And then it's, like, loaded all this and, like, I don't, like,

**Dave Jones:** 0201? What, is there an 0201 part? No, there can't be. There's no .pretties. Like, this is supposed to be the library, imported library for the Eagle import. I mean, look at all these packages. That's just, no, that's just, no. That's bad. 2512 and then $2512 refile.

**Dave Jones:** Like, I don't, this is a mess. I'd be tempted not to even reuse that at all. Like, uh, if I'm gonna do a new one, I'd import the schematic, get the schematic tidied up, get the BOM tidied up, and then just generate a new board and start that from scratch.

**Dave Jones:** 'Cause it doesn't take a long time to lay out a board like that. I mean, you know, there's not a huge number of parts on it. It's not very complicated. So, uh, yeah, you know, you might take the outline and stuff like that, if you were gonna use that,

**Dave Jones:** and then just nuke it. Maybe, you know, keep some things like the connector in place and stuff like that. But you might want to nuke that from orbit. Uh, it's the only way to be sure. I say we take off and nuke the entire site from orbit.

**Dave Jones:** It's the only way to be sure. See, here's the problem. Because there was no project, KiCad only imports, like, project files, and if you select just the schematic or PCB, it wants to create, like, a new project directory for the schematic and for the PCB,

**Dave Jones:** like, separate ones. It's just, I don't know, I don't have enough experience with KiCad, but that seems to be a limitation. For some reason, KiCad shut down, and it's like, I just, what the heck happened? Oh, God, no, this is a mess. 'Kay, import the schematic.

**Dave Jones:** What? I opened the schematic, and I got the project. Not the PCB. What the heck? Okay, anyway, um, yeah, that's weird, but we're in, and there's our schematic. It's done an okay job. That's pretty usable. I don't know what all these words here are.

**Dave Jones:** That is not, uh, that is not English. Symbol RAM A3. Why is there a RAM A3 symbol under there? Okay, there you go. Why is it moving the frame? Is that a KiCad thing? Oh, like, the templates. Moving the template with the part.

**Dave Jones:** That's really weird. Anyway, the part is the part. So, how do, can we, like, edit a part? Once again, I don't have enough experience with KiCad to really, like, know what I'm doing here, unfortunately. So, once again, like, this is many, many hours of work

**Dave Jones:** to get this, like, to import this from Eagle into KiCad, and then get it all usable, and set up the proper bill of materials, and, you know, KiCad, I believe it supports, like, all the datasheet links and the BOM links and stuff like that.

**Dave Jones:** But you'd have to go through, like, yeah, every single item. Anyway, let's do, can we get a 3D view of the PCB? See if it works. Cannot determine board outline. Nah. So, once again, yeah, it, like, it didn't import the board outline properly.

**Dave Jones:** So, there's our, there's our 3D view. So, yeah, that's not exactly spectacular, is it? Yeah, it just thinks we've got a square board. But, yeah, that's alright. Like, there's no component, I didn't, you know, it's not gonna import, like, component models and stuff like that.

**Dave Jones:** Um, so, yeah, that's not a thing. So, that's probably as good as you can expect. Oh, that's what, okay, that's what, is that what those pads, right, you know how I thought that the, uh, that the capacitors had the solder mask all the way under?

**Dave Jones:** It wasn't. That looks like it's glue. That looks like it's a, a glue point. I don't know why you'd bother. It's not a double-sided load, so you don't have to glue the components down before you reflow them. Um, so, yeah, I, is that part of, was that in the Eagle thing?

**Dave Jones:** Or is that part of the import? So, yeah, I assume that that's what that is without actually going and inspecting. But, as I said, yeah, there's no solder mask, uh, between pins or anything like that. So, yeah, you can't just import this and get it manufactured.

**Dave Jones:** It's just, it's, no, it's not gonna work. Right, so that's kind of annoying. So, that, uh, yeah. What do we do for part two of this video? Leave it in the comments down below. Do I spend oodles of my time trying to convert this into,

**Dave Jones:** and tidy this up into a workable KiCad project, and then try and, like, make it, you know, get all the bill of materials, and then make it all turnkey and stuff like that? There's probably three or four parts to just doing that video.

**Dave Jones:** Well, at, at least, really. Or should part two of this just be me, like, seeing if I can just manufacture this myself, actually get one made from the supplied Github, the Eagle file. So, just use Eagle, just generate the Gerbers, hopefully there's no issues there,

**Dave Jones:** and then, uh, send it to, you know, one hung low PCB manufacturer, and get it made, and then order the parts, try and get some sort of bill of materials, probably manually, and then, um, get it together. Like, and then build it up, and see if I can get a working Trezor.

**Dave Jones:** Should that be part two? Or do you want me to actually go down the rabbit hole of effectively learning KiCad? Um, and 'cause, you know, like, it's one thing to do KiCad from, you know, with very little knowledge of KiCad, although I'm an experienced, professional PCB designer,

**Dave Jones:** I'm an Altium guy, right? So, very little KiCad experience. It's one thing to actually start a board from scratch, and it's another thing to, like, import an Eagle file and be messed, and be left with, like, a huge mess, to try and tidy up.

**Dave Jones:** It might even be easiest just to simply start from scratch, get a, like, a physical printout of the, uh, of the schematic, and just manually create parts from scratch, rather than try and import. Although we do have this schematic imported, but is it better just to simply, I don't know, start from scratch?

**Dave Jones:** Ah, that, like, I, maybe this STM part's available in KiCad, and, you know, you've got the, you know, I'm sure there'll be a USB, uh, C connector in, you know, the parts somewhere, and, and things like that. So, you know, apart from that, it's all fairly generic.

**Dave Jones:** Oh, there's a few oddball, uh, protection devices, uh, perhaps, like ESD protection and stuff like that, but is it easier just to start from scratch? Or should you... I don't know, am I pushing the brown stuff up a hill with a pointy stick by trying to import the Eagle files?

**Dave Jones:** Which is easier? Anyway, I'll leave it for this video. Please leave it in the comments down below, what you think I should, uh, do with this, because, well, yeah, I don't know, schematic seems okay, but I, yeah, I don't know. I could just see a lot of hours working this.

**Dave Jones:** Anyway, yeah, I think, um, yeah, that, that's a thumbs down for the Trezor open source, you know, technically you can do it, but they don't make it easy to manufacture one of these on your own, and really, that would've been, like, I'd be advertising that fact.

**Dave Jones:** Look, if you wanna buy it from us, we're safe and secure, you know, buy us, it's already assembled, tested, done, ready, assembled, tested, programmed, and everything else, but, you know, if you're ultra paranoid, or you just wanna do it yourself, um, then here's all the Gerber files,

**Dave Jones:** or here's, you know, and here's the digi-key bill of materials, or here's, you know, the turnkey JLC, uh, thing. So Trezor would actually be in a much easier and simpler position to actually generate something like that. I've gotta, like, go through all the hard work

**Dave Jones:** to redo the, the whole kit and caboodle. So, yeah, not impressed. No bill of materials, no Gerbers, just a couple of Eagle schematic and PCB board. Aww, fail. Anyway, hope you liked that. Catch you next time. Thank you.
