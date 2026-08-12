---
video_id: S3R4r2xvVYQ
title: EEVblog 1479 - Is Your Calculator WRONG?
url: https://www.youtube.com/watch?v=S3R4r2xvVYQ
source: youtube-asr
---

**Dave Jones:** Hi, it's calculator time and you know I love calculators. So, let's take a look at this Twitter question that popped up on my timeline from Nick's Craft who shows that like what the heck is going on here because the result from their

**Dave Jones:** Casio from for a simple equation does not match their shoe phone. So, what's going on? Let's try and explain it. So, let's get one of the latest Casio's here and let's repeat this. 6 / 2 and parenthesis open parenthesis and 2 + 1,

**Dave Jones:** right? So, you might think that 6 / 2, well, that's 3 and then well, there should be a multiply in there and that's 3 of course cuz you got to do inside the bracket. So, 3 * 3 should equal 9, but

**Dave Jones:** let's do equals on here and it gives us the answer of 1. What's going on? So, let's try that on my Android shoe phone here. 6 / 2 parenthesis 2 + 1 and it's already given us well, the answer there without

**Dave Jones:** closing the brackets. It's already given us the answer of 9. So, what's go Why does the shoe phone not match the Casio calculator? Well, it's an interesting question and it's not a bug. Now, you might think that this is

**Dave Jones:** just an issue with I don't know how like these modern shoe phones calculate things. Well, let's get another calculator, shall we? And this is a TI-30XS MultiView. So, let's give this a go. 6 / 2 parenthesis 2 + 1

**Dave Jones:** enter uh 9 and well, we can do that again just to make sure and again and again, it's going to give us the answer of 9. It matches the shoe phone. What's happening? So, what's going on here is

**Dave Jones:** obviously what's called operator priority or priority of calculations. There's many different terms for it, but basically what we've got here is we're implying a multiplication sign between the two and the parentheses here instead of putting it in explicitly, we're actually

**Dave Jones:** implying it. And that's called implied multiplication or sometimes juxtaposition multiplication because they're next to it just by the nature that they're next to each other, that's what it means. Anyway, we'll call it implied multiplication. So, if we actually

**Dave Jones:** repeat this and we put the multiplication in there, okay, it does give us still the result of nine. So, this Android calculator makes no distinction between an implied multiplication sign when it's not there or if you specifically put it in. They're the same

**Dave Jones:** priority of operation. So, obviously, you can completely come a cropper here if you don't know how your calculator works and know how to use it in order to give the result that you actually want. You should never assume that a

**Dave Jones:** calculator's going to work way because if you're used to this and you borrow your friend's TI and it gives you a different result or vice versa, then well, I don't know, your rocket crash-lands on Mars. But now, watch

**Dave Jones:** closely. This new Casio is actually really good. It helps out in this regard. It's actually telling you specifically what it's going to do. So, watch what happens here on the display as I press enter and evaluate that expression.

**Dave Jones:** Ta-da! Did you see it? It added an extra parentheses in here because this is what it's doing internally. And this is Casio's new way of actually telling you, "Hey, look, I specifically don't want to confuse you here, so I'm going to show

**Dave Jones:** you what I'm actually doing internally." So, it's added the parentheses here. So, what it's decided is that it's more important to evaluate this parenthesis first before doing 6 / 2. And that's why you get the answer one Because two

**Dave Jones:** multiplied by three here is six. Again, we actually have an implied multiplication in here, but because we've got the parentheses around here, it's it's not going to make a difference. We've essentially got it does two plus one, and I'll show you the

**Dave Jones:** order of operations in a minute, but it does two plus one first cuz anything inside a parentheses takes priority. So, it does that first. So, it does two plus one, which is three, multiplied implied multiplied by two, which is six. And six

**Dave Jones:** divided by six is, of course, one. So, this is not a bug. It's just the way that the calculator evaluates the expression and has an order of priority. In fact, this particular example seems to be so well known in the industry that

**Dave Jones:** Casio have actually included it in the manual. And here it is for the FX-991EX. And you can see it specifically gives the example here that we've got. And it it specifically tells you how it's going to evaluate it. And it specifically

**Dave Jones:** tells you it will deliberately include the parentheses in there. But why does it do that? And this is what you have to look for in your calculator manual for whether or not your calculator is actually going to do do this.

**Dave Jones:** Calculation priority sequence could be called you know, order of operations or something like that. The priority sequence of input calculations is evaluated in accordance with the rules below. Where when the priority of two expressions is the same, the calculation

**Dave Jones:** is performed from left to right. So, you might think that surely an implied multiplication in here is basically the same priority as a divide here. But it's actually not. Look at this. Number one is as I said, parenthetical expressions.

