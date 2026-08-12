---
video_id: lmy8J8n9wPU
title: EEVblog #1315 - Ultrasound Probe Extreme Teardown!
url: https://www.youtube.com/watch?v=lmy8J8n9wPU
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 24, "3": 37, "4": 47, "5": 67, "6": 85, "7": 94, "8": 107, "9": 120, "10": 143, "11": 164, "12": 174, "13": 185, "14": 197, "15": 215, "16": 221, "17": 238, "18": 248, "19": 262, "20": 278, "21": 285, "22": 299, "23": 313, "24": 331, "25": 344, "26": 355, "27": 371, "28": 385, "29": 397, "30": 408, "31": 428, "32": 441, "33": 456, "34": 472, "35": 487, "36": 499, "37": 514, "38": 526, "39": 536, "40": 549, "41": 559, "42": 573, "43": 584, "44": 599, "45": 613, "46": 621, "47": 637, "48": 647, "49": 669, "50": 686, "51": 696, "52": 712, "53": 728, "54": 745, "55": 761, "56": 773, "57": 791, "58": 800, "59": 814, "60": 824, "61": 830, "62": 852, "63": 869, "64": 888, "65": 904, "66": 915, "67": 932, "68": 945, "69": 952, "70": 961, "71": 973, "72": 985, "73": 997, "74": 1010, "75": 1019, "76": 1034, "77": 1045, "78": 1060, "79": 1070, "80": 1082}
---

**Dave Jones:** Hi, this is a follow-up video to my previous one where I tore down a ATL/Philips ultrasound machine. And that was a pretty epic video, almost 50 minutes long. So, I'll link that in at the end of down below if you haven't seen it.

**Dave Jones:** But, I promised that I would take a look at one of these ultrasound probes. And well, let's try and tear this thing apart to see what makes one of these tick.

**Dave Jones:** Now, this is the this is a curved array. You can get actually the ultrasound that we looked at machine had a three different connectors on there. So, you can permanently connect up to three different ultrasound probes to that particular machine.

**Dave Jones:** So, that then you can switch them in software depending you didn't have to, you know, connect and unconnect the actual sensors like this. And by the way, the actual connectors are absolutely gorgeous.

**Dave Jones:** Look at that. It's just thing of beauty, joy forever. Anyway, really robust kind of, you know, industrial type connector that just latches that in place there. Beautiful. Anyway, this is one of the probes compatible with the HDI 3000 ultrasound.

**Dave Jones:** And it's the C52 curved array. This is Philips branded cuz Philips bought out ATL in the mid-90s. Now, this is the C5240R. Philips currently sell a C52 ultrasound probe that looks very similar to this.

**Dave Jones:** This is actually a curved array. That's why they call it a curved array cuz it's actually curved like that. And they do sell the exact basically the same model as this, but it doesn't have this connector.

**Dave Jones:** It comes with like a USB connector on it that plugs into like a newfangled tablet type device. Not sure if it's customized or whatever. So, that, you know, you can use them in the back of ambulances, in the field, wherever.

**Dave Jones:** You know, you can just you don't need to haul around this big 200 kg ultrasound machine. You can just plug in this little battery-powered tablet thing, hook it up to one of these curved array probes, and you can diagnose people on the spot.

**Dave Jones:** Now, this particular curved array here, the C52, it operates from 2 MHz to 5 MHz range, and it's got a 67° field of view. It can Well, the new one I got the spec that it can penetrate up to 30 cm depth, and this particular type of probe is actually used for abdominal diagnosis.

**Dave Jones:** You know, abdominal injuries, gallbladders, and lung injuries, and you know, things like that. So, if you're in the back of an ambulance and they want to, you know, think you've got an abdominal injury or something's wrong with your lungs or something like that, they might, you know, wax some of the ultrasound gel on this and probe around with one of those tablet-y things, or they might have it

**Dave Jones:** in the emergency department or something like that. They can just check you out while you're lying around. They don't have to haul around a big machine. It also can be used for obstetrics stuff as well, I believe.

**Dave Jones:** anyway, this looks like a sealed unit. Might have to get the Dremel out for that. But, this puppy has some screws. So, I'm not sure if there's any active circuitry in here or whether or not it's just a connector.

**Dave Jones:** Anyway, teardown time. All right, let's crack this open. Got the screws out. And oh, oh, yeah, look at that. Wow. A whole bunch of inductors right off the bat.

