---
video_id: WvaGXF-prz8
title: EEVblog #1034 - Mailbag
url: https://www.youtube.com/watch?v=WvaGXF-prz8
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 14, "2": 39, "3": 54, "4": 75, "5": 93, "6": 114, "7": 129, "8": 147, "9": 159, "10": 177, "11": 198, "12": 213, "13": 228, "14": 243, "15": 258, "16": 273, "17": 294, "18": 309, "19": 327, "20": 345, "21": 360, "22": 375, "23": 390, "24": 405, "25": 423, "26": 438, "27": 453, "28": 471, "29": 489, "30": 504, "31": 522, "32": 537, "33": 555, "34": 570, "35": 588, "36": 606, "37": 621, "38": 636, "39": 654, "40": 672, "41": 690, "42": 702, "43": 717, "44": 732, "45": 750, "46": 765, "47": 783, "48": 801, "49": 819, "50": 834, "51": 849, "52": 861, "53": 879, "54": 894, "55": 912, "56": 945, "57": 969, "58": 996, "59": 1020, "60": 1041, "61": 1068, "62": 1086, "63": 1113, "64": 1140, "65": 1152, "66": 1164, "67": 1182, "68": 1200, "69": 1209, "70": 1227, "71": 1245, "72": 1272, "73": 1290, "74": 1311, "75": 1329, "76": 1354, "77": 1382, "78": 1403, "79": 1421, "80": 1442, "81": 1463, "82": 1484, "83": 1499, "84": 1520, "85": 1547, "86": 1571, "87": 1592, "88": 1625, "89": 1640, "90": 1661, "91": 1682, "92": 1697, "93": 1715, "94": 1736, "95": 1760, "96": 1778, "97": 1796, "98": 1814, "99": 1835, "100": 1871, "101": 1889, "102": 1907, "103": 1922, "104": 1940, "105": 1955, "106": 1976, "107": 1994, "108": 2012, "109": 2030, "110": 2051, "111": 2063, "112": 2078, "113": 2096, "114": 2120, "115": 2144, "116": 2168, "117": 2190, "118": 2205, "119": 2226, "120": 2244, "121": 2259, "122": 2274, "123": 2292, "124": 2313, "125": 2331, "126": 2349, "127": 2373, "128": 2394, "129": 2427, "130": 2451, "131": 2472, "132": 2487}
---

**Dave Jones:** Hi, welcome to everyone's favorite segment, mailbag. Yes, we haven't done one in a while, so let's get to it. This one is from NoStarchPress. They've had several sucks of a salve here on the EEVblog. I don't need this, because it's got a pull tab.

**Dave Jones:** Um, yes, so we know what's in here from NoStarchPress. Now I've got to use this. There we go. Alright, oh, it's thick. Yes, this is the TVEC envelope stuff. Really tough stuff. Anyway, the Arduino Inventor's Guide. Learn electronics by making 10 awesome projects.

**Dave Jones:** Let's have a quick check. Alright, let's have a look at the Arduino Inventor's Guide. It's actually by Sparkfun, so I assume that Brian and Derek work for Sparkfun. And there you go. Brian was a school physics teacher with a affinity for robotics. Derek is a middle school

**Dave Jones:** technology teacher obsessed with pushing the limits, etc. And there you go. Let's have a squiz. It's basically a project-based book, so they go through 10 different projects, and by the way, the book is $29.95 Yankee bucks, and includes the digital one as well, and the index

**Dave Jones:** is quite comprehensive. Each individual project, wow, I mean it's 330 odd, 310 pages long. So let's take a look. I mean, we'll just show you, we'll just jump through to project 10, shall we? They're all going to be very similar. Materials and stuff

**Dave Jones:** like that. Lots of very good photos. What is a membrane potentiometer? Look at that. Piezo buzzers. Building the circuit. We've got our requisite breadboard interface to Arduino type thing. Programming, testing, we've got some code. There we go, got some Arduino code. What you get in the console, and creating

**Dave Jones:** specific notes. Not a huge amount of detail on, like it's just mainly, you know, programming with the Arduino, a bit on soldering, things like that. So flicking through, it's like, you know, yeah there's some Arduino code and stuff like that. They do mention

