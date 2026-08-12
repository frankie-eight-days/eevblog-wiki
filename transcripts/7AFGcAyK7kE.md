---
video_id: 7AFGcAyK7kE
title: FPGA Implementation Tutorial - EEVblog #193
url: https://www.youtube.com/watch?v=7AFGcAyK7kE
source: youtube-asr
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, I was just working on a design that included a an Actel IGLOO nano FPGA, one

**Dave Jones:** of the smallest FPGAs on the market. And it also had a Xilinx Spartan-3 FPGA in there as well. And I haven't really done anything on FPGAs before. Everyone's been asking for something, so I thought I'd just cobble together some

**Dave Jones:** basic notes, really just some comments on implementing FPGAs. They're a little bit random. It's not exactly a step-by-step thing, but hopefully there's some good stuff in there. How you can just take a basic look at the data sheets, what you do at the

**Dave Jones:** schematic level to get the FPGA working, and then some layout stuff as well. It's a bit random, but hopefully there's something good in there. It's about an hour long, so hang in there. Okay, we're going to start out here by assuming that

**Dave Jones:** we've already picked our device, and it's going to be an Actel IGLOO nano part. It just so happens that for this design, we need something that is very small, a small number of IO, a small number of logic, a real small amount,

**Dave Jones:** and preferably very low power. And the Actel IGLOO nano pretty much ticks all the boxes there. So, let's take a look at the actual data sheet itself. Now, it boasts its nano power consumption. And it it's a 1.2 V to 1.5 V core logic

**Dave Jones:** power supply, which is great. The lower the core voltage means the lower power it's going to operate. So, so you can if you can operate from 1.2 to 1.5 V core voltage, then if you're really after ultra-low power, you're

**Dave Jones:** going to want to use 1.2. But, as you'll see later, there's a trap for young players there, so beware. We'll go into that later, but it also it's a single supply uh system device as well, which means that

**Dave Jones:** the whole chip itself can run off the one voltage. A lot of high-end FPGAs will actually require many many different um uh core voltages for various uh aspects and functions, but this one can operate off a single voltage. In this case, from

**Dave Jones:** 1.2 to 1.5, but we'll take a look at that. Um and we will uh take a look at the various devices down here. Now, what we need to look through here, this is a this is a parametric device table for

**Dave Jones:** all of the IGLOO nano devices in this series from in this case uh system gates. Here is is your basic bench line of the part you're going to let need. Now, we know for this design that we it's a very small design. We don't need

**Dave Jones:** much logic at all. I know it'll definitely fit in the 10,000 uh system gate design. So, we'll be using today the AGLN 010 device. Now, it's got uh the equivalent of uh 260 what Actel core core versatile. Um but they're

**Dave Jones:** effectively uh basically D flip-flops or configurable logic, which we'll look at uh later. Equivalent macrocells 86, that tries to that tries to be a comparison with uh the competitors like uh Xilinx and Acro and um Altera who talking terms of

**Dave Jones:** macrocells in instead of uh Actel's versatile. So, it's very hard to actually translate logic density between the various devices and how many resources you'll need and things like that. That can actually be quite complicated if your uh if your design is a very tight fit

**Dave Jones:** inside your FPGA and uh it's got a flash freeze mode. Excellent 2 micro watts consumption. Fantastic. It doesn't have any internal RAM at all or any fancy clock PLLs or anything like that, but we don't need anything like that.

**Dave Jones:** It's got four what they call VersaNet globals, but globals in FPGAs what they're talking about there is they're talking about global clocks and we'll talk about those later. And it's got two different IO banks which for this design

**Dave Jones:** might be handy because we want we may want to operate the different IO banks at different voltages and we'll take a look at that as well. And look, it comes in a only has 34 IO. I do believe don't quote

**Dave Jones:** me on this, but this could be the the smallest FPGA in the industry in terms of size and pin count as well cuz FPGAs are basically really high pin count and high logic density actual devices, but this is one of the

**Dave Jones:** smallest on the market. It's available in the UC36 package which has its good and bad points as we'll see. And if we go down to here, the IOs per package, here's our part again and it's available in the UC36 or a QN48.

**Dave Jones:** It's the only part which is available in the UC36 package there. The larger logic density devices aren't available in that and that's a bit of a shame because if you only need a small number of IO, it basically forces you to choose the

**Dave Jones:** smallest logic density device. Why can't you have a larger density device like the AGL N020 in that package? I don't know. Good question. You have to ask Actel / Microsemi. Um but you'll see that the other devices are basically scale up into larger uh,

**Dave Jones:** count packages. So you can't get these high-density ones in these, um, in smaller, uh, in smaller packages. You You basically go up in size, um, once you meet logic density, and that's pretty standard in the industry, really. And if we take a look down here at the

**Dave Jones:** UC36 package that we're going to use, 3 by 3 mm. It is tiny, 9 sq mm total, and it's got a pin pitch of 0.4 mm. Absolutely tiny and can be a real pain in the ass when you're trying to solder

**Dave Jones:** this thing. And here is a good, uh, representation telling you what, uh, Versatile, what you can do with one of these, uh, Versatiles. Each one of those building blocks inside the FPGA. Uh, they're also called macrocells in in

**Dave Jones:** other, uh, products, and they go under various other names, but you can do, like in this case, a three-input lookup table, uh, logic thing. Or you can do a D flip-flop that has, uh, an an actual clocked, individually clocked flip-flop

**Dave Jones:** which has, um, data and clear, and once again, a more advanced, uh, D flip-flop with a separate enable pin. And that allows you to do a whole bunch of stuff, and you can build up your design based on these basic, uh,

**Dave Jones:** flip-flops and, uh, logic element lookup tables. They're very powerful and very versatile, as the name goes, Versatile. Go figure. Just a quick note with ordering parts here, it actually can be quite complex. This one's relatively easy, but some of

**Dave Jones:** the more advanced FPGAs can be a real pain in the ass, and you've got to make sure you order exactly the right part number with the right, uh, letters over here like this. If you don't do it, then

**Dave Jones:** you'll end up ordering the wrong part from Digi-Key or Mouser or someone, and you'll end up with the wrong package or something like that. In In this case, the first part here is the model number, of course, how many system gates you

