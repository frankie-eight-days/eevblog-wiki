---
video_id: N8hz3MGS01E
title: EEVblog 1381 - Argon Ion Laser 10kW PSU Teardown
url: https://www.youtube.com/watch?v=N8hz3MGS01E
source: youtube-asr
---

**Dave Jones:** Hi. Check this out. It's a 10 W argon ion laser. I once called a laser this big. Look at this bad boy. Haha. It's a coherent brand, which is a US company. It's the Skylight 300C. And it dates from about 1997.

**Dave Jones:** And well, they don't get much better than this. And I know what you're saying, "Dave, 10 W, that's nothing. I bought a laser cutter on AliExpress for a couple hundred bucks that's got more power output than this." Yeah, well, yours is one of those solid

**Dave Jones:** state rubbish. It's not one of these beautiful ION LASERS. OH. The reason these are so good is because they are what's known as a noble gas laser. And these actually produce a incredibly coherent light source out. Hence the

**Dave Jones:** name. I'm here all week, coherent. Get it? Anyway, very coherent light source that the modern ones just can't match. This one does about 470 to 514 nm, but you can get various filters in them and to do various things and they're

**Dave Jones:** fantastic for physics research and stuff like that. So, it might be only 10 W output power, but these bad boys, I believe even still today, please correct me in the comments down below if I'm wrong, but they really can't be beat.

**Dave Jones:** One of these noble gas ion lasers for many exotic types of applications. But this one was actually used for outdoor laser displays. Those big, you know, projection mapping laser displays, how they project laser onto the Sydney Opera House, the heart Sydney

**Dave Jones:** Harbour Bridge, and you know, all those sort on the building side of buildings and stuff like that. And this one was saved from the dumpster. Thank you very much Daryl Tuxbury, who here he is here dropping it off to the lab here. And

**Dave Jones:** thank you very much, cuz he had it in the boot of his car for like a month while I was on holidays, so thanks Daryl. Anyway, I've done an absolutely brilliant amp power podcast episode linked in down below with Daryl and he

**Dave Jones:** talks about his time working at Laser Vision Australia actually designing these laser projection systems. Fantastic talk, so if you want to know how they actually do laser projection in those huge massive outdoor displays, Daryl was responsible for a

**Dave Jones:** whole bunch of those as well as designing a lot of the kit to do that. So, yeah, fantastic talk linked in down below, highly recommended. So, the way these things work is that they have a sealed plasma tube inside filled with

**Dave Jones:** the gas and just like an old-fashioned tube, they actually have a filament in the end which you have to heat up, so you know, it takes like a minute to start these things up cuz you got to heat up the filament, then you apply a

**Dave Jones:** high voltage pulse across that to actually start up and generate the plasma and then they've got a massive electromagnet surrounding that which then confines the ions within and that helps increase the gain of the laser and that's how they can get 10 W out of this

**Dave Jones:** bad boy. So, we'll have to leave the teardown of this for a future video. Thumbs up if you want that, subscribe, click the bell icon, all that rubbish, you know what to do. Anyway, future video. But, the interesting thing

**Dave Jones:** about this is how you actually power it and that's what we're going to tear down in today's video cuz Daryl also saved from the dumpster not only the laser head, this doesn't have any of the power supply stuff in it. This is just the

**Dave Jones:** laser head itself. So, he saved the power supply as well. This bad boy weighs about 42 kilos, the power supply weighs about 39 kilos. The thing about these, they're incredibly efficient. Oh, yeah, 10 W output for round about 10 kW

**Dave Jones:** input power. Get your confuser out, it's about 0.1% efficiency. So, I I think we're going to actually fit both of these on the bench. So, let me get the power supply. Let's Let's take this off. All right, yeah. Bend the knees. And

**Dave Jones:** here comes the power supply. No, that's got to be more than That's got to be more than the data sheet tells you for 39 kilos. This weighs more than the laser head. Going to snap my little fiddly wireless microphone cable.

