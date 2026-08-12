---
video_id: lmy8J8n9wPU
title: EEVblog #1315 - Ultrasound Probe Extreme Teardown!
url: https://www.youtube.com/watch?v=lmy8J8n9wPU
source: youtube-asr
---

**Dave Jones:** Hi, this is a follow-up video to my previous one where I tore down a ATL/Philips ultrasound machine. And that was a pretty epic video, almost 50 minutes long. So, I'll link that in at the end of down below if you haven't

**Dave Jones:** seen it. But, I promised that I would take a look at one of these ultrasound probes. And well, let's try and tear this thing apart to see what makes one of these tick. Now, this is the this is

**Dave Jones:** a curved array. You can get actually the ultrasound that we looked at machine had a three different connectors on there. So, you can permanently connect up to three different ultrasound probes to that particular machine. So, that then you can switch them in software

**Dave Jones:** depending you didn't have to, you know, connect and unconnect the actual sensors like this. And by the way, the actual connectors are absolutely gorgeous. Look at that. It's just thing of beauty, joy forever. Anyway, really robust kind of, you know,

**Dave Jones:** industrial type connector that just latches that in place there. Beautiful. Anyway, this is one of the probes compatible with the HDI 3000 ultrasound. And it's the C52 curved array. This is Philips branded cuz Philips bought out ATL in the mid-90s.

**Dave Jones:** Now, this is the C5240R. Philips currently sell a C52 ultrasound probe that looks very similar to this. This is actually a curved array. That's why they call it a curved array cuz it's actually curved like that. And they do sell the exact

**Dave Jones:** basically the same model as this, but it doesn't have this connector. It comes with like a USB connector on it that plugs into like a newfangled tablet type device. Not sure if it's customized or whatever. So, that, you know, you can

**Dave Jones:** use them in the back of ambulances, in the field, wherever. You know, you can just you don't need to haul around this big 200 kg ultrasound machine. You can just plug in this little battery-powered tablet thing, hook it up to one of these

**Dave Jones:** curved array probes, and you can diagnose people on the spot. Now, this particular curved array here, the C52, it operates from 2 MHz to 5 MHz range, and it's got a 67° field of view. It can Well, the new one I got the spec that it

**Dave Jones:** can penetrate up to 30 cm depth, and this particular type of probe is actually used for abdominal diagnosis. You know, abdominal injuries, gallbladders, and lung injuries, and you know, things like that. So, if you're in the back of an

**Dave Jones:** ambulance and they want to, you know, think you've got an abdominal injury or something's wrong with your lungs or something like that, they might, you know, wax some of the ultrasound gel on this and probe around with one of those

**Dave Jones:** tablet-y things, or they might have it in the emergency department or something like that. They can just check you out while you're lying around. They don't have to haul around a big machine. It also can be used for obstetrics stuff as

**Dave Jones:** well, I believe. anyway, this looks like a sealed unit. Might have to get the Dremel out for that. But, this puppy has some screws. So, I'm not sure if there's any active circuitry in here or whether or not it's just a connector. Anyway,

**Dave Jones:** teardown time. All right, let's crack this open. Got the screws out. And oh, oh, yeah, look at that. Wow. A whole bunch of inductors right off the bat. So, that would be just for like EMC type reasons, wouldn't it? But, anyway,

**Dave Jones:** the cable's going to be heavily shielded cuz as you saw in the ultrasound machine teardown, like it's They really take their shielding seriously cuz these are medical devices. They don't want to them to interfere with other stuff. So, have a look at the

**Dave Jones:** braid in there, and that's just That's tied down right to the metal case. This is all metal, none of that plastic rubbish. And that looks like a large ferrite. Yep, or multiple ferrites there with some sort of tape around it. So, they've

**Dave Jones:** got a ferrite bead on there and it looks like every single channel of this thing. So, count those and you might be able to see how many channels this thing's got because yeah, they're going to have multiple channels spread across here.

