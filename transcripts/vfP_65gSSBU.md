---
video_id: vfP_65gSSBU
title: EEVblog #678 - What is a PCB Spark Gap?
url: https://www.youtube.com/watch?v=vfP_65gSSBU
source: youtube-asr
timestamps: {"0": 0, "1": 20, "2": 38, "3": 48, "4": 62, "5": 81, "6": 97, "7": 112, "8": 124, "9": 146, "10": 155, "11": 171, "12": 185, "13": 203, "14": 213, "15": 227, "16": 237, "17": 250, "18": 262, "19": 272, "20": 292, "21": 309, "22": 322, "23": 335, "24": 344, "25": 369, "26": 397, "27": 410, "28": 426, "29": 438, "30": 460, "31": 471, "32": 484, "33": 506, "34": 514, "35": 524, "36": 535, "37": 548, "38": 561, "39": 587, "40": 608, "41": 617, "42": 632, "43": 643, "44": 653, "45": 661, "46": 670, "47": 685, "48": 699, "49": 715, "50": 728, "51": 743, "52": 759, "53": 772, "54": 781, "55": 792, "56": 804, "57": 826, "58": 837, "59": 854, "60": 872, "61": 883, "62": 905, "63": 917, "64": 925, "65": 936, "66": 956, "67": 968, "68": 977, "69": 992, "70": 1005, "71": 1013, "72": 1025, "73": 1037, "74": 1047, "75": 1055, "76": 1067, "77": 1077, "78": 1093, "79": 1110, "80": 1119, "81": 1131, "82": 1140, "83": 1152, "84": 1163, "85": 1173, "86": 1184, "87": 1195, "88": 1209, "89": 1219}
---

**Dave Jones:** Hi, in a video not that long ago I tore down this medical devices grade plug pack. It's like a normal mains plug pack, but it was designed for medical applications and hence it had extra safety requirements and insulation requirements between primary, secondary and stuff like that to meet various medical safety standards.

**Dave Jones:** Anyway, one of my viewers, Azar, he's from Iraq actually. So, hi to all my Iraqi viewers. Fantastic. I do actually have a few. Now, he actually wanted to know what is this thing on the PCB down here and I called it a spark gap and that's exactly what it is.

**Dave Jones:** But, he wanted to know what is the function of these and why would you put it on a PCB? Well, let's take a quick look at it. Now, as you can see what it is is basically two bare traces like this.

**Dave Jones:** They just happen to be in a like a weird semicircle and then this sort of point arrangement like this is which is quite unusual. I haven't actually seen one exactly like this before, but anyone does them slightly differently, which we'll go into.

**Dave Jones:** Anyway, they all have something in common these spark gaps. They've got exposed metal traces like this. In this case, solder coated or they could be you know, whatever. But, anyway, they're exposed and the solder mask is exposed like that and there's a tiny gap between the two like that.

**Dave Jones:** And the reason it's called a spark gap is because they're designed to arc over. When you get a high voltage between this point here and this point down here, instead of destroying your components, the idea is that this arcs over and you get a spark across the smallest gap there.

**Dave Jones:** Now, there's many different ways to protect your product and circuit against ESD discharges into your product on an input pin for example or some sort of you know, overload pulse or lightning strike or whatever and this is just one of the techniques.

**Dave Jones:** In fact, this is one of the crudest uh techniques, but it has the advantage of being effectively free because you're already get making the PCB, so it doesn't cost you anything to add one of these spark gaps onto here.

**Dave Jones:** It just costs you a bit of board area on your uh PCB, that's all. So, if you've got the room to do it, this can be a cheap and simple, but you know, and reasonably effective uh way to protect your circuit and board against uh electrostatic discharge or uh high voltage overload lightning strikes, strikes, things like that.

**Dave Jones:** Now, of course, I'll say up front that this is not the best uh technique to do. It is basically a poor man's uh way to protect your inputs, and on its own, it's probably not that great.