**Dave Jones:** Look at that. Look at this bad boy. And yes, it comes with an equally badass cable. Look at that. So, I'm led to believe that this whole thing might actually still work. Cuz I think it was pulled from a working environment, but

**Dave Jones:** it's very old and there are issues with uh ion lasers ion lasers as they age. So, anyway, let's tear down this power supply. It's a big three-phase jobby. So, this thing has to supply up to 10 kilowatts to that laser head just to get

**Dave Jones:** 10 watts of light output. So, where does the 9.99 kilowatts go? Well, it goes away in heat in not only here, but in the laser head itself. So, that's an incredible amount of heat. You notice that it didn't have

**Dave Jones:** any heat sinking on that laser really, you know, it had no big external fins or anything like that. That's cuz it's all water cooled. So, this thing has some water pipes on the back. It's got all water cooling in it. And this, I

**Dave Jones:** believe, is a linear power supply cuz the way those laser heads work Here's the VI response curve for it. Whilst it is fairly linear except right at the extreme ends, it'll kind of just tail off like crazy. It's something that's

**Dave Jones:** actually better driven by a constant current source. So, once that high voltage pulse starts up the thing, it basically kicks into constant current mode. And this is basically a water cooling unit and a giant pass transistor basically give a linear pass transistor

**Dave Jones:** to give constant current. Although, I'm sure it's more than one transistor. And we're going to find out by opening this bad boy. So, yeah, this is a piece of work. I think I'll just do the teardown on this table, so it could look a bit

**Dave Jones:** different to where I normally do my teardowns. All right, here it is. I'm going to do this teardown in 4K for those who want to see. Hopefully, we get some detail. Anyway, here's the badass plug on this thing. Look at this, 50 amp

**Dave Jones:** clips or jobby. This is a five-pin three-phase, although they're only using the four pins in there because they've got the three-phase and the earth, and that's it. And just very briefly on the front, there's nothing doing here. Just

**Dave Jones:** got a laser on-off key switch, CPU OK, power supply OK. Yes, this is all CPU controlled. It's not just the pass transistor. As I said, it's got a little bit of intelligence to do some stuff. But, yeah, it's basically a pass

**Dave Jones:** transistor. And on the back here, of course, we've got to have IEEE 4008 in the face. Analog interface, it's got like I think like a zero to five-volt input. You can do like modulation and stuff like that. Anyway,

**Dave Jones:** we've got some big ass They're broken off. Actually, those levers are broken off there. Check that out. That's gorgeous. Big ass fuse holders. Look at that. What a Bobby Dazzler. 80 amp, 120 kiloamps, 500 volts. Beautiful. And we've got some other head

**Dave Jones:** control stuff here. Looks like we've got a couple of electronic breakers up there. 12 amp jobbies each. And the rest of it's basically just like the water cooling. Water in, this is the water out to the laser. This is the drain. This is from

**Dave Jones:** the laser. And couple of the interfaces as well. You might be wondering where the power comes from. You might think, "Oh, that's not you know, that's not enough to actually come out." Well, this whole interface uh here, these are actually the jacks for

**Dave Jones:** the interface because here is the end of the cable right here. Look at the huge four pins. They're the main power pins that actually uh plug go to the head unit and then we've got some control stuff here as well and it looks

**Dave Jones:** like uh does that plug in? That's the serial interface by the looks of it. That'll plug into the serial so it's got serial comms over to the head but uh yeah, and then look at that. What a beast. And then it

**Dave Jones:** looks like uh somebody's just uh terminated a couple of the hoses there cuz I assume that they can break that off and they'd actually go into there to get the water in. Now, it's not going to just recirculate in the head. And then

**Dave Jones:** the remote control um here it is here. We've actually got it. A little nice little um LCD controller here. The laser emission up and down uh menu and stuff like that so it it's all controlled. That's why it needs a microprocessor in

**Dave Jones:** cuz it can do various things. You can tune it, you can set memories and I don't know what light does. Is that your like backlight or something? Anyway, so we've got a date code down there December 1997 and I believe it's a 97

