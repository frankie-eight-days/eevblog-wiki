---
video_id: -VaAplMihrg
title: EEVblog #349 - SMCBA Lecture IPC-2581 Open Standards for PCB Design Data
url: https://www.youtube.com/watch?v=-VaAplMihrg
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 17, "2": 39, "3": 58, "4": 82, "5": 101, "6": 125, "7": 147, "8": 162, "9": 185, "10": 210, "11": 229, "12": 254, "13": 273, "14": 298, "15": 318, "16": 336, "17": 367, "18": 387, "19": 420, "20": 444, "21": 461, "22": 479, "23": 502, "24": 528, "25": 551, "26": 576, "27": 600, "28": 622, "29": 639, "30": 652, "31": 666, "32": 686, "33": 707, "34": 727, "35": 743, "36": 765, "37": 786, "38": 802, "39": 817, "40": 840, "41": 856, "42": 872, "43": 894, "44": 912, "45": 939, "46": 958, "47": 976, "48": 998, "49": 1019, "50": 1042, "51": 1062, "52": 1077, "53": 1092, "54": 1106, "55": 1135, "56": 1150, "57": 1169, "58": 1186, "59": 1208, "60": 1226, "61": 1241, "62": 1259, "63": 1274, "64": 1291, "65": 1307, "66": 1328, "67": 1351, "68": 1377, "69": 1398, "70": 1415, "71": 1433, "72": 1453, "73": 1472, "74": 1492, "75": 1509, "76": 1523, "77": 1541, "78": 1562, "79": 1581, "80": 1597, "81": 1611, "82": 1634, "83": 1663, "84": 1690, "85": 1711, "86": 1733, "87": 1748, "88": 1760, "89": 1773, "90": 1793, "91": 1815, "92": 1833, "93": 1876, "94": 1890, "95": 1904, "96": 1918, "97": 1941, "98": 1960, "99": 1975, "100": 1986, "101": 2004, "102": 2023, "103": 2042, "104": 2054, "105": 2072, "106": 2108, "107": 2121, "108": 2143, "109": 2165, "110": 2184, "111": 2201, "112": 2217, "113": 2236, "114": 2253, "115": 2264, "116": 2280, "117": 2295, "118": 2312, "119": 2329, "120": 2343, "121": 2354, "122": 2372, "123": 2383, "124": 2396, "125": 2408, "126": 2419, "127": 2438, "128": 2453, "129": 2473, "130": 2489, "131": 2509, "132": 2527, "133": 2551, "134": 2569, "135": 2589, "136": 2609, "137": 2627, "138": 2645, "139": 2663, "140": 2687, "141": 2706, "142": 2728, "143": 2744, "144": 2756, "145": 2776, "146": 2793, "147": 2809, "148": 2822, "149": 2839, "150": 2857, "151": 2879, "152": 2900, "153": 2918, "154": 2938, "155": 2959, "156": 2978, "157": 3000, "158": 3023, "159": 3046, "160": 3072, "161": 3097, "162": 3130, "163": 3159, "164": 3198, "165": 3243, "166": 3288, "167": 3335, "168": 3381, "169": 3426, "170": 3471, "171": 3516, "172": 3561, "173": 3606, "174": 3651}
---

**Dave Jones:** Okay, I'm actually filling in for someone on this consortium in the 2581, but I have been somewhat involved with it in the sidelines. So I have a short presentation that will introduce you to what's going on. And basically, the 2581 is a data format.

**Dave Jones:** It's not software, it's a format. And it's used to communicate a lot of information. We'll touch base with some of that information within the slide set. I do want to give you a little bit of a history of data transfer and why we're looking for another format,

**Dave Jones:** why we're doing what we are doing as a group, who the players are and some of the history of data transfer, the good, the bad and the uglies. And Clint Eastwood is not part of that. The first thing I want to talk about is the design process.

**Dave Jones:** Basically, the design process, you design your board, then you pass it out to a prototype manufacturing, and then from that you might be doing some in-circuit tests and assembly, but right on through the whole product development cycle. And what would be nice is if we had one data highway that covered everybody's needs.

**Dave Jones:** And it's a two-way street. You place something down, some information, someone needs that information, they take it off, they put new information on. As we stand right now, every one of those evolutions have their own formats, their own data formats, some of it's paper, some of it's electronic, et cetera.

**Dave Jones:** So we really would like to have something that's more economical. Let's see what happens. The process involves today a multi-format delivery. What that means, very simply, is that I have formats for everything. I have the RS274X for the Gerber files coming out. I have maybe some excellent drill files in their format.

**Dave Jones:** I have the D356 format for the electrical test, and maybe I have the drawing information for the 2511 in ASCII, PDF, HPGL, JPEGs, all these different formats. And every time you have a different format, you have to have a translator to create the format,

**Dave Jones:** and then you need something to create it back into the format that you need in a particular piece of equipment. So there's plenty of room for error, and there are errors. Errors happen every day. And I remember at one point in time, we did an analysis.

**Dave Jones:** It was over $250 million a year goes down in the waste can because of poor data transfer, and that's basically poor communication downstream. So we've been chasing this thing for quite a number of years. Okay, and today, you know, we're trying to do more with less,

**Dave Jones:** and data transfer and errors and things like that are not helping us at all. The CAD companies have been very reluctant in the past to apply any resources to post-processors. They make money selling you the basic tool, right? And the basic post-processors are done by the entry-level programmer just to get used to using the tool,

