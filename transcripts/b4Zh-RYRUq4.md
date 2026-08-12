---
video_id: b4Zh-RYRUq4
title: EEVblog #471 - Overload Detector Circuit Design
url: https://www.youtube.com/watch?v=b4Zh-RYRUq4
source: youtube-asr
---

**Dave Jones:** Hi, welcome to Fundamentals Friday, where we take a look at a basic electronics building block circuit. What we're going to take a look at today is a basic circuit that does overload and peak detection. We're actually going to

**Dave Jones:** build up a circuit based on a requirement and then see what solution we can come up with. Yes, there's more more than one way to skin this cat. So, we'll show you a couple of variations and then we'll build it up on the

**Dave Jones:** breadboard to see if there's any traps for young players as well. So, let's take a look at it. What I've got is an amplifier here. We're feeding in a signal and we're feeding an output signal. What we want to do here on this

**Dave Jones:** output is we want to check to see if this signal is going near the rails or it's going to peak. We want an visual indicator, i.e. LED, to light up when the waveform, this is our output waveform here, the output waveform goes

**Dave Jones:** above a certain voltage threshold here, both positive and negative because you want to get both peaks, not just one side. So, we'll build up a circuit to do this step by step. Now, when you're designing a circuit like this, let's

**Dave Jones:** start out with the basic requirement of what we're actually trying to do. In this case, it's powered from a split 5-V rail. So, +2.5 V, -2.5 V. The value doesn't matter at this stage, but it may matter later when we build

**Dave Jones:** the thing up. Wait for it. Now, what we've got here is we want to detect if a signal is above a certain threshold, i.e. it's getting near the rails, it's going to clip because we want a visual indicator. Our product, for example,

**Dave Jones:** needs to have a LED on the front panel that lights up when the waveform gets near the maximum peak at positive or negative like this. So, basically, it seems like a pretty uh simple requirement, really. We want to light up a LED when the

**Dave Jones:** voltage is above, for example, 2 V here and below -2 V down here. So, in this region down here, we want the LED to switch on. Pretty simple. How do you do it? You've probably already thought of it. A basic voltage comparator. So,

**Dave Jones:** let's take a look at our comparator here. Positive, negative. Negative will have our reference voltage V. Now, let's take the example of just the positive peak first. Let's uh treat both of these problems separately. Let's just solve this one up

**Dave Jones:** here first. We've got 2 volts. Okay? Our amplifier is minus 2.5 volts. Plus 2.5 volts like this. Here's our input um signal. And here's our output. Now, we can actually drive an LED directly like this with this if we wanted to. Now, when the

**Dave Jones:** it's working as a basic comparator because there's no feedback there. You can use an op amp or uh usually you would use a proper comparator designed for the purpose like an LM311 for example. And we'll take a look at this in a minute, the LED. Just

**Dave Jones:** work with me here. Now, 2 volts reference voltage on this pin here. So, when the input signal goes above 2.5 volts, the non-inverting input is higher than the inverting input down here. So, our output goes high like that

**Dave Jones:** during this period here. So, it'll go up high and then go back down low like that during when the sine wave is above that peak value up there. And our LED will light up for that brief period that it is high

**Dave Jones:** like that. And that's all there is to it. We've solved that problem. But, of course, there's a couple of practical problems here. The first one is that let's say this is an LM311 comparator. Your basic, you know, probably the jelly bean comparator

**Dave Jones:** there. It's actually got an open collector output. So, it can't actually drive a LED directly when it goes high like that because the output transistor inside the thing is only like that inside the chip. There's the output pin like this. There's nothing inside it

**Dave Jones:** like that to There's no It's not like a totem pole output to actually drive that thing high. So, you know, when if you used it in this configuration, that LED would never light up because this output pin here can only pull low. It can't

**Dave Jones:** pull high. So, how do you solve that? Easy. You just change those around like that. That's negative. That's positive. And you put your LED like that. Easy. So, what we've done there is just inverted the operation of this comparator so that we

**Dave Jones:** can use the open collector output on a typical comparator like the LM311 or LM339. So, that's great. We've got a solution for our positive point up there. Oh, kind of. What about the negative point down here? Well, we need

