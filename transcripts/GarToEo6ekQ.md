---
video_id: GarToEo6ekQ
title: EEVacademy #9 - Implementing SCPI in C++
url: https://www.youtube.com/watch?v=GarToEo6ekQ
source: youtube-asr
timestamps: {"0": 1, "1": 17, "2": 36, "3": 56, "4": 82, "5": 109, "6": 128, "7": 143, "8": 155, "9": 170, "10": 195, "11": 213, "12": 235, "13": 252, "14": 271, "15": 291, "16": 309, "17": 323, "18": 340, "19": 353, "20": 369, "21": 387, "22": 406, "23": 422, "24": 441, "25": 453, "26": 473, "27": 491, "28": 507, "29": 522, "30": 538, "31": 561, "32": 580, "33": 602, "34": 620, "35": 639, "36": 656, "37": 671, "38": 688, "39": 704, "40": 714, "41": 732, "42": 751, "43": 770, "44": 788, "45": 808, "46": 824, "47": 840, "48": 854, "49": 868, "50": 886, "51": 906, "52": 925, "53": 943, "54": 962, "55": 977, "56": 991, "57": 1006, "58": 1017, "59": 1035, "60": 1054, "61": 1070, "62": 1084, "63": 1097, "64": 1116, "65": 1127, "66": 1150, "67": 1168, "68": 1187, "69": 1201, "70": 1217, "71": 1239, "72": 1253, "73": 1272, "74": 1287, "75": 1304, "76": 1322, "77": 1343, "78": 1361, "79": 1376, "80": 1394, "81": 1408, "82": 1420}
---

**Dave Jones:** Okay, so today we're going to be talking about SCIPPI. This is a um a set of commands that format the standard commands for program mobile instruments. SCIPPI commands are separated into these sections and they're separated by colons. So,

**Dave Jones:** here we have the first node, the second node, and the third node. And when you see these in um documents specifying how to communicate with instruments, you often get these strange syntaxes like you get these square brackets. And this means optional. And

**Dave Jones:** so this is something that we're going to have to implement. Um commands are always separated by these colons. Um each of these commands has two sections. It's a required section and an optional section. The required section is in uppercase and

**Dave Jones:** the optional section is in lowercase. Now, SCIPPI is not strictly case-sensitive. So, this is this command could be written as instrument or instrument or instrument. Those are all valid. And the required section is of course always required, but the optional section isn't. So, you

**Dave Jones:** could abbreviate that node as INST or INST or if you really really INST. And yeah. So, after the different nodes, you get these parameters. And parameters are always separated by commas. And so, here we have three different parameters, A1, A2, and A3. And

**Dave Jones:** this is quite typical. Before the parameters, you always see a white space, but it's an optional white space between them. It doesn't have to be there. So, this going to implement. So, let's So, I called um this a command before. Um

**Dave Jones:** I've called it a keyword here. Um and as I stated, it has two different sections, a required section and an optional section. And these are just strings. Um in an embedded system, you wouldn't use std::string. Um you would use a

**Dave Jones:** fixed-size array, and uh I'll talk about that at the very end for people who care. Um but if you just want a high-level overview, std::string is probably the easiest way to understand it. So, that's what I'm going to do.

**Dave Jones:** So, here we have a the required section being defined in the constructor and the optional section being defined in the constructor. And the optional section is optional because you might have a keyword which is uh something that is

**Dave Jones:** always required, such as the required commands in the skip These uh These are things like test and reset and identification. The all this entire command is required. So, this entire keyword is required. Um So, the optional section is actually

**Dave Jones:** optional. Um and keywords are quite simple. They consist of an an a required section at the start, which is the the capital letter section. And then, if that is found, you then can parse an optional section. And the optional

**Dave Jones:** section, it uh it but obviously by the name may exist or may not, and it always returns true. The function that looks for the optional section is always found because something that's optional always exists, kind of. So, we we return true after we find

**Dave Jones:** that. So, let's have a look at how that works. Now, all of these functions take two parameters, all of the parser functions that is. They take the block which is to be processed and an index which to start

