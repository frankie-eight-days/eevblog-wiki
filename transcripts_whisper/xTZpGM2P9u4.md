---
video_id: xTZpGM2P9u4
title: MCAD Shootout! - Rhino vs Solidworks vs OnShape
url: https://www.youtube.com/watch?v=xTZpGM2P9u4
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 25, "2": 39, "3": 57, "4": 73, "5": 90, "6": 107, "7": 127, "8": 147, "9": 166, "10": 184, "11": 203, "12": 217, "13": 235, "14": 256, "15": 279, "16": 298, "17": 319, "18": 340, "19": 359, "20": 378, "21": 395, "22": 419, "23": 441, "24": 459, "25": 480, "26": 495, "27": 513, "28": 531, "29": 549, "30": 564, "31": 585, "32": 606, "33": 627, "34": 642, "35": 657, "36": 678, "37": 693, "38": 711, "39": 729, "40": 750}
---

**Dave Jones:** Hello everyone. So, today we're going to be looking at a few different mechanical design tools. The surface modelling tool Rhino, the mechanical design tool SolidWorks and the free mechanical browser-based CAD package called Onshape. And the first test I'm going to be doing is modelling some electronics components because, well, EEVblog.

**Dave Jones:** The upcoming tests are designed to stress these packages and they're quite diverse tests, each thing kind of targeting a different problem that a lot of CAD packages have. And by no means am I using even close to the full feature set of any of these tools.

**Dave Jones:** Onshape and SolidWorks both have great parametric design facilities and Rhino has all kinds of advanced surface modelling tools. And SolidWorks and Rhino have excellent renderers and SolidWorks has an excellent simulator and all kinds of things that I'm not even close to fully utilising.

**Dave Jones:** The next test is of modelling a Wirth transformer. This thing doesn't have all the data in the data sheet, so I had to wing it for some of it. But I thought this made a good test to compare the 3D modelling capabilities with respect to electronics components.

**Dave Jones:** Alright, so the first test being modelling a Wirth transformer. You'll notice that the Rhino package really flies out of the gate here. It has no real need to set up constraints, so you're not slowed down by the process of thinking how to constrain all the geometry,

**Dave Jones:** you can kind of just go ahead and do it. The constraints in Onshape and SolidWorks are actually quite similar and while it slows down the modelling process, it makes the model much more versatile and flexible. If I were to change, for example, the fillet radius in Onshape or SolidWorks,

**Dave Jones:** it would be a totally trivial thing. But if I were to do that in Rhino, I would have to basically delete the existing fillets and then redraw a whole bunch of stuff, and it would really be a pain. So you really need to know what you're doing in Rhino before you start.

**Dave Jones:** So, Rhino here, I'm already drawing the pins as I am in SolidWorks, but Onshape has barely gotten the base plate done. SolidWorks here, the sketch editor has some trouble with the constraints, so that's what I'm trying to do in the SolidWorks window to the bottom left,

**Dave Jones:** and I'm really having some trouble. I actually leave it unconstrained because it was just making the test irrelevant because it was taking so long to fully constrain the drawing. That means that all the geometry has formulated positions. So Rhino's actually finished at this point, and SolidWorks and Onshape

**Dave Jones:** haven't even got the pins finished, and Onshape hasn't even got the single pin profile finished. So really, Rhino did quite excellently here. SolidWorks is basically finished at this point. All the pins are set up in an array, and I'm just setting up the materials

**Dave Jones:** so that it appears like a transformer. Probably should have picked a different color than that copper. Onshape doesn't actually have a material properties thing. Well, it kind of does, but it doesn't set up textures or anything like that. And you'll notice that despite all the problems in Onshape,

**Dave Jones:** it only finished a minute after SolidWorks. Not bad at all. So here we have a modeling of wire toy. A wire toy is that thing that goes beep when you hit the ring on the wire. So this can be quite a challenging problem for tools

**Dave Jones:** when you have the profile of the wire turned from a circle to a square because it has to perform an operation called a loft along that curve while the curve moves in three axes. So it's not at all clear whether that curve should rotate around the curve

**Dave Jones:** or how to solve it at all. It's actually got many solutions. So a lot of these packages have a lot of trouble solving this problem. Now Rhino and SolidWorks here really have no problem setting up the drawings or the planes. SolidWorks is a 3D modeling package which with ease

**Dave Jones:** you can set up planes at various angles with respect to each other. SolidWorks is about the same. You can just rotate things arbitrarily around arbitrary axes. OnShape on the other hand, setting up planes can be a real pain and you'll see later on that this really is why OnShape loses so badly in this test.

**Dave Jones:** So Rhino already has the curve set up now. A nice spline curve is what it's called. And I'm already performing the loft operation in Rhino and it's basically done at this point. SolidWorks is very, very close behind. So it's also basically done, only it's a surface at this point

**Dave Jones:** and I just have to fill it in. Only a little under a minute between them. OnShape on the other hand, I haven't even done the profile to set up my 3D curve. OnShape doesn't really have the ability to do the same type of 3D curve that SolidWorks does

**Dave Jones:** so it is somewhat more difficult. The 3D curve it does have, it does allow for splines and stuff in 3D so that's good, that allowed this problem to be solved but it's nowhere near as sophisticated as SolidWorks' 3D tool or Rhino's unconstrained drawings.