**Dave Jones:** an additional circuit to detect that, too. So, here's the same circuit we had before. I've just erased that, redrawn it. Now using a dual comparator, typical jellybean part LM393. And that's the same as we had before, our input signal, our 2-V

**Dave Jones:** reference, and then our output going to our LED. So, that's exactly the same circuit we had before, but now I've added another comparator in here to give us what's called a window comparator, or more precisely an outside window

**Dave Jones:** comparator. Because what this circuit does is it will light up the LED when the voltage is above 2 V or it is below minus 2 volts like that. Exactly what we want. And that's why the these it's or

**Dave Jones:** because this output configuration here where you tie the two outputs to get two open collector outputs together on these comparators it's called a wired or configuration because this lab will turn on if this one is meets a its

**Dave Jones:** conditional this one down here meets its condition. It's a wired or configuration. Now let's take a look at some real scenarios on our input here. Let's say our input is 0 volts. Then this comparator down here the non-inverting input is 2 volts so it's

**Dave Jones:** higher than the inverting input. Therefore our output is going to be high or it's not going to below. It'll be high if we actually had a pull up resistor in there like that. It had actually be high if this wasn't here.

**Dave Jones:** Okay? So the same configuration here but our reference is minus 2 volts and you'll notice that the input goes to the non-inverting input this time and our reference goes to our inverting input. So if our input is 0 volts that's

**Dave Jones:** actually higher than minus 2 volts reference. Remember because it's negative. So this input's actually higher. Bingo. Our comparator the output here is also going to be high. High and high gives us high. So our LED is also it was tied to high so our LED will not

**Dave Jones:** switch on. So in the case of our 0 volts input here or anywhere between that threshold of minus 2 volt plus 2 volts and minus 2 volts that's annoying there then our LED will be off. And you can

**Dave Jones:** run through the scenario again where it's outside of these thresholds above these thresholds. If our input is say 2.1 volts then the inverting input is going to be higher than the non-inverting input so our output will be low. So our LED will

**Dave Jones:** switch on and it doesn't matter what this one's doing over here because that's just going to permanently switch on the LED. And likewise, if our input is minus 2.1 V, so it's uh lower than this it's beyond this

**Dave Jones:** threshold that we want to detect down here. It's out in this region, then the same scenario. This output here is going to go low. And it doesn't matter if Well, they can't physically both turn on at the same time, but even if they did,

**Dave Jones:** it wouldn't matter. It's a wired or configuration. So, that is a solution for our problem. Brilliant. Or is it? Now, this uh window comparator is or window detector, as it's sometimes called, is an absolute standard building block circuit. You'll find it in any

**Dave Jones:** textbook. But usually, it's actually designed to detect within a window like that. So, it gives a useful output when you're within a window, but in our case, we're actually using it in a sort of the opposite effect to detect when we're outside that

**Dave Jones:** window there. So, you can give it the name outside window comparator. It's a bit more descriptive in what it actually does. But really, it's essentially exactly the same thing. And you can actually swap the reference voltages here. This one could become the positive

**Dave Jones:** reference. This could be the negative reference, depending upon your output configuration that you would actually want it. But we won't go into that. Now, I said we weren't finished yet. We haven't fully solved the problem. Why? Because what if this uh the frequency of

**Dave Jones:** our waveform is very quick or we have a very short pulse which just goes above. You won't have time to see it. Yeah, the LED will come on. LEDs have very fast response times, practically instant, but your eye won't see it. If it's a you

**Dave Jones:** know, if it's a 100 microsecond pulse or something, you won't catch it. So, what we want to do is add an extra circuit on the output here that even if we get a very short pulse which goes above or

**Dave Jones:** below our thresholds, we want that to keep the LED on for a certain amount of time. I.e. we want a pulse stretcher. So, how can we do a pulse stretcher? Well, as always, there's more than one way you can skin that cat. And a couple

**Dave Jones:** of ways to do it, you can do a 555 timer to do a one-shot pulse. You can use a 74HC123 monostable retriggerable monostable to generate and stretch that pulse, but we're going to do it a bit simpler cuz

