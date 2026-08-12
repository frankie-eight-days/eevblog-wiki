---
video_id: dm-yZ1N3xmc
title: EEVblog #409 - EDMI - Smart Meter Teardown
url: https://www.youtube.com/watch?v=dm-yZ1N3xmc
source: youtube-asr
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. Today's item is actually viewer submitted. It comes from Lewis Able from Abletronics in the UK. Thank you very much, Lewis. He sent me this little puppy. It's an EDMI Atlas Mark 10A three phase

**Dave Jones:** power meter. You know, one of these smart meters that they put on your house these days and it's got GPRS in it, you know, 3G thing. It comes with a SIM card, talks back to base, it monitors all your power consumption and

**Dave Jones:** you know, they don't have to send somebody around to read your meter anymore. They can do it all with one of these smart meters. Now, EDMI are actually an Australian company, they started out being an Australian company. It's manufactured in Singapore,

**Dave Jones:** so I'm not sure what the deal is if they're fully Australian anymore, but anyway, I'll claim it. So, this is an Australian-made smart meter. It's a 240 V one. It's brand spanking new, still has the unused SIM card in the packet,

**Dave Jones:** so pretty advanced functionality in this puppy. Now, this one's actually a 240 V model designed for the Australian or UK market. It's three phase as I said, not just single phase and it's got a whole bunch of features and I'll link in the

**Dave Jones:** data sheet down below and you can see what advanced capability this does. It does THD and all sorts of weird and wonderful power measurements. Fantastic. So, thought it'd be interesting to crack it open, take a look inside. So, you

**Dave Jones:** know, as I say here on the EEVblog, don't turn it on, take it apart. And I will start out by taking a look just at the spec sheet here, see what we've got. I don't know, it's all sorts

**Dave Jones:** of compliance standards. If you're into that sort of thing, check those out. But, it's 220 to 240 V input, although it does operate from 180 to 290 V input. Burden voltage less than 10 W per phase. Frequency range it operates from 45

**Dave Jones:** hertz to 60 hertz and then the current range is got looks like one channel is that one channel 6 amps 5 channels 20 amps I don't know current limit is 20 times the maximum current range for 0.5 seconds for those

**Dave Jones:** surges then our burden power in this case less than 0.5 VA or 0.5 watts per phase and it does four quadrant energy measurement imports and exports uh real and reactive power it does absolute and three phase and per quadrant and all

**Dave Jones:** that sort of jazz and it does frequency phase angle power factor total harmonic distortion unbalanced stuff and you can do waveform downloads it's got five cycle resolution on sagging and stuff like that so it can record that time date and phase

**Dave Jones:** worst case excursions programmable trigger levels man it's got everything it's got IO as well it's got a various relay drive outputs and stuff like that really quite neat designed to operate over minus 25 to plus 60 degrees range it's 2.1 meg of

**Dave Jones:** non-volatile memory so it can record for 3600 days 10 years with 30 minute intervals across two channels it can do up to 32 channels interval programmable two independent surveys whatever they are instantaneous readings policy inputs ability to store all of that sort of

**Dave Jones:** stuff and it really is a very powerful little beast of course it's got a built-in real time clock as well it's got you know the rate adjustable rate output and stuff like that it's got a big LCD on it we might power it up after

**Dave Jones:** we do the tear down to see how it actually operates and it's going to have security as well because these are security and tamper detection and allowance because these things are smart meters, right? They don't want um the consumer

**Dave Jones:** to be hacking into these things and uh and doing that sort of thing, you know, and uh getting cheaper power bills or no power bills. So, it apparently has detection for bypassing current and reverse uh current provision for sealing

**Dave Jones:** with conventional wire or plastic uh seals and uh advanced tamper detection and login. Well, not quite sure what that is whether or not, you know, you uh can hack the components inside. I don't know. Maybe we'll find out. And then

**Dave Jones:** it's got various communication options. Uh it's got uh RS-232, RS-485 multi-drop, and it's got GPRS compatible, and compatible with ZigBee and MV90, whatever. Don't know what MV90 is. And it's got some software available for the PC which allows you to um set

**Dave Jones:** all this stuff up. And I'd be very surprised if you couldn't uh remotely program this thing as well and uh change all its loads and uh extract the data and run tests and things like that over the um