**Dave Jones:** Basically, anything in the parentheses. So, two plus one will get evaluated first. And then functions that have parentheses, so you know, functions sine, cos, tan, and all that. So, you have to get all the way down to priority

**Dave Jones:** number seven here until you find multiplication where the multiplication sign is admitted. So, they're saying that means implied multiplication or juxtaposition. Some manuals like TI for example might actually use the terminology like implied multiplication, but that's what they mean. So, that's

**Dave Jones:** priority seven and you have to get all the way down to priority 10 here before you get to multiplication and division. So, you can see that implied multiplication actually has a higher priority than just regular multiplication, which is

**Dave Jones:** why it inserts an extra parenthesis there because it's telling you specifically that it has a higher priority. It gives a higher priority to the implied multiplication than it does to the division. But if we put in the specific multiplier sign, we tell it

**Dave Jones:** exactly what we want instead of using parenthesis, we can go 6 / 2 and then multiplied by 2 + 1, we will get the answer 9 because we specifically put in the multiplication sign instead of it implying the multiplication. So, in this

**Dave Jones:** particular case, it's going, "Well, okay, you've used this multiplication sign. I know exactly what you're doing. There is no implied multiplication." So, it's going to do the multiplication first instead of using this higher priority. So, why on earth would a

**Dave Jones:** calculator treat an implied multiplication with a higher priority than a regular multiplication? Well, probably comes about from basic algebra and you almost certainly learned this. This is the what's called the distributive property and if you have A with a parenthesis and B + C, that's

**Dave Jones:** actually equal to A * B + A * c. The dot is the multiplication there. Now, although the calculator doesn't actually like rearrange it and calculate it this way, I don't know, maybe it might internally or something, but it

**Dave Jones:** certainly doesn't show you that. But, the point is this is how you would write an algebraic function on paper like this. So, the calculator actually sees that and goes, "Right, I'm going to put a bracket around like that, and I'm

**Dave Jones:** going to treat that as a function." And then that's going to take higher priority over any sort of like implied multiplication. And you'll see the same thing happen with something like this expression with an implied multiplication before the square root

**Dave Jones:** sign here. Now, the TI gives you the result of square root of 2 or 1.414. So, let's express this on the Casio. You can see that once again, it added the parentheses in there to show you what it's doing. And this is point 707. So,

**Dave Jones:** it's doing exactly the same thing. But, which one's right? Well, you saw that my Android shoe phone gave the result of 9, and this TI gives the result of 9 here. And if you use the Google calculator, it

**Dave Jones:** gives you a result of 9. And if you use Wolfram Alpha, it also gives you a result of 9. So, is there something weird going on with the Casios? Well, yes and no. Now, here's the original Casio FX-991EX

**Dave Jones:** over here in the original Twitter post, and it gives the result of 1. And of course, we've seen that the 991EX instead of MX, so it's the same series. It's the 991, but the MX and EX, it also

**Dave Jones:** gives you 1. But, what if we do the FX-991ES? Not MS, not EX, but ES. What happens? Press enter. Nine. What's going on here? This is nuts. We've got three FX-991 calculators. Two of them give a give the

**Dave Jones:** result of one, which is obviously using that distributive property, the higher priority for the implied multiplication, but the 991 ES works the same as the TI and like those online calculators. Huh? Well, this actually seems to come down

**Dave Jones:** to the markets that the calculators are sold in. Now, I believe the result of nine like this is a very specific American thing. It's a Yankee thing where like the educators in the US, they actually through their various

**Dave Jones:** textbooks, I don't know the history of how they were doing it or whatever, they actually give the same priority to an implied multiplication as they do to a regular multiplication, hence you get the result of nine. And I

**Dave Jones:** I assume that this Casio FX-991 ES is a model specifically for the American market. I believe Please correct me in the comments down below, but this is what I've been able to ascertain is that and I've found evidence of this from

**Dave Jones:** Casio themselves in another video which I'll I just found which I'll link in and they got a response from Casio themselves that saying, "Yeah, this is basically a North American thing." And if you want to actually sell calculators into that

**Dave Jones:** market, the American market, it's got to work like this and give you the result of nine. And this is why calculators are certified for exams. You'll have various, you know, like educational bodies actually verify calculators and certify them for a particular market.

**Dave Jones:** So, let's take this one. We've got a Casio two second edition. Ugh, goodness, Casio. Um, anyway, this one is as this is approved by the Board of Studies uh for the New Zealand QA for external examinations. I assume this is like

**Dave Jones:** Australian as well, cuz this is the AU model. This is the Australian model. So, let's see what this puppy does. 6 / 2 (2 + 1) and it gives us the result sure enough 1 and it added the extra

