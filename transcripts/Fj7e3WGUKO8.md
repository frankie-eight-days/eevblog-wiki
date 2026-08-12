---
video_id: Fj7e3WGUKO8
title: EEVblog #504 - UPS Tutorial & Teardown
url: https://www.youtube.com/watch?v=Fj7e3WGUKO8
source: youtube-asr
---

**Dave Jones:** Hi, welcome to teardown Tuesday. Yes, I'm at the whiteboard. We're not going to jump in to the teardown. Thought I'd just do a little bit of white and board fundamental theory today and then we jump in to the teardown and see if we

**Dave Jones:** can see a similar arrangement to what we get in the basic topology of in this case uninterruptible power supplies or UPS. You've no doubt heard of them. You're probably using one at home to backup power your PC for example when

**Dave Jones:** the mains power fails then the battery inside the UPS takes over and supplies power for 5 or 10 minutes or maybe even longer so that you can continue to use your machine or at least it gracefully can gracefully shut down and save your

**Dave Jones:** work for example. So if the power just fails boom, it doesn't just shut off and you lose everything. So very common device the UPS. And there's actually three types so basically three different topologies. There's a few more but these are the

**Dave Jones:** three basic types which will have a look at. There's the offline standby type probably the most popular you'll find in the really cheap ones. There's line interactive which is the one we'll take a look at today in the teardown

**Dave Jones:** and there's the full online / double conversion type which is the more expensive and reliable types for the more robust applications. So if we take a look at the basic offline standby one you're probably familiar with how they work.

**Dave Jones:** We've got AC mains coming in here. AC mains going out. That's it. And inside we've got ourselves a AC to DC rectifier here. Yes, it's just a traditional bridge rectifier or whatever and that goes into a charger which then charges

**Dave Jones:** the battery and then the battery goes into a switcher or which is usually a H bridge arrangement but it doesn't have to be. But it basically a switcher driving the uh of a transformer and the secondary of the transformer produces your sine or

**Dave Jones:** your square wave out. And then they've got a basic switch in here which can uh usually this thing by meaning offline, it means that the uh the charger and battery part of it is usually offline. So, it's switched out

**Dave Jones:** and your AC is switched directly through to your output like that. So, only when it detects that main input mains power has failed, does it rapidly switch over. So, I haven't shown any switch in here, but it rapidly uh starts up the uh

**Dave Jones:** inverter in here, your step-up uh conversion here, and generates your sinusoidal or square wave output voltage. And it you can usually, you know, it can take it from, you know, tens of milliseconds or 100 milliseconds or something to sort of switch over and

**Dave Jones:** start up. So, the device that you're actually powering has to be able to handle that little uh sort of, you know, drop out or brownout as it uh switches over to the battery backup. Now, that is uh the cheapest and most uh common one.

**Dave Jones:** Now, I'll skip this line interactive one for a second, and we'll jump straight down here to the online {slash} double conversion type. You'll see why it's called double conversion in a second. Now, the difference between these two basic types is that this is the offline

**Dave Jones:** type, as I said, the usually the output is powered directly from the input, it's switched straight through. So, it's the uh battery backup part of it is offline, but you guessed it, the online type is where the uh battery is continuously

**Dave Jones:** powering the output here regardless of what the input is doing. And that's why there's no switch going through the AC input through to the AC output, cuz it's all that power is always coming, well, not necessarily coming from the battery,

**Dave Jones:** but actually coming from the DC rectifier down here. And you'll notice that all of the, you know, all the common components are still there. They're virtually identical. We've got our AC rectifier down here. We've got our battery charger. We've got our

**Dave Jones:** battery. We've got our switcher with our step-up transformer to generate uh either your sine sinusoidal or your square wave output. But, you'll notice that there is no switch connecting it can't bypass any of this stuff. It's always working. And what we're switching

**Dave Jones:** here, instead of switching from input directly to output, we're switching basically whether or not we want to power the output from the battery or from the rectifier circuit down here. And that's one of the big differences. Uh one of the main reasons you want to

**Dave Jones:** do it is for isolation. For example, you'll notice that there's no directly direct electrical connection from the output to the in- input. I.e., it's galvanically isolated. So, if you if your uh the device you're powering needs to be

**Dave Jones:** electrically isolated from the input, then an online or double conversion switcher is the way to go. But, as you can see here, there's no isolation. Even though we've got a transformer in there, you'll notice that it's all common like

**Dave Jones:** that from the input to the output. And the other main reason why you want to use the online one compared to the offline is that uh if you've got a real noisy mains and it's always dropping, there's always brownouts and dropouts,

