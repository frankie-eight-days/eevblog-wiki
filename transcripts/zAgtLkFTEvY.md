---
video_id: zAgtLkFTEvY
title: EEVblog #121 - gEDA Interview with DJ Delorie
url: https://www.youtube.com/watch?v=zAgtLkFTEvY
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 23, "3": 44, "4": 56, "5": 70, "6": 78, "7": 89, "8": 108, "9": 125, "10": 137, "11": 146, "12": 161, "13": 173, "14": 202, "15": 214, "16": 225, "17": 236, "18": 246, "19": 262, "20": 278, "21": 290, "22": 307, "23": 314, "24": 323, "25": 336, "26": 349, "27": 357, "28": 367, "29": 378, "30": 390, "31": 403, "32": 415, "33": 428, "34": 438, "35": 448, "36": 465, "37": 480, "38": 491, "39": 502, "40": 508, "41": 520, "42": 528, "43": 535, "44": 544, "45": 560, "46": 580, "47": 589, "48": 602, "49": 609, "50": 617, "51": 628, "52": 645, "53": 662, "54": 677, "55": 687, "56": 702}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. I'm here with DJ Delorie. Thanks for joining us, DJ.

**Dave Jones:** Welcome. Glad to be here. Excellent. Tell us about who you are and what you do. All right, my name is DJ Delorie. I'm an employee of Red Hat systems doing cross compilers, but as a hobby, I also like to do electronics.

**Dave Jones:** I've been playing with Renesas parts for a long time. Uh, I'm one of the lead contributors to the gEDA suite of EDA tools, and I participate in a lot of the forums and helping people out doing their electronics with Renesas parts or with our EDA tools or GCC questions, cross compilers, etc., etc., etc.

**Dave Jones:** So, what uh part of gEDA do you actually work on? The part that I work on primarily is the PC board layout editor. Uh, gEDA consists of schematic capture, layout, simulation, and a number of other utilities that work together.

**Dave Jones:** My part is primarily the the circuit board layout engine, the the core user interface, uh the the plugin system, the uh some of the trace optimizers and reporting and stuff like that.

**Dave Jones:** So, can you give us a bit of background history on gEDA? Where did it start? Where did it come from? What was the genesis? Who first worked on it?

**Dave Jones:** Each of the different parts of gEDA originated in separate people's projects. Uh, I'm not sure exactly when the schematic capture stuff started. Uh, Ales Hvezda did the first version of that because he wanted something.

**Dave Jones:** The circuit board layout editor started about 25 years ago on an Atari. Awesome. And it has been ported forward to all of these new systems, working its way up through the Athena widgets and and the the Motif widgets, and finally to GTK, and then eventually we we took all of that stuff out.

**Dave Jones:** We put in what we call the HID interface, the human interaction layer, and we build the GUIs on top of that. But it's it's gone through many iterations, but there's still some stuff in the code where you can see that it originated decades ago.

**Dave Jones:** Um that there's that that that the coding methods that were used and some of the names that we are naming conventions that we would never use today because they're well-known names or are used for regular variables.

**Dave Jones:** Some of that still shows through, but we've been slowly been migrating the core code up to new code bases. We've been replacing the auto routers with new technology as that comes around.

**Dave Jones:** We've been adding new user interfaces. There there's two two that we support officially plus batch plus there's I think two or three other projects to add other native interfaces to it using other widget sets.

**Dave Jones:** In addition, we use the the same interface that we use for the user interface also does all of our postscript exports, the Gerber exports, bill of materials, and somebody's actually putting in a scripting engine as an exporter.

**Dave Jones:** So we we we've been working to modernize the interface and to allow us to grow even further. Uh but but many many years ago, my first encounter with it um a long progression of events starting with a broken air conditioner resulted in me looking for a schematic capture and design package for a replacement board for my furnace.

**Dave Jones:** All right. And I originally tried Eagle. And the first component I placed had the wrong footprint. And and the board that it would allow me to do was not quite big enough to fit in the space that I had to do.

**Dave Jones:** So I started looking around again and I found gEDA. And I found its layout engine. And I started working with it and playing with it. And of course, it didn't quite do what I wanted.

**Dave Jones:** So I changed it so that it did do what I wanted. And I really didn't feel like routing all those traces manual, so I went out again and I found a an open source routing engine from Manchester University in England.

**Dave Jones:** And I made the two of them work together, so you could do your layout, Yeah. push a button, and have it auto routed and brought back in. And that was the first auto router that PCB supported.

**Dave Jones:** And I think now we're on number three. Excellent. We we replaced that router with a gridless router at one point, and as part of the Google Summer of Code, we sponsored a PhD candidate to add a topological router to the code.

**Dave Jones:** So, no longer are we required to have straight lines when we're doing our auto router. We can route curves that snake around and fit into things. He's even doing some some fantastic work with trace impedance matching, length matching as part of the auto router.

**Dave Jones:** Um the pictures are very pretty. I haven't actually seen it work on my boards yet. And you've got photo realistic uh image Yeah, that was another case of somebody wanted to do something for themselves.

**Dave Jones:** Uh we have we export Gerbers, of course, because everybody needs Gerbers. And one of our users, his name was Ben, took the Gerbers as layers in and fiddled with the colors and the stacking and the transparencies in order to get something that basically looked like a circuit board.

**Dave Jones:** And and so many people thought that was a great idea that we ended up incorporating that code into the exporter. So, our our image exporter has a checkbox for photo realistic.

**Dave Jones:** It was originally called Ben mode. Right. After the guy who Because he was the one to put the whole thing together. So, there's a little checkbox called Ben mode, and eventually we renamed it to to photo mode.

**Dave Jones:** So, we can export photo realistic images. And in fact, for my lab today, I had to have a picture of the board they were going to be using, but I had not gotten the board back yet.

