---
video_id: 4iEshd6izgk
title: EEVblog #751 - How To Debunk A Product (The Batteriser)
url: https://www.youtube.com/watch?v=4iEshd6izgk
source: youtube-asr
---

**Dave Jones:** Hi, quite a few people on email and via Twitter pointing me towards this news article the other day, the Batteriser. It's a $2.50 gadget that extends disposable battery life by a whopping 800%. It sounds fantastic. Woohoo! And of course it must be true,

**Dave Jones:** right? It's in PC World. And look at all these other news articles that are running with it. Look, Daily Mail, eight times longer. Eight times longer. Eight times longer. Eight times longer. Can you believe it? I'm at 800%.

**Dave Jones:** Oh, wow, 800% again. It's got to be true. A gadget that can make your batteries last 800% longer. Oh, man, this is fantastic. But of course a lot of people smell Hmm, [ __ ] Now, as Carl Sagan had

**Dave Jones:** with his baloney detection kit, I wonder if we can come up with our own electronic gadget news story baloney detection list. Let's try it. Let's go through and see if we can verify the claims of this thing because it's a real

**Dave Jones:** electronic product. It claims things like 800%. There's patent, all sorts of technical information in here that as engineers we can go through and verify. And PC World spin a rather interesting article from none other than John Phillips, the editor-in-chief.

**Dave Jones:** It's a killer story of industrial espionage. The robbery occurred last October in the Batteroo office, the company who makes this Batteriser. And well, they knew the building layout. Oh, breakthrough in technology that if it's legitimate could blow the lid off the

**Dave Jones:** alkaline battery industry that's worth $3.4 billion was Now, the first thing we're going to take a look at in our baloney detection list here is who is making the claim? Is it a big company, reputable people, all that

**Dave Jones:** sort of thing? Well, looks like they're a startup company, but look at this. Uh this guy has the guy who founded has a PhD in electrical engineering. Pretty good. He's a vice president at Broadcom CEO Stint Flex Power. And well, sounds

**Dave Jones:** pretty legitimate. And the next thing on our baloney detection test here is well, does it break any laws of physics? In this case, we're talking about batteries, power, we're talking about conservation of energy. Does it uh promise more power out than what you

**Dave Jones:** put in? Well, no, it doesn't. You read uh down here that uh you know, once the battery voltage drops and it effectively becomes useless, etc., etc. Uh it just has a boost circuit inside that boosts uh low voltage up to 1.5 V, and it uses

**Dave Jones:** the unused energy in your battery. And well, this is a very uh well-known problem with batteries and product design that this thing solving. So, yeah, tick, no problems at all. It's not violating the laws of physics. So, this

**Dave Jones:** is actually sounding really promising cuz there's nothing new here at all. Uh there have been products to do this and also circuitry built inside products to actually do this like a boost converter to utilize all of the energy

**Dave Jones:** or more energy inside the battery. And they say it here themselves, there's no IP in the boost circuitry. Our technology is uh the miniaturization technique that allows them to build it into a sexy-looking sleeve which fits over. So, it's all about, you know, the

**Dave Jones:** physical engineering of this really nice-looking sleeve. So, it's all sounding pretty good right up to this point. And if you actually go in here and have a look at their patent that they've got, they've got a couple of

**Dave Jones:** patents by looks of it. This is the original one, and it shows the drop in the battery voltage here, A typical characteristic curve of uh for example, an alkaline, you know, a Sony or a Duracell or an Energizer or whatever uh

**Dave Jones:** battery, and how you might only use a small amount of the capacity. And if you go over to a data sheet of a typical Duracell or alkaline or whatever battery, you'll see that that characteristic curve, and it's real. So,

**Dave Jones:** with this sort of characteristic curve, if your product is designed to have a battery cutout voltage of say or 1.3 volts, they're they're claiming 1. you know, 35 to 1.4, then if it has that sort of cutout voltage, then you can

**Dave Jones:** actually see how your amount of energy that you're using in your battery is quite small, cuz the amount of energy in the battery is actually the area under this uh blue characteristic curve here. So, we can actually um see that all of this in here

