---
video_id: rfaCFEqk05M
title: EEVacademy | Digital Design Series Part 3 - Designing Combinatorial Digital Logic Circuits
url: https://www.youtube.com/watch?v=rfaCFEqk05M
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 16, "2": 39, "3": 58, "4": 72, "5": 97, "6": 113, "7": 123, "8": 144, "9": 177, "10": 196, "11": 209, "12": 225, "13": 245, "14": 264, "15": 281, "16": 296, "17": 315, "18": 330, "19": 348, "20": 367, "21": 385, "22": 409, "23": 430, "24": 454, "25": 475, "26": 497, "27": 514, "28": 533, "29": 554, "30": 570, "31": 588, "32": 604}
---

**Dave Jones:** Hi, in the previous video in this digital logic design series, we took a look at Boolean algebra and De Morgan's theorems and the various laws, commutative laws, associative laws, distributive laws, and all that horrible Boolean algebra type stuff. And it was quite theoretical but important stuff.

**Dave Jones:** But we didn't really look at how do we actually create a practical digital logic circuit based on the truth table. So that's what we're going to take a look at today, designing combinatorial logic circuits or how to convert basically a truth table into digital logic or complex digital logic

**Dave Jones:** to perform the function that you intend. Because when you're designing a system, you want something, you've got various inputs. So let's go A, B, and we'll have an output X. And you've no doubt seen the truth tables before in the previous videos, you most certainly have.

**Dave Jones:** We've got all the various combinations of the inputs, in this case there's only four of them because we've only got two inputs. And let's say we wanted our outputs like this, right? How do we convert that into a digital logic? Well, we're going to use what's called the sum of products method to do this.

**Dave Jones:** So what we do is we look at which of the outputs here are 1, and then we're going to create that using AND gates. So any expression like that, we just go one by one through the truth table, in this case it's a real easy truth table, there's only four rows in our truth table, and only one of them has a 1 on the output, it's really easy.

**Dave Jones:** So we're going to create the sum of products. So what we need to do is look for the first one here that contains a 1, and we're going to create that using AND gates. So let's do that. So we've got our inputs A and B here, so we'll actually go up here like this,

**Dave Jones:** so this particular line here, A and B inputs. Now, we want the output to be a 1 when A is 0 and B is 1. And we need to do this using an AND gate like this. So this is X on our output.

**Dave Jones:** So how do we do that? Well, it's easy. A needs to have an inverter like that. We've got to convert the 0 of the A here into a 1, and B's already a 1, so we can feed B just straight into our AND gate.

**Dave Jones:** And believe it or not, that's it. X equals, well, not A, because we've inverted it, and B. And believe it or not, that is the entire circuit for this truth table. Why? Because we've gone through and looked at all of these, this one, this one, this one, and this one here, and only one of them has a 1 on the output.

**Dave Jones:** And because this is digital logic, it's either a 1 or a 0, the output here, X, can either be a 1 or a 0, and we've done the case here where it's a 1, so in all other cases, it doesn't matter what A and B are doing here, this output, X, will always be a 0.

**Dave Jones:** So it doesn't matter if they're both 0, it'll give a 0. If they're 1 and 0, it'll give a 0. If they're 1 and 1, it'll give a 0. Because we've designed it around this case here, and all the others are just going to come out in the wash.

**Dave Jones:** So bingo! We've done it. So let's see where this expression, sum of products, comes from. So what we'll do now is just erase that, and we will put a 1 in there. So we've changed it, so this one's already the same here, so we don't have to change that.

**Dave Jones:** This circuit here is going to remain exactly the same. But because we've got another expression in our truth table here that is a 1 on the output, we have to once again create, use another AND gate here, like this, to actually generate that input.

**Dave Jones:** So we're going to have the input, in this case, A is a 1, so we don't need that. But you guessed it, B is going to need the inverter. So it's opposite to what we had before. And in this case, X equals A and not B, like that.

**Dave Jones:** But of course we're not done yet. We've done the product part of this. So each one of these is essentially the product aspect of it, but now we have to do the sum part of it, and we do that using an OR gate like this.

