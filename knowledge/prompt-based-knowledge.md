# Tom / Russ Weekly — May 23, 2025  
*Google Meet*  
**Participants**: Tom McMillan, Russell Foltz-Smith  
**Attachments**:  
- Tom / Russ Weekly (Google Meet)  
- Transcript Notes by Gemini (2025/05/02 10:58 EDT)

---

## Summary

Tom McMillan discussed their project "Sail," a terminal inspired by Betty Miller's client-centered case theory, aiming to combine codex and the Agents SDK for knowledge processing, while expressing concerns about the architecture and the MCP protocol. Russell Foltz-Smith suggested focusing on leveraging LLMs and prompts directly, potentially simplifying the technical flow, and advised Tom on practical aspects like prompt storage and UI frameworks for their envisioned local white box application. The conversation also touched upon project naming, the evolving role of code, and Tom's shifting focus towards consulting, with both participants expressing excitement about future collaboration and shared perspectives on ethical consulting boundaries.

---

## Summary Details

### Project Introduction and Client-Centered Case Theory
Tom McMillan discussed a new project involving a terminal he is building. He was inspired by Betty Miller's work on client-centered case theory, which emphasizes the client's objectives, even if those include going to jail (00:00:00). Tom found this theory helpful for defining the purpose of user interaction within his terminal.

### Exploring codex for Computer Interaction
Tom experimented with codex to manage files on their computer and found the experience surprisingly effective. They questioned why this method isn't more widely adopted for interacting with computers. Russell Foltz-Smith suggested this aligns with some of Sam Altman's vision (00:03:22).

### Combining codex and Agents SDK
Tom outlined their hypothesis for the knowledge terminal, proposing to combine codex with the Agents SDK. They believe codex can handle tools, and agents can manage the knowledge process involving eliciting, instating, exchanging, and artifacting. However, Tom expressed uncertainty about how to effectively layer these two technologies (00:04:16).

### Architectural Concerns and the MCP Protocol
Tom detailed their efforts to create architecture diagrams for the project, focusing on the role of the codeex rust engine. They expressed concern about the MCP protocol layer and wanted to avoid unnecessary rebuilding or breaking existing systems. Tom felt a strong need to understand the architecture before proceeding further (00:05:41).

### Defining the Theory of the Case for the Terminal
Tom clarified their theory of the case, which involves combining codex, the Agents SDK, and their philosophical views on the flow of knowledge to create an exchangeable knowledge terminal. This includes categorizing agents into "speak" (on-demand) and "memory" (circulating) types, leveraging the existing Rust engine for local operation (00:06:54).

### The Role of MCP and Visualizations
Russell explained that MCP is a way to expose an application's functionality to LLMs through prompts, rather than a traditional UI. Tom mentioned using Mermaid and Figma for visualization, noting a preference for Mermaid but struggling with the syntax (00:08:11, 00:15:40). Russell pointed out the contrast between the linguistic nature of a terminal and the visual aspect of flowcharts (00:09:20).

### Argown for Logical Argument Visualization
Tom shared their discovery of Argown, an open-source tool for visualizing logical legal arguments. They integrated it as a backend service to allow users to visualize their arguments or case theories (00:09:20).

### Inspiration from Various Frameworks
Tom discussed the influence of advice from Russell to frame their beliefs within philosophy, strategy, and technology (00:10:34). They found inspiration in American psychoanalyst's reality testing, FBI charging documents, and Betty Miller's theory (00:13:22). The concept of exchangeable knowledge and experiences also resonated (00:14:43).

### The Nature of MCP as a Linguistic Interface
Russell emphasized that MCP enables applications to expose themselves linguistically, as APIs through prompts, rather than through traditional UI components (00:15:40).

### LLMs and the Evolution of Knowledge Processing
Russell explained that LLMs can now process large, structured and implied contexts, suggesting Tom's current architecture might be grounded in a pre-LLM paradigm (00:16:44, 00:21:47, 00:35:20).

### Shifting Focus to Prompts and LLM Capabilities
Russell encouraged Tom to consider letting prompts and the LLM manage more of the flow, suggesting prompt-generated diagrams and structures as an approach (00:23:53, 00:30:04, 00:33:48).

### Naming the Project "Sail"
Tom discussed naming the project "Sail" (SAIL) and purchasing getSail.net. Russell affirmed the creative potential of the name (00:27:00, 00:29:00).

### The Ephemeral Nature of Code in the LLM Era
Russell stated that code is becoming ephemeral in the age of LLMs and advised Tom to not overly rely on traditional versioning like GitHub (00:41:30, 00:42:26).

### Focusing on Prompts and the Codeex Engine
Tom outlined a plan to co-develop prompts with ChatGPT, using the codeex Rust engine at the system's core and a white terminal box as UI (00:42:26, 00:43:27).

### Practical Coding Questions: Prompt Storage and Frameworks
Tom asked about storing prompts as variables and integrating Python with the Rust engine. Russell advised keeping things simple and using Python for modeling (00:43:27, 00:44:41, 00:45:22).

