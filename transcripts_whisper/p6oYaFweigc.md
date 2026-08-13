---
video_id: p6oYaFweigc
title: EEVblog #734 - Giroptic 360cam Kickstarter Prototype
url: https://www.youtube.com/watch?v=p6oYaFweigc
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 25, "2": 41, "3": 57, "4": 73, "5": 85, "6": 105, "7": 121, "8": 137, "9": 149, "10": 165, "11": 185, "12": 201, "13": 217, "14": 237, "15": 257, "16": 273, "17": 289, "18": 301, "19": 325, "20": 341, "21": 353, "22": 369, "23": 385, "24": 405, "25": 425, "26": 441, "27": 457, "28": 470, "29": 490, "30": 510, "31": 530, "32": 550, "33": 576, "34": 593, "35": 609, "36": 625, "37": 641, "38": 657, "39": 669, "40": 682, "41": 702, "42": 718, "43": 734, "44": 751, "45": 767, "46": 787, "47": 803, "48": 816, "49": 836, "50": 852, "51": 872, "52": 888, "53": 905, "54": 929, "55": 950, "56": 966, "57": 986}
---

**Dave Jones:** Hi. Check out this thing. This is the 360 cam from a company called Gyroptic. And they started out as a Kickstarter project. They got $1.5 million or thereabouts to develop this really funky looking 360 degree camera. And this is one of the first early

**Dave Jones:** developer prototype units. It's definitely not the finished product, but Matt dropped by. He was one of the early backers and there's a reason for it, which you'll see in the next couple of months in an upcoming video, which I'm sure everyone will like.

**Dave Jones:** Anyway, there's a reason why I'm taking some 360 degree camera footage of the lab here. Anyway, yeah. I thought we'd just take a quick look at this early developer prototype. Doesn't look quite funky. We've got a metal base here. You'll notice all the heatsink

**Dave Jones:** fins on there. So they're trying to increase the surface area there. The thing does get quite warm when it actually runs, so they must be running this thing at like, you know, really full speed. Where, you know, guessing that there's either an FPGA in there

**Dave Jones:** or they're running like an ARM processor with Linux, but like a really fast one. Because the interesting thing about this, it's got three HD cameras on here. They're all, you know, at fixed angles like that with real wide angle fisheye lenses on them.

**Dave Jones:** That's why they can get full 360 degree coverage around here with only the three cameras. The interesting thing is they do all of the 360 degree video switch stitching in this thing. 30 frames per second in real time hardware. All that stitching. So it must

**Dave Jones:** they must even be doing that in some sort of FPGA or some sort of maybe some sort of GPU or something like that. Or maybe just a really fast Linux processor. Something like that, we're guessing. Anyway, or it could be, it may not be running OS like Linux, it could be

**Dave Jones:** completely proprietary. Anyway, this clips off here, here, and here like this. It's got a tripod mount on the bottom, which is not deep enough. We had to actually use a spacer to get that on a regular tripod. So that was a bit of a fail.

**Dave Jones:** We've got a micro USB here, which you can get the data out of or charge the thing. And it's got this rubber around the outside. In fact, well, we'll power it up in a minute because I'll show you something really funky, but yeah.

**Dave Jones:** There we go. Ta-da! We're in like Flynn. And unfortunately we can't see the electronics, but we do have some photos of the electronics. And here they are from the Kickstarter update page. So we can, you know, see a good lot of what's inside.

**Dave Jones:** This rubber material is actually semi-transparent, as you'll see in a minute with the display. And it looks like they've glued that onto the body there. And it looks like they've probably glued in this into the base of it. So yeah, sorry, but we're not going to

**Dave Jones:** destroy Matt's camera. It goes for about $500. How much did you pay for the developer unit, Matt? I think it was $12.99. $12.99? For two. Oh, for two. $12.99. For two. There we go. For two developer units. And you'll see why Matt needs one.

**Dave Jones:** In the next couple of months I'm going to go on-site and he's going to show us something really cool. Anyway, there is the battery. I'm not sure if that is like a standard size or whether they've developed their own one, but that's 1180

**Dave Jones:** milliamp hours. 4.37 watt-hours. Which is, you know, quite reasonable lithium-ion battery. I like the fact, one interesting design aspect of this thing is that they use this board-to-board interconnect on the bottom here, so presumably all this base gets really quite hot. So presumably

**Dave Jones:** all of the battery, at least the battery charging is in there, but because it even gets hot when it's just being used and not charged, presumably I would say like voltage regulation all done in here as well. Maybe for different rails for the CPUs and or FPGAs or whatever it is they're

**Dave Jones:** using inside this thing. So I think maybe all your power regulation's done in the bottom there. And the interesting thing about, and the reason I say that, is because you can get different attachments like this. You can get one that actually screw it like it has an Edison screw attachment, and it screws into your Edison