**Dave Jones:** these solutions are 555 timer, you need quite a few extra parts on there and stuff like that. 74HC123, yeah, it's okay, but it's an extra chip, you need some extra parts. Whereas, let's say we had an LM393, if we went

**Dave Jones:** for an LM 339 quad comparator, we've got a couple of comparators left over. So, let's take a look at that. Or more specifically, let's take a look at an RC pulse stretcher. So, what I'm going to do here

**Dave Jones:** is take this output, so pretend this LED doesn't exist anymore. We're going to put it somewhere else. We've got a wired or output here. And let's actually have a cap go into ground. You'll see why in a minute. And

**Dave Jones:** then we'll have a pull-up. Oop, that's not a very good resistor, is it? That's pretty crap. There we go. We're going to have a pull-up resistor. And let's make that, say, 10 meg, quite a large resistor cuz we want quite a large pulse time. And

**Dave Jones:** then C down here, we'll be able to work out a value for C, but basically, what we want is this output signal here, we already know that our wired or output is going to give us a pulse, a low pulse.

**Dave Jones:** It's going to with the open collector output, it's going to pull that low or short out the capacitor there. Actually, I made a mistake there. That doesn't go to ground because it goes down to the negative rail. So, let's pull that down

**Dave Jones:** to the negative rail there. You got to be careful when you're working on these split supplies. You can do little brain farts like that. Now, uh let's I'll do that minus 2.5 V there, but you can actually, you know, you can

**Dave Jones:** think of this as a single level uh system really instead of a split rail if you want to. But, anyway, that's that's just argument's sake, that's the negative terminal there. Now, our wide or output goes low, gives us a pulse

**Dave Jones:** when our signal goes outside of that range, either positive or negative. So, it shorts out. What it does is just shorts out that cap as soon as the it detects that over range or overload indicator. So, what happens when you

**Dave Jones:** short out that cap? Well, there's no more charge on it, so it's got to charge up. How does it charge up? Because this is open collector output, it charges up via the 10 meg resistor. So, when we get

**Dave Jones:** our pulse, this cap will slowly start charging up until, well, it gets to full charge. Now, here's where we get into a little bit of math, but stick with me. Now, where the capacitor is obviously going to charge up, you've seen the capacitor

**Dave Jones:** charge waveform like that. It charges initially from zero cuz this open collector transistor is short at the cap, so it starts from zero and it charges up like that. And the formula for that, V at any instant in time, is 1

**Dave Jones:** minus E to the power of minus T on RC. Woah, nasty little formula. Thankfully, unless we're really after a precise application, we don't care about this formula cuz all we want to do is light up a LED for a bit. Who cares if it's on

**Dave Jones:** for half a second or 3/4 of a second or a second, right? Good enough, near enough. So, you can just use the standard um RC time constant formula. Tau, the time constant, is the value at a specific value of 62.3%

**Dave Jones:** of that charge voltage and it's equal to easy to remember the time constant R times C. Resistance times capacitance. Simple. So what's a practical lead on time here? Well, I don't know, about a second. Nice round value. You can see that lights up

**Dave Jones:** for a second. Not a problem. What value capacitor do we need with a 10 meg resistor? Well, you just rearrange that formula. Capacitance equals tau on R or 1 second on 10 meg resistance, 100 nanofarads. What a coincidence. 100

**Dave Jones:** nanofarads is a typical bypass capacitor value. So you're probably already using that up here to bypass your chip like that. Not a problem. So you've already got it in your bill of materials. Beauty. So there you have it. This

**Dave Jones:** output here is going to have Well, we'll get to that point after 1 second. So all you need is another circuit here which detects that threshold. It's threshold again and then lights up our LED during well, that time

**Dave Jones:** period there to there. Too easy. How can we do that? Well, a very simple way is with an inverter like that and our inverter can directly drive our LED like that. So when this output here is low, this

**Dave Jones:** output here is going to go high. Oh, sorry. Inverter has a not on the output of course. An inverter that once it gets to a certain threshold level, it lights up the LED. But of course, you need a

**Dave Jones:** Schmitt inverter in there like I said before HC14 for example because a Schmitt has a very specific defined threshold level so it won't oscillate or do something weird above or below that. It'll just cleanly switch the LED off

