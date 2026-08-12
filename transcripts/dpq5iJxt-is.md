---
video_id: dpq5iJxt-is
title: EEVblog #1115 - Traps In Chips - And the 7660
url: https://www.youtube.com/watch?v=dpq5iJxt-is
source: youtube-asr
---

**Dave Jones:** Hi, sometimes you can come across a sneaky little trap in a chip that you're using that can really make you come a gutsa in your design if you're not careful and if you don't read the data sheets and specify your device

**Dave Jones:** correctly. Let's take a look at an example here. Let's take a look at the LM 2776 switch capacitor inverter. Of course, this is like a variant of the classic 7660 voltage inverter. So, the 7660 will be a classic chip if you want to invert a

**Dave Jones:** voltage rail, for example. Let's say you've got a 5 V rail and you want to generate a minus 5 V rail to power op amps, for example. Like and these 7660 type voltage inverters, I put that in quote marks cuz like 7660 is like such a

**Dave Jones:** jelly bean component. Not only are there just, you know, XXX7660s, but there's many variants of these voltage inverters. It also does voltage doubling, by the way, but typically people use them for voltage inverters. When you got to go from say you've got a

**Dave Jones:** 5 V rail and you want to generate a negative 5 V rail because you've got an op amp in your circuit, you want to power it and and stuff like that. It's a very common requirement. So, you might

**Dave Jones:** use one of these 7660 voltage inverters to do that. Typically, you don't need a lot of current on negative rail of an op amp, for example. You might only need a couple of milliamps. You might need microamps. Or occasionally, there's a couple of

**Dave Jones:** high current types you might need a couple of 100 milliamps, which this one is. Look, it's 200 milliamps output current. But, we'll take a look at that. So, these 7660 voltage inverters, now they're actually not that easy to find

**Dave Jones:** parametrically at the the regular supplies like Digikey and Mouser. Let's take a look at Digikey here. If you look at the categories down here, okay? There's DC to DC switching regulators and that's actually where they're under. There's no category for

**Dave Jones:** these voltage inverters. So, if you actually go in to Here it is DC to DC switching regulators here and and you take a look at the function the topology here they're basically like really isn't like they've got an inverted one here step up

**Dave Jones:** slash inverted which you might think is the case but you've only got three parts remaining here right? So like so we can apply the filter and of course we just end up with these three from Rome semiconductor and

**Dave Jones:** they're not what we want anyway. So you can't sort by function there but if you go over to topology here and you have a look all the way down all the way with LBJ you got a charge pump down here and

**Dave Jones:** 126 devices. So we can actually get and bingo your 7660s will actually come up but the problem is is that we're literally only getting the 7660s here. We're not getting your more like specialized parts that look it's it's pretty much only 7660s

**Dave Jones:** whereas you wouldn't find the one that we're actually looking at that Texas Instruments one you wouldn't find any of those more specialized parts. So even this sub category for the charge pump just says charge pump doesn't say charge

**Dave Jones:** pump inverter just charge pump doesn't actually find all the parts available and that's not always a good thing. Now Mouser's actually made potentially a little bit better here because look you won't find them in here okay? They don't

**Dave Jones:** have the product type in this list here. You've got to know to go into switching voltage regulators down here and then if you get into switching voltage regulators bingo you do get the topology field and you get your boost inverting

**Dave Jones:** sepic but you don't want that really. You're more interested in your well you could get your boost inverting ones and stuff like that but you know, you can start selecting those, but you can select you've got charge pump and you've

**Dave Jones:** got inverting for example. So, we can apply filters. We've got 325 matches remaining. Ta-da! And this one does show up a few other switching voltage regulators. It does show up the you know, more of your other parts and

**Dave Jones:** you will get a ha which we'll see later. As some of the parts down here. So, you can get there, but it it's not particularly easy or obvious and you can potentially miss a lot of parts out there that might otherwise be the best

**Dave Jones:** choice for your application. And you might stumble across something like this LM2 double 76 which capacitor inverter might look like it it does the business. You know, you might need a few tens of milliamps output or something. It's got

**Dave Jones:** a high switching frequency here 2 MHz high switching frequency which based on the classic 7660 design actually implies a low output ripple. So, if we go over to the classic 7660 here, trust me, I'll get to the point eventually.

