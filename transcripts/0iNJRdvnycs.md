---
video_id: 0iNJRdvnycs
title: EEVblog #330 - Medela Swing Teardown & Repair
url: https://www.youtube.com/watch?v=0iNJRdvnycs
source: youtube-asr
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. I was going to do something entirely different today, but at the last minute something turned up for repair here in the lab and I thought, well, might as well do a teardown as well because I don't think

**Dave Jones:** we've had a Swiss or a teardown of something made in Switzerland before. So, hi to all my Swiss viewers. And I like to keep abreast of different technologies, so we've got a breast pump. It's a Medela Swing breast pump.

**Dave Jones:** Yes, cue the jokes, but I don't expect it to be terribly exciting inside. There'll be a motor with a microcontroller to control it, battery powered, and that's about it. But I thought we'd see what's inside this Swiss-made breast pump and see if

**Dave Jones:** we can fix it. You know what we say around the EV blog, don't turn it on because we can't take it apart. And here it is, it's the Medela Swing and this brand Medela is supposed to be the, you

**Dave Jones:** know, the dark scuts. This is supposed to be the Fluke 87 of breast pumps. I guess you could say that sort of, you know, the de facto industry standard. It's got a tube here which attaches to the suction cup which goes, you know

**Dave Jones:** where, and it's made and designed and made in Switzerland. And it's got four soft buttons here on the top, LED, power, up and down, and I'm not sure what that one does. No idea. Sorry, I don't go into the details of how this

**Dave Jones:** thing works. And it's a rather neat, you know, rather neat little shape and it actually contains the battery compartment here on the bottom. It's got a nice sort of three rubber, you know, feet on the bottom molded in

**Dave Jones:** as one big circular ring like that. It's got a belt clip attachment and and this just comes out like that. So, that's just a a friction fit rubber hose there and it's got all the requisite marks on the bottom the UL

**Dave Jones:** stuff you know double insulated all that sort of jazz and B double AR not sure what that is but designed and made in Switzerland and it I guess it conjures up you know images of this thing being designed in some mountain hut

**Dave Jones:** you know at the base of the foothills of the Swiss Alps or something like that I don't know. And if you just lift off the battery cover here it's got the four rechargeable batteries in here standard double A's and nice big finger holes in

**Dave Jones:** there you can just pull them out I really like that you know it it really works quite well because you have to change these things every day or two they don't last all that long you know a couple of days at most or something like

**Dave Jones:** that and it looks like there's a um there's an air inlet there and it looks like that is let's have a look at that. Aha another one looks like that's some sort of filter possibly something like that so there's

**Dave Jones:** two um well I presume they're you know well outlets sorry for you know sucking the air out so anyway there's two screws here we can take those off and uh we can I presume it'll just lift off like that and I expect there to be you

**Dave Jones:** know a motor in there with the suction mechanism that won't be very exciting I don't really want to I don't really care about that more interested in the circuitry why it's failed actually because it actually does absolutely nothing the

**Dave Jones:** power doesn't turn on yes the batteries are good so you know I really want to find out why this thing has failed.

**Dave Jones:** And let's have a look at what we've got here. I expect it to somehow separate. Oh, yeah. Yeah. Oh, wait. Yep, no problems whatsoever. Oh, look at that. Isn't that Isn't that neat? I rather like that. Look at the cable management

**Dave Jones:** in there. They've really there's that's not one That's not some slapped-together one-hung-low cheapy, that's for sure. And as you'd expect, you know, this thing is you know, the the you know, the top-notch, the duck's guts, Rolls-Royce of breast pumps. So, that's rather

**Dave Jones:** There's the Yeah, there's the rubber membrane on there. We've got three carbonized uh conductive contacts there. Nice, they've put three. And that looks like really good quality gold plating on that board, too. They've got white solder mask on

**Dave Jones:** it. But the gold plating looks thick and high-quality, as you'd expect. But what I really like here is this cable management. Look, it's all molded. This is all looks like one big molded plastic piece. And they've gone to the effort to mold in all the

**Dave Jones:** individual stress retainers there and cut management for the individual wires coming out. They've cut them all to the exact length. Look at that, they've put little hooks under there to you know, so that they're actually you know, so that the wire