**Dave Jones:** is all of this energy under this battery is completely wasted. We're only using this amount of energy here. So, it it is a legitimate well-known problem in the field, and that's what this thing overcomes. It uses a boost converter to

**Dave Jones:** convert the lower volt as this battery voltage drops, it actually boosts it back up to 1.5, so that the product uh always thinks that the battery's good, and it uses all of the area under this curve. No problems whatsoever. So,

**Dave Jones:** here's our next step in our baloney detection list. How does Batteriser give your batteries eight new lives? Let Let's look at the assumptions that they're making. See if their assumptions are valid, because if you base a product idea on false assumptions, well, it's

**Dave Jones:** going to be a useless or it's just not going to work as claimed. So, look, here it is. Once a completely new alkaline battery is rated at 1.5, but once it's output drops below 1.35 or even 1.4 volts, it effectively becomes useless.

**Dave Jones:** Well, as an experienced electronics design engineer, I know that's not really true. I've very rarely, in fact, I can't think of one example I've seen where the threshold, the dead battery threshold voltage, it would be 1.4 volts or even 1.35

**Dave Jones:** volts as claimed here. But, hey, we can go test this. Let's go to the lab. So, let's do some quantifiable tests and take some random products that I've got lying around the office here and we're going to use an adjustable power supply

**Dave Jones:** battery-powered products. I'm going to replace the battery with some probes and we can adjust the voltage. We can start from 1.5 volts and we can wind it down until the low battery light comes on. So, I've got this Logitech uh mouse

**Dave Jones:** here. We can switch this on. Okay, we've got our green light on top. So, it'll show uh it'll come up and flash or turn red when the battery voltage um goes down. So, let's wind it down. I'm winding it down in 0.05 volt

**Dave Jones:** um steps. So, we've got 1.40. No, nothing yet. 1.35 is what they claim. You know, a lot of products. They don't say all products, but they say many. They use the word many. Well, wait. Still not getting there. 1. 1.2 volts.

**Dave Jones:** No, we're not there yet. We're not there yet. Hold on to your hats. We're getting down towards a volt. Bingo. There we go. It's around about like 1.01 volts. Now, they use an example of a keyboard and I don't know which one they

**Dave Jones:** use, but I've got a Logitech K330 keyboard here. Uses two AAA batteries, but hey, we can adjust our power supply now for 3 volts instead of 1.5 and do exactly the same thing. Well, look at that. Even at 2.2 volts, i.e. 1.1 volts per cell,

**Dave Jones:** we're still working. Wow, even at 2 volts, we're still going. No problems whatsoever. This keyboard is going to use a ton of capacity in that battery. Well-designed product. One of these little Zoom one handy recorders here. It's got a handy little battery bar

**Dave Jones:** graph on there, three sigma bar graph. Let's wind the wick down. We have to get down to 1.25 volts before the first bar even vanishes. And we have to get down to about 1.1 1 volt before it shows low battery. And

**Dave Jones:** I've got a Sennheiser wireless microphone here with bar graph. It has to get down to about 2.6 volts before the first battery bar graph goes down. So, that's equivalent to 1.3 volts per cell. And it won't die until about 2 volts or 1 volt

**Dave Jones:** per cell. And let's try this remote control here. We've got the LCD display, but I'm also using a video camera to show the infrared LED here. Now, at 2.2 volts, the LCD starting to get a bit dim, so that's a bit of a problem, but

**Dave Jones:** the LED still works. This is still control the product. It still works at 1 volt per cell. Thank you very much. Here's a much more advanced remote control, uses four AA batteries. It's working down to 1 volt per cell. No problems whatsoever. Check

**Dave Jones:** it out. And this old school vacuum fluorescent display Casio calculator works down to 0.8 volts per cell. No worries. Even this Xbox controller works down to 1 volt per cell. Not a problem. Even an old school Game Boy works down

**Dave Jones:** to 1 V per cell. What's this 1.35 V? I can't find anything. And this multimeter still not showing flat battery at under 1 V per cell. This old school Sony DAT Walkman, it still works down to 1.1 V