**Dave Jones:** vintage on the laser head as well. All right, so let's crack this thing open. As I said like there's not a lot in here. It's basically one big giant pass transistor or pass transistor array I expect. I don't know. They could be like

**Dave Jones:** dozens, hundreds of pass transistors in here uh to get all the power and do the constant current drive. It'll have a micro just a probably you know it dates from the 90s um could even be a late 80s design

**Dave Jones:** carried over into various products. I'd expect to see like a like a uh a Z80 or a 6800 or even a like a simple micro like a you know 8051 or something like that perhaps. Uh I think it's one of these imperial Yankee

**Dave Jones:** but I can just get that. All right, let's see what we've got here. These screws were missing, so somebody's had a go at this. I'm pretty sure Daryl didn't do it. Oh, it's another cover. Anyway, high voltage undercover and there's all our

**Dave Jones:** processory goodness on the other side. So, it looks like yeah, we might have all our power supply stuff under like this half here, control on the top. That's all fancy pantsy PLCC over there. We'll check that out. Um and then

**Dave Jones:** underneath all that will be all the water cooling stuff, I'd imagine. We won't go into any detail on here because it's it's simply not that interesting. But anyway, for the processor fan boys, we've got an 88 C196 micro. So, that's a little bit more than

**Dave Jones:** maybe I thought. So, anyway, yeah, it'll have some like interface stuff, some ADC stuff, and some serial stuff. All your basic paraphernalia and stuff like that. Although, there's a large header connector up this end, and this is the front panel. So,

**Dave Jones:** that's Oh, it says motherboard. I guess does that go down to this Okay, there were just two screws up here for the plastic hood. And looks like yep. Oh, we're in. Check out those bad boy caps there. So,

**Dave Jones:** we're going to have a three-phase rectifier in this thing. Now, what's going on here? I'll put up the block diagram. Believe we'd have this would be our cathode transformer down here. There's an enormous filter box under the bottom there. So, I don't know whether

**Dave Jones:** our rectifiers are in there or not because I don't see them. You know, look, here's our input fuses over here. So, looking over here, we've got our black, our blue, and our brown coming in. You might know that Oh, and

**Dave Jones:** our green. Our big earth just goes over to a massive lug over here. And of course, they go directly into the fuse holders that we saw before. And then there's gigantic You can't really see it. I'd have to take the whole thing apart. But

**Dave Jones:** there's gigantic studs on the bottom side of the fuse. So this is the top side of the fuse. Power comes in here and then it goes out the bottom. There's gigantic studs there and they go into this huge filter box all under here. The

**Dave Jones:** transformer's mounted on top of the filter box. So like the bridge rectifier has to be in there. Um so I Yeah, I'm going to have to take this whole thing apart cuz that's you know, rather interesting. I'm sure a lot of people

**Dave Jones:** would be upset if I didn't you know, get all this out. I mean, we're not going to use this anymore. So I'm going to take it all apart. And these are a bunch of circuit breakers that go out. This is

**Dave Jones:** actually looks like the output that goes off to the giant cable. But anyway, we've got a large capacitor bank here. Got a bleed resistor across that of course cuz you don't want that beast to stay charged up. You can tell this

**Dave Jones:** capacitor bank is delivering all the power. There's a huge thick cables going off here. These are actually going directly across the magnetic coil and confinement coil across the plasma tube in the head. So it like I believe like there's nothing

**Dave Jones:** else in the way. It just goes directly out there. That's why if you follow the money here, one of those cables they're going to sleeve over there. It buggers off and it'll go down to those four giant pins on the bottom of the

**Dave Jones:** connector we saw down there. And this bad boy here, half a millihenry at 80 amps. Thank you very much. This is simple LC filter. It's just a big inductor. It's not a transformer. It's just a big ass inductor in series with

**Dave Jones:** the output filter cap. Nice. Turns out there is another board under this. A huge board. I can actually see down there. So I I like this. Somebody's put a cable tie through two holes in the board here cuz this is a large like 96 way DIN