**Dave Jones:** doesn't flap around, so it doesn't get caught when you put the when you put the top on and get pinched and things like that. I've seen so many products fall down in that area, actually, where they just have loose wires running all over

**Dave Jones:** the place. And then when you assemble the thing, they get pinched or, you know, uh it's just uh horrible, but this one is beautiful. Look, it's exact length. There's another cable management hook there. Lovely. Aw, man. It's beautiful. I really I just love

**Dave Jones:** that from a cable management perspective. They put a lot of effort. There's There's another one down in there, little you know, little pinch in there and there to keep the cable in place. Beautiful. Aw. And also, clearly what they've got is

**Dave Jones:** there's the LED in the center of the board there. You can see that. That That's a reverse mount LED, exactly like I have on my microcurrent, if you've you've seen my microcurrent, no doubt. There we go. It's got a reverse mount

**Dave Jones:** LED on it, poking through the well, what this you call the front side of the board, I guess, with all the components mounted on the back. And that just does shine through and uses the rubber here as a little light pipe

**Dave Jones:** kind of thing. So, it just shines out there. They've got the alignment holes there. They've got three of them. They haven't got There's not four, so you It's not like you can accidentally assemble it the wrong way and waste time

**Dave Jones:** in production cuz somebody, you know, assembled it back to front, or it even ships out B and, you know, the plus button becomes the power button or something like that. That That That would be a trap, actually, for when you

**Dave Jones:** have a symmetrical design like this, if you do have your three keys, you know, your little key holes mounted like that, this could be mounted any way, you know, if you had four of them. Eh, could fail dismally, but anyway, let's

**Dave Jones:** I assume the board just pops. Yes, it does. Just pops out. Tada. And just the board mounting is all molded into the one big plastic case. This is really beautiful, really solid, and the PCB supports are also molded in to there

**Dave Jones:** as well. This is great stuff and there's the cable management pass. Well, what we're interested in is the board and that's pretty much what I expected. We've clearly got a main micro controller here. We'll take a look at these in more

**Dave Jones:** detail. Another SO8 package a six-pin slot 23 there a couple of diodes and one big uh tantalum surface mount tantalum there another diode in there a few odd passives and I love the programming port here. This is clearly like a uh

**Dave Jones:** JTAG or an in-circuit serial programming port for the micro controller so they can screw this thing in unprogrammed and then during production uh process of this thing they can just plug up there hook hook up their little custom-made uh

**Dave Jones:** you know probe thing here and and just program this thing and do in-circuit testing maybe as well or you know run some operational tests or things like that. So um yeah, whatever it's something on on here has failed by the way. I'm not sure what

**Dave Jones:** it's certainly not the wiring. It's not like a you know wiring's come loose or anything. These are all hand soldered onto here but they look hand soldered on beautifully as you'd expect in this Swiss made you know someone in the Swiss

**Dave Jones:** Alps is there rubbing rubbing their gray beard and they're soldering each one at the right tongue angle. Beautiful. Anyway, the quality of construction is excellent. Let's take a look in some more detail. Now one of the first things

**Dave Jones:** I see I just went aha. This little sucker down here. We zoom in on this because we're going to I'll look at the components later other components but this immediately drew my eye. It's got 1.5 written on the side of it,

**Dave Jones:** and for all the world, that little puppy there looks like a surface mount fuse. 1.5 amps, presumably. And I think there's a very high likelihood that fuse is popped. And you can tell it's an input fuse here because red and

**Dave Jones:** black, of course they uh would come from the power, and they do. If they come directly from the battery, if you follow the uh wiring on the inside of the thing. We've got a diode here, probably uh in series or reverse protection. I'm

**Dave Jones:** going to have to um check out the uh traces on there. Bit hard to see the traces with this white solder mask on here. One of the disadvantage with disadvantages with uh white and black uh solder masks. Um they're you know, they

**Dave Jones:** can be difficult to see the traces through there. Makes it, you know, harder to reverse engineer and trace things out when you're troubleshooting like this. But considering that uh absolutely nothing happens to this thing um when we attempt to turn it on, it's likely that

