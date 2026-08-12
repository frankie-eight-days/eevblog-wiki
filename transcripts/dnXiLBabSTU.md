---
video_id: dnXiLBabSTU
title: EEVblog #779 - Batteriser: How To Measure Battery Cutoff Voltage
url: https://www.youtube.com/watch?v=dnXiLBabSTU
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 30, "3": 45, "4": 60, "5": 74, "6": 87, "7": 99, "8": 110, "9": 123, "10": 138, "11": 152, "12": 165, "13": 179, "14": 193, "15": 205, "16": 220, "17": 233, "18": 245, "19": 257, "20": 275, "21": 294, "22": 315, "23": 329, "24": 346, "25": 361, "26": 376, "27": 391, "28": 407, "29": 420, "30": 434, "31": 450, "32": 462, "33": 476, "34": 490, "35": 504, "36": 518, "37": 531, "38": 548, "39": 565, "40": 580, "41": 600, "42": 617, "43": 632, "44": 646, "45": 659, "46": 671, "47": 686, "48": 702, "49": 720, "50": 736, "51": 752, "52": 761, "53": 773, "54": 791, "55": 808, "56": 822, "57": 839, "58": 854, "59": 868, "60": 885, "61": 906, "62": 920, "63": 933, "64": 946, "65": 962, "66": 977, "67": 992, "68": 1002, "69": 1016, "70": 1026, "71": 1041, "72": 1062, "73": 1076, "74": 1091, "75": 1103, "76": 1123, "77": 1140, "78": 1154, "79": 1169, "80": 1186, "81": 1202, "82": 1219, "83": 1233, "84": 1243, "85": 1255, "86": 1269, "87": 1284, "88": 1297, "89": 1313, "90": 1333, "91": 1350, "92": 1372, "93": 1390, "94": 1409, "95": 1424, "96": 1441, "97": 1459, "98": 1475, "99": 1488, "100": 1499, "101": 1517, "102": 1534, "103": 1547, "104": 1563, "105": 1583, "106": 1598, "107": 1615, "108": 1631, "109": 1644, "110": 1660, "111": 1674, "112": 1686, "113": 1697, "114": 1713, "115": 1727, "116": 1743, "117": 1759, "118": 1774, "119": 1786, "120": 1801, "121": 1817}
---

**Dave Jones:** Hi, in a recent video I demonstrated measuring the battery cutoff voltage in various electronic products. I think I did like 10 different products and got an average value of about 1 V or just over 1 V, something like that per cell

**Dave Jones:** for a typical modern electronics product. And everyone knows, yeah, that's uh pretty much how products are designed these days to have a battery cutoff voltage around about that 1 V figure. And as I've done in previous videos as well, the usable energy in a

**Dave Jones:** battery often about 0.8 V. So, if you want to maximize the battery life in your battery, you should design your product to work down to 0.8 V per cell. But, somebody put out a video claiming that I did it

**Dave Jones:** completely wrong, that it wasn't valid, and that you can't measure the cutoff voltage of a product with a power supply as I did it. And that's completely puzzling because not only is using an external power supply the correct way to

**Dave Jones:** do it, it's pretty much the only practical way to do it unless you want to actually sit there and watch the battery discharge itself. So, for the very few people who actually don't get it and think that using a power supply

**Dave Jones:** is the incorrect method, let's go through it and see why it is the correct method. Here's how you measure the battery cutoff voltage of your product. So, let's take a typical product, a symbol clapping monkey. Please excuse the crudity of the model, didn't have

**Dave Jones:** time to build it to scale or to paint it. Now, a typical product like this, when you shove the batteries in here, it does what monkeys do, and then it finally gets to a point where the product doesn't work anymore. Now, this

**Dave Jones:** could be it just stops clapping, or it could be an active modern product that actually monitors the battery voltage and tells you when it's finished, just like this wireless microphone I'm using right now to record this. It's got a low

