---
video_id: _R4wQQNSO6k
title: EEVblog 1487 - Do Solar Micro Inverters Take Power at Night?
url: https://www.youtube.com/watch?v=_R4wQQNSO6k
source: youtube-asr
---

**Dave Jones:** Hi, a few people have asked me after I installed my new uh Enphase 5 kW solar system, which is this video down the bottom here. I've now got a total of an 8 kW nominal uh system. A new 5 kW

**Dave Jones:** Enphase system with 14 of these um funky little microinverters uh behind every one of my 14 new panels. That's a 5 kW system. And I've also got my existing 3 kW system, which I installed a long, long time ago, and I moved that to the

**Dave Jones:** other side of the roof over there, and it's not performing terrifically, but you know, it's paid for itself. I've done Yeah, there There it is, the 5-year solar payback video and everything else. So, that's the old system. It's uh paid

**Dave Jones:** for itself. But anyway, I quite I'll link these videos in if you haven't seen them. But anyway, quite a few people have asked many questions about these microinverter um systems. And one of them was, I did a whole video

**Dave Jones:** on this is uh why I'm using 295-W on a with a 370-W uh rated panel. And I've done a whole video on that, LinkedIn. Um and that's an interesting uh question. There's sort of like pros and cons uh both ways. But

**Dave Jones:** anyway, that uh explains that and all about solar shading and stuff. I've done lots of solar videos now. Anyway, quite a few people have asked um Do these microinverters, how much power do they actually draw at nighttime when

**Dave Jones:** they're switched off? And it's an interesting question. And it has to do with the way that these things are uh designed internally and also apparent power. So, we're going to get um into this. Now, this is a I originally did

**Dave Jones:** shoot a video on this, but it wasn't that clear. So, I'm simply I'm This is a new one. I'm re-recording it uh from scratch to make it clearer. Now, I've got a solar analytics uh system here. I've done a video uh installing that.

**Dave Jones:** It's very cool uh system, which monitors, as well as the Enphase uh system. I've done videos on showing all the data you can extract from that. It's one of the advantage of the microinverters here is that um yeah,

**Dave Jones:** it's like I've got the in phase in voice system which communicates over the mains wiring and we might discuss that later and yeah, it can get data out of these things and we can I can log individual panel data. It's really quite cool. But

**Dave Jones:** one thing this thing doesn't tell tell me which is what this solar analytics system is because I've got clamps of voltage it can measure the voltage course and I've got current clamps going over it can measure not only how much

**Dave Jones:** energy my solar system is producing during the day but also how much power it's drawing during the night. So we can see this and if I go into live it shows me this is what is drawing at the

**Dave Jones:** moment. So this is live. This is what's happening right now. But if I go into what what they call long energy I can actually look at both the power the current the reactive power the reactive energy and the

**Dave Jones:** apparent power and the power factor because when you measure the voltage and the when you measure and log the voltage and and current of a system then if you know, you can work out the phase of this and of course this is all in my AC

**Dave Jones:** basics tutorial series I talk about you know, capacitors and inductors leading and lagging lagging and how in an ideal capacitor which is what we'll get into there's no power dissipation in an ideal capacitor when you connect it across the

**Dave Jones:** mains for example and that will come in very important shortly. So this really won't be a like a proper tutorial on reactive energy and apparent power. I'm assuming that you've got the concepts but we'll we'll basically go over the

**Dave Jones:** pros and cons of the this reactive power. So anyway, we're able to measure this. So I'll go back to June 12th here and you can see this yellow curve here. It's a nice perfect day. Okay. So you know, there's no shading or anything

**Dave Jones:** like that and it's you know, it's so the sun starts at about uh 8:00 a.m. something like that. It jumps up, and then because of like shade in the afternoon from the house next door cuz it's wintertime here in Australia.

**Dave Jones:** Remember this for my 8 kW um system. Look at this, I'm only getting 3.8 kW out of it. Uh that's the downside of wintertime here, and my panels aren't on ideal roofs either, especially with my old 3 kW uh

**Dave Jones:** system. So, yeah. Anyway, so at around about uh yeah, 3:00 something like that, it starts to die off, die off, die off. But, the good thing is we can measure the power, the current, the reactive power, the reactive energy,

**Dave Jones:** the voltage, the mains voltage here. Um if if you want to know, I'm I'm at at home. You can go up to like I can get up to like Look at that, 248 V. It's normally like 245 V,

