---
video_id: q53uPn1mKc0
title: EEVblog #181 - Dead Bug Prototype Soldering
url: https://www.youtube.com/watch?v=q53uPn1mKc0
source: youtube-asr
timestamps: {"0": 0, "1": 12, "2": 28, "3": 48, "4": 57, "5": 66, "6": 90, "7": 102, "8": 117, "9": 132, "10": 144, "11": 158, "12": 174, "13": 185, "14": 200, "15": 215, "16": 227, "17": 238, "18": 253, "19": 272, "20": 291, "21": 304, "22": 313, "23": 331, "24": 344, "25": 359, "26": 373, "27": 393, "28": 407, "29": 415, "30": 439, "31": 453, "32": 474, "33": 492, "34": 513, "35": 534, "36": 549, "37": 615, "38": 629, "39": 644, "40": 652}
---

**Dave Jones:** Hi, welcome to the AAVW an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, just a quick one. This is not actually going to be part of my soldering tutorial.

**Dave Jones:** I just so happen to be playing around with a little three-axis accelerometer and I want to hook it up to a Microchip PIC chip and I thought I would just show you just the process of actually soldering this thing dead bug style.

**Dave Jones:** I've talked about this before because these three-axis accelerometers they are not really available in the discontinued all of the usable packages like for basic soldering or the SO type packages and even DIP type packages.

**Dave Jones:** You can only get them in these tiny little LGA or other type surface mount packages now and they're a real pain in the ass, but I thought I'd just show you.

**Dave Jones:** I was just going to hook one up to this PIC demo board so I can play with it and do some software and I just thought I'd show you soldering that chip.

**Dave Jones:** So, let's go. Here's the PICkit demo board I'm going to use. I just had this lying around and it just so happened to have a reasonable PIC chip on it and a prototyping area here and here's my little tiny LGA package accelerometer 3 mm by 2 mm and I'm going to solder onto here dead bug style.

**Dave Jones:** And here's the actual LGA type package it's called. It's a 14-pin LGA and as you can see it's 5 mm by 3 mm in comparison to a standard quarter watt resistor here.

**Dave Jones:** It's It's not overly tiny in the scheme of things for surface mount stuff today, but it still is a real pain to solder because as you can see it's it doesn't have the uh pads extending down the side of the case.

**Dave Jones:** So, you can't really, once you lay this thing down on the board, these pads are not directly accessible with the soldering iron. So, really these chips are only designed for a reflow soldering process.

**Dave Jones:** They're not really designed for hand soldering. So, that's why today I'm going to actually flip it upside down like this and then I'm going to individually wire tiny little bond wires over to my prototyping area here.

**Dave Jones:** So, I'm going to sit it on here and I'm going to wire all the individual pads over to a larger footprint, which then I can um access via hand soldering.

**Dave Jones:** This is an example of dead bug style construction. Now, the term dead bug actually comes from um actually turning something like a DIP package upside down on its back like that and it looks like a bug with its legs on its back dead with its legs sticking up in the air like that.

**Dave Jones:** And that's where the term comes from. So, even though this little LGA package does not have uh legs sticking up in the air, you would still I would still call this dead bug style construction.

**Dave Jones:** So, you flip it on the back, you actually glue it down, and then you individually solder almost like um almost like what's what happens inside an IC itself. They and the machines automatically insert bond automatically wire in little bond wires to the pads, which go out.

**Dave Jones:** If you actually opened one of these uh DIP chips, inside you will find like a silicon uh a silicon die like that with little bond wires going out to these larger legs.

**Dave Jones:** And that's pretty much exactly what we're going to do here today. Now, I'm pretty confident of doing this one because it has a 0.8 mm pin-to-pin pitch. And that's uh reasonably large.

**Dave Jones:** The pads on there are reasonably large in the scheme of things. So, I shouldn't really have too much trouble, I don't think, um actually wiring this one up. It we should be able to do it reasonably easily using a bit of magnification.

**Dave Jones:** I could probably do it by eye as well, but we'll actually use some magnification today. Just start 2 and 1/2 times or something like that, just to help us in actually soldering onto the pads and making sure we don't short things out.