**Dave Jones:** and sometimes that data is just not correct. Scale is off, elements are in the wrong place, missing, et cetera. So while companies undertake to do more or less, they want to reduce reliance upon paper. Okay, we're looking to go more electronic data transfer.

**Dave Jones:** We see in our shop, we see a lot of electronic transfer, just about all of our inputs coming electronically. We have many solutions, but they all require custom extensions, and they're costly to maintain. So at the OEM level, the fabrication level, you know, the contract manufacturers,

**Dave Jones:** all of those have their own specific requirements, and we need to streamline that process somewhat. And it gets a little bit worse as well. Let me give you a little bit of a data transfer standard history. Way back in 1970, I know half of you weren't born then, okay,

**Dave Jones:** but back in 1970, IPC put together this IPC D350 format. It was an intelligent version of Gerber format. Now, Gerber format is very simple. It's the least common denominator in data formats. It's used to drive a plotting machine. It's a proprietary format. It says, turn the light on, drag it over here, shut the light off.

**Dave Jones:** I just created a line on a piece of film, okay? We needed more information, and the D350 series of formats added in the aperture list, they added in a bunch of other items that was okay. But back in 1970, why it didn't really take off, it's very simple.

**Dave Jones:** The CAD companies did not want to support any kind of a format that would allow you to take your work from my tool, from this tool, and put it into someone else's tool. They wanted to lock you on in. So they didn't support any kind of a data format that would allow interchangeability between CAD systems.

**Dave Jones:** That wasn't in their cards in 1970. In 1980, the U.S. military adopted the MIL-STD-275 design for the boards and data transfer in an attempt to also standardize the information that's being placed out there. The IEC in 1988, they adopted the 350, and anything that goes internationally with the IEC

**Dave Jones:** usually gets their own number, their own numbering system, and a lot of times it's the same document that we have. I know at IPC, we submit all of our documents to IEC for adoption, and they had the equivalent, which is the 61182-1 in 1988 for that 350 document.

**Dave Jones:** In 1992 and 94, in that time frame, the JPCA, the Japanese Printing Circuit Association, they created the CAD-to-CAD transfer, and they had different concepts for codes, and that was released in the IEC as well as in IEC 61182-10. And then we come up into nowadays, 1998, IPC had the 25X, 1X series, the GENCAM.

**Dave Jones:** Now GENCAM was a format, GENCAD was a format that was owned by a private organization. They donated it to the industry, and the reason we selected that GENCAD format is because most of the electronic side of the business, the engineering side, was all in this particular type of format.

**Dave Jones:** And it would take very little for us to adopt the basic format and then add the things that were unique to the printing and wiring board side of the business. So back in 1992, we started, I'm sorry, back in 1998, we built that GENCAM,

**Dave Jones:** we called it GENCAM so people had a relationship to the other one, the GENCAD product that was sitting out there. And then we formed some revisions on that, and then came the problem. Okay, it's not on the slides, and I'll give you the problem.

**Dave Jones:** We had a company out there called Valor, and Valor created, has the CAM station software for most of the board shops, about 85% market share worldwide. And they have a format called ODB++, right? And it's a robust format, and it's an intelligent format.

**Dave Jones:** It contains a lot of the database. The only thing is, it's not really structured very well internally. Okay, number one. Number two, it wasn't as robust as GENCAM. And number three, it was proprietary to Valor. Okay, whereas the IPC format is industry-owned. It's developed by the industry and distributed by the industry,

**Dave Jones:** and it's all free of charge. Okay, they went to the NEMI organization, and they had us put a hold on the GENCAM product for five years. Okay, and basically the marching order was very simple. Make a new format that makes ODB++ look like GENCAM,

**Dave Jones:** and then we could adopt it. So after all of that, and we enhanced it. We enhanced the format, and we came up with the 2581 series. In 2003, I and NEMI recommended that. In 2011, we formed this consortia. And so now you have a 2581 series of formats

**Dave Jones:** that gives you the best world of GENCAM and ODB++. We'll talk a little bit more about it as we go along the line. It eliminated the dedicated company's ownership. However, ODB++ still exists. Valor still exists under different names. We'll talk about that in a little bit.

**Dave Jones:** They support the 2581. However, they will modify their ODB output to kind of lock in to their types of thinking. And we'll go through the mergers and all that stuff later on. But basically, then we have the consortia in 2011. We'll talk more about that.

**Dave Jones:** This was what we were talking about a little earlier. We froze the revision for two years to let the cad companies or the software writers write up the format. So let's face it. I have a format. You know what a format is? All it is is a structure.

**Dave Jones:** Each one of these little squares on the ceiling could be a format. So maybe I'll take all the whole information and put it in this square. Like a mailbox. I'll put all the line information over there. I'll put the test information over here.

**Dave Jones:** And on and on, all structured format. So now, if your company needs the whole information, you'll go to that particular box and pull out the whole information. And if you need to do something, you put in another thing. Then the guy in the back, he needs that information.

**Dave Jones:** He pulls it out and puts something else in. So everybody knew where it is. It requires the CAD system to be able to output all the information within the file to the appropriate box in the mailbox. And it involves the manufacturer, the assembler, the tester

**Dave Jones:** to have software that will also extract it from the appropriate box and then move on forward. That's basically a data transfer type of roadmap. In the meantime, the committees looked at what was out there and it looked like the XML type of description,