**Dave Jones:** something like that. I think it can get down to as low as 240. So, it varies between 240 V and like 248 V at absolute maximum. Um but, anyway, the apparent power is something that we can measure. Now, because I've actually got a current

**Dave Jones:** clamp logging the data um coming to and from my solar system, we can actually answer the question, how much power do these uh microinverters Remember, I've got 14 of them all in parallel uh microinverters. I also do have the old

**Dave Jones:** Sunny Boy inverter uh there as well, which is a 3000 TL Sunny Boy inverter. It's But, I've checked the data sheet for that, and it only has um 1 W uh real It specifies 1 W real standby power. I don't know what that is in

**Dave Jones:** apparent uh power, but we'll just like eliminate that cuz it's only one compared to 14 of my microinverters. Now, interestingly, Enphase do not tell you anywhere on the data sheet, anywhere in the website, and I've talked to them

**Dave Jones:** in this about it, and yeah, they do not mention the standby power. They mention the standby power of the Envoy system, which they say is 5 W. I think it is, but they don't say the VA for it, the

**Dave Jones:** apparent power. It's because we'll go into the architecture of this later on in the video. So, stick around and I'll show you exactly how it works inside, at least nominally from a block diagram point of view. This AC port backfeed

**Dave Jones:** current here, this is like a fault current thing. It has to do with fault conditions and stuff like that. We won't go into it, but that's not the standby power. So, we can't get any of this from the data

**Dave Jones:** sheet. So, we have to actually measure it. And of course, one of the things about the Enphase inverters is that they have active power factor correction. So, it's it will when it's on and generating, it'll be power factor of 1.0. And and it can

**Dave Jones:** actually correct adjustable from 0.5. You can actually adjust it, I believe, when you set it up or something. I don't know the install details and things like that. But, yeah, very cool. During the day, we don't know how much power these

**Dave Jones:** things take. But, it doesn't matter. I'll show you the architecture. It's actually powered from the DC side, not from the AC side. So, it you know, that's not the question. But, at nighttime here, look, the you can't see

**Dave Jones:** the yellow curve in there. And sorry, I can't zoom in on this. But, you can see the answer up the top here. You can see yellow minus 7.6 9.1. Let's say eight eight watts, something like that. Let's say eight

**Dave Jones:** watts. So, that's eight watts real power, not apparent power, real power, standby power for the Enphase for the 14 microinverters. But, that will also, as I said, that will also include the Sunny Boy 3000TL, which is 1 W

**Dave Jones:** real power. That's what it says in the data sheet. And the Enphase Envoy system, which is the monitoring box as well. Apparently, that's pun intended. I'm here all week. Apparently, that's also across the same wiring, as well. So, yeah. So, I think

**Dave Jones:** that one might be in there, as well. In post-editing Dave here, I just got some info from I have more at the end. Stick around. But, I just got a info from Enphase that the actual power consumption of the Enphase inverters is

**Dave Jones:** 15 microamps. This is like it's it's essentially zero. So, this is the real power consumption. This is the real measured power consumption. It's basically zero. So, all of this 8 W here um well, we know that 1 W is apparently

**Dave Jones:** coming from my Sunny Boy inverter, and I guess the others the Envoy system and the IQ relays, as well, on there. So, yeah. That's But, basically virtually zero of that is the Enphase microinverters. But, as you can see,

**Dave Jones:** they basically draws naff all at night real power, okay? But, that's not apparent power. So, this is the interesting bit. If you've got If we go over to the current over here, we'll see something very different. And this is

**Dave Jones:** where it becomes confusing and interesting. So, if we go over to current here, look, at night time 1.1 amps. Why are we getting 1.1 amps? Yes, there is actually 1.1 amps of current flowing at night into these Enphase microinverters.

**Dave Jones:** If you get your confuser out, 1.1 * 245 V, that's 270 W. Why isn't it showing 270 W over here? Right? Should be showing -270 W. That is it's, you know, standby power. No, this is because it is

**Dave Jones:** apparent power. It is reactive power. And if we go in here, like this, we'll see that it actually tells us the reactive power, which is VA volts * amps which are That's why it says VAR above there. Volts amps, reactive. The

**Dave Jones:** reactive power is the out of phase power calculated based on the current that's actually being drawn and the voltage. But, this is not real power. So, 280 VAR there, 280 VA. And if we go over to apparent power, it's going to be the

**Dave Jones:** same thing. There we go, minus 280 VA there. We don't have reactive anymore. Apparent power is reactive power plus real power. So, in this particular case, we can actually look at the power factor, and the power factor is