**Dave Jones:** processing. And they always will return a boolean. That is whether it is found or not. Or alternatively um if it's not an optional we're talking about it's whether the index changes or not. So, here we have a keyword and the

**Dave Jones:** keyword consists of "hel" uh which is all required. So, "hel" is required. And then "lo", l o, which is optional. So, if we were to process it, we can say if keyword "hello" with an index and if if that is true, then we know

**Dave Jones:** it's found. And I'm going to step through that function to show how it works. So, when you enter the function we have two parameters. We have "hello" and we have the index. Index is initially zero. But when the required section is found

**Dave Jones:** the index um increments by the length of that that section. So, the the length of that section is three, h e l, 1 2 3. So, index is incremented by three, which means the start the character that will

**Dave Jones:** be processed next is at index three. So, and in this case, as you can see from this array, is an l, a lowercase l, which means it's optional. So, and then the optional section um begins processing at that index. So

**Dave Jones:** if it finds it, which it does, it increments it by the length of the section that it found. So, that's a five. Now it now the index is five, which means it was incremented by that that optional section of length two.

**Dave Jones:** 3 + 2 is 5. There we go. So and then it returns true because it found it. So that's sort of the structure of the um the skip command, but how did we actually determine whether we found a

**Dave Jones:** required section or an optional section? So let's step through it again. So we step in again and now we're going to step into required. So we've taken the keyword. So we're looking for h e l and that is required.

**Dave Jones:** And we're looking for it in the block h e l l o and we're starting at index zero. So here we start. We start by initializing a temporary index to zero and that index is going to go through the keyword and determine how

**Dave Jones:** much of the keyword is found and when it when it finds all of it, it will kind of indicate that. So here we go. Initially, we are checking h. The first letter of keyword and and then we calculate the block index,

**Dave Jones:** which is just how far are we into this for loop plus the offset, which is the starting index. So if if the block index is within the bounds of the block, then we can check the current letter, which is basically

**Dave Jones:** the the start point of the block for the first iteration, then the the next um one will be the next letter and the next one will be the next letter. So So we're saying is it the same letter?

**Dave Jones:** And if it is, if current is the same as required and it is, then we just continue. And we just churn through all these letters until either we reach the end of the keyword with index or the block index

**Dave Jones:** is greater than the block size, which means it breaks. And if it breaks, that means it basically wasn't found because we didn't completely find we didn't completely find the keyword before the block ended. So, then all we have to do is test

**Dave Jones:** whether the index is equal to the keyword size because if the index has incremented by the number of characters in keyword, then we know that we actually have found every character in keyword. And in this case we have. So, then all

**Dave Jones:** we do is say index plus equals that length of keyword. Index on its final iteration increments once more, so it actually equals the length. So, the length of it is three, so we expect it to increment to three. So,

**Dave Jones:** index is now three, which means that we have finished processing the first three characters in the block. There we go. Returns true, and that means that we can now start processing the optional section, and optional is basically identical to

**Dave Jones:** required, but it always returns true. So, it's it's really simple to implement. It calls the required function, ignores the result, and returns true. Yep. Great. That was easy. So, now you know how to kind of implement a parser for the skippy

**Dave Jones:** keywords. Now, let's work on the next section. Okay, so now we have to implement the node, and the node is actually just a keyword with a um with a colon in front of it. That's this. And the root node, the first node in Skippy,

**Dave Jones:** that's this node here, is actually optional. Um it's the only optional colon. Um so we have to have this bool is root flag. And you don't really have to understand templates to understand this. You just have to know it's either true or false

**Dave Jones:** when you create one of these classes. And if it's true, then the colon is optional. And if it's found, it increments the index past the colon. If it's not, it doesn't. And then that means we're free to start processing the keyword. And we

**Dave Jones:** process the keyword exactly the same as we did in our test case. So after we process the keyword, we know that we've found the whole the whole node. So we're free to increment the index. And then we return true because it is

**Dave Jones:** found. Now, if it's if it isn't the root node, the first node, then we're kind of fine to say the colon is required. So this means that it's always found and it will always increment index by one if it is found.

