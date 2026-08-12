---
video_id: 7bVnsXHO6Uw
title: EEVacademy | Digital Design Series Part 1 - Introduction To Digital Logic
url: https://www.youtube.com/watch?v=7bVnsXHO6Uw
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 26, "3": 42, "4": 68, "5": 82, "6": 100, "7": 108, "8": 121, "9": 137, "10": 149, "11": 165, "12": 189, "13": 208, "14": 220, "15": 238, "16": 254, "17": 270, "18": 287, "19": 302, "20": 320, "21": 331, "22": 342, "23": 356, "24": 375, "25": 382, "26": 395, "27": 402, "28": 417, "29": 430, "30": 443, "31": 454, "32": 463, "33": 475, "34": 495, "35": 510, "36": 528, "37": 547, "38": 562, "39": 571, "40": 585, "41": 595, "42": 610, "43": 627, "44": 641, "45": 650, "46": 668, "47": 679, "48": 690, "49": 701, "50": 715, "51": 725, "52": 749, "53": 760, "54": 770, "55": 786, "56": 804, "57": 818, "58": 833, "59": 846, "60": 855, "61": 877, "62": 889, "63": 898, "64": 908, "65": 925, "66": 936, "67": 958, "68": 985, "69": 995, "70": 1010, "71": 1021, "72": 1036, "73": 1050, "74": 1065, "75": 1080, "76": 1098, "77": 1112, "78": 1132, "79": 1157, "80": 1171, "81": 1191, "82": 1206, "83": 1218, "84": 1244, "85": 1257, "86": 1275, "87": 1291, "88": 1304, "89": 1317, "90": 1334, "91": 1351, "92": 1365, "93": 1375, "94": 1391, "95": 1405, "96": 1430, "97": 1445, "98": 1459, "99": 1474, "100": 1490, "101": 1515, "102": 1526, "103": 1543, "104": 1564, "105": 1581, "106": 1600, "107": 1612, "108": 1626, "109": 1637, "110": 1653, "111": 1667, "112": 1680, "113": 1698, "114": 1710, "115": 1731, "116": 1746, "117": 1767, "118": 1794, "119": 1809, "120": 1818, "121": 1828, "122": 1839, "123": 1848}
---

**Dave Jones:** Hi, I thought I'd try something a bit different today. Check this out. The reason you're looking at a blank white screen with a cursor is because I've got myself a new Wacom Intuos tablet and I'm rather taken by this thing.

**Dave Jones:** It's one of these pen-based tablets that allows me to draw and like artists use these things for, you know, doing graphic art and digital, you know, animation and all that sort of stuff.

**Dave Jones:** You can use them as simple drawing tablets like this. So, I thought I'd try and do some tutorial type videos using this capture tablet and I want your feedback in this whether or not you actually like this format or not because I can do some, you know, funky stuff with it.

**Dave Jones:** I can instantly change colors and it's like I can either go light or dark like that and I can change my styles of pens. I can instantly push a button and whoop, if I push the right button, and erase stuff and I can do lots of much more fancier arty stuff like this, but it's just really nice to be able to just, you know, do a drawing-based

**Dave Jones:** tutorial just like my regular Dave CAD stuff that you're no doubt familiar with. So, I thought we'd give it a go. So, I'd really like your opinion on whether or not you think this is a good idea and I'll probably put a poll somewhere up here in the corner.

**Dave Jones:** It should automatically pop up whether or not you'd like to see more of this style of tutorial and whether or not you'd actually like to see this on a second channel like move this sort of screen capture type tutorial content to its own dedicated channel where that's all I uploaded to.

**Dave Jones:** So, let me know if you think that's a good idea or not and let me know what name you'd like to, if you like that idea, what name you'd like to call that second channel.

**Dave Jones:** It could be like EV Learn or EV Tutorial or EV University or something like that. Please let me know. Um, yeah, some YouTube poll thing will pop up and work.

**Dave Jones:** Anyway, let's get to it. So, what is digital logic and how does it differentiate from the analog world? Well, you might be familiar with a sine wave, for example, and that has, you know, 0 V here and 1 V here and -1 V here, for example.

**Dave Jones:** And this is a representation of an analog signal and it can vary anywhere, you know, within that range, for example. But, you might be familiar that a digital system is represented like this.