**Dave Jones:** absolutely terrible. Look at the yellow uh graph here, right? It's absolutely like it's it's rounded down to zero, okay? Because it's that low. I mean, on the graph it's like .03 or something like that. It's essentially zero, okay? There's measurement

**Dave Jones:** resolution on uh this thing. It's basically a power factor of zero. And we'll go into the architecture um shortly about how these Enphase microinverters actually uh work. Um but, it's basically an entire capacitive load. That's why uh we're getting a

**Dave Jones:** negative VA there. If it was an inductive load, like we're seeing the purple one here, the purple one is the fridges, okay? They're my fridges. I've got two fridges, basically, assuming just ignoring all the other phantom power devices in the house at night.

**Dave Jones:** This is mostly the fridges. So, you can see the actual compressors turning off and on, right? For the fridges. And it's yeah, it's drawing 530 VA, 640 VA, something like that. But, if you go into uh real power at night, if you're

**Dave Jones:** powering these from a battery pack, and what you're paying for is only 130, 200 W, something like that, right? So, my fridges and freezers um draw 240, 200 odd watts during the day. And I'm looking at getting, shortly, um like an

**Dave Jones:** independent uh battery backup solution just for the fridges. So, that could make for some interesting videos. So, stick around for that one. So, just to be very clear, residential customers, like myself and like practically everyone else, please, if there is an

**Dave Jones:** exception, leave it in the comments down below, but Enphase don't seem I've talked to Enphase about this. They don't seem to think that there's an exemption to this, which is why they don't mention at all on the data sheet or anything

**Dave Jones:** else. They they don't mention the apparent power because it's not something that the customer gets charged for. It's not something that they need to care about. It's, you know, it it isn't an issue at all, right? So, you

**Dave Jones:** don't get charged for that. I don't get charged for that. I I only get charged for that 8 W. That's all I'm getting charged for, okay? And if I had a battery system, technically, that's all that it would

**Dave Jones:** take overnight from the battery system as well. But, we'll get into that cuz that's an interesting story. But, yeah, you've got to know the difference between if you put a clamp meter on there, you will actually measure 1.1 amps, right? I will measure 1.1 amps

**Dave Jones:** for the 14 microinverters. And as I showed in the previous video, there's another forum, other people have confirmed this, and Enphase have confirmed this as well, and we'll go through the calculations. So, this is the confusing part. When you say

**Dave Jones:** apparent power or reactive power, okay? The word power is in there, okay? But, this is not real power. If you've got capacitance, like we have here, capacitance across the line, capacitors ideal capacitors do not draw any power at all, but they will cause the these

**Dave Jones:** currents to flow, right? They will cause quite large currents to flow. So, you get I squared R copper losses and any converter efficiency switching losses as well. So, we'll go into that in a diagram in a minute of how all this uh

**Dave Jones:** works. But, yeah, um so, don't confuse apparent power, right, which which is a calculation of 280 VA, don't confuse that with the actual real power that you're being charged for and that will be taken from a grid-connected battery system. Yeah,

**Dave Jones:** so, this is uh really cool. You can see here, right, that um at at nighttime, when the microinverters are switched off cuz there's no sunlight hitting the panels at all, all the circuitry is switched off, all you've got is the

**Dave Jones:** filter capacitors on the output, and that's what we're seeing here is the filter capacitors on the output. I'll show you the exact values in a minute. But, and then, as soon as sunlight starts to hit, it turns on the active

**Dave Jones:** electronics in the Enphase microinverter, and boom, it switches from negative reactive apparent power to positive like power, and now it's generating. Right, so, now you don't care about it. It it's not an issue at all. So, yeah, and then it starts

**Dave Jones:** generating power, and at night, you can see there's still some sun, still some sun, still some sun, and even though it's not really generating much if, you know, hardly any real power uh from the panels, and then boop, it switches off,

**Dave Jones:** and we start drawing capacitive power because the inverters the microinverters are switched off, these things are switched off, but they still have large capacitors on the output, which are connected across the mains, which causes this apparent power flow. So, anyway, I

**Dave Jones:** hope that's that's answered uh the question uh many people have asked, "How much What is the standby power of these microinverters, and does it make a difference?" Well, the answer is um what you're paying for, not nothing. But,

**Dave Jones:** it is interesting to note that they do draw 280 VA because of the capacitors on the output. This is isn't just an Enphase thing. You almost certainly get this with any other microinverter or any other inverter um on the market. If

