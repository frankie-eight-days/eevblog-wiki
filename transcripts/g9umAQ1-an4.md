---
video_id: g9umAQ1-an4
title: EEVblog #849 - Sony E-Mount Camera Lens Teardown
url: https://www.youtube.com/watch?v=g9umAQ1-an4
source: youtube-asr
---

**Dave Jones:** Hi, welcome to a hopefully short teardown of this Sony E-mount lens here. This is from my NEX-5T camera. I've been having issues with it. As you can probably see in there, it's got a little bit of uh sand and crud and all sorts of

**Dave Jones:** stuff. I've been actually getting an error message on the uh screen when it boots up saying it can't actually talk to the lens. And of course through the uh Sony E-mount system here. And but I don't think that's the problem because it feels

**Dave Jones:** Trust me, this is not feel-a-vision, but that feels pretty crusty. I think it's been to the beach one too many times and been to one too many canyons and other things and it's just yeah, I think it's stuck. And that's what's causing the

**Dave Jones:** error message. So, I thought we'd actually tear apart one of these things and have a look inside. I don't think I might would bother. I'd probably maybe clean it out and lube it up perhaps and put it back into

**Dave Jones:** condition, but these things are a reasonably cheap and um So, yeah, I'm not sure if I'd I'd bother. It's not a spectacular lens by the way, but it is very like in terms of performance, but it is very compact. And

**Dave Jones:** when you mount it on the Sony NEX-5T camera, it you know, it really is a nice little package and I've shot quite a few field videos using that camera you've seen on the blog using this lens. So, it

**Dave Jones:** really is quite a jazzy little thing. So, yeah, it's got a it's got power and comms of course to uh talk to the camera and it's multi-element and all that sort of jazz, but I've never taken apart a lens

**Dave Jones:** before. So, I thought it might be interesting. I know you lens aficionados out there know exactly what's inside these things, but I have never taken one apart. So, there's four screws and well, I'm going to give it a go. Not sure how

**Dave Jones:** easy it does extend out of course and that's the thing that gets jammed. So, I believe it actually gets jammed up because there's sand and all sorts of crud in there and and then it throws up an error message. It says it can't talk

**Dave Jones:** to the lens rather than, you know, lens jam or something, but I have been able to like pull it back out manually while the power's on and it, you know, and get it to work occasionally, but yeah, I've had now one too many times

**Dave Jones:** where I've taken this somewhere and it just simply refuses to work. So, yes, it's I've lost all trust in it. But anyway, let's take it apart. And the lens we're looking at is the SELP1650. It's like the kit lens which comes with

**Dave Jones:** a lot of NEX 5T and other model cameras with the E-mount. So, I'm not exactly sure what the pinout and interface is here. I haven't looked, but I might have a quick Google on that before when I edit this thing and I'll uh

**Dave Jones:** put it up, but uh some sort of, you know, maybe I2C serial interface or something. It's just got to, you know, it doesn't have to transfer a lot of uh data, so just be some interface like that or

**Dave Jones:** maybe a spy bus or something perhaps, but not sure how easily these come apart or how they or how repairable they are. I guess, you know, you wouldn't bother repairing this lens. You can get these pretty cheap, but you know, more

**Dave Jones:** expensive lenses, you can get them serviced and that sort of jazz, I believe, so let's Oh, we're in like Flynn. We're in like Flynn. Look at that. Oh, straight in. Beauty. So, let's take a look at some stuff here. We've got a

**Dave Jones:** flat flex for the E-mount uh pogo pins in there. Well, no, they're not pogo pins. They're Yeah, pogo pins on the camera, but little contacts on there. So, that's going in, flat flex going over to the board here. We've got

**Dave Jones:** a large flat flex, large pin count flat flex headed off here. So, I'm not sure what that's uh well, that's obviously going to all the other uh sensors and mate, are there any further motors in there or is there only the one motor on

**Dave Jones:** the top here? Anyway, let's have a look. Don't know what that puppy is off hand. I'll have to look that up. Could be some sort of custom job. This thing is interesting. This little ceramic package here. I'm not sure what that's doing.

**Dave Jones:** It's not me, you know, I first thought, oh, it's an oscillator, but no, no, there's our oscillator down in there. But that's interesting. Let's take a look at the oscillator. Okay, can someone please explain to me why we need