**Dave Jones:** battery LED on here, and once that kicks in, well, you stop using the product, otherwise the functionality is not guaranteed. So, we're going to call that point the battery cutoff voltage. And as I showed in a previous video, for a

**Dave Jones:** modern electronic active electronic product, might be typically 1 V per cell. And if it you use multiple cells, multiple batteries in your product, then well, this is per cell voltage. And let's take it as 1 V. So, you might have

**Dave Jones:** some an active cutout detection circuit, a comparator for example, and a voltage reference inside your product that when your battery voltage gets down to that 1 V here, then it turns on your low battery detect LED or shuts down the

**Dave Jones:** product or you know, stops functionality, does whatever. So, how do you test this product, whether or not you designed it yourself or whether or not you've actually bought the product and you want to measure where it actually stops functioning, at what

**Dave Jones:** battery voltage? How do you do that? Well, there's actually only two ways to do it. One is to stick the battery in of course and then go in there and shove some probes up there and try and actually measure that itself or run some

**Dave Jones:** wires out and measure it. Or you can have the battery external and you just run some wires in like that and then you measure your voltage, your battery terminal voltage right at that point there cuz you want to eliminate any drop

**Dave Jones:** in the resistance in your leads like that. And well, you can sit there and wait for that voltage to discharge, discharge, and discharge until it gets to the point where your low battery detection LED comes on or the product

**Dave Jones:** stops working. And well, that can take a long time and that's why hardly anyone does it that way. That's why you use an external power supply. So, instead of hooking your battery up like that, you do exactly the same thing. You just

**Dave Jones:** hook it up to your power supply like that. And once again, ideally, you should measure the battery voltage right at the battery terminal there rather than relying on the uh, voltage measured on your power supply because there might

**Dave Jones:** be a small amount of resistance in there and maybe a tiny amount of contact resistance, but for a lowish power product, that really doesn't matter. You can actually rely on the voltage reading of your power supply. So, then you just

**Dave Jones:** drop the power supply voltage slowly until your low battery detect LED turns on or your product stops working. And then you can read off either from your power supply or if you're doing it because it's a high draw

**Dave Jones:** product, from a meter connected directly as close as possible to the battery terminals there. Bingo, you can read off the cut-off voltage. It's that simple. But, like I said, somebody, namely Batteriser, have put out a video saying that this is an incorrect method of

**Dave Jones:** measuring the cut-off voltage of a product. We have been asked questions about the validity of measuring the cut-off voltage of battery-operated devices with a power supply. Claiming that using a power supply to measure the cut-off voltage of a product

**Dave Jones:** is wrong and misleading at best. To use a power supply to show a battery-operated devices cut-off voltage, ignoring the battery's internal resistance, is wrong and misleading at best. Unbelievable. I'll show you why that statement is demonstrably untrue and using a power

**Dave Jones:** supply is the industry standard method for measuring the cut-off voltage of a battery and why it is equivalent to using the battery itself. Now, they claim that the reason it doesn't work and you can't use a power supply is that

**Dave Jones:** batteries are inherently different to power supplies. And yes, that is completely true, as I've explained in previous videos. A power supply effectively has zero internal resistance. It is designed to deliver large amounts of current over a large operational voltage range, so you can

**Dave Jones:** approximate any internal resistance to effectively zero. But, that's not the same for batteries. Take a a regular AA or AAA battery, for example. It's also got an internal resistance, just like a power supply has a tiny little bit, you

**Dave Jones:** know, like milliohms or something like that internal resistance. Well, a battery actually has quite a large internal resistance. It's also called the ESR, the equivalent series resistance, but we'll use the term IR for internal resistance of the battery.

**Dave Jones:** So, it's like having a little series resistor inside, physically inside your battery like this before it gets to the external contact like this. And the internal resistance for a AA or AAA battery is around about 100 to 300

**Dave Jones:** milliohms. 100 milliohms when it's fresh, 300-odd milliohms once it gets to its end of its discharge curve down here. And here's a graph from Duracell showing how that internal resistance changes with the battery discharge curve like this. And I'll just make mention of

