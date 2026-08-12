---
video_id: bA_hGJVo3DY
title: EEVblog #191 - Mouse Trap Triggering
url: https://www.youtube.com/watch?v=bA_hGJVo3DY
source: youtube-asr
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, it's a rather unusual one today. I've had a couple of people, not just one, but actually two people ask me a

**Dave Jones:** very similar thing. Uh, how can you what's the simplest method or what's a real easy method to electronically trigger some sort of spring-loaded mechanism? And they both gave an example of something like a mouse trap, even though that's

**Dave Jones:** what they weren't trying to do. They were trying to do something else, but you know, a basic spring-loaded mechanism like that. What's the easiest way to electronically trigger it? And of course, one of the first things you'd think of for triggering something like

**Dave Jones:** that is some sort of solenoid-based system, you know, you apply a voltage to a coil and it pulls a plate back or something like that. I don't know. Bit too complicated. Thought got to be able to do it with Ohm's law,

**Dave Jones:** surely. And sure enough, I reckon you can. Simple. A resistor is all you need. A resistor and a voltage source. Here's your This is how I would do it. I would This is your thing that you want to hold back

**Dave Jones:** with your spring mechanism. You just have some cord, fishing line, nylon string, cotton, polyester, whatever. I don't wrap it around the resistor, tie it off, so it holds it back. And then, when you want to trigger the thing,

**Dave Jones:** pass some current through the resistor, heats it up, and it weakens the string or whatever it is and until it breaks, and then bing, gone. Simple. I'm going to try it. Looks like fun. And here we go. I've got my mouse trap or it's

**Dave Jones:** actually a much larger rat trap. It's the eradicator. I love it. Awesome sounding name. Um, tied back the arming plate here because we're not going to hold down the arm here with the traditional arming plate. We're going to

**Dave Jones:** hold it back with this uh I've actually tied some fishing line on there and I'll show you that in a sec. Um, and I've just tied it back so this is actually armed at the moment. It's just tied back

**Dave Jones:** so it doesn't accidentally go off in my hands which would be rather nasty. Now, I've got this fishing line it's tied off down here. It's probably hard to hard to see but this fishing line I've I've wrapped one turn around the arm here and

**Dave Jones:** I've tied it off around the bottom. Uh, on on sorry on the other side but on the bottom here I've got a 10 ohm resistor and I've wrapped a one turn of the fishing line around the 10 ohm

**Dave Jones:** resistor. So when that heats up it should eventually get to a point where it weakens where the fishing line weakens enough and it will break and bingo it'll lift the arm up and boom it'll activate the trap. So, let's give it a

**Dave Jones:** go. A 10 ohm resistor isn't too bad it means it should trigger on the order of volts. We don't have to put much power through this at all. It's standard quarter watt resistor. So we should only have to put like a watt or something or

**Dave Jones:** maybe even two at most. Take the tape off here and arm this sucker. Fishing line should have more than enough strength to hold back that trap there cuz there's because we have a big lever arm here so there's

**Dave Jones:** quite a large leverage there and that should hold there nicely. And bingo it's ready to go and let me get my blast shield just in case. I don't want to damage my new camera here. I don't want the thing

**Dave Jones:** flicking towards the camera and I'll set up the high speed camera on on side and we'll see if we can capture this. And I'm 100% sure this will work. I'm going to switch my load voltage on. I've got it to zero, and I will wind up

**Dave Jones:** the wick. And let's see if we can uh make this sucker do anything. Here we go.

**Dave Jones:** Woo! Awesome. And that sucker's smoking, too. I love it. And there's the melted fishing line around our resistor. I turned that up fairly quickly because of my high-speed camera. I've got to trigger this thing within 10 seconds. That's all it captures. So,

**Dave Jones:** but you could actually do that at a lower current. It'd just take more time to actually generate the heat in the resistor, and and melt the in in this case fishing line, but you can go and try other things, you know, nylon,

**Dave Jones:** polyester, all sorts of all sorts of stuff, if you want. I think they might have higher melting points than something like fishing line. I'm not sure, but great fun. Go and experiment with it. And really, I don't think you can get a simpler trigger

**Dave Jones:** mechanism than Ohm's law. And that, of course, brings us to the humble quarter-watt resistor. Let's take a look at it and see what happens when you pass uh close to the maximum rated power through one of these resistors.

**Dave Jones:** Now, we've got a data sheet here of a uh typical axial quarter watt resistor. And the figure we're interested in down here is what's called the thermal the thermal resistance RTH here. And as you can see, it's 140 K per watt or Kelvins per watt

**Dave Jones:** or basically degrees Celsius per watt. So, if you put 1 W into the or if this if this if this resistor dissipates 1 W, then its temperature is going to rise by 140° K or 140° C above the current ambient temperature.

**Dave Jones:** And the power rating of a resistor is something that beginners forget a lot about. Now, here's two graphs which uh show us um basically the rise in temperature here at rise in temperature degrees Kelvin versus the power dissipated in watts.

**Dave Jones:** And it exactly matches that thermal resistance we saw that figure we saw before. Look, if you put 1 quarter watt if if you dissipate a quarter watt in that resistor, it will rise by 35° K or 35° C

