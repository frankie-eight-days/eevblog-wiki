---
video_id: Eoh-JKVQZwg
title: EEVblog 1472 - Resistor Cube Problem SOLVED
url: https://www.youtube.com/watch?v=Eoh-JKVQZwg
source: youtube-asr
timestamps: {"0": 1, "1": 13, "2": 24, "3": 39, "4": 54, "5": 70, "6": 79, "7": 92, "8": 106, "9": 113, "10": 123, "11": 139, "12": 149, "13": 163, "14": 174, "15": 193, "16": 207, "17": 222, "18": 234, "19": 242, "20": 254, "21": 263, "22": 274, "23": 285, "24": 295, "25": 307, "26": 321, "27": 340, "28": 351, "29": 362, "30": 384, "31": 394, "32": 405, "33": 415, "34": 429, "35": 439, "36": 447, "37": 460, "38": 473, "39": 485, "40": 496, "41": 511, "42": 523, "43": 544, "44": 563, "45": 573, "46": 584, "47": 595, "48": 602, "49": 615, "50": 623, "51": 638, "52": 645, "53": 658, "54": 667, "55": 681, "56": 691, "57": 709, "58": 723, "59": 743, "60": 753, "61": 764, "62": 775, "63": 788, "64": 801, "65": 813, "66": 821, "67": 834, "68": 847, "69": 864, "70": 873, "71": 887, "72": 898, "73": 906, "74": 926, "75": 938, "76": 946, "77": 963, "78": 969, "79": 978, "80": 992, "81": 1002, "82": 1012, "83": 1035, "84": 1045, "85": 1066, "86": 1075, "87": 1083, "88": 1096, "89": 1110, "90": 1129, "91": 1141, "92": 1148, "93": 1162, "94": 1177}
---

**Dave Jones:** Hi, it's Twitter question time. Thank you very much Aditya. Are you Bahandi? Butchering that, sorry. Dave, care to make a quick and easy video on this one for idiots like me trying to learn electronics.

**Dave Jones:** Well, you're not an idiot because you are trying to learn which is excellent. Anyway, world of engineering, I follow them. Basic electrical knowledge test. So, let's have a look.

**Dave Jones:** What is the resistance between A point A and point H here for a cube of resistors like this, three-dimensional cube with so 12 identical resistors of resistance they happen to be 10K here 0.05% but we'll just assume they're like 1 ohm.

**Dave Jones:** It doesn't matter. They're all identical values. And this is actually a very common exam question you'll get in any electronics course and I've done of course way way back which is my the infinite resistor problem and I didn't solve that mathematically.

**Dave Jones:** I actually physically built it up and solved it. And you can physically build one of these yourself. Go and get some resistors. Measure them so they're all reasonably close, you know, choose your you know, pick and choose and then solder them together and actually build it up and verify the answer.

**Dave Jones:** Might do this at the end actually. So, how do we solve this? Well, there's many ways to skin this engineering cat and here's the way I would approach it.

**Dave Jones:** I think it's the way probably majority of people would actually approach this. Now, I'll leave the network up here. Now, the first thing you have to do is to redraw it because this is very common in electronics.

**Dave Jones:** If you redraw circuits to be like familiar to you or easier to understand then often boom, you'll go, "Oh, that's easy." Right? Take any Bob Pease circuit for example.

**Dave Jones:** Your eyes are just rolling in the back of your head going, "How does that work?" Well, if you redraw it in a sensible manner, it it works just fine.

**Dave Jones:** That was that was his style. Okay, so what I've done here, I've I've taken these four top resistors here and I've redrawn them in the middle here. This is the first thing I did.

**Dave Jones:** So, I got points A here, A and H and H. And hopefully, all right, you can see that. That's obvious. If you If you have problem actually translating this into a three-dimensional shape into a two-dimensional diagram, not sure I can help you any further.

**Dave Jones:** But, um yeah, try and work through it. It's It's pretty easy. So, E here obviously goes has a resistor going down to point F. So, I drew a resistor here going off to point F.

