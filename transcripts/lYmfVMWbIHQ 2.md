---
video_id: lYmfVMWbIHQ
title: EEVblog #1273 - EMC Near Field vs Far Field Explained
url: https://www.youtube.com/watch?v=lYmfVMWbIHQ
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 32, "3": 42, "4": 55, "5": 67, "6": 79, "7": 92, "8": 107, "9": 123, "10": 137, "11": 155, "12": 171, "13": 187, "14": 201, "15": 214, "16": 230, "17": 245, "18": 255, "19": 272, "20": 283, "21": 296, "22": 308, "23": 322, "24": 335, "25": 349, "26": 362, "27": 380, "28": 394, "29": 409, "30": 423, "31": 436, "32": 451, "33": 465, "34": 479, "35": 494, "36": 507, "37": 522, "38": 533, "39": 548, "40": 566, "41": 579, "42": 592, "43": 604, "44": 619, "45": 636, "46": 651, "47": 665, "48": 679, "49": 696, "50": 708, "51": 726, "52": 743, "53": 761, "54": 776, "55": 792, "56": 807, "57": 825, "58": 837, "59": 854, "60": 870, "61": 887, "62": 903, "63": 917, "64": 936, "65": 952}
---

**Dave Jones:** Hi, I recently needed to find some of my own content actually, which is not quite unusual. I needed to link to it and it turns out it was I wanted my explanation of near field versus far field EMC or electromagnetic

**Dave Jones:** conformity in regards to EMC testing. And what is the difference between near field and far field? It's trying to explain it and as it turns out I've done like four maybe five videos on various aspects of EMC testing emissions and probing near

**Dave Jones:** field probing and stuff like that and it was actually buried away. I had to do some finding. It was buried away inside one of my videos. So I thought I'd just split that out and do a separate video

**Dave Jones:** here. It's mostly recycled content but it'll be better for people trying to find information for near field. What's the difference between near field and far field testing? And as it turns out you you've no doubt seen my previous

**Dave Jones:** videos. If you haven't, I'll link them in all down below. These are near field probes. These are H field or magnetic field probes various different sizes and I've done a video on how you can manufacture your own for

**Dave Jones:** like 10 bucks or less. Although these are like sets of these are pretty cheap these days. I might link some sets down below on AliExpress. You can pick up a whole set. So you can argue it's probably not worth making your own. If

**Dave Jones:** you already got the rigid coax, you can do that and you can make one for like 10 bucks. Really cheap and you get a little preamplifier. You can get those really cheap as well. But anyway, these are near field probes designed to

**Dave Jones:** probe directly onto your PCB. And then you've got your electric field or E field probe like this and there is a huge difference between electric field and magnetic field probes. But when it comes to measuring the far field i.e.

**Dave Jones:** what you get if you send your product away to an EMC test house to be compliance tested versus the various the various CISPR standards or whatever standard you're actually uh testing against for electromagnetic uh conformity, then they're going to test

**Dave Jones:** it in the far field. They don't use near field probes like these. These are only for your own like debugging and pre-compliance troubleshooting and stuff like that. Extremely handy, and you should have them, and you should know how to use them. But, far field testing

**Dave Jones:** is significantly different. And I've now got, tada, a far field probe. Yes, it's a a probe. A far field antenna. Because when your electric fields and magnetic fields combine at a certain distance, information coming shortly, you need an

**Dave Jones:** a regular antenna like this. In fact, this isn't a regular antenna. This is a log-periodic uh design. This one's uh designed for about uh just under 300 MHz up to 1 gig. And unfortunately, the uh CISPR standards that you might generally

**Dave Jones:** uh test against and uh for compliance for product compliance, uh generally might be say 30 MHz up to 1 gig, for example. So, you need a much bigger antenna for this. So, anyway, I do plan on uh using this in some for doing uh

**Dave Jones:** some far field measurements in a future video. So, watch out for that uh eventually. So, the whole idea is that you take your product and you take it to your EMC test house or an open area test site, an OATS, and you wait this on your

**Dave Jones:** table, you power it up, and you put your um far field antenna a certain distance away from it at a certain orientation, and you can rotate your product as well around like this to get the different axes and stuff like that. But, then you

**Dave Jones:** can measure the electromagnetic far field emissions of your product. So, anyway, there is a quite a substantial difference between near field and far field, and it's very important to understand. So, uh if you uh looking at like getting a like a real antenna, for

**Dave Jones:** example, um for uh, far-field testing. Like, they're quite expensive. This is like a $5,000 one, but this will go down to 20 MHz, for example. So, it'll cover that entire, uh, compliance range, uh, pretty much. But, different products have

**Dave Jones:** different compliance standards and different frequency ranges you need to test over and things like that. It's actually quite, uh, complex. So, yeah, if you want to do it properly, of course, you got to go to an EMC, uh,