**Dave Jones:** It only has two particular levels like this and these can be called logic one and logic zero. They could be called 5 V and 0 V. It could be 3.3 V and 0 V might be common voltages, for example.

**Dave Jones:** There's other ones. It It just represents a binary representation of analog voltages. So, digital is still analog in terms of the actual waveform, but the way it's interpreted and represented, it's only in binary form like this and it could be called one or zero.

**Dave Jones:** Also called true, false, for example. And you know, any name you want to give it, it doesn't matter. It represents two different logic states. And because digital still lives in the analog world, then we have to actually set boundaries.

**Dave Jones:** If this is 0 V here and this is 5 V here, for example, our waveform is not going to be absolutely perfect. So, it's, you know, it might be like this, but it might not.

**Dave Jones:** Okay, 0 and 5 V. So, we have to actually set boundaries in here where something is determined to be a logic one and a logic zero. So, in this particular case, like it might be say 4 volts just as an example.

**Dave Jones:** And anything above 4 volts, so anything in here is determined to be a logic one. And likewise, anything in here is determined to be a logic one. And anything under here like this is determined to be a logic zero.

**Dave Jones:** So, these levels can be called one and zero, true and false, high and low, where 5 volts and 0 volts, whatever you want to call it. But, when if the signal is inside this region here, then it's an undefined state.

**Dave Jones:** Digital doesn't know what to do with it. Systems don't know what to do with it. So, if you've got a slow-changing signal like this that ramps up from 0 to 1 volt like this, then this time period all this period in here is unknown.

**Dave Jones:** So, your digital system is not going to know how to interpret that. So, that is why you'll always see digital signals being just one or zero with as fast an edge as humanly possible.

**Dave Jones:** So, in a typical digital logic system, we might have a chip here, for example, that is connected to ground and is connected to 5 volts or 3.3 volts, for example, are very typical modern digital logic levels or even lower, you know, 1.8 1.2 volts.

**Dave Jones:** It doesn't matter. It's going to represent a binary value one and zero, true and false, high and low. And you will have various inputs to the chip, and you'll have various outputs to the chip.

**Dave Jones:** And these are all going to be either one or zero or one or zero. I.E., in case of a 5-volt rail chip, you'd have 5 volts here, and you'd have 0 volts here.

**Dave Jones:** And it's expecting 5 volts on the input and 0 volts on the input here with those margins that we talked about before. So, what we need to do is actually look at basic digital gates.

**Dave Jones:** These chips are all going to contain digital logic or what's called digital logic gates. And there's only a handful of different types of gates which can be used to make up all any chip, be it your latest Intel microprocessor that's got you know a hundred million gates in the thing or they talk in terms of transistors.

**Dave Jones:** You can think of transistors as gates cuz they're going to turn off and on, but we won't go into detail there. So, let's take a look at your basic logic gates.

**Dave Jones:** Now, there are three types of basic gates that you're going to need to know for starters, the AND gate, the OR gate, and the NOT gate, more commonly referred to as an inverter or an inverter gate.

**Dave Jones:** So, let's take a look at the traditional symbols for these. There are two different types of symbols which makes it a bit confusing. You should know both of them now.

**Dave Jones:** Uh both defined by IEEE and IEC and that sort of stuff. But, I'm just going to call these the you know traditional style ones. So, the traditional style AND gate is a line like that with a curved line like that.

**Dave Jones:** You can think of it as a D. Just remember the D and make like that. So, you've got one output and you've got at least two inputs. As we'll see, a logic AND gate needs at least two inputs.

**Dave Jones:** You can have more, but that's a special case. Now, the OR gate is actually shaped like this, curved there, and then like that's not very good, is it? So, we'll just draw that one a bit nicer.

**Dave Jones:** Once again, two inputs, one output. Now, the NOT gate is different in that it only has one input and one output. And it's got this circle on the end here.

**Dave Jones:** And this is this circle is known as a NOT symbol. So, So, inverter symbol, if you just want to draw it's on its own, is the triangle plus the little not there.

**Dave Jones:** Now, this not can actually be used on its own, and you've probably seen these on data sheets for chips and things like that. The actual symbol on the, you know, right on the pin, it might have this little not on it.