**Dave Jones:** connector. So like you can really damage the board doing that. So they put it fairly reasonably close to there. So that should aid us in pulling that board out. Isn't that brilliant? Somebody was thinking and we didn't have to undo the jack

**Dave Jones:** screws on the D connectors either. But oh, there you go. Caution, high voltage of course. There we're getting down to our pass transistor boards. Wow, is that is that the only one? Hmm. Guess I didn't like expect to see so many

**Dave Jones:** connections like big 96 way DIN connectors going over. Looks like they're going to like a backplane motherboard here and going over to the the pass to what's clearly the pass transistor array and it's called a pass bank board. There it is. So is that the

**Dave Jones:** only one? Anyway, that's I expected it to be kind of like a self-contained. I don't know why they need so much. I mean they've got a lot of monitoring stuff. There's lots of analog action, 741s and LM324s and

**Dave Jones:** a whole bunch of LM324s along there. Oh, once I get the board out I can show you better up close. Looks like yeah, base emitter collector. Looks like and unfortunately there's only like one screw in there. It looks like T maybe

**Dave Jones:** TO3 packages, but there should be a matching screw over there. So that's interesting. And current does sharing resistors. They've got little resistors on standoffs here. That's interesting. Have they done a select on test thing or something? Hmm, fascinating. Fortunately, it might

**Dave Jones:** be a bit of work to get all this out. Anyway, nothing on the back of that processor board. There's no bodges or anything. That's pretty impressive. Yeah, I don't see any any bodges on this. Looks like they got

**Dave Jones:** it right. No workers. Because this is not high volume stuff, of course. You're not going to like if you make a error on these, you're not going to like uh re-spin the board usually. Um you're just going to put in some mod wires and

**Dave Jones:** whatnot. But yeah, all looks good. Now, of course, I don't have to worry about this being uh charged up at all because not only have got bleed connection bleed resistor across uh the main cap there. So, I'm pretty confident I can do that

**Dave Jones:** without worries cuz it's been in the dumpster for Yeah, I don't know. What? A decade or more? Wow. Not even sure how this board is going to come out. Okay, I flipped it around so we can work on this a bit better. But uh anyway,

**Dave Jones:** take a look at the chassis. It's all on the other side as well. It's got all this uh it's See it falling off there? All this stuff caked. I don't know what that is. It's like it's very powdery and

**Dave Jones:** it just gets everywhere. Um yeah, I I don't know. Like my first thought was maybe it was like it was like some sort of salt build-up or something like it was used in you know, near the ocean in some sort of

**Dave Jones:** salt environment or something like that. But I don't know. Leave it in the comments down below if you got any idea what that that is cuz it's caked all inside here. You can see it right up in the case at the back. It's everywhere.

**Dave Jones:** It's horrible stuff. Anyway, there you go. There's our board. We can go over here like this and can have a squeeze around. And as I said, there's lots of uh analog action. There's LM324s and resistor arrays, networks all the way

**Dave Jones:** along there. So, they've got a grid arrangement for the pass in this thing. We've got various uh test points and whatnot. And as I said, it's called a pass bank array. And you can see how we got base emitter, and this would be the

**Dave Jones:** collector down here, the screw. There's no matching screw on the other side, so I'm not sure if that's a TO3 package or not. But interestingly, got another insulator wire coming out going through a hole in the board. And that's

**Dave Jones:** the same for all of these channels. Ah, I thought this axial component here up on these little uh stand-off turrets here soldered up off the board after the board's been assembled, then I thought these were like current sharing

**Dave Jones:** resistors for the individual transistors, but they're not. They're actually fuses. There you go, it's got F on the silk screen there. So it looks like this what probably one what jobby here is the current sharing resistor cuz you need

**Dave Jones:** one of those for each transistor. And that's what you do cuz when you're paralleling transistors like this up, you need to ensure the powers equally fairly equally dissipated between the transistors. You can't just whack them in parallel because they've got

**Dave Jones:** different characteristics unless they they come from like the same physically the same die and they're actually die matched transistors. They're not going to be well matched. So you put a little current sharing resistor in series with each transistor and that just helps when