**Dave Jones:** They're going to have lots of ultrasound elements right across there like that. I don't know if they have like staggered rows or anything like that. Might see that when we tear it down. I hope this thing's not like completely potted cuz

**Dave Jones:** if it is, that'll be a real bummer, but and now it looks like we've got another board down there. So, actually Up, there you go. Double that number of [laughter] channels. So, yeah, that's just that's that's crazy. Or they might had not they

**Dave Jones:** might have like two per transducer. That'd be my guess, but it looks like there's Looks like there's no other active circuitry on there. It's just It's just a physical connection, but and there we go. We can fizz Oh, look at that. We can physically

**Dave Jones:** take that apart. Oh, that's just That is so satisfying. [laughter] That is just gorgeous. That is terrific. Anyway, that's a PCB mount connector on the front there. Absolutely terrific. Um, those aren't spring loaded for those playing along at

**Dave Jones:** home. But yeah, PCB mount and then the board-to-board inner connect. Wow. [laughter] Anyway, we've got a large that they all pass through a large ferrite here. So, yeah, every single individual wire going to a transducer contains an inductor. I

**Dave Jones:** don't think there's any There's no surface mount caps on there, but anyway, we can see they've got a tab bonded connection down to the bottom of the board there for individual wires. That's really quite remarkable, isn't it? Yeah, how do they

**Dave Jones:** do that? Cuz it's not like they're bonded together as like a ribbon. Um, these are they're all individual wired. That's that's really fascinating. Let me get the tape off. Doesn't like me taking that off. Um Anyway, this is a

**Dave Jones:** destructive teardown anyway, so bugger it. So, there you go. That's how that works. Some sort of yeah, metal bar on the base of that, but each wire is is individually uh soldered individually like uh you know, a re- reflow {slash} a hot bar

**Dave Jones:** attached down in there. So, yeah, that's interesting. So, yeah, how exactly they bundle those uh together and put that tab connection on there. It'd be done as a hot bar. Uh that'd be that'd be my guess. That's what it looks

**Dave Jones:** like it's done, but yeah, fascinating. Now, we've just got a couple of extra connections going off there to a lead, and that's about all she wrote. Everything else is just really a direct interconnect. So, yeah, they're very serious about their shielding, and of

**Dave Jones:** course, you have to be cuz we're talking Although we're not talking like really high frequencies, only talking like sub 5 MHz here. You got to understand that these are powered ultrasonic transducers. So, these things operate I showed a data sheet in the previous

**Dave Jones:** video like a typical ultrasound multi-channel driver chip, and we're talking like 50 V at up to 2 amps driving capability. Then when you multiply that by lots of channels and huge big antenna cables coming off here. Yeah. And yep, you guessed it. All this

**Dave Jones:** is going to be metal inside as well. That's going to be shielded. So, if you cut that open, you can start to see the metal thread in there. So, it looks like they've got it'll be all metal casing as

**Dave Jones:** you'd expect cuz why why go to all the trouble of like shielding all that and then just don't do anything on the final leg inside here. And they've really done that strain relief brilliantly because yeah, like this is top quality. Like

**Dave Jones:** they're not going to penny pinch. This could be a bit messy. And yes, this isn't a oscilloscope front cover. Well, the good news is it's not potted. Can see lots of copper shielding tape in there. So, it's actually not doesn't look like

**Dave Jones:** a metal case. That was just a a metal outer like a metal strain relief ring. Yeah, it's going to I can break this apart. Hey, there we go. Look at that. Yep. [laughter] Handmade jobby. Each one of them. Oh, there we go.

**Dave Jones:** That's the thermistor. Sorry, [snorts] I got my mask on. It's let me clean this up. So, there you have it. That's inside the head and as we saw in the previous teardown video of the ultrasound machine, it does temperature

**Dave Jones:** sensing in the head. So, the software can detect that that it's you know it's getting too hot. It's putting too much power into it. It's a safety mechanism. So, that was a that was a thermocouple. That's now a broken thermocouple, I

