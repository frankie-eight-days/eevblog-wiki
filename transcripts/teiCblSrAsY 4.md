---
video_id: teiCblSrAsY
title: EEVblog #968 - Mystery EDA Package
url: https://www.youtube.com/watch?v=teiCblSrAsY
source: youtube-asr
timestamps: {"0": 1, "1": 13, "2": 26, "3": 40, "4": 56, "5": 73, "6": 94, "7": 103, "8": 113, "9": 126, "10": 153, "11": 168, "12": 189, "13": 202, "14": 210, "15": 221, "16": 236, "17": 253, "18": 265, "19": 273, "20": 288, "21": 302, "22": 314, "23": 330, "24": 337, "25": 352, "26": 360, "27": 373, "28": 383, "29": 398, "30": 410, "31": 425, "32": 438, "33": 449, "34": 465, "35": 476, "36": 488, "37": 505, "38": 519, "39": 532, "40": 546, "41": 563, "42": 577, "43": 588, "44": 605, "45": 620, "46": 637, "47": 651, "48": 669, "49": 680, "50": 690, "51": 699, "52": 710, "53": 723, "54": 740, "55": 750, "56": 764, "57": 776, "58": 793, "59": 806, "60": 818, "61": 833, "62": 846, "63": 859, "64": 869, "65": 877, "66": 893, "67": 921, "68": 934, "69": 945, "70": 958, "71": 969, "72": 985, "73": 999, "74": 1011, "75": 1021, "76": 1031, "77": 1045, "78": 1067, "79": 1076, "80": 1090, "81": 1102, "82": 1124, "83": 1132, "84": 1143, "85": 1153, "86": 1166, "87": 1177, "88": 1189, "89": 1204, "90": 1221, "91": 1231, "92": 1248, "93": 1264, "94": 1277, "95": 1296, "96": 1304, "97": 1314, "98": 1327, "99": 1342, "100": 1352, "101": 1370, "102": 1379, "103": 1390, "104": 1400, "105": 1417, "106": 1431, "107": 1452, "108": 1468, "109": 1480, "110": 1488, "111": 1502, "112": 1528, "113": 1537, "114": 1552, "115": 1574, "116": 1591, "117": 1606, "118": 1616, "119": 1628, "120": 1638}
---

**Dave Jones:** Hi, I've got a bit of an interesting one today. I thought we'd take a look at an a rather obscure EDA slash PCB package. Now, I actually got a PCB file that I've got to open.

**Dave Jones:** Um, and I've got the Gerbas as well, but I got the original PCB in a program called Win PCB, and I I don't recall ever hearing of this thing, so I thought we'd actually check it out and see what we can see.

**Dave Jones:** Um, so let's actually have a look at here. It comes from a company called CSI EDA and they're a Japanese uh company and they, you know, here's their product lineup.

**Dave Jones:** Um, let's have a look. Win schematic, Win Spice, Win PCB, which is the one we're after, PCB design 2, Win signal, uh, which would be signal integrity, uh, stuff, i.e., you know, simulation, high, you know, impedance control and all that sort of.

**Dave Jones:** In fact, that one. No. Yeah, that one's just impedance control and cross talk and things like that. Gerber cam editor tool. It's got a 3D PCB viewer, Electra, Electra route, auto routing uh tools, and uh they're just the various packages that you can get.

**Dave Jones:** But you can see it's um like it looks like an old school program. Probably J main market would be Japan because I've never heard of the thing. Um I maybe I've heard of it but I've never like looked at uh the thing before and uh it's got separate modules where you know this is like really you know like older school stuff.

**Dave Jones:** Most of the packages these days are kind of like integrated um sort of thing which is much better but I know you know likes of Keycad and things are uh separate.

**Dave Jones:** But anyway, I thought we'd have a look at this. And it uh if you're wondering about the uh pricing of this package, here it is. It's here in Japanese yen.

**Dave Jones:** So, we'd have to convert this. So, uh let's like if you get like the CSI EDA Pro pack, uh for example, then you get wind schematic, the PCB Pro, the Gerber, and the 3D viewer.

