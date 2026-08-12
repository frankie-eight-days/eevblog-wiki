---
video_id: lYmfVMWbIHQ
title: EEVblog #1273 - EMC Near Field vs Far Field Explained
url: https://www.youtube.com/watch?v=lYmfVMWbIHQ
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 34, "3": 47, "4": 56, "5": 67, "6": 78, "7": 87, "8": 101, "9": 123, "10": 135, "11": 155, "12": 179, "13": 189, "14": 211, "15": 224, "16": 239, "17": 248, "18": 262, "19": 276, "20": 287, "21": 296, "22": 308, "23": 320, "24": 331, "25": 340, "26": 354, "27": 373, "28": 384, "29": 399, "30": 417, "31": 430, "32": 444, "33": 467, "34": 479, "35": 497, "36": 518, "37": 538, "38": 555, "39": 566, "40": 577, "41": 588, "42": 597, "43": 606, "44": 621, "45": 634, "46": 645, "47": 663, "48": 687, "49": 700, "50": 713, "51": 743, "52": 761, "53": 775, "54": 787, "55": 807, "56": 828, "57": 843, "58": 856, "59": 870, "60": 883, "61": 901, "62": 928, "63": 942}
---

**Dave Jones:** Hi, I recently needed to find some of my own content actually, which is not quite unusual. I needed to link to it and it turns out it was I wanted my explanation of near field versus far field EMC or electromagnetic conformity in regards to EMC testing.

**Dave Jones:** And what is the difference between near field and far field? It's trying to explain it and as it turns out I've done like four maybe five videos on various aspects of EMC testing emissions and probing near field probing and stuff like that and it was actually buried away.

**Dave Jones:** I had to do some finding. It was buried away inside one of my videos. So I thought I'd just split that out and do a separate video here. It's mostly recycled content but it'll be better for people trying to find information for near field.

**Dave Jones:** What's the difference between near field and far field testing? And as it turns out you you've no doubt seen my previous videos. If you haven't, I'll link them in all down below.

**Dave Jones:** These are near field probes. These are H field or magnetic field probes various different sizes and I've done a video on how you can manufacture your own for like 10 bucks or less.

**Dave Jones:** Although these are like sets of these are pretty cheap these days. I might link some sets down below on AliExpress. You can pick up a whole set. So you can argue it's probably not worth making your own.

**Dave Jones:** If you already got the rigid coax, you can do that and you can make one for like 10 bucks. Really cheap and you get a little preamplifier. You can get those really cheap as well.

**Dave Jones:** But anyway, these are near field probes designed to probe directly onto your PCB. And then you've got your electric field or E field probe like this and there is a huge difference between electric field and magnetic field probes.

**Dave Jones:** But when it comes to measuring the far field i.e. what you get if you send your product away to an EMC test house to be compliance tested versus the various the various CISPR standards or whatever standard you're actually uh testing against for electromagnetic uh conformity, then they're going to test it in the far field.

**Dave Jones:** They don't use near field probes like these. These are only for your own like debugging and pre-compliance troubleshooting and stuff like that. Extremely handy, and you should have them, and you should know how to use them.

**Dave Jones:** But, far field testing is significantly different. And I've now got, tada, a far field probe. Yes, it's a a probe. A far field antenna. Because when your electric fields and magnetic fields combine at a certain distance, information coming shortly, you need an a regular antenna like this.

**Dave Jones:** In fact, this isn't a regular antenna. This is a log-periodic uh design. This one's uh designed for about uh just under 300 MHz up to 1 gig. And unfortunately, the uh CISPR standards that you might generally uh test against and uh for compliance for product compliance, uh generally might be say 30 MHz up to 1 gig, for example.

**Dave Jones:** So, you need a much bigger antenna for this. So, anyway, I do plan on uh using this in some for doing uh some far field measurements in a future video.

**Dave Jones:** So, watch out for that uh eventually. So, the whole idea is that you take your product and you take it to your EMC test house or an open area test site, an OATS, and you wait this on your table, you power it up, and you put your um far field antenna a certain distance away from it at a certain orientation, and you can rotate your product as well

**Dave Jones:** around like this to get the different axes and stuff like that. But, then you can measure the electromagnetic far field emissions of your product. So, anyway, there is a quite a substantial difference between near field and far field, and it's very important to understand.

**Dave Jones:** So, uh if you uh looking at like getting a like a real antenna, for example, um for uh, far-field testing. Like, they're quite expensive. This is like a $5,000 one, but this will go down to 20 MHz, for example.

**Dave Jones:** So, it'll cover that entire, uh, compliance range, uh, pretty much. But, different products have different compliance standards and different frequency ranges you need to test over and things like that.