**Dave Jones:** It's called this little circle, and that implies well, that particular pin is inverted. But, you also need to know the IEC symbols, I'll call them, and they're all boring square boxes like this, and we can put our two inputs and our one output, and it's got an AND symbol in the middle like that.

**Dave Jones:** It's actually reasonably descriptive. So, from that point of view, I don't mind it at all, and I occasionally use those myself. And the OR one, once again, our square, but it's got greater than or equal to one, and you'll see why in a minute.

**Dave Jones:** So, I I've never really liked that bit. And our not is once again a square, but it's got one, and then our one input, one output, but instead of putting the circle, they define it as a little um 45° diagonal line like that.

**Dave Jones:** So, that just implies the not function, and you might have seen that in some data sheet chips as well. Now, it's actually called digital logic for a reason, because these gates, AND, OR, and the inverter perform logical functions, which we can use to perform computations.

**Dave Jones:** That's how computers and everything else you know, modern digital, almost practically everything in modern society works using digital logic. Now, we can use what's called a truth table here, and you have to know these.

**Dave Jones:** You should remember them off by heart, and learn how each particular function works. Now, we've got two inputs here. I've labeled them A and B, and the output C here.

**Dave Jones:** So, you just draw a table like this with our inputs and our on one side and our output on the other side and you basically fill it out with all of the possible combinations.

**Dave Jones:** So, the two inputs could be zero and zero, low and low. It could be zero and one. It could be one and zero and it could be one one.

**Dave Jones:** We've got two inputs, four possible combinations and you might notice if you know, well, you probably don't know binary if you're still watching this. This is a binary count from zero, one, two, three and I'm I have to do a separate video on binary on number systems.

**Dave Jones:** And the output is a function of these two inputs here. So, in this case an AND gate, the output is true or one only if both A and and get it, A and B are one.

**Dave Jones:** So, according to that rule are A and B one? No. So, it's not true. It's a zero. Is both A and B one in this case? No, it's not.

**Dave Jones:** Is A and B one in this case? No, it's not. Are both A and B one in this case? Yes. Bingo. And that is our truth table for the AND gate.

**Dave Jones:** The output here C is only true if both A and B inputs are true. That's it. And just like the name of the gate AND was descriptive of its functionality here, OR is also descriptive of its functionality.

**Dave Jones:** So, we go in and we write the exact same table that we had before. So, the combination of our inputs is exactly the same as the AND gate. So, we write down the four possible combinations.

**Dave Jones:** They don't have to be in this order, strictly speaking, but by convention they start at zero zero and count their way up depending on how many inputs you have.

**Dave Jones:** So, let's have a look at this. Now, the functionality of an OR gate is the output is true, i.e. the output is one, C is one, if A or or, get it?

**Dave Jones:** A or B is one. So, is A or B one in this case? Nope, they're both zero. So, our output is zero. Is either A or B one? Yes, B is a one, so our output's going to be one.

**Dave Jones:** Is A or B one? Yes, it is. And in the final case here, they're both one, but that's okay because it's an OR function. Is this one one or this one a one?

**Dave Jones:** Yes, so the output is one. That's our OR gate. And our inverter is incredibly easy, too. We only have one input A and we have one output B. We've only got two combinations of inputs, high or low, true or false, one or zero, and our output the name, once again, describes the function.

**Dave Jones:** Invert, so it inverts the Basically, it inverts you Polarity's not the correct term, but it inverts the function of the input. So, if it's a zero on the input, you get a one on the output.

**Dave Jones:** If it's a one on the input, you get a zero on the output. That simple. That's our inverter. Now, as far as two input gates go, AND and OR aren't the only ones.

**Dave Jones:** There's another special snowflake which I'll tell you about in a second, but the reason I mentioned these three first is because with AND ANDs or AND uh inverter gates, you can create any other gate or combination or digital system whatsoever.

**Dave Jones:** These three are the ones that you need to do all that. Actually, strictly speaking, that's not true. You only need the not and the or or the not and the and and you can create any other logic gate or logic system possible.

**Dave Jones:** Okay, so we're going to look at a kind of a special snowflake one here called the XOR or exclusive or. That's what the X stands for, exclusive because well, it's very exclusive gate.

