---
video_id: tjdae8oqYMQ
title: The Signal Path Discussion - Engineering & RF (3/3)
url: https://www.youtube.com/watch?v=tjdae8oqYMQ
source: youtube-asr
timestamps: {"0": 0, "1": 10, "2": 24, "3": 38, "4": 50, "5": 64, "6": 76, "7": 89, "8": 101, "9": 116, "10": 129, "11": 140, "12": 153, "13": 166, "14": 179, "15": 198, "16": 211, "17": 223, "18": 236, "19": 251, "20": 262, "21": 274, "22": 290, "23": 304, "24": 315, "25": 327, "26": 340, "27": 349, "28": 361, "29": 372, "30": 383, "31": 395, "32": 408, "33": 420, "34": 432, "35": 447, "36": 460, "37": 474, "38": 483, "39": 498, "40": 513, "41": 526, "42": 539, "43": 552, "44": 567, "45": 580, "46": 591, "47": 602, "48": 613, "49": 622, "50": 634, "51": 651, "52": 663, "53": 678, "54": 689, "55": 698, "56": 713, "57": 727, "58": 739, "59": 751, "60": 762, "61": 772, "62": 787, "63": 800, "64": 812, "65": 824, "66": 835, "67": 849, "68": 864, "69": 875, "70": 889, "71": 900, "72": 913, "73": 926, "74": 939, "75": 953, "76": 963, "77": 972, "78": 987}
---

**Dave Jones:** Yeah. So, the other thing I want to talk a little bit about is um some of the the stuff that's happening in in the electronics world that I thought you might you guys might find interesting. So, obviously you all know about Moors

**Dave Jones:** law, right? This is a very very very famous thing there. Yep. For uh for all that stuff, but Moors law in terms of in traditional sense actually is not really going on anymore, right? No. No, it's almost ended. Has it ended, do you

**Dave Jones:** think? Or is it It's It's going to almost a generation away from Yeah. I mean Intel already skipped one generation of their scaling, right? So Mor line is most traditional sense refers to the fact that I can simply

**Dave Jones:** double the computational capacity of something because I can cram more stuff in it at the same space that it was before. But we're hitting those limits. Yeah. So once you hit those limits, then obviously you can't just cram more

**Dave Jones:** transistor and expect things to become better, right? So then you have to change. So now but there is still a morsel going on but at a a layer above. So now the computational capability of systems will continue to grow but not at

**Dave Jones:** but not simply riding the the transistor scaling laws. So it actually how so how does that happen? So it happens by now becomes about a hybrid of the system right so now software combination of software combination of hardware

**Dave Jones:** together and design techniques rather than having access to the next technology it's going to create that and is it packaging techniques as well flip like the double flip chip like the memory on the back of the processor and

**Dave Jones:** all that exactly so now now you got 3D integration and so on and more and more some of that you can even think about some of the uh parallelization of software as forwarding integration because now you're paralyzing in time

**Dave Jones:** anyway things like that. So but yeah that's kind of where it is headed u I mean I don't design microp processors my work is on millimeter wave A6 for you know wireless and optical systems but so even for in my field this Mors law now

**Dave Jones:** refers to the entire capacity of the system not just okay so so it's understood that it applies to a different you have to if you want to continue because all you care about is computational capability if computational capability continues to go

**Dave Jones:** up then you can say that okay we're we're riding that Yeah. Nonetheless, yeah. So, it's interesting to see that this is still going to continue. So, if anyone ever tells you, okay, mors law is dead. Yeah. Okay. Is in one in one

**Dave Jones:** sense. Yes. And there's other thing is that the cost per transistor actually hasn't been going down anymore. No, that's right. So, if you want to do a new fabrication run on a 7 nanometer state of the So, memory is not going to

**Dave Jones:** get any cheaper. No, the cost of that except when they amatize the fab cost and the Yeah. So it depends on scale numbers, right? Not numbers. If if you want to make something only 10,000 of something and you want to put it in the

**Dave Jones:** state of the art, it's going to be it's an init. Just the first time you submit for fabrication, you're looking at a couple million, right? So if you're not selling and selling them by millions is just not the mask cost of production is

**Dave Jones:** just so high that it doesn't make sense. Yeah. Dummy question out of left field. um the RF helter wave stuff that you're working on. Is there an bad analogy but is there like an FPGA equivalent in that sort of field so to