**Dave Jones:** uh something has gone wrong there. And there's no obvious signs of uh failure anywhere else. But look at that. Medela. They've got their own branded chip there. And of course they wouldn't have designed, you know, it's not going

**Dave Jones:** to be an ASIC. I greatly doubt it. It's just going to be an off-the-shelf micro controller, I would presume, which they've uh you know, they ordered so many of them, they just got them custom branded direct from the manufacturer.

**Dave Jones:** And uh let's have a look at what what this SO8 is. Perhaps an E squared prom or something like that. And no surprises at all. 24C 01, is it? Clearly an E squared external E squared prom for holding that various

**Dave Jones:** uh settings. And that means that they've used a really low-cost micro controller here. You know, it's not going to be a pic or an like a you know, a new model pic or an Atmel that has built-in e-squared prom or something like that.

**Dave Jones:** It's going to be, you know, a real cheap you know, 8051 or some other obscure brand and it's a sweep elsewhere around the board. They've used large footprints there for the components. Really nice. You can get in there and probe those

**Dave Jones:** beautifully. I like that rather than little tiny footprints cuz they're not you know, this is not a dense layout so they don't really need to do that. There's the there's a 100 mic 10 volt tantalum and a couple of sot 23s. They're

**Dave Jones:** probably transistors. There's another six-pin sot 23 up there. Don't know what that is. Could be a voltage regulator or some such. Not sure although why it would be all the way on the other from the the other side of the

**Dave Jones:** board from the battery input here, I don't know. Actually, I don't see a voltage regulator around the input. Oh, I know, it's probably there. There it is. Sorry. That one there is probably a voltage regulator. So your power

**Dave Jones:** probably comes over here, flows over to your voltage regulator and uh that's that. And they've got it curiously they've got a mouth resistor here, a mouth package resistor whereas in all the rest of it they're just use standard

**Dave Jones:** you know, 0805 package resistors but they've just got one which is a mouth and clearly they've gone for that mouth package because it's physically bigger and will have a bigger power dissipation. So you know, instead of using a big like a 1206 or even a

**Dave Jones:** bigger regular surface mount package, they've gone for a one of the old style mouths which you don't see much anymore. so that's probably a current um sense resistor for the motor, so it can you know, so the software can actually

**Dave Jones:** monitor how much current is flowing through the motor. So they that would dissipate you know, a fair bit of power more than a little 0805 or something like that could tolerate. So they've engineered in a larger physical package. And on second

**Dave Jones:** look, that's actually 6.8 ohms and there it doesn't seem to be used as a current sense one. I can't see any sense lines actually coming off that. So it just looks like it's a series resistor there. And there's your reverse mount LED sort

**Dave Jones:** of in a reverse goal wing type package and that just shines through the hole in the board. Easy. There's a little bit of residue left on the hand solder joints there, but they look fine and there's no obvious signs of

**Dave Jones:** distress in the component. I don't see any blow holes, you know, it's not like the you know, something is charred and I've given it the smell test and I can't uh smell anything wrong with it, so I'm going to

**Dave Jones:** I think I'll bet my bottom dollar that fuse has popped. All right, so let's have a look at that and get in here and probe it.

**Dave Jones:** Bang. There we go. That was my finger there. And yep, it is popped. I That is I'm pretty darn sure that's a fuse and it is open. And by the looks of the traces on there, this is a reverse protection

**Dave Jones:** diode after the fuse there. So the negative So the negative will be on the top side here after the fuse. So it basically got the positive power coming in through the fuse and then So, this is the rail part here and then this reverse

**Dave Jones:** protection diode here. So, the negative will be on this side. So, let's probe this and see if this is popped. No, there we go. It's still 0.45 V. Not a problem. And if we do a Dave CAD drawing here,

**Dave Jones:** we've got our battery input like this, positive on the top side, going through a 1.5 amp fuse. Pretty sure it's 1.5 amps cuz 1.5 is written on there and that will then have a reverse protection diode going to ground like

**Dave Jones:** that. So, if you plug this battery in back to front, if you end up with if you have the positive here and the negative up here, then we'll get current flowing through the diode and then your circuitry over here is only going to get