**Dave Jones:** GSM connection as well. And it actually came with the uh GSM card as well, the SIM card to put in it. So, wooh, it's got a lot of stuff. All right, let's take a look at it. It's quite a big unit here

**Dave Jones:** and unfortunately Lewis has uh had a peek inside. I don't blame him. He couldn't resist. So, the uh calibration um uh not the, you know, the uh warranty void and all that sort of stuff sticker has been busted. So, it's uh one big unit as

**Dave Jones:** well. All the interconnects are on the bottom here, which we'll take a look at. But apart from that, it's just designed for mounting in a box there. And uh the user interface, main LCD here, a couple of LEDs which uh pulses. It uh says that

**Dave Jones:** it does um 10 pulses per kilowatt hour there. So, you'd get 10 pulses on that for every kilowatt hour of power consumption. I'm assuming and that's probably programmable as well. Then we've got a couple of LEDs here and

**Dave Jones:** we've got a couple of push buttons, connect and select, and that's all there is to it. And if we take this bottom off here, we just unscrew this and whoop. There we go. And there's a couple of terminal blocks in

**Dave Jones:** there. They're they're not the mains power input. We'll take a look at those in a second, but um we've got a separate modem down in here. So, it's not actually built in. We'll have to do a separate tear down of that, but that is a

**Dave Jones:** it is a GSM modem, Intelsat Sam, Intelsat Proprietary Limited. It's Australian as well. Beauty, I like it and and there's where you whack your SIM card down in there and it comes with an antenna as well. There we go, just an

**Dave Jones:** external antenna so you can put that away from the box inside your distribution cabinet or something like that. Just a RJ45 on there, connecting it and there's our antenna output. And that is a separate item. That's kind of makes

**Dave Jones:** sense. They can change that for different countries and things like that so they can sell the main unit anywhere in the world and then have different standards for GSM and phone interconnection depending on where you are. And inside the case

**Dave Jones:** they've thoughtfully provided a little pinout here for the interconnects and there's a looks like there's a relay output there, some uh uh probably optocoupled um outputs there. There's our RJ45 and then we've got our mains input down here. And

**Dave Jones:** as I said, this is a three-phase model so they've called the phases A, B, and C. So, we've got phase 1A here going in there and coming out. So, it measures the current on that phase, and of course

**Dave Jones:** it can measure the voltage relative to the neutral over here as well. So, second phase B and third phase C in and out. And check out the size of these big beefy mains input terminals here, absolutely massive. And I'm not sure where you

**Dave Jones:** screw those in. I think you've got to take the uh this whole cover off to actually get in there. And there we go, that cover just pops off there, and there's your huge big screw terminals down in there. Woah,

**Dave Jones:** monsters. And we've got a little jumper here which selects between the internal battery which is currently connected and an external battery pack as well. So, you just move the jumper across there. I'm not sure why you would want a uh

**Dave Jones:** external battery pack. Now, this cover should just pop straight off here because the tamper seal is on the side here. It should just pop off. Now, under here I'd expect a because it it is sealed on the side

**Dave Jones:** there with that thing, I'd expect there to be a a tamper switch under this thing to sense that the cover's removed at a minimum. Woah. And pop. Pop goes the weasel. And there we go. Ta-da! There's inside the unit. I love how it's just bare. I

**Dave Jones:** mean, this is a a transparent case anyway. You can sort of translucent case. You can sort of see through. Aha! There's our micro switch. Ta-da! Love it. So, that's our tamper micro switch. So, it already knows there's our internal battery. So, it

**Dave Jones:** already knows that we've uh presumably if it's actually monitoring, I don't know. You might have to sort of, you know, set it up first and then it's all ready to go. So, this is a factory one, hasn't been used apparently

**Dave Jones:** straight out of the box. So, not sure if it's configured yet, but there's your micro switch which disables when you take that front cover off. Couple of mobs down here by the looks of it. We'll have a look at the board in more detail

**Dave Jones:** and the LCD there. There's our main processor under there and the LCD is just standing off the board like that. You don't see that too often. That's rather quite neat and of course there's a second boards underneath cuz there's

**Dave Jones:** no big power stuff on this top board here. This is just the data logging and processing board, I'm assuming. We've got some light pipes there. There's our two little light pipes going up from the LED down on the bottom there