**Dave Jones:** So if the colon is found and then the keyword is found, then we can do the same thing as before. We're ready to that means the whole node is found and we can increment index.

**Dave Jones:** And and return true. So let's try that out. So a node and we're going to do a non-root node. It's a bit simpler. And a node consists of a keyword.

**Dave Jones:** And the keyword here is hello. We can probably just do equals. So, the node is going to be constructed from this keyword here. And we use the function exactly the same way. Only now we're looking for that colon.

**Dave Jones:** So, if we run it, it won't be found because we don't have the colon and we're going to step into it.

**Dave Jones:** And we step into it. And this is not a root node. So, it runs the required. So, the required colon in this block here is not going to be found. And we return false cuz we haven't found it. So,

**Dave Jones:** that's what should happen. Now, if we add a colon here, the required colon is now inside the block. And index is free to increment by one. And it has. So, now we start looking for hello and we're starting at index one now. And

**Dave Jones:** it's found and the index is now incremented to the end of the keyword. So, and we know the keyword's found, so we know we've found this node.

**Dave Jones:** So, Skippy is really just a bunch of nodes. And all we have to do to actually implement a full Skippy parser is use these nodes um in basically some if statements. So, in this case, we're going to look at

**Dave Jones:** these commands. We're going to look at sense. So, a standard command in Skippy would be sense. And this could be followed by a voltage or something. Um So, that's what we're going to do. And where I've added one more thing, which

**Dave Jones:** is query. And I'm just going to look at this function before we go through this. Query just detects the question mark character, increments the index if there is one, and returns true. So, that's all it does. So, we have three nodes in this.

**Dave Jones:** We have the sense node, which is got the required s e n s and with an optional e at the end. Then we've got a voltage node with the required v o l t and an optional a g e.

**Dave Jones:** And then finally, we have current, which is an with a required c u r r and an optional e n t. Here's the table. The required section and the optional section. Now again, this is not case sensitive. So, these

**Dave Jones:** could be upper or lower case. Okay. So, how do we actually process a command? Well, first we have to take the command as an input. C in just gets gets a string. And then we pass the string to our sense

**Dave Jones:** node. Our sense node is like a function um And the sense node takes the input and the index just as before. And if it finds it, that means we know that we've found this section. We found this s e n s e or s e n s or some

**Dave Jones:** variation of capitals and lower cases. So, if we've done that, we're free to go to the next section. So, because we're looking for sense voltage or we're looking for sense current, we're looking for either or either of those,

**Dave Jones:** but not both. We have voltage. If that's found, then we process that. E- else if current is found, we process the current. So, it's quite simple. Um and then so, in inside the processing of those two, it's either a query or a um

**Dave Jones:** command. Um And the query in this case is just going to print whether it's a query or not with a question mark. But usually this would mean that you would either either return a value or assign a value. So, it's it's relatively simple.

**Dave Jones:** So, let's have a look. Let's run this program. All right. So, here we go. So, if we step through this program with the inputs sense voltage then our input is is what we just entered into the console. And our index starts at zero.

**Dave Jones:** And if we find the word sense, and because it's in here we will then index increments to the end of the word sense. And then we're ready to process the next section of the command. So, sense here ends at character five. So, we're now

**Dave Jones:** ready to process from character five onwards, and that's why index is five. So, now we don't know whether it's voltage or current. So, we have to test it. And this if statement tests that. So, if the voltage is found, it'll run

**Dave Jones:** this. So, it does because it is there. And it moves the index to the end of the word voltage, which is 13, the null character inside the raw array. We're at the right place. And then we just determine whether it's

**Dave Jones:** a query or not. Now, it did not end in a question mark which was that query thing we talked about just before. So, it does not print a question mark. This is an if statement in in a single

**Dave Jones:** line. This says, if this is true, do this. Otherwise, do this. The colon separates the two. Um it's called a ternary operator. It's kind of weird. Yeah. Okay. So, then we just print it. And there we go. Sense voltage found.

**Dave Jones:** Now what about current? What about current? So, let's just continue through. So, since current So, of course, this is the same at the start. It's common between the two. So, we're not going to process since again each time. That would be pointless.