**Dave Jones:** a couple of, you know, like electronic concepts and things like that, but it's basically just how to wire up the pre-programmed, the pre-made kits and stuff like that, and getting them going step-by-step, which is fine, but it's not something that you would want if you want to learn electronics

**Dave Jones:** or something like that. It's just, you know, how to build these particular projects. So there's not a huge amount of value in there unless you're actually building the projects. So there you go. It's a fine book. They put a lot of work into it.

**Dave Jones:** It's very nicely produced, as you expect from No Starch Press, but yeah, it's not, you know, but you've got a pony, you can't just buy the book. It's pretty useless on its own. You've got to pony up for the projects as well. But that's another quality No Starch Press book,

**Dave Jones:** and if you want to check it out, link down below. Thank you very much, Lee Sieng Silent I, maybe from Singapore. Hi to all my Singaporean viewers. I love Singapore. It's probably my favourite Asian stopover destination on the way because if you go, there's only

**Dave Jones:** two directions out of Australia, and if you go one way, you've got to go Asia. Basically, well if you're heading to Europe, you've got to go Asia. So thank you very much. I like the feel of this, because it's obviously going to be a PCB, and yes it is.

**Dave Jones:** Ah! Programmable timer switch. Geez, that's sizeable, isn't it? So Lee is from Malaysia. Big fan, thank you very much. Working on small projects involving some PICs. It acts as a timer switch. Just finished the PCB, which I wish we could take a look at.

**Dave Jones:** This is the first time designing circuits. I'm not really sure if the selected components and their values are suitable. Especially the decoupling and switch decoupling capacitors. Correct if you find any mistakes on the layout. Let's check it out. Alright, first up, your power supply section.

**Dave Jones:** You've got a series diode in there. No worries. It's better than like a back-to-back diode across here, which shorts out your supply if you get the polarity backwards. If you're going to forward the voltage drop, the 0.6 volts across there, or 1 volt, you know, like an amp

**Dave Jones:** or whatever, then it's better to have it in series. Because if you plug in backwards, it just you get no current at all, rather than just short it out. 680 mic is probably quite high for the input. You generally don't need that for just input stability

**Dave Jones:** on a regulator like this. Then, yeah, you don't really need that. Now as for the regulator here, the LD 11175, this is a low dropout regulator. And these are less stable than your regular like 7805 ones, for example. You need a specific type and size of output

**Dave Jones:** capacitors to, you know, make it work. It's not a problem, but it's just that when you've got a 9 to 12 volt input, I wouldn't be using an LDO here. Once again, it's still going to work just fine, but I would just be using biggest 5 volts out, just a

**Dave Jones:** traditional 7805, no worries whatsoever. And as I said, you don't need that bigger input capacitance. And the output cap, you've got the 100 in, 10 mic, and 4.7 mic. And I can see on the well, there's no plus mark on there, so these are all going to be

**Dave Jones:** ceramic caps. And really, there's no point to doing that, especially like something like the 4.7 and the 10 next to each other. They're so near to each other, they're not like an order of magnitude a decade apart. You don't really need that. So yeah,

**Dave Jones:** I don't know whether or not you got that from the data sheet or not, but I doubt it. Now these could be spread across the board, of course. It's typical to put the multi-bypass caps just on the output here instead of, I don't recommend it, but a lot

**Dave Jones:** of people do that, I'm guilty of it myself occasionally. But they're not spread out across the board. Here it is. They're just through all three in parallel like that, right on the output of the regulator, and there's just no point to that. It would have been

**Dave Jones:** fine with just, say, a 10 mic. If it's an LDO, it needs one mic minimum output capacitance or something like that, or the single 4.7. You didn't really need the other ones. And also notice the really large loop area here that I've highlighted

**Dave Jones:** in green. The ground of those three capacitors to get back to where it actually needs to be, which is the ground pin, pin number 1 of the U1 voltage regulator there. It's got a loop all the way around C1 like that, go right

**Dave Jones:** back through the input, go through that little sliver there, go through D6, and then up to the pin like that. And loop area is one of the big traps for young players in terms of PCB layout and, you know, EMC and the whole, you know, electromagnetic

**Dave Jones:** conformity thing. Now I won't go into the technical details of loop area, but it is one of the worst things you can do in PCB layout is to have large loop areas like this, and it's something that beginners get wrong all the time because they don't

