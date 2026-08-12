---
video_id: 6GIscUsnlM0
title: EEVblog #568 - Solderless Breadboard Capacitance
url: https://www.youtube.com/watch?v=6GIscUsnlM0
source: youtube-asr
timestamps: {"0": 1, "1": 31, "2": 61, "3": 89, "4": 110, "5": 131, "6": 147, "7": 177, "8": 216, "9": 245, "10": 261, "11": 291, "12": 308, "13": 337, "14": 362, "15": 379, "16": 393, "17": 425, "18": 461, "19": 481, "20": 513, "21": 529, "22": 559, "23": 585, "24": 618, "25": 652, "26": 685, "27": 700, "28": 730}
---

**Dave Jones:** Hi, the humble breadboard. Yes, you've no doubt got one in your kit and you've no doubt used it before. It is one of the most popular tools for quick circuit prototyping and well, for good reason because you can just plug components in, there's no soldering, you can move things around and you can generally have a play with stuff just to see if something's going to work before you dedicate it to a PCB. And it's good for experimentation, but it has a couple of limitations. The first one of course is

**Dave Jones:** that it's not permanent. You know, things can you can get dicky contacts and all sorts of stuff like that, which we won't go into. But the second is that the breadboard, as you should know, if you don't, well, you will now, that it's not designed for high frequency stuff because, you know, we've got wires hanging all over the place, it's not good, they're all acting as antennas, big loops of things, which isn't good for switching stuff. For example, you wouldn't want to build a switch mode

**Dave Jones:** power supply on here for example, it's not going to work that well. And you'll see in as you saw in a previous video where I was playing around with this precision constant current circuit. Yeah, it's not that great on the breadboard because of all the inter-contact capacitance on here. It's you know, it's not very good at all. But hey, if you can get something working on the breadboard, then that gives you good confidence that it's going to work on a proper PCB when you actually lay the

**Dave Jones:** thing out properly, you do nice tight ground loops and power loops and keep everything nice and short and tidy and stuff like that and you don't have all that stray capacitance between the contacts. Now, you know, the rule of thumb in the industry is that sort of you don't do anything more than like a megahertz on the breadboard.

**Dave Jones:** And the inter-contact capacitance, well, I've always taken as normally are about 10 puff, you know, 10 pF, something like that of that order, but what exactly is it? Now, I've looked at a few data sheets for these things and well, I haven't been able to find an inter-contact capacitance value on here.

**Dave Jones:** And well, some figures that are floating around out there, um not actually in the data sheets, are anywhere from 2 to 25 pF per contact strip. And well, I don't know. What is it? I mean, that's an order of magnitude different difference.

**Dave Jones:** Is it 2 pF or is it 20 pF? But what is it? Well, I decided, let's actually measure it. So, I've got some breadboards here, a few different uh types, and I've got our LCR meter. So, there's nothing better than actually getting real empirical data on this thing cuz I I did a quick Google. I couldn't really find anything out there of anyone who's actually done any real measurements on this thing, just this wide you know, wide-open ballpark figure of 2 to 25 pF. So, I've got my Agilent

**Dave Jones:** U1733C LCR meter here and well, you know, down at 120 hertz, it's only got uh 0.1 pF resolution there, but if we go up in frequency, which is what we're going to have to do on this breadboard because the capacitance will change with frequency, of course. It's not going to be fixed, but this puppy, if we go up in frequency, 1 kilohertz, bingo, we get an extra digit. We're down to uh 10 uh femtofarads there. Awesome. And there we go. 10 kilohertz, we're now at Look at this. 1 femtofarad resolution.

**Dave Jones:** Awesome. But we This one actually goes up to 100 kilohertz as well. And well, but we don't get an extra digit on there, but that's fantastic. So, we'll be able to prove that after we uh null out the residual reading of uh the meter and the leads here. We can null that out. we'll be able to fairly accurately, or you know, good enough, measure the capacitance of these various different breadboards we've got here. Now, if you've never seen inside a breadboard like this, well, you should. You should

**Dave Jones:** take the back off and have a look at the actual strips. They go in columns down here like this, and if you flip it over, you can see the metal contacts down in there like that, and those little spring bar contacts. And because they're long like that, they're well, what are they?

**Dave Jones:** They're like the plates of a capacitor. Between any two wires or any two contacts, you're always going to get some capacitance. And there's the dielectric material as well. Usually these things are like phosphor bronze contacts, but some of them can be silver plated as well on your higher quality breadboards. And well, you know, and the back end also will have an effect on that capacitance well. This is just got a spongy back end on it. Some I think this one down in here, I haven't taken

**Dave Jones:** it out for a while, but I don't think there's any backing on at all. It's just a hard plastic backing. There's no sponge on the bottom of that one. So, first up, we'll have a look at my main breadboard. I've got a few of these. K&H brand. It's a decent brand name model RH32.

**Dave Jones:** Standard tie point configuration. And we'll just measure the vertical between two vertical columns down there just in a random location. Shouldn't really matter. All right, so we're at 100 kHz here to give us the greatest resolution and to operate at the highest frequency possible. And I haven't actually plugged them in yet. I've just got them sort of resting on there. So, because when you sort of, you know, touch these leads, it's going to, especially at this sort of resolution, it's going to change around a bit. Like if I put my fingers