**Dave Jones:** It's actually quite, uh, complex. So, yeah, if you want to do it properly, of course, you got to go to an EMC, uh, test house. They will tell you exactly what uh, standards that your particular product for, and they'll test against those particular standards.

**Dave Jones:** But, yeah, if anyone knows, um, where you can buy a a a far-field EMC test antenna that goes down to, say, 30 MHz, please let me know. Cuz I have been trying to find a cheap one, and I cannot do it.

**Dave Jones:** This one is only 50 bucks, and I'll link it on AliExpress down below. But, as I said, it's an order of magnitude higher than what I want. It's about 300 MHz and up.

**Dave Jones:** I want to go down to 30 MHz, uh, for your various, uh, basic product, uh, standards. But, of course, the lower the frequency it goes, the physically bigger antenna you've got.

**Dave Jones:** So, this is a log-periodic design, for those who don't know. There's a little SMC connector, um, up here, and the center pin of that, um, goes to one side of this, even though the silkscreen shows both.

**Dave Jones:** There's actually only one PCB trace there, and then it'll alternate the next PCB trace, and then this side, and then that side, and the other side uh, can take is hooked up to the ground of the antenna.

**Dave Jones:** So, it'll be the opposite one. So, the center conductor will be this one here, and then the ground will be this one down here, like this. And, it goes down for the different, uh, wavelengths, like this.

**Dave Jones:** So, once you get down to 30 MHz, has to be, you know, you have to start doing, uh, you know, more convoluted designs, um, something like this, to get those low frequencies.

**Dave Jones:** You can see that, uh, this one's got a combination of the log-periodic and, uh, the bowtie approach um, antenna down there. So, yeah, if anyone knows we can get one of these cheap, um, please let me know.

**Dave Jones:** So, I've been able to find the info, but I'll link to this one. It's like 50 Yankee bucks or something on AliExpress. So, I haven't tried it out yet, but I plan on giving this a whirl to do some far field testing on my new four layer inner conductor outer grounded board.

**Dave Jones:** So, that should be interesting, but that's a future video to come within the next month or two, I guess. It won't be immediate, but I'll eventually get around to doing that.

**Dave Jones:** So, herewith is the explanation near field versus far field. Thanks. Catch you next time. And the thing with these H field magnetic probes, and it's not like an issue with them, in fact, it's a feature is that they are dependent upon the orientation.

**Dave Jones:** They work in the plane. So, if you've got your coil like this, it's picking up magnetic fields that are in that flat plane there. So, you'll notice that if we take this, there's our spectrum, and that that's over 250 MHz, and if we simply rotate that like that, it picks up different components.

**Dave Jones:** Look at that. So, you can actually use that as a feature using a smaller diameter one, you can get down there, and you can trace down your offending components and traces better.

**Dave Jones:** Things like that. So, I I'll probably have to do a a whole separate video on this, but yeah, it does make a difference, the orientation. I've seen quite a significant difference here between the four layer and the two layer board.

**Dave Jones:** Makes a heck of a difference. Like typically like broadband noise in this particular case about, you know, 15 dB or so, and that's a lot. But does that translate if you measure say a 15 dB difference here, does it actually with your near field probes, does that actually translate to a 15 dB difference on your EMC testing when you put it through the test house and you test it against the

**Dave Jones:** compliance standard. Well, the answer is unfortunately not. These near field probes, both the H field magnetic field and the electric E field probes, all this is as I said the near field.

**Dave Jones:** Whereas all of the compliance testing is done in the far field and I'll explain that in a minute because I have a Dave Cad. So, what's the point of using these near field probes if they're not sort of like quantitatively equivalent to what they do in the test house?

**Dave Jones:** Well, the good thing about it is that at the design stage or maybe if you fail compliance or something or you need to or you're doing some pre-compliance testing you can go around your board and sniff all around your board with the H field and the E field probe to see if there's any issues, see if there you know, anything's radiating wildly and stuff like that.

**Dave Jones:** You can you might be able to see a big spike or something at one particular frequency. You might go, "Oh, we need to knock that down." Even though you don't even though you it might be compliant at the design stage you might go, "Well, you know, I'm not going to take any chances and I'm going to knock that problem on the head now before I send it across to the test house." So,

**Dave Jones:** we'll briefly talk about near field and far field here and how it relates to the electromagnetic radiation. Now, a you might have heard the term electromagnetic radiation. It's electro and magnetic contains electric and magnetic components and you can look at it.

**Dave Jones:** This is like the standard visual representation of it. The electrical field might like would go up in the Z axis like this and the H field is 90° from that.

**Dave Jones:** So, they actually propagate in different orientations and of course this is the wavelength and here's a cute little animation just to show you how that works as it propagates down.

