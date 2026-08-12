---
video_id: Pr-C7jGczlE
title: EEVblog 1691 - Uni-T UDP6731 360W Bench PSU REVIEW
url: https://www.youtube.com/watch?v=Pr-C7jGczlE
source: youtube-asr
---

**Dave Jones:** Hi, it's power supply review time. Today we've got the Uni-T UDP 6700 series, in particular the UDP 6731, which is top of the range. They've got four different models. I'll put up an overlay graphic here. The 6720 is the

**Dave Jones:** lowest model. That's a 100 watt 60 volt jobbie all the way up to the 6731, which we've got here, which is a 360 and this is an 80 volt jobbie. So So none of that 30 volt rubbish. These are higher

**Dave Jones:** voltage power supplies, which can be useful for, you know, whole bunch of applications. You know, you might need 50 volts if you're doing like power over Ethernet or something like that. So a 60 volt or an 80 volt power supply, very

**Dave Jones:** useful. And they're in this vertical form factor, which I like. These are, you know, getting fairly popular these days. The good thing is is that you can just stack them side by side. Yes, it's only a single output power supply. On

**Dave Jones:** the back we've got an IEC mains input. We've got the AC voltage selected 220 or 110 for you Yanks. And it's got output voltage sensing as well. So yeah, four terminals. It's not on the front, but it is on the rear. And also you can get the

**Dave Jones:** it looks like you can get the voltage out the back as well. Useful if you've got it like maybe in a rack or something like that or you you know, permanently powering gear. You don't want it coming off the front panel. You want it coming

**Dave Jones:** off the rear. And RS232 as well. It's got some software. We'll try that out. And an earth grounding terminal and a fan. Huh. One of the problems with this form factor though is that you're very tempted to stack these up like side by

**Dave Jones:** side next to each other. Unfortunately, yeah, these are the ventilation holes here and here. So if you've got them stacked right up against each other, that's going to be problematic. So kind of defeats the purpose of having that. So yeah, we're going to have to

**Dave Jones:** take a look at the internals. Speaking of which, you know what we say here on the EE blog, don't turn it on, take it apart. And street prices in Yankee bucks range from uh $209 up to $415 for the model we're talking about here,

**Dave Jones:** but prices do vary. Like if you buy it directly on AliExpress, for example, you can get uh specials and things like that. I've seen it as low as like 150 bucks or something uh like that for the lowest model. But this higher end model,

**Dave Jones:** yeah, you're paying for the extra power. A 360 W power supply Whoa, pretty beefy. So these vent holes here, these are actually uh inlets on either side and cuz the fan actually uh blows out the back. So it's sucking air in and if you

**Dave Jones:** got it right up next to the other power supply, it's sucking hot air in from the power supply next to it. Um and unfortunately, like I've shorted this thing out. I haven't actually used it and uh the fan um barely turns on at

**Dave Jones:** all, but uh haven't fully stress tested it yet, so we'll have a go. All right, it's got a lot of screws on it, but uh just on the sides and whoa, pulls off. Ooh, that looks neat and tidy, doesn't it? Whoa,

**Dave Jones:** I'm kind of uh impressed by that right off the bat. And of course, when you got a 360 W power supply, this is a switching jobby. Uh yeah, none of that linear rubbish. Um anyway, um yeah, that looks really neat and tidy. We've got a

**Dave Jones:** giant main board in the back and if we swing that around, yeah, there you go, double-sided load. That looks really nice, doesn't it? I'm quite happy with that. I'll take some high-res photos. I'll put them on the EE blog website.

**Dave Jones:** Yeah, looks like we got the current shunt resistors over here. Anyway, uh we can go through that later. And anyway, all the wiring's neat and tidy. It's all cable tied here. Uh this wire is just soldered on there. I'm

**Dave Jones:** not sure what's going on there. Anyway, look, they do have a giant choke. They've got a giant a That's solid core wire. They've got a giant Why have they used a solid core wire for the earth terminal here? But, that's

**Dave Jones:** got through going going through a giant choke. They've They've really done well with heat shrinking that, and it's going up to uh the uh screw which goes directly into there, and that's got a nice um uh crimp terminal uh crimp lug on it.

**Dave Jones:** So, yeah, no worries whatsoever. We've got our uh Y class uh caps there going down to uh mains earth. So, no problems there, but I'm just like why have they used a solid core wire for that earth? I don't know.

**Dave Jones:** I'm Got any clue? Leave it in the comments. Anyway, let's follow the money. We've got our mains input here. Um they're sleeved, no problems whatsoever. Goes down to Yes, our big clunking mains power switch down there on its own

**Dave Jones:** dedicated board. That's really nice. Um they didn't have to implement it like that, but I'm I'm actually quite impressed. And they've put an insulating sheet under that, too. Nice attention to detail. I'm liking it. So, all of our

**Dave Jones:** switching elements are obviously uh on this heat sink under here. And here's our output caps here. Look at this giant output choke here. This is absolutely enormous. Um and Oh, yeah, there's a couple more caps down there. So, there's

**Dave Jones:** four um So, they're the output uh switching caps there by the looks of it. We've got four extra caps under there, but uh whoop Oh, wow, hello. No, we've got an extra extra bonus extra bonus output cap there on the front panel. So,

**Dave Jones:** we've got a front panel PCB. Um wow, there's quite a lot going on in here. There really is. Um it's quite substantial. Anyway, interestingly, our mains input here is over like on on like the main board, but it's in its own like complete isolated

