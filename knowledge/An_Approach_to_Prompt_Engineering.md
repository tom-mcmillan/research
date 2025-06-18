Between the two pictures a change had taken place which was like a revolution in artistic perception. El Greco had opened wide the door to all that the future was to experience; he had replaced knowledge of an event, its pictorial narrative, by a direct appeal to the emotions, by a drama in perpetual progress. From the formal viewpoint he had broken the harmony of the proportions, subjugated space, and built up his own personal universe from elements of reality.

His audacity seems all the greater for the fact that he had nothing to back him up in his purpose, that he provoked no echo, not even feeble imitations. The great innovators in art, even the most revolutionary of them, even those who departed most from the present and who aimed the highest, knew that on the steps they were cutting, so to speak, in a glacier another would set his feet;

-  Antonina Vallentin

- Alskdjf

Due to my work, I speak about Artificial Intelligence frequently.

Though the questions come in many forms, I believe they are all asking the same simple question: how do I talk to a computer?

I have decided to write a brief answer to that here. My hypothesis is that artificial intelligence is a new material that will upfit or replace nearly

- A Shift in Perception

- El Greco

- Long before Impressionism and Expressionism, before

- Picasso, Degas, and Cezanne, a Greek artist named “El Greco” painted The Vision of Saint John for a small hospital on a hill in Spain.  Twentieth century critics, like Antonina Vallentin, would marvel at how, “Emotion seems to have shed the burden of visible matter and produced its own mysterious equivalent in paint,” able to express a “mood that no other artist had ever attempted to translate into pigment.”  El Greco painted The Vision of Saint John in 1608, and it would take nearly three-hundred years for painters to adopt his language and describe with pigment how the world felt. When they finally did, they called it Modernism.

Fig. 1. El Greco (Domenikos Theotokopoulos), The Vision of Saint John, oil on canvas, ca. 1608-14, Metropolitan Museum of Art, New York, .

- Transformation change

The funny thing about history is that the exact nature of a transformational change to society — be it agrarian, monetary, artistic, or technological — is impossible to fully understand in the moment. For the person who first monetized crops, what would he think of the Commodities Exchange? To a Roman, holding a silver coin stamped with the image of Tiberius, would they pass out before you finished explaining collateralized debt obligations? For the patients at the Hospital of Saint John the Baptist, where El Greco’s painting hung, could they imagine Cubism, and Picasso saying it was El Greco who was the precursor to modern art? Of course, no.

It's just the same with AI. For us who use ChatGPT, how should we understand it? What can we understand of it? I will attempt to answer these questions as best I can and introduce you to a fundamentally different world in which you will naturally and efficiently interact with any computing device, any kind of mechanical device, or anything with a chip in it — a world in which everything is directly addressable through ChatGPT and its successors.

- How this article works

The general design of this article is as follows: I will give you a brief overview of ChatGPT and Large Language Models (LLMs), and then present you with my idea that interacting with computers, in this new way, has a certain style to it that we must understand if we are to have any success. That style informs and shapes how we “prompt engineer”, or whether such a thing is even needed at all.. Following that, I’ll introduce some dialectic methods for ChatGPT, I’ll try to explain what an LLM actually is, and we’ll write a style guide, together, for the non-deterministic conversations we have with computers, today and in the future.

Most of all, I hope this article answers your specific questions about using AI in your everyday life. To that end, I’ve used metaphors sparingly (to save you time), quote others frequently (who are much smarter than I), and provide many headings (so you can skim). Though I call this an “article,” a better term may be field notes — my record of observations and reflections while using and building AI technology in my personal and professional life. In many cases, I am wondering the same thing as you.

- The Design, Form, and Style of Conversational AI

- Large Language Models (LLMs)

All the conversational AI tools we use, such as ChatGPT, Gemini, or Claude, are web interfaces for Large Language Models (LLMs), which are complex machine learning models trained on vast amounts of text. LLMs generate responses by predicting the most likely next word or phrase based on patterns learned from billions of text examples. Consider the following example

When I hear rain on my roof, I _______ in my kitchen.

An LLM determines the probabilities of different words or sequences of words to replace that underscore. For example, a language model might determine the following probabilities:

cook soup 9.4%

warm up a kettle 5.2%

cower 3.6%

nap 2.5%

relax 2.2%

...

OpenAI’s LLM is called GPT, and the web interface they built for it is called ChatGPT.

LLMs are inherently non-deterministic, meaning that given a particular input from you, they may return significantly different outputs. The output they choose is the result of a phenomenally complex process, which is improved daily. If you use ChatGPT often, you may be able to sense these improvements, yourself.

So, what are we to do with a non-deterministic computer?

- ChatGPT