**Dave Jones:** got. Then you've got this digit here, which it says V2 is 1.2 to 1.5 V supply. So, if you wanted to operate at 1.2 V and you accidentally ordered the V5 part, oops, it may not work. You might

**Dave Jones:** be in big trouble there. Um and the you've got to order the Z if you want the nano the the low-power nano device. And V this one up here tells you what package type. In this case, we're using the UC

**Dave Jones:** microchip scale package, the UC36. But, you've got to choose the correct one for your you know for your particular build. Otherwise, you don't want to order the wrong chip and then you can't solder it on your board because you've got the wrong footprint.

**Dave Jones:** Oops. And then, of course, you've got lead-free as well and the lead count as well. But, really, if you order that one, you know, you you're pretty much know you're going to get the right pin count, pretty obviously. And the

**Dave Jones:** temperature range as well. Do you want the industrial or the commercial temperature range? Most of the time, you're just going to want the commercial temperature range. But, if you can't actually get that in stock, you can actually order the industrial

**Dave Jones:** temperature range. And it just works over a wider temp range. It's even better. Generally, they cost more, but if that's the only one you've got in stock, well, you order that. So, just be wary that you order the exact part

**Dave Jones:** number you need. And here's the basic internal diagram of what these Actel IGLOO FPGAs look like. Now, on the on the left and right side here, we've got the bank IO. They're actually the IO pins. Each one of those little pads there is the IO

**Dave Jones:** pin effectively. And it's got two different banks, bank zero and bank one. Now, don't worry about bank one at the top here and bank one down the bottom. The smaller device we have only has the small number on the sides here, but

**Dave Jones:** that allows, having separate IO banks like this, allows you to um uh operate those IO pins at different voltages. So, if you're uh trying to translate, say on the left side here, if you've got a 2.5 V IO bus coming in, you can translate that

**Dave Jones:** into say a 3.3 V on the uh other on the right-hand side here to bank zero, and that can be very handy. Uh and because all Actel non Actel FPGAs are all non-volatile flash FPGAs, uh which is different to

**Dave Jones:** the uh volatile nature of the Xilinx and the Altera parts, you don't need an external configuration prompt, which we'll go into. So, that saves up board space, cost, and a whole bunch of other stuff. Um it's got the flash freeze

**Dave Jones:** technology built in, whatever that does, powers it down, and it's got built-in charge pumps to generate the high voltages required for the flash and uh any other functionality. And uh these parts in the corner, these are CCLs or

**Dave Jones:** global clocks, um the FPGAs will have global clock inputs, and they're very you must use those to route ef- efficiently route your clocks throughout the design, i.e., in the middle between all these little VersaTiles. And we talked about the

**Dave Jones:** VersaTiles before, they're the little logic blocks which are used to build up your design inside this FPGA. But uh clocks are very important in any digital design, and you have to feed those into the global clock pins. It's

**Dave Jones:** very important. You can feed them into the IO, but then you get extra delays, and it's got to go through the logic, it uses up extra logic, which could be used for your design, and things like that. So, trust me, you want to feed your

**Dave Jones:** system clock or other clocks, whatever it is you're working on, uh into a global clock pin, and then it goes between all of these uh elements and allows you to more effectively and uh and route your clocks throughout your

**Dave Jones:** design, lower propagation delays, faster uh faster speeds for your design, and things like that. And if you're really curious to see what's inside one of these VersaTiles, the actual uh configurable switching elements in there that make up uh all that

**Dave Jones:** versatility, here it is. Um this is not in the data sheet. It's in As with all these FPGAs, it's everything's not in the one data sheet. They have application handbooks. And in this case, it's the i GL nano FPGA fabric user's

**Dave Jones:** guide. And it tells you all about the FPGA, what's called They call it the fabric of how the FPGA uh works and how it's made up. So, there you go. Uh follow that to your heart's content. Knock yourself out.

**Dave Jones:** And if you're even keener, you can get into the routing architecture of the FPGA and how you can route between various uh VersaTiles and run your clocks and things like that. But uh generally, unless you're trying to really optimize

**Dave Jones:** your design, uh the FPGA tools will actually uh take care of this for you. But it's good to have knowledge of how these things optim- actually work and how you can optimize them uh because it can be the difference between your your

**Dave Jones:** uh actual design and the FPGA operating at 10 MHz or 20 MHz, for example. If you don't put the uh clocks near the IO or the banks that you want or things like that. So, uh just be aware that uh when

**Dave Jones:** you're designing with FPGAs, you have to consider often have to consider a lot of this stuff if you're trying to optimize your designs and you're wondering why you compile it and uh oh, it you know, it's telling me it only works at 10

**Dave Jones:** mega- MHz and I wanted the thing to work at 20. Oops. So, there's lots of things to uh consider. Uh it can be a good read to actually uh sit through and read these manuals. Now, here's a part of the

**Dave Jones:** data sheet you really want to take notice of. This the basic recommended operating conditions for the various pins. So, down in this uh left-hand column down here, we've got our uh pins, VJTAG, VPUMP, and VCC pins, and IO pins,

**Dave Jones:** and all sorts of things. And uh what specs they operate at. Now, let's take a look at our um intended device here is our 1.2 to 1.5 V um power supply. Our VCC power supply core voltage can operate, sure enough, as it

**Dave Jones:** says, from 1. uh 2 to uh basically 1.2 to 1.5. It's got a bit of margin uh there either side, but they're the basic operating things, as you'd expect. Now, the voltage for the JTAG pin, which we'll take a look at later, uh it can be

**Dave Jones:** in the range from 1.4 V to 3.6 V. Fantastic. Okay? Now, our VPUMP uh programming voltage, okay, during operation, can be anywhere from 3.0 to 3.6 V, cuz it doesn't care when the device is just operating. It's probably

**Dave Jones:** not uh it's not really used at all. But, during programming mode, here's a bit of a trap. 3.15 to 3.45 or 3.3 V. Are you standard 3.3 V? That's what it needs during programming mode. Now, you remember back at the start, we said this