**Dave Jones:** section like this. Um and you can see So, our mains input's going in here. Uh I don't see it fused. That's interesting, but we've already got the fuse out there, but there's no on board fuse. We've got all of our input common

**Dave Jones:** mode chokes, no problem. As I said, the Y class caps going down to ground. X class caps, if you didn't know, are the ones that go across the main, so active and neutral. That's So, this would be an X class capacitor, and Y in

**Dave Jones:** like because it's shaped like a Y, and the bottom of the Y goes down to earth. That's why they're called Y class capacitors. Um so, yeah, that looks all groovy. That is our bridge rectifier in there on its own on tiny little heat sink

**Dave Jones:** there for the bridge rectifier. Which brand caps have we got here? Yeah, I don't actually know what brand they are. So, okay, 105° C rated, but yeah, okay, then. Not exactly a Panasonic or a Nippon Chemicon, but okay. They are somewhat building this

**Dave Jones:** thing down to a price, but otherwise, um I'm actually impressed by the design and construction. And this is our driver board here. They've got that on a vertical riser board. That's quite common in power supplies. You may want

**Dave Jones:** to change that later, and you don't You may want to change the control later, and you don't want to respin your entire main board here. So, yeah, that makes sense. And we've got an arm jobby down there, which I can't read on the LCD.

**Dave Jones:** Does that That looks like an ST thing. The other cap down in there is an LH Nova brand cap. They're the output caps. Yeah, once again, I don't know them. And this is actually specifically the UDP 6731 power supply.

**Dave Jones:** You can see that down there. So, yeah, it looks like they're spinning a different board for each version. And check it out. I totally missed that there's another fan in here. Wow, is that like Oh, no, it doesn't

**Dave Jones:** look like an afterthought because it's actually got a soldered hard to see, but a soldered metal clip like bracket down in there that's holding that in place on the main board. So, they obviously maybe they decided that they need some extra

**Dave Jones:** air flow going over the main switching transformer here. Yeah, that's interesting. I haven't really I can't say I've seen that before. So, it's something to note, but yeah, just the the little extra um air circulation inside there. Maybe that was like a dead

**Dave Jones:** pocket or something, but I don't know. Have a look at the fan here. But, I was actually wrong about these being the switching elements. There's actually four diodes under there. I'll put up the data sheet for them. They're like a

**Dave Jones:** Galaxy Semiconductor thing or something. The main switching transistors must be under here like this. I'll see if I can get a number. And of course, the they have got it. You You notice that's very very close to the fan, so they're really

**Dave Jones:** sucking out the air through those power transistors there. And and they've got the fins in the right direction to get the air flow through there. But, yeah, this might have just been a little dead space inside like from a thermal air

**Dave Jones:** flow point of view. And they decided, "No, we need a fan in there." But, that is attention to detail at the design stage because, you know, they've got the bracket. They've actually designed that bracket and they so you know, put that

**Dave Jones:** on the layout of the PCB. And so, it's not like they haven't just whacked that in as an afterthought as a budge. That's That's all part of the thermal design of this thing. Um interesting. The other way to design this would have just been

**Dave Jones:** to have one large uh heat sink just going all the way along there and have your diodes and your power transistors on there. But, obviously the uh designer thought, "No, no bugger it. I want the power transistors on my own little, you

**Dave Jones:** know, heat sink down there or two separate um heat sinks down in here. Why they didn't manufacture that as uh one, I don't know. Maybe cuz it's uh these are maybe just off-the-shelf uh you know, jobbies or something. So, um yeah,

**Dave Jones:** they just used two of those and put them back-to-back and Bob's your uncle. Not going to go through uh the designers of this thing. Suffice it to say that I'm relatively uh impressed by the design and build quality of this thing. It

**Dave Jones:** looks like uh you're certainly getting your money's worth. And I'm not sure if you can see it, but right down in there you can see that there's a thermistor on the uh diode heat sink here. So, yeah, they're putting in the requisite uh

**Dave Jones:** over-temperature protections. And the switching transistors down in there, I can't quite make out the part, but I do see an ST logo. So, yeah, potentially uh genuine ST jobbies. Mention the current shunt resistors, there you go. 5 10 mΩ

**Dave Jones:** in parallel there. They're the output ones. And down there on the output terminals uh directly on the board, you've got reverse diode protection there. It's a little bit wimpy, not exactly a a big power uh jobby. We've just got a

**Dave Jones:** low value cap there. And this uh cap on the um output would should just be in parallel with these ones, but it's literally right on the output. So, it's got a significant amount of uh output capacitance, which does matter if you're

**Dave Jones:** uh switching into constant uh current mode, of course, because then your uh capacitors can still deliver that charge before the loop has uh time to respond. So, ideally you want the uh in power supply design, you want the lowest

**Dave Jones:** possible output capacitance while still keeping your ripple uh low, but also uh when you switch into constant current mode, you don't want to uh uh fry your circuit. So, it's a trade-off. Now, of course, you might remember this uh Ryden

**Dave Jones:** RD6006 DC power supply. This is also a 360 W power supply in uh quote marks and it's way cheaper than this Unit T, but have a look inside, right? So, both 360 W capable uh I believe this is uh I

**Dave Jones:** think this is 60 V max um as well, whereas this is 80, but basically we're looking at the power capability. I've installed this uh commercial Mean Well uh pet mains power supply here. So, yeah, if you ignore all the main

**Dave Jones:** switching power supply up here and just look at this lower half, I mean, look at the difference here, right? Both 360 W power supplies, you got this massive heat sink here just for the switching diodes. You got these uh rather large