I believe the primary value of conversational AI tools like ChatGPT, Claude, and Gemini is their ability to assist in formulating your own knowledge, thoughts and expressions. They do this through a dialectic — a critical investigation of truth through reasoned argument, often by means of dialogue or discussion. This may sound like Hegel, Marx, Kant, or Socrates. But they all were after the same idea, which is naming the process by which knowledge or history is created. I think ChatGPT is doing something of the same thing, and I’ll call it, Socratic Computing, which is the formulation of knowledge, thoughts and expressions through non-deterministic computing, or conversational AI.

- Style

My thesis is that LLMs should be understood as a form of non-deterministic computing, which has instantiated a new method for creating knowledge, called Socratic Computing. I believe our job today is to master Socratic Computing. I believe we do that by mastering the style of how we speak to them. This article is an attempt to describe the elements of that style.

Crafting a complete guide is an ambitious task, and I won’t be able to finish it here. But where I leave off, I hope you, the reader, will continue.

Fig. 2 Diagram showing hierarchal structure of language. This structure is relevant to prompt engineering, as interacting with LLMs requires understanding and leveraging these linguistic levels to shape responses. Source:

- LLMs: Predicting the Next Best Word

- Technology

To explain how LLMs like GPT work, I’ll refer to an excerpt from Stephen Wolfram’s article, “What is ChatGPT Doing and Why Does it Work?” Wolfram describes the process in a way that makes it clear:

The first thing to explain is that what ChatGPT is always fundamentally trying to do is to produce a “reasonable continuation” of whatever text it’s got so far, where by “reasonable” we mean “what one might expect someone to write after seeing what people have written on billions of webpages, etc.”

So let’s say we’ve got the text “The best thing about AI is its ability to”. Imagine scanning billions of pages of human-written text (say on the web and in digitized books) and finding all instances of this text—then seeing what word comes next what fraction of the time. ChatGPT effectively does something like this, except that (as I’ll explain) it doesn’t look at literal text; it looks for things that in a certain sense “match in meaning”. But the end result is that it produces a ranked list of words that might follow, together with “probabilities”:

Fig. 1. Ranked list of words, together with their "probabilities" for the next word in the sentence, "The best thing about AI is its ability to" taken from Stephen Wolfram's "What Is ChatGPT Doing … and Why Does It Work?"

And the remarkable thing is that when ChatGPT does something like write an essay what it’s essentially doing is just asking over and over again “given the text so far, what should the next word be?”—and each time adding a word. (More precisely, as I’ll explain, it’s adding a “token”, which could be just a part of a word, which is why it can sometimes “make up new words”.)

But, OK, at each step it gets a list of words with probabilities. But which one should it actually pick to add to the essay (or whatever) that it’s writing? One might think it should be the “highest-ranked” word (i.e. the one to which the highest “probability” was assigned). But this is where a bit of voodoo begins to creep in. Because for some reason—that maybe one day we’ll have a scientific-style understanding of—if we always pick the highest-ranked word, we’ll typically get a very “flat” essay, that never seems to “show any creativity” (and even sometimes repeats word for word). But if sometimes (at random) we pick lower-ranked words, we get a “more interesting” essay.

The fact that there’s randomness here means that if we use the same prompt multiple times, we’re likely to get different essays each time. And, in keeping with the idea of voodoo, there’s a particular so-called “temperature” parameter that determines how often lower-ranked words will be used, and for essay generation, it turns out that a “temperature” of 0.8 seems best. (It’s worth emphasizing that there’s no “theory” being used here; it’s just a matter of what’s been found to work in practice. And for example the concept of “temperature” is there because exponential distributions  happen to be being used, but there’s no “physical” connection—at least so far as we know.)

- Best Practices

Wolfram’s explanation sheds light on the core mechanics behind GPT. Instead of producing fixed, deterministic outputs, these models rely on probabilities, selecting the next word based on patterns and context. Randomness plays a role, too—introducing variability and creativity into the responses. That doesn’t mean it’s invalid, or wrong, or bad, or we should ignore it or not use it—it just means you need to know that you’re dealing with something that isn’t human, It’s not even human-like. It is statistical in how it’s dealing with language.

Fig. 2. A visualization of ChatGPT deciding which word to pick, from the “fan” of words, in vector space. A word’s relative “closeness” to the previous word makes it a better choice. Taken from Stephen Wolfram (2023), "What Is ChatGPT Doing ... and Why

Fig. 3 Here’s a 3D representation, going for a total of 40 steps:

So, what does this mean for us? What does it say about the style we should adopt when talking to computers? If we’re writing a style guide for interacting with LLMs?

Fig. 4. 3D Meaning Space Diagram Inside ChatGPT any piece of text is effectively represented by an array of numbers that we can think of as coordinates of a point in some kind of “linguistic feature space”. So when ChatGPT continues a piece of text this corresponds to tracing out a trajectory in linguistic feature space. Here’s an example of how single words (here, common nouns) might get laid out if we project such a feature space down to 2D.

