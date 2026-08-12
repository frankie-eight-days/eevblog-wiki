---
video_id: dnXiLBabSTU
title: EEVblog #779 - Batteriser: How To Measure Battery Cutoff Voltage
url: https://www.youtube.com/watch?v=dnXiLBabSTU
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 30, "3": 54, "4": 67, "5": 78, "6": 89, "7": 97, "8": 108, "9": 118, "10": 133, "11": 154, "12": 165, "13": 179, "14": 194, "15": 205, "16": 218, "17": 239, "18": 250, "19": 262, "20": 281, "21": 298, "22": 323, "23": 335, "24": 349, "25": 363, "26": 376, "27": 391, "28": 405, "29": 417, "30": 427, "31": 441, "32": 453, "33": 466, "34": 482, "35": 493, "36": 502, "37": 513, "38": 527, "39": 545, "40": 558, "41": 577, "42": 591, "43": 605, "44": 623, "45": 636, "46": 653, "47": 661, "48": 682, "49": 702, "50": 720, "51": 739, "52": 752, "53": 767, "54": 788, "55": 800, "56": 814, "57": 825, "58": 839, "59": 859, "60": 874, "61": 898, "62": 913, "63": 921, "64": 935, "65": 946, "66": 960, "67": 975, "68": 992, "69": 998, "70": 1012, "71": 1019, "72": 1036, "73": 1058, "74": 1069, "75": 1084, "76": 1098, "77": 1112, "78": 1126, "79": 1143, "80": 1157, "81": 1171, "82": 1186, "83": 1197, "84": 1215, "85": 1226, "86": 1235, "87": 1241, "88": 1250, "89": 1260, "90": 1277, "91": 1286, "92": 1298, "93": 1313, "94": 1338, "95": 1355, "96": 1372, "97": 1390, "98": 1406, "99": 1420, "100": 1435, "101": 1459, "102": 1488, "103": 1504, "104": 1518, "105": 1535, "106": 1549, "107": 1563, "108": 1578, "109": 1587, "110": 1600, "111": 1615, "112": 1629, "113": 1646, "114": 1674, "115": 1684, "116": 1691, "117": 1704, "118": 1719, "119": 1732, "120": 1743, "121": 1754, "122": 1767, "123": 1776, "124": 1786, "125": 1798, "126": 1813, "127": 1821}
---

**Dave Jones:** Hi, in a recent video I demonstrated measuring the battery cutoff voltage in various electronic products. I think I did like 10 different products and got an average value of about 1 V or just over 1 V, something like that per cell for a typical modern electronics product.

**Dave Jones:** And everyone knows, yeah, that's uh pretty much how products are designed these days to have a battery cutoff voltage around about that 1 V figure. And as I've done in previous videos as well, the usable energy in a battery often about 0.8 V.

**Dave Jones:** So, if you want to maximize the battery life in your battery, you should design your product to work down to 0.8 V per cell. But, somebody put out a video claiming that I did it completely wrong, that it wasn't valid, and that you can't measure the cutoff voltage of a product with a power supply as I did it.

**Dave Jones:** And that's completely puzzling because not only is using an external power supply the correct way to do it, it's pretty much the only practical way to do it unless you want to actually sit there and watch the battery discharge itself.

**Dave Jones:** So, for the very few people who actually don't get it and think that using a power supply is the incorrect method, let's go through it and see why it is the correct method.

**Dave Jones:** Here's how you measure the battery cutoff voltage of your product. So, let's take a typical product, a symbol clapping monkey. Please excuse the crudity of the model, didn't have time to build it to scale or to paint it.

**Dave Jones:** Now, a typical product like this, when you shove the batteries in here, it does what monkeys do, and then it finally gets to a point where the product doesn't work anymore.

**Dave Jones:** Now, this could be it just stops clapping, or it could be an active modern product that actually monitors the battery voltage and tells you when it's finished, just like this wireless microphone I'm using right now to record this.