**Dave Jones:** basically everything that you needed or you know for 2,000 Japanese yen um sorry 2 million Japanese yen you get the uh router as well and they do actually have a free viewer as well which I have actually downloaded and tried but it didn't work so I'm going to download the trial of the full package here and what the I just converted uh 2 million Japanese yen here and it's into US

**Dave Jones:** dollars it's 17 thou 17.5 half th000 US. Wow. Um I found another website which like said it was in the order of like $23,000 or something like that. So that's that is insane price.

**Dave Jones:** But hey, maybe is this uh my Japanese viewers out there is win PCB and CSI EDA is it like a de facto standard in uh Japan or whatever. Anyway, if you go into the win PCB here, which is the package I'm after because I've got a PCB file, you know, here's all the files that it all all the stuff it can do.

**Dave Jones:** Creating PCB parts, blah blah blah. You know, I'm sure it's a fully featured uh PCB uh package, but all separate modules of course, which doesn't make it as integrated as um you know, Alium and other uh type packages out there.

**Dave Jones:** But still, hey, I'm got nothing against like having separate tools like that. I kind of like it. Um, actually I'm a bit old school in that regard. Now I actually had a look.

**Dave Jones:** Um, you can't download it. You can like do an inquiry or something like it's even impossible to find the price on here. I think I like I only found that by googling and stuff like that.

**Dave Jones:** So yeah, I couldn't find it. But after googling some more, I found it's actually available for download from a company called Ruten Technology. And being Australian, I couldn't help but think of this.

**Dave Jones:** Sorry. So, I tell you what we ought to do some rooting in the back of the Yeah, sorry for that Kevin Bloody Wilson there for those. I don't know.

**Dave Jones:** It might be a lot of Kevin Bloody Wilson fanboys out there. Anyway, let's uh have a look at this thing. I downloaded it and this is like they give you a license but I think there's also a hard dongle uh that you can optionally use as well.

**Dave Jones:** It asked us uh before um look at this. This is the interface of actually installing this thing. Um and it said do you wish to do you have a license?

**Dave Jones:** I went no. Do you have a hard uh dongle? And I went no and it brought us to this uh clunky looking thing. Anyway, we can create a new user here called Dave and we can log in.

**Dave Jones:** It's no hard key or license client. Do you want to run in evaluation mode? You bet you we do. So, let's run it. And tada, we're in. Sorry, popped up on the other screen by default.

**Dave Jones:** We're in like Flynn. Welcome to CSI EDA version five. Click here if you want to close this window. Oh no. Look. Um, so this is like the um we're using got the evaluation.

**Dave Jones:** I'm not sure what the limitations of the evaluation. I read somewhere that there could be like a pin limit or uh something like that perhaps. Anyway, we've got uh demos uh PCB1 uh demo.

**Dave Jones:** There we go. We got a nice looking demo. I just use my scroll wheel scroll wheel here and we're in like Flynn. And uh I don't like the big uh crosses there.

**Dave Jones:** Um when you're looks like you've zoomed to a certain point and you get those crosses. Yeah, that's just really really kind of uh frustrating. I'm sure you can change all this now.

**Dave Jones:** Yep. I can pan around using my uh right mouse, hold it down, and then drag. It's a little bit It's a little bit jerky. Um that's just not my screen capture.

**Dave Jones:** It seems to be a bit but it it's okay. Zooms in and out. Look at that. No workers. But yeah, it's hardly um like you know what you see is what you get.

**Dave Jones:** But you can see the hole sizes in there, which is really good. Presumably, I'm just I haven't used this before. I'm going to go in there to my pad dimensions.

**Dave Jones:** Here we go. Pin. Uh that's the X. Where's the whole size? Whole size unit. Mill. We don't want none of that. Uh mill rubbish. I only use mills for um I don't use them for hole sizes of course cuz these drills are all metric.

**Dave Jones:** But if we change that to say uh 1.1 mm. Yep. It's going to change that in real time. But yeah, look um this is like really old school gooey type interface.

**Dave Jones:** Is that someone remind me is that like Delelfy that Alium was originally written in and kind of still is a lot of it. Um, I don't know. That button looks That's sort of those buttons look kind of uh familiar.

**Dave Jones:** Does anyone know? Oh, what happened there? No. What happened to our pad? Oh, no. There we go. Okay. Right. Cuz we had selected it. Okay. There we go. So, we can go in there.

