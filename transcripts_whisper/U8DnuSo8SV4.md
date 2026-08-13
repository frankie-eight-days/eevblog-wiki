---
video_id: U8DnuSo8SV4
title: EEVblog #962 - Hacking A Calculator Into A Counter
url: https://www.youtube.com/watch?v=U8DnuSo8SV4
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 13, "2": 25, "3": 41, "4": 61, "5": 81, "6": 97, "7": 113, "8": 133, "9": 149, "10": 165, "11": 181, "12": 193, "13": 209, "14": 221, "15": 237, "16": 249, "17": 265, "18": 277, "19": 293, "20": 309, "21": 321, "22": 337, "23": 353, "24": 373, "25": 385}
---

**Dave Jones:** Hi. Let's say you've got a little toy train set up like this, and you want to actually count the number of laps that go around like this. Now, I've actually stuck a little magnet on the side of there, and I've got one of these

**Dave Jones:** magnetic read switches here that you can, that you use for your home burglar alarms or whatever, any type of magnetic read switch so when it goes past, it closes the contacts in there, shorts it out, it's just a switch, and you need to count how many laps.

**Dave Jones:** How do you do it? Well, you can do it the complex way which I've shown in my previous video, using a universal counter and all that sort of jazz to do that. But I thought it'd be much more interesting to hack a calculator to do it.

**Dave Jones:** Now, let's take a look at this Casio SL300NC, but it should work with any calculator. If you just go 1 plus like this, and then press plus again, it'll be in the constant mode, and then you just press equals like that every time, and bingo, you've got yourself a counter.

**Dave Jones:** So all we've got to do, in theory, is hook the output of our switch here across the equals key inside here, and bingo, we should have ourselves a nice little train lap counter. Let's give it a go. Quick teardown inside this, this is a dual solar and battery powered system

**Dave Jones:** hence the little diodes in here. They didn't bother with surface mount, they just used a through hole and soldered them directly onto the board, that's really interesting. Another interesting thing to note in here is this lead here. They've got, why they've got a lead in there, I think what they're doing there

**Dave Jones:** is actually clamping the output, using it as a 1.8 volt or whatever diode clamp to clamp the output voltage from the solar cell here, so that's interesting. But there's nothing else in here, we've just got the main IC chip on board, it's just been blobbed, and somewhat annoyingly

**Dave Jones:** and not really ideal for the purpose. This model has the carbon-covered copper pads here, so these are vias here, and individual little test points there, very nice all the way around there, but yeah, they're covered in carbon, so you have to scrape those off to be able to solder

**Dave Jones:** to these pads and vias. And this one's a little bit annoying, doesn't have screws holding it down, it's got these PCB heat stakes here, you can actually just get a knife in there and shear those off, but yeah, this is not the best calculator for this job.

**Dave Jones:** Now with this, what you're better off doing, instead of like removing the key like that, you're better off just finding which tracks actually connect under there, because these are carbon, so you know to try and solder onto those, that's the equals key there, try and solder onto that

**Dave Jones:** have the wires coming out front, not the best option. Probably better to, and of course you can still keep the equals key intact, if you can find the two appropriate matrix traces that come out and access them on the bottom side and then

**Dave Jones:** scrape off some of the carbon on there and then solder wires directly onto the pads if you can. So in this particular case, that's our equals key, there we go. That goes down to a via down there, and that one goes down to a via.

**Dave Jones:** So those two vias, we can access those on the other side. Thank you very much. Now fortunately we've got two pads here connected to the two vias that we want. Isn't that convenient? These are all test pads so that they can test this with a bed of

**Dave Jones:** nails tester. So we can just scrape the carbon off those pads, just get in there with a knife, be very careful and you can expose, check it out, you can expose the copper under there and we should be able to solder to that pad very nicely.

**Dave Jones:** But the problem with soldering to pads instead of putting wires down vias is that it's not very robust. So you definitely want to use low mass wires soldered onto those so that when they flap around in the breeze the weight doesn't peel off the pad.

**Dave Jones:** You want to use a very low temperature on your iron, as low a temperature as you can get away with so you don't lift the pads and also you want to anchor down the wires later. So I'll just do that scrape them off and solder it on.

**Dave Jones:** Bob's your uncle. So there we go, I've modified that, just tacked on a couple of mod wires here. I've got it going off to a connector here, because as I said, if you've got a lot of strain on these wires I mean you can just take them directly off to whatever switch

**Dave Jones:** you've actually got. But don't forget to tape them down, otherwise there'll be stress on these solder joints and they will just fall off the first time that you handle them. Just peel the trace off, the pad off the fiberglass and yeah, really ruin your day.

**Dave Jones:** So better to have some sort of connector interface. I've just got a .1 inch header here, you could use like a screw terminal or something like that. You could do a bit nicer than that if you want. But anyway, that'll allow us to reuse

**Dave Jones:** this as a sort of like a universal counter. I mean we could even sort of hack out the case and put the case back on and stuff like that, and we can just insert our switch on the side. Beauty. And by the way, in this case with the carbon covering

**Dave Jones:** the vias, that's going to be down the via holes as well. So I wouldn't go sticking your wires down there and soldering them into the vias. I would have scraped off if we didn't have those pads there, I would have just gently scraped off the top of the vias, being

**Dave Jones:** careful not to nick the wire in there, and just lay the wire flat on top. Alright, let's give this a bow. I've got it hooked up with our connector on the side. Very nice, look at that. So we'll just go one, plus plus, and of course you might have to subtract

**Dave Jones:** one from the final result, but hey, no big deal. Oh, that's a real bobby dazzler. Fantastic. So I hope you liked that, how to hack a calculator into a simple counter. And yes, it is just a switch input to this thing, so you can't use like a digital input or anything like that.

**Dave Jones:** It has to be just an open contact switch. And if you had some sort of other input that you wanted to drive, a noisy input you might want to clean up first, then you can just do the output using you can short it out using a transistor or a relay

**Dave Jones:** or some, any sort of other system that gives you sort of like, more or less a contact type output. Because remember, this is a matrix keypad. It's not like just individual keys with pull-up resistors or anything like that. They're not digital inputs. So there you go.

**Dave Jones:** Hope you enjoyed that. If you did, please give it a big thumbs up, because that really helps a lot these days. Catch you next time!