**Dave Jones:** The trap with this chip I'm just taking attention here. Now, the classic 7660 can be a very efficient chip or you know, like near 100% like 99% plus, but it depends on the switching frequency. It depends on the

**Dave Jones:** output impedance of the switches inside the chip cuz we have have a look at the topology down here like the basically they've got these output switching a switch capacitor voltage inverter. That's how it works. It switches the voltage on a cap and can invert or

**Dave Jones:** double the signal depending on how you wire it up. So, the impedance of those switches they're also the the amount of output capacitance cuz you're going to have a typical circuit down here like this. So, a general like this capacitor

**Dave Jones:** here, which is always called generally always called like C2 in this circuit. This is the switching capacitor over here, but this one determines how much ripple you ultimately how much ripple, but it depends on the frequency, the internal resistance of the switches, the

**Dave Jones:** ESR of the capacitor, and so forth, a whole bunch of things. So, that's why generally in most 7660 data sheets, you will not actually find a voltage ripple graph. Like you won't actually find ripple in any of the Y

**Dave Jones:** axis here versus you know, output current. You'll find output resistance here and you can see how the output resistance change with it changes with the oscillator frequency and the oscillator capacitor value in here for example. So, the higher the capacitor value, that's

**Dave Jones:** C1 value and it changes with temperature and all sorts of stuff. But they generally won't give you a ripple thing. That's because to actually get the ripple, you've typically got to you know, there's a quite a complicated little formula here that takes into

**Dave Jones:** account the ESR of the capacitor C2 there. For example, the output current of course, the higher the output current, the more ripple you're going to get. It takes into account the frequency of operation and all sorts of things.

**Dave Jones:** So, generally they leave it up to your own devices. But there are a couple of data sheets that will actually show it. So, one example would be the Maxim chip here, which is the ICL 7660 / MAX1044. Basically, you know, pin equivalent

**Dave Jones:** type thing. So, we can go down here and have a look and they will actually give us, thank you very much Maxim, a very nice output ripple here, output ripple in millivolts peak to peak here versus uh, load current. In this case, um, the

**Dave Jones:** well, they've got Why have they got two different load currents? 0 to 10 and 0 to 40 here. And with load, yeah, they've got two different graphs. Good on Maxim. Very comprehensive. Anyway, you can see that this A graph here is with uh, this

**Dave Jones:** boost mode, which is a frequency boost mode. So, the higher the frequency, it's got a pin on there, you can just boost the frequency up. So, the lower the ripple, you know, so at at 10 milliamps output current, you might get 50

**Dave Jones:** millivolts uh, peak-to-peak ripple here. And uh, but that will change if you just use the ICL7660 version on its own, you'll get B, you'll get 200 millivolts ripple, and so forth. But, and that's for a nominal output capacitance of 10 microfarads and a

**Dave Jones:** switching capacitor of 10 microfarads. So, you know, you can't First trap is that you can't just read these graphs and go, "Oh, I'm going to get 50 millivolts peak-to-peak ripple at uh, you know, like that's what the chip's

**Dave Jones:** going to give." No, it depends on the out the capacitance, but the also what the ESR of the capacitor you use and all sorts of stuff. So, they don't actually go into that. So, that's why these graphs can actually be misleading. You

**Dave Jones:** may not You might put your 10 microfarad cap in there, but depending on the voltage rating and the derating of the capacitor with the DC bias on the capacitor, and like that's a whole video. Have I done a video on that? I

**Dave Jones:** don't know, I probably should. Anyway, capacitances can change with DC bias and uh, and the type of capacitor where it's X7R or a like a Y5V, a real crap Y5V uh, class dielectric, for example, the capacitance can massively drop and not

**Dave Jones:** be It might measure 10 microfarads on your LCR meter, but you're going to get diddly squat when you actually put it in the uh, working circuit at the working voltage and whatnot. So, um, yeah, you can actually get those

**Dave Jones:** sort of uh, graphs, but generally they won't give you that for a 7660. Anyway, let's get back to this and the trap with this uh LM2776. And you might think this is a great chip because you picked it cuz it's

**Dave Jones:** available. It might be the right price. Doesn't matter. Right, let's just say that you found this chip, 2 MHz switching frequency. If you're familiar with the 7660s, that might imply uh nice low output ripple and stuff like that.

**Dave Jones:** The higher the frequency, it's got lots of current capability. You know, sounds like a good chip, right? And it's available in like a little tiny six-pin package, none of this eight-pin rubbish, right? That you get with the 7660. And

