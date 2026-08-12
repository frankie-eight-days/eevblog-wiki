---
video_id: gKKWUZeyAac
title: EEVblog #586 - Open Source Hardware uARM 4-Axis Desktop Robotic Arm Kickstarter
url: https://www.youtube.com/watch?v=gKKWUZeyAac
source: youtube-asr
timestamps: {"0": 1, "1": 13, "2": 22, "3": 34, "4": 46, "5": 61, "6": 75, "7": 87, "8": 99, "9": 111, "10": 124, "11": 137, "12": 146, "13": 159, "14": 171, "15": 189, "16": 198, "17": 206, "18": 218, "19": 226, "20": 236, "21": 248, "22": 269, "23": 281, "24": 297, "25": 308, "26": 325, "27": 334, "28": 345, "29": 358, "30": 374, "31": 383, "32": 393, "33": 406, "34": 419, "35": 432, "36": 441, "37": 461, "38": 476, "39": 484, "40": 494, "41": 509, "42": 525, "43": 539, "44": 550, "45": 562, "46": 574, "47": 595, "48": 605, "49": 617, "50": 636, "51": 646, "52": 656, "53": 678, "54": 694, "55": 708, "56": 722, "57": 747, "58": 758, "59": 769, "60": 784, "61": 798, "62": 818, "63": 845, "64": 855}
---

**Dave Jones:** Hi, we're going to take a quick look at the UFactory uArm 4-axis robotic arm. It's a Kickstarter project and you have seen this on my mailbag segment before. I have shown it briefly.

**Dave Jones:** We'll take a little bit more look at it, but it'll be very brief. I've got to upload this today actually because the Kickstarter project ends in 3 days time.

**Dave Jones:** So, if you want to get one of these little robotic arms, you better get in real quick. So, let's take a look at it. Now, it's designed by a group of hardware guys in China.

**Dave Jones:** So, will be designed and produced in China. And it is, as I said, a 4-axis robot. So, what the 4-axis robotic arm. So, what that means it can move in that axis like that.

**Dave Jones:** It can also move around like that. It goes to the end stop there and there. So, it can almost do a full 180° there. And it can raise up and down like that as well.

**Dave Jones:** Sorry, the suction cups aren't really sticking to my antistatic mat here at the moment. And so, that's three. And also, the head can rotate around like that. So, and this one is fitted with a suction cup on it.

**Dave Jones:** And there's the suction pump on the back there. So, it can lift items up and move around. So, it actually has quite a large operating range of movement. I rather like that.

**Dave Jones:** And on the Kickstarter page, they do actually have a three-dimensional you know, envelope three-dimensional operating envelope of how it works over. So, in that aspect, it's not bad at all.

**Dave Jones:** Now, it actually comes as a do-it-yourself kit. My one came fully assembled. So, I can't vouch for being, you know, the kit itself and how easy it is to assemble, but I presume it's not that hard.

**Dave Jones:** It comes with all the screws and bolts and everything else. And just the individual pieces in this case made out of black acrylic like this, but it comes you can order two versions either a wood version laser cut wood or laser cut acrylic like I've got here.

**Dave Jones:** And the basic kit for this thing is $185 US, but that doesn't come with the suction cup. That comes with a gripper attachment that can you know grip things like that.

**Dave Jones:** If you want the suction cup, I believe that's about $219 US for the kit. I'm not sure how that compares to other uh fully assembled or kit robot arms on the market.

**Dave Jones:** I guess I I'm not really familiar with the market at all, but I I think it it doesn't represent bad value at all. Now, as far as the stability of this thing goes, it's not going to be great cuz it's not you know solid metal.

**Dave Jones:** There is a bit of play in that. If I hold that down like that, I mean you know there is a little bit of jiggle in that. You're not going to be able to use this thing as a fully repeatable pick and place machine down to millimeter or so.

**Dave Jones:** You might get maybe millimeter of millimeters repeatable accuracy or something like that. Haven't actually tried it because I don't have the firmware to enable well, I don't have the software to enable you know just accurate point-to-point repeatability tests and things like that.

**Dave Jones:** But yeah, like you're you're not going to be able to get sub-millimeter accuracy on this thing. So, you can forget about maybe you know using it as a homemade pick and place machine or something like that.

**Dave Jones:** But it's going to be good to a few millimeters at at least. So, it's going to be usable for something. That's for sure. If anything, hey, it's a fun toy.

**Dave Jones:** If we have a look in there, you can see the DC servo motor for the head that allows it to rotate around like that and the suction cup on the bottom.

