---
video_id: AYblSfpKRUk
title: EEVblog #419 - Thermocouple Tutorial
url: https://www.youtube.com/watch?v=AYblSfpKRUk
source: youtube-asr
---

**Dave Jones:** Hi, in a previous video I looked at this Fluke CNX T3000 temperature wireless temperature thermometer using a K type thermocouple and we tore it down and had a look inside and somebody suggested that I should actually do a tutorial on

**Dave Jones:** thermocouples. So, that sounds like a good idea. Let's do it. Thermocouples 101 and you're probably familiar with these what they call K type thermocouples. There's many different types. K is only one of the type as we'll see. But these even come with very cheap

**Dave Jones:** multimeters these days and allow you to measure temperatures over very big ranges. But how do they work? It's just a piece of wire, right? Well, yeah, effectively it is but there is a bit of science behind it to actually get a

**Dave Jones:** temperature out of this thing displayed on your multimeter. So, let's have a look at how it works. Now it all has to do with a guy called Thomas Seebeck and he discovered this effect which they call the Seebeck effect and I won't go

**Dave Jones:** into great details about how it actually works at you know the physics level. If you want to go check that out by all means. But basically what it says if you've got a piece of metal, a wire or

**Dave Jones:** something like that and there's a differential in temperature T1 T2 is a difference in temperature from one end of that wire to the other then you will actually get a voltage difference out of this thing and we can prove that. Let's

**Dave Jones:** give it a go. What I've got is a my multimeter Agilent U1272A. It's on the millivolts DC range and this has a resolution of one microvolt which is excellent for our purposes here. We're going to need that as you'll

**Dave Jones:** see. And then I've just got a wire loop on the input here. It's just soldered into two banana plugs down in there and that's it. There's nothing no trickery going on here folks. You can do this yourself. What I'm going to do, watch that reading

**Dave Jones:** up there, right? It's almost zero, which is what you'd expect, but watch what happens when I put my fingers, which are of course warm, on one of these terminals. Look at that. It starts to count up. Look at that. That is the Seebeck effect

**Dave Jones:** in action. I'm creating a temperature differential on in well in this particular loop system. And look, if I touch the other one, I can go back down. The opposite polarity. Look at that. That, folks, is the Seebeck effect. And

**Dave Jones:** no, it's not just noise pick up or anything like that. You can see if I immediately touch it, it doesn't go anywhere cuz it's got a thermal lag. It's got It has to warm up first and then it counts up. And you go to the

**Dave Jones:** other one and it counts back down. Once it reaches thermal equilibrium again, settles back down to zero, it go It should The whole system is at thermal equilibrium, you should read zero. If I get my soldering iron here, watch this.

**Dave Jones:** I'll put it in here. And once again, it doesn't immediately go anywhere, really. So, it's not noise, but when it warms up, you'll notice that it's changing temperature there because there is a temperature differential in this system now. So, it's generating a very small

**Dave Jones:** current. In this case, not as much as we saw before, but it certainly did change. Now, the reason why it changed more down here is because we're actually got dissimilar metals down in here. It's not just the bare copper anymore. There's

**Dave Jones:** copper, there's solder, there's the connectors, they've probably got some nickel plating on the connectors or something like that. That's why it can potentially jump further than what we got with just the soldering iron on the bare copper at the end of this thing.

**Dave Jones:** And if you still don't believe that it's a not picking up noise, well, let's use my micro current here. Uh we're measuring 1 mV equals 1 nA. And as you can see, it's almost zero there. So, let's touch it. And of

**Dave Jones:** course, this is a shorted on the input here because it's a current uh meter. There's a current shunt resistor in there. Granted, it's 10K, but look at that. It's going up as my finger warms that up. And we touch the other one,

**Dave Jones:** it'll go back down. So, sure, we're only generating a few nanoamps there, but as you can see, it is still generating a current. I think we can generate a little bit more though. Let's use another example here. Get rid

**Dave Jones:** of my microcurrent and directly with the multimeter here. I've got down the microamp range. And at the moment, it hasn't reached reached uh thermal equilibrium there, but anyway, if I touch that, you might see that that will slowly go

**Dave Jones:** up. All I've got is a couple of alligator clip leads here because we've got dissimilar metal junctions all through this thing. And look at that. And if we get our soldering iron in here, and we really start to ramp up

