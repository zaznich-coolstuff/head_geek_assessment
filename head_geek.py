def ask_question(question, yes_response, no_response, question_number):
    print()
    print("───────────────────────────────────────────────────────")
    print(f"ASSESSMENT QUESTION {question_number:02}")
    print("───────────────────────────────────────────────────────")
    print()
    print(question)

    while True:
        answer = input("> ").strip().lower()

        if answer in ["yes", "y"]:
            print()
            print(yes_response)
            print()
            return True

        elif answer in ["no", "n"]:
            print()
            print(no_response)
            print()
            return False

        elif answer == "banana":
            print("🍌 You found the Banana.")
            print("Sam specifically asked for this.")

        else:
            print("Please answer YES or NO.")


def main():
    print()
    print("╔═════════════════════════════════════════════════════╗")
    print("║                                                     ║")
    print("║                  TIME FOR YOU                       ║")
    print("║                                                     ║")
    print("║               HEAD GEEK ASSESSMENT                  ║")
    print("║                                                     ║")
    print("╚═════════════════════════════════════════════════════╝")

    print()
    print("Hi Sam.")
    print()
    print("You mentioned that 300+ people applied for your last job. I imagine It'll be the same for this position.")
    print()
    print("Rather than making you read all of those applications,")
    print("I've developed a more efficient tooling solution to help you find the best candidate.")
    print()
    print("You're welcome.")
    print()
    print("───────────────────────────────────────────────────────")
    print()
    print("Please answer YES or NO.")
    print("There are no wrong answers.")
    print()
    print("Except anything that isn't YES or NO. pls don't break my code I worked really hard on this. ")

    # Question 1: Curiosity
    ask_question(
        "You've been given a new piece of software you've never used."
        "\nDo you immediately assume someone else needs to teach you how it works?",
        "Hmm... That's one approach.",
        "Okay self starter! Let's go investigate.",
        1
    )

    # Question 2: Problem solving
    ask_question(
        "\nSomething isn't working."
        "\nDo you give up when the obvious solution doesn't work?",
        "...you've got some thinking to do.",
        "Excellent. Keep thinking, legend.",
        2
    )

    # Question 3: Breaking things
    ask_question(
        "\nYou've built something and it works."
        "\nDo you trust it immediately?",
        "Oh dear. Please take a real good look at yourself in the mirror.",
        "Nice. You're going to try to break it, aren't you?",
        3
    )

    # Question 4: Testing
    ask_question(
        "\nYou've tested something."
        "\nIt works."
        "\nYou've tested it again."
        "\nIt still works."
        "\nAre you finished?",
        "Wrong answer.",
        "Correct. Let's write some documentation so our teammates understand our work better.",
        4
    )

    # Question 5: Automation
    ask_question(
        "\nYou notice someone spends 30 minutes every week doing "
        "the exact same task."
        "\nDo you simply accept that this is how things are done?",
        "Sam would like a word.",
        "Good. Let's think how we can automate this.",
        5
    )

    # Question 6: Learning
    ask_question(
        "\nSam asks you to build something using a tool you've "
        "never used before."
        "\nDo you immediately decide you can't do it?",
        "This makes me sad.",
        "Excellent. You can achieve anything you put your mind to!",
        6
    )

    # Question 7: Ownership
    ask_question(
        "\nSam says: 'I've had an idea.'"
        "\nDo you write it down and hope someone else deals with it?",
        "That's not very Head Geek of you.",
        "You're really cool aren't you? Let's turn the idea into something real.",
        7
    )

    # Question 8: Organisation
    ask_question(
        "\nYou already have three projects on the go."
        "\nSam arrives with a fourth."
        "\nDo you immediately start working on it?",
        "I think you should prioritise, plan, communicate and finish up first.",
        "Great. Prioritise, plan, communicate and finish things, yeah?",
        8
    )

    # Question 9: Opinions
    ask_question(
        "\nSam has an idea."
        "\nYou think it's a terrible idea."
        "\nDo you tell him?",
        "Love this. Opinions are especially useful when accompanied by reasoning.",
        "I think you've misunderstood the job...",
        9
    )

    print()
    print("=" * 55)
    print("                 END OF ASSESSMENT")
    print("=" * 55)

    print()
    print("Thank you for completing the assessment.")
    print()
    print("We've reviewed your answers carefully.")
    print()
    print("Unfortunately, we've found a better fit for the role")
    print()
    print("We wish you the very best in your future endeavours.")
    print()
    print("In the interest of transparency, would you like to see the top canditate's results...")


    while True:
        answer = input("> ").strip().lower()

        if answer in ["yes", "y"]:
            print()
            print("Excellent. Here they are.")
            break

        elif answer in ["no", "n"]:
            print()
            print("That's unfortunate.")
            print("Transparency is important.")
            print("Please reconsider.")

        else:
            print("Please answer YES or NO.")

    print()
    print("=" * 55)
    print("                 TOP CANDIDATE RESULTS")
    print("=" * 55)

    print()
    print("Technical Curiosity....................................HIGH")
    print("Problem solving........................................HIGH")
    print("Desire to break things....................CONCERNINGLY HIGH")
    print("Automation instincts................................PRESENT")
    print("Ability to learn new stuff.....................DEMONSTRATED")
    print("Project Ownership.........................SUSPICIOUSLY GOOD")
    print("Independent thinking.............................YOU BETCHA")
    print("Opinions about Sam's ideas..............................YES")
    print("Sense of humour.....................................MASSIVE")

    print()
    print("Candidate identified:")
    print()
    print("                 Z A Z")
    print()
    print("Recommended job title:")
    print()
    print("                 HEAD GEEK")

    print()
    print("One final administrative requirement.")
    print()
    print("Please enter the secret word from the job advert.")

    while True:
        secret_word = input("> ").strip().lower()

        if secret_word == "banana":
            print()
            print("🍌 BANANA ACCEPTED 🍌")
            print()
            print("All done.")
            print()
            print("I would really, really, really like this job Sam.")
            break

        else:
            print("That's not the secret word. Try again.")


if __name__ == "__main__":
    main()