**Dave Jones:** device was a single supply voltage chip. Now, in that in theory, everything can run off the one supply voltage. In this case, say 1.5 V. Well, that's true during operation, but during programming, you can't operate this thing at 1.5 V. You have to operate

**Dave Jones:** you have that pin has to be 3.3 V. So, it's not really during programming mode a true, uh, single supply device because you can't operate the core voltage at 3.3 V, you have to have a voltage regulator on

**Dave Jones:** there from 1.5. Well, what's what's the big deal here, you ask? Well, that means that you've got to put extra, uh, DC-to-DC converters on your board to cater for this stuff and that adds to your bill of materials, your cost, your

**Dave Jones:** board space, everything. So, just be wary of that. It can be really annoying. Now, uh, VCCPLL, our chip does not have an internal phase lock loop, which is what a PLL is. Uh, so we don't have to worry

**Dave Jones:** about that, but if we did, if we use one of the higher-end, uh, Actel Igloo devices, we would care about that and once again, it's from 1.2 to 1. uh, five It must The PLL must run at 1. five 1.2 to 1.5 V. It can't run

**Dave Jones:** off 3.3 or anything else. And our, uh, VCC IOPs, uh, they can operate anywhere from 1.2 V to 3.3 V. So, that means that this device is not what's called a 5-V, uh, TTL-capable, um, interface device. So, if you were

**Dave Jones:** looking at interfacing, uh, 5-V TTL signals to this this FPGA, you can't do it. You would need a voltage level translator. So, that's a bit of a trap. Don't assume that all FPGAs are 5-V capable because they aren't.

**Dave Jones:** Now, something even more important than looking at your basic recommended operating conditions is looking at these little numbers here. See these little, uh, asterisks there? Look, notes, little note numbers. In this case, the VCC core, note number four and five. Let's

**Dave Jones:** go down and take a look at what this has to say down in the fine print, shall we? It's printed under the table here, often in much finer print than what's here. So, number four, for IGLOO V 2 nano device only operating air, we

**Dave Jones:** don't care too much about that. But look, number five here, real trap for young players. It says the IGLOO nano V5 devices can be programmed with the VCC core voltage at 1.5 volts only. IGLOO nano V2 devices can be programmed with

**Dave Jones:** the core voltage at 1.2 with the FlashPro 4 unit only or 1.5 volts. Ah, if you're using the older FlashPro 3 unit and want to do in-system programming using 1.2 volts, please contact the factory. Now, what this means is that you can be left um up the

**Dave Jones:** creek without a paddle if you uh if you connected your core voltage, your VCC core voltage to 1.2 volts as they claimed all the way back on the front page of the data sheet. They said it could operate at 1.2 volts and it can,

**Dave Jones:** but it cannot be programmed at 1.2 volts. You have to have the VCC core voltage at 1.5 volts during programming. And it also tells you this, it highlights this in the FlashPro 4, which is the in-circuit JTAG um serial serial

**Dave Jones:** programmer for this for the Actel IGLOO devices. It tells you that in the fine print in that user guide as well. So, just be careful. Don't believe everything you read on the front page specs of the data sheet. And yet another

**Dave Jones:** thing to consider, calculating power dissipation, beware of the figures that they use. That 2 micro watt consumption figure for the flash freeze mode, that's assuming these conditions and various other things, sleep, shut down, no flash freeze. Here's a table of the power

**Dave Jones:** supply configurations where the specs are valid. and then it goes into quiescent uh currents during flash freeze mode and then you've got quiescent currents per IO banks and things like this. It can get really complicated and this is a very very simple FPGA and

**Dave Jones:** here's an interesting figure the dynamic power consumption in terms of microwatts per megahertz for for various IO input buffer power like that. It wow, you know, it can get quite complicated and here's a more device specific dynamic power consumption figures for the for

**Dave Jones:** various combinations of these things. You'd have to go and check out the user guides to figure out what all these means. The clock contribution to the versatile used in a as a sequential module is going to have well, in this case for our design 0.143

**Dave Jones:** microwatts per megahertz. Ah. Can get bloody complicated. Good thing that they a lot of the manufacturers have power dynamic power consumption estimate calculators to do a lot of this stuff for you, but often you'll have to go in

**Dave Jones:** here manually to do ballpark calculations of how much power your actual design your compiled design is going to take at a specific frequency and we haven't even scratched the surface there. Can be very complicated stuff and this is not a

**Dave Jones:** complicated FPGA, but look at all this stuff you got to read. Oh my goodness. Well, enough of that data sheet business. Let's actually do a schematic and see the basic things we have to do to get a functional FPGA

**Dave Jones:** design up and running for something like this very simple Actel IGLOO. This is as simple as it gets. So I don't think other FPGAs are this easy. Trust me, they're not. Okay, as we might look at now. Uh you'll see that I've placed the part

**Dave Jones:** here and before anyone asks what package am I using, it's Altium Designer, okay? No more needs to be said. Now, uh we have to the two different banks. Now, it separates uh bank zero and bank one into two specific uh banks. And the reason it

**Dave Jones:** does this is because down here in this one here, you'll notice that there's a separate VCC pin for VCC um input for bank zero, B0 there, VCC in for input for uh bank one. So, you have a different power supply voltage. So,

**Dave Jones:** this B0 pin, C5 there, powers the IO pins on this bank. The other pin, D2 there, powers IO on bank number one. So, if you were doing a voltage translation design, as we mentioned before, and use uh say you want to have a bunch of IO

**Dave Jones:** and you wanted to bring them all into this um bank zero and you wanted to operate that at say uh 1.8 V or something like that, you would tie C5 to 1.8 V and if you wanted 3.3 V

**Dave Jones:** output, you would put all your uh output pins or your other IO pins on to bank one here and then power bank one from uh 3.3 V. So, you can uh generally that's just very versatile. But, in most

**Dave Jones:** designs, you'll generally be operating from a single power supply voltage. So, in that case, you might say put both of those pins to 3.3 V. Now, um I'll copy this over into a working design and uh see what we have.

**Dave Jones:** Now, on these banks here, these each IO pin is capable of not only IO, but lots of other stuff as well. And they would generally um in the in the pin outs for the device, they will tell you that some