**Dave Jones:** But it is also you know, a common gate used. So it should get a group together with the other types of two input gates. So and or and XOR are the three main types of two input gates.

**Dave Jones:** So let's take a look at the functionality. Once again, A B C It's easy as 1 2 3, simple as do re mi. Sorry, I shouldn't subject you to singing.

**Dave Jones:** We've got our inputs just like before. Oh, sorry, I forgot the It's not just a blank box like that. It's actually equals to one like that. That's our I IEC exclusive or symbol.

**Dave Jones:** So the exclusive or function is almost identical to the or function over here, but it's exclusive, which means that it has a special functionality. Now, just like the or gate, if A or B is one, then the output is one.

**Dave Jones:** But with the exclusive case, and I guess you can you know, have a different description for this, but the exclusive case of that only when A or B is one is the output one.

**Dave Jones:** So in this case, is A or B one? No, so we get a zero. Is A or B one? Yes, we get a one. Is A or B one?

**Dave Jones:** Yes, we get a one. Is A or B one? In this case, for the or gate, it would have been a high, but in this case, it's going to give us a zero.

**Dave Jones:** So this exclusive or is actually a very powerful function that allows us to do controlled inversion, which I might explain later. But yeah, they're our three types of two input gates, and or XOR with the not.

**Dave Jones:** Now, what we can do now is actually combine the not or inversion function with our other three two input gates to give us a what are called inverted two input gates.

**Dave Jones:** And these are called the NAND gate, the NOR gate, and the X Well, there we go. XNOR gate, and N for not. So, it's exactly the same, but we've added the symbol is now adding that not that circle on the output like that that I showed you before.

**Dave Jones:** So, that's actually equivalent to getting a physical uh AND gate like this and sticking an inverter on the output like that. In fact, you can do that. You can get a physical NAND gate chip, you can get a physical uh inverter chip, and you can put them like that, and it's exactly the same as buying a NAND gate chip like that, cuz that's all it contains inside the chip is it's got

**Dave Jones:** an extra inverter not circuit on the output. Now, you might think, "Hey, do we have to learn more truth tables for these gates up here, NAND, NOR, and XNOR?" Well, yes, you do.

**Dave Jones:** But, if you've learned the truth tables or you can derive the truth tables for AND, OR, and XOR here, then you can do the same for the NAND, because we've just added, remember, this inverter on the output.

**Dave Jones:** So, we can just take our output here, which is C, and what do we do? All our inputs will stay the same. They haven't changed. But, in this case, we'd have a one, one, one, and a zero.

**Dave Jones:** So, that is for our NAND function. So, that's all you have to do. And likewise here, one, zero, zero, zero, and one, zero, zero, one for the XNOR and the NOR gate.

**Dave Jones:** Simple, you just invert the output. So, let's actually look at a timing diagram because you're probably familiar with the oscilloscope where it displays voltage versus time. Well, we're just going to look at logic level versus time.

**Dave Jones:** So, let's uh take for example the uh whoop Let's take for example the NAND gate here like this, okay? We've got A B and C is our output. Now, I'm going to draw some signals in here.

**Dave Jones:** I'm just going to do these completely randomly and we'll see what we actually get out. So, if I go like this I don't know. Do there's a little grunty pulse like that and okay, we've got a signal on A like that and let's do B.

**Dave Jones:** I don't know. Haven't really thought about this at all. Let's see how it works out. So, let's look at these two waveforms and see what we get on our C output here using our truth table for the NAND gate.

**Dave Jones:** We started out okay, this is okay zero and one, okay? Zero and one and zero and one. So, let's have a look. They're both low, okay? You remember the output's only going to be high when both of them are high.

**Dave Jones:** So, it's going to be low like this and in this case we can sort of do some dashes down there like this to indicate the timing, okay? So, let's actually do the timing for each transition like this and we can go down and go across and do it.

**Dave Jones:** Now, we're following time here. So, this input is one, this input zero. So, according to the truth table we're still going to stay zero. It's only when we hit this point here where they're both one, bingo, that this will actually transition to a one like that and it'll stay one until this point here where uh the A input drops down low, so therefore the output must drop down low with it.

**Dave Jones:** And we won't see a high again until uh you guessed it, round about here, but it'll only stay because, if you follow that down, only a very brief period where they're both high, will that go high.

