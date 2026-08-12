---
video_id: DNlA4X5_S30
title: Schematic Component Library Drawing Tip
url: https://www.youtube.com/watch?v=DNlA4X5_S30
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 19, "2": 47, "3": 67, "4": 82, "5": 97, "6": 114, "7": 128, "8": 142, "9": 157}
---

**Dave Jones:** Just one thing with making component symbols like this, because I had to do this, I couldn't find it in the Altium Vault library, they've got everything but the one you want, Murphy's Law of course, but it's trivial to create your own circuit symbol like this, it takes, you know, a minute or two, it's, you know, not hard at all.

**Dave Jones:** But just one thing, when you're laying out the pins, let's have a look at the data sheet here, don't necessarily just follow this pin out in the data sheet, because then it doesn't make for a nice flowing circuit diagram. So you'll notice how on the data sheet here, like, you know, half of the drains are pins 3 to 6 on one side, half are on the other, and if you're trying to draw a nice, neat schematic and, you know, that is just a pain in the butt.

**Dave Jones:** You've got your Nixie tube on one side. Or your display or whatever, you're driving it, so it makes sense to have all of the outputs on one side here. You'll notice that I've gone to the effort to put in the open collector output symbol here to show that they're, well, in this case, they're open drain, but, you know, same thing, you convey the information.

**Dave Jones:** And then here, of course, VCC, you want VCC up here so that you can put your symbol just there. You want your ground down the bottom so you can put that there. Now, the chip enable, usually you're going to... You know, just, you know, for simple applications, you're just going to tie it to ground.

**Dave Jones:** So why put it, you know, somewhere else? Like, you know, pin 7 down here, and if your ground's over there, then you put another ground symbol. If you put it right next to your ground pin, pin 16 here, then you can just tie it like that.

**Dave Jones:** Bingo. Real easy. And then VCC up the top, of course, then you can just put your VCC symbol there. And, of course, your clear pin, often for simple applications. Again, you will just... Have that permanently tied high because it's an active low because I've put the not symbol.

**Dave Jones:** That's what that circuit is. It shows that it's an active low input. So you put it right next to the VCC pin that you're most usually going to tie it to so you don't have to have all your, you know, wires and your schematic running everywhere

**Dave Jones:** and data in, data clock, and then data out. And that just makes a nice compact symbol like this that's going to flow really well because then I can put my Nixie tube right here. I can put my VCC in next to it and all the wires will just pop straight out

**Dave Jones:** and it'll be ground, VCC, they won't get in the way. And then you can have your wires coming in and out for your clock lines and everything else. So it just makes for a nice flowing schematic. So put a little bit of thought into your circuit symbol there

**Dave Jones:** and really you'll make your life much easier and a much more presentable schematic.