**Dave Jones:** As I mentioned, you can't actually get different gripper you can get a gripper attachment and other attachments for this thing or you can make your own. That's the whole idea.

**Dave Jones:** Oh, and of course the big thing about this of course that it is fully open source uh So, all of the hardware designs will be available for download presumably when it's finished.

**Dave Jones:** I'm not sure if they're available yet. And also all the soft software, the algorithms, and the code to actually drive this thing will all be open source. So, you can do anything you want with it.

**Dave Jones:** Fantastic. And for those who are familiar with their DC servo motors, this one's got 1501 on it, power something brand. I'm not entirely sure what. But, of course, that is one of the main limitations of this thing is that it only uses DC servo motors, not repeatable stepper motors.

**Dave Jones:** But, they say, "Hey, they might release a stepper motor version in the future." But, at the moment, yeah, the biggest limitation here are these DC servo motors. But, it still makes a useful robot.

**Dave Jones:** So, you can see that this DC servo motor here just controls that lever arm there up and down, which then moves without having this main arm move here, actually changes the pivot point for that arm right up there at the pivot point.

**Dave Jones:** So, this is a rather clever design. I like it. It is supposedly modeled on one of like an ABB brand industrial robot or something like that. But, I think it's very loosely based.

**Dave Jones:** But, still it's a neat design. And of course, the neat thing about it is is that this head always stays vertical no matter where in the axis range you put it, it is always vertical by uh virtue of how they've designed the arms and the pivot points.

**Dave Jones:** But, you know, that's standard par for the course for these robots. But, if you don't get that right, hey, you've screwed something up. And as far as the wiring goes on this, I mean, my one came fully assembled.

**Dave Jones:** So, you can if you got the kit, you can assemble it any way you want. But, I've got just the cables, just the three-way ribbon cables to each DC servo motor.

**Dave Jones:** They're just sort of, you know, flapping around in the breeze there, but they are they aren't going to get caught on anything like that. So, it looks like, you know, it it's going to you don't really have to worry too much about that, but you could tidy up the cable management on your own final build.

**Dave Jones:** And there's the DC motor for the vacuum pump. That's a an optional mechanism, of course, if you go for the gripper attachment, you won't actually get this included in the package, so you would have that platform just free to mount anything you like on.

**Dave Jones:** And of course, there's another DC servo motor right in there which handles the rotation of the base platform here. And it does come come standard with these suction cups.

**Dave Jones:** And by the way, this build this was the very first one that they built and shipped. I was the first backer of this Kickstarter project, so I got the very first one.

**Dave Jones:** I believe they've made some design improvements in various areas since this one. So, don't take this one as an absolute finished product. And what they've got here is just a Arduino Uno compatible board.

**Dave Jones:** It's not a genuine Arduino one. And they've done the micro arm sorry, I'll call it the micro arm. It's actually U arm. And their company name is UFactory, as in U.

**Dave Jones:** It's your arm. It's your factory, I guess. And there's the open source hardware logo, brilliant. And they have since said that they've shown photos that they've redesigned this thing entirely.

**Dave Jones:** So, they've integrated this motor shield onto the main board down here. And that's a really good idea cuz when I first got this, I plugged it in. It comes with a 5-V power adapter with it.

**Dave Jones:** And of course, I plugged in the USB, and I plugged in my 5-V power into the Arduino board up here. And then the thing didn't work. And I had to email them and said, "Hey, it didn't work." And they sort of I guess they were giggling and said, "No, you've got to actually plug this into the shield down the bottom there." I didn't see that.

**Dave Jones:** It was tucked away. Another 5-V DC jack tucked away right down in the bottom down in there to power the motors. Well, enough talk. Let's plug this thing in and see what she does.

**Dave Jones:** Whoa, there we go. It zipped back to a home position, I guess. And here is their Kickstarter page and they've absolutely smashed their target. They're only going for a $5,000 goal.

**Dave Jones:** Got 3 days left. Sorry about the late notice of the video. I've been putting it off putting it off. I had other things doing, but they're up to $164,000.

**Dave Jones:** 856 backers. Fantastic. And here's their website over here. They do have some other products as well. They got like a balancing platform and other stuff like that. And uh you can download the software from this site and the software is very very simple.

**Dave Jones:** The only thing that they've got at the moment is a little mouse control program like this. And it really shows that this product is designed by a bunch of hard ware engineers because the software as it stands at the moment is the biggest let down of this thing by far.