**Dave Jones:** and they just go up through the front panel there. There you go. And there's two other LEDs down here that they went through the big clear window on the bottom there. So, um those things don't need a light pipe and

**Dave Jones:** got our two contact switches over here. Looks like they're just a Yeah, they're just a Oh, there we go. They actually fell out. There's the little rubber I rather like that. Check it out. They've got that sitting in there like

**Dave Jones:** that and when you push it, oh, that's a that's a really nice switch. Look at that. That's beautiful. I like And down near our outputs down here, you can see that we've got four outputs, four moves. Those moves are obviously protecting the

**Dave Jones:** outputs there and there's our relay which went to that one, I believe it was. So, one of those relay contacts there would go to there and there's our optocouplers there. Those three optocouplers would be controlling these three channels here. We've got more

**Dave Jones:** optocouplers over here. So, all of this circuitry around in here is We've got four optocouplers there coupling that over from the digital section, the control section all up the top here down into this output which drives the RJ45 which goes

**Dave Jones:** to the G GSM module down there. So, that's all optocoupled isolated, as you'd expect. Safety first on this sort of stuff. Another optocoupler in there, and uh that's it. Bob's your uncle. The main processor, there'll be a a flash memory device

**Dave Jones:** under there as well. Maybe that one down there. It's looking a bit suspicious. So, that'll be our 2 mega flash memory, perhaps. Um and we can't get that LCD out cuz that's actually soldered directly into the board. You may not be able to see that, but I

**Dave Jones:** can see it, and that is a TI MSP430 processor down in there. There's a 32 kHz crystal down there. There's probably another crystal somewhere else as well, or that could be the main one. Plus, there's got to be another real-time clock crystal

**Dave Jones:** somewhere as well. So, yeah. Um I don't know. That's probably it for the main processor board. I mean, it's not, you know, there's not a huge amount doing there. We've got our uh cables connecting down to our main power board

**Dave Jones:** down here. That's where a lot of the interesting stuff is going to be. And of course, we have the classic LM324. It's actually an LMV uh 324. Whole bunch of uh passives around that. It's probably just doing some uh buffering and things

**Dave Jones:** like that. Now, our battery's a Varta uh CA um half double A size, made in Germany. Aha, brilliant. Now, on the uh power board, well, there's probably three boards down there. There's probably a big power one down there.

**Dave Jones:** It's probably in that uh second one down in there. Oh, no. That could be an upside down. I see some uh through-hole components on there. So, maybe there is just one big power board under there, but I wouldn't rule out a uh third board

**Dave Jones:** underneath there as well. And um on that power board, of course, we're going to see a uh big uh beefy current shunt for each um a very precise current shunt for each of the um three uh phases. We're going to see

**Dave Jones:** you know some pretty high spec ADC type stuff. You know, like I don't expect this thing to be terribly accurate down at the watt or sub watt range. Of course, it's designed to measure you know the main current of

**Dave Jones:** your house and monitor the main current. So, if this thing is 2400 watts your standard mains outlet, but it can actually go much higher than that. Well, you know, if you want to say point one watt resolution, that's 24,000.

**Dave Jones:** You know, if one bit is 124,000, you know, you're going to need at least a 15 say you know round it up to you know a 16 bit converter there for each channel. If you wanted you know in the order of sub

**Dave Jones:** one watt resolution on this thing. May not have that. May just you know may just be happy with a 12 bit converter or something like that. But this would be a pretty you know high spec device. They've spared no expense. I'm sure

**Dave Jones:** these things are probably quite expensive. So, let's see if we can Oh, there we go. Hey, look at that. Look at that. The board just pulls back. It's hinged under here like it's hinged at the back here with the connectors and

**Dave Jones:** it's just held in place so it doesn't move with that that plastic retaining clip there. So, you slide it back and ta-da lift it up, forward and out. Oh, no, that's something's Oh, there we go. Got to take this.

**Dave Jones:** I'm not sure what that cable's doing there. I might find out. There we go. Ta-da. Aw, we've been mooned. Look at that. Now, on this main board of course, you can see the classic isolated grounds. This is the

**Dave Jones:** optocouplers would be bridging these two grounds. Here's our output ground here based on our output connectors down here. And then this is all our logic ground up the top. And then they would have the of course, have the optocouplers