**Dave Jones:** heat sinks here uh for the uh switching power transistors, and this one over here, just this piddly little fan like that with that piddly little heat sink and the output choke and the output capacitance and just compare those to

**Dave Jones:** what you get over here for the same 360 W rating. So, if you just compare the physical sizes like that, you know, this one is going to be uh lower noise, it's going to run uh thermally a lot uh lower temperature

**Dave Jones:** and uh than this thing over here. But, this is way cheaper, so you get what you pay for. So, from a thermal airflow point of view, uh really the only part of the uh grill that matters is the one

**Dave Jones:** um on this side. The one on the other side doesn't really matter at all because uh yeah, okay, you might get some inflow here and then down around the bottom side of the board, but there's no power stuff on the back

**Dave Jones:** really that you have to worry about. So, yeah, um just don't block the vent on this side. You can probably block the one on the other side, no worries. Okay, let's power it up. Doesn't look that great on your 16:9 wide screen here, but

**Dave Jones:** uh here we go. We're on. Unit T boot. Bob's your uncle, we're in like Flynn, and I like the display. Any film aficionados? Whoa. Jeez, that's it's stuck. Unbelievable. Look at that. Bobby dazzler. And you might think that

**Dave Jones:** the display is not very bright. It's the yellow display here because we haven't actually set the output on. So I can switch the output on and it gets brighter and then it actually displays the output. So when it's actually

**Dave Jones:** switched off, it goes dimmer like that just to indicate that, you know, it's off but nice bright output thing here and we're constant voltage and constant current mode indicator turns red in constant current mode to match the silk

**Dave Jones:** screen. Everything's hunky-dory. Standard terminal dimensions, no worries. Look at that. Bob's your uncle. So obviously they've got the 4 mm banana jack and the binding post there. Don't mind it at all. We've got the hole in there to put our wire straight through

**Dave Jones:** and also some back part. I would have liked to have seen the back terminal a little like the back metal a little bit bigger for putting your wire in there but overall, I don't mind those. They're pretty decent binding posts. I'm pretty happy

**Dave Jones:** with the layout actually. We've only got the one knob of course shared between the voltage and current. We'll see that in a minute. Got some arrow keys to select which digit you actually want. We've got a scape key for

**Dave Jones:** the menu. We've got an enter key for entering in menus. Doesn't do anything in normal mode. And as I said, we've got the nice output button there. No worries. We've got a menu button. We've got voltage and current right next to

**Dave Jones:** the knob. No problems over voltage protection and over current protection. If you actually hold those down, you can get in there and we've got three voltage and current memory presets like this and we've got our lock button right on the front panel. Really good so

**Dave Jones:** that once you hit that, it's not very bright. I'd like to see it bright like that but it shows a little key lock indicator on here and it doesn't matter what we do now. Keyboard is locked. We can't do a damn

**Dave Jones:** thing unless we unlock that. Brilliant because you don't want to blow up your million-dollar widget when you know management's going to come around and they're going to play with your million-dollar prototype and they're just going to go, "Oh, what does this

**Dave Jones:** knob do?" And you've got it hooked up directly to your 5-V rail and you blow your entire board on your million-dollar project. Um yeah, trust me, I've seen it happen. You don't want that. Lock. Beauty. And it does remember your last

**Dave Jones:** set voltage and current. So, we can go in here. Voltage, let's say we've got you know 5.16 and then we've got you know 0.44 amps, something like that. Okay, and we switch that out. And if we just switch that off, boom, we go back

**Dave Jones:** in there and that should come back. And it does. Winner winner chicken dinner. And as for the display, I really like it. The digits quite big enough. You can read them from some distance away. It could have been a little bit

**Dave Jones:** bigger, but anyway, you've got your output voltage, you've got your output current and it calculates your output power. Nice 10-mV resolution on voltage, 1-mA resolution on your current and 10-mW resolution on your power there. And you can see it's pretty fast at

**Dave Jones:** updating. No worries. And over here you've always got your set voltage, current and output power. Although here I don't think you can set an output power limit. The constant current limit indicator there is not that bright. It's a bit hard to see, but you've got it

**Dave Jones:** nicely down here in the red. No worries. And your limits here are your overvoltage protection and overcurrent protection. I think they're just software. There's not like a has a hardware crowbar, I don't believe. But anyway, we can set that and our little

**Dave Jones:** cursor comes up and then we can adjust that. So, we can move our cursor over using the cursor keys and this is how you set the voltage and the current. So, let's say we're powering a 5-V digital port. You absolutely do not want your

**Dave Jones:** voltage output going above 5.25 V like that. So, we can enter a 5.25. And one of the cool things is you can either use the arrow keys like this or you can just press uh the knob like this to actually

**Dave Jones:** switch your digits. But, anyway, once you've done that, you just hold that in or you can hold in the enter key. We've turned out on our over voltage limit like this. So, then, if we go into voltage like this, 4.5 volts, we should

**Dave Jones:** not be able to go above over the limit voltage, 5.24. So, no idiot managers, you can come around and screw up your design. I wish it could be password protected. And another nice feature, you can set it so that the

**Dave Jones:** output uh can automatically come on when you re-power the thing. So, that's what keep up the top is, and you can actually access that uh down in the menu there, output uh state. So, I've set that to uh

**Dave Jones:** keep. And if we shut down this, and we re-power, we should find that it should come back up, and the output will switch back on. Beautiful. And you saw it there before, uh the knob will actually act as