**Dave Jones:** And likewise, point D going down to point C here, like that. And likewise, for point H and points A, you've got a resistor going off here. In this case, it goes from H to G, like that.

**Dave Jones:** And it goes from A to B, like that. And then, obviously, you can see that there's a resistor between F and B. So, I've added that. And another one from B and C, etc.

**Dave Jones:** So, at this point, the question asks, "What is the resistance between A and H?" And well, uh we've got this point in here and this point in here and we've got resistors going out this way and we've got resistors going out this way and they fold back on each other and they're in series and parallel and all higgledy-piggledy.

**Dave Jones:** But, by looking at this cube here, you can see that the question is exactly the same between A and H here, this point here and this point here. It'd be exactly the same between B and G.

**Dave Jones:** It'd be exactly the same between F and C, etc. Like two opposite points. What's the difference? Because these are all identical resistors. So, this cube has symmetry, okay? So, A and H here, there's no difference, as I said, between B and G.

**Dave Jones:** So, if you solve for B and G, it's exactly the same as solving for A and H. It makes no difference. So, our circuit conveniently already has B on the outside here, and G on the outside here.

**Dave Jones:** So, we'll just solve for B and G. So, we'll forget A and H now. I won't bother. I could relabel them and everything, but I won't bother. I'll just leave it.

**Dave Jones:** So, you've got a more familiar resistor network problem, um with, you know, what is the point between here and here? So, it it's starting to feel a bit more familiar, hopefully.

**Dave Jones:** But, we still have this problem of like, "Oh, look, we've got paths going up here and down here, you know? It's like these things are all over the shop, right?

**Dave Jones:** It's a dog's breakfast. How do we like possibly solve for any of this?" Now, here comes the neat trick, okay? You remember how we talked about symmetry before? Obviously, this circuit is symmetrical.

**Dave Jones:** But, hopefully, you can visualize this, okay? It's obvious to me, and hopefully, it'll be obvious to you now, cuz this is the key trick you need to actually solve this thing.

**Dave Jones:** Otherwise, it's it's really ugly. Like, you could solve it without simplifying the circuit even further, but the equations is just going to be horrible. They're all the same value.

**Dave Jones:** So, hopefully, you can see if I split this down the middle like this, all this side is identical mirror image to what's on left and right. If I split this like this, it's a mirror image top and bottom, right?

**Dave Jones:** You can see that. So, this is a completely symmetrical circuit. So, we can use a technique called equipotential nodes, or equi-potential. It means equal potential, same potential nodes, right?

**Dave Jones:** You remember Kirchhoff's current laws? The sum of the currents exiting the junction equals the sum of the currents going into the junction? Well, if all of these are the same value, okay, then the current going up here is going to be identical to the current going down here if you apply a voltage between B and G, okay?

**Dave Jones:** So, you can try and solve it in terms of like Ohm's law and Kirchhoff's current laws and everything else, right? But, we can do it simpler than this because we know the current up here is the same as the current down here.

**Dave Jones:** And interestingly, the current through here is going to be the same as the current through here. But, you might be thinking, "Oh, what about look, there's a sneaky current path up here." Uh-huh, stick with me.

**Dave Jones:** We'll deal with this in a minute. Now, I'm sure I've mentioned this term in a previous video, by inspection. Due to the symmetry of this circuit, top and bottom, left and right, we can determine that if we applied a voltage between B and G here, then the voltage at point F would be identical to the voltage at point C.

**Dave Jones:** We're inspecting the circuit and we're deeming that the voltage here must be equal to the voltage here because this is a symmetrical circuit. Everything's symmetrical. Why wouldn't those voltages be the same?

**Dave Jones:** And it it's true. The volt If you build this up physically in this configuration like this, which will be no different to the cube over here, it's just in a physical flatter two-dimensional a format.