**Dave Jones:** that temperature, look at that sucker climb. So, look at that. We're generating almost 1 microamp there by just heating up that junction. Brilliant. Now, you probably think that this is a small amount of current and power, and it is, but there's a

**Dave Jones:** practical use for these. And they actually use them on space probes, for example. You may have heard of these thermoelectric generators that use a little plutonium core to generate heat, and then that heat generates uh power, you know, many hundreds of watts in some

**Dave Jones:** cases to power these space probes. And they're using exactly this, the thermoelectric effect. Granted, it's a bit more complicated than just a couple of alligator clips, but exactly the same principle. So, as it turns out, yeah, you can get it just to work with a

**Dave Jones:** single metal like a copper wire, but it's incredibly inefficient. And in practice, of course, interconnecting systems like this have a multitude of different types of metals involved. So, that's what we're going to look at with a thermocouple cuz that's

**Dave Jones:** effectively what one of these thermocouples is. It's two different types of metal. Let's take a look at this diagram here. Type A and type B. And that's exactly what is inside one of these thermal couples. There's just two

**Dave Jones:** different types of wires running down this thing to a temperature sensing point at the end. And I say temperature sensing point in quote marks because that's not technically correct. It measures a voltage differential. It's not measuring the absolute temperature at the end like

**Dave Jones:** that. And there you go. You can see the end of the thermal couple there. And there's actually a red and a yellow wire in there. And they are different types of metals or different types of alloys going back to the connector. And that's

**Dave Jones:** all a thermal couple is. Two metals joined at the end. So, when you got two different types of metals like this and a temperature difference between one end and the other, as we'll see, then you get a differential voltage out of it.

**Dave Jones:** And if you know the voltage at one end, you can determine the voltage, the absolute voltage at the other end. Now, if we take the example of two different types of alloys or two different types of metals here, we've got copper up the

**Dave Jones:** top here, just pure copper, and the other one is constantan. It's If you look that up, it's actually 55% copper, 45% nickel. And that's actually the combination of those two metals is what's called a type T thermal couple. And there is a different type

**Dave Jones:** letter for various combinations of metals, as we'll see. And we'll take a look at the K type thermal couple in detail. Now, in practice, of course, you've got the two different types of metals, okay, running down the wire. But

**Dave Jones:** then at the end, uh it's just all ruined. You've got all this connecting system, and you've got two different connectors on the end. By the way, there's nothing inside here at all. It's just goes soldered directly onto the

**Dave Jones:** connector. So, you got the solder, which is a different type of alloy, you've got the metal in these pins, and metal in these contacts, and uh you've just created a whole hotchpotch of different uh types of metal in your connecting

**Dave Jones:** system here. So, as it turns out, uh each alloy, different type of alloy or metal has a different Seebeck effect or Seebeck coefficient, which is the output uh voltage in proportion to temperature. So, when you combine the two, you

**Dave Jones:** combine the two in different ways, and they can give you different temperature ranges and different characteristics, and that's why we have different types of thermocouples. And we'll take a look at the K-type in detail, but let's take a look at this simple T-type here. It's

**Dave Jones:** just copper, so it's copper from the point here all the way back to this connector here, and then it's also copper going into your uh multimeter as well, effectively, say. And then, you've got constantan type of metal going from

**Dave Jones:** here to here, and once it gets into here, well, then you've got copper connections all the way back to your multimeter. So, uh that's why I've drawn constantan in red there and copper in blue. But, because this point here is

**Dave Jones:** the same type of metal either side, bingo, you've got the same Seebeck coefficient, then you can effectively ignore that point there. So, I've redrawn that down here to show a direct copper connection all the way back. So, now we only have two different

**Dave Jones:** dissimilar metal junctions, T1 and T2, and the output differential voltage here will be in proportion to the differential voltage between those two dissimilar metal junctions, and that is a thermocouple. Now, the key word there is temperature differential between T1 and T2. So, T1

**Dave Jones:** is our probe, effectively, the end of the wire here, which you you know, you dip in the water you want to measure, or you uh touch the surface you want to measure, or you put it inside the air