**Dave Jones:** speak? So there you everything have to be totally custom from scratch or can you sort of depends on what you're doing? Depends on what you're doing. So, so if you want to think of in the analogy of the FBJ like you were saying,

**Dave Jones:** so you know this whole softwaredefined radio business, right? Huge, right? The whole Yeah. I mean you you probably know about software defined radio from the little dongles you can buy or things like that. But in reality what software

**Dave Jones:** defined radio in a in a real communication system is is that I can have one box that can work across a wide range of frequencies can interface with a wide range of modulation formats and communication formats and interpret

**Dave Jones:** them. So in theory you could build a system that behaves like an FPG as a hybrid but on a single chip. Has anyone built a software defined radio in that sense? No. No. Maybe some in back radio they built really broadband um radios

**Dave Jones:** that can be but they're not really quite the way you want. You can't just program it and you know do it. I mean right it's more custom made. Yeah. At lower frequencies in the ISM bands. Yes. Like quad band and penta band or whatever all

**Dave Jones:** those things you can do. Once you go into the higher and higher like at 5G the next generation of communication where we're actually going to jump to 28 GHz and 39 GHz carries and that that'll be consumer level. Yeah. It's going to

**Dave Jones:** be everybody and their uncle is working on 5G radio now. So it's going to happen at some point. Is that because that's a more ideal frequency atmospheric wise or is it a regulatory band that's available? How is it regular? So it's a

**Dave Jones:** band allocated to it. So I think I think it's 800 MHz around 20 29 G. Is that available in every country? I think some of them are actually quite international. I'm not sure about uh in Australia but even higher frequencies in

**Dave Jones:** Japan for example above 100 GHz is available if you want to use but things become a lot more difficult. Yeah. So is that I I heard is that atmospheric or is that chip level difficult? Both probably. Oh yeah. I mean it's it's

**Dave Jones:** difficult for a couple of reasons. for example, 28 GHz just doesn't go through your house, especially if it's raining. Uh the attenuation if it's raining is huge. Um and they also want to do a phase array. So they want to do beam

**Dave Jones:** forming in the air so that they target individuals with a beam. And that is a totally different style of communication than broadcast mode that we're used to in cellular networks. So it's going to be completely different. And uh yeah, so

**Dave Jones:** it's I I'd like to see how it's going to play out. But everybody's working on it and obviously Nokia is working on it which is where I work in Bell Labs. But um yeah, everyone knows about it so it's

**Dave Jones:** not a secret but um it's going to be quite difficult and interesting to see. It's going to have to be very inexpensive in order to be com you know competitive with the 4G networks and so right do we have to change our processes

**Dave Jones:** our semiconductor processes to manufacture this sort of stuff? It's all is it like silicon on sapphire? What is it? What's the process? No, it's just any any basic any basic silicon we can do. Yeah. Yeah, if you look at if you

**Dave Jones:** look at the companies who are working on these kind of things, everybody builds them in the technology that they're the expert at, right? So, so if you go to a company that does um let's just say as a

**Dave Jones:** hypothetical, this is this is not an actual example, just take a hypothetical one. Let's say take Qualcomm, right? So Qualcomm does CMOS does builds lots and lots of CMOS chipsets. And so if they were to build, they would build it in

**Dave Jones:** CMOS. They're going to choose COS because that's what their all their libraries are in. That's but I thought there were physical limitations of especially in the RF domain as a substrate material. Uh any any advanced SMOS process that is used for making

**Dave Jones:** microp processors these days is is good enough to make it's good enough to make really you can even go you can even build I thought you had to go really exotic materials. No you don't need to not anymore. So what's the advantage of

**Dave Jones:** the exotic materials like silicon on sapphire? So things like um not just silicon sapphire specifically. That's really exotic. That's almost no I don't think I've ever seen anyone use it. We've got one fab in here in Sydney that

**Dave Jones:** does and they also make really small w and it actually looks really beautiful. You can see right through the wave. Uh but uh so in 35 gallium indium phosphate process the advantage of those processes is the fact that they have they kind of

**Dave Jones:** combine very high speed with very high breakdown voltages. So you can make really high power PAS really really low noise LNAS and things like that. So they'd be used on the front end amplifier front end RF amplifier. Right. Right. But the problem

