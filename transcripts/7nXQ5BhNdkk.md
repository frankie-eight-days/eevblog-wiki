---
video_id: 7nXQ5BhNdkk
title: EEVblog #98 - Microsoft InstaLoad Battery Technology - Patent Busting Time?
url: https://www.youtube.com/watch?v=7nXQ5BhNdkk
source: youtube-asr
---

**Dave Jones:** Hi, welcome to the AEVlog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Once in every blue moon, along comes an idea, a concept, a product so gobsmackingly simple, you just want to

**Dave Jones:** smack your forehead and go, "Why didn't I think of that? That is just so obvious. It's brilliant. Why hasn't anyone done that before? It solves such an incredibly simple yet annoying problem in almost, you know, in millions, billions

**Dave Jones:** of products out there." What is it? Well, I was reading yesterday about Microsoft's new InstaLoad battery technology. Microsoft? Yeah, it's you know, electronics engineering, Microsoft. It's not something you'd normally associate with a company like Microsoft. But their new InstaLoad

**Dave Jones:** battery technology is just so gobsmackingly simple and brilliant. It has some limitations, but we'll get into that. But you just shake your head and go, "Surely somebody has done that before." What it is is it allows standard AA,

**Dave Jones:** AAA, C's, D's, regular batteries to be inserted into a product either way around. The polarity doesn't matter. And it doesn't involve circuitry. It's just the battery contacts themselves which allow you to do this. It automatically fixes the polarity of the battery

**Dave Jones:** whichever way you insert it. Brilliant! Now, Microsoft just announced this a couple of days ago, and they're trying to license this InstaLoad battery technology. As you'd expect, they've got a patent or patents on it. I haven't actually looked at the patents, but

**Dave Jones:** they've clearly got patents and they're trying to license the technology to people to install, you know, to allow consumers to install product in store batteries either way around. And um they I think they've already picked up a couple of

**Dave Jones:** major manufacturers to actually do it. And here's a photo of the actual battery technology. And take a look at it. These little contacts, it's incredibly simple. It's just you have one of these contacts at either end. And basically what it

**Dave Jones:** does is the battery nipple actually goes down into um into the contacts. So it's got essentially a positive and a negative contact at each end. And they're just wired in parallel crisscross fashion across the battery. And you when you

**Dave Jones:** insert the battery at one end, the nipple, whichever end it is, goes into the nipple contact and makes contact with the nipple bit, the positive one, and the other end makes contact with the negative, and vice versa. And that's it.

**Dave Jones:** And it's just incredibly simple. Now, if somebody came to me and gave me the spec, I need you to design a battery holder or a product that does that, that you can install batteries either way around, and I don't want to pay extra

**Dave Jones:** for any circuitry. Well, I probably would have come up with that because it's so bleedingly obvious. And I'm not sure if anyone's ever done it before, but I'd be a bit surprised if there's not some niche product out there that,

**Dave Jones:** you know, that actually essentially has this in it. I I've heard of a few products over the years that um I think I may have even seen them that, you know, you if you plug the battery in and

**Dave Jones:** it physically won't let you install it the wrong way around. It uses the nipple as a key to install the battery. And that forces you to install the battery the correct way. But this new InstaLoad thing actually handles that either way

**Dave Jones:** around. It just doesn't matter. You plug in the battery in, bingo. Brilliant. Has anyone done it before? I don't know. Let me know if you've seen a product and you can bust the Microsoft patent but with um some actual prior art

**Dave Jones:** cuz it's it's 2010 for God's sake, you know? How how long have these batteries, standard batteries, been around? And well, Microsoft have obviously patented this and presumably nobody's ever done it before, but that doesn't stop the patent office

**Dave Jones:** patent office giving them a patent for it cuz they're notoriously bad at finding prior art, but yeah, if you can find something, leave a comment and let's bust the Microsoft patent on this wide open. Now, this technology isn't magic. I said

**Dave Jones:** there's a few problems with it and here's problem number one. Now, please excuse the crudity of this model. I didn't have time to build it to scale or to paint it. And here it is, right? It's got basically a positive and negative

**Dave Jones:** contact at each end, okay? And what it is, you know, it's got that U-shaped one for the negative terminal and then the inner one which is set back. It's, you know, it's set back a certain distance like that for the positive terminal for

**Dave Jones:** the nipple. And the battery has a nipple on one end and when you insert it, okay, these two negative terminals must be shorted together and the two positive terminals must be shorted together and that goes off to your circuitry, okay?

**Dave Jones:** There's your There's your negative and there's your positive terminal which goes off to your circuitry. Now, clearly you've got two negative terminals shorted at each end. And when you plug the battery in like this, you're you've got uh these two negative terminals

**Dave Jones:** protruding out the furthest. So, if you plug in the battery and it doesn't align correctly, that nipple, if that touches that negative terminal while the back end touches the negative terminal of the battery touches the negative at that

**Dave Jones:** end, bingo, bang, you short out your battery. And if some batteries can produce um you know, a very high um short circuit currents in the orders of, you know, tens of amps for some of the rechargeable batteries. So, really, you