**Dave Jones:** and all sorts of stuff, you don't want this thing to be continually switching back and forth between the uh input and the input and the battery, for example. You're much better off on those noisy in those noisy and troublesome environments

**Dave Jones:** to go for an online conversion, where it's just always running from the DC here. And that's why it's called double conversion, because we're converting AC into DC, and then it's permanently the output here is permanently running from that DC connection. It's not switching

**Dave Jones:** through the AC and then switching between AC and DC sources effectively. It's always powered from that DC source. That's why they call it the double conversion cuz you're converting once and then you convert it again. Yes, this one does it up here, too, but there is

**Dave Jones:** the option to switch through with no conversion at all. Hence the name double conversion. But one of the disadvantages of this double conversion type is that Well, you notice that this switch down here is switching the low relatively low

**Dave Jones:** voltage battery for example, 48 V battery might be typical. They might be using 12 V for example. Then lower voltage Ohm's law still must apply, right? That means for the same amount of output power delivered to the load, you've got

**Dave Jones:** much higher switching currents in here. So, I've shown this as a, you know, a mechanical switch or relay, and the topology doesn't exactly need to be like that. But it it basically means you've got very high switching currents in here

**Dave Jones:** that you have to switch from the battery. Uh up here, if you're got, say for example, a typical 10 amp mains outlet, well, you only need a 10 amp relay in there. That's it. Not a problem. But down here, you need much,

**Dave Jones:** much higher current. So, the switching can be an issue down here. And also, this rectifier down here has to deliver the full load all the time because you notice when it's not powered from the battery, it's got to deliver all that

**Dave Jones:** power from that poor little rectifier down in here. Whereas here, the rectifier is only only needs to be um sized enough, designed well enough to deliver enough power to charge the battery, which might be much, much less than the output load

**Dave Jones:** is capable of. So, that's why these things are more expensive and more difficult to design. They're going to run hotter, things like that cuz the circuitry inside is got to deliver that full load, and then you've got losses in

**Dave Jones:** there, and the switch is always got to be operated and delivering the output load. Whereas up here, your switcher or output load might only need to be sized and designed for operation for 10 minutes, 30 minutes, for example. But

**Dave Jones:** this thing, it's got to work all day, every day, 24/7. So, this thing needs a lot more cooling and much better design system. So, that's why it's typically more expensive to design an online UPS. So, that brings us to the third type,

**Dave Jones:** which we're actually going to look at in the teardown today, is what's called a line interactive UPS. And it's essentially exactly the same as the offline standby type, but it's a bit of a compromise between these two in that,

**Dave Jones:** let's say you've got, you know, a and mains input here, which sort of, you know, brown and browns out or drops out, you know, a couple of times a day. You don't want the thing always switching over to battery. So, instead of it

**Dave Jones:** switching over to battery, what they include in here, you'll notice it's virtually identical, except for the fact that in this path here, where it's the AC is switched through, there's actually what's called an auto transformer in there with

**Dave Jones:** various little taps with some other switching relays in here that can then, or you know, doesn't have to be a relay, it can be an electronic switch as well, then it switches between the different taps on the transformer. So, let's say your

**Dave Jones:** mains input, normally 240 volts, it drops down to 220 or 210, then bingo, what they might do is then switch to this tap here, which then the output voltage is going to be boosted up a bit. So, you're still going to get your 240

**Dave Jones:** volts out. It can compensate for small variations, you know, 10 or 20% variations in your mains input. If your the device you're powering cannot handle that, and then likewise, if the mains input here goes up, goes above what your

**Dave Jones:** load, you know, I really wouldn't like to have, then it can switch in this tap here can switch over to here and then you'll notice that the output is going to be somewhere below, because it's a different tap, somewhere below that

**Dave Jones:** mains input voltage. So, it can accommodate both higher and lower input voltages without having to switch over to the battery backup system. So, that's what a line interactive UPS does. Sort of a compromise between those and that's what we're going to take a look at now.

**Dave Jones:** Oops, I forgot to include that little line in there powering our AC rectifier there, but when we take a look at our teardown now, which we're going to do in a second, we expect to see all these basic components in here. We expect to

**Dave Jones:** see a big ass auto transformer. It's going to be big ass because it's delivering all of the full output power load, the full, you know, 2400 watts or whatever, through to the output. So, that's got to be a big beast. Then we're

**Dave Jones:** going to have our rectifier, we're going to have our charging circuitry, we're going to have our battery bank. In the case of this one, I know it's 48 volts. Then we're going to have our switcher, most likely a H-bridge configuration. We

**Dave Jones:** won't know until we turn it until we actually take it apart. The H-bridge configuration is going to have four large MOSFETs in there driving the primary side of the step-up transformer, which could possibly be integrated into the main auto transformer here with