**Dave Jones:** And there's the device that we're going to solder. It's the MMA7455 3-axis accelerometer. It's from a Freescale, and that's the LLG-14 pin package. Now, as you can see, over in that little the bottom left corner there, it does have a little pin one marker.

**Dave Jones:** It's important for us to actually get that correct when we flip it over, so we know exactly what pin's what. It seems to have another little marker there, if you can see it, which indicates that it's the same side, but you just have to remember which one is actually pin one.

**Dave Jones:** Okay, we want to add a tiny little drop of super glue down in here, just so that we can hold that chip in place. There we go. We've just tacked that in place.

**Dave Jones:** It this stuff sets almost instantly, of course, so you've got to be very, very careful, but that will just hold our chip in place while we solder it, because you don't want the thing moving around.

**Dave Jones:** Okay, the first thing I'm going to do is I'm going to apply some flux from this flux pen just across the main pads there, and also on top of the device as well, just so we can get some good wetting onto those pads.

**Dave Jones:** And what I'm going to use to make the connections is some wire wrapping wire, solid core 30 AWG tinned wire. And this is really useful stuff. I highly recommend you get some.

**Dave Jones:** It's not fine. It's great for uh mods like this. And in fact, it is called a uh mod wire. And it comes in various colors. And uh there's the actual um it's an OK Industries uh brand 130 AWG.

**Dave Jones:** And using my chisel point iron and my 0.46 mm solder, I'm going to tin these pads. Um I've already tinned a couple, and that didn't uh unfortunately, I didn't press the record button.

**Dave Jones:** Oops. And uh this is not my finest work because I am trying to do this under the under the uh camera. So, the angle of the iron is not um ideal to how I'd normally do it, but uh you can just tin these pads like that.

**Dave Jones:** And then we will um solder the wires, each individual bond wire onto those, and take them out to the individual pads. Let's try and solder a wire onto there.

**Dave Jones:** Um it can pay it can pay you to actually tin these wires first um just so that they uh wet a bit better. But there you go. That first one is attached.

**Dave Jones:** And then we'll just get in there and we'll actually uh cut that. And we'll get in and we'll push that down so it contacts one of the pads. Let's say that one there, and then this one will go to that pad, that one will go to that pad, and so forth.

**Dave Jones:** I need to add some more solder to these pads in here because it the last process just uh sucked a fair bit of that away. So, we'll get in here with our wire again.

**Dave Jones:** And I'm doing all this through the camera LCD. I can't actually uh see the board here. So, this would just be just like working under a microscope, really. Except, I haven't got much in the way of magnification here, but there we go.

**Dave Jones:** Now, what I'm going to do here is I'm going to tin the uh wire cuz this is a fairly uh fairly important uh step. Although, this is already tinned copper wire, um really that uh you got to add some flux on there, clean it, get some fresh solder on there to just to make sure it really takes.

**Dave Jones:** And after I do that, I clean my iron on my sponge. And hopefully, if there's enough solder on the uh pad on the chip, that will be enough to reflow onto my what my already tinned wire.

**Dave Jones:** And yep, there it goes. There. Made an attachment, nice and quick, easy, and a good quality joint. And this one here, I've got to bend a bit further over.

**Dave Jones:** And don't bend it down directly cuz you don't want these to short cuz they aren't insulated uh wires, but it's uh pretty easy to solder them onto a smaller um well, a larger, sorry, uh diameter um pad.

**Dave Jones:** So, later on, I will actually solder uh flying leads directly off these pads here onto my PIC chip. And there's my completed dead bug chip. It's uh not my finest uh work.

**Dave Jones:** It is surprisingly difficult um to do on on a shallow angle when you've got the camera in the way, but uh bit harder than usual, but that only took me like 5 minutes or something like that.

**Dave Jones:** It wasn't hard at all. And I've now converted that um in um LGA package chip into a much more uh usable pitch that I can actually come along and now um solder on some of this uh mod wire.

**Dave Jones:** I'll just uh solder them onto each of those and then over to the specific pin on the PIC chip which I need. Simple. So, that should work a treat.

**Dave Jones:** Uh I'll have to do some um more uh up close uh visual inspections under the microscope, but that looks fine to me.