**Dave Jones:** separating those two grounds. Classic, and yeah, they've got a lot of margin on there, that's for sure. Now, it looks like this board is directly connected by these screw terminals down into there. Now, you note that this extra terminals here, which they

**Dave Jones:** said do not connect, they do actually looks like they go through there, and then they do connect down into here. So, are they like a earth connection or something, but it definitely said, if you have a look down in here, uh

**Dave Jones:** do not connect. No connections to terminals 2, 5, 9, and 13. 2, 5, 9, and 13. So, do not connect them, but they are actually connected to something down on the board. So, yeah, we're going to have to uh screw

**Dave Jones:** this thing. We've got direct connection Yeah, direct connection down onto the board, which is what you want, of course. You want big beefy connections down into there. And uh surprise only had one screw, actually. I would have thought maybe they'd have a

**Dave Jones:** have a couple in there, perhaps. So, interesting to see what form the current shunts take, um because I don't think they're mounted on the I'm not sure if they're mounted on the board. They could be like just free

**Dave Jones:** standing underneath, or or like actually, you know, lumped right at the back of these connectors, and then they just and then these are just like the wiring coming up from them or something, the sense lines, perhaps. Um I'm not

**Dave Jones:** entirely sure. We'll find out. This is terribly exciting stuff watching me unscrew. Somebody in the recently commented, "Oh, why don't I use an electric screwdriver?" Ah, come on. That's uh that's cheating. I only use an electric screwdriver for

**Dave Jones:** you know, one of those RF die cast cans or something that have 50 screws on the things. Otherwise, you're cheating. And you can't get me to just banter on about random crap, either. So, there we go. Um that looks like

**Dave Jones:** it is going to leave her out of the Okay. No, okay. They're they're stuck under there like that. So, it looks like you've got to fold probably fold these up. Hmm, this could be tricky. Let me work on it, folks.

**Dave Jones:** Well, that's pretty obvious. You have to unscrew these in here, and they just pop out like so. So, now we should be able to pop this board out. And pop out, presumably. I mean, there was nothing nothing on the bottom

**Dave Jones:** of the case at all. So, um yeah, I think it just needs some delicate persuasion. Aha! This whole terminal block section pulls out, by the looks of it. There we go. Up. There we go.

**Dave Jones:** That all pulls out. The board pops out. It's all rather It's all rather complicated. Not that trivial. Oh, there Oh, look at that. Oh, look at that. Beautiful. Aha! Oh, that's pornographic. Look at that. And isn't this beautiful? We have three

**Dave Jones:** current transformers. There's no traditional current shunt resistor as such. They're using these current transformers. And after a tiny little bit of investigation and thought, it's obvious why. And here's the reason. And the thing that's driving this is the IEC standard

**Dave Jones:** 62053-21 and various other dash standards. They basically say that these current meters, these smart meters, power meters on your house can't take any more than 2 W per phase. And you know, yeah, you've got you know, a million

**Dave Jones:** houses hooked up. I guess all that sort of stuff adds up. So, they're determining that maximum power value that these energy meters can consume per phase, a measly 2 W. So, let's look what happens if you've got one of these We're only going to look at

**Dave Jones:** one phase here, okay? So, let's have a look if you've got a traditional current shunt resistor. What does that mean? Okay, our current shunt resistor RS, we're going to have a current flowing through it. And this particular model

**Dave Jones:** has a 100 amp capability. So, let's take 100 amps. And as you know, um P equals I squared R. So, you rearrange that. Our resistance there, so we're calculating Sorry, that's RS. And we've got RS here is going to be equal to

**Dave Jones:** the power, our maximum power in this case, 2 W, divided by IS squared. So, that's 100 amps maximum capability. Or if you design this meter to be 50 amps, you can redo the calculation. But let's use 100, okay?

**Dave Jones:** It's going to be in the order. So, 2 W on 100 amps squared is going to give us a value of that resistor of 200 microohms. Absolutely tiny. So, you know, what does that mean? Well, at the not only is that an incredibly

**Dave Jones:** low value of resistance, okay? It's going to be, you know, very difficult to implement that. Not impossible, but you can certainly implement that. But what it means is that it then at low values of current, instead of say 100 amps, if your house

**Dave Jones:** is only drawing say 1 amp on that phase, what does that mean? What's the voltage drop across that shunt resistor? Well, 1 amp, do the math. It's going to be 200 microvolts, basically. And we're talking very small voltages there at very small