**Dave Jones:** test house. They will tell you exactly what uh, standards that your particular product for, and they'll test against those particular standards. But, yeah, if anyone knows, um, where you can buy a a a far-field EMC test antenna that goes

**Dave Jones:** down to, say, 30 MHz, please let me know. Cuz I have been trying to find a cheap one, and I cannot do it. This one is only 50 bucks, and I'll link it on AliExpress down below. But, as I said,

**Dave Jones:** it's an order of magnitude higher than what I want. It's about 300 MHz and up. I want to go down to 30 MHz, uh, for your various, uh, basic product, uh, standards. But, of course, the lower the frequency it goes, the physically bigger

**Dave Jones:** antenna you've got. So, this is a log-periodic design, for those who don't know. There's a little SMC connector, um, up here, and the center pin of that, um, goes to one side of this, even though the silkscreen shows both.

**Dave Jones:** There's actually only one PCB trace there, and then it'll alternate the next PCB trace, and then this side, and then that side, and the other side uh, can take is hooked up to the ground of the antenna. So, it'll be the opposite one.

**Dave Jones:** So, the center conductor will be this one here, and then the ground will be this one down here, like this. And, it goes down for the different, uh, wavelengths, like this. So, once you get down to 30 MHz, has to be, you know, you

**Dave Jones:** have to start doing, uh, you know, more convoluted designs, um, something like this, to get those low frequencies. You can see that, uh, this one's got a combination of the log-periodic and, uh, the bowtie approach um, antenna down

**Dave Jones:** there. So, yeah, if anyone knows we can get one of these cheap, um, please let me know. So, I've been able to find the info, but I'll link to this one. It's like 50 Yankee bucks or something on AliExpress. So, I haven't

**Dave Jones:** tried it out yet, but I plan on giving this a whirl to do some far field testing on my new four layer inner conductor outer grounded board. So, that should be interesting, but that's a future video to come within the

**Dave Jones:** next month or two, I guess. It won't be immediate, but I'll eventually get around to doing that. So, herewith is the explanation near field versus far field. Thanks. Catch you next time. And the thing with these H field magnetic probes, and it's

**Dave Jones:** not like an issue with them, in fact, it's a feature is that they are dependent upon the orientation. They work in the plane. So, if you've got your coil like this, it's picking up magnetic fields that are in that flat

**Dave Jones:** plane there. So, you'll notice that if we take this, there's our spectrum, and that that's over 250 MHz, and if we simply rotate that like that, it picks up different components. Look at that. So, you can actually use that

**Dave Jones:** as a feature using a smaller diameter one, you can get down there, and you can trace down your offending components and traces better. Things like that. So, I I'll probably have to do a a whole separate video on this, but

**Dave Jones:** yeah, it does make a difference, the orientation. I've seen quite a significant difference here between the four layer and the two layer board. Makes a heck of a difference. Like typically like broadband noise in this particular case about, you know, 15 dB

**Dave Jones:** or so, and that's a lot. But does that translate if you measure say a 15 dB difference here, does it actually with your near field probes, does that actually translate to a 15 dB difference on your EMC testing when you put it through the

**Dave Jones:** test house and you test it against the compliance standard. Well, the answer is unfortunately not. These near field probes, both the H field magnetic field and the electric E field probes, all this is as I said the near

**Dave Jones:** field. Whereas all of the compliance testing is done in the far field and I'll explain that in a minute because I have a Dave Cad. So, what's the point of using these near field probes if they're not sort of like quantitatively

**Dave Jones:** equivalent to what they do in the test house? Well, the good thing about it is that at the design stage or maybe if you fail compliance or something or you need to or you're doing some pre-compliance testing you can go around your board and

**Dave Jones:** sniff all around your board with the H field and the E field probe to see if there's any issues, see if there you know, anything's radiating wildly and stuff like that. You can you might be able to see a big spike or something at one

**Dave Jones:** particular frequency. You might go, "Oh, we need to knock that down." Even though you don't even though you it might be compliant at the design stage you might go, "Well, you know, I'm not going to take any chances and I'm going to knock

**Dave Jones:** that problem on the head now before I send it across to the test house." So, we'll briefly talk about near field and far field here and how it relates to the electromagnetic radiation. Now, a you might have heard the term

**Dave Jones:** electromagnetic radiation. It's electro and magnetic contains electric and magnetic components and you can look at it. This is like the standard visual representation of it. The electrical field might like would go up in the Z axis like this and the H field is 90°

**Dave Jones:** from that. So, they actually propagate in different orientations and of course this is the wavelength and here's a cute little animation just to show you how that works as it propagates down. Now, what we actually have to look

