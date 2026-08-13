---
video_id: gHZ7wZYbuiI
title: EEVblog #299 - Retro Phone Camera Teardown
url: https://www.youtube.com/watch?v=gHZ7wZYbuiI
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 16, "2": 36, "3": 52, "4": 72, "5": 93, "6": 113, "7": 129, "8": 145, "9": 166, "10": 186, "11": 206, "12": 226, "13": 242, "14": 263, "15": 279, "16": 295, "17": 316, "18": 332, "19": 356, "20": 372, "21": 392, "22": 416, "23": 432, "24": 456, "25": 472, "26": 488, "27": 508, "28": 532, "29": 548, "30": 572, "31": 600, "32": 624, "33": 644, "34": 668, "35": 684, "36": 704, "37": 728, "38": 748, "39": 768, "40": 784, "41": 804, "42": 820}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. I promised this little teardown, and you saw it in the mail bag it was sent to me from someone from Sarajevo, and Vedran, I believe it was, from Sarajevo. That's his email address. Anyway, so thank you very much.

**Dave Jones:** It's a Siemens camera for an S55 Siemens mobile phone. And you know, I mean, you really do not see these things these days anymore. I mean, what vintage? You know, it's not that old in the scheme of things, but the pace of mobile phone

**Dave Jones:** technology has meant that something like this was obsolete before it even started. So let's crack it open, see what's inside. Now there's only one visible screw on this thing, which is on the end here, so let's see if we can take that out

**Dave Jones:** and maybe get inside this sucker. I might have to get my spudger out and... no, there we go, that's all it took. Oh, there was a second, looks like somebody else, looks like somebody's already taken it apart! So let's crack this sucker open.

**Dave Jones:** Maybe get the spudger in there, it helps. There's obviously a clip. I don't need this sucker working anymore. Never owned a Siemens mobile phone actually. Maybe they're big in Sarajevo, I don't know. Ta-da! Here we go! There it is. And the first thing you notice, of course, is this massive

**Dave Jones:** cap here, and what is that, I hear you ask? Well, it's obviously the charging cap for the flash, because these flashes, these bulb flashes require a very high amount of energy in a very short amount of time. Very high discharge current. So you get that from storing all the energy,

**Dave Jones:** and then charging it up in a cap like this, and then discharging it wham! Straight into the flash. And then that's why these things have a cycle time. They take a, you know, they might take anywhere from a second up to 10 seconds to actually recharge.

**Dave Jones:** And the main board is pretty simplistic, that looks like a linear technology logo there, I don't actually know what the part is. We've got SOT 23 device passives, and not much else in here at all. So we'll have to flip this over. Here's the lens,

**Dave Jones:** obviously for the CCD sensor, and we've got the viewfinder down here, which is just a crappy bit of that probably not even glass, probably just plastic. And the flash in there with the reflector. So we took off a couple of screws, and it looks like the whole

**Dave Jones:** kitten caboodle drops out. Hey, we've got some interesting stuff on the bottom here, clearly there's a second board down the bottom. What's our cap in there? It's a 33... no, 330... 330 volt 60 microfarads photo flash. It's specifically designed for photo flash applications.

**Dave Jones:** I'm just curious to see if there's any charge on that at all here, let's have a look. Nah, there's nothing. But if you were walking around with these things and you had already charged up that cap, that could be quite dangerous. So one way to do that is if you've got a meter like this and with a low Z

**Dave Jones:** setting, you know, that's only got a couple of K input impedance, you can actually use that to discharge a cap like that. I think there's quite a bit of electronic-y goodness in this thing, and it is quite an interesting sandwiched application. You can see the main Siemens phone connector

**Dave Jones:** here, and it's got ribbon cable going down to the bottom here as well as up to the top. So that's split between the two boards, and there seems to be several other things split between the two boards, so trying to wedge these together, and we've got some ribbon cable going from board to board here.

**Dave Jones:** And it's quite a little interesting engineering design exercise in trying to fit all this into, you know, a package like this. Of course modern mobile phones are, you know, extremely simplistic compared to this, but back then this was pretty much the only way

**Dave Jones:** to do it, and this might have been an innovative camera attachment for its time. Probably the first camera mobile phone. So this was the first time that they were able to, you know, actually do this thing. So they had to shrink a regular camera

**Dave Jones:** application down into, you know, with the photo flash and everything. When you've got a big photo flash, they use LEDs these days, but on modern mobile phones. But back then, you know, just a big the big cap in itself and the photo flash, and they decided to

**Dave Jones:** put in a tacky little viewfinder because that's what people were used to. But they, yeah, the engineers have done a really good job to sandwich this together. It's rather interesting. And the main processors in NEC are probably a custom chip D64100 F1. I have no idea if you have any info on that.

**Dave Jones:** Let me know. Some sort of image processor or something like that. ICS501M. Yeah, probably like a serial E2 PROM perhaps. Not sure. Got a crystal down there, and a couple of resistor packs around the place. A couple of 5-pin SOT23s, and not much else.

**Dave Jones:** And clearly some firmware in the device, and it's got the firmware number written on it. Now I took out three screws on the top here holding this top board in place, so hopefully it will, something will come apart. Yeah, I don't expect that to come apart

**Dave Jones:** come apart easily, because it's wedged together. There's our sensor. Ah, we've got our sensor on the bottom, directly on the bottom of the board. And, I don't know, it still can't seem to... looks like we're stuck with the Siemens connector on the end here.