- ChatGPT: A New Unit of Cultural Production

GPTs give us all a new “unit of cultural production” that goes beyond the book, the music recording, the poem, the algorithm, the program, etc. We have these new “units of GPT”. (Wolfram calls them “computational essays”). GPTs do not replace any previous unit of culture. All additive.

-  Russell Foltz-Smith

- The conversational form

I believe the primary value of conversational AI tools like ChatGPT, Claude, and Gemini is their ability to assist in formulating your own thoughts and expressions. The experience is unique for two reasons: they employ a Socratic modality and operate on non-deterministic principles. By Socratic modality, I mean the conversation takes the form of a dialectical exchange—questioning to explore and logically examine ideas, rather than searching for immediate answers. By non-deterministic, I mean the outcome isn't fixed by the input; the same question can yield different answers based on context, much like human conversation.

Why does this happen? ChatGPT is simply an interface for OpenAI’s LLMs, such as GPT-4o and others. These are vast models trained on enormous amounts of text—the human knowledge corpus. When you converse with ChatGPT, you’re interacting with these models in a non-deterministic way, meaning the conversation may surprise, excite, or even disappoint you, just like an interaction with another person.

This variability often leads users to two questions: What should I do with this? and How do I do it? Many turn to prompt engineering to bring more predictability to their interactions with AI. By using established frameworks and libraries of prompts, people aim to “tame” the non-deterministic nature of these models. But I ask: Is predictability what you really want?

- The flow

In my view, the best approach is not to direct the AI with rigid commands like “write a paper on Socrates,” but to engage in a flow with it. This flow begins by priming the model—setting up the conversation with context or framing your thoughts. For example, instead of issuing a command, you might start with an intro like,

You can see this in action in some ChatGPT responses below (Fig. 1-3)

Fig. 5  ChatGPT-4o response to “I’m looking to have a socratic exploration of some topics in my mind. Please try not to make up facts but maybe be imaginative with me in understanding things” (October 2024)

Fig. 6 ChatGPT o1-preview response to “I’m looking to have a socratic exploration of some topics in my mind. Please try not to make up facts but maybe be imaginative with me in understanding things” (October 2024)

Fig. 7. ChatGPT 4-o with canvas response to “I’m looking to have a socratic exploration of some topics in my mind. Please try not to make up facts but maybe be imaginative with me in understanding things” (October 2024)

- What conversation do I want to have?

As the examples show, subtle shifts in how you begin a conversation can change the trajectory entirely. Asking “What do you think about my family?” is quite different from “How do you think about families?” In both cases, you're initiating a dialogue rather than seeking a definite answer.

So, when interacting with tools like ChatGPT, start by asking yourself not “What answer do I need?” but rather “What conversation do I want to have?” Now we have the beginnings of a style.

- An Approach to Style

- Prompts

Prompts – the written request you make to an AI model to get a specific response – have become our sole obsession in deciding how to talk to computers. We've even coined a term for those skilled in crafting them: prompt engineers.  But I think good prompts are simply records of good style; they reflect it but do not define it.

- An approach to style

In 1918, Williams Strunk, a professor at Cornell, published a book called The Elements of Style, whose purpose, he said, was “to cut the vast tangle of English rhetoric down to size and write its rules and principles on the head of a pin,”  It’s perhaps the most famous book on writing.

In 1959, a new version of the book was published, with additions by E.B. White, Strunk’s student at Cornell. White added a chapter called, “An Approach to Style.” He said he was, “setting forth my own prejudices, my notions of error, my articles of faith” on writing.

We find ourselves in a similar moment with Socratic computing—the practice of conversing with AI. Like Strunk’s clear instructions for writing, we have tools like prompt engineering to guide our interactions with AI. But much like White’s emphasis on style over rules, I believe true mastery of conversational AI goes beyond prompt engineering. It’s about developing a style of interaction that is adaptable, responsive, and conversational.

Socratic computing is still in its early stages. We don’t yet have a comprehensive guide on how to do it perfectly, but we can start to define its style. Good Socratic computing doesn’t rely solely on well-crafted prompts—it relies on the ability to engage in a flexible dialogue, one that encourages exploration and creativity.

Fig. 8. Diagram of non-deterministic computing session types. There are many ways to interact with ChatGPT. Giving it a long prompt and copying-and-pasting its response is one of sevel options. Another is Socratic Computation.

- My Field Notes

- The role of prompt frameworks

While prompt frameworks—templates for creating effective prompts—are useful tools, they don’t define the full potential of conversational AI. There are many such frameworks, all with minor differences, but what really matters is the shape and style of the prompts we use, and how they foster a deeper, more Socratic interaction with AI.

Take for instance the framework in Figure 10. It offers a structured approach: defining the role of the AI, giving it instructions, setting clear steps to follow, identifying the end goal, and providing narrowing context. These are important elements, not because they force the AI into a specific response, but because they create a conversation that invites thoughtful, contextual answers.

