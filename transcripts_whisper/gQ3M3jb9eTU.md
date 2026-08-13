---
video_id: gQ3M3jb9eTU
title: EEVblog #773 - 80W INDUAL LED Light Teardown
url: https://www.youtube.com/watch?v=gQ3M3jb9eTU
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 41, "3": 65, "4": 77, "5": 93, "6": 109, "7": 133, "8": 149, "9": 173, "10": 189, "11": 209, "12": 233, "13": 253, "14": 269, "15": 285, "16": 305, "17": 317, "18": 337, "19": 353, "20": 369, "21": 385, "22": 401, "23": 417, "24": 429, "25": 449, "26": 469, "27": 485, "28": 501, "29": 517, "30": 537, "31": 553, "32": 577, "33": 597, "34": 613, "35": 629, "36": 649, "37": 673, "38": 693, "39": 709, "40": 729, "41": 745, "42": 765, "43": 785, "44": 805, "45": 821, "46": 841, "47": 857, "48": 877, "49": 893, "50": 913, "51": 929, "52": 945, "53": 961, "54": 977, "55": 989, "56": 1005, "57": 1025, "58": 1041, "59": 1057, "60": 1081, "61": 1109, "62": 1129, "63": 1149, "64": 1173, "65": 1193, "66": 1205, "67": 1221, "68": 1245, "69": 1261, "70": 1273, "71": 1293, "72": 1317, "73": 1337, "74": 1357, "75": 1369, "76": 1381, "77": 1397, "78": 1409, "79": 1429, "80": 1449, "81": 1465, "82": 1481, "83": 1493, "84": 1505, "85": 1517, "86": 1537}
---

**Dave Jones:** Welcome to Teardown Tuesday. We've got something interesting today. Check out this beast. It's an 82 watt LED luminaire light, one of these industrial ones, that you, you know, hang from the ceiling in factories and things like that. Thank you very much to Frederick Wang from Light and

**Dave Jones:** Star, they're called, who sent this in. He's the CEO of Light and Star. This is a new product. They are designed and selling and it's a real chunky industrial beast. This is 159 Australian dollars delivered. Yes, it's specifically designed for the Australian market, but it's also designed for the US

**Dave Jones:** and UK markets as well, so it comes permanent with the proper plug with the insulating pins, all fully type approved, all that sort of jazz. And it is an 8150 lumen, 82 watt LED spotlight for either wall or ceiling mounted, but generally ceiling mounted for like factories and

**Dave Jones:** things like that. We, you know, just light the things up. Designed for 14-7 operations, so pretty much 14 hours a day, 7 days a week, very long life, all that sort of stuff. So it's, I think it's actually really quite nice. I thought we'd do a teardown.

**Dave Jones:** I mean, there's not going to be much in it apart from the switch mode constant current power supply and the LED chip on board module which we'll take a look at. But it should still be interesting. Check out that lens in this puppy.

**Dave Jones:** Look at that. Fantastic. Is that? I don't know. I don't know if that's a chip or a little imperfection, but anyway, very, very nice. This whole outer case here is all, this is like the heatsink for it, which is, it doesn't look like that just for kicks.

**Dave Jones:** It needs to actually dissipate all the heat. Thermal design with these things is, you know, the most critical aspect of this. And that's the thing about this. It's designed for 40,000 hours continuous operation, a 10-year lifespan, it's got a 5-year warranty on the thing, and it only gets a

**Dave Jones:** the LED module in here, which we'll take a look at the data sheet for this, only gets a 3% output loss after 5 years. And it's designed to operate really cool, a maximum temperature rise of 20 degrees C, which they claim is like 70%

**Dave Jones:** of your typical LED luminaires out there for like, you know, factory illumination and things like that. So yeah, 10-year lifespan, real, feels like real beefy industrial quality. Really like it. And quite decently priced. 120 US dollars delivered. Or you can actually pay a bit more and get it, I think 30 bucks more or something, and get it

**Dave Jones:** shipped really fast, like in a couple of days. So the LED module used in this, which we'll take a look at, has an efficacy of 99 lumens per watt. You can actually get, that's not like the highest on the market, but you can actually get up to 135 lumens per watt from

**Dave Jones:** this chip-on-board module manufacturer, which we'll take a look at. But yeah, at 82 watts, that's 8,150 lumens rated output. 105 degrees C beam angle on the thing, so it is actually quite a wide beam angle, because you need that when you're lighting from, you know, the ceiling high up.