**Dave Jones:** another tap. We'll see when we open the thing and and that's pretty much it. We expect to see some big ass relays to switch the taps or some electronic components to actually switch those. Instead, most likely we're going to see

**Dave Jones:** relays in this thing and that's what we expect to find. Will we? Only one way to find out. Take it apart. And here's what we're tearing down today. Please excuse the fact that I've got this thing on the floor. It is a

**Dave Jones:** massively heavy base. It weighs more than a brick, Donnie, and I'm sure it's built like one as well. What it is is an APC. They're a top brand in the UPS business, so we expect top quality. It's a smart UPS model 2200 XL. As you can

**Dave Jones:** see, a rack mount unit designed for server backups and things like that, three unit high rack. And yes, I scored this one from the Australian Defense Force auction that I scored a whole bunch of other stuff, as you've seen in a previous

**Dave Jones:** video. And this is just a front fascia panel here that just pops off to reveal the control panel here and the internal battery pack. I do have a second rack mount unit which just contains an extra two sets of batteries as well. And

**Dave Jones:** you'll see the other connector on the other side. So, this one can have three sets of batteries hooked up to it. And it's model number is SUA 2200 RMUXL to be precise. And you can see on the control panel here why it's a line

**Dave Jones:** interactive UPS. It's got two LEDs here. One to show that look, what happens when like to show you indicate that the mains voltage has gone over voltage and then it needs to correct and pull it back down. So, it needs to switch in that

**Dave Jones:** extra tap there. And then likewise down here, if the mains voltage is sagging, it needs to pull it up and correct it like that. So, obviously it's switching in the taps on the auto transformer there. And there's charge

**Dave Jones:** level and various other stuff, bad battery and whether or not I think that LED is for comes on when it's powered from the battery. And there's some test functionality as well. It's got a Anderson connector on here by

**Dave Jones:** the looks of it for the battery bank. And that just uh, swings around and we can pull I've undone the screws on this. We can pull this sucker out. Needs a bit of percussive maintenance, I think. Hang on.

**Dave Jones:** There we go. There we go. We got it. Bit of percussive maintenance and uh, the battery weighs an absolute ton. More than a brick dunny, as I said. And that will pop out. But the thing is even with that it's still very heavy. So

**Dave Jones:** obviously there's a huge monster uh, auto transformer in here. So uh, we expect to find that. You can see it comes in two models. We got the lower one here, the 2200 W one. Does come in a 3000 W one which uh, maximum input

**Dave Jones:** current of 15 amps. And that's what will and output rating 2700 W. This is 1980 W. So almost 2000 W output power. You see it does have a 15 amp uh, mains input jack there. Uh, what have got a USB interface. We've

**Dave Jones:** got a serial port uh, EPO that's emergency power off. And there's the there's the other Anderson connector the second one that goes off to the battery pack the external one which I've got two. This I believe is an option

**Dave Jones:** slot. There's nothing underneath that so I'm not sure what's actually installed in this thing. I haven't you know, I actually been able to power up and communicate to it or I haven't even tried but there's all the output

**Dave Jones:** connectors big whopping 15 amp one plus eight 10 amp outputs as well. All wired in parallel of course so of course you can't draw 10 amps from each one. You're limited to that 2700 W total. So that's all those outputs are more for

**Dave Jones:** convenience sake. All right, got my cordless drill this time to help out. There's a few screws on this thing. So let's crack it open. And as I said, what do we expect to find? Well, uh pretty much exactly what we saw on

**Dave Jones:** the uh whiteboard there. We expect to find a big ass auto transformer, of course, that'll be the bulk of the weight in this thing. It'll be absolutely massive. And uh we expect to find a uh rectifier. That'll be uh

**Dave Jones:** pretty beefy to handle all the uh charge current for these batteries. I'm not sure what it actually uh charges at, but I'd expect that pretty darn beefy as well. Has to be, especially when it's uh charging external battery packs. We'll

**Dave Jones:** most likely find a huge uh H bridge uh in inverter in there. We'll uh find some massive wiring for the batteries and all that sort of stuff. And uh the H bridge, because there's so much power involved, um I

**Dave Jones:** expect the uh not to use a single MOSFET for each um branch there. There's probably multiple ones in uh parallel. That'd be my guess, anyway. So, we'll give it a go.

**Dave Jones:** All right, let's lift the lid on this thing and see what we get. No, there's nothing else holding it down. Ta-da! Oh, look at that. We have two transformers. We'll uh get a better look at this beast. I'll set the camera up uh

**Dave Jones:** vertical above it, but uh yeah, that looks very nice at first glance. Wow, beauty. Now, first of all, that was a bit of a surprise. We've got two separate transformers here. I expected one huge uh transformer, but I guess uh

