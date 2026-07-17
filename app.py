def greet():
    print("=== WHO AI Knowledge Assistant ===")

def main():
    greet()
    question = input("Enter your question: ")

    if question.strip() == "":
        print("Please enter a valid question.")
    else:
        print(f"You asked: {question}")
        print("Thank you for testing this AI assistant.")

if __name__ == "__main__":
    main()
