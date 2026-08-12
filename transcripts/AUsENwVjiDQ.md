---
video_id: AUsENwVjiDQ
title: EEVblog 1596 - NEW Digilent Analog Discovery Pro ADP2230 TEARDOWN
url: https://www.youtube.com/watch?v=AUsENwVjiDQ
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 35, "3": 55, "4": 68, "5": 79, "6": 90, "7": 106, "8": 118, "9": 131, "10": 141, "11": 156, "12": 168, "13": 186, "14": 205, "15": 217, "16": 233, "17": 245, "18": 260, "19": 274, "20": 287, "21": 296, "22": 306, "23": 317, "24": 328, "25": 341, "26": 351, "27": 360, "28": 375, "29": 398, "30": 412, "31": 423, "32": 433, "33": 447, "34": 460, "35": 473, "36": 484, "37": 498, "38": 509, "39": 518, "40": 534, "41": 544, "42": 554, "43": 567, "44": 582, "45": 594, "46": 602, "47": 621, "48": 642, "49": 661, "50": 678, "51": 693, "52": 704, "53": 715, "54": 731, "55": 743, "56": 755, "57": 768, "58": 779, "59": 798, "60": 812, "61": 826, "62": 840, "63": 851, "64": 867, "65": 880, "66": 892, "67": 910, "68": 920, "69": 936, "70": 947, "71": 955, "72": 961, "73": 975, "74": 989, "75": 1002, "76": 1014, "77": 1027, "78": 1042, "79": 1052, "80": 1063, "81": 1078, "82": 1090, "83": 1099, "84": 1110, "85": 1132, "86": 1141, "87": 1155, "88": 1177, "89": 1187, "90": 1197}
---

**Dave Jones:** Hi, welcome to everyone's FAVORITE SEGMENT, MAILBAG. UM, this one's going to be a single item mailbag cuz that's all I've got from Canton Technologies. So, I have no idea who that is or what this is.

**Dave Jones:** So, uh, tongue at the right angle. And what do we got? Reusable reusable FedEx packaging. Okay. Oh, okay. It's something like It's something from Digilent. So, I guess that that uh, company was a Digilent shipping thing.

**Dave Jones:** OH. OH. OH. I HAD NO IDEA. OH, YES. YES. Look at this bad boy, the Analog Discovery Pro. It's the um, ADP 2230. Of course, I've covered the Analog uh, Discovery before.

**Dave Jones:** I've probably done several videos on it and it is like it is it is awesome. It's the software that makes it awesome. The hardware is just the hardware. I mean, it's just, you know, an ADC and FPGA and Bob's your uncle, really.

**Dave Jones:** Um, all right, it's got an adjustable power supply and stuff, but, you know, and it's great because it's got like the best software in it. It's so flexible. And this is their new This is their new pro version.

**Dave Jones:** Wow. I didn't know they were going to send this. So, that's really something. And product is considered used if seal broken. Oh, well. We now have a used Digilent.

**Dave Jones:** Um, that's that's really schmick. I like the green alloy case on that. Check that out. That's pretty groovy. I'm liking that. So, there you go. So, woah. Film film.

**Dave Jones:** Look at that. Yeah, I mean, we got proper BNC inputs. Um, we've got uh, digital um, inputs. And is that pink connection the standard Analog Discovery interface? I don't know, but what else do we get?

**Dave Jones:** We get stickers, very handy. We get a USB-C to USB-C, the 0.1 in pin header probes, got some spare pins, and a couple of probes. Okay, what's the bandwidth of this thing?

**Dave Jones:** I can't remember if this is just like the regular Analog Discovery, but like in a like a professional box, maybe with a beefier power supply or something like that, or whether or not it's got upgraded specs.

**Dave Jones:** I don't know. Let's find out. Well, turns out this product is so new that it doesn't exist. Like, I'm not kidding. This product does not exist. Boy, here's the card that comes with it.