**Dave Jones:** and on. And we mentioned before, we've got a quad comparator, LM339. So, we actually have a comparator left over. So, we can actually use that as well. So, we don't worry about the Schmitt inverter anymore. We can actually use a

**Dave Jones:** third comparator up here to switch on the LED. So, when this is low, if we have a inverting a non-inverting input up here to a voltage threshold, which if you want the exact time period of 1 second, you'd have to set it to 0.623

**Dave Jones:** of the of of your voltage total voltage supply, of course, to get that exact 1 second threshold there. And if you did that, then that LED would turn on during that period there. Very simple. And of course, that's the trick whether or not

**Dave Jones:** you choose to use a third comparator up here or you whether you choose to use a Schmitt inverter here. Um getting the exact threshold level for the exact time period you want, uh if you want it really, really precise, you have to be

**Dave Jones:** careful. But, because we're just flashing an LED here, it doesn't really matter. We can, you know, just use that RC. It's going to be near enough. Who cares if it's 1.2 seconds or it's 0.6 seconds or something like that? Uh good

**Dave Jones:** enough. So, this is one of the examples of just back of the envelope calculations that can get your circuit working like this. You don't need to worry about this complex formula in the charging graph. All you got to know is

**Dave Jones:** that the time constant is, you know, going to be roughly R * C. And you can pick some, you know, common uh E12 values or something that are just going to do the job. And of course, the reason

**Dave Jones:** that we're using an extra device here instead of, say, um connecting the LED directly on here is because these are high impedance inputs, so they're drawing no current. So, our charge time is going to be accurate. If we just tried to put LED directly on

**Dave Jones:** here, another uh transistor, for example, like a um a, you know, bipolar transistor on there, it's going to take base current or the LED is going to take current, and it's just not all going to add up. So, you know, really it's better

**Dave Jones:** to use a proper buffer here. They're are essentially acting as a buffers on this a high impedance buffer on this RC time constant point. So, whether or not you choose to use that third like a quad comparator for example instead of

**Dave Jones:** the dual comparator because you can get these in a dual package or a quad package and have one left over. But, then you got to generate the voltage so you got to need a couple of extra resistors up here for example. So, you

**Dave Jones:** know, it's all a bit of a trade-off or whether or not you might want to use the Schmitt inverter cuz you have five inverters in your package left over. You might be able to use them somewhere else in your design. It's one of those

**Dave Jones:** trade-off things. It depends on your implementation and how you want to use it. Common values you've got, you know, you might choose a 10 meg up here because well, we want to make use of the additional capacitor down here.

**Dave Jones:** Generally, the resistors are going to be more versatile so you choose the 10 meg up here over say a very high value cap up here if you didn't have high suitable high value caps already in your bomb. And it's going to be cheaper to buy a

**Dave Jones:** resistor than it is to get a high value cap. So, you're better off going 10 meg and 100 in there instead of, you know, 100k and, you know, tens of microfarads down there for example. So, just an interesting trade-off scenario that you

**Dave Jones:** typically get in designs like this. So, as I said, there's more than one way to skin this cat. We've got a solution here. It may or may not be suitable for your particular design. People might go for a discrete transistor solution here.

**Dave Jones:** They might use something else instead of the window comparator, etc. etc. If you wanted a clipping thing to see that your actual waveform actually distorted and clipped, that's a slightly different requirement again instead of just oh, it's getting near the rail switch on the

**Dave Jones:** LED kind of thing. So, you know, just this sort of basic functionality could be done half a dozen different ways. Eh. All right, breadboard time. We'll make it very quick. Exactly the same circuit configuration as we had before with the

**Dave Jones:** uh Schmitt inverter option instead of the comparator 74HC14 rated from 2 V to 6 V, so perfect for this application. Uh dual comparator LM393 jelly bean stuff. Once again, rated for 2 V upwards, perfect for this application. Uh our positive and

**Dave Jones:** negative uh supply is going to be 5 V total, and here's this meter here is measuring the uh power supply uh total. It's a split supply, of course, positive and negative, so it's plus minus 2.5 V relative to this ground point here. And

**Dave Jones:** uh then we've got our LED on the output. We'll have our pulse uh RC pulse stretcher 10 meg 100 nF in that time constant, roughly uh a second or thereabouts. And then we've got um a resistor divider here from the