**Dave Jones:** And we just take each expression that we got from each one of these terms in our truth table here, and then we just OR them together, or we sum them together with an OR gate to give us a final expression like that. Bingo!

**Dave Jones:** Now we have the complete circuit which represents this complete truth table here in the sum of products form. Beautiful. That's it! We've designed a combinatorial logic circuit based on our desired truth table here. Because in system design, you're going to have a bunch of inputs that you want to,

**Dave Jones:** that you have from very, whatever it is, and then you want to actually do some logic on that and produce a particular output. And this is how you do it. It's that simple. Now in practice, this might not be the easiest circuit to implement

**Dave Jones:** if you've got your 74 series logic or whatever, because look, we've got an OR gate over here, we've got two AND gates, we've got two inverters, three different types of logic gate there. So it'd be nice if we actually consolidated this circuit into just one particular type of gate.

**Dave Jones:** And probably the best way to do this and most versatile, as we'll see, is with the NAND gate. So let's actually take this circuit and convert it into just using NAND gates. Now we can do this over here like this, our OR, we can convert into NAND

**Dave Jones:** by inverting or knotting the inputs like that. So we could have our circuit just like this, but we've still got our inverters over here and we've got AND gates here. But look, we've got our knots here. What if we just moved this knot from here to here and here to here?

**Dave Jones:** You guessed it, we've got, let's get rid of that, that, and we use NAND gates there, bingo! Then we can simply erase our inverters there and we can put in a NAND gate like that, just both inputs like that, and Bob's your uncle!

**Dave Jones:** That is the equivalent circuit to that up there, but it's using basically the same number of gates. It's using five gates, but they're all NAND gates. So that can be advantageous if you're using discrete logic or whatnot. It can be just very handy to use the one particular type of gate.

**Dave Jones:** And we actually forgot to look at our final expression here. X equals actually NOT A AND B OR A AND NOT B like that. You can put brackets around those if you want to keep it nice and tidy. And that's our Boolean logic expression, that's our Boolean algebra expression for this particular circuit.

**Dave Jones:** And of course we've seen in the previous video how we can actually use De Morgan's theorem and the various laws to actually simplify Boolean algebra like this. So this would really come into play if you had A, B, C, D, E, F inputs like this.

**Dave Jones:** And if you even, well, just those alone would produce a massive truth table. You know, you have to go through 1, 0, like, and imagine if you had a whole bunch of those, the expression would be, can end up being absolutely enormous. Not excluding the fact that you could have multiple outputs if you really wanted as well.

**Dave Jones:** And this one could be a 1 or, you know, something like that. Whatever, you could have various outputs for various purposes. So you can combine lots of inputs, lots of outputs, and you'd end up with a massive expression. This one is about as simple as it gets.

**Dave Jones:** And yes, we can use those laws and theorems in the previous video to do that, but I think in the next video we'll show you a graphical technique for doing circuit simplification called Karnaugh mapping. And it just uses a visual, it's a visual way to do it, and it is quite neat.

**Dave Jones:** And you might think, well, nobody uses this sort of stuff anymore, it's just all theoretical stuff you learn in your digital logic 101 class. Well, no, all this sort of stuff is still valid whether you're designing the latest Intel, you know, i7, whatever processor, because just reducing the number of gates,

**Dave Jones:** digital circuit simplification is very important. Not only do you use less gates, use less silicon area, which makes your chip smaller, it makes it faster as well, and all sorts of stuff. So this sort of stuff is still done today, even though, you know,

**Dave Jones:** there's not many people designing with, you know, big systems with discrete 7-4 series logic anymore. This was, of course, a big thing back in the day to save X number of chips on your board. It was very handy, but it is still very important to know this from a digital logic point of view.

**Dave Jones:** So we'll look at Karnaugh map simplification next time. So I hope you enjoyed this, and if you did, please give it a big thumb, oh, well, thumbs up. That's not, that's like an inductor, isn't it? Give it a big inductive thumbs up if you liked it, and as always,

**Dave Jones:** discuss it down below in the comments or on the EEVblog forum. Catch you next time. Transcribed by https://otter.ai