**Dave Jones:** of these pins can have four, five, or six different functions on them. They can be incredible. Now, in this case, because we've got a very simple FPGA here, only a couple of these pins have different purposes. You'll see that pin

**Dave Jones:** A4 right up the top here is GDC0 or global clock zero. And once again, you can go in and figure out what these things mean. There's lots of lots of obscure names, and they change from manufacturer to manufacturer. But

**Dave Jones:** generally, if you see the the term G there, you can generally sniff out that that is a global clock pin. And that can be very very important, as we'll talk about. Now, down here, well, as you can see, there's other pins

**Dave Jones:** in bank one, another two global clock pins down here, plus the FF pin. If you go to the data sheet, that's the flash freeze pin. So, if you want to enable the flash freeze functionality, say you want to have a switch on your board or

**Dave Jones:** controlled from other circuitry, then you wouldn't be you might not be able to use that IO pin. You might lose that pin for the flash freeze functionality. And once again, for the global clocks, you can either use them as IO or clock

**Dave Jones:** input. In this case, you might want to use your main oscillator might be fed into global clock zero here. And in in that case, you would lose one of those IO pins for that functionality. Another major thing that you're going to have to

**Dave Jones:** deal with is the JTAG programming interface. Now, because this is a flash-based device, we don't have an external prom here, which I'll show you another example of a Xilinx part that needs that external flash prom. But in this case, we can hook our JTAG program

**Dave Jones:** programming in-circuit system header header connector to directly up to the JTAG pins on the FPGA. And there's five pins here which you need to hook up. These are a JTAG standard JTAG stands for Joint Test Action Group. And JTAG

**Dave Jones:** was originally originally designed for in-circuit testing and boundary testing of the IO pins of the device. So, after you've assembled your board, you hook up JTAG and you can actually test that there's no shorts on the output or

**Dave Jones:** something like that. But but really it's morphed into like a generic programming interface for the device. So, this is how you program your your design project into the flash into the Actel device itself. It's via this JTAG interface.

**Dave Jones:** Now, um this will the header you use will totally depend on the JTAG programmer you're actually using. In this case, we're using a FlashPro4. That's what this pinout's for and that that's an Actel that's that's the genuine Actel flash

**Dave Jones:** programmer. But, you can use others on the market if you so desire. And they may have different pinouts. So, make sure you get it right and don't confuse TDI and TDO, input and output, and things like that. Now, you can actually

**Dave Jones:** daisy chain devices together. So, if you've got more than one FPGA, you can actually daisy chain the input and output pins. You can have basically as many FPGAs or other devices on that one JTAG serial bus. And next we've got the various core

**Dave Jones:** and IO voltages and the JTAG and the voltage pump things. Now, we've mentioned that the different banks can have a different IO voltages. In this case, I've got them both the same at 3.3 volts. But, I could go in there and

**Dave Jones:** change that to say 2.5 volts if you supplied 2.5 volts or 1.8 or any other core voltage you want. And of course, you're going to want a bypass capacitor on each of those voltage pins. Now, sometimes, because this is a very tiny

**Dave Jones:** device, we've only got one pin, but sometimes you might get four, five, or or even more pins for that one voltage bank, and they all have to be tied to the same voltage, and preferably, maybe potentially even very high-speed

**Dave Jones:** device designs, you may have to individually decouple those pins as well, and we'll go into that when we lay out the board, but for most generic designs, especially on a small package like this, you you know, you're going to

**Dave Jones:** get away with just well, you will, cuz there's only one pin. You just need the one bypass cap per pin, or you could even tie them together and possibly get away with just one bypass cap for both pins, but it depends on the location of

**Dave Jones:** your bypass cap, if you're using ground planes, what speed is your design, all all that signal integrity stuff, all that nasty stuff is, you know, really hard to know unless really hard to model even. You really have to know you're doing, but don't let

**Dave Jones:** that scare you. Okay, a bypass cap per pin like that is going to do the business no problem whatsoever. And over here, we've got D3 and D4. They're two VCC pins. Once again, bigger FPGA, you might have a dozen VCC pins you have to

**Dave Jones:** tie, a dozen core voltage pins. In this case, we're happy with just that one. Now, because we've got two pins, I'll use two bypass caps on there. I'll mix it up a bit. I'll put a 100 n and a 1

**Dave Jones:** microfarad on there just for a bit of extra capacitance on the main core. Generally, you will want that you've got to be careful, especially on say the Xilinx devices and big non-flash-based devices, they can have very large startup currents when you

**Dave Jones:** when they actually program the thing at startup, and you need a lot of uh bypass capacitance, a lot of bulk capacitance there to actually handle the charge. But, once again, don't let it scare you. Don't get buried in the details there.

**Dave Jones:** And uh we want to power this from 1.2 to 1.5. I've actually got, because this is a prototype board, I've actually got a core of a core voltage select header here. So, we can actually program the thing. You can move a jumper across,

**Dave Jones:** program it at 1.5 V, and then put it down to 1.2 V. But, but if you were designing this into a more intelligent um system, then uh you would maybe have a uh FET in there or something to control

**Dave Jones:** your DC-to-DC converter, which select automatically selected the voltage during programming, and actually, that's what this pin this unused pin four up here up on the JTAG adapter is designed for exactly that purpose. It's designed for driving a MOSFET, which then can

**Dave Jones:** control the output voltage of your DC-to-DC converter during during the JTAG programming mode, and then so switches up to 1.5 during programming, and then down to the minimum 1.2 during operation of your device, so that you can draw the

**Dave Jones:** minimum amount of power consumption. Or, if you didn't want to worry about all that crap, you just tie the thing to 1.5 V. No worries. Now, uh the JTAG pin here, this is the voltage that uh you want for your JTAG

**Dave Jones:** interface. So, this E6 pin here actually controls the IO voltage on your JTAG interface here. Now, generally, most good uh JTAG ad- adapters can handle any voltage, and that's why I fed back a sense line going all the way around here back to here.

**Dave Jones:** It'll have a voltage sense input, so the in-circuit programmer knows what voltage is being used. It can sense it, and then handle the IO translation accordingly to drive the chip at the correct voltage. Woo, it's too hard. And