**Dave Jones:** data transfer description, would be taking hold. Then the Worldwide Web Committee finally just locked in XML schema as a way that they were going to transfer all kinds of data. So we figured, for an open source type of format, then we're going to make the new version all XML schema-based

**Dave Jones:** so that we're compatible with the rest of the world and everything else that's going on in data transfer. So that's what we did. And what that schema permits us to do, it allows us to look at the numerical, the angular, and other descriptions and we can check for correctness,

**Dave Jones:** do software compliance. So we're using the tools that everyone else is using in order to create new data transfer software. The need for data, intelligent data transfer, as we've moved on over the years is because we're trying to get more efficient. We're trying to get more efficient.

**Dave Jones:** We have much more complex electronics that we're trying to document and transfer the data. So again, we want to have that intelligent data transfer. I'll give you a couple of quickie items on what I feel this means to me. Let's compare it to Gerber.

**Dave Jones:** How many are familiar with Gerber? Most of you are familiar with Gerber. Gerber being the least common denominator, will Gerber tell you what the hole sizes are? It won't tell you what the hole sizes are, the tolerances, or the locations. Will Gerber tell you how many boards to order?

**Dave Jones:** How about the stack-up? Will it tell you what the layer stack-up is, what the copper is on each of the layers? Probably not. Will it tell you which conductors have controlled impedance? Will it tell you about the bare board test fixture? What kind of fixture?

**Dave Jones:** Everything about building that? Or the ICT test fixture? It'll give you all the test vectors. And on and on and on. All of that information is information that we require someplace along development cycle. The intelligent data transfer will contain all of that information.

**Dave Jones:** It'll allow you to have all the information. You can segment it and only send the fabricator what he needs and assemble what he needs, etc. Or you can send the whole darn file. What's nice about it, it's good for archiving your product for long-term.

**Dave Jones:** Everything that's necessary to build that product would be in this archived file. So you can bring it back 20 years from now and duplicate what you had to do. As long as the materials and components are still available, obviously. So, what's the solution to the problem?

**Dave Jones:** The 2581 is a single-source file containing the entire PCB structure. Everything from parts to CRP systems, CAD data, CAM data, models, you name it. The improvements over the existing formats, you have very rich schema defined, which defines all of the intricate parts of everything.

**Dave Jones:** It could support part polarity, part orientation. It gives you consistent definitions. Improves the support for drilled and milled contents, so blind and buried Vs, back drilling, V grooving slots. All that stuff is contained. You won't find that in a Gerber file at all.

**Dave Jones:** And a lot of that you won't find in an ODB Plus file either. However, it's supposed to be totally robust. Improved embedded components, stacked components support. It'll give you improved support for your functional and JTAG and ICT. And it gives you automatic viewing with viewing software.

**Dave Jones:** And Andy will show that afterwards. He'll show you some demonstrations of that. Summary benefits. I've taken this from several presentations that I didn't create. So, you know, I'm guessing at some of it, but we're doing fine. The benefit summary is open, it's vendor neutral, and standards based.

**Dave Jones:** When I say it's open, it's owned by the industry. IPC is an industry-based trade association. SMCBA is part of IPC. They have association with it. So you own it. If you see something missing, you want something, you just let them know, and it gets placed in there.

**Dave Jones:** Whereas something that's private, if you want something, you need something, it has to make a business case to get it. So it wants to be open source. Improves your efficiency in design, fabrication, and manufacturing by passing accurate data. You don't have to assume when you're not losing an aperture list,

**Dave Jones:** something like that. Everything's coming out right directly from the data file. There's no misinterpretation. Okay? And results in lower cost, basically. Your information transfer wants to go from what your cash system is looking for all the way through to the electronic data transfer side.

**Dave Jones:** I'll just kind of skip this slide. There's a couple of slides in here that are necessary or not. Anyway, I have a CAD-specific design. I have a CAD-independent golden file and manufacturing-specific processes. The ideal ultimate goal is to create this data transfer and directly drive your end machine.

**Dave Jones:** I'll give you an example. In a bare board test, okay, we say you have to have a 356 file, which defines the test parameters for the bare board tester. But the software that we send, the 356, doesn't really drive directly the machines, the test machines.

**Dave Jones:** Maybe the new ones will accept it and drive it. So basically what they'll do is they'll have a 356 file that you gave them, and then they'll take the Gerbers that you gave them, they'll extract the net list, they'll compare that net list against the 356,

**Dave Jones:** and they'll make that net list look like the 356, and then they drive their machine. So we're trying to eliminate all of this conversion and driving and stuff like that. If you want to drive it ultimately, just drive it directly. It makes a lot of sense, I would think.

**Dave Jones:** Okay, this is a very busy slide, and I'm certainly not going to point to the little letters because I can't see them. I'm sure you can't see them from the back. But basically it's a roadmap for all the vendor mergers. And I just want to focus on one set of mergers for you.

**Dave Jones:** As an example, and why we're at this stage with the consortium. You had Valor with the ODB++, and then Valor was purchased by Mentor Graphics. Now Mentor Graphics now owns Valor. Now Valor was also supported by Cadence and several other CAD manufacturers. They all had Valor output.

**Dave Jones:** Valor helped them write into all that stuff like that. But when Mentor Graphics took it over, they were a CAD manufacturer. Their competition is Cadence and the rest of those guys. So they immediately went to work to make it so that those other guys