**Dave Jones:** Now, what we actually have to look at though is what's called the wave impedance. And this is where the difference between near field is everything on this side and far field is everything on this side.

**Dave Jones:** Now, the wave impedance in ohms like this in the for this particular scale, please excuse the crudity, didn't have time to build the scale or to paint it, from 10 ohms to 10,000 here.

**Dave Jones:** So, this is where you have to define far field and near field. Well, the electric field and the magnetic or H field, there is a difference between H and B by the way.

**Dave Jones:** B is flux density. You might sometimes be hear it called B, but it's actually H magnetic field as opposed to induced magnetic field as opposed to magnetic flux density.

**Dave Jones:** Anyway, won't go into the details. So, the H or magnetic field actually has a very low impedance source in the near field, whereas the electric or E field has a very high impedance.

**Dave Jones:** I'll clarify that in a minute. But basically, it all comes down to the wavelength lambda here and this is normalized to one here and it's lambda on 2 pi, which is basically we're we're going to normalize to that value.

**Dave Jones:** And of course, let's take for example 100 MHz is a wavelength of 3 m. So, pi on 2, that's about a half meter. So, when you get to a half meter away from your product, this is where the electric fields and the magnetic field actually start to converge.

**Dave Jones:** It's not really clean like this. There's a bit of you know, overlap in here and this is like the transition. There's going to be like a transition region in here where the two fields eventually combine and anything over roughly half a meter away at 100 MHz, the electric and magnetic fields combine to give you a singular impedance, which actually happens to be 377 ohms in free air.

**Dave Jones:** So, anything over the wavelength on 2 pi is deemed to be the far field and anything closer physically closer than that like we just did with our probes here is the near field.

**Dave Jones:** Now, this is why we have two different types of probes. One is the H field probe, the magnetic probe, the other is the E field or electric field probe and the magnetic or H field is going to be generated by higher currents, i.e.

**Dave Jones:** sources that have a very a lower impedance. So, for example, if you've got a lot of current flowing in a in a particular trace either due to an actual like heavy current switching or even very fast switching that's dumping a lot of energy into the bypass capacitors and the capacitance between the power planes and everything else, then that's generating typically be generating a magnetic field due to the

**Dave Jones:** low impedance and the high current. But, very high impedance things that don't generate lots of current, then they generate electric fields and hence the bigger source impedance. So, you can generate electric fields from say just like a static power supply for example, your 5-V power supply.

**Dave Jones:** Whereas all your switching stuff will dominate down in the H field here because there's lots of current being dumped into the trace or the load capacitance or the particular load itself when you're switching things.

**Dave Jones:** So, that's why you need to use these two different probes and the magnetic field probes, they are sensitive to orientation like this and like that as well as I talked about on the plane.

**Dave Jones:** Whereas the electric field is not sensitive. You can just put that in any orientation and it's not going to make a difference. So, if I use my E field probe like this and let's say I probe this power trace over here like this, you can see it's really not going to make any difference the orientation that I put that in.

**Dave Jones:** It's just completely insensitive to that because there's no magnetic field coupling. It's electric field coupling and it's just purely the distance. But if you take a magnetic loop probe like this and I just change the orientation like that, wow, that makes a big difference.

**Dave Jones:** It really brings out the peaks if I put it vertically like that. If I put it horizontal, it gets more of the current flowing through the trace. And if we use our smallest H-field probe, let's just have a look at let's say this like blank area over here.

**Dave Jones:** This is our four-layer board like this or maybe right over on the edge of the corner of the board right over here like this and let's compare that with our two-layer board here.

**Dave Jones:** Bingo, look at that. Because we've actually got a power trace actually running right around this corner as well, which we actually physically remove. And you can actually see that the power trace actually running all the way around there like that.

**Dave Jones:** So, that's just going to radiate like buggery. But even if we go over just the ground plane there, you can see it's much much higher than we get with the four-layer board.

**Dave Jones:** And this is why at the EMC test house they'll test in the far field here cuz it binds the electric and magnetic fields together. And basically the typical testing distances would be like a 1 m, 3 m, 5 m, 10 m for example away.

**Dave Jones:** It depends on the type of product they're testing and to which standard they're actually testing to. But say if you put it 10 m away, then you can have a larger rotating turntable so that your product rotates around like this on the turntable and they can measure all the axes like this when they while they have their super expensive, you know, bi-conical um super calibrated measurement antenna 10 m away measuring

**Dave Jones:** over, say, 30 MHz to 10 GHz far field, for example, might be a typical measurement range. And then there'll be standard like envelopes that you have to get under and also peaks and things like that.

**Dave Jones:** And it gets, you know, the standard gets quite complicated, but yeah, just the near field testing that we do here doesn't really translate to the far field, but you can certainly get an indication of whether or not you've got any nasties on your board.