**Dave Jones:** I don't know for uh technical or manufacturing or uh performance reasons, they decide to go with two separate ones, but if you'll notice that there's a huge cable over here. I love the fact that they've actually clamped that down there with a

**Dave Jones:** a crimp lug and they've screwed it down. You'll notice that there's no connection from basically this is the this is the primary of the transform well, depends on which way you're talking about your terminology. If it's powered from the batteries, then this is the

**Dave Jones:** primary and then this becomes the secondary. So, we'll just call it the battery side of the transformer. You'll notice that there's a huge bridge joining those two, but there's no tap coming off that into the main circuitry. So, really it's effectively just one

**Dave Jones:** winding there. So, they're using this as one big transformer. So, it's not a center tapped winding on that. So, they're definitely a H bridge to do it and if you have a look down in here, ta-da, you'll be able to

**Dave Jones:** see that. Here's where the wiring comes off and once again, huge big crimp terminals screwed into what looks like the heat sink. Well, it is the heat sink for the power MOSFETs, the switching MOSFETs down in there, which

**Dave Jones:** we'll have a closer look. I'll get the macro lens out, see if we can get some part numbers in there, but they're also using that to carry the current down there as well. And you'll notice that there's one, two, three, four. So, I

**Dave Jones:** that looks to be correct. It looks to be a H bridge because that's the most typical configuration. So, it looks like we're going to have four sets of power MOSFETs here, each on their own thing. Each on their own little heat sink slash

**Dave Jones:** current conductor there. And you'll notice that So, these two, there's one over here. So, this top one is the uh black wire which goes over the transformer or one side of the transformer. The other side of the transformer goes to this

**Dave Jones:** um part of the bridge. And then the battery will be connected to these two inner ones. And that H bridge arrangement switches the battery and then alternates the uh supply onto the transformer. And we can see that uh H bridge

**Dave Jones:** configuration on this DaveCad drawing here. Please excuse the crudity of the model. Didn't have time to build it to scale or to paint it. What we've got is uh four MOSFETs here. And you can see why it's called a H bridge cuz it looks

**Dave Jones:** like a H. If you take out that line there and take out that line there, it looks like a H with the uh transformer in the uh center taps there. And we've got our 48-V uh battery across here. And we've got uh

**Dave Jones:** two P-channel MOSFETs up the top. Or as we'll see uh in this case down here, we're going to have multiple ones in that parallel. But it's exactly the same thing. They just uh getting higher power dissipation, better power dissipation

**Dave Jones:** there. So, um basically, I won't go into H bridge in detail, but basically, you can switch pairs like that, which then you can alternate the polarity on your transformer there. So, that's how you can switch it. But then if you just

**Dave Jones:** switch them off and on and had just a simple square wave uh output, which the cheaper UPSs do because when you turn on a MOSFET, you know, they've got very low on resistance so that when you um uh yeah, if you just do a square wave

**Dave Jones:** output, then uh these things turn on hard and there's not a huge amount of power dissipation in these MOSFETs. Although they try to, you know, there's things with gate capacitance and everything else. But and driving conditions, we won't go into any of that

**Dave Jones:** detail. But because we're getting a sine wave out of this thing, we're going to have to dissipate more power in the MOSFETs, which is probably why they've gone for um the arrangement with, you know, this huge uh huge big heat sink. And it looks

**Dave Jones:** like they got four parallel MOSFETs on there as well. As you can clearly see, that's the configuration we've got. We've got our uh transformer uh hooked on to uh two of the taps effectively on that H bridge, the uh center taps there, and

**Dave Jones:** then we've got our battery hooked onto these other two down here. If we follow the wires, we'll find that they actually these two plates here uh go down to the battery pack. I find it rather interesting that they've got a quite a

**Dave Jones:** hefty amount of uh capacitance there across the uh battery uh terminals. Not sure why they're doing that. They're uh 1,500 microfarads at uh 75 volts. I can't get in there to see the uh brand at the moment, but looks like there's

**Dave Jones:** three of those in uh parallel. And uh of course, not an ideal location being stuck between these two heat sinks, which are likely going to get quite hot. But, as I said, only because this is not a full online UPS, this thing is not

**Dave Jones:** used or running 24 hours a day. So, this is going to be dissipating uh uh you know, nothing uh basically until you switch uh until the mains power fails, and then it switches on, and then drives the transformer to uh power your

**Dave Jones:** load. And it does appear that uh the uh battery the internal uh battery pack is just wired in parallel with these cables which go off to the Anderson connector on the output. So, it looks like all the battery packs when you use