**Dave Jones:** per cell, almost empty. And this differential probe takes four AA batteries, still works down to about 0.95 V per cell. Even this little thermometer thingy which has no low battery indicator, but yeah, it starts to dim, but it's still working down at

**Dave Jones:** 1.1 V 1.2 V per cell. Yeah, you'd change it at that point, but jeez, you know, it's not 1.35. So, there you go. I couldn't find a single battery-powered product here in the lab that would drop out at their claimed 1.35 V, let alone

**Dave Jones:** 1.4 V. It's crazy. And I am not cherry-picking here. I genuinely could not find a product, but hey, I know there probably are products out there if really badly designed products. If you search long enough, if you're bored enough, you know, cheap-ass $5

**Dave Jones:** gadgets and Bluetooth keyboards on eBay, you'd eventually find one that was so poorly designed that dropped out at the claimed 1.35 or even 1.4 V that it would be wasting most of this, you know, a majority, as they say, like, you know, maybe 80% of

**Dave Jones:** the capacity of the battery. I don't doubt it, but it's not nearly as prevalent as they imply it is. So, right there, we've demonstrably shown that one of their main assumptions that they're basing their entire product on, their entire business model on, and

**Dave Jones:** indeed, their entire patent. Look, here's the patent that says that right in there. They're basing it all on this 1.35 or 1.4 V battery voltage cutoff claim. The equipment is no longer usable. It's no longer usable in the

**Dave Jones:** product. Are you kidding me? Right there, off the bat, goneski. And indeed, any product that's actually designed to use both rechargeable batteries and primary cell batteries must, absolutely must, cannot get away with it, be able to operate down to at least 1.1 volts

**Dave Jones:** per cell. That is the cutoff voltage for rechargeable products. That's why we saw many of our products there actually cut out at right on 1.1 volts because you don't want to let your rechargeable batteries actually discharge any further. So, you're still using most of

**Dave Jones:** the capacity. There's a Duracell one. Here's AnyLoop ones for example, the Sanyo AnyLoops. Exactly the same thing. You want these things to cut out at 1.1 volts. The AnyLoops are much better. They use like 95, at least 90, maybe 99%

**Dave Jones:** of their capacity down to 1.1 volts. That's why the cutoff voltage is around about that figure typically. So, if you take it the average of those products I tested there and ones designed for rechargeable batteries, you're looking at a cutoff voltage of 1.1 volts. And

**Dave Jones:** look at how much capacity you're losing. It's just this area under the graph here. It's not the a huge 80% that they're running with and they're trying to advertise their product with. It it is using all of this space under this

**Dave Jones:** curve. So, you're only wasting about 20%. So, right off the bat, their figures are completely back to front. Uh, typical marketing. So, this guy who designed the product and founded the company, he must know this. So, he's effectively lying by

**Dave Jones:** not mentioning these things, by omitting it. And that's classic marketing 101 stuff because, you know, you can't get that 800% banner headline that then all the media outlets run with. You can't get that if you tell the truth and

**Dave Jones:** actually say, "Well, yeah, the majority of products they work down to 1.1 volts, you know, no problems whatsoever. Anything designed with a rechargeable battery must work down to 1.1 volts." So, you know, the headline that oh, you get 20% improvement isn't nearly as good

**Dave Jones:** as 800%. No wonder they're not going to mention it. Next thing we want to do on our product bologna detection kit is actually test that banner headline. Can we do that? Of course we can. This is engineering. 800%. Where do they get that from? Well,

**Dave Jones:** let's have a look. Let's see you buy a new battery, you use it for a month, it drops to 1.4. It's now ostensibly dead at 1.4. We've proven that's not true. But, if you slip on the batterizer, that's a two times increase in battery.

**Dave Jones:** You get another month's use out of it. And then if it drops to 1.3, boom, etc. And now they're saying there are now there are more than eight 1.1 volt steps between 0.6 volts and 1.5 volts. So, in

**Dave Jones:** grossly simplified terms, the batterizer can extend battery life somewhere around a factor of eight. Grossly simplified? You bet your ass it's grossly simplified. In fact, it's worse than that. It's downright wrong. And why is it wrong? Well, let's look at this. This