**Dave Jones:** I might have to trim that off maybe. Yeah, so what I've done is just snip those two bottom bits down there, and ta-da! There's the CCD sensor! And there's another device on the bottom, probably a memory, when it's got some copper shielding tape over it.

**Dave Jones:** That's rather interesting. But look at, you know, the amount of work that they've put into all this custom plastic and, you know, they've all integrated it here with the cap. That's a, hey, you know, that's a fairly extensive system engineering, you know, enterprise there, and how they've strapped

**Dave Jones:** looks like they've sort of, maybe sort of, you know, and they've catered for the flash device there, and they've integrated the viewfinder into all that plastic and the lens and everything in there to line up with the hole in the board on the bottom and to sandwich

**Dave Jones:** that all together. It's, ah, it's a rather clever piece of three-dimensional system. Hey, just broke an inductor off there. Oops. Rather interesting bit of three-dimensional systems design there. I like it. It's brilliant. And this can be a really, one of the more difficult

**Dave Jones:** aspects of engineering actually, just packaging. The multidisciplines that you have to have to package something like this all together and, you know, and get it out in a reasonable time frame. You've got to have the mechanical experts, the plastic, you know, packaging experts.

**Dave Jones:** You've got to have marketing involved, of course, and, you know, and then the PCB layout guys and the designers and, you know, the circuit designers and everyone involved in this thing. You'd have, you know, the optics people involved in all that sort of stuff.

**Dave Jones:** So there's, you know, I wonder what sort of, what size team put this thing together. But, you know, it seems, you know, it's a fairly simplistic application in the end. But to put all that together is quite a bit of design work. My hat's off to them.

**Dave Jones:** It just goes to show that even the simplest everyday consumer items, like a little camera attachment for, you know, probably the first camera attachment for a mobile phone, just what, you know, there's quite a big design team that's put, you know, a year of their life, nine months or a year of their life into

**Dave Jones:** designing this thing. Let alone something, you know, hideously more complex like the old style, you know, camcorders or something like that, which are a massive, you know, amount of product engineering which goes into those. This is just, you know, what's involved in a simple camera.

**Dave Jones:** Hmm. Makes you think, doesn't it? I don't know who or what Scanhex is with a K. Maybe it's the subcontract design company who did it. I don't know. But it's the MB35S and it's Rev 1.0. And what do you know? I just looked up the Camerapedia on Google

**Dave Jones:** and Scanhex is a company which makes, yeah, digital imaging devices and cameras. They're a Taiwanese company founded in 1997. They work in the Silicon Valley area of Taiwan and they produced at one point in early 2000s 150,000 cameras a month. Go figure. And it looks like we have a date code here, the 16th week

**Dave Jones:** 2003. And this is probably the best zoom I'm going to be able to do on my video camera here, but that is the CCD sensor chip. The die there and it's, you know, it's directly exposed there's like a glass top on there that's, you know, there's

**Dave Jones:** well, I assume it's glass, yep. There's a glass top on there so it's not like I can penetrate that. So you know, that helps keep out dust and keeps it fairly robust during manufacture. So why they've got that copper tape over the, one of the memory devices there, I

**Dave Jones:** don't exactly know. It's shielding for something, maybe it's the photo flash discharge or something like that perhaps? I'm not entirely sure. So there you go, that's a teardown of one of the world's first mobile phone camera attachments for the Siemens S55. And of course there's no

**Dave Jones:** focusing mechanism or anything for this lens, it's just a fixed focus lens. You can see it's just glued in there, around there so that, you know, there's nothing fancy there at all, there's no zoom, just a fixed focus, you know, I don't know if

**Dave Jones:** it's even a glass lens, you know, it could be like a simple polycarb lens or something like that. I hope this comes out, I'm attempting to film handheld with my compact camera through the eyepiece of my times 80 Olympus SZ microscope here, and hopefully that's in focus and you can

**Dave Jones:** at least see the CCD, there's the CCD substrate itself, and the, all of the sensors, all of the pixel elements in there, and then the surrounding circuitry around the CCD sensor. So hopefully that's in focus, you can see the bond wires going off

**Dave Jones:** there as well, the bond wires go off to the PCB substrate which goes out to the, or I guess what you'd call the PCB substrate going off to the pins of the package. But there's some control circuitry inside there. It's rather neat, that's the highest magnification

**Dave Jones:** I've got here. And you'll notice that with my, I've got my times 2 Barlow lens under there, and my times 10 eyepieces and my times 4 zoom on here. So that gives a total zoom of 80 times, and you'll see the very small working distance I've actually

**Dave Jones:** got here. It's really, it's really tiny. The lens is up there a bit further from there, but you know, we're only talking about 25mm working distance or something like that under this microscope with that times 2 Barlow lens. So thank you very much

**Dave Jones:** Vedran from Sarajevo for sending that in. That was rather interesting. There's, you know, there's a lot more to it, but there's a, you know, I can't really tear down that sucker any further really. But, so it's only a really quick simple tear down, but lots of nice interesting system

**Dave Jones:** engineering going into that. And it's almost a shame for something that you know, really didn't have a long lifespan I don't think. These sort of things would have only lasted a year or two and then disappeared completely from the market until they were

**Dave Jones:** replaced with the, you know, like the CMOS camera sensors and the LED flashes and things like that inside your regular mobile phones as you know them today. Thank you.