**Dave Jones:** a maximum of, you know, 0.4 V. That'll probably be a Schottky or a something like that. 0.4 V. So, your circuitry is all protected. Um and you're going to get a high current flow through like that because this thing is powered from

**Dave Jones:** rechargeable batteries. So, um they're capable of delivering large amounts of current that would certainly exceed 1.5 amps. So, if you put them in backwards, you're going to pop your fuse and all your circuitry's protected, of course, but then well, what? You've popped your

**Dave Jones:** surface mount fuse. So, I don't know why they didn't like use a resettable poly switch there or something like that. It certainly looks like a one-off fuse, but in in any case, it's certainly a failed. That's gone open circuit, which is why

**Dave Jones:** our thing doesn't work at all. So, um I don't know if it's, you know, human error they put the batteries in backwards and this thing is just cactus. And if that's the case, then that's bad design. Um, really, you know, I mean, it

**Dave Jones:** should only be for gross overloads of the load or something like that. Um, it shouldn't uh blow when you just insert the batteries the wrong way around. That's crazy. So, usually to overcome that, of course, you just have

**Dave Jones:** a standard uh series diode in there like that. And then And then that goes to your load internally. And then if you reverse the batteries here, no current flows at all cuz current can't flow back through the diode, and oh, it's fixed. But they

**Dave Jones:** haven't. They've used a reverse protection diode. Hmm. Now, the big question is, of course, what caused the fuse to blow? Was it something in the circuitry? Has the motor done something that's caused that fuse to blow? Or is it just, you know,

**Dave Jones:** the batteries have been inserted uh backwards, you know, and uh and it's just popped it, and it's bad design. Who knows? But uh anyway, um one way to find out is to uh replace that fuse and uh give it a go.

**Dave Jones:** But there are dangers in that. If you just start short that out and do it again, and something in here is shorted, well, you could blow the circuitry. I mean, the fuse is there to actually protect your circuitry. So, really, you

**Dave Jones:** know, you'll What we have to do first is check that there's nothing shorted on here. And the first thing you want to do is check to see if this power rail is shorted to ground. And we'll do that.

**Dave Jones:** We're going to put our negative probe on here. By the way, if you're probing stuff like this, there can be flux residue left on these pins. That's why a sharp probe is important. You've got to actually pierce any oxidization or

**Dave Jones:** residue, even on your uh components as well. Oxidization um is a big problem when you're troubleshooting. You can't You can easily make bad contact on there. But anyway, let's uh measure that. No, it uh yeah, that's a typical cap.

**Dave Jones:** It's It's going down, but that's, you know, it's certainly not shorted, so there's nothing wrong with the input power rail there at all. And the next thing to do is just probe around some of these capacitors on here and see if any

**Dave Jones:** of the capacitors are shorted cuz a few of them are bound to be across the power rails. I mean, we've measured the input to presumably the voltage regulator over here, and that was fine, but, you know, we can do some more probing around here

**Dave Jones:** like we can, you know, measure across that cap, across this one here. Oh, 13 ohms, but that's probably that's, you know, that's probably the motor or something like that. So, probe across here, and I don't see any uh

**Dave Jones:** any gross fires. You know, there's a couple more around. You probe around, but uh if you If you can't find any shorts across any of your caps, then uh you know, it's it leads you towards uh being fairly confident that

**Dave Jones:** uh the input fuse has just uh popped due to a reverse battery or something like that, and it's probably not something, at least on the power rails in this thing, that has popped that fuse. So, what I'm going to do is pop that out.

**Dave Jones:** I'm dual-wielding soldering irons here, and uh that's the easiest way to do this, and I will just pop this sucker off. Bang, it's gone. What I'm going to do is just solder on a couple of little pins onto here so that I can

**Dave Jones:** insert my ammeter in there, and I can measure the current going through this thing when we power it up. All right. Now, what I've done is I've hooked up the two test points. I've got some alligator clips here going to

**Dave Jones:** my Fluke ammeter here and we're in microamp range here and I've plugged the batteries in. I mean, ideally well sometimes you want to do this test with like a bench a current limited bench power supply, but I'm pretty confident

