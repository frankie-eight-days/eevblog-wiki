---
video_id: vfP_65gSSBU
title: EEVblog #678 - What is a PCB Spark Gap?
url: https://www.youtube.com/watch?v=vfP_65gSSBU
source: youtube-asr
---

**Dave Jones:** Hi, in a video not that long ago I tore down this medical devices grade plug pack. It's like a normal mains plug pack, but it was designed for medical applications and hence it had extra safety requirements and insulation

**Dave Jones:** requirements between primary, secondary and stuff like that to meet various medical safety standards. Anyway, one of my viewers, Azar, he's from Iraq actually. So, hi to all my Iraqi viewers. Fantastic. I do actually have a few. Now, he actually wanted to know what is

**Dave Jones:** this thing on the PCB down here and I called it a spark gap and that's exactly what it is. But, he wanted to know what is the function of these and why would you put it on a PCB? Well, let's take a

**Dave Jones:** quick look at it. Now, as you can see what it is is basically two bare traces like this. They just happen to be in a like a weird semicircle and then this sort of point arrangement like this is

**Dave Jones:** which is quite unusual. I haven't actually seen one exactly like this before, but anyone does them slightly differently, which we'll go into. Anyway, they all have something in common these spark gaps. They've got exposed metal traces like this. In this case,

**Dave Jones:** solder coated or they could be you know, whatever. But, anyway, they're exposed and the solder mask is exposed like that and there's a tiny gap between the two like that. And the reason it's called a spark gap is because they're designed to arc

**Dave Jones:** over. When you get a high voltage between this point here and this point down here, instead of destroying your components, the idea is that this arcs over and you get a spark across the smallest gap there. Now, there's many

**Dave Jones:** different ways to protect your product and circuit against ESD discharges into your product on an input pin for example or some sort of you know, overload pulse or lightning strike or whatever and this is just one of the techniques. In fact,

**Dave Jones:** this is one of the crudest uh techniques, but it has the advantage of being effectively free because you're already get making the PCB, so it doesn't cost you anything to add one of these spark gaps onto here. It just

**Dave Jones:** costs you a bit of board area on your uh PCB, that's all. So, if you've got the room to do it, this can be a cheap and simple, but you know, and reasonably effective uh way to protect your circuit

**Dave Jones:** and board against uh electrostatic discharge or uh high voltage overload lightning strikes, strikes, things like that. Now, of course, I'll say up front that this is not the best uh technique to do. It is basically a poor man's uh

**Dave Jones:** way to protect your inputs, and on its own, it's probably not that great. Uh and it's not recommended that you use just a spark gap on its own, but hey, it's better than having no input protection at all. Now, there are more

**Dave Jones:** professional ways to protect your input, of course, and sorry, this won't be a tutorial on how to protect your inputs. I'll have to do a separate video on that, but you can use things uh like gas discharge tubes, you can use uh MOVs,

**Dave Jones:** and uh TVS devices. Now, this gas chart discharge tube or GDT here is actually a spark gap. It's just a much more controlled way to do it than just your crappy little uh you know, PCB on here like this because uh this is quite

**Dave Jones:** uncontrolled. You don't really have much say in what the exact uh breakdown voltage will be and things like that. Whereas with a properly specified gas discharge tube like this, you will, you know, it'll be actually tightly controlled. It'll be tested and

**Dave Jones:** engineered properly, but it's essentially the same thing. What's inside there is a really well-controlled and well-engineered version of that. But, of course, gas discharge tubes and MOVs and uh TVS devices, they all cost money, whereas this costs you absolutely

**Dave Jones:** nothing. So, the way they work is incredibly simple. When you've got uh free air like this between two conductors, well, at a certain voltage, then it's going to arc over. You're going to get that spark, just like you

**Dave Jones:** get a static shock. You know, you walk across the carpet, you're rubbing your feet, you're building up a static charge, and you get near the doorknob, and you see that spark jump across. Well, that's because you can build up

**Dave Jones:** tens of thousands of volts static charge. And, well, you know, tens of thousands of volts is is, you know, quite a lot of voltage, and that will easily jump across a spark gap like this. Because you're so used to seeing,

**Dave Jones:** you know, quite long spark trails. So, when you get them really close like this, you can get reasonably low voltages. By reasonably low, I mean like 1,500 or 2,000 V. You pretty much can't get under that. And that pretty much is

**Dave Jones:** a minimum, you know, let's just do like a rule of thumb, like 2,000 V for example, might be a minimum that you do here, purely based on the fact that there's only so close that you can make these without uh risking them shorting