**Dave Jones:** on there, of course, it's going to go up because of the capacitance of my fingers. But, we should be able to null that out. So, I've got 4.627 pF, and that's reasonably repeatable if I, you know, dick around with that. Hey, you know, jeez, you fart halfway across the room and this thing's going to change at the moment when we're down at one femtofarad. But anyway, all right, so let's null that out and see what we get.

**Dave Jones:** That's not too bad You know, that's not too bad. I mean, we can dick around there, but we won't bother. So, let's stick that in the breadboard. Look at that. Two side-by-side contacts is only 2.4 picofarads. Look at that.

**Dave Jones:** So much for 20 or 10. And just to double-check that, let's just remove that again and check the repeatability. Yeah, you know, it's a little bit It's, you know, I don't have these leads exactly right, but that's going to be near enough.

**Dave Jones:** We're in the order of two picofarads. And if we measure elsewhere on the board, there we go, 2 and 1/2. Right over on the edge over here, 2 and 1/2. So, it looks like it's pretty done repeatable. And let's go for one of these power strips down here. I've actually got them connected like this so that Usually, they're split in the middle like that. So, only those along there are connected and those along there. And it actually shows you that visually on there. Just for kicks, let's

**Dave Jones:** have a look at the uh power bus. Sometimes, it can be a real pain plugging these square pins in. But there you go, we're over. Look at that. Can't handle it. So, we're well over our Let's put that back on our auto range. There you go, 20.25 picofarads or thereabouts for the power bus. So, maybe that's what they're talking about when they talk about that range from 2 to 25 picofarads. But really, all you can You don't really care about the power strips down here usually because you're using them for

**Dave Jones:** power. So, it's not a huge issue, but uh yeah, really the one you got to care about is the inter-contact capacitance down there. No, hang on. I haven't nulled that out. So, because I changed ranges, it didn't keep the null. So, let's null that out, and we should find it's around about There we go. 21 odd picofarads for the power bus.

**Dave Jones:** And if you're curious to know what they are directly opposite over the inner divider in there, well, it's almost unmeasurable, really. I mean, we're down in the noise of our null, really. It's, you know, it's just not, as you'd expect, because they're not physically close together, and because there's a big chunk of dielectric taken out. So, let's null that out. So, I've done this a few times, and I have sort of got a repeatable result around Let's take it as about uh 0.5 picofarads there uh

**Dave Jones:** across the dividing strip on this particular breadboard. And the other thing I want to check is does it change if I plug in a fairly large uh leaded component in there, like that? Does it force it open? Yeah.

**Dave Jones:** No, at 2.7. There we go. Don't touch it. But, of course, as you know, hanging in the air, it's going to disturb it a little bit, but generally, no. Forcing those pins in, you'd expect it because technically, they're a bit closer, so you'd expect it to increase in capacitance. And that's kind of sort of what you see, but it's not really a big deal. Now, this little uh yellow breadboard, just a One Hung Low brand, I have no idea what it is.

**Dave Jones:** And uh but I don't expect any different. And no, it's practically the same. And that's what you expect to get, because it's based on the physical dimensions. And all these breadboards' physical dimensions are basically the same, and the dielectric constant of the material in there probably isn't going to change a huge amount anyway. I wouldn't expect an order of magnitude difference. So, there you go. It is a roundabout that same figure of two puff two pico farads.

**Dave Jones:** And that one across the dividing strip in the middle, even lower than the other one really. It's quite down in the noise. And this one across the dividing strip in the middle, even lower than the K&H one, you know, point two puff. And we've got another generic brand breadboard here, no idea what brand it is. Once again, two puff. And the power strip on this one, once again, 20 that same figure of roundabout 20 puff. And one thing I forgot on the other one, curious to know between the power strip

**Dave Jones:** and one of the columns in there, we're talking, you know, just over one puff. And this PIC development board from Gtronics.net, I don't know the brand of the actual breadboard in here. Don't know where he sources it from, but there you go. Once again, that two puff figure. You can take that to the bank. One thing I haven't done yet, what is the capacitance between two contacts that are separated by one unused column. And of course, you'd expect it to have. And yep, it does. And yep, it's

**Dave Jones:** the same on that one and on that one as well. So, there you go. And if you're curious to know the capacitance at different frequencies, well, at 100 hertz down here, you know, a half a puff, you know, it's barely even measurable, down in the noise. And at 1 kilohertz there, we're looking at just over two puff. And at 10 kilohertz, as you'd expect, it increases slightly again, 2.25. So, there you go. I think that's fairly definitive. I mean, I've tested four different types of breadboards and they're all identical.

**Dave Jones:** Two pico farads capacitance between the individual contacts. And, you know, pretty negligible when you jump over well, go from the power strip to one of the columns or when you jump across the columns like that. But, there you go.

**Dave Jones:** You can take that figure to the bank and you can plug that into your simulations or something to see why your breadboard is oscillating. Nothing can beat empirical measured data like that. I like it. You know, measure your own breadboard and see what you get. But, I reckon you'd be hard-pressed unless the dielectric material was grossly different to all of the four different ones here, then you should get that same figure because the capacitance is based on the physical dimensions. And all these breadboards, as I said, they're going to

**Dave Jones:** be pretty identical in that respect. So, remember that figure, two puff per contact and you'll be right. No worries. So, I hope you enjoyed that quick little empirical video to actually measure this. And if you want to discuss it, jump on over to the EEVblog forum. Catch you next time.