**Dave Jones:** uh in a specific case of the Actels, it requires a V pump voltage down here on the E4 pin, and that is supplied directly from the JTAG programming adapter. And you can read all about this uh typical interface. It gives you

**Dave Jones:** example circuits in the um in the data sheet for the JTAG programming adapter. In this case, the uh the FlashPro 4. And down here, we've got two extra pins, which are the ground pins. Once again, just tied to ground.

**Dave Jones:** They must both be tied to ground. More advanced FPGAs might have 20 or 100 ground pins. I'm not kidding you. And just on the power supply aspect, if you're powering your design from say a 5-V plug pack or any other voltage plug

**Dave Jones:** pack or some other supply, then uh you're going to need a couple of voltage regulators. In this case, you're going to need a uh 3.3-V voltage regulator for the IO if you're using it at that. Uh generally, you will be um unless your

**Dave Jones:** entire system runs at uh 1.5 V, then well, you can get away with just this 1.5-V voltage regulator. Now, as we talked about, this is where you may want to include that uh FET in here to change the value of R28 here to change the

**Dave Jones:** output voltage between 1.5 V and 1.2 V. If you want to get tricky and uh just and and actually minimize your power consumption by operating your FPGA at 1.2 So, this is where you would uh do that in your DC-to-DC converter here.

**Dave Jones:** I've done it as a jumper because it's just a prototype um board. But yeah, if you want to get fancy, uh some uh larger FPGAs can require three, four, or even half a dozen different IO voltage IO voltages for a typical design. It's

**Dave Jones:** crazy. You might have 5 V, you might have some uh 5-V logic stuff, you might have 3.3-V, V, you might need 2.5-V for some phase-locked loop stuff, you might need 1.5-V, you might need 1.2-V, you might need 1.8-V for some other

**Dave Jones:** logic. Can get crazy, get carried away. Even a basic design, a lot of chips, a lot of more advanced chips these days might only work at say 1.8. Well, in that case, you're screwed. You got to add another 1.8-V voltage regulator to

**Dave Jones:** your design. And that's something to think about upfront when you're actually designing your board, especially if you've got size constraints or budget constraints or something like that. You don't want to be including half a dozen voltage regulators. And FPGAs, of course, aren't magic. They

**Dave Jones:** don't have any internal clocks that are of any use to your design, generally. So, really, your for your system to work, you're going to want to supply an external clock from either an oscillator, like we are in this case. Here we go, we've got

**Dave Jones:** a 3.3-V oscillator here, a standard packaged oscillator with its own bypass cap there. And it might be say 20 MHz for a typical a general FPGA system, something like this. And you'll notice we've mentioned we're feeding it into a global

**Dave Jones:** clock pin. This is very important because if you feed it, as we said, if you feed into one of these IO pins up here, which you can do, cuz they are general purpose IO, and you can route those through to

**Dave Jones:** other parts of your design, but it's very inefficient in terms of layout, it's very slow in terms of system speed, and there's some In fact, there's some versatility which you can't get unless you feed the system clock into a global

**Dave Jones:** clock pin. Very, very important. Make sure you get it right, otherwise you'll wonder why you hit the compile button on your uh, on your FPGA design and it says, "Sorry, I can't do that." Or, uh uh, or your design only operates at 1

**Dave Jones:** MHz. Tough titties. Now, just as a bonus, I'm going to show you a different design here that, uh, doesn't use an Actel Igloo part. It uses a Xilinx Spartan-3 part, and it's the, um, Spartan, um, XC3S250E device uh, 4VQ100C.

**Dave Jones:** So, it's a 100, uh, pin quad flat pack package, which is really quite, uh, usable, really easy to, uh, solder package. Now, this is not a high-end FPGA at all. Um, in this case, it's only got, uh, four, uh, banks. And, um, you

**Dave Jones:** know, it's it's a pretty, uh, not not super low-end like the Igloo, uh, we were looking at before, but, uh, it's certainly not a, uh, high-end FPGA device, that's for sure. It's quite, uh, cheap and simple. But, once again, look

**Dave Jones:** at these. We've got the same thing happening here. We've got the different banks. And you'll notice some of the things we saw before. We need a system clock, like we just mentioned, but it's got some weird stuff. What's this H swap

**Dave Jones:** thing? Well, you'll have to go to the data sheet to find out, won't you? Look at this G clock, 11 there on pin 91. All these all these global clocks, uh-huh. We've mentioned those before. Vref, what's that? You'll have to go to the

**Dave Jones:** data sheet to find out. This lowly pin, pin 92 here, it doesn't do much else. It's pretty boring. It's only got one generic IO. And, uh, look at these other, uh, things here. Some of these pins are what's called, uh, IO LO5P.

**Dave Jones:** And, once again, same thing, IO LO5N, positive and negative. That indicates that this is a differential. You can actually use these as differential, um, IO, not just standard single-ended, um, you know, 3.3 or 1.5 V IO. They can be

**Dave Jones:** differential. You can configure them in lots of, uh, weird and unusual ways. Poor old 92 there does nothing. They they short-change that poor sucker and take a look at bank number one here. We've got some other mysterious stuff.

**Dave Jones:** What's this RH clock? Well, that stands for right-hand clock and that literally means the right-hand part of the chip of the physical die itself. And if you want to know what all that and what that actually means, you'll

**Dave Jones:** have to go read the Xilinx data sheet for this device and the app notes and the configuration. What's this CSO? Look, pin 24, what's that do? Init B. Hmm, why have I got that Init B pin tied high to 3.3? Well, there's a reason and

**Dave Jones:** it goes all the way down here and it goes into the the output enable and reset pin of a Xilinx FPGA configuration device. Hmm. Time to look at the data sheet for that, which we won't go into. We don't have

**Dave Jones:** time. But, um because this Xilinx uh Spartan-3 part is a is not a flash-based part like the IGLOO, it is a RAM-based part, it needs a separate chip. This is actually a separate configuration chip here and in fact, I think it's a 1-point it's a

**Dave Jones:** 1-megabit in-circuit serial configuration flash PROM. So, this external chip is what actually holds your program. And when you power up your board, the FPGA is blank, it's dumb. It doesn't know what to do and has to sit there and wait until some