**Dave Jones:** they're switched off, they've still got filter capacitors on the output, so unless you actually disconnect them using a relay, then uh um the capacitor's going to be across the mains, but hey, that's a good thing. Now, it's a good thing in two ways

**Dave Jones:** because you'll notice that my fridge the purple one here, this is the consumed graph, these are my fridges and freezers turning off and on, right? This is the reactive energy or we can go over to the reactive uh power here, right? They're

**Dave Jones:** they're going to the graphs going to look the same, power and energy is going to look exactly the same, just the numbers are different. And you'll notice that the yellow one, which is the capacitors inside the microinverters, are one direction and the purple ones in

**Dave Jones:** the other direction because these those fridges and freezers are primarily inductive loads, so the So, in this case, having a whole lot of these microinverters on here can actually be beneficial locally to your system if you've got inductive loads like fridges

**Dave Jones:** and freezers in this because it can cancel it out and that's why we're not drawing much real uh power here, right? The real the real power that we're actually uh consuming at night is, you know, is is not much. So, um yeah, so

**Dave Jones:** they having capacitors across the mains, it's effectively doing some power factor correction against an inductive load. If you don't have those inductive loads, well, you're not going to get uh the benefit there. But guess what you get with every inverter that you put on your

**Dave Jones:** system at night time, you get a free energy saver. Yes, these these ridiculous energy saver scams, which I've done videos on, these are a capacitor in a box, right? And there's all marketing wank behind these. They're a capacitor in a box. Um and I've done

**Dave Jones:** videos busting these. Here it is, here's one of the ones. There it is, there's the capacitor. Can't remember what value it is. You know, it might even be a couple of mic, right? That they put across the mains and they

**Dave Jones:** they think this is going to save you energy. So, I've got And there's a digital version of these. And yeah, these are just It's just a capacitor in a box, okay? So, we've got the same thing going on here.

**Dave Jones:** These have capacitors in the output. So, let's have a look at the block diagram and see how this is all kind of working. All right, so let's have a look at what's going on here. I don't know the

**Dave Jones:** exact circuit inside the Enphase microinverter, but this has been confirmed by Enphase that the output filter capacitors are three 330 nF capacitors. So, they're in here like this. And by the way, these microinverters are all potted, so I

**Dave Jones:** can't like do a teardown of one. And then of course, it's going to have some switching like a switching transformery type thing in it. And the interesting thing is that all the active circuitry is actually powered from the DC side

**Dave Jones:** coming from the panel. So, when at nighttime, when the light vanishes, there's no more power for the internal circuitry. So, all you're left with is essentially the filter capacitors here. I'm not going to like do all the switching components and

**Dave Jones:** stuff like that. Doesn't matter, you know, it's it's down in the drags. We know the power factor is very close to zero, okay? Which means that it's almost entirely capacitive. So, you can see that over here, right? That that yellow

**Dave Jones:** line for the power factor, it's bordering on zero. And when that's bordering on zero, then yeah, it's going to be in in this particular case, it's going to be entirely capacitive. So, that's what we've got. We've got almost a nanofarad

**Dave Jones:** of capacitance there. Now, of course, we have 14 of these microinverters all in parallel. So, that's actually quite a significant amount of capacitance that's always connected across your mains here, okay? But as I said, this may be beneficial if you've got lots of

**Dave Jones:** inductive loads. It's kind of like a power factor like correction thing. So, it can actually be beneficial. But so, let's see what these capacitors actually do. Okay, the the capacitive reactance here XC is 1 over 2 pi FC. I've done

**Dave Jones:** this in my AC basics tutorial video. So, it's 1 over 2 pi 50 hertz here in Australia, not that 60 hertz rubbish, times 990 nanofarads cuz we've got three in parallel. That gives us reactants of 3,215 ohms. Okay, and then because we've got

**Dave Jones:** 14 of those in parallel, that's what that symbol there, a parallel symbol. 14 of those, it's actually 229 ohms is the capacitive reactance for all of these microinverters all in parallel here. And of course, this will actually, you have to charge

**Dave Jones:** up because it's AC. Remember this, it's cycling one way, the other. These capacitors every cycle are charging, discharging. And capacitors, they this is real current that actually flows. So, if we get 245 volts, which is my nominal voltage divided by 229 ohms,

