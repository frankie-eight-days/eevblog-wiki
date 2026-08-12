---
video_id: tnrazDCiTTc
title: EEVblog 1696 - TUTORIAL: Wind Power Efficiency 101
url: https://www.youtube.com/watch?v=tnrazDCiTTc
source: youtube-asr
---

**Dave Jones:** So, please excuse the crudity of the model. Didn't have time to build it to scale or to paint it, but we've got a typical three-bladed wind turbine here. It doesn't matter how many blades, and we're going to calculate the energy or

**Dave Jones:** the power in the wind that can go through a particular diameter wind turbine. So, in this particular case, I've drawn like a volume a circular volume of air here. So, we've got the area, and D is the distance the

**Dave Jones:** basically the thickness of the air there, and then assuming that passes through the wind turbine. Now, we have to go back, as I said, to first principles here, kinetic energy. You almost certainly learned this formula in like a first-year basic science in like

**Dave Jones:** high school science. You'd learn this, wouldn't you? Kinetic energy equals 1/2 mv² or 1/2 * the mass * the velocity squared. Basic physics. So, we actually could jump directly from this kinetic energy formula to this industry standard formula here that's used in all of the

**Dave Jones:** wind power energy industry. It's it's the formula that explains it all, but I thought we'd just derive this very quickly. So, you can skip this bit if you don't care about transforming that into where this actual formula comes from. So, anyway,

**Dave Jones:** let's go. The volume of air inside here is the area square area * the depth here, and the air density is rho. That's not a P. That's actually a symbol rho is the mass / the volume here. I've got a

**Dave Jones:** volume is just VL there to differentiate it from velocity, which is V. So, we can just rearrange that mass equals rho * the volume. Now, we can take our kinetic energy formula up here, and instead of having the mass, we can substitute in

**Dave Jones:** rho * the volume * V squared. So, it's the same formula. We've just substituted in some equivalent stuff. Now, of course, the volume of this is the area times the depth. So, we can just change that from volume to area times the

**Dave Jones:** depth. Easy. And the depth here, this can be replaced by velocity times time. So, we're just substituting in just to get this to pop out the other end. Now, because we've got two velocity components in this formula, V squared

**Dave Jones:** becomes V cubed. And here's the last step. Power, because we want power, not kinetic energy. Power is kinetic energy divided by time. So, if we divide this part here by time, the T's cancel out and bingo, you're left with power equals

**Dave Jones:** half times rho, which is the air density, times the area, times velocity cubed. Bingo. That is our industry standard wind formula that applies to all wind turbines and actually applies to liquids as well. But anyway, because density is just air or a liquid or

**Dave Jones:** whatever it is, whether or not you have a like a water turbine, for example, you're going to be using the same formula. But this applies to windmill. This is the industry standard formula. This is how much power is available in a

**Dave Jones:** given volume of air to feed in to your turbine. You can't get any more than that. Now, we have to take a look at this rho figure, which is the air density, and this changes with temperature. And you can go look this up

**Dave Jones:** in various charts at a standard 20° C, it is actually 1.2041 kg per cubic meter. So, if we actually put this into the formula, and let's take a standard 10 m per second wind speed, which is about 20 little over 20

**Dave Jones:** mph, that's pretty much where the peak of most wind turbines will be designed. Pretty much a standard calculation figure in the industry. So, 10 m per second. Power equals 1/2 * 1.2041 * let's put per square meter, so 1

**Dave Jones:** square meter, * the velocity 10 m per second cubed here, and that gives us 602 W maximum ideal. This is the maximum ideal power that you can actually have in a 10 m per second wind at 20° C at that air

**Dave Jones:** density. So, anytime you see any marketing claim whatsoever for any sort of wind turbine that can get greater than 602 W per square meter area, you know they're full of crap because that would require over unity, i.e. getting more power out

**Dave Jones:** than what you put in from the wind. In this case, you're not putting it in, the wind's already there. You're just extracting from the wind. There's no way you can possibly get more than 602 W per square meter at that particular air

**Dave Jones:** density. Now, as it turns out, even the most ideal wind turbine can't achieve this figure. Why? Well, not only because like there's the like the turbine hubs in the way and things like that and the blades don't capture, you know, uh

**Dave Jones:** precisely 100% of the wind. They act as airfoils and that increases the effective capture area. That's why a lot of you know, your commercial huge commercial ones are this three-bladed design. Like this is kind of like an optimized design for this type of wind

**Dave Jones:** speed and capture area and efficiency and and things like that. Now, there's this thing called Betz's law. So, there was this smart dude called Albert Betz early last century who came up with Betz's law. He wasn't the I think

**Dave Jones:** somebody else came up with at the same time, but anyway, it's called Betz's law. It states that you can't extract more than 59.3% of the kinetic energy going into a wind turbine or a fluid turbine. That is because when it actually flows into it

**Dave Jones:** like this, it actually spreads out. It can't capture it all and that there's a you know analyzed all this and figured out that that is the absolute maximum figure that you can extract from it. So anyone claiming to extract more than

**Dave Jones:** 59.3% of this 602 watts per square meter at 20° at that air density is violating Betz's law. And I believe nobody's actually done it yet. There's a few people who claim that you can actually do it if you also harness

**Dave Jones:** thermal type stuff with it and other things. And this applies by the way Betz's law applies to open frame wind turbines like this, ones that don't have the frame around them. And all the designs that have actually tried this to

**Dave Jones:** actually put like in in case them in in tunnels and things like that to try and get around Betz's law, they've all sort of come a gutser in practice. It's great in theory and apparently you can actually do some simulations to prove

**Dave Jones:** you can get better, but when you try and do it in practice, Betz's law wins every time. So applying Betz's law to our maximum ideal figure here times 59.3% gives us 357 watts per square meter. And this is

**Dave Jones:** actually called the power density, which again is an industry standard figure that you'll find in the data sheet for wind turbines. And here's one of the data sheets for a huge 100 kilowatt or I think 200 kilowatt wind turbine, which

**Dave Jones:** shows it's just over 300 watts per square meter. And that's you know that typically the best you'll get is like 80 to 85% or because as I said, you know, you've got the hub in there and you've got other sort of you know losses to do

**Dave Jones:** with the blade design and things like that, but you know, a good wind turbine is around about 80% of Betz's law, not the actual maximum power.
