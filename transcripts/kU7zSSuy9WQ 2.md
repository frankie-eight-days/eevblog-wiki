---
video_id: kU7zSSuy9WQ
title: How to ID a Mystery Microcontroller
url: https://www.youtube.com/watch?v=kU7zSSuy9WQ
source: youtube-asr
timestamps: {"0": 0, "1": 34, "2": 68, "3": 81, "4": 102, "5": 118, "6": 147, "7": 177, "8": 196, "9": 225, "10": 258, "11": 280, "12": 305, "13": 335, "14": 354, "15": 382, "16": 399, "17": 432, "18": 459, "19": 491, "20": 520, "21": 551, "22": 566, "23": 605, "24": 632, "25": 655, "26": 675, "27": 693, "28": 718, "29": 755, "30": 785, "31": 817, "32": 851, "33": 880, "34": 900, "35": 933, "36": 966, "37": 1000, "38": 1029, "39": 1047, "40": 1079, "41": 1105, "42": 1124, "43": 1150, "44": 1171, "45": 1196, "46": 1224, "47": 1242, "48": 1272, "49": 1307, "50": 1333, "51": 1364, "52": 1378}
---

**Dave Jones:** Hi, just a quick second channel video which is a follow up to my main channel one on the ANENG socket tester teardown. And here's the PCB in it with this chippity do dah here, this chip on board. It's a bare die under there. And how I found out that this thing was actually an SD7500 multimeter chipset. And when I originally, when I first tore it down, I thought maybe before I tore it down, I thought "Oh, it's just using, you know, a little micro in there or something,

**Dave Jones:** little mixed signal micro to do the measurement." No, it's actually a multi- dedicated multimeter chipset which with hindsight makes absolute sense. But at the time, you know, I was in the "Ah, it's just a micro." Right? I didn't think about multimeter chipset. So, how did we work out that this is an SD7500 here? Well, let's go through a bit of the process cuz I spent a little bit of time not didn't spend hours, but I spent maybe 30 minutes around trying to find the chip. But it actually

**Dave Jones:** in the end it was found by a viewer of well, a somebody on Twitter. So, I'll show you that in a minute. Thank you very much cuz I actually came up empty-handed on this. But let's just go through the process.

**Dave Jones:** Now, of course, what we're looking at here is I we know it's a 44-pin chip, right? So, the chip isn't actually connected to these pads, but there's some other pads inside which then there's a bare die in there. It's probably only, you know, that big. It's probably only tiny, right? And then they'll have little bond wires going out. They use a little bonding machine.

**Dave Jones:** And you might think that's expensive, but you know, you can any like decent assembly house can, you know, actually do that for you. They can do bare dies. And any semiconductor company will sell you a bare die. And it can actually be cost, you know, you might save a few cents or whatever.

**Dave Jones:** And on a product like this, really low-cost product, you are saving, you know, saving a few cents matters when you're making, you know, 100,000 of these things or what however many they make. Probably not that much, but anyway. Um so, yeah. So, we know that almost certainly the bare die in there is going to be um or they might have a like a smaller footprint in there. Uh for example, that was compatible with a smaller footprint version of the chip perhaps. Uh but I believe but because

**Dave Jones:** it's uh it's being gunked like this, it's going to be a bare die. And these bond them over. So, it should be the same pinout, okay? So, this is obviously here's the silkscreen marker up here. So, this is obviously pin one. Okay? So, we know it's a 44-pin chip, okay? And but of course, microcontrollers and other sorts of things, they often come in various uh package like the same type will come in different packages with different pin configurations and stuff like that. So, that confuses uh things

**Dave Jones:** as well. But what do we know, okay? We've got these test pads here, okay? So, we've got uh VPP here, okay? And that's the one I pointed out in the video, but we've also got four test pads over here. So, we know that VPP is on pin one. Okay? Cuz we can physically see it going into there into that cap there.