**Dave Jones:** so, let's actually go down here and have a look. And they they they actually do give you This is one of the ones that actually give you the output ripple. They're actually like right off the bat. Look at

**Dave Jones:** this. Fantastic. Now, if you look at this one here, right? You can see that output ripple versus input voltage. And you go, "Output ripple? Oh, look at that. 10 mV there down at uh input voltage." But they don't tell you yeah, I out at 100 mA.

**Dave Jones:** That's pretty good, right? At 100 mA output uh current. And that might be killer, right? That might be fantastic compared to some other 7660 type uh ones out there, right? So, you might think that's fantastic, but here's the

**Dave Jones:** trap. Look at this one over here, okay? Now, let's say you're operating at uh output current of 100 mA, right? 0.1 amps. Look, no worries, right? We've got 25 mV output ripple. Let's say that's fine for your application, right? But

**Dave Jones:** look what happens if you just drop it back. Well, let's say you're operating at like 60 mA or something there, right? But let's say that your circuit has different modes of operation, for example, or the temperature changes because that's why we have three

**Dave Jones:** parametric curves here. That's what parametric curve means. It means you have a different curve for a particular parameter. In this case, the parameter up here is the ambient temperature. So, the red one is nominal, right? So, look, that's 20 milliamps,

**Dave Jones:** 30, 40, 50. So, at like 60 milliamps there, right? You get like let's say 70, you're going to be operating at you know, 25 Let's say 25 milliamps peak-to-peak ripple. But, IF THAT TEMPERATURE CHANGES, WHOA! LOOK, YOU GO

**Dave Jones:** STRAIGHT UP this curve and you're screwed, right? Because you're you suddenly dropped to another temperature thing, right? It's It's just nuts. So, you might get one uh ripple voltage at a particular temperature, and then all of a sudden,

**Dave Jones:** wham! Changes completely at uh a different temperature or a different output current. Let's say your circuit actually has, you know, a couple of two different current modes, and it takes more current in one mode than the other. The output

**Dave Jones:** ripple can like go up like four, five times, something like that, from 20 millivolts up to like 80 or 100 millivolts peak-to-peak. And that could really ruin your day. Unbelievable. So, like and you don't get that. You don't

**Dave Jones:** get this sort of sharp response that we saw over here. Look, this output ripple, right? It just It just, you know, pretty linear with uh your output current because your traditional 7460s just have a single mode of operation. And here's the And

**Dave Jones:** here's the trick, LM2776 has a low current PFM mode operation, right? So, if you search for PFM devil's in the detail, PFM operation. To minimize quiescent current during light load operation, the LM2776 allows PFM or pulse skipping operation.

**Dave Jones:** It's pulse frequency uh modulation by allowing the charge pump to switch less when the output current is less than 40 milliamps. Bingo, and that's what we saw with that big rise in the um the output ripple there because it's

**Dave Jones:** it's completely changing modes there. It's changing frequency. So, they do this to minimize the quiescent draw from the power supply, and that might be great for your application. You know, if you're really trying to get uh lower that uh quiescent uh current. But, as I

**Dave Jones:** said, most of these things have you know, it depends on where the frequency you use them at. They can be very very efficient, but you've got to pick the right thing. And, by the way, the uh before before I mentioned it, the uh

**Dave Jones:** 7660, it does have an oscillator pin on here, and you can generally either leave that uh Where's the example app? Here we go. You can either leave that open, or you can put a uh external uh capacitor on here to select your

**Dave Jones:** operational frequency, or you can override it by feeding in an external clock. And, that's really good if you got like analog-to-digital converter sampling systems, and you don't want other chips in your system, just especially switching regulators, switching converters, switching

**Dave Jones:** inverters, stuff like this, uh DC-to-DC converters. You don't want those running at just any frequency, you know, higgledy-piggledy, right? Cuz that can interfere with uh core switching uh components inside your sampling system. So, often you want to synchronize the

**Dave Jones:** clock with your sampling clock, and then that can eliminate then your uh converter, your ADC, can actually do a real good job at eliminating those frequencies, those switching frequencies out, all that uh noise on the rail. So, you can often override there, but

**Dave Jones:** uh Anyway, the frequency of pulse operation is not limited and can drop into the sub-1 kHz range when unloaded. And as the load increases, frequency and pulsing increase until it transitions to constant frequency operation. There we go. That's what we see there. Wham, bam,