**Dave Jones:** didn't have access to the right format. Because they wanted everyone to use the ODB. That wasn't the Mentor format. Well, Cadence and Zookin and everyone else got together and said, listen, you know, we're very nervous. We have a private company going to own the only data format that everyone's using.

**Dave Jones:** It's not really a healthy situation. We need to do something different. So they formed a consortium. And the consortium consisted of a lot of suppliers. You'll see them all coming up on the next several slides. So I'll go up one more slide so that you can be looking a little bit.

**Dave Jones:** They formed the consortium to adopt the industry standard of 2581 from IPC because it's owned by the industry. And in the consortium, they said, okay, what do we need to do to make this thing successful since we're adopting it? Number one, we have to make sure that the format itself

**Dave Jones:** coming out of a particular piece of equipment is accurate to the standard. It doesn't hiccup if there's something missing or something is additional. We have to make sure that the software that does that is validated. We have to make sure that when it goes into the next piece of equipment

**Dave Jones:** or into assembly, wherever it's going, that the input software can accurately record and take from that database all the information that it needs. It doesn't hiccup if it doesn't see something or does something in a special way. They have to make sure that all happens.

**Dave Jones:** So when they adopted it, they adopted it and they said, we're going to create the software, we're going to create the models, we're going to get the industry to support an effort to iron out all of the data transfer stuff. So if you go, if you went to the last IPC conference

**Dave Jones:** down in Elkins, Schaumburg, Illinois a few weeks ago, if you're going to PCB West on the west coast of the United States the week after next, you'll see they'll have a booth and they're going to be exchanging a design file that they created in Cadence.

**Dave Jones:** They're going to move it over to Zookin. They're going to move it out to Valor. They're going to move it up and down the whole product development system. They're moving back and forth. And any hiccups or enhancements, they're taking control and they're making the recommendations to IPC committee

**Dave Jones:** so that we can roll the darn things in. So here we have an industry consortium that's sitting out there and basically it's a free consortium. There'll be a slide in here how you can join and what the requirements are for joining because it's a freebie thing.

**Dave Jones:** So you have different working groups within the consortium. And the whole purpose of that evolution is to develop proposals and work with IPCs to extend the standard to new technologies and methodologies. And the leader for that is Gary Carter from Fujitsu. He's the lead in that particular working group.

**Dave Jones:** And Harris, NVIDIA, and Ericsson are all part of that particular working group. From the technical side, you need to validate the 2581 files that were consumed by the tool. You need to identify the areas that needed to be extended. And Cadence, Ed Aitchison, he's the lead downstream.

**Dave Jones:** ADIVA, WISE, Artwork Conversion, Zookin, and Easy Logic are all part of that effort or that particular technical team. And then the awareness and promotion will come from published articles in all the publications at the different conferences, PCB West. Cadence and Hermant Shah is the lead.

**Dave Jones:** Zookin, Downstream, Intercept, Upmedia, they'll all be down at the conference in the booth showing how this thing is demonstrating how everything is working. Who can join the consortium is open to any PC design supply chain company who's prepared to adopt the consortium's goals and objectives.

**Dave Jones:** And there's a slide talking about the goals coming up. And committed to the roadmap. It doesn't cost you anything. All you have to do is make a public statement. A public statement says, listen, we support the 2581, and we're going to try to help promote it any way that we can.

**Dave Jones:** Either ask for our suppliers to accept it in or place it out, whatever the case may be. And you get your logo thrown on there, that type of thing. I mean, it's as simple as that. You open a website and you're just going to join it.

**Dave Jones:** All right? Actively support that 2581. You talk it up in your DFMs, in your FAB, you ask for it. Your CAD company, if it's not one of those, your board suppliers, anybody else down the stream, if you ask for it and you ask for it long enough

**Dave Jones:** and you're threatened to not give them the job or something like that, they'll put pressure on their suppliers to give them the support, the software support that's necessary. All right? The mission statement for the technical working group is simple. The goal of the validation process team is to define

**Dave Jones:** and document the validation of the 2581 export against current exported data formats like Gerber, ODB++, SCDrill, et cetera. So we want to validate against those particular individual programs, make sure that it truly replaces those programs to ensure that 2581 data is identical and complete

**Dave Jones:** for the fabrication, assembly, and the test of printed circuit boards to promote and ensure the industry adoption of that particular standard. We, you know, with the 350 format and all previous efforts, we really never had an industry consortium promoting it and pushing it

**Dave Jones:** and trying to do a lot of the work. This is the first time in many, many years that I've ever seen where the industry is actually getting behind and pushing it. And they had selfish means because they didn't want one company to control everything.

**Dave Jones:** They wanted the industry to stay with it. And the team validation flow from the creation tools, whether it be Cadence, Allegro, Zookin, Intercept, or Altium, whatever it may be, they will output the files in Gerber or 2581, ODB++, and see if they'll output all the files.

**Dave Jones:** And then the validation tools from Adiva or Wise or downstream, those guys, they will actually read the data in and see if it works, see if it's doing the right thing. Okay? The technical team, the comparison process is going through, the 2581 out through the CAD tool,

**Dave Jones:** output individual files back through the CAM tool, and keep doing that type of setup. So the roadmap is very simple. Create and test. It's a suite going to the push and test available all the way out to board fabrication. You can start from the beginning out to the end.

**Dave Jones:** It's as simple as that. Okay? Test cases and viewers, you'll notice there's a link. You'll notice there's a link sitting up here. Okay? And that link will get you up to the test cases and viewers. You can see the results, what they had,