**Dave Jones:** know about this sort of thing. And if you read the layout application notes, especially for switching regulators are really good. If you look at a good, any, almost any good data sheet for a switching regulator will talk about loop area and show you example PCB

**Dave Jones:** layouts, how the ground return of your bypass caps must be as close as physically possible to the ground pin of your regulator device. In this case we've got an LDO, so those three capacitors should have been like flipped over, so that the grounds are on the bottom, and then it just

**Dave Jones:** ground return returns straight over to the pin number 1 of U1 there. Or, as I'm going to mention later, you can do via stitching in there, like heavy duty via stitching. But in this case you didn't really need to do that. So it's important to put, in this case, at least one

**Dave Jones:** that one 10 mic is in the example application note across, pins directly across as close as possible pins 1 and 2 of U1 voltage regulator. Especially for these LDOs, they can be quite susceptible to oscillation and things like that. So having a large

**Dave Jones:** loop area like this may cause a regulator like this to be unstable. But in this particular case we don't have heavy loads, we're just driving a microcontroller it's not high frequency switching stuff, so it's most likely with 95% certainly going to work but hey, there'll be that 5% of the time when you're

**Dave Jones:** kamikaze and the thing oscillates or you get some other issue. So yeah, loop area. Look into it. And we'll go over to the microcontroller schematic here. The next thing I'm going to check is like the bypass caps on the micro to see if you've actually got them.

**Dave Jones:** And yes you do, there we go We've got two 100Ns there, that's fine because we do actually have two different power pins here. And if we have a look over on the board are they close? Yep, C10 and yep. So yep, that's fine and dandy

**Dave Jones:** having those reasonably close to the power pins. You've got them a little bit away, but for this it's not going to matter at all. The other thing I notice about your board here is that you've used what looks like 0603 parts everywhere. Why you do that on such

**Dave Jones:** a, well otherwise quite largely through-hole board, there's lots of other through-hole stuff, but like I don't, I personally I know some people are different, but I don't like going to 0603 unless I need to. On a board like this you'd be using, much better off using 0805

**Dave Jones:** even 1206s, but 0805 is generally the go. But I know a lot of people it's just like their go-to thing is the 0603. And well okay, but on a board like this I would have used larger parts. Here's something that I noticed on your layout

**Dave Jones:** just then. Your input cap is all the way over here you've got your power coming in like this, going off to your input cap, and then tapping off down here to your input. That's not what your input cap is for. Your input cap needs to be close to

**Dave Jones:** your input pin, and not just branching off like this. You don't want to go over to here and then coming back. If you had it over here for space reasons or whatever that's fine, but then have this trace coming off here and going back to the pin like that.

**Dave Jones:** But as I said, you should have it closer, otherwise you've just got the inductor in series, and that's not that great. And it's going to work in this particular case, but you know, little traps like that could ruin your day later on down the track when you get something more advanced.

**Dave Jones:** And the other thing with this board, jeez I don't know if I can get in there and measure it, but your your via holes there are absolutely tiny. What are they, like 0.4mm tops? 0.3? Something like that. You really don't need your vias that

**Dave Jones:** small, because you may pay a penalty in terms of manufacturing costs, because you might have to go to another manufacturing process to get the smaller holes. And two, it makes them not easy to solder wires and hack and mod and things like that.

**Dave Jones:** And the other thing is, the board while I do like the layout, which I'll talk about in a sec, but yeah, it is physically very large so you would have paid a lot, you know, much a lot extra for a board that big.

**Dave Jones:** It could have been shrunk down and made smaller, but maybe there's a reason, physical reason to make it that big, in which case it's fine, but yeah, otherwise I would have tried to get the size down on that. Now as I said, your layout's actually quite neat.

**Dave Jones:** You know, the traces are reasonably short to the point, like I don't know why you chose the locations you did, but okay, that's part of layout, you choose your locations for your parts first and then you route everything and all of your traces are quite

**Dave Jones:** nice. They all flow around like this, around into there, there's just some short ones. You've got multiple directions on here, but you've got to do that on a double-sided layout. You've got your flood fill plane all over. I don't necessarily see any via stitching like joining