**Dave Jones:** Designed for heights between 3.5 and 5 meters, so you know, typical like industrial-type factory heights. And this will give at least 300 lumens over the entire illuminated surface minimum from that height. So it really is quite a light. Whoa! Now this model is actually called

**Dave Jones:** the Injul LED module, and they only make the one type at the moment with the one colour temperature. This is 5700K colour temperature with the one angle, 105 degrees. But I'm assuming that, you know, if they've got interest, they'll make ones with different colour temperatures

**Dave Jones:** and ones with different angles and things like that. And oh, that glass lens in there, look at that. Ooh! And it's designed to operate in environments from minus 20 to plus 55 degrees C. As I said, it's got a, it's designed to have a temperature rise of about 20

**Dave Jones:** degrees C in continuous operation, obviously with full you know, like hanging in free air kind of thing. It's not like you can stick this thing in like some ceiling void and you know, expect it to get the same temperature. It comes with a little hook, by the way

**Dave Jones:** like a screw-in eye hook. So designed to either be wall-mounted or hanging from like a guy wire from the ceiling. There's the badge for those playing along at home. Light and star. It's the Injul model, 82 watts nominal input. The CRI is actually quite

**Dave Jones:** low, it's only 70. So as I mentioned in previous LED videos, like you know, indoors, especially if you're doing video and stuff like that, you want 80 plus. But this one is specifically designed for like industrial environments where the CRI doesn't really matter.

**Dave Jones:** And Frederick tells me there's just not much call for any CRI greater than 80. So in terms of the COB LED module manufacturers in China, they mostly like the real high power ones, they mostly churn out a CRI 70. So if you want a higher color rendering

**Dave Jones:** index, it's going to A, cost a lot more and B, availability isn't as good. But they will be releasing a commercial model soon which will use Citizen brand LEDs and that has a color rendering index of greater than 90. So yeah, if you're using these

**Dave Jones:** for like an indoor video studio or something like that, then you'd hold out for something like that. You wouldn't use something with a CRI of 70. So I wouldn't necessarily use this one here in the lab here because I need, you know, color balance

**Dave Jones:** on my videos is quite important. So if you have a low CRI, it just doesn't, it's exactly what it says, color render, it doesn't render accurate colors in the things that you're shooting well enough. So I wouldn't mix these, unless I was desperate, I wouldn't mix these lights in here with

**Dave Jones:** my studio LEDs. But something for like my bunker that has high concrete ceilings, absolutely perfect. Hang it from there, lights up the entire bunker. Brilliant. Thank you very much Frederick. We're going to take a look at this puppy. You know what we say here on the EEVblog, don't turn it

**Dave Jones:** on, take it apart. So what we've got here is a gigantic heat sink right around the LED. That's where all the thermal business is happening. We'll take a look inside, hopefully we'll see the thermal coupling between the COB module and the massive heat sink here.

**Dave Jones:** This is where our power supply is going to be. It uses the top quality Meanwell branded power supply module, so it'll just be in here. So the wiring inside, it doesn't use any custom electronics, I don't believe, I think it just, you know, it mains input.

**Dave Jones:** They've got a decent quality penetrator here, and it looks like it's all sealed right around the edges. I can see like silicon sealant. Actually you probably can't see it on that side, maybe on the other. You can see it's sort of like something, they've got some sort of

**Dave Jones:** seal in there. This is IP66 rated, so you know, it'll handle like the occasional splash and condensation and that sort of jazz. But yeah, it feels like it's really built like a brick dunny, it really does. Very solid construction, really like it. And we'll take a look at that COB module

**Dave Jones:** of course. That feels like a solid glass lens. It's got a seal, looks like a rubber seal around the glass lens in there. Curious to see what these screws do, I might pop those off and maybe this front cap pops off and we might be able to get a

**Dave Jones:** look at the lead module without having to unbolt the rest of it. That'd be nice. And here we go, got the screws out, we should be able to just pop this pop this poppy out. Can I? Yeah, I can just lift the lens off.

**Dave Jones:** Don't want to get my grubby mitts on that. Ta-da! Oh no, our lead! Oh no, I thought our lead module had slipped, but it wasn't, it was just that little aluminium bracket there. Ta-da! There it is! Ah, well we don't have to get

**Dave Jones:** any further, we don't have to extract this thing from the back. We're in like Flynn. There's our COB or chip-on-board lead module. Nice, it's got thermal paste oozing out there from the sides, as you can see. And screwed in, I mean we could take