**Dave Jones:** currents. And that becomes a pain in the ass to measure. So, you know, let alone get me out trying to measure, you know, 100 milliamps or 50 milliamps or something like that. So, what they've done is they've used these

**Dave Jones:** current transformers instead of your traditional current shunt resistor. I like it. And they've got three big beefy ones here per phase. The output of these current transformers, they're going to convert those into voltage, and they can measure the current as well based on a

**Dave Jones:** burden resistor down in there. And also, if you use traditional current shunt resistors, well, you're going to be dissipating, you know, up to a couple of watts inside this thing. And yeah, it's going to heat up, and that can cause

**Dave Jones:** potential issues as well. So, just something to consider. And the reason that they've gone for these funky current transformers here because, as you can see, you know, there's practically no power dissipation at all in this, um, you know, basically, it's only drawing

**Dave Jones:** the current it needs to drive the circuitry and all the measurement stuff, which isn't going to be much compared to a traditional current shunt resistor. So, look at these big bus bar, um, huge big links down in here. They're

**Dave Jones:** absolutely massive. So, these are the three phases here, and we've got our neutral. But of course, having no other connections on there doesn't make sense. So, figured it out. What it is is you remember these little links that we took

**Dave Jones:** off uh before in here. These are little voltage tap links and they actually um short out. If you have a look down in here, they actually short out the uh one of the phases here down to this terminal. So, you're not supposed

**Dave Jones:** to connect this terminal because these links are connected internally. Got these internal links which then connect it through to this trace which then goes off down in here. So, they're your voltage taps going down to all your uh circuitry over here. And plus,

**Dave Jones:** there's also another tap which come comes off the same pin over to a 3.3 meg resistor on each channel down in there. There's one on each channel. So, that looks like that's the other one looks like uh the all that stuff up there, it

**Dave Jones:** looks like a a protection um tap. That's just a you know, uh getting the protection devices off. This is probably uh powering the rest of the circuit as well. But, the actual measurement voltage measurement on each uh phase seems to be going through this

**Dave Jones:** 3.3 meg resistor into this little uh SOT-23 package there and off to um well, uh I guess the um um ADC uh stuff has to be on the main processor board because I don't see anything on this board down here that uh

**Dave Jones:** looks like it's an ADC. So, it's obviously tapped off. We've got a whole bunch of uh unpopulated circuitry around here. I'm not sure what that was supposed to do. And this link here which we uh saw before and we had to disconnect, which

**Dave Jones:** goes up to this main board here, it's obviously an isolated uh voltage tap. There's a little power supply there and that's going off to power this part of the isolated circuitry down in here on the RJ45 output. So, the rest of the

**Dave Jones:** circuitry around here, which uh taps off the three phases here, any one of the three phases by the looks of it, it is just a mains switch mode DC power supply. There's a switching transformer. There's There's the controller. It's a

**Dave Jones:** uh Power Integrations TNY268GN. So, that's a really efficient switch mode controller, like less than 50 mW no load consumption. So, you know, really one of those eco green ones. So, they really do want to get the power dissipation down on these things, of

**Dave Jones:** course, to meet those various standards that require these things to have low power. So, that powers the rest of the circuitry. It wouldn't need much at all. I mean, they've got big 400-V caps down in here, you know. It seems a

**Dave Jones:** little bit overkill, actually. We've got a got a common mode choke here. So, we've got some filtering over on this side, but it does seem um you know, a little bit overkill for the amount of power that I suspect this

**Dave Jones:** thing requires, but anyway, I'm sure it needs it for a reason. Once again, they've got lots of protection in here, lots of MOVs all over the place. Looks very well designed. I think they've spared no expense there. The The switching

**Dave Jones:** transformer there is really looks first class. So, I really quite like that. And of course, there's that separate winding coming off there I told you about before, which uh powers the output circuitry. That's isolated from this one here, which powers the main circuitry

**Dave Jones:** over there. Now, if you look at each channel here, there's a four components. There's a Zener diode. There it's marked ZD10, but it doesn't look like a uh Zener diode package. Anyway, I'm I'm presume it is, and um they've just got

