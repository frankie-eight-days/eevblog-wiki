---
video_id: lJ3q9RHIatU
title: EEVacademy | Digital Design Series Part 5 - Karnaugh Maps
url: https://www.youtube.com/watch?v=lJ3q9RHIatU
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 23, "2": 23, "3": 54, "4": 79, "5": 102, "6": 113, "7": 121, "8": 140, "9": 157, "10": 179, "11": 203, "12": 222, "13": 247, "14": 263, "15": 283, "16": 301, "17": 320, "18": 346, "19": 364, "20": 380, "21": 400, "22": 413, "23": 413, "24": 413, "25": 461, "26": 521, "27": 581, "28": 581, "29": 611, "30": 671, "31": 731, "32": 791, "33": 851, "34": 881, "35": 911, "36": 971, "37": 1031, "38": 1091, "39": 1151, "40": 1181, "41": 1181, "42": 1211, "43": 1271, "44": 1331, "45": 1391, "46": 1421, "47": 1421, "48": 1421, "49": 1455, "50": 1515, "51": 1575, "52": 1635, "53": 1695, "54": 1725}
---

**Dave Jones:** Hi. In previous parts of this digital logic tutorial design series, we've taken a look at basic digital logic gates, all you need to know about those, and digital Boolean logic and De Morgan's theorems, and then we switched over to designing combinatorial logic circuits, and we went through all the commutative laws and the associative laws, distributive laws, and stuff like that.

**Dave Jones:** So I'll link in those videos if you haven't seen it. In that video, I promised I'd show you a way to actually do digital logic reduction, not using any algebra at all, but using a visual method called KanoMaps. Let's take a look at it.

**Dave Jones:** It's pretty magical. Let's say we've got our truth tape of our logic function that we want here, okay? We've got three inputs here, A, B, and C, and we've got one output we'll call X. And, of course, with three inputs, that gives us eight different...

**Dave Jones:** binary states that we can have on the inputs. So we potentially have eight different output functions here, and we can write this as an algebraic expression. Pretty easy. We can use sum of products. As we learned in a previous video, sum of products is we find all of the ones here on our output, and then we write that as a product expression, because it's a sum of products, okay?

**Dave Jones:** So the product expression here is not A, like this. Because it's a zero, and one, B, is a one, so we just call it B, and C is a zero, so that is not C, like that. And we've got more than one, one, on the output here, so we have to sum the different products.

**Dave Jones:** So we do the products of the other one that we've got here, which is A, like that, and B is a one, so it's just B, and C is a zero. So we do the products of the other one that we've got here, which is A, like that, and B is a one, so it's just B, and C is a zero.

**Dave Jones:** So we do the products of the other one that we've got here, which is A, like that, and B is a one, so it's just B, and C is a zero, here, so that is not C, like that. And that is our expression, so X equals that.

**Dave Jones:** So that's our algebraic logic expression for that function. But we want to simplify this, because if you try and implement that with just discrete gates, you'll find, yeah, you can do it, but you'll end up with too many gates. Now, of course, we can solve this algebraically, but who likes solving algebra equations?

**Dave Jones:** Yeah, nah. But let's... Let's do it anyway, okay? So this, we find that B is the same here, okay? So we can take out B as a separate function, and then we've got C is the same either side, or sorry, not C is the same, so we can actually take out that.

**Dave Jones:** So it's B and C there, so we're left with, we'll put a bracket in there like that, and we're left with not A and A, so it's not A, like that, plus A, okay? So that is, you know, this is algebra stuff. It doesn't matter whether you're doing mathematical algebra or digital algebra like this, the rules are the same.

**Dave Jones:** Now, this not A plus A here, we can actually simplify that, no problems whatsoever, because not A plus A is, it's always 1. So that gives us B, not C, and then 1, like that, right? Or we can put 1 in brackets like that, and because this is like and 1, well, like, we can put the dots in there, like some people like putting the dots in there.

**Dave Jones:** Like that, you don't have to, you can leave it out, it's implied that it's an and function. So if you and B, not C, with 1, well, that just equals B, not C, like that. We've simplified this algebraic expression to just B and not C.

