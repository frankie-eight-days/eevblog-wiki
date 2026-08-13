---
video_id: JnbnlWmxvrs
title: EEVblog #435 - 3D Rocker Teardown
url: https://www.youtube.com/watch?v=JnbnlWmxvrs
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 24, "2": 44, "3": 60, "4": 84, "5": 96, "6": 113, "7": 133, "8": 153, "9": 169, "10": 189, "11": 206, "12": 226, "13": 242, "14": 258, "15": 274, "16": 290, "17": 315, "18": 335, "19": 355, "20": 375, "21": 395, "22": 416, "23": 432, "24": 448, "25": 464, "26": 481, "27": 497, "28": 513, "29": 529, "30": 545, "31": 561, "32": 578, "33": 594, "34": 618, "35": 634, "36": 651, "37": 671, "38": 687, "39": 712, "40": 728, "41": 748, "42": 768, "43": 789, "44": 805, "45": 825, "46": 842, "47": 858, "48": 874, "49": 890, "50": 906, "51": 926, "52": 942, "53": 963, "54": 987, "55": 1003, "56": 1019, "57": 1043, "58": 1060, "59": 1080, "60": 1096, "61": 1104, "62": 1129, "63": 1145, "64": 1161, "65": 1177, "66": 1197, "67": 1213, "68": 1230}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. Sorry if I'm making some people motion sick, but we've got something a bit unusual today. We have a 3D rocker. What the hell is a 3D rocker? Well, as its name implies, it's a three-dimensional rocking platform. It rocks something around and around

**Dave Jones:** and around in three dimensions. It's from Stuart Scientific, it's the 3D rocking platform STR-9. And I scored this for next to Nick's, and well, I don't know, it just has to be useful for something. I don't know, it's just kind of cool. And here it is, shaking my new A10, if I can read it,

**Dave Jones:** PPS3205T3S power supply. It's rated up to 10 kilos, this one, I believe, and this power supply is not too far off the mark. And as you can see, it's just designed to rock these things at a very slow, or rock things at a very slow rate.

**Dave Jones:** I think this one goes from about 5 revolutions per minute up to 70 revolutions per minute. So at 60, of course, it'll rotate it once per second. And it's a bit of scientific laboratory apparatus that is designed to shake, you know, flasks of chemicals or beakers of

**Dave Jones:** chemicals, stir them up in a three-dimensional motion. And you can get all different types of these things. You can get ones that just shake them in a linear, like a linear shaker like that, that just shake back and forth, or in one direction only.

**Dave Jones:** Left, right, back, forth. And this one just rocks like that. So it's good for stirring, you know, liquids and things like that. If you're, you know, if you're into, yeah, chemistry or whatever, and you're, you know, you need to mix chemicals in a certain

**Dave Jones:** predictable way, or samples, specimens, whatever, that's what these things are designed for. So I thought, well, you know, it's practically free, and well, I don't know, it's got to be useful for something, surely. If you've got any good ideas, let me know. So this is not going to be an exciting

**Dave Jones:** teardown from a technical point of view, folks, because what's inside this thing is a mains on-off switch, there's a motor on-off switch, and there's a variable speed controller. And really, inside, I don't expect anything more than just a basic, you know, mains motor speed controller, probably very similar to ones used in

**Dave Jones:** handheld drills or something like that. Similar sort of, you know, motor controller system. One little board in there to drive that, driven directly from the mains, and well, that's it. But I thought, maybe we can make it go a little bit faster. Maybe we can make it go up to 11 on the dial.

**Dave Jones:** What do you think? And no, there's not going to be any fancy mechanicals inside, I don't think it's just a regular motor, which just then turns like an angled offset pivot joint kind of thing. I don't know, I don't know, my mechanical engineering's probably a term for

**Dave Jones:** that sort of, you know, pivot type joint, which then rocks the platform on top. So it's just a basic drill that just turns around. So, you know, it shouldn't be hard at all to reverse engineer the circuit in this and hack the thing, I'm presuming, anyway.

**Dave Jones:** And hi to all my UK viewers made in the United Kingdom, in the old dart. And no, there's absolutely nothing interesting on the back, it's just an IEC mains input connector. And as you can see, it comes from Glaxo, or what I think they're now called Glaxo Klein Smith,