**Dave Jones:** I got no other information. And when you search ADP2230, by coincidence, that just happens to be an Analog Devices DC-to-DC converter part. Obviously, ADP is Analog Discovery Pro, so that makes sense.

**Dave Jones:** And 2230, that is this new model. So, you know, I'm supposed to register here. I go to this address and Wave Kamigata. And then if you go to products over here, they've got the Analog Discovery Pro, which is the big daddy, which I've got, kind of, as the National Instruments Virtual Bench.

**Dave Jones:** And they basically, when National Instruments bought Digilent, they basically rebadged the really high-end, I've done teardown of the really high-end National Instruments Virtual Bench that I've got here, which that's the one I use for like all my on-screen multimeter stuff.

**Dave Jones:** They basically just rebadged that as the Analog Discovery Pro ADP5250. And unfortunately, mine doesn't work with the new software, so I still got to use the old Virtual Bench software.

**Dave Jones:** Anyway, they've got that model, and then they've got this one here, which is the Analog Discovery Pro 3450 and the 3250. So, I assume that's bandwidth. So, that's a four-channel jobby, whereas uh this one, of course, is only a uh two-channel jobbie.

**Dave Jones:** So, this is This is so new so new that it doesn't exist. And I downloaded and installed the latest beta software from only just under 2 weeks ago. It doesn't It doesn't actually work.

**Dave Jones:** It recognizes it, but I think it's just getting that from like a universal descriptor or something like that. Um so, it's getting the serial number of it, and it's getting like that's USB 3 5 gigabit per second, right?

**Dave Jones:** So, it's actually connected. I've got it physically hooked up, and it says uh check device not supported, no configuration found, check for software update. So, there you go. It's so new that it doesn't exist.

**Dave Jones:** So, I can only presume it is a low-cost version of this Analog Discovery Pro here. Now, I believe this is actually quite expensive, right? This four-channel jobbie. So, I believe what they're doing is I guess they got a lot of complaints.

**Dave Jones:** Oh, oh, oh, oh, we only need two channels, right? We don't want to pay for the four-channel jobbie. And it's like it's 1,300 bucks, right? This is a serious bit of kit.

**Dave Jones:** Okay, you can buy a serious benchtop oscilloscope for the price of this, but you can't get the 14 bits, um and you can't get the fantastic software with it, right?

**Dave Jones:** Which is the absolute killer part of this. You're not necessarily paying for the hardware, you're paying for the uh software that goes into this between the Analog Discovery 3 and the uh and this one up here.

**Dave Jones:** And this this one, if you have to ask the price, you can't afford it. And it's, yeah, 2,500. This is Yankee bucks. And the Analog Discovery 3 is 379.

**Dave Jones:** So, I'd say maybe this new one possibly like fits under there I like I'd be say 700 bucks, 800 bucks, maybe, something like that. Don't quote me cuz I have absolutely no idea uh get any info on this.

**Dave Jones:** But if I can, I'll include it in the overlay. So, I guess all we can do today is a teardown. Anyway, there really is no point me going over the fantastic software for this.

**Dave Jones:** It's the same software for this as it is for all the analog discovery products and it's brilliant. I've done like a the extensive review of the analog discovery 3.

**Dave Jones:** So, anyway, so I've got a nice extruded alloy case here. We've got the external 5-volt DC input, the USB 3 over here and it's apparently designed by Digilent in Romania and here and the USA.

**Dave Jones:** I assume it's made in China, but you know, it would have been nice if it was made in Romania. Come on, Digilent, you can do it. It would have been nice if it had the separate banana plugs on there for the power supply because you know, it's got a reasonable little power supply, useful little power adjustable power supply in it that can you can ramp it up and do

**Dave Jones:** all sorts of you know, wonderful things and you can trigger from it and do all sorts of great stuff. Yeah, it would have been nice, but I guess that's you know, encroaching on the territory of the higher end pro model which actually does have Oh no, I thought this pro 3000 had the banana plugs.