**Dave Jones:** that the internal resistance, the ESR, of a battery is comprised of two different things. Now, I have done a video on this, which I'll link in down below. It is the combination of the electrical contact resistance. That's, you know,

**Dave Jones:** the little welds inside and all that sort of stuff, which is particularly relevant to a multi-cell battery like a 9-V battery, for example. That'll have six 4A cells inside it. There's all that extra contact resistance, and that's why

**Dave Jones:** the internal resistance of a 9-V battery is higher than a AA or single AA or AAA cell. But, it also, and most importantly, is also comprised of the what's called the ionic resistance. Now, this is a complex subject. It's the

**Dave Jones:** electrochemistry of the the cell itself. Now, I have actually done a video quite some time back looking at the ionic resistance of a battery. So, click here if you want to see that one. So, to keep this video

**Dave Jones:** simple, we won't get into the complex details of how the electrochemistry inside a battery works. Suffice it to say that you can actually simplify it to an equivalent series resistance and internal resistance value. And that's a common thing to do in the industry. You

**Dave Jones:** don't necessarily have to know how the chemistry works inside to know that the internal resistance of a battery causes a problem. So, okay. The internal resistance of a battery is much higher than a power supply. We're talking several orders of magnitude higher. So,

**Dave Jones:** wouldn't that make a difference when you're measuring measuring the battery cutoff voltage? Well, no, it's not. And here's why. It's a very simple and obvious thing. Now, let's assume that the uh lead resistance in here is negligible for both cases, okay? For the

**Dave Jones:** power supply and the internal resistance of the battery. This has 300 m internal resistance. Say this one has effectively zero. So, why doesn't it matter that this is 300 m and this is zero? It's because we can't measure that point and

**Dave Jones:** we can't measure that point in there of the cell. Well, we can, which I'll explain in a minute, but for the purposes of running the product, you can't. That's why I said you have to actually measure directly on the battery

**Dave Jones:** terminals of the product. And when you do that, when you measure on the battery terminals, that, by definition, okay, is the battery cutoff voltage of the product because you can't measure this value in here. It only matters what the

**Dave Jones:** value is in there because the internal circuitry you've got for your product actually has a voltage reference in there, and that's what's determining what shuts off your product. So, it's the battery. It's the voltage on the battery terminals here. It's got nothing to do

**Dave Jones:** with this internal resistance. It's a complete red herring. And the other reason why this internal resistance here doesn't matter for the cutoff voltage is because look at the data sheets for any battery at all. Every single data sheet

**Dave Jones:** for every battery ever produced shows a characteristic discharge curve that is under load, i.e. the voltage on the terminal of the battery after the internal resistance. They cannot give you a characteristic curve of effectively before that internal resistance. It doesn't exist. This

**Dave Jones:** internal resistance is all part of the electrochemistry inside the cell like this. So, it's meaningless to talk about the voltage of a battery when it's not loaded. So, I've shown here on this discharge characteristic curve here, the battery

**Dave Jones:** voltage when it's fresh for a single alkaline cell might start at say 1.6 V open circuit voltage. And that's why the I've got two curves here. The blue one is the loaded terminal voltage, i.e. the exact curve that you'd get in the data

**Dave Jones:** sheet for a given constant power drain constant current drain constant resistance drain or whatever it is. And then I've got a green curve in here, which is the unloaded terminal voltage, which is the curve you would get if you

**Dave Jones:** had to pull out your battery each time for your product, measure it with a multimeter, which is effectively an open load. There's no load on it, and measure the unloaded voltage, then put it back in your product, and then a minute later

**Dave Jones:** take it back out, and measure the battery voltage again, unloaded. Okay? So, you can actually get two characteristic curves like that. So, the green one, of course, is going to have a higher voltage because when you put a