**Dave Jones:** thank you, ma'am. Not sure like right down here at like um really ridiculously low currents, it can change a lot, too. Even that can ruin your day. Going from 80 mV might be acceptable in your design, cuz you might be post-regulating

**Dave Jones:** this thing either using a low dropout regulator or uh you know, a Zener or even just some um you know, RC or LC filtering or something like that. But you know, going from 80 to 120, that could ruin your day, too. So, at light

**Dave Jones:** loads. So, you could have be, you know, got to be really careful with this thing. So, you can really come a gutser with a chip like this that has different modes of operation, especially if uh voltage uh ripple is important to

**Dave Jones:** you, because look, you got at the top here, applications, data converter power supplies, right? You might think you might see this, you know, banner um app here. These are always always almost always kind of thing. They just marketing just throw these

**Dave Jones:** terms in there just to say, you know, try and cover all the bases, cuz engineers see, you know, a lot of them will see this and go, "Oh, it's perfect for data converter power supplies. I'm on a winner. I'll use this chip."

**Dave Jones:** But of course, it it can have a horrible amount, an unacceptable amount of output ripple. Audio amplifier power supplies. Yeah, that's what you want. Huge amount of ripple on your audio amplifier power supply. Um you know, it's just like

**Dave Jones:** operational amplifier power supplies and stuff like that. So, if you've got, uh, your negative rail, you're using this to generate the negative rail of your power supply, and you've got, you know, 100 millivolts of switching noise on your negative power

**Dave Jones:** supply rail, that can ruin your day. Um, because you, you know, your power supply rejection ratio, your op-amp may not be that great. So, there you go. That's a That's a real trap, these dual mode, um, converter chips. Just watch out for

**Dave Jones:** it. So, in this particular case, like, uh, because these parametric searches on Digi-Key and Mouser aren't that great, this is where one example where you might want to go over to the manufacturer's, uh, website and use their parametric tools or their product

**Dave Jones:** categories. In this case, if you go over to TI and you go into power management devices, you know, you've got all your LDOs, but in the under the switching regulator ones, we do actually have a category down here. We've got a boost

**Dave Jones:** charge pump, inductorless, and we've got a buck boost or inverting charge pump, inductorless, 34 here. So, if you go into that category down here, bingo, you get all these chips down here. And of course, one of them is our friend of the

**Dave Jones:** LM2776 here, the switch capacitor inverter. And just based on that, you might think, "Hey, this one's fantastic. It's equivalent to a 7660." But, it ain't. Um, it's got those different modes of operation that you can really come a cropper on. But, I

**Dave Jones:** actually like the look of, uh, some of these other ones. Check this one out, low noise regulated inverter with integrated LDO. Oh, yeah. Now we're talking. So, let's have a look at this bad boy here, because one of the things

**Dave Jones:** you might want to do, of course, you might use this 7660, uh, inverter, which by the way, that it's such a jelly bean part, the 7660, I thought you go to AliExpress or something like that, they're available in tons of different

**Dave Jones:** one-hung low brands, genuine or not, doesn't matter. In the case of the 7660, it's probably not a major risk in terms of getting like, uh you know, counterfeit parts and stuff like that, unless they physically don't work at all, because

**Dave Jones:** really the um you know, the spread of operation of this thing is is and the topology is so sort of uh wide that, you know, pretty much anyone's going to uh work the 7660, especially at like low currents and

**Dave Jones:** stuff like that. If you're only drawing a milliamp or something like that, pretty much any 7660 will probably uh do the business, but uh of course, it might draw more quiescent current, it might not be as efficient, whatever. But, you

**Dave Jones:** know, generally um you're going to be okay. And and but, they might have a, you know, significant amount of output ripple, cuz you can only do so much. You can't put an infinite amount of capacitance on that with that C2

**Dave Jones:** capacitor on the output, because at some point, the ESR of the capacitance is going to take over. You're going to have a a really well, a minimum amount of ripple that you can get rid of, right? And that you can reduce the ripple to

**Dave Jones:** before the ESR of the capacitor starts going up, cuz the higher the capacitance for a given package size means that your ESR must go up. So, then it it reduces the effectiveness of reducing that output ripple, and as we saw in that uh