**Dave Jones:** If you build this and put a voltage across here, here's some homework for you, go and physically build this, measure the voltage here and here relative to a reference point.

**Dave Jones:** You can choose a reference point. Anyway, these voltages will be the same. And likewise, voltage at point E, node E, and node D will be the same as well.

**Dave Jones:** Bingo. If these voltages are the same, then we can treat them as a short circuit. So, what we can do now is we can actually treat these points as a short circuit.

**Dave Jones:** And I can draw a short circuit in here like this, okay? But, it's a bit how you do it now cuz we have to like jump over um some things like this.

**Dave Jones:** We'll simplify this further in a minute, stick around. So, we've got two points now shorted out in our circuit. Now, we can actually go further and we kind of like have to uh at this point cuz these two resistors here are still confusing us, right?

**Dave Jones:** Is current flowing this way? Is it flowing like what's what's going on here? Well, hopefully you can see that we've still got symmetry, right? Like this. Now, you remember these two resistors are now in parallel.

**Dave Jones:** These two resistors are now in parallel. So, technically, we could redraw that. So, well, let's do that. Okay, so I've redrawn that here. These two resistors, because you remember these were in parallel, these are now R on two.

**Dave Jones:** These are their value. This resistor remains R or whatever that is, you know, could be 1 ohm, 10k, doesn't matter. And these ones up here, these all everything else remains resistance R.

**Dave Jones:** So, the only ones we've solved for now are these two here. But once again, you can see we've got symmetry like this. So, this point up here has to equal this point here, and that's what we determined before, okay?

**Dave Jones:** Short those out. Now, here is where you can go in two different directions to solve this, and you'll get exactly the same answer, okay? So, we know that these two F and C here are, equipotential nodes, right?

**Dave Jones:** They're the same potential because of the symmetry we have here. Now, we can actually short these again, and we can do it that way if we want, but also what you can do is you can simply say that no current flows down here or here in either direction.

**Dave Jones:** No current at all flows. So, you can actually eliminate these two resistors from In fact, let's choose two different paths, and we'll solve it two different ways. And by the way, we kind of have a Wheatstone bridge kind of thing happening here, which means that like we're we're sort of because these are all balanced, right?

**Dave Jones:** This side is balanced with this side here, and this half it right it's all balanced. Oh, might I don't think I've ever done a video on Wheatstone bridge. We'll go check out Wheatstone bridges, right?

**Dave Jones:** So, you can actually, once again, by inspection and knowledge of Wheatstone bridges, you can say that the current down here and down There is no current flowing down here and down here.

**Dave Jones:** Once again, build it up, put your ammeter in there, and measure the current for yourself. There'll be no current flowing. And you can do all this in the newfangled simulators as well.

**Dave Jones:** So, you can just put this into your simulator, and you can actually measure the current. So, it will measure the simulator current through there and through here, and it's zero.

**Dave Jones:** Anyway, solved two different ways. Okay, so the first way we're going to do this is we're going to actually physically short F to C here, and that's the F to C point here.

**Dave Jones:** So, this resistor here and this resistor here become these two resistors, and they're both in parallel because we've shorted physically shorted this point up to this point up here.

**Dave Jones:** And then this resistor down here and this resistor here become these two in parallel. Okay, and then we've got our existing resistors in here. They don't change, and that becomes our new network.

**Dave Jones:** So, we put these in parallel. So, they This R on R becomes R on two like this. You can keep it in fraction form, or you can do like 0.5R.

**Dave Jones:** I've kind of mixed it here. Sorry about that for those who don't like it. Like I've put 1.5R and and R on fraction and decimal here. And whatever. Anyway, hopefully you're still with me.

**Dave Jones:** So, these become R on two, R on two, and this becomes R on two. So, this is getting much simpler, but once again, we've got these current paths like this.

**Dave Jones:** Okay? So, this isn't your traditional series-parallel problem. Once again, you simplify it again using equipotential nodes. Symmetry, right? Down here, like well, it it just imagine B and C are in the middle, right?