**Dave Jones:** that off, like I could unscrew that, but there's no point really because, you know, we're not going to see anything, it's going to be an aluminium backing plate on there which then just goes directly down to the unanodized of course, heat sink at the bottom, the rest of it's

**Dave Jones:** anodized of course for your increased heat dissipation. This COB module is manufactured by a Chinese company called Hongli Tronic, and Frederick assures me that they're one of the bigger manufacturers of these COB modules in China. So you know, they're fairly reputable in that respect, and I'll show you, we'll go through the data sheet in a

**Dave Jones:** minute, but it's basically an array of individual lead elements like this. These COB or chip-on-board modules, just like, you know, the chip-on-board that you get on a regular PCB for example, they'll put the bare die on the board and then they bond wire the things across and then blob the whole thing.

**Dave Jones:** Basically doing a similar thing here, instead of your traditional approach of using a PCB and then getting the individually packaged lead modules, soldering them onto the PCB, having your, you know, your thermal vias and everything else take the power out the back, or you have your mount

**Dave Jones:** or you surface mount reflow them on an aluminium-backed PCB for example, getting them manufactured in one big COB module like this is much more efficient. You don't have to assemble the things yourself, the thermal properties are a lot better, there's lots of advantages to this.

**Dave Jones:** That's why a lot of companies are now producing these COB modules. They're just regular lead dies that you get in your individual lead package, you know, they're real high-efficiency individual leads you'd buy, but they actually take the bare die and pack them in there and actually bond them all

**Dave Jones:** in place. And you might be able to see the individual lead elements inside there. There's actually 12 of them in series by, I think, 12. So that entire module there is 46mm by 40mm and the actual lead array itself is 24.3mm squared. Whoa, beautiful.

**Dave Jones:** Now I'm trying to get in there so I can show you the individual lead arrays. So if I can shine a torch on there, there you go. You can see those individual little leads. There's series string of 12, you can actually see the bond wires

**Dave Jones:** going over to each individual lead chip element. Very nice. There you go, there's a closer shot. And you can see the parallel, you can see the metal strip right up the top there where they're all wired in parallel. So you can see the individual

**Dave Jones:** bond wires going down each chip element, and then those series strings of 12 leads are all paralleled on the top side. But yeah, they're just like, you know, regular high-efficiency leads you'd just buy in your single individual lead packaged products normally. In, you know, your

**Dave Jones:** whatever surface mount package you choose. So here's the data sheet for it. This is the model number, I won't read that out for those playing along at home. And yeah, 40x46mm, and you can actually see the array here, it's actually a string of 12, and then

**Dave Jones:** 12 of those strings in parallel like that. And spec-wise, we're talking about a power input 182 watts here. So yeah, well these are absolute maximum ratings. So yeah, you know, this thing is designed for really long-life industrial use, so you really want to, really wouldn't

**Dave Jones:** want to push it that far. So you know, you'd have to look at your degrees C per watt or your thermal performance and all that sort of jazz. Anyway, forward current maximum of 4.8 amps and a maximum junction temperature 115 degrees C. And of course you've got to read the fine print down here, you know, the temperature of the

**Dave Jones:** aluminum PCB is not to exceed 85 degrees C. So that heat sink that we looked at behind here, you would not want that heat sink to get to, well, and the actual aluminum-backed material, there's only a small loss between those two. But you wouldn't want to get that to greater than 85 degrees C.

**Dave Jones:** So that's your goal. So that's why they designed this thing. If you look at the data sheet for it, it's actually got a maximum operating temperature 55 degrees C, and they say it's got a designed temperature rise of 20 degrees C in continuous operation.

**Dave Jones:** So, you know, 75 degrees C, the PCB should be controlled below 75 degrees C. So, you know, they've actually designed this thing properly based on the data sheet. Nice. Bang on. And it looks like the typical operating current, 4.2 amps, and you're looking at a

**Dave Jones:** maximum forward voltage of 37.5 volts, because it's a string of 12 as we saw, so that averages to 3.125 volts per lead chip. Now the one we're looking at here is the 5700 K temperature one, and typically it's going to be putting out

**Dave Jones:** at that, presumably at that 4.2 amps 15,700 lumens. So, yeah, this thing's only rated for 8,100 and something. Once again, designed for, you know, a lower rating because it's designed to, you know, really last. So you're not going to be going the full monty on this