**Dave Jones:** It it doesn't. So, you have to go over to the that really high end virtual bench one for 2500 before you get actual No, no, on that you don't even get the banana plugs.

**Dave Jones:** You just get the That's right, screw terminals. My my one's actually slightly different to this. My one does actually have the banana plugs on the National Instruments virtual bench.

**Dave Jones:** I thought they did have a version of that identical one, but Okay, but they do have this discovery USB programmable power supply over here. So, yeah, I guess they're protecting that market.

**Dave Jones:** If you want that, there's a separate little power supply. 500 BUCKS, THAT'S PRETTY PRICEY. ANYWAY, YEAH, I would have liked to have seen, you know, just a couple of small a posts or at least some screw terminals.

**Dave Jones:** Maybe, you know, you could have shifted this over on the PCB layout a bit and just added a couple of you know, couple little Phoenix contact you know, screw terminals on there or something perhaps.

**Dave Jones:** That would have been nice. But anyway, you've got the pin header. There you go with a 14-bit 125 megasamples per second, 14-bit 125 megasamples per second scope as well.

**Dave Jones:** I'm Does that correspond to the Analog Discovery 3? Except on the Analog Discovery 3 is 30 meg bandwidth 55 meg bandwidth on this one. So, I assume this one is 55 as well.

**Dave Jones:** Although, 2230 might mean it's a 30 meg bandwidth. So, that would be my guess. The 2230. I think that's what it means. Same bandwidth as the Analog Discovery 3.

**Dave Jones:** It's just in a more pro-y case. No, I suspected there may not be anything under there. Oh, I've got to get in here somewhere. That's This is a split case.

**Dave Jones:** So, this back panel has to come off. Is that like glued in or something? Cuz I don't There's no hidden screws. Uh Aha, that's a sticker. That makes sense.

**Dave Jones:** That That looked like part of the like a back panel, but it's not. Yeah, it's got to be a screw under there. Or is it on the front? No screws under there.

**Dave Jones:** What is that gigantic hole under there? Whoa, there you go. That's a bit brutal. Had to get medieval on its ass here. A bit of the glue's come unstuck.

**Dave Jones:** So, what are they? Deep long screws or something? Yeah. Yeah, I do feel something. So, I think that's That is a screw in there. Yep. Oh, that's weird, isn't it?

**Dave Jones:** I don't think I've ever seen that. Leave it in the comments if you've ever seen an extruded aluminum case like this that has um screws going right through to the front panel.

**Dave Jones:** That's really That's really quite something. I don't know if I'm in there. That one's not coming out. What I might have to take the sticker off the front. Got a lead under there.

**Dave Jones:** If I bash on the connectors, I get nothing. Doesn't budge. What the heck? So, in complete desperation, I had to get that front panel off and you can see that screw hole down in there.

**Dave Jones:** I got that one out, but I didn't get this one out cuz it's like it's threaded or something. So, give it a whack. It's not coming out. I think this requires the AEE hammer.

**Dave Jones:** Harder, maybe. Geez, the other screw came OUT PERFECTLY. DIE. UH, SOMETHING CAME OUT. HEY, THERE WE GO. Got it. Got it. Look at that. Bobby does laugh. Well, WHAT A TURD THAT WAS.

**Dave Jones:** I TRIED TO be as gentle as possible, but nope. Nope. Anyway, um yeah, I the screw The screw is still down in there. You can see it. And I had to shear off the plastic just by brute force this plastic extension here um just to get that out cuz that screw was stripped, stuck, no idea what.

**Dave Jones:** I still don't know. It's still in there. So, this plastic end piece actually must come out somehow, but I don't see Maybe it's just glued onto the end or something.

**Dave Jones:** Not sure what the deal is. Analog Discovery Pro ADP 2230 that you cannot get yet. So, yeah, they've got a two-channel jobby instead of the four-channel. And I'm sure how different this is to the uh Analog Discovery 3.