**Dave Jones:** is from their patent. The time it takes for a battery to drop by 0.1 volts is longer at lower voltages versus at higher voltages. This means at a constant current was drawn from the battery, it would take the battery a lot

**Dave Jones:** longer to discharge from 1.2 to 1.1 than it would from 1.5 to 1.4. This means the extent to which the battery life is increased could be even higher. Well, okay. Yeah, that is true. Look, it's steeper here and then it goes like that.

**Dave Jones:** But, then look, they don't mention they conveniently miss out this like remaining 30% of the capacity here where it starts to drop down even faster again. So, once again, they are effectively lying by omission. They're not telling you the whole story. They're

**Dave Jones:** basing all their claims around a very niche, narrow scenario, which and they're trying to put this out there as this thing is going to save the world. It's going to be a multi-billion dollar business. Invest in us. We're going to

**Dave Jones:** be, you know, fantastic. This is such marvelous technology. And it's No, it's not. It's going to have a very niche application because they don't mention the majority, the vast majority, as I've demonstrated cases where their assumptions are not true. So, the banner

**Dave Jones:** media spec of 800 * eight-fold increase in battery life is based on a one like a very narrow window of products that I couldn't find, but I'm sure they are out there if you look hard enough, that fail

**Dave Jones:** at like 1.3 or 1.4 V within that sort of 1.35 to 1.4 in that sort of region. And then, yeah, okay, they're probably right. You're going to be losing maybe 80% of your capacity under this curve here, but that's also they don't

**Dave Jones:** tell you that it's going to depend on the type of battery. Here's one of these ultra power Duracells. They they last a lot longer. So, there's not going to be as much power lost as you'd get for one of

**Dave Jones:** a standard copper top Duracell, for example. And also, their product claims to work down to 0.6 V. And that's what they again basing part of this data, this 800% calculation on. And 0.6 V is quite impressive for the circuit.

**Dave Jones:** Excellent. Fantastic. Nice design. I like it. But the whole industry, the whole electronics industry and power and battery industry takes 0.8 V as the cutoff voltage for a cell. It doesn't go down to 0.6. There's no capacity left.

**Dave Jones:** This thing batteries drop off like a brick wall. It doesn't matter what data sheet you look at. They all drop off like a brick wall at 0.8 volts. So, having 0.6 volts and then including that in your calculation

**Dave Jones:** for your 800% for these 0.1 volt step, it it's completely and utterly and demonstrably wrong.

**Dave Jones:** And another classic marketing technique, or get a reputable university to test it for you and then cherry-pick some quotes from them so that you can, you know, look like it's fantastic. Look, the device was tested by researchers. San

**Dave Jones:** Jose State University says it helps to prevent the voltage of a battery from decreasing under load. Well, of course it does. That's the whole concept of a bloody boost converter. And Dr. Parvin here, a material scientist, um I'm sure

**Dave Jones:** he's very reputable. Uh and he says, "We tested the Batteriser sleeve in our lab and we confirm that the Batteriser taps into the 80% of energy that is usually thrown away." Yeah, probably based on the Batteriser company's recommendation that it's 1.4. So,

**Dave Jones:** they're basically confirming. Of course they're going to confirm that, but it doesn't matter because it's a bad assumption to begin with. And I'm sure that these scientists at San Jose University, they, you know, they're no fools. They know what they're doing, but they're

**Dave Jones:** probably being taken out of context here. I think they're just cherry-picking the data that was hand-fed to them in the press release from Batteriser. And it doesn't help when the researcher says, "Uh also confirms that 1.3 volts under

**Dave Jones:** load condition at that point we consider it to be dead and throw it away." Well, it's demonstrably wrong. So, I'm sure this San Jose researcher is probably being taken out of context. I you know, I can't believe that he doesn't

**Dave Jones:** understand that electronics products are usually, most of majority of them, designed to actually operate much lower than that. Next on our list, beware of claims like this. The company behind the Batteriser said it's tested the gadget with several