**Dave Jones:** Uh and it's not recommended that you use just a spark gap on its own, but hey, it's better than having no input protection at all. Now, there are more professional ways to protect your input, of course, and sorry, this won't be a tutorial on how to protect your inputs.

**Dave Jones:** I'll have to do a separate video on that, but you can use things uh like gas discharge tubes, you can use uh MOVs, and uh TVS devices. Now, this gas chart discharge tube or GDT here is actually a spark gap.

**Dave Jones:** It's just a much more controlled way to do it than just your crappy little uh you know, PCB on here like this because uh this is quite uncontrolled. You don't really have much say in what the exact uh breakdown voltage will be and things like that.

**Dave Jones:** Whereas with a properly specified gas discharge tube like this, you will, you know, it'll be actually tightly controlled. It'll be tested and engineered properly, but it's essentially the same thing.

**Dave Jones:** What's inside there is a really well-controlled and well-engineered version of that. But, of course, gas discharge tubes and MOVs and uh TVS devices, they all cost money, whereas this costs you absolutely nothing.

**Dave Jones:** So, the way they work is incredibly simple. When you've got uh free air like this between two conductors, well, at a certain voltage, then it's going to arc over.

**Dave Jones:** You're going to get that spark, just like you get a static shock. You know, you walk across the carpet, you're rubbing your feet, you're building up a static charge, and you get near the doorknob, and you see that spark jump across.

**Dave Jones:** Well, that's because you can build up tens of thousands of volts static charge. And, well, you know, tens of thousands of volts is is, you know, quite a lot of voltage, and that will easily jump across a spark gap like this.

**Dave Jones:** Because you're so used to seeing, you know, quite long spark trails. So, when you get them really close like this, you can get reasonably low voltages. By reasonably low, I mean like 1,500 or 2,000 V.

**Dave Jones:** You pretty much can't get under that. And that pretty much is a minimum, you know, let's just do like a rule of thumb, like 2,000 V for example, might be a minimum that you do here, purely based on the fact that there's only so close that you can make these without uh risking them shorting out.

**Dave Jones:** So, you got to meet your PCB design rules, your clearance rules, and that's generally how you would design this thing. You would design it if you're designing an 8-thou board, for example, 8-thou clearance, uh that or, you know, 0.2 mm clearance, for example, then that's what you would set your minimum spark gap distance here.

**Dave Jones:** But, like I said, these are actually highly variable. That's why they're a poor man's uh spark gap. But, there is a somewhat of a formula that can uh help you estimate, but it's going to be very rough.

**Dave Jones:** And this formula is uh thrown around in the odd place. Uh they would have derived this from uh experiment. So, you know, it's not hugely theoretical, but it's based on the atmospheric pressure, because it's going to change.

**Dave Jones:** So, in low-pressure atmospheres, i.e., when you climb up the top of a mountain, for example, you can have that lower pressure, and let's say you've got half the pressure, then that figure is multiplied by half.

**Dave Jones:** So, you're actually going to have a lower uh breakdown voltage at those higher atmospheres. So, that's actually reasonably advantageous for things like these spark gaps, but when you're actually designing laying out boards, I've mentioned this before, when you actually want a keep a minimum, you know, clearance between here, it's really going to matter at what pressure you have to keep a larger distance here at a higher altitude.

**Dave Jones:** Anyway, the basic formula, rough formula here is the breakdown voltage is equal to 3,000 times the pressure in atmosphere. Usually, you just take this as one. So, you know, like at sea level, you got one atmosphere of pressure, and then the distance in millimeters plus 1350 here, and that works out to well, if you got like an 8 thou spacing, for example, which is around 0.2 mm, then you're going to get around

**Dave Jones:** about 2 kV, 2,000 V breakdown, and if you're sort of like the lowest geometry like 4 thou, you can go down to on a regular board, you know, it's going to be at least 1,500 V, but hey, these things can vary.

