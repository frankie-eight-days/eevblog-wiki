---
video_id: 8gJxII4UvSA
title: EEVblog #989 - FLIR ETS320 Thermal Camera Teardown
url: https://www.youtube.com/watch?v=8gJxII4UvSA
source: youtube-asr
---

**Dave Jones:** Hi, it's teardown time. This is the brand spanking new just released FLIR ETS320 thermal imaging camera, 320 by 240 screen resolution screen. Screen, I've done a review on this. So, if you want to have a look at that, it'll be up in

**Dave Jones:** the card somewhere up there. But, we don't want to do that today. We want to tear it apart. Let's go. I see some screws on the top. All right, we've got four screws and then we've got a whole bunch of little

**Dave Jones:** plastic retainer clips. And hopefully nothing uh Yeah, I do We're almost in like Flynn except for the bloody LCD ribbon cable. Bugger. Okay, what's I'll get back to you. We're almost in like Flynn, but um I do not like this at all. This ribbon cable

**Dave Jones:** had no reach to go I don't know how I'm going to get that back in. I honestly don't know. Um that is really bizarre. Um like as it like I might have to No, oh actually, does that I that that

**Dave Jones:** that unclips? Okay, I think that front panel might unclip from there. I was going to say I might have to uh get the heat gun out and you know, that might be the final step or something like that.

**Dave Jones:** So, yeah, but with the plastic there, you can't do it. There's our 18650 um internal uh rechargeable battery. This is interesting. We've got micro USB. Look at that. Going over to That's a that's a die Is that a diecast

**Dave Jones:** alloy or a magnesium alloy shell on there? Uh that's probably that's probably diecast. Is it for uh that'd be for thermal that'd be for thermal thermal mass reasons. And they've got these uh copper straps all over the place and you can

**Dave Jones:** see the copper backing on the LCD as well. Another copper uh shielding sort of plate going over there making contact. That That's making contact to the front there. So, they're really serious about the uh uh RFI in this thing. Wow, they're going

**Dave Jones:** to town. All right, this was really tricky. Um but, it did come out as one module. RFI bead on there. Look at that. Woo! Going to town. Anyway, it did come out as one module. There's our USB, which comes from here

**Dave Jones:** over to here. Wow, they couldn't even design like I it interface. Look at the copper shielding over that as well. You know, it's all a bit No, it's not really how you're doing, but it's you know, it's getting there.

**Dave Jones:** Anyway, we have the module. All comes out in you know, little plastic you know, a plastic retaining hook. And of course, it's all in one big diecast alloy thing as I said for thermal mass reasons. You expect that.

**Dave Jones:** Um but, yeah. It's certainly over-engineered. And that is our main board. We can see we've got our battery backup there. It's got a Well, presumably it's got a real-time clock boot loader 16.5 for those playing along at home.

**Dave Jones:** Winbond. All right, so we've got some SDRAM there. We've got our ROM. Some more memory over here. So, that means the processor is tucked away inside. And for those hacking, I don't know, there's lots of test points here.

**Dave Jones:** One of those could be a debug serial interface, of course. Um so, yeah, I don't know. I'm not going to probe around. I'm not too interested in hacking this thing. Um as long as it gives me the focal length I want, uh, because

**Dave Jones:** like there's no extra model to hack up. So, there's no real incentive to go in there and hack it unless maybe you wanted a higher frame rate or you wanted to repurpose it for, uh, something else. So, yeah, I'm not going to bother in

**Dave Jones:** that respect. Tell you what, this is one complicated ass assembly, but I am quite impressed by, uh, whoever did all the, uh, 3D envelope design and, uh, all the systems integration on this. But, um, check out just wanted to mention this. We've got a

**Dave Jones:** a slot around the PCB like that. There's something there. I reckon that could be some isolation for a, uh, temperature sensor, perhaps. Hmm. And there's our sensor down in there on its own little board with its own, uh, thermal

**Dave Jones:** Is it I think no, it'd be thermally coupled through to the aluminum, uh, case there. So, that's our board-to-board interconnect, which then goes directly onto there into the, uh, FPGA and does all the whiz-bang processing. So, let's see if we can get that module out and

**Dave Jones:** have a look. It's just going to be It's got not going to be a new sensor in here. It's just one of their Lepton's or whatever their latest generation, uh, 320 by 240 sensor is. There is the back

**Dave Jones:** of that. It's upside down, so all the electrons are going to fall out. And that And I won't take this apart further, but there is going to be the, uh, shutter down in there. The red and black wire

**Dave Jones:** going down in there. That'd be the calibration shutter, which comes across and closes that. And you can see the little, uh, germanium, probably germanium, uh, lens in there. I said it before, I really do like how all this

**Dave Jones:** goes together. This has got this self-tapping, uh, points, this plastic holder that sort of holds that in there. But, that's it's It all goes together rather brilliantly, if a bit, you know, the first time you try and take it apart, seems a bit

**Dave Jones:** convoluted, but there's definitely method to the madness in this. And if you're wondering, yep, that temperature sensor there goes down in that little hole down in there. So, it's measuring the uh the chassis uh temperature. So, that makes sense.