**Dave Jones:** you want to measure. And then, we've got the long cable coming out, and we've got our connector into our multimeter. So, if this end here is plugged in your multimeter at room temperature, and then you go stick this probe in your, you

**Dave Jones:** know, boiling hot water, or stick it inside your thermal chamber, or your oven that's at a couple of hundred degrees, you're reading the temperature difference. But, what if this ambient temperature changes? Well, you're going to that will directly affect the

**Dave Jones:** temperature difference proportional with the ambient temperature that you're that the multimeter or this end, or what's called the cold end of the thermocouple is sitting in. So, to correct for that, we need something called cold junction compensation. So, we'll just redraw our

**Dave Jones:** thermocouple again. We've got our two different types of metal. We've got our what's called a hot junction, even though it may not actually be hot. It may actually be colder than what's called our cold junction here, or our

**Dave Jones:** connector. So, this is our connector. This is our cold junction here. This is our hot junction over here for our thermocouple. But, of course, we want this thing to measure the absolute temperature. Otherwise, well, what's the point if it just varies with whatever

**Dave Jones:** ambient temperature we got? That's useless. That makes our thermocouple just a heap of garbage, and, you know, not very accurate at all. So, what happens is the thermocouple is actually referenced to a given a temperature reference here, and it's typically

**Dave Jones:** inside an ice water bath, or spot on 0° C. That is the reference point. And physical measurements have been done of various types of probes, the different types, the K type, the T type, the J type, and all various different types

**Dave Jones:** with different types of metals in them. And it's done by NIST, the National Institute of Standards, and they have produced a whole bunch of tables with the ice water as the reference. So, let If we take a look at these, so granted

**Dave Jones:** this does look a bit complicated and it kind of sort of is, but this is what you have to do to design and build a proper thermocouple sensing thermometer or multimeter or something like that. It's got to take these NIST

**Dave Jones:** tables into account. Well, the good ones do anyway. So, this is for the type K thermacouple, which is the most popular, which we'll be using and take a look at. So, if you have a look at the bottom of the table

**Dave Jones:** down here, there are more tables in this one, but this one goes in the negative direction. And you'll notice that it's got a reference point down here at zero, where the differential voltage, all these figures inside here are the

**Dave Jones:** differential voltage for various temperatures at the hot and the cold junction. So, the hot junction is on the vertical axis here. The cold junction temperature is along the horizontal axis. And as I said, it is referenced to 0° C.

**Dave Jones:** So, if they're both at 0° C, there we go, the hot and the cold junctions, i.e. the system is at thermal equilibrium, then it gives a differential output voltage of zero, precisely zero. And that is taken as the absolute reference

**Dave Jones:** point. And then, if your sensing end changes or your hot end junction changes by 10°, there we go. That's our differential output voltage in millivolts, by the way. So, that's 300 more minus 392 microvolts for a K-type thermocouple.

**Dave Jones:** So, if you kept your multimeter or your cold junction in a room precisely at 0° ambient temperature, then, well, you'd only use this column going down here. But, because, well, you know, real systems are used in ambient conditions,

**Dave Jones:** ambient temperatures change all the time. And that's why you have to add in the compensation along here. This one only goes up to minus 10 though, but then you can extrapolate or get larger tables for that. So, what your

**Dave Jones:** thermometer has to do is take into account all of this data based on the current ambient temperature and that's the key. It must know the the ambient temperature you're currently at or the cold junction temperature, which is the

**Dave Jones:** connector on the front of your multimeter. It has to know what temperature that is at. So, that's why your multimeter has to have an internal temperature sensor and you can see these two multimeters are really good quality one and a one hung low cheapy one and

**Dave Jones:** they both measure the internal temperature in the multimeter and you might wonder why that's the case. Well, it has to have an internal temperature sensor so it knows what temperature the cold junction here is at and in these

**Dave Jones:** multimeters, they don't actually measure that sense the temperature right at the input jacks down here. There's just a sensor somewhere inside the multimeter and usually it's going to be a cheap ass uh you know, silicon uh junction temperature sensor built

**Dave Jones:** into the multimeter chipset or something like that usually. Certainly wouldn't expect a good quality um internal uh thermistor or something like that inside one of these cheapies, but a good quality properly designed thermometer like this uh Fluke CNX t3000, it will