**Dave Jones:** some There's a filter cap there, and they've got a shunt resistor there, a burden shunt resistor on the output of the current transformer. And there's not much else to it. There's So, you're going to have a bunch of the

**Dave Jones:** four of those per channel. There they are, duplicated. And then there's some extra circuitry in here tapped off this one here. So, I'm not sure what that one's doing, but it's going through an optocoupler there. And as I said, I

**Dave Jones:** don't know what that unpopulated stuff is. There's a whole row of resistors in there populated, but all that sort of stuff is unpopulated. So, there's this board basically is just the power supply and the um uh current to voltage conversion. Uh

**Dave Jones:** that's pretty much it. So, the ADC must be up under there somewhere, and I suspect it's Well, it's either going to be the internal to the Texas Instruments 430 processor, or it's probably one of those puppies under there, cuz

**Dave Jones:** that's that LM 324 we saw previously. So, let's have a look at that one. And no, that's just another LMV324. Bummer. And the other 14-pin SO package over there is also an LMV324. So, they must be using the ADC in the

**Dave Jones:** MSP430 processor. And that's an MSP430FG4618. And that's actually a mixed signal one with the higher resolution, 12-bit ADC in it. So, that's what they're using. Just a microcontroller that's got the internal reference. I don't really see an external reference anywhere under

**Dave Jones:** there. They might Yeah, I don't think there is. They're probably using the internal reference there, but as I said, you know, these things don't have to be um you know, hugely accurate right down at the uh low end. So, you know, the

**Dave Jones:** internal reference in the 12-bit uh ADCs there, good enough. And let's take a look at the uh current transformer we got in here. It's a Vac brand, and they make current transformers specifically for electronic watt-hour meters. There it is down there, for electronic

**Dave Jones:** watt-hour meters. Brilliant. I like it. we've got here is the E4626X501. That's a 100 amps uh primary uh current capability. They're all at a current ratio of uh 2,500. So, it's um uh you divide the 100 amps there by

**Dave Jones:** 2,500. We're going to get 40 milliamps uh maximum on the output. And they have pretty much essentially a fixed uh phase error due to It tells you down here, due to the excellent soft magnetic properties of the Vac core. Um these are

**Dave Jones:** DC-tolerant uh current transformers, and they need to They lead to a negligibly small amplitude error, as well as to an extremely low and linear temperature dependence as well. And they've got all the curves in here for all the

**Dave Jones:** temperature dependence and stuff like that. And due to the low permeability of the core material, the phase error is typically 4 to 5°. And there it is, 4.73 they specify precisely. And of course, that you can calibrate that out. They're

**Dave Jones:** saying uh either do it in the software or uh do it in the uh LC RC uh low-pass filter. My guess is they're probably doing it in the software, cuz that's the easiest way to do it. Once this thing is

**Dave Jones:** already uh installed and assembled, they would uh individually calibrate um each one of them to uh uh to basically remove uh that error. And here's those uh components I showed you earlier on the um output there. There's the primary

**Dave Jones:** side. It's just a current transformer. We've got a burden resistor there, which gives us a voltage uh drop across here, and there's our low-pass filter, and off it goes to your ADC. And here's the uh characteristic uh curve graph, and it

**Dave Jones:** shows uh various things versus uh current here. We've got uh basically uh the graphs extend from, you know, a couple of hundred uh milliamps down there all the way up to a couple of hundred amps. So, this one's only rated

**Dave Jones:** to uh 100 amps, but it can obviously go a bit beyond that. And you can see that we have the amplitude uh error here, tiny little amplitude error in percentage down in there. And you can see that basically uh does not change

**Dave Jones:** with that temperature at all. But you can see the uh phase angle does obviously uh change with temperature here. So, that would be uh calibrated Well, they try and calibrate it out at a nominal temperature there, but you can

**Dave Jones:** see it's pretty good over the entire current range. I really like it. And of course, these things accurately measure the uh phase angle as well. So, they may even be taking uh the temperature into account. There might be a temperature

**Dave Jones:** sensor on the board, and uh they're, you know, they could they could compensate for this because, you know, it it you know, it's fairly linear with temperature there. I mean, you know, over an operational range look of, you

**Dave Jones:** know, 55 down to sort of, you know, minus 10 over that sort of 50° range, it's going to change by roughly uh the order of half a degree error there. So, you know, that that could be significant. I don't know. You'd have to