**Dave Jones:** these ones together. So like, you know, it's snaking through here like this. And once again, it's not going to matter on just a timer thing like this. There's no high current stuff, there's no, you know, high frequency stuff or anything like that. It's going to work fine, but on

**Dave Jones:** generally speaking, yeah, you would have added, you know, vias in here to, you know, stitch these and keep the ground planes short rather than create huge loops, like going all the way around here like this and coming back like that. You would, you know, have stitching joining both sides.

**Dave Jones:** As I said, it's not going to matter on a board like this. But otherwise, like for a first design, a first layout, that is excellent. Well done. As for some of your other component values, like 8.06k. You've obviously used the E96 range there.

**Dave Jones:** There's no need to have such precision in a simple base resistor like that, you know. So you use like E12, like an 8k2, something like that would have been fine. And your crystals are correct like this, with your traces coming in kept short, and then your caps

**Dave Jones:** going down to ground, no worries. And then for your microchip MCP7940 real-time clock chip, I don't know why you've got a diode in series with the battery here. You really don't need that. The coin cell holders, like if you put them in backwards, they're going to be okay.

**Dave Jones:** You don't need the 1k series or the diode there. But you can see what you've tried to do in actually protecting the battery putting in, but generally you just, you don't really need those. You can hook your battery straight onto there, no worries.

**Dave Jones:** The reason you can do that is because the internal resistance of the coin cell is actually quite high, and you know, it can't deliver like, you know, a huge amount of current to damage anything, even if you were able to shove it in the

**Dave Jones:** holder back to front, it's generally not going to damage these types of chips. And as for your various switches here, I'm not sure where the switch, are they on the oh yeah, up-down menu, okay, all that sort of jazz. Yeah, you don't need these, I don't know why you've got

**Dave Jones:** the 1k protection resistors in here, and yeah, probably I see why you've done the RC debounce here, but generally you shouldn't need to do the RC debounce, so pretty much all those components will be redundant. And as for the pull-up resistor, well you can just use

**Dave Jones:** the pull-up resistor inside the chip, no worries. And for your relays, excellent, you've got your back EMF protection diodes, nice. So yep, for a first design, that is a bloody ripper. Good on you, Lee. Sir David Jones, thank you very much indeed, a person

**Dave Jones:** unknown, from Parts Unknown. I just killed the stamp, I don't know where that's from. Anyway, let's check it out, see what we've got. What on earth? It is a chocolate bar calculator, a B10 Choculator. What? That's gold. Thank you, Nick. Spotted this Choculator at the boot sale and thought you, if anyone

**Dave Jones:** would mind lifting the skirt on this old four-banger, I'd like to know the source of its unique aroma. Yeah, it does have an aroma of kind of a cross between plastic and chocolate is all I can say. Hmm. Pom in Prague, thank you very much, Nick.

**Dave Jones:** It's a chocolate calculator. Wow. Point over here, one, four, oh, I heard that creak. That wasn't good, was it? Anyway, it works. It's fake solar cell, there's actually a battery in there. Well, it could be dual power, but like yeah. Weird. Let's crack it open.

**Dave Jones:** Alright. We're getting in and yeah, there's our battery and uh-oh, looks like a real solar cell is actually hooked up, but yeah, we've just got the membrane keypad, that's it. And we have this is weird. Oh, no, right, it's just like it's going to be a chip

**Dave Jones:** on board on the back of there. Hmm. And well, yep, that's all she wrote. Hmm, well, you know, chip on board and a membrane keypad. Now, I was going to guess that the chocolate smell of this thing actually maybe because they bundled this with some chocolate in the same

**Dave Jones:** packet and it's like seeped into the plastic or whatnot, but I googled it and apparently they actually sold this as a chocolate scented and shaped calculator. So, like, they've actually they've infused it with a chocolate smell. Like, why do these things exist? What is, like, wrong with this planet?

**Dave Jones:** Like, I don't know, maybe someone wants it then you can get, you know, you can get fake dog poo and farting novelty gnomes and spank-o-meters and oh, geez. Hi to all my German viewers and thank you very much, Alex Hauk. H-A-U-C-K. Hmm, from which part of Germany?

