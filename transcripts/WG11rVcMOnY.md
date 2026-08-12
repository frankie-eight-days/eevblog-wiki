---
video_id: WG11rVcMOnY
title: EEVblog 1377 - The Amazing UNPREDICTABILITY of Fuses!
url: https://www.youtube.com/watch?v=WG11rVcMOnY
source: youtube-asr
---

**Dave Jones:** Hi, just a quick video about multimeter fuses because somebody on the EVBlog forum raised this and it's not the first time and it is a legitimate question. Why on meters like the BM235 and BM786 here, 60 or 6,000 count meter or a

**Dave Jones:** 60,000 count meter, it's got a 600 milliamp range and it says it's fused but the supplied fuse in it is not actually a 600 milliamps. It's actually a 400 milliamps and I actually sell spare fuses for these meters and they're

**Dave Jones:** 400 milliamps. These are AST M brand fuses and I buy these in bulk and they're very popular. I also sell the bigger one for the 10 amp range and these are very nice fuses, the AST M ones. Anyway, yeah, these are only 400

**Dave Jones:** milliamp fuses and that's actually what's supplied and that's actually what Brymen recommend for these meters and this is not specific to Brymen and it's for other manufacturers as well. And you know, there it is, HV620 400 milliamps 1,000 volts AC/DC UL listed of course by

**Dave Jones:** the way. And by the way, 1,000 volts AC/DC, make sure if you're replacing the fuses on your multimeter, make sure you get the high 1,000 volt rated or at least you know, like 600 volt rated ones because if you get like the the real

**Dave Jones:** cheap ass no name meters, they will have like only 250 volt mains rated fuses in them and you don't want that. They can arc over and ruin your day. So yeah, make sure you get like proper high voltage rating

**Dave Jones:** fuses if you're going to replace them. Anyway, why do they have 400 milliamps in here if it's actually 600 milliamp range? So what happens if you actually put 600 milliamps through this meter? As you can see, I got 400 milliamps going

**Dave Jones:** through there at the moment and I've got one of these fuses hooked up and it's not blowing because the rating of a fuse, a 400 milliamp rating is not the rating that it actually trips at. That's actually the sustaining current rating.

**Dave Jones:** So, in theory, we can leave 400 milliamps through this indefinitely and it will not break. It's only when it goes over 400 milliamps, will it start to break. And here's where it gets a bit loosey-goosey. So, let's take a look at

**Dave Jones:** the data sheet for the ASTM fuse that we've got here, right? So, we've got the 400 milliamp job here, right? 1,000 V rated. And a 400 milliamps is actually going to have quite a large voltage drop. And I've done, you know, burden

**Dave Jones:** voltage videos about that. So, yeah, putting a large amount of current through these, you can really get large burden voltage drops. Anyway, they don't actually give you an actual trip current on here, but that is its rated current

**Dave Jones:** is its implied holding current. Now, there is a mysterious figure here called typical pre-arcing. And this is also known as the melting thermal energy. And it's given in amp squared or I squared T. So, it's a time unit. This is the thermal energy

**Dave Jones:** required in order to basically melt the fuse. And well, you can whack, you know, your 400 milliamps into that, but it's not really going to give you like the time taken to actually melt. That's not really what it's for. So, for practical

**Dave Jones:** purposes, it's more academic. For practical purposes, you really have to go to the characteristic curves. So, you get these time versus current curves. Any good fuse manufacturer will give you these. And you've got to look at the individual specific curve for the actual

**Dave Jones:** fuse you've got. Now, unfortunately, they don't have a curve for the specific 400 milliamp one. But of course, you know, here's the 500, here's the 315. Let's just split it down the middle. Well, let's look at 400. 400, if we take

**Dave Jones:** 400 up, 400 up, 400 up, 400 up, 400 up. Oh, at 400 it's going to be like it's practically off the scale. It's practically indefinite. I mean, it might blow eventually, especially if it is in a confined space and it's heating up for