**Dave Jones:** It's got a low battery LED on here, and once that kicks in, well, you stop using the product, otherwise the functionality is not guaranteed. So, we're going to call that point the battery cutoff voltage.

**Dave Jones:** And as I showed in a previous video, for a modern electronic active electronic product, might be typically 1 V per cell. And if it you use multiple cells, multiple batteries in your product, then well, this is per cell voltage.

**Dave Jones:** And let's take it as 1 V. So, you might have some an active cutout detection circuit, a comparator for example, and a voltage reference inside your product that when your battery voltage gets down to that 1 V here, then it turns on your low battery detect LED or shuts down the product or you know, stops functionality, does whatever.

**Dave Jones:** So, how do you test this product, whether or not you designed it yourself or whether or not you've actually bought the product and you want to measure where it actually stops functioning, at what battery voltage?

**Dave Jones:** How do you do that? Well, there's actually only two ways to do it. One is to stick the battery in of course and then go in there and shove some probes up there and try and actually measure that itself or run some wires out and measure it.

**Dave Jones:** Or you can have the battery external and you just run some wires in like that and then you measure your voltage, your battery terminal voltage right at that point there cuz you want to eliminate any drop in the resistance in your leads like that.

**Dave Jones:** And well, you can sit there and wait for that voltage to discharge, discharge, and discharge until it gets to the point where your low battery detection LED comes on or the product stops working.

**Dave Jones:** And well, that can take a long time and that's why hardly anyone does it that way. That's why you use an external power supply. So, instead of hooking your battery up like that, you do exactly the same thing.

**Dave Jones:** You just hook it up to your power supply like that. And once again, ideally, you should measure the battery voltage right at the battery terminal there rather than relying on the uh, voltage measured on your power supply because there might be a small amount of resistance in there and maybe a tiny amount of contact resistance, but for a lowish power product, that really doesn't matter.

**Dave Jones:** You can actually rely on the voltage reading of your power supply. So, then you just drop the power supply voltage slowly until your low battery detect LED turns on or your product stops working.

**Dave Jones:** And then you can read off either from your power supply or if you're doing it because it's a high draw product, from a meter connected directly as close as possible to the battery terminals there.

**Dave Jones:** Bingo, you can read off the cut-off voltage. It's that simple. But, like I said, somebody, namely Batteriser, have put out a video saying that this is an incorrect method of measuring the cut-off voltage of a product.

**Dave Jones:** We have been asked questions about the validity of measuring the cut-off voltage of battery-operated devices with a power supply. Claiming that using a power supply to measure the cut-off voltage of a product is wrong and misleading at best.

**Dave Jones:** To use a power supply to show a battery-operated devices cut-off voltage, ignoring the battery's internal resistance, is wrong and misleading at best. Unbelievable. I'll show you why that statement is demonstrably untrue and using a power supply is the industry standard method for measuring the cut-off voltage of a battery and why it is equivalent to using the battery itself.

**Dave Jones:** Now, they claim that the reason it doesn't work and you can't use a power supply is that batteries are inherently different to power supplies. And yes, that is completely true, as I've explained in previous videos.

**Dave Jones:** A power supply effectively has zero internal resistance. It is designed to deliver large amounts of current over a large operational voltage range, so you can approximate any internal resistance to effectively zero.

**Dave Jones:** But, that's not the same for batteries. Take a a regular AA or AAA battery, for example. It's also got an internal resistance, just like a power supply has a tiny little bit, you know, like milliohms or something like that internal resistance.

**Dave Jones:** Well, a battery actually has quite a large internal resistance. It's also called the ESR, the equivalent series resistance, but we'll use the term IR for internal resistance of the battery.

**Dave Jones:** So, it's like having a little series resistor inside, physically inside your battery like this before it gets to the external contact like this. And the internal resistance for a AA or AAA battery is around about 100 to 300 milliohms.

**Dave Jones:** 100 milliohms when it's fresh, 300-odd milliohms once it gets to its end of its discharge curve down here. And here's a graph from Duracell showing how that internal resistance changes with the battery discharge curve like this.

