---
video_id: ME4Xe53TMxI
title: EEVblog #732 - PCB Sheet Resistance
url: https://www.youtube.com/watch?v=ME4Xe53TMxI
source: youtube-asr
timestamps: {"0": 1, "1": 22, "2": 37, "3": 50, "4": 71, "5": 83, "6": 103, "7": 120, "8": 138, "9": 152, "10": 166, "11": 181, "12": 200, "13": 218, "14": 226, "15": 239, "16": 256, "17": 270, "18": 284, "19": 292, "20": 306, "21": 314, "22": 336, "23": 349, "24": 365, "25": 377, "26": 397, "27": 419, "28": 430, "29": 441, "30": 457, "31": 483, "32": 506, "33": 521, "34": 541, "35": 559, "36": 574, "37": 592, "38": 612, "39": 622, "40": 636, "41": 649, "42": 665, "43": 674, "44": 691, "45": 703, "46": 714, "47": 733, "48": 744, "49": 754, "50": 769, "51": 778, "52": 787, "53": 802, "54": 811, "55": 823, "56": 835, "57": 845, "58": 860, "59": 889, "60": 901, "61": 907, "62": 925, "63": 934, "64": 945, "65": 956, "66": 965, "67": 979, "68": 990, "69": 1002, "70": 1018, "71": 1041, "72": 1055, "73": 1069, "74": 1079, "75": 1091}
---

**Dave Jones:** Hi, welcome to Fundamentals Friday. What if I told you that this piece of 1 oz copper clad board was exactly the same end-to-end resistance as this piece here? Or I could go one further and say that this monster sheet of copper clad, once again 1 oz, is green because it's got a positive pre-photoresist coated on it.

**Dave Jones:** But what if I said that's exactly the same resistance as this tiny little piece of exactly the same 1 oz copper? You'd call me crazy, right? But no, not really.

**Dave Jones:** Hang around and I'll explain what I'm talking about, why this is true, and I'll demonstrate it. Now this topic comes up because of a previous video I did on precision thin film resistor networks, which I'll link in down below if you haven't seen it.

**Dave Jones:** I sort of made the throwaway comment in that video that one piece of resistive material, be it copper or nichrome or anything else, which I'll explain, is exactly the same resistance, I it might be 1 mΩ for example, as a much larger piece if they're both squares like this.

**Dave Jones:** And this confused a lot of people. So what they do with these precision thin film resistor networks, they've got a ceramic base and they might coat them with say a nichrome material which has a relatively high resistance per area.

**Dave Jones:** It might be 100 Ω per square for example, and this is how they create them. They put the a film of the material on there and then they might laser cut like that certain areas out to increase the resistance and trim it to the exact resistance that you require.

**Dave Jones:** And this is actually the same method that they use to make your thin film 0805, you know, 0603 resistors, the SMD resistors that you're familiar with. And exactly the same property regardless of whether or not it's nichrome or whether it's just a regular copper clad PCB.

**Dave Jones:** It's exactly the same in that no matter how big the square of copper or nichrome is, it's going to be exactly the same resistance regardless of the size. So, this brings up a really interesting property called sheet resistance, and its units are ohms per square.

**Dave Jones:** Not ohms per square meter or ohms per square centimeter or other area. There is no area units on it. It's just ohms per square. And copper clad PCB will have a figure for ohms per square.

**Dave Jones:** Your nichrome will have a figure for ohms per square. And pretty much any material which has a uniform thickness like this. Be it copper clad or whether or not it's a 3D solid body, it can also have that.

**Dave Jones:** So, it's just as long as you've got a uniform thickness on the material, you can talk in terms of sheet resistance. So, if we take a look at a piece of resistive material, in this case copper clad, which we'll work with, then of course, we have a length, a width, and a thickness.

**Dave Jones:** It's 1 oz copper, about 35 microns or thereabouts, universal thickness. Now, the resistance of this piece of copper or whatever material it is, is the resistivity, which is That's not a P, it's the symbol rho, and that's the material resistivity.

**Dave Jones:** Each Each material will have its own resistivity figure. And we'll take a look at that. And then it's multiplied by the length divided by the area. Now, of course, the area is so, length on width times thickness.