**Dave Jones:** screw light bulb socket on your roof. So you can just hang your camera from the roof. That's really quite funky. And it is designed to be waterproof, hence why they've got the rubber seal on there. It's not great. If you really want it to be properly waterproof, you've got to

**Dave Jones:** grease up that O-ring, of course. But it's probably good enough for the odd splash and things like that, I'm sure. And it's designed in France. There we go. Hi to all my French viewers, but made in the People's Republic of China. Why can't they make it in France?

**Dave Jones:** Come on, I'm sure you can. Anyway, a very early prototype by the way, the website is 360.tv. They've even got the QR code on there. And there's the battery terminals. Well actually, considering that the battery goes, actually I just thought, considering that the battery goes into there, maybe they don't have voltage regulation in the bottom.

**Dave Jones:** Hmm, I don't know. Because then you'd have to feed it through there, and then back through this connector, back into here, and then your voltage regulation goes out. Anyway, that's quite a lot of work. Anyway, that's quite a lot of pins on that board-to-board interconnect there.

**Dave Jones:** It really is quite nice, and you can get different attachments, different things to plug on the bottom. So I really like the design of this thing, it really is funky, it really is quite small. I mean, if you have a look at the

**Dave Jones:** size of that, I mean it just fits in my hand like that. It really is quite novel. So got an SD card down in there, and that's it. So as you can see, the clips, I haven't done up these two clips here yet, but interesting little clip arrangement.

**Dave Jones:** I'm not sure of the longevity of that, but probably seems okay. And that will, of course, compress it and help give a constant pressure around all sides on the O-ring, which is what you need. You need even pressure right around. So that's, you know, it's not a bad design at all.

**Dave Jones:** And by the way, it does these little holes here, microphones. It's got a spatial microphone array and spatial microphone technology. But unfortunately we have had no luck whatsoever with the audio on this thing. It is absolutely awful. So we don't know if we're doing something

**Dave Jones:** wrong, or there's something wrong with this development unit. Keep in mind, this is a complete development unit. We have shot some 360-degree footage of the lab. It just saves it to a regular MPEG-4 file. 2048 by 1024 resolution on the thing. 30 frames per second with just regular

**Dave Jones:** audio embedded in it. And you just take out that file, save it to MPEG-4 in here. You don't have to convert it on a PC or anything, you just upload that direct to YouTube, and YouTube recognizes that it's a wide format 360-degree video, and it treats it as such.

**Dave Jones:** And you can watch it and pan around side to side and up and down in full 360-degree. Although what they've done is they've watermarked, as you'll see, follow the link to go to the real footage here in the lab. They've actually watermarked, in the firmware here,

**Dave Jones:** they've watermarked the bottom of the image. So if you pan right down, so if you look, you know, right down like that, you can see that they've watermarked the bottom of the image saying this is a development prototype, it's not representative of the final quality, all that sort of jazz.

**Dave Jones:** So, anyway, it's got two buttons here. Yes, it does have Wi-Fi like this, and it's got a really funky display. Watch this. Come on, you can do it. Look at that! It's got these LEDs which show up. Now, here's a photo of the internal LED array.

**Dave Jones:** It's basically got an array of little tiny surface mount diodes on a flat flex, and that's how they're getting the display. And it's really quite funky, and it's got, you know, it scrolls and everything like that, and we can record video, like if I just press that now,

**Dave Jones:** it starts recording. There we go. And press it again, and that's the file name. There we go, it just wrote the MP4 file. And then we've got the various modes over here. We can take a photo, we can take a 360... no, it's waiting.

**Dave Jones:** Yeah. Oh goodness. But it's really funky. What's the bar graph at the bottom, Matt? That was the battery level. I thought it was. All right. We're waiting, waiting. It really is quite slow. And we have had it lock up. We have had an error when we tried to disable

**Dave Jones:** the gyro in it. It does have a gyro inside, and we... so there we go, and take a photo. So it counts down, and then it will ta-da! Take a photo. So we haven't tried burst, but yeah, multiple photos at once. And it's time lapse, time lapse photos, and that

**Dave Jones:** little thing is supposed to be a spanner that goes into your setup, and you can set up various parameters. You can turn the WiFi off and on, there'll be a LED behind that, the WiFi lights up and things like that. And we originally thought, oh, the WiFi might be causing interference with

**Dave Jones:** the microphone. It like drops out. But no, it seems to make no difference. So we're not sure what's going on with the audio. But yeah, check it out. I just thought I'd show you this development prototype. It's the first one. They were like four months behind schedule or something,

**Dave Jones:** actually delivering this thing. And we think they've shipped like just over 50 units to the early backers who wanted one an early development unit. So it's a little bit rough and ready. There's firmware issues. The audio, yeah, sucks. Unless we're doing something horribly wrong.

**Dave Jones:** And the video's, you know, quite pixelated. Go over and have a look at it, and you can see the EEVblog lab in 360 degree. But I just really like the concept. It really is quite nice. Packaged really well. I mean, you know, the