**Dave Jones:** Rothenburg. Haven't been to Rothenburg. So let's check out let's see what's in here. We've got a postcard from one of your latest videos. Seriously? Yes, the problem with the stupid binding posts on all these looks like it's a plague. All of these damn electronic

**Dave Jones:** loads. Awesome. Thank you very much. Aww. Beautiful. There you go. Binding post to banana plug attachment. Beautiful. Now you've seen this BK Precision electronic load before and the annoying binding posts on it. Yeah, they're great if you've got the huge lugs to put on there, but if you just want to plug some banana

**Dave Jones:** plugs in like they've got no hole in there on the end to plug the banana plugs in, they've got no hole in the side of the thread so that you can put your wire through and then screw it on. No, it's just got the stupid lugs.

**Dave Jones:** So thank you very much, Alex. I think somebody else was going to send me one of these too, but they never actually got around with it and it's just a simple board which goes over the terminals. There we go. Look at that. They've

**Dave Jones:** taken off some of the coating there just to get some extra current handling capability. Not that it's going to make a huge amount of difference, but that is very very nice. A very nice solid insulated binding banana plugs. And it just goes over there like that.

**Dave Jones:** Beautiful. It makes contact on the top side and the bottom side of course. Fantastic. So that is an absolute winner, and I'm going to leave that permanently connected because I'll probably use it 95% of the time instead of the binding posts. And they've got the banana plugs

**Dave Jones:** coming out the right way, because you want the cables coming out this way instead of if they were coming out this way, then it would be over the buttons. If you had them coming out the top it would get in the way of that.

**Dave Jones:** You could have them coming out the front, I guess, but then it would get in the way of turning these, so that's ideal. Perfect. Unfortunately it's not the same for the Rigol one, which has the same issue with these stupid things. Anyway, I should be able to fix that

**Dave Jones:** by just drilling another hole in the side there and scraping off some of the solder mask there and on the bottom and that'll work a treat. So yeah, what do they do, like copy each other's like design binding posts? I don't get it.

**Dave Jones:** Another Succula Sav from Germany, um, from Person Unknown. Thank you very much, Person Unknown. Let's chop the note. Whoa, what's something in here? What? It's a switch. Why do we have a PCB mount switch? Hi Dave, I've had this for some years but never got around to sending it.

**Dave Jones:** In one of your videos you mentioned you broke the power switch of your Rigol DS. Oh, 1052 I did the same while changing the fan in mine. Oh, thank you very much. I tracked down the supplier in China, well done, and got a few replacement

**Dave Jones:** switches, so have one. Awesome, thank you very much. Yes, I did break my busted my Rigol original Rigol DS 1052E that's at home now, so I won't be able to show you that that's like Sagan's oscilloscope, he plays with that. Great, thanks, awesome

**Dave Jones:** replacement switch, winner. No drugs because, well, yeah, we do have pretty strict customs here they won't muck around no drugs, only an electronic USB chip to the value of 0.1 cents. Thank you very much from somebody from Laas in Norway. Hi to all my Norwegian

**Dave Jones:** viewers, how's it hanging in Norway? Or, grid paper nice, what have we got? We've got a tiny look in the microscope okay, we've got a tiny little hoard thank you very much, still person unknown with beautiful penmanship look at that, look at that

**Dave Jones:** fantastic, like it's not, you know I just like it, it's not your classic penmanship, but it's almost it's beautiful, they're all the correct height, and it's wonderful excellent. Unfortunately stops decoding in MPEG4 world's smallest TV dongle from sandburz.it, Italian okay, we'll have a quick squeeze under the microscope

**Dave Jones:** so there you go, the world's smallest TV DAB FM receiver that plugs into the USB, no it doesn't it used to have a USB plug on it I think, but yeah, it's tiny just antenna connector on input and yeah, let's check it out, I'll get the macro lens

**Dave Jones:** and there's the top side, looks like we've just got mostly regulator stuff, you can tell just by the bypass caps and the typical 5 pin SOC 23s, that'll do the business and, what have we got? Couple of chippies on the bottom, that's it, geez there's not much doing is there

**Dave Jones:** and that puppy there is a Realtek RTL 2832, and that's just a USB input DV receiver, it's like all the magic smoke is in one chip. And the other one right next to the antenna, dead giveaway, is the RF Tuner it's an Elonyx E4000 and

