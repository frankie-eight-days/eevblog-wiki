---
video_id: fp3eJkH8llI
title: EEVblog #1182 - Mains Interference Simulator Teardown
url: https://www.youtube.com/watch?v=fp3eJkH8llI
source: youtube-asr
---

**Dave Jones:** Hi, got a real interesting bit of kit for teardown for you today. This is a Schaffner made in Switzerland. Hi to all my Swiss viewers. The NSG 200 mains interference simulation system and I scored this from the that big dumpster

**Dave Jones:** that was outside of a company who still shall remain nameless even though this one actually has Alcatel Australia part numbers on it. No, it wasn't Alcatel and someone called the Standard Telephone and Cables Proprietary Limited. No, it wasn't them

**Dave Jones:** either. So, I'm not sure what the deal is there. So, what this bit of kit is for is for like EMC and compliance testing houses that actually test your products for various standards and susceptibility and things like that. And

**Dave Jones:** depending on the type of product, you may have to like a mains power product, you may have to test it for various mains disturbances, dropouts, like lightning strikes on the mains and things like that, surges and bursts and

**Dave Jones:** other motors switching on on the mains or relays clicking and you know, loads switching off and on. All these little transients and pulses on the mains, if you want to ensure that your product survives these, you need one of these

**Dave Jones:** things and generally you'll only find these in test houses. You might find them inside some, you know, companies developing mains powered products and things like that, but it really is a very specialized bit of kit and it is a

**Dave Jones:** actually a mainframe based system. It's the NSG 200 mainframe which is just this main power supply over here and then you can get all these different plug-in modules and we should be able to take this one out. This is the NSG 222A, but

**Dave Jones:** you can get like half a dozen different modules for this system that simulate things like mains dropout for example, uh DC dropout if you've got a DC powered uh product. Uh this one, which is the um fast pulse

**Dave Jones:** uh interference simulator, this one actually uh test 100 nanosecond pulses with a rise time of either 5 or 10 nanoseconds here. So, really fast pulses designed to simulate things like, you know, loads switching off and on very fast on the mains that can uh the

**Dave Jones:** elsewhere on the mains that can cause interference to your particular uh product. And this is this is its only job. Its only job is to generate these 100 nanosecond pulses at various amplitudes up to several kilovolts. And there's a apparently a standard for

**Dave Jones:** this, the 4517/79. I don't know. I can't really find any information on it. And may- maybe I've gone into a more like a recent standard. This is, you know, this is a fairly old uh bit of kit, but this would still be

**Dave Jones:** used in test houses, no doubt. So, in addition to the fast simulation pulses, you can get other types of bursts and also high energy pulses up to, you know, 5 kilovolts, you know, things like that, like real high energy uh pulses into the

**Dave Jones:** mains. This one's just designed for um not I don't think it's necessarily high energy, but uh fast amplitude pulses from like uh from tens of volts, like 50 volts minimum, I think, up to uh several kilovolts. So, I have no idea if this

**Dave Jones:** thing works, but let's have a look. I actually want to turn it on before I take it apart, just to see what the state of it is. And on the back of it here, you can see that all must uh connect internally. There

**Dave Jones:** must be like uh you know, like uh contacts inside or uh something like that. I'd be surprised if it's a cable-based system going over probably some contact-based system. There's the details for those playing along at home. We've got the mains um just the standard

**Dave Jones:** mains input, but also for the uh test supply of the product that that you're actually uh testing. So, we can uh plug Well, let's just plug this one in first and uh see if it at least powers up. So,

**Dave Jones:** I don't know why exactly a bit of kit like this would be thrown out. They're ridiculously uh expensive specialized bits of kit. Maybe it's just obsolete. It doesn't suit the new standards anymore, and they have no uh use for it.

**Dave Jones:** So, let's power this on. I don't know what Oop. Yay! Look at that. Haha. Pulse amplitude. Sweet. I can hear something going buzz. So, Oh, pulse. There we go. And that'll go all the way with LBJ up to how many kilovolts? Should be