**Dave Jones:** internal circuitry in the FPGA, in this case it does have its own clocks and things like that for this specific purpose, it actually loads in uh the configuration program, which you've stored in your configuration PROM here. And once again,

**Dave Jones:** what's this little note I've got here? FPGA configuration. It's in what's called master mode serial. And if you want to know what that is, you'll have to look at the Xilinx FPGA data sheet. You got to know this stuff cuz if you

**Dave Jones:** don't get it right, then you'll then you'll build up your board and wonder why it just doesn't boot up. It doesn't load your program and things don't work. And if you're a beginner, it can be a real pain in the

**Dave Jones:** ass. But we're using master serial mode, which means you got to tie these pins M M0 M1 and M2 to low. And if you go up here and have a squeeze around here, look, there's the M1 pin combined with

**Dave Jones:** an IO pin. So it loses an IO pin. We're going to tie that to ground. M0 there and M2 is down, I don't know, somewhere down here. Your guess is as good as mine. It's there somewhere. There it is,

**Dave Jones:** M2 in that device there, pin 39. You got to tie those low to put it into a boot configuration mode that talks to this prom. It can get even more complicated than that if you want to program your

**Dave Jones:** device via an external micro or something like that. Crazy. What's all this What's this IP stuff? More VREF things, read write pins, all sorts of stuff. It can get very complicated. It's crazy. And once again, this will be

**Dave Jones:** fairly familiar to you to you. It'll It's the JTAG pins, the JTAG interface pins on the FPGA, TDI, TDO. Now in this case, it's actually It's hard to look at the configuration here, but this external prom is actually in series with

**Dave Jones:** the TDI and TDO lines on the JTAG interface. In this case, we're using the Xilinx 14-pin JTAG interface. And once again, they've got example app notes of how to actually configure these devices and stuff like that. But just be aware that this is the

**Dave Jones:** complexity you got to go to just to start up, just to boot this particular Xilinx Spartan 3 FPGA. What a pain in the ass. Now, um as per the actual igloo, we've fed our system clock here, our system clock, you

**Dave Jones:** would feed into one of these global clock pins. Look at them, there's at least 11 of them. There's a lot, but in this case I've fed it in all the way down here, which is pin 40, which is the

**Dave Jones:** global clock, too. Um in this case it really doesn't matter, or it shouldn't matter, which global clock I put that into. Uh but double check that in the data sheet because there might be a small trap there. Not all models of FPGA

**Dave Jones:** are the same, even if they're from the same manufacturer. Now, here's an interesting one. I'm actually using the um this particular design actually has the Altium JTAG interface as well, and it's got what's called a uh soft JTAG

**Dave Jones:** interface. Um now, you'll notice that the uh soft that the what's called the soft T clock pin here, don't worry about the details, but it's basically a clock pin. Now, uh that I because it's a clock pin, and uh I want it to operate be

**Dave Jones:** fairly efficient and operate at fast speeds, I've ensured that the clock pin here actually goes into pin 32, a global clock pin. So, just be careful if you're um same if you've got say an SPI bus or something like that, and you want it to

**Dave Jones:** operate really quickly, well, the clock pin um you might want it well, you might want to hook up to a global clock pin. Uh just just be wary of that or if you've got some other uh clock-based system, very important. And that's why

**Dave Jones:** these FPGAs have so many global clock pins. It just allows you to um uh do really complex uh clock really complex designs with multiple system clocks and things like that. And what sort of power supply voltages does this

**Dave Jones:** device need? Well, I'm glad you asked. In this case of the uh Xilinx Spartan-3, I'm using um once again, different banks. Here we go. The VCCO zip bank zero, bank one, bank two, bank three. I've tied them all to 3.3 V cuz it's not

**Dave Jones:** a multi-voltage um interface uh interface design, this one. I've only used two bypass uh caps because uh this is not a particularly high-speed design, but if it was, you might want to have um bypass pins on even every one of those

**Dave Jones:** pins if you really uh have to. So, because these pins are spread out a lot, look. Um pin 82 is not next to pin 97 on the actual chip, right? It's not right next to it. If it was, then you could

**Dave Jones:** get away with the one bypass cap, but they've actually spread those pins um for for speed reasons and all sorts of other really tricky stuff. They've actually spread those pins apart on the device, and you'll notice none of them

**Dave Jones:** are next to each other. So, um you know, in really high-speed designs, you might want a bypass cap for each one of those pins. It can get really annoying. Now, we've got what's called VCC aux over here. Um that's for auxiliary uh stuff

**Dave Jones:** within inside the FPGA. Read the data sheet if you want to know more, but it must be 2.5 V. This is the only thing in my design that needs 2.5 V. How annoying. I've got to now have a separate voltage regulator up here.

**Dave Jones:** This one has four 3.3, 2.5, 1.5, and 1.2 V. Uh how annoying because the not only do we need 2.5 V for the um auxiliary up here, but we need 1.2 V for the core. It doesn't operate at uh

**Dave Jones:** 3.3 or 2.5. So, bingo, we've just increased our system cost and complexity again by adding extra voltage regulators there. And once again, you might want to bypass each of those uh pins. I'm I'm going to get away with just two bypass uh pins for each

**Dave Jones:** group of four power pins there. And once again, it has a whole bunch of uh ground uh pins on the device, which you'll typically want to tie uh directly down to your uh down to some sort of ground plane on your bottom

**Dave Jones:** layer or an internal layer for multi-layer design, especially if you've got BGA devices. All right, let's take a look at the Actel IGLOO part here on a real FPGA. This is a fairly small board. It's only 50 mm by 33 mm. Couple of 0.1

**Dave Jones:** in headers here. There's the uh JTAG interface down here. No 0.1 in um dual row pin header down there. Pretty standard, but look at the size of this chip here and a couple of 0603 surface mount uh bypass caps. Let's take

**Dave Jones:** a look at the chip. It is absolutely tiny. And if we have a look at the uh 3D view here, you can see that the FPGA itself is only 3 mm by 3 mm. And it really is not much bigger than than the