**Dave Jones:** have a really good quality uh thermistor inside measuring the temperature and it will do cold junction temperature compensation right at the input jacks. And you've seen this before in my teardown of this meter, but we'll have another quick look at how this

**Dave Jones:** meter implements cold junction compensation and how it does it properly. And here's how they do it. They have these two large studs, which of course are going to have a very large thermal mass or you know, relatively large anyway and these large pads down

**Dave Jones:** here, which also increase the thermal mass of this whole system. And this together, what they're trying to achieve here is what's called an isothermal block. In other words, the two junctions here are trying to be kept at an identical temperature. So, uh

**Dave Jones:** regardless of, you know, if you've been holding this connector and, you know, you've warmed it up or something like that with your fingers, and then you go stick it into the jack like this, and it has uh spring contacts which connect

**Dave Jones:** down in there, then well, these might be at a different uh temperature. Even one junction might be a different temperature from the other. And that's what this large thermal mass or iso- thermal block is trying to do. It acts

**Dave Jones:** as a thermal low-pass filter to take out that sort of stuff and keep these two junctions at exactly the same temperature, or as close to it as you can get. So, that's why all this stuff on the input here is all recessed so

**Dave Jones:** that you can't touch it with your fingers. As we saw before, just 5 minutes ago, I was able uh by touching one junction or the other, I was able to upset my reading, and that would cause big errors in a precision temperature

**Dave Jones:** measurement system. So, they avoid that with trying to create a large thermal mass here, and you'll see they've also got a thermistor going in there, which is measuring the absolute temperature at that point. So, they know exactly what

**Dave Jones:** that temperature is. They can use those NIST uh tables, and therefore give you a quite an accurate uh K-type thermocouple system, the goal of which is, of course, to have your accuracy purely determined by the probe. And so, you want as little inaccuracy as

**Dave Jones:** this thing as possible in terms of your uh thermocouple, so that they have a top-quality thermocouple in there, really accurate, and a nice big isothermal block that keeps both junctions at the same temperature. So, you should probably be thinking, "Well,

**Dave Jones:** if my multimeter or my thermometer has a real precision temperature sensor already built into it. Well, why don't they just stick that thing on the end of a probe and use that instead of this dual, you know, this silly

**Dave Jones:** dual metal thermocouple thing where you got to take all this data into account and everything else? Well, these things, these thermistors and other types of internal temperature sensors they use have a very limited internal range that they're accurate over, whereas

**Dave Jones:** thermocouples just two bits of metal can be used over, you know, sometimes many thousands of degrees Celsius range, very large ranges. And also, because they're just a bit of metal, they're extremely rugged as well. So, that's the advantage of these

**Dave Jones:** thermocouples. But, yes, to use a thermocouple, you have to go to all this trouble to measure the temperature and compensate for it. And to compensate for it, your multimeter or thermometer can either use a big huge table data table

**Dave Jones:** like that, but that takes up a lot of memory and that's sort of stuff to actually do that. So, what they often do is just use a polynomial function. And well, you've got to know your polynomial math and all that sort of stuff. So,

**Dave Jones:** NIST also publish some polynomial tables so that you can implement inside the multimeter or the thermometer that does the compensation for you. And if you actually implement a really high order version of these polynomial corrections for any type of thermocouple like a type

**Dave Jones:** K, you can actually get very good accuracy like much better than the probe itself if you actually compensate the thing like, you know, 0.05% is not uncommon. But, a simple meter like your multimeter for example isn't going to

**Dave Jones:** implement a complex polynomial function to get better accuracy really. It's not just worth it. So, they're just going to approximate this sort of thing using other simpler techniques that are computationally less intensive. And the cold junction compensation doesn't always have to be

**Dave Jones:** done in software, although that's probably the most common. It can be done in hardware as well. And there's many different ways to do it. This is just one example here. And you can actually buy chips that actually do cold junction

**Dave Jones:** compensation just like this. And you'll notice it's a traditional three op amp differential amplifier, but it's got a calibrated trimmed internal temperature sensor and compensation circuit designed just for a particular type, say a type K thermocouple. So, what all these

**Dave Jones:** practical measured values give you? Ta-da! Here it is. So, this graph here shows the output, the thermoelectric output voltage in millivolts versus the junction temperature in degrees C relative to that reference point of 0° C at the other end here. You remember the