**Dave Jones:** and you can download the viewers. I think Andy's going to be showing us one of the viewers. Is that correct, Andy? Yeah. The viewers of how it's working. And you can see what was done with the CADs, NVIDIA, and Fujitsu. They've been transferring files back and forth between all of these groups.

**Dave Jones:** It really makes it pretty good. Okay? Common consortia members sitting up there. You'll see media companies. You'll see NVIDIA, Cisco, Intercept Technologies, Harris Corporation, and growing, much growing since then. I mean, my company's not even up there yet. We haven't done that yet.

**Dave Jones:** All right? It's just a matter of just saying, hey, yeah, I support it. They know that I support it. And the next several slides try to give you some kind of a brief description of what's going on in there. You have a standardization strategy for your generic stuff, your administrative data, your drawings, your bare board tests, all the way down to library symbols, alternatives, and how complex the data is for those.

**Dave Jones:** Very simple data. It's just real basic, everything that we have today. All right? Complexity B will now go with the 2581 series where we're adding all the extra information here. Then it's a 2511 series that's supporting that with documentation, et cetera. Okay? And what they did with the segmentation concepts, you have all your bill of materials, hierarchical conductors, your drilling, routing lathes, all that information.

**Dave Jones:** And what they did, they said, okay, you have design, fabrication, assembly, and test. Who contains that information or provides it or uses it? And give the yeses and noes. Try to give them a little bit of a roadmap of what's going on. They all adopt one standard viewing convention that we've had for many years.

**Dave Jones:** You view it from the face you're looking at and go on down, one, two, three, four, five, six, as you're moving on down. That is the viewing convention that's been around for many, many years. The standard in using dictionaries has been defined. We had to define things like butterflies and circles and contours and rectangle rounds, rectangle corners.

**Dave Jones:** All of that standard user dictionary has all been defined as something standard. Because, you know, when you're dealing with electronic format, dealing with computers, you have to have a common name when you're transferring different data. And everyone has to have the same thing.

**Dave Jones:** If you're going to have a slightly different name and you're going to have a slightly different name, we can't really get software to correlate slightly different names. It has to be the same thing so that everything moves on down the line. You know how it is.

**Dave Jones:** You type the wrong letter, the computer shows it back and says, spell it right. Okay? So it's the same type of thing. And they cover all the different types of primitives that you might see out there. And we can keep on adding it.

**Dave Jones:** All right? We can keep on adding it. The new tool schema that was released in the first quarter of 2012. All right? And they're still working on enhancing it. And then the last slide that we have is the standards hierarchy. Here are your data formats, your 2581 series.

**Dave Jones:** This is your generic requirements for the board descriptions and the administrative and manufacturing data in the 282. The design characteristics in the 83, the 84 is the board data description. And it keeps on going on down the line. All right? And your documentation in the 26 is down that way.

**Dave Jones:** So there's an awful lot that's in there. I'll give you just a brief snapshot of what's going on because I know it's late. I'm kind of done with mine. I'm going to transfer it over to Andy. Andy will now show you the actual viewer of the software viewing a data file from 2581.

**Dave Jones:** And I don't know what else you're going to do. So you do the talking. Did anybody notice what was seriously missing on the consortium members? Yes, the 600-pound gorilla of the CADSYS, CAD Vendors, better graphics. They're not in the consortium. Sorry? Oh, I stand corrected.

**Dave Jones:** Fantastic. What about ALTI? Were they part of it? Name was missing. I thought they were, but I didn't see them up there, so I really don't know. Okay. So that's a good thing, right? Because traditionally, as Gary said, traditionally the vendors didn't want to do this, right?

**Dave Jones:** Because I could take an ALTI file and put it into Expedition and vice versa. So vice versa, wouldn't have done that. Right? It costs $220,000 or whatever it costs. And ALTI was $4 or $5 grand or whatever it is. They don't want that tool to go down there because that will do 90% of what this tool does.

**Dave Jones:** Okay? Okay, so there's a whole bunch of issues about how this is not a good thing from a CAD Vendors point of view. Anyway, we don't have liftoff. Yes, we do. Of course we do. I'm going to have a quick look at the standard.

**Dave Jones:** This is free. You can download it from the consortium. Somewhere in there was a link to the consortium, and you can download this stuff from there. The standard is open, free, available to anybody. And if you look through it, typical standard. Right? You got that?

**Dave Jones:** Ask questions later. Are you getting this? Okay. This is really great. I've had a quick look at this. I don't know it in great detail, but it's fantastic. Let me quickly describe how this works. We have a file. It's a text file. It's basically a text file, XML, very well defined.

**Dave Jones:** I have a pad, and I define a pad. And it's got such a certain diameter. And down here I have a pad that's a rectangle. And I define that as a circle 1, rectangle 1, something else 1, something else 1. Further down, somewhere down there, I define an integrated circuit.

**Dave Jones:** And it says, give me 14 of pad 1, and put them there and there and there and there, and there and there and there and there, and so on. So now I've got a little group down here that calls up something up there,

**Dave Jones:** calls it up, instantiates it 14 times, and says, here's an IC, 14 pins. Okay? Further down in the file it says, put one of these down there at this location. Okay? Not only do you put it there, but rotate it 90 degrees and flip it.

**Dave Jones:** Okay? So what you're doing is you're describing something once and calling it up multiple times. Okay? If you think about that system, that's almost infinitely extensible. Whenever I get a different pad shape, and there's a whole bunch of them as you saw, if I get a different pad shape, I can just slot it in there, call it by a unique name,