**Dave Jones:** a proper power supply knob. So, if we go into voltage uh set mode, our cursor's on the last digit over there, and you can see that our voltage will actually change instantaneously on the output like that. And if we jump

**Dave Jones:** over like to like 1 volt like that, it jumps down pretty quick. So, that output uh capacitance ain't doing a lot there. So, yeah, that's change it really quick. Nice. So, it acts like, you know, a proper old school knob on a power

**Dave Jones:** supply, rather than uh you set the voltage and then you go. But, some people prefer that. Maybe it should have been selectable? Uh I don't know. Leave it in the comments down below, but I like that it actually does that. But, I

**Dave Jones:** can understand people who want it to, you know, they don't want to ramp it up. They want it to suddenly set the voltage and then jump up. But, you can do that same feature with the uh memory uh

**Dave Jones:** button. So, you can just pre program the memory buttons and then just hit that, and it'll automatically jump up to whatever voltage or current you set. So, I guess you do get the best of both worlds. And speaking of the memory

**Dave Jones:** groups, if you want to program them easy, we're currently set to 4 volts and 0.44 amps and we can just hold down one like that, save okay, and then we can just go to whatever this one is switched

**Dave Jones:** to. I don't set to zero. Yeah, they're both set to zero. Haven't used them yet, but now we can jump back to 4 and 0.44 amps. Nice and intuitive, works perfectly. But they advertise the fact that they actually have 200 groups of

**Dave Jones:** these three memory spaces. So, if we go in here, we can actually go into memory here and see M1 and it shows the actual displays, but we can actually increment that and we can have like 200 * 3. Like, that's just nuts. Who decided

**Dave Jones:** that like three No, no, sorry, 200. I said 300, 200. Only 200 * 3, only 600 different power supply settings. Oh. There doesn't, however, seem to be any ability to disable the four-terminal measurement on the output. So, if I

**Dave Jones:** disconnect the four-terminal measurement on the back, it should not read anything here, but I've disconnected the positive one and it's still reading. Let me disconnect the negative. There you go. I've disconnected both of them and what do we get?

**Dave Jones:** Uh Bueller? Bueller? We still get our 4 volts. Uh what? It shouldn't read anything. So, the only explanation for that is that they've got loose high impedance coupling internally in there and so if you apply external So, if you disconnect

**Dave Jones:** it, it works perfectly, although they do supply these shorting links with it. So, yeah, it doesn't make sense. And then if it's high impedance, then you can override it. But anyway, let's measure the that we're actually getting the output

**Dave Jones:** voltage on these terminals and sure enough there's our 5 volts and if we go to our sense lines uh we should also be measuring yep 5 volts. So, let's try and override those sense lines with another voltage and

**Dave Jones:** then our display should change. So, first thing we do is we'll short out our sense terminals and bingo oh error disable output uh what? It's disabled the output because the sense is zero? Okay. Uh yeah, it's it's literally switched

**Dave Jones:** off. Okay, safety feature uh great. It's but no, it should have gone into constant current mode though, right? Something's up there. Look, it looks like I've permanently done something to it. I just repowered it. I thought I shooting the video I wasn't

**Dave Jones:** but um yeah, I I like error disable output. There's there's nothing on the output. I've got floating um and I've Have I done something to it? What have I done just by shorting out the sense terminals? Uh maybe I shouldn't have done that, but it

**Dave Jones:** should have tolerated that. Okay, I've actually uh fed the outputs back up the uh clacker again. So, basically the shorting links have we recovered? We have recovered. There you go. So, it didn't like that even repowering the thing

**Dave Jones:** didn't fix that, but we're back. Okay. Interesting. Uh maybe there's a cap on those pins it didn't like that I I don't know. But sure enough, if I connect up a battery, it measures the battery voltage. So, that's exactly what

**Dave Jones:** you'd expect, but if I try and turn the output on, so I'll hit the output button here and error disable output. So, I guess that's too greater voltage difference and it's disabled the output. Hmm. Maybe it knows that there's no load

**Dave Jones:** there, so why should the voltage why should there be a voltage differential there? It kind of maybe it's sort of being too smart for its own good there. Yeah, I don't know. I'd have to do extensive testing to try and figure this

**Dave Jones:** out, but yeah, anyway, voltage sense works. Now, the accuracy spec on this thing is actually rather good. I'll put up the specs here and the output accuracy is .1% on voltage there and I've got to hook that up to my BK Precision 8601, which

**Dave Jones:** is a 0.02% class accurate instrument. And you can see 4.4417, 4.45 there. So, it's not too shabby. Set it to precisely 10 there. We're 9.98. So, we're two least significant digits out. I do believe that's in spec. You

**Dave Jones:** can get your confuser out and check. Actually, according to my BM786 here, that's pretty much bang on. So, yeah, I don't think there's an issue there. Oh, what's up with my 8601? I'm getting no loss on the leads because uh we've got

**Dave Jones:** no load yet. Put a 1 amp constant current load on here and we're getting 1.008. So, I think that's within spec. And according to my 786 over here, we're .99 almost .999 there. So, it's reading a little bit over there on the current,

**Dave Jones:** but that's neither here nor there. As I said, I think that's within spec. Now, you'll notice that I do actually have my sense leads connected across the load here and look what happens if I disable if I actually disconnect the load, then

**Dave Jones:** bingo, error, disable output. It's going to do that disable thing again. Um it didn't like that. A sudden spark. Um and I put it back on and it's of course it's reading exactly 10. Even though there is a drop in these leads, it's