**Dave Jones:** cold junction? This is our cold junction compensated table. And you can see it's pretty darn linear. These are the different types for the different types of material. This is the K type. So, there you go. It's about 50 millivolts

**Dave Jones:** at, you know, 1250°. Please excuse the crudity of this hand-drawn graph. I didn't have time to build it to scale or to paint it. So, you might think, "Geez, that's handy. It's, you know, it's pretty darn linear." So, your multimeter

**Dave Jones:** all it has to do is measure the voltage across the junction there and it gives you the temperature, a direct ratio. That's it. Uh, I'm afraid it ain't that easy. There's a bit more wiggliness inside here than you might

**Dave Jones:** imagine. So, if we go over here and we take a look at the actual Seebeck coefficient it is called, which is microvolts per degree C for the temperature range here on the X axis, you'll see that our K type

**Dave Jones:** thermocouple, yeah, it has a pretty constant, you know, it's kind of sort of, you know, squint your eyes, you know, it's kind of sort of linear from, you know, around about zero to, uh, you know, 1,000° C. There it starts to drop

**Dave Jones:** off the end, but it's, you know, it's reasonably flat like that. So, it gives you a fairly consistent microvolts per degree C. And of course, if we had a if this K-type was actually a flat line, then of course,

**Dave Jones:** that would translate into a completely linear curve here, but the Seebeck coefficient isn't linear at all. There's some slight variations in there. And a K-type thermocouple, which is the most common, is generally taken as roughly 41 microvolts per degree C over that range.

**Dave Jones:** That's the nominal value, but you can see when you get below 0° here, down to -200, it's dropped off. You know, it's like halved down there. So, really, these things aren't linear at all, and you can't really see that

**Dave Jones:** on this graph, but trust me, there is non-linearity in there. And although there are many more types of thermocouples than these, these are probably, you know, some of the foremost uh popular ones. And you can see why the

**Dave Jones:** K-type is uh pretty popular because it actually has, you know, a relatively flat response over a very wide temperature range, much more than the uh J-type one actually. The J-type one actually only goes up to about uh 750°

**Dave Jones:** uh C or something like that when it reaches what's called the uh Curie temperature point, and then its uh characteristic changes drastically. And you'll notice that the dip here in this uh K-type thermocouple, that's also due to the Curie point in the K-type, and

**Dave Jones:** that happens at about 350° C where you get that minimum in the dip there, but it's but it recovers after that and still provides a very wide range. So, that's why the K-type is the most popular. And like all

**Dave Jones:** thermocouples, it's uh composed of two alloys. In this case, chromel and alumel. The chromel is uh the uh positive terminal, and the alumel is the negative terminal. Chromel is 90% nickel, 10% chromium, and the alumel is 95% nickel, 2% manganese, 2% aluminum,

**Dave Jones:** and 1% silicon. And it just so happens through research they found that that combination of alloys work very well. And there's always continuous research going into the thermocouple field, and they're all coming out with new exotic combinations for various niche

**Dave Jones:** applications and things like that. But anyway, yeah, K-type thermocouple, we've seen it before. It's We've got the hot junction here. We've got the cold junction with the standard K-type connector, which will take which you've seen before. It contains one larger pin,

**Dave Jones:** which is the negative pin, and one smaller pin, which is the positive pin. And that's all there is to it. And there is, of course, as we've seen, three different ways to or do cold junction compensation. One, and the poorest way

**Dave Jones:** to do it, is you can just assume, well, it's 41 microvolts per degree C, but you can just assume it's relatively flat. And you might be, you know, 5% out or something like that at any point over the range. But yeah, you could, in

**Dave Jones:** theory, just do that, and there might be one or two, I don't know, cheap-ass multimeters that may actually do that. I don't know, but most are at least going to have a temperature sensor built in, and they're at least going to

**Dave Jones:** do a little bit of compensation, maybe using, you know, a couple of order polynomial or something like that. But of course, as we saw inside this Fluke meter, this is the way to do it properly. If you want a high accuracy

**Dave Jones:** instrument, good precision thermometer in there, all calibrated and a big isothermal block as well. That's the best way. And if you have a look at one of these K-type thermocouples, there it is. It actually tells you it's chromel