**Dave Jones:** apparently these were the ducks guts in the SDR community, the software defined radio community, apparently this combination of chipsets was apparently highly regarded, but Elonyx have apparently folded and you can't get the E4000 chipset anymore, so this is an older design, but apparently

**Dave Jones:** a lot of people use these things for software defined radio stuff, cool. As for heat building up inside the rubber, I'm not sure what the casing it was, but the chipsets wouldn't take much at all I mean these are linear regulators on here, but like you know, 79 milliamps at

**Dave Jones:** 1.5 volts for the tuner, I don't know the Realtek chipset PDF doesn't seem to be easy to come by, probably under bloody NDA or some crap like that, but yeah I don't think it would have consumed a huge amount so I don't think that would have been an issue.

**Dave Jones:** Thank you very much Steve Fazio, or is it Fazid? I think it's Fazio. From Geneva in New York USA once again, hi to all my New York viewers, is there anyone else in Geneva? I've never heard of Geneva, New York I've been to Geneva, Switzerland

**Dave Jones:** been there, but I haven't been to Geneva, New York that I'm aware of anyway. Tissue, oh we have, oh nice, look at that, beautiful handcrafted, it's a solder dispenser wheel fantastic! There you go, scan me Thank you very much Faz, who's a youngster and works on restoring

**Dave Jones:** scopes among other things, these are some various scopes, his favourite is the 7834 awesome analogue storage, ooh fancy pantsy, and designed this little, well built this handcrafted little solder dispenser. Perfect! I've only got the one here and I've got I've only got the one here and I've got multiple rolls of solder, so

**Dave Jones:** that one's going straight to the pool room. Thank you very much it's going to work a treat. Thank you very much Steve Kepler from Leo, Indiana. Yes, it's a Yankee fest, I just pick these randomly I hope it's not fragile Anyway is there anyone from Leo?

**Dave Jones:** Right Circuit Classics a stepped tone generator, sweet! It's got to be a kit. We have note, we have a blank board, and nice! Oh, it's the old Forest Mims circuits brought back to life by I didn't know it was Steve Kepler, it's Star Simpson

**Dave Jones:** who sells these on Crowd Supply, so I'm not sure if Steve is related in some way to that, or whether or not he just randomly sent me a kit. Anyway they brought back the Forest Mims, there's like a how to solder in the

**Dave Jones:** Forest Mims kit. If you don't know we've had Forest on the Airpower podcast, which I'll link in down below Fantastic! A couple of hours, the guy's brilliant So, yeah, let's check it out Yes, so this is the Forest Mims the third, who we've had on the Airpower, fantastic

**Dave Jones:** multi-hour interview, I'll have to link in, and this is basically his project recreated, complete with his original hand-drawn schematics, straight out of the book, look at that, and the various notes and whatnot, from the engineer's mini notebook, the triple five timer IC circuit, page 22

**Dave Jones:** and obviously there's a coin cell battery that goes on the side there, and these were done by Star Simpson so I still don't know what Steve has to do with that but anyway, thank you very much, and it comes with the little original hand-printed, hand-done

**Dave Jones:** Forest Mims how to get, how to solder thing, and this is the IC circuit, classics, there's a whole collection of these which I'll link in down below, oh, look at these, cute anyway, came with all the parts that'll be a kit that Sagan and I can assemble together

**Dave Jones:** brilliant, thank you very much Steve Thank you Chris Cochran, with a K from Northumberland in the UK, the old Dart so let's have a look, from the description on this we've had plenty of these, so I hope it's something for Dave ooh, it's purple, ooh, thought I had the open source

**Dave Jones:** hardware thing, it's not, it's not the key so retro gear, well let's check it out first here we go, and ah, yep, Scion we have done, made in the old Dart people probably haven't seen all my mailbags but we've had Scions at least

**Dave Jones:** 2 or 3 times, cool it's the Scion 2, model CM so we've already done a teardown, unfortunately so yep, we've definitely seen one of these, this is the model CM made in the old Dart, of course fantastic, the Scion Organiser 2, and yes it was one of the

**Dave Jones:** first usable PDAs, and these things were massively popular remember I lusted after these, but we have done a teardown and an extensive comparison I think of the various PDAs back in the day but yep, got a processor in there, we've just got some