**Dave Jones:** what a coincidence. There you go, 1.07 amps. Let's round it to 1.1. What did we measure? Yep, 1.1 amps. There you go, there's the yellow current there. So, that's exactly where it comes from. It comes from the capacitive output filter

**Dave Jones:** of the microinverters. This is nothing specific to the Enphase. Any microinverter or any other inverter, as I said, the Sunny Boy inverters will have this and any inverter will have an AC output filter like this. So, unless you physically

**Dave Jones:** a relay in here to disconnect it, and we'll talk about this in a minute, at night time, yeah, you're going to have all those capacitors across the mains and it will actually draw a current. And that's why my

**Dave Jones:** current clamp in here is actually measuring a real, when when I say real, okay, this is not an imaginary current. Okay, apparent power and reactive power, these are called imaginary powers, right? Then cuz they're it's an imaginary it's on the imaginary plane.

**Dave Jones:** You have to see my AC Basics series to understand all this. But the current is real. The current If you put a clamp meter or a you know, a multimeter, a clamp meter, you will actually measure 1.1 amps RMS in there actually flowing

**Dave Jones:** into into the microinverters at night. Because these capacitors because the cycle's changing, these capacitors must be charged and discharged every cycle. So this 1.1 amps is real. So there is a potential downside to having, you know, a ton of these microinverters in a

**Dave Jones:** series like this. You will get copper losses, okay? And so I squared R copper losses in there, right? And there's resistance in the wiring. It's very small. In fact, we can go in and we can actually calculate the copper losses are

**Dave Jones:** very small, but you will actually dissipate real power in the copper losses in here. But as we explained before, this is not real power, okay? So it's not real power dissipated. It's just reactive power. It's just currents flowing back and forth. There's no

**Dave Jones:** energy transfer from the grid to these inverters over here. But this is a real current, right? So it's got to flow. But it has to do with other loads you have on the system, power factor correction, all that sort of stuff. But

**Dave Jones:** you are only charged for real power. So we're only charged for that 7 watts. We're not charged for the 280 the apparent power that we're actually drawing due to the capacitance and the lagging current caused by these capacitors. But yes, at nighttime, the

**Dave Jones:** only losses in theory that you will have and you will pay for is the copper losses in all of this copper running over here and the connections and stuff like that. There is no power, no real power at all dissipated in these

**Dave Jones:** capacitors here. So if you went out and got a thermal imaging camera and put it on those microinverters at night, in theory, you wouldn't even though it's 280 VA apparent power, um you will see no power dissipation in this microinverter.

**Dave Jones:** Um you will see like in theory, it's nothing. If these capacitors are ideal, there's no other losses, power factor's perfectly zero, um then yeah, you will see no losses um heat generation in this at all. You will, in theory, see a

**Dave Jones:** little bit of heating of the wires here due to the I squared R copper losses in there though. This is post-editing Dave here because I just got a response from uh Enphase with more detail about how the microinverter works. And it's

**Dave Jones:** actually rather clever. Um this is actually a bidirectional system. Um I I was originally uh told that the that the Enphase electronics was powered from the DC panel, right? It's powered from the DC side, so it only gets

**Dave Jones:** powered up when the solar panel uh starts producing power. And that's true the first time that you power it up. It's got to get that initial power, but once it's done that, okay, then it's actually during the day it's powered

**Dave Jones:** from this. But at nighttime, it's actually able to take the AC back out of here, okay? And actually do uh some processing like end of day processing if there's any firmware updates at the end of the day. Apparently, that's when it

**Dave Jones:** uh does it as well. But even though the sun's gone down on your panel here, um it could is completely bidirectional. It can get uh power from your mains because this is a grid-connected uh main system or your battery if it's a, you know,

**Dave Jones:** independent battery connected uh system, then it would it it gets the power like that. And then during the night, it's actually still able to operate. And this is uh it's completely programmable. And what they can do as part of the advanced

**Dave Jones:** functionality in this thing is actually uh generate uh reactive currents to actually help the grid depending on what the authorities want. They can actually program the micro inverters to actually actively power factor control the grid. But in a lot of cases they just go no

**Dave Jones:** way we're just happy with the capacity. You don't need to do anything. But they actually have the capability at night to actively power factor correction and they can even keep one inverter powered up. The rest of them power down and then

**Dave Jones:** that one inverter can compensate for the other inverters, but that's obviously not what's happening here cuz I'm getting 1.1 amps. It's not I don't think it's able to actually compensate for that cuz you got 300 and you know