**Dave Jones:** So, this is pin one. It always goes around uh anticlockwise like that. Um so, we know that's pin one and it's a 44-pin chip. And then it's got a uh other programming uh pins here, which is 44, 42, you know, 40, 39, etc. Stuff like that. Okay? And I thought before I actually uh reverse engineered this schematic uh for this, I thought pin 12 down here was actually ground. I thought that was actually ground, but it's not.

**Dave Jones:** It turns out that's the com uh chip that's the com terminal here of the multimedia chipset, which is not ground over here. But anyway, getting ahead of myself. Um now, what else have we got? We've got right there. That's pretty much the only information we can glean. And at the time, I didn't know that I think pin two is ground and pin three is VDD. No, I think pin three is VDD and pin two is ground there. But I didn't know that at the time cuz I hadn't reverse engineered

**Dave Jones:** uh this. And you probably don't have to uh those. So, anyway, let's go. Right, so we're searching for VPP pin one. So, the first thing I thought was okay, could be like a PIC micro. I know some of the older school PIC micros have VPP on pin one and on pin one. That's just from rusty old Dave at memory here. And I believe that's that's the actual case.

**Dave Jones:** Right, so I'd go over to Microchip over here, right? And then I'd search for I'd put I'd use the parametric search tool. Okay, I won't go in I've done I've done videos on how to do parametric searches and stuff like that. So, I won't go through all the details. I want this video to be not 1 hour long. But I searched for what is it 44-pin packages? Are they Are they here somewhere?

**Dave Jones:** I did search for package type. Anyway, I'm sure I did. Maximum speed. Hang on. Is there No, there's not a bar that goes across there. Why is there no bar at the bottom? Oh yeah, there it is. Okay. Right. So, yeah, anyway, I searched for like 44-pin packages and these are the ones that I came up. So, you know, I went and had a look at a couple of data sheets like this and pin one VPP wasn't a thing, right? And then I had a look at some like some Atmel

**Dave Jones:** variants PIC own Atmel AVR now. So, I thought maybe it's an AVR or something like that. And I didn't get lucky on pin one VPP. So, you know, I kept going. Then I thought, "Okay, if this is a real low-cost product." So, like it costs like 10, 15 bucks or something, right?

**Dave Jones:** It's really low-cost product and it's so it's probably going to use one of these Asian source micros, right? So, it's not going to use one of the like the biggies like your you know your microchips or your Atmel's or your ST's or something like that. It's more likely to use maybe some obscure 8051 variant, you know, some right? So, I thought, "Oh, maybe it's like a high con or something." So, I went into high con and once again, I had a look at you know just some random

**Dave Jones:** high con chips here and I downloaded some Yeah, I got some data sheets for those and none of them matched up, okay? So, at this point like you can go into Digi-Key Oh. No, sorry. All my links are All my links are wrong.

**Dave Jones:** So, anyway, so then I thought like you could go a parametric searching in Digi-Key or Mouser, for example, and then like Okay. Digi-Key Digi-Key I know how to spell, right? Digi-Key Come on, right? And then you can go micro controller and then you can do if if you don't know brands, this is a good way to do it, right? You can go into microcontrollers here. Okay? And come on, you can do it.

**Dave Jones:** Into web is slow today, okay? And it gives you all the manufacturers down here, okay? These are all like your Western ones. So, you won't get any of your Asian source ones. But if you don't you know if you're trying to figure out what this chip is, okay? Then you can actually narrow this down and then of course, you can go over to here package type, right? And you can go over here, you can sort by number of pins. So, you can go 44. So, you would just select all

**Dave Jones:** the 44s, right? Is it a TQFP? Is it a QFP? Uh T instead of instead of in in front of the TQFP stands for thin. So, it's a thin quad flat pack, uh for example. But, anyway, right? Exposed pads, they might even have like bare dies, right? So, you'd select all the 44-pin micros there, right? There's 5,000. There's almost 5,200 of these suckers, right? So, you can apply that and then you can go okay, these are all, you know, it's not going to be AMD.

