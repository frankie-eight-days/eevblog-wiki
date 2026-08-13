---
video_id: _V6nYLIChUA
title: EEVblog #848 - Home Energy Savers BUSTED!
url: https://www.youtube.com/watch?v=_V6nYLIChUA
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 45, "2": 63, "3": 84, "4": 101, "5": 115, "6": 136, "7": 154, "8": 179, "9": 194, "10": 217, "11": 236, "12": 249, "13": 268, "14": 288, "15": 308, "16": 333, "17": 357, "18": 377, "19": 393, "20": 409, "21": 429, "22": 449, "23": 469, "24": 493, "25": 513, "26": 537, "27": 553, "28": 565, "29": 585, "30": 601, "31": 617, "32": 633, "33": 653, "34": 669, "35": 689, "36": 705, "37": 725, "38": 745, "39": 765}
---

**Dave Jones:** Electricity saving box, Carl reckons that, uh, you can save, well, the claim is that, uh, save 20-30% of your power bills just by plugging the stupid thing in. Oh, you've got to be shitting me. And thankfully, they didn't, uh, weld, seal this shut or pot it or anything like that, although, they've potted whatever's in here.

**Dave Jones:** So this is their secret sauce. They haven't just, well, it is just a capacitor, right? Like, what else is bloody well going to be in there? But that's actually a potting box, and they've put something in there, because this is supposed to be an intelligent energy saver.

**Dave Jones:** Intelligent, the result is the best. Um, so, yeah, have they put just, like, a board in there, or is it just, like, two just dangling loose wires in a potted box? Let's see if we can measure it. It's a capacitor, look, 2.86 microfarads up, minus 90 degrees, so it's almost perfectly a capacitor.

**Dave Jones:** So there you go, dissipation factor, 0.001, as good as you get. It's a bloody cap. Let's do a very quick demo of this. This won't be a tutorial on power factor and everything else, but I'm just going to plug in a scope here into my power meter, which I'll show you in a separate shot.

**Dave Jones:** I'll show you with and without this thing, and you'll see that, well, it's going to make a difference. This thing's got a DC to DC converter, so it's going to have a poor power factor, but let's see if this heap of shit improves it.

**Dave Jones:** With a typical product, with a typical DC to DC converter, you might have plugged in. Now, this is without our power correcting wankerizer gadget, okay? So this is just the scope on its own. You can see it's drawing 18.7 watts here. And by the way, watts for a typical consumer, and also in my small office that I've got here, I am being charged watts.

**Dave Jones:** If your bill says kilowatts, you're being charged kilowatt hours, then you're paying for real power, not apparent power, which we're going to have a look at in a second. VA, because look, if we have a look at this, this is apparent power, and sure enough, it's drawing a lot more apparent power.

**Dave Jones:** But unless your electricity bill says you're being charged in VA, then you're not being charged for this power factor. So even if this thing worked and corrected your power factor, you're not being charged for it, so you don't save a damn cent. Anyway, so you can see that the power factor is just a ratio VA versus watts, and the power factor is about half.

**Dave Jones:** So let's plug in the wankerizer gadget and see if it makes a difference. That power factor, if this thing works, it should be a higher power factor, because the closer you get to 1, the better. You're correcting for that. So here we go, we've got to plug it in.

**Dave Jones:** Ta-da! Plugged it in. What's it done? Waa-waa-waa-waa-waa! It's actually lowered the power factor, it's drawing more! Look at this! What the hell? It's drawing 80, uh, 70 VA! It's useless, it's made it worse! And it's drawing a little bit more real power because of the LED in there.

**Dave Jones:** Jeez, it's just, it doesn't, it, not only does it not work, it makes it worse! On a typical DC to DC convert, convert, converter product. Oh! Now, I'll just show you something different, a different type of load. I've got my air purifier here, I've got it on maximum so you can probably hear that.

**Dave Jones:** Normally I have it on low and it's whisper quiet, you can't hear it at all. But it's basically just a big ass fan, that's, you know, it's got a little display and control and everything. But basically I've got it on full, so it's pretty much, you know, and that inductive motor load.

**Dave Jones:** So this power factor correction, you know, if you just put a capacitor across it, it should actually make a difference. And here it is, okay, it's drawing 94 watts, and apparent power 101. So it's got a pretty good power factor correction ratio. Usually if you're above .9 you wouldn't bother to implement anything to solve it.

**Dave Jones:** But I think just putting a capacitor across this, this will go up slightly. So let me plug it in, .929, let's have a look, here we go. Plugged it in, what's it up to? Yep, there we go, .947, there we go. So it has improved, .95, oh, it's going up.

**Dave Jones:** So it has improved it because it's basically an inductive load. So putting a capacitor in parallel, yes, the theory is right. So these, like all these quack scam products, they're based, like, you know, audio fool products and things like that, they're based on an element of technical truth.

**Dave Jones:** But you're not paying, but most houses are not like this. It's not going to make a difference, and you're not even paying for this apparent power anyway. You're paying for the real power, so it makes no difference. But watch what happens if I actually lower this thing, lower the speed on this.

**Dave Jones:** There we go, back down, now the power factor is much worse. This is with the capacitor in there, okay? So now I've got that on, hang on, I'll put that on the lowest. So that's the lowest setting, there you go, .53. Okay, that's with the capacitor, and without it, .7.