**Dave Jones:** So, let's have a look at this under the Tiguan microscope. There's not too much interesting on that side, but here's the money shot. Here's what everyone wants to see. So, let's go in there. And there we go. We've got

**Dave Jones:** a uh Freescale uh thingamabob um thingy. And uh here's your Cyclone 4 FPGA. That'd be a JTAG-y type stuff. And uh Oh, look at this. Load on off. So, that's your uh Is that your load for your uh FPGA?

**Dave Jones:** Perhaps. That'd be That'd be my guess. Anyway, that cool-looking jazzy down in the corner there. Oh, Dialog Semi. Okay. That's the You can tell by all the inductors and all the caps, that's a uh multi-core voltage chip. And we've got

**Dave Jones:** that doesn't connect to anything. So, like inside the camera. So, that's obviously a uh some sort of programming {slash} debug uh interface. And suggested, that is isolated up there. That's isolated for thermal and uh vibration reasons. So, it's either a

**Dave Jones:** voltage reference or a temperature sensor. Take your pick. I don't know. What's a T730 on a six-pin uh SOT-23 package? David's over there busily trying to get that up on his phone. It's easy. Another header there which doesn't seem

**Dave Jones:** to be doing much. So, there you go. That's about all she wrote on that board for those playing along at home. But as I said, you probably don't want to hack this thing. All right, I think you're going to want

**Dave Jones:** to see this under the Tagarno. Got our test pads there. So, there's our That was not our sensor. That is a lens. Once again, that could be a some sort of you know, germanium type lens. And There it is. You can see the lens stuck

**Dave Jones:** to the bottom down there, but that is our sensor. Try not to spit when you're talking, Dave. There it is. Hear that? Here's the 320 by 240 array. How close can I get? That's as close as I can get. There we go. You can see all

**Dave Jones:** the traces. You can see the bond wires going over. Very neat. This is the maximum zoom on the Tagarno. It's not a uh I mean, the Tagarno is a microscope, but it's not a die microscope. You can see the various

**Dave Jones:** layers there on the die. That's fantastic. And oh, there's the text. There's the text. ISC090180 From 2009. Copyright 2009. There you go. So, that is not a new sensor. That is 2009 vintage. Thank you very much. And just the

**Dave Jones:** Oh, no. They've just etched away all the copper on top. I thought might have been some special substrate board or something. It's not. That's just your regular woven fiberglass. But, there you go. There's the sensor. Isn't that groovy?

**Dave Jones:** Woohoo! I love the Tagarno microscope. It's great. And I'm getting this sort of zoom level at at what? 300 mm working distance. I mean, that's just that's just nuts. That's great. That actually went together much nicer than it came apart.

**Dave Jones:** I would I'm actually impressed by that. I still think it's over-engineered in terms of physical complexity, but it's still pretty impressive. Nothing you can't fix with 100° air gun. There you go. That just came off and the shielding they've got everywhere on this

**Dave Jones:** thing is just absolutely crazy. So, that's got full copper shielding right around. Wow, gilding the lily. So, here's how the Mongols have assembled this. It was physically impossible well for this to be an assembly and get that ribbon cable back in there.

**Dave Jones:** Absolutely impossible. So, what you do is now we can get in there and we can just, you know, insert that. No worries, right? It's a little bit tight, but no worries. We can get in there and do that. And once it's done then that

**Dave Jones:** goes whoop, we can take that off and then that goes through there at an angle like that. Look at that. Mongols. And then they glue on the metal and then they glue on the face plate. Unbelievable. LCD part number for those playing along

**Dave Jones:** at home. I think we have a winner winner chicken dinner. Well, it's doing something anyway. It's man, this is really some evil piece of work, let me tell you.

**Dave Jones:** I'm going to put that over the over the back of that without putting stress on the ribbon cable. And then that's got to go back in there and then that's got to fold under there like that. I should just ditch this bloody copper.

**Dave Jones:** Who cares about that? Ah, there we go. All right. I think we got it. We got it. And then that Clean the screen first. Ah, it's pretty clean. And that will go back on the front and uh Bob's your uncle.

**Dave Jones:** He is my uncle. And we did it. Yay! Ta-da! It's like a bought one. It's back and it works again. Oh, by the way, and one of the other things is you might be able to see here you can see my fingers

**Dave Jones:** on the screen, yet I am nowhere near the sensor at all. Like my fingers are not under the sensor. What it's doing is getting even if I hold my hand on top here you might be able to calibration, you might see it come

**Dave Jones:** through maybe. It's getting reflection um off there. So, if you've even got anything nearby, it can actually reflect off there, but you saw a menu option in there to get the um the heat reflected uh setting on that. But, yeah, just be

**Dave Jones:** careful. So, that was a rather interesting tear down. Um a very nicely designed and engineered as you'd expect. Um but, yeah, the stand leaves a little bit to be honest. A bit how you doing the stand? I don't know, a bit cheap.

**Dave Jones:** Kind of lets it down a bit, but uh yeah, that's an interesting bit of kit. If you want to uh discuss it, EEVblog forum down below somewhere as always. Catch you next time.