**Dave Jones:** couple of kilovolts. Yep. Yep. 2.2 kilovolts we can go up to, and we can Ooh. There we go. External pulse. We can apply the pulse, or we can feed in an external uh pulse from here. I Yeah, I

**Dave Jones:** think they've tossed this out. I think I'd be surprised if there's anything wrong with this, actually. I, you know, confidence is high. I repeat, confidence is high. And sure enough, if we plug our 240 volts into the second uh test supply

**Dave Jones:** socket over there, and we hit the big test supply button here, bingo. We got our 240 volts to uh here in the lab. 247 volts AC. So, we should be able to apply here's a little 100 volt pulse. Boop. Boop. Of course,

**Dave Jones:** we won't see anything on the multimeter. So, we're going to have to get the scope out and a high voltage probe. Just want to show you this. When I put it on uh free running frequency here, just listen

**Dave Jones:** to this. You can hear it. And then when I switch it over to 0.2 FL, you can hear like a relay switching in there. Neat, huh? I think that sound That actually sounds like a relay switching. Whoa. Unfortunately, the magic smoke has

**Dave Jones:** escaped. Whoa. something went snap, crackle, and pop. Damn it. So, oops. Yeah, something went horribly wrong here. It's a week later. Is it 2 weeks later? I don't know. This thing actually I panicked. It was releasing so much

**Dave Jones:** smoke. Panicked, had to put it in a cardboard box to stop the smoke from setting off the fire alarm in the building here. And yeah, well, let's take a look inside and see what's wrong with it. It I think it was

**Dave Jones:** mostly coming from like this power supply section over here. So, yeah, let's get into it. And yep, even after that time Oh, that's that's not good. Slide that out and yep as predicted a contact base system. Wow, that's a

**Dave Jones:** doozy, isn't it? Look at the size of that. But, then again, this is like a high energy thing. So, that's impressive. Wow. Um oops, I taking out the screws in there, I thought maybe this might slide out as

**Dave Jones:** well. I didn't think it did, but yeah. Oops, no, that's just the loosey-goosey front panel. And the back panel surprise, surprise, which brand filter do does a Schaffner bit of kit use? Well, uses a Schaffner filter, of course.

**Dave Jones:** Top notch. And they're serious about that earthing, too, aren't they? Very nice. Done right, as you'd expect. Whoa, check this bad boy out. Whoa, let me show you the detail. This transformer is actually wound with solid copper like a bus bar thing. These aren't just

**Dave Jones:** like This isn't just your regular like enamel coated piss ant wire. These are like solid. So, thick as. Look at that. Like, you cannot move though. Cannot budge them. They are thick solid bus bars. That's incredible. Actually, you could get the calipers on

**Dave Jones:** that. For those playing along at home, it's about 3.1 mm by 2.2 mm thick. I think we can see our problem. You can just see the thickness of the the bus bar. I'm just going to call them bus bar windings cuz they're just like

**Dave Jones:** absolutely enormous, but that is that where our smoke has come from? Look, it's dripped down there. It's got that telltale sign of of having dripped off. Wow, you can just get a feeling for those windings. Unbelievable. Yeah. That's That's where the magic smoke

**Dave Jones:** escaped from. And uh not sure why or how that did it cuz it's not like we were loading the thing down. She's burned away, so yeah, it's it's not going to be able to ease in a fix something like

**Dave Jones:** this. You can see here that the uh well, it's I'm not going to call it the primary and the secondary because it's not because uh this doesn't look like it's doing a uh transformer operation. Looks like a huge choke. It's It's just

**Dave Jones:** burned that top bit and then dripped down. It's really strange. So, maybe you know, some like breakdown between one of the windings in there perhaps, but jeez. Now, in terms of uh operation here, we've got uh 50-60 Hz like tap, I guess,

**Dave Jones:** and 400 Hz. Look at that. That's really interesting, but I'm not sure how like it or how it's like selects 400 Hz or 50-60 Hz. There's no like selection for this. This thing There's no Well, it's got 50-60 Hz on the label here, but uh yeah,

