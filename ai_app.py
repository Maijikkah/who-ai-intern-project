def load_knowledge():
    knowledge = {}

    with open("knowledge_base.txt", "r") as file:
        for line in file:
            line = line.strip()
            if ":" in line:
                key, value = line.split(":", 1)
                knowledge[key.strip().lower()] = value.strip()

    return knowledge


def chatbot():
    knowledge = load_knowledge()

    print("=== WHO AI Assistant ===")

    while True:
        question = input("Ask a question (or type 'exit'): ").lower()

        if question == "exit":
            print("Goodbye!")
            break

        found = False

        for key, answer in knowledge.items():
            if key in question:
                print(answer)
                found = True
                break

        if not found:
            print("Sorry, I don't know the answer yet.")


if __name__ == "__main__":
    chatbot()