**Dave Jones:** complicated formula um back there. So, there's only so much you can do. You can't just put, you know, a thousand mic in there and think that your ripple's going to zero. So, you might have to do some post regulation. So, you might put

**Dave Jones:** a low dropout regulator on the output of your 7660, for example, if you need a minimum amount of ripple. But, there there's a bit of a trap there using a uh using a 7660 and then having your post regulator on there is depending on

**Dave Jones:** the voltage drop across that regulator. If you're only dropping a small the smaller voltage you drop, the less effective it becomes of filtering input noise and stuff like that. So, if you only got a low dropout voltage on it,

**Dave Jones:** then your noise might pass mostly through that regulator. So, you know, you've got to be careful there. It's not a magic putting a LDO on the output is not a magic bullet. So, let's have a look at this bad boy.

**Dave Jones:** Inverts and regulates the input supply voltage. Low output ripple. There it is. Shut down lowest quiescent current. Blah blah blah. Up to 250 milliamps output current. That's huge, right? That's enormous. Once again, 2 megahertz operation, high frequency operation.

**Dave Jones:** So, it can get lower output ripple easier. So, I want to see the block diagram of this bad boy. Where is it? Oh, come on. There it is. Output current, switched array, and then yep, you guessed it. We've got an LDO.

**Dave Jones:** There it is. So, yeah, negative band gap, low pass filter, and then we've got a low pass filter here, and a voltage out. So, there you go. It's got integrated LDO. Awesome. Let's check the price on that. See if it's actually cheaper than this

**Dave Jones:** LM72776. Hmm. Nah, unfortunately, it's not cheaper. There in 3,000 quantity, we're talking 44 cents here for the 2776 and the 27761 with the integrated LDO, it's more expensive, needs greater silicon area. They can't get the the yield on the not the yield, the you

**Dave Jones:** know, the density on the wafer. So, you know, you pay for wafer space. So, for 3,000 quantity, 82 cents. So, you'd have to weigh up that. Maybe you could get May see it might be cheaper to just go

**Dave Jones:** with the other one with an external LDO that you might get a you know, a Japan Radio Corp LDO or something like that. And you know, cheap as chips and do that. But once again, it may not be as

**Dave Jones:** effective. But this uh 27761 I rather like this. Like to have that uh LDO integrated. And what what type of powering data Once again, powering data converters, interface power supplies, operational amplifier power. So, you know, just generating a negative rail

**Dave Jones:** for your op-amp and stuff like that. But here we go, output voltage ripple. Here's the money shot. Look at this. Right? We're talking V in at 3 volts and V out minus 1.8. You're going to get higher ripple at the higher voltage

**Dave Jones:** supply. If you're going from you know, 5 to negative 5 for example. But that's really quite good. That's under a under 1 millivolt there. You'll struggle to get that kind of ripple with an external LDO. So, that's you know, it's doing really

**Dave Jones:** good. And of course, that's going to increase with the increased output current. But even at 250 milliamps Anyway, like yeah, there's no you know, weird PFM operation mode where your output ripple just goes to buggery. And yeah, neat. But check out this bad boy

**Dave Jones:** here. Now we're just like surfing for parts. I did sorry for the tangent, but you know, It's just cool. I like this one looks really groovy. Look at this. Generates low noise adjustable positive supply between 1.5 and 5 and negative supply

**Dave Jones:** between -1.5 and 5. So, it's actually got dual regulators in here. Look at this. Wow. Fantastic, right? So, for a single 5-V in, you get a regulated output. So, this could potentially replace Let's go down and look at the block diagram.

**Dave Jones:** Potentially replace two regulators in your design. So, you can put it all in one chip. So, you could have the So, you can consolidate a 7660 and some other positive voltage regulator you're using in your design and the negative filtering

**Dave Jones:** LDO on the negative rail on the output of your 7660. So, there you go. There you go. It's got two It's got a positive and negative one and a separate a totally separate positive one here, by the looks of it. So, that's really

**Dave Jones:** groovy. I like that. And unfortunately, if you go over and the price and look at the price, yep, you pay a bit more. Once again, needs more silicon real estate. So, it's 97 cents in 3,000 quantity. But, hey, that could and it's in a like

**Dave Jones:** a little pain in the ass QFN type package, but you know, it's it's not a huge but you might need that. You might need the density, right? And that could save you space and not potentially cost. You know, it might be in the