**Dave Jones:** rail uh giving us a negative uh 1.25 V reference and a positive 1.25 V reference. I just chose the uh split values. It's just nice and even. We're splitting the rail in half. So, if the input signal, which is this pot here,

**Dave Jones:** goes above or below 1.25 V, our LED should turn on. Let's try it. Here we go. Oh, by the way, this is the uh voltage on the pot here, so this is the voltage on the input. Let's go uh on

**Dave Jones:** the positive side. 1.25 V. It should. Here we go. Very close. Oh, there we go. Wow, within half a bee's dick. Very close. There you go. It's close as you can expect, so not a problem. Let's go down negative. Minus a

**Dave Jones:** bit faster. Minus 1.25. It'd be better if I had a like a 10-turn pot here, but if I only got a single turn, it's a bit crusty, but there you go. It just turns on about 1.22 or thereabouts. Close enough. Look at

**Dave Jones:** that. Perfect. So, there you go. Over that full range, it switches and in the middle, it switches off, of course. Above 1.25 or the voltage set on those reference pins, it switches off. Works perfectly. Beautiful. And let's just test the pulse stretcher

**Dave Jones:** there. What I've just got this disconnected, so I'll just temporarily just tap that. There we go. Tiny little pulse going in and we're getting our LED for all my on for basically a second. Near enough. So, that works

**Dave Jones:** pretty much perfectly because the Schmitt inverter threshold, you know, is round about that time constant really, give or take. So, we are going to get our 1 second there. Fantastic. Now, if we have a look at the data sheet for our

**Dave Jones:** LM393, then look, you you know, it's pretty much ideal for this application. Voltage range goes down to a tiny 2 V and that can, of course, be a plus minus one volt rail. The op-amp doesn't really, you know, know the difference between a

**Dave Jones:** single supply rail and a plus one and a, you know, a split supply like that. Goes right up to 36 V. Yeah, not a problem in this application. We couldn't go that high cuz we're limited via the 6 V of

**Dave Jones:** the 74HC14 inverter. Low input bias current, 25 nA, so that means, you know, it's it's basically taking, you know, nothing from the input. We can have very high value resistors. Here, I've got 100 K's in here, by the way, if you can't read that

**Dave Jones:** not watching in HD. These 100 K's and you know, it's there's effectively no input current there, no input current from our input signal. It's you know, it's really quite nice. Minimum maximum offset voltage plus minus 3 mV. Yeah,

**Dave Jones:** it's not that great, but for this sort of application, ah, doesn't matter a rats, really. The offset voltage uh input common mode voltage range includes ground, which means our input can go all the way down to the negative

**Dave Jones:** rail, not a problem. Fantastic. So, let's try and test this down near 2 V and see what we get. All right, we've got ourselves a 2 V supply now, so plus minus 1 V. Of course, our 74HC can work

**Dave Jones:** down to that. Our LED's not going to be very bright, of course. Got the same value dropper resistor. Uh you know, it's a red LED, 1.8 V or thereabouts, but we still have enough to light it up because 74HC is uh a across the dual um

**Dave Jones:** well, across the full supply, so that's working down at 2 V. This comparator is supposed to be working work to down to 2 V. Well, let's try it. Our LED is off at the moment. There's our 2 V supply, plus minus 1. There's

**Dave Jones:** our input voltage. Now, because um our threshold voltage is going to change now, so we expect half of the split rail, so 0.5 V um well, plus 0.5 V minus 0.5 V. So, let's go down to minus 0. 5 V and it should

**Dave Jones:** switch on. At around about Well, hopefully. Let's try it. Will it Will it Is it still going to be Oh, yeah, it's still still operational around about the 0.25 V Yeah, there we go. 0.5 V. Not a problem. So, that works

**Dave Jones:** a treat. You can see it's a little bit dim there, of course. Now, what about on the positive side? Let's try it. Zero should turn on at plus Oh, hey. Should have turned on. It's already switched on. Look, it should have turned

**Dave Jones:** on at 0.5 V, but it doesn't. It switches on at around about You saw it at around about zero there.