**Dave Jones:** guess. Um anyway, you can see that the braid is connected to the top side there and also down to the bottom side there. So, but yeah, look at that copper shielding tape there. They're really serious there. Why they didn't do it as like a metal

**Dave Jones:** case? Maybe it was you know too heavy or something. I I don't know what the deal is there. Um or the copper tape was just better and cheaper and simpler. Yeah, anyway, I'm not sure if there's anything on that PCB. I think it's just

**Dave Jones:** termination, but uh let's get this tape off. It's just it's soldered down. So, I'm not going to bother to desolder that. Just going to peel it off because it's very thin copper. It just breaks very easily. There you go. Yeah,

**Dave Jones:** I don't see any circuitry on there. Yeah, all I see is a bunch of wires looping back. So, that's just for termination reasons and just a PCB. I can see stitching around the via stitching around the outside of the PCB

**Dave Jones:** like that. So, it's going to be one big ground plane. So, I believe they're like they're going to terminate the uh connections in here. They'll probably run as uh like uh you know, not necessarily controlled impedance, but just like shielded um by the top and

**Dave Jones:** bottom ground plane. Would be my guess. And then, for good measure, of course, they put the copper tape on top. But, of course, you have all this wiring exposed. Uh you have to terminate that somehow. You've got to

**Dave Jones:** like fold it inside. So, the whole thing has to be uh double shielded. And here you have it, the rubber just comes off. I'm so glad that this wasn't entirely potted. And you can see the array there. If you zoom in in 4K Well, if you look

**Dave Jones:** at this in 4K, you'll be able to see that they're vertical elements. You'll be able to count them. Go on. There you go. Try to get a nice deep field of view on that so everything's in focus. And yeah, and

**Dave Jones:** good luck trying to count. There you go. Here's a closer look. Let's have a zoom in on that. You can see the flat flex on top, all the individual wires coming through and actually making contact with a thin vertical slice

**Dave Jones:** of presumably like some sort of uh piezo ceramic transducer element. So, I don't know if they'd have like one uh transmit and one receive next to it. I'm not sure of the actual architecture of that or whether or not

**Dave Jones:** they use the same element transmit and then actually receive somehow on the same element. Not sure what the deal is, but that's neat, huh? And it looks like they're all joined together there, but that's actually the top copper shielding

**Dave Jones:** tape, which I haven't taken off yet. So, you can see all the individual traces buggering off on the copper shielding tape. But, as you can see, all the top traces there are all going to one side of the one contact side of the element,

**Dave Jones:** and all the ones on the other side would be going to the other side. But, hang on. If you have a look at this side of it, you can see that all the elements are actually common. They do actually go

**Dave Jones:** to the one huge copper uh pour on the flat flex there. So, one side of the element is all grounded. And then the other side, that's where they actually get that from. So, there's one There is one huge common attachment

**Dave Jones:** to all presumably like 128 elements or whatever. So, interestingly, there are no gaps between the elements. They're like all uh sandwiched together. So, that's interesting. Not sure of the uh uh the uh beam-forming physics of all this, but yeah, I'm sure someone in the

**Dave Jones:** comments will know. Now, it's not particularly easy to find uh good material on this, but I found this one, multiple element uh transducers and the construction and the electronic scanning techniques. And look, we've got uh linear arrays here. We've got curved

**Dave Jones:** arrays. We've got circular arrays and how they're constructed. And it looks like they might actually fire these in like separate like groups of elements and continually fire them and scan them across uh in linear arrays, although there's multiple uh techniques for doing

**Dave Jones:** this. There's individual uh phasing, as we'll see in a second. Uh but voltage pulses are applied simultaneously all elements in the group, first elements through one, then as a group, and they scan across. That's for a linear array.

**Dave Jones:** And that's but you're uh familiar with the more traditional ultrasound being like a a tapered array like that and sure enough if you use your curved array that's what it does. You know, it gives you that pattern like that and that's what you're

**Dave Jones:** looking at there. It So if you ever see a screen like that you know that they're using a curved element array like that. And once again this is like a 5 megahertz one so this is bang on to what we're looking at here