**Dave Jones:** actually compensating that and reading back 10 exactly on the output. So, it's actually outputting. So, if we actually measure down here with this meter will whoop oh it didn't disconnect it wasn't fast enough. There you go that's interesting. We should

**Dave Jones:** find that this voltage is higher than the actual 10 volts there by the drop in the leads and 10.05 cuz we're only an amp but there is 50 millivolt drop across those leads and if we increase the current that'll be higher. So I've

**Dave Jones:** increased that to 10 amps there and now we're delivering it says bang on 10 amps and so there's a bit of non-linearity there but anyway so we now we should have a bigger drop on the output here because yeah 10.4 so we got 430

**Dave Jones:** millivolts drop across those leads but because we're using the external sense it's going to read precise it's going to deliver precisely 10 volts across our load while compensating for our leads and that's great. But the problem is is

**Dave Jones:** that you can't disable that. I think that's that's a bit of an oversight. You should be able to disable the external sensing I think. That's just yeah cuz you don't want it you know doing playing silly buggers disabling your

**Dave Jones:** output and cuz I've got to go in there. If I want to change it I've got to go physically in there and actually short out the outputs on the back of this thing again and I don't want to be doing

**Dave Jones:** that higgledy-piggledy. Anyway even at a 100 watts output um that fan has not increased at all. I can't hear it it's basically silent. So that's a winner at 100 watts. I guess we'll have to stress it at the full 360

**Dave Jones:** and see what happens. And at 200 watts I still can't hear a thing and barely any airflow coming from that. In fact I might be hearing the fan from this one instead of this one. I can barely hear it like it's

**Dave Jones:** just not switching on. So that's great and we're now up to the full 250 watt capability of this electronic load and it just switched on its fan. So I don't know if you can hear that fan noise, but

**Dave Jones:** it's not coming from here. This basically hasn't increased at all. Beautiful. What I've got now is I've got it on constant resistance mode set to 1 amp. Now, this has killed power supplies in the past because this is going to

**Dave Jones:** have a loop response in the electronic load here trying to keep the 1 amp there. And it just goes into that current limit just fine and dandy. So, nothing's oscillating, nothing's dying. It's just hunky-dory. So, it's a simple test, but

**Dave Jones:** it just does show that that loop response in the load isn't upsetting the constant current mode in the power supply. And even if I set the maximum output voltage of 80 volts here, it's still it's still handling that just

**Dave Jones:** fine. So, I can disconnect that. Error disable output. Whoa, sparky. And well, yep. No problems whatsoever. Okay, maximum power draw 365 watts. In fact, I haven't actually turned it up. Well, yep. It just something just happened there. Uh the output's still on. Oh, constant

**Dave Jones:** current it went into constant current mode. What happened there? I'm not quite sure. I'll have to review the footage, but yeah, anyway, let's try that again, shall we? Nope. Where output is 0.16. Uh maybe I didn't have my load switch.

**Dave Jones:** Nope. Hang on. No, 13 What's what's what's going on? Something's happened. Uh let me stop. I'll get back to you. Off. And off. Uh Okay, I've looped the sense lines on the back. I've powered it off. Let's power

**Dave Jones:** it back on and see. Hopefully, I haven't buggered it. No, 18 volts. It's back. Okay, let's try that again. Uh Okay, what I've got is an overcurrent protection input disabled here on my Rigol load, but watch what happens. Like

**Dave Jones:** both of these loads are off. Okay? Like they're both the output is switched off. Okay, so they should be a high impedance input. Now, watch what happens when I connect over here, right? It's just I've got 18 volts, 13.5 amps set.

**Dave Jones:** It's oscillating. And I can hear some sort of oscillation thing happening. You can see it on the LED there. The LED is blinking. And this is going silly buggers. What? Disable this? What? My Rigol load is causing that? The input should be

**Dave Jones:** disabled, but why would this be going into constant current mode if our current limit is 13.1 amps? It doesn't make any sense whatsoever. Let's plug this back in. Yeah? It's causing that It's causing that issue again. Oh, I just realized that my

**Dave Jones:** terminals here were loose when I cuz I had my wires in there and I didn't screw them back up, but that shouldn't do anything cuz this load is off. Just plugging in this load with overcurrent protection disabled is causing this thing

**Dave Jones:** to oscillate with a 13.1 13.5 amp setting. What's going on? Okay, let's see what happens, right? I've just got 18 volts and I've just got like 13.5 amps set there. What happens if I short these out? Let's Let's try it.

**Dave Jones:** Yeah? 13.5 amps, no worries. Wow. What the heck is this load doing? Um I Okay, even if we postulate that there's something weird happening with this load even though it's input is supposed to be disabled, it doesn't explain why it would cause

**Dave Jones:** this supply to like oscillate in and out of current mode when it's set to 13 and 1/2 amps. That just doesn't make sense. What the heck is going on here? Maybe you're screaming at me, but I'm I'm not

**Dave Jones:** seeing it at the moment. What would actually cause that? And this seems to work just fine and dandy. So, I'm going to plug this back into the load over here. Yeah, it got to round the right way. And we've got our 18 volts and

**Dave Jones:** let's just go constant current mode 7 amps. 7 amps. Everything's working fine, so we haven't blown anything. What the heck's going on with this thing? And causing but even if this thing is somehow faulty and doing something weird, it doesn't explain why

**Dave Jones:** this would go into current mode. I'm going to like just measure ohms on the on the input here. Like what the heck? Yeah, that's shorted. Wow, okay. So, we might have killed the Rigol DL3021. That input is shorted. Overcurrent