**Dave Jones:** And like Analog Devices, it's not going to be any of that, but you know, here's some like Western manufacturers. It's not going to be a Xilinx, um NXP, probably not, all right? Motorola, probably not. Um for like one of these Asian products, more likely one of these Asian-sourced parts, right? So, you're not really going to find anything on Digi-Key or Mouser, apart from giving you some, you know, some supplier names and stuff like that. And you might, you know, convenient links to data sheets, uh for example. So, you can go uh open

**Dave Jones:** them real easy and check them out. But, unfortunately, there's no way to sort of like um search for like pin one VPP here, unfortunately, right? So, anyway, another way, so if you think, "Oh, maybe it's an Asian-sourced micro." You'd go to someone like LCSC, which is the Asian equivalent of Digi-Key and Mouser and Element14 and uh your catalog suppliers, uh basically. And um once again, like you can search for packages down here.

**Dave Jones:** Can you search for pin count? Sorry, I can't remember. I did this quite a few days ago. I'm just shooting this video now. And uh yeah. Here we go. Come on, you can do it. Package, no. Program size, no.

**Dave Jones:** No. Can't search for package. That's annoying. Maybe you can search for GP, you know, you can narrow it down using the GPIO, uh for example, which should be like two less uh usually on uh you know good micro two or four pins less than what you need. So, you might go say 38 40 IOs or something like that. Anyway, I don't think they uh package. No, okay. So, silly me, right? LQFP. But once again, they don't sort it by pin number. They sort it by type. So, if you want TQFP, it's not as

**Dave Jones:** convenient as the DGK one that we actually did before, right? So, a TQFN and you know, so you'd have to go through and select quite a few of them. But you can go in there and you can apply and then they've got different sizes as well. That's 7 by 7 is 7 mm by 7 mm package. So, I haven't measured like the size of this thing, but you wouldn't, right? You wouldn't bother going to that sort of detail. But anyway, you can go in there and analog

**Dave Jones:** devices Maxim. Let's go back out there for the 7 by 7, right? And then we get Hang on. No. Oh, bugger. No. How do I unapply? Anyway, here's all the manufacturers, right? So, here's all a ton of different ones that you wouldn't get from there.

**Dave Jones:** But anyway, as it so happens, cut a long story short, right? I use some LCSC's and I was looking at various chips. So, I was looking at this one here, whatever this one is, right? It's a slow for loading. So, I was just looking at various Asian ones, right? Seeing if I could get lucky and stuff like that.

**Dave Jones:** And no, no, I couldn't. And really the only information we had is VPP on pin one. But there is more information here which I totally missed. See if you can see it, right? There's more information here. I'll tell you about that in a minute. But I I did totally totally miss it. So, whoop.

**Dave Jones:** Where's my mouse pointer gone? It's gone. Turn it off, then on again. Okay, I got a fresh battery and we're back. Okay? So, yeah, I was looking through, um you know, various micros, right? I couldn't really find anything and then I decided, ah, come on, it's 2024. Let's use chat GPT, shall we?

**Dave Jones:** So, I actually used chat GPT-4, okay? And I went, find a microcontroller in a 44-pin package that has pin one as VPP. I had no idea if this would work, right? But it actually it it gave me a few hints, right? And it goes, you can consider microcontrollers from the PIC18Q24 and PIC18Q71 families by Microchip. These processors uh and they are available in 44-pin packages and include a pin designated as MCLR/VPP, right? So, it actually knows. This is really interesting stuff, right? The pin says multiple functions programming

**Dave Jones:** voltage, blah blah blah blah, right? And but it didn't necessarily tie pin one on there, right? So, you know, but I hadn't considered those PICs before. I'd looked at a few PICs based on the parametric search and those ones didn't actually uh turn up, right? And so, I said to it again, VPP on pin 18 on these chips cuz I actually went in and checked. Um I need I My grammar's poor there. In on pin 18 is on pin 18 on these chips. I need VPP to be on pin one. Try again,