**Dave Jones:** example. So, let's actually measure the temperature of this one cuz it is actually going to get fairly warm. So, I've actually had this running for I don't know 10-15 minutes now or something like that. 37° also my air

**Dave Jones:** con's off so there's no air flow. But, of course if you put one of these inside like a sealed fuse compartment inside a multimeter, then it's going to heat up more cuz it takes you know more effort for the heat to

**Dave Jones:** actually radiate out. But, then again the heat can actually go into it might also be lower because the heat can actually dissipate bloody thing. The heat can actually battery. The heat can actually dissipate of course through the metal fuse contacts and into the PCB

**Dave Jones:** traces and stuff like that. So, they inherently have a bit of heat sinking on them. But, anyway, you know, this might eventually blow but like according to the data sheet it's it's going to take a long time and there's going to be like

**Dave Jones:** manufacturing tolerances in the fuse as well, the fuse wire itself. And well, you know, these are just like typical curves. They're not like absolute guaranteed. Anyway, what do we expect to happen at 600 milliamps? So, if we extrapolate this up here, it's going to

**Dave Jones:** be somewhere between here and here and I put that I my mark one eyeball says it's around about there. So, we're looking at 100 seconds, 200 seconds, 300 seconds, somewhere between 300 and 400 seconds. It should probably blow at 600

**Dave Jones:** milliamps. So, you can like according to the data sheet, it actually does have a significant amount of time to actually measure. That's more than enough time to measure your uh the current your 600 your maximum 600 milliamps, but it's

**Dave Jones:** enough to protect the meter that it will eventually uh blow or certainly if it goes to an amp, it's going to blow a lot quicker. What do we get for an amp? Let's have a look. So, I've taken it up

**Dave Jones:** to an amp. Yeah, it could blow it's going to blow in a couple of seconds there. And that's what you want. And if you're going to get like an old overcurrent fault, you you know, you might get a couple of amps or something

**Dave Jones:** like that. And you can see how it gets, you know, pretty non-linear here at the higher end cuz it's all a bit yeah, it's all to do with the thermals and they blow. And it's it's really complicated stuff if you want to get into the

**Dave Jones:** physics of the real physics of how uh fuses blow. But bit non-linear, but like, you know, it's going to be blowing in like the upper at a couple of amps going to be blowing in like tens of milliseconds or something like that.

**Dave Jones:** Okay, so I'm going to increase this to 600 milliamps. We'll see how long with the stopwatch it takes to blow. There you go. 600 milliamps. As you can see, more than enough time to take your measurement and it's not blowing yet. Of

**Dave Jones:** course, it's had already had time to heat up from, you know, tens of minutes. 47°, you know, it's getting significantly hotter. So, oh no, she she blew. It was somewhere in 50 seconds there. Okay, so let's do that again. 600

**Dave Jones:** milliamps. And I'll get some data on a couple of these. So, what we had at like 50-odd seconds before, which is, you know, as I said, it's going to vary quite substantially. If it blew in a couple of seconds, I would be concerned,

**Dave Jones:** but it's not. It's There you go. I've got some heat sinking here from the leads, but it might have more if it's like on a PCB and there's big current tree you know, big clamps right around it. Thermal transfer is not very good.

**Dave Jones:** They're like little spikes on them. So, you might actually get them better results inside the meter. But as you can see, look, we're going for a minute 20 now. Oh, there we go. Minute 57. Let's do another one. There is really going to be

**Dave Jones:** like a large tolerance difference between these, I think, if we test the whole box. Now, of course, it's got to be said that this is this specific type of fuse. Another brand 400 milliamp, even if it's a thousand volts, all the specs seem the

**Dave Jones:** same, they might have substantially different characteristic curves than these ASTM brand ones. So, wait, there we go. 3 minutes 47, was it? This one's up to 53 and a half after a minute 46. This one is about to crack 60. Yep, at 2