**Dave Jones:** envelope design that you have to get your electronics to fit in there, and it's no surprise it gets hot. You know, to do real-time video stitching at 30 frames per second is just, requires a whole bunch of grunny processing. So yeah, you know,

**Dave Jones:** if it does have an ARM processor doing that, it's probably running at, you know, 800 megahertz or you know, something like that. It must be really screaming along, or it could be using FPGA, as I said, or some sort of GPU chip. Unfortunately we don't

**Dave Jones:** have any internal photos. If anyone does have any more info on it, or maybe the developers can, if they're watching this, can leave it in the comments, maybe. And tell us, it's not open hardware, is it Matt? I don't believe so. Not open source?

**Dave Jones:** No, we don't think it's open source hardware, so it's, you know, just a regular commercial product. So it's been recording for almost 5 minutes now, as you can see. And let's get a look at the thermal profile of it. And sorry about the overhead lights and

**Dave Jones:** crap like that. But you can see that it is the bottom that really gets quite warm, even though it's not being charged. There we go, that top, it's actually that part of it that gets really hot. So the lower part of the bottom, so that's where

**Dave Jones:** all the processing is. So there you go, yeah, you can see where all the processing is happening, and all the voltage regulation, they're going to have some loss in there, your DC to DC converters aren't going to be, you know, they're only going to be 90% efficient tops.

**Dave Jones:** So yeah, there's lots of power in there, of course there's no you know, there's no airflow at all, there's no way they can do that, it's all passive radiator with the heatsink. But there you go, that's just a thermal look at the 360 cam after 6 minutes.

**Dave Jones:** It will warm up a bit more, but yeah, it's getting up to like 45 degrees or something so it's getting a little bit toasty in there right about now. It'll be warmer inside. Of course, I'm not sure if they like fill, I don't think they fill it with

**Dave Jones:** like a, you know, a gel or a thermal compound, like potted or anything like that to get the heat out. So who knows how they're getting the heat from the main processor in there, which would be the thing that's contributing most of the power dissipation in these things.

**Dave Jones:** And you can see some misalignment in the, like my thumb to the thermal image there, that's just the camera because I'm actually closer than the 30 centimetre distance there. But there you go, 45 degrees. So I'm not sure if the processor has got some, you know,

**Dave Jones:** heat spreader or heatsink on top to actually spread that power, whether or not they've flipped the processor, you know, is pressed on the other side like is in the bottom side of the board down here. That'd be how, if I was designing this thing, that's how I'd do it.

**Dave Jones:** I would put the processor on the bottom of the board and then put a thermal pad between it and the base of the unit. But yeah, the poor old battery is trapped in there of course, and but yeah, you can see because of the o-ring seal, there's not much heat that's getting

**Dave Jones:** from like the, where it's being generated through to the base of the unit like this. So yeah, it's just, it's, you know, it's helping of course, but it's not happening too much. It doesn't help that you've got all the plastic over the top of the thing either.

**Dave Jones:** So anyway, there you go, there's a quick thermal look at that. It's been running for 9 minutes now and a little bit warm, but eh, she'll be right. No worries. And I'm not sure if the battery gauge is linear or not, but yeah, after like 10 minutes of use, you saw where it was before,

**Dave Jones:** it had like bars up to here, and it's, yeah, it's really sucking the juice out of this thing, assuming that that's a linear bar graph. And what voltage they drop out at, I don't know, but I'm going to give them benefit of the doubt that they've got their battery management correct

**Dave Jones:** in that respect. But yeah, there's only a 4 watt hour battery, so I'm not sure what the quoted battery life of this thing is, if it's in the specs, I'll annotate on there. But yeah, it's really chewing the power. Hmm, but it's got to do a lot.

**Dave Jones:** I mean, 30 frames per second stitching from 3 HD cameras in real time, that's just, that's crazy. And this is connected to a charger now, and you can see that the processor hotspot is now up to 50 odd, and the bottom is now up to 45, so that's to be expected because you're generating

**Dave Jones:** heat in the bottom, that's going to radiate to the top as well, increasing that, the average temperature in the top half. So you can't shoot video while it's doing USB charging, but that's just another data point for you, about 50. We've only had it going for like a few minutes on the

**Dave Jones:** USB charger, 5 minutes. And here's their development kit box that they shipped it in, there we go! First batch, woohoo! And ta-da! It opens up and ta-da! Pulls out, beautiful. Bit of a wank there, but you know, that's a, how do you package something like that?

**Dave Jones:** There's got to be a fair bit of, you know, wasted space in your packaging, but that's nice foam packaging, really like that. It's really cute. So there you go, early development prototype, and they've implemented it quite nicely. It's just a, you know, it's got a lot of issues and needs some

**Dave Jones:** ironing out, but there you go. There's the Gyroptic 360 cam. Hope you liked it. Catch you next time.