**Dave Jones:** like it's all hooked up. So, like So, I'm not sure what the deal is there, but there's not much on the board at all. The mains inputs are here. That just goes over to the switch on the front, and then that's

**Dave Jones:** also routed to the board probably for some switching, and then goes over to a terminal block here, which then is going to bugger off, which then comes just goes directly into these contacts here. So, like, this is not a transformer for

**Dave Jones:** the modules. The modules basically I have their own 240 volts inputs. So, the modules will have their own local transformer to do whatever power requirements that they have. This block here, which is Schaffner branded, made in Switzerland. Hello to all my Swiss viewers again.

**Dave Jones:** It's like just a big potted monolithic block. I'm not sure if you can see that down there, but that's an ITT cap made in West Germany. Not this East German rubbish. Now, I did finally find a schematic for this thing, and as it

**Dave Jones:** turns out, this giant transformer here is actually a 16 millihenry common mode choke, and this Schaffner RF529 big potted unit here is a massive filter. And the board is just basically some extra like filtering type stuff. But, yeah,

**Dave Jones:** it's not much to it at all. But, this is an absolute beast. So, I'm not sure what happened to like burn this common mode choke. That's just nuts. So, that 400 hertz 50-60 hertz labeling there, which seems to label like each different like

**Dave Jones:** tap there, so to speak, that's a furphy because this is a common mode choke. There's no switching or anything based on frequency. It's just there. So, yeah, that labeling's a bit Don't know why they did that. Well, inside the injection module, isn't that

**Dave Jones:** sweet. So, we've got a big-ass contacts coming in here. I love that. That's absolutely brilliant. But, that is really quite neat. There's not, you know, a lot of space in there, but that's very neatly laid out. We've got

**Dave Jones:** the the control side of it all over here, which of course, cuz it's got to do the display. It's measuring Oh, look, a chip's almost falling out. Check that out. I never seen that. That That chip is almost falling out. That is

**Dave Jones:** hilarious. I'm not saying it's aliens, but it's aliens. There's nothing too exciting on this board over here, but I like their little nice little regulation local regulation block down there. Little heat sink block, that's very nice. It They've got

**Dave Jones:** seal pads on each one. It ties into the chassis down there. Beautiful. And of course, we've got a mains transformer here, 240 V just comes in on the bottom side here. Woah. Oh, that's an Elco. It's an Elco. For

**Dave Jones:** all you Elco fanboys, it's upside down, so all the electrons are going to fall out, but jeez, you don't see many Elcos. And what's interesting about the rest of it is it's all that like, you know, 4000 series stuff. None of this TTL rubbish.

**Dave Jones:** And the only microcontroller you can see in there is for the display panel board where they've rolled their own display panel board. It's got its own little trimmer for calibration and everything else. So, I'd say they've actually designed that for maybe, you know, a few

**Dave Jones:** different products. Look, it's got decimal point here, 99.9, 9.99. So, you know, that's really neat. It's probably used in several different uh Shaftner designs, I'd be willing to bet. The wires just soldered it onto the coil legs of the lid there.

**Dave Jones:** Pretty how you doing? But, all the interesting stuff is over on this injection PCB over here. I'll call it for want of a better name cuz that's really what it's doing. Check out the lead length they're getting on that

**Dave Jones:** power resistor just flapping around in the breeze there. Wow. And they've put an insulated sleeve over the leg there as well. That one has the the little alien crop circle in there. They just needed some extra inductance, I guess.

**Dave Jones:** These black jobs here Yeah, these are actually Kaco relays. I don't know those offhand, but they're huge beasts. Look at that. We might actually be able to Can we just like pry it off there maybe? Yep, I got him. Check that out. Isn't

**Dave Jones:** that beautiful? Look at that. Lovely relay. You can see the contacts down in there like that. And she pulls it in. Excite the coil and that's beautiful. That's actually a There you go. Double pole double throw contact. Neat.