**Dave Jones:** minutes 40. Well, this one's a champ. 63. Of course, we don't know what the internal temperature is because it's all embedded inside that the ceramic or the sand. Well, there we go. 3 minutes 22. At 63 degrees. We have our first

**Dave Jones:** 4-minute jobby. Look at this. Ha-ha, you little ripper. Really big tolerance range on these fuses, which is why, you know, you don't necessarily want to over-range, like over-rate them. It looks like they've chosen it right. Ah. Oh, you

**Dave Jones:** little beauty. It lasted three times longer than that first one we tested. That's incredible. And this is what you have to account for when you're designing fuses like this into a system, especially if it's, you know, critical. You don't

**Dave Jones:** don't want to oversize and don't want to undersize them for your task. It's, you know, and beware of our surge currents as well. By the way, I'm not turning this on 600 milliamp straight. I'm turning on 400 milliamps first and then

**Dave Jones:** ramping up to 600 so that, you know, any like power supply turn-on spikes don't the output capacitor or whatever doesn't dump some extra charge into it and make it, you know, surge blow or something like that. So, cuz these are quick-blow fuses. These

**Dave Jones:** aren't slow-blow jobbies. 77 degrees after 7 and a half minutes. Wow, this is crazy. This is going to last four times more than the first one we tested from exactly the same batch, like the same box. Check it out, 83°.

**Dave Jones:** So, I actually spoke to Brymen quite a few years ago now about cuz somebody asked this exact same question. So, I thought I'd get Brymen's opinion on it and they said yeah, like exactly this is that you know, it holds up for long enough but

**Dave Jones:** you don't want to oversize it. But then you can get potential temperature issues and that can damage other stuff in your meter or whatever. So, you don't you know you don't necessarily want these things to heat up too badly but you want to

**Dave Jones:** protect them. It's a trade but you want to protect your meter of course. So, you don't want to make it too high. So, it's a trade-off. So, there's a super fuse. Oh, yeah, yeah, Bernie Ernie Bernie Ernie Bernie don't touch these things.

**Dave Jones:** But that's that's a crazy yet 90°. Wow. Oh, there we go. It blew. I missed it. Walked away for a little bit, got our shortest one at 45 second. Okay, what I'm doing is measuring the voltage drop across there. As you can see, it is sort

**Dave Jones:** of ramping up, isn't it? I wonder if there's I don't think I've ever experimented with this. I wonder if there's like a really rapid ramp up right near the point of fire. You can really see what happens when

**Dave Jones:** these things really you know, heat it up because well, it's changing the resistance of the filament and it's just going upity up and up. So, there yeah, that's probably like an 80° or something now. More. Oh, and blow you bastard. By the way, I

**Dave Jones:** had a previous one that I didn't shoot. Um 45 seconds. Are we going to crack three volts? It's a massive drop. You really have to take all this into account when you're uh using your meter. Burn voltage can be a

**Dave Jones:** real bugger and changing your fuse from one brand to another can make a very large impact. And at high values like this, at really high temperatures, yeah, I mean, it will go to that maximum of you know, it'll it'll be able to

**Dave Jones:** measure your 600 milliamps, but at the huge cost of burden voltage. Wow, will this one crack the other one? I think we might have a new winner here. There's a huge difference in it's not like I'm adding, you know, really any

**Dave Jones:** extra major heat sinking there by adding those two extra clips on. This is why when you're measuring these sort of currents, you want to use your amps range instead of your milliamp range. You you know, sure you lose a digit,

**Dave Jones:** lose a digit of resolution, but well worth it. I want to get this video done and edit the thing. I came back to the lab. It's now it's now 20 past 9:00 p.m. Wish the meter had a feature when it

**Dave Jones:** would beep when it drops to zero. That'd be neat. Yes, 100 100 102 103°. Oh, we just lost a digit of resolution on our floor there. Wow, this is actually this is turning into a bit of a valuable