**Dave Jones:** at though is what's called the wave impedance. And this is where the difference between near field is everything on this side and far field is everything on this side. Now, the wave impedance in ohms like this in the for

**Dave Jones:** this particular scale, please excuse the crudity, didn't have time to build the scale or to paint it, from 10 ohms to 10,000 here. So, this is where you have to define far field and near field. Well, the electric field and the

**Dave Jones:** magnetic or H field, there is a difference between H and B by the way. B is flux density. You might sometimes be hear it called B, but it's actually H magnetic field as opposed to induced magnetic field as

**Dave Jones:** opposed to magnetic flux density. Anyway, won't go into the details. So, the H or magnetic field actually has a very low impedance source in the near field, whereas the electric or E field has a very high impedance. I'll clarify that in a minute. But

**Dave Jones:** basically, it all comes down to the wavelength lambda here and this is normalized to one here and it's lambda on 2 pi, which is basically we're we're going to normalize to that value. And of course, let's take for example 100 MHz

**Dave Jones:** is a wavelength of 3 m. So, pi on 2, that's about a half meter. So, when you get to a half meter away from your product, this is where the electric fields and the magnetic field actually start to converge. It's not really clean

**Dave Jones:** like this. There's a bit of you know, overlap in here and this is like the transition. There's going to be like a transition region in here where the two fields eventually combine and anything over roughly half a meter away

**Dave Jones:** at 100 MHz, the electric and magnetic fields combine to give you a singular impedance, which actually happens to be 377 ohms in free air. So, anything over the wavelength on 2 pi is deemed to be the far field and anything

**Dave Jones:** closer physically closer than that like we just did with our probes here is the near field. Now, this is why we have two different types of probes. One is the H field probe, the magnetic probe, the other is the E field or electric field

**Dave Jones:** probe and the magnetic or H field is going to be generated by higher currents, i.e. sources that have a very a lower impedance. So, for example, if you've got a lot of current flowing in a in a particular trace either due to an

**Dave Jones:** actual like heavy current switching or even very fast switching that's dumping a lot of energy into the bypass capacitors and the capacitance between the power planes and everything else, then that's generating typically be generating a magnetic field due to the

**Dave Jones:** low impedance and the high current. But, very high impedance things that don't generate lots of current, then they generate electric fields and hence the bigger source impedance. So, you can generate electric fields from say just like a static power supply for example,

**Dave Jones:** your 5-V power supply. Whereas all your switching stuff will dominate down in the H field here because there's lots of current being dumped into the trace or the load capacitance or the particular load itself when you're switching things. So, that's why you

**Dave Jones:** need to use these two different probes and the magnetic field probes, they are sensitive to orientation like this and like that as well as I talked about on the plane. Whereas the electric field is not sensitive. You can just put that in

**Dave Jones:** any orientation and it's not going to make a difference. So, if I use my E field probe like this and let's say I probe this power trace over here like this, you can see it's really not going to make any difference the orientation

**Dave Jones:** that I put that in. It's just completely insensitive to that because there's no magnetic field coupling. It's electric field coupling and it's just purely the distance. But if you take a magnetic loop probe like this and I just change the orientation like

**Dave Jones:** that, wow, that makes a big difference. It really brings out the peaks if I put it vertically like that. If I put it horizontal, it gets more of the current flowing through the trace. And if we use our

**Dave Jones:** smallest H-field probe, let's just have a look at let's say this like blank area over here. This is our four-layer board like this or maybe right over on the edge of the corner of the board right over here like this and let's compare

**Dave Jones:** that with our two-layer board here. Bingo, look at that. Because we've actually got a power trace actually running right around this corner as well, which we actually physically remove. And you can actually see that the power trace actually running all the

**Dave Jones:** way around there like that. So, that's just going to radiate like buggery. But even if we go over just the ground plane there, you can see it's much much higher than we get with the four-layer board. And this is why at the EMC test house

**Dave Jones:** they'll test in the far field here cuz it binds the electric and magnetic fields together. And basically the typical testing distances would be like a 1 m, 3 m, 5 m, 10 m for example away. It depends on the type of product

**Dave Jones:** they're testing and to which standard they're actually testing to. But say if you put it 10 m away, then you can have a larger rotating turntable so that your product rotates around like this on the turntable and they can measure all the

**Dave Jones:** axes like this when they while they have their super expensive, you know, bi-conical um super calibrated measurement antenna 10 m away measuring over, say, 30 MHz to 10 GHz far field, for example, might be a typical measurement range. And then there'll be

**Dave Jones:** standard like envelopes that you have to get under and also peaks and things like that. And it gets, you know, the standard gets quite complicated, but yeah, just the near field testing that we do here doesn't really translate to

**Dave Jones:** the far field, but you can certainly get an indication of whether or not you've got any nasties on your board.