**Dave Jones:** Check this out. This is really interesting. They've got these mechanical buttons here, of course, which have these just the mechanical indicator in there. Just a little shutter which which just covers and uncovers that because this is like a

**Dave Jones:** real, you know, a high voltage high power thing. You want it physically decoupled. So here's the mechanical switch here and it must have like a steel wire which goes around this bend here and the actual switch is up on the

**Dave Jones:** PCB here. So if I press that, that's where your 10 nanosecond pulse switch is on the PCB. Physically and electrically decoupled from the poor ass user pressing the button on the front. So maybe that's what our little crop

**Dave Jones:** circle is there. Maybe that's a little bit of delay. But the problem with that theory is that the normally it's a 100 nanoseconds delay and you can switch in the 10 nanoseconds. So it's not like, you know, that little coil of wires

**Dave Jones:** going to add 90 nanoseconds in there. That's just not going to happen. Anyway, it's switching in some sort of element which changes the pulse width. This gigantic orange job here is a huge high voltage reed relay or just a yeah,

**Dave Jones:** a high voltage relay. Sweet. Apart from that, there's not a huge amount extra. Another little custom wound transformer down there. A board to board interconnect uses a good old fashioned dip socket arrangement. But look, they've got some copper tape on

**Dave Jones:** top of that. The copper tape actually terminates on this side of the shield. They don't want anything coupling into that ribbon cable going between the logic and the pulser board. Obviously, they need that because you've got lots of fast

**Dave Jones:** high voltage switching in here. So huge d i v t a a change in current over time. You don't want that to couple into your ribbon cable and back into your logic circuitry. Just attached at the one point on this side here. Basically, just

**Dave Jones:** down to chassis earth. Whole bunch of huge caps in there. There you go, rated for 6 kilovolts. Wow. Yeah, another 6 kilovolt job. Woohoo. Then you've got these huge wire wound inductors here done by Schaffner. Made in Switzerland. So some

**Dave Jones:** nude virgin in Switzerland sat there and wound these and uh he shrunk them and they're on there with a nice big high voltage standoff. Another one of these mysterious potted filter blocks down there. You can see that just they go off

**Dave Jones:** because it's it's actually symmetrical on the line here and it goes off the active and the neutral, so to speak. But, in terms of doing pulse injection like this, it's L1 and L2 they call it. And all the

**Dave Jones:** connections just look brilliant. So, they go over to either the banana jacks on the front or they go or they jumper over with this brown wire here over to the European test socket. And I'd say that's your main cap there storing the charge.

**Dave Jones:** That's a 4,000-V jobbie, .04 mfd. None of this uh millifarad rubbish. This is microfarads. So, 47n, 4,000 V. Do the math. That's how much energy that they can dump into this thing, and the whole rest of it's just a you know,

**Dave Jones:** just the mechanism to actually inject uh the pulse onto the mains. So, there's really not much else inside that, but it is fascinating um to look inside like a high-voltage test injection system like this. And it's really not something that you'd

**Dave Jones:** ordinarily get to have a look inside. As I said, this is a very specialized bit of kit. So, that was a great find to find in the dumpster, and I think this injection module uh just works or interference simulator

**Dave Jones:** um module likely works okay. It's just that yeah, we've had some sort of winding failure in the common-mode choke on the input. So, you could potentially try and like take that apart, and I don't know, try and repair it maybe, but

**Dave Jones:** yeah, I Certainly, a fair bit of smoke did escape from it. So, it's not a happy little puppy, but anyway, I hope you found that interesting. And if anyone's got access to a schematic for this, um please, I'd

**Dave Jones:** love to see it cuz I wasn't able to uh find one. Cuz that'd be fascinating just to see exactly how they uh implement uh this pulse injection onto the mains. And as always, I hope you enjoyed that. And

**Dave Jones:** if you did, please give it a big thumbs up, and you can always discuss down below or over on the EV blog forum. Catch you next time.
