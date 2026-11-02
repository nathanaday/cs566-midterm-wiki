---
name: run
description: How to run a Yami session. Read its input, load its skills, call its agents, follow its policies, deliver its promises, check the work, and expect a review.
---
# Run a Yami session

A Yami session is one piece of work, and one markdown document in the vault. The message that invoked this skill names the session document and gives its context: the instructions, the policies, the promises, the skills, the agents, and the articles. The working directory is the vault, and paths are relative to it.

1. **Read the input.** The session's input is its Request section, which says what to do, its session properties, and its articles. A person writes the Request section. Yami writes the properties and the Deliverables, Progress, and Review sections. Do not edit the session document.
2. **Load the session's skills.** Load the first skill of the message before you begin, and load the others when you need them. To load a skill, invoke it by its command, `/<module>:<skill>`, or read the `SKILL.md` in the folder that the message gives. A skill that the message gives in full is loaded already.
3. **Call an agent for work that needs a fresh context,** such as a second look at your work. Call the tool `yami_agent` with the agent's name and a task that holds everything it needs. The agent returns its final message, and you decide what to do with it. The message lists the session's agents.
4. **Follow every policy.** A policy is a rule for all of the work.
5. **Deliver every promise.** A promise names a deliverable, and where it goes. In a promise, `{{session}}` is the session's name, and `{{field}}` is the value of a session property.
6. **Check the work before the turn ends.** Call the tool `yami_check` with the session document's path. It runs the checks of the promises and returns each result, and it records nothing. Fix each unmet promise, and check again.
7. **Expect a review.** After your turn, Yami checks the promises. When the checks pass, a reviewer judges each policy, and each promise that has no check. The reviewer works in a new conversation, and does not change files. When a check fails, or the reviewer finds a broken policy or an unmet promise, you get the reasons as the next message. Fix what they name.

End your turn when the work is done and the checks pass. Say in your last message what you did, and which files you changed.