**Dave Jones:** please, AI. And sure enough, it goes, finding a microcontroller with VPP on pin one in a 44-pin package is quite specific, but it knows. This is really quite amazing, right? And based on the information available, there are certain PIC microcontrollers where the MCLR/VPP pin one is typically pin one. So, it's focusing on PICs again. It hasn't sort of reevaluated its search, I don't think. But sure enough, um for instance, modern PIC microcontrollers, which is used for programming, is is often assigned to pin one. This is a common

**Dave Jones:** configuration for PICs as indicated in this and then it gives you, right? And then it gives you this reference here. And this is where it was scraping its you know, it trained its data on understanding um right, in-circuit programming. So, VPP yeah, is and and that's where it's gotten on VPP is the programming PICs either programming mode when 13 volts are placed, usually pin one on modern PICs, right? So, that's where it was getting that information from. Isn't that interesting? Unfortunately, um it didn't help. Um even though I gave one

**Dave Jones:** example of a 16F877, uh however, it's important to note that particular model is a 40-pin microcontroller, not 44. Um is important to check its data sheet and I went in and checked the data sheet and I've used that PIC before and it's not the 18 uh seven no, pin one is not VPP there, okay? So, yeah, a bit still, you know, it it did an okay job at least leading me in the right and you know, at least keeping me on track and giving me some

**Dave Jones:** things to look in it would be Anyway, it says it would be best to consult the data sheets. Yeah, yeah, well, that's what I was trying to do. I was hoping that uh it could bypass it. Anyway, so what is um PIC right. Bloody ads. Um so, what is the trick? Well, in the end, I sort of like gave up at this point.

**Dave Jones:** And so, I put it on uh Twitter. Can anyone find this? And remember, have you seen Do you notice any more information there than what we had than what I was giving you VPP on pin one? It's obvious, but but I totally missed it. I totally missed it. So, I put it on uh the um So, I put it on uh X here Twitter and I asked if anyone knows and then people threw a few things at me but the winner winner chicken dinner was Bas Stewart

**Dave Jones:** at info exchange info sec exchange and he said it's an SDIC SD7500 on pin one looks to be a multimeter system on chip which is right up your street and bang on. So thank you very much. That's how I actually found thanks to Bas Stewart here. Um and then he goes how he found it was it was the second link on Google for the search terms QFP44 VPP and P54 with file type P PDF and I totally missed it. I like YP54 and then after I

**Dave Jones:** typed that it dawned on me what it actually was is P54 up here. I just my mind sort of just went that's a component designator for the capacitor or the resistor above it. And like maybe like I was viewing it at lower res and looked like an R54 instead of a P54 maybe and my mind just totally skipped that as a P54 next to that pad. So yeah I I totally missed it. So we actually have two pieces of information there. As it turns out the ground down

**Dave Jones:** here on pin what I thought was pin 12 that's a complete furphy. So you know if you started searching for that you would come a cropper but I was searching the only information I had was VPP on pin one and it's a 44 pin chip and it's some sort of microcontroller which a multimeter chipset is a microcontroller but it just contains all the analog multi plexes and the dual slope ADC and everything else required for multimeter functionality of course but that's some extra information. So I actually tried

**Dave Jones:** that exact he said it was the second search term he got. So I tried QFP44 or you could do TQFP haven't actually tried that. Um and he said it was the second search term, but that's not. It gives you an e-land electronics corp one. I haven't even looked at that, but it's not there.

**Dave Jones:** So, that that 7500 is not there. So, let's try that again with TQFP. So, I'm not sure uh TQFP44. Yeah. So, I'm not sure here how he found it. No. No, that doesn't give anything at all. So, I got no idea how that popped up on Google for him. If you got any idea how how it worked, let us know. Try it. See if it pops up for you, but I don't get it. Anyway, it said it you know, like you can put like plus in front and you can put plus in front

**Dave Jones:** like that if you want to, you know, it has to specifically um like have those that string plus that string in there. And um no. So, what's this um EM uh 8-bit microcontroller e-land corporation. Let's go down. VPP boom uh Give us the pin.