**Dave Jones:** the external ones uh just all wired in uh parallel, basically. And of course, we've just got our positive and negative there. There's no um smart, you know, there's no like a sense wire or anything like that. But of

**Dave Jones:** course, um maybe if they wanted to, maybe they could be passing uh some sort of uh sense data over the uh power as well. I'm not sure. I haven't gone into the uh details of how that works. I find

**Dave Jones:** this rather interesting. Check it out. They've got two fans here. They've got a big ass one here, which is obviously blowing air directly over these large heat sinks here. So, I presume that that sucker only turns on when you're when

**Dave Jones:** it's actually powering the load. Then they've got a small little, you know, wimpy piss ant one down here, which might be running all the time or something like that just to get some air flow through the system. And they've got

**Dave Jones:** an additional fan here, which looks like it just Yeah, I can just put my finger through there and spin it. So, it looks like it's just sucking some air over the battery compartment. Now, as for the main board

**Dave Jones:** down here, there's just one board. It looks like it's all combination of surface mount and through hole just single sided. So, I'm not going to take this whole thing apart because I don't expect there to be anything on the bottom of this board of

**Dave Jones:** any note whatsoever. Looks like it's big enough, sparse enough for all the SMD stuff to be on top. And anything of interest is going to be on the top anyway. So, we've got our mains input over here securely

**Dave Jones:** clamped down to the chassis down there with earth. And remember as I said, because this is a line interactive UPS, it is not isolated. So, the transformer is an auto transformer. So, the output the mains output is not isolated from

**Dave Jones:** the mains input. Anyway, if we have a look down here, I should probably get a shot of that. You can see the flow through here. We've got our input filter here. We've got some these five five relays. One two yeah, five relays. There's our

**Dave Jones:** relays used for we're going to be switching some taps down here. So, here's the Anyway, it it flows through. We've got some protect We've got some common mode choke, line filtering. We've got some more filtering. Looks like we've got a

**Dave Jones:** current transformer down there. And here's our output line. So, it comes straight through the input from the input straight through some filtering and some surge protection and stuff like that and then straight off to your output connectors over there and then

**Dave Jones:** we've got the switching of our auto transformer here. So it looks like these couple of relays around here or these two are probably your high side and your low side auto transformer switch. I can't see any electronic switching.

**Dave Jones:** These things are uh What are they? 20 amps I think. 20 amp relays mains are rated of course. So they're definitely going to be able to do the job and they switch the taps on the auto transformer over here. So it

**Dave Jones:** looks like we've only got one on the high side, one on the low side. So not particularly they're not catering for various steps. It's basically is it higher than a threshold? Yes, switch on a transformer and then pull the output voltage lower

**Dave Jones:** and same thing on the low side as well. Got our fan outputs there. Oops, looks like we've got a second current transformer down in there and uh that's all she wrote. Let's get some close-ups. Have a look at our input

**Dave Jones:** circuitry down in here. We can see a MOV directly on the input there and then we've got a classic common mode filter here, common mode choke with some filtering. Moving along we've got a couple of extra inductors here and then

**Dave Jones:** we've got some more filtering. Large, huge filter caps down here and then there's our current transformer. There it is. See here? It's even labeled CT. CT1. You can see that they've got a single wire going through a little

**Dave Jones:** transformer coil there so they can just get an isolated tap off that and they can measure the current coming from the mains input and they've got our and then we've got a bleeder resistor there by the looks of

**Dave Jones:** it. Then we've got ourselves another current transformer down in there. That would be measuring the output current. And of course I'd be tapping the output voltage as well as the input voltage and reading those so they can get the output

**Dave Jones:** power and the output voltage. So, yeah, pretty obvious. Um mains input here and then we've got our the other one over here is measuring the output and these cables here then bugger off to our output over here. And as you can see,

**Dave Jones:** yep, they're all wired in uh parallel there. So, uh there's not they're obviously got So, they've got a separate wire there going off to the 15 amp jack and then all the 10 amp jacks are wired in parallel. And we've got ourselves a

**Dave Jones:** little Well, not a little, a big ferrite. And I'd probably say that this third relay here is the one that actually switches the input directly through to the output basically until Look, they've got these huge beefy Well, that's actually coming from this one

**Dave Jones:** here. I mean, huge beefy tracks in there. I mean, check that out. Joined in and then the output, of course, big beefy ones going over to here. So, I don't know what the exact topology they're actually using for the auto

**Dave Jones:** transformer and the power bypass. But, yeah, these ones are also got beefy power tracks going through them as well. So, make up your own mind. Trace it out if you want to. And we've got more protection here, another MOV there, and