**Dave Jones:** battery-powered devices, including game controllers, look this Xbox One and TV remotes, etc. Well, wireless keyboards? Well, I tested it with wireless keyboards, didn't I? And it was just demonstrably untrue that they drop out at the claimed 1.4 volts. So, yeah, they

**Dave Jones:** may have tested the product in there and it might work in "quote marks", but it doesn't mean that it gives any usable increase in life, let alone the banner spec of 800%. Now, you'll be thinking at this point that this thing is done and

**Dave Jones:** dusted. It's just not going to be even close to the claimed figures and it might only work in some real niche application. Well, we can go even further and show how when you look at the engineering of it, it gets even

**Dave Jones:** worse. Now, let's take a look at a typical boost converter chip that might be used in something like this. It's designed to go down to a low input voltage, work off a single cell. Now, let's go down here and take a look at

**Dave Jones:** some of the efficiency versus output graphs and this one on the right-hand side here, efficiency on the Y axis here and then we've got the output current on the X axis here. The efficiency of this thing is going to change based on the

**Dave Jones:** output current and you can see how at really low output currents, like in, you know, hundreds or tens of microamps, like you know, typically get in one of their example products, a remote control, well, you're looking at like,

**Dave Jones:** you know, 50% efficiency. Some converters are even much worse than this. This is a typical characteristic response curve of a boost converter like this. If I go over to this data sheet from Linear Technology, for example, then you can have a look at their

**Dave Jones:** efficiency curve. Look, there's a big bump up there. Yeah, you might get your 90% efficiency, but only over a very narrow operational range of output current, i.e. how much power your product is actually taking. But once again, it drops off down at the low

**Dave Jones:** output currents. And your efficiency is going to change a fair amount based on your battery voltage as it drops. You can see the blue curve here at 0.7 volts battery voltage, the efficiency is a good 10% less than what it might be when

**Dave Jones:** it's up at 1.5 volts. And what does that translate into in your final product? Well, let's assume that's only 50% efficient down at that point. Well, your 800% claim, even if you could find the niche product to do it and cut off at

**Dave Jones:** 1.4 volts, you're still looking at losing half of your efficiency down at that thing unless you specifically design your circuit for a specific type of product. You when you use a general purpose chip like this and you have to

**Dave Jones:** design a general purpose product to work over the range of any unknown product. You don't know whether that product's going to be a wireless keyboard that draws a small amount of current down here or whether or not it's going to

**Dave Jones:** draw hundreds of milliamps right up here. You just don't know. So, you've got to look at the efficiency and higher currents, it's just going to drop off like a brick wall. So, any potential gains that you're going to get from this

**Dave Jones:** batterizer based on uh the drop out voltage of your product is going to be offset by the efficiency of this thing depending on what type of product you've got. So, once again, it even narrows the range of usable products even further

**Dave Jones:** than what it already is based on their ridiculous original ridiculous claim of 1.35 volts cut out voltage. So, let's say you found a product that, well, you could double your life if you used if you're only using half the capacity of

**Dave Jones:** the battery and this batterizer can use the extra 50% of that capacity. Well, if it's only 50% efficient, then you're screwed. You just you're back to square one. You're going to get exactly the same life out of it

**Dave Jones:** as you did with just using the regular battery and pissing away your extra 50%. It's not going to help at all. And the other thing to consider is the equivalent series resistance of the battery. Now, this gets a bit

**Dave Jones:** complicated, but look at this red graph here for this uh Duracell Coppertop uh AA. They don't actually show it extending out here, but the resistance rises as the capacity goes down and the voltage drops. And it's going to sort of

**Dave Jones:** like tail up like this as the voltage drops off like that, like a brick wall. It's going to sort of like tail up in the opposite direction. And the exact effect of this depends upon the product that you're actually powering, whether

**Dave Jones:** or not it's uh taking uh pulse loads, for example, like high current pulse loads. That's going to be a big deal where if it takes a, you know, your battery voltage might be falling like this, but then if it switches on a

**Dave Jones:** motor, for example, then boom, you might get a low dropout like that, which may product and things like that. That depends on how much decoupling they've got internally. And all sorts of technical details like that. And is this