**Dave Jones:** So, that would be just for like EMC type reasons, wouldn't it? But, anyway, the cable's going to be heavily shielded cuz as you saw in the ultrasound machine teardown, like it's They really take their shielding seriously cuz these are medical devices.

**Dave Jones:** They don't want to them to interfere with other stuff. So, have a look at the braid in there, and that's just That's tied down right to the metal case.

**Dave Jones:** This is all metal, none of that plastic rubbish. And that looks like a large ferrite. Yep, or multiple ferrites there with some sort of tape around it. So, they've got a ferrite bead on there and it looks like every single channel of this thing.

**Dave Jones:** So, count those and you might be able to see how many channels this thing's got because yeah, they're going to have multiple channels spread across here. They're going to have lots of ultrasound elements right across there like that.

**Dave Jones:** I don't know if they have like staggered rows or anything like that. Might see that when we tear it down. I hope this thing's not like completely potted cuz if it is, that'll be a real bummer, but and now it looks like we've got another board down there.

**Dave Jones:** So, actually Up, there you go. Double that number of [laughter] channels. So, yeah, that's just that's that's crazy. Or they might had not they might have like two per transducer.

**Dave Jones:** That'd be my guess, but it looks like there's Looks like there's no other active circuitry on there. It's just It's just a physical connection, but and there we go.

**Dave Jones:** We can fizz Oh, look at that. We can physically take that apart. Oh, that's just That is so satisfying. [laughter] That is just gorgeous. That is terrific. Anyway, that's a PCB mount connector on the front there.

**Dave Jones:** Absolutely terrific. Um, those aren't spring loaded for those playing along at home. But yeah, PCB mount and then the board-to-board inner connect. Wow. [laughter] Anyway, we've got a large that they all pass through a large ferrite here.

**Dave Jones:** So, yeah, every single individual wire going to a transducer contains an inductor. I don't think there's any There's no surface mount caps on there, but anyway, we can see they've got a tab bonded connection down to the bottom of the board there for individual wires.

**Dave Jones:** That's really quite remarkable, isn't it? Yeah, how do they do that? Cuz it's not like they're bonded together as like a ribbon. Um, these are they're all individual wired.

**Dave Jones:** That's that's really fascinating. Let me get the tape off. Doesn't like me taking that off. Um Anyway, this is a destructive teardown anyway, so bugger it. So, there you go.

**Dave Jones:** That's how that works. Some sort of yeah, metal bar on the base of that, but each wire is is individually uh soldered individually like uh you know, a re- reflow {slash} a hot bar attached down in there.

**Dave Jones:** So, yeah, that's interesting. So, yeah, how exactly they bundle those uh together and put that tab connection on there. It'd be done as a hot bar. Uh that'd be that'd be my guess.

**Dave Jones:** That's what it looks like it's done, but yeah, fascinating. Now, we've just got a couple of extra connections going off there to a lead, and that's about all she wrote.

**Dave Jones:** Everything else is just really a direct interconnect. So, yeah, they're very serious about their shielding, and of course, you have to be cuz we're talking Although we're not talking like really high frequencies, only talking like sub 5 MHz here.

**Dave Jones:** You got to understand that these are powered ultrasonic transducers. So, these things operate I showed a data sheet in the previous video like a typical ultrasound multi-channel driver chip, and we're talking like 50 V at up to 2 amps driving capability.

**Dave Jones:** Then when you multiply that by lots of channels and huge big antenna cables coming off here. Yeah. And yep, you guessed it. All this is going to be metal inside as well.

**Dave Jones:** That's going to be shielded. So, if you cut that open, you can start to see the metal thread in there. So, it looks like they've got it'll be all metal casing as you'd expect cuz why why go to all the trouble of like shielding all that and then just don't do anything on the final leg inside here.

**Dave Jones:** And they've really done that strain relief brilliantly because yeah, like this is top quality. Like they're not going to penny pinch. This could be a bit messy. And yes, this isn't a oscilloscope front cover.

**Dave Jones:** Well, the good news is it's not potted. Can see lots of copper shielding tape in there. So, it's actually not doesn't look like a metal case. That was just a a metal outer like a metal strain relief ring.