### Clarifying the Role of Rust and Compiled Code
Russell explained Rust's speed and compiled nature, and how the knowledge process remains logically prompt-driven regardless of implementation (00:44:41).

### Interacting with the Codeex Engine Through Instructions
Tom clarified their goal to give custom instructions to codeex without rewriting core functions. Russell confirmed this as aligned with the Agent/MCP pattern (00:46:20, 00:47:12).

### The Concept of a Database as Files and Metadata
Russell explained PostgreSQL as just structured files with metadata, aligning this with prompt-based thinking. Tom found this insight clarifying (00:47:12, 00:48:13).

### Desired User Interface: A Local White Box Application
Tom described a simple white box interface in an Electron app from getSail.net. Russell confirmed Electron's suitability (00:49:11, 00:50:17).

### Considerations for Building a Desktop Application
Russell advised Tom to focus on core functionality before worrying about OS-specific packaging. Electron would help package at the end (00:51:12, 00:52:02).

### Front-End Frameworks and Immediate Testing Needs
Tom asked if front-end frameworks are needed now. Russell recommended skipping them early on and relying on Electron (00:52:02).

### Clarifying Terminology: React, Versel, and Electron
Russell clarified the roles: React = UI, Vercel = web host, Electron = local app builder. For a local-only app, Vercel isn't needed (00:52:53).

### Side Project and Inspiration
Tom mentioned starting a soccer side project and shared aspirations for a minimalist getSail.net homepage (00:53:58).

### The "Moby Dick" Nature of the Project
Russell likened the project to *Moby Dick* — endlessly evolving and never truly finished — which Tom agreed with (00:55:08).

### Shifting Motivation Towards Consulting
Tom prefers consulting over investor funding. Their near-term goal is a site exposing README files to attract clients (00:56:15, 00:57:20).

### The Nature of "Being Done" and Client Perception
Russell noted that “done” may be illusory for real creators, and clients often hire based on trajectory and insight (00:57:20).

### Shared Ground in Consulting Perspectives
Despite differences, Tom and Russell found common ground in their consulting philosophies (00:58:08).

### Excitement of Collaboration
Tom expressed excitement about working alongside Russell. Both recognized shared potential in their roles (00:59:13).

### Consulting Strengths
Russell noted that Tom may be better suited to profit-aligned consulting clients, while Russell tends to avoid exploitative work (00:59:13).

### Ethical Boundaries in Consulting
Both reflected on refusing work that was profitable but misaligned with their ethics (01:00:11).

### Appreciation and Well Wishes
Tom thanked Russell for friendship and mentorship. Russell reciprocated, ending the conversation with mutual appreciation and Friday well-wishes (01:00:11).

-------------------------------------------------------

## Foundations of a Prompt-Based Knowledge Architecture

### 1. Case Theory / Theory of the Case

*“We have to build a theory of a case together. Like, what is the point of talking to you today? And let’s not proceed until we have a theory of a case.”*  —Tom

*“That is my theory of the case: these two things combined plus my belief about the flow of a knowledge process that returns exchangeable economic knowledge.”* —Tom

*“You could see your argument or a visualization of your case theory... ‘Here are my premises. Here’s your theory of the case.’”* —Tom

- The conversation framed “case theory” as foundational—not just in law, but as a method of epistemic anchoring for knowledge systems. Tom integrates a client-centered lens (inspired by Binnie Miller), where user objectives may be non-obvious (“their objectives may be to go to jail”) and thus require interpretive alignment.
- Russ affirmed that this is a mental model for structuring the architecture: premise, proof, and purpose.
- Visualization tools like Argdown are positioned as helpful scaffolds for making the theory visible and interactive.

---

### 2. Knowledge

*“Exchangeable knowledge and experiences… that share button. That’s what it is.”*  —Tom (recalling Russ)

*“You're flowing out… how you want the human and the machine to proceed through a process.”*  —Russ

*“If you can’t translate all of your knowledge back into a prompt, then you’ve made nothing in today’s LLM-overridden world.”*  —Russ

- Knowledge, in Russ’s framing, is only real if it is *translatable*—linguistically, programmatically, and structurally.
- The value of knowledge lies in its ability to be shared, iterated on, and integrated across layers of interface—thus aligning with a kind of epistemological pragmatism.
- Russ introduces a stark warning: if you fail to prompt-ify knowledge, you’ve failed to make it computable or usable in the current era.
- There is also a metaphysical shift: from knowledge as stably codified (e.g., Hammurabi’s Code) to knowledge as ephemeral, iterative, and procedural.

---

### 3. LLMs

*“This is why the LLMs were such a breakthrough—they can take 17 pages of context and keep track of all the implied boxes and arrows within.”*  —Russ

*“LLMs have blown up what is an authoritative source. It is epistemological anarchism.”*  —Russ

*“Claude 4 just dropped yesterday… GPT-5 is coming… they’re going to collapse boxes.”*  —Russ