**Dave Jones:** uh batterizer going to help in that respect? I don't think a huge amount, because it's physically not a large DC-to-DC converter. It has to be like one of the world's smallest DC-to-DC boost converters in order to fit in this

**Dave Jones:** form factor. So, naturally, it's going to have extremely limited output capacitance and uh peak current uh capability. So, you're relying on the internal uh decoupling of your product to handle those uh pulse loads effectively. Now, will the batterizer actually make a

**Dave Jones:** difference in this case? Well, it it may, but in the majority of cases, I don't think so, because yeah, it's boosting the voltage up to 1.5 V, which is great for those products which have a low dropout voltage. But in terms of uh

**Dave Jones:** peak current at end of life, for example, um yeah, it's boosting up to 1.5, but there's going to be a corresponding increase in the current, cuz you have to keep constant power output from your DC-to-DC converter. So, the current from the battery is actually

**Dave Jones:** more, and ESR plays more of an effect. So, you know, as I said, it depends on the how your product is designed and the decoupling. So, but mostly, because of the physical size of the thing, I don't think it's going to make a huge, if any,

**Dave Jones:** difference at all. In fact, what they don't tell you is that instead of increasing it, it depends on your product. So, while they might, you know, you might be able to find a product which says, "Oh, yeah, look, I doubled my

**Dave Jones:** battery life, or even tripled it, or even quadrupled it." No way you're going to increase it by eight times, but hey, you might be able to double it. But, hey, you might have some other product where the battery life halves because of

**Dave Jones:** the particular efficiency and the design of the thing. And what's another downside? What is the maximum output current of this thing? They haven't told you. I bet you they're not going to tell you until you hand over your hard-earned

**Dave Jones:** money and find out, "Oh, it can't be used in my high-power product because it's only got a maximum output current of a couple hundred milliamps or something like that." So, you can't use it in a toy that's uh designed to work

**Dave Jones:** with double A's, and then, you know, you might have to suck an amp at peak or something like that. Your product could easily fail if this batterizer cannot deliver peak currents, for example. Heck, let's just take a standard copper

**Dave Jones:** top double A battery here. If you've got a product that actually cuts out at 1 volt, which was like a lot of the products that I just showed, then, well, you're using already using like 90% of your energy, and the best-case

**Dave Jones:** efficiency you're going to get out of a DC-to-DC converter, even if it's optimized, is going to be like 90 percent, uh sort of like at best. So, it's already a useless product right there, and could actually be detrimental

**Dave Jones:** if you use it down the efficiency curve. So, they're not going to tell you that. They're not going to tell you that this thing may actually decrease your battery life, and you won't know that until you actually put it in and do the battery

**Dave Jones:** drain comparisons yourself, and figure out whether or not this damn thing works. Oh, man. And take a look at the PCB. Look at how much room you've got to fit the chip and the magnetics, i.e., the inductor, because you need an inductor in this

**Dave Jones:** thing. Here's the inductor over here. That's everything in this boost converter. And the smaller and smaller and smaller you make your inductor, they've probably got a tiny little 0402 or 0, you know, 201 uh inductor in there. You've got to get really low

**Dave Jones:** profile in there. It's going to be a tiny amount of magnetic. The smaller your magnetics leads to a much lower efficiency, the smaller it is, and also limits your output current. So, how much output current can they fit in these

**Dave Jones:** things? Well, my engineering estimate is not very much at all. And they're not going to be very efficient, either. But they're not going to give you the numbers on this, cuz that just ruins their whole marketing campaign. How do

**Dave Jones:** you dissipate your heat in this thing? Well, it could be quite uh novel. You could actually use the metal uh bar like this as a heatsink. I'd certainly be using that. But then you've got to make sure your chip is uh properly

**Dave Jones:** thermally bonded to your metal uh package here to get out the heat, especially at those higher currents. Might be fine for low current devices like a wireless keyboard, for example. You put in one of those Xbox uh controllers that's got the, you know,