**Dave Jones:** Mills. Why does it keep going back to mills? Because I'm defaulting to it or something. Anyway. Yeah. There we go. Tada. Look at that. And it's changed all in real time.

**Dave Jones:** Beauty. So that is all got the basics of a PCB package. So this is win CSI EDA or root using root technology. I love it. I don't know if root are an affiliate company or reseller or whatever.

**Dave Jones:** But anyway, I was able to do the download from there. That's kind of groovy. I'm not sure. Uh yeah, you can select it just that trace segment. What if you hold down shift or something?

**Dave Jones:** Oh no. Yeah, there we Okay, we can select multiple ones. Can we hold down like something and select entire How do you select entire traces? I don't know. Attribute, edit, select.

**Dave Jones:** Anyway, it's it looks like a reasonably fully featured PCB package. We've got an inspector that presumably we can inspect a part. Can we? No. Oh, there we go. The track attribute showing you the entire net.

**Dave Jones:** That's kind of groovy. and uh packages. There's a list of package files that we got. No, it's very similar to out in the like the little preview window down there and things like that.

**Dave Jones:** Um but that's that's not too shabby. They're they're all the different p all the different pads in here are they? So there's an AT mega 128 and they're all the different uh pads and uh that are used and VAS presumably are they?

**Dave Jones:** And we've got DRC design rules setup. It's all very familiar default. So you can set it up. That's all. Oh, I kind of like the grid array there. So copper to copper for example.

**Dave Jones:** I like that. There you go. You can do pad to pad clearances. H same net route length limit track width minimum all that sort of stuff. And you could s store those as a configuration.

**Dave Jones:** So if it didn't have that, then uh that would be really kind of messy. Um can we how do we turn off layers? Top bottom. That just focuses on a layer.

**Dave Jones:** And uh not sure how to go single layer mode. Oh, look. We can do density analysis. Density net all. Oh, I love a good density analysis. Look at that.

**Dave Jones:** There we go. All our hot spot is around that uh micro there that uh at mega was it? So you can see that's just like the routing density where you know like you you can do that with your board to see where all the you know there's not much room left to route additional traces and stuff like that.

**Dave Jones:** So that's kind of cool. It's got all the funky stuff. PCB 3D designer and database report image vector height diagram. That would be for all your 3D stuff and gate and pin swapping.

**Dave Jones:** Oh, nice. It's got pin swapping. Poor thermals. Setting it all a command line for those who uh Oh, no. Didn't pop up anywhere. Oh, yeah. There it is down there.

**Dave Jones:** Is that the command line? There you go. Can probably just run commands. There is, I think, a hotkey list for it as well. Of course, one of the uh keys to a good efficient uh CAD package is having and knowing your uh PCB shortcuts.

**Dave Jones:** But uh layering colors, it's pretty fullfeatured package. Wow. That wannabe for if it is 2 million Japanese yen designed for manufacturer. Cool. Just for kicks, I'm going to see if I can unout.

**Dave Jones:** Yep. Can I? All nets will be unouted. But are you sure? You bet. I'm sure. There we go. And that is the rat's nest. Uh that's the rat's nest display.

**Dave Jones:** It takes a little bit to redraw the um the fills on there. They're not terribly quick. So, it's not the most responsive thing when the copper paws are on.

**Dave Jones:** Presumably, you can uh turn the copper paws off and stuff like that, but yeah, it's left. So, it's unouted everything except and left all the uh paws and everything else.

**Dave Jones:** I wonder if we can just uh reroute that. Set up auto route. Can we just auto route designer or ah Spectra? No, we've got to go over and use the auto route tool.

**Dave Jones:** Do we run all No, run auto router. But you can export to Spectra and other better has process in your application instance. Please wait for end of routing. Yeah.

**Dave Jones:** Okay. I want to see it laying out the tracks. Come on. Come on. A. Is it like Yeah. No, it's not doing anything, is it? No, that's boring. Oh, well, worth a shot.

**Dave Jones:** Oh, here we go. I just loaded in sample one 3DI. So, it's called up the 3D tool here. And uh that's There we go. Can we just hold control and and spin it?