**Dave Jones:** is the positive, and alumel is the negative terminal there. And if we have a look inside the thing, as you can see, they actually haven't soldered it. What they've done is just crimped that in there, because you don't want another

**Dave Jones:** dissimilar metal junction. You want as fewer dissimilar metal junctions in your thermocouple system as possible. So, a good one will just be clamped like that. And ideally, you would also want the uh connectors here to be the exact same

**Dave Jones:** material as the uh lead as well. But, you would uh traditionally only get that in very uh precision systems. Now, obviously, because these are two specific types of alloys uh with different Seebeck coefficient specifically chosen to give you the

**Dave Jones:** maximum differential voltage between them like this, you can't just go swapping them willy-nilly. So, if you swap the polarity on it now, if we do it here, here we go, our thermocouple's reading the ambient temperature, because we're at ambient temperature, very

**Dave Jones:** little temperature difference between them like this. If we swap it, there's not going to be much difference at all. You see, it just swapped around a bit. If it was actually 24.6, you wouldn't have seen any change, but if we go up,

**Dave Jones:** look, we're going up in temperature. So, now we're actually going back down. No good. Doesn't work at all, folks. Make sure you get the polarity right. And for K-type thermocouples, there are two different tolerance classes, class 1, class 2. 1.5°

**Dave Jones:** C and plus minus 2.5° C. And it's quite similar for the other uh types of probes as well. And just for kicks, let's see if we can actually measure and confirm that uh rough uh Seebeck coefficient for a

**Dave Jones:** K-type thermocouple of 41 microvolts per degree C. So, got my K-type probe here. I've got some warm water here. We are going to use this as our absolute reference. So, it's currently 25.2° ambient temperature, and we're getting 2.75

**Dave Jones:** millivolts offset, so we'll null that out. There we go, it's near enough. Let's stick both of them in the water here and see what we get. Now, what I've got is my microcurrent here acting basically as a times 100

**Dave Jones:** amplifier cuz that's essentially what it is is a precision times 100 amplifier. So, put that in the water. Water's about 35. 35.1° and we're 39.5 mV. So, if we have a look at the data on DaveCAD here, we've got 25.2° C ambient,

**Dave Jones:** 35.1° C water. Subtract that, that's a 9.9° C difference in temperature for 39.5 mV output. But, of course, our microcurrent here has had a gain of 100. So, we have to divide that by 100. We actually got out of the

**Dave Jones:** thermocouple a differential voltage of 395 microvolts cuz that's what our microcurrent is was acting as a differential amplifier directly across the connector of the thermocouple probe. And if we take 395 microvolts divided by 9.9° C cuz if you remember, we zeroed

**Dave Jones:** out the offset, the original offset we had in the multimeter. Otherwise, we would have had to subtract it in here first. Sorry. So, you divide those and we get a value pretty close to our predicted value. We get 39.9 microvolts

**Dave Jones:** per degree C. Or if we actually plug in the number we expected, 41 microvolts, which is a nominal value, by the way, it comes out to 9.63° C. We had a 9.9° C difference. Not bad. So, we're certainly

**Dave Jones:** in the ballpark there and we didn't do any cold junction compensation at all. And of course, the K-type probe is going to have 1.5° or 2.5° C, you know, accuracy anyway because we could get more accuracy out of this if

**Dave Jones:** we did it over a larger range, of course, but very limited range. We can see we got the figure within the ballpark. Beauty. So, there you have it, folks. That's all you you to know about thermocouples. They're actually quite

**Dave Jones:** tricky to use and get accurate. You really have to know what you're doing and understand the physics involved in these things. And there's a lot more reading you can do as well. It's quite a fascinating topic. I recommend you look

**Dave Jones:** into it. And you can also have lots of fun just experiment with creating your own thermocouples. Just twist two wires together of different materials and bingo, you've got yourself a thermocouple. But just watch out for that cold junction compensation, okay?

**Dave Jones:** And because every type of metal or alloy has a known specific Seebeck coefficient, you can actually use this to determine what a particular type of metal is. And that can be fascinating in its own right. So, go ahead and play

**Dave Jones:** around with thermocouples. They're great fun. So, if you like that tutorial, please give it a big thumbs up. And if you want to discuss it, jump on over to the EVblog forum. Catch you next time.