**Dave Jones:** SRAM, none of that modern DRAM rubbish this would and of course the program packs you could just slide the program packs in, they'd just go on these .1 inch headers and they had pre-programmed you know, expanded memory and pre-programmed apps and things like that, and these were very popular

**Dave Jones:** probably more so in the industrial market for like inventory control and things like that, they were really huge I don't know which would have been bigger, the consumer or that industrial market, but my guess might be the industrial market in the end because these things were built like a brick dunny

**Dave Jones:** Hi to all my Austrian viewers, in particular Reinhard Greil from Osterich in Austria not Australia, let's crack it open once again, we've had these on, oi that, sweet that is a full on radio son we have had one of these before but this, ah, Vesala, we've had the Vesala radio

**Dave Jones:** sonde before, but this looks like a complete intact one, the one we had before was like a real old much older one, it was like 20 years old or something in like a, was it a cardboard and styrofoam box or something? This one's in a proper plastic

**Dave Jones:** geez it weighs a bit, because normally if you don't know what a radio sonde is, these things are atmospheric sensors, hence all the fancy whiz-bang stuff up the top, and they sense, you know, temperature, pressure, altitude all that sort of jazz, and they transmit it back to the

**Dave Jones:** ground, they send them up, they're basically weather balloons and that's how they do it, they whack them on the helium balloons and up they go and they drift around and they get the, I assume they get the location as well and transmit it all back, anyway

**Dave Jones:** very cool, wow is this worthy of like a separate teardown video perhaps because they're fascinating stuff, they really are yeah, oh geez, it's even got a little port on it wow, yeah, if you don't see this in the mailbag, it's probably because I thought it was too interesting and I decided

**Dave Jones:** to do a separate teardown video on it. I got the note with it, this one actually fell into Reinhard's backyard with a note attached to it saying it belonged to a weather balloon and he should be so kind as to dispose of it, so instead of disposing of it, he decided to send it

**Dave Jones:** straight to us, fully intact awesome, yeah, these things litter the planet, they just you know, they send up thousands of these radio songs probably every day and to get, you know, weather data and stuff like that so, fantastic, I love it to his backyard, what are the odds of falling into a, well

**Dave Jones:** I've got like almost half a million subscribers, so maybe can anyone calculate the odds, how many go up per day versus the square area versus like number of viewers? thank you very much Reinhard, who was lucky enough to have one of these land in his

**Dave Jones:** backyard, directly near his garden hanging from a parachute, and I've done one before but it was an old model, this is a newer model, which has the GPS antenna, the transmitter, all the sensors and things like that but I'm going to save that

**Dave Jones:** for not only a separatarium video, but I'm thinking it might be an EEVDiscover video, if I can get the right contacts, I might be able to do some interesting stuff with this, but yeah somebody on Twitter said they actually work for Vasala, I don't know

**Dave Jones:** how you pronounce it, and they manufacture they said thousands of these are released per day, and they are a one shot deal so I'm going to leave that as a tease sorry, next and also somebody on Twitter actually converted their car into a tracking vehicle, I believe he's from South Australia

**Dave Jones:** and actually tracks down these, you can actually get modelling software to predict where these things are going to land, and then you can go and hunt them down and it's a bit of a game, and some people out there go and hunt these things down

**Dave Jones:** and have a big trophy wall of all their radio songs brilliant. And you may know what this is from Zintany Ra, thank you very much I've done a video, was it a video? Yeah, it was a video review of the Zintany Ra backpack

**Dave Jones:** light, and they actually saw that Kogala is the company, and they said they'd send they said they liked the video and they appreciated the feedback and all that sort of stuff and they said that they would send me some accessories for it, so thank you very much

**Dave Jones:** Egyptian stuff, cool I'm really into Egyptian stuff and yeah, these are like little attachment things which you can put on it so you can put it on your backpack and whatnot and they've sent me another battery pack tiny little battery pack oh, isn't it cute

**Dave Jones:** anyway, can't do a teardown, it's all ultrasonically welded or whatnot, but assembled in China, US patents pending what, a design patent for how can you patent just a battery pack it has to be a design patent in terms of the look and feel kind of thing