**Dave Jones:** And I'll just make mention of that the internal resistance, the ESR, of a battery is comprised of two different things. Now, I have done a video on this, which I'll link in down below.

**Dave Jones:** It is the combination of the electrical contact resistance. That's, you know, the little welds inside and all that sort of stuff, which is particularly relevant to a multi-cell battery like a 9-V battery, for example.

**Dave Jones:** That'll have six 4A cells inside it. There's all that extra contact resistance, and that's why the internal resistance of a 9-V battery is higher than a AA or single AA or AAA cell.

**Dave Jones:** But, it also, and most importantly, is also comprised of the what's called the ionic resistance. Now, this is a complex subject. It's the electrochemistry of the the cell itself.

**Dave Jones:** Now, I have actually done a video quite some time back looking at the ionic resistance of a battery. So, click here if you want to see that one. So, to keep this video simple, we won't get into the complex details of how the electrochemistry inside a battery works.

**Dave Jones:** Suffice it to say that you can actually simplify it to an equivalent series resistance and internal resistance value. And that's a common thing to do in the industry. You don't necessarily have to know how the chemistry works inside to know that the internal resistance of a battery causes a problem.

**Dave Jones:** So, okay. The internal resistance of a battery is much higher than a power supply. We're talking several orders of magnitude higher. So, wouldn't that make a difference when you're measuring measuring the battery cutoff voltage?

**Dave Jones:** Well, no, it's not. And here's why. It's a very simple and obvious thing. Now, let's assume that the uh lead resistance in here is negligible for both cases, okay?

**Dave Jones:** For the power supply and the internal resistance of the battery. This has 300 m internal resistance. Say this one has effectively zero. So, why doesn't it matter that this is 300 m and this is zero?

**Dave Jones:** It's because we can't measure that point and we can't measure that point in there of the cell. Well, we can, which I'll explain in a minute, but for the purposes of running the product, you can't.

**Dave Jones:** That's why I said you have to actually measure directly on the battery terminals of the product. And when you do that, when you measure on the battery terminals, that, by definition, okay, is the battery cutoff voltage of the product because you can't measure this value in here.

**Dave Jones:** It only matters what the value is in there because the internal circuitry you've got for your product actually has a voltage reference in there, and that's what's determining what shuts off your product.

**Dave Jones:** So, it's the battery. It's the voltage on the battery terminals here. It's got nothing to do with this internal resistance. It's a complete red herring. And the other reason why this internal resistance here doesn't matter for the cutoff voltage is because look at the data sheets for any battery at all.

**Dave Jones:** Every single data sheet for every battery ever produced shows a characteristic discharge curve that is under load, i.e. the voltage on the terminal of the battery after the internal resistance.

**Dave Jones:** They cannot give you a characteristic curve of effectively before that internal resistance. It doesn't exist. This internal resistance is all part of the electrochemistry inside the cell like this.

**Dave Jones:** So, it's meaningless to talk about the voltage of a battery when it's not loaded. So, I've shown here on this discharge characteristic curve here, the battery voltage when it's fresh for a single alkaline cell might start at say 1.6 V open circuit voltage.

**Dave Jones:** And that's why the I've got two curves here. The blue one is the loaded terminal voltage, i.e. the exact curve that you'd get in the data sheet for a given constant power drain constant current drain constant resistance drain or whatever it is.

**Dave Jones:** And then I've got a green curve in here, which is the unloaded terminal voltage, which is the curve you would get if you had to pull out your battery each time for your product, measure it with a multimeter, which is effectively an open load.

**Dave Jones:** There's no load on it, and measure the unloaded voltage, then put it back in your product, and then a minute later take it back out, and measure the battery voltage again, unloaded.

**Dave Jones:** Okay? So, you can actually get two characteristic curves like that. So, the green one, of course, is going to have a higher voltage because when you put a load on a battery like this, this internal resistance, of course, Ohm's law, it's going to drop some voltage, and that voltage is going to be the differential between those two curves there.