**Dave Jones:** lesson video here. Is that these things can get insanely hot and you know, hot enough to damage your product in some way, perhaps, damage surrounding components, or affect its performance, or whatever. We've gone from like the shortest one, 45 seconds,

**Dave Jones:** to 12 minutes. I I could be here all night. Who knows what the upper bound on this is? All it takes is for the wire to come out however they stretch the filament wires in the machine that extrudes them, or

**Dave Jones:** whatever, however it does it. I don't know how they actually manufacture that. That'd be a fascinating video, wouldn't it? Tour of a fuse factory. Um yeah, can't exactly travel at the moment, so it's not that we have any fuse factories

**Dave Jones:** here in Australia. 111, it just ain't stopping. So, you can imagine if you had that like inside a sealed case. I mean, I don't have my air con here, so there's really no air flow in here, but still we

**Dave Jones:** do have like it's just sitting there flapping around in the breeze, right? Well, it's flapping around in no breeze. It's a bit different to being cooped up in a uh little fuse compartment, sealed fuse compartment. Glad I I was almost going

**Dave Jones:** to stop my testing at five, after the 45-second one. I went, "Ah, yeah, do another couple." And I'm glad I did. Look at this, 14 minutes. I mean, what was the upper bound of that? 1,000 seconds. 1,000 / 60, um you know, that's

**Dave Jones:** 16.6 minutes. So, you know, that's like And that's just like eyeballing it and guesstimating that the characteristic curve is going to be in there somewhere, but you can see when you got huge vertical lines like this and not much

**Dave Jones:** differentiation. It's you know, the the more that these lines get vertical, the more they get vertical, the more uncertainty you have. That's how it works. If it's more slopey like that, then you're going to get a more a narrow

**Dave Jones:** a narrower band of uncertainty um for any given fuse, but they don't even give you uncertain characteristics. This is just like typical curve. So, they like they don't even give you any notes for it. They just say, "Here's the graph,

**Dave Jones:** you know, we've measured it." I don't know, did they take averages? They don't say. Like, so they don't really guarantee these things. So, I maybe see, you know, some other manufacturers might be different. You'd have to look at

**Dave Jones:** different uh data sheets and stuff. Got to got to remember, this graph you know, this axis, the Y axis is log axis. Um well, so is the X axis as well, but come on, give this video a thumbs-up just for

**Dave Jones:** my perseverance here. Perseverance, rover just landed, fantastic, did a video, I did a live stream of that. Come on, you got to give this video a thumbs-up just for me standing here waiting for a bloody fuse to blow.

**Dave Jones:** Ah, the glamorous life of engineering video blogging. 118. Why is the current dropping? I've got a constant current power supply. And unfortunately, I can't show you what power supply I'm using cuz it hasn't been released yet. It's up there. Hasn't

**Dave Jones:** been released yet. There it is. 22 minutes. I actually know why the current dropped though cuz it we've reached the compliance voltage of the power supply. I had it set to 6 V. 6.17 is the highest. So, yeah. Unfortunately, I chose a 6-V

**Dave Jones:** output power supply to do this test. Um I didn't even occur to me that we'd get to that sort of compliance voltage. That's just That's nuts. Um I might actually stop it because really the only I'd better not

**Dave Jones:** put paper on top of that. It'll burn. I've done that That's not the first time I've actually uh burnt paper from uh components. I've even put them in the report. I've even put the burnt piece of paper in the report to show the test

**Dave Jones:** report to show Anyway, long story. The only guaranteed spec they give you is up here in the uh vague electrical characteristics. And they just say, "Well, at one of its nominal current, I nominal, um it's it's going to last you

**Dave Jones:** know, it'll last at least 4 hours minimum. So, in theory, that 400 mA fuse can blow after 4 hours. But, then they only specify like 120 seconds absolute maximum 2.5 times the nominal current. And we're like nowhere near 2.5 times

**Dave Jones:** the nominal um current. So, yeah. Um take these curves with a grain of salt. I'm going to stop it and we'll um I'll change my uh supply and we'll try and ramp this thing up to uh say 700 mA. See