**Dave Jones:** they're in parallel to actually do that. And it looks like they've got LM324 up here dedicated to sort of like a string of four pass transistors or four in parallel and then they've got like multiple groups of those. So yeah, each

**Dave Jones:** one of those is individually fused. You got to have that cuz if you get one transistor fail short, it's going to take down the whole array and it's going to ruin your day. So they're individually fused and having them on

**Dave Jones:** the turret stand-offs like that it means you can get in there and you can actually repair these things easily. Nice. So, this array is not a hugely high voltage. You're only talking about, you know, 250 V maximum up to

**Dave Jones:** 40-odd amps. So, it's the current and but it's the total power. I mean, the total you multiply those and wow, that's a lot. But anyway, yeah, I'm not seeing how this board comes out easily. Hmm, got a bus bar happening over here.

**Dave Jones:** Okay, so it looks like what's happening here is we've got the bus bar and this negative here, this goes to like a metal like Well, it looks like a huge chassis down the bottom, big black like a whole base plate kind of thing.

**Dave Jones:** And then it looks like we've got this bus bar going across here. Looks like it just joins four bars, which then looks like it probably runs this whole length the board like this, which is what you'd expect uh when they're all paralleled

**Dave Jones:** up. So, yeah, how this board comes out of here though. It's stuck under a railing at the top. You almost can't get it out unless you slide it out the front. Yeah, maybe disconnect this and then slide out the whole water

**Dave Jones:** cooling thing perhaps. But anyway, it's going to be interesting to see what uh transistors they use under here and how they're thermally coupled to the big water uh sink block. I can see one of the uh tubes going around on the top there. So,

**Dave Jones:** how they're actually thermally coupled down to that. So, but anyway, it looks like the board can't come out. It's got a like slide out the front with this uh black like Delrin type railing. Warning, Will Robinson. Warning. Right, so I started taking out

**Dave Jones:** a screw here, then I realized uh no, this uh thing like comes out. There's two Phillips here and there's a reason this puppy has a handle. So, taking out those, I don't see how the board how the bottom

**Dave Jones:** can slide out without the board. So, probably the whole thing is going to come out with the DIN connector. Yep. Yep. There you go. Beautiful. Oh, that's fantastic. We got another board underneath. Check it out. Okay, let's have a quick sneak a peek

**Dave Jones:** under Oh, we got some big ass resistors under there. Check those out. No, that's I was wrong about these resistors on the top being your emitter resistors, your current sharing resistors down here. No, they got real big beefy ones down here. So, and yeah,

**Dave Jones:** yeah, some TO3 transistors under there by the the looks of it. All right, this is what we came here to see. Looks like there's big plastic cover. You can see the TO3 packages under there. So, it's all a little bit more discreety

**Dave Jones:** than I had in mind. Lucky last, and we'll see an array of TO3 packages and the big current sharing resistors. Ta-da! All hooked onto a bus bar. Very nice. Look at that. So, yeah, that's what I was kind of expecting. I like the

**Dave Jones:** little ceramic standoffs down there. Check those out. That's pretty groovy. I like that. Cuz you don't want the whole thing flapping around in the breeze. Cuz this is fairly long. You can give that a wiggle wiggle wiggle. Yeah. Oh,

**Dave Jones:** okay. Those screws I took out, they were actually going into the ceramic standoffs there. Nice, but we're not talking about thousands of volts here. We're talking like this is like 250 V compliance voltage maximum. So, you know, not huge voltages. Yeah,

**Dave Jones:** so that insulated wire we saw coming through the board there goes through our current sharing resistor and goes up to the top bus bar here, and they're all just parallel like that. But, of course, this is only one side of the argument,

**Dave Jones:** right? We've actually got to have a another side all paralleled up, basically. So, might be able to see down in here, we're not done with the bus bars yet. There's another bus bar going across there. Actually, looks like it's