**Dave Jones:** That's the area. Now, if we take that formula and we just rearrange it a little bit, it's still exactly the same, just to make it a little bit clearer.

**Dave Jones:** You'll see why in a second. So, it's rho on thickness times the length on the width. And you'll notice this here, because now it's now a separate term. What if the length and the width are the same?

**Dave Jones:** I.e. a square that we were talking about here. Well, that becomes one. So, it's multiplied by one. So, all we're left with in the case of a square, the resistance is only determined by row on the thickness.

**Dave Jones:** It's got nothing to do with how big this square is. Doesn't matter if it's that big or if it's that big like that. It's still one. The only thing that matters is the thickness.

**Dave Jones:** And it's not just a square, either. If you had a small rectangle like that, which was say like two squares joined, and you had another one there, which was exactly the same, it's the same thing.

**Dave Jones:** It's just a different ratio there. Instead of being one, it's something else. So, no matter how big the rectangle is, the resistance is going to stay exactly the same.

**Dave Jones:** But, I know what you're thinking. Dave, that doesn't make sense. I know for a fact that if I have a longer trace, I'm going to get more resistance. So, what the hell's going on here?

**Dave Jones:** And well, I haven't lied to you. This is actually true. The resistance of this smaller one is exactly the same resistance as this bigger one. But, there's a catch.

**Dave Jones:** It all has to do with how you connect to it. Now, in this case, sheet resistance, and the examples we're talking about here, assume that you connect across the entire length like of the end like that, from one side to the other.

**Dave Jones:** If you just solder a wire on there, and a wire on there, like that, eh, we're better off. This theory doesn't Well, it the theory still works, but it's it you have to calculate it differently.

**Dave Jones:** So, if you physically connect like have one big long contact strip across there and across there, then and here and here, then trust me and we'll measure it in a minute, this resistance of this bigger one will be exactly the same as that one.

**Dave Jones:** That's what sheet resistance is all about and why it's a unit without a dimensional area. It's just units ohms per square. It doesn't matter how big the square is.

**Dave Jones:** And that's why it's actually quite relevant to these thin film resistor networks here because if you've seen the previous video, take a look, I might include a photo a screenshot here, they'll have like a big conductive piece on there that connects to the pin which overlays onto the much higher resistance resistive nichrome material.

**Dave Jones:** So, that you do effectively get a you know, a big connection point on the one end. It's not just like a single wire point connecting usually. And it's even more appropriate with your standard thin film resistor networks as well cuz they'll have like a bulk connection on one end like that and then you might have your little laser trim cut in there, something like that to trim the value.

**Dave Jones:** But you're connecting across you know, the entire end piece of that resistive material. So, what it all comes down to and how you can analyze sheet resistances like this and think about it is in terms of squares.

**Dave Jones:** So, if you just got a single square like this, then our ratio is one here. That but if you put two squares like this in series effectively, then of course you're going to double your resistance.

**Dave Jones:** Put a third square over here, make your trace make your copper PCB trace longer, then you get a longer resistance again. And again, if we were just adding things up like that, it's all about the connection point, remember, a solid connection point at the end.

**Dave Jones:** But what if it was just a single connection point like this. Well, then then you start getting into the fact that okay, you got square here, a square here, and all the way along there, but then you've got squares in parallel up here like this and you can kind of divide it up or you can say okay, I've got a big square like this and then I've got other ones and it gets

**Dave Jones:** a bit tricky. So yes, if you've got a just a single connection point like that instead of the entire edge, then of course yes, you're going to have all those extra little squares, however you want to sort of break it up and figure it out and sort of you know, guesstimate it based on um square areas, then yeah, of course your resistance is going to lower because you've got all these extra

**Dave Jones:** squares in parallel and it just becomes a different geometrical problem than the one of that we've been talking about about a single square piece of copper. But that's really essentially how it works with you know, your SMD resistors, how they trim them and your thin film resistor networks.

**Dave Jones:** You know, you can say okay, we've got a a big square there and we might say we've got a square there and a square there and it just becomes a real difficult uh geometrical uh problem based on squares and things like that, but that's generally how you can think about it and the whole aspect why it's called ohms per square.