**Dave Jones:** and then just call it up every time I need it. Okay? So the people who thought through this thing I think did a really brilliant job. So it's really great. And the standard is free. This business rotation is a big issue. Okay? If I pick something up out of a tape this way, and I rotate it 90 degrees,

**Dave Jones:** did I rotate it minus 90 degrees or plus 270? What happens if I put it on the bottom side of the board and rotate it 90 degrees? Did I go this way, or did I go that way? This is not a trivial exercise.

**Dave Jones:** Okay? This is defining. Right? And cast it in stone, if you like, so that there are no possibility of errors. Okay. So that's the standard. You call it up, it's free. Have a look at it. Okay? I'll have a... Let me show you the file itself.

**Dave Jones:** Oh. I digress. I need to digress. I got so wrapped in this thing, I had to show it. Okay. 0201... 0201. Okay. 0402. 0201. 01005. Right? Just last week, a new capacitor from Rata. 0.4 by 0.125 millimetres. Okay. They have trouble with this.

**Dave Jones:** Okay? And a lot of people are reluctant with this. What are we going to do here? Okay, this is about the size of a full stop on a sheet of paper. Okay? What are you going to do here? I had to show you that.

**Dave Jones:** Sorry. Yes. It's going to be a long time before I design something like that. Okay, first thing to do. We're going to... This is the file. Right? If you look at the file well, it's a test case, something rather than XML. Okay? This file is one of the test cases that you can get off the consortium website.

**Dave Jones:** They have six test cases generated by different CAD systems, right? So the file is presented like this. Right? It's very hierarchical. Okay? It's 44 megabytes long. Okay? So it's a reasonably serious file. If you want to look at it in text, you'll need a reasonably serious text editor.

**Dave Jones:** Okay? I have a thing called Notepad++. Search. Do a Google search on it. That handles this really well. Not only that, it's... You can shrink things. Right? So what I can do is I can view... Where are we? Collapse... Collapse level... Collapse level one.

**Dave Jones:** Right? So what I'm doing is this hierarchical file that has multiple steps. I can collapse it so I can look at the main headings. Okay? And I have a slow laptop. And I wish it was quicker. But it isn't. Either that or I did it wrong.

**Dave Jones:** I did... No, it's still working. Okay, so this is serious text editing, I guess. But if you look at the structure of this thing, very, very hierarchical. Okay? Describes a circle. Then it describes a rectangle. Numbers against them. Names, etc. and so forth.

**Dave Jones:** So it's sort of very stepwise. While that thing's working, it's probably using up every CPU cycle it can lay its hands on. This is a viewer. Free viewer from Downstream Technologies. Okay? This sucks. Right? To use this thing is like something nobody's ever seen in their lives before.

**Dave Jones:** It's a shame. At home, I've got the WISE viewer. W-I-S-E. That's from the consortium as well. You can download that for free. But you go through a little rigmarole to get a license. Okay? I've got a license at home. What I didn't realize was you need a separate license for your laptop.

**Dave Jones:** And so I, of course, sent off the file and I haven't had a reply. Okay. So I can't show you the WISE one. Let me tell you, the WISE one is infinitely better than this one. This one was almost certainly going to improve.

**Dave Jones:** Downstream Technologies are the people that have Vixie Gerber. CAM350, I think it is. They do those sort of processing tools. Okay. WISE do the same sort of stuff. And they did a much better job of this. So if you're going to use a tool, start with WISE.

**Dave Jones:** And I'm sure these people will catch up. But you can do sort of typical things. The highlighting sucks. I should be able to highlight a tool. And if you really look really closely, and I'm looking and I can't see it, that C14 is highlighted somewhere in there.

**Dave Jones:** Okay. I can zoom in. I tell you, I tell you. If this was cancer, this is almost like healthy but impossible to use. I'm joking. Okay. So you can just keep zooming in until finally it looks like something you understand. Okay. You can turn holes on and off.

**Dave Jones:** What do we do? Drills. Different sizes. I can turn them off. Somewhere in there is a... Come on. Just turn it off. Turn some of them off. So you get a look at the sizes. You can look at nets. There's a list of all of the nets in there.

**Dave Jones:** Technically, if I click on there, it's probably highlighted. Why doesn't it zoom to that? I don't quite know. So I'm not sure what they were thinking when this happened. You can look at layers. Change the colors of layers, et cetera, and so forth.

**Dave Jones:** I should be able to right-click there and say turn them all off. And then turn on only the ones I want to. No, they don't do that. So I've got to click them all off one by one, et cetera. The wise one, infinitely better.

**Dave Jones:** Okay. I just wish I had a license. Parts. You've got components. What have we got here? These are footprints. So I guess you can look at different types of footprints. They should be highlighted wherever they appear. And the components, typical. Okay. So that works a bit like a CAD system.

**Dave Jones:** Only much worse in this case. So I would imagine this type of viewer is going to be fairly common. It'll be like your PC Gerber or like your Gerber editor. You know, you do a CAD design. You've been looking at this for three weeks.

**Dave Jones:** Everything's perfect. The VRCs are clean. You call up the Gerbers just for one final check, and the very first thing you see is an error. Boom. Right there. Okay. You see things that a Gerber editor that you have missed in your CAD system