**Dave Jones:** Shift move. Alt. No. How do we spin? Damn it. I want to spin this puppy in three dimensions. Anyway, copyright 1995 to 99. Yeah, that kind of says it all.

**Dave Jones:** Oh, check it out. We got it auto rolling. We have auto rolling. Oh, great. Oh, look at that. Oh, that could be my new intro for the blog. What do you think?

**Dave Jones:** I get that old spinning intro. If people remember, I had a spinning 3D um 3D board back when um you know like I don't know episode 20 or something um to 50 or some the early episodes and I actually did that in Alium.

**Dave Jones:** That was a board I designed at Alium and I actually spun that by hand using a space navigator. Um so if you go watch the intro to those videos, yeah, I spun that by hand and that took quite a bit of skill.

**Dave Jones:** But there you go. Whoa. Makes you dizzy. Oh man, psychedelic. I loaded up another one which was uh the largest at 3.2 meg here. Um it seems to have not remembered that.

**Dave Jones:** Yes, I wish to run eval mode. And uh this one looks fairly funky. So let's uh let's pull this full screen and let's go auto roll because I know you want to.

**Dave Jones:** Oh, that's really struggling. And I've got no slouch of a machine, let me tell you. There we go. I'm scrolling in all three axis. Come on, flip it over so we can see the parts.

**Dave Jones:** It works. This would have been state-of-the-art for the day. Uh, no doubt. Well, I'm not sure, you know, when when did they introduce this? You know, who knows? You've just got to hold down the button and move your mouse.

**Dave Jones:** There you go. We can zoom in. Look at that. Can we zoom into the board like you can in AI? I wonder. Oh, yes. We can see inside the VA.

**Dave Jones:** Look at that. And see inside the board, can we? No, we're not. No. Sorry. It's not that advanced cuz that's cool. That's what you can do in Alium is you can fly inside the board.

**Dave Jones:** It's really impressive on uh multilayer boards and stuff like that. So, it's really it's actually quite handy. But yeah, there you go. That's the 3D package. And that is a separate uh program.

**Dave Jones:** So, what do we got system information wise here? CPU. There you go. Copyright. It's got still got copyright 2006. Wow. Wow. Um, and that's the thing. I'm running version 5.4 here and I think this is from the routin uh website, but if you go to CSEDA, I think I downloaded the latest viewers 5.8.2.

**Dave Jones:** two or something. Um, so yeah, I don't know how update how frequent this software is updated, what the latest version is or whatever, but this is the latest version on the written website.

**Dave Jones:** So anyway, h contrary to what it says on the website, this actually seems to be fairly integrated. I mean, you know, here's schematic and PCB um, you know, all operating in the same window.

**Dave Jones:** It's, you know, very familiar to uh Alium uh users, for example, and other uh CAD packages. So, um yeah, I'm not sure what's going on there. I can't show you.

**Dave Jones:** I haven't screen captured the other screen here, but if I actually go into what it's installed in my programs menu, there's a CSI EDA version 5. There's the Gerber designer, which is separate.

**Dave Jones:** There's the 3D designer, which we've seen, which is a separate package. There's a route designer, which is separate, and signal integrity. But apart from that, um, they're identical. Um, so, and the signal integrity won't let me run.

**Dave Jones:** It says there's no license for the signal integrity. So, there you go. This is a bit plain jane, but that works. It's much quicker than the PCB. Um, of course, because PCB's got to draw, you know, solid polygons and everything else for the ground paws.

**Dave Jones:** I did check it is not being slowed down by my um uh screen capture uh program. So yeah, it it is a bit slow even on my machine which is pretty darn good.

**Dave Jones:** So there is the you know you got your standard sheet stuff. Still haven't figured out how to go single uh oh yeah takes a while. It reminds me of old Protel for DOSs.

**Dave Jones:** It very much reminds me of that except it you couldn't see whole sizes on ProTel for DOSs, but it's kind of that's just what that refresh reminds me of.

**Dave Jones:** And look, I mean, we can have multiple boards in the one uh you know project. So this is the driver board we've got here. So I'm not sure what this thing's doing.