**Dave Jones:** It's going to depend with uh it's going to depend upon the exact uh geometry, etching, you know, over-etching, things like that, contamination of the board, whether or not it's already arced over before, and uh you know, whether or not anything's carbonized.

**Dave Jones:** So, anyway, enough of that. Let's actually put a high voltage across this, see if we can get it to spark. Okay, so what I've got here is my uh Uni-T UT513, a 5 kV mega uh insulation tester.

**Dave Jones:** So, it'll allow us to go It'll only allow us us to do basically 1,000 uh 2,500 or 5,000 V, but hey, this will let us spark it over, and it's got a reasonable amount of energy behind it as well, so it should hopefully continue to spark, not just, you know, like a static uh discharge, for example, when you build up on yourself.

**Dave Jones:** Yeah, it can get, you know, 20 kilovolts or something like that, but hey, it's all over red rover once you discharge it. But this thing should hopefully can continue to spark this thing over.

**Dave Jones:** Okay, here we go. I've uh got it set to 500 volts. So, we'll start out low and we shouldn't get any arc over at all. Yes, I have uh scraped away some of the uh tracks there just so it doesn't uh run off and uh discharge somewhere else.

**Dave Jones:** So, hopefully, here we go. Let's test 500 volts. Nope, nothing. All right. And here we go. This is 1,000 volts. Nope. Nothing at all. Didn't expect it to because as I said, pretty much minimum, but it depends on contamination and uh all sorts of stuff, but generally, it's going to be, you know, like 2 kilovolts or something.

**Dave Jones:** Now, here we go. Here is where I expect it to possibly arc over, although it hey, it may not. There is a lot of tolerance. I don't know what the gap is down in there.

**Dave Jones:** Looks quite large, so wouldn't surprise me if this doesn't arc over, but it might. So, here we go. This is 2,500 volts. Hey, look at that. We got it.

**Dave Jones:** And it shut actually, it shut off. There you go. Yeah, so the uh insulation tester just uh shut down there, so it must have uh been overcurrent and it shut down to protect.

**Dave Jones:** Anyway, let's try Let's go higher. Let's ramp it up to 5 kilovolts. Here we go. Here's our maximum. It did last for like a second or two before though, but let's give this a whirl.

**Dave Jones:** Oh, yeah. Look at that. And it's switched off. Now, you can see the carbonization of that trace. Look, you can see got some carbonization down in there between that point and that point.

**Dave Jones:** And that is the problem with hey, no pun intended, uh points like this. When you have very sharp points, it, you know, it can often be a one-shot deal like this, especially for high energy, reasonably high energy device devices like this uh insulation resistance tester, if it arcs over like that and does it for a couple of seconds, then you can get some carbonization and then, well, you know,

**Dave Jones:** your board could be pretty much toast. So, yeah, it they could actually short out. So, you've got to be careful. So, in theory, sharp points are the way to go because as you saw, you know, the spark will come to that sharp point, but in practice, it's not that great because it can lead to little carbonized tracks like we just saw here.

**Dave Jones:** That's neat. Now, that's got a little bit of carbon there. Let's go back and test 1,000 V again. It It'll probably be okay, but I just want to test it out of curiosity.

**Dave Jones:** No, there we go. But, let's try 2.5 kV again. Yeah. Haha, love it. But, things like ESD, electrostatic discharge, they're not going to be huge amounts of energy like this.

**Dave Jones:** So, they're just going to like spark over once and boom, that's it. It It absorbs all the energy out of it. And that's the whole idea of these things is to take out the energy before it reaches your circuit.

**Dave Jones:** So, generally, this isn't the best example here, but generally, these would be right near your input connector, for example, going down to ground. And I'll show you that in a minute.

**Dave Jones:** And then, you'd have the trace leading off to your chip over here because you want the energy to be dissipated right at your input connector where the impulse actually happens.

**Dave Jones:** You don't want to like put it after your chip because then, by the time it gets to your chip, you're going to blow your chip. And here's another example here.