**Dave Jones:** you got all this capacitance to compensate for it's not that great. It can actually do active power line compensation which is pretty impressive. Other micro inverters might have this capability as well. So leave it or other inverters doesn't have to like there's

**Dave Jones:** no real difference between a micro inverter and a regular inverter. It's just that you have an inverter per panel really. But there's other functionality differences that you might get as well. But essentially it's just an inverter. So it can actually do bi-directional

**Dave Jones:** power transfer and this is why if we go over here and have a look at their end phases own battery system coming late 2022. Can't buy I thought you could buy it already but I don't know maybe delays. There's a lithium shortage or

**Dave Jones:** something isn't there? Anyway, if you go down here you can see how these are the regular micro inverters the same ones I've got. They just plug in to here because you can actually get power direction both ways. They can charge the

**Dave Jones:** batteries and they can get energy back out. It's bi-directional power transfer. And of course that's how other batteries battery inverters will operate as well. You've got it they're bi-directional power transfer but I didn't know that or I kind of maybe I didn't I'd

**Dave Jones:** forgotten but they're bi-directional because that's just the way that they've designed them. You don't need this bi-directional capability for a microinverter that goes in the panel. You could have just had it going in the one direction, but they've tried but

**Dave Jones:** they've thought ahead and gone, "Aha, no, if we make it bi-directional, we can do lots of cool stuff in the future, advanced grid control, power factor, re-reactive power correction, and all sorts of stuff, and then put them on our

**Dave Jones:** batteries and reuse the same inverter." So, that's pretty cool. And we also got a figure for this standby power consumption. 15 microamps is the real measured by them 15 microamps. So, it's naffle. 15 microamps * 245 V, yeah, that's only 3.6

**Dave Jones:** mW. Yeah, it's you might as well round that down to zero. In fact, all the all of the microinverters combined, even if I had 50 of these things, it's going to be less than my Sunny Boy inverter at

**Dave Jones:** 1 W real power. So, yeah, the answer to that question is the standby the real standby power is zero, but the reactive current is still there because of the capacitance. So, unless you physically disconnect them, you've still got the

**Dave Jones:** capacitance there. So, this isn't a big deal. You can have as many microinverters here as you like, and well, you can argue about, "Okay, where the actual current is delivered from?" And usually, it's kind of like sort of locally. So,

**Dave Jones:** it doesn't come from like the the the generator over here. It doesn't come from the coal-fired or wind-fired or nuclear power plant over here, right? It doesn't come all the way in here. But but the utility the company that owns the grid, they have to

**Dave Jones:** account for all this sort of stuff, right? Apparent power is a big deal. That's why big industrial customers with huge heavy equipment and stuff like that, they might get charged for their apparent power. So, that's a complicated thing. For for residential

**Dave Jones:** customers, they don't get charged for it. But the the utilities will have to install like big capacitor banks like on here and stuff like that. So, you could argue, "Oh, yeah, you're doing them some good by having these microinverters

**Dave Jones:** here, but it's a complex system argument which we won't go into, okay?" So, the apparent power is not delivered, right? It's not delivered right back from the generator over here, but it's delivered from somewhere. So, at at nighttime, if

**Dave Jones:** your system is grid-connected, okay? Like this, Enphase uh sort of confirmed this, and they say it's going to come from the grid over here, and I tend to agree. So, it's really the grid that's going to provide that current over here.

**Dave Jones:** So, it's not If you've got a home battery storage system, it's not going to come from your battery here. This battery at night is only going to be delivering the real power, i.e. that 7 or 8 W that we uh saw. I think it's

**Dave Jones:** still going to come from the grid over here. Leave it in the comments down below if you don't agree with that, but once again, it's a complex system thing. But, the interesting thing is if we disconnect from the grid, if you've got

**Dave Jones:** a grid-independent system, this 1.8 1 amps, this is real current. It needs to be delivered from somewhere. And in this case, it has to be delivered from your battery, right? There's no saving you from the grid, right? Cuz you're

**Dave Jones:** disconnected from the grid, okay? But, it is not real power being delivered. So, it's not 280 W that is coming out of this battery. It's only going to be the real power, which is that 8 W or thereabouts um or in theory nothing,

**Dave Jones:** right? If these are all ideal capacitors. You can put as much capacitance on this line as as you want, right? It's not going to dissipate any energy. There's no energy transfer from the battery or the grid for that matter