**Dave Jones:** So, this is why it's fundamentally and demonstrably wrong to measure the open circuit unloaded voltage of a battery when you're talking about discharge curves, battery cut off voltages, and everything else because it's meaningless because you're not loading down the product and you're actually not taking into account that internal resistance.

**Dave Jones:** It It's so fundamentally wrong. Nobody in the industry does it like that. You can't. It's wrong. And as I said, and I'll repeat, this is why the manufacturers only publish loaded voltage curves because all you can get is this terminal voltage here.

**Dave Jones:** And when you design a product, all that matters All that matters is the voltage on those terminals. And this is why it's fundamentally correct to use a power supply to measure the cut off voltage of a product because you're effectively You've got zero ohms in there, okay?

**Dave Jones:** You're putting that voltage. You're forcing the voltage right onto the terminals there. You've got no internal resistance whatsoever. So, you're actually measuring the true uh cut off voltage of the product by doing that.

**Dave Jones:** And like I said, if you really want to, yes, you can use the real battery and you can hook it up to the product and you can sit there, twiddle your thumbs, and wait and wait and wait days, months, a year, or whatever until it happens to get down to the cut off voltage of your product, but nobody's got time to do that.

**Dave Jones:** So, you just hook up a power supply. It is fundamentally the correct way to do it. So, if you remove your battery from the product after you've used it and then measure the terminal voltage with your multimeter, which is an open uh circuit, then what you're measuring is this green characteristic curve here effectively.

**Dave Jones:** You're measuring it by not taking into account the ESR when the product's actually being powered. What is the point of that? It It's It's just completely silly and actually fundamentally wrong.

**Dave Jones:** All that matters is the battery voltage there on the terminals when it's under load? Of course, that's the only thing that matters, because that's what you're testing. You're testing the product during its operation.

**Dave Jones:** So, if you take the battery out, and your battery voltage recovers because there's no current flowing through your battery like that to give an internal drop, that is not an accurate measurement.

**Dave Jones:** This is fundamental stuff. This is hobby-level stuff. I learned this when I was like 7 years old. It's not hard to measure the battery voltage not under load is demonstrably wrong.

**Dave Jones:** You cannot argue it. You cannot argue it. To do so is just to make a complete fool of yourself. So, by saying that batteries are different to power supplies, yes, they are, but that is a completely pointless statement when you're talking about battery cutoff voltage, cuz as I said, all that matters is the terminal voltage here.

**Dave Jones:** So, yes, they're different. So, using the power supply to measure the cutoff voltage is actually taking into account the internal resistance of this battery, unlike the claim that they're made that it's not taken into account the internal resistance.

**Dave Jones:** It is. It fundamentally is. I don't know how much simpler I can explain it. It's just Ah. So, let's actually go and take a look at this Batteriser response video, because it is actually a direct response to my debunking video, and also my Batteriser explained blog article down here.

**Dave Jones:** So, let's have a look. They've actually confusingly made two different videos here with this clapping monkey thing trying to prove that my using a power supply to measure the cutoff voltage is incorrect.

**Dave Jones:** But really, there doesn't seem to be any major difference between the two except the ending why they've called this one a conclusion here. So, we're going to take a look it.

**Dave Jones:** Curiously, it is on not at the Batteriser's YouTube channel, but the Batteriser Batteroo channel, which they actually claim, if you go to the about tab, "Disclaimer, we are not in any way affiliated with Batteriser or Batteroo.

**Dave Jones:** We are simply a fan page." Yet, it has all their official videos and everything else. And they also talk in the first person that they're "Thanks to all our supporters, blah, blah, blah." I don't get it.

**Dave Jones:** And by the way, if you're after some laughs, go and look at these uh supposed fan submitted videos, these professionally produced fan submitted videos here, which extol the virtues of the Batteriser.