**Dave Jones:** another MOV over there. So, there's no shortage of protection in this thing as you'd expect cuz they actually claim it's part of the functionality of this UPS is to basically clean up your input mains waveform. You know, it it filters it and

**Dave Jones:** it clamps it with some MOVs and then with the auto transformer configuration actually can slightly adjust and correct for the input voltage. Now, there's one thing that I'm is starting to puzzle me, I'm not quite sure about, is where is the rectifier

**Dave Jones:** and the charging circuitry in this thing. Obviously, look, we've got two isolation transformers down in here. If we take a look at these, there they are there, but they're you know, really small fry. I mean, you know, not a huge amount of power at all,

**Dave Jones:** especially for the battery pack. So, these are clearly not charging the battery packs. But, if you saw our topology on the whiteboard, then that's what you'd expect. I expected a really big another big transformer in here just and and some big rectification and

**Dave Jones:** filtering and everything else. We've got We've got some filtering happening over here, but it's directly across the batteries rather than at the output of any rectifier. So, I don't see any power rectifier in here. These are obviously just little low-power

**Dave Jones:** isolation transformers to power all the circuitry underneath here. So, I mean, I can take out the fan there, but I don't think there's going to be anything doing there at all. So, I'm rather rather puzzled by that. They're

**Dave Jones:** obviously doing it some other some other way. No. No, they've just got some control stuff under there. No, there's nothing. So, it's This thing is clearly not uh working like our classic uh topology we had on the whiteboard up there. There it is.

**Dave Jones:** Ooh, there's a new perspective. Now, I've had a little head scratch over this rectifier thing, and some people are probably screaming at me right now saying, "Oh, yeah, it's obvious, Sandor." It is obvious when you think about what they're actually doing here,

**Dave Jones:** and it's rather clever, I think. Um this is my uh first thought of what they're doing, and it uh tips off why they've got a huge amount of capacitance in parallel with the battery here and no other I

**Dave Jones:** mean clearly there's no other uh you know a charger you know a power charger circuitry or uh rectifier. So, how are they doing it? Well, they must be doing it by tapping off the output of the transformer. So, the

**Dave Jones:** transformer is not actually uh switched here. They're actually they're always feeding power back through the transformer uh back in the other direction back into and using the H-bridge itself to actually uh charge the batteries. It's rather clever. This is the only way that they

**Dave Jones:** can be getting away with it cuz we need a huge amount of power to charge these huge battery packs. And the only power devices in here uh the H-bridge um devices themselves. Actually, I probably should have a look down here. I might be

**Dave Jones:** jumping the gun, but what I haven't shown here on my Dave CAD drawing, what I omitted because I thought it didn't matter, is the substrate diode across each one of these. And there's going to be one of those uh substrate

**Dave Jones:** reverse bias diodes across each of these MOSFETs. I won't go into details of why, but all MOSFETs are going to have these substrate diodes in there. And when you have diodes like that in reverse bias, you can feed power back in from this

**Dave Jones:** transformer, and then you can actually have um huge amount, you know, large capacitance across here like this or across there and there. You got large amount of capacitance, and that's what we've got. We've got these huge three huge caps here, and I think they're

**Dave Jones:** feeding power back in from the transformer through the reverse bias substrate diodes, filtering that out and using that to charge the batteries. That is incredibly clever. I really like that. Now, you may or may not be able to

**Dave Jones:** see that, but what we've got is four international rectifier IRFB4710 power MOSFETs in there. They're 100 V 75 amp rated, 14 mΩ on resistance, and they're clearly paralleling four of those up, and there's room for another four in there. So, obviously the

**Dave Jones:** 3,300 W model would have fully populated power MOSFETs in there. So, they're getting away with four, and they're tapped into holes directly on the heat sink. Or, well, it's not really a heat sink. It's actually used as the main current

**Dave Jones:** carrier as well. Quite neat. And if you try and have a look down the heat sinks at the other ones, you can see that they're exactly the same. They'll be two with P-channel MOSFETs and two with matching N-channel MOSFETs, of course, and I

**Dave Jones:** don't see anything else down in there. There's no huge power diodes or anything like that sharing the heat sink. So, they're obviously there's just some caps down in there. You can see those things down there. And really, there's nothing

**Dave Jones:** left for me to conclude except for the fact that they must be doing exactly what I said there and using the substrate diodes on here reverse biased to then charge up Well, to then and then they rectify that.

**Dave Jones:** So, it's effectively rectifying the AC coming from the output. When you're plugging in the mains, it's coming back from the transformer, and they're just rectifying that and filtering that, and then charging the battery from that. There's probably some, you know, more

**Dave Jones:** smarts in there, of course, actually taking care of things, but that's the basic topology that they're using. And it's very clever. And if we get rid of that option slot, which literally is an option slot and that and that just plugs