**Dave Jones:** There we Hang on. There we go. So, you know, all my Let's call that zero. It It switched on at zero volts and not the half volts we expected. Why? Trap the young players. Now, the trap here is that this is not a rail-to-rail

**Dave Jones:** comparator. It is just your regular stock standard ancient bipolar comparator, very simple, and it has a a limitation in its common mode input range, which if we have a look at our electrical characteristics here, LM393 down here, so this group over here.

**Dave Jones:** Where is it? We've got our input common mode voltage range. Here we go. Minimum of zero, of course, you'd expect that cuz if you remember way back at the front here it said that it could sense to ground. It could sense in your ground

**Dave Jones:** common mode range includes ground. There it is. And it these specs actually back up that top level claim. It does go There it is. It goes down to zero there. But look at the maximum side of it is V+

**Dave Jones:** - 1.5 V. So, it's your supply voltage V+ - 1.5. What that means is effectively your input signal on your circuit here this one here can't go above one the supply voltage minus 1.5 V. And that's why with a supply voltage of

**Dave Jones:** only plus 1 V there and minus 1 V, you know, relative to that ground reference point when we're feeding in a zero. So, that's only 1 V below the positive rail. So, it's a wonder it even worked that well at all. It should have

**Dave Jones:** been actually worse than that really according to the data sheet, but we were lucky enough to get, you know, at least up to zero V there. So, that's why it worked on the negative side, this value up here it worked at minus 0.5 V. Our

**Dave Jones:** reference worked fine, but this point here our reference point at plus 5 volts, it just could not get the common mode input range didn't include right up to the supply. So, that's a trap for young players. That's why it didn't work

**Dave Jones:** at all at those lower voltages. Something to watch out for. And if you think about it, it shouldn't have actually worked with our 5-V supply either because then we had a supply voltage of effectively at 2 and 1/2 volts and our

**Dave Jones:** reference voltage down here was 1.25. Well, that's only 1.25 volts below that positive rail. So, it should have actually been 1 and 1/2 volts. So, it shouldn't have actually worked at all, but it did because the the practical

**Dave Jones:** comparator is, you know, a bit better in this particular application than the data sheet says with that nasty trap there. Common-mode input range. This applies to our op-amps as well, not just to comparators. Very key spec for an

**Dave Jones:** op-amp and a comparator. So, what's the solution? Well, we could just use an expensive rail-to-rail comparator that just does the business. Not a problem, but, you know, it's not a jelly bean part. May not be in stock. Whatever.

**Dave Jones:** Yada yada. More expensive. Um we don't need to do that. We can just solve the problem with some extra resistor dividers. So, instead of our input voltage going straight in, we actually divide it by a significant amount. So, I put in a 1-meg series

**Dave Jones:** resistor and a 270K to ground. So, that will act as a divider in there. And also, the these values I'll change here, 100K and 22K. So, it's a very similar divider ratio. This one's just slightly higher than the others. So, that means

**Dave Jones:** when we get near the peak voltage, you know, 90% or something, it'll turn on our LED. And likewise down here. So, let's change the values and see if it works now. So, instead of asking the op-amp to sense the input over the full

**Dave Jones:** range, what we're doing is just uh dividing the range down over a much smaller area. So, we always have the headroom in there above the positive supply. And just a pro tip here, when you're using breadboards like this and you're

**Dave Jones:** getting your resistors from these bandoliers, they can actually have glue inside there that when you pull the resistor out, it gets stuck on the ends there and when you plug them in, they may not make good contact with the

**Dave Jones:** springs inside. So, just trim those off like that and it'll work a treat. All right, let's give it a try now. Back up to 5 volts again just to make sure it works at 5 volts and we're not sure of

**Dave Jones:** the exact voltage, but it should be down around 1.1 or near to the full rail actually. So, there we go. So, not 2.5. So, it's around about or negative. There you go, around about negative 2.1. 2.1 or something like that.

**Dave Jones:** So, our positive side should be plus 2.1. Should be exactly the same. And is it? Oh, yeah, you know, near enough. Good enough. Okay. Not a problem. Now, let's wind it down to 2 volts. Now, unfortunately, at 2 volts, we're