**Dave Jones:** go through the math and figure it out. Um do some ballpark calculations. But if it is, you could compensate for that in the firmware. No problems at all. Just by measuring the ambient temperature. Now, here's an interesting uh

**Dave Jones:** performance graph. It shows the um uh the basically the behavior of uh different types of VAC core materials compared to regular 80% nickel iron uh cores. So, they've got, you know, they're Vitroperm and Vitrovac. Um you know, these are probably, you know,

**Dave Jones:** trademark terms for their own uh core material that they actually use. And they've got an amplitude error here. And you can see theirs is basically flat over the full current range there compared to a typical 80% nickel iron

**Dave Jones:** core like that. So, much more linear using their Vitrovac. And the same thing on the phase error as well, of course. Look at that. It's pretty much almost ruler flat pretty much for the um phase angle there compared to the typical 80%

**Dave Jones:** nickel iron stuff. So, really, you know, they've got some wizbang core technology that makes these um pretty linear current transformers. I like them. And they've gone to town here. They've even got typical characteristics of the amplitude error versus the primary

**Dave Jones:** current over the full current range from 1 milliamp all the way up to past 100 amps there. And you'll, you know, you'll note that it's only um you know, barely even uh plus minus .25% amplitude error. Well, as for the

**Dave Jones:** supposed wizbang uh tamper protection and all that, yeah, they've got the micro switch down here. But uh apart from that, you know, I don't know if they're um you know, got uh firmware and uh maybe even circuitry to try try and uh detect uh whether or

**Dave Jones:** not uh you know, somebody's Well, they've got to um try and detect the how somebody's bypassing the current. So, maybe they're able to do that in firmware somehow. But um yeah, I you know, I'm not sure um you know, you

**Dave Jones:** could probably get in there. And if you're really uh knowledgeable about these things, you could get in there and hack the uh uh shunt values in there or something like that. And I'm not sure if the firmware would be able to um know

**Dave Jones:** that sort of thing. But of course, um once you of course to get into it, you physically got to bypass the yard micro switch and then well, it alerts the the utility that you know, somebody's you know, broken into this thing and

**Dave Jones:** yeah, they'll probably wave the finger at you. So, you know, I I don't think they have to do too much in in part in you know, in regards to the tamper protection and stuff like that. It's built in. It'll be interesting to know

**Dave Jones:** how they actually buy you know, actually detect bypass current like in the main box itself rather than going through here. I'm not actually sure how they would do that. So, there you go. That's a look at the main guts

**Dave Jones:** of this thing and you know, there it's very well engineered and looks like they spared no expense for this thing as you'd as you'd probably expect. It really is quite nice and I've run out of time to power this thing up and have a play with

**Dave Jones:** it. And I kind of wanted to do that, but I might even leave that for another video if there's enough interest in that powering up and playing around with it, but I'm not sure if I could use it for

**Dave Jones:** anything useful really cuz you know, I'm not into doing the high current stuff and things like that, but it might come in handy for something, but I might try and power it up and see if I can have a fiddle around with it

**Dave Jones:** later. So, I hope you liked that little tear down. If anyone has a schematic or service manual of this thing, that would be great cuz that would reveal a bit more I'm sure of what they're doing here. So,

**Dave Jones:** if you have it, please let us know in the comments. And of course, we can't leave it without taking a look inside the GSM adapter here. So, there's our SIM card module. There's nothing terribly exciting in here at all. Let's uh

**Dave Jones:** flip it over and there's our wireless uh wireless CPU model Q24 plus. Woohoo! Whoop-dee-doo! And there we have a Sipex SP3238. Nothing terribly exciting there. It's just an RS232 transceiver. But all of the magic is done in that Wavecom

**Dave Jones:** wireless CPU module. So, I'm not going to take that out. That requires to unsolder the tabs on the whole thing and get it out and rip it apart and ah couldn't be bothered. So, there you have it. There's a teardown of the EDMI

**Dave Jones:** Australian supposedly Atlas Mark 10A three-phase energy meter. Hope you enjoyed it. And if you've got any further info and you want to discuss it, jump on over to the EEVblog forum. The link is below as well as to

**Dave Jones:** various data sheets in this teardown as well. And don't forget, if you haven't already done so, please subscribe to my YouTube channel. Catch you next time.