**Dave Jones:** Yep. So, I took the photo realistic export from the package, Mhm. and I took a picture of my prototype that was made in my basement with, you know, lots of wires all over the place.

**Dave Jones:** I took both of those pictures and I scaled them to be the same size and gave them there. And I very carefully traced around all of the components. you moved each component.

**Dave Jones:** And I Well, no. I made them the same size. Yep. So, when I cut out the parts of the board, the other board showed through and everything was in the right spot, including all those little deviations in position.

**Dave Jones:** I moved a few of them that were way off and then redid a few things. And it looked real. We have so many people that look at these pictures and say, "Oh, you've got boards." No.

**Dave Jones:** Well, where did the picture come from? Well, the CAD package spits them out that way. And of course, the next question is, "Where do you get that package?" Are you looking at introducing 3D component modeling?

**Dave Jones:** We have a couple of 3D initiatives that we're working on. We do have an option to use the 3D renderer to produce translucent Right. layers, which is very complicated to do or very CPU intensive to do and the GPU can do it better.

**Dave Jones:** We have one experimental version that allows you to take your board and rotate it so that you can see the stacking orders and the vertical spacing, but we have not quite gotten to the point where we can model the components themselves.

**Dave Jones:** The other free software EDA package, KiCad, does have 3D modeling so that you can see all of that and we are interested in adding it, but it's just a matter of finding somebody who's interested in doing it and willing to put the time in.

**Dave Jones:** What's the difference between KiCad and and Jada? And they're both open source? They're both open source. They both perform basically the same functions. I think it's more a matter of which one is more comfortable for use.

**Dave Jones:** A lot of people who are new to the packages find that KiCad is easier to use because it's more integrated and it's more like Eagle and it's more of a Yeah.

**Dave Jones:** I hate hesitate to say it's for beginners because it's still just as powerful, but it's more keyed towards usability. They They use a cross-platform toolkit that makes it a little more consistent and everything is integrated together, whereas Jada, each of the pieces is a separate application, so you don't have to use them together the way that we want you to.

**Dave Jones:** You can spread them out. You can use our schematic capture with somebody else's PCB layout. Okay. Or you can go to simulation, or you can put I like to put huge amounts of scripts between one and the other in order to help me design repetitive circuits and things like that.

**Dave Jones:** So, we we like to think of gEDA as more of a power user approach. Is there any future in actually blending these two together cuz they're both open source?

**Dave Jones:** All the development We've talked with them. What we'd like to do is put together a set of converters that convert back and forth between the the file format so that you can pick and choose and go back and forth, share libraries and stuff like that.

**Dave Jones:** In the free software world, it tends to be, "Well, I want to do it my way." "Well, I want to do it my way." And then they do. Yeah.

**Dave Jones:** But we we really would like to be able to script And of course, since they're both open source, there's no reason why we can't do it. Again, time. Someone could come along and go, "I like the best features of both." And do a fork of that.

**Dave Jones:** Oh, easily. And there've been forks of PCB before as well. Where somebody decided they wanted a different user interface and they go off and they do their own thing.

**Dave Jones:** Yeah. What uh user base have you got at the moment for gEDA? Do you have any stats on that? I don't have any statistics because people don't have to tell us.

**Dave Jones:** We don't have Since it's there's no license, we don't know how many copies we've sold. Um I do know there have been a number of interesting projects and it's starting to filter into other things.

**Dave Jones:** The most interesting project built with gEDA is currently a couple million miles away on its way out of the solar system. On which probe? It uh not one of the ones that anybody knows, but there have been some small probes that have been sent up by universities and in research groups.

**Dave Jones:** Fantastic. are built with gEDA. I I know there's some experiments in the UK where they're putting gEDA stuff into spacecraft. Right. How many developers are there on gEDA? Um it depends upon what you consider developer because there's kind of a really There's always a gray area between between developers and users.

**Dave Jones:** Yeah. And we really only have one mailing list for both. We have We have an internal one for for the core developers. There's oh, probably only a handful of real core developers.

**Dave Jones:** On the PCB side, uh mostly it's me. Yeah. And there's a couple of other people that have their pieces that work on it. And we have a few other core developers who you know, we just kind of take turns, you know, paying attention.

**Dave Jones:** You know, life comes by. When it When it's a hobby thing, if something happens, you know, uh we lost one developer because his wife had a baby. Yeah. Oh, well.

**Dave Jones:** It happens. But if you include all of the other participants who add their bits and pieces, we try to encourage people to add things on the fringe, plugins and whatnot.

**Dave Jones:** Easily done as a side But they range from somebody who's written five lines of code all the way up to people who have written like that student who wrote the topological auto router.

**Dave Jones:** Do Do you see gEDA being involved with the open source hardware, the new open source hardware standard? We're trying to promote the idea that if you're making open hardware, it's not really open if the tools you need are not themselves open.

**Dave Jones:** Very true. KiCad, gEDA, you know, we kind of don't really mind which one you use as long as you use something. But if you use a proprietary package like Eagle or OrCAD or Altium to produce a design, is the design really open?

**Dave Jones:** Granted, you can use it Mhm. for whatever you want. But you can't change it unless you have buy the tools. So, we're trying to encourage the open hardware specs, the initiatives, to specify that open hardware is not truly open unless the file formats are open as well.

**Dave Jones:** Maybe it it at least if you can interpret the files and do something with the files as opposed to having a completely closed file system. We'd like them to use open source EDA tools.

**Dave Jones:** But But the very least, you need to be able to work with the EDA pods. And how much does Jeda cost? Jeda costs nothing. Completely free? Maybe a penny if you have to pay for your ISP.

**Dave Jones:** How do you make your money? Volume.