**Dave Jones:** load on a battery like this, this internal resistance, of course, Ohm's law, it's going to drop some voltage, and that voltage is going to be the differential between those two curves there. So, this is why it's fundamentally and demonstrably wrong to

**Dave Jones:** measure the open circuit unloaded voltage of a battery when you're talking about discharge curves, battery cut off voltages, and everything else because it's meaningless because you're not loading down the product and you're actually not taking into account that

**Dave Jones:** internal resistance. It It's so fundamentally wrong. Nobody in the industry does it like that. You can't. It's wrong. And as I said, and I'll repeat, this is why the manufacturers only publish loaded voltage curves because all you can get is this terminal

**Dave Jones:** voltage here. And when you design a product, all that matters All that matters is the voltage on those terminals. And this is why it's fundamentally correct to use a power supply to measure the cut off voltage of a product because you're effectively

**Dave Jones:** You've got zero ohms in there, okay? You're putting that voltage. You're forcing the voltage right onto the terminals there. You've got no internal resistance whatsoever. So, you're actually measuring the true uh cut off voltage of the product by doing that.

**Dave Jones:** And like I said, if you really want to, yes, you can use the real battery and you can hook it up to the product and you can sit there, twiddle your thumbs, and wait and wait and wait days, months,

**Dave Jones:** a year, or whatever until it happens to get down to the cut off voltage of your product, but nobody's got time to do that. So, you just hook up a power supply. It is fundamentally the correct way to do it.

**Dave Jones:** So, if you remove your battery from the product after you've used it and then measure the terminal voltage with your multimeter, which is an open uh circuit, then what you're measuring is this green characteristic curve here effectively. You're measuring it by not taking into

**Dave Jones:** account the ESR when the product's actually being powered. What is the point of that? It It's It's just completely silly and actually fundamentally wrong. All that matters is the battery voltage there on the terminals when it's under load?

**Dave Jones:** Of course, that's the only thing that matters, because that's what you're testing. You're testing the product during its operation. So, if you take the battery out, and your battery voltage recovers because there's no current flowing through your battery

**Dave Jones:** like that to give an internal drop, that is not an accurate measurement. This is fundamental stuff. This is hobby-level stuff. I learned this when I was like 7 years old. It's not hard to measure the battery voltage not under load

**Dave Jones:** is demonstrably wrong. You cannot argue it. You cannot argue it. To do so is just to make a complete fool of yourself. So, by saying that batteries are different to power supplies, yes, they are, but that is a completely

**Dave Jones:** pointless statement when you're talking about battery cutoff voltage, cuz as I said, all that matters is the terminal voltage here. So, yes, they're different. So, using the power supply to measure the cutoff voltage is actually taking into account the internal

**Dave Jones:** resistance of this battery, unlike the claim that they're made that it's not taken into account the internal resistance. It is. It fundamentally is. I don't know how much simpler I can explain it. It's just Ah. So, let's actually go and take a

**Dave Jones:** look at this Batteriser response video, because it is actually a direct response to my debunking video, and also my Batteriser explained blog article down here. So, let's have a look. They've actually confusingly made two different videos here with this clapping monkey

**Dave Jones:** thing trying to prove that my using a power supply to measure the cutoff voltage is incorrect. But really, there doesn't seem to be any major difference between the two except the ending why they've called this one a conclusion here. So,

**Dave Jones:** we're going to take a look it. Curiously, it is on not at the Batteriser's YouTube channel, but the Batteriser Batteroo channel, which they actually claim, if you go to the about tab, "Disclaimer, we are not in any way

**Dave Jones:** affiliated with Batteriser or Batteroo. We are simply a fan page." Yet, it has all their official videos and everything else. And they also talk in the first person that they're "Thanks to all our supporters, blah, blah, blah." I don't

**Dave Jones:** get it. And by the way, if you're after some laughs, go and look at these uh supposed fan submitted videos, these professionally produced fan submitted videos here, which extol the virtues of the Batteriser. Oh, goodness, there's even nature man

