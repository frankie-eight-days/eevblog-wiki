---
video_id: q53uPn1mKc0
title: EEVblog #181 - Dead Bug Prototype Soldering
url: https://www.youtube.com/watch?v=q53uPn1mKc0
source: youtube-asr
---

**Dave Jones:** Hi, welcome to the AAVW an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, just a quick one. This is not actually going to be part of my soldering tutorial. I just

**Dave Jones:** so happen to be playing around with a little three-axis accelerometer and I want to hook it up to a Microchip PIC chip and I thought I would just show you just the process of actually soldering this thing dead bug style. I've talked

**Dave Jones:** about this before because these three-axis accelerometers they are not really available in the discontinued all of the usable packages like for basic soldering or the SO type packages and even DIP type packages. You can only get them in these

**Dave Jones:** tiny little LGA or other type surface mount packages now and they're a real pain in the ass, but I thought I'd just show you. I was just going to hook one up to this PIC demo board so I can play

**Dave Jones:** with it and do some software and I just thought I'd show you soldering that chip. So, let's go. Here's the PICkit demo board I'm going to use. I just had this lying around and it just so happened to have a reasonable

**Dave Jones:** PIC chip on it and a prototyping area here and here's my little tiny LGA package accelerometer 3 mm by 2 mm and I'm going to solder onto here dead bug style. And here's the actual LGA type package it's called. It's a 14-pin LGA and as

**Dave Jones:** you can see it's 5 mm by 3 mm in comparison to a standard quarter watt resistor here. It's It's not overly tiny in the scheme of things for surface mount stuff today, but it still is a real pain to solder because as you can

**Dave Jones:** see it's it doesn't have the uh pads extending down the side of the case. So, you can't really, once you lay this thing down on the board, these pads are not directly accessible with the soldering iron. So, really these chips

**Dave Jones:** are only designed for a reflow soldering process. They're not really designed for hand soldering. So, that's why today I'm going to actually flip it upside down like this and then I'm going to individually wire tiny little bond wires

**Dave Jones:** over to my prototyping area here. So, I'm going to sit it on here and I'm going to wire all the individual pads over to a larger footprint, which then I can um access via hand soldering. This is an example of dead bug style

**Dave Jones:** construction. Now, the term dead bug actually comes from um actually turning something like a DIP package upside down on its back like that and it looks like a bug with its legs on its back dead with its legs sticking up in the air

**Dave Jones:** like that. And that's where the term comes from. So, even though this little LGA package does not have uh legs sticking up in the air, you would still I would still call this dead bug style construction. So, you flip it on the

**Dave Jones:** back, you actually glue it down, and then you individually solder almost like um almost like what's what happens inside an IC itself. They and the machines automatically insert bond automatically wire in little bond wires to the pads, which go out. If you

**Dave Jones:** actually opened one of these uh DIP chips, inside you will find like a silicon uh a silicon die like that with little bond wires going out to these larger legs. And that's pretty much exactly what we're going to do here today. Now, I'm

**Dave Jones:** pretty confident of doing this one because it has a 0.8 mm pin-to-pin pitch. And that's uh reasonably large. The pads on there are reasonably large in the scheme of things. So, I shouldn't really have too much trouble, I don't

**Dave Jones:** think, um actually wiring this one up. It we should be able to do it reasonably easily using a bit of magnification. I could probably do it by eye as well, but we'll actually use some magnification today. Just start 2 and 1/2 times or

**Dave Jones:** something like that, just to help us in actually soldering onto the pads and making sure we don't short things out. And there's the device that we're going to solder. It's the MMA7455 3-axis accelerometer. It's from a Freescale, and that's the LLG-14

**Dave Jones:** pin package. Now, as you can see, over in that little the bottom left corner there, it does have a little pin one marker. It's important for us to actually get that correct when we flip it over, so we know exactly what pin's

**Dave Jones:** what. It seems to have another little marker there, if you can see it, which indicates that it's the same side, but you just have to remember which one is actually pin one. Okay, we want to add a tiny little drop

**Dave Jones:** of super glue down in here, just so that we can hold that chip in place.

**Dave Jones:** There we go. We've just tacked that in place. It this stuff sets almost instantly, of course, so you've got to be very, very careful, but that will just hold our chip in place while we solder it, because you don't want the

**Dave Jones:** thing moving around. Okay, the first thing I'm going to do is I'm going to apply some flux from this flux pen just across the main pads there, and also on top of the device as well, just so we

**Dave Jones:** can get some good wetting onto those pads. And what I'm going to use to make the connections is some wire wrapping wire, solid core 30 AWG tinned wire. And this is really useful stuff. I highly recommend you get some.

**Dave Jones:** It's not fine. It's great for uh mods like this. And in fact, it is called a uh mod wire. And it comes in various colors. And uh there's the actual um it's an OK Industries uh brand 130 AWG.

**Dave Jones:** And using my chisel point iron and my 0.46 mm solder, I'm going to tin these pads. Um I've already tinned a couple, and that didn't uh unfortunately, I didn't press the record button. Oops. And uh this is not my

**Dave Jones:** finest work because I am trying to do this under the under the uh camera. So, the angle of the iron is not um ideal to how I'd normally do it, but uh you can just tin these pads like that. And then we will

**Dave Jones:** um solder the wires, each individual bond wire onto those, and take them out to the individual pads.

**Dave Jones:** Let's try and solder a wire onto there. Um it can pay it can pay you to actually tin these wires first um just so that they uh wet a bit better. But there you go. That first one is attached. And then

**Dave Jones:** we'll just get in there and we'll actually uh cut that. And we'll get in and we'll push that down so it contacts one of the pads. Let's say that one there, and then this one will go to that pad, that one

**Dave Jones:** will go to that pad, and so forth. I need to add some more solder to these pads in here because it the last process just uh sucked a fair bit of that away. So, we'll get in here with our wire

**Dave Jones:** again. And I'm doing all this through the camera LCD. I can't actually uh see the board here. So, this would just be just like working under a microscope, really. Except, I haven't got much in the way of magnification here, but there we go.

**Dave Jones:** Now, what I'm going to do here is I'm going to tin the uh wire cuz this is a fairly uh fairly important uh step. Although, this is already tinned copper wire, um really that uh you got to add some flux

**Dave Jones:** on there, clean it, get some fresh solder on there to just to make sure it really takes. And after I do that, I clean my iron on my sponge. And hopefully, if there's enough solder on the uh pad on the chip,

**Dave Jones:** that will be enough to reflow onto my what my already tinned wire. And yep, there it goes. There. Made an attachment, nice and quick, easy, and a good quality joint.

**Dave Jones:** And this one here, I've got to bend a bit further over. And don't bend it down directly cuz you don't want these to short cuz they aren't insulated uh wires, but it's uh pretty easy to solder them onto a

**Dave Jones:** smaller um well, a larger, sorry, uh diameter um pad. So, later on, I will actually solder uh flying leads directly off these pads here onto my PIC chip.

**Dave Jones:** And there's my completed dead bug chip. It's uh not my finest uh work. It is surprisingly difficult um to do on on a shallow angle when you've got the camera in the way, but uh bit harder than usual, but that only took me

**Dave Jones:** like 5 minutes or something like that. It wasn't hard at all. And I've now converted that um in um LGA package chip into a much more uh usable pitch that I can actually come along and now um solder on some of this

**Dave Jones:** uh mod wire. I'll just uh solder them onto each of those and then over to the specific pin on the PIC chip which I need. Simple. So, that should work a treat. Uh I'll have to do some um more

**Dave Jones:** uh up close uh visual inspections under the microscope, but that looks fine to me.