**Dave Jones:** a 54 megahertz oscillator in here? It's a bloody lens. What does it have to do? It just controls the elements and it it's slow as a wet week at that. So, what the 54 meg? Geez. And I Google that number

**Dave Jones:** on the top and I get a Renesas part. So, yeah, Renesas micro, something like that. You know, renumbered, something peculiar. Made in Japan, of course, Renesas stuff is made in Japan, so that makes sense. So, yeah, some sort of

**Dave Jones:** probably Joe Blog's Renesas micro. Can see some more screws around here. So, I think this is going to actually come out uh in several modules. It should come out quite nicely. But anyway, here's the first of our motor here, which looks

**Dave Jones:** like it maybe drives this cog around here. Of course, the whole thing, as I said, the whole thing extends out. So, there's going to be some sort of like a worm, you know, small counter worm drive on the inner

**Dave Jones:** mechanism in there, which for want of a better term, I don't know my lens terminology and things like that, so you will have to please forgive me, but um yeah, anyway, I there's probably another Is there another motor in there

**Dave Jones:** somewhere, perhaps? Anyway, we'll find out. And you can clearly see the pin out on here. These two thick traces here, obviously the power. I don't know, what is it, 5 volts or 3.3 or something like that going over and then the rest are

**Dave Jones:** just signal wires. I've got the board out. There's another chippy on that side. We'll have a squeeze at that and we can see the flat flex here that uh big multi-trace one. Look at that. I don't know. Count the number of traces

**Dave Jones:** on that puppy in HD if you want and that just that folds back under like that. Really is quite complicated. They've gone to a lot of effort so it might be going they might be splitting that off into multiple lengths and levels going

**Dave Jones:** down into different uh part and different sensors down in different parts of the lens and the lens. F52108, I have no idea what that puppy is. Maybe another uh micro perhaps. Why they need two, I'm a bit uh surprised to find two

**Dave Jones:** large BGA devices in here. Anyway, that one's running at a much more sensible 12 MHz but still jeez, what does this thing have to do? And there's that motor assembly. It's got a cog on the bottom of there so

**Dave Jones:** some sort of reduction drive gear in there and then that obviously goes down into there and it drives our ring. And just as I was wondering how this all comes out, it sort of slid out on its own like that. You can see these

**Dave Jones:** guides in there like that. There's one there. There's one down there and there's one down there as well and but it doesn't pop out any further than that. That's it. So not sure what the go is. Uh okay, what

**Dave Jones:** I'm going to do is probe its ass. Here we go. Um this little motor in here, I'm I've just put in a two screws back in there just to hold that uh the whole thing from sliding in place and I'm just going to

**Dave Jones:** because the board's out, we can apply voltage to the motor. I have no idea about the polarity. I have no idea what it's going to do. I presume it's going to try and move the whole thing um out, extend the lens. So, uh let's

**Dave Jones:** give it a go. Um I'm assuming like 3 V is going to be like one of a low voltage motor. So, I've got Yeah, I got about 3 V set on the supply. So, let's give it a burl and uh

**Dave Jones:** see what she does. Here we go. Oh, there we go. Yeah, look. Hey, woah! Woohoo! Yay! Let's go back.

**Dave Jones:** There we go. Wow! Terrific. Now, you saw there how it was like a multi uh step thing. You know, this starts extending out, then the other, then the inner one comes back, and it all That's how they get the

**Dave Jones:** real compact uh the compact lens configuration like this. Oh, there we go. It's super quick. Okay, I haven't put all the uh screws back in. I think it's a bit loosey-goosey. But, you can see how it uh certainly extends a whole lot. It's

**Dave Jones:** really interesting because I didn't This outer part here, I didn't actually see any uh worm drive in the outer plastic. This part here, I mean, obviously there's nothing in here cuz otherwise you'd be able to see it. So, it's obviously doing

**Dave Jones:** that from the inside, some sort of inner ring in there which is uh doing the business. That pulls that one in and out cuz there's nothing on the surface of this, and there's nothing on the inner surface of this one here to actually

**Dave Jones:** drive this. So, it must be coming from this center part, uh the center uh part down in the lens here. And yep, I can really see it and feel it here now when I try and move this back into place