**Dave Jones:** footprints of the two 0603 bypass capacitors here. Absolutely crazy. It's That's how small this device um actually is. It's one of the I think it is the smallest FPGA on the market, but uh I mean, we can go for smaller

**Dave Jones:** bypass uh caps there, of course, but um really, you know, it depends on the design you want to do. This is a prototype, so I'm going to use 0603. Now, the device, as we've mentioned, is a 0.4 mm pin pitch. So, it's 0.4 mm between

**Dave Jones:** each one of those pins. Now, this is a This is a standard uh footprint for this for this particular BGA device. It's 36 pins. You can see the tiny little pads in there. Now, um the first thing you're

**Dave Jones:** going to want to do when you put this down is to figure out how you're actually going to uh route out or what's called fan out the pins on this device and that is dependent upon whether you're using a double-sided board or

**Dave Jones:** you're using a multi-layer board. Now, I'm going to put this on a double-sided board and I've decided to actually completely fan out the device on the one layer and I can do this because it's only effectively two layers

**Dave Jones:** deep on the outer pads to get down to the core down here. Now, these traces that because well, FPGA when you're fanning out these sort of things, there's a whole trade-off between how many layers PCB you're going to need when you're fanning out these

**Dave Jones:** BGA type devices as opposed to a quad flat pack or something like that which has all the pins around the outside and you can just route them out really easily. But because this is a BGA device, a ball grid array, real pain in

**Dave Jones:** the ass and this is why it's a massive trade-off between your ability to route out the traces and the minimum trace width. These traces I've got here, they're only 0.1 mm or just on 4 thou width and a lot

**Dave Jones:** of PC a lot of the cheap PCB manufacturers will not be able to do 4 thou traces. If you want to go to you know, all all you'll have to pay more for that technology. So even though we've instantly

**Dave Jones:** we we're using as basically as smaller um we're using a 4 thou track and space as it's called in between here, then really we have to pay a manufacturer who's capable of manufacturing a what's called a 44 spec board, 4 thou trace, 4 thou

**Dave Jones:** clearance and that doesn't include any vias at all on this design. Now, I've got some vias up here. Now, they might look like typical vias, but take into account that my grid spacing here is .1 mm. Okay, each one of these grids and this

**Dave Jones:** via here is a whole size, a drill hole size of .1 mm. It's ridiculously small and it's got a pad diameter of .2 mm. This is really you know, that's quite leading edge stuff. You would be very hard pressed to get anyone to do

**Dave Jones:** anything under this one here, which is a .3 mm hole size or a and a .4 mm pad. Now, generally you wouldn't do that because you would want to include a bigger ratio between the via hole size and the pad

**Dave Jones:** size. So, you might want to increase that to say .5 mm like that. So, you don't get what's called via breakout. So, the drill is not always aligned perfectly and it you don't want it to break out the pad. So, you've got to

**Dave Jones:** take into account what your PCB manufacturer specifies in their tolerance there, but that's a .3 mm, which for general boards you would not want to go below .3 mm drill size. Trust me, you get you're in for a lot of expense

**Dave Jones:** and and special costing. Now, this is a .4 mm via size here, but I would typically use on a dense surface mount board. I'll typically my standard via will be .3 mm like this one. Now, if I try and drag that via under this chip

**Dave Jones:** and you can see because it's only a .4 mm pin pitch, I can't use a .3 mm via under there. It's impossible. I can't even use a .2 mm. Oh, maybe I could get away with a .2 mm via if I reduced the um solder

**Dave Jones:** mask expansion which we've got here, but we'll talk about that in a second. If I want to uh actually uh fan out this FPGA on different layers with vias, I'm going to have to use a 0.1 mm drill size. Maybe I

**Dave Jones:** can get away with .2, but it's just crazy. Now, um solder mask, as I show in my soldering tutorials, is very, very important here. Look, you can see that tiny sliver down there. The manufacturer is not going to be able to manufacture

**Dave Jones:** that, okay? There'll be no solder mask left. We've actually got a what's called a solder mask expansion here of uh 0.05 mm or 2 mil or 2 thou, okay? That is a very small uh solder mask expansion. On

**Dave Jones:** a general board, you might use, say, 4 thou, but because this is a very dense uh chip, which, by the way, this chip drives this entire design, okay? You might have through-hole parts on the rest of your board, big through-hole

**Dave Jones:** parts, massive uh pin pitches, you can use 20 thou tracks, 20 thou space, but because you've decided to use this little tiny piss ant FPGA in this pain in the ass uh 0.4 mm pin pitch BGA package, bingo, instantly, you're uh to get your

**Dave Jones:** PCB manufactured manufactured, you've got to go down to at least 4 4 thou rules, or if you wanted to route out individual vias on different layers, say this was a four-layer board and you wanted to use the uh drop through to the bottom layer

**Dave Jones:** to route out some of those pins, well, you've got to use a tiny little drill size like that. Now, I could actually um change my solder mask expansion if the manufacturer uh actually could actually do this. I could

**Dave Jones:** change it down to say 1 thou like that, and you'll see it change. And in this case, I might be able to get away with a uh 0.2 mm, maybe. But, look at the solder mask expansion there. It's bugger all. So,

**Dave Jones:** you don't want your paste uh when you solder this in your solder paste to short out to your via. And you would want what you would want what is called a tented via. So, you'd want to go in

**Dave Jones:** there and you'd want to force tenting onto those vias like that so that uh uh there is no solder mask expansion. So, uh flip to the 3D view, you'll actually uh see the difference there. So, if I drag, say, two vias in here

**Dave Jones:** like this, I've got my 0.1 mm one here, my 0.2 mm. This one has a tenting on the top of the via, top and the bottom. So, uh if we go into 3D view here, you'll see you'll notice that uh it's it's it's

**Dave Jones:** This is what uh one of the things 3D mode is really great for because it can actually show you the uh the real solder mask expansion on the board and what it's actually going to look like. In this case, it's a blue solder mask, and

**Dave Jones:** you can see the individual pads there and the solder mask expansion. Once again, remember, we've only got a very tiny, very tight tolerance 1 thou solder mask expansion on those pads. The manufacturer is going to choke when they

