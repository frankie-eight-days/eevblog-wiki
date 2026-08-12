---
video_id: hFvqEfZfMtA
title: EEVacademy | Digital Design Series Part 2 - Digital Logic Boolean & Demorgan's Theorems
url: https://www.youtube.com/watch?v=hFvqEfZfMtA
source: youtube-asr
timestamps: {"0": 1, "1": 15, "2": 27, "3": 42, "4": 60, "5": 71, "6": 82, "7": 95, "8": 113, "9": 133, "10": 147, "11": 162, "12": 176, "13": 199, "14": 216, "15": 235, "16": 247, "17": 261, "18": 277, "19": 291, "20": 310, "21": 320, "22": 339, "23": 352, "24": 365, "25": 381, "26": 395, "27": 406, "28": 423, "29": 436, "30": 447, "31": 460, "32": 477, "33": 502, "34": 514, "35": 532, "36": 544, "37": 561, "38": 573, "39": 584, "40": 603, "41": 618, "42": 628, "43": 641, "44": 654, "45": 688, "46": 700, "47": 712, "48": 729, "49": 744, "50": 762, "51": 775, "52": 794, "53": 811, "54": 825, "55": 836, "56": 851, "57": 864}
---

**Dave Jones:** Hi, in a previous video we took a look at basic digital logic gates, truth tables, and basic Boolean algebra. Now it's time to move on to theorems. More specifically, Boolean and De Morgan's theorems which allow us to do circuit or digital logic simplification.

**Dave Jones:** So, let's take a look at Boolean theorems first. It won't be complex at all, so don't worry about theorems you might think are hard, but these are pretty basic concepts.

**Dave Jones:** So, there are two types of Boolean theorems. There are single variable theorems and multi-variable theorems. Now, single variable theorems are really easy. Let's take the example of we have an AND gate here like this.

**Dave Jones:** We have an output, we have an input, and the other input here is inverted like that. And our input is A like this. Then our theorem can said to be A AND NOT A because it's inverted over here.

**Dave Jones:** If you remember your truth tables from before, you can just figure it out from your knowledge of AND gates, both of the inputs can never be high at the same time cuz there's an inverter in there giving you the not.

**Dave Jones:** So, the output is always going to be zero. And that right there is a single variable theorem because we've only got one variable A here. That's all there is to it.

**Dave Jones:** And you can have any combination of gates doing the same thing. Let's uh for example, say we had an OR gate here and we actually tied the inputs to the OR gate together like that.

**Dave Jones:** Then if we had A here, then that would give us A on the output. So, the theorem would be A OR, which is the plus symbol, A like that is always equal to A.

**Dave Jones:** Very simple. Just a single variable theorem because we only have the one variable involved in the equation. Now, we move on to multivariable theorems. Now, a theorem is not an equation, so we're not going to put, say, output Z here or anything like that because this we're not dealing with equations.

**Dave Jones:** Theorems are just propositions based on in this case logical conclusions based on these gates. So, let me try and explain this a bit better. So, we've got an AND gate here with A on the input.

**Dave Jones:** So, this can be A and B, but it can be said that A and B can also be equal to B and A. We don't care about the order in which they go.

**Dave Jones:** And likewise, we can do A or B is actually equal to B or A. And these two laws or theorems here are called commutative laws, and these basically mean we don't care in which order those terms go.

**Dave Jones:** It makes absolutely no difference. And if we introduce a third variable here, then we can go A and B and C is equal to A and B and C and is also equal to A and B and C like that.

**Dave Jones:** The brackets, it makes no difference in which order you actually group them. And likewise, we can do the exact same thing with the OR function. A plus B plus C equals A plus B grouped together or C, it makes absolutely no difference.

**Dave Jones:** And you can actually represent those with external gates as well, not just with one three-input OR gate, for example. You can actually add extra gates in here. So, these are called associative laws in that we can group the variables of or or ands together in any combination we like.