**Dave Jones:** going to connect the case of the uh TO3. And that's what we expect. If you Motorola fan boys, there it is, MJ15022s. '97 uh 27th week '97 date code. Wonder what they're worth each. Anyway, we do have uh yeah, the old-school mica washers,

**Dave Jones:** thermal uh paste, and uh the resistors, of course, they also have uh thermal paste on the bottom of them, but you don't need the mica washers because the resistor the case of uh these uh clad resistors is uh isolated from

**Dave Jones:** the terminals. Now, unfortunately, to get this apart, I'm going to have to undo a screw on each and every TO3 package. Bummer. Actually, on top of undoing the screws on each and every uh TO3, cuz that's what these uh captive studs in

**Dave Jones:** the PCB uh are for, I would also have to desolder every single one of the collector wires as well. I don't want to do that. I This thing's just gorgeous to look at. Yeah, so I'm not going to do that cuz there's nothing on

**Dave Jones:** the bottom of the board that's really of interest. So, as you can see, the uh heat transfer block is this big metal plate here, and that's just got the uh the water elements uh you know, tubes just welded onto them. So, really,

**Dave Jones:** like there's nothing under that at all. Um so there's really nothing to see. There's no value to be gained by taking off all those transistors. Yeah, I can get the board out, but then like it doesn't show us anything extra. So

**Dave Jones:** I'm not going to do that. I It's almost artistic like on its own. Right. So yeah, I'm just going to leave that as a block. So hopefully you can see how that works. The only thing extra is that there's a

**Dave Jones:** bus bar running from there which actually connects all the cases together. So they don't So they're using a bus bar for that. They're not relying upon the uh the metal of the this heat transfer block to actually do

**Dave Jones:** that. They're specifically putting in an extra bar in there um just to get lower contact resistance across all the cases. So that is very cool. What you're looking at there is basically one big ass pass transistor um to regulate a

**Dave Jones:** constant current through this. And they simply uh well, there should be one big ass current sense resistor somewhere which uh measures it all cuz they don't uh measure these. These are just uh balancing resistors. So there's got to

**Dave Jones:** be another uh huge, you know, 20, 30 amp or whatever it is uh current shunt resistor somewhere that allows them to uh then measure the voltage drop across that. And I've done a video on this how to design an electronic load. Works

**Dave Jones:** exactly the same way. It's just an op amp and a transistor and a current sense resistor. That's it. And second thought, what I think they're actually doing here is that uh because they've got an LM324 for each one. And as you've seen in my

**Dave Jones:** electronic uh load video, linked in up here if you haven't seen it, like if you have an op amp and if you have the emitter resistor like that, you measure you use that as the feedback and then you can control the current. So it look,

**Dave Jones:** they've got four lines coming out here like this and they've got the resistor uh block. They're just series resistors going out by the looks of it uh to drive the uh base of the transistor, and then it just links over to the individual

**Dave Jones:** transistor like this. So, what I think they're doing is I think they're actually setting um constant current for each individual transistor, rather than just paralleling all the transistors and uh then having one external current sense resistor. And that's why they've

**Dave Jones:** gone to all this complexity of having all the individual op-amps and all the individual control and look they've got uh some protection here, by the looks of it. And I you know they haven't Otherwise, this board would be like completely dumb ass, and well

**Dave Jones:** you wouldn't need all of this fancy pants stuff to drive each individual transistor. So, I reckon each one is set up as its own constant current load, using that power resistor as the sense element. And then each one, of course,

**Dave Jones:** is individually fused. So, that's how they're doing it. They're just whacking a whole bunch of like adjustable current sources all in parallel. So, it's not just a big ass pass transistor. So, yeah, these are uh two ohm resistors, so

**Dave Jones:** they're actually using those as individual current sense resistors to set a constant current for each one of these transistors, and they simply parallel them all up. So, then you're going to share the current across all of them. So, the downside of that uh might

**Dave Jones:** mean that well if one of these fails, technically, then you know if the fuse pops or whatever, then uh you're getting that amount of current less per uh you know in in your entire current going to your uh coil, going to