**Dave Jones:** out. So, you got to meet your PCB design rules, your clearance rules, and that's generally how you would design this thing. You would design it if you're designing an 8-thou board, for example, 8-thou clearance, uh that or, you know, 0.2 mm clearance,

**Dave Jones:** for example, then that's what you would set your minimum spark gap distance here. But, like I said, these are actually highly variable. That's why they're a poor man's uh spark gap. But, there is a somewhat of a formula that can uh help

**Dave Jones:** you estimate, but it's going to be very rough. And this formula is uh thrown around in the odd place. Uh they would have derived this from uh experiment. So, you know, it's not hugely theoretical, but it's based on the

**Dave Jones:** atmospheric pressure, because it's going to change. So, in low-pressure atmospheres, i.e., when you climb up the top of a mountain, for example, you can have that lower pressure, and let's say you've got half the pressure, then that figure is multiplied by half. So, you're

**Dave Jones:** actually going to have a lower uh breakdown voltage at those higher atmospheres. So, that's actually reasonably advantageous for things like these spark gaps, but when you're actually designing laying out boards, I've mentioned this before, when you actually want a keep a minimum, you

**Dave Jones:** know, clearance between here, it's really going to matter at what pressure you have to keep a larger distance here at a higher altitude. Anyway, the basic formula, rough formula here is the breakdown voltage is equal to 3,000 times the pressure in atmosphere.

**Dave Jones:** Usually, you just take this as one. So, you know, like at sea level, you got one atmosphere of pressure, and then the distance in millimeters plus 1350 here, and that works out to well, if you got like an 8 thou

**Dave Jones:** spacing, for example, which is around 0.2 mm, then you're going to get around about 2 kV, 2,000 V breakdown, and if you're sort of like the lowest geometry like 4 thou, you can go down to on a regular board, you know, it's going to

**Dave Jones:** be at least 1,500 V, but hey, these things can vary. It's going to depend with uh it's going to depend upon the exact uh geometry, etching, you know, over-etching, things like that, contamination of the board, whether or not it's already arced over before, and

**Dave Jones:** uh you know, whether or not anything's carbonized. So, anyway, enough of that. Let's actually put a high voltage across this, see if we can get it to spark. Okay, so what I've got here is my uh Uni-T UT513, a 5 kV

**Dave Jones:** mega uh insulation tester. So, it'll allow us to go It'll only allow us us to do basically 1,000 uh 2,500 or 5,000 V, but hey, this will let us spark it over, and it's got a reasonable amount of

**Dave Jones:** energy behind it as well, so it should hopefully continue to spark, not just, you know, like a static uh discharge, for example, when you build up on yourself. Yeah, it can get, you know, 20 kilovolts or something like that, but

**Dave Jones:** hey, it's all over red rover once you discharge it. But this thing should hopefully can continue to spark this thing over. Okay, here we go. I've uh got it set to 500 volts. So, we'll start out low and we shouldn't get any arc

**Dave Jones:** over at all. Yes, I have uh scraped away some of the uh tracks there just so it doesn't uh run off and uh discharge somewhere else. So, hopefully, here we go. Let's test 500 volts. Nope, nothing. All right. And here we go. This is 1,000

**Dave Jones:** volts. Nope. Nothing at all. Didn't expect it to because as I said, pretty much minimum, but it depends on contamination and uh all sorts of stuff, but generally, it's going to be, you know, like 2 kilovolts or something.

**Dave Jones:** Now, here we go. Here is where I expect it to possibly arc over, although it hey, it may not. There is a lot of tolerance. I don't know what the gap is down in there. Looks quite large, so

**Dave Jones:** wouldn't surprise me if this doesn't arc over, but it might. So, here we go. This is 2,500 volts.

**Dave Jones:** Hey, look at that. We got it. And it shut actually, it shut off. There you go. Yeah, so the uh insulation tester just uh shut down there, so it must have uh been overcurrent and it shut down to

**Dave Jones:** protect. Anyway, let's try Let's go higher. Let's ramp it up to 5 kilovolts. Here we go. Here's our maximum. It did last for like a second or two before though, but let's give this a whirl.

**Dave Jones:** Oh, yeah. Look at that. And it's switched off. Now, you can see the carbonization of that trace. Look, you can see got some carbonization down in there between that point and that point. And that is the problem with hey, no pun

**Dave Jones:** intended, uh points like this. When you have very sharp points, it, you know, it can often be a one-shot deal like this, especially for high energy, reasonably high energy device devices like this uh insulation resistance tester, if it arcs