**Dave Jones:** if it blows. All right. So, I'm back to 400 mA. So, I've got a compliance voltage of uh 10 V this time. So, we're still at uh 3.6 V. Anyway, let's uh now ramp this up to Let's go 0.7,

**Dave Jones:** shall we? Let's try 700 mA. So, let's I'll reset that time. So, that lasted, you know, at least 30 minutes. Here we go. 0.7, go. And whoa, whoa, jeez. No, we're Oh, yeah. it yeah, it it blew. It blew

**Dave Jones:** straight away. It just couldn't handle it. So, yeah. So, you can see that like any gross overload will blow these things, you know, almost practically instantly. So, it'll save your meter, it'll save your circuit in a gross overload. And that's what fuses are

**Dave Jones:** designed to do. They're designed for gross overloads. They're not designed for like really, you know, discriminatory uh current. Like, you can't really design a product for a fuse to blow within a specific region. Cuz look at the slope of these curves. You're just

**Dave Jones:** not going to get that when you have a slope like that. You might get other brands of fuses where you might get a more controlled characteristic, uh so to speak, or a, you know, a softer, I don't know. What What What would be the word

**Dave Jones:** for that? For, you know, making the slope go, you know, near vertical and having a big tolerance, you know, maybe maybe a tighter tolerance, for example. Um something like that. You got a better word for that, leave it in the comments.

**Dave Jones:** I'm sure it's at the tip of my tongue if I actually thought about it. Anyway, uh yeah, you could, you know, different types, but then if the user goes and changes the fuse to whatever, like, that can totally um change your uh product

**Dave Jones:** and change the safety of your product. It can uh change the characteristics um based on burden voltage and other stuff. So, yeah, you really have to take this stuff into account. Anyway, that's fascinating. So, I've got one, you know,

**Dave Jones:** 30-plus minutes. So, there you go. We went from 45 seconds at the last one. The first one was around about that, wasn't it? And then we went up to 30-plus minutes. Massive tolerance in fuses like this. All right, what I've got here is a data

**Dave Jones:** sheet for a Seba brand. This is basically uh the identical fuse to the uh ASTM. So, uh once again, fast-blow fuse, 400 milliamps, 1,000 volts. Uh there's the actual uh part number there. Once again, UL uh uh, So,

**Dave Jones:** uh, the interesting thing is is that the characteristic curves are very different. I It only has one curve like this or that or that actually has two for different current ranges. One for 100 milliamps to 800 milliamps and one

**Dave Jones:** for 1 amp to 2 amps. Now, check this out. For 100 milliamps to 800 milliamps, they don't even give you a graph that extends down and this is, uh, times the nominal current times IN. So, they don't actually So, you have to multiply. So,

**Dave Jones:** this is, uh, So, this will be 400 milliamps. They don't give you any separate characteristic curves for all the different currents. It's the one curve for all of them. So, once again, like it it's totally different to the

**Dave Jones:** ASTM fuse, uh, which seems more comprehensive in terms of the characteristic curves. But, interestingly, look, it's the unfilled triangle there. It The curve stops at four times the nominal current. So, 4 4s, that's 1.6 amps. Beyond that, we we just don't

**Dave Jones:** know. I mean, you could, you know, kind of like say, "Oh, it's going to be a similar curve to that." But, they don't actually give you the data. So, we have no idea cuz we How's it be at 600

**Dave Jones:** milliamps? It'll be 1.5 * 400 milliamps. So, it'll be this. This is, uh, seconds, but we just don't know the value. So, anyway, I'm just going to whack this in and test it. See what we get. Okay, this

**Dave Jones:** is the Seba at 400 milliamps. There you go. Um, a little bit lower, uh, drop, but, you know, it's neither here nor there. up bit. So, let's choose 0.6. There we go. It's jumped up to 1.1. And let's see how long it takes. Okay,