**Dave Jones:** they're a pharmaceutical company here in Australia. So, you know, eh, mixing chemicals, who knows what they were doing with this thing. And it does have this arm here on the side, but I don't think it, you know, it just maybe, it doesn't actually, you know, exert any

**Dave Jones:** force on there. So I think it's just there to stabilise it, or something like that perhaps. That's, I think that's its only role, I don't think it's you know, really there's a huge amount of mechanical stress on that. But I see like there's a compliant rubber in there, and really it just, it sort of

**Dave Jones:** bounces up and down, so I think it may be just, I don't know, taking out some sort of vibrational mode or something like that perhaps. Nothing exciting on the bottom of course. And we've just got some screws here, that looks like it holds this base

**Dave Jones:** on. And I think it's just going to pull off like that. So I'll probably expect the motor to be mounted on the top case and then, you know, the controller board just mounted on the bottom here somewhere like that. And that's probably all she wrote, so let's take it apart.

**Dave Jones:** Here we go, let's take this thing. Yep, I can see inside. Yeah, it's exactly what I thought. Hang on, there's some cable ties holding it in place. I may have to flip it around. And that's all we've got inside, a little tiny controller board here

**Dave Jones:** as I expected. And there's our motor with a little optical encoder on it, we'll have a look at that in a bit more detail. There's the feedback sensor which goes back to the controller to keep it at a specific rotational speed. And well, that's it.

**Dave Jones:** Bob's your uncle. And here we have a basic brushless AC controller and a basic brushless AC motor. You can tell it's brushless because of the external coil around here. There is no brushes like you would find brushes and contacts like you would find in an electric drill, for example.

**Dave Jones:** That's why in drills, because they have the brush contacts on there connecting the coil inside, that's how they generate, you know, you see sparks coming out of it from those brushes. And it's a very limited lifespan. These things are incredibly reliable because there's no brushes to wear out or anything like that.

**Dave Jones:** They just use the optical encoding here to as a tacho to set the speed driving this thing. And that's it, there's a permanent magnet inside the rotor down inside there. And that's all there is to it. Very simple. And there's our phototransistor and LED combination

**Dave Jones:** in there. And of course our wheel with the black marks embedded on it so that as it spins around, of course, it interrupts the LED and the phototransistor in there. And it can get a pulse out of that which feeds back and controls the speed very, well, fairly precisely on these

**Dave Jones:** particular types of motors. Very simple, very reliable. And it looks like we have a reduction mechanism down in here and of course there's a shaft which goes through into there and that just turns that. You can see as I turn the wheel here

**Dave Jones:** you can see that just rotating very, very slowly. If I put some speed on that, there we go. You can see it rotating, so there's a fairly big reduction there. But I don't know how fast we can get this motor up to. I guess we'll find out.

**Dave Jones:** And here's our control board, very simple. One TDA2086A, I assume that's a motor controller. Don't know that one off the top of my head. We'll have a look at the data sheet for that thing. But yeah, powered directly from the mains. Here's the mains input

**Dave Jones:** here. We've got our big dropper resistor there. Yes, the power is turned off. Because this, folks, is all this board is at mains potential. So you don't want to go probing around in this thing. With your scope, I've done a whole video on that and how you can

**Dave Jones:** do the ARS audio scope. You've got to use a proper high voltage differential probe or a portable scope, which I tore down last week. And if you have a look at the earth terminal here, coming from the IAC mains input, of course it goes to the metal, bottom of the metal

**Dave Jones:** case and also goes up to the top here on the metal or the metal chassis up here for the motor. But it doesn't of course go to our board over here. Now of course in the MEN system, the multiple earth neutral system, back at

**Dave Jones:** your house or your board or whatever, distribution board or panel or whatever it is, of course your earth down here is connected to your neutral. And your neutral will be connected all the way and that'll be the negative, the neutral input on your IAC mains connector

**Dave Jones:** will of course be the ground, in quote marks, or the negative point on your board over here. So in theory you can, if your wiring system is all correct and hooked up properly, in theory you could connect your ground lead of your scope

**Dave Jones:** probe over to the negative point of the circuit, but in practice you do not do that. You need a proper isolated high voltage differential probe. So if you hook your scope probe up to that, of course, you would have this huge earth loop between your oscilloscope