**Dave Jones:** in that ribbon cable just plugs in there. It's non-populated in my unit, but you can get like I believe you can get like ethernet interfaces and various other management modules and things to plug into. And as you can see, it looks

**Dave Jones:** like we've got a socketed micro there. I'll maybe try and get a close-up of that. Looks like we've got a USB micro cable micro here. It's a dead giveaway. It's right next to the USB. We've got an RS-232

**Dave Jones:** you know, probably a Maxim serial driver in there. And that's about all she wrote. Not a huge amount of control, you know, we're obviously going to have some analog to digital converter stuff around here to measure your voltage coming from your the

**Dave Jones:** current transformer and also measuring the mains input and output voltages as well to try and track that power. And of course, the battery management charging capability as well. And for those who absolutely must know what the main processor is, I peeled off the sticker

**Dave Jones:** there. It's a Philips 87C51 classic. Now, I was curious about how that charging system worked. So, what do you do when you want to find out info on how something works? Well, look at what we have here on the back. US patent

**Dave Jones:** number 5,302,858. Let's look it up. And bingo, look what we have here. Sometimes you just get lucky. Now, at best I expected maybe to find a snippet of information on how the charger system worked in the patent application and

**Dave Jones:** but we haven't. Look what we found here. Method and apparatus for providing battery charging in a backup power system. It is exactly what and it turns out it's exactly what I thought was happening or pretty you know, pretty darn close to it. So, this

**Dave Jones:** is where I love Google patents. It pops up. You just type in Google and the patent number. Here's the patent number and it's got all the images and the full text of the patent and it's fantastic. I'll link this in, by the way, so that

**Dave Jones:** you can have a look to your heart's content. And here we go. We have some images popped up here and they've got some prior art here. What they're showing is that this is how a traditional UPS works with the what they

**Dave Jones:** call a static switch here, the exactly the switch we showed on the whiteboard there. Then we've got a a transformer rectifier configuration converts AC to DC. Then we've got a battery charger circuitry, a battery, an inverter, a H

**Dave Jones:** bridge, and then our output transformer powering the output. And that's the prior art, but what they've got this patent for, by the looks of it, I haven't read all the details of the patent and what everything does, but

**Dave Jones:** I've got the general overview of it. And look what we have here. It's the same as before. You got your AC input here. You've got your switch which goes through the output, but there's no charger that we had before. There's

**Dave Jones:** Look, there's no rectifier here and there's no charging circuitry. And that's exactly what we found when we opened this thing. It looked like there was no charging circuitry, effectively, and there was no rectified power rectifier in there and power charger.

**Dave Jones:** So, what they've got is the original inverter, the battery for driving the output, and what they're clearly doing is permanently connecting the output transformer instead of switching it between the input and this. It's permanently connected to the output and

**Dave Jones:** that back feeds power into the inverter here through those body diodes of that MOSFET and then are charging the battery here. And they've got a controller circuitry to power all that. They're obviously monitoring input and output currents and voltages and everything

**Dave Jones:** else, but that's basically working exactly like I said. And if we take a look at this figure here, they're actually showing some of the details. They're showing an ideal transformer here, but they're obviously showing uh you know, the winding inductance and

**Dave Jones:** uh stuff in there cuz that obviously has something to do with it. They're storing the energy in the winding inductances in there to actually back power the uh charging circuitry the battery. And look, they've drawn in the body diodes

**Dave Jones:** there, substrate diodes on the MOSFETs there. And that's exactly what they're doing. Now, they're showing the AC input here. And if you flick it over and we rotate it, oops. There we go. Then they What they're showing is that they are powering the uh

**Dave Jones:** well, they're taking the line uh output voltage um and then using the winding inductance to then supply power back through those diodes. They don't show any filter caps in here, of course. They're grossly uh simplifying this in the uh patent uh

**Dave Jones:** diagram. They're not going to show anything they don't need to. And but that back charges the battery. And it is very clever, as I figured. And look, they've got uh they're showing you know, various configurations here. And you'd have to

**Dave Jones:** look up the text and all the individual points are numbered, so you'd have to read the text in depth if you wanted to uh figure out how this works cuz this is how patent applications work. They obfuscate everything. They just, you

**Dave Jones:** know, rewrite it. They take a clear technical description from the engineer who designed this thing and uh they just That's what patent attorneys do. They just change it into gobbledygook. But it's all eventually there in the uh text. So, they're showing both

**Dave Jones:** uh positive and negative configurations of which MOSFETs turn on. And look, this is showing clearly this diode here is then back charging through there, etc., etc. So, looks like they've got a charging waveform here. Perhaps you'd have to read the associated text. And