**Dave Jones:** with them is that they are a very expensive and b is that they they don't offer level of integration. So you can't for example build a microprocessor or a huge with a little bit of silicon. You're going to have to break it up. So

**Dave Jones:** as soon as you want to say I want you to go on a board. Yeah. you're going to either or in a package or something and then then you lose the and also for 35 technologies they have to be

**Dave Jones:** hermetically sealed. So you so moisture is a problem. Moisture and oxygen all this stuff. So you whereas silicon is not silicon can be exposed. So that's a huge it may not seem like much but it's a huge advantage. Even even though some of some

**Dave Jones:** plastic packages are actually not they're not hermetically sealed some kind of a metallic dome over it. Yep. Yeah. So that increases the cost by an enormous amount. So yeah and level of integration I mean that's what silicon does right silicon is on a on a

**Dave Jones:** transistor level on individual transistor level is not the highest performance thing in the world right you can easily beat it with some other technology but it's the integration that gives it the power I'm going to put so much functionality onto it that there's

**Dave Jones:** just you're not going to be able to beat for for example especially for beam forming I cannot make a power amplifier that puts out a watt but I can build a thousand power little power amplifiers and combine power and you will never

**Dave Jones:** beat that with anything in terms of integration and cost eventually. Yeah. So this is no but military uses a lot of 35 use a lot of gamma because the military doesn't care so much about the cost and also they want you know

**Dave Jones:** exceptional performance and things that silicon just simp simply doesn't give you.5 dB noise figure at certain frequ cannot get that. So and also temperature ranges and things like that. But yeah, so they they they is the reason actually

**Dave Jones:** 35 and and gas and so on advanced so much was because the US monetary put so much money into it for their communication. Yeah, that's the other the other thing that's really the military doesn't care about FCC regulations. Right. Right. They can they

**Dave Jones:** can radiate they can do whatever they want whatever power you want and whatever frequency you want and no one cares. So they can jam you. They can do what Yeah. They don't care about that stuff. So that's why it makes it a

**Dave Jones:** little bit easier to design. But if you want to build uh if you want to build something, let's say you want to build a 5G system, it's not enough to make it work at 20 GHz. You also have to make

**Dave Jones:** sure it doesn't emit outside of your band. It doesn't emit anything in other frequency. This is also true for lower frequencies too, which is very difficult to to do, especially when the channels uh like Wi-Fi channels are so close to

**Dave Jones:** each other, of course. Yeah, it's a big deal. Yeah. At at higher frequencies, they're further apart. It relax them a little bit. because otherwise no one would be able to build anything. Yep. Yeah. So that's that's the kind of stuff

**Dave Jones:** that uh is really interesting and exciting and then the packaging like you said and 3D integration and at the system level the optimization then takes you another step forward. Yeah. So I think I mentioned this to you before at

**Dave Jones:** Bell Labs a long time ago there used to be this Bell Labs Shannon lecture series that was a long time ago and they actually restarted now. Nice. And so now we've had three and the first one was about the kind of artificial sensing

**Dave Jones:** with merging materials with the human body and it was very very interesting. The second one which I thought why I personally enjoyed very much was the the head of the artificial intelligence at Facebook was there and he was talking

**Dave Jones:** about AI and neural networks and how they handle information because Facebook receives so much data each day. I mean, and almost an inconceivable amount of data. Not not just text, but photos. Oh, photos and videos. And and what they

**Dave Jones:** need to do is that every video needs every every photo needs to be processed before it shows up. So when you put it, it's actually even though it's real time, it's actually not, right? It gets processed at some superco computer

**Dave Jones:** somewhere and then it comes back and gets posted so that it doesn't have some content that you don't like to have, you know, pornography and so on has to be removed. So but this is not done in a

**Dave Jones:** traditional way. It's done with neural networks and learning system. It's a learning system. It figures out how okay based on other things. It continuously grows, right? It's grows to be smarter and smarter. Uh but it's obviously not nowhere near the the human brain. In

**Dave Jones:** fact, in fact, somebody asked this question. And the the thing that makes the human brain extraordinary is is how much it does with how much power it consumes. Yes. Is the is the computational power, 100 watts or something. And how much it does with