**Dave Jones:** I'm still setting up planes at this point. I've got to set up the angle between the planes and then I've got to offset the angle from the previous plane and that's how much it takes to set up the drawing planes in this. It's really quite a pain.

**Dave Jones:** So at this point I've actually got the curve set up and I'm just doing that final spline curve which will hopefully end this modeling exercise. What I was trying to do there was make it so that the start and end were kind of normal to the surface at the bottom

**Dave Jones:** but it really just wouldn't do it so I gave up. OnShape is the only tool that produced such a hopeless curve by default. You had to fiddle with the settings quite a lot and even despite the time it took it still was around double the time for Rhino

**Dave Jones:** and that's really not very performant in this test. Alright, so this is going to be modeling a kettle thing but it's designed to show a major problem that I've bumped into every other day with Rhino when I'm doing fillet operations. I have also had a similar issue with SolidWorks

**Dave Jones:** and with OnShape in different scenarios but I found SolidWorks has the most robust fillet system of the three. Here you're going to see Rhino really, really sucking. Here I'm creating the base plate. This is an 80mm cylinder and in SolidWorks I'm just showing off the constraints

**Dave Jones:** where you can make one dimension relative to another and it's actually really cool but it did slow down the result of the SolidWorks kettle thing here. In Rhino I'm already doing the loft but that's going to be about the end of Rhino being ahead.

**Dave Jones:** OnShape is really, really close behind. In fact, OnShape is seconds from finishing. It is done at this point. All I'm going to do is set the material and it's done. Three minutes, 44 seconds. Both SolidWorks and Rhino have barely started. Usually you're fighting with the tool

**Dave Jones:** and usually I'm fighting with OnShape but OnShape really had no problems with this exercise at all. In Rhino here I'm having to manually do the fillet. I'm having to trim the surfaces with respect to each other because if you do a fillet operation on two surfaces

**Dave Jones:** or on a solid in Rhino it will not work if the fillet crosses over multiple surfaces. It doesn't do the trimming properly. In SolidWorks I'm just about done. I'm doing the fillet using its really nice fillet engine. There you go, last fillet there

**Dave Jones:** I'm going to do an operation called Shell which makes it hollow. SolidWorks just finishing up now with 6 minutes 55 seconds. Really great. Rhino, I'm still manually doing what looks like the simplest fillet on this whole damn thing except for the external fillet.

**Dave Jones:** What I'm going to do is blend between these surfaces. That basically means smoothly moving between them, that's what you've got here. It might result in the best looking fillet. I think Rhino has produced the best looking geometry here. Wow, it was a lot more work.

**Dave Jones:** This test wasn't the first time I tried this. I tried all kinds of things. If you know a good way to do it, put it in the comments. I found this to be a real pain. What I'm doing here is basically creating the shell.

**Dave Jones:** I didn't use a shell command this time because it failed too often. It failed worse than this offset operation. Even the offset operation failed. It didn't create a solid, it left gaps in it so I had to manually fill them up. Onshape finished here a third of the time of Rhino

**Dave Jones:** and half the time of SolidWorks. Really quite impressive for a free online browser based tool. Why am I comparing all these apples and oranges? It's because I'm really just showcasing how different the tools are. Rhino is an excellent surface modelling tool. It's great for architecture and industrial design.

**Dave Jones:** SolidWorks is excellent for mechanical design and industrial design as well. Onshape is fabulous for the hobbyist. It's free, albeit you have to have publicly listed models. The tool is free, which is really wonderful considering its capabilities are similar to the other two. If I were to recommend something to an electronics engineer

**Dave Jones:** I'd probably say Onshape if all you're doing is electronics component modelling for PCBs. It's free, why spend a whole bunch of money on something that isn't a whole bunch faster, it'll only save you a few minutes. But if you're doing something like industrial design

**Dave Jones:** the answer's a little bit more fuzzy. SolidWorks or Rhino will probably serve you really well. If you're an architect, people tend to not use SolidWorks for architecture as far as I know, so probably Rhino. But I don't see why SolidWorks couldn't do it.

**Dave Jones:** But it definitely doesn't have facilities designed for architects whereas Rhino does. So we are clearly the winners in this. A great variety of tools available to us. And the hobbyist community through Onshape, really a winner. FreeCAD almost made it to this video but it wasn't really ready for some of these tests.

**Dave Jones:** The workflow in FreeCAD is very different to the other two which made a video comparing the tool to the others very difficult. So as an example of a model you can produce in Rhino this is a CNC machine I designed about 7 years ago.

**Dave Jones:** It's based on galvanised steel and NEMA 23 stepper motors and I still use the machine today. And this is the kind of thing you can use Rhino for a little hobbyist project. And here is a 3D printer I designed in SolidWorks. It's parametric so you can change one number

**Dave Jones:** and it changes the size of a whole bunch of different parts. And SolidWorks made this rendering as well. We also have this assembly here a flippy dot assembly done in Onshape. This was just a little hobby thing and I've kind of just created some photos to make an animation for you.

**Dave Jones:** Everyone loves flippy dots right? So if you wanted other tools compared and I already realise people are going to nag me to do all kinds of tools I'm opening the floodgates here but leave it in the comments below if you get enough thumbs up maybe we can do a video

**Dave Jones:** comparing the tools that you talk about in the comments. I hope you liked the video. Have a great day. Bye.