**Dave Jones:** But in this case, A has gone low, so that's going to stay low. Oops, it's going to go high again because they're both high. Look at that. And it's going to stay low and low and low until this point here, where it goes high, and down again.

**Dave Jones:** So, that is a timing diagram, and you can see the relationship. So, now, uh if you actually physically hooked this gate up on your breadboard and fed in two digital signals like this with this timing, you would get that waveform on the output.

**Dave Jones:** You'd get a you know, your 5 V or 3.3 V here, and your 0 V there. Too easy. So, you might have some ridiculously complicated logic circuit with hundreds or thousands of these gates.

**Dave Jones:** It's all going to follow these basic truth tables you've learned, nothing more. And there's no more magic to that. That's all there is to analyzing digital circuits. And likewise, if we had a NAND gate there instead of a uh AND gate, if we had a simple NAND gate, you guessed it, it would be the inverse of that because it's got that NOT on the output.

**Dave Jones:** Everything is totally Well, that was a bit how you doing there. There you go, totally inverted. You get the idea. Now, we get on to, and I'm hoping I don't lose people here, we get on to what's called Boolean algebra.

**Dave Jones:** Yes, algebra, uh but in a Boolean digital logic form. Now, So, this case, uh we would the output would not be called Well, it's still called C. It's labeled C here, but we'd put what's called a bar on top of it to signify that it's inverted.

**Dave Jones:** So, it's a not C output or an inverted C output. And these things will tie into Ooh, Boolean algebra. Let's go. Now, what we've been looking at here is what's called Boolean logic.

**Dave Jones:** Boolean Uh named after George Boole back in the 18 uh hundreds who came up with the idea that, you know, you can describe a system that's either one or zero, high or low, true or false.

**Dave Jones:** And that's So, this is Boolean logic, but now we're going to look at Boolean algebra and when how we can express all this sort of stuff, you know, practically in tables, we can actually express this mathematically.

**Dave Jones:** And trust me, it's not hard. Stick with me. So, just like we have mathematical operators you're familiar with, plus, minus, you know, multiply, divide, that sort of thing, we also have uh Boolean operators that describe the mathematics of Boolean logic.

**Dave Jones:** So, let's take the case of a simple NAND gate Oh, sorry, an AND gate here like this, okay? Input A, input B there, and our output um well, our output we labeled C before, but let's do this uh mathematically.

**Dave Jones:** The output is A AND AND is represented Here's the operator for AND as a dot. So, A AND B like that. And that's all there is to it. That is the Boolean algebra expression for the AND gate.

**Dave Jones:** Okay, so I'll just redraw that here. A AND B like that. And let's feed the output of this AND gate into the uh input of an OR gate, shall we?

**Dave Jones:** So, we'll draw our OR gate here. And let's call this input C because uh this input here is A and B. It's the output from that AND gate, and this one is just input that we'll call C.

**Dave Jones:** Now, what How do we describe mathematically this output here? Okay, we could call this output D, for example. I'd call it X or anything you want or just don't call it anything at all like we did here.

**Dave Jones:** It's just A and B. So, the expression for the output of this combinatorial logic, let's call cuz we've combined different logic gates. So, it's called combinatorial logic. So, D equals A and B or the operator, the Boolean algebra operator for the OR gate is a plus C.

**Dave Jones:** That's it. That is our Boolean algebra expression that describes this gate. So, you don't actually have to draw these gates. If you just said D equals A and B uh or C, then that describes the functionality of that circuit.

**Dave Jones:** It's very simple. Now, just like in uh regular arithmetic that you're used to, there's an order of operations. For example, you might be confused. Is this actually A and B or C, or is it A and B or C?

**Dave Jones:** I.e., do B and C go to the input of an OR gate first, or do they go to the input of an AND gate uh first? So, uh like B and C, is it like Are these things actually swapped around?

**Dave Jones:** Well, in this particular case, if you wanted to be really clear, you could put parentheses around A and B there to show that. But, in Boolean algebra, it's assumed that the A that the AND function is going to be performed first unless otherwise stated.

**Dave Jones:** So, you could actually, if we actually put A If we put parentheses around there like that, then that would imply that we actually had an or function like this, and we had B and C, and that was going into uh and and end function.