**Dave Jones:** So, I'll take some high-res photos of this. I'll put on eevblog.com and linked into my Flickr account. So, yeah. Because I'm sure I'm the first one to do a teardown of this bad boy.

**Dave Jones:** We've got two power supplies there. Are they fixed at 10 volts and minus for our waveform gen? Presumably, but what everyone wants to see, of course, all the magic's in the Spartan-7.

**Dave Jones:** Not sure how much that bad boy uh cost, but it's I believe these are fairly grunty ones. I'll try and find a price. Obviously, they get it cheaper because uh Digilent originally, I think, did a deal with Xilinx, didn't they?

**Dave Jones:** And they That's how they could get the price down on this thing. Now, it's not so cheap. Back when it was like a student thing, it was cheap. Anyway, external memory there.

**Dave Jones:** Oh, upside down. All the electrons are going to fall out. 3.3 volt rail there. Looks like we've got our input protection there for our logic inputs. UPS, that would be the universal power supply, would it?

**Dave Jones:** Positive and negative rails, so that would be the adjustable power supply, is it? So, there's our 61175 boost converter there. 3-amp high-voltage boost converter soft start programmable switching frequency.

**Dave Jones:** So, are they adjusting the feedback resistor there to give them the adjustable power supply? Don't know what that five-pin jobby is there, but they might very well be doing that.

**Dave Jones:** That would give them the adjustable supplies and 1.35 volt core voltage for the FPGA and or memory. 5 volts VCC here, another 1.2 volt core. There's There's a ton of voltage levels are required here.

**Dave Jones:** That looks like our USB power delivery controller there. So, that'd be handling all that. 1.8 volt core reg, 2.5 volts analog uh VCC, so that'll be for the ADC, would it?

**Dave Jones:** And where is all the magic happening? That would be there. That would be your analog That would be your ADC. There she is, the ADC 3644, 14-bit, 125 megasamples per second.

**Dave Jones:** I I think that's the same one used in the Analog Discovery 3. I'd have to actually look up my previous teardown to do a comparison. There's your arbitrary waveform generator, DAC 5672, relay output, there's your output termination resistor.

**Dave Jones:** That's a 14-bit, 275 megasamples per second and DAC. So, yep, exactly what you'd expect. Is that the same? And if I go to the EVblog Flickr account, there it is.

**Dave Jones:** The Analog Discovery 3. Yeah, the DAC 5672, it's exactly the same. And the 3644, it's exactly the same. I like the front end is going to be I reckon the front end's going to be exactly the same.

**Dave Jones:** Oh, that looks shorter. No, the new front end looks different. It looks shorter. So, that's an XC7S25. And on this one, aha, it's an XC7S53. Say that three times quickly.

**Dave Jones:** Yeah, so that one's more betterer. It's got going to have more logic elements. I'll might put up the difference here if I can, but yeah, it's got a bigger, badder FPGA in there.

**Dave Jones:** And but the same ADC, the same DAC, but that front end looks looks physically shorter. So, I'd say they've they've reconfigured or redesigned that front end. I think I'm going to have to desolder those so to get a look at that.

**Dave Jones:** I'll take one for the team. Anyway, your bottom side of your PCB looks like that. And what do we got over here? Is that a Cypress USB? Yeah, that's easy USB super speed USB controller there.

**Dave Jones:** So, that handles all that. It's got a USB 3.5 and all the rest of the goody USB on the go, blah, blah, blah, blah, blah. But that other chip there, I reckon is doing some power delivery negotiation perhaps.

**Dave Jones:** And yeah, that's a TI jobbie again. Wow, um USB type-C DRP port controller super speed. Yep, with integrated super speed marks. Supports up to 15 watts of power delivery with 3 amps.

**Dave Jones:** Yep, yep, I think this is 3 amp rated or something like that. Um and it does come with the plug pack. So, that just interfaces your power delivery stuff.

**Dave Jones:** It's all they're using it for, I think. Well, there you go. That was a bit of a fight to get that off, but I got it. The other one will be absolutely identical.