**Dave Jones:** to these capacitors. Cuz these capacitors, if they're ideal, they don't dissipate any power at all. But, the current must flow to charge and discharge them every every cycle, and that must ultimately come from your battery here. So, where you will see

**Dave Jones:** losses, actual real power losses that must be delivered from the kilowatt-hour capacity of your battery here is is switching losses in your inverter. You've got to generate that 1.1 amps. So, you will get switching losses in this uh inverter. So, you know, your

**Dave Jones:** inverter might be, I don't know, 95 97% efficient. Although, if the characteristic graph of your converter is like this, I might see if I can find one, all right? At high if if if this is power level, right? And this is

**Dave Jones:** percentage efficiency, okay? It you know, it might be designed for a sweet spot over here when it's delivering high amounts of power, it it could be very efficient. You know, it might be like 95% efficient like right up here, but

**Dave Jones:** where you know, at lower powers, it might, you know, I don't know, might be 70% efficient. Who knows? But anyway, you will have some real power loss due to the efficiency of your inverter over here that has to deliver that current.

**Dave Jones:** Even though there's no transfer energy transfer into the capacitors, you've got the I squared R losses in the cables, all in here, and you've got a little bit, you know, a few percent, 5% could be more, 10% um loss in your inverters

**Dave Jones:** here. So, you so you don't get that for free. So, if you've got a grid disconnected, a grid independent battery storage system, and you're using microinverters like this, it might be beneficial for you to put a relay in

**Dave Jones:** here at night and disconnect it. But, as I said, most people have a grid connected system. So, it's actually connected through to the grid, in which case you don't have to worry about this. It's a nothing burger. Um in fact, it

**Dave Jones:** could be beneficial, as I said, cuz if you got inductive loads, it can sort of you know, the capacitance can help cancel out. And here we go, I just found um this uh randomly uh from Penn State Department of Energy Mineral uh the

**Dave Jones:** efficiency of uh inverters like these solar uh inverter things. There you go. Uh that's the graph that I showed you. There's like a peak efficiency here, you know? They claim like the data sheet will show, "Oh, yeah, our solar inverter

**Dave Jones:** is 98% efficient." Yeah. Yeah, it'll have a peak efficiency there. So, at night time, if you're only uh have to supply the current, remember, not not power, not real power, but the current, um you know, the current's got to come

**Dave Jones:** from your inverter. It's got to come from your battery. So, you know, your your efficiency is going at low power levels is going to drop uh significantly. So, you know, you'll pay a bit of a penalty for that. And if

**Dave Jones:** you've got a huge system with, you know, a ton of micro inverters, you know, it it could start to add up. So, I'm just, you know, just be aware that uh that could be the case. But, that's really the only

**Dave Jones:** downside if you have a grid disconnected system, a totally isolated independent battery storage system, then yeah, um the currents have to flow. So, there you go. I hope you found that um interesting. And yeah, this is why um

**Dave Jones:** you know, there's a lot of people out there, a lot of people that install their solar system, they'll put a clamp meter on there at night time, and they'll measure, "Oh, it's drawing amps." You know, and yeah, it is

**Dave Jones:** actually yeah, there's real current flowing in these wires. So, yeah, just be aware of that. Um oh, I squared R copper losses, how much? Let's quantify it. We've got annealed copper at 20° C. We're doing it per meter, okay? We've

**Dave Jones:** got a cross-sectional area 1.5 sq mm. I do believe that's the uh size of the radial, it's uh called. Uh it's called a radial because it it it's not looped, it radiates out from your junction box like that. And so, yeah, it's only 11 mΩ per

**Dave Jones:** meter. But, of course, you have to double that. So, it'll Let's say about 22 mΩ, you know, 220 mΩ, something like that over a 10-m run. So, the losses are I squared R. So, I 1 amp, um you square

**Dave Jones:** that, it's still 1, conveniently. Um it times the uh resistance, which is 220 mΩ, 0.22. So, you're talking about 220 odd mW real power loss for a 10-m run at 1 amp. So, you know, it's it's not a

**Dave Jones:** lot, but, you know, once again, you've got the kid connections in there as well and I wouldn't be at all concerned with the I squared R losses in here, but technically they are there. Just be aware of that. But I think you'd

**Dave Jones:** probably get larger losses in your battery inverter system at low efficiency levels when it's trying to you know generate this current and that's ultimately going to come from your battery, but only if you disconnected from the grid. If you're