**Dave Jones:** like this to line up these screw holes here. Pull that out and that just spins around like that. So Wow. Fascinating. Imagine designing this thing. Absolutely incredible amount of engineering's gone into making these sort of Well, they're not pancake lenses, but

**Dave Jones:** very narrow compact lenses like that. I'm sure it's order of magnitude more difficult to make these that sort of fold in on themselves rather than just, you know, your more traditional lens which just goes from one stop to

**Dave Jones:** the, you know, one end stop to the next. I think now it's getting to the point where if you don't know the exact disassembly procedure for this or assembly procedure which you could reverse, then uh you could come a gutser here

**Dave Jones:** real easy. It's getting It's getting quite tricky real fast. Anyway, I don't consider this I'm not, you know, fussed if I actually can't get this back together. So Yep, it's just might be a sacrificial teardown. And yeah, I'd recommend you

**Dave Jones:** don't go playing around with that motor because I've had to put it back in the fully retracted position that internal barrel there before I now take the screws back out and drop it back out and figure out how to separate

**Dave Jones:** the two. So from what I can see, as I said before, there's three of these guides down here and there seems to be little clips or, you know, like sort of pins or something holding those in. So I've got to somehow

**Dave Jones:** get those out and it maybe you just like lift get under here and lift or something like that perhaps. Let me try that. Oh yeah, there you go. I got one of them out. Yep, there we go. I think

**Dave Jones:** that's the trick. You just have to get them out. Maybe maybe not one at a time, maybe all three at once. I need multiple hands. Ta-da! That's easy once you know how. And you missed it, but I I just operated

**Dave Jones:** the motor and oops! It's come apart. But that's obviously how it does it. See, there you go. There's the internal as I suspected there'd be something like a not a worm drive, but there's actually a complicated arrangement and that

**Dave Jones:** actually uh is what does the multiple uh you know, zooming and compacting of the lens. So, that's really quite fascinating. But yeah, um the motor went really quick and it just accelerated and went boop! And uh came off. Whoa! Now, yep, it's coming

**Dave Jones:** off in multiple parts now. Got multiple stages here. Very very interesting. As you saw, there's nothing on the inside of that barrel. It's just, you know, really an outer retaining clip which just holds the back here and this is the

**Dave Jones:** this is the whole part which extends out. Okay, so we have There we go. There's the uh the front lens. So, it's just a fixed it's just a fixed lens. Doesn't do anything at all. Looks like a fair bit

**Dave Jones:** of glass in there. Actually looks pretty thick. Um that's it's hard to see on the camera. It's hard to get a feel for it unless you've got uh unless you're looking at it in 3D like I am. But yeah, that's a

**Dave Jones:** thick bit of glass and then this is behind it. So, here's the next part. Can see a little motor in there. So, it drives that inner Whoop! There's the inner Whoa, there's the inner part. We're really coming apart now. There we go.

**Dave Jones:** Look at that. And this is as we saw before, as I suspected, it looks like this is the one piece of flat flex which then that's why they had so many connections on it because it went to multiple levels of

**Dave Jones:** the lens as I expected. See? So, it it when goes through there and then pops out the other side here. So, this is why this one had so many connections on it. Count them. is because they snake their way off. And

**Dave Jones:** this is why this one has to be bent, of course, because it's compliant. So, when the lens zooms lens zooms in and out. And so, it's got to break off to motor down in here. So, there's motor at the top which drives the whole

**Dave Jones:** lot. Looks like there's a second one. Is there? Down in there? It's a second one down in there. Yeah. Oh, a second something down in there. There's definitely a uh third looks like a third motor over on that side there. So, wow.

**Dave Jones:** Complicated beast. Unbelievable. Multi-stage mechanism. How do you design this? Wow. Hats off to the designers. Really, that is awesome. Actually, I wasn't 100% correct on the uh flat flex going all the way with LBJ there. It's uh you can

**Dave Jones:** see that this rotate this inner barrel here rotates. All right. So, that one rotates a little bit. You can see there's another flat flex connector down in there. So, that So, the one that comes from the top board actually comes down here and just

**Dave Jones:** terminates to another board down in here. I guess that makes sense cuz this is going to be a whole uh assembly um you know, this is going to be a whole manufacturing uh step just for this uh first or second lens assembly here.

