---
video_id: S3R4r2xvVYQ
title: EEVblog 1479 - Is Your Calculator WRONG?
url: https://www.youtube.com/watch?v=S3R4r2xvVYQ
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 32, "3": 41, "4": 52, "5": 70, "6": 81, "7": 101, "8": 127, "9": 139, "10": 156, "11": 172, "12": 183, "13": 202, "14": 219, "15": 232, "16": 250, "17": 260, "18": 277, "19": 288, "20": 303, "21": 317, "22": 335, "23": 351, "24": 374, "25": 391, "26": 419, "27": 437, "28": 451, "29": 459, "30": 473, "31": 495, "32": 510, "33": 518, "34": 533, "35": 542, "36": 560, "37": 577, "38": 598, "39": 612, "40": 633, "41": 660, "42": 670, "43": 682, "44": 698, "45": 714, "46": 725, "47": 743, "48": 761, "49": 774, "50": 785, "51": 799, "52": 820, "53": 834, "54": 851, "55": 862, "56": 889, "57": 904, "58": 916, "59": 952, "60": 965, "61": 981, "62": 989, "63": 1006, "64": 1024, "65": 1033, "66": 1047}
---

**Dave Jones:** Hi, it's calculator time and you know I love calculators. So, let's take a look at this Twitter question that popped up on my timeline from Nick's Craft who shows that like what the heck is going on here because the result from their Casio from for a simple equation does not match their shoe phone.

**Dave Jones:** So, what's going on? Let's try and explain it. So, let's get one of the latest Casio's here and let's repeat this. 6 / 2 and parenthesis open parenthesis and 2 + 1, right?

**Dave Jones:** So, you might think that 6 / 2, well, that's 3 and then well, there should be a multiply in there and that's 3 of course cuz you got to do inside the bracket.

**Dave Jones:** So, 3 * 3 should equal 9, but let's do equals on here and it gives us the answer of 1. What's going on? So, let's try that on my Android shoe phone here.

**Dave Jones:** 6 / 2 parenthesis 2 + 1 and it's already given us well, the answer there without closing the brackets. It's already given us the answer of 9. So, what's go Why does the shoe phone not match the Casio calculator?

**Dave Jones:** Well, it's an interesting question and it's not a bug. Now, you might think that this is just an issue with I don't know how like these modern shoe phones calculate things.

**Dave Jones:** Well, let's get another calculator, shall we? And this is a TI-30XS MultiView. So, let's give this a go. 6 / 2 parenthesis 2 + 1 enter uh 9 and well, we can do that again just to make sure and again and again, it's going to give us the answer of 9.

**Dave Jones:** It matches the shoe phone. What's happening? So, what's going on here is obviously what's called operator priority or priority of calculations. There's many different terms for it, but basically what we've got here is we're implying a multiplication sign between the two and the parentheses here instead of putting it in explicitly, we're actually implying it.

**Dave Jones:** And that's called implied multiplication or sometimes juxtaposition multiplication because they're next to it just by the nature that they're next to each other, that's what it means. Anyway, we'll call it implied multiplication.

**Dave Jones:** So, if we actually repeat this and we put the multiplication in there, okay, it does give us still the result of nine. So, this Android calculator makes no distinction between an implied multiplication sign when it's not there or if you specifically put it in.

**Dave Jones:** They're the same priority of operation. So, obviously, you can completely come a cropper here if you don't know how your calculator works and know how to use it in order to give the result that you actually want.

**Dave Jones:** You should never assume that a calculator's going to work way because if you're used to this and you borrow your friend's TI and it gives you a different result or vice versa, then well, I don't know, your rocket crash-lands on Mars.

**Dave Jones:** But now, watch closely. This new Casio is actually really good. It helps out in this regard. It's actually telling you specifically what it's going to do. So, watch what happens here on the display as I press enter and evaluate that expression.

**Dave Jones:** Ta-da! Did you see it? It added an extra parentheses in here because this is what it's doing internally. And this is Casio's new way of actually telling you, "Hey, look, I specifically don't want to confuse you here, so I'm going to show you what I'm actually doing internally."

**Dave Jones:** So, it's added the parentheses here. So, what it's decided is that it's more important to evaluate this parenthesis first before doing 6 / 2. And that's why you get the answer one Because two multiplied by three here is six.

**Dave Jones:** Again, we actually have an implied multiplication in here, but because we've got the parentheses around here, it's it's not going to make a difference. We've essentially got it does two plus one, and I'll show you the order of operations in a minute, but it does two plus one first cuz anything inside a parentheses takes priority.

**Dave Jones:** So, it does that first. So, it does two plus one, which is three, multiplied implied multiplied by two, which is six. And six divided by six is, of course, one.

**Dave Jones:** So, this is not a bug. It's just the way that the calculator evaluates the expression and has an order of priority. In fact, this particular example seems to be so well known in the industry that Casio have actually included it in the manual.