**Dave Jones:** connected to the grid and you've got your home battery storage solution, don't worry about it. I don't think the 1.1 amps is coming from your battery. If you think otherwise, then leave it in the comments. As I said, I

**Dave Jones:** think it's going to be coming from the grid, but it also depends on the load that you've got connected over here and is it an inductive load and stuff like that. If it is, it's beneficial. Blah blah blah. There you go. It's it's

**Dave Jones:** rather an interesting question. What is the power draw of these things at night? And this is why Enphase don't bother to tell you on the data sheet of the website. It's just going to confuse you. Oh, by the way, relay So some people

**Dave Jones:** ask, "Why don't we just disconnect it here with a relay at night?" Why not? Because on my system I do actually have Well, I've got two of these. Oh, look. Look, they do actually tell you the power consumption here. Look at that, 10

**Dave Jones:** VA. That's interesting. I I didn't see that before. They they tell you. Um they they don't tell you it's apparent power either. They just say 10 VA. So anyway, I've got two of these things and my real power consumption is only 8

**Dave Jones:** watts total. So yeah, it's it's going to be naff all, but it's an interesting that they tell you that on the VA and they don't tell you the VA on the micro inverters. So anyway, anyway. Um yeah, so I actually have two of these things

**Dave Jones:** installed, which is apparently a legislative requirement here in Australia to meet the Australian standards for solar installs, you must have one of these intelligent relays installed, which can automatically this does some automatic fancy fancy stuff inside so that, you know, during fault conditions,

**Dave Jones:** over voltage, under voltage, and other, it will automatically disconnect your solar array because, you know, the the utilities don't want cuz we got a huge we got the largest solar uptake in the world home solar uptake in the world

**Dave Jones:** here. I think it's now 35% of homes or something in Australia have solar on their roof. So, it's a big deal and it's a big deal for the grid. Can be beneficial and also can have downsides for the grid. So, during peak times um

**Dave Jones:** they don't want everyone's solar pumping stuff on here. So, if the voltage rises, this is the mechanism that they use. They can actually sort of like force people's solar arrays to turn off, but I've never had I never had any

**Dave Jones:** indication of mine ever been turned off, but it this is an automatic relay that actually does that. But, this is technically this is also under software control. I I can actually see this. I can see I can see the serial number of

**Dave Jones:** this and that it's physically connected in my Enphase Enlighten system. See, here's my Enphase system. You can see at the top I've got two IQ relays installed in there. So, these are actually software controlled and these are in

**Dave Jones:** series with with the actual panels. Okay? So, here's the DC isolator boxes here and then there's two of these relays actually disconnecting cuz there's two separate circuits here cuz I've got 14. I think if I had like 10 or 12 or something, I don't need the

**Dave Jones:** one relay and one DC isolator, but, you know, it's a larger system, so they had to install the two isolators and the two relays. I can physically see those devices in there. And they but I can't do anything with

**Dave Jones:** them. Okay? There's There's the IQ relays down there. You know, they're operating normally retire replace. I I can't even get the Can I get the data on that? Anyway, Enphase give you data out the way the wazoo. It's absolutely amazing, but um

**Dave Jones:** yeah, there's all my individual microinverters, but I can't like in theory they could actually have a manual thing in here or an automatic timer base system to actually disconnect these. They did say it requires 300 seconds or something for the whole system to power

**Dave Jones:** back up. So, if you did disconnect it at night, you would leave the the Enphase system running, which is the box, the separate box that does all this login, that does all this stuff. This is the Enphase gateway doing all this.

**Dave Jones:** So, yeah, so in theory, they they could actually software control all these relays. But, I was just talking to Enphase and they said, "Not real like we don't want people around with that sort of stuff, really, you know? It's just going to

**Dave Jones:** like if you give them the tools they'll hang themselves kind of thing, you know? Then they'll get support requests from people saying, "Oh, no, you know, my solar system's turned off. Why?" I don't know, you were around with the

**Dave Jones:** setting, I you know, and stuff like that. So, they they they want to make it sort of like bulletproof. So, yeah, I guess I can't blame them. But, technically, that's I think that's in theory possible to actually disconnect that. It's all

**Dave Jones:** fascinating. So, thank you for the people who have asked how much power do these microinverters take at night? The answer is, well, naff all, really, unless you've got an independent storage battery solution which is disconnected from the grid, and then maybe you might

**Dave Jones:** have to think about yeah, these currents because these reactive currents can flow. You can't stop them. So, the currents are not imaginary, but the power is. Hmm. Catch you next time.