**Dave Jones:** because of the way that you're looking at things. You're looking at fresh eyes when you're looking at a Gerber file. Because you're just looking at one layer, generally. Looking at two layers is fairly complex and difficult to grasp. So suddenly you're looking at one layer with fresh eyes

**Dave Jones:** because you haven't seen it this way before. And that's where you start to pick up little strange things that the DMCs did not pick up. And we will get viewers like this that will actually do that for us also. Like we'll be able to turn things on and off

**Dave Jones:** that looks at assembly information, looks at fabrication information, testing information, and so on and so forth. That fabrication information, test information, should be able to isolate all of those things independent of our CAD system. Right? Because now we can look at it with fresh eyes yet again.

**Dave Jones:** And these viewers, no doubt, will also check the file, that 44 megabyte file, that's this one, 44 megabytes. It will go through all of that to make sure the syntax is correct. Okay, and if the syntax is correct, then it's going to go downstream without any problems.

**Dave Jones:** That's the plan. Okay. There's not much more to say with this because it's basically an extension of what we do with CAD, only much better. Now we've got the information, one big file, and that's all there is. And I'm not sure about the segmentation.

**Dave Jones:** I don't know that these viewers do that. But what I should be able to do is extract out of here only the information for the board fabricator. Because if you think about it, this entire file can go to a competitor and they can export it.

**Dave Jones:** Right in there. Yes, sir? I think the segmentation and export that you're looking for really comes from the CAD side. The CAD side? This is just allowing you to view the file that you output. So if you output only the fab information, then you'd be able to do that.

**Dave Jones:** If you output only the assembly information, you should be able to view the assembly information. Ah, so the CAD vendor is going to say that this is the file for just the fabrication. Correct. At this end, not at this end. That makes sense.

**Dave Jones:** Just on that, is it possible or is it intended that this file format be the native description of the PCB that your CAD program is actually using? It can be used that way, yes. At the moment, Metagraphics or Altium. Altium has its own structure.

**Dave Jones:** So the way that Altium describes its database appears in schematic files, PCB files, and then there's some background files to extract some sort of information. So it has a way of describing the way it works. And Metagraphics has the same sort of thing

**Dave Jones:** but in a totally different way. And Zookin and Cadence, etc. and so forth. So none of them are compatible. It's a format that everybody can use. In a neutral format which is text-based, XML-based, which people can use worldwide because it's well-defined. So in terms of what you're trying to say

**Dave Jones:** is it converts a CAD file to a neutral file, or it can do. PICAD years and years ago had what they called a neutral file format. And it was a completely text-based file. It was fairly hierarchical also. And you could take that but there were no translators

**Dave Jones:** to translate that neutral file format into something different, into a different CAD system. But this goes a long way to that. So if you can generate a file that carries the whole thing, then that becomes the file that somebody can manufacture your board from.

**Dave Jones:** I guess the point I'm thinking about is could you take one of these, if you had the complete description, could you take it into a CAD system, manipulate it, change components, whatever, and then send it off to the manufacturer? Right. Hang on, there's a proviso,

**Dave Jones:** there's a caveat. Let's say I'm sitting at Altium. And Altium's very happy to supply an output of 2581. But it may say no, I won't let you bring in a 2581. Suddenly the whole business of translating from one CAD system to another falls apart.

**Dave Jones:** Altium just might do an input also and just snatch, work away from the expedition, for example. I can almost bet my house on the fact that Metagraphics might have an importer. Happy to give an exporter, that's fine, because that's all downstream stuff. An importer, maybe not.

**Dave Jones:** Yeah, excuse me. Let me just add to that. At this conference you'll see where they created a file and read it into Zookin to do the changes that you're asking about and put the Zookin file right back into CADIS. So they've got importers?

**Dave Jones:** Oh yeah, they're importing back and forth. But we are talking purely at a manufacturer level rather than a schematic patch load level. I mean, this file does not actually incorporate what we regard as a human and it's not a true CAD format. And it probably, I assume,

**Dave Jones:** loses a whole lot of intelligence that are built into the parts and the design. Like design rules. Design rules, all that sort of stuff. Key bouts and all that sort of stuff that they can build into parts. Well, all the key bouts, all that stuff,

**Dave Jones:** that's all part of the 25-minute report. All that information is in the 25-minute report. The only one I'm not certain about is the schematic information itself, just the straight schematic. There's nothing in here that makes sense. Yeah, I didn't see anything and that may be that

**Dave Jones:** other 25 series thing. 2583 or 13 or something. Right. I'm not sure of that. But I know from the board side, you can archive the total construction including all of the test pictures, everything involved with manufacturing, assembly tests, all your test specs coming out of your CAE system,

**Dave Jones:** all captured within the format to be able to drive your ICT tests. So does, if we're talking about archive format, does it also capture things like 3D mechanical models because that's part of the archive because the mechanical engineers are going to need to sit there

**Dave Jones:** and deal with that. So is the format except, does it currently cover that or am I imagining it as an extension? I can answer that. Yeah, I'm not sure about, although I certainly have a step file reference somewhere in there, I'm sure. I could do a search

**Dave Jones:** but it would take too long. You're right about schematics that's something I hadn't thought of. Maybe it's not the all things to all people that we thought it might be. I'm not positive that it does it I just don't know. I didn't see

**Dave Jones:** anything like it. Anyway, it's a big file. Let me just see whether that thing's finished its ruminations. There it goes. Right, I've collapsed it down to the top level. Okay, so there's two lines in that top level. If I unfold it for the next one,