**Dave Jones:** down here. Crikey. Because they do make very specific uh claims on this video that the Batteriser has come under skepticism due to a flawed test, i.e., my test, in which a power supply was used to debunk the Batteriser. There is

**Dave Jones:** no other video out there, so they're obviously uh this is a response to my video. So, I'm happily making this response video to their video. And by the way, I tried to comment on uh their most recent video, but they deleted my

**Dave Jones:** comment. Well, but I'm more than happy to have them uh come on to my videos and and discuss it all they want. Leave all the comments they like. I don't delete comments. I don't uh delete comments on the forum or

**Dave Jones:** my blog uh sites. So, they're welcome to come in and discuss it any time they like. And in this Yahoo Makers article, uh they interviewed uh Batteriser and uh Mr. Roopavah. Um this is what he had to say about me. Discussing the EV blog

**Dave Jones:** video, he says, "I think he's a good guy." Oh, thank you. I'm sure you're a good guy, too. I just think he didn't know enough.

**Dave Jones:** Really? I don't know enough? Like I just showed that using a power supply is the correct industry standard method for measuring battery cutoff voltage, and you're claiming it's not. You're basically the only one on the planet who claims it's not and I don't know what

**Dave Jones:** I'm talking about. Okay. Well, at least I know enough not to go around claiming that there's 1.5 volts of energy and that many devices stop functioning around the 1.3 volt mark. Goodness. And then when everyone including myself had to try and tell you

**Dave Jones:** that no, the cut out voltage of a product is about 1.1 volts under load and you finally came out on your website and here it is I screen captured it. You admitted that the secret is that most 1.5 volt batteries drain to about 1.1

**Dave Jones:** volts under load. Thank you for agreeing with me. But then of course you went and removed that and changed it and removed any reference to that 1.1 volts. But thankfully it's still in your frequently asked questions down in here. At least

**Dave Jones:** you left it in and admitted that products do actually cut out at 1.1 volts. I'm glad I was right about that in my video. So let's look at their final conclusion again. To use a power supply to show a battery

**Dave Jones:** operated devices cut off voltage ignoring the batteries internal resistance is wrong and misleading at best. Batteries behave different from power supplies. Well, I just spent the last 15 minutes explaining that yes, batteries do behave different from power supplies, but

**Dave Jones:** what's your point? You're not stating anything of value there whatsoever. It's basically just one big straw man argument to set up the idea that yes, you're technically right. Batteries are different from power supplies and then somehow that proves and debunks my

**Dave Jones:** entire debunking video because I got it wrong. But yet never once in the video as we'll see do you actually explain how to measure the cut off voltage. So let's go and have a look at the rest of the

**Dave Jones:** video and see how you sort of try and justify this. Oh, I won't show the whole thing. I'll just cut out various parts that aren't actually relevant. Power supplies can source a huge amount of current while maintaining constant

**Dave Jones:** output voltage. Batteries, on the other hand, are not capable of maintaining a constant voltage when it is connecting to a device that draws current. Due to the internal resistance of the battery, its terminal voltage will drop when connecting to a device.

**Dave Jones:** Well, yeah, of course. That's why I explained in the video that all that matters is measuring measuring the actual terminal voltage battery terminal voltage of the product under test while it's operating, i.e., under load. This is precisely the reason why battery

**Dave Jones:** manufacturers publish discharge curves under load because that's the only measurement that matters and it takes into account the internal resistance. Oh, so you're interested in this monkey. First of all, who is this guy? It says on the YouTube video that he's a

**Dave Jones:** professor of electrical engineering. Okay, I'm sure he is, but hey, I can't believe he's saying this. So, first I got to set it to 3 volts because each battery is 1 and 1/2 volts. Now, I don't know about you, but uh take

**Dave Jones:** a look at this uh soldering iron here. This well as soldering iron looks like it's never been used. And who the hell just leaves the thing lying on a bench like that? And where is the solder? If I