**Dave Jones:** your laser head. So, that looks like it's probably what they the trade-off they're doing. I mean, you know, one or two of these might pop if your current changes by, you know, a few percent. It's not going to matter

**Dave Jones:** much. Hang on. Count these. 10 10 10 nine. What? Find that deeply offensive. Okay, so what that leaves us with is another board down in here with some big-ass traces down there and I don't know set our current sense

**Dave Jones:** resistor or multiple ones down there perhaps to measure that. I'm not sure. Anyway, it looks like this might be there's our there's our rectifier diodes. I see them. Aha, now I see the wiring flow. I don't think I have to get all this out

**Dave Jones:** to access to the filter. Okay, I think I've got this right now. We've got our three phase coming in here. That goes through our big-ass fuses like this and the output of those fuses goes into that giant filter block on the bottom

**Dave Jones:** there. That's just like a mains filter. Then the output of that comes up to these. Aha, there you go. You can maybe see Yeah, got some circuit breakers down there. So they just like look like you know, big industrial circuit breakery

**Dave Jones:** things. Okay, like three phase breaker whatever and then the output of those comes over to our input rectifier. This is our three phase rectifier. I'll try and get the board out of here. Show you the diodes, but basically we've got

**Dave Jones:** three big diodes here for rectification and then the output of that which are these two bad boys here. They go over by those thick cables over to our LC filter here so I threw a series inductor and then our main caps like that and then

**Dave Jones:** our caps bugger off as I said before down to those terminals on the front down here which then go directly over the the magnetizing coil is directly in parallel with those caps. Magnetizing coil in the head in the laser head is directly

**Dave Jones:** across those caps there. All right, I've got all the screws out of here and these go down to various blocks and components down the bottom. And once again, we've got a neat little pull cable tie here. It looks like we've

**Dave Jones:** got some connectors going back down to another level as well. And of course, you've noticed the big ass fan down in there. So, let me Uh So, tug on this. There we go. And Yeah. Oh. Forgot to cut the screws down

**Dave Jones:** here. It looks like over here, they weren't relying on the PCB traces to carry all the current, which you wouldn't of course. Yeah, there we go. There you go. That's under the board. So, yeah. That that runs like that. So, you don't rely

**Dave Jones:** on So, these ones on the PCB might be handling significant current, but it comes a point where No. Let's use a big thick block like that to connect. There you go. To connect to those like that, cuz you just can't get that sort of low

**Dave Jones:** resistance on a PCB, even if you use, you know, ridiculous thicknesses of copper. It's just yeah. So, here we go. It's going to come out. We're out. WHOA! WOOHOO! LOOK AT THAT. There we go. Oh. Look at the Whoa. Look

**Dave Jones:** at that. Is that Is that our current shunt resistor? 20 ohms plus minus 20%. Whoa. Reifer. Reifer caps. Reifer madness. Yeah, you probably wouldn't want to power this thing up after all these years. I've done videos on Reifer

**Dave Jones:** madness. Got a 20 amp cartridge fuse over here. So, that's interesting because our We saw our metal bar join this before. So, it looks like that 20 ohm resistor is directly across there like that. Hmm. Cancel. Interesting. 20 ohm 20% Like it's just

**Dave Jones:** like a gigantic ceramic body with like a a conductive coating on the ends. That's really fascinating. I've never seen a resistor like that. Hang on. I think we have some magic smoke released. Yeah, magic smoke. There you go.

**Dave Jones:** I think there was supposed to be three there. I think there's one in the middle that has disintegrated. It's just completely disintegrated. It's goneski. Oh, wow. Look at that. You know, something of this expense, you wouldn't been it just for that. You

**Dave Jones:** would try and repair it, I'd imagine, but maybe it was coming to near the end of its operational life cuz Laser Vision Australia, they have switched over to RGB lasers because for their sort of outdoor applications and stuff like that, they just don't need

**Dave Jones:** the coherence. They just don't need the coherent brand ion lasers. So, anyway, there you go. Whole bunch of power supply stuff. Small frame, that's called the small frame power supply board. Anyway, I know you really are fishing amateurs have probably been drooling