- Russ articulates that the key advantage of LLMs lies in their capacity to *hold context*, replacing traditional architecture with a transformer’s relational fluidity.
- The epistemic consequence is *anarchy*: previous notions of source, validity, and method are destabilized.
- LLMs are described as not modeling language per se, but rather regurgitating and transforming whatever textual garbage they’ve ingested—implying a kind of stochastic epistemology.
- The punchline: stop overbuilding structure that LLMs will inevitably collapse. Build the *prompt logic*, not rigid workflows.

---

### 4. Prompts / "Prompts All the Way Down"

*“It’s prompts all the way down.”*  —Russ

*“You’re saying… expose your application as a linguistic interface.”*  —Tom

*“What I want is 20 prompts that connect a user desire to a machine execution.”*  —Tom

- Prompts are elevated to ontological primitives. Everything—from buttons to UI menus to application logic—is reducible to a prompt.
- MCP (Model Context Protocol) exists to formalize prompt-based control surfaces for LLMs: APIs become linguistic APIs.
- Prompt chaining is envisioned as orchestration: user input → prompt → output → another prompt, until execution hits a system-level command (via Codex).
- This logic replaces legacy "applications" with composable prompt systems. “The UI thing is the box everyone wants—but you’re actually building a prompt network.”

---

### 5. MCP / Model Context Protocol

*“You have to describe what you do in language. You need to give me the codex for your application.”*  —Russ

*“MCP is just a way for you to describe the functionality of your app and expose your menus and your buttons in the form of prompts.”*  —Russ

- MCP is a method for making your application legible to an LLM.
- It sidesteps traditional UI/UX by providing a full linguistic specification—a prompt-based API.
- Russ sees MCP not as a framework, but as a *linguistic exposure layer*—an interface for agents, not humans.

---

### 6. Codex

**“Why doesn’t everybody just use codex to talk to their computer?”*  —Tom

“The Codex Rust engine is like the core engine that does this thing.”*  —Tom

*“I just want to give [Codex] a different set of instructions to perform those activities.”*  —Tom

- Codex is positioned as the *execution layer*—the runtime where the prompts become machine actions.
- The implementation language (Rust, Python) is considered irrelevant by Russ: what matters is the ability to compile logic to system-executable action.
- Codex is the final layer—when prompting and orchestration end, Codex *executes*.

---

### 7. Agents / Orchestration

*“Break down the agents into two categories: ‘speak’ and ‘memory’... speak is your on-demand agents, and memory is your circling agents.”*  —Tom

*“Can you get the system to build itself?”*  —Russ

*“Don’t keep adding boxes to your knowledge process… they will be collapsed by bigger models.”*  —Russ

- The orchestration layer is both architectural and conceptual: it connects user intention to executable action via agent roles.
- Tom’s taxonomy (speak / memory) begins to define temporal roles: reactive vs reflective.
- Russ’s counsel: resist the urge to over-architect. The real system is emergent—built through prompts, refined by use, and continuously co-evolving with model capacity.

------------------------------------------------

## Big Ideas

### 1. Exchangeability as Epistemic Standard

*“It’s that f***ing share button. That’s what it is. It’s exchangeable knowledge and experiences.”*
—Tom (recalling Russ)

- The idea that knowledge is only real if it is exchangeable is a recurring thesis.
- This isn’t about virality or communication—it’s about the moment when an experience becomes structured enough to be transferred, judged, reused, or priced.
- It introduces a knowledge economy framing: epistemic value is determined by its ability to circulate.

---

### 2. Epistemological Anarchism

*“There’s no method.”* —Russ (paraphrasing Feyerabend)

*“LLMs have blown up what is an authoritative source… we’re truly in anarchy right now.”* —Russ

- This isn't just a critique of legacy science or method—it's a radical reframing of how authority and process function post-LLM.
- Knowledge is not built by a universal method but by iterative, historically contingent, and now model-shaped practices.
- Your architecture can’t be static because the medium that generates and verifies knowledge is itself evolving.

---

### 3. Prompting as Ontology

*“If you can’t translate all your knowledge back into a prompt, then you’ve made nothing.”* —Russ

*“Every layer is the same. It’s the layers of the layer. It’s the same stuff.”* —Russ

- Prompts aren’t just API calls—they are the new ontology. Every “thing” (UI, database, agent) is ultimately a linguistically represented intention.
- Russ is guiding you toward the idea that prompting is not a means to an end—it is the structure of reality inside model-mediated software.

---

### 4. Architectural Futility (and the Moby Dick Metaphor)

*“Don’t get too hung up trying to come up with the perfect architecture.”* —Russ
*“This is your Moby Dick.”* —Russ

- You’re building a system (Sail) that resembles Ahab’s pursuit—not because it’s doomed, but because it is a relentless act of self-definition.
- Russ is reminding you to keep building, not to wait for epistemic closure.
- The key is to define enough to proceed, then let the system (and the world) evolve the rest.

---

### 5. Recursive Tooling: The System That Builds Itself

*“Can you get the system to build itself?”* —Russ

- This is a deeply recursive idea: the prompts you’re writing describe the system that eventually writes prompts.
- The tooling isn’t separate from the process—it is the process.
- This theme ties into dreams of bootstrapped AI, self-reconfiguring architectures, and what you’re calling “the white box.”