**Dave Jones:** So you'll analyze this based on a square which is a dimensionless quantity. It's just a square. Doesn't matter how big or how small it is. So just to complete this, what is the sheet resistance of typical 1 oz copper clad PCB material?

**Dave Jones:** I'm glad you asked. Let's take a quick look at it. It is row on the thickness, remember? So our sheet resistance of typical 1 oz copper is the row, the material resistivity of copper is 1.7 * 10 to the minus 8 ohm meters.

**Dave Jones:** That's ohm meters, not ohms per meter. Ohm meters is the units of resistivity of a material, whether copper or anything else. And we divide that by a 1 oz copper-clad board is around about 35 microns thickness.

**Dave Jones:** And that comes out to 0.5 milliohms per square, not per square meter, not per square centimeter, per square, like that. Doesn't matter how big it is, remember? But there's one very important point to be made here is that this sheet resistance, ohms per square, does not change.

**Dave Jones:** It never changes, regardless of what shape you can have a weird and wonderful shape, no matter how many laser cuts you put in there in your fin field, it doesn't matter.

**Dave Jones:** The sheet resistance is a constant for that particular material and thickness and everything else. It doesn't change. All you're doing is changing your electrical resistance between one end and the other for your practical purpose.

**Dave Jones:** And the mathematicians out there can get really excited about this sort of stuff, and you can prove that how you add up the squares and everything, and it's always going to come back to the exact same ohms per square figure.

**Dave Jones:** And there's all sorts of mathematical proofs. Go for your life. So I know what you're thinking, "Dave, I still don't believe it. Show us some measurements." Okay, let's go to the bench and prove that this theory is actually true.

**Dave Jones:** Now, I would love to show you how this works on a piece of copper-clad board, but unfortunately, that's not going to be easy because as you saw, 0.5 milliohms, i.e.

**Dave Jones:** 500 microhms, per square. And trying to get a some sort of contact probe, which probes along all the ends like that of the thing and down in the microhm region is just it's just not practical.

**Dave Jones:** So unfortunately, we're going to have to use something else. Now, I'd love to use like a sheet of nichrome, for example, like they use in those thin film resistor networks at like 100 ohms per square.

**Dave Jones:** That'd be really controlled, and that'd be really nice. Unfortunately, I don't have something like that, but what I do have is tada, a conductive antistatic mat. You've seen these.

**Dave Jones:** You plug your ICs, this high-density foam that you can get. And these It's not going to be a hugely controlled resistance across here, across the material. This is, you know, it's reasonably thick, but as I said, it doesn't matter about the thickness as long as it's a uniform thickness across there.

**Dave Jones:** Anyway, this will have a much higher resistance, you know, tens of K, hundreds of K, that sort of thing. So, we should be able to use this as to get some ballpark measurements and prove this thing.

**Dave Jones:** So, to do this experiment, what I've got is some conductive foam I got from Jaycar. I have no idea what the sheet resistance of this stuff is. Don't have a data sheet for it or anything.

**Dave Jones:** I cut these from exactly the same larger sheet, so they're all identical. And I've got two copper clad plates, which allow me to get the a contact along the full edge like that.

**Dave Jones:** And of course, it doesn't matter if it's longer than that. It's no problem. You just have to contact along the entire edge like that, as I as we saw on the whiteboard.

**Dave Jones:** And then we're just going to measure the resistance. Let's try it. Now, the size of these squares doesn't really matter, but hey, each one is about a quarter of the size than the one before it.

**Dave Jones:** So, let's give that a whirl. Okay, I've got my meter on a fixed range here, the 50 K ohm range, and let's put these plates on. Now, unfortunately, the resistance is going to vary depending on the amount of pressure I put on.

**Dave Jones:** That's just a function of the you know, of the material and the contact area and things like that. And no, my hands aren't touching. Sorry, I'll get out of shot there.

**Dave Jones:** And basically, what I'll do is I'll apply a large amount of pressure on there and get sort of a minimum value. So, I'll put like maximum pressure on all of them.