**Dave Jones:** Oh, goodness, there's even nature man down here. Crikey. Because they do make very specific uh claims on this video that the Batteriser has come under skepticism due to a flawed test, i.e., my test, in which a power supply was used to debunk the Batteriser.

**Dave Jones:** There is no other video out there, so they're obviously uh this is a response to my video. So, I'm happily making this response video to their video. And by the way, I tried to comment on uh their most recent video, but they deleted my comment.

**Dave Jones:** Well, but I'm more than happy to have them uh come on to my videos and and discuss it all they want. Leave all the comments they like. I don't delete comments.

**Dave Jones:** I don't uh delete comments on the forum or my blog uh sites. So, they're welcome to come in and discuss it any time they like. And in this Yahoo Makers article, uh they interviewed uh Batteriser and uh Mr.

**Dave Jones:** Roopavah. Um this is what he had to say about me. Discussing the EV blog video, he says, "I think he's a good guy." Oh, thank you. I'm sure you're a good guy, too.

**Dave Jones:** I just think he didn't know enough. Really? I don't know enough? Like I just showed that using a power supply is the correct industry standard method for measuring battery cutoff voltage, and you're claiming it's not.

**Dave Jones:** You're basically the only one on the planet who claims it's not and I don't know what I'm talking about. Okay. Well, at least I know enough not to go around claiming that there's 1.5 volts of energy and that many devices stop functioning around the 1.3 volt mark.

**Dave Jones:** Goodness. And then when everyone including myself had to try and tell you that no, the cut out voltage of a product is about 1.1 volts under load and you finally came out on your website and here it is I screen captured it.

**Dave Jones:** You admitted that the secret is that most 1.5 volt batteries drain to about 1.1 volts under load. Thank you for agreeing with me. But then of course you went and removed that and changed it and removed any reference to that 1.1 volts.

**Dave Jones:** But thankfully it's still in your frequently asked questions down in here. At least you left it in and admitted that products do actually cut out at 1.1 volts. I'm glad I was right about that in my video.

**Dave Jones:** So let's look at their final conclusion again. To use a power supply to show a battery operated devices cut off voltage ignoring the batteries internal resistance is wrong and misleading at best.

**Dave Jones:** Batteries behave different from power supplies. Well, I just spent the last 15 minutes explaining that yes, batteries do behave different from power supplies, but what's your point? You're not stating anything of value there whatsoever.

**Dave Jones:** It's basically just one big straw man argument to set up the idea that yes, you're technically right. Batteries are different from power supplies and then somehow that proves and debunks my entire debunking video because I got it wrong.

**Dave Jones:** But yet never once in the video as we'll see do you actually explain how to measure the cut off voltage. So let's go and have a look at the rest of the video and see how you sort of try and justify this.

**Dave Jones:** Oh, I won't show the whole thing. I'll just cut out various parts that aren't actually relevant. Power supplies can source a huge amount of current while maintaining constant output voltage.

**Dave Jones:** Batteries, on the other hand, are not capable of maintaining a constant voltage when it is connecting to a device that draws current. Due to the internal resistance of the battery, its terminal voltage will drop when connecting to a device.

**Dave Jones:** Well, yeah, of course. That's why I explained in the video that all that matters is measuring measuring the actual terminal voltage battery terminal voltage of the product under test while it's operating, i.e., under load.

**Dave Jones:** This is precisely the reason why battery manufacturers publish discharge curves under load because that's the only measurement that matters and it takes into account the internal resistance. Oh, so you're interested in this monkey.

**Dave Jones:** First of all, who is this guy? It says on the YouTube video that he's a professor of electrical engineering. Okay, I'm sure he is, but hey, I can't believe he's saying this.

**Dave Jones:** So, first I got to set it to 3 volts because each battery is 1 and 1/2 volts. Now, I don't know about you, but uh take a look at this uh soldering iron here.

**Dave Jones:** This well as soldering iron looks like it's never been used. And who the hell just leaves the thing lying on a bench like that? And where is the solder?