**Dave Jones:** didn't know any better, I'd say that they just set up this bench as a just a promo video shot. And I just couldn't help but notice the oscilloscope. Look at the square wave they've got there and you can see that all they're doing is

**Dave Jones:** measuring the compensation on the front of the scope and it's probably the worst compensation I've ever seen. They don't even know how to compensate the probe. Hilarious. Sorry, had to point it out. So, we got the power supply set at 3

**Dave Jones:** volts. Now, we can see how he behaves at the same voltage as two fresh batteries. Oh, yeah. Nope, I'm sorry. It's not the same as the voltage of the two fresh batteries because it's not taking into account the

**Dave Jones:** internal resistance of the battery, which will cause a drop. It's unbelievable. You make the claim that I'm wrong cuz I'm not taking into account the internal resistance of the battery. You're the one who's not taking into account the internal resistance of

**Dave Jones:** the battery. Oh. So, now let's turn it down to 2 and 1/2 volts. Still moving and making a lot of noise. And again, still making a lot of noise at 2 volts.

**Dave Jones:** Down at 1 and 1/2 volts, he's starting to slow down a little bit. And slowly going down on the voltage. And he's stopped moving at 0.9 volts. This demonstration shows that with a power supply, the monkey will operate

**Dave Jones:** even when we bring the voltage down all the way to 0.9 volts. Wow, that's pretty awesome, isn't it? I love this monkey. Can work down to 0.45 volts per cell. Incredible. Awesome. However, when using two batteries with a

**Dave Jones:** total voltage of 2.5 volts, the monkey will not operate. We checked the voltages of two used batteries. The first battery voltage measured at 1.231 volts. What are you doing? You do not measure the battery voltage when it's not under

**Dave Jones:** load. It does not tell you you're not taking into account the internal resistance. As I said, this is hobby level stuff. This is battery 101 stuff. For a professor to not know that you can't do this is just ah, it's

**Dave Jones:** incredible. These are used batteries. You don't know how much energy is left in that battery, how much the internal resistance is going to affect the monkey under test. We measured the second battery at 1.267 volts. This monkey uses two batteries in

**Dave Jones:** series. So, you have to add the voltages together, resulting in 2.5 volts being supplied to the monkey. 2.5 volts is not being supplied to the monkey. Because when you turn the monkey on, it is a load. It loads down the

**Dave Jones:** voltage voltage. You get a drop on the internal resistance. Unless you measure the voltage on the terminals of the battery probe right up the monkey's ass, you are not measuring anything. This is just so fundamentally wrong. It's just

**Dave Jones:** what Oh, go. Look, you even say this on your own website. Here's your frequently asked questions where you quote Wikipedia. Look, when the source delivers current, the measured voltage output is lower lower than the no load voltage, which is

**Dave Jones:** what you just measured. You measured the no load voltage, and you're saying that 2. That no load voltage is being delivered to the monkey. Unbelievable. How you can possibly say this in the video when your own frequently asked

**Dave Jones:** questions where you try and explain this says completely the opposite thing where the internal resistance of the battery, as I've just spent 15 minutes explaining, will actually cause a drop, and you won't get it as you claim that

**Dave Jones:** 2.5 volts. It's going to be much much lower, causing the monkey potentially not to operate at all, as we'll see in a second. Duh.

**Dave Jones:** And then flip it to on. And you saw it tried to go, but stopped. So, we'll see if it if it can go you know, second time. Just give it another shot. Yep, it it tries, but it can't it can't

**Dave Jones:** go. Well, that's not the least bit surprising. This is a high drain device, this clapping monkey, and obviously the internal resistance of those because you're using already, you know, half dead or 3/4 dead batteries or whatever, that it does not have the capability to

**Dave Jones:** power the monkey cuz there's too much loss in the internal resistance. And this is completely obvious. The entire premise of your video has been to show that there is a difference between a power supply and a battery. As I