**Dave Jones:** they've got some clearly some uh control circuitry here. Here's the battery. They've got some other Yeah, they've got a error amplifier here with a voltage reference control ADC all that sort of jazz. So, that's clearly the control if

**Dave Jones:** looks like they got some There we go. Energy build-up state. That would be in the winding inductance and they got the discharge state and energy build-up state again. And you can associate that with the text description of the system

**Dave Jones:** operation. And there's a full resistive discharge curves and all sorts of goodness in there. So, they're showing you exactly how it works. But, the detail is all down here in this descriptive text. And here it is in the

**Dave Jones:** summary of the invention here. The present invention eliminates the need for separate charger transformer and battery charger conveniently used in backup power systems by utilizing the main inverter to do the battery charging. Bingo. Eliminating the separate charger lowers cost, reduces

**Dave Jones:** complexity and weight of the system, and improves system reliability. Cuz as I said, I expected there to be a fairly hefty charging transformer in there plus associated power circuitry as well. But, this does away with it. Fantastic. The

**Dave Jones:** invention provides inherent power factor correction because without the need for any additional control circuitry, the inverter charger draws a sinusoidal non-distorted current from the power lines. Brilliant. Another side benefit of this. And here's a bit more detail. The present invention utilizes the

**Dave Jones:** primary and secondary leakage reactances of the main power transformer in cooperation with the switching devices for the H-bridge inverter. The Consequently, the battery pack will back bias diodes intrinsic anti-parallel diodes conduct connected across each of the switching devices in the inverter

**Dave Jones:** bridge. Brilliant. Does exactly what I thought. But, in the end, like when I you know, thought about it for 5 minutes, it was obvious due to the lack of various components that um you know this was exactly what they

**Dave Jones:** were doing. There was no other way to do it. And it also tells you the inverter may be operating in constant frequency inverter charge mode or a variable frequency mode as well, yielding a higher charge current. So, there's they

**Dave Jones:** can probably chop and choose under software control what method they want to use. Fantastic. And this patent isn't new either. It's dates back to 1991. It was granted in 1994 and it was done by a guy named Douglas C. Faults. Good

**Dave Jones:** on you, Doug. And he worked for a company called Best Power Technology. I have no idea who they are or how they're associated with APC. I haven't checked. But maybe they got acquired or maybe it's Doug's company. Who knows? Anyway,

**Dave Jones:** one smart cookie invented this and presumably nobody in the UPS business has been able to implement this I don't know what what you would call it you know reverse inverter battery charger technology or something like that. Nobody else has been able to implement

**Dave Jones:** it because they would presumably violate the APC patent on this thing. Or I'm sure there's people out there are using it and they don't care and you know they're in another country and well, it's you know, it's real difficult and expensive

**Dave Jones:** to sue them. But anyway, it's has the patent expired? I don't know. What is it? 20 or 25 years on a patent or something. But presumably APC have been the only ones that have been able to incorporate this novel

**Dave Jones:** this novel technology. I mean there could be you know prior art. Just because they grant the thing doesn't mean that it's you know enforceable and stuff like that. If you can find prior art to beat it, then you can easily

**Dave Jones:** well, not easily. Still cost you a buttload of money to win any patent infringement lawsuit. That's for sure. And that's the disadvantage of these patents. You think you're protecting your design and well, you not cuz here's all the details in depth of how it all

**Dave Jones:** works. So, it doesn't stop anyone copying it. It puts all the info out there so that anyone uh in the world can copy it. But, what it does do, the patent, is gives you a right to sue them

**Dave Jones:** very expensively if they do. So, there you go. I hope you enjoyed that look at a to well, a combined tutorial teardown Tuesday, I guess you could call it. Uh where I started with some uh theory. I thought, oh, you know,

**Dave Jones:** some basic theory on how these things operate. See how well a product when you take it apart matches the basic uh theory that you'd find in any uh textbook basic block diagram approach. And usually, you know, it does. But, in

**Dave Jones:** this case, it actually surprised us, and it's a good example of how and why I like taking things apart because you often find surprises like this. I hadn't heard of this technique before, but it seems obvious with the hindsight. Maybe

**Dave Jones:** this widely uh used in the industry, I'm not sure, but anyway, that was a rather interesting. I found something I didn't know. I'm going to have to read further about how this works, but it seems to be a very clever little technique, and I'm

**Dave Jones:** bet there's a lot of people out there that didn't know about this either. So, there you go. Some uh benefits to tearing stuff down and investigating things. I love it. And uh if you like the video, please give it a big thumbs

**Dave Jones:** up on YouTube. And if you want to discuss it, jump on over to the EEVblog forum. Catch you next time.