**Dave Jones:** Easy. So we can just draw that as an and gate like that, and we could go B, and of course, C is not like that. So we need to put an inverter, and C, like that, and that's our output, X. And you'll notice that A, it doesn't matter what A is, we always get that output function is only dependent upon B and C.

**Dave Jones:** And if you don't believe me, you can do this by inspection of the table, right? Our output's 1 here, okay? It's when B and C is 1, 0, B and C here is also 1, 0, and it doesn't matter whether A is a 0.

**Dave Jones:** Or a 1 in this case, you get a 1. So that's why A does not matter. You only rely upon B and C to give you the output X there. But if we implemented this function up here with gates, we'd be actually using A because A is in our expression there.

**Dave Jones:** So we can actually draw this original function here and see how many gates we've actually saved. So here it is, this original algebraic expression, if we just implemented that, directly with gates, we would end it up with two 3-input AND gates and OR gates and three inverters like this.

**Dave Jones:** And we have now actually simplified that to a 2-input AND gate and an inverter. And that's the power of not only algebraic simplification, you can do this via algebraic mathematical methods, or you can do it visually using Kano maps that I'm about to show you.

**Dave Jones:** But you might have noticed, the keen eye here might have noticed, Dave, look, you didn't need this extra inverter in here, you could have actually connected that directly up to there. And if you spotted that, bonus internet points. But these sort of circuit simplifications here are the entire point of doing Kano maps and also algebraic logic like this and algebraic simplification as well.

**Dave Jones:** And this, you might think, oh, who designs with discrete logic chips anymore? No one, right? Well, no, you do. Because you don't want to be working inside FPGAs and inside ASIC chips and inside processors and things like that. You don't want to be implementing this many gates if you can get away with just this.

**Dave Jones:** Because not only do you have the extra gates and the extra silicon, you also have the extra propagation delay time to get every stage of gates you go through, increases your propagation delay, that slows down the maximum frequency of your chip, like your latest Intel processor or whatever it is.

**Dave Jones:** So you definitely want to be simplifying logic. So there is still a huge place for learning this sort of stuff. So this clever dude called Maurice Kano, he figured out in the 1960s, I think, that you can actually do this visually, this simplification visually, without any algebraic skills whatsoever.

**Dave Jones:** Alright, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table. Alright, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table.

**Dave Jones:** Alright, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table. Alright, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table.

**Dave Jones:** Alright, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table. Alright, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table.

**Dave Jones:** Alright, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table. Alright, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table.

**Dave Jones:** Alright, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table. Alright, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table.

**Dave Jones:** Alright, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table. Alright, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table.

**Dave Jones:** Alright, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table. Alright, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table.

**Dave Jones:** Alright, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table. Alright, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table.

**Dave Jones:** Alright, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table. Alright, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table.

**Dave Jones:** Alright, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table. Alright, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table.

**Dave Jones:** Alright, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table. Alright, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table.

**Dave Jones:** Alright, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table. Alright, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table.

**Dave Jones:** Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table. Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table.

**Dave Jones:** Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table. Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table.

**Dave Jones:** Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table. Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table.

**Dave Jones:** Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table. Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table.

**Dave Jones:** Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table. Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table.

**Dave Jones:** Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table. Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table.

**Dave Jones:** Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table. Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table.

**Dave Jones:** Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table. Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table.

**Dave Jones:** Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table. Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table.

**Dave Jones:** Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table. Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table.

**Dave Jones:** Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table. Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table.

**Dave Jones:** Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table. Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table.

**Dave Jones:** Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table. Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table.

**Dave Jones:** Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table. Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table.

**Dave Jones:** Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table. Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table.

**Dave Jones:** Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table. Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table.

**Dave Jones:** Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table. Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table.

**Dave Jones:** Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table. Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table.

**Dave Jones:** Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table. Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table.

**Dave Jones:** Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table. Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table.

**Dave Jones:** Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table. Okay, so what we're going to do now is we're going to draw a table that has the same number of squares as elements in our truth table.

**Dave Jones:** Subtitles by the Amara.org community
