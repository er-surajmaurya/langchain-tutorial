from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama


def main() -> None:
    information = """
    Elon Reeve Musk is a businessman, industrialist, and former public official.
    He is the CEO and largest shareholder of Tesla and SpaceX. He has been one of
    the wealthiest people in the world and has built a career around technology,
    space exploration, and electric vehicles.

    Musk was born in Pretoria, South Africa, and later moved to Canada and then the
    United States. He studied at the University of Pennsylvania and later founded
    multiple major companies, including Zip2, X.com (which became PayPal), SpaceX,
    Tesla, Neuralink, and The Boring Company. He also acquired Twitter and rebranded
    it as X.

    He is known for ambitious goals such as reducing the cost of space travel,
    accelerating sustainable energy, and developing advanced AI systems.
    """

    summary_template = """
    Given the information below about a person, create:
    1. A short summary
    2. Two interesting facts about them

    Information:
    {information}
    """

    prompt = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
    )

    llm = ChatOllama(
        model="llama3.2",
        base_url="http://localhost:11434",
        temperature=0,
    )

    try:
        response = (prompt | llm).invoke({"information": information})
        print(response.content)
    except Exception as exc:
        print("Ollama is not available or the model is not installed yet.")
        print("Run: ollama pull llama3.2")
        print(f"Details: {exc}")


if __name__ == "__main__":
    main()