**Dave Jones:** And I'm getting around about 5K there. I'm going to take that as say 5K, right? So, that's about as high a pressure as I can get. I'll get my smaller one here and let's see if it's the same.

**Dave Jones:** It should be if I apply even pressure cuz you got to have that even contact. Bingo, there it is. There's your There's your five odd There's your five odd K.

**Dave Jones:** I know it's bouncing around and I know people will complain that oh, it's not controlled test. It's as good as I can do here. Now, let's put in the smaller one and up because we've got to make contact over the whole area.

**Dave Jones:** Bingo, look at that. We're still around about that 5K figure with even pressure on all those. So, tada. We've essentially proven and demonstrated there that the sheet resistance, the ohms per square, not square millimeter, not square meter, not square furlong, ohms per square of this material is not determined by the size the physical size.

**Dave Jones:** And of course, you'd get exactly the same result would be at a copper clad board regardless of how thick it is, a solid piece of copper or some other metal or anything else.

**Dave Jones:** And of course, you have to contact the entire edge of that thing. You can't just like like go on the like at an angle on the top like that.

**Dave Jones:** It's not going to work. So, you have to get the If it's a bulk material like that on the entire thing. So, the thinner it gets down to the level where it's, you know, like 35 microns thick on a PCB copper clad like this, then basically you can just put like a contact on the edge.

**Dave Jones:** But, of course, copper this is so incredibly low resistance, um and then you'd have to do proper four-terminal measurement across the entire edge. Oh, I uh it's just a nightmare.

**Dave Jones:** But, this conductive foam demonstrates it rather nicely. And it it's not like a close analogy or anything like that. It is exactly the same thing as copper-clad or nichrome or any other material whatsoever.

**Dave Jones:** It's just that um yeah, this is not hugely controlled, but good enough to see that, you know, if if you expect something higher, if I chop that in a quarter again, we'll get exactly the same result.

**Dave Jones:** Heck, let's do that. Here we go. We got a tiny tiny little piece in there like that. And let's There we go. It's still around about that 5K figure.

**Dave Jones:** Depends on the pressure and things like that. So, you would expect that to increase based on, you know, before you knew about sheet resistance, you would think this would be much larger resistance than this massive sheet here, but it's not.

**Dave Jones:** It's ohms per square. And if you don't believe me that it adds up, well, I've cut that square in half. It's slightly wonky, but anyway, it's good enough. This should only give us 10.

**Dave Jones:** There we go. We've got ourselves 10. I CAN GET IT I CAN'T GET IT MUCH LOWER than that. Look, it's double. It is it has increased double. Oh, now it's starting to bend and it's getting a bit tricky, but you saw it.

**Dave Jones:** And if we do three times the length, there we go. There's our There's our 15 odd K. So, just think about the sheet resistance next time you're calculating the resistance of a PCB trace, for example, because this is not just theoretical mumbo jumbo.

**Dave Jones:** It has real-world practical applications. If you've got a PCB trace like this, you are actually going to have pretty much an end-to-end connection, like the entire edge on here and the entire edge over here, cuz imagine this is a little tiny, you know, 10,000 trace or whatever, going into a surface-mount component this end, a surface mount component at that end, then you you know, you're basically touching the

**Dave Jones:** entire edge. So, you can divide this up into squares. 1 2 3 4 or however many squares length. So, you know the sheet resistance of 1 oz copper, uh you can say it's a like a rule of thumb, it's going to be pretty darn precisely close to it, actually.

**Dave Jones:** Um 0.5 m per square. Just count up the number of squares you got, you can calculate the length of your trace. Brilliant. And that will apply to copper or any other material which has its sheet resistance specified.

**Dave Jones:** So, I hope you found that Fundamentals Friday useful. A lot of people don't know about sheet resistance cuz it's a little bit counterintuitive to what they're used to, but it's a real thing.

**Dave Jones:** And it's how materials like the nichrome films and and copper clad PCB and other stuff are actually specified. So, there you go. If you liked it, please give it a big thumbs up cuz that always helps a lot.

**Dave Jones:** And if you want to discuss it, jump on over to the EEVblog forum or leave YouTube or blog comments. Catch you next time.