**Dave Jones:** we're at 4 minutes now, only 1.2 volts drop, and we're looking at 65° there. So, it just goes to show that, uh, really in Well, in this particular case, um, if you were designing a product, these, uh, Seba fuses, they're

**Dave Jones:** less predictable. than I mean you don't even have the data. You don't even have the data. You don't know what this curve like you can assume the curve's going to do something, but at least the ASTM fuses had all the multiple

**Dave Jones:** characteristics. At least you could you know get a indication. You don't get that with the Ciba fuses. So really the ASTM fuses are like more tightly spec. They're better controlled. They're better to design in your product than the Ciba fuses in this particular

**Dave Jones:** case cuz we have no idea. This could like just last forever. And well, if that's what you want, then that's fine. But you know, if you're trying to protect your product or do whatever, the lack of data like this could be a real

**Dave Jones:** problem. You would have to like do your own testing and then continue to do testing to ensure that they haven't changed their manufacturing process etc. over time. Because you can't design this Ciba fuse into your product and then

**Dave Jones:** measure them and they're all fine. You know, you've done all your due diligence and everything's hunky-dory and then year or two later out in the field you know all your fuses start blowing or they don't start blowing or whatever.

**Dave Jones:** And you go back to them say, "Hey, what's changed? What are you doing?" And they'll go, "Oh, sorry. We don't provide any data below four times the nominal current. So if you did your own testing, well, that's on you. That ain't our problem." Okay,

**Dave Jones:** we're getting towards 20 minutes now. 1.2 volts drop and 65° there. Like yeah, this this sucker's just not going to blow. So I'll ramp it up to 700 milliamps. Okay, 700 milliamps go. Yeah, significantly higher, but yeah, it's going to take a longer much

**Dave Jones:** longer to blow than the uh ASTM did. This This could This could last minutes at 700 milliamps. So this is a 400 milliamp fuse. No wonder they were a bit coy with their curves over here because well, yeah, they just well,

**Dave Jones:** they don't want to tell you. No, I just don't think it's got the balls to do it. Not at 1.6 volts. So, I don't think the temperature's going to be high enough, but you know, they've all got this

**Dave Jones:** secret sauce, their metallurgical secret sauce and everything, but I yeah, no, should I take it 800? Yeah, why not? Okay, 0.8 amps, go. 2 volts drop. This is double its rated current. 400 milliamp fuse. Yeah, it's it's still

**Dave Jones:** only creeping up though. I I think it's going to last a significant amount of time. Double the current, it's a scandalous. And after a minute, we're probably going to crack 100° shortly. Okay, no, this is getting ridiculous. 5 minutes at twice the

**Dave Jones:** current. And if you attempt to extrapolate the curve here, you're probably going to come a gutser because look, this is 1 second here at basically two two times the normal current, which is what we're at. It should last that 1

**Dave Jones:** second, but uh nope. So, obviously, you know, something it's it's really ramping up when it gets past here. It's just going nuts. That's why they don't bother. And look how they actually reset this. I mean, what do you

**Dave Jones:** choose? If you're designing your product, let's say at four times nominal current in this particular case, 1.6 amps for a 400 milliamp fuse, which which data point do you choose? Do you choose this one or this one? But this is

**Dave Jones:** like Schrödinger's data. So, yeah, it's ridiculous, but anyway, you are down in like the, you know, the millisecond, you know, tens of milliseconds region. So, I guess it doesn't matter too much. Okay, so we have the data. Let's say

**Dave Jones:** three times here. Three times nominal current, 1.2 amps. You expect that to blow in like, well, a couple of hundred milliseconds here. This is 1 second. So, let's go. Let's give that a whirl. All right, here we go. I'm going to take it

**Dave Jones:** to 1.2 amps for a 400 milliamp fuse. Let's give it a go. I've currently I've just had it for like a minute. I've sort of like blown it let it cool down for a little bit at 400 milliamps. So, we're