The best interactions with AI happen when prompts serve as  the beginning of a conversation, rather than a fixed set of instructions. Your goal isn’t to extract a single, static answer but to guide the AI in a process of dialogue and discovery.

- Article-Writing Prompt Example

Figure 2 offers a prompt used to guide a model in writing a Substack article. This is a prompt I wrote for my work. I generated this prompt by looking at some writing by Derek Parfit, who I think has a concise, and clear style. In fact, I gave GPT the introduction to his book, Reasons and Persons, and asked it why it was so good. An hour later, we had a prompt.

The prompt lays out a structured process to extract essential information from the user in stages, ensuring that all necessary variables—such as the main themes, point of view, references, and rationale—are captured through a guided conversation. The model is then tasked with constructing the article based on the extracted details.

The prompt is successful because it achieves clarity on the user’s goal through conversation. By prompting the model to ask relevant questions step-by-step, the user is guided into a deeper exploration of their ideas, ensuring that nothing is missed. This approach reflects the key principle that most professional writing doesn’t emerge fully formed—it evolves through a process of inquiry and refinement.

This method allows the user to clarify their ideas while maintaining the core principles of simplicity and sincerity and can be used to improve not just what we write, but how we think about writing.

- Asking better questions

One of the most powerful aspects of Socratic computing is how it can help us structure our thoughts and refine our inquiries, especially when dealing with complex topics. Consider a scenario where you're trying to decipher a technical paper on the effects of climate change on real estate pricing. The questions you ask, and the way you ask them, shape the quality of the answers you'll receive from an AI like ChatGPT.

Take, for example, this detailed prompt in Fig 14. This is a perfect example of a Socratic approach to conversational AI—asking a series of thoughtful, structured questions that not only aim for clarity but guide the conversation toward a deeper understanding. The prompt invites the AI to break down the paper into digestible pieces, which can then be explored one step at a time. It’s not a simple command to summarize the paper but an invitation to engage with the material methodically and analytically.

What makes this prompt so effective is the way it’s designed to lead the conversation. Rather than simply asking for an overview, it directs the AI to look at specific aspects of the paper—data sources, hypothesis, analytic methods, and equations—and consider how they interact. This layered questioning aligns with the principles of Socratic computing, where the goal is not just to extract information but to guide a process of inquiry and refinement. The result is a more collaborative, in-depth dialogue between the user and the AI.

Figure 11. This is a prompt from a session with ChatGPT-4o. We are priming the model for a session, in which we will exchange ideas, back and forth, about the PDF I’ve supplied.

- How Should We Think about Thinking?

Last year, I called a friend who advises a major tech company to discuss the growing questions around intellectual property, specifically ChatGPT’s ability to mimic the style of famous writers and artists. My friend had helped build one of the most widely used Large Language Models (LLMs), and I was curious to know his thoughts. He was uncertain and circumspect saying, “Today, I trained ChatGPT to do vector math in Klingon. Who owns that? Me? OpenAI? Gene Roddenberry?” He sighed and laughed. “Lawyers will make a lot of money answering that question in the next couple years.”

Prompt engineering is not a science with fixed rules; it's an art that requires experimentation, iteration, and creativity. At its core, interacting with large language models like ChatGPT is about embracing ambiguity, engaging in conversation, and evolving our thinking.

- Conclusion

While it might be tempting to view these AI tools as replacements for our own creativity, their real power lies in the Socratic conversation. They can inspire us, sharpen our ideas, and help us articulate complex thoughts—but only if we know how to converse with them. The true art of prompt engineering is not in trying to make these models perfect but in understanding their nuances and using them to amplify our own creative processes.

But ultimately, you still have to do the thinking.

- Helpful Resources

Amatriain, X. (2024). Prompt design and engineering: Introduction and advanced methods. arXiv.

Foltz-Smith, Russell (2020, December 13). GPT-3 linguistics 101: A multi-part series (This is part 1 on structure). Medium.

Google AI. Prompting strategies. Google Gemini API Documentation. Retrieved October 23, 2024, from

Google. NotebookLM. Google. Retrieved October 23, 2024, from

OpenAI. Prompt engineering. OpenAI Documentation. Retrieved October 23, 2024, from

OpenAI. OpenAI cookbook. OpenAI. Retrieved October 23, 2024, from

OpenAI. Prompt generation. OpenAI Documentation. Retrieved October 23, 2024, from

OpenAI. Chat playground. OpenAI. Retrieved October 23, 2024, from

snwfdhmp. Awesome GPT prompt engineering. GitHub. Retrieved October 23, 2024, from

Wolfram, Stephen. (2023, February). What is ChatGPT doing and why does it work? Stephen Wolfram Writings. Retrieved October 23, 2024, from