**Dave Jones:** So, but that can obviously travel back and forth in there. All right. And I had completely forgotten that this lens actually has image stabilization. So, of Of here we go. Look, here it is. We can see this mountain here. This is the Sony

**Dave Jones:** SteadyShot, and this is what this flat flex goes over here for. So, there's no what that the tiny little motors there and there which drive the XY plane on that lens there. There we go. Like at at high frequency. So, that's that's

**Dave Jones:** what all the processing is doing. That's why they need all the granny processor. Of course, I didn't realize they're doing that in the lens. They're not doing that in the um uh the main processor in the camera. That image stabilization must be

**Dave Jones:** happening in the lens there. You know, the actual processing of it and the correction. This is all high frequency. This You know, these things operate at kilohertz or something like that. They're You know, they're really quite uh quite high frequency in terms of You

**Dave Jones:** know, being able to position this lens. So, you know, at least hundreds of hertz. And I'd love to be able to demo that, but uh yeah, like hooking all into there and You know, you'd really actually have to

**Dave Jones:** um you know, power the entire lens up really um in its You know, disassembled state like this and and plug it into the You know, the front of the camera and everything else and actually have it uh and have it actually control that cuz I

**Dave Jones:** don't think it's enough just to apply power to the thing. Anyway, that's fun. Look at that. Okay, so now we can see the lens system in order. We have our front lens here, which is just a fixed thick bit of

**Dave Jones:** glass, and then that goes into another fixed one here, and then on the back of that, we have the Sony SteadyShot lens that actually corrects for uh uh stabilization, and then up under here the output of that, you can see it fall

**Dave Jones:** away. Hang on. If Yep. I can't push it back. But hang on. I'll let it fall under gravity, and you can see that it's all the way out here. There you go. It's all the way out, and watch it drop

**Dave Jones:** in. Watch it drop in. Watch it drop. There we go. It drops in. And there is the There is the magnet in there that it slides along. And then finally, on the back side of that is the final fixed

**Dave Jones:** lens, and that's the last one, and that's the one that focuses on the APSC size sensor inside the camera. So that there is a real interesting slider arrangement. Look at that. That really is quite neat, like a linear

**Dave Jones:** slider. So that That is not a motor as such. They're going to position that based on that permanent magnet right in there. And there it is. You can see it. There's the magnet down in there. That's obviously the drive, and it looks like

**Dave Jones:** they have some sort of positional sensor feedback in there to know exactly where it is. That's interesting. Now, I was a little bit medieval before driving that main lens zoom motor. Just, you know, whacking it up to the 3.3 V power

**Dave Jones:** supply. That was a bit rude. So I've now got a 1 Hz sine wave coming from my function gen, and I'm going to probe the motor on this thing. See if it does anything. Let's have a go. Once again, I have no idea

**Dave Jones:** what this is going to do. Hang on. I'm presuming it's the motor. So let's give it a whirl. All right. Here we go. I've got it set to 2 Hz. Let's give this a go. Sorry, it's tricky to get these bloody probes on here.

**Dave Jones:** There we go. That's 2 volts RMS at uh 2 hertz sine wave and you can see it just oscillating there. Nice. There you go. You can really see the coil in there on top of this fixed permanent magnet. So, you can see that

**Dave Jones:** the coil can go woohoo. Look at that. That's fun. So, yeah, they've obviously got coil inside there like that. Multi-turns, you know, what is it there like I don't know, 20 30 turns on there or something. And uh

**Dave Jones:** that is good enough to actually position this thing across there. Oh, and I forgot to show you in addition to the uh zoom guide mechanism out here, you can see how it sort of, you know, the pin in

**Dave Jones:** that can go in there and then ride that slot. So, you can see how it can go back and then forward and then back again, have that particular pattern. Well, there's also one on the inside here as well just to allow

**Dave Jones:** Yep, there we go. It just rotates that. There's a little on the inner side right in there in the ring, there's a little uh uh similar sort of but not as complex guide as that one. You should be able to

**Dave Jones:** see that snaking its way around in there. And that has a guide pin on it on the top there. So, that goes into there like Hang on. Where does it go into? Goes into Does it go into that slot? Yeah, it goes into

**Dave Jones:** that slot and then rotates in like that. Beautiful. And here it is all assembled back on the camera. Well, kinda. Um I've attached I had to screw the ring back in there so I could get um some rotational