**Dave Jones:** protection input disabled. We might have killed it putting both of these loads independently in parallel across here. Um what? Why? Okay, I'm going to choose okay. Going to re-power this. I know that like now we're getting into the territory of

**Dave Jones:** troubleshooting what's going on here. Um that we might have killed it. Oh my goodness. Okay, let's let's shine. No. No, it's oh no, it's not shorted anymore, all right? It's it's 200k. Okay, so everything's hunky-dory now. All right? So, that's gone into

**Dave Jones:** some weird mode. Okay, so let's go over here and we had that set for uh let's set that for 7 amps. I think we had that before. Now, at 40 amp range, 7 amp uh current limit, and let's go over there

**Dave Jones:** and see see if it works. Uh got to turn on. And it works. We haven't killed it. Okay, that's weird. Okay, this Rigol will wrap that up to this Rigol load doing something weird, and it was shorting out, and maybe it was like

**Dave Jones:** like it's obviously not dead short. It was some sort of electronic short, and it was causing this to oscillate. But anyway, okay, that's kind of a great test. This thing was oscillating off and on off and on. You saw that at like 13

**Dave Jones:** and 1/2 amps at 18 volts. So, that's a couple hundred watts, and that was like not This thing didn't flinch at a Well, we haven't killed it. So, I deem that to be a great test, and inadvertent test,

**Dave Jones:** but that was kind of sort of what I was trying to do with that 1 ohm constant resistance mode, trying to get it to, you know, loop or oscillate or do something weird like that. And we actually got it to do it. So, okay, that

**Dave Jones:** is a pass. Um great. It's robust. Okay, ripple and noise here at low load, the value the spec is 12 millivolts RMS. They don't give you a peak to peak value, but as you can see, well, I can clear those

**Dave Jones:** sweeps and reset the averages here. Peak to peak is 137 millivolts. This is at a 5 volt output voltage RMS 5 millivolts. So, yeah, no worries. So, it is under the RMS, and you can see the but you can see the clear switching

**Dave Jones:** noise here. This is 50 millivolts per division, 120 kilohertz switching frequency there, and well, yeah, that's what you expect from a switching supply. You get what you get. You don't get upset. But it's well within spec RMS-wise, and if we bump the voltage up,

**Dave Jones:** we'll find that that is going to drop. Let's go Let's go all the way with LBJ, shall we? 82 volts here, and it's slowly coming down. We're AC coupling, of course, and it's actually much less there. So, at the max voltage,

**Dave Jones:** you can see that the peak-to-peak has gone down significantly here. But, uh you know, we're only talking uh you know, 78 millivolts peak-to-peak. But, the RMS has gone up a little bit. We're talking six millivolts there. But, yeah,

**Dave Jones:** still half of what the uh spec says. But, uh let's whack a load on this thing. So, if you're keen to see the switching noise in there, there you go. We can stop that, and there you go. There's our switching, and if you go

**Dave Jones:** out, you can see whoa, there's not really much ripple, is there? Is it? There's really no low-frequency ripple there, cuz all you care about is really on the switching supply is the switching frequency, which is 120 kHz. I'm going

**Dave Jones:** to plug in a 2-ohm resistive load here. So, at whoa, 20 volts, there you go. We're delivering 200 watts. Oh, look at that. We're all over the shop there. Look at that. We've got an extra little doohickey in there, extra little

**Dave Jones:** frequency switching. So, that's still at 120 kHz there, but it's added an extra That's just not a capture artifact. That's actually really there. It's actually got two little switches in there. So, it's changed modes at that higher current. And what happens if we

**Dave Jones:** go into constant current mode there? So, I'll do just 9 amps there. And uh well, let's restart that. Well, there we go. So, there it is there. And let's plug it in. Constant current mode. Yeah, it's doing the same. Still doing

**Dave Jones:** the same job there, but you'll see that we have some lower frequency stuff in there now. Look at that. There you go. It's getting toasty now. Whoa, Annie, Bernie. Um but we're still looking at uh 7.5 mV RMS there. And let's test the uh

**Dave Jones:** switch on now and um yeah, I had it set to AC couple and went "Ooh, you little prick." Yeah, DC couple, Dave, you dog. So, let's try that again. Let's single shot capture. We'll switch your output off uh 1 V per division uh rising edge

**Dave Jones:** trigger smack in the middle and boom. There we go. That's very nice and clean. There's only a small hint of uh something happening right at the start here, but you know, that's a nothingburger. Um so, yeah, I'm I'm

**Dave Jones:** pretty happy with that. There's no overshoot at all. Beautiful. And what time did that take? Uh it's 200 ms uh per division there, you know, about 300-odd ms, something like that, to ramp on. But it's not But what you care about is nice and clean.

**Dave Jones:** There's no overshoot. So, uh it's not going to ruin your day if you're you know, you're powering your 5-V TTL stuff and it jumps up to 12 V. You don't want that. And there's the same time base at

**Dave Jones:** uh 80 the maximum 82 V there and you can see that took What's that? Uh 800 ms or something to ramp up. But once again, there's no overshoot at all. It's beautiful. Okay, let's try that again, but let's do

**Dave Jones:** falling edge, shall we? So, single shot capture and Yee, that's taking a while. I'm going to have to zoom out. Let's try that again. Once again, from maximum 82 V, so I will switch it on and switch it off.