**Dave Jones:** We're going to process it once. And it will continue to the next node, and it will go to its child nodes. That That's these nodes. So, voltage wasn't found. So, index stays at five, which is at the end of the word

**Dave Jones:** since at the the colon. Here we go. So, now we're going to process from five onwards starting with the colon. So, this time I'm going to step in so you can see kind of what it does. So, it says, is the the colon there? I

**Dave Jones:** mean, it has to be cuz it's not a root. At So, is it at character five inside the block? It is, and now we're ready to search for the keyword. The keyword is the current. So, if current's found,

**Dave Jones:** then we're going to continue. We're going to to assign the new end index to the parameter P index. And then we return true. Then we know, finally, we have current. And that's how Skippy's command That's how Skippy interpreted. And

**Dave Jones:** um just as some variations. So, if you didn't If you admitted the sem- the colon at the front, it should still work.

**Dave Jones:** No problem. And if you admit the optional characters, it should still work. And um if you now end it with a query, it works still. But, this time it's detected that it is a query. So, this is the basic structure of a Skippy

**Dave Jones:** interpreter. It's quite lightweight with the exception of using the standard string. And it's something that you can put on your own devices, your own test equipment, which makes it much more usable for people who aren't um aren't you.

**Dave Jones:** So, if you look at the Micro Supply SCPI specification, we basically have everything that we talked about here before. Um we have an optional semicolon at the start. Optional things are put around square brackets. Um and then we can have source, voltage,

**Dave Jones:** and then we can assign it a value, or we can ask for what it is. Now, SCPI is typically done by serial, so that's what we're going to do. That's what we've done. So, let's try it out. So, if we input source

**Dave Jones:** colon voltage, that's the the source node, then voltage with a single parameter of 1.2 V, it will set the source voltage to 1.2. It doesn't return anything here. But, we can query whether it was correct, and this is usually a good

**Dave Jones:** idea. So, there we go. We It returned 1.2 when I queried the voltage. How about source current? Source current. And we're going to assign 0.123 because that's awesome. Or something. Source current query should return the same thing, and

**Dave Jones:** it does. So, this is basically a real-world example of a SCPI command interface. So, of course, it's not case sensitive as well as tests weren't.

**Dave Jones:** It does exactly the same thing. So, yeah, it's a really useful interface. And if there's there's a few Here's the required commands that we have implemented, and this is why it says SCPI-ish because SCPI requires all of them. All of them, but we

**Dave Jones:** there's no practical use of implementing all of them. So, for the minimum viable product, we are not doing that. Maybe we'll do it later. Um so, now the required commands start in a star. That's the only difference. And they have to have that star, I

**Dave Jones:** think. So, here we go. IDN with a query. And there you go. Returns this query string. Build. So, if you want to get the build, you could query it. So, the build the query date of this is the the build date

**Dave Jones:** is October 12th. And the build time was at 6:44 uh 40 seconds. So, this these are this is a good command interface. It's something that is human-readable. Um it's something that that is easy to extend and build build

**Dave Jones:** applications with because all you need to do is send a simple string to the device through the serial interface. I mean, serial serial interface libraries are common as mud and yeah. If we now type this voltage command with a different voltage as you are

**Dave Jones:** seeing, uh yeah. Then we see it changes. And we can of course query it.

**Dave Jones:** And it returns the voltage. And you've got all these other commands. And you've got all these other commands. There's you've got you've got some measurement commands. You've got some output commands. Um and the structure of these commands might change. I mean, this is pretty

**Dave Jones:** preliminary. I probably should have written preliminary in the document name, but this is what we got. So, hey, cool. Okay, well, hope you enjoyed the video. Hope you learned something and I hope this kind of pattern of parsers is

**Dave Jones:** useful to you because writing parsers can be a real pain if you don't have a standardized pattern and this is what I use generally. So, hope you have a good day. Have a good one. Bye.

**Dave Jones:** In production, I don't use stood string. I use a replacement using template metaprogramming. If you want to see how to do that and you want to go full node with C++ which you probably don't, the link is down below. Consider this a

**Dave Jones:** warning.