**Dave Jones:** If I didn't know any better, I'd say that they just set up this bench as a just a promo video shot. And I just couldn't help but notice the oscilloscope.

**Dave Jones:** Look at the square wave they've got there and you can see that all they're doing is measuring the compensation on the front of the scope and it's probably the worst compensation I've ever seen.

**Dave Jones:** They don't even know how to compensate the probe. Hilarious. Sorry, had to point it out. So, we got the power supply set at 3 volts. Now, we can see how he behaves at the same voltage as two fresh batteries.

**Dave Jones:** Oh, yeah. Nope, I'm sorry. It's not the same as the voltage of the two fresh batteries because it's not taking into account the internal resistance of the battery, which will cause a drop.

**Dave Jones:** It's unbelievable. You make the claim that I'm wrong cuz I'm not taking into account the internal resistance of the battery. You're the one who's not taking into account the internal resistance of the battery.

**Dave Jones:** Oh. So, now let's turn it down to 2 and 1/2 volts. Still moving and making a lot of noise. And again, still making a lot of noise at 2 volts.

**Dave Jones:** Down at 1 and 1/2 volts, he's starting to slow down a little bit. And slowly going down on the voltage. And he's stopped moving at 0.9 volts. This demonstration shows that with a power supply, the monkey will operate even when we bring the voltage down all the way to 0.9 volts.

**Dave Jones:** Wow, that's pretty awesome, isn't it? I love this monkey. Can work down to 0.45 volts per cell. Incredible. Awesome. However, when using two batteries with a total voltage of 2.5 volts, the monkey will not operate.

**Dave Jones:** We checked the voltages of two used batteries. The first battery voltage measured at 1.231 volts. What are you doing? You do not measure the battery voltage when it's not under load.

**Dave Jones:** It does not tell you you're not taking into account the internal resistance. As I said, this is hobby level stuff. This is battery 101 stuff. For a professor to not know that you can't do this is just ah, it's incredible.

**Dave Jones:** These are used batteries. You don't know how much energy is left in that battery, how much the internal resistance is going to affect the monkey under test. We measured the second battery at 1.267 volts.

**Dave Jones:** This monkey uses two batteries in series. So, you have to add the voltages together, resulting in 2.5 volts being supplied to the monkey. 2.5 volts is not being supplied to the monkey.

**Dave Jones:** Because when you turn the monkey on, it is a load. It loads down the voltage voltage. You get a drop on the internal resistance. Unless you measure the voltage on the terminals of the battery probe right up the monkey's ass, you are not measuring anything.

**Dave Jones:** This is just so fundamentally wrong. It's just what Oh, go. Look, you even say this on your own website. Here's your frequently asked questions where you quote Wikipedia. Look, when the source delivers current, the measured voltage output is lower lower than the no load voltage, which is what you just measured.

**Dave Jones:** You measured the no load voltage, and you're saying that 2. That no load voltage is being delivered to the monkey. Unbelievable. How you can possibly say this in the video when your own frequently asked questions where you try and explain this says completely the opposite thing where the internal resistance of the battery, as I've just spent 15 minutes explaining, will actually cause a drop, and you won't get it as you claim that

**Dave Jones:** 2.5 volts. It's going to be much much lower, causing the monkey potentially not to operate at all, as we'll see in a second. Duh. And then flip it to on.

**Dave Jones:** And you saw it tried to go, but stopped. So, we'll see if it if it can go you know, second time. Just give it another shot. Yep, it it tries, but it can't it can't go.

**Dave Jones:** Well, that's not the least bit surprising. This is a high drain device, this clapping monkey, and obviously the internal resistance of those because you're using already, you know, half dead or 3/4 dead batteries or whatever, that it does not have the capability to power the monkey cuz there's too much loss in the internal resistance.

**Dave Jones:** And this is completely obvious. The entire premise of your video has been to show that there is a difference between a power supply and a battery. As I explained right at the start of my video, of course there is.