**Dave Jones:** going all the way back to this thing and, well, it's not a nice situation. And if your power point or wiring is incorrectly wired, it can be incredibly dangerous. Take care when you're probing and playing around with these things, folks. Keep one hand behind your back.

**Dave Jones:** And check this out, we have a little trim pot down in there, so I wonder if that sets the maximum speed or not. I don't know. It's worth a tweak. Well let's take a look at this thing spinning. I've powered it up, and let's take it right down to

**Dave Jones:** sort of, that's like minimum, and it's just got enough torque to just switch over there. And I take it up to the first marker, which is, I don't know, it's 1 revolution per minute. So that's the speed, 1 revolution per minute, 10, and then, woohoo!

**Dave Jones:** Full on! Up to 70 revolutions per minute. But of course this is faster because we have a reduction gear inside the thing, of course. As you can see, there really isn't much else on there. There's a triac, of course, for the motor control, and a huge

**Dave Jones:** power dropper resistor to power the circuit. And we've got our mains rated cap, of course. But really there's not much to these things. We're going to have our triac, of course, which is our power device which controls the motor, chops the voltage up, go into the motor.

**Dave Jones:** And we've got a big power resistor over here, some little ceramic standoffs down there, that's of course directly mains powered. And really not much else. The circuit's probably straight out of the up-note. And I've reverse-engineered this board, and I've got a horrible looking circuit like this,

**Dave Jones:** which ends up, if I redraw it, looking quite smart and funky like this that you can see in this Davecad drawing. Now, as I said before, it'll probably be very, very similar to the up-note. Well, the actual data sheet, the TDA 2086A. Here it is.

**Dave Jones:** And it's I don't know if it's still a current part, it was a bit difficult to find the data sheet for it, but ta-da! Look, here is the typical universal motor application, as they call it, for the TDA 2086A. And yes, if you actually put them side-by-side,

**Dave Jones:** it is absolutely identical to what I reverse-engineered here. No surprises whatsoever. Now there's a ton of detail on how this thing works. It's, you know, it's fairly complicated, and the data sheet has some brilliant explanations, theory of operation, and all that sort of stuff.

**Dave Jones:** So if you enter all your motor control and things like that, I'd recommend you download the data sheet and take a good look at it. But the circuit is nothing special at all. Here's our motor here, the TRIAC is a T410R600, nothing special.

**Dave Jones:** Direct gate drive from the chip, of course. And that controls the speed. And we've got a TACO here, which is our phototransistor. Here's our LED here, here's our 2-watt power dropper power resistor here, which goes through in series with the phototransistor LED there,

**Dave Jones:** and through another diode, and that is the V plus for the chip. And if you do the math, power equals I squared R on this thing, then for a 75k 2-watt resistor in series with that LED current, you'll know that that can only be drawing, well, there can only be 5 milliamps

**Dave Jones:** maximum current through that to dissipate 2-watt power in that dropper resistor there. So likely it's running at, you know, half that, or 2.5 milliamps, or something like that. Anyway, it's got an internal regulator, so that generates the power for the chip. There's also

**Dave Jones:** a minus 5 volt internal generator as well. Actually, when I'm talking about minus 5 volts here, this one here isn't actually V plus, it's actually V minus, and that's minus 15 volts there. So the whole thing's operating on negative potential. So this cap down here will actually be negative like that, and

**Dave Jones:** this, what you think is ground down here is actually positive in respect to the minus 15 volt rail there. That's why if you have a look at the board here, this capacitor down here is actually it looks like it's back to front like that, but

**Dave Jones:** because that's actually minus 15 volts there instead of plus 15. And you're probably asking, well, why do they put this diode here in series with the supply here? Well, if you just, of course, you could, if you didn't use that tacho at all, of course that would be

**Dave Jones:** wired straight through and you just have the chip and the circuit drawing power from there. But of course this draws its own power, and as the calculations before, even a couple of milliamps can have very significant power, you know, a watt or two, a couple of watts, dissipated

**Dave Jones:** in this power resistor here. So if you had that shorted directly through powering your circuit, you'd still need that one or two watt big resistor there. And if you had the separate lead powered from the same, powered from the mains rail as well, you'd need an additional

**Dave Jones:** power resistor in there just to power the, you know, two or three or five milliamps going through that LED. So this is just a way to cheat, because you've got such a high mains voltage here, you can just cheat and put the LED in series, so you utilize the current flowing