**Dave Jones:** And come on, you can do it. Boom. Look at that. Perfect ramp down. No worries whatsoever. Um and how long's that taking? Couple of seconds? Yeah, 2.2, but it's nice and clean. There's no overshoots or anything. And there we go. That's the

**Dave Jones:** ramp down from 5 volts. That was me ramping it on and that was ramping off. So, once again, that's very clean. Beautiful. Okay, let's test it going into constant current mode, shall we? So, there we go and boom! There we go.

**Dave Jones:** That went cleanly into pretty cleanly into constant current mode. We don't know if you know there's some contact bounce in there or not. Constant voltage mode down into constant current mode didn't overshoot, didn't oscillate, do anything weird like that. Let me just

**Dave Jones:** try that again, shall we? Here we go and boom! Like that. Yeah, it looks like that's just my contact. I'll see if I can do it faster. I'll go over here. Let's try it again. Boom! Look at that. There we go. Clean.

**Dave Jones:** Clean as a whistle. So, what does it look like exiting constant current mode? Well, I'm glad you asked. We can go in here and we can go back on the trigger on the rising edge again. Single shot capture and

**Dave Jones:** boom! Look at that. That's clean. We can try that again with a longer time base, but you can see it there. No worries. Yep, it's clean. Clean bill of health. Only one more test left. What happens when we power it off and we do

**Dave Jones:** the power on thing where it like automatically switches on. I wouldn't expect any difference, but I will check it nonetheless. So, hopefully I've got that trigger right. And five, yep. Beautiful. So, no worries whatsoever. So, it passes all the test going in

**Dave Jones:** into and out of constant current mode and uh switching the output off and on and even restarting the output when you switch uh the unit on physically on at the uh power switch. Um so, yeah, and at uh higher voltages, too. So, it's pretty

**Dave Jones:** good. I like it. Okay, lastly, let's try the instrument application which you can get with this thing. Uh sadly, it doesn't have uh networking, so it's got the RS232s. So, I've connected it in. I installed it, had the stupid National

**Dave Jones:** Instruments NI-VISA install and that didn't work cuz I've probably already got it installed for 10 million other things. Hate the bloody NI-VISA thing. Um leave it in the comments down below if you're a similar. Anyway, I just did

**Dave Jones:** the scan. Um it was default uh Here we go, RS232. It was default 9600. You can change that in the uh menu in there. So, let's uh UDP 6731. It found it. And there it is. And sure enough, um 5 V.

**Dave Jones:** So, we can control this sucker. There we go. Look Look at this. We can turn it up with the knobby. Um whoop. That That took a while to respond there. But uh yeah, so we can use the slider.

**Dave Jones:** Presumably, we can type type in 5. Yep, we can indeed. Um okay, we can turn on overvoltage protection. We can set the um the voltage there. Nice, okay. So, let's actually try that. And if we try to slide that higher, nope, it

**Dave Jones:** beeped at me. I heard it beep. So, yep. It It doesn't show me a message, but it beeps and then goes back. Winner. Um and now we can do the listing thing. So, we can actually um set Whoop. Hello, why is

**Dave Jones:** that Uh let's go full screen. Ah, here it is. Okay. Right, so this is what This is the graph. That That's really quite nice, voltage and current here. So, that's really groovy. I don't know where that little point one five point

**Dave Jones:** one five amps came from. I've got nothing connected to it. Don't know what's going on there. Oh, so this is a log. I thought this was This is logging like every second or with a bit more than a second. Um I thought this was

**Dave Jones:** like the listing cuz you can set up a list of things so you can get it to like cycle through different voltage and current modes and things like that. Good for like ramping up products and you know, um automated testing and stuff

**Dave Jones:** like that. So, that's just a log. Okay, so that's just a graphical table of uh and no, it is Yeah, it's like twice a second. Yeah, I think it's about twice a second there. What are our options? Interval, okay, sample time interval,

**Dave Jones:** sample interval, sample points. So, let's go to 100 milliseconds and see what that does. Doesn't seem to be any quicker. So, that's like the maximum it can do over the RS232, I guess. Now, as I mentioned, the manual here um talks

**Dave Jones:** about this list and delay function and it looks like that was like runs on the screen, but I didn't see that when I was operating it. So, um and it doesn't seem to be in the software. So, it's assumed

**Dave Jones:** it'd be in the software, but it doesn't appear to be. It doesn't There is no like Well, no, that's just English and then like there's no options to do anything. We can export the data, okay, but uh So, it's kind of useful that we can log

**Dave Jones:** it, but yeah, I I and that's just a quick setting so we can set voltage and current. Um but that's in addition to the memory down here. Uh um but anyway, it looks like you can Yeah, you can set up those like 200

**Dave Jones:** memories here so you can set those up, but also this just allows you to quickly jump and um do whatever, but uh that's a bit underwhelming, isn't it? Um I was hoping to get like a list of things.

**Dave Jones:** Bummer. Well, that's embarrassing. How did I not find this before? While you're in regular operation, you can just use the arrow keys to go across to the delayer function or to the list function. So, there you go. That's

**Dave Jones:** pretty cool. All right. It wasn't obvious. Shame you can't do it in the software though. It doesn't look like you can. Now, the delayer function is useful more useful if you had a multiple output power supply and you want to like

**Dave Jones:** sequence power supply say for like a complex FPGA or something like that that needs, you know, sometimes to uh power up the voltage rails in a certain sequence. Otherwise, you can come a gutser. You can get like like SCR latch

**Dave Jones:** up inside the chip and stuff like that. Anyway, um so, yeah, something like that. So, unfortunately, there's no external trigger on this thing. So, it's not like you can have like a manual external trigger. So, you could have