**Dave Jones:** know, it's critical that you design the space between, um, between the positive, uh, between that negative, um, terminal there, so that and your battery holder itself, the physical implementation of the battery holder, so the battery slides down and there's

**Dave Jones:** absolutely no possibility at all of actually shorting your battery. So, that's critical. And some batteries actually have different size nipples. They can actually be different, um, depths and different, uh, widths. So, you've got to actually, but, you know,

**Dave Jones:** account for that. So, I'm just wondering if, the Microsoft, uh, they give you application notes if you sign up for them to use their technology. I wonder if they've actually, how much engineering they've put into that of actually assembling the battery in

**Dave Jones:** there. Now, of course, it might be possible to protect against that short circuit, uh, condition by installing a resettable poly switch or something in there between the two negative terminals, but that's not really a proper solution. So, that's problem number one. Problem

**Dave Jones:** number two comes from people's just decades worth, I don't know, 30, 40 years worth of, um, installing these batteries a certain way around. People are conditioned to look when they open a product to replace the batteries, they're conditioned up here to look for

**Dave Jones:** those positive and negative terminal markers. And if they don't find them, they get all paranoid and, "Ooh, which way should the battery go?" And, you know, Microsoft claim that, uh, one of the big things is that, "Oh, you don't need

**Dave Jones:** those markings anymore." Well, you're going to have to have something bigger and better that says it can go either way around to make it obvious. But, either way, people have to look for that. So, really, unless you know that

**Dave Jones:** you're that the product you've actually bought is um uh you know, has this InstaLoad technology in it, then, you know, you're just going to have to look for that and you're going to have to unless every product in the world changes um

**Dave Jones:** instantly and then maybe 10 years time it doesn't polarity doesn't matter. But, that's not going to happen. So, really, you can't really get around people's mind conditioning to having to install batteries the right way. So, really, there's no huge time saving there unless

**Dave Jones:** you're actually aware of it. It could actually confuse some people. And the third problem might actually come down the track. Now, let's say this technology works and it gets out there and people start getting familiar with it. It's been out there for 5 or 10

**Dave Jones:** years and uh you know, there might be some really stupid people out there. Now, don't underestimate stupid because people will surprise you every time. People might start inserting thinking that oh, every product should have this technology where polarity on the battery

**Dave Jones:** doesn't matter and I can insert it either way around and people start blowing up their products. But, hey, you know, you can't cater against stupid and I'm sure the lawyers already have that uh you know, squared away in every product

**Dave Jones:** by having the warning markings on there and printing it in the manual. So, eh, don't worry about that one. Now, curiously, take a look at this. This is one of the terminals from um their InstaLoad battery PDF document.

**Dave Jones:** Now, clearly, this one is just um only suitable for products that have like a cylindrical um tube like a keychain flashlight battery where the battery gets actually loaded into the actual tube because um really, unless there's something that aligns the battery on

**Dave Jones:** that axial um plane, you can't just use this terminal to slide the battery in cuz the nipple will just short out to to that complete circular outer negative ring. So, you know, they don't actually show that here as um being used in um

**Dave Jones:** any sort of, you know, tubular type system, but that one clearly does. Now, here's a photo of the other type they've actually got, and this one can clearly um be used in products where you actually insert the batteries, you know,

**Dave Jones:** horizontally or you know, vertically, sorry, vertically down into the actual uh product. And you can see that that the nipple can't actually um short out to the negative terminal. So, that's a pretty good design there. Now, the third

**Dave Jones:** one here, which they show as you're getting one of their test products, I think it is. Um that's sort of a similar kind of concept, but I like the other plastic one uh better. Now, this one could actually, you can see that if the nipple

**Dave Jones:** was too wide or something like that, or uh or the battery was or the if those battery wells weren't actually set to the correct width, then people could actually, possibly, insert that battery um and short out the actual nipple to

**Dave Jones:** the negative terminal. So, you've got to be real careful with this design. Microsoft or people who implement this design really need to take into account uh you know, the variant types of nipples out there on batteries and how

**Dave Jones:** they're actually going to be inserted to make sure it's completely safe. So, this new Microsoft InstaLoad technology, is it any good? Well, I don't know. The verdict's still out on that. Let's see what they what products they actually come up with. And um I

**Dave Jones:** think there are quite a few niche products out there where this quite handy. Um you know, in for an emergency situations like um headlamps and torches. Um you know, if you're hanging on the side of a cliff or something and

**Dave Jones:** you're you're doing something really dangerous and you need to and your batteries run out and you need to change them and you've only got one hand and you've got no other lights and you you know, and you just need to wham those

**Dave Jones:** batteries in to get uh the thing working again, then, you know, this technology could be really, really handy. And well, I'm surprised nobody's done it before. I saw it and I went, "Ah, why didn't I come up with that and patent that? God,

**Dave Jones:** could have MADE A MILLION BUCKS, 10 MILLION, 100 million, a billion. I don't know. Let's see how far the technology can go. And if you've Remember, if you've seen this before in some other product, leave a note and we'll bust

**Dave Jones:** this Microsoft patent wide open. Beauty.