**Dave Jones:** I think we might have a couple of more PCBs this one's from Person Unknown, so let's just probably shouldn't have done that because it has like a note we have a PCB it is a smart supply oh, wow, okay, cool it's a, there you go

**Dave Jones:** it's probably a variation of the micro supply somehow two 18650s neat, 0 to 20 volts, 0 to 1 amp sorry for ripping that later, that's a real pain in the butt isn't it, geez, electronics engineering student from Belgium, thank you very much, Thomas

**Dave Jones:** yeah, he stumbled across my micro supply project and knew he wanted to make one, only to find out after 14 episodes that you didn't finish it, yeah, sorry, various reasons for that we are working on it again, actually from completely from scratch, it's not based on this

**Dave Jones:** LT3080 design anymore so it's a smart supply, that's neat glad it worked out for you, I got quite a lot of people actually built their own variants based on well, my last micro supply schematic based on the LT3080, cool, nice work hi, I'm Thomas, an electronics engineering student from Belgium

**Dave Jones:** hi, I'm Dave, and I'm a dickhead for tearing your note with my big ass knife anyway, he stumbled across a micro supply project first time I saw the video, I knew he wanted to make it after 14 episodes, we never finished yes, we didn't finish, but

**Dave Jones:** having said that, David Du and I are now working on the micro supply again, it's not carrying on from where we had before, but trust us, we are working on it big time, so hopefully we will come out with that, and videos will be

**Dave Jones:** posted, there's some talk I've done, there's a section on the EEVblog forum where I've shown like a custom LCD which we're going to do for it, and stuff like that, and everyone's discussing it, and things like that from that, no other details, sorry, anyway

**Dave Jones:** specifications similar, 0-20 volts, 0-1 amp powered from two protected 18650 lithium cells, and it looks something like that isn't that neat? I can't remember what my interface looked like, it was very similar to that, wasn't it? Set and out and put it into a funky little case

**Dave Jones:** and isn't that jazzy? There you go so I'll link it in down below where is it? Do we have a website somewhere? GitHub, there we go, GitHub, ThomasVDD smart supply, fully fledged open source hardware logo, excellent, hasn't got my letters on there though, so that looks pretty jazzy doesn't it?

**Dave Jones:** I like it, cool bananas, there you go a lot of people have done micro supply type variants of the project and I totally encourage it, it's great to see yeah, there's lots of people on the forum who've done that sort of stuff, I like how it's almost all

**Dave Jones:** through hole, except for that puppy up there but anyway, that looks like a nice layout jazzy, aha, there's inside the finished product and yeah, we've got the, using the back panel as the heat sink in time honoured tradition, and it looks like it uses the LT

**Dave Jones:** 3080 still, so there you go so well done Thomas, that's an excellent implementation linked in down below, it's all open source-y Hi to all my Finnish viewers, this one's from Julius Willuco from Espoo Espoo in Finland, there you go let's have a squares, I believe this one is a

**Dave Jones:** PCB, feels like a PCB it's always a dead giveaway, hi Dave this is mystery PCB, can you guess what it does and what it's electrical function is? Julius Willuco from Finland, the answer is it's in this second envelope, ah, there's a second envelope

**Dave Jones:** no, no, no argh can I guess the circuit function oh, jeez, it's got two it's like, there's no the only tracers on there are tell the hand focus, the only tracers on there are those two big fat ones yeah, you can see that there, those two big fat ones

**Dave Jones:** so it's some sort of, well it's high current and everything else is like mechanical type interfaces, so it's like, I would say it's from some maybe a little robot car or something like that, it's probably got some high current motor drive or something, it's kind of like a base, or it could be

**Dave Jones:** like for a quadcopter or some other base that mounts motory type things onto it would be my guess gotta go to that web address to see if I'm right bang on, I just went to check and it's for a slot car, it's actually the bottom chassis of a

**Dave Jones:** slot car with the motor connection and stuff like that, like a homemade slot car so yeah, I was bang on, it hooks up to the motors and it's the mounting, like I said it was a base kind of thing and motors hooked up and that's exactly what it was

**Dave Jones:** a slot car, cool, see, wasn't that hard mystery PCB, nailed it hang on, that was easy thank you for watching and I'll see you in the next video peace