**Dave Jones:** thing. And there's the CRI, it just, as most cases, it just says the CRI like a minimum value, so it's just greater than 70, that's it. And we've got our thermal resistance junction to case here at 4.2 amps, 0.13 degrees C per watt.

**Dave Jones:** So that's reasonably small. So at 80 watts, for example, you'd only be looking at a 10 degrees C rise for the actual lead chip junction as above the case temperature. So that's pretty good. And they do make different color bins, of course, but

**Dave Jones:** Light and Star only, at the moment, only sell a 5700 K one. And of course the characteristics are going to change a little bit depending on the operating point of this thing. And here's the wavelength characteristics here, I won't go into detail, but this is what determines the color

**Dave Jones:** rendering index. So when you get a response of, you know, with little dips, you know, with big, huge dips in here like this, that affects the color rendering index. So the higher the color rendering index then you're going to get less of these dips, and the more broadband

**Dave Jones:** light, your actually even light, that you're actually going to get over the full color spectrum like this. And as with most leads, they're pretty darn linear in terms of forward voltage drop versus current. There we go. Now the thing is, the module itself is

**Dave Jones:** actually 120 degrees C viewing angle, but the light itself is rated for 105 degrees C angle, so that's what our lens is going to be doing here. Woohoo! Look at that. Beautiful. And we've got some little, it's a bit concave-y happening in there.

**Dave Jones:** There we go, I'll give you a good look at that. There we've got some concave, I'm not sure if that shows up on camera, it's a bit weird with all the reflections, but it is concave inside there, and it just is one big arse.

**Dave Jones:** That feels like glass to me. Of course you need glass to handle the heat. You know, there's no way you're going to get like a 10 year lifetime out of some, you know, cheap arse little plastic lens. This is not going to do it.

**Dave Jones:** Proper glass. Look at that. Beautiful. Wonder how much that costs in volume. Hmm. And I've just powered it up, and sure enough let's have a look. Yep, 82 watts. There we go. And the power factor's about 0.95 I think it's pretty good. 0.97, it was claimed at

**Dave Jones:** 0.95, so yeah, it's better than what it claims. Nice. Alright, we'll just do a quick test here. I'll power it up. I've actually only got two of my new LED lights on so this is the regular light here in the lab, but I've fixed the

**Dave Jones:** exposure on the thing, so it does look actually quite dark at the moment, but yeah. Anyway, I've got to fix the exposure otherwise the camera will compensate. So here we go, I'll switch the lights off. And as you can see it's pitch black.

**Dave Jones:** Let me plug this puppy in and see what we get. Hang on if I can find it. Ta-da! There we go! Lit up! Very, very nice. Love it. Okay, so let's take the back off here, and as I said, there's going to be no custom circuitry in here

**Dave Jones:** it's just a Meanwell brand. I know that name is like so shitty. I mean, Meanwell. Oh jeez, it's borderline wung-hung-wo, but no, they're actually a really good quality manufacturer of supplies, and very reputable. And so it's going to have a nice high quality LED driver in here, so it'll just be

**Dave Jones:** the mains wiring straight into that, and then that'll have your constant, you know, your 4 amp output at the nominal, you know, 37 volt compliance voltage, it'll probably go like, you know, up to 40 volts compliance voltage or something like that. We had that, yeah, it's

**Dave Jones:** siliconed down. I've got to wedge that open. Yeah, certainly these things are certainly tight. Yeah, there we go, there's our silicon. Hey, look at that. I should have put an o-ring in there, I mean, you know, that's a bit how you do it.

**Dave Jones:** Oh, really? Is that... Oh, look at that! Wow, that's dodgy. I mean, yeah, it's got a great quality Meanwell power supply in it, but it's just... it's just siliconed down in there. Oh jeez, they need to... oh wow, really? No. God, they need to fix that, come on.

**Dave Jones:** No, that's not good enough at all. Thumbs down to that. And you know what? Here's the other one they sent. Listen to this. Haven't opened this yet. Yep, loosey-goosey in there. Ah, that just does not cut the mustard at all. They need to really

**Dave Jones:** fix that damn thing in place. I mean, look, it's got the proper lugs on the thing to mount the thing down. Gone to all the trouble to custom make this. Just tap some damn holes in here and screw the thing down. Unbelievable, they've gone to...

**Dave Jones:** you know, it's otherwise very, you know, well designed. Like it's quite, you know, they're using a top quality supply and it's all, you know, it's built like a brick dunny and it's all properly thermally rated and everything else but, ah, just let down by that.