**Dave Jones:** But this does not explain why at all. There is nothing in this video to explain why using a power supply is the incorrect method for determining battery cutout voltage, which is all that matters.

**Dave Jones:** You haven't even done the fundamental first principle thing of measuring the battery voltage, putting the probes in there when the batteries are in there. This is an unbelievable beginner mistake.

**Dave Jones:** It's so embarrassing. If you did this at a job interview, you'd be booted right out the door. If you did this in made this mistake in an exam, you'd fail.

**Dave Jones:** If you made this mistake in a job, you'd you'd be booted out. Or they'd looked at very strangely. It's As I said, this is hobby level understanding to measure the battery voltage under load.

**Dave Jones:** It's absolutely incredible. This is one of the greatest straw man arguments I've ever seen. It is just facepalmly dumb. It really is. But if you didn't know any better you'd take this video and go yeah that sounds okay.

**Dave Jones:** But it's just fundamentally wrong. Just take a look at this Energizer double a battery sheet. It shows the industry standard test for different types of products toothbrushes portable lighting and toy in this case.

**Dave Jones:** You know this clapping monkey yeah it might get 8 or 10 hours life or something like that. So look at that discharge curve of that toy. This is under load like it high discharge current every time it it bangs those symbols together it it's just going to die because of the internal resistance of the battery it can't recover.

**Dave Jones:** There's no more not enough useful energy left to actually provide enough voltage to operate the device given the required current draw. And if you actually did this test properly and actually measured the battery terminal voltage inside the monkey when it was operating you would see it actually drop below that that point four five volts or what it per cell or whatever it was that you measured with the power supply.

**Dave Jones:** That's how this testing works. That's how I spent 15 minutes explaining it to you. didn't do the right test. You didn't probe it. All you did is shove the batteries in there.

**Dave Jones:** See it doesn't work. Of course it doesn't work because it's a pulse load. Look at the thing for the toy here. It's designed to be one hour per day.

**Dave Jones:** You put in those used batteries in the toy and start to deliver a pulse load. The electrochemistry inside the ionic resistance cannot deliver a low enough resistance in order to clap those symbols.

**Dave Jones:** Battery 101 stuff. And of course you would expect the monkey to work with the power supply because it's got no internal resistance. It's an ideal battery. So it's going to deliver as much current as needed as much pulse current as needed.

**Dave Jones:** There's no ionic resistance in there. Of course batteries are different. You stated the bleeding obvious in this video and then trying to claim that the whole method of using a power supply is wrong.

**Dave Jones:** Clearly do not fundamentally understand the concept of measuring this. Unbelievable. There's not a single credible engineer in the industry who will agree with this video. Not a single one.

**Dave Jones:** Go find me one, please. Prove me wrong. So, that's it. I've had enough. I don't know what more to say about this laughable straw man video. It is It's got to be a parody.

**Dave Jones:** Surely the the joke's on all of us. It This guy They cannot be serious. I don't know how anyone could put their name forward and actually say this sort of stuff.

**Dave Jones:** If I said this, I'd be laughed out of the industry. Anyway, leave your comments down below. I'll link to the forum down below where you can discuss this thing.

**Dave Jones:** And as I said, Batteriser, more than welcome to come in here and discuss it and try and prove I'm wrong. I'm happy to always be corrected. I won't delete your comments, unlike what you did to me.

**Dave Jones:** So, I didn't really want to do this video. I'd had enough of the Batteriser and their silly claims, but I just couldn't let it stand. They were presenting fundamentally wrong and misleading information.

**Dave Jones:** Exactly the claim they made about my video, but in this case, it's demonstrably true that they are incorrect here and being deceptive. It's fundamentally wrong. There's no way anyone can stand behind this.

**Dave Jones:** They should be totally embarrassed. If I did this, I'd be I wouldn't be able to make another video again. I'd be laughed out of the industry. Unbelievable. Anyway, this is my response.

**Dave Jones:** Hope you enjoyed it. Hope you found it interesting and educational. Catch you next time.