**Dave Jones:** uh for a quarter watt. And that means And if you multiply that by four for 1 W, as this thing wouldn't handle a watt, but if it did, then uh uh you would get that 140° C per watt. Now, a lot of people a lot

**Dave Jones:** of beginners think, "Oh, this quarter watt this quarter watt resistor can handle a quarter watts." Yeah, it can. It's designed to do that continuously, but it will rise by 35° C above your ambient temperature. And that's the key thing.

**Dave Jones:** It doesn't get to 35°. It gets to 35° plus your current So, if your lab's at 20° C, that's already 50 that component, that resistor, it's going to get to 55°C. And if your lab's you know, if you're

**Dave Jones:** using the product outside in summer time and it's 30°C, then you're going to be that resistor is going to be at 65°C. And so on. And you can get higher temperature resistors, which can actually uh you can get uh

**Dave Jones:** the Not all quarter watt resistors are the same size. They can actually be physically different uh sizes. And yeah, they all handle a quarter watts, but they might the smaller ones might get Well, will get physically hotter with

**Dave Jones:** that quarter watt. They won't be the same as this particular one. So, I just something to watch out for when you're designing your boards. Don't If you are going to go to limit and dissipate a quarter watt in a quarter watt resistor,

**Dave Jones:** just make sure that your board can handle that your product can handle that temperature. Make sure there's adequate air flow and things like that. If you put this resistor, if you mount it on the board right next to an electrolytic

**Dave Jones:** capacitor, then well, that the temperature of the nearby electrolytic capacitor is going to rise, which may derate its life and things like that. I've explained that before on various episodes of the blog. Now, if you're curious about this graph on the

**Dave Jones:** right-hand side here, it's very similar to the one on the left. Now, the one on left we just looked at is what's called the hotspot temperature. And that's basically the temperature in the core of the resistor itself. Or you can take it

**Dave Jones:** essentially um as the temperature of the case of the actual resistor itself. But this one over here um is uh a temperature It's exactly the same Y axis, temperature rise versus X axis, power dissipated, but it's the temperature rise at the end of the lead

**Dave Jones:** when it's soldered into a board like this. When you've actually put it on there, you bend the leads, and you've got a X amount of lead length, and you trim them off, and they're soldered onto the individual pads. Okay? Now, this is

**Dave Jones:** let's say you leave 5 mm lead length at each end of the resistor. This here, Y axis, will be the temperature on the actual pad itself. Uh and that's the key because you can actually use your PCB as

**Dave Jones:** as a heat sink itself. If you actually put it close enough to the leads, then the PCB can help dissipate the heat from the core of the resistor itself. But, there are limits actually to that because the leads themselves have a

**Dave Jones:** certain thermal resistance, and it becomes a thermal resistance series equation and stuff like that. I've done a previous uh blog on that for um heat sinks and things like that. But, yeah, you can use your PCB as a heat sink to

**Dave Jones:** help dissipate the heat in your product. So, that's something to think of. If you are a design um a product which will uh which will dissipate close to the maximum power in that resistor itself. And as you can

**Dave Jones:** see, this is no longer a linear graph like this. It It actually tapers off like that depending on the lead length which you actually have. Now, the uh the greater the lead the smaller the lead length, the more linear the line becomes

**Dave Jones:** and because of the thermal resistance in that actual lead itself. So, if you have uh uh a longer lead length of 15 mm, as you can see, the temperature will drop off. And And if you bent it right out here

**Dave Jones:** and had like 25 mm or 30 mm of lead length and bent it right there, you know, really extreme kind of stuff, it'd taper off something like that and you would actually get very little heat at the end cuz all the heat would be in the

**Dave Jones:** core plus a little bit dissipated um along the leads itself. So, if you're going to do that, try and trim them closer to the board so that you can actually get you don't lose as much heat in the legs and you can uh take the

**Dave Jones:** uh heat out of the core of the resistor itself. And this brings us on to a what's called a derating curve. Every resistor datasheet will have one of these. Not all Only few of them will actually have the actual um thermal

**Dave Jones:** resistance graph like this, but they'll have what's called a derating curve and basically it shows its uh maximum power dissipated or 100% of its nominal rated value. Now, basic resistors like this are almost always spec'd at a wattage,

**Dave Jones:** in this case a quarter watt resistor, is specified at a temperature, maximum temperature of 70°C, and that's why it's shown on the graph here with this dotted line going up at 70° uh C on the X axis here and that's

**Dave Jones:** actually ambient. That's ambient temperature, not the temperature rise as in the resistor as we've actually looked at. So, if you if you're designing your product to work over a temperature range, say up to 70°C, then the resistor can actually dissipate

**Dave Jones:** um two and a half its nominal two and a half watts and continue to function function correctly and that's fine because the temperature rise plus the ambient temperature um will still be within the working limits of the resistor itself. But, after 70°C, it

**Dave Jones:** derates linearly like this until it gets to a point, in this case for this particular resistor, even though it isn't this one, but this data sheet for this resistor is 155 degrees. So, that will be the maximum absolute maximum

**Dave Jones:** temperature that you can use a resistor at because and then you won't be able to dissipate any power in it because you can't go beyond that temperature. It just won't work anymore or it won't be reliable or something like that. What

**Dave Jones:** does all this have to do with our mouse trap? Well, not much at all really, but I just wanted to show some things on resistors.