**Dave Jones:** I've just got another mains power supply I pulled from another teardown and yeah, it has one of these jaw type ones over here. Now, this one's not particularly good practice cuz once again, it uses the sharp points like this even though it uses multiple ones like this.

**Dave Jones:** There's no solder mask removed in there at all. They haven't actually taken it out. And that's you know, not good practice. You're supposed to take the solder mask out and certainly you don't want to cover the whole thing in solder mask cuz this doesn't work.

**Dave Jones:** It relies upon the fact that there's free air on actually between the two traces. And when you cover the things with solder mask, that's why you know, this gap here even if this trace came to within close to here, it wouldn't spark across here.

**Dave Jones:** It'd spark across here first because it's an air gap and not and because the solder mask on here actually provides really good insulation between the two. So in this particular case, that was actually between I've taken out the transformer.

**Dave Jones:** It was between the primary and the secondary of the transformer here. Anyway, let's spark this one over. Okay, let's go 500 volts. And as usual, you don't expect anything even though it looks pretty crusty in there.

**Dave Jones:** And a thousand volts. No, it's still holding in there. And here we go, 2500 volts. Wow, look at that center one. And this isn't switching off the meter. So it's just continually going.

**Dave Jones:** Look at that. So it's just going to burn a trace in there. It's just going to burn the board and leave a horrible carbonized trace behind there. That's fantastic.

**Dave Jones:** Look at that. Let's go to Oh, there we go. There we go. It burnt. Here you go. It actually fried that sharp point and then bingo, the next one took over.

**Dave Jones:** So this was the idea but I Yeah, there we go. Now it's doing a dance and the meter just switched off. Brilliant. But yeah, look what's left behind. See, there you go.

**Dave Jones:** You can really see the carbonized ends of that thing. As I don't know if it's left a trail there on the board itself but yeah, yep. Those three as functional as they once were.

**Dave Jones:** And we didn't get around to testing 5 kilovolts. Here we go. Yeah. All right. So, how do you do this when you're actually laying out a board? Well, there's every as I've said, everyone has their own way of doing it and there's pros and cons and you could argue until the cows come home about this.

**Dave Jones:** But anyway, I showed you just a couple of simple methods. And now what we've got here on the right-hand side is our IO connector that we want to protect, for example, from ESD and we've got our chip over here.

**Dave Jones:** Now, we don't want to put our spark gap over here on the chip. You want it to be over here on the connector, as close to the connector as possible so that so that energy is absorbed at the connector before it has a chance to propagate along here and go into your chip.

**Dave Jones:** And yes, we're not going to have any extra input protection for the chip. We're just going absolute tight-ass poor man's spark gap. So, what we can do is on the uh layer here, we can place a whoop, wrong layer.

**Dave Jones:** Here we go. So, we can what we can do is we can go in here and we can place a fill. You'll see this reasonably often and then we go to our which which of course will be our ground.

**Dave Jones:** You would set that to your ground net and then we can go to our top solder mask and we can place a corresponding a fill over here so that our solder mask is removed on these points here and it might not look obvious at the moment, but if we go into 3D view, bingo, I've removed the top silk screen and this is what you get.

**Dave Jones:** There you go. So, we've got you can see that uh out here's our pad here and we've effectively created a little spark gap in there. So, we've got this exposed.

**Dave Jones:** It's shown as gold here. That's our copper or your gold plate or your tin plate or or it is. So, we've removed our solder mask around there and we've created that little gap in there.

**Dave Jones:** So, if this is like an 8 8 board for example, really quite crude but a typical one you might have then you would set your minimum design spacing in there to 8 thou or 8 mil.

**Dave Jones:** So, not to be when a mil I say 1/1000 of an inch it equals a thou it doesn't equal millimeters. I'm talking imperial here. Or, you know, if you talk metric you're laying out your boards in metric it could be 0.2 millimeters for example would be a spacing in there.

**Dave Jones:** So, there you go you've created that little spark gap across there but you know, it that's probably not the best solution but you'll see see this actually quite common in various products.