**Dave Jones:** So, there's no point. Uh two trimmers exactly the same as we have on the other one. I think it's actually exactly the same arrangement. I think they've just re-laid it out because if I show you the difference, if I orient it this way and I'll swap between, there you go.

**Dave Jones:** So, that's the old one that Well, the old the Analog Discovery 3 and it's basically just a re-laid out front end, I think. This is a 4817. I don't know what that is.

**Dave Jones:** So, it maybe that is that is a bit different. Almost the same arrangement. Got differential output here, obviously. So, that's a differential gain driver stage. What's a 4817? There you go.

**Dave Jones:** That's a 1 gig bandwidth fast FET op amp. So, 1 gig bandwidth minus 3 dB. So, yeah, that's exactly what you'd expect to find. Guess Oh, look, ADC drivers.

**Dave Jones:** Go figure. Instrumentation. The analog um acquisition front ends and stuff like that. So, yeah, exactly what you expect. Slightly better performance perhaps or something, but there you go. That's the analog front end DAC output.

**Dave Jones:** We've got our ADC, of course. So, this will be identical up there. Got our two trimmers. It is shielded. They did add ability to uh shield the arbitrary waveform gen and DAC down here, but they didn't do it.

**Dave Jones:** And it's got a slightly more betterer FPGA. Most of the rest of it is just yeah, your power supply stuff and exactly what we saw on the Analog Discovery 3.

**Dave Jones:** On the bottom side, just some extra stuff down here. Oh, there we go. There's our Is that our solid state uh relay there for the AC coupling by the looks of it.

**Dave Jones:** So, the mechanical relay on top side must be doing the uh range selection. So, that's about all she wrote. And then is that like just a little power supply or something next to it, little local power supply?

**Dave Jones:** Perhaps for the front end. Uh bloody black solder mask. Anyway, we've got the Cypress there and Bob's your uncle. So, there you go. No, the board's not warped. That's my Takano lens there doing that.

**Dave Jones:** So, yeah, cool bananas. Obviously, they're going to position that between the Analog Discovery 3 and the other Analog Discovery uh Pro 3000. And that'll be a lower cost solution.

**Dave Jones:** It's It looks like like almost identical hardware, little bit more fancy pantsy. So, I think the 30 here probably means 30 meg bandwidth. If it is, that's the same as the Analog Discovery 3, isn't it?

**Dave Jones:** So, yeah, more betterer FPGA, but yeah, I don't think you can charge a whole lot extra for it. It's in a nicer case and everything. It's slightly more usable, but you still don't It's not like you get banana plugs or screw terminals or anything for your you know, but there's lots of third-party accessories, lots of third-party accessories for uh you know, plugging into the Analog Discovery um

**Dave Jones:** pinout here. But uh yeah, it's in a more betterer case, but you can't charge a huge amount extra for it, I don't think. But anyway, thank you very much, Digilent, for sending that one in.

**Dave Jones:** It's completely unreleased and sorry, I can't use it at all. But I'll link in my Analog Discovery 3 video down below and I extensively use of software in that and it do lots of weird and wacky things and it's absolutely fantastic and that's really what you're paying for.

**Dave Jones:** You're not necessarily paying although the hardware's quite expensive. These FPGAs, these ADCs and DACs, these really high-speed 14-bit jobbies, these are not cheap. So, you can you can go and try and build your own and and try and buy these chips one-off or even in, you know, medium uh volume or something, lowish volume, and and just try and build your own and you'll find out pretty quick that the hardware, you

**Dave Jones:** know, you can't spin this board out for a 10 bucks. It just doesn't work like that, right? These are really high-performance uh ADCs and DACs and FPGA and everything.

**Dave Jones:** So, rather pricey, but uh yeah, you're you're really the software is where the value is in this thing. And the WaveForms software is just absolutely incredible, so check that out in my Analog Discovery 3 video.

**Dave Jones:** Anyway, if you like that, give it a big thumbs up and as always discuss it down below. Catch you next time.