**Dave Jones:** going to ramp it up right to 1.2. Here we go. Oh, an amp. Oh, what? Oh, that's right. Sorry. No, it blew. It blew. Sorry, doll. My power supply again. I Power supply was only capable of maximum of an amp. So, anyway, when you

**Dave Jones:** take it up to an amp, yeah, it blew within what sub 10 seconds there or something like that. So, okay. But, yeah, in any case, I think there's a a good reason why they're not giving you the data below like four times nominal.

**Dave Jones:** Bastards. And there are various standards for these fuses, by the way. There's an IEC standard, which is 6127-2, I believe, is the latest one. And also the UL 248 standard, which it looks like these fuses might actually go by. And of course, it's hard to get

**Dave Jones:** these standards, but I was able to get this page, which is a 6 by 32 quick acting low breaking capacity. It's not a high breaking high voltage capacity one. I don't know if that changes. Please leave it in the comments if you've

**Dave Jones:** actually got the standards and stuff. But, anyway, it does give you like a maximum voltage drops, maximum power dissipation, 1.6 watts and stuff like that for like, you know, nominal 400 milliamps. So, you know, take this with a grain of salt. But, it does actually

**Dave Jones:** give you down here. Look, it it actually doesn't give you anything actually below two times nominal current. It just says, "Look, at two times nominal current, a maximum for 100 milliamps to a 10 amp fuse is 20 seconds." So, yeah, what

**Dave Jones:** happens at 1.5? Like, but then it does have like as part of the endurance testing down here, it says, "Oh, 1.15 times nominal current for an hour" and things like that. It must do must survive 100 cycles at 1.05

**Dave Jones:** times the rated current and stuff like that. So, yeah, you can actually heat these things up and cool them back down and there are endurance standards for these. So, yeah, but it just like complicates the whole thing, but it it certainly might

**Dave Jones:** explain why there's a difference between the Seba one and the ATSM one. They might be working to different standards and well, if you're serious about this sort of stuff, like you've got to take all this into consideration. I found something on

**Dave Jones:** the UL 248 standard anyway and there's all these different classes and things like that and of course, there's ambient like derating at temperatures. So, you know, if your product's being used from like zero to 40 or something like that,

**Dave Jones:** like that can like make a fairly big difference in the rating capacity, the effect on the blowing time, the effect on the carrying current and stuff like that. So, yeah, it's all it's all up in the air. Hold on to your hat. I just found this

**Dave Jones:** from Littlefuse, the importance of fuse low overload performance. A low overload is like a low grade fever. It doesn't cause immediate death, but indicates that something is wrong. It can cause localized overheating, weaken the spring clips or damage the plating on the fuse

**Dave Jones:** holders and increase their contact resistance. It can melt the solder on the surface mount fuses, can melt plastic housings and make fuses impossible to remove. Yeah, all are valid design points you've got to consider. Anyway, they say currents

**Dave Jones:** between 110 and 135% of fuse ratings present a severe challenge to the designer because they can subject parts to high heat for extended periods of time and because fuse behavior at these currents can be difficult to predict. The fuse does not blow before damage

**Dave Jones:** occurs, there can be claims under warranty, etc., etc. Fuses behave in predictable ways when subjected to substantial overloads or short circuits, but low overloads exist in a less predictable realm. For example, 110% of rating of a mini automotive fuse will

**Dave Jones:** open somewhere between 100 hours and never. At 135% of rating, the fuse opening time is between 0.75 seconds and 10 minutes. Yeah, that's the kind of variability we've seen here. Published curves are available from the fuse manufacturer. However, typically they

**Dave Jones:** apply to overloads in excess of 150%, hence why the Ciba fuse while Ciba they're they're just saying anything over anything under four times bugger it. And they show average characteristics. As I said, it's you know, they're not guaranteed. They only

**Dave Jones:** show averages. In fact, low value overloads are not generally considered part of fuse specification at all. Good luck. Another source of difficulty is that different technical standards for fuses describe different behaviors at low overloads. For example, with one