**Dave Jones:** So, you might be able to see where we're going here if you know basic algebra. If you don't, this might not make, you know, a huge amount of sense, but hopefully you can follow through.

**Dave Jones:** We've now got what's called distributive laws, and these work just like regular algebra except in digital form. They follow the same grouping expressions just like you find in regular algebra.

**Dave Jones:** So, just like regular algebra, we can expand these by multiplying or anding the terms out just like that. So, these are all these three different laws here have direct correlation to regular regular algebra you might have learned.

**Dave Jones:** And likewise, just like regular algebra, if we have a common term, so let's take this logic function here, A and not B and C or not A not B not C, we have the common term here.

**Dave Jones:** We have B not B is common and not B is common over here. We can actually simplify that out. So, we can take out our not B, and then we can end it with we can go A and C or not A and not C.

**Dave Jones:** We can take that out, and of course you can put parentheses around there just to group the expressions if you really want to. But, that's just like regular algebra you know about learned at school.

**Dave Jones:** Works exactly the same on multi-variable Boolean logic. Awesome. So, the reason we're doing all this is for circuit simplification because over here we've got three input and gates, for example, and we might need a lot more gates and more gates to implement this than we do for this function over here.

**Dave Jones:** And if I rather crudely draw out the expression on the left-hand and the right-hand side of this uh equivalency here. Um please excuse the crudity. I didn't have time to build it to scale or to paint it.

**Dave Jones:** You'll notice that we have 1 2 3 4 5 two-input gates here and three inverters. Whereas this equivalent circuit over here, we've simplified it only by a little a smidgen by one gate.

**Dave Jones:** Now we've only got 1 2 3 4 two-input gates plus three inverters. So we've eliminated one whole gate. Now this isn't the best uh example, but see that we have simplified the circuit and they're completely equivalent using standard Boolean algebra.

**Dave Jones:** In this case, using distributive law algebra or distributive law Boolean algebra. Beautiful. Now, let's take a look at a way to simplify things much easier using De Morgan's theorem.

**Dave Jones:** Now De Morgan's theorem or De Morgan's laws, however you want to call it, as is common in electronics, the name comes from the person who found it. In this case, Augustus uh De Morgan.

**Dave Jones:** Real clever dude in the uh 19th century. Came up with two very simple laws for Boolean algebra here. Now if we've got A or B and there's a bar right over the top like that, it's equal to not A and not B.

**Dave Jones:** You'll notice that it's changed from an or to an and. And the second one is if we've got A and B with a not right over the top, it's equal to not A or not B.

**Dave Jones:** You'll notice that it's changed from an and here to an or here. Now these that's all there is to De Morgan's laws, De Morgan's theorems. Now you should memorize these, but there's a much easier way to think about it.

**Dave Jones:** Let me show you. Let's say you've got any expression like A or B or C. It can have as many terms as you want. If you've got a bar over the top of all that.

**Dave Jones:** What you want to do is instead of remembering these laws over here, what you can do is just remember if you've got a bar on top, what you do is you drop the bar, drop the bar down like this and change any signs.

**Dave Jones:** So, this will become not A and not B and not C. Drop the bar and of course the bar remains. Okay, when you drop it like this, it changes the signs here and here and it just simply leaves a bar that bar over the top.

**Dave Jones:** So, you can't drop the bar through a term, but those um operations there change and that follows this law, this theorem over here. Drop the bar, change the operator.

**Dave Jones:** That's all you need to remember for anything to do with uh De Morgan's theorem. Simple. Let's go more complicated. Let's say we've got A bar like this and B or C bar like this with a bar all the way over the top.

**Dave Jones:** What's that one be going to uh go into turn out to be, I hear you ask? Well, let's what we do is we drop the bar down and we change the sign like this.

**Dave Jones:** So, we're going to end up with A bar bar, black sheep plus B bar like that and we got to change the sign there because we're dropping the bar down and C with a dual bar.