**Dave Jones:** that. It's just such a massive system. such a parallel system and anyway so he's talking about how so neural networks is not like a so take a GPU for example like an Nvidia GPU which by the way is used at the heart of a lot of

**Dave Jones:** neural networks because of its computational capability a GPU that let's say you're watching movie or playing a game it doesn't need to be 100% error-free in fact it's not your GPU makes mistakes all the time it's just that it doesn't matter you don't

**Dave Jones:** care if a pixel isn't rendered right now it doesn't matter you won't even notice it right so in fact some of the higher great Nvidia processors that you can buy for let's say 10 times the cost of a

**Dave Jones:** regular one. The only difference is that it's been tested so it doesn't produce errors. So it's been like kind of handpicked in a way sometimes not not always but some some of them are like that. Interesting. And u so what would

**Dave Jones:** cause those discrepancies by tangent technical questions? Yeah, it's just mistakes in the in the mistakes in the timing or some bit getting flipped somewhere or some error that exists in some Is that because of the but it's not because of the inherent

**Dave Jones:** design architecture otherwise each tip could operate identically. You're are you talking about quantum? No no no I'm not not at that level. No, but so the thing is about the if you look at the architecture of the GPU itself, it's a

**Dave Jones:** massive computational platform and sometimes it it's pushed a little bit beyond how fast it can go. Let's just as an example, right? So if you push it a little bit faster and it's so it's an overclocking. Yeah, it sometimes makes

**Dave Jones:** mistakes here and there and some bits may get flipped here and there and these errors happen all the time in any computational network, right? It's just that sometimes that sometimes it's unacceptable and sometimes there is error correction behind it, right? So a

**Dave Jones:** wireless system can h can have bit error rates in the order of 1 to the minus three right so out of every 1,000 bits is one wrong right which is very very bad right but there's so much error

**Dave Jones:** correction behind the system such that the overall system is error-free or it goes below 1 to 12 so for GPUs uh for example they may not do error correction because they don't care about some bits being flipped here and there and the

**Dave Jones:** point I was making originally was that in neural networks because it's a hurist istic system actually errors aren't catastrophic necessarily right because then the system is constantly learning and constantly correcting as it goes forward and uh so it does it doesn't

**Dave Jones:** have to be perfect I mean your brain makes mistakes all the time right but it doesn't necessarily matter because your eye is not perfect you think you're seeing a perfect image but you're not your brain's inter filling in fact

**Dave Jones:** there's just so many things that go wrong but it's because it's so massively parallel and so much stuff happening all the time it kind of averages out and it turns out as this as the head of the AI person at Facebook was talking about

**Dave Jones:** AI lab is that yeah this this so you can take advantage of that you can take advantage of the the algorithms that go into neural networks the fact that they don't have to be perfect to constantly reduce the power consumption of the

**Dave Jones:** system because you don't need to be so computationally aggressively trying to fix everything it may not matter right so he was saying also that uh in your GPU for example you do 16 point 32 point floating point accuracy

**Dave Jones:** He he was saying that you can get away with four or five. Yeah, exactly. Doesn't matter, right? Because I mean it doesn't make that much of a difference, right? So it floors out very quickly. So he was saying a next generation of uh

**Dave Jones:** DSPs so-called for neural networks don't need to be 16.4. You can get rid of all of that, bring the power down, make the system more efficient. And this is only something we've learned in recent times. Yeah. Because there's Yeah, this is very

**Dave Jones:** very very recent stuff. uh because experiments at that level are just simply not that common. So they're just basically figuring this stuff out. So they realize they went not quite went down the right track. Oh, we're pushing towards more precision, more precision.

**Dave Jones:** And then they find out, oh, we don't actually need a lot of practical purpose. Some scientific applications of course you need rigorous. Yeah. And I don't know for an operating system is a little bit different. For example, when

**Dave Jones:** you have a depth of a memory, you're putting a lot of data in and out. But for neural networks, for example, we can get away with it. So it is really cool to yeah that was really I'm I'm sure I'm

**Dave Jones:** butchering some aspects of it because AI is not my expertise but uh you can actually go and watch that episode it's on Bell Labs Shannon Luminary series if you go on YouTube there on YouTube it's easy to find so go and watch and listen

**Dave Jones:** to this uh this gentleman talk about it he's he's obviously an expert