**Dave Jones:** Symmetry, like that. So, once again, you can short out this point to this point here. So, let's do that. Okay, so there's There's current flowing through this R on 2 at all here.

**Dave Jones:** There's no current flowing through these two here. So, we can short those out and bingo. Now, we've simplified it to one. If you were given this in an exam, you'd solve that easy peasy lemon squeezy because we've just got two resistors in parallel and then the total in series.

**Dave Jones:** Easy. So, I've converted back to decimal here. Um R on 2 becomes .5 R. Now, just to keep it consistent in this diagram here. So, half an ohm in parallel with 1.5 ohms.

**Dave Jones:** And that's 0.375 R. And likewise here, 0.375 R. You add those up cuz they're in series. Bingo. Your answer is 0.75 R for the resistance between B and G or as we said before A and H or E and D or C and F or whatever.

**Dave Jones:** Doesn't matter. Now, I'm going to show you an easier method to actually do this. You notice that there's like this one had one, two, three, and like four kind of steps.

**Dave Jones:** Well, this one only really has two steps and you get exactly the same answer. Let's see how we did it. Okay, before path number one, we actually treated this as a short circuit.

**Dave Jones:** If you remember that, okay? But I also said, "Remember you can think in terms of this is like a balanced like Wheatstone bridge. So, there's no current flowing through here.

**Dave Jones:** So, we don't have to actually short these out." What we can do is just actually eliminate these entirely from the circuit. We can scrub them out. So, that's what I'm going to do in path two here, okay?

**Dave Jones:** So, we've got these four resistors in series like this. There they are. They're identical. We've eliminated the resistor in here. We've got it out of the circuit cuz if there's no current flowing through there, is it shorted or is it open?

**Dave Jones:** Ah, doesn't matter. Could be either. You can treat it either way, okay? And so therefore, we're left with the two series resistors up here and two series resistors down the bottom.

**Dave Jones:** So, we're left with a simple parallel circuit of three resistors cuz these are all in series, okay? So, you solve your series ones first. So, these two resistors become 2R here.

**Dave Jones:** Likewise, that becomes 2R and this one becomes R + R + 1/2 an R + 1/2 an R, which becomes 3R. So, now you've got three resistors in parallel.

**Dave Jones:** Solve that using whatever a method of the parallel resistance uh equation you want to get and bingo, you get the answer 0.75R. So, they match regardless of the method that you use.

**Dave Jones:** So, there's there's two different methods. One is using equipotential nodes shorted, one is using equipotential nodes nodes open. So, there you go. There's And there's other techniques. Please leave it in the comments down below um how you would actually solve this.

**Dave Jones:** This is how um I would solve this uh problem and I just did and hopefully that makes sense to you. So, when you ever see questions like this, just go right.

**Dave Jones:** I I can't think in this. So, you redraw it in two dimensions. Once you redraw it in two dimensions, you look for any sym- symmetries. Have you got any equipotential nodes that nodes at the same potential?

**Dave Jones:** Um and then we can I short them together and or can I um open them? And you know, which choose the path of least resistance. I'm here all week.

**Dave Jones:** Um and choose whichever method you want and you get to the same answer. So, there you go. I hope you found that useful. I hope I've answered uh that question.

**Dave Jones:** He said simple. Um but this is I think it's a very simple uh concept to do. Once you know you have these tools available in your uh mathematical and and our circuit analysis toolkit to actually do this using equipotential nodes and just redrawing things and symmetry, um then yeah, you can really simplify these circuits.

**Dave Jones:** But I you can do it using complex equations and everything, I'm sure, and I wouldn't even bother. For me, this is like the easiest way to do it. Just, you know, step-by-step reducing it.

**Dave Jones:** So, in this case, I think probably, you know, that method there would be like the simplest way to do it. So, anyway, thoughts and comments down below if you found that interesting.