**Dave Jones:** Boom. With input A here like this. If you draw the parentheses like that. So, you know, the order of operators matters. So, if you want to be really clear, then put the parentheses in.

**Dave Jones:** Now, let's not forget the notch symbol, shall we? Let's say that we added an inverter on C input here like this. How would you describe that? Well, the inverter, like I said before, uses the bar approach.

**Dave Jones:** So, we will put a bar above C, and that signifies that it's inverted. That's all there is to it. And likewise, if we put a not on the output here of our uh entire function, so D, then we would put a bar right across the entire expression like that.

**Dave Jones:** Beautiful. So, that shows that we've got an inverter on the output. Fantastic. Okay, so our logical operators, you've seen the and is a dot, and the or is a plus, and the not is a bar on top of something.

**Dave Jones:** So, it'll be A and B, A or B, and just not A, or it could be A plus or A or B, and not that. But, we're forgetting the XOR gate, our special little snowflake here, um because it's pretty close to an or.

**Dave Jones:** It is A plus B. I shouldn't say plus, it's A or, but, you know, like it's habit. You see it and you say plus, even though you mean B.

**Dave Jones:** But because it's a special snowflake and we need to signify the XOR symbol is just a circle around the or or the plus. Easy. Okay, so let's forget Boolean algebra for for a minute.

**Dave Jones:** We'll come back to it in a second. Let's actually analyze a logic circuit like this, a combinatorial logic circuit. In this case, we've got three inputs A, B, C and we've got our output here.

**Dave Jones:** We'll call X for example. Now, I said before that you can have more than two inputs on any of the any of your two input gates, your NAND, NOR, your XOR, your NANDs, ANDs, ORs, exclusive or, all that sort of stuff.

**Dave Jones:** You can have more than one. In this case, I've got a three input AND gate. It's called. So, although you may not have actually seen the truth table for this, you can derive it because you would have an extra input over here on this table.

**Dave Jones:** So, you would, you know, you would go 0 0 0 0 and then you'd start 1 0 0 0 1 0 0 1 for example. And oh, what am I doing?

**Dave Jones:** There we go. 1 and 1 like that. So, you would just count up for a three input gate and you'd do the functions on the output. But once again, if all of all of the inputs are one, this input and this input and this input are one, then the output is one.

**Dave Jones:** So, let's try and work out what our output expression will be based on this input, shall we? So, let's have a look here. This is A and this is B.

**Dave Jones:** So, this is A and B. Okay? So, this is just a basic two input AND gate. Now, the output here is a little bit harder. What we've got is we've got not A like that and B and C.

**Dave Jones:** So, we've got these two Boolean algebra expressions now. Now, we can figure out what X is. So, X is equal to A and B or we'll put parentheses around these.

**Dave Jones:** A and B or because it's an or gate you guessed it the other expression on the input. A and B and C like that. Bingo. And say if this was a nor gate, well, it would be that function with a big not over the top of it.

**Dave Jones:** Beauty. So, that is basic digital logic and I'll call it quits there cuz this is long enough already and we'll need to expand this topic into Boolean logic simplification and how you can actually simplify your circuits using uh De Morgan's theorem and Karno maps and other uh techniques to actually uh simplify logic because you know, if you've got a 100 uh different gates in here, if you can get away with you know,

**Dave Jones:** minimizing that to 50 gates, then you're going to save either number of chips, you're going to save silicon space, you're going to save all that sort of jazz. But, I hope you learned basic introduction to digital logic there and it's not that hard at all.

**Dave Jones:** Once you know your basic uh logic gate types, there's not many of them. Learn how to derive the tables. Also, they're not hard to memorize because it's in the name.

**Dave Jones:** Um or and you know, exclusive or is probably the little uh special snowflake one in there, but it these things are not difficult at all. So, anyway, I hope you enjoyed that.

**Dave Jones:** If you did, please give it a big thumbs up and uh because this is the first video of this type, let me know what you think in the comments down below or over on the EEVblog forum.

**Dave Jones:** And if you'd like to see more of this content, possibly on a second channel. If you think that's a good idea, let me know. Anyway, hope you found it useful.

**Dave Jones:** Catch you next time.