**Dave Jones:** over that thing. Wow. That's a bit of a beast. It's a Shrek. Made in the Czech Republic. I don't know if we have viewers in the Czech Republic. It's a bit of a beast. It's only 12 It's only 10 amp, but it's 400 volts though.

**Dave Jones:** And I know you want to see in the rest of it. Well, let's have a look. As I said, these are some big ass diodes down here. I'll show you the side. Looks like we got some bridge rectifiers there

**Dave Jones:** as well, and they love how they just like big standoffs. They're using those as electrical standoffs to go up into the thing. And it looks like this is part of the water cooling block as well. So, they had to get the heat cuz the inlet

**Dave Jones:** This This the drain port on the back here. So, this says uh from laser. So, the water from the laser comes here and you do have a drain port if you want to actually Is there any water in there?

**Dave Jones:** Any water stuck in there? No, I don't think so. Um and yeah, uh and then the outlet is over there like that. So, obviously uh enough dissipation in uh the import rectifier diodes and these diode bridge here to uh warrant a uh thermal block

**Dave Jones:** and to get the heat out. And you might notice a tiny little thermal fuse just stuck on those. I've done those in like a very old video. I've used those on my uh solar sponge, my solar air heater. Um

**Dave Jones:** yeah, it's just a they open or close uh the contacts when it reaches a certain temperature. So, it's an over temperature protection. But, moving right along, down here, there you go. All this uh goes off to our head here

**Dave Jones:** and uh these are the big ass cables coming in and going off uh to the head. But, then looks like we got a little tap coming off here on each one going into three cartridge fuses here. And then

**Dave Jones:** they're buggering off uh somewhere up to the header boards up here. So, they're obviously uh tapping off that voltage there, but um not just tapping off the voltage, they're actually extracting some power from that cuz they're big ass fuses and

**Dave Jones:** big ass wires. So, yeah. And then finally, down in here, we got just like an open frame uh power supply that it'd just be, you know, generically powering um the bus over here and powering all the electronics and stuff like that.

**Dave Jones:** That'd be a mid-90s uh jobby and that's about it. So, there you go. Um I was thought that I'd have to take apart all that, but no, it's obvious uh now. Oh, I forgot to show you the diodes. There you go. Dual

**Dave Jones:** diodes, AC in, positive negative out. Thank you very much and uh we got three of those. Sorry about this dodgy camera work. Um the other one is different. There it is. Aha, the other one there. That's not a diode. That's an SCR. Your

**Dave Jones:** dual SCR. Yeah, dual SCR. There you go. That's interesting. And yeah, they've got the uh control wires coming out here and they were poking up uh through a hole in the board. Interesting. And yeah, these are probably just bridge

**Dave Jones:** rectifiers based on the configuration. So, there you go. Thank you very much again, Daryl, for uh going to the effort to save this from the dumpster. And uh keeping it for all that time and delivering it here so that we could have

**Dave Jones:** a teardown of this thing. Absolutely fantastic. And there's even bigger ones than this. This is like the runt of the litter. It's only 10 kW. Like, there's ones that go up to 30 kW and probably even uh higher. And yes, I've got all

**Dave Jones:** the manuals uh for these as well and they're very uh comprehensive. So, they don't actually have schematics, but you know, theory of operation and all sorts of stuff in them. So, I won't bore you with uh the details of all those, but

**Dave Jones:** yeah, absolutely fascinating stuff. That's just the power supply for a 10 kW ion laser with 0.1% efficiency that gets 10 W out of it. Unbelievable. Like, there you go. Hope you found that as interesting as I did. If you did, please give it a big uh

**Dave Jones:** thumbs up. As always, discuss down below. And do yourself a favor and check out that AmpHour link where Daryl and I discuss some all things to do with uh laser vision and actually designing and implementing these sorts of systems.

**Dave Jones:** Wonder how much this thing cost. If anyone knows, leave it in the comments down below. Catch you next time.