**Dave Jones:** If you did, please give it a big a thumbs up and as always discuss down below. And yes, I'm on the Twitters. I've got 60,000 followers now on Twitter and it's a way to directly interact uh with me and you can also do it on uh Patreon, of course, and the um uh supporters section of the uh forum as well.

**Dave Jones:** You can interact directly with me and ask me questions like this and hopefully I'll go on and do a video answering them cuz I think, you know, this has nice broad appeal.

**Dave Jones:** Anyway, waffle it on long enough. Catch you next time. All right, please excuse the crudity of the model. I didn't have time to build it to scale or to paint it.

**Dave Jones:** I have fledified the cube here as we uh saw before. Uh 1% resistors and if you follow me on Twitter, you'll know that I could not find, damn it, my box of uh several boxes of thousand resistors, um several thousand resistors per box.

**Dave Jones:** Um so, I could have matched them uh like actually handpicked them out to match them a bit better. But anyway, uh this is all I could scrounge, 4.7k resistors, have not matched them at all.

**Dave Jones:** So, just 1% tolerance, like crusty old ones from like 30 years ago. You get what you get and you don't get upset. Let's measure it. What does the confuser say we should get?

**Dave Jones:** Well, 4,700 ohms * 0.75 uh is th- 3.525 k. DO WE GET IT? OH, THAT'S GOOD ENOUGH FOR AUSTRALIA, 3.517. That's well within spec. And if we work that out, we get 0.7483 um as the scale factor.

**Dave Jones:** So, that's well within uh the 1% tolerance of the resistors that we're using. And for those curious, and you should be, uh minus 1% on 0.75 is 0.7425, which would be 3.489 K.

**Dave Jones:** And we're only 0.23% off. So, yeah, we're we're ballsing that one in. And this is a good time to give you a trap for young players. When you're using axial resistors like this, all the band lead uh components in these bands, as they're called, when you pull them out, you'll notice Look at that.

**Dave Jones:** There's glue left on the end of it. So, yeah. Don't go sticking these directly into breadboards because you're going to come a gutser. And uh they're not great to uh solder, either.

**Dave Jones:** So, you want to get a scalpel in there and uh get rid of that glue. Okay, so what I've done is I've put a 10-V voltage source across this.

**Dave Jones:** I've trimmed it uh to exactly 10 V. We'll use uh the this point over here as a ground reference, but, you know, you can do it anywhere. Anyway, what we want to see is that these two points here are exactly the same, and these two points here are exactly the same.

**Dave Jones:** Hear that? 5 V. Perfect. Oh, look at that. 5 V. A smidgen out, cuz remember, we're just using stock 1% resistors here. 5 V. And you guessed it. 5 V down there.

**Dave Jones:** Now, as for the uh current flowing through these resistors, remember how I said it should be zero? Well, we can measure that. Uh we can't just use the ammeter on the multimeter because the burden voltage of the multimeter, even though this is a low burden voltage multimeter, um it still could be a problem because we're only dealing with uh 4.7 K there.

**Dave Jones:** So, you know, if you whack a couple hundred ohms in there or whatever, even for a low burden voltage one, it uh it will unbalance these resistors. And remember when I said it's a Wheatstone uh bridge?

**Dave Jones:** And a Wheatstone bridge, you adjust the two of the resistors until you actually null out uh the current or null out the uh voltage. Anyway, we can measure the voltage across there.

**Dave Jones:** 0.9 uh 3 mV, and that works out to with 4.7 k resistor, uh 197 nanoamps. Nanoamps. That's pretty low. It's essentially zero. And this one's even lower. Works out to 51 nanoamps.

**Dave Jones:** So, yeah, there's no current flowing through those resistors. So, if you actually trimmed all these absolutely perfectly or you put them in the simulator and they're all ideal, yeah, there's actually zero current in those two resistors there.

**Dave Jones:** So, this means that I can physically snip these two resistors and it makes absolutely no difference to the circuit resistance at all. Cool, huh? Catch you next time.