**Dave Jones:** hear that. They're going to charge you a crap load of money if they're actually able to do that at all. But, as you can see, this one here, this uh 0.2 mm hole here, doesn't matter if it's 0.1 or 0.2 mm what the size is,

**Dave Jones:** but because it's uh forced tenting on top of those, then um there is no chance of uh paste when you uh manufacture your board, you'll lay down some solder paste, no chance of it shorting to the via next to it. But,

**Dave Jones:** look at this one here. It's tiny, and that distance in there is only going to be less than 0.1 mm. It's tiny. So, if you accidentally get some solder bridging across there, you're in deep trouble if you've applied too much

**Dave Jones:** solder paste. So, really, when you're doing high-density BGA boards like this, make sure that you tent your vias. And you may actually have to plug them, too. You may have to get the manufacturer to what's called plug it, and they actually put a little

**Dave Jones:** resin or something in inside to plug the hole first so that the solder mask truly does cover it. But when you're talking about like a .1 mm hole like this one, which is insanely small, it's almost a micro

**Dave Jones:** via size, really. So, um uh generally, if we go back in, I've just start tented that one. There you go. It's It's tented. Just make sure you tent or plug them. Otherwise, you could end up with massive shorts under there,

**Dave Jones:** and you won't be able to inspect it, of course, and you won't know till you until you go and actually power up your prototype, and it could actually even go bang. If you accidentally short out ground and power,

**Dave Jones:** poof. Release the magic smoke. Oops. Now, I got a little bit sidetracked there talking about all that sort of stuff, but we're talking about fanning out this FPGA either using vias or traces. Now, because this is only two

**Dave Jones:** layers two pin layers deep, I'm actually able to get one trace out there. I can't get two, really, cuz we're already down to 4 thou or .1 mm track width. But sometimes in some FPGAs, especially on the larger pin pitch ones, you can

**Dave Jones:** actually get two tracks out between one individual pin. Now, if this FPGA was any bigger, we would not be able to route out the extra tracks here. We'd be forced to use some vias here to drop through to

**Dave Jones:** our other layers. Bingo, we've instantly meant that we have to get .1 or .2 mm drill hole boards, much more expensive, pain in the ass. But anyway, um I figured out a way to uh route or fan out

**Dave Jones:** this device um uh based on and uh just based on a single layer here. So, uh if you'll notice each quadrant of the FPGA like this is basically a rotational mirror image of the one up here. Well, it's not quite, but it's uh close. Sort

**Dave Jones:** of this one matches that this quadrant matches the diagonal quadrant over there and uh so on and uh and really it it is quite a nice symmetrical rotational design. I like it. Brings a bit of a tear to the eye, really. Um so, we've

**Dave Jones:** routed out uh these using 4 thou traces. Okay, let's switch to Imperial mode cuz I like to use Imperial not metric mode for my uh traces, but for hole sizes and board sizes and things like that, I use

**Dave Jones:** metric. Go figure. Um but uh yeah, that's just the way the a lot of the industry works, the PCB industry. They does mix up their uh their uh millimeters and their thou's quite a lot. Um but you have to generally juggle

**Dave Jones:** both when you're doing a PCB design like this. Anyway, um this means that we can um sort of start fanning out um these using larger traces. We might uh say go to a 6 thou trace or something like that

**Dave Jones:** when we um take that because you don't want to use a 4 thou trace all over your board. So, you might just fan it out with those small uh 4 thou traces or you can even uh say fan it out with say an 8

**Dave Jones:** thou trace perhaps. You might be able to get away with that, but just watch your clearances in there. Um if you don't have enough space, there we go. We might Yeah, that's probably going to be enough space in there. So,

**Dave Jones:** we could fan this out with an 8 with 8 mm traces. No problems at all. So, there you go. That is um basically um laying out a or fanning out a a FPGA a 0.4 mm pitch BGA device. Really, if you

**Dave Jones:** can avoid it using these type of packages and these devices, do it cuz it can be really expensive and a real pain in the butt. And likewise, we're trying to get our bypass caps here close to our close

**Dave Jones:** to our power pins in here. So, you drag it all the way over here and then you might have say a a via in here like this, okay? Dropping it down to a dropping it down to, you know, a power

**Dave Jones:** tracer on on a different layer. But look, this is a 0.3 mm via, which is the which is the minimum size I would be comfortable with on on a basic board like this without paying a lot more. Some people would even say 0.4 mm is too

**Dave Jones:** small. Okay, but once I get in there, you can see that routing out these becomes a bit of a pain and then I've got to move my cap in here and just it gets really quite ugly really quickly, especially if you've got a lot

**Dave Jones:** of bypass caps on a design like this. Now, a lot of FPGA designs, especially some more advanced ones, will actually the bypass caps will be directly under the chip on the bottom layer the bottom side of the board on what's called a

**Dave Jones:** what's called a two-sided load components on both sides of the board. So, you can get a very low inductance path between your pad. Like if your via is here like this, okay? I might swap my um I might swap my component down to the

**Dave Jones:** bottom layer down there, okay? It's now flipped over to the bottom and I might sit that on the bottom like that, okay? So, I can actually get if this was a huge device like a massive big, you know, 4 500 or a pin BGA device, I'd put

**Dave Jones:** that bypass cap on the bottom there and bingo, it's disappeared. You'll find that it's actually vanished onto the bottom side of the board right next to the via that allows me to get a low inductance path through to that bottom

**Dave Jones:** layer, but there you go. There's FPGAs for you. I hope you found that interesting. Really, this was a very basic implementation, a very like the lowest-end FPGA you can get and there's actually a lot of factors I didn't

**Dave Jones:** cover. So, please don't leave comments saying I left out this, I left out that. It's designed to be food for thought thought and hopefully you learn something. But, go check the data sheets. Don't be scared of these sorts

**Dave Jones:** of devices. Just be aware that there's lots of traps for young players, a lot of things which drive your design decisions for FPGA not only on the schematic and the component level, but on the PCB level as well. Hope you liked

**Dave Jones:** it. I'll see you next time and don't forget to sub- scribe and uh rate and uh do all and comment and all that sort of stuff. Even if it's a flame comment, I don't mind, really. See you.