**Dave Jones:** parentheses in there. So, that works just like the other Casios I have, but this particular ES model is different and this is why this is not a bug. This is very deliberate. They deliberately choose the difference in the uh priority

**Dave Jones:** order of operations for different markets and America seems to be different to the rest of the world, but please leave it in the comments down below if what your calculator does um in your particular country. But, this sort of stuff is in

**Dave Jones:** the manual if you just hunt for it. Calculation priority sequence. So, you can know exactly what your calculator's going to do. It's going to follow this implied multiplication with a higher priority than it does for regular multiplication, but others like this TI

**Dave Jones:** over here, they won't. Here's the manual for that. It says that they're specifically the same. So, there you have it. Oh, by the way, I think some of the more modern TI ones actually um have a higher priority to the implied

**Dave Jones:** multiplication. So, uh yeah, I just don't have one here to show you, but there you go. I hope you found that video interesting and you got to be careful and know the order of priority of your calculations. But, of

**Dave Jones:** course, the best way to avoid any issues with this for the calculator and every calculator will then work the same is to not imply anything. As you know, the expression assumptions are the mother of all you know what's, right? So, 6 / 2

**Dave Jones:** multiplied. Put the multiple in there and then parentheses 2 + 1, and then you will get the result you will usually desire for 9. So, I probably all mathematicians are probably going to say this one is correct. That gives you the answer of

**Dave Jones:** one. But engineers, personally, I'm like old school. I think it should give a result of 9. Just as an aside, Casio came up with VPAM back in the '80s. Visually perfect algebraic method, it's called. And this was a

**Dave Jones:** technique to try and, you know, express things exactly. So, if you put 10 * sign, for example, you would have to press sign first before you actually put in the number. Whereas older non-VPAM calculators, which I greatly prefer, and you'll hear me in videos all

**Dave Jones:** the time saying, "Ah, none of that VPAM rubbish." Cuz I'm I'm old school in that regard. Then you would go 10 * 10, and then press the sign button. Whereas, you know, Casio decided, "No, we want things to

**Dave Jones:** match what they are on paper, so it doesn't confuse the kids, so the calculators don't operate in a different way to what you're seeing down on paper." And this isn't necessarily related to the implied multiplication, because as you saw here, okay, both of

**Dave Jones:** these are VPAM calculators, but they give a different result. So, yeah, you can't rely on just VPAM and non-VPAM actually giving you this. It's calculators for a specific market. Woo. Speaking of non-VPAM calculators, right? We've got a really old school one here,

**Dave Jones:** and we've got a more modern FX-260, which I've done a review and teardown of, by the way. Anyway, 6 / 2 ( 2 + 1 2 + 1 dirt = 2. Uh? Oh, god, we've got something different again. Try this on

**Dave Jones:** here. 6 / 2 ( 2 + 1 and what do we get? Two as well. So, what's happening here is when you do 6 / 2 like this and then don't press enter, but you press the parentheses, what it's doing is actually eliminating

**Dave Jones:** the digit you just typed in and then it's going 2 + 1 which evaluates to 3 and then it's going 6 / 3 is equal to 2 and we can see that in operation here. If we go 6 / 10 for example, (

**Dave Jones:** parentheses) 2 + 1 it gives us the same result. It's ignored that 10. It's wiped it out. So, that's just how non-VPAM calculators work. So, you could argue that's even worse than the argument we're having between whether it should

**Dave Jones:** be 9 or 1 that we use the order of priority thing here. That's just how these older school non-VPAM calculators work. Although, if we go back to my shoe phone here, this is using the Real Calc app which is what I actually use. It's

**Dave Jones:** supposed to have like a look and feel like of a Casio calculator, not like an exact emulator, but anyway, if we go 6 / 2 ( 2 + 1) it does actually give us nine. Just to throw a spanner in the

**Dave Jones:** works. I was going to throw this on the second channel, but I thought, "Nah, it's important enough to be on the main channel cuz you know, you could really come a gutter with this thing and you know, calculations are important in

**Dave Jones:** engineering and you could get them wrong when you're doing calculations on the fly like this and you're implying something, but your calculator should give you the right result if you tell it specifically what you want to do." So,

**Dave Jones:** anyway, if you enjoyed that video and found it interesting, please give it a big thumbs up. As always, discuss it down below and let us know if you've got oddball calculators cuz uh once again, it's not a brand thing as you saw like

**Dave Jones:** Casio do it in different ways depending on the market. TI I believe do the same thing and yeah, I know all the HP enter key fanboys are out there going what's this parenthesis rubbish? Catch you next time.