**Dave Jones:** Yeah, it's going to I can break this apart. Hey, there we go. Look at that. Yep. [laughter] Handmade jobby. Each one of them. Oh, there we go. That's the thermistor.

**Dave Jones:** Sorry, [snorts] I got my mask on. It's let me clean this up. So, there you have it. That's inside the head and as we saw in the previous teardown video of the ultrasound machine, it does temperature sensing in the head.

**Dave Jones:** So, the software can detect that that it's you know it's getting too hot. It's putting too much power into it. It's a safety mechanism. So, that was a that was a thermocouple.

**Dave Jones:** That's now a broken thermocouple, I guess. Um anyway, you can see that the braid is connected to the top side there and also down to the bottom side there.

**Dave Jones:** So, but yeah, look at that copper shielding tape there. They're really serious there. Why they didn't do it as like a metal case? Maybe it was you know too heavy or something.

**Dave Jones:** I I don't know what the deal is there. Um or the copper tape was just better and cheaper and simpler. Yeah, anyway, I'm not sure if there's anything on that PCB.

**Dave Jones:** I think it's just termination, but uh let's get this tape off. It's just it's soldered down. So, I'm not going to bother to desolder that. Just going to peel it off because it's very thin copper.

**Dave Jones:** It just breaks very easily. There you go. Yeah, I don't see any circuitry on there. Yeah, all I see is a bunch of wires looping back. So, that's just for termination reasons and just a PCB.

**Dave Jones:** I can see stitching around the via stitching around the outside of the PCB like that. So, it's going to be one big ground plane. So, I believe they're like they're going to terminate the uh connections in here.

**Dave Jones:** They'll probably run as uh like uh you know, not necessarily controlled impedance, but just like shielded um by the top and bottom ground plane. Would be my guess. And then, for good measure, of course, they put the copper tape on top.

**Dave Jones:** But, of course, you have all this wiring exposed. Uh you have to terminate that somehow. You've got to like fold it inside. So, the whole thing has to be uh double shielded.

**Dave Jones:** And here you have it, the rubber just comes off. I'm so glad that this wasn't entirely potted. And you can see the array there. If you zoom in in 4K Well, if you look at this in 4K, you'll be able to see that they're vertical elements.

**Dave Jones:** You'll be able to count them. Go on. There you go. Try to get a nice deep field of view on that so everything's in focus. And yeah, and good luck trying to count.

**Dave Jones:** There you go. Here's a closer look. Let's have a zoom in on that. You can see the flat flex on top, all the individual wires coming through and actually making contact with a thin vertical slice of presumably like some sort of uh piezo ceramic transducer element.

**Dave Jones:** So, I don't know if they'd have like one uh transmit and one receive next to it. I'm not sure of the actual architecture of that or whether or not they use the same element transmit and then actually receive somehow on the same element.

**Dave Jones:** Not sure what the deal is, but that's neat, huh? And it looks like they're all joined together there, but that's actually the top copper shielding tape, which I haven't taken off yet.

**Dave Jones:** So, you can see all the individual traces buggering off on the copper shielding tape. But, as you can see, all the top traces there are all going to one side of the one contact side of the element, and all the ones on the other side would be going to the other side.

**Dave Jones:** But, hang on. If you have a look at this side of it, you can see that all the elements are actually common. They do actually go to the one huge copper uh pour on the flat flex there.

**Dave Jones:** So, one side of the element is all grounded. And then the other side, that's where they actually get that from. So, there's one There is one huge common attachment to all presumably like 128 elements or whatever.

**Dave Jones:** So, interestingly, there are no gaps between the elements. They're like all uh sandwiched together. So, that's interesting. Not sure of the uh uh the uh beam-forming physics of all this, but yeah, I'm sure someone in the comments will know.

**Dave Jones:** Now, it's not particularly easy to find uh good material on this, but I found this one, multiple element uh transducers and the construction and the electronic scanning techniques. And look, we've got uh linear arrays here.

**Dave Jones:** We've got curved arrays. We've got circular arrays and how they're constructed. And it looks like they might actually fire these in like separate like groups of elements and continually fire them and scan them across uh in linear arrays, although there's multiple uh techniques for doing this.

**Dave Jones:** There's individual uh phasing, as we'll see in a second. Uh but voltage pulses are applied simultaneously all elements in the group, first elements through one, then as a group, and they scan across.