**Dave Jones:** force to actually lock it into the metal uh clamping uh ring the E-mount ring around the outside there. And I'm going to foolishly power it up. Unfortunately, uh like the control here on the outer ring is not hooked up. So, I'm hoping

**Dave Jones:** So, that's the encoder for there plus that ring. I'm hoping that that's not needed and it will actually do something when it powers up, but I don't know. Will we see the lens the optical steady shot thing work? Will

**Dave Jones:** we see this coming and out? I don't know. Let's power it up. All right, here we go. Let's get in here. And here we go. Will it do anything? Yep. There we go. Hey, it's rotating. Oh. That's great.

**Dave Jones:** And it's more difficult to move that lens now. It's more difficult. I probably shouldn't because I'd be probably back feeding the motor drive, but that is really quite That's really quite stiff now. So, you know, I can still move it, but it's

**Dave Jones:** not loosey-goosey like it was before. It's definitely energized up. You can see that there's actually no error there. So, that's It's really quite good. Of course, there's nothing coming through the uh through the lens unless I stick my

**Dave Jones:** finger in there and block out some light. But, I don't want to stick my finger right in and uh touch the sensor, of course. That would be really really bad. But, let's You can see the the iris in there as well.

**Dave Jones:** Sorry, I missed that. There's our iris motor. There it is. So, that's driving the iris inside there. Let's see if we can get a close-up of the iris. Okay, you can see the iris changing there. Maybe if I stick my finger in front.

**Dave Jones:** I don't know where it's doing the metering for that, but let's power it. Let's maybe take a photo. There we go. There we go. Push the shutter button down. And you can see the iris blade moving in there.

**Dave Jones:** There we go. Just took a photo. Try and show you that iris up close. There we go. Press the shutter button. Comes in a little bit. Let me block out some more or allow some more light in, sorry.

**Dave Jones:** There we go. I'm tilting What I'm doing is tilting the camera up to the lights here. So, it's getting more light coming in and you can really see that how many blades is that iris? There you go. And I tilt the camera back

**Dave Jones:** down. Or put my hand in front of it, cover it a bit, and there you go. Iris goes wider. Now, watch this. I can actually show you the SteadyShot system working. What I'm doing now is I'm actually recording a

**Dave Jones:** video. Okay, so it's live. It doesn't work if I don't record a video. So, of course, as I as I showed, the sensor is actually on the top board here, I believe. So, let's actually watch this mechanism down here. If I shake it like

**Dave Jones:** that, it does nothing. Okay, because there's no accelerometer in there. But, oh, look. I just have to start wobbling the camera. Wobbling the camera a little bit and and look, I'll actually pick it up and start shaking it around. And there you go. You

**Dave Jones:** can see the SteadyShot. That's great. You can see it it wobble. Here you go. I'll get closer. Wow. And that's not a vibration coming through the desk or anything like that. I've got it off the desk. That is

**Dave Jones:** That is the drives doing that. And I move it slowly around. That's the SteadyShot system at work. Good stuff. Look. You can see the You can see the travel on these little guides. Guides in here. Look at that.

**Dave Jones:** There we go. Wow. Haha. That's great. I could play with this all day. So, there you go. I hope you enjoyed that teardown of this Sony lens. And it really is quite amazing engineering that goes into these things.

**Dave Jones:** I Wow, you know, my hat's off to the designers of this thing. I'd love to know the design team behind just a lens like this because you got to have the optical people figuring out, you know, the the irises and the lenses, you know, you

**Dave Jones:** got to have the lens people, you got to have the people who are figuring out the you know, the correct focal lengths and all that you know, just grinding the glass and getting all that right is an art in itself, let alone

**Dave Jones:** getting all the zoom drive mechanism across the top here and inside. Oh, you can see it move. There we go. It moved. It moved. Woohoo! Still alive. It's alive. And the iris and just everything else that goes into of

**Dave Jones:** course the optical steady shot system is, you know, absolutely amazing technology in itself. So, if you like the video, please give it a big thumbs up and all that sort of jazz. And if you want to discuss it,

**Dave Jones:** comments down below, EV blog forum, all that sort of stuff. Thank you to my Patreon supporters. If you want to help support the channel, Patreon link down below. Catch you next time.