**Dave Jones:** multiple supplies and then you'd have to start the timer the the delay is all at the same time. But, you can potentially do that. list function, as I said, is just the ability to like cycle through different voltage

**Dave Jones:** setting voltage and or current settings based on time. So, you can sequence the voltage and current to do particular things that you want to do over a sequence of time. So, if we go in there, we can cycle

**Dave Jones:** infinite or we can go as many cycles as you want. So, you can just do it like do it once or you can just keep on repeating. So, let's just do it once, shall we? Unfortunately, the user interface is very confusing. They've got

**Dave Jones:** what looks like like soft buttons down here. And of course, this is not a touchy-feely screen and there's no actual buttons there. So, instead of that, you've got to actually well, escape from there and then your knob actually selects the various things and

**Dave Jones:** status stop and then you can enter that and then run, save, and clean selection. Gets I guess that resets it all does it? It's totally non-obvious. So then we go in there like we can go into that one

**Dave Jones:** and then we can select which one we want like that and then we should be able to Okay, let's go like first set in here. Let's go do do do do. So you know, it's a bit tedious but it works. Okay, one

**Dave Jones:** and then we can escape like that and then we can jump down to Well, let's just keep it on 2 amps and let's just go over it. So let's escape back out and go over here and then we can enter. Yep.

**Dave Jones:** And we can go in there and then we can adjust that to 2 volts for example and then we can escape out of there. Once you get the hang of it, it kind of works. Of course, this is not something

**Dave Jones:** that you set up all the time. So the fact that it you know, takes a little bit to do it it's neither here nor there. Right. So how many of these? We should go up to the full. Is that the 48

**Dave Jones:** for the counter up there? Yes, it is. Okay. So that's how many counts that we go through. So I've set up Well, I'll set up five here. It would have been nice if it like auto scale this window cuz it knows I've only got

**Dave Jones:** five counts and it knows that I'm only going 1 2 3 4 5 volts like this. So be nice to be able to auto scale that cuz you can just kind of sort of see this if you squint you can see the steps I've

**Dave Jones:** actually programmed into the yellows of voltage and blue is the current. Anyway, I'm going to run this and we'll see what happens. So Okay, let's run that. So I've selected run. I've got 1 second for each of those and

**Dave Jones:** Oh, single single shot capture. Okay, let's run. And we're single shot capture on the scope. Hopefully, I've got that set up correctly and it's running and it's completed in 5 seconds. What's my scope doing? Yep. Oh, there it

**Dave Jones:** is. Oh. That's interesting, is it not? What's going on here? Look at this little extra sort of like down and up. What's going on there? It's in each one of them. That is weird. Is it not? That there's something going on there.

**Dave Jones:** Not too happy with that. That should be clean. We've seen before that when it changes voltages, it does it really cleanly. So, not sure what the deal is. Just as this quick sanity check, I've got 5 volts programmed into uh M2 here and 6 volts

**Dave Jones:** programmed into M1. So, I'm going to single shot capture that and we're at 5 volts and I'm just going to go to 6 volts like that and I'm going to see what happens. Uh had the threshold set wrong. Dumbass.

**Dave Jones:** All right, let's try that again. I've got a faster uh time base this time and we're assuming going from 5 to uh wasn't bloody in the center. Unbelievable. Single shot capture that again. It's in the center and 5 to 6

**Dave Jones:** volts. Boom, it's clean. Right? It's clean. So, what's going on? That's the same 1 volt step. So, what's going on with that programming mode? That is really weird. Let's try that again and see what happens. Run. Boom. It's running. Running. Running.

**Dave Jones:** Should capture it. And boom, we get the same little quirky thing. That is some sort of bug. I'm not sure what the heck that is, but yeah. Got you. Huh. Uni-T, um get back to us on that one. Firmware

**Dave Jones:** update. Leave in the comments down below if you got any good idea what would actually cause that. I offhand, I don't know. So, anyway, that's a review of the Uni-T UTP 6700 series, the uh top of the range 6731. As I said, available in like

**Dave Jones:** different voltage and current and power grades here, but yeah, a very nice supply. The design and build quality is really excellent. I like it. I I do like, you know, the list is a bit it's a bit how you doing and it's like

**Dave Jones:** user interface, but I do actually like the actual the main user interface is really quite nice and it works quite well. It seems very robust and it's hasn't got the best peak-to-peak noise. So, if you're, you know, after that peak-to-peak noise,

**Dave Jones:** it's decent RMS noise, but yeah, the peak-to-peak's a bit high, but anyway, that's why they don't spec it, right? Yeah, I expected it to be a bit better, but anyway, it looks like a really well-built and robust supply in

**Dave Jones:** the nice form factor. I like these small vertical form factors and the UI works really quite well. So, just an issue with that. I don't know what's going on over there. They probably need to fix that. And yeah, the software's a bit

**Dave Jones:** disappointing. I would like to have seen better. I checked at the moment there is no support for this in the test controller that free test controller software which I've done a video on, but you can easily add it

**Dave Jones:** yourself or I'm sure, you know, someone will actually add that sooner or later. But yeah, it's a nice little power supply. It's worth checking out. So, anyway, I'll leave the link down below. Thanks Uni-T for sending that one in. As

**Dave Jones:** always, thoughts and comments down below or over on the EEVblog forum, always linked down below. Some teardown photos over on the EEVblog website and my merch as well over on evblog.store. Catch you next time.