**Dave Jones:** And here it is for the FX-991EX. And you can see it specifically gives the example here that we've got. And it it specifically tells you how it's going to evaluate it.

**Dave Jones:** And it specifically tells you it will deliberately include the parentheses in there. But why does it do that? And this is what you have to look for in your calculator manual for whether or not your calculator is actually going to do do this.

**Dave Jones:** Calculation priority sequence could be called you know, order of operations or something like that. The priority sequence of input calculations is evaluated in accordance with the rules below. Where when the priority of two expressions is the same, the calculation is performed from left to right.

**Dave Jones:** So, you might think that surely an implied multiplication in here is basically the same priority as a divide here. But it's actually not. Look at this. Number one is as I said, parenthetical expressions.

**Dave Jones:** Basically, anything in the parentheses. So, two plus one will get evaluated first. And then functions that have parentheses, so you know, functions sine, cos, tan, and all that. So, you have to get all the way down to priority number seven here until you find multiplication where the multiplication sign is admitted.

**Dave Jones:** So, they're saying that means implied multiplication or juxtaposition. Some manuals like TI for example might actually use the terminology like implied multiplication, but that's what they mean. So, that's priority seven and you have to get all the way down to priority 10 here before you get to multiplication and division.

**Dave Jones:** So, you can see that implied multiplication actually has a higher priority than just regular multiplication, which is why it inserts an extra parenthesis there because it's telling you specifically that it has a higher priority.

**Dave Jones:** It gives a higher priority to the implied multiplication than it does to the division. But if we put in the specific multiplier sign, we tell it exactly what we want instead of using parenthesis, we can go 6 / 2 and then multiplied by 2 + 1, we will get the answer 9 because we specifically put in the multiplication sign instead of it implying the multiplication.

**Dave Jones:** So, in this particular case, it's going, "Well, okay, you've used this multiplication sign. I know exactly what you're doing. There is no implied multiplication." So, it's going to do the multiplication first instead of using this higher priority.

**Dave Jones:** So, why on earth would a calculator treat an implied multiplication with a higher priority than a regular multiplication? Well, probably comes about from basic algebra and you almost certainly learned this.

**Dave Jones:** This is the what's called the distributive property and if you have A with a parenthesis and B + C, that's actually equal to A * B + A * c.

**Dave Jones:** The dot is the multiplication there. Now, although the calculator doesn't actually like rearrange it and calculate it this way, I don't know, maybe it might internally or something, but it certainly doesn't show you that.

**Dave Jones:** But, the point is this is how you would write an algebraic function on paper like this. So, the calculator actually sees that and goes, "Right, I'm going to put a bracket around like that, and I'm going to treat that as a function." And then that's going to take higher priority over any sort of like implied multiplication.

**Dave Jones:** And you'll see the same thing happen with something like this expression with an implied multiplication before the square root sign here. Now, the TI gives you the result of square root of 2 or 1.414.

**Dave Jones:** So, let's express this on the Casio. You can see that once again, it added the parentheses in there to show you what it's doing. And this is point 707.

**Dave Jones:** So, it's doing exactly the same thing. But, which one's right? Well, you saw that my Android shoe phone gave the result of 9, and this TI gives the result of 9 here.

**Dave Jones:** And if you use the Google calculator, it gives you a result of 9. And if you use Wolfram Alpha, it also gives you a result of 9. So, is there something weird going on with the Casios?

**Dave Jones:** Well, yes and no. Now, here's the original Casio FX-991EX over here in the original Twitter post, and it gives the result of 1. And of course, we've seen that the 991EX instead of MX, so it's the same series.

**Dave Jones:** It's the 991, but the MX and EX, it also gives you 1. But, what if we do the FX-991ES? Not MS, not EX, but ES. What happens? Press enter.

**Dave Jones:** Nine. What's going on here? This is nuts. We've got three FX-991 calculators. Two of them give a give the result of one, which is obviously using that distributive property, the higher priority for the implied multiplication, but the 991 ES works the same as the TI and like those online calculators.

**Dave Jones:** Huh? Well, this actually seems to come down to the markets that the calculators are sold in. Now, I believe the result of nine like this is a very specific American thing.

**Dave Jones:** It's a Yankee thing where like the educators in the US, they actually through their various textbooks, I don't know the history of how they were doing it or whatever, they actually give the same priority to an implied multiplication as they do to a regular multiplication, hence you get the result of nine.

**Dave Jones:** And I I assume that this Casio FX-991 ES is a model specifically for the American market. I believe Please correct me in the comments down below, but this is what I've been able to ascertain is that and I've found evidence of this from Casio themselves in another video which I'll I just found which I'll link in and they got a response from Casio themselves that saying, "Yeah, this is basically a

**Dave Jones:** North American thing." And if you want to actually sell calculators into that market, the American market, it's got to work like this and give you the result of nine.

**Dave Jones:** And this is why calculators are certified for exams. You'll have various, you know, like educational bodies actually verify calculators and certify them for a particular market. So, let's take this one.