**Dave Jones:** It It very primitive. It allows you to operate the thing with the mouse as we'll see, but it doesn't do anything else. I don't even have access to the to to the commands the serial commands to actually talk to this thing.

**Dave Jones:** Maybe it is on their website and I just haven't looked, but anyway, you have to install the Arduino software first all the Arduino drivers cuz it identifies itself as an Arduino Uno.

**Dave Jones:** So, you just install the Arduino software and then you just run this mouse control program. There's no install. It's just a simple XE. COM port 3 is what it's hooked up to.

**Dave Jones:** 9600 board and that's it. And you start it and Woohoo! This is all we got. This is all you get with it is this mouse control program. But what this mouse program allows me to do it is fairly intuitive.

**Dave Jones:** I can just use move my mouse forward, move it back, and left, right, and then up and down with the scrolly uh the scroll wheel on the thing, and it really is quite easy and intuitive just to play around with and operate this robot.

**Dave Jones:** Of course, this is just like a demo type thing. The real power with this thing comes when you can actually script it with serial commands, and they do apparently have some software that allows it to uh learn things.

**Dave Jones:** So, I can bring this down like this, and I press that, and suction, and I can lift up my little lens there. Oh, no, dropped it. There we go.

**Dave Jones:** It couldn't hold that couldn't hold that lens. It was before. Oh, no. Ah, fail. So, I'm trying to pick up this uh 100 g lens here, but the Yeah, it doesn't seem to be doing it.

**Dave Jones:** I'm not sure if it's just the uh surface isn't quite good enough for the uh suction cup. That could certainly be it. Okay, let's try that again. There we go.

**Dave Jones:** There we go. Yeah, it's just a matter of the surface. Ah, baba. But, it can certainly pick up Whoa, the suction cups. Can I get it to flip? Can I get it to flip?

**Dave Jones:** Will it flip? I don't know. Yay. Okay, so let's pick up a micro ruler. That should be real easy. It doesn't weigh anything. Only weighs a couple of grams, but uh it really is quite fun to uh quite fun to play with.

**Dave Jones:** If I I hold down the uh mouse uh hold down the right button, and then do the scroll wheel, I can get it to uh rotate that around. I don't I haven't figured out how to actually release the uh suction yet.

**Dave Jones:** Not entirely sure if you can. You probably can, but I haven't figured out how to do it. There you go. But, it does work. Ah, it's neat. It's actually quite a fun toy to play with.

**Dave Jones:** And as you can probably hear it just every couple of seconds it just redoes that suction cup. I'm not sure if you can disable that or whether or not that's part of the algorithm actually built into the Arduino itself that uses to control this.

**Dave Jones:** But, anyway, the Arduino controller in there has all of the reverse kinematic algorithms to what that basically means that this robot arm you can control using XY coordinates. So, you can say, you know, go to this point, go back, go back, and it handles all of the algorithms of how to actually figure out how to get there and step over to there and move and coordinate the arm to a given

**Dave Jones:** three-dimensional coordinate in space. But, as I said, I don't actually have the serial commands yet to actually, you know, program this to do anything. I've only got just the little mouse program just to muck around with it.

**Dave Jones:** But, even that's quite good. But, because it's all open source hardware and software, all that stuff will be released and you'll be able to play with it to your heart's content.

**Dave Jones:** Fantastic. So, there you go. That's a quick look at the Well, the very first UFactory uArm released. And if you want one of these little fun little toys, there are is, as I said, 3 days left in the Kickstarter campaign.

**Dave Jones:** And yeah, this is just so much fun. I have no idea what I'm going to use it for. I don't think I really have any real practical use for a four-axis robot arm on my bench here, a bench mount version.

**Dave Jones:** But, you know, I I don't know. Uses are limited by your imagination, I guess. It's an okay design like physically, but as it's implemented, the build quality is fine of it, but of course there are just you're always going to get the limitations based on the acrylic and build and all that sort of stuff and the DC servo motors.

**Dave Jones:** And of course the biggest thing with this sort of stuff is what software tools you get to actually control the thing. That is going to be the bigger kicker, no pun intended, but they do say that with the Kickstarter money they are going to hire real software programmers to work on developing various software apps and things like that, but really if you got the serial commands, that's all

**Dave Jones:** you need because you can, you know, write your own programs and your own control stuff to control your own little personal benchtop robot arm. Anyway, I hope you like that quick look at it.

**Dave Jones:** If you want to discuss it, jump on over to the EV blog forum and I will provide a link to the Kickstarter down below. Catch you next time.