**Dave Jones:** over like that and does it for a couple of seconds, then you can get some carbonization and then, well, you know, your board could be pretty much toast. So, yeah, it they could actually short out. So, you've got to be careful.

**Dave Jones:** So, in theory, sharp points are the way to go because as you saw, you know, the spark will come to that sharp point, but in practice, it's not that great because it can lead to little carbonized tracks like we just saw here. That's

**Dave Jones:** neat. Now, that's got a little bit of carbon there. Let's go back and test 1,000 V again. It It'll probably be okay, but I just want to test it out of curiosity. No, there we go. But, let's try 2.5 kV again.

**Dave Jones:** Yeah. Haha, love it. But, things like ESD, electrostatic discharge, they're not going to be huge amounts of energy like this. So, they're just going to like spark over once and boom, that's it. It It absorbs all the energy out of it. And

**Dave Jones:** that's the whole idea of these things is to take out the energy before it reaches your circuit. So, generally, this isn't the best example here, but generally, these would be right near your input connector, for example, going down to

**Dave Jones:** ground. And I'll show you that in a minute. And then, you'd have the trace leading off to your chip over here because you want the energy to be dissipated right at your input connector where the impulse actually happens. You

**Dave Jones:** don't want to like put it after your chip because then, by the time it gets to your chip, you're going to blow your chip. And here's another example here. I've just got another mains power supply I pulled from another teardown and yeah,

**Dave Jones:** it has one of these jaw type ones over here. Now, this one's not particularly good practice cuz once again, it uses the sharp points like this even though it uses multiple ones like this. There's no solder mask removed in there at all.

**Dave Jones:** They haven't actually taken it out. And that's you know, not good practice. You're supposed to take the solder mask out and certainly you don't want to cover the whole thing in solder mask cuz this doesn't work. It relies upon the

**Dave Jones:** fact that there's free air on actually between the two traces. And when you cover the things with solder mask, that's why you know, this gap here even if this trace came to within close to here, it wouldn't spark

**Dave Jones:** across here. It'd spark across here first because it's an air gap and not and because the solder mask on here actually provides really good insulation between the two. So in this particular case, that was actually between I've taken out the transformer. It was

**Dave Jones:** between the primary and the secondary of the transformer here. Anyway, let's spark this one over. Okay, let's go 500 volts. And as usual, you don't expect anything even though it looks pretty crusty in there. And a thousand volts.

**Dave Jones:** No, it's still holding in there. And here we go, 2500 volts. Wow, look at that center one. And this isn't switching off the meter. So it's just continually going. Look at that. So it's just going to burn a trace in there. It's just going

**Dave Jones:** to burn the board and leave a horrible carbonized trace behind there. That's fantastic. Look at that. Let's go to Oh, there we go. There we go. It burnt. Here you go. It actually fried that sharp point and then bingo,

**Dave Jones:** the next one took over. So this was the idea but I Yeah, there we go. Now it's doing a dance and the meter just switched off. Brilliant. But yeah, look what's left behind. See, there you go. You can really see the carbonized ends

**Dave Jones:** of that thing. As I don't know if it's left a trail there on the board itself but yeah, yep. Those three as functional as they once were. And we didn't get around to testing 5 kilovolts. Here we go.

**Dave Jones:** Yeah. All right. So, how do you do this when you're actually laying out a board? Well, there's every as I've said, everyone has their own way of doing it and there's pros and cons and you could argue until the cows come home about

**Dave Jones:** this. But anyway, I showed you just a couple of simple methods. And now what we've got here on the right-hand side is our IO connector that we want to protect, for example, from ESD and we've got our chip over here. Now, we don't

**Dave Jones:** want to put our spark gap over here on the chip. You want it to be over here on the connector, as close to the connector as possible so that so that energy is absorbed at the connector before it has

**Dave Jones:** a chance to propagate along here and go into your chip. And yes, we're not going to have any extra input protection for the chip. We're just going absolute tight-ass poor man's spark gap. So, what we can do is on the uh layer here, we

**Dave Jones:** can place a whoop, wrong layer. Here we go. So, we can what we can do is we can go in here and we can place a fill. You'll see this reasonably often and then we go to our which which of course will be our

**Dave Jones:** ground. You would set that to your ground net and then we can go to our top solder mask and we can place a corresponding a fill over here so that our solder mask is removed on these points here and it

**Dave Jones:** might not look obvious at the moment, but if we go into 3D view, bingo, I've removed the top silk screen and this is what you get. There you go. So, we've got you can see that uh out here's our pad here and we've