**Dave Jones:** exception it's impossible it's impossible for a fuse to satisfy both the UL CSA and the IEC rating standards. So, pick one. Calls for a fuse to operate continuously at 100% of its rating. A fuse made to the UL 248 and standard and operated at

**Dave Jones:** its rated current will eventually open. For this reason UL fuses are customarily operated well more than 75% their rated current. That's interesting. And look at all these different standards here. So, there's various standards and at the 600 milliamps we're looking at here or 150%

**Dave Jones:** of the rating, well, these are the SAE and the UL standards not even specified at all. This standard not specified like 60 minutes minimum for example. It's like it's all over the shop. But they say look there is a new 6127 IEC -4

**Dave Jones:** standard. Fuses must not open in less than 1 hour at 125% of the rated current and must open within 2 minutes at 200% of the rated current. So, it can still at twice the current it can still last 2

**Dave Jones:** minutes under this new IEC standard. Nuts. And here's a table for different little fuse they're different types and what the applicable standards are and the opening time at 135% for example. And look, it's just it's all over the Like, 0.75 seconds to 30

**Dave Jones:** minutes. Come on. So, basically, one of the top manufacturers little fuse here, they're using like all the Fluke meters and everything, and they're just saying throwing up their hands and just saying you know, it's complicated. It's like, you're pretty much on your own. And you

**Dave Jones:** know, leave it in the comments if you want me to do more detailed test, but I'll leave it for now um cuz I've got no shortage of these. I've got many many boxes. I sell these on the EV blog store and bulk buy them

**Dave Jones:** like a thousand at a time, so it's not a problem. If I wanted to a huge number of test, I'd have to automate this rig. There's no way I'd want to sit there. Maybe that's a It would that be a mini

**Dave Jones:** project anyone would want to see? Would be designing like a a little board that had like, you know, like 20 fuse holders on it or something. And 10 of you measure 10 at a time, you'd have like independent current generators for each

**Dave Jones:** one, and then you'd have like a timer for each one, and then you'd have like You could automate them. You would actually do that if you were a test engineer as I was donkeys years. Did test engineering, and

**Dave Jones:** they they're the sort of jigs that you would actually design for stuff like this for measuring production characteristics. Although, you know, if you want the full characteristics and stuff like that, that's more complicated. If you just wanted to like

**Dave Jones:** sample test fuses coming off the production line, you might actually have a jig, and they probably do have a jig, and they might, you know, just sample test a handful from each batch or something like that just to see that

**Dave Jones:** they're within the rather large tolerance that they actually have here. It's interesting cuz they sell like 315 milliamps, 400 milliamps, 500 milliamps. They don't even give you a curve for the 400 milliamp job, right? And the tolerance between like even the

**Dave Jones:** 315 milliamp and the half amp here, like you might find and half amp might blow quicker than a particular 315 mA just based on the tolerance and the massive slope of this line here. So, yeah, fuses. Fascinating business. Anyway, I think

**Dave Jones:** this video is probably fascinating enough to elevate to the main channel. So, if you like the video, please give it a big thumbs up. As always, comment down below. Do you work in a fuse factory? I'm sure somebody out there

**Dave Jones:** does. There's always a viewer out there that has worked in something or other that I mentioned. Doesn't matter how obscure it is. And uh leave it in the comments down below. So, I hope you found that fascinating. Yeah, fuses. Anyway, so to

**Dave Jones:** answer the question, like is a 400 mA fuse suitable for a meter like this? And Brymen is not the only one that I'm sort of like underrates their fuses like this. And there's probably good reasons why you would actually want to do that.

**Dave Jones:** And yeah, sure, you can measure up to your 600 mA, but it could uh blow depending on what type of fuse you've got. It'll eventually blow. Could blow in seconds, tens of seconds, minutes, tens of minutes. So, huge

**Dave Jones:** variability. Anyway, fascinating stuff. Catch you next time.