**Dave Jones:** That's for a linear array. And that's but you're uh familiar with the more traditional ultrasound being like a a tapered array like that and sure enough if you use your curved array that's what it does.

**Dave Jones:** You know, it gives you that pattern like that and that's what you're looking at there. It So if you ever see a screen like that you know that they're using a curved element array like that.

**Dave Jones:** And once again this is like a 5 megahertz one so this is bang on to what we're looking at here cuz ours is a 2 to 5 megahertz array.

**Dave Jones:** So this is linear phased array operated by applying voltage pulses to all elements not a small group in the assembly as a complete group but with small less than microsecond time differences or phasing essentially so that the resulting sound pulse may be sent over a specified path direction if the same time differences are used each time the process is repeated the same direction will result repeatedly.

**Dave Jones:** However, the time difference phases are changed with these successive repetitions so that each beam direction can tangentially change as each pulse travels in a slightly different direction. That can reside and then result in sweeping of the beam producing a sector image in which the scan lines fan out in different directions from a common starting point.

**Dave Jones:** Space arrays sometimes called an electronic sector transducer. There you go. Who knew? Phasing can also be applied on reception of echoes so the array can listen I most sensitive in a particular direction but phasing can also be applied to that group based firing structure in linear sequenced arrays as well.

**Dave Jones:** So yeah, there you go. That's the sector type image that you get with a curved array like this. Cool. But yeah, what they're actually doing inside this particular one inside this ultrasound you can probably program the thing to do different things.

**Dave Jones:** I'd be stunned if it didn't have the flexibility to you know if a group them and phase them in different ways and stuff like that. So yeah, like is it 128?

**Dave Jones:** Did anyone count 128 elements in there? Possibly. I don't know. So, yeah, that flat flex would all be hot bar attached right across there. And I'm sure it's uh not easy to do all this.

**Dave Jones:** I'm sure there'd be a lot of uh finesse involved in this thing. And yeah, does anyone want to try and guess the uh pin pitch in there? Hmm. Really impressed by that.

**Dave Jones:** And I'm glad, as I said, I'm glad that wasn't potted so that we can see it. And if we peel off the Mylar tape there, ta-da! There you go.

**Dave Jones:** You can see how they've got that that bundles all the wires together. I think they do. They do run as a ribbon, do they? But anyway, there you go.

**Dave Jones:** You can see the Once again, hot bar attachment. And if we peel that off, we're probably just going to peel the whole lot off. Jumps down through the vias down to the inner layers.

**Dave Jones:** And uh as I said, vias stitched around the outside so all the electrons don't escape. And then jumps back up. And they've got to route around these alignment spigots as well.

**Dave Jones:** Uh that's pesky. So, there you have it. That is inside a Well, I'm assuming that that the modern ones would be exactly the same. Like this one I think dates from like uh you know, 20-plus years ago.

**Dave Jones:** But I like they make exactly the same model. So, maybe they've you know, refined the manufacturing processes or something like that. But the shielding and all the other uh stuff which goes into it would be uh exactly the same because they've got the same model number.

**Dave Jones:** I assume that they're going to have like the same head on this. They've probably been using that same uh ceramic transducer technology for like 20 years or something like that.

**Dave Jones:** Um you know, if it ain't broken, don't fix it. Uh so, that's very cool. So, yeah, we got uh got lucky there. We got some nice connector action. We've got some beautiful uh EMC inductor action going on there for you inductor fanboys.

**Dave Jones:** And and got the ceramic action going on here for the ceramic fan boys and and it's just like fantastic what goes into one of these little ultrasound probes. Absolutely terrific.

**Dave Jones:** So, now next time you're being uh probed in a hospital or in the back of an ambulance somewhere, well, maybe you've got something better to think about, but yeah, just think about the ultrasound here, you know, 2 to 5 MHz for this you know, you can talk to the talk to the doctors in there.

**Dave Jones:** Oh, yeah, you're using the C5 curved array. Oh, yeah, yeah, that works from 2 to 5 meg and you know, 40 mm aperture and stuff. Yeah, know all about it.

**Dave Jones:** Saw it on the EEVblog. So, anyway, if you like that video, please give it a big thumbs up. As always, discuss down below or over on the EEVblog forum or one of my many other platforms I'm on.

**Dave Jones:** I'm on everything. I sign up for a lot of them. Gives everyone choice. Catch you next time. [music]