**Dave Jones:** the the transmitter and everything. It's got the vibrator motor, all that sort of stuff happening, or some other high-power product. Uh, this tiny amount of space on here. It not There's going to be very severe limitations imposed on this product, and

**Dave Jones:** they don't give you that data. They just put out this press release with glowing, you know, numbers and they just gloss over all these technical details. And then what about the quiescent current for low current products that aren't drawing much? Look at this. For

**Dave Jones:** this converter, yeah, you can get better than this, but you know, this might be a typical figure. 300 microamps typical for your active quiescent current. And that doesn't include your efficiency of the thing which as I said, at absolute

**Dave Jones:** best if you use it at the optimal part of the efficiency curve, 90% might typically be be, you know, like 70 to 80% something like that. So, they can happily throw around marketing buzz terms like up to 800% improvement, all

**Dave Jones:** that sort of stuff. Well, from an engineering point of view, we can practically guarantee that there will be some products out there. I don't know how many, but then will certainly be some where this thing will have a

**Dave Jones:** detrimental effect on the battery life. They don't tell you that. That ain't good marketing. And if you take a look at a typical alkaline battery like this, the positive terminal on the top is all of this metal can. If this is still the

**Dave Jones:** positive terminal here, and the only thing isolating the positive and negative terminal is this tiny little gap, this tiny little rubber O-ring around the bottom. So, you could easily get in there and short it out. You can probably see the little tiny spark.

**Dave Jones:** Wait, there we go. We just generated some smoke. Woohoo! There we go. I made something smoke. If you short out this negative terminal to the positive here. So, if you take a look at the design of this thing, this whole metal body along

**Dave Jones:** here is connected to the negative tab there. So, you're relying upon just the outer, like, you know, Mylar insulating wrap or whatever it is around the battery there to stop any spurs from shorting out between all this cut metal

**Dave Jones:** along here. I mean, if any there could be a tiny burr on there and it could short through to the negative terminal. It's an accident waiting to happen and they want to use this on like they're saying up to D cells. Are you kidding

**Dave Jones:** me? The amount of energy in a D cell is incredible. Let alone a double A is enough to ruin your day, possibly start a fire. Geez, I wouldn't want to rely on a product like that. Woo. So, there you

**Dave Jones:** go. That is the Batterizer product that made all the headlines and basically hardly anyone almost nobody in the news world wanted to actually think and verify this and it's not hugely hard. Just ask any competent electronics engineer and they would have been able

**Dave Jones:** to tell you this. I know I've taken 30 minutes to do this. I basically came to this exact conclusion in like tens of seconds after I immediately saw this product. I just knew the limitations that would be involved in this thing.

**Dave Jones:** It's obvious to any practitioner in the field. Yet, they're just running with all this marketing spin and they don't tell you any of the downsides. So, that's why I've presented hopefully a useful product baloney detection kit here. You got to look at the claims.

**Dave Jones:** You know, look at their assumptions. Verify the headline claims of 800%. It's not even close to that and just look at the downsides of something like this. Don't just get caught up in the hype because it sounds fantastic. And

**Dave Jones:** usually, if it sounds too good to be true, it usually is. And while they're like technically right in some of the things that they say and what they're doing here and the product is going to work in some very specific circumstances

**Dave Jones:** and it may actually give an improved battery life, but they don't tell you about all the downsides and everything else with it. Wait, stop the presses. Um since So finished this uh video yesterday just overnight, they've updated their

**Dave Jones:** website. It was just coming soon, but now they've actually got some details here. It's one of these typical uh slick, you know, one-page uh marketing websites. And let's have a look. Here it works. The most new batteries contain

**Dave Jones:** 1.5 volts of energy. Right there, they're wrong. They just have no idea what they're talking about energy and 1.5 volts of energy. That's just ridiculous. The problem is that many devices stop functioning around the 1.3 volt mark. Look, they use the word

**Dave Jones:** many. Many. Yeah, how many? I couldn't find one here in the lab. Maybe I could if I looked a bit harder, but the majority of devices that we showed this is demonstrably not true that many devices do this. It's