**Dave Jones:** Some sort of serial interface or something like that. Is this some sort of like motherboard or something like that? And then this is the serial main board. And they've got multiple ones of those in the same projects, but I'm not sure what's doing with um in terms of integrating, you know, it's it doesn't have to doesn't seem to have any uh ecam stuff where, you know, you can integrate

**Dave Jones:** them and fit together. Um it might, you know, you might be able to fit them together in the 3D view or something that like that. I got no idea where obviously this is just the first time I've used it and had a look at it.

**Dave Jones:** It's a complete fail here. I mean, check it out. like these pin numbers. These are all horizontal. These ones are horizontal as well on those pins. It should automatically reroute them to uh vertical if you know if you're going to do that.

**Dave Jones:** That's just that's just silly stuff. I mean, you know, it doesn't even put them in the center of the pad. Oh goodness. It's it's got the net names down here, but yeah, that's not that's not terrific.

**Dave Jones:** And when you highlight the package, um the net names disappear. So yeah, that's not the best thing. Uh yeah, look, they've got unique part number IDs. Very kind of, you know, kind of Alium like um so anyway, I'm not sure if this how popular this package is.

**Dave Jones:** Maybe it's the industry deacto standard in Japan. Who knows? But I'm dealing with another company who's not in Japan and they're using this and I'm trying to read the file.

**Dave Jones:** Unfortunately, I have tried to read in my file. They gave me a PCB file. And in this, as you can see here, it's expecting PCB file, the actual word.

**Dave Jones:** I've actually just gott um but even then I tried to rename it. It would it just sits there and spins its wheels forever and I have to shut down the software.

**Dave Jones:** So it's maybe it's not a it's obviously not a compatible file or whatever. So maybe it's in an older version, a different version, not the root version. Um that could be the problem.

**Dave Jones:** Routting is always a problem. What else can we do in here with the route stuff? Uh, we saw the une before analog. Oh, teardrops. Teardrops. F11 is the hotkey.

**Dave Jones:** So, can we just go in there, select that, and go F11, please? A teardrop. Except what? What are the default values? Look at that. Bobby Dazzler got ourselves a teardrop.

**Dave Jones:** Ah, it brings a tear to the eye. And it's got parallel routing modes, but you know, these aren't I don't think you can just drag them and select and drag and things like that in terms of like uh you know, buses and all sorts of stuff.

**Dave Jones:** You can spread them. Um spread action. Love it. Spread all. No. What about placing a new part? That looks like a part symbol up there. And get part. Yep, that's the right one.

**Dave Jones:** But, uh, there's just like nothing there. Looks like all the libraries, if it does come with libraries, it's not installed. It's like a 300meg, um, install. It's not huge.

**Dave Jones:** Don't know what extend is. No, no. Unmount. No, no, no. Nothing installed in evaluation mode by default. Complete fail. And granted, Alium's not a huge amount better. Go in here and double click on a part and open it up.

**Dave Jones:** Um 74 ALS 574 classic and the pins. We can just go in there and have a fiddle. No wuckers. That's the uh preview. So maybe we'd have to No, you can't even like can't reorder, can we?

**Dave Jones:** No. No. But we can go in there and change them. Live simulation unknown model file. You can insert the model file directly here. So that would go into the uh simulator.

**Dave Jones:** That's pretty good. Analog to digital bridge. H VHDL. Oo. Wow. VHDL integration. Really? H. That's interesting. Didn't expect that one. So, what you can do is you can just highlight tracks here and delete them.

**Dave Jones:** It's exactly Oh, it deleted the via. Oh, there you go. You can connected stuff. I'm sure you can change that. This one still had a connected. And then if we go up here, we've got manual route.

**Dave Jones:** Let's give that a burl. It's like, well, it's not snapping to anything. I like it when it snaps and highlights, but presumably we can just select that. Oh, yeah.

**Dave Jones:** There we go. Snaps to center. Beautiful. It dims everything else and shows the uh net that we go into. Fantastic. A Bobby Dazzler. So, if I go like that, like that, we're done.

**Dave Jones:** And it automatically goes out. It's completed that net. It knows. So, it's reasonably reasonably uh intelligent manual routing there. I'm sure I can do more advanced stuff. And it's uh got itself a Gerber viewer, too.