**Dave Jones:** Unbelievable. Look, they tried to put some double-sided tape on the bottom here and that's just real crusty stuff. That's not even good quality stuff. Nut. Fail. So here's the Mean World power supply HLG80H42 and yeah, as I said 40, yeah, there we go, just over 40 volts compliant voltage,

**Dave Jones:** 42 volts, and this one's actually 2 amps. So they're actually running this at less than half of what this thing, what the lead module itself is actually capable of. So, you know, but that's what you have to do when you design, you know, high endurance

**Dave Jones:** products like this to last a long time. You can't necessarily run them at that huge current. You could, but you probably need a bigger, better, badder-ass heatsink and all that sort of jazz. Now, I would have loved to have shown you inside this thing, but unfortunately this is the dead giveaway.

**Dave Jones:** Suitable for use in dry, damp, and wet locations. It's not not suitable, it is suitable. What does that mean? Well, it means that it's potted. And here's the current out adjust and the voltage out adjust. And if we take that off, ta-da! Potted block.

**Dave Jones:** There we go. It's that sort of, you know, softy kind of it's, you know, that sort of rubbery, softy kind of potting, silicon potting compound. But yeah, I mean, I'm not going to go and destroy this and dig it out just to show you inside there and anyway to be hideously

**Dave Jones:** ugly. So sorry about that. Can't show you inside this thing. There's the pots right deep down in there and that's it. But anyway, mean world make decent supplies so no problems there at all. And the other thing is, the earth wire here, well, you know, it's heat shrunk, no problems there at all

**Dave Jones:** is actually connected through to the case of this thing. It's not a double-insulated supply. Now we can prove that by poking that on there, okay? That's fine and dandy right, that it's earth. But the fact that then this, the case of this is not solidly earth to the case of this, I'm not sure

**Dave Jones:** if that's even legal in this country. I, if anyone knows ins and outs of the regulations and stuff like that, sorry I don't know off the top of my head. I don't have a copy of the various standards and things like that, but yeah

**Dave Jones:** this thing needs to be properly bolted down to here and I would have liked to have seen the earth go off to the proper lug mounted on here with the shake-proof washers and then a second wire of course going off to the module itself.

**Dave Jones:** So yeah, don't like that at all. And it also doesn't help getting the power out of the power supply. This dissipates a fair amount of power as well. And that's critical to the life of this thing just like the lead module is. And to just stick that in

**Dave Jones:** there with tape and not actually mount it properly to try and get the heat out, blah. Now I've had this thing on for like over an hour now, it's just sitting there, I've got no air conditioning on in here so it's not like any

**Dave Jones:** extra airflow or something. And let's get our FLIR our E8, beautiful little thermal camera, and we're looking at 45 degrees C. Yeah it's like right in the center there. 44. If we look at the bottom case down there, it's not a huge amount

**Dave Jones:** cooler down there, but right down in the core there. As advertised 20 degrees C above the ambient temperature here, which is about 24 or something like that. So yeah, pretty much spot on as advertised. Nice. And if you want to see down in the guts of it, I'm not sure what the glass is going to do there, but

**Dave Jones:** doesn't that look funky? Looks like some alien spaceship or something like that. That's just beautiful. I love it. I should use that as like the screenshot for my video. The thumbnail for my video, what do you think? I'll capture that image. There we go.

**Dave Jones:** So that's all we've got for this puppy. Sorry, couldn't show you inside this nice power supply and there's not much we can do with the LED module. Really we just had a look at the datasheet which I'll link in down below by the way if you want to take a look

**Dave Jones:** at it. And I'll link in their website if you want one of these puppies. I mean, they've got to fix this issue of just flapping around in the breeze in here, that's just crazy. But if they did that, it's just these little small things

**Dave Jones:** like that. You know, otherwise it's quite a nice unit. I like it and I'd probably buy some more for the bunker, but yeah, they've just got to fix that. So we'll see what they have to say about that and I'll let you know.

**Dave Jones:** And if you like the video, please give it a big thumbs up if you want to discuss it. All the links, all that stuff there down below. Catch you next time. Oh, just an update. I heard back from Frederick and he said that

**Dave Jones:** the guy who assembled these, these were specifically samples for me. They didn't know that I'd actually open them up. The proper ones will actually be stuck solid in there. You cannot remove them. They will be solidly stuck. I didn't mention anything about bolting in there, but yeah, apparently this is

**Dave Jones:** not normal. Thanks for watching!