**Dave Jones:** not. It's probably a small minority of devices. Yet they're basing their entire product and everything around this stupid 1.3 volt figure. And it uses Yeah, it lets you instantly tap into the existing 80% energy that's usually thrown away. [ __ ] Any device that

**Dave Jones:** uses a rechargeable battery automatically will must go down to 1.1 volts and and use probably, you know, 80 90% of your capacity. More if you use those Sanyo eneloops. And wait, they've got a marketing video. Let's run it.

**Dave Jones:** Did you know that every dead battery you've ever thrown away had only used up to 20% of its battery life? Whoa, hang on. What did they say? Did you know that every dead battery you've ever thrown away had only used up

**Dave Jones:** to 20% of its battery life? That every dead battery you've ever thrown away? That every dead battery you've ever thrown away? That every dead battery you've ever thrown away? Unbelievable. They've gone from using the word many to every. You heard it there. They're

**Dave Jones:** claiming every battery you've ever thrown away has wasted 80% of its capacity. Ah, this is demonstrably untrue. What if you could instantly tap into the other 80% that is still trapped inside? Now you can with Batterizer. When your

**Dave Jones:** batteries are running out of juice, just slip the Batterizer micro thin sleeve onto your low or dead battery. Insert it back into your device and see your power level jump from low to 100% instantly. We tested the Batterizer in our lab and

**Dave Jones:** we confirmed that the Batterizer taps into that 80% energy that is usually thrown away.

**Dave Jones:** So I kind of feel a bit sorry for our professor colleague here. I'm I'm sure he means well, but he should know better than this. He got duped into doing this marketing video for this company and but even he admitted that he used the word

**Dave Jones:** usually thrown away. The 80% is usually thrown away, but that didn't stop the company then going to use previously in the video just before him say every battery. Ah. So as an electronics design engineer and product designer, I can't help but look

**Dave Jones:** at this thing and just go ah, jeez, it's just mostly marketing. And yeah, sure it's going to work and give some extra output in, you know, maybe quite a few circumstances, but probably not the majority of them. And yeah, it

**Dave Jones:** could work reasonably well in something that's uh, you know, is a marginal current uh, drain and it's dropping out at, you know, 1.2 volts or something like that. Yeah, you might be able to, you know, squeeze an extra maybe up to,

**Dave Jones:** you know, 50% efficiency out of it, but then you can't help but look at the efficiency figures like this and go, well, it's, you know, you're going to have some loss there as well. It's not going to be that

**Dave Jones:** great." And all the different products and uh jeez, yeah, it's going to work and they can easily spin a demo for anyone and show that, "Oh, yeah, look, it just, you know, increases." I can find a product easily. I can whack this thing

**Dave Jones:** in and show that it works wonders and, you know, people just go, "Wow, this thing is just the most amazing thing ever. It's going to revolutionize the world." And well, not in practice it ain't going to revolutionize much. I'm sorry. And it's

**Dave Jones:** not even a new idea. It's like, yeah, it's actually quite some innovative uh packaging and things like that they've done to get it in this sort of uh form factor and things like that. So, I'm reasonably impressed by the engineering

**Dave Jones:** side of the, you know, the physicality apart from the uh shorting out thing, of course. That's a man. So, yes, whilst this product can actually work and give an improvement, a measurable improvement in some products, some is the key word there. It's not

**Dave Jones:** going to magically work in all products. It's mostly marketing spin preying on people's ignorance of how this sort of stuff works. So, if you're looking to buy this thing thinking that it's going to be magic or if you're heck, you're

**Dave Jones:** looking to invest in something like this, then well, you've got to know all the story and they're not telling you that because well, that's not good marketing, is it? So, there you go. I hope you found that baloney detection

**Dave Jones:** kit useful. That is a bit of a step-by-step procedure on how to look at the claims of a product like this. And the baloney detection kit might change a little bit depending on what the product is and what specific area, but

**Dave Jones:** something like this that's real easy to debunk using just basic, you know, look at the engineering data. So, there you go. If you want to discuss it, if I missed anything, or or you think that I'm wrong and it actually might work

**Dave Jones:** better than I'm making out, then leave it in the comments down below. Catch you next time.