**Dave Jones:** So, I don't mind uh that at all. That seems to work uh fairly well. I've got multiple layers uh selected here. So, this is going to be good enough for my purpose.

**Dave Jones:** I've got the Gerber files as well, or you could use any other Gerber uh viewer, Alium, or whatever uh one you want to use. So, yeah. Now, unfortunately, my PCB file that I want to inspect doesn't work, but uh yeah, I'll still be able to uh do the job with the Gerbers, but yeah, nice little Gerber viewer.

**Dave Jones:** That's a separate uh program. It just loads up. It doesn't didn't ask me for a license evaluation or anything like that, so maybe that's a freebie. And here you go.

**Dave Jones:** I found all the uh library files, 3D library files in there. So, there we go. There's all your different packages. Not a massive amount, but yeah, it's got some.

**Dave Jones:** No, that wasn't uh Delelfy that I was thinking of before. It was uh Visual Basic, like an old Maybe it's an old version of Visual Basic or something. Um, and it's got a V-basic subdirectory in here.

**Dave Jones:** So, there you go. That makes sense. And also, when I installed this, it asked me if I wanted to install uh Microsoft.NET Framework 1.1. So, I'm not sure what the current version is, but yeah, it um seemed ancient and it wanted me to install it.

**Dave Jones:** So, I installed it and it just all worked. So, that was pretty seamless. And they've got some hilariously old examples in here. Oh, look at this nice rounded corners so the electrons don't fly off.

**Dave Jones:** Beautiful. 2006 for these evaluation uh samples in here. Education PCB sample CSI EDA EDA solution. Yes, we want to run that. But yeah, this is it's pretty old and clunky, but uh you know it it's a reasonably powerful uh PCB package.

**Dave Jones:** So, you know, do the business. It's just a tool. Now we're talking. Look at this samples down there. Bluetooth demo. That's not 2006. So, let's uh There we go.

**Dave Jones:** Let's call up the uh 3D. Yeah, it keeps asking me do I wish to do that. Geez, that's not modeled very well. That's not a terrific example, is it?

**Dave Jones:** You got a couple of throughhole parts over here. Nothing else is rendered. You got your like your flash memory here. And that's about all she wrote. I mean, jeez.

**Dave Jones:** Yeah, they need to uh give better examples than that. Wow. Highspeed 8 bit risk base. What else have we got? There's a card reader. What's What's MP3? Oh, no.

**Dave Jones:** It's all pretty simple stuff, isn't it? Oh, that's 2005. Wow. Jeez, it's pretty old. SMC tests. There you go. Look at that. PLCC. Wow. But, you know, hey, that's that's a actually quite quite decent uh 3D mode.

**Dave Jones:** I don't mind that at all. But, you know, you'd have to go in there and see if you can um you know, you get your solder mask. Uh well, actually, yeah.

**Dave Jones:** No, hang on. Yeah, that is the No, that's the ground plane. Can you see the solder mask expansion? No, not by default, I don't think. Or is No, that's the ground.

**Dave Jones:** What's it trying to do? Oh no, I'm not entirely sure what the hell is wrong with that. Huh? What's wrong with that routing? Goodness gracious. Anyway, I've waffled on for far too long showing you this package which you'll never ever use and you'll never ever consider, I'm sure, CSIDA.

**Dave Jones:** But hey, the website, you know, it's still there and they're still, it looks like that they're still uh, you know, selling this thing and it's a global alliance. um you know and that's their main that's pretty much their the best CAD tool for circuit design and development.

**Dave Jones:** Um so you know I'm sure they got a nice loyal uh client base and everything else. It's just that you know hands up if you've ever used this in any way shape or form even like a previous version could have been bought out by this CSI Global Alliance.

**Dave Jones:** I don't know. I think I have heard of like wind PCB like you know a decade or two back or whatever it is. Um, and Electra route I think I may have heard of.

**Dave Jones:** Anyway, um, yeah, but it's a pretty obscure uh, type package. So, if you've had any experience with this, let us know in the comments down below how uh, prevalent is it.

**Dave Jones:** Um, I'm sure it's, you know, probably quite uh, it's got a good audience in Japan or whatever, but that price can't be right. Can't be. Surely it's an insane amount of money.

**Dave Jones:** Wow. written. Catch you next time.