**Dave Jones:** explained right at the start of my video, of course there is. But this does not explain why at all. There is nothing in this video to explain why using a power supply is the incorrect method for determining battery cutout voltage,

**Dave Jones:** which is all that matters. You haven't even done the fundamental first principle thing of measuring the battery voltage, putting the probes in there when the batteries are in there. This is an unbelievable beginner mistake. It's so embarrassing. If you did this at a job interview,

**Dave Jones:** you'd be booted right out the door. If you did this in made this mistake in an exam, you'd fail. If you made this mistake in a job, you'd you'd be booted out. Or they'd looked at very strangely. It's As I said, this is hobby

**Dave Jones:** level understanding to measure the battery voltage under load. It's absolutely incredible. This is one of the greatest straw man arguments I've ever seen. It is just facepalmly dumb. It really is. But if you didn't know any better you'd take this video and go yeah

**Dave Jones:** that sounds okay. But it's just fundamentally wrong. Just take a look at this Energizer double a battery sheet. It shows the industry standard test for different types of products toothbrushes portable lighting and toy in this case. You know this clapping monkey yeah it

**Dave Jones:** might get 8 or 10 hours life or something like that. So look at that discharge curve of that toy. This is under load like it high discharge current every time it it bangs those symbols together it it's just going to

**Dave Jones:** die because of the internal resistance of the battery it can't recover. There's no more not enough useful energy left to actually provide enough voltage to operate the device given the required current draw. And if you actually did this test properly and

**Dave Jones:** actually measured the battery terminal voltage inside the monkey when it was operating you would see it actually drop below that that point four five volts or what it per cell or whatever it was that you measured with the power supply.

**Dave Jones:** That's how this testing works. That's how I spent 15 minutes explaining it to you. didn't do the right test. You didn't probe it. All you did is shove the batteries in there. See it doesn't work. Of course it

**Dave Jones:** doesn't work because it's a pulse load. Look at the thing for the toy here. It's designed to be one hour per day. You put in those used batteries in the toy and start to deliver a pulse load. The

**Dave Jones:** electrochemistry inside the ionic resistance cannot deliver a low enough resistance in order to clap those symbols. Battery 101 stuff. And of course you would expect the monkey to work with the power supply because it's got no internal resistance.

**Dave Jones:** It's an ideal battery. So it's going to deliver as much current as needed as much pulse current as needed. There's no ionic resistance in there. Of course batteries are different. You stated the bleeding obvious in this video and then

**Dave Jones:** trying to claim that the whole method of using a power supply is wrong. Clearly do not fundamentally understand the concept of measuring this. Unbelievable. There's not a single credible engineer in the industry who will agree with this video. Not a single

**Dave Jones:** one. Go find me one, please. Prove me wrong. So, that's it. I've had enough. I don't know what more to say about this laughable straw man video. It is It's got to be a parody. Surely the the joke's on all of us. It

**Dave Jones:** This guy They cannot be serious. I don't know how anyone could put their name forward and actually say this sort of stuff. If I said this, I'd be laughed out of the industry. Anyway, leave your comments down below. I'll

**Dave Jones:** link to the forum down below where you can discuss this thing. And as I said, Batteriser, more than welcome to come in here and discuss it and try and prove I'm wrong. I'm happy to always be corrected. I won't delete your comments,

**Dave Jones:** unlike what you did to me. So, I didn't really want to do this video. I'd had enough of the Batteriser and their silly claims, but I just couldn't let it stand. They were presenting fundamentally wrong and misleading information. Exactly the claim they made

**Dave Jones:** about my video, but in this case, it's demonstrably true that they are incorrect here and being deceptive. It's fundamentally wrong. There's no way anyone can stand behind this. They should be totally embarrassed. If I did this, I'd be I wouldn't be able to

**Dave Jones:** make another video again. I'd be laughed out of the industry. Unbelievable. Anyway, this is my response. Hope you enjoyed it. Hope you found it interesting and educational. Catch you next time.