**Dave Jones:** with this thing. I couldn't be bothered hooking it up. So I'm going to be a bit brave and going to use the existing batteries here and try and get the peak current of this thing. Now, I've got it switched off. I

**Dave Jones:** haven't switched it on yet and it's drawing about 150 microamps. That that would be the microcontroller. Just you know switched off waiting for those soft buttons to be pressed and that's and that's pretty high in the scheme of things. You know, you

**Dave Jones:** can actually get a lot better than that, but really you don't need to. You put the batteries in this thing. It's used practically they're rechargeable used practically every day. So you know, really you don't need this thing to last

**Dave Jones:** for you know, years or decades in standby. So that's just fine. So really what we want to do now is change our current jack over to 10 amps. Yeah, beep beep beep. Bloody default AC current. This is an electronics multimeter not a

**Dave Jones:** bloody industrial thing. They claim it is, but they've got other meters for that. It's really annoying. Right. So what we're going to do here is we're going to switch our min max mode on. So that will capture the maximum. It can capture pulses much

**Dave Jones:** or spikes much faster than what the display can update. So that will capture that and hopefully give us our max current there and let's switch button is which. There we go. That's the power. I don't know what uh, uh, suction setting it's

**Dave Jones:** set to. I haven't I've got the tube plugged in so that we can actually, uh, you know, short out the tube if that's the correct terminology. Plug it anyway, we'll use that and, uh, that should increase the current draw, but here we

**Dave Jones:** go. Let's see what peak current we get. And then presume and hopefully it works. Gee, you know, that's the main purpose. Want to fix this thing, so let's go. Oh, bang. Bang. There we go. It's working. That's all it was. You can see the LED

**Dave Jones:** flashing there. No problem whatsoever. That seems to be working fine. I won't plug the tube up yet cuz I would, uh, presume that'll increase the, uh, current. But let's, uh, let's have a look at the, uh, max reading there. 0.56

**Dave Jones:** amps is what it was, uh, is the maximum reading. The minimum and the average is, you know, uh, 68. Who cares? But the maximum value there is 0.56. So let's, um, do that again with let's just plug this

**Dave Jones:** up and I think we'll find the current increase. The sound has certainly changed. We you you heard it beep there, so it's obviously got a new maximum peak value there. So there it goes again. It beeps when it detects a new

**Dave Jones:** maximum value. And 0.58. No, no, that's terribly unexciting, but there you go. That's, uh, it's fixed it. So looks like it was only the fuse that was dead. Of course, that could be on minimum suction, too, so I'll

**Dave Jones:** There we go. I can hear that. Wow, really ramping this. That's probably That's probably max now. Can really hear that. So, let's Yeah, it's I think it's still going to be very very similar. Yep. No drama. But, it certainly increases the uh

**Dave Jones:** suction on that thing. And there is suction there. It's really good. It's working a treat. It's just switched to another mode. It's got That's why it's got a microcontroller in here and it's got I don't know, scientifically proven to, you know,

**Dave Jones:** suck out the most milk, I guess. It's got all these different modes and it does seem to switch between them. So, and it's not flashing anymore. It's just uh going single. But, I'm sure if I read the uh user manual or actually

**Dave Jones:** uh was familiar with how this thing worked, I'm uh sure that is all normal. Now, I don't have a uh replacement uh fuse for that to hand. So, you know, the best I I sort of seem to have is one of

**Dave Jones:** these uh axial uh 2-amp uh slow-blow types. Eh, whatever. It's better than just bodging it and and uh shorting it out. So, I might just to to get it back up and running today, which is what I have to do, I'll just uh whack in one of

**Dave Jones:** these. And if you're curious to know what rail is being used in here, let's probe one of these caps down here. And we get in 3.8 volts or thereabouts.

**Dave Jones:** So, it looks like Oh, no. I accidentally pressed the button there. Started it up. There we go. So, it looks like it's uh 3.8 V rail there. It's not uh your traditional 3.3, for example. So, I deem this thing to be repaired,

**Dave Jones:** but uh that's not the end of the story because um we want to at least uh have a look at the motor underneath this thing. I mean, I don't want to take it uh fully apart. It won't be that