**Dave Jones:** cuz ours is a 2 to 5 megahertz array. So this is linear phased array operated by applying voltage pulses to all elements not a small group in the assembly as a complete group but with small less than microsecond time differences

**Dave Jones:** or phasing essentially so that the resulting sound pulse may be sent over a specified path direction if the same time differences are used each time the process is repeated the same direction will result repeatedly. However, the time difference phases are changed with

**Dave Jones:** these successive repetitions so that each beam direction can tangentially change as each pulse travels in a slightly different direction. That can reside and then result in sweeping of the beam producing a sector image in which the scan lines fan out in

**Dave Jones:** different directions from a common starting point. Space arrays sometimes called an electronic sector transducer. There you go. Who knew? Phasing can also be applied on reception of echoes so the array can listen I most sensitive in a particular direction but phasing can

**Dave Jones:** also be applied to that group based firing structure in linear sequenced arrays as well. So yeah, there you go. That's the sector type image that you get with a curved array like this. Cool. But yeah, what they're actually doing

**Dave Jones:** inside this particular one inside this ultrasound you can probably program the thing to do different things. I'd be stunned if it didn't have the flexibility to you know if a group them and phase them in different ways and stuff like that.

**Dave Jones:** So yeah, like is it 128? Did anyone count 128 elements in there? Possibly. I don't know.

**Dave Jones:** So, yeah, that flat flex would all be hot bar attached right across there. And I'm sure it's uh not easy to do all this. I'm sure there'd be a lot of uh finesse involved in this thing. And yeah, does anyone want to try and guess

**Dave Jones:** the uh pin pitch in there? Hmm. Really impressed by that. And I'm glad, as I said, I'm glad that wasn't potted so that we can see it. And if we peel off the Mylar tape there, ta-da! There you go. You can see how

**Dave Jones:** they've got that that bundles all the wires together. I think they do. They do run as a ribbon, do they? But anyway, there you go. You can see the Once again, hot bar attachment. And if we peel that off, we're probably just

**Dave Jones:** going to peel the whole lot off. Jumps down through the vias down to the inner layers. And uh as I said, vias stitched around the outside so all the electrons don't escape. And then jumps back up. And they've got to route around these

**Dave Jones:** alignment spigots as well. Uh that's pesky. So, there you have it. That is inside a Well, I'm assuming that that the modern ones would be exactly the same. Like this one I think dates from like uh you know,

**Dave Jones:** 20-plus years ago. But I like they make exactly the same model. So, maybe they've you know, refined the manufacturing processes or something like that. But the shielding and all the other uh stuff which goes into it would be uh exactly the same because they've

**Dave Jones:** got the same model number. I assume that they're going to have like the same head on this. They've probably been using that same uh ceramic transducer technology for like 20 years or something like that. Um you know, if it

**Dave Jones:** ain't broken, don't fix it. Uh so, that's very cool. So, yeah, we got uh got lucky there. We got some nice connector action. We've got some beautiful uh EMC inductor action going on there for you inductor fanboys. And

**Dave Jones:** and got the ceramic action going on here for the ceramic fan boys and and it's just like fantastic what goes into one of these little ultrasound probes. Absolutely terrific. So, now next time you're being uh probed in a hospital or in the back

**Dave Jones:** of an ambulance somewhere, well, maybe you've got something better to think about, but yeah, just think about the ultrasound here, you know, 2 to 5 MHz for this you know, you can talk to the talk to the doctors in there. Oh, yeah,

**Dave Jones:** you're using the C5 curved array. Oh, yeah, yeah, that works from 2 to 5 meg and you know, 40 mm aperture and stuff. Yeah, know all about it. Saw it on the EEVblog. So, anyway, if you like that video,

**Dave Jones:** please give it a big thumbs up. As always, discuss down below or over on the EEVblog forum or one of my many other platforms I'm on. I'm on everything. I sign up for a lot of them. Gives everyone choice.

**Dave Jones:** Catch you next time. [music]