**Dave Jones:** effectively created a little spark gap in there. So, we've got this exposed. It's shown as gold here. That's our copper or your gold plate or your tin plate or or it is. So, we've removed our solder mask around there and we've

**Dave Jones:** created that little gap in there. So, if this is like an 8 8 board for example, really quite crude but a typical one you might have then you would set your minimum design spacing in there to 8 thou or 8 mil. So,

**Dave Jones:** not to be when a mil I say 1/1000 of an inch it equals a thou it doesn't equal millimeters. I'm talking imperial here. Or, you know, if you talk metric you're laying out your boards in metric it could be 0.2

**Dave Jones:** millimeters for example would be a spacing in there. So, there you go you've created that little spark gap across there but you know, it that's probably not the best solution but you'll see see this actually quite common in various products. You've seen them

**Dave Jones:** probably in a couple of tear downs I've done where they've just removed the solder mask. It's just easy and lazy way to do it from a layout point of view but hey, crude but effective. All right, so let me show you a slightly better method

**Dave Jones:** to just to avoid that point source that we got before with the pad in there and you know, it it just wasn't as as controlled as you'd generally like. So, what what I've done here is I've extended a track out from

**Dave Jones:** each one of these equal length like that. So, every pin that you want to protect and then we're going to place a polygon pour. Okay, so this would be connected to your ground net but I don't have all the you

**Dave Jones:** know, an actual project set up with nets but that's what you connect it to your ground. So, we'd go in here and then we'd create our polygon. You can do this as part of your like you just your usual

**Dave Jones:** ground fill on on your board but here we go and we've already set up our design rules for 8 thou. So, it automatically creates the spacing around that trace with 8 thou. Now, of course if we go over to our 3D view the solder mask is

**Dave Jones:** there and it's not going to work, okay? That solder mask is going to insulate that completely. So, what we want to do, of course, is go to our top solder mask, and then we just want to place a solder

**Dave Jones:** mask fill on there. Don't go all the way to there. Let's just go, say, from there to there. Should do the trick. And if we go over to here, bingo! Look at this. We now have a very nice, completely rounded

**Dave Jones:** one like that. So, you know, really there's no um sharp point to sort of, you know, wear out and all that sort of stuff. So, it should be fairly evenly distributed, as we uh saw in the video before. It

**Dave Jones:** should just sort of like spark around in any sort of random location. So, that one is, you know, is pretty ideal. But, as I said, you can argue the pros and cons about this um until the cows come home. Everyone's got

**Dave Jones:** their own favorite method. Some people will say like a square-ended uh track in there is better, and well, that's okay, too. But, yeah, you know, something like this. That's just a couple of different methods to do that. Like I said before,

**Dave Jones:** the whole point of this is to basically uh clamp the energy, get it to spark over right at the input connector where that uh transient is going to happen. The last thing you want to do is for it

**Dave Jones:** to propagate along this trace and go into your IC pin. So, if you can clamp the energy right at your input pin, that is the place to do it. And of course, good design practice, as I said, you

**Dave Jones:** would generally uh put some extra protection on the um input pins. Although, the ICs generally, you know, fairly robust in terms of uh ESD these days. Not perfect, but, you know, um pretty darn good. So, often just adding

**Dave Jones:** a spark gap like this, uh not too bad at all. But, the best part about this is that it is free. It only costs you board space and a couple of minutes of your time at the layout stage, and bingo! You've got at least

**Dave Jones:** some form of uh crude spark gap protection for ESD or other surges. You know, yeah, it has limited use, but it's better than nothing. So, hey, why not add it to your next design? And there's many different ways to do it. Hey, pick

**Dave Jones:** your favorite flavor, but as long as you got something, you know, it's better than nothing at all. So, I hope you enjoyed that video and found it somewhat useful. If you want to discuss it, jump on over to the EEVblog forum, that's the

**Dave Jones:** place to do it, but hey, YouTube comments are cool, too. And if you like it, please give it a big thumbs up on YouTube cuz that helps a lot. Catch you next time. Oh, by the way, just a quick plug if I

**Dave Jones:** may. I'm now accepting donations via Patreon. So, there's a whole bunch of benefits to this over PayPal for those who are thinking about donating. You don't have to, of course. I'm happy just to have your viewership, but for those

**Dave Jones:** who have been asking, I had people ask, "Can I set up a Patreon?" So, I have done that and you can accept donations through there. So, you can donate to your favorite bloggers and stuff like that. There's a lot of people on there

**Dave Jones:** and it's really good. It just allows me to interact with my backers a bit better. It's much better than PayPal. It's more visible. Anyway, link down below if you want to do that. Thanks.