**Dave Jones:** Now, what do you do with these when you got two bars like this? Well, if you've got A here and you put an inverter like that and then you have another inverter cuz that's basically what it's saying.

**Dave Jones:** Well, what is the output here? This point is going to be uh A bar, but this one is just going to be A again. So, A equals A. So, if you got two bars like that, they cancel out.

**Dave Jones:** So, that actually becomes A or B bar and C. That's it. Easy. We've simplified the expression. So, what is the implication of this? If we have a look at our function over here, which is just a NOR function which represented by the NOR gate here, there it is.

**Dave Jones:** That is equivalent to an AND gate with the inputs inverted like this. Now, you can produce an AND gate from a NAND gate up here by simply shorting the two inputs.

**Dave Jones:** A NAND gate can become an inverter. Go have a look at the truth table you should learn previously. So, we can You might start to see that we can create a NOR gate from NAND gates.

**Dave Jones:** And likewise, we can create a NAND gate from NOR gates down here because once again, you tie both inputs of a NOR gate together like this, then that becomes an inverter.

**Dave Jones:** You invert that, it becomes an OR gate. And then, of course, you can just go invert invert the inputs like this, short those together, and that becomes your inverter.

**Dave Jones:** And boop boop boop like that. Inverter input, bingo. We've created that NAND gate from NOR gates and vice versa. In fact, I'll go even further than this and claim, uh which is true, you can go try it for yourself, that you can create any combinatorial logic circuit right up to the complexity of an Intel i7 processor or whatever complex digital system you like using just NAND gates or just NOR

**Dave Jones:** gates. And that includes exclusive OR and every other function you can possibly think of. You only need one type of gate. Brilliant. So, let's use the example of this little combinatorial circuit here.

**Dave Jones:** We've got two two-input NOR gates here with the inputs shorted together. So, they're acting as inverters, inverting the inputs to this NOR gate here. Now, this could be part of a more complex circuit or whatever, but we'll take it just on its own.

**Dave Jones:** So, the if we call the output C here, then we can actually give that an expression A bar, because it's inverted, or B bar, cuz it's inverted, and we put the bar over the top like that, and that is the expression.

**Dave Jones:** Now, if we apply De Morgan's theorem to this, what do we get? We drop the bar and change the operator sign. So, we've got not not A and B with a not like that, and we can eliminate these nots.

**Dave Jones:** They cancel each other out, right? So, getting rid of that, what are we left with? Ah, A and B. It's equal to a simple AND gate like that. Simple.

**Dave Jones:** We've completely simplified. So, if you saw a circuit that had these gates in it, you know, "Oh, I can simplify that." And bugger off using three two-input gates, I can replace that with one AND gate, and it's a functionally equivalent circuit.

**Dave Jones:** That's the power of uh Boolean theorems and De Morgan's theorem to simplify circuits. So, if we go have a look at a data sheet for an exclusive OR gate, for example, 74HC86, absolute classic, you'll notice there's no exclusive OR gate.

**Dave Jones:** It's made from, well, in this case, inverters, AND gates, and NOR gates, and another inverter. But, we've already determined that we can make this NOR gate here, for example, we can actually make this NOR gate from NAND gates.

**Dave Jones:** We can make the AND gate from NAND gates, or we can make the AND gates from NOR gates, etc. So, we can build that exclusive NOR function, or exclusive OR function, sorry, out of just regular gates.

**Dave Jones:** So, that's how they're physically Well, that's similar to how they would physically be implemented in the actual silicon itself. Everything would out of either NOR gates or NAND gates.

**Dave Jones:** It's as simple as that. So, I hope you found that interesting. It's a bit a little bit theoretical this you know, Boolean and De Morgan's theorems, but it is one way that we do simplification, circuit simplification.

**Dave Jones:** Another more advanced way might be say Karnaugh maps, which we'll have to leave to another video. But, anyway, I hope you found that interesting. If you did, please give it a big thumbs up, and as always, comments down below.

**Dave Jones:** Catch you next time.