**Dave Jones:** not actually going to get a free lunch here because we're we're still working around that that reference that ground reference point. So, we haven't really shifted that. So, we're still only going to get that plus 1 volt relative difference.

**Dave Jones:** So, unfortunately, at 2 volts, it's not going to make any difference. Let's try the negative side here. It's around about right. It should be 1 volt. It's going to around about Well, 1 1 volt is the maximum supply. There it

**Dave Jones:** is. And it turns on at about yeah, 0.75 or something like 0.8. And we expect it to turn on at plus 0.8 as well, but no, it doesn't. It's down near zero again because we've got exactly the same

**Dave Jones:** issue. Where this helps though, this divider helps is at um the higher voltages where you need to sense near the input. You know how we had 100k 100k here before? Well, if we had, you know, a 10k and a 100k and we're sensing it

**Dave Jones:** right near the positive or here, sensing right near the positive rail, it wouldn't have worked before with those um at even at 5 volts because our it would have tried to sense the input there up near 5 volts. So, this

**Dave Jones:** technique doesn't actually help down at 2 volts. We'd have to shift everything. It gets real nasty. But, at slightly higher voltages, it's always going to help you when you're trying to detect up near the peak range because instead of

**Dave Jones:** the input having to detect up here now, it's only got to detect down here. So, it gives you that extra voltage margin in there. And just to prove that, what I've done is I've removed my divider there and

**Dave Jones:** I've swapped these two resistors and these two around so that the 20k 22k is on the top and the 100k is on the bottom. So, it should sense with the 5 volt rail at around about two uh that uh

**Dave Jones:** 2 volt mark instead of 2.5 volts peak. Does it? Well, let's have a look. My That's the full uh minus two. Let's see where it switches off. Yeah, it switches on around about that minus 2 volt mark. And we'd expect, just like before it was

**Dave Jones:** symmetrical, we'd expect on the positive side to also switch at 2 volts. But, you'll find that it won't. Will it make a liar out of me? I don't think so. There we go. 1. There it is. 1.5 volts instead of 2 volts. So, even

**Dave Jones:** at a relatively high supply voltage of plus minus 2 and 1/2 volts or 5 volts total, then this thing isn't going this basic circuit, as we saw without this divider, isn't going to work at near the rails there. It worked when we had 100k and

**Dave Jones:** 100k and we're only sensing half of the rail voltage or 1.25 volts, but when we wanted to sense 2 volts, nah, sorry. We Oh, sorry, down here. I keep getting these confused. If we want to sense 2 volts here, sorry, our supply voltage is

**Dave Jones:** only 2 and 1/2. That's not that's um, you know, not within the common mode input range, so it only worked as we saw at that 1-volt difference to 2.5 minus 1.8 minus 1 is 1.5 and that's where it switched on because that is our

**Dave Jones:** common mode operational or our practical operational input range. But, if you want to go just by the data sheet, of course, where is it? Then, you'd have to allow the 1.5 volts full. But, in this case, we're getting around about a volt in practice

**Dave Jones:** measured. And I'd love to be able to show you the charge waveform on that cap there, but I can't because my scope probe * 10 is 10 meg input impedance. 10 meg 10 meg As you can see, look, the LED just stays

**Dave Jones:** on permanently unless I Whoop. There you go. It stays off and then once it triggers on, it just stays on because of the bloody scope probe. But, if I change those values to 100k and 470 nanofarads, then ta-da! There we go. But, of course, that

**Dave Jones:** won't be entirely accurate as the real circuit. Your timing's going to be a bit off because of the 10 meg still 10 meg loading of your scope probe. So, just be careful. There's uh practical effects when you probe things. So, there you go.

**Dave Jones:** I hope you enjoyed that. That's another Fundamentals Friday. If you want to discuss it, jump on over to the EVblog forum. That's the best place to do it. And if you do like this segment, please give it a big thumbs up. Yes, it took

**Dave Jones:** longer than I expected. Yes, I said I'd keep it to 10 15 minutes last week. I did for the theory part. This one, it turns out the theory's about you know, just under 20 minutes. I'm not sure how much longer the practical.

**Dave Jones:** Could be 30 minutes. Ah, what the hell. Catch you next time.