**Dave Jones:** I think I have to go to there. I spent another half an hour waiting. This laptop is slow. What I've done there is I've actually uncollapsed it once. Okay, here we go. Things like content, role function equals, I'm not sure what that means,

**Dave Jones:** function load full, level one, step name PCB, layer reference top, layer reference ground two, layer reference L10, et cetera and so forth. Coming down here we've got a dictionary standard equals inch, entry standard circle one, now we're starting to describe primitives. Okay, ID circle underscore

**Dave Jones:** one, it's a circle of diameter that, right, we define inch up here, this is inch. Okay, circle two is that many inches. Right, keep So once again we've missed an opportunity to actually get the world on the same page that we here are going to tell

**Dave Jones:** the United States to adopt metric. I think the simple logic for this is if you find everything in units of angstroms or nanometers or whatever you want to, you can at least get exact inch measurements. If you just find things in inch measurements

**Dave Jones:** you can't bring it back to exact. Gary, could I just point out that John is a stirrer. The documentation committee that's doing all the documentation, and it's not part of these slides, they are going through hammering out all the naming conventions and everything

**Dave Jones:** else from the schematic drawings down to the back drawings, the assembly drawings, all that documentation side in preparation for the 2581 committee to be able to now take that on the end. So I'm positive that it's not there yet. All that information is

**Dave Jones:** being formatted in such a way so that the consortium can then take it and start working this stuff in. So it's a work in progress. The more I'm thinking about this I know what's going on with that other group. And I'm sure that

**Dave Jones:** eventually in the metric and the conversion state I'm sure that's an issue with that. So I'm not sure about the way this file works. So you've got circles and if you keep going further you come to polygons. Here we have a shape and

**Dave Jones:** this is what we're calling that shape. For reasons I'm not quite sure why that happens. It's a contour which means I don't know what. Polygon, rectangle, there's a rectangle by centre. The rectangle centre is there and the width is that and the height is that.

**Dave Jones:** So they're describing all these basic real primitives. We saw a slide of some of those. If you keep going down further and further and further and further you come to the bit of materials. You come to things like this. It has a net point.

**Dave Jones:** X and Y is a layer reference's bottom. That's referring to a description that was at the top of the file. So it describes nets and it picks up shapes which we described up there somewhere. So it's calling all those shapes up by name.

**Dave Jones:** It'll start from the primitives and work its way up to the primitives, the genic stacks, the genic stacks, the performance, the arrays and do something that works its way up. Yeah, somewhere I've missed it. It's up there somewhere. So this is, what have we got

**Dave Jones:** here? Right, 1,034,976 and we've got the structure right at the end here. So if you look at this, there's level 1, 2, 3, 4, 5, 6, 7, I know there's other levels further up. So that's basically sort of it. But you know, there's

**Dave Jones:** a lot more about it describing a whole lot more stuff. Far smarter than any girl before I ever saw. Which started 30 years ago, turn the light on, draw it and then turn it off again. It's pretty dumb. Are there any questions about

**Dave Jones:** that? I don't want to make light of what you're saying, because you're quite right. There's a ball bomb. Let me see if I can find another one of those. I don't know what it was, but I know it was a bomb. I think

**Dave Jones:** it is. I think it is. I think it is. I think it is. I think it is. I think it is. I think it is. I think it is. I think it is. I think it is. I think it is. I don't have

**Dave Jones:** any cards for you. I think it is. I think it is. I don't have any cards for you. I think it is. I don't have any cards for you. I think it is. I don't have any cards for you. I think it is.

**Dave Jones:** I don't have any cards for you. I don't have any cards for you. I think it is. I do not have any cards for you. I don't have any cards for you. I don't have any cards for you. I don't have any cards

**Dave Jones:** for you. I don't have any cards for you. I don't have any cards for you. I don't have any cards for you. It's probably a serious issue. It's an absolutely serious issue. I have an ash of cards for you. I don't have any

**Dave Jones:** cards for you. It's an absolutely serious issue. I don't have any cards for you. It's an absolutely serious issue. I don't have any cards for you. It's an absolutely serious issue. I don't have any cards for you. It's an absolutely serious issue. I

**Dave Jones:** don't have any cards for you. It's an absolutely serious issue. I don't have any cards for you. It's an absolutely serious issue. I don't have any cards for you. It's an absolutely serious issue. It's an absolutely serious issue. I don't have any cards

**Dave Jones:** for you. It's an absolutely serious issue. I don't have any cards for you. It's an absolutely serious issue. I don't have any cards for you. It's an absolutely serious issue. I don't have any cards for you. It's an absolutely serious issue. I don't

**Dave Jones:** have any cards for you. It's an absolutely serious issue. I don't have any cards for you. It's an absolutely serious issue. I don't have any cards for you. It's an absolutely serious issue. I don't have any cards for you. It's an absolutely serious

**Dave Jones:** issue. I don't have any cards for you. It's an absolutely serious issue. I don't have any cards for you. It's an absolutely serious issue. I don't have any cards for you. It's an absolutely serious issue. I don't have any cards for you. It's

**Dave Jones:** an absolutely serious issue. I don't have any cards for you. It's an absolutely serious issue. I don't have any cards for you. It's an absolutely serious issue. I don't have any cards for you. It's an absolutely serious issue. I don't have any cards

**Dave Jones:** for you. It's an absolutely serious issue. I don't have any cards for you. I don't have any cards for you.