**Dave Jones:** We've got a Casio two second edition. Ugh, goodness, Casio. Um, anyway, this one is as this is approved by the Board of Studies uh for the New Zealand QA for external examinations.

**Dave Jones:** I assume this is like Australian as well, cuz this is the AU model. This is the Australian model. So, let's see what this puppy does. 6 / 2 (2 + 1) and it gives us the result sure enough 1 and it added the extra parentheses in there.

**Dave Jones:** So, that works just like the other Casios I have, but this particular ES model is different and this is why this is not a bug. This is very deliberate.

**Dave Jones:** They deliberately choose the difference in the uh priority order of operations for different markets and America seems to be different to the rest of the world, but please leave it in the comments down below if what your calculator does um in your particular country.

**Dave Jones:** But, this sort of stuff is in the manual if you just hunt for it. Calculation priority sequence. So, you can know exactly what your calculator's going to do. It's going to follow this implied multiplication with a higher priority than it does for regular multiplication, but others like this TI over here, they won't.

**Dave Jones:** Here's the manual for that. It says that they're specifically the same. So, there you have it. Oh, by the way, I think some of the more modern TI ones actually um have a higher priority to the implied multiplication.

**Dave Jones:** So, uh yeah, I just don't have one here to show you, but there you go. I hope you found that video interesting and you got to be careful and know the order of priority of your calculations.

**Dave Jones:** But, of course, the best way to avoid any issues with this for the calculator and every calculator will then work the same is to not imply anything. As you know, the expression assumptions are the mother of all you know what's, right?

**Dave Jones:** So, 6 / 2 multiplied. Put the multiple in there and then parentheses 2 + 1, and then you will get the result you will usually desire for 9. So, I probably all mathematicians are probably going to say this one is correct.

**Dave Jones:** That gives you the answer of one. But engineers, personally, I'm like old school. I think it should give a result of 9. Just as an aside, Casio came up with VPAM back in the '80s.

**Dave Jones:** Visually perfect algebraic method, it's called. And this was a technique to try and, you know, express things exactly. So, if you put 10 * sign, for example, you would have to press sign first before you actually put in the number.

**Dave Jones:** Whereas older non-VPAM calculators, which I greatly prefer, and you'll hear me in videos all the time saying, "Ah, none of that VPAM rubbish." Cuz I'm I'm old school in that regard.

**Dave Jones:** Then you would go 10 * 10, and then press the sign button. Whereas, you know, Casio decided, "No, we want things to match what they are on paper, so it doesn't confuse the kids, so the calculators don't operate in a different way to what you're seeing down on paper." And this isn't necessarily related to the implied multiplication, because as you saw here, okay, both of these are VPAM calculators, but they

**Dave Jones:** give a different result. So, yeah, you can't rely on just VPAM and non-VPAM actually giving you this. It's calculators for a specific market. Woo. Speaking of non-VPAM calculators, right?

**Dave Jones:** We've got a really old school one here, and we've got a more modern FX-260, which I've done a review and teardown of, by the way. Anyway, 6 / 2 ( 2 + 1 2 + 1 dirt = 2.

**Dave Jones:** Uh? Oh, god, we've got something different again. Try this on here. 6 / 2 ( 2 + 1 and what do we get? Two as well. So, what's happening here is when you do 6 / 2 like this and then don't press enter, but you press the parentheses, what it's doing is actually eliminating the digit you just typed in and then it's going 2 + 1 which evaluates to 3

**Dave Jones:** and then it's going 6 / 3 is equal to 2 and we can see that in operation here. If we go 6 / 10 for example, ( parentheses) 2 + 1 it gives us the same result.

**Dave Jones:** It's ignored that 10. It's wiped it out. So, that's just how non-VPAM calculators work. So, you could argue that's even worse than the argument we're having between whether it should be 9 or 1 that we use the order of priority thing here.

**Dave Jones:** That's just how these older school non-VPAM calculators work. Although, if we go back to my shoe phone here, this is using the Real Calc app which is what I actually use.

**Dave Jones:** It's supposed to have like a look and feel like of a Casio calculator, not like an exact emulator, but anyway, if we go 6 / 2 ( 2 + 1) it does actually give us nine.

**Dave Jones:** Just to throw a spanner in the works. I was going to throw this on the second channel, but I thought, "Nah, it's important enough to be on the main channel cuz you know, you could really come a gutter with this thing and you know, calculations are important in engineering and you could get them wrong when you're doing calculations on the fly like this and you're implying something, but your calculator should

**Dave Jones:** give you the right result if you tell it specifically what you want to do." So, anyway, if you enjoyed that video and found it interesting, please give it a big thumbs up.

**Dave Jones:** As always, discuss it down below and let us know if you've got oddball calculators cuz uh once again, it's not a brand thing as you saw like Casio do it in different ways depending on the market.

**Dave Jones:** TI I believe do the same thing and yeah, I know all the HP enter key fanboys are out there going what's this parenthesis rubbish? Catch you next time.