**Dave Jones:** through there, and you only need one dropper of power resistor. Neat. Circuit optimization. And then we've got a voltage sync signal coming from here, which is just your mains input, and your current sink coming from across your triac there. So and the rest of these down here all have to do with how the block diagram

**Dave Jones:** of this thing works. And how this all works can get relatively complicated. Go into the details, we've got difference limiters, we've got frequency to current converters, and all sorts of weird and wonderful stuff. And you'll find one difference in the schematic here, in that the triac, there's no

**Dave Jones:** load current monitor resistor like there is down in here, because this pin 5 here has actually got dual pin functionality and it's not actually utilizing any load current sensing in this particular application. Doesn't really need it. So unfortunately our series pot down in there isn't really going to do much.

**Dave Jones:** I think it just mainly adjusts the lower speed threshold of the thing and that's probably it, it just stops completely. And it takes longer to start up. So that's no good for increasing our speed. If anything, it just lowers it. And for some bizarre reason, the circuit actually does have 3 parallel

**Dave Jones:** resistors in here. I mean this is a 50k pot, I mean there's no current flowing through this thing at all, but they do actually have 3 parallel resistors wired into the circuit. I have no idea why. Trimming? Alright, what I'm going to do now is have a quick probe of the

**Dave Jones:** gate drive signal on the triac there. So I've got my Fluke scope meter here. No, I'm not going to use my regular scope, my regular grounded scope of course. This one is a floating scope, so I can do that as long as I don't

**Dave Jones:** touch the probes down there, I'm all fine. Sorry for the crappiness of the signal here, but you can see the positive and negative transitions, DC coupled here on where 5 milliseconds per division, 500 millivolts per division vertical there, so you know, we're just over, you know, 650 millivolts or thereabouts

**Dave Jones:** positive and negative peaks. And I've got that at about 10 RPM or thereabouts. So let's take that up to 70. And we can see it sort of jump over the place as it's trying to hunt to keep this thing at a stable speed.

**Dave Jones:** This scope is really slow, folks. It's absolutely terrible. So we can't see all the fine, wee, there we go. Can't see the fine detail in there. And if I physically stop it with my hand, hang on, there we go. Whoa, it's stopped, it's barely

**Dave Jones:** going at all. And if I let it go again, it slowly recovers back, hunts, and it generates the required trigger signal to keep this thing at a constant speed. Okay, so I've got 30 RPM on there with no load at all. And if I put my hand,

**Dave Jones:** what I'm going to do is I'm just going to put my hand on here like this and just sort of apply a bit of force like that, just to keep it sort of, you know, just to give it a bit of extra force.

**Dave Jones:** And let's see what happens. There we go, you can see it expand out, the on time. So you can see that pulse really expand out and where it the time when it's widest there, that is when it's actually trying to really go against my hand.

**Dave Jones:** So because this thing's moving up and down, it now gets my hand so it goes really wide like that, it's really trying to keep it going. And on the other part of the cycle, then I'm not applying much pressure. Now if I try and apply a constant amount of pressure,

**Dave Jones:** I can maybe try and keep it over there, but ah, it's pretty hard. But unfortunately, folks, Teardown Tuesday has come to an end. I have run out of time today, I have to get home, and of course people will complain if I don't edit it out.

**Dave Jones:** And of course people will complain if I don't edit and upload the video today. So, which is Tuesday, there it is, check it out. It really is Tuesday, it's 6pm, I've got to head home. And lots of things happening today, big server upgrade

**Dave Jones:** just took place actually. So my EEV blog and forum website, they're all run on a dedicated server, and that just got upgraded. And that's done by HostGator, my web host provider, and they upgraded me to new hardware, you know, standardized hardware, it's some Xenon

**Dave Jones:** processor, however you pronounce it, something like that. Dedicated server, it's all running. Seems to have happened really smooth, but if there's any issues at all, please let me know, that'll happen in the next couple of hours, I'll just change the IP addresses and all that magic

**Dave Jones:** geeky stuff, penguin stuff. So anyway, I hope that goes real smooth, lots of stuff happening at the moment. I was hoping to play around with this more, measure some more stuff, hack it and things like that, but unfortunately I might have to leave that

**Dave Jones:** for a part 2. You know what they say in show business, always leave them wanting more. Catch you next time. http://TheBusinessProfessor.com