**Dave Jones:** There you go, once again, it's made it worse. It depends on the type of load that you're actually doing. If you've got a pure inductive load, then yes, these things can make a difference, even though you're not paying for it. It's only really the industrial customers that are going to pay for this apparent power.

**Dave Jones:** Because I changed the speed on this, because I changed the speed of the fan there, now it's not drawing much at all, therefore the electronics in it are taking more as a percentage of that, and it's becoming less of a pure inductive load,

**Dave Jones:** it's becoming a complex DC to DC converter load more now. So that's why the power factor has dropped very significantly compared to when the fan was on maximum. But of course, the interesting thing about all this real versus apparent power and everything else, okay,

**Dave Jones:** is that we plug this wankerizer gadget in, okay, and it gives us a much worse power factor, okay, so it's pretty bad, so it's, you know, environmentally and grid-wise and everything else, in this case, if everyone had one of these air purifiers and they plugged in one of these,

**Dave Jones:** then there'd be a fairly substantial increase on the grid to actually provide that power. But you don't actually pay anything more because this is what you'll pay, this is real power, okay? Well, you'll pay a little bit more because of the little LED in here, as we saw before, right?

**Dave Jones:** So it's drawing, it's taking 23.3 watts at the moment, that's real power, that's what you're paying for on your bill, okay? So I'll go plug it in, and you'll see it, it'll probably go up slightly. Yeah, it's gone up, you know, because it has to display the LEDs and a few other little factors,

**Dave Jones:** but, you know, basically as far as your electricity bill is concerned, it's, you know, it's going to be exactly the same. It hasn't done anything. Just like we saw before, it actually slightly increases the consumption. Oh! These things are a complete fail! Because the thing is, an ideal capacitor actually takes

**Dave Jones:** no energy, it takes no power, consumes no power whatsoever. So if we repeat that, and I actually disconnect the LEDs, disconnect everything else, all we've got is just the capacitor across the thing, you'll see that the power basically won't change at all, because as we saw before, this is a pretty darn good capacitor.

**Dave Jones:** So here we go, we're taking 23.22, it's going to fluctuate a little bit. Let me go plug it in. Here we go, this is with nothing, with just the capacitor itself. And no more LEDs. There we go! Just a quick smidgen, because maybe, like, we don't have an ideal capacitor there, but it's pretty darn close.

**Dave Jones:** It's bugger all. Ideal capacitors don't take any power. And it actually really matters where you place this thing relative to the load that you're trying to compensate, as well you can't just have it willy-nilly on the other side of the house, it's not going to work the same.

**Dave Jones:** To think that just whacking a capacitor on one of the power points in your home can, ugh, fix anything, I don't know. What if they try and market these, you know, you need one of these per appliance, you know, to plug it in

**Dave Jones:** right next to it, ugh. So although most residential customers are only paying for this real power here, you are not paying for this apparent power, which means that these boxes are just complete bullshit, even if you do correct the power factor of the particular type of appliance, you're just not going to save any money.

**Dave Jones:** They are a scam. But there might be some countries out there where residential customers are actually paying for that, I don't know, I can only speak for here in Australia and in New South Wales where I live anyway. But even if you don't pay for it, this apparent power is still

**Dave Jones:** a real problem. And of course, poor power factor like this, VA is volts times amps. So the utilities ultimately have to provide more current down the line, down the transmission line. And of course, more current down the transmission line equals I squared R losses.

**Dave Jones:** The losses are squared. So of course the utilities really take this seriously, this power factor, and they put in power factor correction. Here's a photo of a particular power factor correction capacitor bank, or condenser bank as they, you know, might be known in the industry, to actually correct for these sorts of things.

**Dave Jones:** Because they don't want to be providing any more current than they have to. So that's why a lot of industrial customers, they will be paying for VA. Your bill will be in volt amps. So yes, it pays if you've got a lot of, you know, motor drives and all sorts of industrial machinery

**Dave Jones:** or something, you know, and you're paying big electricity bills, it can really pay to put in power factor correction. But you don't just plug in one of these stupid $5 things you get on eBay, you know, you install it, you measure it properly, and you install professional capacitor

**Dave Jones:** banks to actually correct for that. So from an environmental point of view and an overall system grid cost point of view, yeah, you know, it's a real major problem that the utilities are certainly aware of. It's no magic secret that, you know, oh, the energy cartels are keeping from us, you know, just buy this magic

**Dave Jones:** box and, you know, oh, you can beat the big energy. Ugh. So if every residential customer had an overall poor power factor, you know, of 0.5 or something, that would be a real concern for the utilities. And they do, as I said, do do certain

**Dave Jones:** things, power factor correction, to actually compensate for that. And what your overall house is doing, eh, if the utility companies were really that concerned they'd be installing VA meters to charge for real apparent power instead of real power. But yep, adding a capacitor across your power point at home is just complete and utter

**Dave Jones:** bullshit. Oh, goodness. These things are just garbage. Do not buy them. Yes, I had to get medieval on the arse of that thing to make it fit with the adapter. Anyway, yeah, do not buy these things. They are a scam. Based on, yes, an element

**Dave Jones:** of engineering truth. But yeah, don't let that fool you. It can even like make your bill worse, as you saw. And one little couple of microfarad cap against your whole house supply, like even if you had a big, everything was, you know, purely inductive, it's going to make a rat's arse difference.

**Dave Jones:** Just don't touch these things. They are 100% scam. So there's only one place these things belong. Thank you for watching.