**Dave Jones:** You've seen them probably in a couple of tear downs I've done where they've just removed the solder mask. It's just easy and lazy way to do it from a layout point of view but hey, crude but effective.

**Dave Jones:** All right, so let me show you a slightly better method to just to avoid that point source that we got before with the pad in there and you know, it it just wasn't as as controlled as you'd generally like.

**Dave Jones:** So, what what I've done here is I've extended a track out from each one of these equal length like that. So, every pin that you want to protect and then we're going to place a polygon pour.

**Dave Jones:** Okay, so this would be connected to your ground net but I don't have all the you know, an actual project set up with nets but that's what you connect it to your ground.

**Dave Jones:** So, we'd go in here and then we'd create our polygon. You can do this as part of your like you just your usual ground fill on on your board but here we go and we've already set up our design rules for 8 thou.

**Dave Jones:** So, it automatically creates the spacing around that trace with 8 thou. Now, of course if we go over to our 3D view the solder mask is there and it's not going to work, okay?

**Dave Jones:** That solder mask is going to insulate that completely. So, what we want to do, of course, is go to our top solder mask, and then we just want to place a solder mask fill on there.

**Dave Jones:** Don't go all the way to there. Let's just go, say, from there to there. Should do the trick. And if we go over to here, bingo! Look at this.

**Dave Jones:** We now have a very nice, completely rounded one like that. So, you know, really there's no um sharp point to sort of, you know, wear out and all that sort of stuff.

**Dave Jones:** So, it should be fairly evenly distributed, as we uh saw in the video before. It should just sort of like spark around in any sort of random location. So, that one is, you know, is pretty ideal.

**Dave Jones:** But, as I said, you can argue the pros and cons about this um until the cows come home. Everyone's got their own favorite method. Some people will say like a square-ended uh track in there is better, and well, that's okay, too.

**Dave Jones:** But, yeah, you know, something like this. That's just a couple of different methods to do that. Like I said before, the whole point of this is to basically uh clamp the energy, get it to spark over right at the input connector where that uh transient is going to happen.

**Dave Jones:** The last thing you want to do is for it to propagate along this trace and go into your IC pin. So, if you can clamp the energy right at your input pin, that is the place to do it.

**Dave Jones:** And of course, good design practice, as I said, you would generally uh put some extra protection on the um input pins. Although, the ICs generally, you know, fairly robust in terms of uh ESD these days.

**Dave Jones:** Not perfect, but, you know, um pretty darn good. So, often just adding a spark gap like this, uh not too bad at all. But, the best part about this is that it is free.

**Dave Jones:** It only costs you board space and a couple of minutes of your time at the layout stage, and bingo! You've got at least some form of uh crude spark gap protection for ESD or other surges.

**Dave Jones:** You know, yeah, it has limited use, but it's better than nothing. So, hey, why not add it to your next design? And there's many different ways to do it.

**Dave Jones:** Hey, pick your favorite flavor, but as long as you got something, you know, it's better than nothing at all. So, I hope you enjoyed that video and found it somewhat useful.

**Dave Jones:** If you want to discuss it, jump on over to the EEVblog forum, that's the place to do it, but hey, YouTube comments are cool, too. And if you like it, please give it a big thumbs up on YouTube cuz that helps a lot.

**Dave Jones:** Catch you next time. Oh, by the way, just a quick plug if I may. I'm now accepting donations via Patreon. So, there's a whole bunch of benefits to this over PayPal for those who are thinking about donating.

**Dave Jones:** You don't have to, of course. I'm happy just to have your viewership, but for those who have been asking, I had people ask, "Can I set up a Patreon?" So, I have done that and you can accept donations through there.

**Dave Jones:** So, you can donate to your favorite bloggers and stuff like that. There's a lot of people on there and it's really good. It just allows me to interact with my backers a bit better.

**Dave Jones:** It's much better than PayPal. It's more visible. Anyway, link down below if you want to do that. Thanks.