**Dave Jones:** interesting. So, let's see if we can pop it off. And what it looks like. Aha. Down in there. Look at that. Little clip down in there. It looks like it uh it joins it uh clamps this top half to the bottom half there. There's

**Dave Jones:** probably a matching Yeah. Matching one over there. So, if I get in here pop goes the weasel. There we go. Lifted that one up. Give that a little gentle prod. Aha. Ta-da. Ooh. Oh, that seems stuck. There's something

**Dave Jones:** something not There's our motor. Ta-da. There's our motor. There's something not Oh, yeah. There's the uh Yep. Looks like that's the uh little plastic um rubber uh air hose there. So, Oh, yeah. They're actually joined onto there. I don't want to take that apart.

**Dave Jones:** That'll be annoying to uh They actually just popped off. So, but there you go. Anyway, that's the uh that's the motor. Not very interesting with the uh And it just uh generates uh suction in there. So, I'm not going to tear all

**Dave Jones:** that to bits. This thing's fixed. And uh hopefully, whoop, that plug needs to go back in there. Anyway, not terribly exciting. And if you actually look at the uh wiring here, we've got two larger gauge wires here, which are clearly the uh motor drive.

**Dave Jones:** And there's two black ones as well here. Um a thinner gauge, obviously some sort of uh sense some sort of sensor or uh something like that coming back from the suction mechanism. That's uh that's what I would presume anyway.

**Dave Jones:** And if you're curious to see the way motor drive waveform, as I am, let's see if we can probe it here. I'll switch it on. Here we go. Whoa, hang on. Look at that. That's interesting. Wow, look at that. We've got

**Dave Jones:** some sort of variable pulse width modulation thing happening there in packets like that. So, if we stop that, we can zoom in and see that that No, that's pretty consistent. And there's packets of those. So, 1 2 3

**Dave Jones:** 4, yeah, 4.3 milliseconds. And And then it switches off, of course, during those periods. So, we really slow the sweep speeds down, we can see it switching on then off. And when it's on, that's what it's That's what it's doing.

**Dave Jones:** And now what we're looking at here is the sense waveform or that that sense wire coming back. So, there's a See those spikes? We've got some over voltage spikes there. If you can see those happening. We can capture on those, of course. Move

**Dave Jones:** the trigger level up above here, and we can uh single shot capture one of those. There we go. So, let's Let's have a look at that. Tada!

**Dave Jones:** Look at that. Beautiful. Let's turn the trigger back trigger level back down. So, that is um yeah, I do it's some sense winding coming back from the pump mechanism, the motor slash pump mechanism. And if you want to see

**Dave Jones:** both of them, the top waveform there, the green one, channel two, is the motor drive waveform, and the bottom one is that sensor or something, whatever it is, line coming back. So, we single shot capture that. Bam! So, that's rather curious. You can

**Dave Jones:** see that when the pump stops, when the pump actually, this is the point where the pump stops. It's, you know, it's going through its cycles here, and then it stops for its, you know, 1 second or half a second or

**Dave Jones:** whatever. Then the sensor's normally high when the pump's on, and then it starts to rise up and give a PWM output like that. I assume it's an output. And it's it's not some input waveform or something or rather, and then that

**Dave Jones:** starts to rise, and it levels out until such time as it starts up again. Let's capture a big length there. There we go. They're exactly exactly opposite. So, I'm not sure entirely how these things work, but maybe that's actually an out this

**Dave Jones:** waveform is not actually a sense input. It might actually be an output going to some sort of valve or something like that. Perhaps. But then why would you why why would you uh you know, pulse it like that? Why would you actually

**Dave Jones:** do that? I don't don't quite understand. So, if you've got a better idea of exactly what's going on there with that, please, by all means, leave it in the comments or on the forum. There you go. That is a repaired

**Dave Jones:** Medela, or is it Medela, swing breast pump. Um, not the world's exciting most exciting repair, sorry. Turned out just to be of the fuse, but anyway, I hope I made that as interesting as possible for a blown fuse anyway, and uh

**Dave Jones:** well, if you like the video, if you like Teardown Tuesday, please give it a big thumbs up. And if you want to discuss it, jump on over to the EEVblog forum. Catch you next time.