**Dave Jones:** Pin number 15. No. See, it's not uh it's sorry, 44. Pin number 14. No. No. So, let's come and get some. So, I'm not sure how he found it. I'm not sure why it showed up in his Google search and it does not show up on mine, but anyway, he found it. Um winner winner chicken dinner.

**Dave Jones:** So, yes, specifically put in that information P54. But uh it looks like like yeah, he used the right mentality. Searching like this is the right mentality using the information. If I knew I had uh that P54, if I had noticed that in the image, I certainly would have started searching for that and I would have started doing strings like this VPPP54 or stuff like that, right? But uh yeah.

**Dave Jones:** Anyway, it did show up. Doesn't show up for me. Don't know why, but then you like you can leave off the file type and you don't want to specifically search for that and still still not there. Still not there. Still pulling up data and PDF data sheets, but not not it just ain't there.

**Dave Jones:** Right? But anyway, somehow he got lucky and that's how I found it. So, thank you very much uh about Stewart um on Twitter for finding that. Otherwise, it wouldn't have been a nearly as interesting a video cuz I was, you know, after spending like 30 minutes around trying to find things I went, "Uh it's not worth the extra effort." kind of thing. I sort of gave up, put it on Twitter hoping for some Hail Mary and uh he's the only one who came up with it.

**Dave Jones:** So, there you go. But that it's this video's about the techniques you use, right? So, you can use your industry knowledge to guess on some manufacturers. Maybe you've, you know, you know this company that manufactures this uh has used this particular microcontroller before and usually a lot of companies like to stick to the one type of microcontroller. So, if they've got one particular type in another product, you might go, "Aha. I'll, you know, search that uh first." But I knew that PICs had VPP on pin one and there

**Dave Jones:** are some older um DIP PIC parts which have VPP on pin one, I believe. Um so, yeah, that was the first place. Then I went into a catalog uh supplier like Digi-Key, for example, or and what Digi-Key? We had the search here.

**Dave Jones:** Anyway, you saw the parametric uh search before and um that can give you other manufacturer names. And then if you want some Asian names, you go to an Asian source uh catalog supplier like LCSC. They're really uh quite good even though the packages here are a bit trickier to actually select 44. You'd have to go through and select all the different variants of 44. So, you'd have to go 44 WQFN, then you'd have to go, you know, go up just keep going to find all the 44s and

**Dave Jones:** then you do control shift and you include those, right? One's coming up. Surely No, 45. Oh, no. And come on, you can do it. All right, anyway, you'll eventually hit upon other 44s. 40 48. And you'll eventually hit upon them and you can see it's a very long list, right? And then you can do just stick control shift and then you select multiple ones like that and then you apply and then it narrows it down, right? To 117 parts down here, I believe. There you go. And then it can

**Dave Jones:** give you All right, once again, we're back at pick again, sort of focusing on that. And but it can give you a list of manufacturers, especially Asian manufacturers that you wouldn't have thought of, like not many people have heard of Hi-Con, uh, tech, for example. And the ultimately ultimately the, uh, 7500 D7500 and PDF is from ST Micro.

**Dave Jones:** And it's a multimeter chipset. Boom! And there it is, right? And we had VPP, there it is, VPP on pin one. Turns out pin two is VDD, pin three is VSS, pin 12 is the com, uh, terminal which hooks up to the common of your multimeter and it's it's the absolute perfect chip for this sort of application, um, which is that little socket tester with an LCD that just measures, uh, mains voltages and whatnot. So, yeah. Yeah, absolutely perfect thing to have and it's even got

**Dave Jones:** the non-contact voltage circuit in it. Anyway, did that as part of my video, so there you go. That's how I found it. Um, I I In the end, I didn't find it. It was found by, uh, bar steward, so thank you very much on the Twitters.

**Dave Jones:** There you go. Hope you found that interesting. If you did, please give it a big thumbs up. As always, discuss down below. Catch you next time.