**Dave Jones:** main driving criteria is cost. You know, you may not use this part. But, the problem with using these specialized parts is that there's one source. I bet you you won't find another pin compatible one from another manufacturer with this. So,

**Dave Jones:** that's the advantage of the 7660. You can get a jelly bean part from anyone available, you know, it'll never go become unavailable, really. And you can just use then standard regulators, which have a standard pinout. Once again, you

**Dave Jones:** got a wide choice of manufacturers. But, you might have demanding requirements like you know, the ability to like you know, noise pass through dropout versus dropout voltage and all that sort of jazz. But, anyway, there you go. TI have

**Dave Jones:** some uh interesting parts in that respect. So, you don't often as a general rule you don't want to be locked into a specialized part like this if you can avoid it. Um but, you know, you may need it because you need the board space or

**Dave Jones:** whatever um or the size. So, they've got some interesting parts in here. Look at this one. Low noise negative bias generator. Woah. Well, here's a specialized part for you. Look at this funky thing. It literally like it generates a negative

**Dave Jones:** 2.32 V. Why 2.32? Because you just need Often you just need to be able to go to ground with an op amp uh or some other uh part. So, uh you can't power the part from like 0 to 5 V for example. You can't always get

**Dave Jones:** right down to 0 even you can't sense down to 0 or you can't output down to 0. But, if you have just a small a smidgen below, you know, 0.1 V below ground, then your circuit can happily sense and

**Dave Jones:** output all the way to ground. So, um often you might just need something like this. You don't need -5 V or -3.3 V. You just need -0.1 or something like that. And that's exactly what this chip does with an output ripple of 4 mV

**Dave Jones:** peak-to-peak, uh supply voltage of 3 to 5. Um 25 98% conversion cuz it's just driving bugger all. It probably only has like 10 mA tops. Um and it just generates a negative rail. That's all there There it is. Low voltage amplifier for example

**Dave Jones:** and true zero output voltage. There it is. It actually tells you by generating a negative 0.23 V rail. And that's all you need. So, that's a nice little specialized part there. Geez, how much does that cost? There you

**Dave Jones:** go. 33 cents in 3,000 quantity. So, that might do the business there. But, uh once again, that's not going Is that a um a compatible a pin compatible uh the 7660? Oh, for goodness sake. Like, just put the

**Dave Jones:** put the labels directly on here, not pin one through to pin eight and then have a table. Just just put the lazy ass whoever did this data sheet. Anyway, is that VSS ground pin two? No, that's not a 7660 compatible

**Dave Jones:** pin out, I don't think. So, yeah, you might be stuck there if you decide to uh use that part. Isn't it neat? So, there you go. Anyway, I've waffled on enough. Sorry about that. I just I started out just wanting to show this

**Dave Jones:** trap here. And it it might look obvious, you know? It might look really Look, well, there it is. The first graph in the data sheet shows you that. But, you know, if you're not paying attention, you look at this one or you know, you

**Dave Jones:** whatever reason, you didn't notice this or didn't think about the changing mode of operation in this chip and what effect it can have on voltage ripple, especially if you're doing the famed data converter power supply or audio amplifier power

**Dave Jones:** supplies where ripple is almost certainly important. And you can really come a gutser. Anyway, there you go. Traps for young players. Modes in chips. Geez. You got to watch out for it. Oh, by the way, I just thought I'd shill my own product. I

**Dave Jones:** don't do it very often. So, uh please forgive me, but it's kind of relevant. Um the micro sleeves. The micro sleeves are back in stock. I'll have to link it in the video at the end of this if you

**Dave Jones:** haven't seen the micro sleeve. And it's a neat way just to hold your parts in a static um static protective thing. You can just slide your parts in there, label them all, and it's just a real handy way to

**Dave Jones:** do it. So, yeah, it's just a really cool way to organize all your parts for a particular project. So, you might have a folder like this for a particular product. In this case, we've got like schematics and other uh stuff in

**Dave Jones:** here. We've even got uh I won't show you that. But, we've even got like waffle trays and other other parts taped inside here. So, curly is quite handy. They didn't have them in stock for a while, but they're back over on the website.

**Dave Jones:** So, I'll link it in down below. Check it out. Anyway, if you like that video, give it a thumbs up. As always, discuss down below. And as always, uh you can support me on uh Patreon. I often release videos early on Patreon. So,

**Dave Jones:** that's linked down below as well. Catch you next time.
